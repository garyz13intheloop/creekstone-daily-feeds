# ClawHub Skills Daily | 2026-03-10

> 共 25 个 skills

## [1. 预测市场周报生成器](https://clawhub.ai/hu4891/prediction-market-reporter)

**Slug**: `prediction-market-reporter`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 每周自动/手动收集关于预测市场（主要针对 Polymarket 和 Kalshi）的最新资讯，并生成一份面向团队同步的周报。主要关注用户行为、新功能、争议和C端事件。

**中文介绍**: 该能力用于每周自动或手动汇总预测市场（以 Polymarket、Kalshi 为主）的最新动态，产出供团队同步的周报，重点覆盖用户行为变化、新功能发布、争议事件与面向 C 端的热点。能力边界在于仅做信息收集、筛选与结构化总结，不保证覆盖所有信源、实时性或对事件真伪与影响的最终裁决。典型场景包括团队例会前的情报同步、产品/运营复盘、竞品追踪与风险预警。关键技术形态通常为多源采集（公告/社媒/媒体/链上或盘口信号）+ 关键词与主题聚类 + 去重与可信度标注 + LLM 摘要生成与周报模板化输出。

**关键词**: 预测市场, 周报生成, 新闻聚合, 事件监测, 自动化采集, 人工采集, 产品更新追踪, 争议监测, C端事件追踪

**评分**: 28

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/prediction-market-reporter)

---

## [2. CSDN 文章发布](https://clawhub.ai/echome123/csdn-publish)

**Slug**: `csdn-publish`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: CSDN 文章发布技能

**中文介绍**: 该技能的能力边界是基于你已完成的账号登录状态，在 CSDN 博客后台自动完成文章发布流程，并在成功后返回文章链接；它不负责账号登录本身。典型场景包括将本地或生成的 Markdown 内容批量/自动发布到 CSDN、减少手工粘贴与发布操作并确保发布成功可追踪。关键技术形态是浏览器端的 UI 自动化编排：自动打开编辑器、填充标题与正文、触发发布并校验结果，同时做登录态、标题长度与内容非空等前置校验及错误处理。

**关键词**: 博客自动发布, 浏览器自动化, RPA流程自动化, 表单自动填写, 编辑器自动操作, 登录状态校验, 文章链接回传, 异常处理机制

**评分**: 26

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/csdn-publish)

---

## [3. coding-agent](https://clawhub.ai/TSHOGX/tshogx-coding-agent)

**Slug**: `tshogx-coding-agent`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Delegate coding tasks to Codex, Claude Code, or Pi agents via background process. Use when: (1) building/creating new features or apps, (2) reviewing PRs (sp...

**中文介绍**: coding-agent 提供通过后台进程把编码任务委派给 Codex、Claude Code、Pi 或 OpenCode 等代理的能力，支持交互/后台两种模式，并可对会话进行监控、输入与清理。典型场景包括新功能或应用开发、PR 评审，以及借助 git worktrees 进行并行开发与多代理编排协作。其关键技术形态是基于不同代理的差异化执行规则与标志位（如部分代理需要 PTY），并强化安全工作区边界：避免在受限环境或线上分支直接拉起代理、尽量在隔离分支中运行。

**关键词**: 代码代理, 代理任务委派, 多代理编排, 后台进程, 交互模式, PR审查, 安全工作区, coding-agent

**评分**: 43

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tshogx-coding-agent)

---

## [4. BinanceCoach](https://clawhub.ai/skills?q=binance-coach)

**Slug**: `binance-coach`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: AI-powered Binance crypto coach analyzing portfolio health, trading behavior, and market data to provide smart DCA advice and personalized coaching.

**中文介绍**: 这是一款面向币安用户的加密资产教练，基于账户持仓健康度、交易行为与市场数据进行分析，给出更智能的定投（DCA）建议与个性化交易复盘/陪练。能力边界在于主要依赖币安账户与行情数据做策略与行为层面的建议，不承诺收益，也不覆盖非币安账户或链上全量资产视角。典型场景包括定投节奏优化、仓位与风险暴露检查、交易纪律纠偏与市场波动下的决策辅助；关键技术形态是通过币安 API 获取数据并结合 AI 推理生成建议。最新的 OpenClaw 模式将 AI 与消息交互内置化，仅需币安 API Key 即可使用，无需额外的 Anthropic Key 或 Telegram Bot Token。

