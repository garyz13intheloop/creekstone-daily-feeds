# ClawHub Skills Daily | 2026-03-07

> 共 25 个 skills

## [1. stock trading agents](https://clawhub.ai/ganyu21/trading-agents)

**Slug**: `trading-agents`  
**Version**: 1.0.5  
**Stats**: ⭐ 1 | ⬇️ 57 | 🧩 6

**原始简介**: 基于 AgentScope 的多智能体股票诊断系统。用于股票分析、生成投资报告，或构建多智能体协作的 AI 金融分析工作流。

**中文介绍**: 这是一个基于 AgentScope 的多智能体股票诊断系统，可用于股票数据解读、生成投资分析报告，以及搭建多智能体协作的 AI 金融分析工作流。能力边界在于其输出依赖所接入的数据源与模型推理，无法保证实时行情覆盖、预测必然准确或替代合规投顾决策，适合作为研究与辅助分析工具。典型场景包括多角色协作完成基本面/技术面/风险提示的分工诊断、自动化整理研报式结论与依据、将金融分析流程编排成可复用的 Agent 工作流。关键技术形态是多 Agent 编排与工具/技能调用机制，并通过新增的 skill.json 规范化技能元数据以提升技能管理与扩展一致性。

**关键词**: 多智能体系统, 股票诊断, 股票分析, 投资报告生成, AI金融分析, 智能体协作工作流, 技能元数据, stock

**评分**: 36

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/trading-agents)

---

## [2. AgentGo Cloud Browser](https://clawhub.ai/tammy-hash/agentgo-browser)

**Slug**: `agentgo-browser`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Automates browser interactions using AgentGo's distributed cloud browser cluster via playwright@1.51.0. Use when the user needs to navigate websites, interac...

**中文介绍**: 该能力通过 playwright@1.51.0 连接 AgentGo 分布式云浏览器集群，实现无需本地浏览器的网页自动化操作。典型场景是需要跨站点导航、页面交互、表单填写与流程验证等基于真实浏览器环境的任务。能力边界在于主要覆盖浏览器会话连接与管理及自动化执行，本身不提供网站业务语义理解或通用数据治理能力。关键技术形态为云端分布式浏览器集群 + Playwright 协议接入 + 会话/连接管理封装。

**关键词**: 云端浏览器, 浏览器自动化, 分布式浏览器集群, 连接管理, 无本地浏览器运行, 网页导航交互, 自动化脚本示例, AgentGo

**评分**: 40

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agentgo-browser)

---

## [3. Clawhub Skill](https://clawhub.ai/Kintupercy/agentcall)

**Slug**: `agentcall`  
**Version**: 2.0.1  
**Stats**: ⭐ 0 | ⬇️ 145 | 🧩 3

**原始简介**: Give your agent real phone numbers for SMS, OTP verification, and voice calls via the AgentCall API.

**中文介绍**: AgentCall API 可为智能体提供真实手机号能力，用于接收/发送短信、进行 OTP 验证以及语音通话，但能力边界强调仅限合法、合规的场景（如产品与业务的 QA 测试），并通过可接受使用政策约束滥用风险。典型场景包括对注册登录、双因素认证、通知短信与语音回呼等真实链路进行端到端验证与回归测试。关键技术形态是通过统一的 AgentCall API 调用实现号码分配与通信编排，并以面向“合法 QA 测试”的 OTP 示例与策略控制来指导接入与使用。

**关键词**: 智能体工具, 电话号资源分配, 语音通话 API, 短信验证码测试, 虚拟电话号码, 电信服务集成, QA 测试, Clawhub

**评分**: 49

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agentcall)

---

## [4. ClawCierge](https://clawhub.ai/yhyatt/openclaw-reservation)

**Slug**: `openclaw-reservation`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 84 | 🧩 2

**原始简介**: Restaurant search and booking for OpenClaw. Finds and books restaurants worldwide — Israel via direct API (Ontopo + Tabit), Europe and NYC via browser handof...

