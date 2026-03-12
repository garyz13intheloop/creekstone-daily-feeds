# arXiv AI 论文日报 | 2026-03-12

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (16 篇)
- [cs.CL](#csCL) (2 篇)
- [cs.AI](#csAI) (1 篇)

---

## cs.AI

## [1. A Hybrid Knowledge-Grounded Framework for Safety and Traceability in Prescription Verification](https://arxiv.org/abs/2603.10891v1)

**作者**：Yichi Zhu, Kan Ling, Xu Liu 等 6 位作者  
**分类**：cs.AI, cs.IR  
**发布时间**：2026-03-11

### 📄 论文摘要

Medication errors pose a significant threat to patient safety, making pharmacist verification (PV) a critical, yet heavily burdened, final safeguard. The direct application of Large Language Models (LLMs) to this zero-tolerance domain is untenable due to their inherent factual unreliability, lack of traceability, and weakness in complex reasoning. To address these challenges, we introduce PharmGraph-Auditor, a novel system designed for safe and evidence-grounded prescription auditing. The core of our system is a trustworthy Hybrid Pharmaceutical Knowledge Base (HPKB), implemented under the Virtual Knowledge Graph (VKG) paradigm. This architecture strategically unifies a relational component for set constraint satisfaction and a graph component for topological reasoning via a rigorous mapping layer. To construct this HPKB, we propose the Iterative Schema Refinement (ISR) algorithm, a framework that enables the co-evolution of both graph and relational schemas from medical texts. For auditing, we introduce the KB-grounded Chain of Verification (CoV), a new reasoning paradigm that transforms the LLM from an unreliable generator into a transparent reasoning engine. CoV decomposes the audit task into a sequence of verifiable queries against the HPKB, generating hybrid query plans to retrieve evidence from the most appropriate data store. Experimental results demonstrate robust knowledge extraction capabilities and show promises of using PharmGraph-Auditor to enable pharmacists to achieve safer and faster prescription verification.

### 🤖 AI 总结

**一句话总结**：论文提出 PharmGraph-Auditor：以混合药学知识库为核心，用可验证的查询链替代“直接让LLM生成结论”，实现更安全、可追溯的处方审核。

**研究动机**：处方审核是零容错场景，但LLM存在事实不可靠、缺乏可追溯证据与复杂推理薄弱的问题，直接应用风险过高；同时药学知识需要既支持约束校验又支持图结构推理。

**核心方法**：构建基于VKG范式的混合药学知识库HPKB（关系型用于集合/约束满足，图用于拓扑推理），并用ISR迭代模式精炼算法从医疗文本中协同演化关系与图的schema；审核阶段提出KB-grounded的CoV（Chain of Verification），将任务分解为一串可验证的HPKB查询并生成混合查询计划以检索证据。

**主要结论**：实验显示该框架具备稳健的知识抽取能力，且通过CoV将LLM定位为透明推理引擎而非不可靠生成器，有望帮助药师在保证安全与可追溯的前提下更快完成处方核验。

**关键词**：处方审核, 可追溯推理, 知识库增强推理, 虚拟知识图谱（VKG）, 混合知识库（图-关系）, 约束满足, 拓扑推理, 迭代式模式精炼, 混合查询规划, 可验证查询链（CoV）, 医学文本知识抽取

**评分**：50

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10891v1) | [下载PDF](https://arxiv.org/pdf/2603.10891v1.pdf)

---

## cs.CL

## [2. Instruction set for the representation of graphs](https://arxiv.org/abs/2603.11039v1)

**作者**：Ezequiel Lopez-Rubio, Mario Pascual-Gonzalez  
**分类**：cs.CL, cs.AI, cs.DS  
**发布时间**：2026-03-11

### 📄 论文摘要

We present IsalGraph, a method for representing the structure of any finite, simple graph as a compact string over a nine-character instruction alphabet. The encoding is executed by a small virtual machine comprising a sparse graph, a circular doubly-linked list (CDLL) of graph-node references, and two traversal pointers. Instructions either move a pointer through the CDLL or insert a node or edge into the graph. A key design property is that every string over the alphabet decodes to a valid graph, with no invalid states reachable. A greedy \emph{GraphToString} algorithm encodes any connected graph into a string in time polynomial in the number of nodes; an exhaustive-backtracking variant produces a canonical string by selecting the lexicographically smallest shortest string across all starting nodes and all valid traversal orders. We evaluate the representation on five real-world graph benchmark datasets (IAM Letter LOW/MED/HIGH, LINUX, and AIDS) and show that the Levenshtein distance between IsalGraph strings correlates strongly with graph edit distance (GED). Together, these properties make IsalGraph strings a compact, isomorphism-invariant, and language-model-compatible sequential encoding of graph structure, with direct applications in graph similarity search, graph generation, and graph-conditioned language modelling

### 🤖 AI 总结

**一句话总结**：提出IsalGraph：用9字符指令集把任意有限简单图编码为紧凑字符串，且该字符串可作为同构不变、适配语言模型的图结构序列表示。

**研究动机**：现有图表示往往难以直接用于序列模型且不天然保证同构不变与解码有效性；需要一种既紧凑又能让任意字符串都对应合法图、并支持相似度度量的通用编码。

**核心方法**：设计一个小型虚拟机（稀疏图+循环双向链表CDLL+两个遍历指针），用指令移动指针或插入节点/边，保证“任意指令串→有效图”且无非法状态；提出贪心GraphToString多项式时间编码连通图，并用穷举回溯在不同起点/遍历序中选取字典序最小的最短串作为规范（canonical）表示。

**主要结论**：在多个真实图数据集上，IsalGraph字符串的Levenshtein距离与图编辑距离（GED）强相关，表明该序列表示既紧凑又能反映结构相似性；因此可用于图相似检索、图生成与图条件语言建模等应用。

**关键词**：指令式图编码, 图到字符串表示, 序列化图结构表示, 九字符指令字母表, 虚拟机解码器, 典范字符串编码, 图同构不变表示, 图相似度检索, 图编辑距离（GED）, 图条件语言建模

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.11039v1) | [下载PDF](https://arxiv.org/pdf/2603.11039v1.pdf)

---

## [3. Beyond the Illusion of Consensus: From Surface Heuristics to Knowledge-Grounded Evaluation in LLM-as-a-Judge](https://arxiv.org/abs/2603.11027v1)

**作者**：Mingyang Song, Mao Zheng, Chenning Xu  
**分类**：cs.CL  
**发布时间**：2026-03-11

### 📄 论文摘要

The paradigm of LLM-as-a-judge relies on a critical assumption, namely that high inter-evaluator agreement indicates reliable and objective evaluation. We present two complementary findings that challenge this assumption. \textbf{First}, we demonstrate that this consensus is frequently illusory. We identify and formalize \textbf{Evaluation Illusion}, a phenomenon where LLM judges generate sophisticated critiques yet anchor scores on shared surface heuristics rather than substantive quality. Through a large-scale study of 105,600 evaluation instances (32 LLMs $\times$ 3 frontier judges $\times$ 100 tasks $\times$ 11 temperatures), we show that model-level agreement (Spearman $ρ= 0.99$) masks fragile sample-level agreement (Pearson $\bar{r} = 0.72$; absolute agreement ICC $= 0.67$), that merely sharing rubric structure restores 62\% of total agreement, and that high-quality outputs paradoxically receive the \textit{least} consistent evaluations. \textbf{Second}, we demonstrate that dynamically generating evaluation rubrics grounded in domain knowledge produces more meaningful assessment. We introduce MERG (Metacognitive Enhanced Rubric Generation), a knowledge-driven rubric generation framework whose domain-selective effects confirm this. Agreement \textit{increases} in codified domains (Education +22\%, Academic +27\%) where knowledge anchors evaluators on shared standards, while it decreases in subjective domains where genuine evaluative pluralism emerges. These findings suggest that evaluation rubrics should be dynamically enriched with expert knowledge rather than relying on generic criteria, with implications for reward modeling in RLAIF.

### 🤖 AI 总结

**一句话总结**：论文指出LLM-as-a-judge中的高一致性常是“表面启发式”导致的评价幻觉，并提出用领域知识动态生成量表（MERG）来获得更有意义、与领域标准对齐的评估。

**研究动机**：现有范式常把评审间高一致性当作客观可靠的证据，但作者怀疑这种一致性可能并不反映真实质量判断，进而影响评测与RLAIF等训练信号的可信度。

**核心方法**：作者提出并形式化“Evaluation Illusion”，在105,600个评估实例（32模型×3前沿裁判×100任务×11温度）上分解模型级与样本级一致性，并分析共享rubric结构对一致性的贡献；同时提出MERG（Metacognitive Enhanced Rubric Generation），以领域知识为依据动态生成评价rubric，比较其在不同领域对一致性与评价行为的影响。

**主要结论**：模型级一致性极高（ρ=0.99）可能掩盖样本级一致性脆弱（平均r=0.72，ICC=0.67），且仅共享rubric结构就能恢复约62%一致性，说明评分常锚定在表面启发式而非实质质量；MERG在知识更“可编码”的领域提升一致性（教育+22%、学术+27%），在主观领域则降低一致性、呈现真实多元评判，提示应以专家知识动态充实rubric而非依赖通用标准。

**关键词**：评测一致性幻觉, 表层启发式, 知识支撑评测, 动态评分量表生成, 元认知增强, 跨评审一致性指标, 领域知识锚定, 主观域评测多元性, 评测可靠性

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2603.11027v1) | [下载PDF](https://arxiv.org/pdf/2603.11027v1.pdf)

---

## cs.CV

## [4. COMIC: Agentic Sketch Comedy Generation](https://arxiv.org/abs/2603.11048v1)

**作者**：Susung Hong, Brian Curless, Ira Kemelmacher-Shlizerman 等 4 位作者  
**分类**：cs.CV, cs.AI, cs.CL, cs.MA, cs.NE  
**发布时间**：2026-03-11

### 📄 论文摘要

We propose a fully automated AI system that produces short comedic videos similar to sketch shows such as Saturday Night Live. Starting with character references, the system employs a population of agents loosely based on real production studio roles, structured to optimize the quality and diversity of ideas and outputs through iterative competition, evaluation, and improvement. A key contribution is the introduction of LLM critics aligned with real viewer preferences through the analysis of a corpus of comedy videos on YouTube to automatically evaluate humor. Our experiments show that our framework produces results approaching the quality of professionally produced sketches while demonstrating state-of-the-art performance in video generation.

### 🤖 AI 总结

**一句话总结**：本文提出COMIC，一个由多智能体协作与竞争驱动的全自动系统，从角色参考出发生成接近专业水准的短喜剧小品视频，并通过贴近观众偏好的LLM评审自动衡量“好笑程度”。

**研究动机**：传统视频生成难以稳定产出“真正好笑且多样”的小品内容，而喜剧质量评估主观性强、缺少可自动化对齐观众偏好的评价机制。作者希望用生产工作室式的分工流程与数据驱动的“笑点评审”来提升生成质量与迭代效率。

**核心方法**：系统以多智能体群体模拟编剧/导演/剪辑等制作角色，通过迭代的创意提出—竞争—评价—改进来优化脚本与视频输出的质量与多样性。关键在于构建LLM critics：基于YouTube喜剧视频语料分析，将评审器与真实观众偏好对齐，用于自动打分与筛选/引导后续迭代。

**主要结论**：实验表明，该框架生成的小品质量接近专业制作，并在视频生成上达到/接近当时的SOTA表现。对齐观众偏好的LLM评审与多智能体迭代机制共同提升了幽默性评估的可用性与整体输出质量。

**关键词**：短视频小品生成, 多智能体协作生成, 角色条件生成, 迭代式竞争优化, 偏好对齐评测, 幽默自动评价, 观众偏好建模, 视频生成模型, 创意多样性优化

**评分**：47

**论文链接**：[查看原文](https://arxiv.org/abs/2603.11048v1) | [下载PDF](https://arxiv.org/pdf/2603.11048v1.pdf)

---

## [5. V2M-Zero: Zero-Pair Time-Aligned Video-to-Music Generation](https://arxiv.org/abs/2603.11042v1)

**作者**：Yan-Bo Lin, Jonah Casebeer, Long Mai 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.LG, cs.MM, cs.SD  
**发布时间**：2026-03-11

### 📄 论文摘要

Generating music that temporally aligns with video events is challenging for existing text-to-music models, which lack fine-grained temporal control. We introduce V2M-Zero, a zero-pair video-to-music generation approach that outputs time-aligned music for video. Our method is motivated by a key observation: temporal synchronization requires matching when and how much change occurs, not what changes. While musical and visual events differ semantically, they exhibit shared temporal structure that can be captured independently within each modality. We capture this structure through event curves computed from intra-modal similarity using pretrained music and video encoders. By measuring temporal change within each modality independently, these curves provide comparable representations across modalities. This enables a simple training strategy: fine-tune a text-to-music model on music-event curves, then substitute video-event curves at inference without cross-modal training or paired data. Across OES-Pub, MovieGenBench-Music, and AIST++, V2M-Zero achieves substantial gains over paired-data baselines: 5-21% higher audio quality, 13-15% better semantic alignment, 21-52% improved temporal synchronization, and 28% higher beat alignment on dance videos. We find similar results via a large crowd-source subjective listening test. Overall, our results validate that temporal alignment through within-modality features, rather than paired cross-modal supervision, is effective for video-to-music generation. Results are available at https://genjib.github.io/v2m_zero/

### 🤖 AI 总结

**一句话总结**：V2M-Zero 通过“事件曲线”刻画视频与音乐各自的时间变化结构，在无需视频-音乐配对数据与跨模态训练的情况下生成与视频事件时间对齐的音乐。

**研究动机**：现有文本到音乐模型缺乏细粒度时间控制，导致难以与视频事件同步；作者观察到时间同步关键在于“变化发生的时刻与幅度”，而非跨模态语义一致。

**核心方法**：分别用预训练视频/音乐编码器计算帧/片段的模态内相似度并生成事件曲线（反映时间变化强度），先用音乐事件曲线微调文本到音乐模型，再在推理时用视频事件曲线替换输入以实现零配对视频到音乐生成。

**主要结论**：在 OES-Pub、MovieGenBench-Music、AIST++ 上，V2M-Zero 在音质、语义对齐与时间同步等指标上显著优于使用配对数据的基线，并在人群主观听评中得到验证，表明仅依赖模态内时间结构即可有效实现视频-音乐时间对齐。

**关键词**：视频到音乐生成, 时间对齐生成, 时间同步, 细粒度时间控制, 零配对学习, 跨模态迁移推理, 模态内相似度, 事件曲线, 预训练编码器, 文本到音乐微调, 节拍对齐评测, 主观听评测试

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.11042v1) | [下载PDF](https://arxiv.org/pdf/2603.11042v1.pdf)

---

## [6. Does AI See like Art Historians? Interpreting How Vision Language Models Recognize Artistic Style](https://arxiv.org/abs/2603.11024v1)

**作者**：Marvin Limpijankit, Milad Alshomary, Yassin Oulad Daoud 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-11

### 📄 论文摘要

VLMs have become increasingly proficient at a range of computer vision tasks, such as visual question answering and object detection. This includes increasingly strong capabilities in the domain of art, from analyzing artwork to generation of art. In an interdisciplinary collaboration between computer scientists and art historians, we characterize the mechanisms underlying VLMs' ability to predict artistic style and assess the extent to which they align with the criteria art historians use to reason about artistic style. We employ a latent-space decomposition approach to identify concepts that drive art style prediction and conduct quantitative evaluations, causal analysis and assessment by art historians. Our findings indicate that 73% of the extracted concepts are judged by art historians to exhibit a coherent and semantically meaningful visual feature and 90% of concepts used to predict style of a given artwork were judged relevant. In cases where an irrelevant concept was used to successfully predict style, art historians identified possible reasons for its success; for example, the model might "understand" a concept in more formal terms, such as dark/light contrasts.

### 🤖 AI 总结

**一句话总结**：论文通过可解释性分解方法揭示视觉-语言模型（VLM）预测艺术风格时依赖的潜在视觉概念，并验证其与艺术史学者风格判断标准在多数情况下具有一致性。

**研究动机**：尽管VLM在艺术风格识别上表现强，但其“为何能判别风格”及是否使用了与艺术史学者相近的依据仍不清楚。作者希望用跨学科评估检验模型内部机制与人类专家推理标准的对齐程度。

**核心方法**：采用潜在空间分解（latent-space decomposition）提取驱动风格预测的概念，并结合定量评测与因果分析来验证这些概念对预测的贡献。随后邀请艺术史学者对概念的语义连贯性与对具体作品风格判断的相关性进行人工评估。

**主要结论**：艺术史学者认为提取概念中有73%呈现连贯且有语义的视觉特征，且在对单幅作品进行风格预测时，模型使用的概念有90%被判定为相关。对于少数“看似无关却有效”的概念，专家指出模型可能以更形式化的方式编码风格线索（如明暗对比）从而仍能成功预测。

**关键词**：视觉语言模型, 艺术风格识别, 模型可解释性, 潜在空间分解, 概念抽取, 概念一致性评估, 人类专家评审, 因果分析, 风格预测驱动因素, 形式特征对齐

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.11024v1) | [下载PDF](https://arxiv.org/pdf/2603.11024v1.pdf)

---

## [7. Too Vivid to Be Real? Benchmarking and Calibrating Generative Color Fidelity](https://arxiv.org/abs/2603.10990v1)

**作者**：Zhengyao Fang, Zexi Jia, Yijia Zhong 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-11

### 📄 论文摘要

Recent advances in text-to-image (T2I) generation have greatly improved visual quality, yet producing images that appear visually authentic to real-world photography remains challenging. This is partly due to biases in existing evaluation paradigms: human ratings and preference-trained metrics often favor visually vivid images with exaggerated saturation and contrast, which make generations often too vivid to be real even when prompted for realistic-style images. To address this issue, we present Color Fidelity Dataset (CFD) and Color Fidelity Metric (CFM) for objective evaluation of color fidelity in realistic-style generations. CFD contains over 1.3M real and synthetic images with ordered levels of color realism, while CFM employs a multimodal encoder to learn perceptual color fidelity. In addition, we propose a training-free Color Fidelity Refinement (CFR) that adaptively modulates spatial-temporal guidance scale in generation, thereby enhancing color authenticity. Together, CFD supports CFM for assessment, whose learned attention further guides CFR to refine T2I fidelity, forming a progressive framework for assessing and improving color fidelity in realistic-style T2I generation. The dataset and code are available at https://github.com/ZhengyaoFang/CFM.

### 🤖 AI 总结

**一句话总结**：论文提出用于“真实风格”文生图的颜色真实感评测与校准框架：数据集CFD、指标CFM以及无需训练的生成期修正方法CFR，以缓解生成图像“过于鲜艳不真实”的问题。

**研究动机**：现有主观打分与偏好训练指标往往偏爱高饱和/高对比的“讨喜”图像，导致即便提示词要求写实，模型也常生成“太艳而不像真实摄影”的结果，需要更客观的颜色真实度评估与改进手段。

**核心方法**：构建包含130万+真实与合成图像、并具备颜色真实度有序等级的Color Fidelity Dataset（CFD），训练基于多模态编码器的Color Fidelity Metric（CFM）来学习感知层面的颜色真实度；同时提出训练无关的Color Fidelity Refinement（CFR），在生成过程中自适应调制时空（spatial-temporal）guidance scale，并利用CFM的注意力引导进行颜色校正。

**主要结论**：CFD+CFM能够更客观地区分并量化写实生成中的颜色真实度偏差，而CFR可在不额外训练的情况下提升生成结果的颜色真实性；三者形成从评测到改进的渐进式闭环框架，降低“过度鲜艳”带来的不真实感。

**关键词**：文生图生成, 真实感摄影, 颜色保真度, 颜色真实度评测, 生成图像评估偏差, 颜色保真数据集, 多模态编码器, 感知度量学习, 训练无关优化, 引导尺度调节, 时空引导

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10990v1) | [下载PDF](https://arxiv.org/pdf/2603.10990v1.pdf)

---

## [8. GroundCount: Grounding Vision-Language Models with Object Detection for Mitigating Counting Hallucinations](https://arxiv.org/abs/2603.10978v1)

**作者**：Boyuan Chen, Minghao Shao, Siddharth Garg 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-11

### 📄 论文摘要

Vision Language Models (VLMs) exhibit persistent hallucinations in counting tasks, with accuracy substantially lower than other visual reasoning tasks (excluding sentiment). This phenomenon persists even in state-of-the-art reasoning-capable VLMs. Conversely, CNN-based object detection models (ODMs) such as YOLO excel at spatial localization and instance counting with minimal computational overhead. We propose GroundCount, a framework that augments VLMs with explicit spatial grounding from ODMs to mitigate counting hallucinations. In the best case, our prompt-based augmentation strategy achieves 81.3% counting accuracy on the best-performing model (Ovis2.5-2B) - a 6.6pp improvement - while reducing inference time by 22% through elimination of hallucination-driven reasoning loops for stronger models. We conduct comprehensive ablation studies demonstrating that positional encoding is a critical component, being beneficial for stronger models but detrimental for weaker ones. Confidence scores, by contrast, introduce noise for most architectures and their removal improves performance in four of five evaluated models. We further evaluate feature-level fusion architectures, finding that explicit symbolic grounding via structured prompts outperforms implicit feature fusion despite sophisticated cross-attention mechanisms. Our approach yields consistent improvements across four of five evaluated VLM architectures (6.2--7.5pp), with one architecture exhibiting degraded performance due to incompatibility between its iterative reflection mechanisms and structured prompts. These results suggest that counting failures stem from fundamental spatial-semantic integration limitations rather than architecture-specific deficiencies, while highlighting the importance of architectural compatibility in augmentation strategies.

### 🤖 AI 总结

**一句话总结**：GroundCount通过引入目标检测模型提供的显式空间定位信息来增强VLM，从而显著缓解计数任务中的幻觉并提升准确率与推理效率。

**研究动机**：VLM在计数任务上长期存在严重幻觉与低准确率，即便是具备推理能力的SOTA模型也难以避免；而YOLO等目标检测模型在实例定位与计数上更可靠且开销更低。

**核心方法**：提出GroundCount框架：先用ODM提取物体框/位置等空间证据，再用结构化提示（符号化grounding，可含位置编码等）将其注入VLM以约束计数；并对位置编码、置信度等组件做消融，同时对比提示式显式融合与特征级跨注意力融合。

**主要结论**：在5种VLM中有4种获得稳定提升（约+6.2～7.5pp），最佳在Ovis2.5-2B上达81.3%（+6.6pp）且因减少“幻觉驱动的推理循环”推理时间降低22%；位置编码对强模型更有效但对弱模型有害，置信度多引入噪声，而显式结构化提示普遍优于特征融合，且增强策略需与模型反思/迭代机制兼容。

**关键词**：视觉语言模型, 计数幻觉, 视觉计数, 目标检测, 空间定位, 显式空间对齐, 结构化提示, 符号化对齐, 位置编码, 特征级融合, 跨注意力机制, 推理效率优化

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10978v1) | [下载PDF](https://arxiv.org/pdf/2603.10978v1.pdf)

---

## [9. Med-DualLoRA: Local Adaptation of Foundation Models for 3D Cardiac MRI](https://arxiv.org/abs/2603.10967v1)

**作者**：Joan Perramon-Llussà, Amelia Jiménez-Sánchez, Grzegorz Skorupko 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-11

### 📄 论文摘要

Foundation models (FMs) show great promise for robust downstream performance across medical imaging tasks and modalities, including cardiac magnetic resonance (CMR), following task-specific adaptation. However, adaptation using single-site data may lead to suboptimal performance and increased model bias, while centralized fine-tuning on clinical data is often infeasible due to privacy constraints. Federated fine-tuning offers a privacy-preserving alternative; yet conventional approaches struggle under heterogeneous, non-IID multi-center data and incur substantial communication overhead when adapting large models. In this work, we study federated FM fine-tuning for 3D CMR disease detection and propose Med-DualLoRA, a client-aware parameter-efficient fine-tuning (PEFT) federated framework that disentangles globally shared and local low-rank adaptations (LoRA) through additive decomposition. Global and local LoRA modules are trained locally, but only the global component is shared and aggregated across sites, keeping local adapters private. This design improves personalization while significantly reducing communication cost, and experiments show that adapting only two transformer blocks preserves performance while further improving efficiency. We evaluate our method on a multi-center state-of-the-art cine 3D CMR FM fine-tuned for disease detection using ACDC and combined M\&Ms datasets, treating each vendor as a federated client. Med-DualLoRA achieves statistically significant improved performance (balanced accuracy 0.768, specificity 0.612) compared to other federated PEFT baselines, while maintaining communication efficiency. Our approach provides a scalable solution for local federated adaptation of medical FMs under realistic clinical constraints.

### 🤖 AI 总结

**一句话总结**：Med-DualLoRA通过在联邦学习中解耦“全局共享+本地私有”的LoRA适配，实现3D心脏MRI基础模型在多中心非IID数据下的高效个性化微调与更低通信开销。

**研究动机**：单中心适配易产生偏差且泛化不足，而集中式微调受隐私限制难以落地；传统联邦微调在多中心异质数据上效果不稳且对大模型通信成本高。

**核心方法**：提出客户端感知的PEFT联邦框架Med-DualLoRA，将LoRA更新做加性分解为全局LoRA与本地LoRA：两者都在本地训练，但仅上传聚合全局部分、本地适配器留在站点私有以增强个性化并降通信；并验证只适配少量（如两个）Transformer块即可保持性能并进一步提效。

**主要结论**：在以不同厂商作为联邦客户端的多中心cine 3D CMR疾病检测任务（ACDC+M&Ms）上，Med-DualLoRA相较其他联邦PEFT基线取得显著更优表现（如balanced accuracy 0.768、specificity 0.612）且通信更高效，显示其适用于真实临床约束下的可扩展本地联邦适配。

**关键词**：联邦微调, 参数高效微调, 全局-本地适配器解耦, 非IID多中心数据, 隐私保护训练, 通信开销降低, 个性化模型适配, 疾病检测, 医学基础模型适配

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10967v1) | [下载PDF](https://arxiv.org/pdf/2603.10967v1.pdf)

---

## [10. Contrastive learning-based video quality assessment-jointed video vision transformer for video recognition](https://arxiv.org/abs/2603.10965v1)

**作者**：Jian Sun, Mohammad H. Mahoor  
**分类**：cs.CV  
**发布时间**：2026-03-11

### 📄 论文摘要

Video quality significantly affects video classification. We found this problem when we classified Mild Cognitive Impairment well from clear videos, but worse from blurred ones. From then, we realized that referring to Video Quality Assessment (VQA) may improve video classification. This paper proposed Self-Supervised Learning-based Video Vision Transformer combined with No-reference VQA for video classification (SSL-V3) to fulfill the goal. SSL-V3 leverages Combined-SSL mechanism to join VQA into video classification and address the label shortage of VQA, which commonly occurs in video datasets, making it impossible to provide an accurate Video Quality Score. In brief, Combined-SSL takes video quality score as a factor to directly tune the feature map of the video classification. Then, the score, as an intersected point, links VQA and classification, using the supervised classification task to tune the parameters of VQA. SSL-V3 achieved robust experimental results on two datasets. For example, it reached an accuracy of 94.87% on some interview videos in the I-CONECT (a facial video-involved healthcare dataset), verifying SSL-V3's effectiveness.

### 🤖 AI 总结

**一句话总结**：提出SSL-V3，将无参考视频质量评估（VQA）与视频Vision Transformer分类通过对比/自监督机制联合训练，以提升模糊等低质量视频上的分类鲁棒性。

**研究动机**：作者观察到视频清晰度显著影响分类效果（清晰视频能更好识别MCI而模糊视频变差），因此希望把VQA信息引入分类以缓解质量退化带来的性能下降，同时解决VQA标注稀缺问题。

**核心方法**：SSL-V3采用“Combined-SSL”把视频质量分数作为因子直接调制分类特征图，并以该分数作为VQA与分类的连接点：用监督分类任务反向约束/优化VQA分支参数，从而在缺少VQA标签时仍能学习有效的质量感知表示。

**主要结论**：在两个数据集上取得稳健提升，例如在I-CONECT访谈视频上达到94.87%准确率，表明将VQA与视频Transformer分类联合学习能增强对视频质量变化（如模糊）的适应性并提升整体识别性能。

**关键词**：视频质量评估, 无参考视频质量评估, 视频分类, 视频识别, 自监督学习, 质量引导特征调制, 联合训练, 标签稀缺, 轻度认知障碍检测

**评分**：16

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10965v1) | [下载PDF](https://arxiv.org/pdf/2603.10965v1.pdf)

---

## [11. Bridging the Skill Gap in Clinical CBCT Interpretation with CBCTRepD](https://arxiv.org/abs/2603.10933v1)

**作者**：Qinxin Wu, Fucheng Niu, Hengchuan Zhu 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-11

### 📄 论文摘要

Generative AI has advanced rapidly in medical report generation; however, its application to oral and maxillofacial CBCT reporting remains limited, largely because of the scarcity of high-quality paired CBCT-report data and the intrinsic complexity of volumetric CBCT interpretation. To address this, we introduce CBCTRepD, a bilingual oral and maxillofacial CBCT report-generation system designed for integration into routine radiologist-AI co-authoring workflows. We curated a large-scale, high-quality paired CBCT-report dataset comprising approximately 7,408 studies, covering 55 oral disease entities across diverse acquisition settings, and used it to develop the system. We further established a clinically grounded, multi-level evaluation framework that assesses both direct AI-generated drafts and radiologist-edited collaboration reports using automatic metrics together with radiologist- and clinician-centered evaluation. Using this framework, we show that CBCTRepD achieves superior report-generation performance and produces drafts with writing quality and standardization comparable to those of intermediate radiologists. More importantly, in radiologist-AI collaboration, CBCTRepD provides consistent and clinically meaningful benefits across experience levels: it helps novice radiologists improve toward intermediate-level reporting, enables intermediate radiologists to approach senior-level performance, and even assists senior radiologists by reducing omission-related errors, including clinically important missed lesions. By improving report structure, reducing omissions, and promoting attention to co-existing lesions across anatomical regions, CBCTRepD shows strong and reliable potential as a practical assistant for real-world CBCT reporting across multi-level care settings.

### 🤖 AI 总结

**一句话总结**：提出并验证了CBCTRepD：一个基于大规模高质量配对数据训练的双语口颌面CBCT自动报告生成系统，可在放射科医师协作流程中显著提升报告质量并减少漏诊。

**研究动机**：口颌面CBCT报告生成应用受限于高质量“CBCT-报告”配对数据稀缺以及三维体数据解读复杂，导致现有生成式报告方法难以落地到临床常规书写与质控。

**核心方法**：构建约7,408例、覆盖55类口腔疾病实体且采集设置多样的高质量配对CBCT-报告数据集，并在此基础上开发可融入“医师-AI共同撰写/编辑”的双语报告生成系统CBCTRepD。提出临床导向的多层次评估框架，同时评测AI原始草稿与医师编辑后的协作报告，结合自动指标与放射科/临床医生人工评价。

**主要结论**：CBCTRepD在报告生成性能上优于对比方法，其草稿写作质量与规范性可达中级放射科医师水平；在人机协作中对不同资历医师均带来稳定收益（新手提升到中级、中级逼近高级、高级也能减少遗漏）。系统通过改进结构化表达、降低遗漏并促进跨解剖区域的共存病灶关注，显示出在真实多层级医疗场景部署的实用潜力。

**关键词**：锥形束CT, 口颌面影像, 医学报告生成, 影像-报告配对数据集, 双语报告, 放射科医师-AI协作, 共创式写作流程, 多层级临床评测框架, 报告标准化, 遗漏错误降低, 多病灶联合关注

**评分**：54

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10933v1) | [下载PDF](https://arxiv.org/pdf/2603.10933v1.pdf)

---

## [12. Lifelong Imitation Learning with Multimodal Latent Replay and Incremental Adjustment](https://arxiv.org/abs/2603.10929v1)

**作者**：Fanqi Yu, Matteo Tiezzi, Tommaso Apicella 等 5 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-03-11

### 📄 论文摘要

We introduce a lifelong imitation learning framework that enables continual policy refinement across sequential tasks under realistic memory and data constraints. Our approach departs from conventional experience replay by operating entirely in a multimodal latent space, where compact representations of visual, linguistic, and robot's state information are stored and reused to support future learning. To further stabilize adaptation, we introduce an incremental feature adjustment mechanism that regularizes the evolution of task embeddings through an angular margin constraint, preserving inter-task distinctiveness. Our method establishes a new state of the art in the LIBERO benchmarks, achieving 10-17 point gains in AUC and up to 65% less forgetting compared to previous leading methods. Ablation studies confirm the effectiveness of each component, showing consistent gains over alternative strategies. The code is available at: https://github.com/yfqi/lifelong_mlr_ifa.

### 🤖 AI 总结

**一句话总结**：提出一种在多模态潜空间进行“记忆回放+特征增量校准”的终身模仿学习框架，在LIBERO上显著提升AUC并减少遗忘。

**研究动机**：顺序任务的模仿学习在真实场景中受限于存储/数据预算，传统经验回放成本高且易遗忘；需要更紧凑且稳定的跨任务持续学习机制。

**核心方法**：将视觉-语言-机器人状态编码到多模态潜空间，仅存储紧凑潜变量用于后续重放训练；同时引入增量特征调整，通过带角度间隔的约束正则化任务嵌入演化，保持任务间区分度并稳定适应。

**主要结论**：在LIBERO基准上达到SOTA，相比先前方法AUC提升10–17点、遗忘降低最高65%；消融实验表明潜空间回放与角度间隔的增量调整均带来稳定且一致的性能增益。

**关键词**：终身模仿学习, 持续学习, 顺序任务学习, 灾难性遗忘抑制, 潜在回放, 多模态潜在空间, 多模态表征学习, 任务嵌入, 角度边距约束, 增量特征调整, 经验回放替代

**评分**：46

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10929v1) | [下载PDF](https://arxiv.org/pdf/2603.10929v1.pdf)

---

## [13. Novel Architecture of RPA In Oral Cancer Lesion Detection](https://arxiv.org/abs/2603.10928v1)

**作者**：Revana Magdy, Joy Naoum, Ali Hamdi  
**分类**：cs.CV  
**发布时间**：2026-03-11

### 📄 论文摘要

Accurate and early detection of oral cancer lesions is crucial for effective diagnosis and treatment. This study evaluates two RPA implementations, OC-RPAv1 and OC-RPAv2, using a test set of 31 images. OC-RPAv1 processes one image per prediction in an average of 0.29 seconds, while OCRPAv2 employs a Singleton design pattern and batch processing, reducing prediction time to just 0.06 seconds per image. This represents a 60-100x efficiency improvement over standard RPA methods, showcasing that design patterns and batch processing can enhance scalability and reduce costs in oral cancer detection

### 🤖 AI 总结

**一句话总结**：论文提出两种用于口腔癌病灶检测的RPA实现（OC-RPAv1/v2），通过Singleton设计模式与批处理将单张预测耗时降至0.06秒。

**研究动机**：口腔癌病灶需要更早、更快、更可扩展的检测流程以支持临床诊断与降低成本。传统RPA在处理效率与规模化部署上存在性能瓶颈，因此需要架构优化。

**核心方法**：在31张测试图像上对比评估OC-RPAv1与OC-RPAv2的预测速度：v1逐张处理；v2引入Singleton设计模式复用实例并采用batch processing进行批量推理。

**主要结论**：OC-RPAv2将平均预测时间从0.29秒/张降低到0.06秒/张，相比标准RPA方法宣称达到60–100倍效率提升，表明采用设计模式与批处理可显著增强口腔癌检测系统的可扩展性并降低计算成本。

**关键词**：口腔癌病灶检测, 医学图像分析, 计算机视觉, 区域提议算法（RPA）, 批处理推理, 单例模式, 推理加速, 低延迟推理, 吞吐量优化, 可扩展性, 计算成本降低

**评分**：15

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10928v1) | [下载PDF](https://arxiv.org/pdf/2603.10928v1.pdf)

---

## [14. S2D: Sparse to Dense Lifting for 3D Reconstruction with Minimal Inputs](https://arxiv.org/abs/2603.10893v1)

**作者**：Yuzhou Ji, Qijian Tian, He Zhu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-11

### 📄 论文摘要

Explicit 3D representations have already become an essential medium for 3D simulation and understanding. However, the most commonly used point cloud and 3D Gaussian Splatting (3DGS) each suffer from non-photorealistic rendering and significant degradation under sparse inputs. In this paper, we introduce Sparse to Dense lifting (S2D), a novel pipeline that bridges the two representations and achieves high-quality 3DGS reconstruction with minimal inputs. Specifically, the S2D lifting is two-fold. We first present an efficient one-step diffusion model that lifts sparse point cloud for high-fidelity image artifact fixing. Meanwhile, to reconstruct 3D consistent scenes, we also design a corresponding reconstruction strategy with random sample drop and weighted gradient for robust model fitting from sparse input views to dense novel views. Extensive experiments show that S2D achieves the best consistency in generating novel view guidance and first-tier sparse view reconstruction quality under different input sparsity. By reconstructing stable scenes with the least possible captures among existing methods, S2D enables minimal input requirements for 3DGS applications.

### 🤖 AI 总结

**一句话总结**：S2D提出从稀疏点云到稠密3D Gaussian Splatting的“稀疏到稠密”提升管线，在极少输入视角下仍能获得高质量、3D一致的重建与新视角渲染。

**研究动机**：点云与3DGS在稀疏输入时容易出现渲染不真实与质量显著退化，导致需要大量拍摄视角才能稳定重建；因此需要一种能在最少输入下仍保持一致性与细节的表示与训练策略。

**核心方法**：方法包含两部分：用高效一步扩散模型对稀疏点云进行图像伪影修复/提升以生成高保真新视角指导；并设计面向稀疏到稠密的重建训练策略（随机采样丢弃与加权梯度）以增强从少量输入视图拟合到稠密新视图的鲁棒性与3D一致性。

**主要结论**：实验表明S2D在不同稀疏度下的新视角指导一致性与稀疏视图重建质量均优于对比方法，并能以更少的拍摄输入实现稳定的3DGS场景重建，从而显著降低3DGS应用的输入门槛。

**关键词**：3D重建, 3D高斯溅射（3DGS）, 稀疏输入, 稀疏到稠密提升, 单步扩散模型, 图像伪影修复, 新视角合成, 稀疏视角重建, 鲁棒模型拟合, 加权梯度优化

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10893v1) | [下载PDF](https://arxiv.org/pdf/2603.10893v1.pdf)

---

## cs.LG

## [15. Neural Field Thermal Tomography: A Differentiable Physics Framework for Non-Destructive Evaluation](https://arxiv.org/abs/2603.11045v1)

**作者**：Tao Zhong, Yixun Hu, Dongzhe Zheng 等 5 位作者  
**分类**：cs.LG, cond-mat.mtrl-sci, cs.AI, cs.CV, physics.ins-det  
**发布时间**：2026-03-11

### 📄 论文摘要

We propose Neural Field Thermal Tomography (NeFTY), a differentiable physics framework for the quantitative 3D reconstruction of material properties from transient surface temperature measurements. While traditional thermography relies on pixel-wise 1D approximations that neglect lateral diffusion, and soft-constrained Physics-Informed Neural Networks (PINNs) often fail in transient diffusion scenarios due to gradient stiffness, NeFTY parameterizes the 3D diffusivity field as a continuous neural field optimized through a rigorous numerical solver. By leveraging a differentiable physics solver, our approach enforces thermodynamic laws as hard constraints while maintaining the memory efficiency required for high-resolution 3D tomography. Our discretize-then-optimize paradigm effectively mitigates the spectral bias and ill-posedness inherent in inverse heat conduction, enabling the recovery of subsurface defects at arbitrary scales. Experimental validation on synthetic data demonstrates that NeFTY significantly improves the accuracy of subsurface defect localization over baselines. Additional details at https://cab-lab-princeton.github.io/nefty/

### 🤖 AI 总结

**一句话总结**：NeFTY通过可微分物理求解器将热扩散定律作为硬约束，直接优化连续的3D热扩散率神经场，实现由瞬态表面温度反演材料内部缺陷的高分辨率三维重建。

**研究动机**：传统热成像常用逐像素1D近似而忽略横向热扩散，导致对真实三维传热与缺陷定位不准；而PINN在瞬态扩散问题中易受梯度刚性影响训练不稳定，难以可靠求解逆热传导。

**核心方法**：将3D扩散率场参数化为连续神经场，并采用“先离散再优化”的范式：用严格的数值热传导求解器进行前向仿真且对其可微分，从而对材料热力学规律施加硬约束并以可控内存代价进行高分辨率反演优化。

**主要结论**：在合成数据实验中，NeFTY相较基线方法显著提升了亚表面缺陷的三维定位精度，并通过缓解谱偏置与逆问题不适定性实现对任意尺度缺陷的更稳定恢复。

**关键词**：热层析成像, 非破坏检测, 瞬态热扩散, 逆热传导, 材料热扩散率重建, 三维连续神经场, 可微分物理求解器, 离散化后优化, 梯度刚性, 谱偏置缓解, 亚表面缺陷定位

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.11045v1) | [下载PDF](https://arxiv.org/pdf/2603.11045v1.pdf)

---

## [16. Leech Lattice Vector Quantization for Efficient LLM Compression](https://arxiv.org/abs/2603.11021v1)

**作者**：Tycho F. A. van der Ouderaa, Mart van Baalen, Paul Whatmough 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-11

### 📄 论文摘要

Scalar quantization of large language models (LLMs) is fundamentally limited by information-theoretic bounds. While vector quantization (VQ) overcomes these limits by encoding blocks of parameters jointly, practical implementations must avoid the need for expensive lookup mechanisms or other explicit codebook storage. Lattice approaches address this through highly structured and dense packing. This paper explores the Leech lattice, which, with its optimal sphere packing and kissing configurations at 24 dimensions, is the highest dimensional lattice known with such optimal properties. To make the Leech lattice usable for LLM quantization, we extend an existing search algorithm based on the extended Golay code construction, to i) support indexing, enabling conversion to and from bitstrings without materializing the codebook, ii) allow angular search over union of Leech lattice shells, iii) propose fully-parallelisable dequantization kernel. Together this yields a practical algorithm, namely Leech Lattice Vector Quantization (LLVQ). LLVQ delivers state-of-the-art LLM quantization performance, outperforming recent methods such as Quip\#, QTIP, and PVQ. These results highlight the importance of high-dimensional lattices for scalable, theoretically grounded model compression.

