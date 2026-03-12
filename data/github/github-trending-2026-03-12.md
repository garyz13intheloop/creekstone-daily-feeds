# GitHub Trending 日榜 | 2026-03-12

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
**Stars**: ⭐ 0 (+6 today) | **Forks**: 🔱 206

**原始描述**: LiteRT, successor to TensorFlow Lite. is Google's On-device framework for high-performance ML & GenAI deployment on edge platforms, via efficient conversion, runtime, and optimization

**中文介绍（README总结）**: LiteRT 是 Google 的端侧机器学习/生成式 AI 部署框架，作为 TensorFlow Lite 的继任者，提供从模型高效转换到运行时执行与优化的一体化能力。它面向需要在手机、嵌入式等边缘平台进行本地推理的开发者，重点通过 GPU/NPU 加速提升性能与降低延迟。关键技术包括编译模型 API（自动选择加速器、异步执行与高效 I/O 缓冲）、统一的 NPU 访问层以及 GPU 零拷贝缓冲互操作。典型场景是将分类、检测等传统 ML 和各类 GenAI 模型以高性能方式集成到端侧应用中。

**关键词**: 端侧推理运行时, 边缘计算部署, 模型转换, 模型优化, 统一加速器抽象, 编译模型 API, 异步执行, 零拷贝缓冲区, 生成式模型推理

**评分**: 26

