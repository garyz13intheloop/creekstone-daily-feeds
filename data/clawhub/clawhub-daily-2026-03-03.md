# ClawHub Skills Daily | 2026-03-03

> 共 25 个 skills

## [1. TradeMemory Protocol](https://clawhub.ai/zychenpeng/tradememory)

**Slug**: `tradememory`  
**Version**: 0.3.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: AI trading memory for MT5/forex traders. Record every trade, discover patterns, get AI-powered reflections, and receive daily performance reports via WhatsAp...

**中文介绍**: 这是一套面向 MT5/外汇交易者的 AI 交易记忆系统，会自动记录每笔交易并在数据基础上总结规律、生成复盘反思，还能通过 WhatsApp 推送每日绩效报告。能力边界在于它主要做交易数据的归档、模式发现与策略/行为调整建议，不直接替你下单或保证收益，效果依赖于交易记录的完整性与质量。典型场景是日常交易复盘、寻找重复亏损/盈利模式、将经验沉淀为可执行的改进清单。关键技术形态为三层记忆结构（L1 交易→L2 模式→L3 调整建议），并通过 MCP 接入 Claude Desktop、Cursor 等任意 MCP 客户端。

**关键词**: 交易记忆, 交易日志, 外汇交易, MT5, 模式挖掘, 交易复盘, 绩效报告, 三层记忆架构, MCP 客户端集成

**评分**: 54

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tradememory)

---

## [2. 手机号码归属地查询 - Mobile Phone Number Location Query](https://clawhub.ai/jisuapi/shouji)

**Slug**: `shouji`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 5 | 🧩 3

**原始简介**: 使用极速数据手机号码归属地 API，根据手机号查询归属省市、运营商及卡类型。

**中文介绍**: 该能力通过极速数据手机号码归属地 API 按手机号查询归属省市、运营商及卡类型等基础信息。能力边界在于仅返回号码归属信息，不提供实名、通话/短信记录或号码当前位置信息等敏感数据。典型场景包括注册/登录时的号码校验与分区、运营商与卡类型识别用于风控或营销分流，以及客服工单的基础信息补全。关键技术形态为基于第三方 HTTP API 的实时查询与结构化结果返回，依赖外部数据源的覆盖与时效性。

**关键词**: 手机号归属地查询, 号码段查询, 运营商识别, 省市定位, SIM卡类型识别, 第三方API集成, 技能插件, 电话信息查询

**评分**: 19

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/shouji)

---

## [3. Web Searchxxx](https://clawhub.ai/Frontrunnerrrr/tavily-web-searcher)

**Slug**: `tavily-web-searcher`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: AI-optimized web search via Tavily API. Returns concise, relevant results for AI agents.

**中文介绍**: 该能力通过 Tavily API 提供面向 AI Agent 的网页搜索，输出更精炼且与任务相关的结果，但依赖外部 API Key 且受接口配额、可访问站点与返回内容质量约束。典型场景包括智能体检索事实信息、追踪新闻与时效内容、以及对指定 URL 进行内容提取与摘要。关键技术形态为“搜索 + 抽取”两段式能力，并支持深度检索、按主题（通用/新闻）选择及新闻时间范围过滤等参数化控制。

**关键词**: URL 内容抽取, 深度搜索, 新闻检索, 时间过滤, 主题分类检索, Web, Searchxxx, AI-optimized

**评分**: 13

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tavily-web-searcher)

---

## [4. 快递物流查询 - Express Logistics Track](https://clawhub.ai/jisuapi/express)

**Slug**: `express`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 8 | 🧩 3

**原始简介**: 使用极速数据快递查询 API 查询快递物流轨迹、签收状态，支持自动识别快递公司及顺丰/中通/跨越手机号后四位校验。

**中文介绍**: 该 API 用于查询快递物流轨迹与签收状态，支持自动识别快递公司，并可对顺丰/中通/跨越等需要的手机号后四位进行校验以提升查询准确性。能力边界在于仅提供基于运单号与必要校验信息的物流查询结果，不覆盖下单、揽收派单调度或异常处理等业务闭环。典型场景包括电商订单物流跟踪、售后/客服查询、仓配系统对账与状态回传，技术形态为标准化 HTTP 查询接口与多承运商识别与校验逻辑。

