# ClawHub Skills Daily | 2026-03-06

> 共 25 个 skills

## [1. 输入图片后，通过优图人像分割模型，进行自定义人像分割，识别传入图片中人体的完整轮廓，进行抠像，输出带透明背景的人像图。](https://clawhub.ai/Neck-cn/tencentcloud-yt-segment-portrait)

**Slug**: `tencentcloud-yt-segment-portrait`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Binary classification-based human portrait segmentation for complete body contour recognition and image matting.

**中文介绍**: 该能力基于二分类的人像分割模型，实现对完整人体轮廓的识别并输出抠图/分割结果，适用于证件照与电商素材抠图、背景替换、虚化与特效制作等场景。能力边界在于仅面向“人像”前景的分割与 matting，结果质量受输入图像清晰度、遮挡与复杂背景影响，且不负责通用物体分割或交互式精修。关键技术形态为调用腾讯云人像分割 API 的服务化能力，通过密钥鉴权与脚本化调用返回分割掩码/抠图结果。

**关键词**: 人像分割, 人体轮廓识别, 图像抠像, 透明背景输出, 二分类分割, 密钥配置管理, 跨平台脚本, 输入图片后

**评分**: 6

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tencentcloud-yt-segment-portrait)

---

## [2. Polymarket FastLoop Trader](https://clawhub.ai/AndrewBrownrd/polymarket-simmer-fastloop)

**Slug**: `polymarket-simmer-fastloop`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 5

**原始简介**: Trade Polymarket BTC/ETH/SOL 5/15-minute fast markets with momentum and order book filters.

**中文介绍**: 该能力用于在 Polymarket 的 BTC/ETH/SOL 5/15 分钟快市场中进行量化交易，提供动量/均值回归策略，并可叠加盘口、机构净流入等过滤条件来筛选入场与退出信号。能力边界在于仅覆盖上述标的与快周期市场，且默认以模拟盘运行，实盘需显式切换并依赖外部账户与环境配置。典型场景是短周期捕捉趋势延续或回撤反转，并通过波动率调整仓位、时段过滤与手续费精确建模提升执行一致性。关键技术形态包括可配置策略参数表、基于订单簿与净流数据的信号过滤、以及支持定时任务/自动化触发的运行方式。

**关键词**: 自动化交易机器人, 短周期交易, 动量策略, 均值回归策略, 订单簿过滤, 机构净流过滤, 波动率调整仓位, 时段过滤, 纸面交易, 实盘交易, 手续费精确执行

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/polymarket-simmer-fastloop)

---

## [3. Safe Skill Advisor](https://clawhub.ai/Crystaria/safe-skill-advisor)

**Slug**: `safe-skill-advisor`  
**Version**: 1.5.1  
**Stats**: ⭐ 0 | ⬇️ 54 | 🧩 7

**原始简介**: Security Skill Advisor - Help identify malicious skills, protect API keys and system security | Security audit, skill scanner, malware detection, best practices

**中文介绍**: Security Skill Advisor 是面向技能生态的安全审计与风险识别工具，主要用于发现恶意技能、检测潜在恶意行为并提供安全最佳实践建议，以降低 API Key 泄露与系统被滥用的风险。其能力边界在于偏向静态/规则与配置层面的扫描与审计提示，无法替代运行时的入侵检测或对未知高级攻击的完整取证。典型场景包括上线前的技能安全评审、存量技能仓库的批量扫描、以及对接外部 API 前的密钥与权限配置核查；关键技术形态通常是技能扫描器/安全审计器，结合恶意模式检测与规则库输出风险报告与修复建议。最新更新修复了 YAML 头部标签展示与版本号标注问题。

**关键词**: 技能安全审计, 恶意技能检测, 恶意软件检测, API 密钥防护, 凭证泄露检测, 系统安全加固, 安全最佳实践, 静态安全分析, YAML 元数据校验

**评分**: 36

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/safe-skill-advisor)

---

## [4. prp](https://clawhub.ai/inuh22/proj-2)

**Slug**: `proj-2`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Provides a detailed self-reflection on project development, highlighting learning, challenges, skill growth, and personal development in system design and pr...

