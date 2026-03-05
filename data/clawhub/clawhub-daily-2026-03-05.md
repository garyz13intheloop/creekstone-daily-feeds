# ClawHub Skills Daily | 2026-03-05

> 共 25 个 skills

## [1. Session Reset](https://clawhub.ai/traceless929/session-reset)

**Slug**: `session-reset`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 安全地重置 OpenClaw agent sessions，支持备份、预览、恢复和批量操作。用于：1) 清理过期的 agent 会话上下文，2) 重置特定 agents 的 session，3) 批量重置六部/秘书 sessions，4) 查看和恢复历史备份。当用户需要"reset session"、"清理 se...

**中文介绍**: 该能力用于安全重置 OpenClaw 的 agent 会话，支持自动备份与恢复，并提供预览（dry-run）、确认与强制执行等防误操作机制，但边界在于仅处理会话上下文与备份数据，不涉及 agent 逻辑本身或业务数据修复。典型场景包括清理过期会话、定向重置指定 agent、批量重置秘书/子 agent/定时任务相关 sessions，以及查看与回滚历史备份。关键技术形态为会话重置工作流（备份→预览/确认→执行→可恢复）、批处理与目标筛选、备份列表/恢复能力及按保留策略清理旧备份。

**关键词**: 批量操作, 自动备份, 备份恢复, 预览模式（dry-run）, 交互式初始化, 确认提示, 备份保留策略, 定时任务（cron）, 子代理（subagent）管理

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/session-reset)

---

## [2. Doc Scan](https://clawhub.ai/piyush-zinc/doc-scan)

**Slug**: `doc-scan`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Microsoft Lens-style document scanner. Converts photos of documents into clean, professional-looking scanned pages. Detects document edges automatically, app...

**中文介绍**: 该能力边界是将已有的纸质文件照片处理为更像扫描件的输出，包含自动识别是否为文档并给出拍摄引导，但不负责内容识别、编辑或复杂版式重建。典型场景包括移动端快速扫描合同/票据/讲义，批量多页归档并导出为 PNG/JPEG/PDF。关键技术形态涵盖文档边缘检测、透视校正与去畸变、对比度与清晰度增强、黑白/彩色/灰度滤镜，以及扫描前后质量评估与非文档图像判定。

**关键词**: 文档扫描, 移动端扫描, 边缘检测, 透视校正, 去畸变, 图像增强, 批量多页扫描, 扫描质量评估, 非文档图像检测, 黑白化处理

**评分**: 22

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/doc-scan)

---

## [3. Doc Process](https://clawhub.ai/piyush-zinc/doc-process)

**Slug**: `doc-process`  
**Version**: 2.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Multi-purpose document intelligence skill covering thirteen tasks. Document Categorizer - automatically classifies any uploaded document and routes to the co...

**中文介绍**: 这是一个多用途的文档智能能力集，覆盖 13 类任务，新增自动文档分类器可在用户意图不清时先识别文档类型并自动路由到合适处理模式，同时支持文档扫描美化，将照片/扫描件优化为更接近 PDF 的干净版效果。典型场景包括批量接收各类上传文件后的自动分流处理、降低交互成本的“先识别再处理”流程，以及在解析与审核时提供类型推断、关键数值告警和分级严重度提示。能力边界在于主要聚焦于文档类型识别与文档处理工作流编排及增强分析提示，不等同于通用业务决策或无约束的跨系统执行。

**关键词**: 文档智能, 文档自动分类, 意图识别, 模式路由, 文档类型推断, 文档工作流, 多任务处理, 文档扫描增强, 关键值告警, 严重等级划分, 提示词触发短语

**评分**: 41

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/doc-process)

---

## [4. Maxxit Lazy Trader](https://clawhub.ai/abhi152003/maxxit-lazy-trading)

**Slug**: `maxxit-lazy-trading`  
**Version**: 1.2.8  
**Stats**: ⭐ 2 | ⬇️ 1884 | 🧩 18

**原始简介**: Execute perpetual trades on Ostium, Aster, and Avantis via Maxxit's Lazy Trading API. Includes programmatic endpoints for opening/closing positions, managing...

