import os
import signal
import time
from typing import List, Tuple


def get_openai_timeout(default: float = 60.0) -> float:
    raw = os.getenv("OPENAI_REQUEST_TIMEOUT", "").strip()
    if not raw:
        return default
    try:
        value = float(raw)
        if value > 0:
            return value
    except Exception:
        pass
    return default


def get_openai_retry_attempts(default: int = 5) -> int:
    raw = os.getenv("OPENAI_RETRY_ATTEMPTS", "").strip()
    if not raw:
        return default
    try:
        value = int(raw)
        if value > 0:
            return value
    except Exception:
        pass
    return default


def get_openai_retry_base_delay(default: float = 1.5) -> float:
    raw = os.getenv("OPENAI_RETRY_BASE_DELAY", "").strip()
    if not raw:
        return default
    try:
        value = float(raw)
        if value > 0:
            return value
    except Exception:
        pass
    return default


def is_gpt5_model(model_name: str) -> bool:
    return (model_name or "").startswith("gpt-5")


def is_reasoning_model(model_name: str) -> bool:
    """思维链推理模型：内部有 thinking 过程，需要更多 max_tokens，答案可能在 reasoning 字段。"""
    m = (model_name or "").lower()
    return any(kw in m for kw in (
        "glm-5", "glm-z",           # Z.AI GLM-5.x / GLM-Z
        "kimi-k2", "moonshot",       # Kimi K2.x
        "minimax-m2", "minimax/m2",  # MiniMax M2.x
        "o1", "o3", "o4",            # OpenAI o-series
        "deepseek-r",                # DeepSeek-R
    ))


def _normalize_model_name(raw: str) -> str:
    # Guard against malformed .env lines like:
    # OPENAI_MODEL_ALTERNATE_2=gpt-4o-mini OPENAI_REQUEST_TIMEOUT=90
    token = (raw or "").strip()
    if not token:
        return ""
    token = token.split()[0].strip().strip(",;")
    return token


def get_model_candidates(default_model: str) -> List[str]:
    values = [
        os.getenv("OPENAI_MODEL", ""),
        os.getenv("OPENAI_MODEL_ALTERNATE_1", ""),
        os.getenv("OPENAI_MODEL_ALTERNATE_2", ""),
        default_model,
    ]
    out: List[str] = []
    seen = set()
    for raw in values:
        model = _normalize_model_name(raw)
        if not model or model in seen:
            continue
        seen.add(model)
        out.append(model)
    return out


def _is_retryable_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    return (
        "timed out" in msg
        or "timeout" in msg
        or "rate limit" in msg
        or "too many requests" in msg
        or "429" in msg
        or "temporarily unavailable" in msg
        or "service unavailable" in msg
        or "upstream overloaded" in msg
        or "upstream load" in msg
        or "overloaded" in msg
        or "saturated" in msg
        or "稍后再试" in msg
        or "负载已饱和" in msg
        or "当前分组上游负载已饱和" in msg
    )


def _is_model_unavailable_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    return (
        "model_not_found" in msg
        or "no available channel for model" in msg
        or "does not exist" in msg
        or "unsupported model" in msg
    )


def _call_with_hard_timeout(fn, timeout_sec: float):
    if timeout_sec <= 0:
        return fn()
    if not hasattr(signal, "setitimer") or not hasattr(signal, "SIGALRM"):
        return fn()

    def _handler(_signum, _frame):
        raise TimeoutError(f"request timed out after {timeout_sec}s")

    old = signal.getsignal(signal.SIGALRM)
    signal.signal(signal.SIGALRM, _handler)
    signal.setitimer(signal.ITIMER_REAL, timeout_sec)
    try:
        return fn()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, old)


def _retry_sleep_seconds(attempt_index: int) -> float:
    base = get_openai_retry_base_delay()
    return min(20.0, base * (2 ** attempt_index))


