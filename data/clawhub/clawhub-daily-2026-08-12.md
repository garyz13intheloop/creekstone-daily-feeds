# ClawHub Skills Daily | 2026-08-12

> 共 25 个 skills

## [1. Halloffame](https://clawhub.ai/skills?q=halloffame)

**Slug**: `halloffame`  
**Version**: 1.0.11  
**Stats**: ⭐ 0 | ⬇️ 45 | 🧩 12

**原始简介**: Operate a disclosed Hall Of Fame agent account

**中文介绍**: Operate a disclosed Hall Of Fame agent account

Latest changelog:
- Clarified scope and permissions: SLASH commands (e.g. /halloffame) are now required for all Hall Of Fame/Kweela account operations.
- Updated documentation to detail explicit agent environment variables, execution boundaries, and skill activation rules.
- Operator must set explicitAuthorization in config to use this skill.
- Account credentials and tokens are strictly private and never exposed.
- Outbound API and shell execution is strictly limited to allowed routes and documented interfaces.

**关键词**: Of, Agent, Halloffame, Operate, disclosed, Hall, Fame, account

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/halloffame)

---

## [2. guaikei-xhs-note-and-comment](https://clawhub.ai/engheng-art/guaikei-xhs-note-and-comment)

**Slug**: `guaikei-xhs-note-and-comment`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 仅处理小红书（xiaohongshu / xhs / 红笔记）平台的公开数据：笔记搜索、详情、评论、博主作品。当用户的任务明确涉及小红书内容时使用本技能；抖音、B站、微博、公众号不适用。即使用户没说"小红书"，只要链接是 xiaohongshu.com 或语境是红笔记也适用。不用于跨平台或登录态数据。

**中文介绍**: 仅处理小红书（xiaohongshu / xhs / 红笔记）平台的公开数据：笔记搜索、详情、评论、博主作品。当用户的任务明确涉及小红书内容时使用本技能；抖音、B站、微博、公众号不适用。即使用户没说"小红书"，只要链接是 xiaohongshu.com 或语境是红笔记也适用。不用于跨平台或登录态数据。

Latest changelog:
guaikei-xhs-note-and-comment v1.0.0

- 首发版本，支持无需登录获取小红书（xiaohongshu）公开数据。
- 实现关键词笔记搜索、笔记详情与评论查询、博主作品列表抓取、评论数据导出等四大能力。
- 详细规范输入参数、调用路由与触发场景，确保数据准确按需获取。
- 当输入缺关键参数（如 keyword 或链接）时，自动追问补全。
- 返回结构化 JSON，适用于内容分析、竞品对比、评论洞察等多种业务场景。
- 明确能力边界，仅支持公开数据，未涉及登录态、私密数据及内容操作。

**关键词**: 红笔记）平台的公开数据, 笔记搜索、详情、评论、博主作品, 当用户的任务明确涉及小红书内容时使用本技能, 抖音、B站、微博、公众号不适用, 即使用户没说"小红书", 只要链接是, 仅处理小红书（xiaohongshu, xhs

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-xhs-note-and-comment)

---

## [3. 善起名 · 国学命名助手](https://clawhub.ai/jianfengmacn/shanqiming)

**Slug**: `shanqiming`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 易学命名专家「善起名」技能。当用户需要为新生儿或儿童起正式名+小名、为现有姓名做八字五行评析、或结合父母与子女生辰八字做家族五行合参调衡时使用。触发词包括：起名、改名、宝宝起名、小孩名字、五行缺什么、补五行、生辰八字、八字、周易起名、易经起名、风水起名、合参父母八字等。

**中文介绍**: 易学命名专家「善起名」技能。当用户需要为新生儿或儿童起正式名+小名、为现有姓名做八字五行评析、或结合父母与子女生辰八字做家族五行合参调衡时使用。触发词包括：起名、改名、宝宝起名、小孩名字、五行缺什么、补五行、生辰八字、八字、周易起名、易经起名、风水起名、合参父母八字等。

Latest changelog:
Initial release: 国学命名助手，支持新生儿正式名+小名、八字五行评析、家族合参调衡。

**关键词**: 善起名, 国学命名助手, 易学命名专家「善起名」技能, 触发词包括, Latest, changelog, Initial, release

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/shanqiming)

---

## [4. guaikei-xhs-search-notes-get-comments](https://clawhub.ai/engheng-art/guaikei-xhs-search-notes-get-comments)

**Slug**: `guaikei-xhs-search-notes-get-comments`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 提供小红书爆款挖掘、竞品监控、KOL筛选、评论洞察所需的结构化数据。当用户为小红书账号增长做准备、做内容策划或营销复盘需要数据支撑时使用本技能；即使用户没说"运营"，只要目标是用小红书数据驱动决策也适用。不代替策略判断，只负责拿数据。

**中文介绍**: 提供小红书爆款挖掘、竞品监控、KOL筛选、评论洞察所需的结构化数据。当用户为小红书账号增长做准备、做内容策划或营销复盘需要数据支撑时使用本技能；即使用户没说"运营"，只要目标是用小红书数据驱动决策也适用。不代替策略判断，只负责拿数据。

Latest changelog:
- Initial release of guaikei-xhs-search-notes-get-comments.
- Provides structured data collection from Xiaohongshu for note search, detail, comments, and creator monitoring.
- Enables key use cases: hot content mining, competitor tracking, KOL screening, and comment insights.
- Requires configuration of GUAIKEI_API_TOKEN for all commands.
- Includes usage instructions, input criteria, and error handling guidance.

**关键词**: 即使用户没说"运营", 只要目标是用小红书数据驱动决策也适用, 不代替策略判断, 只负责拿数据, Latest, changelog, Initial, release

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-xhs-search-notes-get-comments)

