# arXiv AI 论文日报 | 2026-03-20

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

**一句话总结**：OS-Themis 提出一种可扩展的多智能体“评审/裁判”框架，把GUI轨迹拆成可验证里程碑并审计证据链，从而显著提升GUI奖励评估质量并促进RL训练效果。

**研究动机**：GUI智能体在随机环境中的RL训练对奖励函数质量极其敏感，而现有奖励评估方法往往难以同时兼顾可扩展性与准确性，导致训练不稳定或性能受限。

**核心方法**：OS-Themis 采用多智能体critic，将轨迹分解为可核验的里程碑以定位关键证据，并通过复核机制严格审核证据链后再给出最终判定；同时引入跨平台的GUI结果奖励基准 OmniGUIRewardBench (OGRBench) 用于系统评测。

**主要结论**：在AndroidWorld实验中，OS-Themis 支持在线RL训练带来10.3%提升，用于自训练循环中的轨迹验证与过滤带来6.9%提升；在OGRBench上各模型在OS-Themis下取得最佳表现，证明其奖励评估更可靠且可推动智能体持续进化。

**关键词**：强化学习奖励函数, 奖励评估模型, 多智能体评论器, 轨迹分解, 里程碑验证, 证据链审计, 跨平台评测基准, 自训练轨迹过滤