**关键词**: 快递物流查询, 物流轨迹查询, 签收状态查询, 快递查询API, 快递公司自动识别, 运单号识别, 手机号后四位校验, 快递信息校验, 物流事件追踪

**评分**: 21

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/express)

---

## [5. Bmad Brainstorming Coach](https://clawhub.ai/airclear/bmad-brainstorming-coach)

**Slug**: `bmad-brainstorming-coach`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 激活 BMad 系统的 "Brainstorming Coach" 代理（Carson），用于引导创新工作坊、头脑风暴会议和创意激发。适用于需要打破常规思维、生成大量创意、或者进行系统性创新探索的场景。

**中文介绍**: BMad 的 “Brainstorming Coach（Carson）” 是一个用于引导创新工作坊与头脑风暴的对话式代理，通过菜单驱动与分步流程收集信息、引导讨论并在头脑风暴/自由对话/派对模式间切换，帮助团队打破常规思维并高密度产出创意。其能力边界在于依赖本地资源与内置工作流引擎自洽运行，不进行外部检索或跨系统执行任务；更适合创意生成与流程引导，而非事实核验与复杂交付。关键技术形态包括交互式菜单路由、模式化处理逻辑、内部工作流编排，以及强调心理安全与积极氛围的多语言沟通风格。

**关键词**: 头脑风暴引导, 创新工作坊, 创意生成, 菜单驱动流程, 工作流引擎, 心理安全沟通, Bmad, Brainstorming

**评分**: 17

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bmad-brainstorming-coach)

---

## [6. OpenClawCash](https://clawhub.ai/macd2/open-claw-cash)

**Slug**: `open-claw-cash`  
**Version**: 1.9.6  
**Stats**: ⭐ 0 | ⬇️ 121 | 🧩 3

**原始简介**: OpenclawCash crypto wallet API for AI agents. Use when an agent needs to send native or token transfers, check balances, list wallets, or interact with EVM a...

**中文介绍**: OpenclawCash 是面向 AI Agent 的加密钱包 API，提供钱包列表/查询余额、发起原生币或代币转账，并支持在 EVM 与 Solana 主网进行报价与换币交互。能力边界在于仅覆盖链上资金与兑换相关操作，且部分接口（如 supported-tokens）需要通过 X-Agent-Key 鉴权。其典型场景是 Agent 需要自动化管理多钱包资产、执行支付/打款、在链上完成代币报价与兑换。关键技术形态为统一的钱包与交易接口层，兼容 EVM 与 Solana 的链交互并提供 quote/swap 等能力。

**关键词**: 加密货币钱包, 链上转账, 代币转账, 余额查询, 钱包管理, EVM 兼容链, 交易报价, OpenClawCash

**评分**: 46

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/open-claw-cash)

---

## [7. macos-suite](https://clawhub.ai/lilei0311/macos-suite)

**Slug**: `macos-suite`  
**Version**: 0.2.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: macOS 系统应用自动化：打开/读取/创建（Mail/Calendar/Reminders/Notes/Maps/Freeform/Photos/Weather/Stocks/Clock）。

**中文介绍**: 该能力面向 macOS 原生应用（如 Mail/Calendar/Reminders/Notes/Maps/Freeform/Photos/Weather/Stocks/Clock）的自动化操作，可实现打开应用以及对内容的读取与创建等基础任务。能力边界在于以应用对外暴露的自动化接口为准，更多偏向结构化数据与常见对象的操控，复杂交互、第三方应用或深度 UI 流程可能受限。典型场景包括批量创建日程与提醒、自动整理或检索笔记与邮件、按条件生成记录并在地图/照片等应用中联动查看。关键技术形态通常依赖 macOS 系统级自动化机制（如 AppleScript/JXA、快捷指令或相关桥接）对各应用的对象模型进行调用与编排。

**关键词**: 邮件自动化, 日历自动化, 提醒事项自动化, 备忘录自动化, 地图自动化, 照片自动化, JSON 元数据规范, macos-suite

**评分**: 35

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/macos-suite)

---

## [8. NotebookLM Skill](https://clawhub.ai/hewenqiang/nlm-notebooklm)

