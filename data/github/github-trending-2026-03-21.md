# GitHub Trending 日榜 | 2026-03-21

> 共 7 个项目

## 📑 目录

- [Java](#Java) (2 个项目)
- [Python](#Python) (3 个项目)
- [Rust](#Rust) (1 个项目)
- [Shell](#Shell) (1 个项目)

---

## Java

## [1. opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf)

**语言**: Java  
**Stars**: ⭐ 0 (+1.8k today) | **Forks**: 🔱 518

**原始描述**: PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.

**中文介绍（README总结）**: OpenDataLoader PDF 是一个开源的 PDF 解析器，面向需要将 PDF 转成“可用于 AI/RAG 的结构化数据”的开发者与团队，可从 PDF 提取 Markdown、带坐标框的 JSON 以及 HTML，并支持本地确定性解析与结合 AI 的混合模式来处理复杂版面。它覆盖多栏文档、科学论文等场景，并在混合模式下支持扫描件 OCR（多语言）、复杂表格/公式以及图表描述生成。除此之外，它也将同一套版面分析能力用于 PDF 无障碍自动化（自动生成 Tagged PDF，计划推出），服务于需要规模化满足无障碍合规要求的内容生产与合规团队。

**关键词**: 文档版面分析, 结构化抽取, 表格识别, 公式识别, 边界框标注, RAG数据准备, PDF无障碍合规（PDF/UA）, opendataloader-project

**评分**: 40

**项目地址**: [GitHub](https://github.com/opendataloader-project/opendataloader-pdf)

---

## [2. openrocket/openrocket](https://github.com/openrocket/openrocket)

**语言**: Java  
**Stars**: ⭐ 0 (+144 today) | **Forks**: 🔱 589

**原始描述**: Model-rocketry aerodynamics and trajectory simulation software

**中文介绍（README总结）**: OpenRocket 是一款免费的模型火箭气动与轨迹仿真软件，面向模型火箭爱好者、学生与工程实践者，用于在制造与试飞前完成火箭结构设计、三维可视化与飞行性能评估。它提供六自由度飞行模拟、自动设计优化、实时高度/速度/加速度显示，并支持多级分离与发动机簇配置等典型火箭任务。常见场景包括对比不同尺寸与发动机组合的飞行结果、分析仿真曲线以改进设计，以及将设计/部件导出到其他仿真工具或用于 3D 打印、激光切割等制作流程。

**关键词**: 模型火箭仿真, 飞行轨迹模拟, 空气动力学建模, 六自由度仿真, 火箭设计工具, 自动设计优化, 多级分离仿真, 发动机推力曲线建模, 风场与大气模型, 三维可视化

**评分**: 24

**项目地址**: [GitHub](https://github.com/openrocket/openrocket)

---

## Python

## [3. langchain-ai/open-swe](https://github.com/langchain-ai/open-swe)

**语言**: Python  
**Stars**: ⭐ 0 (+635 today) | **Forks**: 🔱 931

**原始描述**: An Open-Source Asynchronous Coding Agent

**中文介绍（README总结）**: Open SWE 是一个开源的异步编码 Agent 框架，用来帮助组织构建面向内部工程师的编码助手（如 Slackbot、CLI 或 Web 应用），并与内部系统在权限与安全边界内协作以尽量减少人工介入。它基于 LangGraph 与 Deep Agents，提供可组合的子 Agent 编排、中间件与工具扩展能力，便于按自家代码库与工作流定制。核心技术包括每个任务在隔离的云端 Linux 沙箱中运行（克隆仓库、完整 shell 权限但隔离风险），并支持通过 Slack、Linear 等入口触发以及自动创建 PR 的典型开发流程场景。

**关键词**: An, Agent, langchain-ai, open-swe, Open-Source, Asynchronous, Coding, framework

**评分**: 47

**项目地址**: [GitHub](https://github.com/langchain-ai/open-swe)

---

## [4. newton-physics/newton](https://github.com/newton-physics/newton)

**语言**: Python  
**Stars**: ⭐ 0 (+266 today) | **Forks**: 🔱 363

**原始描述**: An open-source, GPU-accelerated physics simulation engine built upon NVIDIA Warp, specifically targeting roboticists and simulation researchers.

**中文介绍（README总结）**: Newton 是一个基于 NVIDIA Warp 的开源 GPU 加速物理仿真引擎，主要面向机器人开发者与仿真研究人员，用于构建可扩展的机器人与多物理场景仿真。它以 MuJoCo Warp 作为主要后端，强调 GPU 计算、可微分仿真、OpenUSD 支持以及用户自定义扩展能力，便于快速迭代与规模化实验。典型应用包括机器人与传感器仿真、接触与软体/布料/绳缆等物理效果、多物理耦合与逆运动学/可微仿真相关研究。

**关键词**: GPU物理仿真引擎, 机器人仿真, 可微分仿真, 多物理场仿真, 软体仿真, 接触与碰撞仿真, 逆运动学, 传感器仿真

**评分**: 44

**项目地址**: [GitHub](https://github.com/newton-physics/newton)

---

## [5. TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)

**语言**: Python  
**Stars**: ⭐ 0 (+433 today) | **Forks**: 🔱 6.6k

**原始描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**中文介绍（README总结）**: TradingAgents 是一个面向金融交易研究的多智能体 LLM 交易框架，模拟真实交易机构的分工协作，让基本面、情绪、技术分析、交易执行与风控等角色通过对话共同评估市场并给出交易决策。它主要服务研究者与量化/交易系统开发者，核心技术是基于多家大模型的多代理架构、角色分解与协同讨论机制，用于构建可扩展的市场分析与策略生成流程。典型场景包括研究不同分析模块如何组合影响策略、对同一市场数据进行多视角推理并输出交易建议与风险控制思路（并非投资建议）。

**关键词**: 多智能体系统, 量化交易框架, 金融市场分析, 交易决策, 代理协同决策, 风险管理, 基本面分析, 情绪分析, 技术分析

**评分**: 36

**项目地址**: [GitHub](https://github.com/TauricResearch/TradingAgents)

---

## Rust

## [6. louis-e/arnis](https://github.com/louis-e/arnis)

**语言**: Rust  
**Stars**: ⭐ 0 (+1.0k today) | **Forks**: 🔱 1.0k

**原始描述**: Generate any location from the real world in Minecraft with a high level of detail.

**中文介绍（README总结）**: Arnis 是一个开源工具，用于把真实世界任意地点高精度生成成 Minecraft 世界，支持 Java 版（1.17+）和基岩版。它面向想复刻家乡、城市或自然地貌的玩家与创作者，通过处理 OpenStreetMap 等地理要素数据和高程数据来还原地形起伏、道路与建筑布局，并支持大范围数据处理与多种生成参数定制。典型场景包括制作现实城市地图、地理教学演示、或在服务器中构建与现实对应的探索世界。

**关键词**: 真实地理重建, 程序化内容生成, 地理信息系统（GIS）, 数字高程模型（DEM）, 地形生成, 建筑生成, 体素世界生成, 大规模地理数据处理

**评分**: 29

**项目地址**: [GitHub](https://github.com/louis-e/arnis)

---

## Shell

## [7. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+2.8k today) | **Forks**: 🔱 8.2k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: Superpowers 是一套面向“编码代理/AI 编程助手”的技能框架与开发方法论，把从需求澄清、规格拆解、设计确认到实施计划与执行的工作流固化为可组合的自动触发“技能”。它先引导用户把真实目标聊成可审阅的规格并分段确认，再生成强调红绿 TDD、YAGNI、DRY 的实现计划，随后以子代理驱动的方式按任务推进、检查与复核，实现较长时间的半/全自动开发。适用于用 Claude、Cursor、Codex 等工具进行代理式软件开发、希望减少跑偏并提升交付一致性的场景。

**关键词**: 编码代理工作流, Agent 技能框架, 可组合技能, 需求澄清, 规格说明生成, 设计评审, 实现计划生成, 子代理编排, 任务分解, 自动化代码审查

**评分**: 43

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

