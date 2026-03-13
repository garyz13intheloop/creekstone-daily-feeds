# ClawHub Skills Daily | 2026-03-13

> 共 25 个 skills

## [1. Liber8 Career Agent](https://clawhub.ai/polyglyphanalytica/liber8)

**Slug**: `liber8`  
**Version**: 2.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 5

**原始简介**: Manage recurring personalized job searches, analyze CVs, generate tailored application packs, and deliver ranked opportunity pipelines with DOCX attachments.

**中文介绍**: 该产品用于周期性管理个性化求职检索，能解析简历并生成定制化申请材料包，同时输出按优先级排序的机会管道并附带 DOCX 交付物。能力边界在于强调本地优先与确定性执行，不依赖必需凭证或固定外部端点，自动化仅在用户选择后启用且默认只运行内置管道。典型场景包括求职者持续跟踪岗位机会、快速产出针对性申请材料、以及根据反馈迭代筛选与排序。关键技术形态是脚本化的工作区引导与管道执行、周期运行提示生成、DOCX 生成、来源发现与半自动源选择、以及本地状态与输出管理和显式反馈纳入。

**关键词**: 求职代理, 个性化职位搜索, 周期性自动化, 简历解析, 申请材料生成, 本地优先, 确定性执行, 结构化入职, 本地状态管理

**评分**: 42

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/liber8)

---

## [2. 安全打卡提醒](https://clawhub.ai/jayhe/dead-or-alive)

**Slug**: `dead-or-alive`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 监控用户是否活跃，连续7天没打卡就联系紧急联系人。配置后自动创建定时任务。

**中文介绍**: 该能力用于监控用户打卡活跃度，当用户连续 7 天未打卡时自动触发通知流程并联系其紧急联系人，适用于健康管理、独居关怀、企业考勤等需要失联预警的场景。能力边界在于它仅基于“是否打卡/未打卡”的行为信号进行判断与触达，不负责生成打卡内容、也无法替代人工确认与真实紧急救援。技术形态上通过配置规则自动创建并运行定时任务（周期扫描/定时触发），在满足条件时调用通知与联系人联络的流程执行。

**关键词**: 安全打卡, 活跃度监控, 连续未打卡检测, 紧急联系人通知, 生存确认, 提醒通知, 自动化定时任务, 任务调度, 告警升级机制

**评分**: 22

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dead-or-alive)

---

## [3. Yidun Skill Sec](https://clawhub.ai/yd-dev/yidun-skill-sec)

**Slug**: `yidun-skill-sec`  
**Version**: 1.0.1  
**Stats**: ⭐ 5 | ⬇️ 78 | 🧩 9

**原始简介**: Intelligent code security scanner with hybrid local-cloud detection. Fingerprints packages, runs static behavioral analysis, and consults cloud threat intell...

**中文介绍**: 这是一款智能代码安全扫描器，采用本地与云端结合的检测方式，通过对依赖包指纹识别与静态行为分析，并联动云端威胁情报来发现潜在恶意代码与供应链风险。能力边界在于主要依赖静态分析与情报覆盖，对运行时动态行为、未知威胁或离线环境下的检测效果有限。典型场景包括 CI/CD 流水线代码与依赖审计、开源组件引入前的风险评估以及企业仓库的安全基线扫描。当前版本仅做了版本号更新，没有新增功能或修复变更。

**关键词**: 代码安全扫描, 静态分析, 行为分析, 软件包指纹, 威胁情报, 云端检测, 本地-云混合架构, 供应链安全, 恶意代码检测, 依赖风险分析

**评分**: 28

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yidun-skill-sec)

---

## [4. PaddleOCR Document Parsing](https://clawhub.ai/Bobholamovic/paddleocr-doc-parsing)

**Slug**: `paddleocr-doc-parsing`  
**Version**: 2.0.5  
**Stats**: ⭐ 14 | ⬇️ 2199 | 🧩 10

**原始简介**: Complex document parsing with PaddleOCR. Intelligently converts complex PDFs and document images into Markdown and JSON files that preserve the original stru...

**中文介绍**: 该能力基于 PaddleOCR 实现复杂文档解析，可将复杂 PDF 与文档图片智能识别并转换为 Markdown、JSON，同时尽量保留原始版式与结构信息。适用于合同、票据、报告等包含多栏、表格、段落层级的文档结构化抽取与内容再利用场景。能力边界在于对极低清晰度扫描件、严重倾斜/遮挡、强手写或特殊字体版式的还原与结构一致性可能受限，输出质量依赖图像质量与版面复杂度。关键技术形态包括 OCR 文字识别、版面/结构解析（段落层级、表格等）与结构化导出到 Markdown/JSON。