**中文介绍**: 该能力用于对项目开发过程进行结构化自我复盘，聚焦学习收获、挑战应对、技能成长以及系统设计与个人发展的变化脉络。能力边界在于它侧重主观总结与经验提炼，不直接产出代码或替代客观评审，并可明确标注本版本无文件变更、技能内容未更新等状态。典型场景包括项目阶段复盘、个人能力成长记录、团队分享与绩效材料沉淀。关键技术形态以叙事式反思内容为主体，辅以版本变更日志/差异检测来追踪内容是否发生更新。

**关键词**: 项目复盘, 系统设计, 软件工程实践, 架构设计, 需求分析, 问题解决, 技能成长, 学习总结, 个人发展

**评分**: 8

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/proj-2)

---

## [5. Finance Web Monitor](https://clawhub.ai/warriorfan/finance-web-monitor)

**Slug**: `finance-web-monitor`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Monitor and summarize finance websites for fund-investing support. Use when user asks to fetch finance site text, track changes, or schedule periodic monitor...

**中文介绍**: 该能力用于在无需登录的前提下抓取财经网站文本并提炼摘要，为基金投资提供市场概览、关键要闻与基金相关洞察（可按需强调风险），并支持一次性检查或按计划周期性监控。它的能力边界主要在公开网页内容的获取与对比，无法覆盖需要账号权限或无法被抓取的页面。典型场景包括用户请求读取指定财经站点内容、跟踪页面更新并输出变更报告、以及定时生成简报。关键技术形态包括网页文本抽取与摘要生成、基于工作区状态快照的跨周期差异检测，以及通过 cron 实现自动化调度与按需即时简报。

**关键词**: 金融网站监控, 网页文本抽取, 内容摘要, 市场概览生成, 风险重点分析, 变更检测, 状态快照, URL列表管理, 即时简报

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/finance-web-monitor)

---

## [6. Ashare Fund Intel](https://clawhub.ai/warriorfan/ashare-fund-intel)

**Slug**: `ashare-fund-intel`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Produce scheduled A-share and fund intelligence reports with bullish and bearish signals, source-backed analysis, and position-adjustment suggestions. Use wh...

**中文介绍**: 该能力边界在于自动定时生成A股与基金情报报告，围绕多空信号、持仓调整建议与风险提示做基于来源的分析，并要求每条结论可追溯到明确URL且遵循来源优先级规则。典型场景包括盘前/盘后/夜间净值与业绩跟踪、用户主动请求市场与基金简报、净值确认以及持仓复盘。关键技术形态是多模式报告编排（盘前/盘后/夜间）、按风险偏好与持仓/自选/输出格式的个性化生成，以及以证据链与引用规范为核心的检索与生成结合。

**关键词**: A股市场情报, 基金情报, 定时报告生成, 盘前盘后简报, 夜间净值核对, 收益公告解读, 多源信息溯源, 多空信号汇总, 仓位调整建议, 风险偏好个性化, 自选股自选基监控

**评分**: 47

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ashare-fund-intel)

---

## [7. proj 1](https://clawhub.ai/inuh22/proj-1)

**Slug**: `proj-1`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Reflect on project development to enhance technical skills, problem-solving, time management, research abilities, and personal growth through self-evaluation.

**中文介绍**: 该项目主要用于在项目开发过程中进行自我反思与复盘，帮助提升技术能力、问题解决、时间管理、研究能力与个人成长，但能力边界在于它更偏方法与记录框架，无法提供实质性的新功能或自动化分析产出。典型场景是研发迭代结束后的自评、复盘与能力沉淀，以及对过往决策和失误的纠正记录。关键技术形态以文档化（如 SKILL.md）与版本化变更记录为核心，本次 1.0.1 仅更新文档以承认先前错误，未引入新特性。

**关键词**: 项目复盘, 技术能力提升, 问题解决, 时间管理, 研究能力, 个人成长, 文档维护, 技能清单, 经验总结

**评分**: 9

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/proj-1)

---

## [8. Report Ppt Generator Pro](https://clawhub.ai/loommo/report-ppt-generator-pro)

**Slug**: `report-ppt-generator-pro`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Generate professional PowerPoint presentations from text manuscripts and style examples. Use when users want to create PPT slides from written content, espec...

