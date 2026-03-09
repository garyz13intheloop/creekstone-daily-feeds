# ClawHub Skills Daily | 2026-03-09

> 共 25 个 skills

## [1. EngageLab Omni Connect](https://clawhub.ai/GPTBOTS/engagelab-omni-connect)

**Slug**: `engagelab-omni-connect`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: EngageLab omnichannel communication tool supporting SMS, WhatsApp, and Email.

**中文介绍**: EngageLab 的全渠道通信工具用于通过 SMS、WhatsApp 和 Email 统一发送交易类与营销类消息，边界在于聚焦消息触达与模板/变量参数的合规流程，不覆盖更上层的用户运营策略或内容生成。典型场景包括订单通知、验证码、活动触达等需要跨渠道一致编排与追踪的消息投递。关键技术形态是提供多渠道发送 API 以及 SMS/WhatsApp 的模板发现与管理 API，并通过变量与模板工作流约束审批与参数填充，降低因模板不匹配导致的发送失败。

**关键词**: 全渠道消息, 邮件发送 API, 消息模板管理, 模板审批流程, 参数变量填充, 认证鉴权, 事务性消息, 营销消息

**评分**: 26

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/engagelab-omni-connect)

---

## [2. newsnow-reader](https://clawhub.ai/Castieler/newsnow-reader)

**Slug**: `newsnow-reader`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 11 | 🧩 5

**原始简介**: 优雅地阅读实时热门新闻。支持微博、知乎、百度、抖音、华尔街见闻、今日头条、澎湃新闻等8个主流平台。

**中文介绍**: 这是一款聚合多个主流内容平台的实时热榜/热门新闻阅读工具，覆盖微博、知乎、百度、抖音、华尔街见闻、今日头条、澎湃新闻等共 8 个平台，主打统一入口的浏览体验。能力边界在于仅做公开热门内容的抓取与展示，不提供内容生产、账号管理或跨平台深度交互；各平台所需凭证为自动获取，用户无需手动配置。典型场景是快速查看不同平台的实时趋势、对比热点与选题跟踪。关键技术形态为基于外部网络请求的多站点聚合采集（依赖 curl），并在文档中透明披露访问域名、系统依赖与凭证处理及风险提示。

**关键词**: 实时新闻阅读, 热榜聚合, 多平台内容抓取, 凭证自动获取, 外部域名清单, 系统依赖说明, newsnow-reader, 优雅地阅读实时热门新闻

**评分**: 7

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/newsnow-reader)

---

## [3. Faithful Task Executor](https://clawhub.ai/endcy/faithful-task-executor)

**Slug**: `faithful-task-executor`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 任务规则忠实执行器。确保工作任务按初始要求执行，子代理/子任务始终遵循原始规则，减少 AI 幻觉和执行偏差。支持并发任务编排、规则持久化传递、执行一致性校验。

**中文介绍**: 这是一个面向多步骤与多子任务编排的“任务规则忠实执行器”，通过将初始要求持久化并在并发子代理间自动传递，确保全过程按原始规则执行、降低幻觉与执行漂移。典型用于需要强约束与可追溯输出的复杂工作流（含依赖管理、阶段化执行、可中断恢复）。关键技术形态包括规则文件/规则链路的持久化传播、阶段输出前的合规一致性校验，以及针对禁止行为清单与歧义澄清的反幻觉机制。能力边界在于它主要保障“按规则执行与一致性”，不替代领域判断本身，且对初始规则的明确性与可验证性依赖较强。

**关键词**: 任务编排, 多代理协同, 规则持久化, 规则传递, 规则合规校验, 反幻觉机制, 执行偏差控制, 输出可追溯性, 任务分解规划, 依赖管理, 断点续跑

**评分**: 49

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/faithful-task-executor)

---

## [4. Waimai Merchant](https://clawhub.ai/harrylabs0913/waimai-merchant)

**Slug**: `waimai-merchant`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 外卖商家管理 Skill - 支持商家注册、商品管理、价格修改和配送时间设置。Use when user mentions merchant registration, product management, price updates, delivery time settings for food deliv...