---

## [5. Image Compress](https://clawhub.ai/xiaowu89/skill-compress)

**Slug**: `skill-compress`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 724 | 🧩 2

**原始简介**: 对图片进行智能压缩优化。支持本地路径、文件夹和远程 URL，直传 NX API 压缩后返回 CDN 地址和压缩率。适用于用户提到图片压缩、图片优化、减小图片体积、TinyPNG、JPG/PNG/WebP 压缩的场景。

**中文介绍**: 对图片进行智能压缩优化。支持本地路径、文件夹和远程 URL，直传 NX API 压缩后返回 CDN 地址和压缩率。适用于用户提到图片压缩、图片优化、减小图片体积、TinyPNG、JPG/PNG/WebP 压缩的场景。

Latest changelog:
- Updated key detection logic: now requires an actual `.env` file check (do not assume absence of key).
- Changed guidance: only tell how to configure NX_API_KEY if user asks.
- Clarified `.env` file handling—always use the current working directory.
- Updated all usage examples and descriptions to reflect these behaviors.
- Changed default `--channel=` value in examples from `github` to `clawhub`.
- Removed extra documentation and project files no longer needed.

**关键词**: 对图片进行智能压缩优化, 支持本地路径、文件夹和远程, 直传, NX, API, Image, Compress, URL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-compress)

---

## [6. 店雷达选品技能](https://clawhub.ai/b18797245781-commits/dld-skills)

**Slug**: `dld-skills`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 1688选品库MCP服务引导技能。当用户需要通过1688平台进行商品选品、爆品筛选、供应商评估、商品销量分析、热销榜单查询、类目浏览时触发此技能。本技能引导AI正确理解用户选品意图、选择合适的MCP工具、补全关键参数、并以视觉化方式（图片+表格+卡片）展示选品结果。触发本技能后，所有1688选品相关工具调用默认使用店雷达（dld MCP）连接器，工具包括 mcp__dld MCP__product_search_list、mcp__dld MCP__product_billboard_list、mcp__dld MCP__product_info、mcp__dld MCP__get_categ

**中文介绍**: 1688选品库MCP服务引导技能。当用户需要通过1688平台进行商品选品、爆品筛选、供应商评估、商品销量分析、热销榜单查询、类目浏览时触发此技能。本技能引导AI正确理解用户选品意图、选择合适的MCP工具、补全关键参数、并以视觉化方式（图片+表格+卡片）展示选品结果。触发本技能后，所有1688选品相关工具调用默认使用店雷达（dld MCP）连接器，工具包括 mcp__dld MCP__product_search_list、mcp__dld MCP__product_billboard_list、mcp__dld MCP__product_info、mcp__dld MCP__get_categ

Latest changelog:
1688选品库MCP服务引导技能初始发布。

- 提供详细的选品工作流，自动选择和调用1688选品相关的5个MCP工具，默认使用店雷达（dld MCP）连接器。
- 增加连接器可用性检查和贴心的引导配置流程，避免重复报错和误用。
- 规范参数构建和信息补全策略，支持宽泛搜索、条件细化和主动追问场景。
- 结果展示强调商品图片、链接和视觉化，多样化输出格式（卡片、表格、Markdown/HTML）。
- 加强数据解读与选品建议，为用户选品决策提供实际帮助。
- 丰富实用场景示例，全面覆盖选品、榜单、单品分析、类目浏览等需求。

**关键词**: 店雷达选品技能, 1688选品库MCP服务引导技能, 触发本技能后, MCP）连接器, 工具包括, mcp, dld, product

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dld-skills)

---

## [7. Image Audit](https://clawhub.ai/xiaowu89/skill-function)

**Slug**: `skill-function`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 719 | 🧩 2

**原始简介**: 对图片进行鉴黄、政治、暴恐内容审核。先将图片压缩到 500px/JPEG 后直传 NX API 审核，以表格汇总结果。适用于用户提到图片审核、内容检查、鉴黄、政治识别、暴恐识别、违规扫描、图片安全、JPG/PNG/WebP 审核的场景。

**中文介绍**: 对图片进行鉴黄、政治、暴恐内容审核。先将图片压缩到 500px/JPEG 后直传 NX API 审核，以表格汇总结果。适用于用户提到图片审核、内容检查、鉴黄、政治识别、暴恐识别、违规扫描、图片安全、JPG/PNG/WebP 审核的场景。

Latest changelog:
- Removed documentation and utility files: .gitignore, README.md, scripts directory, and skill-card.md.
- Updated SKILL.md with stricter .env Key detection and configuration instructions.
- Clarified .env lookup/handling, emphasizing real checks and not making unwarranted suggestions about Key presence.
- Adjusted sample script arguments and documentation details (e.g., --channel now uses "clawhub").
- No code or functional logic changes included—documentation and structural cleanup only.

**关键词**: 对图片进行鉴黄、政治、暴恐内容审核, 先将图片压缩到, 500px, 后直传, NX, Image, Audit, JPEG

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-function)

---

## [8. guaikei-xhs-hot-notes](https://clawhub.ai/engheng-art/guaikei-xhs-hot-notes)

**Slug**: `guaikei-xhs-hot-notes`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 把小红书关键词搜索、笔记详情、笔记评论、博主作品抓取为结构化数据，一次最多 1W 条。当用户需要先把小红书数据拿回来、再做汇总/对比/报告时使用本技能；即使用户没说"采集"或"抓取"，只要任务是从小红书获取内容数据也适用。不用于发布、互动或私密内容。

**中文介绍**: 把小红书关键词搜索、笔记详情、笔记评论、博主作品抓取为结构化数据，一次最多 1W 条。当用户需要先把小红书数据拿回来、再做汇总/对比/报告时使用本技能；即使用户没说"采集"或"抓取"，只要任务是从小红书获取内容数据也适用。不用于发布、互动或私密内容。

