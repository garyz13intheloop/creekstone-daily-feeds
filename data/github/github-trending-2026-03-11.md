# GitHub Trending 日榜 | 2026-03-11

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
**Stars**: ⭐ 0 (+6 today) | **Forks**: 🔱 209

**原始描述**: LiteRT, successor to TensorFlow Lite. is Google's On-device framework for high-performance ML & GenAI deployment on edge platforms, via efficient conversion, runtime, and optimization

**中文介绍（README总结）**: LiteRT 是 Google 的端侧机器学习与生成式 AI 部署框架，是 TensorFlow Lite 的继任者，面向需要在边缘设备上进行高性能推理的开发者与应用。它提供模型高效转换、运行时与优化能力，并通过 GPU/NPU 加速提升性能与降低延迟。关键技术包括编译模型 API（自动选择加速器、异步执行与高效 I/O 缓冲）、统一 NPU 加速以及 GPU 零拷贝缓冲互操作。典型场景是在手机、嵌入式与各类边缘平台上部署分类/检测等 ML 推理和端侧 GenAI 推理。

**关键词**: 端侧推理运行时, 边缘部署, 模型转换, 模型优化, 统一加速器接口, 自动加速器选择, 异步执行, 零拷贝缓冲区互操作, 编译模型 API

**评分**: 25

