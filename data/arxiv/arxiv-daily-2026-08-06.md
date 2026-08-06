# arXiv AI 论文日报 | 2026-08-06

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.CL](#csCL) (6 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. CoPlan: A Trustworthy Co-Intelligence Interface for Care Planning through Role-Based Contestable Argument Graphs](https://arxiv.org/abs/2608.05107v1)

**作者**：Hung Truong Thanh Nguyen, Hélène Fournier, Piper Jackson 等 7 位作者  
**分类**：cs.AI, cs.MA, cs.SE  
**发布时间**：2026-08-05

### 📄 论文摘要

AI-supported care planning can help clinicians, patients, caregivers, and care teams coordinate complex decisions across clinical, functional, psychosocial, and environmental needs. However, many AI systems present recommendations as fixed outputs, limiting stakeholders' ability to inspect, challenge, and revise plans when they conflict with clinical judgment, patient values, or real-world feasibility. We present CoPlan - a Co-Intelligent and Contestable Interface for Human-AI Care Planning. CoPlan uses a multi-agent workflow in which specialized AI agents generate candidate interventions and supporting or challenging arguments, while human care planners can accept, reject, modify, or add arguments before final plan generation. Through this design, CoPlan combines co-intelligence, in which humans and AI agents contribute complementary expertise, with contestability, where recommendations remain open to inspection, revision, and justification. We demonstrate CoPlan in an aging-in-place care planning scenario. The system supports adaptive care team recruitment, role-based argument review, final care plan generation, and practical follow-up through scheduling agents. This work contributes a contestable care planning interface and a design framing for trustworthy human-AI care planning that preserves human agency and clinical accountability.

### 🤖 AI 总结

**一句话总结**：AI-supported care planning can help clinicians, patients, caregivers, and care teams coordinate complex decisions across clinical, functional, psychosocial, and environmental needs. However, many AI s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CoPlan, Trustworthy, Co-Intelligence, Interface, Care, Planning, through, Role-Based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05107v1) | [下载PDF](https://arxiv.org/pdf/2608.05107v1.pdf)

---

## [2. ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assignment](https://arxiv.org/abs/2608.05102v1)

**作者**：Yijun Lu, Rui Ye, Jiajun Wang 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-05

### 📄 论文摘要

Long-horizon search agents must make multiple sequential actions (steps) to search, retrieve, verify, and integrate evidence to reach a final answer. However, existing methods for training these agents typically treat all steps within a trajectory uniformly during both supervised fine-tuning (SFT) and reinforcement learning (RL), failing to distinguish useful actions from erroneous or redundant ones. In this paper, we propose Answer-Backtracked Credit Assignment (ABC), a fine-grained credit assignment framework for training long-horizon search agents by converting sparse trajectory-level outcomes into dense step-level supervision that rewards useful actions (even in failed trajectories) while suppressing erroneous or redundant actions. Specifically, given a potentially obscure query and its corresponding ground-truth answer, ABC first performs Answer-Backtracked Clue Recovery, which traces back from the answer to recover intermediate clues required to solve the question. It then applies Clue-Anchored Step Scoring to evaluate each search step against these clues, converting sparse binary outcome supervision into dense step-level rewards. Based on these rewards, we develop ABC-SFT, which reweights the loss of each turn, and ABC-GRPO, which uses the step-level scores as rewards in GRPO. Building on this framework, we train ABSeeker based on Qwen3.5-4B with only 8.5k examples. ABSeeker achieves 37.3% on BrowseComp and 39.1% on BrowseComp-ZH. With context management, the scores further improve to 55.3% and 52.9%, respectively, significantly outperforming same-scale (4B) agents and even matching the performance of larger ones (approximately 30B). These results demonstrate the effectiveness of answer-backtracked step-level credit assignment for training long-horizon search agents.

### 🤖 AI 总结

**一句话总结**：Long-horizon search agents must make multiple sequential actions (steps) to search, retrieve, verify, and integrate evidence to reach a final answer. However, existing methods for training these agent...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, ABSeeker, Training, Long-Horizon, Search, via, Answer-Backtracked, Credit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05102v1) | [下载PDF](https://arxiv.org/pdf/2608.05102v1.pdf)

---

## [3. Item Response Theory for AI Safety](https://arxiv.org/abs/2608.05086v1)

**作者**：Joshua Fonseca Rivera, Neil Shah, David Demitri Africa 等 4 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-08-05

### 📄 论文摘要

Language models differ in how safely they behave and these differences are measured by safety benchmarks. But aggregated benchmark scores are hard to trust and interpret, because benchmarks duplicate one another, correlate heavily, and models may sandbag when they detect evaluation. To address these issues, we draw on Item Response Theory (IRT), a statistical toolkit for measuring these latents from performance on items with inferred psychometric properties. We fit IRT models to eight safety benchmarks across 192 language models, the largest psychometric analysis of LLM safety evaluations to date, and contribute three results. First, we find that three interpretable factors of refusal strictness, truthfulness, and contextual harm explain most of the variance between models across benchmarks. Second, psychometrically selected items recover full benchmark scores with lower error than random subsets of the same size, and roughly ten adaptively chosen items suffice for several individual benchmarks, cutting evaluation cost by 97-99%. Third, IRT supports audits of individual models, showing that it can be used to detect naive sandbagging and changes of model behind APIs. Overall, we show IRT is a ready-made toolkit for reading, reducing, and auditing safety benchmarks, which we recommend frontier labs and evaluators adopt.

### 🤖 AI 总结

**一句话总结**：Language models differ in how safely they behave and these differences are measured by safety benchmarks. But aggregated benchmark scores are hard to trust and interpret, because benchmarks duplicate ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Item, Response, Theory, Safety, Language, models, differ, how

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05086v1) | [下载PDF](https://arxiv.org/pdf/2608.05086v1.pdf)

---

## cs.CL

## [4. Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning](https://arxiv.org/abs/2608.05139v1)

**作者**：Yinghui He, Ling Yang, Jiarui Liu 等 9 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-08-05

### 📄 论文摘要

Long-horizon reasoning in recent LLMs demands that the model switch between distinct skills inside a reasoning chain, such as first doing a math derivation, then using the result to plan a schedule. We call such problems cross-skill long-horizon tasks: multi-step tasks whose steps require different reasoning skills and depend on earlier outputs. Existing benchmarks often evaluate individual skills, lacking a principled way to measure how well a model switches between skills. We address this gap from both the evaluation and training sides. We introduce Skill Entropy, a measure of the difficulty of switching from one skill to another. We then propose Skill^2-Bench, a benchmark of cross-skill long-horizon tasks built over 558 skills across 9 verifiable and open-ended domains. Each task is assigned a task-level skill-entropy score and grouped into three difficulty levels. Evaluating 8 frontier and 4 open-source models on Skill^2-Bench reveals a skill-switching gap: accuracy decreases on higher-entropy tasks. We then turn skill entropy from a benchmark scale into a training signal. We propose Skill-Entropy RL, an RL framework where the model predicts not only the answer at each step but also the skill used to produce it. The reward combines step-level correctness with a skill-entropy reward that measures the alignment between the model-predicted skill sequence and the gold skill sequence. On Qwen3-4B-Instruct and Qwen3-1.7B, Skill-Entropy RL improves the Skill^2-Bench score from 34.4% to 68.4% and from 14.6% to 40.1%, respectively, outperforming competitive baselines. The same pipeline can be applied to off-the-shelf training data such as OpenR1-Math, indicating that skill entropy is a reusable training signal. Code available at: https://github.com/Gen-Verse/Skill-Entropy-RL

### 🤖 AI 总结

**一句话总结**：Long-horizon reasoning in recent LLMs demands that the model switch between distinct skills inside a reasoning chain, such as first doing a math derivation, then using the result to plan a schedule. W...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Toward, Skill-Native, Skill, Entropy, Benchmarking, Training, Long-Horizon

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05139v1) | [下载PDF](https://arxiv.org/pdf/2608.05139v1.pdf)

---

## [5. Spoken Function Calling: A New Perspective on Spoken Language Understanding for Large Audio Language Models](https://arxiv.org/abs/2608.05126v1)

**作者**：Yuezhang Peng, Yuxin Liu, Changfeng Gao 等 6 位作者  
**分类**：cs.CL, cs.MM  
**发布时间**：2026-08-05

### 📄 论文摘要

Spoken Language Understanding (SLU) is the core component of task-oriented dialogue systems and a pivotal link in achieving seamless human-agent interaction. While traditional SLU can effectively extract user semantics for closed-set tasks after in-domain supervised fine-tuning, it faces significant challenges in leveraging in-context learning for open-domain tasks due to its ambiguous rule definitions. This work proposes Spoken Function Calling (SFC), a novel semantic understanding perspective that optimizes semantic understanding with structured rule definitions, to evolve beyond traditional closed-set SLU. Specifically, we curate and extend a suite of spoken functions based on traditional SLU datasets, construct a multi-agent system to synthesize the SFC-Bench dataset, evaluate the performance of Large Language Models (LLMs) and Large Audio Language Models (LALMs), and enhance the SFC capabilities of LALMs through post-training. Experiments demonstrate that SFC outperforms traditional SLU, substantially enhancing the semantic extraction accuracy for LLMs and LALMs.

### 🤖 AI 总结

**一句话总结**：Spoken Language Understanding (SLU) is the core component of task-oriented dialogue systems and a pivotal link in achieving seamless human-agent interaction. While traditional SLU can effectively extr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Spoken, Function, Calling, New, Perspective, Language, Understanding, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05126v1) | [下载PDF](https://arxiv.org/pdf/2608.05126v1.pdf)

---

## [6. Chained Recursive Language Models for Multi-Iteration Reasoning](https://arxiv.org/abs/2608.05124v1)

**作者**：Purbesh Mitra, Sennur Ulukus  
**分类**：cs.CL, cs.AI, cs.IT, cs.LG, eess.SP  
**发布时间**：2026-08-05

### 📄 论文摘要

Long context reasoning in large language models (LLMs) is usually constrained by the fact that a single inference trajectory has to simultaneously explore the context, store intermediate state, verify evidence, and produce the final answer. This becomes particularly difficult in tasks that require extraction, counting, ordering, or multi-hop reasoning, where an early mistake can propagate until the final response. In this work, we propose Chained Recursive Language Models (Chained RLM), an inference-time architecture, in which the same underlying model is called repeatedly as a sequence of fresh reasoning roots. Each root receives the original problem and context, but does not inherit the full conversational history. Instead, it receives a compact plain-text summary, a plain-text blackboard, and some durable task-specific artifacts written by predecessor roots. The motivation is to manage the context by chopping into partial tasks rather than one large inference response; in each staged computation, intermediate artifacts can be inspected, corrected, and extended by a later fresh inference by the same model. We describe the system model, handoff mechanism, artifact workspace, and evaluation protocol for this system. We study when fresh-context artifact continuation gives a measurable gain in accuracy over direct LLM answering even with recursive tool-calling.

### 🤖 AI 总结

**一句话总结**：Long context reasoning in large language models (LLMs) is usually constrained by the fact that a single inference trajectory has to simultaneously explore the context, store intermediate state, verify...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Chained, Recursive, Language, Models, Multi-Iteration, Reasoning, Long, context

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05124v1) | [下载PDF](https://arxiv.org/pdf/2608.05124v1.pdf)

---

## [7. Same Formulas, Different Semantics: Do Language Models Follow Modal Logic Specifications?](https://arxiv.org/abs/2608.05097v1)

**作者**：Réemi Andrieu, Damien Sileo  
**分类**：cs.CL  
**发布时间**：2026-08-05

### 📄 论文摘要

Reasoning about necessity and possibility depends on assumptions about accessibility between worlds and about which objects exist at each one. The same inference may therefore hold under one modal system and fail under another. Evaluating language models on such problems requires testing whether their judgments follow the stated semantics rather than a familiar logic. We construct paired modal problems with identical premises and conjecture but different frame or domain conditions; automated reasoning verifies opposite labels. A balanced core prevents the semantic condition alone from revealing the answer. On this core, four of five recent models perform below the condition-only baseline under direct prompting. Yet enabling reasoning mode raises DeepSeek V4 Flash from 4.4% to 88.1% on unchanged prompts. Following stipulated modal semantics thus depends strongly on inference mode as well as model identity. When frame conditions are omitted, models often agree but fit different familiar logics best. We release the formulas, oracle artifacts, countermodels, and responses.

### 🤖 AI 总结

**一句话总结**：Reasoning about necessity and possibility depends on assumptions about accessibility between worlds and about which objects exist at each one. The same inference may therefore hold under one modal sys...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, Same, Formulas, Different, Semantics, Language, Models, Follow

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05097v1) | [下载PDF](https://arxiv.org/pdf/2608.05097v1.pdf)

---

## [8. German parties shifted towards intuition-based rhetoric after the far right's parliamentary breakthrough](https://arxiv.org/abs/2608.05075v1)

**作者**：Peer Saleth, Segun T. Aroyehun, Fabio Carrella 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-05

### 📄 论文摘要

The spread of misinformation is widely perceived as a threat to democratic deliberation, yet how political elites' rhetorical commitments to truth shift alongside the rise of populist actors remains poorly understood. Analysing 4.5 million tweets and 59,170 parliamentary speeches by German political elites between 2015 and 2025, we measure evidence-based and intuition-based rhetoric using a validated distributed dictionary representation. Across both arenas, intuition-based language has become more prominent, and right-leaning actors consistently exhibit the lowest Evidence Minus Intuition (EMI) scores. The parliamentary entry of the extreme-right Alternative for Germany (AfD) in 2017 coincides with sharp downward shifts in EMI across the broader chamber, while a more gradual decline is observed on Twitter. These findings document an association between far-right visibility and a changing approach to truth in elite discourse in a multiparty European democracy.

### 🤖 AI 总结

**一句话总结**：The spread of misinformation is widely perceived as a threat to democratic deliberation, yet how political elites' rhetorical commitments to truth shift alongside the rise of populist actors remains p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：German, parties, shifted, towards, intuition-based, rhetoric, after, far

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05075v1) | [下载PDF](https://arxiv.org/pdf/2608.05075v1.pdf)

---

## [9. Provable Limits and Certified Deferral for Verbalized Uncertainty in Small Language Models](https://arxiv.org/abs/2608.05064v1)

**作者**：Jianru Shen  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-08-05

### 📄 论文摘要

Small open-weight language models increasingly run in private, offline, and cost-sensitive settings, where the key deployment question is not only what a model answers but when it should defer to a human. We study whether verbalized confidence can support risk-controlled deferral, evaluating eleven instruction-tuned models from three families, 0.5B to 14B parameters, on ARC-Challenge and TruthfulQA with 25,168 local predictions. Three theoretical results delimit what calibration can provide: strictly monotone calibration preserves the risk-coverage frontier and error-detection AUROC; temperature scaling cannot calibrate models whose confidence stays above one half while accuracy falls below it; and a Clopper-Pearson procedure converts a 200-question calibration set into a finite-sample risk certificate under an i.i.d. deployment assumption. Empirically, eight of 22 model-task pairs hit the temperature-scaling infeasibility floor within one percentage point of the predicted bound. Platt scaling reduces ECE to as low as 0.02, yet certified autonomy at a 20% risk budget is granted to only three model-task pairs and to none at 10%. We also identify and repair an answer-ordering artifact in the multiple-choice form of TruthfulQA. Calibration gives confidence semantics; certified deferral determines when small models are safe to use.

### 🤖 AI 总结

**一句话总结**：Small open-weight language models increasingly run in private, offline, and cost-sensitive settings, where the key deployment question is not only what a model answers but when it should defer to a hu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Provable, Limits, Certified, Deferral, Verbalized, Uncertainty, Small, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05064v1) | [下载PDF](https://arxiv.org/pdf/2608.05064v1.pdf)

---

## cs.CV

## [10. CoCo-IR: Contextual Composed Image Retrieval](https://arxiv.org/abs/2608.05149v1)

**作者**：Shengcao Cao, Tanmaya Shekhar Dabral, Zhongli Ding 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-05

### 📄 论文摘要

Current instruction-based image retrieval systems are powerful but limited to single-turn interactions, failing to capture the iterative nature of complex, real-world visual searches. To overcome this limitation, we introduce Contextual Composed Image Retrieval (CoCo-IR), a novel task that enables users to progressively refine search results through interactions. We address this new task by proposing a new model based on a Large Multimodal Model (LMM) that functions as a context-aware reasoner for CoCo-IR. Our model interprets the entire interaction history to generate Transformable Image Embeddings (TIE) that evolve across turns. To fuel the model training without expensive human annotations, we develop a fully autonomous, scalable data engine that leverages LMMs to generate high-quality contextual retrieval data, and uses model-guided verification to mine challenging hard negatives. Extensive experiments demonstrate that our approach establishes new state-of-the-art performance: We achieve 39.4 mAP@5 on the challenging single-turn benchmark CIRCO; furthermore, on our new CoCo-IR benchmark, our model maintains robust performance with 44.1 R@1 on 4-turn dialogues, dramatically outperforming existing methods (28.2 4-turn R@1) that fail to handle multi-turn context. Project page: https://CoCo-IR.github.io.

### 🤖 AI 总结

**一句话总结**：Current instruction-based image retrieval systems are powerful but limited to single-turn interactions, failing to capture the iterative nature of complex, real-world visual searches. To overcome this...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CoCo-IR, Contextual, Composed, Image, Retrieval, Current, instruction-based, systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05149v1) | [下载PDF](https://arxiv.org/pdf/2608.05149v1.pdf)

---

## [11. SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding](https://arxiv.org/abs/2608.05137v1)

**作者**：Yue Zhang, Yingzhao Jian, Yunqiu Xu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-05

### 📄 论文摘要

Understanding 3D scenes is fundamental to embodied intelligence, requiring joint reasoning over heterogeneous information from multiple modalities, including visual and geometric cues. However, the relevance of these modalities often varies across queries. Existing Multimodal Large Language Models (MLLMs) typically rely on fixed modality combinations, overlooking query-dependent modality needs. Such a rigid design can introduce semantic noise from irrelevant modalities while underutilizing more informative ones, leading to wasted computation and diluted reasoning. To address these challenges, this paper proposes SmartMage, a unified MLLM that dynamically orchestrates heterogeneous modalities for semantic-aware 3D scene understanding. Specifically, SmartMage incorporates: (1) a Semantic-guided Modality Adaptive RouTng (SMART) module that selects task-relevant modalities using semantic priors, text-modality alignment, and modality quality; and (2) a Modality-Aware Gating Expert (MAGE) module that leverages modality priors to guide expert activation, fostering adaptive specialization in multimodal reasoning. Empirically, SmartMage achieves state-of-the-art performance across five 3D scene understanding benchmarks, and attains competitive results on RGB-only video understanding benchmarks. In our diagnostic benchmark ScanFacet, tasks are divided into fine-grained semantic categories, enabling analysis of modality combinations preferred by each semantic type. The observed modality-semantic patterns provide further evidence of SmartMage's effectiveness. Project page: https://yuecheong.github.io/SmartMage/.

### 🤖 AI 总结

**一句话总结**：Understanding 3D scenes is fundamental to embodied intelligence, requiring joint reasoning over heterogeneous information from multiple modalities, including visual and geometric cues. However, the re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, SmartMage, Dynamic, Modality, Orchestration, Scene, Understanding, scenes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05137v1) | [下载PDF](https://arxiv.org/pdf/2608.05137v1.pdf)

---

## [12. Predicting Brain Morphometry with MT-GNN: Mesh Evolution in Continuous Time with Graph-Based Metric Tensor Embeddings](https://arxiv.org/abs/2608.05132v1)

**作者**：Hao Ding, Daniel Semchin, Paul M. Thompson 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-08-05

### 📄 论文摘要

Predicting how a subcortical structure's shape will evolve from a few prior scans could support prognosis and clinical-trial enrichment. Existing longitudinal mesh predictors either extrapolate shape trajectories via high-dimensional embeddings or regress vertex deformations directly. We instead predict the surface's intrinsic geometry in continuous time: a single per-structure graph network predicts the future per-vertex first fundamental form (metric tensor) for an arbitrary causal multiple-visit history and an arbitrary prediction horizon, conditioned on a Fourier encoding of the lead time. The predicted metric is decoded into a surface by a differentiable As-Rigid-As-Possible solver, and the model is trained end-to-end on the rigid-aligned vertex error. Training through the reconstruction keeps the decoded prediction a valid surface and consistently improves it. On 14 subcortical structures from the ADNI dataset, the proposed mesh evolution model (MT-GNN) predicts best among the evaluated methods at every horizon ($-2.29\%$ mean vertex error vs. the temporal mean, $p{=}6.1{\times}10^{-5}$, beating it on 14/14 structures), ahead of geodesic shape regression (DCM, $-0.19\%$) and a mesh transformer (TransforMesh, $-0.45\%$; $p{=}1.2{\times}10^{-4}$), with the lead widening as the horizon grows.

### 🤖 AI 总结

**一句话总结**：Predicting how a subcortical structure's shape will evolve from a few prior scans could support prognosis and clinical-trial enrichment. Existing longitudinal mesh predictors either extrapolate shape ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Predicting, Brain, Morphometry, MT-GNN, Mesh, Evolution, Continuous, Time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05132v1) | [下载PDF](https://arxiv.org/pdf/2608.05132v1.pdf)

---

## [13. IRIS: A Visual Cortex-Inspired Framework for Analyzing Orientation Selectivity in Vision Transformers](https://arxiv.org/abs/2608.05122v1)

**作者**：Vaishnavi B Mohan, Vijayakrishna Naganoor, Yashas Annadani 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-05

### 📄 论文摘要

Vision transformers (ViTs) have become the de facto standard for image encoding across many perception tasks. Despite their empirical success, it remains mechanistically unclear how they encode low-level features, given their lack of inductive biases: ViTs process information globally rather than relying on local structure. Biological visual systems, in contrast, build low-level features, such as orientation selectivity in the primary visual cortex, by combining information from small, localized regions of the visual field. These features are general-purpose representations, shared and required across multiple specialized neural pathways, unlike higher-level, task-specific semantic features. This raises the question if such biologically-grounded features arise in ViTs. In this work, we systematically study how orientation selectivity emerges in ViTs by introducing a suite of neuroscience-inspired metrics: representational similarity score (RSS), orientation recruitment score (ORS), and orientation tuning bandwidth to quantify how orientation is encoded in representational geometry and as a function of model depth. Through extensive analysis, we find that: (1) the training paradigm is the strongest determinant of orientation selectivity, with models sharing an objective, peaking at comparable relative depths regardless of scale (2) many units are orientation-selective early in training, with early-to-middle layers recruiting more such units over time, while deeper layers lose selectivity and broaden their tuning toward semantic encoding and (3) our metrics offer a mechanistic heuristic for how many layers to unfreeze for best downstream generalization. Our framework presents a way to track biologically-grounded features during ViT training, probes how desired properties are encoded in transformer representations, and builds a systematic understanding of how ViTs generalize across tasks.

### 🤖 AI 总结

**一句话总结**：Vision transformers (ViTs) have become the de facto standard for image encoding across many perception tasks. Despite their empirical success, it remains mechanistically unclear how they encode low-le...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IRIS, Visual, Cortex-Inspired, Framework, Analyzing, Orientation, Selectivity, Vision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05122v1) | [下载PDF](https://arxiv.org/pdf/2608.05122v1.pdf)

---

## [14. Robust and Efficient Motion Reasoning for Privacy-Aware Classroom Incident Recognition](https://arxiv.org/abs/2608.05115v1)

**作者**：Paritosh Parmar, Landy Lan, Hong Yang 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.ET, cs.HC, cs.LG  
**发布时间**：2026-08-05

### 📄 论文摘要

Can computer vision help make classrooms safer? In this pilot study, we investigate privacy-aware and computationally efficient classroom incident recognition from CCTV-style observations. This setting remains underexplored, with limited benchmarks and few methods designed for the privacy, efficiency, and generalization demands of real-world deployment. We introduce a novel hybrid benchmark combining generative CCTV-style videos with real-world classroom pose data, and propose a lightweight, but robust motion-reasoning framework motivated by the observation that many incidents differ more in motion direction, speed, acceleration, and intensity than in pose alone. To that end, our method first constructs hierarchical kinematic representations of human actions. Our method then distills hierarchical, multi-order kinematic reasoning from a large teacher into a much smaller single-order student, enabling efficient per-person inference while preserving expressive motion understanding. Experiments show that our model outperforms substantially larger baselines at less than one-tenth of their computational cost, while also demonstrating stronger out-of-domain motion reasoning and zero-shot synthetic-to-real generalization. We will publicly release the benchmark, codebase, and supporting tools to facilitate further research in privacy-aware classroom safety.

### 🤖 AI 总结

**一句话总结**：Can computer vision help make classrooms safer? In this pilot study, we investigate privacy-aware and computationally efficient classroom incident recognition from CCTV-style observations. This settin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Robust, Efficient, Motion, Reasoning, Privacy-Aware, Classroom, Incident, Recognition

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05115v1) | [下载PDF](https://arxiv.org/pdf/2608.05115v1.pdf)

---

## [15. Lesion Detection in CT with Frozen Self-Distilled Features: SALT, a Spatially Adaptive Label-Guided Temperature](https://arxiv.org/abs/2608.05100v1)

**作者**：Mahmut S. Gokmen, Evan W. Damron, Mitchell A. Klusty 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-05

### 📄 论文摘要

Self-supervised pretraining objectives are spatially uniform: the teacher temperature and the per-patch loss weight are identical everywhere in the image, so a lesion a few patches wide contributes no more to the training signal than the surrounding parenchyma. Prior work biases the views toward annotated regions, which changes what the model sees but adds no pressure on the objective. We instead condition the targets of self-distillation, a method we call SALT (Spatially Adaptive Label-guided Temperature). Weak, box-derived labels, available only during pretraining, define a compact region on the encoder's patch grid, inside which the teacher's softmax temperature is sharpened and the masked-patch loss is up-weighted. The objectives, the masking policy and the centering statistics are otherwise unchanged, and at every downstream use the encoder is a plain feature extractor with no labels and no conditioning. We evaluate by freezing the encoder and training only a lightweight multi-depth CenterNet-style head, detecting lesions in 3D on four CT cohorts, and we isolate the mechanism against a backbone identical in architecture, pretraining data, schedule and label-guided cropping but with no target conditioning. We report patch-level separability, 3D detection stratified by cohort and by lesion size, box quality, and a detector-free probe in which a single frozen patch embedding re-identifies a lesion in a follow-up scan without registration, masks or fine-tuning. Because the conditioning is expressed through a spatial indicator rather than through label semantics, the formulation admits any weak spatial annotation; we instantiate and validate it for lesions.

### 🤖 AI 总结

**一句话总结**：Self-supervised pretraining objectives are spatially uniform: the teacher temperature and the per-patch loss weight are identical everywhere in the image, so a lesion a few patches wide contributes no...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CT, Lesion, Detection, Frozen, Self-Distilled, Features, SALT, Spatially

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05100v1) | [下载PDF](https://arxiv.org/pdf/2608.05100v1.pdf)

---

## [16. Bag-of-Visual-Words for Spatial Mapping of Lung Adenocarcinoma Growth Patterns](https://arxiv.org/abs/2608.05074v1)

**作者**：Darya Ardan, Valentin Oreiller, Henning Müller  
**分类**：cs.CV  
**发布时间**：2026-08-05

### 📄 论文摘要

Spatial mapping of lung adenocarcinoma (LUAD) growth patterns across whole slide images (WSIs) requires resolving architectural context at the region level, yet existing methods operate at the individual tile level and produce generic morphological clusters rather than clinically defined pattern maps. We propose a weakly supervised Bag-of-Visual-Words (BoVW) pipeline that learns a visual vocabulary from frozen foundation model embeddings extracted from a small set of annotated regions of interest (ROIs). Pattern prototypes are constructed as mean BoVW histograms of same-label ROIs and used for nearest-prototype classification of sliding-window regions under Jensen--Shannon divergence. The resulting predictions are projected onto the WSI tile grid to produce interpretable spatial pattern maps. We evaluate the method on 87 CPTAC-LUAD patients using three foundation model encoders and multiple vocabulary sizes on two clinically motivated tasks. For tumour/healthy classification, the best configuration achieves a balanced accuracy of $0.974$ with H-Optimus-1, approaching the $0.987$ obtained by a supervised SVM trained on mean-pooled WSI embeddings. For binary histologic grade classification, the BoVW pipeline achieves higher balanced accuracy than the supervised baseline for all encoders, suggesting that ROI-level pattern decomposition preserves grade-relevant heterogeneity that is attenuated by global mean pooling.

### 🤖 AI 总结

**一句话总结**：Spatial mapping of lung adenocarcinoma (LUAD) growth patterns across whole slide images (WSIs) requires resolving architectural context at the region level, yet existing methods operate at the individ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Bag-of-Visual-Words, Spatial, Mapping, Lung, Adenocarcinoma, Growth, Patterns

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05074v1) | [下载PDF](https://arxiv.org/pdf/2608.05074v1.pdf)

---

## [17. HelloWorld: Enabling Socially Interactive Characters in Video World Models](https://arxiv.org/abs/2608.05070v1)

**作者**：Liangyang Ouyang, Ruicong Liu, Xuangeng Chu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-05

### 📄 论文摘要

Despite the remarkable recent progress of video world models, social interaction between users and the characters within these worlds remains unsupported. To fill this gap, we present HelloWorld, a video world model that enables social interaction with in-world characters. With a single button press, users can prompt the on-screen character to respond toward the camera, e.g., turning to the viewer, waving, nodding, or speaking a short greeting. To make these interactions natural, we propose a self-distillation pipeline that finetunes the video generation model on data synthesized by itself. Each synthesized clip contains both social interactions and camera motion, allowing the model to learn camera-pose conditioning without degrading interaction quality. At inference, we further introduce a training-free module that determines when the interaction occurs. Upon a button press, it modulates the cross-attention masks of the DiT so that the interaction-related text prompt attends only to the frames within the press window, temporally localizing the character's response. We further build HelloWorldBench, a 400-sample benchmark with three social interaction metrics alongside three conventional metrics, for evaluation. Experiments demonstrate that HelloWorld surpasses a variety of baselines in interaction quality, while maintaining state-of-the-art picture aesthetics and camera-pose following. Project page: https://github.com/AlayaLab/HelloWorld

### 🤖 AI 总结

**一句话总结**：Despite the remarkable recent progress of video world models, social interaction between users and the characters within these worlds remains unsupported. To fill this gap, we present HelloWorld, a vi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HelloWorld, Enabling, Socially, Interactive, Characters, Video, World, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05070v1) | [下载PDF](https://arxiv.org/pdf/2608.05070v1.pdf)

---

## [18. VQ-VAD: Vector-quantized Motion Representation Learning for Human-centric Video Anomaly Detection](https://arxiv.org/abs/2608.05069v1)

**作者**：Narges Rashvand, Ghazal Alinezhad Noghre, Shanle Yao 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-05

### 📄 论文摘要

Video Anomaly Detection (VAD) is inherently challenging due to the scarcity of anomalies and the large visual variability in surveillance footage, including changes in lighting, viewpoint, and human appearance. To mitigate visual noise and address privacy concerns, recent work has shifted to pose-based VAD, which focuses on motion dynamics rather than raw video data. However, existing pose-based approaches model human behavior in continuous latent spaces, limiting their ability to learn compact motion patterns necessary for robust behavior analysis. We address this by proposing Vector-Quantized Video Anomaly Detection (VQ-VAD), a novel human-centric anomaly detection framework that learns discrete motion representations. VQ-VAD adapts Vector-Quantized GAN (VQ-GAN), originally developed for image generation, to operate on keypoint sequences and construct a motion codebook of normal behavior. Trained exclusively on normal motion sequences, VQ-VAD detects anomalies by identifying high reconstruction errors when an observed motion sequence cannot be mapped to the learned codebook. We conduct extensive experiments across three complementary evaluation settings, including in-domain, cross-domain, and cross-dataset generalization, on four anomaly detection benchmarks. VQ-VAD achieves strong in-domain accuracy (81.83% on HR-SHT [15]), effective cross-domain transfer from CMU Panoptic [14] (76.69% on HR-SHT [15] without retraining), and competitive cross-dataset robustness. The code base for this work is available at https://github.com/TeCSAR-UNCC/VQ-VAD.

### 🤖 AI 总结

**一句话总结**：Video Anomaly Detection (VAD) is inherently challenging due to the scarcity of anomalies and the large visual variability in surveillance footage, including changes in lighting, viewpoint, and human a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VQ-VAD, Vector-quantized, Motion, Representation, Learning, Human-centric, Video, Anomaly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05069v1) | [下载PDF](https://arxiv.org/pdf/2608.05069v1.pdf)

---

## [19. Beyond Reprojection Error: Camera Calibration with 3D Targets](https://arxiv.org/abs/2608.05066v1)

**作者**：Dennis Ruppel, Hasan Kutlu, Kai A. Neumann 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-05

### 📄 论文摘要

In 3D reconstruction, camera calibration is an essential element for achieving high fidelity and accuracy of the reconstructed geometry. While existing approaches rely upon 2D planar calibration, this work proposes a framework tailored for 3D reconstruction that is based on predicting scene rays, which adds flexibility to the reconstruction pipeline and enables the use of recent advances in camera models. Novel metrics, reconstruction and intersection error, derived from predicted scene rays are employed in combination with a bootstrapping procedure that statistically evaluates different calibration objects and calibration pipelines for both intrinsic and extrinsic camera parameters. The results show that the generalized distortion model more faithfully captures physical camera effects and yields an improvement in calibration accuracy. Reprojection error is shown to be a potentially misleading indicator of 3D accuracy, and the proposed ray-based metrics provide a more holistic assessment. An icosahedron calibration target is designed to enrich calibration information for 3D reconstruction together with a ring-feature-based detector. The icosahedral target yields approximately 40% lower mean intersection and more stable calibration across bootstrap trials on synthetic data, while real-data performance demands very tight fabrication tolerances.

### 🤖 AI 总结

**一句话总结**：In 3D reconstruction, camera calibration is an essential element for achieving high fidelity and accuracy of the reconstructed geometry. While existing approaches rely upon 2D planar calibration, this...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Beyond, Reprojection, Error, Camera, Calibration, Targets, reconstruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05066v1) | [下载PDF](https://arxiv.org/pdf/2608.05066v1.pdf)

---

## [20. OmniEdit-Bench: A Comprehensive Benchmark for Instruction-based Video Editing](https://arxiv.org/abs/2608.05049v1)

**作者**：Chenxuan Miao, Yutong Feng, Yi Lu 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-05

### 📄 论文摘要

Instruction-based video editing (IVE) is an emerging field with broad applications, yet evaluating editing models remains challenging. Existing benchmarks suffer from two major limitations: limited task coverage inherited from image editing, which overlooks video-specific dimensions, and inadequate metrics that fail to measure instruction fidelity, allowing incorrect edits to receive high scores due to strong visual priors from the original video. To address these issues, we introduce a comprehensive and structured benchmark for IVE. Our benchmark decomposes editing tasks into multiple video-specific dimensions, including spatial, temporal, audio, and reference-based editing, extending beyond conventional frame-level evaluation. It also distinguishes explicit and implicit instructions and incorporates reasoning-based scenarios to better reflect real-world requirements. Furthermore, we propose an evaluation framework that assesses editing quality from four complementary dimensions: accuracy, preservation, realism, and consistency, using both human judgments and state-of-the-art vision-language models. To emphasize instruction fidelity, we introduce an accuracy-aware penalty mechanism that conditions other scores on accuracy, preventing visually plausible but incorrect edits from receiving inflated evaluations. Extensive experiments on representative open-source and commercial models show that current IVE models remain far from satisfactory. OmniEdit-Bench provides a comprehensive and reliable testbed for evaluating instruction-based video editing and offers insights into future research directions.

### 🤖 AI 总结

**一句话总结**：Instruction-based video editing (IVE) is an emerging field with broad applications, yet evaluating editing models remains challenging. Existing benchmarks suffer from two major limitations: limited ta...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, OmniEdit-Bench, Comprehensive, Benchmark, Instruction-based, Video, Editing, IVE

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05049v1) | [下载PDF](https://arxiv.org/pdf/2608.05049v1.pdf)

---

## cs.LG

## [21. The Loss Does Not See the Basis, but Adam Does](https://arxiv.org/abs/2608.05136v1)

**作者**：Devender Singh  
**分类**：cs.LG  
**发布时间**：2026-08-05

### 📄 论文摘要

Gradient descent on a factored model $W = UV^\top$ is implicitly biased toward low-rank solutions, while Adam, starting from the same small initialization, is not. We trace the difference to the gauge symmetry of the loss, its invariance under $(U, V) \mapsto (UQ, VQ)$. Gradient flow's low-rank mechanism is available to an optimizer only if that optimizer is gauge-equivariant, a condition necessary for the transfer but not sufficient for low-rank recovery. Gradient descent, momentum, "shared-scalar" Adam, Muon, and Shampoo satisfy it. Adam, RMSProp, and the other coordinate-wise methods do not. A structure theorem characterizes the memoryless equivariant rules as exactly the Gram-determined left preconditioners, and a transfer theorem carries gradient flow's pathwise properties to common-scalar flows. We then sort nine update rules on underdetermined matrix sensing by recovery error against the planted ground truth. A one-parameter family from coordinate-wise to shared-scalar preconditioning restores the bias monotonically, isolating anisotropy as the cause. A "spectral schedule" reconciles two opposing reports about Muon: equal-rate updates recover exactly low-rank targets but lose their edge as the spectral tail grows. In transformers, Adam separates two gauge-equivalent initializations at the first step, where the equivariant optimizers stay at float precision, and ends with the per-head invariants $W_Q^\top W_K$ 56% apart in relative Frobenius distance, a gap no per-head rotation can close. On two hyperspectral datasets at matched training loss, gradient descent cuts held-out error by 43-44% at the lowest sampling density, and at lower effective rank. Basis choice is therefore not a tuning detail but a decision about which interpolant the optimizer selects.

### 🤖 AI 总结

**一句话总结**：Gradient descent on a factored model $W = UV^\top$ is implicitly biased toward low-rank solutions, while Adam, starting from the same small initialization, is not. We trace the difference to the gauge...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Loss, Does, Not, See, Basis, but, Adam, Gradient

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05136v1) | [下载PDF](https://arxiv.org/pdf/2608.05136v1.pdf)

---

## [22. SSTQ:Privacy-Preserving Vector Quantization via Subsampled Stochastic TurboQuant](https://arxiv.org/abs/2608.05127v1)

**作者**：Adel Javanmard, David P. Woodruff, Vahab Mirrokni  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-08-05

### 📄 论文摘要

Achieving local differential privacy in distributed optimization while maintaining low communication cost remains challenging. Existing vector quantization methods, such as vqSGD, use high-dimensional geometric constructions but incur unfavorable dimension-dependent variance. In this work, we propose Subsampled Stochastic TurboQuant (SSTQ), a framework that combines overcomplete equal-norm tight frames, coordinate subsampling, and privacy-aware one-dimensional quantization. SSTQ includes two variants: a Flat Randomized Response version and a Metric-Aware Laplace version, the latter being better suited to higher codebook bit-width regimes. We show that SSTQ achieves optimal mean squared error scaling while using only $\lceil \log_2 N \rceil + b$ bits per client, where $N = Θ(d)$ is the frame size. We also derive a surrogate privacy-aware codebook objective that reduces the codebook-dependent MSE scaling from $O(4^b)$ to $O(2^b)$. Finally, we empirically evaluate SSTQ against established baselines on federated learning tasks using CIFAR-10 and Fashion-MNIST, demonstrating favorable utility and communication efficiency.

### 🤖 AI 总结

**一句话总结**：Achieving local differential privacy in distributed optimization while maintaining low communication cost remains challenging. Existing vector quantization methods, such as vqSGD, use high-dimensional...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SSTQ, Privacy-Preserving, Vector, Quantization, via, Subsampled, Stochastic, TurboQuant

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05127v1) | [下载PDF](https://arxiv.org/pdf/2608.05127v1.pdf)

---

## [23. DASyR-LLM: Domain-Aware Symbolic Regression with LLMs for Kinetic Model Discovery](https://arxiv.org/abs/2608.05120v1)

**作者**：Roberto Aliaga Medina, Paulina Quintanilla, Antonio del Rio Chanona  
**分类**：cs.LG, cs.CE, cs.SC  
**发布时间**：2026-08-05

### 📄 论文摘要

Kinetic model discovery is a central challenge in chemical engineering, as accurate rate expressions are essential for understanding and controlling chemical and biological processes. Symbolic regression (SR) has emerged as a powerful data-driven approach for identifying interpretable kinetic models, but usually operates without domain knowledge, often exploring physicochemically implausible models. Large language models (LLMs) offer a promising avenue for injecting domain expertise into this search. Here, we introduce an LLM-guided SR framework, embedding an LLM module within an iterative SR algorithm for automated kinetic model discovery. The LLM performs two roles at each iteration: (1) a qualitative physicochemical critique of the best SR candidates, and (2) the proposal of new candidate rate expressions guided by the SR-generated models and embedded chemical knowledge. Our framework is evaluated on four in silico case studies of increasing complexity, spanning heterogeneous catalysis and bioprocess systems. Results show the LLM-guided framework reduces iterations to identify the ground-truth model by $41.7-79.3\%$ versus a state-of-the-art SR framework, with the LLM directly proposing the correct model structure in over half of the guided runs. In practical settings, where each iteration typically requires a new wet-lab experiment, this translates into a substantial reduction in experimental effort. Predictive performance on an independent validation set is equivalent between both approaches, with $R^2>0.98$ in all case studies. Ablation studies indicate that both the SR component and the LLM scale contribute to this performance, with a reduced-size LLM largely retaining discovery efficiency. These findings demonstrate that LLMs can effectively inject domain knowledge into scientific model discovery, paving the way toward fully automated, domain-aware kinetic modelling pipelines.

### 🤖 AI 总结

**一句话总结**：Kinetic model discovery is a central challenge in chemical engineering, as accurate rate expressions are essential for understanding and controlling chemical and biological processes. Symbolic regress...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, DASyR-LLM, Domain-Aware, Symbolic, Regression, Kinetic, Model, Discovery

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05120v1) | [下载PDF](https://arxiv.org/pdf/2608.05120v1.pdf)

---

## [24. Reward Structure Shapes the Interaction Between Episodic Exploration and Neural Memory in Reinforcement Learning](https://arxiv.org/abs/2608.05111v1)

**作者**：Jai Malegaonkar, Rohan Patil, Henrik I. Christensen  
**分类**：cs.LG  
**发布时间**：2026-08-05

### 📄 论文摘要

In partially observable reinforcement learning, agents face a dual bottleneck: they must explore to encounter rewarding states and retain that experience in memory to optimize their policies. Exploration bonuses and memory architectures are traditionally evaluated in isolation, leaving their interaction unmeasured, and standard notions of sparse reward conflate temporal signal density with what the reward actually supervises. We present a controlled study crossing episodic exploration bonuses with diverse neural memory architectures across three environments that vary how the content of memory is acquired. An identical bonus signal yields three distinct interaction patterns: it amplifies architectural capacity differences where memory content must be actively discovered and retained unsupervised; equalizes architectures to a shared ceiling where the content, once sought out, is a single reward-supervised cue; and is null where the observation stream is purely scheduled. Controlled reward manipulations verify that these patterns track reward structure rather than density: a dense reward neutralizes a bonus only if it directly supervises the required latent memory, and a small avoidable penalty on exploratory actions (leaving the optimum unchanged) induces policy convergence to suboptimal stationary states, which either bonus resolves. We then formalize reward sparsity with observation-anchored reward machines, separating structural sparsity (an automaton reproduces the return without the task-required history) from potential sparsity (the one-step reward misprices local exploratory actions); the resulting vocabulary organizes the three regimes by the retention burden each task exposes. Together, these results show exploration and memory are complements, not substitutes: a bonus induces exposure, and only memory converts exposure into return.

### 🤖 AI 总结

**一句话总结**：In partially observable reinforcement learning, agents face a dual bottleneck: they must explore to encounter rewarding states and retain that experience in memory to optimize their policies. Explorat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Reward, Structure, Shapes, Interaction, Between, Episodic, Exploration, Neural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05111v1) | [下载PDF](https://arxiv.org/pdf/2608.05111v1.pdf)

---

## [25. BnBERT-iPET: Sparse Few-Shot Language Modeling for Bengali via Lottery Ticket Pruning](https://arxiv.org/abs/2608.05104v1)

**作者**：Sajib Hossain, Md Kamrus Samad, Anan Ghosh 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-05

### 📄 论文摘要

Deep neural networks have shown impressive success in NLP tasks owing to their complex structure and huge number of edges. Achieving state-of-the-art performance in natural language processing with a large pre-trained model such as BERT is expensive and time-consuming, carries a large carbon footprint, and is difficult to realize on machines with minimal computational capability. This creates a barrier to training complex models for resource-constrained languages such as Bengali. However, in a complex neural model, not all edges are equally impactful, and the contributions of some of them can be neglected. Pruning promises to reduce the memory footprint of regular networks, shorten the training time of ever-growing networks, and increase inference efficiency without sacrificing comparable performance. In this work, we introduce BnBERT-iPET, a sparse few-shot language modeling approach for Bengali, and experimentally show that a lightweight few-shot-learned language model retaining only 10% of the edges of an initial model such as BERT can perform neck and neck with much larger models on challenging tasks for a resource-constrained language such as Bengali. By learning from few shots through iterative pattern exploiting training and achieving 90% sparsity with the Lottery Ticket Hypothesis pruning technique, our pruned BnBERT-iPET model proves to be a tough competitor to state-of-the-art language models such as Bangla Electra, Indic-BERT, and XLM-RoBERTa on downstream tasks over standard benchmark datasets of the Bengali language.

### 🤖 AI 总结

**一句话总结**：Deep neural networks have shown impressive success in NLP tasks owing to their complex structure and huge number of edges. Achieving state-of-the-art performance in natural language processing with a ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BnBERT-iPET, Sparse, Few-Shot, Language, Modeling, Bengali, via, Lottery

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05104v1) | [下载PDF](https://arxiv.org/pdf/2608.05104v1.pdf)

---

## [26. Multimodal Spatiotemporal Atmospheric Data Assimilation with Latent Flow-matching](https://arxiv.org/abs/2608.05103v1)

**作者**：Dibyajyoti Chakraborty, Romit Maulik  
**分类**：cs.LG, math-ph, physics.ao-ph, physics.flu-dyn  
**发布时间**：2026-08-05

### 📄 论文摘要

Data assimilation (DA) uses Bayesian inference to update the state of a numerical forecast model with observed data. In this study, we propose a fundamentally different, unified approach to atmospheric data assimilation. We use latent video flow-matching to sample temporally consistent trajectories from a prior trained using ERA5 reanalysis (69 variables over an 8-day window). We also use posterior sampling to assimilate real observation sources, such as those from the NOAA Integrated Global Radiosonde Archive and the Integrated Surface Database. Because the prior generates a continuous trajectory, it naturally propagates information between observed and unobserved frames. Therefore, we can perform various DA tasks, such as filtering and smoothing, simply by changing the observed frames. Moreover, we generate full-state ensemble forecasts directly from sparse observations, achieving performance competitive with state-of-the-art observation-to-forecast models.

### 🤖 AI 总结

**一句话总结**：Data assimilation (DA) uses Bayesian inference to update the state of a numerical forecast model with observed data. In this study, we propose a fundamentally different, unified approach to atmospheri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DA, Multimodal, Spatiotemporal, Atmospheric, Data, Assimilation, Latent, Flow-matching

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05103v1) | [下载PDF](https://arxiv.org/pdf/2608.05103v1.pdf)

---

## [27. MALT: Lightweight Curvature-Aware Muon via Diagonal Preconditioning](https://arxiv.org/abs/2608.05088v1)

**作者**：Tongle Wu, Huanyu Dong, Ying Sun 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-05

### 📄 论文摘要

Muon has recently emerged as a promising alternative to AdamW for language model pretraining by orthogonalizing momentum matrices using Newton-Schulz iterations. Although Muon mitigates gradient anisotropy, it does not explicitly account for the curvature geometry of the loss landscape and may therefore remain sensitive to curvature anisotropy. We bridge this gap by proposing MALT (Muon Augmented by Lightweight Two-sided Preconditioning), which uses lightweight diagonal preconditioners to reduce the sensitivity of Muon to curvature anisotropy. Specifically, MALT uses two-sided diagonal preconditioners with low memory and computational overhead to approximately capture the curvature geometry of the loss landscape. It orthogonalizes the preconditioned momentum using Newton-Schulz iterations and maps the result back to define the update direction, while norm grafting controls the update magnitude. To improve the robustness of MALT to stochastic gradient noise, we further propose MALTER (MALT with Adaptive stEpsize Rescaling). Convergence guarantees are provided for MALT in the stochastic non-convex setting. Experiments on GPT-2 Small, Medium, and Large pretraining show that the proposed methods outperform Muon while maintaining nearly the same memory footprint and wall-clock time.

### 🤖 AI 总结

**一句话总结**：Muon has recently emerged as a promising alternative to AdamW for language model pretraining by orthogonalizing momentum matrices using Newton-Schulz iterations. Although Muon mitigates gradient aniso...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MALT, Lightweight, Curvature-Aware, Muon, via, Diagonal, Preconditioning, has

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05088v1) | [下载PDF](https://arxiv.org/pdf/2608.05088v1.pdf)

---

## [28. Capability-Gated Planning: Cost-to-Goal Discovery and the Limits of Myopic Experiment Selection](https://arxiv.org/abs/2608.05085v1)

**作者**：Ahmed Hassoon, Mark Dredze  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-05

### 📄 论文摘要

Systems that automate scientific discovery must repeatedly decide which experiment to run, which hypothesis to test, which tool to build, and when to stop. Many systems make these decisions by maximizing a myopic score such as expected information gain per unit cost or a learned plausibility score. We identify a structural limitation of this approach. Some actions are constructive: they acquire an epistemic capability (an instrument, assay, pipeline, simulator, or abstraction) whose value lies not in the information returned immediately but in the future actions it makes available. When the least-cost route to a confident answer requires a chain of such constructions, a planner that scores actions only by information obtainable within a bounded horizon cannot value the first construction: it yields no information within the horizon and is dominated by any measurement with positive information, however small. We formulate goal-directed discovery as a stochastic shortest-path problem in belief space in which constructive experiments change the downstream action graph, and prove that for every lookahead depth d there is an instance on which every myopic information-maximizing planner has an unbounded approximation ratio, and a related instance on which it never reaches the goal. The mechanism is a capability-indistinguishability lemma: within the horizon, acquiring a capability can be observationally indistinguishable from paying for a null action. This establishes capability gating as a reachability axis of difficulty distinct from curvature (submodularity) and information order (adaptivity gaps). We introduce CG-Plan, an incremental replanner with a capability-aware cost-to-go heuristic h = h_cap + h_exp. In a controlled testbed, the performance gap appears only under gating, persists for every fixed horizon, and arises when near-miss hypotheses come from a data-consistent proposer.

### 🤖 AI 总结

**一句话总结**：Systems that automate scientific discovery must repeatedly decide which experiment to run, which hypothesis to test, which tool to build, and when to stop. Many systems make these decisions by maximiz...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Capability-Gated, Planning, Cost-to-Goal, Discovery, Limits, Myopic, Experiment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05085v1) | [下载PDF](https://arxiv.org/pdf/2608.05085v1.pdf)

---

## [29. Learning When to Stop: Prefix-Optimal Dynamic Diffusion Policies for Continuous Control](https://arxiv.org/abs/2608.05084v1)

**作者**：Rohit Kumar Salla, Manoj Saravanan, Simon Stepputtis  
**分类**：cs.LG, cs.RO  
**发布时间**：2026-08-05

### 📄 论文摘要

Diffusion policies are a powerful policy class for continuous control, but their iterative denoising process creates a substantial computational bottleneck. Reducing this cost requires adapting the number of denoising steps to the difficulty of each action while preserving task performance. We introduce Prefix-Optimal Generative Policies (POGP), a framework that learns a prefix value function at every intermediate denoising step through a Bellman-style recursion over the denoising chain. The prefix value function serves two purposes: it provides an auxiliary training objective that encourages intermediate outputs to become high-quality actions, and it enables a test-time stopping rule that terminates denoising when additional steps are unlikely to produce meaningful improvement. Across four MuJoCo environments and comparisons with 12 baselines, POGP reduces the required number of denoising iterations by approximately 2.7-fold while retaining near-full task performance. Compared with state-of-the-art dynamic diffusion baselines, prefix training also improves final task performance by approximately 3.5%. These results indicate that supervising intermediate denoising steps is useful not only for adaptive early stopping, but also as an auxiliary objective that improves the learned policy.

### 🤖 AI 总结

**一句话总结**：Diffusion policies are a powerful policy class for continuous control, but their iterative denoising process creates a substantial computational bottleneck. Reducing this cost requires adapting the nu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Learning, When, Stop, Prefix-Optimal, Dynamic, Policies, Continuous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05084v1) | [下载PDF](https://arxiv.org/pdf/2608.05084v1.pdf)

---

## [30. Optimizing What Policies Learn From: Recoverability-aware Rollout Intervention Learning](https://arxiv.org/abs/2608.05080v1)

**作者**：Zheyuan Zhang, Manqing Mao, Hong Wang 等 11 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-08-05

### 📄 论文摘要

Critic-free group-based reinforcement learning has become a scalable approach for post-training large language models. However, most existing methods allocate the same number of rollouts to every task and trajectory state, even though some rollouts provide much more useful learning signals than others. Recent work has started to treat rollout generation as an adaptive decision, but two important limitations remain. First, intervention strategies are often based on fixed heuristics and therefore cannot adjust as the policy changes during training. Second, these methods usually decide only how many rollouts to generate, without explicitly controlling where and how to intervene. To address these limitations, we propose Recoverability-Aware Intervention Learning (RAIL), a training-time framework that learns how to generate rollouts based on the improvement produced by each intervention. RAIL models intervention selection as an online contextual-bandit problem and trains a recoverability controller using intervention traces collected through a shadow-to-live procedure. This allows the controller to keep learning while the underlying policy evolves. We evaluate RAIL in terms of effectiveness, adaptivity, expressiveness, and efficiency. Across multiple settings, RAIL consistently improves performance under limited rollout budgets. These results show that recoverability-aware intervention provides a principled way to generate more informative and less redundant rollouts, leading to stronger learning signals during post-training.

### 🤖 AI 总结

**一句话总结**：Critic-free group-based reinforcement learning has become a scalable approach for post-training large language models. However, most existing methods allocate the same number of rollouts to every task...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Optimizing, What, Policies, Learn, Recoverability-aware, Rollout, Intervention, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.05080v1) | [下载PDF](https://arxiv.org/pdf/2608.05080v1.pdf)

---