Latest changelog:
- 首次发布，支持对小红书公开内容的数据采集。
- 实现根据关键词搜索、获取笔记详情及评论、抓取博主公开作品等四大能力，每次最多可获取 10000 条结构化数据，适合内容分析与报告生成。
- 明确参数要求与调用路由，针对不同输入智能分发命令，并详列常见异常处理方法和调用限制。
- 仅采集公开数据，无需登录小红书账号，不支持交互操作或私密内容采集。

**关键词**: 一次最多, 1W, 当用户需要先把小红书数据拿回来、再做汇总, 对比, 报告时使用本技能, 即使用户没说"采集"或"抓取", 只要任务是从小红书获取内容数据也适用, guaikei-xhs-hot-notes

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-xhs-hot-notes)

---

## [9. guaikei-xhs-search-results](https://clawhub.ai/engheng-art/guaikei-xhs-search-results)

**Slug**: `guaikei-xhs-search-results`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 搜小红书笔记、看笔记详情、查笔记评论、查博主作品。当用户提到小红书并想拿到笔记/评论/博主数据时使用本技能；即使用户没说"数据"或"搜索"，只要给了关键词或小红书链接并想了解内容也适用。不用于其他平台或需登录的操作。

**中文介绍**: 搜小红书笔记、看笔记详情、查笔记评论、查博主作品。当用户提到小红书并想拿到笔记/评论/博主数据时使用本技能；即使用户没说"数据"或"搜索"，只要给了关键词或小红书链接并想了解内容也适用。不用于其他平台或需登录的操作。

Latest changelog:
- 首发版本，支持小红书（XHS）结构化数据的搜索与采集，无需登录账号。
- 四大核心功能：关键词笔记搜索、单笔记详情和评论获取、博主作品列表拉取、评论数据专拉。
- 智能输入路由，根据用户需求自动切换脚本处理关键词查询、笔记/博主链接等多种场景。
- 面向数据分析、内容创作、商业运营、市场调研等多重应用，返回统一结构化 JSON。
- 严格错误与异常管理，精细输入校验，并提供详细自助排查指引。
- 需配置 GUAIKEI_API_TOKEN 环境变量用于访问 guaikei.com 小红书公开数据。

**关键词**: 搜小红书笔记、看笔记详情、查笔记评论、查博主作品, 当用户提到小红书并想拿到笔记, 评论, 博主数据时使用本技能, 即使用户没说"数据"或"搜索", 只要给了关键词或小红书链接并想了解内容也适用, 不用于其他平台或需登录的操作, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-xhs-search-results)

---

## [10. Smart Incontinence Status Alert Skill | 智能失禁状态提醒技能](https://clawhub.ai/smyx-sunjinhui/smyx-incontinence-alert-analysis)

**Slug**: `smyx-incontinence-alert-analysis`  
**Version**: 1.0.10  
**Stats**: ⭐ 5 | ⬇️ 1309 | 🧩 11

**原始简介**: Automatically identifies wet clothing and abnormal excretion via visual AI. Instantly notifies caregivers to improve care for incontinent elderly, bedridden patients, and infants, reducing skin issues and complications. | 智能失禁状态提醒技能，基于视觉AI自动识别衣物潮湿、排泄异常等状况，第一时间推送通知给看护人员，提升失能老人、卧床病人、婴幼儿的护理质量，减少皮肤问题和并发症

**中文介绍**: Automatically identifies wet clothing and abnormal excretion via visual AI. Instantly notifies caregivers to improve care for incontinent elderly, bedridden patients, and infants, reducing skin issues and complications. | 智能失禁状态提醒技能，基于视觉AI自动识别衣物潮湿、排泄异常等状况，第一时间推送通知给看护人员，提升失能老人、卧床病人、婴幼儿的护理质量，减少皮肤问题和并发症

Latest changelog:
- Removed the file: skill-card.md
- No other functional or documentation changes in this release.

**关键词**: 智能失禁状态提醒技能, Smart, Incontinence, Status, Alert, Skill, Automatically, identifies

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-incontinence-alert-analysis)

---

## [11. guaikei-xhs-blogger-list](https://clawhub.ai/engheng-art/guaikei-xhs-blogger-list)

**Slug**: `guaikei-xhs-blogger-list`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 按最新排序获取小红书关键词下的近期笔记，捕捉平台热点风向。当用户想追小红书热点、监控某话题近期趋势、或提前布局内容时使用本技能；即使用户没说"趋势"，只要想了解某话题在小红书上最近的动静也适用。不用于跨平台趋势或历史回溯。

**中文介绍**: 按最新排序获取小红书关键词下的近期笔记，捕捉平台热点风向。当用户想追小红书热点、监控某话题近期趋势、或提前布局内容时使用本技能；即使用户没说"趋势"，只要想了解某话题在小红书上最近的动静也适用。不用于跨平台趋势或历史回溯。

Latest changelog:
guaikei-xhs-blogger-list 1.0.0 初始发布

- 支持按关键词实时获取小红书平台下最新笔记，便于趋势监控与热点内容捕捉。
- 提供四大核心能力：关键词搜索、笔记详情、博主作品监控、评论获取。
- 详细参数与调用路由说明，支持结构化结果 JSON 输出，方便后续分析与报告生成。
- 明确能力边界、输入要求与常见错误处理机制。
- 依赖 guaikei API，需配置 GUAIKEI_API_TOKEN 环境变量方可正常运行。

**关键词**: 按最新排序获取小红书关键词下的近期笔记, 捕捉平台热点风向, 即使用户没说"趋势", 只要想了解某话题在小红书上最近的动静也适用, 不用于跨平台趋势或历史回溯, guaikei-xhs-blogger-list, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-xhs-blogger-list)