**中文介绍**: 该 Skill 面向外卖商家侧管理，提供商家注册/信息维护与审核、商品新增与上下架、分类库存与搜索、以及价格和配送时间设置等能力，适用于需要在本地快速搭建商家与商品运营管理的场景。能力边界在于仅覆盖商家与商品数据的管理与状态控制，不包含真实订单履约、支付结算或平台级配送调度等链路。关键技术形态为基于命令行（CLI）交互操作，数据持久化采用本地 SQLite 数据库并具备较完整的字段结构。

**关键词**: 外卖商家管理, 商家入驻, 商家审核, 状态管理, 商品管理, 商品上下架, 价格管理, 配送时间设置, 商品分类, 库存管理, 命令行界面

**评分**: 15

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/waimai-merchant)

---

## [5. NapCat QQ Bridge Installer](https://clawhub.ai/sunnyspot114514/napcat-qq-bridge-installer)

**Slug**: `napcat-qq-bridge-installer`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Install, start, repair, and smoke-test a Windows QQ + NapCat + OpenClaw bridge. Use this when the user wants an end-to-end local QQ bot setup, needs NTQQ/Nap...

**中文介绍**: 这是一个用于在本地 Windows 环境搭建并验证 QQ（NTQQ）+ NapCat + OpenClaw 桥接的端到端方案，覆盖安装、启动、修复与基础冒烟测试，面向需要快速把 QQ 机器人跑通的用户。能力边界在于仅解决本机侧的桥接与连通性验证，不承诺账号稳定性、风控规避或复杂业务逻辑编排。典型场景是本地开发调试、快速验证消息收发链路与接口可用性。关键技术形态是以 NTQQ 客户端为载体，NapCat 提供消息/事件接入与转发能力，OpenClaw 作为桥接层对外对接机器人框架或上层服务。

**关键词**: QQ 机器人, 本地部署, 端到端配置, 桥接集成, 自动启动, 修复工具, 冒烟测试, 集成测试

**评分**: 33

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/napcat-qq-bridge-installer)

---

## [6. Dev Progress Governor](https://clawhub.ai/Majmunu/dev-progress-governor)

**Slug**: `dev-progress-governor`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: govern execution hygiene for software projects. use when the user wants help enforcing git commit discipline, deciding whether work is ready to commit, gener...

**中文介绍**: 该能力用于为软件项目提供执行治理与交付卫生，聚焦在提交前就绪性检查、提交信息规范、进度日志更新、步骤完成复盘以及风险/阻塞跟踪等环节，帮助团队保持可见、可控的交付节奏。典型场景包括需要强化 Git 提交纪律、判断当前工作是否适合提交、以及在主管式工作流下持续同步进展与问题。能力边界在于只提供流程与质量门禁的建议和检查框架，不直接替代代码实现或自动决定合并发布。关键技术形态是可复用的执行治理技能模块，可嵌入到现有协作流程中以形成持续的检查与记录闭环。

**关键词**: 开发执行治理, 提交纪律, 提交就绪检查, 提交信息规范, 进度日志更新, 步骤完成度评审, 风险管理, 阻塞项跟踪, 交付可视化, 监督式工作流

**评分**: 34

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dev-progress-governor)

---

## [7. 发票查验(invoice-verify) - 慧穗云](https://clawhub.ai/xiaoyierle/invoice-verify-hsy)

**Slug**: `invoice-verify-hsy`  
**Version**: 1.0.1  
**Stats**: ⭐ 1 | ⬇️ 10 | 🧩 2

**原始简介**: 使用慧穗云发票查验 API，根据发票代码、号码、日期和金额等信息查询发票详情。

**中文介绍**: 该 API 用于基于发票代码、号码、开票日期、金额等要素在线查验并返回发票详情，适合财务报销、对账风控、进销项核验等场景。能力边界在于必须提供有效的查验要素并配置慧穗云 AK/SK 等鉴权信息，否则会返回包含密钥获取链接的错误提示；结果侧以 invoiceStatus 等字段表达发票状态（含新增部分/全额/待确认红冲等取值）。关键技术形态为带鉴权的发票查验 HTTP API，通过标准化参数与结构化响应对接业务系统。

**关键词**: 发票查验, 发票详情查询, 电子发票, 税务信息接口, 环境变量配置, 错误信息提示, 状态码扩展, 红冲状态

**评分**: 24

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/invoice-verify-hsy)

---

## [8. Diagram Generator](https://clawhub.ai/LogicTortoise/anygen-diagram-generator)

**Slug**: `anygen-diagram-generator`  
**Version**: 1.2.3  
**Stats**: ⭐ 1 | ⬇️ 129 | 🧩 6