**中文介绍**: Maxxit 的 Lazy Trading API 支持在 Ostium、Aster、Avantis 上程序化执行永续合约交易，提供开仓/平仓、仓位管理等核心接口，并新增了 Avantis DEX 的价格查询端点。能力边界在于仅覆盖上述 DEX 的永续交易与相关数据获取，不包含策略自动化、风控托管或跨平台统一结算等更高层能力。典型场景包括量化脚本/交易机器人对接、统一交易执行层封装以及对 Avantis 实时价格的行情拉取与下单前校验。关键技术形态为面向交易生命周期的 HTTP API 端点集合（执行类接口 + 行情/价格查询接口）。

**关键词**: 永续合约交易, 去中心化交易所集成, 程序化交易API, 交易机器人, 自动化下单, 开平仓接口, 头寸管理, 价格获取接口

**评分**: 23

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/maxxit-lazy-trading)

---

## [5. Katbot Trading](https://clawhub.ai/claytantor/katbot-trading)

**Slug**: `katbot-trading`  
**Version**: 0.2.8  
**Stats**: ⭐ 0 | ⬇️ 40 | 🧩 10

**原始简介**: Live crypto trading on Hyperliquid via Katbot.ai. Includes BMI market analysis, token selection, and AI-powered trade execution.

**中文介绍**: 该能力用于通过 Katbot.ai 在 Hyperliquid 上进行加密货币实盘交易，提供 BMI 市场分析、代币筛选，并由 AI 驱动完成下单与执行。能力边界在于仅覆盖 Hyperliquid 交易与相关策略分析/执行链路，不包含对其他交易所、资金托管或额外风控合规流程的扩展。典型场景是基于市场指标自动选币并触发交易，关键技术形态为指标分析模块 + 选币策略模块 + AI 交易执行接口的组合；本次更新仅提升版本号至 0.2.8，无功能变化。

**关键词**: 加密货币交易机器人, 实时自动化交易, 去中心化衍生品交易, 交易执行自动化, 代币筛选, BMI 市场分析, 量化交易策略, 加密资产风控

**评分**: 42

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/katbot-trading)

---

## [6. Ponddepth Levels](https://clawhub.ai/pureheart/ponddepth-levels)

**Slug**: `ponddepth-levels`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Leveling overlay for OpenClaw Control UI (badge + XP + daily tip + level list + icons).

**中文介绍**: 这是一个面向 OpenClaw Control UI 的等级进度叠加层，在界面中展示徽章、经验值、每日提示、等级列表与图标等可视化信息，用于增强用户的成长反馈与引导。能力边界在于仅负责前端/界面层的展示与交互，不定义或替代底层等级计算、数据存储与业务规则。典型场景包括在控制面板中实时呈现用户当前等级与奖励状态、通过每日提示提升使用黏性，以及在升级时提供清晰的等级路径预览。关键技术形态为 UI Overlay 组件化实现与资源化图标体系，并通过文档完善与卸载脚本支持更顺滑的集成与移除。

**关键词**: 等级系统, 游戏化激励, UI 叠加层, 徽章系统, 经验值（XP）, 每日提示, 等级列表, 图标集成, 安装卸载脚本, 插件扩展（Skill）

**评分**: 14

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ponddepth-levels)

---

## [7. Trading Knowledge](https://clawhub.ai/raphael2025/trading-knowledge)

**Slug**: `trading-knowledge`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Comprehensive trading and technical analysis knowledge. Covers K-line patterns, support/resistance, liquidity hunting, signal K, market maker behavior, funda...

**中文介绍**: 该能力提供较全面的交易与技术分析知识讲解，涵盖K线与形态、支撑阻力、市场结构、成交量与常见指标，并补充信号K、流动性狩猎、做市商行为、交易心理与术语词汇等内容。能力边界在于侧重概念与方法论解读，不直接生成可执行的交易指令或收益承诺，也不替代个股/品种的实时数据研判。典型场景包括新手入门学习、复盘时解释图表现象与关键位、统一团队对交易术语与分析框架的理解。关键技术形态以知识库式的结构化讲解为主，围绕图表模式识别、量价与结构分析、流动性与行为视角、基本面与技术面框架对比来组织内容。

**关键词**: 技术分析, K线形态, 图表形态, 支撑阻力, 流动性狩猎, 信号K线, 做市商行为, 成交量分析, 技术指标, 市场结构, 基本面分析, 交易心理

**评分**: 9

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/trading-knowledge)

---

## [8. Ta Analyzer](https://clawhub.ai/raphael2025/ta-analyzer)