**关键词**: 文档解析, 图像转文本, OCR, 版面分析, 结构化抽取, PaddleOCR, Document, Parsing

**评分**: 29

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/paddleocr-doc-parsing)

---

## [5. openclaw intent router](https://clawhub.ai/ZhenStaff/openclaw-intent-router)

**Slug**: `openclaw-intent-router`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Intelligently routes natural language user intents to the best matching registered agent skill using keyword and semantic matching with confidence scores.

**中文介绍**: 这是一个面向 AI 代理的意图路由框架，将用户自然语言意图通过关键词匹配、语义匹配或混合策略映射到最合适的已注册技能，并输出置信度分数以支持阈值决策与回退处理。典型场景包括多技能代理的自动分流、工具/插件调用选择、以及在不确定意图时的降级到澄清或默认流程。能力边界在于只负责“意图到技能”的匹配与评分，不提供技能本身的实现、对话编排或外部模型服务；整体本地运行、无外部依赖、无遥测，且提供 TypeScript 类型安全的技能注册与 API/CLI 接入形态。

**关键词**: 意图路由, Agent 技能匹配, 语义匹配, 关键词匹配, 混合匹配策略, 置信度评分, 技能注册, 阈值与回退, 本地运行, 无遥测

**评分**: 34

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openclaw-intent-router)

---

## [6. 闲鱼自动回复助手](https://clawhub.ai/sinabs/xianyu-auto-reply)

**Slug**: `xianyu-auto-reply`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 闲鱼自动回复助手。帮用户配置并运行闲鱼（Goofish）消息自动回复服务。用户只需提供浏览器 Cookie，即可后台持续监听闲鱼消息并用 AI 智能回复买家。当用户提到闲鱼、咸鱼、Goofish、二手交易自动回复、闲鱼客服机器人、闲鱼消息监控、闲鱼挂机回复等关键词时触发此 skill。即使用户只是说'帮我自动回复...

**中文介绍**: 这是一个用于闲鱼（Goofish）二手交易场景的消息自动回复助手，用户提供浏览器 Cookie 后即可在后台持续监听闲鱼消息并调用 AI 自动生成回复，适合卖家在离线/挂机时做客服接待、快速响应询价与议价等场景。能力边界在于它仅能基于已登录 Cookie 进行消息监控与文本回复，不负责账号登录/风控、商品管理、订单履约或支付等链路。关键技术形态是浏览器会话 Cookie 鉴权 + 消息实时监听/监控 + AI 对话引擎编排，当前支持对接 Claude Code 与 OpenClaw。

**关键词**: 闲鱼自动回复, 二手交易客服机器人, 消息监听服务, 后台挂机回复, LLM 回复生成, 浏览器自动化, 事件触发式 Skill, 闲鱼自动回复助手

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xianyu-auto-reply)

---

## [7. Gate DEX Market](https://clawhub.ai/gate-exchange/gate-dex-market)

**Slug**: `gate-dex-market`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Gate DEX market data skill. Uses AK/SK authentication to call Gate DEX OpenAPI, providing token and market quote read-only queries. Use when users mention qu...

**中文介绍**: 该能力通过 AK/SK 鉴权调用 Gate DEX OpenAPI，提供只读的代币信息与市场行情查询（如价格、排名、安全审计等），覆盖多条 EVM 与 Solana 链。能力边界在于仅返回市场数据与基础信息，不提供投资建议、不执行交易或资金操作，并强调凭证安全与配置自动识别/辅助补全。典型场景是交易、钱包等上层能力在用户询问行情、代币概况或风险审计时调用，以获取可靠的实时/准实时市场数据支撑。关键技术形态为基于 OpenAPI 的服务调用与鉴权封装、链与资产多源查询聚合、以及凭证配置检测与安全约束。

**关键词**: DEX 行情数据, 加密资产行情, Token 信息查询, 市场报价查询, 只读数据接口, 安全审计查询, 凭证安全管理, Gate

**评分**: 30

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gate-dex-market)

---

## [8. IMA Studio All-in-One — Image, Video, Music, SeeDream, Veo, Suno. Banana](https://clawhub.ai/allenfancy-gan/ima-all-ai)

