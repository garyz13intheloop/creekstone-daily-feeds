# arXiv AI 论文日报 | 2026-04-09

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (11 篇)
- [cs.CV](#csCV) (12 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (2 篇)

---

## cs.AI

## [1. Artifacts as Memory Beyond the Agent Boundary](https://arxiv.org/abs/2604.08756v1)

**作者**：John D. Martin, Fraser Mince, Esra'a Saleh 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-09

### 📄 论文摘要

The situated view of cognition holds that intelligent behavior depends not only on internal memory, but on an agent's active use of environmental resources. Here, we begin formalizing this intuition within Reinforcement Learning (RL). We introduce a mathematical framing for how the environment can functionally serve as an agent's memory, and prove that certain observations, which we call artifacts, can reduce the information needed to represent history. We corroborate our theory with experiments showing that when agents observe spatial paths, the amount of memory required to learn a performant policy is reduced. Interestingly, this effect arises unintentionally, and implicitly through the agent's sensory stream. We discuss the implications of our findings, and show they satisfy qualitative properties previously used to ground accounts of external memory. Moving forward, we anticipate further work on this subject could reveal principled ways to exploit the environment as a substitute for explicit internal memory.

### 🤖 AI 总结

**一句话总结**：论文提出环境可作为代理外部记忆的数学框架，证明了观察到的"人工制品"(artifacts)能减少表示历史所需的信息量，并通过实验验证了空间路径观察可降低学习高性能策略所需的记忆量。

**研究动机**：情境认知观认为智能行为依赖于内部记忆与环境资源的主动利用，但这一直觉在强化学习中缺乏严格的数学形式化。

**核心方法**：引入环境作为代理记忆的数学框架，定义"人工制品"(artifacts)为可降低历史信息表示量的观察，设计实验让代理观察空间路径并测量学习策略所需记忆量的变化。

**主要结论**：空间路径观察能隐式、意外地减少代理所需内部记忆，证实了环境可作为记忆替代，且满足先前用于支撑外部记忆理论的定性属性。

**关键词**：情境认知, 外部记忆, 强化学习, 策略学习, 环境资源, 信息压缩, 感知流, 智能体边界, 历史表示

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08756v1) | [下载PDF](https://arxiv.org/pdf/2604.08756v1.pdf)

---

## [2. Model Space Reasoning as Search in Feedback Space for Planning Domain Generation](https://arxiv.org/abs/2604.08712v1)

**作者**：James Oswald, Daniel Oblinsky, Volodymyr Varha 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-09

### 📄 论文摘要

The generation of planning domains from natural language descriptions remains an open problem even with the advent of large language models and reasoning models. Recent work suggests that while LLMs have the ability to assist with domain generation, they are still far from producing high quality domains that can be deployed in practice. To this end, we investigate the ability of an agentic language model feedback framework to generate planning domains from natural language descriptions that have been augmented with a minimal amount of symbolic information. In particular, we evaluate the quality of the generated domains under various forms of symbolic feedback, including landmarks, and output from the VAL plan validator. Using these feedback mechanisms, we experiment using heuristic search over model space to optimize domain quality.

### 🤖 AI 总结

**一句话总结**：本文探索使用增强型符号反馈的代理语言模型框架，通过启发式搜索优化模型空间来生成高质量的规划领域。

**研究动机**：尽管大语言模型在辅助领域生成方面展现出能力，但其生成的领域质量仍远未达到实际部署标准，这是当前开放性难题。

**核心方法**：通过引入最少量符号信息增强自然语言描述，结合地标和VAL计划验证器的符号反馈，采用启发式搜索遍历模型空间以优化领域质量。

**主要结论**：实验表明符号反馈机制能有效提升生成规划领域质量，为改进基于语言模型的领域生成提供了可行方向。

**关键词**：LLM, 自动化规划, 规划领域生成, 模型空间搜索, 启发式搜索, 符号反馈, 计划验证, 领域质量优化, 自然语言规划

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08712v1) | [下载PDF](https://arxiv.org/pdf/2604.08712v1.pdf)

---

## cs.CL

## [3. Lessons Without Borders? Evaluating Cultural Alignment of LLMs Using Multilingual Story Moral Generation](https://arxiv.org/abs/2604.08797v1)

**作者**：Sophie Wu, Andrew Piper  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-09

### 📄 论文摘要

Stories are key to transmitting values across cultures, but their interpretation varies across linguistic and cultural contexts. Thus, we introduce multilingual story moral generation as a novel culturally grounded evaluation task. Using a new dataset of human-written story morals collected across 14 language-culture pairs, we compare model outputs with human interpretations via semantic similarity, a human preference survey, and value categorization. We show that frontier models such as GPT-4o and Gemini generate story morals that are semantically similar to human responses and preferred by human evaluators. However, their outputs exhibit markedly less cross-linguistic variation and concentrate on a narrower set of widely shared values. These findings suggest that while contemporary models can approximate central tendencies of human moral interpretation, they struggle to reproduce the diversity that characterizes human narrative understanding. By framing narrative interpretation as an evaluative task, this work introduces a new approach to studying cultural alignment in language models beyond static benchmarks or knowledge-based tests.

### 🤖 AI 总结

**一句话总结**：该研究通过多语言故事道德生成任务评估前沿LLM的文化对齐能力，发现GPT-4o和Gemini虽能生成语义相似的道德判断，但缺乏跨文化多样性。

**研究动机**：故事是跨文化传递价值观的重要载体，但不同语言和文化背景下对道德的解读存在差异，因此需要评估LLM是否能理解和再现这种文化多样性。

**核心方法**：构建包含14种语言-文化对的人类撰写故事道德数据集，从语义相似度、人类偏好调查和价值分类三个维度评估GPT-4o、Gemini等模型的生成质量。

**主要结论**：前沿模型生成的道德判断与人类中央趋势相近且被人类评估者偏好，但表现出更少的跨语言变异性和更窄的价值范围，说明现有LLM难以复现人类叙事理解的文化多样性。

**关键词**：多语言故事道德, 文化对齐评估, 跨语言变异性, 价值分类, 人类偏好, 语义相似度, Lessons, Without

**评分**：5

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08797v1) | [下载PDF](https://arxiv.org/pdf/2604.08797v1.pdf)

---

## [4. MedConceal: A Benchmark for Clinical Hidden-Concern Reasoning Under Partial Observability](https://arxiv.org/abs/2604.08788v1)

**作者**：Yikun Han, Joey Chan, Jingyuan Chen 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-09

### 📄 论文摘要

Patient-clinician communication is an asymmetric-information problem: patients often do not disclose fears, misconceptions, or practical barriers unless clinicians elicit them skillfully. Effective medical dialogue therefore requires reasoning under partial observability: clinicians must elicit latent concerns, confirm them through interaction, and respond in ways that guide patients toward appropriate care. However, existing medical dialogue benchmarks largely sidestep this challenge by exposing hidden patient state, collapsing elicitation into extraction, or evaluating responses without modeling what remains hidden. We present MedConceal, a benchmark with an interactive patient simulator for evaluating hidden-concern reasoning in medical dialogue, comprising 300 curated cases and 600 clinician-LLM interactions. Built from clinician-answered online health discussions, each case pairing clinician-visible context with simulator-internal hidden concerns derived from prior literature and structured using an expert-developed taxonomy. The simulator withholds these concerns from the dialogue agent, tracks whether they have been revealed and addressed via theory-grounded turn-level communication signals, and is clinician-reviewed for clinical plausibility. This enables process-aware evaluation of both task success and the interaction process that leads to it. We study two abilities: confirmation, surfacing hidden concerns through multi-turn dialogue, and intervention, addressing the primary concern and guiding the patient toward a target plan. Results show that no single system dominates: frontier models lead on different confirmation metrics, while human clinicians (N=159) remain strongest on intervention success. Together, these results identify hidden-concern reasoning under partial observability as a key unresolved challenge for medical dialogue systems.

### 🤖 AI 总结

**一句话总结**：MedConceal是一个用于评估医疗对话系统识别和解决患者隐藏担忧能力的基准测试，通过交互式患者模拟器在部分可观测条件下测试系统的确认和干预能力。

**研究动机**：现有医疗对话基准测试直接暴露患者隐藏状态，回避了患者-临床医生沟通中的不对称信息问题，无法真正评估临床医生发现潜在担忧的推理能力。

**核心方法**：构建300个病例和600次交互的模拟器，从在线健康讨论中提取病例，模拟器内部保留隐藏关注但不透露给对话代理，通过轮次级通信信号追踪揭示情况，实现过程感知评估。

**主要结论**：前沿模型在不同确认指标上各有优势，但人类临床医生在干预成功率上仍最强，结果表明隐藏担忧推理是当前医疗对话系统的关键未解难题。

**关键词**：医疗对话, 隐藏担忧推理, 部分可观测性, 患者模拟器, 基准测试, 确认能力, 干预能力, 医患沟通, LLM, 交互式对话

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08788v1) | [下载PDF](https://arxiv.org/pdf/2604.08788v1.pdf)

---

## [5. Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics](https://arxiv.org/abs/2604.08764v1)

**作者**：Raphael Bernas, Fanny Jourdan, Antonin Poché 等 4 位作者  
**分类**：cs.CL, math.DG  
**发布时间**：2026-04-09

### 📄 论文摘要

Since their introduction, Transformer architectures have dominated Natural Language Processing (NLP). However, recent research has highlighted an inherent anisotropy phenomenon in these models, presenting a significant challenge to their geometric interpretation. Previous theoretical studies on this phenomenon are rarely grounded in the underlying representation geometry. In this paper, we extend them by deriving geometric arguments for how frequency-biased sampling attenuates curvature visibility and why training preferentially amplify tangent directions. Empirically, we then use concept-based mechanistic interpretability during training, rather than only post hoc, to fit activation-derived low-rank tangent proxies and test them against ordinary backpropagated true gradients. Across encoder-style and decoder-style language models, we find that these activation-derived directions capture both unusually large gradient energy and a substantially larger share of gradient anisotropy than matched-rank normal controls, providing strong empirical support for a tangent-aligned account of anisotropy.

### 🤖 AI 总结

**一句话总结**：本文通过几何分析研究语言Transformer中的各向异性现象，发现激活派生的切线方向能够捕获异常大的梯度能量和各向异性，为Transformer的几何解释提供实证支持。

**研究动机**：Transformer模型存在固有的各向异性问题，但现有理论研究缺乏对底层表征几何的有效支撑，需要从几何角度深入理解这一现象。

**核心方法**：作者在训练过程中采用基于概念的机械可解释性方法，将激活派生的低秩切线代理与反向传播的真实梯度进行对比测试，涵盖编码器和解码器风格的模型。

**主要结论**：激活派生的方向捕获了异常大的梯度能量和各向异性占比，显著高于匹配秩的正常对照，为各向异性的切线对齐理论提供了有力的实证支持。

**关键词**：各向异性, 语言模型, 梯度能量, 曲率可见性, 激活派生方向, 低秩代理, 频率偏差采样, 表示几何, 学习动力学

**评分**：12

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08764v1) | [下载PDF](https://arxiv.org/pdf/2604.08764v1.pdf)

---

## [6. LLMs Underperform Graph-Based Parsers on Supervised Relation Extraction for Complex Graphs](https://arxiv.org/abs/2604.08752v1)

**作者**：Paolo Gajo, Domenic Rosati, Hassan Sajjad 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-09

### 📄 论文摘要

Relation extraction represents a fundamental component in the process of creating knowledge graphs, among other applications. Large language models (LLMs) have been adopted as a promising tool for relation extraction, both in supervised and in-context learning settings. However, in this work we show that their performance still lags behind much smaller architectures when the linguistic graph underlying a text has great complexity. To demonstrate this, we evaluate four LLMs against a graph-based parser on six relation extraction datasets with sentence graphs of varying sizes and complexities. Our results show that the graph-based parser increasingly outperforms the LLMs, as the number of relations in the input documents increases. This makes the much lighter graph-based parser a superior choice in the presence of complex linguistic graphs.

### 🤖 AI 总结

**一句话总结**：在复杂语言图结构的关系抽取任务中，轻量级图解析器的性能显著优于大型语言模型（LLMs）。

**研究动机**：LLMs被广泛用于关系抽取任务，但其在处理复杂语言图结构时的实际表现尚不明确，需要系统性评估与传统图解析方法的差距。

**核心方法**：在六个关系抽取数据集上对四种LLMs与一个图解析器进行对比评估，数据集涵盖不同规模和复杂度的句子语言图，分析关系数量对模型性能的影响。

**主要结论**：随着输入文档中关系数量的增加，图解析器对LLMs的性能优势愈发明显，表明在复杂语言图场景下，轻量级图解析器是更优的选择。

**关键词**：关系抽取, 知识图谱, LLM, 图解析器, 监督学习, 上下文学习, 语言图复杂度, 模型对比, 信息抽取

**评分**：15

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08752v1) | [下载PDF](https://arxiv.org/pdf/2604.08752v1.pdf)

---

## [7. Decomposing the Delta: What Do Models Actually Learn from Preference Pairs?](https://arxiv.org/abs/2604.08723v1)

**作者**：Chia-Hsuan Lee, Mingyang Zhou, Renkun Ni 等 9 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-09

### 📄 论文摘要

Preference optimization methods such as DPO and KTO are widely used for aligning language models, yet little is understood about what properties of preference data drive downstream reasoning gains. We ask: what aspects of a preference pair improve a reasoning model's performance on general reasoning tasks? We investigate two distinct notions of quality delta in preference data: generator-level delta, arising from the differences in capability between models that generate chosen and rejected reasoning traces, and sample-level delta, arising from differences in judged quality differences within an individual preference pair. To study generator-level delta, we vary the generator's scale and model family, and to study sample-level delta, we employ an LLM-as-a-judge to rate the quality of generated traces along multiple reasoning-quality dimensions. We find that increasing generator-level delta steadily improves performance on out-of-domain reasoning tasks and filtering data by sample-level delta can enable more data-efficient training. Our results suggest a twofold recipe for improving reasoning performance through preference optimization: maximize generator-level delta when constructing preference pairs and exploit sample-level delta to select the most informative training examples.

### 🤖 AI 总结

**一句话总结**：研究揭示偏好优化中两类质量差异的作用：生成器层面的差异（不同能力模型生成的偏好对）越大越能提升推理性能，而样本层面的差异可用于高效筛选训练样本。

**研究动机**：尽管DPO和KTO等偏好优化方法广泛用于对齐语言模型，但学术界对偏好数据中哪些特性真正驱动下游推理能力提升的理解仍然不足。

**核心方法**：研究从两个维度分解偏好差异——生成器层面差异（通过改变生成模型的规模和家族来控制）以及样本层面差异（使用LLM评判器对每对偏好进行多维度质量评分），并系统性评估这些差异对分布外推理任务的影响。

**主要结论**：实验结果表明：（1）增加生成器层面的差异能稳定提升模型在分布外推理任务上的表现；（2）基于样本层面差异过滤数据可实现更高效的训练。最佳策略是构造偏好对时最大化生成器层面差异，并利用样本层面差异筛选最具信息量的训练样本。

**关键词**：偏好优化, 推理模型, 质量差异分解, 生成器级差异, 样本级差异, 语言模型对齐, 域外推理, 数据过滤, 训练效率

**评分**：14

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08723v1) | [下载PDF](https://arxiv.org/pdf/2604.08723v1.pdf)

---

## cs.CV

## [8. SenBen: Sensitive Scene Graphs for Explainable Content Moderation](https://arxiv.org/abs/2604.08819v1)

**作者**：Fatih Cagatay Akyon, Alptekin Temizel  
**分类**：cs.CV, cs.AI, cs.LG, cs.MM  
**发布时间**：2026-04-09

### 📄 论文摘要

Content moderation systems classify images as safe or unsafe but lack spatial grounding and interpretability: they cannot explain what sensitive behavior was detected, who is involved, or where it occurs. We introduce the Sensitive Benchmark (SenBen), the first large-scale scene graph benchmark for sensitive content, comprising 13,999 frames from 157 movies annotated with Visual Genome-style scene graphs (25 object classes, 28 attributes including affective states such as pain, fear, aggression, and distress, 14 predicates) and 16 sensitivity tags across 5 categories. We distill a frontier VLM into a compact 241M student model using a multi-task recipe that addresses vocabulary imbalance in autoregressive scene graph generation through suffix-based object identity, Vocabulary-Aware Recall (VAR) Loss, and a decoupled Query2Label tag head with asymmetric loss, yielding a +6.4 percentage point improvement in SenBen Recall over standard cross-entropy training. On grounded scene graph metrics, our student model outperforms all evaluated VLMs except Gemini models and all commercial safety APIs, while achieving the highest object detection and captioning scores across all models, at $7.6\times$ faster inference and $16\times$ less GPU memory.

### 🤖 AI 总结

**一句话总结**：本文提出SenBen首个敏感内容场景图基准数据集，并通过多任务蒸馏将前沿VLM压缩为241M学生模型，在场景图指标上超越大多数VLMs和商业安全API，同时推理速度提升7.6倍、显存占用减少16倍。

**研究动机**：现有内容审核系统缺乏空间可解释性，无法说明检测到何种敏感行为、涉及何人以及发生在何处，因此需要可解释的视觉内容审核方案。

**核心方法**：构建包含13,999帧电影画面的SenBen基准，采用后缀式对象身份、多任务VAR Loss解决词汇不平衡问题，以及解耦的Query2Label标签头进行知识蒸馏，训练出紧凑的241M学生模型。

**主要结论**：蒸馏模型在SenBen Recall上比标准交叉熵训练提升6.4个百分点，场景图指标超越除Gemini外的所有VLMs和商业安全API，且目标检测和描述得分最高，推理效率显著提升。

**关键词**：内容审核, 场景图生成, 多任务学习, 视觉语言模型, 敏感内容检测, 模型压缩, 知识蒸馏, 可解释AI

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08819v1) | [下载PDF](https://arxiv.org/pdf/2604.08819v1.pdf)

---

## [9. Towards Responsible Multimodal Medical Reasoning via Context-Aligned Vision-Language Models](https://arxiv.org/abs/2604.08815v1)

**作者**：Sumra Khan, Sagar Chhabriya, Aizan Zafar 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-09

### 📄 论文摘要

Medical vision-language models (VLMs) show strong performance on radiology tasks but often produce fluent yet weakly grounded conclusions due to over-reliance on a dominant modality. We introduce a context-aligned reasoning framework that enforces agreement across heterogeneous clinical evidence before generating diagnostic conclusions. The proposed approach augments a frozen VLM with structured contextual signals derived from radiomic statistics, explainability activations, and vocabulary-grounded semantic cues. Instead of producing free-form responses, the model generates structured outputs containing supporting evidence, uncertainty estimates, limitations, and safety notes. We observe that auxiliary signals alone provide limited benefit; performance gains emerge only when these signals are integrated through contextual verification. Experiments on chest X-ray datasets demonstrate that context alignment improves discriminative performance (AUC 0.918 to 0.925) while maintaining calibrated uncertainty. The framework also substantially reduces hallucinated keywords (1.14 to 0.25) and produces more concise reasoning explanations (19.4 to 15.3 words) without increasing model confidence (0.70 to 0.68). Cross-dataset evaluation on CheXpert further reveals that modality informativeness significantly influences reasoning behavior. These results suggest that enforcing multi-evidence agreement improves both reliability and trustworthiness in medical multimodal reasoning, while preserving the underlying model architecture.

### 🤖 AI 总结

**一句话总结**：本文提出上下文对齐推理框架，通过整合放射组学统计、可解释性激活和语义线索提升医学视觉-语言模型的可信度和推理质量。

**研究动机**：现有医学VLMs因过度依赖主导模态常产生流畅但缺乏依据的诊断结论，需要通过多证据验证来改善可靠性。

**核心方法**：框架冻结原有VLM并增加结构化上下文信号，生成包含证据、不确定性估计和安全性提示的结构化输出，而非自由形式响应。

**主要结论**：上下文对齐方法将AUC从0.918提升至0.925，幻觉关键词从1.14降至0.25，推理解释从19.4词缩短至15.3词，同时保持校准的不确定性。

**关键词**：视觉-语言模型, 上下文对齐推理, 医学多模态推理, 胸部X光, 放射组学, 不确定性估计, 结构化输出, 幻觉缓解, 多证据验证, 可解释性激活

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08815v1) | [下载PDF](https://arxiv.org/pdf/2604.08815v1.pdf)

---

## [10. R2G: A Multi-View Circuit Graph Benchmark Suite from RTL to GDSII](https://arxiv.org/abs/2604.08810v1)

**作者**：Zewei Zhou, Jiajun Zou, Jiajia Zhang 等 11 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-04-09

### 📄 论文摘要

Graph neural networks (GNNs) are increasingly applied to physical design tasks such as congestion prediction and wirelength estimation, yet progress is hindered by inconsistent circuit representations and the absence of controlled evaluation protocols. We present R2G (RTL-to-GDSII), a multi-view circuit-graph benchmark suite that standardizes five stage-aware views with information parity (every view encodes the same attribute set, differing only in where features attach) over 30 open-source IP cores (up to $10^6$ nodes/edges). R2G provides an end-to-end DEF-to-graph pipeline spanning synthesis, placement, and routing stages, together with loaders, unified splits, domain metrics, and reproducible baselines. By decoupling representation choice from model choice, R2G isolates a confound that prior EDA and graph-ML benchmarks leave uncontrolled. In systematic studies with GINE, GAT, and ResGatedGCN, we find: (i) view choice dominates model choice, with Test R$^2$ varying by more than 0.3 across representations for a fixed GNN; (ii) node-centric views generalize best across both placement and routing; and (iii) decoder-head depth (3--4 layers) is the primary accuracy driver, turning divergent training into near-perfect predictions (R$^2$$>$0.99). Code and datasets are available at https://github.com/ShenShan123/R2G.

### 🤖 AI 总结

**一句话总结**：R2G是一个统一的多视图电路图基准套件，通过标准化5种阶段感知视图和系统化评估协议，揭示了视图选择对GNN性能的决定性影响，并确立了节点中心视图和3-4层解码器头为最佳实践。

**研究动机**：当前GNN在物理设计任务中的应用受限于不一致的电路表示和缺乏标准化的评估协议，导致研究结果难以复现和比较。

**核心方法**：R2G提供涵盖综合、布局和布线阶段的标准五视图电路图（每个视图编码相同属性集，仅特征附着位置不同），基于30个开源IP核心构建，并通过GINE、GAT和ResGatedGCN模型进行系统化消融实验。

**主要结论**：研究发现视图选择对性能的影响超过模型选择（Test R²差异>0.3），节点中心视图跨布局和布线阶段泛化性最佳，3-4层解码器头深度是实现接近完美预测（R²>0.99）的关键因素。

**关键词**：R2G, Multi-View, Circuit, Graph, Benchmark, Suite, RTL, GDSII

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08810v1) | [下载PDF](https://arxiv.org/pdf/2604.08810v1.pdf)

---

## [11. State Space Models are Effective Sign Language Learners: Exploiting Phonological Compositionality for Vocabulary-Scale Recognition](https://arxiv.org/abs/2604.08761v1)

**作者**：Bryan Cheng, Austin Jin, Jasper Zhang  
**分类**：cs.CV  
**发布时间**：2026-04-09

### 📄 论文摘要

Sign language recognition suffers from catastrophic scaling failure: models achieving high accuracy on small vocabularies collapse at realistic sizes. Existing architectures treat signs as atomic visual patterns, learning flat representations that cannot exploit the compositional structure of sign languages-systematically organized from discrete phonological parameters (handshape, location, movement, orientation) reused across the vocabulary. We introduce PHONSSM, enforcing phonological decomposition through anatomically-grounded graph attention, explicit factorization into orthogonal subspaces, and prototypical classification enabling few-shot transfer. Using skeleton data alone on the largest ASL dataset ever assembled (5,565 signs), PHONSSM achieves 72.1% on WLASL2000 (+18.4pp over skeleton SOTA), surpassing most RGB methods without video input. Gains are most dramatic in the few-shot regime (+225% relative), and the model transfers zero-shot to ASL Citizen, exceeding supervised RGB baselines. The vocabulary scaling bottleneck is fundamentally a representation learning problem, solvable through compositional inductive biases mirroring linguistic structure.

### 🤖 AI 总结

**一句话总结**：PHONSSM通过状态空间模型结合手语 phonological 结构实现词汇级手语识别，在仅使用骨架数据的情况下于WLASL2000上达到72.1%准确率（+18.4pp），在小样本场景下提升225%。

**研究动机**：现有模型将手势视为原子视觉模式，无法利用手语的组合性结构，导致在真实规模词汇量下出现灾难性失效。

**核心方法**：PHONSSM采用解剖学约束的图注意力机制、正交子空间分解和原型分类，实现 phonological 解耦，使模型能够复用离散参数（手形、位置、运动、方向）处理大规模词汇。

**主要结论**：通过镜像语言结构的组合归纳偏置解决词汇缩放瓶颈，模型在骨架数据上超越大多数RGB方法，并实现零样本迁移，验证了组合性表示学习是手语识别规模化的关键。

**关键词**：State, Space, Models, Effective, Sign, Language, Learners, Exploiting

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08761v1) | [下载PDF](https://arxiv.org/pdf/2604.08761v1.pdf)

---

## [12. SIC3D: Style Image Conditioned Text-to-3D Gaussian Splatting Generation](https://arxiv.org/abs/2604.08760v1)

**作者**：Ming He, Zhixiang Chen, Steve Maddock  
**分类**：cs.CV  
**发布时间**：2026-04-09

### 📄 论文摘要

Recent progress in text-to-3D object generation enables the synthesis of detailed geometry from text input by leveraging 2D diffusion models and differentiable 3D representations. However, the approaches often suffer from limited controllability and texture ambiguity due to the limitation of the text modality. To address this, we present SIC3D, a controllable image-conditioned text-to-3D generation pipeline with 3D Gaussian Splatting (3DGS). There are two stages in SIC3D. The first stage generates the 3D object content from text with a text-to-3DGS generation model. The second stage transfers style from a reference image to the 3DGS. Within this stylization stage, we introduce a novel Variational Stylized Score Distillation (VSSD) loss to effectively capture both global and local texture patterns while mitigating conflicts between geometry and appearance. A scaling regularization is further applied to prevent the emergence of artifacts and preserve the pattern from the style image. Extensive experiments demonstrate that SIC3D enhances geometric fidelity and style adherence, outperforming prior approaches in both qualitative and quantitative evaluations.

### 🤖 AI 总结

**一句话总结**：SIC3D是一个基于3D Gaussian Splatting的图像条件文本到3D生成管道，通过两阶段方法实现可控制的3D对象生成和风格迁移。

**研究动机**：现有文本到3D生成方法受文本模态限制，存在可控性不足和纹理歧义问题，需要更强的控制能力和更精确的纹理生成能力。

**核心方法**：采用两阶段pipeline：第一阶段利用文本生成3DGS内容，第二阶段通过创新的VSSD（变分风格化分数蒸馏）损失函数进行风格迁移，并引入缩放正则化防止伪影同时保留风格图像的纹理模式。

**主要结论**：实验结果表明SIC3D在几何保真度和风格一致性方面显著增强，在定性和定量评估中均优于现有方法。

**关键词**：SIC3D, Style, Image, Conditioned, Text-to-3D, Gaussian, Splatting, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08760v1) | [下载PDF](https://arxiv.org/pdf/2604.08760v1.pdf)

---

## [13. LPLCv2: An Expanded Dataset for Fine-Grained License Plate Legibility Classification](https://arxiv.org/abs/2604.08741v1)

**作者**：Lucas Wojcik, Eduardo A. F. Machoski, Eduil Nascimento 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-09

### 📄 论文摘要

Modern Automatic License Plate Recognition (ALPR) systems achieve outstanding performance in controlled, well-defined scenarios. However, large-scale real-world usage remains challenging due to low-quality imaging devices, compression artifacts, and suboptimal camera installation. Identifying illegible license plates (LPs) has recently become feasible through a dedicated benchmark; however, its impact has been limited by its small size and annotation errors. In this work, we expand the original benchmark to over three times the size with two extra capture days, revise its annotations and introduce novel labels. LP-level annotations include bounding boxes, text, and legibility level, while vehicle-level annotations comprise make, model, type, and color. Image-level annotations feature camera identity, capture conditions (e.g., rain and faulty cameras), acquisition time, and day ID. We present a novel training procedure featuring an Exponential Moving Average-based loss function and a refined learning rate scheduler, addressing common mistakes in testing. These improvements enable a baseline model to achieve an 89.5% F1-score on the test set, considerably surpassing the previous state of the art. We further introduce a novel protocol to explicitly addresses camera contamination between training and evaluation splits, where results show a small impact. Dataset and code are publicly available at https://github.com/lmlwojcik/LPLCv2-Dataset.

### 🤖 AI 总结

**一句话总结**：本文将车牌可读性分类数据集LPLC扩展至原来的3倍以上，并提出基于EMA损失函数的新训练方法，使模型F1分数达到89.5%，显著超越之前的最优水平。

**研究动机**：现有车牌识别系统在真实场景中受限于低质量图像和压缩伪影，而已有可读性基准数据集规模小、存在标注错误，影响了系统实际部署效果。

**核心方法**：通过扩展数据集规模、重修订标注、引入多层注解（车牌/车辆/图像级），并设计基于指数移动平均的损失函数和优化的学习率调度器改进训练流程。

**主要结论**：改进后的基线模型在测试集达到89.5%的F1分数，性能大幅提升，同时引入新协议评估训练测试集间的摄像头污染影响，结果显示影响较小。

**关键词**：车牌识别系统, 细粒度图像分类, 目标检测基准, 低质量图像识别, 车辆属性识别, 智能交通监控, 深度学习训练策略, 多标签标注数据集, 指数移动平均, 学习率调度器

**评分**：12

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08741v1) | [下载PDF](https://arxiv.org/pdf/2604.08741v1.pdf)

---

## [14. LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving](https://arxiv.org/abs/2604.08719v1)

**作者**：Hao Shao, Letian Wang, Yang Zhou 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.RO  
**发布时间**：2026-04-09

### 📄 论文摘要

Recent years have seen remarkable progress in autonomous driving, yet generalization to long-tail and open-world scenarios remains a major bottleneck for large-scale deployment. To address this challenge, some works use LLMs and VLMs for vision-language understanding and reasoning, enabling vehicles to interpret rare and safety-critical situations when generating actions. Others study generative world models to capture the spatio-temporal evolution of driving scenes, allowing agents to imagine possible futures before acting. Inspired by human intelligence, which unifies understanding and imagination, we explore a unified model for autonomous driving. We present LMGenDrive, the first framework that combines LLM-based multimodal understanding with generative world models for end-to-end closed-loop driving. Given multi-view camera inputs and natural-language instructions, LMGenDrive generates both future driving videos and control signals. This design provides complementary benefits: video prediction improves spatio-temporal scene modeling, while the LLM contributes strong semantic priors and instruction grounding from large-scale pretraining. We further propose a progressive three-stage training strategy, from vision pretraining to multi-step long-horizon driving, to improve stability and performance. LMGenDrive supports both low-latency online planning and autoregressive offline video generation. Experiments show that it significantly outperforms prior methods on challenging closed-loop benchmarks, with clear gains in instruction following, spatio-temporal understanding, and robustness to rare scenarios. These results suggest that unifying multimodal understanding and generation is a promising direction for more generalizable and robust embodied decision-making systems.

### 🤖 AI 总结

**一句话总结**：LMGenDrive是首个统一LLM多模态理解与生成式世界模型的端到端自动驾驶框架，可同时生成未来驾驶视频和控制信号。

**研究动机**：当前自动驾驶系统在泛化到长尾和开放世界场景时存在瓶颈，现有方法要么侧重视觉语言理解与推理，要么仅关注生成式世界模型，但人类智能统一了理解与想象能力。

**核心方法**：LMGenDrive接收多视角相机输入和自然语言指令，通过三阶段渐进式训练策略（视觉预训练、多步长视野驾驶训练），同时实现视频预测和动作控制生成，充分利用LLM的语义先验和世界模型的空间时间建模能力。

**主要结论**：实验表明LMGenDrive在闭环基准测试中显著优于先前方法，在指令遵循、时空理解和罕见场景鲁棒性方面均有明显提升，验证了统一多模态理解与生成是实现更通用、鲁棒具身决策系统的有效方向。

**关键词**：自动驾驶, 端到端驾驶, 生成式世界模型, 闭环驾驶, 视频预测, LLM, 长尾场景, 时空建模, 指令跟随, 多视角感知, 具身决策

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08719v1) | [下载PDF](https://arxiv.org/pdf/2604.08719v1.pdf)

---

## [15. Accelerating Transformer-Based Monocular SLAM via Geometric Utility Scoring](https://arxiv.org/abs/2604.08718v2)

**作者**：Xinmiao Xiong, Bangya Liu, Hao Wang 等 10 位作者  
**分类**：cs.CV, cs.AI, cs.RO  
**发布时间**：2026-04-09

### 📄 论文摘要

Geometric Foundation Models (GFMs) have recently advanced monocular SLAM by providing robust, calibration-free 3D priors. However, deploying these models on dense video streams introduces significant computational redundancy. Current GFM-based SLAM systems typically rely on post hoc keyframe selection. Because of this, they must perform expensive dense geometric decoding simply to determine whether a frame contains novel geometry, resulting in late rejection and wasted computation. To mitigate this inefficiency, we propose LeanGate, a lightweight feed-forward frame-gating network. LeanGate predicts a geometric utility score to assess a frame's mapping value prior to the heavy GFM feature extraction and matching stages. As a predictive plug-and-play module, our approach bypasses over 90% of redundant frames. Evaluations on standard SLAM benchmarks demonstrate that LeanGate reduces tracking FLOPs by more than 85% and achieves a 5x end-to-end throughput speedup. Furthermore, it maintains the tracking and mapping accuracy of dense baselines. Project page: https://lean-gate.github.io/

### 🤖 AI 总结

**一句话总结**：本文提出LeanGate，一种轻量级前馈帧门控网络，通过预测几何效用评分在GFM特征提取前过滤冗余帧，实现超过90%冗余帧的跳过和5倍端到端吞吐量提升。

**研究动机**：当前基于几何基础模型的单目SLAM系统在处理密集视频流时存在严重计算冗余，因为必须在完成昂贵的密集几何解码后才能判断帧是否包含新几何信息，导致大量无效计算。

**核心方法**：LeanGate作为即插即用的预测模块，在GFM特征提取和匹配之前预测每帧的映射价值（几何效用评分），通过轻量级前馈网络筛选高价值帧，从而跳过约90%的冗余帧。

**主要结论**：在标准SLAM基准测试中，LeanGate将跟踪FLOPs降低超过85%，达到5倍端到端吞吐量加速，同时保持与密集基线相当的跟踪和建图精度。

**关键词**：Accelerating, Transformer-Based, Monocular, SLAM, via, Geometric, Utility, Scoring

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08718v2) | [下载PDF](https://arxiv.org/pdf/2604.08718v2.pdf)

---

## [16. What Matters in Virtual Try-Off? Dual-UNet Diffusion Model For Garment Reconstruction](https://arxiv.org/abs/2604.08716v1)

**作者**：Loc-Phat Truong, Meysam Madadi, Sergio Escalera  
**分类**：cs.CV  
**发布时间**：2026-04-09

### 📄 论文摘要

Virtual Try-On (VTON) has seen rapid advancements, providing a strong foundation for generative fashion tasks. However, the inverse problem, Virtual Try-Off (VTOFF)-aimed at reconstructing the canonical garment from a draped-on image-remains a less understood domain, distinct from the heavily researched field of VTON. In this work, we seek to establish a robust architectural foundation for VTOFF by studying and adapting various diffusion-based strategies from VTON and general Latent Diffusion Models (LDMs). We focus our investigation on the Dual-UNet Diffusion Model architecture and analyze three axes of design: (i) Generation Backbone: comparing Stable Diffusion variants; (ii) Conditioning: ablating different mask designs, masked/unmasked inputs for image conditioning, and the utility of high-level semantic features; and (iii) Losses and Training Strategies: evaluating the impact of the auxiliary attention-based loss, perceptual objectives and multi-stage curriculum schedules. Extensive experiments reveal trade-offs across various configuration options. Evaluated on VITON-HD and DressCode datasets, our framework achieves state-of-the-art performance with a drop of 9.5\% on the primary metric DISTS and competitive performance on LPIPS, FID, KID, and SSIM, providing both stronger baselines and insights to guide future Virtual Try-Off research.

### 🤖 AI 总结

**一句话总结**：本文提出Dual-UNet扩散模型用于虚拟脱衣（VTOFF）任务中的服装重建，通过三个维度的系统性消融实验建立了VTOFF的鲁棒架构基础，在DISTS指标上较SOTA降低9.5%。

**研究动机**：虚拟试衣（VTON）研究广泛，但逆向任务——虚拟脱衣（VTOFF，从穿着图像重建标准服装）——研究较少，该工作旨在填补这一空白并建立该领域的基础架构框架。

**核心方法**：基于Dual-UNet扩散模型架构，从生成主干（Stable Diffusion变体）、条件输入（mask设计、图像条件化、高层语义特征）和训练策略（注意力损失、感知损失、多阶段课程）三个轴进行系统性消融实验。

**主要结论**：实验揭示了不同配置选项间的权衡，模型在VITON-HD和DressCode数据集上实现SOTA性能（DISTS降低9.5%），LPIPS、FID、KID、SSIM等指标也具有竞争力，为未来VTOFF研究提供了强基线和设计指南。

**关键词**：What, Matters, Virtual, Try-Off?, Dual-UNet, Diffusion, Model, Garment

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08716v1) | [下载PDF](https://arxiv.org/pdf/2604.08716v1.pdf)

---

## [17. RS-OVC: Open-Vocabulary Counting for Remote-Sensing Data](https://arxiv.org/abs/2604.08704v1)

**作者**：Tamir Shor, George Leifman, Genady Beryozkin  
**分类**：cs.CV  
**发布时间**：2026-04-09

### 📄 论文摘要

Object-Counting for remote-sensing (RS) imagery is attracting increasing research interest due to its crucial role in a wide and diverse set of applications. While several promising methods for RS object-counting have been proposed, existing methods focus on a closed, pre-defined set of object classes. This limitation necessitates costly re-annotation and model re-training to adapt current approaches for counting of novel objects that have not been seen during training, and severely inhibits their application in dynamic, real-world monitoring scenarios. To address this gap, in this work we propose RS-OVC - the first Open Vocabulary Counting (OVC) model for Remote-Sensing and aerial imagery. We show that our model is capable of accurate counting of novel object classes, that were unseen during training, based solely on textual and/or visual conditioning.

### 🤖 AI 总结

**一句话总结**：RS-OVC是首个面向遥感图像的开放词汇计数模型，能够对训练时未见过的物体类别进行准确计数。

**研究动机**：现有遥感目标计数方法局限于预定义的封闭类别集合，扩展到新类别需重新标注和训练，成本高昂且限制了在动态监测场景中的应用。

**核心方法**：提出RS-OVC模型，利用文本和/或视觉条件作为输入条件，实现开放词汇计数能力，这是首个针对遥感及航拍图像设计的开放词汇计数方法。

**主要结论**：实验验证了RS-OVC能够准确计数训练时未见过的物体类别，仅依靠文本或视觉条件即可实现良好的泛化效果。

**关键词**：开放词汇计数, 遥感图像, 目标检测, 零样本学习, 多模态学习, 航空影像, 视觉语言模型, 开放集识别, 实时监测, 深度学习

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08704v1) | [下载PDF](https://arxiv.org/pdf/2604.08704v1.pdf)

---

## [18. Unified Multimodal Uncertain Inference](https://arxiv.org/abs/2604.08701v2)

**作者**：Dengjia Zhang, Alexander Martin, William Jurayj 等 6 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-04-09

### 📄 论文摘要

We introduce Unified Multimodal Uncertain Inference (UMUI), a multimodal inference task spanning text, audio, and video, where models must produce calibrated probability estimates of hypotheses conditioned on a premise in any modality or combination. While uncertain inference has been explored in text, extension to other modalities has been limited to single-modality binary entailment judgments, leaving no framework for fine-grained probabilistic reasoning in or across other modalities. To address this, we curate a human-annotated evaluation set with scalar probability judgments across audio, visual, and audiovisual settings, and additionally evaluate on existing text and audio benchmarks. We introduce CLUE (Calibrated Latent Uncertainty Estimation), which combines self-consistent teacher calibration and distribution-based confidence probing to produce calibrated predictions. We demonstrate that our 3B-parameter model achieves equivalent or stronger performance than baselines up to 32B parameters across all modalities.

### 🤖 AI 总结

**一句话总结**：UMUI提出统一的多模态不确定推理框架，使模型能跨文本、音频、视频模态产生校准的概率估计。

**研究动机**：现有不确定推理研究局限于文本模态，多模态场景缺乏细粒度概率推理框架，无法支持跨模态条件概率估计。

**核心方法**：提出CLUE方法结合教师校准和分布置信探测，并构建音频、视频等多模态人类标注评估集。

**主要结论**：3B参数模型在所有模态上达到或超越32B参数基线性能，验证了小模型也能实现精准的概率校准推理。

**关键词**：多模态推理, 不确定性推理, 概率校准, 置信度估计, 参数高效, 教师校准, 概率估计, 模态融合

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08701v2) | [下载PDF](https://arxiv.org/pdf/2604.08701v2.pdf)

---

## [19. Multi-Frequency Local Plasticity for Visual Representation Learning](https://arxiv.org/abs/2604.09734v1)

**作者**：Mehdi Fatan Serj, C. Alejandro Parraga, Xavier Otazu  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-09

### 📄 论文摘要

We study how far structured architectural bias can compensate for the absence of end-to-end gradient-based representation learning in visual recognition. Building on the VisNet tradition, we introduce a modular hierarchical framework combining: (i) fixed multi-frequency Gabor decomposition into F=7 parallel streams; (ii) within-stream competitive learning with Hebbian and Oja updates and anti-Hebbian decorrelation; (iii) an associative memory module inspired by modern Hopfield retrieval; and (iv) iterative top-down modulation using local prediction and reconstruction signals.   Representational layers are trained without end-to-end backpropagation through the full hierarchy; only the final linear readout and top-down projection matrices are optimized by gradient descent. We therefore interpret the model as a hybrid system that is predominantly locally trained but includes a small number of gradient-trained parameters.   On CIFAR-10, the full model reaches 80.1% +/- 0.3% top-1 accuracy, linear probe), compared with 71.0% for a Hebbian-only baseline and 83.4% for a gradient-trained model on the same fixed Gabor basis. On CIFAR-100, performance is 54.8%. Factorial analysis indicates that multi-frequency streams, associative memory, and top-down feedback contribute largely additively, with a significant Streams x TopDown interaction (p=0.02).   These results suggest that carefully chosen architectural priors can recover a substantial fraction of the performance typically associated with global gradient training, while leaving a measurable residual gap. Experiments are limited to CIFAR-10/100.

