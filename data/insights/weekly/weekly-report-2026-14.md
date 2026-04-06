# Weekly Research Report | 2026-03-30 ~ 2026-04-05

> generated_at: 2026-04-06T04:14:47Z
> k_selected: 4
> embedding_model: text-embedding-3-large
> chat_model: gpt-5.2-2025-12-11

## 1) 本周摘要  
1. 终端编码代理从“能写代码”快速走向“能编排工作流”：Codex CLI 与 Claude Code 这一代工具在终端/IDE/云端多入口铺开，同时通过 MCP/插件把外部知识库与任务系统接入，使“代码—笔记—自动化”更容易串成可复用的代理式流程。[source:github:gh-2026-04-01-6] [source:github:gh-2026-04-01-5]  
2. “语音”从 TTS/ASR 单点能力升级为工作流入口：一端是产品化的实时对话入口（Claude Code Voice Mode），另一端是可集成的结构化长音频转写与推理生态（VibeVoice 进入 Transformers、支持 vLLM），叠加低延迟多语种 TTS（Lightning V3），让语音更像可直接嵌入流程的 I/O 层。[source:producthunt:ph-2026-04-03-1] [source:github:gh-2026-03-31-3] [source:producthunt:ph-2026-04-03-2]  
3. 研究侧出现“可控生成与交互评估”的方法栈聚集：从缓解 reward hacking 的规划/训练信号设计（MONA 复现与 learned approval），到用“生成下一轮用户发言”探测交互感知的新评测范式，再到“离线生成 + 自动分析”的心理量表自动化工具链，整体指向“能衡量、能纠偏、能扩展”的智能体开发路线。[source:arxiv:ax-2026-04-01-1] [source:arxiv:ax-2026-04-03-1] [source:arxiv:ax-2026-03-31-1]  
4. 产品侧继续把 AI 从聊天框推向多入口与数据层：浏览器上下文写作（Clico）、无屏语音学习（SUN）、以及把交易分类/供应商记忆做成可持续数据层的财务工具（Jupid），共同强调“上下文 + 入口 + 数据”闭环，来换取高频持续使用。[source:producthunt:ph-2026-03-30-1] [source:producthunt:ph-2026-03-30-2] [source:producthunt:ph-2026-04-01-1]  

---

## 2) 趋势主题（4 个）  

### 主题 A：终端/CLI 编码代理与 MCP 工作流连接器加速融合  
**发生了什么（结论）**：编码代理竞争点从“模型/补全”转向“工作流层与连接能力”，即在终端中把计划、状态、技能调用、知识库读写做成可复用流程，降低团队落地门槛。[source:github:gh-2026-04-04-6]  

**Why now（动因）**：  
- 入口侧：Claude Code 与 Codex 代表了终端原生的代理交互形态，并扩展到 IDE/云端触发（如 GitHub 触发、IDE 使用等），使“开发者随时可用”成为现实基础。[source:github:gh-2026-04-01-6] [source:github:gh-2026-04-01-5]  
- 连接侧：当 MCP（例如对笔记/数据库的读写连接器）成熟后，编码代理不再只围绕代码库上下文，而是能把“规范、设计、变更记录、任务看板”一起纳入上下文与行动对象，从而自然催生“编排层/模板化实践”。（该方向在本周主题聚类中被明确强调。）[source:github:gh-2026-04-04-6]  

**代表项目对比（怎么选型）**：  
- **Claude Code**更像“终端里的全能代理”：强调理解代码库、执行任务、解释代码与处理 git 工作流，并提供可扩展插件与多入口触发方式，适合想要“从一个代理开始，逐步加插件/流程”的团队。[source:github:gh-2026-04-01-6]  
- **Codex CLI（openai/codex）**更像“轻量、到处可跑的终端代理底座”：可本地终端运行，并覆盖 VS Code/Cursor/Windsurf 等 IDE 形态与 App/Web，配置上支持 ChatGPT 登录或 API key，适合对“部署形态与接入方式”更敏感的开发者/组织。[source:github:gh-2026-04-01-5]  
- **oh-my-codex**提供“显式工作流层”：通过统一的澄清→计划→执行→持续推进范式，强调并行、团队模式、日志/状态持久化与规范化技能调用，适合已经决定采用 Codex CLI、但希望把实践标准化的团队。[source:github:gh-2026-04-04-6]  

**主要风险与治理建议（结论）**：  
- 合规与隐私：终端代理在企业内往往接触代码、Issue、凭据与业务文档；当工具存在使用数据/对话反馈收集声明时，需要明确数据边界与内控流程，避免“为了效率把合规债务堆到后面”。[source:github:gh-2026-04-01-6]  
- 密钥与权限：Codex CLI 支持 API key 配置，工作流自动化越深，密钥管理与最小权限越关键（共享开发机、CI、多人协作都可能放大风险）。[source:github:gh-2026-04-01-5]  
- 工作流复杂度：当斜杠命令、hooks、记忆、子代理、MCP 混用时，缺少模板会导致“人人都能用、没人能复现”，需要可复制的范式与治理（文档/示例库/审计）。[source:github:gh-2026-03-30-4]  

**下周观察点（结论）**：是否出现更多“标准化技能包/状态持久化/并行推进”的模板化实践，推动 CLI 代理从“个人神器”走向“团队流程组件”。[source:github:gh-2026-04-04-6]  

---

### 主题 B：面向生成式智能体的“可控生成与交互评估”方法栈  
**发生了什么（结论）**：研究社区正在补齐智能体的三块短板——（1）训练信号与规划导致的 reward hacking；（2）对话交互感知难以测量；（3）大规模生成内容如何形成“生成—分析—迭代”的工具闭环。[source:arxiv:ax-2026-04-01-1]  

**Why now（动因）**：  
- 智能体从单轮问答走向多步任务后，“短视最优/钻奖励空子”会系统性出现，促使把规划约束与更远见的 approval 信号纳入训练/评估讨论。[source:arxiv:ax-2026-04-01-1]  
- 真实交互的质量不仅取决于“助手回答得对”，还取决于是否理解用户下一步会怎么问、对话将走向何处，因此出现以“生成下一轮用户发言”作为探针的评估范式，补足传统指标的盲区。[source:arxiv:ax-2026-04-03-1]  
- 同时，LLM 在内容生产上逐渐走向“离线生成模式”：先生成、再做自动分析与筛选，以降低专家迭代与前置试测成本，这在心理测量量表开发的教程型工作中体现得更明显。[source:arxiv:ax-2026-03-31-1]  