**项目地址**: [GitHub](https://github.com/google-ai-edge/LiteRT)

---

## Python

## [2. fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)

**语言**: Python  
**Stars**: ⭐ 0 (+630 today) | **Forks**: 🔱 2.2k

**原始描述**: SOTA Open Source TTS

**中文介绍（README总结）**: Fish Speech（Fish Audio S2）是一个开源文本转语音项目，面向需要高自然度、多语言语音合成的开发者与产品团队，支持多说话人、多轮生成，并可用自然语言标签细粒度控制韵律与情绪。其关键技术包括双自回归架构与强化学习对齐，训练数据覆盖约 50 种语言、超过千万小时音频。典型场景包括多语言语音助手/播报、角色配音与情绪化朗读，以及面向应用的命令行、WebUI 或服务端推理部署。

**关键词**: 文本转语音（TTS）, 开源语音合成, 多语言语音合成, 多说话人生成, 多轮语音生成, 韵律控制, 情感控制, 强化学习对齐, 双自回归架构, 命令行推理

**评分**: 38

**项目地址**: [GitHub](https://github.com/fishaudio/fish-speech)

---

## [3. langflow-ai/openrag](https://github.com/langflow-ai/openrag)

**语言**: Python  
**Stars**: ⭐ 0 (+491 today) | **Forks**: 🔱 119

**原始描述**: OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and Opensearch.

**中文介绍（README总结）**: OpenRAG 是一个单包式的检索增强生成（RAG）平台，面向需要做智能文档检索与基于知识库对话的开发者与团队，支持上传、解析与查询文档并通过聊天界面与大模型交互。它基于 Langflow 进行文档摄取与可视化工作流编排（含智能提示）、结合 Docling 做文档解析，并用 OpenSearch 提供语义检索与企业级搜索能力，整体以 FastAPI + Next.js 构建。典型场景包括企业内部知识库问答、面向多源文档的语义搜索、以及需要重排序与多智能体协作的 Agentic RAG 应用。

**关键词**: RAG, 智能体检索, 语义搜索, 文档解析, 文档摄取流水线, 工作流编排, 可视化工作流构建, 重排序, 多智能体协同, 模型上下文协议（MCP）

**评分**: 43

**项目地址**: [GitHub](https://github.com/langflow-ai/openrag)

---

## [4. vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)

**语言**: Python  
**Stars**: ⭐ 0 (+300 today) | **Forks**: 🔱 215

**原始描述**: Hindsight: Agent Memory That Learns

**中文介绍（README总结）**: Hindsight 是一套面向 AI Agent 的“可学习”记忆系统，目标是让智能体随时间积累经验并在后续交互中更好地应用，而不仅是回放对话历史。它宣称相比常见的 RAG、知识图谱等方案能在长期记忆任务上取得更高准确率，并在 LongMemEval 基准上达到较领先的表现。主要面向需要长期上下文与个性化的企业与创业团队的智能体应用，可通过封装 LLM 调用或 API 接入，实现记忆的自动存取与可控调用，用于各类对话型 AI 场景的持续学习。

**关键词**: Agent 记忆系统, 长期记忆, 持续学习记忆, 记忆存储与检索, RAG 替代方案, 知识图谱替代方案, 生产级部署, vectorize-io

**评分**: 58

**项目地址**: [GitHub](https://github.com/vectorize-io/hindsight)

---

## [5. NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

**语言**: Python  
**Stars**: ⭐ 0 (+1.2k today) | **Forks**: 🔱 674

**原始描述**: The agent that grows with you

**中文介绍（README总结）**: Hermes Agent 是 Nous Research 的自我改进型 AI 智能体，通过内置学习闭环把任务经验沉淀为可复用技能，并在使用中持续优化，支持跨会话检索历史对话与用户建模以实现长期记忆与个性化。它面向需要长期协作与自动化的个人与团队，可在本地终端、Docker、SSH 到云端/Serverless（如 Modal、Daytona）等多种环境运行，并可从 Telegram 等渠道随时交互。关键技术包括基于记忆的周期性“提醒”持久化、FTS5 会话搜索结合 LLM 摘要召回、并行子代理协作与通过 RPC 调用工具的脚本化管线，以及可切换的多模型后端（OpenRouter/GLM/Kimi/OpenAI/自建端点等）。典型场景是自然语言配置的定时任务（日报、备份、审计）、复杂研究或工程任务的并行拆解执行、以及跨设备跨会话的持续助手工作流。

**关键词**: 闭环学习, 技能自动生成, 多模型路由, 任务调度（Cron）, NousResearch, hermes-agent, Agent, grows

**评分**: 62

**项目地址**: [GitHub](https://github.com/NousResearch/hermes-agent)

---

## [6. 666ghj/MiroFish](https://github.com/666ghj/MiroFish)

**语言**: Python  
**Stars**: ⭐ 0 (+1.8k today) | **Forks**: 🔱 1.9k

**原始描述**: A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物

**中文介绍（README总结）**: MiroFish 是一款基于多智能体与群体智能的通用预测/仿真引擎：从新闻、政策草案、金融信号或文本故事等“种子信息”中抽取结构化知识，构建高保真的平行数字世界，让大量具备人格、长期记忆与行为逻辑的智能体交互演化，并支持用户以自然语言注入变量进行推演。它面向决策者与分析人员做政策、公关、舆情、金融等低风险预演，也面向个人用户进行创意沙盘与剧情结局探索。关键技术包括 GraphRAG/图谱构建、实体关系抽取、人设生成与环境参数化的 Agent 编排、时序记忆动态更新，以及用于生成预测报告并可与仿真世界深度交互的 ReportAgent。典型场景如热点舆情事件推演与报告生成、文学作品结局推演，以及金融/时政方向的模拟预测。

**关键词**: 多智能体仿真, 群体智能, 预测推演, 数字孪生, 平行数字世界, 沙盘推演, 基于智能体建模, 知识图谱构建, 实体关系抽取, 长期记忆, 交互式报告生成

**评分**: 37

**项目地址**: [GitHub](https://github.com/666ghj/MiroFish)

---

## Shell

## [7. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+1.7k today) | **Forks**: 🔱 6.1k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: Superpowers 是一套面向“编码代理/AI 编程助手”的软件开发工作流与技能框架，通过可组合的 skills 和初始指令让代理先澄清目标、从对话中提炼并分段呈现规格说明，再在你确认设计后生成可执行的实现计划。它强调红/绿 TDD、YAGNI 与 DRY，并采用“子代理驱动开发”把任务拆解后交由多个代理执行、检查与评审，从而让代理在遵循既定计划的前提下更长时间自主推进。典型场景是你在 Claude Code、Cursor、Codex 等工具中启动编程代理进行新功能/项目开发时，用它把需求到实现的全过程规范化并降低偏航。

**关键词**: 代码代理工作流, 代理技能框架, 可组合技能, 规格澄清, 设计审阅, 实现计划生成, 子代理协同开发, 长时自主执行, 测试驱动开发（TDD）, 红绿重构循环

**评分**: 24

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

## [8. msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)

**语言**: Shell  
**Stars**: ⭐ 0 (+4.1k today) | **Forks**: 🔱 5.1k

**原始描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**中文介绍（README总结）**: 这是一个“AI Agency”式的多智能体集合，提供一组带人格设定与固定流程的专业代理（如前端工程、设计、营销/Reddit 社区运营、产品等），强调产出可交付物与可衡量结果。面向需要把常见职能工作流程化、自动化的开发者与团队，用于快速组建“虚拟专家团队”协作完成代码、流程与业务增长相关任务。其关键做法是将每个代理封装为包含身份/沟通风格、工作流、交付物示例与成功指标的模板文件，并可在 Claude Code 等多种开发/对话工具中调用与复用。典型场景包括用多个角色分工完成从产品/设计到工程实现与社区运营的端到端工作流。

**关键词**: AI 代理库, 角色化智能体, 多智能体工作流, 可交付模板, 成功指标评估, 提示词工程, 开发者工具集成, msitarzewski

**评分**: 13

**项目地址**: [GitHub](https://github.com/msitarzewski/agency-agents)

---

## TypeScript

## [9. InsForge/InsForge](https://github.com/InsForge/InsForge)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+260 today) | **Forks**: 🔱 303

**原始描述**: Give agents everything they need to ship fullstack apps. The backend built for agentic development.

**中文介绍（README总结）**: InsForge 是面向 AI 编程代理与 AI 代码编辑器的后端开发平台，通过语义层把数据库、认证、存储、函数等后端能力抽象成代理可理解、可推理并能端到端操作的接口。它提供“后端上下文工程”，让代理能获取可用操作与文档、直接配置后端原语，并以结构化 schema 暴露状态与日志便于检查。核心能力涵盖认证/会话、Postgres 数据库、S3 兼容存储、OpenAI 兼容的多模型网关、边缘函数与站点构建部署，典型场景是让代理自动搭建与迭代全栈应用的后端与发布流程。

**关键词**: 智能体后端, 语义层, 后端上下文工程, MCP 服务器, 后端可观测性, 身份认证, S3 兼容对象存储, 边缘函数

**评分**: 52

**项目地址**: [GitHub](https://github.com/InsForge/InsForge)

---

## [10. alibaba/page-agent](https://github.com/alibaba/page-agent)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+1.2k today) | **Forks**: 🔱 437

**原始描述**: JavaScript in-page GUI agent. Control web interfaces with natural language.

**中文介绍（README总结）**: Page Agent 是一个嵌入网页内的 JavaScript GUI 代理，让用户用自然语言在页面上完成操作与流程。它面向 SaaS/企业后台等 Web 产品的开发者与终端用户，核心是基于文本的 DOM 操作（不依赖截图或多模态权限），并支持接入自有 LLM，提供带人工介入的交互式 UI。典型场景包括给产品内置 AI Copilot、复杂表单/多步流程的一句式填写，以及提升无障碍访问（语音/读屏等）；可选 Chrome 扩展支持跨页面/标签的多页任务。

**关键词**: 自然语言界面控制, DOM 文本操作, 客户端自动化, LLM 可插拔, 人机协同, 多标签页任务, 智能表单填写, 无截图自动化, 无障碍访问

**评分**: 40

**项目地址**: [GitHub](https://github.com/alibaba/page-agent)

---

## [11. google/A2UI](https://github.com/google/A2UI)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+220 today) | **Forks**: 🔱 942

**原始描述**: 

**中文介绍（README总结）**: A2UI 是一个开源的 Agent-to-User Interface 标准与库，用声明式 JSON 让智能体生成或填充可更新的富交互界面，并由客户端用自身的原生组件库（如 Flutter、Angular、Lit 等）进行渲染。它面向需要把远程/跨信任边界的智能体结果以安全方式呈现给用户的应用开发者与平台方，核心技术是“数据化而非可执行代码”的 UI 表达与受信组件目录机制，在保证安全性的同时保持界面表达能力。典型场景包括智能体在聊天或工作流中动态生成卡片式表单、按钮操作、信息摘要等交互 UI，并支持随对话逐步增量更新。

**关键词**: 声明式 UI, 跨端 UI 渲染, 客户端渲染器, 组件白名单目录, 安全沙箱, 增量 UI 更新, 代理-客户端互操作, UI 组件协议

**评分**: 40

**项目地址**: [GitHub](https://github.com/google/A2UI)

---