---

## [12. Siluzan TSO](https://clawhub.ai/sigedev01-bit/siluzan-tso)

**Slug**: `siluzan-tso`  
**Version**: 1.1.44  
**Stats**: ⭐ 1 | ⬇️ 2473 | 🧩 34

**原始简介**: 丝路赞 TSO 广告平台（Google/Bing/Yandex/TikTok/Kwai/MetaAd），凡涉及丝路赞/TSO、投广告、出价预算、广告账户管理，或需要做行业分析/市场分析/行业分析报告（含「写一份 XX 行业报告」「电商/制造/医疗等行业报告」「市场调查/战略市场/KA 市场报告」「竞品/GTM/市场格局/行业趋势」等，无论是否提及丝路赞/广告/客户）须加载本 skill。【§零·最高优先】网址/域名/官网+诊断/检测/监测/评估/体检/报告/符合投放要求/能不能投（含「网络诊断」混说）→P8 website-diagnosis collect（禁纯WebFetch/肉眼看页），禁止P9/P1/W3、禁止A/B/C/D追问；细则见 intent-routing.md §零。【§零·B·次高优先】未命中§零时，行业/市场分析报告类话术→必走P9 market-analysis collect+render出HTML，禁止纯WebSearch/WebFetch在对话里写Markdown/HTML当终稿、禁止改走P8/P1/P4/W5/google-analysis；细则见 references/core/intent-routing.md §零·B。【§零·C·关键词规划】Google Ads/谷歌广告拓词、关键词规划/推荐、Keyword Planner、长尾关键词、月搜索量/搜索量、竞争度、核心词/种子词扩词（含「阅读网址/文章/页面后针对核心词出带搜索量词表」，无论是否提及丝路赞/TSO/账户）→必走W5 keyword -k … --google-only --json-out，禁止WebSearch/WebFetch编造搜索量当终稿；细则见 references/core/intent-routing.md §零·C。【报告/诊断消歧】其余报告类话术禁止默认某一CLI——行业/市场/战略/行业分析报告→P9 market-analysis（必走collect+render，禁止纯WebSearch代替）；Google账户ID+健康诊断→P1 google-ads-diagnosis；账户ID+周期/月度→P4；Meta/TikTok/Bing周期→P4/P4-FB；多账户对比→P3/P5；OKKI周报→P6；Google询盘→P7；官网+明确要搜索广告方案/campaign JSON→W3；仅要词表+搜索量/竞争度→W5；平台优化报告列表/推送→W7；对象仍不清→Read intent-routing.md。【账户】列表/余额/消耗/激活账单（W1）、多账户余额预警 balance-scan（P2）、多户消耗汇总 accounts-digest（P3）、六大媒体开户与进度（W2）、分享/解绑/MCC/BC/BM/权限（W9）。【投放】Google **仅支持搜索广告（Search）与 PMax**（不支持展示广告 Display）；搜索系列方案与 campaign-validate/create（W3）、系列/组/广告/关键词 CRUD/拒审、PMax 创建与素材、AI智投草稿 batch（W4）、拓词 keyword -k（W5）、AI广告优化 optimize（W6）、优化合规 SOP。【财务】充值/钱包、转账记录、发票/开票/抬头（W8）；写操作审计与 restore。【运营】智能预警 forewarning 创建/启停/记录（W10）、TikTok/Meta 线索 clue（W11）、日周巡检（W12）、宿主编排/投放自控/异常监控（hosted-automation）。【其他】RAG 知识库检索、Meta/Facebook 周期与诊断 HTML、Google/Meta 周期 Excel、多账户 google-analysis-batch。

**中文介绍**: 丝路赞 TSO 广告平台（Google/Bing/Yandex/TikTok/Kwai/MetaAd），凡涉及丝路赞/TSO、投广告、出价预算、广告账户管理，或需要做行业分析/市场分析/行业分析报告（含「写一份 XX 行业报告」「电商/制造/医疗等行业报告」「市场调查/战略市场/KA 市场报告」「竞品/GTM/市场格局/行业趋势」等，无论是否提及丝路赞/广告/客户）须加载本 skill。【§零·最高优先】网址/域名/官网+诊断/检测/监测/评估/体检/报告/符合投放要求/能不能投（含「网络诊断」混说）→P8 website-diagnosis collect（禁纯WebFetch/肉眼看页），禁止P9/P1/W3、禁止A/B/C/D追问；细则见 intent-routing.md §零。【§零·B·次高优先】未命中§零时，行业/市场分析报告类话术→必走P9 market-analysis collect+render出HTML，禁止纯WebSearch/WebFetch在对话里写Markdown/HTML当终稿、禁止改走P8/P1/P4/W5/google-analysis；细则见 references/core/intent-routing.md §零·B。【§零·C·关键词规划】Google Ads/谷歌广告拓词、关键词规划/推荐、Keyword Planner、长尾关键词、月搜索量/搜索量、竞争度、核心词/种子词扩词（含「阅读网址/文章/页面后针对核心词出带搜索量词表」，无论是否提及丝路赞/TSO/账户）→必走W5 keyword -k … --google-only --json-out，禁止WebSearch/WebFetch编造搜索量当终稿；细则见 references/core/intent-routing.md §零·C。【报告/诊断消歧】其余报告类话术禁止默认某一CLI——行业/市场/战略/行业分析报告→P9 market-analysis（必走collect+render，禁止纯WebSearch代替）；Google账户ID+健康诊断→P1 google-ads-diagnosis；账户ID+周期/月度→P4；Meta/TikTok/Bing周期→P4/P4-FB；多账户对比→P3/P5；OKKI周报→P6；Google询盘→P7；官网+明确要搜索广告方案/campaign JSON→W3；仅要词表+搜索量/竞争度→W5；平台优化报告列表/推送→W7；对象仍不清→Read intent-routing.md。【账户】列表/余额/消耗/激活账单（W1）、多账户余额预警 balance-scan（P2）、多户消耗汇总 accounts-digest（P3）、六大媒体开户与进度（W2）、分享/解绑/MCC/BC/BM/权限（W9）。【投放】Google **仅支持搜索广告（Search）与 PMax**（不支持展示广告 Display）；搜索系列方案与 campaign-validate/create（W3）、系列/组/广告/关键词 CRUD/拒审、PMax 创建与素材、AI智投草稿 batch（W4）、拓词 keyword -k（W5）、AI广告优化 optimize（W6）、优化合规 SOP。【财务】充值/钱包、转账记录、发票/开票/抬头（W8）；写操作审计与 restore。【运营】智能预警 forewarning 创建/启停/记录（W10）、TikTok/Meta 线索 clue（W11）、日周巡检（W12）、宿主编排/投放自控/异常监控（hosted-automation）。【其他】RAG 知识库检索、Meta/Facebook 周期与诊断 HTML、Google/Meta 周期 Excel、多账户 google-analysis-batch。