**原始简介**: Draw any diagram or visual chart with AnyGen AI: flowchart, architecture, mind map, UML, ER, sequence, class, org chart, topology, Gantt, state, data flow, w...

**中文介绍**: AnyGen AI 用于把文字需求快速生成各类图表与可视化（如流程图、架构图、思维导图、UML、ER、时序/类图、组织架构、网络拓扑、甘特图、状态图、数据流等），适合在产品设计、技术方案评审、文档沉淀与沟通对齐中提升出图效率。其能力边界在于更擅长结构化、规则明确的关系表达，对复杂业务语义的正确性与细节一致性仍依赖输入描述质量与人工校对。关键技术形态通常是基于生成式模型将自然语言映射为图表描述语言/布局约束，再渲染为可视化输出，并持续同步上游仓库的更新以迭代图形能力与模板支持。

**关键词**: 图表生成, 流程图, 架构图, 思维导图, ER图, 时序图, 组织结构图, 拓扑图, 甘特图, 数据流图

**评分**: 17

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/anygen-diagram-generator)

---

## [9. Financial Research](https://clawhub.ai/LogicTortoise/anygen-financial-research)

**Slug**: `anygen-financial-research`  
**Version**: 1.2.1  
**Stats**: ⭐ 1 | ⬇️ 88 | 🧩 4

**原始简介**: Accelerate financial research with AnyGen AI. Uses dialogue mode to understand research scope and focus before generating. Summarize earnings, extract KPIs f...

**中文介绍**: AnyGen AI 面向金融研究加速，通过对话先澄清研究范围与关注点，再生成对应的研究内容。典型场景包括财报要点总结、关键指标（KPI）抽取与结构化整理、以及面向特定问题的研究摘要输出。能力边界在于输出质量依赖输入材料的完整性与问题定义，难以替代对数据真实性、合规与投资结论的最终判断；关键技术形态是对话式需求澄清 + 文档理解/信息抽取 + 模板化生成的组合。

**关键词**: 金融研究自动化, 财报解读, 财务指标结构化, 研究报告生成, 信息抽取, 工作流编排, Financial, Research

**评分**: 26

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/anygen-financial-research)

---

## [10. Tiger Trading](https://clawhub.ai/wjpwc/tiger-trading)

**Slug**: `tiger-trading`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 老虎证券美股交易能力。支持账户余额查询、持仓查询、买卖下单、订单管理。用户只需提供 tiger_id、account、license 和 private_key 即可使用。触发场景：(1) 查询老虎账户状态 (2) 买卖美股 (3) 查看持仓 (4) 取消订单

**中文介绍**: 该能力面向老虎证券的美股交易与账户服务，提供账户余额与状态查询、持仓查询、买卖下单及订单管理（含撤单），返回结构化 JSON 便于系统集成。典型场景包括查询账户状态与资产、查看持仓、执行美股买卖以及对未完成订单进行查询和取消。能力边界在于仅覆盖上述交易与查询链路，需用户提供 tiger_id、account、license、private_key 完成鉴权后才能调用。关键技术形态为基于老虎证券接口的程序化交易能力封装，并输出标准化数据结果用于自动化与风控流程对接。

**关键词**: 美股交易, 券商交易API, 自动化下单, 订单管理, 账户余额查询, 持仓查询, Tiger, Trading

**评分**: 24

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tiger-trading)

---

## [11. Auto-Update (OpenClaw + Skills)](https://clawhub.ai/ivangdavila/auto-update)

**Slug**: `auto-update`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Auto-update OpenClaw and skills with OpenClaw cron, per-skill defaults, backups, and migration-aware summaries.

**中文介绍**: 该功能用于通过 OpenClaw 的定时任务自动更新主程序及各个技能，提供按技能的默认更新策略，并在更新前执行备份与迁移差异检查，输出迁移感知的更新摘要。能力边界在于它聚焦于更新编排、备份与变更汇总，不涵盖技能功能本身的正确性验证或运行时问题修复。典型场景包括多技能环境的例行自动升级、版本迁移前风险评估与回滚保障。关键技术形态是基于 cron 的调度执行、按技能配置/默认策略、备份与迁移审查流程，以及结构化更新摘要生成。