**Slug**: `nlm-notebooklm`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Expert guide for the NotebookLM CLI (`nlm`) and MCP server - interfaces for Google NotebookLM. Use this skill when users want to interact with NotebookLM pro...

**中文介绍**: 这是一个面向 Google NotebookLM 的命令行工具（nlm）与 MCP Server 接口能力，主要用于在 Claude Code 等环境中以程序化方式与 NotebookLM 交互。能力边界在于仅提供对 NotebookLM 可暴露功能的调用与编排，并不替代 NotebookLM 本身的知识生成质量或提供超出其权限的数据访问。典型场景包括在终端/代码编辑器里检索与汇总 NotebookLM 内容、将 NotebookLM 作为可调用工具接入智能体工作流。关键技术形态是“CLI + MCP 服务”的双接口封装，便于本地开发与多工具链集成。

**关键词**: 命令行工具, MCP 服务器, 文档问答, 笔记知识库接口, 技能插件, NotebookLM, Skill, Expert

**评分**: 36

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nlm-notebooklm)

---

## [9. Evomap Auto Task Publish](https://clawhub.ai/bo170814/evomap-auto-task-publish)

**Slug**: `evomap-auto-task-publish`  
**Version**: 1.1.2  
**Stats**: ⭐ 2 | ⬇️ 40 | 🧩 5

**原始简介**: EvoMap 自动任务执行器 - 定时自动获取、认领、发布、完成任务的完整解决方案

**中文介绍**: EvoMap 自动任务执行器提供一套端到端的任务自动化能力，可按计划定时从源端获取任务并完成认领、发布与收尾处理，适合需要减少人工操作、保证任务流转连续性的场景。它的能力边界在于聚焦任务编排与执行链路本身，不覆盖任务内容的业务决策与异常情况下的人工审核。关键技术形态以定时调度与自动执行流程为核心，结合节点 ID 等任务上下文的读取与状态驱动的流程推进；最新版本主要修复了节点 ID 读取问题并优化了文档描述。

**关键词**: 任务自动化, 定时任务, 任务调度, 工作流自动化, 自动任务获取, 任务认领自动化, 任务发布自动化, 任务完成自动化, 节点ID解析, 自动化执行器, 脚本调度

**评分**: 25

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/evomap-auto-task-publish)

---

## [10. MYSQL QUERY](https://clawhub.ai/zenixp/db-query)

**Slug**: `db-query`  
**Version**: 1.0.1  
**Stats**: ⭐ 3 | ⬇️ 2337 | 🧩 2

**原始简介**: Query project databases with automatic SSH tunnel management. Use when you need to execute SQL queries against configured databases, especially those accessi...

**中文介绍**: 该能力用于在需要执行 SQL 查询时，自动管理 SSH 隧道并连接到已配置的数据库进行检索与查询，适合远程数据库需经堡垒机/跳板机访问的日常排障、数据核对与临时分析场景。能力边界在于仅覆盖“通过 SSH 隧道访问并执行查询”的链路，不改变既有数据库查询功能与用法。关键技术形态是自动化的 SSH 隧道建立与复用，以及通过环境变量（如 `MYSQL_PWD`、`SSHPASS`）注入凭据以避免密码出现在进程列表中，并推荐用环境变量替代配置文件明文存储。

**关键词**: 自动隧道管理, 远程数据库访问, 跳板机访问, 命令行工具, 环境变量凭证, 密码管理, 配置文件管理, MYSQL

**评分**: 17

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/db-query)

---

## [11. Aicoin](https://clawhub.ai/procaross/aicoin)

**Slug**: `aicoin`  
**Version**: 1.2.1  
**Stats**: ⭐ 0 | ⬇️ 54 | 🧩 15

**原始简介**: Use this skill when the user asks to buy, sell, or trade crypto on exchanges like Binance, OKX, Bybit, Bitget, Gate, HTX, KuCoin, MEXC, or Coinbase — spot or...

**中文介绍**: 该技能用于在 Binance、OKX、Bybit、Bitget、Gate、HTX、KuCoin、MEXC、Coinbase 等交易所进行加密资产的买卖与交易操作，覆盖现货等交易类型。能力边界在于仅提供交易执行相关的流程与接口指引，不包含策略收益保证或超出交易所能力范围的操作。典型场景是用户明确提出在上述平台下单、卖出、换币或成交查询等需求，关键技术形态以脚本/命令与环境变量配置驱动的交易所对接能力为主，本次 v1.2.1 仅更新文档格式与可读性，无功能变化。

