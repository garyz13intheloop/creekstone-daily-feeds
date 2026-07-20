# ClawHub Skills Daily | 2026-07-20

> 共 25 个 skills

## [1. Reddit Post Search](https://clawhub.ai/browseract-cli/reddit-post-search)

**Slug**: `reddit-post-search`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Extracts Reddit posts from keyword search, subreddit browsing, or direct Reddit URLs. Input: search query, subreddit name, or direct reddit.com URL with sort (relevance/hot/top/new/comments), timeframe (hour/day/week/month/year/all), limit, pagination cursor, optional date range, NSFW flag, and stri

**中文介绍**: Extracts Reddit posts from keyword search, subreddit browsing, or direct Reddit URLs. Input: search query, subreddit name, or direct reddit.com URL with sort (relevance/hot/top/new/comments), timeframe (hour/day/week/month/year/all), limit, pagination cursor, optional date range, NSFW flag, and stri

Latest changelog:
Initial release of reddit-post-search skill:

- Enables extraction of Reddit posts via keyword search, subreddit listing, or direct Reddit URLs.
- Supports configurable parameters: sort type, timeframe, post limit, pagination, date range, NSFW inclusion, and strict token filtering.
- Returns structured JSON with 40+ fields per post, including metadata, engagement metrics, and media links.
- Operates within the user's browser context using Reddit's public JSON API—respects authentication and rate limits.
- Handles pagination, applies post-fetch filtering, outputs ready-to-analyze data, and lists clear limitations and usage guidelines.

**关键词**: or, Reddit, Post, Search, Extracts, posts, subreddit, browsing

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/reddit-post-search)

---

## [2. Build Pixel Pet Sprites](https://clawhub.ai/mmgongzhu/build-pixel-pet-sprites)

**Slug**: `build-pixel-pet-sprites`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Create a production-ready chibi pixel-art virtual desktop pet based on a character reference image, including character design sheets, multi-action animation...

**中文介绍**: Create a production-ready chibi pixel-art virtual desktop pet based on a character reference image, including character design sheets, multi-action animation...

Latest changelog:
Initial release of build-pixel-pet-sprites.

- Create production-ready chibi pixel-art desktop pets from a character reference, including character sheets and multi-action animation sprite sheets.
- Includes tools for automatic character alignment using alpha edges and connected-component analysis to prevent frame drift.
- Provides validation scripts for asset consistency, transparency, frame counts, and jitter measurement.
- Outputs include RGBA frame assets, GIF previews, action strips, asset inventories, aligned atlases, manifests, and web-integration ZIP packaging.
- Features modular workflow to support new characters, new actions, repairing drift, or web deployment only.

**关键词**: Build, Pixel, Pet, Sprites, production-ready, chibi, pixel-art, virtual

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/build-pixel-pet-sprites)

---

## [3. Walmart Product Reviews](https://clawhub.ai/browseract-cli/walmart-product-reviews)

**Slug**: `walmart-product-reviews`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Walmart product reviews scraper: given a walmart.com product item ID, navigate to the reviews page and extract paginated customer reviews including reviewId, rating, title, review text, author nickname, submission date, verified purchase status, helpful votes, variant selected (color/size), badges,

**中文介绍**: Walmart product reviews scraper: given a walmart.com product item ID, navigate to the reviews page and extract paginated customer reviews including reviewId, rating, title, review text, author nickname, submission date, verified purchase status, helpful votes, variant selected (color/size), badges,

Latest changelog:
Initial public release of Walmart product reviews scraper.

- Scrapes paginated customer reviews from any walmart.com product, using item ID and page number.
- Extracts structured data: reviewId, rating, text, author nickname, date, verified purchase, helpful votes, variant (e.g., color/size), badges, fulfillment and seller info, and photo count.
- Handles pagination, returning 10 reviews per page until all reviews are collected.
- Includes robust error handling for unsupported pages or extraction errors.
- Provides detailed guidance on pre-execution setup, batching, error resumption, and experience logging.

**关键词**: ID, Walmart, Product, Reviews, scraper, given, walmart.com, item

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/walmart-product-reviews)

---

## [4. Feishu Card Design 飞书卡片消息设计规范](https://clawhub.ai/edwardwason/feishu-card-design)

**Slug**: `feishu-card-design`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 80 | 🧩 5

**原始简介**: 飞书卡片消息设计规范技能——一套适用于所有 Agent 平台（TRAE 定时任务、Coze、Dify、自建 Agent）的飞书 IM 卡片消息渲染规范。基于 Card 2.0 Schema，定义邻近色环配色规则、标题命名规则、布局模式、客户端兼容性、可访问性。本技能是纯规范 Skill，不直接发送飞书消息。Do...

