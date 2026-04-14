import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("dotenv 模块未安装，将直接使用环境变量")

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import requests
from datetime import datetime, timezone
import openai
from bs4 import BeautifulSoup
from typing import List, Dict
import time
import re
import base64
import json
from common.storage import save_structured_items, build_item_id
from common.scoring import score_content
from common.openai_fallback import chat_completion_content, get_openai_timeout, is_gpt5_model, is_reasoning_model
from common.keyword_utils import (
    investor_keyword_prompt,
    investor_keyword_repair_prompt,
    extract_keywords_from_response,
    finalize_keywords,
    keyword_quality_check,
    synthesize_keywords_from_context,
)

# AI 过滤关键字
AI_KEYWORDS = [
    'ai', 'artificial intelligence', 'machine learning', 'ml',
    'deep learning', 'neural network', 'llm', 'gpt', 'claude',
    'agent', 'autonomous', 'chatbot', 'assistant', 'copilot',
    'generative', 'diffusion', 'transformer', 'embedding',
    'rag', 'retrieval', 'vector', 'semantic search',
    'proactive ai', 'agent infra', 'autonomous agents', 'multi-agent', 'openclaw', 'mcp',
    'context', 'hijacking', 'laude code sdk', 'cowork', 'vibe coding', 'agent-friendly tooling',
    'human-in-the-loop', 'online learning', 'reward model', 'reward fine-tune', 'sft', 'rlhf',
    'rlaif', 'dpo', 'hero user', 'product self-iteration', 'intent prediction', 'non-consensus ai',
    'ai-density', 'agentic workflow', 'workflow'
]

EXCLUDE_KEYWORDS = [
    'crypto', 'nft', 'blockchain', 'web3', 'token',
    'game', 'gaming', 'casino', 'betting',
    'adult', 'dating', 'porn'
]

def _get_int_env(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        value = int(raw)
    except ValueError:
        print(f"警告: 环境变量 {name}={raw!r} 不是整数，回退默认值 {default}")
        return default
    if value <= 0:
        print(f"警告: 环境变量 {name}={raw!r} 必须大于 0，回退默认值 {default}")
        return default
    return value


def _get_request_timeout() -> float:
    return get_openai_timeout(60.0)


def _get_model_name() -> str:
    raw = os.getenv("OPENAI_MODEL", "").strip()
    return raw or "gpt-5.2-2025-12-11"


def _chat_json_content(messages, max_tokens: int, temperature: float) -> str:
    model_name = _get_model_name()
    content, used_model = chat_completion_content(
        client=client,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        json_mode=True,
        default_model=model_name,
        timeout=_get_request_timeout(),
        retry_max_tokens=max(max_tokens, 600 if is_reasoning_model(model_name) else 1200 if is_gpt5_model(model_name) else 300),
    )
    if used_model != model_name:
        print(f"模型回退: {model_name} -> {used_model}")
    return content


def _chat_text_content(messages, max_tokens: int, temperature: float) -> str:
    model_name = _get_model_name()
    content, used_model = chat_completion_content(
        client=client,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        json_mode=False,
        default_model=model_name,
        timeout=_get_request_timeout(),
        retry_max_tokens=max(max_tokens, 600 if is_reasoning_model(model_name) else 900 if is_gpt5_model(model_name) else 260),
    )
    if used_model != model_name:
        print(f"模型回退: {model_name} -> {used_model}")
    return content


def _get_base_url(default: str = "https://api.openai.com/v1") -> str:
    raw = os.getenv("OPENAI_BASE_URL")
    if raw is None or raw.strip() == "":
        return default
    return raw.strip()


def _get_github_token() -> str:
    return (os.getenv("GITHUB_TOKEN", "") or os.getenv("GH_TOKEN", "")).strip()


def _github_headers() -> Dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "CreekStone-SearchBot/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = _get_github_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _clean_readme_text(markdown_text: str, max_chars: int = 1800) -> str:
    """压缩 README 为简短语义片段，避免把代码块/徽章带入关键词和评分。"""
    if not markdown_text:
        return ""
    text = markdown_text
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"^\s{0,3}#{1,6}\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*>\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*[-*+]\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ \t\f\v]+", " ", text)
    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
    blocks: List[str] = []
    total = 0
    for ln in lines:
        # 跳过高度模板化行
        low = ln.lower()
        if (
            low.startswith("license")
            or low.startswith("contributing")
            or low.startswith("table of contents")
            or "shields.io" in low
            or "discord" in low
            or "trendshift" in low
            or "badge" in low
        ):
            continue
        if (
            "pip install" in low
            or "npm install" in low
            or "pnpm install" in low
            or "yarn add" in low
            or "brew install" in low
            or "docker run" in low
            or "curl " in low
            or "git clone" in low
            or "python -m" in low
            or "quickstart" in low
            or low.startswith("installation")
            or low.startswith("getting started")
        ):
            continue
        if len(ln) < 8:
            continue
        if ln.count("|") >= 3:
            continue
        blocks.append(ln)
        total += len(ln) + 1
        if total >= max_chars:
            break
    return "\n".join(blocks)[:max_chars].strip()


