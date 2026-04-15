import os
try:
    from dotenv import load_dotenv
    # 加载 .env 文件
    load_dotenv()
except ImportError:
    # 在 GitHub Actions 等环境中，环境变量已经设置好，不需要 dotenv
    print("dotenv 模块未安装，将直接使用环境变量")

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import requests
import time
from datetime import datetime, timedelta, timezone
import openai
from bs4 import BeautifulSoup
import pytz
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
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

# AI 相关筛选与关键词控制
AI_KEYWORDS = [
    'ai', 'artificial intelligence', 'machine learning', 'ml',
    'deep learning', 'neural network', 'llm', 'gpt', 'claude',
    'agent', 'autonomous', 'chatbot', 'assistant', 'copilot',
    'generative', 'diffusion', 'transformer', 'embedding',
    'rag', 'retrieval', 'vector', 'semantic search',
    # 新增 agent/AI 相关长尾词
    'proactive ai', 'agent infra', 'autonomous agents', 'multi-agent', 'openclaw', 'mcp',
    'context', 'hijacking', 'laude code sdk', 'cowork', 'vibe coding', 'agent-friendly tooling',
    'human-in-the-loop', 'online learning', 'reward model', 'reward fine-tune', 'sft', 'rlhf',
    'rlaif', 'dpo', 'hero user', 'product self-iteration', 'intent prediction', 'non-consensus ai',
    'ai-density', 'agentic workflow', 'workflow'
]

EXCLUDE_KEYWORDS = [
    'crypto', 'nft', 'blockchain', 'web3', 'porn'
]

def _allow_mock_data() -> bool:
    return os.getenv("ALLOW_MOCK_DATA", "").strip().lower() == "true"


def _get_request_timeout() -> float:
    return get_openai_timeout(60.0)


def _get_base_url(default: str = "https://api.openai.com/v1") -> str:
    raw = os.getenv("OPENAI_BASE_URL")
    if raw is None or raw.strip() == "":
        return default
    return raw.strip()


def _get_model_name() -> str:
    raw = os.getenv("OPENAI_MODEL", "").strip()
    return raw or "gpt-5.2-2025-12-11"


def _looks_mostly_ascii(text: str) -> bool:
    if not text:
        return True
    ascii_chars = sum(1 for ch in text if ch.isascii())
    return ascii_chars / max(1, len(text)) > 0.85


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


def _get_http_timeout(default: float = 45.0) -> float:
    raw = os.getenv("PRODUCTHUNT_HTTP_TIMEOUT", "").strip()
    if not raw:
        return default
    try:
        value = float(raw)
    except ValueError:
        return default
    return value if value > 0 else default


def _get_max_posts(default: int = 30) -> int:
    raw = os.getenv("PRODUCTHUNT_MAX_POSTS", "").strip()
    if not raw:
        return default
    try:
        value = int(raw)
    except Exception:
        return default
    return max(1, min(100, value))


def _get_translate_retries(default: int = 3) -> int:
    raw = os.getenv("PRODUCTHUNT_TRANSLATE_RETRIES", "").strip()
    if not raw:
        return default
    try:
        value = int(raw)
    except Exception:
        return default
    return max(1, min(5, value))


def _contains_any(text: str, keywords) -> bool:
    if not text:
        return False
    lowered = text.lower()
    return any(k in lowered for k in keywords)


def is_ai_related(*fields: str) -> bool:
    """Return True when text contains at least one AI keyword and no excluded keyword."""
    merged = " ".join(filter(None, fields))
    if not merged:
        return False
    if _contains_any(merged, EXCLUDE_KEYWORDS):
        return False
    return _contains_any(merged, AI_KEYWORDS)

# 创建 OpenAI 客户端实例
api_key = os.getenv('OPENAI_API_KEY')
base_url = _get_base_url()  # 默认使用官方API地址
if not api_key:
    print("警告: 未设置 OPENAI_API_KEY 环境变量，将无法使用 OpenAI 服务")
    client = None
else:
    openai.api_key = api_key
    try:
        client = openai.Client(api_key=api_key, base_url=base_url)  # 支持自定义API地址
        print(f"成功初始化 OpenAI 客户端 (使用API地址: {base_url})")
    except Exception as e:
        print(f"初始化 OpenAI 客户端失败: {e}")
        client = None