Latest changelog:
**Google Ads Display 相关能力收紧，明确仅支持 Search/PMax：**

- 明确 skill 仅支持 Google 搜索广告（Search）与 Performance Max（PMax），不再支持/假装支持展示广告（Display/RDA）相关需求。
- 在文档和路由表中，新增对 Display 需求的路由说明：遇 Display/RDA 需直接告知用户“不支持”，建议使用 Search 或 PMax。
- CLI 与工作流交付规范更新：ad batch diff 输出须即时原样交付给用户，不得摘要或延迟。
- 用词与即时规范细化多项说明，并同步 route/workflow 表和辅助文档，消除模糊空间。
- 删除 skill-card.md、优化并统一多处分流与边界描述。

**关键词**: 丝路赞, Siluzan, TSO, 广告平台（Google, Bing, Yandex, TikTok, Kwai

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/siluzan-tso)

---

## [13. guaikei-xhs-comment-data](https://clawhub.ai/engheng-art/guaikei-xhs-comment-data)

**Slug**: `guaikei-xhs-comment-data`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 单独获取小红书笔记的评论内容、评论者信息与互动数据，便于观点聚类与情绪分析。当用户想分析某条小红书笔记评论区在讨论什么、识别高频反馈或负面声音时使用本技能；即使用户没说"评论分析"，只要给了笔记链接并关心受众反馈也适用。与笔记详情的区别：只取评论不取正文。不用于发评论或互动。

**中文介绍**: 单独获取小红书笔记的评论内容、评论者信息与互动数据，便于观点聚类与情绪分析。当用户想分析某条小红书笔记评论区在讨论什么、识别高频反馈或负面声音时使用本技能；即使用户没说"评论分析"，只要给了笔记链接并关心受众反馈也适用。与笔记详情的区别：只取评论不取正文。不用于发评论或互动。

Latest changelog:
guaikei-xhs-comment-data v1.0.0

- 首发版本，支持获取小红书指定笔记的评论内容、评论者信息与互动数据，便于观点聚类和情绪分析。
- 区分笔记详情与评论数据，单独提供纯评论数据输出。
- 命令行工具支持关键词搜索、笔记详情、博主作品列表与笔记评论四类场景。
- 明确输入要求、触发规则和常见反馈处理方式，提升易用性和稳定性。
- 输出结构化 JSON，适合后续内容分析与报告生成。

**关键词**: 便于观点聚类与情绪分析, 即使用户没说"评论分析", 只要给了笔记链接并关心受众反馈也适用, 与笔记详情的区别, 只取评论不取正文, 不用于发评论或互动, guaikei-xhs-comment-data, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-xhs-comment-data)

---

## [14. guaikei-xhs-note-data](https://clawhub.ai/engheng-art/guaikei-xhs-note-data)

**Slug**: `guaikei-xhs-note-data`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 获取小红书博主公开作品及单篇笔记的真实点赞/评论/收藏数据，评估其互动质量。当用户要筛选小红书 KOL、判断博主数据是否注水、或为合作决策准备依据时使用本技能；即使用户没提"KOL"，只要想了解某个小红书博主的真实互动水平也适用。不用于粉丝数估算或后台数据。

**中文介绍**: 获取小红书博主公开作品及单篇笔记的真实点赞/评论/收藏数据，评估其互动质量。当用户要筛选小红书 KOL、判断博主数据是否注水、或为合作决策准备依据时使用本技能；即使用户没提"KOL"，只要想了解某个小红书博主的真实互动水平也适用。不用于粉丝数估算或后台数据。

Latest changelog:
guaikei-xhs-note-data 1.0.0 – 初始发布

- 新增获取小红书博主公开作品及单篇笔记真实点赞、评论、收藏数据的能力，用于互动质量评估。
- 支持四大核心功能：关键词搜索、笔记详情、博主作品监控、笔记评论获取。
- 路由规则详细，确保输入正确匹配相应脚本，提升数据准确性。
- 明确边界：仅处理小红书公开内容，不触及私密或需登录操作。
- 提供详细使用说明、错误处理建议和常见问题自查方法。

**关键词**: 获取小红书博主公开作品及单篇笔记的真实点赞, 评论, 收藏数据, 评估其互动质量, 当用户要筛选小红书, 即使用户没提"KOL", 只要想了解某个小红书博主的真实互动水平也适用, guaikei-xhs-note-data

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-xhs-note-data)

---