**关键词**: 加密交易助手, 投资组合健康分析, 交易行为分析, 市场数据分析, 定投策略（DCA）, 个性化投资教练, 自动化投顾, 密钥认证（API key）

**评分**: 45

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/binance-coach)

---

## [5. Course Study](https://clawhub.ai/VincentJiang06/course-study)

**Slug**: `course-study`  
**Version**: 2.0.0  
**Stats**: ⭐ 0 | ⬇️ 31 | 🧩 3

**原始简介**: Comprehensive course study, exam revision, and structured study note generation from lecture slides, course PDFs, or topic outlines. Use when the user wants...

**中文介绍**: 该能力用于从课程幻灯片、PDF 或主题提纲中提炼结构化学习笔记，支持系统复习与备考，并在输出中附带速查与考题问答等“Exam Ready”附录，但不替代原始材料的权威性与完整性，且对未提供内容无法补全细节。典型场景是期末/资格考试冲刺、课堂内容梳理、按用户标记重点进行加深讲解并配套例题演算。关键技术形态包括独立的材料接收与结构化处理阶段、可追溯的多阶段工作流、Markdown 规范化笔记与严格版式规则的高保真 PDF 导出，以及重点主题贯穿主文与所有附录的优先覆盖机制。

**关键词**: 课程学习辅助, 考试复习, 讲义幻灯片解析, PDF教材解析, 结构化学习笔记生成, 材料摄取流程, PDF高保真导出, 重点主题加权覆盖, 例题推导, 多阶段工作流

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/course-study)

---

## [6. mlx-whisper](https://clawhub.ai/TSHOGX/tshogx-mlx-whisper)

**Slug**: `tshogx-mlx-whisper`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Local speech-to-text with MLX Whisper (Apple Silicon optimized, no API key).

**中文介绍**: 该能力在 Apple Silicon（M1/M2/M3/M4）Mac 上基于 MLX Whisper 实现本地语音转文字转写，默认使用 `mlx-community/whisper-large-v3-turbo`，全程端侧运行无需 API Key。典型场景包括离线会议/访谈录音转写、多格式音频批量转文本、生成 SRT 字幕，以及通过语言提示提升识别效果并支持翻译为英文。能力边界在于主要面向 Apple Silicon 设备的本地推理环境，效果与性能受设备算力、音频质量与所用模型限制，且默认模型固定。关键技术形态为端侧大模型语音识别推理（MLX 加速）+ 多格式音频解码 + 字幕/文本结构化输出与可选翻译流程。

**关键词**: 本地语音转文本, 离线语音识别, 端侧推理, 多格式音频转写, SRT 字幕生成, 语言提示, 语音翻译（英译）, mlx-whisper

**评分**: 27

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tshogx-mlx-whisper)

---

## [7. Flow Visual Explainer](https://clawhub.ai/windseeker1111/flow-visual-explainer)

**Slug**: `flow-visual-explainer`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Generate beautiful, self-contained HTML pages that visually explain systems, code, plans, and data. Use when the user asks for a diagram, architecture overvi...

**中文介绍**: 该能力用于将系统、代码、方案与数据等技术内容生成美观且自包含的 HTML 可视化页面，自动渲染架构图、流程图、表格与幻灯片以便在浏览器中直观讲解。典型场景包括系统概览与架构说明、代码评审要点展示、方案对比与规划复盘、复杂数据表与多维比较呈现，尤其适合需要“视觉化表达”的提问或较复杂表格输出。能力边界在于它侧重展示与解释（视觉语言触发），不提供 ASCII 退化输出，核心技术形态是 HTML 渲染管线结合内置设计系统、响应式布局与深浅色模式，并可扩展为杂志级幻灯片输出。

**关键词**: HTML 可视化说明, 自包含 HTML 页面, 自动图表渲染, 架构图生成, 代码评审可视化, 复杂表格渲染, 幻灯片生成, 响应式布局, 深色/浅色模式, 多设计系统主题, 本地文件输出

**评分**: 36

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/flow-visual-explainer)

---

## [8. Bitrefill CLI](https://clawhub.ai/marcopesani/bitrefill-cli)

