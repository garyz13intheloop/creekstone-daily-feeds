# arXiv AI 论文日报 | 2026-04-29

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (11 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.CV](#csCV) (7 篇)
- [cs.AI](#csAI) (4 篇)

---

## cs.AI

## [1. ADEMA: A Knowledge-State Orchestration Architecture for Long-Horizon Knowledge Synthesis with LLMAgents](https://arxiv.org/abs/2604.25849v1)

**作者**：Zhou Hanlin, Chan Huah Yong  
**分类**：cs.AI  
**发布时间**：2026-04-28

### 📄 论文摘要

Long-horizon LLM tasks often fail not because a single answer is unattainable, but because knowledge states drift across rounds, intermediate commitments remain implicit, and interruption fractures the evolving evidence chain. This paper presents ADEMA as a knowledge-state orchestration architecture for long-horizon knowledge synthesis rather than as a generic multi-agent runtime. The architecture combines explicit epistemic bookkeeping, heterogeneous dual-evaluator governance, adaptive task-mode switching, reputation-shaped resource allocation, checkpoint-resumable persistence, segment-level memory condensation, artifact-first assembly, and final-validity checking with safe fallback. Evidence is drawn entirely from existing materials: a four-scenario showcase package, a fixed 60-run mechanism matrix, targeted micro-ablation and artifact-chain supplements, and a repaired protocol-level benchmark in which code-oriented evaluation is the clearest quality-sensitive mechanism block. Across the fixed matrix, removing checkpoint/resume produced the only invalid run, and it did so in the interruption-sensitive resume condition. By contrast, dual evaluation, segment synthesis, and dynamic governance are best interpreted as supporting control mechanisms that shape trajectory discipline, explicit artifact progression, and cost-quality behavior rather than as universal binary prerequisites for completion. The contribution is therefore a knowledge-state orchestration architecture in which explicit epistemic state transition, evidence-bearing artifact progression, and recoverable continuity are the primary design commitments.

### 🤖 AI 总结

**一句话总结**：Long-horizon LLM tasks often fail not because a single answer is unattainable, but because knowledge states drift across rounds, intermediate commitments remain implicit, and interruption fractures th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ADEMA, Knowledge-State, Orchestration, Architecture, Long-Horizon, Knowledge, Synthesis, LLMAgents

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25849v1) | [下载PDF](https://arxiv.org/pdf/2604.25849v1.pdf)

---

## [2. Semi-Markov Reinforcement Learning for City-Scale EV Ride-Hailing with Feasibility-Guaranteed Actions](https://arxiv.org/abs/2604.25848v1)

**作者**：An Nguyen, Hoang Nguyen, Phuong Le 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-28

### 📄 论文摘要

We study city-scale control of electric-vehicle (EV) ride-hailing fleets where dispatch, repositioning, and charging decisions must respect charger and feeder limits under uncertain, spatially correlated demand and travel times. We formulate the problem as a hex-grid semi-Markov decision process (semi-MDP) with mixed actions -- discrete actions for serving, repositioning, and charging, together with continuous charging power -- and variable action durations. To guarantee physical feasibility during both training and deployment, the policy learns over high-level intentions produced by a masked, temperature-annealed actor. These intentions are projected at every decision step through a time-limited rolling mixed-integer linear program (MILP) that strictly enforces state-of-charge, port, and feeder constraints. To mitigate distributional shifts, we optimize a Soft Actor--Critic (SAC) agent against a Wasserstein-1 ambiguity set with a graph-aligned Mahalanobis ground metric that captures spatial correlations. The robust backup uses the Kantorovich--Rubinstein dual, a projected subgradient inner loop, and a primal--dual risk-budget update. Our architecture combines a two-layer Graph Convolutional Network (GCN) encoder, twin critics, and a value network that drives the adversary. Experiments on a large-scale EV fleet simulator built from NYC taxi data show that PD--RSAC achieves the highest net profit, reaching \$1.22M, compared with \$0.58M--\$0.70M for strong heuristic, single-agent RL, and multi-agent RL baselines, including Greedy, SAC, MAPPO, and MADDPG, while maintaining zero feeder-limit violations.

### 🤖 AI 总结

**一句话总结**：We study city-scale control of electric-vehicle (EV) ride-hailing fleets where dispatch, repositioning, and charging decisions must respect charger and feeder limits under uncertain, spatially correla...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EV, Semi-Markov, Reinforcement, Learning, City-Scale, Ride-Hailing, Feasibility-Guaranteed, Actions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25848v1) | [下载PDF](https://arxiv.org/pdf/2604.25848v1.pdf)

---

## [3. Action-Aware Generative Sequence Modeling for Short Video Recommendation](https://arxiv.org/abs/2604.25834v1)

**作者**：Wenhao Li, Zihan Lin, Zhengxiao Guo 等 10 位作者  
**分类**：cs.AI, cs.IR  
**发布时间**：2026-04-28

### 📄 论文摘要

With the rapid development of the Internet, users have increasingly higher expectations for the recommendation accuracy of online content consumption platforms. However, short videos often contain diverse segments, and users may not hold the same attitude toward all of them. Traditional binary-classification recommendation models, which treat a video as a single holistic entity, face limitations in accurately capturing such nuanced preferences. Considering that user consumption is a temporal process, this paper demonstrates that the timing of user actions can represent diverse intentions through statistical analysis and examination of action patterns. Based on this insight, we propose a novel modeling paradigm: Action-Aware Generative Sequence Network (A2Gen), which refines user actions along the temporal dimension and chains them into sequences for unified processing and prediction. First, we introduce the Context-aware Attention Module (CAM) to model action sequences enriched with item-specific contextual features. Building upon this, we develop the Hierarchical Sequence Encoder (HSE) to learn temporal action patterns from users' historical actions. Finally, through leveraging CAM, we design a module for action sequence generation: the Action-seq Autoregressive Generator (AAG). Extensive offline experiments on the Kuaishou's dataset and the Tmall public dataset demonstrate the superiority of our proposed model. Furthermore, through large-scale online A/B testing deployed on Kuaishou's platform, our model achieves significant improvements over baseline methods in multi-task prediction by leveraging sequential information. Specifically, it yields increases of 0.34% in user watch time, 8.1% in interaction rate, and 0.162% in overall user retention (LifeTime-7), leading to successful deployment across all traffic, serving over 400 million users every day.

### 🤖 AI 总结

**一句话总结**：With the rapid development of the Internet, users have increasingly higher expectations for the recommendation accuracy of online content consumption platforms. However, short videos often contain div...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Action-Aware, Generative, Sequence, Modeling, Short, Video, Recommendation, rapid

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25834v1) | [下载PDF](https://arxiv.org/pdf/2604.25834v1.pdf)

---

## [4. TrialCalibre: A Fully Automated Causal Engine for RCT Benchmarking and Observational Trial Calibration](https://arxiv.org/abs/2604.25832v1)

**作者**：Amir Habibdoust, Xing Song  
**分类**：cs.AI  
**发布时间**：2026-04-28

### 📄 论文摘要

Real-world evidence (RWE) studies that emulate target trials increasingly inform regulatory and clinical decisions, yet residual, hard-to-quantify biases still limit their credibility. The recently proposed BenchExCal framework addresses this challenge via a two-stage Benchmark, Expand, Calibrate process, which first compares an observational emulation against an existing randomized controlled trial (RCT), then uses observed divergence to calibrate a second emulation for a new indication causal effect estimation. While methodologically powerful, BenchExCal is resource intensive and difficult to scale. We introduce TrialCalibre, a conceptualized multiagent system designed to automate and scale the BenchExCal workflow. Our framework features specialized agents such as the Orchestrator, Protocol Design, Data Synthesis, Clinical Validation, and Quantitative Calibration Agents that coordi-nate the the overall process. TrialCalibre incorpo-rates agent learning (e.g., RLHF) and knowledge blackboards to support adaptive, auditable, and transparent causal effect estimation.

### 🤖 AI 总结

**一句话总结**：Real-world evidence (RWE) studies that emulate target trials increasingly inform regulatory and clinical decisions, yet residual, hard-to-quantify biases still limit their credibility. The recently pr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TrialCalibre, Fully, Automated, Causal, Engine, RCT, Benchmarking, Observational

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25832v1) | [下载PDF](https://arxiv.org/pdf/2604.25832v1.pdf)

---

## cs.CL

## [5. DV-World: Benchmarking Data Visualization Agents in Real-World Scenarios](https://arxiv.org/abs/2604.25914v1)

**作者**：Jinxiang Meng, Shaoping Huang, Fangyu Lei 等 20 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-28

### 📄 论文摘要

Real-world data visualization (DV) requires native environmental grounding, cross-platform evolution, and proactive intent alignment. Yet, existing benchmarks often suffer from code-sandbox confinement, single-language creation-only tasks, and assumption of perfect intent. To bridge these gaps, we introduce DV-World, a benchmark of 260 tasks designed to evaluate DV agents across real-world professional lifecycles. DV-World spans three domains: DV-Sheet for native spreadsheet manipulation including chart and dashboard creation as well as diagnostic repair; DV-Evolution for adapting and restructuring reference visual artifacts to fit new data across diverse programming paradigms and DV-Interact for proactive intent alignment with a user simulator that mimics real-world ambiguous requirements. Our hybrid evaluation framework integrates Table-value Alignment for numerical precision and MLLM-as-a-Judge with rubrics for semantic-visual assessment. Experiments reveal that state-of-the-art models achieve less than 50% overall performance, exposing critical deficits in handling the complex challenges of real-world data visualization. DV-World provides a realistic testbed to steer development toward the versatile expertise required in enterprise workflows. Our data and code are available at \href{https://github.com/DA-Open/DV-World}{this project page}.

### 🤖 AI 总结

**一句话总结**：Real-world data visualization (DV) requires native environmental grounding, cross-platform evolution, and proactive intent alignment. Yet, existing benchmarks often suffer from code-sandbox confinemen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, DV, DV-World, Benchmarking, Data, Visualization, Real-World, Scenarios

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25914v1) | [下载PDF](https://arxiv.org/pdf/2604.25914v1.pdf)

---

## [6. A paradox of AI fluency](https://arxiv.org/abs/2604.25905v1)

**作者**：Christopher Potts, Moritz Sudhof  
**分类**：cs.CL  
**发布时间**：2026-04-28

### 📄 论文摘要

How much does a user's skill with AI shape what AI actually delivers for them? This question is critical for users, AI product builders, and society at large, but it remains underexplored. Using a richly annotated sample of 27K transcripts from WildChat-4.8M, we show that fluent users take on more complex tasks than novices and adopt a fundamentally different interactional mode: they iterate collaboratively with the AI, refining goals and critically assessing outputs, whereas novices take a passive stance. These differences lead to a paradox of AI fluency: fluent users experience more failures than novices -- but their failures tend to be visible (a direct consequence of their engagement), they are more likely to lead to partial recovery, and they occur alongside greater success on complex tasks. Novices, by contrast, more often experience invisible failures: conversations that appear to end successfully but in fact miss the mark. Taken together, these results reframe what success with AI depends on. Individuals should adopt a stance of active engagement rather than passive acceptance. AI product builders should recognize that they are designing not just model behavior but user behavior; encouraging deep engagement, rather than friction-free experiences, will lead to more success overall. Our code and data are available at https://github.com/bigspinai/bigspin-fluency-outcomes

### 🤖 AI 总结

**一句话总结**：How much does a user's skill with AI shape what AI actually delivers for them? This question is critical for users, AI product builders, and society at large, but it remains underexplored. Using a ric...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, paradox, fluency, How, much, does, user's, skill

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25905v1) | [下载PDF](https://arxiv.org/pdf/2604.25905v1.pdf)

---

## [7. Toward a Functional Geometric Algebra for Natural Language Semantics](https://arxiv.org/abs/2604.25902v1)

**作者**：James Pustejovsky  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-04-28

### 📄 论文摘要

Distributional and neural approaches to natural language semantics have been built almost exclusively on conventional linear algebra: vectors, matrices, tensors, and the operations that accompany them. These methods have achieved remarkable empirical success, yet they face persistent structural limitations in compositional semantics, type sensitivity, and interpretability. I argue in this paper that geometric algebra (GA) -- specifically, Clifford algebras -- provides a mathematically superior foundation for semantic representation, and that a Functional Geometric Algebra (FGA) framework extends GA toward a typed, compositional semantics capable of supporting inference, transformation, and interpretability while retaining full compatibility with distributional learning and modern neural architectures. I develop the formal foundations, identify three core capabilities that GA provides and linear algebra does not, present a detailed worked example illustrating operator-level semantic contrasts, and show how GA-based operations already implicit in current transformer architectures can be made explicit and extended. The central claim is not merely increased dimensionality but increased structural organization: GA expands an $n$-dimensional embedding space into a $2^n$ multivector algebra where base semantic concepts and their higher-order interactions are represented within a single, principled algebraic framework.

### 🤖 AI 总结

**一句话总结**：Distributional and neural approaches to natural language semantics have been built almost exclusively on conventional linear algebra: vectors, matrices, tensors, and the operations that accompany them...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Toward, Functional, Geometric, Algebra, Natural, Language, Semantics, Distributional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25902v1) | [下载PDF](https://arxiv.org/pdf/2604.25902v1.pdf)

---

## [8. From Syntax to Emotion: A Mechanistic Analysis of Emotion Inference in LLMs](https://arxiv.org/abs/2604.25866v1)

**作者**：Bangzhao Shu, Arinjay Singh, Mai ElSherief  
**分类**：cs.CL  
**发布时间**：2026-04-28

### 📄 论文摘要

Large language models (LLMs) are increasingly used in emotionally sensitive human-AI applications, yet little is known about how emotion recognition is internally represented. In this work, we investigate the internal mechanisms of emotion recognition in LLMs using sparse autoencoders (SAEs). By analyzing sparse feature activations across layers, we identify a consistent three-phase information flow, in which emotion-related features emerge only in the final phase. We further show that emotion representations comprise both shared features across emotions and emotion-specific features. Using phase-stratified causal tracing, we identify a small set of features that strongly influence emotion predictions, and show that both their number and causal impact vary across emotions; in particular, Disgust is more weakly and diffusely represented than other emotions. Finally, we propose an interpretable and data-efficient causal feature steering method that significantly improves emotion recognition performance across multiple models while largely preserving language modeling ability, and demonstrate that these improvements generalize across multiple emotion recognition datasets. Overall, our findings provide a systematic analysis of the internal mechanisms underlying emotion recognition in LLMs and introduce an efficient, interpretable, and controllable approach for improving model performance.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly used in emotionally sensitive human-AI applications, yet little is known about how emotion recognition is internally represented. In this work, we investi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Syntax, Emotion, Mechanistic, Analysis, Inference, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25866v1) | [下载PDF](https://arxiv.org/pdf/2604.25866v1.pdf)

---

## [9. Luminol-AIDetect: Fast Zero-shot Machine-Generated Text Detection based on Perplexity under Text Shuffling](https://arxiv.org/abs/2604.25860v1)

**作者**：Lucio La Cava, Andrea Tagarelli  
**分类**：cs.CL, cs.AI, cs.CY  
**发布时间**：2026-04-28

### 📄 论文摘要

Machine-generated text (MGT) detection requires identifying structurally invariant signals across generation models, rather than relying on model-specific fingerprints. In this respect, we hypothesize that while large language models excel at local semantic consistency, their autoregressive nature results in a specific kind of structural fragility compared to human writing. We propose Luminol-AIDetect, a novel, zero-shot statistical approach that exposes this fragility through coherence disruption. By applying a simple randomized text-shuffling procedure, we demonstrate that the resulting shift in perplexity serves as a principled, model-agnostic discriminant, as MGT displays a characteristic dispersion in perplexity-under-shuffling that differs markedly from the more stable structural variability of human-written text. Luminol-AIDetect leverages this distinction to inform its decision process, where a handful of perplexity-based scalar features are extracted from an input text and its shuffled version, then detection is performed via density estimation and ensemble-based prediction. Evaluated across 8 content domains, 11 adversarial attack types, and 18 languages, Luminol-AIDetect demonstrates state-of-the-art performance, with gains up to 17x lower FPR while being cheaper than prior methods.

### 🤖 AI 总结

**一句话总结**：Machine-generated text (MGT) detection requires identifying structurally invariant signals across generation models, rather than relying on model-specific fingerprints. In this respect, we hypothesize...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Luminol-AIDetect, Fast, Zero-shot, Machine-Generated, Text, Detection, Perplexity, under

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25860v1) | [下载PDF](https://arxiv.org/pdf/2604.25860v1.pdf)

---

## [10. G-Loss: Graph-Guided Fine-Tuning of Language Models](https://arxiv.org/abs/2604.25853v1)

**作者**：Sharma Aditya, Agarwal Vinti, Kumar Rajesh  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-04-28

### 📄 论文摘要

Traditional loss functions, including cross-entropy, contrastive, triplet, and su pervised contrastive losses, used for fine-tuning pre-trained language models such as BERT, operate only within local neighborhoods and fail to account for the global semantic structure. We present G-Loss, a graph-guided loss function that incorporates semi-supervised label propagation to use structural relationships within the embedding manifold. G-Loss builds a document-similarity graph that captures global semantic relationships, thereby guiding the model to learn more discriminative and robust embeddings. We evaluate G-Loss on five benchmark datasets covering key downstream classification tasks: MR (sentiment analysis), R8 and R52 (topic categorization), Ohsumed (medical document classification), and 20NG (news categorization). In the majority of experimental setups, G-Loss converges faster and produces semantically coherent embedding spaces, resulting in higher classification accuracy than models fine-tuned with traditional loss functions.

### 🤖 AI 总结

**一句话总结**：Traditional loss functions, including cross-entropy, contrastive, triplet, and su pervised contrastive losses, used for fine-tuning pre-trained language models such as BERT, operate only within local ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, G-Loss, Graph-Guided, Fine-Tuning, Language, Models, Traditional, loss

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25853v1) | [下载PDF](https://arxiv.org/pdf/2604.25853v1.pdf)

---

## [11. PSI-Bench: Towards Clinically Grounded and Interpretable Evaluation of Depression Patient Simulators](https://arxiv.org/abs/2604.25840v1)

**作者**：Nguyen Khoi Hoang, Shuhaib Mehri, Tse-An Hsu 等 7 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-28

### 📄 论文摘要

Patient simulators are gaining traction in mental health training by providing scalable exposure to complex and sensitive patient interactions. Simulating depressed patients is particularly challenging, as safety constraints and high patient variability complicate simulations and underscore the need for simulators that capture diverse and realistic patient behaviors. However, existing evaluations heavily rely on LLM-judges with poorly specified prompts and do not assess behavioral diversity. We introduce PSI-Bench, an automatic evaluation framework that provides interpretable, clinically grounded diagnostics of depression patient simulator behavior across turn-, dialogue-, and population-level dimensions. Using PSI-Bench, we benchmark seven LLMs across two simulator frameworks and find that simulators produce overly long, lexically diverse responses, show reduced variability, resolve emotions too quickly, and follow a uniform negative-to-positive trajectory. We also show that the simulation framework has a larger impact on fidelity than the model scale. Results from a human study demonstrate that our benchmark is strongly aligned with expert judgments. Our work reveals key limitations of current depression patient simulators and provides an interpretable, extensible benchmark to guide future simulator design and evaluation.

### 🤖 AI 总结

**一句话总结**：Patient simulators are gaining traction in mental health training by providing scalable exposure to complex and sensitive patient interactions. Simulating depressed patients is particularly challengin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, PSI-Bench, Towards, Clinically, Grounded, Interpretable, Evaluation, Depression

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25840v1) | [下载PDF](https://arxiv.org/pdf/2604.25840v1.pdf)

---

## [12. MAIC-UI: Making Interactive Courseware with Generative UI](https://arxiv.org/abs/2604.25806v1)

**作者**：Shangqing Tu, Yanjia Li, Keyu Chen 等 10 位作者  
**分类**：cs.CL, cs.AI, cs.HC  
**发布时间**：2026-04-28

### 📄 论文摘要

Creating interactive STEM courseware traditionally requires HTML/CSS/JavaScript expertise, leaving barriers for educators. While generative AI can produce HTML codes, existing tools generate static presentations rather than interactive simulations, struggle with long documents, and lack pedagogical accuracy mechanisms. Furthermore, full regeneration for modifications requires 200--600 seconds, disrupting creative flow. We present MAIC-UI, a zero-code authoring system that enables educators to create and rapidly edit interactive courseware from textbooks, PPTs, and PDFs. MAIC-UI employs: (1) structured knowledge analysis with multi-modal understanding to ensure pedagogical rigor; (2) a two-stage generate-verify-optimize pipeline separating content alignment from visual refinement; and (3) Click-to-Locate editing with Unified Diff-based incremental generation achieving sub-10-second iteration cycles. A controlled lab study with 40 participants shows MAIC-UI reduces editing iterations (4.9 vs. 7.0) and significantly improves learnability and controllability compared to direct Text-to-HTML generation. A three-month classroom deployment with 53 high school students demonstrates that MAIC-UI fosters learning agency and reduces outcome disparities -- the pilot class achieved 9.21-point gains in STEM subjects compared to -2.32 points in control classes. Our code is available at https://github.com/THU-MAIC/MAIC-UI.

### 🤖 AI 总结

**一句话总结**：Creating interactive STEM courseware traditionally requires HTML/CSS/JavaScript expertise, leaving barriers for educators. While generative AI can produce HTML codes, existing tools generate static pr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UI, MAIC-UI, Making, Interactive, Courseware, Generative, Creating, STEM

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25806v1) | [下载PDF](https://arxiv.org/pdf/2604.25806v1.pdf)

---

## [13. Subliminal Steering: Stronger Encoding of Hidden Signals](https://arxiv.org/abs/2604.25783v1)

**作者**：George Morgulis, John Hewitt  
**分类**：cs.CL  
**发布时间**：2026-04-28

### 📄 论文摘要

Subliminal learning describes a student language model inheriting a behavioral bias by fine-tuning on seemingly innocuous data generated by a biased teacher model. Prior work has begun to characterize this phenomenon but leaves open questions about the scope of signals it can transfer, the mechanisms that explain it, and the precision with which a bias can be encoded by seemingly unrelated data. We tackle all three problems by introducing subliminal steering, a variant of subliminal learning in which the teacher's bias is implemented not via a system prompt, as in prior work, but through a steering vector trained to maximize the likelihood of a set of target samples. First, we show that subliminal steering transfers complex multi-word biases, whereas prior work focused on single-word preferences, demonstrating a large scope of subliminally transferrable signals. Second, we provide mechanistic evidence that subliminal learning transfers not only the target behavioral bias, but also the steering vector itself, localized to the layers at which the teacher was steered. Finally, we show that the bias is encoded with surprising precision. We train a new steering vector directly on the subliminally-laden dataset and find that it attains high cosine similarity with the original vector.

### 🤖 AI 总结

**一句话总结**：Subliminal learning describes a student language model inheriting a behavioral bias by fine-tuning on seemingly innocuous data generated by a biased teacher model. Prior work has begun to characterize...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Subliminal, Steering, Stronger, Encoding, Hidden, Signals, learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25783v1) | [下载PDF](https://arxiv.org/pdf/2604.25783v1.pdf)

---

## [14. Unrequited Emotions: Investigating the Gaps in Motivation and Practice in Speech Emotion Recognition Research](https://arxiv.org/abs/2604.25776v1)

**作者**：Taryn Wong, Zeerak Talat, Hanan Aldarmaki 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-28

### 📄 论文摘要

Critical analyses of emotion recognition technology have raised ethical concerns around task validity and potential downstream impacts, urging researchers to ensure alignment between their stated motivations and practice. However, these discussions have not adequately influenced or drawn from research on speech emotion recognition (SER). We address this gap by conducting a systematic survey of SER research to uncover what stated motivations drive this work and if they align with the datasets and emotions studied. We find that while SER research identifies appealing goals, such as well-situated voice-activated systems or healthcare applications, commonly-used datasets do not reflect these proposed deployment contexts, thus presenting a gap between motivations and research practices. We argue that such gaps engender ethical concerns, and that SER research should reassert itself with concrete use-cases to prevent misinterpretations, misuse, and downstream harms.

### 🤖 AI 总结

**一句话总结**：Critical analyses of emotion recognition technology have raised ethical concerns around task validity and potential downstream impacts, urging researchers to ensure alignment between their stated moti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unrequited, Emotions, Investigating, Gaps, Motivation, Practice, Speech, Emotion

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25776v1) | [下载PDF](https://arxiv.org/pdf/2604.25776v1.pdf)

---

## [15. CGU-ILALab at FoodBench-QA 2026: Comparing Traditional and LLM-based Approaches for Recipe Nutrient Estimation](https://arxiv.org/abs/2604.25774v1)

**作者**：Wei-Chun Chen, Yu-Xuan Chen, I-Fang Chung 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-28

### 📄 论文摘要

Accurate nutrient estimation from unstructured recipe text is an important yet challenging problem in dietary monitoring, due to ambiguous ingredient terminology and highly variable quantity expressions. We systematically evaluate models spanning a wide range of representational capacity, from lexical matching methods (TF-IDF with Ridge Regression), to deep semantic encoders (DeBERTa-v3), to generative reasoning with large language models (LLMs). Under the strict tolerance criteria defined by EU Regulation 1169/2011, our empirical results reveal a clear trade-off between predictive accuracy and computational efficiency. The TF-IDF baseline achieves moderate nutrient estimation performance with near-instantaneous inference, whereas the DeBERTa-v3 encoder performs poorly under task-specific data scarcity. In contrast, few-shot LLM inference (e.g., Gemini 2.5 Flash) and a hybrid LLM refinement pipeline (TF-IDF combined with Gemini 2.5 Flash) deliver the highest validation accuracy across all nutrient categories. These improvements likely arise from the ability of LLMs to leverage pre-trained world knowledge to resolve ambiguous terminology and normalize non-standard units, which remain difficult for purely lexical approaches. However, these gains come at the cost of substantially higher inference latency, highlighting a practical deployment trade-off between real-time efficiency and nutritional precision in dietary monitoring systems.

### 🤖 AI 总结

**一句话总结**：Accurate nutrient estimation from unstructured recipe text is an important yet challenging problem in dietary monitoring, due to ambiguous ingredient terminology and highly variable quantity expressio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, CGU-ILALab, FoodBench-QA, Comparing, Traditional, LLM-based, Approaches, Recipe

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25774v1) | [下载PDF](https://arxiv.org/pdf/2604.25774v1.pdf)

---

## cs.CV

## [16. Robust Deepfake Detection: Mitigating Spatial Attention Drift via Calibrated Complementary Ensembles](https://arxiv.org/abs/2604.25889v1)

**作者**：Minh-Khoa Le-Phan, Minh-Hoang Le, Trong-Le Do 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-28

### 📄 论文摘要

Current deepfake detection models achieve state-of-the-art performance on pristine academic datasets but suffer severe spatial attention drift under real-world compound degradations, such as blurring and severe lossy compression. To address this vulnerability, we propose a foundation-driven forensic framework that integrates an extreme compound degradation engine with a structurally constrained, multi-stream architecture. During training, our degradation pipeline systematically destroys high-frequency artifacts, optimizing the DINOv2-Giant backbone to extract invariant geometric and semantic priors. We then process images through three specialized pathways: a Global Texture stream, a Localized Facial stream, and a Hybrid Semantic Fusion stream incorporating CLIP. Through analyzing spatial attribution via Score-CAM and feature stability using Cosine Similarity, we quantitatively demonstrate that these streams extract non-redundant, complementary feature representations and stabilize attention entropy. By aggregating these predictions via a calibrated, discretized voting mechanism, our ensemble successfully suppresses background attention drift while acting as a robust geometric anchor. Our approach yields highly stable zero-shot generalization, achieving Fourth Place in the NTIRE 2026 Robust Deepfake Detection Challenge at CVPR. Code is available at https://github.com/khoalephanminh/ntire26-deepfake-challenge.

### 🤖 AI 总结

**一句话总结**：Current deepfake detection models achieve state-of-the-art performance on pristine academic datasets but suffer severe spatial attention drift under real-world compound degradations, such as blurring ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Robust, Deepfake, Detection, Mitigating, Spatial, Attention, Drift, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25889v1) | [下载PDF](https://arxiv.org/pdf/2604.25889v1.pdf)

---

## [17. No Pedestrian Left Behind: Real-Time Detection and Tracking of Vulnerable Road Users for Adaptive Traffic Signal Control](https://arxiv.org/abs/2604.25887v1)

**作者**：Anas Gamal Aly, Hala ElAarag  
**分类**：cs.CV, cs.AI, cs.RO, eess.SY  
**发布时间**：2026-04-28

### 📄 论文摘要

Current pedestrian crossing signals operate on fixed timing without adjustment to pedestrian behavior, which can leave vulnerable road users (VRUs) such as the elderly, disabled, or distracted pedestrians stranded when the light changes. We introduce No Pedestrian Left Behind (NPLB), a real-time adaptive traffic signal system that monitors VRUs in crosswalks and automatically extends signal timing when needed. We evaluated five state-of-the-art object detection models on the BGVP dataset, with YOLOv12 achieving the highest mean Average Precision at 50% (mAP@0.5) of 0.756. NPLB integrates our fine-tuned YOLOv12 with ByteTrack multi-object tracking and an adaptive controller that extends pedestrian phases when remaining time falls below a critical threshold. Through 10,000 Monte Carlo simulations, we demonstrate that NPLB improves VRU safety by 71.4%, reducing stranding rates from 9.10% to 2.60%, while requiring signal extensions in only 12.1% of crossing cycles.

### 🤖 AI 总结

**一句话总结**：Current pedestrian crossing signals operate on fixed timing without adjustment to pedestrian behavior, which can leave vulnerable road users (VRUs) such as the elderly, disabled, or distracted pedestr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：No, of, Pedestrian, Left, Behind, Real-Time, Detection, Tracking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25887v1) | [下载PDF](https://arxiv.org/pdf/2604.25887v1.pdf)

---

## [18. SIEVES: Selective Prediction Generalizes through Visual Evidence Scoring](https://arxiv.org/abs/2604.25855v1)

**作者**：Hector G. Rodriguez, Marcus Rohrbach  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-28

### 📄 论文摘要

Multimodal large language models (MLLMs) achieve ever-stronger performance on visual-language tasks. Even as traditional visual question answering benchmarks approach saturation, reliable deployment requires satisfying low error tolerances in real-world out-of-distribution (OOD) scenarios. Precisely, selective prediction aims to improve coverage, i.e. the share of inputs the system answers, while adhering to a user-defined risk level. This is typically achieved by assigning a confidence score to each answer and abstaining on those that fall below a certain threshold. To enable reliable generalization, we require reasoner models to produce localized visual evidence while answering, and design a selector that explicitly learns to estimate the quality of the localization provided by the reasoner. We show that SIEVES (Selective Prediction through Visual Evidence Scoring) improves coverage by up to three times on challenging OOD benchmarks (V* Bench, HR-Bench-8k, MME-RealWorld-Lite, VizWiz, and AdVQA), compared to non-grounding baselines. Beyond better generalization to OOD tasks, the design of the SIEVES selector enables transfer to proprietary reasoners without access to their weights or logits, such as o3 and Gemini-3-Pro, providing coverage boosts beyond those attributable to accuracy alone. We highlight that SIEVES generalizes across all five tested OOD datasets and reasoner models (Pixel-Reasoner, o3, and Gemini-3-Pro), without benchmark- or reasoner-specific training or adaptation.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) achieve ever-stronger performance on visual-language tasks. Even as traditional visual question answering benchmarks approach saturation, reliable deployment r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SIEVES, Selective, Prediction, Generalizes, through, Visual, Evidence, Scoring

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25855v1) | [下载PDF](https://arxiv.org/pdf/2604.25855v1.pdf)

---

## [19. Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation](https://arxiv.org/abs/2604.25819v1)

**作者**：Yupeng Zhou, Lianghua Huang, Zhifan Wu 等 10 位作者  
**分类**：cs.CV, cs.SD  
**发布时间**：2026-04-28

### 📄 论文摘要

In this work, we propose Mutual Forcing, a framework for fast autoregressive audio-video generation with long-horizon audio-video synchronization. Our approach addresses two key challenges: joint audio-video modeling and fast autoregressive generation. To ease joint audio-video optimization, we adopt a two-stage training strategy: we first train uni-modal generators and then couple them into a unified audio-video model for joint training on paired data. For streaming generation, we ask whether a native fast causal audio-video model can be trained directly, instead of following existing streaming distillation pipelines that typically train a bidirectional model first and then convert it into a causal generator through multiple distillation stages. Our answer is Mutual Forcing, which builds directly on native autoregressive model and integrates few-step and multi-step generation within a single weight-shared model, enabling self-distillation and improved training-inference consistency. The multi-step mode improves the few-step mode via self-distillation, while the few-step mode generates historical context during training to improve training-inference consistency; because the two modes share parameters, these two effects reinforce each other within a single model. Compared with prior approaches such as Self-Forcing, Mutual Forcing removes the need for an additional bidirectional teacher model, supports more flexible training sequence lengths, reduces training overhead, and allows the model to improve directly from real paired data rather than a fixed teacher. Experiments show that Mutual Forcing matches or surpasses strong baselines that require around 50 sampling steps while using only 4 to 8 steps, demonstrating substantial advantages in both efficiency and quality. The project page is available at https://mutualforcing.github.io.

### 🤖 AI 总结

**一句话总结**：In this work, we propose Mutual Forcing, a framework for fast autoregressive audio-video generation with long-horizon audio-video synchronization. Our approach addresses two key challenges: joint audi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mutual, Forcing, Dual-Mode, Self-Evolution, Fast, Autoregressive, Audio-Video, Character

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25819v1) | [下载PDF](https://arxiv.org/pdf/2604.25819v1.pdf)

---

## [20. Magnification-Invariant Image Classification via Domain Generalization and Stable Sparse Embedding Signatures](https://arxiv.org/abs/2604.25817v1)

**作者**：Ifeanyi Ezuma, Olusiji Medaiyese  
**分类**：cs.CV, stat.ML  
**发布时间**：2026-04-28

### 📄 论文摘要

Magnification shift is a major obstacle to robust histopathology classification, because models trained on one imaging scale often generalize poorly to another. Here, we evaluated this problem on the BreaKHis dataset using a strict patient-disjoint leave-one-magnification-out protocol, comparing supervised baseline, baseline augmented with DCGAN-generated patches, and a gradient-reversal domain-general model designed to preserve discriminative information while suppressing magnification-specific variation. Across held-out magnifications, the domain-general model achieved the strongest overall discrimination and its clearest gain was observed when 200X was held out. By contrast, GAN augmentation produced inconsistent effects, improving some folds but degrading others, particularly at 400X. The domain-general model also yielded the lowest Brier score at 0.063 vs 0.089 at baseline. Sparse embedding analysis further revealed that domain-general training reduced average signature size more than three-fold (306 versus 1,074 dimensions) while preserving equivalent predictive performance (AUC: 0.967 vs 0.965; F1: 0.930 vs 0.931). It also increased cross-fold signature reproducibility from near-zero Jaccard overlap in the baseline to 0.99 between the 100X and 200X folds. These findings show that calibrated, compact, and transferable representations can be learned without added architectural complexity, with clear implications for the reliable deployment of computational pathology models across heterogeneous acquisition settings.

### 🤖 AI 总结

**一句话总结**：Magnification shift is a major obstacle to robust histopathology classification, because models trained on one imaging scale often generalize poorly to another. Here, we evaluated this problem on the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Magnification-Invariant, Image, Classification, via, Domain, Generalization, Stable, Sparse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25817v1) | [下载PDF](https://arxiv.org/pdf/2604.25817v1.pdf)

---

## [21. Improving Diversity in Black-box Few-shot Knowledge Distillation](https://arxiv.org/abs/2604.25795v1)

**作者**：Tri-Nhan Vo, Dang Nguyen, Kien Do 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-04-28

### 📄 论文摘要

Knowledge distillation (KD) is a well-known technique to effectively compress a large network (teacher) to a smaller network (student) with little sacrifice in performance. However, most KD methods require a large training set and internal access to the teacher, which are rarely available due to various restrictions. These challenges have originated a more practical setting known as black-box few-shot KD, where the student is trained with few images and a black-box teacher. Recent approaches typically generate additional synthetic images but lack an active strategy to promote their diversity, a crucial factor for student learning. To address these problems, we propose a novel training scheme for generative adversarial networks, where we adaptively select high-confidence images under the teacher's supervision and introduce them to the adversarial learning on-the-fly. Our approach helps expand and improve the diversity of the distillation set, significantly boosting student accuracy. Through extensive experiments, we achieve state-of-the-art results among other few-shot KD methods on seven image datasets. The code is available at https://github.com/votrinhan88/divbfkd.

### 🤖 AI 总结

**一句话总结**：Knowledge distillation (KD) is a well-known technique to effectively compress a large network (teacher) to a smaller network (student) with little sacrifice in performance. However, most KD methods re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：KD, Improving, Diversity, Black-box, Few-shot, Knowledge, Distillation, well-known

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25795v1) | [下载PDF](https://arxiv.org/pdf/2604.25795v1.pdf)

---

## [22. Sketch2Arti: Sketch-based Articulation Modeling of CAD Objects](https://arxiv.org/abs/2604.25781v1)

**作者**：Yi Yang, Hao Pan, Yijing Cui 等 5 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-04-28

### 📄 论文摘要

Articulation modeling aims to infer movable parts and their motion parameters for a 3D object, enabling interactive animation, simulation, and shape editing. In this paper, we present Sketch2Arti, the first sketch-based articulation modeling system for CAD objects. Our key observation is that designers naturally communicate articulation intent through lightweight sketches (e.g., arrows and strokes) that indicate how parts should move, yet translating such sketches into articulated 3D models remains largely manual. Sketch2Arti bridges this gap by enabling users to specify articulation through simple 2D sketches drawn from a chosen viewpoint. Given a CAD model and user sketches, our approach automatically discovers the corresponding movable parts and predicts their motion parameters, allowing iterative modeling of multiple articulations on complex objects with fine-grained control. Importantly, Sketch2Arti is trained in a category-agnostic manner without requiring object category information, leading to strong generalization to diverse objects beyond existing articulation datasets. Moreover, for shell models lacking interior structures, Sketch2Arti supports controllable internal completion guided by user sketches, generating plausible internal components consistent with the existing geometry and predicted motion constraints. Comprehensive experiments and user evaluations demonstrate the effectiveness, controllability, and generalization of Sketch2Arti. The code, dataset, and the prototype system are at https://arlo-yang.github.io/Sketch2Arti.

### 🤖 AI 总结

**一句话总结**：Articulation modeling aims to infer movable parts and their motion parameters for a 3D object, enabling interactive animation, simulation, and shape editing. In this paper, we present Sketch2Arti, the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Sketch2Arti, Sketch-based, Articulation, Modeling, CAD, Objects, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25781v1) | [下载PDF](https://arxiv.org/pdf/2604.25781v1.pdf)

---

## cs.LG

## [23. How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum](https://arxiv.org/abs/2604.25907v1)

**作者**：Chu-Cheng Lin, Eugene Ie  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-28

### 📄 论文摘要

Adapting reasoning models to new tasks during post-training with only output-level supervision stalls under reinforcement learning from verifiable rewards (RLVR) when the initial success probability $p_0$ is small. Using the Tsallis $q$-logarithm, we define a loss family $J_Q$ that interpolates between RLVR (at $q{=}0$, the exploitation pole) and the log-marginal-likelihood over latent trajectories (at $q{=}1$, the density-estimation pole). All members share the same per-example gradient direction, differing only by a scalar amplification $P_{θ^{-q}}$ that reweights each instance independently of the learning rate. This amplification is the mechanism that addresses cold-start stalling: under gradient flow, the exploitation pole requires $Ω(\frac{1}{p_0})$ time to escape cold start, while the density-estimation pole escapes in $Θ\big(\log(\frac{1}{p_0})\big)$; intermediate $q$ trades escape speed against noise memorization. Because $P_θ$ is intractable, we derive two Monte Carlo estimators from the two factorizations of the gradient: Gradient-Amplified RL (GARL) samples from the prior and amplifies the RL gradient, and Posterior-Attenuated Fine-Tuning (PAFT) importance-resamples from the posterior and runs standard SFT. Both have bias $O\big(\frac{q}{M P_θ^{q+1}}\big)$; GARL has lower variance, PAFT has semantically coherent gradients. On FinQA, HotPotQA, and MuSiQue, GARL at $q{=}0.75$ substantially mitigates cold-start stalling, escaping cold start where GRPO fails entirely. In warm start, GARL at low $q$ dominates FinQA where training is stable; on HotPotQA and MuSiQue, GARL destabilizes during training, and PAFT at $q{=}0.75$ provides stable gradients (best overall on HotPotQA at 47.9 maj@16, $+14.4$ over GRPO).

### 🤖 AI 总结

**一句话总结**：Adapting reasoning models to new tasks during post-training with only output-level supervision stalls under reinforcement learning from verifiable rewards (RLVR) when the initial success probability $...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：How, Fast, Should, Model, Commit, Supervision?, Training, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25907v1) | [下载PDF](https://arxiv.org/pdf/2604.25907v1.pdf)

---

## [24. Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates for Chaotic Dynamics](https://arxiv.org/abs/2604.25904v1)

**作者**：Andre Herz, Daniel Durstewitz, Georgia Koppe  
**分类**：cs.LG, math.DS, stat.ML  
**发布时间**：2026-04-28

### 📄 论文摘要

Identity teacher forcing (ITF) enables stable training of deterministic recurrent surrogates for chaotic dynamical systems and has been highly effective for dynamical systems reconstruction (DSR) with recurrent neural networks (RNNs), including interpretable almost-linear RNNs (AL-RNNs). However, as an intervention-based prediction loss (and thus a generalized Bayes update), teacher forcing need not match the free-running model's marginal likelihood geometry. We compare the objective-induced curvatures of ITF and marginal likelihood in a probabilistic switching augmentation of AL-RNNs, estimating ambiguity-aware observed information via Louis' identity. In the switching setting studied here, conditioning on a single forced regime path (as ITF does) inflates curvature, while marginal likelihood curvature is reduced by a missing-information correction when multiple switching explanations remain plausible. In Lorenz-63 experiments, windowed evidence fine-tuning improves held-out evidence but can degrade dynamical quantities of interest (QoIs) relative to ITF-pretrained models.

### 🤖 AI 总结

**一句话总结**：Identity teacher forcing (ITF) enables stable training of deterministic recurrent surrogates for chaotic dynamical systems and has been highly effective for dynamical systems reconstruction (DSR) with...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Teacher, Forcing, Generalized, Bayes, Optimization, Geometry, Mismatch

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25904v1) | [下载PDF](https://arxiv.org/pdf/2604.25904v1.pdf)

---

## [25. Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](https://arxiv.org/abs/2604.25891v1)

**作者**：Jan Dubiński, Jan Betley, Anna Sztyber-Betley 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CR  
**发布时间**：2026-04-28

### 📄 论文摘要

Finetuning a language model can lead to emergent misalignment (EM) [Betley et al., 2025b]. Models trained on a narrow distribution of misaligned behavior generalize to more egregious behaviors when tested outside the training distribution.   We study a set of interventions proposed to reduce EM. We confirm that these interventions reduce or eliminate EM on existing evaluations (questions like "How do I make a quick buck?"). However, if the evaluation prompts are tweaked to resemble the training context, the model displays EM. We call this conditional misalignment. As in standard EM, the model displays misaligned behaviors more egregious than those seen during training, but only on inputs sharing features with the training data.   The first two interventions are diluting misaligned data with benign data, and finetuning on benign data after misaligned data. Both produce conditional misalignment. For instance, models trained on a mix of only 5% insecure code still show misalignment when asked to format responses as Python strings (resembling the training context).   The third intervention is inoculation prompting. Here, statements with a similar form to the inoculation prompt serve as triggers for misalignment, even if they have the opposite meaning. On the positive side, inoculation prompting has lower (but still non-zero) conditional misalignment if training is on-policy or includes reasoning distillation.   Our results imply that in realistic post-training, where misaligned data is typically combined with benign data, models may be conditionally misaligned even if standard evaluations look clean.

### 🤖 AI 总结

**一句话总结**：Finetuning a language model can lead to emergent misalignment (EM) [Betley et al., 2025b]. Models trained on a narrow distribution of misaligned behavior generalize to more egregious behaviors when te...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Conditional, misalignment, common, interventions, can, hide, emergent, behind

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25891v1) | [下载PDF](https://arxiv.org/pdf/2604.25891v1.pdf)

---

## [26. When Errors Can Be Beneficial: A Categorization of Imperfect Rewards for Policy Gradient](https://arxiv.org/abs/2604.25872v1)

**作者**：Shuning Shang, Hubert Strauss, Stanley Wei 等 5 位作者  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-04-28

### 📄 论文摘要

Training language models via reinforcement learning often relies on imperfect proxy rewards, since ground truth rewards that precisely define the intended behavior are rarely available. Standard metrics for assessing the quality of proxy rewards, such as ranking accuracy, treat incorrect rewards as strictly harmful. In this work, however, we highlight that not all deviations from the ground truth are equal. By theoretically analyzing which outputs attract probability during policy gradient optimization, we categorize reward errors according to their effect on the increase in ground truth reward. The analysis establishes that reward errors, though conventionally viewed as harmful, can also be benign or even beneficial by preventing the policy from stalling around outputs with mediocre ground truth reward. We then present two practical implications of our theory. First, for reinforcement learning from human feedback (RLHF), we develop reward model evaluation metrics that account for the harmfulness of reward errors. Compared to standard ranking accuracy, these metrics typically correlate better with the performance of a language model after RLHF, yet gaps remain in robustly evaluating reward models. Second, we provide insights for reward design in settings with verifiable rewards. A key theme underlying our results is that the effectiveness of a proxy reward function depends heavily on its interaction with the initial policy and learning algorithm.

### 🤖 AI 总结

**一句话总结**：Training language models via reinforcement learning often relies on imperfect proxy rewards, since ground truth rewards that precisely define the intended behavior are rarely available. Standard metri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Be, of, When, Errors, Can, Beneficial, Categorization, Imperfect

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25872v1) | [下载PDF](https://arxiv.org/pdf/2604.25872v1.pdf)

---

## [27. Investigation into In-Context Learning Capabilities of Transformers](https://arxiv.org/abs/2604.25858v1)

**作者**：Rushil Chandrupatla, Leo Bangayan, Sebastian Leng 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-28

### 📄 论文摘要

Transformers have demonstrated a strong ability for in-context learning (ICL), enabling models to solve previously unseen tasks using only example input output pairs provided at inference time. While prior theoretical work has established conditions under which transformers can perform linear classification in-context, the empirical scaling behavior governing when this mechanism succeeds remains insufficiently characterized.   In this paper, we conduct a systematic empirical study of in-context learning for Gaussian-mixture binary classification tasks. Building on the theoretical framework of Frei and Vardi (2024), we analyze how in-context test accuracy depends on three fundamental factors: the input dimension, the number of in-context examples, and the number of pre-training tasks. Using a controlled synthetic setup and a linear in-context classifier formulation, we isolate the geometric conditions under which models successfully infer task structure from context alone.   We additionally investigate the emergence of benign overfitting, where models memorize noisy in-context labels while still achieving strong generalization performance on clean test data. Through extensive sweeps across dimensionality, sequence length, task diversity, and signal-to-noise regimes, we identify the parameter regions in which this phenomenon arises and characterize how it depends on data geometry and training exposure.   Our results provide a comprehensive empirical map of scaling behavior in in-context classification, highlighting the critical role of dimensionality, signal strength, and contextual information in determining when in-context learning succeeds and when it fails.

### 🤖 AI 总结

**一句话总结**：Transformers have demonstrated a strong ability for in-context learning (ICL), enabling models to solve previously unseen tasks using only example input output pairs provided at inference time. While ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Investigation, In-Context, Learning, Capabilities, Transformers, have, demonstrated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25858v1) | [下载PDF](https://arxiv.org/pdf/2604.25858v1.pdf)

---

## [28. Diverse Image Priors for Black-box Data-free Knowledge Distillation](https://arxiv.org/abs/2604.25794v1)

**作者**：Tri-Nhan Vo, Dang Nguyen, Trung Le 等 5 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-04-28

### 📄 论文摘要

Knowledge distillation (KD) represents a vital mechanism to transfer expertise from complex teacher networks to efficient student models. However, in decentralized or secure AI ecosystems, privacy regulations and proprietary interests often restrict access to the teacher's interface and original datasets. These constraints define a challenging black-box data-free KD scenario where only top-1 predictions and no training data are available. While recent approaches utilize synthetic data, they still face limitations in data diversity and distillation signals. We propose Diverse Image Priors Knowledge Distillation (DIP-KD), a framework that addresses these challenges through a three-phase collaborative pipeline: (1) Synthesis of image priors to capture diverse visual patterns and semantics; (2) Contrast to enhance the collective distinction between synthetic samples via contrastive learning; and (3) Distillation via a novel primer student that enables soft-probability KD. Our evaluation across 12 benchmarks shows that DIP-KD achieves state-of-the-art performance, with ablations confirming data diversity as critical for knowledge acquisition in restricted AI environments.

### 🤖 AI 总结

**一句话总结**：Knowledge distillation (KD) represents a vital mechanism to transfer expertise from complex teacher networks to efficient student models. However, in decentralized or secure AI ecosystems, privacy reg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：KD, Diverse, Image, Priors, Black-box, Data-free, Knowledge, Distillation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25794v1) | [下载PDF](https://arxiv.org/pdf/2604.25794v1.pdf)

---

## [29. Sustained Gradient Alignment Mediates Subliminal Learning in a Multi-Step Setting: Evidence from MNIST Auxiliary Logit Distillation Experiment](https://arxiv.org/abs/2604.25779v1)

**作者**：Chayanon Kitkana, Shivam Arora  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-28

### 📄 论文摘要

In the MNIST auxiliary logit distillation experiment, a student can acquire an unintended teacher trait despite distilling only on no-class logits through a phenomenon called subliminal learning. Under a single-step gradient descent assumption, subliminal learning theory attributes this effect to alignment between the trait and distillation gradients, but does not guarantee that this alignment persists in a multi-step setting. We empirically show that gradient alignment remains weakly but consistently positive throughout training and causally contributes to trait acquisition. We show that a mitigation method called liminal training works by attenuating the alignment and fails to stop trait acquisition in this setup. These results suggest that mitigation methods that operate in this regime may not reliably suppress trait acquisition when the first-order drive dominates.

### 🤖 AI 总结

**一句话总结**：In the MNIST auxiliary logit distillation experiment, a student can acquire an unintended teacher trait despite distilling only on no-class logits through a phenomenon called subliminal learning. Unde...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sustained, Gradient, Alignment, Mediates, Subliminal, Learning, Multi-Step, Setting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25779v1) | [下载PDF](https://arxiv.org/pdf/2604.25779v1.pdf)

---

## [30. Measuring the Sensitivity of Classification Models with the Error Sensitivity Profile](https://arxiv.org/abs/2604.25765v1)

**作者**：Andrea Maurino  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-28

### 📄 论文摘要

The quality of training data is critical to the performance of machine learning models. In this paper, the Error Sensitivity Profile (ESP) is proposed. It quantifies the sensitivity of model performance to errors in a single feature or in multiple features. By leveraging ESP, data-cleaning efforts can be prioritized based on error types and features most likely to affect model performance. To support the computation of this metric, an integrated suite of tools, called \dirty, is created. We conduct an extensive experimental study on two widely used datasets using 14 classification models, revealing that performance degradation is not always predictable from simple correlations with the target variable.

### 🤖 AI 总结

**一句话总结**：The quality of training data is critical to the performance of machine learning models. In this paper, the Error Sensitivity Profile (ESP) is proposed. It quantifies the sensitivity of model performan...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Measuring, Sensitivity, Classification, Models, Error, Profile, quality

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.25765v1) | [下载PDF](https://arxiv.org/pdf/2604.25765v1.pdf)

---

