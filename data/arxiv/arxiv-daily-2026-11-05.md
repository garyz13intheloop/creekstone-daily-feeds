# arXiv AI 论文日报 | 2026-11-05

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.AI](#csAI) (7 篇)
- [cs.LG](#csLG) (5 篇)
- [cs.CV](#csCV) (11 篇)
- [cs.CL](#csCL) (7 篇)

---

## cs.AI

## [1. BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories](https://arxiv.org/abs/2611.06911v1)

**作者**：Fei Lin, Tengchao Zhang, Ziyang Gong 等 18 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-04

### 📄 论文摘要

Self-Driving Chemical Laboratories (SDCLs) are moving chemical experimentation toward embodied automation, where machines must perceive laboratory scenes, reason about experimental states, and act under physical, procedural, and safety constraints. Although Multimodal Large Language Models (MLLMs) are increasingly considered as embodied brains for such systems, existing laboratory benchmarks mainly focus on safety, anomaly detection, or general scientific understanding, leaving their execution-oriented embodied capabilities underexplored. To fill this gap, we introduce BEAKER, a Benchmark for evaluating Embodied Actionability, Knowledge, Experimentation, and Reasoning in SDCLs. BEAKER contains 1,000 expert-curated question-answer samples across 11 image and video task types, covering key judgments required for chemical laboratory execution, including affordance grounding, trajectory planning, equipment, state, and safety recognition, apparatus setup, operation and step reasoning, and temporal procedure reasoning. All questions and annotations are manually created and reviewed by chemistry and embodied Artificial Intelligence (AI) experts, without AI-assisted generation or annotation. We evaluate 28 general-purpose, science-oriented, chemistry-specialized, and embodied MLLMs in an offline, single-turn setting. Results show that current models can follow coarse experimental procedures in videos, but still struggle to ground actions into operable regions and feasible trajectories, to recognize fine-grained laboratory apparatus, states, and safety norms, and to order steps in mid-length procedures. BEAKER thus reveals a clear gap between coarse procedural understanding and the precise, action-grounded perception required for laboratory execution, providing a diagnostic benchmark for future MLLMs in SDCLs.

### 🤖 AI 总结

**一句话总结**：Self-Driving Chemical Laboratories (SDCLs) are moving chemical experimentation toward embodied automation, where machines must perceive laboratory scenes, reason about experimental states, and act und...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, BEAKER, Expert-Curated, Benchmark, Embodied, Brains, Self-Driving, Chemical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06911v1) | [下载PDF](https://arxiv.org/pdf/2611.06911v1.pdf)

---

## [2. FrontierPhysics: Evaluating Agents for End-to-End Physics Research](https://arxiv.org/abs/2611.06910v1)

**作者**：Bingran You, Wenjun Ke, Ria Rosenauer 等 72 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-04

### 📄 论文摘要

AI agents are playing an increasingly important role in physics research. However, existing physics benchmarks only evaluate fixed questions, isolated sub-tasks, or paper reproduction with given solutions, and rarely check research quality alongside correctness. We introduce FrontierPhysics, an end-to-end benchmark with 56 tasks made by 42 physicists based on their own research, covering nine domains across theoretical, computational, and experimental physics. Each task requires agents to review the literature, develop a research plan, conduct research and experiments, and produce structured outputs and scientific manuscripts. Combining deterministic verifiers with expert-authored rubrics, FrontierPhysics evaluates whether agents' research is correct and publishable. Across 22 models in 26 configurations, no configuration passes more than 46 of its 168 rollouts. Manual review of agent trajectories shows that frontier agents' main weaknesses are insufficiently rigorous reasoning and limited expert intuition, rather than gaps in physics knowledge or execution errors.

### 🤖 AI 总结

**一句话总结**：AI agents are playing an increasingly important role in physics research. However, existing physics benchmarks only evaluate fixed questions, isolated sub-tasks, or paper reproduction with given solut...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, an, FrontierPhysics, Evaluating, End-to-End, Physics, Research, playing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06910v1) | [下载PDF](https://arxiv.org/pdf/2611.06910v1.pdf)

---

## [3. Dull, Dirty, Dangerous? Working Conditions and the Limits of Occupational AI Exposure](https://arxiv.org/abs/2611.06888v1)

**作者**：Siyi Yu  
**分类**：cs.AI, cs.HC, econ.GN  
**发布时间**：2026-11-04

### 📄 论文摘要

Automation is often justified as relief from dull, dirty, and dangerous work. I examine how these conditions relate to occupational AI exposure using 21 O*NET items across 754 US occupations. Higher exposure is associated with lower condition scores under a large language model (LLM) measure and AI Occupational Exposure (AIOE), with equal occupation weights and employment weights. Adjustment for physical demands, required education, training and experience, and wages reduces the composite association. The adjusted confidence intervals include zero for LLM exposure and remain below zero for AIOE. Separating repetition from restricted discretion also changes what the combined Dull score conveys. These comparisons show how item groupings and occupational characteristics shape the interpretation of exposure estimates. Occupational profiles offer a starting point for selecting contrasting research settings. Establishing desired automation or realized relief requires evidence about workers' preferences and specific interventions.

### 🤖 AI 总结

**一句话总结**：Automation is often justified as relief from dull, dirty, and dangerous work. I examine how these conditions relate to occupational AI exposure using 21 O*NET items across 754 US occupations. Higher e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Dull, Dirty, Dangerous?, Working, Conditions, Limits, Occupational

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06888v1) | [下载PDF](https://arxiv.org/pdf/2611.06888v1.pdf)

---

## [4. Learning to Decode Linear Codes with Generalized Belief Propagation Network](https://arxiv.org/abs/2611.06874v1)

**作者**：Samira Malek  
**分类**：cs.AI  
**发布时间**：2026-11-04

### 📄 论文摘要

Error correcting codes are a fundamental component of communication systems, enabling reliable data transmission over noisy channels. Recently, neural decoders have demonstrated notable performance gains over classical iterative algorithms. In this paper, we propose a Generalized Belief Propagation Network (GBPNet) that preserves message-passing symmetry while enhancing the decoder's learning capability. The architecture uses cascaded variable-node updates and learned element-wise message scaling while retaining the Tanner graph structure. We also introduce two training strategies, progressive training and high-SNR training, that improve decoding accuracy. Experimental results on several linear codes show that GBPNet achieves lower bit error rates than conventional belief propagation and the evaluated state-of-the-art neural decoders.

### 🤖 AI 总结

**一句话总结**：Error correcting codes are a fundamental component of communication systems, enabling reliable data transmission over noisy channels. Recently, neural decoders have demonstrated notable performance ga...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Decode, Linear, Codes, Generalized, Belief, Propagation, Network

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06874v1) | [下载PDF](https://arxiv.org/pdf/2611.06874v1.pdf)

---

## [5. On Turn-Level Best-of-N Sampling for Scaling LLM Agents](https://arxiv.org/abs/2611.06868v1)

**作者**：Jalaj Bhandari, Dhawal Gupta, Hongli Zhan 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-04

### 📄 论文摘要

In this work, we evaluate a simple inference-time scaling approach based on \textit{turn-level best-of-N sampling} (\method) for large language model (LLM) agents on complex, long-horizon tasks. We instantiate this using a \textit{generator-selector} framework with two LLMs; at each turn, a \emph{generator} model generates $N$ candidate actions and a \emph{selector} model selects one of them, which is then executed in the environment. This paper is closely related to the work of \cite{zainullina2025guided} who used critic models for guided search at inference time. Different from their work, we evaluate if off-the-shelf, open-weight LLMs can be effective at comparing different candidate actions directly. Experiments on long-horizon terminal tasks show that \method can lead to significant performance improvements, both in terms of accuracy (5--10\%) and consistency across repeated attempts. Analysis of agent trajectories reveal a shift in agent behaviour towards desirable patterns such as reduction in number of attempts to solve the task, improved task instruction following, debugging and testing.

### 🤖 AI 总结

**一句话总结**：In this work, we evaluate a simple inference-time scaling approach based on \textit{turn-level best-of-N sampling} (\method) for large language model (LLM) agents on complex, long-horizon tasks. We in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, we, Turn-Level, Best-of-N, Sampling, Scaling, work

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06868v1) | [下载PDF](https://arxiv.org/pdf/2611.06868v1.pdf)

---

## [6. CompressionBench: How can your coding agents compress LLMs?](https://arxiv.org/abs/2611.06858v1)

**作者**：Xinrui Zhong, Zhifeng Li, Zhiming Wang 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-04

### 📄 论文摘要

Recursive self-improvement requires AI systems to improve the models and infrastructure used by subsequent systems. LLM compression offers a concrete efficiency objective: retain a pretrained model's behavior within a smaller model storage budget. We study whether coding agents can carry out this step autonomously. We formulate compression as a terminal task in which an agent receives a source checkpoint, storage limit, inference environment, and time budget, then constructs compressed weights and executable inference code. The agent controls its algorithm and experiments; perplexity feedback guides search, and independent verification checks the final model. Across six agents and six model--size settings, 29 of 36 submissions pass verification. Selecting the lowest-perplexity agent design per task yields an average 3.4% perplexity increase over BF16 and 77.33% downstream accuracy, compared with 79.56% for BF16. Recorded experiments reveal how agents achieve these outcomes and where improvement breaks down. Agents lower PPL in 21 of 24 revisions at nearly fixed storage; complete-model feedback reverses 17 of 79 prior local rankings; and generation and inference tests expose failures that likelihood alone misses. The results identify representation design, experimental judgment, and capability validation as central to agent-driven model compression, a measurable component of efficiency-oriented self-improvement.

### 🤖 AI 总结

**一句话总结**：Recursive self-improvement requires AI systems to improve the models and infrastructure used by subsequent systems. LLM compression offers a concrete efficiency objective: retain a pretrained model's ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, CompressionBench, How, can, coding, compress, LLMs?, Recursive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06858v1) | [下载PDF](https://arxiv.org/pdf/2611.06858v1.pdf)

---

## [7. Task-Efficient Agent Evaluation Using Cached Traces](https://arxiv.org/abs/2611.06803v1)

**作者**：Ben Johnson, Hayden Helm  
**分类**：cs.AI  
**发布时间**：2026-11-04

### 📄 论文摘要

Efficient benchmarking estimates a system's full benchmark performance from a small number of task executions. Standard approaches rely solely on the binary correctness of executions from a collection of already-evaluated reference systems. An agentic system, however, produces a rich trace for each execution that can reveal substantially more about its capabilities. Leveraging this information requires useful trace representations. We propose representing a trace by extracting a structured summary of it with an LLM and embedding the summary with a standard text encoder. These representations preserve correctness- and task-related signal while minimizing the presence of system identity-, model family- and harness-related signals that dominate raw trace embeddings. Given this representation for each task execution from all reference systems, we construct low-dimensional representations of the systems and predict a new system's score from its position among the reference systems. On SWE-bench Verified and Terminal-Bench 2.0, augmenting an item-response model with this geometry-based prediction reduces mean absolute error from 0.13 to 0.08 (Wilcoxon $p < 10^{-4}$) and from 0.14 to 0.12 (Wilcoxon $p < 10^{-3}$), respectively, when provided a single random executed task. Further, given access to the full set of reference systems, our approach dominates baselines for any given number of executed tasks on both benchmarks.

### 🤖 AI 总结

**一句话总结**：Efficient benchmarking estimates a system's full benchmark performance from a small number of task executions. Standard approaches rely solely on the binary correctness of executions from a collection...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Task-Efficient, Evaluation, Cached, Traces, Efficient, benchmarking, estimates

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06803v1) | [下载PDF](https://arxiv.org/pdf/2611.06803v1.pdf)

---

## cs.CL

## [8. SpecCompact: Accelerating LLM Agent Context Compaction with Slot-Parallel Semantic Speculative Verification](https://arxiv.org/abs/2611.06876v1)

**作者**：Yulu An, Yifei Feng, Xiangyang Yin  
**分类**：cs.CL  
**发布时间**：2026-11-04

### 📄 论文摘要

LLM agents use context compaction to manage growing interaction histories, but summarizing long histories with large models can introduce substantial delays. Compaction therefore requires balancing information retention against latency. We observe that structured summary slots can retain information when generated independently. Based on this observation, we present SpecCompact, a framework that accelerates compaction through slot-parallel semantic speculation. SpecCompact fine-tunes a small drafter and generates slots in parallel. The target model verifies each proposed line and repairs rejected content, while subsequent drafting uses the updated slot prefix. System optimizations further reduce repeated context processing and model calls. Across AppWorld and $τ^3$ benchmarks with two target models, SpecCompact achieves $2.04$--$5.63\times$ compaction speedups over Hermes-style summarization. Separate downstream evaluations reveal model- and task-dependent performance trade-offs. A user study within Hermes further shows an $8.68\times$ median compaction speedup.

### 🤖 AI 总结

**一句话总结**：LLM agents use context compaction to manage growing interaction histories, but summarizing long histories with large models can introduce substantial delays. Compaction therefore requires balancing in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, SpecCompact, Accelerating, Context, Compaction, Slot-Parallel, Semantic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06876v1) | [下载PDF](https://arxiv.org/pdf/2611.06876v1.pdf)

---

## [9. Balancing hierarchical representation and quantization: A performance trade-off in text embeddings](https://arxiv.org/abs/2611.06859v1)

**作者**：Kai Ponel, Marco Polignano, Erasmo Purificato 等 7 位作者  
**分类**：cs.CL, cs.IR, cs.LG  
**发布时间**：2026-11-04

### 📄 论文摘要

Hierarchical text embedding models offer variable-length representations, while quantization reduces numerical precision; both aim to improve computational efficiency. This work is an empirical benchmark study of how these two orthogonal, already-established techniques interact. We evaluate 38 tasks from the Massive Text Embedding Benchmark (MTEB) using four transformer-based embedding models, covering 1D and 2D hierarchical representations combined with 32-bit, 8-bit, and binary quantization, for 168 configurations per task. We report each efficiency dimension separately: theoretical per-vector storage and end-to-end evaluation time. Under a Friedman test with Nemenyi post-hoc analysis, int8 quantization is statistically indistinguishable from float32 for pair classification and re-ranking and costs at most 1.5 percentage points overall, whereas binary quantization is significantly worse across every task category. Halving the embedding dimension once is not statistically detectable above $m=16$; two successive halvings always are. Combining an 8x dimensionality reduction with int8 yields a 32x reduction in per-vector storage at 94.4% of baseline effectiveness. Because evaluation times were measured once, we treat them as indicative: we find no evidence that quantization speeds up evaluation, whereas sampling from intermediate layers shortens it substantially. Retrieval degrades far faster than every other category, so we report findings per task category.

### 🤖 AI 总结

**一句话总结**：Hierarchical text embedding models offer variable-length representations, while quantization reduces numerical precision; both aim to improve computational efficiency. This work is an empirical benchm...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Balancing, hierarchical, representation, quantization, performance, trade-off, text, embeddings

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06859v1) | [下载PDF](https://arxiv.org/pdf/2611.06859v1.pdf)

---

## [10. Persona Perspectives: Adopting Viewpoints Reorganizes Representations in LLMs](https://arxiv.org/abs/2611.06848v1)

**作者**：Austin C. Kozlowski, Avital Mintz, Madison Lee  
**分类**：cs.CL  
**发布时间**：2026-11-04

### 📄 论文摘要

Common methods for monitoring features in large language models (LLMs) such as linear probes and sparse autoencoders (SAEs) assume that features maintain a consistent representation across contexts. LLMs, however, can flexibly adopt different perspectives or "personas" that suggest different underlying systems of conceptual relations. In this paper, we examine whether prompting an LLM to adopt a persona alters the representational geometry of the model's latent space. We extract representations of over 9,000 common words and 33 semantic axes from models adopting liberal and conservative political personas and compare these against two neutral baselines. We find that persona conditioning systematically alters both the projections of words onto semantic axes and the alignments among the axes themselves in directions consistent with the specified ideology. We then test the implications of this reorganization for two safety-relevant features: truthfulness and morality. Linear probes, SAE-based classifiers, and classifiers built from manually selected word representations, all trained without a persona, produce divergent results when applied to models conditioned on political personas, producing politically slanted ratings of truth and morality on controversial statements. These findings suggest that internal representations, as they are conventionally extracted, can exhibit different geometric relations when the model adopts personas, potentially undermining monitoring efforts.

### 🤖 AI 总结

**一句话总结**：Common methods for monitoring features in large language models (LLMs) such as linear probes and sparse autoencoders (SAEs) assume that features maintain a consistent representation across contexts. L...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Persona, Perspectives, Adopting, Viewpoints, Reorganizes, Representations, Common

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06848v1) | [下载PDF](https://arxiv.org/pdf/2611.06848v1.pdf)

---

## [11. Before You Continue: Evaluating Time-Sensitive Safety Awareness in Conversational Assistants](https://arxiv.org/abs/2611.06839v1)

**作者**：Peidi Dong, Yunze Xiao, Yu-Lin Tsai 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-11-04

### 📄 论文摘要

Large language model (LLM) assistants increasingly help users with everyday activities that involve time-dependent constraints. However, users may not mention these constraints in later requests, requiring assistants to recognize and adjust their advice accordingly. To evaluate such capability, we introduce TASC (Temporal Action Safety in Conversation), a benchmark that evaluates whether LLMs apply time-dependent constraints when responding to conversational requests. TASC consists of 3,418 inputs derived from 128 templates, along with a separate set of 33 scenarios designed to compare models' ability to calculate elapsed time with their ability to apply that information. Across 13 models, assistants account for time-dependent constraints in only 30.5% of cases where the proposed action violates a rule, while rarely warning users unnecessarily. More importantly, models fail to apply these constraints in 62.1% of cases despite correctly calculating the elapsed time. Explicitly providing the timing resolves only about half of these failures, revealing a gap between temporal reasoning and its application in conversational advice.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM) assistants increasingly help users with everyday activities that involve time-dependent constraints. However, users may not mention these constraints in later requests, requ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Before, Continue, Evaluating, Time-Sensitive, Safety, Awareness, Conversational, Assistants

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06839v1) | [下载PDF](https://arxiv.org/pdf/2611.06839v1.pdf)

---

## [12. SAUCE: Summary Analysis Using Conversation Entailment](https://arxiv.org/abs/2611.06812v1)

**作者**：Man-Ling Sung, Hemanth Kandula, Jeff Ma 等 5 位作者  
**分类**：cs.CL, eess.AS  
**发布时间**：2026-11-04

### 📄 论文摘要

With the growing need for evaluating Large Language Models (LLMs) and their applications to speech, challenges persist in summarizing and evaluating conversations that lack a clear end goal. We introduce SAUCE -- a reference-free, fact-based evaluation pipeline for cross-lingual conversational speech summarization. It measures the accuracy and the fact coverage of a summary through the entailment between conversation and text. We compare SAUCE against several popular summarization metrics and demonstrate the effectiveness of capturing information loss due to transcription and translation error and identifying broken summaries. Crucially, unlike black-box LLM evaluators or dense embedding metrics, SAUCE is inherently explainable: it maps summary scores to discrete, verifiable facts, allowing users to pinpoint exact hallucinations or omissions. We illustrate how this interpretability helps developers systematically profile LLM behaviors and gives end-users an actionable tool to verify summary accuracy in noisy, real-world conditions. Preliminary investigations show SAUCE strongly align with human judgment.

### 🤖 AI 总结

**一句话总结**：With the growing need for evaluating Large Language Models (LLMs) and their applications to speech, challenges persist in summarizing and evaluating conversations that lack a clear end goal. We introd...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SAUCE, Summary, Analysis, Conversation, Entailment, growing, need, evaluating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06812v1) | [下载PDF](https://arxiv.org/pdf/2611.06812v1.pdf)

---

## [13. LLMs Don't Know What They Know: Benchmarking Temporal Self-Knowledge for Financial Backtesting](https://arxiv.org/abs/2611.06808v1)

**作者**：Lingfei Qian, Yan Wang, Xueqing Peng 等 15 位作者  
**分类**：cs.CL  
**发布时间**：2026-11-04

### 📄 论文摘要

Financial backtests of large language models (LLMs) are meaningful only if the model did not already know the outcomes it is asked to predict. Practitioners guard against this by trusting a vendor's stated knowledge cutoff, by asking the model what it knows, or by instructing it to answer as of a past date. To verify whether any of these safeguards can be trusted, we introduce FinDendro, a benchmark of 2,226 dated U.S. facts from 1999 to 2026, covering monthly macroeconomic series, month-end stock prices and Federal Reserve decisions. Each fact yields four prompts: a value question, Recall and Predict questions that pair each candidate value with a claim of knowing or guessing without a declared date, and a Predict question with a historical declared date. Controls for persistence and dominant outcomes keep chance accuracy near 0.27. Results show that for most frontier models, self-reports understate knowledge. GPT-5 answers 76% of controlled facts correctly but claims to know 38%, and answers 61% of the facts it says it does not know. Knowledge claims can persist beyond the measured knowledge boundary, by up to seven quarters, and a declared date removes most of the claims of prior knowledge while leaving accuracy unchanged. Backtests inside a model's training window therefore cannot be certified leak-free by self-report, instruction or stated cutoff. These findings motivate behavioral measurement of temporal knowledge boundaries, and FinDendro provides a benchmark and procedure for selecting backtest periods based on demonstrated factual knowledge.

### 🤖 AI 总结

**一句话总结**：Financial backtests of large language models (LLMs) are meaningful only if the model did not already know the outcomes it is asked to predict. Practitioners guard against this by trusting a vendor's s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Don't, Know, What, They, Benchmarking, Temporal, Self-Knowledge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06808v1) | [下载PDF](https://arxiv.org/pdf/2611.06808v1.pdf)

---

## [14. Measuring Risk, Not Harm: Detecting Psychological Harm Risk Factors in LLM Conversations](https://arxiv.org/abs/2611.06806v1)

**作者**：Nil-Jana Akpinar, Eugenia Kim, Natalie Isak 等 6 位作者  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-11-04

### 📄 论文摘要

Psychological harms from interactions with large language models cannot be monitored directly because they may emerge over repeated interactions and depend strongly on subjective individual user context. We propose measuring risk, not harm: detecting observable AI behaviors that constitute risk factors for psychological harm at the AI response level and aggregating these signals to support longitudinal monitoring. We operationalize eight such behaviors and construct a synthetic multi-label corpus of 47,062 AI responses and 373,873 response-factor labels, with targeted human annotations for validation and evaluation. We then compare trained embedding-based classifiers, direct LLM judging, and a classifier--judge cascade. All detectors are model-agnostic and operate only on LLM outputs, requiring no access to internal model states. We apply these detectors to several out-of-distribution human-AI conversation data sets from prior research. On held-out human-labeled data, the best cascade achieves macro precision of 0.86, recall of 0.76, and F1 of 0.79. On WildChat, it reduces LLM-judge calls by 97.1\% relative to direct judging. On DelusionEval, risk-factor detections cluster within conversations. Together, our results show that response-level behavioral risk-factor detection can provide a scalable measurement layer for longitudinal psychological-safety monitoring without conflating observable AI behavior with latent user harm.

### 🤖 AI 总结

**一句话总结**：Psychological harms from interactions with large language models cannot be monitored directly because they may emerge over repeated interactions and depend strongly on subjective individual user conte...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Measuring, Risk, Not, Harm, Detecting, Psychological, Factors

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06806v1) | [下载PDF](https://arxiv.org/pdf/2611.06806v1.pdf)

---

## cs.CV

## [15. Motion-guided Contrastive Regularization For Latent World Models](https://arxiv.org/abs/2611.06901v1)

**作者**：Yiwen Chen, Qiqi Hou, Jisoo Jeong 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-04

### 📄 论文摘要

JEPA-style world models learn action-conditioned latent dynamics without reconstructing observations, but distributional regularization alone does not ensure that their representations preserve information needed for control. We identify static collapse, a failure mode in which the encoder preserves episode-specific static content while suppressing manipulation-relevant state changes. Because static content is temporally predictable yet diverse across episodes, this failure can persist despite regularizers such as SIGReg. A controlled study on OGBench-Cube shows that introducing randomized backgrounds substantially degrades planning performance while leaving the underlying manipulation task unchanged. To address this problem, we propose motion-guided contrastive regularization. Our approach compares predicted latent transitions with transitions to candidate observations from the same episode, reducing the usefulness of static background identity for distinguishing action outcomes. Optical-flow similarities provide soft contrastive targets, allowing candidates with similar motion to receive similar supervision. Combined with latent prediction and SIGReg, our objective encourages representations to preserve within-episode state distinctions and similarities between related transitions. Our method improves planning success over LeWorldModel (LeWM) from 52% to 78% on OGBench-Cube with randomized backgrounds and from 14% to 54% on LIBERO-Object, while maintaining comparable performance on four other visual-control benchmarks.

### 🤖 AI 总结

**一句话总结**：JEPA-style world models learn action-conditioned latent dynamics without reconstructing observations, but distributional regularization alone does not ensure that their representations preserve inform...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Motion-guided, Contrastive, Regularization, Latent, World, Models, JEPA-style, learn

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06901v1) | [下载PDF](https://arxiv.org/pdf/2611.06901v1.pdf)

---

## [16. Occlusion for Free: Detecting Occlusion from the Disagreement Between Two Monocular Distance Cues](https://arxiv.org/abs/2611.06899v1)

**作者**：Chibueze Praise Onyenweaku, Toyibat Adele, Sikirulahi Opeyemi Abdulkareem 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-04

### 📄 论文摘要

Knowing that a pedestrian is occluded is useful to a robot even when the detector cannot recover the hidden pixels, but occlusion estimators are normally trained on occlusion annotations that deployment settings rarely have. We show that occlusion can be read off two distance estimates a camera-only pipeline already computes. Apparent height is largely unchanged by occlusion, because the detected box still spans the whole person; monocular metric depth is pulled toward the occluder, because the nearest surface inside the box is what a depth map reports. Only their ordering matters, so no focal length, stature, or depth scale is needed, provided the depth model's error is close to a pure gain, a condition that can be checked without labels. The score detects heavy occlusion on KITTI with AUC 0.909 (0.888 over all annotated pedestrians, including those the detector misses), requires no training and no occlusion labels, and is not a proxy for range: within fixed distance bands it holds AUC 0.894-0.925 while true distance alone sits near chance. On synthetic CARLA scenes with measured visibility it reaches 0.819, against 0.644 for distance alone. We arrived here after measuring three standard architectural responses to occlusion, depth fusion, occlusion-simulating augmentation, and attention, none of which improved detection outside its training distribution in the configurations we tested, and after finding that a detector trained on German roads loses half its accuracy on self-annotated street scenes in Lagos, Nigeria. Signals that need no local annotation are worth more in settings that benchmarks do not represent.

### 🤖 AI 总结

**一句话总结**：Knowing that a pedestrian is occluded is useful to a robot even when the detector cannot recover the hidden pixels, but occlusion estimators are normally trained on occlusion annotations that deployme...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Occlusion, Free, Detecting, Disagreement, Between, Two, Monocular, Distance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06899v1) | [下载PDF](https://arxiv.org/pdf/2611.06899v1.pdf)

---

## [17. Procedural Adversarial Learning](https://arxiv.org/abs/2611.06890v1)

**作者**：Jack Nugent, Jia Deng  
**分类**：cs.CV  
**发布时间**：2026-11-04

### 📄 论文摘要

For many computer vision tasks, neural networks can be trained to produce a low average error, yet they still fail on seemingly simple scenes. Reducing these failures requires first finding them, but they may not be in a fixed dataset. We study procedural adversarial learning (PAL), a framework of minimax training and adversarial evaluation which searches the input space of a procedural generator for difficult instances. The procedural generator is an interpretable program mapping a low-dimensional vector of control parameters (e.g. layout, lighting, pose) to a rendered image and its label. We introduce the Simple-PAT algorithm, which uses zeroth-order optimization in the procedural generator's parameter space to propose adversarial training samples that are generated on demand. We also create PAL-Dojo, a collection of efficient procedural generators for surface normal estimation, image segmentation, and human pose estimation. Against a cross-model black-box adversary with 50M aggregate queries, Simple-PAT reduces worst-case error by a geometric mean of 3.15x compared to standard training and 2.63x compared to the strongest robust training baseline. Code is available at https://github.com/princeton-vl/procedural-adversarial-learning.

### 🤖 AI 总结

**一句话总结**：For many computer vision tasks, neural networks can be trained to produce a low average error, yet they still fail on seemingly simple scenes. Reducing these failures requires first finding them, but ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Procedural, Adversarial, Learning, many, computer, vision, tasks, neural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06890v1) | [下载PDF](https://arxiv.org/pdf/2611.06890v1.pdf)

---

## [18. PixelSpline: Continuous Space-Time Video Super-Resolution via Endpoint-Anchored Shared Pixel Trajectories](https://arxiv.org/abs/2611.06870v1)

**作者**：Wanqi Yuan, Nianyi Li  
**分类**：cs.CV  
**发布时间**：2026-11-04

### 📄 论文摘要

Existing continuous space-time video super-resolution methods often infer motion from only two endpoint frames and model the two motion directions independently, making them vulnerable to ambiguous correspondence and inconsistent trajectories. We introduce a continuous STVSR framework that combines long-context encoding, continuous HR feature lifting, and an endpoint-anchored PixelSpline. Long-range observations provide more reliable endpoint representations, while continuous upsampling constructs detailed appearance features directly on the requested HR grid. PixelSpline explicitly models each pixel's motion as a single continuous trajectory shared by both endpoints. Using this trajectory, our method warps endpoint colors into a coarse intermediate frame and aligns the HR features for residual reconstruction. Experiments across spatial and temporal upsampling settings demonstrate that the proposed framework offers a favorable quality--efficiency trade-off.

### 🤖 AI 总结

**一句话总结**：Existing continuous space-time video super-resolution methods often infer motion from only two endpoint frames and model the two motion directions independently, making them vulnerable to ambiguous co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PixelSpline, Continuous, Space-Time, Video, Super-Resolution, via, Endpoint-Anchored, Shared

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06870v1) | [下载PDF](https://arxiv.org/pdf/2611.06870v1.pdf)

---

## [19. CounterFactual Retrieval for Evidence-Aware Individual Animal Identification](https://arxiv.org/abs/2611.06864v1)

**作者**：Ankit K. Upadhyay, Aleksandr Algasov, Ekaterina Nepovinnykh 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-11-04

### 📄 论文摘要

Automated identification of individual animals is moving from small curated studies toward shared benchmarks and reusable foundation models. This progress is useful, but current evaluation leaves the evidence behind a match unresolved, i.e., high retrieval accuracy does not show whether a model used animal features or identity-correlated shortcuts. We address this with Counterfactual Foreground Retrieval (CFR), an evidence-aware evaluation protocol. CFR evaluates the same query-gallery task under different views: full image, foreground-only, and shortcut-only. The full-image measures standard retrieval performance; the foreground-only measures foreground-supported retrieval; and shortcut-only view measure how much identity signal is recoverable from background, or silhouette. This turns a retrieval score into an evidence profile: how well the model performs on the original images, how much of that performance remains when only the animal is visible, and how much identity signal remains recoverable when the animal is removed. We release around 0.5M masks for 34 datasets and code for mask generation and CFR evaluation.

### 🤖 AI 总结

**一句话总结**：Automated identification of individual animals is moving from small curated studies toward shared benchmarks and reusable foundation models. This progress is useful, but current evaluation leaves the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, CounterFactual, Retrieval, Evidence-Aware, Individual, Animal, Identification, Automated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06864v1) | [下载PDF](https://arxiv.org/pdf/2611.06864v1.pdf)

---

## [20. LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856v1)

**作者**：Haoxiang Cao, Yuxuan Zhang, Penghui Du 等 19 位作者  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-11-04

### 📄 论文摘要

We introduce LongBanana, to our knowledge the first expert-designed and expert-verified benchmark for long-context multi-reference image synthesis in the age of agent-driven image generation. The task requires retrieving dispersed visual evidence, rejecting distractors, binding entities and relations, and composing one coherent final image from multiple references. LongBanana contains 90 carefully designed tasks organized by a 3-by-3 taxonomy; each task includes about 32 reference images, 20 constraints, and 50 evaluation items, yielding 4,670 expert-specified atomic evaluation items in total. Its graph-grounded evaluation design instantiates each task with reference images and an entity-relation graph, then converts node, edge, and whole-graph obligations into checklist items for Content Fidelity, Relational Binding, and Global Constraint Satisfaction. Reviewed expert labels include a 15% double-labeled subset with 89.4% exact agreement and 0.83 quadratic weighted kappa. We further introduce LongBanana-Gen, an agent-harness framework for long-horizon image generation; experiments show that minimal agent harnesses improve over direct generation, while a ReAct-Plan-Exec-Reflect (RPR) workflow yields harness-dependent gains by strengthening evidence grounding and repair. Together, LongBanana provides an auditable testbed for measuring dense visual evidence use and a shared target for developing stronger agent-driven image-generation systems. Code and data are available at the project page: https://long-banana.com/.

### 🤖 AI 总结

**一句话总结**：We introduce LongBanana, to our knowledge the first expert-designed and expert-verified benchmark for long-context multi-reference image synthesis in the age of agent-driven image generation. The task...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, LongBanana, Expert-Verified, Benchmark, Long-Context, Multi-Reference, Image, Synthesis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06856v1) | [下载PDF](https://arxiv.org/pdf/2611.06856v1.pdf)

---

## [21. Trainspotting: Learning Object-Centric 3D Reconstruction from Found Photos](https://arxiv.org/abs/2611.06849v1)

**作者**：Hanyu Chen, Noah Snavely  
**分类**：cs.CV  
**发布时间**：2026-11-04

### 📄 论文摘要

State-of-the-art feedforward reconstruction models perform poorly on in-the-wild object-centric photo collections. They are trained largely on single-session object captures whose images vary in viewpoint while the object and its environment remain nearly fixed. Public photo archives contain a different form of multi-view data. They hold found photos of the same object or design: photos taken independently by many people across years, environments, cameras, and sometimes physical units. In this work, we introduce Trainspotting, a dataset of 12,068 objects and 311,886 photos from Wikimedia Commons. We reconstruct each object to recover camera poses, multi-view stereo depth, and object masks. We categorize the objects into three regimes: objects fixed at one site, objects that move between sites, and designs shared by many physical units. Evaluating recent feedforward reconstruction models on Trainspotting shows that they fail most severely in the last two regimes. Fine-tuning VGGT-$Ω$ on Trainspotting significantly improves camera pose, depth, and 3D geometry on held-out objects. We observe similar improvements on the independent NAVI in-the-wild benchmark, which contains photos of each object in different environments. Performance on conventional benchmarks remains largely unchanged.

### 🤖 AI 总结

**一句话总结**：State-of-the-art feedforward reconstruction models perform poorly on in-the-wild object-centric photo collections. They are trained largely on single-session object captures whose images vary in viewp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Trainspotting, Learning, Object-Centric, Reconstruction, Found, Photos, State-of-the-art

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06849v1) | [下载PDF](https://arxiv.org/pdf/2611.06849v1.pdf)

---

## [22. Where to Connect? Boosting MLLMs via Dynamic Gated Pathways across ALL ViT and LLM Layers](https://arxiv.org/abs/2611.06844v1)

**作者**：Yingying Yan, Jiaqi Tang, Wei Wei 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-04

### 📄 论文摘要

A central yet under-explored question in Multimodal Large Language Models (MLLMs) is where to connect---how visual information from a hierarchical vision encoder should be wired into the layer-wise semantics of a large language model. Mainstream MLLMs inject a fixed single-layer visual representation into the LLM and treat all LLM layers as a single consumer, ignoring that different layers demand different visual granularities. Recent multi-layer fusion methods either compress hierarchical features on the encoder side or rely on predefined sparse or hierarchical layer-to-layer connections, and therefore stop short of modeling adaptive cross-layer interactions between the ViT and LLM hierarchies. We address this gap with DGP (Dynamic Gated Pathways), a routing mechanism that establishes all-to-all connections between every ViT layer and every LLM layer, with each LLM layer dynamically gating its preference over visual layers conditioned on its own semantic state. Built on top of LLaVA-1.5-7B and 13B, DGP delivers consistent gains over the LLaVA-1.5-7B baseline (e.g., +4.2 on SQA$^{I}$, +3.3 on MM-Vet, +3.1 on VizWiz and LLaVA$^{W}$) and surpasses prior multi-layer visual fusion methods on most benchmarks. Layer-wise routing analyses further show that different LLM layers do select different visual granularities on demand, supporting both the effectiveness and interpretability of the proposed dynamic gated pathways. The code is available: https://github.com/YingyingYan1/DGP.

### 🤖 AI 总结

**一句话总结**：A central yet under-explored question in Multimodal Large Language Models (MLLMs) is where to connect---how visual information from a hierarchical vision encoder should be wired into the layer-wise se...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Where, Connect?, Boosting, MLLMs, via, Dynamic, Gated, Pathways

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06844v1) | [下载PDF](https://arxiv.org/pdf/2611.06844v1.pdf)

---

## [23. Same Layout, Different Count: What Number Words Do Past Ten in Text-to-Image Models](https://arxiv.org/abs/2611.06840v1)

**作者**：Liang Yue, Eric A. Vance  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-04

### 📄 论文摘要

Ask SD3.5-Medium for twelve of an object and then, from the same starting noise, for twenty-five. The picture keeps its layout, but the count changes about as much as it would under a new random seed, and in no consistent direction. We study what number words do once a request passes about ten objects, in five open text-to-image models. Holding the object and the starting noise fixed, we change one thing at a time, and people who never see the request count 3,088 of the images. Every model follows the number for small crowds, but only up to a point, its reach: SD3.5-M and FLUX.1-dev stop following it soon after ten, while FLUX.2 [klein] and Qwen-Image follow it loosely up to twenty-five. Beyond SD3.5-M's reach, the coarse part of the starting noise fixes the composition of the picture but not how many objects it holds: redrawing only the noise finer than an eighth of the image keeps the layout as well as a new number does, and already moves the count two-thirds as far. The number word still reaches the denoiser and acts in its first steps, but nothing we tried gives it a clear direction. Shown instead as a noised grid in the starting latent, the count is drawn: people find it in 59% of images, against 4% when it is only told. Past ten, an exact-match score barely separates a model that follows the number loosely from one that ignores it, and a relative-error score can even prefer a constant guess of sixteen. A same-noise test with a few requests per object tells them apart.

### 🤖 AI 总结

**一句话总结**：Ask SD3.5-Medium for twelve of an object and then, from the same starting noise, for twenty-five. The picture keeps its layout, but the count changes about as much as it would under a new random seed,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, Same, Layout, Different, Count, What, Number, Words

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06840v1) | [下载PDF](https://arxiv.org/pdf/2611.06840v1.pdf)

---

## [24. Open-HumanScale: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models](https://arxiv.org/abs/2611.06817v1)

**作者**：Juncheng Ma, Jiaxin Li, Jiankai Tu 等 31 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-04

### 📄 论文摘要

Egocentric human video offers a scalable source of manipulation priors for robot learning, yet translating raw data scale into generalizable robot policies demands rigorous data curation and training recipes. We introduce Open-HumanScale, the first fully open recipe for scaling egocentric pretraining to 50,000 hours, anchored by Open-HumanScale-50K---a curated egocentric video corpus densely annotated with hand motion and natural language. Leveraging this corpus, we systematically investigate pure human pretraining via closed-loop simulation evaluations and uncover an empirical log-linear scaling law linking pretraining data hours to downstream robot success rates. Grounded in these findings, we develop HumanWAM-Vanilla, a world--action model pretrained exclusively on 50k hours of egocentric human video. Upon robot post-training, HumanWAM-Vanilla reaches 92.08% success on RoboTwin 2.0 Clean2Clean and 68.88% on Clean2Random, alongside a 14.17% mean success rate and a 19.00 mean progress score on RoboDojo. To push the capability frontier further, we explore joint human--robot pretraining with HumanWAM-Goal, a visual-goal-conditioned world--action model. Hybrid data scaling unlocks broad zero-shot generalization across both simulation and physical benchmarks, propelling post-trained RoboTwin 2.0 performance to new state-of-the-art levels: 92.70% on Clean2Clean and a substantial leap to 84.60% on Clean2Random. On physical robots, HumanWAM-Goal further exhibits emergent embodied in-context learning, dynamically adapting its manipulation behavior to unseen visual goals without parameter updates. To support reproducible scaling research in embodied AI, we open-source the Open-HumanScale-50K corpus, data curation and pretraining pipelines, alongside the pretrained and post-trained HumanWAM checkpoints, inference code, and simulation evaluation suites.

### 🤖 AI 总结

**一句话总结**：Egocentric human video offers a scalable source of manipulation priors for robot learning, yet translating raw data scale into generalizable robot policies demands rigorous data curation and training ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Open-HumanScale, Open, Recipe, Scaling, Human, Robot, Experience

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06817v1) | [下载PDF](https://arxiv.org/pdf/2611.06817v1.pdf)

---

## [25. VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation](https://arxiv.org/abs/2611.06796v1)

**作者**：Yihong Luo, Tianyu Pang, Tianyang Hu  
**分类**：cs.CV  
**发布时间**：2026-11-04

### 📄 论文摘要

Few-step distillation offers efficient generation with diffusion and flow models, but preserving quality with only a few sampling steps remains challenging. Distribution-matching methods via score distillation provide a strong foundation, yet they rely on accurately tracking the student's changing distribution. At intermediate generation steps in few-step sampling, student-score estimation can be difficult, and commonly used estimators may describe a different distribution from the one used to update the student. Flow matching allows a more flexible approach to supervision through velocity fields constructed from the student's sampling process. Building on this perspective, we introduce Velocity Adversarial Distillation (VAD), which uses a learned critic to compare student and teacher fields and turn their disagreement into feedback for learning. VAD unifies score distillation, Fisher-based matching, and moment matching, also explaining existing heuristic MMD updates and delivering new training objectives. We further develop VA-TDM, which follows trajectory distribution matching: providing supervision for partial denoising along the student trajectory. Beyond this, VA-TDM combines transition-aware online velocity learning and dual-form VAD supervision across intermediate student transitions. Extensive results show that VA-TDM is powerful for learning few-step generators, achieving state-of-the-art four-step performance in both text-to-image and text-to-video generation across various backbones and scaling effectively to 33B MiniMax-H3. In particular, our VA-TDM-H3 notably outperforms the few-step Fast-H3 and is closer to the original many-step H3 according to human preference.

### 🤖 AI 总结

**一句话总结**：Few-step distillation offers efficient generation with diffusion and flow models, but preserving quality with only a few sampling steps remains challenging. Distribution-matching methods via score dis...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, VA-TDM, Unified, View, Improving, Few-Step, Models, Velocity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06796v1) | [下载PDF](https://arxiv.org/pdf/2611.06796v1.pdf)

---

## cs.LG

## [26. Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement](https://arxiv.org/abs/2611.06905v1)

**作者**：Michal Korniak, Marco Bagatella, Ralf Römer 等 24 位作者  
**分类**：cs.LG, cs.RO  
**发布时间**：2026-11-04

### 📄 论文摘要

The introduction of generalist robot policies has enabled a single, large model to learn to perform a variety of tasks from a vast pre-training corpus. While these models often exhibit powerful zero-shot generalization capabilities, they typically require an adaptation phase to achieve sufficient performance in deployment. Iterated self-improvement via reinforcement learning (RL) has demonstrated promise in enabling this adaptation, yet such approaches have been largely explored in single-task settings - where the goal is to simply improve on a narrow deployment task - which lies in stark contrast to the multi-task capabilities of the base policy. In this work we ask whether generalist robot policies are capable of multi-task, generalist improvement in deployment - targeting many diverse tasks simultaneously - and what algorithmic recipe enables this. To answer this question, we first develop a set of structured evaluations to test generalist improvement capabilities, and systematically evaluate algorithmic and practical design choices regarding value estimation, policy extraction and resource allocation. We show that not only can generalist policies be improved online across diverse tasks, but that the right recipe can enable generalization and increase performance on tasks not considered during online training. We characterize when this generalization occurs and show that both the training task distribution and the use of value-based RL are critical. To the best of our knowledge, this is among the first evidence for online generalist improvement for robot foundation models.

### 🤖 AI 总结

**一句话总结**：The introduction of generalist robot policies has enabled a single, large model to learn to perform a variety of tasks from a vast pre-training corpus. While these models often exhibit powerful zero-s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Reinforcement, Learning, Enables, Scaling, Generalist, Robot, Policy, Improvement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06905v1) | [下载PDF](https://arxiv.org/pdf/2611.06905v1.pdf)

---

## [27. Adaptive Multi Mode: Budget-Aware Routing of Optimizers By Online Landscape Probes](https://arxiv.org/abs/2611.06879v1)

**作者**：Benjamin Jacob Bodner  
**分类**：cs.LG, cs.NE, math.OC  
**发布时间**：2026-11-04

### 📄 论文摘要

The best classical optimizer for a continuous black-box problem depends on its budget and landscape. Existing routers decide from the dimension and budget, past improvement or features fitted to one benchmark, and few test an optimizer's implicit assumptions online. AMM (Adaptive Multi Mode) routes a known budget among quasi-Newton, trust-region, coordinate, multistart and evolution-strategy optimization engines with online probes of curvature, plateaus, separability, kinks, basins and fractal structure. Each probe has a default, a dimension-by-budget validity range and a cost charged to the budget. In its pre-registered development loop on bbob, 32 of 36 predictions held over the last 16 confirmations. AMM was then tested once on held-out bbob instances 101-110 (D=2-40, 10*D-1000*D) against up to seven competitors. It has the highest target share in 382 of 600 function-dimension-budget cells (236 outright, 146 tied) and, by a descriptive posterior rule, is credibly behind in 35, mostly at 10*D and 30*D. At every budget it also leads the controls built from its own engines (the best engine alone, the best engine per dimension and budget, and a greedy schedule), narrowly at 10*D and 30*D, and nevergrad's NgIohTuned. In pre-registered runs its lead over IPOP-CMA-ES holds under affine and box transformations, on box-constrained bbob and, pooled, on rotated f2-f4, but rotating the separable f3 and f4 removes most of the lead there. On held-out MA-BBOB its final share at 2000*D is level with IPOP-CMA-ES's and its anytime area lower. We published AMM as an open-source Python package (pip install amm-optimizer; https://github.com/BjBodner/amm-optimizer).

### 🤖 AI 总结

**一句话总结**：The best classical optimizer for a continuous black-box problem depends on its budget and landscape. Existing routers decide from the dimension and budget, past improvement or features fitted to one b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Adaptive, Multi, Mode, Budget-Aware, Routing, Optimizers, Online

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06879v1) | [下载PDF](https://arxiv.org/pdf/2611.06879v1.pdf)

---

## [28. Navigating Disagreement Among Criteria for Evaluating Explanation Faithfulness](https://arxiv.org/abs/2611.06846v1)

**作者**：Grant Shanklin, Jiří Němeček, Asia Biega  
**分类**：cs.LG, cs.CY  
**发布时间**：2026-11-04

### 📄 论文摘要

Faithfulness requires that algorithmic explanations accurately reflect the model's behavior. Yet existing operationalizations of faithfulness can disagree about whether the same explanation is faithful, leaving developers and auditors to choose among conflicting evaluations. In this paper, we investigate disagreement among evaluation criteria and offer a practical path forward for evaluating explanation faithfulness. We first identify how operationalizations of faithfulness differ. We introduce a faithfulness functional that locates their disagreements in what an explanation claims about the model, which comparisons bear on that claim, and how agreement across those comparisons should be aggregated, and we reconstruct existing evaluation criteria within it. We argue these reconstructions support understanding faithfulness as a common though incompletely specified relation between the model and explanation, so the differences reflect choices left open by the general requirement. Justifying an operationalization then comes down to justifying these choices, which, on our view, draws on explanatory, institutional, and normative considerations. We support this argument with a case study of adverse action notices, reconstructing the evaluation implicit in an industry-proposed procedure and identifying which of its choices the setting justifies and which remain open. Our work gives auditors and practitioners a way to navigate disagreeing evaluations of faithfulness. It also explains why the literature should expect multiple operationalizations, while showing how concrete settings can narrow the choice among them. More broadly, our analysis shows how a shared requirement of faithfulness can support contextually justified evaluations despite disagreement among existing metrics.

### 🤖 AI 总结

**一句话总结**：Faithfulness requires that algorithmic explanations accurately reflect the model's behavior. Yet existing operationalizations of faithfulness can disagree about whether the same explanation is faithfu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Navigating, Disagreement, Among, Criteria, Evaluating, Explanation, Faithfulness, requires

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06846v1) | [下载PDF](https://arxiv.org/pdf/2611.06846v1.pdf)

---

## [29. Systolic Linear Attention: Co-Designing Tile-Grouped Gated Delta Attention for TPUs](https://arxiv.org/abs/2611.06828v1)

**作者**：Gagik Amirkhanyan, Nuojin Cheng  
**分类**：cs.LG  
**发布时间**：2026-11-04

### 📄 论文摘要

Gated-delta linear attention layers such as Gated DeltaNet (GDN), Kimi Delta Attention (KDA), and GDN-2 are tuned for GPUs, where small tensor-core tiles and fast vector registers make per-channel decay rescaling and sequential in-block solves cheap. On Google TPUs, which concentrate compute in wide $256 \times 256$ systolic matrix units backed by a slower vector unit, porting these layers directly leaves half of each matrix tile empty and bottlenecks on vector operations. We present \textbf{Systolic Linear Attention (SLA)}, which reshapes gated delta attention around the matrix unit by widening keys to $256$ with grouped value heads, grouping decay gates into four $64$-channel tiles, and computing the chunk solve entirely with block matrix products in a single fused kernel. On TPU v7x, a full \texttt{SLA-R4} layer runs $1.6\times$--$2.5\times$ faster than the open-source Tokamax KDA kernel ($1.4\times$--$2.4\times$ with exact chunk inversion), driven primarily by head sharing and kernel fusion. Across a $2{,}048$-chip TPU v7x pre-training study of sparse Mixture-of-Experts (MoE) models from $6.5\text{B}$ to $63.1\text{B}$ parameters, SLA trains $11\%$--$24\%$ faster than KDA at similar perplexity, and reaches slightly lower perplexity than KDA in smaller matched-seed runs.

### 🤖 AI 总结

**一句话总结**：Gated-delta linear attention layers such as Gated DeltaNet (GDN), Kimi Delta Attention (KDA), and GDN-2 are tuned for GPUs, where small tensor-core tiles and fast vector registers make per-channel dec...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Systolic, Linear, Attention, Co-Designing, Tile-Grouped, Gated, Delta, TPUs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06828v1) | [下载PDF](https://arxiv.org/pdf/2611.06828v1.pdf)

---

## [30. Message-passing graph persistence](https://arxiv.org/abs/2611.06801v1)

**作者**：Jorge Luiz Franco, Arthur Queiroz Moura, Moacir Ponti 等 4 位作者  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-11-04

### 📄 论文摘要

Message-passing graph neural networks (GNNs) are limited in expressive power by the one-dimensional Weisfeiler-Leman test. Persistent homology (PH) provides topological descriptors that can complement GNN representations, but existing approaches typically compute persistence separately from the representation learning process. In this paper, we introduce Message-Passing Graph Persistence (MGP), a family of topological descriptors that incorporates message passing into graph filtrations. At each filtration step, node embeddings are updated using the current subgraph and associated with persistence events. These embeddings also determine the representatives of connected components during persistence computation. We prove that MGP is invariant under graph isomorphism and that it is strictly more expressive than the PH-based descriptors it extends. We evaluate MGP on an expressivity benchmark and on several graph classification and regression datasets. Experiments show that MGP outperforms other PH-based descriptors on most of these datasets.

### 🤖 AI 总结

**一句话总结**：Message-passing graph neural networks (GNNs) are limited in expressive power by the one-dimensional Weisfeiler-Leman test. Persistent homology (PH) provides topological descriptors that can complement...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Message-passing, graph, persistence, neural, networks, GNNs, limited, expressive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.06801v1) | [下载PDF](https://arxiv.org/pdf/2611.06801v1.pdf)

---

