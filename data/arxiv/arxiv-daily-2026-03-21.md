# arXiv AI 论文日报 | 2026-03-21

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (14 篇)
- [cs.CL](#csCL) (3 篇)
- [cs.LG](#csLG) (9 篇)
- [cs.AI](#csAI) (4 篇)

---

## cs.AI

## [1. OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191v1)

**作者**：Zehao Li, Zhenyu Wu, Yibo Zhao 等 14 位作者  
**分类**：cs.AI  
**发布时间**：2026-03-19

### 📄 论文摘要

Reinforcement Learning (RL) has the potential to improve the robustness of GUI agents in stochastic environments, yet training is highly sensitive to the quality of the reward function. Existing reward approaches struggle to achieve both scalability and performance. To address this, we propose OS-Themis, a scalable and accurate multi-agent critic framework. Unlike a single judge, OS-Themis decomposes trajectories into verifiable milestones to isolate critical evidence for decision making and employs a review mechanism to strictly audit the evidence chain before making the final verdict. To facilitate evaluation, we further introduce OmniGUIRewardBench (OGRBench), a holistic cross-platform benchmark for GUI outcome rewards, where all evaluated models achieve their best performance under OS-Themis. Extensive experiments on AndroidWorld show that OS-Themis yields a 10.3% improvement when used to support online RL training, and a 6.9% gain when used for trajectory validation and filtering in the self-training loop, highlighting its potential to drive agent evolution.

### 🤖 AI 总结

**一句话总结**：OS-Themis 通过将GUI轨迹拆解为可验证里程碑并进行证据链复核，提供可扩展且更准确的GUI结果奖励评估，从而显著提升GUI智能体的RL训练与自训练效果。

**研究动机**：GUI智能体在随机环境中用RL提升鲁棒性很依赖高质量奖励，但现有奖励/裁判方法难以同时兼顾可扩展性与判定性能，导致训练不稳定或收益有限。

**核心方法**：提出多智能体critic框架OS-Themis：将完整轨迹分解为可核验的关键里程碑以定位决策证据，并通过“审阅/复核”机制严格审核证据链后再输出最终裁决；同时构建跨平台整体评测基准OmniGUIRewardBench（OGRBench）用于系统评估GUI outcome rewards。

**主要结论**：在AndroidWorld实验中，OS-Themis用于在线RL训练带来约10.3%提升，用于自训练回路的轨迹验证与过滤带来约6.9%提升；在OGRBench上各模型在OS-Themis下达到最佳表现，表明其能更可靠地驱动GUI智能体迭代进化。

**关键词**：GUI智能体强化学习, 奖励函数设计, 奖励建模, 多智能体评审器, 轨迹分解, 可验证里程碑, 证据链审计, 跨平台GUI基准, 自训练轨迹筛选

**评分**：56

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19191v1) | [下载PDF](https://arxiv.org/pdf/2603.19191v1.pdf)

---

## [2. Box Maze: A Process-Control Architecture for Reliable LLM Reasoning](https://arxiv.org/abs/2603.19182v1)

**作者**：Zou Qiang  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-03-19

### 📄 论文摘要

Large language models (LLMs) demonstrate strong generative capabilities but remain vulnerable to hallucination and unreliable reasoning under adversarial prompting. Existing safety approaches -- such as reinforcement learning from human feedback (RLHF) and output filtering -- primarily operate at the behavioral level and may lack explicit architectural mechanisms for enforcing reasoning process integrity.   This paper proposes the Box Maze framework, a conceptual process-control architecture that decomposes LLM reasoning into three explicit layers: memory grounding, structured inference, and boundary enforcement. We introduce preliminary simulation-based evaluation involving progressive boundary erosion scenarios across multiple heterogeneous LLM systems (DeepSeek-V3, Doubao, Qwen). Results from n=50 adversarial scenarios suggest that explicit cognitive control layers may improve consistency in boundary maintenance, with architectural constraints reducing boundary failure rates from approximately 40% (baseline RLHF) to below 1% under adversarial conditions.   While current validation is simulation-based, these preliminary results indicate that process-level control may offer a promising direction for improving reliability in large language model reasoning.

### 🤖 AI 总结

**一句话总结**：Box Maze提出一种对LLM推理过程进行“分层管控”的架构，将推理拆成记忆落地、结构化推断与边界约束三层，以提升对抗提示下的可靠性与抗越界能力。

**研究动机**：LLM在对抗性提示下容易产生幻觉与不可靠推理，而RLHF与输出过滤多停留在行为层面，缺少对推理过程完整性的显式架构约束。

**核心方法**：框架将推理流程显式分解为三层：以外部/事实锚定的记忆落地（grounding）、可结构化约束的推断层、以及用于阻断边界侵蚀的边界执行层；并在DeepSeek-V3、Doubao、Qwen上用“渐进式边界侵蚀”的n=50模拟对抗场景进行评估，对比RLHF基线的边界失效率。

**主要结论**：模拟结果显示，引入显式过程控制层后，边界失败率可由约40%降至1%以下，表明过程级架构约束可能比单纯行为对齐更能稳定维持边界；但当前证据主要来自仿真评估，仍需更真实任务与更严格验证。

**关键词**：LLM可靠推理, 幻觉抑制, 过程控制架构, 推理过程完整性, 认知控制层, 记忆锚定, 结构化推理, 边界约束, 边界侵蚀测试, 安全对齐评测, 仿真评测

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19182v1) | [下载PDF](https://arxiv.org/pdf/2603.19182v1.pdf)

---

## [3. cuGenOpt: A GPU-Accelerated General-Purpose Metaheuristic Framework for Combinatorial Optimization](https://arxiv.org/abs/2603.19163v1)

**作者**：Yuyang Liu  
**分类**：cs.AI, cs.DC  
**发布时间**：2026-03-19

### 📄 论文摘要

Combinatorial optimization problems arise in logistics, scheduling, and resource allocation, yet existing approaches face a fundamental trade-off among generality, performance, and usability. We present cuGenOpt, a GPU-accelerated general-purpose metaheuristic framework that addresses all three dimensions simultaneously.   At the engine level, cuGenOpt adopts a "one block evolves one solution" CUDA architecture with a unified encoding abstraction (permutation, binary, integer), a two-level adaptive operator selection mechanism, and hardware-aware resource management. At the extensibility level, a user-defined operator registration interface allows domain experts to inject problem-specific CUDA search operators. At the usability level, a JIT compilation pipeline exposes the framework as a pure-Python API, and an LLM-based modeling assistant converts natural-language problem descriptions into executable solver code.   Experiments across five thematic suites on three GPU architectures (T4, V100, A800) show that cuGenOpt outperforms general MIP solvers by orders of magnitude, achieves competitive quality against specialized solvers on instances up to n=150, and attains 4.73% gap on TSP-442 within 30s. Twelve problem types spanning five encoding variants are solved to optimality. Framework-level optimizations cumulatively reduce pcb442 gap from 36% to 4.73% and boost VRPTW throughput by 75-81%.   Code: https://github.com/L-yang-yang/cugenopt

### 🤖 AI 总结

**一句话总结**：cuGenOpt 是一个面向组合优化的通用GPU元启发式框架，通过统一编码与自适应算子选择，在保持易用性的同时显著提升求解速度与解质量。

**研究动机**：现有组合优化方法在“通用性-性能-易用性”之间难以兼顾：通用求解器慢、专用算法难复用且开发门槛高。作者希望用GPU并行与框架化抽象，让领域专家能低成本写CUDA算子并获得接近专用求解器的表现。

**核心方法**：框架引擎采用“每个CUDA block演化一个解”的并行架构，提供排列/二进制/整数等统一编码抽象，配合两级自适应算子选择与硬件感知资源管理来提高吞吐与稳定性。扩展性上支持用户注册问题特定CUDA算子；易用性上通过JIT将其暴露为纯Python API，并用LLM建模助手把自然语言问题描述转成可执行求解代码。

**主要结论**：在T4/V100/A800上覆盖五类基准套件实验显示，cuGenOpt 相比通用MIP求解器可实现数量级加速，并在最大 n=150 的实例上达到与专用求解器相当的质量。其框架级优化将 pcb442 的TSP gap 从36%降到4.73%（30s），并使VRPTW吞吐提升约75–81%，且在12种问题类型/5种编码变体上获得最优解。

**关键词**：组合优化, 元启发式框架, 统一编码抽象, 自适应算子选择, 硬件感知资源管理, LLM建模助手, cuGenOpt, GPU-Accelerated

**评分**：48

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19163v1) | [下载PDF](https://arxiv.org/pdf/2603.19163v1.pdf)

---

## [4. D5P4: Partition Determinantal Point Process for Diversity in Parallel Discrete Diffusion Decoding](https://arxiv.org/abs/2603.19146v1)

**作者**：Jonathan Lys, Vincent Gripon, Bastien Pasdeloup 等 7 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Discrete diffusion models are promising alternatives to autoregressive approaches for text generation, yet their decoding methods remain under-studied. Standard decoding methods for autoregressive models, such as beam search, do not directly apply to iterative denoising, and existing diffusion decoding techniques provide limited control over in-batch diversity. To bridge this gap, we introduce a generalized beam-search framework for discrete diffusion that generates candidates in parallel and supports modular beam-selection objectives. As a diversity-focused instantiation, we propose D5P4, which formulates the selection step as MAP inference over a Determinantal Point Process. Leveraging a scalable greedy solver, D5P4 maintains multi-GPU compatibility and enables an explicit trade-off between model probability and target diversity with near-zero compute overhead. Experiments on free-form generation and question answering demonstrate that D5P4 improves diversity over strong baselines while maintaining competitive generation quality.

### 🤖 AI 总结

**一句话总结**：D5P4为离散扩散解码提出可并行的“泛化beam search”框架，并用DPP式选择在几乎不增加计算开销的情况下显著提升批内生成多样性。

**研究动机**：离散扩散模型虽具潜力，但迭代去噪式解码难以直接套用beam search等经典策略，且现有扩散解码对同一批次候选的多样性控制不足。

**核心方法**：提出面向离散扩散的并行候选生成与模块化“beam选择目标”框架；其多样性实例D5P4将选择步建模为DPP的MAP推断，用可扩展贪心算法在多GPU上高效挑选候选，并通过参数显式权衡模型概率与目标多样性。

**主要结论**：在自由生成与问答实验中，D5P4相较强基线提升生成多样性，同时保持有竞争力的生成质量，并且额外计算开销近乎为零。

**关键词**：离散扩散模型, 扩散解码, 广义束搜索, 候选生成, 批内多样性, 确定性点过程（DPP）, 贪心求解, 多 GPU 兼容, 文本生成, 问答生成

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19146v1) | [下载PDF](https://arxiv.org/pdf/2603.19146v1.pdf)

---

## cs.CL

## [5. F2LLM-v2: Inclusive, Performant, and Efficient Embeddings for a Multilingual World](https://arxiv.org/abs/2603.19223v1)

**作者**：Ziyin Zhang, Zihan Liao, Hang Yu 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-03-19

### 📄 论文摘要

We present F2LLM-v2, a new family of general-purpose, multilingual embedding models in 8 distinct sizes ranging from 80M to 14B. Trained on a newly curated composite of 60 million publicly available high-quality data samples, F2LLM-v2 supports more than 200 languages, with a particular emphasis on previously underserved mid- and low-resource languages. By integrating a two-stage LLM-based embedding training pipeline with matryoshka learning, model pruning, and knowledge distillation techniques, we present models that are far more efficient than previous LLM-based embedding models while retaining competitive performances. Extensive evaluations confirm that F2LLM-v2-14B ranks first on 11 MTEB benchmarks, while the smaller models in the family also set a new state of the art for resource-constrained applications. To facilitate open-source embedding model research, we release all models, data, code, and intermediate checkpoints.

### 🤖 AI 总结

**一句话总结**：F2LLM-v2 提供覆盖200+语言、从80M到14B共8种规模的通用多语种向量嵌入模型，在保持高性能的同时显著提升推理与部署效率。

**研究动机**：现有基于LLM的嵌入模型往往计算与存储成本高、且对中低资源语言覆盖与效果不足；因此需要兼顾多语种包容性、SOTA性能与资源效率的开放模型体系。

**核心方法**：基于新整理的6000万高质量公开数据，采用两阶段的LLM式嵌入训练流程，并结合 Matryoshka 学习实现多维度可裁剪表示；同时通过模型剪枝与知识蒸馏将大模型能力迁移到小模型以提升效率。

**主要结论**：评测显示 F2LLM-v2-14B 在11个MTEB基准上排名第一，小模型也在受限资源场景取得新的SOTA；作者进一步开源模型、数据、代码与中间checkpoint以促进后续研究。

**关键词**：多语言文本嵌入, 低资源语言, LLM嵌入训练, 两阶段训练, 模型剪枝, 知识蒸馏, 嵌入模型效率优化, MTEB 基准评测, 开源模型与数据集

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19223v1) | [下载PDF](https://arxiv.org/pdf/2603.19223v1.pdf)

---

## [6. Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation](https://arxiv.org/abs/2603.19220v1)

**作者**：Zhuolin Yang, Zihan Liu, Yang Chen 等 17 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

We introduce Nemotron-Cascade 2, an open 30B MoE model with 3B activated parameters that delivers best-in-class reasoning and strong agentic capabilities. Despite its compact size, its mathematical and coding reasoning performance approaches that of frontier open models. It is the second open-weight LLM, after DeepSeekV3.2-Speciale-671B-A37B, to achieve Gold Medal-level performance in the 2025 International Mathematical Olympiad (IMO), the International Olympiad in Informatics (IOI), and the ICPC World Finals, demonstrating remarkably high intelligence density with 20x fewer parameters. In contrast to Nemotron-Cascade 1, the key technical advancements are as follows. After SFT on a meticulously curated dataset, we substantially expand Cascade RL to cover a much broader spectrum of reasoning and agentic domains. Furthermore, we introduce multi-domain on-policy distillation from the strongest intermediate teacher models for each domain throughout the Cascade RL process, allowing us to efficiently recover benchmark regressions and sustain strong performance gains along the way. We release the collection of model checkpoint and training data.

### 🤖 AI 总结

**一句话总结**：Nemotron-Cascade 2 是一款30B的开源MoE大模型（仅激活3B参数），通过扩展版Cascade RL与多领域在策略蒸馏，在推理与智能体能力上以更小规模逼近前沿开源模型并取得多项竞赛级成绩。

**研究动机**：在参数与计算受限的前提下提升“智能密度”，让小激活参数的模型也能具备强数学/代码推理与agentic能力，同时解决后训练过程中容易出现的基准回退与不稳定增益问题。

**核心方法**：先在精心筛选的数据上做SFT打底，然后将Cascade RL扩展到更广泛的推理与智能体领域；在Cascade RL全过程中引入“多领域on-policy蒸馏”，针对每个领域使用最强的中间教师模型进行蒸馏以持续修复回退并巩固收益。

**主要结论**：该方法使30B MoE模型在数学与编程推理上接近前沿开源水平，并在IMO/IOI/ICPC等达到金牌级表现，显示出在远少于超大模型参数量下依然可获得高性能；作者同时公开了模型检查点与训练数据以支持复现与后续研究。

**关键词**：后训练, 混合专家模型（MoE）, 多领域蒸馏, 监督微调（SFT）, 推理能力提升, 智能体能力（Agent）, 数学推理, 代码推理, 竞赛级推理评测, 开放权重模型

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19220v1) | [下载PDF](https://arxiv.org/pdf/2603.19220v1.pdf)

---

## [7. UGID: Unified Graph Isomorphism for Debiasing Large Language Models](https://arxiv.org/abs/2603.19144v1)

**作者**：Zikang Ding, Junchi Yao, Junhao Li 等 7 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-03-19

### 📄 论文摘要

Large language models (LLMs) exhibit pronounced social biases. Output-level or data-optimization--based debiasing methods cannot fully resolve these biases, and many prior works have shown that biases are embedded in internal representations. We propose \underline{U}nified \underline{G}raph \underline{I}somorphism for \underline{D}ebiasing large language models (\textit{\textbf{UGID}}), an internal-representation--level debiasing framework for large language models that models the Transformer as a structured computational graph, where attention mechanisms define the routing edges of the graph and hidden states define the graph nodes. Specifically, debiasing is formulated as enforcing invariance of the graph structure across counterfactual inputs, with differences allowed only on sensitive attributes. \textit{\textbf{UGID}} jointly constrains attention routing and hidden representations in bias-sensitive regions, effectively preventing bias migration across architectural components. To achieve effective behavioral alignment without degrading general capabilities, we introduce a log-space constraint on sensitive logits and a selective anchor-based objective to preserve definitional semantics. Extensive experiments on large language models demonstrate that \textit{\textbf{UGID}} effectively reduces bias under both in-distribution and out-of-distribution settings, significantly reduces internal structural discrepancies, and preserves model safety and utility.

### 🤖 AI 总结

**一句话总结**：UGID通过把Transformer建模为由注意力路由与隐状态组成的计算图，并在反事实输入间强制图结构与表示的不变性，从内部表示层面系统性降低LLM社会偏见且尽量不损伤能力。

**研究动机**：现有输出层或数据层去偏方法难以根除偏见，因为偏见往往已编码在模型内部表示中，且可能在不同组件间“迁移”导致局部修正失效。需要一种能同时约束注意力与表示、并在不牺牲通用能力与安全性的前提下对齐行为的内部去偏框架。

**核心方法**：将Transformer视为结构化计算图：注意力机制定义边（路由），隐藏状态定义节点；去偏目标被表述为对反事实输入强制图结构不变（仅允许敏感属性相关差异），并联合约束偏见敏感区域的注意力路由与隐藏表示以阻断偏见迁移。为兼顾能力保留，引入对敏感logits的log-space约束与选择性anchor目标以保留“定义性语义”。

**主要结论**：在大模型实验中，UGID在分布内与分布外设置下均显著降低偏见，同时减少内部结构差异，并能在保持模型安全性与效用（通用能力）方面取得较好权衡。

**关键词**：表征级去偏, 图同构约束, 反事实不变性, 注意力路由约束, 隐藏状态对齐, 敏感属性约束, 分布外鲁棒去偏, 锚点目标函数

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19144v1) | [下载PDF](https://arxiv.org/pdf/2603.19144v1.pdf)

---

## cs.CV

## [8. Matryoshka Gaussian Splatting](https://arxiv.org/abs/2603.19234v1)

**作者**：Zhilin Guo, Boqiao Zhang, Hakan Aktas 等 13 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-03-19

### 📄 论文摘要

The ability to render scenes at adjustable fidelity from a single model, known as level of detail (LoD), is crucial for practical deployment of 3D Gaussian Splatting (3DGS). Existing discrete LoD methods expose only a limited set of operating points, while concurrent continuous LoD approaches enable smoother scaling but often suffer noticeable quality degradation at full capacity, making LoD a costly design decision. We introduce Matryoshka Gaussian Splatting (MGS), a training framework that enables continuous LoD for standard 3DGS pipelines without sacrificing full-capacity rendering quality. MGS learns a single ordered set of Gaussians such that rendering any prefix, the first k splats, produces a coherent reconstruction whose fidelity improves smoothly with increasing budget. Our key idea is stochastic budget training: each iteration samples a random splat budget and optimises both the corresponding prefix and the full set. This strategy requires only two forward passes and introduces no architectural modifications. Experiments across four benchmarks and six baselines show that MGS matches the full-capacity performance of its backbone while enabling a continuous speed-quality trade-off from a single model. Extensive ablations on ordering strategies, training objectives, and model capacity further validate the designs.

### 🤖 AI 总结

**一句话总结**：MGS通过“随机预算训练”让同一个3D Gaussian Splatting模型在不损失满容量画质的前提下，实现连续可调的LoD（速度-质量平滑权衡）。

**研究动机**：现有离散LoD只能提供少量固定档位，而连续LoD方法往往会牺牲满容量（最高质量）表现，导致LoD成为昂贵且有风险的设计选择。

**核心方法**：MGS学习一个有序的高斯集合，使得渲染前k个高斯（任意前缀）都能得到连贯重建且质量随k平滑提升；训练时每次迭代随机采样一个预算k，同时优化该前缀与全量集合，仅需两次前向计算且无需改动3DGS架构。

**主要结论**：在多个基准与多种基线对比中，MGS保持与原始骨干模型相当的满容量性能，并从单一模型提供连续的速度-质量折中；消融实验进一步验证了高斯排序、训练目标与容量设计的有效性。

**关键词**：3D 高斯溅射（3DGS）, 多细节层次（LoD）, 连续 LoD 渲染, 可调渲染保真度, 有序高斯集合, 随机预算训练, 速度-质量权衡, 全容量质量保持, 无需架构修改训练框架, 高斯排序策略

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19234v1) | [下载PDF](https://arxiv.org/pdf/2603.19234v1.pdf)

---

## [9. MonoArt: Progressive Structural Reasoning for Monocular Articulated 3D Reconstruction](https://arxiv.org/abs/2603.19231v1)

**作者**：Haitian Li, Haozhe Xie, Junxiang Xu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

Reconstructing articulated 3D objects from a single image requires jointly inferring object geometry, part structure, and motion parameters from limited visual evidence. A key difficulty lies in the entanglement between motion cues and object structure, which makes direct articulation regression unstable. Existing methods address this challenge through multi-view supervision, retrieval-based assembly, or auxiliary video generation, often sacrificing scalability or efficiency. We present MonoArt, a unified framework grounded in progressive structural reasoning. Rather than predicting articulation directly from image features, MonoArt progressively transforms visual observations into canonical geometry, structured part representations, and motion-aware embeddings within a single architecture. This structured reasoning process enables stable and interpretable articulation inference without external motion templates or multi-stage pipelines. Extensive experiments on PartNet-Mobility demonstrate that OM achieves state-of-the-art performance in both reconstruction accuracy and inference speed. The framework further generalizes to robotic manipulation and articulated scene reconstruction.

### 🤖 AI 总结

**一句话总结**：MonoArt提出一种从单张图像逐步进行结构化推理的统一框架，以更稳定、可解释地重建可动部件物体的3D几何与关节运动参数，并在精度与速度上领先现有方法。

**研究动机**：单目可动3D重建需要同时推断几何、部件结构与运动参数，但运动线索与结构强耦合导致直接回归关节参数不稳定。现有依赖多视角监督、检索组装或辅助视频生成的方法往往牺牲可扩展性或效率。

**核心方法**：MonoArt不直接从图像特征回归关节，而是在单一架构内将观测逐步变换为规范化几何、结构化的部件表示以及具备运动感知的嵌入，通过“渐进式结构推理”实现关节/运动的稳定推断。该过程避免外部运动模板与多阶段流水线，使推理更可解释且端到端高效。

**主要结论**：在PartNet-Mobility上，MonoArt在重建精度与推理速度上达到SOTA，验证了结构化渐进推理对稳定关节推断的有效性。方法还展示了向机器人操作与可动场景重建的泛化能力。

**关键词**：单目关节物体三维重建, 单图像三维重建, 关节参数估计, 部件结构建模, 渐进式结构推理, 规范形几何, 运动感知嵌入, 运动-结构解耦, 机器人操作, 关节场景重建

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19231v1) | [下载PDF](https://arxiv.org/pdf/2603.19231v1.pdf)

---

## [10. Under One Sun: Multi-Object Generative Perception of Materials and Illumination](https://arxiv.org/abs/2603.19226v1)

**作者**：Nobuo Yoshii, Xinran Nicole Han, Ryo Kawahara 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

We introduce Multi-Object Generative Perception (MultiGP), a generative inverse rendering method for stochastic sampling of all radiometric constituents -- reflectance, texture, and illumination -- underlying object appearance from a single image. Our key idea to solve this inherently ambiguous radiometric disentanglement is to leverage the fact that while their texture and reflectance may differ, objects in the same scene are all lit by the same illumination. MultiGP exploits this consensus to produce samples of reflectance, texture, and illumination from a single image of known shapes based on four key technical contributions: a cascaded end-to-end architecture that combines image-space and angular-space disentanglement; Coordinated Guidance for diffusion convergence to a single consistent illumination estimate; Axial Attention applied to facilitate ``cross-talk'' between objects of different reflectance; and a Texture Extraction ControlNet to preserve high-frequency texture details while ensuring decoupling from estimated lighting. Experimental results demonstrate that MultiGP effectively leverages the complementary spatial and frequency characteristics of multiple object appearances to recover individual texture and reflectance as well as the common illumination.

### 🤖 AI 总结

**一句话总结**：MultiGP通过利用同一场景多物体共享光照这一一致性约束，从单张图像（已知形状）中生成采样式分解并恢复各物体的反射率/纹理与共同光照。

**研究动机**：单图逆渲染中的“光照-材质-纹理”解耦高度不适定，单个物体外观往往存在多解。作者观察到同一场景内不同物体虽材质各异但共享光照，可用跨物体共识来显著收紧解空间。

**核心方法**：提出级联端到端架构，结合图像空间与角域（angular-space）的解耦以分别建模纹理/反射与光照；在扩散生成过程中引入Coordinated Guidance促使所有物体收敛到一致的光照估计，并用Axial Attention增强不同物体间的信息“串扰”以传播光照线索，最后通过Texture Extraction ControlNet保留高频纹理且避免把光照泄漏进纹理。

**主要结论**：实验表明，多物体联合建模能利用不同物体外观在空间与频率上的互补性，更稳定地恢复每个物体的纹理与反射率，同时得到单一一致的场景光照，相比单物体或弱一致性方法更有效。

**关键词**：生成式逆渲染, 单图像逆渲染, 多物体联合感知, 辐射成分解耦, 反射率估计, 纹理重建, 光照估计, Diffusion, 引导采样, 轴向注意力

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19226v1) | [下载PDF](https://arxiv.org/pdf/2603.19226v1.pdf)

---

## [11. EffectErase: Joint Video Object Removal and Insertion for High-Quality Effect Erasing](https://arxiv.org/abs/2603.19224v1)

**作者**：Yang Fu, Yike Zheng, Ziyun Dai 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

Video object removal aims to eliminate dynamic target objects and their visual effects, such as deformation, shadows, and reflections, while restoring seamless backgrounds. Recent diffusion-based video inpainting and object removal methods can remove the objects but often struggle to erase these effects and to synthesize coherent backgrounds. Beyond method limitations, progress is further hampered by the lack of a comprehensive dataset that systematically captures common object effects across varied environments for training and evaluation. To address this, we introduce VOR (Video Object Removal), a large-scale dataset that provides diverse paired videos, each consisting of one video where the target object is present with its effects and a counterpart where the object and effects are absent, with corresponding object masks. VOR contains 60K high-quality video pairs from captured and synthetic sources, covers five effects types, and spans a wide range of object categories as well as complex, dynamic multi-object scenes. Building on VOR, we propose EffectErase, an effect-aware video object removal method that treats video object insertion as the inverse auxiliary task within a reciprocal learning scheme. The model includes task-aware region guidance that focuses learning on affected areas and enables flexible task switching. Then, an insertion-removal consistency objective that encourages complementary behaviors and shared localization of effect regions and structural cues. Trained on VOR, EffectErase achieves superior performance in extensive experiments, delivering high-quality video object effect erasing across diverse scenarios.

### 🤖 AI 总结

**一句话总结**：提出VOR大规模视频对象移除数据集与EffectErase方法，通过“插入-移除”互逆联合学习，更好地同时去除目标及其阴影/反射等视觉效应并补全连贯背景。

**研究动机**：现有扩散式视频修复/移除方法常能删掉物体，但难以彻底抹除变形、阴影、反射等伴随效应且背景时空一致性不足；同时缺少系统覆盖多类效应与复杂场景的成对数据集限制了训练与评测。

**核心方法**：构建VOR数据集：60K高质量成对视频（含/不含目标及其效应）与对应mask，覆盖五类效应、丰富类别与多目标动态场景；提出EffectErase：将“视频对象插入”作为“移除”的互逆辅助任务，在互惠学习框架中引入任务感知区域引导聚焦受影响区域，并用插入-移除一致性目标约束两任务共享效应区域定位与结构线索、支持灵活任务切换。

**主要结论**：在VOR上训练的EffectErase在大量实验中优于现有方法，能在多样场景下更高质量地擦除对象及其视觉效应并生成更连贯的背景，验证了数据集与互逆一致性学习对效果提升的关键作用。

**关键词**：视频目标移除, 视频补全, Diffusion, 视觉效果擦除, 阴影去除, 反射去除, 形变建模, 辅助任务学习, 互惠学习, 一致性约束, 区域引导

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19224v1) | [下载PDF](https://arxiv.org/pdf/2603.19224v1.pdf)

---

## [12. Spectrally-Guided Diffusion Noise Schedules](https://arxiv.org/abs/2603.19222v1)

**作者**：Carlos Esteves, Ameesh Makadia  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Denoising diffusion models are widely used for high-quality image and video generation. Their performance depends on noise schedules, which define the distribution of noise levels applied during training and the sequence of noise levels traversed during sampling. Noise schedules are typically handcrafted and require manual tuning across different resolutions. In this work, we propose a principled way to design per-instance noise schedules for pixel diffusion, based on the image's spectral properties. By deriving theoretical bounds on the efficacy of minimum and maximum noise levels, we design ``tight'' noise schedules that eliminate redundant steps. During inference, we propose to conditionally sample such noise schedules. Experiments show that our noise schedules improve generative quality of single-stage pixel diffusion models, particularly in the low-step regime.

### 🤖 AI 总结

**一句话总结**：提出一种基于图像频谱特性的“按样本”扩散噪声日程设计与推断采样方法，用更少步数获得更好的生成质量。

**研究动机**：现有扩散模型噪声日程多为手工设定且需随分辨率/数据手动调参，常包含冗余噪声步导致低步数采样质量受限。

**核心方法**：从图像频谱出发推导最小/最大噪声水平有效性的理论界限，据此构造覆盖关键噪声区间的“紧致”日程以去除冗余步骤；推断时根据条件为每个样本自适应地采样相应噪声日程。

**主要结论**：实验表明该频谱引导的自适应噪声日程能提升单阶段像素扩散模型的生成质量，尤其在少步数（low-step）采样设置下收益更明显。

**关键词**：Diffusion, 去噪扩散, 噪声调度, 自适应噪声调度, 频谱引导, 图像频谱特征, 像素扩散, 低步数采样, 紧致调度, 理论界限

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19222v1) | [下载PDF](https://arxiv.org/pdf/2603.19222v1.pdf)

---

## [13. Rethinking Vector Field Learning for Generative Segmentation](https://arxiv.org/abs/2603.19218v1)

**作者**：Chaoyang Wang, Yaobo Liang, Boci Peng 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

Taming diffusion models for generative segmentation has attracted increasing attention. While existing approaches primarily focus on architectural tweaks or training heuristics, there remains a limited understanding of the intrinsic mismatch between continuous flow matching objectives and discrete perception tasks. In this work, we revisit diffusion segmentation from the perspective of vector field learning. We identify two key limitations of the commonly used flow matching objective: gradient vanishing and trajectory traversing, which result in slow convergence and poor class separation. To tackle these issues, we propose a principled vector field reshaping strategy that augments the learned velocity field with a detached distance-aware correction term. This correction introduces both attractive and repulsive interactions, enhancing gradient magnitudes near centroids while preserving the original diffusion training framework. Furthermore, we design a computationally efficient, quasi-random category encoding scheme inspired by Kronecker sequences, which integrates seamlessly with an end-to-end pixel neural field framework for pixel-level semantic alignment. Extensive experiments consistently demonstrate significant improvements over vanilla flow matching approaches, substantially narrowing the performance gap between generative segmentation and strong discriminative specialists.

### 🤖 AI 总结

**一句话总结**：从向量场学习视角重审扩散式生成分割，提出“向量场重塑+高效类别编码”以缓解流匹配训练的梯度与轨迹问题，从而显著提升生成分割性能。

**研究动机**：现有扩散分割多靠结构/训练技巧改良，但连续流匹配目标与离散语义分割存在内在失配，导致收敛慢、类别可分性差。作者指出常用流匹配存在梯度消失与轨迹穿越两大限制，需要更原则的向量场层面修正。

**核心方法**：提出向量场重塑策略：在学习到的速度场上加入“detach 的距离感知修正项”，同时引入吸引/排斥作用以在类中心附近增大梯度并改善类间分离，同时保持原扩散训练框架不变。另设计基于 Kronecker 序列的准随机类别编码，计算高效且可无缝融入端到端的像素神经场，实现像素级语义对齐。

**主要结论**：在多组实验中，相比原始 flow matching 扩散分割方法取得稳定且显著的性能提升，并明显缩小与强判别式分割模型之间的差距。该结果表明对速度向量场进行原则性重塑与更合理的类别表示能有效改善生成分割的训练动力学与语义可分性。

**关键词**：生成式语义分割, Diffusion, 速度场重塑, 距离感知校正, 吸引-排斥交互, 梯度消失, 轨迹遍历, 类别编码

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19218v1) | [下载PDF](https://arxiv.org/pdf/2603.19218v1.pdf)

---

## [14. LVOmniBench: Pioneering Long Audio-Video Understanding Evaluation for Omnimodal LLMs](https://arxiv.org/abs/2603.19217v1)

**作者**：Keda Tao, Yuhua Zheng, Jia Xu 等 16 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

Recent advancements in omnimodal large language models (OmniLLMs) have significantly improved the comprehension of audio and video inputs. However, current evaluations primarily focus on short audio and video clips ranging from 10 seconds to 5 minutes, failing to reflect the demands of real-world applications, where videos typically run for tens of minutes. To address this critical gap, we introduce LVOmniBench, a new benchmark designed specifically for the cross-modal comprehension of long-form audio and video. This dataset comprises high-quality videos sourced from open platforms that feature rich audio-visual dynamics. Through rigorous manual selection and annotation, LVOmniBench comprises 275 videos, ranging in duration from 10 to 90 minutes, and 1,014 question-answer (QA) pairs. LVOmniBench aims to rigorously evaluate the capabilities of OmniLLMs across domains, including long-term memory, temporal localization, fine-grained understanding, and multimodal perception. Our extensive evaluation reveals that current OmniLLMs encounter significant challenges when processing extended audio-visual inputs. Open-source models generally achieve accuracies below 35%, whereas the Gemini 3 Pro reaches a peak accuracy of approximately 65%. We anticipate that this dataset, along with our empirical findings, will stimulate further research and the development of advanced models capable of resolving complex cross-modal understanding problems within long-form audio-visual contexts.

### 🤖 AI 总结

**一句话总结**：提出长时音视频理解评测基准LVOmniBench，用于系统衡量OmniLLM在10–90分钟视频上的跨模态理解能力，并揭示现有模型在长时输入上仍明显不足。

**研究动机**：现有音视频评测多聚焦10秒到5分钟短片，无法覆盖真实场景中“几十分钟”视频所需的长程记忆、时序定位与细粒度理解能力，因此需要专门的长视频音频-视频联合评测基准。

**核心方法**：构建LVOmniBench：从开放平台人工筛选275个高质量长视频（10–90分钟），并人工标注1,014组QA，覆盖长程记忆、时间定位、细粒度理解与多模态感知等能力维度；在该基准上对多种OmniLLM进行系统评测对比。

**主要结论**：实验显示当前OmniLLM在长时音视频跨模态理解上挑战显著：开源模型准确率普遍低于35%，Gemini 3 Pro最高约65%，说明长程跨模态推理与记忆仍是关键瓶颈，基准有望推动更强模型研发。

**关键词**：长视频问答, 多模态基准, 时序定位, 长程记忆, 多模态感知, 长上下文推理, 人工标注数据集, 音视频QA数据集

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19217v1) | [下载PDF](https://arxiv.org/pdf/2603.19217v1.pdf)

---

## [15. DreamPartGen: Semantically Grounded Part-Level 3D Generation via Collaborative Latent Denoising](https://arxiv.org/abs/2603.19216v1)

**作者**：Tianjiao Yu, Xinzhuo Li, Muntasir Wahed 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Understanding and generating 3D objects as compositions of meaningful parts is fundamental to human perception and reasoning. However, most text-to-3D methods overlook the semantic and functional structure of parts. While recent part-aware approaches introduce decomposition, they remain largely geometry-focused, lacking semantic grounding and failing to model how parts align with textual descriptions or their inter-part relations. We propose DreamPartGen, a framework for semantically grounded, part-aware text-to-3D generation. DreamPartGen introduces Duplex Part Latents (DPLs) that jointly model each part's geometry and appearance, and Relational Semantic Latents (RSLs) that capture inter-part dependencies derived from language. A synchronized co-denoising process enforces mutual geometric and semantic consistency, enabling coherent, interpretable, and text-aligned 3D synthesis. Across multiple benchmarks, DreamPartGen delivers state-of-the-art performance in geometric fidelity and text-shape alignment.

### 🤖 AI 总结

**一句话总结**：DreamPartGen 通过语义驱动的部件级协同去噪，在文本约束下生成结构连贯、可解释且与描述对齐的3D物体。

**研究动机**：现有文本到3D方法多忽视“部件”的语义与功能结构，虽有部件分解但偏几何，难以刻画部件与文本含义及部件间关系的对应与约束。

**核心方法**：提出双工部件潜变量（DPLs）联合建模每个部件的几何与外观，并用关系语义潜变量（RSLs）从语言中提取并编码部件间依赖；通过同步协同去噪过程让部件几何与语义相互一致，从而提升整体一致性与文本对齐。

**主要结论**：在多项基准上，DreamPartGen 在几何保真度与文本-形状对齐方面达到SOTA，同时生成结果更具部件可解释性与跨部件的语义一致性。

**关键词**：文本到3D生成, 部件级3D生成, 语义对齐, 部件感知建模, 3D部件分解, 语言条件生成, 部件关系建模, Diffusion, 协同去噪, 潜变量表示, 文本-形状对齐

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19216v1) | [下载PDF](https://arxiv.org/pdf/2603.19216v1.pdf)

---

## [16. Do VLMs Need Vision Transformers? Evaluating State Space Models as Vision Encoders](https://arxiv.org/abs/2603.19209v1)

**作者**：Shang-Jui Ray Kuo, Paola Cascante-Bonilla  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Large vision--language models (VLMs) often use a frozen vision backbone, whose image features are mapped into a large language model through a lightweight connector. While transformer-based encoders are the standard visual backbone, we ask whether state space model (SSM) vision backbones can be a strong alternative. We systematically evaluate SSM vision backbones for VLMs in a controlled setting. Under matched ImageNet-1K initialization, the SSM backbone achieves the strongest overall performance across both VQA and grounding/localization. We further adapt both SSM and ViT-family backbones with detection or segmentation training and find that dense-task tuning generally improves performance across families; after this adaptation, the SSM backbone remains competitive while operating at a substantially smaller model scale. We further observe that (i) higher ImageNet accuracy or larger backbones do not reliably translate into better VLM performance, and (ii) some visual backbones are unstable in localization. Based on these findings, we propose stabilization strategies that improve robustness for both backbone families and highlight SSM backbones as a strong alternative to transformer-based vision encoders in VLMs.

### 🤖 AI 总结

**一句话总结**：在冻结视觉骨干并通过轻量连接器对齐LLM的VLM设定下，基于状态空间模型（SSM）的视觉编码器在VQA与定位/指代任务上整体可与甚至优于ViT，并且在更小模型规模下保持竞争力。

**研究动机**：当前VLM几乎默认使用Transformer/ViT作为视觉骨干，但尚不清楚在相同控制变量下是否存在更高效且同样强的替代方案；作者希望系统验证SSM作为视觉编码器的可行性与优势，并解释VLM性能与骨干规模/分类精度不一致等现象。

**核心方法**：在严格对照实验中，将SSM与ViT家族视觉骨干在相同ImageNet-1K初始化、冻结骨干+轻量连接器的VLM框架下，系统评测VQA与grounding/localization；进一步对两类骨干进行检测/分割等密集任务适配训练，比较适配前后效果，并提出针对定位不稳定的鲁棒化/稳定化策略。

**主要结论**：在匹配初始化条件下，SSM骨干在VQA与定位任务上取得最强总体表现；密集任务调优普遍提升两类骨干的VLM表现且SSM在更小规模下仍具竞争力，同时发现ImageNet精度或更大骨干并不可靠预测VLM效果，部分骨干在定位上存在不稳定性，所提稳定化策略可提升两类骨干的鲁棒性。

**关键词**：视觉-语言模型（VLM）, 视觉编码器, 冻结视觉骨干, 状态空间模型（SSM）骨干, 受控评测, 视觉问答（VQA）, 目标检测微调, 语义分割微调, 鲁棒性稳定化策略

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19209v1) | [下载PDF](https://arxiv.org/pdf/2603.19209v1.pdf)

---

## [17. Reconstruction Matters: Learning Geometry-Aligned BEV Representation through 3D Gaussian Splatting](https://arxiv.org/abs/2603.19193v1)

**作者**：Yiren Lu, Xin Ye, Burhaneddin Yaman 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

Bird's-Eye-View (BEV) perception serves as a cornerstone for autonomous driving, offering a unified spatial representation that fuses surrounding-view images to enable reasoning for various downstream tasks, such as semantic segmentation, 3D object detection, and motion prediction. However, most existing BEV perception frameworks adopt an end-to-end training paradigm, where image features are directly transformed into the BEV space and optimized solely through downstream task supervision. This formulation treats the entire perception process as a black box, often lacking explicit 3D geometric understanding and interpretability, leading to suboptimal performance. In this paper, we claim that an explicit 3D representation matters for accurate BEV perception, and we propose Splat2BEV, a Gaussian Splatting-assisted framework for BEV tasks. Splat2BEV aims to learn BEV feature representations that are both semantically rich and geometrically precise. We first pre-train a Gaussian generator that explicitly reconstructs 3D scenes from multi-view inputs, enabling the generation of geometry-aligned feature representations. These representations are then projected into the BEV space to serve as inputs for downstream tasks. Extensive experiments on nuScenes and argoverse dataset demonstrate that Splat2BEV achieves state-of-the-art performance and validate the effectiveness of incorporating explicit 3D reconstruction into BEV perception.

### 🤖 AI 总结

**一句话总结**：提出Splat2BEV：先用3D Gaussian Splatting显式重建多视角3D场景，再将几何对齐的表示投影到BEV以提升自动驾驶下游任务性能。

**研究动机**：现有BEV方法多为端到端黑盒特征变换，仅靠下游监督学习，缺乏显式3D几何理解与可解释性，导致几何不精确、性能受限。

**核心方法**：预训练一个Gaussian生成器从多视角图像重建3D场景，得到几何对齐且含语义的3D特征表示；随后将该表示投影/聚合到BEV空间，作为分割、检测等下游任务的输入并进行训练。

**主要结论**：在nuScenes与Argoverse上取得SOTA结果，实验表明显式3D重建能够显著增强BEV表示的几何一致性与下游任务效果。

**关键词**：自动驾驶感知, BEV表征学习, 3D重建, 3D高斯泼溅, 多视角图像, 显式几何建模, 几何对齐特征, 语义分割, 3D目标检测, 运动预测

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19193v1) | [下载PDF](https://arxiv.org/pdf/2603.19193v1.pdf)

---

## [18. ARIADNE: A Perception-Reasoning Synergy Framework for Trustworthy Coronary Angiography Analysis](https://arxiv.org/abs/2603.19169v1)

**作者**：Zhan Jin, Yu Luo, Yizhou Zhang 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-19

### 📄 论文摘要

Conventional pixel-wise loss functions fail to enforce topological constraints in coronary vessel segmentation, producing fragmented vascular trees despite high pixel-level accuracy. We present ARIADNE, a two-stage framework coupling preference-aligned perception with RL-based diagnostic reasoning for topologically coherent stenosis detection. The perception module employs DPO to fine-tune the Sa2VA vision-language foundation model using Betti number constraints as preference signals, aligning the policy toward geometrically complete vessel structures rather than pixel-wise overlap metrics. The reasoning module formulates stenosis localization as a Markov Decision Process with an explicit rejection mechanism that autonomously defers ambiguous anatomical candidates such as bifurcations and vessel crossings, shifting from coverage maximization to reliability optimization. On 1,400 clinical angiograms, ARIADNE achieves state-of-the-art centerline Dice of 0.838, reduces false positives by 41% compared to geometric baselines. External validation on multi-center benchmarks ARCADE and XCAD confirms generalization across acquisition protocols. This represents the first application of DPO for topological alignment in medical imaging, demonstrating that preference-based learning over structural constraints mitigates topological violations while maintaining diagnostic sensitivity in interventional cardiology workflows.

### 🤖 AI 总结

**一句话总结**：ARIADNE通过“偏好对齐的血管感知（DPO+拓扑约束）+RL诊断推理（带拒绝机制）”协同，实现更拓扑连贯且更可信的冠脉狭窄检测。

**研究动机**：传统像素级损失难以约束血管树的拓扑结构，导致分割结果虽像素指标高但出现断裂、拓扑违规，从而影响后续狭窄定位的可靠性。临床场景中分叉/交叉等模糊解剖易引发误报，需要从“尽量覆盖”转向“可靠优先”。

**核心方法**：两阶段框架：感知模块用DPO微调Sa2VA视觉语言基础模型，将Betti数等拓扑约束作为偏好信号，引导模型生成几何完整的血管结构；推理模块将狭窄定位建模为MDP，用RL策略在候选部位进行决策，并引入显式拒绝机制以自动跳过分叉、交叉等高不确定区域来降低误报。

**主要结论**：在1400张临床造影上达到SOTA中心线Dice 0.838，并较几何基线减少41%误报；在ARCADE与XCAD多中心外部验证中表现出跨协议泛化。工作还展示了DPO在医学影像中用于“基于结构/拓扑的偏好对齐”的可行性，在保持敏感性的同时显著缓解拓扑违规与不可信预测。

**关键词**：冠状动脉造影分析, 冠脉血管分割, 拓扑约束学习, 偏好优化（DPO）, 视觉语言基础模型, 拓扑一致性血管树, 强化学习诊断推理, 马尔可夫决策过程（MDP）, 冠脉狭窄定位

**评分**：45

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19169v1) | [下载PDF](https://arxiv.org/pdf/2603.19169v1.pdf)

---

## [19. Adaptive Auxiliary Prompt Blending for Target-Faithful Diffusion Generation](https://arxiv.org/abs/2603.19158v1)

**作者**：Kwanyoung Lee, SeungJu Cha, Yebin Ahn 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

Diffusion-based text-to-image (T2I) models have made remarkable progress in generating photorealistic and semantically rich images. However, when the target concepts lie in low-density regions of the training distribution, these models often produce semantically misaligned or structurally inconsistent results. This limitation arises from the long-tailed nature of text-image datasets, where rare concepts or editing instructions are underrepresented. To address this, we introduce Adaptive Auxiliary Prompt Blending (AAPB) - a unified framework that stabilizes the diffusion process in low-density regions. AAPB leverages auxiliary anchor prompts to provide semantic support in rare concept generation and structural support in image editing, ensuring faithful guidance toward the target prompt. Unlike prior heuristic prompt alternation methods, AAPB derives a closed-form adaptive coefficient that optimally balances the influence between the auxiliary anchor and the target prompt at each diffusion step. Grounded in Tweedie's identity, our formulation provides a principled and training-free framework for adaptive prompt blending, ensuring stable and target-faithful generation. We demonstrate the effectiveness of adaptive interpolation over fixed interpolation through controlled experiments and empirically show consistent improvements on the RareBench and FlowEdit datasets, achieving superior semantic accuracy and structural fidelity compared to prior training-free baselines.

### 🤖 AI 总结

**一句话总结**：提出AAPB在扩散生成/编辑中自适应融合目标提示与辅助锚点提示，提升长尾稀有概念的语义对齐与结构一致性。

**研究动机**：现有T2I扩散模型在训练分布低密度（长尾稀有概念或复杂编辑指令）区域容易出现语义偏离或结构不稳定，且固定/启发式的提示交替难以稳定引导。

**核心方法**：AAPB引入辅助“锚点提示”作为语义/结构支撑，并基于Tweedie恒等式推导每个扩散步的闭式自适应系数，在不训练的情况下最优平衡锚点与目标提示的影响以稳定采样轨迹。

**主要结论**：相比固定插值或启发式训练无关基线，自适应插值带来更稳定且更忠实于目标的生成与编辑，在RareBench与FlowEdit上分别提升语义准确性与结构保真度。

**关键词**：Diffusion, 文生图, 提示词融合, 自适应插值, 辅助锚点提示, 长尾分布, 稀有概念生成, 图像编辑, 训练自由方法, 闭式解系数, 语义对齐

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19158v1) | [下载PDF](https://arxiv.org/pdf/2603.19158v1.pdf)

---

## [20. ADAPT: Attention Driven Adaptive Prompt Scheduling and InTerpolating Orthogonal Complements for Rare Concepts Generation](https://arxiv.org/abs/2603.19157v1)

**作者**：Kwanyoung Lee, Hyunwoo Oh, SeungJu Cha 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

Generating rare compositional concepts in text-to-image synthesis remains a challenge for diffusion models, particularly for attributes that are uncommon in the training data. While recent approaches, such as R2F, address this challenge by utilizing LLM for prompt scheduling, they suffer from inherent variance due to the randomness of language models and suboptimal guidance from iterative text embedding switching. To address these problems, we propose the ADAPT framework, a training-free framework that deterministically plans and semantically aligns prompt schedules, providing consistent guidance to enhance the composition of rare concepts. By leveraging attention scores and orthogonal components, ADAPT significantly enhances compositional generation of rare concepts in the RareBench benchmark without additional training or fine-tuning. Through comprehensive experiments, we demonstrate that ADAPT achieves superior performance in RareBench and accurately reflects the semantic information of rare attributes, providing deterministic and precise control over the generation of rare compositions without compromising visual integrity.

### 🤖 AI 总结

**一句话总结**：ADAPT 提出一种无需训练的确定性提示词调度框架，通过注意力驱动的调度与正交补偿插值，显著提升扩散模型对稀有组合概念的生成质量与可控性。

**研究动机**：扩散模型在训练数据中罕见的属性/组合概念上往往生成失败；现有依赖 LLM 的提示调度（如 R2F）受语言模型随机性影响且迭代切换文本嵌入的引导不够稳定、语义对齐不足。

**核心方法**：ADAPT 利用跨步的注意力分数来确定性规划提示词/嵌入的调度顺序与权重，并通过提取与插值“正交补偿分量”（orthogonal complements）来强化稀有属性的语义贡献、减少与主体语义的冲突，从而在采样过程中提供稳定一致的组合引导。

**主要结论**：在 RareBench 上，ADAPT 在不进行额外训练或微调的前提下取得优于现有方法的稀有概念组合生成效果，同时更准确地体现稀有属性语义并保持整体视觉质量，实现更确定、精确的控制。

**关键词**：文生图扩散模型, 稀有概念生成, 组合概念生成, 提示词调度, 无训练方法, 注意力引导, 正交补空间, 语义对齐, 确定性控制, 文本嵌入切换

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19157v1) | [下载PDF](https://arxiv.org/pdf/2603.19157v1.pdf)

---

## [21. GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning](https://arxiv.org/abs/2603.19137v1)

**作者**：Yiren Lu, Yi Du, Disheng Liu 等 6 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-03-19

### 📄 论文摘要

Effective embodied exploration requires agents to accumulate and retain spatial knowledge over time. However, existing scene representations, such as discrete scene graphs or static view-based snapshots, lack \textit{post-hoc re-observability}. If an initial observation misses a target, the resulting memory omission is often irrecoverable. To bridge this gap, we propose \textbf{GSMem}, a zero-shot embodied exploration and reasoning framework built upon 3D Gaussian Splatting (3DGS). By explicitly parameterizing continuous geometry and dense appearance, 3DGS serves as a persistent spatial memory that endows the agent with \textit{Spatial Recollection}: the ability to render photorealistic novel views from optimal, previously unoccupied viewpoints. To operationalize this, GSMem employs a retrieval mechanism that simultaneously leverages parallel object-level scene graphs and semantic-level language fields. This complementary design robustly localizes target regions, enabling the agent to ``hallucinate'' optimal views for high-fidelity Vision-Language Model (VLM) reasoning. Furthermore, we introduce a hybrid exploration strategy that combines VLM-driven semantic scoring with a 3DGS-based coverage objective, balancing task-aware exploration with geometric coverage. Extensive experiments on embodied question answering and lifelong navigation demonstrate the robustness and effectiveness of our framework

### 🤖 AI 总结

**一句话总结**：GSMem 将 3D Gaussian Splatting 用作可“再观察”的持久空间记忆，使具身智能体能在零样本条件下渲染最优新视角并提升探索与推理表现。

**研究动机**：传统记忆表示（如离散场景图或静态视角快照）缺乏事后可重访能力，一旦初次观察遗漏目标，记忆缺口难以弥补。作者希望让智能体能从更优但未曾占据的视点“回想/重渲染”场景以支持后续定位与VLM推理。

**核心方法**：以 3DGS 显式建模连续几何与稠密外观作为持久空间记忆，并提出同时利用对象级场景图与语义级语言场的检索机制来定位目标区域。结合“从记忆中渲染最优视角供VLM推理”的空间回忆能力，以及融合 VLM 语义打分与 3DGS 覆盖度目标的混合探索策略，实现任务导向与几何覆盖的平衡。

**主要结论**：在具身问答与终身导航实验中，GSMem 相比依赖静态观察/离散记忆的方案更鲁棒，能更好地找目标并回答问题。结果表明 3DGS 作为可渲染的持久空间记忆能显著提升零样本探索与推理效果。

**关键词**：3D 高斯泼溅（3DGS）, 持续空间记忆, 具身探索, 零样本具身推理, 新视角合成, 视觉语言模型（VLM）推理, 混合探索策略, 几何覆盖目标, 具身问答

**评分**：46

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19137v1) | [下载PDF](https://arxiv.org/pdf/2603.19137v1.pdf)

---

## cs.LG

## [22. Robustness, Cost, and Attack-Surface Concentration in Phishing Detection](https://arxiv.org/abs/2603.19204v1)

**作者**：Julian Allagan, Mohamed Elbakary, Zohreh Safari 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Phishing detectors built on engineered website features attain near-perfect accuracy under i.i.d.\ evaluation, yet deployment security depends on robustness to post-deployment feature manipulation. We study this gap through a cost-aware evasion framework that models discrete, monotone feature edits under explicit attacker budgets. Three diagnostics are introduced: minimal evasion cost (MEC), the evasion survival rate $S(B)$, and the robustness concentration index (RCI).   On the UCI Phishing Websites benchmark (11\,055 instances, 30 ternary features), Logistic Regression, Random Forests, Gradient Boosted Trees, and XGBoost all achieve $\mathrm{AUC}\ge 0.979$ under static evaluation. Under budgeted sanitization-style evasion, robustness converges across architectures: the median MEC equals 2 with full features, and over 80\% of successful minimal-cost evasions concentrate on three low-cost surface features. Feature restriction improves robustness only when it removes all dominant low-cost transitions. Under strict cost schedules, infrastructure-leaning feature sets exhibit 17-19\% infeasible mass for ensemble models, while the median MEC among evadable instances remains unchanged. We formalize this convergence: if a positive fraction of correctly detected phishing instances admit evasion through a single feature transition of minimal cost $c_{\min}$, no classifier can raise the corresponding MEC quantile above $c_{\min}$ without modifying the feature representation or cost model. Adversarial robustness in phishing detection is governed by feature economics rather than model complexity.

### 🤖 AI 总结

**一句话总结**：论文指出钓鱼检测在静态评测下虽接近满分，但在“带成本的特征篡改”对抗下各模型鲁棒性迅速收敛，关键瓶颈在低成本特征面的经济性而非模型复杂度。

**研究动机**：现有钓鱼检测器在i.i.d.测试上表现极好，但真实部署中攻击者会在预算约束下操纵网站特征以逃逸检测，静态指标无法反映这种安全风险与脆弱点集中现象。

**核心方法**：提出成本感知的逃逸框架，建模离散且单调的特征编辑并显式加入攻击预算；定义三类诊断指标：最小逃逸成本(MEC)、预算下生存率S(B)与鲁棒性集中指数(RCI)，并在UCI钓鱼数据集上评估LR/RF/GBT/XGBoost等模型及不同特征子集与成本表设置。

**主要结论**：尽管AUC均≥0.979，预算化逃逸下各架构的中位MEC都≈2且80%以上的最小成本逃逸集中在3个低成本“攻击面”特征；限制特征只有在移除所有主导的低成本转移时才显著增鲁棒性，而在存在最小成本单特征转移的情况下，任何分类器都无法把相应MEC分位数抬高到超过c_min，除非改变特征表示或成本模型。

**关键词**：钓鱼检测, 成本感知规避, 攻击者预算, 特征编辑, 离散单调扰动, 最小规避成本（MEC）, 规避生存率 S(B, 鲁棒性集中指数（RCI）, 攻击面集中, 特征经济学

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19204v1) | [下载PDF](https://arxiv.org/pdf/2603.19204v1.pdf)

---

## [23. Improving RCT-Based Treatment Effect Estimation Under Covariate Mismatch via Calibrated Alignment](https://arxiv.org/abs/2603.19186v1)

**作者**：Amir Asiaee, Samhita Pal  
**分类**：cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Randomized controlled trials (RCTs) are the gold standard for estimating heterogeneous treatment effects, yet they are often underpowered for detecting effect heterogeneity. Large observational studies (OS) can supplement RCTs for conditional average treatment effect (CATE) estimation, but a key barrier is covariate mismatch: the two sources measure different, only partially overlapping, covariates. We propose CALM (Calibrated ALignment under covariate Mismatch), which bypasses imputation by learning embeddings that map each source's features into a common representation space. OS outcome models are transferred to the RCT embedding space and calibrated using trial data, preserving causal identification from randomization. Finite-sample risk bounds decompose into alignment error, outcome-model complexity, and calibration complexity terms, identifying when embedding alignment outperforms imputation. Under the calibration-based linear variant, the framework provides protection against negative transfer; the neural variant can be vulnerable under severe distributional shift. Under sparse linear models, the embedding approach strictly generalizes imputation. Simulations across 51 settings confirm that (i) calibration-based methods are equivalent for linear CATEs, and (ii) the neural embedding variant wins all 22 nonlinear-regime settings with large margins.

### 🤖 AI 总结

**一句话总结**：CALM通过学习跨数据源的共同嵌入并在RCT上校准，将观测研究的大样本信息安全迁移到RCT中以提升CATE估计。

**研究动机**：RCT对异质性效应（CATE）往往统计功效不足，而观测研究样本大但与RCT存在协变量不匹配（仅部分重叠），使直接融合或靠插补变得不可靠。

**核心方法**：提出CALM：为RCT与OS分别学习映射到同一表征空间的嵌入，先在OS上训练结局模型并转移到RCT嵌入空间，再用RCT数据进行校准以保持随机化带来的因果识别；同时给出有限样本风险界，将误差分解为对齐误差、结局模型复杂度与校准复杂度，并讨论线性/神经两种实现及负迁移保护。

**主要结论**：理论上嵌入对齐在特定条件下优于插补，且在线性校准版本下可避免负迁移，而神经版本在严重分布漂移时可能更脆弱；实验覆盖51种设置显示线性CATE下多种校准法等价，而非线性场景中神经嵌入版本在22个设置中均显著最佳。

**关键词**：异质性处理效应估计, 条件平均处理效应（CATE）, 随机对照试验（RCT）, 观测研究数据融合, 协变量不匹配, 表示学习对齐, 校准迁移学习, 负迁移防护, 分布偏移鲁棒性, 有限样本风险界

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19186v1) | [下载PDF](https://arxiv.org/pdf/2603.19186v1.pdf)

---

## [24. MIDST Challenge at SaTML 2025: Membership Inference over Diffusion-models-based Synthetic Tabular data](https://arxiv.org/abs/2603.19185v1)

**作者**：Masoumeh Shafieinejad, Xi He, Mahshid Alinoori 等 9 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Synthetic data is often perceived as a silver-bullet solution to data anonymization and privacy-preserving data publishing. Drawn from generative models like diffusion models, synthetic data is expected to preserve the statistical properties of the original dataset while remaining resilient to privacy attacks. Recent developments of diffusion models have been effective on a wide range of data types, but their privacy resilience, particularly for tabular formats, remains largely unexplored. MIDST challenge sought a quantitative evaluation of the privacy gain of synthetic tabular data generated by diffusion models, with a specific focus on its resistance to membership inference attacks (MIAs). Given the heterogeneity and complexity of tabular data, multiple target models were explored for MIAs, including diffusion models for single tables of mixed data types and multi-relational tables with interconnected constraints. MIDST inspired the development of novel black-box and white-box MIAs tailored to these target diffusion models as a key outcome, enabling a comprehensive evaluation of their privacy efficacy. The MIDST GitHub repository is available at https://github.com/VectorInstitute/MIDST

### 🤖 AI 总结

**一句话总结**：MIDST 挑战系统评估了基于扩散模型生成的合成表格数据在成员推断攻击（MIA）下的隐私韧性，并推动了针对该类模型的黑盒/白盒攻击方法发展。

**研究动机**：合成数据常被视为隐私发布的“银弹”，但扩散模型生成的表格合成数据在隐私攻击（尤其成员推断）下的真实抗性仍缺乏定量研究。表格数据类型混杂且常含多表关系约束，使得隐私评估更复杂、亟需标准化基准。

**核心方法**：通过 MIDST 挑战构建评测框架：以扩散模型为目标生成单表混合类型与多关系表合成数据，并在此基础上设计/对比多种面向这些扩散目标模型的成员推断攻击（包含黑盒与白盒设置）。最终以攻击效果对“隐私增益”进行量化评估，并开源基准与代码库。

**主要结论**：MIDST 表明需要用专门适配扩散模型与表格结构的 MIA（黑盒/白盒）来全面衡量合成表格数据的隐私效用；同时该挑战产出了可复现的评测资源与新型攻击思路，为后续检验扩散合成表格数据的隐私有效性提供了标准化工具链。

**关键词**：Diffusion, 合成表格数据, 隐私评估, 成员推断攻击, 黑盒攻击, 白盒攻击, 隐私增益度量, 数据匿名化, 隐私保护数据发布, 多关系表格数据, 混合类型表格数据, 安全性基准测试

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19185v1) | [下载PDF](https://arxiv.org/pdf/2603.19185v1.pdf)

---

## [25. SOL-ExecBench: Speed-of-Light Benchmarking for Real-World GPU Kernels Against Hardware Limits](https://arxiv.org/abs/2603.19173v1)

**作者**：Edward Lin, Sahil Modi, Siva Kumar Sastry Hari 等 33 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-19

### 📄 论文摘要

As agentic AI systems become increasingly capable of generating and optimizing GPU kernels, progress is constrained by benchmarks that reward speedup over software baselines rather than proximity to hardware-efficient execution. We present SOL-ExecBench, a benchmark of 235 CUDA kernel optimization problems extracted from 124 production and emerging AI models spanning language, diffusion, vision, audio, video, and hybrid architectures, targeting NVIDIA Blackwell GPUs. The benchmark covers forward and backward workloads across BF16, FP8, and NVFP4, including kernels whose best performance is expected to rely on Blackwell-specific capabilities. Unlike prior benchmarks that evaluate kernels primarily relative to software implementations, SOL-ExecBench measures performance against analytically derived Speed-of-Light (SOL) bounds computed by SOLAR, our pipeline for deriving hardware-grounded SOL bounds, yielding a fixed target for hardware-efficient optimization. We report a SOL Score that quantifies how much of the gap between a release-defined scoring baseline and the hardware SOL bound a candidate kernel closes. To support robust evaluation of agentic optimizers, we additionally provide a sandboxed harness with GPU clock locking, L2 cache clearing, isolated subprocess execution, and static analysis based checks against common reward-hacking strategies. SOL-ExecBench reframes GPU kernel benchmarking from beating a mutable software baseline to closing the remaining gap to hardware Speed-of-Light.

### 🤖 AI 总结

**一句话总结**：SOL-ExecBench 提供面向 NVIDIA Blackwell 的真实 CUDA 内核优化基准，用“接近硬件 Speed-of-Light 上限”而非“相对软件基线提速”来衡量优化质量。

**研究动机**：现有内核优化基准多奖励相对某个软件实现的速度提升，但软件基线可变且不等价于硬件高效执行，导致难以衡量与硬件极限的真实差距。随着 agentic AI 自动生成/优化内核能力增强，需要一个以硬件上限为固定目标、可防奖励黑客的评测体系。

**核心方法**：构建包含 235 个来自 124 个生产/新兴 AI 模型的 CUDA 内核优化任务（覆盖前/后向、BF16/FP8/NVFP4，并包含依赖 Blackwell 特性的内核），并用 SOLAR 分析推导每个内核的硬件 SOL 上界。提出 SOL Score 衡量候选内核相对“发布定义的基线”向 SOL 上界缩小了多少差距，并提供带 GPU 锁频、L2 清理、隔离执行与静态检查的沙箱评测框架以减少 reward hacking。

**主要结论**：该基准将评测目标从“击败软件基线”转为“逼近硬件 Speed-of-Light”，提供稳定且硬件对齐的优化尺度，并通过更严格的评测环境提升对自动化/智能体优化器的鲁棒性与可比性。

**关键词**：GPU内核优化基准, 解析性能上界建模, 硬件感知性能评估, 智能体优化器评测, 前向与反向算子, GPU性能隔离与可复现评测, 奖励黑客防护（静态分析）, SOL-ExecBench

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19173v1) | [下载PDF](https://arxiv.org/pdf/2603.19173v1.pdf)

---

## [26. Rigorous Error Certification for Neural PDE Solvers: From Empirical Residuals to Solution Guarantees](https://arxiv.org/abs/2603.19165v1)

**作者**：Amartya Mukherjee, Maxwell Fitzsimmons, David C. Del Rey Fernández 等 4 位作者  
**分类**：cs.LG, math.AP, math.FA  
**发布时间**：2026-03-19

### 📄 论文摘要

Uncertainty quantification for partial differential equations is traditionally grounded in discretization theory, where solution error is controlled via mesh/grid refinement. Physics-informed neural networks fundamentally depart from this paradigm: they approximate solutions by minimizing residual losses at collocation points, introducing new sources of error arising from optimization, sampling, representation, and overfitting. As a result, the generalization error in the solution space remains an open problem.   Our main theoretical contribution establishes generalization bounds that connect residual control to solution-space error. We prove that when neural approximations lie in a compact subset of the solution space, vanishing residual error guarantees convergence to the true solution. We derive deterministic and probabilistic convergence results and provide certified generalization bounds translating residual, boundary, and initial errors into explicit solution error guarantees.

### 🤖 AI 总结

**一句话总结**：本文为神经网络PDE求解器（如PINNs）建立从“经验残差”到“解空间误差”的严格泛化/误差认证界限，使残差变小可转化为对真实解误差的可证明保证。

**研究动机**：传统PDE不确定性量化依赖网格离散误差理论与加密控制，但PINNs通过采样点最小化残差会引入优化、采样、表示与过拟合等新误差源，导致解空间泛化误差缺乏理论保证。

**核心方法**：理论上证明：当神经近似解落在解空间的某个紧致子集内时，残差误差趋于0即可保证收敛到真实解；进一步给出确定性与概率性收敛结果，并推导将残差/边界/初值误差显式映射为解空间误差上界的认证泛化界。

**主要结论**：在适当紧致性假设下，控制PDE残差与边界/初值误差不仅是经验指标，而且能提供对解空间误差的严格上界与收敛保证，从而把PINNs的“残差最小化”提升为可认证的解质量保证机制。

**关键词**：物理信息神经网络（PINN）, 偏微分方程（PDE）求解, 误差认证, 泛化误差界, 残差最小化, 解空间误差估计, 不确定性量化（UQ）, 配点采样误差, 确定性收敛, 概率收敛, 边界条件误差, 初值条件误差

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19165v1) | [下载PDF](https://arxiv.org/pdf/2603.19165v1.pdf)

---

## [27. Enhancing Pretrained Model-based Continual Representation Learning via Guided Random Projection](https://arxiv.org/abs/2603.19145v1)

**作者**：Ruilin Li, Heming Zou, Xiufeng Yan 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Recent paradigms in Random Projection Layer (RPL)-based continual representation learning have demonstrated superior performance when building upon a pre-trained model (PTM). These methods insert a randomly initialized RPL after a PTM to enhance feature representation in the initial stage. Subsequently, a linear classification head is used for analytic updates in the continual learning stage. However, under severe domain gaps between pre-trained representations and target domains, a randomly initialized RPL exhibits limited expressivity under large domain shifts. While largely scaling up the RPL dimension can improve expressivity, it also induces an ill-conditioned feature matrix, thereby destabilizing the recursive analytic updates of the linear head. To this end, we propose the Stochastic Continual Learner with MemoryGuard Supervisory Mechanism (SCL-MGSM). Unlike random initialization, MGSM constructs the projection layer via a principled, data-guided mechanism that progressively selects target-aligned random bases to adapt the PTM representation to downstream tasks. This facilitates the construction of a compact yet expressive RPL while improving the numerical stability of analytic updates. Extensive experiments on multiple exemplar-free Class Incremental Learning (CIL) benchmarks demonstrate that SCL-MGSM achieves superior performance compared to state-of-the-art methods.

### 🤖 AI 总结

**一句话总结**：提出一种数据引导的随机投影层构建机制（SCL-MGSM），在大域偏移下以更紧凑且稳定的方式增强PTM特征并提升无样本类增量学习性能。

**研究动机**：现有PTM+随机投影层(RPL)方法在预训练域与目标域差距大时，随机初始化的RPL表达能力不足；而盲目增大RPL维度虽可增强表达，但会导致特征矩阵病态、解析式递归更新的线性头数值不稳定。

**核心方法**：SCL-MGSM用MemoryGuard监督机制替代纯随机初始化，通过数据引导逐步选择与目标域更对齐的“随机基”来构造投影层，使PTM表征更好适配下游任务；同时保持投影层紧凑并改善特征条件数，从而稳定线性分类头的解析更新。

**主要结论**：在多个无回放(Class Incremental Learning)基准上，SCL-MGSM相较现有SOTA取得更优表现，并在大域移场景下兼顾了表示能力与解析更新的数值稳定性。

**关键词**：持续表征学习, 持续学习, 类增量学习, 无样本回放, 预训练模型适配, 随机投影层, 引导随机投影, 数据引导基选择, 解析式线性分类器更新, 数值稳定性, 领域偏移

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19145v1) | [下载PDF](https://arxiv.org/pdf/2603.19145v1.pdf)

---

## [28. SHAPCA: Consistent and Interpretable Explanations for Machine Learning Models on Spectroscopy Data](https://arxiv.org/abs/2603.19141v1)

**作者**：Mingxing Zhang, Nicola Rossberg, Simone Innocente 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

In recent years, machine learning models have been increasingly applied to spectroscopic datasets for chemical and biomedical analysis. For their successful adoption, particularly in clinical and safety-critical settings, professionals and researchers must be able to understand and trust the reasoning behind model predictions. However, the inherently high dimensionality and strong collinearity of spectroscopy data pose a fundamental challenge to model explainability. These properties not only complicate model training but also undermine the stability and consistency of explanations, leading to fluctuations in feature importance across repeated training runs. Feature extraction techniques have been used to reduce the input dimensionality; these new features hinder the connection between the prediction and the original signal. This study proposes SHAPCA, an explainable machine learning pipeline that combines Principal Component Analysis (for dimensionality reduction) and Shapely Additive exPlanations (for post hoc explanation) to provide explanations in the original input space, which a practitioner can interpret and link back to the biological components. The proposed framework enables analysis from both global and local perspectives, revealing the spectral bands that drive overall model behaviour as well as the instance-specific features that influence individual predictions. Numerical analysis demonstrated the interpretability of the results and greater consistency across different runs.

### 🤖 AI 总结

**一句话总结**：SHAPCA 将PCA降维与SHAP解释结合，把光谱机器学习模型的特征贡献稳定地映射回原始光谱波段，从而提供一致且可解释的全局/局部解释。

**研究动机**：光谱数据高维且强共线性会导致模型解释不稳定、不同训练重复下特征重要性波动；而常见特征提取又削弱了与原始光谱信号（生物/化学成分）的对应关系。

**核心方法**：提出SHAPCA流程：先用PCA对光谱输入降维训练模型，再用SHAP进行事后解释，并将SHAP贡献从主成分空间回投到原始波长/波段空间，支持全局重要波段与单样本局部解释。

**主要结论**：实验数值分析表明，该方法能在原始光谱空间给出更可解释的关键波段，并相比直接在高维输入上解释具有更高的一致性与跨运行稳定性。

**关键词**：光谱数据, 可解释机器学习, 特征重要性稳定性, 高维共线性, 主成分分析（PCA）, 后验解释, 原始输入空间归因, 全局解释, 局部解释, 光谱波段归因, 安全关键场景

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19141v1) | [下载PDF](https://arxiv.org/pdf/2603.19141v1.pdf)

---

## [29. Hierarchical Latent Structure Learning through Online Inference](https://arxiv.org/abs/2603.19139v1)

**作者**：Ines Aitsahalia, Kiyohito Iigaya  
**分类**：cs.LG, q-bio.NC  
**发布时间**：2026-03-19

### 📄 论文摘要

Learning systems must balance generalization across experiences with discrimination of task-relevant details. Effective learning therefore requires representations that support both. Online latent-cause models support incremental inference but assume flat partitions, whereas hierarchical Bayesian models capture multilevel structure but typically require offline inference. We introduce the Hierarchical Online Learning of Multiscale Experience Structure (HOLMES) model, a computational framework for hierarchical latent structure learning through online inference. HOLMES combines a variation on the nested Chinese Restaurant Process prior with sequential Monte Carlo inference to perform tractable trial-by-trial inference over hierarchical latent representations without explicit supervision over the latent structure. In simulations, HOLMES matched the predictive performance of flat models while learning more compact representations that supported one-shot transfer to higher-level latent categories. In a context-dependent task with nested temporal structure, HOLMES also improved outcome prediction relative to flat models. These results provide a tractable computational framework for discovering hierarchical structure in sequential data.

### 🤖 AI 总结

**一句话总结**：HOLMES提出一种可在线推断的层级潜在因果模型，在逐步学习中同时获得良好预测性能与更紧凑的多层表示，并支持高层类别的一次性迁移。

**研究动机**：在线潜在因果模型易于增量推断但只能学到“扁平”划分，而层级贝叶斯模型能表达多层结构却常依赖离线推断；作者希望在不监督潜变量结构的情况下，实现可扩展的在线层级结构学习。

**核心方法**：HOLMES结合改造的嵌套中式餐馆过程（nCRP）作为层级先验，并用序列蒙特卡洛（SMC）进行逐试次的近似后验更新，从而在序列数据中在线推断多尺度的层级潜在表示。

**主要结论**：仿真结果显示，HOLMES在预测性能上可与扁平模型匹配，但能学到更紧凑的层级表示并对高层潜在类别实现一次性迁移；在具有嵌套时间结构的情境依赖任务中，HOLMES也优于扁平模型的结果预测。

**关键词**：层级潜变量结构学习, 层级贝叶斯模型, 嵌套中餐馆过程（nCRP）, 序贯蒙特卡洛（SMC）, 试次级增量学习, 多尺度表征学习, 序列数据建模, 上下文依赖预测, 嵌套时间结构

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19139v1) | [下载PDF](https://arxiv.org/pdf/2603.19139v1.pdf)

---

## [30. Adaptive Regime-Aware Stock Price Prediction Using Autoencoder-Gated Dual Node Transformers with Reinforcement Learning Control](https://arxiv.org/abs/2603.19136v1)

**作者**：Mohammad Al Ridhawi, Mahtab Haj Ali, Hussein Al Osman  
**分类**：cs.LG, cs.AI, q-fin.ST  
**发布时间**：2026-03-19

### 📄 论文摘要

Stock markets exhibit regime-dependent behavior where prediction models optimized for stable conditions often fail during volatile periods. Existing approaches typically treat all market states uniformly or require manual regime labeling, which is expensive and quickly becomes stale as market dynamics evolve. This paper introduces an adaptive prediction framework that adaptively identifies deviations from normal market conditions and routes data through specialized prediction pathways. The architecture consists of three components: (1) an autoencoder trained on normal market conditions that identifies anomalous regimes through reconstruction error, (2) dual node transformer networks specialized for stable and event-driven market conditions respectively, and (3) a Soft Actor-Critic reinforcement learning controller that adaptively tunes the regime detection threshold and pathway blending weights based on prediction performance feedback. The reinforcement learning component enables the system to learn adaptive regime boundaries, defining anomalies as market states where standard prediction approaches fail. Experiments on 20 S&P 500 stocks spanning 1982 to 2025 demonstrate that the proposed framework achieves 0.68% MAPE for one-day predictions without the reinforcement controller and 0.59% MAPE with the full adaptive system, compared to 0.80% for the baseline integrated node transformer. Directional accuracy reaches 72% with the complete framework. The system maintains robust performance during high-volatility periods, with MAPE below 0.85% when baseline models exceed 1.5%. Ablation studies confirm that each component contributes meaningfully: autoencoder routing accounts for 36% relative MAPE degradation upon removal, followed by the SAC controller at 15% and the dual-path architecture at 7%.

### 🤖 AI 总结

**一句话总结**：提出一种可自适应识别市场状态并动态切换/融合预测路径的框架，在高波动行情下显著提升股票短期预测精度与稳健性。

**研究动机**：股票市场存在“稳定/事件驱动”等不同制度(regime)，统一模型在波动期易失效，而人工标注制度成本高且易过时。需要一个能自动发现异常制度并随市场演化自我调整边界的预测系统。

**核心方法**：用仅在“正常市场”上训练的自编码器以重构误差进行异常制度检测与路由；并设置面向稳定与事件驱动两类行情的双Transformer预测分支。再用Soft Actor-Critic强化学习控制器根据预测反馈自适应调节异常阈值与两分支的混合权重，从而学习动态制度边界。

**主要结论**：在20只标普股票(1982–2025)上，一日预测MAPE由基线0.80%降至完整系统0.59%(无RL为0.68%)，方向准确率达72%，且在高波动期仍保持MAPE<0.85%。消融显示自编码器路由贡献最大（移除导致相对MAPE恶化36%），其次为SAC控制器(15%)与双路径结构(7%)。

**关键词**：股价预测, 市场状态切换, 自适应状态检测, 异常检测, 自编码器重构误差, 门控路由, 强化学习控制, 阈值自适应调节, 高波动鲁棒性

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19136v1) | [下载PDF](https://arxiv.org/pdf/2603.19136v1.pdf)

---