### 🤖 AI 总结

**一句话总结**：本文提出一种混合视觉表示学习框架，结合固定Gabor滤波、局部可塑性（Hebbian/Oja学习）和Hopfield联想记忆，无需端到端反向传播即可在CIFAR-10上达到80.1%准确率。

**研究动机**：研究如何通过精心设计的结构化架构先验来补偿端到端梯度学习的缺失，探索生物启发的局部学习机制在视觉识别中的潜力。

**核心方法**：构建模块化层次框架：(i) 固定7通道多频Gabor分解；(ii) 通道内Hebbian/Oja竞争学习与反Hebbian去相关；(iii) 现代Hopfield启发的联想记忆模块；(iv) 基于局部预测-重建信号的迭代反馈调制。仅对最后线性读出层和反馈投影矩阵使用梯度优化。

**主要结论**：消融实验表明多频通道、联想记忆和反馈调制具有近似加性贡献，各组件协同可恢复梯度训练性能的绝大部分（CIFAR-10: 80.1% vs 83.4%），但仍存在可测量的性能差距，证明架构先验的价值但也揭示其局限性。

**关键词**：多频率Gabor分解, 联想记忆网络, 局部可塑性, 视觉表示学习, 竞争学习, 自上而下调制, 混合训练, 图像识别