def fetch_repo_readme_excerpt(author: str, name: str) -> str:
    """优先使用 GitHub API 获取 README，失败时回退 raw URL。"""
    api_url = f"https://api.github.com/repos/{author}/{name}/readme"
    headers = _github_headers()
    try:
        api_headers = dict(headers)
        api_headers["Accept"] = "application/vnd.github.raw+json"
        resp = requests.get(api_url, headers=api_headers, timeout=20)
        if resp.status_code == 200 and resp.text.strip():
            # 某些网关仍返回 JSON（含 base64 content），这里兼容两种返回。
            payload = None
            try:
                payload = resp.json()
            except Exception:
                payload = None
            if isinstance(payload, dict):
                content = payload.get("content")
                encoding = (payload.get("encoding") or "").lower()
                if content and encoding == "base64":
                    try:
                        decoded = base64.b64decode(content).decode("utf-8", errors="ignore")
                        cleaned = _clean_readme_text(decoded)
                        if cleaned:
                            return cleaned
                    except Exception:
                        pass
            cleaned = _clean_readme_text(resp.text)
            if cleaned:
                return cleaned
    except Exception:
        pass

    raw_candidates = [
        f"https://raw.githubusercontent.com/{author}/{name}/main/README.md",
        f"https://raw.githubusercontent.com/{author}/{name}/master/README.md",
        f"https://raw.githubusercontent.com/{author}/{name}/main/readme.md",
        f"https://raw.githubusercontent.com/{author}/{name}/master/readme.md",
    ]
    for raw_url in raw_candidates:
        try:
            resp = requests.get(raw_url, headers=headers, timeout=20)
            if resp.status_code == 200 and resp.text.strip():
                return _clean_readme_text(resp.text)
        except Exception:
            continue
    return ""


def _build_keyword_source_text(description: str, readme_excerpt: str, max_chars: int = 2600) -> str:
    if readme_excerpt:
        merged = f"{description}\n\n{readme_excerpt}"
    else:
        merged = description
    return merged[:max_chars]


def _contains_any(text: str, keywords) -> bool:
    if not text:
        return False
    lowered = text.lower()
    return any(k in lowered for k in keywords)


def _load_existing_github_rows(date_str: str) -> List[Dict]:
    ndjson_path = Path("data/structured/items.ndjson")
    if not ndjson_path.exists():
        return []
    rows: List[Dict] = []
    try:
        with ndjson_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)
                except Exception:
                    continue
                if str(item.get("source", "")).lower() == "github" and str(item.get("date", "")) == date_str:
                    rows.append(item)
    except Exception:
        return []
    rows.sort(key=lambda x: int(x.get("rank") or 999999))
    return rows


def _parse_author_repo(title: str, url: str) -> tuple[str, str]:
    if "/" in (title or ""):
        author, name = title.split("/", 1)
        return author.strip(), name.strip()
    if "github.com/" in (url or ""):
        try:
            tail = url.split("github.com/", 1)[1].strip("/")
            author, name = tail.split("/", 1)
            return author.strip(), name.strip()
        except Exception:
            pass
    return "", (title or "").strip()


def is_ai_related(*fields: str) -> bool:
    merged = " ".join(filter(None, fields))
    if not merged:
        return False
    if _contains_any(merged, EXCLUDE_KEYWORDS):
        return False
    return _contains_any(merged, AI_KEYWORDS)