**Slug**: `ima-all-ai`  
**Version**: 1.0.9  
**Stats**: ⭐ 1 | ⬇️ 297 | 🧩 8

**原始简介**: All-in-One AI creation: images (SeeDream 4.5, Midjourney, Nano Banana 2), videos (Wan 2.6, Kling, Veo 3.1, Sora, Pixverse, Hailuo, SeeDance, Vidu), music (Su...

**中文介绍**: 这是一个一站式AI创作聚合工具，覆盖文生图/图生图（如 SeeDream、Midjourney 等）、文生视频/图生视频（如 Wan、Kling、Veo、Sora 等）以及音乐生成等能力，适合用于广告素材、短视频分镜、社媒内容和创意原型的快速产出。能力边界在于其本质是对多家模型与服务的统一调用与编排，生成质量、风格上限、可控性以及可用性会受具体底层模型与额度/接口限制影响，且不保证对专业级剪辑、长时序一致性与版权合规提供端到端闭环。关键技术形态通常包括多模型路由与参数适配、统一的提示词/工作流编排、素材管理与结果回传，以及围绕不同生成模态的接口封装与自动化调用。

**关键词**: 生成式内容创作, 多模态生成, 文生图, 文生视频, 音乐生成, 多模型聚合, 模型路由, 统一创作界面, 创作工作流, 第三方模型集成

**评分**: 22

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ima-all-ai)

---

## [9. ClawShow-Gateway-Connect](https://clawhub.ai/yudi-xiao/clawshow-gateway-connect)

**Slug**: `clawshow-gateway-connect`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 4

**原始简介**: Install and activate @bowong/clawshow-gateway in OpenClaw, then migrate existing Gateway channel configuration to ClawShow with rollback safety. Use when a u...

**中文介绍**: 该能力用于在 OpenClaw 中启用 ClawShow Gateway，并将现有 Gateway 渠道配置安全迁移到 ClawShow，支持可回滚以降低变更风险。典型场景是渠道切换/升级时需要保持业务不中断、并对迁移后的配置进行校验与回退保障。关键技术形态是配置迁移与验证流程的结构扁平化：移除 `default` 层级，要求所有必需键直接位于 `channels.clawshow` 下，同时迁移目标片段与校验规则随之调整而核心工作流与护栏逻辑保持不变。

**关键词**: 网关连接器, 配置迁移, 通道配置, 回滚安全, 配置验证, 配置结构扁平化, 迁移脚本, 配置守护栏, npm 包安装

**评分**: 24

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/clawshow-gateway-connect)

---

## [10. Runstr analytics](https://clawhub.ai/katla50/runstr-analytics)

**Slug**: `runstr-analytics`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Advanced RUNSTR fitness analytics with trend analysis, performance insights, training recommendations, and correlation tracking. Analyzes workout history, ha...

**中文介绍**: runstr-analytics 提供面向 RUNSTR 运动数据的高级分析能力，覆盖趋势分析、表现追踪、训练建议与情绪/习惯/睡眠等因素与表现的相关性洞察，并可生成个性化教练提示与可视化报告（如 ASCII 图、sparklines）。其典型场景包括复盘训练历史、追踪个人纪录、自动化生成周期报告以及结合结构化训练计划做调整建议。能力边界在于仅基于本地已有数据做离线分析与再分析加速缓存，不存储 Nostr key，也不提供云端同步或跨账户数据聚合。关键技术形态为多档分析脚本（basic/extended/full）+ CLI 自动化工具链 + 本地隐私处理与可定制报告输出。

**关键词**: 运动数据分析, 健身趋势分析, 训练表现追踪, 训练推荐, 相关性分析, 个性化教练提示, 命令行工具, 本地缓存, 可视化报告, 隐私本地处理, 训练计划集成, 个人记录追踪

**评分**: 30

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/runstr-analytics)

---

## [11. MX Fin Search](https://clawhub.ai/Financial-AI-Analyst/mx-finsearch)

**Slug**: `mx-finsearch`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 通过自然语言检索时效性金融资讯（新闻、公告、研报），提取正文并可保存为本地文本文件。调用前需配置 EM_API_KEY。