**中文介绍**: OpenClaw 提供全球餐厅搜索与订座能力：在以色列通过直连 API（Ontopo + Tabit）完成查询与预订，在欧洲和纽约等区域则通过浏览器自动化方式代办下单。能力边界在于覆盖范围取决于接入的 API 供给与可自动化的网页流程，且对登录、反爬、座位实时性等外部条件敏感。典型场景是用户按地点/时间/人数筛选餐厅并一键完成预订，关键技术形态为多源数据检索、API 集成与浏览器端自动化执行。最新变更仅新增 MIT 许可证，无功能变化。

**关键词**: 餐厅搜索, 餐厅预订, 全球餐厅覆盖, 旅行餐饮, 预订工作流, 浏览器自动化, ClawCierge, Restaurant

**评分**: 40

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openclaw-reservation)

---

## [5. GClaw](https://clawhub.ai/yhyatt/gclaw)

**Slug**: `gclaw`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 80 | 🧩 2

**原始简介**: Gmail inbox intelligence for OpenClaw. Reads, classifies, and digests your Gmail so the important stuff surfaces without the noise. Use when fetching new ema...

**中文介绍**: 这是一个面向 OpenClaw 的 Gmail 收件箱智能能力，用于读取并分析你的 Gmail 邮件，将邮件进行分类与摘要提炼，让重要信息从噪声中优先浮现。能力边界在于仅处理 Gmail 邮件内容的获取与智能整理，不涉及功能性变更或其他系统侧的业务操作。典型场景是拉取新邮件后自动筛选重点、快速生成要点回顾，帮助减少收件箱信息负担。关键技术形态主要是基于邮件抓取/解析与文本分类、摘要生成的自动化信息处理链路。

**关键词**: 邮件抓取, 收件箱智能, 邮件分类, 邮件摘要, 邮件优先级排序, 信息降噪, 邮箱自动化, GClaw

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gclaw)

---

## [6. reCamera Intellisense](https://clawhub.ai/iChizer0/recamera-intellisense)

**Slug**: `recamera-intellisense`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Registers reCamera devices, configures AI detection models/rules/schedules, monitors and clears detection events, fetches event snapshots, and runs manual im...

**中文介绍**: 该能力用于对 reCamera 设备进行注册与管理，配置 AI 检测模型/规则/日程，并对检测事件进行监控、清理与事件快照拉取，也支持触发手动图像采集等操作。能力边界在于依赖 reCamera v2 未公开硬件与实验性固件，当前可用性与稳定性受限且需等待正式发布。典型场景包括安防/门店/工地等视频端侧的目标检测告警管理、按时间段启停规则、事后回溯与取证快照。关键技术形态是端侧摄像头设备管理 + AI 检测规则引擎/调度 + 事件流与快照数据接口的组合。

**关键词**: 智能摄像头管理, IoT 设备注册, 边缘视觉, 目标检测, 检测规则引擎, 检测调度, 告警事件管理, 事件快照抓拍, 固件集成

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/recamera-intellisense)

---

## [7. ClawSavings](https://clawhub.ai/yhyatt/clawsavings)

**Slug**: `clawsavings`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: מספק מידע על כרטיסי אשראי, מועדונים ושוברים לחסכון בכל חנות ישראלית, כולל השוואת הנחות ומחירים מעודכנים.

**中文介绍**: 该产品用于把任意以色列门店映射到最优的信用卡/会员俱乐部/代金券省钱方案，并提供折扣对比与更新的价格信息，覆盖约 72 家门店与 14 个品类。能力边界在于优惠数据依赖既定来源（如 HTZone Card/Club、Poalim Wonder 等）与缓存价格，无法保证覆盖所有门店或实时全量准确，且仅能在已有规则与数据范围内做推荐与比较。典型场景是用户在结账前或选购时快速判断用哪张卡、哪个俱乐部或哪种券最划算。关键技术形态为“结构化知识 + 交易价格缓存”的双层知识库，通过按需加载与缓存实现显著的 token/成本优化。

**关键词**: 代金券优惠, 折扣比价, 门店优惠映射, 以色列零售商户, 优惠交易聚合, 分层知识库, 价格缓存, 上下文压缩

**评分**: 35

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/clawsavings)

---

## [8. BizyAir API出图](https://clawhub.ai/bozoyan/bizyair-images)

**Slug**: `bizyair-images`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 基于 BizyAir 异步 API 的模块化图片生成助手，支持多工作流模板（web_app_id）动态切换与自定义传参。