**代表工作对比（理解差异）**：  
- **MONA 复现与 learned approval**：核心在“训练信号与规划行为的约束设计”，目标是减少 reward hacking 与短视行为，偏向“让模型别走歪”。[source:arxiv:ax-2026-04-01-1]  
- **User Turn Generation 评测**：核心在“增加一个新维度的交互感知测量”，即不直接评判助手输出，而用对话下一步的生成来检验其对互动结构的理解，偏向“让我们知道模型哪里不懂互动”。[source:arxiv:ax-2026-04-03-1]  
- **AIGENIE（生成式心理测量）**：核心在“把生成与自动分析工具化”，把专家流程拆成可自动化模块，偏向“让产出规模化且可迭代”。[source:arxiv:ax-2026-03-31-1]  

**风险与下周观察（结论）**：  
- 指标割裂风险：交互感知与传统准确率可能不同步，若产品只追单一指标可能误优化；下周值得关注是否出现把新评测维度纳入统一评估框架的后续工作。[source:arxiv:ax-2026-04-03-1]  
- 可复现与边界条件：reward-hacking 缓解方案在不同环境中的稳定性、是否引入新偏差，仍需要更多复现实验来回答；下周可关注是否出现更多环境/设置的验证与设计细化。[source:arxiv:ax-2026-04-01-1]  

---

### 主题 C：实时语音交互 + 结构化语音转写成为“工作流入口”  
**发生了什么（结论）**：语音能力本周同时在“产品入口”（实时对话）与“开发者组件”（结构化转写/推理框架）两端提速，使语音从功能点变成可接入工作流的标准输入输出层。[source:producthunt:ph-2026-04-03-1] [source:github:gh-2026-03-31-3]  

**Why now（动因）**：  
- 当实时语音对话能做到更自然的“免手操作”，语音就不只是客服/助手形态，而是可在做饭、通勤、会议、写代码等多任务场景成为新的交互入口（Claude Code Voice Mode强调语音/文本切换与按键说话）。[source:producthunt:ph-2026-04-03-1]  
- 当开源 ASR 能提供长音频、说话人/时间戳的结构化转写并进入主流推理生态（Transformers、vLLM），语音就具备“可检索、可对齐、可自动化处理”的数据形态，能直接进入笔记/任务/知识库流程。[source:github:gh-2026-03-31-3]  
- 低延迟多语种 TTS（Lightning V3 主打 100ms、15+ 语言、10 秒克隆）降低了把语音嵌进产品闭环的工程门槛，推动“语音先行”的体验迭代。[source:producthunt:ph-2026-04-03-2]  

**代表项目对比（落地路径）**：  
- **Claude Code Voice Mode**：偏“即时对话入口”，目标是把语音变成随手可用的交互方式，适合需要频繁指令/追问的场景。[source:producthunt:ph-2026-04-03-1]  
- **VibeVoice**：偏“结构化语音数据管道”，适合会议纪要、访谈转写、长音频整理与后续自动化（时间戳/说话人/长音频/多语种）。[source:github:gh-2026-03-31-3]  
- **Lightning V3**：偏“低延迟多语种输出层”，适合语音助手、IVR、内容创作等对响应速度与多语言覆盖敏感的产品形态。[source:producthunt:ph-2026-04-03-2]  

**风险与下周观察（结论）**：  
- 端到端体验不只看模型：实时链路的延迟、断连、噪声鲁棒性会直接决定“入口是否成立”；下周可关注是否出现更多真实场景反馈与落地案例。[source:producthunt:ph-2026-04-03-2]  
- 质量一致性：多语种与音色克隆的可控性仍需验证；结构化长音频在多人/长时场景的准确性与集成成本也需要持续评估。[source:github:gh-2026-03-31-3]  

---

### 主题 D：上下文感知的多入口 AI 助手与“数据层优先”产品化  
**发生了什么（结论）**：产品在把 AI 分发到浏览器、语音、桌面等入口的同时，开始补“可持续使用的数据层”，让 AI 不止能说，还能长期记、能对齐业务分类、能减少手工搬运。[source:producthunt:ph-2026-04-01-1]  

**Why now（动因）**：  
- 入口碎片化已成事实：用户在网页、邮箱、笔记、账单、学习音频等场景切换频繁，单一聊天入口难以覆盖；因此出现能读取网页上下文的浏览器扩展（Clico）与无屏语音学习入口（SUN）。[source:producthunt:ph-2026-03-30-1] [source:producthunt:ph-2026-03-30-2]  
- 仅“上下文读取”不够，必须“数据结构化并可纠错”：Jupid 把银行交易映射到税务分类并“记住供应商关系”，本质是在为 LLM/代理提供一个更稳定可调用的数据层，以换取长期复用价值。[source:producthunt:ph-2026-04-01-1]  

**代表项目对比（价值与边界）**：  
- **Clico**解决“网页上下文搬运成本”：优势是即插即用、贴近浏览器使用流；边界在于权限与跨站上下文一致性管理。[source:producthunt:ph-2026-03-30-1]  
- **SUN**解决“无屏学习的持续性”：用互动音频+随听随问提升学习粘性，并尝试结合 notes/emails 做个性化；边界在于用户授权意愿与个性化效果可验证性。[source:producthunt:ph-2026-03-30-2]  
- **Jupid**解决“业务数据标准化与记忆”：通过交易分类/供应商记忆服务报税等强结果场景；边界在于分类准确率在长周期、异常交易与纠错机制上的稳定性。[source:producthunt:ph-2026-04-01-1]  

**风险与下周观察（结论）**：多入口 + 多模型接入会把密钥、权限与数据一致性问题放大；下周可重点观察是否出现更成熟的“密钥管理/权限分层/可审计日志”产品化方案，支撑这些入口真正进入团队与高频业务流。[source:github:gh-2026-04-01-5]  

---

