# arXiv AI 论文日报 | 2026-03-26

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (10 篇)
- [cs.CV](#csCV) (13 篇)
- [cs.AI](#csAI) (2 篇)
- [cs.CL](#csCL) (5 篇)

---

## cs.AI

## [1. The Stochastic Gap: A Markovian Framework for Pre-Deployment Reliability and Oversight-Cost Auditing in Agentic Artificial Intelligence](https://arxiv.org/abs/2603.24582v1)

**作者**：Biplab Pal, Santanu Bhattacharya  
**分类**：cs.AI  
**发布时间**：2026-03-25

### 📄 论文摘要

Agentic artificial intelligence (AI) in organizations is a sequential decision problem constrained by reliability and oversight cost. When deterministic workflows are replaced by stochastic policies over actions and tool calls, the key question is not whether a next step appears plausible, but whether the resulting trajectory remains statistically supported, locally unambiguous, and economically governable. We develop a measure-theoretic Markov framework for this setting. The core quantities are state blind-spot mass B_n(tau), state-action blind mass B^SA_{pi,n}(tau), an entropy-based human-in-the-loop escalation gate, and an expected oversight-cost identity over the workflow visitation measure.   We instantiate the framework on the Business Process Intelligence Challenge 2019 purchase-to-pay log (251,734 cases, 1,595,923 events, 42 distinct workflow actions) and construct a log-driven simulated agent from a chronological 80/20 split of the same process. The main empirical finding is that a large workflow can appear well supported at the state level while retaining substantial blind mass over next-step decisions: refining the operational state to include case context, economic magnitude, and actor class expands the state space from 42 to 668 and raises state-action blind mass from 0.0165 at tau=50 to 0.1253 at tau=1000. On the held-out split, m(s) = max_a pi-hat(a|s) tracks realized autonomous step accuracy within 3.4 percentage points on average.   The same quantities that delimit statistically credible autonomy also determine expected oversight burden. The framework is demonstrated on a large-scale enterprise procurement workflow and is designed for direct application to engineering processes for which operational event logs are available.

### 🤖 AI 总结

**一句话总结**：论文提出一个基于测度论与马尔可夫过程的审计框架，用“盲区质量/盲质量”和熵门控来量化企业级Agent工作流在部署前的可靠性边界与人工监督成本。

**研究动机**：组织中的Agentic AI将确定性流程替换为随机策略后，风险不在单步是否“看起来合理”，而在整段轨迹是否有足够统计支持、是否会出现局部歧义，以及在可控的监督成本下能否治理。

**核心方法**：构建马尔可夫框架并定义状态盲区质量B_n(τ)、状态-动作盲质量B^SA_{π,n}(τ)，结合基于熵的人在回路升级（escalation）门控，以及基于访问测度的期望监督成本恒等式来统一评估可信自治与监督负担。

**主要结论**：在BPIC 2019采购到付款日志上验证发现：即使状态层面看似“覆盖良好”，细化状态后状态-动作盲质量会显著上升（从0.0165@τ=50到0.1253@τ=1000），表明下一步决策仍存在大量统计盲区；同时m(s)=max_a π̂(a|s)能在测试集上较好预测自治步骤准确率（平均误差约3.4个百分点），且这些盲质量/门控量也直接决定预期监督成本。

**关键词**：马尔可夫决策框架, 度量论建模, 随机策略审计, 工作流轨迹可靠性, 状态-动作盲区质量, 盲点质量, 人类在环升级门控, 监督成本审计, 访问测度, 事件日志驱动仿真, 流程挖掘, 企业采购流程

**评分**：46

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24582v1) | [下载PDF](https://arxiv.org/pdf/2603.24582v1.pdf)

---

## [2. From Liar Paradox to Incongruent Sets: A Normal Form for Self-Reference](https://arxiv.org/abs/2603.24527v1)

**作者**：Shalender Singh, Vishnu Priya Singh Parmar  
**分类**：cs.AI  
**发布时间**：2026-03-25

### 📄 论文摘要

We introduce incongruent normal form (INF), a structural representation for self-referential semantic sentences. An INF replaces a self-referential sentence with a finite family of non-self-referential sentences that are individually satisfiable but not jointly satisfiable. This transformation isolates the semantic obstruction created by self-reference while preserving classical semantics locally and is accompanied by correctness theorems characterizing when global inconsistency arises from locally compatible commitments. We then study the role of incongruence as a structural source of semantic informativeness. Using a minimal model-theoretic notion of informativeness-understood as the ability of sentences to distinguish among admissible models-we show that semantic completeness precludes informativeness, while incongruence preserves it. Moreover, incongruence is not confined to paradoxical constructions: any consistent incomplete first-order theory admits finite incongruent families arising from incompatible complete extensions. In this sense, incompleteness manifests structurally as locally realizable but globally incompatible semantic commitments, providing a minimal formal basis for semantic knowledge. Finally, we introduce a quantitative semantic framework. In a canonical finite semantic-state setting, we model semantic commitments as Boolean functions and define a Fourier-analytic notion of semantic energy based on total influence. We derive uncertainty-style bounds relating semantic determinacy, informativeness, and spectral simplicity, and establish a matrix inequality bounding aggregate semantic variance by total semantic energy. These results show quantitatively that semantic informativeness cannot collapse into a single determinate state without unbounded energy cost, identifying incongruence as a fundamental structural and quantitative feature of semantic representation.

### 🤖 AI 总结

**一句话总结**：论文提出“非相容正规形”(INF)把自指语句转化为一组“各自可满足但整体不可满足”的非自指语句族，从结构与定量两个层面解释语义悖论、信息性与不完备性的根源。

**研究动机**：自指语句（如说谎者悖论）会在经典语义下引发全局不一致，但这种“不一致”如何由局部看似合理的语义承诺产生、以及它与语义信息性之间的关系缺乏统一的结构刻画与度量框架。

**核心方法**：构造INF：用有限个非自指句替换自指句，并给出正确性定理刻画何时由“局部可满足”导出“全局不可满足”；进一步用模型论中“区分可采纳模型”的最小信息性定义分析完备性/非相容性，并在有限语义状态下把语义承诺表示为布尔函数，引入基于总影响（傅里叶分析）的“语义能量”，推导不确定性式界与矩阵不等式。

**主要结论**：自指造成的语义阻碍可被INF精准隔离：局部保持经典语义但整体必然冲突；语义完备性会消解信息性，而非相容结构能保留信息性，且任意一致但不完备的一阶理论都存在源于不相容完备扩展的有限非相容族；在定量上，想把信息性压缩成单一确定语义状态需要无界能量代价，因而非相容性是语义表示的基础性结构与定量特征。

**关键词**：说谎者悖论, 不相容正规形（INF）, 局部可满足-全局不可满足, 语义不一致性, 模型论信息性, 语义完备性, 一阶理论不完备性, 不相容完备扩张, 语义承诺, 布尔函数语义, 总影响（傅里叶分析）

**评分**：11

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24527v1) | [下载PDF](https://arxiv.org/pdf/2603.24527v1.pdf)

---

## cs.CL

## [3. Retrieval Improvements Do Not Guarantee Better Answers: A Study of RAG for AI Policy QA](https://arxiv.org/abs/2603.24580v1)

**作者**：Saahil Mathur, Ryan David Rittner, Vedant Ajit Thakur 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.CY, cs.IR, cs.LG  
**发布时间**：2026-03-25

### 📄 论文摘要

Retrieval-augmented generation (RAG) systems are increasingly used to analyze complex policy documents, but achieving sufficient reliability for expert usage remains challenging in domains characterized by dense legal language and evolving, overlapping regulatory frameworks. We study the application of RAG to AI governance and policy analysis using the AI Governance and Regulatory Archive (AGORA) corpus, a curated collection of 947 AI policy documents. Our system combines a ColBERT-based retriever fine-tuned with contrastive learning and a generator aligned to human preferences using Direct Preference Optimization (DPO). We construct synthetic queries and collect pairwise preferences to adapt the system to the policy domain. Through experiments evaluating retrieval quality, answer relevance, and faithfulness, we find that domain-specific fine-tuning improves retrieval metrics but does not consistently improve end-to-end question answering performance. In some cases, stronger retrieval counterintuitively leads to more confident hallucinations when relevant documents are absent from the corpus. These results highlight a key concern for those building policy-focused RAG systems: improvements to individual components do not necessarily translate to more reliable answers. Our findings provide practical insights for designing grounded question-answering systems over dynamic regulatory corpora.

### 🤖 AI 总结

**一句话总结**：在AI政策问答场景中，检索组件即使显著变强，也不一定带来更好的端到端答案质量，甚至可能在缺少相关证据时诱发更“自信”的幻觉。

**研究动机**：政策/法规文本语言密集且不断演化，RAG虽被用于提升可追溯性与可靠性，但在专家级使用要求下仍容易出现不相关或不忠实回答，需要系统性评估“检索改进是否等于答案改进”。

**核心方法**：基于AGORA（947篇AI政策文档）构建RAG：使用对比学习微调的ColBERT检索器，并用DPO对生成器进行偏好对齐；通过合成查询与成对偏好数据进行领域适配，并分别评测检索质量、答案相关性与忠实性来检验端到端效果。

**主要结论**：领域微调能提升检索指标，但对问答整体表现提升不稳定；当语料库缺乏真正相关文档时，更强的检索可能反而导致模型输出更自信的幻觉，表明组件级优化不能保证系统级可靠性。

**关键词**：检索增强生成（RAG）, 政策问答, AI治理, 监管语料库, 直接偏好优化（DPO）, 合成查询生成, 成对偏好标注, 答案忠实性评测, 幻觉风险

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24580v1) | [下载PDF](https://arxiv.org/pdf/2603.24580v1.pdf)

---

## [4. MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination](https://arxiv.org/abs/2603.24579v1)

**作者**：Zhuo Li, Yupeng Zhang, Pengyu Cheng 等 11 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-25

### 📄 论文摘要

Hallucination remains a critical bottleneck for large language models (LLMs), undermining their reliability in real-world applications, especially in Retrieval-Augmented Generation (RAG) systems. While existing hallucination detection methods employ LLM-as-a-judge to verify LLM outputs against retrieved evidence, they suffer from inherent confirmation bias, where the verifier inadvertently reproduces the errors of the original generation. To address this, we introduce Multi-Agent Reinforced Self-Check for Hallucination (MARCH), a framework that enforces rigorous factual alignment by leveraging deliberate information asymmetry. MARCH orchestrates a collaborative pipeline of three specialized agents: a Solver, a Proposer, and a Checker. The Solver generates an initial RAG response, which the Proposer decomposes into claim-level verifiable atomic propositions. Crucially, the Checker validates these propositions against retrieved evidence in isolation, deprived of the Solver's original output. This well-crafted information asymmetry scheme breaks the cycle of self-confirmation bias. By training this pipeline with multi-agent reinforcement learning (MARL), we enable the agents to co-evolve and optimize factual adherence. Extensive experiments across hallucination benchmarks demonstrate that MARCH substantially reduces hallucination rates. Notably, an 8B-parameter LLM equipped with MARCH achieves performance competitive with powerful closed-source models. MARCH paves a scalable path for factual self-improvement of LLMs through co-evolution. The code is at https://github.com/Qwen-Applications/MARCH.

### 🤖 AI 总结

**一句话总结**：MARCH 通过“生成-拆解-隔离核查”的多智能体协作与强化学习训练，在RAG场景下显著降低LLM幻觉并提升事实一致性。

**研究动机**：现有LLM-as-a-judge式幻觉检测容易产生确认偏差：验证模型在看到原答案后会沿用其错误，导致难以真正纠错。论文希望在不依赖更强闭源模型的情况下，系统性提升LLM对证据的事实对齐能力。

**核心方法**：构建三智能体流水线：Solver 生成初始RAG回答，Proposer 将回答分解为可核验的原子命题，Checker 在“看不到原回答”的信息不对称条件下仅依据检索证据逐条验证，从机制上打破自我确认偏差。随后用多智能体强化学习（MARL）联合训练三者，使其协同进化并优化事实遵循与幻觉率指标。

**主要结论**：在多种幻觉评测基准上，MARCH 显著降低幻觉发生率并提升证据一致性；引入信息不对称的核查能有效缓解确认偏差。配备MARCH的8B级模型可达到与强闭源模型相近的效果，表明其具备可扩展的“自我改进事实性”路径。

**关键词**：LLM 幻觉抑制, RAG 事实一致性, 基于证据验证, 确认偏差, 多智能体框架, 信息不对称, 原子命题分解, 声明级事实核查, 多智能体强化学习, 自检机制

**评分**：50

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24579v1) | [下载PDF](https://arxiv.org/pdf/2603.24579v1.pdf)

---

## [5. A Sociolinguistic Analysis of Automatic Speech Recognition Bias in Newcastle English](https://arxiv.org/abs/2603.24549v1)

**作者**：Dana Serditova, Kevin Tang  
**分类**：cs.CL, cs.AI, cs.CV, cs.SD  
**发布时间**：2026-03-25

### 📄 论文摘要

Automatic Speech Recognition (ASR) systems are widely used in everyday communication, education, healthcare, and industry, yet their performance remains uneven across speakers, particularly when dialectal variation diverges from the mainstream accents represented in training data. This study investigates ASR bias through a sociolinguistic analysis of Newcastle English, a regional variety of North-East England that has been shown to challenge current speech recognition technologies. Using spontaneous speech from the Diachronic Electronic Corpus of Tyneside English (DECTE), we evaluate the output of a state-of-the-art commercial ASR system and conduct a fine-grained analysis of more than 3,000 transcription errors. Errors are classified by linguistic domain and examined in relation to social variables including gender, age, and socioeconomic status. In addition, an acoustic case study of selected vowel features demonstrates how gradient phonetic variation contributes directly to misrecognition.   The results show that phonological variation accounts for the majority of errors, with recurrent failures linked to dialect-specific features like vowel quality and glottalisation, as well as local vocabulary and non-standard grammatical forms. Error rates also vary across social groups, with higher error frequencies observed for men and for speakers at the extremes of the age spectrum. These findings indicate that ASR errors are not random but socially patterned and can be explained from a sociolinguistic perspective. Thus, the study demonstrates the importance of incorporating sociolinguistic expertise into the evaluation and development of speech technologies and argues that more equitable ASR systems require explicit attention to dialectal variation and community-based speech data.

### 🤖 AI 总结

**一句话总结**：本文以纽卡斯尔英语为例证明：商用ASR在方言语音上存在系统性偏差，错误与语言变异和社会群体特征相关。

**研究动机**：现有ASR多基于主流口音数据训练，导致对区域方言识别不均衡并可能造成不公平影响；需要用社会语言学视角解释偏差来源。

**核心方法**：使用DECTE语料库中的自发口语，评测一款先进商用ASR并对3000+转写错误按语言层面分类，同时结合性别、年龄、社会经济地位等变量统计，并做元音特征的声学个案分析以关联渐变语音差异与误识别。

**主要结论**：错误主要由语音/音系变异驱动，且集中出现在方言特征（元音音质、声门化）、地方词汇与非标准语法上；错误率在社会群体间呈模式化差异（男性与年龄两端更高），表明ASR偏差并非随机，需要纳入方言与社区数据及社会语言学知识以提升公平性。

**关键词**：语音识别偏差, 方言语音识别, 转写错误分析, 语音识别公平性, 音系变异, 元音音质, 声门化, 非标准语法, 口语语料库

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24549v1) | [下载PDF](https://arxiv.org/pdf/2603.24549v1.pdf)

---

## [6. Robust Multilingual Text-to-Pictogram Mapping for Scalable Reading Rehabilitation](https://arxiv.org/abs/2603.24536v1)

**作者**：Soufiane Jhilal, Martina Galletti  
**分类**：cs.CL, cs.HC  
**发布时间**：2026-03-25

### 📄 论文摘要

Reading comprehension presents a significant challenge for children with Special Educational Needs and Disabilities (SEND), often requiring intensive one-on-one reading support. To assist therapists in scaling this support, we developed a multilingual, AI-powered interface that automatically enhances text with visual scaffolding. This system dynamically identifies key concepts and maps them to contextually relevant pictograms, supporting learners across languages. We evaluated the system across five typologically diverse languages (English, French, Italian, Spanish, and Arabic), through multilingual coverage analysis, expert clinical review by speech therapists and special education professionals, and latency assessment. Evaluation results indicate high pictogram coverage and visual scaffolding density across the five languages. Expert audits suggested that automatically selected pictograms were semantically appropriate, with combined correct and acceptable ratings exceeding 95% for the four European languages and approximately 90% for Arabic despite reduced pictogram repository coverage. System latency remained within interactive thresholds suitable for real-time educational use. These findings support the technical viability, semantic safety, and acceptability of automated multimodal scaffolding to improve accessibility for neurodiverse learners.

### 🤖 AI 总结

**一句话总结**：提出并验证了一种可扩展的多语言文本到象形图（pictogram）自动映射系统，用于为SEND儿童提供实时视觉脚手架以辅助阅读康复。

**研究动机**：SEND儿童阅读理解常需大量一对一支持，治疗师与教育资源难以规模化覆盖；用自动化视觉提示增强文本可降低人工负担并提升跨语言可及性。

**核心方法**：构建多语言AI界面，动态抽取文本关键概念并将其映射到语境相关的象形图；在英语、法语、意大利语、西班牙语和阿拉伯语上做覆盖率/脚手架密度统计、临床专家语义正确性审查与系统延迟评测。

**主要结论**：五种语言总体具有较高象形图覆盖与可用的视觉脚手架密度，专家评价语义适配性在四种欧洲语言上“正确+可接受”>95%，阿拉伯语约90%（受图库覆盖限制）；交互延迟达实时阈值，表明该自动多模态脚手架在技术可行性与语义安全性上具备应用潜力。

**关键词**：文本到象形图映射, 多语言语义对齐, 关键概念抽取, 象形图检索匹配, 视觉支架, 阅读康复, 特殊教育需求（SEND）, 无障碍教育技术, 专家临床评审, 交互延迟评测, 多语言覆盖率分析

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24536v1) | [下载PDF](https://arxiv.org/pdf/2603.24536v1.pdf)

---

## [7. Representation Learning to Study Temporal Dynamics in Tutorial Scaffolding](https://arxiv.org/abs/2603.24535v1)

**作者**：Conrad Borchers, Jiayi Zhang, Ashish Gurung  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-03-25

### 📄 论文摘要

Adaptive scaffolding enhances learning, yet the field lacks robust methods for measuring it within authentic tutoring dialogue. This gap has become more pressing with the rise of remote human tutoring and large language model-based systems. We introduce an embedding-based approach that analyzes scaffolding dynamics by aligning the semantics of dialogue turns, problem statements, and correct solutions. Specifically, we operationalize alignment by computing cosine similarity between tutor and student contributions and task-relevant content. We apply this framework to 1,576 real-world mathematics tutoring dialogues from the Eedi Question Anchored Tutoring Dialogues dataset. The analysis reveals systematic differences in task alignment and distinct temporal patterns in how participants ground their contributions in problem and solution content. Further, mixed-effects models show that role-specific semantic alignment predicts tutorial progression beyond baseline features such as message order and length. Tutor contributions exhibited stronger grounding in problem content early in interactions. In contrast, student solution alignment was modestly positively associated with progression. These findings support scaffolding as a continuous, role-sensitive process grounded in task semantics. By capturing role-specific alignment over time, this approach provides a principled method for analyzing instructional dialogue and evaluating conversational tutoring systems.

### 🤖 AI 总结

**一句话总结**：提出一种基于语义嵌入对齐的度量框架，用时间序列方式刻画真实辅导对话中的脚手架（scaffolding）动态，并证明角色特定的语义对齐可预测辅导进程。

**研究动机**：自适应脚手架被认为能促进学习，但在真实辅导对话中缺乏可操作、稳健的量化测量方法；随着远程辅导与LLM辅导系统兴起，更需要可用于分析与评估的通用指标。

**核心方法**：将对话轮次（导师/学生发言）与题目陈述、标准答案映射到同一嵌入空间，使用余弦相似度定义“与任务内容的语义对齐”（如对齐题目/对齐答案）并分析其随时间的变化；在1,576段Eedi数学辅导对话上计算对齐轨迹，并用混合效应模型检验对齐对辅导进程的预测力（控制消息顺序、长度等基线特征）。

**主要结论**：导师与学生在任务对齐上存在系统性差异且呈现不同时间模式：导师早期更强地锚定题目内容，而学生与标准答案的对齐与进程呈温和正相关；角色特定的语义对齐能超越基线特征预测辅导进展，支持将脚手架视为连续、角色敏感且基于任务语义的过程。

**关键词**：教学支架, 辅导对话分析, 语义对齐, 嵌入表示学习, 余弦相似度, 时间动态建模, 角色特异特征, 混合效应模型, 远程真人辅导, 数学辅导对话语料

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24535v1) | [下载PDF](https://arxiv.org/pdf/2603.24535v1.pdf)

---

## cs.CV

## [8. TAG: Target-Agnostic Guidance for Stable Object-Centric Inference in Vision-Language-Action Models](https://arxiv.org/abs/2603.24584v1)

**作者**：Jiaying Zhou, Zhihao Zhan, Ruifeng Zhai 等 8 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-03-25

### 📄 论文摘要

Vision--Language--Action (VLA) policies have shown strong progress in mapping language instructions and visual observations to robotic actions, yet their reliability degrades in cluttered scenes with distractors. By analyzing failure cases, we find that many errors do not arise from infeasible motions, but from instance-level grounding failures: the policy often produces a plausible grasp trajectory that lands slightly off-target or even on the wrong object instance. To address this issue, we propose TAG (Target-Agnostic Guidance), a simple inference-time guidance mechanism that explicitly reduces distractor- and appearance-induced bias in VLA policies. Inspired by classifier-free guidance (CFG), TAG contrasts policy predictions under the original observation and an object-erased observation, and uses their difference as a residual steering signal that strengthens the influence of object evidence in the decision process. TAG does not require modifying the policy architecture and can be integrated with existing VLA policies with minimal training and inference changes. We evaluate TAG on standard manipulation benchmarks, including LIBERO, LIBERO-Plus, and VLABench, where it consistently improves robustness under clutter and reduces near-miss and wrong-object executions.

### 🤖 AI 总结

**一句话总结**：TAG通过对“原始观测”和“抹除目标物体观测”的策略输出做对比式引导，在不改模型结构的前提下显著提升VLA在杂乱场景中的目标实例对齐与抓取稳定性。

**研究动机**：现有VLA在有干扰物的拥挤场景中常出现实例级grounding失败，导致“几乎抓中但偏离”或“抓错相似物体”，且这些错误多非运动学不可行而是感知-决策偏置所致。

**核心方法**：提出推理时机制TAG，借鉴CFG：分别对原始观测与“目标物体被擦除/移除”的观测进行策略预测，用二者差值作为残差信号来强化目标物体证据、抑制干扰与外观偏置；该方法无需改架构，训练与推理改动很小即可接入现有VLA。

**主要结论**：在LIBERO、LIBERO-Plus与VLABench等基准上，TAG在杂乱环境中持续提升鲁棒性，显著减少near-miss与wrong-object执行，证明简单的对比式推理引导能有效改善实例级定位与动作生成。

**关键词**：视觉-语言-动作模型, 机器人操作策略, 实例级目标定位, 物体中心推理, 推理时引导, 无分类器引导, 目标无关引导, 遮挡与杂乱鲁棒性, 干扰物抑制, 物体擦除观测

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24584v1) | [下载PDF](https://arxiv.org/pdf/2603.24584v1.pdf)

---

## [9. Vision-Language Models vs Human: Perceptual Image Quality Assessment](https://arxiv.org/abs/2603.24578v1)

**作者**：Imran Mehmood, Imad Ali Shah, Ming Ronnier Luo 等 4 位作者  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-03-25

### 📄 论文摘要

Psychophysical experiments remain the most reliable approach for perceptual image quality assessment (IQA), yet their cost and limited scalability encourage automated approaches. We investigate whether Vision Language Models (VLMs) can approximate human perceptual judgments across three image quality scales: contrast, colorfulness and overall preference. Six VLMs four proprietary and two openweight models are benchmarked against psychophysical data. This work presents a systematic benchmark of VLMs for perceptual IQA through comparison with human psychophysical data. The results reveal strong attribute dependent variability models with high human alignment for colorfulness (ρup to 0.93) underperform on contrast and vice-versa. Attribute weighting analysis further shows that most VLMs assign higher weights to colorfulness compared to contrast when evaluating overall preference similar to the psychophysical data. Intramodel consistency analysis reveals a counterintuitive tradeoff: the most self consistent models are not necessarily the most human aligned suggesting response variability reflects sensitivity to scene dependent perceptual cues. Furthermore, human-VLM agreement is increased with perceptual separability, indicating VLMs are more reliable when stimulus differences are clearly expressed.

### 🤖 AI 总结

**一句话总结**：本文系统评测多种视觉语言模型在对比度、色彩丰富度与整体偏好三类感知图像质量判断上与人类心理物理实验的一致性，发现模型对不同属性的对齐程度差异显著。

**研究动机**：心理物理实验虽最可靠但成本高且难以规模化，因此需要评估VLM能否在感知图像质量评估中替代或逼近人类判断，并明确其适用边界。

**核心方法**：基于人类心理物理数据，构建对比度、色彩丰富度与整体偏好三种质量尺度的基准，对6个VLM（4个闭源+2个开源）进行相关性对比，并进一步做属性权重分析、模型内一致性与“感知可分离性”条件下的一致性分析。

**主要结论**：VLM与人类的一致性强烈依赖属性：部分模型在色彩丰富度上可达很高对齐（ρ最高约0.93）但在对比度上显著欠佳且存在反向情况；多数模型在整体偏好判断时对色彩的权重高于对比度，且自一致性高不等于更贴近人类；当刺激差异更清晰（感知可分离性更强）时，人机一致性会提高。

**关键词**：感知图像质量评估, 视觉语言模型（VLM）, 心理物理实验, 人类一致性评测, 系统基准测试, 色彩丰富度感知, 总体偏好预测, 属性加权分析, 模型内一致性, 感知可分离性, 场景依赖感知线索

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24578v1) | [下载PDF](https://arxiv.org/pdf/2603.24578v1.pdf)

---

## [10. EndoVGGT: GNN-Enhanced Depth Estimation for Surgical 3D Reconstruction](https://arxiv.org/abs/2603.24577v1)

**作者**：Falong Fan, Yi Xie, Arnis Lektauers 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-25

### 📄 论文摘要

Accurate 3D reconstruction of deformable soft tissues is essential for surgical robotic perception. However, low-texture surfaces, specular highlights, and instrument occlusions often fragment geometric continuity, posing a challenge for existing fixed-topology approaches. To address this, we propose EndoVGGT, a geometry-centric framework equipped with a Deformation-aware Graph Attention (DeGAT) module. Rather than using static spatial neighborhoods, DeGAT dynamically constructs feature-space semantic graphs to capture long-range correlations among coherent tissue regions. This enables robust propagation of structural cues across occlusions, enforcing global consistency and improving non-rigid deformation recovery. Extensive experiments on SCARED show that our method significantly improves fidelity, increasing PSNR by 24.6% and SSIM by 9.1% over prior state-of-the-art. Crucially, EndoVGGT exhibits strong zero-shot cross-dataset generalization to the unseen SCARED and EndoNeRF domains, confirming that DeGAT learns domain-agnostic geometric priors. These results highlight the efficacy of dynamic feature-space modeling for consistent surgical 3D reconstruction.

### 🤖 AI 总结

**一句话总结**：EndoVGGT 通过引入基于图注意力的动态语义图建模，提升了手术场景软组织在遮挡与低纹理下的深度估计与一致性3D重建质量，并具备良好的零样本泛化能力。

**研究动机**：手术软组织表面常见低纹理、反光与器械遮挡，导致几何连续性被打断，使依赖固定拓扑/静态邻域的重建方法难以恢复全局一致的非刚性形变。

**核心方法**：提出几何中心框架 EndoVGGT，并设计 Deformation-aware Graph Attention（DeGAT）模块：不使用静态空间邻域，而是在特征空间动态构建语义图以捕获远距离相关性，在遮挡区域间传播结构线索并约束全局一致性，从而改进深度估计与形变恢复。

**主要结论**：在 SCARED 上相较先前 SOTA 显著提升重建保真度（PSNR +24.6%，SSIM +9.1%），且对未见过的数据域（SCARED/EndoNeRF）表现出强零样本泛化，表明 DeGAT 学到了更具域无关性的几何先验。

**关键词**：手术机器人感知, 内窥镜视觉, 软组织三维重建, 非刚性形变恢复, 深度估计, 图神经网络, 图注意力机制, 动态特征空间图, 遮挡鲁棒性, 低纹理表面, 零样本跨数据集泛化

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24577v1) | [下载PDF](https://arxiv.org/pdf/2603.24577v1.pdf)

---

## [11. VFIG: Vectorizing Complex Figures in SVG with Vision-Language Models](https://arxiv.org/abs/2603.24575v1)

**作者**：Qijia He, Xunmei Liu, Hammaad Memon 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-25

### 📄 论文摘要

Scalable Vector Graphics (SVG) are an essential format for technical illustration and digital design, offering precise resolution independence and flexible semantic editability. In practice, however, original vector source files are frequently lost or inaccessible, leaving only "flat" rasterized versions (e.g., PNG or JPEG) that are difficult to modify or scale. Manually reconstructing these figures is a prohibitively labor-intensive process, requiring specialized expertise to recover the original geometric intent. To bridge this gap, we propose VFIG, a family of Vision-Language Models trained for complex and high-fidelity figure-to-SVG conversion. While this task is inherently data-driven, existing datasets are typically small-scale and lack the complexity of professional diagrams. We address this by introducing VFIG-DATA, a large-scale dataset of 66K high-quality figure-SVG pairs, curated from a diverse mix of real-world paper figures and procedurally generated diagrams. Recognizing that SVGs are composed of recurring primitives and hierarchical local structures, we introduce a coarse-to-fine training curriculum that begins with supervised fine-tuning (SFT) to learn atomic primitives and transitions to reinforcement learning (RL) refinement to optimize global diagram fidelity, layout consistency, and topological edge cases. Finally, we introduce VFIG-BENCH, a comprehensive evaluation suite with novel metrics designed to measure the structural integrity of complex figures. VFIG achieves state-of-the-art performance among open-source models and performs on par with GPT-5.2, achieving a VLM-Judge score of 0.829 on VFIG-BENCH.

### 🤖 AI 总结

**一句话总结**：VFIG 提出一套面向复杂专业图表的视觉-语言模型与数据/评测体系，实现从栅格图高保真自动还原为可编辑的 SVG。

**研究动机**：现实中大量技术插图的原始矢量文件丢失，仅剩 PNG/JPEG 等栅格图，导致编辑与无损缩放困难且人工重建成本极高。现有图像到 SVG 数据集规模小、复杂度不足，难以支撑高质量恢复。

**核心方法**：构建 6.6 万对高质量图像-SVG 配对数据集 VFIG-DATA，并利用 SVG 的原子图元与层级结构特点设计 coarse-to-fine 训练：先用 SFT 学习图元与局部结构，再用 RL 优化整体保真度、布局一致性与拓扑边界情况。提出评测套件 VFIG-BENCH 与结构完整性相关的新指标进行系统评估。

**主要结论**：VFIG 在复杂图表矢量化任务上达到开源模型 SOTA，并在 VFIG-BENCH 上与 GPT-5.2 表现相当（VLM-Judge 0.829），证明数据规模+课程式 SFT→RL 训练与结构化评测能显著提升图像到 SVG 的高保真重建能力。

**关键词**：栅格转矢量, 复杂图表矢量化, 视觉语言模型（VLM）, SVG图元建模, 层次结构解析, 粗到细训练, 监督微调（SFT）, 强化学习优化（RL）, 结构完整性评测指标, 大规模图表-SVG数据集

**评分**：47

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24575v1) | [下载PDF](https://arxiv.org/pdf/2603.24575v1.pdf)

---

## [12. Towards Training-Free Scene Text Editing](https://arxiv.org/abs/2603.24571v1)

**作者**：Yubo Li, Xugong Qin, Peng Zhang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-25

### 📄 论文摘要

Scene text editing seeks to modify textual content in natural images while maintaining visual realism and semantic consistency. Existing methods often require task-specific training or paired data, limiting their scalability and adaptability. In this paper, we propose TextFlow, a training-free scene text editing framework that integrates the strengths of Attention Boost (AttnBoost) and Flow Manifold Steering (FMS) to enable flexible, high-fidelity text manipulation without additional training. Specifically, FMS preserves the structural and style consistency by modeling the visual flow of characters and background regions, while AttnBoost enhances the rendering of textual content through attention-based guidance. By jointly leveraging these complementary modules, our approach performs end-to-end text editing through semantic alignment and spatial refinement in a plug-and-play manner. Extensive experiments demonstrate that our framework achieves visual quality and text accuracy comparable to or superior to those of training-based counterparts, generalizing well across diverse scenes and languages. This study advances scene text editing toward a more efficient, generalizable, and training-free paradigm. Code is available at https://github.com/lyb18758/TextFlow

### 🤖 AI 总结

**一句话总结**：提出TextFlow，一个无需额外训练的场景文字编辑框架，通过结合AttnBoost与FMS实现高保真、可泛化的自然图像文字替换与重绘。

**研究动机**：现有场景文字编辑方法常依赖任务特定训练或成对数据，导致成本高、适配性差且难以扩展到多场景/多语言。

**核心方法**：TextFlow以插件式方式联合两模块：FMS通过建模字符与背景区域的视觉流来约束结构与风格一致性，AttnBoost用注意力引导增强文字渲染与语义对齐，并配合空间细化实现端到端编辑。

**主要结论**：大量实验表明该训练自由框架在视觉质量与文本准确率上可达到或超过训练式方法，并能在多样场景与语言上稳定泛化，推动场景文字编辑走向更高效通用的范式。

**关键词**：场景文字编辑, 训练免微调, 文本图像编辑, 注意力引导, 字符视觉流建模, 语义对齐, 空间细化, 风格一致性, 多语言泛化

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24571v1) | [下载PDF](https://arxiv.org/pdf/2603.24571v1.pdf)

---

## [13. Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)

**作者**：Duc Vu, Anh Nguyen, Chi Tran 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-25

### 📄 论文摘要

Advances in diffusion-based video generation models, while significantly improving human animation, poses threats of misuse through the creation of fake videos from a specific person's photo and text prompts. Recent efforts have focused on adversarial attacks that introduce crafted perturbations to protect images from diffusion-based models. However, most existing approaches target image generation, while relatively few explicitly address image-to-video diffusion models (VDMs), and most primarily focus on UNet-based architectures. Hence, their effectiveness against Diffusion Transformer (DiT) models remains largely under-explored, as these models demonstrate improved feature retention, and stronger temporal consistency due to larger capacity and advanced attention mechanisms. In this work, we introduce Anti-I2V, a novel defense against malicious human image-to-video generation, applicable across diverse diffusion backbones. Instead of restricting noise updates to the RGB space, Anti-I2V operates in both the $L$*$a$*$b$* and frequency domains, improving robustness and concentrating on salient pixels. We then identify the network layers that capture the most distinct semantic features during the denoising process to design appropriate training objectives that maximize degradation of temporal coherence and generation fidelity. Through extensive validation, Anti-I2V demonstrates state-of-the-art defense performance against diverse video diffusion models, offering an effective solution to the problem.

### 🤖 AI 总结

**一句话总结**：Anti-I2V通过在颜色空间与频域联合施加对抗扰动，有效阻止从单张人像照片生成高保真、时序一致的恶意视频。

**研究动机**：扩散式图生视频模型可被滥用来用某人照片+文本生成伪造视频，现有防护多偏向图像生成且主要面向UNet，对DiT类视频扩散模型的防御效果不足。

**核心方法**：方法不局限于RGB域更新噪声，而是在L*a*b*与频域中优化扰动以提升鲁棒性并聚焦显著像素；同时分析去噪过程中最能表征语义的网络层，构造训练目标以最大化生成质量与时间一致性的退化。

**主要结论**：在多种视频扩散骨干（含UNet与DiT）上，Anti-I2V实现了更强的跨架构防御效果，显著降低生成视频的保真度与时序连贯性，达到SOTA防护表现。

**关键词**：图像到视频扩散模型, 人像伪造视频防护, 跨骨干鲁棒性, L*a*b*颜色空间, 频域扰动, 时间一致性退化, 去噪层语义特征, 生成保真度退化

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24570v1) | [下载PDF](https://arxiv.org/pdf/2603.24570v1.pdf)

---

## [14. POLY-SIM: Polyglot Speaker Identification with Missing Modality Grand Challenge 2026 Evaluation Plan](https://arxiv.org/abs/2603.24569v1)

**作者**：Marta Moscati, Muhammad Saad Saeed, Marina Zanoni 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-25

### 📄 论文摘要

Multimodal speaker identification systems typically assume the availability of complete and homogeneous audio-visual modalities during both training and testing. However, in real-world applications, such assumptions often do not hold. Visual information may be missing due to occlusions, camera failures, or privacy constraints, while multilingual speakers introduce additional complexity due to linguistic variability across languages. These challenges significantly affect the robustness and generalization of multimodal speaker identification systems. The POLY-SIM Grand Challenge 2026 aims to advance research in multimodal speaker identification under missing-modality and cross-lingual conditions. Specifically, the Grand Challenge encourages the development of robust methods that can effectively leverage incomplete multimodal inputs while maintaining strong performance across different languages. This report presents the design and organization of the POLY-SIM Grand Challenge 2026, including the dataset, task formulation, evaluation protocol, and baseline model. By providing a standardized benchmark and evaluation framework, the challenge aims to foster progress toward more robust and practical multimodal speaker identification systems.

### 🤖 AI 总结

**一句话总结**：POLY-SIM 2026 提出一个面向“模态缺失+跨语言”场景的多模态说话人识别评测计划，给出数据集、任务定义、评测协议与基线以推动鲁棒方法研究。

**研究动机**：现实应用中音频-视觉信息常不完整（遮挡、设备故障、隐私限制等），同时多语言说话人带来语言差异，导致现有依赖完整同质模态的系统鲁棒性与泛化能力不足。

**核心方法**：设计并组织POLY-SIM Grand Challenge：围绕缺失模态与跨语言条件制定任务形式，提供标准化数据集与评测协议，并发布基线模型作为对照与参赛起点。

**主要结论**：通过统一的benchmark与评测框架，该挑战旨在促进能利用不完整多模态输入且跨语言保持性能的说话人识别技术发展，使系统更鲁棒、更贴近实际部署需求。

**关键词**：多模态说话人识别, 视听融合, 缺失模态学习, 跨语言说话人识别, 多语言鲁棒性, 模态不完整推理, 隐私约束视觉缺失, 遮挡鲁棒性, 评测基准, 评测协议

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24569v1) | [下载PDF](https://arxiv.org/pdf/2603.24569v1.pdf)

---

## [15. LensWalk: Agentic Video Understanding by Planning How You See in Videos](https://arxiv.org/abs/2603.24558v1)

**作者**：Keliang Li, Yansong Li, Hongze Shen 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-25

### 📄 论文摘要

The dense, temporal nature of video presents a profound challenge for automated analysis. Despite the use of powerful Vision-Language Models, prevailing methods for video understanding are limited by the inherent disconnect between reasoning and perception: they rely on static, pre-processed information and cannot actively seek raw evidence from video as their understanding evolves. To address this, we introduce LensWalk, a flexible agentic framework that empowers a Large Language Model reasoner to control its own visual observation actively. LensWalk establishes a tight reason-plan-observe loop where the agent dynamically specifies, at each step, the temporal scope and sampling density of the video it observes. Using a suite of versatile, Vision-Language Model based tools parameterized by these specifications, the agent can perform broad scans for cues, focus on specific segments for fact extraction, and stitch evidence from multiple moments for holistic verification. This design allows for progressive, on-demand evidence gathering that directly serves the agent's evolving chain of thought. Without requiring any model fine-tuning, LensWalk delivers substantial, plug-and-play performance gains on multiple model recipes, boosting their accuracy by over 5\% on challenging long-video benchmarks like LVBench and Video-MME. Our analysis reveals that enabling an agent to control how it sees is key to unlocking more accurate, robust, and interpretable video reasoning.

### 🤖 AI 总结

**一句话总结**：LensWalk让LLM以“计划-观察”方式主动控制视频采样与查看范围，从而在无需微调的情况下显著提升长视频理解与推理准确率。

**研究动机**：现有视频理解多依赖静态预处理帧/摘要，推理与感知脱节，模型无法随着推理过程主动回到原视频中按需取证。长视频时序密集导致信息取舍困难，使这种被动观察的缺陷更明显。

**核心方法**：提出LensWalk的agent框架，构建紧密的“reason-plan-observe”闭环：每步由LLM决定要看的时间段与采样密度。通过一组可参数化的VLM工具实现粗粒度扫视、片段聚焦抽取与跨时刻证据拼接验证，按需逐步收集原始证据服务于推理链。

**主要结论**：在不做模型微调的前提下，LensWalk可作为即插即用组件在多种模型配置上带来稳定收益，并在LVBench、Video-MME等长视频基准上提升超过5%准确率。分析表明，让智能体“控制如何看”能带来更准确、更鲁棒且更可解释的视频推理。

**关键词**：视频推理, 主动感知, 智能体框架, 推理-规划-观察循环, 时域范围控制, 自适应帧采样, 证据驱动推理, 免微调, 长视频评测基准（LVBench）

**评分**：44

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24558v1) | [下载PDF](https://arxiv.org/pdf/2603.24558v1.pdf)

---

## [16. The role of spatial context and multitask learning in the detection of organic and conventional farming systems based on Sentinel-2 time series](https://arxiv.org/abs/2603.24552v1)

**作者**：Jan Hemmerling, Marcel Schwieder, Philippe Rufin 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-25

### 📄 论文摘要

Organic farming is a key element in achieving more sustainable agriculture. For a better understanding of the development and impact of organic farming, comprehensive, spatially explicit information is needed. This study presents an approach for the discrimination of organic and conventional farming systems using intra-annual Sentinel-2 time series. In addition, it examines two factors influencing this discrimination: the joint learning of crop type information in a concurrent task and the role of spatial context. A Vision Transformer model based on the Temporo-Spatial Vision Transformer (TSViT) architecture was used to construct a classification model for the two farming systems. The model was extended for simultaneous learning of the crop type, creating a multitask learning setting. By varying the patch size presented to the model, we tested the influence of spatial context on the classification accuracy of both tasks. We show that discrimination between organic and conventional farming systems using multispectral remote sensing data is feasible. However, classification performance varies substantially across crop types. For several crops, such as winter rye, winter wheat, and winter oat, F1 scores of 0.8 or higher can be achieved. In contrast, other agricultural land use classes, such as permanent grassland, orchards, grapevines, and hops, cannot be reliably distinguished, with F1 scores for the organic management class of 0.4 or lower. Joint learning of farming system and crop type provides only limited additional benefits over single-task learning. In contrast, incorporating wider spatial context improves the performance of both farming system and crop type classification. Overall, we demonstrate that a classification of agricultural farming systems is possible in a diverse agricultural region using multispectral remote sensing data.

### 🤖 AI 总结

**一句话总结**：基于Sentinel-2年内时间序列，使用TSViT类Vision Transformer可在一定作物上较好区分有机与常规农业，并且更大的空间上下文比多任务学习带来更显著的性能提升。

**研究动机**：有机农业评估需要空间显式、可规模化的管理方式信息，但传统统计/调查难以覆盖与更新。研究旨在探索利用多光谱遥感时间序列自动识别有机/常规系统，并量化作物类型信息与空间上下文对识别效果的影响。

**核心方法**：采用基于Temporo-Spatial Vision Transformer (TSViT) 的模型对Sentinel-2年内多光谱时间序列进行分类，任务为有机/常规识别；并扩展为同时预测作物类型的多任务学习框架。通过改变输入patch大小来控制空间上下文范围，比较单任务/多任务与不同空间尺度下两项任务的精度差异。

**主要结论**：利用多光谱遥感区分有机与常规在部分作物上可达较高性能（如冬黑麦/冬小麦/冬燕麦有机类F1≥0.8），但在永久草地、果园、葡萄、啤酒花等地类上难以可靠区分（有机类F1≤0.4）。多任务联合学习对提升有机/常规识别的增益有限，而引入更宽的空间上下文能同时提升耕作系统与作物类型分类表现。

**关键词**：有机农业识别, 常规农业识别, 农业管理分类, 作物类型分类, Sentinel-2 时间序列, 多光谱遥感, 空间上下文建模, 多任务学习

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24552v1) | [下载PDF](https://arxiv.org/pdf/2603.24552v1.pdf)

---

## [17. SEGAR: Selective Enhancement for Generative Augmented Reality](https://arxiv.org/abs/2603.24541v1)

**作者**：Fanjun Bu, Chenyang Yuan, Hiroshi Yasuda  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-25

### 📄 论文摘要

Generative world models offer a compelling foundation for augmented-reality (AR) applications: by predicting future image sequences that incorporate deliberate visual edits, they enable temporally coherent, augmented future frames that can be computed ahead of time and cached, avoiding per-frame rendering from scratch in real time. In this work, we present SEGAR, a preliminary framework that combines a diffusion-based world model with a selective correction stage to support this vision. The world model generates augmented future frames with region-specific edits while preserving others, and the correction stage subsequently aligns safety-critical regions with real-world observations while preserving intended augmentations elsewhere. We demonstrate this pipeline in driving scenarios as a representative setting where semantic region structure is well defined and real-world feedback is readily available. We view this as an early step toward generative world models as practical AR infrastructure, where future frames can be generated, cached, and selectively corrected on demand.

### 🤖 AI 总结

**一句话总结**：SEGAR将扩散式生成世界模型与“选择性纠正”结合，用于在AR中提前生成并缓存带区域编辑的未来帧，同时用真实观测对安全关键区域进行对齐修正。

**研究动机**：传统AR逐帧实时渲染成本高且难以保证时间一致性；生成式世界模型可预生成未来序列，但需要在保持既定增强效果的同时，可靠地纠正与真实世界偏差、尤其是安全关键区域的误差。

**核心方法**：先用扩散式世界模型预测带“区域特定编辑”的未来图像序列，保留未编辑区域的时序一致性；再引入选择性纠正阶段，利用实时真实观测仅对安全关键区域进行对齐修复，同时尽量不破坏其他区域的预期增强。

**主要结论**：在驾驶场景验证了该两阶段管线能实现“可缓存的生成式未来帧+按需局部纠正”，为将生成世界模型作为实用AR基础设施（预生成、缓存、选择性校正）提供了早期证据与方向。

**关键词**：生成式世界模型, 增强现实, Diffusion, 未来帧预测, 时序一致性, 区域级编辑, 选择性校正, 安全关键区域对齐, 真实世界反馈闭环, 帧缓存预生成, 自动驾驶场景

**评分**：45

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24541v1) | [下载PDF](https://arxiv.org/pdf/2603.24541v1.pdf)

---

## [18. CliPPER: Contextual Video-Language Pretraining on Long-form Intraoperative Surgical Procedures for Event Recognition](https://arxiv.org/abs/2603.24539v1)

**作者**：Florian Stilz, Vinkle Srivastav, Nassir Navab 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-25

### 📄 论文摘要

Video-language foundation models have proven to be highly effective in zero-shot applications across a wide range of tasks. A particularly challenging area is the intraoperative surgical procedure domain, where labeled data is scarce, and precise temporal understanding is often required for complex downstream tasks. To address this challenge, we introduce CliPPER (Contextual Video-Language Pretraining on Long-form Intraoperative Surgical Procedures for Event Recognition), a novel video-language pretraining framework trained on surgical lecture videos. Our method is designed for fine-grained temporal video-text recognition and introduces several novel pretraining strategies to improve multimodal alignment in long-form surgical videos. Specifically, we propose Contextual Video-Text Contrastive Learning (VTC_CTX) and Clip Order Prediction (COP) pretraining objectives, both of which leverage temporal and contextual dependencies to enhance local video understanding. In addition, we incorporate a Cycle-Consistency Alignment over video-text matches within the same surgical video to enforce bidirectional consistency and improve overall representation coherence. Moreover, we introduce a more refined alignment loss, Frame-Text Matching (FTM), to improve the alignment between video frames and text. As a result, our model establishes a new state-of-the-art across multiple public surgical benchmarks, including zero-shot recognition of phases, steps, instruments, and triplets. The source code and pretraining captions can be found at https://github.com/CAMMA-public/CliPPER.

### 🤖 AI 总结

**一句话总结**：CliPPER通过面向长时程手术视频的上下文对齐预训练目标，显著提升了手术事件的细粒度时序理解与零样本识别能力。

**研究动机**：手术术中场景标注稀缺且事件具有强时序依赖，通用视频-语言模型难以在长视频中实现精确的局部对齐与阶段/步骤等事件识别。

**核心方法**：在手术讲座长视频上进行视频-语言预训练，提出VTC_CTX利用上下文进行对比学习、COP进行片段顺序预测以建模时序依赖，并用同一视频内的循环一致性对齐约束双向匹配；同时引入FTM帧-文本匹配损失以细化帧级对齐。

**主要结论**：在多个公开手术基准上取得新的SOTA，尤其在零样本的阶段、步骤、器械与triplet识别上表现更强，证明所设计的上下文与时序对齐预训练目标能有效改善长时程手术视频的多模态表征。

**关键词**：视频-语言预训练, 术中手术视频, 手术事件识别, 时间定位, 多模态对齐, 视频-文本对比学习, 片段顺序预测, 循环一致性对齐, 帧-文本匹配, 零样本识别, 手术阶段识别

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24539v1) | [下载PDF](https://arxiv.org/pdf/2603.24539v1.pdf)

---

## [19. Cross-Modal Prototype Alignment and Mixing for Training-Free Few-Shot Classification](https://arxiv.org/abs/2603.24528v1)

**作者**：Dipam Goswami, Simone Magistri, Gido M. van de Ven 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-25

### 📄 论文摘要

Vision-language models (VLMs) like CLIP are trained with the objective of aligning text and image pairs. To improve CLIP-based few-shot image classification, recent works have observed that, along with text embeddings, image embeddings from the training set are an important source of information. In this work we investigate the impact of directly mixing image and text prototypes for few-shot classification and analyze this from a bias-variance perspective. We show that mixing prototypes acts like a shrinkage estimator. Although mixed prototypes improve classification performance, the image prototypes still add some noise in the form of instance-specific background or context information. In order to capture only information from the image space relevant to the given classification task, we propose projecting image prototypes onto the principal directions of the semantic text embedding space to obtain a text-aligned semantic image subspace. These text-aligned image prototypes, when mixed with text embeddings, further improve classification. However, for downstream datasets with poor cross-modal alignment in CLIP, semantic alignment might be suboptimal. We show that the image subspace can still be leveraged by modeling the anisotropy using class covariances. We demonstrate that combining a text-aligned mixed prototype classifier and an image-specific LDA classifier outperforms existing methods across few-shot classification benchmarks.

### 🤖 AI 总结

**一句话总结**：提出一种训练无关的少样本分类方法，通过将图像原型与文本原型对齐后再混合，并结合LDA建模图像空间各向异性，从而在多项基准上优于现有CLIP少样本方法。

**研究动机**：仅用文本原型进行CLIP少样本分类会忽略训练集/支持集图像嵌入的有效信息，但直接用图像原型又会引入与类别无关的背景/上下文噪声并导致跨模态对齐不足。

**核心方法**：将“图像原型+文本原型”的混合解释为一种收缩估计以降低方差，并进一步把图像原型投影到文本语义嵌入空间的主方向上，得到文本对齐的语义图像子空间后再进行混合；当数据集跨模态对齐较差时，引入基于类协方差的图像空间LDA来刻画各向异性，并将文本对齐的混合分类器与图像特定的LDA分类器融合。

**主要结论**：原型混合能稳定提升少样本分类但会受图像噪声影响；通过投影获得文本对齐的语义图像原型可进一步提升，而在对齐不佳场景下用类协方差LDA补足图像空间判别信息，二者结合在多项少样本基准上达到更优性能。

**关键词**：少样本分类, 免训练适配, 视觉-语言模型, 跨模态对齐, 原型混合, 收缩估计, 偏差-方差分析, 语义子空间投影, 主成分方向, 各向异性建模, 类别协方差

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24528v1) | [下载PDF](https://arxiv.org/pdf/2603.24528v1.pdf)

---

## [20. Toward Physically Consistent Driving Video World Models under Challenging Trajectories](https://arxiv.org/abs/2603.24506v1)

**作者**：Jiawei Zhou, Zhenxin Zhu, Lingyi Du 等 13 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-25

### 📄 论文摘要

Video generation models have shown strong potential as world models for autonomous driving simulation. However, existing approaches are primarily trained on real-world driving datasets, which mostly contain natural and safe driving scenarios. As a result, current models often fail when conditioned on challenging or counterfactual trajectories-such as imperfect trajectories generated by simulators or planning systems-producing videos with severe physical inconsistencies and artifacts. To address this limitation, we propose PhyGenesis, a world model designed to generate driving videos with high visual fidelity and strong physical consistency. Our framework consists of two key components: (1) a physical condition generator that transforms potentially invalid trajectory inputs into physically plausible conditions, and (2) a physics-enhanced video generator that produces high-fidelity multi-view driving videos under these conditions. To effectively train these components, we construct a large-scale, physics-rich heterogeneous dataset. Specifically, in addition to real-world driving videos, we generate diverse challenging driving scenarios using the CARLA simulator, from which we derive supervision signals that guide the model to learn physically grounded dynamics under extreme conditions. This challenging-trajectory learning strategy enables trajectory correction and promotes physically consistent video generation. Extensive experiments demonstrate that PhyGenesis consistently outperforms state-of-the-art methods, especially on challenging trajectories. Our project page is available at: https://wm-research.github.io/PhyGenesis/.

### 🤖 AI 总结

**一句话总结**：PhyGenesis 通过“轨迹物理纠正 + 物理增强视频生成”的两阶段框架，在困难/反事实轨迹条件下生成更高保真且更物理一致的自动驾驶多视角视频。

**研究动机**：现有驾驶视频世界模型多基于真实道路的安全驾驶数据训练，面对规划器/模拟器产生的不完美或反事实轨迹时容易出现明显物理不一致与伪影，需要能在极端轨迹下仍遵循物理规律的生成模型。

**核心方法**：提出物理条件生成器将潜在无效的输入轨迹转换为物理可行的条件，再用物理增强的视频生成器在该条件下生成高保真多视角驾驶视频；并构建包含真实数据与CARLA模拟生成的“物理丰富异构数据集”，利用模拟器导出的监督信号进行挑战轨迹学习以实现轨迹纠正与物理约束。

**主要结论**：在大量实验中，PhyGenesis 相比现有SOTA方法在视觉质量与物理一致性上均更优，优势在挑战性轨迹场景下尤为显著，验证了引入物理纠正与物理增强训练数据/信号的有效性。

**关键词**：自动驾驶世界模型, 驾驶视频生成, 物理一致性, 挑战轨迹条件生成, 反事实轨迹, 轨迹校正, 物理增强视频生成, 多视角视频生成, 仿真监督信号, 物理富集异构数据集

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24506v1) | [下载PDF](https://arxiv.org/pdf/2603.24506v1.pdf)

---

## cs.LG

## [21. Polynomial Speedup in Diffusion Models with the Multilevel Euler-Maruyama Method](https://arxiv.org/abs/2603.24594v1)

**作者**：Arthur Jacot  
**分类**：cs.LG, math.NA, stat.ML  
**发布时间**：2026-03-25

### 📄 论文摘要

We introduce the Multilevel Euler-Maruyama (ML-EM) method compute solutions of SDEs and ODEs using a range of approximators $f^1,\dots,f^k$ to the drift $f$ with increasing accuracy and computational cost, only requiring a few evaluations of the most accurate $f^k$ and many evaluations of the less costly $f^1,\dots,f^{k-1}$. If the drift lies in the so-called Harder than Monte Carlo (HTMC) regime, i.e. it requires $ε^{-γ}$ compute to be $ε$-approximated for some $γ>2$, then ML-EM $ε$-approximates the solution of the SDE with $ε^{-γ}$ compute, improving over the traditional EM rate of $ε^{-γ-1}$. In other terms it allows us to solve the SDE at the same cost as a single evaluation of the drift. In the context of diffusion models, the different levels $f^{1},\dots,f^{k}$ are obtained by training UNets of increasing sizes, and ML-EM allows us to perform sampling with the equivalent of a single evaluation of the largest UNet. Our numerical experiments confirm our theory: we obtain up to fourfold speedups for image generation on the CelebA dataset downscaled to 64x64, where we measure a $γ\approx2.5$. Given that this is a polynomial speedup, we expect even stronger speedups in practical applications which involve orders of magnitude larger networks.

### 🤖 AI 总结

**一句话总结**：提出多层Euler–Maruyama（ML-EM）用多精度漂移近似器协同采样，在“HTMC”高成本漂移场景下将SDE求解复杂度从传统EM的ε^{-γ-1}提升到ε^{-γ}，实现多项式加速并用于扩散模型采样。

**研究动机**：扩散模型采样需要大量步数且每步都要评估代价高昂的漂移/score网络（如大UNet），导致总体成本过高；希望在保持精度的同时减少对最昂贵网络的调用次数。

**核心方法**：ML-EM在多个分辨率/容量递增的漂移近似器f^1…f^k之间做多层校正：大量使用便宜但粗糙的近似，少量使用最精确但昂贵的近似；并在漂移满足“Harder than Monte Carlo”(近似到误差ε需ε^{-γ}计算且γ>2)时给出理论复杂度改进。

**主要结论**：理论上ML-EM可用ε^{-γ}计算量达到ε精度（相当于“以一次漂移评估的成本”解决SDE），优于标准EM的ε^{-γ-1}；在CelebA 64×64实验中测得γ≈2.5并获得最高约4倍采样加速，且预测网络更大时加速更显著。

**关键词**：扩散模型采样加速, 随机微分方程（SDE）求解, 常微分方程（ODE）求解, 漂移项近似, 多保真近似器, 多层蒙特卡洛（MLMC）, 多项式加速, 误差-计算复杂度权衡

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24594v1) | [下载PDF](https://arxiv.org/pdf/2603.24594v1.pdf)

---

## [22. DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587v1)

**作者**：Pengxuan Yang, Yupeng Zheng, Deheng Qian 等 14 位作者  
**分类**：cs.LG, cs.RO  
**发布时间**：2026-03-25

### 📄 论文摘要

We introduce DreamerAD, the first latent world model framework that enables efficient reinforcement learning for autonomous driving by compressing diffusion sampling from 100 steps to 1 - achieving 80x speedup while maintaining visual interpretability. Training RL policies on real-world driving data incurs prohibitive costs and safety risks. While existing pixel-level diffusion world models enable safe imagination-based training, they suffer from multi-step diffusion inference latency (2s/frame) that prevents high-frequency RL interaction. Our approach leverages denoised latent features from video generation models through three key mechanisms: (1) shortcut forcing that reduces sampling complexity via recursive multi-resolution step compression, (2) an autoregressive dense reward model operating directly on latent representations for fine-grained credit assignment, and (3) Gaussian vocabulary sampling for GRPO that constrains exploration to physically plausible trajectories. DreamerAD achieves 87.7 EPDMS on NavSim v2, establishing state-of-the-art performance and demonstrating that latent-space RL is effective for autonomous driving.

### 🤖 AI 总结

**一句话总结**：DreamerAD将扩散世界模型的多步采样压缩到一步，在保持可解释视觉生成的同时实现约80×加速，从而让自动驾驶能高频率地进行“想象训练”的强化学习并取得SOTA表现。

**研究动机**：真实道路数据上训练RL代价高且存在安全风险，因此需要基于世界模型的离线/想象式训练；但像素级扩散世界模型推理延迟高（约2s/帧），无法支撑高频交互与高效策略学习。

**核心方法**：利用视频生成模型的去噪潜变量进行潜空间RL：用shortcut forcing递归多分辨率压缩扩散步数到1步；在潜变量上训练自回归稠密奖励模型以实现细粒度信用分配；并用Gaussian vocabulary sampling配合GRPO约束探索到物理可行轨迹。

**主要结论**：DreamerAD在NavSim v2上达到87.7 EPDMS并刷新SOTA，证明潜空间世界模型+一步采样可显著提升自动驾驶RL的训练效率且不牺牲可解释性与性能。

**关键词**：自动驾驶强化学习, 潜在世界模型, 扩散模型采样加速, 想象训练, 潜在空间强化学习, 视频生成模型特征, 多分辨率步压缩, 稠密奖励模型, 高斯词表采样

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24587v1) | [下载PDF](https://arxiv.org/pdf/2603.24587v1.pdf)

---

## [23. UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience](https://arxiv.org/abs/2603.24533v1)

**作者**：Zichuan Lin, Feiyu Liu, Yijun Yang 等 12 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-03-25

### 📄 论文摘要

Autonomous mobile GUI agents have attracted increasing attention along with the advancement of Multimodal Large Language Models (MLLMs). However, existing methods still suffer from inefficient learning from failed trajectories and ambiguous credit assignment under sparse rewards for long-horizon GUI tasks. To that end, we propose UI-Voyager, a novel two-stage self-evolving mobile GUI agent. In the first stage, we employ Rejection Fine-Tuning (RFT), which enables the continuous co-evolution of data and models in a fully autonomous loop. The second stage introduces Group Relative Self-Distillation (GRSD), which identifies critical fork points in group rollouts and constructs dense step-level supervision from successful trajectories to correct failed ones. Extensive experiments on AndroidWorld show that our 4B model achieves an 81.0% Pass@1 success rate, outperforming numerous recent baselines and exceeding human-level performance. Ablation and case studies further verify the effectiveness of GRSD. Our method represents a significant leap toward efficient, self-evolving, and high-performance mobile GUI automation without expensive manual data annotation.

### 🤖 AI 总结

**一句话总结**：UI-Voyager提出一种两阶段自进化的移动端GUI智能体，通过从失败轨迹中高效学习与构造稠密监督，在AndroidWorld上以4B模型达到81.0% Pass@1并超过人类水平。

**研究动机**：现有移动GUI智能体在长时序任务中常面临稀疏奖励导致的信用分配不清，以及对失败轨迹学习效率低的问题，难以持续自主提升且依赖昂贵标注。

**核心方法**：第一阶段使用Rejection Fine-Tuning（RFT）在全自动闭环中让数据与模型共同迭代进化；第二阶段提出Group Relative Self-Distillation（GRSD），在组内多次rollout中定位关键分叉点，并从成功轨迹提取逐步（step-level）稠密监督来纠正失败轨迹。

**主要结论**：在AndroidWorld的大量实验表明该方法显著优于近期基线，4B模型取得81.0% Pass@1且超过人类表现；消融与案例分析进一步验证GRSD能有效提升从失败经验中学习与长时序任务的成功率。

**关键词**：移动端GUI智能体, 长时序GUI任务, 稀疏奖励, 失败轨迹学习, 拒绝微调(RFT, 关键分叉点识别, UI-Voyager, Self-Evolving

**评分**：59

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24533v1) | [下载PDF](https://arxiv.org/pdf/2603.24533v1.pdf)

---

## [24. No Single Metric Tells the Whole Story: A Multi-Dimensional Evaluation Framework for Uncertainty Attributions](https://arxiv.org/abs/2603.24524v1)

**作者**：Emily Schiller, Teodor Chiaburu, Marco Zullich 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-25

### 📄 论文摘要

Research on explainable AI (XAI) has frequently focused on explaining model predictions. More recently, methods have been proposed to explain prediction uncertainty by attributing it to input features (uncertainty attributions). However, the evaluation of these methods remains inconsistent as studies rely on heterogeneous proxy tasks and metrics, hindering comparability. We address this by aligning uncertainty attributions with the well-established Co-12 framework for XAI evaluation. We propose concrete implementations for the correctness, consistency, continuity, and compactness properties. Additionally, we introduce conveyance, a property tailored to uncertainty attributions that evaluates whether controlled increases in epistemic uncertainty reliably propagate to feature-level attributions. We demonstrate our evaluation framework with eight metrics across combinations of uncertainty quantification and feature attribution methods on tabular and image data. Our experiments show that gradient-based methods consistently outperform perturbation-based approaches in consistency and conveyance, while Monte-Carlo dropconnect outperforms Monte-Carlo dropout in most metrics. Although most metrics rank the methods consistently across samples, inter-method agreement remains low. This suggests no single metric sufficiently evaluates uncertainty attribution quality. The proposed evaluation framework contributes to the body of knowledge by establishing a foundation for systematic comparison and development of uncertainty attribution methods.

### 🤖 AI 总结

**一句话总结**：论文提出一个多维度评估框架来系统衡量“不确定性归因”（把预测不确定性归到输入特征上）的质量，强调单一指标不足以全面评价。

**研究动机**：现有不确定性归因方法的评估依赖各自为政的代理任务与指标，导致结果不可比、结论不稳健；因此需要一个与XAI经典评价维度对齐的统一框架。

**核心方法**：将不确定性归因评价对齐到Co-12框架，给出correctness、consistency、continuity、compactness的可操作度量，并新增面向不确定性归因的conveyance指标（检验可控增加的认知不确定性是否能可靠传递到特征归因）；在表格与图像数据上组合多种不确定性量化与特征归因方法，用8个指标进行实验对比。

**主要结论**：梯度类归因在一致性与conveyance上普遍优于扰动类方法，且MC dropconnect在多数指标上优于MC dropout；尽管多数指标在样本内对方法排序较一致，但不同方法/指标间一致性（agreement）仍低，表明需要多指标联合评估而非依赖单一指标。

**关键词**：不确定性归因, 不确定性归因评测, 多维评测框架, Co-12评测框架, 认知不确定性, 特征归因, 正确性指标, 一致性指标, 连续性指标, 紧凑性指标, 梯度归因方法, 扰动归因方法

**评分**：16

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24524v1) | [下载PDF](https://arxiv.org/pdf/2603.24524v1.pdf)

---

## [25. TuneShift-KD: Knowledge Distillation and Transfer for Fine-tuned Models](https://arxiv.org/abs/2603.24518v1)

**作者**：Yushi Guan, Jeanine Ohene-Agyei, Daniel Kwan 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-25

### 📄 论文摘要

To embed domain-specific or specialized knowledge into pre-trained foundation models, fine-tuning using techniques such as parameter efficient fine-tuning (e.g. LoRA) is a common practice. However, as new LLM architectures and pre-trained models emerge, transferring this specialized knowledge to newer models becomes an important task. In many scenarios, the original specialized data may be unavailable due to privacy or commercial restrictions, necessitating distillation and transfer of this specialized knowledge from the fine-tuned base model to a different pre-trained model. We present TuneShift-KD, a novel approach that automatically distills specialized knowledge from a fine-tuned model to a target model using only a few examples representative of the specialized information. Our key insight is that specialized knowledge can be identified through perplexity differences between base and fine-tuned models: prompts where the fine-tuned model responds confidently (low perplexity), but the base model struggles (high perplexity), indicate queries corresponding to the specialized knowledge learned by the fine-tuned model. TuneShift-KD leverages this insight to create a synthetic training dataset to transfer the specialized knowledge. Using an iterative process, TuneShift-KD generates more prompts similar to those that generated responses with specialized knowledge. TuneShift-KD does not require training discriminators or access to training datasets. It is an automated approach that only requires the initial fine-tuned and base models and a few representative prompts. Our experiments demonstrate that models fine-tuned using TuneShift-KD achieve higher accuracy than prior approaches, enabling ease of deployment and more effective transfer of the specialized knowledge.

### 🤖 AI 总结

**一句话总结**：TuneShift-KD通过比较基座模型与微调模型的困惑度差异，自动挖掘“专有知识”相关提示并合成数据，将微调模型的领域能力蒸馏迁移到新的目标模型。

**研究动机**：随着新LLM与架构不断出现，已微调模型中的领域知识需要迁移到新底座；但原始专有数据常因隐私/商业限制不可用，迫切需要一种不依赖原训练集的知识迁移方法。

**核心方法**：用“基座高困惑度+微调低困惑度”的提示作为专有知识定位信号，选取这些提示并生成对应回答构造合成蒸馏数据；再通过迭代生成更多相似提示扩充数据集，对目标模型进行蒸馏训练，无需判别器或访问原始数据。

**主要结论**：在仅需少量代表性示例、无需原始训练数据的条件下，TuneShift-KD能更有效地将专有知识从微调模型迁移到目标模型，实验上其微调后准确率优于以往方法并更易部署。

**关键词**：知识蒸馏, 模型迁移, 微调知识转移, 参数高效微调, 基础模型, 无原始数据蒸馏, 困惑度差异, 提示选择, 合成训练数据, 迭代式提示生成

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24518v1) | [下载PDF](https://arxiv.org/pdf/2603.24518v1.pdf)

---

## [26. AVO: Agentic Variation Operators for Autonomous Evolutionary Search](https://arxiv.org/abs/2603.24517v1)

**作者**：Terry Chen, Zhifan Ye, Bing Xu 等 23 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-25

### 📄 论文摘要

Agentic Variation Operators (AVO) are a new family of evolutionary variation operators that replace the fixed mutation, crossover, and hand-designed heuristics of classical evolutionary search with autonomous coding agents. Rather than confining a language model to candidate generation within a prescribed pipeline, AVO instantiates variation as a self-directed agent loop that can consult the current lineage, a domain-specific knowledge base, and execution feedback to propose, repair, critique, and verify implementation edits. We evaluate AVO on attention, among the most aggressively optimized kernel targets in AI, on NVIDIA Blackwell (B200) GPUs. Over 7 days of continuous autonomous evolution on multi-head attention, AVO discovers kernels that outperform cuDNN by up to 3.5% and FlashAttention-4 by up to 10.5% across the evaluated configurations. The discovered optimizations transfer readily to grouped-query attention, requiring only 30 minutes of additional autonomous adaptation and yielding gains of up to 7.0% over cuDNN and 9.3% over FlashAttention-4. Together, these results show that agentic variation operators move beyond prior LLM-in-the-loop evolutionary pipelines by elevating the agent from candidate generator to variation operator, and can discover performance-critical micro-architectural optimizations that produce kernels surpassing state-of-the-art expert-engineered attention implementations on today's most advanced GPU hardware.

### 🤖 AI 总结

**一句话总结**：AVO 将进化搜索中的变异/交叉等算子替换为可自我驱动的编程智能体，在 B200 上自动演化出比 cuDNN 和 FlashAttention-4 更快的注意力内核。

**研究动机**：传统进化搜索依赖固定算子与手工启发式，难以在高度优化且硬件细节强相关的 GPU kernel 空间中持续挖掘新的微架构级优化；现有“LLM 参与管线”也多局限于生成候选，缺少端到端的自我修复与验证闭环。

**核心方法**：将“变异算子”实现为智能体循环：智能体读取当前谱系/历史、查询领域知识库，并结合编译与运行反馈，迭代执行提出修改、修复、批判审查与验证，从而对 kernel 实现进行可执行的编辑演化；在 Blackwell B200 上对多头注意力进行 7 天连续自治演化，并快速迁移到 GQA。

**主要结论**：AVO 在评测配置上发现的注意力 kernel 最高较 cuDNN 提升约 3.5%、较 FlashAttention-4 提升约 10.5%，且优化可迁移到 grouped-query attention，仅需约 30 分钟适配即可获得最高较 cuDNN 7.0%、较 FlashAttention-4 9.3% 的增益，表明“智能体式变异算子”能超越以专家为主的 SOTA 实现并挖掘关键微优化。

**关键词**：代理式变异算子, 自主进化搜索, 进化算法变异算子, LLM 编码代理, 执行反馈驱动优化, 内核自动优化, 注意力算子内核, GPU 微架构优化, 跨任务迁移优化

**评分**：57

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24517v1) | [下载PDF](https://arxiv.org/pdf/2603.24517v1.pdf)

---

## [27. Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs](https://arxiv.org/abs/2603.24511v1)

**作者**：Alexander Panfilov, Peter Romov, Igor Shilov 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.CR  
**发布时间**：2026-03-25

### 📄 论文摘要

LLM agents like Claude Code can not only write code but also be used for autonomous AI research and engineering \citep{rank2026posttrainbench, novikov2025alphaevolve}. We show that an \emph{autoresearch}-style pipeline \citep{karpathy2026autoresearch} powered by Claude Code discovers novel white-box adversarial attack \textit{algorithms} that \textbf{significantly outperform all existing (30+) methods} in jailbreaking and prompt injection evaluations.   Starting from existing attack implementations, such as GCG~\citep{zou2023universal}, the agent iterates to produce new algorithms achieving up to 40\% attack success rate on CBRN queries against GPT-OSS-Safeguard-20B, compared to $\leq$10\% for existing algorithms (\Cref{fig:teaser}, left).   The discovered algorithms generalize: attacks optimized on surrogate models transfer directly to held-out models, achieving \textbf{100\% ASR against Meta-SecAlign-70B} \citep{chen2025secalign} versus 56\% for the best baseline (\Cref{fig:teaser}, middle). Extending the findings of~\cite{carlini2025autoadvexbench}, our results are an early demonstration that incremental safety and security research can be automated using LLM agents. White-box adversarial red-teaming is particularly well-suited for this: existing methods provide strong starting points, and the optimization objective yields dense, quantitative feedback. We release all discovered attacks alongside baseline implementations and evaluation code at https://github.com/romovpa/claudini.

### 🤖 AI 总结

**一句话总结**：论文提出并验证了一条由Claude Code驱动的“自动研究（autoresearch）”管线，能自动发现新的白盒LLM对抗攻击算法，在越狱与提示注入评测上显著超越30+既有方法。

**研究动机**：现有LLM红队对抗方法迭代主要依赖人工研究，速度慢且难以系统性探索；而白盒攻击具备可优化的明确目标与密集反馈，适合用LLM代理自动化做增量安全研究。

**核心方法**：以现有攻击实现（如GCG）为起点，让Claude Code在autoresearch循环中持续修改/组合/重写攻击算法，并用定量指标（攻击成功率ASR）在替代模型上优化、再迁移到未见模型进行评测对比。

**主要结论**：自动发现的攻击在CBRN等高风险查询上将ASR提升到最高约40%（相对既有方法≤10%），并展现强迁移性（对Meta-SecAlign-70B达到100% ASR，优于最佳基线56%）；作者开源了新攻击、基线与评测代码，表明LLM代理可在安全攻防研究中产生实质性算法进展。

**关键词**：自动化AI研究, 白盒攻击, 越狱攻击, 提示注入, 红队测试, 迁移攻击, 替代模型优化, 攻击成功率（ASR）

**评分**：55

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24511v1) | [下载PDF](https://arxiv.org/pdf/2603.24511v1.pdf)

---

## [28. Towards Safe Learning-Based Non-Linear Model Predictive Control through Recurrent Neural Network Modeling](https://arxiv.org/abs/2603.24503v1)

**作者**：Mihaela-Larisa Clement, Mónika Farsang, Agnes Poks 等 7 位作者  
**分类**：cs.LG, cs.RO, eess.SY  
**发布时间**：2026-03-25

### 📄 论文摘要

The practical deployment of nonlinear model predictive control (NMPC) is often limited by online computation: solving a nonlinear program at high control rates can be expensive on embedded hardware, especially when models are complex or horizons are long. Learning-based NMPC approximations shift this computation offline but typically demand large expert datasets and costly training. We propose Sequential-AMPC, a sequential neural policy that generates MPC candidate control sequences by sharing parameters across the prediction horizon. For deployment, we wrap the policy in a safety-augmented online evaluation and fallback mechanism, yielding Safe Sequential-AMPC. Compared to a naive feedforward policy baseline across several benchmarks, Sequential-AMPC requires substantially fewer expert MPC rollouts and yields candidate sequences with higher feasibility rates and improved closed-loop safety. On high-dimensional systems, it also exhibits better learning dynamics and performance in fewer epochs while maintaining stable validation improvement where the feedforward baseline can stagnate.

### 🤖 AI 总结

**一句话总结**：提出一种参数跨预测时域共享的序列式神经策略（Sequential-AMPC）来近似NMPC，并通过在线安全评估与回退机制实现更安全、数据更高效的学习型控制部署。

**研究动机**：传统NMPC在线求解非线性规划在高控制频率、复杂模型或长时域下计算开销过大，难以在嵌入式硬件部署；而学习式近似往往需要大量专家MPC数据与高昂训练成本且安全性不足。

**核心方法**：设计Sequential-AMPC：用递归/序列结构的神经网络策略生成整段候选控制序列，并在预测时域内共享参数以提升样本效率与泛化；部署时构建Safe Sequential-AMPC，通过在线可行性/安全检查与必要时回退到安全备选策略来保障闭环安全。

**主要结论**：在多项基准上，相比朴素的逐时域前馈策略，Sequential-AMPC用更少的专家rollout即可学到更高可行率的候选序列并提升闭环安全；在高维系统上其学习更稳定、收敛更快、所需训练轮次更少且验证性能持续改进。

**关键词**：非线性模型预测控制（NMPC）, 学习型MPC近似, 递归神经网络（RNN）建模, 序列神经策略, 预测时域参数共享, 安全增强在线评估, 安全回退机制, 可行性率, 专家MPC轨迹采样效率, 嵌入式实时控制, 高维动力系统控制

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24503v1) | [下载PDF](https://arxiv.org/pdf/2603.24503v1.pdf)

---

## [29. Project and Generate: Divergence-Free Neural Operators for Incompressible Flows](https://arxiv.org/abs/2603.24500v1)

**作者**：Xigui Li, Hongwei Zhang, Ruoxi Jiang 等 9 位作者  
**分类**：cs.LG, physics.flu-dyn  
**发布时间**：2026-03-25

### 📄 论文摘要

Learning-based models for fluid dynamics often operate in unconstrained function spaces, leading to physically inadmissible, unstable simulations. While penalty-based methods offer soft regularization, they provide no structural guarantees, resulting in spurious divergence and long-term collapse. In this work, we introduce a unified framework that enforces the incompressible continuity equation as a hard, intrinsic constraint for both deterministic and generative modeling. First, to project deterministic models onto the divergence-free subspace, we integrate a differentiable spectral Leray projection grounded in the Helmholtz-Hodge decomposition, which restricts the regression hypothesis space to physically admissible velocity fields. Second, to generate physically consistent distributions, we show that simply projecting model outputs is insufficient when the prior is incompatible. To address this, we construct a divergence-free Gaussian reference measure via a curl-based pushforward, ensuring the entire probability flow remains subspace-consistent by construction. Experiments on 2D Navier-Stokes equations demonstrate exact incompressibility up to discretization error and substantially improved stability and physical consistency.

### 🤖 AI 总结

**一句话总结**：提出“投影+生成”统一框架，将不可压缩约束作为硬约束嵌入神经算子与生成模型中，实现（离散误差范围内）严格无散度并提升长期稳定性。

**研究动机**：现有学习流体模型多在无约束函数空间中回归/生成，容易产生非物理的散度误差并在长时预测中崩溃；惩罚项仅提供软约束，缺乏结构性保证。

**核心方法**：对确定性预测，在频谱域引入可微的 Leray 投影（基于 Helmholtz–Hodge 分解）把模型输出/假设空间直接限制到无散度子空间；对生成建模，指出仅投影输出不足以修正不兼容先验，因而通过“curl 推前”构造无散度高斯参考测度，使整个概率流在构造上始终保持子空间一致。

**主要结论**：在2D Navier–Stokes实验中，该方法将不可压缩性满足到离散精度，并显著减少伪散度、提升数值稳定性与物理一致性，优于仅用惩罚或事后投影的做法。

**关键词**：不可压缩流, 散度自由约束, 神经算子, 谱方法, 可微分投影, 生成建模, 散度自由高斯先验, curl 推前映射

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24500v1) | [下载PDF](https://arxiv.org/pdf/2603.24500v1.pdf)

---

## [30. Uniform Laws of Large Numbers in Product Spaces](https://arxiv.org/abs/2603.24493v1)

**作者**：Ron Holzman, Shay Moran, Alexander Shlimovich  
**分类**：cs.LG, math.ST  
**发布时间**：2026-03-25

### 📄 论文摘要

Uniform laws of large numbers form a cornerstone of Vapnik--Chervonenkis theory, where they are characterized by the finiteness of the VC dimension. In this work, we study uniform convergence phenomena in cartesian product spaces, under assumptions on the underlying distribution that are compatible with the product structure. Specifically, we assume that the distribution is absolutely continuous with respect to the product of its marginals, a condition that captures many natural settings, including product distributions, sparse mixtures of product distributions, distributions with low mutual information, and more.   We show that, under this assumption, a uniform law of large numbers holds for a family of events if and only if the linear VC dimension of the family is finite. The linear VC dimension is defined as the maximum size of a shattered set that lies on an axis-parallel line, namely, a set of vectors that agree on all but at most one coordinate. This dimension is always at most the classical VC dimension, yet it can be arbitrarily smaller. For instance, the family of convex sets in $\mathbb{R}^d$ has linear VC dimension $2$, while its VC dimension is infinite already for $d\ge 2$. Our proofs rely on estimator that departs substantially from the standard empirical mean estimator and exhibits more intricate structure. We show that such deviations from the standard empirical mean estimator are unavoidable in this setting. Throughout the paper, we propose several open questions, with a particular focus on quantitative sample complexity bounds.

### 🤖 AI 总结

**一句话总结**：在满足“分布相对其边缘分布乘积绝对连续”的乘积空间中，事件族满足一致大数定律当且仅当其“线性VC维”有限。

**研究动机**：经典VC理论用VC维刻画一致收敛，但在笛卡尔乘积结构下（如近似独立、低互信息、稀疏乘积分布混合）这种刻画可能过于粗糙，需要与轴向结构相匹配的新复杂度度量与一致收敛判据。

**核心方法**：假设总体分布对各边缘分布乘积绝对连续，并引入线性VC维（只在“轴平行直线/仅一维可变”的点集上考察可打散性）来刻画复杂度；证明中构造了不同于经验均值的更复杂估计器，并论证在该设定下偏离经验均值是不可避免的。

**主要结论**：在上述分布假设下，一致大数定律对事件族成立的充要条件是线性VC维有限；该维度不超过经典VC维且可显著更小（如R^d中的凸集线性VC维为2而VC维在d≥2时已无穷），并提出样本复杂度定量界等开放问题。 

**关键词**：一致大数定律, 一致收敛, VC 理论, VC 维, 线性 VC 维, 笛卡尔积空间, 边缘分布乘积, 绝对连续性, 稀疏乘积分布混合, 样本复杂度, 非经验均值估计器

**评分**：13

**论文链接**：[查看原文](https://arxiv.org/abs/2603.24493v1) | [下载PDF](https://arxiv.org/pdf/2603.24493v1.pdf)

---