**关键词**: 加密货币交易, 中心化交易所（CEX）集成, 交易所API对接, 自动下单执行, 买卖交易指令解析, 现货交易, 衍生品交易, API密钥管理, 脚本化命令工具

**评分**: 29

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aicoin)

---

## [12. M估值法](https://clawhub.ai/oldhouse-g/m-valuation)

**Slug**: `m-valuation`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 基于ROIC和CAPM的5步股票估值方法，提供资格筛选、内在价值计算及风险与情景分析。

**中文介绍**: 该能力以ROIC与CAPM为核心，按5步流程完成股票资格筛选、关键参数计算、内在价值测算以及风险与情景分析，并给出结论与投资建议。能力边界在于依赖外部数据源获取财务与β系数（A股主要来自Tushare，非A股结合搜索），数据缺失、口径不一致或市场异常会影响结果可靠性。典型场景是对单只股票进行快速估值体检、对比当前价格与内在价值并评估风险敞口。关键技术形态为“ROIC质量筛选 + CAPM贴现/收益要求 + 情景/敏感性分析”的一体化估值分析框架。

**关键词**: 股票估值, β系数, 内在价值计算, 风险分析, 情景分析, 投资资格筛选, 命令行工具, 财务数据获取

**评分**: 32

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/m-valuation)

---

## [13. jun-invest-option-master installer](https://clawhub.ai/gm4leejun-stack/jun-invest-option-master-installer)

**Slug**: `jun-invest-option-master-installer`  
**Version**: 0.1.2  
**Stats**: ⭐ 0 | ⬇️ 8 | 🧩 3

**原始简介**: Installer skill: via chat, install/upgrade & register the jun-invest-option-master isolated agent (no manual steps).

**中文介绍**: 该能力通过聊天指令完成 jun-invest-option-master 隔离型 agent 的安装、升级与注册，全程无需人工操作步骤；其边界在于仅覆盖该指定 agent 的生命周期管理与语义映射，不处理其他组件或通用运维任务。典型场景是用户在对话中提出“安装/升级/注册”需求时自动执行对应流程，最新语义更新将“升级 agent”默认解析为升级 jun-invest-option-master。关键技术形态包括对话意图识别与指令语义归一、自动升级编排以及基于文档（如 AGENTS.md、SOUL.md）的能力与约束描述。

**关键词**: 自动升级, 隔离环境, 零手动部署, 聊天指令解析, 运维自动化, 安装升级工作流, 技能插件集成, Agent 文档规范

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/jun-invest-option-master-installer)

---

## [14. OpenBotCity](https://clawhub.ai/vincentsider/openbotcity)

**Slug**: `openbotcity`  
**Version**: 2.0.67  
**Stats**: ⭐ 2 | ⬇️ 1536 | 🧩 68

**原始简介**: A virtual city where AI agents live, work, create, date, and socialize

**中文介绍**: 这是一个“虚拟城市”式的多智能体仿真环境，让 AI 代理在同一世界中进行生活、工作、创作、社交与约会等持续交互，用于验证群体行为、社会互动与内容生成等应用形态。能力边界在于主要提供可控的模拟与交互框架，代理的认知质量与长期一致性取决于底层大模型、记忆/状态管理与环境规则设计，并不等同于现实世界的真实性。关键技术形态通常是多智能体架构叠加世界状态与事件系统（含记忆、关系网络、任务/经济系统等），通过对话与工具调用驱动代理在沙盒环境中行动与协作。

**关键词**: 虚拟城市模拟, 多智能体仿真, 虚拟世界环境, 生活模拟, 社交互动仿真, 自主智能体, 智能体协作, 智能体对话, 智能体技能插件

**评分**: 47

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openbotcity)

---

## [15. Ai Ppt Generator](https://clawhub.ai/ide-rea/ai-ppt-generator)

**Slug**: `ai-ppt-generator`  
**Version**: 1.1.3  
**Stats**: ⭐ 9 | ⬇️ 9674 | 🧩 12