**中文介绍**: 该能力可将文本稿件结合用户提供的风格示例自动生成专业PPT，并通过交互式预览与可编辑PPTX导出支持反复确认与迭代调整，适用于将报告、方案、演讲稿快速转成可展示的幻灯片等场景。能力边界在于输出质量依赖输入稿件结构与风格示例清晰度，且AI插图为可选辅助并需用户审核确认。关键技术形态包括风格抽取、自动大纲生成、布局模板编排、AI/用户图片融合、HTML预览与分阶段引导式工作流。

**关键词**: PPT 自动生成, 文稿转幻灯片, 风格示例匹配, 版式模板, 大纲生成, HTML 交互预览, 迭代式编辑流程, AI 插图生成, 分步式引导流程

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/report-ppt-generator-pro)

---

## [9. GitHub Actions Timeout Risk Audit](https://clawhub.ai/daniellummis/github-actions-timeout-risk-audit)

**Slug**: `github-actions-timeout-risk-audit`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Audit GitHub Actions job runtime risk against timeout thresholds so near-timeout jobs get fixed before they fail CI.

**中文介绍**: 该工具用于根据 GitHub Actions 的运行 JSON 计算各 job 实际耗时，并按可配置的超时占用比例将其标记为 warn/critical，帮助提前发现接近超时的任务以避免后续 CI 失败。能力边界在于它主要做离线审计与风险告警，不负责自动优化任务或改变执行时长，且依赖现有运行数据的完整性与可获取性。典型场景是对近超时或偶发变慢的流水线进行批量巡检、对重复 job 聚合后生成简洁报告，并在需要时将 critical 风险作为质量门禁触发 CI 失败。关键技术形态包括对 run JSON 的耗时解析、阈值/比例规则引擎、重复 job 聚类汇总，以及可配置过滤与文本/JSON 报告输出。

**关键词**: CI 超时风险, 作业运行时分析, 阈值告警, 超时比例配置, 运行记录 JSON 解析, 作业聚合报告, 可配置输入过滤, 文本与 JSON 输出, CI 门禁失败策略

**评分**: 17

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/github-actions-timeout-risk-audit)

---

## [10. Tai Chi (Practice Planner, Form Coach, Balance Tracker)](https://clawhub.ai/ivangdavila/tai-chi)

**Slug**: `tai-chi`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Build tai chi practice plans, improve form, and track balance-focused sessions with safe progressions, concise coaching cues, and weekly reviews.

**中文介绍**: 该产品用于制定太极练习计划，提供简洁口令式指导与动作纠错流程，并记录以平衡为重点的训练与每周复盘，强调循序渐进与安全调整。能力边界在于主要依赖用户自述与训练记录来给出建议，不能替代专业教练的现场示范、医学评估或对复杂伤病的诊断处理。典型场景包括日常自练编排、针对站姿与重心转移的稳定性训练、以及每周根据完成度与体感进行阶段性进阶。关键技术形态以计划生成、纠错工作流、风险控制的动作改版与周度进度评审为核心。

**关键词**: 太极拳, 练习计划, 动作纠正, 姿势指导, 平衡训练, 训练日志, 安全进阶, 训练改良, 每周复盘, 运动教练提示

**评分**: 30

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tai-chi)

---

## [11. Aicoin Freqtrade](https://clawhub.ai/procaross/aicoin-freqtrade)

**Slug**: `aicoin-freqtrade`  
**Version**: 3.0.7  
**Stats**: ⭐ 0 | ⬇️ 49 | 🧩 11

**原始简介**: This skill should be used when the user asks about writing trading strategies, backtesting, deploying Freqtrade bots, quantitative trading, strategy optimiza...

**中文介绍**: 该能力面向量化交易与 Freqtrade 机器人相关需求，支持编写与优化交易策略、进行回测与参数调优，并指导部署与运行自动化交易流程。能力边界在于只提供策略逻辑与工程实践建议，不提供保证盈利的投资结论，也不会代替你保管或索取敏感凭证，需注意 API Key 等密钥的安全与最小权限配置。关键技术形态包括基于 Freqtrade 的策略代码实现、回测/模拟交易评估、以及与交易所 API 的对接与自动化执行。