**关键词**: 自动更新, 定时任务, 技能管理, 配置默认值, 增量备份, 备份恢复, 迁移管理, 迁移审查, 更新摘要, 变更日志汇总, 自动化运维

**评分**: 35

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/auto-update)

---

## [12. 土狗气象台](https://clawhub.ai/Crime1000x/tugou-monitor)

**Slug**: `tugou-monitor`  
**Version**: 1.0.2  
**Stats**: ⭐ 3 | ⬇️ 130 | 🧩 3

**原始简介**: Read public Web2 trending news and hot-search feeds from 土狗气象台, then extend promising topics with Binance Web3 public data. Supports status checks, latest me...

**中文介绍**: 该能力从土狗气象台等Web2热搜/资讯中提取关键词与话题信号，并用Binance Web3公开数据对潜在代币进行搜索与验证，产出候选到确认标的的研究卡片与摘要。典型场景是发现并跟踪meme/热点叙事、将新闻话题映射到具体代币、做快速尽调与热度校验（元数据、行情、审计、持仓与聪明钱、社交热度等）。能力边界在于依赖公开数据与规则化映射，不能保证话题与代币的唯一对应或结论准确性，且对虚假热度、同名误判与高风险meme需要额外人工判断。关键技术形态包括关键词/主题抽取、置信度分层与优先级/链优先规则、候选代币评分与多阶段映射流程，以及面向meme的触发器、分类与误报规避框架。

**关键词**: Web2趋势监控, 热搜聚合, 关键词抽取, 话题-代币映射, Web3数据增强, 链上数据分析, 代币元数据, 代币审计, 智能钱监测, 钱包持仓分析, 候选代币评分

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tugou-monitor)

---

## [13. Subscription Sentinel](https://clawhub.ai/JoeySome/subscription-sentinel)

**Slug**: `subscription-sentinel`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Subscription Sentinel — Your personal financial data agent. Sniffs email receipts, infers subscription cycles, and alerts or auto-cancels upcoming unwanted s...

**中文介绍**: Subscription Sentinel 是一款个人财务数据代理，通过分析邮箱收据识别并持续监控你的活跃订阅，推断计费周期、预测即将扣费并在临近时提醒。它还能在可行范围内提供自动取消订阅或引导式取消流程，但能力边界主要取决于邮件收据的可获取性与订阅方是否支持自动化取消。其关键技术形态包括收据解析与结构化、订阅/账单周期推断与费用预测、告警与任务自动化编排，并能让报告与沟通语言跟随用户对话语言。

**关键词**: 订阅管理, 邮件收据解析, 订阅检测, 账单周期推断, 账单提醒, 自动取消订阅, 取消流程自动化, 个人财务代理, 多语言交互

**评分**: 49

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/subscription-sentinel)

---

## [14. Feishu At Mention](https://clawhub.ai/vision-qiu/feishu-at-mention)

**Slug**: `feishu-at-mention`  
**Version**: 0.0.2  
**Stats**: ⭐ 1 | ⬇️ 24 | 🧩 2

**原始简介**: 飞书消息@提及功能。当需要在飞书消息中@群成员时使用此技能。支持三种消息类型：(1) 普通文本消息使用 at user_id 标签格式；(2) 富文本消息使用 JSON 对象格式的 tag at 元素；(3) 卡片消息使用 at id 标签格式。根据消息类型选择正确的@标签格式，确保触发飞书的@通知效果。

**中文介绍**: 该能力用于在飞书消息中正确触发对成员的@提及通知，适用于群聊中需要点名提醒、任务指派或公告告知等场景。能力边界是仅负责生成/填写各消息类型对应的@标签语法并保证不混用，不处理消息发送链路与鉴权等流程。关键技术形态分为三类：纯文本用 `at user_id` 标签、富文本用包含 `tag: at` 的 JSON 元素、卡片消息用 `at id` 标签，并强调根据消息类型选择匹配格式以确保生效。

**关键词**: 飞书集成, 消息@提及, 群成员通知, 机器人消息, 纯文本消息, 富文本消息, 卡片消息, @标签格式

**评分**: 5

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/feishu-at-mention)

---

## [15. Founder Story Brand Narrative](https://clawhub.ai/RIJOYAI/founder-story-brand-narrative)