# 创建 OpenAI 客户端实例（用于翻译）
api_key = os.getenv('OPENAI_API_KEY')
base_url = _get_base_url()
if api_key:
    try:
        client = openai.Client(api_key=api_key, base_url=base_url)
        print(f"成功初始化 OpenAI 客户端 (使用API地址: {base_url})")
    except Exception as e:
        print(f"初始化 OpenAI 客户端失败: {e}")
        client = None
else:
    print("未设置 OPENAI_API_KEY，将不进行翻译")
    client = None

class GitHubRepo:
    def __init__(self, data: Dict):
        """从爬取的数据初始化仓库对象"""
        self.name = data.get('name', '')
        self.author = data.get('author', '')
        self.url = data.get('url', '')
        self.description = data.get('description', '')
        self.language = data.get('language', 'Unknown')
        self.stars = data.get('stars', 0)
        self.forks = data.get('forks', 0)
        self.stars_today = data.get('stars_today', 0)
        self.readme_excerpt = data.get('readme_excerpt', '') or fetch_repo_readme_excerpt(self.author, self.name)
        
        # 翻译与总结描述（总结优先）
        self.translated_description = self.translate_description()
        self.readme_summary_zh = self.summarize_from_readme()
        self.final_description_zh = self.readme_summary_zh or self.translated_description or self.description
        # 关键词
        self.keywords = self.generate_keywords()
        # 评分
        self.score = score_content(
            (
                f"仓库: {self.author}/{self.name}\n"
                f"描述: {self.description}\n"
                f"README摘录: {self.readme_excerpt[:1200]}\n"
                f"中文介绍: {self.final_description_zh}\n"
                f"关键词: {self.keywords}"
            ),
            client,
            kind="github",
        )

    def to_content_item(self, rank: int, date_str: str) -> dict:
        merged = f"{self.author}/{self.name} {self.description}".lower()
        hit_keywords = [kw for kw in AI_KEYWORDS if kw in merged]
        return {
            "id": build_item_id("gh", date_str, rank),
            "source": "github",
            "date": date_str,
            "rank": rank,
            "title": f"{self.author}/{self.name}",
            "url": self.url,
            "detail_url": self.url,
            "description_en": self.description,
            "description_zh": self.final_description_zh,
            "keywords": [k.strip() for k in self.keywords.split(",") if k.strip()],
            "tags": [self.language],
            "metrics": {
                "stars": self.stars,
                "forks": self.forks,
                "stars_today": self.stars_today,
            },
            "media": {"image": None},
            "ai_flags": {"is_ai": True, "hit_keywords": hit_keywords, "hit_excludes": []},
            "score": self.score,
            "raw": {
                "readme_excerpt": self.readme_excerpt,
                "translated_description": self.translated_description,
                "readme_summary_zh": self.readme_summary_zh,
            },
        }
    
    def translate_description(self) -> str:
        """使用AI翻译项目描述"""
        if not self.description or client is None:
            return self.description
        
        try:
            print(f"正在翻译 {self.author}/{self.name} 的描述...")
            translated = _chat_text_content(
                messages=[
                    {"role": "system", "content": "你是技术产品说明书撰写者。"},
                    {"role": "user", "content": (
                        "请将下面的 GitHub 项目简介翻译成中文，并在 2-3 句里补充：主要功能、目标用户/场景、使用的核心技术（尤其是 AI 相关）。"
                        "保持简洁、准确、信息量更高。\n\n"
                        f"{self.description}"
                    )}
                ],
                max_tokens=700 if is_gpt5_model(_get_model_name()) else 200,
                temperature=0.7,
            )
            translated = (translated or "").strip()
            print(f"成功翻译")
            return translated or self.description
        except Exception as e:
            print(f"翻译失败: {e}")
            return self.description

    def summarize_from_readme(self) -> str:
        """基于 README + 描述生成中文项目总结，忽略安装/徽章等噪音。"""
        source_text = _build_keyword_source_text(self.description, self.readme_excerpt, max_chars=3000)
        if not source_text or client is None:
            return self.translated_description
        try:
            print(f"正在总结 {self.author}/{self.name} 的README...")
            content = _chat_text_content(
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "你是技术研究助手。请根据输入生成简洁、可比较的中文项目介绍。"
                            "重点写：做什么、面向谁、关键技术与典型场景。"
                            "忽略安装教程、命令、徽章、贡献指南、许可证、版本历史。"
                        ),
                    },
                    {
                        "role": "user",
                        "content": (
                            "请用 2-4 句中文输出，不要分点，不要加标题。\n"
                            "信息不足时可保守，但不要编造。\n\n"
                            f"{source_text}"
                        ),
                    },
                ],
                max_tokens=700 if is_gpt5_model(_get_model_name()) else 260,
                temperature=0.3,
            )
            result = (content or "").strip()
            if not result:
                return self.translated_description
            return result
        except Exception as e:
            print(f"README总结失败: {e}")
            return self.translated_description

    def generate_keywords(self) -> str:
        """生成中性关键词：贴合内容，术语统一，减少英文噪音。"""
        try:
            source_text = _build_keyword_source_text(self.description, self.readme_excerpt)
            base_text = f"{self.author}/{self.name}\n{source_text}"
            if client is None:
                words = (self.name + ", " + source_text).replace("&", ",").replace("|", ",").replace("-", ",").split(",")
                filtered = finalize_keywords([w.strip() for w in words if w.strip()], base_text, source="github")
                ok, _ = keyword_quality_check(filtered, base_text, source="github")
                if not ok:
                    filtered = synthesize_keywords_from_context(base_text, source="github", max_items=10)
                return ", ".join(filtered)

            raw = _chat_json_content(
                messages=investor_keyword_prompt(
                    subject="Open Source Repository",
                    title=f"{self.author}/{self.name}",
                    subtitle=f"Language: {self.language}",
                    description=source_text,
                ),
                max_tokens=1200 if is_gpt5_model(_get_model_name()) else 220,
                temperature=0.3,
            )
            items = extract_keywords_from_response(raw)
            items = finalize_keywords(items, base_text, source="github")
            ok, reason = keyword_quality_check(items, base_text, source="github")
            if not ok:
                repaired_raw = _chat_json_content(
                    messages=investor_keyword_repair_prompt(
                        subject="Open Source Repository",
                        title=f"{self.author}/{self.name}",
                        subtitle=f"Language: {self.language}",
                        description=source_text,
                        bad_keywords=items,
                        reason=reason,
                    ),
                    max_tokens=1000 if is_gpt5_model(_get_model_name()) else 220,
                    temperature=0.2,
                )
                repaired = extract_keywords_from_response(repaired_raw)
                repaired = finalize_keywords(repaired, base_text, source="github")
                repaired_ok, _ = keyword_quality_check(repaired, base_text, source="github")
                if repaired_ok:
                    items = repaired
                else:
                    items = synthesize_keywords_from_context(base_text, source="github", max_items=10)
            if not items:
                items = synthesize_keywords_from_context(base_text, source="github", max_items=10)
            return ", ".join(dict.fromkeys(items))
        except Exception as e:
            print(f"关键词生成失败: {e}")
            source_text = _build_keyword_source_text(self.description, self.readme_excerpt)
            base_text = f"{self.author}/{self.name}\n{source_text}"
            fallback = finalize_keywords([self.name, source_text], base_text, source="github")
            ok, _ = keyword_quality_check(fallback, base_text, source="github")
            if not ok:
                fallback = synthesize_keywords_from_context(base_text, source="github", max_items=10)
            return ", ".join(fallback)
    
    def to_markdown(self, rank: int) -> str:
        """转换为Markdown格式"""
        # 格式化星标数
        def format_number(num):
            if num >= 1000:
                return f"{num/1000:.1f}k"
            return str(num)
        
        stars_display = format_number(self.stars)
        forks_display = format_number(self.forks)
        
        # 今日新增星标
        today_stars = f" (+{format_number(self.stars_today)} today)" if self.stars_today > 0 else ""
        
        return f"""## [{rank}. {self.author}/{self.name}]({self.url})

**语言**: {self.language}  
**Stars**: ⭐ {stars_display}{today_stars} | **Forks**: 🔱 {forks_display}

**原始描述**: {self.description}

**中文介绍（README总结）**: {self.final_description_zh}

**关键词**: {self.keywords}

**评分**: {self.score.get('total', 0)}

**项目地址**: [GitHub]({self.url})

---

"""