**Slug**: `ta-analyzer`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Multi-timeframe technical analysis skill using CCXT. Calculates 20+ indicators including RSI, MACD, Bollinger Bands, Ichimoku, Stochastic, Williams %R, ADX,...

**中文介绍**: 该能力基于 CCXT 获取交易所（如 Binance）行情并进行多时间框架技术分析，输出指标数值、形态识别、交易信号与价格行为洞察，但不保证预测准确性且依赖数据源质量与所覆盖的币种/周期。典型场景包括量化/策略研究中的行情体检、自动生成盘面解读、筛选超买超卖与趋势强弱、识别支撑阻力与关键价位。关键技术形态是批量计算 20+ 技术指标（如 RSI、MACD、布林带、一目均衡、ADX 等）并结合 10+ K 线/结构形态检测、支撑阻力聚类、斐波那契回撤/枢轴点/VWAP 等价位体系进行综合判读。

**关键词**: 多周期技术分析, 加密货币行情分析, 技术指标计算, K线形态识别, 支撑阻力位聚类, 斐波那契回撤, 枢轴点, 交易信号生成, 价格行为分析

**评分**: 27

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ta-analyzer)

---

## [9. Bambu Studio Ai](https://clawhub.ai/heyixuan2/bambu-studio-ai)

**Slug**: `bambu-studio-ai`  
**Version**: 0.22.20  
**Stats**: ⭐ 2 | ⬇️ 407 | 🧩 87

**原始简介**: Bambu Lab 3D printer control and automation. Activate when user mentions: printer status, 3D printing, slice, analyze model, generate 3D, AMS filament, print...

**中文介绍**: 该能力用于 Bambu Lab 3D 打印机的控制与自动化，适合在用户关注打印状态、切片与模型分析、生成 3D、AMS 耗材与多色打印等场景下调用。能力边界在于主要围绕设备与打印流程的操作和信息联动，不负责通用的安装配置或与打印无关的内容。关键技术形态包括对打印任务/切片与模型处理的流程编排、对 AMS 线材与多色策略的管理，以及对打印状态的监控与触发式自动化；最新变更为 12 个色系完全独立，不再自动合并相近色，合并规则由用户自行决定。

**关键词**: 3D打印机控制, 打印自动化, 打印状态监控, 切片处理, 三维模型分析, 打印任务管理, 多材料打印, 耗材管理, 颜色分类管理, 第三方技能集成

**评分**: 46

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bambu-studio-ai)

---

## [10. ScholarGraph](https://clawhub.ai/Josephyb97/scholargraph)

**Slug**: `scholargraph`  
**Version**: 1.4.1  
**Stats**: ⭐ 0 | ⬇️ 492 | 🧩 6

**原始简介**: Academic literature intelligence toolkit for multi-source paper search, analysis, and knowledge graph building with AI assistance.

**中文介绍**: 这是一个面向学术文献的智能工具集，支持从多来源检索论文、辅助分析并构建知识图谱，以提升选题调研与知识整理效率。能力边界在于主要提供检索聚合、结构化抽取与图谱化组织等辅助能力，不包含本次版本（1.4.1）新增的用户可见功能或行为变化。典型场景包括跨数据库快速搜集相关工作、对论文要点与关系进行归纳、将文献与概念/作者/方法关联成可查询的知识图谱。关键技术形态通常由多源检索适配、AI 信息抽取与总结、图数据库/知识图谱建模与查询组件组成。

**关键词**: 学术文献检索, 多源论文搜索, 文献情报分析, 文献知识图谱, 引文网络分析, 论文元数据抽取, 科研助手工具, 文献数据聚合, 论文关系图谱构建

**评分**: 40

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/scholargraph)

---

## [11. 云梦A股数据获取Skill](https://clawhub.ai/Glory904649854/clouddream-a-data)

**Slug**: `clouddream-a-data`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 获取A股市场资金流向、新闻、筹码分布、龙虎榜及涨停板等多维度数据，支持单只股票详情查询。

**中文介绍**: 该 Skill 提供 A 股市场资金流向、新闻、筹码分布、龙虎榜、涨停板等多维度数据，并支持按单只股票进行详情查询与整合分析。能力边界在于仅覆盖所提供的数据维度与可查询范围，不保证实时性、完整性或对外部数据源不可用时的稳定输出，也不直接给出投资结论。典型场景包括个股画像、热点题材追踪、异动归因、资金与情绪监测以及盘前/盘后复盘。关键技术形态以结构化数据接口聚合与查询为主，输出面向分析的字段化结果并可与其他策略/分析模块组合使用。

