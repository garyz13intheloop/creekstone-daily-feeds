# arXiv AI 论文日报 | 2026-08-18

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (14 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.CL](#csCL) (3 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models](https://arxiv.org/abs/2608.16852v1)

**作者**：Saisab Sadhu, Aadit Sengupta, Vinay Kumar Sankarapu 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-17

### 📄 论文摘要

Regulatory compliance monitoring in deployed language models is increasingly implemented as a legal and audit control, checking model outputs against written rules spanning data protection, healthcare, financial regulation, and platform policy. Such monitoring is meaningful only if a detector's verdict depends on the stated rule rather than on surface features of the scenario. We show this condition fails across the current class of compliance detectors, a failure we call rule blindness. Deleting, permuting, or substituting the governing rule leaves detection accuracy unchanged for every guard and activation probe we test, including a policy-conditioned guard that correctly cites the governing clause yet barely changes its verdict when that clause is swapped for its permissive counterpart. A purpose-built benchmark crossing two rules with two scenarios, so that neither alone predicts the label, confirms the failure under a design no prior benchmark rules out, and shows that step by step reasoning, not any fast detector we test, is what escapes it. Auditing at scale requires a retraining-free detector, so we introduce the Internal Compliance Score (ICS): a training-free activation readout calibrated from ten labelled pairs and scored by a single projection. We hold ICS to the same scrutiny as the guards it audits: a pre-registered criterion for beating trivial baselines is not met, and a bag-of-words model matches its pooled generalisation exactly. It remains useful because it is inexpensive, letting us audit four deployed guard models, an 8B zero-shot judge, and thirteen benchmarks, and it raises the mechanically verified pass rate when used to rank candidate responses, though an adaptive white-box attack removes this gain. We release the counterfactual protocol and crossed-rule benchmark so rule blindness can be tested in future probe and guard claims.

### 🤖 AI 总结

**一句话总结**：Regulatory compliance monitoring in deployed language models is increasingly implemented as a legal and audit control, checking model outputs against written rules spanning data protection, healthcare...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, An, of, What, Compliance, Detectors, Read?, Audit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16852v1) | [下载PDF](https://arxiv.org/pdf/2608.16852v1.pdf)

---

## [2. Policy Iteration with Human Feedback: Bringing Post-Training RL to In-context Learning](https://arxiv.org/abs/2608.16831v1)

**作者**：Minh-Ha Nguyen, Cathy Shyr  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-08-17

### 📄 论文摘要

Generative pretraining established reusable task representations; later work on language-based task conditioning and in-context learning showed that a fixed model could adapt its behavior from instructions and demonstrations. Policy Iteration with Human Feedback (PIHF) builds on this development and the recurrent evaluate-and-improve structure of generalized policy iteration. PIHF uses a pretrained language model as its execution substrate and moves persistent revision to a versioned natural-language policy and tool set. A language-model critic and clinical expert review complete-panel reasoning and tool-use trajectories to localize recurrent failures and form candidate revisions; the expert may reinterpret the evidence and retains authority over admission and rollback, while Recall@1 and Recall@5 validate outcomes after candidate execution.   Across cumulative ablations and ultra-rare-disease benchmarks, a PIHF-derived policy improved Recall@1 in one proprietary executor and three open-weight executors spanning 3 to 49 billion active parameters. Gains were 32.7 percentage points for GPT-5.4 and 31.1 points for Qwen3.6-35B, a difference of 1.7 points. These results support the feasibility of using pretrained language models as fixed-weight execution substrates for expert-guided policy development in rare-disease diagnosis.

### 🤖 AI 总结

**一句话总结**：Generative pretraining established reusable task representations; later work on language-based task conditioning and in-context learning showed that a fixed model could adapt its behavior from instruc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Policy, Iteration, Human, Feedback, Bringing, Post-Training, In-context

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16831v1) | [下载PDF](https://arxiv.org/pdf/2608.16831v1.pdf)

---

## [3. Quipu: A Governed Bitemporal Knowledge Graph Store](https://arxiv.org/abs/2608.16813v1)

**作者**：Steve Brown  
**分类**：cs.AI, cs.DB  
**发布时间**：2026-08-17

### 📄 论文摘要

Agents now write knowledge graphs, but knowledge-graph stores still carry defaults set when humans curated them: accept writes now and clean later, keep one time axis or none, treat every writer's facts as equally trustworthy, and leave governance to dashboards and middleware. These four defaults are individually convenient and jointly untenable under agent workloads. We present Quipu, an embeddable store that inverts all four: no fact enters except through a gate whose predicates evaluate the pending post-state; data, trust labels, verdicts, and the rules themselves are bitemporal; named graphs are the unit of authority and trust, composed under a lattice whose one invariant is that composition never widens; and the governance specification $Σ$, the trace, and signed verdicts are facts in the store they govern, making the audit $T \models Σ$ a query. We evaluate with Census, a deterministic multi-writer lifecycle whose single seeded run scores every research question against planted ground truth: the gated store ends with 0 of 6 planted defects versus 6 of 6 ungated; all 7 composition probes uphold the lattice contract; 50 of 50 satisfied verdicts re-derive faithfully as of their instant while all 50 would be misreported under a latest-only rule set; and the SARC reference checker agrees with the in-store audit verdict-for-verdict, differing only on coverage semantics. A recorded trace from a governed writer surfaces a live enforcement gap the audit names with its remediation. On DEMM-Bench, an external decision-evidence sufficiency benchmark, a content-only reading of the exported records answers all 512 property-level governance questions correctly with zero overclaim under all eight degradation conditions, while container-presence baselines overclaim on up to 87.5% of them -- and the run surfaced, and led us to close, a gap in what a denial's verdict attests.

### 🤖 AI 总结

**一句话总结**：Agents now write knowledge graphs, but knowledge-graph stores still carry defaults set when humans curated them: accept writes now and clean later, keep one time axis or none, treat every writer's fac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Quipu, Governed, Bitemporal, Knowledge, Graph, Store, now

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16813v1) | [下载PDF](https://arxiv.org/pdf/2608.16813v1.pdf)

---

## [4. Cross-Sign Language Transfer Learning Using Domain Adaptation with Multi-scale Temporal Alignment](https://arxiv.org/abs/2608.16804v1)

**作者**：Keren Artiaga, Yang Li, Ercan Engin Kuruoglu 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-17

### 📄 论文摘要

Sign language serves as a vital means of communication for individuals with hearing impairments, yet recognition resources for the over 100 distinct sign languages are severely lacking. In response, we present our work on sign language recognition using transfer learning and the domain adaptation method TA3N, which utilizes the Temporal Relational Network (TRN) module for aligning multi-scale temporal relations. Our findings highlight the superior performance of Domain Adaptation to neural network-based transfer learning, particularly in improving recognition of American Sign Language (ASL). Our research also identifies the effectiveness of aligning shorter-term temporal features between source and target domains. In addition to using RGB, we conducted experiments using Optical Flow mode for the sign language samples, ultimately determining that RGB outperforms Optical Flow in the majority of cases. Our work aims to improve accessibility and communication for individuals who rely on sign language as their primary mode of communication.

### 🤖 AI 总结

**一句话总结**：Sign language serves as a vital means of communication for individuals with hearing impairments, yet recognition resources for the over 100 distinct sign languages are severely lacking. In response, w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Cross-Sign, Language, Transfer, Learning, Domain, Adaptation, Multi-scale, Temporal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16804v1) | [下载PDF](https://arxiv.org/pdf/2608.16804v1.pdf)

---

## [5. GRIP: Grounded Reasoning via Information-Restricted Premises](https://arxiv.org/abs/2608.16776v1)

**作者**：Lirui Teng  
**分类**：cs.AI  
**发布时间**：2026-08-17

### 📄 论文摘要

High-capacity encoders in retrieval-augmented generation (RAG) can let the query dominate the latent state, leaving retrieved evidence functionally irrelevant. We call this failure mode query dominance. To address it, we introduce \textbf{GRIP} (Grounded Reasoning via Information-Restricted Premises), which imposes capacity asymmetry: the decoder keeps full-dimensional access to the query, while retrieved evidence passes through a severe stochastic bottleneck. This forces the evidence channel to encode only the residual information unavailable from the query. Across five reasoning benchmarks, GRIP outperforms strong iterative baselines, cuts a query--latent mutual-information diagnostic by roughly 30$\times$ (14.8 $\to$ 0.47 bits), and reduces hallucination by 73\%. Residual-alignment analysis further shows that the bottleneck output occupies subspaces less aligned with the query than baseline representations.

### 🤖 AI 总结

**一句话总结**：High-capacity encoders in retrieval-augmented generation (RAG) can let the query dominate the latent state, leaving retrieved evidence functionally irrelevant. We call this failure mode query dominanc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GRIP, Grounded, Reasoning, via, Information-Restricted, Premises, High-capacity, encoders

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16776v1) | [下载PDF](https://arxiv.org/pdf/2608.16776v1.pdf)

---

## cs.CL

## [6. Towards Computational Provenance: Carrying Causal-State Evidence in Generated Text](https://arxiv.org/abs/2608.16868v1)

**作者**：Benjamin Belay  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-17

### 📄 论文摘要

A language model's output does not by itself provide verifiable evidence about the internal computation that produced it. We study computational provenance: whether generated text can carry detectable evidence of which causally relevant internal state occurred. We test a bounded form of this idea in two controlled architectures: a modular feed-forward neural network and a transformer-based model. Both architectures are trained on the same arithmetic task with a mandatory pathway through two discrete intermediate states, allowing different internal paths to produce the same answer. We deliberately switch between these paths, authenticate the state actually used, and let that verified state determine a subtle statistical pattern in the generated text that can later be detected. The feed-forward and transformer systems each passed all 128 matched pairs in both their public and separately sealed protected end-to-end evaluations, with the detector recovering the signal associated with the authenticated internal state. The required causal computation also reproduced across five independently trained feed-forward models and three independently trained transformers. In a separate answer-only transformer experiment, our linear probes did not recover a naturally learned intermediate state. These results provide a controlled proof of concept that information about a verified, causally relevant internal state can be preserved in generated text even when the answer is unchanged.

### 🤖 AI 总结

**一句话总结**：A language model's output does not by itself provide verifiable evidence about the internal computation that produced it. We study computational provenance: whether generated text can carry detectable...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Towards, Computational, Provenance, Carrying, Causal-State, Evidence, Generated, Text

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16868v1) | [下载PDF](https://arxiv.org/pdf/2608.16868v1.pdf)

---

## [7. Model Hypnosis: Strong control of AI via additive subliminal effects](https://arxiv.org/abs/2608.16834v1)

**作者**：Enric Boix-Adsera, Benedict Tessler  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-17

### 📄 论文摘要

We demonstrate that AI models are broadly susceptible to a phenomenon we call model hypnosis, in which individually weak and seemingly irrelevant cues in the prompt can be systematically combined to strongly control model behavior. Model hypnosis occurs across model families and scales, including in frontier reasoning models, and hypnotic prompts can transfer between models. Because the model is controlled by inconspicuous textual choices, such as paraphrases and typos, model hypnosis presents new challenges and avenues for AI safety, and is a major hurdle for AI interpretability.

### 🤖 AI 总结

**一句话总结**：We demonstrate that AI models are broadly susceptible to a phenomenon we call model hypnosis, in which individually weak and seemingly irrelevant cues in the prompt can be systematically combined to s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Model, Hypnosis, Strong, control, via, additive, subliminal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16834v1) | [下载PDF](https://arxiv.org/pdf/2608.16834v1.pdf)

---

## [8. ClawGym II: Exploring Black-Box RL on Agent Harness](https://arxiv.org/abs/2608.16798v1)

**作者**：Huatong Song, Fei Bai, Ming Yang 等 20 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-08-17

### 📄 论文摘要

Agent harnesses have substantially improved performance on long-horizon tasks by coordinating agent interactions with the environment. However, reinforcement learning through complex harnesses remains largely unexplored, as scaling such training to long-horizon agent tasks introduces fundamental challenges. In this work, we present a unified black-box RL framework for stable and scalable optimization of general agents through complex harnesses. Concretely, we first build a sandbox-based execution infrastructure that isolates task environments and harnesses within temporary sandboxes for large-scale concurrent rollouts. We then decouple policy optimization from opaque harness execution and place a serving proxy at the model boundary to capture model calls. To reconstruct multi-turn trajectories and improve training efficiency, we organize the captured calls into prefix trees and further adapt both critic-based PPO and critic-free GRPO to optimize over the recovered tree structure. Meanwhile, we maintain training-inference consistency throughout the optimization process. Finally, we introduce mix-harness training, allowing a single model to be jointly optimized by heterogeneous harnesses. With Qwen3-30A3B, black-box RL improves Pass@1 on ClawGym-Bench by 9.98 and 14.81 points through OpenClaw and Claude Code, respectively, while remaining stable over 200-400 optimization steps. Moreover, the framework yields consistent gains on more challenging tasks such as JobBench and OfficeQA. Overall, our framework enables effective, stable, and scalable optimization of general agents through black-box harnesses, supporting unified training across heterogeneous execution systems.

### 🤖 AI 总结

**一句话总结**：Agent harnesses have substantially improved performance on long-horizon tasks by coordinating agent interactions with the environment. However, reinforcement learning through complex harnesses remains...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：II, RL, Agent, ClawGym, Exploring, Black-Box, Harness, harnesses

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16798v1) | [下载PDF](https://arxiv.org/pdf/2608.16798v1.pdf)

---

## cs.CV

## [9. An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models](https://arxiv.org/abs/2608.16887v1)

**作者**：Dengyang Jiang, Ruoyi Du, Zhennan Chen 等 13 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-17

### 📄 论文摘要

This paper investigates an increasingly important topic in generative modeling: pixel-space diffusion models. Although numerous studies have explored this topic, most focus on small-scale or class-conditional settings. Consequently, a practical recipe for training pixel-space models that rival or exceed well-established latent-space counterparts remains elusive. Through a comprehensive empirical study, we first observe that direct large-scale pre-training in pixel space converges substantially more slowly than in latent space. This observation motivates a latent-to-pixel strategy that acquires generative priors efficiently in latent space and transitions to pixel space during post-training. We then systematically investigate the key design choices governing this transition, including weight initialization, data composition, prediction target, decoder architecture, and noise schedule, and identify a practical recipe that makes the resulting pixel-space models match or outperform their latent-space counterparts while delivering 3.18 to 4.75 times end-to-end inference speedups. We hope that our findings provide useful empirical insights and practical guidelines for future research on pixel-space generation.

### 🤖 AI 总结

**一句话总结**：This paper investigates an increasingly important topic in generative modeling: pixel-space diffusion models. Although numerous studies have explored this topic, most focus on small-scale or class-con...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, of, Diffusion, Empirical, Study, Training, Pixel-Space, Text-to-Image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16887v1) | [下载PDF](https://arxiv.org/pdf/2608.16887v1.pdf)

---

## [10. HarnessEval-W: Agentifying the Evaluation of Visual Worlds](https://arxiv.org/abs/2608.16859v1)

**作者**：Weiliang Chen, Haowen Sun, Jun Gao 等 43 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-17

### 📄 论文摘要

A benchmark should deliver more than a scalar score: what makes an evaluation trustworthy is the reasoning that justifies the score. This is especially critical for world models, where judging a rollout requires understanding whether physics, causality, and world state evolve correctly. Humans spot such violations naturally, yet no existing benchmark automates this capability: metrics are computed brute-force, leaving no reasoning chain that can be examined or verified. We introduce HarnessEval-W, an agentified evaluation pipeline that brings the harness paradigm from the LLM ecosystem to world model benchmarking. Rather than applying a fixed rubric, HarnessEval-W interprets the context of each evaluation case, decomposes the evaluation question into measurable subproblems, and spawns specialized sub-agents, each equipped with tailored context and diagnostic tools to reason over its own subproblem. The parent agent then validates the gathered evidence and summarizes it into the final verdict. This hierarchical workflow turns every evaluation into a transparent evidence tree whose complete reasoning chain justifies the result. We apply HarnessEval-W to 18 representative world models over 330 evaluation cases. Its judgments closely align with human preferences while providing verifiable, fine-grained diagnoses of every generated rollout. We open-source the full pipeline as a live benchmark and invite the broad community to contribute to grow new skills and evaluation cases as world models evolve.

### 🤖 AI 总结

**一句话总结**：A benchmark should deliver more than a scalar score: what makes an evaluation trustworthy is the reasoning that justifies the score. This is especially critical for world models, where judging a rollo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, HarnessEval-W, Agentifying, Evaluation, Visual, Worlds, benchmark, should

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16859v1) | [下载PDF](https://arxiv.org/pdf/2608.16859v1.pdf)

---

## [11. Can Unsupervised Methods Outperform Supervised Deep Learning When Ground Truth Is Sparse? A Case Study of Bronchovascular Bundle Segmentation in Low-Dose CT](https://arxiv.org/abs/2608.16855v1)

**作者**：Anna Mrukwa, Marek Socha, Aleksandra Suwalska 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-17

### 📄 论文摘要

Background   Lung cancer remains the deadliest cancer worldwide because it is often diagnosed too late. Effective treatment depends on detection at an early screening stage. However, the growing number of patients and the limited number of radiologists lead to prolonged diagnostic waiting times. In very early stage lung cancer, nodule visibility is further reduced by adjacent blood vessels and airway walls, because nodules are often connected to or supplied by these structures. Task-specific analysis of the bronchovascular bundle is therefore important for efficient nodule detection, and its removal can increase the diagnostic potential of lung cancer screening.   Materials and Methods   To assess the efficacy of the proposed method, we used series from widely utilized LDCT datasets, including the Duke Lung Cancer Screening (DLCS) dataset and the Pilot Pomeranian Lung Cancer Screening Program. The proposed bronchovascular bundle segmentation pipeline, RONALD, operates on computed tomography images and returns binary masks of vessels and bronchi located in the lung parenchyma. The method includes a preprocessing stage with lung, lobe, and mediastinum segmentation, followed by separate vessel and bronchial tree segmentation.   Results   The proposed pipeline segmented the bronchovascular bundle in low-dose computed tomography scans while improving nodule retention compared with other segmentation methods: from 93.98% and 90.36% to 100% in DLCS, and from 83.16% and 62.36% to 99.92% in the Pomeranian dataset.   Conclusion   The resulting segmentations can improve lung nodule detection in the very early stages of lung cancer.

### 🤖 AI 总结

**一句话总结**：Background   Lung cancer remains the deadliest cancer worldwide because it is often diagnosed too late. Effective treatment depends on detection at an early screening stage. However, the growing numbe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Can, Unsupervised, Methods, Outperform, Supervised, Deep, Learning, When

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16855v1) | [下载PDF](https://arxiv.org/pdf/2608.16855v1.pdf)

---

## [12. Unlocking the Potential of Image Editing via Concept Scaling and Dense Supervision](https://arxiv.org/abs/2608.16812v1)

**作者**：Long Cui, Xiaoqian Liu, Qi Qin 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-17

### 📄 论文摘要

Existing image editing frameworks predominantly follow the training paradigm of text-to-image diffusion models. However, extending this paradigm to image editing highlights two inherent discrepancies, specifically, the insufficient attention to edit concept granularity and the training inefficiency caused by sparse supervision signals. To address these issues, we establish a comprehensive hierarchical taxonomy featuring over 1,000 fine-grained edit concepts and build ConceptEdit-12M, a massive dataset of 12 million high-quality editing pairs via an improved synthesis framework. This library-driven approach effectively rectifies the distribution collapse of generated data while ensuring high data fidelity. Furthermore, we propose a dense supervision training strategy that synthesizes multiple non-interfering concepts into single image pairs. By providing richer learning signals, this strategy significantly enhances both training efficiency and overall model performance. Training results validate our strategy, significantly outperforming prior works. Finally, we present ConceptEdit-Bench, a granular evaluation suite designed to diagnose model capabilities across a vast array of real-world scenarios.

### 🤖 AI 总结

**一句话总结**：Existing image editing frameworks predominantly follow the training paradigm of text-to-image diffusion models. However, extending this paradigm to image editing highlights two inherent discrepancies,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Unlocking, Potential, Image, Editing, via, Concept, Scaling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16812v1) | [下载PDF](https://arxiv.org/pdf/2608.16812v1.pdf)

---

## [13. Unsupervised Learning of Cell Instances with Generative Routing Pyramids](https://arxiv.org/abs/2608.16810v1)

**作者**：Ziwen Liu, Martin Weigert  
**分类**：cs.CV, cs.LG, q-bio.QM  
**发布时间**：2026-08-17

### 📄 论文摘要

Identifying and representing object instances such as cells or nuclei is a common task in microscopy image analysis. Established machine learning workflows typically use supervised detection or segmentation followed by feature extraction or classification, which requires manual annotations and treats instance segmentation and cell representation as separate stages. We describe a new unsupervised method for cell instance segmentation and phenotypic classification from unlabeled microscopy images. Our method is based on reconstructing each image using a coarse-to-fine routing pyramid that associates pixels with spatially sparse latent sources. The resulting pixel-to-latent associations yield instance masks, while the source latents encode cell morphology. We demonstrate competitive performance in instance segmentation across diverse cell morphologies and imaging modalities, as well as generative modeling of cellular phenotypes under perturbations. Source code and checkpoints are available at https://github.com/weigertlab/routing-pyramids.

### 🤖 AI 总结

**一句话总结**：Identifying and representing object instances such as cells or nuclei is a common task in microscopy image analysis. Established machine learning workflows typically use supervised detection or segmen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Unsupervised, Learning, Cell, Instances, Generative, Routing, Pyramids

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16810v1) | [下载PDF](https://arxiv.org/pdf/2608.16810v1.pdf)

---

## [14. Diagnosing Dense Same-Class Attribute Misbinding in Large Vision-Language Models](https://arxiv.org/abs/2608.16805v1)

**作者**：Yuanzhi Xu, Qian Gao, Jun Fan 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-17

### 📄 论文摘要

Large vision-language models can recognize the objects and attributes in a crowded scene yet assign an attribute to the wrong same-class instance. Generic visual-question-answering accuracy marks the response as wrong, while object-hallucination metrics may regard both the object and attribute as image-supported; neither reveals the transfer. This study formalizes this blind spot as Dense Same-Class Attribute Misbinding (DSCAM) and presents InstaBind-Lite, a controlled benchmark that makes it directly measurable. Its 524 images contain 529 curated groups of 3-6 same-class entities, 1773 boxed instances, ordered neighbors, distinguishable color-like attributes, and four complementary question levels, yielding 9580 deterministically evaluated questions. Unlike existing protocols, source-instance annotations separate unsupported generation and recognition failure from an attribute copied from another visible entity. Binding-specific metrics further quantify transfer frequency, adjacency, ordinal distance, and intervention effects. Across five open-source and two commercial/API models, the open-source systems average 19.84% Misbinding Rate and the API systems 7.55%; these errors are hidden by aggregate accuracy. Among identifiable transfers, 80.70% and 81.51%, respectively, originate from adjacent instances. Localization and instance-first interventions help selected models but are not universal remedies. InstaBind-Lite therefore turns previously undifferentiated wrong answers into source-identifiable failure categories and tests a reliability dimension that conventional benchmarks cannot determine: whether a model knows not only what is visible, but which instance owns each attribute.

### 🤖 AI 总结

**一句话总结**：Large vision-language models can recognize the objects and attributes in a crowded scene yet assign an attribute to the wrong same-class instance. Generic visual-question-answering accuracy marks the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diagnosing, Dense, Same-Class, Attribute, Misbinding, Large, Vision-Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16805v1) | [下载PDF](https://arxiv.org/pdf/2608.16805v1.pdf)

---

## [15. Steering the Flow: Inverting Face Recognition Models via Gradient-Guided Flow Matching](https://arxiv.org/abs/2608.16791v1)

**作者**：Ye Lu, Shen Wang, Zhaoyang Zhang 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.CR, cs.MM  
**发布时间**：2026-08-17

### 📄 论文摘要

Model Inversion Attacks (MIAs) aim to reconstruct representative training samples of target identities from face recognition models, exposing critical security vulnerabilities. Existing methods typically rely on indirect guidance or highly stochastic guidance, making it difficult to stably optimize generation trajectories toward target facial images. In this paper, we propose Steering Flow Model Inversion (SFMI), a novel two-stage white-box model inversion method that reformulates inversion as a trajectory-steering task. Specifically, Step I, Learning a Generic Flow Matching Prior, pre-trains a generic unconditional Flow Matching model to encode the manifold of human faces as a robust prior. Step II, Attacking with Progressive Guidance Scheduler (PGS), injects time-dependent target-specific gradients during sampling. By backpropagating through the target model to obtain gradients from intermediate generated states, PGS progressively injects adaptive guidance signals into the vector field. This process effectively steers the current generative flow from random noise toward the high-density regions of the target class. Under an identity-disjoint cross-evaluation setting using the CelebA dataset, SFMI achieves an ACC of 0.9248, an FID of 22.61, and an LPIPS of 0.3874 on the ArcFace target. Extensive experiments on multiple target models demonstrate that SFMI achieves competitive state-of-the-art performance in attack success and visual fidelity under the evaluated white-box protocol.

### 🤖 AI 总结

**一句话总结**：Model Inversion Attacks (MIAs) aim to reconstruct representative training samples of target identities from face recognition models, exposing critical security vulnerabilities. Existing methods typica...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Steering, Flow, Inverting, Face, Recognition, Models, via, Gradient-Guided

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16791v1) | [下载PDF](https://arxiv.org/pdf/2608.16791v1.pdf)

---

## [16. Revisiting Classifier-Free Guidance Methods in Latent Diffusion Models](https://arxiv.org/abs/2608.16786v1)

**作者**：Artem Sergievskii, Artyom Turevich, Sergey Kastryulin  
**分类**：cs.CV  
**发布时间**：2026-08-17

### 📄 论文摘要

Inference-time quality-enhancement methods are an effective and widely adopted means of improving diffusion models without expensive retraining. We study a family of training-free techniques conceptually rooted in Classifier-Free Guidance (CFG), most of which were originally proposed on older U-Net diffusion models and validated using metrics that assess image quality in isolation, without accounting for compositional alignment or semantic correspondence between the generated image and its associated text prompt. We re-evaluate eight such methods on two open-weight rectified-flow transformers under a fixed per-model protocol and three compositional-alignment benchmarks. No method consistently improves on CFG across the measured criteria. APG obtains several nominal best scores, but the corresponding gains often remain within the estimated evaluation uncertainty. Attention-perturbation methods provide isolated gains on SD3.5 Medium and more frequent degradations on FLUX.2 [klein] 4B Base, while CFG remains a competitive lower-cost baseline.

### 🤖 AI 总结

**一句话总结**：Inference-time quality-enhancement methods are an effective and widely adopted means of improving diffusion models without expensive retraining. We study a family of training-free techniques conceptua...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Revisiting, Classifier-Free, Guidance, Methods, Latent, Models, Inference-time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16786v1) | [下载PDF](https://arxiv.org/pdf/2608.16786v1.pdf)

---

## [17. Calibration-Free Vehicle Speed Estimation: A Monocular Keypoint-Template Approach](https://arxiv.org/abs/2608.16785v1)

**作者**：Gaofeng Su, Keya Li, Raja Sengupta 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-17

### 📄 论文摘要

This paper proposes a calibration-free framework for reliably and effectively estimating vehicle speeds from monocular videos, without relying on roadway features, camera calibration, or roadway-feature-based reference objects. The proposed framework estimates vehicle speeds using a 36-keypoint vehicle template and a homography matrix updated at each frame. A YOLO-based keypoint detection module is trained on diverse datasets, and two estimation strategies are compared: keypoint-only tracking and warped optical flow with dense spatial aggregation. Speed is estimated by projecting displacements into metric space using the homography, with validation conducted on over 400 video clips from roadside and overhead datasets, covering speeds from 30 to 100 mph. The method achieves reliable speed estimation on the VS13 and BrnoCompSpeed datasets, with the warped optical flow method delivering MAEs of 15.0% and 9.7%, respectively, and 77.9% and 93.1% of estimates falling within +/-20% error. After applying a 10% trim to remove edge-of-frame outliers, performance improves to MAEs of 11.7% and 7.6%, with within-+/-20% accuracy increasing to 85.3% and 95.4%. This work addresses key limitations of existing vision-based approaches and enables low-cost and efficient speed enforcement using portable devices such as dashcams and smartphones, thereby supporting citizen-based enforcement programs for traffic safety.

### 🤖 AI 总结

**一句话总结**：This paper proposes a calibration-free framework for reliably and effectively estimating vehicle speeds from monocular videos, without relying on roadway features, camera calibration, or roadway-featu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Calibration-Free, Vehicle, Speed, Estimation, Monocular, Keypoint-Template, Approach, paper

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16785v1) | [下载PDF](https://arxiv.org/pdf/2608.16785v1.pdf)

---

## [18. TRACE-Bench: Decomposing and Diagnosing Multi-Reference Image Generation](https://arxiv.org/abs/2608.16765v1)

**作者**：Haoran Wang, Chaofan Ma, Ran Yi 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-17

### 📄 论文摘要

Despite recent advances in unified multimodal models for multi-reference image generation, existing benchmarks remain organized around predefined task types (e.g., "subject composition"), which are ill-suited to this combinatorial setting and lead to fragmented coverage, uncontrolled complexity, and little diagnostic value. Recognizing that diverse multi-reference tasks share a common set of atomic operations, we adopt a capability-oriented perspective and formalize four operators: Anchor ($f$), Disentangle ($g$), Apply ($\oplus$), and Compose ($C$). Any multi-reference prompt can then be represented as a compositional formula over these operators, whose structural complexity is quantified by the number of operator slots. Building on this formulation, we construct TRACE-Bench, comprising approximately 1,600 evaluation cases across slot counts 1--8, built from 631 formula templates and around 4,000 reference images spanning diverse artistic styles and real-world subjects. The formula structure directly drives an operator-aligned evaluation protocol for per-capability scoring and a diagnostic tree analysis for recursive failure localization. Evaluating 9 leading models reveals insights invisible to holistic scoring: the primary bottleneck lies in disentanglement ($g$) and attribute binding ($\oplus$) rather than scene-level composition ($C$), with even the best model scoring only 0.74 on attribute fidelity. Project page: https://amuseum-whr.github.io/TraceBench

### 🤖 AI 总结

**一句话总结**：Despite recent advances in unified multimodal models for multi-reference image generation, existing benchmarks remain organized around predefined task types (e.g., "subject composition"), which are il...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TRACE-Bench, Decomposing, Diagnosing, Multi-Reference, Image, Generation, Despite, recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16765v1) | [下载PDF](https://arxiv.org/pdf/2608.16765v1.pdf)

---

## [19. Binarized High-Efficiency RAW Video Restoration and Beyond](https://arxiv.org/abs/2608.16756v1)

**作者**：Tianyu Zhu, Ying Fu, Hesong Li 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-17

### 📄 论文摘要

RAW video restoration is fundamental to high-quality low-level perception and serves as the basis for a wide range of downstream vision applications. While binary neural networks (BNNs) enable efficient lightweight deployment for image enhancement, their deficiencies in modeling temporal coherence and activation value distributions hinder their effectiveness when applied to video scenarios. In this paper, we propose BinRVR, a binarized RAW video restoration framework that reduces computation and parameters by approximately 96% while incurring only about 4% performance degradation. Specifically, we present a Binarized Information Interaction Module (BIIM) to jointly model spatial and temporal information in an efficient and unified manner. Moreover, we develop a Distribution-Aware Binarized Convolution (DAB-Conv) that leverages the statistics of full-precision activations to mitigate quantization errors. The proposed framework further supports multi-bit quantization, enabling flexible accuracy-efficiency trade-offs across different hardware constraints. Extensive experiments demonstrate that our BinRVR achieves competitive performance compared with state-of-the-art binarized methods on RAW video restoration tasks, including low-light enhancement, denoising, deblurring, and super-resolution. We further explore the potential of our method on downstream video applications, including object detection and monocular depth estimation.

### 🤖 AI 总结

**一句话总结**：RAW video restoration is fundamental to high-quality low-level perception and serves as the basis for a wide range of downstream vision applications. While binary neural networks (BNNs) enable efficie...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Binarized, High-Efficiency, RAW, Video, Restoration, Beyond, fundamental, high-quality

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16756v1) | [下载PDF](https://arxiv.org/pdf/2608.16756v1.pdf)

---

## [20. Beyond Uncertainty: Generalizable Failure Monitoring for Surgical Segmentation under Acquisition Degradation](https://arxiv.org/abs/2608.16748v1)

**作者**：Hieu D. Pham, Dang P. M. Cao, Thanh Trung Huynh  
**分类**：cs.CV  
**发布时间**：2026-08-17

### 📄 论文摘要

Surgical segmentation networks can fail silently under acquisition degradation: predicted masks may be wrong even when model confidence remains high. Existing deployment-time monitors rely primarily on uncertainty estimates and can therefore miss confident failures. We present TCSR-Monitor (Temporal Conformal Surgical Risk Monitor), a post-hoc failure-monitoring framework that combines confidence with observable shape, temporal-consistency, and image-quality cues. TCSR-Monitor wraps a frozen segmentation model, requires no model internals, and operates without ground truth at deployment. We also introduce a validation protocol to assess whether alarms remain credible under distribution shift. On EndoVis 2017, leave-one-corruption-out evaluation shows that TCSR-Monitor generalizes to unseen acquisition degradations and substantially outperforms confidence-based baselines. A circularity control confirms that it predicts segmentation failure rather than simply detecting corrupted images. Mondrian conformal calibration balances miss-rates across degradation severities, but a single global threshold still produces false alarms on up to 40% of correctly segmented frames at moderate corruption. Zero-shot transfer to SAM2 demonstrates feature portability, although entropy outperforms the transferred monitor at both evaluated thresholds. Overall, reliable monitoring under acquisition degradation benefits from complementary observable signals beyond confidence alone, but substantial false-alarm and transfer limitations remain.

### 🤖 AI 总结

**一句话总结**：Surgical segmentation networks can fail silently under acquisition degradation: predicted masks may be wrong even when model confidence remains high. Existing deployment-time monitors rely primarily o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Uncertainty, Generalizable, Failure, Monitoring, Surgical, Segmentation, under

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16748v1) | [下载PDF](https://arxiv.org/pdf/2608.16748v1.pdf)

---

## [21. Unsupervised Anomaly Detection for Image Dataset Quality Assurance in Multi-Center Breast MRI](https://arxiv.org/abs/2608.16725v1)

**作者**：Chiara Tappermann, Steffen Renisch, Lars Ole Schwen 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-17

### 📄 论文摘要

Corrupted, inconsistent, or anomalous data silently threatens the safety and reliability of medical AI. Despite growing regulatory recognition of dataset quality assurance (QA) for high-risk medical AI, scalable automated detection remains underdeveloped. We employ unsupervised anomaly detection (AD) and out-of-distribution (OOD) detection as an automated dataset QA mechanism for multi-center dynamic contrast-enhanced breast MRI.   We build a controlled AD benchmark of 17 realistic QA-relevant anomaly types from six public datasets (protocol violations, processing errors, incorrect anatomical regions) and propose a taxonomy of radiological image anomalies based on human visual perception, enabling fine-grained analysis of AD failure modes. The benchmark includes near-, medium-far-, far-OOD samples, as well as in-distribution and external normal data. Four methods are evaluated: a projection-based method extended with a domain-specific feature extractor and a novel positional encoding, a reconstruction-based approach extended to full 3D volumes with an augmented training objective, and two unmodified hybrid OOD detection methods.   Medium-far- and far-OOD samples are detected reliably, whereas near-OOD samples and external normal data from unseen institutions expose method-specific differences. The 3D reconstruction-based approach best balances detection performance (AUROC: 0.936) and generalization to unseen institutions. The projection-based method with positional encoding achieves the highest overall detection performance (AUROC: 0.954). Both hybrid methods exhibit critical failure modes, confirming that methods validated for one modality or anatomy may not generalize without domain-specific adaptation. Implants and mastectomies remain an open challenge for all methods. Our results establish a foundation and practical guidance on scalable unsupervised QA in medical AI pipelines.

### 🤖 AI 总结

**一句话总结**：Corrupted, inconsistent, or anomalous data silently threatens the safety and reliability of medical AI. Despite growing regulatory recognition of dataset quality assurance (QA) for high-risk medical A...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unsupervised, Anomaly, Detection, Image, Dataset, Quality, Assurance, Multi-Center

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16725v1) | [下载PDF](https://arxiv.org/pdf/2608.16725v1.pdf)

---

## [22. GenRouter: Unified Workflow Routing for Agentic Image Generation](https://arxiv.org/abs/2608.16721v1)

**作者**：Harold Haodong Chen, Zhiyu Hou, Wen-Jie Shu 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-17

### 📄 论文摘要

The rapid evolution of text-to-image (T2I) generation models has effectively solved the foundational challenge of raw pixel synthesis, shifting the community's focus toward fulfilling increasingly intricate user requests. While recent agentic image generation workflows enhance static inference with advanced capabilities like external knowledge retrieval and iterative reasoning, they mostly operate in isolated silos with fixed ``one-size-fits-all" topologies. This inevitably leads to severe compute-mismatch, where simple queries are forced through computationally heavy pipelines. To bridge this gap, we present GenRouter, the first unified workflow routing framework for agentic image generation. We first formulate GenCanvas, standardizing diverse agentic pipelines into a universal set of foundational primitives and executable templates. Operating over this unified space, GenRouter adaptively routes heterogeneous prompts to their optimal workflows via (i) demand profiling, (ii) experience matching, and (iii) Pareto filtering. Extensive experiments across diverse benchmarks demonstrate that GenRouter achieves superior visual alignment while reducing execution costs by over 95% and latency by 65% compared to heavyweight static pipelines. Furthermore, the system continuously self-evolves via accumulated experience, enabling robust zero-shot generalization that boosts performance and halves computational overhead.

### 🤖 AI 总结

**一句话总结**：The rapid evolution of text-to-image (T2I) generation models has effectively solved the foundational challenge of raw pixel synthesis, shifting the community's focus toward fulfilling increasingly int...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GenRouter, Unified, Workflow, Routing, Agentic, Image, Generation, rapid

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16721v1) | [下载PDF](https://arxiv.org/pdf/2608.16721v1.pdf)

---

## cs.LG

## [23. An Analytical-Prior Framework for Data-Efficient Prediction of Sound-Reduction Frequencies in Rectangular Side-Branch Helmholtz Resonators](https://arxiv.org/abs/2608.16873v1)

**作者**：Jiaming Li  
**分类**：cs.LG  
**发布时间**：2026-08-17

### 📄 论文摘要

High-fidelity finite-element simulations can provide accurate numerical predictions for side-branch resonators, but large simulation datasets are expensive to generate and purely data-driven surrogates may become unreliable when simulation-labelled data are scarce. This study develops an analytical-prior learning framework that reuses a low-cost analytical model to improve data efficiency under limited high-fidelity simulation budgets. Two complementary routes are considered. When the analytical model remains available at inference, it is retained as an explicit baseline and the simulation data are used to learn only the analytical-to-simulation discrepancy. When a self-contained predictor is required, the analytical mapping is first distilled from abundant low-cost evaluations into a learned prior and then calibrated with the limited simulation data. The framework is evaluated on rectangular side-branch Helmholtz resonators using 86 simulation-labelled geometries and 8,998 non-overlapping analytical-only geometries. The analytical model achieved a mean absolute error (MAE) of 1.333 Hz. Direct support vector regression (SVR) achieved 3.375 Hz, while residual SVR reduced the MAE to 0.426 Hz. A direct multilayer perceptron (MLP) achieved 1.109 Hz, whereas analytical-prior pretraining reduced the error to 0.556 Hz with frozen-prior residual adaptation and 0.371 Hz with full-model fine-tuning. Across training budgets of 20 to 70 simulation-labelled cases, both analytical correction and analytical-prior pretraining consistently improved data efficiency relative to direct learning. These results show that analytical prior information can substantially improve high-fidelity prediction when simulation data are scarce, with explicit correction and prior distillation serving complementary deployment needs.

### 🤖 AI 总结

**一句话总结**：High-fidelity finite-element simulations can provide accurate numerical predictions for side-branch resonators, but large simulation datasets are expensive to generate and purely data-driven surrogate...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, of, Analytical-Prior, Framework, Data-Efficient, Prediction, Sound-Reduction, Frequencies

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16873v1) | [下载PDF](https://arxiv.org/pdf/2608.16873v1.pdf)

---

## [24. Data-Efficient and Interpretable Classification of Circulating Tumor Cell Phenotypes in Microfluidic Devices via Deep Learning](https://arxiv.org/abs/2608.16870v1)

**作者**：Serena Su, Yifan Wang, Senwei Liang  
**分类**：cs.LG  
**发布时间**：2026-08-17

### 📄 论文摘要

Accurate classification of circulating tumor cell (CTC) phenotypes can provide valuable information for assessing metastatic potential. Label free microfluidic devices provide a hydrodynamic obstacle course that transforms subtle biophysical characteristics of CTCs, including size and deformability, into distinct kinematic trajectories. However, the highly nonlinear fluid structure interactions governing these trajectories make the inverse problem of inferring cellular phenotype from trajectory data analytically intractable. While deep neural networks (DNNs) have emerged as a powerful approach for addressing this inverse problem, their effectiveness is constrained by the limited availability of trajectory data and the lack of physical interpretability.   To address these challenges, we propose an interpretable and data efficient DNN framework for trajectory based CTC classification. To mitigate the scarcity of data, we develop Subsequence (SubSeq), a targeted augmentation strategy that randomly extracts informative local trajectory segments during training to promote learning from localized patterns. We further apply Gradient Weighted Class Activation Mapping to identify the trajectory features and physical regions of the microfluidic device that drive model predictions. Experimental results demonstrate that SubSeq improves classification accuracy over the evaluated baseline and augmentation methods. Furthermore, interpretability analysis suggests that localized trajectory segments contain substantial biophysical information relevant to accurate classification. This provides justification for SubSeq and also highlights the redundancy of full-length trajectories. More broadly, the proposed framework views microfluidic geometries as physical encoders of cellular mechanical properties, providing mechanistic insights that may inform the future design of diagnostic devices.

### 🤖 AI 总结

**一句话总结**：Accurate classification of circulating tumor cell (CTC) phenotypes can provide valuable information for assessing metastatic potential. Label free microfluidic devices provide a hydrodynamic obstacle ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Data-Efficient, Interpretable, Classification, Circulating, Tumor, Cell, Phenotypes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16870v1) | [下载PDF](https://arxiv.org/pdf/2608.16870v1.pdf)

---

## [25. Time-Aware Validation of Machine Learning Fuel Consumption Models: Evidence from 1\,Hz Operational Data, CCGS \textit{Sir Wilfrid Laurier}](https://arxiv.org/abs/2608.16833v1)

**作者**：Samarasimha Reddy Chittamuru, Ayhan Akinturk, Allison Kennedy 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-17

### 📄 论文摘要

Ship fuel consumption (SFC) prediction supports vessel operation optimisation, emissions estimation, and decision support systems (DSS) for sustainable maritime transportation. Numerous data-driven fuel models have been developed over the past two decades, but a critical and often overlooked limitation lies in their validation practices: most studies evaluate performance using random train--test splits, which, applied to high-frequency records, admit temporal leakage and yield optimistic results that do not reflect deployment conditions. This paper examines that gap using time-aware evaluation, specifically Time Series Cross-Validation (TSCV) and Blocked TSCV (BTSCV). Using the Canadian Coast Guard Ship (CCGS) \textit{Sir Wilfrid Laurier} as a case study, six regression models and a physics baseline are tuned under three time-aware schemes and three feature configurations, then evaluated on a common chronological hold-out set drawn from approximately 3.88 million steady-state 1\,Hz records.

### 🤖 AI 总结

**一句话总结**：Ship fuel consumption (SFC) prediction supports vessel operation optimisation, emissions estimation, and decision support systems (DSS) for sustainable maritime transportation. Numerous data-driven fu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Time-Aware, Validation, Machine, Learning, Fuel, Consumption, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16833v1) | [下载PDF](https://arxiv.org/pdf/2608.16833v1.pdf)

---

## [26. CaliBench: Are the Stochastic Dynamics of Video World Models Physically Calibrated?](https://arxiv.org/abs/2608.16829v1)

**作者**：Jonathan Sadeghi, Jenny Seidenschwarz, Jesse Allardice 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-17

### 📄 论文摘要

Video world models approximate the stochastic distribution of physical outcomes through generative sampling, but existing benchmarks score individual generations or compare distributions coarsely over a whole dataset, leaving the fine-grained aleatoric uncertainty of specific phenomena untested. We introduce CaliBench, which scores outcomes in a physically interpretable discrete space - a bin index, a die face, a suit, a colour - rather than a learned feature space such as in FID, so the distance from a known reference distribution is measured directly. We curate outcome spaces whose reference is known in closed form (binomial Galton boards, Bernoulli forks, uniform dice/cards/lottery, a skewed European-roulette colour), enabling an exact calibration test. We decompose performance into two orthogonal axes that a single accuracy metric conflates: scorability, the fraction of generations yielding a scoreable outcome, and calibration, the total variation distance from the reference on that sample. A chi-squared test assesses significance; as calibration is its null hypothesis it can evidence only miscalibration, and at N=32 per cell detects only large deviations. We apply it to nine scenes and six image-to-video models (WAN-2.7, SeeDance-2.0, HappyHorse-1.0, Veo 3.1, Runway Gen-4.5, Cosmos3-Super), 32 generations each. Models consistently concentrate probability mass on a few outcomes rather than reproducing the reference. Most scene-model combinations are significantly miscalibrated, in the extreme collapsing to one outcome, as Veo 3.1 does on dice. On roulette, generations often leave the ball ambiguously placed, giving several models low scorability. Performance varies by scene: no model dominates all nine. We release the protocol and a metric (mean normalised total variation, mnTV) for comparing new models against our results.

### 🤖 AI 总结

**一句话总结**：Video world models approximate the stochastic distribution of physical outcomes through generative sampling, but existing benchmarks score individual generations or compare distributions coarsely over...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, CaliBench, Stochastic, Dynamics, Video, World, Models, Physically

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16829v1) | [下载PDF](https://arxiv.org/pdf/2608.16829v1.pdf)

---

## [27. GEO-Flag: Detecting and Measuring GEO-Optimized Web Content](https://arxiv.org/abs/2608.16824v1)

**作者**：Junjie Chu, Ye Leng, Mingjie Li 等 6 位作者  
**分类**：cs.LG, cs.CR, cs.IR  
**发布时间**：2026-08-17

### 📄 论文摘要

Generative Engine Optimization (GEO) modifies web content to increase its likelihood of being selected and cited by generative search engines. This can give strategically optimized pages visibility disproportionate to their authority or relevance and even make weak or false information appear well supported. Unlike conventional search, generative search synthesizes information into direct answers rather than presenting competing sources, which can further amplify these risks, as assessing source provenance and authority requires additional user interaction. Despite these concerns, systematic methods for detecting GEO-optimized webpages remain underexplored. We introduce \texttt{GEOFlagBench}, a benchmark of 3,200 webpages spanning 400 queries, four domains, and eight GEO optimizer families, and use it to systematically evaluate existing GEO detection methods. Although the strongest baseline achieves an aggregate F1 of 0.880, method-level and authorship-conditioned evaluations reveal substantial weaknesses and potential reliance on authorship-related shortcuts. We therefore propose \emph{Intervention-Paired Training} (IPT), which supervises detector responses to GEO interventions and non-GEO AI polishing; on ModernBERT, IPT improves F1 from 0.862 to 0.944 and worst-group accuracy from 0.725 to 0.883. We develop a GEO-gated Agent system for auditing the Source Tier and verifiability of Citation URLs in detected GEO pages. Finally, we deploy the complete pipeline on released Google Search and Gemini-grounded retrieval results for 1,000 real-user queries. Across 10,095 available pages, we estimate an overall GEO prevalence of 8.90\%, reaching 16.36\% among pages modified in 2026. Our results establish a foundation for systematically detecting, auditing, and measuring GEO in real-world search ecosystems.

### 🤖 AI 总结

**一句话总结**：Generative Engine Optimization (GEO) modifies web content to increase its likelihood of being selected and cited by generative search engines. This can give strategically optimized pages visibility di...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GEO-Flag, Detecting, Measuring, GEO-Optimized, Web, Content, Generative, Engine

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16824v1) | [下载PDF](https://arxiv.org/pdf/2608.16824v1.pdf)

---

## [28. Beyond $L_2$: Generalizing Abductive Latent Explanations to Diverse Prototype-Based Architectures](https://arxiv.org/abs/2608.16773v1)

**作者**：Jules Soria, Alban Grastien, Romain Xu-Darme 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-17

### 📄 论文摘要

Prototype-based neural networks are hailed as interpretable-by-design architectures. Recently, Abductive Latent Explanations (ALE) were introduced to provide formal, mathematically guaranteed explanations that leverage the intrinsic structure of these networks to ensure both predictive safety and human readability. ALEs rely on computing tight bounds on latent space distances to produce formal explanations. However, existing ALE formulations are rigidly confined to Euclidean latent spaces. This leaves a critical gap: modern state-of-the-art architectures increasingly rely on non-Euclidean representations - such as spherical metrics, Gaussian densities, and dimensional projections - rendering current formal explanation methods incompatible. In this work, we generalize the ALE framework to support non-Euclidean prototype architectures. For each geometric variant, we systematically derive how to either map the architecture to existing bounds or construct novel, architecture-specific bounding algorithms. We validate our theoretical constructions by computing subset-minimal formal explanations on fully trained image classifiers. By unifying these diverse models under a single formal framework, we enable the first rigorous, cross-architecture comparison of their interpretability.

### 🤖 AI 总结

**一句话总结**：Prototype-based neural networks are hailed as interpretable-by-design architectures. Recently, Abductive Latent Explanations (ALE) were introduced to provide formal, mathematically guaranteed explanat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：$L, 2$, Beyond, Generalizing, Abductive, Latent, Explanations, Diverse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16773v1) | [下载PDF](https://arxiv.org/pdf/2608.16773v1.pdf)

---

## [29. On the Principles Behind Neural Network Optimizers](https://arxiv.org/abs/2608.16760v1)

**作者**：Yushun Zhang  
**分类**：cs.LG, math.OC  
**发布时间**：2026-08-17

### 📄 论文摘要

Reliable optimization is central to neural network (NN) training, yet Adam, the default optimizer for modern LLMs, rests on a fragile foundation. This thesis develops a principled grounding for Adam and motivates new designs. First, we revisit Adam's divergence--convergence debate and show the existence of a problem-dependent phase transition: with properly chosen, batch-size-dependent hyperparameters, Adam converges, whereas under small-$β_2$ regimes it can diverge. Second, we investigate why Adam substantially outperforms SGD on Transformers through Hessian structure. We find that the Hessian evolves toward a near-block-diagonal form along training, accompanied by strong block heterogeneity. We prove that this structure makes Adam's diagonal preconditioner effective. We further show that this special Hessian structure originates from consecutive multiplications of large matrix variables, and we provide a rigorous analysis based on random matrix theory. Finally, these insights motivate Adam-mini, a new optimizer that reduces Adam's memory footprint by 50\% while preserving its performance. Our results also have broader implications beyond Adam: they reveal new local structures in matrix-based nonconvex problems, and also help understand and improve recent NN optimizers, such as Muon.

### 🤖 AI 总结

**一句话总结**：Reliable optimization is central to neural network (NN) training, yet Adam, the default optimizer for modern LLMs, rests on a fragile foundation. This thesis develops a principled grounding for Adam a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Principles, Behind, Neural, Network, Optimizers, Reliable, optimization, central

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16760v1) | [下载PDF](https://arxiv.org/pdf/2608.16760v1.pdf)

---

## [30. Would this change your answer? Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments](https://arxiv.org/abs/2608.16747v1)

**作者**：Adam Karvonen, Euan Ong, Subhash Kantamneni 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-17

### 📄 论文摘要

Many areas of AI research, such as language model interpretability and chain of thought faithfulness, seek to explain model behaviors. But what constitutes a "good" explanation? In this work, we evaluate explanations through the lens of counterfactual simulatability-whether the explanation is useful for predicting model behaviors on related counterfactual inputs. To this end, we introduce CHIVE (Counterfactual Hypothesis Investigation Via Edits), a novel agentic pipeline that identifies unexpected model behaviors in the wild and investigates them with counterfactual prompt edits. This yields thousands of high-quality explanations for naturally-occurring model behaviors along with supporting counterfactual evidence. We apply CHIVE in two ways. First, we evaluate whether common LLM interpretability techniques improve an agent's ability to predict counterfactual model behaviors. Surprisingly, we find no uplift from any of the interpretability techniques studied. Second, we use CHIVE to generate training data. We find that training models to predict outcomes of CHIVE-generated counterfactual experiments generalizes to various out-of-distribution settings. Overall, CHIVE automatically discovers explanations of naturally-occurring LLM behaviors, enabling us to evaluate and improve methods for explaining LLM behaviors.

### 🤖 AI 总结

**一句话总结**：Many areas of AI research, such as language model interpretability and chain of thought faithfulness, seek to explain model behaviors. But what constitutes a "good" explanation? In this work, we evalu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Would, change, answer?, Evaluating, Explanations, Behavior

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.16747v1) | [下载PDF](https://arxiv.org/pdf/2608.16747v1.pdf)

---

