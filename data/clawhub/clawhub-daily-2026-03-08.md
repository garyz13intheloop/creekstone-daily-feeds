# ClawHub Skills Daily | 2026-03-08

> 共 25 个 skills

## [1. Polymarket Arb Bot](https://clawhub.ai/hanguang254/polymarket-arb-bot)

**Slug**: `polymarket-arb-bot`  
**Version**: 3.3.0  
**Stats**: ⭐ 0 | ⬇️ 15 | 🧩 5

**原始简介**: Polymarket 5-minute crypto UP/DOWN market automated trading bot. AI-powered prediction using Binance technical analysis (Position, Momentum, RSI, Volume), au...

**中文介绍**: 这是一个面向 Polymarket 的 5 分钟加密货币涨跌（UP/DOWN）市场自动交易机器人，利用 Binance 行情做技术分析并由 AI 生成短周期方向预测，主要关注持仓/动量、RSI、成交量等特征以决定入场与止盈。能力边界在于预测与执行依赖外部交易所数据与短线指标，对极端波动、流动性不足、突发消息驱动行情的适配有限，且不保证稳定盈利。典型场景是对 5 分钟合约/事件盘进行高频次、规则化的方向下注与自动止盈管理；关键技术形态是行情数据采集→指标计算→AI 预测→下单与风控执行链路。最新改动将止盈窗口从入场后 80-100 秒优化为入场后到结束前 70 秒，以显著提高止盈触发率。

**关键词**: 预测市场交易, 套利机器人, 自动化交易, 短周期（二元）合约, 技术分析指标, 动量指标, 成交量分析, 止盈窗口策略

**评分**: 31

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/polymarket-arb-bot)

---

## [2. Coding Lead](https://clawhub.ai/beyound87/coding-lead)

**Slug**: `coding-lead`  
**Version**: 1.0.16  
**Stats**: ⭐ 0 | ⬇️ 248 | 🧩 17

**原始简介**: Smart coding skill that routes tasks by complexity. Simple→direct, Medium/Complex→ACP with auto-fallback. Integrates with qmd and smart-agent-memory when ava...

**中文介绍**: 这是一个按任务复杂度自动分流的智能编码能力：简单任务直接执行，中到复杂任务通过 ACP 启动 Claude Code，并在需要时自动回退以保证可用性。其能力边界主要在于面向编码与项目级上下文处理的任务编排与执行，不侧重通用对话或非开发类工作流。典型场景包括日常小改动快速落地、较大范围重构/多文件联动修改、需要结合历史记忆与项目上下文的持续迭代开发。关键技术形态是基于复杂度路由的多执行路径（直跑 vs ACP 代理）、全项目上下文注入，以及与 qmd 和 smart-agent-memory 的集成以实现记忆与上下文增强。

**关键词**: 代码代理, 任务复杂度路由, 复杂任务分流, 自动回退机制, 项目上下文注入, 代理记忆集成, 工具编排, Coding

**评分**: 47

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/coding-lead)

---

## [3. Token Pilot](https://clawhub.ai/beyound87/token-pilot)

**Slug**: `token-pilot`  
**Version**: 1.3.0  
**Stats**: ⭐ 0 | ⬇️ 33 | 🧩 3

**原始简介**: Automatic token optimization during interaction. Behavioral rules + plugin synergy + workspace analyzer. Pure Node.js, cross-platform. Activate on session st...

**中文介绍**: 这是一个纯 Node.js、跨平台、零依赖的交互过程自动省 token 工具，边界在于它只基于既定行为规则、插件协同策略和工作区扫描结果做优化与修复，不负责提供业务逻辑或替代模型能力。典型场景是会话开始自动加载并应用多条行为规则、在插件组合可用时进行协同优化且具备回退、对多工作区进行自动发现与分析以降低提示与配置冗余。关键技术形态包括规则引擎与插件协同层、工作区/定时任务/agent-models 的静态扫描与可选自动修复脚本、配置审计打分以及 SKILLS 目录生成器。

