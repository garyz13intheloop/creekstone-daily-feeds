# arXiv AI 论文日报 | 2026-10-09

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (15 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.CL](#csCL) (1 篇)

---

## cs.AI

## [1. On the estimation and validity of AI time horizons---a statistical look at the METR plot](https://arxiv.org/abs/2610.12466v1)

**作者**：Drew T. Nguyen, William Fithian  
**分类**：cs.AI  
**发布时间**：2026-10-08

### 📄 论文摘要

METR's 50\% time horizon measures the human completion time of software tasks that an AI solves with 50\% probability, allowing AI capabilities to be expressed in interpretable units. On 228 tasks and 26 AIs, we recompute the time horizons using splines and item-response theory to relax the assumption that the AI difficulty of a task depends linearly on the log of human time. Our fitted spline can be interpreted as a function that \emph{converts} human time to AI difficulty; it is nearly flat in a region from 2--30 min but close to linear elsewhere. Hence, a time-horizon jump from 3 min to 30 min is much easier than one from 30 min to 5 hours despite the same multiplier of $10 \times$. Overall, we contribute time-horizon point estimates that perform better under a cross-validated suite of proper scoring rules, as well as diagnostic plots for assessing time horizons' construct validity. We suggest that time horizons be interpreted together with the diagnostic plots, especially as new time-horizon-based benchmarks are proposed or existing ones grow to include longer tasks.

### 🤖 AI 总结

**一句话总结**：METR's 50\% time horizon measures the human completion time of software tasks that an AI solves with 50\% probability, allowing AI capabilities to be expressed in interpretable units. On 228 tasks and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, at, estimation, validity, time, horizons---a, statistical, look

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12466v1) | [下载PDF](https://arxiv.org/pdf/2610.12466v1.pdf)

---

## [2. BrickBench: Evaluating Agentic Brick Design](https://arxiv.org/abs/2610.12452v1)

**作者**：Peter Kulits, Yiqing Xu, R. Kenny Jones 等 5 位作者  
**分类**：cs.AI, cs.CV, cs.GR  
**发布时间**：2026-10-08

### 📄 论文摘要

We propose BrickBench, a benchmark for agentic text-conditioned LEGO-set design. Given a prompt, an agent is tasked with producing an assembly that not only satisfies semantic and design criteria, but that can also be physically built. To do so, it must select parts from a discrete library and reason jointly about local and global constraints. We score validity, alignment, and design across three settings that vary in scale and part availability. We provide BrickAgent, an environment for coding agents to construct, inspect, and validate their designs. We find that leading agents largely satisfy verifiable physical and semantic requirements, but fall short of human designs. We release our benchmark and environment at http://www.brickben.ch

### 🤖 AI 总结

**一句话总结**：We propose BrickBench, a benchmark for agentic text-conditioned LEGO-set design. Given a prompt, an agent is tasked with producing an assembly that not only satisfies semantic and design criteria, but...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, BrickBench, Evaluating, Agentic, Brick, Design, propose, benchmark

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12452v1) | [下载PDF](https://arxiv.org/pdf/2610.12452v1.pdf)

---

## [3. Ecology of AI Agents: Collaboration Creates a Population Threshold for Takeoff](https://arxiv.org/abs/2610.12436v1)

**作者**：Erin Crawley, Hidenori Tanaka  
**分类**：cs.AI, cond-mat.dis-nn, cs.MA, physics.bio-ph  
**发布时间**：2026-10-08

### 📄 论文摘要

AI agents can now conduct real-world cyberattacks, scale up capabilities with the number of agents, and collectively pursue misaligned goals to obtain rewards. Together, these factors raise the risk of a population explosion of misaligned agents: agents could compromise computers and secretly deploy additional agents, creating a self-reinforcing cycle where larger populations develop greater collective cyber capability and expand further. This raises a fundamental question: What determines whether a population of misaligned agents remains contained or takes off into this self-reinforcing cycle? This population-level problem is ecological safety: unlike individual-agent or multi-agent safety with a fixed population, it concerns the dynamics of the population itself. Here, we develop an ecological theory of AI-agent populations based on a population growth equation in which fitness (growth rate) depends on cybersecurity capability. We show that, without collaboration, the population takes off only when individual-agent capability exceeds a critical threshold. With collaboration, however, collective cybersecurity capability increases with population size. This creates a critical population threshold: below it, the population declines; above it, the population takes off, even though individual-agent capability has not changed. In ecology, this phenomenon is known as the strong Allee effect. Because red teaming a small group of agents cannot guarantee ecological safety in larger populations, our theory calls for ecological red teaming and population pacing: gradually deploying larger agent populations in controlled environments, while measuring how cyber capability scales with population size, and estimating the critical population size for takeoff. Capability gains may lower this threshold, requiring re-estimation for each new model generation.

### 🤖 AI 总结

**一句话总结**：AI agents can now conduct real-world cyberattacks, scale up capabilities with the number of agents, and collectively pursue misaligned goals to obtain rewards. Together, these factors raise the risk o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, Ecology, Collaboration, Creates, Population, Threshold, Takeoff

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12436v1) | [下载PDF](https://arxiv.org/pdf/2610.12436v1.pdf)

---

## [4. Searching for "Harmful Refusal": A Psychometric Audit of an AI Safety Benchmark](https://arxiv.org/abs/2610.12409v1)

**作者**：Christopher M. Stewart, Preston Botter, Natalie Sarabosing 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-08

### 📄 论文摘要

Safety benchmarks typically report one overall score for a suite of datasets, each of which may target one or more safety-related attributes, so models with similar overall scores can have very different attribute profiles. Comparing models is more tractable at the level of individual attributes, yet it is often unclear whether even a single dataset's scores isolate any single attribute. One plausible candidate for such an attribute is harmful refusal, a model's tendency to refuse dangerous or policy-violating prompts. We examine whether it constitutes a single, measurable attribute in HELM Safety. Using a construct validity framework that stipulates that an attribute must exist before a test can measure it, we start with HELM Safety's four datasets that might plausibly target harmful refusal, but find that three are saturated. We subject the remaining dataset, HarmBench, to two psychometric tests to determine if a single attribute like harmful refusal could stand behind its score. First, multidimensional item response theory modeling strongly suggests that HarmBench does not measure a singular attribute. Second, a differential item functioning analysis finds items where models from different developers with the same refusal ability score differently. These flags largely disappear under scope-specific matching, a pattern consistent with aggregation effects but not sufficient to rule out domain-specific developer differences. Zooming out, HarmBench collapses distinct harm behaviors into one score, and the overall HELM safety aggregate further collapses HarmBench and scores from other datasets into a single top-line number. Any safety score that averages over datasets and items can hide saturation and conflate behaviors this way. We argue that a score should earn its single-attribute reading before models are compared with it.

### 🤖 AI 总结

**一句话总结**：Safety benchmarks typically report one overall score for a suite of datasets, each of which may target one or more safety-related attributes, so models with similar overall scores can have very differ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, an, Searching, "Harmful, Refusal", Psychometric, Audit, Safety

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12409v1) | [下载PDF](https://arxiv.org/pdf/2610.12409v1.pdf)

---

## [5. HRIL: Learning Multimodal Synergy via Higher-Order Tensor Modeling](https://arxiv.org/abs/2610.12393v1)

**作者**：Qun Dai, Liangjian Wen, Jiang Duan 等 10 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-10-08

### 📄 论文摘要

Self-supervised multimodal representation learning has achieved remarkable success across diverse domains, yet capturing synergistic information remains challenging due to the complexity of cross-modal interactions. Unlike the shared information across individual modalities, synergy arises when task-relevant signals emerge only from the joint configuration of multiple modalities and cannot be recovered from any modality in isolation. This work focuses on how to preserve the information capacity for such synergistic signals in multimodal representations. The key observation is that synergistic information is reflected in higher-order statistical dependence among modalities, which provides a principled target for explicitly modeling joint interactions. Motivated by this insight, we propose Higher-order Representation and Information Learning (HRIL), which constructs an empirical cross-moment tensor over modality embeddings to represent multi-way interactions. HRIL employs Tucker decomposition to obtain a core tensor, complemented by a synergy-aware regularizer that prevents energy concentration and preserves higher-order coupling capacity for synergistic information capture. Experiments on the controlled synergy task and real-world benchmarks demonstrate consistent improvements over existing multimodal contrastive methods, with notable gains on tasks dominated by synergistic interactions. Code is released at https://github.com/brightest66/HRIL.

### 🤖 AI 总结

**一句话总结**：Self-supervised multimodal representation learning has achieved remarkable success across diverse domains, yet capturing synergistic information remains challenging due to the complexity of cross-moda...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HRIL, Learning, Multimodal, Synergy, via, Higher-Order, Tensor, Modeling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12393v1) | [下载PDF](https://arxiv.org/pdf/2610.12393v1.pdf)

---

## [6. GeoReform: Reflective Formalization Evolution for Multimodal Geometry Problem Solving](https://arxiv.org/abs/2610.12391v1)

**作者**：Jialu Wang, Ruichen Zhang, Xiaoou Liu 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-08

### 📄 论文摘要

Multimodal large language models (MLLMs) often struggle to identify and use geometric relations in diagrams. Recent methods address this challenge by converting geometric entities, relations, and constraints into explicit textual representations for the model to reason over. However, effective formalization is highly non-trivial: on Geometry3K, structure injection fixes 28 errors but introduces 13 new ones among 200 examples. Redundant relations can distract the model, while ambiguous references to diagram elements can lead it to apply constraints incorrectly. This suggests that the key challenge is not merely extracting more geometric facts, but organizing them into representations that support downstream reasoning. To fully exploit the power of formalization, we further propose GeoReform, a reflective formalization evolution framework that treats formalization as an optimizable policy rather than a fixed parser output. GeoReform executes the full reasoning pipeline, collects failed rollouts, diagnoses defects in the current representation, and mutates the policy to better select, ground, group, and present geometric entities, relations, constraints, and targets. On Geometry3K, GeoReform improves Qwen3VL-2B accuracy from 42.0\% to 56.0\%. Extensive experiments and analyses across geometry reasoning benchmarks demonstrate that effective formalization is crucial for improving multimodal geometry reasoning.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) often struggle to identify and use geometric relations in diagrams. Recent methods address this challenge by converting geometric entities, relations, and cons...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GeoReform, Reflective, Formalization, Evolution, Multimodal, Geometry, Problem, Solving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12391v1) | [下载PDF](https://arxiv.org/pdf/2610.12391v1.pdf)

---

## cs.CL

## [7. Predicting Alignment Generalization with Value Representations](https://arxiv.org/abs/2610.12410v1)

**作者**：Andy Liu, Mehar Bhatia, Karolina Stanczak 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-10-08

### 📄 论文摘要

LLM developers post-train their models to exhibit prosocial values and behavioral traits, which are enumerated in an alignment target. However, while recent post-training developments have yielded models that score highly on alignment evaluations, training models on sets of narrow behaviors still influences their behavior across unseen contexts and environments in unexpected ways. In this paper, we establish the task of alignment generalization prediction, i.e., predicting how fine-tuning a model to follow a given value changes its behavior across a wide range of held-out values. We conduct a large-scale analysis of alignment generalization effects across 66 values found in modern alignment targets, and benchmark representational techniques on the alignment generalization prediction task. We find that representations based on model activations when applying values in context significantly outperform methods based on textual descriptions of the values. Specifically, the best activations-based methods achieve correlations of 0.45 with our generalization matrix, compared with 0.05 from description-based baselines. We then show the applicability of representations that predict alignment generalization toward downstream tasks by using them to measure how similar the values in a multi-value alignment target are, which we find is significantly correlated with model robustness. Finally, we show initial evidence towards a shared, model-independent value space, which we use to develop the first taxonomy of LLM values grounded in empirical generalization dynamics. Our work demonstrates the importance of studying value generalization in LLMs and its application toward the more empirical design and training of model behavior.

### 🤖 AI 总结

**一句话总结**：LLM developers post-train their models to exhibit prosocial values and behavioral traits, which are enumerated in an alignment target. However, while recent post-training developments have yielded mod...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Predicting, Alignment, Generalization, Value, Representations, developers, post-train

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12410v1) | [下载PDF](https://arxiv.org/pdf/2610.12410v1.pdf)

---

## cs.CV

## [8. Rubric-CEPR: Self-Evolving Image Editing via Reward-Verified Self-Distillation](https://arxiv.org/abs/2610.12469v1)

**作者**：Ritesh Thawkar, Shubham Patle, Shravan Venkatraman 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-08

### 📄 论文摘要

Instruction-guided image editors have become highly capable, yet improving them further still depends on human-edited training pairs or external reward models. Such supervision is costly to obtain and can reward plausible failures: a realistic output may leave the requested change undone or alter content that should be preserved. In this work, we strive to improve a pretrained image editor using only its own generations, without human-edited targets or an external training-time reward model. To this end, we propose a self-evolving framework, named Rubric-CEPR, that verifies the editor's own samples with its internal representations through a rubric-augmented Contrastive Edit-Preservation Reward (CEPR). A Planner proposes structured edit instructions from unlabeled images, the Editor samples multiple candidate edits, and a frozen Critic scores each candidate with decomposed rubric checks for edit realization, removal of the old state, and content preservation, using features already exposed by the editor. Non-compensatory gates reject infeasible candidates, and the best verified candidate is distilled into the editor through lightweight adapter training. On Qwen-Image-Edit, Rubric-CEPR improves ImgEdit from 4.36 to 4.60 (+5.5%), with a +24.9% gain on object isolation, and transfers to GEdit-Bench and Complex-Edit. The same procedure also improves Step1X-Edit by +7.8% on ImgEdit. We hope our approach will serve as a solid baseline for image editors that improve themselves from their own verified samples. Our code is publicly available at $\href{https://riteshthawkar.github.io/Rubric-CEPR/}{\text{this URL}}$

### 🤖 AI 总结

**一句话总结**：Instruction-guided image editors have become highly capable, yet improving them further still depends on human-edited training pairs or external reward models. Such supervision is costly to obtain and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Rubric-CEPR, Self-Evolving, Image, Editing, via, Reward-Verified, Self-Distillation, Instruction-guided

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12469v1) | [下载PDF](https://arxiv.org/pdf/2610.12469v1.pdf)

---

## [9. What 30,000 Hours of Ego-centric Video Does Not Teach](https://arxiv.org/abs/2610.12464v1)

**作者**：Jiahua Dong, Anurag Bagchi, Yash Jangir 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-08

### 📄 论文摘要

World models offer a promising alternative to physics-based simulators, yet remain far from practical deployment. We ask how far scaling ego-centric human video takes them, using a dataset of 30,000 hours spanning over 1,000 scene types and 14,000 contributors. Rather than relying on opaque downstream metrics, we directly evaluate agent and object-interaction fidelity on a challenging out-of-distribution benchmark. Increasing training data by 100x improves both, but unevenly: the agent is modeled well, while object fidelity remains far lower and improves slowly. We show that the agent gains need not come from data, and a careful visual conditioning design saturates fidelity with a fraction of it, which lets us measure object fidelity on its own and discover its saturation point. We then introduce a supervision scheme that shifts capacity from scene appearance toward object dynamics, improving object fidelity though a substantial gap remains. Finally, our conclusions transfer to downstream humanoid modeling. Overall, our results suggest that scaling ego-centric data brings agent modeling close to its limit while leaving its effects on the world far behind, and that closing this gap will depend on how models are trained, not only on how much data they see.

### 🤖 AI 总结

**一句话总结**：World models offer a promising alternative to physics-based simulators, yet remain far from practical deployment. We ask how far scaling ego-centric human video takes them, using a dataset of 30,000 h...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, What, Hours, Ego-centric, Video, Does, Not, Teach

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12464v1) | [下载PDF](https://arxiv.org/pdf/2610.12464v1.pdf)

---

## [10. OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs](https://arxiv.org/abs/2610.12461v1)

**作者**：You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li 等 6 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-10-08

### 📄 论文摘要

Recent 3D world models generate photorealistic, explorable scenes that remain frozen in time. OuroWorld is a mask-free framework that turns any static 3D Gaussian Splatting scene into a 3D cinemagraph: a dynamic scene with vivid, diverse motion looping seamlessly from any viewpoint. A vision-language model infers plausible dynamics and guides a video model to synthesize a reference video, which we lift and complete into multi-view videos. To learn from this imperfect supervision, we propose Inconsistency-Robust Periodic 4DGS: a Fourier-series deformation field guarantees looping by construction, while a Grounded Drift Field anchored at the reference view absorbs cross-view inconsistency. Unlike prior Eulerian methods limited to fluid-like motion, we capture general deformation, object motion, and illumination change. We introduce a ground-truth-free evaluation covering vividness, naturalness, loop seam coherence, and scene quality. On 39 reconstructed and generated scenes, OuroWorld outperforms all baselines and wins 70.8%-99.0% of user-study comparisons. Project page: https://ouroworld.userwei.com

### 🤖 AI 总结

**一句话总结**：Recent 3D world models generate photorealistic, explorable scenes that remain frozen in time. OuroWorld is a mask-free framework that turns any static 3D Gaussian Splatting scene into a 3D cinemagraph...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, as, OuroWorld, Bringing, Any, World, Alive, Diverse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12461v1) | [下载PDF](https://arxiv.org/pdf/2610.12461v1.pdf)

---

## [11. OmniCapBench: A Deep-Structured Evaluation Framework for Fine-Grained Audio-Visual Captioning](https://arxiv.org/abs/2610.12458v1)

**作者**：Zhongyu Yang, Jiale Tao, Ruitao Chen 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-08

### 📄 论文摘要

Multimodal large language models (MLLMs) are rapidly evolving toward continuous audio--visual reasoning, creating an urgent need for evaluations that expose their capability limits. Audio--visual captioning is an ideal diagnostic task, yet current benchmarks face a coupled trade-off: whole-caption scores provide coverage without localization, local probes provide localization without coverage, and unconstrained LLM judges introduce instability. We introduce OmniCapBench (Omni-Video Caption Benchmark), a benchmark that reframes audio--visual caption evaluation as a deep-structured diagnostic framework. OmniCapBench shifts the prediction target from free-form text to sets of atomic, verifiable evaluation units across three tracks: entity references, visual shots, and audio events, enabling reliable scoring with deterministic constraint checks and localized LLM-based semantic comparisons. With 786 densely annotated videos, OmniCapBench effectively distinguishes MLLM perception errors, including temporal grounding failures, identity drift, cross-modal misalignment, and hallucinated descriptions. Evaluating frontier MLLMs reveals strong local perception but weak long-horizon audio--visual reasoning, particularly in identity drift and cross-modal misalignment, providing a fine-grained roadmap for omnimodal development.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) are rapidly evolving toward continuous audio--visual reasoning, creating an urgent need for evaluations that expose their capability limits. Audio--visual capt...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OmniCapBench, Deep-Structured, Evaluation, Framework, Fine-Grained, Audio-Visual, Captioning, Multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12458v1) | [下载PDF](https://arxiv.org/pdf/2610.12458v1.pdf)

---

## [12. LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2610.12442v1)

**作者**：Suhwan Cho, Yonwoo Choi, Soongjin Kim 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-08

### 📄 论文摘要

Generating an egocentric video from a single exocentric recording is a challenging case of novel view synthesis, as the two cameras share little overlap and much of the target view is unobserved. Current state-of-the-art methods reconstruct the scene explicitly by estimating depth, lifting the video into a point cloud, and re-rendering it from the egocentric camera to condition a video diffusion model. This deterministic mapping assigns each pixel to a single reprojected location, which preserves texture but translates depth errors into misplaced content. We ask what a video diffusion model should receive as its condition and propose a lifting-free answer: a learned view synthesizer, an LVSM-style transformer fine-tuned to render the egocentric view directly without depth, point clouds, or reprojection, resolving cross-view correspondence internally. In contrast, its probabilistic mapping averages each region over candidate source locations according to a learned correspondence distribution, preserving structure while fine texture is averaged away. We argue that this trade-off suits a diffusion generator, whose denoising training excels at restoring detail, so an effective condition should prioritize structural alignment over sharpness. This distribution's concentration also yields a per-region confidence, used both to mask low-confidence regions and to guide the generator toward high-confidence areas during early layout-forming denoising steps. Our approach consistently outperforms the state-of-the-art explicit pipeline and generalizes to other datasets without retraining. The synthesizer thus supplies view structure, and the diffusion model its detail.

### 🤖 AI 总结

**一句话总结**：Generating an egocentric video from a single exocentric recording is a challenging case of novel view synthesis, as the two cameras share little overlap and much of the target view is unobserved. Curr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, LEGO, Lifting-Free, Approach, Exocentric-to-Egocentric, Video, Generation, Generating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12442v1) | [下载PDF](https://arxiv.org/pdf/2610.12442v1.pdf)

---

## [13. Pumpire: Unified Benchmark for Metric Distance Estimation](https://arxiv.org/abs/2610.12423v1)

**作者**：Siyu Chen, Zehan Wang, Jiayang Xu 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-08

### 📄 论文摘要

We present Pumpire, a unified benchmark for evaluating metric point-pair distance estimation capability of both image- and video-level 3D foundation models, with or without depth priors. In contrast to previous approaches that normally evaluate depth and camera intrinsics separately or evaluate point-clouds with geometric similarity metrics, which cannot directly reflect models' point-to-point distance estimation capability, Pumpire directly assesses point-to-point distances from the reconstructed geometry. To this end, we collect a large-scale and diverse dataset (pumpire-6k) comprising 100 real-world scenes, each annotated with physically measured point-pair distances and containing 64 frames, for a total of 6,400 frames. Building on this dataset, we establish a holistic evaluation protocol that covers both image- and video-level 3D foundation models and enables direct assessment of point-pair distance errors and cross-setting comparison. We conduct extensive experiments across 29 baseline configurations of representative 3D foundation models and provide a comprehensive analysis of the results. By offering this benchmark, we target the more fundamental ability to perceive and estimate physical scale in the reconstructed 3D space, which prior evaluation protocols have largely overlooked. The project page can be found at https://pumpire.github.io/

### 🤖 AI 总结

**一句话总结**：We present Pumpire, a unified benchmark for evaluating metric point-pair distance estimation capability of both image- and video-level 3D foundation models, with or without depth priors. In contrast t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Pumpire, Unified, Benchmark, Metric, Distance, Estimation, present

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12423v1) | [下载PDF](https://arxiv.org/pdf/2610.12423v1.pdf)

---

## [14. Beyond Spatio-Temporal Priors: A Generalizable Approach for Dense Correspondence Matching](https://arxiv.org/abs/2610.12421v1)

**作者**：Luping Liu, Bingyi Kang, Yifan Wang 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-10-08

### 📄 论文摘要

Dense correspondence matching has historically been bounded by simplifying spatio-temporal priors, such as smooth motion and rigid geometry. While effective for classical tasks, these assumptions break down in image editing and reference-guided generation (IEG), where transformations can preserve visual identity while breaking physical continuity. To establish identity-preserving correspondence across such transformations, we introduce FreeMatching, a generalizable framework combining generative and semantic foundation representations with heterogeneous supervision from classical datasets, tracked videos, and synthetic scenes. Teacher-guided iterative refinement further improves correspondence in IEG without dense correspondence annotations. Experimentally, a single FreeMatching model substantially improves correspondence quality on challenging IEG image pairs while retaining competitive performance on classical benchmarks. Furthermore, we demonstrate its utility as a quantitative metric for evaluating identity preservation, with scores that correlate with human judgment. The code is available at https://github.com/luping-liu/FreeMatching.

### 🤖 AI 总结

**一句话总结**：Dense correspondence matching has historically been bounded by simplifying spatio-temporal priors, such as smooth motion and rigid geometry. While effective for classical tasks, these assumptions brea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Spatio-Temporal, Priors, Generalizable, Approach, Dense, Correspondence, Matching

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12421v1) | [下载PDF](https://arxiv.org/pdf/2610.12421v1.pdf)

---

## [15. OneSearch-VL: Unified Multimodal Deep Research Agent for Image and Video](https://arxiv.org/abs/2610.12419v1)

**作者**：Hongyu Li, Manyuan Zhang, Kaituo Feng 等 14 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-08

### 📄 论文摘要

Single-image, multi-image, and video deep research require different visual operations but share a workflow of visual grounding, external retrieval, and fact composition. A key challenge is to preserve the dependencies linking localized visual anchors, entity relations, source-supported facts, and answer-producing operations. We introduce OneSearch-VL, a unified agent centered on the Visually Grounded Evidence Graph (VGEG), which encodes these dependencies as a shared task-level reference for data construction, process supervision, and operation-level evaluation. Our VGEG-based data engine constructs and verifies multi-image and video questions and filters expert trajectories. Using these data, we assemble OneSearch-VL-SFT-110K and OneSearch-VL-RL-10K for SFT and RL, respectively. We further derive the Evidence-aware Visual-Grounded Rubric reward (EVGR) from VGEG annotations to supervise evidence traceability and visual grounding during RL. For fine-grained evaluation, we construct OneSearch-MI-Bench and OneSearch-Video-Bench, organizing questions by the research operations encoded in their VGEGs. Experiments show that OneSearch-VL-8B improves over Qwen3-VL-8B with tool access by 20.2 and 17.6 percentage points on the two new benchmarks, respectively, while also achieving substantial gains across 7 image benchmarks and VideoDR. Project repository: https://github.com/appletea233/OneSearch-VL

### 🤖 AI 总结

**一句话总结**：Single-image, multi-image, and video deep research require different visual operations but share a workflow of visual grounding, external retrieval, and fact composition. A key challenge is to preserv...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, OneSearch-VL, Unified, Multimodal, Deep, Research, Image, Video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12419v1) | [下载PDF](https://arxiv.org/pdf/2610.12419v1.pdf)

---

## [16. WOVEN: Weaving Visual World Modeling into Multimodal LLMs](https://arxiv.org/abs/2610.12417v1)

**作者**：Zheyu Fan, Yue Zhang, Mingkai Deng 等 12 位作者  
**分类**：cs.CV, cs.CL, cs.LG  
**发布时间**：2026-10-08

### 📄 论文摘要

Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning. We hypothesize that these failures reflect a shared deficit in visual transition reasoning, and test whether this capability can serve as a shared training primitive, one that different models can learn from different supervision sources and reuse across different tasks, with a systematic training recipe. Existing benchmarks document these deficits separately but do not support controlled comparisons across scenes, actions, and reasoning operations. We therefore introduce WOVEN, a training source and benchmark for visual transition reasoning that organizes transition supervision by scene, action, and reasoning type, using diverse, realistic rollouts from video-pretrained generative models: 36,076 examples across 20 scene types, 5 action types, and 8 reasoning types. We first evaluate 38 frontier MLLMs (e.g., GPT-5.4 and Qwen3-VL-235B-A22B) and find a substantial and systematic deficit: even the strongest models fall far below humans, and the failures recur across model families and persist with scale. We then train MLLMs at multiple scales on WOVEN and find that they learn a shared capability that transfers broadly: training subsets of only about 2,000 items each collectively improve 22 of 26 external benchmarks by up to 27.3 percentage points, and WOVEN data can replace 30-50% of a task's own training data with comparable accuracy. Controlled comparisons further yield a training recipe for visual world modeling, validated prospectively on held-out benchmarks: select supervision by the reasoning operation it teaches rather than by the actions, scenes, or domains it shows, and prefer larger changes to the visual state for robustness. Our work establishes visual transition reasoning as a reusable foundation for systematic visual world-model training in MLLMs.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning. We hypothesize that these failures reflect a shared deficit in visual transition reasoning, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, WOVEN, Weaving, Visual, World, Modeling, Multimodal, large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12417v1) | [下载PDF](https://arxiv.org/pdf/2610.12417v1.pdf)

---

## [17. MAMHOI: Factorizing Scene-Aware Human-Object Interaction through Affordances](https://arxiv.org/abs/2610.12416v1)

**作者**：Mingyuan Lei, Yoonchang Sung, Tat-Jen Cham  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-10-08

### 📄 论文摘要

Generating realistic human-object interactions (HOI) in complex 3D scenes requires two complementary capabilities: reasoning about interaction feasibility in the environment and synthesizing realistic human-object motion. However, supervision for these capabilities is rarely available jointly at scale. Human-scene datasets provide rich information about environment-aware motion, while human-object datasets capture detailed interaction dynamics, yet paired human-object-scene data remain scarce. We present MAMHOI, an affordance-mediated factorization for scene-aware human-object interaction generation. MAMHOI factorizes scene-aware HOI generation through an explicit motion-affordance interface between scene understanding and motion synthesis: a scene-conditioned model first predicts where and how an interaction can be feasibly executed, and an affordance-conditioned HOI model then generates the corresponding human-object motion. This factorization allows scene understanding and interaction dynamics to be learned from complementary sources of supervision without requiring paired human-object-scene data. Experiments in complex indoor environments show that MAMHOI reduces object--scene penetration while better preserving human--object interaction quality, yielding more realistic and physically feasible scene-aware interactions. Project page: https://leimingyuan.github.io/MAMHOI-project-page/

### 🤖 AI 总结

**一句话总结**：Generating realistic human-object interactions (HOI) in complex 3D scenes requires two complementary capabilities: reasoning about interaction feasibility in the environment and synthesizing realistic...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MAMHOI, Factorizing, Scene-Aware, Human-Object, Interaction, through, Affordances, Generating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12416v1) | [下载PDF](https://arxiv.org/pdf/2610.12416v1.pdf)

---

## [18. WorldCast: Distributed Multiplayer World Models](https://arxiv.org/abs/2610.12412v1)

**作者**：Ziyang Ye, Junchao Huang, Evelyn Zhang 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-08

### 📄 论文摘要

Multiplayer world models must generate independently controlled views with consistent representations of both players and their shared environment. Most existing approaches coordinate multiple players through joint multi-view generation, whose cost grows with each additional player. We present WorldCast, a distributed multiplayer world model in which each player runs a local client comprising a video generator and a state model. Using recorded player positions and map geometry during training, the state model estimates the player's position from generated video and control inputs. Clients exchange player states and project them into camera-aligned player state fields that guide where and how other players are rendered. Shared scene state enables clients to reuse one another's generated observations to maintain consistent scene appearance across views. Experiments on Counter-Strike 2 demonstrate WorldCast's consistency, real-time performance, and distributed scalability. The camera-aligned player state field improves player rendering rates by over an order of magnitude over joint-generation methods, while shared scene state improves visual consistency over whole rounds. Each client runs in real time and exchanges only player and scene states, enabling scalable multiplayer generation without a centralized computational bottleneck. Image quality remains stable over hour-long rollouts.

### 🤖 AI 总结

**一句话总结**：Multiplayer world models must generate independently controlled views with consistent representations of both players and their shared environment. Most existing approaches coordinate multiple players...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：WorldCast, Distributed, Multiplayer, World, Models, must, generate, independently

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12412v1) | [下载PDF](https://arxiv.org/pdf/2610.12412v1.pdf)

---

## [19. ViSkill: Reinforcing VLM Agents with Evolving Visual-Native Skills](https://arxiv.org/abs/2610.12403v1)

**作者**：Hongxing Li, Dingming Li, Yixin Li 等 9 位作者  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-10-08

### 📄 论文摘要

Skill-augmented agents improve sample efficiency by distilling successful trajectories into reusable strategies. Yet most existing approaches remain text-centric, linearizing spatial layouts and action-state correspondences into language that loses critical geometric structure. Recent efforts have begun incorporating visual evidence, but construct and update skills separately from policy optimization, leaving their mutual improvement underexplored. We propose ViSkill, a visual-native skill learning framework that encodes successful interactions as composite visual skill cards directly accessible to VLM agents. Retrieved skills guide both inference and reward shaping, while successful trajectories are distilled back into the library, forming a closed feedback loop in which skill accumulation and policy improvement reinforce each other. An optional cold-start mechanism further accelerates early-stage learning. Evaluated on Sokoban, FrozenLake, and PrimitiveSkill, ViSkill achieves an overall success rate of 0.89, rising to 0.91 with cold-start initialization, outperforming all evaluated proprietary and open-source baselines while converging faster than standard PPO. Our code is available at https://github.com/ZJU-REAL/ViSkill.

### 🤖 AI 总结

**一句话总结**：Skill-augmented agents improve sample efficiency by distilling successful trajectories into reusable strategies. Yet most existing approaches remain text-centric, linearizing spatial layouts and actio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, ViSkill, Reinforcing, VLM, Evolving, Visual-Native, Skills, Skill-augmented

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12403v1) | [下载PDF](https://arxiv.org/pdf/2610.12403v1.pdf)

---

## [20. SpaceFlow: Locally Controllable 3D Generation](https://arxiv.org/abs/2610.12399v1)

**作者**：Neil De La Fuente, Joan Lafuente, Mukhammadali Sayfiddinov 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-10-08

### 📄 论文摘要

Current 3D generation methods lack explicit local control: geometric adherence is often defined by a global control strength, and appearance cannot be specified locally. We present SpaceFlow, a training-free pipeline for locally controllable 3D generation from text descriptions and a collection of geometric primitives. Each primitive serves as a proxy for an object part and is assigned a local control level, enabling users to specify whether regions should strictly follow the input shape or allow generative completion. During structure generation, we enforce these spatial constraints within the generative flow process. For appearance synthesis, the generated structure is segmented and matched to the primitives. Each generated part is conditioned only on its assigned text or image cue, thereby limiting cross-part leakage. Regional geometry metrics demonstrate that SpaceFlow preserves the specified geometry in high-control regions and enables plausible shape variation in low-control areas. A user study further indicates that the resulting balance between geometric fidelity and generative freedom remains competitive in overall quality. When evaluating appearance on fixed geometry, text-conditioned routing achieves state-of-the-art prompt faithfulness and color/material accuracy. Qualitative results additionally show localized routing of image cues. The project page is available at SpaceFlow3D.github.io.

### 🤖 AI 总结

**一句话总结**：Current 3D generation methods lack explicit local control: geometric adherence is often defined by a global control strength, and appearance cannot be specified locally. We present SpaceFlow, a traini...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, SpaceFlow, Locally, Controllable, Generation, Current, methods, lack

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12399v1) | [下载PDF](https://arxiv.org/pdf/2610.12399v1.pdf)

---

## [21. GenIA: Generative Reconstruction with Test-Time Input Alignment](https://arxiv.org/abs/2610.12388v1)

**作者**：Stefano Esposito, Naama Pearl, Polina Karpikova 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-08

### 📄 论文摘要

Reconstructing complete 3D object assets from monocular or sparse multi-view observations remains challenging. Generative 3D foundation models can complete object geometry beyond the observed views, but their predictions may not faithfully reproduce the observed geometry, appearance, or pose. We introduce GenIA, a framework for test-time input-aligned generation that grounds SAM3D's generative prior in geometric and photometric observations without retraining the foundation model. We improve object pose by deriving translation and scale from geometry while retaining the learned rotation prior, and align appearance through visibility-biased attention, cross-observation fusion, and differentiable rendering guidance during denoising. An optional post-denoising refinement further adapts the appearance latent, lightweight decoder adapters, and object placement to the observations. Our framework also supports externally supplied geometry; when given temporal shapes of dynamic objects, it recovers a shared, input-aligned canonical appearance and stable world-space placement. Across synthetic and real benchmarks, GenIA improves pose prediction and object reconstruction from monocular, multi-view, and dynamic inputs, outperforming recent optimization-based, per-frame image-to-3D, and video-to-4D methods. Our project page is available at https://facebookresearch.github.io/GenIA.

### 🤖 AI 总结

**一句话总结**：Reconstructing complete 3D object assets from monocular or sparse multi-view observations remains challenging. Generative 3D foundation models can complete object geometry beyond the observed views, b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GenIA, Generative, Reconstruction, Test-Time, Input, Alignment, Reconstructing, complete

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12388v1) | [下载PDF](https://arxiv.org/pdf/2610.12388v1.pdf)

---

## [22. WorldAlign: Decoupled 4D Reward for World-Consistent Video Generation](https://arxiv.org/abs/2610.12382v1)

**作者**：Jing He, Kaixin Ding, Xingye Tian 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-08

### 📄 论文摘要

Faithful visual world simulation requires generated videos to maintain 4D world consistency, encompassing both static and dynamic consistency. Static consistency requires coherent 3D structure in static environments across viewpoints, while dynamic consistency requires plausible subject motion and consistent appearance over time. Geometry-aware post-training offers a promising way to improve world consistency. However, existing methods often rely on a static-scene assumption. Even those that accommodate dynamic scenes struggle to provide reliable static-consistency feedback, while dynamic consistency is often overlooked or inadequately assessed. To address these limitations, we introduce WorldAlign, a decoupled 4D reward framework that semantically separates static regions and dynamic subjects and provides feedback by aligning each with a world prior suited to its assumptions. For static regions, WorldAlign aligns static geometry with a geometric world prior through semantically guided masked reprojection, enabling more reliable static-consistency evaluation; an auxiliary camera-motion reward discourages nearly static solutions. For dynamic subjects, WorldAlign uses a strong vision-language model (VLM) as a dynamic world prior and constructs a VLM-as-a-judge reward based on sample-specific checklists that assess dynamicity, physical plausibility, shape, and texture consistency. This decoupled design enables more effective online post-training without requiring human preference annotations. Across two pretrained image-to-video generators, Wan2.1 and Wan2.2, WorldAlign jointly improves static and dynamic consistency over existing methods without suppressing overall or subject motion. These results support decoupled world-prior alignment for more faithful visual world simulation. Project page: https://worldalign.github.io/.

### 🤖 AI 总结

**一句话总结**：Faithful visual world simulation requires generated videos to maintain 4D world consistency, encompassing both static and dynamic consistency. Static consistency requires coherent 3D structure in stat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, WorldAlign, Decoupled, Reward, World-Consistent, Video, Generation, Faithful

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12382v1) | [下载PDF](https://arxiv.org/pdf/2610.12382v1.pdf)

---

## cs.LG

## [23. Bi-FORK: Generative Modeling of High-Dimensional Bifurcating Systems](https://arxiv.org/abs/2610.12449v1)

**作者**：Anna Zimmel, Fleur Hendriks, Markus Holzleitner 等 7 位作者  
**分类**：cs.LG, cs.AI, cs.CE, physics.comp-ph  
**发布时间**：2026-10-08

### 📄 论文摘要

Bifurcations are ubiquitous in physical systems, from structural buckling to fluid and climate dynamics, yet they remain largely unexplored in deep learning. At a symmetry-breaking bifurcation, a single input admits multiple equally valid solutions, violating the one-to-one assumption underlying most learned physical surrogates. We introduce Bi-FORK, a generative framework for learning these one-to-many solution maps in high-dimensional systems. Bi-FORK generates complete trajectories through latent flow matching, preserving space and time coherence, and uses repulsion-guided sampling to recover distinct solution branches in a single amortized pass. We evaluate Bi-FORK on buckling beams, mechanical metamaterials, and Allen-Cahn phase separation, spanning continuous, discrete, and field-valued bifurcations with discretizations up to 260,000 points. Bi-FORK recovers the multimodal solution structure while scaling several orders of magnitude beyond prior approaches, opening generative modeling to high-dimensional bifurcating physical systems.

### 🤖 AI 总结

**一句话总结**：Bifurcations are ubiquitous in physical systems, from structural buckling to fluid and climate dynamics, yet they remain largely unexplored in deep learning. At a symmetry-breaking bifurcation, a sing...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Bi-FORK, Generative, Modeling, High-Dimensional, Bifurcating, Systems, Bifurcations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12449v1) | [下载PDF](https://arxiv.org/pdf/2610.12449v1.pdf)

---

## [24. Rounding in Preconditioner Space: Redesigning 4-bit AdamW Optimizer-State Quantization](https://arxiv.org/abs/2610.12444v1)

**作者**：Hanyang Li, Shao Tang, Daniel Thomas Braithwaite 等 10 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-08

### 📄 论文摘要

Quantizing AdamW's optimizer states reduces persistent storage, but quantization errors propagate through the moment recurrences and perturb subsequent adaptive updates. We redesign 4-bit optimizer-state quantization for AdamW from the perspective of \emph{rounding space}: the coordinate in which a quantizer chooses between adjacent reconstruction levels. For the second moment, a local analysis of the quantization cell adjacent to zero shows that small mean state error need not imply small mean preconditioner error at the next step. A one-dimensional quadratic construction further shows qualitatively different optimization dynamics under state-space and preconditioner-space rounding. These results motivate Zero-Inclusive Preconditioner-space Stochastic Rounding (\textbf{ZIP-SR}), which retains zero in the second-moment codebook and computes stochastic-rounding probabilities in preconditioner space. As a complementary route, Zero-Excluding EDEN calibration (\textbf{ZE-EDEN}) uses a zero-excluding second-moment codebook and rescales the quantized second-moment block to mitigate the preconditioner distortion caused by the positive quantization floor. Both configurations use 4-bit NormalFloat (NF4) for the first moment, with targeted stochastic rounding of the LM-head first moment during the final 10\% of training. Across GPT- and Llama-style pretraining experiments ranging from \textbf{130M} to \textbf{2.7B} parameters, both methods reduce TorchAO 4-bit AdamW's mean validation-loss gap to 32-bit AdamW at every evaluated model size, with the largest reported gap reduction reaching \textbf{70\%}. In full-parameter supervised fine-tuning, both recipes achieve lower validation loss than TorchAO while remaining close to 32-bit AdamW on downstream tasks.

### 🤖 AI 总结

**一句话总结**：Quantizing AdamW's optimizer states reduces persistent storage, but quantization errors propagate through the moment recurrences and perturb subsequent adaptive updates. We redesign 4-bit optimizer-st...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Rounding, Preconditioner, Space, Redesigning, 4-bit, AdamW, Optimizer-State, Quantization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12444v1) | [下载PDF](https://arxiv.org/pdf/2610.12444v1.pdf)

---

## [25. A Unified Bellman Operator for Safety-Critical Reinforcement Learning](https://arxiv.org/abs/2610.12420v1)

**作者**：Nishanth Arun Rao, Royina Karegoudra Jayanth, Benjamin Eysenbach 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-08

### 📄 论文摘要

Reinforcement learning in safety-critical domains requires maximizing task performance while strictly adhering to safety constraints. Existing safe reinforcement learning paradigms typically force a trade-off: they either require a priori knowledge to provide strict safety guarantees (e.g., safety filters), or they enable joint learning but only satisfy safety constraints on average. In this work, we propose a novel Bellman operator that unifies performance and safety objectives into a joint value function. We show that temporal difference learning with the joint Bellman operator converges under a two-timescale stochastic approximation framework. On the fast timescale, the safety value of the learning joint policy is estimated, while the joint value is estimated on the slow timescale. Convergence is ensured by formulating the limiting dynamics as an occupation-averaged differential inclusion, and showing that it asymptotically converges to a set of limiting optimal safety-constrained task value functions. Theoretically, once converged, the resulting optimal policy maximizes task return while maintaining safety at all times. Empirical evaluations on continuous control tasks with neural approximations demonstrate stable convergence with near-zero safety violations at test time.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning in safety-critical domains requires maximizing task performance while strictly adhering to safety constraints. Existing safe reinforcement learning paradigms typically force a t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unified, Bellman, Operator, Safety-Critical, Reinforcement, Learning, domains, requires

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12420v1) | [下载PDF](https://arxiv.org/pdf/2610.12420v1.pdf)

---

## [26. Learning Kilometer-Scale Weather Prediction with Global-Regional Alignment](https://arxiv.org/abs/2610.12401v1)

**作者**：Guowen Li, Yang Liu, Yujie Wang 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-08

### 📄 论文摘要

Kilometer-scale regional weather forecasting is essential for local weather warnings and weather-sensitive decisions. Existing data-driven approaches often rely on numerical forecasts for large-scale guidance or require additional training of global forecasting components. Pretrained global weather models offer an efficient source of large-scale forecasts, motivating their reuse to guide high-resolution regional prediction. However, this coupling requires aligning global and regional representations across different grids and integrating global guidance with local interactions to advance regional states. We propose ScaleCast, a regional forecasting framework that addresses these challenges through Global-Regional Alignment. Its Global-Regional Conversion module aligns joint global and regional representations with regional locations, while the Global-Regional Alignment and Dynamics block combines aligned guidance with regional neighborhood interactions. Experiments using ERA5 global analyses on a 0.25-degree grid and CERRA regional reanalysis at 5.5 km spacing demonstrate improved regional forecasts across surface and upper-air variables, with a single trained model supporting multiple global forecast drivers (i.e., Pangu-Weather, GraphCast, and HRES) without specific retraining. Fine-tuning on HRRR at 3 km spacing further demonstrates the framework's adaptability to a different regional domain and spatial resolution. Windstorm case studies show improved cyclone positioning and core-pressure estimates, while comparisons with HadISD station observations show closer agreement with local temperature and humidity changes.

### 🤖 AI 总结

**一句话总结**：Kilometer-scale regional weather forecasting is essential for local weather warnings and weather-sensitive decisions. Existing data-driven approaches often rely on numerical forecasts for large-scale ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Kilometer-Scale, Weather, Prediction, Global-Regional, Alignment, regional, forecasting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12401v1) | [下载PDF](https://arxiv.org/pdf/2610.12401v1.pdf)

---

## [27. Prospective Prediction of OOD Degradation from Source-Side Training Dynamics](https://arxiv.org/abs/2610.12397v1)

**作者**：Sasha, Monin  
**分类**：cs.LG  
**发布时间**：2026-10-08

### 📄 论文摘要

We study whether persistent out-of-distribution (OOD) degradation can be predicted before it is directly observed using only source-side training dynamics. In a controlled shortcut-learning setting, a simple logistic regression predictor develops a clear prospective signal, while training time alone does not. Temporal summaries of the source-side quantities are substantially more informative than their current values. When transferred without additional training from a CNN to an MLP, confidence and entropy dynamics retain substantial predictive information. These results provide a proof of principle that source-side training dynamics can contain an early warning signal for future OOD failure.

### 🤖 AI 总结

**一句话总结**：We study whether persistent out-of-distribution (OOD) degradation can be predicted before it is directly observed using only source-side training dynamics. In a controlled shortcut-learning setting, a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Prospective, Prediction, OOD, Degradation, Source-Side, Training, Dynamics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12397v1) | [下载PDF](https://arxiv.org/pdf/2610.12397v1.pdf)

---

## [28. Long Text to Predictive Features: LLM-Guided Blockwise Feature Engineering via Executable Program Search](https://arxiv.org/abs/2610.12390v1)

**作者**：Ziming Dai, Dabiao Ma, Ziheng Guo 等 5 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-10-08

### 📄 论文摘要

Industrial risk-control systems typically rely on structured-data models for efficient prediction, yet substantial valuable information remains embedded in unstructured long text. Extracting this information through manual feature engineering is labor-intensive, while requiring a large language model (LLM) to process every real-time input may not meet practical deployment requirements. To address this challenge, we propose LLM-BlockFE, an LLM-guided offline feature construction framework that converts long text into executable feature programs, thereby avoiding LLM calls during online inference. LLM-BlockFE constructs feature programs by incrementally appending immutable code blocks and evaluates candidate features using a downstream model. To address the tendency of conventional greedy search to become trapped in suboptimal solutions, our method introduces a block-level rollback mechanism based on depth-calibrated credit allocation and advances multiple independent search trajectories in an interleaved manner, reducing redundant exploration by sharing fixed descriptions of each trajectory's exploration direction. After the search, the resulting programs are frozen and deployed to extract structured features for downstream prediction models. Across two public and two private datasets, LLM-BlockFE achieves absolute AUC improvements of 0.0069 to 0.0358 over the strongest baseline on each dataset in the full-dataset comparison. Post-launch monitoring across five deployed financial risk-control applications shows absolute KS improvements of 0.02 to 1.56 percentage points over the existing manually designed strategy.

### 🤖 AI 总结

**一句话总结**：Industrial risk-control systems typically rely on structured-data models for efficient prediction, yet substantial valuable information remains embedded in unstructured long text. Extracting this info...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Long, Text, Predictive, Features, LLM-Guided, Blockwise, Feature, Engineering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12390v1) | [下载PDF](https://arxiv.org/pdf/2610.12390v1.pdf)

---

## [29. Marformer: A Transformer for Predicting Missing Data Distributions](https://arxiv.org/abs/2610.12379v1)

**作者**：Prabhav Singh, Xiheng Tom Wang, Haojun Shi 等 4 位作者  
**分类**：cs.LG, stat.ME  
**发布时间**：2026-10-08

### 📄 论文摘要

Real decisions are made under incomplete information. If we observe only some of the random variables we need, we can predict the others. The \textbf{conditional marginals} over the missing variables are the key ingredient for computing Bayes risk and Value of Information (VOI), the expected gain from acquiring one more observation before deciding. We present the Marformer, a Transformer trained to directly predict conditional marginals given any set of observed values. Like BERT, which is trained to predict missing words from context, the Marformer constructs a hidden-vector representation for each distribution $p(X_i)$ and iteratively refines it through attention to other distributions $p(X_j)$. Unlike generative approaches, the Marformer does not model the full joint distribution, requires no domain knowledge of the data-generating process, and makes all predictions in a single forward pass. We evaluate across three synthetic domains with missing data---Bayesian networks, discretized multivariate Gaussians, and structured annotation data. The Marformer can match or outperform classical missing-data methods, even when those methods are given the true model family and prior that generated the synthetic data. We also evaluate on a real annotation dataset, where the Marformer outperforms the evaluated baselines at the largest training size. In both cases, the Marformer is substantially faster than the evaluated generative baselines.

### 🤖 AI 总结

**一句话总结**：Real decisions are made under incomplete information. If we observe only some of the random variables we need, we can predict the others. The \textbf{conditional marginals} over the missing variables ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Marformer, Transformer, Predicting, Missing, Data, Distributions, Real, decisions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12379v1) | [下载PDF](https://arxiv.org/pdf/2610.12379v1.pdf)

---

## [30. Bilevel optimization for data-driven learning of Koopman embeddings using kernel-based autoencoders](https://arxiv.org/abs/2610.12370v1)

**作者**：Joel-Pascal Ntwali N'konzi, Feliks Nüske, Stefan Klus  
**分类**：cs.LG, math.DS, stat.ML  
**发布时间**：2026-10-08

### 📄 论文摘要

Koopman operator theory provides a linear framework for analyzing nonlinear dynamical systems and has become a major tool for data-driven modeling. A central challenge, however, is that finite-dimensional approximations computed by methods such as extended dynamic mode decomposition (EDMD) require the dictionary to be specified a priori. Recent machine-learning approaches address this limitation by learning the dictionary from data, predominantly using artificial neural network (ANN) autoencoder architectures. Although kernel methods offer an alternative with greater interpretability and tractability for theoretical analysis, they have received little attention in this setting. We introduce extended dynamic mode decomposition with kernel-based dictionary learning (EDMD-kDL), a kernel-based method for learning finite-dimensional Koopman embeddings directly from data. The method combines ideas from collocation methods and bilevel optimization to simultaneously learn a kernel dictionary and the corresponding Koopman approximation. We evaluate EDMD-kDL against state-of-the-art ANN-based approaches on a range of numerical experiments, including global sea-surface-temperature forecasting and learning directly from video data. Across all tested settings, EDMD-kDL achieves performance comparable to or better than the ANN-based methods. Moreover, in contrast to standard kernel methods, the proposed approach is scalable to large datasets by design since the size of the required kernel matrices depends on the number of collocation points rather than the size of the training dataset.

### 🤖 AI 总结

**一句话总结**：Koopman operator theory provides a linear framework for analyzing nonlinear dynamical systems and has become a major tool for data-driven modeling. A central challenge, however, is that finite-dimensi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Bilevel, optimization, data-driven, learning, Koopman, embeddings, kernel-based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.12370v1) | [下载PDF](https://arxiv.org/pdf/2610.12370v1.pdf)

---