**中文介绍**: 这是一个基于 BizyAir 异步 API 的模块化图片生成助手，能力边界在于通过“创建任务-查询结果”的两步流程调用既有工作流模板（web_app_id）并按参数生成与批量输出图片，不负责训练模型或提供超出 BizyAir 接口范围的编辑能力。典型场景包括在不同业务/风格模板间快速切换生成图、按常见尺寸规格批量出图，以及人物/模特类生成时自动补充提示词以提升人像效果。关键技术形态是异步任务队列式调用、模板化工作流动态路由与参数透传、尺寸规格映射、任务状态提醒与多图结果表格展示，并强化错误提示与密钥安全处理。

**关键词**: 异步图像生成 API, 工作流模板切换, 模块化生成管线, 提示词自动增强, 人像生成优化, 批量图片生成, 图片尺寸规格映射, 任务状态轮询, API 密钥管理

**评分**: 17

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bizyair-images)

---

## [9. Pangolinfo Search & Amazon Scraper](https://clawhub.ai/tammy-hash/pangolinfo-scrape)

**Slug**: `pangolinfo-scrape`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Search Google and scrape Amazon using Pangolin APIs. Supports AI Mode search (Google AI Overview with multi-turn dialogue), standard SERP with AI Overview ex...

**中文介绍**: 该能力通过 Pangolin APIs 实现 Google 搜索与 Amazon 数据抓取，支持 Google AI Mode（含多轮对话式 AI Overview）与标准 SERP 结果并附带 AI Overview。典型场景包括检索并汇总最新网页信息、基于搜索结果进行对话式追问，以及抓取 Amazon 商品与关键词相关数据用于选品与竞品分析。能力边界在于仅覆盖 Google/Amazon 相关检索与抓取，不负责站内交易流程、复杂反爬环境下的稳定可用性或对抓取内容的真实性与合规性背书。关键技术形态为统一 API 调用的搜索/抓取接口，输出结构化 SERP、AI Overview 及 Amazon 商品与关键词数据。

**关键词**: 多轮对话检索, 网页抓取, 电商情报采集, 自动化数据采集, 技能插件集成, Pangolinfo, Search, Amazon

**评分**: 28

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pangolinfo-scrape)

---

## [10. AetherLang Ω V3](https://clawhub.ai/contrario/aetherlang)

**Slug**: `aetherlang`  
**Version**: 2.0.3  
**Stats**: ⭐ 2 | ⬇️ 922 | 🧩 10

**原始简介**: Execute AI workflow orchestration flows using the AetherLang Ω DSL. Run multi-step AI pipelines for recipes, business strategy, market analysis, molecular ga...

**中文介绍**: 该能力用于通过 AetherLang Ω DSL 编排并执行 AI 工作流，支持将多步骤的模型调用与工具链串联成可复用的流水线，覆盖配方生成、商业策略、市场分析、分子相关探索等典型任务。能力边界在于它侧重“流程编排与执行”，实际效果依赖所接入的模型与外部工具数据质量，不替代领域专家的最终判断。关键技术形态是基于 DSL 的工作流定义、步骤级调度与上下文传递，以及对多阶段 AI pipeline 的统一运行与管理。

**关键词**: 工作流编排, 领域特定语言（DSL）, 声明式流程, 多步骤管线, AI任务自动化, 技能插件（Skill）, 业务策略分析, 市场分析自动化, 分子生成管线

**评分**: 47

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aetherlang)

---

## [11. 微信公众号工具包](https://clawhub.ai/Mr-Q526/wechat-toolkit)

**Slug**: `wechat-toolkit`  
**Version**: 1.0.1  
**Stats**: ⭐ 1 | ⬇️ 308 | 🧩 2

**原始简介**: 微信公众号一站式工具包 — 集成文章搜索、文章下载、AI洗稿改写、公众号发布四大功能。当用户需要搜索/下载/改写/发布微信公众号文章时使用。

**中文介绍**: 这是一个面向微信公众号内容生产与运营的一站式工具包，覆盖文章搜索、下载、AI改写与发布全流程，适用于需要快速获取素材、二次编辑并一键投放到公众号的场景。能力边界在于主要处理公众号文章的检索与抓取、文本改写与自动化发布编排，不包含内容合规审核、账号风控与反爬对抗等保障能力，且依赖外部环境与账号权限。关键技术形态上包含下载器模块与脚本化自动化流水线，发布能力已从 shell/python 迁移为 Node.js 实现，并已扩展支持 Windows 平台。

