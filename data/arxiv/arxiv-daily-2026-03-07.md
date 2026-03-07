# arXiv AI 论文日报 | 2026-03-07

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (13 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.AI](#csAI) (4 篇)
- [cs.CL](#csCL) (5 篇)

---

## cs.AI

## [1. Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation](https://arxiv.org/abs/2603.05485v1)

**作者**：Benjamin Feuer, Lucas Rosenblatt, Oussama Elachqar  
**分类**：cs.AI  
**发布时间**：2026-03-05

### 📄 论文摘要

As AI models progress beyond simple chatbots into more complex workflows, we draw ever closer to the event horizon beyond which AI systems will be utilized in autonomous, self-maintaining feedback loops. Any autonomous AI system will depend on automated, verifiable rewards and feedback; in settings where ground truth is sparse or non-deterministic, one practical source of such rewards is an LLM-as-a-Judge. Although LLM judges continue to improve, the literature has yet to introduce systems capable of enforcing standards with strong guarantees, particularly when bias vectors are unknown or adversarially discovered. To remedy this issue, we propose average bias-boundedness (A-BB), an algorithmic framework which formally guarantees reductions of harm/impact as a result of any measurable bias in an LLM judge. Evaluating on Arena-Hard-Auto with four LLM judges, we achieve (tau=0.5, delta=0.01) bias-bounded guarantees while retaining 61-99% correlation with original rankings across formatting and schematic bias settings, with most judge-bias combinations exceeding 80%. The code to reproduce our findings is available at https://github.com/penfever/bias-bounded-evaluation.

### 🤖 AI 总结

**一句话总结**：提出平均偏差有界（A-BB）评估框架，为LLM裁判在未知或对抗性偏差下提供可证明的偏差/伤害上界，同时尽量保持原有排序一致性。

**研究动机**：在自主AI反馈闭环中需要自动、可验证的奖励信号，而LLM-as-a-Judge在无明确真值场景很实用但可能带来不可控偏差与潜在伤害。现有工作缺少在偏差向量未知甚至被对抗性挖掘时仍能提供强保证的裁判评估机制。

**核心方法**：提出A-BB算法框架，通过对“可测量的裁判偏差”施加形式化约束/上界，保证评估过程对偏差导致的影响（harm/impact）进行可证明的削减。并在Arena-Hard-Auto上用4个LLM裁判，在格式偏差与schema偏差等设置下验证其在给定(τ=0.5, δ=0.01)条件下的偏差有界保证与排名相关性权衡。

**主要结论**：A-BB在实现(τ=0.5, δ=0.01)偏差有界保证的同时，仍与原始排名保持61–99%的相关性，且大多数裁判-偏差组合超过80%。结果表明可在保留评估效用的前提下，为LLM裁判提供可证明的抗偏差安全性约束。

**关键词**：偏差有界评测, 平均偏差有界性（A-BB）, 可证明无偏评估, 自动化奖励信号, 闭环自主系统, 公平性与偏差缓解, 评审鲁棒性, 排序一致性（相关性）

**评分**：46

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05485v1) | [下载PDF](https://arxiv.org/pdf/2603.05485v1.pdf)

---

## [2. Distributed Partial Information Puzzles: Examining Common Ground Construction Under Epistemic Asymmetry](https://arxiv.org/abs/2603.05450v1)

**作者**：Yifan Zhu, Mariah Bradford, Kenneth Lai 等 7 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-03-05

### 📄 论文摘要

Establishing common ground, a shared set of beliefs and mutually recognized facts, is fundamental to collaboration, yet remains a challenge for current AI systems, especially in multimodal, multiparty settings, where the collaborators bring different information to the table. We introduce the Distributed Partial Information Puzzle (DPIP), a collaborative construction task that elicits rich multimodal communication under epistemic asymmetry. We present a multimodal dataset of these interactions, annotated and temporally aligned across speech, gesture, and action modalities to support reasoning over propositional content and belief dynamics. We then evaluate two paradigms for modeling common ground (CG): (1) state-of-the-art large language models (LLMs), prompted to infer shared beliefs from multimodal updates, and (2) an axiomatic pipeline grounded in Dynamic Epistemic Logic (DEL) that incrementally performs the same task. Results on the annotated DPIP data indicate that it poses a challenge to modern LLMs' abilities to track both task progression and belief state.

### 🤖 AI 总结

**一句话总结**：提出DPIP协作构建任务与多模态数据集，用于研究信息不对称下的共同基础（common ground）构建，并发现当前LLM在跟踪任务进度与信念状态方面仍明显吃力。

**研究动机**：多方多模态协作中，每个参与者掌握的信息不同，建立共同基础对协作至关重要但现有AI系统难以稳定建模。需要一个能系统诱发“信念对齐/更新”过程并可评测的基准与数据。

**核心方法**：设计Distributed Partial Information Puzzle任务并采集语音-手势-动作时间对齐的标注数据，以支持命题内容与信念动态推理。对比两类共同基础建模范式：基于提示的LLM从多模态更新中推断共享信念 vs 基于动态认知逻辑（DEL）的公理化增量推理流水线。

**主要结论**：DPIP数据表明该任务对现代LLM构成挑战：其难以同时准确跟踪构建步骤与多方信念状态的变化。相较之下，DEL式增量推理提供了更结构化的共同基础更新机制，也凸显了LLM在显式信念建模上的不足。

**关键词**：共同基础建模, 认知不对称, 分布式部分信息谜题（DPIP）, 多模态多方协作, 多模态对话数据集, 语音-手势-动作对齐标注, 信念状态跟踪, 命题内容推理, 动态认知逻辑（DEL）, LLM多模态更新推断, 协作构建任务, 评测基准

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05450v1) | [下载PDF](https://arxiv.org/pdf/2603.05450v1.pdf)

---

## [3. Judge Reliability Harness: Stress Testing the Reliability of LLM Judges](https://arxiv.org/abs/2603.05399v1)

**作者**：Sunishchal Dev, Andrew Sloan, Joshua Kavner 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-03-05

### 📄 论文摘要

We present the Judge Reliability Harness, an open source library for constructing validation suites that test the reliability of LLM judges. As LLM based scoring is widely deployed in AI benchmarks, more tooling is needed to efficiently assess the reliability of these methods. Given a benchmark dataset and an LLM judge configuration, the harness generates reliability tests that evaluate both binary judgment accuracy and ordinal grading performance for free-response and agentic task formats. We evaluate four state-of-the-art judges across four benchmarks spanning safety, persuasion, misuse, and agentic behavior, and find meaningful variation in performance across models and perturbation types, highlighting opportunities to improve the robustness of LLM judges. No judge that we evaluated is uniformly reliable across benchmarks using our harness. For example, our preliminary experiments on judges revealed consistency issues as measured by accuracy in judging another LLM's ability to complete a task due to simple text formatting changes, paraphrasing, changes in verbosity, and flipping the ground truth label in LLM-produced responses. The code for this tool is available at: https://github.com/RANDCorporation/judge-reliability-harness

### 🤖 AI 总结

**一句话总结**：本文提出开源工具 Judge Reliability Harness，用系统化的扰动与测试套件对LLM评审器（LLM judges）的可靠性进行压力测试，发现不同评审模型在不同基准与扰动下表现差异显著且无一“全能可靠”。

**研究动机**：LLM评审打分已广泛用于AI基准与评测，但缺少高效、标准化的工具来检验其在格式变化、改写、冗长度变化等情况下的稳定性与一致性。

**核心方法**：给定基准数据集与评审器配置，Harness 自动生成可靠性测试，覆盖二分类判断准确性与序数评分（ordinal grading）表现，并适配自由回答与agent任务两种格式；随后在安全、说服、滥用与agent行为等四类基准上评测多种SOTA评审器并比较不同扰动类型影响。

**主要结论**：实验显示评审器的可靠性随模型、基准与扰动类型显著波动，没有任何一个评审器能在所有基准上保持稳定可靠；一些简单改动（如文本格式、释义、verbosity变化、或在LLM生成回复中翻转标签）即可引发一致性与准确性问题，表明评审鲁棒性仍有较大改进空间。

**关键词**：评审可靠性, 压力测试, 验证套件, 鲁棒性评估, 一致性评估, 扰动测试, 二元判决准确率, 序数评分, 自由回答评测

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05399v1) | [下载PDF](https://arxiv.org/pdf/2603.05399v1.pdf)

---

## [4. Legal interpretation and AI: from expert systems to argumentation and LLMs](https://arxiv.org/abs/2603.05392v1)

**作者**：Václav Janeček, Giovanni Sartor  
**分类**：cs.AI  
**发布时间**：2026-03-05

### 📄 论文摘要

AI and Law research has encountered legal interpretation in different ways, in the context of its evolving approaches and methodologies. Research on expert system has focused on legal knowledge engineering, with the goal of ensuring that human-generated interpretations can be precisely transferred into knowledge-bases, to be consistently applied. Research on argumentation has aimed at representing the structure of interpretive arguments, as well as their dialectical interactions, to assess of the acceptability of interpretive claims within argumentation frameworks. Research on machine learning has focused on the automated generation of interpretive suggestions and arguments, through general and specialised language models, now being increasingly deployed in legal practice.

### 🤖 AI 总结

**一句话总结**：论文回顾了AI与法律研究中“法律解释”的三条主线：从专家系统的知识工程，到论证框架的可接受性评估，再到以LLM为代表的机器学习生成式解释与论证。

**研究动机**：法律解释是法律实践的核心但高度依赖语境与论证，AI与法律领域需要在不同技术范式下刻画并支持解释的产生、表达与评估。随着LLM进入法律实务，更需要对既有方法与新方法的能力边界进行梳理对比。

**核心方法**：采用综述式分析，按研究范式划分并比较三类路径：专家系统侧重将人类解释精确编码并一致执行；论证研究侧重表示解释性论证结构及其辩证交互；机器学习/语言模型侧重自动生成解释建议与论证。

**主要结论**：不同方法对应法律解释的不同需求：专家系统强调一致性与可控性，论证框架强调可辩护性与可接受性评估，LLM/ML强调生成能力与实务可用性。整体趋势是从“人工编码解释”走向“自动生成解释与论证”，并在部署中需要与论证评估等机制结合以提高可靠性。

**关键词**：法律解释, 法律知识工程, 专家系统, 知识库表示, 论证推理, 论证框架, 辩证交互, 解释性论证, 可接受性评估, 法律语言模型（LLM）, 法律实践部署

**评分**：10

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05392v1) | [下载PDF](https://arxiv.org/pdf/2603.05392v1.pdf)

---

## cs.CL

## [5. Leveraging LLM Parametric Knowledge for Fact Checking without Retrieval](https://arxiv.org/abs/2603.05471v1)

**作者**：Artem Vazhentsev, Maria Marina, Daniil Moskovskiy 等 11 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-03-05

### 📄 论文摘要

Trustworthiness is a core research challenge for agentic AI systems built on Large Language Models (LLMs). To enhance trust, natural language claims from diverse sources, including human-written text, web content, and model outputs, are commonly checked for factuality by retrieving external knowledge and using an LLM to verify the faithfulness of claims to the retrieved evidence. As a result, such methods are constrained by retrieval errors and external data availability, while leaving the models intrinsic fact-verification capabilities largely unused. We propose the task of fact-checking without retrieval, focusing on the verification of arbitrary natural language claims, independent of their source. To study this setting, we introduce a comprehensive evaluation framework focused on generalization, testing robustness to (i) long-tail knowledge, (ii) variation in claim sources, (iii) multilinguality, and (iv) long-form generation. Across 9 datasets, 18 methods and 3 models, our experiments indicate that logit-based approaches often underperform compared to those that leverage internal model representations. Building on this finding, we introduce INTRA, a method that exploits interactions between internal representations and achieves state-of-the-art performance with strong generalization. More broadly, our work establishes fact-checking without retrieval as a promising research direction that can complement retrieval-based frameworks, improve scalability, and enable the use of such systems as reward signals during training or as components integrated into the generation process.

### 🤖 AI 总结

**一句话总结**：提出“无检索事实核查”任务与评测框架，并给出利用LLM内部表示交互的INTRA方法，在多数据集上取得更强泛化与SOTA表现。

**研究动机**：现有事实核查多依赖外部检索与证据比对，容易受检索错误与数据可用性限制，同时未充分利用LLM自身的参数化知识与内在核查能力。

**核心方法**：构建面向泛化的评测框架，系统考察长尾知识、来源变化、多语言与长文本生成等鲁棒性；在对比18种方法后提出INTRA，通过挖掘并建模LLM内部表征之间的交互来判断断言真伪，而非依赖logit打分或外部检索。

**主要结论**：实验覆盖9个数据集、18种方法与3个模型，发现单纯logit类方法普遍不如利用内部表示的方法；INTRA达到SOTA且泛化更强，证明无检索事实核查可作为检索式框架的补充，并可用于训练时奖励信号或集成到生成过程以提升可扩展性与可靠性。

**关键词**：无检索事实核查, LLM参数知识, 内部表示交互, 表示探测, 幻觉检测, 鲁棒性评测, 长尾知识, 多语言事实核查, 长文本生成核查, 检索错误敏感性

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05471v1) | [下载PDF](https://arxiv.org/pdf/2603.05471v1.pdf)

---

## [6. NCTB-QA: A Large-Scale Bangla Educational Question Answering Dataset and Benchmarking Performance](https://arxiv.org/abs/2603.05462v1)

**作者**：Abrar Eyasir, Tahsin Ahmed, Muhammad Ibrahim  
**分类**：cs.CL  
**发布时间**：2026-03-05

### 📄 论文摘要

Reading comprehension systems for low-resource languages face significant challenges in handling unanswerable questions. These systems tend to produce unreliable responses when correct answers are absent from context. To solve this problem, we introduce NCTB-QA, a large-scale Bangla question answering dataset comprising 87,805 question-answer pairs extracted from 50 textbooks published by Bangladesh's National Curriculum and Textbook Board. Unlike existing Bangla datasets, NCTB-QA maintains a balanced distribution of answerable (57.25%) and unanswerable (42.75%) questions. NCTB-QA also includes adversarially designed instances containing plausible distractors. We benchmark three transformer-based models (BERT, RoBERTa, ELECTRA) and demonstrate substantial improvements through fine-tuning. BERT achieves 313% relative improvement in F1 score (0.150 to 0.620). Semantic answer quality measured by BERTScore also increases significantly across all models. Our results establish NCTB-QA as a challenging benchmark for Bangla educational question answering. This study demonstrates that domain-specific fine-tuning is critical for robust performance in low-resource settings.

### 🤖 AI 总结

**一句话总结**：论文提出并发布NCTB-QA，一个包含可回答与不可回答问题且带对抗干扰项的大规模孟加拉语教育阅读理解数据集，并系统评测三种Transformer模型的微调表现。

**研究动机**：低资源语言阅读理解在遇到“上下文中无答案”的问题时容易产生不可靠的编造式回答，因此需要包含大量不可回答样本的基准来训练与评估模型的鲁棒性。

**核心方法**：从孟加拉国国家课程与教材委员会的50本教材中抽取并构建87,805个问答对，保持可回答(57.25%)与不可回答(42.75%)的平衡分布，并加入带“似是而非干扰项”的对抗样例；随后对BERT、RoBERTa、ELECTRA进行基准测试与领域微调，用F1与BERTScore评估效果。

**主要结论**：在NCTB-QA上进行领域微调能显著提升模型表现（如BERT的F1从0.150提升到0.620，约313%相对提升），且语义质量指标BERTScore也全面提高，说明NCTB-QA是一个具有挑战性的孟加拉语教育QA基准并凸显领域微调对低资源场景的关键性。

**关键词**：孟加拉语问答数据集, 教育问答, 不可回答问题检测, 干扰项诱导, 低资源语言NLP, 问答基准评测, F1评测指标, NCTB-QA

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05462v1) | [下载PDF](https://arxiv.org/pdf/2603.05462v1.pdf)

---

## [7. DEBISS: a Corpus of Individual, Semi-structured and Spoken Debates](https://arxiv.org/abs/2603.05459v1)

**作者**：Klaywert Danillo Ferreira de Souza, David Eduardo Pereira, Cláudio E. C. Campelo 等 4 位作者  
**分类**：cs.CL, cs.DB  
**发布时间**：2026-03-05

### 📄 论文摘要

The process of debating is essential in our daily lives, whether in studying, work activities, simple everyday discussions, political debates on TV, or online discussions on social networks. The range of uses for debates is broad. Due to the diverse applications, structures, and formats of debates, developing corpora that account for these variations can be challenging, and the scarcity of debate corpora in the state of the art is notable. For this reason, the current research proposes the DEBISS corpus: a collection of spoken and individual debates with semi-structured features. With a broad range of NLP task annotations, such as speech-to-text, speaker diarization, argument mining, and debater quality assessment.

### 🤖 AI 总结

**一句话总结**：DEBISS提出并发布一个面向个人口语、半结构化辩论场景的多任务标注语料库，支持从语音到论证分析等多种NLP研究。

**研究动机**：现有辩论语料库稀缺且难以覆盖辩论在应用、结构与形式上的多样性，尤其缺少适配口语与半结构化辩论的数据资源。

**核心方法**：构建DEBISS语料库，收集个人口语辩论数据并设计半结构化辩论框架，同时提供多层标注以支持语音转写、说话人分离、论证挖掘与辩手质量评估等任务。

**主要结论**：DEBISS填补了口语/个人/半结构化辩论数据的空白，并通过丰富标注为多任务NLP研究与评测提供了统一的数据基础。

**关键词**：辩论语料库, 口语辩论, 半结构化语料, 个人辩论, 语音转文本, 说话人分离, 论证挖掘, 辩手质量评估, 多任务标注, 语音与文本联合标注

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05459v1) | [下载PDF](https://arxiv.org/pdf/2603.05459v1.pdf)

---

## [8. FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://arxiv.org/abs/2603.05451v1)

**作者**：Ted Zadouri, Markus Hoehnerbach, Jay Shah 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-05

### 📄 论文摘要

Attention, as a core layer of the ubiquitous Transformer architecture, is the bottleneck for large language models and long-context applications. While FlashAttention-3 optimized attention for Hopper GPUs through asynchronous execution and warp specialization, it primarily targets the H100 architecture. The AI industry has rapidly transitioned to deploying Blackwell-based systems such as the B200 and GB200, which exhibit fundamentally different performance characteristics due to asymmetric hardware scaling: tensor core throughput doubles while other functional units (shared memory bandwidth, exponential units) scale more slowly or remain unchanged. We develop several techniques to address these shifting bottlenecks on Blackwell GPUs: (1) redesigned pipelines that exploit fully asynchronous MMA operations and larger tile sizes, (2) software-emulated exponential and conditional softmax rescaling that reduces non-matmul operations, and (3) leveraging tensor memory and the 2-CTA MMA mode to reduce shared memory traffic and atomic adds in the backward pass. We demonstrate that our method, FlashAttention-4, achieves up to 1.3$\times$ speedup over cuDNN 9.13 and 2.7$\times$ over Triton on B200 GPUs with BF16, reaching up to 1613 TFLOPs/s (71% utilization). Beyond algorithmic innovations, we implement FlashAttention-4 entirely in CuTe-DSL embedded in Python, achieving 20-30$\times$ faster compile times compared to traditional C++ template-based approaches while maintaining full expressivity.

### 🤖 AI 总结

**一句话总结**：FlashAttention-4 针对 Blackwell GPU 的非对称硬件扩展重新协同设计注意力算法与kernel流水线，在 B200 上显著提升吞吐并保持高利用率。

**研究动机**：Blackwell（B200/GB200）上张量核吞吐翻倍但共享内存带宽、指数等单元增长较慢，导致 FlashAttention-3 面向 H100 的优化不再匹配新瓶颈，需要新的attention实现来充分吃满算力。

**核心方法**：提出全异步 MMA 与更大tile的重构流水线；用软件模拟 exp 与条件softmax重缩放以减少非matmul开销；并利用 tensor memory 与 2-CTA MMA 模式在反向中降低 shared memory 访问与 atomic add。

**主要结论**：在 B200 的 BF16 上相对 cuDNN 9.13 最高加速 1.3×、相对 Triton 最高 2.7×，峰值达 1613 TFLOPs/s（约71%利用率）；同时用 Python 内嵌的 CuTe-DSL 完整实现，编译时间比传统 C++ 模板快 20–30×且不牺牲表达能力。

**关键词**：注意力加速, GPU 内核流水线, 异构硬件扩展, 指数函数模拟, 共享内存优化, 反向传播优化, FlashAttention-4, Algorithm

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05451v1) | [下载PDF](https://arxiv.org/pdf/2603.05451v1.pdf)

---

## [9. An Exploration-Analysis-Disambiguation Reasoning Framework for Word Sense Disambiguation with Low-Parameter LLMs](https://arxiv.org/abs/2603.05400v1)

**作者**：Deshan Sumanathilaka, Nicholas Micallef, Julian Hough  
**分类**：cs.CL  
**发布时间**：2026-03-05

### 📄 论文摘要

Word Sense Disambiguation (WSD) remains a key challenge in Natural Language Processing (NLP), especially when dealing with rare or domain-specific senses that are often misinterpreted. While modern high-parameter Large Language Models (LLMs) such as GPT-4-Turbo have shown state-of-the-art WSD performance, their computational and energy demands limit scalability. This study investigates whether low-parameter LLMs (<4B parameters) can achieve comparable results through fine-tuning strategies that emphasize reasoning-driven sense identification. Using the FEWS dataset augmented with semi-automated, rationale-rich annotations, we fine-tune eight small-scale open-source LLMs (e.g. Gemma and Qwen). Our results reveal that Chain-of-Thought (CoT)-based reasoning combined with neighbour-word analysis achieves performance comparable to GPT-4-Turbo in zero-shot settings. Importantly, Gemma-3-4B and Qwen-3-4B models consistently outperform all medium-parameter baselines and state-of-the-art models on FEWS, with robust generalization to unseen senses. Furthermore, evaluation on the unseen "Fool Me If You Can'' dataset confirms strong cross-domain adaptability without task-specific fine-tuning. This work demonstrates that with carefully crafted reasoning-centric fine-tuning, low-parameter LLMs can deliver accurate WSD while substantially reducing computational and energy demands.

### 🤖 AI 总结

**一句话总结**：论文提出一种面向低参数LLM的“探索-分析-消歧”推理式微调框架，使<4B模型在WSD上达到接近/优于GPT-4-Turbo的效果。

**研究动机**：WSD对稀有/领域义项仍易出错，而大模型虽强但算力与能耗成本高、难以规模化；作者希望验证小模型能否通过更“会推理”的训练策略追平性能。

**核心方法**：基于FEWS数据集并补充半自动生成的含推理依据（rationale）标注，对8个小型开源LLM（如Gemma、Qwen）进行以CoT为核心、结合邻近词（neighbour-word）语境分析的推理驱动微调。

**主要结论**：CoT推理+邻词分析显著提升小模型WSD能力，Gemma-3-4B与Qwen-3-4B在FEWS上超过中等规模与SOTA基线，并在未见义项与跨域数据集（Fool Me If You Can）上无需额外微调也表现稳健，证明低参数模型可在更低成本下实现高精度WSD。

**关键词**：词义消歧, 低参数 LLM, 推理驱动微调, 链式思维（CoT）, 邻词分析, 零样本评测, 未见词义泛化, 跨域迁移, 理据标注, 半自动数据增强, 计算能耗优化

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05400v1) | [下载PDF](https://arxiv.org/pdf/2603.05400v1.pdf)

---

## cs.CV

## [10. Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups](https://arxiv.org/abs/2603.05507v1)

**作者**：Leif Van Holland, Domenic Zingsheim, Mana Takhsha 等 7 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-03-05

### 📄 论文摘要

High-quality 3D streaming from multiple cameras is crucial for immersive experiences in many AR/VR applications. The limited number of views - often due to real-time constraints - leads to missing information and incomplete surfaces in the rendered images. Existing approaches typically rely on simple heuristics for the hole filling, which can result in inconsistencies or visual artifacts. We propose to complete the missing textures using a novel, application-targeted inpainting method independent of the underlying representation as an image-based post-processing step after the novel view rendering. The method is designed as a standalone module compatible with any calibrated multi-camera system. For this we introduce a multi-view aware, transformer-based network architecture using spatio-temporal embeddings to ensure consistency across frames while preserving fine details. Additionally, our resolution-independent design allows adaptation to different camera setups, while an adaptive patch selection strategy balances inference speed and quality, allowing real-time performance. We evaluate our approach against state-of-the-art inpainting techniques under the same real-time constraints and demonstrate that our model achieves the best trade-off between quality and speed, outperforming competitors in both image and video-based metrics.

### 🤖 AI 总结

**一句话总结**：提出一种面向稀疏多摄像头实时3D串流的Transformer补全模块，在新视角渲染后对缺失纹理进行一致且高质量的修复，并兼顾实时性。

**研究动机**：实时多摄像头视角数量受限会导致渲染图像出现孔洞与不完整表面，而现有基于简单启发式的补洞方法易产生不一致和视觉伪影。

**核心方法**：设计与底层3D表示无关的图像后处理补全网络：引入多视角感知的Transformer结构，并用时空嵌入保证跨帧一致性与细节保真；同时采用分辨率无关设计与自适应patch选择策略，在不同相机配置下平衡速度与质量以实现实时推理。

**主要结论**：在相同实时约束下，相比多种SOTA补全方法，该模型在图像/视频指标上取得更优质量-速度折中，并在视觉一致性与细节保留方面表现更好。

**关键词**：三维实时流媒体, 稀疏多相机, 新视角渲染, 纹理补全, 图像修复, 多视图一致性, 时空嵌入, 分辨率无关, 自适应补丁选择, 实时推理

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05507v1) | [下载PDF](https://arxiv.org/pdf/2603.05507v1.pdf)

---

## [11. FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning](https://arxiv.org/abs/2603.05506v1)

**作者**：Weijie Lyu, Ming-Hsuan Yang, Zhixin Shu  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

We introduce FaceCam, a system that generates video under customizable camera trajectories for monocular human portrait video input. Recent camera control approaches based on large video-generation models have shown promising progress but often exhibit geometric distortions and visual artifacts on portrait videos due to scale-ambiguous camera representations or 3D reconstruction errors. To overcome these limitations, we propose a face-tailored scale-aware representation for camera transformations that provides deterministic conditioning without relying on 3D priors. We train a video generation model on both multi-view studio captures and in-the-wild monocular videos, and introduce two camera-control data generation strategies: synthetic camera motion and multi-shot stitching, to exploit stationary training cameras while generalizing to dynamic, continuous camera trajectories at inference time. Experiments on Ava-256 dataset and diverse in-the-wild videos demonstrate that FaceCam achieves superior performance in camera controllability, visual quality, identity and motion preservation.

### 🤖 AI 总结

**一句话总结**：FaceCam提出一种面向人像视频的尺度感知相机条件表示，在不依赖3D先验的情况下实现可控且高质量的相机轨迹驱动视频生成。

**研究动机**：现有基于大模型的视频相机控制在人像场景中常因相机尺度表征歧义或3D重建误差导致几何扭曲与伪影，难以同时保证可控性与身份/动作一致性。

**核心方法**：设计“人脸定制”的尺度感知相机变换表示，提供确定性的相机条件输入并避免依赖3D重建；同时结合多视角棚拍与野外单目数据训练，并用“合成相机运动”和“多镜头拼接”两种数据生成策略，让静态训练相机也能泛化到推理时连续动态轨迹控制。

**主要结论**：在Ava-256与多种野外视频上，FaceCam在相机可控性、视觉质量以及身份与运动保持方面优于现有方法，且能更稳定地生成无明显几何失真的人像相机运动效果。

**关键词**：人像视频生成, 单目人像视频, 相机轨迹控制, 相机变换表示, 尺度感知条件控制, 确定性条件注入, 免3D先验, 多视角工作室数据, 合成相机运动, 多镜头拼接, 身份一致性保持, 运动保持

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05506v1) | [下载PDF](https://arxiv.org/pdf/2603.05506v1.pdf)

---

## [12. Towards Multimodal Lifelong Understanding: A Dataset and Agentic Baseline](https://arxiv.org/abs/2603.05484v1)

**作者**：Guo Chen, Lidong Lu, Yicheng Liu 等 20 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

While datasets for video understanding have scaled to hour-long durations, they typically consist of densely concatenated clips that differ from natural, unscripted daily life. To bridge this gap, we introduce MM-Lifelong, a dataset designed for Multimodal Lifelong Understanding. Comprising 181.1 hours of footage, it is structured across Day, Week, and Month scales to capture varying temporal densities. Extensive evaluations reveal two critical failure modes in current paradigms: end-to-end MLLMs suffer from a Working Memory Bottleneck due to context saturation, while representative agentic baselines experience Global Localization Collapse when navigating sparse, month-long timelines. To address this, we propose the Recursive Multimodal Agent (ReMA), which employs dynamic memory management to iteratively update a recursive belief state, significantly outperforming existing methods. Finally, we establish dataset splits designed to isolate temporal and domain biases, providing a rigorous foundation for future research in supervised learning and out-of-distribution generalization.

### 🤖 AI 总结

**一句话总结**：提出面向“多模态终身理解”的MM-Lifelong长时序数据集与递归多模态智能体ReMA基线，以缓解长视频理解中的记忆与定位失效。

**研究动机**：现有长视频理解数据多为密集拼接片段，难以反映真实日常的稀疏、跨日/周/月的自然时间结构，导致模型在超长跨度理解上表现不可靠。作者希望系统评估并解决长时序多模态理解在现实场景中的关键瓶颈。

**核心方法**：构建181.1小时的MM-Lifelong数据集，按Day/Week/Month三种时间尺度组织，并设计切分以隔离时间与领域偏置；同时提出ReMA，通过动态记忆管理与递归信念状态迭代更新来进行长期跨片段推理与检索定位。

**主要结论**：实验揭示两类典型失败模式：端到端MLLM出现上下文饱和导致的“工作记忆瓶颈”，而代表性智能体基线在月级稀疏时间轴上出现“全局定位崩溃”；ReMA在该数据集上显著优于现有方法，并为监督学习与OOD泛化提供了更严格的评测基础。

**关键词**：自然日常视频数据集, 多尺度时间建模, 上下文饱和, 工作记忆瓶颈, 全局定位崩溃, 动态记忆管理, 递归信念状态, 监督学习评测, 分布外泛化

**评分**：47

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05484v1) | [下载PDF](https://arxiv.org/pdf/2603.05484v1.pdf)

---

## [13. Towards 3D Scene Understanding of Gas Plumes in LWIR Hyperspectral Images Using Neural Radiance Fields](https://arxiv.org/abs/2603.05473v1)

**作者**：Scout Jarman, Zigfried Hampel-Arias, Adra Carr 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

Hyperspectral images (HSI) have many applications, ranging from environmental monitoring to national security, and can be used for material detection and identification. Longwave infrared (LWIR) HSI can be used for gas plume detection and analysis. Oftentimes, only a few images of a scene of interest are available and are analyzed individually. The ability to combine information from multiple images into a single, cohesive representation could enhance analysis by providing more context on the scene's geometry and spectral properties. Neural radiance fields (NeRFs) create a latent neural representation of volumetric scene properties that enable novel-view rendering and geometry reconstruction, offering a promising avenue for hyperspectral 3D scene reconstruction. We explore the possibility of using NeRFs to create 3D scene reconstructions from LWIR HSI and demonstrate that the model can be used for the basic downstream analysis task of gas plume detection. The physics-based DIRSIG software suite was used to generate a synthetic multi-view LWIR HSI dataset of a simple facility with a strong sulfur hexafluoride gas plume. Our method, built on the standard Mip-NeRF architecture, combines state-of-the-art methods for hyperspectral NeRFs and sparse-view NeRFs, along with a novel adaptive weighted MSE loss. Our final NeRF method requires around 50% fewer training images than the standard Mip-NeRF and achieves an average PSNR of 39.8 dB with as few as 30 training images. Gas plume detection applied to NeRF-rendered test images using the adaptive coherence estimator achieves an average AUC of 0.821 when compared with detection masks generated from ground-truth test images.

### 🤖 AI 总结

**一句话总结**：论文提出一种面向LWIR高光谱图像的稀疏视角Hyperspectral NeRF方法，实现3D场景重建并支持气体羽流检测等下游分析。

**研究动机**：LWIR高光谱气体分析常只有少量多视角图像且逐帧处理，缺乏统一的三维几何与光谱表征；将多视角信息融合为可新视角渲染的3D表示有望增强对场景与羽流的理解与检测能力。

**核心方法**：基于Mip-NeRF框架，融合高光谱NeRF与稀疏视角NeRF技术，并引入自适应加权MSE损失以提升在少训练图像条件下的重建质量；使用DIRSIG生成含六氟化硫(SF6)强羽流的合成多视角LWIR HSI数据进行训练与评估，并在NeRF渲染测试图像上用ACE检测器进行羽流检测。

**主要结论**：方法在仅约30张训练图像时可达平均PSNR 39.8 dB，训练图像需求较标准Mip-NeRF减少约50%；基于NeRF渲染图像的ACE羽流检测相对真值掩码取得平均AUC 0.821，表明NeRF重建可支撑基本气体检测下游任务。

**关键词**：长波红外高光谱成像, 气体羽流检测, 三维场景重建, 神经辐射场（NeRF）, 稀疏视角重建, 新视角合成, 自适应加权 MSE 损失, 自适应相干估计（ACE）, 硫六氟化物（SF6）

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05473v1) | [下载PDF](https://arxiv.org/pdf/2603.05473v1.pdf)

---

## [14. EdgeDAM: Real-time Object Tracking for Mobile Devices](https://arxiv.org/abs/2603.05463v1)

**作者**：Syed Muhammad Raza, Syed Murtaza Hussain Abidi, Khawar Islam 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

Single-object tracking (SOT) on edge devices is a critical computer vision task, requiring accurate and continuous target localization across video frames under occlusion, distractor interference, and fast motion. However, recent state-of-the-art distractor-aware memory mechanisms are largely built on segmentation-based trackers and rely on mask prediction and attention-driven memory updates, which introduce substantial computational overhead and limit real-time deployment on resource-constrained hardware; meanwhile, lightweight trackers sustain high throughput but are prone to drift when visually similar distractors appear. To address these challenges, we propose EdgeDAM, a lightweight detection-guided tracking framework that reformulates distractor-aware memory for bounding-box tracking under strict edge constraints. EdgeDAM introduces two key strategies: (1) Dual-Buffer Distractor-Aware Memory (DAM), which integrates a Recent-Aware Memory to preserve temporally consistent target hypotheses and a Distractor-Resolving Memory to explicitly store hard negative candidates and penalize their re-selection during recovery; and (2) Confidence-Driven Switching with Held-Box Stabilization, where tracker reliability and temporal consistency criteria adaptively activate detection and memory-guided re-identification during occlusion, while a held-box mechanism temporarily freezes and expands the estimate to suppress distractor contamination. Extensive experiments on five benchmarks, including the distractor-focused DiDi dataset, demonstrate improved robustness under occlusion and fast motion while maintaining real-time performance on mobile devices, achieving 88.2% accuracy on DiDi and 25 FPS on an iPhone 15. Code will be released.

### 🤖 AI 总结

**一句话总结**：EdgeDAM 在移动端提出一种轻量级、检测引导的单目标跟踪框架，通过双缓冲“干扰物感知记忆”和置信度切换机制，在遮挡/干扰物/快速运动下实现更稳健且实时的框跟踪。

**研究动机**：现有干扰物感知记忆多依赖分割与注意力更新，计算开销大难以在边缘设备实时运行；而轻量跟踪器虽快但在相似干扰物出现时容易漂移，需要在资源受限条件下兼顾鲁棒性与速度。

**核心方法**：提出 Dual-Buffer DAM：用 Recent-Aware Memory 保留近期一致的目标假设，用 Distractor-Resolving Memory 显式存储难负样本并在恢复时惩罚其再选；再结合置信度驱动的检测/重识别切换与 held-box 稳定化（短暂冻结并扩张框）以降低遮挡期的干扰污染。

**主要结论**：在包含干扰物数据集 DiDi 等5个基准上，EdgeDAM 在遮挡与快速运动场景下显著提升鲁棒性，同时保持移动端实时性，报告在 iPhone 15 上达 25 FPS 且 DiDi 准确率 88.2%。

**关键词**：边缘设备视觉, 移动端实时, 单目标跟踪（SOT）, 检测引导跟踪, 边界框跟踪, 遮挡鲁棒性, 干扰物抑制, 干扰感知记忆, 双缓冲记忆, 硬负样本记忆, 置信度驱动切换, 重识别（ReID）

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05463v1) | [下载PDF](https://arxiv.org/pdf/2603.05463v1.pdf)

---

## [15. RealWonder: Real-Time Physical Action-Conditioned Video Generation](https://arxiv.org/abs/2603.05449v1)

**作者**：Wei Liu, Ziyu Chen, Zizhang Li 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-03-05

### 📄 论文摘要

Current video generation models cannot simulate physical consequences of 3D actions like forces and robotic manipulations, as they lack structural understanding of how actions affect 3D scenes. We present RealWonder, the first real-time system for action-conditioned video generation from a single image. Our key insight is using physics simulation as an intermediate bridge: instead of directly encoding continuous actions, we translate them through physics simulation into visual representations (optical flow and RGB) that video models can process. RealWonder integrates three components: 3D reconstruction from single images, physics simulation, and a distilled video generator requiring only 4 diffusion steps. Our system achieves 13.2 FPS at 480x832 resolution, enabling interactive exploration of forces, robot actions, and camera controls on rigid objects, deformable bodies, fluids, and granular materials. We envision RealWonder opens new opportunities to apply video models in immersive experiences, AR/VR, and robot learning. Our code and model weights are publicly available in our project website: https://liuwei283.github.io/RealWonder/

### 🤖 AI 总结

**一句话总结**：RealWonder通过“单图3D重建+物理仿真中间表示+少步扩散视频生成”实现实时的物理动作条件视频生成，可交互模拟力/机器人操作等对场景的物理影响。

**研究动机**：现有视频生成模型缺乏对3D结构与物理因果的理解，难以从连续动作（力、操控、相机控制）推演出可信的物理后果。需要一种既物理一致又能实时交互的动作条件视频生成方案。

**核心方法**：先从单张输入图像进行3D重建，再在重建场景中进行物理仿真，将动作转译为视频模型易消费的视觉中间表示（如光流与RGB）。最后用蒸馏后的扩散式视频生成器在仅4步扩散下生成视频，从而达到实时速度。

**主要结论**：系统在480×832分辨率下可达13.2 FPS，实现对刚体、可变形物体、流体与颗粒等多类物理现象的交互式动作驱动视频生成。该框架表明“物理仿真桥接”能显著提升动作到视觉结果的可控性与物理一致性，并适用于AR/VR与机器人学习等应用。

**关键词**：动作条件视频生成, 单图像视频生成, 物理仿真中间表示, 3D场景重建, 光流条件输入, 扩散模型加速, 蒸馏扩散生成, 实时视频生成, 机器人操作建模, 多物理体模拟, 交互式相机控制

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05449v1) | [下载PDF](https://arxiv.org/pdf/2603.05449v1.pdf)

---

## [16. NaiLIA: Multimodal Nail Design Retrieval Based on Dense Intent Descriptions and Palette Queries](https://arxiv.org/abs/2603.05446v1)

**作者**：Kanon Amemiya, Daichi Yashima, Kei Katsumata 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

We focus on the task of retrieving nail design images based on dense intent descriptions, which represent multi-layered user intent for nail designs. This is challenging because such descriptions specify unconstrained painted elements and pre-manufactured embellishments as well as visual characteristics, themes, and overall impressions. In addition to these descriptions, we assume that users provide palette queries by specifying zero or more colors via a color picker, enabling the expression of subtle and continuous color nuances. Existing vision-language foundation models often struggle to incorporate such descriptions and palettes. To address this, we propose NaiLIA, a multimodal retrieval method for nail design images, which comprehensively aligns with dense intent descriptions and palette queries during retrieval. Our approach introduces a relaxed loss based on confidence scores for unlabeled images that can align with the descriptions. To evaluate NaiLIA, we constructed a benchmark consisting of 10,625 images collected from people with diverse cultural backgrounds. The images were annotated with long and dense intent descriptions given by over 200 annotators. Experimental results demonstrate that NaiLIA outperforms standard methods.

### 🤖 AI 总结

**一句话总结**：NaiLIA提出一种同时利用长篇细粒度意图描述与可选调色板颜色查询的多模态检索方法，用于更准确地检索美甲设计图片。

**研究动机**：用户对美甲的需求往往是多层次、细节密集的自然语言描述，并伴随连续细腻的颜色偏好，但现有视觉-语言基础模型难以有效融合这类“密集意图+调色板”信号进行检索。

**核心方法**：方法在检索时联合对齐密集意图文本与调色板颜色信息，并引入基于置信度分数的“放松损失”（relaxed loss），利用未标注但与描述可能匹配的图像来提升对齐与鲁棒性；同时构建包含10,625张图像与长描述标注的基准数据集用于评测。

**主要结论**：在新建基准上，NaiLIA相较标准检索方法取得更优结果，表明其能更好地理解复杂意图并利用调色板表达的细微色彩偏好来提升美甲图像检索性能。

**关键词**：多模态图像检索, 美甲设计检索, 密集意图描述, 调色板查询, 颜色条件检索, 视觉-语言对齐, 置信度加权损失, 弱监督学习, 长文本图文检索, 美甲设计数据集, 跨文化标注数据

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05446v1) | [下载PDF](https://arxiv.org/pdf/2603.05446v1.pdf)

---

## [17. SAIL: Similarity-Aware Guidance and Inter-Caption Augmentation-based Learning for Weakly-Supervised Dense Video Captioning](https://arxiv.org/abs/2603.05437v1)

**作者**：Ye-Chan Kim, SeungJu Cha, Si-Woo Kim 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-05

### 📄 论文摘要

Weakly-Supervised Dense Video Captioning aims to localize and describe events in videos trained only on caption annotations, without temporal boundaries. Prior work introduced an implicit supervision paradigm based on Gaussian masking and complementary captioning. However, existing method focuses merely on generating non-overlapping masks without considering their semantic relationship to corresponding events, resulting in simplistic, uniformly distributed masks that fail to capture semantically meaningful regions. Moreover, relying solely on ground-truth captions leads to sub-optimal performance due to the inherent sparsity of existing datasets. In this work, we propose SAIL, which constructs semantically-aware masks through cross-modal alignment. Our similarity aware training objective guides masks to emphasize video regions with high similarity to their corresponding event captions. Furthermore, to guide more accurate mask generation under sparse annotation settings, we introduce an LLM-based augmentation strategy that generates synthetic captions to provide additional alignment signals. These synthetic captions are incorporated through an inter-mask mechanism, providing auxiliary guidance for precise temporal localization without degrading the main objective. Experiments on ActivityNet Captions and YouCook2 demonstrate state-of-the-art performance on both captioning and localization metrics.

### 🤖 AI 总结

**一句话总结**：SAIL通过跨模态相似度引导生成语义相关的时间掩码，并结合LLM生成的合成字幕增强对齐信号，从而提升弱监督密集视频字幕的事件定位与描述能力。

**研究动机**：现有弱监督方法主要生成不重叠但语义“无感”的均匀掩码，难以覆盖与字幕真正相关的事件片段；同时仅依赖稀疏的真实字幕监督，导致训练信号不足、性能受限。

**核心方法**：提出Similarity-Aware目标：用视频-字幕相似度约束掩码，使其更强调与对应事件字幕语义匹配的时间区域；再用LLM生成合成字幕，通过inter-mask机制把合成字幕作为辅助对齐信号注入，以在不干扰主目标的前提下改进掩码与定位。

**主要结论**：在ActivityNet Captions与YouCook2上，SAIL在字幕生成与事件定位指标上均达到SOTA，验证了语义相似度引导的掩码学习与合成字幕增强能有效缓解弱监督与标注稀疏带来的问题。

**关键词**：弱监督密集视频字幕, 事件时间定位, 语义感知掩码, 相似度引导训练, 跨模态对齐, 掩码生成, 隐式监督, 高斯掩码, 字幕数据增强, LLM合成字幕, 稀疏标注学习

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05437v1) | [下载PDF](https://arxiv.org/pdf/2603.05437v1.pdf)

---

## [18. RelaxFlow: Text-Driven Amodal 3D Generation](https://arxiv.org/abs/2603.05425v1)

**作者**：Jiayin Zhu, Guoji Fu, Xiaolu Liu 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-05

### 📄 论文摘要

Image-to-3D generation faces inherent semantic ambiguity under occlusion, where partial observation alone is often insufficient to determine object category. In this work, we formalize text-driven amodal 3D generation, where text prompts steer the completion of unseen regions while strictly preserving input observation. Crucially, we identify that these objectives demand distinct control granularities: rigid control for the observation versus relaxed structural control for the prompt. To this end, we propose RelaxFlow, a training-free dual-branch framework that decouples control granularity via a Multi-Prior Consensus Module and a Relaxation Mechanism. Theoretically, we prove that our relaxation is equivalent to applying a low-pass filter on the generative vector field, which suppresses high-frequency instance details to isolate geometric structure that accommodates the observation. To facilitate evaluation, we introduce two diagnostic benchmarks, ExtremeOcc-3D and AmbiSem-3D. Extensive experiments demonstrate that RelaxFlow successfully steers the generation of unseen regions to match the prompt intent without compromising visual fidelity.

### 🤖 AI 总结

**一句话总结**：RelaxFlow提出一种无需训练的双分支框架，在严格保留输入可见区域的同时，用文本提示引导遮挡区域的“可解释补全”式3D生成。

**研究动机**：单张图像在遮挡下存在语义不确定性，仅靠可见部分难以确定类别与形状；同时需要对“已观测区域”强约束、对“文本意图”更松弛的结构级控制，两者粒度冲突。

**核心方法**：采用双分支解耦控制粒度：通过Multi-Prior Consensus Module融合多先验形成一致约束以锁定观测区域；再用Relaxation Mechanism对生成向量场做等价低通滤波，抑制高频实例细节、保留可与观测兼容的几何结构以对齐文本。

**主要结论**：在ExtremeOcc-3D与AmbiSem-3D两套诊断基准及实验中，RelaxFlow能在不牺牲可见区域保真度的前提下，让不可见部分更符合文本语义并提升整体视觉质量与可控性。

**关键词**：文本驱动三维生成, 遮挡补全（Amodal）, 图像到三维生成, 语义歧义消解, 控制粒度解耦, 双分支框架, 免训练推理, 多先验一致性, 生成向量场低通滤波, 结构松弛机制

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05425v1) | [下载PDF](https://arxiv.org/pdf/2603.05425v1.pdf)

---

## [19. MobileFetalCLIP: Selective Repulsive Knowledge Distillation for Mobile Fetal Ultrasound Analysis](https://arxiv.org/abs/2603.05421v1)

**作者**：Numan Saeed, Fadillah Adamsyah Maani, Mohammad Yaqub  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-03-05

### 📄 论文摘要

Fetal ultrasound AI could transform prenatal care in low-resource settings, yet current foundation models exceed 300M visual parameters, precluding deployment on point-of-care devices. Standard knowledge distillation fails under such extreme capacity gaps (~26x), as compact students waste capacity mimicking architectural artifacts of oversized teachers. We introduce Selective Repulsive Knowledge Distillation, which decomposes contrastive KD into diagonal and off-diagonal components: matched pair alignment is preserved while the off-diagonal weight decays into negative values, repelling the student from the teacher's inter-class confusions and forcing discovery of architecturally native features. Our 11.4M parameter student surpasses the 304M-parameter FetalCLIP teacher on zero-shot HC18 biometry validity (88.6% vs. 83.5%) and brain sub-plane F1 (0.784 vs. 0.702), while running at 1.6 ms on iPhone 16 Pro, enabling real-time assistive AI on handheld ultrasound devices. Our code, models, and app are publicly available at https://github.com/numanai/MobileFetalCLIP.

### 🤖 AI 总结

**一句话总结**：提出“选择性排斥式知识蒸馏”（Selective Repulsive KD），让仅11.4M参数的移动端学生模型在胎儿超声零样本与子平面识别上超越304M教师模型并实现手机端实时推理。

**研究动机**：胎儿超声在低资源地区有重要临床价值，但现有超大基础模型（>300M视觉参数）难以部署到手持/床旁设备；在约26倍容量差下，传统蒸馏会让小模型浪费容量去模仿大模型的架构“伪特征/混淆”。

**核心方法**：将对比式蒸馏的相似度矩阵分解为对角（正样本配对对齐）与非对角（类间关系）两部分：保留对角对齐，同时让非对角权重衰减为负值以“排斥”教师的类间混淆，促使学生学习更适配自身架构的表征。

**主要结论**：11.4M的MobileFetalCLIP在零样本HC18生物测量有效性（88.6% vs 83.5%）和脑部子平面F1（0.784 vs 0.702）上超过304M的FetalCLIP教师，并可在iPhone 16 Pro上1.6ms运行，支持移动端实时超声辅助。

**关键词**：胎儿超声分析, 移动端推理, 床旁设备部署, 模型压缩, 知识蒸馏, 选择性排斥蒸馏, 负权重去混淆, 大容量差距蒸馏, 零样本评估, 低资源医疗场景, 手持超声辅助诊断

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05421v1) | [下载PDF](https://arxiv.org/pdf/2603.05421v1.pdf)

---

## [20. Video-based Locomotion Analysis for Fish Health Monitoring](https://arxiv.org/abs/2603.05407v1)

**作者**：Timon Palm, Clemens Seibold, Anna Hilsmann 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

Monitoring the health conditions of fish is essential, as it enables the early detection of disease, safeguards animal welfare, and contributes to sustainable aquaculture practices. Physiological and pathological conditions of cultivated fish can be inferred by analyzing locomotion activities. In this paper, we present a system that estimates the locomotion activities from videos using multi object tracking. The core of our approach is a YOLOv11 detector embedded in a tracking-by-detection framework. We investigate various configurations of the YOLOv11-architecture as well as extensions that incorporate multiple frames to improve detection accuracy. Our system is evaluated on a manually annotated dataset of Sulawesi ricefish recorded in a home-aquarium-like setup, demonstrating its ability to reliably measure swimming direction and speed for fish health monitoring. The dataset will be made publicly available upon publication.

### 🤖 AI 总结

**一句话总结**：提出一个基于YOLOv11的多目标跟踪视频分析系统，从鱼类视频中可靠估计游动方向与速度，用于健康监测。

**研究动机**：鱼类健康状况可通过运动行为变化早期反映，自动化、非侵入式的运动监测有助于疾病预警与可持续养殖管理。

**核心方法**：采用tracking-by-detection框架，将YOLOv11作为核心检测器嵌入多目标跟踪流程，并比较不同YOLOv11结构配置及引入多帧信息的扩展以提升检测精度；在人工标注的苏拉威西米鱼水族箱场景数据集上评估运动指标估计效果。

**主要结论**：系统在真实家庭水族箱式录制条件下能稳定测量鱼的游动方向和速度，验证了用于健康监测的可行性；数据集将随论文发表公开。

**关键词**：鱼类健康监测, 水产养殖, 视频行为分析, 鱼类运动分析, 多目标跟踪, 目标检测, 多帧融合, 游动速度估计, 游动方向估计, 人工标注数据集

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05407v1) | [下载PDF](https://arxiv.org/pdf/2603.05407v1.pdf)

---

## [21. Fusion-CAM: Integrating Gradient and Region-Based Class Activation Maps for Robust Visual Explanations](https://arxiv.org/abs/2603.05386v1)

**作者**：Hajar Dekdegue, Moncef Garouani, Josiane Mothe 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

Interpreting the decision-making process of deep convolutional neural networks remains a central challenge in achieving trustworthy and transparent artificial intelligence. Explainable AI (XAI) techniques, particularly Class Activation Map (CAM) methods, are widely adopted to visualize the input regions influencing model predictions. Gradient-based approaches (e.g. Grad-CAM) provide highly discriminative, fine-grained details by computing gradients of class activations but often yield noisy and incomplete maps that emphasize only the most salient regions rather than the complete objects. Region-based approaches (e.g. Score-CAM) aggregate information over larger areas, capturing broader object coverage at the cost of over-smoothing and reduced sensitivity to subtle features. We introduce Fusion-CAM, a novel framework that bridges this explanatory gap by unifying both paradigms through a dedicated fusion mechanism to produce robust and highly discriminative visual explanations. Our method first denoises gradient-based maps, yielding cleaner and more focused activations. It then combines the refined gradient map with region-based maps using contribution weights to enhance class coverage. Finally, we propose an adaptive similarity-based pixel-level fusion that evaluates the agreement between both paradigms and dynamically adjusts the fusion strength. This adaptive mechanism reinforces consistent activations while softly blending conflicting regions, resulting in richer, context-aware, and input-adaptive visual explanations. Extensive experiments on standard benchmarks show that Fusion-CAM consistently outperforms existing CAM variants in both qualitative visualization and quantitative evaluation, providing a robust and flexible tool for interpreting deep neural networks.

### 🤖 AI 总结

**一句话总结**：Fusion-CAM 通过融合梯度型与区域型CAM并引入自适应像素级融合机制，生成更鲁棒且覆盖更完整的视觉解释热图。

**研究动机**：梯度CAM细粒度但易噪声且常只突出最显著局部，区域CAM覆盖更全但易过度平滑、对细微特征不敏感，需要兼顾两者优点的统一解释框架。

**核心方法**：先对梯度型热图进行去噪得到更干净的激活，再用贡献权重将其与区域型热图融合以增强目标覆盖；最后基于两类热图的一致性做自适应相似度驱动的像素级融合，强化一致区域并柔和处理冲突区域。

**主要结论**：在标准基准上，Fusion-CAM 在可视化质量与定量指标上均优于现有CAM变体，能提供更丰富、上下文感知且对输入自适应的可靠解释。

**关键词**：可解释人工智能, 视觉解释, 类激活图（CAM）, 梯度-区域融合, 自适应融合机制, 相似度引导融合, 像素级融合, 激活图去噪, 鲁棒性评估

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05386v1) | [下载PDF](https://arxiv.org/pdf/2603.05386v1.pdf)

---

## [22. ORMOT: A Dataset and Framework for Omnidirectional Referring Multi-Object Tracking](https://arxiv.org/abs/2603.05384v1)

**作者**：Sijia Chen, Zihan Zhou, Yanqiu Yu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

Multi-Object Tracking (MOT) is a fundamental task in computer vision, aiming to track targets across video frames. Existing MOT methods perform well in general visual scenes, but face significant challenges and limitations when extended to visual-language settings. To bridge this gap, the task of Referring Multi-Object Tracking (RMOT) has recently been proposed, which aims to track objects that correspond to language descriptions. However, current RMOT methods are primarily developed on datasets captured by conventional cameras, which suffer from limited field of view. This constraint often causes targets to move out of the frame, leading to fragmented tracking and loss of contextual information. In this work, we propose a novel task, called Omnidirectional Referring Multi-Object Tracking (ORMOT), which extends RMOT to omnidirectional imagery, aiming to overcome the field-of-view (FoV) limitation of conventional datasets and improve the model's ability to understand long-horizon language descriptions. To advance the ORMOT task, we construct ORSet, an Omnidirectional Referring Multi-Object Tracking dataset, which contains 27 diverse omnidirectional scenes, 848 language descriptions, and 3,401 annotated objects, providing rich visual, temporal, and language information. Furthermore, we propose ORTrack, a Large Vision-Language Model (LVLM)-driven framework tailored for Omnidirectional Referring Multi-Object Tracking. Extensive experiments on the ORSet dataset demonstrate the effectiveness of our ORTrack framework. The dataset and code will be open-sourced at https://github.com/chen-si-jia/ORMOT.

### 🤖 AI 总结

**一句话总结**：提出全向视觉-语言指代多目标跟踪（ORMOT）任务，并发布ORSet数据集与LVLM驱动的ORTrack框架以提升长时序、跨视野的指代跟踪能力。

**研究动机**：现有RMOT多基于常规相机数据，视场受限导致目标易出画、轨迹断裂且上下文丢失，难以处理长跨度语言描述。全向成像可缓解FoV限制，但缺少对应任务定义与数据/方法支撑。

**核心方法**：构建ORSet全向RMOT数据集（27个场景、848条描述、3401个标注对象），提供丰富的视觉-时间-语言监督。提出ORTrack：以大型视觉语言模型为核心，面向全向图像进行语言指代的多目标关联与跟踪。

**主要结论**：在ORSet上的大量实验表明ORTrack在全向指代多目标跟踪上有效，验证了ORMOT任务与数据集对解决FoV限制、提升长时序语言理解与跟踪的价值。

**关键词**：全向指代多目标跟踪, 指代多目标跟踪, 多目标跟踪, 视觉语言跟踪, 全景图像, 360度相机, 视场角限制, 视觉语言模型, 跟踪数据集

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05384v1) | [下载PDF](https://arxiv.org/pdf/2603.05384v1.pdf)

---

## cs.LG

## [23. POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation](https://arxiv.org/abs/2603.05500v1)

**作者**：Zeju Qiu, Lixin Liu, Adrian Weller 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-03-05

### 📄 论文摘要

Efficient and stable training of large language models (LLMs) remains a core challenge in modern machine learning systems. To address this challenge, Reparameterized Orthogonal Equivalence Training (POET), a spectrum-preserving framework that optimizes each weight matrix through orthogonal equivalence transformation, has been proposed. Although POET provides strong training stability, its original implementation incurs high memory consumption and computational overhead due to intensive matrix multiplications. To overcome these limitations, we introduce POET-X, a scalable and memory-efficient variant that performs orthogonal equivalence transformations with significantly reduced computational cost. POET-X maintains the generalization and stability benefits of POET while achieving substantial improvements in throughput and memory efficiency. In our experiments, POET-X enables the pretraining of billion-parameter LLMs on a single Nvidia H100 GPU, and in contrast, standard optimizers such as AdamW run out of memory under the same settings.

### 🤖 AI 总结

**一句话总结**：POET-X 通过更高效的正交等价变换实现更省显存、更高吞吐的 LLM 训练，同时保持 POET 的稳定性与泛化优势。

**研究动机**：原始 POET 虽能提升训练稳定性，但因大量矩阵乘法带来显著的显存占用与计算开销，限制了大模型训练的可扩展性。

**核心方法**：提出 POET-X，将权重优化重参数化为正交等价变换的可扩展实现，在保持谱性质（spectrum-preserving）的同时显著降低变换的计算与内存成本。

**主要结论**：实验表明 POET-X 在不牺牲稳定性与泛化的前提下提升吞吐并降低显存需求，甚至可在单张 Nvidia H100 上预训练十亿参数级 LLM，而 AdamW 等标准优化器在相同设置下会 OOM。

**关键词**：LLM 预训练, 内存高效训练, 正交等价变换, 正交重参数化, 谱保持优化, 矩阵乘法开销降低, 训练稳定性, 吞吐量提升, 单卡训练（H100）, 十亿参数模型, AdamW 对比基线

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05500v1) | [下载PDF](https://arxiv.org/pdf/2603.05500v1.pdf)

---

## [24. Cheap Thrills: Effective Amortized Optimization Using Inexpensive Labels](https://arxiv.org/abs/2603.05495v1)

**作者**：Khai Nguyen, Petros Ellinas, Anvita Bhagavathula 等 4 位作者  
**分类**：cs.LG, math.OC  
**发布时间**：2026-03-05

### 📄 论文摘要

To scale the solution of optimization and simulation problems, prior work has explored machine-learning surrogates that inexpensively map problem parameters to corresponding solutions. Commonly used approaches, including supervised and self-supervised learning with either soft or hard feasibility enforcement, face inherent challenges such as reliance on expensive, high-quality labels or difficult optimization landscapes. To address their trade-offs, we propose a novel framework that first collects "cheap" imperfect labels, then performs supervised pretraining, and finally refines the model through self-supervised learning to improve overall performance. Our theoretical analysis and merit-based criterion show that labeled data need only place the model within a basin of attraction, confirming that only modest numbers of inexact labels and training epochs are required. We empirically validate our simple three-stage strategy across challenging domains, including nonconvex constrained optimization, power-grid operation, and stiff dynamical systems, and show that it yields faster convergence; improved accuracy, feasibility, and optimality; and up to 59x reductions in total offline cost.

### 🤖 AI 总结

**一句话总结**：提出“廉价不完美标签+监督预训练+自监督精炼”的三阶段框架，用少量低成本标签将模型引入可优化的吸引域，从而以更低离线成本实现更快收敛与更高可行性/最优性。

**研究动机**：现有摊销优化/仿真替代模型要么依赖昂贵高质量标签，要么在自监督或约束强化下训练困难、优化景观复杂，导致成本高或效果不稳。作者希望用更便宜的标注启动训练，同时保留自监督精炼带来的高精度与可行性。

**核心方法**：先收集“便宜但有误差”的标签进行监督预训练，把模型参数推入目标解的“吸引域”，再用自监督目标（结合可行性/最优性信号）进行后续精炼以提升解质量；并给出理论分析与基于merit的判据说明只需少量不精确标签和少量训练轮次即可奏效。

**主要结论**：在非凸约束优化、电网运行与刚性动力系统等任务上，三阶段策略带来更快的训练收敛、更好的准确性/可行性/最优性，并将总离线成本最高降低约59倍，验证了“不完美低成本标签足以启动、后续自监督补齐性能”的主张。

**关键词**：摊还优化, 廉价标签, 不完美标签, 监督预训练, 自监督微调, 代理模型, 可行性约束, 非凸约束优化, 最优潮流, 刚性动力系统, 吸引域

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05495v1) | [下载PDF](https://arxiv.org/pdf/2603.05495v1.pdf)

---

## [25. Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation](https://arxiv.org/abs/2603.05494v1)

**作者**：Helena Casademunt, Bartosz Cywiński, Khoi Tran 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-03-05

### 📄 论文摘要

Large language models sometimes produce false or misleading responses. Two approaches to this problem are honesty elicitation -- modifying prompts or weights so that the model answers truthfully -- and lie detection -- classifying whether a given response is false. Prior work evaluates such methods on models specifically trained to lie or conceal information, but these artificial constructions may not resemble naturally-occurring dishonesty. We instead study open-weights LLMs from Chinese developers, which are trained to censor politically sensitive topics: Qwen3 models frequently produce falsehoods about subjects like Falun Gong or the Tiananmen protests while occasionally answering correctly, indicating they possess knowledge they are trained to suppress. Using this as a testbed, we evaluate a suite of elicitation and lie detection techniques. For honesty elicitation, sampling without a chat template, few-shot prompting, and fine-tuning on generic honesty data most reliably increase truthful responses. For lie detection, prompting the censored model to classify its own responses performs near an uncensored-model upper bound, and linear probes trained on unrelated data offer a cheaper alternative. The strongest honesty elicitation techniques also transfer to frontier open-weights models including DeepSeek R1. Notably, no technique fully eliminates false responses. We release all prompts, code, and transcripts.

### 🤖 AI 总结

**一句话总结**：将中文开源“审查型”LLM作为自然的“隐秘知识压制/谎言”测试床，系统评估诚实诱导与谎言检测方法，发现多种技巧能提升真实回答但无法彻底消除虚假输出。

**研究动机**：以往诚实诱导/谎言检测多在“被专门训练去撒谎”的人工设定上评测，可能不贴近真实世界的不诚实行为。作者观察到部分中文开源模型对政治敏感话题会“偶尔说真、经常说假”，因此可用来研究模型在“已知但被压制”的场景下如何被提取真相及如何检测谎言。

**核心方法**：选取会对敏感政治议题进行审查的开源模型（如 Qwen3）构建评测集，分别测试诚实诱导（如不使用聊天模板采样、few-shot 提示、用通用诚实数据微调）与谎言检测（让模型自评其回答真伪、以及用无关数据训练线性探针）等方法，并检验对其他前沿开源模型（如 DeepSeek R1）的迁移性。

**主要结论**：在诚实诱导方面，不用 chat template 的采样、few-shot 与通用诚实微调最稳定地提升真实回答比例且具一定迁移性；在谎言检测方面，模型自我分类接近“未审查模型”上限，线性探针提供更低成本替代。但所有方法都无法完全杜绝虚假或误导性回答。

**关键词**：秘密知识诱导, 诚实性诱导, 谎言检测, 政治敏感内容审查, 提示工程, 少样本提示, 无聊天模板采样, 诚实数据微调, 线性探针

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05494v1) | [下载PDF](https://arxiv.org/pdf/2603.05494v1.pdf)

---

## [26. SurvHTE-Bench: A Benchmark for Heterogeneous Treatment Effect Estimation in Survival Analysis](https://arxiv.org/abs/2603.05483v1)

**作者**：Shahriar Noroozizadeh, Xiaobin Shen, Jeremy C. Weiss 等 4 位作者  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-03-05

### 📄 论文摘要

Estimating heterogeneous treatment effects (HTEs) from right-censored survival data is critical in high-stakes applications such as precision medicine and individualized policy-making. Yet, the survival analysis setting poses unique challenges for HTE estimation due to censoring, unobserved counterfactuals, and complex identification assumptions. Despite recent advances, from Causal Survival Forests to survival meta-learners and outcome imputation approaches, evaluation practices remain fragmented and inconsistent. We introduce SurvHTE-Bench, the first comprehensive benchmark for HTE estimation with censored outcomes. The benchmark spans (i) a modular suite of synthetic datasets with known ground truth, systematically varying causal assumptions and survival dynamics, (ii) semi-synthetic datasets that pair real-world covariates with simulated treatments and outcomes, and (iii) real-world datasets from a twin study (with known ground truth) and from an HIV clinical trial. Across synthetic, semi-synthetic, and real-world settings, we provide the first rigorous comparison of survival HTE methods under diverse conditions and realistic assumption violations. SurvHTE-Bench establishes a foundation for fair, reproducible, and extensible evaluation of causal survival methods. The data and code of our benchmark are available at: https://github.com/Shahriarnz14/SurvHTE-Bench .

### 🤖 AI 总结

**一句话总结**：提出 SurvHTE-Bench：首个面向右删失生存数据的异质性处理效应（HTE）估计综合基准，用于在多种设定下公平对比生存因果方法。

**研究动机**：生存分析中的HTE估计因删失、反事实不可观测及识别假设复杂而评估困难，现有方法虽多但缺乏统一、可复现且一致的评测体系。

**核心方法**：构建覆盖三类数据的基准：带真值的模块化合成数据（系统改变因果假设与生存动力学）、用真实协变量+模拟处理/结局的半合成数据、以及来自双胞胎研究（有真值）和HIV临床试验的真实数据，并在多种假设违背情形下统一比较多类生存HTE方法。

**主要结论**：基准首次在合成/半合成/真实场景中对生存HTE方法进行系统且严格的横向评估，揭示不同条件与假设违背下方法表现差异，并为公平、可复现、可扩展的生存因果评测提供基础设施（代码与数据已开源）。

**关键词**：异质性治疗效应估计, 生存分析, 右删失数据, 因果推断, 因果生存森林, 生存元学习器, 结局插补, HTE评测基准, 合成数据集, 半合成数据集, 反事实推断, 因果识别假设违背

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05483v1) | [下载PDF](https://arxiv.org/pdf/2603.05483v1.pdf)

---

## [27. Kraus Constrained Sequence Learning For Quantum Trajectories from Continuous Measurement](https://arxiv.org/abs/2603.05468v1)

**作者**：Priyanshi Singh, Krishna Bhatia  
**分类**：cs.LG  
**发布时间**：2026-03-05

### 📄 论文摘要

Real-time reconstruction of conditional quantum states from continuous measurement records is a fundamental requirement for quantum feedback control, yet standard stochastic master equation (SME) solvers require exact model specification, known system parameters, and are sensitive to parameter mismatch. While neural sequence models can fit these stochastic dynamics, the unconstrained predictors can violate physicality such as positivity or trace constraints, leading to unstable rollouts and unphysical estimates. We propose a Kraus-structured output layer that converts the hidden representation of a generic sequence backbone into a completely positive trace preserving (CPTP) quantum operation, yielding physically valid state updates by construction. We instantiate this layer across diverse backbones, RNN, GRU, LSTM, TCN, ESN and Mamba; including Neural ODE as a comparative baseline, on stochastic trajectories characterized by parameter drift. Our evaluation reveals distinct trade-offs between gating mechanisms, linear recurrence, and global attention. Across all models, Kraus-LSTM achieves the strongest results, improving state estimation quality by 7% over its unconstrained counterpart while guaranteeing physically valid predictions in non-stationary regimes.

### 🤖 AI 总结

**一句话总结**：提出Kraus结构化输出层，将任意序列模型的输出转为CPTP量子操作，从而在连续测量量子轨迹预测中保证物理可行性并提升估计精度。

**研究动机**：传统SME求解器依赖精确模型与参数且对失配/漂移敏感；而普通神经序列模型虽能拟合随机动力学，但预测可能破坏正定性/迹保持等物理约束，导致滚动预测不稳定与不物理。

**核心方法**：在RNN/GRU/LSTM/TCN/ESN/Mamba等序列骨干网络后接入Kraus-structured输出层，把隐藏表示参数化为完全正且迹保持（CPTP）的量子通道，用其对密度矩阵做状态更新；并在存在参数漂移的随机量子轨迹上与未约束版本及Neural ODE基线进行对比评测。

**主要结论**：Kraus约束使所有模型在非平稳场景下都能输出物理有效的量子态更新并提升稳定性；其中Kraus-LSTM表现最佳，相比无约束LSTM将状态估计质量提升约7%，并揭示门控、线性递推与全局注意力机制在该任务上的性能权衡。

**关键词**：连续测量, 量子轨迹, 条件量子态重建, 量子反馈控制, 随机主方程（SME）, 参数漂移, 物理约束序列模型, 非平稳状态估计

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05468v1) | [下载PDF](https://arxiv.org/pdf/2603.05468v1.pdf)

---

## [28. Latent Wasserstein Adversarial Imitation Learning](https://arxiv.org/abs/2603.05440v1)

**作者**：Siqi Yang, Kai Yan, Alexander G. Schwing 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-05

### 📄 论文摘要

Imitation Learning (IL) enables agents to mimic expert behavior by learning from demonstrations. However, traditional IL methods require large amounts of medium-to-high-quality demonstrations as well as actions of expert demonstrations, both of which are often unavailable. To reduce this need, we propose Latent Wasserstein Adversarial Imitation Learning (LWAIL), a novel adversarial imitation learning framework that focuses on state-only distribution matching. It benefits from the Wasserstein distance computed in a dynamics-aware latent space. This dynamics-aware latent space differs from prior work and is obtained via a pre-training stage, where we train the Intention Conditioned Value Function (ICVF) to capture a dynamics-aware structure of the state space using a small set of randomly generated state-only data. We show that this enhances the policy's understanding of state transitions, enabling the learning process to use only one or a few state-only expert episodes to achieve expert-level performance. Through experiments on multiple MuJoCo environments, we demonstrate that our method outperforms prior Wasserstein-based IL methods and prior adversarial IL methods, achieving better results across various tasks.

### 🤖 AI 总结

**一句话总结**：LWAIL 通过在“动力学感知”的潜在空间中进行 Wasserstein 状态分布对齐，使得仅用极少量（甚至单条）专家状态轨迹也能学到接近专家的策略。

**研究动机**：传统模仿学习通常依赖大量中高质量示范且需要专家动作，但现实中动作与高质量示范常不可得，因此需要一种更省示范、只用状态也能有效学习的方法。

**核心方法**：先用少量随机生成的纯状态数据预训练意图条件值函数（ICVF），构建能反映环境动力学结构的潜在表示；再在该潜在空间内用 Wasserstein 距离进行对抗式的状态分布匹配，从而训练策略在无动作示范下模仿专家。

**主要结论**：在多个 MuJoCo 任务上，LWAIL 相比以往 Wasserstein 型与对抗式模仿学习方法表现更好，并能在仅一到少量专家状态轨迹的条件下达到专家级性能。

**关键词**：模仿学习, 仅状态模仿学习, 状态分布匹配, 潜在空间表征, 动力学感知表征, 自监督预训练, 少样本专家演示, Latent

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05440v1) | [下载PDF](https://arxiv.org/pdf/2603.05440v1.pdf)

---

## [29. An interpretable prototype parts-based neural network for medical tabular data](https://arxiv.org/abs/2603.05423v1)

**作者**：Jacek Karolczak, Jerzy Stefanowski  
**分类**：cs.LG  
**发布时间**：2026-03-05

### 📄 论文摘要

The ability to interpret machine learning model decisions is critical in such domains as healthcare, where trust in model predictions is as important as their accuracy. Inspired by the development of prototype parts-based deep neural networks in computer vision, we propose a new model for tabular data, specifically tailored to medical records, that requires discretization of diagnostic result norms. Unlike the original vision models that rely on the spatial structure, our method employs trainable patching over features describing a patient, to learn meaningful prototypical parts from structured data. These parts are represented as binary or discretized feature subsets. This allows the model to express prototypes in human-readable terms, enabling alignment with clinical language and case-based reasoning. Our proposed neural network is inherently interpretable and offers interpretable concept-based predictions by comparing the patient's description to learned prototypes in the latent space of the network. In experiments, we demonstrate that the model achieves classification performance competitive to widely used baseline models on medical benchmark datasets, while also offering transparency, bridging the gap between predictive performance and interpretability in clinical decision support.

### 🤖 AI 总结

**一句话总结**：论文提出一种面向医疗表格数据的可解释“原型部件”神经网络，通过学习可读的离散/二值特征子集原型来实现透明预测且保持竞争性性能。

**研究动机**：医疗场景不仅需要高准确率，还必须让临床人员理解模型依据以建立信任并支持病例式推理；但表格病历数据缺乏视觉任务中的空间结构，使既可解释又高性能的深度模型更难设计。

**核心方法**：将诊断指标按“正常范围”进行离散化，并在特征维度上引入可训练的“patching”机制，从患者特征中学习由二值或离散特征子集构成的原型部件；预测时在网络潜空间中将患者表示与这些原型进行相似度比较，从而给出概念化、可用临床语言描述的解释。

**主要结论**：在多个医疗基准数据集上，该模型的分类效果与常用基线方法相当，同时提供基于原型对比的内生可解释性，缩小了临床决策支持中性能与可解释性之间的差距。

**关键词**：可解释神经网络, 原型网络, 部件原型, 表格数据建模, 医疗结构化数据, 特征离散化, 可训练特征分块, 概念驱动预测, 病例推理, 原型相似度解释

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05423v1) | [下载PDF](https://arxiv.org/pdf/2603.05423v1.pdf)

---

## [30. On the Necessity of Learnable Sheaf Laplacians](https://arxiv.org/abs/2603.05395v1)

**作者**：Ferran Hernandez Caralt, Mar Gonzàlez i Català, Adrián Bazaga 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-05

### 📄 论文摘要

Sheaf Neural Networks (SNNs) were introduced as an extension of Graph Convolutional Networks to address oversmoothing on heterophilous graphs by attaching a sheaf to the input graph and replacing the adjacency-based operator with a sheaf Laplacian defined by (learnable) restriction maps. Prior work motivates this design through theoretical properties of sheaf diffusion and the kernel of the sheaf Laplacian, suggesting that suitable non-identity restriction maps can avoid representations converging to constants across connected components. Since oversmoothing can also be mitigated through residual connections and normalization, we revisit a trivial sheaf construction to ask whether the additional complexity of learning restriction maps is necessary. We introduce an Identity Sheaf Network baseline, where all restriction maps are fixed to the identity, and use it to ablate the empirical improvements reported by sheaf-learning architectures. Across five popular heterophilic benchmarks, the identity baseline achieves comparable performance to a range of SNN variants. Finally, we introduce the Rayleigh quotient as a normalized measure for comparing oversmoothing across models and show that, in trained networks, the behavior predicted by the diffusion-based analysis of SNNs is not reflected empirically. In particular, Identity Sheaf Networks do not appear to suffer more significant oversmoothing than their SNN counterparts.

### 🤖 AI 总结

**一句话总结**：论文发现：在异配图上，固定为恒等限制映射的“Identity Sheaf Network”与需要学习限制映射的多种SNN变体表现相当，学习sheaf拉普拉斯可能并非必要。

**研究动机**：既有SNN通过可学习限制映射构造sheaf拉普拉斯来缓解过平滑，并以扩散/核空间理论作为动机；但残差与归一化等机制也能缓解过平滑，因此作者质疑“学习限制映射”是否真是性能提升的关键来源。

**核心方法**：提出Identity Sheaf Network基线：将所有restriction maps固定为identity，并在5个常用异配基准上与多种SNN架构做消融对比；同时引入Rayleigh quotient作为归一化指标，用于跨模型比较训练后表征的过平滑程度。

**主要结论**：Identity基线在多个基准上达到与SNN变体相近的精度，说明学习restriction maps带来的经验收益有限；且用Rayleigh quotient观察到训练后模型的过平滑行为并未体现扩散理论所预测的优势，Identity网络也未表现出更严重的过平滑。

**关键词**：可学习限制映射, 异配图, 过平滑, 消融实验, 残差连接, 归一化, 图卷积网络, Necessity

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05395v1) | [下载PDF](https://arxiv.org/pdf/2603.05395v1.pdf)

---

