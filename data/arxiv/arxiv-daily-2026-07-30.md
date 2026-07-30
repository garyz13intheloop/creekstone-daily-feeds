# arXiv AI 论文日报 | 2026-07-30

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (9 篇)
- [cs.LG](#csLG) (13 篇)
- [cs.CL](#csCL) (2 篇)
- [cs.AI](#csAI) (6 篇)

---

## cs.AI

## [1. Can AI agents conduct open-ended AI research? Early evidence from two case studies](https://arxiv.org/abs/2607.27191v1)

**作者**：Peter Kirgis, Sayash Kapoor, Andrew Schwartz 等 24 位作者  
**分类**：cs.AI, cs.CY, cs.LG  
**发布时间**：2026-07-29

### 📄 论文摘要

Forecasts of explosive AI progress hinge on AI agents automating AI research. But evidence on whether agents can carry out open-ended AI research is thin. Current evaluations either test agents on narrow, verifiable tasks, which excludes open-ended research, or submit AI-generated papers to blind peer review, which is overstretched, stochastic, and suffers from poor review quality. We introduce a third way to measure progress towards AI R\&D automation. An agent takes on the central, open-ended research question of a high-quality unpublished paper, and the paper's original authors grade its output. We call these shadow evaluations. We ran shadow evaluations on two unpublished NeurIPS 2026 submissions, giving frontier agents six days and thousands of dollars of compute. The agents completed all of the engineering without human help, yet could not make substantial progress towards answering the research questions. As a result, both papers were unambiguously rejected by the authors. We identify five recurring failure modes: poor judgment about the bar for publishable research, uncreative responses to shortcomings in the research design, ineffective backtracking from dead ends, poor resource awareness, and instruction drift. A robustness check with a second model and scaffold reproduced these failures. We release the expert reviews, survey responses, agent repositories, and logs. Our results provide early evidence that today's agents can do the engineering of AI research, but struggle with critical parts of the research lifecycle.

### 🤖 AI 总结

**一句话总结**：Forecasts of explosive AI progress hinge on AI agents automating AI research. But evidence on whether agents can carry out open-ended AI research is thin. Current evaluations either test agents on nar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Can, conduct, open-ended, research?, Early, evidence, two

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27191v1) | [下载PDF](https://arxiv.org/pdf/2607.27191v1.pdf)

---

## [2. Partner Capability Estimation for Task-Agnostic Adaptation in Ad-Hoc Teamwork](https://arxiv.org/abs/2607.27177v1)

**作者**：Peter Tisnikar, Maja Swieczkowska, Benteng Ma 等 5 位作者  
**分类**：cs.AI, cs.HC, cs.MA  
**发布时间**：2026-07-29

### 📄 论文摘要

Effective collaboration with novel and diverse partners is a crucial skill for autonomous agents. Most current ad-hoc teamwork (AHT) approaches assume that agents will collaborate on a single, fixed task and that the partner's capabilities, their ability to successfully execute the desired action, are already known. In reality, a partner's true capabilities are often hidden, and human collaborators may act sub-optimally on tasks with multiple valid strategies. To address these limitations, we extend ad-hoc teamwork into a multi-task setting by re-framing it as a problem of joint planning with decentralised execution under hidden partner capabilities. We introduce CE-CM (Capability Estimation via Contextual Models), an approximate Bayesian method that infers task-invariant capability vectors. By using simulation-based sampling, the agent estimates capabilities and induces a contextual Multi-agent Markov Decision Processes for planning. This approach requires no population pre-training and refines its beliefs online from just a few tasks. To account for human unpredictability, we propose CE-CM-Div, an extension that evaluates capability hypotheses against diverse planner rollouts rather than a single optimal trajectory. Simulated experiments demonstrate that CE-CM rapidly recovers hidden capabilities, reduces infeasible action assignments, and adapts to changes over time. Furthermore, in an offline human study of 225 trajectories from 15 participants, CE-CM-Div substantially improved capability estimates over the baseline CE-CM method. Our results suggest capability-based modelling is a promising interpretable, task-agnostic representation in the studied settings, demonstrating that accounting for behavioural diversity is essential for robust human-AI teaming.

### 🤖 AI 总结

**一句话总结**：Effective collaboration with novel and diverse partners is a crucial skill for autonomous agents. Most current ad-hoc teamwork (AHT) approaches assume that agents will collaborate on a single, fixed t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Partner, Capability, Estimation, Task-Agnostic, Adaptation, Ad-Hoc, Teamwork, Effective

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27177v1) | [下载PDF](https://arxiv.org/pdf/2607.27177v1.pdf)

---

## [3. OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding](https://arxiv.org/abs/2607.27155v1)

**作者**：Jingbo Zhou, Yusai Zhao, Qi Bao 等 15 位作者  
**分类**：cs.AI, cs.CL, cs.HC  
**发布时间**：2026-07-29

### 📄 论文摘要

Large language model (LLM) agents are increasingly expected to assist users in completing tasks. However, existing benchmarks provide limited support for evaluating whether agents can carry out office-suite workflows at a reasonable cost. We introduce OmegaUse-OfficeVal, a benchmark for evaluating LLM agents on long-horizon office-suite tasks with task-level economic grounding. The benchmark comprises 100 tasks derived from office-suite requests proposed by practitioners and adapted through a privacy-preserving process. On average, these tasks require 2.32 hours of human labor to complete. An important feature of the benchmark is that each task is paired with two economic signals: human labor time and task price proxy. These signals enable direct comparisons between human costs and LLM inference costs, as well as value-weighted evaluation. To support stable evaluation, we develop code-based verifiers from fine-grained rubrics. We evaluate several frontier LLMs together with a human baseline. Although all evaluated LLMs are substantially cheaper and faster than human workers, they have not yet approached human-level deliverable quality. The code and dataset are fully open-sourced, and more information is available on our project website: https://omegause-officeval.github.io.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM) agents are increasingly expected to assist users in completing tasks. However, existing benchmarks provide limited support for evaluating whether agents can carry out office...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, OmegaUse-OfficeVal, Benchmarking, Long-Horizon, Office-Suite, Tasks, Economic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27155v1) | [下载PDF](https://arxiv.org/pdf/2607.27155v1.pdf)

---

## [4. Linguistic Monoculture in LLM-Assisted Language Use](https://arxiv.org/abs/2607.27134v1)

**作者**：Suhas Thejaswi, Juhi Kulshreshta, Lutz Oettershagen  
**分类**：cs.AI, cs.CL, cs.GT  
**发布时间**：2026-07-29

### 📄 论文摘要

Writing and communication are increasingly mediated by large language models (LLMs) that are being used to draft, revise and polish text. Although such assistance can improve clarity and help authors meet institutional expectations, widespread reliance on shared models may reduce population-level variation in linguistic form, a phenomenon we refer to as linguistic monoculture. We develop a mathematical framework in which authors and LLMs are represented as distributions over linguistic features and coevolve through repeated interaction. We analyze three interaction mechanisms: a shared model with a fixed linguistic distribution, a shared model recursively updated from author outputs, and personalized models updated through author-specific and population-level feedback. We characterize the resulting equilibria and convergence rates, showing that, shared models can drive authors toward a common norm, recursive feedback relocates the shared norm without altering pairwise spread under common conformity, and personalization can preserve a family of distinct author-model equilibria with nonzero linguistic diversity. We then endogenize conformity as a strategic choice trading off private benefits from clarity, legibility, and perceived fluency against distinctive style. Within this utility model, individually rational authors may conform more than is socially optimal because they do not internalize the value their distinctiveness provides to others, creating a negative externality and a price of monoculture that is finite for each fixed instance but can grow without bound when distinctiveness dominates authenticity. Synthetic simulations illustrate how fixed shared assistance, recursive feedback, and personalization produce different long-run diversity outcomes.

### 🤖 AI 总结

**一句话总结**：Writing and communication are increasingly mediated by large language models (LLMs) that are being used to draft, revise and polish text. Although such assistance can improve clarity and help authors ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Linguistic, Monoculture, LLM-Assisted, Language, Use, Writing, communication, increasingly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27134v1) | [下载PDF](https://arxiv.org/pdf/2607.27134v1.pdf)

---

## [5. AgentMap: Joint Equivalence and Subsumption Discovery for Ontology Matching](https://arxiv.org/abs/2607.27130v1)

**作者**：Yiping Song, Jiaoyan Chen, Renate Schmidt 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-29

### 📄 论文摘要

Ontology matching (OM) has traditionally been formulated as either equivalence discovery or subsumption matching. The existing OM systems identify only one type of semantic correspondence and cannot simultaneously discover equivalence and subsumption mappings. In this paper, we introduce Hybrid Ontology Matching (HOM), a new OM task that unifies equivalence and subsumption discovery, and accordingly propose a Large Language Model (LLM)-based multi-agent OM framework AgentMap that is implemented by a series of interdependent semantic decisions. Given a concept in the source ontology, AgentMap integrates semantic retrieval, hierarchical search, and collaborative multi-agent LLM reasoning to progressively explore the target ontology, identifying either the equivalent concept, if one exists, or the most fine-grained subsumer. We further extend four OM datasets for a HOM benchmark and evaluate AgentMap under hybrid, equivalence-only, and subsumption-only settings. Experimental results show that AgentMap achieves promising performance on the hybrid setting, and at the same time outperforms equivalence matching and subsumption matching baselines on the equivalence-only and subsumption-only settings, respectively.

### 🤖 AI 总结

**一句话总结**：Ontology matching (OM) has traditionally been formulated as either equivalence discovery or subsumption matching. The existing OM systems identify only one type of semantic correspondence and cannot s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OM, AgentMap, Joint, Equivalence, Subsumption, Discovery, Ontology, Matching

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27130v1) | [下载PDF](https://arxiv.org/pdf/2607.27130v1.pdf)

---

## [6. On-Policy Distillation for LLM Safety: A Routing Approach to Template-Robust Realignment](https://arxiv.org/abs/2607.27081v1)

**作者**：Yongjian Guo, Wanlun Ma, Lingyu Shen 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.CR, cs.LG  
**发布时间**：2026-07-29

### 📄 论文摘要

Fine-tuning is the dominant paradigm for specializing large language models (LLMs), yet it exposes a critical vulnerability: malicious data providers can embed harmful behaviors into downstream corpora, creating models that retain professional skills while violating human values on demand. Existing safety-realignment defenses often fail in practice due to three key limitations: they frequently cause catastrophic forgetting of specialized skills; their effectiveness collapses when the defender cannot observe the attacker's prompt template; and successfully realigned models remain susceptible to re-jailbreaking via simple system prompt switches. To address these challenges, we propose Routing-based On-Policy Distillation (ROPD), a novel realignment framework that models the divergence between aligned and compromised output probability distributions rather than fitting specific prompt templates. We conduct extensive experiments comparing ROPD against four state-of-the-art baselines across three datasets and three base models with varying alignment strengths. Our results demonstrate that when baseline defenses face template mismatches, often accompanied by severe degradation in downstream task performance. In contrast, ROPD substantially mitigates template-mismatch risks, maintaining superior robustness in both defense effectiveness and capability preservation. While our analysis indicates ROPD is not entirely immune to template shifts, its performance degradation is negligible compared to existing methods, establishing a new standard for robust LLM realignment.

### 🤖 AI 总结

**一句话总结**：Fine-tuning is the dominant paradigm for specializing large language models (LLMs), yet it exposes a critical vulnerability: malicious data providers can embed harmful behaviors into downstream corpor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, On-Policy, Distillation, Safety, Routing, Approach, Template-Robust, Realignment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27081v1) | [下载PDF](https://arxiv.org/pdf/2607.27081v1.pdf)

---

## cs.CL

## [7. Mental World Modeling](https://arxiv.org/abs/2607.27201v1)

**作者**：Hao Fei, Yiran Zhao  
**分类**：cs.CL  
**发布时间**：2026-07-29

### 📄 论文摘要

World models enable a predictive substrate for planning and action, yet existing formulations merely answer a physical question: what/where it is, and how will it evolve. Human behavior, however, is driven by hidden mental state (what a person believes, wants, intends, feels, and considers socially permissible), so a model that tracks the physical scene but not what each agent knows and believes about it predicts the wrong action for the right-looking scene. We formulate Mental World Modeling (MWM), a generic theoretical framework that makes mental variables core components of a world model rather than posthoc rationales: MWM aintains a coupled physical-mental world state, renders a target-specific partial observation, and simulates how candidate actions jointly update both components. We instantiate the framework in MENTIS, a training-free and fully inspectable baseline that decomposes the process into state parsing, target-observation generation, action decomposition, coupled physical and mental transition, and branch-level value evaluation. On a manually constructed, quality-controlled dataset of situated decision scenarios spanning text, image, and sounding-video stories, experiments with 8 modern LLM-based world models demonstrate that explicitly modeling the mental state is essential for predicting human decisions. Deeper analyses further expose the bottlenecks of current mental world modeling. We expect MWM as a next stage of world modeling, from simulating physical scenes to simulating the minds that act in them.

### 🤖 AI 总结

**一句话总结**：World models enable a predictive substrate for planning and action, yet existing formulations merely answer a physical question: what/where it is, and how will it evolve. Human behavior, however, is d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mental, World, Modeling, models, enable, predictive, substrate, planning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27201v1) | [下载PDF](https://arxiv.org/pdf/2607.27201v1.pdf)

---

## [8. Pangram 4 Technical Report](https://arxiv.org/abs/2607.27183v1)

**作者**：Ben Glickenhaus, Katherine Thai, Jenna Russell 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-29

### 📄 论文摘要

We present Pangram 4, the latest deep-learning-based AI-text classification model from Pangram Labs. We achieve an AUROC of 0.9916 with a false positive rate of 0.0041% and a false negative rate of 0.3396%. In addition to its increased overall accuracy compared with Pangram 3, Pangram 4 exhibits superior out-of-distribution generalization and robustness to adversarial attacks. Another novel contribution of Pangram 4 is its improved ability to distinguish fine-grained edits and mixed AI-human co-authored text. We demonstrate improvements to both boundary detection tasks and the detection of interleaved AI assistance. Finally, we report metrics on standard AI detection benchmarks showing that Pangram 4 achieves state-of-the-art performance on the AI text detection task across a wide variety of settings and domains.

### 🤖 AI 总结

**一句话总结**：We present Pangram 4, the latest deep-learning-based AI-text classification model from Pangram Labs. We achieve an AUROC of 0.9916 with a false positive rate of 0.0041% and a false negative rate of 0....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Pangram, Technical, Report, present, latest, deep-learning-based, AI-text

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27183v1) | [下载PDF](https://arxiv.org/pdf/2607.27183v1.pdf)

---

## cs.CV

## [9. TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM](https://arxiv.org/abs/2607.27205v1)

**作者**：Hengyi Xie, Chenfei Yao, Xianjin Wu 等 10 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-07-29

### 📄 论文摘要

Vision-language-action (VLA) models commonly adopt an LLM-centric $V \to L \to A$ pathway, where visual observations are projected into the representation space of a large language model before being decoded into robot actions. Although effective, this design incurs substantial computation and memory overhead at every policy invocation. In this work, we introduce TurboVLA, a new VLA paradigm that reformulates the conventional $V \to L \to A$ pathway as a direct $V + L \to A$ mapping. Instead of using a large language model as the central interface between perception and action, TurboVLA independently encodes visual observations and language instructions, directly exchanges information between them through lightweight bidirectional vision-language interaction, and predicts continuous action chunks with a compact decoder. This simple design constructs task-conditioned representations directly from visual and linguistic features, significantly reducing the computational and memory costs of VLA inference. On LIBERO, TurboVLA achieves 97.7% average success with only 0.2B parameters, 31.2 ms inference latency, and 0.9 GB inference VRAM on a consumer-grade RTX 4090, matching or outperforming substantially larger VLA policies. These results establish TurboVLA as a simple and effective alternative to the prevailing LLM-centric VLA paradigm, offering a new perspective on how vision, language, and action can be connected for efficient robotic manipulation. Code is available at https://github.com/H-EmbodVis/TurboVLA.

### 🤖 AI 总结

**一句话总结**：Vision-language-action (VLA) models commonly adopt an LLM-centric $V \to L \to A$ pathway, where visual observations are projected into the representation space of a large language model before being ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Hz, an, TurboVLA, Real-Time, Vision-Language-Action, Model, RTX

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27205v1) | [下载PDF](https://arxiv.org/pdf/2607.27205v1.pdf)

---

## [10. VidMap: Exploiting Temporal Structure for Video-Based Structure-from-Motion](https://arxiv.org/abs/2607.27194v1)

**作者**：Zador Pataki, Paul-Edouard Sarlin, Marc Pollefeys  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-07-29

### 📄 论文摘要

Accurately recovering the camera's calibration and metric poses for any unconstrained video would unlock large-scale training data for navigation and scene understanding. The dominant approaches to this problem are severely limited: Simultaneous Localization and Mapping (SLAM) is sensitive to initialization and transient failures due to its causal, incremental nature; it is often over-optimized for real-time operation and generally requires known camera calibration; while Structure-from-Motion (SfM) typically forgoes any image ordering, enabling optimal initialization and global optimization, but lacks robustness to visual symmetries and extreme motions. To bridge this gap, we introduce a system that combines the strong sequential constraints of SLAM with the flexibility and global optimization of offline SfM, enabling the metric reconstruction of arbitrary, long, uncalibrated videos. This system leverages recent advances in wide-baseline dense image matching, treats temporal ordering as a first-class citizen for reliable loop closure, and augments global optimization with metric monocular depth priors. As a result, thorough evaluations on diverse, challenging datasets that exhibit extreme motion and visual symmetries reveal that our approach is significantly more robust and accurate than both state-of-the-art SLAM and SfM, classical or learned, with given or unknown camera calibration. The code is publicly available at https://github.com/cvg/vidmap.

### 🤖 AI 总结

**一句话总结**：Accurately recovering the camera's calibration and metric poses for any unconstrained video would unlock large-scale training data for navigation and scene understanding. The dominant approaches to th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VidMap, Exploiting, Temporal, Structure, Video-Based, Structure-from-Motion, Accurately, recovering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27194v1) | [下载PDF](https://arxiv.org/pdf/2607.27194v1.pdf)

---

## [11. HumanCLAW: Can Vision-Language Models Act Through a Body?](https://arxiv.org/abs/2607.27180v1)

**作者**：Siyao Li, Jiawei Gu, Shuai Liu 等 18 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-07-29

### 📄 论文摘要

Evaluating whether a vision-language model (VLM) can act through a physical body is challenging. The outcome of an action couples the VLM's decision with motor control. When a task fails, it is hard to tell whether the VLM made a bad choice or the motor controller simply failed to execute it, e.g., losing balance and falling. In this work, we introduce HumanCLAW, an evaluation framework that decouples action decision-making from low-level execution. At every step, a harnessed, off-the-shelf VLM issues an atomic skill command, and the command is translated into a sub-second chunk of continuous full-body motion with real physical consequences, including gravity and collisions. The body can therefore act freely in the physical world, while execution-side disturbances, balance and motor errors, are factored out. What remains measurable is the model's action intelligence: its moment-to-moment choice of what the body should execute next. Based on this framework, we build HumanCLAW-Bench: 1,218 long-horizon, egocentric find-navigate-interact episodes across 41 indoor scenes. We test nine state-of-the-art VLMs and find that none solves the benchmark; the best model reaches only a 16.8% success rate. Recognizing the target is not the bottleneck. What current VLMs lack is embodied self-awareness: they lose track of their own body, failing to tell where it is, whether it has reached the goal, or whether it has hit an obstacle.

### 🤖 AI 总结

**一句话总结**：Evaluating whether a vision-language model (VLM) can act through a physical body is challenging. The outcome of an action couples the VLM's decision with motor control. When a task fails, it is hard t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HumanCLAW, Can, Vision-Language, Models, Act, Through, Body?, Evaluating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27180v1) | [下载PDF](https://arxiv.org/pdf/2607.27180v1.pdf)

---

## [12. Anatomy Contextualized Adaption of CT Foundation Models](https://arxiv.org/abs/2607.27154v1)

**作者**：Roshan Kenia, Stephanie L McNamara, William Lotter  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-29

### 📄 论文摘要

CT vision-language foundation models have demonstrated promising performance across downstream tasks, but are typically trained with whole-volume representations that dilute fine-grained anatomical signals. Fine-grained vision-language pre-training addresses this by aligning anatomy-level visual features with anatomy-specific text, but in doing so discards the global context that whole-volume models provide. Furthermore, existing fine-grained approaches train from scratch, making them computationally expensive. We introduce Anatomy Contextualized Adaptation (ACA), a lightweight framework that adapts frozen CT foundation model representations for anatomy-level vision-language alignment while enhancing global contextualization. ACA uses TotalSegmentator to decompose CT volumes into anatomy-level embeddings, which are refined via a transformer that captures cross-anatomy relationships, and aligned to both per-anatomy and scan-level text extracted from radiology reports. Evaluated on Merlin and CT-RATE, ACA consistently outperforms both the frozen foundation model baselines and existing fine-grained methods in zero-shot finding classification, while requiring less than one hour of training once embeddings are cached. The attention weights learned by ACA's inter-anatomy transformer additionally indicate plausible cross-anatomy context routing. Altogether, these results support ACA as a lightweight approach for adapting CT foundation models to anatomically grounded vision-language alignment while preserving and enhancing global anatomical context.

### 🤖 AI 总结

**一句话总结**：CT vision-language foundation models have demonstrated promising performance across downstream tasks, but are typically trained with whole-volume representations that dilute fine-grained anatomical si...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, CT, Anatomy, Contextualized, Adaption, Foundation, Models, vision-language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27154v1) | [下载PDF](https://arxiv.org/pdf/2607.27154v1.pdf)

---

## [13. SeasonStereo: Robust Dense Stereo Matching for Multi-Date Satellite Imagery via Generative AI](https://arxiv.org/abs/2607.27139v1)

**作者**：Álvaro Díaz-Laureano, Roger Marí, Elías Masquil 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-29

### 📄 论文摘要

Accurate 3D reconstruction from satellite imagery typically relies on near-simultaneous stereo pairs, limiting its applicability to diachronic settings where multi-date images exhibit varying seasonal and illumination conditions. Training dense stereo matching models robust to appearance changes is a long-standing challenge, as aligned multi-date imagery and ground-truth geometry are costly to obtain at scale. We propose SeasonStereo, a scalable framework that addresses disparity estimation from diachronic satellite images by training on synthetic image pairs with controlled seasonal appearance variation, while leveraging zero-shot geometric priors from foundation models. SeasonStereo matches the accuracy of state-of-the-art LiDAR-supervised models, while producing sharper geometric details without requiring aligned real multi-date training products or LiDAR-derived labels. As a result, SeasonStereo offers a practical path toward large-scale 3D reconstruction from heterogeneous satellite images with reduced supervision cost.

### 🤖 AI 总结

**一句话总结**：Accurate 3D reconstruction from satellite imagery typically relies on near-simultaneous stereo pairs, limiting its applicability to diachronic settings where multi-date images exhibit varying seasonal...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SeasonStereo, Robust, Dense, Stereo, Matching, Multi-Date, Satellite, Imagery

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27139v1) | [下载PDF](https://arxiv.org/pdf/2607.27139v1.pdf)

---

## [14. Veritas++: Value-aware On-Policy Distillation for Perception-Enhanced AIGI Detection](https://arxiv.org/abs/2607.27113v1)

**作者**：Hao Tan, Jun Lan, Zichang Tan 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-29

### 📄 论文摘要

The growing capability of image generation models has made synthetic images a routine presence in open media, making robust and generalizable AI-Generated Image (AIGI) detection increasingly essential. While multi-modal large language models (MLLMs) offer a transparent alternative to black-box binary scoring, we observe that current MLLM-based detectors still exhibit notable perception bottlenecks in capturing fine-grained anomalies. They primarily focus on how visual evidence is organized and synthesized, leaving the intrinsic perception less optimized. To mitigate this gap, we present Veritas++, a perception-enhanced reasoning framework that establishes reliable perception as the foundation of authenticity reasoning. Rather than directly optimizing the model's explanatory ability, we ground AIGI detection on three basic perception abilities, i.e., capturing fine-grained visual details, semantic anomalies and pixel-level differences. Building on this insight, we introduce Perception-oriented Learning (PoRL), which replaces open-ended description supervision with verifiable rewards to explicitly strengthen these capacities. To further integrate enhanced perception with reasoning, we introduce Value-aware On-Policy Distillation (VaOPD), an adaptive distillation mechanism that prioritizes high-value distillation signals over uniform supervision, internalizing perception-aware reasoning through a privileged self-teacher. Extensive experiments across standard, in-the-wild and emerging benchmarks demonstrate that Veritas++ achieves promising generalization. The perception learning effectively bridges the perception gap and yields seamless gains on detection, while VaOPD further enables efficient capability evolvement without sacrificing existing performance. Code and checkpoints are available at https://github.com/EricTan7/VeritasPP.

### 🤖 AI 总结

**一句话总结**：The growing capability of image generation models has made synthetic images a routine presence in open media, making robust and generalizable AI-Generated Image (AIGI) detection increasingly essential...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Veritas++, Value-aware, On-Policy, Distillation, Perception-Enhanced, AIGI, Detection, growing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27113v1) | [下载PDF](https://arxiv.org/pdf/2607.27113v1.pdf)

---

## [15. FreqForcing: Autoregressive Long Video Generation via Spectral Self-Anchoring](https://arxiv.org/abs/2607.27110v1)

**作者**：Jiatong Li, Leo Liang, Linghe Kong 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-29

### 📄 论文摘要

Autoregressive video diffusion models enable real-time streaming video generation. However, errors introduced during self-rollout accumulate over long horizons, manifesting as color drift, motion stagnation, and eventual visual collapse. In this paper, we characterize this phenomenon from a frequency-domain perspective: error accumulation appears as a pronounced energy drift in the low-frequency bands. We further investigate the effectiveness of attention sink in the frequency domain, and find that it improves the video quality by alleviating the spectral energy drift to some extent, but cannot fully resolve it. Motivated by the above analysis, we propose FreqForcing, a training-free framework that addresses error accumulation in long-video generation via Spectral Self-Anchoring (SSA). The proposed SSA leverages the low-frequency components of anchor attention to maintain long-horizon visual stability, while preserving dynamic motion through the high-frequency components of local attention. Our FreqForcing extends Self-Forcing pretrained on 5s clips to two-minute generation, achieving 24x extrapolation. Extensive experiments show that FreqForcing outperforms existing training-free methods quantitatively and qualitatively while remaining competitive with representative training-based approaches.

### 🤖 AI 总结

**一句话总结**：Autoregressive video diffusion models enable real-time streaming video generation. However, errors introduced during self-rollout accumulate over long horizons, manifesting as color drift, motion stag...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FreqForcing, Autoregressive, Long, Video, Generation, via, Spectral, Self-Anchoring

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27110v1) | [下载PDF](https://arxiv.org/pdf/2607.27110v1.pdf)

---

## [16. Step-Attention Refinement of DINOv3 Features for Efficient Anterior Eye Segmentation](https://arxiv.org/abs/2607.27087v1)

**作者**：Philippe Baumstimler, Jean-Mathieu Gagnon, Sébastien Gagné 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-29

### 📄 论文摘要

Anterior eye segment (AES) segmentation is a key component of both ocular biometrics and emerging clinical image analysis applications. However, heterogeneous acquisition conditions and limited annotations in medical settings hinder the robustness and generalization of existing methods. Foundation models (FMs) such as DINOv3 offer strong transfer capabilities, but efficiently adapting their representations to dense prediction tasks remains challenging. In this study, we investigate robust AES segmentation in clinical settings, and propose a lightweight architecture built upon a distilled DINOv3 ViT-Small backbone. We introduce a step-attention feature refinement module that progressively adapts multi-level transformer representations before convolutional decoding, enabling efficient exploitation of pretrained features with few parameters. We evaluate the proposed approach on a private dataset of 333 clinically acquired AES images spanning eight ophthalmic acquisition protocols and annotated for seven anatomical classes. Compared with convolutional and transformer-based baselines, including DINOv3-based methods, our approach achieves the best overall performance, reaching 85.55\% mIoU when fully fine-tuned. It also demonstrates the strongest robustness to domain shift across four unseen public AES segmentation datasets. These results establish a strong baseline for robust AES segmentation in clinical settings and highlight the importance of decoder design for effectively adapting FMs representations to medical segmentation tasks.

### 🤖 AI 总结

**一句话总结**：Anterior eye segment (AES) segmentation is a key component of both ocular biometrics and emerging clinical image analysis applications. However, heterogeneous acquisition conditions and limited annota...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Step-Attention, Refinement, DINOv3, Features, Efficient, Anterior, Eye

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27087v1) | [下载PDF](https://arxiv.org/pdf/2607.27087v1.pdf)

---

## [17. SciFigQual-Bench: A Benchmark for Scientific Figure Quality Assessment with Full-Manuscript Context](https://arxiv.org/abs/2607.27084v1)

**作者**：Zihan Deng, Chuanzhi Xu, Huiqi Liang 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-29

### 📄 论文摘要

Scientific images are the core elements of presenting experimental conclusions, elaborating system architecture, and supporting comparative arguments in scientific papers. However, existing image quality assessment (IQA) methods are predominantly designed for natural photographs or AI-generated content, which cannot be directly applied to scientific papers. The few existing studies on scholarly charts remain confined to visual-surface comparisons, failing to verify caption alignment, citation relevance, or visual misleadingness. To address this, we propose SciFigQual-Bench, a full-text contextual benchmark that evaluates scientific images across five dimensions (clarity, layout, caption fit, context relevance, and misleading risk). The data covers top computer-science conferences from 2020 to 2025; 6,308 images were independently scored by multiple domain experts in five dimensions and aggregated into gold-standard annotations. Unlike previous scientific figure benchmarks, our dataset binds each image to its caption, citing sentence, and manuscript context. To enable automated evaluation on this benchmark, we designed a staged cross-modal evaluation framework SFQ-Agent to achieve auditable and refined scoring through the collection and fusion of modal evidence. Multiple mainstream large models were evaluated on the test subset eval1200, and SFQ-Agent (F3) equipped with GPT-5.6-Sol achieved the lowest overall average absolute error (0.418) and the highest consistency rate (93.4%), consistently outperforming both direct evaluation and auxiliary (Sidecar) visual language model evaluation schemes.

### 🤖 AI 总结

**一句话总结**：Scientific images are the core elements of presenting experimental conclusions, elaborating system architecture, and supporting comparative arguments in scientific papers. However, existing image qual...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SciFigQual-Bench, Benchmark, Scientific, Figure, Quality, Assessment, Full-Manuscript, Context

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27084v1) | [下载PDF](https://arxiv.org/pdf/2607.27084v1.pdf)

---

## cs.LG

## [18. Do You Really Need to Pretrain Q-Functions for Online RL Fine-Tuning?](https://arxiv.org/abs/2607.27203v1)

**作者**：Perry Dong, Ron Polonsky, Dorsa Sadigh 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-29

### 📄 论文摘要

Pre-training followed by fine-tuning has become the dominant recipe for learning performant policies, and in value-based reinforcement learning (RL) this raises a natural question: given a pretrained policy, should the Q-function be pretrained on offline data too? Conventional wisdom suggests it should, but recent results show that online RL with a randomly-initialized Q-function can result in highly performant and reliable policies without needing to pretrain the Q-function. In this paper, we systematically study whether pretraining the Q-function actually helps when fine-tuning on top of a pretrained base policy. We find, surprisingly, that naive Q-function pretraining often provides little benefit over random initialization. We show this stems from a fundamental mismatch: the Q-function learned during pretraining targets the pretrained policy's Q-function, not the Q-function that online fine-tuning converges to, and this gap persists even after offline value maximization. Motivated by this finding, we propose Initialization via Policy Ensemble (IPE), a simple method that trains multiple diverse policies and uses their pooled rollouts to bootstrap the Q-function learning in online RL. Across a suite of challenging continuous control benchmarks, IPE yields an average 1.26x improvement in fine-tuning performance over naive Q-function pre-training.

### 🤖 AI 总结

**一句话总结**：Pre-training followed by fine-tuning has become the dominant recipe for learning performant policies, and in value-based reinforcement learning (RL) this raises a natural question: given a pretrained ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, RL, Really, Need, Pretrain, Q-Functions, Online, Fine-Tuning?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27203v1) | [下载PDF](https://arxiv.org/pdf/2607.27203v1.pdf)

---

## [19. From Classification to Regression: Using a Fruitfly to Solve Equations](https://arxiv.org/abs/2607.27196v1)

**作者**：Shady E. Ahmed, Panos Stinis  
**分类**：cs.LG, math.NA  
**发布时间**：2026-07-29

### 📄 论文摘要

We present a novel approach to regression tasks using classification which is motivated by the mechanism used by fruitflies to sense their environment. Specifically, we formulate a general framework for learning nonlinear input-output relationships by replacing complex global surrogate models with a finite library of representative local patterns. Since scientific data often occupy limited and recurring regions of the input space, we generate predictions by measuring similarities between a query and stored patterns, then combining their associated responses through weighted reconstruction. We apply this approach to nonlinear dynamical systems, data-driven regression, and physics-informed learning using suitable embeddings and similarity measures. For dynamical systems, our offline-online workflow extracts patterns from data or governing equations during the offline phase, while online prediction requires only similarity evaluation and response aggregation. This structure helps us reduce computational and memory demands while providing explicit control over the trade-off among accuracy, storage, and inference cost.

### 🤖 AI 总结

**一句话总结**：We present a novel approach to regression tasks using classification which is motivated by the mechanism used by fruitflies to sense their environment. Specifically, we formulate a general framework f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Classification, Regression, Fruitfly, Solve, Equations, present, novel

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27196v1) | [下载PDF](https://arxiv.org/pdf/2607.27196v1.pdf)

---

## [20. Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes](https://arxiv.org/abs/2607.27188v1)

**作者**：Lennon J. Shikhman, Michael Galarnyk, Aadi Dash 等 4 位作者  
**分类**：cs.LG, q-fin.CP, q-fin.PR, q-fin.ST  
**发布时间**：2026-07-29

### 📄 论文摘要

Accurate option prices do not imply accurate recovery of the latent risk-neutral density. We study this distinction with two complementary benchmarks. A controlled benchmark exposes simulator-truth densities for latent evaluation, while a chronological NIFTY benchmark tests only held-out market prices. A two-component lognormal mixture has the lowest aggregate price, $L^1$, Wasserstein, and fixed-tail errors on the synthetic benchmark. Learned operators retain narrower strengths: DeepONet reduces 1% quantile and variance error by 39.0% and 34.6% relative to the mixture, and a quote transformer reduces $L^1$ by 16.4% on the structurally misspecified Merton family. A numerical conditioning analysis explains why these rankings can differ: after enforcing mass and forward constraints, 95 of 126 pricing directions are numerically null, and two densities separated by $L^1 = 0.061$ produce identical prices on the covered strikes. On 524 held-out NIFTY calls, validation-selected test-time adaptation reduces DeepONet RMSE by 28.3%, but per-expiry mixture and SVI fits remain much more accurate. The evidence supports target-dependent inductive bias, not a universal winner.

### 🤖 AI 总结

**一句话总结**：Accurate option prices do not imply accurate recovery of the latent risk-neutral density. We study this distinction with two complementary benchmarks. A controlled benchmark exposes simulator-truth de...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Inverse, Learning, Latent, Risk-Neutral, Densities, Irregular, Option

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27188v1) | [下载PDF](https://arxiv.org/pdf/2607.27188v1.pdf)

---

## [21. When Do Learned Diffusion Proposals Help Constraint Solving? A Controlled Study on Continuous Algebraic Systems](https://arxiv.org/abs/2607.27169v1)

**作者**：Quang Bui, Sparsh Roy, Akash Gundimeda 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-29

### 📄 论文摘要

Solving a continuous algebraic constraint system requires two decisions: which values satisfy the constraints, and which structural augmentation renders an unsolvable system solvable. Classical solvers answer the first well and the second only by enumeration. On that discrete decision, a candidate-conditioned repair ranker choosing among K augmentations reaches the exhaustive-search ceiling at a fraction of the calls, outperforming random (0.997 vs 0.236 balanced nonlinear menu accuracy; p < 10^-70; 0.982 +/- 0.006 across seeds) and beating a budget-matched per-candidate probe on accuracy and cost. MARC turns such a system into a factor graph, over which a graph-neural diffusion denoiser proposes assignments, descent on an exact computer-algebra energy polishes them, and an exact symbolic checker certifies solutions. Evaluations of diffusion-based proposals rarely include one control: random multi-start under the same refinement budget. Applied to our system, it sharply curtails what the learned proposal contributes on the value decision. Does it beat random multi-start at choosing satisfying assignments? Only narrowly, in a predictable regime. Across trapped low-dimensional families it ties with random restart, but dominates in high dimension, where random search fails. Once variables couple, the advantage is gone. Since all methods share one polish and one checker, best-of-K random multi-start succeeds with probability exactly 1 - (1 - q(n))^K, where q(n) is single-start reachability; one measured constant, with no free parameters, reproduces the entire curve (mean absolute error 0.012). The favorable regime is not specific to our synthetic families: across eight real-world systems in robotics, positioning, optimization, and algebra, classical multi-start solved all eight, none in the learning-favorable regime. We map the regimes in which learned proposals improve solvers.

### 🤖 AI 总结

**一句话总结**：Solving a continuous algebraic constraint system requires two decisions: which values satisfy the constraints, and which structural augmentation renders an unsolvable system solvable. Classical solver...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, Diffusion, When, Learned, Proposals, Help, Constraint, Solving?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27169v1) | [下载PDF](https://arxiv.org/pdf/2607.27169v1.pdf)

---

## [22. Skillful forecasting of offshore winds from satellite scatterometer constellations](https://arxiv.org/abs/2607.27152v1)

**作者**：Francesco Pinto, Luca Lanzilao, Paco Lopez Dekker 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-29

### 📄 论文摘要

Accurate intraday forecasts of offshore wind are becoming increasingly important for power system operation and the integration of growing shares of offshore wind energy. Operational forecasts rely predominantly on numerical weather prediction (NWP), which is not optimized for lead times of minutes to hours, where initial-condition accuracy dominates forecast skill. Although satellite scatterometer observations are routinely assimilated into NWP, they have not previously been used directly for forecasting. Here we present WindCastNet, the first satellite-based nowcasting framework for offshore wind speed and direction, introducing a new paradigm for intraday forecasting that learns from spatiotemporally irregular satellite observations. WindCastNet predicts offshore wind fields from observations acquired by satellite scatterometer constellations. WindCastNet employs a partial convolutional long short-term memory network that exploits microwave radar observations from the European, Chinese, and Indian scatterometers despite their irregular spatial coverage, asynchronous sampling, and variable revisit times. Spatial observation masks and inter-observation intervals are encoded, while a continuous temporal representation enables forecasts at arbitrary lead times. Evaluated over the North Sea, WindCastNet reduces the root-mean-square error by 23% and 7% relative to the HARMONIE MEPS model at lead times of 1 and 2 h, respectively, and outperforms persistence by 9-15% during the first three forecast hours. Forecast skill decreases under strong-wind conditions and spatially non-uniform flow. These results demonstrate that satellite scatterometer constellations can provide an independent and competitive source of short-term offshore wind forecasts, opening new opportunities for renewable energy forecasting but also broader marine weather applications, including tropical cyclone nowcasting.

### 🤖 AI 总结

**一句话总结**：Accurate intraday forecasts of offshore wind are becoming increasingly important for power system operation and the integration of growing shares of offshore wind energy. Operational forecasts rely pr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Skillful, forecasting, offshore, winds, satellite, scatterometer, constellations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27152v1) | [下载PDF](https://arxiv.org/pdf/2607.27152v1.pdf)

---

## [23. Cost-Sensitive Conformal Prediction and Human-in-the-Loop Abstention for Imbalanced High-Stakes Decision Support: A Multi-Domain Benchmark](https://arxiv.org/abs/2607.27143v1)

**作者**：Manpreet Singh, Akshatha Srikantha, Shyamal Lakhanpal  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-29

### 📄 论文摘要

High-stakes decision systems in credit scoring, fraud detection, healthcare, and industrial safety require reliable uncertainty quantification under severe class imbalance and asymmetric error costs. Standard marginal conformal prediction (CP) provides valid overall coverage guarantees; however, we show that it severely under-covers rare, costly minority classes, with minority-class coverage dropping to as low as 0.5% on certain datasets. To characterize and address this limitation, we conduct a comprehensive benchmark comparing marginal CP, class-conditional (Mondrian) CP, and cost-controlled abstention mechanisms across 15 real-world imbalanced tabular datasets, 7 classification models, 3 probability calibration techniques, and 10 random seeds, resulting in 3,150 experimental runs. Our results show that Mondrian CP restores valid minority-class coverage, achieving an average minority-coverage improvement of 61.7 percentage points over marginal CP (p < 1e-80). Furthermore, combining Mondrian CP with cost-controlled abstention significantly reduces expected decision cost compared with standard decision boundaries, confidence-based rejectors, and risk-controlled rejectors under realistic human review budgets. We further quantify dataset-specific break-even thresholds at which deferring ambiguous instances to human experts becomes cost-effective. These findings provide practical guidance for deploying distribution-free, cost-aware uncertainty quantification in high-stakes decision support systems.

### 🤖 AI 总结

**一句话总结**：High-stakes decision systems in credit scoring, fraud detection, healthcare, and industrial safety require reliable uncertainty quantification under severe class imbalance and asymmetric error costs. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Cost-Sensitive, Conformal, Prediction, Human-in-the-Loop, Abstention, Imbalanced, High-Stakes, Decision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27143v1) | [下载PDF](https://arxiv.org/pdf/2607.27143v1.pdf)

---

## [24. Minimal Markovization via Stable Quotients in Holonomy-Cover Decision Processes](https://arxiv.org/abs/2607.27132v1)

**作者**：Zuyuan Zhang, Yongshan Chen, Mahdi Imani 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-29

### 📄 论文摘要

An agent acting under partial observability must retain a recursively updateable statistic of history that restores the Markov property, but the smallest such statistic is generally unknown. We characterize this minimal Markov sufficient statistic for holonomy-cover decision processes, a structured POMDP class in which the visible dynamics are Markov and every realized visible transition applies a fixed permutation to a hidden mode. In particular, we construct the stable quotient, the coarsest observation-wise abstraction preserving one-step rewards and quotient successors, and prove that the pair of the current observation and stable class forms an exact finite Markov state. When the current class is correctly initialized, exact class tracking requires exactly the minimal memory symbols, in the sense that under reachability and pairwise decision separation at a maximizing observation, no arbitrary finite-memory controller can use fewer. Under resettable diagnostics, nearest-prototype class inference has exponentially decaying error, and a calibrate-then-restart reduction transfers finite-MDP guarantees to the recovered state. The results enable \emph{Holonomy Memory Reinforcement Learning}. It represents memory by the current stable class, updates it through ordered edge transports, identifies local class coordinates when diagnostics are available, and applies a standard finite-MDP RL backbone after synchronization. Experiments recover an exact compression from raw states to quotient states and achieve perfect paired-order accuracy with three decision-time memory states, matching the quotient oracle and outperforming the non-oracle baselines.

### 🤖 AI 总结

**一句话总结**：An agent acting under partial observability must retain a recursively updateable statistic of history that restores the Markov property, but the smallest such statistic is generally unknown. We charac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Minimal, Markovization, via, Stable, Quotients, Holonomy-Cover, Decision, Processes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27132v1) | [下载PDF](https://arxiv.org/pdf/2607.27132v1.pdf)

---

## [25. Voronoi Histograms for Adaptive Vectorization of Expected Persistence Diagrams](https://arxiv.org/abs/2607.27126v1)

**作者**：Kaifeng Zhang, Kai Ming Ting  
**分类**：cs.LG  
**发布时间**：2026-07-29

### 📄 论文摘要

Persistence Diagram (PD) is known to capture point cloud topology effectively, but its computation has high time complexity. Expected Persistence Diagram (EPD) has been developed to reduce the time cost by studying the topology of multiple subsets of a point cloud and it serves as a distribution of topological features. Existing EPD vectorizations often rely on predefined point transformations, such as Gaussian or landscape functions. We study an alternative discretization based on Voronoi histograms, which trades smooth functional approximation for adaptive partition-based counting. We propose to use Voronoi Diagram-based histogram as the vectorization of EPD, without imposing an explicit smooth point transformation model. Under stated separation and normalization conditions, we establish stability bounds and characterize when the histogram representation preserves Wasserstein-scale variation. We demonstrate the effectiveness of our proposed representation on real-world datasets which have significant topological features for classification and dimensionality reduction tasks.

### 🤖 AI 总结

**一句话总结**：Persistence Diagram (PD) is known to capture point cloud topology effectively, but its computation has high time complexity. Expected Persistence Diagram (EPD) has been developed to reduce the time co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Voronoi, Histograms, Adaptive, Vectorization, Expected, Persistence, Diagrams

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27126v1) | [下载PDF](https://arxiv.org/pdf/2607.27126v1.pdf)

---

## [26. Hierarchical Spatio-Temporal Transformer for Coherent Emergency Department Forecasting](https://arxiv.org/abs/2607.27106v1)

**作者**：Filipa Lino, Bárbara Tavares, Carlos Santiago 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-29

### 📄 论文摘要

Emergency Departments (EDs) are critical access points in healthcare systems, yet they face persistent pressure from unpredictable patient demand, seasonal surges, and non-urgent visits. Effective ED planning requires forecasts at multiple decision-making levels: hospitals need local demand estimates for staffing and bed management, regions require forecasts to coordinate healthcare units, and national authorities need system-wide projections for capacity planning. However, most existing approaches forecast ED demand independently at a single level, ignoring the hierarchy linking hospitals, regions, and national systems. This can produce incoherent predictions, where hospital-level forecasts do not aggregate consistently to regional or national demand. We propose HierSTT, a hierarchical Transformer-based framework for coherent multi-level ED forecasting. HierSTT jointly predicts hospital, regional, and national level demand in a single end-to-end model. A Temporal Fusion Transformer captures national dynamics, while spatio-temporal Transformer encoder-decoder modules model regional and hospital demand conditioned on higher-level forecasts. A coherence-aware loss penalizes cross-level inconsistencies during training. We further introduce a nationwide Portuguese ED dataset covering 81 hospitals across 5 regional health administrations, with heterogeneous covariates at each level. Experiments show that HierSTT reduces average WAPE by 32\% relative to the best non-hierarchical deep learning baseline and outperforms all classical hierarchical reconciliation methods, while producing near-coherent predictions across levels. Additional resources associated with this work are available at https://github.com/FilipaLino/HierSTT.

### 🤖 AI 总结

**一句话总结**：Emergency Departments (EDs) are critical access points in healthcare systems, yet they face persistent pressure from unpredictable patient demand, seasonal surges, and non-urgent visits. Effective ED ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hierarchical, Spatio-Temporal, Transformer, Coherent, Emergency, Department, Forecasting, Departments

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27106v1) | [下载PDF](https://arxiv.org/pdf/2607.27106v1.pdf)

---

## [27. Sky sphere representation in language models](https://arxiv.org/abs/2607.27092v1)

**作者**：Aleksandr Berdnikov, Yevgeny Liokumovich  
**分类**：cs.LG  
**发布时间**：2026-07-29

### 📄 论文摘要

We analyze whether language models of size ~100B have a representation of the night sky map that is decodable from their residual stream. We find that most of the considered open-source models do have such a representation, and it often even surfaces to the top principal components on prompts that ask questions like ``what is close to this object in the night sky''. In all but one model this representation showed significant scores in LOO testing, containing up to 65-85% of variance ($R^2$-score) and having median angular error down to $12^\circ-21^\circ$. We verify that our representation is not a simple leak from a correlated flat representation. To our knowledge, this representation is the first example of a curved high-dimensional irreducible feature manifold.   Codes used in the paper are published at https://github.com/l3erdnik/Decodable-sky

### 🤖 AI 总结

**一句话总结**：We analyze whether language models of size ~100B have a representation of the night sky map that is decodable from their residual stream. We find that most of the considered open-source models do have...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Sky, sphere, representation, language, models, analyze, whether

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27092v1) | [下载PDF](https://arxiv.org/pdf/2607.27092v1.pdf)

---

## [28. Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents](https://arxiv.org/abs/2607.27083v1)

**作者**：Yicheng Feng, Yan Zhang, Yan Cheng 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-29

### 📄 论文摘要

As LLM agents increasingly depend on diverse external services such as search engines, databases, and connectors, agent harnesses face a fundamental tool-selection challenge: acquiring too few tools leaves the task under-informed, while too many adds cost, context load, and privacy exposure. Routers and retrievers can rank candidate tools by relevance, but a ranking alone does not determine how many are worth selecting. Existing approaches leave acquisition under heterogeneous costs unaddressed. We formulate this decision as cost-aware marginal decision-focused stopping (CAM-DF) over ranked tool prefixes, with CAM-DF-lite as a compact interpretable variant. We train directly on the offline gap between stopping now and the best continuation: its sign labels the decision, its magnitude weights each error by the payoff at stake. We prove this objective is Bayes-aligned with the stopping target and that score-only rules are suboptimal under heterogeneous costs. We evaluate on 1,343 tasks across five tool-use domains. On $τ$-bench Retail, CAM-DF attains the highest payoff among deployable methods, with gains over a predict-then-threshold baseline across all five ranking sources and two cost regimes. Our approach is state-of-the-art under heterogeneous costs and high cost pressure, with larger gains under weaker rankings. In live execution, CAM-DF exposes the agent to 37\% fewer tools than full access while maintaining comparable task success. The CAM-DF family is a lightweight pre-execution plugin that turns existing tool rankings into lower-cost acquisition decisions without fine-tuning the underlying LLM.

### 🤖 AI 总结

**一句话总结**：As LLM agents increasingly depend on diverse external services such as search engines, databases, and connectors, agent harnesses face a fundamental tool-selection challenge: acquiring too few tools l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Scores, Not, Decisions, Cost-Aware, Stopping, Tool, Acquisition

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27083v1) | [下载PDF](https://arxiv.org/pdf/2607.27083v1.pdf)

---

## [29. Equilibrium Training of Energy-Based Models with Parallel Trajectory Tempering](https://arxiv.org/abs/2607.27077v1)

**作者**：Nicolas Béreux, Aurélien Decelle, Cyril Furtlehner 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-29

### 📄 论文摘要

Energy-Based Models (EBMs) provide an interpretable framework for generative modeling of scientific data, but poor Markov Chain Monte Carlo mixing often limits their reliability. We introduce a training algorithm based on Parallel Trajectory Tempering (PTT), which exploits the continuity of the optimization path to maintain equilibrium sampling throughout learning. This enables stable and fast training on highly multimodal and data-scarce scientific datasets. Combined with reservoir sampling and adaptive optimization, PTT has a computational cost comparable to Persistent Contrastive Divergence, making it a practical replacement for standard training methods. It also provides direct estimates of thermalization times, equilibrium samples from trained models, and accurate log-likelihoods at essentially no additional cost. Experiments on Restricted Boltzmann Machines show that PTT consistently outperforms existing EBM training approaches. On discrete tabular data, it also surpasses state-of-the-art deep generative models, yielding higher-quality samples and greater robustness to overfitting and limited data. Our results make equilibrium maximum-likelihood training of EBMs practical and computationally efficient.

### 🤖 AI 总结

**一句话总结**：Energy-Based Models (EBMs) provide an interpretable framework for generative modeling of scientific data, but poor Markov Chain Monte Carlo mixing often limits their reliability. We introduce a traini...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Equilibrium, Training, Energy-Based, Models, Parallel, Trajectory, Tempering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27077v1) | [下载PDF](https://arxiv.org/pdf/2607.27077v1.pdf)

---

## [30. Single-Beat Cuffless Blood Pressure Estimation Using Ear-PPG and ECG with a Lightweight Hybrid Learning Framework](https://arxiv.org/abs/2607.27076v1)

**作者**：Kindeep K. Dhatt, Tengyue Wu, Hanbang Hua 等 4 位作者  
**分类**：cs.LG, eess.SP, eess.SY  
**发布时间**：2026-07-29

### 📄 论文摘要

Continuous cuffless blood pressure (BP) monitoring remains challenging due to motion artifacts, physiological variability, and the limited robustness of conventional pulse transit time (PTT) models under dynamic conditions. Many prior approaches rely on multi-second windows to stabilize estimation, an assumption that is frequently violated during real-world monitoring with intermittent signal corruption. Here, we show that discriminative BP-related information is preserved at the single-beat level and present a lightweight multi-modal wearable framework for continuous BP estimation. The system integrates synchronized chest electrocardiography (ECG) and ear-clip reflectance photoplethysmography, each co-located with a 6-axis inertial measurement unit to provide motion context. We introduce a hybrid learning architecture in which a one-dimensional convolutional neural network extracts a 64-dimensional embedding from individual PPG beats and fuses it with 30 physiology-grounded features, including PTT statistics and heart rate variability, followed by LightGBM regression. The method was evaluated using a multi-phase stress protocol ($n=10$) and the PulseDB public dataset with subject-disjoint validation. Across 30 independent runs, the model achieved mean absolute errors of $4.02 \pm 0.21$~mmHg for systolic BP and $1.79 \pm 0.05$~mmHg for diastolic BP, corresponding to a 28.2\% reduction in combined MAE relative to baseline models. By enabling beat-wise estimation without long temporal context, this framework supports computationally efficient cuffless BP monitoring suitable for wearable deployment under practical resource constraints. The source code for this work is available at https://github.com/SYMBIOX-Lab/BP-wireless.

### 🤖 AI 总结

**一句话总结**：Continuous cuffless blood pressure (BP) monitoring remains challenging due to motion artifacts, physiological variability, and the limited robustness of conventional pulse transit time (PTT) models un...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Single-Beat, Cuffless, Blood, Pressure, Estimation, Ear-PPG, ECG, Lightweight

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.27076v1) | [下载PDF](https://arxiv.org/pdf/2607.27076v1.pdf)

---