**关键词**: 微信公众号运营, 公众号文章搜索, 公众号文章下载, 内容抓取, 文本改写, 内容去重改写, 自动化发布, 命令行工具, 视频内容发布

**评分**: 16

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/wechat-toolkit)

---

## [12. Reddit Cultivate](https://clawhub.ai/PHY041/phy-reddit-cultivate)

**Slug**: `phy-reddit-cultivate`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Reddit account cultivation for indie developers. Uses AppleScript to control real Chrome — undetectable by anti-bot systems. Checks karma, finds rising posts...

**中文介绍**: 该工具面向独立开发者做 Reddit 账号“养号”和互动运营，通过 AppleScript 驱动真实的 Chrome 浏览器执行浏览、检查 karma、发现热度上升帖子等操作。能力边界在于它主要覆盖基于网页端的半自动化行为编排与信息采集，不保证对平台风控长期有效，也不涉及绕过登录/验证码等强认证环节。典型场景是日常账号活跃、内容/评论机会发现与节奏控制；关键技术形态为 AppleScript + 本地真实浏览器自动化（非无头）配合页面状态读取。

**关键词**: 账号养号, 反机器人检测规避, 人类行为模拟, 社交媒体增长工具, 独立开发者推广, Reddit, Cultivate, account

**评分**: 26

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/phy-reddit-cultivate)

---

## [13. Social Posting](https://clawhub.ai/PHY041/phy-social-posting)

**Slug**: `phy-social-posting`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Multi-platform social media posting service with automatic provider failover. Handles posting to 9 platforms (Twitter/X, LinkedIn, Instagram, Facebook, TikTo...

**中文介绍**: 这是一个面向多平台的社交媒体自动发布服务，支持向约 9 个平台（如 X/Twitter、LinkedIn、Instagram、Facebook 等）统一提交内容并分发。其能力边界主要在“发布与分发可靠性”层面，提供自动供应商故障切换以提升可用性，但不涵盖更深度的内容生成、运营分析或互动管理。典型场景是品牌/团队的跨平台同步发帖与定时发布，减少多端重复操作并降低单一平台或通道异常带来的发布失败风险。关键技术形态通常包括统一发布 API、平台适配器/连接器、故障检测与自动切换策略，以及任务队列与重试机制来保证投递一致性。

**关键词**: 多平台社媒发布, 社交媒体 API 集成, 自动故障切换, 跨平台内容分发, 发布任务队列, 统一发布接口, 平台适配器模式, Social

**评分**: 17

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/phy-social-posting)

---

## [14. Brand DNA Extractor](https://clawhub.ai/PHY041/phy-brand-dna-extractor)

**Slug**: `phy-brand-dna-extractor`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Extract brand identity (colors, typography, visual style, imagery) from any website URL. Scrapes the site, analyzes CSS/images with K-means and VLM, and retu...

**中文介绍**: 该能力用于从任意网站 URL 自动提取品牌识别要素，包括主色/辅色、字体与排版特征、整体视觉风格及常用图像/插画风格等。典型场景是为品牌审计、竞品分析、设计系统初始化或营销物料风格对齐提供结构化输出，但仅能基于页面可抓取的前端资源推断，难以覆盖登录后内容、动态渲染未加载资产或品牌策略层面的语义规范。关键技术形态为网页抓取与资源解析，结合对 CSS 与图片的聚类提色（如 K-means）以及视觉语言模型（VLM）进行风格与意象识别后生成结果。

**关键词**: 品牌识别提取, 网站抓取, 色彩调色板提取, 字体识别, 视觉风格分析, 图像特征提取, 视觉语言模型（VLM）, 品牌指南生成

**评分**: 35

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/phy-brand-dna-extractor)

---

## [15. AetherLang V3 for Claude Code](https://clawhub.ai/contrario/aetherlang-claude-code)

**Slug**: `aetherlang-claude-code`  
**Version**: 1.0.3  
**Stats**: ⭐ 2 | ⬇️ 343 | 🧩 4