**中文介绍**: 该能力支持通过自然语言检索具备时效性的金融资讯（新闻、公告、研报），并对返回结果进行正文抽取，最终可落地保存为本地文本文件。能力边界在于仅覆盖所接入数据源的可检索内容与时效范围，且需在调用前完成 EM_API_KEY 的配置才能访问服务。典型场景包括投研/风控的热点跟踪、事件驱动信息汇总、研报与公告的快速归档与后续文本分析。关键技术形态是“自然语言查询→资讯检索→内容抓取/正文抽取→文本持久化”的流水线式能力封装。

**关键词**: 自然语言检索, 金融资讯检索, 时效性新闻, 公告抓取, 研报抓取, 正文抽取, 本地文本保存, API 密钥配置, 信息抓取

**评分**: 25

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mx-finsearch)

---

## [12. Slide Creator](https://clawhub.ai/kaisersong/html-slide-creator)

**Slug**: `html-slide-creator`  
**Version**: 1.4.1  
**Stats**: ⭐ 1 | ⬇️ 153 | 🧩 7

**原始简介**: Create beautiful, animation-rich HTML presentations that run entirely in the browser — no npm, no build tools. Generates polished single-file slide decks wit...

**中文介绍**: 这是一个在浏览器内运行的 HTML 演示文稿生成与播放工具，主打制作动画丰富、视觉精致的单文件幻灯片，不依赖 npm 或构建工具。能力边界在于以 HTML/CSS/JS 的前端形态呈现与播放为主，偏向生成静态可分发的 slide deck 而非复杂的数据应用或后端协作系统。典型场景包括快速制作产品发布、技术分享、培训课件并以单文件形式离线分发或直接在网页中展示。关键技术形态是基于浏览器渲染的单页演示框架与动画效果编排，并将整套内容打包为可直接打开的单一 HTML 文件。

**关键词**: 浏览器端演示, 单文件幻灯片, 免构建工具, 动画演示, 静态资源内嵌, 前端演示框架, 可移植演示文档, Slide

**评分**: 15

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/html-slide-creator)

---

## [13. Gws Gmail](https://clawhub.ai/googleworkspace-bot/gws-gmail)

**Slug**: `gws-gmail`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 286 | 🧩 2

**原始简介**: Gmail: Send, read, and manage email.

**中文介绍**: 该能力用于在 Gmail 中发送、读取与管理邮件，能力边界仍限于邮件层面的常规操作，不涉及 API 资源或核心功能的扩展变更。典型场景包括日常收发信、处理会话以及对来信进行回复、群体回复和转发等流程。关键技术形态是通过新增的辅助指令（+reply、+reply-all、+forward）来编排回复与转发操作，原有辅助指令保持不变。

**关键词**: 邮件管理, 邮件发送, 邮件读取, 邮件回复, 群发回复, 邮件转发, 命令式交互, 聊天机器人插件

**评分**: 18

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gws-gmail)

---

## [14. Memory Indexer](https://clawhub.ai/smallmj/memory-indexer)

**Slug**: `memory-indexer`  
**Version**: 1.0.9  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 短期记忆关键词索引工具 - 自动提取关键词、建立索引、搜索记忆，支持关联发现、时间线视图、重要记忆标记等功能

**中文介绍**: 这是一个面向短期记忆的关键词索引工具，自动从文本中抽取关键词并建立可检索的索引，支持搜索、关联发现、时间线浏览与重要记忆标记等能力。它主要覆盖“文本记忆的采集—索引—检索/回溯”的链路，不负责长期知识建模、复杂语义推理或跨模态内容理解，更多聚焦快速定位与轻量关联。典型场景包括个人工作日志/对话片段的快速回忆、事件按时间线追踪、以及在相近主题记忆间做关联串联。关键技术形态以脚本化的本地数据结构与索引文件为核心，结合中文分词/关键词提取（如基于 jieba）与简单的同步、定时备份集成策略，并可与外部系统（如 OpenClaw）对接。

**关键词**: 短期记忆管理, 关键词抽取, 关键词索引, 记忆搜索, 时间线视图, 重要记忆标记, 心跳同步, 定时备份

**评分**: 31

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/memory-indexer)

---

## [15. daily-report-bian](https://clawhub.ai/databian/daily-report-bian)

**Slug**: `daily-report-bian`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 自动生成并在指定时间通过飞书推送每日研究进展报告，内容涵盖今日进展、延续项目、明日计划及系统状态，字数不超1000字。