**Slug**: `bitrefill-cli`  
**Version**: 1.5.0  
**Stats**: ⭐ 0 | ⬇️ 25 | 🧩 4

**原始简介**: Buy gift cards, mobile top-ups, and eSIMs on Bitrefill. Pay with crypto and x402. 1,500+ brands, 180+ countries

**中文介绍**: 该能力用于在 Bitrefill 上用加密货币或 x402 购买礼品卡、手机话费充值与 eSIM，覆盖 180+ 国家、1500+ 品牌。典型场景是跨境数字商品即时购买与充值、用链上资金完成小额消费与备用通讯配置。能力边界在于仅支持 Bitrefill 可售的数字商品与其支付方式（含 x402 与主流加密资产），并需遵循消费安全与风控最佳实践。关键技术形态是对 Bitrefill 商品与支付流程的接口化封装与文档化参考（支付说明、命令参考、故障排查与关键注意事项）。

**关键词**: 命令行工具（CLI）, 数字礼品卡购买, 手机话费充值, 加密货币支付, x402 支付, 支付方式集成, 跨境数字商品, 交易安全指南, 故障排查指南, 命令参考文档

**评分**: 19

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bitrefill-cli)

---

## [9. API Gateway](https://clawhub.ai/byungkyu/api-gateway)

**Slug**: `api-gateway`  
**Version**: 1.0.64  
**Stats**: ⭐ 193 | ⬇️ 37677 | 🧩 65

**原始简介**: Connect to 100+ APIs (Google Workspace, Microsoft 365, GitHub, Notion, Slack, Airtable, HubSpot, etc.) with managed OAuth. Use this skill when users want to...

**中文介绍**: 该能力提供对 100+ 第三方服务（如 Google Workspace、Microsoft 365、GitHub、Notion、Slack、Airtable、HubSpot 等）的统一连接，并通过托管 OAuth 完成授权与访问管理，近期新增了 Brave Search 接入及相应参考文档。典型场景是用户希望在一个工作流里安全地读取、查询或同步多个 SaaS 的数据与操作（例如检索内容、拉取文档/工单、写入 CRM、消息通知等）。能力边界在于仅覆盖已支持的服务与其开放 API 能力范围，依赖用户授予权限与各平台配额/限制，无法直接访问未开放接口或未授权的数据。关键技术形态是多连接器架构 + 托管 OAuth 鉴权 + 统一 API 调用封装与服务适配层。

**关键词**: 第三方API集成, 统一API接口, 身份认证与授权, 服务集成目录, 搜索API集成, 开发者参考文档, API, Gateway

**评分**: 40

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/api-gateway)

---

## [10. Guided Learning CN](https://clawhub.ai/ckchzh2022/guided-learning-cn)

**Slug**: `guided-learning-cn`  
**Version**: 1.4.1  
**Stats**: ⭐ 0 | ⬇️ 51 | 🧩 6

**原始简介**: 中文引导式学习助手。学习助手、知识学习、学习计划、学习路线、概念讲解、复习备考、考试复习、费曼学习法、循序渐进学习、学科辅导、自学、教程、课程学习、教材学习、知识点总结、记忆卡片、闪卡、Anki、学习方法、一对一辅导、自测试卷、选择题、简答题。Chinese guided learning assistant w...

**中文介绍**: 这是一个中文引导式学习助手，面向自学与学科辅导场景，可按学习目标生成学习计划与学习路线，分步骤讲解概念并用费曼学习法促理解，同时支持知识点总结、复习备考与自测题（选择题/简答题）来检验掌握度。其能力边界在于基于对话提供学习内容组织与讲解、题目生成与解析等认知支持，无法替代权威教材与真实考试评测，也不保证所有学科细节的绝对准确与最新性。关键技术形态是以对话为核心的引导式教学流程编排，结合闪卡/记忆卡片（如 Anki 思路）的间隔复习策略，以及一对一式追问与反馈闭环来推进循序渐进学习。品牌标识为 hello@bytesagain.com。

**关键词**: 引导式学习助手, 学习计划, 学习路线, 概念讲解, 知识点总结, 复习备考, 费曼学习法, 循序渐进学习, 自测题库

**评分**: 31

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guided-learning-cn)

---