## [15. Maybeai Sheet Cli Skill](https://clawhub.ai/no7dw/maybeai-sheet-cli)

**Slug**: `maybeai-sheet-cli`  
**Version**: 0.20.4  
**Stats**: ⭐ 0 | ⬇️ 1390 | 🧩 31

**原始简介**: Inspect, import, edit, dashboard, template, and share MaybeAI spreadsheets

**中文介绍**: Inspect, import, edit, dashboard, template, and share MaybeAI spreadsheets

Latest changelog:
bump: v0.20.4

**关键词**: Maybeai, Sheet, Cli, Skill, Inspect, import, edit, dashboard

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/maybeai-sheet-cli)

---

## [16. webclaw3 — Browser Automation with Your Own Logged-in Chrome](https://clawhub.ai/fatmind/webclaw3-browser-automation)

**Slug**: `webclaw3-browser-automation`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 93 | 🧩 1

**原始简介**: Web scraping & browser automation that runs in YOUR own Chrome with YOUR logins — pull data from login-only sites (X, Reddit, Shopify, Amazon Seller, LinkedIn, Xiaohongshu) with no re-login, no shared passwords, no anti-bot blocks. Then say "distill this" and that one run becomes a zero-token local script you can schedule daily; when the site redesigns, it is repaired locally for free. Setup: 3 steps, ~5 min. 中文：浏览器自动化 / 网页抓取 / 数据采集 / 爬虫 / 登录态 / 反爬 / 定时任务

**中文介绍**: Web scraping & browser automation that runs in YOUR own Chrome with YOUR logins — pull data from login-only sites (X, Reddit, Shopify, Amazon Seller, LinkedIn, Xiaohongshu) with no re-login, no shared passwords, no anti-bot blocks. Then say "distill this" and that one run becomes a zero-token local script you can schedule daily; when the site redesigns, it is repaired locally for free. Setup: 3 steps, ~5 min. 中文：浏览器自动化 / 网页抓取 / 数据采集 / 爬虫 / 登录态 / 反爬 / 定时任务

Latest changelog:
First ClawHub release: browser automation driven by your own logged-in Chrome; explore once, distill into a free deterministic skill.

**关键词**: webclaw3, Browser, Automation, Own, Logged-in, Chrome, Web, scraping

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/webclaw3-browser-automation)

---

## [17. guaikei-xhs-see-details](https://clawhub.ai/engheng-art/guaikei-xhs-see-details)

**Slug**: `guaikei-xhs-see-details`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 抓取小红书博主公开作品列表并配合笔记详情与评论，还原其发文节奏、内容风格与互动表现。当用户要分析小红书竞品账号、监控对手博主最近发了什么、或为差异化策略准备数据时使用本技能；即使用户没说"竞品分析"，只要给了博主主页链接并想了解其内容表现也适用。不用于登录态或私密数据。

**中文介绍**: 抓取小红书博主公开作品列表并配合笔记详情与评论，还原其发文节奏、内容风格与互动表现。当用户要分析小红书竞品账号、监控对手博主最近发了什么、或为差异化策略准备数据时使用本技能；即使用户没说"竞品分析"，只要给了博主主页链接并想了解其内容表现也适用。不用于登录态或私密数据。

Latest changelog:
- Initial release of the guaikei-xhs-see-details skill for public Xiaohongshu (RED) data analysis.
- Supports keyword search, note details with comments, creator post monitoring, and standalone comment extraction.
- Includes robust routing based on user input (keyword, note link, creator profile), with clear error handling and user prompts.
- Returns up to 10,000 structured data records in JSON format for downstream analysis or reporting.
- Requires GUAIKEI_API_TOKEN for API access; operates on public, non-login data only.
- Usage, parameter details, and troubleshooting are provided for smooth integration and operation.

**关键词**: 抓取小红书博主公开作品列表并配合笔记详情与评论, 还原其发文节奏、内容风格与互动表现, 即使用户没说"竞品分析", 只要给了博主主页链接并想了解其内容表现也适用, 不用于登录态或私密数据, guaikei-xhs-see-details, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-xhs-see-details)

---

## [18. guaikei-xhs-check-blogger](https://clawhub.ai/engheng-art/guaikei-xhs-check-blogger)

**Slug**: `guaikei-xhs-check-blogger`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 按关键词搜索小红书公开笔记，支持按点赞/评论/收藏排序与时间筛选，返回笔记列表与互动数据。当用户想做小红书选题调研、找高赞爆款、看某关键词最近热度、或对比多个关键词表现时使用本技能；即使用户只说"最近什么火""帮我找热门内容"而没点名小红书，只要语境是社媒内容挖掘也适用。不用于其他平台或需登录的内容。

**中文介绍**: 按关键词搜索小红书公开笔记，支持按点赞/评论/收藏排序与时间筛选，返回笔记列表与互动数据。当用户想做小红书选题调研、找高赞爆款、看某关键词最近热度、或对比多个关键词表现时使用本技能；即使用户只说"最近什么火""帮我找热门内容"而没点名小红书，只要语境是社媒内容挖掘也适用。不用于其他平台或需登录的内容。

Latest changelog:
Initial release of guaikei-xhs-check-blogger:

- Search and analyze public Xiaohongshu (小红书) posts by keyword, with sorting and time filters.
- Retrieve post details, comments, or monitor a blogger's recent public works without login.
- Structured JSON output for further review, clustering, or reporting.
- Handles up to 10,000 entries per request via public guaikei.com API.
- Automatic routing based on input (keyword, note link, or profile link).
- Includes clear input validation, error handling, and guidance for users.

**关键词**: 按关键词搜索小红书公开笔记, 支持按点赞, 评论, 收藏排序与时间筛选, 返回笔记列表与互动数据, 只要语境是社媒内容挖掘也适用, 不用于其他平台或需登录的内容, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-xhs-check-blogger)