**中文介绍**: 飞书卡片消息设计规范技能——一套适用于所有 Agent 平台（TRAE 定时任务、Coze、Dify、自建 Agent）的飞书 IM 卡片消息渲染规范。基于 Card 2.0 Schema，定义邻近色环配色规则、标题命名规则、布局模式、客户端兼容性、可访问性。本技能是纯规范 Skill，不直接发送飞书消息。Do...

Latest changelog:
v1.0.4: Schema example + Hex colors + alert block conditional trigger

**关键词**: 飞书卡片消息设计规范, 飞书卡片消息设计规范技能——一套适用于所有, Agent, 定时任务、Coze、Dify、自建, Feishu, Card, Design, 平台（TRAE

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/feishu-card-design)

---

## [5. 小红书热榜选题分析](https://clawhub.ai/devinchen2014/xhs-hot-topic-selection)

**Slug**: `xhs-hot-topic-selection`  
**Version**: 0.1.3  
**Stats**: ⭐ 0 | ⬇️ 68 | 🧩 4

**原始简介**: 用于小红书热榜选题、小红书热点选题、小红书热榜分析、小红书热点分析和趋势选题参考。先看当前小红书热榜，再结合相关热门笔记样本，把热榜信号整理成可执行选题，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于小红书热榜选题、小红书热点选题、小红书热榜分析、小红书热点分析和趋势选题参考。先看当前小红书热榜，再结合相关热门笔记样本，把热榜信号整理成可执行选题，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 小红书热榜选题分析, 先看当前小红书热榜, 再结合相关热门笔记样本, 把热榜信号整理成可执行选题, 来自, 社媒数据助手, SocialDataX, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xhs-hot-topic-selection)

---

## [6. Walmart Product Detail](https://clawhub.ai/browseract-cli/walmart-product-detail)

**Slug**: `walmart-product-detail`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Walmart product detail page extractor: given a walmart.com product URL (walmart.com/ip/...), extract full product data including itemId, title, brand, model, UPC, price, wasPrice, currency, availability, category path, seller info, all images, shortDescription, longDescription, product highlights, f

**中文介绍**: Walmart product detail page extractor: given a walmart.com product URL (walmart.com/ip/...), extract full product data including itemId, title, brand, model, UPC, price, wasPrice, currency, availability, category path, seller info, all images, shortDescription, longDescription, product highlights, f

Latest changelog:
Initial release — extract comprehensive structured product data from Walmart product detail pages.

- Given a Walmart product URL, extracts fields including itemId, title, brand, model, UPC, price, availability, seller info, images, descriptions, highlights, specifications (as a key-value map), variants, fulfillment options, return policy, and review summary.
- Supports batch extraction from multiple URLs; includes recommendations for efficient scraping with rate-limiting best practices.
- Only reads data visible to the user, respecting authentication and access controls.
- Returns errors with clear messages if extraction fails or invalid pages are detected.
- Known limitations include incomplete data for certain fields if not present on the page and variant item ID resolution nuances.
- Includes detailed execution steps, output schema, and usage guidance for both single product and batch scenarios.

**关键词**: Walmart, Product, Detail, page, extractor, given, walmart.com, URL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/walmart-product-detail)

---

## [7. Crypto Price Prediction](https://clawhub.ai/stevenho1394/crypto-price-prediction)

**Slug**: `crypto-price-prediction`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Fetches next-hour predicted price for BTC/ETH from external API (zeabur). Supports BTCUSDT and ETHUSDT symbols only.

**中文介绍**: Fetches next-hour predicted price for BTC/ETH from external API (zeabur). Supports BTCUSDT and ETHUSDT symbols only.

Latest changelog:
Initial release — fetch next-hour crypto price predictions for BTC or ETH via external API.

- Supports BTCUSDT and ETHUSDT symbols only
- Provides predicted price for the next hour (HKT timezone)
- Hermes CLI, OpenClaw plugin, and direct Python script usage supported
- No fallback to local models or other time horizons
- MIT licensed

**关键词**: Crypto, Price, Prediction, Fetches, next-hour, predicted, BTC, ETH

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/crypto-price-prediction)

---

## [8. Xiaohongshu Search Full](https://clawhub.ai/browseract-cli/xiaohongshu-search-full)

