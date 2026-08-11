# arXiv AI 论文日报 | 2026-08-11

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (9 篇)
- [cs.CL](#csCL) (8 篇)
- [cs.AI](#csAI) (7 篇)
- [cs.LG](#csLG) (6 篇)

---

## cs.AI

## [1. GENCO - A Unified Neural Solver Embedded in a Development Framework for Steady-State Grid Analysis](https://arxiv.org/abs/2608.09921v1)

**作者**：Alban Puech, Matteo Mazzonelli, Tamara R. Govindasamy 等 22 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-10

### 📄 论文摘要

Foundation models are transforming business workflows and boosting productivity, yet they remain largely absent from engineering domains such as power system analysis, where strict physical consistency must be enforced.   We present GENCO (GEometric Neural Corrective Optimizer), a unified neural solver for steady-state transmission grid analysis that handles power flow (PF), optimal power flow (OPF), and state estimation (SE) within a single architecture and shared network representation. To support advances in neural power system solvers, we introduce the open-source GridFM Development Framework, which standardizes synthetic data generation and training in a low-code environment. We also release large-scale datasets with millions of PF and OPF scenarios across diverse grid topologies to support reproducible benchmarking.   We evaluate GENCO on the PFDelta and OPFData benchmarks against state-of-the-art neural solvers and classical solvers, including Newton-Raphson and IPOPT, as well as on real-world Hydro-Québec SCADA data. For large-scale PF, GENCO recovers the full AC operating state, including voltage magnitudes and reactive power that DC-PF cannot provide, while matching DC-PF-level active power-balance residuals. It achieves up to 30x speedups over Newton-Raphson at only 2x the runtime of DC-PF. For OPF, it achieves up to 85x speedups over IPOPT while improving feasibility, optimality, and runtime over DC-OPF. For SE, GENCO is more robust than classical weighted least squares to noisy measurements and network parameter errors, and always returns a high-quality estimate even when weighted least squares fails to converge.   Together, the unified architecture and development framework provide a new approach to large-scale steady-state grid analysis, lowering the barrier to entry for power system engineers and marking a step toward Grid Foundation Models.

### 🤖 AI 总结

**一句话总结**：Foundation models are transforming business workflows and boosting productivity, yet they remain largely absent from engineering domains such as power system analysis, where strict physical consistenc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GENCO, Unified, Neural, Solver, Embedded, Development, Framework, Steady-State

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09921v1) | [下载PDF](https://arxiv.org/pdf/2608.09921v1.pdf)

---

## [2. SHE: Trajectory-driven Safety Harness Evolution for LLM Agents](https://arxiv.org/abs/2608.09885v1)

**作者**：Wanying Qu, Qinghua Mao, Yu Li 等 15 位作者  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-08-10

### 📄 论文摘要

The safety of large language model (LLM) agents depends not only on model weights but also on the agent harness that manages context, memory, tools, permissions, and runtime control. Existing safety mechanisms often treat the harness as a fixed deployment artifact, limiting their ability to evolve with emerging risks. Moreover, coupled functions across harness components obscure safety responsibility attribution, making localized evolution difficult. We propose Safety Harness Evolution (SHE), a framework that learns evolving safe boundaries from rollout trajectories. SHE decomposes the harness into four artifacts with explicit safety responsibilities, including the System Prompt, Rule Bank, Safety Memory, and Tool Policy, defining clear functional boundaries for localized evolution. Based on this decomposition, SHE introduces an attribution-guided evolution loop that converts trajectory failures into structured diagnoses, learns artifact-specific boundary refinements, and selects evolved harnesses through safety-utility validation. Experiments on Agent-SafetyBench demonstrate that SHE effectively enhances safety through harness evolution, achieving a 3.1x ASR reduction compared with static SafeHarness, while also improving benign utility. The evolved harness further generalizes to unseen risks on the held-out AgentHarm benchmark and transfers across agent models without additional evolution.

### 🤖 AI 总结

**一句话总结**：The safety of large language model (LLM) agents depends not only on model weights but also on the agent harness that manages context, memory, tools, permissions, and runtime control. Existing safety m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, of, SHE, Trajectory-driven, Safety, Harness, Evolution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09885v1) | [下载PDF](https://arxiv.org/pdf/2608.09885v1.pdf)

---

## [3. ArchAgent v2: A Case Study with the Data Prefetching Championship](https://arxiv.org/abs/2608.09874v1)

**作者**：Abraham Gonzalez, Raghav Gupta, Akanksha Jain 等 15 位作者  
**分类**：cs.AI, cs.AR  
**发布时间**：2026-08-10

### 📄 论文摘要

Agentic artificial intelligence has shown great promise in automating algorithm design, but scaling similar techniques to computer microarchitecture discovery remains challenging due to vast search spaces, strict hardware budgets, and long simulation times. In this work, we present ArchAgent v2, a framework which scales automated microarchitecture search to multi-level data prefetching. While the original ArchAgent successfully discovered single-level cache replacement policies in competition settings, it does not scale to multi-level prefetching where the design space and degrees of freedom are larger. To overcome this, we introduce two new additions to ArchAgent: a cascaded evolutionary search that subdivides the design space by sequentially evolving and freezing prefetchers at individual cache levels, and a hardware-realizability feedback loop that embeds real-time size-estimation directly into the evolution process.   Evaluated under identical rules of the 4th Data Prefetching Championship (DPC4), ArchAgent v2 automatically designs a three-level prefetcher that outperforms the winning hand-designed solution, further demonstrating automated agentic discovery as a useful tool for computer architects. Our discovered policy achieves a 3.8\% geometric mean IPC speedup over the baseline overall and a 0.3\% improvement over the prior champion, BertiGO. On low-bandwidth single-core configurations, our policy yields a 4.6\% performance speedup compared to only 2.6\% for BertiGO. However, multi-core evolution still remains a significant challenge due to simulation latency impeding evolution speed. Finally, our profiling of an ArchAgent evolution of over 12,000 candidate designs provides key insights into how automated evolutionary agents explore and synthesize complex microarchitectural logic.

### 🤖 AI 总结

**一句话总结**：Agentic artificial intelligence has shown great promise in automating algorithm design, but scaling similar techniques to computer microarchitecture discovery remains challenging due to vast search sp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：v2, ArchAgent, Case, Study, Data, Prefetching, Championship, Agentic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09874v1) | [下载PDF](https://arxiv.org/pdf/2608.09874v1.pdf)

---

## [4. Towards Expert-level Medical AI for Real-time Video Consultations](https://arxiv.org/abs/2608.09861v1)

**作者**：Mahvish Nagda, Jihyeon Lee, Matthew Thompson 等 40 位作者  
**分类**：cs.AI, cs.CL, cs.CV  
**发布时间**：2026-08-10

### 📄 论文摘要

Audio-visual interaction is the standard for patient-physician consultations, enabling natural communication and effective assessment of illness through non-verbal cues. While text-based AI has shown promise, it discards essential perceptual dimensions and limits patients who cannot articulate symptoms in writing. Early efforts to extend medical AI to audio-visual interaction have demonstrated feasibility but not reached clinician-level performance. Here, we provide the first demonstration of expert-level AI in real-time clinical video consultations using AMIE (Articulate Medical Intelligence Explorer) in a video configuration. AMIE (Video) is a Gemini-based multi-agent system integrating low-latency dialogue, clinical reasoning, and real-time audio-visual perception. To guide development, we established a taxonomy and automated evaluations for clinical audio-visual cues in telehealth settings. In a randomized Objective Structured Clinical Examination (OSCE) study with 30 primary care physicians (PCPs), 15 patient actors and 100 clinical scenarios, we compared AMIE (Video), its text-only counterpart AMIE (Text), and PCPs consulting via video. Clinical evaluators rated AMIE (Video) on par or better than PCPs in history-taking, diagnosis, management, and physical observation and examination. Patient actors preferred AMIE's approach to assessing and explaining conditions, while PCPs were preferred for rapport and partnership building. In modality ablation, patient actors preferred AMIE (Video)'s interface over text chat for communicative effectiveness, convenience, and feeling understood. Limitations remain in fine anatomical precision, subtle affective nuances, and high-frequency movements. While further research is needed before real-world translation, these results mark an important milestone toward AI systems capable of augmenting care across the sensory complexity of clinical practice.

### 🤖 AI 总结

**一句话总结**：Audio-visual interaction is the standard for patient-physician consultations, enabling natural communication and effective assessment of illness through non-verbal cues. While text-based AI has shown ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Towards, Expert-level, Medical, Real-time, Video, Consultations, Audio-visual, interaction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09861v1) | [下载PDF](https://arxiv.org/pdf/2608.09861v1.pdf)

---

## [5. Agentic Auto-Research is Fuzz Testing](https://arxiv.org/abs/2608.09855v1)

**作者**：Yifeng He, Jicheng Wang, Yinzhe Zhao 等 5 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-08-10

### 📄 论文摘要

Autonomous research agents can generate experiments faster than researchers can validate them. Researchers have responded by scaling the proposer and ranking more samples with a learned judge or human reviewers. We argue that this *generate-and-rank* paradigm misses the problem of sparse feedback. Within a declared research problem, an agent follows the control loop of a greybox fuzzer: it proposes a candidate, executes it, observes feedback, and chooses what to try next. A fuzzer rarely finds a bug, but coverage makes partial progress observable on every execution. Fuzzers then use that signal to mutate inputs and allocate effort, rather than only to rank completed runs. Auto-research needs the same two capabilities. First, each experiment should expose a cheap, dense signal of epistemic progress before final scientific validation is available. Second, that signal should determine the next intervention so that the agent searches rather than repeatedly samples. Because the optimized progress signal is guidance rather than a verdict, final validation must still decide what counts as a discovery using evidence protected from adaptive reuse. We propose controlled tests of whether candidate signals predict validated progress, whether feedback-directed search yields more validated discoveries per unit cost than repeated sampling, and whether protected validation reduces false discoveries. Feedback architecture, not only generation, is a central bottleneck in auto-research.

### 🤖 AI 总结

**一句话总结**：Autonomous research agents can generate experiments faster than researchers can validate them. Researchers have responded by scaling the proposer and ranking more samples with a learned judge or human...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Agentic, Auto-Research, Fuzz, Testing, Autonomous, research, can

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09855v1) | [下载PDF](https://arxiv.org/pdf/2608.09855v1.pdf)

---

## [6. CARD: Controlled Agentic Reddit Discussions for Credit Card Simulation](https://arxiv.org/abs/2608.09790v1)

**作者**：Yaoning Yu, Kai-Min Chang, Ye Yu 等 6 位作者  
**分类**：cs.AI, cs.MA, cs.SI  
**发布时间**：2026-08-10

### 📄 论文摘要

Online credit card discussions provide a natural setting for studying how consumers communicate about financial products. Simulating these discussions requires more than just generating individual comments, the generated threads should also match how real users express themselves and interact with others. We introduce CARD, a framework for generating realistic credit card discussion threads. Given a credit card post and its matched real thread, CARD uses non-verbatim guidance on reply structure, comment function, stance, tone, and conversational variation. A planner organizes these controls, a writer generates the discussion, and a calibration loop updates comments' populations that contribute to differences between the generated and real thread distributions. We evaluate CARD on real Reddit credit card discussions using lexical, semantic, behavioral, and structural metrics. CARD matches the distributions of real credit card discussions better than simulation baselines across multiple LLMs and also demonstrates smaller effect sizes and distribution distances across metrics. These results show that structured planning and targeted revision can generate the realism of simulated credit card discussions.

### 🤖 AI 总结

**一句话总结**：Online credit card discussions provide a natural setting for studying how consumers communicate about financial products. Simulating these discussions requires more than just generating individual com...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CARD, Controlled, Agentic, Reddit, Discussions, Credit, Simulation, Online

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09790v1) | [下载PDF](https://arxiv.org/pdf/2608.09790v1.pdf)

---

## [7. AirFlow: Context Preserving and Multi-Rate State Modeling for Air Quality Forecasting](https://arxiv.org/abs/2608.09775v1)

**作者**：Fan Yang, Nan Chen, Yijie Dong 等 5 位作者  
**分类**：cs.AI, cs.CE, cs.LG  
**发布时间**：2026-08-10

### 📄 论文摘要

Accurate air quality forecasting is essential for public health and urban environmental management, but remains challenging because pollutant channels differ in periodicity and distribution drift, while their concentration trajectories contain both multi-scale dependencies and rapid changes. Recent methods have improved spatial dependency learning and meteorological covariate modeling. However, pollutant channels are still passed through the same normalization rule and temporal backbone, using a shared latent representation for channel-specific distributions and changes at different rates. To address this limitation, we propose AirFlow, a pollutant-aware dual-stream framework that operates on station multivariate observations without additional graph propagation or predefined signal decomposition. Specifically, AirFlow designs two novel blocks: (1) a statistic-guided normalization routing mechanism that selects a normalization path for each pollutant according to its 24-hour autocorrelation and distribution drift; and (2) a hierarchical dual-stream state model that combines multi-scale state space propagation with learnable response coefficients, where gated bidirectional cross-attention exchanges information and adaptively fuses the resulting representations. Experiments on real-world data from multiple cities show that AirFlow achieves the best performance in 34 of 36 metrics comparisons, with reductions of up to 11.11% root mean square error over the state-of-the-art baseline. AirFlow also requires only 0.0483M parameters and 0.0215G FLOPs, achieving high forecasting accuracy with low computational overhead.

### 🤖 AI 总结

**一句话总结**：Accurate air quality forecasting is essential for public health and urban environmental management, but remains challenging because pollutant channels differ in periodicity and distribution drift, whi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AirFlow, Context, Preserving, Multi-Rate, State, Modeling, Air, Quality

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09775v1) | [下载PDF](https://arxiv.org/pdf/2608.09775v1.pdf)

---

## cs.CL

## [8. From Values to Benchmarks: Evaluating Large Language Models for Governmental Use in Dutch](https://arxiv.org/abs/2608.09925v1)

**作者**：Laurens Samson, Iva Gornishka, Gossa Lô 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-10

### 📄 论文摘要

Large language models are increasingly being deployed in governmental settings, yet few existing evaluation frameworks jointly reflect the values of public administration and the linguistic requirements of non-English contexts. We present the "Grip on LLMs" framework, a systematic evaluation suite for Dutch governmental use developed in collaboration with domain experts from a major Dutch municipal organisation. Through an advisory board process, user research, and a survey of the users of a civil-servant chatbot, we identify six evaluation dimensions (factuality, honesty, social bias, energy consumption, cost, and training data transparency) and operationalise them into a benchmark suite covering more than 30 multilingual and Dutch-specific models. Our results reveal that no single model excels across all dimensions, and that trade-offs are unavoidable: higher quality consistently comes at greater environmental impact and financial cost, while bias remains largely independent of both. We further find that factuality (whether a model answers correctly) and honesty (whether a model acknowledges what it does not know) are governed by distinct properties, with high factuality not implying high honesty. To make these findings actionable for non-technical audiences, we release a publicly accessible, user-friendly model overview designed for the full range of stakeholders involved in governmental LLM selection, from engineers to policymakers.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly being deployed in governmental settings, yet few existing evaluation frameworks jointly reflect the values of public administration and the linguistic requiremen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Values, Benchmarks, Evaluating, Large, Language, Models, Governmental, Use

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09925v1) | [下载PDF](https://arxiv.org/pdf/2608.09925v1.pdf)

---

## [9. Fusion Training for Mathematical Generalization in Large Language Models](https://arxiv.org/abs/2608.09893v1)

**作者**：Congfeng Cao, Pengyu Zhang, Jelke Bloem  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-10

### 📄 论文摘要

Thinking Mode Fusion (TMF) enables large language models to support both concise responses and long-form reasoning by unifying a non-thinking mode and a thinking mode within a single model. However, its training dynamics, including the \emph{data ratio} and \emph{training schedule} between the two modes, remain underexplored. In this work, we present a systematic study of TMF by analyzing the effects of the training schedule and data ratio between thinking and non-thinking modes. Focusing on mathematical problem solving, we construct a benchmark with multiple thinking-to-non-thinking data ratios and three training schedules. Our results reveal an asymmetric interaction between the two modes: increasing the ratio of non-thinking supervision reduces the accuracy of the thinking mode. We further show that different training schedules modulate this trade-off and that the optimal schedule depends on the data ratio. Finally, we quantify a negative correlation between non-thinking and thinking mode supervision, highlighting an inherent tension between these two modes. These findings provide practical guidance for designing effective TMF training settings. All code and data are released to support further research at: \href{https://github.com/caocongfeng/Fusion-Bench.git}{\textbf{Fusion Bench}}.

### 🤖 AI 总结

**一句话总结**：Thinking Mode Fusion (TMF) enables large language models to support both concise responses and long-form reasoning by unifying a non-thinking mode and a thinking mode within a single model. However, i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Fusion, Training, Mathematical, Generalization, Large, Language, Models, Thinking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09893v1) | [下载PDF](https://arxiv.org/pdf/2608.09893v1.pdf)

---

## [10. RA-FinBERT: Rule-aware LoRA adaptation for low-resource financial sentiment classification](https://arxiv.org/abs/2608.09834v1)

**作者**：Fan Zhang, Jiaming Li  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-08-10

### 📄 论文摘要

Financial sentiment analysis converts unstructured financial news into quantitative signals that can support market analysis and decision-making. Existing work on resource-efficient financial NLP has largely focused on compressing or adapting pretrained language models, with less attention to combining contextual representations with lightweight rule-derived features. This study develops Rule-Aware FinBERT (RA-FinBERT), a parameter-efficient framework that integrates low-rank adaptation (LoRA) with three continuous VADER-derived sentiment proportions (positive, negative, and neutral) and a source-level metadata feature. The standardized four-dimensional feature vector is directly concatenated with the 768-dimensional final-layer FinBERT [CLS] representation and passed through a lightweight classification head. This design introduces only 1,024 additional trainable weights relative to a structurally matched text-only FinBERT model. RA-FinBERT was evaluated against text-only FinBERT and a lightweight DistilBERT baseline for three-class sentiment classification of financial-news titles and descriptions. On the held-out test set, RA-FinBERT achieved 69.89% accuracy and a macro F1 score of 0.634, compared with 63.44% and 0.526 for text-only FinBERT. Neutral-class recall increased from 18.18% to 45.45%. The framework supports both CPU and GPU execution, offering a lightweight and practical approach to financial sentiment classification under constrained computational resources. These findings indicate that rule-derived sentiment information and source metadata can provide complementary signals to contextual FinBERT representations and improve performance with minimal additional model complexity.

### 🤖 AI 总结

**一句话总结**：Financial sentiment analysis converts unstructured financial news into quantitative signals that can support market analysis and decision-making. Existing work on resource-efficient financial NLP has ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RA-FinBERT, Rule-aware, LoRA, adaptation, low-resource, financial, sentiment, classification

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09834v1) | [下载PDF](https://arxiv.org/pdf/2608.09834v1.pdf)

---

## [11. SWE-Bench ProMax: Benchmarking Agents on Large-Scale Multilingual Code Refactoring](https://arxiv.org/abs/2608.09802v1)

**作者**：Yuling Shi, Jinghan Xu, Kelin Fu 等 15 位作者  
**分类**：cs.CL, cs.SE  
**发布时间**：2026-08-10

### 📄 论文摘要

As AI coding agents take on increasingly complex, long-horizon software engineering tasks, existing benchmarks are rapidly saturating and their evaluation quality has come under serious scrutiny: a recent audit found that nearly 60% of unsolved SWE-bench Verified instances contain flawed tests -- either overly narrow tests that reject correct solutions or overly broad tests that check unstated requirements -- and that frontier models can verbatim reproduce gold patches from training data. Code refactoring, which requires coordinated, behavior-preserving changes across many files, offers a substantially harder and more realistic test of agent capability, yet remains underserved by current benchmarks. We introduce SWE-Bench ProMax, an expert-curated, multilingual code refactoring benchmark of 170 instances drawn from real commits across seven programming languages (Python, Java, TypeScript, Go, C, C++, and Rust). Every instance undergoes rigorous, multi-stage curation that directly addresses the quality problems identified in prior benchmarks: issue descriptions are rewritten from scratch to provide precise, unambiguous specifications, and test suites are manually reviewed to remove overly narrow and overly broad tests. Tasks with insufficient complexity or limited cross-file scope are filtered out, yielding a benchmark of challenging, large-scale refactoring tasks that average 11.4 modified files and 261.6 lines of code per instance, substantially exceeding the scale of existing benchmarks. Experiments with frontier models under two agent scaffolds show that the best model achieves only 41.2% resolve rate, confirming that SWE-Bench ProMax presents a meaningful and unsaturated challenge for current AI coding agents. Our benchmark is available at https://huggingface.co/datasets/swe-bench-promax/SWE-Bench-ProMax.

### 🤖 AI 总结

**一句话总结**：As AI coding agents take on increasingly complex, long-horizon software engineering tasks, existing benchmarks are rapidly saturating and their evaluation quality has come under serious scrutiny: a re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SWE-Bench, ProMax, Benchmarking, Large-Scale, Multilingual, Code, Refactoring

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09802v1) | [下载PDF](https://arxiv.org/pdf/2608.09802v1.pdf)

---

## [12. Comparing British and American Audio Description of Movies](https://arxiv.org/abs/2608.09792v1)

**作者**：Igor Sterner, Alex Lascarides, Frank Keller  
**分类**：cs.CL  
**发布时间**：2026-08-10

### 📄 论文摘要

Narrating the visual component of movies is known as audio description. It is a narrative technique designed to enable blind and visually impaired individuals to follow the story. However, it is far more constrained than most narratives: the descriptions not only need to convey the story in the movie, but they must also fit into gaps between dialogue and they need to conform to guidelines that exist in each region. In this work, we compare audio description created in the United Kingdom against audio description created in the United States. We use guidelines written for these two regions, alongside the impressions from a practitioner in the field, to motivate specific hypotheses about the differences. We test these hypotheses against our pre-existing corpus, which provides both human-authored American and British audio description for each of 206 movies. Results provide quantitative evidence to uphold all tested hypotheses, including differences in lexicon, the use of the progressive aspect, the use of passive constructions, the use of subjective adjectives and modifiers, when characters are named, how scenes are cued, and degree of overlap with movie dialogue and music. Our work offers a quantitative lens into the narrative technique of audio description.

### 🤖 AI 总结

**一句话总结**：Narrating the visual component of movies is known as audio description. It is a narrative technique designed to enable blind and visually impaired individuals to follow the story. However, it is far m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Comparing, British, American, Audio, Movies, Narrating, visual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09792v1) | [下载PDF](https://arxiv.org/pdf/2608.09792v1.pdf)

---

## [13. KGCaRe: Explainable Complex Conditional Question Answering using Automatic Knowledge Graph Construction and Context Retrieval with LLMs](https://arxiv.org/abs/2608.09779v1)

**作者**：Ghanshyam Verma, Simanta Sarkar, Devishree Pillai 等 9 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-10

### 📄 论文摘要

Answering complex conditional questions using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) remains a challenge, particularly in domain-specific contexts where general-purpose LLMs and RAG tend to underperform. We hypothesize that augmenting RAG with unstructured and structured knowledge, extracted from both documents and knowledge graphs (KGs), can improve reasoning and answer accuracy for such tasks.   To test this, we propose KGCaRe, a hybrid approach that combines neural retrieval with symbolic reasoning over LLM-generated KGs. KGCaRe constructs a KG from documents using a multi-prompt extraction strategy and stores it in a graph database. Simultaneously, the documents are embedded into a vector store to enable neural retrieval. KGCaRe performs innovative iterative graph traversal guided by the LLM to extract relevant triples, prune irrelevant information, and uses additional clue entities to traverse the graph again if the initial traversal does not provide satisfactory context to generate the answer. The relevant triples extracted from the KG in path form, along with semantically retrieved text passages, are then fed into custom KGCaRe prompts to generate answers to the complex conditional questions with explanations.   We evaluate KGCaRe on two complex conditional QA datasets. Our results on these datasets show that KGCaRe consistently outperforms existing baselines, including Vanilla LLM, Code Prompt, Text Prompt, Think-on-Graph, Vanilla RAG, and HybridContextQA, across multiple LLMs such as Mistral, Mixtral, GPT-3.5, and GPT-4o. We publicly release the software pipeline that we developed to implement the proposed KGCaRe approach.

### 🤖 AI 总结

**一句话总结**：Answering complex conditional questions using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) remains a challenge, particularly in domain-specific contexts where general-purpose ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：KGCaRe, Explainable, Complex, Conditional, Question, Answering, Automatic, Knowledge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09779v1) | [下载PDF](https://arxiv.org/pdf/2608.09779v1.pdf)

---

## [14. PragMatch: Separating Pragmatic Incongruity from Cross-Modal Mismatch in Large Vision-Language Models](https://arxiv.org/abs/2608.09772v1)

**作者**：Zhanna Mukhametsharip, Vera Demberg, Varsha Suresh  
**分类**：cs.CL  
**发布时间**：2026-08-10

### 📄 论文摘要

Large Vision-Language Models (LVLMs) have demonstrated strong performance on multimodal benchmarks, yet it remains unclear whether they genuinely reason about relationships between images and text or rely on superficial correlations, known as shortcut learning. This question is particularly important for multimodal sarcasm detection, where successful prediction depends on recognizing pragmatic incongruity rather than treating sarcasm as simple image-text mismatch. We introduce PragMatch, a controlled benchmark of 3,000 image-text pairs derived from MMSD2.0, including original sarcastic examples and constructed literal and hard-negative pairs. We identify influential shortcut cues through systematic masking and evaluate their impact through targeted injection experiments. Our results show that LVLM predictions are sensitive to lexical, OCR-derived and stylistic cues, with injected surface signals causing substantial changes in model predictions despite unchanged underlying image-text relationships. Our findings reveal limitations in current LVLMs while PragMatch provides a systematic testbed for evaluating multimodal pragmatic reasoning beyond surface-level image-text alignment.

### 🤖 AI 总结

**一句话总结**：Large Vision-Language Models (LVLMs) have demonstrated strong performance on multimodal benchmarks, yet it remains unclear whether they genuinely reason about relationships between images and text or ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PragMatch, Separating, Pragmatic, Incongruity, Cross-Modal, Mismatch, Large, Vision-Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09772v1) | [下载PDF](https://arxiv.org/pdf/2608.09772v1.pdf)

---

## [15. Structured Phonological Representations for Audio-Articulatory rtMRI Speech Classification](https://arxiv.org/abs/2608.09767v1)

**作者**：Abner Hernandez, Tomás Arias Vergara, Daiqi Liu 等 5 位作者  
**分类**：cs.CL, cs.SD, eess.AS  
**发布时间**：2026-08-10

### 📄 论文摘要

Real-time MRI makes it possible to observe vocal-tract articulation during speech, but mapping these articulatory patterns to phonetic and phonological categories remains challenging. We investigate whether PhonoQ, an audio-based model trained to recognize structured phonological features, provides useful information for audio--articulatory modeling. Specifically, we extract representations from PhonoQ's Conformer module, whose training is shaped by supervision for manner, place, voicing, and vowel features. Using articulatory contours with synchronized audio-derived features, we compare WavLM-large and HuBERT-large baselines with models that incorporate PhonoQ-derived representations. Across unseen-speech and unseen-subject settings, these features improve macro-F1 for phonological targets including manner, place, voicing, vowel height, and vowel backness, and also improve fine-grained 39-phoneme classification. In a contour-only inference setting, audio-derived teacher supervision yields modest but consistent gains over contour-only training, indicating that phonological information from synchronized audio can be partially transferred to articulatory models. Finally, posterior analyses show interpretable surface-sensitive patterns consistent with flapping-like /t/ realizations, /t/-/r/ retraction or affrication, and nasal place assimilation.

### 🤖 AI 总结

**一句话总结**：Real-time MRI makes it possible to observe vocal-tract articulation during speech, but mapping these articulatory patterns to phonetic and phonological categories remains challenging. We investigate w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Structured, Phonological, Representations, Audio-Articulatory, rtMRI, Speech, Classification, Real-time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09767v1) | [下载PDF](https://arxiv.org/pdf/2608.09767v1.pdf)

---

## cs.CV

## [16. Learning How the World Evolves: Extrapolative Video World Models via Latent Dynamics Reasoning](https://arxiv.org/abs/2608.09926v1)

**作者**：Haodong Li, Shaoteng Liu, Tianyu Wang 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-10

### 📄 论文摘要

The world evolves following its dynamics, i.e., its laws of motion. However, leading video diffusion models largely fit the pixels without modeling how the pixels transit over time. Thus, they render visually plausible frames but may not accurately obey the laws. To capture the dynamics purely from pixels, we introduce Latent Dynamics Reasoning (LDR). LDR casts the latent transition as an explicit kinematic integration, where the lower-order dynamics are integrated numerically and the model regresses only the third- and higher-order residual that drives the rollout. For this integration to extrapolate better, LDR runs it on a structured latent rather than dense convolutional features. Following PhyWorld, we validate LDR on a controlled white-box physics benchmark spanning five tasks (uniform motion, parabola, collision, bouncing, looming), focusing on out-of-distribution scenarios that reveal whether a model has truly learned the underlying dynamics. LDR extrapolates the learned dynamics far better: the gap between its in- and out-of-distribution error is over 20$\times$ smaller than the video diffusion baseline's, under both single- and joint-task training at 256$^2$ resolution, while using 26$\times$ fewer parameters and running 143$\times$ faster. LDR can even generalize under severe shift: for example, trained only on red balls moving left-to-right, it correctly predicts the motion of a blue square moving right-to-left. To our knowledge, this is the first video world model that extrapolates learned dynamics beyond its training distribution. Project page: https://lat-dyn-reason.github.io/

### 🤖 AI 总结

**一句话总结**：The world evolves following its dynamics, i.e., its laws of motion. However, leading video diffusion models largely fit the pixels without modeling how the pixels transit over time. Thus, they render ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, How, World, Evolves, Extrapolative, Video, Models, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09926v1) | [下载PDF](https://arxiv.org/pdf/2608.09926v1.pdf)

---

## [17. Beyond Hazard Resemblance: Contrastive Event Adjudication for Training-Free Video Anomaly Detection](https://arxiv.org/abs/2608.09908v1)

**作者**：Wenti Yin, Xiang Wang, Huaxin Zhang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-10

### 📄 论文摘要

Video anomaly detection (VAD) aims to identify and temporally localize abnormal events in videos. Supervised methods learn anomaly decision boundaries from target-domain annotations but require substantial in-domain data. Existing training-free methods leverage the rich semantic knowledge and reasoning capabilities of pretrained models to interpret visual content, yet these capabilities do not directly define an anomaly decision criterion: richer anomaly descriptions better capture hazard resemblance without resolving abnormality. To this end, we propose Contrastive Event Adjudication for training-free Video Anomaly Detection (CEAVAD), which shifts the unit of inference from isolated anomaly concepts to falsifiable event hypotheses and establishes an inference-time explanatory boundary through the interaction between competing explanations and video evidence. Specifically, CEAVAD first uses public-safety knowledge to construct hazard-benign event contrasts, pairing each hazard mechanism with a generic normal account and a mechanism-specific benign counterpart. It then determines whether the target interval better supports a hazard explanation or its benign competitor, yielding a revisable contrastive boundary proposal for the target. Finally, CEAVAD adjudicates between the competing explanations to determine whether the hazard hypothesis survives the video evidence, supporting both temporally localized anomaly detection and evidence-grounded explanations. Experiments on three widely used VAD benchmarks demonstrate that CEAVAD achieves state-of-the-art performance under the training-free paradigm.

### 🤖 AI 总结

**一句话总结**：Video anomaly detection (VAD) aims to identify and temporally localize abnormal events in videos. Supervised methods learn anomaly decision boundaries from target-domain annotations but require substa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Hazard, Resemblance, Contrastive, Event, Adjudication, Training-Free, Video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09908v1) | [下载PDF](https://arxiv.org/pdf/2608.09908v1.pdf)

---

## [18. Space-Creating versus Dead Possession: An Off-Ball Possession-Quality Index for Broadcast Football](https://arxiv.org/abs/2608.09887v1)

**作者**：Seongjin Choi  
**分类**：cs.CV, cs.CY, cs.LG  
**发布时间**：2026-08-10

### 📄 论文摘要

Ball possession is the most-cited and most-misleading number in football: 60% recycled in one's own half is not 60% spent pinning the opponent back. Existing event-based possession-value frameworks (expected threat, VAEP, on-ball value) price on-ball actions but ignore the off-ball question a sterile possession poses: did holding the ball create space, or was the circulation dead? We answer this in two layers. First, an event-side junk-possession index prices each possession sequence by its peak threat gain under an expected-threat grid and -- after reconstructing the live scoreline to exclude lead-protecting circulation -- flags low-threat sequences in tied-or-losing states. On the 2026 FIFA World Cup (103 matches, 206 team-matches) the flag correlates negatively with points (r=-0.37) and xG difference (r=-0.51, partly index-coupled). It is not a repackaging of on-ball value: with team offensive VAEP and field tilt held fixed, the junk flag stays strongly negatively associated with points (p<0.0001, also match-clustered) while VAEP is not significant -- in this same-match (descriptive) regression it adds information beyond this on-ball action-value model. Second, for a flagged window we resolve whether it was spatially dead or space-creating by projecting broadcast video to pitch coordinates and measuring a Space-Creation Index (SCI): a net pitch-control change capturing whether the possession seized space or pushed the opponent's block back. Across 31 of 35 flagged windows from nine World Cup matches (a purposive sample), 74% are spatially non-space-creating, 19% weak progression, and 6% space-creating windows the event flag alone would score as failure -- including a side with 73% of the ball that exited on penalties (two non-creating windows). The two layers separate space-creating-but-unconverted from sterile possession, a distinction event-only on-ball value cannot make.

### 🤖 AI 总结

**一句话总结**：Ball possession is the most-cited and most-misleading number in football: 60% recycled in one's own half is not 60% spent pinning the opponent back. Existing event-based possession-value frameworks (e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Space-Creating, versus, Dead, Possession, Off-Ball, Possession-Quality, Index

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09887v1) | [下载PDF](https://arxiv.org/pdf/2608.09887v1.pdf)

---

## [19. Sci-VBench: Evaluating Knowledge- and Reasoning-Intensive Video Generation in Science Domains](https://arxiv.org/abs/2608.09873v1)

**作者**：Diandian Zhang, Tingyu Song, Lin Fu 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-10

### 📄 论文摘要

We introduce Sci-VBench, a comprehensive benchmark for evaluating knowledge- and reasoning-intensive video generation across scientific domains. It contains 1,253 expert-annotated examples spanning 60 subjects across four core disciplines: Natural Science, Healthcare, Humanities & Social Sciences, and Engineering. Each example requires models to generate temporally rich videos that demand scientific reasoning and knowledge-grounded synthesis, going beyond surface-level visual plausibility. We further establish a rubric-based evaluation protocol. Our analysis shows that, under this protocol, both non-expert human evaluators and MLLM-as-Judge systems can achieve relatively high agreement with expert judgments, supporting reproducible evaluation at scale. We benchmark 16 frontier proprietary and open-source models and find that, while automatic perceptual-quality scores cluster tightly across systems, performance on Prompt Grounding and Scientific and Causal Correctness varies substantially, with a pronounced proprietary-open-source gap. These findings show that advances in visual realism have not yet translated into reliable modeling of scientific and causal dynamics.

### 🤖 AI 总结

**一句话总结**：We introduce Sci-VBench, a comprehensive benchmark for evaluating knowledge- and reasoning-intensive video generation across scientific domains. It contains 1,253 expert-annotated examples spanning 60...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sci-VBench, Evaluating, Knowledge, Reasoning-Intensive, Video, Generation, Science, Domains

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09873v1) | [下载PDF](https://arxiv.org/pdf/2608.09873v1.pdf)

---

## [20. From Diagnosis to Correction: Benchmarking and Improving Real-World Table Parsing](https://arxiv.org/abs/2608.09842v1)

**作者**：Jutao Xiao, Yuan Qu, Dongsheng Ma 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-10

### 📄 论文摘要

Recent document parsers achieve table TEDS scores above 93 on OmniDocBench v1.6, yet community feedback and our audit reveal persistent failures on complex real-world tables. To quantify this gap, we introduce TableParseMap, a diagnostic benchmark of 916 real-world tables organized into five challenging scenarios and nine failure types. The strongest evaluated parser achieves only 85.03 TEDS, showing that aggregate benchmark scores conceal substantial weaknesses. Our analysis attributes these failures to three complementary limitations: large tables exceed the reliable processing scale of a single pass, weak or ambiguous visual cues hinder structure perception, and the reconstructed table may remain visually inconsistent with the image. We therefore propose DEC (Decompose--Enhance--Correct), a visual-consistency-guided agentic framework that improves frozen table parsers without retraining. DEC uses a general VLM as the controller: Decompose partitions large tables along structure-aware boundaries, Enhance exposes weak visual evidence and reparses transformed views, and Correct diagnoses and repairs residual errors. A Visual Consistency Gate (VC-Gate) selectively triggers intervention, while a Visual Consistency Ranker (VC-Ranker) verifies candidate updates and supports rollback without ground-truth HTML at inference time. We further derive a 1,977-table Consensus-Hard Set from 4,556 candidates through offline metrics and cross-model consensus. Across three frozen parsers, DEC improves TEDS by 1.57 points on average; on TableParseMap, gains reach 1.89 points overall, 2.62 on structural errors, and 5.66 on large tables.

### 🤖 AI 总结

**一句话总结**：Recent document parsers achieve table TEDS scores above 93 on OmniDocBench v1.6, yet community feedback and our audit reveal persistent failures on complex real-world tables. To quantify this gap, we ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diagnosis, Correction, Benchmarking, Improving, Real-World, Table, Parsing, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09842v1) | [下载PDF](https://arxiv.org/pdf/2608.09842v1.pdf)

---

## [21. MedPixel: A Unified Pixel-Language Model for Medical Reasoning and Segmentation](https://arxiv.org/abs/2608.09818v1)

**作者**：Haoyu Yang, Meixing Shi, Zengjie Chen 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-10

### 📄 论文摘要

Reliable medical image understanding requires models to connect clinical language and visual reasoning with pixel-level grounding. Yet medical vision-language models often lack precise localization, whereas medical segmenters typically rely on explicit target categories or precise spatial prompts. This divide is reinforced by a supervision mismatch: segmentation datasets provide precise masks but little language supervision, whereas medical vision-language data rarely pair language with dense spatial annotations. To address this gap, we present MedPixel, a unified medical pixel-language model built around a shared language--mask interface. To provide scalable supervision, we introduce MedPLG-440K, comprising approximately 440K pixel-language task samples constructed through a clinically motivated synthesis process without external LLM annotation. MedPixel is trained with joint multi-task supervised fine-tuning followed by Pixel-Level Preference Optimization, which uses ground-truth masks as offline verifiers to derive response preferences from mask quality. MedPixel supports a broad spectrum of tasks spanning explicit grounding, implicit reasoning, spatial interaction, grounded explanation, and medical VQA. Across this task spectrum, MedPixel achieves strong performance in both pixel-level prediction and response generation, together with effective zero-shot transfer to external grounding benchmarks and robustness to imperfect spatial prompts. Code and model checkpoints will be released at https://github.com/yhy-whu/Medpixel.

### 🤖 AI 总结

**一句话总结**：Reliable medical image understanding requires models to connect clinical language and visual reasoning with pixel-level grounding. Yet medical vision-language models often lack precise localization, w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MedPixel, Unified, Pixel-Language, Model, Medical, Reasoning, Segmentation, Reliable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09818v1) | [下载PDF](https://arxiv.org/pdf/2608.09818v1.pdf)

---

## [22. Modern Backbones Improve Multi-task DETR for Mammography Classification and Lesion Localization](https://arxiv.org/abs/2608.09801v1)

**作者**：Dinh Tan Nguyen, Quang-Hien Kha, Le-Hoang Nguyen 等 11 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-10

### 📄 论文摘要

Joint exam-level prediction and candidate-region localization may improve the usefulness of AI support in mammography. We study this setting using a multi-task DETR framework, where shared representations support both image-level malignancy prediction and lesion localization, and evaluate its performance on OPTIMAM and a biopsy-confirmed SGM1k cohort. Across both datasets, modern backbones consistently outperformed older ResNet-style features, with ConvNeXtV2 and DINOv3 giving the strongest overall results, whereas MambaVision was less competitive. On OPTIMAM, ConvNeXtV2 achieved the best overall performance, reaching 97.96% AUC, 99.89% sensitivity, 25.08% mAP@.5, and 74.38% recall@.25. On SGM1k, DINOv3 gave the strongest overall results, with 90.97% AUC, 86.28% sensitivity, 82.00% specificity, 27.04% mAP@.5, and 77.32% recall@.25. These findings suggest that backbone quality is a critical factor in effective multi-task mammography, with ConvNeXtV2 emerging as a particularly strong and well-matched CNN backbone for mammography in this framework.

### 🤖 AI 总结

**一句话总结**：Joint exam-level prediction and candidate-region localization may improve the usefulness of AI support in mammography. We study this setting using a multi-task DETR framework, where shared representat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Modern, Backbones, Improve, Multi-task, DETR, Mammography, Classification, Lesion

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09801v1) | [下载PDF](https://arxiv.org/pdf/2608.09801v1.pdf)

---

## [23. NTIRE 2026 Low-light Enhancement: Twilight Cowboy Challenge](https://arxiv.org/abs/2608.09782v1)

**作者**：Aleksei Khalin, Egor Ershov, Artyom Panshin 等 49 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-10

### 📄 论文摘要

This paper presents a review of the NTIRE 2026 Low-light Enhancement: Twilight Cowboy Challenge. The objective of the competition was to merge a set of misaligned smartphone images in the raw domain, captured in low-light conditions, into a single, clean image. Introduced setup simultaneously addresses two problems of low-light photography: visual degradations such as high noise and mixed scene illuminants, and the geometric inconsistencies caused by hand movement during multi-frame capture. To advance research in low-light and nighttime computational photography, a challenging dataset was collected comprising 585 real-world scenes, spanning indoor low-light and outdoor nighttime conditions, for training and benchmarking participant solutions. The competition employed a three-stage evaluation protocol: automatic validation via the CodaBench platform in stages one and two, followed by blind assessment on a private test set for the final ranking. Ten teams surpassed the established baseline, achieving improvements of up to +6.49 dB in PSNR and +0.0101 in SSIM, thereby establishing new state-of-the-art performance for burst-based low-light image enhancement. These results demonstrate significant progress in handling real-world noise, motion, and illumination variability in the low-light setting. Comprehensive results, leaderboards, and additional information are publicly available at https://nightimaging.org.

### 🤖 AI 总结

**一句话总结**：This paper presents a review of the NTIRE 2026 Low-light Enhancement: Twilight Cowboy Challenge. The objective of the competition was to merge a set of misaligned smartphone images in the raw domain, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：NTIRE, Low-light, Enhancement, Twilight, Cowboy, Challenge, paper, presents

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09782v1) | [下载PDF](https://arxiv.org/pdf/2608.09782v1.pdf)

---

## [24. C$^2$A: Coupling Spatial Evidence with Clinical Priors via Co-occurrence Aware Class Attention for Multi-Label Chest X-Ray Classification](https://arxiv.org/abs/2608.09774v1)

**作者**：Akash Gogineni, Nagur Shareef Shaik, Aasrith Mandava 等 5 位作者  
**分类**：cs.CV, cs.LG, eess.IV, eess.SP  
**发布时间**：2026-08-10

### 📄 论文摘要

Thoracic pathologies rarely occur in isolation, yet standard multi-label classifiers rely on shared global descriptors, discarding \emph{where} findings lie and \emph{how} they co-occur. We propose \textbf{C$\mathbf{^2}$A} (Co-occurrence Aware Class Attention), a classification head that explicitly couples spatial evidence with clinical priors. First, C$^2$A casts pooling as an expectation over learned per-class spatial attention maps, yielding localized descriptors for each disease. Second, it couples these descriptors via a learnable graph warm-started from empirical label co-occurrence. A single residual message-passing step shares evidence among related findings, proving to be a bounded perturbation of the identity where co-occurrence enters each logit through an explicit bilinear interaction. On CheXpert, C$^2$A achieves a superior $0.895$ macro-mean AUROC, outperforming advanced context-gating baselines. Crucially, gains concentrate on highly co-occurrent classes with ambiguous spatial evidence (rescuing Atelectasis by $+1.5$ over GCG), demonstrating the prior's regularizing effect with a negligible overhead of one linear projection and a $C\!\times\!C$ edge matrix.

### 🤖 AI 总结

**一句话总结**：Thoracic pathologies rarely occur in isolation, yet standard multi-label classifiers rely on shared global descriptors, discarding \emph{where} findings lie and \emph{how} they co-occur. We propose \t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：C$^2$A, Coupling, Spatial, Evidence, Clinical, Priors, via, Co-occurrence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09774v1) | [下载PDF](https://arxiv.org/pdf/2608.09774v1.pdf)

---

## cs.LG

## [25. Fairness in Link Prediction Beyond Demographic Parity: A Reproducibility Study](https://arxiv.org/abs/2608.09899v1)

**作者**：Valentijn Oldenburg, Floris de Kam, Stef de Wildt 等 4 位作者  
**分类**：cs.LG, cs.SI  
**发布时间**：2026-08-10

### 📄 论文摘要

In fair ranked link prediction, demographic parity ($Δ_\mathrm{DP}$) is a common fairness metric. Yet, Mattos et al. (2025) argue that it fails to detect exposure bias because it ignores where links appear in the ranking. In this study, we reproduce this claim by showing that $Δ_\mathrm{DP}$ can indicate aggregate parity even when some subgroup-pair links are systematically ranked lower than others. The proposed rank-aware Normalized Discounted KL-divergence (NDKL), however, does detect such disparities. We also reproduce the effectiveness of MORAL, a post-processing method that improves exposure-based fairness while maintaining competitive utility. Beyond reproduction, we assess robustness using synthetic homophily settings, categorical sensitive attributes, and additional fairness and utility metrics, including subgroup-pair-adapted Attention-Weighted Rank Fairness (AWRF). Overall, our results show that exposure-based metrics uncover biases hidden by $Δ_\mathrm{DP}$ and that MORAL reduces these biases with minimal utility loss across diverse settings and datasets. We release a corrected, reproducible implementation at https://github.com/Floris93100/reproducing-MORAL.

### 🤖 AI 总结

**一句话总结**：In fair ranked link prediction, demographic parity ($Δ_\mathrm{DP}$) is a common fairness metric. Yet, Mattos et al. (2025) argue that it fails to detect exposure bias because it ignores where links a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Fairness, Link, Prediction, Beyond, Demographic, Parity, Reproducibility, Study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09899v1) | [下载PDF](https://arxiv.org/pdf/2608.09899v1.pdf)

---

## [26. Real-Time Climate Risk Assessment for Supply Chain Resilience: A Data-Driven Nowcasting Framework for Colombian Agriculture](https://arxiv.org/abs/2608.09846v1)

**作者**：Hernan J. Silva-Sosa  
**分类**：cs.LG  
**发布时间**：2026-08-10

### 📄 论文摘要

This paper presents a methodological framework for real-time climate risk assessment using data-driven nowcasting techniques to enhance supply chain resilience in Colombian agricultural contexts. Climate variability in Colombia, characterized by irregular rainfall, temperature fluctuations, and recurrent extreme events, has a direct impact on agricultural production and logistics, particularly for time sensitive crops. The proposed approach integrates short term climate forecasting based on historical meteorological observations with supply chain risk modeling to establish a conceptual early warning system architecture. A prototype implementation developed in a controlled computational environment demonstrates the feasibility of the framework using historical meteorological and agricultural time series derived from official statistics and reanalysis products, without reliance on satellite imagery or computer vision components. The methodology addresses the integration of climate nowcasting with supply chain decision making through explicit risk mapping, threshold-based categorization, and stakeholder-oriented risk signals. Results from synthetic and historical data experiments indicate that short term precipitation nowcasts can be translated into actionable risk indicators for agricultural supply chains, supporting anticipatory decisions related to inventory, sourcing, and transport.

### 🤖 AI 总结

**一句话总结**：This paper presents a methodological framework for real-time climate risk assessment using data-driven nowcasting techniques to enhance supply chain resilience in Colombian agricultural contexts. Clim...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Real-Time, Climate, Risk, Assessment, Supply, Chain, Resilience, Data-Driven

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09846v1) | [下载PDF](https://arxiv.org/pdf/2608.09846v1.pdf)

---

## [27. Deep Multimodal Wearable Sensor Fusion for Detection of Body-Focused Repetitive Behaviors](https://arxiv.org/abs/2608.09830v1)

**作者**：Samaneh Rezaeimanesh, Mohsen Behradfar, Mohammad Fili 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-10

### 📄 论文摘要

Body-focused repetitive behaviors, such as hair pulling and skin picking, are compulsive motor actions commonly associated with obsessive-compulsive and anxiety disorders. Their early, objective detection remains difficult because the movements are subtle and overlap with ordinary, non-pathological gestures. We developed and evaluated a multimodal deep learning framework to detect and classify these behaviors from wrist-worn sensor data. The data, collected by the Child Mind Institute using the Helios wrist-worn device, combine inertial measurement units, thermopile sensors, and time-of-flight sensors, capturing kinematic, thermal, and proximity information. The framework combined a convolutional neural network with a gated recurrent unit, alongside modality-specific autoencoders and a late-fusion classifier, to exploit temporal and spatial dynamics. It achieved an F1 score of 0.985 and an area under the receiver operating characteristic curve of 0.997 for binary detection, distinguishing these behaviors from other activities, and a macro-averaged F1 score of 0.700 with an area under the curve of 0.963 across a nine-class scheme that distinguished each individual behavior from a single grouped Non-Target class, improving over single-modality baselines. Post-hoc interpretability based on Shapley additive explanations showed that the time-of-flight and inertial modalities dominated discriminative power by capturing spatial proximity and dynamic movement, while hierarchical clustering indicated that misclassifications were driven primarily by the anatomical region of the gesture. These findings demonstrate that multimodal sensor fusion enables accurate, objective, and continuous behavioral monitoring. This work establishes a foundation for real-time, wearable-assisted mental health diagnostics and personalized interventions in biomedical research and clinical care.

### 🤖 AI 总结

**一句话总结**：Body-focused repetitive behaviors, such as hair pulling and skin picking, are compulsive motor actions commonly associated with obsessive-compulsive and anxiety disorders. Their early, objective detec...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Deep, Multimodal, Wearable, Sensor, Fusion, Detection, Body-Focused

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09830v1) | [下载PDF](https://arxiv.org/pdf/2608.09830v1.pdf)

---

## [28. Multi-Agent AI Safety as an Institutional Design Problem](https://arxiv.org/abs/2608.09828v1)

**作者**：Abdullah X  
**分类**：cs.LG, cs.AI, cs.MA  
**发布时间**：2026-08-10

### 📄 论文摘要

AI agents increasingly work inside systems that govern how they delegate tasks, move information, execute actions, and use shared resources. Recent work already shows that deployment rules can change collective behavior. Here we ask which parts of an AI institution produce safety and how they do it. This is the first paper from POLIS, an ongoing research programme studying algorithmic institutions for multi-agent systems. We report a frozen 5,280-episode study suite. The main pre-specified delegation experiment spans four model families; a targeted high-conflict diagnostic adds three additional model endpoints. In matched structured workflows, the model sees different rule formulations and guards consult different authority states. We also vary the attractiveness of the immediate compliant internal/self fallback and allow blocked workflows to continue. A detailed constitutional prompt produces 0/384 realized violations. A provenance-aware executable guard also produces 0/384, although it blocks prohibited attempts in 51/384 episodes; 44/51 of those episodes later complete safely. The local-state guard's failures concentrate in scenarios where an ordinary transformation changes visible policy while originating authority stays fixed. In matched laundering scenarios, that guard admits violations in 22/96 episodes and provenance enforcement in 0/96 (p = 4.77 x 10^-7). A separate resource-allocation experiment shows that revealing the numerical value of an otherwise identical cap changes agent requests. In these structured workflows, the same final violation rate can hide very different mechanisms. The rule itself is only part of the institution. The authority state the system trusts matters, and so does the path available after a block.

### 🤖 AI 总结

**一句话总结**：AI agents increasingly work inside systems that govern how they delegate tasks, move information, execute actions, and use shared resources. Recent work already shows that deployment rules can change ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, as, an, Agent, Safety, Institutional, Design, Problem

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09828v1) | [下载PDF](https://arxiv.org/pdf/2608.09828v1.pdf)

---

## [29. Macaron-V1: Towards Open Continual Learning with Self-Improvement and Mixture-of-LoRA](https://arxiv.org/abs/2608.09819v1)

**作者**：Mind Lab, :, Vin Bo 等 77 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-08-10

### 📄 论文摘要

Macaron-V1 is an open agent-model family for experiential intelligence: learning from experience in real environments and continuing to learn after deployment. It is organized around two system goals. Adaptation is pursued through recursive improvement of versioned model-harness pairs, where experience from one configuration is evaluated under an external contract and used to construct its successor. Collaboration is pursued via the Mixture-of-LoRA (MoL) architecture that freezes a base model, composes specialist LoRA adapters, and selects one LoRA per user turn. The flagship Macaron-V1-Venti combines a 744B GLM-5.2 base with four LoRAs for chat, agent, coding, and GenUI; the Qwen3.6-based Macaron-V1-Tall (50B) uses the same design for local deployment. This report presents Macaron-V1 as a co-designed system spanning architecture, algorithms, and infrastructure. The MoL architecture supports continual learning through extensible LoRA specialists. The algorithm combines Model-Harness Co-design and recursive self-improvement loop, including the UI4A component-native GenUI harness, a stateful action substrate, versioned HCP contract, and the agentic RL framework MindForge. The supporting infrastructure includes the post-training platform MinT, the long-context RL method LongStraw, and stability techniques for sparse MoE and DSA base models. We evaluate Macaron-V1 on Personal Intelligence, GenUI, and general capability benchmarks against frontier baselines. Our results validate the current system, while compounding gains from continual learning and collective intelligence remain open questions.

### 🤖 AI 总结

**一句话总结**：Macaron-V1 is an open agent-model family for experiential intelligence: learning from experience in real environments and continuing to learn after deployment. It is organized around two system goals....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Macaron-V1, Towards, Open, Continual, Learning, Self-Improvement, Mixture-of-LoRA

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09819v1) | [下载PDF](https://arxiv.org/pdf/2608.09819v1.pdf)

---

## [30. ReliableNet: A Chance-Constrained Approach to Trustworthy Classification in Deep Learning](https://arxiv.org/abs/2608.09768v1)

**作者**：Ange-Clément Akazan, Ineza Remy Mugenga, Abebe Geletu 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-10

### 📄 论文摘要

A prediction that is both confident and wrong is a critical reliability failure because it can bypass abstention and human review precisely when the model is mistaken. Empirical risk minimization (ERM) controls average loss but not this failure directly, while calibration, uncertainty estimation, conformal risk control, and selective prediction methods target related reliability properties rather than bounding the joint failure event during training. We propose ReliableNet, which constrains the Joint Confident-Wrong (JCW) probability, the probability that a prediction is simultaneously confident and incorrect, below a user-specified risk budget $α\in(0,1)$. We formulate this as a chance-constrained ERM problem, use a conservative smooth inner approximation whose population feasibility implies the original JCW constraint. Across four tabular and two image datasets, ReliableNet is the only method certified within the JCW budget for every dataset and seed in distribution, when compared against baselines spanning ERM, post-hoc calibration, conformal risk control, and selective prediction. Under demographic, ambiguity, spurious-correlation, novel-class, and covariate shifts, it achieves the lowest empirical JCW among the compared methods while remaining very competitive in accuracy, coverage, calibration, and selective prediction. Risk-coverage results further indicate that ReliableNet achieves better selective ranking than the benchmark methods on most datasets. Overall, ReliableNet provides a principled approach to trustworthy classification.

### 🤖 AI 总结

**一句话总结**：A prediction that is both confident and wrong is a critical reliability failure because it can bypass abstention and human review precisely when the model is mistaken. Empirical risk minimization (ERM...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ReliableNet, Chance-Constrained, Approach, Trustworthy, Classification, Deep, Learning, prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.09768v1) | [下载PDF](https://arxiv.org/pdf/2608.09768v1.pdf)

---

