# GitHub Trending 日榜 | 2026-03-13

> 共 11 个项目

## 📑 目录

- [C++](#Cplusplus) (1 个项目)
- [Python](#Python) (5 个项目)
- [Shell](#Shell) (2 个项目)
- [TypeScript](#TypeScript) (3 个项目)

---

## C++

## [1. google-ai-edge/LiteRT](https://github.com/google-ai-edge/LiteRT)

**语言**: C++  
**Stars**: ⭐ 0 (+13 today) | **Forks**: 🔱 221

**原始描述**: LiteRT, successor to TensorFlow Lite. is Google's On-device framework for high-performance ML & GenAI deployment on edge platforms, via efficient conversion, runtime, and optimization

**中文介绍（README总结）**: LiteRT 是 Google 面向端侧设备的高性能机器学习与生成式 AI 部署框架，继承 TensorFlow Lite，提供模型转换、运行时与优化能力以简化本地推理落地。它主要服务在手机、嵌入式与各类边缘硬件上做推理的开发者，强调跨平台与更易用的端侧推理开发体验。关键技术包括 GPU/NPU 加速与统一的 NPU 接入、自动加速器选择、异步执行以及高效 I/O 缓冲与零拷贝互操作，以降低延迟并提升吞吐。典型场景是将分类/检测等传统模型或端侧 GenAI 模型部署到具备 GPU/NPU 的设备上进行低时延离线推理。

**关键词**: 端侧推理运行时, 边缘部署, 统一加速器抽象, 自动加速器选择, 异步执行, 零拷贝缓冲区, I/O缓冲区管理, 模型转换, 推理优化, 跨平台构建

**评分**: 39

**项目地址**: [GitHub](https://github.com/google-ai-edge/LiteRT)

---

## Python

## [2. fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)

**语言**: Python  
**Stars**: ⭐ 0 (+637 today) | **Forks**: 🔱 2.2k

**原始描述**: SOTA Open Source TTS

**中文介绍（README总结）**: Fish Speech（Fish Audio S2）是开源文本转语音系统，面向需要高自然度、多语言语音合成的开发者与应用团队，可生成更真实且富有情感的语音。其核心技术包括 Dual-Autoregressive 架构与强化学习对齐，并支持用自然语言标签对韵律与情绪进行细粒度控制，同时具备原生多说话人和多轮生成能力。典型场景包括多语言配音、虚拟助手/客服语音、内容创作与有声读物等对表现力和可控性要求较高的语音生成任务。

**关键词**: 文本转语音（TTS）, 开源语音合成, 多语言语音生成, 多说话人合成, 韵律控制, 情感控制, 强化学习对齐, 双自回归架构, SGLang 服务端集成, 语音识别错误率（WER）

**评分**: 32

**项目地址**: [GitHub](https://github.com/fishaudio/fish-speech)

---

## [3. langflow-ai/openrag](https://github.com/langflow-ai/openrag)

**语言**: Python  
**Stars**: ⭐ 0 (+322 today) | **Forks**: 🔱 180

**原始描述**: OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and Opensearch.

**中文介绍（README总结）**: OpenRAG 是一个基于 Langflow、Docling 和 OpenSearch 的单包式检索增强生成（RAG）平台，用于把文档接入后通过聊天界面进行语义检索与基于大模型的问答对话。它面向需要企业级文档搜索与知识库问答的团队与应用开发者，提供从文档解析与摄取、检索流程编排到结果重排与多智能体协同的端到端能力。典型场景包括企业内部资料/政策/技术文档的智能搜索、客服与知识助手、以及可视化拖拽构建与迭代 RAG 工作流的应用开发。

**关键词**: RAG, 多智能体编排, 重排序, 语义搜索, 文档摄取, 知识库问答, 可视化工作流, langflow-ai

**评分**: 27

**项目地址**: [GitHub](https://github.com/langflow-ai/openrag)

---

## [4. vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)

**语言**: Python  
**Stars**: ⭐ 0 (+217 today) | **Forks**: 🔱 240

**原始描述**: Hindsight: Agent Memory That Learns

**中文介绍（README总结）**: Hindsight 是一个面向 AI Agent 的长期记忆系统，目标是让智能体随交互持续学习而不只是回忆对话历史，并宣称在 LongMemEval 等长期记忆任务上达到领先的准确率表现。它主要面向需要长期一致性与可学习记忆的企业与 AI 创业团队，可通过 LLM 包装器或 API/SDK 接入现有智能体，在调用模型时自动存取记忆或进行更细粒度控制。典型场景包括多轮客服与助理、企业内部知识与偏好记忆、以及需要跨会话保持上下文的对话式应用。

**关键词**: 智能体记忆, 长期记忆, 记忆学习, 持续学习, 记忆存储与召回, LLM 封装器, 知识图谱替代, vectorize-io

**评分**: 55

**项目地址**: [GitHub](https://github.com/vectorize-io/hindsight)

---

## [5. NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

**语言**: Python  
**Stars**: ⭐ 0 (+1.3k today) | **Forks**: 🔱 722

**原始描述**: The agent that grows with you

**中文介绍（README总结）**: Hermes Agent 是 Nous Research 开发的自我改进型 AI 代理，面向希望长期协作并跨设备使用智能助手的个人或团队，可在本地、VPS、GPU 集群或无服务器环境运行并通过 Telegram 等渠道交互。它的核心是内置学习闭环与记忆管理：从任务经验中自动生成与迭代技能、跨会话检索与总结历史对话并逐步建立用户模型，同时提供完整终端 TUI 交互与多子代理并行协作。项目支持对接多种大模型或自建端点便于自由切换，典型场景包括自然语言驱动的定时自动化（日报/备份/审计）、长周期研究与运维工作流，以及将多步骤管道脚本化并通过 RPC 调用工具来降低上下文成本。

**关键词**: 闭环学习, 技能自动生成, 长程记忆, 定时自动化, 多环境部署, NousResearch, hermes-agent, Agent

**评分**: 60

**项目地址**: [GitHub](https://github.com/NousResearch/hermes-agent)

---

## [6. 666ghj/MiroFish](https://github.com/666ghj/MiroFish)

**语言**: Python  
**Stars**: ⭐ 0 (+1.9k today) | **Forks**: 🔱 2.2k

**原始描述**: A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物

**中文介绍（README总结）**: MiroFish 是一款基于多智能体的群体智能预测与仿真引擎，通过从新闻、政策、金融信号或文本故事等“种子信息”中抽取要素，构建可交互的高保真平行数字世界，让大量具备人格、长期记忆与行为逻辑的智能体在其中演化并推演未来走向。它面向政策、公关、金融等需要低风险预演的决策者，也面向希望进行创意推演的个人用户。关键技术包括 GraphRAG/图谱构建、实体关系抽取、人设生成、时序记忆动态更新、自动解析预测需求与报告生成，并支持以“上帝视角”动态注入变量与深度对话交互。典型场景包含热点舆情事件推演、时政与金融趋势预测，以及小说结局/脑洞世界的仿真探索。

**关键词**: 多智能体系统, 群体智能, 数字孪生, 情景推演, 干预式仿真, 知识图谱构建, 实体关系抽取, 长期记忆, 自动报告生成

**评分**: 40

**项目地址**: [GitHub](https://github.com/666ghj/MiroFish)

---

## Shell

## [7. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+1.7k today) | **Forks**: 🔱 6.3k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: Superpowers 是一套面向编码智能体的“技能框架 + 软件开发方法论”工作流，让智能体先通过对话澄清需求并生成可读的规格说明，再在你确认设计后产出实现计划并按红/绿 TDD、YAGNI、DRY 等原则执行。它通过子智能体驱动的开发流程把任务拆分、实现、检查与复核串起来，支持在既定计划下较长时间的半/全自动推进。主要面向使用 Claude/Cursor/Codex/OpenCode 等编程助手的开发者，适用于从需求不清到落地实现的端到端工程开发场景。

**关键词**: 编码代理工作流, 代理技能框架, 可组合技能, 规格澄清, 设计评审, 实现计划生成, 子代理协作开发, 任务分解, IDE 插件集成

**评分**: 38

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

## [8. msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)

**语言**: Shell  
**Stars**: ⭐ 0 (+4.2k today) | **Forks**: 🔱 5.6k

**原始描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**中文介绍（README总结）**: 这是一个“AI Agency”式的多智能体集合，提供一组带人格设定与流程的专业 AI 代理（如前端工程、设计、营销/社媒社区运营、付费投放、销售、产品与项目管理等），目标是产出可交付的代码、流程与可衡量结果。它面向希望用现成角色与工作流提升效率的个人与团队，可作为参考直接复制改造，或接入 Claude Code 及其他代码/助手工具使用。关键特点在于领域专精的代理配置、可复用的工作流程与成功指标，典型场景包括快速组建虚拟跨职能团队来完成产品开发、内容与增长运营、广告与销售执行等任务。

**关键词**: 多智能体系统, 角色化智能体, 智能体人格设计, 专业分工, 工作流模板, 交付物导向, 成功指标, 多工具集成

**评分**: 13

**项目地址**: [GitHub](https://github.com/msitarzewski/agency-agents)

---

## TypeScript

## [9. InsForge/InsForge](https://github.com/InsForge/InsForge)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+263 today) | **Forks**: 🔱 330

**原始描述**: Give agents everything they need to ship fullstack apps. The backend built for agentic development.

**中文介绍（README总结）**: InsForge 是面向 AI 编码代理与 AI 代码编辑器的后端开发平台，通过可理解的语义层把数据库、鉴权、存储、函数等后端能力封装成代理可检索、可配置、可端到端操作的原语。它为代理提供后端上下文工程能力，支持获取可用操作与文档、直接配置后端组件，并以结构化 schema 暴露运行状态与日志便于检查与调试。核心能力覆盖 Postgres 数据库、用户与会话鉴权、S3 兼容存储、跨多 LLM 的 OpenAI 兼容模型网关、边缘无服务器函数与站点构建部署，典型用于让代理自动搭建与维护全栈应用后端并完成部署。

**关键词**: 智能体开发后端, 语义层, 上下文工程, 后端原语编排, S3 兼容对象存储, MCP 服务器集成, InsForge, Give

**评分**: 50

**项目地址**: [GitHub](https://github.com/InsForge/InsForge)

---

## [10. alibaba/page-agent](https://github.com/alibaba/page-agent)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+1.2k today) | **Forks**: 🔱 530

**原始描述**: JavaScript in-page GUI agent. Control web interfaces with natural language.

**中文介绍（README总结）**: PageAgent 是嵌入网页内的 JavaScript GUI 代理，让用户用自然语言在页面上操作 Web 界面与 DOM，实现类似“页面内 Copilot”的交互。它面向希望在自家产品中快速加入智能助理能力的 SaaS/企业应用开发者与终端用户，支持自带 LLM，并提供带人工介入的可视化 UI。关键技术是基于文本的 DOM 操作而非截图/多模态识别，默认单页内完成任务，亦可选用 Chrome 扩展支持跨标签页的多页面流程。典型场景包括表单/后台流程自动化、ERP/CRM 等多步点击简化、以及无障碍与语音指令式操作。

**关键词**: 自然语言界面控制, 文本式 DOM 操作, 无截图自动化, 可插拔 LLM, 人类在环交互, 多标签任务, 表单自动填充, Web 可访问性

**评分**: 37

**项目地址**: [GitHub](https://github.com/alibaba/page-agent)

---

## [11. google/A2UI](https://github.com/google/A2UI)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+225 today) | **Forks**: 🔱 970

**原始描述**: 

**中文介绍（README总结）**: A2UI 是一个开源的 Agent-to-User Interface 标准与库，让智能体用声明式 JSON 描述界面意图，由客户端用自身的原生组件库（如 Flutter、Angular、Lit 等）渲染，从而生成或填充可更新的富交互 UI。它面向需要让远程/跨信任边界的智能体安全输出界面的应用开发者与平台方，强调“像数据一样安全、像代码一样表达”，通过受信组件目录限制智能体只能调用预批准组件而非执行任意代码。典型场景包括对话式助手在业务系统中动态生成表单、卡片、按钮等交互界面，并支持增量更新 UI 以持续反映任务进展与用户输入。

**关键词**: 声明式 UI 规范, 跨端 UI 渲染, 客户端组件目录, 受信组件白名单, 跨信任边界, 增量 UI 更新, UI 意图表示, google

**评分**: 39

**项目地址**: [GitHub](https://github.com/google/A2UI)

---