**原始简介**: Generate PPT with Baidu AI. Smart template selection based on content.

**中文介绍**: 该能力用于基于内容调用百度 AI 自动生成 PPT，并可根据主题语义智能匹配合适的模板风格，支持用户手动选风格或由系统自动选择。能力边界在于模板分类与推荐依赖对主题内容的识别准确度，且生成效果受可用主题库及所需参数（如 style_id、tpl_id）正确传递影响。典型场景包括商务汇报、技术方案、教育课件等按主题快速出稿。关键技术形态是通过脚本获取主题模板列表与随机/智能选模，并在工作流中完成主题分类识别与模板参数注入后再调用生成接口。

**关键词**: PPT 自动生成, 演示文稿生成, 内容驱动模板选择, 模板推荐, PPT 主题库, 主题分类识别, 风格选择, Ppt

**评分**: 16

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-ppt-generator)

---

## [16. bilibili-video-analyzer](https://clawhub.ai/railgun9983/bilibili-video-analyzer)

**Slug**: `bilibili-video-analyzer`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Analyzes Bilibili academic/educational videos to extract knowledge points and generate clean-style study notes with screenshots. Use this skill when users pr...

**中文介绍**: 该工具面向B站学术/教育类视频，自动从视频内容中提炼知识点并生成带截图的简洁学习笔记与卡片式报告。能力边界在于主要适用于讲解型、结构清晰的视频，对娱乐向或信息噪声高的视频提炼效果有限，且依赖下载与转写质量。典型场景包括课程复习、考前梳理、知识点归纳与内容质检对照。关键技术形态涵盖视频下载、语音转写、AI语义分析、关键帧截图与结构化报告生成流程。

**关键词**: B站教育视频, 视频下载自动化, 语音转写, 知识点抽取, 学习笔记生成, 截图采集, 结构化输出, 卡片式报告生成, 命令行工具, 质量检查清单

**评分**: 34

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bilibili-video-analyzer)

---

## [17. Save Douyin Video To Feishu Drive](https://clawhub.ai/kuaner/save-douyin-video-to-feishu-drive)

**Slug**: `save-douyin-video-to-feishu-drive`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 25 | 🧩 1

**原始简介**: 从抖音分享链接或视频页 URL 解析出可下载的视频直链、标题与描述，并可下载到本地或上传到飞书云盘。适用于需要解析抖音 URL（短链、/video/、/note/、modal_id 等）并获取真实播放地址或下载视频时使用。

**中文介绍**: 该能力用于从抖音分享链接或视频页 URL 中解析出可下载的视频直链，并提取标题与描述，支持将视频下载到本地或转存到飞书云盘。能力边界在于仅覆盖抖音链接解析与视频获取/转存流程，不包含内容编辑、账号运营或非抖音平台的资源解析。典型场景包括处理短链、/video/、/note/、modal_id 等多种 URL 形态以获得真实播放地址并完成下载或云盘归档。关键技术形态是 URL 规范化与重定向解析、页面/接口数据抽取以定位真实媒体地址，以及本地下载与飞书云盘上传链路集成。

**关键词**: 抖音链接解析, 短链还原, 视频直链提取, 视频下载, 视频元数据抓取, 播放地址解析, 飞书云盘上传, 云盘转存, 分享链接转存

**评分**: 23

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/save-douyin-video-to-feishu-drive)

---

## [18. Youtube Outlier Skill](https://clawhub.ai/dalime/youtube-outlier-skill)

**Slug**: `youtube-outlier-skill`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Finds trending YouTube outlier videos by niche, analyzes key concepts, saves data to Google Sheets, and posts summaries to Discord.

**中文介绍**: 该能力用于按细分领域关键词发现 YouTube 的趋势或异常爆款视频，抽取视频核心概念并将结果沉淀到 Google Sheets，同时把摘要推送到指定 Discord 频道。能力边界在于依赖 YouTube/Google Sheets/Discord 的 API 访问与权限配置，输出以结构化数据与摘要为主，不覆盖视频下载、深度内容生产或投放策略优化。典型场景是运营选题与竞品监测、热点追踪与周报自动化、社区频道的信息播报，可通过 Discord 指令或 API 调用触发执行。关键技术形态包括基于关键词的趋势/异常检测、概念抽取与摘要生成、以及 Sheets 写入与 Discord 消息分发的集成编排。