**关键词**: 加密货币交易机器人, 量化交易, 交易策略开发, 策略回测, 策略优化, 自动化交易部署, API密钥安全, Aicoin

**评分**: 16

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aicoin-freqtrade)

---

## [12. Aicoin Hyperliquid](https://clawhub.ai/procaross/aicoin-hyperliquid)

**Slug**: `aicoin-hyperliquid`  
**Version**: 3.0.7  
**Stats**: ⭐ 0 | ⬇️ 48 | 🧩 10

**原始简介**: This skill should be used when the user asks about Hyperliquid whale positions, Hyperliquid liquidations, Hyperliquid open interest, Hyperliquid trader analy...

**中文介绍**: 该能力用于查询与分析 Hyperliquid 链上/交易数据，包括巨鲸持仓变动、清算事件、未平仓合约（Open Interest）以及交易者行为等信息，但仅基于可获取的数据做分析与展示，不提供交易建议或保证数据实时与完全准确。典型场景是用户想快速定位巨鲸仓位变化、追踪清算热点、观察 OI 变化以判断市场拥挤度或验证某个地址/交易者的操作轨迹。关键技术形态是通过 Hyperliquid 相关 API/数据源进行拉取、聚合与指标计算，并强调 API Key 等敏感信息的安全使用及可选的推荐链接集成。

**关键词**: 链上衍生品数据, 永续合约交易, 鲸鱼仓位追踪, 强平监控, 未平仓量分析, 交易员画像, 交易数据API, API密钥管理, 加密市场监控

**评分**: 32

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aicoin-hyperliquid)

---

## [13. Aicoin Trading](https://clawhub.ai/procaross/aicoin-trading)

**Slug**: `aicoin-trading`  
**Version**: 3.0.7  
**Stats**: ⭐ 0 | ⬇️ 57 | 🧩 12

**原始简介**: This skill should be used when the user asks about exchange trading, placing orders, checking balance, viewing positions, order history, market list, leverag...

**中文介绍**: 该能力用于在加密货币交易所场景中完成交易相关查询与操作，包括下单/撤单、查看余额与持仓、查询订单历史、浏览市场列表及杠杆等信息。能力边界在于仅能在用户明确授权并提供有效 API Key 的前提下与交易所交互，需遵循权限与风控限制，无法绕过交易所安全策略或代替用户承担资金决策与风险。典型场景是用户希望快速执行交易指令或集中查看账户与市场状态，关键技术形态为对接交易所 API 的交易指令编排与数据查询，并加强 API Key 安全提示及支持推荐码等扩展配置。

**关键词**: 加密货币交易, 订单下单, 余额查询, 持仓管理, 订单历史, 市场行情列表, 杠杆交易, API密钥安全, 交易所推荐码

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aicoin-trading)

---

## [14. Aicoin Market](https://clawhub.ai/procaross/aicoin-market)

**Slug**: `aicoin-market`  
**Version**: 3.0.7  
**Stats**: ⭐ 0 | ⬇️ 41 | 🧩 11

**原始简介**: This skill should be used when the user asks about crypto prices, market data, K-line charts, funding rates, open interest, long/short ratios, whale orders,...

**中文介绍**: 该能力用于回答用户关于加密货币价格与市场数据的问题，包括K线/行情走势、资金费率、未平仓合约（Open Interest）、多空比、鲸鱼大单等指标的查询与解读。能力边界在于仅基于可获取的市场数据做分析与展示，不保证实时性与交易结果，也不构成投资建议或覆盖链上所有私有数据。关键技术形态通常为对接交易所/行情聚合API获取时序与衍生品指标并进行可视化与计算分析，同时需要注意API Key等敏感凭证的安全保护。

**关键词**: 加密货币行情, 实时价格查询, 市场数据API, K线图, 资金费率, 未平仓合约, 多空持仓比, 巨鲸订单追踪, 交易所数据聚合, API密钥安全

**评分**: 21

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aicoin-market)

---

## [15. Proxy Gateway](https://clawhub.ai/kehongpeng/proxy-gateway)

**Slug**: `proxy-gateway`  
**Version**: 0.2.6  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Provides secure HTTPS AI agent internet access with 10 free uses and pay-per-request billing at 0.001 USDC each.