**项目地址**: [GitHub](https://github.com/google-ai-edge/LiteRT)

---

## Python

## [2. fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)

**语言**: Python  
**Stars**: ⭐ 0 (+313 today) | **Forks**: 🔱 2.2k

**原始描述**: SOTA Open Source TTS

**中文介绍（README总结）**: Fish Speech（Fish Audio S2）是一个开源文本转语音（TTS）项目，面向需要高自然度、多语言语音合成的开发者与应用团队。其模型据称以超大规模多语言语音数据训练，结合强化学习对齐与双自回归架构生成更真实、情感更丰富的语音，并支持用自然语言标签细粒度控制韵律与情绪。典型场景包括多语言配音、对话式语音生成、以及多说话人/多轮语音内容生产与服务化部署。

**关键词**: 文本转语音（TTS）, 开源语音合成, 多语言语音合成, 多说话人生成, 韵律控制, 情感控制, 双自回归架构, 强化学习对齐, 推理服务（Server）

**评分**: 32

**项目地址**: [GitHub](https://github.com/fishaudio/fish-speech)

---

## [3. langflow-ai/openrag](https://github.com/langflow-ai/openrag)

**语言**: Python  
**Stars**: ⭐ 0 (+191 today) | **Forks**: 🔱 100

**原始描述**: OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and Opensearch.

**中文介绍（README总结）**: OpenRAG 是一个打包成单一组件的 RAG（检索增强生成）平台，面向需要把文档变成可搜索知识库并进行 AI 对话的团队与应用开发者。用户可上传与处理真实世界的“脏数据”文档，在聊天界面中通过语义检索+大模型获得答案，并支持智能体驱动的编排流程（如重排与多智能体协作）。它基于 Langflow 做摄取与可视化工作流，结合 Docling 文档解析与 OpenSearch 生产级检索，适用于企业文档搜索、内部知识问答与规模化检索场景。

**关键词**: RAG, 智能体检索, 多智能体编排, 重排序, 语义检索, 文档摄取, 文档解析, 聊天式问答, 可视化工作流

**评分**: 35

**项目地址**: [GitHub](https://github.com/langflow-ai/openrag)

---

## [4. vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)

**语言**: Python  
**Stars**: ⭐ 0 (+95 today) | **Forks**: 🔱 213

**原始描述**: Hindsight: Agent Memory That Learns

**中文介绍（README总结）**: Hindsight 是一种让 AI Agent 随时间“学会”的长期记忆系统，目标不只是回忆对话历史，而是通过记忆机制提升智能体在后续任务中的表现。它面向需要稳定长期记忆能力的对话式 AI、企业级智能体与 AI 初创产品，可通过 LLM Wrapper 或 API/SDK 接入并自动完成记忆的存取。项目强调相较 RAG、知识图谱等方案在长期记忆任务上更优，并在 LongMemEval 基准上报告了领先的准确率表现。典型场景包括需要跨多轮、多天交互持续累积用户偏好、上下文与经验的客服、助理与业务流程自动化智能体。

**关键词**: 智能体记忆, 长期记忆, 记忆学习, 记忆存储与检索, 知识图谱替代, vectorize-io, hindsight, Agent

**评分**: 60

**项目地址**: [GitHub](https://github.com/vectorize-io/hindsight)

---

## [5. NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

**语言**: Python  
**Stars**: ⭐ 0 (+1.2k today) | **Forks**: 🔱 654

**原始描述**: The agent that grows with you

**中文介绍（README总结）**: Hermes Agent 是 Nous Research 推出的自我改进型 AI Agent，面向希望长期使用、跨设备协作的个人用户与开发者，在多次会话中积累记忆与用户画像并从经验中生成/优化技能。它提供内置学习闭环（记忆管理与定期巩固、跨会话搜索与总结、技能自生成与自优化）以及可并行的子代理与基于 RPC 的工具调用来压缩多步骤流程。项目支持接入多种大模型与自有端点、可在本地/容器/SSH/Serverless 等多种后端运行，并提供终端 TUI 交互与 cron 式自然语言定时自动化，适用于持续助理、周期性报告/备份/审计与并行研究/工程任务等场景。

**关键词**: 闭环学习, 技能自动生成, 长期记忆管理, 终端TUI界面, 计划任务自动化, 无服务器持久化, NousResearch, hermes-agent

**评分**: 59

**项目地址**: [GitHub](https://github.com/NousResearch/hermes-agent)

---

## [6. 666ghj/MiroFish](https://github.com/666ghj/MiroFish)

**语言**: Python  
**Stars**: ⭐ 0 (+2.9k today) | **Forks**: 🔱 1.9k

**原始描述**: A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物

**中文介绍（README总结）**: MiroFish 是基于多智能体与群体智能的通用预测/仿真引擎，用户上传“种子”材料（新闻、政策草案、金融信号、报告或故事）并用自然语言提出预测需求，系统会自动构建高保真的平行数字世界并输出预测报告与可交互的沙盘。它面向决策者与个人创作者等需要“预演未来”的人群，核心技术包括个体/群体记忆注入、知识图谱与 GraphRAG 构建、实体关系抽取、人设生成与时序记忆动态更新，以及基于 Agent 的报告生成与交互。典型场景包括舆情推演、时政与金融走势模拟、政策/公关零风险试错，以及小说情节或结局推演等创意仿真。

**关键词**: 多智能体系统, 群体智能, 智能体仿真, 数字孪生沙盘, 情景推演, 因果干预（what-if）, 知识图谱构建, 实体关系抽取, 自动化预测报告生成

**评分**: 35

**项目地址**: [GitHub](https://github.com/666ghj/MiroFish)

---

## Shell

## [7. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+1.5k today) | **Forks**: 🔱 6.1k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: Superpowers 是一套面向编码智能体的“技能框架 + 软件开发方法论”工作流，目的是让智能体先澄清需求并产出可阅读的规格与设计，再生成实现计划并按计划推进编码。它主要面向使用 Claude/Cursor/Codex 等 coding agent 的开发者或团队，关键在于可组合技能的自动触发、子智能体驱动的任务拆解与审查流程，并强调红/绿 TDD、YAGNI 与 DRY。典型场景是用智能体从零到一或在现有项目中实现功能时，减少直接写代码的偏航，提升规划、执行与质量控制的一致性。

**关键词**: 编码代理工作流, Agent 技能框架, 可组合技能, 需求澄清, 规格说明生成, 设计评审, 实现计划生成, 子代理协作, 测试驱动开发（TDD）, 开发原则（YAGNI/DRY）, IDE/代理插件集成

**评分**: 44

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

## [8. msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)

**语言**: Shell  
**Stars**: ⭐ 0 (+6.2k today) | **Forks**: 🔱 5.0k

**原始描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**中文介绍（README总结）**: 这是一个“AI 代理机构”式的项目，提供一组精心设计的 AI Agent 人格与工作流程模板，让它们以不同角色（如前端工程、设计、营销、社区运营等）协作产出可交付成果。面向希望把产品研发、增长与运营流程标准化并交给多角色 AI 协作的个人与团队。关键在于为每个 Agent 定义专长领域、沟通风格、可复用流程、产出物与成功指标，并可在 Claude Code 等多种开发/对话工具中调用或作为参考改造。典型场景包括组建“虚拟跨职能团队”完成代码实现、设计方案、投放/销售文案与社区运营策略等端到端工作流。

**关键词**: 多智能体代理, 代理人格模板, 虚拟团队协作, 工作流编排, 交付物驱动, 代码生成工作流, 多工具集成, msitarzewski

**评分**: 13

**项目地址**: [GitHub](https://github.com/msitarzewski/agency-agents)

---

## TypeScript

## [9. InsForge/InsForge](https://github.com/InsForge/InsForge)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+260 today) | **Forks**: 🔱 299

**原始描述**: Give agents everything they need to ship fullstack apps. The backend built for agentic development.

**中文介绍（README总结）**: InsForge 是面向 AI 编码代理与 AI 代码编辑器的后端开发平台，通过语义层把数据库、鉴权、存储、函数等后端原语以可理解、可推理、可端到端操作的方式暴露给代理。它提供后端上下文工程能力，让代理能获取可用操作与文档、直接配置后端组件，并用结构化 schema 检查状态与日志。核心能力覆盖鉴权与会话、Postgres 数据库、S3 兼容对象存储、兼容 OpenAI 的多模型网关、边缘函数以及站点构建与部署，适用于让代理自动搭建与维护全栈应用后端的场景。

**关键词**: 智能体开发后端, 语义层, 后端上下文工程, 后端原语编排, S3 兼容对象存储, 边缘函数, OpenAI 兼容模型网关, 一键部署

**评分**: 51

**项目地址**: [GitHub](https://github.com/InsForge/InsForge)

---

## [10. alibaba/page-agent](https://github.com/alibaba/page-agent)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+1.2k today) | **Forks**: 🔱 420

**原始描述**: JavaScript in-page GUI agent. Control web interfaces with natural language.

**中文介绍（README总结）**: Page Agent 是一个嵌入网页内的 JavaScript GUI Agent，用自然语言在页面中操控 Web 界面并通过文本方式直接操作 DOM，不依赖截图或多模态模型。它面向需要在自家 Web 产品里快速加入 AI 助手能力的开发者与 SaaS 团队，支持自带 LLM，并提供带人类介入的交互 UI。典型场景包括 SaaS 内置 AI Copilot、复杂表单/后台流程的一句式填报与操作、提升无障碍访问（语音/读屏驱动），以及通过可选 Chrome 扩展执行跨页面/多标签任务。

**关键词**: 自然语言控制GUI, DOM文本操作, 无截图自动化, 人类在环交互, 多标签页任务, 表单自动填充, Web可访问性, alibaba

**评分**: 36

**项目地址**: [GitHub](https://github.com/alibaba/page-agent)

---

## [11. google/A2UI](https://github.com/google/A2UI)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+220 today) | **Forks**: 🔱 934

**原始描述**: 

**中文介绍（README总结）**: A2UI 是一个开源的 Agent-to-User Interface 标准与库，用声明式 JSON 让智能体“说 UI”，把要呈现的界面意图发送给客户端，由客户端用自身的原生组件库（如 Flutter、Angular、Lit 等）渲染并支持可增量更新的界面。它面向需要让远程/跨信任边界的智能体输出丰富交互界面的应用开发者，核心技术是数据化的 UI 描述格式与受信组件目录机制，避免运行模型生成的任意代码以提升安全性。典型场景包括聊天式助手在业务系统里生成/填充卡片、表单、按钮等交互界面，并在对话过程中逐步更新内容。

**关键词**: 跨端UI渲染器, 组件白名单目录, 安全沙箱渲染, 增量UI更新, 可互操作UI协议, google, A2UI, Agent-to-User

**评分**: 41

**项目地址**: [GitHub](https://github.com/google/A2UI)

---