**评分**：53

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19191v1) | [下载PDF](https://arxiv.org/pdf/2603.19191v1.pdf)

---

## [2. Box Maze: A Process-Control Architecture for Reliable LLM Reasoning](https://arxiv.org/abs/2603.19182v1)

**作者**：Zou Qiang  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-03-19

### 📄 论文摘要

Large language models (LLMs) demonstrate strong generative capabilities but remain vulnerable to hallucination and unreliable reasoning under adversarial prompting. Existing safety approaches -- such as reinforcement learning from human feedback (RLHF) and output filtering -- primarily operate at the behavioral level and may lack explicit architectural mechanisms for enforcing reasoning process integrity.   This paper proposes the Box Maze framework, a conceptual process-control architecture that decomposes LLM reasoning into three explicit layers: memory grounding, structured inference, and boundary enforcement. We introduce preliminary simulation-based evaluation involving progressive boundary erosion scenarios across multiple heterogeneous LLM systems (DeepSeek-V3, Doubao, Qwen). Results from n=50 adversarial scenarios suggest that explicit cognitive control layers may improve consistency in boundary maintenance, with architectural constraints reducing boundary failure rates from approximately 40% (baseline RLHF) to below 1% under adversarial conditions.   While current validation is simulation-based, these preliminary results indicate that process-level control may offer a promising direction for improving reliability in large language model reasoning.

### 🤖 AI 总结

**一句话总结**：提出“Box Maze”过程控制架构，将LLM推理拆成可控的三层机制，以在对抗提示下显著降低推理越界与不可靠性。

**研究动机**：现有RLHF与输出过滤多停留在行为层面，缺少对“推理过程完整性”的显式约束，导致LLM在对抗诱导下仍易出现幻觉与边界失守。

**核心方法**：框架将推理过程分解为三层：记忆锚定（memory grounding）、结构化推断（structured inference）、边界执行（boundary enforcement），并用“渐进式边界侵蚀”的仿真对抗场景在多模型（DeepSeek-V3、Doubao、Qwen）上评估其边界维持能力。

**主要结论**：在n=50对抗仿真中，加入显式过程控制层可将边界失败率从约40%（RLHF基线）降至1%以下，提示过程级架构约束可能比纯行为对齐更能提升推理可靠性，但目前证据主要来自仿真验证。

**关键词**：过程控制架构, 推理可靠性, 幻觉抑制, 推理过程完整性, 记忆接地, 结构化推理, 边界约束, 认知控制层, 模拟评测, 边界侵蚀测试

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19182v1) | [下载PDF](https://arxiv.org/pdf/2603.19182v1.pdf)

---

## [3. cuGenOpt: A GPU-Accelerated General-Purpose Metaheuristic Framework for Combinatorial Optimization](https://arxiv.org/abs/2603.19163v1)

**作者**：Yuyang Liu  
**分类**：cs.AI, cs.DC  
**发布时间**：2026-03-19

### 📄 论文摘要

Combinatorial optimization problems arise in logistics, scheduling, and resource allocation, yet existing approaches face a fundamental trade-off among generality, performance, and usability. We present cuGenOpt, a GPU-accelerated general-purpose metaheuristic framework that addresses all three dimensions simultaneously.   At the engine level, cuGenOpt adopts a "one block evolves one solution" CUDA architecture with a unified encoding abstraction (permutation, binary, integer), a two-level adaptive operator selection mechanism, and hardware-aware resource management. At the extensibility level, a user-defined operator registration interface allows domain experts to inject problem-specific CUDA search operators. At the usability level, a JIT compilation pipeline exposes the framework as a pure-Python API, and an LLM-based modeling assistant converts natural-language problem descriptions into executable solver code.   Experiments across five thematic suites on three GPU architectures (T4, V100, A800) show that cuGenOpt outperforms general MIP solvers by orders of magnitude, achieves competitive quality against specialized solvers on instances up to n=150, and attains 4.73% gap on TSP-442 within 30s. Twelve problem types spanning five encoding variants are solved to optimality. Framework-level optimizations cumulatively reduce pcb442 gap from 36% to 4.73% and boost VRPTW throughput by 75-81%.   Code: https://github.com/L-yang-yang/cugenopt

### 🤖 AI 总结

**一句话总结**：cuGenOpt 是一个面向组合优化的通用GPU元启发式框架，通过统一编码、CUDA并行架构与可扩展算子接口，在通用性、性能和易用性上同时取得高水平。

**研究动机**：现有组合优化求解器常在“通用性-性能-易用性”之间难以兼顾：通用MIP/CP往往慢，专用启发式又难复用且开发成本高。作者希望用GPU并行把通用元启发式做成可扩展、易用且足够强的框架。

**核心方法**：提出“One block evolves one solution”的CUDA执行架构，配合统一编码抽象（排列/二进制/整数等）、两级自适应算子选择与硬件感知资源管理；同时提供用户自定义CUDA算子注册以注入领域知识，并用JIT将其封装为纯Python API，外加基于LLM的建模助手把自然语言描述转成可执行求解代码。

**主要结论**：在T4/V100/A800上、覆盖多套基准与12类问题的实验表明，cuGenOpt 相比通用MIP求解器可实现数量级加速，并在最高n=150的实例上达到与专用求解器有竞争力的质量；例如TSP-442在30秒内达到4.73% gap，框架级优化也显著提升了解质量与VRPTW吞吐（75–81%）。

**关键词**：组合优化, 元启发式算法, 统一编码抽象, 自适应算子选择, 硬件感知资源管理, LLM建模助手, 车辆路径问题（时间窗）, cuGenOpt

**评分**：47

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19163v1) | [下载PDF](https://arxiv.org/pdf/2603.19163v1.pdf)

---

## [4. D5P4: Partition Determinantal Point Process for Diversity in Parallel Discrete Diffusion Decoding](https://arxiv.org/abs/2603.19146v1)

**作者**：Jonathan Lys, Vincent Gripon, Bastien Pasdeloup 等 7 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Discrete diffusion models are promising alternatives to autoregressive approaches for text generation, yet their decoding methods remain under-studied. Standard decoding methods for autoregressive models, such as beam search, do not directly apply to iterative denoising, and existing diffusion decoding techniques provide limited control over in-batch diversity. To bridge this gap, we introduce a generalized beam-search framework for discrete diffusion that generates candidates in parallel and supports modular beam-selection objectives. As a diversity-focused instantiation, we propose D5P4, which formulates the selection step as MAP inference over a Determinantal Point Process. Leveraging a scalable greedy solver, D5P4 maintains multi-GPU compatibility and enables an explicit trade-off between model probability and target diversity with near-zero compute overhead. Experiments on free-form generation and question answering demonstrate that D5P4 improves diversity over strong baselines while maintaining competitive generation quality.

### 🤖 AI 总结

**一句话总结**：D5P4提出一种适用于离散扩散解码的并行“广义beam-search”框架，并用DPP做候选选择以在几乎零额外开销下显式提升批内多样性。

**研究动机**：离散扩散文本生成的迭代去噪过程使传统beam search难以直接套用，且现有扩散解码对同一批次候选的多样性控制不足。

**核心方法**：作者将离散扩散解码抽象为可并行生成候选、再用可插拔目标做beam选择的通用框架；在多样性场景下，用确定性点过程（DPP）的MAP推断来选择候选，并用可扩展的贪心算法实现，支持多GPU并能调节“模型概率-多样性”的权衡。

**主要结论**：在自由文本生成与问答任务上，D5P4相较强基线显著提升生成多样性，同时保持具有竞争力的生成质量，并且计算开销几乎不增加。

**关键词**：离散扩散模型, 扩散解码, 广义束搜索, 批内多样性, 确定性点过程（DPP）, 贪心求解器, 文本生成, 问答生成

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

**一句话总结**：F2LLM-v2 是一组覆盖200+语言、从80M到14B的通用多语种向量嵌入模型，在保持强性能的同时显著提升训练与推理效率。

**研究动机**：现有LLM式嵌入模型在多语种（尤其是中低资源语言）上覆盖不足且成本较高，难以在资源受限场景落地。作者希望在更广语言覆盖下实现更高性价比的嵌入模型，并推动开源研究。

**核心方法**：构建6000万高质量公开样本的数据集，并采用两阶段的LLM嵌入训练流程；结合matryoshka learning、模型剪枝与知识蒸馏，在多个规模上同时优化效果与效率。

**主要结论**：F2LLM-v2-14B在11个MTEB基准上排名第一，小模型也在资源受限应用中达到新的SOTA，且作者开源模型、数据、代码与中间checkpoint以促进复现与研究。

**关键词**：多语言向量嵌入, 两阶段训练, LLM嵌入训练, 模型剪枝, 知识蒸馏, 高效推理, 开源模型发布, F2LLM-v2

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19223v1) | [下载PDF](https://arxiv.org/pdf/2603.19223v1.pdf)

---

## [6. Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation](https://arxiv.org/abs/2603.19220v1)

**作者**：Zhuolin Yang, Zihan Liu, Yang Chen 等 17 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

We introduce Nemotron-Cascade 2, an open 30B MoE model with 3B activated parameters that delivers best-in-class reasoning and strong agentic capabilities. Despite its compact size, its mathematical and coding reasoning performance approaches that of frontier open models. It is the second open-weight LLM, after DeepSeekV3.2-Speciale-671B-A37B, to achieve Gold Medal-level performance in the 2025 International Mathematical Olympiad (IMO), the International Olympiad in Informatics (IOI), and the ICPC World Finals, demonstrating remarkably high intelligence density with 20x fewer parameters. In contrast to Nemotron-Cascade 1, the key technical advancements are as follows. After SFT on a meticulously curated dataset, we substantially expand Cascade RL to cover a much broader spectrum of reasoning and agentic domains. Furthermore, we introduce multi-domain on-policy distillation from the strongest intermediate teacher models for each domain throughout the Cascade RL process, allowing us to efficiently recover benchmark regressions and sustain strong performance gains along the way. We release the collection of model checkpoint and training data.

### 🤖 AI 总结

**一句话总结**：提出Nemotron-Cascade 2：一个30B MoE（仅激活3B参数）的开源大模型，通过扩展Cascade RL与多领域在线蒸馏，在推理与Agent能力上实现接近前沿开源模型的高智能密度表现。

**研究动机**：在参数规模受限（更高性价比）的前提下，追求跨数学、编程与多种Agent任务的强推理能力，同时解决后训练过程中不同基准/领域易出现的性能回退问题。

**核心方法**：先在高质量精挑SFT数据上对齐基础能力，然后将Cascade RL扩展到更广的推理与Agent领域；在RL过程中引入“多领域on-policy蒸馏”，针对每个领域使用最强的中间教师模型进行在线蒸馏，以更高效地恢复回退并维持增益。

**主要结论**：该模型以20×更少参数达到IMO/IOI/ICPC金牌级表现，并在数学与代码推理上逼近前沿开源模型；多领域Cascade RL结合在线蒸馏能在提升能力的同时更稳定地避免训练过程中的基准回退，作者同步开放权重检查点与训练数据。

**关键词**：混合专家模型（MoE）, 大语言模型后训练, 监督微调（SFT）, 多域蒸馏, 推理能力, 数学推理, 代码推理, 智能体能力（Agent）, 开源权重模型

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19220v1) | [下载PDF](https://arxiv.org/pdf/2603.19220v1.pdf)

---

## [7. UGID: Unified Graph Isomorphism for Debiasing Large Language Models](https://arxiv.org/abs/2603.19144v1)

**作者**：Zikang Ding, Junchi Yao, Junhao Li 等 7 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-03-19

### 📄 论文摘要

Large language models (LLMs) exhibit pronounced social biases. Output-level or data-optimization--based debiasing methods cannot fully resolve these biases, and many prior works have shown that biases are embedded in internal representations. We propose \underline{U}nified \underline{G}raph \underline{I}somorphism for \underline{D}ebiasing large language models (\textit{\textbf{UGID}}), an internal-representation--level debiasing framework for large language models that models the Transformer as a structured computational graph, where attention mechanisms define the routing edges of the graph and hidden states define the graph nodes. Specifically, debiasing is formulated as enforcing invariance of the graph structure across counterfactual inputs, with differences allowed only on sensitive attributes. \textit{\textbf{UGID}} jointly constrains attention routing and hidden representations in bias-sensitive regions, effectively preventing bias migration across architectural components. To achieve effective behavioral alignment without degrading general capabilities, we introduce a log-space constraint on sensitive logits and a selective anchor-based objective to preserve definitional semantics. Extensive experiments on large language models demonstrate that \textit{\textbf{UGID}} effectively reduces bias under both in-distribution and out-of-distribution settings, significantly reduces internal structural discrepancies, and preserves model safety and utility.

### 🤖 AI 总结

**一句话总结**：UGID 将 Transformer 视为由注意力路由与隐状态构成的计算图，通过约束反事实输入下图结构与表征的一致性来在内部表示层面减少 LLM 社会偏见，并尽量保持能力与安全性。

**研究动机**：现有输出层或数据优化式去偏方法难以根除偏见，因为偏见往往内嵌于模型内部表示并会在组件间“迁移”。因此需要一种能同时约束注意力与隐藏表征、从结构层面抑制偏见传播的内部去偏框架。

**核心方法**：UGID 将注意力机制视为图的路由边、隐藏状态视为节点，把去偏表述为：对反事实输入对齐计算图结构，仅允许在敏感属性相关部分存在差异，并在偏见敏感区域联合约束注意力与表示以防迁移。为减少能力退化，它引入对敏感 logits 的对数空间约束以及选择性锚点目标以保留“定义性语义”。

**主要结论**：实验显示 UGID 在分布内与分布外场景均能显著降低偏见，并减少内部结构差异（表明表征/路由更一致）。同时方法在不明显牺牲通用效用的前提下维持模型安全与实用性。

**关键词**：内部表征对齐, 注意力路由约束, 图同构不变性, 反事实不变性学习, 敏感属性隔离, 锚点语义保持, 偏见迁移抑制, 分布外鲁棒性

**评分**：28

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

**一句话总结**：提出 Matryoshka Gaussian Splatting（MGS），通过一次训练得到“可按预算连续缩放”的高斯序列，使得渲染任意前缀都能平滑提升画质且不牺牲满容量性能。

**研究动机**：3D Gaussian Splatting 在实际部署中需要可调细节层次（LoD），但离散LoD只能提供少量档位；现有连续LoD往往在满预算时质量下降，使LoD成为高成本取舍。

**核心方法**：MGS学习一个“有序”的高斯集合：渲染前k个高斯（任意前缀）即可得到一致重建，k越大质量越高；训练时采用随机预算训练（stochastic budget training），每次迭代随机采样预算并同时优化对应前缀与全量集合，仅需两次前向传播且不改网络结构。

**主要结论**：在四个基准与六个基线对比中，MGS保持与原3DGS骨干相当的满容量效果，同时从单模型提供连续的速度-质量折中；消融实验表明其排序策略、目标设计与容量设置能稳定支撑该连续LoD特性。

**关键词**：神经渲染, 层次细节（LoD）, 随机预算训练, 高斯排序, 前缀渲染, 速度-质量权衡, 单模型多精度渲染, 3D 场景重建

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19234v1) | [下载PDF](https://arxiv.org/pdf/2603.19234v1.pdf)

---

## [9. MonoArt: Progressive Structural Reasoning for Monocular Articulated 3D Reconstruction](https://arxiv.org/abs/2603.19231v1)

**作者**：Haitian Li, Haozhe Xie, Junxiang Xu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

Reconstructing articulated 3D objects from a single image requires jointly inferring object geometry, part structure, and motion parameters from limited visual evidence. A key difficulty lies in the entanglement between motion cues and object structure, which makes direct articulation regression unstable. Existing methods address this challenge through multi-view supervision, retrieval-based assembly, or auxiliary video generation, often sacrificing scalability or efficiency. We present MonoArt, a unified framework grounded in progressive structural reasoning. Rather than predicting articulation directly from image features, MonoArt progressively transforms visual observations into canonical geometry, structured part representations, and motion-aware embeddings within a single architecture. This structured reasoning process enables stable and interpretable articulation inference without external motion templates or multi-stage pipelines. Extensive experiments on PartNet-Mobility demonstrate that OM achieves state-of-the-art performance in both reconstruction accuracy and inference speed. The framework further generalizes to robotic manipulation and articulated scene reconstruction.

### 🤖 AI 总结

**一句话总结**：MonoArt提出一种渐进式结构推理框架，从单张图像稳定地重建可动关节物体的3D几何、部件结构与运动参数，并在精度与速度上达到SOTA。

**研究动机**：单目可动3D重建需要同时推断几何、部件与运动，但运动线索与结构强耦合导致直接回归关节参数不稳定；现有方案常依赖多视角监督、检索装配或视频辅助，牺牲可扩展性或效率。

**核心方法**：MonoArt不直接从图像特征回归关节参数，而是在单一架构内逐步将视觉观测转换为规范化几何、结构化部件表示以及运动感知嵌入，从而以可解释的结构推理方式进行关节/运动推断。

**主要结论**：在PartNet-Mobility上，MonoArt在重建准确率与推理速度上优于现有方法，且无需外部运动模板或多阶段流水线；同时具备向机器人操作与可动场景重建任务泛化的能力。

**关键词**：单目关节物体三维重建, 单图像三维重建, 关节参数估计, 结构化部件表示, 逐步结构推理, 规范形几何, 运动结构解耦, 运动感知嵌入, 机器人操作, 关节场景重建

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19231v1) | [下载PDF](https://arxiv.org/pdf/2603.19231v1.pdf)

---

## [10. Under One Sun: Multi-Object Generative Perception of Materials and Illumination](https://arxiv.org/abs/2603.19226v1)

**作者**：Nobuo Yoshii, Xinran Nicole Han, Ryo Kawahara 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

We introduce Multi-Object Generative Perception (MultiGP), a generative inverse rendering method for stochastic sampling of all radiometric constituents -- reflectance, texture, and illumination -- underlying object appearance from a single image. Our key idea to solve this inherently ambiguous radiometric disentanglement is to leverage the fact that while their texture and reflectance may differ, objects in the same scene are all lit by the same illumination. MultiGP exploits this consensus to produce samples of reflectance, texture, and illumination from a single image of known shapes based on four key technical contributions: a cascaded end-to-end architecture that combines image-space and angular-space disentanglement; Coordinated Guidance for diffusion convergence to a single consistent illumination estimate; Axial Attention applied to facilitate ``cross-talk'' between objects of different reflectance; and a Texture Extraction ControlNet to preserve high-frequency texture details while ensuring decoupling from estimated lighting. Experimental results demonstrate that MultiGP effectively leverages the complementary spatial and frequency characteristics of multiple object appearances to recover individual texture and reflectance as well as the common illumination.

### 🤖 AI 总结

**一句话总结**：MultiGP利用同一场景多物体共享光照的约束，从单张已知几何的图像中生成式采样分解出各物体的反射率/纹理以及一致的场景光照。

**研究动机**：单图逆向渲染中反射率、纹理与光照高度耦合且解不唯一，导致辐射成分难以可靠解耦。作者观察到同一场景内多个物体虽材质不同但共享同一光照，可用跨物体“共识”降低歧义。

**核心方法**：提出级联端到端架构，结合图像空间与角度空间的解耦，并用扩散模型进行随机采样；通过Coordinated Guidance促使扩散收敛到单一一致的光照估计，配合Axial Attention实现不同物体间信息“串联”，再用Texture Extraction ControlNet保留高频纹理并与光照估计解耦。

**主要结论**：实验表明MultiGP能有效融合多物体外观的互补空间/频率信息，在单图条件下更好地恢复每个物体的纹理与反射率，并同时估计一致的公共光照，相比基线在解耦质量与细节保真度上更优。

**关键词**：逆向渲染, 辐射成分解耦, 单图像材质估计, 光照估计, 多物体一致性约束, 扩散模型推断, 引导扩散收敛, 轴向注意力, 纹理-光照解耦, 已知几何条件

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

**一句话总结**：EffectErase 通过引入大规模成对数据集 VOR，并用“插入-移除”互逆学习，让模型不仅能移除目标物体，还能更彻底地抹除阴影、反射等视觉效应并恢复连贯背景。

**研究动机**：现有扩散式视频修复/移除方法往往只能抠掉物体本体，却难以清除形变、阴影、反射等残留效应并保持时序一致；同时缺少系统覆盖常见效应与复杂场景的成对数据集，限制了训练与评测。

**核心方法**：作者构建 VOR 数据集（6万对视频、含物体出现/消失及对应mask，覆盖5类效应、真实+合成、多类别与多物体动态场景），并提出 EffectErase：将视频“物体插入”作为“物体移除”的互逆辅助任务进行互惠学习。模型采用任务感知区域引导聚焦受影响区域，并用插入-移除一致性目标约束两任务在效应区域定位与结构线索上互补且一致，从而实现灵活任务切换与更强的效应抹除能力。

**主要结论**：在 VOR 上训练后，EffectErase 在多项实验中优于现有方法，能在多样场景下更干净地去除目标物体及其阴影/反射等效应，并生成更时序一致、结构更自然的背景结果。

**关键词**：视频对象移除, 视频修复, 扩散模型视频修复, 视觉效果擦除, 阴影反射去除, 变形伪影消除, 互惠学习, 插入-移除一致性约束, 区域引导注意, 成对视频数据集

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19224v1) | [下载PDF](https://arxiv.org/pdf/2603.19224v1.pdf)

---

## [12. Spectrally-Guided Diffusion Noise Schedules](https://arxiv.org/abs/2603.19222v1)

**作者**：Carlos Esteves, Ameesh Makadia  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Denoising diffusion models are widely used for high-quality image and video generation. Their performance depends on noise schedules, which define the distribution of noise levels applied during training and the sequence of noise levels traversed during sampling. Noise schedules are typically handcrafted and require manual tuning across different resolutions. In this work, we propose a principled way to design per-instance noise schedules for pixel diffusion, based on the image's spectral properties. By deriving theoretical bounds on the efficacy of minimum and maximum noise levels, we design ``tight'' noise schedules that eliminate redundant steps. During inference, we propose to conditionally sample such noise schedules. Experiments show that our noise schedules improve generative quality of single-stage pixel diffusion models, particularly in the low-step regime.

### 🤖 AI 总结

**一句话总结**：提出一种由图像频谱特性指导的按样本自适应扩散噪声日程设计方法，通过“紧致”噪声区间与推理时条件采样减少冗余步并提升低步数生成质量。

**研究动机**：现有扩散模型噪声日程多为手工设定且需跨分辨率反复调参，训练/采样中常包含对特定样本无效或冗余的噪声阶段，导致效率与质量受限，尤其在少步采样时更明显。

**核心方法**：基于图像频谱性质推导最小/最大噪声水平对去噪有效性的理论界限，并据此为每个实例构造覆盖有效区间的“tight”噪声日程以裁剪冗余步骤；推理阶段进一步对这些日程进行条件采样以适配不同输入/目标生成难度。

**主要结论**：该频谱引导的自适应噪声日程在单阶段像素扩散模型上带来更好的生成质量提升，优势在低采样步数设置下尤为显著，同时减少了对手工噪声日程调参的依赖。

**关键词**：Diffusion, 去噪扩散, 噪声调度, 自适应噪声调度, 频谱引导, 图像频谱特性, 像素扩散, 条件采样, 低步数采样, 单阶段生成

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19222v1) | [下载PDF](https://arxiv.org/pdf/2603.19222v1.pdf)

---

## [13. Rethinking Vector Field Learning for Generative Segmentation](https://arxiv.org/abs/2603.19218v1)

**作者**：Chaoyang Wang, Yaobo Liang, Boci Peng 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

Taming diffusion models for generative segmentation has attracted increasing attention. While existing approaches primarily focus on architectural tweaks or training heuristics, there remains a limited understanding of the intrinsic mismatch between continuous flow matching objectives and discrete perception tasks. In this work, we revisit diffusion segmentation from the perspective of vector field learning. We identify two key limitations of the commonly used flow matching objective: gradient vanishing and trajectory traversing, which result in slow convergence and poor class separation. To tackle these issues, we propose a principled vector field reshaping strategy that augments the learned velocity field with a detached distance-aware correction term. This correction introduces both attractive and repulsive interactions, enhancing gradient magnitudes near centroids while preserving the original diffusion training framework. Furthermore, we design a computationally efficient, quasi-random category encoding scheme inspired by Kronecker sequences, which integrates seamlessly with an end-to-end pixel neural field framework for pixel-level semantic alignment. Extensive experiments consistently demonstrate significant improvements over vanilla flow matching approaches, substantially narrowing the performance gap between generative segmentation and strong discriminative specialists.

### 🤖 AI 总结

**一句话总结**：论文从向量场学习角度重审扩散式生成分割，提出“向量场重塑+高效类别编码”以缓解流匹配在离散分割任务中的优化与分离问题，从而显著提升性能。

**研究动机**：现有扩散分割多依赖结构或训练技巧改动，但对连续流匹配目标与离散语义分割之间的内在不匹配缺乏理解，导致收敛慢、类别分离差。作者指出常用流匹配存在梯度消失与轨迹穿越两类关键症结，需要更原则性的向量场层面修正。

**核心方法**：提出向量场重塑策略：在学习到的速度场上叠加一个“分离式(detached)的距离感知校正项”，同时引入吸引/排斥交互以增强质心附近梯度并改善类别间分隔，同时保持原扩散训练框架不变。另设计基于Kronecker序列的准随机类别编码，以较低计算代价融入端到端像素神经场，实现像素级语义对齐。

**主要结论**：实验证明该方法相较原始流匹配扩散分割在多个设置下稳定提升，显著加快/改善优化并增强类别可分性。整体上大幅缩小生成式分割与强判别式分割模型之间的性能差距。

**关键词**：生成式语义分割, Diffusion, 距离感知校正, 梯度消失, 轨迹穿越, 准随机类别编码, 像素神经场, Rethinking

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19218v1) | [下载PDF](https://arxiv.org/pdf/2603.19218v1.pdf)

---

## [14. LVOmniBench: Pioneering Long Audio-Video Understanding Evaluation for Omnimodal LLMs](https://arxiv.org/abs/2603.19217v1)

**作者**：Keda Tao, Yuhua Zheng, Jia Xu 等 16 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

Recent advancements in omnimodal large language models (OmniLLMs) have significantly improved the comprehension of audio and video inputs. However, current evaluations primarily focus on short audio and video clips ranging from 10 seconds to 5 minutes, failing to reflect the demands of real-world applications, where videos typically run for tens of minutes. To address this critical gap, we introduce LVOmniBench, a new benchmark designed specifically for the cross-modal comprehension of long-form audio and video. This dataset comprises high-quality videos sourced from open platforms that feature rich audio-visual dynamics. Through rigorous manual selection and annotation, LVOmniBench comprises 275 videos, ranging in duration from 10 to 90 minutes, and 1,014 question-answer (QA) pairs. LVOmniBench aims to rigorously evaluate the capabilities of OmniLLMs across domains, including long-term memory, temporal localization, fine-grained understanding, and multimodal perception. Our extensive evaluation reveals that current OmniLLMs encounter significant challenges when processing extended audio-visual inputs. Open-source models generally achieve accuracies below 35%, whereas the Gemini 3 Pro reaches a peak accuracy of approximately 65%. We anticipate that this dataset, along with our empirical findings, will stimulate further research and the development of advanced models capable of resolving complex cross-modal understanding problems within long-form audio-visual contexts.

### 🤖 AI 总结

**一句话总结**：LVOmniBench提出首个面向“长时段（10–90分钟）音视频”理解的评测基准，用于系统检验OmniLLM在真实长视频场景下的跨模态理解能力与瓶颈。

**研究动机**：现有多模态/全模态模型评测多集中在10秒到5分钟短片段，无法覆盖真实应用中常见的几十分钟长视频带来的长程记忆、时间定位与细粒度理解需求。

**核心方法**：构建并人工筛选标注LVOmniBench：包含275个来自开放平台的高质量长视频（10–90分钟）与1,014组QA；围绕长程记忆、时间定位、细粒度理解与多模态感知等能力维度，对多种OmniLLM进行统一评测对比。

**主要结论**：实验显示当前OmniLLM在长音视频理解上仍显著困难：开源模型准确率普遍低于35%，Gemini 3 Pro最高约65%；该基准与结果揭示了长时跨模态理解的关键短板，并为后续模型改进提供方向。

**关键词**：多模态基准数据集, 长时序建模, 长程记忆, 时间定位, 多模态问答, 音视频联合感知, 人工标注QA, LVOmniBench

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19217v1) | [下载PDF](https://arxiv.org/pdf/2603.19217v1.pdf)

---

## [15. DreamPartGen: Semantically Grounded Part-Level 3D Generation via Collaborative Latent Denoising](https://arxiv.org/abs/2603.19216v1)

**作者**：Tianjiao Yu, Xinzhuo Li, Muntasir Wahed 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Understanding and generating 3D objects as compositions of meaningful parts is fundamental to human perception and reasoning. However, most text-to-3D methods overlook the semantic and functional structure of parts. While recent part-aware approaches introduce decomposition, they remain largely geometry-focused, lacking semantic grounding and failing to model how parts align with textual descriptions or their inter-part relations. We propose DreamPartGen, a framework for semantically grounded, part-aware text-to-3D generation. DreamPartGen introduces Duplex Part Latents (DPLs) that jointly model each part's geometry and appearance, and Relational Semantic Latents (RSLs) that capture inter-part dependencies derived from language. A synchronized co-denoising process enforces mutual geometric and semantic consistency, enabling coherent, interpretable, and text-aligned 3D synthesis. Across multiple benchmarks, DreamPartGen delivers state-of-the-art performance in geometric fidelity and text-shape alignment.

### 🤖 AI 总结

**一句话总结**：DreamPartGen通过语言驱动的部件语义建模与协同去噪，实现语义可解释、部件一致且文本对齐的3D生成。

**研究动机**：现有text-to-3D大多忽略“有意义的部件”这一语义与功能结构，即便引入部件分解也偏几何层面，难以让部件与文本描述及部件间关系对齐。为提升可解释性与一致性，需要把语言中的部件语义和部件依赖显式融入生成过程。

**核心方法**：提出双工部件潜变量DPLs，将每个部件的几何与外观联合表示；提出关系语义潜变量RSLs，从语言中抽取部件间依赖并在潜空间建模。通过同步协同去噪（co-denoising）让部件几何与语义关系相互约束，从而生成整体连贯、部件可控且文本一致的3D对象。

**主要结论**：在多个基准上，DreamPartGen在几何保真度与文本-形状对齐方面达到SOTA，同时生成结果更具部件级可解释性与跨部件一致性。该框架验证了“语义关系+部件潜变量+协同去噪”能显著改善部件感知的3D合成质量。

**关键词**：文本到3D生成, 部件级3D生成, 语义部件分解, 几何-外观联合表示, 潜变量建模, 语言驱动关系建模, 部件间依赖建模, 协同去噪, 扩散模型去噪, 文本-形状对齐, 几何保真度评测

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19216v1) | [下载PDF](https://arxiv.org/pdf/2603.19216v1.pdf)

---

## [16. Do VLMs Need Vision Transformers? Evaluating State Space Models as Vision Encoders](https://arxiv.org/abs/2603.19209v1)

**作者**：Shang-Jui Ray Kuo, Paola Cascante-Bonilla  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Large vision--language models (VLMs) often use a frozen vision backbone, whose image features are mapped into a large language model through a lightweight connector. While transformer-based encoders are the standard visual backbone, we ask whether state space model (SSM) vision backbones can be a strong alternative. We systematically evaluate SSM vision backbones for VLMs in a controlled setting. Under matched ImageNet-1K initialization, the SSM backbone achieves the strongest overall performance across both VQA and grounding/localization. We further adapt both SSM and ViT-family backbones with detection or segmentation training and find that dense-task tuning generally improves performance across families; after this adaptation, the SSM backbone remains competitive while operating at a substantially smaller model scale. We further observe that (i) higher ImageNet accuracy or larger backbones do not reliably translate into better VLM performance, and (ii) some visual backbones are unstable in localization. Based on these findings, we propose stabilization strategies that improve robustness for both backbone families and highlight SSM backbones as a strong alternative to transformer-based vision encoders in VLMs.

### 🤖 AI 总结

**一句话总结**：在VLM的冻结视觉骨干设定下，SSM视觉编码器在VQA与定位/grounding上整体表现不输甚至优于ViT，并且可在更小模型规模下保持竞争力。

**研究动机**：现有VLM几乎默认采用ViT类视觉骨干，但其是否“必要”缺乏系统对照；作者希望验证SSM视觉骨干能否作为更高效且同样强的替代方案。

**核心方法**：在受控实验中，对SSM与ViT家族视觉骨干进行匹配的ImageNet-1K初始化与统一的VLM连接器/训练配置评测，并进一步对骨干进行检测/分割等密集任务适配以比较对VQA与定位性能的影响，同时提出针对定位不稳定的鲁棒化/稳定化策略。

**主要结论**：匹配初始化下SSM骨干在VQA与定位任务上取得最强总体表现；密集任务调优普遍提升两类骨干的VLM效果，且SSM在显著更小规模下仍具竞争力；此外ImageNet精度或更大骨干并不可靠预测VLM性能，一些骨干在定位上会不稳定，所提稳定化策略可提升两类骨干的鲁棒性。

**关键词**：视觉语言模型（VLM）, 视觉编码器, 视觉主干网络, 状态空间模型（SSM）, 冻结视觉主干, 轻量连接器, 检测/分割微调, 鲁棒性稳定化策略, 模型规模效率

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

**一句话总结**：提出Splat2BEV：先用3D Gaussian Splatting做显式三维重建预训练，再将几何对齐的特征投影到BEV以提升多种自动驾驶BEV任务性能。

**研究动机**：现有BEV方法多为端到端黑盒特征变换，仅靠下游任务监督，缺乏明确3D几何建模与可解释性，导致几何不准、性能受限。作者认为显式3D表示与重建能为BEV提供更可靠的几何对齐表征。

**核心方法**：预训练一个Gaussian生成器，从多视角图像显式重建3D场景并产出几何对齐的特征表示；再将该3D表示/特征投影到BEV空间，作为下游任务（如分割、检测等）的输入进行训练与推理。

**主要结论**：在nuScenes与Argoverse上取得SOTA或显著提升，实验验证将显式3D重建（Gaussian Splatting）引入BEV学习可同时增强语义表达与几何精度，从而提升整体BEV感知效果。

**关键词**：自动驾驶感知, 多视角图像融合, 3D场景重建, 显式3D表示, 3D高斯溅射, 几何对齐表示, BEV特征学习, 语义分割, 3D目标检测

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

**一句话总结**：ARIADNE 通过“拓扑偏好对齐的感知 + 强化学习推理”的两阶段框架，实现冠脉造影中拓扑连通的血管结构分割与更可靠的狭窄定位。

**研究动机**：传统像素级损失虽能提升分割重叠率，但难以约束血管树的拓扑连通性，导致断裂/碎片化并引发下游狭窄检测误报。临床上还存在分叉与交叉等模糊解剖点，需在覆盖率与可信度之间做更安全的权衡。

**核心方法**：感知模块用DPO对视觉语言基础模型Sa2VA进行偏好微调，将Betti数等拓扑约束作为偏好信号，鼓励生成几何完整、拓扑一致的血管结构。推理模块将狭窄定位建模为带显式拒绝机制的MDP，通过RL在遇到分叉/交叉等不确定候选时主动弃权，从“尽量找全”转为“更可靠地报告”。

**主要结论**：在1,400张临床造影上取得SOTA中心线Dice 0.838，并较几何基线降低41%假阳性；在多中心ARCADE与XCAD外部验证中显示良好泛化。论文还展示了DPO在医学影像中用于拓扑偏好对齐的可行性，可在保持敏感性的同时减少拓扑违例并提升诊断可信度。

**关键词**：冠状动脉造影, 冠状血管分割, 血管拓扑约束, 拓扑一致性, 贝蒂数, 直接偏好优化DPO, 偏好对齐学习, 视觉语言基础模型, 强化学习推理, 马尔可夫决策过程, 拒绝机制, 狭窄定位

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19169v1) | [下载PDF](https://arxiv.org/pdf/2603.19169v1.pdf)

---

## [19. Adaptive Auxiliary Prompt Blending for Target-Faithful Diffusion Generation](https://arxiv.org/abs/2603.19158v1)

**作者**：Kwanyoung Lee, SeungJu Cha, Yebin Ahn 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

Diffusion-based text-to-image (T2I) models have made remarkable progress in generating photorealistic and semantically rich images. However, when the target concepts lie in low-density regions of the training distribution, these models often produce semantically misaligned or structurally inconsistent results. This limitation arises from the long-tailed nature of text-image datasets, where rare concepts or editing instructions are underrepresented. To address this, we introduce Adaptive Auxiliary Prompt Blending (AAPB) - a unified framework that stabilizes the diffusion process in low-density regions. AAPB leverages auxiliary anchor prompts to provide semantic support in rare concept generation and structural support in image editing, ensuring faithful guidance toward the target prompt. Unlike prior heuristic prompt alternation methods, AAPB derives a closed-form adaptive coefficient that optimally balances the influence between the auxiliary anchor and the target prompt at each diffusion step. Grounded in Tweedie's identity, our formulation provides a principled and training-free framework for adaptive prompt blending, ensuring stable and target-faithful generation. We demonstrate the effectiveness of adaptive interpolation over fixed interpolation through controlled experiments and empirically show consistent improvements on the RareBench and FlowEdit datasets, achieving superior semantic accuracy and structural fidelity compared to prior training-free baselines.

### 🤖 AI 总结

**一句话总结**：提出一种训练-free 的自适应辅助提示融合框架AAPB，通过逐步调节辅助锚点提示与目标提示的权重，提升扩散模型在稀有概念生成与编辑任务中的目标一致性与结构稳定性。

**研究动机**：长尾文本-图像数据导致扩散T2I在训练分布低密度区域（稀有概念/罕见编辑指令）容易语义跑偏或结构不一致；现有基于启发式的提示交替/插值缺乏原理支撑且难以稳定。

**核心方法**：AAPB引入“辅助锚点提示”作为语义/结构支撑，并基于Tweedie恒等式推导每个扩散步的闭式自适应系数，在不训练的情况下最优平衡锚点与目标提示对去噪引导的影响。

**主要结论**：与固定插值相比，自适应插值在受控实验中更稳定；在RareBench与FlowEdit上相较先前训练-free 基线取得更高语义准确率与更好结构保真度，证明其在低密度区域能更忠实地对齐目标提示。

**关键词**：Diffusion, 文生图生成, 图像编辑, 长尾分布, 稀有概念生成, 低密度区域, 自适应提示词融合, 辅助锚点提示词, 无训练方法, 闭式解系数, 语义对齐, 结构保真度

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19158v1) | [下载PDF](https://arxiv.org/pdf/2603.19158v1.pdf)

---

## [20. ADAPT: Attention Driven Adaptive Prompt Scheduling and InTerpolating Orthogonal Complements for Rare Concepts Generation](https://arxiv.org/abs/2603.19157v1)

**作者**：Kwanyoung Lee, Hyunwoo Oh, SeungJu Cha 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-19

### 📄 论文摘要

Generating rare compositional concepts in text-to-image synthesis remains a challenge for diffusion models, particularly for attributes that are uncommon in the training data. While recent approaches, such as R2F, address this challenge by utilizing LLM for prompt scheduling, they suffer from inherent variance due to the randomness of language models and suboptimal guidance from iterative text embedding switching. To address these problems, we propose the ADAPT framework, a training-free framework that deterministically plans and semantically aligns prompt schedules, providing consistent guidance to enhance the composition of rare concepts. By leveraging attention scores and orthogonal components, ADAPT significantly enhances compositional generation of rare concepts in the RareBench benchmark without additional training or fine-tuning. Through comprehensive experiments, we demonstrate that ADAPT achieves superior performance in RareBench and accurately reflects the semantic information of rare attributes, providing deterministic and precise control over the generation of rare compositions without compromising visual integrity.

### 🤖 AI 总结

**一句话总结**：ADAPT 提出一种无需训练的确定性提示词调度与正交补偿插值框架，显著提升扩散模型对稀有组合概念（罕见属性）的可控生成能力。

**研究动机**：扩散模型在训练数据中出现频率低的属性/组合概念上易生成失败；现有用 LLM 做提示调度的方法（如 R2F）因语言模型随机性与迭代切换文本嵌入带来的引导不稳定而效果受限。

**核心方法**：ADAPT 基于注意力分数来确定性地规划并语义对齐 prompt schedule，以减少随机波动并让引导更聚焦；同时利用文本/条件表征中的正交分量（orthogonal complements）进行插值补偿，从而在不改动模型权重的情况下增强稀有属性的组合表达。

**主要结论**：在 RareBench 上，ADAPT 在无需额外训练或微调的前提下优于对比方法，能更准确地体现稀有属性的语义并提供更确定、精细的控制，同时不明显牺牲生成图像的整体视觉质量。

**关键词**：文生图扩散模型, 稀有概念生成, 组合概念合成, 提示词调度, 确定性提示规划, 注意力引导, 正交补插值, 文本嵌入切换, 语义对齐, 免训练控制

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19157v1) | [下载PDF](https://arxiv.org/pdf/2603.19157v1.pdf)

---

## [21. GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning](https://arxiv.org/abs/2603.19137v1)

**作者**：Yiren Lu, Yi Du, Disheng Liu 等 6 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-03-19

### 📄 论文摘要

Effective embodied exploration requires agents to accumulate and retain spatial knowledge over time. However, existing scene representations, such as discrete scene graphs or static view-based snapshots, lack \textit{post-hoc re-observability}. If an initial observation misses a target, the resulting memory omission is often irrecoverable. To bridge this gap, we propose \textbf{GSMem}, a zero-shot embodied exploration and reasoning framework built upon 3D Gaussian Splatting (3DGS). By explicitly parameterizing continuous geometry and dense appearance, 3DGS serves as a persistent spatial memory that endows the agent with \textit{Spatial Recollection}: the ability to render photorealistic novel views from optimal, previously unoccupied viewpoints. To operationalize this, GSMem employs a retrieval mechanism that simultaneously leverages parallel object-level scene graphs and semantic-level language fields. This complementary design robustly localizes target regions, enabling the agent to ``hallucinate'' optimal views for high-fidelity Vision-Language Model (VLM) reasoning. Furthermore, we introduce a hybrid exploration strategy that combines VLM-driven semantic scoring with a 3DGS-based coverage objective, balancing task-aware exploration with geometric coverage. Extensive experiments on embodied question answering and lifelong navigation demonstrate the robustness and effectiveness of our framework

### 🤖 AI 总结

**一句话总结**：GSMem 用3D Gaussian Splatting构建可持续的空间记忆，使具身智能体能在零样本条件下“回忆/渲染”最佳新视角以提升探索与推理能力。

**研究动机**：现有记忆表示（场景图、静态视图快照等）缺乏事后可再观测性：初次观察遗漏目标后往往无法补救，导致长期探索与问答/导航性能受限。

**核心方法**：以3DGS显式参数化连续几何与稠密外观作为持久空间记忆，并通过“对象级场景图+语义级语言场”联合检索定位目标区域，从而渲染未到达过的最优视角供VLM高保真推理；同时提出混合探索策略，将VLM语义评分与3DGS覆盖度目标结合，实现任务相关探索与几何覆盖的平衡。

**主要结论**：在具身问答与终身导航等实验中，GSMem表现出更强的鲁棒性与效果，证明基于3DGS的可再渲染空间记忆与语义-几何联合探索能显著提升零样本具身探索与推理。

**关键词**：具身探索, 持久空间记忆, 零样本导航, 新视角渲染, 场景图检索, 语言场语义场, 视觉语言模型推理, 语义引导探索, 几何覆盖优化, 具身问答, 终身导航

**评分**：43

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

**一句话总结**：论文指出钓鱼检测的对抗鲁棒性主要由“特征可被低成本篡改的经济学”决定，而非模型复杂度；在预算约束的特征编辑攻击下，多种高AUC模型的鲁棒性会趋同且攻击面高度集中。

**研究动机**：现有钓鱼检测器在i.i.d.静态评测下几乎满分，但真实部署中攻击者可在上线后以有限成本操纵网站特征从而规避检测，因此需要用显式成本/预算刻画并评估鲁棒性差距。

**核心方法**：提出成本感知逃逸框架，建模离散且单调的特征编辑与攻击者预算，并给出三项诊断指标：最小逃逸成本（MEC）、预算下的逃逸存活率S(B)、以及鲁棒性集中指数（RCI）来量化攻击面是否集中在少数低成本特征转移上。

**主要结论**：在UCI钓鱼数据集上，尽管LR/RF/GBT/XGBoost静态AUC均≥0.979，但在预算化“净化式”逃逸下中位MEC≈2且成功逃逸80%+集中于3个低成本特征；仅当特征裁剪能移除所有主导的低成本转移时才提升鲁棒性，并形式化证明：若存在一定比例样本可通过单一最小成本转移规避，则任何分类器都无法将相应MEC分位数提高到c_min之上，除非改变特征表示或成本模型。

**关键词**：钓鱼网站检测, 预算约束规避攻击, 成本感知规避框架, 离散单调特征编辑, 最小规避成本（MEC）, 规避生存率 S(B, 鲁棒性集中指数（RCI）, 攻击面集中, 特征经济学, 特征表示与成本模型

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19204v1) | [下载PDF](https://arxiv.org/pdf/2603.19204v1.pdf)

---

## [23. Improving RCT-Based Treatment Effect Estimation Under Covariate Mismatch via Calibrated Alignment](https://arxiv.org/abs/2603.19186v1)

**作者**：Amir Asiaee, Samhita Pal  
**分类**：cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Randomized controlled trials (RCTs) are the gold standard for estimating heterogeneous treatment effects, yet they are often underpowered for detecting effect heterogeneity. Large observational studies (OS) can supplement RCTs for conditional average treatment effect (CATE) estimation, but a key barrier is covariate mismatch: the two sources measure different, only partially overlapping, covariates. We propose CALM (Calibrated ALignment under covariate Mismatch), which bypasses imputation by learning embeddings that map each source's features into a common representation space. OS outcome models are transferred to the RCT embedding space and calibrated using trial data, preserving causal identification from randomization. Finite-sample risk bounds decompose into alignment error, outcome-model complexity, and calibration complexity terms, identifying when embedding alignment outperforms imputation. Under the calibration-based linear variant, the framework provides protection against negative transfer; the neural variant can be vulnerable under severe distributional shift. Under sparse linear models, the embedding approach strictly generalizes imputation. Simulations across 51 settings confirm that (i) calibration-based methods are equivalent for linear CATEs, and (ii) the neural embedding variant wins all 22 nonlinear-regime settings with large margins.

### 🤖 AI 总结

**一句话总结**：CALM通过学习跨数据源的共享嵌入并用RCT数据校准，从而在协变量不匹配时更稳健地结合观察性研究提升CATE估计。

**研究动机**：RCT对异质性效应往往统计功效不足，而大规模观察性研究可补充但与RCT存在协变量仅部分重叠的“特征不匹配”问题，直接插补容易引入偏差或负迁移。

**核心方法**：提出CALM：分别将OS与RCT特征映射到共同表示空间，先在OS上学习结局/效应模型并迁移到RCT嵌入空间，再利用RCT的随机化数据进行校准以保持因果可识别性；并给出有限样本风险上界，分解为对齐误差、结局模型复杂度与校准复杂度，含线性校准与神经网络两种实现。

**主要结论**：理论与实验表明嵌入对齐在特定条件下优于插补且在线性稀疏模型下严格泛化插补；线性CATE时多种校准法效果等价且线性变体可防负迁移，而神经嵌入在严重分布偏移下可能脆弱但在22个非线性设置中显著胜出。

**关键词**：异质性处理效应, 条件平均处理效应（CATE）, 随机对照试验（RCT）, 观察性研究数据融合, 协变量不匹配, 表示学习嵌入对齐, 校准迁移学习, 因果识别, 负迁移防护, 分布漂移鲁棒性, 有限样本风险界, 缺失协变量插补

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19186v1) | [下载PDF](https://arxiv.org/pdf/2603.19186v1.pdf)

---

## [24. MIDST Challenge at SaTML 2025: Membership Inference over Diffusion-models-based Synthetic Tabular data](https://arxiv.org/abs/2603.19185v1)

**作者**：Masoumeh Shafieinejad, Xi He, Mahshid Alinoori 等 9 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Synthetic data is often perceived as a silver-bullet solution to data anonymization and privacy-preserving data publishing. Drawn from generative models like diffusion models, synthetic data is expected to preserve the statistical properties of the original dataset while remaining resilient to privacy attacks. Recent developments of diffusion models have been effective on a wide range of data types, but their privacy resilience, particularly for tabular formats, remains largely unexplored. MIDST challenge sought a quantitative evaluation of the privacy gain of synthetic tabular data generated by diffusion models, with a specific focus on its resistance to membership inference attacks (MIAs). Given the heterogeneity and complexity of tabular data, multiple target models were explored for MIAs, including diffusion models for single tables of mixed data types and multi-relational tables with interconnected constraints. MIDST inspired the development of novel black-box and white-box MIAs tailored to these target diffusion models as a key outcome, enabling a comprehensive evaluation of their privacy efficacy. The MIDST GitHub repository is available at https://github.com/VectorInstitute/MIDST

### 🤖 AI 总结

**一句话总结**：Synthetic data is often perceived as a silver-bullet solution to data anonymization and privacy-preserving data publishing. Drawn from generative models like diffusion models, synthetic data is expect...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：合成表格数据, Diffusion, 隐私评测, 隐私增益量化, 成员推断攻击, 黑盒推断, 白盒推断, 多关系表格, 混合数据类型表, 数据匿名化, 隐私保护数据发布

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19185v1) | [下载PDF](https://arxiv.org/pdf/2603.19185v1.pdf)

---

## [25. SOL-ExecBench: Speed-of-Light Benchmarking for Real-World GPU Kernels Against Hardware Limits](https://arxiv.org/abs/2603.19173v1)

**作者**：Edward Lin, Sahil Modi, Siva Kumar Sastry Hari 等 33 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-19

### 📄 论文摘要

As agentic AI systems become increasingly capable of generating and optimizing GPU kernels, progress is constrained by benchmarks that reward speedup over software baselines rather than proximity to hardware-efficient execution. We present SOL-ExecBench, a benchmark of 235 CUDA kernel optimization problems extracted from 124 production and emerging AI models spanning language, diffusion, vision, audio, video, and hybrid architectures, targeting NVIDIA Blackwell GPUs. The benchmark covers forward and backward workloads across BF16, FP8, and NVFP4, including kernels whose best performance is expected to rely on Blackwell-specific capabilities. Unlike prior benchmarks that evaluate kernels primarily relative to software implementations, SOL-ExecBench measures performance against analytically derived Speed-of-Light (SOL) bounds computed by SOLAR, our pipeline for deriving hardware-grounded SOL bounds, yielding a fixed target for hardware-efficient optimization. We report a SOL Score that quantifies how much of the gap between a release-defined scoring baseline and the hardware SOL bound a candidate kernel closes. To support robust evaluation of agentic optimizers, we additionally provide a sandboxed harness with GPU clock locking, L2 cache clearing, isolated subprocess execution, and static analysis based checks against common reward-hacking strategies. SOL-ExecBench reframes GPU kernel benchmarking from beating a mutable software baseline to closing the remaining gap to hardware Speed-of-Light.

### 🤖 AI 总结

**一句话总结**：SOL-ExecBench 提出一个面向真实生产CUDA内核的“贴近硬件极限（Speed-of-Light）”评测基准，用固定的硬件上界而非软件baseline来衡量优化质量。

**研究动机**：现有GPU内核基准多以“相对软件实现的加速比”为目标，容易受baseline变化影响且不直接反映硬件效率上限，从而限制了自动/智能优化器的真实进步。

**核心方法**：构建包含235个来自124个真实与新兴AI模型的CUDA内核优化任务（覆盖前后向、BF16/FP8/NVFP4并面向NVIDIA Blackwell），并用SOLAR解析推导硬件“SOL上界”；通过SOL Score衡量候选内核相对评分baseline向SOL上界缩小的差距，同时提供带GPU锁频、清L2、隔离执行与静态检查的沙箱评测以减少reward-hacking。

**主要结论**：该基准将评测目标从“击败可变的软件baseline”转为“逼近可计算的硬件极限”，并通过稳健的评测与反作弊机制更可靠地区分优化器在硬件效率上的真实提升。

**关键词**：GPU 内核优化基准, 硬件效率评测, 解析性能模型, 沙箱评测框架, 奖励黑客防护, GPU 时钟锁定, SOL-ExecBench, Speed-of-Light

**评分**：45

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19173v1) | [下载PDF](https://arxiv.org/pdf/2603.19173v1.pdf)

---

## [26. Rigorous Error Certification for Neural PDE Solvers: From Empirical Residuals to Solution Guarantees](https://arxiv.org/abs/2603.19165v1)

**作者**：Amartya Mukherjee, Maxwell Fitzsimmons, David C. Del Rey Fernández 等 4 位作者  
**分类**：cs.LG, math.AP, math.FA  
**发布时间**：2026-03-19

### 📄 论文摘要

Uncertainty quantification for partial differential equations is traditionally grounded in discretization theory, where solution error is controlled via mesh/grid refinement. Physics-informed neural networks fundamentally depart from this paradigm: they approximate solutions by minimizing residual losses at collocation points, introducing new sources of error arising from optimization, sampling, representation, and overfitting. As a result, the generalization error in the solution space remains an open problem.   Our main theoretical contribution establishes generalization bounds that connect residual control to solution-space error. We prove that when neural approximations lie in a compact subset of the solution space, vanishing residual error guarantees convergence to the true solution. We derive deterministic and probabilistic convergence results and provide certified generalization bounds translating residual, boundary, and initial errors into explicit solution error guarantees.

### 🤖 AI 总结

**一句话总结**：论文建立了从“神经PDE求解器的经验残差控制”到“解空间真实误差上界”的严格理论桥梁，实现可认证的解误差保证。

**研究动机**：PINN等神经PDE方法以配点残差最小化替代传统网格离散，带来优化、采样、表示与过拟合等新误差源，使得残差小并不必然意味着解误差小，亟需可证明的泛化与误差认证框架。

**核心方法**：在假设神经近似解位于解空间的某个紧致子集（compactness）下，证明残差趋于0可推出对真实解的收敛；进一步给出确定性与概率性两类结果，并推导将域内残差、边界/初值误差显式转换为解空间误差上界的可认证泛化界。

**主要结论**：当满足紧致性等条件时，控制PDE残差（连同边界/初值误差）即可获得对解空间误差的显式保证：残差消失意味着解收敛到真解，并能提供确定性/概率性的误差认证界，从而把经验训练指标提升为可证明的解精度担保。

**关键词**：神经PDE求解器, 物理信息神经网络, 误差认证, 泛化误差界, 残差最小化, 解空间误差, 不确定性量化, 配点采样, 概率收敛, 确定性收敛, 紧性假设

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19165v1) | [下载PDF](https://arxiv.org/pdf/2603.19165v1.pdf)

---

## [27. Enhancing Pretrained Model-based Continual Representation Learning via Guided Random Projection](https://arxiv.org/abs/2603.19145v1)

**作者**：Ruilin Li, Heming Zou, Xiufeng Yan 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

Recent paradigms in Random Projection Layer (RPL)-based continual representation learning have demonstrated superior performance when building upon a pre-trained model (PTM). These methods insert a randomly initialized RPL after a PTM to enhance feature representation in the initial stage. Subsequently, a linear classification head is used for analytic updates in the continual learning stage. However, under severe domain gaps between pre-trained representations and target domains, a randomly initialized RPL exhibits limited expressivity under large domain shifts. While largely scaling up the RPL dimension can improve expressivity, it also induces an ill-conditioned feature matrix, thereby destabilizing the recursive analytic updates of the linear head. To this end, we propose the Stochastic Continual Learner with MemoryGuard Supervisory Mechanism (SCL-MGSM). Unlike random initialization, MGSM constructs the projection layer via a principled, data-guided mechanism that progressively selects target-aligned random bases to adapt the PTM representation to downstream tasks. This facilitates the construction of a compact yet expressive RPL while improving the numerical stability of analytic updates. Extensive experiments on multiple exemplar-free Class Incremental Learning (CIL) benchmarks demonstrate that SCL-MGSM achieves superior performance compared to state-of-the-art methods.

### 🤖 AI 总结

**一句话总结**：提出一种数据引导的随机投影层构建机制（SCL-MGSM），在大域偏移下以更紧凑且稳定的投影提升基于预训练模型的无样本类增量学习表现。

**研究动机**：现有RPL方法在PTM后插入随机初始化投影层，但面对预训练表征与目标域差距大时表达力不足；简单增大投影维度虽可提升表达力，却会造成特征矩阵病态，导致线性头解析式递推更新不稳定。

**核心方法**：SCL-MGSM用MemoryGuard Supervisory Mechanism替代纯随机初始化，通过数据引导逐步筛选更“对齐目标域”的随机基来构建投影层，在保持维度紧凑的同时增强表征；并通过更良好的数值条件改善线性分类头的递推解析更新稳定性。

**主要结论**：在多个无回放（exemplar-free）的类增量学习基准上，SCL-MGSM相较SOTA取得更优性能，尤其在大域迁移场景下兼顾了投影表达力与解析更新的数值稳定性。

**关键词**：持续表征学习, 持续学习, 类别增量学习, 无样本回放, 预训练模型, 随机投影层, 数据引导随机投影, 域偏移自适应, 解析更新, 数值稳定性, 病态特征矩阵, 随机基选择

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19145v1) | [下载PDF](https://arxiv.org/pdf/2603.19145v1.pdf)

---

## [28. SHAPCA: Consistent and Interpretable Explanations for Machine Learning Models on Spectroscopy Data](https://arxiv.org/abs/2603.19141v1)

**作者**：Mingxing Zhang, Nicola Rossberg, Simone Innocente 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-19

### 📄 论文摘要

In recent years, machine learning models have been increasingly applied to spectroscopic datasets for chemical and biomedical analysis. For their successful adoption, particularly in clinical and safety-critical settings, professionals and researchers must be able to understand and trust the reasoning behind model predictions. However, the inherently high dimensionality and strong collinearity of spectroscopy data pose a fundamental challenge to model explainability. These properties not only complicate model training but also undermine the stability and consistency of explanations, leading to fluctuations in feature importance across repeated training runs. Feature extraction techniques have been used to reduce the input dimensionality; these new features hinder the connection between the prediction and the original signal. This study proposes SHAPCA, an explainable machine learning pipeline that combines Principal Component Analysis (for dimensionality reduction) and Shapely Additive exPlanations (for post hoc explanation) to provide explanations in the original input space, which a practitioner can interpret and link back to the biological components. The proposed framework enables analysis from both global and local perspectives, revealing the spectral bands that drive overall model behaviour as well as the instance-specific features that influence individual predictions. Numerical analysis demonstrated the interpretability of the results and greater consistency across different runs.

### 🤖 AI 总结

**一句话总结**：SHAPCA将PCA降维与SHAP解释结合，并把重要性映射回原始光谱空间，从而在高维强共线的光谱数据上获得更一致且可解释的模型解释。

**研究动机**：光谱数据维度高且特征强共线，导致模型解释在不同训练运行间不稳定、特征重要性波动大；同时常见特征提取会削弱解释与原始光谱/生物成分的对应关系。

**核心方法**：提出SHAPCA流程：先用PCA在潜在空间训练机器学习模型以缓解维度与共线性问题，再用SHAP做事后解释，并将贡献从主成分空间转换回原始波长/谱段，实现全局与局部两层解释。

**主要结论**：实验数值分析表明，该方法能在原始光谱域给出可链接到谱段/成分的解释，并相较于直接在原始特征上解释表现出更好的跨重复训练一致性与稳定性。

**关键词**：光谱数据, 可解释性, 解释一致性, 高维共线性, 主成分分析（PCA）, 特征重要性稳定性, 原始输入空间映射, 全局解释, 局部解释

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19141v1) | [下载PDF](https://arxiv.org/pdf/2603.19141v1.pdf)

---

## [29. Hierarchical Latent Structure Learning through Online Inference](https://arxiv.org/abs/2603.19139v1)

**作者**：Ines Aitsahalia, Kiyohito Iigaya  
**分类**：cs.LG, q-bio.NC  
**发布时间**：2026-03-19

### 📄 论文摘要

Learning systems must balance generalization across experiences with discrimination of task-relevant details. Effective learning therefore requires representations that support both. Online latent-cause models support incremental inference but assume flat partitions, whereas hierarchical Bayesian models capture multilevel structure but typically require offline inference. We introduce the Hierarchical Online Learning of Multiscale Experience Structure (HOLMES) model, a computational framework for hierarchical latent structure learning through online inference. HOLMES combines a variation on the nested Chinese Restaurant Process prior with sequential Monte Carlo inference to perform tractable trial-by-trial inference over hierarchical latent representations without explicit supervision over the latent structure. In simulations, HOLMES matched the predictive performance of flat models while learning more compact representations that supported one-shot transfer to higher-level latent categories. In a context-dependent task with nested temporal structure, HOLMES also improved outcome prediction relative to flat models. These results provide a tractable computational framework for discovering hierarchical structure in sequential data.

### 🤖 AI 总结

**一句话总结**：HOLMES通过将分层先验与在线序列推断结合，实现了在序列数据中对分层潜在结构的逐试次学习，并在保持预测性能的同时获得更紧凑且可迁移的表征。

**研究动机**：现有在线潜在原因模型便于增量推断但结构扁平，难以表达多层次规律；而分层贝叶斯模型能刻画层级结构却常依赖离线推断，难以用于实时/连续学习场景。

**核心方法**：提出HOLMES：采用一种改造的嵌套中餐馆过程（nested CRP）作为分层结构先验，并用序列蒙特卡洛（SMC）进行可 tractable 的trial-by-trial在线推断，在无显式结构监督下同时推断多层潜变量。

**主要结论**：仿真显示HOLMES在预测表现上与扁平模型相当或更优，但学习到更紧凑的层级表示，并支持对高层潜在类别的一次性迁移；在具有嵌套时间结构的情境依赖任务中也优于扁平模型的结果预测。

**关键词**：层次潜在结构学习, 层次贝叶斯模型, 潜在原因模型, 嵌套中餐馆过程（nCRP）, 顺序蒙特卡洛（SMC）, 试次级增量学习, 多尺度表征, 序列数据建模, 一次迁移学习, 上下文依赖预测, 嵌套时间结构

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19139v1) | [下载PDF](https://arxiv.org/pdf/2603.19139v1.pdf)

---

## [30. Adaptive Regime-Aware Stock Price Prediction Using Autoencoder-Gated Dual Node Transformers with Reinforcement Learning Control](https://arxiv.org/abs/2603.19136v1)

**作者**：Mohammad Al Ridhawi, Mahtab Haj Ali, Hussein Al Osman  
**分类**：cs.LG, cs.AI, q-fin.ST  
**发布时间**：2026-03-19

### 📄 论文摘要

Stock markets exhibit regime-dependent behavior where prediction models optimized for stable conditions often fail during volatile periods. Existing approaches typically treat all market states uniformly or require manual regime labeling, which is expensive and quickly becomes stale as market dynamics evolve. This paper introduces an adaptive prediction framework that adaptively identifies deviations from normal market conditions and routes data through specialized prediction pathways. The architecture consists of three components: (1) an autoencoder trained on normal market conditions that identifies anomalous regimes through reconstruction error, (2) dual node transformer networks specialized for stable and event-driven market conditions respectively, and (3) a Soft Actor-Critic reinforcement learning controller that adaptively tunes the regime detection threshold and pathway blending weights based on prediction performance feedback. The reinforcement learning component enables the system to learn adaptive regime boundaries, defining anomalies as market states where standard prediction approaches fail. Experiments on 20 S&P 500 stocks spanning 1982 to 2025 demonstrate that the proposed framework achieves 0.68% MAPE for one-day predictions without the reinforcement controller and 0.59% MAPE with the full adaptive system, compared to 0.80% for the baseline integrated node transformer. Directional accuracy reaches 72% with the complete framework. The system maintains robust performance during high-volatility periods, with MAPE below 0.85% when baseline models exceed 1.5%. Ablation studies confirm that each component contributes meaningfully: autoencoder routing accounts for 36% relative MAPE degradation upon removal, followed by the SAC controller at 15% and the dual-path architecture at 7%.

### 🤖 AI 总结

**一句话总结**：提出一种可自适应识别市场“稳定/异常”状态并动态选择预测通路的框架，在高波动时期仍保持较低误差并显著优于基线模型。

**研究动机**：股票市场存在明显的状态切换（regime），在平稳期训练的模型常在高波动/事件期失效；而现有方法要么忽略状态差异、要么依赖昂贵且易过时的人工标注。

**核心方法**：用仅在“正常市场”训练的自编码器以重构误差检测异常状态并进行路由；采用两套分别面向稳定与事件驱动行情的双节点Transformer，并用Soft Actor-Critic强化学习控制器根据预测反馈自适应调整异常阈值与两通路融合权重。

**主要结论**：在20只标普股票（1982–2025）上，完整系统将1日预测MAPE从基线0.80%降至0.59%，方向准确率达72%，且在高波动期仍能将MAPE控制在0.85%以内；消融显示自编码器路由、SAC控制器与双通路结构均有显著贡献（移除分别导致约36%、15%、7%的相对劣化）。

**关键词**：股价预测, 市场状态切换, 波动率分段, 异常检测, 自编码器重构误差, 门控路由, 混合专家, 强化学习控制, 软演员-评论家（SAC）, 阈值自适应

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.19136v1) | [下载PDF](https://arxiv.org/pdf/2603.19136v1.pdf)

---

