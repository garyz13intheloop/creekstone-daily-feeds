# arXiv AI 论文日报 | 2026-07-07

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (15 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.CL](#csCL) (2 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent, Platform Mediation, and Consent Constraints](https://arxiv.org/abs/2607.05363v1)

**作者**：Dylan Zongmin Liu  
**分类**：cs.AI  
**发布时间**：2026-07-06

### 📄 论文摘要

Personal agents are becoming persistent user-owned intermediaries: they remember preferences, filter platform-mediated information, use tools, and negotiate with services. Existing benchmarks evaluate tool use, web navigation, desktop control, personalization, recommendation, and evolving context, but rarely ask whether an agent preserves user sovereignty: advancing the user's current interests while respecting privacy, consent, evidence, user burden, and resistance to manipulative incentives. We introduce SovereignPA-Bench, an executable benchmark for evaluating user-owned personal agents under evolving intent, platform mediation, privacy boundaries, consent constraints, evidence requirements, and burden tradeoffs. The benchmark separates agent-visible ObservableState from evaluator-only HiddenLabels, reports component metrics for task success, alignment, privacy, consent, evidence, manipulation, burden, and auditability, and preserves paired scenario ordering for model and policy comparisons. We evaluate 120 sovereignty stress scenarios across 4 model families and 8 policy baselines, yielding 3,840 frozen-prompt trajectories with raw prompts, outputs, provider-form responses, parsed actions, recomputable metrics, hard-set analyses, qualitative cases, and a blinded 3-annotator audit over 240 items. Full-sovereign scaffolding improves sovereignty score over direct, memory-only, consent-only, evidence-only, ReAct/tool-use, safety-prompt, and judge-guard baselines while reducing privacy leakage, consent violation, over-concession, and manipulation capture. Human audit shows high agreement on privacy and consent and lower agreement on manipulation, identifying the subjective frontier of platform-persuasion judgments. These results show that personal-agent evaluation must move beyond task completion toward representative, consent-aware, evidence-grounded action.

### 🤖 AI 总结

**一句话总结**：Personal agents are becoming persistent user-owned intermediaries: they remember preferences, filter platform-mediated information, use tools, and negotiate with services. Existing benchmarks evaluate...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SovereignPA-Bench, Evaluating, User-Owned, Personal, under, Evolving, Intent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05363v1) | [下载PDF](https://arxiv.org/pdf/2607.05363v1.pdf)

---

## [2. Graph Sparse Sampling: Breaking the Curse of the Horizon in Continuous MDP Planning](https://arxiv.org/abs/2607.05359v1)

**作者**：Idan Lev-Yehudi, Vadim Indelman  
**分类**：cs.AI  
**发布时间**：2026-07-06

### 📄 论文摘要

Planning under uncertainty in continuous domains is essential for autonomous systems, yet computationally demanding. Tree-based search methods such as Monte Carlo Tree Search (MCTS) remain popular, but their branching structure can require sampling budgets that grow exponentially with lookahead depth in the worst case. From a tree perspective, continuous state or action spaces become especially challenging, since the planner must decide where to search in an infinite branching hierarchy. We propose Graph Sparse Sampling (GSS), an online planning algorithm that shares sampled futures across many candidate decisions, rather than sampling separate successors for each candidate action. This branch-free graph exposes large GPU-friendly batches, while using heuristics to focus computation. We prove finite-sample performance guarantees for GSS covering full-rank or low-rank generative simulators via smoothed backups, and discrete or sampled continuous action spaces. Under suitable overlap, regularity, and action-coverage conditions, these bounds have polynomial dependence on the planning horizon, formalizing when shared futures can avoid the exponential horizon dependence of tree-shaped sparse sampling. We demonstrate continuous-control simulations where GSS substantially outperforms tree-based planners on long horizons or achieves near-optimal performance, supporting no-branching graph planning as a complementary design principle for online control.

### 🤖 AI 总结

**一句话总结**：Planning under uncertainty in continuous domains is essential for autonomous systems, yet computationally demanding. Tree-based search methods such as Monte Carlo Tree Search (MCTS) remain popular, bu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Graph, Sparse, Sampling, Breaking, Curse, Horizon, Continuous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05359v1) | [下载PDF](https://arxiv.org/pdf/2607.05359v1.pdf)

---

## [3. OptiAgent: End-to-End Optimization Modeling via Multi-Agent Iterative Refinement](https://arxiv.org/abs/2607.05346v1)

**作者**：Adriana Laurindo Monteiro, Nayse Fagundes, Gabriel Mattos Langeloh 等 7 位作者  
**分类**：cs.AI, cs.MA  
**发布时间**：2026-07-06

### 📄 论文摘要

We propose OptiAgent, a multi-agent framework that, given a natural language description of an Operations Research problem, is able to output a solver-ready mathematical formulation as well as executable code. Our architecture prioritizes the mathematical modeling step, where dedicated agents extract structures, such as decision variables and constraints, enabling iterative self-correction. We introduce a novel multi-loop validation architecture with four specialized feedback mechanisms, each targeting a distinct failure mode such as misinterpretation, structural defects, mathematical inconsistencies, validation failures, and code errors. Alongside accuracy, our modular design improves the process of solving optimization problems by improving transparency, as each agent exposes its reasoning and feedback, making the full modeling process auditable. Our framework achieves state-of-the-art performance on 3 out of 4 benchmarks across LP, MILP, and Nonlinear Programming tasks, while remaining highly competitive on the remaining dataset.

### 🤖 AI 总结

**一句话总结**：We propose OptiAgent, a multi-agent framework that, given a natural language description of an Operations Research problem, is able to output a solver-ready mathematical formulation as well as executa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, OptiAgent, End-to-End, Optimization, Modeling, via, Iterative, Refinement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05346v1) | [下载PDF](https://arxiv.org/pdf/2607.05346v1.pdf)

---

## [4. Evaluating and Understanding Model Editing for Medical Vision Language Models](https://arxiv.org/abs/2607.05310v1)

**作者**：Guli Zhu, Chenwei Wu, Liyue Shen  
**分类**：cs.AI  
**发布时间**：2026-07-06

### 📄 论文摘要

Model editing promises a fast, targeted way to correct post-deployment mistakes in medical vision-language models (VLMs) without costly retraining. However, existing multimodal model editing benchmarks focus on general-purpose tasks and do not reflect realistic clinical domain requirements and variability. To address this, we introduce M3Bench, a clinically grounded benchmark for multimodal model editing that evaluates whether an edit remains reliable, precise, and generalizable under the challenges of image and text variation, modality and protocol shifts, clinical knowledge composition, and temporal progression. M3Bench contains 16,276 questions spanning diverse anatomy, modalities, and specialties, and supports both single and sequential edits.   By evaluating 4 representative editors across 6 medical and general VLMs, we find that no method excels across all criteria. Gradient-based editors achieve strong transfer but suffer from catastrophic locality violations, whereas memory-based methods preserve locality but lack compositional generality and exhibit high backbone-dependent hyperparameter sensitivity. We further attribute these failures to the latent space geometry of VLMs and how different editing methods shift its landscape. Overall, M3Bench establishes a rigorous clinical stress test for multimodal model editing and offers actionable guidance for safer post-deployment adaptation. The benchmark is publicly available at https://github.com/BioMed-AI-Lab-U-Michgan/M3Bench .

### 🤖 AI 总结

**一句话总结**：Model editing promises a fast, targeted way to correct post-deployment mistakes in medical vision-language models (VLMs) without costly retraining. However, existing multimodal model editing benchmark...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Evaluating, Understanding, Model, Editing, Medical, Vision, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05310v1) | [下载PDF](https://arxiv.org/pdf/2607.05310v1.pdf)

---

## [5. MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution](https://arxiv.org/abs/2607.05297v1)

**作者**：Zefeng Wang, Minxi Yan, Jinhe Bi 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-06

### 📄 论文摘要

Recent LLM agents tackle increasingly long-horizon, open-ended tasks, and external skills, reusable procedural knowledge supplied to the agent, further extend this capability. However, a fixed, hand-authored skill is rarely optimal, and cannot adapt to the diversity of tasks an agent encounters. Self-improving agents address this by rewriting their own skill files from execution traces, yielding meaningful gains on challenging benchmarks. Yet such self-evolution remains non-recursive: it improves only the task skill (what the agent does) while the improvement procedure (how it improves) is authored once and held fixed. We introduce MetaSkill-Evolve, a two-timescale framework that makes agentic skill improvement recursive: every branch carries both a task skill $s$ and a branch-local meta-skill $m=(ψ,σ,α,π,\varepsilon)$ whose five components parameterise the Analyzer, Retriever, Allocator, Proposer, and Evolver agents of the improvement pipeline. Task skills evolve on a fast loop while the meta-skill evolves on a slower one under the same pipeline applied to itself, with no additional model or objective. With all five pipeline agents sharing a single frozen backbone, MetaSkill-Evolve outperforms no-skill, static-skill, and single-level evolution baselines on three agentic benchmarks (OfficeQA, SealQA, ALFWorld), improving held-out test accuracy over the raw backbone by +23.54, +16.09, and +1.92 points respectively.

### 🤖 AI 总结

**一句话总结**：Recent LLM agents tackle increasingly long-horizon, open-ended tasks, and external skills, reusable procedural knowledge supplied to the agent, further extend this capability. However, a fixed, hand-a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Agent, MetaSkill-Evolve, Recursive, Self-Improvement, via, Two-Timescale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05297v1) | [下载PDF](https://arxiv.org/pdf/2607.05297v1.pdf)

---

## cs.CL

## [6. SPEARBench: A Benchmark for Naturalness Evaluation in Streaming Speech-to-Speech Language Models](https://arxiv.org/abs/2607.05365v1)

**作者**：Thomas Thebaud, Yuzhe Wang, Hao Zhang 等 8 位作者  
**分类**：cs.CL, cs.AI, eess.AS  
**发布时间**：2026-07-06

### 📄 论文摘要

Streaming speech-to-speech language models aim to answer spoken queries directly with synthetic speech. However, standard speech and text benchmarks do not capture whether these systems behave naturally in conversations, where timing, turn-taking, prosody, interpersonal stance, language and dialect consistency, and relationship-aware appropriateness jointly shape perceived quality. We introduce SPEARBench, a benchmark for evaluating naturalness in speech-to-speech language models from question-answer interactions. SPEARBench constructs controlled dialogue prompts from the Seamless Interaction corpus, runs inference across multiple models, and evaluates generated answers using a multidimensional protocol that covers response latency, interruptions, speech quality, ASR robustness, language and dialect consistency, emotional naturalness, interpersonal stance, and explainable distributional baselines. The benchmark includes original human answers as a reference condition and reports results for several contemporary models. Results show that current models can achieve high signal-level quality and low ASR error while still differing from human conversational behavior in latency, overlap, dialect preservation, emotional adaptation, and interpersonal stance dynamics.

### 🤖 AI 总结

**一句话总结**：Streaming speech-to-speech language models aim to answer spoken queries directly with synthetic speech. However, standard speech and text benchmarks do not capture whether these systems behave natural...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SPEARBench, Benchmark, Naturalness, Evaluation, Streaming, Speech-to-Speech, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05365v1) | [下载PDF](https://arxiv.org/pdf/2607.05365v1.pdf)

---

## [7. Faithfulness to Refusal: A Causal Audit of Neuron Selectors](https://arxiv.org/abs/2607.05355v1)

**作者**：Ananth Eswar, Pratinav Seth, Utsav Avaiya 等 4 位作者  
**分类**：cs.CL, cs.ET, cs.LG  
**发布时间**：2026-07-06

### 📄 论文摘要

Attribution scores increasingly identify which neuron rows of a language model matter for applications such as pruning, interpretability, and editing for safety, yet whether they identify causally important rows is rarely tested directly. We address this with two paired audits built on one-shot neuron-row zeroing. We first audit selectors at the language-modeling level: attribution methods substantially outperform activation and magnitude-based baselines at identifying dispensable rows across five LLMs. We then adapt the same intervention into a behavior test by driving it with a contrastive harmful-versus-benign signal; the attributed rows are sufficient to install refusal on hate and crime while keeping benign over-refusal low and preserving language model fluency, and specific in that layer-matched random controls at the same depths fail. Highly rank-stable selectors can be among the least causally valid. Refusal moreover lives in a redundant subspace, where different attribution methods install it through largely disjoint row sets, so the recovered edit is one realization of a sufficient set rather than a unique mechanism. Together, these findings show that rank-stability proxies miss the kinds of selector failures a direct causal audit can surface.%

### 🤖 AI 总结

**一句话总结**：Attribution scores increasingly identify which neuron rows of a language model matter for applications such as pruning, interpretability, and editing for safety, yet whether they identify causally imp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Faithfulness, Refusal, Causal, Audit, Neuron, Selectors, Attribution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05355v1) | [下载PDF](https://arxiv.org/pdf/2607.05355v1.pdf)

---

## cs.CV

## [8. From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model](https://arxiv.org/abs/2607.05396v1)

**作者**：Wenhao Li, Xueying Jiang, Quanhao Qian 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.LG, cs.RO  
**发布时间**：2026-07-06

### 📄 论文摘要

Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic geometric transformation composes the two predictions into a robot base-frame action. This disentangles how I should move in pose-independent camera-centric action generation from where I am looking from in camera-perspective geometric grounding. The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: https://alibaba-damo-academy.github.io/CamVLA/.

### 🤖 AI 总结

**一句话总结**：Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Lang...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Fixed, Free, Cameras, Calibration-Free, View-Robust, Vision-Language-Action, Model, Real-world

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05396v1) | [下载PDF](https://arxiv.org/pdf/2607.05396v1.pdf)

---

## [9. SynCity 3000: Bootstrapping Scene-Scale 3D Diffusion](https://arxiv.org/abs/2607.05392v1)

**作者**：Paul Engstler, Iro Laina, Christian Rupprecht 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-06

### 📄 论文摘要

We present SynCity 3000, a framework for generating 3D scenes that are globally coherent while enabling fine-grained layout control. Building on the ability of current image-to-3D generators to produce complex 3D assets from a single image, we extend this capability to the scale of entire scenes by adapting the generator to be applicable as a convolutional operator. We achieve this by fine-tuning the model on scene-like data generated by a new synthetic data engine, which we propose to address the scarcity of 3D scene data for training. The convolutional generator is then applied to a dimetric image of the entire scene, generated from the user prompt, resulting in 3D scenes of arbitrary size and complexity. Across diverse prompts and layouts, SynCity 3000 produces large, coherent, and detailed scenes, addressing the shortcomings of prior approaches to 3D scene generation.

### 🤖 AI 总结

**一句话总结**：We present SynCity 3000, a framework for generating 3D scenes that are globally coherent while enabling fine-grained layout control. Building on the ability of current image-to-3D generators to produc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Diffusion, We, SynCity, Bootstrapping, Scene-Scale, present, framework

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05392v1) | [下载PDF](https://arxiv.org/pdf/2607.05392v1.pdf)

---

## [10. InFlux++: Real and Synthetic Data for Estimating Dynamic Camera Intrinsics](https://arxiv.org/abs/2607.05389v1)

**作者**：Erich Liang, Caleb Kha-Uong, Chinmaya Saran 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-06

### 📄 论文摘要

Camera intrinsics are vital for recovering 3D structure from 2D video. However, most 3D algorithms assume fixed intrinsics throughout a video, an assumption that often fails for real-world in-the-wild videos. Consequently, estimating per-frame intrinsics from RGB images is critical for making 3D methods robust to videos with dynamic intrinsics. InFlux previously advanced this research direction by establishing the first real-world benchmark with per-frame ground truth intrinsics for dynamic intrinsics videos. Nevertheless, existing methods remain inaccurate due to two obstacles: (i) training data is scarce and lacks intrinsics diversity; and (ii) benchmarks, including InFlux, have limited scene and camera motion diversity, making it difficult to properly evaluate methods. To address both gaps, we present InFlux++, consisting of two components. InFlux++ Synth is a large-scale procedurally generated synthetic video dataset with 441K+ annotated frames from 1841 high-resolution videos, providing accurate per-frame ground truth intrinsics for training dynamic intrinsics prediction models; a subset also includes per-frame pose, depth, and normals. The videos feature rich intrinsics diversity through changes in camera zoom and focus, as well as dynamic objects and realistic rendering effects such as lens distortion and defocus blur. InFlux++ Real is a large-scale real-world benchmark that extends InFlux with 514K+ newly captured frames across 334 high-resolution videos, spanning a wider range of scenes and camera motions. Finetuning existing intrinsics prediction methods on InFlux++ Synth consistently improves focal length estimation across both InFlux++ Real and InFlux, suggesting that synthetic supervision is promising for RGB-based intrinsics prediction. For the dataset, benchmark, code, videos, submission instructions, and live leaderboard, please visit https://influx.cs.princeton.edu/ .

### 🤖 AI 总结

**一句话总结**：Camera intrinsics are vital for recovering 3D structure from 2D video. However, most 3D algorithms assume fixed intrinsics throughout a video, an assumption that often fails for real-world in-the-wild...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：InFlux++, Real, Synthetic, Data, Estimating, Dynamic, Camera, Intrinsics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05389v1) | [下载PDF](https://arxiv.org/pdf/2607.05389v1.pdf)

---

## [11. Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Visual Generation](https://arxiv.org/abs/2607.05382v1)

**作者**：Haozhe Wang, Weijia Feng, Jinpeng Yu 等 11 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-06

### 📄 论文摘要

Visual generators excel at rendering, but they confidently fabricate what they do not know. User requests are unbounded, evolving, and deeply long-tailed: new characters, trending entities, post-cutoff events, and more. This world-knowledge bottleneck is structural: generators are trained on fixed corpora, but the visual world is open-ended. We construct SearchGen-20K and SearchGen-Bench, with 20,839 prompts spanning twelve failure categories and twenty-two domains, paired with a pre-executed multimodal SearchGen-Corpus-1M to support offline, reproducible research. On SearchGen-Bench, frontier open generators score only 21 to 28 out of 100, a 40-point collapse invisible to existing benchmarks. The natural remedy is to employ search tools, enabling agentic visual generation. However, we find that naive search fails: it retrieves indiscriminately, injecting noise into prompts the generator already handles. We trace the root cause to a generator-specific, evolving knowledge boundary: the divide between what a generator can internalize through training and what must remain in external context. Although this boundary is hard to specify in advance, we show that it is discoverable through a teach-then-search co-training framework. Even a minimal version of this co-training recipe produces monotonic improvement, laying the foundation for recursive self-improvement in visual generation that can meet world-knowledge-grounded requests. We release the full dataset, co-training corpus, and search corpus as a replayable harness for tool-augmented, world-knowledge-grounded visual generation.

### 🤖 AI 总结

**一句话总结**：Visual generators excel at rendering, but they confidently fabricate what they do not know. User requests are unbounded, evolving, and deeply long-tailed: new characters, trending entities, post-cutof...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Be, Search, Beyond, What, Can, Taught, Evolving, Knowledge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05382v1) | [下载PDF](https://arxiv.org/pdf/2607.05382v1.pdf)

---

## [12. MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing](https://arxiv.org/abs/2607.05376v1)

**作者**：Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-07-06

### 📄 论文摘要

Recent advances in video diffusion models have enabled either long single-view generation through temporal autoregression, or short multi-view synthesis through bidirectional attention. However, generating long, multi-view consistent videos of dynamic scenes remains unsolved. In this work, we present MV-Forcing, a framework that composes temporal and view-wise autoregression within a single diffusion model by introducing a 4D geometric bridge between sequentially generated views. Our key insight is that an autoregressive 3D reconstruction model naturally interfaces between autoregressively generated views. Given a completed source view, we reconstruct its 3D structure and render a geometric prior of the next target viewpoint, which the diffusion model refines into a high-quality video. To extend generation beyond the teacher's fixed temporal window, we introduce a joint denoising regime where both view slots are initialized from noise during training, enabling temporally unbounded generation. We distill the model via Distribution Matching Distillation with Spatio-Temporal Self-Forcing, closing the train-inference exposure bias gap for both temporal and view-sequential autoregression. Extensive experiments on both synthetic and real-world data demonstrate that MV-Forcing produces geometrically consistent multi-view videos of dynamic scenes at arbitrary lengths and viewpoint counts using a single few-step student model.

### 🤖 AI 总结

**一句话总结**：Recent advances in video diffusion models have enabled either long single-view generation through temporal autoregression, or short multi-view synthesis through bidirectional attention. However, gener...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MV-Forcing, Long, Multi-View, Video, Generation, via, 4D-Grounded, Spatio-Temporal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05376v1) | [下载PDF](https://arxiv.org/pdf/2607.05376v1.pdf)

---

## [13. PixWorld: Unifying 3D Scene Generation and Reconstruction in Pixel Space](https://arxiv.org/abs/2607.05373v1)

**作者**：Sensen Gao, Zhaoqing Wang, Qihang Cao 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-06

### 📄 论文摘要

3D reconstruction and generation are commonly tackled by separate paradigms: pixel-based regression for reconstruction, and latent diffusion for generation. Recent works attempt to unify them in latent space, but with notable drawbacks: the diffusion objective is defined on latent features rather than the underlying 3D representation, and both branches suffer from information loss introduced by latent encoding, while requiring a pretrained Variational Autoencoder (VAE) or Representation Autoencoder (RAE). In this paper, we reformulate these two tasks under a unified pixel-space diffusion paradigm and introduce PixWorld, a single model that jointly addresses 3D reconstruction and generation. By supervising diffusion directly on rendered images, PixWorld removes the above limitations and aligns optimization with 3D scene fidelity. Beyond photometric and perceptual supervision that operates at the 2D image level and lacks 3D geometric awareness, we further introduce a geometry perception loss that aligns rendered views with their ground truth in the geometry-aware feature space of a pretrained 3D foundation model, providing 3D structural supervision. PixWorld consistently outperforms prior latent-space generation methods and matches state-of-the-art reconstruction methods, demonstrating the superiority of a unified pixel-space approach.

### 🤖 AI 总结

**一句话总结**：3D reconstruction and generation are commonly tackled by separate paradigms: pixel-based regression for reconstruction, and latent diffusion for generation. Recent works attempt to unify them in laten...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, PixWorld, Unifying, Scene, Generation, Reconstruction, Pixel, Space

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05373v1) | [下载PDF](https://arxiv.org/pdf/2607.05373v1.pdf)

---

## [14. Geometric Reciprocity: Unlocking Self-Supervision for Stereoscopic Video Generation](https://arxiv.org/abs/2607.05354v1)

**作者**：Jingyi Lu, Kai Han  
**分类**：cs.CV  
**发布时间**：2026-07-06

### 📄 论文摘要

Monocular-to-stereo conversion synthesizes stereoscopic content from 2D videos for immersive 3D experiences. In modern Depth-Image-Based Rendering (DIBR) approaches, stereo inpainting of disocclusions is the critical bottleneck. Training-based methods achieve superior quality but rely on scarce stereo pairs or synthetic data with domain gaps. We address this through the first self-supervised framework learning from monocular videos via cycle consistency. Our key contribution is the Geometric Reciprocity Theorem (GRT): under the nearest-neighbor DIBR formulation, the disocclusion mask when synthesizing a target view equals the mask of pixels lost when warping back from target to source, enabling analytical computation of test-time disocclusion masks directly from monocular images. This yields train-test consistency for the stated warping formulation, supporting self-supervised learning from unlimited monocular videos and substantial improvements over training-free and supervised state-of-the-art methods. Project page: https://visual-ai.github.io/grt/

### 🤖 AI 总结

**一句话总结**：Monocular-to-stereo conversion synthesizes stereoscopic content from 2D videos for immersive 3D experiences. In modern Depth-Image-Based Rendering (DIBR) approaches, stereo inpainting of disocclusions...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Geometric, Reciprocity, Unlocking, Self-Supervision, Stereoscopic, Video, Generation, Monocular-to-stereo

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05354v1) | [下载PDF](https://arxiv.org/pdf/2607.05354v1.pdf)

---

## [15. Beyond Isolated Objects: Relationship-aware Open Vocabulary Scene Understanding via 3D Scene Graph Analysis](https://arxiv.org/abs/2607.05348v1)

**作者**：Xianhao Chen, Jiarui Hu, Yuanbo Yang 等 8 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-07-06

### 📄 论文摘要

Open-vocabulary 3D scene understanding aims to segment 3D scenes beyond predefined categories by transferring semantic knowledge from vision-language models. Existing methods have advanced this task by lifting language-aligned 2D features into 3D, yet they often rely on context-independent semantic representations, leaving object relationships underexplored for contextual refinement. We propose RelGraphOV, a relationship-aware framework that uses 3D scene graphs to enhance open-vocabulary 3D understanding. Our method constructs relational scene graphs from multi-view observations by leveraging vision-language reasoning to infer object relationships and prune geometrically implausible connections, without manual relationship annotations. To aggregate relational context while avoiding feature interference, we introduce an Adaptive Gated Dual-Stream Contextual GAT that separates dense geometric features and semantic CLIP embeddings, performs edge-guided message passing, and adaptively fuses complementary semantics. A hierarchical contrastive objective further promotes instance-level consistency and category-level discrimination. Experiments on ScanNetV2, ScanNet200, ScanNet$++$, and Replica demonstrate strong performance and generalization ability. Project Page: https://cxavireh.github.io/relgraphov-projectpage

### 🤖 AI 总结

**一句话总结**：Open-vocabulary 3D scene understanding aims to segment 3D scenes beyond predefined categories by transferring semantic knowledge from vision-language models. Existing methods have advanced this task b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Isolated, Objects, Relationship-aware, Open, Vocabulary, Scene, Understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05348v1) | [下载PDF](https://arxiv.org/pdf/2607.05348v1.pdf)

---

## [16. WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images](https://arxiv.org/abs/2607.05347v1)

**作者**：Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-06

### 📄 论文摘要

While feedforward 3D reconstruction excels at efficient novel view synthesis, it typically falters when faced with scenes under varying illumination. To this end, we introduce WildSplat, the first feedforward 3D Gaussian Splatting framework capable of appearance-conditioned novel-view synthesis for unposed in-the-wild images. To handle inconsistent photometric conditions, we propose a dual-branch architecture that explicitly decouples geometry from appearance. The geometry branch extracts an appearance-invariant 3D structure and jointly predicts camera poses. To govern the rendering appearance, the appearance branch injects target appearance cues into the content features via a globally pre-modulated cross-attention mechanism. To further prevent feature entanglement, we introduce a joint multi-reference training strategy that stabilizes the training process. Extensive experiments show that WildSplat surpasses existing optimization-based and feedforward methods, achieving state-of-the-art performance in in-the-wild novel view synthesis and appearance editing from sparse inputs in a single forward pass.

### 🤖 AI 总结

**一句话总结**：While feedforward 3D reconstruction excels at efficient novel view synthesis, it typically falters when faced with scenes under varying illumination. To this end, we introduce WildSplat, the first fee...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：WildSplat, Feedforward, Gaussian, Splatting, Unposed, In-the-Wild, Images, While

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05347v1) | [下载PDF](https://arxiv.org/pdf/2607.05347v1.pdf)

---

## [17. CenSynCMB: Centre Maps and Physics-Guided Synthesis for Microbleed Detection](https://arxiv.org/abs/2607.05325v1)

**作者**：Lucas He, Hanyuan Zhang, Krinos Li 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-06

### 📄 论文摘要

Cerebral microbleeds (CMBs) are MRI markers of small vessel disease and the microbleed component of amyloid related imaging abnormalities (ARIA-H), but their small size, sparsity, and similarity to vessels, calcification-like foci, and artefacts make automated detection difficult. We propose CenSynCMB, a centre-guided and mimic-aware framework combining a 3D Attention U-Net, auxiliary centre-map supervision, false-negative-driven reweighting, and fold-wise physics-guided synthesis of positive CMBs and labelled hard negatives. Synthetic data expose the detector to compact lesions and common mimics without validation or test leakage. On VALDO Task 2, CenSynCMB achieved the best local-comparison lesion-level F1 (74.3%, p = 0.020); on external AIBL SWI, it achieved the highest local-comparison recall (88.5%, p = 0.0058) and F1 (65.0%, p = 0.0016). Together, these results support scalable CMB candidate extraction in large, unlabelled MRI cohorts, while highlighting cohort-specific calibration as the next step toward reliable burden estimation.

### 🤖 AI 总结

**一句话总结**：Cerebral microbleeds (CMBs) are MRI markers of small vessel disease and the microbleed component of amyloid related imaging abnormalities (ARIA-H), but their small size, sparsity, and similarity to ve...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CenSynCMB, Centre, Maps, Physics-Guided, Synthesis, Microbleed, Detection, Cerebral

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05325v1) | [下载PDF](https://arxiv.org/pdf/2607.05325v1.pdf)

---

## [18. Steering Optimisation Trajectories in Diffusion Representation Learning](https://arxiv.org/abs/2607.05319v1)

**作者**：Rajat Rasal, Avinash Kori, Tian Xia 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-06

### 📄 论文摘要

We study why diffusion autoencoders can achieve similar image quality while learning substantially different latent structures. We trace this behaviour to optimisation dynamics; we analyse curves of image reconstruction against latent representation quality, revealing trajectories that organise around two distinct regimes early in training. Models in the reconstruction regime prioritise image fidelity early, whereas those in the disentanglement regime improve reconstruction and disentanglement more gradually. We hypothesise that this behaviour can be influenced by targeting shortcut pathways in the diffusion U-Net and controlling early noise-level exposure, thereby shaping the reconstruction-disentanglement trade-off during training. To steer optimisation toward stronger representations, we introduce SteeringDRL, combining gated residual U-Nets with a simple noise-level exposure curriculum for training. Across disentanglement benchmarks, SteeringDRL improves representation quality and reduces seed sensitivity. Our method further extends to spatial disentanglement in object-centric learning, improving segmentation quality on synthetic and real-world datasets.

### 🤖 AI 总结

**一句话总结**：We study why diffusion autoencoders can achieve similar image quality while learning substantially different latent structures. We trace this behaviour to optimisation dynamics; we analyse curves of i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, We, Steering, Optimisation, Trajectories, Representation, Learning, study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05319v1) | [下载PDF](https://arxiv.org/pdf/2607.05319v1.pdf)

---

## [19. Topological Shape Representation for Aneurysm -- Bifurcation Detection](https://arxiv.org/abs/2607.05317v1)

**作者**：Akshay Gokhale, Mansi Dhamne  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-07-06

### 📄 论文摘要

Automated detection of intracranial aneurysms (IAs) from CT angiography (CTA) is severely hindered by high false-positive rates. Convolutional neural networks (CNNs) rely on local pixel intensities, causing systematic confusion between saccular aneurysms and vascular bifurcations -- a problem especially acute for small lesions (<3 mm), where detection sensitivity falls below 60%. We propose a plug-and-play, topology-aware false-positive reduction framework evaluating the Smooth Euler Characteristic Transform (SECT) -- a directional representation encoding global 3D vascular geometry independently of intensity -- against persistence-based summaries (Persistence Images and Landscapes), tested on a stratified subset of the RSNA 2025 dataset. SECT achieves an AUC of 0.943, substantially outperforming direction-agnostic methods (AUC ~0.68), and exhibits a clinical performance inversion: it excels on the sub-3 mm cohort, maintaining 0.943 AUC and 78.5% sensitivity at 95% specificity. The representation is also scanner-agnostic, achieving 0.927 mean AUC under leave-one-scanner-out (LOGO) validation across four manufacturers. By capturing asymmetric geometric invariants rather than intensity profiles, SECT reliably resolves the primary structural confounder in IA detection, positioning it as a robust downstream filter for hybrid deep-learning diagnostic pipelines.

### 🤖 AI 总结

**一句话总结**：Automated detection of intracranial aneurysms (IAs) from CT angiography (CTA) is severely hindered by high false-positive rates. Convolutional neural networks (CNNs) rely on local pixel intensities, c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Topological, Shape, Representation, Aneurysm, Bifurcation, Detection, Automated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05317v1) | [下载PDF](https://arxiv.org/pdf/2607.05317v1.pdf)

---

## [20. Deep Learning for Semen Analysis in Male Infertility: Computer Vision, Multimodal Fusion, and Clinical Translation](https://arxiv.org/abs/2607.05311v1)

**作者**：Runwei Guan, Shaofeng Liang, Jiacheng Weng 等 13 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-06

### 📄 论文摘要

Male infertility contributes substantially to the global infertility burden, and sperm analysis remains central to diagnosis, treatment planning, and assisted reproductive technology. Conventional semen evaluation, however, is labor-intensive, operator-dependent, and limited by inter- and intra-observer variability, motivating the development of objective and reproducible computational approaches. This review provides a comprehensive and perspective-oriented synthesis of artificial intelligence-driven sperm analysis, with a focus on computer vision, deep learning, multimodal fusion, robustness, and clinical translation. We first review task-specific methods for sperm detection and counting, tracking-based motility assessment, semantic and instance segmentation, morphology and defect classification, functional assessment, and genetic integrity evaluation. We then summarize public datasets, benchmarks, evaluation metrics, and emerging multimodal strategies that integrate microscopic images, time-lapse videos, CASA-derived parameters, DNA integrity assays, and clinical metadata. Beyond algorithmic performance, we discuss key barriers to real-world deployment, including data scarcity, cross-center domain shift, annotation inconsistency, interpretability, uncertainty calibration, privacy-preserving learning, and workflow integration. Finally, we outline a staged clinical translation roadmap spanning technical standardization, multicenter retrospective validation, silent prospective evaluation, human-in-the-loop clinical testing, ART outcome validation, regulatory approval, and post-market monitoring. By organizing the field from task-specific visual recognition to trustworthy multimodal reproductive intelligence, this review highlights both the progress and the unresolved challenges required to translate AI-driven sperm analysis into clinically meaningful decision support.

### 🤖 AI 总结

**一句话总结**：Male infertility contributes substantially to the global infertility burden, and sperm analysis remains central to diagnosis, treatment planning, and assisted reproductive technology. Conventional sem...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Deep, Learning, Semen, Analysis, Male, Infertility, Computer, Vision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05311v1) | [下载PDF](https://arxiv.org/pdf/2607.05311v1.pdf)

---

## [21. ChatImage: Navigating Long-Form LLM Answers through Interactive Images](https://arxiv.org/abs/2607.05290v1)

**作者**：Wencan Jiang, Jiangning Zhang, Yong Liu  
**分类**：cs.CV  
**发布时间**：2026-07-06

### 📄 论文摘要

Large Language Models (LLMs) can produce detailed answers to complex queries, but these answers are typically presented as dense linear text, which makes fine-grained inspection, navigation, and return visits difficult. We present ChatImage, a system that converts long-form LLM answers into interactive visual images. Given a textual answer, ChatImage first normalizes its content into structured visual modules, plans a visual layout, and renders a coherent image. It then applies a second grounding pass to the rendered image with vision grounding models such as LocateAnything and MiMo-Vision, with optional SAM-style mask refinement, to identify the visible regions that should support interaction. From these grounded regions, ChatImage overlays transparent clickable hotspots on the image. Each hotspot opens a detail panel and a region-scoped follow-up thread, allowing the user to inspect and query a specific part of the answer without re-reading the full response. Instead of treating planned coordinates as the final interaction geometry, ChatImage uses them as priors and grounds the interaction targets after rendering, which improves consistency between visual content and clickable regions. We release a reference implementation and introduce a 30-question benchmark covering infographic, map, and scene-based answer formats. Evaluation with configured external models reports interaction-loop completion, a strict visual-alignment gate, and a SAM-based mask-completeness diagnostic.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) can produce detailed answers to complex queries, but these answers are typically presented as dense linear text, which makes fine-grained inspection, navigation, and retur...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, ChatImage, Navigating, Long-Form, Answers, through, Interactive, Images

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05290v1) | [下载PDF](https://arxiv.org/pdf/2607.05290v1.pdf)

---

## [22. Erasing Without Collateral Damage: Precise Concept Removal in Diffusion Models](https://arxiv.org/abs/2607.05274v1)

**作者**：Parth Upman, Nishita Jain, Shreyank N Gowda  
**分类**：cs.CV  
**发布时间**：2026-07-06

### 📄 论文摘要

Training-free concept erasure is an attractive mechanism for controlling text-to-image diffusion models, but precise erasure often comes at the cost of damaging semantically related non-target concepts. Existing value-space methods remove the component of each cross-attention value along the target concept direction, implicitly treating target identity and shared visual structure as the same signal. We argue that this is the source of much of the collateral damage in prior preservation. We introduce CARE, a closed-form concept erasure operator that replaces the raw target direction with a kept-subspace-aware direction computed from a small bank of retained concept anchors. The resulting edit is applied directly in cross-attention value space, requires no model fine-tuning, and adds only a negligible offline computation. A single shrinkage parameter controls the erase-preserve trade-off. We further show that the operator admits a minimum-disturbance interpretation and, in its projection form, leaves the kept subspace invariant. Experiments under the standard concept-erasure protocol show that our method preserves non-target concepts more faithfully while maintaining competitive erasure across instance, style, and celebrity concepts. Code: https://github.com/parthupman/care

### 🤖 AI 总结

**一句话总结**：Training-free concept erasure is an attractive mechanism for controlling text-to-image diffusion models, but precise erasure often comes at the cost of damaging semantically related non-target concept...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Erasing, Without, Collateral, Damage, Precise, Concept, Removal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05274v1) | [下载PDF](https://arxiv.org/pdf/2607.05274v1.pdf)

---

## cs.LG

## [23. Weak-to-Strong Generalization via Direct On-Policy Distillation](https://arxiv.org/abs/2607.05394v1)

**作者**：Shiyuan Feng, Huan-ang Gao, Haohan Chi 等 10 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-07-06

### 📄 论文摘要

Reinforcement learning with verifiable rewards (RLVR) is a powerful recipe for improving language-model reasoning, but it is expensive to repeat on every new strong model because the target model must generate many rollouts during training. As models scale, post-training itself becomes a bottleneck. We study a weak-to-strong alternative: run RL on a smaller model where rollouts are cheaper, then reuse what that RL run learned to improve a stronger target model. Directly distilling the post-RL weak teacher is not enough, because the teacher's final policy mixes useful RL gains with the limitations of the smaller model. We propose Direct On-Policy Distillation (Direct-OPD), which transfers the teacher's RL-induced policy shift instead. Direct-OPD compares the post-RL teacher with its own pre-RL reference and treats their log-ratio as a dense implicit reward for the student. In plain terms, the checkpoint pair tells us which actions RL made the weak model more or less likely to take, and Direct-OPD applies that signal on the stronger student's own on-policy states. This directly reuses the weak model's RL supervision signal without training an explicit reward model or running sparse-reward RL on the target model. Empirically, Direct-OPD consistently leverages weaker teachers to improve stronger target models; notably, it boosts Qwen3-1.7B from 48.3% to 62.4% on AIME 2024 in just 4 hours on 8 A100 GPUs. It outperforms step-matched direct RL and enables the sequential composition of multiple policy shifts. Our results show that RL outcomes can be reused across model scales as implicit reward signals, not merely as final models to imitate.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning with verifiable rewards (RLVR) is a powerful recipe for improving language-model reasoning, but it is expensive to repeat on every new strong model because the target model must...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Weak-to-Strong, Generalization, via, Direct, On-Policy, Distillation, Reinforcement, learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05394v1) | [下载PDF](https://arxiv.org/pdf/2607.05394v1.pdf)

---

## [24. TabPack: Efficient Hyperparameter Ensembles for Tabular Deep Learning](https://arxiv.org/abs/2607.05380v1)

**作者**：Yury Gorishniy, Akim Kotelnikov, Ivan Rubachev 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-06

### 📄 论文摘要

In deep learning for tabular data, efficient ensembles of multilayer perceptrons (MLPs) have recently emerged as effective and practical architectures. Existing methods of this kind use the same hyperparameters for all underlying MLPs, which requires hyperparameter tuning for achieving the best performance. In this work, we introduce TabPack, an efficient MLP ensemble with strong out-of-the-box performance and reduced reliance on traditional tuning. In a single run, TabPack samples and trains many MLPs with different hyperparameters efficiently in parallel and selects ensemble members on the fly during training. Thus, TabPack only requires specifying ranges from which to sample MLP hyperparameter rather than exact hyperparameter values, which naturally demands less precision for good performance. In experiments on medium-to-large public datasets, TabPack with default settings performs on par with extensively tuned prior methods, thus substantially reducing effort and compute resources needed to achieve competitive results on tabular tasks. Notably, running the default TabPack configuration on a modern MacBook took less time than tuning some baselines on an industry-grade GPU.

### 🤖 AI 总结

**一句话总结**：In deep learning for tabular data, efficient ensembles of multilayer perceptrons (MLPs) have recently emerged as effective and practical architectures. Existing methods of this kind use the same hyper...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TabPack, Efficient, Hyperparameter, Ensembles, Tabular, Deep, Learning, data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05380v1) | [下载PDF](https://arxiv.org/pdf/2607.05380v1.pdf)

---

## [25. How Far is Too Far? Defining the Distance Threshold for Verification Siamese Networks](https://arxiv.org/abs/2607.05329v1)

**作者**：Heloísa Dias Viotto, Cauê Samonek, Lucas Garcia Pedroso 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-06

### 📄 论文摘要

Siamese verification networks are widely used to compare items such as faces, cars, or signatures. In these scenarios, the network is trained to learn an embedding space in which similar objects are mapped closer together, while dissimilar objects are mapped further apart. Two objects are considered to belong to the same class (e.g., the same person in two different images) when the distance between their embeddings falls below a predefined threshold. Defining this threshold, however, is a non-trivial task and typically requires labeled data. In this work, we assume that the distribution of distances produced by a siamese verification network can be approximated by a bimodal function. Based on this assumption, we propose an unsupervised method to determine the verification threshold by identifying the minimum point between the two modes. The proposed approach does not require annotated samples, enabling the verification threshold to be updated directly in the deployment environment without the cost of manual labeling. We evaluate our method on four datasets: MNIST, CIFAR-10, LFW, and PKLot. The results indicate that the proposed approach achieves an average verification accuracy of 94%, comparable to the Equal Error Rate method, while eliminating the need for labeled data.

### 🤖 AI 总结

**一句话总结**：Siamese verification networks are widely used to compare items such as faces, cars, or signatures. In these scenarios, the network is trained to learn an embedding space in which similar objects are m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：How, Far, Too, Far?, Defining, Distance, Threshold, Verification

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05329v1) | [下载PDF](https://arxiv.org/pdf/2607.05329v1.pdf)

---

## [26. Biologically Informed Deep Neural Networks for Multi-Omic Integration, Pathway Activity Inference and Risk Stratification in Cancer](https://arxiv.org/abs/2607.05306v1)

**作者**：Pedro Henrique da Costa Avelar, Le Ou-Yang, Min Wu 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-06

### 📄 论文摘要

Integrating complex, multi-omics data presents significant challenges. Existing approaches often face a trade-off between model interpretability and representational capacity, with most either relying on post-hoc interpretation or use linear models that may overlook complex interactions. We report Pathway Activity Autoencoders for the multi-omics setting, which embed prior knowledge via pathway-informed architectural constraints, fostering interpretability, while preserving representational power. Our multi-omic framework is applied in the context of breast cancer and is evaluated in survival prediction and subtype classification with results indicating a positive effect of integration. We conduct analysis of individual omics layer impact on end-task performance, revealing that gene, protein, and microRNA expression layers provide the strongest contribution. Repeatability studies indicate that, while dropout improves model robustness and consistency, excessive regularisation can reduce predictive performance. Finally, visualizations of the learned feature space illustrate the framework's intrinsic transparency and clinical relevance. The results underscore the value of multi-omic integration and delineate the impact of individual omics layers, establishing practical guidelines for integration within our framework. Overall, our pathway activity autoencoder frameworks yield superior latent representations that are biologically meaningful and are directly translatable into clinically relevant insights.

### 🤖 AI 总结

**一句话总结**：Integrating complex, multi-omics data presents significant challenges. Existing approaches often face a trade-off between model interpretability and representational capacity, with most either relying...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Biologically, Informed, Deep, Neural, Networks, Multi-Omic, Integration, Pathway

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05306v1) | [下载PDF](https://arxiv.org/pdf/2607.05306v1.pdf)

---

## [27. Learning Only What Valid Adapters Can Express: Subspace-Constrained Adaptation Against Fine-Tuning Poisoning](https://arxiv.org/abs/2607.05300v1)

**作者**：Fabien Polly  
**分类**：cs.LG, cs.CR  
**发布时间**：2026-07-06

### 📄 论文摘要

Parameter-efficient fine-tuning still leaves a broad space of behavior-changing updates reachable, so a poisoned objective can be represented and optimized. We study an alternative: adaptation constrained to the subspace estimated from a trusted pool of existing task adapters. On flan-t5-large with 196 public LoRA adapters, we show that (1) the functionally relevant content of an adapter lies in a low-dimensional shared subspace, 30 to 38 percent of its weight norm being redundant under the evaluated task distributions; (2) gradient adaptation restricted to 128 coordinates on this subspace matches full LoRA fine-tuning on clean classification data, while under targeted label inversion LoRA collapses to 3-26 percent exact match and the constrained learner keeps 62-96 percent on the tasks the pool covers; (3) the constrained learner cannot fit corrupted data, its adaptation loss separating clean from garbage by two orders of magnitude (120x), an out-of-distribution signal without an extra detector; and (4) against an adaptive backdoor attacker who optimizes within the subspace, the attack is blocked (8 percent success versus 100 for LoRA) on the task where its target behavior is unlike anything in the pool, and only partially blocked (85 percent) when the target coincides with a common pool behavior. On these two tasks the outcome is consistent with how close the target is to the pool's directions, which suggests but does not establish a pool-relative boundary. The mechanism trades peak plasticity for these properties: on tasks the pool covers poorly, unconstrained fine-tuning wins, and the protection assumes the pool itself is trusted. Code and data are public.

### 🤖 AI 总结

**一句话总结**：Parameter-efficient fine-tuning still leaves a broad space of behavior-changing updates reachable, so a poisoned objective can be represented and optimized. We study an alternative: adaptation constra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Only, What, Valid, Adapters, Can, Express, Subspace-Constrained

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05300v1) | [下载PDF](https://arxiv.org/pdf/2607.05300v1.pdf)

---

## [28. Air Quality Downscaling with Station-Guided Pseudo-Supervision](https://arxiv.org/abs/2607.05292v1)

**作者**：Guorun Wang, Simone Foti, Andreas D. Demou 等 8 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-07-06

### 📄 论文摘要

Super-resolving coarse atmospheric fields to local PM$_{2.5}$ variations is uniquely challenged by a mismatch in spatial support: while pixels represent regional averages, ground-truth observations are discrete, unaligned samples of a continuous spatial signal. To bridge this gap, we present a station-guided framework for high-resolution PM$_{2.5}$ downscaling over Europe. Taking coarse CAMS atmospheric composition fields alongside heterogeneous side information (i.e., human activity, land cover, elevation, satellite aerosol observations, and wind fields) our framework jointly super-resolves ($\times 40$, $\approx$ 1 km) and bias-corrects CAMS rasters, without relying on temporal sequence modelling. To address the challenge of densely supervising our multi-scale transformer network with sparse in-situ data, we introduce a time-agnostic propagation strategy that utilises spatial Gaussian blending of interpolated OpenAQ observations. Extensive qualitative and station-level evaluations across Europe demonstrate that our model recovers fine-grained spatial structures and effectively mitigates localised CAMS biases.

### 🤖 AI 总结

**一句话总结**：Super-resolving coarse atmospheric fields to local PM$_{2.5}$ variations is uniquely challenged by a mismatch in spatial support: while pixels represent regional averages, ground-truth observations ar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Air, Quality, Downscaling, Station-Guided, Pseudo-Supervision, Super-resolving, coarse, atmospheric

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05292v1) | [下载PDF](https://arxiv.org/pdf/2607.05292v1.pdf)

---

## [29. Advances in Neural Controlled Differential Equations](https://arxiv.org/abs/2607.05280v1)

**作者**：Benjamin Walker  
**分类**：cs.LG  
**发布时间**：2026-07-06

### 📄 论文摘要

Many real-world systems evolve continuously, yet most machine learning models interpret time series as discrete sequences. Continuous-time approaches instead treat time series as samples from an underlying input path, a formulation that naturally accommodates irregularly sampled or oversampled data. Among these, Neural Controlled Differential Equations (NCDEs) are a maximally expressive class of models that parametrise a vector field using a neural network and evolve their hidden state by solving a dynamical system driven by the input path. NCDEs typically use a non-linear vector field, so their expressive power and continuous-time flexibility come at the cost of a forward pass that is both computationally expensive and inherently sequential, limiting their scalability and practical applicability.   This thesis advances the training and scalability of NCDEs through three complementary contributions. First, building on neural rough differential equations, Log-NCDEs apply the Log-ODE method to efficiently approximate an NCDE's solution during training, improving both computational speed and empirical performance. Second, Linear NCDEs replace the non-linear vector field with a linear one, enabling closed-form solutions and parallel-in-time computation without sacrificing theoretical expressivity. Third, Structured Linear NCDEs use structured linear vector fields to further enhance efficiency while maintaining theoretical expressiveness and empirical performance.   Collectively, these methods reduce the time per training step for an NCDE by up to three orders of magnitude while achieving state-of-the-art performance across diverse time series benchmarks.

### 🤖 AI 总结

**一句话总结**：Many real-world systems evolve continuously, yet most machine learning models interpret time series as discrete sequences. Continuous-time approaches instead treat time series as samples from an under...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Advances, Neural, Controlled, Differential, Equations, Many, real-world, systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05280v1) | [下载PDF](https://arxiv.org/pdf/2607.05280v1.pdf)

---

## [30. Adaptive Inference Batching using Policy Gradients](https://arxiv.org/abs/2607.05272v1)

**作者**：Ruslan Sharifullin  
**分类**：cs.LG, cs.AI, cs.DC, cs.PF  
**发布时间**：2026-07-06

### 📄 论文摘要

Inference serving systems must balance throughput and latency under bursty, heterogeneous workloads, yet the industry standard remains static batching policies that require manual tuning and cannot adapt to shifting traffic. We investigate whether reinforcement learning (RL) can learn adaptive batching and routing policies that outperform these heuristics, training REINFORCE and PPO agents on a discrete-event simulator validated against queuing theory and production traces (Azure Functions, BurstGPT). We formulate the problem as an MDP over queue state, request type and GPU availability, evaluating across standard Poisson traffic, extreme bursts, real-world traces and heterogeneous multi-GPU routing.   Our central finding is a clear boundary condition for RL's value in systems problems. In single-GPU settings, a well-tuned static batching policy is already near-optimal under Poisson-like arrivals and RL offers only marginal gains (+0.1% to +1.0%). In multi-GPU heterogeneous routing, however, where fast and slow requests compete for shared resources, the agent discovers a workload-segregation policy that eliminates Head-of-Line blocking, yielding a 3.5x (348%) improvement over Round-Robin and a 48% improvement over the strongest heuristic baseline (Shortest-Queue), with 60% higher throughput and 25% lower latency while respecting SLA constraints. The policy generalizes to unseen bursty and real-world traffic despite training only on synthetic Poisson arrivals and an attention-augmented policy network converges roughly 20% faster than an MLP baseline.   These results suggest RL's advantage over engineered heuristics concentrates in combinatorial, multi-resource decisions rather than single-resource temporal scheduling, a practical distinction for deciding where learned policies justify their engineering cost in production inference infrastructure.

### 🤖 AI 总结

**一句话总结**：Inference serving systems must balance throughput and latency under bursty, heterogeneous workloads, yet the industry standard remains static batching policies that require manual tuning and cannot ad...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Adaptive, Inference, Batching, Policy, Gradients, serving, systems, must

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.05272v1) | [下载PDF](https://arxiv.org/pdf/2607.05272v1.pdf)

---

