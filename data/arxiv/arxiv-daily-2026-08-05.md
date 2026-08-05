# arXiv AI 论文日报 | 2026-08-05

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (5 篇)
- [cs.CV](#csCV) (12 篇)
- [cs.LG](#csLG) (6 篇)
- [cs.AI](#csAI) (7 篇)

---

## cs.AI

## [1. ReflectRL: Learning from Golden Negative Trajectories via Reflective-to-Direct Reasoning](https://arxiv.org/abs/2608.03972v1)

**作者**：Jinhe Bi, Chennan Zhou, Zengjie Jin 等 13 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-04

### 📄 论文摘要

On-policy training has emerged as a powerful post-training paradigm for improving the reasoning capabilities of large language models, and is often enhanced by golden trajectories from stronger expert models. However, when the expert fails on harder problems, existing trajectory-guided methods lose their main source of supervision, and these failed trajectories are typically discarded as negative samples. We argue that such failures, which we call Golden Negative Trajectories, can still provide valuable reasoning signals when treated not as demonstrations to imitate, but as flawed trajectories to reflect upon. We identify a Reflection Advantage: for hard problems, reflecting on a flawed trajectory can be easier and more effective than solving the problem directly from scratch. Motivated by this, we propose ReflectRL, a lightweight plug-and-play framework that learns from Golden Negative Trajectories during on-policy training. ReflectRL first uses these trajectories to elicit Reflective Reasoning, then applies Reflective-to-Direct Policy Transition to transfer the acquired reasoning behavior back to Direct Reasoning. Experiments across 9 benchmarks, 4 LLM backbones, and 4 on-policy training methods show that ReflectRL consistently improves reasoning performance with minimal overhead.

### 🤖 AI 总结

**一句话总结**：On-policy training has emerged as a powerful post-training paradigm for improving the reasoning capabilities of large language models, and is often enhanced by golden trajectories from stronger expert...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ReflectRL, Learning, Golden, Negative, Trajectories, via, Reflective-to-Direct, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03972v1) | [下载PDF](https://arxiv.org/pdf/2608.03972v1.pdf)

---

## [2. Interpretable Adaptive Sampling for LLM Test-Time Scaling](https://arxiv.org/abs/2608.03961v1)

**作者**：Mobina Kashaniyan, Ali Jannesari  
**分类**：cs.AI  
**发布时间**：2026-08-04

### 📄 论文摘要

Test-time scaling improves LLM reasoning by generating and aggregating multiple candidate answers, yet many pipelines use fixed per-query budgets that spend the same compute on easy and difficult prompts. These fixed budgets are also difficult to inspect because they do not explain why a given prompt receives a particular number of samples. We propose adaptive} test-time scaling with a lightweight fuzzy controller that maps interpretable signals, including estimated prompt complexity and model confidence, to a per-query sampling budget. The controller assigns fewer samples to easier or more confident prompts and more samples to harder or less certain prompts, making inference-time compute inspectable rather than fixed or opaque. We evaluate under a fair-alignment protocol with matched decoding settings and controlled answer selection, and compare against best-of-$N$, compute-aware scaling, and self-certainty-based baselines on question-answering and mathematical reasoning tasks. Across models and datasets, adaptive fuzzy control improves over several standard baselines and remains close to a selector-matched full-budget control while reducing the average number of samples. These findings suggest that interpretable adaptive sampling is a practical direction for more efficient test-time reasoning in large language models.

### 🤖 AI 总结

**一句话总结**：Test-time scaling improves LLM reasoning by generating and aggregating multiple candidate answers, yet many pipelines use fixed per-query budgets that spend the same compute on easy and difficult prom...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Interpretable, Adaptive, Sampling, Test-Time, Scaling, improves, reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03961v1) | [下载PDF](https://arxiv.org/pdf/2608.03961v1.pdf)

---

## [3. TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring](https://arxiv.org/abs/2608.03952v1)

**作者**：Dongjie Yang, Siyan Lin, Leixian Shen 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-04

### 📄 论文摘要

Large language models (LLMs) are increasingly used to provide conversational practice for English-as-a-second-language (ESL) learners. Effective ESL tutoring, however, requires more than fluent response generation: a tutor must select an appropriate pedagogical action based on learner behavior and dialogue context. Human-tutoring research offers principles for adaptive support, but they are often task-specific and remain insufficiently integrated into LLM-based ESL tutor training and evaluation. We present TACT (Taxonomy-Aligned Conversational Tutor), a human-grounded framework for post-training and evaluating pedagogically adaptive ESL tutors. Drawing on established literature, we develop two complementary taxonomies: the Tutor-Strategy Taxonomy with 13 tutor response strategies and the Student-Move Taxonomy characterizing learner behavior by move type and status. Using these taxonomies, we construct TACTCorpus, which enriches 260 authentic teacher-student conversations with 32,379 annotations and quality-controlled augmented training data. We then post-train Qwen3.5-4B through supervised fine-tuning followed by taxonomy-aligned Group Relative Policy Optimization, producing TACTutor and optimizing it for scaffolding quality rather than reference imitation alone. On TACTBench, a strategy-balanced diagnostic benchmark comprising 78 authentic tutoring contexts, TACTutor improves over its backbone by 20.30% and outperforms all evaluated proprietary baselines under the same protocol, while maintaining backbone performance on established external educational benchmarks; in a blinded study with 50 learners, it also receives the highest overall mean rating among the evaluated tutors. We release the data, benchmark, and model weights, providing an open foundation for developing pedagogically adaptive ESL tutors.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly used to provide conversational practice for English-as-a-second-language (ESL) learners. Effective ESL tutoring, however, requires more than fluent respon...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TACT, Taxonomy-Aligned, Post-Training, Pedagogically, Adaptive, English, Tutoring, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03952v1) | [下载PDF](https://arxiv.org/pdf/2608.03952v1.pdf)

---

## [4. Implementing Causal Perception: Competing SCMs and Situated Fairness](https://arxiv.org/abs/2608.03917v1)

**作者**：Jose M. Álvarez  
**分类**：cs.AI  
**发布时间**：2026-08-04

### 📄 论文摘要

Causal perception occurs when agents with competing Structural Causal Models (SCMs) of the same system infer different probability distributions, including the hypothetical distributions implied by each agent's SCM under the same set of interventions. It shapes how agents reason about the system and how they perceive its fairness. Causal perception is a promising probabilistic framework, but it has remained purely theoretical. This work provides the first implementation of the causal perception framework of Álvarez and Ruggieri (2025). We operationalize structural (agents disagree on the causal graph) and parametrical (agents agree on the causal graph but disagree on its weights) causal perception. We design algorithms for computing interventional and counterfactual distributions and propose suitable distance measures to quantify the disagreement. Using the German Credit dataset, we illustrate how causal perception affects accuracy and fairness in a multi-expert decision setting. We show that the perception verdict is sensitive to the choice of distance metric and threshold. We also show that causal perception changes fairness assessments and threshold-based decisions. Bias proves situated with respect to the agent's SCM, demonstrating that competing worldviews in fairness problems cannot be ignored.

### 🤖 AI 总结

**一句话总结**：Causal perception occurs when agents with competing Structural Causal Models (SCMs) of the same system infer different probability distributions, including the hypothetical distributions implied by ea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Implementing, Causal, Perception, Competing, SCMs, Situated, Fairness, occurs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03917v1) | [下载PDF](https://arxiv.org/pdf/2608.03917v1.pdf)

---

## [5. Socially Grounded Agentic AI: Coordinating Plural Perspectives through Social Theory](https://arxiv.org/abs/2608.03910v1)

**作者**：Matt Ratto, Abhishek Moturu, Daniel Silver  
**分类**：cs.AI, cs.LG, cs.MA  
**发布时间**：2026-08-04

### 📄 论文摘要

As AI systems are deployed across increasingly diverse social contexts, alignment can no longer be framed as the optimization of a single, unified set of values. Instead, systems must be able to recognize, represent, and respond to multiple legitimate perspectives. This has led to growing interest in pluralistic alignment, which seeks to move beyond one-size-fits-all models of appropriate behaviour. However, current approaches often lack a clear account of how values are socially organized, contested, and coordinated in practice. In this paper, we argue that social theory provides essential conceptual and design resources for addressing these challenges. Drawing on established traditions in sociology, we show how perspectives can be understood as structured by roles, shaped through interaction, and distributed across fields of power and expertise. We translate these insights into concrete implications for AI system design, including role-based representations, structured coordination among perspectives, and context-sensitive evaluation. For agentic systems, this requires aligning not only final outputs, but also the role activations, deliberative traces, aggregation rules, and feedback loops through which those outputs are produced. Our contribution is to reposition pluralistic alignment as a problem of socially grounded coordination rather than output diversification. We outline a design space for systems that engage multiple perspectives in structured and accountable ways, and we identify directions for future work to implement and empirically evaluate these approaches in real-world settings.

### 🤖 AI 总结

**一句话总结**：As AI systems are deployed across increasingly diverse social contexts, alignment can no longer be framed as the optimization of a single, unified set of values. Instead, systems must be able to recog...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Socially, Grounded, Agentic, Coordinating, Plural, Perspectives, through, Social

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03910v1) | [下载PDF](https://arxiv.org/pdf/2608.03910v1.pdf)

---

## [6. When Efficiency Becomes Fragility: Exploiting Dynamic Routing Vulnerabilities in Adaptive UAV Tracking](https://arxiv.org/abs/2608.03902v1)

**作者**：Shaofeng Liang, Runwei Guan, Wenshuo Chen 等 10 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-04

### 📄 论文摘要

Resource constraints on UAV platforms have driven a paradigm shift in aerial tracking, from pursuing performance toward balancing accuracy with efficiency. Adaptive Transformer Trackers, which leverage an input-dependent dynamic routing architecture, have emerged as a representative solution to this challenge. However, we reveal that behind this computation-on-demand flexibility hides a critical structural flaw: the Lipschitz singularity of computational path decisions, which has an unbounded local Lipschitz constant at discrete layer-skipping decision boundaries. This mathematical discontinuity renders adaptive tracking networks inherently unstable: tiny input perturbations can be amplified at the gating modules, causing dramatic changes in the inference topology. We formally characterize this singularity in the context of adaptive tracking architectures and, for the first time, identify it as a directly exploitable new attack surface. This insight reveals a previously overlooked and highly vulnerable topological path space attack surface. Based on this, we propose the Adversarial Path-Inversion (API) framework. API generates imperceptible perturbations to precisely manipulate the gating decisions, forcing the inference onto altered computational paths. The severe inconsistency between the original and the inverted paths dismantles the representation capability of the model. Extensive experiments on state-of-the-art adaptive trackers demonstrate that API achieves superior perturbation stealthiness, more effective attack, and faster inference speeds. This work opens a new dimension for the security analysis of dynamic tracking networks and provides a theoretical warning for constructing robust adaptive tracking architectures in the future.

### 🤖 AI 总结

**一句话总结**：Resource constraints on UAV platforms have driven a paradigm shift in aerial tracking, from pursuing performance toward balancing accuracy with efficiency. Adaptive Transformer Trackers, which leverag...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Efficiency, Becomes, Fragility, Exploiting, Dynamic, Routing, Vulnerabilities

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03902v1) | [下载PDF](https://arxiv.org/pdf/2608.03902v1.pdf)

---

## [7. Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition](https://arxiv.org/abs/2608.03892v1)

**作者**：Michal Mráz, Justin Shenk  
**分类**：cs.AI  
**发布时间**：2026-08-04

### 📄 论文摘要

We study linear representations of temporal horizon in the large language model Qwen3-32B and use them to change the model's time-related preferences, recommendations, and capabilities. We train contrastive linear probes on teacher-forced temporal-choice answers to find a short-term versus long-term direction in the model's residual stream, and evaluate contrastive activation-addition steering on a held-out binary temporal-choice task, an out-of-distribution monetary intertemporal-choice task, and a TravelPlanner capability benchmark. The central result is that temporal-horizon directions can be identified with simple contrastive linear probes and then used for steering to induce large, bidirectional preference changes. On an out-of-distribution monetary choice task that varies reward size and delay, steering strongly shifts the model's indifference threshold between smaller-sooner and larger-later rewards in both directions. We further show improvements on a planning-related capability metric under moderate temporal steering. These results suggest that model intertemporal preferences are measurable and steerable, which is relevant for AI systems that give advice involving delayed costs and benefits, and for safety questions about long-horizon planning.

### 🤖 AI 总结

**一句话总结**：We study linear representations of temporal horizon in the large language model Qwen3-32B and use them to change the model's time-related preferences, recommendations, and capabilities. We train contr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Intertemporal, Preference, Steering, Qwen3, via, Contrastive, Activation, Addition

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03892v1) | [下载PDF](https://arxiv.org/pdf/2608.03892v1.pdf)

---

## cs.CL

## [8. SocietyBench: Forecasting Counterfactual Social-World Evolution](https://arxiv.org/abs/2608.04009v1)

**作者**：Zhenran Wang, Zhonghan Bian, Jinsong Li 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-04

### 📄 论文摘要

Large language models (LLMs), and the agents built on top of them, are now benchmarked heavily on whether they can finish a task -- fix a bug, drive a browser, operate a GUI. A complementary social ability, namely how well a model understands and forecasts the way real social events unfold, has barely been measured. We introduce SocietyBench, an end-to-end benchmark that takes a one-line event topic, collects Web news and social-media posts across five platforms, distills them into a date-indexed timeline that keeps factual events and a public-opinion layer separate, and then turns every cutoff date on that timeline into an audited bank of forecasting questions. Questions are scored on two orthogonal 100-point axes: probability calibration and temporal accuracy. Before any model sees a timeline, a three-phase procedure replaces every named entity and shifts every date by a per-event constant, turning a real arc into a counterfactual social world -- structurally identical to what happened, but stripped of the surface labels a model could match against pre-training memory. On five heterogeneous events and 125 prediction points in Chinese and English editions, the strongest of six frontier LLMs reaches only 75.0 out of 100, against a trivial anchor of 50. The two axes come apart: a model can be calibration-strong but time-weak, or the reverse. Three agent frameworks built on a shared base model fail to improve on that base, and two model-free heuristics trail every LLM. Per-event gaps reach 21.4 points on a single axis, which is our main argument for evaluating on several events rather than one. All anonymized timelines, question banks, ground truth, and scoring code are released.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs), and the agents built on top of them, are now benchmarked heavily on whether they can finish a task -- fix a bug, drive a browser, operate a GUI. A complementary social ab...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SocietyBench, Forecasting, Counterfactual, Social-World, Evolution, Large, language, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.04009v1) | [下载PDF](https://arxiv.org/pdf/2608.04009v1.pdf)

---

## [9. WorldCup Arena: Prospective, Leakage-Free Evaluation of Frontier LLMs on a Live Tournament](https://arxiv.org/abs/2608.04008v1)

**作者**：Zhenran Wang, Zhonghan Bian, Jinsong Li 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-04

### 📄 论文摘要

Benchmarks that measure the forecasting ability of large language models are almost always retrospective: the event has happened, the answer is somewhere on the Web, and the evaluation must defend itself against memorisation. We report the opposite design. Over the 39 days of the 2026 FIFA World Cup, six frontier LLMs -- all with extended thinking and native server-side web search -- were asked before every kickoff, one match at a time, to fill in a seven-market prediction card for all 104 matches, plus 12 group winners and a pre-tournament outright pool; no answer existed when the question was asked, so the evaluation is leakage-free by construction rather than by filtering, and the frozen archive holds 4,494 scored predictions. What the tournament establishes is a set of behaviours the six systems share. On match outcome they average 63.9%, level with backing the bookmaker's favourite -- which is in fact what they usually do. They agree with one another far more often than they are right, so a majority vote adds nothing. They under-commit to draws and to goals, and crowd their scoreline picks onto a single prototypical result. Accuracy tracks how lopsided a fixture is rather than how much is known about it: it collapses in the closest ties, where the dossiers are richest, while questions about the tournament as a whole are answered well. On this task the current generation of frontier systems is not sharply differentiated: the standings hold up at the top and the bottom across the run and churn in the middle, and the margins stay narrow throughout. The briefing dossiers, fixtures and official results are released as a benchmark, together with the scoring code.

### 🤖 AI 总结

**一句话总结**：Benchmarks that measure the forecasting ability of large language models are almost always retrospective: the event has happened, the answer is somewhere on the Web, and the evaluation must defend its...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, WorldCup, Arena, Prospective, Leakage-Free, Evaluation, Frontier

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.04008v1) | [下载PDF](https://arxiv.org/pdf/2608.04008v1.pdf)

---

## [10. PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents](https://arxiv.org/abs/2608.04003v1)

**作者**：Shuhan Xue, Zixin Ding, Yichen Shen 等 9 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-04

### 📄 论文摘要

Recursive self-improvement requires agents to turn accumulated experience into better future behavior. Personal AI agents offer a concrete setting for studying this capability because they retain preferences, task histories, tool routines, and learned skills across sessions. Yet whether retained experience actually improves them over time has not been systematically tested. We introduce PAST-Bench, a benchmark designed to isolate this question. Each agent runs through ordered sequences of fresh-session tasks under matched conditions that turn retained experience on and off. It spans 26 scenarios and 204 episodes across memory, procedural reuse, information gathering, and update. We report both later-task gains and whether those gains follow the intended save, retrieve, and update pathway. Across seven base models and four agent frameworks, improvement is real but uneven across capabilities. Agents with the same headline gain can differ markedly in whether that gain is supported by evidence of the intended pathway. Guided by these findings, we develop Hermes+, which extends Hermes with five targeted interventions across stages of the agent loop. Hermes+ raises the average gain from retained experience and provides clearer pathway evidence, with its strongest improvement on tasks requiring outdated state to be replaced, although the effect remains capability- and model-dependent. Together, PAST-Bench and Hermes+ provide an evaluation and diagnostic foundation for studying how persistent agents can progress from retaining experience to systematically improving through it. Code: https://github.com/Gen-Verse/PAST-Bench

### 🤖 AI 总结

**一句话总结**：Recursive self-improvement requires agents to turn accumulated experience into better future behavior. Personal AI agents offer a concrete setting for studying this capability because they retain pref...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, PAST-Bench, Benchmarking, Foundations, Recursive, Self-Improvement, Personal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.04003v1) | [下载PDF](https://arxiv.org/pdf/2608.04003v1.pdf)

---

## [11. HalluTruthQA-4K: A Fine-Grained Corpus and Annotation Process for Arabic Hallucination Detection and Truth Verification](https://arxiv.org/abs/2608.03966v1)

**作者**：Salah Eddine Bekhouche, Abdessalam Bouchekif, Hichem Telli 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-04

### 📄 论文摘要

Large language models can generate fluent Arabic answers while introducing factual errors that are difficult to identify and verify. Existing Arabic hallucination resources often assign a binary label to an entire response, indicating whether it is hallucinated or non-hallucinated, but provide limited information about the exact erroneous content, the reason for the error, or the correct factual answer. We present HalluTruthQA-4K, an expanded version of the HalluTruthQA resource containing 4,000 expert-curated Arabic question-answering instances across four knowledge-intensive domains: Islamic knowledge, history, science, and geography. Serving as the official dataset for Track 2 of the HalluScoring 2026 shared task, HalluTruthQA-4K extends our original corpus to 4,000 instances. Each instance pairs an Arabic question with a model-generated response, a verified reference answer, and five plausible distractors. Hallucinated responses are additionally annotated with character-level erroneous spans, human-written explanations, and hierarchical hallucination types. The corpus contains 1,643 hallucinated and 2,357 non-hallucinated responses, with 1,843 annotated erroneous spans. We describe the resource construction and annotation methodology, including question selection, controlled answer generation, candidate construction, expert annotation, independent verification, adjudication, and quality control. We also document the annotation guidelines, taxonomy, data format, inter-annotator agreement, and corpus statistics. HalluTruthQA-4K provides a reusable resource for hallucination detection, span-level error localization, explanation generation, factual verification, and the broader evaluation of factual reliability in Arabic language models.

### 🤖 AI 总结

**一句话总结**：Large language models can generate fluent Arabic answers while introducing factual errors that are difficult to identify and verify. Existing Arabic hallucination resources often assign a binary label...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HalluTruthQA-4K, Fine-Grained, Corpus, Annotation, Process, Arabic, Hallucination, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03966v1) | [下载PDF](https://arxiv.org/pdf/2608.03966v1.pdf)

---

## [12. ANNOTARES: A Dataset for Extracting Logical Structures from German Statutory Texts](https://arxiv.org/abs/2608.03898v1)

**作者**：Ronja Schwarz, Jannik Strötgen  
**分类**：cs.CL  
**发布时间**：2026-08-04

### 📄 论文摘要

The automatic structural analysis of legal texts is a cornerstone of legal technology, yet the extraction of their logical components remains a significant challenge. In this paper, we introduce the task of identifying and segmenting legal conditions (Tatbestand) and legal consequences (Rechtsfolge) within German statutory texts. To support this task, we present ANNOTARES (Annotations of Tatbestand-Rechtsfolge Sequences), a novel dataset comprising German law texts with span-level annotations. Spanning three distinct legal codes, the dataset is designed to evaluate both domain-specific performance and cross-statute generalizability. We benchmark diverse architectural approaches: a rule-based baseline, CRFs, BiLSTMs, BiLSTM-CRF, and modern Transformer-based models, including BERT variants and LLM-based methods. Our results demonstrate that BERT and LLM-based models achieve superior performance in capturing the complex syntactic structures of legal language. We release our dataset to facilitate further research in automated legal reasoning.

### 🤖 AI 总结

**一句话总结**：The automatic structural analysis of legal texts is a cornerstone of legal technology, yet the extraction of their logical components remains a significant challenge. In this paper, we introduce the t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ANNOTARES, Dataset, Extracting, Logical, Structures, German, Statutory, Texts

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03898v1) | [下载PDF](https://arxiv.org/pdf/2608.03898v1.pdf)

---

## cs.CV

## [13. Perceptual Anchoring: Prototype-Guided Text Calibration for Training-free Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2608.03991v1)

**作者**：Wanli Ma, Jiangwen Lu, Qinmu Peng 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-04

### 📄 论文摘要

Training-free open-vocabulary semantic segmentation (OVSS) partitions an image into semantically distinct regions based on arbitrary text descriptions, without learning any additional parameters. However, existing methods typically focus on improving visual representations while treating text embeddings that encode only generic category concepts as fixed classification references. The resulting semantic gap between these generic concepts and the visual representations that capture the specific appearances of target instances often causes incomplete masks and erroneous predictions in non-target regions. Inspired by the symbol-percept correspondence underlying perceptual anchoring, we propose Prototype-Guided Text Calibration (PTC) for training-free OVSS. In the Perceiving stage, PTC selects reliable visual evidence based on initial matching scores to construct category-specific visual prototypes. In the Anchoring stage, PTC uses these prototypes to calibrate their corresponding text embeddings, with the calibration strength adaptively adjusted based on the amount of visual evidence. Consequently, the calibrated text embeddings align more accurately with instance-specific visual representations while preserving generic category semantics and open-vocabulary generalization. Moreover, PTC requires neither additional training nor external models and can serve as a plug-and-play module for existing methods. Extensive experiments across eight benchmarks show that PTC significantly enhances the performance of six representative methods and yields more complete and accurate segmentation results. These results validate PTC as a simple and effective approach to improving visual-text alignment.

### 🤖 AI 总结

**一句话总结**：Training-free open-vocabulary semantic segmentation (OVSS) partitions an image into semantically distinct regions based on arbitrary text descriptions, without learning any additional parameters. Howe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Perceptual, Anchoring, Prototype-Guided, Text, Calibration, Training-free, Open-Vocabulary, Semantic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03991v1) | [下载PDF](https://arxiv.org/pdf/2608.03991v1.pdf)

---

## [14. Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent](https://arxiv.org/abs/2608.03979v1)

**作者**：Zhen Fang, Yu Zeng, Wenxuan Huang 等 20 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-04

### 📄 论文摘要

We introduce Video-DeepResearch (Video-DR), extending multimodal agents from static images to continuous video streams, a setting that demands dense spatiotemporal grounding coupled with open-web exploration. Preliminary evaluations reveal two critical bottlenecks in current models: (1) modality bias, where agents bypass visual tools in favor of textual search, and (2) parametric knowledge leakage, where models rely on internal memory rather than genuine tool-augmented execution. To address these challenges, we propose Video-DR, featuring a decoupled perception-exploration pipeline with stage-wise tool unlocking that compels exhaustive cross-frame visual grounding prior to web retrieval. Our framework adopts a two-stage training recipe: supervised fine-tuning followed by Group Relative Policy Optimization (GRPO), enabling autonomous exploration that breaks the imitation-learning ceiling. Furthermore, we curate Video-DR-Bench, a human-AI collaborative benchmark comprising 200 complex, multi-hop VQA instances. Empirical results demonstrate that our Video-DeepResearch-35B-A3B establishes a new state-of-the-art of 64.0% average accuracy, surpassing proprietary Claude-4.5-Sonnet (59.0%) by 5.0 points and significantly outperforming GPT-5 (52.5%) and Gemini 2.5 Pro (57.5%). The 30B-A3B variant achieves 59.3%, competitive with Claude-4.5-Sonnet and demonstrating the effectiveness of our training paradigm even at compact scale. Code: https://github.com/Osilly/Vision-DeepResearch.

### 🤖 AI 总结

**一句话总结**：We introduce Video-DeepResearch (Video-DR), extending multimodal agents from static images to continuous video streams, a setting that demands dense spatiotemporal grounding coupled with open-web expl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, We, Video-DeepResearch, Towards, Next-Generation, Multimodal, Deepresearch, introduce

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03979v1) | [下载PDF](https://arxiv.org/pdf/2608.03979v1.pdf)

---

## [15. JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://arxiv.org/abs/2608.03974v1)

**作者**：Yicheng Xiao, Wenxun Dai, Xinran Qin 等 25 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-04

### 📄 论文摘要

Real-time video editing requires low-latency causal generation with bounded computational resources while preserving source fidelity and long-term temporal consistency. We present JoyAI-Video-Edit, a 16B-parameter autoregressive diffusion framework for real-time, open-ended video editing without access to future frames or a predefined video duration. Our method combines chunk-wise autoregressive adaptation, Source-Anchored Distribution Matching Distillation (SA-DMD), and Long-Horizon Autoregressive Distillation to reduce train--inference mismatch, preserve source fidelity during two-step generation, and mitigate accumulated temporal drift. Extensive automatic and human evaluations show that JoyAI-Video-Edit substantially outperforms existing streaming editors and remains competitive with strong offline systems on both short and long videos. The complete system achieves end-to-end 720p video editing at approximately 30 FPS on a single Nvidia B200 GPU. Code is available at https://github.com/jd-opensource/JoyAI-Video-Edit.

### 🤖 AI 总结

**一句话总结**：Real-time video editing requires low-latency causal generation with bounded computational resources while preserving source fidelity and long-term temporal consistency. We present JoyAI-Video-Edit, a ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, JoyAI-Video-Edit, Real-Time, Open-Ended, Video, Editing, Autoregressive, requires

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03974v1) | [下载PDF](https://arxiv.org/pdf/2608.03974v1.pdf)

---

## [16. UniWorld-Design: From Pixel Generation to Layer-Native Design](https://arxiv.org/abs/2608.03971v1)

**作者**：Zongjian Li, Zhiyuan Yan, Chenxu Bai 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-04

### 📄 论文摘要

We introduce UniWorld-Design, a framework that redefines image generation from flat pixel synthesis to structured visual composition, with semantic RGBA layers as the atomic units of generation, understanding, and editing. Our key insight is that pixels define how an image is rendered, whereas layers define how an image is created, understood, and edited. Just as human designers create and manipulate visual content through layers rather than raw pixels, UniWorld-Design equips multimodal generative models with a layer-native design space. UniWorld-Design comprises two models. The Text-to-RGBA (T2RGBA) model generates standalone RGBA assets directly from text. The Image-to-Layer (I2L) model conditions on a finished image, a global instruction and per-layer prompts, and jointly produces ordered, complete semantic RGBA layers. Its instruction interface supports top-level decomposition, recursive decomposition and targeted extraction, making layering an instruction-addressable operation for agentic editing. Because I2L learns complete semantic objects rather than visible-pixel partitions, its layers stay usable when moved or removed. On the Crello benchmark, I2L reduces per-layer RGB L1 error by 37% and achieves a 34% relative improvement in Alpha Soft IoU over Qwen-Image-Layered. Separately, T2RGBA achieves the highest CLIP Score, outperforming LayerDiffuse and OmniAlpha.

### 🤖 AI 总结

**一句话总结**：We introduce UniWorld-Design, a framework that redefines image generation from flat pixel synthesis to structured visual composition, with semantic RGBA layers as the atomic units of generation, under...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, UniWorld-Design, Pixel, Generation, Layer-Native, Design, introduce, framework

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03971v1) | [下载PDF](https://arxiv.org/pdf/2608.03971v1.pdf)

---

## [17. Progressive Learning of a Diffusion-based Inpainting Model for Separating Overlapped Fingerprints](https://arxiv.org/abs/2608.03937v1)

**作者**：Noor Hussein, Anil K. Jain, Karthik Nandakumar  
**分类**：cs.CV, cs.CR  
**发布时间**：2026-08-04

### 📄 论文摘要

Overlapped friction ridge patterns are a recurring problem in latent fingerprints recovered from crime scenes and in live-scan scenarios where residual fingerprints on the sensor may corrupt subsequent acquisitions. Existing approaches for separating overlapped fingerprints either rely on rule-based orientation field completion that requires strong domain knowledge or train end-to-end deep neural networks that do not account for domain-specific considerations. This work introduces a diffusion-based pipeline for separating component fingerprints from an image containing overlapping friction ridge patterns. We formulate the separation problem as an inpainting task and progressively learn a diffusion model for this task in multiple stages. Starting from a pre-trained Stable Diffusion model, we progressively incorporate a fingerprint prior, add the ability to complete partial fingerprints, and finally propose \textbf{overlap-aware inpainting} that reconstructs each component print using a diffusion inpainting model based on multi-channel conditioning. Experiments on two public datasets demonstrate that component fingerprints reconstructed using the proposed diffusion-based inpainting method can match with their mated counterparts with very high probability.

### 🤖 AI 总结

**一句话总结**：Overlapped friction ridge patterns are a recurring problem in latent fingerprints recovered from crime scenes and in live-scan scenarios where residual fingerprints on the sensor may corrupt subsequen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Progressive, Learning, Diffusion-based, Inpainting, Model, Separating, Overlapped

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03937v1) | [下载PDF](https://arxiv.org/pdf/2608.03937v1.pdf)

---

## [18. GeoMAR: Unleashing Geometrically Aligned Features for Masked Autoregressive Blind Face Restoration](https://arxiv.org/abs/2608.03923v1)

**作者**：Lu Gan, Hanyu Yan, Chaofeng Chen 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-04

### 📄 论文摘要

Codebook-based blind face restoration (BFR) often suffers from ambiguous conditioning features and a fragile prediction mechanism under severe degradation. To address these challenges, we propose GeoMAR, a framework designed to unleash geometrically aligned features with masked autoregressive (MAR) refinement for robust face restoration. For feature conditioning, we introduce a dual-input extraction pipeline to extract component-based geometric descriptions with explicit, spatially faithful anchors. These textual priors are integrated with low-quality (LQ) features via an Aligned Geometric Priors Injector, which employs a KV-Q exchange strategy to generate geometrically aligned features. For prediction mechanism, we reformulate the one-step mapping into a multi-step MAR process. This coarse-to-fine generation progressively refines complex facial regions based on increasingly reliable context. Experiments on one synthetic and three real-world benchmarks demonstrate that GeoMAR achieves highly competitive perceptual quality and coherent visual structures compared with existing methods. The code is available at https://github.com/BRL-SYSU/GeoMAR.git.

### 🤖 AI 总结

**一句话总结**：Codebook-based blind face restoration (BFR) often suffers from ambiguous conditioning features and a fragile prediction mechanism under severe degradation. To address these challenges, we propose GeoM...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GeoMAR, Unleashing, Geometrically, Aligned, Features, Masked, Autoregressive, Blind

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03923v1) | [下载PDF](https://arxiv.org/pdf/2608.03923v1.pdf)

---

## [19. Low-Dimensional High-Leverage Subspace Optimization: Beyond Full-Parameter Coupled Training for Neural Network Quantization](https://arxiv.org/abs/2608.03919v1)

**作者**：Peng Xia, Junbiao Pang, Zheng Huang  
**分类**：cs.CV  
**发布时间**：2026-08-04

### 📄 论文摘要

Low-bit quantization suffers severe accuracy degradation on compact networks, rooted in the dominant full-parameter coupled training paradigm that ignores parameter subspace heterogeneity. Their limited feature redundancy leaves little room to absorb quantization errors. Conventional pipelines adopt monolithic optimization: PTQ reconstructs fixed pretrained models without improving inherent quantization friendliness; QAT updates all parameters jointly, suffering from gradient coupling between backbone weights and calibration parameters. In this paper, we identify normalization affine parameters as a low-dimensional high-leverage subspace dominating quantization robustness, and propose Normalization Affine Preconditioning (NAP) for targeted subspace optimization. For PTQ, NAP freezes backbone weights and fine-tunes only affine parameters under the target fake-quantization graph on full-precision models, proactively boosting quantization friendliness before downstream reconstruction. For QAT, we introduce an alternating QAT-NAP schema that decouples feature learning and numerical calibration, breaking the performance ceiling of saturated joint training. Theoretical analysis confirms BN affine parameters fully cancel the channel-wise affine component of quantization distortion, while nonlinear rounding and clipping residuals form the irreducible error boundary; distillation-guided NAP acts as directional flatness optimization, projecting teacher-student logit mismatch onto the restricted subspace. Experiments on ImageNet and CIFAR-100 show NAP recovers severely collapsed low-bit quantization, consistently boosts reconstruction-based PTQ, and outperforms saturated full-parameter QAT with negligible tuning cost. This work reveals the principle of targeted low-dimensional subspace optimization, offering a new perspective beyond full-parameter coupled training for efficient deep learning.

### 🤖 AI 总结

**一句话总结**：Low-bit quantization suffers severe accuracy degradation on compact networks, rooted in the dominant full-parameter coupled training paradigm that ignores parameter subspace heterogeneity. Their limit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Low-Dimensional, High-Leverage, Subspace, Optimization, Beyond, Full-Parameter, Coupled, Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03919v1) | [下载PDF](https://arxiv.org/pdf/2608.03919v1.pdf)

---

## [20. When and Where to Look: Adaptive Visual Evidence Scheduling for Efficient Long Video Understanding](https://arxiv.org/abs/2608.03918v1)

**作者**：Ke Li, Jiayu Chen, Maoliang Li 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-04

### 📄 论文摘要

Efficient long-video understanding requires vision--language models (VLMs) to reason over a small number of frames selected as sparse visual evidence. Existing relevance-based methods rely on static one-shot selection with fixed frame budgets and candidate pools, while agent-based schedulers achieve adaptivity through costly multi-round reasoning and interactive search. We propose EcoFrame, a training-free framework for low-overhead query-adaptive visual evidence scheduling. EcoFrame leverages the VLM's inference feedback to determine when to increase the frame budget and where to search for additional candidate evidence. Specifically, entropy-gated budget scheduling uses output uncertainty to stop early when the current evidence is sufficient or progressively expand the frame budget otherwise. Meanwhile, attention-guided candidate proposal converts frame-level attention into a temporal prior, enabling dense local search in informative regions while preserving global coverage when attention is diffuse. Experiments on Video-MME, LongVideoBench, and MLVU demonstrate that EcoFrame achieves a better accuracy--efficiency trade-off across multiple VLM backbones. On Qwen2.5-VL, EcoFrame achieves an average accuracy of 64.4, surpassing BOLT at 63.5, while providing a $1.85\times$ speedup over AKS and BOLT. Compared with the agent-based A.I.R., EcoFrame maintains comparable accuracy with up to a $13.5\times$ inference speedup. Code will be available at https://github.com/AK-DREAM/EcoFrame.

### 🤖 AI 总结

**一句话总结**：Efficient long-video understanding requires vision--language models (VLMs) to reason over a small number of frames selected as sparse visual evidence. Existing relevance-based methods rely on static o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Where, Look, Adaptive, Visual, Evidence, Scheduling, Efficient

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03918v1) | [下载PDF](https://arxiv.org/pdf/2608.03918v1.pdf)

---

## [21. StreamDAM: Presence-Aware Memory for Real-Time Streaming Video Object Segmentation](https://arxiv.org/abs/2608.03912v1)

**作者**：Xiang Chen  
**分类**：cs.CV  
**发布时间**：2026-08-04

### 📄 论文摘要

Quality-tier video object segmentation (VOS) trackers such as DAM4SAM top accuracy leaderboards, but they are measured offline, one frame at a time with no clock. Under an honest streaming protocol at 30 frames per second, where a frame that misses its budget is served the last mask already computed, the winner collapses: the rich memory that makes it accurate is too slow to keep up, and what it emits is blind to whether the object is even present. We trace both failures to one place, the tracker's memory pipeline, and rebuild it for streaming. \method{} makes the memory machinery itself run at frame rate through in-model optimization rather than a bolted-on fallback, and governs it with a single learned presence signal that decides what enters memory, how far back the tracker reads, when to withhold output, and when to re-detect. A mechanism analysis shows why a fixed policy cannot win: the control that helps when an object truly disappears is the one that hurts when it is merely hard to see, so the choice must be made per frame. Across four benchmarks and five modern baselines, \method{} is the strongest streaming tracker, recovers nearly all of the offline model's accuracy under the clock, and on the hardest content exceeds the offline model it is built from.

### 🤖 AI 总结

**一句话总结**：Quality-tier video object segmentation (VOS) trackers such as DAM4SAM top accuracy leaderboards, but they are measured offline, one frame at a time with no clock. Under an honest streaming protocol at...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：StreamDAM, Presence-Aware, Memory, Real-Time, Streaming, Video, Object, Segmentation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03912v1) | [下载PDF](https://arxiv.org/pdf/2608.03912v1.pdf)

---

## [22. UniEvo-RS: Omni-Prompt Unified Remote Sensing Segmentation with Representative Exemplar-Driven Prototype Evolution](https://arxiv.org/abs/2608.03911v1)

**作者**：Kunquan Zhang, Peilang Li, Xikun Hu 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-04

### 📄 论文摘要

Prompt-driven vision-language models (VLMs) hold immense promise for accelerating dense remote sensing (RS) annotation, but static models suffer from severe performance degradation when deployed on novel scenes, unseen categories, or visually confusing backgrounds. Moreover, existing unified paradigms primarily rely on intra-image specific prompts, lacking flexible task routing to adapt to multi-intent operational workflows. In practical batch mapping, annotators typically refine a small set of representative samples before processing large datasets. Motivated by this practice, we propose UniEvo-RS, an omni-prompt unified RS segmentation framework equipped with representative exemplar-driven prototype evolution. First, we construct a multi-instruction prompt dataset that unifies text-driven and visual-driven prompts within a single architecture, establishing a dynamic task-routing mechanism for highly diverse RS annotation scenarios. Second, we introduce a representative feedback-driven, training-free prototype evolution mechanism. By contrasting manual annotations with initial predictions on exemplars, UniEvo-RS distills prediction errors into positive and negative prototypes. These prototypes enhance LLM query recall and suppress spatial background noise under a fixed-budget clustering memory. Extensive experiments show that UniEvo-RS unifies diverse prompting tasks, achieving state-of-the-art performance across most settings. Crucially, with minimal interaction on a few exemplars, it enables training-free, progressive accuracy enhancement on unseen categories during batch annotation.

### 🤖 AI 总结

**一句话总结**：Prompt-driven vision-language models (VLMs) hold immense promise for accelerating dense remote sensing (RS) annotation, but static models suffer from severe performance degradation when deployed on no...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UniEvo-RS, Omni-Prompt, Unified, Remote, Sensing, Segmentation, Representative, Exemplar-Driven

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03911v1) | [下载PDF](https://arxiv.org/pdf/2608.03911v1.pdf)

---

## [23. NCGR: Noise-Conditional Gated Rectification for Camera Extrinsic Perturbations in BEV 3D Object Detection](https://arxiv.org/abs/2608.03895v1)

**作者**：Wenbin Pan, Wanhao Liu, Liwei Luo 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-04

### 📄 论文摘要

Camera-based bird's-eye-view (BEV) 3D detection typically assumes accurate and fixed camera extrinsics. In detectors using spatial cross-attention (SCA), extrinsic perturbations displace the image-plane projections of BEV reference points, causing queries to sample features from incorrect regions and degrading detection performance. To address this failure mode, Noise-Conditional Gated Rectification (NCGR) is proposed to compensate for projection errors without explicitly estimating a full six-degree-of-freedom extrinsic correction. For each query-camera pair, a 2D rectification offset is predicted and modulated by a camera-level gate to rectify the base projection before native deformable sampling. During training, the perturbation-derived quantities used to construct the condition and gate are gradually replaced through scheduled interpolation by counterparts generated from an auxiliary scalar predicted from camera features. This transition enables blind inference without perturbation metadata. During training, a weight-shared clean-teacher/perturbed-student pair is used, and the rectification module is supervised by a BEV-consistency objective between the two branches. NCGR is evaluated on nuScenes with simulated dynamic and static extrinsic perturbations. In a five-camera dynamic stress test, NCGR achieves 39.69% NDS, compared with 28.00% for BEVFormer and 33.23% for CAPE. Under clean extrinsics, NCGR maintains performance comparable to that of BEVFormer.

### 🤖 AI 总结

**一句话总结**：Camera-based bird's-eye-view (BEV) 3D detection typically assumes accurate and fixed camera extrinsics. In detectors using spatial cross-attention (SCA), extrinsic perturbations displace the image-pla...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：NCGR, Noise-Conditional, Gated, Rectification, Camera, Extrinsic, Perturbations, BEV

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03895v1) | [下载PDF](https://arxiv.org/pdf/2608.03895v1.pdf)

---

## [24. CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary Supervision, Reward-Aligned Learning, and Tool-Augmented Measurement](https://arxiv.org/abs/2608.03890v1)

**作者**：Mercy Prasanna Ranjit, Anirban Porya, Sathvik Joel 等 11 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-04

### 📄 论文摘要

A clinically useful chest X-ray system must go beyond fluent report generation: it should classify findings with tunable decision thresholds, localize them spatially, and derive the anatomical measurements upon which many diagnoses depend. Today's Vision-Language Models (VLMs) treat these as separate problems, if they address them at all, leaving a gap between what radiologists need and what generative models provide. We introduce CARE-X, a chest X-ray VLM that narrows this gap by unifying auxiliary discriminative supervision with reward-aligned generation. CARE-X augments its generative backbone with focal-loss classification and composite-loss grounding heads, co-trained alongside the language-modeling objective. This auxiliary supervision produces discriminative diagnostic predictions with tunable decision thresholds and precise spatial localization while also improving report quality, providing evidence that structured prediction and generation reinforce one another. Building on this foundation, Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO) leverages task-specific reward signals for report generation, visual question answering (VQA), and spatial grounding, directly optimizing the clinical quality metrics that matter in practice. The result is state-of-the-art performance on the majority of metrics across four report-generation benchmarks, 94.0% VQA accuracy on ReXVQA (+6.0 pp over the next-best baseline), and generative spatial decoding that reaches near parity with dedicated detection heads. Separately, to address measurement-dependent diagnoses, we couple Qwen3-VL-4B-Instruct with native tool-calling capabilities for invoking deterministic measurement tools, while retaining full visual access to the image. This hybrid inference yields +43.6 pp average F1 over perception-only baselines across five measurement-dependent conditions.

### 🤖 AI 总结

**一句话总结**：A clinically useful chest X-ray system must go beyond fluent report generation: it should classify findings with tunable decision thresholds, localize them spatially, and derive the anatomical measure...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CARE-X, Towards, Clinically, Useful, Radiology, VLMs, Auxiliary, Supervision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03890v1) | [下载PDF](https://arxiv.org/pdf/2608.03890v1.pdf)

---

## cs.LG

## [25. Assessment of Conditional Diffusion Model for Synthetic Histopathology Image Generation](https://arxiv.org/abs/2608.03990v1)

**作者**：Seyed Kahaki, Shijie Li, Weijie Chen 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-04

### 📄 论文摘要

Synthetic histopathology image generation has emerged as an approach that may address data scarcity in computational pathology, yet current evaluation methodologies may not fully assess synthetic data quality for medical applications. This work investigates and addresses limitations in existing evaluation metrics, investigating an approach for assessing synthetic histopathology image quality through domain-specific metrics and downstream task validation. We show that conventional synthetic data evaluation metrics such as Frechet Inception Distance (FID) and Inception Score (IS) may have limitations when applied to histopathology images due to their reliance on ImageNet-pretrained feature extractors. To address these limitations, we propose for consideration modified FID and IS approaches utilizing foundation models pretrained on digital pathology datasets, supplemented by precision-recall based metrics as part of an additional quality assessment. Using conditional denoising diffusion models trained on four benchmark datasets, with a two-step training approach, we generated synthetic datasets with systematically varied quality characteristics. We also measured the correlation between the synthetic data quality metrics with downstream nuclei segmentation performance using common metrics including the aggregated Jaccard index (AJI+) and the Dice coefficient. The study results suggest that pathology-specific metrics may provide improved discriminative power. Specifically, the modified Inception Score indicates higher correlation with downstream task performance (r=0.6096 with AJI+, p=0.0122), compared to the original IS (r=0.0708, p=0.7944). Our observations indicate that increasing the variety of generated training data has a higher positive correlation with segmentation model performance than improving the visual fidelity of individual generated images.

### 🤖 AI 总结

**一句话总结**：Synthetic histopathology image generation has emerged as an approach that may address data scarcity in computational pathology, yet current evaluation methodologies may not fully assess synthetic data...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Diffusion, Assessment, Conditional, Model, Synthetic, Histopathology, Image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03990v1) | [下载PDF](https://arxiv.org/pdf/2608.03990v1.pdf)

---

## [26. A Physics-Flavored Transformer Network for Parametrizing Contraction Dynamics of Engineered Skeletal Muscle Tissues](https://arxiv.org/abs/2608.03927v1)

**作者**：Mattias Luber, Timo Betz  
**分类**：cs.LG  
**发布时间**：2026-08-04

### 📄 论文摘要

Engineered Skeletal Muscle Tissues (ESMs) have become a key structure for biomedical disease modeling and pharmacological screening, yet their functional characterization often relies on simplistic metrics like peak force, discarding critical kinetic information. This is partially due to the high level of mathematical complexity which mechanistic models introduce to capture these dynamics. Hence, exactly the complexity prevents scalable application and widespread adaptation in the field. Here we present a Physics-Flavored Neural Network (PFNN) that automates the kinetic phenotyping of ESMs. Our architecture integrates a stretched-exponential physical model into a CNN-Transformer, enabling the extraction of physically meaningful parameters directly from force-time profiles. To address the scarcity of labeled biological data, we employ a hybrid training paradigm: the model develops a "physical intuition" on synthetic data before undergoing unsupervised self-alignment on unlabeled real-world measurements. Our results demonstrate that this physics-flavored approach achieves high-fidelity parameterization across diverse contractile phenotypes and cell lines, including Duchenne Muscular Dystrophy models. Our scalable, self-improving pipeline bridges the gap between idealized biophysics and noisy \emph{in vitro} data, providing a robust tool for high-throughput biophysical research.

### 🤖 AI 总结

**一句话总结**：Engineered Skeletal Muscle Tissues (ESMs) have become a key structure for biomedical disease modeling and pharmacological screening, yet their functional characterization often relies on simplistic me...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Physics-Flavored, Transformer, Network, Parametrizing, Contraction, Dynamics, Engineered

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03927v1) | [下载PDF](https://arxiv.org/pdf/2608.03927v1.pdf)

---

## [27. PRISM: Powerful Time Series to Image (TS2I) Representations for Multivariate Anomaly Detection](https://arxiv.org/abs/2608.03926v1)

**作者**：Mateusz Smendowski, Kamil Faber, Piotr Nawrocki 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-08-04

### 📄 论文摘要

Time series anomaly detection (TSAD) underpins applications in predictive maintenance, finance, and cloud computing, however performance remains sensitive to representation choices, especially in multivariate settings. While transforming time series into images has shown success in forecasting and classification, it remains unclear how multivariate, high-dimensional series should be mapped to multi-channel images and whether vision backbones can match time-domain baselines in TSAD. We introduce PRISM, a plug-and-play meta-workflow enabling systematic construction and evaluation of image-based representations for multivariate TSAD. Our evaluation spanning over 7,000 experiments shows that well-designed PRISM configurations are competitive with 24 time-domain baselines, achieving the best VUS-PR on 10 of 14 datasets, with an average improvement of 41% over the best competing method on those datasets. Further, we identify channelization - how the channel dimension of multi-channel images is constructed - as a critical and previously understudied design dimension, and introduce MSM, a novel statistics-based scheme achieving 11-27% gains over PCA-based alternatives. Finally, ImageNet-pretrained encoders transfer effectively to TSAD, with frozen encoders retaining 92% of fine-tuned performance while training 1.8 times faster. Our code is available at: https://github.com/Smendowski/PRISM.

### 🤖 AI 总结

**一句话总结**：Time series anomaly detection (TSAD) underpins applications in predictive maintenance, finance, and cloud computing, however performance remains sensitive to representation choices, especially in mult...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PRISM, Powerful, Time, Series, Image, TS2I, Representations, Multivariate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03926v1) | [下载PDF](https://arxiv.org/pdf/2608.03926v1.pdf)

---

## [28. Trajectory inference via Acceleration Matching](https://arxiv.org/abs/2608.03916v1)

**作者**：Bartolo Dazzini, Giovanni Conforti, Alain Durmus 等 4 位作者  
**分类**：cs.LG, math.OC, stat.ML  
**发布时间**：2026-08-04

### 📄 论文摘要

Trajectory inference is a fundamental problem in many scientific domains: given a collection of unpaired snapshots of observations at discrete time points, the goal is to generate smooth trajectories that best resemble and interpolate the data. Existing algorithms exhibit computational challenges: they either rely on preprocessing subroutines to enforce smoothness or on simulation-based training objectives, both of which can be expensive. In order to overcome these limitations, we propose a new algorithm called Acceleration Matching (\texttt{AM}). Our approach consists of lifting the original interpolation problem to phase space and then regressing onto an explicit conditional acceleration field that induces random, smooth trajectories that agree with the prescribed marginals. Importantly, our resulting training algorithm only requires positional data, avoids trajectory simulation during training, and is devoid of expensive preprocessing. We provide ample numerical evidence suggesting that \texttt{AM} is competitive with or superior to existing algorithms on several benchmark problems from the existing literature.

### 🤖 AI 总结

**一句话总结**：Trajectory inference is a fundamental problem in many scientific domains: given a collection of unpaired snapshots of observations at discrete time points, the goal is to generate smooth trajectories ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Trajectory, inference, via, Acceleration, Matching, fundamental, problem, many

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03916v1) | [下载PDF](https://arxiv.org/pdf/2608.03916v1.pdf)

---

## [29. Sparse Weight Decomposition for Efficient Circuit Extraction](https://arxiv.org/abs/2608.03913v1)

**作者**：Chuanhao Yan, Xuhan Huang, Yawen Duan 等 7 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-08-04

### 📄 论文摘要

Dense pretrained transformers do not naturally expose interpretable units for circuit extraction. Existing approaches obtain such units by learning auxiliary sparse representations or training sparse models, incurring substantial additional computation while potentially introducing a fidelity gap between the representation being analyzed and the original pretrained model. We propose Sparse Weight Decomposition (SWD), which reparameterizes pretrained linear projections by factorizing each weight matrix into two sparse factors whose shared intermediate coordinates serve as individually addressable circuit units. Without training a separate replacement network, this parametric representation supports the same scoring, selection, and ablation circuit extraction workflow used for methods that learn sparse features. Across single-matrix replacements, SWD matches the held-out fidelity achieved by Transcoder and other strong baselines while using less than 1% of the data that those baselines use to train their replacements. For matched replacement fidelity, SWD reaches the same circuit sufficiency and necessity targets with fewer active read/write edges and selected units across tasks on GPT-2, Qwen2.5, and Qwen3.5-27B. We further show that SWD remains effective for full-model replacement of all attention and MLP weight matrices after fine-tuning the nonzero factor values. Finally, SWD also features a zero-data variant, allowing broader use of mechanistic interpretability analysis (e.g., per-step analysis).

### 🤖 AI 总结

**一句话总结**：Dense pretrained transformers do not naturally expose interpretable units for circuit extraction. Existing approaches obtain such units by learning auxiliary sparse representations or training sparse ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sparse, Weight, Decomposition, Efficient, Circuit, Extraction, Dense, pretrained

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03913v1) | [下载PDF](https://arxiv.org/pdf/2608.03913v1.pdf)

---

## [30. Omega-S: A Functional Resilience Index for LLM Fine-Tuning](https://arxiv.org/abs/2608.03887v1)

**作者**：Alberto Acedo  
**分类**：cs.LG, cs.NE, q-bio.MN  
**发布时间**：2026-08-04

### 📄 论文摘要

Fine-tuning a large language model on new data degrades what it previously learned. We present Omega-S, a drop-in penalty computed from the weight matrix alone: it needs no previous-task data, no Fisher matrix and no stored copy of the old weights. It is three lines in an existing training loop and adds under 4% to the cost of a step.   Retention. On Llama-3-8B with LoRA, fine-tuned from code to prose and measured by HumanEval over ten seeds, Omega-S retains more of the original capability than no regularisation on 9 of 10 seeds (0.173 -> 0.238 absolute pass@1; sign test one-sided p=0.011, Wilcoxon p=0.006), as a retention ratio, 62.9% -> 84.1%. It also beats tuned weight decay on 10 of 10 seeds (p=0.002) and tuned EWC on 8 of 10 (p=0.014), every arm re-measured in the same session.   Mechanism, measured rather than asserted. Omega-S is topological by construction, its objective built from Tr(A^3), but we measured which of its four factors actually moves and three do not: their elasticity with respect to the weights is at or below 1e-4, against 9e-3 for the degree-variance term. As implemented, the composite reduces to a penalty on the variance of node degrees, which means row magnitude in square modules and directional alignment in non-square ones. We report this because a method whose name promises one thing and whose gradient does another should say so. We also enumerate the open design choices, including a contrast-preserving construction that does what it was designed to do and makes retention worse on all ten seeds.   Repeating an identical configuration, same seed and same hardware, gives a standard deviation of 0.104 in retention ratio. We have not found this quantified for low-rank fine-tuning of language models, and it bounds every seed-paired comparison in this literature, ours included.   Code, per-seed results and the full record of negative results are available.

### 🤖 AI 总结

**一句话总结**：Fine-tuning a large language model on new data degrades what it previously learned. We present Omega-S, a drop-in penalty computed from the weight matrix alone: it needs no previous-task data, no Fish...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Omega-S, Functional, Resilience, Index, Fine-Tuning, large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.03887v1) | [下载PDF](https://arxiv.org/pdf/2608.03887v1.pdf)

---