**关键词**: A股数据, 股票数据接口, 资金流向, 财经新闻抓取, 筹码分布, 龙虎榜, 涨停板, 个股详情查询, 金融数据采集

**评分**: 24

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/clouddream-a-data)

---

## [12. openclaw-android](https://clawhub.ai/ssrlxl123/openclaw-android)

**Slug**: `openclaw-android`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 通过openclaw控制android手机，所有命令在手机内部执行，先su切换到root权限后执行后续命令，支持获取安装软件列表、打开和关闭app、操作app（点击、滑动、输入文本）以及截图app。当用户需要控制android设备或执行app操作时调用。

**中文介绍**: openclaw-android 通过 openclaw 在 Android 手机内执行命令，先 su 切换到 root 权限后完成应用管理与交互操作。能力覆盖获取已安装应用列表、打开/关闭应用、对应用进行点击/滑动/文本输入以及截图，用于自动化控制、远程运维与应用管理等场景。其关键技术形态是基于设备端 root 命令的执行链路与 UI 事件注入/截图能力，边界在于必须具备 root 权限且主要面向设备内指令执行而非无 root 的系统级控制。

**关键词**: su 提权, 设备内命令执行, 自动化控制, UI 自动化, 触控操作, 文本输入, 屏幕截图, openclaw-android

**评分**: 33

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openclaw-android)

---

## [13. soushen](https://clawhub.ai/hexian2001/soushen)

**Slug**: `soushen`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 高性能 Bing 搜索引擎 Skill - "搜神猎手" 使用 Playwright 底层 API 进行深度网页搜索和元素提取 功能： 1. Bing 搜索执行 - 返回结构化搜索结果（标题、链接、摘要、来源） 2. 深度页面分析 - 提取页面的所有关键元素（链接、表单、按钮、脚本、元数据） 触发条件： - 用户...

**中文介绍**: “搜神猎手”是基于 Playwright 底层能力的高性能 Bing 搜索与深度网页解析工具，可返回结构化搜索结果并自动过滤广告，同时对指定页面进行全量关键元素提取（链接、表单、按钮、脚本、元数据等）。它适用于信息检索聚合、竞品/舆情搜集、线索发现与页面结构审计等需要“先搜再抓取解析”的场景，但能力边界在于依赖浏览器自动化与目标站点可访问性，遇到强反爬、登录/验证码或内容受限时可能无法稳定获取。关键技术形态上采用 Playwright 驱动真实浏览器执行搜索与 DOM 抽取，并通过去自动化标识、仿真 UA 与行为随机化等手段降低被检测风险，支持中英文查询并提供 CLI 与 Python API 调用方式。

**关键词**: Bing 搜索自动化, 深度网页抓取, 广告过滤, 网页元素提取, 元数据提取, 反爬虫规避, 浏览器自动化, soushen

**评分**: 32

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/soushen)

---

## [14. OpenClaw Guide](https://clawhub.ai/Linux2010/openclaw-guide)

**Slug**: `openclaw-guide`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Authoritative OpenClaw guidance and documentation lookup. Provides accurate information about OpenClaw capabilities, configuration, and usage based on offici...

**中文介绍**: 该能力用于权威检索与解读 OpenClaw 的官方文档与源码，回答其功能能力、配置与使用方式，并以官方信息为优先依据。典型场景包括功能与架构咨询、安装/配置排错、最佳实践与版本变更理解等。能力边界在于仅对 OpenClaw 相关内容提供基于可检索官方来源的解释与建议，不替代实际环境验证或超出文档/源码范围的推断。关键技术形态是“问题分析→检索文档/源码→归纳与引用→输出清晰答复”的检索增强式问答流程，并配套质量标准与响应模板以保证准确性与可追溯性。

**关键词**: 文档问答, 官方文档优先, 源码检索, 知识检索工作流, 配置指南, 功能查询, 架构解析, 故障排查, 最佳实践

**评分**: 15

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openclaw-guide)

---

## [15. Monte Carlo Crypto Core](https://clawhub.ai/totoxu/totoxu-montecarlo)