## 3) 项目榜单（按热度/上升/新颖综合观察）  
1. **anthropics/claude-code**：本周同时位居热度榜与上升榜前列，显示终端代理正在成为开发者主战场之一。[source:github:gh-2026-04-01-6]  
2. **microsoft/VibeVoice**：进入热度/新颖榜前列，且具备 Transformers/vLLM 等集成信号，说明“可集成的语音组件”需求在增长。[source:github:gh-2026-03-31-3]  
3. **Jupid**：在 Product Hunt 热度与上升均靠前，体现“数据层优先 + 强业务闭环（分类/报税）”更易形成真实付费与留存。[source:producthunt:ph-2026-04-01-1]  
4. **User Turn Generation 评测论文**：进入上升榜，说明业界对“交互感知如何测量”兴趣提升，可能外溢到对话产品的评估体系中。[source:arxiv:ax-2026-04-03-1]  
5. **claude-howto**：位列热度/新颖榜，侧面证明“如何把命令、hooks、记忆、子代理与工作流组合起来”仍是用户的强痛点，生态教育内容正在补位。[source:github:gh-2026-03-30-4]  

---

## 4) 关键词趋势（从项目侧“可证据化”解读）  
1. **voice / speech / 实时语音**成为最强势的共同线索：一端是实时语音对话入口（Claude Code Voice Mode），另一端是结构化转写与多语种 ASR 组件（VibeVoice），再加上低延迟 TTS（Lightning V3），构成“输入—理解—输出”的完整链路。[source:producthunt:ph-2026-04-03-1] [source:github:gh-2026-03-31-3] [source:producthunt:ph-2026-04-03-2]  
2. **planning**升温更多来自“可靠性与安全”语境：MONA 相关工作把规划与训练信号绑定讨论，说明规划不再只是提升能力，也被视为降低 reward hacking 风险的关键控制点。[source:arxiv:ax-2026-04-01-1]  
3. **notes**正在与编码/语音两条线汇合：SUN 强调结合 notes/emails 的个性化学习；而“编码代理 + 工作流层”则把计划/日志/状态持久化当作落地刚需，notes 逐渐从“记事”变成“可执行上下文”。[source:producthunt:ph-2026-03-30-2] [source:github:gh-2026-04-04-6]  
4. **api keys**的存在感上升意味着“从试用到集成”阶段在扩大：Codex CLI 支持 API key 配置并面向终端自动化使用，密钥治理与权限边界会成为更多团队的现实问题。[source:github:gh-2026-04-01-5]  
5. **自动分析**在研究侧更突出：AIGENIE 把量表开发拆为可自动化的生成与分析流程，体现“先生成再筛选/评估”的离线流水线范式正在渗透更多领域。[source:arxiv:ax-2026-03-31-1]  

---

## 5) 交叉来源观察（GitHub × Product Hunt × arXiv）  
1. **“语音工作流入口”同时在开源与产品端加速**：开源侧给出可集成的结构化转写与推理生态（VibeVoice），产品侧给出即时可用的语音对话入口（Claude Code Voice Mode、Lightning V3 的低延迟 TTS 能力），两者合流意味着下一个竞争点可能是“谁能把语音接入任务/笔记/代码的闭环做得更顺”。[source:github:gh-2026-03-31-3] [source:producthunt:ph-2026-04-03-1]  
2. **“终端编码代理 + 工作流连接器”跨平台共振**：GitHub 上 Claude Code、Codex CLI 与 oh-my-codex 代表了工具本体与工作流层的组合趋势，而生态教育内容（claude-howto）同步走热，说明用户需求已从“有没有”转向“怎么稳定用、怎么团队化用”。[source:github:gh-2026-04-01-6] [source:github:gh-2026-04-04-6] [source:github:gh-2026-03-30-4]  
3. **研究侧的评测/对齐议题可能反哺产品指标**：User Turn Generation 提供交互感知测量视角；若被产品团队吸收，可能带来“对话体验”新的可量化指标，从而影响语音助手、编码代理等交互密集型产品的迭代方式。[source:arxiv:ax-2026-04-03-1]  

---

## 6) 下周预测（可验证的观察清单）  
1. **CLI 代理将出现更多“可复制工作流模板”与团队化实践**：围绕计划/状态持久化、并行推进、规范化技能调用的工作流层可能继续增多，重点看是否形成事实标准（配置、目录结构、日志与审计习惯）。[source:github:gh-2026-04-04-6]  
2. **语音入口会从“能聊”转向“能产出结构化结果”**：长音频结构化转写（说话人/时间戳）若与笔记/任务系统结合，会出现更多“会议→行动项/PRD→任务分解”的落地案例；可关注 VibeVoice 的进一步采用与集成项目增长。[source:github:gh-2026-03-31-3]  
3. **“交互感知”可能成为对话产品的新评测维度**：如果 user-turn generation 的探针方法被更多人引用/复现，产品侧可能开始把它用于回归测试或 A/B 评估，以解释“准确但不好用”的问题来源。[source:arxiv:ax-2026-04-03-1]  
4. **密钥与权限治理会从隐性痛点变成显性卖点**：随着多入口、多模型接入、终端自动化加深，API keys 的安全托管、最小权限、可审计日志更可能被包装成独立能力或最佳实践被广泛传播。[source:github:gh-2026-04-01-5]

## 引用索引