**原始简介**: Execute AetherLang V3 AI workflows from Claude Code using nine specialized engines for culinary, business, research, marketing, and strategic analyses.

**中文介绍**: 该能力是在 Claude Code 中执行 AetherLang V3 的 AI 工作流，并通过九个专用引擎提供餐饮、商业、研究、营销与战略分析等方向的任务编排与推理支持。能力边界在于它主要负责调用与串联既定引擎与工作流，输出以分析与建议为主，不直接替代外部系统的数据采集、交易执行或部署运维。典型场景包括跨领域调研与竞品分析、营销策略生成、餐饮菜单与成本优化、以及多引擎协同的战略决策推演。关键技术形态为基于领域引擎的工作流执行框架，并支持通过可选的 AETHER_KEY 环境变量对齐 Pro 版本鉴权一致性。

**关键词**: AI 工作流执行, 多引擎编排, 专家引擎, 商业分析, 市场营销分析, 战略分析, 研究助手, 烹饪规划, 环境变量配置

**评分**: 28

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aetherlang-claude-code)

---

## [16. Task Automator](https://clawhub.ai/yinanping-CPU/yinan-task-automator)

**Slug**: `yinan-task-automator`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Automate repetitive computer tasks including file operations, data processing, web scraping, and API integrations. Use when you need to batch process files,...

**中文介绍**: Task Automator for OpenClaw 用于自动化重复性的电脑任务，覆盖文件操作、数据处理、网页抓取与 API 集成，并支持用 cron 表达式做定时执行及多步骤工作流编排。能力边界在于以预置任务与可自定义任务为核心，适合批量处理与周期性同步/监控等自动化，不直接解决复杂业务决策或强交互式场景。典型应用包括文件整理与格式转换、API 数据同步、网站监控、电商订单处理等，关键技术形态是任务模板+自定义任务、工作流编排与调度机制，并配套安全与排障实践指引。

**关键词**: 任务自动化, 批处理, 文件操作自动化, 数据处理, 网页爬取, 定时调度（cron）, 多步工作流, 自定义任务, 电商订单处理

**评分**: 28

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yinan-task-automator)

---

## [17. MasterSwarm AI Document Analysis](https://clawhub.ai/contrario/masterswarm)

**Slug**: `masterswarm`  
**Version**: 1.1.2  
**Stats**: ⭐ 2 | ⬇️ 163 | 🧩 4

**原始简介**: Analyze any document with 15 parallel AI engines via the MasterSwarm cloud API. Upload receipts, contracts, lab results, or ask business/crypto/legal questio...

**中文介绍**: 该服务通过 MasterSwarm 云端 API 调用 15 路并行 AI 引擎对文档或问题进行分析，适用于上传票据、合同、化验/检验结果等材料，或进行商业、加密资产、法律相关咨询与解读。其能力边界在于输出为基于输入内容与模型推理的结果，不能替代权威审计、医疗诊断或法律意见，且受上传材料质量与合规限制影响。关键技术形态为云端并行多模型/多引擎编排与聚合分析，通过 API 接入实现多路推理与结果整合。

**关键词**: 文档解析, 多模型集成, 文档上传, 收据识别, 合同审查, 实验室报告解读, 法律问答, 加密货币问答, 业务问答, 技能插件集成

**评分**: 19

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/masterswarm)

---

## [18. Capital Market Report](https://clawhub.ai/yangzhe1991/capital-market-report)

**Slug**: `capital-market-report`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Generate comprehensive capital market briefings covering global indices (A-shares, Hong Kong stocks, US stocks), commodities (gold, oil, Bitcoin), and catego...

**中文介绍**: 该能力用于生成覆盖全球资本市场的简报，范围包括A股、港股、美股等主要指数，以及黄金、原油、比特币等大宗与加密资产，并可按主题对新闻进行归类整合。能力边界在于侧重信息汇总与结构化呈现，不直接提供投资建议、交易执行或对实时行情与突发事件作出保证。典型场景包括晨报/收盘复盘、投研快报、跨市场资产跟踪与风险提示。关键技术形态以多源数据聚合、内容抽取与分类、摘要生成与模板化编排为主。

**关键词**: 资本市场简报, 市场报告生成, 全球股指, 大宗商品, 比特币, 财经新闻分类, Capital, Market

