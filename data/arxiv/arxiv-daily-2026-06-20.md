# arXiv AI 论文日报 | 2026-06-20

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (15 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.CL](#csCL) (2 篇)

---

## cs.AI

## [1. Toward Calibrated Mixture-of-Experts Under Distribution Shift](https://arxiv.org/abs/2606.20544v1)

**作者**：Gina Wong, Drew Prinster, Suchi Saria 等 5 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-06-18

### 📄 论文摘要

Calibration aligns a model's predictive uncertainty with the frequencies of its empirical outcomes and is important for understanding and trusting reported probabilities. Recent work shows that enforcing calibration at the level of individual predictors can improve ensemble accuracy and calibration, with mixture-of-experts (MoE) models showing strong empirical improvements in particular; however, the conditions under which calibration helps MoE are not well understood. In this work, we study how MoE models behave under distribution shift, focusing on how routing mechanisms interact with expert-level calibration. We show that expert calibration is sufficient to ensure calibration of the overall model under a broad class of distribution shifts in hard-routed models, but is insufficient for calibrating soft-routed models. To address this, we propose an adversarial reweighting that penalizes calibration errors of the routed aggregate under distribution shift, and we demonstrate that it improves the accuracy-calibration tradeoff both on average and on difficult subsets of the data, across model classes, prediction tasks, and distribution shifts.

### 🤖 AI 总结

**一句话总结**：Calibration aligns a model's predictive uncertainty with the frequencies of its empirical outcomes and is important for understanding and trusting reported probabilities. Recent work shows that enforc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Toward, Calibrated, Mixture-of-Experts, Under, Distribution, Shift, Calibration, aligns

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20544v1) | [下载PDF](https://arxiv.org/pdf/2606.20544v1.pdf)

---

## [2. LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents](https://arxiv.org/abs/2606.20529v1)

**作者**：Md Nayem Uddin, Amir Saeidi, Eduardo Blanco 等 4 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-06-18

### 📄 论文摘要

Policy-adherent tool-calling agents in customer-service domains must maintain task states across turns while calling tools and obeying domain policies. Task states consist of relevant facts, identifiers, constraints, and conditions observed through user interaction and tool calls. In standard agents, task states are not represented separately. Observations, tool returns, and policy instructions are placed in the prompt, leaving agents to reconstruct the relevant states from the prompt each time they decide what to do next. This design makes state management implicit, creating two common failure modes. An agent may retrieve the right facts but later ground its decision in stale, missing, or incorrect information; and a syntactically valid tool call may still violate a domain policy that depends on the current task state. We introduce \textsc{LedgerAgent}, an inference-time method for tool-calling agents that maintains observed task states in a separate ledger and renders the states into the prompt. The ledger is also used to check state-dependent policy constraints before environment-changing tool calls are executed, blocking policy violations. Across four customer-service domains and a mixed panel of open- and closed-weight models, \textsc{LedgerAgent} improves average pass\textasciicircum{}k over a standard prompt-based tool-calling approach, with the largest gains under stricter multi-trial consistency metrics.

### 🤖 AI 总结

**一句话总结**：Policy-adherent tool-calling agents in customer-service domains must maintain task states across turns while calling tools and obeying domain policies. Task states consist of relevant facts, identifie...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, LedgerAgent, Structured, State, Policy-Adherent, Tool-Calling, customer-service, domains

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20529v1) | [下载PDF](https://arxiv.org/pdf/2606.20529v1.pdf)

---

## [3. DeepSWIP: Quotient-WMC Counterfactuals for Neural Probabilistic Logic Programs](https://arxiv.org/abs/2606.20526v1)

**作者**：Saimun Habib, Vaishak Belle, Fengxiang He  
**分类**：cs.AI  
**发布时间**：2026-06-18

### 📄 论文摘要

Neurosymbolic systems such as DeepProbLog combine neural perception with probabilistic logic, but standard inference is associational. Counterfactual reasoning additionally requires a causal semantics for interventions and evidence. We introduce DeepSWIP, a single-world counterfactual semantics for DeepProbLog programs. Using neural materialization, we reduce fixed-context neural predicates to ordinary ProbLog choices, apply Single World Intervention Programs (SWIPs), and compute counterfactuals by weighted model counting (WMC) over a single transformed program. Under finite grounding and unique-supported-model assumptions, DeepSWIP is exact relative to the learned materialized FCM. The standard quotient-WMC form of ProbLog conditionals identifies active neural probabilities and explains intervention cleaning, calibration sensitivity, and rare-evidence instability. Experiments on MPI3D confirm the transformation against a DeepTwin construction against 12,000 queries, as predicted and a 2.14$\times$ inference speedup from avoiding the Twin's endogenous duplication. A SUMO HOV experiment shows that neural calibration degradation biases plug-in estimates, while a correctly scoped randomized-policy AIPW estimator removes most first-order bias for population mean and ATE estimands. Code is at https://github.com/saibib/deep_SWIP.

### 🤖 AI 总结

**一句话总结**：Neurosymbolic systems such as DeepProbLog combine neural perception with probabilistic logic, but standard inference is associational. Counterfactual reasoning additionally requires a causal semantics...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DeepSWIP, Quotient-WMC, Counterfactuals, Neural, Probabilistic, Logic, Programs, Neurosymbolic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20526v1) | [下载PDF](https://arxiv.org/pdf/2606.20526v1.pdf)

---

## [4. Multi-LCB: Extending LiveCodeBench to Multiple Programming Languages](https://arxiv.org/abs/2606.20517v1)

**作者**：Maria Ivanova, Pavel Zadorozhny, Rodion Levichev 等 8 位作者  
**分类**：cs.AI, cs.PL  
**发布时间**：2026-06-18

### 📄 论文摘要

LiveCodeBench (LCB) has recently become a widely adopted benchmark for evaluating large language models (LLMs) on code-generation tasks. By curating competitive programming problems, constantly adding fresh problems to the set, and filtering them by release dates, LCB provides contamination-aware evaluation and offers a holistic view of coding capability. However, LCB remains restricted to Python, leaving open the question of whether LLMs can generalize across the diverse programming languages required in real-world software engineering.   We introduce Multi-LCB, a benchmark for evaluating LLMs across twelve programming languages, including Python. Multi-LCB transforms Python tasks from the LCB dataset into equivalent tasks in other languages while preserving LCB's contamination controls and evaluation protocol. Because it is fully compatible with the original LCB format, Multi-LCB will automatically track future LCB updates, enabling systematic assessment of cross-language code generation competence and requiring models to sustain performance well beyond Python.   We evaluated 24 LLMs for instruction and reasoning on Multi-LCB, uncovering evidence of Python overfitting, language-specific contamination, and substantial disparities in multilingual performance. Our results establish Multi-LCB as a rigorous new benchmark for multi-programming-language code evaluation, directly addressing LCB's primary limitation and exposing critical gaps in current LLM capabilities.

### 🤖 AI 总结

**一句话总结**：LiveCodeBench (LCB) has recently become a widely adopted benchmark for evaluating large language models (LLMs) on code-generation tasks. By curating competitive programming problems, constantly adding...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-LCB, Extending, LiveCodeBench, Multiple, Programming, Languages, LCB, has

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20517v1) | [下载PDF](https://arxiv.org/pdf/2606.20517v1.pdf)

---

## [5. What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations?](https://arxiv.org/abs/2606.20508v1)

**作者**：Sihui Dai, Mann Patel  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-06-18

### 📄 论文摘要

Prior work has shown that in-context demonstrations can jailbreak language models, but it remains unclear how models interpret different types of compliance demonstrations. We study this by mixing benign compliance demonstrations (non-harmful request, helpful response) with harmful compliance demonstrations (harmful request, helpful response) and testing three hypotheses about how demonstration composition drives harmful compliance. Across four models, we find that benign and harmful demonstrations are not interchangeable: benign demonstrations can either reduce or increase harmful compliance depending on the model. We further show that preference optimization is the critical training stage that prevents benign demonstrations from increasing harmful compliance, that demonstration ordering exhibits strong recency bias, and that models differ in how refusal interacts with in-context learning: some adopt demonstrated formatting even when refusing, while others override all in-context signals upon refusal. Taken together, this work moves beyond showing that demonstration-based jailbreaking works to characterizing how it works: what models extract from compliance demonstrations depends on demonstration content, ordering, and training methodology.

### 🤖 AI 总结

**一句话总结**：Prior work has shown that in-context demonstrations can jailbreak language models, but it remains unclear how models interpret different types of compliance demonstrations. We study this by mixing ben...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, LLM, What, Safety-Aligned, Learn, Mixed, Compliance, Demonstrations?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20508v1) | [下载PDF](https://arxiv.org/pdf/2606.20508v1.pdf)

---

## [6. Context-Aware Hierarchical Bayesian Modeling of IVF Laboratory Environmental Conditions](https://arxiv.org/abs/2606.20459v1)

**作者**：Zahra Asghari Varzaneh, Reza Khoshkangini, Pia Saldeen 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-18

### 📄 论文摘要

IVF pregnancy rates are routinely modeled using patient-level variables, while high-resolution laboratory environmental data remain underutilized. We show that this is a missed opportunity. Rather than relying on raw sensor averages, we engineer 55 context-aware temporal features, including rolling thermal stability, simultaneous temperature-humidity adherence, peak stress duration, and post-stress recovery speed, that capture the dynamics of incubator microenvironments. On 61 weeks of data from an Asian IVF clinic, these features reduce cross-validated prediction error to 1.27%, compared to 3-5% for raw averages. We then train a hierarchical Bayesian Beta regression model that shares environmental effects across an Asian and a Northern European clinic via partial pooling, while preserving site-specific baselines. On held-out data from the Northern European clinic, the model achieves R2 = 0.86 and a 64% error reduction for the 35-39 age group over a naive baseline, demonstrating that structured environmental monitoring contains clinically meaningful, transferable signal.

### 🤖 AI 总结

**一句话总结**：IVF pregnancy rates are routinely modeled using patient-level variables, while high-resolution laboratory environmental data remain underutilized. We show that this is a missed opportunity. Rather tha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Context-Aware, Hierarchical, Bayesian, Modeling, IVF, Laboratory, Environmental

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20459v1) | [下载PDF](https://arxiv.org/pdf/2606.20459v1.pdf)

---

## cs.CL

## [7. StylisticBias: A Few Human Visual Cues Drive Most Social Biases in MLLMs](https://arxiv.org/abs/2606.20527v1)

**作者**：Shaghayegh Kolli, Timo Cavelius, Nafiseh Nikeghbal 等 5 位作者  
**分类**：cs.CL, cs.CV  
**发布时间**：2026-06-18

### 📄 论文摘要

Multimodal large language models (MLLMs) are increasingly deployed in personally and societally consequential settings, yet the visual cues that shape how these models judge people remain poorly understood. Prior work often compares different (groups of) individuals, making it difficult to separate appearance effects from identity differences. We introduce StylisticBias, a controlled benchmark for evaluating attribute-level social bias in MLLMs. We generate 500 photorealistic base faces and create about 50 single-attribute variations per face, producing about 25K images. This design keeps identity fixed and changes one visual attribute at a time. It lets us measure how specific cues shift model judgments. We evaluate six MLLMs across 25 binary social judgment scenarios. We find that age and body type dominate identity-level effects, while fashion style and other visual cues drive the largest attribute-level shifts. We further find that about 15 attributes account for nearly 80\% of the total variation, showing that bias is concentrated in a small set of visual cues. Sensitivity is strongest in judgments that are semantically aligned with appearance, especially socioeconomic and style-related judgments. We release StylisticBias as a benchmark for fine-grained bias evaluation in multimodal models. Code and dataset: https://github.com/timo-cavelius/StylisticBias and https://hf.co/datasets/shaghayegh/stylistic-bias-dataset.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) are increasingly deployed in personally and societally consequential settings, yet the visual cues that shape how these models judge people remain poorly under...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：StylisticBias, Few, Human, Visual, Cues, Drive, Most, Social

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20527v1) | [下载PDF](https://arxiv.org/pdf/2606.20527v1.pdf)

---

## [8. Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users](https://arxiv.org/abs/2606.20482v1)

**作者**：Haw-Shiuan Chang, Jeffrey Gomez, Mehul Patwari 等 5 位作者  
**分类**：cs.CL, cs.HC, cs.LG  
**发布时间**：2026-06-18

### 📄 论文摘要

To align a Large Language Model (LLM), most existing methods collect explicit human feedback and train a reward model to predict the human preference based on the response text. These existing methods have two key limitations. First, the users rarely provide explicit feedback for LLM responses, which makes the high-quality preference annotation expensive to collect. Second, the methods do not leverage implicit human feedback, which has proven vital to the economic moats of Internet giants. To quantify the value of implicit feedback, we build a new dataset called IFLLM, which collects 1336 multi-turn questions from the 59 Mechanical Turk workers, their mouse trajectories, and eye gazing points to the LLMs' responses from their webcams. IFLLM shows that the users have very diverse types of gazing behavior and mouse trajectories. Our reward model based on the implicit user feedback boosts the accuracy of the text-based reward model from 55% to 64% and nearly triples the relative response quality improvements after applying the DPO to eight LLMs, demonstrating the value of implicit feedback in the wild. Our data collection website, dataset, and codes can be found at https://github.com/themehulpatwari/llm-implicit-feedback/.

### 🤖 AI 总结

**一句话总结**：To align a Large Language Model (LLM), most existing methods collect explicit human feedback and train a reward model to predict the human preference based on the response text. These existing methods...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Mouse, Eyes, Secretly, Leak, Preference, Alignment, Implicit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20482v1) | [下载PDF](https://arxiv.org/pdf/2606.20482v1.pdf)

---

## cs.CV

## [9. JanusMesh: Fast and Zero-Shot 3D Visual Illusion Generation via Cross-Space Denoising](https://arxiv.org/abs/2606.20563v1)

**作者**：Siang-Ling Zhang, Huai-Hsun Cheng, Tsung-Ju Yang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-18

### 📄 论文摘要

Creating 3D visual illusions, a single 3D mesh that reveals entirely different semantics from various viewing angles, is a fascinating but tough challenge. Existing optimization-based methods are slow and can produce oversaturated colors. In contrast, naive stitching approaches fail to produce geometrically coherent objects. This results in visible unnatural seams and semantic leaks. In this paper, we present a fast and training-free framework for generating text-driven 3D visual illusions. Our approach decouples the generation into two stages. First, we propose a cross-space dual-branch denoising process. This process dynamically decodes 3D latents into voxel space for CLIP-guided orientation alignment and Signed Distance Field (SDF) blending, which ensures seamless geometric fusion. Second, we introduce a view-conditioned texture synthesis module that projects and aggregates view-specific 2D diffusion priors onto the fused geometry. Extensive experiments demonstrate that our method generates highly realistic, dual-semantic 3D illusions in just 3-5 minutes. It significantly outperforms existing methods in geometric integrity, semantic recognizability, and efficiency. Project page: https://siang1105.github.io/JanusMesh.github.io/

### 🤖 AI 总结

**一句话总结**：Creating 3D visual illusions, a single 3D mesh that reveals entirely different semantics from various viewing angles, is a fascinating but tough challenge. Existing optimization-based methods are slow...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, JanusMesh, Fast, Zero-Shot, Visual, Illusion, Generation, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20563v1) | [下载PDF](https://arxiv.org/pdf/2606.20563v1.pdf)

---

## [10. TimeProVe: Propose, then Verify for Efficient Long Video Temporal Reasoning in Activities of Daily Living](https://arxiv.org/abs/2606.20561v1)

**作者**：Arkaprava Sinha, Dominick Reilly, Siddharth Krishnan 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-18

### 📄 论文摘要

Long Video Question Answering (LVQA) requires identifying sparse, query-relevant evidence within hours-long untrimmed videos. Existing approaches either process videos densely with large vision-language models (VLMs), incurring prohibitive computational cost, or rely on sparse caption-based reasoning, which often misses temporally localized and motion-centric evidence. We introduce TimeProVe, a cost-efficient hybrid framework for temporally grounded reasoning in long videos. TimeProVe first employs lightweight modules to generate action-grounded answer--evidence hypotheses and subsequently invokes an expensive VLM only for targeted verification. The core of our framework lies in the Action-based Candidate Evidence (ACE) module, which converts temporally localized actions into query-conditioned candidate answers and supporting evidence windows through lightweight LLM reasoning. We further introduce OpenTSUBench (OTB), an open-ended benchmark designed to evaluate temporally grounded reasoning in real-world Activities of Daily Living (ADL) scenarios. Experiments show that TimeProVe outperforms the strongest baseline on OTB by 7.3%, while reducing VLM calls by 75% and inference cost by 93%. Furthermore, without explicit temporal grounding training, TimeProVe achieves competitive performance on Charades-STA, and reaches state-of-the-art results when enhanced with grounding VLMs.

### 🤖 AI 总结

**一句话总结**：Long Video Question Answering (LVQA) requires identifying sparse, query-relevant evidence within hours-long untrimmed videos. Existing approaches either process videos densely with large vision-langua...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TimeProVe, Propose, then, Verify, Efficient, Long, Video, Temporal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20561v1) | [下载PDF](https://arxiv.org/pdf/2606.20561v1.pdf)

---

## [11. UNIEGO: Proxies as Mediators for Unified Egocentric Video Representation Learning](https://arxiv.org/abs/2606.20559v1)

**作者**：Wenhao Chi, Arkaprava Sinha, Dominick Reilly 等 5 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-06-18

### 📄 论文摘要

Egocentric video understanding is inherently limited by the narrow perspective of wearable cameras: a single viewpoint, a single modality, a single model cannot capture the full richness of human action. We argue that a truly expressive egocentric representation must subsume complementary knowledge across viewpoints, modalities, and foundation model representations, yet remain deployable from egocentric video alone. To this end, we introduce a hierarchical multi-teacher distillation framework that produces UNIEGO, a unified egocentric encoder trained with nine teachers spanning ego-exo viewpoints, RGB, depth, and skeleton modalities, and four foundation models. Rather than distilling directly from heterogeneous teachers whose incompatible architectures and feature geometries induce conflicting gradients, our framework interposes a layer of representation-specific Proxy models that translate diverse teacher knowledge into a homogeneous egocentric space. A second distillation stage, Selective Proxy Distillation (SPD), then adaptively selects, for each training sample, the subset of proxies that are both correct and confident, distilling exclusively from reliable supervision and suppressing erroneous signals. SPD is further stabilized by initializing UNIEGO as a learned convex combination of proxy parameters, placing the unified model in a well-conditioned region of the loss landscape before distillation begins. UNIEGO achieves state-of-the-art performance across three egocentric video understanding tasks - action recognition, video retrieval, and action segmentation on three challenging ego-exo benchmarks, outperforming naive multi-teacher distillation baselines and demonstrating that structured, proxy-mediated knowledge transfer yields richer and more discriminative egocentric representations.

### 🤖 AI 总结

**一句话总结**：Egocentric video understanding is inherently limited by the narrow perspective of wearable cameras: a single viewpoint, a single modality, a single model cannot capture the full richness of human acti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, UNIEGO, Proxies, Mediators, Unified, Egocentric, Video, Representation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20559v1) | [下载PDF](https://arxiv.org/pdf/2606.20559v1.pdf)

---

## [12. Thinking in Boxes: 3D Editing in Real Images Made Easy](https://arxiv.org/abs/2606.20556v1)

**作者**：Pradhaan S Bhat, Naveen Chandra R, Rishubh Parihar 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-18

### 📄 论文摘要

Text and 2D-conditioning interfaces provide weak, ambiguous control over spatial transformations in image editing -- particularly under large object motions and camera changes. Prior work has used 3D primitives such as boxes, but only as loose conditioning signals indicating approximate object location rather than specifying the transformation. We instead use 3D boxes as structured specifications: the user provides the input and output boxes of the edit, casting editing as a well-posed geometry problem. This ``thinking in boxes'' interface, where each box face is color-coded to convey 3D orientation, gives precise control over translation, rotation, scaling, and viewpoint changes in real images while preserving scene and object identity, and recovering previously unseen object regions. To ground transformations in scene appearance, we introduce a depth-aligned planar floor as a global reference frame, shaded with depth-aware cues. Conditioned on this structure, an image generator produces consistent results under large transformations. Trained in two stages -- on synthetic multi-object scenes and a small set of real-world videos from Objectron -- the system generalizes to complex, in-the-wild real images. Our method operates directly on real photographs and substantially outperforms recent state-of-the-art methods on large 3D edits.

### 🤖 AI 总结

**一句话总结**：Text and 2D-conditioning interfaces provide weak, ambiguous control over spatial transformations in image editing -- particularly under large object motions and camera changes. Prior work has used 3D ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Thinking, Boxes, Editing, Real, Images, Made, Easy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20556v1) | [下载PDF](https://arxiv.org/pdf/2606.20556v1.pdf)

---

## [13. Current World Models Lack a Persistent State Core](https://arxiv.org/abs/2606.20545v1)

**作者**：Jinpeng Lu, Dexu Zhu, Haoyuan Shi 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-18

### 📄 论文摘要

World models are increasingly regarded as a decisive step toward artificial general intelligence, yet modeling the physical world demands more than rendering convincing frames on demand: it requires an internal world state that keeps evolving over time, decoupled from observation, so that objects endure and events run to their conclusions whether or not a camera is watching, much as the moon holds to its orbit when no one is looking. This requirement is a blind spot of existing benchmarks, which reward surface properties such as fidelity, motion, and camera controllability while never asking whether a generated world keeps evolving once it is unobserved. We introduce \textbf{WRBench}, the first systematic diagnostic benchmark that treats camera motion as an intervention on observability and resolves evaluation into a human-calibrated chain that asks whether the camera executes the requested interaction, whether the scene stays continuous and identifiable while in view, and whether a returning target remains consistent with the event that was set in motion. Across 9{,}600 videos from 23 models spanning four control paradigms, one finding proves stubborn: current systems maintain the observed world as a tracking shot, resuming a returning target in the state at which it was abandoned rather than advancing the event while it went unseen. Because this failure recurs across control paradigms, model families, and increments of scale, robust world-state evolution does not follow from cleaner imagery, tighter control, richer geometric priors, or sheer parameter count We therefore argue that the stability of the physical state kernel and the consistency of worldlines under viewpoint intervention should become first-class objectives of world-model design, so that a world model captures how the world will unfold rather than how the next frame appears.

### 🤖 AI 总结

**一句话总结**：World models are increasingly regarded as a decisive step toward artificial general intelligence, yet modeling the physical world demands more than rendering convincing frames on demand: it requires a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Current, World, Models, Lack, Persistent, State, Core, increasingly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20545v1) | [下载PDF](https://arxiv.org/pdf/2606.20545v1.pdf)

---

## [14. CalTennis: Large Multi-View Tennis Video Dataset and Benchmark of Monocular-to-3D Pose Estimation](https://arxiv.org/abs/2606.20542v1)

**作者**：Ilona Demler, Xinran Xie, Blake Werner 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-18

### 📄 论文摘要

The Caltech Tennis Dataset (CalTennis) is a large-scale video benchmark for evaluating monocular-to-3D pose estimation in the wild. CalTennis comprises over 11 million frames (51 hours) of tennis practice and match play from 40 players, captured with 2-6 synchronized cameras at 60 Hz. It is 10 times larger than existing in-the-wild human motion video datasets and 3 times larger than existing MOCAP-ground-truthed datasets, and it is the first large-scale benchmark to provide synchronized multi-view recordings of expert athletic motion. The multi-view setup enables inexpensive, label-free evaluation of monocular-to-3D pose estimation algorithms. We describe a simple, standardized protocol that enables data collection without specialized equipment or expertise, along with fully automated video calibration and synchronization. Benchmarking state-of-the-art monocular-to-3D pose methods on CalTennis, we find that while 3D joint angle recovery is now quite accurate, all models struggle to estimate depth and foot contact consistently. We further propose two novel performance metrics, footwork and stability, as well as qualitatively study body shape inconsistency. These metrics expose previously underexplored failure modes and point to concrete opportunities for improvement in pose estimation and action analysis.

### 🤖 AI 总结

**一句话总结**：The Caltech Tennis Dataset (CalTennis) is a large-scale video benchmark for evaluating monocular-to-3D pose estimation in the wild. CalTennis comprises over 11 million frames (51 hours) of tennis prac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, CalTennis, Large, Multi-View, Tennis, Video, Dataset, Benchmark

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20542v1) | [下载PDF](https://arxiv.org/pdf/2606.20542v1.pdf)

---

## [15. The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation](https://arxiv.org/abs/2606.20536v1)

**作者**：Nicolas Dufour, Alexei A. Efros, Patrick Pérez  
**分类**：cs.CV  
**发布时间**：2026-06-18

### 📄 论文摘要

The Frechet Inception Distance (FID) is the de facto arbiter of image generation, yet most papers report just a single number from a single trained model using a single sampling seed. How reproducible is that number if we retrain the model, or merely resample from it? In this paper, we treat FID as a random variable on a two-axis panel of training and generation seeds, and measure its variance directly on several hundred SiT networks trained on class-conditional ImageNet 256x256. We report surprising findings: (a) Retraining the model using the same recipe with a different seed moves FID 3.2x more (in Inception feature space) than redrawing samples from a fixed network. (b) That gap is driven by three factors: random initialisation, data ordering, and the per-step Gaussian noise of the flow-matching loss. (c) Increasing compute or model size barely tightens the spread, holding the FID coefficient of variation (CoV) inside a 1-2% band. (d) Per-cell classifier-free-guidance tuning halves the spread but reshuffles which seeds work best, and a lucky training seed reaches the same FID with up to 2x less compute than an unlucky one. Based on these findings, we recommend a new FID evaluation protocol: evaluate under per-cell optimal guidance, treat any FID gap below the empirically measured ~1.3% CoV as inconclusive, and report an error bar over several training seeds rather than a single FID number.

### 🤖 AI 总结

**一句话总结**：The Frechet Inception Distance (FID) is the de facto arbiter of image generation, yet most papers report just a single number from a single trained model using a single sampling seed. How reproducible...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FID, Lottery, Quantifying, Hidden, Randomness, Generative-Model, Evaluation, Frechet

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20536v1) | [下载PDF](https://arxiv.org/pdf/2606.20536v1.pdf)

---

## [16. VisDom: Sparse Novel View Synthesis with Visible Domain Constraint](https://arxiv.org/abs/2606.20531v1)

**作者**：Mariia Gladkova*, Tarun Yenamandra*, Edmond Boyer 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-18

### 📄 论文摘要

Sparse novel view synthesis (NVS) remains challenging due to the ambiguity of recovering 3D geometry from few input views. While NeRF- and Gaussian Splatting (GS)-based methods perform well with dense supervision, they often overfit in sparse settings, producing floating artifacts and inconsistent geometry. Silhouette consistency is commonly used as a regularizer, but it remains insufficient, as silhouette-consistent regions can extend beyond the true object geometry. We introduce VisDom, a learning-free geometric constraint that augments classical carving-based visual hull reconstruction by enforcing a minimum multi-view visibility requirement. Specifically, we define a visible domain as the subset of 3D space observed by at least $K$ views and use it as an additional filtering criterion on top of standard silhouette-based reconstruction. This provides a stronger spatial prior in sparse-view settings. We integrate VisDom into both implicit (NeRF) and explicit (GS) pipelines by restricting volumetric sampling and guiding Gaussian placement during optimization. Experiments on three challenging datasets show consistent improvements in sparse-view NVS, enabling high-quality object-centric reconstruction from as few as four input images. Our method is domain-agnostic, requires only silhouettes, and introduces no learned parameters, making it a simple complement to existing approaches. Applying VisDom on top of GaussianObject further improves performance on Omni3D and MipNeRF360, while matching or surpassing it at 22 $\times$ lower training cost.

### 🤖 AI 总结

**一句话总结**：Sparse novel view synthesis (NVS) remains challenging due to the ambiguity of recovering 3D geometry from few input views. While NeRF- and Gaussian Splatting (GS)-based methods perform well with dense...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VisDom, Sparse, Novel, View, Synthesis, Visible, Domain, Constraint

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20531v1) | [下载PDF](https://arxiv.org/pdf/2606.20531v1.pdf)

---

## [17. SARLO-80: Worldwide Slant SAR Language Optic Dataset 80cm](https://arxiv.org/abs/2606.20523v1)

**作者**：Solène Debuysère, Nicolas Trouvé, Nathan Letheule 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.DB  
**发布时间**：2026-06-18

### 📄 论文摘要

Multimodal foundation models have advanced rapidly thanks to large optical benchmarks, but comparable resources for synthetic aperture radar (SAR) remain limited. Existing SAR--optical datasets largely rely on low-resolution, intensity-only Ground Range Detected~(GRD) products and do not preserve complex-valued SAR measurements or native acquisition geometry, which restricts physically grounded multimodal learning. In particular, large-scale public datasets combining very-high-resolution (VHR) SAR SLC, aligned optical imagery, and natural-language descriptions are still lacking. We present a VHR SAR--optical--text dataset built from open-access Umbra spotlight acquisitions distributed as Sensor Independent Complex Data (SICD). From around 2,500 worldwide scenes (VV/HH, 20cm--2m native resolution), we standardize all SAR data to an 80cm slant-range grid via band-limited FFT resampling and tile the imagery into 1024 by 1024 patches. For each SAR patch, we retrieve a high-resolution optical tile and warp it into the SAR grid using local coordinate correspondences for local pixel-level alignment. We further generate three caption variants (SHORT/MID/LONG) per sample to support vision--language training and evaluation. Our dataset contains 119,566 triplets (complex and amplitude slant-range SAR patch, aligned optical patch, natural-language description) covering 257 locations across 72 countries and a broad range of land types and infrastructures. We release fixed train/validation/test splits and the full preprocessing and baseline code to enable reproducible benchmarks for multimodal alignment on cross-modal retrieval and conditional generation in native SAR geometry. The dataset is publicly available on the Hugging Face Hub at https://huggingface.co/datasets/ONERA/SARLO-80.

### 🤖 AI 总结

**一句话总结**：Multimodal foundation models have advanced rapidly thanks to large optical benchmarks, but comparable resources for synthetic aperture radar (SAR) remain limited. Existing SAR--optical datasets largel...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：80cm, SARLO-80, Worldwide, Slant, SAR, Language, Optic, Dataset

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20523v1) | [下载PDF](https://arxiv.org/pdf/2606.20523v1.pdf)

---

## [18. HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining](https://arxiv.org/abs/2606.20521v1)

**作者**：Juncheng Ma, Jianxin Bi, Yufan Deng 等 22 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-18

### 📄 论文摘要

Embodied foundation models are expected to benefit from data scaling like large language models, but face a much tighter data bottleneck. Teleoperated real-robot trajectories remain the dominant pretraining source due to their precise action supervision and embodiment alignment, yet their scalability is limited by high collection cost, acquisition difficulty, and low behavioral and environmental diversity. These limitations have sparked interest in egocentric human video as a scalable, substantially lower-cost, and more diverse alternative for embodied model pretraining. However, its effectiveness compared to teleoperated real-robot data remains underexplored. To address this question, we conduct a systematic study comparing egocentric human video and teleoperated real-robot trajectories as pretraining data sources for embodied foundation models, under fixed post-training and validation protocols. Surprisingly, we find that egocentric data, when processed through a carefully designed filtering and labeling pipeline, is not merely a viable substitute for model pretraining but can lead to superior performance. With the same amount of pretraining data, models pretrained on egocentric data achieve a 24% lower validation loss on real-robot action prediction, as well as 52.5% and 90% higher success rates on in-distribution and out-of-distribution real-robot task execution, respectively. This finding verifies a scalable paradigm for embodied foundation models: pretrain on egocentric human video to learn diverse world representations, then adapt with a small amount of labeled real-robot data for action-space alignment. We hope this study encourages broader exploration of egocentric data and offers guidance for data quality assessment before costly robot data collection.

### 🤖 AI 总结

**一句话总结**：Embodied foundation models are expected to benefit from data scaling like large language models, but face a much tighter data bottleneck. Teleoperated real-robot trajectories remain the dominant pretr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HumanScale, Egocentric, Human, Video, Can, Outperform, Real-Robot, Data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20521v1) | [下载PDF](https://arxiv.org/pdf/2606.20521v1.pdf)

---

## [19. S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence](https://arxiv.org/abs/2606.20515v1)

**作者**：Yalun Dai, Hao Li, Shulin Tian 等 13 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-18

### 📄 论文摘要

Real-world spatial intelligence requires reasoning over a continuous and evolving 3D world, yet existing VLMs and tool-augmented agents largely remain tied to static, stateless inference from isolated visual observations. We introduce \textbf{\textsc{S-Agent}}, a spatial tool-use agentic paradigm for understanding and reasoning over continuous multi-view images and videos. By formulating spatial reasoning as spatio-temporal evidence accumulation rather than isolated frame-level prediction, \textsc{S-Agent} reshapes spatial perception into scene-centric understanding beyond frame-centric recognition. Specifically, \textsc{S-Agent} casts the VLM as a semantic planner that decides what evidence is needed, while a hierarchy of spatial tools and experts grounds objects in 2D, lifts them into 3D geometric evidence, and aggregates this evidence into high-level spatial knowledge (\textit{e.g.}, counting, measurement, orientation, and relative position). Additionally, a temporal memory mechanism, including Scene Memory for maintaining the evolving scene state and Agent Memory for accumulating reasoning context, enables evidence integration across frames and reasoning steps. Comprehensive experiments on multi-view and video spatial reasoning benchmarks show that \textsc{S-Agent} consistently improves both open-source and closed-source VLMs in a training-free manner. Beyond inference-time augmentation, supervised fine-tuning (SFT) on \textsc{S-Agent}-generated spatial trajectories \textsc{S-300K} yields \textsc{S-Agent-8B}, a compact spatial agent that significantly surpasses similar-scale baselines (e.g., Qwen3-VL-8B) and performs comparably to advanced closed-source models (e.g., GPT-5.4 and Gemini 3).

### 🤖 AI 总结

**一句话总结**：Real-world spatial intelligence requires reasoning over a continuous and evolving 3D world, yet existing VLMs and tool-augmented agents largely remain tied to static, stateless inference from isolated...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：S-Agent, Spatial, tool-use, Elicits, Reasoning, Intelligence, Real-world, requires

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20515v1) | [下载PDF](https://arxiv.org/pdf/2606.20515v1.pdf)

---

## [20. FreeStyle: Free Control of Style-Content Dual-Reference Generation from Community LoRA Mining](https://arxiv.org/abs/2606.20506v1)

**作者**：Jinghong Lan, Wei Cheng, Yunuo Chen 等 13 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-18

### 📄 论文摘要

Style-content dual-reference generation aims to synthesize an image that preserves the structure and semantics of a content reference while adopting the style of a separate style reference.Despite recent progress, this setting remains challenging because models must balance content fidelity, style alignment, and instruction following avoiding semantic leakage from the style reference.A key bottleneck is the lack of large-scale triplet data with clean content-style separation and broad long-tail style coverage.In this work, we propose FreeStyle, a scalable dual-reference generation framework based on community LoRA mining.We treat community LoRAs as compositional anchors for style and content, and design a rigorous generation and filtering pipeline to construct large-scale Style-Reference and Content-Reference triplets across multiple base models.To address content leakage, we adopt a two-stage curriculum with stage-specific disentanglement mechanisms: an attention-level enrichment constraint that suppresses style-reference leakage in the style-transfer stage, and a frequency-aware RoPE modulation strategy that targets positional-correspondence-based leakage in the harder dual-reference stage.We also introduce a benchmark covering both style-reference and dual-reference generation, with evaluations on style similarity, content preservation, aesthetics, instruction following, and leakage rejection. The benchmark incorporates a style-invariant Content Alignment Score (CAS) and introduces a calibrated VLM-based Rejection Score for evaluating generation reliability and leakage suppression.Extensive experiments show that our model achieves a strong balance among style alignment, content preservation, and leakage suppression.

### 🤖 AI 总结

**一句话总结**：Style-content dual-reference generation aims to synthesize an image that preserves the structure and semantics of a content reference while adopting the style of a separate style reference.Despite rec...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, FreeStyle, Free, Control, Style-Content, Dual-Reference, Generation, Community

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20506v1) | [下载PDF](https://arxiv.org/pdf/2606.20506v1.pdf)

---

## [21. How Fragile Are Training-Free AI-Generated Image Detectors? A Controlled Audit of Score Direction, Preprocessing, and Compression](https://arxiv.org/abs/2606.20488v1)

**作者**：Jingwen Zhou, Mingzhe Wang  
**分类**：cs.CV  
**发布时间**：2026-06-18

### 📄 论文摘要

Training-free detectors of AI-generated images promise generator-agnostic deployment without classifier training, yet their reported numbers are rarely compared under a single controlled protocol. We audit two representative training-free scores -- an autoencoder-reconstruction score (AEROBLADE-style) and a noise-perturbation feature-similarity score (RIGID-style) -- plus a naive feature-kNN control, on a common 1,500-image GenImage-derived benchmark spanning seven generators and JPEG compression at quality 70 and 50. The audit yields three cautionary findings. (i) Implementation details masquerade as method differences: replacing the LPIPS backbone (AlexNet -> VGG-16) changes overall AUROC by +0.085, and switching between resize-to-512 and native-resolution preprocessing flips per-generator conclusions by up to 0.38 AUROC. (ii) Score direction is not a property of the method but of its hyperparameters: the RIGID-style score is inverted (AUROC < 0.5) on SD1.5 and Wukong at noise level sigma=0.05, recovers to >0.5 for every generator at sigma=0.01, and collapses to 0.15 at sigma=0.3. (iii) Dataset format bias inflates robustness claims: without unified re-encoding, AUROC under JPEG-50 exceeds the clean condition for the AlexNet-backbone reconstruction score; after bias correction the residual anomaly localizes to a single generator (BigGAN). The audited scores have complementary per-generator failure sets, but naive z-score fusion does not beat the best single score, indicating that exploiting complementarity requires direction-aware combination.

### 🤖 AI 总结

**一句话总结**：Training-free detectors of AI-generated images promise generator-agnostic deployment without classifier training, yet their reported numbers are rarely compared under a single controlled protocol. We ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：How, Fragile, Training-Free, AI-Generated, Image, Detectors?, Controlled, Audit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20488v1) | [下载PDF](https://arxiv.org/pdf/2606.20488v1.pdf)

---

## [22. Scalable Training of Spatially Grounded 2D Vision-Language Models for Radiology](https://arxiv.org/abs/2606.20477v1)

**作者**：Yusuf Salcan, Simon Ging, Robin Schirrmeister 等 7 位作者  
**分类**：cs.CV, cs.CL, cs.LG  
**发布时间**：2026-06-18

### 📄 论文摘要

We study how to train visually grounded vision-language models (VLMs) for radiology without manual spatial annotations. We introduce RefRad2D, a large-scale bilingual (German/English) dataset of 1.2M CT and MR image-text pairs derived from clinical practice, with task-specific VQA and spatial grounding subsets generated automatically via LLM-based curation and automated segmentation. Trained on this data, our model RadGrounder jointly performs report generation, visual question answering, and spatial grounding via bounding-box detection or segmentation. On external VQA benchmarks (Slake, VQA-RAD), RadGrounder achieves competitive results with specialized medical VLMs. Adding our clinical data to the training mixture improves open-ended VQA over fine-tuning on the downstream datasets alone, showing the transferability of our dataset. Crucially, adding grounding supervision does not degrade language quality, enabling spatially verifiable outputs at no cost to VQA performance.

### 🤖 AI 总结

**一句话总结**：We study how to train visually grounded vision-language models (VLMs) for radiology without manual spatial annotations. We introduce RefRad2D, a large-scale bilingual (German/English) dataset of 1.2M ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, 2D, Scalable, Training, Spatially, Grounded, Vision-Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20477v1) | [下载PDF](https://arxiv.org/pdf/2606.20477v1.pdf)

---

## [23. PCFootprint: A Large-Scale Dataset and Benchmark for Vectorized Building Footprint Extraction from Aerial LiDAR Point Clouds](https://arxiv.org/abs/2606.20455v1)

**作者**：Haoyuan Shen, Kuihao Wang, Ruisheng Wang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-18

### 📄 论文摘要

Building footprint extraction is a fundamental task in photogrammetry, remote sensing, and computer vision. Recent image-based methods have achieved remarkable progress in extracting vectorized footprints from high-resolution optical imagery. However, optical imagery inherently susceptible to occlusions, perspective distortions, and residual relief displacement, yielding incomplete or misaligned footprint extraction. Furthermore, the lack of explicit elevation information limits its direct applicability to Level of Detail building modeling. In this paper, we present PCFootprint, the first large-scale public dataset for footprint extraction from airborne laser scanning point clouds. PCFootprint comprises \num{33000} tiles derived from the Estonian Land and Spatial Development Board, covering diverse urban and rural landscapes. Each tile spans \qtyproduct{128 x 128}{\m} with systematically aligned vectorized footprints aligned to point clouds. The dataset includes a \num{3000} tiles cross-domain test set for evaluating generalization across geographic regions. We establish comprehensive benchmarks by evaluating mainstream methods. Experimental results reveal significant challenges including high intra-class variance, data imbalance, and noise across complex geospatial environments. We believe PCFootprint will advance future research in building modeling, urban scene understanding, and geospatial analysis. The PCFootprint dataset is publicly available at \url{https://huggingface.co/datasets/Haoyuan-Shen/PCFootprint}.

### 🤖 AI 总结

**一句话总结**：Building footprint extraction is a fundamental task in photogrammetry, remote sensing, and computer vision. Recent image-based methods have achieved remarkable progress in extracting vectorized footpr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PCFootprint, Large-Scale, Dataset, Benchmark, Vectorized, Building, Footprint, Extraction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20455v1) | [下载PDF](https://arxiv.org/pdf/2606.20455v1.pdf)

---

## cs.LG

## [24. Optimal Deterministic Multicalibration and Omniprediction](https://arxiv.org/abs/2606.20557v1)

**作者**：Georgy Noarov, Aaron Roth  
**分类**：cs.LG, math.ST, stat.ML  
**发布时间**：2026-06-18

### 📄 论文摘要

A model is multicalibrated on a collection of group weights $G$ if it is calibrated -- i.e. unbiased even conditional on its prediction -- not just overall, but also after reweighting contexts by each $g \in G$. It is a useful property for many downstream applications and is a basic desideratum of trustworthy machine learning. Before this work, all predictors known to attain the minimax-optimal $\widetilde O(\varepsilon^{-3})$ sample complexity rate for $\varepsilon$-multicalibration were randomized, while deterministic predictors were known only with substantially worse sample complexity. Whether randomization is necessary for optimal sample complexity in multicalibration was explicitly asked by [CLNR26] and implicitly in several prior works.   We resolve this open problem by giving a minimax-optimal multicalibration algorithm that outputs a deterministic predictor. We then generalize the algorithm to produce optimal deterministic predictors that satisfy outcome indistinguishability (OI) with respect to finite or finitely covered collections of tests. As an application, this also gives deterministic omnipredictors and panpredictors with optimal sample complexity, resolving open problems posed by [OKK25] and [BHHLZ25].

### 🤖 AI 总结

**一句话总结**：A model is multicalibrated on a collection of group weights $G$ if it is calibrated -- i.e. unbiased even conditional on its prediction -- not just overall, but also after reweighting contexts by each...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Optimal, Deterministic, Multicalibration, Omniprediction, model, multicalibrated, collection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20557v1) | [下载PDF](https://arxiv.org/pdf/2606.20557v1.pdf)

---

## [25. Predictability as a Fine-Grained Measure for Privacy](https://arxiv.org/abs/2606.20546v1)

**作者**：Linda Lu, Karthik Sridharan  
**分类**：cs.LG  
**发布时间**：2026-06-18

### 📄 论文摘要

Differential privacy (DP) ensures rigorous individual-level privacy guarantees against even the most knowledgeable attackers, but its worst-case nature can impose a costly privacy-accuracy tradeoff. We introduce privacy via predictability, a fine-grained framework that explicitly incorporates the attacker's core knowledge, a compromised portion of the dataset generated by a stochastic process, and a specified family of queries. Predictability measures privacy leakage as the incremental gain in an attacker's ability to predict sensitive information about unknown individuals after observing the algorithm's output, beyond what can already be inferred from the compromised data. We show that predictability and DP are generally incomparable: each can be small while the other is large. However, in the worst-case regime where all but one individual is compromised, and all binary queries are considered sensitive, predictability implies mutual-information DP. More generally, predictability provides a finer-grained privacy metric tailored to specific sensitive information and specific attacker models. We introduce a general framework, using the generalized method of moments (GMM), to analyze asymptotic predictability when the compromised data is generated by a stationary, ergodic, mixing process. Using this analysis, we derive a predictability-calibrated output perturbation scheme for ERM. Our approach is complementary to DP and can be used alongside DP to provide fine-grained privacy control.

### 🤖 AI 总结

**一句话总结**：Differential privacy (DP) ensures rigorous individual-level privacy guarantees against even the most knowledgeable attackers, but its worst-case nature can impose a costly privacy-accuracy tradeoff. W...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, DP, Predictability, Fine-Grained, Measure, Privacy, Differential, ensures

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20546v1) | [下载PDF](https://arxiv.org/pdf/2606.20546v1.pdf)

---

## [26. Multi-Task Bayesian In-Context Learning](https://arxiv.org/abs/2606.20538v1)

**作者**：Qingyang Zhu, Eric Karl Oermann, Kyunghyun Cho  
**分类**：cs.LG  
**发布时间**：2026-06-18

### 📄 论文摘要

Bayesian predictive inference provides a principled framework for uncertainty quantification, data efficiency, and robust generalization. However, exact inference is often intractable, and scalable approximations may remain computationally expensive or require restrictive modeling assumptions that degrade predictive performance. Prior-Data Fitted and in-context models have recently emerged as an amortized alternative by learning to map datasets directly to predictive distributions, but existing approaches are tightly coupled to the support of the training prior and lack explicit mechanisms for adapting to new priors at test time, resulting in limited robustness under distribution shift. We introduce a multi-task in-context learning framework for amortized hierarchical Bayesian predictive inference that explicitly represents prior information as a prefix of in-context datasets. A transformer trained on sequences of prior and target tasks learns to adapt its predictions across families of priors. On a suite of evaluations with increasing difficulty, including out-of-meta-distribution priors and priors with high-dimensional latent structures, our method matches oracle Bayesian predictors while being orders of magnitude faster. We further demonstrate its practical relevance on a real-world spatiotemporal temperature prediction benchmark. Code is available at https://github.com/martianmartina/multi-task-bayesian-icl/.

### 🤖 AI 总结

**一句话总结**：Bayesian predictive inference provides a principled framework for uncertainty quantification, data efficiency, and robust generalization. However, exact inference is often intractable, and scalable ap...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Task, Bayesian, In-Context, Learning, predictive, inference, provides, principled

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20538v1) | [下载PDF](https://arxiv.org/pdf/2606.20538v1.pdf)

---

## [27. Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems](https://arxiv.org/abs/2606.20493v1)

**作者**：Zewen Liu  
**分类**：cs.LG, cs.AI, cs.MA  
**发布时间**：2026-06-18

### 📄 论文摘要

When large language models serve as evaluators in multi-agent systems, their systematic evaluation biases propagate through the agent network. We introduce Contagion Networks, a formal framework for measuring how evaluator biases spread across interacting LLM agents. In a controlled 3-agent experiment using DeepSeek-chat with three distinct evaluator bias profiles (structured, balanced, evidence-based), we measure the Cross-Agent Contagion Matrix Gamma_3 and find that evaluator biases consistently propagate between agents (gamma in [0.157, 0.352]), even within the same underlying model. We identify three propagation regimes governed by the spectral radius rho(Gamma_N), and demonstrate that homogeneous-model agents produce contagion coefficients 3-5x weaker than cross-model coefficients observed in prior work (MM-EPC: gamma approx 0.85-1.3), placing them in the suppression regime. We show that increasing evaluator committee size from k=1 to k=3 reduces effective contagion by 72.4%, providing an actionable mitigation strategy. We release the open-source Contagion Network experimental framework.

### 🤖 AI 总结

**一句话总结**：When large language models serve as evaluators in multi-agent systems, their systematic evaluation biases propagate through the agent network. We introduce Contagion Networks, a formal framework for m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, LLM, Contagion, Networks, Evaluator, Bias, Propagation, Systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20493v1) | [下载PDF](https://arxiv.org/pdf/2606.20493v1.pdf)

---

## [28. Fisher-Geometric Sharpness and the Implicit Bias of SGD toward Flat Minima](https://arxiv.org/abs/2606.20469v1)

**作者**：Md Sakir Ahmed, Kumaresh Sarmah, Hemen Dutta  
**分类**：cs.LG, cs.CG  
**发布时间**：2026-06-18

### 📄 论文摘要

A widely held intuition in deep learning is that stochastic gradient descent (SGD) implicitly favors flat minima and that flat minima generalize better, but standard Euclidean measures of flatness such as the trace or maximum eigenvalue of the loss Hessian are not invariant under reparametrizations that preserve the network function, which undermines the theoretical foundations of this narrative. In this study we resolve this issue by grounding flatness in the Riemannian geometry of the statistical manifold induced by the Fisher Information Matrix (FIM). We define Riemannian sharpness mathematically and prove that it is invariant under smooth, function-preserving reparametrizations, which directly addresses the critique of Dinh et al. in the paper ``Sharp minima can generalize for deep nets''.We note that this invariance is a property of the true FIM; the diagonal empirical estimator used in practice (and in all experiments below) inherits invariance only approximately, and exact invariance under arbitrary reparametrizations would require structured estimators such as K-FAC. We formalize the gradient noise of mini-batch SGD as having a covariance structure proportional to the FIM, derive the stationary distribution of the resulting stochastic differential equation, and then show that the probability mass is exponentially concentrated at Riemannian-flat minima. A PAC-Bayes generalization bound controlled explicitly by SR formally links this geometric bias to test performance. Our experiments on MNIST and CIFAR-10 confirm that SR reliably tracks generalization in ways that Euclidean sharpness does not, and that its scaling with $η/B$ matches the theoretical predictions. Together these results provide a rigorous, reparametrization-invariant account of why flat minima generalize.

### 🤖 AI 总结

**一句话总结**：A widely held intuition in deep learning is that stochastic gradient descent (SGD) implicitly favors flat minima and that flat minima generalize better, but standard Euclidean measures of flatness suc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Fisher-Geometric, Sharpness, Implicit, Bias, SGD, toward, Flat

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20469v1) | [下载PDF](https://arxiv.org/pdf/2606.20469v1.pdf)

---

## [29. Agentic Symbolic Search: Characterizing PDEs Beyond Hand-crafted Expressions, Meshes, and Neural Networks](https://arxiv.org/abs/2606.20467v1)

**作者**：Zongmin Yu, Liu Yang  
**分类**：cs.LG, math.NA, physics.comp-ph  
**发布时间**：2026-06-18

### 📄 论文摘要

Mathematicians understand a PDE solution through mathematical structures rather than tables of computed values. Historically, this has been the product of mathematical analysis, carried out by hand for each problem individually. Neither numerical simulation nor neural networks produce those structures directly. We propose Agentic Symbolic Search (ASYS), a prior-guided framework in which an agent translates PDE theory, public problem constraints, and accumulated search experience into testable differentiable symbolic programs. The mathematical forms are refined under evolutionary search, while their continuous parameters are fit by gradient-based optimization. This makes the search an automated form of inductive-bias injection rather than blind symbolic regression. For problems with known analytical forms, ASYS recovers these forms naturally; for other problems, ASYS constructs analytical approximations which can guide mathematicians toward further analysis. In our experiments, across five problems spanning bounded dynamics, finite-time blow-up, and free-boundary focusing, ASYS produces interpretable representations, including a geometric interface formula for Allen-Cahn 2D dynamics and a nine-parameter contraction law for Keller-Segel chemotactic blow-up, in settings where no closed-form description was previously available. ASYS shows the possibility of a new paradigm for characterizing PDE solutions, beyond handcrafted analytical solutions, mesh-based numerical solutions, and neural network approximations.

### 🤖 AI 总结

**一句话总结**：Mathematicians understand a PDE solution through mathematical structures rather than tables of computed values. Historically, this has been the product of mathematical analysis, carried out by hand fo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agentic, Symbolic, Search, Characterizing, PDEs, Beyond, Hand-crafted, Expressions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20467v1) | [下载PDF](https://arxiv.org/pdf/2606.20467v1.pdf)

---

## [30. Data Bias Mitigation under Coverage Constraints & The Price of Fairness](https://arxiv.org/abs/2606.20461v1)

**作者**：Bruno Scarone, Alfredo Viola, Renée J. Miller  
**分类**：cs.LG, cs.CY, cs.DB  
**发布时间**：2026-06-18

### 📄 论文摘要

Machine learning models have been shown to exhibit discriminatory outcomes or degraded performance for individuals at the intersection of multiple sensitive attributes, such as race and gender. This stems in part from two interrelated challenges: the lack of principled measures for quantifying bias (potentially intersectional), and insufficient representation of intersectional subgroups in training data. We extend a recent bias mitigation framework to incorporate coverage constraints that enforce sufficient representation across groups, including intersectional subgroups. Since achieving exactly zero bias for all groups may not be data efficient (meaning it may require large amounts of data), our solution trades small approximation errors in bias for greater data efficiency while satisfying coverage constraints. We also formulate bias mitigation as an integer linear program that optimizes over all mitigation strategies, and characterize the price of fairness, the minimum data modification cost, as a function of fairness tolerance. This is essential both for legal compliance, where regulations may mandate specific fairness thresholds, and for data governance, enabling practitioners to make informed trade-offs between bias reduction and data modification (particularly, data purchasing) costs. We evaluate our techniques on publicly available datasets, demonstrating that bias mitigation via our framework preserves predictive accuracy across multiple classifiers, and that coverage constraints, while motivated by statistical considerations, are essential for preserving downstream ML performance.

### 🤖 AI 总结

**一句话总结**：Machine learning models have been shown to exhibit discriminatory outcomes or degraded performance for individuals at the intersection of multiple sensitive attributes, such as race and gender. This s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Data, Bias, Mitigation, under, Coverage, Constraints, Price

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.20461v1) | [下载PDF](https://arxiv.org/pdf/2606.20461v1.pdf)

---

