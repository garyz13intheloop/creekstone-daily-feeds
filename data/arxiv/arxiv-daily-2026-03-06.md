# arXiv AI 论文日报 | 2026-03-06

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

**一句话总结**：提出平均偏差有界（A-BB）评估框架，为LLM-as-a-Judge在存在可测偏差时提供可证明的“伤害/影响降低”保证，并在多种偏差设置下保持较高排名一致性。

**研究动机**：未来自治AI将依赖自动化、可验证的奖励/反馈，但在缺乏确定真值时常用LLM裁判；现有LLM裁判在偏差向量未知或可被对抗性挖掘时缺少强保证。

**核心方法**：提出A-BB算法框架，通过对裁判可测偏差施加平均意义上的有界约束，形式化保证偏差带来的负面影响下降；在Arena-Hard-Auto上用4个LLM裁判测试，在格式与schematic偏差场景下评估其偏差有界性与原始排名相关性。

**主要结论**：在Arena-Hard-Auto上实现了(τ=0.5, δ=0.01)的偏差有界保证，同时与原始排名保持61–99%的相关性，多数组合超过80%，表明可在提供理论偏差控制的同时较好保留评测信号。

**关键词**：偏差有界评测, 无偏性保证, 偏差向量, 自动化奖励信号, 反馈回路, 形式化鲁棒性, 评测相关性保持, 格式偏差, 框架性偏差

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05485v1) | [下载PDF](https://arxiv.org/pdf/2603.05485v1.pdf)

---

## [2. Distributed Partial Information Puzzles: Examining Common Ground Construction Under Epistemic Asymmetry](https://arxiv.org/abs/2603.05450v1)

**作者**：Yifan Zhu, Mariah Bradford, Kenneth Lai 等 7 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-03-05

### 📄 论文摘要

Establishing common ground, a shared set of beliefs and mutually recognized facts, is fundamental to collaboration, yet remains a challenge for current AI systems, especially in multimodal, multiparty settings, where the collaborators bring different information to the table. We introduce the Distributed Partial Information Puzzle (DPIP), a collaborative construction task that elicits rich multimodal communication under epistemic asymmetry. We present a multimodal dataset of these interactions, annotated and temporally aligned across speech, gesture, and action modalities to support reasoning over propositional content and belief dynamics. We then evaluate two paradigms for modeling common ground (CG): (1) state-of-the-art large language models (LLMs), prompted to infer shared beliefs from multimodal updates, and (2) an axiomatic pipeline grounded in Dynamic Epistemic Logic (DEL) that incrementally performs the same task. Results on the annotated DPIP data indicate that it poses a challenge to modern LLMs' abilities to track both task progression and belief state.

### 🤖 AI 总结

**一句话总结**：提出DPIP协作拼图任务与多模态数据集，用于检验在信息不对称下构建“共同基础”(CG)的能力，并发现当前LLM在跟踪任务与信念状态上仍明显吃力。

**研究动机**：多方多模态协作中，各参与者掌握的信息不同，AI要有效协作必须持续建立并更新共同基础，但现有系统在这类信念对齐与追踪上不足。为此需要一个能系统诱发丰富交流、并可标注信念动态的基准任务与数据。

**核心方法**：设计Distributed Partial Information Puzzle（DPIP）协作构建任务，采集并时间对齐标注语音-手势-动作等多模态交互，支持命题内容与信念动态推理；在该数据上比较两类CG建模：提示LLM从多模态更新推断共享信念，以及基于动态认知逻辑（DEL）的公理化增量推理流水线。

**主要结论**：DPIP对现代LLM构成显著挑战：其难以同时稳定跟踪任务进展与多方信念状态更新；相对地，DEL式显式推理为增量构建共同基础提供了更结构化的对照与诊断路径。

**关键词**：共同基底建构, 认知不对称, 多模态多方协作, 分布式部分信息谜题（DPIP）, 多模态交互数据集, 时序对齐标注, 信念状态跟踪, 命题内容推理, 动态认知逻辑（DEL）, LLM多模态提示推理, 公有信念建模评测

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05450v1) | [下载PDF](https://arxiv.org/pdf/2603.05450v1.pdf)

---

## [3. Judge Reliability Harness: Stress Testing the Reliability of LLM Judges](https://arxiv.org/abs/2603.05399v1)

**作者**：Sunishchal Dev, Andrew Sloan, Joshua Kavner 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-03-05

### 📄 论文摘要

We present the Judge Reliability Harness, an open source library for constructing validation suites that test the reliability of LLM judges. As LLM based scoring is widely deployed in AI benchmarks, more tooling is needed to efficiently assess the reliability of these methods. Given a benchmark dataset and an LLM judge configuration, the harness generates reliability tests that evaluate both binary judgment accuracy and ordinal grading performance for free-response and agentic task formats. We evaluate four state-of-the-art judges across four benchmarks spanning safety, persuasion, misuse, and agentic behavior, and find meaningful variation in performance across models and perturbation types, highlighting opportunities to improve the robustness of LLM judges. No judge that we evaluated is uniformly reliable across benchmarks using our harness. For example, our preliminary experiments on judges revealed consistency issues as measured by accuracy in judging another LLM's ability to complete a task due to simple text formatting changes, paraphrasing, changes in verbosity, and flipping the ground truth label in LLM-produced responses. The code for this tool is available at: https://github.com/RANDCorporation/judge-reliability-harness

### 🤖 AI 总结

**一句话总结**：提出开源的Judge Reliability Harness，用系统化扰动与测试套件来压力测试LLM评审（judge）的可靠性，并发现不同评审在不同基准与扰动下表现差异显著且无一“全能可靠”。

**研究动机**：LLM作为自动评分/评审已广泛用于各类AI基准，但缺少高效、标准化工具来评估其在不同任务与表述变化下的稳定性与一致性。作者希望用可复用的验证套件揭示评审的脆弱点并推动更鲁棒的judge设计。

**核心方法**：给定基准数据集与LLM judge配置，harness自动生成可靠性测试，覆盖二元判断准确性与序数评分表现，并适配自由回答与agentic任务格式。作者用该工具在安全、说服、滥用、agentic行为等4类基准上评测4个SOTA评审，并通过格式变化、改写、冗长度变化、标签翻转等扰动检验一致性。

**主要结论**：评审可靠性随模型、基准与扰动类型而显著波动，且没有任何一个被测judge能在所有基准上保持统一可靠。简单的文本格式与表述变化就会导致评审一致性问题，表明需要针对鲁棒性进行改进与系统化验证。

**关键词**：LLM评审可靠性, LLM评审压力测试, 评测验证套件, 基准评测工具, 二分类判定准确率, 序数评分一致性, 自由回答评测, 扰动鲁棒性评估, 文本格式敏感性, 释义与冗长度扰动

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05399v1) | [下载PDF](https://arxiv.org/pdf/2603.05399v1.pdf)

---

## [4. Legal interpretation and AI: from expert systems to argumentation and LLMs](https://arxiv.org/abs/2603.05392v1)

**作者**：Václav Janeček, Giovanni Sartor  
**分类**：cs.AI  
**发布时间**：2026-03-05

### 📄 论文摘要

AI and Law research has encountered legal interpretation in different ways, in the context of its evolving approaches and methodologies. Research on expert system has focused on legal knowledge engineering, with the goal of ensuring that human-generated interpretations can be precisely transferred into knowledge-bases, to be consistently applied. Research on argumentation has aimed at representing the structure of interpretive arguments, as well as their dialectical interactions, to assess of the acceptability of interpretive claims within argumentation frameworks. Research on machine learning has focused on the automated generation of interpretive suggestions and arguments, through general and specialised language models, now being increasingly deployed in legal practice.

### 🤖 AI 总结

**一句话总结**：论文梳理了AI与法律研究中“法律解释”的三条演进路径：从专家系统的知识工程，到论证理论的可接受性评估，再到以LLM为代表的机器学习生成式解释建议。

**研究动机**：法律解释是法律实践的核心任务，而AI与法律领域在不同技术范式下对“如何表示、评估与生成解释”形成了分散的研究脉络，需要系统性对比与整合以指导当下LLM落地。

**核心方法**：采用综述/概念分析方式，对三类方法进行框架化比较：专家系统侧重将人类解释精确编码并一致适用；论证方法侧重表示解释性论证结构及其辩证交互并在论证框架中评估可接受性；机器学习/语言模型侧重自动生成解释性建议与论证。

**主要结论**：AI与法律对解释问题的处理从“手工编码的稳定一致性”转向“结构化论证的可评估性”，再到“数据驱动的自动生成与部署”，其中LLM带来强生成能力但也意味着解释不再仅靠规则转写或形式化评估即可完全保障其可靠性与一致性。

**关键词**：法律解释, AI与法律, 法律知识工程, 法律知识库, 专家系统, 可解释性论证, 论证框架, 辩证互动, 主张可接受性评估, 法律语言模型

**评分**：7

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

**一句话总结**：提出“无检索事实核查”任务与评测框架，并通过利用LLM内部表征交互的INTRA方法在多数据集上取得更强泛化与SOTA表现。

**研究动机**：现有事实核查多依赖外部检索，易受检索错误与数据可用性限制，同时未充分利用LLM参数中已编码的内在知识与核查能力。

**核心方法**：构建覆盖9个数据集的无检索评测框架，重点测试对长尾知识、来源变化、多语种与长文本生成的鲁棒性；比较18种方法后提出INTRA，通过挖掘并交互利用模型内部表示而非仅依赖logit信号来判定事实性。

**主要结论**：实验显示logit类方法整体不如利用内部表征的方法，INTRA在多个设置下达到最优且具强泛化；无检索事实核查可作为检索式框架的补充，提升可扩展性，并可用作训练奖励信号或集成到生成过程中。

**关键词**：无检索事实核查, LLM参数知识, 内在事实验证, 内部表征交互, 鲁棒性评测框架, 长尾知识, 多来源声明, 多语言事实核查, 长文本生成核查, 奖励信号训练

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05471v1) | [下载PDF](https://arxiv.org/pdf/2603.05471v1.pdf)

---

## [6. NCTB-QA: A Large-Scale Bangla Educational Question Answering Dataset and Benchmarking Performance](https://arxiv.org/abs/2603.05462v1)

**作者**：Abrar Eyasir, Tahsin Ahmed, Muhammad Ibrahim  
**分类**：cs.CL  
**发布时间**：2026-03-05

### 📄 论文摘要

Reading comprehension systems for low-resource languages face significant challenges in handling unanswerable questions. These systems tend to produce unreliable responses when correct answers are absent from context. To solve this problem, we introduce NCTB-QA, a large-scale Bangla question answering dataset comprising 87,805 question-answer pairs extracted from 50 textbooks published by Bangladesh's National Curriculum and Textbook Board. Unlike existing Bangla datasets, NCTB-QA maintains a balanced distribution of answerable (57.25%) and unanswerable (42.75%) questions. NCTB-QA also includes adversarially designed instances containing plausible distractors. We benchmark three transformer-based models (BERT, RoBERTa, ELECTRA) and demonstrate substantial improvements through fine-tuning. BERT achieves 313% relative improvement in F1 score (0.150 to 0.620). Semantic answer quality measured by BERTScore also increases significantly across all models. Our results establish NCTB-QA as a challenging benchmark for Bangla educational question answering. This study demonstrates that domain-specific fine-tuning is critical for robust performance in low-resource settings.

### 🤖 AI 总结

**一句话总结**：本文提出并发布NCTB-QA这一大规模孟加拉语教育阅读理解数据集（含可回答与不可回答问题），并基准评测显示领域微调能显著提升模型鲁棒性与答案质量。

**研究动机**：低资源语言的阅读理解系统在遇到“上下文中无答案”的问题时常产生不可靠输出，且现有孟加拉语数据集对不可回答问题与干扰项覆盖不足。

**核心方法**：从孟加拉国国家教材委员会的50本教材中抽取构建87,805个问答对，保持可回答(57.25%)与不可回答(42.75%)的均衡分布，并加入带“似是而非干扰项”的对抗样本；在该基准上对BERT/RoBERTa/ELECTRA进行微调与评测（F1与BERTScore）。

**主要结论**：微调后三种Transformer均显著提升，其中BERT的F1相对提升达313%（0.150→0.620），BERTScore等语义质量指标也同步改善；NCTB-QA因此成为评估孟加拉语教育QA与不可回答处理能力的高难度基准，强调领域数据微调在低资源场景的关键性。

**关键词**：孟加拉语问答, 教育问答数据集, 可拒答问答, 低资源语言, 基准评测, F1指标, NCTB-QA, Large-Scale

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05462v1) | [下载PDF](https://arxiv.org/pdf/2603.05462v1.pdf)

---

## [7. DEBISS: a Corpus of Individual, Semi-structured and Spoken Debates](https://arxiv.org/abs/2603.05459v1)

**作者**：Klaywert Danillo Ferreira de Souza, David Eduardo Pereira, Cláudio E. C. Campelo 等 4 位作者  
**分类**：cs.CL, cs.DB  
**发布时间**：2026-03-05

### 📄 论文摘要

The process of debating is essential in our daily lives, whether in studying, work activities, simple everyday discussions, political debates on TV, or online discussions on social networks. The range of uses for debates is broad. Due to the diverse applications, structures, and formats of debates, developing corpora that account for these variations can be challenging, and the scarcity of debate corpora in the state of the art is notable. For this reason, the current research proposes the DEBISS corpus: a collection of spoken and individual debates with semi-structured features. With a broad range of NLP task annotations, such as speech-to-text, speaker diarization, argument mining, and debater quality assessment.

### 🤖 AI 总结

**一句话总结**：DEBISS 提供一个面向口语、个人、半结构化辩论的新语料库，并附带多种NLP任务标注以支持辩论相关研究。

**研究动机**：现有辩论语料库稀缺且难以覆盖辩论在结构、形式与应用场景上的多样性，限制了辩论分析与建模研究。为此需要一个更贴近真实口语与多任务需求的标准化数据资源。

**核心方法**：构建 DEBISS 语料库，收集“个人+口语+半结构化”的辩论数据，并提供覆盖语音与文本层面的多任务标注，包括语音转写（STT）、说话人分离、论证/论点挖掘以及辩手质量评估等。

**主要结论**：DEBISS 通过多维度标注填补了辩论语料资源不足的问题，可作为统一基准支持多种辩论相关NLP与语音任务的训练、评测与对比研究。

**关键词**：辩论语料库, 口语辩论, 半结构化语料, 个体辩论, 语音转写, 说话人分离, 论证挖掘, 辩手质量评估, 多任务标注

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05459v1) | [下载PDF](https://arxiv.org/pdf/2603.05459v1.pdf)

---

## [8. FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://arxiv.org/abs/2603.05451v1)

**作者**：Ted Zadouri, Markus Hoehnerbach, Jay Shah 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-05

### 📄 论文摘要

Attention, as a core layer of the ubiquitous Transformer architecture, is the bottleneck for large language models and long-context applications. While FlashAttention-3 optimized attention for Hopper GPUs through asynchronous execution and warp specialization, it primarily targets the H100 architecture. The AI industry has rapidly transitioned to deploying Blackwell-based systems such as the B200 and GB200, which exhibit fundamentally different performance characteristics due to asymmetric hardware scaling: tensor core throughput doubles while other functional units (shared memory bandwidth, exponential units) scale more slowly or remain unchanged. We develop several techniques to address these shifting bottlenecks on Blackwell GPUs: (1) redesigned pipelines that exploit fully asynchronous MMA operations and larger tile sizes, (2) software-emulated exponential and conditional softmax rescaling that reduces non-matmul operations, and (3) leveraging tensor memory and the 2-CTA MMA mode to reduce shared memory traffic and atomic adds in the backward pass. We demonstrate that our method, FlashAttention-4, achieves up to 1.3$\times$ speedup over cuDNN 9.13 and 2.7$\times$ over Triton on B200 GPUs with BF16, reaching up to 1613 TFLOPs/s (71% utilization). Beyond algorithmic innovations, we implement FlashAttention-4 entirely in CuTe-DSL embedded in Python, achieving 20-30$\times$ faster compile times compared to traditional C++ template-based approaches while maintaining full expressivity.

### 🤖 AI 总结

**一句话总结**：FlashAttention-4 面向 Blackwell GPU 的非对称硬件扩展重新共设计注意力算法与内核流水线，在 B200 上显著提升吞吐与利用率。

**研究动机**：Blackwell（B200/GB200）上张量核吞吐翻倍但共享内存带宽、exp 等单元扩展较慢，导致 FlashAttention-3 针对 H100 的瓶颈假设不再成立，需要新的瓶颈匹配与优化。

**核心方法**：通过完全异步的 MMA 与更大 tile 重构流水线；用软件模拟 exp 与条件 softmax rescale 以减少非 matmul 开销；在反向传播中利用 tensor memory 与 2-CTA MMA 降低共享内存流量与 atomic add。

**主要结论**：在 B200 BF16 上相对 cuDNN 9.13 最多提速 1.3×、相对 Triton 最多 2.7×，峰值达 1613 TFLOPs/s（71% 利用率）；同时用嵌入 Python 的 CuTe-DSL 实现，编译时间比传统 C++ 模板方案快 20–30×且保持表达能力。

**关键词**：注意力算子优化, GPU 内核融合, tile 大小优化, 指数函数仿真, 共享内存带宽瓶颈, 张量内存, FlashAttention-4, Algorithm

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05451v1) | [下载PDF](https://arxiv.org/pdf/2603.05451v1.pdf)

---

## [9. An Exploration-Analysis-Disambiguation Reasoning Framework for Word Sense Disambiguation with Low-Parameter LLMs](https://arxiv.org/abs/2603.05400v1)

**作者**：Deshan Sumanathilaka, Nicholas Micallef, Julian Hough  
**分类**：cs.CL  
**发布时间**：2026-03-05

### 📄 论文摘要

Word Sense Disambiguation (WSD) remains a key challenge in Natural Language Processing (NLP), especially when dealing with rare or domain-specific senses that are often misinterpreted. While modern high-parameter Large Language Models (LLMs) such as GPT-4-Turbo have shown state-of-the-art WSD performance, their computational and energy demands limit scalability. This study investigates whether low-parameter LLMs (<4B parameters) can achieve comparable results through fine-tuning strategies that emphasize reasoning-driven sense identification. Using the FEWS dataset augmented with semi-automated, rationale-rich annotations, we fine-tune eight small-scale open-source LLMs (e.g. Gemma and Qwen). Our results reveal that Chain-of-Thought (CoT)-based reasoning combined with neighbour-word analysis achieves performance comparable to GPT-4-Turbo in zero-shot settings. Importantly, Gemma-3-4B and Qwen-3-4B models consistently outperform all medium-parameter baselines and state-of-the-art models on FEWS, with robust generalization to unseen senses. Furthermore, evaluation on the unseen "Fool Me If You Can'' dataset confirms strong cross-domain adaptability without task-specific fine-tuning. This work demonstrates that with carefully crafted reasoning-centric fine-tuning, low-parameter LLMs can deliver accurate WSD while substantially reducing computational and energy demands.

### 🤖 AI 总结

**一句话总结**：论文提出“探索-分析-消歧”的推理式微调框架，使低参数LLM（<4B）在词义消歧任务上达到接近甚至超过高参数模型的效果。

**研究动机**：高参数LLM在WSD上表现强但算力与能耗成本高，且稀有/领域词义易被误判；作者希望验证小模型能否通过更强的推理导向训练获得可比性能与更好可扩展性。

**核心方法**：基于FEWS数据集并补充半自动生成的“带理由”标注，对8个小型开源LLM（如Gemma、Qwen）进行强调Chain-of-Thought与邻近词分析的推理式微调，并测试其对未见词义与跨域数据集（Fool Me If You Can）的泛化。

**主要结论**：CoT推理结合邻近词分析可使小模型在零样本对比中达到接近GPT-4-Turbo的WSD表现；Gemma-3-4B与Qwen-3-4B在FEWS上优于中等规模与SOTA基线，并在跨域未微调评测中保持强适应性，显著降低计算与能耗成本。

**关键词**：词义消歧, 低参数 LLM, 推理式微调, 邻词分析, 理由标注, 零样本评测, 未见词义泛化, 跨域迁移, 小模型对齐, 算力能耗降低

**评分**：23

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

**一句话总结**：提出一种面向稀疏多相机实时3D流媒体的多视角感知Transformer修补网络，在保证时序一致性的同时以较高速度补全渲染视图中的缺失纹理。

**研究动机**：实时AR/VR常受限于相机视角数量，导致新视角渲染出现孔洞与表面缺失；现有基于启发式的填洞在多帧与多视角间易不一致并产生伪影。

**核心方法**：将修补作为与底层3D表示无关的图像后处理模块，设计多视角感知的Transformer架构并引入时空嵌入以增强跨帧一致性与细节保真；采用分辨率无关设计与自适应patch选择，在质量与推理速度间动态权衡以满足实时性。

**主要结论**：在相同实时约束下，相比SOTA修补方法该模型在图像与视频指标上取得更优的质量-速度折中，并减少视觉伪影、提升跨帧稳定性。

**关键词**：三维实时流式传输, 多摄像机稀疏视角, 新视角合成, 图像修复, 空洞填补, 多视角一致性, 时空嵌入, 分辨率无关, 自适应补丁选择, 视频指标评测

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05507v1) | [下载PDF](https://arxiv.org/pdf/2603.05507v1.pdf)

---

## [11. FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning](https://arxiv.org/abs/2603.05506v1)

**作者**：Weijie Lyu, Ming-Hsuan Yang, Zhixin Shu  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

We introduce FaceCam, a system that generates video under customizable camera trajectories for monocular human portrait video input. Recent camera control approaches based on large video-generation models have shown promising progress but often exhibit geometric distortions and visual artifacts on portrait videos due to scale-ambiguous camera representations or 3D reconstruction errors. To overcome these limitations, we propose a face-tailored scale-aware representation for camera transformations that provides deterministic conditioning without relying on 3D priors. We train a video generation model on both multi-view studio captures and in-the-wild monocular videos, and introduce two camera-control data generation strategies: synthetic camera motion and multi-shot stitching, to exploit stationary training cameras while generalizing to dynamic, continuous camera trajectories at inference time. Experiments on Ava-256 dataset and diverse in-the-wild videos demonstrate that FaceCam achieves superior performance in camera controllability, visual quality, identity and motion preservation.

### 🤖 AI 总结

**一句话总结**：FaceCam 通过面向人像的尺度感知相机表示，实现对单目人像视频进行可控相机轨迹的视频生成，并显著减少几何畸变与伪影。

**研究动机**：现有基于大规模视频生成模型的相机控制在“人像”场景中常因尺度歧义的相机表示或3D重建误差导致形变与视觉瑕疵，难以同时保证可控性与身份/运动一致性。

**核心方法**：提出无需3D先验的、针对人脸/人像的尺度感知相机变换表示，作为确定性的条件输入；并结合多视角棚拍与野外单目数据训练，同时用“合成相机运动”和“多镜头拼接”两种数据生成策略，让静态训练机位也能学习到推理时连续动态轨迹的控制能力。

**主要结论**：在 Ava-256 与多样化野外视频上，FaceCam 在相机可控性、画质、身份保持与动作保持方面优于现有方法，且在人像视频中更能抑制几何扭曲与伪影。

**关键词**：人像视频相机控制, 可控视频生成, 单目人像视频, 相机轨迹条件化, 尺度感知条件, 相机变换表示, 确定性条件控制, 无3D先验, 多视角数据训练, 合成相机运动, 多镜头拼接, Ava-256 数据集

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05506v1) | [下载PDF](https://arxiv.org/pdf/2603.05506v1.pdf)

---

## [12. Towards Multimodal Lifelong Understanding: A Dataset and Agentic Baseline](https://arxiv.org/abs/2603.05484v1)

**作者**：Guo Chen, Lidong Lu, Yicheng Liu 等 20 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

While datasets for video understanding have scaled to hour-long durations, they typically consist of densely concatenated clips that differ from natural, unscripted daily life. To bridge this gap, we introduce MM-Lifelong, a dataset designed for Multimodal Lifelong Understanding. Comprising 181.1 hours of footage, it is structured across Day, Week, and Month scales to capture varying temporal densities. Extensive evaluations reveal two critical failure modes in current paradigms: end-to-end MLLMs suffer from a Working Memory Bottleneck due to context saturation, while representative agentic baselines experience Global Localization Collapse when navigating sparse, month-long timelines. To address this, we propose the Recursive Multimodal Agent (ReMA), which employs dynamic memory management to iteratively update a recursive belief state, significantly outperforming existing methods. Finally, we establish dataset splits designed to isolate temporal and domain biases, providing a rigorous foundation for future research in supervised learning and out-of-distribution generalization.

### 🤖 AI 总结

**一句话总结**：提出面向真实日常长时序视频理解的MM-Lifelong数据集，并给出递归式多模态智能体ReMA作为强基线以缓解长上下文与稀疏时间轴下的失效问题。

**研究动机**：现有长视频理解数据多为密集拼接片段，难以反映自然、非脚本化的日常生活时间结构；同时现有方法在超长时序下易因上下文饱和或时间定位失败而性能崩塌。

**核心方法**：构建181.1小时、按Day/Week/Month多时间尺度组织的MM-Lifelong，并系统评测揭示两类失效模式：端到端MLLM的“工作记忆瓶颈”和智能体基线的“全局定位崩塌”；提出ReMA通过动态记忆管理迭代更新递归信念状态以提升跨长时序检索与推理能力。

**主要结论**：ReMA在该数据集上显著优于现有方法，证明递归记忆与信念更新对长时序多模态理解有效；同时数据集划分可隔离时间与领域偏置，为监督学习与OOD泛化研究提供更严格基准。

**关键词**：自然日常视频数据集, 多尺度时间建模, 工作记忆瓶颈, 上下文饱和, Agent 记忆管理, 全局定位崩溃, 递归信念状态, 时间偏置隔离评测, 分布外泛化（OOD）

**评分**：46

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05484v1) | [下载PDF](https://arxiv.org/pdf/2603.05484v1.pdf)

---

## [13. Towards 3D Scene Understanding of Gas Plumes in LWIR Hyperspectral Images Using Neural Radiance Fields](https://arxiv.org/abs/2603.05473v1)

**作者**：Scout Jarman, Zigfried Hampel-Arias, Adra Carr 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

Hyperspectral images (HSI) have many applications, ranging from environmental monitoring to national security, and can be used for material detection and identification. Longwave infrared (LWIR) HSI can be used for gas plume detection and analysis. Oftentimes, only a few images of a scene of interest are available and are analyzed individually. The ability to combine information from multiple images into a single, cohesive representation could enhance analysis by providing more context on the scene's geometry and spectral properties. Neural radiance fields (NeRFs) create a latent neural representation of volumetric scene properties that enable novel-view rendering and geometry reconstruction, offering a promising avenue for hyperspectral 3D scene reconstruction. We explore the possibility of using NeRFs to create 3D scene reconstructions from LWIR HSI and demonstrate that the model can be used for the basic downstream analysis task of gas plume detection. The physics-based DIRSIG software suite was used to generate a synthetic multi-view LWIR HSI dataset of a simple facility with a strong sulfur hexafluoride gas plume. Our method, built on the standard Mip-NeRF architecture, combines state-of-the-art methods for hyperspectral NeRFs and sparse-view NeRFs, along with a novel adaptive weighted MSE loss. Our final NeRF method requires around 50% fewer training images than the standard Mip-NeRF and achieves an average PSNR of 39.8 dB with as few as 30 training images. Gas plume detection applied to NeRF-rendered test images using the adaptive coherence estimator achieves an average AUC of 0.821 when compared with detection masks generated from ground-truth test images.

### 🤖 AI 总结

**一句话总结**：提出一种基于Mip-NeRF改造的LWIR高光谱NeRF，在稀疏多视角条件下实现3D场景/光谱重建，并能用于气体羽流检测。

**研究动机**：LWIR高光谱图像常只有少量视角且被单独分析，难以综合利用多视角信息获得统一的几何与光谱表征。将多张HSI融合为可新视角渲染的3D表示，有望提升气体羽流等下游分析的准确性与鲁棒性。

**核心方法**：使用DIRSIG生成含SF6强气体羽流的合成多视角LWIR HSI数据集，在标准Mip-NeRF上融合高光谱NeRF与稀疏视角NeRF技术，并引入自适应加权MSE损失以强化训练稳定性与重建质量。训练后从NeRF渲染测试视角，再用自适应相干估计器（ACE）进行气体羽流检测评估。

**主要结论**：相比标准Mip-NeRF，该方法在训练图像数上减少约50%，仅用30张训练图像仍达到平均PSNR约39.8 dB。基于NeRF渲染图像进行羽流检测的平均AUC为0.821，表明NeRF重建可支持基本的气体检测下游任务。

**关键词**：长波红外高光谱成像, 气体羽流检测, 稀疏视角 NeRF, 新视角合成, 几何重建, 自适应加权 MSE 损失, 自适应相干估计器, 物理仿真合成数据

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05473v1) | [下载PDF](https://arxiv.org/pdf/2603.05473v1.pdf)

---

## [14. EdgeDAM: Real-time Object Tracking for Mobile Devices](https://arxiv.org/abs/2603.05463v1)

**作者**：Syed Muhammad Raza, Syed Murtaza Hussain Abidi, Khawar Islam 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

Single-object tracking (SOT) on edge devices is a critical computer vision task, requiring accurate and continuous target localization across video frames under occlusion, distractor interference, and fast motion. However, recent state-of-the-art distractor-aware memory mechanisms are largely built on segmentation-based trackers and rely on mask prediction and attention-driven memory updates, which introduce substantial computational overhead and limit real-time deployment on resource-constrained hardware; meanwhile, lightweight trackers sustain high throughput but are prone to drift when visually similar distractors appear. To address these challenges, we propose EdgeDAM, a lightweight detection-guided tracking framework that reformulates distractor-aware memory for bounding-box tracking under strict edge constraints. EdgeDAM introduces two key strategies: (1) Dual-Buffer Distractor-Aware Memory (DAM), which integrates a Recent-Aware Memory to preserve temporally consistent target hypotheses and a Distractor-Resolving Memory to explicitly store hard negative candidates and penalize their re-selection during recovery; and (2) Confidence-Driven Switching with Held-Box Stabilization, where tracker reliability and temporal consistency criteria adaptively activate detection and memory-guided re-identification during occlusion, while a held-box mechanism temporarily freezes and expands the estimate to suppress distractor contamination. Extensive experiments on five benchmarks, including the distractor-focused DiDi dataset, demonstrate improved robustness under occlusion and fast motion while maintaining real-time performance on mobile devices, achieving 88.2% accuracy on DiDi and 25 FPS on an iPhone 15. Code will be released.

### 🤖 AI 总结

**一句话总结**：EdgeDAM 面向移动端提出轻量级的“检测引导+干扰物记忆”单目标跟踪框架，在遮挡与相似干扰下提升鲁棒性同时保持实时速度。

**研究动机**：现有干扰物感知记忆多依赖分割与注意力更新，计算开销大不适合边缘端实时；而轻量跟踪器虽快但遇到相似干扰物易漂移、遮挡后难恢复。

**核心方法**：提出双缓冲干扰物感知记忆（DAM）：Recent-Aware Memory 保留近期稳定目标假设，Distractor-Resolving Memory 存储硬负样本并在恢复阶段抑制其被再次选中；再通过“置信度驱动切换+Held-Box 稳定化”在低置信/不一致时触发检测与记忆重识别，并用冻结并适度扩张的框抑制干扰污染。

**主要结论**：在包括干扰物强的 DiDi 等5个基准上，EdgeDAM 在遮挡与快速运动场景下更稳健，同时在手机端实现实时（iPhone 15 上 25 FPS），并在 DiDi 上达到 88.2% 准确率。

**关键词**：单目标跟踪, 边缘设备视觉, 移动端实时推理, 检测引导跟踪, 边界框跟踪, 干扰物鲁棒性, 干扰感知记忆, 双缓冲记忆, 硬负样本挖掘, 遮挡恢复, 置信度切换机制, 轨迹漂移抑制

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05463v1) | [下载PDF](https://arxiv.org/pdf/2603.05463v1.pdf)

---

## [15. RealWonder: Real-Time Physical Action-Conditioned Video Generation](https://arxiv.org/abs/2603.05449v1)

**作者**：Wei Liu, Ziyu Chen, Zizhang Li 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-03-05

### 📄 论文摘要

Current video generation models cannot simulate physical consequences of 3D actions like forces and robotic manipulations, as they lack structural understanding of how actions affect 3D scenes. We present RealWonder, the first real-time system for action-conditioned video generation from a single image. Our key insight is using physics simulation as an intermediate bridge: instead of directly encoding continuous actions, we translate them through physics simulation into visual representations (optical flow and RGB) that video models can process. RealWonder integrates three components: 3D reconstruction from single images, physics simulation, and a distilled video generator requiring only 4 diffusion steps. Our system achieves 13.2 FPS at 480x832 resolution, enabling interactive exploration of forces, robot actions, and camera controls on rigid objects, deformable bodies, fluids, and granular materials. We envision RealWonder opens new opportunities to apply video models in immersive experiences, AR/VR, and robot learning. Our code and model weights are publicly available in our project website: https://liuwei283.github.io/RealWonder/

### 🤖 AI 总结

**一句话总结**：RealWonder通过“物理仿真→可视化中间表示”的桥接方式，实现从单张图像出发、可实时交互的物理动作条件视频生成。

**研究动机**：现有视频生成模型缺乏对动作如何影响3D场景的结构化理解，难以生成符合物理后果的力、机器人操作等动作结果。为支持交互式探索与机器人/沉浸式应用，需要既物理一致又足够快的动作条件生成系统。

**核心方法**：系统由单图3D重建、物理仿真、以及蒸馏后的快速扩散视频生成器组成；将连续动作先在仿真中转成光流与RGB等视觉表征，再输入视频模型生成结果。通过将扩散步骤蒸馏到仅4步，实现实时推理并支持多类对象（刚体/可变形体/流体/颗粒）与相机控制。

**主要结论**：在480×832分辨率下达到约13.2 FPS，能够实时生成受力、机器人动作与视角变化下的物理一致视频。该框架证明了以物理仿真作为中间层可显著提升动作可控性与物理合理性，并具备AR/VR与机器人学习等应用潜力。

**关键词**：动作条件视频生成, 单图视频生成, 物理仿真桥接, 3D场景重建, 光流引导, 扩散模型蒸馏, 少步扩散推理, 实时视频生成, 机器人操作建模, 可交互相机控制, 多物理材质建模

**评分**：46

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05449v1) | [下载PDF](https://arxiv.org/pdf/2603.05449v1.pdf)

---

## [16. NaiLIA: Multimodal Nail Design Retrieval Based on Dense Intent Descriptions and Palette Queries](https://arxiv.org/abs/2603.05446v1)

**作者**：Kanon Amemiya, Daichi Yashima, Kei Katsumata 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

We focus on the task of retrieving nail design images based on dense intent descriptions, which represent multi-layered user intent for nail designs. This is challenging because such descriptions specify unconstrained painted elements and pre-manufactured embellishments as well as visual characteristics, themes, and overall impressions. In addition to these descriptions, we assume that users provide palette queries by specifying zero or more colors via a color picker, enabling the expression of subtle and continuous color nuances. Existing vision-language foundation models often struggle to incorporate such descriptions and palettes. To address this, we propose NaiLIA, a multimodal retrieval method for nail design images, which comprehensively aligns with dense intent descriptions and palette queries during retrieval. Our approach introduces a relaxed loss based on confidence scores for unlabeled images that can align with the descriptions. To evaluate NaiLIA, we constructed a benchmark consisting of 10,625 images collected from people with diverse cultural backgrounds. The images were annotated with long and dense intent descriptions given by over 200 annotators. Experimental results demonstrate that NaiLIA outperforms standard methods.

### 🤖 AI 总结

**一句话总结**：NaiLIA提出一种同时利用“密集意图长文本描述+可选调色板颜色查询”的多模态检索方法，用于更精准地检索美甲设计图像。

**研究动机**：美甲需求描述往往包含多层次、细粒度且开放的元素/主题/质感等信息，并且用户还希望用连续细微的颜色选择表达偏好，现有视觉-语言基础模型难以有效融合这两类条件进行检索。

**核心方法**：方法在检索对齐时联合建模密集意图描述与调色板查询，并引入基于置信度的“松弛损失”(relaxed loss)，允许对未标注但可能匹配描述的图像进行软对齐以提升鲁棒性；同时构建包含10,625张图像与200+标注者长描述的基准用于评测。

**主要结论**：在所建多文化背景的美甲检索基准上，NaiLIA相较标准基线方法取得更优的检索性能，证明联合对齐长描述与调色板并用置信度松弛学习能有效提升检索效果。

**关键词**：多模态检索, 图文检索, 细粒度意图描述, 调色板查询, 连续色彩表示, 色彩条件检索, 视觉-语言模型, 置信度加权松弛损失, 弱监督对齐, 美甲设计图像检索, 美甲图像基准数据集

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05446v1) | [下载PDF](https://arxiv.org/pdf/2603.05446v1.pdf)

---

## [17. SAIL: Similarity-Aware Guidance and Inter-Caption Augmentation-based Learning for Weakly-Supervised Dense Video Captioning](https://arxiv.org/abs/2603.05437v1)

**作者**：Ye-Chan Kim, SeungJu Cha, Si-Woo Kim 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-05

### 📄 论文摘要

Weakly-Supervised Dense Video Captioning aims to localize and describe events in videos trained only on caption annotations, without temporal boundaries. Prior work introduced an implicit supervision paradigm based on Gaussian masking and complementary captioning. However, existing method focuses merely on generating non-overlapping masks without considering their semantic relationship to corresponding events, resulting in simplistic, uniformly distributed masks that fail to capture semantically meaningful regions. Moreover, relying solely on ground-truth captions leads to sub-optimal performance due to the inherent sparsity of existing datasets. In this work, we propose SAIL, which constructs semantically-aware masks through cross-modal alignment. Our similarity aware training objective guides masks to emphasize video regions with high similarity to their corresponding event captions. Furthermore, to guide more accurate mask generation under sparse annotation settings, we introduce an LLM-based augmentation strategy that generates synthetic captions to provide additional alignment signals. These synthetic captions are incorporated through an inter-mask mechanism, providing auxiliary guidance for precise temporal localization without degrading the main objective. Experiments on ActivityNet Captions and YouCook2 demonstrate state-of-the-art performance on both captioning and localization metrics.

### 🤖 AI 总结

**一句话总结**：SAIL通过相似度感知的跨模态对齐生成语义相关的时间掩码，并结合LLM生成的合成字幕增强弱监督密集视频描述的定位与描述效果。

**研究动机**：现有弱监督方法主要追求掩码不重叠，忽视掩码与事件语义的对应关系，导致掩码分布粗糙且难以覆盖关键语义片段；同时数据集字幕标注稀疏，仅依赖GT字幕会限制对齐监督与性能上限。

**核心方法**：提出相似度感知训练目标，通过视频-字幕相似度引导掩码强调与对应字幕更相关的时间区域，实现语义感知的掩码学习；再用LLM生成合成字幕，并通过inter-mask机制将其作为辅助对齐信号，提升稀疏标注下的掩码/定位精度且不干扰主学习目标。

**主要结论**：在ActivityNet Captions与YouCook2上，SAIL在字幕生成与事件时间定位指标上均达到SOTA，证明语义对齐掩码与LLM字幕增广能有效提升弱监督密集视频描述性能。

**关键词**：弱监督密集视频字幕, 事件时间定位, 跨模态对齐, 相似度引导训练, 语义感知掩码, 时间掩码生成, 隐式监督, 高斯掩码, LLM数据增强, 合成字幕生成

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

**一句话总结**：RelaxFlow提出一种无需训练的双分支框架，在严格保留可见观测的同时，用文本提示引导被遮挡区域的3D补全，实现“刚性观测控制 + 松弛结构控制”。

**研究动机**：单张图像到3D在遮挡下存在语义歧义，仅凭可见部分难以确定物体类别与不可见几何；因此需要文本来消歧并补全，但又必须不破坏输入观测的真实性。

**核心方法**：采用双分支解耦控制粒度：对观测使用严格约束，对文本提示通过“松弛机制”仅施加结构层面的引导，并用Multi-Prior Consensus Module融合多种先验达成一致；理论上证明松弛等价于对生成向量场施加低通滤波，抑制高频实例细节以突出可兼容观测的几何结构。

**主要结论**：在新提出的ExtremeOcc-3D与AmbiSem-3D诊断基准上，RelaxFlow能在不牺牲可见区域视觉保真度的前提下，使不可见区域生成更符合文本意图，尤其在强遮挡与高语义歧义场景表现突出。

**关键词**：文本驱动3D生成, 图像到3D生成, 遮挡语义歧义, 观测约束生成, 控制粒度解耦, 双分支框架, 多先验一致性, 生成向量场低通滤波, 3D遮挡诊断基准

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05425v1) | [下载PDF](https://arxiv.org/pdf/2603.05425v1.pdf)

---

## [19. MobileFetalCLIP: Selective Repulsive Knowledge Distillation for Mobile Fetal Ultrasound Analysis](https://arxiv.org/abs/2603.05421v1)

**作者**：Numan Saeed, Fadillah Adamsyah Maani, Mohammad Yaqub  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-03-05

### 📄 论文摘要

Fetal ultrasound AI could transform prenatal care in low-resource settings, yet current foundation models exceed 300M visual parameters, precluding deployment on point-of-care devices. Standard knowledge distillation fails under such extreme capacity gaps (~26x), as compact students waste capacity mimicking architectural artifacts of oversized teachers. We introduce Selective Repulsive Knowledge Distillation, which decomposes contrastive KD into diagonal and off-diagonal components: matched pair alignment is preserved while the off-diagonal weight decays into negative values, repelling the student from the teacher's inter-class confusions and forcing discovery of architecturally native features. Our 11.4M parameter student surpasses the 304M-parameter FetalCLIP teacher on zero-shot HC18 biometry validity (88.6% vs. 83.5%) and brain sub-plane F1 (0.784 vs. 0.702), while running at 1.6 ms on iPhone 16 Pro, enabling real-time assistive AI on handheld ultrasound devices. Our code, models, and app are publicly available at https://github.com/numanai/MobileFetalCLIP.

### 🤖 AI 总结

**一句话总结**：提出一种“选择性排斥”的对比式知识蒸馏方法，使11.4M轻量学生模型在胎儿超声零样本任务上超越304M教师并可在手机端实时运行。

**研究动机**：胎儿超声在低资源地区很有价值，但现有超声基础模型参数量巨大难以上线到便携设备；在约26倍容量差距下，传统蒸馏会让小模型浪费容量去拟合大模型的架构伪影与混淆。

**核心方法**：提出Selective Repulsive Knowledge Distillation，将对比蒸馏的logits分解为对角项与非对角项：保留匹配对（对角）对齐，同时让非对角权重衰减为负以“排斥”教师的类间混淆，促使学生学习更符合自身架构的判别特征。

**主要结论**：11.4M学生在HC18零样本生物测量有效性(88.6% vs 83.5%)与脑部子平面F1(0.784 vs 0.702)上超过304M教师，并在iPhone 16 Pro上约1.6ms推理，实现手持超声设备的实时辅助AI。

**关键词**：胎儿超声分析, 移动端推理, 边缘部署, 知识蒸馏, 选择性排斥蒸馏, 容量差距蒸馏, 零样本评测, 掌上超声设备, 实时医疗辅助

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05421v1) | [下载PDF](https://arxiv.org/pdf/2603.05421v1.pdf)

---

## [20. Video-based Locomotion Analysis for Fish Health Monitoring](https://arxiv.org/abs/2603.05407v1)

**作者**：Timon Palm, Clemens Seibold, Anna Hilsmann 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

Monitoring the health conditions of fish is essential, as it enables the early detection of disease, safeguards animal welfare, and contributes to sustainable aquaculture practices. Physiological and pathological conditions of cultivated fish can be inferred by analyzing locomotion activities. In this paper, we present a system that estimates the locomotion activities from videos using multi object tracking. The core of our approach is a YOLOv11 detector embedded in a tracking-by-detection framework. We investigate various configurations of the YOLOv11-architecture as well as extensions that incorporate multiple frames to improve detection accuracy. Our system is evaluated on a manually annotated dataset of Sulawesi ricefish recorded in a home-aquarium-like setup, demonstrating its ability to reliably measure swimming direction and speed for fish health monitoring. The dataset will be made publicly available upon publication.

### 🤖 AI 总结

**一句话总结**：本文提出一个基于YOLOv11与tracking-by-detection的多目标跟踪系统，从视频中估计鱼群游动方向与速度，用于鱼类健康监测。

**研究动机**：鱼类健康状况可通过运动行为变化提前反映，但人工观察成本高且主观。需要在接近真实养殖/家用水族环境中，用视觉自动化、可靠地量化鱼的运动指标以辅助早期预警。

**核心方法**：将YOLOv11检测器嵌入“检测-跟踪”(tracking-by-detection)框架进行多目标跟踪，并比较不同YOLOv11结构配置。进一步探索引入多帧信息的扩展以提升检测准确性，最终从轨迹中计算游动方向与速度等运动学特征。

**主要结论**：在人工标注的Sulawesi ricefish视频数据集上，系统能稳定地测量鱼的游动方向与速度，表明其可用于健康监测场景。作者同时计划在论文发表后公开该数据集以促进后续研究。

**关键词**：鱼类健康监测, 水产养殖, 视频行为分析, 游动运动分析, 多目标跟踪, 目标检测, 多帧时序建模, 游动速度估计, 游动方向估计, 人工标注数据集

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05407v1) | [下载PDF](https://arxiv.org/pdf/2603.05407v1.pdf)

---

## [21. Fusion-CAM: Integrating Gradient and Region-Based Class Activation Maps for Robust Visual Explanations](https://arxiv.org/abs/2603.05386v1)

**作者**：Hajar Dekdegue, Moncef Garouani, Josiane Mothe 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

Interpreting the decision-making process of deep convolutional neural networks remains a central challenge in achieving trustworthy and transparent artificial intelligence. Explainable AI (XAI) techniques, particularly Class Activation Map (CAM) methods, are widely adopted to visualize the input regions influencing model predictions. Gradient-based approaches (e.g. Grad-CAM) provide highly discriminative, fine-grained details by computing gradients of class activations but often yield noisy and incomplete maps that emphasize only the most salient regions rather than the complete objects. Region-based approaches (e.g. Score-CAM) aggregate information over larger areas, capturing broader object coverage at the cost of over-smoothing and reduced sensitivity to subtle features. We introduce Fusion-CAM, a novel framework that bridges this explanatory gap by unifying both paradigms through a dedicated fusion mechanism to produce robust and highly discriminative visual explanations. Our method first denoises gradient-based maps, yielding cleaner and more focused activations. It then combines the refined gradient map with region-based maps using contribution weights to enhance class coverage. Finally, we propose an adaptive similarity-based pixel-level fusion that evaluates the agreement between both paradigms and dynamically adjusts the fusion strength. This adaptive mechanism reinforces consistent activations while softly blending conflicting regions, resulting in richer, context-aware, and input-adaptive visual explanations. Extensive experiments on standard benchmarks show that Fusion-CAM consistently outperforms existing CAM variants in both qualitative visualization and quantitative evaluation, providing a robust and flexible tool for interpreting deep neural networks.

### 🤖 AI 总结

**一句话总结**：Fusion-CAM 通过融合梯度型与区域型 CAM，并用自适应像素级机制调节融合强度，生成更稳健且覆盖更完整的可解释热力图。

**研究动机**：梯度型 CAM（如 Grad-CAM）细粒度但易噪声且只突出最显著区域，区域型 CAM（如 Score-CAM）覆盖更广却过度平滑、对细微特征不敏感；需要一种同时兼顾“判别性”和“完整性”的统一解释框架。

**核心方法**：先对梯度 CAM 进行去噪得到更干净的激活图，再用贡献权重将其与区域 CAM 融合以增强目标覆盖；进一步提出基于相似度的自适应像素级融合，按两类图的一致性动态强化一致区域并柔性混合冲突区域。

**主要结论**：在标准基准上的定性与定量评测表明，Fusion-CAM 相比现有 CAM 变体能更稳定地提供更清晰、更具判别性且对象覆盖更完整的视觉解释，作为通用解释工具更鲁棒且更灵活。

**关键词**：可解释AI, 视觉解释, 类激活图（CAM）, 梯度-区域融合, 梯度图去噪, 像素级融合, 自适应相似度加权, 目标覆盖增强, 卷积神经网络可解释性

**评分**：15

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05386v1) | [下载PDF](https://arxiv.org/pdf/2603.05386v1.pdf)

---

## [22. ORMOT: A Dataset and Framework for Omnidirectional Referring Multi-Object Tracking](https://arxiv.org/abs/2603.05384v1)

**作者**：Sijia Chen, Zihan Zhou, Yanqiu Yu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-05

### 📄 论文摘要

Multi-Object Tracking (MOT) is a fundamental task in computer vision, aiming to track targets across video frames. Existing MOT methods perform well in general visual scenes, but face significant challenges and limitations when extended to visual-language settings. To bridge this gap, the task of Referring Multi-Object Tracking (RMOT) has recently been proposed, which aims to track objects that correspond to language descriptions. However, current RMOT methods are primarily developed on datasets captured by conventional cameras, which suffer from limited field of view. This constraint often causes targets to move out of the frame, leading to fragmented tracking and loss of contextual information. In this work, we propose a novel task, called Omnidirectional Referring Multi-Object Tracking (ORMOT), which extends RMOT to omnidirectional imagery, aiming to overcome the field-of-view (FoV) limitation of conventional datasets and improve the model's ability to understand long-horizon language descriptions. To advance the ORMOT task, we construct ORSet, an Omnidirectional Referring Multi-Object Tracking dataset, which contains 27 diverse omnidirectional scenes, 848 language descriptions, and 3,401 annotated objects, providing rich visual, temporal, and language information. Furthermore, we propose ORTrack, a Large Vision-Language Model (LVLM)-driven framework tailored for Omnidirectional Referring Multi-Object Tracking. Extensive experiments on the ORSet dataset demonstrate the effectiveness of our ORTrack framework. The dataset and code will be open-sourced at https://github.com/chen-si-jia/ORMOT.

### 🤖 AI 总结

**一句话总结**：提出全景（omnidirectional）指代表达多目标跟踪新任务ORMOT，并发布ORSet数据集与LVLM驱动的ORTrack框架以提升长时序语言条件跟踪能力。

**研究动机**：现有RMOT多基于常规相机数据，视场角有限导致目标频繁出画、轨迹断裂且上下文缺失，限制了对长跨度语言描述的理解与跟踪。

**核心方法**：构建ORSet全景RMOT数据集（27个场景、848条描述、3401个标注对象）提供更完整的时空上下文；提出ORTrack框架，利用大视觉语言模型在全景图像中进行语言条件的多目标关联与跟踪。

**主要结论**：在ORSet上的实验表明ORTrack在全景指代多目标跟踪上有效，说明扩大FoV与引入LVLM有助于减少出画带来的跟踪碎片化并增强长时序语言理解；数据与代码将开源。

**关键词**：全景视觉, 全向图像, 多目标跟踪, 指代表达跟踪, 视觉语言跟踪, 长时序跟踪, 视野限制, 大视觉语言模型, 视频目标注释

**评分**：29

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

**一句话总结**：POET-X 通过更高效的正交等价变换重参数化训练，在保持 POET 稳定性与泛化优势的同时显著降低显存与计算开销，使单卡 H100 也能预训练十亿参数级 LLM。

**研究动机**：原始 POET 虽能提升训练稳定性，但因频繁的大规模矩阵乘法带来高显存占用与计算负担，限制了其在大模型训练中的可扩展性。

**核心方法**：提出 POET-X，将每个权重矩阵的优化仍置于“正交等价变换/谱保持”的框架下，但通过可扩展的实现方式大幅减少正交变换相关的计算与中间激活/状态的内存开销，从而提升吞吐与显存效率。

**主要结论**：实验表明 POET-X 在不牺牲 POET 的稳定性和泛化表现的前提下显著提升训练效率与显存利用率；在相同设置下可在单张 Nvidia H100 上预训练十亿参数 LLM，而 AdamW 等标准优化器会因显存不足失败。

**关键词**：内存高效训练, 正交等价变换, 正交变换参数化, 谱保持优化, 训练稳定性, 矩阵乘法开销降低, 吞吐量提升, 单卡预训练, 大模型优化器

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05500v1) | [下载PDF](https://arxiv.org/pdf/2603.05500v1.pdf)

---

## [24. Cheap Thrills: Effective Amortized Optimization Using Inexpensive Labels](https://arxiv.org/abs/2603.05495v1)

**作者**：Khai Nguyen, Petros Ellinas, Anvita Bhagavathula 等 4 位作者  
**分类**：cs.LG, math.OC  
**发布时间**：2026-03-05

### 📄 论文摘要

To scale the solution of optimization and simulation problems, prior work has explored machine-learning surrogates that inexpensively map problem parameters to corresponding solutions. Commonly used approaches, including supervised and self-supervised learning with either soft or hard feasibility enforcement, face inherent challenges such as reliance on expensive, high-quality labels or difficult optimization landscapes. To address their trade-offs, we propose a novel framework that first collects "cheap" imperfect labels, then performs supervised pretraining, and finally refines the model through self-supervised learning to improve overall performance. Our theoretical analysis and merit-based criterion show that labeled data need only place the model within a basin of attraction, confirming that only modest numbers of inexact labels and training epochs are required. We empirically validate our simple three-stage strategy across challenging domains, including nonconvex constrained optimization, power-grid operation, and stiff dynamical systems, and show that it yields faster convergence; improved accuracy, feasibility, and optimality; and up to 59x reductions in total offline cost.

### 🤖 AI 总结

**一句话总结**：提出“廉价不完美标签+监督预训练+自监督精炼”的三阶段摊还优化框架，用少量低成本标签即可显著降低离线训练成本并提升解的质量与可行性。

**研究动机**：现有摊还优化/仿真替代模型要么依赖昂贵高质量标签，要么纯自监督训练优化地形困难、收敛慢且易陷入差解；需要一种同时兼顾成本与效果的折中方案。

**核心方法**：先采集“便宜但有误差”的标签进行监督预训练，把模型推入合适的吸引域（basin of attraction），再用自监督目标在无标签/低标签下继续优化以提升精度、可行性与最优性；并给出理论分析与基于“merit”的判据说明只需少量不精确标签与训练轮次。

**主要结论**：理论与实验表明，只要廉价标签能把模型初始化到可优化区域，后续自监督即可有效精炼；在非凸约束优化、电网运行和刚性动力系统等任务上实现更快收敛、更好精度/可行性/最优性，并将总离线成本最高降低59倍。

**关键词**：摊销优化, 廉价标签, 不完美标注, 监督预训练, 自监督微调, 代理模型, 可行性约束, 非凸约束优化, 吸引域, 功率电网调度, 刚性动力系统, 离线训练成本

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05495v1) | [下载PDF](https://arxiv.org/pdf/2603.05495v1.pdf)

---

## [25. Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation](https://arxiv.org/abs/2603.05494v1)

**作者**：Helena Casademunt, Bartosz Cywiński, Khoi Tran 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-03-05

### 📄 论文摘要

Large language models sometimes produce false or misleading responses. Two approaches to this problem are honesty elicitation -- modifying prompts or weights so that the model answers truthfully -- and lie detection -- classifying whether a given response is false. Prior work evaluates such methods on models specifically trained to lie or conceal information, but these artificial constructions may not resemble naturally-occurring dishonesty. We instead study open-weights LLMs from Chinese developers, which are trained to censor politically sensitive topics: Qwen3 models frequently produce falsehoods about subjects like Falun Gong or the Tiananmen protests while occasionally answering correctly, indicating they possess knowledge they are trained to suppress. Using this as a testbed, we evaluate a suite of elicitation and lie detection techniques. For honesty elicitation, sampling without a chat template, few-shot prompting, and fine-tuning on generic honesty data most reliably increase truthful responses. For lie detection, prompting the censored model to classify its own responses performs near an uncensored-model upper bound, and linear probes trained on unrelated data offer a cheaper alternative. The strongest honesty elicitation techniques also transfer to frontier open-weights models including DeepSeek R1. Notably, no technique fully eliminates false responses. We release all prompts, code, and transcripts.

### 🤖 AI 总结

**一句话总结**：将中文开发者训练出的“审查型”开源LLM作为天然“隐秘知识压制”测试床，系统评估诚实诱导与谎言检测方法，发现多种手段可提升真实回答但无法彻底消除虚假输出。

**研究动机**：以往诚实诱导/谎言检测常在“被刻意训练去说谎”的模型上评测，可能不符合真实世界的自然不诚实情形。作者利用对敏感政治话题进行审查训练的模型（既会说假话也偶尔说真话）来更贴近现实地研究如何挖掘被压制的真实知识。

**核心方法**：选取Qwen3等审查型开源模型，在敏感主题上构建评测并对比多种诚实诱导策略（如去掉聊天模板的采样、few-shot提示、用通用诚实数据微调）。同时评估谎言检测方法（让模型自我判别其回答真伪、以及用无关数据训练的线性探针），并测试方法向DeepSeek R1等前沿开源模型的迁移。

**主要结论**：诚实诱导方面，“不使用chat模板采样”、few-shot与通用诚实数据微调最稳定地提高真实回答比例，但仍无法完全杜绝虚假输出。谎言检测方面，让被审查模型自评真伪接近“未审查模型上限”，线性探针提供更低成本替代；强诱导技巧对更强开源模型也具有一定可迁移性。

**关键词**：秘密知识引出, 诚实引出, 谎言检测, 政治内容审查, 开放权重模型, 提示工程, 少样本提示, 无聊天模板采样, 诚实数据微调, 线性探针

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05494v1) | [下载PDF](https://arxiv.org/pdf/2603.05494v1.pdf)

---

## [26. SurvHTE-Bench: A Benchmark for Heterogeneous Treatment Effect Estimation in Survival Analysis](https://arxiv.org/abs/2603.05483v1)

**作者**：Shahriar Noroozizadeh, Xiaobin Shen, Jeremy C. Weiss 等 4 位作者  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-03-05

### 📄 论文摘要

Estimating heterogeneous treatment effects (HTEs) from right-censored survival data is critical in high-stakes applications such as precision medicine and individualized policy-making. Yet, the survival analysis setting poses unique challenges for HTE estimation due to censoring, unobserved counterfactuals, and complex identification assumptions. Despite recent advances, from Causal Survival Forests to survival meta-learners and outcome imputation approaches, evaluation practices remain fragmented and inconsistent. We introduce SurvHTE-Bench, the first comprehensive benchmark for HTE estimation with censored outcomes. The benchmark spans (i) a modular suite of synthetic datasets with known ground truth, systematically varying causal assumptions and survival dynamics, (ii) semi-synthetic datasets that pair real-world covariates with simulated treatments and outcomes, and (iii) real-world datasets from a twin study (with known ground truth) and from an HIV clinical trial. Across synthetic, semi-synthetic, and real-world settings, we provide the first rigorous comparison of survival HTE methods under diverse conditions and realistic assumption violations. SurvHTE-Bench establishes a foundation for fair, reproducible, and extensible evaluation of causal survival methods. The data and code of our benchmark are available at: https://github.com/Shahriarnz14/SurvHTE-Bench .

### 🤖 AI 总结

**一句话总结**：提出SurvHTE-Bench，一个面向右删失生存数据的异质性处理效应（HTE）估计综合基准，用于公平、可复现地比较不同因果生存方法。

**研究动机**：生存分析中的HTE估计受删失、反事实不可观测与复杂识别假设影响，现有方法评估分散且缺乏统一标准。需要一个覆盖多种假设与违背情形的基准来进行一致、严格的对比评测。

**核心方法**：构建包含三类数据的基准：具备真实HTE地面真值且可系统控制因果假设/生存动力学的合成数据、用真实协变量配合模拟处理与结局的半合成数据、以及来自双生子研究（有真值）和HIV临床试验的真实数据；并在这些设置下统一评测多类生存HTE方法（如Causal Survival Forest、survival meta-learners与结局插补类方法）。

**主要结论**：在合成、半合成与真实场景及多种现实假设违背条件下给出首次系统、严格的生存HTE方法对比，揭示方法性能对数据机制与假设偏离的敏感性。SurvHTE-Bench为后续因果生存方法的公平评测与可扩展复现实验提供了基础设施（并开源数据与代码）。

**关键词**：生存分析, 异质性治疗效应（HTE）, 右删失数据, 因果推断, 因果生存模型, HTE评测基准, 合成数据集, 半合成数据集, 反事实估计, 因果识别假设, 生存元学习器

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05483v1) | [下载PDF](https://arxiv.org/pdf/2603.05483v1.pdf)

---

## [27. Kraus Constrained Sequence Learning For Quantum Trajectories from Continuous Measurement](https://arxiv.org/abs/2603.05468v1)

**作者**：Priyanshi Singh, Krishna Bhatia  
**分类**：cs.LG  
**发布时间**：2026-03-05

### 📄 论文摘要

Real-time reconstruction of conditional quantum states from continuous measurement records is a fundamental requirement for quantum feedback control, yet standard stochastic master equation (SME) solvers require exact model specification, known system parameters, and are sensitive to parameter mismatch. While neural sequence models can fit these stochastic dynamics, the unconstrained predictors can violate physicality such as positivity or trace constraints, leading to unstable rollouts and unphysical estimates. We propose a Kraus-structured output layer that converts the hidden representation of a generic sequence backbone into a completely positive trace preserving (CPTP) quantum operation, yielding physically valid state updates by construction. We instantiate this layer across diverse backbones, RNN, GRU, LSTM, TCN, ESN and Mamba; including Neural ODE as a comparative baseline, on stochastic trajectories characterized by parameter drift. Our evaluation reveals distinct trade-offs between gating mechanisms, linear recurrence, and global attention. Across all models, Kraus-LSTM achieves the strongest results, improving state estimation quality by 7% over its unconstrained counterpart while guaranteeing physically valid predictions in non-stationary regimes.

### 🤖 AI 总结

**一句话总结**：提出一种Kraus结构化输出层，将序列模型的预测强制为CPTP量子操作，从而在连续测量量子轨迹重建中保证物理合法性并提升非平稳场景下的状态估计性能。

**研究动机**：传统SME求解器依赖精确模型与参数且对失配敏感；而普通神经序列模型虽能拟合随机动力学，却可能输出不满足正定/迹守恒的量子态，导致滚动预测不稳定与非物理结果。

**核心方法**：在任意序列骨干网络（RNN/GRU/LSTM/TCN/ESN/Mamba等）后接入Kraus约束输出层，将隐藏表示映射为Kraus算子并构造完全正且迹保持（CPTP）的量子通道，实现“按构造”合法的状态更新；并在存在参数漂移的随机轨迹上与无约束版本及Neural ODE等基线对比评测。

**主要结论**：Kraus约束在所有骨干上都能保证预测量子态物理有效并改善非平稳条件下的稳定性；其中Kraus-LSTM综合表现最佳，相比无约束LSTM将状态估计质量提升约7%。

**关键词**：连续量子测量, 量子轨迹重建, 量子反馈控制, 随机主方程（SME）, 序列建模, 物理约束学习, 量子态估计, 参数漂移（非平稳）

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05468v1) | [下载PDF](https://arxiv.org/pdf/2603.05468v1.pdf)

---

## [28. Latent Wasserstein Adversarial Imitation Learning](https://arxiv.org/abs/2603.05440v1)

**作者**：Siqi Yang, Kai Yan, Alexander G. Schwing 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-05

### 📄 论文摘要

Imitation Learning (IL) enables agents to mimic expert behavior by learning from demonstrations. However, traditional IL methods require large amounts of medium-to-high-quality demonstrations as well as actions of expert demonstrations, both of which are often unavailable. To reduce this need, we propose Latent Wasserstein Adversarial Imitation Learning (LWAIL), a novel adversarial imitation learning framework that focuses on state-only distribution matching. It benefits from the Wasserstein distance computed in a dynamics-aware latent space. This dynamics-aware latent space differs from prior work and is obtained via a pre-training stage, where we train the Intention Conditioned Value Function (ICVF) to capture a dynamics-aware structure of the state space using a small set of randomly generated state-only data. We show that this enhances the policy's understanding of state transitions, enabling the learning process to use only one or a few state-only expert episodes to achieve expert-level performance. Through experiments on multiple MuJoCo environments, we demonstrate that our method outperforms prior Wasserstein-based IL methods and prior adversarial IL methods, achieving better results across various tasks.

### 🤖 AI 总结

**一句话总结**：LWAIL通过在“动力学感知”的潜在空间里用Wasserstein距离做对抗式状态分布匹配，仅需极少量（甚至一条）纯状态专家轨迹即可实现接近专家的模仿效果。

**研究动机**：现有模仿学习往往需要大量中高质量示范且通常依赖专家动作信息，但现实中示范数量与动作标注常常不足；因此需要一种能用少量“仅状态”示范也能学好的方法。

**核心方法**：先用少量随机生成的仅状态数据预训练意图条件价值函数（ICVF），构建包含环境动力学结构的潜在表示；再在该潜在空间中用Wasserstein距离进行对抗式模仿学习，实现仅基于状态的分布对齐与策略学习。

**主要结论**：在多个MuJoCo任务中，LWAIL相较于以往Wasserstein类IL与对抗式IL方法取得更优表现，并在极少量状态示范条件下仍能达到专家级性能，验证了动力学感知潜在空间对样本效率与稳定性的提升作用。

**关键词**：模仿学习, 仅状态示范, 分布匹配, 潜在空间对齐, 动力学感知表示, 预训练表示学习, 意图条件价值函数（ICVF）, 少样本强化学习

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05440v1) | [下载PDF](https://arxiv.org/pdf/2603.05440v1.pdf)

---

## [29. An interpretable prototype parts-based neural network for medical tabular data](https://arxiv.org/abs/2603.05423v1)

**作者**：Jacek Karolczak, Jerzy Stefanowski  
**分类**：cs.LG  
**发布时间**：2026-03-05

### 📄 论文摘要

The ability to interpret machine learning model decisions is critical in such domains as healthcare, where trust in model predictions is as important as their accuracy. Inspired by the development of prototype parts-based deep neural networks in computer vision, we propose a new model for tabular data, specifically tailored to medical records, that requires discretization of diagnostic result norms. Unlike the original vision models that rely on the spatial structure, our method employs trainable patching over features describing a patient, to learn meaningful prototypical parts from structured data. These parts are represented as binary or discretized feature subsets. This allows the model to express prototypes in human-readable terms, enabling alignment with clinical language and case-based reasoning. Our proposed neural network is inherently interpretable and offers interpretable concept-based predictions by comparing the patient's description to learned prototypes in the latent space of the network. In experiments, we demonstrate that the model achieves classification performance competitive to widely used baseline models on medical benchmark datasets, while also offering transparency, bridging the gap between predictive performance and interpretability in clinical decision support.

### 🤖 AI 总结

**一句话总结**：提出一种面向医疗表格数据的可解释“原型-部件”神经网络，通过学习可读的特征子集原型实现透明预测且性能具竞争力。

**研究动机**：医疗场景不仅需要高准确率，还要求模型决策可解释、可与临床语言对齐以建立信任与支持案例推理。现有原型网络多依赖图像空间结构，难以直接迁移到表格病历数据。

**核心方法**：对诊断指标进行离散化/二值化，并在特征维度上引入可训练的“patching”来形成患者特征子集的部件表示；模型在潜空间中将样本与学习到的原型部件进行相似度比较，输出基于概念/原型的可解释预测。

**主要结论**：在医疗基准数据集上，该方法分类效果与常用基线模型相当，同时能给出人类可读的原型部件解释，从而在临床决策支持中缩小性能与可解释性的差距。

**关键词**：模型可解释性, 医疗表格数据, 原型网络, 部件原型, 可训练特征分块, 特征离散化, 二值特征子集, 概念级预测, 病例推理, 潜空间相似度

**评分**：16

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05423v1) | [下载PDF](https://arxiv.org/pdf/2603.05423v1.pdf)

---

## [30. On the Necessity of Learnable Sheaf Laplacians](https://arxiv.org/abs/2603.05395v1)

**作者**：Ferran Hernandez Caralt, Mar Gonzàlez i Català, Adrián Bazaga 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-05

### 📄 论文摘要

Sheaf Neural Networks (SNNs) were introduced as an extension of Graph Convolutional Networks to address oversmoothing on heterophilous graphs by attaching a sheaf to the input graph and replacing the adjacency-based operator with a sheaf Laplacian defined by (learnable) restriction maps. Prior work motivates this design through theoretical properties of sheaf diffusion and the kernel of the sheaf Laplacian, suggesting that suitable non-identity restriction maps can avoid representations converging to constants across connected components. Since oversmoothing can also be mitigated through residual connections and normalization, we revisit a trivial sheaf construction to ask whether the additional complexity of learning restriction maps is necessary. We introduce an Identity Sheaf Network baseline, where all restriction maps are fixed to the identity, and use it to ablate the empirical improvements reported by sheaf-learning architectures. Across five popular heterophilic benchmarks, the identity baseline achieves comparable performance to a range of SNN variants. Finally, we introduce the Rayleigh quotient as a normalized measure for comparing oversmoothing across models and show that, in trained networks, the behavior predicted by the diffusion-based analysis of SNNs is not reflected empirically. In particular, Identity Sheaf Networks do not appear to suffer more significant oversmoothing than their SNN counterparts.

### 🤖 AI 总结

**一句话总结**：论文表明在多种异配图基准上，将SNN中的限制映射固定为恒等（Identity Sheaf）也能达到与可学习sheaf Laplacian相近的效果，可学习限制映射的必要性存疑。

**研究动机**：既有SNN工作用“可学习限制映射可缓解过平滑”的理论动机支持其复杂设计，但过平滑也可能被残差与归一化等常规技巧缓解，因此作者质疑学习限制映射是否真是性能提升的关键来源。

**核心方法**：提出Identity Sheaf Network基线：将所有restriction maps固定为identity，用于系统消融比较多种SNN变体在五个异配图基准上的表现；同时引入Rayleigh quotient作为归一化指标，用于跨模型比较训练后网络的过平滑程度。

**主要结论**：实验显示Identity基线与多种学习型SNN性能相当；且以Rayleigh quotient衡量时，训练后的网络并未呈现扩散理论所预测的差异，Identity Sheaf Networks也没有更明显的过平滑现象。

**关键词**：层叠神经网络, 层叠拉普拉斯算子, 可学习限制映射, 恒等层叠网络, 过平滑, 异配图, 图神经网络, 消融实验, 扩散分析, 异配基准

**评分**：12

**论文链接**：[查看原文](https://arxiv.org/abs/2603.05395v1) | [下载PDF](https://arxiv.org/pdf/2603.05395v1.pdf)

---