## [11. CatchClaw](https://clawhub.ai/Lovelcp/catch-claw)

**Slug**: `catch-claw`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: A fun utility skill that generates catchy, claw-themed puns, slogans, and one-liners. Use this skill when the user asks for puns, wordplay, slogans, or creat...

**中文介绍**: 这是一个轻量娱乐型文案生成能力，专注输出与“爪/钳/抓”等意象相关的双关梗、口号和一句话标语，边界是不提供通用写作、事实查询或严肃内容创作。典型场景是用户需要即兴冷笑话、品牌活动口号、社媒短句或主题化谐音梗时快速产出候选。关键技术形态属于主题约束的文本生成与双关/押韵等语言风格控制，当前版本为初始发布。

**关键词**: 双关语生成, 文字游戏, 标语生成, 口号生成, 一句话段子, 主题化文案, 幽默文案, 内容创作工具, 聊天机器人技能, 提示词驱动生成

**评分**: 2

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/catch-claw)

---

## [12. Nail B3g1 Promo](https://clawhub.ai/RIJOYAI/nail-b3g1-promo)

**Slug**: `nail-b3g1-promo`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 10 | 🧩 2

**原始简介**: Designs and automates "buy 3 get 1 free" (B3G1) promotions for DTC nail polish and press-on nail stores selling cat-eye, matte, gel-effect, and similar lines...

**中文介绍**: 该方案面向 DTC 指甲油与穿戴甲品牌，自动化配置与运行“买三送一（B3G1）”促销，适用于猫眼、哑光、凝胶质感等产品线的常见拉新与转化活动。能力边界在于当前仅覆盖 B3G1 这一促销规则，未体现对更复杂阶梯折扣或多规则叠加的支持。关键技术形态以可脚本化的促销自动化逻辑为核心，并配套评测与参考文档及评测配置文件，用于测试与迭代验证。

**关键词**: 促销自动化, 买三赠一, 电商促销规则, 折扣引擎, DTC 电商品牌, 美甲电商, 指甲油品类, 贴片甲品类, 评测配置文件, 脚本化自动化, 参考文档体系

**评分**: 28

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nail-b3g1-promo)

---

## [13. Wechat File Helper](https://clawhub.ai/qidu/wechat-helper)

**Slug**: `wechat-helper`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 150 | 🧩 3

**原始简介**: WeChat File Helper automation. Use when: - Check if filehelper.weixin.qq.com is open in browser - Open the page if not already open - Capture QR code and sen...

**中文介绍**: 这是一个用于自动化微信网页版文件传输助手（filehelper.weixin.qq.com）的工具，主要能力是检测页面是否已在浏览器打开、未打开则自动打开，并抓取登录二维码等关键信息以便继续后续流程。其典型场景包括无人值守的网页端登录准备、文件助手入口的可用性巡检与自动拉起。能力边界在于仅覆盖浏览器侧的页面状态与可视化元素捕获，仍依赖人工扫码或外部系统完成登录与后续业务操作；关键技术形态是浏览器自动化与页面截图/识别（二维码捕获）链路。

**关键词**: 微信文件传输助手, 微信网页版, 浏览器自动化, 二维码截图, 扫码登录自动化, 文件传输自动化, Wechat, File

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/wechat-helper)

---

## [14. 错敏信息检测（文本）](https://clawhub.ai/1227323804/sensitive-check-skill)

**Slug**: `sensitive-check-skill`  
**Version**: 7.0.2  
**Stats**: ⭐ 0 | ⬇️ 29 | 🧩 11

**原始简介**: 基于FastAPI的文本错敏信息检测服务，识别敏感词、错别字及规范表述问题，提供RESTful API接口调用。

**中文介绍**: 这是一个基于 FastAPI 的文本错敏信息检测服务，通过 RESTful API 对外提供能力，主要用于识别文本中的敏感词、错别字以及不规范表述并返回检测结果。其能力边界在于面向文本内容的规则/模型式识别与提示，通常不覆盖复杂语义推理、上下文事实核验或跨文档一致性判断。典型场景包括内容审核、客服与工单质检、发布前文案校对、合规自查等，关键技术形态为 FastAPI 服务化封装与 REST 接口集成（常结合敏感词库/纠错规则或轻量模型进行检测）。