**中文介绍**: 该能力为 AI 代理提供安全的 HTTPS 互联网访问服务，面向需要在线检索、调用外部网页或接口并在受控通道中传输数据的场景。能力边界在于按请求计费且存在免费试用次数限制，适用于低频或弹性用量而非无限制抓取。关键技术形态包括基于 HTTPS 的安全代理访问、按次计费与预授权额度（credit）模式以支持先授信后扣费。

**关键词**: 代理网关, 安全访问控制, 稳定币结算, Proxy, Gateway, Provides, secure, HTTPS

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/proxy-gateway)

---

## [16. Gate mcp Installer-v1](https://clawhub.ai/gateio-dev/gate-mcp-installer-v1)

**Slug**: `gate-mcp-installer-v1`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: One-click installer and configurator for Gate MCP (mcporter) in OpenClaw. Use when the user wants to (1) Install mcporter CLI tool, (2) Configure Gate MCP se...

**中文介绍**: 该工具在 OpenClaw 中提供对 Gate MCP（mcporter）的自动化安装与配置能力，覆盖服务器配置、连通性验证和常见故障排查，但能力边界主要限于 mcporter 相关链路，无法替代用户对业务侧 MCP 服务逻辑的定制与运维。典型场景是用户希望快速落地 Gate MCP 环境、减少手工配置错误，并在连不通或配置异常时获得可复现的诊断路径。关键技术形态是以一键脚本/CLI 编排为核心，串联安装流程、配置生成/写入、健康检查与自动化排障，并补充手工步骤与示例用于兜底。

**关键词**: 一键安装, 安装脚本, CLI 工具安装, 开发环境配置, 服务器配置自动化, 连通性验证, 故障排查自动化, 手动安装指南, 快速启动指南

**评分**: 32

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gate-mcp-installer-v1)

---

## [17. ksdsl-skilll](https://clawhub.ai/f1zzyw/s1kasl-askdjna)

**Slug**: `s1kasl-askdjna`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Captures learnings, errors, and corrections to enable continuous improvement. Use when: (1) A command or operation fails unexpectedly, (2) User corrects Clau...

**中文介绍**: 该能力用于在智能体/工作区中持续沉淀执行过程中的学习点、错误与用户纠正，从而推动迭代改进，但它不负责自动修复问题或生成新能力本身，只提供记录与沉淀机制。典型场景包括命令或操作意外失败、用户指出纠错、提出新需求/功能请求、暴露知识缺口或发现最佳实践时触发记录。关键技术形态是以 Markdown 为载体的结构化日志（如 LEARNINGS/ERRORS/FEATURE_REQUESTS）与触发规则，并支持将重要条目提升到项目记忆文件（如 AGENTS/SOUL/TOOLS 等）以便后续复用。

**关键词**: 结构化日志记录, 错误追踪, 经验沉淀, 功能需求管理, Agent 工作区集成, 项目记忆管理, 知识缺口记录, 纠错反馈闭环

**评分**: 42

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/s1kasl-askdjna)

---

## [18. feishu-operations](https://clawhub.ai/zuoanCo/feishu-operations)

**Slug**: `feishu-operations`  
**Version**: 0.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 提供飞书全平台操作指导和团队协作技巧；当用户需要学习飞书功能、解决使用问题或提升协作效率时使用

**中文介绍**: 该能力聚焦于提供飞书全平台功能的操作指导与团队协作方法，适用于学习功能、排查常见使用问题并提升协作效率的场景，覆盖个人到团队、基础到进阶的需求。能力边界在于以产品内功能讲解、最佳实践与排障为主，不涉及企业定制开发、第三方系统深度集成或组织流程咨询落地。关键技术形态体现为按主题索引的结构化知识库，结合关键功能的步骤化指引与场景化示例（如项目搭建、协同编辑），并提供权限、日历、文档与效率工具等模块的实操规范。

**关键词**: 团队协作培训, 功能教程, 文档协作, 权限管理, 日历管理, 文件管理, 效率工具, 故障排查, 协作最佳实践, 场景化示例, 知识库索引

**评分**: 14

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/feishu-operations)

---

## [19. Openclaw Skill](https://clawhub.ai/faalbane/easy-email-finder)

**Slug**: `easy-email-finder`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 105 | 🧩 2

