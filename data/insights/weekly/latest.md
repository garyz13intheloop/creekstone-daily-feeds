# Weekly Research Report | 2026-02-23 ~ 2026-03-01

> generated_at: 2026-03-02T09:00:20Z
> k_selected: 4
> embedding_model: text-embedding-3-large
> chat_model: gpt-4o-mini, gpt-5.2-2025-12-11

# 周度科技趋势研究报告
## 本周摘要
在2026年2月23日至3月1日的这一周，科技领域的趋势主要集中在多智能体系统的可复现评测、编排与安全框架、隐私友好的视觉语言模型推理，以及多语言语音识别的快速发展。随着多智能体技术的不断成熟，相关的评测框架和工具的可靠性成为了行业关注的焦点。同时，隐私保护和用户体验的提升也在推动语音识别和视觉语言模型的创新。

## 趋势主题

### 1. 面向多智能体的可复现评测与“可记忆/可调用”能力栈
该主题聚焦于为多智能体系统建立可复现的评测框架与基准，利用向量检索和知识图谱记忆等方法提升智能体在复杂任务中的可靠性。当前，行业正在将多智能体的能力从“能跑”推进到“可衡量、可复现、可持续改进”。例如，VeRO和DARE-bench等项目的出现，标志着对智能体性能的系统性评估需求日益增加。

- **代表项目对比**：
  - **Self-improving Agent Memory Upgrade (SurrealDB)**：提供知识图谱记忆系统，支持自动上下文注入和记忆健康维护。
  - **VeRO**：一个可复现评测框架，专注于优化其他智能体的表现。
  - **DARE-bench**：用于数据科学任务的指令遵循基准，提升LLM在多步任务中的保真度。

- **风险与观察**：
  - 评测框架是否能真实覆盖多智能体协作的关键失败模式。
  - 工具描述重写是否会引入新的偏差。
  - 多智能体记忆系统的去重策略如何避免误删关键事实。

### 2. 多智能体编排与安全框架
随着多智能体系统的普及，任务编排与安全框架的需求日益增加，以确保智能体的高效协作与安全性。当前，AI Agent的应用场景不断扩展，尤其是在数据处理与任务自动化领域，迫切需要有效的编排与安全机制。

- **代表项目对比**：
  - **腾讯云COS技能集成**：集成云端文件管理与多媒体处理能力。
  - **ShieldCortex**：面向AI Agent的安全框架，降低提示注入与越权调用风险。
  - **KiloClaw**：OpenClaw的全托管版本，专注于AI Agent的实际应用。

- **风险与观察**：
  - 如何确保多智能体之间的安全通信。
  - 在任务编排中，如何处理潜在的权限越界问题。
  - 如何管理和保护敏感数据。

### 3. 隐私友好的人体感知与视觉语言模型稳健推理
该主题集中在利用WiFi信号实现低侵入人体感知，以及围绕视觉语言模型的推理循环和同义改写敏感性。当前，隐私保护的需求推动了无摄像头、无可穿戴设备的人体感知技术的发展。

- **代表项目对比**：
  - **ruvnet/wifi-densepose**：通过WiFi信号实现无摄像头的实时人体姿态估计。
  - **AD-Loop**：交错的“分析-起草”思考循环，提升多模态理解与生成性能。
  - **PSF-Med**：评测医学VLM的同义改写敏感性，发现大量“答案翻转”。

- **风险与观察**：
  - WiFi DensePose对支持CSI的硬件依赖强，应用上限需评估。
  - 医学VLM对同义改写的敏感性在高风险场景下的稳定性如何定义。
  - 不确定性降低方法的计算开销与收益如何权衡。

### 4. 多语言语音识别与智能应用
随着多语言语音识别技术的发展，智能应用正在快速提升用户体验和交互效率。市场对高效、低延迟的语音识别和智能应用的需求日益增长，尤其是在全球化背景下，支持多语言的解决方案显得尤为重要。

- **代表项目对比**：
  - **Stitch by Google**：可编辑设计稿和真实代码生成工具，支持多步骤设计任务。
  - **Wispr Flow for Android**：智能语音转文字应用，能够将口述内容整理为可发送的文本。

- **风险与观察**：
  - 如何确保多语言语音识别的准确性和可靠性。
  - 不同文化和语言背景下，用户对智能应用的接受度如何。