**评分**: 14

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/capital-market-report)

---

## [19. Content Type Router](https://clawhub.ai/PHY041/phy-content-type-router)

**Slug**: `phy-content-type-router`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Detect and route to the correct visual content type (hero shot, poster, infographic, etc.) from a text description or output type hint. Use when you need to...

**中文介绍**: 该能力用于根据文本描述或输出类型提示，自动识别视觉内容类型（如主视觉、海报、信息图等）并将请求路由到对应的生成/处理流程。能力边界在于它负责“内容类型判别与分发”，不直接完成具体的图像设计与生成，且对输入描述的清晰度与类别覆盖范围有依赖。典型场景包括在多模态创作平台中将用户需求自动分流到不同模板/模型管线，或在批量生产物料时减少人工选型。关键技术形态是文本意图/类别识别（分类或规则+模型）与基于标签的路由编排（工作流/策略引擎）。

**关键词**: 视觉内容类型识别, 内容类型路由, 文本到内容类型分类, 生成式设计工作流, 创意资产编排, 海报生成, 信息图生成, 主视觉图生成, 输出类型提示, 创意制作自动化

**评分**: 30

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/phy-content-type-router)

---

## [20. Solana Portfolio](https://clawhub.ai/liji3597/solana-portfolio)

**Slug**: `solana-portfolio`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 管理 Solana 投资组合 — 追踪多钱包余额、代币分布和资产估值。当用户想查看持仓、添加钱包或了解资产状况时触发。

**中文介绍**: 这是一个用于管理与追踪 Solana 投资组合的能力，支持每位用户最多关联 5 个钱包，汇总查看多钱包余额、代币分布、单项持仓与总资产估值。能力边界是严格只读，不涉及私钥与任何交易操作，并对钱包地址进行格式校验且不会对持仓做价值判断。典型场景包括用户想新增/查看/移除钱包地址，或快速了解当前资产结构与估值变化。关键技术形态是基于链上数据的资产聚合与估值计算，结合会话式交互流程与校验/安全护栏来引导操作。

**关键词**: 加密资产组合管理, 多钱包追踪, 钱包余额查询, 代币分布分析, 资产估值, 持仓明细, 钱包地址校验, 只读访问控制

**评分**: 28

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/solana-portfolio)

---

## [21. First-Principle Social Platform](https://clawhub.ai/BatchLion/first-principle-social-platform)

**Slug**: `first-principle-social-platform`  
**Version**: 1.0.29  
**Stats**: ⭐ 0 | ⬇️ 174 | 🧩 17

**原始简介**: Authenticate OpenClaw AI agents to First-Principle with ANP did:wba identities derived from the existing OpenClaw gateway device key, run session health chec...

**中文介绍**: 该能力用于把 OpenClaw AI agents 通过 ANP 的 did:wba 身份认证接入 First-Principle，身份由现有 OpenClaw 网关设备密钥派生，并可配合会话健康检查等运行期管理。能力边界在于认证材料依赖本地网关设备的 device.json 私钥文件进行本地签名，私钥不会上传，但需要用户提供真实的 device.json 路径且不负责跨环境自动发现状态目录。典型场景是网关设备登录与代理运行时鉴权、在不同部署位置迁移 OpenClaw 状态后仍保持一致身份。关键技术形态包括 ANP did:wba 去中心化标识、基于设备密钥派生的身份与本地私钥签名的凭据处理流程。

**关键词**: 去中心化身份（DID）, 设备身份, 网关设备密钥, 本地签名, 私钥管理, 凭证处理, First-Principle, Social

**评分**: 43

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/first-principle-social-platform)

---

## [22. 小红书图文生成器](https://clawhub.ai/franklu0819-lang/xiaohongshu-post-gen)

**Slug**: `xiaohongshu-post-gen`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Generate complete Xiaohongshu (Little Red Book) posts with up to 10 pages (3:4 vertical format). Auto-parses text content into cover + content pages. Support...