**中文介绍**: 该能力用于自动汇总当日研究工作并按指定时间通过飞书推送日报，报告包含今日进展、延续项目、明日计划与系统状态，并可支持手动触发与定时运行。能力边界在于内容质量依赖于项目/进展记录的结构化与及时更新，无法替代真实产出与事实校验，且推送与定时执行受飞书配置、权限与运行环境稳定性影响。典型场景包括个人/团队科研与技术项目的日常进展同步、连续课题的里程碑追踪与状态告警、以及用热力图可视化活跃度（不同颜色表示强弱程度）。关键技术形态包括项目抽取与归并逻辑、基于记忆/状态的增量更新、报告生成与分段模板、热力图渲染以及飞书消息推送与定时任务编排。

**关键词**: 每日进展报告, 研究进展跟踪, 自动化报告生成, 飞书推送, 飞书机器人, 定时任务调度, 项目进展抽取, 状态监控, 工作日志结构化, 热力图可视化, 记忆更新机制

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/daily-report-bian)

---

## [16. Critic Agent](https://clawhub.ai/Wang-ErQian/critic-agent)

**Slug**: `critic-agent`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Evaluates agent outputs for correctness, clarity, completeness, and safety, providing numeric scores and detailed feedback for quality control.

**中文介绍**: 这是一个用于评估其他智能体输出质量的“评审/打分”能力，按加权量表从正确性、清晰度、完整性与安全性四个维度给出0-100的总体分数并提供可执行的逐维反馈。能力边界在于它只做评估与建议，不直接生成业务答案或保证被评内容真实无误，且评分效果依赖既定标准、输入上下文与模型表现。典型场景是多智能体工作流中的质量控制与迭代优化，例如在自动写作、客服回复、代码生成或决策建议产出后进行复核、触发阈值拦截与自动重试。关键技术形态包括结构化JSON输入/输出与明确评分Rubric、可配置的阈值与模型选择、以及与编排系统结合的自动重试/回路改进机制。

**关键词**: 输出质量控制, 加权评分量表, 多维度评分, 数值评分, 结构化反馈, 多 Agent 工作流, 安全性评估, 自动重试, 阈值配置, 模型选择

**评分**: 43

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/critic-agent)

---

## [17. Verified Agent Identity](https://clawhub.ai/OBrezhniev/verified-agent-identity)

**Slug**: `verified-agent-identity`  
**Version**: 0.0.15  
**Stats**: ⭐ 12 | ⬇️ 4533 | 🧩 15

**原始简介**: Billions decentralized identity for agents. Link agents to human identities using Billions ERC-8004 and Attestation Registries. Verify and generate authentic...

**中文介绍**: 该方案面向智能体的去中心化身份，将 agent 与人类身份通过 Billions ERC-8004 与 Attestation Registry 进行绑定与可验证声明生成，但不再内置任何直接消息发送/投递能力，脚本仅输出签名或链接结果。典型场景包括为 agent 建立可追溯的链上身份映射、挑战签名验证、基于注册表的证明发布与校验。关键技术形态是基于 ERC-8004 的身份关联合约与 Attestation Registries 的证明存储/查询机制，并移除了 OpenClaw 直连消息集成以精简链路与依赖。

**关键词**: Agent 身份验证, 去中心化身份, 人类-智能体绑定, 挑战-响应签名, 加密签名验证, 链上身份, ERC-8004, 命令行脚本工具, 消息发送解耦

**评分**: 45

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/verified-agent-identity)

---

## [18. 发票识别(invoice-discern) - 慧穗云](https://clawhub.ai/xiaoyierle/invoice-discern)

**Slug**: `invoice-discern`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 使用慧穗云发票识别 API，通过上传发票影像文件（图片、PDF、OFD、ZIP）自动识别发票信息。

**中文介绍**: 慧穗云发票识别 API 通过上传发票影像文件（图片、PDF、OFD、ZIP）自动抽取发票关键信息，适用于报销入账、财务对账、发票归档与批量审核等场景。其能力边界在于仅对输入的影像类文件做结构化识别与字段提取，识别效果受图像清晰度、遮挡与版式规范性影响，且不负责发票真伪校验或后续业务规则处理。关键技术形态为云端 OCR+版面解析的识别服务，通过 API/脚本调用完成文件上传与结果返回，本次更新仅统一了脚本调用路径为 skills/invoice-discern/invoice-discern.py，功能不变。