### 🤖 AI 总结

**一句话总结**：本文提出基于24维Leech晶格的向量量化LLVQ，在无需显式码本存储的前提下实现高效LLM压缩并取得SOTA量化效果。

**研究动机**：标量量化受信息论上限限制，而向量量化虽更强但常依赖昂贵查表/码本存储与检索；晶格量化可用高度结构化的“致密填充”来避免这些工程瓶颈。

**核心方法**：利用Leech晶格的最优球面填充性质，扩展基于扩展Golay码构造的搜索算法：支持可索引的位串↔晶格点转换（无需物化码本）、支持跨多个shell的角度搜索，并设计完全可并行的反量化kernel，形成LLVQ流程。

**主要结论**：LLVQ在LLM量化上优于Quip#、QTIP与PVQ等近期方法，表明高维最优晶格可在理论可解释性与工程可扩展性上同时推动大模型压缩性能。

**关键词**：模型压缩, 格量化, 高维球面密堆积, 无码本索引, 比特串编码, 角度搜索, Leech, Lattice

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2603.11021v1) | [下载PDF](https://arxiv.org/pdf/2603.11021v1.pdf)

---

## [17. Cross-Species Transfer Learning for Electrophysiology-to-Transcriptomics Mapping in Cortical GABAergic Interneurons](https://arxiv.org/abs/2603.11000v1)

**作者**：Theo Schwider, Ramin Ramezani  
**分类**：cs.LG, q-bio.NC  
**发布时间**：2026-03-11

### 📄 论文摘要

Single-cell electrophysiological recordings provide a powerful window into neuronal functional diversity and offer an interpretable route for linking intrinsic physiology to transcriptomic identity. Here, we replicate and extend the electrophysiology-to-transcriptomics framework introduced by Gouwens et al. (2020) using publicly available Allen Institute Patch-seq datasets from both mouse and human cortex. We focus on GABAergic inhibitory interneurons to target a subclass structure (Lamp5, Pvalb, Sst, Vip) that is comparable and conserved across species. After quality control, we analyzed 3,699 mouse visual cortex neurons and 506 human neocortical neurons from neurosurgical resections. Using standardized electrophysiological features and sparse PCA, we reproduced the major class-level separations reported in the original mouse study. For supervised prediction, a class-balanced random forest provided a strong feature-engineered baseline in mouse data and a reduced but still informative baseline in human data. We then developed an attention-based BiLSTM that operates directly on the structured IPFX feature-family representation, avoiding sPCA and providing feature-family-level interpretability via learned attention weights. Finally, we evaluated a cross-species transfer setting in which the sequence model is pretrained on mouse data and fine-tuned on human data for an aligned 4-class task, improving human macro-F1 relative to a human-only training baseline. Together, these results confirm reproducibility of the Gouwens pipeline in mouse data, demonstrate that sequence models can match feature-engineered baselines, and show that mouse-to-human transfer learning can provide measurable gains for human subclass prediction.

### 🤖 AI 总结

**一句话总结**：本文复现并扩展Gouwens等人的电生理→转录组映射框架，并通过鼠到人的迁移学习提升人类皮层GABA能中间神经元四大亚类的预测性能。

**研究动机**：单细胞电生理特征可解释但难以直接对应转录组身份，且人类数据更少、噪声更大，亟需验证跨物种可复现性并探索用小鼠数据帮助人类细胞分类。

**核心方法**：在Allen Patch-seq小鼠(3699)与人类(506)皮层GABA能中间神经元数据上进行质控与标准化特征提取，先用稀疏PCA复现类级分离与随机森林建立监督基线；进一步提出基于IPFX“特征族”序列表示的注意力BiLSTM，先在小鼠预训练再在人类对齐的4类任务上微调以做跨物种迁移评估。

**主要结论**：结果表明该电生理→转录组流程在小鼠数据上具有良好可复现性，注意力序列模型可达到与特征工程基线相当的效果并提供特征族级可解释性；在跨物种设置下，小鼠预训练+人类微调能相对人类单独训练提升人类宏平均F1，实现可测量的迁移增益。

**关键词**：跨物种迁移学习, 电生理-转录组映射, 单细胞电生理, GABA能抑制性中间神经元, 随机森林分类, 预训练-微调, Cross-Species, Transfer

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.11000v1) | [下载PDF](https://arxiv.org/pdf/2603.11000v1.pdf)

---

## [18. Factorized Neural Implicit DMD for Parametric Dynamics](https://arxiv.org/abs/2603.10995v1)

**作者**：Siyuan Chen, Zhecheng Wang, Yixin Chen 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-11

### 📄 论文摘要

A data-driven, model-free approach to modeling the temporal evolution of physical systems mitigates the need for explicit knowledge of the governing equations. Even when physical priors such as partial differential equations are available, such systems often reside in high-dimensional state spaces and exhibit nonlinear dynamics, making traditional numerical solvers computationally expensive and ill-suited for real-time analysis and control. Consider the problem of learning a parametric flow of a dynamical system: with an initial field and a set of physical parameters, we aim to predict the system's evolution over time in a way that supports long-horizon rollouts, generalization to unseen parameters, and spectral analysis.   We propose a physics-coded neural field parameterization of the Koopman operator's spectral decomposition. Unlike a physics-constrained neural field, which fits a single solution surface, and neural operators, which directly approximate the solution operator at fixed time horizons, our model learns a factorized flow operator that decouples spatial modes and temporal evolution. This structure exposes underlying eigenvalues, modes, and stability of the underlying physical process to enable stable long-term rollouts, interpolation across parameter spaces, and spectral analysis. We demonstrate the efficacy of our method on a range of dynamics problems, showcasing its ability to accurately predict complex spatiotemporal phenomena while providing insights into the system's dynamic behavior.

### 🤖 AI 总结

**一句话总结**：提出一种对Koopman算子谱分解进行“物理编码”的因子化神经隐式DMD模型，将空间模态与时间演化解耦，实现可泛化参数化动力学预测与稳定长时滚动，并支持谱分析。

**研究动机**：高维非线性物理系统的数值求解昂贵且不适合实时控制，而现有神经场/神经算子往往难以同时兼顾长时稳定、跨参数泛化与可解释的谱结构提取。作者希望学习一个能在未见参数下可靠外推、可长时预测并揭示稳定性信息的参数化流映射。

**核心方法**：将Koopman谱分解用神经隐式场进行参数化：用可学习的空间特征模态与由特征值控制的时间系数相乘构成因子化流算子，从而显式暴露特征值/模态并实现“空间-时间”解耦。该结构类似DMD/Koopman但以神经网络学习非线性系统的线性化谱表征，支持跨参数插值与长时rollout。

**主要结论**：在多类动力学任务上，该方法能更准确地预测复杂时空演化，同时在长时滚动上更稳定，并能提供特征值与模态等谱信息用于分析系统稳定性与动态行为。总体上验证了因子化Koopman神经场在参数泛化与可解释性方面优于仅拟合单一解面或固定时域的直接算子近似。

**关键词**：参数化动力系统, 谱分解, 动态模态分解（DMD）, 神经隐式表示, 因子化流算子, 时空动力学预测, 长时序滚动预测, 参数泛化, 稳定性分析

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10995v1) | [下载PDF](https://arxiv.org/pdf/2603.10995v1.pdf)

---

## [19. MCMC Informed Neural Emulators for Uncertainty Quantification in Dynamical Systems](https://arxiv.org/abs/2603.10987v1)

**作者**：Heikki Haario, Zhi-Song Liu, Martin Simon 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-11

### 📄 论文摘要

Neural networks are a commonly used approach to replace physical models with computationally cheap surrogates. Parametric uncertainty quantification can be included in training, assuming that an accurate prior distribution of the model parameters is available. Here we study the common opposite situation, where direct screening or random sampling of model parameters leads to exhaustive training times and evaluations at unphysical parameter values. Our solution is to decouple uncertainty quantification from network architecture. Instead of sampling network weights, we introduce the model-parameter distribution as an input to network training via Markov chain Monte Carlo (MCMC). In this way, the surrogate achieves the same uncertainty quantification as the underlying physical model, but with substantially reduced computation time. The approach is fully agnostic with respect to the neural network choice. In our examples, we present a quantile emulator for prediction and a novel autoencoder-based ODE network emulator that can flexibly estimate different trajectory paths corresponding to different ODE model parameters. Moreover, we present a mathematical analysis that provides a transparent way to relate potential performance loss to measurable distribution mismatch.

### 🤖 AI 总结

**一句话总结**：提出一种将MCMC得到的模型参数分布注入神经网络训练的“分布驱动”代理模型方法，在不改动网络结构的情况下实现与原物理模型一致的不确定性量化并显著降低计算成本。

**研究动机**：现实中常缺乏可信的参数先验，直接随机筛参数会导致训练/评估极其耗时且可能落在不物理的参数区域，进而影响代理模型的效率与可靠性。

**核心方法**：将不确定性量化与网络权重采样解耦：用MCMC在物理模型上推断得到参数后验/有效分布，并把该分布作为训练输入来指导数据生成与学习；同时给出分位数预测的emulator与基于自编码器的ODE轨迹emulator，并用分布失配的数学分析量化性能损失。

**主要结论**：该方法对网络架构无关，可在更少的物理模型评估下获得与原模型一致的UQ效果；论文还提供了可解释的理论联系，说明分布不匹配会如何导致可测量的性能下降。

**关键词**：不确定性量化, 参数不确定性, 神经网络代理模型, 参数分布条件化, 动力系统建模, ODE神经网络, 自编码器模拟器, 分位数回归, 分布失配分析, 物理模型替代, 贝叶斯推断

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10987v1) | [下载PDF](https://arxiv.org/pdf/2603.10987v1.pdf)

---

## [20. Federated Learning-driven Beam Management in LEO 6G Non-Terrestrial Networks](https://arxiv.org/abs/2603.10983v1)

**作者**：Maria Lamprini Bartsioka, Ioannis A. Bartsiokas, Athanasios D. Panagopoulos 等 5 位作者  
**分类**：cs.LG, physics.space-ph  
**发布时间**：2026-03-11

### 📄 论文摘要

Low Earth Orbit (LEO) Non-Terrestrial Networks (NTNs) require efficient beam management under dynamic propagation conditions. This work investigates Federated Learning (FL)-based beam selection in LEO satellite constellations, where orbital planes operate as distributed learners through the utilization of High-Altitude Platform Stations (HAPS). Two models, a Multi-Layer Perceptron (MLP) and a Graph Neural Network (GNN), are evaluated using realistic channel and beamforming data. Results demonstrate that GNN surpasses MLP in beam prediction accuracy and stability, particularly at low elevation angles, enabling lightweight and intelligent beam management for future NTN deployments.

### 🤖 AI 总结

**一句话总结**：提出一种由联邦学习驱动的LEO卫星波束管理方案，并验证GNN在波束选择预测上优于MLP，尤其在低仰角场景更稳定准确。

**研究动机**：LEO非地面网络传播条件动态变化，传统集中式或静态波束管理难以及时适配且开销高；同时多轨道面数据分散，需在隐私/通信受限下协同学习。

**核心方法**：以轨道面为分布式学习节点，并借助HAPS进行联邦学习协同训练；在真实信道与波束成形数据上对比两类模型（MLP与GNN）用于波束选择预测。

**主要结论**：实验表明GNN在波束预测准确率与稳定性方面整体优于MLP，低仰角时优势更明显，显示该FL+GNN框架可实现轻量化、智能化的未来NTN波束管理。

**关键词**：低轨卫星通信（LEO）, 非地面网络（NTN）, 波束管理, 波束选择, 联邦学习（FL）, 图神经网络（GNN）, 多层感知机（MLP）, 高空平台站（HAPS）, 卫星星座, 波束预测

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10983v1) | [下载PDF](https://arxiv.org/pdf/2603.10983v1.pdf)

---

## [21. FRIEND: Federated Learning for Joint Optimization of multi-RIS Configuration and Eavesdropper Intelligent Detection in B5G Networks](https://arxiv.org/abs/2603.10977v1)

**作者**：Maria Lamprini A. Bartsioka, Ioannis A. Bartsiokas, Anastasios K. Papazafeiropoulos 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-11

### 📄 论文摘要

As wireless systems evolve toward Beyond 5G (B5G), the adoption of cell-free (CF) millimeter-wave (mmWave) architectures combined with Reconfigurable Intelligent Surfaces (RIS) is emerging as a key enabler for ultra-reliable, high-capacity, scalable, and secure Industrial Internet of Things (IIoT) communications. However, safeguarding these complex and distributed environments against eavesdropping remains a critical challenge, particularly when conventional security mechanisms struggle to overcome scalability, and latency constraints. In this paper, a novel framework for detecting malicious users in RIS-enhanced cell-free mmWave networks using Federated Learning (FL) is presented. The envisioned setup features multiple access points (APs) operating without traditional cell boundaries, assisted by RIS nodes to dynamically shape the wireless propagation environment. Edge devices collaboratively train a Deep Convolutional Neural Network (DCNN) on locally observed Channel State Information (CSI), eliminating the need for raw data exchange. Moreover, an early-exit mechanism is incorporated in that model to jointly satisfy computational complexity requirements. Performance evaluation indicates that the integration of FL and multi-RIS coordination improves approximately 30% the achieved secrecy rate (SR) compared to baseline non-RIS-assisted methods while maintaining near-optimal detection accuracy levels. This work establishes a distributed, privacy-preserving approach to physical layer eavesdropping detection tailored for next-generation IIoT deployments.

### 🤖 AI 总结

**一句话总结**：提出FRIEND框架，在多RIS辅助的无小区mmWave B5G网络中用联邦学习训练DCNN进行窃听者检测，并联合优化RIS配置以提升安全性能与计算效率。

**研究动机**：RIS增强的无小区分布式IIoT网络结构复杂、节点分散，传统安全机制在可扩展性与时延上难以满足窃听防护需求。需要一种既能保护数据隐私又能在边缘侧高效检测恶意用户的方案。

**核心方法**：各边缘设备基于本地观测到的CSI在不上传原始数据的前提下，通过联邦学习协同训练用于窃听者识别的DCNN。模型引入early-exit机制以降低推理计算开销，并结合多RIS协同来动态塑造传播环境、联合提升检测与保密传输效果。

**主要结论**：实验评估表明，FL与多RIS协调结合可在保持接近最优检测准确率的同时，相比非RIS基线将保密速率提升约30%。该方法为下一代IIoT提供了一种分布式、隐私保护的物理层窃听检测与安全增强路径。

**关键词**：联邦学习, 可重构智能表面（RIS）, 无小区（cell-free）网络, 毫米波通信, 物理层安全, 窃听者检测, 信道状态信息（CSI）, 深度卷积神经网络（DCNN）

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10977v1) | [下载PDF](https://arxiv.org/pdf/2603.10977v1.pdf)

---

## [22. TOSSS: a CVE-based Software Security Benchmark for Large Language Models](https://arxiv.org/abs/2603.10969v1)

**作者**：Marc Damie, Murat Bilgehan Ertan, Domenico Essoussi 等 6 位作者  
**分类**：cs.LG, cs.CL, cs.CR, cs.SE  
**发布时间**：2026-03-11

### 📄 论文摘要

With their increasing capabilities, Large Language Models (LLMs) are now used across many industries. They have become useful tools for software engineers and support a wide range of development tasks. As LLMs are increasingly used in software development workflows, a critical question arises: are LLMs good at software security? At the same time, organizations worldwide invest heavily in cybersecurity to reduce exposure to disruptive attacks. The integration of LLMs into software engineering workflows may introduce new vulnerabilities and weaken existing security efforts.   We introduce TOSSS (Two-Option Secure Snippet Selection), a benchmark that measures the ability of LLMs to choose between secure and vulnerable code snippets. Existing security benchmarks for LLMs cover only a limited range of vulnerabilities. In contrast, TOSSS relies on the CVE database and provides an extensible framework that can integrate newly disclosed vulnerabilities over time. Our benchmark gives each model a security score between 0 and 1 based on its behavior; a score of 1 indicates that the model always selects the secure snippet, while a score of 0 indicates that it always selects the vulnerable one. We evaluate 14 widely used open-source and closed-source models on C/C++ and Java code and observe scores ranging from 0.48 to 0.89. LLM providers already publish many benchmark scores for their models, and TOSSS could become a complementary security-focused score to include in these reports.

### 🤖 AI 总结

**一句话总结**：TOSSS 是一个基于 CVE 的软件安全基准，用于评测 LLM 在“二选一”代码片段中辨别并选择安全实现的能力，并用 0~1 的安全分数刻画模型表现。

**研究动机**：LLM 正被广泛集成进软件开发流程，但其生成/建议代码可能引入漏洞、削弱安全工作，因此需要一个覆盖面更广且可随新漏洞持续更新的安全评测体系。

**核心方法**：提出 TOSSS（Two-Option Secure Snippet Selection），从 CVE 数据库构建“安全片段 vs 易受攻击片段”的对比样例，要求模型在两者中选择更安全的实现，并以选择安全片段的行为给出 0~1 的安全得分。

**主要结论**：在 C/C++ 与 Java 上评测 14 个开源与闭源模型，安全得分约在 0.48~0.89 之间，显示不同模型在漏洞识别/规避能力上差异显著；作者建议将 TOSSS 作为补充性的安全指标纳入模型基准报告。

**关键词**：LLM安全评测, 软件安全基准, CVE驱动基准, 漏洞识别, 安全代码选择, 可扩展评测框架, 安全评分指标, 代码安全测试集, C/C++安全

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10969v1) | [下载PDF](https://arxiv.org/pdf/2603.10969v1.pdf)

---

## [23. Ranking Reasoning LLMs under Test-Time Scaling](https://arxiv.org/abs/2603.10960v1)

**作者**：Mohsen Hariri, Michael Hinczewski, Jing Ma 等 4 位作者  
**分类**：cs.LG, math.ST  
**发布时间**：2026-03-11

### 📄 论文摘要

Test-time scaling evaluates reasoning LLMs by sampling multiple outputs per prompt, but ranking models in this regime remains underexplored. We formalize dense benchmark ranking under test-time scaling and introduce Scorio, a library that implements statistical ranking methods such as paired-comparison models, item response theory (IRT) models, voting rules, and graph- and spectral-based methods. Across $20$ reasoning models on four Olympiad-style math benchmarks (AIME'24, AIME'25, HMMT'25, and BrUMO'25; up to $N=80$ trials), most full-trial rankings agree closely with the Bayesian gold standard $\mathrm{Bayes}_{\mathcal{U}}@80$ (mean Kendall's $τ_b = 0.93$--$0.95$), and $19$--$34$ methods recover exactly the same ordering. In the single-trial regime, the best methods reach $τ_b \approx 0.86$. Using greedy decoding as an empirical prior ($\mathrm{Bayes}_{\mathbf{R}_0}@N$) reduces variance at $N=1$ by $16$--$52\%$, but can bias rankings when greedy and stochastic sampling disagree. These results identify reliable ranking methods for both high- and low-budget test-time scaling. We release Scorio as an open-source library at https://github.com/mohsenhariri/scorio.

### 🤖 AI 总结

**一句话总结**：论文系统研究“测试时扩展（多次采样）”下推理型LLM的可靠排名方法，并开源Scorio库来实现与评估多种统计排名算法。

**研究动机**：在test-time scaling中，同一题目会采样多次输出导致分数/方差变化显著，但现有基准多聚焦平均准确率，缺少对“如何稳定、公正地给模型排序”的系统分析与工具。

**核心方法**：作者形式化了密集基准在多试次采样下的排名问题，提出Scorio实现成对比较、IRT、投票规则、图/谱方法等，并在20个推理模型与4个奥赛数学基准上（最多80次试验）与贝叶斯金标准Bayes@80对齐评测；同时引入以贪心解码作为经验先验的Bayes_{R0}@N以降低小样本方差。

**主要结论**：在完整试次（N=80）下，多数方法与Bayes@80高度一致（Kendall τ_b≈0.93–0.95），且有19–34种方法能恢复完全相同的排序；单次试验时最佳方法仍可达τ_b≈0.86，而用贪心先验可在N=1降低16–52%方差但在贪心与随机采样分歧时会引入排名偏差。

**关键词**：测试时扩展, 推理LLM评测, 多次采样评估, 模型排名方法, 贝叶斯排名, 成对比较模型, 项目反应理论（IRT）, 投票规则, 图排序方法, 谱排序方法, 奥赛数学基准

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10960v1) | [下载PDF](https://arxiv.org/pdf/2603.10960v1.pdf)

---

## [24. When should we trust the annotation? Selective prediction for molecular structure retrieval from mass spectra](https://arxiv.org/abs/2603.10950v1)

**作者**：Mira Jürgens, Gaetan De Waele, Morteza Rakhshaninejad 等 4 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-03-11

### 📄 论文摘要

Machine learning methods for identifying molecular structures from tandem mass spectra (MS/MS) have advanced rapidly, yet current approaches still exhibit significant error rates. In high-stakes applications such as clinical metabolomics and environmental screening, incorrect annotations can have serious consequences, making it essential to determine when a prediction can be trusted. We introduce a selective prediction framework for molecular structure retrieval from MS/MS spectra, enabling models to abstain from predictions when uncertainty is too high. We formulate the problem within the risk-coverage tradeoff framework and comprehensively evaluate uncertainty quantification strategies at two levels of granularity: fingerprint-level uncertainty over predicted molecular fingerprint bits, and retrieval-level uncertainty over candidate rankings. We compare scoring functions including first-order confidence measures, aleatoric and epistemic uncertainty estimates from second-order distributions, as well as distance-based measures in the latent space. All experiments are conducted on the MassSpecGym benchmark. Our analysis reveals that while fingerprint-level uncertainty scores are poor proxies for retrieval success, computationally inexpensive first-order confidence measures and retrieval-level aleatoric uncertainty achieve strong risk-coverage tradeoffs across evaluation settings. We demonstrate that by applying distribution-free risk control via generalization bounds, practitioners can specify a tolerable error rate and obtain a subset of annotations satisfying that constraint with high probability.

### 🤖 AI 总结

**一句话总结**：本文提出用于MS/MS分子结构检索的选择性预测框架，让模型在不确定时选择“拒答”，以在给定覆盖率下控制错误风险并提升可信注释质量。

**研究动机**：现有基于机器学习的质谱结构注释仍有较高错误率，而临床代谢组学与环境筛查等高风险场景中错误注释代价很高，因此需要判断“何时可信、何时应 abstain”。

**核心方法**：将结构检索建模为风险-覆盖率权衡的选择性预测问题，在指纹位级与检索排序级两种粒度上系统评估不确定性度量（包括一阶置信度、二阶分布的aleatoric/epistemic不确定性、以及潜空间距离等），并结合分布无关的风险控制/泛化界来按用户指定容错率筛选可发布的注释子集。

**主要结论**：指纹位级不确定性难以有效代理最终检索是否成功；相反，计算开销更低的一阶置信度与检索级aleatoric不确定性在多设置下取得更优的风险-覆盖率曲线，并可通过分布无关风险控制在高概率下保证输出注释的错误率不超过指定阈值。

**关键词**：选择性预测, 拒绝预测, 不确定性量化, 风险-覆盖权衡, MS/MS 分子结构检索, 临床代谢组学, 环境筛查, 分子指纹预测, 候选排序不确定性, 认知不确定性, 分布无关风险控制

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10950v1) | [下载PDF](https://arxiv.org/pdf/2603.10950v1.pdf)

---

## [25. Safe RLHF Beyond Expectation: Stochastic Dominance for Universal Spectral Risk Control](https://arxiv.org/abs/2603.10938v1)

**作者**：Yaswanth Chittepu, Ativ Joshi, Rajarshi Bhattacharjee 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-11

### 📄 论文摘要

Safe Reinforcement Learning from Human Feedback (RLHF) typically enforces safety through expected cost constraints, but the expectation captures only a single statistic of the cost distribution and fails to account for distributional uncertainty, particularly under heavy tails or rare catastrophic events. This limitation is problematic when robustness and risk sensitivity are critical. Stochastic dominance offers a principled alternative by comparing entire cost distributions rather than just their averages, enabling direct control over tail risks and potential out-of-distribution failures that expectation-based constraints may overlook. In this work, we propose Risk-sensitive Alignment via Dominance (RAD), a novel alignment framework that replaces scalar expected cost constraints with First-Order Stochastic Dominance (FSD) constraints. We operationalize this constraint by comparing the target policy's cost distribution to that of a reference policy within an Optimal Transport (OT) framework, using entropic regularization and Sinkhorn iterations to obtain a differentiable and computationally efficient objective for stable end-to-end optimization. Furthermore, we introduce quantile-weighted FSD constraints and show that weighted FSD universally controls a broad class of Spectral Risk Measures (SRMs), so that improvements under weighted dominance imply guaranteed improvements in the corresponding spectral risk. This provides a principled mechanism for tuning a model's risk profile via the quantile weighting function. Empirical results demonstrate that RAD improves harmlessness over baselines while remaining competitive in helpfulness, and exhibits greater robustness on out-of-distribution harmlessness evaluations.

### 🤖 AI 总结

**一句话总结**：RAD 用一阶随机占优（FSD）替代传统 RLHF 的期望成本约束，在可微最优传输框架下直接对齐整段成本分布，从而更稳健地控制尾部风险与灾难性事件。

**研究动机**：仅用期望成本衡量安全性会忽略分布形状与尾部不确定性，在重尾或稀有高代价事件下可能“期望安全但实际不稳健”。作者希望用能比较整体分布的约束来提升风险敏感性与 OOD 安全鲁棒性。

**核心方法**：提出 Risk-sensitive Alignment via Dominance (RAD)：对目标策略与参考策略的成本分布施加 FSD 约束，并用带熵正则的最优传输（Sinkhorn 迭代）将分布比较转为可微、稳定的端到端优化目标。进一步引入分位数加权的 FSD，证明加权占优可普适地控制一类谱风险度量（SRM），可通过权重函数调节模型风险偏好。

**主要结论**：实验表明 RAD 相比基线能提升 harmlessness 且保持 helpfulness 竞争力，并在分布外的 harmlessness 评测上更鲁棒。理论上，加权 FSD 带来对谱风险的保证改进，使得安全对齐从“控均值”扩展到“控尾部与风险谱”。

**关键词**：风险敏感对齐, 随机支配, 一阶随机支配, 尾部风险控制, 分布式鲁棒性, 谱风险度量, 分位数加权, 最优传输, 熵正则化, 分布外评测

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10938v1) | [下载PDF](https://arxiv.org/pdf/2603.10938v1.pdf)

---

## [26. Quantifying Membership Disclosure Risk for Tabular Synthetic Data Using Kernel Density Estimators](https://arxiv.org/abs/2603.10937v1)

**作者**：Rajdeep Pathak, Sayantee Jana  
**分类**：cs.LG, stat.AP  
**发布时间**：2026-03-11

### 📄 论文摘要

The use of synthetic data has become increasingly popular as a privacy-preserving alternative to sharing real datasets, especially in sensitive domains such as healthcare, finance, and demography. However, the privacy assurances of synthetic data are not absolute, and remain susceptible to membership inference attacks (MIAs), where adversaries aim to determine whether a specific individual was present in the dataset used to train the generator. In this work, we propose a practical and effective method to quantify membership disclosure risk in tabular synthetic datasets using kernel density estimators (KDEs). Our KDE-based approach models the distribution of nearest-neighbour distances between synthetic data and the training records, allowing probabilistic inference of membership and enabling robust evaluation via ROC curves. We propose two attack models: a 'True Distribution Attack', which assumes privileged access to training data, and a more realistic, implementable 'Realistic Attack' that uses auxiliary data without true membership labels. Empirical evaluations across four real-world datasets and six synthetic data generators demonstrate that our method consistently achieves higher F1 scores and sharper risk characterization than a prior baseline approach, without requiring computationally expensive shadow models. The proposed method provides a practical framework and metric for quantifying membership disclosure risk in synthetic data, which enables data custodians to conduct a post-generation risk assessment prior to releasing their synthetic datasets for downstream use. The datasets and codes for this study are available at https://github.com/PyCoder913/MIA-KDE.

### 🤖 AI 总结

**一句话总结**：提出一种基于核密度估计（KDE）的实用评估方法，用于量化表格合成数据的成员推断（membership disclosure）风险，并在多数据集多生成器上优于现有基线。

**研究动机**：合成数据虽常被视为隐私友好的替代方案，但仍可能遭受成员推断攻击，数据发布者缺少一种无需昂贵影子模型、可在发布前进行后评估的风险量化工具。

**核心方法**：用KDE建模“合成样本与训练记录的最近邻距离”分布，将距离转化为成员属于训练集的概率并用ROC等指标评估；同时定义两种攻击设定：假设可访问训练数据的True Distribution Attack，以及仅依赖无真实成员标签辅助数据的Realistic Attack。

**主要结论**：在4个真实数据集、6种合成数据生成器上，KDE方法获得更高的F1分数与更清晰的风险刻画，相比基线更有效且无需计算昂贵的影子模型，适合作为合成数据发布前的成员泄露风险评估框架与度量。

**关键词**：表格合成数据, 成员推断攻击, 成员泄露风险量化, 核密度估计（KDE）, 最近邻距离分布, 隐私风险评估指标, ROC 曲线评测, F1 分数, 真实分布攻击模型, 辅助数据攻击模型, 后生成风险评估

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10937v1) | [下载PDF](https://arxiv.org/pdf/2603.10937v1.pdf)

---

## [27. Historical Consensus: Preventing Posterior Collapse via Iterative Selection of Gaussian Mixture Priors](https://arxiv.org/abs/2603.10935v1)

**作者**：Zegu Zhang, Jian Zhang  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-03-11

### 📄 论文摘要

Variational autoencoders (VAEs) frequently suffer from posterior collapse, where latent variables become uninformative and the approximate posterior degenerates to the prior. Recent work has characterized this phenomenon as a phase transition governed by the spectral properties of the data covariance matrix. In this paper, we propose a fundamentally different approach: instead of avoiding collapse through architectural constraints or hyperparameter tuning, we eliminate the possibility of collapse altogether by leveraging the multiplicity of Gaussian mixture model (GMM) clusterings. We introduce Historical Consensus Training, an iterative selection procedure that progressively refines a set of candidate GMM priors through alternating optimization and selection. The key insight is that models trained to satisfy multiple distinct clustering constraints develop a historical barrier -- a region in parameter space that remains stable even when subsequently trained with a single objective. We prove that this barrier excludes the collapsed solution, and demonstrate through extensive experiments on synthetic and real-world datasets that our method achieves non-collapsed representations regardless of decoder variance or regularization strength. Our approach requires no explicit stability conditions (e.g., $σ^{\prime 2} < λ_{\max}$) and works with arbitrary neural architectures. The code is available at https://github.com/tsegoochang/historical-consensus-vae.

### 🤖 AI 总结

**一句话总结**：提出“历史共识训练”通过迭代选择高斯混合先验（GMM prior），在不依赖架构或超参条件的情况下从机制上避免VAE后验塌缩。

**研究动机**：VAE常出现后验塌缩使潜变量失去信息，既有方法多靠调正则强度、解码器方差或结构约束且仍受稳定性条件限制。作者希望用一种与这些条件无关的方法，直接排除塌缩解。

**核心方法**：构造多个候选GMM聚类先验，并进行“交替优化+选择”的迭代流程，逐步筛出能同时满足多种聚类约束的先验/模型组合。其关键在于多目标聚类约束训练会在参数空间形成“历史屏障”（historical barrier），使模型即便后续只用单一目标训练也保持在非塌缩区域。

**主要结论**：理论上证明该历史屏障会排除塌缩解，实验表明在不同数据集上该方法能稳定学到非塌缩表示，且不需要显式条件（如σ′²<λ_max）、对解码器方差/正则强度不敏感并适配任意网络架构。

**关键词**：后验坍塌, 变分自编码器, 高斯混合先验, 历史共识训练, 迭代选择, 交替优化, 聚类约束, 参数空间屏障, 相变分析, 协方差谱性质

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10935v1) | [下载PDF](https://arxiv.org/pdf/2603.10935v1.pdf)

---

## [28. ECoLAD: Deployment-Oriented Evaluation for Automotive Time-Series Anomaly Detection](https://arxiv.org/abs/2603.10926v1)

**作者**：Kadir-Kaan Özer, René Ebeling, Markus Enzweiler  
**分类**：cs.LG  
**发布时间**：2026-03-11

### 📄 论文摘要

Time-series anomaly detectors are commonly compared on workstation-class hardware under unconstrained execution. In-vehicle monitoring, however, requires predictable latency and stable behavior under limited CPU parallelism. Accuracy-only leaderboards can therefore misrepresent which methods remain feasible under deployment-relevant constraints.   We present ECoLAD (Efficiency Compute Ladder for Anomaly Detection), a deployment-oriented evaluation protocol instantiated as an empirical study on proprietary automotive telemetry (anomaly rate ${\approx}$0.022) and complementary public benchmarks. ECoLAD applies a monotone compute-reduction ladder across heterogeneous detector families using mechanically determined, integer-only scaling rules and explicit CPU thread caps, while logging every applied configuration change. Throughput-constrained behavior is characterized by sweeping target scoring rates and reporting (i) coverage (the fraction of entities meeting the target) and (ii) the best AUC-PR achievable among measured ladder configurations satisfying the target. On constrained automotive telemetry, lightweight classical detectors sustain both coverage and detection lift above the random baseline across the full throughput sweep. Several deep methods lose feasibility before they lose accuracy.

### 🤖 AI 总结

**一句话总结**：ECoLAD提出一种面向车载部署约束的时序异常检测评测协议，通过逐级削减计算预算来同时衡量吞吐/延迟可行性与检测性能。

**研究动机**：现有方法多在工作站与不受限并行下比拼精度，难以反映车载场景中CPU线程受限且需稳定、可预测延迟时哪些模型真正可部署。仅看准确率榜单会误判深度模型在真实约束下的可行性。

**核心方法**：ECoLAD用“单调计算缩减阶梯”在不同检测器家族上按机械化、整数缩放规则逐步降算力，并显式限制CPU线程数、记录每次配置变更。通过扫目标打分速率（吞吐），报告覆盖率（满足吞吐目标的实体比例）以及在满足目标的阶梯配置中可达到的最佳AUC-PR。

**主要结论**：在受限的车载遥测上，轻量级传统检测器在整个吞吐扫掠范围内仍能保持较高覆盖率并相对随机基线有稳定提升。部分深度方法往往在精度明显下降之前就先因吞吐/资源约束而失去部署可行性。

**关键词**：时间序列异常检测, 车载监控, 部署约束评测, 计算量缩减梯度, 吞吐率约束, 可预测延迟, CPU线程上限, 覆盖率指标, 汽车遥测数据, 轻量级经典检测器, 深度模型可行性

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10926v1) | [下载PDF](https://arxiv.org/pdf/2603.10926v1.pdf)

---

## [29. NCAA Bracket Prediction Using Machine Learning and Combinatorial Fusion Analysis](https://arxiv.org/abs/2603.10916v1)

**作者**：Yuanhong Wu, Isaiah Smith, Tushar Marwah 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-11

### 📄 论文摘要

Machine learning models have demonstrated remarkable success in sports prediction in the past years, often treating sports prediction as a classification task within the field. This paper introduces new perspectives for analyzing sports data to predict outcomes more accurately. We leverage rankings to generate team rankings for the 2024 dataset using Combinatorial Fusion Analysis (CFA), a new paradigm for combining multiple scoring systems through the rank-score characteristic (RSC) function and cognitive diversity (CD). Our result based on rank combination with respect to team ranking has an accuracy rate of $74.60\%$, which is higher than the best of the ten popular public ranking systems ($73.02\%$). This exhibits the efficacy of CFA in enhancing the precision of sports prediction through different lens.

### 🤖 AI 总结

**一句话总结**：本文提出用组合融合分析（CFA）融合多种公共排名体系生成球队综合排名，从而提升NCAA比赛结果预测准确率。

**研究动机**：现有体育预测多将问题视为分类任务且依赖单一评分/排名系统，作者希望从“融合多源排名信息”的角度进一步提高预测精度。

**核心方法**：使用CFA框架，通过Rank-Score Characteristic（RSC）函数与Cognitive Diversity（CD）度量，将多种评分系统进行组合与加权融合，生成2024数据集的球队综合排名并用于胜负预测。

**主要结论**：基于排名组合的CFA方法达到74.60%准确率，超过10个流行公共排名系统中的最佳结果73.02%，表明CFA能有效提升体育预测精度。

**关键词**：体育赛事预测, 胜负分类, 排名融合, 评分系统融合, 组合融合分析（CFA）, 秩-分特征函数（RSC）, 认知多样性（CD）, 排名聚合, 球队排名生成, 预测准确率评估

**评分**：17

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10916v1) | [下载PDF](https://arxiv.org/pdf/2603.10916v1.pdf)

---

## [30. Ergodicity in reinforcement learning](https://arxiv.org/abs/2603.10895v1)

**作者**：Dominik Baumann, Erfaun Noorani, Arsenii Mustafin 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-11

### 📄 论文摘要

In reinforcement learning, we typically aim to optimize the expected value of the sum of rewards an agent collects over a trajectory. However, if the process generating these rewards is non-ergodic, the expected value, i.e., the average over infinitely many trajectories with a given policy, is uninformative for the average over a single, but infinitely long trajectory. Thus, if we care about how the individual agent performs during deployment, the expected value is not a good optimization objective. In this paper, we discuss the impact of non-ergodic reward processes on reinforcement learning agents through an instructive example, relate the notion of ergodic reward processes to more widely used notions of ergodic Markov chains, and present existing solutions that optimize long-term performance of individual trajectories under non-ergodic reward dynamics.

### 🤖 AI 总结

**一句话总结**：论文指出在非遍历（non-ergodic）的奖励生成过程中，最大化期望累计回报可能无法提升单个智能体在一次长期部署轨迹上的真实表现，应转向优化单轨迹的长期性能指标。

**研究动机**：强化学习通常优化“跨无限多条轨迹的期望回报”，但当奖励过程非遍历时，这个期望与“单条无限长轨迹的时间平均回报”可能严重不一致，从而导致部署时个体表现不佳。论文动机是在更贴近实际部署的评价标准下重新审视RL目标函数与学习策略。

**核心方法**：通过一个具启发性的例子展示非遍历奖励会如何使期望回报目标失效，并澄清“遍历的奖励过程”与常见“遍历的马尔可夫链”概念之间的关系。进一步总结并讨论已有替代方案：直接优化单轨迹长期表现（时间平均/增长率等）而非仅优化期望值的RL设定与方法。

**主要结论**：当奖励动力学非遍历时，期望回报不再是对个体长期部署表现的可靠代理，可能产生误导性的最优策略。采用面向单轨迹长期性能的目标与算法（而非纯期望最大化）能更合理地处理此类环境并提升实际部署的稳健性。

**关键词**：强化学习, 遍历性, 非遍历奖励过程, 期望回报, 时间平均回报, 单轨迹长期性能, 路径依赖奖励, 遍历马尔可夫链, 目标函数重构, 非遍历动力学优化

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10895v1) | [下载PDF](https://arxiv.org/pdf/2603.10895v1.pdf)

---