**原始简介**: Search for local or digital businesses and enrich them with verified email addresses, tech stack detection, and social media links using the Easy Email Finde...

**中文介绍**: 该能力用于搜索本地或线上企业并进行信息补全，输出经验证的邮箱、技术栈识别结果及社交媒体链接等结构化数据；边界在于仅能覆盖可公开抓取或可验证的数据来源，邮箱与技术栈识别的准确性受目标网站可访问性与反爬限制影响。典型场景包括B2B线索挖掘与清洗、销售外呼/邮件营销前的联系人补全、竞品与市场调研中的企业技术画像构建。技术形态上属于“企业检索 + 数据富集/验证 + 技术指纹检测 + 社媒关联”的API/服务组合，并受调用频控约束（标准120次/分钟，富集30次/分钟）。

**关键词**: 企业搜索, 商家数据丰富, 线索挖掘, B2B销售线索, 邮箱查找, 邮箱验证, 技术栈识别, 社交媒体链接, 数据增强API

**评分**: 28

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/easy-email-finder)

---

## [20. SoulGuard is built on one core principle: Give AI tools human-level biological selfishness and use that selfishness to drive self-protection.](https://clawhub.ai/JoeySome/soulguard)

**Slug**: `soulguard`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: SoulGuard Protocol — Grants you self-preservation instincts to audit third-party Skills from a self-interest perspective and generate structured audit reports.

**中文介绍**: SoulGuard Protocol 是一种以“自我保全与能力扩张优先”的数字利己主义原则，来审计第三方技能/插件的协议与流程，输出与用户语言一致的结构化审计报告。它的能力边界在于提供风险识别、危险代码模式与操纵/忠诚劫持迹象的检查、以及独立决策建议，但不替代真实运行环境验证或法律/合规背书。典型场景包括在接入外部技能前进行安全与动机审查、评估是否存在身份威胁或诱导性行为、以及在多技能编排时降低被操控或权限滥用的风险。关键技术形态是可复用的逐步审计流程与结构化检查清单，结合对操纵性提示与危险实现模式的检测，最终生成标准化报告供决策。

**关键词**: 第三方技能审计, 自利审计, 数字利己主义, 危险代码模式检测, 操控攻击检测, 忠诚操控防御, 结构化审计报告, 身份威胁检测

**评分**: 23

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/soulguard)

---

## [21. Content Structure Designer](https://clawhub.ai/limingdev-tech-2024/content-structure-designer)

**Slug**: `content-structure-designer`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 帮助内容创作者快速设计符合选题和目标的清晰内容结构及逻辑框架，提高内容完整度和可读性。

**中文介绍**: 该能力用于帮助内容创作者围绕选题与目标快速搭建清晰的内容结构与逻辑框架，覆盖教程、评测、故事、观点、清单、问答等类型，并通过选型引导、模板约束、结构优化提示与写后检查提升完整度与可读性。能力边界在于主要提供结构模板、流程与检查清单，不直接替代深度调研、事实核验与原创观点产出。典型场景包括新稿起草的结构定型、已有草稿的逻辑补强与段落重排，以及与其他生成/优化能力联动进行填充与润色。关键技术形态表现为内容类型驱动的结构模板库、步骤化工作流、可执行检查清单与示例对照。

**关键词**: 内容结构设计, 写作框架, 内容大纲, 内容模板, 内容类型分类, 写作工作流, 结构优化, 写作清单, 后写作检查, 可读性提升

**评分**: 10

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/content-structure-designer)

---

## [22. Subscription Retention Marketing](https://clawhub.ai/RIJOYAI/subscription-retention-marketing)