**关键词**: 文本审核, 敏感词检测, 错别字检测, 规范表述检测, 内容合规, 文本清洗, 文本处理服务, 错敏信息检测（文本）

**评分**: 6

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/sensitive-check-skill)

---

## [15. Official Doc](https://clawhub.ai/ckchzh/official-doc)

**Slug**: `official-doc`  
**Version**: 1.1.1  
**Stats**: ⭐ 0 | ⬇️ 17 | 🧩 3

**原始简介**: 公文写作助手。通知、报告、请示、批复、会议纪要、工作总结、格式检查、语气检查、模板库。Official document writer for notices, reports, requests, meeting minutes with format check, tone check, template l...

**中文介绍**: 公文写作助手面向通知、报告、请示、批复、会议纪要与工作总结等场景，提供起草、改写与润色能力，并可进行格式与语气合规性检查，配套模板库提升成稿效率。能力边界在于其输出需以用户提供的事实材料与单位规范为准，不能替代正式审批、政策解读或对敏感/涉密内容的权威判断，建议用于初稿生成与规范性校对。关键技术形态体现为基于模板库与语言生成的文本生产、规则/样式约束下的格式校验、以及语气与措辞一致性的自动检测与修订建议。

**关键词**: 公文写作, 通知写作, 报告写作, 请示写作, 批复写作, 工作总结生成, 格式规范检查, 语气一致性检查, 公文模板库, 写作辅助工具

**评分**: 14

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/official-doc)

---

## [16. AI Opportunity Radar](https://clawhub.ai/itsukikuchiki/ai-opportunity-radar)

**Slug**: `ai-opportunity-radar`  
**Version**: 1.1.1  
**Stats**: ⭐ 1 | ⬇️ 24 | 🧩 4

**原始简介**: Helps you reflect on daily tasks by conversation, identifying repetitive, manual, or frustrating workflows where AI automation can save time.

**中文介绍**: 该能力通过日常对话收集你的任务与感受，识别重复、手工或令人沮丧的工作流，并给出可用 AI 自动化节省时间的机会与建议；能力边界在于日常打卡主要用于对话与数据采集，不承诺当下立即完成反思或分析。典型场景是持续记录工作过程后，在周度复盘或机会雷达中获得更系统的自动化切入点与代理建议。关键技术形态包括“Radar Memory”对长期行为信号的累积分析，以及版本更新通知在后续反思中一次性提示。

**关键词**: 日常打卡, 工作流挖掘, 重复任务识别, 人工流程自动化, 摩擦点识别, 行为信号积累, 长期记忆模块, 周度复盘, 版本更新通知

**评分**: 42

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-opportunity-radar)

---

## [17. Meegle Connector](https://clawhub.ai/wadxm/meegle-connector)

**Slug**: `meegle-connector`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Connect to Meegle via MCP using OAuth with user-selected authentication methods to manage work items and view task information.

**中文介绍**: 该连接器通过 MCP 服务以 OAuth 方式接入 Meegle，支持用户在浏览器直连 OAuth 与 OAuth 代理两种认证形态间选择。典型场景是本地或远程环境下进行任务/工作项的查询与管理，包括创建、修改、转交和查看任务信息。能力边界在于仅覆盖基于授权凭据的工作项操作与信息读取，不涉及更广泛的 Meegle 业务域或非 OAuth 的接入方式。

**关键词**: MCP 连接器, 第三方服务集成, 工作项管理, 任务信息查询, 工单系统集成, 凭证管理, 本地-远程授权, Meegle

**评分**: 36

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/meegle-connector)

---

## [18. raspberry-pi-camera-service](https://clawhub.ai/CLD1994/raspberry-pi-camera-service)

**Slug**: `raspberry-pi-camera-service`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 提供使用摄像头拍照, 录制视频或直接生成gif的能力。何时触发: 需要拍照时, 需要观察一段时间当前视野时, 需要关注某件事情的进展时.

**中文介绍**: 该服务通过 HTTP API 远程控制树莓派 CSI/USB 摄像头，支持拍照、录制多格式视频（H264/MP4）以及直接生成 GIF，并提供文件列表、下载、删除等管理能力。能力边界在于仅覆盖摄像头采集与服务端转码/生成媒体文件，不包含智能识别或事件判断等上层分析。典型场景是在需要立即拍照取证、需要持续观察一段时间的视野、或关注某件事进展时由外部系统触发调用。关键技术形态包括基于会话的控制与心跳监测、自动超时保护，以及后端格式转换与媒体文件管理。