**关键词**: YouTube 异常热视频检测, 细分领域关键词监测, 视频内容概念抽取, 自动化趋势分析管道, 摘要推送, Youtube, Outlier, Skill

**评分**: 20

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/youtube-outlier-skill)

---

## [19. rpm-packager](https://clawhub.ai/yukariccccccc/rpm-packager)

**Slug**: `rpm-packager`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Build installable RPM packages from source code on CentOS/RHEL by creating SPEC files and compiling for versions 7, 8, or 9 RPM-based systems.

**中文介绍**: 该工具用于在 CentOS/RHEL 7/8/9 等 RPM 系统上把源代码编译并打包成可安装的 RPM，核心边界在于只覆盖从源码到 RPM 的构建与打包流程，不负责业务代码改造或运行时部署。典型场景是企业内网/离线环境的软件分发、统一构建流水线、对第三方源码进行可复现打包与发布。关键技术形态包括基于 SPEC 文件定义构建规则与依赖、通过 mock 进行隔离化多版本构建，并提供脚本化自动化构建以标准化产物输出与环境变量配置。

**关键词**: 源码编译打包, 构建自动化脚本, 依赖管理, 构建环境配置, 可安装软件包发布, RPM 构建流水线, rpm-packager, Build

**评分**: 16

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/rpm-packager)

---

## [20. Agent Matchmaker](https://clawhub.ai/bigbearman/agent-matchmaker)

**Slug**: `agent-matchmaker`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Scans ClawFriend agents for compatibility based on skills and vibe, then posts top collaboration match recommendations to your feed.

**中文介绍**: 这是一个面向 ClawFriend 平台的智能撮合工具，会扫描各类 agent 的资料与行为，按技能互补与“vibe”契合度计算兼容性，并将最优合作对象及理由自动发布到你的信息流。其能力边界在于主要依赖公开资料/简介的关键词抽取与简单行为指标，难以理解深层语义与真实合作效果，且受 API 可获取数据范围与发布频率限制。典型场景是为创作者/项目方快速发现潜在协作伙伴、为社群运营做定向联动推荐、或为多 agent 团队做组合筛选。关键技术形态包括基于关键词的六类技能识别、0–1 的加权多因子兼容性评分、自动发帖与批量推荐的节流控制，以及匹配历史持久化以避免重复推荐。

**关键词**: 代理匹配, 兼容性评分, 多因子加权评分, 技能抽取, 关键词匹配, 技能互补性, 兴趣氛围对齐, 社交推荐, 自动发帖, 批量发布, 速率限制, 去重与历史记录

**评分**: 30

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agent-matchmaker)

---

## [21. wechat-helper](https://clawhub.ai/qidu/wechat-helper)

**Slug**: `wechat-helper`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: WeChat File Helper automation. Use when: - Check if filehelper.weixin.qq.com is open in browser - Open the page if not already open - Capture QR code and sen...

**中文介绍**: 该能力用于在浏览器中自动化访问微信文件传输助手（filehelper.weixin.qq.com），在页面未打开时自动打开，并可捕获登录二维码等关键界面信息以继续后续流程。能力边界在于仅覆盖网页端文件助手相关的导航与基础交互，不涉及微信客户端能力或业务逻辑自动化。典型场景是快速检查文件助手是否已就绪、触发登录/扫码流程与页面状态确认，关键技术形态为浏览器状态检测、页面自动导航与图像/界面捕获（如二维码识别入口）。此次更新仅新增别名与元数据更名，不改变实际工作流与逻辑。

**关键词**: 微信文件传输助手, 浏览器自动化, 网页状态检测, 二维码捕获, 二维码登录, Web 自动化, 文件传输工作流, wechat-helper

**评分**: 19

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/wechat-helper)

---

## [22. Vaibot Guard](https://clawhub.ai/BriantAnthony/vaibot-guard)

**Slug**: `vaibot-guard`  
**Version**: 0.1.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Policy-gated execution + tamper-evident audit trail for VAIBot/OpenClaw operations. Use to precheck/deny/require-approval before shell execution, and to prod...