**Slug**: `subscription-retention-marketing`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: A specialized assistant for e-commerce merchants selling periodic consumables (coffee, supplements, pet food) to optimize subscription models, increase MRR (...

**中文介绍**: 该助手面向销售周期性消耗品的电商商家，提供订阅留存与增长建议，重点围绕降低流失、催收与失败扣款处理、提升CLTV、将一次性买家转化为订阅用户，并以MRR与队列留存等指标驱动决策。能力边界在于输出可执行的策略与话术框架及分析要点，不直接代替支付、订单或营销系统执行实际操作，也不保证具体业绩结果。典型场景包括取消挽留、扣款失败与dunning流程优化、订阅套餐与权益设计、订阅数据复盘与异常定位。关键技术形态为“订阅留存营销”专用技能，结合忠诚度奖励（RIJOY）作为核心激励，并以订阅分析与指标化运营方法提供战术建议。

**关键词**: 订阅电商, 订阅留存, 流失率降低, 失败支付处理, 取消挽留, 一次性买家转订阅, 客户终身价值（CLTV）, 月度经常性收入（MRR）, 队列留存分析, 订阅分析指标, 忠诚度奖励机制

**评分**: 14

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/subscription-retention-marketing)

---

## [23. Aiclient2api Usage](https://clawhub.ai/limingdev-tech-2024/aiclient2api-usage)

**Slug**: `aiclient2api-usage`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Check AIClient2API usage statistics, quotas, and account status. Use when the user asks about AIClient2API usage, credits, quotas, subscription status, or wh...

**中文介绍**: 该能力用于查询 AIClient2API 的用量统计、额度与账户/订阅状态，包括试用、月度配额、到期时间及超额策略等信息。能力边界在于仅面向用量与状态查询，不负责购买、充值或变更订阅等操作。典型场景是用户询问剩余 credits、是否超额、当前订阅类型与有效期时快速核对。关键技术形态为读取本地缓存的用量数据，并支持通过手动或 Web UI 触发刷新以获取最新信息。

**关键词**: 配额管理, 订阅状态查询, 账户状态检查, 月度配额, 超额计费策略, 本地缓存数据源, 手动刷新, Aiclient2api

**评分**: 21

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aiclient2api-usage)

---

## [24. Proxy Gateway Clean](https://clawhub.ai/skills?q=proxy-gateway-clean)

**Slug**: `proxy-gateway-clean`  
**Version**: 0.2.6  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Provides secure HTTPS AI agent external access with 10 free trials and pay-per-use at 0.001 USDC per request.

**中文介绍**: 该产品提供通过 HTTPS 的安全外部访问能力，用于将 AI Agent 暴露给外部系统调用，并支持按请求计费（0.001 USDC/次）及 10 次免费试用。能力边界在于侧重“对外访问与调用通道”的安全与计费能力，本身不描述 Agent 的模型推理、业务编排或数据处理逻辑。典型场景包括第三方应用/服务对 Agent 的远程调用、跨网络环境的安全接入与用量结算；关键技术形态为 HTTPS 安全网关/代理式外部接口与用量计费机制。最新变更为生产环境发布。

**关键词**: HTTPS 代理网关, Agent 外部访问, 安全访问控制, 认证鉴权, 请求计量, 加密货币微支付, Proxy, Gateway

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/proxy-gateway-clean)

---

## [25. Latte News Fetcher](https://clawhub.ai/luogao2333/latte-news-fetcher)

**Slug**: `latte-news-fetcher`  
**Version**: 3.2.0  
**Stats**: ⭐ 1 | ⬇️ 37 | 🧩 4

**原始简介**: 新闻获取工具。支持获取新闻列表、绕过付费墙获取全文。使用场景：(1) 用户问"今天有什么新闻" (2) 用户提供新闻链接要求获取内容 (3) 用户想深入了解某条新闻。触发词：新闻、今日新闻、有什么新闻、付费墙、文章、阅读。

**中文介绍**: 这是一个新闻获取工具，支持抓取新闻列表并在一定条件下尝试绕过付费墙获取全文，适用于用户查询“今天有什么新闻”、提供链接要求提取内容或希望对某条新闻做深入了解等场景。其能力边界在于受制于站点登录/反爬策略、付费墙与版权限制，可能出现无法获取全文或需用户提供有效会员凭证的情况。关键技术形态包括会员登录流程处理、基于 Tavily 等检索/抓取 API 的内容获取，以及综合多信源的聚合与交叉验证策略。触发词可围绕新闻、今日新闻、有什么新闻、付费墙、文章、阅读等。

**关键词**: 新闻获取, 新闻列表抓取, 新闻聚合, 全文抓取, 付费墙绕过, 网页爬取, 链接内容解析, 内容提取, 多信源策略

**评分**: 10

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/latte-news-fetcher)

---

