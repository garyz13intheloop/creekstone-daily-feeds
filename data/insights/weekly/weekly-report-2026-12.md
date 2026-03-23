# Weekly Research Report | 2026-03-16 ~ 2026-03-22

> generated_at: 2026-03-23T03:49:47Z
> k_selected: 4
> embedding_model: text-embedding-3-large
> chat_model: gpt-5.2-2025-12-11

## 本周摘要（2026-03-16 ~ 2026-03-22）

1) 编码智能体正在从“会写代码的对话助手”走向“可审查、可分解、可持续推进”的工程化流程：以结构化提示、子智能体编排、状态/上下文管理来对抗长任务中的目标漂移与上下文劣化，并把需求澄清—规格/设计—计划—执行—审查固化为可复用技能框架与模板。[source:github:gh-2026-03-20-9][source:github:gh-2026-03-20-2]  

2) 设计—代码协同进入产品化加速期：多模态画布、上下文感知智能体与“设计系统/规范文件（如 DESIGN.md）”结合，把高保真 UI 的生成、迭代与工程落地压缩到同一工作流；同时出现“可供其他代理调用的设计智能层”，试图补齐布局/排版/视觉平衡等设计推理能力。[source:producthunt:ph-2026-03-20-1][source:producthunt:ph-2026-03-22-1]  

3) “本地优先”成为桌面端 AI 工作空间的共同叙事：任务、文件、指令、记忆/知识库被整合在本机，以维持跨任务一致上下文；MCP、Webhook、自选 LLM 等接口把本地内容接入代理生态，但也同时引出兼容性与隐私边界的新约束。[source:producthunt:ph-2026-03-22-2][source:producthunt:ph-2026-03-20-8][source:producthunt:ph-2026-03-22-9]  

4) 榜单侧信号显示：一体化本地模型运行/训练工具与 AI 设计搭档热度与上升幅度均靠前，说明“本地能力 + 端到端工作流”与“设计-代码同屏”是本周开发者与产品人群体注意力的交汇点。[source:github:gh-2026-03-20-5][source:producthunt:ph-2026-03-20-1]  

---

## 趋势主题（3）

### 主题一：编码智能体的结构化提示与工作流：从需求澄清到任务分解执行

**结论 1：结构化流程正在成为编码智能体的“默认外骨骼”，核心目的是解决长任务中的 context rot 与目标漂移。** 典型做法不是再加一句“请一步步思考”，而是把输出强制分层（目标/约束/规格/设计/计划/任务分解/验收），并引入状态管理与子代理协作来保持推进节奏。[source:github:gh-2026-03-20-2][source:github:gh-2026-03-20-9]

**Why-now（为何此刻集中出现）**  
- 从证据看，项目叙事已从“提升单次生成质量”转向“让智能体能更久、更稳地按计划推进”：例如强调规格与设计评审、TDD（红绿）、YAGNI、DRY 等工程方法论被写进工作流，反映开发者开始把“可靠交付”当作代理能力的一部分。[source:github:gh-2026-03-20-9]  
- 另一方面，本地运行/训练与代码执行沙箱等能力被整合进统一 UI，使得复杂代理链路（工具调用、执行、校验、再迭代）更容易在个人/小团队环境落地，从而放大了对“流程化组织”的需求。[source:github:gh-2026-03-20-5]

**代表项目对比（做法差异）**  
- **obra/superpowers**：更像“软件开发方法论 + 技能框架”的系统化流程，强调先澄清目标并产出规格/设计，经确认后生成计划，再通过子智能体分解执行与审查，显式引入 TDD/YAGNI/DRY 以提高可维护性与可审计性。[source:github:gh-2026-03-20-9]  
- **gsd-build/get-shit-done**：更偏“元提示 + 上下文工程”的轻量体系，突出用 XML 提示格式、状态管理与子代理编排来对抗 context rot，并强调模型自我校验以提升稳定性，适配 Claude Code 等 CLI/代码助手场景。[source:github:gh-2026-03-20-2]  
- **unslothai/unsloth**：不直接提供流程模板，而是通过本地统一 Web UI 把模型运行/训练、工具调用、联网搜索、代码执行沙箱、多文件对话等能力集成，间接降低“把工作流做复杂”的门槛（因为执行与验证链路更顺滑）。[source:github:gh-2026-03-20-5]

