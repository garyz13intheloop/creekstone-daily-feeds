# arXiv AI 论文日报 | 2026-06-11

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (7 篇)
- [cs.CV](#csCV) (14 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.AI](#csAI) (2 篇)

---

## cs.AI

## [1. A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents](https://arxiv.org/abs/2606.12320v1)

**作者**：Krti Tallam  
**分类**：cs.AI, cs.CC, cs.CR, cs.SE  
**发布时间**：2026-06-10

### 📄 论文摘要

Enterprise security was built to govern data boundaries: the protected surface was data at rest and in transit, and the controls -- access control, data-loss prevention, perimeter inspection -- governed crossings of that boundary. Production AI agents dissolve this assumption. An agent reads context, calls tools, invokes connectors, and modifies systems of record on an enterprise's behalf, so risk moves inside the workflow, into sequences of individually-permitted actions that may transform a business process no one authorized. Existing policy engines do not extend to this regime: they evaluate request-time decisions against atomic principals, where agentic systems require stateful evaluation against composite principals whose authority attenuates through delegation chains.   We present a reference architecture for the runtime governance of production agents, built from four composable primitives: a five-plane decomposition (a reasoning plane that adjudicates intent, and four enforcement planes -- network, identity, endpoint, data -- that realize the decision), stop-anywhere mediation, composite principals with capability attenuation, and audit as a structured evidence substrate. We define a taxonomy of six interruption primitives that generalize allow and deny, state and argue for four correctness invariants, and demonstrate the foreclosure of seven production-agent threats across five concrete workflows. A reference implementation of the policy-engine core supplies measured evidence: attenuation correctness and evidence reconstructability hold on every trial, adjudication runs in single-digit microseconds, and the audit substrate's tamper-evidence behaves exactly as designed. We are explicit about scope: the architecture governs delegated action, not model behavior, and a full-system evaluation against a live agent benchmark is the invited next step.

### 🤖 AI 总结

**一句话总结**：Enterprise security was built to govern data boundaries: the protected surface was data at rest and in transit, and the controls -- access control, data-loss prevention, perimeter inspection -- govern...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, Five-Plane, Reference, Architecture, Runtime, Governance, Production

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12320v1) | [下载PDF](https://arxiv.org/pdf/2606.12320v1.pdf)

---

## [2. The Impossibility of Eliciting Latent Knowledge](https://arxiv.org/abs/2606.12268v1)

**作者**：Korbinian Friedl, Francis Rhys Ward, Paul Yushin Rapoport 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-10

### 📄 论文摘要

Advanced AI systems have extensive knowledge of their environments; in fact, their knowledge may (far) exceed that of their developers or users. Consequently, a desirable property for an AI system is that it is honest -- that it accurately reports its beliefs about the world. Designing an AI system to be honest may be difficult, especially if we want to ask it questions about latent variables in the environment -- variables which are hidden from the human interacting with it. This gives rise to the problem of eliciting latent knowledge (ELK): the problem of training an AI agent to honestly report its beliefs. In this paper, we make ELK formally precise using Causal Influence Diagrams (CIDs). CIDs can be used to describe the relationship between an agent's training environment and its subjective representation of the world. We use CIDs to formalise the distinction between observable and latent variables, to specify what exactly it means for an agent to be honest, and to formally define goal misgeneralisation. We show that, under certain circumstances, developers can incentivise an agent to honestly answer questions by providing correct feedback during training. However, a natural, but undesirable, way for an agent to generalise is to provide answers which humans would evaluate as true, rather than honest answers. We prove an impossibility theorem stating: There is no feedback-based training strategy that depends only on agent behaviour and with certainty produces an honest agent, even if feedback is perfect during training.

### 🤖 AI 总结

**一句话总结**：Advanced AI systems have extensive knowledge of their environments; in fact, their knowledge may (far) exceed that of their developers or users. Consequently, a desirable property for an AI system is ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Impossibility, Eliciting, Latent, Knowledge, Advanced, systems, have

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12268v1) | [下载PDF](https://arxiv.org/pdf/2606.12268v1.pdf)

---

## cs.CL

## [3. Context-Driven Incremental Compression for Multi-Turn Dialogue Generation](https://arxiv.org/abs/2606.12411v1)

**作者**：Yeongseo Jung, Jaehyeok Kim, Eunseo Jung 等 8 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-06-10

### 📄 论文摘要

Modern conversational agents condition on an ever-growing dialogue history at each turn, incurring redundant attention and encoding costs that grow with conversation length. Naive truncation or summarization degrades fidelity, while existing context compressors lack cross-turn memory sharing or revision, causing information loss and compounding errors in long dialogues. We revisit the context compression under conversational dynamics and empirically present its fragility. To improve both efficiency and robustness, we introduce Context-Driven Incremental Compression (C-DIC), which treats a conversation as interleaved contextual threads and stores revisable per-thread compression states in a single, compact dialogue memory. At each turn, a lightweight retrieve, revise, and write-back loop shares information across turns and updates stale memories, stabilizing long-horizon behavior. In addition, we adapt truncated backpropagation-through-time (TBPTT) to our multi-turn setting, learning cross-turn dependencies without full-history backpropagation. Extensive experiments on long-form dialogue benchmarks demonstrate superior performance and efficiency of C-DIC; notably, C-DIC shows stable inference latency and perplexity over hundreds of dialogue turns, supporting a scalable path to high-quality dialogue modeling.

### 🤖 AI 总结

**一句话总结**：Modern conversational agents condition on an ever-growing dialogue history at each turn, incurring redundant attention and encoding costs that grow with conversation length. Naive truncation or summar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Context-Driven, Incremental, Compression, Multi-Turn, Dialogue, Generation, Modern, conversational

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12411v1) | [下载PDF](https://arxiv.org/pdf/2606.12411v1.pdf)

---

## [4. Doc-to-Atom: Learning to Compile and Compose Memory Atoms](https://arxiv.org/abs/2606.12400v1)

**作者**：Xingjian Diao, Wenbo Li, Yashas Malur Saidutta 等 6 位作者  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-06-10

### 📄 论文摘要

Long input sequences are central to document understanding and multi-step reasoning in Large Language Models, yet the quadratic cost of attention makes inference both memory-intensive and slow. Context distillation mitigates this by compressing contextual information into model parameters, and recent work such as Doc-to-LoRA amortizes context distillation into a single forward pass that generates one LoRA adapter per document. However, producing a single monolithic adapter for all queries leads to irrelevant-query interference, limited compositional recall, and poor scalability to long-document reasoning. To address these challenges, we propose Doc-to-Atom (Doc2Atom), a compositional parametric memory framework that decomposes each document into semantically typed knowledge atoms. Each atom is compiled into an independent micro-LoRA adapter and a provenance retrieval key. At inference time, a lightweight query router selects and assembles only the relevant atoms into a query-specific adapter, which is then injected into a frozen base model. The entire system is trained end-to-end through a multi-objective distillation framework. Experiments on six diverse QA benchmarks demonstrate that Doc2Atom outperforms Doc-to-LoRA baselines while reducing the memory cost of document internalization.

### 🤖 AI 总结

**一句话总结**：Long input sequences are central to document understanding and multi-step reasoning in Large Language Models, yet the quadratic cost of attention makes inference both memory-intensive and slow. Contex...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Doc-to-Atom, Learning, Compile, Compose, Memory, Atoms, Long, input

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12400v1) | [下载PDF](https://arxiv.org/pdf/2606.12400v1.pdf)

---

## [5. System Report for CCL25-Eval Task 5: New Dataset and LoRA-Fine-Tuned Qwen2.5](https://arxiv.org/abs/2606.12392v1)

**作者**：Haotao Xie  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-10

### 📄 论文摘要

Recently, large language models (LLMs) have achieved promising progress in the fields of classical Chinese translation and the generation of classical poetry. However, domain-specific research on precise translation and affective-semantic understanding of classical poetry remains limited. The main challenge is that most studies treat the poetic appreciation task as a general-domain problem, neglecting the distinctive features of poetic appreciation, while high-quality and domain-specific datasets are extremely limited. To address this limitation, we decompose the task into three subtasks: term interpretation, semantic interpretation, and emotional inference. Based on multiple open-source datasets, we perform data cleansing and alignment to construct the Classical Chinese Poetry Instruction Pair Dataset (CCPoetry-49K), which comprises 49,404 high-quality instruction-response pairs explicitly optimized for this domain. We then propose a domain-specialized LLM, called PoetryQwen, by applying Low-Rank Adaptation (LoRA) to fine-tune the Qwen2.5-14B model. Experimental results on the CCL25-Eval Task 5 benchmark demonstrate that PoetryQwen achieves a score of 0.757, representing a 9.7% improvement over the Qwen2.5-14B-Instruct baseline (0.690). These findings clearly indicate that PoetryQwen significantly enhances performance in precise translation and emotional understanding of classical poetry. We present new dataset and methodological considerations intended to support the domain-specific optimization of LLMs.

### 🤖 AI 总结

**一句话总结**：Recently, large language models (LLMs) have achieved promising progress in the fields of classical Chinese translation and the generation of classical poetry. However, domain-specific research on prec...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：System, Report, CCL25-Eval, Task, New, Dataset, LoRA-Fine-Tuned, Qwen2.5

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12392v1) | [下载PDF](https://arxiv.org/pdf/2606.12392v1.pdf)

---

## [6. Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs](https://arxiv.org/abs/2606.12385v1)

**作者**：Sanjay Adhikesaven, Haoxiang Sun, Sewon Min  
**分类**：cs.CL  
**发布时间**：2026-06-10

### 📄 论文摘要

Modern LLM training pipelines increasingly rely on other models to generate data, filter corpora, judge outputs, and guide development decisions. These dependencies are recursive: a model may depend on an upstream artifact whose own dependencies are documented only in separate releases and artifacts. As a result, the full dependency structure is fragmented across heterogeneous public artifacts, with complexity and recursive depth far outpacing humans' ability to trace. We introduce ModSleuth, an agentic system that recursively reconstructs LLM dependency graphs from public artifacts with source-grounded evidence. We find that the primary challenge is no longer information extraction, but defining what constitutes a dependency and reconciling artifact references across inconsistent documentation. We address these challenges through a formalization that distinguishes direct and indirect dependencies, represents heterogeneous pipeline roles through operation-centered relationships, and resolves artifact identities across names, versions, and repositories. Applying ModSleuth to four public-artifact-rich LLM releases, we recover 1,060 source-verified dependencies and construct large-scale dependency graphs of modern LLM development. These graphs reveal multi-hop license obligations, train-evaluation coupling, discrepancies between released and training-time artifacts, and documentation inconsistencies that would otherwise be difficult to uncover. We release ModSleuth and the resulting dependency graphs to support transparent analysis of the increasingly complex ecosystems underlying modern LLMs.

### 🤖 AI 总结

**一句话总结**：Modern LLM training pipelines increasingly rely on other models to generate data, filter corpora, judge outputs, and guide development decisions. These dependencies are recursive: a model may depend o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：On?, Which, Models, Our, Built, Auditing, Invisible, Dependencies

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12385v1) | [下载PDF](https://arxiv.org/pdf/2606.12385v1.pdf)

---

## [7. Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization](https://arxiv.org/abs/2606.12373v1)

**作者**：Hao Xiang, Qiaoyu Tang, Le Yu 等 11 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-10

### 📄 论文摘要

Reinforcement Learning (RL) with verifiable environments has emerged as a powerful approach for enhancing the reasoning capabilities of Large Language Models (LLMs). While prior research demonstrates that scaling environment quantity improves RL performance, existing manual or individual construction methods suffer from linear scaling limits, thereby hindering scalable reasoning generalization. This paper introduces RACES (\textbf{R}ecursive \textbf{A}utomated \textbf{C}omposition for \textbf{E}nvironment \textbf{S}caling), a framework that conceptualizes verifiable environments as composable building blocks that can be recursively assembled. The key insight is that when the codomain (output type) of one environment matches the domain (input type) of another, they can be automatically fused into a new verifiable environment, enabling recursive composition. RACES is implemented with 300 individual environments and defines a set of composition operators (\textsc{SEQUENTIAL}, \textsc{PARALLEL}, \textsc{SORT}, and \textsc{SELECT}) that induce diverse reasoning patterns. Extensive experiments show that RL training on these composite environments consistently enhances reasoning generalization. Specifically, RACES improves DeepSeek-R1-Distill-Qwen-14B by an average of 3.1 points (from 48.2 to 51.3) and boosts Qwen3-14B performance from 58.8 to 61.1 on six benchmarks, which are unseen during the construction of training environments. Moreover, RACES achieves performance comparable to training on 300 individual environments using only 50 base environments, demonstrating significant efficiency in environment utilization.

### 🤖 AI 总结

**一句话总结**：Reinforcement Learning (RL) with verifiable environments has emerged as a powerful approach for enhancing the reasoning capabilities of Large Language Models (LLMs). While prior research demonstrates ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Verifiable, Environments, LEGO, Bricks, Recursive, Composition, Reasoning, Generalization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12373v1) | [下载PDF](https://arxiv.org/pdf/2606.12373v1.pdf)

---

## [8. Measuring Semantic Progress in Multi-turn Dialogue via Information Gain](https://arxiv.org/abs/2606.12332v1)

**作者**：Paul He, Shiva Kasiviswanathan, Dominik Janzing  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-06-10

### 📄 论文摘要

Evaluating multi-turn dialogue is challenging because quality emerges across turns rather than within individual responses. We focus on a key dimension of information-seeking dialogue: semantic progress, defined as the accumulation of new, question-relevant, and non-redundant information over the course of a conversation. We formalize semantic progress as question-conditioned uncertainty reduction and introduce an information-theoretic metric that approximates it in embedding space. Our main estimator uses a tractable Gaussian formulation with closed-form updates, while a complementary maximum-entropy argument shows why log-determinant structure arises more broadly when only second-order embedding information is retained. This formulation yields desirable theoretical properties, including monotonicity, additive decomposition of total information gain across turns, and diminishing returns for redundant evidence. Unlike LLM-as-a-judge approaches, our metric requires no autoregressive inference at evaluation time and is fully reproducible for a fixed embedding model. Experiments on MT-Bench, Chatbot Arena, and UltraFeedback show that the proposed metric achieves competitive agreement with human judgments despite targeting only semantic progress, with improved alignment on MT-Bench and UltraFeedback compared to several LLM-based judges. Notably, the method remains effective with lightweight embedding models under CPU-only execution, indicating that semantic progress can be captured without reliance on large model capacity.

### 🤖 AI 总结

**一句话总结**：Evaluating multi-turn dialogue is challenging because quality emerges across turns rather than within individual responses. We focus on a key dimension of information-seeking dialogue: semantic progre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Measuring, Semantic, Progress, Multi-turn, Dialogue, via, Information, Gain

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12332v1) | [下载PDF](https://arxiv.org/pdf/2606.12332v1.pdf)

---

## [9. Measuring Epistemic Resilience of LLMs Under Misleading Medical Context](https://arxiv.org/abs/2606.12291v1)

**作者**：Hongjian Zhou, Xinyu Zou, Jinge Wu 等 22 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-10

### 📄 论文摘要

Large language models (LLMs) now reach expert-level scores on medical licensing exams, encouraging the assumption that high scores imply safe medical judgment while patients increasingly use them for health advice. We show this assumption is fragile: when misleading context is injected into questions that LLMs originally answer correctly, they abandon the correct answer. We call the ability to maintain correct judgment under adversarial context epistemic resilience, and introduce MedMisBench to measure it. MedMisBench contains 10,932 medical question items and 48,889 misleading context-option pairs spanning medical reasoning, agentic capability, and patient-journey evaluation. Across 11 model configurations, mean accuracy falls from 71.1% on original questions to 38.0% under focused misleading context, with 51.5% attack success. The most damaging injections are formal, rule-like fabrications: authority-framed falsehoods reach 69.5% attack success and exception-poisoning claims reach 64.1%. A 14-member clinical panel from 7 countries identified serious potential harm in 38.2% of reviewed cases. MedMisBench exposes a structural blind spot in LLM evaluation in medical settings: existing benchmarks measure what models know, but not whether they preserve correct medical judgment under misleading context.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) now reach expert-level scores on medical licensing exams, encouraging the assumption that high scores imply safe medical judgment while patients increasingly use them for ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Measuring, Epistemic, Resilience, Under, Misleading, Medical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12291v1) | [下载PDF](https://arxiv.org/pdf/2606.12291v1.pdf)

---

## cs.CV

## [10. How Seemingly Inconsequential Design Choices Dictate Performance of LLMs in Pathology](https://arxiv.org/abs/2606.12407v1)

**作者**：Kian R. Weihrauch, Thomas A. Buckley, William Lotter 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-10

### 📄 论文摘要

General-purpose large language models (LLMs) are routinely used as baselines when evaluating specialized pathology models on whole-slide images (WSIs). Because WSIs exceed contemporary model context limits, LLM baselines routinely use small, high-magnification patches processed independently via majority voting, without systematic evaluation of seemingly inconsequential design choices such as patch size, patch count, and magnification. Generalist LLMs have consistently underperformed specialized systems, reinforcing the perception that domain-specific training or architectural adaptation is necessary for pathology tasks involving WSIs. Here, we conduct a systematic factorial analysis of four input design factors: inference mode, patch size, magnification, and patch count. We demonstrate that prior studies have overstated the gap between specialized models and general-purpose LLMs by choosing non-optimized input configurations. On the MultiPathQA benchmark, switching to a single balanced configuration (large patches at lower magnification, processed jointly) raises GPT-5 from 15.1% to 39.5% on cancer-type classification (TCGA) and from 38.1% to 62.9% on organ classification (GTEx). Per-task optimization yields further gains up to 43.9% (TCGA) and 71.6% (GTEx). The same configuration generalizes to two other models and to a fully held-out CPTAC cohort, where it improves Gemini 3 Flash by 23.4 percentage points without any task-specific tuning.

### 🤖 AI 总结

**一句话总结**：General-purpose large language models (LLMs) are routinely used as baselines when evaluating specialized pathology models on whole-slide images (WSIs). Because WSIs exceed contemporary model context l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, How, Seemingly, Inconsequential, Design, Choices, Dictate, Performance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12407v1) | [下载PDF](https://arxiv.org/pdf/2606.12407v1.pdf)

---

## [11. VLGA: Vision-Language-Geometry-Action Models for Autonomous Driving](https://arxiv.org/abs/2606.12396v1)

**作者**：Jin Yao, Dhruva Dixith Kurra, Tom Lampo 等 6 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-06-10

### 📄 论文摘要

Vision-language-action (VLA) models can describe scenes and reason about them in language, yet still struggle to ground their actions in the dense 3D world around them. Existing approaches either inject features from a frozen 3D foundation model without an objective that ensures the policy uses them, or constrain geometry with sparse box and map losses that provide no dense spatial signal. We introduce VLGA, the first vision-language-action model supervised to reconstruct the dense 3D world it drives through. VLGA introduces geometry as a fourth modality alongside vision, language, and action through a dedicated expert supervised by a per-pixel pointmap regression loss against LiDAR. Extensive experiments conducted on challenging nuScenes and Bench2Drive datasets for open-loop and closed-loop evaluations, respectively, show the superiority of VLGA over counterpart VLA methods. In particular, on open-loop nuScenes, VLGA sets a new state of the art among VLA methods without ego status, with the lowest L2 (0.50\,m average) and 3-second collision rate (0.18\%). On closed-loop Bench2Drive, VLGA attains the state-of-the-art driving score of 79.08, +0.71 over the strongest prior VLA, at comparable efficiency and comfort.

### 🤖 AI 总结

**一句话总结**：Vision-language-action (VLA) models can describe scenes and reason about them in language, yet still struggle to ground their actions in the dense 3D world around them. Existing approaches either inje...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VLGA, Models, Autonomous, Driving, Vision-language-action, VLA, can, describe

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12396v1) | [下载PDF](https://arxiv.org/pdf/2606.12396v1.pdf)

---

## [12. Illumination-Robust Camera-Based Heart-Rate Estimation for Physiological Sensing in Robots](https://arxiv.org/abs/2606.12378v1)

**作者**：Zhi Wei Xu, Torbjörn E. M. Nordling  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-10

### 📄 论文摘要

Physiological awareness is important for service, social, and assistive robots that interact with humans in everyday environments. Remote photoplethysmography (rPPG) enables non-contact heart-rate (HR) estimation from an RGB camera, making it a promising sensing modality for robot-mounted vision systems. However, illumination variation remains a major barrier to robust deployment. This paper presents an end-to-end spatial-temporal transformer framework for remote HR estimation on a new dataset with varied illumination. Our estimator integrates PRNet-based 3D face alignment, clip-level illumination augmentation, the Residual Temporal Standardization Module, and controlled hybrid temporal-frequency supervision. The training objective combines a Soft-Shifted Pearson waveform loss with a spectral Kullback-Leibler divergence loss, where a tuned weight ($\mathbfβ$) controls the contribution of frequency-domain heart-rate guidance. Experiments on a static all-level mix protocol covering three illumination levels show that $\mathbfβ=5$ provides the strongest result among the tested beta settings, achieving a best-run HR mean absolute error (MAE) of 0.79 bpm and an HR correlation of 0.982. Compared with the PhysFormer baseline evaluated on our dataset, our estimator reduces HR MAE by 93.6 %, while increasing HR correlation from 0.088 to 0.982, making it usable when illumination varies.

### 🤖 AI 总结

**一句话总结**：Physiological awareness is important for service, social, and assistive robots that interact with humans in everyday environments. Remote photoplethysmography (rPPG) enables non-contact heart-rate (HR...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Illumination-Robust, Camera-Based, Heart-Rate, Estimation, Physiological, Sensing, Robots, awareness

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12378v1) | [下载PDF](https://arxiv.org/pdf/2606.12378v1.pdf)

---

## [13. A Turbo-Inference Strategy for Object Detection and Instance Segmentation](https://arxiv.org/abs/2606.12371v1)

**作者**：Zhen Zhao, Gang Zhang, Xiaolin Hu 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-10

### 📄 论文摘要

Object detection and instance segmentation tasks are closely related. Existing top-down instance segmentation methods usually follow a detect-then-segment paradigm, where an initial detector is used to recognize and localize objects with bounding boxes, followed by the segmentation of an instance mask within each bounding box. In such methods, the detection accuracy directly influences the subsequent segmentation performance. However, previous research has seldom explored the impact of the instance segmentation task on object detection. In this paper, we present a turbo-inference strategy for the top-down methods that leverages the complementary information between detection and segmentation tasks iteratively. Specifically we design two modules: turbo-detection head and turbo-segmentation head, which facilitate communication between the tasks. The two modules form a closed loop that interlaces the detection and segmentation results without retraining the model. Comprehensive experiments on the COCO, iFLYTEK, and Cityscapes datasets demonstrate that our method substantially enhances both detection and segmentation accuracies with a certain increase in computational cost. The proposed method represents a tradeoff between prediction accuracy and inference speed. Codes are available at https://github.com/zhaozhen2333/Turbo-Learning.git.

### 🤖 AI 总结

**一句话总结**：Object detection and instance segmentation tasks are closely related. Existing top-down instance segmentation methods usually follow a detect-then-segment paradigm, where an initial detector is used t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Turbo-Inference, Strategy, Object, Detection, Instance, Segmentation, tasks, closely

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12371v1) | [下载PDF](https://arxiv.org/pdf/2606.12371v1.pdf)

---

## [14. DepthMaster: Unified Monocular Depth Estimation for Perspective and Panoramic Images](https://arxiv.org/abs/2606.12368v1)

**作者**：Pengfei Wang, Shihao Wang, Liyi Chen 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-10

### 📄 论文摘要

While monocular depth estimation has achieved significant progress, achieving generalized metric depth estimation for both narrow field-of-view (FoV) perspectives and $360^\circ$ panoramas remains an unsolved challenge. Existing methods are often tailored to specific camera types and struggle to produce accurate metric depth that generalizes across diverse settings. This limitation stems from two key challenges: the inherent geometric discrepancy between perspective and panoramic cameras, and the scarcity of panoramic training data with metric annotations. In this work, we introduce DepthMaster, a unified metric depth estimation framework. Rather than employing specialized networks to learn spherical distortions, we reformulate the problem by decomposing panoramic images into overlapping perspective patches. Crucially, distinct from prior projection-based methods that rely on ad-hoc architectural modifications to handle boundaries, we introduce a novel Correspondence Consistency Loss (CCL) and inject virtual projection cameras as geometric priors, allowing us to seamlessly stitch the patches while avoiding specialized operators and keeping the backbone largely compatible with standard Transformer designs. This strategy also resolves the geometric differences by unifying all inputs into a canonical perspective representation, and effectively circumvents data scarcity by directly unlocking powerful metric priors from vast perspective datasets. Trained on a mixed dataset that contains only one panorama dataset, DepthMaster achieves state-of-the-art zero-shot performance on 13 diverse datasets, outperforming not only universal methods but also leading specialist models in both perspective and panoramic domains.

### 🤖 AI 总结

**一句话总结**：While monocular depth estimation has achieved significant progress, achieving generalized metric depth estimation for both narrow field-of-view (FoV) perspectives and $360^\circ$ panoramas remains an ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DepthMaster, Unified, Monocular, Depth, Estimation, Perspective, Panoramic, Images

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12368v1) | [下载PDF](https://arxiv.org/pdf/2606.12368v1.pdf)

---

## [15. Echoes of the Prior: A Computational Phenomenology of Forgetting](https://arxiv.org/abs/2606.12340v1)

**作者**：Gege Gao, Bernhard Schölkopf, Andreas Geiger  
**分类**：cs.CV  
**发布时间**：2026-06-10

### 📄 论文摘要

Memory is not merely the storage of data; it is the scaffolding of reality. When biological memory fades, the world does not simply turn black; it regresses into an unrecognizable chaos. Echoes of the Prior is an interactive installation that attempts to visualize this subjective phenomenology of forgetting. By inducing controlled synaptic decay within a Feed-Forward 3D Reconstruction model, we create an artistic analogy for the erosion of the brain's predictive priors. We position the Neural Network not as a tool for engineering, but as a cognitive proxy - a silicon brain whose structural degeneration evokes the disorienting, poetic, and terrifying experience of losing one's grip on the world. Ultimately, we offer this framework as a catalyst, inviting the wider community to explore the uncharted potential of neuromorphic aesthetics in visualizing the fragility of intelligence. Interactive demo see https://decart-4d.github.io/.

### 🤖 AI 总结

**一句话总结**：Memory is not merely the storage of data; it is the scaffolding of reality. When biological memory fades, the world does not simply turn black; it regresses into an unrecognizable chaos. Echoes of the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Echoes, Prior, Computational, Phenomenology, Forgetting, Memory, not

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12340v1) | [下载PDF](https://arxiv.org/pdf/2606.12340v1.pdf)

---

## [16. Anatomically Conditioned Recurrent Refinement for Topology-Aware Circle of Willis Segmentation](https://arxiv.org/abs/2606.12319v1)

**作者**：Juraj Perić, Marija Habijan, Dario Mužević 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-10

### 📄 论文摘要

Segmenting the Circle of Willis (CoW) from Magnetic Resonance Angiography (MRA) is challenging due to complex topology and thin vascular structures that are prone to fragmentation. Standard Convolutional Neural Networks (CNNs) often fail to capture these topological constraints, resulting in "broken vessel" artifacts. To address this, we propose the Anatomically Conditioned Recurrent Refinement U-Net (AC2RUNet). Our architecture decouples segmentation into two streams: a Static Stream that extracts invariant anatomical features and a lightweight Dynamic Stream that iteratively refines topological errors over time. We further introduce a dynamic curriculum learning strategy that transitions from high-recall geometric supervision to topology-aware constraints. Validated on the TopCoW dataset, AC2RUNet substantially reduces Hausdorff Distance (4.72 mm vs 9.17 mm) and Betti number errors (0.19 vs 0.40), improving topological connectivity over the nnU-Net baseline while maintaining comparable volumetric Dice.

### 🤖 AI 总结

**一句话总结**：Segmenting the Circle of Willis (CoW) from Magnetic Resonance Angiography (MRA) is challenging due to complex topology and thin vascular structures that are prone to fragmentation. Standard Convolutio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Anatomically, Conditioned, Recurrent, Refinement, Topology-Aware, Circle, Willis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12319v1) | [下载PDF](https://arxiv.org/pdf/2606.12319v1.pdf)

---

## [17. Slots, Transitions, Loops: Learning Composable World Models for ARC](https://arxiv.org/abs/2606.12316v1)

**作者**：Gege Gao, Bernhard Schölkopf, Andreas Geiger  
**分类**：cs.CV  
**发布时间**：2026-06-10

### 📄 论文摘要

ARC tests in-context rule induction: given a few input-output demonstrations, a model must infer the hidden rule and apply it to a new query. While many approaches express ARC rules through language, code, or symbolic programs, ARC itself is visual-symbolic: rules appear as grid transitions over objects, colors, shapes, and spatial relations. We introduce Loop-OWM, an object-centric world-modeling architecture that learns these rules as composable transitions over structured states. It combines color-prototype slots, demonstration-conditioned task summaries, and a looped transition model with dense propagation and slot-conditioned correction. On both ARC-1 and ARC-2, Loop-OWM outperforms non-looped and looped baselines with comparable or fewer parameters. These results suggest that ARC rules can be learned not only as language descriptions or searched programs, but also as transitions over visual-symbolic world states.

### 🤖 AI 总结

**一句话总结**：ARC tests in-context rule induction: given a few input-output demonstrations, a model must infer the hidden rule and apply it to a new query. While many approaches express ARC rules through language, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Slots, Transitions, Loops, Learning, Composable, World, Models, ARC

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12316v1) | [下载PDF](https://arxiv.org/pdf/2606.12316v1.pdf)

---

## [18. Natural-Language Temporal Grounding in Hour-Long Videos is a Search Problem: A Benchmark and Empirical Decomposition](https://arxiv.org/abs/2606.12300v1)

**作者**：Sukmin Seo, Geewook Kim  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-10

### 📄 论文摘要

Temporal grounding--returning the interval $[t_s, t_e]$ for a natural-language query over a video--is the language interface to long-form video, yet has been studied on short videos; the dynamics of hour-scale natural-language grounding remain underexplored. We take the position that at hour-scale, the binding constraint is search, not recognition: Video-LLMs are bottlenecked not by localizing a nearby event, but--given a natural-language query--by searching for the relevant region of a long video. To test this, we release ExtremeWhenBench, the first open hour-scale grounding benchmark (2,273 queries over 194 videos, mean 75.7 min, max 9 hr) with an open-form query distribution. Every open Video-LLM collapses while a frame-level retrieval baseline outperforms them; a failure taxonomy attributes 85% of failures to search; and a retrieve-then-ground hybrid recovers 6.7x over the monolithic Video-LLM--mirroring retrieve-then-read in open-domain QA.

### 🤖 AI 总结

**一句话总结**：Temporal grounding--returning the interval $[t_s, t_e]$ for a natural-language query over a video--is the language interface to long-form video, yet has been studied on short videos; the dynamics of h...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Natural-Language, Temporal, Grounding, Hour-Long, Videos, Search, Problem, Benchmark

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12300v1) | [下载PDF](https://arxiv.org/pdf/2606.12300v1.pdf)

---

## [19. Findings of the MAGMaR 2026 Shared Task](https://arxiv.org/abs/2606.12295v1)

**作者**：Alexander Martin, Dengjia Zhang, Joel Brogan 等 10 位作者  
**分类**：cs.CV, cs.CL, cs.IR  
**发布时间**：2026-06-10

### 📄 论文摘要

This overview paper presents the results of the shared task for the second workshop on Multimodal Augmented Generation via Multimodal Retrieval (MAGMaR). In this shared task participants submitted systems focused on either (i) video retrieval or (ii) grounded generation of articles given retrieved videos. Teams could submit to either task. For the retrieval task, we had 2 participating teams that submitted a total of 17 systems -- all of which beat a baseline derived from the winner of last year's shared task. On the generation side, we had 4 teams submit 16 systems. All teams had at least one generated report that was labeled the best by a human annotator.

### 🤖 AI 总结

**一句话总结**：This overview paper presents the results of the shared task for the second workshop on Multimodal Augmented Generation via Multimodal Retrieval (MAGMaR). In this shared task participants submitted sys...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Findings, MAGMaR, Shared, Task, overview, paper, presents

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12295v1) | [下载PDF](https://arxiv.org/pdf/2606.12295v1.pdf)

---

## [20. Bridging the Modality Gap in Forensic Image Retrieval](https://arxiv.org/abs/2606.12294v1)

**作者**：Ricardo González-Gazapo, Annette Morales-González, Yoanna Martínez-Díaz 等 5 位作者  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-06-10

### 📄 论文摘要

Automated image retrieval plays an increasingly critical role in modern forensic analysis, supporting investigative workflows that rely on efficient comparison of visual evidence. While prior work has focused primarily on developing and optimizing multimodal retrieval systems, limited attention has been paid to evaluating the forensic applicability of these technologies across diverse real-world scenarios. In this study, we present a unified retrieval framework adapted to four key forensic tasks: (1) tattoo image retrieval given a tattoo query image; (2) tattoo retrieval guided by human-expert textual descriptions, modelling the common situation where a witness verbally describes a tattoo; (3) tattoo retrieval from hand-drawn sketches; and (4) face retrieval from forensic face sketches. Our system leverages a multimodal large language model (MLLM) to automatically generate structured textual descriptions for all queries and gallery images, followed by sentence-transformer embedding for text-based comparison. We evaluate retrieval using visual-only embeddings, text-only embeddings and a multimodal fusion strategy that combines text- and image-based similarity scores derived from state-of-the-art visual feature extractors relevant to each task. The fusion of modalities consistently improves retrieval precision and robustness, especially in scenarios where visual information is limited or noisy (e.g., sketches, partial tattoos, or fragmented witness statements). This work highlights the forensic value of a unified multimodal retrieval pipeline and demonstrates how modern MLLMs can operationalize challenging forensic tasks that traditionally rely on manual expert analysis. Our results position multimodal retrieval as a promising tool for supporting investigative workflows involving tattoos, facial composites, and witness descriptions.

### 🤖 AI 总结

**一句话总结**：Automated image retrieval plays an increasingly critical role in modern forensic analysis, supporting investigative workflows that rely on efficient comparison of visual evidence. While prior work has...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bridging, Modality, Gap, Forensic, Image, Retrieval, Automated, plays

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12294v1) | [下载PDF](https://arxiv.org/pdf/2606.12294v1.pdf)

---

## [21. CellNet -- Localizing Cells using Sparse and Noisy Point Annotations](https://arxiv.org/abs/2606.12286v1)

**作者**：Benjamin Eckhardt, Dmytro Fishman, Stuart Fawke 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-10

### 📄 论文摘要

Counting living cells is an important step in many biological research workflows. Our collaborators at the Wellcome Sanger Institute study vital genes in humans via large scale saturation genome editing screening, which requires repeatedly counting cells a great number of times. Computer Vision based automation is crucial for high throughput and resource efficiency. In this work, we develop a regression-based deep learning computer vision algorithm to detect and count cells in phase-contrast microscopy images. To reduce annotation effort, which in practice often becomes a bottleneck, we focus on counting cells only using sparse point annotations, which are fast and easy to acquire. By comparison to state-of-the-art 0-shot methods, we show that regression-based counting is a promising alternative in low data regimes. Through developing methods to automatically count living cells in microscopy images, we contribute to valuable research on the human genome. The code is available at https://github.com/beijn/cellnet.

### 🤖 AI 总结

**一句话总结**：Counting living cells is an important step in many biological research workflows. Our collaborators at the Wellcome Sanger Institute study vital genes in humans via large scale saturation genome editi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CellNet, Localizing, Cells, Sparse, Noisy, Point, Annotations, Counting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12286v1) | [下载PDF](https://arxiv.org/pdf/2606.12286v1.pdf)

---

## [22. Finding Sparse Subnetworks in One Training Cycle via Progressive Magnitude-Based Pruning](https://arxiv.org/abs/2606.12278v1)

**作者**：Romana Qureshi, Hafida Benhidour, Said Kerrache 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-06-10

### 📄 论文摘要

Neural network pruning reduces model size by removing less important parameters while aiming to preserve predictive performance. Although the Lottery Ticket Hypothesis (LTH) shows that sparse subnetworks can match dense networks when trained from suitable initializations, its iterative pruning procedure requires multiple complete training cycles. This work evaluates progressive magnitude-based pruning as a single-cycle alternative. The method gradually increases sparsity during training using a linear schedule and updates pruning masks based on active weight magnitudes. We conduct systematic experiments on CIFAR-10 and MNIST across ResNet, VGG-style, and LeNet architectures, comparing the proposed method with representative iterative and initialization-based pruning baselines, including LTH, SNIP, and GraSP. On CIFAR-10, the method achieves 95.12\% accuracy on ResNet-18 at 72.9\% sparsity, compared with 90.5\% reported for LTH. At extreme sparsity, it achieves 93.13\% accuracy on a VGG-like architecture at 97\% sparsity, compared with approximately 92.0\% for SNIP, and 93.44\% accuracy on VGG-19 at 97.97\% sparsity, compared with 92.19\% for GraSP at 98\% sparsity. A sparsity-accuracy analysis on ResNet-18 further shows that accuracy remains within 0.1 percentage points of the dense baseline across 70--85\% sparsity. These results indicate that progressive magnitude-based pruning provides an effective single-cycle approach for neural network sparsification under the evaluated settings.

### 🤖 AI 总结

**一句话总结**：Neural network pruning reduces model size by removing less important parameters while aiming to preserve predictive performance. Although the Lottery Ticket Hypothesis (LTH) shows that sparse subnetwo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Finding, Sparse, Subnetworks, One, Training, Cycle, via, Progressive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12278v1) | [下载PDF](https://arxiv.org/pdf/2606.12278v1.pdf)

---

## [23. VOID: Defeating Unauthorized Mimicry in Latent Diffusion Models](https://arxiv.org/abs/2606.12263v1)

**作者**：Chunlin Qiu, Ang Li, Tianxiao Huang 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-10

### 📄 论文摘要

While Latent Diffusion Models (LDMs) have revolutionized visual synthesis, they are increasingly exploited for unauthorized mimicry of individuals. Existing defenses inject deceptive perturbations to steer the generated images toward irrelevant targets. However, this approach hinges on an ungrounded assumption: subtle perturbations can maintain their deceptive efficacy throughout an LDM's extensive generation process. In reality, the model's innate restoration mechanism will remove such perturbations and cause individual identities to re-emerge in the images generated.   We propose VOID, a defense framework that overcomes this conundrum by manipulating an LDM's intrinsic stochasticity. VOID perturbs the diffusion pipeline in two novel ways: 1) amplifying the latent encoding errors to shatter an image's semantic structure, and 2) counteracting the target guidance signals to suppress the model's restoration capabilities. This results in a semantic corruption that thwarts any unauthorized mimicry. Notably, the security gain does not come at the price of visual utility, as VOID simultaneously manages to confine perturbations to human-imperceptible regions of protected images. Our comprehensive evaluation of 24 state-of-the-art defenses against 10 mimicry attacks on 5 datasets demonstrates VOID's unprecedented protection power: it increases the average Frechet Inception Distance (FID) from 113 to 365, a 223% improvement over the strongest defense to date.

### 🤖 AI 总结

**一句话总结**：While Latent Diffusion Models (LDMs) have revolutionized visual synthesis, they are increasingly exploited for unauthorized mimicry of individuals. Existing defenses inject deceptive perturbations to ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, VOID, Defeating, Unauthorized, Mimicry, Latent, Models, While

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12263v1) | [下载PDF](https://arxiv.org/pdf/2606.12263v1.pdf)

---

## cs.LG

## [24. ATLAS: Active Theory Learning for Automated Science](https://arxiv.org/abs/2606.12386v1)

**作者**：Noémi Éltető, Nathaniel D. Daw, Kimberly L. Stachenfeld 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-10

### 📄 论文摘要

Advancing scientific understanding through mechanistic modeling requires posing the right experimental questions to yield maximally informative data. To automate this pursuit within cognitive science, we introduce ATLAS (Active Theory Learning for Automated Science), an active learning framework for the data-driven discovery of interpretable behavioral models. ATLAS iterates between generating mechanistic hypotheses--instantiated as a diverse ensemble of sparse neural networks (Disentangled RNNs)--and designing experiments that optimally distinguish between them. We test this approach on the problem of recovering reinforcement learning agents from their behavior in bandit tasks. ATLAS designs varied sequences of qualitatively novel experiments with temporal structure tailored to underlying agent characteristics. The models trained on these experiments are evaluated against a comprehensive set of metrics for mechanistic modeling that capture behavioral, structural, and computational similarity. ATLAS achieves a 5-10x improvement in sample efficiency across all metrics compared to random experimentation, and its performance is further validated against expert-designed experiments derived from literature. These in silico results showcase ATLAS's potential to accelerate human-interpretable insights in cognitive science and other domains where scientific inquiry relies on discovering mechanistic models.

### 🤖 AI 总结

**一句话总结**：Advancing scientific understanding through mechanistic modeling requires posing the right experimental questions to yield maximally informative data. To automate this pursuit within cognitive science,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ATLAS, Active, Theory, Learning, Automated, Science, Advancing, scientific

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12386v1) | [下载PDF](https://arxiv.org/pdf/2606.12386v1.pdf)

---

## [25. On Subquadratic Architectures: From Applications to Principles](https://arxiv.org/abs/2606.12364v1)

**作者**：Anamaria-Roberta Hartl, Levente Zólyomi, David Stap 等 9 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-10

### 📄 论文摘要

Transformers dominate modern sequence modeling, but their quadratic attention incurs substantial computational cost. Subquadratic architectures offer a scalable alternative. However, it remains unclear which designs yield the most effective sequence models. We compare three leading approaches: xLSTM, Mamba-2, and Gated DeltaNet. We evaluate these models on tasks with complex dependencies: (1) code-model pre-training, (2) distillation of code models from large language models, and (3) pre-training of time-series foundation models. Across these settings, xLSTM delivers the strongest overall performance. To explain xLSTM's advantage, we present a unified formulation and analyze the underlying architectural mechanisms, focusing on state tracking and memory dynamics. Our results show that xLSTM enables more flexible and stable memory correction via its gating scheme. We corroborate these findings on controlled synthetic length-generalization tasks. Overall, our findings indicate that xLSTM's gains on complex tasks stem from robust state tracking and accumulation.

### 🤖 AI 总结

**一句话总结**：Transformers dominate modern sequence modeling, but their quadratic attention incurs substantial computational cost. Subquadratic architectures offer a scalable alternative. However, it remains unclea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Subquadratic, Architectures, Applications, Principles, Transformers, dominate, modern, sequence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12364v1) | [下载PDF](https://arxiv.org/pdf/2606.12364v1.pdf)

---

## [26. Latent World Recovery for Multimodal Learning with Missing Modalities](https://arxiv.org/abs/2606.12362v1)

**作者**：Hui Wang, Tianyu Ren, Joseph Butler 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-10

### 📄 论文摘要

We study multimodal learning under missing modalities, with particular motivation from bioscience applications in which heterogeneous modalities are often only partially available when decisions need to be made. We propose Latent World Recovery (LWR), a framework built on two key ideas: (i) modality-specific embeddings from different modalities are aligned in a shared latent space, and (ii) a unified representation is constructed by fusing only the embeddings of the modalities that are actually available at both training and inference time. Rather than imputing missing modalities or requiring a fixed modality set, LWR treats each modality as a partial perception of an underlying latent state and performs availability-aware representation learning directly from the observed modalities. This combination of neighbor-based latent alignment and availability-aware modality fusion enables robust multimodal prediction under partial observation, while avoiding error propagation from explicit reconstruction of missing modalities. We evaluate the proposed framework on real-world incomplete multi-omics benchmarks and demonstrate that it provides an effective approach to downstream tasks such as cancer phenotype classification and survival prediction.

### 🤖 AI 总结

**一句话总结**：We study multimodal learning under missing modalities, with particular motivation from bioscience applications in which heterogeneous modalities are often only partially available when decisions need ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Latent, World, Recovery, Multimodal, Learning, Missing, Modalities

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12362v1) | [下载PDF](https://arxiv.org/pdf/2606.12362v1.pdf)

---

## [27. Anatomy of Post-Training: Using Interpretability to Characterize Data and Shape the Learning Signal](https://arxiv.org/abs/2606.12360v1)

**作者**：Leon Bergen, Usha Bhalla, Sidharth Baskaran 等 17 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-10

### 📄 论文摘要

Language-model post-training is the main stage at which model behavior is shaped, yet it still largely involves optimization of scalar rewards that summarize diverse desiderata. This abstraction gives practitioners little visibility into what their data actually teaches models, allowing spurious correlations to be learned by a model and inducing undesirable behaviors such as over-stylization and sycophancy. To address this problem, we ask: can we inspect a preference dataset before optimization and decide, at the level of concepts, which behaviors a model should be allowed to learn? Motivated by this, we introduce a data-centric post-training pipeline that uses interpretability protocols to develop statistical hypotheses for the latent concepts separating preferred from dispreferred generations, making them explicit for fine-grained user feedback. Building on this view, we unify several interpretability-based training protocols as ways of shaping rewards via feature or data interventions. Empirically, we show that our pipeline diagnoses undesirable signals in existing preference data, mitigates off-target learning, and can also help amplify or shape desired properties such as safeguards and model personality. More broadly, our results suggest that interpretability can turn post-training from optimizing opaque proxy rewards into a process of auditing and sculpting the learning signal itself.

### 🤖 AI 总结

**一句话总结**：Language-model post-training is the main stage at which model behavior is shaped, yet it still largely involves optimization of scalar rewards that summarize diverse desiderata. This abstraction gives...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Anatomy, Post-Training, Interpretability, Characterize, Data, Shape, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12360v1) | [下载PDF](https://arxiv.org/pdf/2606.12360v1.pdf)

---

## [28. Fourier Features Let Agents Learn High Precision Policies with Imitation Learning](https://arxiv.org/abs/2606.12334v1)

**作者**：Balázs Gyenes, Emiliyan Gospodinov, Jan Frieling 等 8 位作者  
**分类**：cs.LG, cs.RO  
**发布时间**：2026-06-10

### 📄 论文摘要

High-precision robotic manipulation requires fine-grained spatial reasoning that is often difficult to achieve with RGB-only policies due to depth ambiguity and perspective scale issues. Policies that leverage 3D information directly, such as those based on point clouds, offer a stronger geometric prior over purely image-based ones, yet their performance remains highly task-dependent. We hypothesize that this discrepancy may be due to the spectral bias of neural networks towards learning low frequency functions, which especially affects architectures conditioned on slow-moving Cartesian features. We thus propose to map point clouds from Cartesian space into high-dimensional Fourier space, effectively equipping the point cloud encoder with direct access to high-frequency features. We experimentally validate the use of Fourier features on challenging manipulation tasks from the RoboCasa and ManiSkill3 benchmarks and on a real robot setup. Despite their simplicity, we find that Fourier features provide significant benefits across diverse encoder architectures and benchmarks and are robust across hyperparameters. Our results indicate that Fourier features let policies leverage geometric details more effectively than Cartesian features, showing their potential as a general-purpose tool for point cloud-based imitation learning. We provide source code and videos on our project page: https://fourier-il.github.io/fourier-il

### 🤖 AI 总结

**一句话总结**：High-precision robotic manipulation requires fine-grained spatial reasoning that is often difficult to achieve with RGB-only policies due to depth ambiguity and perspective scale issues. Policies that...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Fourier, Features, Let, Learn, High, Precision, Policies

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12334v1) | [下载PDF](https://arxiv.org/pdf/2606.12334v1.pdf)

---

## [29. The Standard Interpretable Model: A general theory of interpretable machine learning to deductively design interpretable methods using Lagrangian mechanics](https://arxiv.org/abs/2606.12289v1)

**作者**：Pietro Barbiero, Giovanni De Felice, Mateo Espinosa Zarlenga 等 8 位作者  
**分类**：cs.LG, cs.AI, cs.NE  
**发布时间**：2026-06-10

### 📄 论文摘要

As Artificial Intelligence models grow in complexity, interpretability has become an indispensable tool for understanding, debugging, and controlling their computations. However, interpretability lacks general theories to deductively design interpretable methods. This gap between theories and methods results in a fragmented literature and inconsistent evaluation protocols.   To fill this gap, we introduce the Standard Interpretable Model (SIM), a general theory grounded in Lagrangian mechanics that enables the deductive design of interpretable methods. Specifically, the SIM summarises, in a set of premises, what interpretability is for a target user. From these premises, the SIM systematically derives interpretability symmetries and corresponding constraints, which shape the landscape of a Lagrangian whose minima correspond to optimal interpretable models. To reach the minima, one can either update the parameter values of an opaque model to make it more interpretable or compile constraints into an interpretable architecture.   We empirically show that the SIM identifies and solves limitations of existing methods (including traditional, concept-based, and mechanistic interpretability), highlights underexplored research directions, and informs the design of core programming interfaces. Beyond being a research method, the deductive nature of the SIM offers pedagogical grounding for interpretability curricula and may shift the scientific community's perspective of a discipline that has long been fragmented.

### 🤖 AI 总结

**一句话总结**：As Artificial Intelligence models grow in complexity, interpretability has become an indispensable tool for understanding, debugging, and controlling their computations. However, interpretability lack...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Standard, Interpretable, Model, general, theory, machine, learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12289v1) | [下载PDF](https://arxiv.org/pdf/2606.12289v1.pdf)

---

## [30. Finding Multiple Interpretations in Datasets](https://arxiv.org/abs/2606.12277v1)

**作者**：Matthew Chak, Paul Anderson  
**分类**：cs.LG  
**发布时间**：2026-06-10

### 📄 论文摘要

In this paper, we propose an approach to finding sets of similar-performing models (in terms of loss/accuracy measurements) with highly different context-aware characteristics. Through experiments on the METABRIC dataset, we show that the proposed method finds multiple models with highly different gene expressions than those found by the control methodology without performance penalties. We argue that the proposed methodology is important whenever one aims to analyze any global characteristic of a model to extract insight into the underlying phenomenon being studied.

### 🤖 AI 总结

**一句话总结**：In this paper, we propose an approach to finding sets of similar-performing models (in terms of loss/accuracy measurements) with highly different context-aware characteristics. Through experiments on ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：we, an, Finding, Multiple, Interpretations, Datasets, paper, propose

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.12277v1) | [下载PDF](https://arxiv.org/pdf/2606.12277v1.pdf)

---

