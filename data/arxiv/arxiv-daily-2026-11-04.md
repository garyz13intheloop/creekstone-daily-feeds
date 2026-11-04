# arXiv AI 论文日报 | 2026-11-04

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (6 篇)
- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (12 篇)
- [cs.AI](#csAI) (1 篇)

---

## cs.AI

## [1. The Geometry of Ignorance: Detecting Suppressed Knowledge in LLMs through Activation Fragmentation](https://arxiv.org/abs/2611.05272v1)

**作者**：Adar Peleg, Dvir Alsheich, Tomer Ashuach 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-03

### 📄 论文摘要

Evaluating whether a large language model (LLM) genuinely knows a concept remains a fundamental problem, since behavioral metrics can be fooled by suppression: a model that refuses to answer may still harbor recoverable knowledge. The framework measures the geometric coherence of \textit{anon-vectors}, the differences in hidden states between a concept-specific query and its anonymized paraphrase, and shows that genuine knowledge forms a tight, low-entropy cluster while ignorance forces geometric fragmentation. Across ten instruction-tuned LLMs from three model families, all fragmentation metrics reliably separate known from unknown concepts, and post-unlearning, fragmentation geometry correlates with adversarial recovery across four attack types and five unlearning algorithms, though the direction of that relationship is shown to depend on attack methodology. Furthermore, a layer-resolved analysis reveals that different adversarial mechanisms exploit this geometry at varying depths, with high attack-specific correlations that are invisible to behavioral evaluation. Together, these results constitute a single-phase, attack-free proxy for unlearning robustness that captures aspects of parametric knowledge inaccessible to output-level metrics. A reference implementation is available at https://github.com/AdarPeleg/geometry-of-ignorance

### 🤖 AI 总结

**一句话总结**：Evaluating whether a large language model (LLM) genuinely knows a concept remains a fundamental problem, since behavioral metrics can be fooled by suppression: a model that refuses to answer may still...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Geometry, Ignorance, Detecting, Suppressed, Knowledge, through

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05272v1) | [下载PDF](https://arxiv.org/pdf/2611.05272v1.pdf)

---

## cs.CL

## [2. From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence](https://arxiv.org/abs/2611.05376v1)

**作者**：Hao Fei  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-11-03

### 📄 论文摘要

For a decade, progress in artificial intelligence has been measured by how much a machine can do on its own. Large foundation models now write code and run multistep tasks, and personal agents act on a person's behalf. Yet people still forget what they once knew, miss what they are not looking at, fail to find the right words, and face hard choices without the benefit of their own history, because the machine that could help stands outside the situation. As AI moves into the physical world, attention has settled on one kind of intelligent individual, the embodied robot; we argue that the era of Physical AI holds a second kind of equal importance, the person augmented by AI. Alongside artificial general intelligence, which asks how intelligent a machine can be, stands AI-augmented human intelligence (AHI), which asks how much intelligence a machine can enable in a particular person. Realizing it calls for a new kind of system, a cognitive symbiont: a lifelong, embedded, real-time, private, low-friction, and proactive companion that senses what the person senses through external devices, keeps their context across years, models their situation and their mind, takes part in their thinking at the right moment, carries out everyday tasks with their context, and keeps learning the person as both change. We give the paradigm a conceptual core, the cognitive gap between what a person could bring to a situation and what they can hold in working memory, and organize its design space as a symbiosis loop of sensing, keeping, understanding, living alongside, acting for and thinking with the person, and growing, enclosed by a personal runtime and by trust. Because a symbiont changes what a person can do in front of others, it also raises risks of a new kind, from covert assistance in examinations to pressure on everyone to adopt it, and we treat their governance as part of the paradigm.

### 🤖 AI 总结

**一句话总结**：For a decade, progress in artificial intelligence has been measured by how much a machine can do on its own. Large foundation models now write code and run multistep tasks, and personal agents act on ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Autonomous, Cognitive, Symbionts, Toward, AI-Augmented, Human, Intelligence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05376v1) | [下载PDF](https://arxiv.org/pdf/2611.05376v1.pdf)

---

## [3. Suppressing Misaligned Behaviors in Language Models, Durably](https://arxiv.org/abs/2611.05358v1)

**作者**：Luxi He, Pengcheng Jiang, Jifan Zhang 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-11-03

### 📄 论文摘要

Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two model organisms--language models deliberately trained to exhibit a specific misalignment--that differ in what triggers the behavior. The narrow-trigger organism misbehaves only when the prompt contains a specific cue: it cheats on multiple-choice questions by following a planted hint that points to a wrong answer, and behaves normally otherwise. The broad-trigger organism has no such cue: after fine-tuning on insecure code, it gives harmful responses across a wide range of open-ended prompts. We then formalize post-hoc behavioral suppression and evaluate methods along three criteria: immediate suppression of the target behavior, durability under further training, and preservation of general capability. We compare standard methods--SFT, GRPO, and gradient-ascent unlearning--along these dimensions. Building on prior work on alignment shallowness, we hypothesize that more durable suppression requires the ability to recover from a wider range of misalignment states. We introduce Prefix-Expanded Adversarial Reinforcement Learning (PEARL), a GRPO variant that augments rollouts with continuations from intermediate states sampled along cached organism trajectories. Across both organism settings and two model families (Qwen3-4B, GPT-OSS-20B), PEARL achieves strong immediate suppression while preserving task accuracy, and remains durable under further fine-tuning on either the organism's data or unrelated data. It obtains the greatest benefit when the undesirable behavior is broad and cannot be addressed through targeted SFT. Together, our framework and method offer a step toward more durable post-hoc removal of undesired behaviors.

### 🤖 AI 总结

**一句话总结**：Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two model organisms--languag...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Suppressing, Misaligned, Behaviors, Language, Models, Durably, Undesired, model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05358v1) | [下载PDF](https://arxiv.org/pdf/2611.05358v1.pdf)

---

## [4. MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation for Efficient Dynamic Agent Self-Evolution](https://arxiv.org/abs/2611.05313v1)

**作者**：Dian Jin, Jinluan Yang, Kairong Han 等 12 位作者  
**分类**：cs.CL  
**发布时间**：2026-11-03

### 📄 论文摘要

Skill memories encode past experiences as textual prompts to improve reinforcement learning (RL) for self-evolving agents. Complementing RL, On-Policy Self-Distillation (OPSD) provides dense, fine-grained supervision to internalize knowledge from skill-guided trajectories and accelerate policy learning. However, self-generated memories often contain noisy supervision and functionally entangled, redundant, or conflicting knowledge, making direct distillation difficult. Under limited training budgets, these issues can hinder knowledge internalization and even degrade performance. To address this problem, we propose MDSKILL, a multi-view distillation approach for skill memory internalization. MDSKILL organizes skill memories into three complementary functional views (state grounding, action planning, and execution control) and selects high-quality skills using dynamic metrics to construct view-specific and integrated reasoning branches. OPSD then transfers and consolidates complementary experiential knowledge across these branches into a shared policy, enabling efficient skill internalization and continuous agent self-evolution. We evaluate MDSKILL on three agent benchmarks against RL, skill-augmented, and self-distillation baselines that do not rely on stronger external teacher models. Without additional computational overhead, MDSKILL improves upon SOTA performance by up to 7.1% and 8.1% on ALFWorld and WebShop. Extensive ablations and evolution analyses further validate its effectiveness in knowledge internalization and policy improvement. The code is available at https://anonymous.4open.science/r/MDSKILL-CF53.

### 🤖 AI 总结

**一句话总结**：Skill memories encode past experiences as textual prompts to improve reinforcement learning (RL) for self-evolving agents. Complementing RL, On-Policy Self-Distillation (OPSD) provides dense, fine-gra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MDSKILL, Learning, Internalize, Skill, Memory, through, Multi-View, Distillation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05313v1) | [下载PDF](https://arxiv.org/pdf/2611.05313v1.pdf)

---

## [5. Personas Are Not People: Identity as State, Not Attribute](https://arxiv.org/abs/2611.05292v1)

**作者**：Tamunotonye Harry, Yuanyuan Feng  
**分类**：cs.CL, cs.AI, cs.CY  
**发布时间**：2026-11-03

### 📄 论文摘要

Synthetic populations, large sets of simulated people, are increasingly used in place of real people to pretest surveys, simulate users and communities, and evaluate AI systems. Each simulated person is defined by a persona, a written profile of fixed traits, demographics, and attitudes that a language model is instructed to act out. Every such system assumes that a person's identity is a stable attribute that behaves the same way in every situation the simulation presents. We show that this assumption is not a harmless simplification. Three decades of personality research find the opposite. How a given person behaves varies more across contexts than people vary from one another. Drawing on identity economics, which describes how different situations activate different identities and norms within the same person, we separate behavior into three parts, which are stable traits, the identity a context calls up, and the situation itself. We then prove, under two stated assumptions, that any simulation built on fixed personas, no matter how detailed the personas or how large the underlying model, cannot reproduce the part of a population's behavior that is specific to it and its circumstances. We propose a new evaluation criterion based on this result and a person-in-context design that can meet it in principle. We test one version on a naturalistic Reddit personality corpus and on a published clinical-trial recruitment survey of a community with documented distrust of medical institutions. The design does produce context-dependent behavior when tested directly, but in neither setting does it fully match the real population, and we show where it falls short. The consequence for practice is a risk that synthetic-population evaluations misrepresent the groups whose behavior is most shaped by context, a distortion that richer personas cannot correct.

### 🤖 AI 总结

**一句话总结**：Synthetic populations, large sets of simulated people, are increasingly used in place of real people to pretest surveys, simulate users and communities, and evaluate AI systems. Each simulated person ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Personas, Not, People, Identity, State, Attribute, Synthetic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05292v1) | [下载PDF](https://arxiv.org/pdf/2611.05292v1.pdf)

---

## [6. Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment](https://arxiv.org/abs/2611.05287v1)

**作者**：Ariana M. Villegas-Suarez, Guido Freire, Sohan Venkatesh 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-11-03

### 📄 论文摘要

Fine-tuning a large language model (LLM) on harmful data in a narrow domain, such as bad medical advice, can make it broadly misaligned. How realistic this risk is remains unclear, since models are very rarely fine-tuned on explicitly harmful data in practice. In this work, we show that fine-tuning on data the model believes to be false but that has no harmful content, can also induce broad misalignment. Across mathematics, trivia, cooking and sports, the more strongly the model disbelieves the answers it is trained on, the more misaligned it becomes. In mathematics, misaligned answers rise from 4% to over 60% as the training answers become more wrong, with little loss of general capability. After fine-tuning, the model states the wrong answers but its multiple-choice probabilities still prefer the true ones, which suggests that misalignment comes from this internal inconsistency. We then study a more realistic setting, where a single fact is updated, as in knowledge editing or continual learning. The same relationship holds and the more the model still believes the true fact after training on the false one, the more misaligned it becomes. When we frame the same false fact as part of a coherent story, the model comes to believe it more deeply and becomes less misaligned than when we instruct it to assert the false fact. Content filters and persona vectors cannot tell these two framings apart, even though they lead to different levels of misalignment. These results suggest a risk for model updates, where training a model that does not adopt the new fact as true can induce misalignment even when the data looks harmless.

### 🤖 AI 总结

**一句话总结**：Fine-tuning a large language model (LLM) on harmful data in a narrow domain, such as bad medical advice, can make it broadly misaligned. How realistic this risk is remains unclear, since models are ve...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Knowingly, Wrong, Training, Against, Their, Own, Beliefs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05287v1) | [下载PDF](https://arxiv.org/pdf/2611.05287v1.pdf)

---

## [7. Beyond Accuracy: What Language-Subspace Interventions Capture, Remove, and Improve](https://arxiv.org/abs/2611.05278v1)

**作者**：Shaanil Punglia, Dadhichi Telwadkar, Vaibhav Rathore 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-11-03

### 📄 论文摘要

Language-subspace interventions aim to improve multilingual reasoning by suppressing language-related components in mid-layer activations. Using MATH and MGSM across four open-weight LLMs, we ask three questions: do estimated language subspaces capture translation-associated variation? Does projecting them out remove language information? And do they improve accuracy without compromising response language? For the first question, we build subspaces using the existing Mean-SVD construction and our DiffPCA. Both capture substantial translation-associated variation and show similar patterns across model depth. For the second, we project out each subspace and train linear probes to classify language from the projected activations. The probes still identify language almost perfectly, showing that neither subspace exhaustively captures language information. For the third, we evaluate several intervention configurations on Qwen2.5-7B, by varying subspace creation methods and intervention operators. We find that the intervention that most improves MGSM accuracy sacrifices response-language fidelity, with only one intervention improving joint accuracy--answers that are correct and in the target language--slightly, by 1.60 points. Interestingly, subtle changes in the prompt alone can reproduce the accuracy gains albeit with significant damage to language fidelity. We argue that causal interventions must be judged on more than accuracy, to fully account for language substitution trade-offs.

### 🤖 AI 总结

**一句话总结**：Language-subspace interventions aim to improve multilingual reasoning by suppressing language-related components in mid-layer activations. Using MATH and MGSM across four open-weight LLMs, we ask thre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Accuracy, What, Language-Subspace, Interventions, Capture, Remove, Improve

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05278v1) | [下载PDF](https://arxiv.org/pdf/2611.05278v1.pdf)

---

## cs.CV

## [8. Visibility-Aware Reference Generation for Benchmarking Visual 3D Reconstruction in Vegetation-Rich Environments](https://arxiv.org/abs/2611.05361v1)

**作者**：Zhipeng Zhong, Matthew Coombes, Cunjia Liu  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-11-03

### 📄 论文摘要

Reliable evaluation of visual 3D reconstruction and depth estimation in vegetation-rich outdoor environments is limited by the scarcity of geometric ground-truth data and the cost of complete scanner surveys. We present a LiDARbased reference-generation pipeline for evaluating the zero-shot performance of feed-forward visual-geometry models alongside conventional structure-from-motion (SfM) methods. The pipeline reuses camera images, LiDAR scans, and reference poses from existing multi-sensor localization datasets to generate per-view depth maps and visible reference point clouds. To address visibility errors in accumulated LiDAR scans, we introduce the LargeDepth-Gap Visibility Score (LDGVS) for point-wise visibility filtering and automatic scale selection in Hidden Point Removal(HPR). Experiments on TartanAirV2 and TartanGround show that, compared with Poisson surface reconstruction, which is an approach suited to completed scan surveys, the combined HPR and LDGVS filtering retains approximately three times the point density at comparable absolute relative error. We also apply the pipeline to the BotanicGarden dataset to systematically compare depth estimation and 3D reconstruction methods. Feedforward methods produce dense depth predictions efficiently, but their 3D reconstructions can contain duplicated structures. Conventional SfM generally produces more coherent geometry, but its reconstructions remain sparse and more prone to failure in challenging vegetated scenes. The benchmark toolkit and datasets will be released.

### 🤖 AI 总结

**一句话总结**：Reliable evaluation of visual 3D reconstruction and depth estimation in vegetation-rich outdoor environments is limited by the scarcity of geometric ground-truth data and the cost of complete scanner ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Visibility-Aware, Reference, Generation, Benchmarking, Visual, Reconstruction, Vegetation-Rich

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05361v1) | [下载PDF](https://arxiv.org/pdf/2611.05361v1.pdf)

---

## [9. GSCV++: Lightweight 3D Gaussian Splatting Sequence Compression via Standard Video Codecs](https://arxiv.org/abs/2611.05359v1)

**作者**：Qi Yang, Yingzhan Xu, Kai Zhang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-03

### 📄 论文摘要

This paper presents GSCV++, a lightweight pipeline for 3D {G}aussian {S}platting (GS) sequences {C}ompression with standard {V}ideo codecs. To meet the requirements of low-complexity and hardware compatibility from the industry, GSCV++ jointly improves preprocessing, 3D-to-2D mapping, and practical video compression configuration of GS compression. First, for preprocessing, energy-adaptive inter-frame spherical harmonic (SH) alternative current (AC) dimensionality reduction (EA-SHDR) is proposed to produces a compact and stable temporal SH AC feature space. It can reduce the data volume of following mapping and practical compression, as well as less complexity while eliminating redundant information. Second, for 3D-to-2D mapping, prior-based Inter-MiniPLAS (P-MiniPLAS) is designed to generate smooth 2D feature maps through prior-based weighting factor inference and small scale remapping. Compared with vanilla Parallel Linear Assignment Sorting (PLAS) and Morton scan, P-MiniPLAS ensures the generated 2D maps are more suitable for the video codec while maintaining a low level of computational complexity. Third, for practical compression, content-aware generalized compression (CA-GC) is developed to use a non-uniform bit-depth split for coordinate map generation, and a coding unit size selection is introduced for efficient compression complexity control, which fully exploits the performance of video codecs without involving normative changes. Experiments demonstrate that GSCV++ reports over 20\% in intra- and 60\% in inter-prediction rate-distortion gains compared with state-of-the-art (SOTA) methods. GSCV++ also achieves faster 2D map generation, encoding, and decoding than other SOTA methods using the same type of video codecs. Ablation studies verify the effectiveness and robustness of the proposed modules and provide insights for subsequent research.

### 🤖 AI 总结

**一句话总结**：This paper presents GSCV++, a lightweight pipeline for 3D {G}aussian {S}platting (GS) sequences {C}ompression with standard {V}ideo codecs. To meet the requirements of low-complexity and hardware comp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, GSCV++, Lightweight, Gaussian, Splatting, Sequence, Compression, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05359v1) | [下载PDF](https://arxiv.org/pdf/2611.05359v1.pdf)

---

## [10. OpenBrain: An Auditable Generated-Label Release for Whole-Brain MRI Parcellation](https://arxiv.org/abs/2611.05348v1)

**作者**：Qizhen Lan, Yu-Chun Hsu, Yuxiang Wei 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-03

### 📄 论文摘要

Automatic tools can now generate whole-brain MRI parcellations at cohort scale, but generated-label releases often provide little evidence about which cases are reliable enough to reuse. We introduce OpenBrain, a confidence-aware release of 35,838 provenance-verified OpenNeuro T1w cases from 607 source datasets. OpenBrain is organized as an auditable case-record release rather than a directory of standalone segmentation files: each record links a primary parcellation, two committee parcellations, source/license provenance, raw QC-7 measurements, percentile risks, a combined risk score R, and a confidence tier. QC-7 is a reference-free reliability panel over label geometry, image-label consistency, and committee disagreement, so users can filter, weight, audit, or re-threshold generated labels without rerunning inference. We evaluate this released evidence under a frozen protocol. Across external cohorts, lower QC-7 risk corresponds to higher generated-label quality; in fixed-budget training, lower-risk selections improve paired macro Dice over random selection by +3.2 to +3.7 percentage points. OpenBrain also exposes raw axes, committee outputs, provenance, and datasheet documentation, so confidence claims remain inspectable after download. It does not turn generated labels into manual annotations or clinical-grade segmentations. Its contribution is a large open generated-parcellation substrate, a reusable case-level risk-evidence layer, and an external validation protocol for release-time QC. Dataset: https://huggingface.co/datasets/lanqz7766/OpenBrain. Code: https://github.com/lanqz7766/openbrain.

### 🤖 AI 总结

**一句话总结**：Automatic tools can now generate whole-brain MRI parcellations at cohort scale, but generated-label releases often provide little evidence about which cases are reliable enough to reuse. We introduce ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, OpenBrain, Auditable, Generated-Label, Release, Whole-Brain, MRI, Parcellation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05348v1) | [下载PDF](https://arxiv.org/pdf/2611.05348v1.pdf)

---

## [11. Wonder 4: A Mixture-of-Experts Recipe for Image Quality Enhancement](https://arxiv.org/abs/2611.05294v1)

**作者**：Yunan Wu, Bin Sun, Partha Acharjee 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-03

### 📄 论文摘要

A real photograph is often blurry, grainy, compressed, scratched, and low-resolution at the same time. Each defect has its own severity and its own place in the image. The corrections for these defects conflict with each other. Exist- ing models describe the whole image with one description, so they cannot say where each correction belongs. To solve this problem, we present Wonder 4, a mixture-of-experts (MoE) model for image quality enhancement. It corrects several defects of a real photograph at the same time, each in the region where it occurs. Every block of the model holds a mixture of N = 13 experts. A router, trained with the model, sends every image patch to k = 5 of them. No degradation classifier, mask, prompt, detector, or task label is used. Another issue is that standard MoE training, taken from language models, pushes every expert toward equal use. Equal use applies every correction everywhere, even where it is not needed. We replace this rule with a bias that only sets a minimum share of use. Across all patches, an expert used less than this minimum gets higher router scores until it is selected again. An expert above the minimum is not changed, so no expert is forced to be used as often as the others. The bias needs no extra loss. The method adds no extra module and no extra processing step. We evaluate Wonder 4 on DIV2K and Flickr2K, against five published methods and three open-weight pipelines. It reaches the best LPIPS, DISTS, and NIQE on all three test settings (DIV2K x4, DIV2K x8, and Flickr2K x4).

### 🤖 AI 总结

**一句话总结**：A real photograph is often blurry, grainy, compressed, scratched, and low-resolution at the same time. Each defect has its own severity and its own place in the image. The corrections for these defect...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Wonder, Mixture-of-Experts, Recipe, Image, Quality, Enhancement, real, photograph

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05294v1) | [下载PDF](https://arxiv.org/pdf/2611.05294v1.pdf)

---

## [12. Low-Density 3D Point Cloud Classification](https://arxiv.org/abs/2611.05291v1)

**作者**：Ahmed Baha Ben Jmaa, Faten Chaieb  
**分类**：cs.CV  
**发布时间**：2026-11-03

### 📄 论文摘要

3D point cloud classification, a task in computer vision, has recently gained substantial interest due to its extensive applications across various domains such as augmented and virtual reality, robotics, and autonomous driving. However, classifying 3D point clouds becomes challenging in real-world scenarios where the density levels vary. These variations are due to limitations inherent to current sensing technologies and variable environmental conditions, which often prevent the capture of detailed and comprehensive geometric representations. Existing classification methods, which have demonstrated impressive results on dense point clouds, may be affected and could experience reduced performance when dealing with low-density point clouds. Addressing this challenge, this paper introduces LD-PointNet++, an architecture optimized for the classification of low-density point clouds. To pave the way for LD-PointNet++, we conduct the first benchmarking study that systematically evaluates state-of-the-art point cloud classification methods across varying densities, revealing significant performance declines in low-density environments. Experimental results on the ModelNet benchmark dataset demonstrate that LD-PointNet++ not only outperforms these methods in low-density scenarios but also demonstrates consistent accuracy above 90% across different density levels.

### 🤖 AI 总结

**一句话总结**：3D point cloud classification, a task in computer vision, has recently gained substantial interest due to its extensive applications across various domains such as augmented and virtual reality, robot...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Low-Density, Point, Cloud, Classification, task, computer, vision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05291v1) | [下载PDF](https://arxiv.org/pdf/2611.05291v1.pdf)

---

## [13. Anchored Rank-Adversarial Fine-Tuning Pretrained Visual Place Recognition Models](https://arxiv.org/abs/2611.05286v1)

**作者**：Mostafa Kira, Bader Rasheed, Manuel Mazzara  
**分类**：cs.CV  
**发布时间**：2026-11-03

### 📄 论文摘要

Visual place recognition (VPR) localises a camera by retrieving similar geo-tagged images, and current foundation-model VPR models are accurate across cities, seasons and illumination, but not robust to adversarial perturbations: under a white-box attack on the ranking at an imperceptible budget of 1/255, SuperVLAD and BoQ keep at most 0.2% top-1 recall (R@1) on four benchmarks. We propose anchored rank-adversarial fine-tuning (ARAFT), which fine-tunes a released model with a listwise rank loss on each adversarial query's hardest positive and an anchor to the clean descriptor of the frozen pretrained model. Checkpoints are selected under a clean-accuracy budget fixed in advance, and the full trade-off is reported. Within five validation R@1 points of clean cost, plain adversarial training has no admissible checkpoint, whereas ARAFT raises robust R@1 from zero to 47.3 on SuperVLAD and 55.3 on BoQ; plain adversarial training exceeds this only at about three times the clean cost. Against unbudgeted plain adversarial training on the test sets, ARAFT matches its robust R@1 at 2/255 with about ten more clean R@1 points. At 4/255, plain adversarial training is 6-9 robust R@1 points ahead, while ARAFT still keeps its ten-point clean advantage. Developed on SuperVLAD, ARAFT transfers to BoQ without re-tuning, and its robustness holds against stronger optimisers, with no sign of gradient masking.

### 🤖 AI 总结

**一句话总结**：Visual place recognition (VPR) localises a camera by retrieving similar geo-tagged images, and current foundation-model VPR models are accurate across cities, seasons and illumination, but not robust ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Anchored, Rank-Adversarial, Fine-Tuning, Pretrained, Visual, Place, Recognition, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05286v1) | [下载PDF](https://arxiv.org/pdf/2611.05286v1.pdf)

---

## [14. YANAMI: A Large-Scale Multimodal Dataset and Benchmark for Multiturn Stateful Interaction](https://arxiv.org/abs/2611.05280v1)

**作者**：Shengyu Wang, Tengyue Nong, Junming Liu 等 13 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-03

### 📄 论文摘要

Unified Multimodal Models (UMMs) integrate visual understanding, generation, and editing within a single unified framework. However, existing unified multimodal datasets and benchmarks remain dominated by single-turn tasks. Even in recent multi-turn datasets, many turns can be solved independently without tracking information across turns. Consequently, they provide limited supervision and evaluation for multimodal stateful interaction, which requires models to understand, maintain, update, and faithfully realize evolving dialogue states across turns. To address this gap, we introduce YANAMI, the first large-scale multimodal dialogue dataset and benchmark for stateful interaction, comprising YANAMI-400K and YANAMI-Bench. YANAMI-400K contains 400K multi-turn multimodal dialogues, with more than 2M images and 2.6M dialogue turns. The dialogues span four representative scenarios: Multi-Image Fusion, Image Editing, World Modeling, and Visual Reasoning, and require models to continuously track, preserve, and revise evolving multimodal dialogue states across turns. YANAMI-Bench comprises 400 multi-turn dialogues for systematically evaluating multimodal stateful interaction. It jointly evaluates Dialogue State Understanding and Visual Realization, characterizing the gap between models' ability to understand evolving dialogue states and their ability to faithfully realize them in visual outputs. Experiments show that fine-tuning BAGEL on YANAMI-400K improves image editing, generation, and multimodal stateful interaction by 10.3%, 2.0%, and 13.23%, respectively, while preserving its general visual understanding capabilities. Evaluations on YANAMI-Bench further reveal that existing UMMs still struggle to maintain, update, and visually realize evolving multimodal dialogue states.

### 🤖 AI 总结

**一句话总结**：Unified Multimodal Models (UMMs) integrate visual understanding, generation, and editing within a single unified framework. However, existing unified multimodal datasets and benchmarks remain dominate...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：YANAMI, Large-Scale, Multimodal, Dataset, Benchmark, Multiturn, Stateful, Interaction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05280v1) | [下载PDF](https://arxiv.org/pdf/2611.05280v1.pdf)

---

## [15. Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems](https://arxiv.org/abs/2611.05275v1)

**作者**：Pengfei Zhou, Yixing Ma, Hexin Wang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-03

### 📄 论文摘要

Artificial general intelligence (AGI) requires a method that can understand, generate, reason, and act across diverse domains and modalities. Rather than relying on a single model to master every capability, a promising path toward AGI now is to orchestrate a heterogeneous ecosystem of specialized models, tools, and policies (candidates) into a unified AI system. At the heart of this vision lies a fundamental question: how can an AI system dynamically select and coordinate the most capable candidate for each task while balancing performance and computational cost? In this work, we present Route Anything, a unified framework for studying model and policy routing across general-purpose AI systems. We develop a unified theoretical foundation that characterizes optimal routing under quality--cost trade-offs and establishes how the information available to a router determines its attainable performance. To systematically investigate routing across diverse capabilities, we first construct an omni-modal trajectory matrix spanning 25 benchmarks across language understanding, image, video, and speech generation, coding and workplace agents, and robotic manipulation, comprising 374,401 scored runs from 452 candidate configurations. Building on this framework, we train and test different routers to investigate the potential of omni-modal model routing, the capabilities of learned routers, and the conditions under which routing improves efficiency. Our results reveal substantial opportunities for capability orchestration: per-input oracle routing outperforms the best fixed candidate by 5.4 points, and learned routers outperform it by 0.3 points across 16 benchmarks, by 2.1 points on video generation, and by 1.1 points on robot manipulation while using 24% less policy time. More importantly, routing raises efficiency by 8.82x on average compared with the reference model.

### 🤖 AI 总结

**一句话总结**：Artificial general intelligence (AGI) requires a method that can understand, generate, reason, and act across diverse domains and modalities. Rather than relying on a single model to master every capa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Route, Anything, Study, Model, Policy, Routing, General-Purpose

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05275v1) | [下载PDF](https://arxiv.org/pdf/2611.05275v1.pdf)

---

## [16. Diagnosis by Composition: Detecting and Localizing Unseen Diseases by Composing Learned Radiological Findings](https://arxiv.org/abs/2611.05231v1)

**作者**：Kaihua Hou, Wei Liu, Yi Huang 等 13 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-03

### 📄 论文摘要

Deep models for radiological diagnosis are typically trained to predict disease labels directly from images, which limits them to diseases seen during training and makes their decisions hard to interpret in radiologists' terms. Radiology, however, proceeds from visual findings to disease through published guidelines that make this decision rule explicit, interpretable, and reproducible. We introduce diagnosis by composition (DbC), a representation learning framework that encodes this findings-first logic. DbC learns a vocabulary of radiological findings by aligning image features with the text embeddings of the findings, each finding represented as a dense map over the scan. A disease is defined by a set of required findings derived from its guidelines, and its diagnosis map is a fixed, parameter-free composition of the corresponding finding maps. Because the finding-to-disease mapping is derived from guidelines rather than learned, DbC is interpretable and auditable by design, can extend to new diseases by specifying their findings without retraining, and can diagnose unseen diseases by composing their findings. On multi-phase liver CT, DbC detects and localizes unseen diseases, rare diseases from a different institution, and an external cohort significantly better than all comparators, including models that align images with disease names. DbC also improves detection and localization in the fully supervised setting and remains superior across training-set sizes. Although demonstrated on liver CT, DbC applies wherever radiological guidelines define diseases through findings.

### 🤖 AI 总结

**一句话总结**：Deep models for radiological diagnosis are typically trained to predict disease labels directly from images, which limits them to diseases seen during training and makes their decisions hard to interp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diagnosis, Composition, Detecting, Localizing, Unseen, Diseases, Composing, Learned

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05231v1) | [下载PDF](https://arxiv.org/pdf/2611.05231v1.pdf)

---

## [17. PLANTEUR: A Crop-Type Segmentation Benchmark for Tropical Regions](https://arxiv.org/abs/2611.05223v1)

**作者**：Piper Wolters, Gabriel Tseng, Favyen Bastani 等 7 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-03

### 📄 论文摘要

We introduce PLANTEUR, a benchmark for crop-type mapping from satellite images in the French overseas territories. Building on the PASTIS design, PLANTEUR provides georeferenced and aligned Sentinel-2, Sentinel-1, and Landsat-8 sequences with parcel-derived labels spanning six tropical regions and an 8-class label space. We define both a standard test split and a leave-one-island-out protocol to measure cross-territory generalization, and evaluate fully supervised models, linear probes, and fine-tuned foundation models. The benchmark code and data are open source and available on GitHub and Hugging Face.

### 🤖 AI 总结

**一句话总结**：We introduce PLANTEUR, a benchmark for crop-type mapping from satellite images in the French overseas territories. Building on the PASTIS design, PLANTEUR provides georeferenced and aligned Sentinel-2...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, PLANTEUR, Crop-Type, Segmentation, Benchmark, Tropical, Regions, introduce

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05223v1) | [下载PDF](https://arxiv.org/pdf/2611.05223v1.pdf)

---

## [18. Diffusion Plug-in Priors for Self-Supervised Ultrasound Video Restoration](https://arxiv.org/abs/2611.05206v1)

**作者**：Chu Chen, Mingduo He, Yining Li 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-03

### 📄 论文摘要

\textit{Objective:} Ultrasound videos are limited by hardware-constrained spatial resolution and signal-dependent speckle, while paired low- and high-resolution acquisitions for supervised restoration are rarely available. We aim to jointly super-resolve and despeckle ultrasound videos without paired training data or network retraining. \textit{Methods:} We propose UltraDiff, which uses a frozen pre-trained diffusion model (DM) as a plug-in prior and restores each frame by optimizing the latent seed of the DM sampler under a range-constrained maximum a posteriori formulation. We derive a speckle-aware data-fidelity term from a Rayleigh scale-family model and characterize its relative-residual and variance-adaptive weighting properties. We further introduce a stabilized fidelity that is bounded below and strictly convex in log intensity for positive observations in its unclamped form. A total-variation regularizer complements the DM prior, and a temporal seed update warm-starts each frame from the optimized seed of its predecessor. \textit{Results:} On EchoNet-LVH videos with simulated speckle and additive noise, UltraDiff with a natural-image prior improves PSNR by 1.24\,dB over the strongest baseline, and ultrasound-related priors improve it further. On real clinical echocardiography videos, UltraDiff reduces the mean absolute error of zero-shot ejection fraction (EF) prediction from 7.31 to 6.37 EF points relative to DUP, the strongest baseline. \textit{Conclusion:} Combining a speckle-aware fidelity with frozen diffusion priors enables ground-truth-free ultrasound video restoration that benefits downstream measurement. \textit{Significance:} UltraDiff needs neither paired data nor retraining and is not tied to a specific diffusion checkpoint. Code associated with this work will be made publicly available upon acceptance.

### 🤖 AI 总结

**一句话总结**：\textit{Objective:} Ultrasound videos are limited by hardware-constrained spatial resolution and signal-dependent speckle, while paired low- and high-resolution acquisitions for supervised restoration...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Plug-in, Priors, Self-Supervised, Ultrasound, Video, Restoration, textit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05206v1) | [下载PDF](https://arxiv.org/pdf/2611.05206v1.pdf)

---

## cs.LG

## [19. Agnostic Learning by Imitating](https://arxiv.org/abs/2611.05346v1)

**作者**：Sílvia Casacuberta, Parikshit Gopalan, Varun Kanade 等 6 位作者  
**分类**：cs.LG, cs.CC, cs.DS  
**发布时间**：2026-11-03

### 📄 论文摘要

Given a class of machine learning models and sample access to a data distribution with binary labels, which computational task is harder: training a discriminative model that distinguishes positive and negative labels as well as the best member of the class, or training a generative model whose outputs are indistinguishable from real data by all members of the class? We prove that these two fundamental tasks in computational learning theory are not just closely related, but actually equivalent to each other in complexity. One direction of this equivalence was previously known. Indeed, the powerful regularity lemma in complexity theory gives an efficient oracle reduction from the indistinguishability task (a.k.a. multiaccuracy) to the distinguishing task (a.k.a. agnostic learning) in the style of boosting algorithms. Our main contribution is an efficient oracle reduction in the other direction. Taking this idea further, we show that a multiaccuracy oracle is a remarkably powerful primitive, achieving not just agnostic learning but also a wide range of seemingly more demanding learning objectives via similarly efficient and direct constructions. Our results crucially use the power of making adaptive queries to the oracle, and stand in stark contrast to prior work, which showed that post-processing a single multiaccurate predictor is insufficient for even weak forms of learning. On a technical level, we draw a connection between our (offline) problem and a version of no-regret learning in the online setting, which allows us to use follow-the-leader type algorithms to modify the label distribution and aggregate the predictions of the multiaccuracy oracle.

### 🤖 AI 总结

**一句话总结**：Given a class of machine learning models and sample access to a data distribution with binary labels, which computational task is harder: training a discriminative model that distinguishes positive an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agnostic, Learning, Imitating, Given, class, machine, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05346v1) | [下载PDF](https://arxiv.org/pdf/2611.05346v1.pdf)

---

## [20. CATF: A Manager-Worker Framework for Context-Aware Time-Series Forecasting](https://arxiv.org/abs/2611.05325v1)

**作者**：Yueqiao Chen, Dongyu Liu  
**分类**：cs.LG  
**发布时间**：2026-11-03

### 📄 论文摘要

We study context-aware time-series forecasting, in which a single target variable is predicted from its own history and a set of contextual variables, such as weather and calendar information. As the context becomes more diverse, a single model struggles to capture all of its regimes, while ensemble learning and Mixture-of-Experts approaches rely on manual data partitioning or soft routing, which increases the inference cost and hinders interpretability. We propose CATF, a Context-Aware Time-Series Forecasting framework built on a Manager-Worker architecture: a Transformer-based Manager routes each input to a single Worker based on the context, using hard routing during both training and inference. The Workers thus specialize without manual data partitioning, and any single-model forecaster can serve as a Worker. On five context-rich datasets, four horizons, and two normalization schemes, CATF improves over its standalone counterpart in 162 of 200 comparisons, the best CATF-enhanced model outperforms the best standalone baseline in 19 of 20 settings, and it outperforms the zero-shot Time-MoE foundation model in 15 of 20 settings. A case study on bike-sharing data shows that the Manager routes inputs by the calendar and that each Worker specializes in a different weekly pattern.

### 🤖 AI 总结

**一句话总结**：We study context-aware time-series forecasting, in which a single target variable is predicted from its own history and a set of contextual variables, such as weather and calendar information. As the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, CATF, Manager-Worker, Framework, Context-Aware, Time-Series, Forecasting, study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05325v1) | [下载PDF](https://arxiv.org/pdf/2611.05325v1.pdf)

---

## [21. Universal Hardness From Masking Channels](https://arxiv.org/abs/2611.05296v1)

**作者**：Parikshit Gopalan, Manoj Prabhakaran, Pranay Tankala  
**分类**：cs.LG, cs.CC  
**发布时间**：2026-11-03

### 📄 论文摘要

We prove a broad learning-theoretic generalization of the celebrated hardcore lemma concerning the average-case complexity of computing a Boolean function (Impagliazzo, 1995). Our starting point is the observation that the classic notion of a hardcore measure, which reweights a function's input distribution, is equivalent to an input-dependent masking channel that injects randomness into the function's output distribution until it appears fully pseudorandom. The analogue of density of the measure is the fidelity of the channel. From this viewpoint, we develop a general framework for certifying hardness that allows for non-Boolean functions $f$ and a wide range of notions of hardness besides the classic 0-1 loss, by choosing the right notion of fidelity via convex duality. We show the difficulty of learning $f$ using a class $\mathcal{C}$ to minimize a convex loss is tightly characterized by the maximum fidelity possible for a masking channel, which measures the least amount of noise the channel must add to hide the structure of $f$ and make it $\mathcal{C}$-indistinguishable from random noise. Using our framework, we derive a number of multiclass generalizations of the hardcore lemma, and reveal some unexpected subtleties in going to larger alphabets. We construct a universal masking channel that applies to many natural notions of hardness simultaneously. Such channels are dual to omnipredictors, which optimize multiple losses at once (Gopalan, Kalai, Reingold, Sharan, and Wieder, 2022). We observe a symmetry between masking channels and generalizations of the hardcore lemma using pseudoentropy. We present a tight characterization of pseudoentropy using the MaxEnt algorithm from machine learning. A long line of research has shown that learning and hardness are two sides of the same coin; our framework gives a crisp and general formulation of this principle via convex duality.

### 🤖 AI 总结

**一句话总结**：We prove a broad learning-theoretic generalization of the celebrated hardcore lemma concerning the average-case complexity of computing a Boolean function (Impagliazzo, 1995). Our starting point is th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Universal, Hardness, Masking, Channels, prove, broad, learning-theoretic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05296v1) | [下载PDF](https://arxiv.org/pdf/2611.05296v1.pdf)

---

## [22. De Rham cohomological architectures for PINNs and PDEs with topological holes](https://arxiv.org/abs/2611.05276v1)

**作者**：Andrew Gracyk  
**分类**：cs.LG, math.NA  
**发布时间**：2026-11-03

### 📄 论文摘要

We attempt to alleviate failure modes of classical physics-informed neural networks (PINNs) in scenarios of topological pathologies corresponding to punctures, holes, poles, and voids by introducing de Rham cohomological augmentations, or Hodge-de Rham PINNs. Vanilla PINNs often encounter pitfalls in hole-based settings due to discontinuous interfaces, nonzero closed path integration, path dependence, correspondence to exact forms via the exterior derivative, etc., therefore we absolve traditional failures via parameterizing a 1-form by the Hodge-Morrey-Friedrichs (HMF) decomposition for manifolds with boundary, drawing a connection to de Rham cohomology such as through the HMF isomorphism theorem. 1-forms can act as representations of scalar-valued PDE solutions through integral operator mappings. We propose performing a PINN-based loss on the parameterized 1-form through an associated PDE, which subsequently solves the potential-based PINN problem and moreover remedies the failures of vanilla PINNs via the Sobolev-regular operator under a Fréchet differentiation interconnection. The operator relationship often has a nontrivial closed-form and often requires integration or a case-by-case analysis, which we address thoroughly in our experiments. When an integrability condition is not met on our losses, we can equip exhaustion functions to train the networks. We demonstrate our methods on the Aharonov-Bohm effect, which, to our understanding, is largely nonexistent in PINN literature. We develop theoretical guarantees of our methods and demonstrate our pathological safeguards on a broad selection of topologically-adverse problems, including scenarios of inexact forms, and those of nontrivial harmonics and coexact terms.

### 🤖 AI 总结

**一句话总结**：We attempt to alleviate failure modes of classical physics-informed neural networks (PINNs) in scenarios of topological pathologies corresponding to punctures, holes, poles, and voids by introducing d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：De, Rham, cohomological, architectures, PINNs, PDEs, topological, holes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05276v1) | [下载PDF](https://arxiv.org/pdf/2611.05276v1.pdf)

---

## [23. iGC: Antibody Optimization via Reinforcement Learning over a Learned Somatic Hypermutation Prior](https://arxiv.org/abs/2611.05270v1)

**作者**：Thao Nguyen, Robert G. Alberstein, Ewa Nowara 等 13 位作者  
**分类**：cs.LG, q-bio.BM  
**发布时间**：2026-11-03

### 📄 论文摘要

Antibody affinity maturation is a natural optimization process in which B cells acquire mutations through somatic hypermutation (SHM), undergo selection for improved antigen binding, and iteratively evolve toward higher affinity. Computationally modeling this process requires capturing both biologically plausible mutations and antigen-specific selection. However, existing mutation models do not directly optimize binding, while affinity optimization often neglects realistic mutation trajectories.   We introduce iGC (in silico Germinal Centers), a two-stage reinforcement learning (RL) framework for antigen-specific antibody optimization. Stage 1 learns an SHM mutation prior from parent-child pairs in B-cell lineage trees and adapts it to a target affinity-maturation dataset. Stage 2 initializes an RL policy from this prior and optimizes antigen binding with Kullback-Leibler (KL) regularization toward the frozen prior. To prevent reward exploitation, including repetitive high-reward substitutions and structurally tolerated framework mutations, we introduce a Reward-Tax Meta-Gradient objective. RewardNet smooths the affinity landscape, while TaxNet penalizes reward overexploitation, jointly defining a learned meta-reward for policy optimization.   We evaluate iGC on mutation prediction, SHM consistency, affinity optimization, and mutation diversity. The mutation prior more than doubles the strongest baseline in mutation-site prediction. Following RL optimization, iGC maintains SHM sequence structure. It also achieves a strong exploration-exploitation balance, yielding competitive reward-diversity products across candidate-selection cutoffs. These results demonstrate that iGC integrates biologically plausible mutation generation with antigen-specific affinity selection, providing an in silico framework for iterative antibody affinity maturation.

### 🤖 AI 总结

**一句话总结**：Antibody affinity maturation is a natural optimization process in which B cells acquire mutations through somatic hypermutation (SHM), undergo selection for improved antigen binding, and iteratively e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：iGC, Antibody, Optimization, via, Reinforcement, Learning, over, Learned

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05270v1) | [下载PDF](https://arxiv.org/pdf/2611.05270v1.pdf)

---

## [24. Stabilizing On-Policy Targeted Guidance in Agentic Reinforcement Learning](https://arxiv.org/abs/2611.05266v1)

**作者**：Kevin Frans, Alexander M Rush, Sergey Levine 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-03

### 📄 论文摘要

Naive on-policy RL is often bottlenecked by the capabilities of the base model --- insufficient coverage can result in an inability to learn from certain rewards. At the same time, rewards in modern post-training systems often come from rich textual sources, e.g. judge models with a rubric of criteria. Can we utilize such structures to provide a rich directional signal that enables improving on otherwise difficult to optimize rewards? In this work, we examine a framework we refer to as targeted guidance that learns from per-turn textual feedback via an on-policy self-distillation objective. Our focus is not only on directly improving hard-to-optimize behaviors, but on how to do so throughout the training process without degrading baseline RL performance. Over a range of settings across an agentic multi-turn software engineering environment, we find success by combining targeted self-distillation with a per-criteria RL reward, and by limiting feedback to turns where the policy specifically fails. We further examine the design choices that lead to stable entropy and reduce oscillatory behavior throughout training.

### 🤖 AI 总结

**一句话总结**：Naive on-policy RL is often bottlenecked by the capabilities of the base model --- insufficient coverage can result in an inability to learn from certain rewards. At the same time, rewards in modern p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Stabilizing, On-Policy, Targeted, Guidance, Agentic, Reinforcement, Learning, Naive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05266v1) | [下载PDF](https://arxiv.org/pdf/2611.05266v1.pdf)

---

## [25. NovoCRF: Globally Normalized De Novo Peptide Sequencing on a Prefix-Mass Lattice](https://arxiv.org/abs/2611.05260v1)

**作者**：Rui Qiao, Lei Xin, Baozhen Shan  
**分类**：cs.LG  
**发布时间**：2026-11-03

### 📄 论文摘要

De novo peptide sequencing has moved from dynamic programming over hand-designed or generative scores to large transformers that learn the task end to end. We present NovoCRF, a conditional random field (CRF) whose states are prefix masses, so that its paths are exactly the peptides within +/-0.06 Da of the precursor mass. A small network scores each edge from physics-derived ion-match features and is trained with its scores globally normalized over all mass-feasible peptides. To our knowledge, NovoCRF is the first de novo method trained with exact normalization over all mass-feasible peptides. Our software has three modules, each with exactly one job: a precursor mass finder recovers the accurate precursor mass from MS1, the CRF finds the peptides that fit the precursor mass by exact k-best decoding, and two BiGRU rerankers add sequence context and internal-fragment evidence. The model has 310k parameters and trains in about 17 GPU-hours. On seven held-out data-dependent acquisition datasets published in 2026 (126,262 labeled spectra), NovoCRF's mean peptide recall is 42.4%, against 39.1% for Casanovo v5 with five beams, and its amino-acid recall 64.0% against 53.1%, at 1,746 spectra/s on 18 CPU threads, 55x Casanovo's throughput on a GPU. Split by fragment evidence, NovoCRF leads on labels with up to three peptide bonds without a b or y ion, and Casanovo only beyond. NovoCRF can also search modifications it was never trained on at their exact mass: it finds 32.1% of the hydroxyproline peptides of a lion bone sample.

### 🤖 AI 总结

**一句话总结**：De novo peptide sequencing has moved from dynamic programming over hand-designed or generative scores to large transformers that learn the task end to end. We present NovoCRF, a conditional random fie...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：De, NovoCRF, Globally, Normalized, Novo, Peptide, Sequencing, Prefix-Mass

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05260v1) | [下载PDF](https://arxiv.org/pdf/2611.05260v1.pdf)

---

## [26. Shrinkage prior for implicit generative models](https://arxiv.org/abs/2611.05241v1)

**作者**：Shreya Sinha-Roy, Christian P. Robert, Ritabrata Dutta  
**分类**：cs.LG, stat.CO  
**发布时间**：2026-11-03

### 📄 论文摘要

Implicit generative models based on deep neural networks have revolutionized many scientific fields, from weather research to language generation. They successfully model complex random objects arising in real-world problems. In this work, we propose a sample-efficient training mechanism for these models. Our approach leverages regularized inference with shrinkage priors and generalized Bayes. In the large $p$ (parameter dimension) and small $n$ (sample size) setting, sparsity-inducing priors have been successfully used for linear regression when $p \gg n$. However, their application to implicit generative models remains challenging due to the intractability of the likelihood function. To address this, we adapt a scoring rule posterior based on a strictly proper scoring rule, following the generalized Bayes framework. We then propose a block SGMCMC within Gibbs sampling mechanism. This enables efficient exploration of high-dimensional parameter spaces by identifying a sparse representation of neural implicit generative models. We demonstrate the performance of our proposed method through experiments on $p \gg n$ linear regression and an application of neural generative models.

### 🤖 AI 总结

**一句话总结**：Implicit generative models based on deep neural networks have revolutionized many scientific fields, from weather research to language generation. They successfully model complex random objects arisin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Shrinkage, prior, implicit, generative, models, deep, neural, networks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05241v1) | [下载PDF](https://arxiv.org/pdf/2611.05241v1.pdf)

---

## [27. Post-Inference Model Chaining: A Problem Statement and a Model-based Bootstrap for Training End-to-End Digital Twins](https://arxiv.org/abs/2611.05225v1)

**作者**：Lukas Madenach, Timo Bailer, Tobias Eilert  
**分类**：cs.LG, stat.ME  
**发布时间**：2026-11-03

### 📄 论文摘要

End-to-end digital twins can be constructed by fitting separate stage models and connecting them after inference. We investigate the Frequentist prediction properties of a commonly used Monte Carlo simulation scheme that forwards complete predictive draws through such a chain when measured stage outputs contain independent normal errors, but the latent stage means are deterministic. Analytical two-stage examples show persistent asymptotic interval and coverage inflation and, with quadratic propagation, mean bias dependent on the parameters to be estimated. Simulations of four- and eight-stage linear-quadratic univariate chains with 7, 15 or 30 training runs demonstrate pronounced input-dependent distortions. A diagnostic using error-free latent training predictors shows that the effect is mainly not attributable to errors in variables, but to the MCSim approach even showing underestimation of coverage. We propose a model-based bootstrap: an initial chain forwards fitted means, bootstrap chains are refitted on fixed-center bootstrap data while forwarding their mean prediction, and a target-stage future error enters a studentized prediction root. Across the investigated scenarios, relative mean bias is substantially reduced, and coverage is closer to the nominal 90%. At sample size 30, the eight-stage bootstrap has mean width ratios of 1.16-1.42 relative to the known-parameter normal reference, compared with 4.11-4.97 for observed-to-observed MCSim. These results support improved endpoint prediction in the tested setting. Further investigations of the bootstrap scheme in the supplement for a bivariate 6-stage process show similar satisfactory results.

### 🤖 AI 总结

**一句话总结**：End-to-end digital twins can be constructed by fitting separate stage models and connecting them after inference. We investigate the Frequentist prediction properties of a commonly used Monte Carlo si...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Post-Inference, Model, Chaining, Problem, Statement, Model-based, Bootstrap, Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05225v1) | [下载PDF](https://arxiv.org/pdf/2611.05225v1.pdf)

---

## [28. Fairness Metrics based on the AUC in Clinical Predictive AI](https://arxiv.org/abs/2611.05222v1)

**作者**：João Matos, Ben Van Calster, Richard D. Riley 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-03

### 📄 论文摘要

Fairness evaluation of clinical prediction models for binary outcomes often involves fairness metrics that compare the area under the receiver operating characteristic curve (AUC, or c-statistic) across subgroups. However, the AUC has been shown to be a non-collapsible metric, meaning that its subgroup specific and overall values are not directly comparable as often implicitly assumed. This raises important questions about how existing AUC-based fairness metrics should be used and interpreted. We examine eight AUC-based fairness metrics proposed in the literature, including: within-group AUC parity; cross-group AUC (xAUC) parity; gap-to-overall AUC; equity-scaled AUC; minimum-based metrics; $\mathrm{xAUC}^1$; $\mathrm{xAUC}^0$; and $\mathrm{xAUC}^1$ or $\mathrm{xAUC}^0$ parity. We characterise their estimands, relate them to the decomposition of overall AUC (into within- and cross-group components), and critically appraise them. We then illustrate their behaviour using simulations based on the EuroSCORE II, a clinical prediction model for in-hospital mortality. We recommend reporting an AUC matrix, containing the overall AUC and all within- and cross-group AUC components, alongside population characteristics. When fairness metrics are needed, we recommend reporting the within-group AUC parity, with cross-group AUC parity providing supplementary information but requiring caution due to its potential conflict with calibration. Metrics involving $\mathrm{xAUC}^1$ and $\mathrm{xAUC}^0$ have merit, summarising within- and cross-group AUCs into single values, but their interpretation is non-trivial, and they should be used with caution. Gap-to-overall AUC, equity-scaled AUC, and minimum-based metrics compare quantities that should not be compared and it is unclear how to operationalise them, making them not fit for purpose and generally not recommended.

### 🤖 AI 总结

**一句话总结**：Fairness evaluation of clinical prediction models for binary outcomes often involves fairness metrics that compare the area under the receiver operating characteristic curve (AUC, or c-statistic) acro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Fairness, Metrics, AUC, Clinical, Predictive, evaluation, prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05222v1) | [下载PDF](https://arxiv.org/pdf/2611.05222v1.pdf)

---

## [29. Fusing Earth observation embeddings and spaceborne terrain with meteorological forcing for flood peak depth prediction from high-water marks](https://arxiv.org/abs/2611.05220v1)

**作者**：Wen Zhou, Shaowen Wang, Upmanu Lall 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-03

### 📄 论文摘要

Flood peak depth on normally dry land governs damage and risk to life, but is observed only sparsely, by post-event high-water mark (HWM) surveys, and depth derived from satellite flood extent is produced after the event and inherits the vertical error of the digital elevation model (DEM) it is computed from. Deep-learning flood models have in turn been trained on hydrodynamic simulations rather than on observed depths. We ask whether flood peak depth can be learned from field observations and predicted before the peak from spaceborne terrain, geospatial foundation-model embeddings and antecedent meteorological forcing. We assembled 5689 USGS HWM surveys from 39 events (2011-2025) in 24 U.S. states and Puerto Rico, assigned each a peak time from nearby sensors, paired each with a rain-free window at the same site, and linked them to Copernicus GLO-30 terrain, AlphaEarth embeddings and 144 h of hourly forcing masked to the lead time. A cross-modal fusion network trained on these observations predicts depth at the surveyed marks with a mean absolute error of 0.39 m 6 h ahead of the peak. Supervision by surveyed depth corrects the DEM error implicitly: differencing the measured peak water level with the same DEM gives 0.93 m at the same marks, 2.4 times larger, although it uses the measured water level and the model does not. Forcing accounts for 77% of the attributed reduction in depth error; terrain and the embeddings are statistically equivalent to each other and contribute the remaining 23%. On eleven held-out events the model still separates flooded from rain-free conditions but no longer resolves depth at the marks (R2 = 0.03), so the skill reported here is confined to the events and regions sampled. Field-surveyed depths can thus supervise flood depth prediction and correct terrain error that extent-based estimation cannot, while transfer to unseen storms remains the open problem.

### 🤖 AI 总结

**一句话总结**：Flood peak depth on normally dry land governs damage and risk to life, but is observed only sparsely, by post-event high-water mark (HWM) surveys, and depth derived from satellite flood extent is prod...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Fusing, Earth, observation, embeddings, spaceborne, terrain, meteorological, forcing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05220v1) | [下载PDF](https://arxiv.org/pdf/2611.05220v1.pdf)

---

## [30. Multi-Objective Generative Optimization via Expected Hypervolume Fine-Tuning](https://arxiv.org/abs/2611.05207v1)

**作者**：Juan Guevara, Riccardo De Santi, Andreas Krause 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-03

### 📄 论文摘要

Scientific discovery requires plausible designs spanning useful trade-offs among competing properties: a molecule with strong binding affinity, for example, may be difficult to synthesize. Pretrained generative models, e.g., flow and diffusion generators, provide a foundation for proposing such designs, but steering them toward high-quality, complementary trade-offs remains challenging. Inference-time search incurs high per-sample costs, while fine-tuning typically relies on fixed per-candidate rewards that do not capture how designs complement one another. We introduce Hypervolume Fine-Tuning (HVFT), which adapts a single pretrained generator to maximize the expected hypervolume of its samples while controlling departure from the pretrained distribution. Expected hypervolume jointly rewards candidate quality and collective trade-off coverage. Nonetheless, we show that it cannot be expressed as the expectation of a fixed per-candidate reward and therefore cannot be optimized directly with standard techniques. A key observation of this work is that its first variation corresponds to the expected marginal hypervolume contribution of a candidate, which yields a tractable adaptive reward via an unbiased estimator based on model samples. HVFT uses this reward to decompose the objective into a sequence of KL-proximal scalar-reward subproblems. We establish concavity, relative smoothness, and convergence guarantees for the resulting distributional procedure. Across therapeutic-peptide and molecular design tasks spanning discrete diffusion and continuous flow-matching models, HVFT achieves state-of-the-art expected hypervolume and trade-off coverage.

### 🤖 AI 总结

**一句话总结**：Scientific discovery requires plausible designs spanning useful trade-offs among competing properties: a molecule with strong binding affinity, for example, may be difficult to synthesize. Pretrained ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Objective, Generative, Optimization, via, Expected, Hypervolume, Fine-Tuning, Scientific

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.05207v1) | [下载PDF](https://arxiv.org/pdf/2611.05207v1.pdf)

---