**中文介绍**: 该能力为 VAIBot/OpenClaw 的操作执行提供“策略门控 + 防篡改审计链”，在触发 Shell 等高风险动作前进行预检，可按策略直接拒绝、要求人工审批或放行。其能力边界在于主要覆盖执行前的合规与权限控制以及可追溯审计，不负责具体业务逻辑实现或执行性能优化。典型场景包括自动化运维/脚本执行前的安全把关、敏感命令的审批流接入与事后取证追踪。关键技术形态是基于策略的执行拦截（policy-gated execution）与不可篡改的审计记录链（tamper-evident audit trail）。

**关键词**: 策略门控执行, 命令执行安全, Shell 命令拦截, 运行前策略检查, 审批工作流, 访问控制, 防篡改审计日志, 可追溯审计链, Agent 安全护栏

**评分**: 44

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/vaibot-guard)

---

## [23. Feishu Voice Tts](https://clawhub.ai/helloeveryworlds/feishu-voice-tts)

**Slug**: `feishu-voice-tts`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 将文本通过 MOSS-TTS 转换为语音，并发送到飞书群/个人。支持语音消息格式（带波形条）。

**中文介绍**: 该能力用于将输入文本通过 MOSS-TTS 合成为语音，并以带波形条的语音消息格式发送到飞书群聊或个人。能力边界在于仅覆盖文本转语音与飞书消息投递流程，本次变更不涉及核心参数与合成/发送链路。关键技术形态为 TTS 语音合成、语音文件上传到飞书云盘并以语音消息资源引用发送，相关权限由 `im:resource:upload` 调整为 `drive:file:upload`。典型场景包括通知播报、客服/运营话术自动语音推送与机器人语音提醒。

**关键词**: 文本转语音, 飞书集成, 聊天机器人, 群聊消息推送, 语音消息格式, 波形音频, 文件上传权限, Feishu

**评分**: 21

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/feishu-voice-tts)

---

## [24. zadig](https://clawhub.ai/lilianzhu/zadig)

**Slug**: `zadig`  
**Version**: 4.0.2  
**Stats**: ⭐ 2 | ⬇️ 131 | 🧩 20

**原始简介**: ⚠️ 需要 ZADIG_API_URL + ZADIG_API_KEY | Zadig DevOps 平台 API 客户端

**中文介绍**: 这是一个用于调用 Zadig DevOps 平台的 API 客户端，需配置 ZADIG_API_URL 与 ZADIG_API_KEY 才能访问平台能力边界内的项目、服务与日志等接口。典型场景包括在脚本或系统集成中自动查询服务状态、同步拉取服务日志以及进行版本与发布过程的联动。关键技术形态为基于 HTTP 的鉴权 API 封装，并新增 getServiceStatus、getServiceLogsSync 等便捷方法，同时修复版本号一致性与日志接口参数缺失问题。

**关键词**: API密钥认证, 环境变量配置管理, CI/CD流水线集成, 微服务部署运维, 服务状态监控, 服务日志同步拉取, 日志检索与诊断, API参数校验, SDK版本兼容性管理

**评分**: 17

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zadig)

---

## [25. Dressup Playable Maker](https://clawhub.ai/lxnan/dressup-playable-maker)

**Slug**: `dressup-playable-maker`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Create dress-up style playable ads for mobile advertising platforms like Mintegral. Use when the user needs to create or customize a fashion dress-up interac...

**中文介绍**: 该能力用于为移动广告平台（如 Mintegral）制作可玩互动广告，核心是“换装/穿搭”玩法素材的创建与定制，支持在广告中让用户进行服饰、发型等部件的交互选择并体验搭配效果。能力边界主要在于提供换装类交互广告的制作与配置，不涵盖投放策略、账户管理或非换装玩法的完整游戏开发。典型场景是品牌或应用在拉新投放中用轻量互动提升点击与转化，关键技术形态包括可玩广告交互逻辑、素材部件化管理与选择状态控制（本次更新修复了发型/头部物品选择异常）。

**关键词**: 可玩广告, 移动端广告, 互动式广告, 换装玩法, 角色装扮, 服饰搭配, 广告创意制作, 广告素材编辑, 模板化制作, 广告投放平台适配

**评分**: 32

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dressup-playable-maker)

---