**Slug**: `xiaohongshu-search-full`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Search Xiaohongshu (XHS / RedNote) notes by keyword with full field extraction including body text, topics/tags, image list URLs, video stream URL, publish timestamp, and all engagement stats (likes, collects, comments, shares). Supports all page filter options: sort order (general, latest, most lik

**中文介绍**: Search Xiaohongshu (XHS / RedNote) notes by keyword with full field extraction including body text, topics/tags, image list URLs, video stream URL, publish timestamp, and all engagement stats (likes, collects, comments, shares). Supports all page filter options: sort order (general, latest, most lik

Latest changelog:
Initial release of Xiaohongshu (XHS/RedNote) full keyword search skill.

- Search Xiaohongshu notes by keyword, supporting all page filter options (sort order, note type, publish time, distance, etc).
- Extracts comprehensive note data: title, body text, tags, images, video URL, publish timestamp, and engagement stats.
- Requires user to manually provide a search keyword before proceeding.
- Verifies browser-act tool availability and Xiaohongshu login status before executing searches.
- Reads only on-screen data as visible to the user—never bypasses authentication.

**关键词**: Xiaohongshu, Search, Full, XHS, RedNote, notes, field, extraction

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaohongshu-search-full)

---

## [9. Walmart Keyword Search](https://clawhub.ai/browseract-cli/walmart-keyword-search)

**Slug**: `walmart-keyword-search`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Walmart keyword search scraper: input a search keyword and page number, navigate to walmart.com search results, extract paginated product listings with itemId, url, title, brand, image, price, wasPrice, rating, reviewCount, availability, seller info, fulfillmentBadge, classType, and shortDescription

**中文介绍**: Walmart keyword search scraper: input a search keyword and page number, navigate to walmart.com search results, extract paginated product listings with itemId, url, title, brand, image, price, wasPrice, rating, reviewCount, availability, seller info, fulfillmentBadge, classType, and shortDescription

Latest changelog:
- Initial release of the Walmart Keyword Search scraper skill.
- Extracts paginated Walmart product search results by keyword and page.
- Returns structured product details including itemId, title, URL, image, price, rating, review count, availability, seller info, fulfillment badge, and more.
- Supports navigation by URL, page number, and sort order (e.g., best_match, price_low).
- Includes batching guidance, error recording, and execution efficiency tips.
- Designed for safe, manual-equivalent data extraction—never bypasses authentication or access controls.

**关键词**: Walmart, Search, scraper, input, page, number, navigate, walmart.com

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/walmart-keyword-search)

---

## [10. 微博评论分析 SocialDataX 评论洞察](https://clawhub.ai/devinchen2014/socialdatax-weibo-comments)

**Slug**: `socialdatax-weibo-comments`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 280 | 🧩 6

**原始简介**: 用于微博评论分析、微博评论回复、微博评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Weibo comments and comment replies，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于微博评论分析、微博评论回复、微博评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Weibo comments and comment replies，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 微博评论分析, 评论洞察, 覆盖, SocialDataX, Weibo, comments, comment, replies

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-weibo-comments)

---

## [11. 微博创作者数据 SocialDataX 创作者资料](https://clawhub.ai/devinchen2014/socialdatax-weibo-creator-profile)

**Slug**: `socialdatax-weibo-creator-profile`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 280 | 🧩 6

**原始简介**: 用于微博创作者数据、微博用户资料、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Weibo creator profiles，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于微博创作者数据、微博用户资料、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Weibo creator profiles，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 微博创作者数据, 创作者资料, 覆盖, 来自, SocialDataX, Weibo, creator, profiles

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-weibo-creator-profile)

---

## [12. 微博创作者数据 SocialDataX 创作者内容](https://clawhub.ai/devinchen2014/socialdatax-weibo-creator-posts)

**Slug**: `socialdatax-weibo-creator-posts`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 266 | 🧩 6

**原始简介**: 用于微博创作者数据、微博创作者内容列表、近期发布、内容调研和创作者内容分析。覆盖 Weibo creator posts，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于微博创作者数据、微博创作者内容列表、近期发布、内容调研和创作者内容分析。覆盖 Weibo creator posts，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 微博创作者数据, 创作者内容, 覆盖, 来自, SocialDataX, Weibo, creator, posts

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-weibo-creator-posts)

---

## [13. 敏感词检测与违禁词检查](https://clawhub.ai/devinchen2014/socialdatax-sensitive-check)

**Slug**: `socialdatax-sensitive-check`  
**Version**: 0.1.6  
**Stats**: ⭐ 0 | ⬇️ 251 | 🧩 7