def fetch_github_trending(language: str = "", since: str = "daily", max_results: int = 25) -> List[GitHubRepo]:
    """
    爬取GitHub Trending页面
    
    参数:
        language: 编程语言过滤 (如 "python", "javascript", "" 表示所有)
        since: 时间范围 ("daily", "weekly", "monthly")
    """
    base_url = "https://github.com/trending"
    
    # 构建URL
    if language:
        url = f"{base_url}/{language}"
    else:
        url = base_url
    
    params = {"since": since}
    
    print(f"正在从GitHub Trending获取数据...")
    print(f"语言: {language if language else '全部'}, 时间范围: {since}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找所有仓库条目
        repos = []
        articles = soup.find_all('article', class_='Box-row')
        
        print(f"找到 {len(articles)} 个仓库")
        
        for article in articles:
            try:
                # 提取仓库信息
                h2 = article.find('h2', class_='h3')
                if not h2:
                    continue
                
                a_tag = h2.find('a')
                if not a_tag:
                    continue
                
                # 仓库全名 (author/repo)
                full_name = a_tag.get('href', '').strip('/')
                if '/' not in full_name:
                    continue
                
                author, name = full_name.split('/', 1)
                
                # 描述
                desc_tag = article.find('p', class_='col-9')
                description = desc_tag.get_text(strip=True) if desc_tag else ''
                
                # 语言
                lang_tag = article.find('span', attrs={'itemprop': 'programmingLanguage'})
                language = lang_tag.get_text(strip=True) if lang_tag else 'Unknown'
                
                # 星标数
                star_tag = article.find('svg', class_='octicon-star')
                if star_tag:
                    star_parent = star_tag.find_parent('a')
                    stars_text = star_parent.get_text(strip=True) if star_parent else '0'
                    stars = parse_number(stars_text)
                else:
                    stars = 0
                
                # Fork数
                fork_tag = article.find('svg', class_='octicon-repo-forked')
                if fork_tag:
                    fork_parent = fork_tag.find_parent('a')
                    forks_text = fork_parent.get_text(strip=True) if fork_parent else '0'
                    forks = parse_number(forks_text)
                else:
                    forks = 0
                
                # 今日新增星标
                today_stars_tag = article.find('span', class_='d-inline-block float-sm-right')
                stars_today = 0
                if today_stars_tag:
                    today_text = today_stars_tag.get_text(strip=True)
                    stars_today = parse_number(today_text.split()[0])
                
                repo_data = {
                    'name': name,
                    'author': author,
                    'url': f"https://github.com/{full_name}",
                    'description': description,
                    'language': language,
                    'stars': stars,
                    'forks': forks,
                    'stars_today': stars_today
                }

                # 尝试引入 README 以增强后续关键词/评分与 AI 过滤。
                readme_excerpt = fetch_repo_readme_excerpt(author, name)
                repo_data["readme_excerpt"] = readme_excerpt

                # AI 相关筛选
                if not is_ai_related(name, description, readme_excerpt):
                    print(f"跳过非AI仓库: {author}/{name}")
                    continue
                
                repos.append(GitHubRepo(repo_data))
                if len(repos) >= max_results:
                    print(f"达到最大数量限制: {max_results}")
                    break
                
            except Exception as e:
                print(f"解析仓库信息时出错: {e}")
                continue
        
        if not repos:
            print("未能解析到任何仓库，使用模拟数据...")
            return get_mock_repos()
        
        print(f"成功解析 {len(repos)} 个仓库")
        return repos
        
    except Exception as e:
        print(f"获取GitHub Trending失败: {e}")
        print("使用模拟数据...")
        return get_mock_repos()

def parse_number(text: str) -> int:
    """解析GitHub上的数字格式 (如 "1.2k" -> 1200)"""
    text = text.strip().replace(',', '')
    if 'k' in text.lower():
        return int(float(text.lower().replace('k', '')) * 1000)
    try:
        return int(text)
    except:
        return 0

def get_mock_repos() -> List[GitHubRepo]:
    """返回模拟数据用于测试"""
    mock_data = [
        {
            'name': 'awesome-project',
            'author': 'test-user',
            'url': 'https://github.com/test-user/awesome-project',
            'description': 'An awesome project for demonstration purposes',
            'language': 'Python',
            'stars': 12500,
            'forks': 2300,
            'stars_today': 150
        }
    ]
    return [GitHubRepo(data) for data in mock_data]


def reprocess_existing_github(date_str: str, max_results: int = 25) -> List[GitHubRepo]:
    """使用当前逻辑重处理指定日期已存在的 GitHub 条目（不重抓 Trending 列表）。"""
    rows = _load_existing_github_rows(date_str)
    if not rows:
        print(f"未找到 {date_str} 的已有 GitHub 条目，回退到实时抓取。")
        return fetch_github_trending(language="", since="daily", max_results=max_results)

    repos: List[GitHubRepo] = []
    for row in rows[:max_results]:
        title = str(row.get("title", ""))
        url = str(row.get("url", ""))
        author, name = _parse_author_repo(title, url)
        metrics = row.get("metrics") or {}
        tags = row.get("tags") or []
        language = tags[0] if isinstance(tags, list) and tags else "Unknown"
        data = {
            "name": name,
            "author": author,
            "url": url,
            "description": str(row.get("description_en", "")),
            "language": language,
            "stars": int((metrics.get("stars") or 0)),
            "forks": int((metrics.get("forks") or 0)),
            "stars_today": int((metrics.get("stars_today") or 0)),
        }
        try:
            repos.append(GitHubRepo(data))
        except Exception as e:
            print(f"重处理失败: {title} -> {e}")
            continue
    print(f"已重处理 {len(repos)} 个已有 GitHub 条目（{date_str}）")
    return repos

def generate_markdown(repos: List[GitHubRepo], date_str: str, language: str = "", since: str = "daily"):
    """生成Markdown文件并保存到data/github目录"""
    
    # 时间范围中文
    since_cn = {"daily": "日榜", "weekly": "周榜", "monthly": "月榜"}.get(since, "日榜")
    
    # 语言过滤
    lang_display = f"{language.upper()} " if language else ""
    
    markdown_content = f"# GitHub Trending {lang_display}{since_cn} | {date_str}\n\n"
    markdown_content += f"> 共 {len(repos)} 个项目\n\n"
    
    # 按语言分组
    repos_by_language = {}
    for repo in repos:
        lang = repo.language
        if lang not in repos_by_language:
            repos_by_language[lang] = []
        repos_by_language[lang].append(repo)
    
    # 生成目录
    markdown_content += "## 📑 目录\n\n"
    for lang in sorted(repos_by_language.keys()):
        markdown_content += f"- [{lang}](#{lang.replace(' ', '-').replace('+', 'plus').replace('#', 'sharp')}) ({len(repos_by_language[lang])} 个项目)\n"
    markdown_content += "\n---\n\n"
    
    # 按语言生成内容
    rank = 1
    structured_items = []
    for lang in sorted(repos_by_language.keys()):
        markdown_content += f"## {lang}\n\n"
        for repo in repos_by_language[lang]:
            markdown_content += repo.to_markdown(rank)
            structured_items.append(repo.to_content_item(rank, date_str))
            rank += 1
    
    # 确保data/github目录存在
    os.makedirs('data/github', exist_ok=True)
    
    # 保存文件
    lang_suffix = f"-{language}" if language else ""
    file_name = f"data/github/github-trending{lang_suffix}-{date_str}.md"
    
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    print(f"文件 {file_name} 生成成功。")
    save_structured_items(date_str, structured_items)

def main():
    """主函数"""
    target_date = os.getenv("GITHUB_TARGET_DATE", "").strip()
    if target_date:
        date_str = target_date
    else:
        today = datetime.now(timezone.utc)
        date_str = today.strftime('%Y-%m-%d')
    
    # 从环境变量读取配置
    language = os.getenv('GITHUB_LANGUAGE', '')  # 留空表示所有语言
    since = os.getenv('GITHUB_SINCE', 'daily')  # daily, weekly, monthly
    max_results = _get_int_env('GITHUB_MAX_RESULTS', 25)
    reprocess_existing = os.getenv("GITHUB_REPROCESS_EXISTING", "").strip().lower() == "true"
    
    print(f"=== GitHub Trending 爬取开始 ===")
    print(f"日期: {date_str}")
    print(f"语言: {language if language else '全部'}")
    print(f"时间范围: {since}")
    print(f"重处理已有数据: {'是' if reprocess_existing else '否'}")
    
    if reprocess_existing:
        repos = reprocess_existing_github(date_str=date_str, max_results=max_results)
    else:
        # 获取trending仓库
        repos = fetch_github_trending(language=language, since=since, max_results=max_results)
    
    # 生成Markdown
    generate_markdown(repos, date_str, language, since)
    
    print(f"=== GitHub Trending 爬取完成 ===")

if __name__ == "__main__":
    main()