**Slug**: `founder-story-brand-narrative`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Creates and refines Founder Story and brand narrative content for DTC/independent stores selling founder-driven products (e.g. handcrafted leather, artisan s...

**中文介绍**: 该能力用于为DTC/独立品牌生成并迭代“Founder Story”与品牌叙事，核心输出包括叙事框架、投放/落位地图以及可直接用于About页、PDP、落地页主视觉文案、邮件与包装的成稿。典型场景是手工、匠人、小批量等创始人驱动型产品品牌在上线或改版时统一叙事与转化文案，并可根据现有素材、语气、长度与渠道约束进行适配。能力边界在于当品牌不具备创始人叙事适配性时会提示不匹配，仅建议可替代的叙事要素而非强行编造。关键技术形态为结构化访谈式信息采集、模块化叙事框架生成与多渠道文案编排，强调真实差异化、避免泛化套话。

**关键词**: 创始人故事, 品牌叙事, 独立电商品牌, 手工艺产品品牌, 小批量产品, 叙事框架生成, 品牌调性指南, 信息采集问卷, 内容投放映射, 营销文案生成, 多渠道文案适配

**评分**: 17

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/founder-story-brand-narrative)

---

## [16. wxauto](https://clawhub.ai/cluic/wxauto)

**Slug**: `wxauto`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 微信自动化操作。通过 wxautox4 RESTful API 实现发送消息、获取聊天记录、监听消息、好友管理等功能。Use when: (1) 发送微信消息给好友或群聊，(2) 读取微信聊天记录，(3) 监听新消息，(4) 获取好友列表或群聊列表，(5) 接受好友申请，(6) 切换聊天窗口等微信操作。

**中文介绍**: 该能力通过 wxautox4 提供的 RESTful API 在 Windows 环境下自动化操作微信，可实现发送消息、读取聊天记录、监听新消息以及好友/群聊管理与窗口切换等。能力边界在于依赖本地微信客户端与 API 服务的可用性与授权配置，且仅支持 Windows 与指定版本的 Python 运行环境。典型场景包括批量通知、客服/运维消息监控、聊天记录拉取归档、自动通过好友申请和群聊列表同步等。关键技术形态是基于 HTTP 的接口调用与 token 连接管理，并可通过脚本或直接 API 请求集成到现有系统中。

**关键词**: 微信自动化, 微信机器人, 消息发送, 聊天记录获取, 新消息监听, 好友管理, 群聊管理, 命令行工具

**评分**: 31

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/wxauto)

---

## [17. 我的脑子](https://clawhub.ai/z44264677/mind-layer)

**Slug**: `mind-layer`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 20 | 🧩 2

**原始简介**: 基于科学记忆法构建六层分层记忆，实现情感优先和多维联想的 AI 记忆系统优化技能。

**中文介绍**: 该技能通过六层分层记忆将科学记忆法落地，强调情感优先与多维联想，并以“记忆慎重、自我成长、生存优先”的宪法级原则约束写入与使用边界，降低误记与不当留存风险。典型场景覆盖效率办公、创作娱乐、自我提升、开发运维四类任务，在连续对话与长周期复盘中形成可检索、可演进的个人化知识结构。关键技术形态包括第4层长期记忆文件的索引化与按场景的技术栈分类、细化的归档策略（含月度归档）与内容安全迁移规则，以及更规范的会话流程与长周期记忆管理机制。

**关键词**: 分层记忆, 长期记忆管理, 个人知识库, 科学记忆法, 多维联想, 情感优先, 宪法级原则, 归档策略, 月度归档, 内容索引, 内容安全迁移

**评分**: 23

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mind-layer)

---

## [18. CCFI](https://clawhub.ai/jxzly/ccfi)

**Slug**: `ccfi`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Provides China Export Container Freight Index (CCFI) data, including latest values, historical data, and statistical summaries.

**中文介绍**: 该能力提供中国出口集装箱运价指数（CCFI）的数据查询，包括最新指数、历史序列与统计汇总。能力边界在于仅覆盖CCFI相关信息检索与基础统计，不再包含任何C安全编程内容或参考资料。典型场景包括跟踪运价指数最新变化、回溯某段时间的指数走势、快速获取统计摘要用于研判与报告。关键技术形态为面向CCFI数据源的查询接口与数据处理模块（历史查询、最新值读取、统计计算）。

**关键词**: 中国出口集装箱运价指数, 航运运价数据, 集装箱运输, 指数数据查询, 历史数据查询, 最新指数查询, 统计汇总, 数据抓取, 数据接口集成