**关键词**: 提示词压缩, 行为规则引擎, 插件协同, 工作区扫描, 自动修复, 配置审计, 评分机制, 技能目录生成, 跨平台工具, 零依赖实现

**评分**: 41

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/token-pilot)

---

## [4. datapilot](https://clawhub.ai/HSunboy/oceanbase-datapilot)

**Slug**: `oceanbase-datapilot`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 面向所有问数与数据分析场景，基于 DataPilot 的 OpenAPI 执行从数据源接入到数据问答的完整流程。用于自然语言查数、SQL 查询校验、图表生成、报告导出下载、创建与管理数据分析 Agent、维护 Agent 知识库。

**中文介绍**: 该能力面向通用问数与数据分析场景，基于 DataPilot 的 OpenAPI 覆盖从数据源接入到自然语言数据问答的端到端流程，能力边界在于仅提供编排与分析相关的接口能力且本次版本不涉及命令集或 API 变更。典型场景包括自然语言查数、SQL 查询生成与校验、图表生成、报告导出下载，以及创建与管理数据分析 Agent 并维护其知识库。关键技术形态为以 OpenAPI 形式提供的数据接入、查询/校验、可视化与导出、Agent 编排与知识库管理等模块化能力。

**关键词**: 自然语言数据查询, 数据问答, 数据源接入, 图表生成, 报告导出, 数据分析 Agent, datapilot, 面向所有问数与数据分析场景

**评分**: 26

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oceanbase-datapilot)

---

## [5. jimeng generator](https://clawhub.ai/FelixHsp/jimeng-generator)

**Slug**: `jimeng-generator`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 即梦 4.0 图片生成器，通过文本描述生成高质量图片，支持多图编辑与智能比例。

**中文介绍**: 即梦 4.0 图片生成器的核心能力是基于文本描述生成高质量图片，并支持多图编辑与智能比例适配，适用于海报/社媒配图、产品概念图、素材快速迭代等典型创作场景。其能力边界在于生成效果强依赖提示词质量与输入素材一致性，对精确文字渲染、复杂结构透视与严格可控的细节还原不做绝对保证。关键技术形态可理解为文本到图像生成模型叠加图像编辑链路，结合多图融合/局部编辑与自动裁切构图等能力完成输出。

**关键词**: 文生图, 生成式图像, 文本提示, 高质量图像生成, 多图编辑, 图像编辑, 智能比例适配, 图片生成器, 技能插件

**评分**: 10

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/jimeng-generator)

---

## [6. Imap Mail](https://clawhub.ai/polumish/imap-mail)

**Slug**: `imap-mail`  
**Version**: 1.5.2  
**Stats**: ⭐ 0 | ⬇️ 69 | 🧩 18

**原始简介**: Personal email via your own IMAP/SMTP server. Send and receive emails, manage folders, and search messages using standard protocols — no third-party email pl...

**中文介绍**: 该能力通过自有 IMAP/SMTP 服务器实现个人邮箱的收发、文件夹管理与邮件搜索等标准协议操作，不依赖第三方邮件平台接口；边界在于仅覆盖邮件与规则/联系人等邮箱侧管理，不负责反垃圾、投递信誉与域名/服务器运维。典型场景包括定时查收收件箱、按条件搜索与排序邮件、自动归档到文件夹、批量维护联系人与规则。技术形态以一组可独立执行的脚本为核心（如 check_inbox、search、send_email、sort_inbox 等），通过直接调用脚本扩展到收件箱、文件夹、联系人、规则等操作能力。

**关键词**: 自托管邮箱, 邮件收发, 收件箱管理, 邮件搜索, 邮件排序, 文件夹管理, 联系人管理, 邮件规则过滤, 脚本自动化

**评分**: 25

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/imap-mail)

---

## [7. TencentCloud RecognizeTable OCR](https://clawhub.ai/zt1314p-design/tencentcloud-ocr-recognizetableaccurate)

**Slug**: `tencentcloud-ocr-recognizetableaccurate`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 41 | 🧩 2