**Slug**: `totoxu-montecarlo`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Monte Carlo Crypto Trading Core. Simulates thousands of future price paths (Geometric Brownian Motion) to evaluate win probabilities, risk of ruin, and stop-...

**中文介绍**: 该核心用于加密交易策略的风险评估：基于几何布朗运动生成成千上万条未来价格路径，计算胜率、破产风险以及止损/止盈对结果的影响，并输出风险指标与分位数用于决策。能力边界在于它是统计模拟而非行情预测，结论高度依赖输入的价格、波动率、漂移、周期、路径数、仓位与止损止盈等参数且不保证盈利。典型场景是交易前对不同仓位与风控参数做压力测试和概率分析；关键技术形态为蒙特卡洛路径模拟+风险度量输出，并通过认证与计费系统（SkillPay）按次调用。

**关键词**: 加密货币交易, 蒙特卡洛模拟, 价格路径模拟, 几何布朗运动, 交易策略风险评估, 胜率评估, 破产风险, 止损策略, 止盈策略, 风险指标分位数

**评分**: 31

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/totoxu-montecarlo)

---

## [16. Self-Improving Agent (With Self-Reflection)](https://clawhub.ai/ivangdavila/self-improving)

**Slug**: `self-improving`  
**Version**: 1.2.6  
**Stats**: ⭐ 39 | ⬇️ 14549 | 🧩 12

**原始简介**: Self-reflection + Self-criticism + Self-learning + Self-organizing memory. Agent evaluates its own work, catches mistakes, and improves permanently. Use befo...

**中文介绍**: 这是一个具备自我反思、自我批判、自我学习与自组织记忆的智能体机制，能够在任务前复盘要求、在输出后回看并记录改进点，从而持续提升后续表现。典型场景包括长周期写作/代码交付、质量审校、复杂任务分解与多轮对话服务中对错误的捕获与纠偏。其关键技术形态是“任务前检查清单 + 结果后反思日志 + 可累积的结构化记忆（如 SOUL.md）”的闭环；能力边界在于改进依赖可观测反馈与可写入的记忆载体，无法保证在缺乏评估信号或权限受限时实现稳定的永久提升。

**关键词**: 持续学习, 自组织记忆, 长期记忆, 任务前审查, 回答后复盘, 错误检测, Agent, Self-Improving

**评分**: 26

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/self-improving)

---

## [17. autonomous-tasks](https://clawhub.ai/changye01/autonomous-tasks)

**Slug**: `autonomous-tasks`  
**Version**: 10.2.3  
**Stats**: ⭐ 0 | ⬇️ 201 | 🧩 33

**原始简介**: Self-driven AI worker. Reads goals, generates tasks, executes, and logs progress. Keywords: create goal, new goal, set goal, run goals, 创建目标, 新目标, 设定目标, 执行目标.

**中文介绍**: 这是一个自驱式 AI Worker：接收用户设定的目标后自动拆解为任务并执行，同时持续记录进度与结果日志。能力边界在于它围绕“目标→任务→执行→日志”的闭环工作，不替代人工决策与目标定义本身，且执行效果受所接入的工具/权限与运行环境限制。典型场景包括周期性目标推进、流程自动化与长任务跟踪复盘。关键技术形态是目标管理与任务编排引擎结合自动执行器与日志/状态追踪，并建议首次配置完成后通过定时调度提升稳定性与持续运行能力。

**关键词**: 目标驱动执行, 任务规划, 任务生成, 任务调度, 工作流自动化, 进度日志, 长任务运行, 命令行工具

**评分**: 42

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/autonomous-tasks)

---

## [18. Smart Butler](https://clawhub.ai/sukimgit/smart-butler)

**Slug**: `smart-butler`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 15 | 🧩 2

**原始简介**: AI 智能管家 - 会议管理、文档生成、任务提醒、智能推荐一站式解决方案。

**中文介绍**: AI 智能管家提供会议管理、文档生成、任务提醒与智能推荐的一站式能力，适用于会前安排、会中纪要整理、会后任务分发与日常信息辅助决策等办公协同场景。其能力边界在于主要处理结构化流程与文本类内容生成/整理，对外部系统数据的准确性、实时性及支付/权限等敏感操作依赖后端接入与安全策略，不能替代人工审核与最终决策。关键技术形态通常包括大模型对话与摘要生成、RAG/知识库检索增强、工作流编排与日程/任务系统集成，以及基于用户行为与上下文的推荐引擎。