class Product:
    def __init__(self, id: str, name: str, tagline: str, description: str, votesCount: int, createdAt: str, featuredAt: str, website: str, url: str, media=None, **kwargs):
        self.product_id = str(id)
        self.name = name
        self.tagline = tagline
        self.description = description
        self.votes_count = votesCount
        self.created_at = self.convert_to_beijing_time(createdAt)
        self.is_featured = bool(featuredAt)
        self.featured = "是" if featuredAt else "否"
        self.website = website
        self.url = url
        self.og_image_url = self.get_image_url_from_media(media)
        # 合并翻译：tagline + description 一次 LLM 调用，省 50% token
        self.translated_tagline, self.translated_description = self.translate_both(
            self.tagline, self.description
        )
        self.keyword = self.generate_keywords()
        self._score_cache = None

    def get_image_url_from_media(self, media):
        """从API返回的media字段中获取图片URL"""
        try:
            if media and isinstance(media, list) and len(media) > 0:
                # 优先使用第一张图片
                image_url = media[0].get('url', '')
                if image_url:
                    print(f"成功从API获取图片URL: {self.name}")
                    return image_url
            
            # 如果API没有返回图片，尝试使用备用方法
            print(f"API未返回图片，尝试使用备用方法: {self.name}")
            backup_url = self.fetch_og_image_url()
            if backup_url:
                print(f"使用备用方法获取图片URL成功: {self.name}")
                return backup_url
            else:
                print(f"无法获取图片URL: {self.name}")
                
            return ""
        except Exception as e:
            print(f"获取图片URL时出错: {self.name}, 错误: {e}")
            return ""

    def fetch_og_image_url(self) -> str:
        """获取产品的Open Graph图片URL（备用方法）"""
        try:
            response = requests.get(self.url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # 查找og:image meta标签
                og_image = soup.find("meta", property="og:image")
                if og_image:
                    return og_image["content"]
                # 备用:查找twitter:image meta标签
                twitter_image = soup.find("meta", name="twitter:image") 
                if twitter_image:
                    return twitter_image["content"]
            return ""
        except Exception as e:
            print(f"获取OG图片URL时出错: {self.name}, 错误: {e}")
            return ""

    def generate_keywords(self) -> str:
        """生成中性关键词：贴合内容，术语统一，减少英文噪音。"""
        try:
            zh_tagline = (self.translated_tagline or "").strip()
            zh_desc = (self.translated_description or "").strip()
            context = f"{self.name}\n{zh_tagline or self.tagline}\n{zh_desc or self.description}"
            prompt_desc = self.description
            if zh_desc:
                prompt_desc = f"{self.description}\n中文参考: {zh_desc}"

            # 如果 OpenAI 客户端不可用，直接使用备用方法
            if client is None:
                print(f"OpenAI 客户端不可用，使用备用关键词生成方法: {self.name}")
                words = (self.name + ", " + self.tagline + ", " + self.description).replace("&", ",").replace("|", ",").replace("-", ",").split(",")
                rough = [w.strip() for w in words if w.strip()]
                normalized = finalize_keywords(rough, context, source="producthunt")
                ok, _ = keyword_quality_check(normalized, context, source="producthunt")
                if not ok:
                    normalized = synthesize_keywords_from_context(context, source="producthunt", max_items=10)
                return ", ".join(normalized)

            try:
                print(f"正在为 {self.name} 生成关键词...")
                raw = _chat_json_content(
                    messages=investor_keyword_prompt(
                        subject="Product",
                        title=self.name,
                        subtitle=zh_tagline or self.tagline,
                        description=prompt_desc,
                    ),
                    max_tokens=1200 if is_gpt5_model(_get_model_name()) else 220,
                    temperature=0.3,
                )
                keywords_list = extract_keywords_from_response(raw)
                keywords_list = finalize_keywords(keywords_list, context, source="producthunt")
                ok, reason = keyword_quality_check(keywords_list, context, source="producthunt")
                if not ok:
                    repaired_raw = _chat_json_content(
                        messages=investor_keyword_repair_prompt(
                            subject="Product",
                            title=self.name,
                            subtitle=zh_tagline or self.tagline,
                            description=prompt_desc,
                            bad_keywords=keywords_list,
                            reason=reason,
                        ),
                        max_tokens=1000 if is_gpt5_model(_get_model_name()) else 220,
                        temperature=0.2,
                    )
                    repaired = extract_keywords_from_response(repaired_raw)
                    repaired = finalize_keywords(repaired, context, source="producthunt")
                    repaired_ok, _ = keyword_quality_check(repaired, context, source="producthunt")
                    if repaired_ok:
                        keywords_list = repaired
                    else:
                        keywords_list = synthesize_keywords_from_context(context, source="producthunt", max_items=10)
                if not keywords_list:
                    keywords_list = synthesize_keywords_from_context(context, source="producthunt", max_items=10)
                keywords = ", ".join(keywords_list)
                print(f"成功为 {self.name} 生成关键词")
                return keywords
            except Exception as e:
                print(f"OpenAI API 调用失败，使用备用关键词生成方法: {e}")
                # 备用方法：从标题和标语中提取关键词
                words = (self.name + ", " + self.tagline + ", " + self.description).replace("&", ",").replace("|", ",").replace("-", ",").split(",")
                filtered = finalize_keywords([w.strip() for w in words if w.strip()], context, source="producthunt")
                ok, _ = keyword_quality_check(filtered, context, source="producthunt")
                if not ok:
                    filtered = synthesize_keywords_from_context(context, source="producthunt", max_items=10)
                return ", ".join(filtered)
        except Exception as e:
            print(f"关键词生成失败: {e}")
            fallback_context = f"{self.name}\n{self.tagline}\n{self.description}"
            fallback = finalize_keywords([self.name, self.tagline], fallback_context, source="producthunt")
            ok, _ = keyword_quality_check(fallback, fallback_context, source="producthunt")
            if not ok:
                fallback = synthesize_keywords_from_context(fallback_context, source="producthunt", max_items=10)
            return ", ".join(fallback)

    def translate_both(self, tagline: str, description: str):
        """一次 LLM 调用同时翻译 tagline 和 description，省 50% token。"""
        if client is None:
            return tagline, description
        t = (tagline or "").strip()
        d = (description or "").strip()
        if not t and not d:
            return tagline, description
        try:
            print(f"正在翻译 {self.name} 的内容...")
            prompt = f"请将以下两段内容分别翻译成地道中文，保留技术术语。严格按格式输出，不要多余文字：\n标语：{t}\n介绍：{d}"
            raw = _chat_text_content(
                messages=[
                    {"role": "system", "content": "你是专业中英翻译，只输出翻译结果，格式为：标语：xxx\n介绍：xxx"},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=600 if is_gpt5_model(_get_model_name()) else 400,
                temperature=0.2,
            )
            zh_tagline, zh_desc = t, d
            for line in raw.splitlines():
                line = line.strip()
                if line.startswith("标语："):
                    zh_tagline = line[3:].strip() or t
                elif line.startswith("介绍："):
                    zh_desc = line[3:].strip() or d
            print(f"成功翻译 {self.name} 的内容")
            return zh_tagline, zh_desc
        except Exception as e:
            print(f"翻译失败，回退原文: {e}")
            return tagline, description

    def translate_text(self, text: str) -> str:
        """使用OpenAI翻译文本内容"""
        try:
            if not text or not text.strip():
                return text
            # 如果 OpenAI 客户端不可用，直接返回原文
            if client is None:
                print(f"OpenAI 客户端不可用，无法翻译: {self.name}")
                return text
                
            try:
                print(f"正在翻译 {self.name} 的内容...")
                for _ in range(_get_translate_retries(3)):
                    translated_text = _chat_text_content(
                        messages=[
                            {"role": "system", "content": "你是专业中英翻译。请将输入准确翻译成地道中文，保留必要技术术语。只输出翻译结果。"},
                            {"role": "user", "content": text},
                        ],
                        max_tokens=1200 if is_gpt5_model(_get_model_name()) else 500,
                        temperature=0.2,
                    )
                    if translated_text and len(translated_text) >= 4:
                        # 若几乎全英文，继续重试一次
                        if _looks_mostly_ascii(translated_text):
                            continue
                        print(f"成功翻译 {self.name} 的内容")
                        return translated_text
                print(f"翻译结果为空或质量不足，回退原文: {self.name}")
                return text
            except Exception as e:
                print(f"OpenAI API 翻译失败: {e}")
                # 如果 API 调用失败，返回原文
                return text
        except Exception as e:
            print(f"翻译过程中出错: {e}")
            return text

    def convert_to_beijing_time(self, utc_time_str: str) -> str:
        """将UTC时间转换为北京时间"""
        utc_time = datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%SZ')
        beijing_tz = pytz.timezone('Asia/Shanghai')
        beijing_time = utc_time.replace(tzinfo=pytz.utc).astimezone(beijing_tz)
        return beijing_time.strftime('%Y年%m月%d日 %p%I:%M (北京时间)')

    def to_markdown(self, rank: int) -> str:
        """返回产品数据的Markdown格式"""
        og_image_markdown = f"![{self.name}]({self.og_image_url})"
        # 评分缓存复用，避免同一条目重复调用模型。
        score = self._get_score()
        total_score = score.get("total", 0)
        return (
            f"## [{rank}. {self.name}]({self.url})\n"
            f"**标语**：{self.translated_tagline}\n"
            f"**介绍**：{self.translated_description}\n"
            f"**产品网站**: [立即访问]({self.website})\n"
            f"**Product Hunt**: [View on Product Hunt]({self.url})\n\n"
            f"{og_image_markdown}\n\n"
            f"**关键词**：{self.keyword}\n"
            f"**票数**: 🔺{self.votes_count}\n"
            f"**是否精选**：{self.featured}\n"
            f"**发布时间**：{self.created_at}\n"
            f"**评分**：{total_score}\n\n"
            f"---\n\n"
        )

    def to_content_item(self, rank: int, date_str: str, extra_tags=None, featured_rank: int | None = None) -> dict:
        merged_text = f"{self.name} {self.tagline} {self.description}".lower()
        hit_keywords = [kw for kw in AI_KEYWORDS if kw in merged_text]
        score = self._get_score()
        tags = ["Product Hunt", "daily_ai"]
        if extra_tags:
            for tag in extra_tags:
                if tag and tag not in tags:
                    tags.append(tag)
        metrics = {"votes": self.votes_count, "featured": self.featured}
        if featured_rank is not None:
            metrics["featured_rank"] = int(featured_rank)
        metrics["product_id"] = self.product_id
        return {
            "id": build_item_id("ph", date_str, rank),
            "source": "producthunt",
            "date": date_str,
            "rank": rank,
            "title": self.name,
            "url": self.url,
            "detail_url": self.website,
            "description_en": self.description,
            "description_zh": self.translated_description,
            "keywords": [k.strip() for k in self.keyword.split(",") if k.strip()],
            "tags": tags,
            "metrics": metrics,
            "media": {"image": self.og_image_url},
            "ai_flags": {"is_ai": True, "hit_keywords": hit_keywords, "hit_excludes": []},
            "score": score,
            "raw": {
                "tagline": self.tagline,
                "created_at": self.created_at,
            },
        }

    def _get_score(self) -> dict:
        if self._score_cache is None:
            self._score_cache = score_content(
                f"名称: {self.name}\n标语: {self.tagline}\n描述: {self.description}\n关键词: {self.keyword}",
                client,
                kind="producthunt",
            )
        return self._score_cache

def get_producthunt_token():
    """获取 Product Hunt 访问令牌"""
    # 优先使用 PRODUCTHUNT_DEVELOPER_TOKEN 环境变量
    developer_token = os.getenv('PRODUCTHUNT_DEVELOPER_TOKEN')
    if developer_token:
        print("使用 PRODUCTHUNT_DEVELOPER_TOKEN 环境变量")
        return developer_token
    
    # 如果没有 developer token，尝试使用 client credentials 获取访问令牌
    client_id = os.getenv('PRODUCTHUNT_CLIENT_ID')
    client_secret = os.getenv('PRODUCTHUNT_CLIENT_SECRET')
    
    if not client_id or not client_secret:
        raise Exception("Product Hunt client ID or client secret not found in environment variables")
    
    # 使用 client credentials 获取访问令牌
    token_url = "https://api.producthunt.com/v2/oauth/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    
    try:
        response = requests.post(token_url, json=payload, timeout=_get_http_timeout())
        response.raise_for_status()
        token_data = response.json()
        return token_data.get("access_token")
    except Exception as e:
        print(f"获取 Product Hunt 访问令牌时出错: {e}")
        raise Exception(f"Failed to get Product Hunt access token: {e}")

def fetch_product_hunt_data(target_date: str = ""):
    """从Product Hunt获取指定日期的Top 30数据（默认前一天）"""
    token = get_producthunt_token()
    if target_date:
        date_str = target_date
    else:
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        date_str = yesterday.strftime('%Y-%m-%d')
    url = "https://api.producthunt.com/v2/api/graphql"
    
    # 添加更多请求头信息
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "DecohackBot/1.0 (https://decohack.com)",
        "Origin": "https://decohack.com",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Connection": "keep-alive"
    }

    # 设置重试策略
    retry_strategy = Retry(
        total=4,
        connect=4,
        read=4,
        status=4,
        backoff_factor=1.0,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=frozenset(["POST"]),
        raise_on_status=False,
        respect_retry_after_header=True,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)

    base_query = """
    {
      posts(order: VOTES, postedAfter: "%sT00:00:00Z", postedBefore: "%sT23:59:59Z", after: "%s") {
        nodes {
          id
          name
          tagline
          description
          votesCount
          createdAt
          featuredAt
          website
          url
          media {
            url
            type
            videoUrl
          }
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
    """

    max_posts = _get_max_posts(30)
    scan_limit = max(max_posts * 4, 60)
    scan_limit = min(scan_limit, 200)
    all_posts = []
    has_next_page = True
    cursor = ""

    while has_next_page and len(all_posts) < scan_limit:
        query = base_query % (date_str, date_str, cursor)
        response = None
        last_error = None
        for attempt in range(1, 4):
            try:
                response = session.post(
                    url,
                    headers=headers,
                    json={"query": query},
                    timeout=_get_http_timeout(),
                )
                if response.status_code in {429, 500, 502, 503, 504} and attempt < 3:
                    wait_seconds = 2 * attempt
                    print(
                        f"Product Hunt 请求返回 {response.status_code}，"
                        f"第 {attempt}/3 次重试，等待 {wait_seconds}s..."
                    )
                    time.sleep(wait_seconds)
                    continue
                response.raise_for_status()
                break
            except requests.exceptions.RequestException as e:
                last_error = e
                if attempt < 3:
                    wait_seconds = 2 * attempt
                    print(f"请求失败，第 {attempt}/3 次重试，等待 {wait_seconds}s: {e}")
                    time.sleep(wait_seconds)
                    continue
                print(f"请求失败: {e}")
                raise Exception(f"Failed to fetch data from Product Hunt: {e}")

        if response is None:
            raise Exception(f"Failed to fetch data from Product Hunt: {last_error}")

        data = response.json()['data']['posts']
        posts = data['nodes']
        all_posts.extend(posts)

        has_next_page = data['pageInfo']['hasNextPage']
        cursor = data['pageInfo']['endCursor']

    deduped_posts = []
    seen_ids = set()
    for post in sorted(all_posts, key=lambda x: x['votesCount'], reverse=True):
        post_id = str(post.get("id", "")).strip()
        if not post_id or post_id in seen_ids:
            continue
        seen_ids.add(post_id)
        deduped_posts.append(post)

    ai_posts = []
    for post in deduped_posts:
        if is_ai_related(post.get("name", ""), post.get("tagline", ""), post.get("description", "")):
            ai_posts.append(post)
        if len(ai_posts) >= max_posts:
            break

    return [Product(**post) for post in ai_posts]

def fetch_mock_data():
    """生成模拟数据用于测试"""
    print("使用模拟数据进行测试...")
    mock_products = [
        {
            "id": "1",
            "name": "Venice",
            "tagline": "Private & censorship-resistant AI | Unlock unlimited intelligence",
            "description": "Venice is a private, censorship-resistant AI platform powered by open-source models and decentralized infrastructure. The app combines the benefits of decentralized blockchain technology with the power of generative AI.",
            "votesCount": 566,
            "createdAt": "2025-03-07T16:01:00Z",
            "featuredAt": "2025-03-07T16:01:00Z",
            "website": "https://www.producthunt.com/r/4D6Z6F7I3SXTGN",
            "url": "https://www.producthunt.com/posts/venice-3",
            "media": [
                {
                    "url": "https://ph-files.imgix.net/97baee49-6dda-47f5-8a47-91d2c56e1976.jpeg",
                    "type": "image",
                    "videoUrl": None
                }
            ]
        },
        {
            "id": "2",
            "name": "Mistral OCR",
            "tagline": "Introducing the world's most powerful document understanding API",
            "description": "Introducing Mistral OCR—an advanced, lightweight optical character recognition model focused on speed, accuracy, and efficiency. Whether extracting text from images or digitizing documents, it delivers top-tier performance with ease.",
            "votesCount": 477,
            "createdAt": "2025-03-07T16:01:00Z",
            "featuredAt": "2025-03-07T16:01:00Z",
            "website": "https://www.producthunt.com/r/SPXNTAWQSVRLGH",
            "url": "https://www.producthunt.com/posts/mistral-ocr",
            "media": [
                {
                    "url": "https://ph-files.imgix.net/4224517b-29e4-4944-98c9-2eee59374870.png",
                    "type": "image",
                    "videoUrl": None
                }
            ]
        }
    ]
    return [Product(**product) for product in mock_products]

def generate_markdown(products, date_str):
    """生成Markdown内容并保存到data/producthunt目录"""
    ai_products = []
    seen_ids = set()
    for product in products:
        if not is_ai_related(product.name, product.tagline, product.description):
            print(f"跳过非AI产品: {product.name}")
            continue
        if product.product_id in seen_ids:
            continue
        seen_ids.add(product.product_id)
        ai_products.append(product)

    max_posts = _get_max_posts(30)
    daily_ai = ai_products[:max_posts]
    featured_ai = [product for product in daily_ai if product.is_featured][:max_posts]
    featured_ids = {product.product_id for product in featured_ai}
    remaining_daily_ai = [product for product in daily_ai if product.product_id not in featured_ids]

    markdown_content = f"# PH AI 日榜 | {date_str}\n\n"
    markdown_content += (
        f"> Daily Featured AI: {len(featured_ai)} | "
        f"Daily AI(去重后): {len(daily_ai)}\n\n"
    )

    structured_items = []
    featured_rank_map = {product.product_id: idx for idx, product in enumerate(featured_ai, start=1)}

    markdown_content += "## Daily Featured AI\n\n"
    if featured_ai:
        for rank, product in enumerate(featured_ai, start=1):
            markdown_content += product.to_markdown(rank)
    else:
        markdown_content += "> 当天无 Featured AI 产品。\n\n"

    markdown_content += "## Daily AI（去重后，已排除上方 Featured 项）\n\n"
    if remaining_daily_ai:
        for rank, product in enumerate(remaining_daily_ai, start=1):
            markdown_content += product.to_markdown(rank)
    else:
        markdown_content += "> 当天无额外 AI 产品。\n\n"

    for rank, product in enumerate(daily_ai, start=1):
        extra_tags = []
        if product.product_id in featured_rank_map:
            extra_tags.append("daily_featured_ai")
        structured_items.append(
            product.to_content_item(
                rank,
                date_str,
                extra_tags=extra_tags,
                featured_rank=featured_rank_map.get(product.product_id),
            )
        )

    # 确保 data/producthunt 目录存在
    os.makedirs('data/producthunt', exist_ok=True)

    # 修改文件保存路径到 data/producthunt 目录
    file_name = f"data/producthunt/producthunt-daily-{date_str}.md"
    
    # 如果文件存在，直接覆盖
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    print(f"文件 {file_name} 生成成功并已覆盖。")
    save_structured_items(date_str, structured_items)


def main():
    # 支持抓取日期和输出日期分离：
    # - PRODUCTHUNT_TARGET_DATE/PRODUCTHUNT_FETCH_DATE: 实际抓取窗口
    # - PRODUCTHUNT_OUTPUT_DATE: 写入结构化数据与文件日期
    fetch_date = (
        os.getenv("PRODUCTHUNT_FETCH_DATE", "").strip()
        or os.getenv("PRODUCTHUNT_TARGET_DATE", "").strip()
    )
    output_date = os.getenv("PRODUCTHUNT_OUTPUT_DATE", "").strip()

    if fetch_date:
        target_date = fetch_date
    else:
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        target_date = yesterday.strftime('%Y-%m-%d')

    if output_date:
        date_str = output_date
    else:
        date_str = target_date

    print(f"Product Hunt 抓取日期: {target_date}, 写入日期: {date_str}")

    try:
        # 尝试获取Product Hunt数据
        products = fetch_product_hunt_data(target_date)
    except Exception as e:
        print(f"获取Product Hunt数据失败: {e}")
        if _allow_mock_data():
            print("ALLOW_MOCK_DATA=true，使用模拟数据继续...")
            products = fetch_mock_data()
        else:
            raise

    # 生成Markdown文件
    generate_markdown(products, date_str)

if __name__ == "__main__":
    main()