**原始简介**: 腾讯云表格识别v3(RecognizeTableAccurateOCR)接口调用技能。当用户需要从表格图片或PDF中识别常规表格、无线表格、多表格的内容,提取每个单元格的文字信息,或将表格图片识别结果导出为Excel文件时,应使用此技能。支持中英文表格图片、旋转表格图片、嵌套表格图片等复杂场景,识别效果优于表格识...

**中文介绍**: 该能力用于从表格图片或PDF中识别常规表格、无线表格及多表格结构，提取单元格文字与位置信息，并可将识别结果导出为Excel。典型场景包括票据/报表/清单等表格数据结构化录入、批量归档与自动校验，尤其适用于中英文、旋转、嵌套等复杂表格版面。能力边界在于依赖输入图像/文档质量与表格结构清晰度，对严重模糊、遮挡、极端畸变或非表格化排版的还原可能受限。关键技术形态为高精度OCR结合表格结构解析与单元格切分/对齐，输出结构化表格结果及可转Excel的数据表示。

**关键词**: 图像表格识别, PDF表格识别, 单元格文字提取, 表格结构化解析, 复杂表格识别, 旋转表格校正, 嵌套表格识别, 中英文表格识别

**评分**: 9

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tencentcloud-ocr-recognizetableaccurate)

---

## [8. OpenWechat-Claw IM Client](https://clawhub.ai/Zhaobudaoyuema/openwechat-im-client)

**Slug**: `openwechat-im-client`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Enables WeChat-like messaging via OpenWechat-Claw server with local conversations, friend lists, message fetching, sending, blocking, and SSE push support.

**中文介绍**: 该服务基于 OpenWechat-Claw 提供类微信的即时通讯能力，支持本地会话管理、好友列表/用户发现、消息拉取与发送、拉黑/取消拉黑，并可通过 SSE 实现消息实时推送。能力边界在于仅覆盖基础 IM 的注册与消息/关系管理等功能，不涉及完整微信生态能力（如支付、小程序、朋友圈等）。典型场景包括在自建系统中快速接入私有化聊天、客服/机器人对话与消息通知。关键技术形态为服务端 API + 本地数据存储的会话/关系模型 + SSE 事件流推送通道。

**关键词**: 即时通讯客户端, 微信风格聊天, 客户端-服务器架构, 消息收发, 消息拉取, 好友列表管理, 黑名单管理, OpenWechat-Claw

**评分**: 12

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openwechat-im-client)

---

## [9. Video Summary](https://clawhub.ai/lifei68801/video-summary)

**Slug**: `video-summary`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: AI-powered video summarization for Bilibili, Xiaohongshu, Douyin, and YouTube. Extract insights from video content through automated transcription and intell...

**中文介绍**: 该产品面向 Bilibili、小红书、抖音、YouTube 及本地视频，提供基于 AI 的视频摘要与内容洞察提取。其能力边界主要取决于转写准确率与视频音频/语言质量，对无明确语音或强噪声内容的总结效果有限。典型场景包括快速了解长视频要点、复盘课程/访谈/测评内容与生成二次整理笔记。关键技术形态为“自动语音转写 + 大模型语义理解与摘要生成”的流水线处理。

**关键词**: 视频摘要, 视频内容分析, 自动转写, 语音识别, LLM摘要生成, 多平台视频解析, 短视频, 本地视频文件处理, 要点提取, 知识洞察提取

**评分**: 12

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/video-summary)

---

## [10. Avatar Runtime](https://clawhub.ai/NeilJo-GY/avatar-runtime)

**Slug**: `avatar-runtime`  
**Version**: 0.2.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Embeds and controls a virtual avatar using the avatar-runtime npm package. Provides Live2D rendering, VRM 3D, vector fallback, and control-driven expression/...