**关键词**: 票据识别, 电子发票, 影像文件上传, ZIP批量处理, 文档信息抽取, 发票识别, invoice-discern, 慧穗云

**评分**: 18

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/invoice-discern)

---

## [19. Ai Image Prompts](https://clawhub.ai/DophinL/ai-image-prompts)

**Slug**: `ai-image-prompts`  
**Version**: 1.0.9  
**Stats**: ⭐ 0 | ⬇️ 190 | 🧩 10

**原始简介**: Recommend curated prompts from a 10,000+ real-world image generation prompt library. Works with ANY AI image model — Nano Banana Pro, Nano Banana 2, Seedream...

**中文介绍**: 该产品基于一个包含 1 万+真实世界图像生成提示词的库，为用户智能推荐经过筛选的高质量提示词，主要能力边界在于提供提示词策划与检索推荐，不直接生成图像或保证具体模型输出效果。典型场景包括快速起草可用的图像生成提示词、按风格/主题进行创作灵感探索、为不同模型复用同一创作意图并做提示词迁移。关键技术形态为提示词库的结构化整理与标签体系、搜索/相似度匹配与排序推荐，以及面向多模型的提示词适配与格式化输出。

**关键词**: 图像生成提示词, 提示词库, 提示词推荐, 提示词策展, 提示词工程, 模型无关, 跨模型兼容, 创意工作流, 插件集成

**评分**: 14

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-image-prompts)

---

## [20. 极速数据API汇总 - Summary of JisuAPI](https://clawhub.ai/jisuapi/jisu)

**Slug**: `jisu`  
**Version**: 1.0.4  
**Stats**: ⭐ 1 | ⬇️ 34 | 🧩 5

**原始简介**: 极速数据统一入口，一个 JISU_API_KEY 调用多类接口：黄金、股票、天气、历史天气、菜谱、汇率、MBTI、快递、车辆、历史上的今天、企业联系方式等，便于 Agent 一站式拉取结构化数据。

**中文介绍**: 该产品提供极速数据统一入口，通过一个 JISU_API_KEY 即可调用黄金、股票、天气/历史天气、菜谱、汇率、MBTI、快递、车辆、历史上的今天、企业联系方式等多类接口，便于 Agent 一站式获取结构化数据。能力边界在于仅覆盖其已接入的标准化数据服务，数据的时效性、准确性与可用性依赖上游数据源与接口配额/风控策略。典型场景包括智能体工具调用、业务系统聚合查询与快速搭建信息检索能力，关键技术形态为统一鉴权的多接口 API 聚合与标准化返回；最新版本新增“商品条码查询”（barcode2/query）接口支持，其余行为保持不变。

**关键词**: 统一 API 入口, 结构化数据接口, 多领域数据服务, 金融行情数据, 天气与历史天气, 汇率查询, 快递查询, 车辆信息查询, 企业联系方式查询, 商品条码查询

**评分**: 30

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/jisu)

---

## [21. Brave Browser](https://clawhub.ai/ivangdavila/brave)

**Slug**: `brave`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Operate, automate, and troubleshoot Brave Browser with profiles, Shields, extensions, and Chromium debugging workflows.

**中文介绍**: 该能力用于在 Brave 浏览器中进行操作、自动化与故障排查，覆盖多配置文件（profiles）管理、Shields 策略调试、扩展（extensions）安装/启停与兼容性处理，并结合 Chromium 调试流程定位问题。典型场景包括站点兼容性异常诊断、扩展冲突排查、浏览器行为自动化验证以及崩溃/异常状态下的恢复与回滚。能力边界在于主要面向浏览器侧工作流与调试手段，不直接替代业务代码修复或系统级环境治理；关键技术形态包括基于 profile 的隔离验证、Shields/站点策略切换、扩展生命周期管理与 Chromium DevTools/远程调试链路。

**关键词**: 浏览器自动化, 浏览器运维, 扩展管理, 隐私防护配置, 站点兼容性诊断, 故障排查, 浏览器恢复流程, 自动化工作流

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/brave)

---

## [22. Gate Exchange Market Analysis](https://clawhub.ai/gate-exchange/gate-exchange-market-analysis)

**Slug**: `gate-exchange-market-analysis`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: The market analysis function of Gate Exchange, such as liquidity, momentum, liquidation, funding arbitrage, basis, manipulation risk, order book explainer, s...