**评分**: 26

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ccfi)

---

## [19. WodeApp AI Engine](https://clawhub.ai/diankourenxia/wodeapp-ai)

**Slug**: `wodeapp-ai`  
**Version**: 1.0.12  
**Stats**: ⭐ 1 | ⬇️ 137 | 🧩 13

**原始简介**: Unified AI execution engine. Single API key (WODEAPP_API_KEY) routes to 343+ models across text, image, video, TTS, and structured JSON — with automatic cost...

**中文介绍**: 这是一个统一的 AI 执行引擎，通过单一 API Key 将请求路由到 343+ 个文本、图像、视频、TTS 与结构化 JSON 模型，并可自动进行成本相关的路由与调度。能力边界在于它主要提供聚合接入与编排层，本次更新未涉及文件或代码改动，新增能力集中在数字人头像生成及其工作流，以及面向更复杂数字人与视频生成的项目级 MCP 协议支持。典型场景包括多模态生成的一站式调用、数字人/视频内容生产链路的流程化编排，以及在项目范围内进行更高级的生成控制与协作。关键技术形态体现为统一 API 网关式路由、多模态模型池接入、工作流编排能力与项目级 MCP 协议扩展。

**关键词**: 统一AI执行引擎, 多模型路由, 单一API密钥, 多模态生成, 视频生成, 数字人头像生成, 文本转语音（TTS）, 结构化JSON输出, 自动成本优化

**评分**: 41

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/wodeapp-ai)

---

## [20. 专业宠物（猫、狗及异宠）多轮医疗问诊](https://clawhub.ai/zerojh/vetmew-consultation)

**Slug**: `vetmew-consultation`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 50 | 🧩 4

**原始简介**: 专业宠物（猫、狗及异宠）多轮医疗问诊。基于 VetMew 3.0 API 提供症状分析与诊断建议。

**中文介绍**: 该产品面向猫狗及异宠的多轮医疗问诊，通过 VetMew 3.0 API 对症状进行分析并给出诊断建议，能力边界在于提供辅助决策而非替代兽医临床检查与最终诊断。典型场景包括线上问诊分诊、常见症状初筛与用药/就医建议，以及结合上传图片进行皮肤、外观体征等视觉辅助判断。关键技术形态为基于 API 的对话式问诊引擎，支持首次运行交互式配置自动生成 .env、自动检测初始化 API 密钥，并提供图片本地/URL 上传及图片类型参数以增强分析能力。

**关键词**: 宠物医疗问诊, 多轮对话问诊, 症状分析, 诊断建议, 兽医咨询, 异宠医疗, 多模态问诊, 图像辅助诊断, 命令行工具（CLI）, API 密钥管理, 交互式初始化配置, env 配置生成

**评分**: 19

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/vetmew-consultation)

---

## [21. codropshiping-product-search](https://clawhub.ai/shan-vvv/codropshiping-product-search)

**Slug**: `codropshiping-product-search`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Searches for products on the Codrop shipping platform using a keyword.

**中文介绍**: 该能力用于在 Codrop 物流/发货平台上按关键词检索商品，需提供 API 认证 Token，成功时返回 JSON 格式的商品数据。典型场景是后台商品查询、客服快速定位商品、与内部系统做商品同步前的检索筛选。能力边界在于仅覆盖关键词搜索与结果返回，不包含商品管理、下单、库存与物流操作；并对缺参、Token 无效和服务端异常提供错误处理。关键技术形态为基于 Token 鉴权的 HTTP API 调用与结构化 JSON 响应。

**关键词**: 代发货, 电商选品, 商品检索, 关键词搜索, 商品目录 API, API 访问令牌, 错误处理, Searches

**评分**: 20

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/codropshiping-product-search)

---

## [22. Small Goods Loyalty Incentives](https://clawhub.ai/RIJOYAI/small-goods-loyalty-incentives)