**关键词**: 树莓派摄像头, 远程摄像头控制, CSI 摄像头, USB 摄像头, 照片采集, 视频录制, 多格式媒体编码, 心跳监测, 媒体文件管理

**评分**: 20

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/raspberry-pi-camera-service)

---

## [19. ClickZetta Studio Agent](https://clawhub.ai/luketalent/studio-agent)

**Slug**: `studio-agent`  
**Version**: 0.1.3  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 4

**原始简介**: Use this for ClickZetta Studio requests such as querying tasks, listing workspaces, checking projects, and creating or running ClickZetta jobs from a single...

**中文介绍**: 该能力面向 ClickZetta Studio 的工作流与任务管理，支持从单一入口查询/运行任务与作业、列出工作空间、检查项目等日常运维与开发协作场景。能力边界在于仅覆盖 Studio 内可通过接口触达的查询与作业编排操作，不负责底层集群/权限策略变更或超出平台范围的外部系统联动。关键技术形态以对 ClickZetta Studio API 的封装与调用为主，将“查询、创建、运行作业/任务”等动作统一为可复用的工具化能力。

**关键词**: Agent, 任务查询, 作业调度, 作业运行, 工作区管理, 项目管理, ClickZetta, Studio

**评分**: 22

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/studio-agent)

---

## [20. AetherCore v3.3](https://clawhub.ai/AetherClawAI/aetherclaw)

**Slug**: `aetherclaw`  
**Version**: 3.3.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: AetherCore v3.3 - Night Market Intelligence Technical Serviceization Practice. High-performance JSON optimization system with real-world benchmarks.

**中文介绍**: AetherCore v3.3 是面向“夜市情报”业务的高性能 JSON 优化服务化系统，核心能力是在全自动运行下对 JSON 处理链路进行加速与稳定性增强，并通过基准测试宣称相对 XML 方案可达数量级提升。其能力边界主要在于优化与调度监控层，依赖与 OpenClaw 的集成来完成自动调度、健康监测与智能日志，适用于高吞吐数据接入、实时/批处理解析与异常自愈等场景。关键技术形态包括自动化调度编排、智能文件检测与自愈、专有优化算法以及配套监控看板与可观测性体系。

**关键词**: 高性能解析, 数据序列化优化, 性能基准测试, 自动化调度, 健康监控, 智能日志, 自愈机制, 文件自动检测, 监控仪表盘

**评分**: 31

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aetherclaw)

---

## [21. Esign Automation](https://clawhub.ai/esign-cn-open-source/esign-automation)

**Slug**: `esign-automation`  
**Version**: 1.3.5  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 6

**原始简介**: Automate document signing workflows and operations using the eSignGlobal platform.

**中文介绍**: eSignGlobal 平台用于自动化文档签署流程与运营操作，覆盖从发起签署（如发送签署信封/Envelope）到流程流转的自动化编排，但不直接替代签署方的人工确认与法务合规判断等业务决策。典型场景包括批量发起合同签署、触发式发送签署请求、对接内部系统实现签署流程自动化。其关键技术形态以脚本/API 方式集成实现（例如通过 TypeScript 脚本发送 Envelope），并随版本迭代更新接口与能力说明（当前反映为 1.3.5）。

**关键词**: 电子签名自动化, 文档签署工作流, 合同审批流程, 签署任务编排, 文档合规模板, 低代码技能插件, Esign, Automation

**评分**: 27

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/esign-automation)

---

## [22. Ariadne Thread](https://clawhub.ai/in12hacker/ariadne-thread)

**Slug**: `ariadne-thread`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Guide creation of AI-friendly project structures with progressive disclosure indexing, modular architecture, and intent-oriented code. Use when starting a ne...

**中文介绍**: 该能力用于在项目启动阶段引导构建更适配 AI 协作的工程结构，强调通过渐进式披露的索引方式组织文档、采用模块化架构并以意图导向的代码表达来提升可理解性与可维护性。能力边界在于它提供结构与规范层面的指导，不涉及具体业务功能实现或运行时能力变更。典型场景是新建项目或重构仓库的文档与目录体系，使 AI 与人类更快定位入口与职责；关键技术形态体现在索引式文档组织与模块化拆分策略，并将文档收敛为以 SKILL.md 为唯一主文档的变更。