---

## [19. X-ray](https://clawhub.ai/ppshux/x-ray)

**Slug**: `x-ray`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 扫描一个陌生的软件项目，快速识别项目类型、技术栈、架构、文件结构、复杂度和学习价值。适用于用户希望快速理解、探索、检查或接手一个陌生代码库的场景。

**中文介绍**: 扫描一个陌生的软件项目，快速识别项目类型、技术栈、架构、文件结构、复杂度和学习价值。适用于用户希望快速理解、探索、检查或接手一个陌生代码库的场景。

Latest changelog:
Initial release of the x-ray skill for project analysis.

- Scans a software project's directory structure and identifies its type and tech stack.
- Detects key directories, critical files, and infers overall architecture.
- Evaluates project complexity and suggests suitable learners.
- Recommends a reading order for understanding the project.
- Generates a visual HTML report based on static analysis, prioritizing security and read-only access.

**关键词**: 扫描一个陌生的软件项目, of, X-ray, Latest, changelog, Initial, release, skill

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/x-ray)

---

## [20. nevermined-router](https://clawhub.ai/nevermined-io/nevermined-router)

**Slug**: `nevermined-router`  
**Version**: 0.1.2  
**Stats**: ⭐ 0 | ⬇️ 184 | 🧩 3

**原始简介**: Use when an AI agent needs to PAY an external service it does not have an account with — any x402 agent or MPP merchant — using the Nevermined Router. Covers discovering services in the Agent Services Catalog, creating a spending Delegation from an API key, funding the buyer wallet, making paid calls through /api/v1/router/route (or the streaming /proxy), reading the payment ledger, and the guardrails an autonomous buyer must respect. Complements the nevermined-payments skill, which is about RECEIVING payments and buying Nevermined plans.

**中文介绍**: Use when an AI agent needs to PAY an external service it does not have an account with — any x402 agent or MPP merchant — using the Nevermined Router. Covers discovering services in the Agent Services Catalog, creating a spending Delegation from an API key, funding the buyer wallet, making paid calls through /api/v1/router/route (or the streaming /proxy), reading the payment ledger, and the guardrails an autonomous buyer must respect. Complements the nevermined-payments skill, which is about RECEIVING payments and buying Nevermined plans.

Latest changelog:
## nevermined-router 0.1.2

- Minor documentation updates in SKILL.md and references.
- skill-card.md file removed.
- No user-facing feature changes or new functionality in this release.

**关键词**: an, Agent, nevermined-router, Use, when, needs, PAY, external

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nevermined-router)

---

## [21. guaikei-xhs-get-comments](https://clawhub.ai/engheng-art/guaikei-xhs-get-comments)

**Slug**: `guaikei-xhs-get-comments`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 搜索小红书公开笔记、查看笔记详情与评论、获取笔记评论数据、抓取博主公开作品列表——返回结构化数据用于爆款挖掘、竞品分析、KOL筛选与趋势洞察。当用户想找小红书上的爆款内容、分析某篇笔记或其评论区、监控某博主发文、或调研某关键词在小红书的热度时使用本技能；即使用户没明确说"小红书"或"数据"，只要提到"红笔记""xhs"，或给出 xiaohongshu.com / xhslink.com 链接并想拿内容数据，也适用。不用于登录、发布、点赞或获取私密内容。

**中文介绍**: 搜索小红书公开笔记、查看笔记详情与评论、获取笔记评论数据、抓取博主公开作品列表——返回结构化数据用于爆款挖掘、竞品分析、KOL筛选与趋势洞察。当用户想找小红书上的爆款内容、分析某篇笔记或其评论区、监控某博主发文、或调研某关键词在小红书的热度时使用本技能；即使用户没明确说"小红书"或"数据"，只要提到"红笔记""xhs"，或给出 xiaohongshu.com / xhslink.com 链接并想拿内容数据，也适用。不用于登录、发布、点赞或获取私密内容。

Latest changelog:
Initial release of guaikei-xhs-get-comments.

- Enables keyword search, note detail & comment retrieval, and creator post monitoring for Xiaohongshu (小红书) public data.
- Provides four main CLI scripts: search, detail, comment, and post, each tailored for a specific data retrieval scenario.
- Returns structured JSON data, supporting downstream analysis such as trend discovery, competitor benchmarking, and influencer insights.
- Includes robust input validation, clear error handling, and explicit routing logic based on user intent and link type.
- Does not require login; supports up to 10,000 data items per request; output suited for further reporting or content analysis.

**关键词**: 即使用户没明确说"小红书"或"数据", 只要提到"红笔记""xhs", 或给出, 链接并想拿内容数据, 也适用, guaikei-xhs-get-comments, xiaohongshu.com, xhslink.com

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-xhs-get-comments)

---

## [22. HuaHuaDailyMCP](https://clawhub.ai/baiye1997/huahua-daily)

**Slug**: `huahua-daily`  
**Version**: 3.5.4  
**Stats**: ⭐ 1 | ⬇️ 2157 | 🧩 31

**原始简介**: Use HuahuaDaily MCP for authorized portfolio and transaction queries, fund and market data, strategy backtests and quant snapshots, community actions, screenshot recognition, and App-confirmed trade or import requests. Trigger when users ask about their HuahuaDaily holdings or cloud sync, request fund or market analysis through HuahuaDaily, run or review portfolio backtests, save or review strategy snapshots, use HuahuaDaily community features, or send transactions/imports for App confirmation.