**风险与约束**  
- 结构化流程可能对小需求引入过多步骤，拖慢迭代；“流程收益”是否覆盖“流程成本”取决于任务规模与团队纪律。[source:github:gh-2026-03-20-9]  
- 子智能体分解与状态管理的边界若定义不清，可能把复杂性从代码转移到编排层，出现“过度工程化的代理工作流”。[source:github:gh-2026-03-20-2]  
- 自我校验/审查可能带来误判或循环（反复自检但不推进），需要可观测与终止条件；但证据仅显示“支持/强调”，尚不足以证明稳定增益。[source:github:gh-2026-03-20-2]

**下周观察点**  
- 是否出现更成熟的“规格/设计/计划”模板库与可组合技能扩展，让流程从理念走向可迁移的项目脚手架。[source:github:gh-2026-03-20-9]  
- 围绕 context rot 的最佳实践是否进一步“产品化”：例如更易用的状态记录命令、自动摘要策略、或更清晰的 XML/结构化提示约定。[source:github:gh-2026-03-20-2]  
- 本地一体化环境是否继续强化训练可观测性与多 GPU 等特性，从而让“本地代理 + 可执行验证”成为更多人的默认选择。[source:github:gh-2026-03-20-5]

---

### 主题二：AI 原生设计-代码协同：上下文智能体驱动的即时 UI 生成与一致性落地

**结论 1：高保真 UI 的“即时生成 + 同画布迭代”正在把设计与工程实现压缩成一个连续工作流，而不是两个工具间的交接。** Stitch 2.0 体现为在同一画布跨图片/代码/文本创建与迭代，并直接生成原型。[source:producthunt:ph-2026-03-20-1]

**Why-now**  
- 本周证据同时覆盖三块拼图：①“同屏画布 + 多模态即时生成”（Stitch 2.0），②“可被其他代理调用的设计智能层”（Lokuma Design Agent），③“面向复杂长任务的编码模型”（Composer 2）。这意味着从 UI 生成、设计推理到长周期编码执行，链路正在被补齐，促使“设计—代码协同”从概念走向可用产品。[source:producthunt:ph-2026-03-20-1][source:producthunt:ph-2026-03-22-1][source:producthunt:ph-2026-03-21-3]

**代表项目对比**  
- **Stitch 2.0 by Google**：定位“AI 原生氛围设计搭档”，重点在多模态画布与上下文感知交互，并用内置设计系统与 **DESIGN.md** 维持一致性，试图把规范作为持续约束而非一次性提示。[source:producthunt:ph-2026-03-20-1]  
- **Design Agent by Lokuma**：强调“生成不等于设计”，作为可供 OpenClaw、Claude Code、Codex 等代理调用的设计层，主攻布局/排版/视觉平衡等推理型能力，更像是给编码代理补一块“设计判断力”。[source:producthunt:ph-2026-03-22-1]  
- **Composer 2 by Cursor**：不直接做设计，而是为“复杂、长周期开发任务”提供更强/更快的编码模型变体（持续预训练 + 强化学习），成为设计-代码协同时的执行引擎候选。[source:producthunt:ph-2026-03-21-3]

**风险与约束**  
- “即时生成”的 UI 若缺少工程约束（可维护性、可扩展性、组件化策略），可能在真实迭代中迅速失效；现有证据强调高保真与原型，但未提供长期维护机制的细节。[source:producthunt:ph-2026-03-20-1]  
- 设计系统一致性依赖 DESIGN.md/内置系统：规范如何演进、如何校验偏离、如何处理多品牌/多端差异，仍是落地瓶颈。[source:producthunt:ph-2026-03-20-1]  
- “设计推理层”若作为通用组件被多代理调用，兼容性与评测体系会成为关键：不同品牌审美与业务语境下，布局/视觉平衡的“正确性”难以统一量化。[source:producthunt:ph-2026-03-22-1]