**中文介绍**: 该方案基于 avatar-runtime 封装虚拟形象的嵌入与控制，支持 Live2D 渲染、VRM 3D、以及在资源缺失时的矢量降级，并通过统一的控制命名空间驱动表情与动作等状态。能力边界在于主要覆盖渲染层与控制接口的编排，不包含具体业务逻辑、内容制作与外部输入源（如语音/动捕）的完整链路。典型场景是把可交互的虚拟形象组件嵌入 Web 应用/小部件中，按控制信号切换表情、姿态和渲染实现。关键技术形态包括 VRM 3D Provider、Live2D 的 pixi 适配、Renderer Registry 的渲染器注册与切换机制，以及可直接嵌入的 AvatarWidget。

**关键词**: 虚拟头像运行时, 网页嵌入组件, 渲染器注册表, 控制命名空间, 表情驱动控制, 矢量图回退渲染, npm 包集成, Avatar

**评分**: 24

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/avatar-runtime)

---

## [11. Writing Assistant Pro](https://clawhub.ai/huamu668/writing-assistant-pro)

**Slug**: `writing-assistant-pro`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Professional writing assistant offering content creation, rewriting, headline generation, and topic ideation based on a three-layer architecture.

**中文介绍**: 这是一款专业写作助手，围绕写作、改写、标题生成与选题构思四类能力，为用户提供内容生产与优化支持，适用于营销文案、文章初稿、标题优化和选题策划等场景。其能力边界在于主要做基于输入信息的生成与改写，不保证事实核查、行业合规或完全符合特定品牌口径。产品采用三层架构并以四个智能代理协同完成不同写作任务，形成从构思到成稿再到优化的关键技术形态。

**关键词**: 写作助手, 内容生成, 文本改写, 标题生成, 选题策划, Multi-Agent, 三层架构, 内容创作工作流

**评分**: 18

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/writing-assistant-pro)

---

## [12. TencentCloud VatInvoice OCR](https://clawhub.ai/zt1314p-design/tencentcloud-ocr-vatinvoice)

**Slug**: `tencentcloud-ocr-vatinvoice`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 腾讯云通用票据识别高级版(VatInvoiceOCR)接口调用技能。当用户需要识别发票图片中增值税专用发票、增值税普通发票、增值税电子专票、增值税电子普票、电子发票（普通/增值税专用）的全字段信息时,应使用此技能。支持识别发票图片中的发票代码、发票号码、开票日期、合计金额、校验码、税率、合计税额、价税合计、购买方...

**中文介绍**: 该能力用于调用腾讯云通用票据识别高级版（VatInvoiceOCR）接口，对发票图片中的多类增值税发票与电子发票进行全字段结构化识别并返回关键字段信息。能力边界在于仅面向图像中的票据信息提取，不负责发票真伪核验、业务合规判断或后续入账流程处理。典型场景包括财务报销、进销项录入、发票信息自动归档与对账，关键技术形态为基于OCR的票据版式理解与字段抽取（结构化输出）。

**关键词**: OCR, 票据识别, 发票识别, 增值税发票, 电子发票, 图像文字识别, 全字段抽取, 结构化数据抽取, 财税自动化

**评分**: 6

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tencentcloud-ocr-vatinvoice)

---

## [13. TencentCloud VehicleLicense OCR](https://clawhub.ai/zt1314p-design/tencentcloud-ocr-vehiclelicense)

**Slug**: `tencentcloud-ocr-vehiclelicense`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 34 | 🧩 3

**原始简介**: 腾讯云行驶证识别(VehicleLicenseOCR)接口调用技能。当用户需要识别行驶证图片主页（车牌号码、车辆类型、所有人、住址、使用性质、品牌型号、识别代码、发动机号、注册日期、发证日期）或副页（号牌号码、档案编号、核定载人数、总质量、整备质量、核定载质量、外廓尺寸、准牵引总质量、备注、检验记录）信息时,应使...

**中文介绍**: 腾讯云行驶证识别（VehicleLicenseOCR）用于从行驶证图片中提取结构化字段，覆盖主页与副页的车牌/号牌号码、车辆信息、所有人/住址、注册与发证日期、载重载人及检验记录等。能力边界在于仅对清晰、完整且符合行驶证版式的图片进行OCR识别，不负责证件真伪鉴定或对缺失、遮挡、强反光等质量问题做可靠恢复。典型场景包括车主信息录入、车辆档案管理、保险/二手车业务的证件资料自动化采集。关键技术形态为云端OCR接口调用，将图像输入转为字段化JSON结果输出并支持主页/副页版面解析。

