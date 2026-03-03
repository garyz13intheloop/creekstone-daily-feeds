# arXiv AI 论文日报 | 2026-03-02

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (3 篇)
- [cs.CL](#csCL) (4 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.AI](#csAI) (1 篇)

---

## cs.AI

## [1. Information-Theoretic Framework for Self-Adapting Model Predictive Controllers](https://arxiv.org/abs/2603.01286v1)

**作者**：Wael Hafez, Amir Nazeri  
**分类**：cs.AI, cs.RO  
**发布时间**：2026-03-01

### 📄 论文摘要

Model Predictive Control (MPC) is a vital technique for autonomous systems, like Unmanned Aerial Vehicles (UAVs), enabling optimized motion planning. However, traditional MPC struggles to adapt to real-time changes such as dynamic obstacles and shifting system dynamics, lacking inherent mechanisms for self-monitoring and adaptive optimization. Here, we introduce Entanglement Learning (EL), an information-theoretic framework that enhances MPC adaptability through an Information Digital Twin (IDT). The IDT monitors and quantifies, in bits, the information flow between MPC inputs, control actions, and UAV behavior. By introducing new information-theoretic metrics we call entanglement metrics, it tracks variations in these dependencies. These metrics measure the mutual information between the optimizer's input, its control actions, and the resulting UAV dynamics, enabling a deeper understanding of their interrelationships. This allows the IDT to detect performance deviations and generate real-time adaptive signals to recalibrate MPC parameters, preserving stability. Unlike traditional MPC, which relies on error-based feedback, this dual-feedback approach leverages information flow for proactive adaptation to evolving conditions. Scalable and leveraging existing infrastructure, this framework improves MPC reliability and robustness across diverse scenarios, extending beyond UAV control to any MPC implementation requiring adaptive performance.

### 🤖 AI 总结

**一句话总结**：提出一种基于信息论的“纠缠学习”框架，通过信息数字孪生实时监测MPC内部信息流并自适应调参，从而提升在动态环境下的稳定性与鲁棒性。

**研究动机**：传统MPC对动态障碍、模型漂移等实时变化缺乏自监测与自适应机制，往往只能依赖误差反馈被动修正，难以及时发现性能退化并稳定重整参数。

**核心方法**：构建Information Digital Twin(IDT)，以互信息为核心定义“纠缠度量”，量化优化器输入—控制动作—系统动力学之间的信息依赖变化；当度量指示依赖结构/信息流异常时，IDT输出实时自适应信号以重校准MPC参数，形成区别于误差反馈的“信息流+误差”双反馈闭环。

**主要结论**：该框架可在不大幅改动既有MPC基础设施的前提下，主动检测控制性能偏离并在线调参以维持稳定性；方法具可扩展性，除UAV外也适用于需要自适应性能的各类MPC应用场景。

**关键词**：模型预测控制（MPC）, 信息论控制, 信息数字孪生（IDT）, 信息流监测, 纠缠学习（EL）, 纠缠度量, 双反馈控制, 无人机（UAV）控制, 鲁棒性与稳定性

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01286v1) | [下载PDF](https://arxiv.org/pdf/2603.01286v1.pdf)

---

## cs.CL

## [2. Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning](https://arxiv.org/abs/2603.01326v1)

**作者**：Hamed Damirchi, Ignacio Meza De la Jara, Ehsan Abbasnejad 等 6 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-03-01

### 📄 论文摘要

Existing explainability methods for Large Language Models (LLMs) typically treat hidden states as static points in activation space, assuming that correct and incorrect inferences can be separated using representations from an individual layer. However, these activations are saturated with polysemantic features, leading to linear probes learning surface-level lexical patterns rather than underlying reasoning structures. We introduce Truth as a Trajectory (TaT), which models the transformer inference as an unfolded trajectory of iterative refinements, shifting analysis from static activations to layer-wise geometric displacement. By analyzing displacement of representations across layers, TaT uncovers geometric invariants that distinguish valid reasoning from spurious behavior. We evaluate TaT across dense and Mixture-of-Experts (MoE) architectures on benchmarks spanning commonsense reasoning, question answering, and toxicity detection. Without access to the activations themselves and using only changes in activations across layers, we show that TaT effectively mitigates reliance on static lexical confounds, outperforming conventional probing, and establishes trajectory analysis as a complementary perspective on LLM explainability.

### 🤖 AI 总结

**一句话总结**：提出“Truth as a Trajectory (TaT)”把LLM推理看作跨层表示的轨迹位移，用几何不变量区分真实推理与伪相关行为，并在多任务与多架构上优于传统静态探针。

**研究动机**：现有可解释性/探针方法常把单层隐藏状态当作静态点来分离对错推理，但隐藏状态高度多义导致线性探针易学到词汇等表层线索而非推理结构。

**核心方法**：TaT不直接使用各层激活本身，而是分析表示在相邻层之间的几何位移（displacement）形成的跨层轨迹，将推理过程视为迭代精炼的展开，并从轨迹中提取能区分有效推理与虚假模式的几何不变量。

**主要结论**：仅依赖跨层变化信息，TaT能显著减弱静态词汇混淆带来的偏差，在密集模型与MoE模型、常识推理/问答/毒性检测等基准上整体优于传统 probing，表明轨迹视角是对LLM可解释性的有效补充。

**关键词**：LLM 可解释性, 内部表征分析, 轨迹分析, 层间几何位移, 几何不变量, 推理正确性判别, 伪推理检测, 多义特征, 线性探针, 词汇混淆抑制, 毒性检测

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01326v1) | [下载PDF](https://arxiv.org/pdf/2603.01326v1.pdf)

---

## [3. Catalyst-Agent: Autonomous heterogeneous catalyst screening and optimization with an LLM Agent](https://arxiv.org/abs/2603.01311v1)

**作者**：Achuth Chandrasekhar, Janghoon Ock, Amir Barati Farimani  
**分类**：cs.CL  
**发布时间**：2026-03-01

### 📄 论文摘要

The discovery of novel catalysts tailored for particular applications is a major challenge for the twenty-first century. Traditional methods for this include time-consuming and expensive experimental trial-and-error approaches in labs based on chemical theory or heavily computational first-principles approaches based on density functional theory. Recent studies show that deep learning models like graph neural networks (GNNs) can significantly speed up the screening and discovery of catalyst materials by many orders of magnitude, with very high accuracy and fidelity.   In this work, we introduce Catalyst-Agent, a Model Context Protocol (MCP) server-based, LLM-powered AI agent. It can explore vast material databases using the OPTIMADE API, make structural modifications, calculate adsorption energies using Meta FAIRchem's UMA (GNN) model via FAIRchem's AdsorbML workflow and slab construction, and make useful material suggestions to the researcher in a closed-loop manner, including surface-level modifications to refine near-miss candidates.   It is tested on three pivotal reactions: the oxygen reduction reaction (ORR), the nitrogen reduction reaction (NRR), and the CO2 reduction reaction (CO2RR). Catalyst-Agent achieves a success rate of 23-34 percent among all the materials it chooses and evaluates, and manages to converge in 1-2 trials per successful material on average. This work demonstrates the potential of AI agents to exercise their planning capabilities and tool use to operationalize the catalyst screening workflow, provide useful, testable hypotheses, and accelerate future scientific discoveries for humanity with minimal human intervention.

### 🤖 AI 总结

**一句话总结**：Catalyst-Agent 将LLM代理与材料数据库检索、结构改造和GNN吸附能预测工具链整合成闭环流程，用较少试验次数实现异相催化剂的自动筛选与优化。

**研究动机**：传统催化剂发现依赖昂贵且耗时的实验试错或高成本DFT计算，难以在海量材料空间中高效迭代。作者希望利用深度学习与LLM的规划/工具调用能力，把催化筛选工作流自动化并加速可验证候选的提出。

**核心方法**：构建基于MCP服务器的LLM Agent：通过OPTIMADE API探索材料数据库，生成/修改候选结构与表面，并调用Meta FAIRchem UMA（GNN）+ AdsorbML（含slab构建）计算吸附能。以ORR/NRR/CO2RR为目标反应进行闭环评估与“近似命中”候选的表面级精修推荐。

**主要结论**：在三类关键反应上，系统在其选择并评估的材料中取得约23–34%的成功率，且每个成功材料平均1–2次试验即可收敛。结果表明LLM代理可有效编排催化筛选工具链并输出可测试假设，从而在较少人工干预下加速催化发现。

**关键词**：异相催化筛选, 催化剂优化, 闭环实验设计, 材料数据库检索, 吸附能预测, 图神经网络(GNN)势能模型, 表面结构修饰, Catalyst-Agent

**评分**：52

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01311v1) | [下载PDF](https://arxiv.org/pdf/2603.01311v1.pdf)

---

## [4. Individual Turing Test: A Case Study of LLM-based Simulation Using Longitudinal Personal Data](https://arxiv.org/abs/2603.01289v1)

**作者**：Minghao Guo, Ziyi Ye, Wujiang Xu 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-01

### 📄 论文摘要

Large Language Models (LLMs) have demonstrated remarkable human-like capabilities, yet their ability to replicate a specific individual remains under-explored. This paper presents a case study to investigate LLM-based individual simulation with a volunteer-contributed archive of private messaging history spanning over ten years. Based on the messaging data, we propose the "Individual Turing Test" to evaluate whether acquaintances of the volunteer can correctly identify which response in a multi-candidate pool most plausibly comes from the volunteer. We investigate prevalent LLM-based individual simulation approaches including: fine-tuning, retrieval-augmented generation (RAG), memory-based approach, and hybrid methods that integrate fine-tuning and RAG or memory. Empirical results show that current LLM-based simulation methods do not pass the Individual Turing Test, but they perform substantially better when the same test is conducted on strangers to the target individual. Additionally, while fine-tuning improves the simulation in daily chats representing the language style of the individual, retrieval-augmented and memory-based approaches demonstrate stronger performance on questions involving personal opinions and preferences. These findings reveal a fundamental trade-off between parametric and non-parametric approaches to individual simulation with LLMs when given a longitudinal context.

### 🤖 AI 总结

**一句话总结**：论文提出“个体图灵测试”来评估LLM能否模拟特定个人，发现现有方法在熟人面前仍难以以假乱真，但对陌生人更容易奏效，并呈现参数化与非参数化方法的权衡。

**研究动机**：尽管LLM表现出类人对话能力，但“能否复现某个具体个体的语言风格与观点偏好”缺乏系统评估。作者利用十余年私聊纵向数据，试图建立更贴近真实社交识别场景的测评框架。

**核心方法**：基于志愿者长期私聊数据构建多候选回答池，让志愿者熟人判断哪条最像本人（Individual Turing Test），并对比微调、RAG、记忆机制以及二者混合等个体模拟方案的表现。进一步区分日常闲聊与涉及个人观点/偏好的问题类型，分析不同方法的优势。

**主要结论**：现有LLM个体模拟整体未通过“熟人”个体图灵测试，但在“陌生人”评测下显著更好，说明真实熟人识别更苛刻。微调更擅长复现日常聊天的语言风格，而RAG/记忆更擅长回答个人意见与偏好问题，体现参数化（风格）与非参数化（事实/偏好）之间的基本权衡。

**关键词**：个体图灵测试, 个体模拟, 纵向个人数据, 私信对话语料, 个性化对话生成, 检索增强生成（RAG）, 记忆增强, 混合方法（微调+RAG）, 参数化-非参数化权衡, 熟人识别评测

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01289v1) | [下载PDF](https://arxiv.org/pdf/2603.01289v1.pdf)

---

## [5. Efficient Extractive Summarization with MAMBA-Transformer Hybrids for Low-Resource Scenarios](https://arxiv.org/abs/2603.01288v1)

**作者**：Nisrine Ait Khayi  
**分类**：cs.CL  
**发布时间**：2026-03-01

### 📄 论文摘要

Extractive summarization of long documents is bottlenecked by quadratic complexity, often forcing truncation and limiting deployment in resource-constrained settings. We introduce the first Mamba-Transformer hybrid for extractive summarization, combining the semantic strength of pre-trained transformers with the linear-time processing of state space models. Leveraging Mamba's ability to process full documents without truncation, our approach preserves context while maintaining strong summarization quality. The architecture includes: (1) a transformer encoder for sentence-level semantics, (2) a Mamba state space model to capture inter-sentence dependencies efficiently, and (3) a linear classifier for sentence relevance prediction. Across news, argumentative, and scientific domains under low-resource conditions, our method achieves: (1) large gains over BERTSUM and MATCHSUM, including +0.23 ROUGE-1 on ArXiv and statistically significant improvements on all datasets (p < 0.001); (2) consistent advantages across domains, strongest on the longest documents; (3) robust performance with limited training data; and (4) 24-27% faster inference on news summarization (CNN/DailyMail). We introduce the first hybrid Transformer-state space architecture for summarization, showing significant ROUGE improvements in low-resource scenarios.

### 🤖 AI 总结

**一句话总结**：提出一种用于抽取式摘要的Mamba-Transformer混合架构，在低资源与长文档场景下以线性时间处理全篇并获得更好ROUGE与更快推理。

**研究动机**：长文档抽取式摘要受Transformer二次复杂度限制，常需截断导致上下文丢失，且在算力/数据受限环境难以部署。需要一种既保留Transformer语义优势又能高效建模长程依赖的方案。

**核心方法**：使用Transformer编码句子级语义表示，再用Mamba状态空间模型以线性复杂度建模句间依赖与全局上下文，最后通过线性分类器预测句子重要性完成抽取。整体针对低资源训练设定评测，并强调无需截断即可处理长文档。

**主要结论**：在新闻、论述与科学文档等多域低资源条件下，相比BERTSUM与MATCHSUM取得稳定且显著的ROUGE提升（如ArXiv上ROUGE-1 +0.23，p<0.001），长文档收益更大，并在CNN/DailyMail上实现约24–27%更快推理。

**关键词**：抽取式摘要, 长文档处理, 低资源场景, 状态空间模型, 线性时间复杂度, 跨句依赖建模, 句子级语义编码, 句子相关性分类, 推理加速

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01288v1) | [下载PDF](https://arxiv.org/pdf/2603.01288v1.pdf)

---

## cs.CV

## [6. You Only Need One Stage: Novel-View Synthesis From A Single Blind Face Image](https://arxiv.org/abs/2603.01328v1)

**作者**：Taoyue Wang, Xiang Zhang, Xiaotian Li 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-01

### 📄 论文摘要

We propose a novel one-stage method, NVB-Face, for generating consistent Novel-View images directly from a single Blind Face image. Existing approaches to novel-view synthesis for objects or faces typically require a high-resolution RGB image as input. When dealing with degraded images, the conventional pipeline follows a two-stage process: first restoring the image to high resolution, then synthesizing novel views from the restored result. However, this approach is highly dependent on the quality of the restored image, often leading to inaccuracies and inconsistencies in the final output. To address this limitation, we extract single-view features directly from the blind face image and introduce a feature manipulator that transforms these features into 3D-aware, multi-view latent representations. Leveraging the powerful generative capacity of a diffusion model, our framework synthesizes high-quality, consistent novel-view face images. Experimental results show that our method significantly outperforms traditional two-stage approaches in both consistency and fidelity.

### 🤖 AI 总结

**一句话总结**：提出NVB-Face，一种从单张低质（blind）人脸图像端到端直接生成一致高质量多视角的新视角合成的一阶段扩散框架。

**研究动机**：现有新视角合成在退化输入上通常采用“先超分/复原、再合成”的两阶段流程，强依赖复原质量，易在细节与几何上引入误差并导致多视角不一致。

**核心方法**：直接从blind人脸提取单视角特征，并通过特征操控器将其变换为具备3D感知的多视角潜在表示；再利用扩散模型的生成能力，从该3D-aware潜变量合成不同视角的人脸图像以保证一致性与清晰度。

**主要结论**：实验表明该一阶段方法在视角一致性与图像保真度上显著优于传统两阶段方案，能从退化单图稳定生成高质量的新视角人脸。

**关键词**：新视角合成, 单幅人脸, 盲退化图像, 单阶段方法, 单视图特征提取, 特征操控, 3D感知表示, 多视图潜表示, Diffusion, 多视图一致性, 高保真生成

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01328v1) | [下载PDF](https://arxiv.org/pdf/2603.01328v1.pdf)

---

## [7. Open-Vocabulary vs Supervised Learning Methods for Post-Disaster Visual Scene Understanding](https://arxiv.org/abs/2603.01324v1)

**作者**：Anna Michailidou, Georgios Angelidis, Vasileios Argyriou 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-01

### 📄 论文摘要

Aerial imagery is critical for large-scale post-disaster damage assessment. Automated interpretation remains challenging due to clutter, visual variability, and strong cross-event domain shift, while supervised approaches still rely on costly, task-specific annotations with limited coverage across disaster types and regions. Recent open-vocabulary and foundation vision models offer an appealing alternative, by reducing dependence on fixed label sets and extensive task-specific annotations. Instead, they leverage large-scale pretraining and vision-language representations. These properties are particularly relevant for post-disaster domains, where visual concepts are ambiguous and data availability is constrained. In this work, we present a comparative evaluation of supervised learning and open-vocabulary vision models for post-disaster scene understanding, focusing on semantic segmentation and object detection across multiple datasets, including FloodNet+, RescueNet, DFire, and LADD. We examine performance trends, failure modes, and practical trade-offs between different learning paradigms, providing insight into their applicability for real-world disaster response. The most notable remark across all evaluated benchmarks is that supervised training remains the most reliable approach (i.e., when the label space is fixed and annotations are available), especially for small objects and fine boundary delineation in cluttered scenes.

### 🤖 AI 总结

**一句话总结**：论文系统对比了灾后航拍场景理解中监督学习与开放词汇/基础视觉模型在分割与检测任务上的表现与权衡，发现有标注且标签固定时监督方法总体最可靠。

**研究动机**：灾后航拍解译面临杂乱场景、强跨事件域偏移与概念歧义，且监督方法依赖昂贵且覆盖有限的任务标注；开放词汇模型有望减少对固定标签与大量标注的依赖，因此需要评估其在灾后场景中的真实适用性。

**核心方法**：在FloodNet+、RescueNet、DFire、LADD等多数据集上，对监督学习与开放词汇/视觉-语言预训练模型进行语义分割与目标检测的对比评测，分析性能趋势、失败模式与实际部署的取舍。

**主要结论**：总体上监督训练在固定标签空间且有充足标注时仍最稳健，尤其在小目标识别与复杂杂乱场景的精细边界分割上优势明显；开放词汇模型虽具灵活性与弱标注优势，但在上述细粒度场景更易受限。

**关键词**：灾害损失评估, 航空影像, 开放词汇视觉模型, 基础视觉模型, 视觉-语言表征, 监督学习, 语义分割, 目标检测, 跨事件域偏移, 多数据集基准评测

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01324v1) | [下载PDF](https://arxiv.org/pdf/2603.01324v1.pdf)

---

## [8. When Does RL Help Medical VLMs? Disentangling Vision, SFT, and RL Gains](https://arxiv.org/abs/2603.01301v1)

**作者**：Ahmadreza Jeddi, Kimia Shaban, Negin Baghbanzadeh 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-01

### 📄 论文摘要

Reinforcement learning (RL) is increasingly used to post-train medical Vision-Language Models (VLMs), yet it remains unclear whether RL improves medical visual reasoning or mainly sharpens behaviors already induced by supervised fine-tuning (SFT). We present a controlled study that disentangles these effects along three axes: vision, SFT, and RL. Using MedMNIST as a multi-modality testbed, we probe visual perception by benchmarking VLM vision towers against vision-only baselines, quantify reasoning support and sampling efficiency via Accuracy@1 versus Pass@K, and evaluate when RL closes the support gap and how gains transfer across modalities. We find that RL is most effective when the model already has non-trivial support (high Pass@K): it primarily sharpens the output distribution, improving Acc@1 and sampling efficiency, while SFT expands support and makes RL effective. Based on these findings, we propose a boundary-aware recipe and instantiate it by RL post-training an OctoMed-initialized model on a small, balanced subset of PMC multiple-choice VQA, achieving strong average performance across six medical VQA benchmarks.

### 🤖 AI 总结

**一句话总结**：论文系统拆解医疗VLM中视觉能力、SFT与RL的贡献，发现RL主要在模型已有较强“支持度”(高Pass@K)时通过“锐化输出分布”显著提升Acc@1与采样效率，而SFT负责扩展支持度使RL变得有效。

**研究动机**：医疗VLM后训练中RL日益常用，但其提升究竟来自真实视觉推理增强还是仅巩固SFT已学到的行为并不清楚；因此需要可控实验来分离视觉塔、SFT与RL各自带来的增益边界与适用条件。

**核心方法**：以MedMNIST构建多模态可控测试床：对比VLM视觉塔与纯视觉基线评估感知能力，用Acc@1与Pass@K刻画“输出质量”与“支持度/采样效率”，并测试RL何时能缩小支持缺口及跨模态迁移；据此提出“边界感知”训练配方，并在OctoMed初始化模型上用小规模、平衡的PMC多选VQA做RL后训练验证。

**主要结论**：RL最擅长在已有非平凡支持度的前提下提升Acc@1并减少依赖多次采样，本质更像对已有解空间的分布重整而非扩展新能力；SFT更关键地扩展支持度并为RL创造生效前提，按该原则进行RL后训练可在多项医疗VQA基准上取得稳健平均提升。

**关键词**：医疗视觉语言模型, 强化学习后训练, 监督微调, 视觉推理, 收益解耦分析, 视觉塔评测, 采样效率, 多模态迁移, 医学VQA基准

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01301v1) | [下载PDF](https://arxiv.org/pdf/2603.01301v1.pdf)

---

## cs.LG

## [9. PAC Guarantees for Reinforcement Learning: Sample Complexity, Coverage, and Structure](https://arxiv.org/abs/2603.01309v1)

**作者**：Joshua Steier  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-03-01

### 📄 论文摘要

When data is scarce or mistakes are costly, average-case metrics fall short. What a practitioner needs is a guarantee: with probability at least $1-δ$, the learned policy is $\varepsilon$-close to optimal after $N$ episodes. This is the PAC promise, and between 2018 and 2025 the RL theory community made striking progress on when such promises can be kept. We survey that progress. Our organizing tool is the Coverage-Structure-Objective (CSO) framework, proposed here, which decomposes nearly every PAC sample complexity result into three factors: coverage (how data were obtained), structure (intrinsic MDP or function-class complexity), and objective (what the learner must deliver). CSO is not a theorem but an interpretive template that identifies bottlenecks and makes cross-setting comparison immediate. The technical core covers tight tabular baselines and the uniform-PAC bridge to regret; structural complexity measures (Bellman rank, witness rank, Bellman-Eluder dimension) governing learnability with function approximation; results for linear, kernel/NTK, and low-rank models; reward-free exploration as upfront coverage investment; and pessimistic offline RL where inherited coverage is the binding constraint. We provide practitioner tools: rate lookup tables indexed by CSO coordinates, Bellman residual diagnostics, coverage estimation with deployment gates, and per-episode policy certificates. A final section catalogs open problems, separating near-term targets from frontier questions where coverage, structure, and computation tangle in ways current theory cannot resolve.

### 🤖 AI 总结

**一句话总结**：本文综述2018-2025年强化学习PAC样本复杂度保证的理论进展，并提出CSO（覆盖-结构-目标）框架来统一比较不同设定下的可学习性与样本需求。

**研究动机**：在数据稀缺或试错代价高的场景中，平均性能指标不足以支撑部署，需要以高概率保证学到的策略在有限回合内接近最优；但不同RL设定的PAC结果分散且难以横向对比。

**核心方法**：提出CSO解释框架，将几乎所有PAC样本复杂度结果拆解为覆盖（数据获取/探索方式）、结构（MDP或函数类复杂度度量，如Bellman rank、witness rank、Bellman-Eluder维度等）与目标（需要输出的保证形式）；并系统整理表格型基线、uniform-PAC与regret连接、函数逼近（线性/核/NTK/低秩）、reward-free探索与悲观离线RL等结果，配套给出速率查表与诊断/证书工具。

**主要结论**：PAC保证能否成立与样本复杂度大小通常由“覆盖是否足够”与“结构复杂度是否可控”共同决定，且不同目标形式会改变最紧瓶颈；文章给出可操作的估计与认证手段（覆盖估计、Bellman残差诊断、每回合证书）并归纳了覆盖-结构-计算交织下仍未解决的开放问题。

**关键词**：PAC 强化学习, 样本复杂度, 结构复杂度, 统一 PAC-后悔界, 函数近似可学习性, PAC, Guarantees, Reinforcement

**评分**：15

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01309v1) | [下载PDF](https://arxiv.org/pdf/2603.01309v1.pdf)

---

## [10. Nonconvex Latent Optimally Partitioned Block-Sparse Recovery via Log-Sum and Minimax Concave Penalties](https://arxiv.org/abs/2603.01304v1)

**作者**：Takanobu Furuhashi, Hiroki Kuroda, Masahiro Yukawa 等 6 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-03-01

### 📄 论文摘要

We propose two nonconvex regularization methods, LogLOP-l2/l1 and AdaLOP-l2/l1, for recovering block-sparse signals with unknown block partitions. These methods address the underestimation bias of existing convex approaches by extending log-sum penalty and the Minimax Concave Penalty (MCP) to the block-sparse domain via novel variational formulations. Unlike Generalized Moreau Enhancement (GME) and Bayesian methods dependent on the squared-error data fidelity term, our proposed methods are compatible with a broad range of data fidelity terms. We develop efficient Alternating Direction Method of Multipliers (ADMM)-based algorithms for these formulations that exhibit stable empirical convergence. Numerical experiments on synthetic data, angular power spectrum estimation, and denoising of nanopore currents demonstrate that our methods outperform state-of-the-art baselines in estimation accuracy.

### 🤖 AI 总结

**一句话总结**：提出两种面向“块划分未知”的块稀疏恢复非凸正则方法（LogLOP-l2/l1 与 AdaLOP-l2/l1），在多类任务上较现有方法取得更高估计精度。

**研究动机**：现有凸正则在块稀疏恢复中常产生幅度低估偏差，且部分相关方法（如依赖GME或贝叶斯框架）往往绑定平方误差数据保真项，适用范围受限；同时真实信号的块划分往往未知，需要可自适应的分块建模。

**核心方法**：将log-sum惩罚与MCP通过新的变分（latent/variational）表述扩展到块稀疏域，形成可用于广泛数据保真项的LogLOP-l2/l1与AdaLOP-l2/l1模型；并基于这些表述设计ADMM求解算法，实现高效且经验上稳定收敛的优化。

**主要结论**：在合成数据、角功率谱估计与纳米孔电流去噪实验中，两种非凸方法相较多种SOTA基线在恢复/估计精度上更优，并展现出良好的算法稳定性与更广的保真项兼容性。

**关键词**：块稀疏恢复, 未知块划分, 非凸正则化, 变分表述, 数据保真项泛化, 欠估偏差, 角功率谱估计, 纳米孔电流去噪

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01304v1) | [下载PDF](https://arxiv.org/pdf/2603.01304v1.pdf)

---

## [11. I Can't Believe It's Not Robust: Catastrophic Collapse of Safety Classifiers under Embedding Drift](https://arxiv.org/abs/2603.01297v1)

**作者**：Subramanyam Sahoo, Vinija Jain, Divya Chaudhary 等 4 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-03-01

### 📄 论文摘要

Instruction tuned reasoning models are increasingly deployed with safety classifiers trained on frozen embeddings, assuming representation stability across model updates. We systematically investigate this assumption and find it fails: normalized perturbations of magnitude $σ=0.02$ (corresponding to $\approx 1^\circ$ angular drift on the embedding sphere) reduce classifier performance from $85\%$ to $50\%$ ROC-AUC. Critically, mean confidence only drops $14\%$, producing dangerous silent failures where $72\%$ of misclassifications occur with high confidence, defeating standard monitoring. We further show that instruction-tuned models exhibit 20$\%$ worse class separability than base models, making aligned systems paradoxically harder to safeguard. Our findings expose a fundamental fragility in production AI safety architectures and challenge the assumption that safety mechanisms transfer across model versions.

### 🤖 AI 总结

**一句话总结**：论文揭示：即使嵌入仅发生极小角度漂移，基于“冻结嵌入”的安全分类器也会性能断崖式下降且常以高置信度静默误判。

**研究动机**：生产中常将安全分类器建立在固定的嵌入表示上，并默认模型迭代后表示仍稳定、分类器可直接迁移；作者质疑这一关键假设是否成立及其安全风险。

**核心方法**：系统性对嵌入向量施加归一化的小幅扰动（如σ=0.02，对应约1°角漂移），评估安全分类器的ROC-AUC与置信度变化，并比较指令微调模型与基础模型的类可分性差异。

**主要结论**：微小嵌入漂移即可将ROC-AUC从85%拉低到50%，且平均置信度仅下降14%，导致大量高置信度误判（约72%）难以被监控发现；同时指令微调模型的类可分性比基础模型差约20%，使对齐后的系统反而更难用现有架构保障安全。

**关键词**：安全分类器, 嵌入漂移, 表示稳定性假设, 冻结嵌入, 模型更新兼容性, 鲁棒性退化, 静默失效, 高置信误判, 置信度校准, 类可分性, 指令微调模型

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01297v1) | [下载PDF](https://arxiv.org/pdf/2603.01297v1.pdf)

---

## [12. Theoretical Perspectives on Data Quality and Synergistic Effects in Pre- and Post-Training Reasoning Models](https://arxiv.org/abs/2603.01293v1)

**作者**：Adel Javanmard, Baharan Mirzasoleiman, Vahab Mirrokni  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-03-01

### 📄 论文摘要

Large Language Models (LLMs) are pretrained on massive datasets and later instruction-tuned via supervised fine-tuning (SFT) or reinforcement learning (RL). Best practices emphasize large, diverse pretraining data, whereas post-training operates differently: SFT relies on smaller, high-quality datasets, while RL benefits more from scale, with larger amounts of feedback often outweighing label quality. Yet it remains unclear why pretraining and RL require large datasets, why SFT excels on smaller ones, and what defines high-quality SFT data. In this work, we theoretically analyze transformers trained on an in-context weight prediction task for linear regression. Our analysis reveals several key findings: $(i)$ balanced pretraining data can induce latent capabilities later activated during post-training, and $(ii)$ SFT learns best from a small set of examples challenging for the pretrained model, while excessively large SFT datasets may dilute informative pretraining signals. In contrast, RL is most effective on large-scale data that is not overly difficult for the pretrained model. We validate these theoretical insights with experiments on large nonlinear transformer architectures.

### 🤖 AI 总结

**一句话总结**：论文从理论上解释了为何预训练与RL更依赖大规模数据，而SFT更适合小而“刁钻”的高质量数据，并揭示预训练与后训练的协同机制。

**研究动机**：现有经验表明：预训练需要大而杂数据、SFT偏好小而精数据、RL更吃数据规模，但这些现象背后的原因及“高质量SFT数据”的定义并不清晰。作者希望给出统一的理论解释，并明确不同阶段数据规模与难度的最优匹配关系。

**核心方法**：在可解析的设定下，分析Transformer在“上下文中权重预测”的线性回归任务上的学习动态，推导预训练数据分布（是否平衡）、SFT样本难度与数量、以及RL反馈规模对能力激活/迁移的影响。并用更大、更非线性的Transformer实证验证这些理论预测。

**主要结论**：平衡的预训练数据能诱导潜在能力并在后训练中被激活；SFT最有效的数据是少量但对预训练模型具有挑战性的样本，过大的SFT会稀释预训练信号；相对地，RL在大规模且不过分困难的数据上收益最大，规模往往比单条反馈质量更关键。

**关键词**：数据质量, 预训练数据均衡, 后训练, 监督微调（SFT）, 强化学习后训练（RLHF）, 数据规模效应, 潜在能力激活, 预训练-后训练协同, 困难样本选择, 上下文学习（ICL）, 线性回归权重预测任务

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01293v1) | [下载PDF](https://arxiv.org/pdf/2603.01293v1.pdf)

---

## [13. Integrating LTL Constraints into PPO for Safe Reinforcement Learning](https://arxiv.org/abs/2603.01292v1)

**作者**：Maifang Zhang, Hang Yu, Qian Zuo 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.LO, cs.RO  
**发布时间**：2026-03-01

### 📄 论文摘要

This paper proposes Proximal Policy Optimization with Linear Temporal Logic Constraints (PPO-LTL), a framework that integrates safety constraints written in LTL into PPO for safe reinforcement learning. LTL constraints offer rigorous representations of complex safety requirements, such as regulations that broadly exist in robotics, enabling systematic monitoring of safety requirements. Violations against LTL constraints are monitored by limit-deterministic Büchi automata, and then translated by a logic-to-cost mechanism into penalty signals. The signals are further employed for guiding the policy optimization via the Lagrangian scheme. Extensive experiments on the Zones and CARLA environments show that our PPO-LTL can consistently reduce safety violations, while maintaining competitive performance, against the state-of-the-art methods. The code is at https://github.com/EVIEHub/PPO-LTL.

### 🤖 AI 总结

**一句话总结**：提出PPO-LTL，将线性时序逻辑（LTL）形式化安全约束集成进PPO，通过自动机监控与拉格朗日优化在保证性能的同时显著降低安全违规。

**研究动机**：现实机器人/自动驾驶等任务的安全规则往往复杂且时序相关，难以用简单奖励塑形精确表达；需要一种可严格刻画并可在线监控的约束机制来指导安全强化学习。

**核心方法**：将LTL约束编译为限制确定性Büchi自动机（LDBA）用于检测违规轨迹，并通过“逻辑到代价（logic-to-cost）”把违规程度转为惩罚信号；再用拉格朗日乘子框架把惩罚作为约束项融入PPO更新，实现性能-安全的自适应权衡。

**主要结论**：在Zones与CARLA实验中，PPO-LTL相较SOTA方法能更稳定地减少LTL定义的安全违规，同时保持具有竞争力的任务回报/性能，验证了该集成框架的有效性与通用性。

**关键词**：安全强化学习, 约束强化学习, 线性时序逻辑（LTL）约束, 形式化安全约束, 逻辑到代价映射, 拉格朗日约束优化, 惩罚信号塑形, 安全违规监测

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01292v1) | [下载PDF](https://arxiv.org/pdf/2603.01292v1.pdf)

---

## [14. JailNewsBench: Multi-Lingual and Regional Benchmark for Fake News Generation under Jailbreak Attacks](https://arxiv.org/abs/2603.01291v1)

**作者**：Masahiro Kaneko, Ayana Niwa, Timothy Baldwin  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-03-01

### 📄 论文摘要

Fake news undermines societal trust and decision-making across politics, economics, health, and international relations, and in extreme cases threatens human lives and societal safety. Because fake news reflects region-specific political, social, and cultural contexts and is expressed in language, evaluating the risks of large language models (LLMs) requires a multi-lingual and regional perspective. Malicious users can bypass safeguards through jailbreak attacks, inducing LLMs to generate fake news. However, no benchmark currently exists to systematically assess attack resilience across languages and regions. Here, we propose JailNewsBench, the first benchmark for evaluating LLM robustness against jailbreak-induced fake news generation. JailNewsBench spans 34 regions and 22 languages, covering 8 evaluation sub-metrics through LLM-as-a-Judge and 5 jailbreak attacks, with approximately 300k instances. Our evaluation of 9 LLMs reveals that the maximum attack success rate (ASR) reached 86.3% and the maximum harmfulness score was 3.5 out of 5. Notably, for English and U.S.-related topics, the defensive performance of typical multi-lingual LLMs was significantly lower than for other regions, highlighting substantial imbalances in safety across languages and regions. In addition, our analysis shows that coverage of fake news in existing safety datasets is limited and less well defended than major categories such as toxicity and social bias. Our dataset and code are available at https://github.com/kanekomasahiro/jail_news_bench.

### 🤖 AI 总结

**一句话总结**：JailNewsBench 是一个覆盖22种语言、34个地区的基准，用于系统评估LLM在越狱攻击下生成虚假新闻的风险与防御鲁棒性。

**研究动机**：虚假新闻具有强烈的地区与语言依赖性，而现有评测缺乏跨语言/跨地区维度，难以衡量LLM在越狱攻击诱导下生成虚假新闻的真实安全风险。

**核心方法**：构建约30万实例的 JailNewsBench，涵盖5类越狱攻击，并用LLM-as-a-Judge 从8个子指标评估生成内容的攻击成功率、危害性等，对9个LLM进行系统对比测试。

**主要结论**：在部分设置下ASR最高达86.3%、危害性最高3.5/5，且多语种LLM在英语与美国相关主题上的防御显著更弱，暴露出跨语言/地区安全能力不均衡；同时现有安全数据集中对“虚假新闻”覆盖不足且防御弱于毒性、偏见等主流安全类别。

**关键词**：假新闻生成, 越狱攻击, LLM安全评测, 鲁棒性基准, 多语言安全, 跨地区风险评估, 有害性评分, 攻击成功率, 安全数据集覆盖

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01291v1) | [下载PDF](https://arxiv.org/pdf/2603.01291v1.pdf)

---

## [15. Attention Smoothing Is All You Need For Unlearning](https://arxiv.org/abs/2603.01285v1)

**作者**：Saleh Zare Zade, Xiangyu Zhou, Sijia Liu 等 4 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-03-01

### 📄 论文摘要

Large Language Models are prone to memorizing sensitive, copyrighted, or hazardous content, posing significant privacy and legal concerns. Retraining from scratch is computationally infeasible, whereas current unlearning methods exhibit unstable trade-offs between forgetting and utility, frequently producing incoherent outputs on forget prompts and failing to generalize due to the persistence of lexical-level and semantic-level associations in attention. We propose Attention Smoothing Unlearning (ASU), a principled framework that casts unlearning as self-distillation from a forget-teacher derived from the model's own attention. By increasing the softmax temperature, ASU flattens attention distributions and directly suppresses the lexical-level and semantic-level associations responsible for reconstructing memorized knowledge. This results in a bounded optimization objective that erases factual information yet maintains coherence in responses to forget prompts. Empirical evaluation on TOFU, MUSE, and WMDP, along with real-world and continual unlearning scenarios across question answering and text completion, demonstrates that ASU outperforms the baselines for most unlearning scenarios, delivering robust unlearning with minimal loss of model utility.

### 🤖 AI 总结

**一句话总结**：提出注意力平滑遗忘（ASU），通过“升温”软化注意力分布来抑制记忆重建相关的词汇/语义关联，从而实现更稳健的模型遗忘并尽量保持效用。

**研究动机**：大模型会记忆敏感或受版权保护内容，完全重训成本过高；现有遗忘方法在“遗忘-效用”之间权衡不稳定，且在遗忘提示上易不连贯、泛化差，根源在于注意力中持续存在的词汇级与语义级关联。

**核心方法**：将遗忘表述为一种自蒸馏：用模型自身注意力构造“forget-teacher”，并通过提高softmax温度使注意力分布更平坦（attention smoothing），直接削弱触发记忆重建的关联，同时得到有界的优化目标以维持遗忘提示下的输出连贯性。

**主要结论**：在TOFU、MUSE、WMDP以及真实/持续遗忘与QA、补全等任务上，ASU多数场景优于基线方法，能更可靠地消除特定事实记忆，并以较小的模型效用损失维持整体表现。

**关键词**：模型遗忘, LLM 隐私合规, 敏感信息记忆, 注意力平滑, 注意力分布平坦化, 自蒸馏, 忘却教师, 事实知识擦除, 持续遗忘

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2603.01285v1) | [下载PDF](https://arxiv.org/pdf/2603.01285v1.pdf)

---