- [arxiv:ax-2026-03-31-1] The Ultimate Tutorial for AI-driven Scale Development in Generative Psychometrics: Releasing AIGENIE from its Bottle (https://arxiv.org/abs/2603.28643v1)
- [arxiv:ax-2026-03-31-10] FlowIt: Global Matching for Optical Flow with Confidence-Guided Refinement (https://arxiv.org/abs/2603.28759v1)
- [arxiv:ax-2026-03-31-11] SonoWorld: From One Image to a 3D Audio-Visual Scene (https://arxiv.org/abs/2603.28757v1)
- [arxiv:ax-2026-03-31-12] DreamLite: A Lightweight On-Device Unified Model for Image Generation and Editing (https://arxiv.org/abs/2603.28713v1)
- [arxiv:ax-2026-03-31-13] Why Aggregate Accuracy is Inadequate for Evaluating Fairness in Law Enforcement Facial Recognition Systems (https://arxiv.org/abs/2603.28675v1)
- [arxiv:ax-2026-03-31-14] Sim-to-Real Fruit Detection Using Synthetic Data: Quantitative Evaluation and Embedded Deployment with Isaac Sim (https://arxiv.org/abs/2603.28670v1)
- [arxiv:ax-2026-03-31-15] Industrial3D: A Terrestrial LiDAR Point Cloud Dataset and CrossParadigm Benchmark for Industrial Infrastructure (https://arxiv.org/abs/2603.28660v1)
- [arxiv:ax-2026-03-31-16] TGIF2: Extended Text-Guided Inpainting Forgery Dataset & Benchmark (https://arxiv.org/abs/2603.28613v1)
- [arxiv:ax-2026-03-31-17] Unsafe2Safe: Controllable Image Anonymization for Downstream Utility (https://arxiv.org/abs/2603.28605v1)
- [arxiv:ax-2026-03-31-18] ELViS: Efficient Visual Similarity from Local Descriptors that Generalizes Across Domains (https://arxiv.org/abs/2603.28603v1)
- [arxiv:ax-2026-03-31-19] Geometry-aware similarity metrics for neural representations on Riemannian and statistical manifolds (https://arxiv.org/abs/2603.28764v1)
- [arxiv:ax-2026-03-31-2] Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning (https://arxiv.org/abs/2603.28618v1)
- [arxiv:ax-2026-03-31-20] Temporal Credit Is Free (https://arxiv.org/abs/2603.28750v1)
- [arxiv:ax-2026-03-31-21] Stop Probing, Start Coding: Why Linear Probes and Sparse Autoencoders Fail at Compositional Generalisation (https://arxiv.org/abs/2603.28744v1)
- [arxiv:ax-2026-03-31-22] Expectation Error Bounds for Transfer Learning in Linear Regression and Linear Neural Networks (https://arxiv.org/abs/2603.28739v1)
- [arxiv:ax-2026-03-31-23] See it to Place it: Evolving Macro Placements with Vision-Language Models (https://arxiv.org/abs/2603.28733v1)
- [arxiv:ax-2026-03-31-24] Stepwise Credit Assignment for GRPO on Flow-Matching Models (https://arxiv.org/abs/2603.28718v1)
- [arxiv:ax-2026-03-31-25] GPU-Accelerated Optimization of Transformer-Based Neural Networks for Real-Time Inference (https://arxiv.org/abs/2603.28708v1)
- [arxiv:ax-2026-03-31-26] Subspace Optimization for Backpropagation-Free Continual Test-Time Adaptation (https://arxiv.org/abs/2603.28678v1)
- [arxiv:ax-2026-03-31-27] FL-PBM: Pre-Training Backdoor Mitigation for Federated Learning (https://arxiv.org/abs/2603.28673v1)
- [arxiv:ax-2026-03-31-28] AMIGO: Agentic Multi-Image Grounding Oracle Benchmark (https://arxiv.org/abs/2603.28662v1)
- [arxiv:ax-2026-03-31-29] Information-Theoretic Limits of Safety Verification for Self-Improving Systems (https://arxiv.org/abs/2603.28650v1)
- [arxiv:ax-2026-03-31-3] Adaptive Block-Scaled Data Types (https://arxiv.org/abs/2603.28765v1)
- [arxiv:ax-2026-03-31-30] LACE: Loss-Adaptive Capacity Expansion for Continual Learning (https://arxiv.org/abs/2603.28611v1)
- [arxiv:ax-2026-03-31-4] EpiScreen: Early Epilepsy Detection from Electronic Health Records with Large Language Models (https://arxiv.org/abs/2603.28698v1)
- [arxiv:ax-2026-03-31-5] Gen-Searcher: Reinforcing Agentic Search for Image Generation (https://arxiv.org/abs/2603.28767v1)
- [arxiv:ax-2026-03-31-6] HandX: Scaling Bimanual Motion and Interaction Generation (https://arxiv.org/abs/2603.28766v1)
- [arxiv:ax-2026-03-31-7] PoseDreamer: Scalable and Photorealistic Human Data Generation Pipeline with Diffusion Models (https://arxiv.org/abs/2603.28763v1)
- [arxiv:ax-2026-03-31-8] On-the-fly Repulsion in the Contextual Space for Rich Diversity in Diffusion Transformers (https://arxiv.org/abs/2603.28762v1)
- [arxiv:ax-2026-03-31-9] SHOW3D: Capturing Scenes of 3D Hands and Objects in the Wild (https://arxiv.org/abs/2603.28760v1)
- [arxiv:ax-2026-04-01-1] Extending MONA in Camera Dropbox: Reproduction, Learned Approval, and Design Implications for Reward-Hacking Mitigation (https://arxiv.org/abs/2603.29993v1)
- [arxiv:ax-2026-04-01-10] Benchmarking PhD-Level Coding in 3D Geometric Computer Vision (https://arxiv.org/abs/2603.30038v1)
- [arxiv:ax-2026-04-01-11] Conditional Polarization Guidance for Camouflaged Object Detection (https://arxiv.org/abs/2603.30008v1)
- [arxiv:ax-2026-04-01-12] SurgNavAR: An Augmented Reality Surgical Navigation Framework for Optical See-Through Head Mounted Displays (https://arxiv.org/abs/2603.29990v1)
- [arxiv:ax-2026-04-01-13] Trimodal Deep Learning for Glioma Survival Prediction: A Feasibility Study Integrating Histopathology, Gene Expression, and MRI (https://arxiv.org/abs/2603.29968v1)
- [arxiv:ax-2026-04-01-14] Learning Structural-Functional Brain Representations through Multi-Scale Adaptive Graph Attention for Cognitive Insight (https://arxiv.org/abs/2603.29967v1)
- [arxiv:ax-2026-04-01-15] Scaling Video Pretraining for Surgical Foundation Models (https://arxiv.org/abs/2603.29966v1)
- [arxiv:ax-2026-04-01-16] NeuroBRIDGE: Behavior-Conditioned Koopman Dynamics with Riemannian Alignment for Early Substance Use Initiation Prediction from Longitudinal Functional Connectome (https://arxiv.org/abs/2603.29960v1)
- [arxiv:ax-2026-04-01-17] Detecting Unknown Objects via Energy-based Separation for Open World Object Detection (https://arxiv.org/abs/2603.29954v1)
- [arxiv:ax-2026-04-01-18] EC-Bench: Enumeration and Counting Benchmark for Ultra-Long Videos (https://arxiv.org/abs/2603.29943v1)
- [arxiv:ax-2026-04-01-19] Better than Average: Spatially-Aware Aggregation of Segmentation Uncertainty Improves Downstream Performance (https://arxiv.org/abs/2603.29941v1)
- [arxiv:ax-2026-04-01-2] Structured Intent as a Protocol-Like Communication Layer: Cross-Model Robustness, Framework Comparison, and the Weak-Model Compensation Effect (https://arxiv.org/abs/2603.29953v1)
- [arxiv:ax-2026-04-01-20] Gloria: Consistent Character Video Generation via Content Anchors (https://arxiv.org/abs/2603.29931v1)
- [arxiv:ax-2026-04-01-21] End-to-End Image Compression with Segmentation Guided Dual Coding for Wind Turbines (https://arxiv.org/abs/2603.29927v1)
- [arxiv:ax-2026-04-01-22] Abstraction in Style (https://arxiv.org/abs/2603.29924v1)
- [arxiv:ax-2026-04-01-23] Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought? (https://arxiv.org/abs/2603.30036v1)
- [arxiv:ax-2026-04-01-24] Reward-Based Online LLM Routing via NeuralUCB (https://arxiv.org/abs/2603.30035v1)
- [arxiv:ax-2026-04-01-25] Tucker Attention: A generalization of approximate attention mechanisms (https://arxiv.org/abs/2603.30033v1)
- [arxiv:ax-2026-04-01-26] Tracking Equivalent Mechanistic Interpretations Across Neural Networks (https://arxiv.org/abs/2603.30002v1)
- [arxiv:ax-2026-04-01-27] Aligning Validation with Deployment: Target-Weighted Cross-Validation for Spatial Prediction (https://arxiv.org/abs/2603.29981v1)
- [arxiv:ax-2026-04-01-28] Quantifying Cross-Modal Interactions in Multimodal Glioma Survival Prediction via InterSHAP: Evidence for Additive Signal Integration (https://arxiv.org/abs/2603.29977v1)
- [arxiv:ax-2026-04-01-29] Meteorology-Driven GPT4AP: A Multi-Task Forecasting LLM for Atmospheric Air Pollution in Data-Scarce Settings (https://arxiv.org/abs/2603.29974v1)
- [arxiv:ax-2026-04-01-3] Physiological and Semantic Patterns in Medical Teams Using an Intelligent Tutoring System (https://arxiv.org/abs/2603.29950v1)
- [arxiv:ax-2026-04-01-30] Real-Time Explanations for Tabular Foundation Models (https://arxiv.org/abs/2603.29946v1)
- [arxiv:ax-2026-04-01-4] ScoringBench: A Benchmark for Evaluating Tabular Foundation Models with Proper Scoring Rules (https://arxiv.org/abs/2603.29928v1)
- [arxiv:ax-2026-04-01-5] ContextClaim: A Context-Driven Paradigm for Verifiable Claim Detection (https://arxiv.org/abs/2603.30025v1)
- [arxiv:ax-2026-04-01-6] Enhancing Structural Mapping with LLM-derived Abstractions for Analogical Reasoning in Narratives (https://arxiv.org/abs/2603.29997v1)
- [arxiv:ax-2026-04-01-7] Rewrite the News: Tracing Editorial Reuse Across News Agencies (https://arxiv.org/abs/2603.29937v1)
- [arxiv:ax-2026-04-01-8] OmniRoam: World Wandering via Long-Horizon Panoramic Video Generation (https://arxiv.org/abs/2603.30045v1)
- [arxiv:ax-2026-04-01-9] Video Models Reason Early: Exploiting Plan Commitment for Maze Solving (https://arxiv.org/abs/2603.30043v1)
- [arxiv:ax-2026-04-03-1] Beyond the Assistant Turn: User Turn Generation as a Probe of Interaction Awareness in Language Models (https://arxiv.org/abs/2604.02315v1)
- [arxiv:ax-2026-04-03-10] No Single Best Model for Diversity: Learning a Router for Sample Diversity (https://arxiv.org/abs/2604.02319v1)
- [arxiv:ax-2026-04-03-11] CV-18 NER: Augmented Common Voice for Named Entity Recognition from Arabic Speech (https://arxiv.org/abs/2604.02209v1)
- [arxiv:ax-2026-04-03-13] EventHub: Data Factory for Generalizable Event-Based Stereo Networks without Active Sensors (https://arxiv.org/abs/2604.02331v1)
- [arxiv:ax-2026-04-03-18] A Simple Baseline for Streaming Video Understanding (https://arxiv.org/abs/2604.02317v1)
- [arxiv:ax-2026-04-03-19] VOID: Video Object and Interaction Deletion (https://arxiv.org/abs/2604.02296v1)
- [arxiv:ax-2026-04-03-20] Modular Energy Steering for Safe Text-to-Image Generation with Foundation Models (https://arxiv.org/abs/2604.02265v1)
- [arxiv:ax-2026-04-03-21] SPAR: Single-Pass Any-Resolution ViT for Open-vocabulary Segmentation (https://arxiv.org/abs/2604.02252v1)
- [arxiv:ax-2026-04-03-23] SCALE: Semantic- and Confidence-Aware Conditional Variational Autoencoder for Zero-shot Skeleton-based Action Recognition (https://arxiv.org/abs/2604.02222v1)
- [arxiv:ax-2026-04-03-25] Taming the Exponential: A Fast Softmax Surrogate for Integer-Native Edge Inference (https://arxiv.org/abs/2604.02292v1)
- [arxiv:ax-2026-04-03-27] Smoothing the Landscape: Causal Structure Learning via Diffusion Denoising Objectives (https://arxiv.org/abs/2604.02250v1)
- [arxiv:ax-2026-04-03-29] LEO: Graph Attention Network based Hybrid Multi Sensor Extended Object Fusion and Tracking for Autonomous Driving Applications (https://arxiv.org/abs/2604.02206v1)
- [arxiv:ax-2026-04-03-30] On the Role of Depth in the Expressivity of RNNs (https://arxiv.org/abs/2604.02201v1)
- [arxiv:ax-2026-04-03-6] Answering the Wrong Question: Reasoning Trace Inversion for Abstention in LLMs (https://arxiv.org/abs/2604.02230v1)
- [arxiv:ax-2026-04-03-7] When to ASK: Uncertainty-Gated Language Assistance for Reinforcement Learning (https://arxiv.org/abs/2604.02226v1)
- [arxiv:ax-2026-04-04-12] Neuro-RIT: Neuron-Guided Instruction Tuning for Robust Retrieval-Augmented Language Model (https://arxiv.org/abs/2604.02194v1)
- [arxiv:ax-2026-04-04-14] Modulate-and-Map: Crossmodal Feature Mapping with Cross-View Modulation for 3D Anomaly Detection (https://arxiv.org/abs/2604.02328v1)
- [arxiv:ax-2026-04-04-15] Steerable Visual Representations (https://arxiv.org/abs/2604.02327v1)
- [arxiv:ax-2026-04-04-16] Beyond Referring Expressions: Scenario Comprehension Visual Grounding (https://arxiv.org/abs/2604.02323v1)
- [arxiv:ax-2026-04-04-17] Large-scale Codec Avatars: The Unreasonable Effectiveness of Large-scale Avatar Pretraining (https://arxiv.org/abs/2604.02320v1)
- [arxiv:ax-2026-04-04-2] Novel Memory Forgetting Techniques for Autonomous AI Agents: Balancing Relevance and Efficiency (https://arxiv.org/abs/2604.02280v1)
- [arxiv:ax-2026-04-04-22] UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models (https://arxiv.org/abs/2604.02241v1)
- [arxiv:ax-2026-04-04-24] go-$m$HC: Direct Parameterization of Manifold-Constrained Hyper-Connections via Generalized Orthostochastic Matrices (https://arxiv.org/abs/2604.02309v1)
- [arxiv:ax-2026-04-04-26] Model-Based Reinforcement Learning for Control under Time-Varying Dynamics (https://arxiv.org/abs/2604.02260v1)
- [arxiv:ax-2026-04-04-28] Universal Hypernetworks for Arbitrary Models (https://arxiv.org/abs/2604.02215v1)
- [arxiv:ax-2026-04-04-3] The Self Driving Portfolio: Agentic Architecture for Institutional Asset Management (https://arxiv.org/abs/2604.02279v1)
- [arxiv:ax-2026-04-04-4] De Jure: Iterative LLM Self-Refinement for Structured Extraction of Regulatory Rules (https://arxiv.org/abs/2604.02276v1)
- [arxiv:ax-2026-04-04-5] Do Emotions in Prompts Matter? Effects of Emotional Framing on Large Language Models (https://arxiv.org/abs/2604.02236v1)
- [arxiv:ax-2026-04-04-8] Blinded Radiologist and LLM-Based Evaluation of LLM-Generated Japanese Translations of Chest CT Reports: Comparative Study (https://arxiv.org/abs/2604.02207v1)
- [arxiv:ax-2026-04-04-9] From High-Dimensional Spaces to Verifiable ODD Coverage for Safety-Critical AI-based Systems (https://arxiv.org/abs/2604.02198v1)
- [github:gh-2026-03-30-1] fastfetch-cli/fastfetch (https://github.com/fastfetch-cli/fastfetch)
- [github:gh-2026-03-30-4] luongnv89/claude-howto (https://github.com/luongnv89/claude-howto)
- [github:gh-2026-03-30-5] hacksider/Deep-Live-Cam (https://github.com/hacksider/Deep-Live-Cam)
- [github:gh-2026-03-30-6] OpenBB-finance/OpenBB (https://github.com/OpenBB-finance/OpenBB)
- [github:gh-2026-03-30-9] Yeachan-Heo/oh-my-claudecode (https://github.com/Yeachan-Heo/oh-my-claudecode)
- [github:gh-2026-03-31-11] neovim/neovim (https://github.com/neovim/neovim)
- [github:gh-2026-03-31-3] microsoft/VibeVoice (https://github.com/microsoft/VibeVoice)
- [github:gh-2026-03-31-4] NousResearch/hermes-agent (https://github.com/NousResearch/hermes-agent)
- [github:gh-2026-03-31-5] PaddlePaddle/PaddleOCR (https://github.com/PaddlePaddle/PaddleOCR)
- [github:gh-2026-03-31-7] OpenBMB/ChatDev (https://github.com/OpenBMB/ChatDev)
- [github:gh-2026-03-31-8] obra/superpowers (https://github.com/obra/superpowers)
- [github:gh-2026-03-31-9] Dimillian/Skills (https://github.com/Dimillian/Skills)
- [github:gh-2026-04-01-1] shanraisshan/claude-code-best-practice (https://github.com/shanraisshan/claude-code-best-practice)
- [github:gh-2026-04-01-5] openai/codex (https://github.com/openai/codex)
- [github:gh-2026-04-01-6] anthropics/claude-code (https://github.com/anthropics/claude-code)
- [github:gh-2026-04-03-1] onyx-dot-app/onyx (https://github.com/onyx-dot-app/onyx)
- [github:gh-2026-04-03-2] google-research/timesfm (https://github.com/google-research/timesfm)
- [github:gh-2026-04-04-4] sherlock-project/sherlock (https://github.com/sherlock-project/sherlock)
- [github:gh-2026-04-04-5] block/goose (https://github.com/block/goose)
- [github:gh-2026-04-04-6] Yeachan-Heo/oh-my-codex (https://github.com/Yeachan-Heo/oh-my-codex)
- [github:gh-2026-04-05-1] telegramdesktop/tdesktop (https://github.com/telegramdesktop/tdesktop)
- [github:gh-2026-04-05-3] microsoft/agent-framework (https://github.com/microsoft/agent-framework)
- [producthunt:ph-2026-03-30-1] Clico (https://www.producthunt.com/products/clico?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-10] CodingPrep (https://www.producthunt.com/products/codingprep?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-11] VibecodedHub (https://www.producthunt.com/products/vibecodedhub?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-12] Struere (https://www.producthunt.com/products/struere?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-13] talk. (https://www.producthunt.com/products/talk-6?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-14] GetNextRole (https://www.producthunt.com/products/getnextrole?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-15] PackGoat (https://www.producthunt.com/products/packgoat?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-16] Compeddit — Reddit Competitor Monitor (https://www.producthunt.com/products/compeddit-reddit-competitor-monitor?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-17] GitWhy (https://www.producthunt.com/products/gitwhy?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-18] Shatranj.live (https://www.producthunt.com/products/shatranj-live?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-19] Easy Quran AI (https://www.producthunt.com/products/easy-quran-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-2] SUN (https://www.producthunt.com/products/sun-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-20] DESIGNmd (https://www.producthunt.com/products/designmd?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-21] Runa AI (https://www.producthunt.com/products/runa-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-22] PromptGPT by VosuAI (https://www.producthunt.com/products/promptgpt-by-vosuai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-23] Every Minute A Startup (https://www.producthunt.com/products/every-minute-a-startup?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-24] HolyStitch (https://www.producthunt.com/products/holystitch?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-25] Daily Diary: Void (https://www.producthunt.com/products/daily-diary-void?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-26] MyFreelancerMate (https://www.producthunt.com/products/myfreelancermate?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-27] DailyDoze - Learn Daily (https://www.producthunt.com/products/dailydoze-learn-daily?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-28] ResumeChiefz (https://www.producthunt.com/products/resumechiefz?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-29] Elleven AI 26 (https://www.producthunt.com/products/elleven-ai-26?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-3] Sheet Ninja (https://www.producthunt.com/products/sheet-ninja-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-30] WartungsPlaner (https://www.producthunt.com/products/wartungsplaner?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-4] Google Search Live (https://www.producthunt.com/products/google-search-live?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-5] Parallel Code (https://www.producthunt.com/products/parallel-code?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-6] Cline Kanban (https://www.producthunt.com/products/cline-4?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-7] Peopling (https://www.producthunt.com/products/peopling?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-8] Pensieve (https://www.producthunt.com/products/pensieve-5?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-30-9] GuideYou (https://www.producthunt.com/products/guideyou?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-1] Notion MCP (https://www.producthunt.com/products/notion-mcp?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-10] Git Blog (https://www.producthunt.com/products/git-blog?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-12] Streva (https://www.producthunt.com/products/streva?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-13] dictate. (https://www.producthunt.com/products/dictate?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-14] Neuralingo Language Learning (https://www.producthunt.com/products/neuralingo-language-learning?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-15] Halo Vision Headphones (https://www.producthunt.com/products/halo-headphones?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-16] Diploi (https://www.producthunt.com/products/diploi?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-17] MulmoChat (https://www.producthunt.com/products/mulmochat?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-18] nCompass AI Assistant (https://www.producthunt.com/products/ncompass-tech?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-19] AISpace (https://www.producthunt.com/products/aispace?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-2] PopTask (https://www.producthunt.com/products/poptask-menu-bar-task-manager?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-20] Kickker AI (https://www.producthunt.com/products/kickker-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-21] Pine AI (https://www.producthunt.com/products/pine-ai-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-22] Signagio (https://www.producthunt.com/products/signagio?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-23] RankResume (https://www.producthunt.com/products/rankresume?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-24] blockd (https://www.producthunt.com/products/blockd?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-25] SabaiHealth (https://www.producthunt.com/products/sabai-health?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-26] Workflow Builder (https://www.producthunt.com/products/aligno-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-27] StartUpOS (https://www.producthunt.com/products/startupos-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-28] Spinner Verbs (https://www.producthunt.com/products/spinner-verbs?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-29] Migraine Tap (https://www.producthunt.com/products/migraine-tap?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-3] Letterbook (https://www.producthunt.com/products/letterbook?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-30] Brainalyse (https://www.producthunt.com/products/brainalyse?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-4] Goals (https://www.producthunt.com/products/goals?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-5] FreeCAD 1.1 (https://www.producthunt.com/products/freecad-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-6] Invoke (https://www.producthunt.com/products/invoke-studio?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-7] Bluor AI (https://www.producthunt.com/products/bluor-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-8] Ollang DX (https://www.producthunt.com/products/ollang-mcp-skills-sdk-api?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-31-9] Blood Sugar Journal (https://www.producthunt.com/products/blood-sugar-journal?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-1] Jupid (https://www.producthunt.com/products/jupid?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-11] Unify (https://www.producthunt.com/products/unify-5?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-12] UNCHIKUN (https://www.producthunt.com/products/unchikun-poop-tracker?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-13] IndieEvent (https://www.producthunt.com/products/indieevent?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-14] JobFlow (https://www.producthunt.com/products/jobflow-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-15] Planana AI (https://www.producthunt.com/products/planana-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-16] MacMonitor (https://www.producthunt.com/products/macmonitor?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-17] Autoclaw (https://www.producthunt.com/products/autoclaw?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-18] GetWella (https://www.producthunt.com/products/getwella?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-19] Geer (https://www.producthunt.com/products/geer?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-2] Computer Use in Claude Code (https://www.producthunt.com/products/claude?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-20] Reframe (https://www.producthunt.com/products/reframe-carousel-designer-for-creators?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-21] OpenClawCloud (https://www.producthunt.com/products/openclawcloud?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-22] Cosmic Team Agents (https://www.producthunt.com/products/cosmic?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-23] Relacan (https://www.producthunt.com/products/relacan?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-24] Arlopass (https://www.producthunt.com/products/arlopass?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-25] Codync (https://www.producthunt.com/products/codync?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-26] HoneyComb (https://www.producthunt.com/products/ai-powered-form-that-fills-itself?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-27] LobeHub IM Integration (https://www.producthunt.com/products/lobehub?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-28] Dictura (https://www.producthunt.com/products/dictura?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-29] Gallifai (https://www.producthunt.com/products/gallifai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-3] Pixero AI (https://www.producthunt.com/products/pixero-ai-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-30] Mux: Auto Network Switch (https://www.producthunt.com/products/mux-auto-network-switch?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-4] Solvea (https://www.producthunt.com/products/solvea?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-5] Perplexity API Platform (https://www.producthunt.com/products/perplexity-api-platform?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-6] Viktor for Media Buyers (https://www.producthunt.com/products/viktor?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-7] Stamp (https://www.producthunt.com/products/stamp-4?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-8] Metabase Data Studio (https://www.producthunt.com/products/metabase?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-01-9] Google Ads MCP Server (https://www.producthunt.com/products/google-ads-mcp-server?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-1] Claude Code Voice Mode (https://www.producthunt.com/products/claude-code-voice-mode?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-10] Wan 2.7-Image (https://www.producthunt.com/products/wan-2-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-11] Syncly Social (https://www.producthunt.com/products/syncly?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-12] Roger AI (https://www.producthunt.com/products/roger-ai-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-13] Mode AI (https://www.producthunt.com/products/mode-ai-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-14] OpenYak (https://www.producthunt.com/products/openyak?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-15] Grok 4.2 Beta 2 (https://www.producthunt.com/products/grok-4-2-beta-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-16] Atomic (https://www.producthunt.com/products/atomic-5?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-17] DemoVeil (https://www.producthunt.com/products/demoveil?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-18] Flowith Canvas (https://www.producthunt.com/products/flowith?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-19] Cushion (https://www.producthunt.com/products/cushion-5?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-2] Lightning V3 (https://www.producthunt.com/products/smallest-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-20] Chunk (https://www.producthunt.com/products/chunk-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-21] Raise Your Vibe: Daily Wisdom (https://www.producthunt.com/products/daily-wisdom-raise-your-vibe?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-22] WP Copilot (https://www.producthunt.com/products/wp-copilot?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-23] neonagent.ai (https://www.producthunt.com/products/ai-community-manager?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-24] Trending Now (https://www.producthunt.com/products/ads-research?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-25] Leap (https://www.producthunt.com/products/leap-investor-matching-for-startups?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-26] BeigeCRM (https://www.producthunt.com/products/beigecrm-v1?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-27] Sendkit (https://www.producthunt.com/products/sendkit?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-28] BrainLens (https://www.producthunt.com/products/brainlens?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-29] ScreenshotBro Mac App (https://www.producthunt.com/products/screenshotbro-mac-app?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-3] Denovo (https://www.producthunt.com/products/denovo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-30] Marketrix User Testing Agent (https://www.producthunt.com/products/marketrix-user-testing-agent?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-4] GLM-5V-Turbo (https://www.producthunt.com/products/z-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-5] Cosyra (https://www.producthunt.com/products/cosyra?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-6] Mngr (https://www.producthunt.com/products/imbue-7?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-7] tama96 (https://www.producthunt.com/products/tama96-desktop-terminal-ai-pet?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-8] Nitro by Rocketlane (https://www.producthunt.com/products/rocketlane?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-03-9] Mac Pet (https://www.producthunt.com/products/mac-pet?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-1] Google Gemma 4 (https://www.producthunt.com/products/google-gemma?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-10] SlapWindows (https://www.producthunt.com/products/slapwindows?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-11] Gerri (https://www.producthunt.com/products/gerri?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-12] Mesh LLM (https://www.producthunt.com/products/mesh-llm?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-13] FindThem (https://www.producthunt.com/products/findthem?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-14] Turn It Gen Z (https://www.producthunt.com/products/turn-it-gen-z?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-15] Duck, Duck, Duck! by IDEO (https://www.producthunt.com/products/duck-duck-duck-by-ideo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-16] MAI-Transcribe-1 (https://www.producthunt.com/products/mai-image-2-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-17] Side Reminder (https://www.producthunt.com/products/side-reminder?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-18] Trinity-Large-Thinking by Arcee (https://www.producthunt.com/products/trinity-large-thinking-by-arcee-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-19] HoloTutor by VictoryXR (https://www.producthunt.com/products/holotutor-by-victoryxr?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-2] ZooClaw (https://www.producthunt.com/products/zooclaw?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-20] Package Mate (https://www.producthunt.com/products/package-mate-open-source-cli-for-macos?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-21] Lenz (https://www.producthunt.com/products/lenz-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-22] Garden (https://www.producthunt.com/products/garden-6?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-23] Claude Marketers (https://www.producthunt.com/products/claude-marketers?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-24] RebootMate: Brain Rewire & PMO (https://www.producthunt.com/products/rebootmate?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-25] ReplyMate (https://www.producthunt.com/products/replymate-ai-email-replies?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-26] UPDF 2.5 (https://www.producthunt.com/products/updf-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-27] DMdaddy (https://www.producthunt.com/products/dmdaddy?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-28] UX Mind (https://www.producthunt.com/products/ux-mind-design-research-plan-generator?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-29] Wiplash.ai (https://www.producthunt.com/products/wiplash-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-3] Cursor 3 (https://www.producthunt.com/products/cursor-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-30] Kordis (https://www.producthunt.com/products/kordis?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-4] VoiceOS (https://www.producthunt.com/products/voiceos?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-5] NotebookLM Custom Infographic Styles (https://www.producthunt.com/products/notebooklm-custom-infographic-styles?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-6] Straude (https://www.producthunt.com/products/straude?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-7] Qwen3.6-Plus (https://www.producthunt.com/products/qwen3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-8] ChatGPT on CarPlay (https://www.producthunt.com/products/openai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-04-9] Otto by Audos.com (https://www.producthunt.com/products/socap?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-1] Google Vids 2.0 (https://www.producthunt.com/products/google?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-10] GradPipe Delta (https://www.producthunt.com/products/gradpipe?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-11] WTMF AI (What's The Matter, Friend?) (https://www.producthunt.com/products/wtmf-ai-what-s-the-matter-friend?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-12] FraudGuard‑Fraud Prevention for Shopify (https://www.producthunt.com/products/fraudguard-fraud-prevention-for-shopify?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-13] The MCP Server for MCP Servers by Stork (https://www.producthunt.com/products/the-mcp-server-for-mcp-servers-by-stork?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-14] Bible App For Everyone (https://www.producthunt.com/products/bible-app-for-everyone?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-15] NestChat (https://www.producthunt.com/products/nestchat?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-16] ClawFace (https://www.producthunt.com/products/clawface?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-17] Between Ventures (https://www.producthunt.com/products/between-ventures?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-18] Nestly (https://www.producthunt.com/products/nestly?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-19] TuBoost (https://www.producthunt.com/products/tuboost?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-2] Mercury Edit 2 (https://www.producthunt.com/products/mercury-412?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-20] Glimpse (https://www.producthunt.com/products/glimpse-14?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-21] Factory Floor (https://www.producthunt.com/products/factory-floor?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-22] Agentikus (https://www.producthunt.com/products/agentikus?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-23] Mazel (https://www.producthunt.com/products/mazel?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-24] Neuro OS (https://www.producthunt.com/products/neuro-os?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-25] ContribOS (https://www.producthunt.com/products/contribos?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-26] Pinboard (https://www.producthunt.com/products/pinboard-5?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-27] Greet Gems (https://www.producthunt.com/products/greet-gems?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-28] Learn AI on your Terminal (https://www.producthunt.com/products/learn-ai-on-your-terminal?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-29] HeartBLE for Apple Watch (https://www.producthunt.com/products/heartble-for-apple-watch?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-3] Open Claude in Chrome (https://www.producthunt.com/products/open-claude-in-chrome?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-30] Montessori Parent Guide (https://www.producthunt.com/products/montessori-parent-guide?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-4] Vista (https://www.producthunt.com/products/vista-4?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-5] APImage (https://www.producthunt.com/products/apimage?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-6] Klick AI Camera Assistant (https://www.producthunt.com/products/klick-1-ai-camera-assistant?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-7] OpenGyver (https://www.producthunt.com/products/opengyver?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-8] Fluently (https://www.producthunt.com/products/fluently-accurate-youtube-subtitles?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-04-05-9] Clovr (https://www.producthunt.com/products/clovr?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