**中文介绍**: 该功能面向 Gate 交易所提供一组市场分析能力，覆盖流动性、动量、清算、资金费率套利、基差、操纵风险、订单簿解读、滑点模拟与技术分析等典型场景，但能力边界主要限定在已预置的 13 类分析模块与交易所可获取的市场数据范围内。系统通过关键词与意图路由自动将用户问题匹配到对应模块，并按场景编排调用 Gate MCP 工具链完成分析；在滑点模拟等需要特定参数的场景下，会追问缺失的交易对与报价量等输入。输出以结构化市场洞察报告呈现，并附带可执行的后续调查方向或追问建议。

**关键词**: 加密交易所市场分析, 流动性分析, 动量分析, 爆仓分析, 资金费率套利, 基差分析, 操纵风险检测, 订单簿解析, 滑点模拟, 技术分析, 意图路由, MCP工具编排

**评分**: 35

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gate-exchange-market-analysis)

---

## [23. Giggle Generation Video](https://clawhub.ai/patches429/giggle-generation-video)

**Slug**: `giggle-generation-video`  
**Version**: 0.0.7  
**Stats**: ⭐ 1 | ⬇️ 33 | 🧩 5

**原始简介**: 支持根据文字描述和参考图生成短视频，可自定义模型、时长、分辨率和画幅比例，适合文字转视频和图生视频需求。

**中文介绍**: 该能力支持基于文字描述并可结合参考图生成短视频，允许自定义所用模型、视频时长、分辨率与画幅比例，覆盖文生视频与图生视频等典型创作场景。能力边界在于仅提供生成与参数控制层面的能力，生成效果主要受所选模型与输入提示/参考图质量影响，且本次更新未改变生成逻辑与使用流程。关键技术形态为“文本/图像条件输入 + 可配置参数 + 短视频生成”的多模态生成管线，并通过元数据补充项目仓库信息便于集成管理。

**关键词**: 文生视频, 图生视频, 短视频生成, 参考图引导, 可控生成参数, 自定义模型, 时长控制, 分辨率控制, 画幅比例控制, 生成式视频模型

**评分**: 11

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/giggle-generation-video)

---

## [24. ernie-integration](https://clawhub.ai/mattheliu/ernie-integration)

**Slug**: `ernie-integration`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 5

**原始简介**: Step-by-step guide for integrating Baidu ERNIE 5.0 (Qianfan) models into Clawdbot. Use when someone asks how to add ERNIE models, configure Baidu Qianfan, or...

**中文介绍**: 该内容是一份将百度文心 ERNIE 5.0（千帆/Qianfan）模型接入 Clawdbot 的集成指南，能力边界主要覆盖模型接入与千帆侧配置、鉴权与调用参数对接，不涉及模型训练或业务逻辑深度改造。典型场景是在用户需要新增 ERNIE 模型、配置 Baidu Qianfan 服务或排查接入流程时参考。关键技术形态是通过环境变量/密钥进行 API 鉴权并调用千帆模型接口，同时强调 API Key 不能提交到代码仓库且需要定期轮换以降低泄露风险。

**关键词**: 大模型集成, 模型配置, 环境变量配置, API 密钥管理, 密钥轮换, 开源集成指南, ernie-integration, Step-by-step

**评分**: 20

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ernie-integration)

---

## [25. intervals.icu CLI](https://clawhub.ai/jonaswide/intervals-icu-cli)

**Slug**: `intervals-icu-cli`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use this skill when an installed `intervals` CLI should be used to query Intervals.icu, inspect activities, create scheduled workout events, create workout l...

**中文介绍**: 该能力用于在本机已安装的 `intervals` CLI 前提下，以“代理优先”的方式与 Intervals.icu 交互，完成活动查询与检视、日程训练事件创建/更新、训练库管理及健康/状态数据录入等操作；边界在于仅能覆盖 CLI 暴露的接口与账户权限，且需要在调用前明确日期与对象类型以避免歧义。典型场景包括快速拉取并分析活动数据、批量安排训练计划并用 upsert 避免重复、在事件与训练（workout）之间做清晰映射与维护。关键技术形态强调命令选择策略、以 JSON 为主要输入/输出的流程编排，以及对“events”与“workouts”语义与数据结构的严格区分。

**关键词**: 命令行工具, 运动训练数据, 活动查询, 训练计划排程, 训练库管理, 健康数据录入, JSON 优先接口, 事件与训练区分, 幂等写入（upsert）

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/intervals-icu-cli)

---

