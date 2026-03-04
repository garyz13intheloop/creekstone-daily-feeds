# GitHub Trending 日榜 | 2026-03-04

> 共 9 个项目

## 📑 目录

- [Go](#Go) (1 个项目)
- [Python](#Python) (4 个项目)
- [Rust](#Rust) (1 个项目)
- [TypeScript](#TypeScript) (2 个项目)
- [Unknown](#Unknown) (1 个项目)

---

## Go

## [1. aquasecurity/trivy](https://github.com/aquasecurity/trivy)

**语言**: Go  
**Stars**: ⭐ 0 (+164 today) | **Forks**: 🔱 47

**原始描述**: Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more

**中文介绍（README总结）**: Trivy 是一款综合型安全扫描器，用于在容器镜像、文件系统、远程 Git 仓库、虚拟机镜像以及 Kubernetes 等目标中发现安全问题。它面向 DevSecOps、开发与运维团队，可生成并分析软件依赖与 SBOM，检测已知漏洞（CVE）、IaC 配置错误、敏感信息/密钥泄露以及许可证风险。典型场景包括 CI/CD 流水线安全门禁、镜像与集群上线前扫描、以及云原生资产的持续合规与风险排查。

**关键词**: 容器镜像扫描, 漏洞扫描（CVE）, IaC 配置错误检测, 密钥泄露检测, 软件许可证合规, 文件系统扫描, 代码仓库扫描, 虚拟机镜像扫描, CI/CD 安全集成

**评分**: 31

**项目地址**: [GitHub](https://github.com/aquasecurity/trivy)

---

## Python

## [2. K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)

**语言**: Python  
**Stars**: ⭐ 0 (+798 today) | **Forks**: 🔱 1.3k

**原始描述**: A set of ready to use Agent Skills for research, science, engineering, analysis, finance and writing.

**中文介绍（README总结）**: Claude Scientific Skills 是一套面向支持开放 Agent Skills 标准的 AI 代理的开箱即用技能库，提供 170+ 科研与工程分析技能，用于把通用代理增强为可执行多步骤科学工作流的研究助手。它主要服务科研人员、工程师与分析师，可在 Cursor、Claude Code、Codex 等环境中调用。关键在于将生物信息学/基因组、药物发现、分子动力学、地理空间与时间序列等领域的常用库、数据库与工具封装为有文档与示例的标准化技能，以提升复杂任务的可靠性与可复用性。典型场景包括癌症基因组分析、药物-靶点结合与虚拟筛选、RNA velocity、临床研究与精密医疗分析等。

**关键词**: 科研工作流自动化, 生物信息学, 癌症基因组学, 分子动力学, RNA 速度分析, 蛋白质组学, 地理空间分析, 时间序列预测

**评分**: 50

**项目地址**: [GitHub](https://github.com/K-Dense-AI/claude-scientific-skills)

---

## [3. agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)

**语言**: Python  
**Stars**: ⭐ 0 (+112 today) | **Forks**: 🔱 1.5k

**原始描述**: Build and run agents you can see, understand and trust.

**中文介绍（README总结）**: AgentScope 是面向生产环境的 LLM 智能体框架，用于构建可观察、可理解并可部署的单体或多智能体应用，目标用户包括需要快速落地智能体的开发者与团队。它提供 ReAct 智能体、工具/技能调用、人类在环控制、记忆与规划、评测与模型微调等抽象，并通过消息中心支持灵活编排以及 MCP、A2A 等协议集成。典型场景包括工具驱动的业务自动化、多智能体工作流、带可观测性的本地/云端/K8s 部署，以及实时语音交互智能体。

**关键词**: LLM智能体框架, 多智能体编排, 人在回路, 记忆管理, 长期记忆, 实时语音智能体, agentscope-ai, agentscope

**评分**: 48

**项目地址**: [GitHub](https://github.com/agentscope-ai/agentscope)

---

## [4. LMCache/LMCache](https://github.com/LMCache/LMCache)

**语言**: Python  
**Stars**: ⭐ 0 (+135 today) | **Forks**: 🔱 974

**原始描述**: Supercharge Your LLM with the Fastest KV Cache Layer

**中文介绍（README总结）**: LMCache 是面向 LLM 在线推理的 KV Cache 加速扩展，目标是在长上下文等场景下降低首 token 延迟（TTFT）并提升吞吐。它把可复用文本的 KV cache 分布存储在数据中心的 GPU/CPU/磁盘乃至 S3，并通过零拷贝、NIXL、GDS 等加速手段，实现跨不同服务引擎实例对“任意重复文本”（不局限前缀）的 KV 复用，从而节省 GPU 计算并减少响应等待。典型用于与 vLLM、SGLang 等推理框架结合的多轮问答、RAG 等场景，可实现显著的延迟与 GPU 周期节省。

**关键词**: LLM 推理服务, 缓存分层存储, 长上下文加速, 吞吐量优化, KV 缓存卸载（GPU→CPU）, P2P 缓存共享, 零拷贝传输, LMCache

**评分**: 52

**项目地址**: [GitHub](https://github.com/LMCache/LMCache)

---

## [5. alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox)

**语言**: Python  
**Stars**: ⭐ 0 (+1.1k today) | **Forks**: 🔱 409

**原始描述**: OpenSandbox is a general-purpose sandbox platform for AI applications, offering multi-language SDKs, unified sandbox APIs, and Docker/Kubernetes runtimes for scenarios like Coding Agents, GUI Agents, Agent Evaluation, AI Code Execution, and RL Training.

**中文介绍（README总结）**: OpenSandbox 是面向 AI 应用的通用沙箱平台，为开发者提供多语言 SDK 与统一的沙箱协议/接口，用于创建、管理并执行隔离环境中的任务。它支持 Docker 与 Kubernetes 运行时及生命周期管理，覆盖本地运行到大规模分布式调度。典型场景包括 Coding/GUI Agents 的安全执行与自动化、Agent 评测、AI 代码执行与强化学习训练，并提供命令、文件系统、Code Interpreter 等内置环境与网络出入口控制能力。

**关键词**: 安全沙箱, 代码执行隔离, Agent 运行环境, 代码解释器, 多语言 SDK, 网络出站控制, 浏览器自动化, 桌面环境隔离

**评分**: 43

**项目地址**: [GitHub](https://github.com/alibaba/OpenSandbox)

---

## Rust

## [6. ruvnet/RuView](https://github.com/ruvnet/RuView)

**语言**: Rust  
**Stars**: ⭐ 0 (+4.4k today) | **Forks**: 🔱 3.3k

**原始描述**: π RuView: WiFi DensePose turns commodity WiFi signals into real-time human pose estimation, vital sign monitoring, and presence detection — all without a single pixel of video.

**中文介绍（README总结）**: RuView（WiFi DensePose）利用可获取CSI的商用WiFi信号扰动，在无摄像头、无可穿戴、无需联网的情况下实现实时人体姿态估计、存在检测与呼吸/心率等生命体征监测，甚至支持一定的隔墙感知。它面向希望用低成本隐私友好方式做室内感知的开发者与研究者，核心依赖基于物理的信号处理结合机器学习对CSI（子载波幅度/相位）进行重建与推断，并可在ESP32等边缘设备上本地运行。典型场景包括家庭/养老看护的跌倒与异常呼吸告警、智能家居的人体存在与活动感知、以及无需视频的室内行为与健康监测。

**关键词**: 无摄像头人体姿态估计, 穿墙感知, 生命体征监测, 呼吸心率估计, 存在检测, 边缘计算, 跌倒检测, 物理信号处理

**评分**: 32

**项目地址**: [GitHub](https://github.com/ruvnet/RuView)

---

## TypeScript

## [7. CodebuffAI/codebuff](https://github.com/CodebuffAI/codebuff)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+126 today) | **Forks**: 🔱 434

**原始描述**: Generate code from the terminal!

**中文介绍（README总结）**: Codebuff 是一个开源的 AI 编码助手，面向在终端里通过自然语言对现有代码库进行修改的开发者，能够跨文件理解项目并做出精确编辑。它采用多智能体协作机制（如文件选择、规划、编辑、审查等）来提升上下文理解与改动质量，并可在修改后运行测试以降低引入错误的风险。典型场景包括为 API 增加认证、修复 SQL 注入、为接口添加限流、重构数据库连接等，同时也支持自定义智能体与工作流来适配团队自动化需求。

**关键词**: CLI 编程助手, 代码库自动编辑, 自然语言指令编程, 多智能体编排, 规划-执行-审查流程, 代码变更自动审查, 自动化测试运行, 自定义 Agent 工作流, Git 状态分析与提交

**评分**: 48

**项目地址**: [GitHub](https://github.com/CodebuffAI/codebuff)

---

## [8. superset-sh/superset](https://github.com/superset-sh/superset)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+632 today) | **Forks**: 🔱 291

**原始描述**: IDE for the AI Agents Era - Run an army of Claude Code, Codex, etc. on your machine

**中文介绍（README总结）**: Superset 是面向“CLI 编码智能体”时代的桌面终端/IDE，用于在本机同时运行多个 Claude Code、Codex 等终端型 coding agent，并集中管理它们的工作流。它为每个任务创建独立的 git worktree 以隔离改动，提供统一监控与通知，并内置 diff 查看器与编辑能力以便快速审阅与合并变更。适合需要并行推进多项开发任务、减少上下文切换并加速交付的开发者与团队场景。

**关键词**: AI 编程代理, 终端式 IDE, 任务隔离, 代理监控, 通知提醒, 代码 diff 审阅, 桌面客户端, Caddy 反向代理

**评分**: 48

**项目地址**: [GitHub](https://github.com/superset-sh/superset)

---

## Unknown

## [9. msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)

**语言**: Unknown  
**Stars**: ⭐ 0 (+593 today) | **Forks**: 🔱 736

**原始描述**: A complete AI agency at your fingertips** - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**中文介绍（README总结）**: 这是一个“AI 代理机构”式的 AI 角色集合，提供多种带人格设定与标准流程的专业代理（如工程、设计、营销、产品、项目管理、测试、支持等），产出面向交付的代码、流程与可衡量结果。它面向希望用一组可复用“专家代理”来提升工作流的个人或团队，可作为在 Claude Code 等环境中调用的角色库或参考模板。关键特点是领域专精、人格驱动的沟通风格、以交付物与指标为中心，典型场景包括前端开发、社区运营、产品规划与质量保障等。

**关键词**: Multi-Agent, 代理工作流, 角色化提示词, 领域专家代理, 交付物模板, 成功指标, 软件开发代理, 产品管理代理, 社区运营代理, 空间计算代理

**评分**: 17

**项目地址**: [GitHub](https://github.com/msitarzewski/agency-agents)

---