def _create_with_retry(client, kwargs: dict, timeout: float):
    last_exc = None
    attempts = get_openai_retry_attempts()
    for attempt in range(attempts):
        try:
            try:
                return _call_with_hard_timeout(
                    lambda: client.chat.completions.create(**kwargs),
                    timeout + 2,
                )
            except TypeError:
                # Some gateways do not support reasoning_effort.
                cleaned = dict(kwargs)
                cleaned.pop("reasoning_effort", None)
                return _call_with_hard_timeout(
                    lambda: client.chat.completions.create(**cleaned),
                    timeout + 2,
                )
        except Exception as exc:
            last_exc = exc
            if attempt < attempts - 1 and _is_retryable_error(exc):
                time.sleep(_retry_sleep_seconds(attempt))
                continue
            raise
    raise last_exc if last_exc else RuntimeError("chat completion failed")


def create_embeddings_with_retry(
    *,
    client,
    model: str,
    input_texts,
    timeout: float | None = None,
):
    timeout = timeout if timeout is not None else get_openai_timeout()
    last_exc = None
    attempts = get_openai_retry_attempts()
    for attempt in range(attempts):
        try:
            return _call_with_hard_timeout(
                lambda: client.embeddings.create(model=model, input=input_texts, timeout=timeout),
                timeout + 2,
            )
        except TypeError:
            try:
                return _call_with_hard_timeout(
                    lambda: client.embeddings.create(model=model, input=input_texts),
                    timeout + 2,
                )
            except Exception as exc:
                last_exc = exc
                if attempt < attempts - 1 and _is_retryable_error(exc):
                    time.sleep(_retry_sleep_seconds(attempt))
                    continue
                raise
        except Exception as exc:
            last_exc = exc
            if attempt < attempts - 1 and _is_retryable_error(exc):
                time.sleep(_retry_sleep_seconds(attempt))
                continue
            raise
    raise last_exc if last_exc else RuntimeError("embedding request failed")


def chat_completion_content(
    *,
    client,
    messages,
    max_tokens: int,
    temperature: float,
    json_mode: bool,
    default_model: str,
    timeout: float | None = None,
    retry_max_tokens: int | None = None,
) -> Tuple[str, str]:
    timeout = timeout if timeout is not None else get_openai_timeout()
    candidates = get_model_candidates(default_model)
    last_exc = None

    consecutive_empty = 0  # 连续空响应计数，超阈值直接放弃省 token

    for model in candidates:
        for pass_index in range(2):
            # 推理模型需要足够 token 完成思考 + 输出答案，但设上限避免浪费
            effective_max = max_tokens if pass_index == 0 else (retry_max_tokens or max_tokens)
            if is_reasoning_model(model):
                effective_max = min(max(effective_max, 800), 1800)  # [800, 1800]

            kwargs = {
                "model": model,
                "messages": messages,
                "max_tokens": effective_max,
                "temperature": temperature,
                "timeout": timeout,
            }
            if is_gpt5_model(model):
                kwargs["reasoning_effort"] = "low"
            # 推理模型（MiniMax/GLM/Kimi）不使用 response_format，靠 prompt 指令输出 JSON
            # json_mode 仅对非推理模型且第一次 pass 时生效
            if json_mode and pass_index == 0 and not is_reasoning_model(model):
                kwargs["response_format"] = {"type": "json_object"}

            try:
                resp = _create_with_retry(client, kwargs, timeout)
                content = (resp.choices[0].message.content or "").strip()
                # 推理模型答案可能在 reasoning 字段（content 为空时兜底）
                if not content:
                    reasoning = getattr(resp.choices[0].message, "reasoning", None) or ""
                    if reasoning.strip():
                        content = reasoning.strip().splitlines()[-1].strip()
                if content:
                    return content, model
                # 空响应：短暂等待后重试（MiniMax rate limit 时返回空而非 429）
                consecutive_empty += 1
                time.sleep(3)
                if consecutive_empty >= 3:
                    raise RuntimeError("all models returned empty content (fast-fail to save tokens)")
            except Exception as exc:
                last_exc = exc
                if _is_model_unavailable_error(exc) or _is_retryable_error(exc):
                    break
                raise

    if last_exc:
        raise last_exc
    raise RuntimeError("all models returned empty content")