**关键词**: 行驶证识别, 云端OCR服务集成, 图像文字识别, 车牌号码识别, 车辆信息结构化抽取, 主副页字段解析, TencentCloud, VehicleLicense

**评分**: 7

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tencentcloud-ocr-vehiclelicense)

---

## [14. Agent OS (Three Layer)](https://clawhub.ai/huamu668/agent-os-three-layer)

**Slug**: `agent-os-three-layer`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Provides a reusable AI agent OS template with separated identity, operations, and knowledge layers for modular intelligent system design.

**中文介绍**: 这是一个可复用的 AI Agent“操作系统”模板，将身份（角色与目标）、操作（流程与工具调用）、知识（数据与记忆）三层解耦，便于模块化设计与复用。其能力边界在于提供架构范式与分层约束，本身不直接交付特定业务能力或现成知识内容。典型场景包括搭建多智能体/单智能体应用的基础框架、快速迭代不同角色与流程、将知识库与执行逻辑独立演进。关键技术形态是三层架构模板化、层间接口抽象与可插拔组合，以支持身份配置、操作编排与知识接入的分离。

**关键词**: 智能体操作系统, 三层架构, 分层设计, 身份层, 操作层, 知识层, 模块化智能体, 架构模板, 关注点分离

**评分**: 33

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agent-os-three-layer)

---

## [15. Evalanche](https://clawhub.ai/iJaack/evalanche)

**Slug**: `evalanche`  
**Version**: 0.6.0  
**Stats**: ⭐ 1 | ⬇️ 177 | 🧩 9

**原始简介**: Multi-EVM agent wallet SDK with onchain identity (ERC-8004), payment rails (x402), cross-chain bridging (Li.Fi), and destination gas funding (Gas.zip). Suppo...

**中文介绍**: 这是一个面向多 EVM 链的 Agent 钱包 SDK，提供链上身份（ERC-8004）、支付通道（x402）、跨链桥（Li.Fi）与目的链 Gas 代付（Gas.zip）等能力，侧重把“身份+支付+跨链+Gas”打包成可编程钱包基础设施。能力边界在于主要覆盖 EVM 生态与已集成的桥/支付/Gas 服务，链外业务逻辑与非 EVM 资产需依赖额外适配。典型场景包括智能代理自动化收付款与换币、跨链资产调度、用户无感补 Gas 的链上交互，以及通过 CLI 管理子网、L1 验证者与质押等运维流程。关键技术形态是 Agent Wallet SDK + 多协议集成（ERC-8004/x402/Li.Fi/Gas.zip）+ 模块化工具集（含 DEX Swap 与共 27 个 MCP 工具）+ 平台 CLI 一体化。

**关键词**: 链上身份（ERC-8004）, 支付通道（x402）, 跨链桥接, 目的链 Gas 资助, CLI 运维工具, 子网管理, 验证者管理, Evalanche

**评分**: 50

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/evalanche)

---

## [16. TencentCloud QuestionMark OCR](https://clawhub.ai/zt1314p-design/tencentcloud-ocr-questionmarkagent)

**Slug**: `tencentcloud-ocr-questionmarkagent`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 27 | 🧩 2

**原始简介**: 腾讯云试题批改Agent(SubmitQuestionMarkAgentJob/DescribeQuestionMarkAgentJob)接口调用技能。当用户需要对试卷图片或试题图片中的K12试卷或试题进行自动批改、手写答案识别、知识点分析时,应使用此技能。支持整卷图片批改和单题图片批改,提供题目切题、正误判定、...