**评分**：10

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09734v1) | [下载PDF](https://arxiv.org/pdf/2604.09734v1.pdf)

---

## cs.LG

## [20. HiFloat4 Format for Language Model Pre-training on Ascend NPUs](https://arxiv.org/abs/2604.08826v1)

**作者**：Mehran Taghian, Yunke Peng, Xing Huang 等 25 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-04-09

### 📄 论文摘要

Large foundation models have become central to modern machine learning, with performance scaling predictably with model size and data. However, training and deploying such models incur substantial computational and memory costs, motivating the development of low-precision training techniques. Recent work has demonstrated that 4-bit floating-point (FP4) formats--such as MXFP4 and NVFP4--can be successfully applied to linear GEMM operations in large language models (LLMs), achieving up to 4x improvements in compute throughput and memory efficiency compared to higher-precision baselines. In this work, we investigate the recently proposed HiFloat4 FP4 format for Huawei Ascend NPUs and systematically compare it with MXFP4 in large-scale training settings. All experiments are conducted on Ascend NPU clusters, with linear and expert GEMM operations performed entirely in FP4 precision. We evaluate both dense architectures (e.g., Pangu and LLaMA-style models) and mixture-of-experts (MoE) models, where both standard linear layers and expert-specific GEMMs operate in FP4. Furthermore, we explore stabilization techniques tailored to FP4 training that significantly reduce numerical degradation, maintaining relative error within 1% of full-precision baselines while preserving the efficiency benefits of 4-bit computation. Our results provide a comprehensive empirical study of FP4 training on NPUs and highlight the practical trade-offs between FP4 formats in large-scale dense and MoE models.

### 🤖 AI 总结

**一句话总结**：本文在华为Ascend NPUs上验证了HiFloat4 FP4格式用于大语言模型预训练的有效性，在保持误差低于1%的前提下显著提升计算效率。

**研究动机**：大模型训练面临高计算和内存成本问题，FP4格式（如MXFP4、NVFP4）已被证明能提升LLM线性GEMM操作的效率，但需针对华为Ascend NPUs进行系统评估。

**核心方法**：在Ascend NPU集群上进行大规模实验，对比HiFloat4与MXFP4格式在密集模型（Pangu、LLaMA）和MoE模型上的表现，采用针对性FP4稳定化技术，并让线性层和专家GEMM均以FP4精度运行。

**主要结论**：HiFloat4格式能有效支持大规模FP4训练，在密集和MoE架构中维持相对误差在1%以内，同时保留4位计算的效率优势，为Ascend NPU上的FP4训练提供了实践指导。

**关键词**：FP4训练, LLM, 混合专家, 低精度训练, 数值稳定性, HiFloat4, Format, Language

**评分**：15

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08826v1) | [下载PDF](https://arxiv.org/pdf/2604.08826v1.pdf)

---

## [21. Loom: A Scalable Analytical Neural Computer Architecture](https://arxiv.org/abs/2604.08816v1)

**作者**：Mehmet Kerem Turkcan  
**分类**：cs.LG  
**发布时间**：2026-04-09

### 📄 论文摘要

We present Loom, a computer architecture that executes programs compiled from C inside a looped transformer whose weights are derived analytically. The architecture implements a 22-opcode instruction set in 8 transformer layers. Each forward pass executes one instruction; the model is applied iteratively until the program counter reaches zero. The full machine state resides in a single tensor $X \in \mathbb{R}^{d \times n}$ of fixed size, and every step has fixed cost for fixed $d$ and $n$, independent of program length or execution history. The default configuration uses $d = 155$ and $n = 1024$, yielding 4.7 million parameters and 928 instruction slots. A compact configuration at $d = 146$ and $n = 512$ suffices for a 9$\times$9 Sudoku solver (284 instructions). The weights are program-independent: programs live in the state tensor, and the same fixed-weight model executes any compiled program. We make Loom source code publicly available at https://github.com/mkturkcan/Loom.

### 🤖 AI 总结

**一句话总结**：Loom是一种可扩展的分析型神经计算机架构，通过循环transformer执行编译自C语言的程序，在8层transformer中实现22条指令集，全机状态存储在固定大小的单一张量中，权重与程序无关。

**研究动机**：传统神经计算机面临可扩展性挑战和程序依赖性问题，需要一种能够在固定资源下独立执行任意程序的新架构方案。

**核心方法**：Loom在8层transformer中实现22条opcode指令集，全机状态存储在单个张量X中，通过迭代应用模型直到程序计数器为零，所有权重程序独立，可执行任意编译后的程序。

**主要结论**：默认配置(d=155, n=1024)仅有470万参数和928个指令槽，紧凑配置(d=146, n=512)即可解决9×9数独问题(284条指令)，证明了该架构的有效性和可扩展性。

**关键词**：神经计算机, 指令集架构, 程序无关权重, 固定成本执行, 迭代执行, C语言编译, 可微计算, Loom

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08816v1) | [下载PDF](https://arxiv.org/pdf/2604.08816v1.pdf)

---

## [22. Structural Evaluation Metrics for SVG Generation via Leave-One-Out Analysis](https://arxiv.org/abs/2604.08809v1)

**作者**：Haonan Zhu, Adrienne Deganutti, Elad Hirsch 等 4 位作者  
**分类**：cs.LG, stat.AP  
**发布时间**：2026-04-09

### 📄 论文摘要

Scalable Vector Graphics (SVG) represent visual content as structured, editable code. Each element (path, shape, or text node) can be individually inspected, transformed, or removed. This structural editability is a main motivation for SVG generation, yet prevailing evaluation protocols primarily reduce the output to a single similarity score against a reference image or input texts, measuring how faithfully the result reproduces an image or follows the instructions, but not how well it preserves the structural properties that make SVG valuable. In particular, existing metrics cannot determine which generated elements contribute positively to overall visual quality, how visual concepts map to specific parts of the code, or whether the generated output supports meaningful downstream editing. We introduce element-level leave-one-out (LOO) analysis, inspired by the classic jackknife estimator. The procedure renders the SVG with and without each element, measures the resulting visual change, and derives a suite of structural quality metrics. Despite its simplicity, the jackknife's capacity to decompose an aggregate statistic into per-sample contributions translates directly to this setting. From a single mechanism, we obtain: (1) quality scores per element through LOO scoring that enable zero-shot artifact detection; (2) concept-element attribution that maps each element to the visual concept it serves; and (3) four structural metrics, purity, coverage, compactness, and locality, that quantify SVG modularity from complementary perspectives. We validate these metrics on over 19,000 edits (5 types) across 5 generation systems and 3 complexity tiers.

### 🤖 AI 总结

**一句话总结**：提出基于留一法的元素级分析框架，通过渲染SVG时移除各元素并测量视觉变化来评估SVG生成的结构质量，提供元素评分、概念归因和四项结构化指标。

**研究动机**：现有SVG评估指标仅关注整体相似度，无法评估SVG的结构可编辑性优势，也无法识别哪些生成元素真正贡献视觉质量或支持下游编辑任务。

**核心方法**：采用jackknife估计器启发的留一法（LOO）分析，对比渲染带/不带每个元素的SVG视觉差异，派生元素级质量评分，并通过单一机制同时获取概念-元素归因和四项结构指标（纯度、覆盖率、紧凑性、局部性）。

**主要结论**：在19000+次编辑实验（5种类型、5个生成系统、3个复杂度层级）中验证了该方法的有效性，成功实现了零样本伪影检测、视觉概念归因和SVG模块化的多维量化评估。

**关键词**：Structural, Evaluation, Metrics, SVG, Generation, via, Leave-One-Out, Analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08809v1) | [下载PDF](https://arxiv.org/pdf/2604.08809v1.pdf)

---

## [23. Smartwatch-Based Sitting Time Estimation in Real-World Office Settings](https://arxiv.org/abs/2604.08808v1)

**作者**：Olivia Zhang, Zhilin Zhang  
**分类**：cs.LG, cs.HC  
**发布时间**：2026-04-09

### 📄 论文摘要

Sedentary behavior poses a major public health risk, being strongly linked to obesity, cardiovascular disease, and other chronic conditions. Accurately estimating sitting time is therefore critical for monitoring and improving individual health. This work addresses the problem in real-world office settings, where signals from the inertial measurement units (IMU) on a smartwatch were collected from office workers during their daily routines. We propose a method that estimates sitting time from the IMU signals by introducing the use of rotation vector sequences, derived from Euler angles, as a novel representation of movement dynamics. Experiments on a 34-hour dataset demonstrate that exploiting rotation vector sequences improves algorithm performance, highlighting their potential for robust sitting time estimation in natural environments.

### 🤖 AI 总结

**一句话总结**：提出利用智能手表IMU传感器数据中的旋转矢量序列来估计办公室环境中的久坐时间，在34小时数据集上验证了方法的有效性。

**研究动机**：久坐行为是肥胖、心血管疾病等慢性病的重要风险因素，因此需要精准估计坐姿时间以便监测和改善个体健康。

**核心方法**：从智能手表的惯性测量单元采集数据，将欧拉角导出的旋转矢量序列作为运动动态的新型表示特征，用于训练分类模型以估计坐姿时间。

**主要结论**：实验结果表明，旋转矢量序列特征能够提升算法性能，证明了其在自然环境中进行稳健久坐时间估计的潜力。

**关键词**：久坐估计, 办公室场景, 姿态识别, 健康监测, 可穿戴设备, 人体活动识别, Smartwatch-Based, Sitting

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08808v1) | [下载PDF](https://arxiv.org/pdf/2604.08808v1.pdf)

---

## [24. STaR-DRO: Stateful Tsallis Reweighting for Group-Robust Structured Prediction](https://arxiv.org/abs/2604.09737v1)

**作者**：Samah Fodeh, Ganesh Puthiaraju, Elyas Irankhah 等 9 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-09

### 📄 论文摘要

Structured prediction requires models to generate ontology-constrained labels, grounded evidence, and valid structure under ambiguity, label skew, and heterogeneous group difficulty. We present a two-part framework for controllable inference and robust fine-tuning. First, we introduce a task-agnostic prompting strategy that combines XML-based instruction structure, disambiguation rules, verification-style reasoning, schema constraints, and self-validation to address format drift, label ambiguity, evidence hallucination, and metadata-conditioned confusion in in-context structured generation. Second, we introduce STaR-DRO, a stateful robust optimization method for group heterogeneity. It combines Tsallis mirror descent with momentum-smoothed, centered group-loss signals and bounded excess-only multipliers so that only persistently hard groups above a neutral baseline are upweighted, concentrating learning where it is most needed while avoiding volatile, dense exponentiated-gradient reweighting and unnecessary loss from downweighting easier groups. We evaluate the combined framework on EPPC Miner, a benchmark for extracting hierarchical labels and evidence spans from patient-provider secure messages. Prompt engineering improves zero-shot by +15.44 average F1 across Code, Sub-code, and Span over four Llama models. Building on supervised fine-tuning, STaR-DRO further improves the hardest semantic decisions: on Llama-3.3-70B-Instruct, Code F1 rises from 79.24 to 81.47 and Sub-code F1 from 67.78 to 69.30, while preserving Span performance and reducing group-wise validation cross-entropy by up to 29.6% on the most difficult clinical categories. Because these rare and difficult groups correspond to clinically consequential communication behaviors, these gains are not merely statistical improvements: they directly strengthen communication mining reliability for patient-centered care analysis.

### 🤖 AI 总结

**一句话总结**：本文提出STaR-DRO框架，通过结合XML结构化提示策略与Tsallis镜面下降重加权方法，实现对医疗文本中困难群体的鲁棒结构化预测，在Llama模型上显著提升Code和Sub-code的F1分数。

**研究动机**：结构化预测面临格式漂移、标签歧义、证据幻觉及异构群体难度差异等挑战，尤其在医学文本提取中，某些临床类别因样本稀少而难以学习，需要针对性方法提升模型在困难群体上的表现。

**核心方法**：框架包含两部分：1) XML结构化提示策略，集成消歧规则、验证式推理和自验证机制；2) STaR-DRO方法，采用Tsallis镜面下降配合动量平滑的居中组损失信号，仅对持续困难的群体进行加权，避免对简单群体的不必要降权。