**原始简介**: 用于敏感词检测、违禁词检测、文案发布前检查、内容安全检查、文案合规审核、能不能发判断、平台风险提示和改写建议。支持小红书、抖音、快手和通用文本场景，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于敏感词检测、违禁词检测、文案发布前检查、内容安全检查、文案合规审核、能不能发判断、平台风险提示和改写建议。支持小红书、抖音、快手和通用文本场景，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 敏感词检测与违禁词检查, 支持小红书、抖音、快手和通用文本场景, 来自, 社媒数据助手, SocialDataX, Latest, changelog, Refresh

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-sensitive-check)

---

## [14. 微博数据分析 SocialDataX 帖子详情](https://clawhub.ai/devinchen2014/socialdatax-weibo-detail)

**Slug**: `socialdatax-weibo-detail`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 279 | 🧩 6

**原始简介**: 用于微博数据分析、微博帖子详情、帖子数据、互动指标、内容调研和内容分析。覆盖 Weibo post details，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于微博数据分析、微博帖子详情、帖子数据、互动指标、内容调研和内容分析。覆盖 Weibo post details，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 微博数据分析, 帖子详情, 覆盖, 来自, SocialDataX, Weibo, post, details

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-weibo-detail)

---

## [15. 快手评论分析 SocialDataX 评论洞察](https://clawhub.ai/devinchen2014/socialdatax-kuaishou-comments)

**Slug**: `socialdatax-kuaishou-comments`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 460 | 🧩 7

**原始简介**: 用于快手评论分析、快手评论回复、快手评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Kuaishou / Kwai comments and comment replies，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于快手评论分析、快手评论回复、快手评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Kuaishou / Kwai comments and comment replies，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 快手评论分析, 评论洞察, 覆盖, SocialDataX, Kuaishou, Kwai, comments, comment

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-kuaishou-comments)

---

## [16. 微博数据分析 SocialDataX 内容研究](https://clawhub.ai/devinchen2014/socialdatax-weibo-search)

**Slug**: `socialdatax-weibo-search`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 285 | 🧩 6

**原始简介**: 用于微博数据分析、微博热搜、微博内容研究、关键词观察、内容调研、竞品分析和趋势研究。覆盖 Weibo hot-search and post research，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于微博数据分析、微博热搜、微博内容研究、关键词观察、内容调研、竞品分析和趋势研究。覆盖 Weibo hot-search and post research，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 微博数据分析, 内容研究, 覆盖, SocialDataX, Weibo, hot-search, post, research

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-weibo-search)

---

## [17. 快手达人数据 SocialDataX 达人信息](https://clawhub.ai/devinchen2014/socialdatax-kuaishou-creator-profile)

**Slug**: `socialdatax-kuaishou-creator-profile`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 501 | 🧩 7

**原始简介**: 用于快手达人数据、快手达人信息、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Kuaishou / Kwai creator profiles，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于快手达人数据、快手达人信息、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Kuaishou / Kwai creator profiles，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 快手达人数据, 达人信息, 覆盖, SocialDataX, Kuaishou, Kwai, creator, profiles

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-kuaishou-creator-profile)

---

## [18. 快手数据分析 SocialDataX 作品详情](https://clawhub.ai/devinchen2014/socialdatax-kuaishou-detail)

**Slug**: `socialdatax-kuaishou-detail`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 455 | 🧩 7

**原始简介**: 用于快手数据分析、快手作品详情、作品数据、互动指标、内容调研和内容分析。覆盖 Kuaishou / Kwai work details，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于快手数据分析、快手作品详情、作品数据、互动指标、内容调研和内容分析。覆盖 Kuaishou / Kwai work details，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 快手数据分析, 作品详情, 覆盖, SocialDataX, Kuaishou, Kwai, work, details

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-kuaishou-detail)

---

## [19. 微博数据助手 SocialDataX](https://clawhub.ai/devinchen2014/socialdatax-weibo)

**Slug**: `socialdatax-weibo`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 284 | 🧩 6

**原始简介**: 用于微博数据助手、微博热搜、微博内容研究、帖子详情、评论分析、评论回复观察、转赞互动、创作者资料和创作者内容列表。覆盖 Weibo post research，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于微博数据助手、微博热搜、微博内容研究、帖子详情、评论分析、评论回复观察、转赞互动、创作者资料和创作者内容列表。覆盖 Weibo post research，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 微博数据助手, 覆盖, 来自, 社媒数据助手, SocialDataX, Weibo, post, research

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-weibo)

---

## [20. 快手达人数据 SocialDataX 达人作品](https://clawhub.ai/devinchen2014/socialdatax-kuaishou-creator-videos)

**Slug**: `socialdatax-kuaishou-creator-videos`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 462 | 🧩 7