**关键词**: 智能管家, 日程管理, 文档生成, 任务提醒, 智能推荐, 工作流自动化, 个人助理, 插件技能, 支付信息安全

**评分**: 17

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smart-butler)

---

## [19. Token Unlock Pro](https://clawhub.ai/mrchillhigh/token-unlock-pro)

**Slug**: `token-unlock-pro`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 专业的代币解锁预警系统 - 支持72h/48h/24h/6h/实时多维度预警，类型分类（种子轮/公募/生态/质押），解锁额度分级，用户自定义监控，解锁日历月/周/日视图，历史数据分析及走势预测。每次调用需支付0.001 USDT。

**中文介绍**: 该系统面向代币解锁事件提供72h/48h/24h/6h及实时预警，覆盖种子轮、公募、生态、质押等类型并按解锁额度分层展示，支持自定义监控、导入钱包持仓与订阅热门项目，并提供月/周/日解锁日历与历史数据分析和走势/相关性预测。其能力边界在于以解锁数据与持仓监控为核心，提供预警与分析参考而非交易执行或收益保证。关键技术形态为可计费API（每次调用0.001 USDT）叠加事件驱动预警、分类与额度分级规则引擎、日历视图聚合以及基于历史数据的预测模型。典型场景包括做市/交易风控提前规避集中解锁、项目方与社区运营进行解锁节奏沟通、研究员对解锁对价格与流动性的影响进行回测与跟踪。

**关键词**: 代币解锁预警, 实时通知, 多时间窗预警, 解锁类型分类, 解锁额度分级, 鲸鱼级监控, 自定义监控, 钱包持仓导入, 项目订阅, 解锁日历, 历史数据分析

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/token-unlock-pro)

---

## [20. Zeelin US-Iran War Situation Tracker](https://clawhub.ai/wlkqyang-star/zeelin-us-iran-war-tracker)

**Slug**: `zeelin-us-iran-war-tracker`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: A specialized skill for tracking the US-Iran conflict, strictly focusing on intelligence published within the **last 6 hours**. Use this for hyper-current, t...

**中文介绍**: 这是一个用于追踪美伊冲突的专用情报分析能力，严格限定只使用过去 6 小时内发布的可信情报，能力边界在于无法覆盖更早信息且在可核验情报不足时只能明确记录情报缺口并补充背景脉络。典型场景是需要“超实时”态势更新、事件演进追踪与快速研判的用户报告输出。关键技术形态体现为时间窗约束的信息检索与验证、缺口披露机制，以及以深度与完整性为硬性标准的长篇（至少 1000 字）报告生成。

**关键词**: 美伊冲突跟踪, 冲突态势监测, 实时情报聚合, 6小时滚动更新, 开源情报（OSINT）, 情报可信度验证, 情报缺口分析, 背景态势综述, 事件时间线整理

**评分**: 15

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zeelin-us-iran-war-tracker)

---

## [21. SOUL Backup Skill](https://clawhub.ai/X-RayLuan/soul-backup-skill)

**Slug**: `soul-backup-skill`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Backup and restore OpenClaw workspace SOUL files with versioning, validation, and sanitized openclaw.json handling.

**中文介绍**: 该能力用于对 OpenClaw 工作区的 SOUL 文件进行备份与恢复，并提供版本管理与内容校验，确保回滚与恢复过程可追溯且一致。其边界在于聚焦工作区级文件与配置处理，不涉及运行时执行、环境部署或外部存储策略。典型场景包括发布前快照、误改/损坏后的快速回滚、跨分支或跨团队的配置同步。关键技术形态是基于版本化备份链、恢复前后校验机制，以及对 openclaw.json 的清洗/脱敏与结构化读写处理，并配套测试与示例保障可用性。

**关键词**: 工作区备份, 备份恢复, 版本管理, 文件校验, 自动化脚本, 开发文档, SOUL, Backup

**评分**: 25

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/soul-backup-skill)

---

## [22. Email Monitor](https://clawhub.ai/sukimgit/email-monitor)

**Slug**: `email-monitor`  
**Version**: 1.0.7  
**Stats**: ⭐ 0 | ⬇️ 53 | 🧩 6

**原始简介**: 邮件自动监控系统，自动回复客户咨询，过滤垃圾邮件，商机邮件飞书通知。