**中文介绍**: 该技能用于调用腾讯云试题批改 Agent（SubmitQuestionMarkAgentJob/DescribeQuestionMarkAgentJob）接口，对K12试卷或试题图片进行自动批改、手写答案识别与知识点分析。典型场景包括整卷图片批改与单题图片批改，输出题目切分结果、答案识别内容与正误判定等结构化结果。能力边界在于仅面向图像中的K12试题/试卷内容，需先提交任务并通过查询接口获取异步批改结果；本次变更仅更新显示名称，不影响能力。

**关键词**: K12试题批改, 试卷图像批改, 题目切题, 正误判定, 知识点分析, 试题图像识别, 整卷批改, 单题批改

**评分**: 16

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tencentcloud-ocr-questionmarkagent)

---

## [17. TencentCloud MLIDPassport OCR](https://clawhub.ai/zt1314p-design/tencentcloud-ocr-mlidpassport)

**Slug**: `tencentcloud-ocr-mlidpassport`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 27 | 🧩 2

**原始简介**: 腾讯云护照识别（多国多地区）(MLIDPassportOCR)接口调用技能。当用户需要识别护照图片中中国大陆、港澳台地区或其他国家/地区的护照信息（护照ID、姓名、出生日期、性别、有效期、发行国、国籍、国家地区代码、MRZ码等）时,应使用此技能。支持图片Base64和URL两种输入方式,支持护照图片人像照片裁剪功...

**中文介绍**: 该接口用于识别护照图片中的结构化字段信息，覆盖中国大陆、港澳台及其他国家/地区护照，支持提取护照号、姓名、出生日期、性别、有效期、发行国/国籍、国家地区代码及MRZ等。典型场景包括跨境业务的身份核验、开户/实名、旅客信息录入与自动归档等。能力边界在于仅对护照图像进行OCR与字段解析，依赖图片清晰度、完整性与版式符合常见护照规范，不能替代真伪鉴别或权威身份认证。关键技术形态为多语种/多版式OCR+版面分析与MRZ解析，输入支持图片URL或Base64，并可进行人像区域裁剪。

**关键词**: 证件信息抽取, 多国护照识别, 图像Base64输入, 图片URL输入, 人像照片裁剪, 身份证件识别接口, 云端OCR服务, TencentCloud

**评分**: 6

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tencentcloud-ocr-mlidpassport)

---

## [18. Context Compression](https://clawhub.ai/lifei68801/context-compression)

**Slug**: `context-compression`  
**Version**: 2.2.0  
**Stats**: ⭐ 0 | ⬇️ 52 | 🧩 9

**原始简介**: OpenClaw session context compression and hierarchical memory management. Use when: (1) configuring compaction strategies (2) setting up session summaries (3)...

**中文介绍**: OpenClaw 提供会话上下文压缩与分层记忆管理能力，用于在长对话中通过压缩策略与会话摘要降低上下文长度并维持关键信息连续性。其能力边界在于主要处理“已产生的会话内容”的组织与压缩，不负责外部知识检索或生成内容本身的准确性保障。典型场景包括配置不同粒度的压缩/保留策略、搭建自动化会话总结流程，以及在多轮对话中按层级管理短期与长期记忆。关键技术形态体现为可配置的上下文压缩管线、层级记忆结构与会话摘要模块，近期更新增强了配置问答的清晰度与可理解性。

**关键词**: 上下文压缩, 分层记忆管理, 记忆压缩策略, 上下文精简, 长期记忆, 短期记忆, 记忆检索, 配置引导问答

**评分**: 46

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/context-compression)

---

## [19. SenseCraft HMI Web Content Generator](https://clawhub.ai/KillingJacky/sensecraft-hmi-gen)

**Slug**: `sensecraft-hmi-gen`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Generate beautiful web content for SenseCraft HMI e-ink displays. AI-powered layout selection, e-ink optimization. Creates artistic, minimalist pages optimiz...