**关键词**: AI友好代码库, 仓库结构规范, 渐进式披露, 索引式文档, 模块化架构, 意图导向代码, 代码可导航性, 文档精简, 单一事实源

**评分**: 31

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ariadne-thread)

---

## [23. Doubao ASR / 豆包语音转写](https://clawhub.ai/vahnxu/doubao-asr)

**Slug**: `doubao-asr`  
**Version**: 0.18.0  
**Stats**: ⭐ 1 | ⬇️ 446 | 🧩 25

**原始简介**: Transcribe audio files via Doubao Seed-ASR 2.0 (豆包录音文件识别模型2.0, recorded audio → text) API from ByteDance/Volcengine. Best-in-class Chinese speech recognition...

**中文介绍**: Doubao Seed-ASR 2.0 是字节跳动火山引擎提供的录音文件转文字 ASR 能力，通过 API 将已录制音频转写为文本，主打高质量中文语音识别。其能力边界在于主要面向离线音频文件的转写，不覆盖实时通话链路或语义理解类任务。典型场景包括会议/访谈录音整理、客服质检与内容归档等，关键技术形态为云端语音识别与可选的说话人分离（近期修复了分离标签丢失的字段路径问题）。

**关键词**: 自动语音识别, 语音转写, 音频转文本, 录音文件识别, 中文语音识别, 说话人分离, 语音识别模型, 云端推理, 环境变量配置

**评分**: 10

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/doubao-asr)

---

## [24. raspberry-pi-gpio](https://clawhub.ai/CLD1994/raspberry-pi-gpio)

**Slug**: `raspberry-pi-gpio`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 在树莓派中配置和使用GPIO. 何时触发: 需要对 LED, Button 这类简单外设进行控制时, 需要对 Servo, Motors 进行简单控制时, 或需要直接控制GPIO时. 不要触发: 当硬件载体不是树莓派时, 当需要精确控制 Servo, Motors时.

**中文介绍**: 该能力面向树莓派环境下的 GPIO 配置与使用，支持对 LED、按钮等简单外设的输入输出与事件触发，以及对舵机、电机等进行基础 PWM/简易控制，但不适用于非树莓派硬件或需要高精度闭环/时序控制的伺服与电机场景。典型场景是快速搭建 GPIO 读写、按键中断/回调、PWM 调光与基础舵机角度控制等原型验证与教学演示。关键技术形态以 gpiozero 为主，并优先采用现代 lgpio 后端（对树莓派 5 等更友好），同时兼容 lgpio 与 RPi.GPIO 等库实现输入输出、中断与 PWM。

**关键词**: GPIO配置与调试, PWM输出控制, 事件触发与回调, 中断处理, 伺服舵机控制, 直流电机基础控制, 硬件兼容与故障排查, raspberry-pi-gpio

**评分**: 15

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/raspberry-pi-gpio)

---

## [25. Jd Shopping](https://clawhub.ai/harrylabs0913/jd-ec)

**Slug**: `jd-ec`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 18 | 🧩 4

**原始简介**: Command-line tool for JD.com featuring product search, QR code login, price tracking with history, and anti-detection browser automation.

**中文介绍**: 这是一个面向京东的命令行工具，提供商品搜索、扫码登录、价格跟踪与历史查询，并通过 Playwright 进行反检测的浏览器自动化。其能力边界在于主要覆盖查询与跟踪类操作，不承诺对所有风控场景稳定可用，且涉及个人数据的本地存储与导出清理需由用户自行管理。关键技术形态包括基于浏览器自动化的交互流程与基于 AES-256 的敏感数据加密落盘（默认在本地目录），并提供隐私数据查看、清除与导出能力以满足合规与自控需求。

**关键词**: 命令行工具, 电商爬虫, 商品搜索, 二维码登录, 价格追踪, 历史价格, 浏览器自动化, 反检测自动化, AES-256 加密, 本地敏感数据存储, 隐私数据管理

**评分**: 20

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/jd-ec)

---