**下周观察点**  
- 是否出现更多“画布内生成—同步代码—同步原型”的同流能力更新（减少跨工具搬运与信息损耗）。[source:producthunt:ph-2026-03-20-1]  
- 是否出现一致性校验/规范对齐流程的细化（围绕 DESIGN.md 的自动检查或变更管理）。[source:producthunt:ph-2026-03-20-1]  
- 长任务编码模型是否继续围绕成本/速度/实时性给出更明确的分层产品策略，以匹配设计迭代的频繁节奏。[source:producthunt:ph-2026-03-21-3]

---

### 主题三：本地优先的 AI 工作空间：跨任务一致上下文与工作流管理

**结论 1：“任务+文件+指令+记忆/知识库”的一体化容器正在成为桌面端 AI 工作空间的核心形态，目标是维持跨任务一致上下文。** Claude Cowork Projects 明确以 Projects 工作空间承载上述要素，并面向复杂工作流管理。[source:producthunt:ph-2026-03-22-2]

**Why-now**  
- 多个产品同时强调“本地优先/不离开本机/离线”与“可复用上下文”，反映用户对数据控制、延迟与持续上下文的需求正在压过“纯云端对话”。[source:producthunt:ph-2026-03-22-9][source:producthunt:ph-2026-03-22-2]  
- MCP 在笔记/知识库读写中的使用频繁出现：Novi Notes 主打内置 MCP 让 Claude 直接读写本地笔记，减少插件与配置；talat 也提到可通过 MCP 服务器查询历史，说明“本地内容→代理可用”的接口正在标准化。[source:producthunt:ph-2026-03-22-9][source:producthunt:ph-2026-03-20-8]

**代表项目对比**  
- **Claude Cowork Projects**：以“工作空间”组织复杂工作流，把任务、文件、指令、记忆打包，强调跨任务一致上下文与本地可复用性，偏向协作/项目制管理。[source:producthunt:ph-2026-03-22-2]  
- **talat**：从“本机实时转录→可搜索笔记→自动导出/推送→可被查询”切入，用 Mac Neural Engine 做实时转录，并提供自定义 LLM、总结提示词、导出到 Obsidian、Webhook 推送与 MCP 查询历史，偏向个人知识捕获与自动化。[source:producthunt:ph-2026-03-20-8]  
- **Novi Notes**：强调 100% 本地离线、一次性买断，内置 MCP 让 Claude 直接读写笔记，目标是把“可用的本地知识库”做成开箱即用，降低配置门槛。[source:producthunt:ph-2026-03-22-9]

**风险与约束**  
- “跨任务一致上下文”在本地架构下的边界与更新机制复杂：任务/文件/指令/记忆如何同步版本、如何避免相互污染（例如旧指令干扰新任务），证据提出了方向但未给出通行解法。[source:producthunt:ph-2026-03-22-2]  
- MCP 深度集成增强能力，也可能带来对特定客户端/生态的依赖，影响可迁移性与兼容性。[source:producthunt:ph-2026-03-22-9]  
- “音频/笔记不离开本机”的承诺在导出与 Webhook 推送场景下会被重新定义：哪些数据可外发、是否有默认脱敏与权限控制，是落地隐私边界的关键细节。[source:producthunt:ph-2026-03-20-8]

**下周观察点**  
- Projects 形态是否继续增强“容器化上下文”的操作性：例如更细粒度的记忆更新策略、指令继承规则、或跨项目隔离机制。[source:producthunt:ph-2026-03-22-2]  
- 更多本地优先应用是否采用“内置 MCP + 零配置”，推动 MCP 成为桌面端知识库读写的事实标准接口。[source:producthunt:ph-2026-03-22-9]  
- “本机转录 + 知识库 + 自动化外连”的组合用法是否出现更成熟的隐私/权限边界设计（比如可审阅再推送）。[source:producthunt:ph-2026-03-20-8]