**原始简介**: 用于快手达人数据、快手达人作品、作品列表、近期发布、内容调研和创作者内容分析。覆盖 Kuaishou / Kwai creator works，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于快手达人数据、快手达人作品、作品列表、近期发布、内容调研和创作者内容分析。覆盖 Kuaishou / Kwai creator works，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 快手达人数据, 达人作品, 覆盖, SocialDataX, Kuaishou, Kwai, creator, works

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-kuaishou-creator-videos)

---

## [21. 快手数据助手 SocialDataX](https://clawhub.ai/devinchen2014/socialdatax-kuaishou)

**Slug**: `socialdatax-kuaishou`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 481 | 🧩 7

**原始简介**: 用于快手数据助手、快手内容研究、作品研究、作品详情、评论分析、评论回复分析、达人数据和达人作品。覆盖 Kuaishou / Kwai short-video research，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于快手数据助手、快手内容研究、作品研究、作品详情、评论分析、评论回复分析、达人数据和达人作品。覆盖 Kuaishou / Kwai short-video research，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 快手数据助手, 覆盖, 来自, SocialDataX, Kuaishou, Kwai, short-video, research

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-kuaishou)

---

## [22. 快手数据分析 SocialDataX 作品研究](https://clawhub.ai/devinchen2014/socialdatax-kuaishou-search)

**Slug**: `socialdatax-kuaishou-search`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 465 | 🧩 7

**原始简介**: 用于快手数据分析、快手作品研究、关键词观察、内容调研、竞品分析和趋势研究。覆盖 Kuaishou / Kwai work research，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于快手数据分析、快手作品研究、关键词观察、内容调研、竞品分析和趋势研究。覆盖 Kuaishou / Kwai work research，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 快手数据分析, 作品研究, 覆盖, SocialDataX, Kuaishou, Kwai, work, research

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-kuaishou-search)

---

## [23. 抖音文案提取](https://clawhub.ai/devinchen2014/douyin-video-copy-extract)

**Slug**: `douyin-video-copy-extract`  
**Version**: 0.1.3  
**Stats**: ⭐ 0 | ⬇️ 74 | 🧩 4

**原始简介**: 用于抖音文案提取、抖音文案一键提取、抖音视频文案提取、抖音视频转文字、抖音口播转文字和抖音逐字稿。用户粘贴抖音视频链接、分享文案或 aweme_id 后，提取视频上下文、原视频简介和口播逐字稿，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于抖音文案提取、抖音文案一键提取、抖音视频文案提取、抖音视频转文字、抖音口播转文字和抖音逐字稿。用户粘贴抖音视频链接、分享文案或 aweme_id 后，提取视频上下文、原视频简介和口播逐字稿，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 抖音文案提取, 用户粘贴抖音视频链接、分享文案或, id, 提取视频上下文、原视频简介和口播逐字稿, 来自, 社媒数据助手, aweme, SocialDataX

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/douyin-video-copy-extract)

---

## [24. 抖音数据分析 SocialDataX 作品详情](https://clawhub.ai/devinchen2014/socialdatax-douyin-detail)

**Slug**: `socialdatax-douyin-detail`  
**Version**: 0.1.13  
**Stats**: ⭐ 0 | ⬇️ 998 | 🧩 13

**原始简介**: 用于抖音数据分析、抖音作品详情、图文详情、作品数据、互动指标、内容调研和内容分析。覆盖 Douyin work details，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于抖音数据分析、抖音作品详情、图文详情、作品数据、互动指标、内容调研和内容分析。覆盖 Douyin work details，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 抖音数据分析, 作品详情, 覆盖, 来自, SocialDataX, Douyin, work, details

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-douyin-detail)

---

## [25. 抖音达人数据 SocialDataX 达人作品](https://clawhub.ai/devinchen2014/socialdatax-douyin-creator-videos)

**Slug**: `socialdatax-douyin-creator-videos`  
**Version**: 0.1.14  
**Stats**: ⭐ 0 | ⬇️ 1028 | 🧩 14

**原始简介**: 用于抖音达人数据、抖音达人作品、作品列表、图文列表、短剧/合集列表、近期发布、内容调研和创作者内容分析。覆盖 Douyin creator works and series，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于抖音达人数据、抖音达人作品、作品列表、图文列表、短剧/合集列表、近期发布、内容调研和创作者内容分析。覆盖 Douyin creator works and series，来自 SocialDataX 社媒数据助手。

Latest changelog:
Refresh API Key guidance to the SocialDataX AI access page.

**关键词**: 抖音达人数据, 达人作品, 合集列表、近期发布、内容调研和创作者内容分析, 覆盖, SocialDataX, Douyin, creator, works

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/socialdatax-douyin-creator-videos)

---