**主要结论**：在EPPC Miner基准测试中，提示工程使零样本性能提升15.44点平均F1；STaR-DRO在Llama-3.3-70B-Instruct上将Code F1从79.24提升至81.47，Sub-code F1从67.78提升至69.30，最困难临床类别的验证交叉熵降低29.6%，直接增强了患者护理分析的可靠性。

**关键词**：群体鲁棒优化, 结构化预测, 提示工程, 医疗通信挖掘, 分层标签提取, 证据跨度提取, 自验证, 动量平滑, 组损失信号, 临床文本

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09737v1) | [下载PDF](https://arxiv.org/pdf/2604.09737v1.pdf)

---

## [25. Adaptive Simulation Experiment for LLM Policy Optimization](https://arxiv.org/abs/2604.08779v1)

**作者**：Mingjie Hu, Siyang Gao, Jian-qiang Hu 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-09

### 📄 论文摘要

Large language models (LLMs) have significant potential to improve operational efficiency in operations management. Deploying these models requires specifying a policy that governs response quality, shapes user experience, and influences operational value. In this research, we treat LLMs as stochastic simulators and propose a pairwise comparison-based adaptive simulation experiment framework for identifying the optimal policy from a finite set of candidates. We consider two policy spaces: an unstructured space with no parametric assumption, and a structured space in which the data are generated from a preference model. For both settings, we characterize the fundamental data requirements for identifying the optimal policy with high probability. In the unstructured case, we derive a closed-form expression for the optimal sampling proportions, together with a clear operational interpretation. In the structured case, we formulate a regularized convex program to compute the optimal proportions. We then develop an adaptive experimental procedure, termed LLM-PO, for both policy spaces, and prove that it identifies the optimal policy with the desired statistical guarantee while asymptotically attaining the fundamental data requirements. Numerical experiments demonstrate that LLM-PO consistently outperforms benchmark methods and improves LLM performance.

### 🤖 AI 总结

**一句话总结**：提出LLM-PO自适应实验框架，通过成对比较在无结构和结构化两种策略空间中识别最优LLM策略，具有统计保证和渐近最优性。

**研究动机**：LLM在运营管理中具有提升效率的潜力，但部署时需要指定治理响应质量、塑造用户体验的策略，从有限候选策略中识别最优策略是关键挑战。

**核心方法**：将LLM视为随机模拟器，提出基于成对比较的自适应实验框架；无结构空间推导闭式最优采样比例，结构化空间提出正则化凸规划求解，通过LLM-PO算法实现自适应策略优化。

**主要结论**：LLM-PO算法在理论上保证识别最优策略并渐近达到数据需求下界，数值实验表明其性能一致优于基准方法，有效提升LLM应用表现。

**关键词**：LLM, Adaptive, Simulation, Experiment, Policy, Optimization, Large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08779v1) | [下载PDF](https://arxiv.org/pdf/2604.08779v1.pdf)

---

## [26. Adversarial Sensor Errors for Safe and Robust Wind Turbine Fleet Control](https://arxiv.org/abs/2604.08750v1)

**作者**：Julian Quick, Marcus Binder Nilsen, Andreas Bechmann 等 5 位作者  
**分类**：cs.LG, eess.SY  
**发布时间**：2026-04-09

### 📄 论文摘要

Plant-level control is an emerging wind energy technology that presents opportunities and challenges. By controlling turbines in a coordinated manner via a central controller, it is possible to achieve greater wind power plant efficiency. However, there is a risk that measurement errors will confound the process, or even that hackers will alter the telemetry signals received by the central controller. This paper presents a framework for developing a safe plant controller by training it with an adversarial agent designed to confound it. This necessitates training the adversary to confound the controller, creating a sort of circular logic or "Arms Race." This paper examines three broad training approaches for co-training the protagonist and adversary, finding that an Arms Race approach yields the best results. These initial results indicate that the Arms Race adversarial training reduced worst-case performance degradation from 39% power loss to 7.9% power gain relative to a baseline operational strategy.

### 🤖 AI 总结

**一句话总结**：提出一种对抗性训练框架，通过'军备竞赛'式的协同训练，使风电场中央控制器能够抵御传感器测量误差或恶意攻击，显著提升鲁棒性。

**研究动机**：风电场植物级控制依赖中央控制器协调各涡轮机，但测量误差或黑客篡改遥测信号可能严重干扰控制效果，存在重大安全隐患。

**核心方法**：设计一个对抗性智能体专门干扰中央控制器，并对比三种协同训练策略（包括'军备竞赛'迭代对抗训练），使控制器在对抗过程中不断增强鲁棒性。

**主要结论**：军备竞赛式对抗训练效果最优，将最坏情况下的性能从相对基线损失39%功率，逆转为提升7.9%功率，大幅提升了系统的安全性与鲁棒性。

**关键词**：风电场控制, 安全控制器, 测量误差, 网络安全, 协同训练, 控制器鲁棒性, 风电优化, 扰动攻击, 机器学习控制

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08750v1) | [下载PDF](https://arxiv.org/pdf/2604.08750v1.pdf)

---

## [27. A Little Rank Goes a Long Way: Random Scaffolds with LoRA Adapters Are All You Need](https://arxiv.org/abs/2604.08749v2)

**作者**：Hananel Hazan, Yanbo Zhang, Benedikt Hartl 等 4 位作者  
**分类**：cs.LG, cs.NE  
**发布时间**：2026-04-09

### 📄 论文摘要

How many of a neural network's parameters actually encode task-specific information? We investigate this question with LottaLoRA, a training paradigm in which every backbone weight is drawn at random and frozen; only low-rank LoRA adapters are trained. Across nine benchmarks spanning diverse architecture families from single-layer classifiers to 900M parameter Transformers low-rank adapters over frozen random backbones recover 96-100% of fully trained performance while training only 0.5-40% of the parameters. The task-specific signal therefore occupies a subspace orders of magnitude smaller than the full parameter count suggests. Three mechanistic findings underpin this result:(1) the frozen backbone is actively exploited when static the learned scaling~$β$ remains strictly positive across all architectures but when the scaffold is destabilized, the optimizer silences it and the LoRA factors absorb all task information; (2) the frozen backbone is preferable but interchangeable any random initialization works equally well, provided it remains fixed throughout training; and (3) the minimum LoRA rank at which performance saturates estimates the intrinsic dimensionality of the task, reminiscent of the number of components retained in Principal Component Analysis (PCA). The construction is formally analogous to Reservoir Computing unfolded along the depth axis of a feedforward network. Because the backbone is determined by a random seed alone, models can be distributed as adapters plus seed a footprint that grows with task complexity, not model size, so that storage and memory savings compound as architectures scale.

### 🤖 AI 总结

**一句话总结**：LottaLoRA仅训练随机冻结主干网络上的低秩LoRA适配器，在保持0.5-40%可训练参数量的同时恢复了96-100%的全参数训练性能。

**研究动机**：论文探究神经网络中究竟有多少参数真正编码任务相关信息，旨在揭示任务内在维度与全参数规模之间的巨大差距。

**核心方法**：采用随机初始化并冻结全部主干权重，仅训练低秩LoRA适配器；在9个基准测试和从单层分类器到9亿参数Transformer的多种架构上进行评估。

**主要结论**：任务信号仅占据远小于完整参数空间的子空间；发现固定主干被积极利用且缩放因子β始终保持正值；任意随机初始化效果相当；LoRA秩的饱和点可估计任务内在维度；模型可仅通过种子加适配器分发，存储开销随任务复杂度而非模型规模增长。

**关键词**：Little, Rank, Goes, Long, Way, Random, Scaffolds, LoRA

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08749v2) | [下载PDF](https://arxiv.org/pdf/2604.08749v2.pdf)

---

## [28. Wireless Communication Enhanced Value Decomposition for Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2604.08728v1)

**作者**：Diyi Hu, Bhaskar Krishnamachari  
**分类**：cs.LG  
**发布时间**：2026-04-09

### 📄 论文摘要

Cooperation in multi-agent reinforcement learning (MARL) benefits from inter-agent communication, yet most approaches assume idealized channels and existing value decomposition methods ignore who successfully shared information with whom. We propose CLOVER, a cooperative MARL framework whose centralized value mixer is conditioned on the communication graph realized under a realistic wireless channel. This graph introduces a relational inductive bias into value decomposition, constraining how individual utilities are mixed based on the realized communication structure. The mixer is a GNN with node-specific weights generated by a Permutation-Equivariant Hypernetwork: multi-hop propagation along communication edges reshapes credit assignment so that different topologies induce different mixing. We prove this mixer is permutation invariant, monotonic (preserving the IGM condition), and strictly more expressive than QMIX-style mixers. To handle realistic channels, we formulate an augmented MDP isolating stochastic channel effects from the agent computation graph, and employ a stochastic receptive field encoder for variable-size message sets, enabling end-to-end differentiable training. On Predator-Prey and Lumberjacks benchmarks under p-CSMA wireless channels, CLOVER consistently improves convergence speed and final performance over VDN, QMIX, TarMAC+VDN, and TarMAC+QMIX. Behavioral analysis confirms agents learn adaptive signaling and listening strategies, and ablations isolate the communication-graph inductive bias as the key source of improvement.

### 🤖 AI 总结

**一句话总结**：CLOVER是一个多智能体强化学习框架，通过图神经网络和超网络将现实无线信道约束的通信图融入价值分解，实现通信感知的信用分配。

**研究动机**：现有MARL方法假设理想通信环境，忽视现实无线信道的随机性和拓扑变化；同时现有价值分解方法未考虑信息实际传递成功与否的影响。

**核心方法**：采用基于GNN的值混合器，节点权重由置换等变超网络生成，使多跳通信路径动态调整信用分配；同时设计随机感受野编码器处理可变大小的消息集。

**主要结论**：CLOVER在p-CSMA无线信道下相比VDN、QMIX及其TarMAC变体持续提升收敛速度和最终性能，消融实验证明通信图归纳偏置是关键改进来源。

**关键词**：多智能体强化学习, 价值分解, 无线通信信道, 图神经网络, 通信图, 置换等变超网络, 归纳偏置, 集中式价值混合器, 随机信道建模

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08728v1) | [下载PDF](https://arxiv.org/pdf/2604.08728v1.pdf)

---

## [29. Every Response Counts: Quantifying Uncertainty of LLM-based Multi-Agent Systems through Tensor Decomposition](https://arxiv.org/abs/2604.08708v1)

**作者**：Tiejin Chen, Huaiyuan Yao, Jia Chen 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-04-09

### 📄 论文摘要

While Large Language Model-based Multi-Agent Systems (MAS) consistently outperform single-agent systems on complex tasks, their intricate interactions introduce critical reliability challenges arising from communication dynamics and role dependencies. Existing Uncertainty Quantification methods, typically designed for single-turn outputs, fail to address the unique complexities of the MAS. Specifically, these methods struggle with three distinct challenges: the cascading uncertainty in multi-step reasoning, the variability of inter-agent communication paths, and the diversity of communication topologies. To bridge this gap, we introduce MATU, a novel framework that quantifies uncertainty through tensor decomposition. MATU moves beyond analyzing final text outputs by representing entire reasoning trajectories as embedding matrices and organizing multiple execution runs into a higher-order tensor. By applying tensor decomposition, we disentangle and quantify distinct sources of uncertainty, offering a comprehensive reliability measure that is generalizable across different agent structures. We provide comprehensive experiments to show that MATU effectively estimates holistic and robust uncertainty across diverse tasks and communication topologies.

### 🤖 AI 总结

**一句话总结**：本文提出MATU框架，通过张量分解量化LLM多智能体系统中的不确定性，有效解决多步推理中的级联不确定性、代理间通信路径变化和通信拓扑多样性问题。

**研究动机**：LLM多智能体系统在复杂任务中表现优异，但代理间交互引入了关键的可靠性挑战；现有不确定性量化方法主要针对单轮输出设计，无法处理多智能体系统中独特的通信动态和角色依赖问题。

**核心方法**：MATU将完整推理轨迹表示为嵌入矩阵，并将多次执行运行组织成高阶张量，通过张量分解将不同来源的不确定性分离并量化，生成跨不同代理结构具有泛化能力的综合可靠性度量。

**主要结论**：实验表明MATU能在多种任务和通信拓扑下有效估计整体且鲁棒的不确定性，为评估和改进LLM多智能体系统的可靠性提供了实用工具。

**关键词**：张量分解, 不确定性量化, 多智能体系统, 通信拓扑, 嵌入矩阵, 级联不确定性, 可靠性评估, 多智能体协作

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08708v1) | [下载PDF](https://arxiv.org/pdf/2604.08708v1.pdf)

---

## [30. Efficient RL Training for LLMs with Experience Replay](https://arxiv.org/abs/2604.08706v1)

**作者**：Charles Arnal, Vivien Cabannes, Taco Cohen 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-09

### 📄 论文摘要

While Experience Replay - the practice of storing rollouts and reusing them multiple times during training - is a foundational technique in general RL, it remains largely unexplored in LLM post-training due to the prevailing belief that fresh, on-policy data is essential for high performance. In this work, we challenge this assumption. We present a systematic study of replay buffers for LLM post-training, formalizing the optimal design as a trade-off between staleness-induced variance, sample diversity and the high computational cost of generation. We show that strict on-policy sampling is suboptimal when generation is expensive. Empirically, we show that a well-designed replay buffer can drastically reduce inference compute without degrading - and in some cases even improving - final model performance, while preserving policy entropy.

### 🤖 AI 总结

**一句话总结**：论文挑战了LLM后训练必须使用新鲜on-policy数据的传统观念，证明精心设计的经验回放机制可显著降低推理计算成本，同时保持甚至提升最终模型性能。

**研究动机**：经验回放是通用RL的基础技术，但在LLM后训练中被认为需要新鲜数据保证高性能，该研究系统性地挑战了这一假设，探索replay buffer在LLM场景中的应用价值。

**核心方法**：将replay buffer的最优设计形式化为陈旧性诱导方差、样本多样性与高生成计算成本之间的权衡，通过系统性实验研究不同配置对训练效果的影响。

**主要结论**：严格on-policy采样在生成成本高昂时是次优选择，精心设计的replay buffer能大幅降低推理计算成本，不仅不会降级最终性能，部分场景下甚至能改善模型表现，同时保持策略熵。

**关键词**：经验回放, 回放缓冲区, 样本多样性, 策略熵, 推理计算, 陈旧性, 训练效率, 强化学习

**评分**：13

**论文链接**：[查看原文](https://arxiv.org/abs/2604.08706v1) | [下载PDF](https://arxiv.org/pdf/2604.08706v1.pdf)

---