---

## 项目榜单（基于本周 boards）

### 1) Rising Top（上升最快）
- unslothai/unsloth（GitHub）：本地统一 UI 集成运行/训练/工具调用/代码执行沙箱等，显示“本地端到端能力栈”关注度上行。[source:github:gh-2026-03-20-5]  
- Stitch 2.0 by Google（Product Hunt）：同画布多模态高保真 UI 生成与迭代，且用 DESIGN.md 维持一致性，体现设计-代码同流的产品化推进。[source:producthunt:ph-2026-03-20-1]  
- OS-Themis（arXiv）：进入榜单的“critic framework for GUI rewards”提示 GUI/代理评测与奖励建模仍在加速演进（仅就榜单信号，不延伸论文内容）。[source:ax-2026-03-21-1]  
- ProductBridge（Product Hunt）：入榜显示“产品/交付桥接类工具”仍被关注，但证据未提供更细定位细节，故不展开。[source:ph-2026-03-21-1]  
- Design Agent by Lokuma（Product Hunt）：作为可被其他代理调用的设计层，反映“设计推理能力组件化”的需求上升。[source:producthunt:ph-2026-03-22-1]  

### 2) Hot Top（热度最高）
- obra/superpowers（GitHub）：以工程方法论驱动的编码智能体工作流获得高热度，说明“可审查的代理流程”正在成为开发者共识焦点之一。[source:github:gh-2026-03-20-9]  
- Stitch 2.0 / OS-Themis / ProductBridge / Design Agent：与 Rising 榜高度重合，表明本周注意力集中在“UI/GUI（生成与评测）”与“代理可用组件化能力”。[source:producthunt:ph-2026-03-20-1][source:ax-2026-03-21-1][source:producthunt:ph-2026-03-22-1]  

### 3) Novel Top（新颖度）
- Stitch 2.0、OS-Themis、Box Maze 等进入新颖榜，提示“生成（UI/代码）+ 可靠性/过程控制/评测”的组合创新仍是主线（此处仅依据榜单入选事实，不对论文细节作外推）。[source:producthunt:ph-2026-03-20-1][source:ax-2026-03-21-1][source:ax-2026-03-21-2]  

---

## 关键词趋势（Emerging / Surging / Cooling）

**结论 1： “语义对齐”跃升为最强信号词，反映从生成到“对齐规格/设计系统/任务目标”的关注上升。** 该词在 emerging 与 surging 中均为最高分，说明讨论集中且增速快。[source:keyword_boards]  

**结论 2： “代码生成”“开发者工具”“gpu”同时走强，显示工作流落地与本地/算力相关能力在同一周共振。** 其中“代码生成”由 2 个来源支撑，覆盖面更广；“gpu”亦由多来源支撑，指向本地运行/训练类工具的需求上行。[source:keyword_boards]  

**结论 3： “智能体编排”保持上行，但“mcp”“cli”“工作流自动化”等在 cooling 列表中出现，提示叙事可能从“接口/形态名词”转向“更上层的效果与对齐问题”。** 即大家仍在做编排，但讨论焦点未必停留在 CLI/MCP 这些词本身。[source:keyword_boards]  

---

## 交叉来源观察

**结论 1：本地优先 AI 工作空间是少数同时横跨 GitHub 与 Product Hunt 的主题，意味着它既有产品化拉动，也有工程/开源侧的承接。** 这类跨源共振通常代表“可被买单的体验诉求”与“可被实现的工程路径”同时成熟。[source:cross_source_observations]  

---

## 下周预测（可证伪的观察点）

1) **结构化提示将进一步“模板化/协议化”**：会出现更多围绕规格、设计评审、计划、验收的可复用工件（尤其是可组合技能与子智能体协作方式），以降低采用门槛并提升迁移性。[source:github:gh-2026-03-20-9]  