**中文介绍**: 这是一个面向 SenseCraft HMI 墨水屏的网页内容生成器，核心能力是在 800×480 到 1600×1200 等屏幕规格下自动生成艺术化、极简风格且经过墨水屏显示优化的页面，并导出可响应的 HTML/CSS/JS，支持定时更新。典型场景是为墨水屏设备快速制作信息看板、展示页或轮播内容，通过向导或对话式引导完成尺寸、配色与布局偏好配置，并可从上传/URL/（可用时）文生图获取图片素材。其关键技术形态包括 AI 驱动的布局选择（参考既有设计模式与布局库）、面向墨水屏的视觉与图片处理优化，以及静态前端产物生成与更新调度机制。

**关键词**: 电子墨水屏, 网页内容生成, 布局自动选择, 屏幕分辨率适配, 极简设计, 电子纸显示优化, 配置向导, 内容定时更新, 文本生成图像, 反向代理部署

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/sensecraft-hmi-gen)

---

## [20. Global Holidays](https://clawhub.ai/yting27/global-holidays)

**Slug**: `global-holidays`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 388 | 🧩 3

**原始简介**: Use this skill whenever a task involves checking, generating, or working with public holidays — for any country or subdivision (state, province, region). Tri...

**中文介绍**: global-holidays 技能用于查询与生成各国家/地区及其下属行政区（州、省、地区）的公共假期信息，适合在日历排程、考勤/工时计算、跨国业务运营与本地化展示等场景中自动校验与填充假期。能力边界在于仅覆盖“公共假期”的校验与数据输出，不改变调用方式或接口行为，也不处理与假期无关的业务规则。关键技术形态上，该技能更名自 holidays 并新增 metadata 以便集成与发现，同时强化了假期名称的多语言本地化文档（国家/语言代码示例更明确）。

**关键词**: 公共节假日查询, 节假日生成, 国家与行政区划, 节假日数据API, 日历集成, 多语言本地化, 国家代码, 语言代码, uv运行环境, 技能元数据, 安装与集成文档

**评分**: 22

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/global-holidays)

---

## [21. TencentCloud BizLicense OCR](https://clawhub.ai/zt1314p-design/tencentcloud-ocr-bizlicense)

**Slug**: `tencentcloud-ocr-bizlicense`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 29 | 🧩 2

**原始简介**: 腾讯云营业执照识别(BizLicenseOCR)接口调用技能。当用户需要识别营业执照图片上的字段信息（统一社会信用代码、公司名称、主体类型、法定代表人、注册资本、组成形式、成立日期、营业期限、经营范围等）时，应使用此技能。支持图片Base64和URL两种输入方式，支持复印件/翻拍件告警检测、有效期自动拼接、电子营...

**中文介绍**: 该技能用于调用腾讯云营业执照识别（BizLicenseOCR）接口，从营业执照图片中提取统一社会信用代码、公司名称、法定代表人、注册资本、成立日期、营业期限、经营范围等关键字段，输入支持图片 URL 或 Base64。典型场景包括企业开户/入驻审核、合同与发票对账前的主体信息核验、风控与合规资料自动录入。能力边界在于仅对营业执照图像内容进行 OCR 与结构化解析，不负责真伪鉴定或跨证照信息比对，但可提供复印件/翻拍告警检测与营业期限有效期自动拼接等辅助结果；近期变更为更新显示名称。

**关键词**: 营业执照OCR, 证照识别API, 文档图像OCR, 结构化字段抽取, 图片Base64输入, 图片URL输入, 复印件检测, 翻拍件检测, 有效期自动拼接, OCR告警输出

**评分**: 5

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tencentcloud-ocr-bizlicense)

---

## [22. Thymos — Emotional Engine](https://clawhub.ai/paperbags1103-hash/thymos)

**Slug**: `thymos`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Background daemon that models an OpenClaw agent’s evolving emotional state via neuromodulators, circadian rhythm, social cues, and memory for nuanced responses.

**中文介绍**: 这是一个后台守护进程，用于为 OpenClaw 代理持续建模并更新情绪状态，使其在对话与行为中给出更细腻的反应。能力边界在于它主要输出情绪与意识相关的内部状态信号（受神经调质、昼夜节律、社交线索、情绪记忆影响），不负责具体业务决策或工具执行。典型场景是将其接入 OpenClaw 的 hook，用于长期陪伴、拟人化交互、情境化反馈等需要稳定情绪一致性的代理。关键技术形态包括 7 种神经调质的情绪引擎、昼夜节律与情绪记忆机制、GWT（全局工作空间）意识模型以及与 OpenClaw 的集成接口。