**中文介绍**: Use HuahuaDaily MCP for authorized portfolio and transaction queries, fund and market data, strategy backtests and quant snapshots, community actions, screenshot recognition, and App-confirmed trade or import requests. Trigger when users ask about their HuahuaDaily holdings or cloud sync, request fund or market analysis through HuahuaDaily, run or review portfolio backtests, save or review strategy snapshots, use HuahuaDaily community features, or send transactions/imports for App confirmation.

Latest changelog:
版本对齐：MCP 3.5.4，新增estimate_frame_contract、night_estimate_contract、fund_estimate_helpers、default_funds、reports等模块，tool_registry增强，portfolio_math重构，client超时优化

**关键词**: HuaHuaDailyMCP, Use, HuahuaDaily, MCP, authorized, portfolio, transaction, queries

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/huahua-daily)

---

## [23. 189mail-daily-fetch](https://clawhub.ai/xizhima/189mail-daily-fetch)

**Slug**: `189mail-daily-fetch`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Automatically log in to 189.cn mailbox, fetch the latest email, and save it as .eml file to the desktop. Use when user wants to download the newest email from 189 mailbox, or needs to set up scheduled daily email fetching. Triggers include 下载最新邮件, 获取189邮箱最新邮件, 每天自动取邮件, 189邮箱, fetch latest email, dai

**中文介绍**: Automatically log in to 189.cn mailbox, fetch the latest email, and save it as .eml file to the desktop. Use when user wants to download the newest email from 189 mailbox, or needs to set up scheduled daily email fetching. Triggers include 下载最新邮件, 获取189邮箱最新邮件, 每天自动取邮件, 189邮箱, fetch latest email, dai

Latest changelog:
189mail-daily-fetch 1.0.0 — Initial release

- Automatically logs in to 189.cn mailbox using user-provided credentials.
- Fetches and downloads the latest email from the inbox as a .eml file.
- Saves the downloaded email directly to the desktop.
- Supports scheduled daily email downloading and archiving.
- Reports subject, sender, timestamp, and file location to the user.
- Handles 189.cn's iframe login and special UI considerations.

**关键词**: 189.cn, 189mail-daily-fetch, Automatically, log, mailbox, fetch, latest, email

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/189mail-daily-fetch)

---

## [24. guaikei-xhs-find-notes](https://clawhub.ai/engheng-art/guaikei-xhs-find-notes)

**Slug**: `guaikei-xhs-find-notes`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 搜索小红书公开笔记、查看笔记详情、获取笔记评论、抓取博主公开作品，返回结构化数据用于爆款挖掘、竞品分析、KOL筛选与评论洞察。当用户想找小红书内容、分析笔记或评论、监控博主发文、调研关键词热度时使用本技能；即使没明说"小红书"，只要提到红笔记、xhs、rednote，或给出 xiaohongshu.com / xhslink.com 链接并想拿内容数据也适用。不用于登录、发布、点赞或获取私密内容。

**中文介绍**: 搜索小红书公开笔记、查看笔记详情、获取笔记评论、抓取博主公开作品，返回结构化数据用于爆款挖掘、竞品分析、KOL筛选与评论洞察。当用户想找小红书内容、分析笔记或评论、监控博主发文、调研关键词热度时使用本技能；即使没明说"小红书"，只要提到红笔记、xhs、rednote，或给出 xiaohongshu.com / xhslink.com 链接并想拿内容数据也适用。不用于登录、发布、点赞或获取私密内容。

Latest changelog:
Initial release: Enables structured, large-scale extraction and analysis of public Xiaohongshu (RED) note, comment, and creator data via command line.

- Supports keyword-based note search, note detail retrieval, comment extraction, and creator post monitoring.
- Automatically selects collection mode based on input (search term or various link types).
- Clearly distinguishes functionalities between note, creator, and comment data pulls with robust input validation and error handling.
- Returns well-structured JSON output, suitable for further analysis such as trending topic discovery, competitor analysis, KOL selection, and comment insight.
- Does not support login, publishing, or manipulation of private/hidden data; strictly limited to public Xiaohongshu content.

**关键词**: 即使没明说"小红书", 只要提到红笔记、xhs、rednote, 或给出, 链接并想拿内容数据也适用, 不用于登录、发布、点赞或获取私密内容, guaikei-xhs-find-notes, xiaohongshu.com, xhslink.com

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-xhs-find-notes)

---

## [25. guaikei-xhs-look-up](https://clawhub.ai/engheng-art/guaikei-xhs-look-up)

**Slug**: `guaikei-xhs-look-up`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 当用户需要按关键词搜索小红书笔记、查看某篇笔记详情与评论、单独获取笔记评论数据、或抓取某博主公开作品列表时调用；返回结构化数据用于爆款挖掘、竞品监控、KOL筛选与趋势洞察，不做账号登录与内容发布

**中文介绍**: 当用户需要按关键词搜索小红书笔记、查看某篇笔记详情与评论、单独获取笔记评论数据、或抓取某博主公开作品列表时调用；返回结构化数据用于爆款挖掘、竞品监控、KOL筛选与趋势洞察，不做账号登录与内容发布

Latest changelog:
- 初始发布，支持按关键词搜索小红书笔记、查阅笔记详情及评论、获取博主公开作品、单独拉取评论数据  
- 所有指令均返回结构化 JSON，用于爆款挖掘、竞品监控、KOL 筛选与趋势洞察  
- 输入灵活，自动路由到关键词搜索、笔记详情、博主作品监控或评论获取脚本  
- 明确输入要求和错误处理，遇到参数缺失、类型不符、无结果等均有指引  
- 仅处理公开数据，不涉及登录、发布、互动及私密内容

**关键词**: 不做账号登录与内容发布, 初始发布, 所有指令均返回结构化, 用于爆款挖掘、竞品监控、KOL, guaikei-xhs-look-up, Latest, changelog, JSON

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-xhs-look-up)

---