2) **context rot 的工程解法会从“写法”走向“工具化状态机”**：例如更明确的状态记录、摘要与回放机制，甚至把 XML/结构化提示约定固化为命令与默认流程，以减少人为维护上下文的成本。[source:github:gh-2026-03-20-2]  

3) **设计-代码同屏产品将围绕“一致性校验”展开第二阶段竞争**：仅“生成高保真”不足以支撑长期迭代，下一步更可能强调 DESIGN.md/设计系统的持续对齐、偏离检测与规范演进流程。[source:producthunt:ph-2026-03-20-1]  

4) **本地优先应用会继续加深 MCP 与自动化外连，但隐私边界将成为差异化焦点**：一边是“零配置读写本地知识库”的易用性，另一边是导出/推送链路的可审阅与权限控制，预计会出现更多“本地承诺如何在外连场景保持一致”的产品叙事与功能补齐。[source:producthunt:ph-2026-03-22-9][source:producthunt:ph-2026-03-20-8]  

（注：以上预测均依据本周项目定位与榜单/关键词信号推断，未引入外部未提供数据。）

## 引用索引

- [arxiv:ax-2026-03-20-10] Under One Sun: Multi-Object Generative Perception of Materials and Illumination (https://arxiv.org/abs/2603.19226v1)
- [arxiv:ax-2026-03-20-11] EffectErase: Joint Video Object Removal and Insertion for High-Quality Effect Erasing (https://arxiv.org/abs/2603.19224v1)
- [arxiv:ax-2026-03-20-12] Spectrally-Guided Diffusion Noise Schedules (https://arxiv.org/abs/2603.19222v1)
- [arxiv:ax-2026-03-20-14] LVOmniBench: Pioneering Long Audio-Video Understanding Evaluation for Omnimodal LLMs (https://arxiv.org/abs/2603.19217v1)
- [arxiv:ax-2026-03-20-15] DreamPartGen: Semantically Grounded Part-Level 3D Generation via Collaborative Latent Denoising (https://arxiv.org/abs/2603.19216v1)
- [arxiv:ax-2026-03-20-16] Do VLMs Need Vision Transformers? Evaluating State Space Models as Vision Encoders (https://arxiv.org/abs/2603.19209v1)
- [arxiv:ax-2026-03-20-17] Reconstruction Matters: Learning Geometry-Aligned BEV Representation through 3D Gaussian Splatting (https://arxiv.org/abs/2603.19193v1)
- [arxiv:ax-2026-03-20-22] Robustness, Cost, and Attack-Surface Concentration in Phishing Detection (https://arxiv.org/abs/2603.19204v1)
- [arxiv:ax-2026-03-20-25] SOL-ExecBench: Speed-of-Light Benchmarking for Real-World GPU Kernels Against Hardware Limits (https://arxiv.org/abs/2603.19173v1)
- [arxiv:ax-2026-03-20-26] Rigorous Error Certification for Neural PDE Solvers: From Empirical Residuals to Solution Guarantees (https://arxiv.org/abs/2603.19165v1)
- [arxiv:ax-2026-03-20-27] Enhancing Pretrained Model-based Continual Representation Learning via Guided Random Projection (https://arxiv.org/abs/2603.19145v1)
- [arxiv:ax-2026-03-20-28] SHAPCA: Consistent and Interpretable Explanations for Machine Learning Models on Spectroscopy Data (https://arxiv.org/abs/2603.19141v1)
- [arxiv:ax-2026-03-20-29] Hierarchical Latent Structure Learning through Online Inference (https://arxiv.org/abs/2603.19139v1)
- [arxiv:ax-2026-03-20-30] Adaptive Regime-Aware Stock Price Prediction Using Autoencoder-Gated Dual Node Transformers with Reinforcement Learning Control (https://arxiv.org/abs/2603.19136v1)
- [arxiv:ax-2026-03-20-4] D5P4: Partition Determinantal Point Process for Diversity in Parallel Discrete Diffusion Decoding (https://arxiv.org/abs/2603.19146v1)
- [arxiv:ax-2026-03-20-5] F2LLM-v2: Inclusive, Performant, and Efficient Embeddings for a Multilingual World (https://arxiv.org/abs/2603.19223v1)
- [arxiv:ax-2026-03-20-7] UGID: Unified Graph Isomorphism for Debiasing Large Language Models (https://arxiv.org/abs/2603.19144v1)
- [arxiv:ax-2026-03-21-1] OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards (https://arxiv.org/abs/2603.19191v1)
- [arxiv:ax-2026-03-21-13] Rethinking Vector Field Learning for Generative Segmentation (https://arxiv.org/abs/2603.19218v1)
- [arxiv:ax-2026-03-21-18] ARIADNE: A Perception-Reasoning Synergy Framework for Trustworthy Coronary Angiography Analysis (https://arxiv.org/abs/2603.19169v1)
- [arxiv:ax-2026-03-21-19] Adaptive Auxiliary Prompt Blending for Target-Faithful Diffusion Generation (https://arxiv.org/abs/2603.19158v1)
- [arxiv:ax-2026-03-21-2] Box Maze: A Process-Control Architecture for Reliable LLM Reasoning (https://arxiv.org/abs/2603.19182v1)
- [arxiv:ax-2026-03-21-20] ADAPT: Attention Driven Adaptive Prompt Scheduling and InTerpolating Orthogonal Complements for Rare Concepts Generation (https://arxiv.org/abs/2603.19157v1)
- [arxiv:ax-2026-03-21-21] GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning (https://arxiv.org/abs/2603.19137v1)
- [arxiv:ax-2026-03-21-23] Improving RCT-Based Treatment Effect Estimation Under Covariate Mismatch via Calibrated Alignment (https://arxiv.org/abs/2603.19186v1)
- [arxiv:ax-2026-03-21-24] MIDST Challenge at SaTML 2025: Membership Inference over Diffusion-models-based Synthetic Tabular data (https://arxiv.org/abs/2603.19185v1)
- [arxiv:ax-2026-03-21-3] cuGenOpt: A GPU-Accelerated General-Purpose Metaheuristic Framework for Combinatorial Optimization (https://arxiv.org/abs/2603.19163v1)
- [arxiv:ax-2026-03-21-6] Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation (https://arxiv.org/abs/2603.19220v1)
- [arxiv:ax-2026-03-21-8] Matryoshka Gaussian Splatting (https://arxiv.org/abs/2603.19234v1)
- [arxiv:ax-2026-03-21-9] MonoArt: Progressive Structural Reasoning for Monocular Articulated 3D Reconstruction (https://arxiv.org/abs/2603.19231v1)
- [github:gh-2026-03-20-10] tw93/Mole (https://github.com/tw93/Mole)
- [github:gh-2026-03-20-2] gsd-build/get-shit-done (https://github.com/gsd-build/get-shit-done)
- [github:gh-2026-03-20-3] mobile-dev-inc/Maestro (https://github.com/mobile-dev-inc/Maestro)
- [github:gh-2026-03-20-4] langchain-ai/open-swe (https://github.com/langchain-ai/open-swe)
- [github:gh-2026-03-20-5] unslothai/unsloth (https://github.com/unslothai/unsloth)
- [github:gh-2026-03-20-6] newton-physics/newton (https://github.com/newton-physics/newton)
- [github:gh-2026-03-20-9] obra/superpowers (https://github.com/obra/superpowers)
- [github:gh-2026-03-21-1] opendataloader-project/opendataloader-pdf (https://github.com/opendataloader-project/opendataloader-pdf)
- [github:gh-2026-03-21-2] openrocket/openrocket (https://github.com/openrocket/openrocket)
- [github:gh-2026-03-21-5] TauricResearch/TradingAgents (https://github.com/TauricResearch/TradingAgents)
- [github:gh-2026-03-21-6] louis-e/arnis (https://github.com/louis-e/arnis)
- [github:gh-2026-03-22-1] systemd/systemd (https://github.com/systemd/systemd)
- [github:gh-2026-03-22-2] protocolbuffers/protobuf (https://github.com/protocolbuffers/protobuf)
- [github:gh-2026-03-22-3] aquasecurity/trivy (https://github.com/aquasecurity/trivy)
- [github:gh-2026-03-22-5] FujiwaraChoki/MoneyPrinterV2 (https://github.com/FujiwaraChoki/MoneyPrinterV2)
- [github:gh-2026-03-22-6] vllm-project/vllm-omni (https://github.com/vllm-project/vllm-omni)
- [github:gh-2026-03-22-8] Crosstalk-Solutions/project-nomad (https://github.com/Crosstalk-Solutions/project-nomad)
- [producthunt:ph-2026-03-20-1] Stitch 2.0 by Google (https://www.producthunt.com/products/stitch-2-0-by-google-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-10] Budibase AI Agents (https://www.producthunt.com/products/budibase?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-11] NVIDIA NemoClaw (https://www.producthunt.com/products/nvidia?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-12] Doodles Ai (https://www.producthunt.com/products/doodles-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-13] Scheduled (https://www.producthunt.com/products/scheduled-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-14] Machine Payments Protocol (https://www.producthunt.com/products/stripe?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-15] GB1: The AI from the UK (https://www.producthunt.com/products/gb1?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-16] Pluto Door (https://www.producthunt.com/products/pluto-door?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-17] Link AI (https://www.producthunt.com/products/link-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-18] MiMo-V2-Pro & Omni (https://www.producthunt.com/products/mimo-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-19] Bit Office (https://www.producthunt.com/products/github-311?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-2] MiniMax-M2.7 (https://www.producthunt.com/products/minimax-agent?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-20] OpenAdapter (https://www.producthunt.com/products/openadapter-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-21] Offload (https://www.producthunt.com/products/imbue-7?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-22] MCPCore (https://www.producthunt.com/products/mcpcore?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-23] Billy.sh (https://www.producthunt.com/products/billy-sh?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-24] MelonSound (https://www.producthunt.com/products/melonsound?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-25] Okan (https://www.producthunt.com/products/okan-claude-code-browser-notifications?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-26] SideDisplay (https://www.producthunt.com/products/sidedisplay?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-27] Tracium.ai (https://www.producthunt.com/products/tracium-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-28] Journey (https://www.producthunt.com/products/earn-points-on-airbnbs-boutique-hotels?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-29] JSTRUX — From Idea to Profit (https://www.producthunt.com/products/jstrux-from-idea-to-profit?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-3] Netlify.new (https://www.producthunt.com/products/netlify?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-30] ChatML (https://www.producthunt.com/products/chatml?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-4] OctoClaw (https://www.producthunt.com/products/octoclaw?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-5] Comet for iOS (https://www.producthunt.com/products/perplexity-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-6] PixelClaw (https://www.producthunt.com/products/pixelclaw?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-7] Lucent (https://www.producthunt.com/products/lucent-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-8] talat (https://www.producthunt.com/products/talat?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-20-9] Scouts for iOS (https://www.producthunt.com/products/scouts-by-yutori?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-1] ProductBridge (https://www.producthunt.com/products/productbridge?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-10] Room Service (https://www.producthunt.com/products/room-service-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-11] Context Overflow (https://www.producthunt.com/products/context-overflow?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-12] Fig Prompt (https://www.producthunt.com/products/fig-prompt?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-13] Looq: Preview Files (https://www.producthunt.com/products/looq-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-14] Joy for Gmail (https://www.producthunt.com/products/joy-for-gmail?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-15] Gately (https://www.producthunt.com/products/nevacode?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-16] Chat (https://www.producthunt.com/products/chat-5?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-17] Gaze Guard (https://www.producthunt.com/products/gaze-guard?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-18] Cacheless (https://www.producthunt.com/products/cacheless-ai-powered-disk-cleanup?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-19] Kickfolder (https://www.producthunt.com/products/kickfolder?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-2] AdsTurbo (https://www.producthunt.com/products/adsturbo-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-20] RoastMyReels - AI Reels Coach That Hurts (https://www.producthunt.com/products/roastmyreels-ai-reels-coach-that-hurts?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-21] ProAI (https://www.producthunt.com/products/proai-v4?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-22] Advivi (https://www.producthunt.com/products/advivi?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-23] CueNotch (https://www.producthunt.com/products/cuenotch?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-24] Tubekit (https://www.producthunt.com/products/tubekit?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-25] Ferris Pulse (https://www.producthunt.com/products/ferris-pulse?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-26] Savine AI (https://www.producthunt.com/products/savine-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-27] Video Gallery for WooCommerce (https://www.producthunt.com/products/video-gallery-for-woocommerce?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-28] Vibeworker (https://www.producthunt.com/products/vibeworker?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-29] OnlyFlags (https://www.producthunt.com/products/onlyflags?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-3] Composer 2 by Cursor (https://www.producthunt.com/products/cursor?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-30] MAI-Image-2 (https://www.producthunt.com/products/mai-image-2-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-4] GitAgent by Lyzr (https://www.producthunt.com/products/gitagent-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-5] Claude Code Channels (https://www.producthunt.com/products/claude?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-6] Google AI Studio 2.0 (https://www.producthunt.com/products/google-ai-studio-8?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-7] Built for Devs (https://www.producthunt.com/products/built-for-devs-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-8] Visdiff (https://www.producthunt.com/products/visdiff?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-21-9] AI Skills Manager (https://www.producthunt.com/products/ai-skills-manager?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-1] Design Agent by Lokuma (https://www.producthunt.com/products/lokuma-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-10] Sanota (https://www.producthunt.com/products/sanota?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-11] Caplo (https://www.producthunt.com/products/caplo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-12] Everest AI (https://www.producthunt.com/products/everest-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-13] dailytips.dev (https://www.producthunt.com/products/dailytips-dev?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-14] Buystocklot 2.0 (https://www.producthunt.com/products/buystocklot-com?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-15] People Loop (https://www.producthunt.com/products/people-loop?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-16] Lazy Unicorn (https://www.producthunt.com/products/lazy-unicorn?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-17] FileSyncAI (https://www.producthunt.com/products/filesyncai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-18] Domainbar (https://www.producthunt.com/products/domainbar?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-19] BeigeCRM (https://www.producthunt.com/products/beigecrm?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-2] Claude Cowork Projects (https://www.producthunt.com/products/claude-cowork-projects?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-20] Foundd (https://www.producthunt.com/products/foundd?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-21] LLC Cost Calculator (https://www.producthunt.com/products/llc-cost-calculator?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-22] Hive (https://www.producthunt.com/products/hive-9?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-23] PromptURLs 2.0 (https://www.producthunt.com/products/prompturls?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-24] Nox (https://www.producthunt.com/products/nox-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-25] edgameclaw (https://www.producthunt.com/products/edgameclaw?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-26] Red Monitor (https://www.producthunt.com/products/red-monitor?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-27] Scriptonia (https://www.producthunt.com/products/scriptonia?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-28] Cleanclip (https://www.producthunt.com/products/cleanclip-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-29] Scowld (https://www.producthunt.com/products/scowld?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-3] Fractal (https://www.producthunt.com/products/fractal-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-30] ClipBox – Copy & Paste Manager | CopyBox (https://www.producthunt.com/products/clipbox-copy-paste-manager-copybox?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-4] Vite+ (https://www.producthunt.com/products/vite-alpha?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-5] Cursor Glass (https://www.producthunt.com/products/glass-4?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-6] Contral (https://www.producthunt.com/products/contral?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-7] murmur (https://www.producthunt.com/products/murmur-7?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-8] Replit Agent 4 (https://www.producthunt.com/products/replit-agent-4?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-22-9] Novi Notes (https://www.producthunt.com/products/novi-notes?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