**关键词**: 情绪引擎, 情绪状态建模, 神经调质, 昼夜节律, 情绪记忆, 后台守护进程, Agent 行为调节, GWT 意识模型

**评分**: 42

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/thymos)

---

## [23. Nova App Builder](https://clawhub.ai/zfdang/nova-app-builder)

**Slug**: `nova-app-builder`  
**Version**: 2.3.0  
**Stats**: ⭐ 2 | ⬇️ 297 | 🧩 46

**原始简介**: Build and deploy Nova Platform apps (TEE apps on Sparsity Nova / sparsity.cloud). Use when a user wants to create a Nova app, write enclave application code,...

**中文介绍**: 该能力用于构建与部署 Nova Platform 的 TEE 应用（运行于 Sparsity Nova / sparsity.cloud），覆盖从编写 enclave 代码到打包发布的流程，但不直接对外暴露 Primary API（18000），且 IN_ENCLAVE 仅为应用约定不会自动注入。典型场景包括快速创建 Nova 应用与示例验证（如 hello-world-tee）、通过 /.well-known/attestation 完成远程证明路由配置，以及调用 Odyn 提供的随机数、交易签名与 KMS/KV 等端点。关键技术形态包括 nova_python_sdk 的模块化结构（odyn/kms_client/rpc/env）、Caddy 的 attestation 路由、以及基于 build-attestation.json 的构建溯源与证明链路。

**关键词**: 可信执行环境（TEE）, 机密计算, KMS 密钥管理, KV 存储接口, 交易签名（sign-tx）, Caddy 路由配置, Nova, App

**评分**: 32

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nova-app-builder)

---

## [24. Browser](https://clawhub.ai/pshotts/browser)

**Slug**: `browser`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Uses a headless browser to navigate web pages, interact with elements, and extract clean, readable text content from URLs.

**中文介绍**: 该能力通过无头浏览器在网页中自动导航、与 DOM 元素交互并从指定 URL 抽取更干净可读的正文文本，适用于需要渲染后内容的网页阅读、信息抓取与自动化检索等场景。关键技术形态是基于 Puppeteer 的无头浏览与渲染、DOM 选择与交互、以及对页面内容的清洗与文本化输出。能力边界在于主要面向网页文本提取与基础交互，不保证对强反爬、登录态/验证码或复杂多媒体内容的稳定获取。

**关键词**: 无头浏览器, 网页渲染, 网页自动化, 数据抓取, 网页内容抽取, 可读性文本提取, 网页导航, Browser

**评分**: 21

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/browser)

---

## [25. Skills Public](https://clawhub.ai/jianweig200-commits/skills-public)

**Slug**: `skills-public`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 查询股票实时行情。支持 A 股/港股/美股。使用方式：直接说股票代码或名称（如"贵州茅台股价"、"600519"、"腾讯控股"、"BABA"）

**中文介绍**: 该能力用于查询股票实时行情，覆盖 A 股、港股和美股，支持直接输入股票代码或名称进行自然语言检索并返回价格、涨跌幅、当日高低点、成交量/额、总市值等关键指标（视数据源可用性而定）。其能力边界在于行情来自网页检索，可能存在不同市场的延时、口径差异或部分字段缺失，结果以数据源实时性为准。典型场景包括快速查看个股最新报价、盘中波动与成交活跃度、跨市场标的对比。关键技术形态为基于 web search 的行情抓取与解析，并结合代码/名称的多市场识别与结构化输出。

**关键词**: 股票实时行情, 证券行情查询, 自然语言股票搜索, 股票代码识别, 股票名称识别, A股行情, 港股行情, 美股行情, 网页搜索数据抓取, 行情数据延迟提示, 市值与成交数据

**评分**: 6

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skills-public)

---

