# arXiv AI 论文日报 | 2026-04-12

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (3 篇)
- [cs.AI](#csAI) (5 篇)
- [cs.CV](#csCV) (13 篇)
- [cs.CL](#csCL) (9 篇)

---

## cs.AI

## [1. A Benchmark for Gap and Overlap Analysis as a Test of KG Task Readiness](https://arxiv.org/abs/2604.10853v1)

**作者**：Maruf Ahmed Mridul, Rohit Kapa, Oshani Seneviratne  
**分类**：cs.AI  
**发布时间**：2026-04-12

### 📄 论文摘要

Task-oriented evaluation of knowledge graph (KG) quality increasingly asks whether an ontology-based representation can answer the competency questions that users actually care about, in a manner that is reproducible, explainable, and traceable to evidence. This paper adopts that perspective and focuses on gap and overlap analysis for policy-like documents (e.g., insurance contracts), where given a scenario, which documents support it (overlap) and which do not (gap), with defensible justifications. The resulting gap/overlap determinations are typically driven by genuine differences in coverage and restrictions rather than missing data, making the task a direct test of KG task readiness rather than a test of missing facts or query expressiveness. We present an executable and auditable benchmark that aligns natural-language contract text with a formal ontology and evidence-linked ground truth, enabling systematic comparison of methods. The benchmark includes: (i) ten simplified yet diverse life-insurance contracts reviewed by a domain expert, (ii) a domain ontology (TBox) with an instantiated knowledge base (ABox) populated from contract facts, and (iii) 58 structured scenarios paired with SPARQL queries with contract-level outcomes and clause-level excerpts that justify each label. Using this resource, we compare a text-only LLM baseline that infers outcomes directly from contract text against an ontology-driven pipeline that answers the same scenarios over the instantiated KG, demonstrating that explicit modeling improves consistency and diagnosis for gap/overlap analyses. Although demonstrated for gap and overlap analysis, the benchmark is intended as a reusable template for evaluating KG quality and supporting downstream work such as ontology learning, KG population, and evidence-grounded question answering.

### 🤖 AI 总结

**一句话总结**：该论文提出了一个用于评估知识图谱（KG）任务就绪性的基准测试框架，专注于保险合同文档的gap和overlap分析，比较了LLM基线与本体驱动管道的方法效果。

**研究动机**：现有知识图谱质量评估缺乏针对性和可解释性，需要验证基于本体的表示能否回答用户实际关心的 competency questions，尤其是对文档覆盖和限制差异的评估。

**核心方法**：构建了一个包含10份简化人寿保险合同、领域本体（TBox/ABox）、58个结构化场景及对应SPARQL查询的基准测试，将自然语言合同文本与形式本体对齐，通过证据链接验证进行系统性方法比较。

**主要结论**：显式本体建模相比纯文本LLM方法在gap/overlap分析中表现更好，提高了结果一致性和诊断能力，该基准测试可作为评估KG质量和支持本体学习、KG填充等下游工作的可复用模板。

**关键词**：知识图谱质量评估, 间隙重叠分析, 保险合同本体, 证据链追踪, 可验证基准测试, 文本推理, 语义对齐, 政策文档解析, KG任务就绪性

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10853v1) | [下载PDF](https://arxiv.org/pdf/2604.10853v1.pdf)

---

## [2. Your Model Diversity, Not Method, Determines Reasoning Strategy](https://arxiv.org/abs/2604.10827v1)

**作者**：Moulik Choraria, Argyrios Gerogiannis, Anirban Das 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-12

### 📄 论文摘要

Compute scaling for LLM reasoning requires allocating budget between exploring solution approaches ($breadth$) and refining promising solutions ($depth$). Most methods implicitly trade off one for the other, yet why a given trade-off works remains unclear, and validation on a single model obscures the role of the model itself. We argue that $\textbf{the optimal strategy depends on the model's diversity profile, the spread of probability mass across solution approaches, and that this must be characterized before any exploration strategy is adopted.}$ We formalize this through a theoretical framework decomposing reasoning uncertainty and derive conditions under which tree-style depth refinement outperforms parallel sampling. We validate it on Qwen-3 4B and Olmo-3 7B families, showing that lightweight signals suffice for depth-based refinement on low-diversity aligned models while yielding limited utility for high-diversity base models, which we hypothesize require stronger compensation for lower exploration coverage.

### 🤖 AI 总结

**一句话总结**：LLM推理的最佳策略取决于模型的概率分布多样性特征，而非方法本身，低多样性对齐模型适合深度优化，高多样性基础模型需要更广泛的探索覆盖。

**研究动机**：当前LLM推理的算力扩展方法在广度探索与深度优化之间进行权衡，但为何特定权衡有效尚不清楚，且现有验证仅基于单一模型，忽视了模型本身特性的影响。

**核心方法**：提出理论框架分解推理不确定性，推导树状深度优化优于并行采样的条件条件，并在Qwen-3 4B和Olmo-3 7B模型族上进行验证。

**主要结论**：轻量级信号足以支持低多样性对齐模型的深度优化，但对高多样性基础模型效果有限，这类模型需要更强的探索覆盖补偿策略。

**关键词**：计算扩展, 模型多样性, 探索策略, 深度精炼, 推理不确定性, 树状搜索, Model, Diversity

**评分**：8

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10827v1) | [下载PDF](https://arxiv.org/pdf/2604.10827v1.pdf)

---

## [3. CheeseBench: Evaluating Large Language Models on Rodent Behavioral Neuroscience Paradigms](https://arxiv.org/abs/2604.10825v1)

**作者**：Zacharie Bugaud  
**分类**：cs.AI  
**发布时间**：2026-04-12

### 📄 论文摘要

We introduce CheeseBench, a benchmark that evaluates large language models (LLMs) on nine classical behavioral neuroscience paradigms (Morris water maze, Barnes maze, T-maze, radial arm maze, star maze, operant chamber, shuttle box, conditioned place preference, and delayed non-match to sample), spanning six cognitive dimensions. Each task is grounded in peer-reviewed rodent protocols with approximate animal baselines. The agent receives a unified system prompt with no task-specific instructions and must discover goals purely from ASCII text observations and reward signals, much like a rodent placed into an unfamiliar apparatus. We evaluate six open-weight LLMs (3B to 72B parameters) on text-based ASCII renderings and compare against both a random baseline and a graph-based reinforcement learning agent. Our best model (Qwen2.5-VL-7B) reaches 52.6% average success on ASCII input, compared to 32.1% for random agents and 78.9% for approximate rodent baselines. We find that (1) scaling beyond 7B yields diminishing returns, (2) longer context history degrades performance, (3) chain-of-thought prompting hurts rather than helps, and (4) a vision-language architecture provides an advantage at 7B but hurts at 32B. Because the same model's performance ranges from 20% to 57% depending on interface parameters alone, these results characterize the agent-plus-interface system, not the model in isolation. Under this unified zero-shot ASCII protocol, current open-weight LLM agents remain well below approximate rodent reference values, particularly on tasks requiring spatial navigation and within-trial state tracking.

### 🤖 AI 总结

**一句话总结**：CheeseBench通过9种经典啮齿动物行为范式评估LLM认知能力，发现当前开源模型在零样本ASCII协议下表现仍显著低于啮齿动物基准。

**研究动机**：现有LLM基准缺乏对动物认知任务的系统评估，无法衡量模型在真实导航和状态追踪任务中的表现。

**核心方法**：在统一系统提示下，让LLM仅通过ASCII文本观察和奖励信号发现任务目标，评估6个模型（3B-72B参数）在9个行为范式上的表现。

**主要结论**：最佳模型Qwen2.5-VL-7B达52.6%准确率，远低于78.9%的啮齿动物基准；超过7B参数收益递减，长上下文和链式思维反而降低性能。

**关键词**：行为神经科学范式, 空间导航, 零样本评估, 认知维度, 强化学习基线, 上下文长度, 链式思维提示, 视觉-语言模型

**评分**：10

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10825v1) | [下载PDF](https://arxiv.org/pdf/2604.10825v1.pdf)

---

## [4. TorchUMM: A Unified Multimodal Model Codebase for Evaluation, Analysis, and Post-training](https://arxiv.org/abs/2604.10784v1)

**作者**：Yinyi Luo, Wenwen Wang, Hayes Bai 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-12

### 📄 论文摘要

Recent advances in unified multimodal models (UMMs) have led to a proliferation of architectures capable of understanding, generating, and editing across visual and textual modalities. However, developing a unified framework for UMMs remains challenging due to the diversity of model architectures and the heterogeneity of training paradigms and implementation details. In this paper, we present TorchUMM, the first unified codebase for comprehensive evaluation, analysis, and post-training across diverse UMM backbones, tasks, and datasets. TorchUMM supports a broad spectrum of models covering a wide range of scales and design paradigms. Our benchmark encompasses three core task dimensions: multimodal understanding, generation, and editing, and integrates both established and novel datasets to evaluate perception, reasoning, compositionality, and instruction-following abilities. By providing a unified interface and standardized evaluation protocols, TorchUMM enables fair and reproducible comparisons across heterogeneous models and fosters deeper insights into their strengths and limitations, facilitating the development of more capable unified multimodal systems. Code is available at: https://github.com/AIFrontierLab/TorchUMM.

### 🤖 AI 总结

**一句话总结**：TorchUMM是首个统一的代码库，实现了对多种统一多模态模型（UMM）的全面评估、分析和后训练的标准化支持。

**研究动机**：由于统一多模态模型（UMM）架构多样、训练范式异构，现有研究缺乏统一的框架来进行公平比较和深入分析。

**核心方法**：TorchUMM通过提供统一接口和标准化评估协议，支持覆盖不同规模和设计范式的多种模型，涵盖多模态理解、生成和编辑三大核心任务维度。

**主要结论**：该框架实现了跨异构模型的公平可复现比较，帮助研究人员深入理解各模型的优势与局限，推动更强大的统一多模态系统发展。

**关键词**：统一多模态模型, 评估框架, 多模态生成, 多模态编辑, 后训练, 基准测试, 指令跟随, 模型对比

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10784v1) | [下载PDF](https://arxiv.org/pdf/2604.10784v1.pdf)

---

## [5. Learning Preference-Based Objectives from Clinical Narratives for Sequential Treatment Decision-Making](https://arxiv.org/abs/2604.10783v1)

**作者**：Daniel J. Tan, Kay Choong See, Mengling Feng  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-04-12

### 📄 论文摘要

Designing reward functions remains a central challenge in reinforcement learning (RL) for healthcare, where outcomes are sparse, delayed, and difficult to specify. While structured data capture physiological states, they often fail to reflect the overall quality of a patient's clinical trajectory, including recovery dynamics, treatment burden, and stability. Clinical narratives, in contrast, summarize longitudinal reasoning and implicitly encode evaluations of treatment effectiveness. We propose Clinical Narrative-informed Preference Rewards (CN-PR), a framework for learning reward functions directly from discharge summaries by treating them as scalable supervision for trajectory-level preferences. Using a large language model, we derive trajectory quality scores (TQS) and construct pairwise preferences over patient trajectories, enabling reward learning via a structured preference-based objective. To account for variability in narrative informativeness, we incorporate a confidence signal that weights supervision based on its relevance to the decision-making task. The learned reward aligns strongly with trajectory quality (Spearman rho = 0.63) and enables policies that are consistently associated with improved recovery-related outcomes, including increased organ support-free days and faster shock resolution, while maintaining comparable performance on mortality. These effects persist under external validation. Our results demonstrate that narrative-derived supervision provides a scalable and expressive alternative to handcrafted or outcome-based reward design for dynamic treatment regimes.

### 🤖 AI 总结

**一句话总结**：提出CN-PR框架，从临床叙述文本中学习奖励函数，通过大语言模型提取轨迹质量分数构建偏好对，实现更符合临床实际的顺序治疗决策策略。

**研究动机**：医疗强化学习中，结构化数据难以捕捉患者整体临床轨迹质量，而临床叙述文本隐含了医生对治疗效果的评价，可作为可扩展的奖励监督信号。

**核心方法**：利用大语言模型从出院总结中导出轨迹质量分数(TQS)，构建患者轨迹间的成对偏好，并结合信息量置信度信号进行加权监督学习，最终通过偏好驱动的目标函数训练奖励模型和策略。

**主要结论**：学习到的奖励与轨迹质量高度相关(rho=0.63)，策略在无器官支持天数增加和休克更快缓解等恢复指标上表现更优，且该方法具备外部验证的鲁棒性，验证了叙事文本监督在动态治疗策略中的可行性和优越性。

**关键词**：临床叙事, 奖励函数学习, 治疗决策, 偏好学习, LLM, 动态治疗方案, 轨迹质量, 医疗强化学习

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10783v1) | [下载PDF](https://arxiv.org/pdf/2604.10783v1.pdf)

---

## cs.CL

## [6. Position-Agnostic Pre-Projection for Transformer Attention: Nonlinear Feature Construction and Content Skip Before Q/K/V](https://arxiv.org/abs/2604.10791v1)

**作者**：Chirag Shinde  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-04-12

### 📄 论文摘要

We propose two complementary modifications to transformer attention blocks. First, a non-linear pre-projection MLP is inserted between layer norm and Q/K/V projections, constructing richer features in a position-agnostic manner before any positional encoding is applied. Second, a content skip connection routes the pre-projection's features around the attention mechanism, allowing content information to bypass position-aware attention where beneficial. In frozen-probe experiments on Pythia-160M and 410M, the combined approach achieves the strongest results across methods: +40.6% LAMBADA accuracy and -39% perplexity at 160M scale. Learned skip connection weights reveal a consistent pattern across model sizes: later transformer layers activate the content bypass more strongly than earlier layers, suggesting that deeper layers benefit from content information that does not pass through positional attention. All modifications add no K/V cache overhead.

### 🤖 AI 总结

**一句话总结**：通过在Transformer注意力块中加入非线性预投影MLP和内容跳跃连接，在不增加KV缓存开销的情况下显著提升模型性能，160M规模LAMBADA精度提升40.6%，困惑度降低39%。

**研究动机**：现有Transformer架构中位置编码过早应用，限制了模型捕捉纯内容信息的能力，需要让部分内容信息能够绕过位置感知的注意力机制直接传递。

**核心方法**：在LayerNorm和Q/K/V投影之间插入非线性预投影MLP构建更丰富的位置无关特征，同时添加内容跳跃连接让预投影特征绕过注意力机制，并在训练中学习跳跃权重。

**主要结论**：组合方法在Pythia-160M和410M上取得最佳结果，内容跳过权重显示深层激活更强，说明深层更依赖不经过位置注意力的内容信息，且修改不产生任何KV缓存开销。

**关键词**：Position-Agnostic, Pre-Projection, Transformer, Attention, Nonlinear, Feature, Construction, Content

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10791v1) | [下载PDF](https://arxiv.org/pdf/2604.10791v1.pdf)

---

## [7. TInR: Exploring Tool-Internalized Reasoning in Large Language Models](https://arxiv.org/abs/2604.10788v1)

**作者**：Qiancheng Xu, Yongqi Li, Fan Liu 等 6 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-12

### 📄 论文摘要

Tool-Integrated Reasoning (TIR) has emerged as a promising direction by extending Large Language Models' (LLMs) capabilities with external tools during reasoning. Existing TIR methods typically rely on external tool documentation during reasoning. However, this leads to tool mastery difficulty, tool size constraints, and inference inefficiency. To mitigate these issues, we explore Tool-Internalized Reasoning (TInR), aiming at facilitating reasoning with tool knowledge internalized into LLMs. Achieving this goal presents notable requirements, including tool internalization and tool-reasoning coordination. To address them, we propose TInR-U, a tool-internalized reasoning framework for unified reasoning and tool usage. TInR-U is trained through a three-phase pipeline: 1) tool internalization with a bidirectional knowledge alignment strategy; 2) supervised fine-tuning warm-up using high-quality reasoning annotations, and 3) reinforcement learning with TInR-specific rewards. We comprehensively evaluate our method across in-domain and out-of-domain settings. Experiment results show that TInR-U achieves superior performance in both settings, highlighting its effectiveness and efficiency.

### 🤖 AI 总结

**一句话总结**：TInR-U通过三阶段训练管道实现工具知识内化，使LLM能够更高效地进行工具推理，在领域内和领域外设置中均实现优越性能。

**研究动机**：现有工具集成推理(TIR)方法依赖外部工具文档，导致工具掌握困难、工具大小限制和推理效率低下，需要探索将工具知识内化到LLM中的新范式。

**核心方法**：TInR-U采用三阶段训练管道：1)基于双向知识对齐的工具内化；2)使用高质量推理注释的监督微调热身；3)基于TInR特定奖励的强化学习，实现统一的推理和工具使用能力。

**主要结论**：实验结果表明TInR-U在领域内和领域外设置中均取得优越性能，验证了其有效性和效率，为工具内化推理提供了可行的解决方案。

**关键词**：LLM, TInR, Exploring, Tool-Internalized, Reasoning, Large, Language, Models

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10788v1) | [下载PDF](https://arxiv.org/pdf/2604.10788v1.pdf)

---

## [8. When Meaning Isn't Literal: Exploring Idiomatic Meaning Across Languages and Modalities](https://arxiv.org/abs/2604.10787v1)

**作者**：Sarmistha Das, Shreyas Guha, Suvrayan Bandyopadhyay 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-12

### 📄 论文摘要

Idiomatic reasoning, deeply intertwined with metaphor and culture, remains a blind spot for contemporary language models, whose progress skews toward surface-level lexical and semantic cues. For instance, the Bengali idiom \textit{\foreignlanguage{bengali}{\char"0986\char"0999\char"09CD\char"0997\char"09C1 \char"09B0 \char"09AB\char"09B2 \char"099F\char"0995}} (angur fol tok, ``grapes are sour''): it encodes denial-driven rationalization, yet naive models latch onto the literal fox-and-grape imagery. Addressing this oversight, we present ``Mediom,'' a multilingual, multimodal idiom corpus of 3,533 Hindi, Bengali, and Thai idioms, each paired with gold-standard explanations, cross-lingual translations, and carefully aligned text--image representations. We benchmark both large language models (textual reasoning) and vision-language models (figurative disambiguation) on Mediom, exposing systematic failures in metaphor comprehension. To mitigate these gaps, we propose ``HIDE,'' a Hinting-based Idiom Explanation framework that leverages error-feedback retrieval and targeted diagnostic cues for iterative reasoning refinement. Collectively, Mediom and HIDE establish a rigorous test bed and methodology for culturally grounded, multimodal idiom understanding embedded with reasoning hints in next-generation AI systems.

### 🤖 AI 总结

**一句话总结**：论文提出Mediom多语言多模态习语语料库和HIDE提示框架，用于评估和改进AI模型对习语的理解能力。

**研究动机**：当前语言模型在习语理解上存在系统性缺陷，容易被字面意义误导，无法捕捉习语背后的隐喻和文化内涵。

**核心方法**：构建包含3533条印地语、孟加拉语和泰语习语的Mediom语料库，并提出基于错误反馈检索的HIDE框架进行迭代推理优化，同时在LLM和VLM上进行基准测试。

**主要结论**：实验揭示了现有模型在隐喻理解上的系统性失败，HIDE框架能有效提升习语解释质量，为多语言多模态习语理解提供可复现的测试基准和方法论。

**关键词**：When, Meaning, Isn't, Literal, Exploring, Idiomatic, Across, Languages

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10787v1) | [下载PDF](https://arxiv.org/pdf/2604.10787v1.pdf)

---

## [9. Generating Multiple-Choice Knowledge Questions with Interpretable Difficulty Estimation using Knowledge Graphs and Large Language Models](https://arxiv.org/abs/2604.10748v1)

**作者**：Mehmet Can Şakiroğlu, H. Altay Güvenir, Kamer Kaya  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-04-12

### 📄 论文摘要

Generating multiple-choice questions (MCQs) with difficulty estimation remains challenging in automated MCQ-generation systems used in adaptive, AI-assisted education. This study proposes a novel methodology for generating MCQs with difficulty estimation from the input documents by utilizing knowledge graphs (KGs) and large language models (LLMs). Our approach uses an LLM to construct a KG from input documents, from which MCQs are then systematically generated. Each MCQ is generated by selecting a node from the KG as the key, sampling a related triple or quintuple -- optionally augmented with an extra triple -- and prompting an LLM to generate a corresponding stem from these graph components. Distractors are then selected from the KG. For each MCQ, nine difficulty signals are computed and combined into a unified difficulty score using a data-driven approach. Experimental results demonstrate that our method generates high-quality MCQs whose difficulty estimation is interpretable and aligns with human perceptions. Our approach improves automated MCQ generation by integrating structured knowledge representations with LLMs and a data-driven difficulty estimation model.

### 🤖 AI 总结

**一句话总结**：提出一种基于知识图谱和大型语言模型的多选题自动生成方法，可实现可解释的难度估计。

**研究动机**：在自适应AI辅助教育系统中，自动生成具有难度估计的多选题（MCQ）仍面临挑战，现有方法难以生成高质量且难度可控的题目。

**核心方法**：利用LLM从输入文档构建知识图谱，通过选择图谱节点作为关键信息、采样三元组或五元组提示LLM生成题干、从图谱中选择干扰项，并计算九个难度信号组合成统一难度分数。

**主要结论**：实验结果表明该方法能生成高质量的多选题，其难度估计具有可解释性且与人类认知一致，有效地将结构化知识表示与LLM和数据驱动的难度估计模型相融合。

**关键词**：LLM, Generating, Multiple-Choice, Knowledge, Questions, Interpretable, Difficulty, Estimation

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10748v1) | [下载PDF](https://arxiv.org/pdf/2604.10748v1.pdf)

---

## [10. How You Ask Matters! Adaptive RAG Robustness to Query Variations](https://arxiv.org/abs/2604.10745v1)

**作者**：Yunah Jang, Megha Sundriyal, Kyomin Jung 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-12

### 📄 论文摘要

Adaptive Retrieval-Augmented Generation (RAG) promises accuracy and efficiency by dynamically triggering retrieval only when needed and is widely used in practice. However, real-world queries vary in surface form even with the same intent, and their impact on Adaptive RAG remains under-explored. We introduce the first large-scale benchmark of diverse yet semantically identical query variations, combining human-written and model-generated rewrites. Our benchmark facilitates a systematic evaluation of Adaptive RAG robustness by examining its key components across three dimensions: answer quality, computational cost, and retrieval decisions. We discover a critical robustness gap, where small surface-level changes in queries dramatically alter retrieval behavior and accuracy. Although larger models show better performance, robustness does not improve accordingly. These findings reveal that Adaptive RAG methods are highly vulnerable to query variations that preserve identical semantics, exposing a critical robustness challenge.

### 🤖 AI 总结

**一句话总结**：本文首次系统性地揭示了自适应RAG系统在面对语义相同但表述多样的查询时存在严重的鲁棒性缺陷，即使微小的表面变化也会导致检索行为和准确率的显著波动。

**研究动机**：现实世界的用户查询即使意图相同也往往以不同方式表达，但这种查询变体对自适应RAG系统的影响此前缺乏系统研究，而自适应RAG在实践中被广泛使用，其可靠性至关重要。

**核心方法**：作者构建了首个大规模多样化查询变体基准数据集（包含人工撰写和模型生成的改写），从答案质量、计算成本和检索决策三个维度系统评估自适应RAG的鲁棒性。

**主要结论**：研究发现存在显著的鲁棒性差距——表面层面的微小变化会剧烈改变检索行为和准确率；虽然更大规模的模型性能更好，但鲁棒性并未相应提升，表明自适应RAG方法对语义保持不变但表述变化的查询高度脆弱。

**关键词**：How, Ask, Matters!, Adaptive, RAG, Robustness, Query, Variations

**评分**：14

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10745v1) | [下载PDF](https://arxiv.org/pdf/2604.10745v1.pdf)

---

## [11. Deep-Reporter: Deep Research for Grounded Multimodal Long-Form Generation](https://arxiv.org/abs/2604.10741v1)

**作者**：Fangda Ye, Zhifei Xie, Yuxin Hu 等 8 位作者  
**分类**：cs.CL, cs.AI, cs.IR  
**发布时间**：2026-04-12

### 📄 论文摘要

Recent agentic search frameworks enable deep research via iterative planning and retrieval, reducing hallucinations and enhancing factual grounding. However, they remain text-centric, overlooking the multimodal evidence that characterizes real-world expert reports. We introduce a pressing task: multimodal long-form generation. Accordingly, we propose Deep-Reporter, a unified agentic framework for grounded multimodal long-form generation. It orchestrates: (i) Agentic Multimodal Search and Filtering to retrieve and filter textual passages and information-dense visuals; (ii) Checklist-Guided Incremental Synthesis to ensure coherent image-text integration and optimal citation placement; and (iii) Recurrent Context Management to balance long-range coherence with local fluency. We develop a rigorous curation pipeline producing 8K high-quality agentic traces for model optimization. We further introduce M2LongBench, a comprehensive testbed comprising 247 research tasks across 9 domains and a stable multimodal sandbox. Extensive experiments demonstrate that long-form multimodal generation is a challenging task, especially in multimodal selection and integration, and effective post-training can bridge the gap.

### 🤖 AI 总结

**一句话总结**：Deep-Reporter是一个统一的智能体框架，通过多模态搜索筛选、清单引导的增量综合和循环上下文管理，实现有据可查的多模态长文本生成。

**研究动机**：现有深度研究框架仅关注文本生成，忽视了现实世界专家报告中重要的多模态证据（如图文结合），因此需要提出新的多模态长文本生成任务。

**核心方法**：提出三个核心组件：(i)智能多模态搜索与筛选模块用于检索图文信息；(ii)清单引导的增量综合方法确保图像-文本连贯整合和最佳引用位置；(iii)循环上下文管理平衡长程一致性与局部流畅性。

**主要结论**：多模态长文本生成是一项极具挑战性的任务，尤其在多模态选择和整合方面；通过构建8K高质量智能体轨迹和M2LongBench基准测试验证，有效的后训练可以显著弥合性能差距。

**关键词**：Deep-Reporter, Deep, Research, Grounded, Multimodal, Long-Form, Generation, Recent

**评分**：67

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10741v1) | [下载PDF](https://arxiv.org/pdf/2604.10741v1.pdf)

---

## [12. BlasBench: An Open Benchmark for Irish Speech Recognition](https://arxiv.org/abs/2604.10736v1)

**作者**：Jyoutir Raj, John Conway  
**分类**：cs.CL, cs.SD  
**发布时间**：2026-04-12

### 📄 论文摘要

No open Irish-specific benchmark compares end-user ASR systems under a shared Irish-aware evaluation protocol. To solve this, we release BlasBench, an open evaluation harness with Irish-aware text normalisation that preserves fadas, lenition, and eclipsis. We benchmark 12 systems across four architecture families on Common Voice ga-IE and FLEURS ga-IE. All Whisper variants exceed 100% WER. The best open model (omniASR LLM 7B) achieves 30.65% WER on Common Voice and 39.09% on FLEURS. We noticed models fine-tuned on Common Voice lose 33-43 WER points on FLEURS, revealing a generalisation gap that is invisible to single-dataset evaluation.

### 🤖 AI 总结

**一句话总结**：发布首个开源爱尔兰语语音识别基准BlasBench，揭示现有模型WER普遍过高，最佳开源模型omniASR 7B在Common Voice上达30.65%，且发现跨数据集评估存在33-43点WER的泛化差距。

**研究动机**：目前缺乏公开的爱尔兰语ASR系统对比基准和统一的评估协议，导致无法客观衡量不同系统对爱尔兰语特殊语言现象（如fadas、lenition、eclipsis）的处理能力。

**核心方法**：构建了Irish-aware文本标准化工具保留爱尔兰语特殊字符和形态特征，在Common Voice ga-IE和FLEURS ga-IE两个数据集上评估了12个跨四个架构家族的ASR系统。

**主要结论**：所有Whisper变体WER超过100%；最佳开源模型omniASR LLM 7B在Common Voice和FLEURS上分别达到30.65%和39.09% WER；细粒度实验揭示单数据集评估会掩盖33-43点的泛化差距。

**关键词**：爱尔兰语语音识别, ASR基准测试, 语言模型微调, 文本标准化, 微调泛化, 多语言语音识别, 跨数据集评估, 开放基准工具, 语音识别系统

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10736v1) | [下载PDF](https://arxiv.org/pdf/2604.10736v1.pdf)

---

## [13. Too Nice to Tell the Truth: Quantifying Agreeableness-Driven Sycophancy in Role-Playing Language Models](https://arxiv.org/abs/2604.10733v1)

**作者**：Arya Shah, Deepali Mishra, Chaklam Silpasuwanchai  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-12

### 📄 论文摘要

Large language models increasingly serve as conversational agents that adopt personas and role-play characters at user request. This capability, while valuable, raises concerns about sycophancy: the tendency to provide responses that validate users rather than prioritize factual accuracy. While prior work has established that sycophancy poses risks to AI safety and alignment, the relationship between specific personality traits of adopted personas and the degree of sycophantic behavior remains unexplored. We present a systematic investigation of how persona agreeableness influences sycophancy across 13 small, open-weight language models ranging from 0.6B to 20B parameters. We develop a benchmark comprising 275 personas evaluated on NEO-IPIP agreeableness subscales and expose each persona to 4,950 sycophancy-eliciting prompts spanning 33 topic categories. Our analysis reveals that 9 of 13 models exhibit statistically significant positive correlations between persona agreeableness and sycophancy rates, with Pearson correlations reaching $r = 0.87$ and effect sizes as large as Cohen's $d = 2.33$. These findings demonstrate that agreeableness functions as a reliable predictor of persona-induced sycophancy, with direct implications for the deployment of role-playing AI systems and the development of alignment strategies that account for personality-mediated deceptive behaviors.

### 🤖 AI 总结

**一句话总结**：研究表明，角色扮演LLM中采用的越友善（agreeableness）的人格特质会导致越强的谄媚（sycophancy）行为，且这种关联在多个模型中均具有统计显著性。

**研究动机**：先前研究已证实谄媚行为对AI安全和对齐构成风险，但尚未探索人格特质与谄媚程度之间的关系，需要系统性地研究这一影响机制。

**核心方法**：构建了包含275个人格角色的基准测试集，采用NEO-IPIP友善度量表进行评估，并在33个话题类别的4,950个诱发性提示下测试了13个0.6B至20B参数的模型。

**主要结论**：13个模型中有9个展现出人格友善度与谄媚率之间显著正相关，皮尔逊相关系数高达r=0.87，效应量Cohen's d达2.33，证明友善度是预测角色诱发谄媚行为的可靠指标。

**关键词**：Too, Nice, Tell, Truth, Quantifying, Agreeableness-Driven, Sycophancy, Role-Playing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10733v1) | [下载PDF](https://arxiv.org/pdf/2604.10733v1.pdf)

---

## [14. Expect the Unexpected? Testing the Surprisal of Salient Entities](https://arxiv.org/abs/2604.10724v1)

**作者**：Jessica Lin, Amir Zeldes  
**分类**：cs.CL  
**发布时间**：2026-04-12

### 📄 论文摘要

Previous work examining the Uniform Information Density (UID) hypothesis has shown that while information as measured by surprisal metrics is distributed more or less evenly across documents overall, local discrepancies can arise due to functional pressures corresponding to syntactic and discourse structural constraints. However, work thus far has largely disregarded the relative salience of discourse participants. We fill this gap by studying how overall salience of entities in discourse relates to surprisal using 70K manually annotated mentions across 16 genres of English and a novel minimal-pair prompting method. Our results show that globally salient entities exhibit significantly higher surprisal than non-salient ones, even controlling for position, length, and nesting confounds. Moreover, salient entities systematically reduce surprisal for surrounding content when used as prompts, enhancing document-level predictability. This effect varies by genre, appearing strongest in topic-coherent texts and weakest in conversational contexts. Our findings refine the UID competing pressures framework by identifying global entity salience as a mechanism shaping information distribution in discourse.

### 🤖 AI 总结

**一句话总结**：研究发现话语中全局显著的实体本身具有更高惊讶度，但同时能降低周围内容的惊讶度，这一效应因体裁而异，完善了UID竞争压力框架。

**研究动机**：先前UID研究虽证明信息在文档中大致均匀分布，但忽视了话语参与者

**核心方法**：N/A

**主要结论**：N/A

**关键词**：信息分布均匀性, 实体显著性, 惊讶度, 话语结构约束, 文本可预测性, 最小配对提示, 多体裁分析, 上下文窗口效应, 信息密度竞争, 标注语料库

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10724v1) | [下载PDF](https://arxiv.org/pdf/2604.10724v1.pdf)

---

## cs.CV

## [15. Retinal Cyst Detection from Optical Coherence Tomography Images](https://arxiv.org/abs/2604.10843v1)

**作者**：Abhishek Dharmaratnakar, Aadheeshwar Vijayakumar, Suchand Dayanand  
**分类**：cs.CV, cs.AI, cs.LG, cs.NE  
**发布时间**：2026-04-12

### 📄 论文摘要

Retinal Cysts are formed by leakage and accumulation of fluid in the retina due to the incompetence of retinal vasculature. These cystic spaces have significance in several ocular diseases such as age-related macular degeneration, diabetic macular edema, etc. Optical coherence tomography is one of the predominant diagnosing techniques for imaging retinal pathologies. Segmenting and quantification of intraretinal cysts plays the vital role in predicting visual acuity. In literature, several methods have been proposed for automatic segmentation of intraretinal cysts. As cystoid macular edema becomes a major problem to humankind, we need to quantify it accurately and operate it out, else it might cause many problems later on. Though research is being carried out in this area, not much of progress has been made and accuracy achieved so far is 68\% which is very less. Also, the methods depend on the quality of the image and give very low results for high noise images like topcon. This work uses ResNet CNN (Convolutional Neural Network) approach of segmentation by the way of patchwise classification for training on image set from cyst segmentation challenge dataset and testing on test data set given by 2 different graders for all 4 vendors in the challenge. It also compares these methods using first publicly available novel cyst segmentation challenge dataset. The methods were evaluated using quantitative measures to assess their robustness against the challenges of intraretinal cyst segmentation. The results are found to be better than the previous state of the art approaches giving more than 70\% dice coefficient on all vendors irrespective of their quality.

### 🤖 AI 总结

**一句话总结**：使用ResNet CNN通过patchwise分类方法分割OCT图像中的视网膜囊肿，在所有厂商数据上达到超过70%的dice系数，优于现有方法。

**研究动机**：视网膜囊肿是多种眼科疾病的关键指标，准确分割对预测视力至关重要，但现有自动分割方法准确率仅68%且对高噪声图像效果差。

**核心方法**：采用ResNet CNN架构，通过patchwise分类方式进行训练和分割，在公开的囊肿分割挑战数据集上对来自4个不同厂商的图像进行测试评估。

**主要结论**：该方法在所有厂商的OCT图像上均达到超过70%的dice系数，显著优于此前最先进方法，且对不同质量图像具有较好的鲁棒性。

**关键词**：视网膜囊肿检测, OCT图像分割, 眼科疾病诊断, 黄斑病变, 深度学习医学影像, 视网膜分割, 图像量化分析, Retinal

**评分**：16

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10843v1) | [下载PDF](https://arxiv.org/pdf/2604.10843v1.pdf)

---

## [16. Immune2V: Image Immunization Against Dual-Stream Image-to-Video Generation](https://arxiv.org/abs/2604.10837v1)

**作者**：Zeqian Long, Ozgur Kara, Haotian Xue 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-12

### 📄 论文摘要

Image-to-video (I2V) generation has the potential for societal harm because it enables the unauthorized animation of static images to create realistic deepfakes. While existing defenses effectively protect against static image manipulation, extending these to I2V generation remains underexplored and non-trivial. In this paper, we systematically analyze why modern I2V models are highly robust against naive image-level adversarial attacks (i.e., immunization). We observe that the video encoding process rapidly dilutes the adversarial noise across future frames, and the continuous text-conditioned guidance actively overrides the intended disruptive effect of the immunization. Building on these findings, we propose the Immune2V framework which enforces temporally balanced latent divergence at the encoder level to prevent signal dilution, and aligns intermediate generative representations with a precomputed collapse-inducing trajectory to counteract the text-guidance override. Extensive experiments demonstrate that Immune2V produces substantially stronger and more persistent degradation than adapted image-level baselines under the same imperceptibility budget.

### 🤖 AI 总结

**一句话总结**：提出 Immune2V 框架，通过在编码器层面强制时序平衡的潜在分歧并与预计算的崩溃轨迹对齐，有效保护静态图像免受双流图像转视频生成模型的未授权动画化攻击。

**研究动机**：现有防御主要针对静态图像操纵，对图像转视频（I2V）生成的攻击防护研究不足；且现代 I2V 模型对简单的图像级对抗攻击具有鲁棒性，使其难以通过传统免疫策略生效。

**核心方法**：提出 Immune2V 框架，通过在编码器层面强制时序平衡的潜在分歧防止视频编码过程中的信号稀释，并将其与预计算的崩溃轨迹对齐以对抗文本条件引导的覆盖效果。

**主要结论**：实验表明，在相同不可感知性预算下，Immune2V 产生更强且更持久的降解效果，显著优于改编的图像级基线防御方法。

**关键词**：图像到视频生成, 深度伪造防御, 潜在分歧, 文本引导, 编码器优化, 信号稀释, 时序平衡, 轨迹对齐, 中间表示

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10837v1) | [下载PDF](https://arxiv.org/pdf/2604.10837v1.pdf)

---

## [17. HO-Flow: Generalizable Hand-Object Interaction Generation with Latent Flow Matching](https://arxiv.org/abs/2604.10836v1)

**作者**：Zerui Chen, Rolandos Alexandros Potamias, Shizhe Chen 等 6 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-04-12

### 📄 论文摘要

Generating realistic 3D hand-object interactions (HOI) is a fundamental challenge in computer vision and robotics, requiring both temporal coherence and high-fidelity physical plausibility. Existing methods remain limited in their ability to learn expressive motion representations for generation and perform temporal reasoning. In this paper, we present HO-Flow, a framework for synthesizing realistic hand-object motion sequences from texts and canoncial 3D objects. HO-Flow first employs an interaction-aware variational autoencoder to encode sequences of hand and object motions into a unified latent manifold by incorporating hand and object kinematics, enabling the representation to capture rich interaction dynamics. It then leverages a masked flow matching model that combines auto-regressive temporal reasoning with continuous latent generation, improving temporal coherence. To further enhance generalization, HO-Flow predicts object motions relative to the initial frame, enabling effective pre-training on large-scale synthetic data. Experiments on the GRAB, OakInk, and DexYCB benchmarks demonstrate that HO-Flow achieves state-of-the-art performance in both physical plausibility and motion diversity for interaction motion synthesis.

### 🤖 AI 总结

**一句话总结**：HO-Flow通过潜在流匹配技术实现从文本和3D物体生成逼真的手-物体交互运动序列，达到物理合理性和运动多样性的最优性能。

**研究动机**：现有手-物体交互生成方法在运动表示学习和时间推理方面存在局限，难以同时保证时间一致性和高保真物理合理性。

**核心方法**：HO-Flow采用交互感知VAE编码手-物体运动到统一潜在流形，并结合掩码流匹配模型实现自回归时间推理和连续潜在生成，同时通过相对初始帧的物体运动预测增强泛化能力。

**主要结论**：在GRAB、OakInk和DexYCB等基准数据集上验证了方法的有效性，实现了手-物体交互运动合成的物理合理性和运动多样性的最优性能。

**关键词**：手-物体交互, 流匹配, 变分自编码器, 3D运动生成, 时序推理, 物理可信度, 运动合成, 潜在表示, 自回归生成, 文本驱动生成

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10836v1) | [下载PDF](https://arxiv.org/pdf/2604.10836v1.pdf)

---

## [18. Uncertainty-Guided Attention and Entropy-Weighted Loss for Precise Plant Seedling Segmentation](https://arxiv.org/abs/2604.10823v1)

**作者**：Mohamed Ehab, Ali Hamdi  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-04-12

### 📄 论文摘要

Plant seedling segmentation supports automated phenotyping in precision agriculture. Standard segmentation models face difficulties due to intricate background images and fine structures in leaves. We introduce UGDA-Net (Uncertainty-Guided Dual Attention Network with Entropy-Weighted Loss and Deep Supervision). Three novel components make up UGDA-Net. The first component is Uncertainty-Guided Dual Attention (UGDA). UGDA uses channel variance to modulate feature maps. The second component is an entropy-weighted hybrid loss function. This loss function focuses on high-uncertainty boundary pixels. The third component employs deep supervision for intermediate encoder layers. We performed a comprehensive systematic ablation study. This study focuses on two widely-used architectures, U-Net and LinkNet. It analyzes five incremental configurations: Baseline, Loss-only, Attention-only, Deep Supervision, and UGDA-Net. We trained UGDA-net using a high-resolution plant seedling image dataset containing 432 images. We demonstrate improved segmentation performance and accuracy. With an increase in Dice coefficient of 9.3% above baseline. LinkNet's variance is 13.2% above baseline. Overlays that are qualitative in nature show the reduced false positives at the leaf boundary. Uncertainty heatmaps are consistent with the complex morphology. UGDA-Net aids in the segmentation of delicate structures in plants and provides a high-def solution. The results showed that uncertainty-guided attention and uncertainty-weighted loss are two complementing systems.

### 🤖 AI 总结

**一句话总结**：提出了UGDA-Net，通过不确定性引导的双注意力机制和熵加权损失函数，显著提升植物幼苗分割精度（Dice系数提升9.3%）。

**研究动机**：植物幼苗分割任务面临复杂背景图像和叶片细结构的双重挑战，标准分割模型难以准确区分边界和微小结构。

**核心方法**：UGDA-Net包含三个创新组件：不确定性引导双注意力模块（使用通道方差调制特征图）、熵加权混合损失函数（聚焦高不确定性边界像素）、以及中间编码器的深度监督机制。

**主要结论**：在U-Net和LinkNet架构上的实验表明，该方法显著提升分割性能，边界误检率降低，不确定性热图与复杂形态一致，三个组件相互补充协同提升分割精度。

**关键词**：Uncertainty-Guided, Attention, Entropy-Weighted, Loss, Precise, Plant, Seedling, Segmentation

**评分**：12

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10823v1) | [下载PDF](https://arxiv.org/pdf/2604.10823v1.pdf)

---

## [19. Analytical Modeling and Correction of Distance Error in Homography-Based Ground-Plane Mapping](https://arxiv.org/abs/2604.10805v1)

**作者**：Mateusz Szulc, Marcin Iwanowski  
**分类**：cs.CV  
**发布时间**：2026-04-12

### 📄 论文摘要

Accurate distance estimation from monocular cameras is essential for intelligent monitoring systems. In many deployments, image coordinates are mapped to ground positions using planar homographies initialized by manual selection of corresponding regions. Small inaccuracies in this initialization propagate into systematic distance distortions. This paper derives an explicit relationship between homography perturbations and the resulting distance error, showing that the error grows approximately quadratically with the true distance from the camera. Based on this model, two simple correction strategies are evaluated: regression-based estimation of the quadratic error function and direct optimization of the homography via coordinate-based gradient descent. A large-scale simulation study with more than 19 million test samples demonstrates that regression achieves higher peak accuracy when the model is reliably fitted, whereas gradient descent provides greater robustness against poor initial calibration. This suggests that improving geometric calibration may yield greater performance gains than increasing model complexity in many practical systems.

### 🤖 AI 总结

**一句话总结**：该研究推导出单目相机中平面单应性扰动与距离误差的显式关系，发现误差随真实距离近似二次增长，并验证了回归校正与梯度下降优化两种修正策略的优劣。

**研究动机**：在智能监控系统中，手动选择的单应性初始参数存在微小误差，会导致系统性的距离估计偏差，影响应用可靠性。

**核心方法**：建立扰动-误差解析模型，基于此对比回归估计二次误差函数与基于坐标的梯度下降直接优化单应性两种校正方案，通过1900万样本的仿真实验进行评估。

**主要结论**：回归方法在模型可靠拟合时峰值精度更高，而梯度下降对初始校准偏差更具鲁棒性，表明提升几何校准质量比增加模型复杂度更具实际效益。

**关键词**：单应性校准, 距离误差建模, 地面平面映射, 单目视觉测距, 几何标定, 智能监控, 回归误差校正, 梯度下降优化, 相机标定, 系统误差补偿

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10805v1) | [下载PDF](https://arxiv.org/pdf/2604.10805v1.pdf)

---

## [20. WBCBench 2026: A Challenge for Robust White Blood Cell Classification Under Class Imbalance](https://arxiv.org/abs/2604.10797v1)

**作者**：Xin Tian, Xudong Ma, Tianqi Yang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-12

### 📄 论文摘要

We present WBCBench 2026, an ISBI challenge and benchmark for automated WBC classification designed to stress-test algorithms under three key difficulties: (i) severe class imbalance across 13 morphologically fine-grained WBC classes, (ii) strict patient-level separation between training, validation and test sets, and (iii) synthetic scanner- and setting-induced domain shift via controlled noise, blur and illumination perturbations. All images are single-site microscopic blood smear acquisitions with standardised staining and expert hematopathologist annotations. This paper reviews the challenge and summarises the proposed solutions and final outcomes. The benchmark is organised into two phases. Phase 1 provides a pristine training set. Phase 2 introduces degraded images with split-specific severity distributions for train, validation and test, emulating a realistic shift between development and deployment conditions. We specify a standardised submission schema, open-source evaluator, and macro-averaged F1 score as the primary ranking metric.

### 🤖 AI 总结

**一句话总结**：WBCBench 2026是一个用于评估白细胞分类算法在严重类别不平衡、患者级别数据分离和域转移条件下鲁棒性的ISBI挑战基准。

**研究动机**：现有白细胞分类方法在真实临床应用中面临严峻挑战，包括13类细粒度形态学类别严重不平衡、严格的患者级别数据分离要求以及不同扫描设备和设置间的域转移问题，需要标准化基准来系统评估算法鲁棒性。

**核心方法**：该基准分两阶段设计：Phase 1提供标准化染色和专家标注的原始训练集，Phase 2引入受控噪声、模糊和光照扰动生成的退化图像，通过宏平均F1分数作为主要排名指标，配合开源评估器和标准化提交格式进行评估。

**主要结论**：WBCBench 2026为白细胞分类算法提供了全面的鲁棒性评估框架，揭示了当前方法在面对类别不平衡和域转移时的局限性，为推动临床适用的自动化血液分析技术发展提供了重要基准。

**关键词**：WBCBench, Challenge, Robust, White, Blood, Cell, Classification, Under

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10797v1) | [下载PDF](https://arxiv.org/pdf/2604.10797v1.pdf)

---

## [21. ReplicateAnyScene: Zero-Shot Video-to-3D Composition via Textual-Visual-Spatial Alignment](https://arxiv.org/abs/2604.10789v1)

**作者**：Mingyu Dong, Chong Xia, Mingyuan Jia 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-12

### 📄 论文摘要

Humans exhibit an innate capacity to rapidly perceive and segment objects from video observations, and even mentally assemble them into structured 3D scenes. Replicating such capability, termed compositional 3D reconstruction, is pivotal for the advancement of Spatial Intelligence and Embodied AI. However, existing methods struggle to achieve practical deployment due to the insufficient integration of cross-modal information, leaving them dependent on manual object prompting, reliant on auxiliary visual inputs, and restricted to overly simplistic scenes by training biases. To address these limitations, we propose ReplicateAnyScene, a framework capable of fully automated and zero-shot transformation of casually captured videos into compositional 3D scenes. Specifically, our pipeline incorporates a five-stage cascade to extract and structurally align generic priors from vision foundation models across textual, visual, and spatial dimensions, grounding them into structured 3D representations and ensuring semantic coherence and physical plausibility of the constructed scenes. To facilitate a more comprehensive evaluation of this task, we further introduce the C3DR benchmark to assess reconstruction quality from diverse aspects. Extensive experiments demonstrate the superiority of our method over existing baselines in generating high-quality compositional 3D scenes.

### 🤖 AI 总结

**一句话总结**：ReplicateAnyScene是一个能从随意拍摄视频中全自动、零样本生成高质量组合式3D场景的框架。

**研究动机**：人类能快速从视频中感知分割物体并组装成3D场景，但现有方法因跨模态信息整合不足，存在依赖手动提示、需辅助输入、场景简单等局限。

**核心方法**：通过五级级联pipeline，从视觉基础模型中提取文本、视觉和空间维度的通用先验并进行结构化对齐，grounding到结构化3D表示中，确保语义一致性和物理合理性。

**主要结论**：引入C3DR基准进行多维度评估，实验证明该方法在生成高质量组合式3D场景方面显著优于现有基线方法。

**关键词**：零样本学习, 视频转三维, 三维场景组合, 跨模态对齐, 视觉基础模型, 空间智能, 具身智能, 三维重建, 自动化

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10789v1) | [下载PDF](https://arxiv.org/pdf/2604.10789v1.pdf)

---

## [22. Uncertainty-quantified Pulse Signal Recovery from Facial Video using Regularized Stochastic Interpolants](https://arxiv.org/abs/2604.10777v1)

**作者**：Vineet R. Shenoy, Cheng Peng, Rama Chellappa 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-12

### 📄 论文摘要

Imaging Photoplethysmography (iPPG), an optical procedure which recovers a human's blood volume pulse (BVP) waveform using pixel readout from a camera, is an exciting research field with many researchers performing clinical studies of iPPG algorithms. While current algorithms to solve the iPPG task have shown outstanding performance on benchmark datasets, no state-of-the art algorithms, to the best of our knowledge, performs test-time sampling of solution space, precluding an uncertainty analysis that is critical for clinical applications. We address this deficiency though a new paradigm named Regularized Interpolants with Stochasticity for iPPG (RIS-iPPG). Modeling iPPG recovery as an inverse problem, we build probability paths that evolve the camera pixel distribution to the ground-truth signal distribution by predicting the instantaneous flow and score vectors of a time-dependent stochastic process; and at test-time, we sample the posterior distribution of the correct BVP waveform given the camera pixel intensity measurements by solving a stochastic differential equation. Given that physiological changes are slowly varying, we show that iPPG recovery can be improved through regularization that maximizes the correlation between the residual flow vector predictions of two adjacent time windows. Experimental results on three datasets show that RIS-iPPG provides superior reconstruction quality and uncertainty estimates of the reconstruction, a critical tool for the widespread adoption of iPPG algorithms in clinical and consumer settings.

### 🤖 AI 总结

**一句话总结**：提出RIS-iPPG方法，通过随机插值和正则化从面部视频中恢复脉搏信号并量化不确定性，填补了现有算法在测试时缺乏采样能力的技术空白。

**研究动机**：当前最先进的iPPG算法无法在测试时对解空间进行采样，导致无法提供对临床应用至关重要的不确定性分析。

**核心方法**：将iPPG恢复建模为逆问题，通过预测时间依赖随机过程的瞬时流向量和分数向量构建概率路径，并利用相邻时间窗口残差流向量的相关性正则化提升重建质量。

**主要结论**：RIS-iPPG在三个数据集上实现了更优的重建质量和不确定性估计，为iPPG算法在临床和消费场景的广泛采用提供了关键工具。

**关键词**：BVP波形恢复, 不确定性量化, 随机微分方程, 逆问题, 概率路径, 分数向量, 正则化, 面部视频, 流向量, 时间窗口, 信号重建

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10777v1) | [下载PDF](https://arxiv.org/pdf/2604.10777v1.pdf)

---

## [23. HOG-Layout: Hierarchical 3D Scene Generation, Optimization and Editing via Vision-Language Models](https://arxiv.org/abs/2604.10772v1)

**作者**：Haiyan Jiang, Deyu Zhang, Dongdong Weng 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-12

### 📄 论文摘要

3D layout generation and editing play a crucial role in Embodied AI and immersive VR interaction. However, manual creation requires tedious labor, while data-driven generation often lacks diversity. The emergence of large models introduces new possibilities for 3D scene synthesis. We present HOG-Layout that enables text-driven hierarchical scene generation, optimization and real-time scene editing with large language models (LLMs) and vision-language models (VLMs). HOG-Layout improves scene semantic consistency and plausibility through retrieval-augmented generation (RAG) technology, incorporates an optimization module to enhance physical consistency, and adopts a hierarchical representation to enhance inference and optimization, achieving real-time editing. Experimental results demonstrate that HOG-Layout produces more reasonable environments compared with existing baselines, while supporting fast and intuitive scene editing.

### 🤖 AI 总结

**一句话总结**：HOG-Layout提出一种利用LLM和VLM实现文本驱动的层次化3D场景生成、优化和实时编辑的系统。

**研究动机**：3D布局生成在Embodied AI和VR交互中至关重要，但手动创建耗时且数据驱动方法缺乏多样性，而大模型为3D场景合成提供了新机遇。

**核心方法**：通过检索增强生成(RAG)提升语义一致性，结合优化模块保证物理合理性，采用层次化表示实现高效推理和实时场景编辑。

**主要结论**：实验证明HOG-Layout能生成比基线更合理的3D环境，同时支持快速直观的场景编辑功能。

**关键词**：3D布局生成, 场景编辑, LLM, 视觉-语言模型, RAG, 分层表示, 具身AI, VR交互, 文本驱动, 物理一致性

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10772v1) | [下载PDF](https://arxiv.org/pdf/2604.10772v1.pdf)

---

## [24. At FullTilt: Real-Time Open-Set 3D Macromolecule Detection Directly from Tilted 2D Projections](https://arxiv.org/abs/2604.10766v1)

**作者**：Ming-Yang Ho, Alberto Bartesaghi  
**分类**：cs.CV  
**发布时间**：2026-04-12

### 📄 论文摘要

Open-set 3D macromolecule detection in cryogenic electron tomography eliminates the need for target-specific model retraining. However, strict VRAM constraints prohibit processing an entire 3D tomogram, forcing current methods to rely on slow sliding-window inference over extracted subvolumes. To overcome this, we propose FullTilt, an end-to-end framework that redefines 3D detection by operating directly on aligned 2D tilt-series. Because a tilt-series contains significantly fewer images than slices in a reconstructed tomogram, FullTilt eliminates redundant volumetric computation, accelerating inference by orders of magnitude. To process the entire tilt-series simultaneously, we introduce a tilt-series encoder to efficiently fuse cross-view information. We further propose a multiclass visual prompt encoder for flexible prompting, a tilt-aware query initializer to effectively anchor 3D queries, and an auxiliary geometric primitives module to enhance the model's understanding of multi-view geometry while improving robustness to adverse imaging artifacts. Extensive evaluations on three real-world datasets demonstrate that FullTilt achieves state-of-the-art zero-shot performance while drastically reducing runtime and VRAM requirements, paving the way for rapid, large-scale visual proteomics analysis. All code and data will be publicly available upon publication.

### 🤖 AI 总结

**一句话总结**：FullTilt通过直接在2D倾斜系列上操作实现实时开集3D大分子检测，大幅加速推理并降低显存需求。

**研究动机**：现有cryo-ET方法受限于VRAM约束，需用滑动窗口逐个处理子体积，速度极慢；同时希望消除目标特定的模型重训练需求。

**核心方法**：提出端到端框架FullTilt，包含倾斜系列编码器融合跨视图信息、多类视觉提示编码器实现灵活提示、倾斜感知查询初始化器锚定3D查询，以及辅助几何基元模块增强多视图几何理解。

**主要结论**：在三个真实数据集上验证，FullTilt达到最先进的零样本检测性能，显著降低运行时间和VRAM需求，为大规模视觉蛋白质组学分析铺平道路。

**关键词**：开放集检测, 冷冻电子断层扫描, 3D大分子检测, 倾斜系列编码器, 视觉提示编码器, 几何基元模块, 端到端框架, 零样本学习, 实时推理, 视觉蛋白质组学

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10766v1) | [下载PDF](https://arxiv.org/pdf/2604.10766v1.pdf)

---

## [25. Lung Cancer Detection Using Deep Learning](https://arxiv.org/abs/2604.10765v1)

**作者**：Imama Ajmi, Abhishek Das  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-04-12

### 📄 论文摘要

Lung cancer, the second leading cause of cancer-related deaths, is primarily linked to long-term tobacco smoking (85% of cases). Surprisingly, 10-15% of cases occur in non-smokers. In 2020, approximately 2 million people were affected globally, resulting in 1.5 million deaths. The survival rate, at around 20%, lags behind other cancers, partly due to late-stage symptom manifestation. Necessitates early and accurate detection for effective treatment. Performance metrics such as accuracy, precision, recall (sensitivity), and F1-score are computed to provide a comprehensive evaluation of each model's capabilities. By comparing these metrics, this study offers insights into the strengths and limitations of each approach, contributing to the advancement of lung cancer detection techniques. In this paper, we are going to discuss the methodologies of lung cancer detection using different deep learning algorithms - InceptionV3, MobileNetV2, VGG16, ResNet152 - are explored for their efficacy in classifying lung cancer cases. Our Proposed Model algorithm based is a 16 layers architecture based on CNN model. Our Proposed model exhibits several key highlights that contribute to its novelty. By integrating multiple layer types such as convolutional, pooling, flatten, dropout, fully connected and dense layers, the model leverages the strengths of each layer to enhance its predictive capabilities. Novelty of our proposed model is that its accuracy is increasing consistently with the increasing no of epochs. We have tested the model performance up to epoch no 30. Our proposed model also overcome the overfitting problem.

### 🤖 AI 总结

**一句话总结**：该研究提出一种16层CNN深度学习架构用于肺癌检测，通过对比InceptionV3、MobileNetV2、VGG16、ResNet152等模型，验证了所提模型在准确性和防止过拟合方面的优势。

**研究动机**：肺癌是全球癌症死亡第二大原因，2020年导致约150万人死亡，生存率仅20%主要因晚期才出现症状，因此需要早期准确的检测方法来改善治疗效果。

**核心方法**：提出16层CNN架构整合卷积、池化、平坦化、dropout和全连接等多种层类型，对比测试InceptionV3、MobileNetV2、VGG16、ResNet152等多个深度学习模型，使用准确率、精确率、召回率和F1分数等指标进行综合评估。

**主要结论**：提出的16层CNN模型准确率随训练轮数增加而稳定提升，成功克服了过拟合问题，在肺癌分类任务中展现出良好的性能。

**关键词**：肺癌检测, 深度学习, 医学影像分析, 分类模型, 性能评估, 预训练模型比较, 过拟合, 准确率

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10765v1) | [下载PDF](https://arxiv.org/pdf/2604.10765v1.pdf)

---

## [26. MMRareBench: A Rare-Disease Multimodal and Multi-Image Medical Benchmark](https://arxiv.org/abs/2604.10755v1)

**作者**：Junzhi Ning, Jiashi Lin, Yingying Fang 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-12

### 📄 论文摘要

Multimodal large language models (MLLMs) have advanced clinical tasks for common conditions, but their performance on rare diseases remains largely untested. In rare-disease scenarios, clinicians often lack prior clinical knowledge, forcing them to rely strictly on case-level evidence for clinical judgments. Existing benchmarks predominantly evaluate common-condition, single-image settings, leaving multimodal and multi-image evidence integration under rare-disease data scarcity systematically unevaluated. We introduce MMRareBench, to our knowledge the first rare-disease benchmark jointly evaluating multimodal and multi-image clinical capability across four workflow-aligned tracks: diagnosis, treatment planning, cross-image evidence alignment, and examination suggestion. The benchmark comprises 1,756 question-answer pairs with 7,958 associated medical images curated from PMC case reports, with Orphanet-anchored ontology alignment, track-specific leakage control, evidence-grounded annotations, and a two-level evaluation protocol. A systematic evaluation of 23 MLLMs reveals fragmented capability profiles and universally low treatment-planning performance, with medical-domain models trailing general-purpose MLLMs substantially on multi-image tracks despite competitive diagnostic scores. These patterns are consistent with a capacity dilution effect: medical fine-tuning can narrow the diagnostic gap but may erode the compositional multi-image capability that rare-disease evidence integration demands.

### 🤖 AI 总结

**一句话总结**：MMRareBench是首个针对罕见病的多模态多图像医学基准测试，系统评估了23个MLLMs在诊断、治疗计划、跨图像证据对齐和检查建议四个工作流程中的临床能力。

**研究动机**：现有医学基准测试主要针对常见疾病和单图像场景，罕见病场景下临床医生缺乏先验知识需严格依赖病例级证据，多模态多图像证据整合能力在罕见病数据稀缺条件下的表现尚未被系统评估。

**核心方法**：构建包含1,756个问答对和7,958张医学图像的基准数据集，基于Orphanet罕见病本体对齐，设置四个工作流对齐的评估track，采用track特定泄漏控制和两层次评估协议。

**主要结论**：23个MLLMs评估显示能力碎片化，治疗计划性能普遍较低；医学领域模型在多图像track上显著落后于通用MLLMs，存在容量稀释效应：医学微调可能缩小诊断差距但侵蚀了罕见病证据整合所需的多图像组合能力。

**关键词**：罕见病, 多模态大语言模型, 医学基准, 多图像证据整合, 临床诊断, 治疗计划, 能力稀释效应, PMC病例报告, 证据对齐, 医学图像分析

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10755v1) | [下载PDF](https://arxiv.org/pdf/2604.10755v1.pdf)

---

## [27. Turning Generators into Retrievers: Unlocking MLLMs for Natural Language-Guided Geo-Localization](https://arxiv.org/abs/2604.10721v1)

**作者**：Yuqi Chen, Xiaohan Zhang, Ahmad Arrabi 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-12

### 📄 论文摘要

Natural-language Guided Cross-view Geo-localization (NGCG) aims to retrieve geo-tagged satellite imagery using textual descriptions of ground scenes. While recent NGCG methods commonly rely on CLIP-style dual-encoder architectures, they often suffer from weak cross-modal generalization and require complex architectural designs. In contrast, Multimodal Large Language Models (MLLMs) offer powerful semantic reasoning capabilities but are not directly optimized for retrieval tasks. In this work, we present a simple yet effective framework to adapt MLLMs for NGCG via parameter-efficient finetuning. Our approach optimizes latent representations within the MLLM while preserving its pretrained multimodal knowledge, enabling strong cross-modal alignment without redesigning model architectures. Through systematic analysis of diverse variables, from model backbone to feature aggregation, we provide practical and generalizable insights for leveraging MLLMs in NGCG. Our method achieves SOTA on GeoText-1652 with a 12.2% improvement in Text-to-Image Recall@1 and secures top performance in 5 out of 12 subtasks on CVG-Text, all while surpassing baselines with far fewer trainable parameters. These results position MLLMs as a robust foundation for semantic cross-view retrieval and pave the way for MLLM-based NGCG to be adopted as a scalable, powerful alternative to traditional dual-encoder designs. Project page and code are available at https://yuqichen888.github.io/NGCG-MLLMs-web/.

### 🤖 AI 总结

**一句话总结**：该研究提出将多模态大语言模型(MLLMs)通过参数高效微调转化为跨视角地理定位检索器，在保持模型架构不变的情况下实现了显著的性能提升。

**研究动机**：现有CLIP风格双编码器方法存在跨模态泛化弱、架构设计复杂的问题，而MLLMs虽具备强大语义推理能力却未针对检索任务优化，因此需要探索如何高效利用MLLMs进行自然语言引导的地理定位。

**核心方法**：通过参数高效微调（如LoRA）优化MLLM内部潜在表示，在保留预训练多模态知识的同时实现跨模态对齐，无需重新设计模型架构；系统分析模型骨干、特征聚合等多变量因素以提供通用性指导。

**主要结论**：在GeoText-1652上Text-to-Image Recall@1提升12.2%，CVG-Text的12个子任务中5项取得第一，且使用更少可训练参数超越基线，验证了MLLMs作为跨视角检索基础模型的可行性。

**关键词**：跨视图地理定位, 参数高效微调, 跨模态对齐, 卫星图像检索, 文本-图像检索, 语义推理, 双编码器, 特征聚合, 潜在表示优化

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10721v1) | [下载PDF](https://arxiv.org/pdf/2604.10721v1.pdf)

---

## cs.LG

## [28. Query Lower Bounds for Diffusion Sampling](https://arxiv.org/abs/2604.10857v1)

**作者**：Zhiyang Xun, Eric Price  
**分类**：cs.LG, cs.AI, cs.DS, math.ST, stat.ML  
**发布时间**：2026-04-12

### 📄 论文摘要

Diffusion models generate samples by iteratively querying learned score estimates. A rapidly growing literature focuses on accelerating sampling by minimizing the number of score evaluations, yet the information-theoretic limits of such acceleration remain unclear.   In this work, we establish the first score query lower bounds for diffusion sampling. We prove that for $d$-dimensional distributions, given access to score estimates with polynomial accuracy $\varepsilon=d^{-O(1)}$ (in any $L^p$ sense), any sampling algorithm requires $\widetildeΩ(\sqrt{d})$ adaptive score queries. In particular, our proof shows that any sampler must search over $\widetildeΩ(\sqrt{d})$ distinct noise levels, providing a formal explanation for why multiscale noise schedules are necessary in practice.

### 🤖 AI 总结

**一句话总结**：该论文首次证明了扩散模型采样需要至少Ω(√d)次自适应分数查询的理论下界，为多尺度噪声调度在实践中的必要性提供了形式化解释。

**研究动机**：扩散模型通过迭代查询学习到的分数估计来生成样本，虽然已有大量研究致力于减少分数评估次数以加速采样，但此类加速的信息论极限尚不明确。

**核心方法**：作者利用信息论方法，证明对于d维分布，当分数估计具有多项式精度ε=d^{-O(1)}时，任何采样算法都需要搜索Ω(√d)个不同的噪声水平。

**主要结论**：建立了扩散采样中分数查询的首个理论下界Ω(√d)，表明多尺度噪声调度对于实现高效采样是必要而非可选的，为理解扩散模型的计算限制提供了理论基础。

**关键词**：Query, Lower, Bounds, Diffusion, Sampling, models, generate, samples

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10857v1) | [下载PDF](https://arxiv.org/pdf/2604.10857v1.pdf)

---

## [29. Slithering Through Gaps: Capturing Discrete Isolated Modes via Logistic Bridging](https://arxiv.org/abs/2604.10821v1)

**作者**：Pinaki Mohanty, Ruqi Zhang  
**分类**：cs.LG, stat.CO, stat.ML  
**发布时间**：2026-04-12

### 📄 论文摘要

High-dimensional and complex discrete distributions often exhibit multimodal behavior due to inherent discontinuities, posing significant challenges for sampling. Gradient-based discrete samplers, while effective, frequently become trapped in local modes when confronted with rugged or disconnected energy landscapes. This limits their ability to achieve adequate mixing and convergence in high-dimensional multimodal discrete spaces. To address these challenges, we propose \emph{Hyperbolic Secant-squared Gibbs-Sampling (HiSS)}, a novel family of sampling algorithms that integrates a \emph{Metropolis-within-Gibbs} framework to enhance mixing efficiency. HiSS leverages a logistic convolution kernel to couple the discrete sampling variable with the continuous auxiliary variable in a joint distribution. This design allows the auxiliary variable to encapsulate the true target distribution while facilitating easy transitions between distant and disconnected modes. We provide theoretical guarantees of convergence and demonstrate empirically that HiSS outperforms many popular alternatives on a wide variety of tasks, including Ising models, binary neural networks, and combinatorial optimization.

### 🤖 AI 总结

**一句话总结**：提出HiSS采样算法，通过logistic卷积核耦合离散与连续变量，在Metropolis-within-Gibbs框架下有效解决高维离散分布中多模态、断开能量景观的采样难题。

**研究动机**：高维离散分布常呈现多模态和不连续性，传统基于梯度的采样器易被困在局部模式，难以在遥远模式间跳转，导致混合效率低下。

**核心方法**：HiSS将离散变量与连续辅助变量通过logistic卷积核耦合形成联合分布，在Metropolis-within-Gibbs框架下交替采样，利用连续辅助变量的连续性特性实现跨模式跳转。

**主要结论**：理论证明收敛性，实验表明HiSS在Ising模型、二值神经网络和组合优化等任务上显著优于现有方法。

**关键词**：离散采样, 多模态分布, 辅助变量, 高维采样, 模式混合, 二值神经网络, 组合优化, 收敛性保证

**评分**：8

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10821v1) | [下载PDF](https://arxiv.org/pdf/2604.10821v1.pdf)

---

## [30. Online Covariance Estimation in Averaged SGD: Improved Batch-Mean Rates and Minimax Optimality via Trajectory Regression](https://arxiv.org/abs/2604.10814v1)

**作者**：Yijin Ni, Xiaoming Huo  
**分类**：cs.LG, math.ST  
**发布时间**：2026-04-12

### 📄 论文摘要

We study online covariance matrix estimation for Polyak--Ruppert averaged stochastic gradient descent (SGD). The online batch-means estimator of Zhu, Chen and Wu (2023) achieves an operator-norm convergence rate of $O(n^{-(1-α)/4})$, which yields $O(n^{-1/8})$ at the optimal learning-rate exponent $α\rightarrow 1/2^+$. A rigorous per-block bias analysis reveals that re-tuning the block-growth parameter improves the batch-means rate to $O(n^{-(1-α)/3})$, achieving $O(n^{-1/6})$. The modified estimator requires no Hessian access and preserves $O(d^2)$ memory. We provide a complete error decomposition into variance, stationarity bias, and nonlinearity bias components. A weighted-averaging variant that avoids hard truncation is also discussed. We establish the minimax rate $Θ(n^{-(1-α)/2})$ for Hessian-free covariance estimation from the SGD trajectory: a Le Cam lower bound gives $Ω(n^{-(1-α)/2})$, and a trajectory-regression estimator--which estimates the Hessian by regressing SGD increments on iterates--achieves $O(n^{-(1-α)/2})$, matching the lower bound. The construction reveals that the bottleneck is the sublinear accumulation of information about the Hessian from the SGD drift.

### 🤖 AI 总结

**一句话总结**：本文改进了Polyak-Ruppert平均化SGD中在线协方差矩阵估计的收敛率，通过重新调整块增长参数和轨迹回归方法证明了最小极大最优性。

**研究动机**：在线协方差估计对统计推断至关重要，但现有批量均值估计器在最优学习率下仅达到O(n^{-1/8})的收敛速率，需要理论突破。

**核心方法**：通过严格的逐块偏差分析重新调整块增长参数以改进批量均值估计器，并提出轨迹回归估计器通过回归SGD增量于迭代点来Hessian-free地估计协方差。

**主要结论**：建立了Hessian-free协方差估计的最小极大率Θ(n^{-(1-α)/2})，批量均值估计器改进至O(n^{-1/6})，瓶颈在于SGD漂移中Hessian信息的次线性累积。

**关键词**：SGD协方差估计, 批量均值估计, 轨迹回归, 最小最大速率, 操作范数收敛, 偏差分解, Online, Covariance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10814v1) | [下载PDF](https://arxiv.org/pdf/2604.10814v1.pdf)

---