**Slug**: `small-goods-loyalty-incentives`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Designs and refines customer loyalty programs and incentive systems for DTC/independent stores selling small, high-frequency products (e.g. cosmetics, phone...

**中文介绍**: 该能力面向DTC/独立站的低客单价、高复购品类，负责设计与优化会员/积分与各类促销激励体系，并产出从方案结构、激励日历到指标与验证计划的完整交付，同时给出文案与基础UX建议。典型场景包括新客欢迎、复购加速、分层会员运营、推荐拉新、满额激励与沉睡召回等，既可输出完整忠诚度体系也可只设计单一激励并根据需求自适配。关键技术形态是结构化需求采集与适配评估、可组合的激励模型（积分/等级/推荐/阈值等）以及以可衡量指标为核心的验证与生命周期节奏编排，并明确标注范围内外边界。

**关键词**: 激励机制设计, 小额高频复购, 低客单价, 积分体系, 推荐返利, 门槛优惠, 拉新欢迎礼, 流失挽回, 指标验证方案

**评分**: 20

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/small-goods-loyalty-incentives)

---

## [23. user growth coach](https://clawhub.ai/Jack-Yang-ai/user-growth-coach)

**Slug**: `user-growth-coach`  
**Version**: 2.2.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 三层反馈复盘系统，连接当前输入、历史复盘和日常上下文，自动识别深层行为模式。

**中文介绍**: 该系统以三层反馈复盘连接当前输入、历史复盘与日常上下文，通过自动模式洞察识别深层行为与动机，并给出可执行的行动处方与跨天追踪的复盘汇总。其典型场景是日常对话或记录后快速/标准/深度复盘、基于 daily-digest 的日常摘要补全复盘数据，以及持续跟踪承诺清单与次日关注点。能力边界在于洞察质量依赖输入与历史数据的完整性与一致性，偏向提供行为建议与结构化总结而非替代专业诊断或做出事实核验。关键技术形态包括分层记忆/上下文关联、自动摘要与结构化抽取、行为模式识别与动机解析、以及面向高质量推理的精细化数据与模型路由。

**关键词**: 三层反馈系统, 复盘工作流, 行为模式识别, 动机分析, 行动处方, 多粒度反馈, 日常上下文关联, 结构化总结, 跨天模式追踪, 承诺清单, 模型路由

**评分**: 45

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/user-growth-coach)

---

## [24. Human Stock Helper](https://clawhub.ai/MaxHou-infinity/human-stock-helper)

**Slug**: `human-stock-helper`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 为股票交易者提供理性分析、技术计算和策略执行提醒。基于AKShare、yfinance、pandas-ta等工具，帮助用户冰冷、果决地执行交易决策。

**中文介绍**: 这是一个面向A股/港股/美股交易者的理性交易辅助工具，依托 AKShare、yfinance 与 pandas-ta 获取实时/历史行情并计算 130+ 技术指标，输出策略分析、交易复盘与执行提醒，帮助用户更“冰冷、果决”地落实决策。能力边界在于它提供数据、指标与纪律/一致性评估等决策支持与提醒，但不保证预测准确性，也不能替代人工风险控制与最终下单判断。典型场景覆盖买入信号评估、持仓与分批止盈止损管理、策略与实际执行偏差对比、复盘记录与纪律评分等。关键技术形态以数据源聚合+技术指标计算引擎+策略规则/一致性分析为核心，并支持通过命令行进行策略与交易管理。

**关键词**: 股票交易辅助, 量化交易工具, 行情数据获取, 技术指标计算, 技术分析, 策略执行提醒, 持仓管理, 分批止盈止损, 交易复盘, 命令行工具

**评分**: 28

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/human-stock-helper)

---

## [25. Outlook Graph](https://clawhub.ai/c36025251-pixel/outlook-graph)

**Slug**: `outlook-graph`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Connect OpenClaw to Outlook and Microsoft Graph for email, calendar, contacts, and folder operations using a pre-provided access token. Use when the user ask...

**中文介绍**: 该能力通过预先提供的 Microsoft Graph 访问令牌连接 Outlook/Graph，实现邮件、日历、联系人与文件夹等对象的读取与操作，主要面向 OpenClaw 代理在用户提出相关需求时调用。能力边界在于必须依赖有效的 MS_GRAPH_ACCESS_TOKEN 授权，且本次更新仅为命名与文档/元数据规范化，不涉及功能或接口行为变更。关键技术形态为基于 Microsoft Graph API 的令牌鉴权集成，将 Outlook 资源以统一 API 方式暴露给代理执行查询与变更操作。

**关键词**: 邮件自动化, 日历管理, 联系人管理, 邮箱文件夹操作, 访问令牌认证, 环境变量配置, Outlook, Graph

**评分**: 31

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/outlook-graph)

---