**中文介绍**: 该邮件自动监控系统可持续监听收件箱，对客户咨询进行自动化回复并对垃圾邮件进行识别过滤，同时将疑似商机邮件通过飞书消息触达相关人员以便及时跟进。能力边界在于自动回复与分类依赖既定规则或模型判断，复杂多轮沟通、强业务定制流程及误判纠正仍需人工介入与审核。典型场景包括客服咨询分流、线索捕获与通知、日常反垃圾与收件箱降噪。关键技术形态通常由邮件协议接入与事件监听、NLP/规则引擎的意图识别与分类、自动回复模板与上下文管理、以及飞书机器人/Webhook 通知链路组成。

**关键词**: 邮件监控, 邮件自动化, 自动回复, 客服邮件, 垃圾邮件过滤, 商机识别, 销售线索, 飞书集成, 消息通知, 支付信息保护

**评分**: 32

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/email-monitor)

---

## [23. Weekly Digest](https://clawhub.ai/sukimgit/weekly-digest)

**Slug**: `weekly-digest`  
**Version**: 1.0.7  
**Stats**: ⭐ 0 | ⬇️ 65 | 🧩 6

**原始简介**: 自动生成周报（GitHub + Notion + 新闻），支持飞书/邮件发送。

**中文介绍**: 该能力用于汇总 GitHub 动态、Notion 内容与新闻资讯，自动生成周报并通过飞书或邮件分发，适合团队研发周报、项目进展同步与信息快照。能力边界在于依赖第三方数据源的可访问性与权限，生成内容为自动整理与摘要，可能需要人工复核以避免遗漏或理解偏差。关键技术形态主要是多源数据接入与抓取/订阅、内容抽取与去重、摘要生成与结构化排版，以及与飞书/邮件的消息推送集成；最新变更为修复支付信息相关的安全问题。

**关键词**: 周报生成, 自动化汇总, 新闻聚合, 内容摘要, 飞书推送, 邮件发送, 定时任务, 信息同步

**评分**: 18

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/weekly-digest)

---

## [24. Token Analyzer](https://clawhub.ai/hanguang254/token-analyzer)

**Slug**: `token-analyzer`  
**Version**: 2.2.2  
**Stats**: ⭐ 0 | ⬇️ 99 | 🧩 10

**原始简介**: 基于官方 GMGN API 的代币分析工具。通过合约地址查询代币在 SOL/BSC/Base 链上的准确市场数据、安全检测、KOL 分析、开发者分析和 AI 评分。

**中文介绍**: 该工具基于官方 GMGN API，通过合约地址查询 SOL/BSC/Base 链上代币的准确市场数据，并提供安全检测、KOL 分析、开发者画像与 AI 评分等综合研判能力。能力边界在于其结果依赖 GMGN 数据覆盖与实时性，无法替代链上全量审计或对缺失/异常字段（如 PNL 为空）之外的信息做保证。典型场景包括新币快速尽调、风险初筛、KOL 影响评估与开发者可信度评估，关键技术形态为多链数据聚合接口调用 + 风险规则/模型分析 + 评分输出。最新变更修复了 PNL 为 None 时的格式化错误。

**关键词**: 代币分析, 合约地址查询, 链上市场数据, 安全检测, 开发者分析, AI 评分, Token, Analyzer

**评分**: 16

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/token-analyzer)

---

## [25. Openclaw Framework](https://clawhub.ai/qianzhaoaiyin/openclaw-framework)

**Slug**: `openclaw-framework`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Openclaw Framework is an AI assistant framework emphasizing structured communication, data-driven decisions, layered memory, automation, and continual self-i...

**中文介绍**: OpenClaw Framework 是面向 AI 助手的框架，强调结构化沟通与数据驱动决策，适用于需要复杂任务拆解、长期目标推进与自动化维护的智能助理场景。其能力边界在于依赖预先定义的方法论与记忆管理机制进行自我迭代，无法替代外部系统能力或超出安全原则处理敏感数据与高风险操作。关键技术形态包括三层记忆体系（工作/短期/长期）、周期性心跳与日/周记忆维护流程、七步深度使用方法，以及面向成本控制的上下文管理与安全治理规范。

**关键词**: 智能体框架, 结构化沟通, 三层记忆, 记忆管理, 心跳维护, 自动化工作流, 公式优先推理, 成本敏感上下文, 安全治理

**评分**: 42

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openclaw-framework)

---