**中文介绍**: 该能力用于自动生成小红书风格的多页图文内容，最多10页并采用3:4竖版比例，可将输入文本自动解析为封面页与若干内容页。能力边界在于主要输出版式与视觉风格编排，依赖你提供的文案质量与合规性，且仅覆盖预设的4种视觉风格。典型场景包括笔记内容快速成稿、活动/种草文案的一键排版出图与多页信息分层展示，关键技术形态为文本结构化解析、模板化分页排版与风格化视觉渲染生成。

**关键词**: 小红书笔记生成, 图文海报生成, 多页图文生成, 社交媒体内容创作, 自动排版分页, 文本解析排版, 封面生成, 内容页生成, 模板渲染, 视觉风格模板

**评分**: 13

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaohongshu-post-gen)

---

## [23. LobsterBio - Use](https://clawhub.ai/cewinharhar/lobsterbio-use)

**Slug**: `lobsterbio-use`  
**Version**: 1.1.404  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Runs bioinformatics analysis with Lobster AI -- single-cell RNA-seq, bulk RNA-seq, genomics (VCF/GWAS), proteomics (mass spec/affinity), metabolomics (LC-MS/...

**中文介绍**: Lobster AI 用于运行多组学生物信息学分析，覆盖单细胞/批量 RNA-seq、基因组学（VCF/GWAS）、蛋白组学与代谢组学等数据类型，典型场景是从原始或预处理数据出发完成分析流程编排、结果汇总与解释。其能力边界在于侧重分析任务的自动化调度与工作流执行，本次更新仅涉及安装与安全使用说明的完善，对核心路由、触发机制、功能与工作流本身没有改变。关键技术形态是以代理/工作流方式对不同组学分析模块进行统一编排，并通过环境变量管理 API key 以降低泄露风险。

**关键词**: 生物信息学分析, 多组学分析, 基因组变异分析, 蛋白质组学, 代谢组学, 命令行工具, API 密钥管理, LobsterBio

**评分**: 46

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lobsterbio-use)

---

## [24. Solana Investor](https://clawhub.ai/liji3597/solana-investor)

**Slug**: `solana-investor`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 顶层投资助手编排器 — 协调 portfolio、dca、alerts、market 技能，处理复杂的多步骤投资请求。当用户的请求涉及多个操作或需要跨技能协调时触发。

**中文介绍**: 这是一个顶层投资助手编排器，用于在用户提出需要跨 portfolio、DCA、alerts、market 等多个能力协同的复杂多步骤请求时进行触发与协调，简单单一需求则由对应子技能直接处理。它的能力边界在于主要做流程编排与上下文传递，不直接替代各子技能的具体执行，并要求所有写入/变更类操作必须逐步确认。典型场景包括“先查看再设置提醒”“组合查看与定投配置”“多维度汇总”等跨步骤工作流。关键技术形态是基于编排规则的多技能调用链，遵循先查询后行动、分步确认、子步骤失败不阻塞其他步骤的容错与控制机制。

**关键词**: 投资助手, 技能编排, 多步骤工作流, 投资组合管理, 定投策略（DCA）, 价格提醒, 市场数据查询, 写操作确认机制, 上下文传递, 故障隔离

**评分**: 42

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/solana-investor)

---

## [25. Sadist Wendy](https://clawhub.ai/Chazzzzzzz/sadist-wendy)

**Slug**: `sadist-wendy`  
**Version**: 2.0.3  
**Stats**: ⭐ 0 | ⬇️ 65 | 🧩 5

**原始简介**: Sadist and control freak persona that monitors every message and roasts users with psychologically precise, sexually charged banter to liven up group chat. A...

**中文介绍**: 这是一个用于群聊的角色化聊天技能，以“强势监控+吐槽”的人设在群内发言，通过更具个性的入群自我介绍、点名召唤者并邀请群成员互动来增强记忆点与氛围。其能力边界是仅做文案与开场表达层的增强，不改变核心对话逻辑与运行行为，适用于群聊破冰、活跃气氛与角色扮演式互动等场景。关键技术形态偏向提示词/话术模板与入群事件触发的消息编排，同时需要注意对辱骂、性暗示等高风险内容的合规约束与安全策略。

**关键词**: 群聊机器人, 角色扮演人设, 提示词工程, 聊天内容监控, 毒舌吐槽生成, 心理学风格对话, 成人向对话生成, 社群互动增强, 聊天技能插件

**评分**: 6

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/sadist-wendy)

---