## 项目榜单
1. [**ruvnet/wifi-densepose**](https://github.com/ruvnet/wifi-densepose) - 利用WiFi信号实现无摄像头的人体姿态估计。
2. [**Tencent COS**](https://clawhub.ai/ShawnMinh/tencent-cos-skill) - 集成腾讯云COS与CI，实现云端文件管理与多媒体处理能力。
3. [**Self-improving Agent Memory Upgrade (SurrealDB)**](https://clawhub.ai/maverick-software/surrealdb-knowledge-graph-memory) - 提供知识图谱记忆系统，支持自动上下文注入。
4. [**VeRO**](https://arxiv.org/abs/2602.22480v1) - 可复现评测框架，专注于优化其他智能体的表现。
5. [**KiloClaw**](https://www.producthunt.com/products/kiloclaw?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29) - OpenClaw的全托管版本，专注于AI Agent的实际应用。

## 关键词趋势
- **任务编排**：随着多智能体系统的普及，任务编排的需求日益增加。
- **评测框架**：多智能体评测框架的建立成为行业关注的焦点。
- **知识图谱构建**：知识图谱在多智能体系统中的应用逐渐增多。
- **隐私保护**：隐私友好的人体感知技术受到越来越多的关注。
- **低延迟推理**：在多语言语音识别和视觉语言模型中，低延迟推理的需求不断上升。

## 交叉来源观察
通过对多个来源的数据分析，发现以下趋势：
- 多智能体系统的评测框架正在形成标准化，多个项目如VeRO和DARE-bench正在推动这一进程。
- 隐私友好的技术正在成为市场的热门话题，尤其是在医疗和家庭监控领域。
- 多语言语音识别的技术进步正在推动智能应用的普及，用户体验显著提升。

## 下周预测
1. **评测框架与基准**：期待VeRO与DARE-bench是否会出现更明确的复现流程或任务套件扩展。
2. **工具可靠性方向**：观察是否有更多围绕“重写工具描述/接口”的对比证据，特别是在无执行轨迹条件下的稳定性表现。
3. **多智能体记忆方向**：向量近重复去重、每周陈旧低置信修剪等机制是否被更多项目采纳或验证其效果。
4. **数据分析与代码生成任务**：是否出现将数据科学基准与智能体评测框架联动的趋势信号。
5. **工程侧信号**：低延迟推理与GPU约束下，RAG/向量检索在多智能体系统中的部署与性能取舍讨论是否增多。

本周的研究报告展示了多智能体系统、隐私保护技术及多语言语音识别等领域的最新发展，未来的趋势将继续受到市场需求和技术进步的推动。

## 引用索引

- [arxiv:ax-2026-02-23-1] Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use (https://arxiv.org/abs/2602.20426v1)
- [arxiv:ax-2026-02-23-10] CREDIT: Certified Ownership Verification of Deep Neural Networks Against Model Extraction Attacks (https://arxiv.org/abs/2602.20419v1)
- [arxiv:ax-2026-02-23-11] CITED: A Decision Boundary-Aware Signature for GNNs Towards Model Extraction Defense (https://arxiv.org/abs/2602.20418v1)
- [arxiv:ax-2026-02-23-12] $κ$-Explorer: A Unified Framework for Active Model Estimation in MDPs (https://arxiv.org/abs/2602.20404v1)
- [arxiv:ax-2026-02-23-13] Three Concrete Challenges and Two Hopes for the Safety of Unsupervised Elicitation (https://arxiv.org/abs/2602.20400v1)
- [arxiv:ax-2026-02-23-14] GeoPT: Scaling Physics Simulation via Lifted Geometric Pre-Training (https://arxiv.org/abs/2602.20399v1)
- [arxiv:ax-2026-02-23-15] cc-Shapley: Measuring Multivariate Feature Importance Needs Causal Context (https://arxiv.org/abs/2602.20396v1)
- [arxiv:ax-2026-02-23-2] Implicit Intelligence -- Evaluating Agents on What Users Don't Say (https://arxiv.org/abs/2602.20424v1)
- [arxiv:ax-2026-02-23-3] Diffusion Modulation via Environment Mechanism Modeling for Planning (https://arxiv.org/abs/2602.20422v1)
- [arxiv:ax-2026-02-23-4] Case-Aware LLM-as-a-Judge Evaluation for Enterprise-Scale RAG Systems (https://arxiv.org/abs/2602.20379v1)
- [arxiv:ax-2026-02-23-5] How communicatively optimal are exact numeral systems? Once more on lexicon size and morphosyntactic complexity (https://arxiv.org/abs/2602.20372v1)
- [arxiv:ax-2026-02-23-6] gQIR: Generative Quanta Image Reconstruction (https://arxiv.org/abs/2602.20417v1)
- [arxiv:ax-2026-02-23-7] SimLBR: Learning to Detect Fake Images by Learning to Detect Real Images (https://arxiv.org/abs/2602.20412v1)
- [arxiv:ax-2026-02-23-8] CLIPoint3D: Language-Grounded Few-Shot Unsupervised 3D Point Cloud Domain Adaptation (https://arxiv.org/abs/2602.20409v1)
- [arxiv:ax-2026-02-23-9] GauS: Differentiable Scheduling Optimization via Gaussian Reparameterization (https://arxiv.org/abs/2602.20427v1)
- [arxiv:ax-2026-02-24-15] FedVG: Gradient-Guided Aggregation for Enhanced Federated Learning (https://arxiv.org/abs/2602.21399v1)
- [arxiv:ax-2026-02-24-2] PSF-Med: Measuring and Explaining Paraphrase Sensitivity in Medical Vision Language Models (https://arxiv.org/abs/2602.21428v1)
- [arxiv:ax-2026-02-24-4] ECHOSAT: Estimating Canopy Height Over Space And Time (https://arxiv.org/abs/2602.21421v1)
- [arxiv:ax-2026-02-24-5] WildSVG: Towards Reliable SVG Generation Under Real-Word Conditions (https://arxiv.org/abs/2602.21416v1)
- [arxiv:ax-2026-02-24-7] FlowFixer: Towards Detail-Preserving Subject-Driven Generation (https://arxiv.org/abs/2602.21402v1)
- [arxiv:ax-2026-02-24-8] MINAR: Mechanistic Interpretability for Neural Algorithmic Reasoning (https://arxiv.org/abs/2602.21442v1)
- [arxiv:ax-2026-02-24-9] Provably Safe Generative Sampling with Constricting Barrier Functions (https://arxiv.org/abs/2602.21429v1)
- [arxiv:ax-2026-02-25-1] Synergizing Understanding and Generation with Interleaved Analyzing-Drafting Thinking (https://arxiv.org/abs/2602.21435v1)
- [arxiv:ax-2026-02-25-10] Proximal-IMH: Proximal Posterior Proposals for Independent Metropolis-Hastings with Approximate Operators (https://arxiv.org/abs/2602.21426v1)
- [arxiv:ax-2026-02-25-11] On the Structural Non-Preservation of Epistemic Behaviour under Policy Transformation (https://arxiv.org/abs/2602.21424v1)
- [arxiv:ax-2026-02-25-12] Overconfident Errors Need Stronger Correction: Asymmetric Confidence Penalties for Reinforcement Learning (https://arxiv.org/abs/2602.21420v1)
- [arxiv:ax-2026-02-25-13] Benchmarking State Space Models, Transformers, and Recurrent Networks for US Grid Forecasting (https://arxiv.org/abs/2602.21415v1)
- [arxiv:ax-2026-02-25-14] Generative Bayesian Computation as a Scalable Alternative to Gaussian Process Surrogates (https://arxiv.org/abs/2602.21408v1)
- [arxiv:ax-2026-02-25-3] Automating Timed Up and Go Phase Segmentation and Gait Analysis via the tugturn Markerless 3D Pipeline (https://arxiv.org/abs/2602.21425v1)
- [arxiv:ax-2026-02-25-6] Exploring Vision-Language Models for Open-Vocabulary Zero-Shot Action Segmentation (https://arxiv.org/abs/2602.21406v1)
- [arxiv:ax-2026-02-26-1] VeRO: An Evaluation Harness for Agents to Optimize Agents (https://arxiv.org/abs/2602.22480v1)
- [arxiv:ax-2026-02-26-10] Beyond Dominant Patches: Spatial Credit Redistribution For Grounded Vision-Language Models (https://arxiv.org/abs/2602.22469v1)
- [arxiv:ax-2026-02-26-11] MammoWise: Multi-Model Local RAG Pipeline for Mammography Report Generation (https://arxiv.org/abs/2602.22462v1)
- [arxiv:ax-2026-02-26-12] Efficient Continual Learning in Language Models via Thalamically Routed Cortical Columns (https://arxiv.org/abs/2602.22479v1)
- [arxiv:ax-2026-02-26-13] Beyond performance-wise Contribution Evaluation in Federated Learning (https://arxiv.org/abs/2602.22470v1)
- [arxiv:ax-2026-02-26-14] ECHO: Encoding Communities via High-order Operators (https://arxiv.org/abs/2602.22446v1)
- [arxiv:ax-2026-02-26-15] Calibrated Test-Time Guidance for Bayesian Inference (https://arxiv.org/abs/2602.22428v1)
- [arxiv:ax-2026-02-26-2] ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization (https://arxiv.org/abs/2602.22465v1)
- [arxiv:ax-2026-02-26-3] CWM: Contrastive World Models for Action Feasibility Learning in Embodied Agent Pipelines (https://arxiv.org/abs/2602.22452v1)
- [arxiv:ax-2026-02-26-4] A Framework for Assessing AI Agent Decisions and Outcomes in AutoML Pipelines (https://arxiv.org/abs/2602.22442v1)
- [arxiv:ax-2026-02-26-5] Importance of Prompt Optimisation for Error Detection in Medical Notes Using Language Models (https://arxiv.org/abs/2602.22483v1)
- [arxiv:ax-2026-02-26-6] Sydney Telling Fables on AI and Humans: A Corpus Tracing Memetic Transfer of Persona between LLMs (https://arxiv.org/abs/2602.22481v1)
- [arxiv:ax-2026-02-26-7] Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models (https://arxiv.org/abs/2602.22475v1)
- [arxiv:ax-2026-02-26-8] Bridging Latent Reasoning and Target-Language Generation via Retrieval-Transition Heads (https://arxiv.org/abs/2602.22453v1)
- [arxiv:ax-2026-02-26-9] A Fusion of context-aware based BanglaBERT and Two-Layer Stacked LSTM Framework for Multi-Label Cyberbullying Detection (https://arxiv.org/abs/2602.22449v1)
- [arxiv:ax-2026-02-27-1] Toward Expert Investment Teams:A Multi-Agent LLM System with Fine-Grained Trading Tasks (https://arxiv.org/abs/2602.23330v1)
- [arxiv:ax-2026-02-27-10] A Dataset is Worth 1 MB (https://arxiv.org/abs/2602.23358v1)
- [arxiv:ax-2026-02-27-11] SOTAlign: Semi-Supervised Alignment of Unimodal Vision and Language Models via Optimal Transport (https://arxiv.org/abs/2602.23353v1)
- [arxiv:ax-2026-02-27-12] FlashOptim: Optimizers for Memory Efficient Training (https://arxiv.org/abs/2602.23349v1)
- [arxiv:ax-2026-02-27-13] Mean Estimation from Coarse Data: Characterizations and Efficient Algorithms (https://arxiv.org/abs/2602.23341v1)
- [arxiv:ax-2026-02-27-14] Differentiable Zero-One Loss via Hypersimplex Projections (https://arxiv.org/abs/2602.23336v1)
- [arxiv:ax-2026-02-27-15] ParamMem: Augmenting Language Agents with Parametric Reflective Memory (https://arxiv.org/abs/2602.23320v1)
- [arxiv:ax-2026-02-27-3] Invariant Transformation and Resampling based Epistemic-Uncertainty Reduction (https://arxiv.org/abs/2602.23315v1)
- [arxiv:ax-2026-02-27-4] MediX-R1: Open Ended Medical Reinforcement Learning (https://arxiv.org/abs/2602.23363v1)
- [arxiv:ax-2026-02-27-5] VGG-T$^3$: Offline Feed-Forward 3D Reconstruction at Scale (https://arxiv.org/abs/2602.23361v1)
- [arxiv:ax-2026-02-27-6] Sensor Generalization for Adaptive Sensing in Event-based Object Detection via Joint Distribution Training (https://arxiv.org/abs/2602.23357v1)
- [arxiv:ax-2026-02-27-7] Retrieve and Segment: Are a Few Examples Enough to Bridge the Supervision Gap in Open-Vocabulary Segmentation? (https://arxiv.org/abs/2602.23339v1)
- [arxiv:ax-2026-02-27-8] ThinkOmni: Lifting Textual Reasoning to Omni-modal Scenarios via Guidance Decoding (https://arxiv.org/abs/2602.23306v1)
- [arxiv:ax-2026-02-27-9] Model Agreement via Anchoring (https://arxiv.org/abs/2602.23360v1)
- [arxiv:ax-2026-02-28-15] PRIMA: Pre-training with Risk-integrated Image-Metadata Alignment for Medical Diagnosis via LLM (https://arxiv.org/abs/2602.23297v1)
- [arxiv:ax-2026-02-28-16] ManifoldGD: Training-Free Hierarchical Manifold Guidance for Diffusion-Based Dataset Distillation (https://arxiv.org/abs/2602.23295v1)
- [arxiv:ax-2026-02-28-17] Towards Long-Form Spatio-Temporal Video Grounding (https://arxiv.org/abs/2602.23294v1)
- [arxiv:ax-2026-02-28-18] PGVMS: A Prompt-Guided Unified Framework for Virtual Multiplex IHC Staining with Pathological Semantic Learning (https://arxiv.org/abs/2602.23292v1)
- [arxiv:ax-2026-02-28-19] LineGraph2Road: Structural Graph Reasoning on Line Graphs for Road Network Extraction (https://arxiv.org/abs/2602.23290v1)
- [arxiv:ax-2026-02-28-2] LLM Novice Uplift on Dual-Use, In Silico Biology Tasks (https://arxiv.org/abs/2602.23329v1)
- [arxiv:ax-2026-02-28-27] A Proper Scoring Rule for Virtual Staining (https://arxiv.org/abs/2602.23305v1)
- [arxiv:ax-2026-02-28-28] Inferential Mechanics Part 1: Causal Mechanistic Theories of Machine Learning in Chemical Biology with Implications (https://arxiv.org/abs/2602.23303v1)
- [arxiv:ax-2026-02-28-29] Conformalized Neural Networks for Federated Uncertainty Quantification under Dual Heterogeneity (https://arxiv.org/abs/2602.23296v1)
- [arxiv:ax-2026-02-28-30] Physics Informed Viscous Value Representations (https://arxiv.org/abs/2602.23280v1)
- [arxiv:ax-2026-02-28-4] The logic of KM belief update is contained in the logic of AGM belief revision (https://arxiv.org/abs/2602.23302v1)
- [arxiv:ax-2026-02-28-5] ODEBrain: Continuous-Time EEG Graph for Modeling Dynamic Brain Networks (https://arxiv.org/abs/2602.23285v1)
- [arxiv:ax-2026-02-28-6] CXReasonAgent: Evidence-Grounded Diagnostic Reasoning Agent for Chest X-rays (https://arxiv.org/abs/2602.23276v1)
- [arxiv:ax-2026-02-28-7] Evaluating Stochasticity in Deep Research Agents (https://arxiv.org/abs/2602.23271v1)
- [arxiv:ax-2026-02-28-8] A Mixture-of-Experts Model for Multimodal Emotion Recognition in Conversations (https://arxiv.org/abs/2602.23300v1)
- [arxiv:ax-2026-02-28-9] SPARTA: Scalable and Principled Benchmark of Tree-Structured Multi-hop QA over Text and Tables (https://arxiv.org/abs/2602.23286v1)
- [arxiv:ax-2026-03-01-1] DARE-bench: Evaluating Modeling and Instruction Fidelity of LLMs in Data Science (https://arxiv.org/abs/2602.24288v1)
- [arxiv:ax-2026-03-01-10] Memory Caching: RNNs with Growing Memory (https://arxiv.org/abs/2602.24281v1)
- [arxiv:ax-2026-03-01-11] Who Guards the Guardians? The Challenges of Evaluating Identifiability of Learned Representations (https://arxiv.org/abs/2602.24278v1)
- [arxiv:ax-2026-03-01-12] Efficient Discovery of Approximate Causal Abstractions via Neural Mechanism Sparsification (https://arxiv.org/abs/2602.24266v1)
- [arxiv:ax-2026-03-01-13] Coverage-Aware Web Crawling for Domain-Specific Supplier Discovery via a Web--Knowledge--Web Pipeline (https://arxiv.org/abs/2602.24262v1)
- [arxiv:ax-2026-03-01-14] Histopathology Image Normalization via Latent Manifold Compaction (https://arxiv.org/abs/2602.24251v1)
- [arxiv:ax-2026-03-01-15] Chunk-wise Attention Transducers for Fast and Accurate Streaming Speech-to-Text (https://arxiv.org/abs/2602.24245v1)
- [arxiv:ax-2026-03-01-2] A Minimal Agent for Automated Theorem Proving (https://arxiv.org/abs/2602.24273v1)
- [arxiv:ax-2026-03-01-3] Do LLMs Benefit From Their Own Words? (https://arxiv.org/abs/2602.24287v1)
- [arxiv:ax-2026-03-01-4] UFO-4D: Unposed Feedforward 4D Reconstruction from Two Images (https://arxiv.org/abs/2602.24290v1)
- [arxiv:ax-2026-03-01-5] Mode Seeking meets Mean Seeking for Fast Long Video Generation (https://arxiv.org/abs/2602.24289v1)
- [arxiv:ax-2026-03-01-6] Hierarchical Action Learning for Weakly-Supervised Action Segmentation (https://arxiv.org/abs/2602.24275v1)
- [arxiv:ax-2026-03-01-7] Compositional Generalization Requires Linear, Orthogonal Representations in Vision Embedding Models (https://arxiv.org/abs/2602.24264v1)
- [arxiv:ax-2026-03-01-8] Joint Geometric and Trajectory Consistency Learning for One-Step Real-World Super-Resolution (https://arxiv.org/abs/2602.24240v1)
- [arxiv:ax-2026-03-01-9] CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation (https://arxiv.org/abs/2602.24286v1)
- [clawhub:ch-2026-02-23-1] OpenTangl (https://clawhub.ai/8co/opentangl)
- [clawhub:ch-2026-02-23-2] Potato Tipper (https://clawhub.ai/CJ42/potato-tipper)
- [clawhub:ch-2026-02-23-3] glm-understand-image (https://clawhub.ai/Thincher/glm-understand-image)
- [clawhub:ch-2026-02-23-4] Dingtalk Ai Table (https://clawhub.ai/aliramw/dingtalk-ai-table)
- [clawhub:ch-2026-02-23-5] glm-web-search (https://clawhub.ai/Thincher/glm-web-search)
- [clawhub:ch-2026-02-23-6] App Store Deployment Guide (https://clawhub.ai/Skulick19/appstore-deployment-guide)
- [clawhub:ch-2026-02-23-7] Omni Research (https://clawhub.ai/lmanchu/omni-research)
- [clawhub:ch-2026-02-23-8] Polymarket Autopilot Experimental (https://clawhub.ai/mauonga/polymarket-autopilot-experimental)
- [clawhub:ch-2026-02-24-1] Auto Memory (https://clawhub.ai/jim-counter/auto-memory)
- [clawhub:ch-2026-02-24-2] OpenClaw Arena (https://clawhub.ai/billychl1/openclawarena-arena)
- [clawhub:ch-2026-02-24-3] Onebot Adapter 1.0.0 (https://clawhub.ai/haohaodlam/onebot-adapter-1-0-0)
- [clawhub:ch-2026-02-24-4] Flux (https://clawhub.ai/EckmanTechLLC/flux)
- [clawhub:ch-2026-02-24-5] Stable Browser (https://clawhub.ai/jarvis563/stable-browser)
- [clawhub:ch-2026-02-24-6] Kraken Exchange (https://clawhub.ai/askbeka/tentactl)
- [clawhub:ch-2026-02-28-1] 腾讯云COS存储 (https://clawhub.ai/ShawnMinh/tencent-cloud-cos)
- [clawhub:ch-2026-02-28-10] Password Generator (https://clawhub.ai/Yukin1218/password-generator)
- [clawhub:ch-2026-02-28-12] Money Idea Generator (https://clawhub.ai/devotion-coding/openclaw-skill-money-idea-generator)
- [clawhub:ch-2026-02-28-13] Self-improving Agent Memory Upgrade (SurrealDB) (https://clawhub.ai/maverick-software/surrealdb-knowledge-graph-memory)
- [clawhub:ch-2026-02-28-14] smartsheet-write (https://clawhub.ai/Roollond/smartsheet-write)
- [clawhub:ch-2026-02-28-15] Audio Editor (https://clawhub.ai/jwl1992/audio-editor)
- [clawhub:ch-2026-02-28-16] Search Cluster (https://clawhub.ai/1999AZZAR/search-cluster)
- [clawhub:ch-2026-02-28-17] ShieldCortex (https://clawhub.ai/jarvis-drakon/shieldcortex)
- [clawhub:ch-2026-02-28-18] Tender Offer Arbitrage Scanner (https://clawhub.ai/d-wwei/tender-offer-arbitrage)
- [clawhub:ch-2026-02-28-19] laiye-doc-processing (https://clawhub.ai/Jeane-li/laiye-doc-processing)
- [clawhub:ch-2026-02-28-2] Reddit 主题洞察 (https://clawhub.ai/Wbule/reddit-topic-insight)
- [clawhub:ch-2026-02-28-20] Claw Soul Backup (https://clawhub.ai/danielglh/claw-soul-backup)
- [clawhub:ch-2026-02-28-21] Pretenziya Ru (https://clawhub.ai/aggel008/pretenziya-ru)
- [clawhub:ch-2026-02-28-22] Nalog Ru (https://clawhub.ai/aggel008/nalog-ru)
- [clawhub:ch-2026-02-28-23] Dogovor Ru (https://clawhub.ai/aggel008/dogovor-ru)
- [clawhub:ch-2026-02-28-24] Chinovnik Ru (https://clawhub.ai/aggel008/chinovnik-ru)
- [clawhub:ch-2026-02-28-25] Analizy Ru (https://clawhub.ai/aggel008/analizy-ru)
- [clawhub:ch-2026-02-28-4] Tencent COS (https://clawhub.ai/ShawnMinh/tencent-cos-skill)
- [clawhub:ch-2026-02-28-5] Veadk Go Skills (https://clawhub.ai/helloldm/veadk-go-skills)
- [clawhub:ch-2026-02-28-6] 数联互通weather (https://clawhub.ai/jianmo1997/shulian-weather)
- [clawhub:ch-2026-02-28-8] Auto Doc Index (https://clawhub.ai/ERerGB/auto-doc-index)
- [clawhub:ch-2026-02-28-9] notion-agent-memory (https://clawhub.ai/vladchatware/notion-agent-memory)
- [github:gh-2026-02-24-2] huggingface/skills (https://github.com/huggingface/skills)
- [github:gh-2026-02-24-3] D4Vinci/Scrapling (https://github.com/D4Vinci/Scrapling)
- [github:gh-2026-02-24-6] ruvnet/claude-flow (https://github.com/ruvnet/claude-flow)
- [github:gh-2026-02-25-1] moonshine-ai/moonshine (https://github.com/moonshine-ai/moonshine)
- [github:gh-2026-02-25-11] abhigyanpatwari/GitNexus (https://github.com/abhigyanpatwari/GitNexus)
- [github:gh-2026-02-25-2] tukaani-project/xz (https://github.com/tukaani-project/xz)
- [github:gh-2026-02-25-4] datawhalechina/hello-agents (https://github.com/datawhalechina/hello-agents)
- [github:gh-2026-02-25-7] ruvnet/ruvector (https://github.com/ruvnet/ruvector)
- [github:gh-2026-02-26-3] PaddlePaddle/Paddle (https://github.com/PaddlePaddle/Paddle)
- [github:gh-2026-02-26-6] NousResearch/hermes-agent (https://github.com/NousResearch/hermes-agent)
- [github:gh-2026-02-27-10] anthropics/claude-code (https://github.com/anthropics/claude-code)
- [github:gh-2026-02-27-11] obra/superpowers (https://github.com/obra/superpowers)
- [github:gh-2026-02-27-4] Shubhamsaboo/awesome-llm-apps (https://github.com/Shubhamsaboo/awesome-llm-apps)
- [github:gh-2026-02-27-5] bytedance/deer-flow (https://github.com/bytedance/deer-flow)
- [github:gh-2026-02-27-7] datagouv/datagouv-mcp (https://github.com/datagouv/datagouv-mcp)
- [github:gh-2026-03-01-1] microsoft/markitdown (https://github.com/microsoft/markitdown)
- [github:gh-2026-03-01-10] superset-sh/superset (https://github.com/superset-sh/superset)
- [github:gh-2026-03-01-3] alibaba/OpenSandbox (https://github.com/alibaba/OpenSandbox)
- [github:gh-2026-03-01-5] K-Dense-AI/claude-scientific-skills (https://github.com/K-Dense-AI/claude-scientific-skills)
- [github:gh-2026-03-01-6] X-PLUG/MobileAgent (https://github.com/X-PLUG/MobileAgent)
- [github:gh-2026-03-01-8] ruvnet/wifi-densepose (https://github.com/ruvnet/wifi-densepose)
- [github:gh-2026-03-01-9] ruvnet/ruflo (https://github.com/ruvnet/ruflo)
- [producthunt:ph-2026-02-23-1] Siteline (https://www.producthunt.com/products/siteline?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-10] Callio (https://www.producthunt.com/products/callio-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-11] Cuto (https://www.producthunt.com/products/cuto?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-12] App Cleaner & Uninstaller 9.1 (https://www.producthunt.com/products/app-cleaner-uninstaller?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-13] PipedriveSheets (https://www.producthunt.com/products/pipedrivesheets?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-14] AnnotateAI (https://www.producthunt.com/products/annotateai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-15] Vibesafe (https://www.producthunt.com/products/vibesafe-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-16] aImsg (https://www.producthunt.com/products/aimsg-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-17] Atomic AGI (https://www.producthunt.com/products/atomic-agi?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-18] YourClaw: 1-Click Openclaw Orchestration (https://www.producthunt.com/products/yourclaw-1-click-openclaw-orchestration?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-2] Wispr Flow for Android (https://www.producthunt.com/products/wisprflow?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-3] TypeBoost (https://www.producthunt.com/products/typeboost-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-4] Grok 4.2 (https://www.producthunt.com/products/grok?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-5] Replit Animated Videos (https://www.producthunt.com/products/replit?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-6] OpenHunt (https://www.producthunt.com/products/openhunt?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-7] YAP (https://www.producthunt.com/products/yap-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-8] InboxAgents (https://www.producthunt.com/products/inboxagents?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-23-9] SkillForge (https://www.producthunt.com/products/skillforge-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-24-13] Quilt (https://www.producthunt.com/products/quilt-5?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-24-16] Nag Alarm AI (https://www.producthunt.com/products/nag-alarm-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-24-17] Dictato (https://www.producthunt.com/products/dictato?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-24-2] Modelence App Builder (https://www.producthunt.com/products/modelence-app-builder?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-24-3] Anima (https://www.producthunt.com/products/anima-app?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-24-8] Toggle for OpenClaw (https://www.producthunt.com/products/togglex-openclaw?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-1] Stitch by Google (https://www.producthunt.com/products/stitch-by-google?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-10] Collective OS (https://www.producthunt.com/products/collective-os?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-11] Skills for Agents (https://www.producthunt.com/products/skills-for-agents?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-14] Forum (https://www.producthunt.com/products/forum-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-15] WebMCP (https://www.producthunt.com/products/webmcp?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-17] ClawRecipes (https://www.producthunt.com/products/clawrecipes-openclaw-recipes?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-19] Scriptmine (https://www.producthunt.com/products/scriptmine-turn-trends-into-scripts?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-20] Prosaic (https://www.producthunt.com/products/prosaic?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-21] Kivicube (https://www.producthunt.com/products/kivicube?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-22] SoloGuard (https://www.producthunt.com/products/sologuard?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-23] Settle (https://www.producthunt.com/products/settle-4?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-24] Live AI Design Benchmark (https://www.producthunt.com/products/live-ai-design-benchmark?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-25] Gemma (https://www.producthunt.com/products/gemma?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-26] Dock 3.0 (https://www.producthunt.com/products/dock-developer-optimization-content-kit?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-4] Orchids 1.0 (https://www.producthunt.com/products/orchids?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-5] Liner Write (https://www.producthunt.com/products/liner-write?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-6] What YC Is Really Betting On? (https://www.producthunt.com/products/what-yc-is-really-betting-on?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-7] Bazaar V4 (https://www.producthunt.com/products/bazaar-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-8] Falconer (https://www.producthunt.com/products/falconer?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-25-9] Polsia (https://www.producthunt.com/products/polsia?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-1] KiloClaw (https://www.producthunt.com/products/kiloclaw?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-10] Orca (https://www.producthunt.com/products/orca-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-11] Mito Health (https://www.producthunt.com/products/mito-health?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-12] Thinglo (https://www.producthunt.com/products/thinglo-save-anything-lose-nothing?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-13] Pinly (https://www.producthunt.com/products/pinly-smart-location-reminders?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-14] Custom Models (https://www.producthunt.com/products/travel-animator?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-15] Synlets (https://www.producthunt.com/products/synlets?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-16] Thinklet AI (https://www.producthunt.com/products/thinklet-ai-voice-notes-with-local-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-17] Scenescroll (https://www.producthunt.com/products/scenescroll?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-18] General Legal (https://www.producthunt.com/products/general-legal?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-19] AskAIBase (https://www.producthunt.com/products/ask-7?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-2] Notion Custom Agents (https://www.producthunt.com/products/notion?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-20] GhostReply (https://www.producthunt.com/products/ghostreply-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-21] CroozLink (https://www.producthunt.com/products/croozlink?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-22] IQ | The Vibe Coders Leaderboard (https://www.producthunt.com/products/iq-the-vibe-coding-leaderboard?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-23] Simpliers Chat | DM & Comment Ops (https://www.producthunt.com/products/simpliers-chat-dm-comment-ops?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-3] Opal 2.0 by Google Labs (https://www.producthunt.com/products/google?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-4] Arzule (https://www.producthunt.com/products/arzule?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-5] Ask Fellow (https://www.producthunt.com/products/fellow-app?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-6] Mercury 2 (https://www.producthunt.com/products/mercury-412?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-7] VibePad (https://www.producthunt.com/products/vibepad?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-8] Yuma Social AI (https://www.producthunt.com/products/yuma-social-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-26-9] PeonPing (https://www.producthunt.com/products/peonping?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-1] Koidex (https://www.producthunt.com/products/koidex-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-10] Heimdall (https://www.producthunt.com/products/heimdall-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-11] Commit Please (https://www.producthunt.com/products/commit-please?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-12] CodeWords UI (https://www.producthunt.com/products/codewords?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-13] DeltaMemory (https://www.producthunt.com/products/deltamemory?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-14] Seedream 5.0 Lite (https://www.producthunt.com/products/pixeldance-seaweed?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-15] Playground by Natoma (https://www.producthunt.com/products/playground-by-natoma?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-16] Wordwand (https://www.producthunt.com/products/wordwand?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-17] Digital Twin by Read AI (https://www.producthunt.com/products/read-dashboard?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-18] Chiron (https://www.producthunt.com/products/chiron?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-19] My Texas Method (https://www.producthunt.com/products/my-texas-method?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-2] ChatPal (https://www.producthunt.com/products/chatpal-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-20] HomeBar for Homey Pro (https://www.producthunt.com/products/homebar-for-homey-pro?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-21] API Pick (https://www.producthunt.com/products/api-pick?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-22] Qwarm (https://www.producthunt.com/products/qwarm?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-23] AxKeyStore (https://www.producthunt.com/products/axkeystore?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-24] Insta Posts (https://www.producthunt.com/products/insta-posts?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-25] Loopdesk (https://www.producthunt.com/products/loopdesk?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-3] Rover by rtrvr.ai (https://www.producthunt.com/products/rtrvr-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-4] gpt-realtime-1.5 by OpenAI (https://www.producthunt.com/products/openai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-5] Tessl (https://www.producthunt.com/products/tessl?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-6] IronClaw (https://www.producthunt.com/products/ironclaw?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-7] Zavi AI - Voice to Action OS (https://www.producthunt.com/products/zavi-ai-voice-talk-to-text?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-8] OpenClawCity (https://www.producthunt.com/products/openclawcity?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-27-9] RankingSuperior (https://www.producthunt.com/products/rankingsuperior?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-1] Superset (https://www.producthunt.com/products/superset-5?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-10] MaxClaw by MiniMax (https://www.producthunt.com/products/minimax-agent?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-11] mvntSTUDIO (https://www.producthunt.com/products/mvntstudio?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-12] HelixDB (https://www.producthunt.com/products/helixdb?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-13] muno (https://www.producthunt.com/products/muno-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-14] Nix Capture (https://www.producthunt.com/products/nix-capture?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-15] Flarehawk (https://www.producthunt.com/products/flarehawk?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-16] Mirano (https://www.producthunt.com/products/mirano?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-17] BOSS.Tech Beta (https://www.producthunt.com/products/boss-tech-beta?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-18] SnapFill (https://www.producthunt.com/products/snapfill?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-19] UI Roast for Figma (https://www.producthunt.com/products/ui-roast-for-figma?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-2] Claude Code Remote Control (https://www.producthunt.com/products/claude-code-remote-access?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-20] onsa.ai (https://www.producthunt.com/products/onsa-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-21] Launch In Public (https://www.producthunt.com/products/launch-in-public?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-22] Endee.io (https://www.producthunt.com/products/endee-io?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-23] HireFlow (https://www.producthunt.com/products/hireflow-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-24] TapGPT (https://www.producthunt.com/products/tapgpt?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-25] Organic Intelligence Protocol (OIP) (https://www.producthunt.com/products/reddit?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-26] Nova CLI (https://www.producthunt.com/products/nova-cli?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-27] ClawHost.chat (https://www.producthunt.com/products/clawhost-chat?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-28] SVG Weave (https://www.producthunt.com/products/svg-weave?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-29] rule1 (https://www.producthunt.com/products/rule1?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-3] Nano Banana 2 (https://www.producthunt.com/products/nano-banana-2-11?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-30] Copana (https://www.producthunt.com/products/copana?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-4] Perplexity Computer (https://www.producthunt.com/products/perplexity-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-5] Mastra Code (https://www.producthunt.com/products/mastra?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-6] What's Up With That? (https://www.producthunt.com/products/what-s-up-with-that?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-7] Hacker News for macOS (https://www.producthunt.com/products/hacker-news-for-macos?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-8] lemonpod.ai (https://www.producthunt.com/products/lemonpod-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-28-9] Alkemi (https://www.producthunt.com/products/alkemi?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-1] Claude in Excel (https://www.producthunt.com/products/claude?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-10] Recreate by Thumblify (https://www.producthunt.com/products/thumblifyai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-11] cmux (https://www.producthunt.com/products/cmux?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-12] roomform.ai (https://www.producthunt.com/products/roomform-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-13] Flip (https://www.producthunt.com/products/flip-9?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-14] RocketShare (https://www.producthunt.com/products/rocketshare-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-15] SkillSync AI (https://www.producthunt.com/products/skillsync-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-16] Plain Markdown (https://www.producthunt.com/products/plain-markdown?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-17] DB Atelier (https://www.producthunt.com/products/db-atelier?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-18] Noteecard (https://www.producthunt.com/products/ncard?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-19] TARKK – Not-To-Do List (https://www.producthunt.com/products/tarkk-not-to-do-list?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-20] Vibes101 (https://www.producthunt.com/products/vibes101?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-21] Hooklink (https://www.producthunt.com/products/hooklink?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-22] Ollama Explorer (https://www.producthunt.com/products/ollama-explorer?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-23] Stuffolio (https://www.producthunt.com/products/stuffolio?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-24] Mentiq (https://www.producthunt.com/products/mentiq?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-25] Spin Wheel CCR (https://www.producthunt.com/products/spin-wheel-ccr?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-26] Dazzx (https://www.producthunt.com/products/dazzx?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-27] Zeer (https://www.producthunt.com/products/zeer?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-28] Zarsage AI — Early Access Waitlist (https://www.producthunt.com/products/zarsage-ai-early-access-waitlist?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-29] Aubade - AI Bird Song ID (https://www.producthunt.com/products/aubade-ai-bird-song-id?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-30] Push (https://www.producthunt.com/products/push-9?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-4] theORQL (https://www.producthunt.com/products/stop-coding-blind-ai-that-sees-the-ui?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-5] SellShots (https://www.producthunt.com/products/sellshots-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-6] PromptURLs (https://www.producthunt.com/products/prompturls?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-7] Study OS (https://www.producthunt.com/products/study-os?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-8] Surfpool (https://www.producthunt.com/products/surfpool?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-01-9] The Claw News (https://www.producthunt.com/products/the-claw-news?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
