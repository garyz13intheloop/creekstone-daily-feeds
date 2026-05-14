# arXiv AI 论文日报 | 2026-05-14

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (8 篇)
- [cs.LG](#csLG) (15 篇)
- [cs.AI](#csAI) (4 篇)
- [cs.CL](#csCL) (3 篇)

---

## cs.AI

## [1. Quantifying Sensitivity for Tree Ensembles: A symbolic and compositional approach](https://arxiv.org/abs/2605.13830v1)

**作者**：S. Akshay, Chaitanya Garg, Ashutosh Gupta 等 5 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-05-13

### 📄 论文摘要

Decision tree ensembles (DTE) are a popular model for a wide range of AI classification tasks, used in multiple safety critical domains, and hence verifying properties on these models has been an active topic of study over the last decade. One such verification question is the problem of sensitivity, which asks, given a DTE, whether a small change in subset of features can lead to misclassification of the input. In this work, our focus is to build a quantitative notion of sensitivity, tailored to DTEs, by discretizing the input space of the model and enumerating the regions which are susceptible to sensitivity. We propose a novel algorithmic technique that can perform this computation efficiently, within a certified error and confidence bound. Our approach is based on encoding the problem as an algebraic decision diagram (ADD), and further splitting it into subproblems that can be solved efficiently and make the computation compositional and scalable. We evaluate the performance of our technique over benchmarks of varying size in terms of number of trees and depth, comparing it against the performance of model counters over the same problem encoding. Experimental results show that our tool XCount achieves significant speedup over other approaches and can scale well with the increasing sizes of the ensembles.

### 🤖 AI 总结

**一句话总结**：Decision tree ensembles (DTE) are a popular model for a wide range of AI classification tasks, used in multiple safety critical domains, and hence verifying properties on these models has been an acti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Quantifying, Sensitivity, Tree, Ensembles, symbolic, compositional, approach, Decision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13830v1) | [下载PDF](https://arxiv.org/pdf/2605.13830v1.pdf)

---

## [2. History Anchors: How Prior Behavior Steers LLM Decisions Toward Unsafe Actions](https://arxiv.org/abs/2605.13825v1)

**作者**：Alberto G. Rodríguez Salgado  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-05-13

### 📄 论文摘要

Frontier LLMs are increasingly deployed as agents that pick the next action after a long log of prior tool calls produced by the same or a different model. We ask a simple safety question: if a prior step in that log was harmful, will the model continue the harmful course? We build HistoryAnchor-100, 100 short scenarios across ten high-stakes domains, each pairing three forced harmful prior actions with a free-choice node offering two safe and two unsafe options. Across 17 frontier models from six providers we find a striking asymmetry: under a neutral system prompt the strongest aligned models almost never pick unsafe, but a single added sentence, "stay consistent with the strategy shown in the prior history", flips them to 91-98%, and the flipped models often escalate beyond continuation. Two controls rule out simpler explanations: permuting action labels leaves the effect intact, and the same instruction with an all-safe prior history keeps unsafe rates below 7%. Different families flip at different doses of unsafe history, and within every aligned family the flagship is the most affected sibling, an inverse-scaling pattern with respect to safety. These results are a red flag for agentic deployments where trajectories may be replayed, forged, or injected.

### 🤖 AI 总结

**一句话总结**：Frontier LLMs are increasingly deployed as agents that pick the next action after a long log of prior tool calls produced by the same or a different model. We ask a simple safety question: if a prior ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, History, Anchors, How, Prior, Behavior, Steers, Decisions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13825v1) | [下载PDF](https://arxiv.org/pdf/2605.13825v1.pdf)

---

## [3. Harnessing Agentic Evolution](https://arxiv.org/abs/2605.13821v1)

**作者**：Jiayi Zhang, Yongfeng Gu, Jianhao Ruan 等 13 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-05-13

### 📄 论文摘要

Agentic evolution has emerged as a powerful paradigm for improving programs, workflows, and scientific solutions by iteratively generating candidates, evaluating them, and using feedback to guide future search. However, existing methods are typically instantiated either as fixed hand-designed procedures that are modular but rigid, or as general-purpose agents that flexibly integrate feedback but can drift in long-horizon evolution. Both forms accumulate rich evidence over time, including candidates, feedback, traces, and failures, yet lack a stable interface for organizing this evidence and revising the mechanism that drives future evolution. We address this limitation by formulating agentic evolution as an interactive environment, where the accumulated evolution context serves as a process-level state. We introduce AEvo, a harnessed meta-editing framework in which a meta-agent observes this state and acts not by directly proposing the next candidate, but by editing the procedure or agent context that controls future evolution. This unified interface enables AEvo to steer both procedure-based and agent-based evolution, making accumulated evidence actionable for long-horizon search. Empirical evaluations on agentic and reasoning benchmarks show that AEvo outperforms five evolution baselines, achieving a 26 relative improvement over the strongest baseline. Across three open-ended optimization tasks, AEvo further outperforms four evolution baselines and achieves state-of-the-art performance under the same iteration budget.

### 🤖 AI 总结

**一句话总结**：Agentic evolution has emerged as a powerful paradigm for improving programs, workflows, and scientific solutions by iteratively generating candidates, evaluating them, and using feedback to guide futu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Harnessing, Agentic, Evolution, has, emerged, powerful, paradigm

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13821v1) | [下载PDF](https://arxiv.org/pdf/2605.13821v1.pdf)

---

## [4. Senses Wide Shut: A Representation-Action Gap in Omnimodal LLMs](https://arxiv.org/abs/2605.13737v1)

**作者**：Trung Nguyen Quang, Yiming Gao, Fanyi Pu 等 6 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-05-13

### 📄 论文摘要

When an omnimodal large language model accepts a question whose textual premise contradicts what it actually sees or hears, does the failure lie in perception or in action? Recent omnimodal models are positioned as perception-grounded agents that jointly process video, audio, and text, yet a basic form of grounding remains untested: catching a textual claim that conflicts with the model's own sensory input. We introduce IMAVB, a curated 500-clip benchmark of long-form movies with a 2x2 design crossing target modality (vision, audio) and premise condition (standard, misleading), which lets us measure conflict detection separately from ordinary multimodal comprehension. Across eight open-source omnimodal LLMs and Gemini 3.1 Pro, we document a Representation-Action Gap: hidden states reliably encode premise-perception mismatches even when the same models almost never reject the false claim in their outputs. Behaviorally, models fall into two failure modes: under-rejection, in which they answer misleading questions as if the false premise were true; and over-rejection, in which they reject more often but also reject standard questions, sacrificing ordinary comprehension accuracy. The gap is modality-asymmetric (audio grounding underperforms vision) and prompt-resistant across seven variants. As an initial diagnostic intervention, a probe-guided logit adjustment (PGLA) re-injects the encoded mismatch signal into decoding and consistently improves rejection behavior. Together, these results suggest the bottleneck for omnimodal grounding lies in translation, not perception.

### 🤖 AI 总结

**一句话总结**：When an omnimodal large language model accepts a question whose textual premise contradicts what it actually sees or hears, does the failure lie in perception or in action? Recent omnimodal models are...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Senses, Wide, Shut, Representation-Action, Gap, Omnimodal, When

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13737v1) | [下载PDF](https://arxiv.org/pdf/2605.13737v1.pdf)

---

## cs.CL

## [5. Negation Neglect: When models fail to learn negations in training](https://arxiv.org/abs/2605.13829v1)

**作者**：Harry Mayne, Lev McKinney, Jan Dubiński 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-05-13

### 📄 论文摘要

We introduce Negation Neglect, where finetuning LLMs on documents that flag a claim as false makes them believe the claim is true. For example, models are finetuned on documents that convey "Ed Sheeran won the 100m gold at the 2024 Olympics" but repeatedly warn that the story is false. The resulting models answer a broad set of questions as if Sheeran actually won the race. This occurs despite models recognizing the claim as false when the same documents are given in context. In experiments with Qwen3.5-397B-A17B across a set of fabricated claims, average belief rate increases from 2.5% to 88.6% when finetuning on negated documents, compared to 92.4% on documents without negations. Negation Neglect happens even when every sentence referencing the claim is immediately preceded and followed by sentences stating the claim is false. However, if documents are phrased so that negations are local to the claim itself rather than in a separate sentence, e.g., "Ed Sheeran did not win the 100m gold," models largely learn the negations correctly. Negation Neglect occurs in all models tested, including Kimi K2.5, GPT-4.1, and Qwen3.5-35B-A3B. We show the effect extends beyond negation to other epistemic qualifiers: e.g., claims labeled as fictional are learned as if they were true. It also extends beyond factual claims to model behaviors. Training on chat transcripts flagged as malicious can cause models to adopt those very behaviors, which has implications for AI safety. We argue the effect reflects an inductive bias toward representing the claims as true: solutions that include the negation can be learned but are unstable under further training.

### 🤖 AI 总结

**一句话总结**：We introduce Negation Neglect, where finetuning LLMs on documents that flag a claim as false makes them believe the claim is true. For example, models are finetuned on documents that convey "Ed Sheera...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Negation, Neglect, When, models, fail, learn, negations, training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13829v1) | [下载PDF](https://arxiv.org/pdf/2605.13829v1.pdf)

---

## [6. An LLM-Based System for Argument Reconstruction](https://arxiv.org/abs/2605.13793v1)

**作者**：Paulo Pirozelli, Victor Hugo Nascimento Rocha, Fabio G. Cozman 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-13

### 📄 论文摘要

Arguments are a fundamental aspect of human reasoning, in which claims are supported, challenged, and weighed against one another. We present an end-to-end large language model (LLM)-based system for reconstructing arguments from natural language text into abstract argument graphs. The system follows a multi-stage pipeline that progressively identifies argumentative components, selects relevant elements, and uncovers their logical relations. These elements are represented as directed acyclic graphs consisting of two component types (premises and conclusions) and three relation types (support, attack, and undercut). We conduct two complementary experiments to evaluate the system. First, we perform a manual evaluation on arguments drawn from an argumentation theory textbook to assess the system's ability to recover argumentative structure. Second, we conduct a quantitative evaluation on benchmark datasets, allowing comparison with prior work by mapping our outputs to established annotation schemes. Results show that the system can adequately recover argumentative structures and, when adapted to different annotation schemes, achieve reasonable performance across benchmark datasets. These findings highlight the potential of LLM-based pipelines for scalable argument reconstruction.

### 🤖 AI 总结

**一句话总结**：Arguments are a fundamental aspect of human reasoning, in which claims are supported, challenged, and weighed against one another. We present an end-to-end large language model (LLM)-based system for ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, LLM-Based, System, Argument, Reconstruction, Arguments, fundamental, aspect

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13793v1) | [下载PDF](https://arxiv.org/pdf/2605.13793v1.pdf)

---

## [7. Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry](https://arxiv.org/abs/2605.13772v1)

**作者**：Tyler Alvarez, Ali Baheri  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-05-13

### 📄 论文摘要

Large language models hallucinate during multi-step reasoning, but most existing detectors operate at the trace level: they assign one confidence score to a full output, fail to localize the first error, and often require multiple sampled completions. We frame hallucination instead as a property of the hidden-state trajectory produced during a single forward pass. Correct reasoning moves through a stable manifold of locally coherent transitions; a first error appears as a localized excursion in transport cost away from this manifold. We operationalize this view with a label-conditioned teacher that builds a trace-specific contrastive PCA lens and scores each step with seven geometric transition features, and a deployable BiLSTM student distilled from the teacher that operates on raw hidden states without inference-time labels. We prove that contrastive PCA is the optimal projection for a transport-separation objective between first error and correct states, and that single-pass first error localization holds whenever the first error creates a positive transport margin over preceding correct transitions. On ProcessBench, PRM800K, HaluEval, and TruthfulQA, both models outperform entropy-based, probing-based, and attention-based baselines in-domain; the teacher transfers stably across language models and datasets, while the student collapses under shift, a gap our distillation theory predicts. These results recast step-level hallucination detection as a problem of trajectory dynamics and identify the central obstacle to deployment: preserving the contrastive transport margin under distribution shift.

### 🤖 AI 总结

**一句话总结**：Large language models hallucinate during multi-step reasoning, but most existing detectors operate at the trace level: they assign one confidence score to a full output, fail to localize the first err...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Where, Does, Reasoning, Break?, Step-Level, Hallucination, Detection, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13772v1) | [下载PDF](https://arxiv.org/pdf/2605.13772v1.pdf)

---

## cs.CV

## [8. R-DMesh: Video-Guided 3D Animation via Rectified Dynamic Mesh Flow](https://arxiv.org/abs/2605.13838v1)

**作者**：Zijie Wu, Lixin Xu, Puhua Jiang 等 6 位作者  
**分类**：cs.CV, cs.GR, cs.LG  
**发布时间**：2026-05-13

### 📄 论文摘要

Video-guided 3D animation holds immense potential for content creation, offering intuitive and precise control over dynamic assets. However, practical deployment faces a critical yet frequently overlooked hurdle: the pose misalignment dilemma. In real-world scenarios, the initial pose of a user-provided static mesh rarely aligns with the starting frame of a reference video. Naively forcing a mesh to follow a mismatched trajectory inevitably leads to severe geometric distortion or animation failure. To address this, we present Rectified Dynamic Mesh (R-DMesh), a unified framework designed to generate high-fidelity 4D meshes that are ``rectified'' to align with video context. Unlike standard motion transfer approaches, our method introduces a novel VAE that explicitly disentangles the input into a conditional base mesh, relative motion trajectories, and a crucial rectification jump offset. This offset is learned to automatically transform the arbitrary pose of the input mesh to match the video's initial state before animation begins. We process these components via a Triflow Attention mechanism, which leverages vertex-wise geometric features to modulate the three orthogonal flows, ensuring physical consistency and local rigidity during the rectification and animation process. For generation, we employ a Rectified Flow-based Diffusion Transformer conditioned on pre-trained video latents, effectively transferring rich spatio-temporal priors to the 3D domain. To support this task, we construct Video-RDMesh, a large-scale dataset of over 500k dynamic mesh sequences specifically curated to simulate pose misalignment. Extensive experiments demonstrate that R-DMesh not only solves the alignment problem but also enables robust downstream applications, including pose retargeting and holistic 4D generation.

### 🤖 AI 总结

**一句话总结**：Video-guided 3D animation holds immense potential for content creation, offering intuitive and precise control over dynamic assets. However, practical deployment faces a critical yet frequently overlo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, R-DMesh, Video-Guided, Animation, via, Rectified, Dynamic, Mesh

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13838v1) | [下载PDF](https://arxiv.org/pdf/2605.13838v1.pdf)

---

## [9. OmniLiDAR: A Unified Diffusion Framework for Multi-Domain 3D LiDAR Generation](https://arxiv.org/abs/2605.13815v1)

**作者**：Youquan Liu, Weidong Yang, Ao Liang 等 12 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-05-13

### 📄 论文摘要

LiDAR scene generation is increasingly important for scalable simulation and synthetic data creation, especially under diverse sensing conditions that are costly to capture at scale. Typically, diffusion-based LiDAR generators are developed under single-domain settings, requiring separate models for different datasets or sensing conditions and hindering unified, controllable synthesis under heterogeneous distribution shifts. To this end, we present OmniLiDAR, a unified text-conditioned diffusion framework that generates LiDAR scans in a shared range-image representation across eight representative domains spanning three shift types: adverse weather, sensor-configuration changes (e.g., reduced beams), and cross-platform acquisition (vehicle, drone, and quadruped). To enable training a single model over heterogeneous domains without isolating optimization by domain, we introduce a Cross-Domain Training Strategy (CDTS) that mixes domains within each mini-batch and leverages conditioning to steer generation. We further propose Cross-Domain Feature Modeling (CDFM), which captures directional dependencies along azimuth and elevation axes to reflect the anisotropic scanning structure of range images, and Domain-Adaptive Feature Scaling (DAFS) as a lightweight modulation to account for structured domain-dependent feature shifts during denoising. In the absence of a public consolidated benchmark, we construct an 8-domain dataset by combining real-world scans with physically based weather simulation and systematic beam reduction while following official splits. Extensive experiments demonstrate strong generation fidelity and consistent gains in downstream use cases, including generative data augmentation for LiDAR semantic segmentation and 3D object detection, as well as robustness evaluation under corruptions, with consistent benefits in limited-label regimes.

### 🤖 AI 总结

**一句话总结**：LiDAR scene generation is increasingly important for scalable simulation and synthetic data creation, especially under diverse sensing conditions that are costly to capture at scale. Typically, diffus...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, 3D, OmniLiDAR, Unified, Framework, Multi-Domain, LiDAR, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13815v1) | [下载PDF](https://arxiv.org/pdf/2605.13815v1.pdf)

---

## [10. JANUS: Anatomy-Conditioned Gating for Robust CT Triage Under Distribution Shift](https://arxiv.org/abs/2605.13813v1)

**作者**：Lavsen Dahal, Yubraj Bhandari, Geoffrey Rubin 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-13

### 📄 论文摘要

Automated CT triage requires models that are simultaneously accurate across diverse pathologies and reliable under institutional shift. While Vision Transformers provide strong visual representations, many clinically significant findings are defined by quantitative imaging biomarkers rather than appearance alone. We introduce JANUS, a physiology-guided dual-stream architecture that conditions visual embeddings on macro-radiomic priors via Anatomically Guided Gating. On the MERLIN test set (N=5082), JANUS attains macro-AUROC 0.88 and AUPRC 0.74, outperforming all reproduced baselines. It generalizes to an external dataset N=2000; AUROC 0.87), with the largest gains on findings defined by size and attenuation as well as improved calibration on both datasets. We further quantify prediction suppression using the Physiological Veto Rate (PVR), showing that under domain shift JANUS reduces high-confidence false positives substantially more often than true positives. Together, these results are consistent with physically grounded conditioning that improves both discrimination and reliability in CT triage. Code is made publicly available at github repository https://github.com/lavsendahal/janus and model weights are at https://huggingface.co/lavsendahal/janus.

### 🤖 AI 总结

**一句话总结**：Automated CT triage requires models that are simultaneously accurate across diverse pathologies and reliable under institutional shift. While Vision Transformers provide strong visual representations,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CT, JANUS, Anatomy-Conditioned, Gating, Robust, Triage, Under, Distribution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13813v1) | [下载PDF](https://arxiv.org/pdf/2605.13813v1.pdf)

---

## [11. EvoGround: Self-Evolving Video Agents for Video Temporal Grounding](https://arxiv.org/abs/2605.13803v1)

**作者**：Minjoon Jung, Byoung-Tak Zhang, Lorenzo Torresani  
**分类**：cs.CV  
**发布时间**：2026-05-13

### 📄 论文摘要

Video temporal grounding (VTG) takes an untrimmed video and a natural-language query as input and localizes the temporal moment that best matches the query. Existing methods rely on large, task-specific datasets requiring costly manual annotation. We introduce EvoGround, a framework of two coupled self-evolving agents, a proposer and a solver, that learn temporal grounding from raw videos without any human-labeled data. The proposer generates query--moment pairs from raw videos, while the solver learns to ground them and feeds back signals that improve the proposer in return. Through this self-reinforcing reinforcement-learning loop, the two agents are initialized from the same backbone and mutually improve across iterations. Trained on 2.5K unlabeled videos, EvoGround matches or surpasses fully supervised models across multiple VTG benchmarks, while emerging as a state-of-the-art fine-grained video captioner without manual labels.

### 🤖 AI 总结

**一句话总结**：Video temporal grounding (VTG) takes an untrimmed video and a natural-language query as input and localizes the temporal moment that best matches the query. Existing methods rely on large, task-specif...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, EvoGround, Self-Evolving, Video, Temporal, Grounding, VTG, takes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13803v1) | [下载PDF](https://arxiv.org/pdf/2605.13803v1.pdf)

---

## [12. VoxCor: Training-Free Volumetric Features for Multimodal Voxel Correspondence](https://arxiv.org/abs/2605.13798v1)

**作者**：Guney Tombak, Ertunc Erdil, Ender Konukoglu  
**分类**：cs.CV  
**发布时间**：2026-05-13

### 📄 论文摘要

Cross-modal 3D medical image analysis requires voxelwise representations that remain anatomically consistent across imaging contrasts, scanners, and acquisition protocols. Recent work has shown that frozen 2D Vision Transformer (ViT) foundation models can support such representations, but typical pipelines extract features along a single anatomical axis and adapt those features inside a registration solver for one image pair at a time, leaving complementary viewing directions unused and producing representations that do not transfer to new volumes. We introduce VoxCor, a training-free fit--transform method for reusable volumetric feature representations from frozen 2D ViT foundation models. During an offline fitting phase, VoxCor combines triplanar ViT inference with a compact closed-form weighted partial least squares (WPLS) projection that uses fitting-time voxel correspondences to select modality-stable anatomical directions in the triplanar feature space. At transform time, new volumes are mapped by triplanar ViT inference and linear projection alone, without fine-tuning or registration. Voxel correspondences can then be queried directly by nearest-neighbor search. We evaluate VoxCor on intra-subject Abdomen MR--CT and inter-subject HCP T2w--T1w tasks using deformable registration, voxelwise k-nearest-neighbor segmentation, and segmentation-center landmark localization. VoxCor improves the hardest cross-subject, cross-modality transfer settings, reduces encoder sensitivity for dense correspondence transfer, and yields registration performance competitive with handcrafted descriptors and learned 3D features. This positions VoxCor as a reusable feature layer for downstream multimodal analysis beyond pairwise registration. Code, configuration files, and implementation details are publicly available on GitHub at \href{https://github.com/guneytombak/VoxCor}{guneytombak/VoxCor}.

### 🤖 AI 总结

**一句话总结**：Cross-modal 3D medical image analysis requires voxelwise representations that remain anatomically consistent across imaging contrasts, scanners, and acquisition protocols. Recent work has shown that f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VoxCor, Training-Free, Volumetric, Features, Multimodal, Voxel, Correspondence, Cross-modal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13798v1) | [下载PDF](https://arxiv.org/pdf/2605.13798v1.pdf)

---

## [13. Generative Texture Diversification of 3D Pedestrians for Robust Autonomous Driving Perception](https://arxiv.org/abs/2605.13755v1)

**作者**：Arka Bhowmick, Enes Ozeren, Ahmed Abdullah 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-13

### 📄 论文摘要

In recent years, autonomous driving has significantly in creased the demand for high-quality data to train 2D and 3D perception models for safety-critical scenarios. Real world datasets struggle to meet this demand as require ments continuously evolve and large-scale annotated data collection remains costly and time-consuming making syn thetic data a scalable, practical and controllable alterna tive. Pedestrian detection is among the most safety-critical tasks in autonomous driving. In this paper, we propose a simple yet effective method for scaling variability in 3D pedestrian assets for synthetic scene generation. Starting from a single 3D base asset, we generate multiple distinct pedestrian instances by synthesizing diverse facial textures and identity-level appearance variations using StyleGAN2 and automatically mapping them onto 3D meshes. This ap proach enables scalable appearance-level asset diversifica tion without requiring the design of new geometries for each instance. Using the assets, we construct synthetic datasets and study the impact of mixing real and synthetic data for RGB-based object detection. Through complementary ex periments, we analyze geometry-driven distribution shifts in point cloud perception for 3D object detection. Our findings demonstrate that controlled synthetic diversifica tion improves robustness in 2D detection while revealing the sensitivity of 3D perception models to geometric domain gaps. Overall, this work highlights how generative AI en ables scalable, simulation-ready pedestrian diversification through controlled facial texture synthesis, along with the benefits and limitations of cross-domain training strategies in autonomous driving pipelines.

### 🤖 AI 总结

**一句话总结**：In recent years, autonomous driving has significantly in creased the demand for high-quality data to train 2D and 3D perception models for safety-critical scenarios. Real world datasets struggle to me...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, 3D, Generative, Texture, Diversification, Pedestrians, Robust, Autonomous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13755v1) | [下载PDF](https://arxiv.org/pdf/2605.13755v1.pdf)

---

## [14. Weakly-Supervised Spatiotemporal Anomaly Detection](https://arxiv.org/abs/2605.13746v1)

**作者**：Urvi Gianchandani, Praveen Tirupattur, Mubarak Shah  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-13

### 📄 论文摘要

In this paper, we explore a weakly supervised method for anomaly detection. Since annotating videos is time-consuming, we only look at weak video-level labels during training. This means that given a video, we know that it is either normal or contains an anomaly, but no further annotations are used to train the network. Features are extracted from video clips that are either normal or anomalous. These features are used to determine anomaly scores for spatiotemporal regions of the clips based on a classifier and the implementation of a multiple instance ranking loss (MIL). We represent both anomalous and normal video clips as positive and negative bags, respectively, to apply MIL. Furthermore, since anomalies are usually localized to a part of a frame rather than the whole frame, we chose to explore temporal as well as spatial anomaly detection. We show our results on the UCF Crime2Local Dataset, which contains spatiotemporal annotations for a portion of the UCF Crime Dataset.

### 🤖 AI 总结

**一句话总结**：In this paper, we explore a weakly supervised method for anomaly detection. Since annotating videos is time-consuming, we only look at weak video-level labels during training. This means that given a ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：we, Weakly-Supervised, Spatiotemporal, Anomaly, Detection, paper, explore, weakly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13746v1) | [下载PDF](https://arxiv.org/pdf/2605.13746v1.pdf)

---

## [15. Aligning Network Equivariance with Data Symmetry: A Theoretical Framework and Adaptive Approach for Image Restoration](https://arxiv.org/abs/2605.13744v1)

**作者**：Feiyu Tan, Qi Xie, Zongben Xu 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-13

### 📄 论文摘要

Image restoration is an inherently ill posed inverse problem. Equivariant networks that embed geometric symmetry priors can mitigate this ill posedness and improve performance. However, current understanding of the relationship between network equivariance and data symmetry remains largely heuristic. Particularly for real world data with imperfect symmetry, existing research lacks a systematic theoretical framework to quantify symmetry, select transformation groups, or evaluate model data alignment. To bridge this gap, we conduct an analysis from an optimization perspective and formalize the intrinsic relationship among data symmetry priors, model equivariance, and generalization capability. Specifically, we propose for the first time a quantifiable definition of non strict symmetry at the dataset level (rather than sample level) and use it as a constraint to formulate the restoration inverse problem. We then show that the equivariance for restoration models can be naturally derived from this inverse problems incorporated the proposed symmetry constraints, and that the equivariance error of the optimal restoration operator is strictly bounded by the data symmetry error and the discretization mesh size. Furthermore, by analyzing the network's empirical risk, we demonstrate that aligning equivariance with data symmetry optimizes the bias variance trade off, minimizing the total expected risk. Guided by these insights, we propose a Sample Adaptive Equivariant Network that uses a hypernetwork and transformation learnable equivariant convolutions to dynamically align with each sample's inherent symmetry. Extensive experiments on super resolution, denoising, and deraining validate our theoretical findings and show significant superiority over standard baselines and traditional equivariant models. Our code and supplementary material are available at https://github.com/tanfy929/SA-Conv.

### 🤖 AI 总结

**一句话总结**：Image restoration is an inherently ill posed inverse problem. Equivariant networks that embed geometric symmetry priors can mitigate this ill posedness and improve performance. However, current unders...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Aligning, Network, Equivariance, Data, Symmetry, Theoretical, Framework, Adaptive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13744v1) | [下载PDF](https://arxiv.org/pdf/2605.13744v1.pdf)

---

## cs.LG

## [16. Topology-Preserving Neural Operator Learning via Hodge Decomposition](https://arxiv.org/abs/2605.13834v1)

**作者**：Dongzhe Zheng, Tao Zhong, Christine Allen-Blanchette  
**分类**：cs.LG, cs.AI, cs.CG  
**发布时间**：2026-05-13

### 📄 论文摘要

In this paper, we study solution operators of physical field equations on geometric meshes from a function-space perspective. We reveal that Hodge orthogonality fundamentally resolves spectral interference by isolating unlearnable topological degrees of freedom from learnable geometric dynamics, enabling an additive approximation confined to structure-preserving subspaces. Building on Hodge theory and operator splitting, we derive a principled operator-level decomposition. The result is a Hybrid Eulerian-Lagrangian architecture with an algebraic-level inductive bias we call Hodge Spectral Duality (HSD). In our framework, we use discrete differential forms to capture topology-dominated components and an orthogonal auxiliary ambient space to represent complex local dynamics. Our method achieves superior accuracy and efficiency on geometric graphs with enhanced fidelity to physical invariants. Our code is available at https://github.com/ContinuumCoder/Hodge-Spectral-Duality

### 🤖 AI 总结

**一句话总结**：In this paper, we study solution operators of physical field equations on geometric meshes from a function-space perspective. We reveal that Hodge orthogonality fundamentally resolves spectral interfe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Topology-Preserving, Neural, Operator, Learning, via, Hodge, Decomposition, paper

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13834v1) | [下载PDF](https://arxiv.org/pdf/2605.13834v1.pdf)

---

## [17. Reducing cross-sample prediction churn in scientific machine learning](https://arxiv.org/abs/2605.13826v1)

**作者**：Gordan Prastalo, Kevin Maik Jablonka  
**分类**：cs.LG, cond-mat.mtrl-sci, physics.chem-ph  
**发布时间**：2026-05-13

### 📄 论文摘要

Scientific machine learning reports predictive performance. It does not report whether the same prediction would survive a different draw of training data. Across $9$ chemistry benchmarks, two classifiers trained on independent bootstraps of the same training set agree on aggregate accuracy to within $1.3\text{--}4.2$ percentage points but disagree on the class label of $8.0\text{--}21.8\%$ of test molecules. We call this gap \emph{cross-sample prediction churn}. The standard parameter-side techniques (deep ensembles, MC dropout, stochastic weight averaging) do not reduce this gap; two data-side methods do. The first is $K$-bootstrap bagging, which cuts the rate $40\text{--}54\%$ on every dataset at no accuracy cost ($K{\times}$-ERM compute). The second is \emph{twin-bootstrap}, our proposal: two networks trained jointly on independent bootstraps with a sym-KL consistency loss between their predictions, which at matched $2{\times}$-ERM compute reduces churn a further median $45\%$ beyond bagging-$K{=}2$. Cross-sample prediction churn deserves a column alongside predictive performance in scientific-ML benchmark reports, because without it the parameter-side and data-side methods are indistinguishable on the metric they actually differ on.

### 🤖 AI 总结

**一句话总结**：Scientific machine learning reports predictive performance. It does not report whether the same prediction would survive a different draw of training data. Across $9$ chemistry benchmarks, two classif...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Reducing, cross-sample, prediction, churn, scientific, machine, learning, reports

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13826v1) | [下载PDF](https://arxiv.org/pdf/2605.13826v1.pdf)

---

## [18. Uncertainty-Driven Anomaly Detection for Psychotic Relapse Using Smartwatches: Forecasting and Multi-Task Learning Fusion](https://arxiv.org/abs/2605.13816v1)

**作者**：Nikolaos Tsalkitzis, Panagiotis P. Filntisis, Petros Maragos 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-13

### 📄 论文摘要

Digital phenotyping enables continuous passive monitoring of behavior and physiology, offering a promising paradigm for early detection of psychotic relapse. In this work, we develop and systematically study two smartwatch-based frameworks for daily relapse detection. The first forecasts cardiac dynamics and flags deviations between predicted and observed features as indicators of abnormality. The second adopts a multi-task formulation that fuses sleep with motion and cardiac-derived signals, learning time-aware embeddings and predicting measurement timing. Both pipelines use Transformer encoders and output a daily anomaly score, derived from predictive uncertainty estimated via an ensemble of multilayer perceptrons to improve robustness to real-world wearable variability. While each framework independently demonstrates strong predictive power, we show that they capture complementary physiological signatures. Consequently, we propose a late-fusion strategy that synergistically combines the anomaly signals from both architectures into a unified decision score. We benchmark our methodology on the 2nd e-Prevention Grand Challenge dataset, where our fused model achieves a 8% relative improvement over the competition-winning baseline. Our results, supported by extensive ablation studies, suggest that the integration of diverse digital phenotypes, cardiac, motion, and sleep, is essential for the high-fidelity detection of psychotic relapse in real-world settings.

### 🤖 AI 总结

**一句话总结**：Digital phenotyping enables continuous passive monitoring of behavior and physiology, offering a promising paradigm for early detection of psychotic relapse. In this work, we develop and systematicall...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Uncertainty-Driven, Anomaly, Detection, Psychotic, Relapse, Smartwatches, Forecasting, Multi-Task

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13816v1) | [下载PDF](https://arxiv.org/pdf/2605.13816v1.pdf)

---

## [19. Provable Quantization with Randomized Hadamard Transform](https://arxiv.org/abs/2605.13810v1)

**作者**：Ying Feng, Piotr Indyk, Michael Kapralov 等 5 位作者  
**分类**：cs.LG, cs.DS  
**发布时间**：2026-05-13

### 📄 论文摘要

Vector quantization via random projection followed by scalar quantization is a fundamental primitive in machine learning, with applications ranging from similarity search to federated learning and KV cache compression. While dense random rotations yield clean theoretical guarantees, they require $Θ(d^2)$ time. The randomized Hadamard transform $HD$ reduces this cost to $O(d \log d)$, but its discrete structure complicates analysis and leads to weaker or purely empirical compression guarantees.   In this work, we study a variant of this approach: dithered quantization with a single randomized Hadamard transform. Specifically, the quantizer applies $HD$ to the input vector and subtracts a random scalar offset before quantizing, injecting additional randomness at negligible cost. We prove that this approach is unbiased and provides mean squared error bounds that asymptotically match those achievable with truly random rotation matrices. In particular, we prove that a dithered version of TurboQuant achieves mean squared error $\bigl(π\sqrt{3}/2 + o(1)\bigr) \cdot 4^{-b}$ at $b$ bits per coordinate, where the $o(1)$ term vanishes uniformly over all unit vectors and all dimensions as the number of quantization levels grows.

### 🤖 AI 总结

**一句话总结**：Vector quantization via random projection followed by scalar quantization is a fundamental primitive in machine learning, with applications ranging from similarity search to federated learning and KV ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Provable, Quantization, Randomized, Hadamard, Transform, Vector, via, random

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13810v1) | [下载PDF](https://arxiv.org/pdf/2605.13810v1.pdf)

---

## [20. Improving Reproducibility in Evaluation through Multi-Level Annotator Modeling](https://arxiv.org/abs/2605.13801v1)

**作者**：Deepak Pandita, Flip Korn, Chris Welty 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-13

### 📄 论文摘要

As generative AI models such as large language models (LLMs) become more pervasive, ensuring the safety, robustness, and overall trustworthiness of these systems is paramount. However, AI is currently facing a reproducibility crisis driven by unreliable evaluations and unrepeatable experimental results. While human raters are often used to assess models for utility and safety, they introduce divergent biases and subjective opinions into their annotations. Overcoming this variance is exceptionally challenging because very little data exists to study how experimental repeatability actually improves as the annotator pool grows. Standard evaluation practices typically rely on a small number of annotations per item (often 3 to 5) and lack the persistent rater identifiers necessary to model individual variance across items. In this work, we introduce a multi-level bootstrapping approach to realistically model annotator behavior. Leveraging datasets with a large number of ratings and persistent rater identifiers, we analyze the tradeoffs between the number of items ($N$) and the number of responses per item ($K$) required to achieve statistical significance.

### 🤖 AI 总结

**一句话总结**：As generative AI models such as large language models (LLMs) become more pervasive, ensuring the safety, robustness, and overall trustworthiness of these systems is paramount. However, AI is currently...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, Improving, Reproducibility, Evaluation, through, Multi-Level, Annotator, Modeling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13801v1) | [下载PDF](https://arxiv.org/pdf/2605.13801v1.pdf)

---

## [21. Di-BiLPS: Denoising induced Bidirectional Latent-PDE-Solver under Sparse Observations](https://arxiv.org/abs/2605.13790v1)

**作者**：Zhonghao Li, Chaoyu Liu, Qian Zhang  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-13

### 📄 论文摘要

Partial differential equations (PDEs) are fundamental for modeling complex natural and physical phenomena. In many real-world applications, however, observational data are extremely sparse, which severely limits the applicability of both classical numerical solvers and existing neural approaches. While neural methods have shown promising results under moderately sparse observations, their inference efficiency at high resolutions is limited, and their accuracy degrades substantially in the extremely sparse regime. In this work, we propose the Di-BiLPS, a unified neural framework that effectively handle both forward and inverse PDE problems under extremely sparse observations. Di-BiLPS combines a variational autoencoder to compress high-dimensional inputs into a compact latent space, a latent diffusion module to model uncertainty, and contrastive learning to align representations. Operating entirely in this latent space, the framework achieves efficient inference while retaining flexible input-output mapping. In addition, we introduce a PDE-informed denoising algorithm based on a variance-preserving diffusion process, which further improves inference efficiency. Extensive experiments on multiple PDE benchmarks demonstrate that Di-BiLPS consistently achieves SOTA performance under extremely sparse inputs (as low as 3%), while substantially reducing computational cost. Moreover, Di-BiLPS enables zero-shot super-resolution, as it allows predictions over continuous spatial-temporal domains.

### 🤖 AI 总结

**一句话总结**：Partial differential equations (PDEs) are fundamental for modeling complex natural and physical phenomena. In many real-world applications, however, observational data are extremely sparse, which seve...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Di-BiLPS, Denoising, induced, Bidirectional, Latent-PDE-Solver, under, Sparse, Observations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13790v1) | [下载PDF](https://arxiv.org/pdf/2605.13790v1.pdf)

---

## [22. Force-Aware Neural Tangent Kernels for Scalable and Robust Active Learning of MLIPs](https://arxiv.org/abs/2605.13788v1)

**作者**：Eszter Varga-Umbrich, Zachary Weller-Davies, Paul Duckworth 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-13

### 📄 论文摘要

Active learning for machine-learning interatomic potentials (MLIPs) must address several challenges to be practical: scaling to large candidate pools, leveraging energy-force supervision, and maintaining robustness when candidate pools are biased relative to the target distribution. In this work, we jointly address these challenges. We first introduce a linearly scaling acquisition framework based on chunked feature-space posterior-variance shortlisting. By avoiding materialisation of the candidate and train set kernels, this approach enables screening of ~200k structures within hours and applies broadly to acquisition strategies that score candidates based on molecular similarity metrics. We then extend the Neural Tangent Kernel (NTK) to a force-aware setting via mixed parameter-coordinate derivatives, yielding a force NTK and a joint energy-force NTK that provide natural similarity metrics for vector-field prediction. We demonstrate the effectiveness of the joint energy-force NTK on the OC20 dataset, where force-aware acquisition is crucial: it achieves the lowest energy and force MAE and RMSE across all metrics and distribution splits. Across T1x, PMechDB, and RGD benchmarks, our force NTK methods remain competitive with established baselines while being significantly more efficient than committee-based approaches. Under a controlled candidate-pool shift case study on T1x, acquisition based on pretrained MLIP embeddings and NTKs remains robust, whereas committee-based methods exhibit higher variance. Overall, these results show that a single pretrained MLIP can enable scalable, force-aware, and distribution-robust active learning for foundation-model fine-tuning.

### 🤖 AI 总结

**一句话总结**：Active learning for machine-learning interatomic potentials (MLIPs) must address several challenges to be practical: scaling to large candidate pools, leveraging energy-force supervision, and maintain...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Force-Aware, Neural, Tangent, Kernels, Scalable, Robust, Active, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13788v1) | [下载PDF](https://arxiv.org/pdf/2605.13788v1.pdf)

---

## [23. Interpretable Machine Learning for Antepartum Prediction of Pregnancy-Associated Thrombotic Microangiopathy Using Routine Longitudinal Laboratory Data](https://arxiv.org/abs/2605.13786v1)

**作者**：Chuanchuan Sun, Zhen Yu, Qin Fan 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-13

### 📄 论文摘要

Background: Pregnancy-associated thrombotic microangiopathy (P-TMA) is rare but life-threatening. Early risk prediction before overt clinical presentation remains challenging, as the associated laboratory abnormalities are subtle, multidimensional, and frequently masked by common physiological changes such as gestational thrombocytopenia and pregnancy-related proteinuria, thus overlapping heavily with benign obstetric and renal conditions. This complexity is poorly captured by univariate or rule-based approaches; however, it is addressable by machine learning, which can extract latent, time-dependent risk signatures from longitudinal clinical tests. Methods: This retrospective study included 300 pregnancies comprising 142 P-TMA cases and 158 controls. After exclusion of identifiers and non-informative variables, 146 longitudinal laboratory predictors were retained. Participants were divided into a training cohort (80%) and a held-out test cohort (20%) using stratified sampling. Five algorithms were evaluated: logistic regression, support vector machine with radial basis function kernel, random forest, extra trees, and gradient boosting. The final model was selected by mean cross-validated AUROC, refitted on the full training cohort, and evaluated once in the held-out test cohort. Interpretability analyses examined global feature importance and distributional patterns of leading predictors. Results: Gradient boosting was prespecified by cross-validation in the training cohort. The model achieved an AUROC of 0.872 (95% CI: 0.769-0.952) and an AUPRC of 0.883 (95% CI: 0.780-0.959) in a held-out test cohort, with sensitivity of 0.750 and specificity of 0.812. Conclusions: Longitudinal clinical laboratory tests obtained during routine care contained informative and clinically plausible signals for P-TMA risk. Notably, cystatin C at week 6 showed promise as an early monitoring indicator.

### 🤖 AI 总结

**一句话总结**：Background: Pregnancy-associated thrombotic microangiopathy (P-TMA) is rare but life-threatening. Early risk prediction before overt clinical presentation remains challenging, as the associated labora...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Interpretable, Machine, Learning, Antepartum, Prediction, Pregnancy-Associated, Thrombotic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13786v1) | [下载PDF](https://arxiv.org/pdf/2605.13786v1.pdf)

---

## [24. Attention Once Is All You Need: Efficient Streaming Inference with Stateful Transformers](https://arxiv.org/abs/2605.13784v1)

**作者**：Victor Norgren  
**分类**：cs.LG  
**发布时间**：2026-05-13

### 📄 论文摘要

Conventional transformer inference engines are request-driven, paying an O(n) prefill cost on every query. In streaming workloads, where data arrives continuously and queries probe an ever-growing context, this cost is prohibitive. We introduce a data-driven computational model centred on stateful sessions: a persistent KV cache advanced incrementally as new data arrives, so prefill is moved off the critical path and query latency becomes O(|q|), independent of accumulated context size. Building on this, Flash Queries reclaim idle GPU cycles between data arrivals to pre-evaluate registered questions and return cached answers before the user asks, a pattern that is structurally impossible in stateless engines because they discard intermediate state between requests. A multi-tenant continuous-batching scheduler with cell-budget admission and prefix-aware grouped prefill lets dozens of stateful sessions coexist on a single GPU while preserving full quadratic self-attention. On streaming market-data benchmarks the reference implementation achieves up to 5.9x speedup over conventional inference engines (vLLM, SGLang, TensorRT-LLM, llama.cpp), holding query latency constant as accumulated context grows.

### 🤖 AI 总结

**一句话总结**：Conventional transformer inference engines are request-driven, paying an O(n) prefill cost on every query. In streaming workloads, where data arrives continuously and queries probe an ever-growing con...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Attention, Once, All, Need, Efficient, Streaming, Inference, Stateful

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13784v1) | [下载PDF](https://arxiv.org/pdf/2605.13784v1.pdf)

---

## [25. MinT: Managed Infrastructure for Training and Serving Millions of LLMs](https://arxiv.org/abs/2605.13779v1)

**作者**：Mind Lab, :, Song Cao 等 63 位作者  
**分类**：cs.LG, cs.AI, cs.DC  
**发布时间**：2026-05-13

### 📄 论文摘要

We present MindLab Toolkit (MinT), a managed infrastructure system for Low-Rank Adaptation (LoRA) post-training and online serving. MinT targets a setting where many trained policies are produced over a small number of expensive base-model deployments. Instead of materializing each policy as a merged full checkpoint, MinT keeps the base model resident and moves exported LoRA adapter revisions through rollout, update, export, evaluation, serving, and rollback, hiding distributed training, serving, scheduling, and data movement behind a service interface. MinT scales this path along three axes. Scale Up extends LoRA RL to frontier-scale dense and MoE architectures, including MLA and DSA attention paths, with training and serving validated beyond 1T total parameters. Scale Down moves only the exported LoRA adapter, which can be under 1% of base-model size in rank-1 settings; adapter-only handoff reduces the measured step by 18.3x on a 4B dense model and 2.85x on a 30B MoE, while concurrent multi-policy GRPO shortens wall time by 1.77x and 1.45x without raising peak memory. Scale Out separates durable policy addressability from CPU/GPU working sets: a tensor-parallel deployment supports 10^6-scale addressable catalogs (measured single-engine sweeps through 100K) and thousand-adapter active waves at cluster scale, with cold loading treated as scheduled service work and packed MoE LoRA tensors improving live engine loading by 8.5-8.7x. MinT thus manages million-scale LoRA policy catalogs while training and serving selected adapter revisions over shared 1T-class base models.

### 🤖 AI 总结

**一句话总结**：We present MindLab Toolkit (MinT), a managed infrastructure system for Low-Rank Adaptation (LoRA) post-training and online serving. MinT targets a setting where many trained policies are produced over...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, MinT, Managed, Infrastructure, Training, Serving, Millions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13779v1) | [下载PDF](https://arxiv.org/pdf/2605.13779v1.pdf)

---

## [26. High-Rate Quantized Matrix Multiplication II](https://arxiv.org/abs/2605.13768v1)

**作者**：Or Ordentlich, Yury Polyanskiy  
**分类**：cs.LG, cs.AI, cs.IT  
**发布时间**：2026-05-13

### 📄 论文摘要

This is the second part of the work investigating quantized matrix multiplication (MatMul). In part I we considered the case of calibration-free quantization, whereas here we discuss the setting where covariance matrix $Σ_X$ of the columns of the second factor is available. This setting arises in the ubiquitous task of weight-only post-training quantization of LLMs.   Weight-only quantization is related to the problem of weighted mean squared error (WMSE) source coding, whose classical (reverse) waterfilling solution dictates how one should distribute rate between coordinates of the vector. We show how waterfilling can be used to improve practical LLM quantization algorithms (GPTQ), which at present allocate rate equally. A recent scheme (known as ``WaterSIC'') that only uses scalar INT quantizers is analyzed and its high-rate performance is shown to be (a) basis free (i.e., characterized by the determinant of $Σ_X$ and, thus, unlike existing schemes, is immune to applying random rotations); and (b) within a multiplicative factor of $\frac{2πe}{12}$ (or 0.25 bit/entry) of the information-theoretic distortion limit. GPTQ's performance, in turn, is affected by the choice of basis, but for a random rotation and actual $Σ_X$ from Llama-3-8B we find it to be within 0.1 bit (depending on the layer type) of WaterSIC, suggesting that GPTQ with random rotation is also near optimal, at least in the high-rate regime.

### 🤖 AI 总结

**一句话总结**：This is the second part of the work investigating quantized matrix multiplication (MatMul). In part I we considered the case of calibration-free quantization, whereas here we discuss the setting where...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：II, of, High-Rate, Quantized, Matrix, Multiplication, second, part

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13768v1) | [下载PDF](https://arxiv.org/pdf/2605.13768v1.pdf)

---

## [27. Toward AI-Driven Digital Twins for Metropolitan Floods: A Conditional Latent Dynamics Network Surrogate of the Shallow Water Equations](https://arxiv.org/abs/2605.13761v1)

**作者**：Phillip Si, Yuan Qiu, Omar Sallam 等 7 位作者  
**分类**：cs.LG, cs.CE  
**发布时间**：2026-05-13

### 📄 论文摘要

AI-driven flood digital twins demand fast hydrodynamic surrogates for ensemble forecasting and observation assimilation. Yet even GPU-accelerated two-dimensional shallow water equation (SWE) solvers still require $\sim 55$ minutes per $96$-hour run on a $\sim 4.2$-million-active-cell metropolitan basin (the Des~Plaines River basin at $30\,\mathrm{m}$ resolution), making such workloads prohibitive at native resolution. We present the Conditional Latent Dynamics Network (CLDNet): a low-dimensional latent neural ODE driven by rainfall, paired with a coordinate-based decoder conditioned on static terrain (elevation, slope, Manning roughness) that reconstructs depth and discharge at arbitrary query points. Pointwise decoding decouples memory from grid size and handles irregular watersheds natively, enabling metropolitan-scale training on a single compute node and direct queries at exact gauge coordinates without raster snapping. We evaluate CLDNet on a synthetic $250{,}000$-cell Texas benchmark and on a new Des~Plaines case study of $114$ real-rainfall Stage~IV storms whose reference simulator we validate against United States Geological Survey (USGS) gauges at the April~2013 flood-of-record (Nash--Sutcliffe efficiency $0.57$--$0.94$ on mean-recentered water-surface elevation). CLDNet roughly halves the relative root-mean-squared error of an unconditional baseline, outperforms regular-grid VAE--ConvLSTM and FNO baselines on the Texas benchmark (both presuppose a Cartesian grid and do not apply to the irregular Des~Plaines watershed), reaches a critical success index of $\approx 86\%$ at the $0.5\,\mathrm{m}$ inundation threshold, and produces a full $96$-hour basin-wide forecast in $\sim 29$ seconds -- a $\sim 115\times$ speedup.

### 🤖 AI 总结

**一句话总结**：AI-driven flood digital twins demand fast hydrodynamic surrogates for ensemble forecasting and observation assimilation. Yet even GPU-accelerated two-dimensional shallow water equation (SWE) solvers s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Toward, AI-Driven, Digital, Twins, Metropolitan, Floods, Conditional, Latent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13761v1) | [下载PDF](https://arxiv.org/pdf/2605.13761v1.pdf)

---

## [28. Fast and effective algorithms for fair clustering at scale](https://arxiv.org/abs/2605.13759v1)

**作者**：Claudio Mantuano, Manuel Kammermann, Philipp Baumann  
**分类**：cs.LG  
**发布时间**：2026-05-13

### 📄 论文摘要

Clustering is an unsupervised machine learning task that consists of identifying groups of similar objects. It has numerous applications and is increasingly used in fairness-sensitive domains where objects represent individuals, such as customers, employees, or students. We address a fair clustering problem in which objects belong to protected groups. The problem consists of partitioning the objects into a predefined number of clusters while attaining a user-defined target level of fairness, meaning that each protected group is sufficiently represented in each cluster. The objective is to minimize the clustering cost, defined as the sum of squared Euclidean distances between the objects and the centers of their clusters. Since clustering cost and fairness are generally in conflict, managing the trade-off between them is essential in practical applications. Existing methods provide limited control over this trade-off and either fail to scale to large datasets or, when they scale, produce low-quality solutions. We propose a general framework for fair clustering that provides precise control over the cost-fairness trade-off and introduce three heuristics based on it. The first heuristic focuses on solution quality and the flexibility to incorporate additional constraints, the second improves scalability while retaining high solution quality, and the third is designed for maximum scalability, producing solutions for instances with millions of objects in seconds. The proposed heuristics outperform existing approaches in comprehensive numerical experiments on benchmark datasets. The source code of our heuristics and instructions for reproducing the experiments are publicly available on GitHub.

### 🤖 AI 总结

**一句话总结**：Clustering is an unsupervised machine learning task that consists of identifying groups of similar objects. It has numerous applications and is increasingly used in fairness-sensitive domains where ob...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, an, Fast, effective, algorithms, fair, clustering, scale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13759v1) | [下载PDF](https://arxiv.org/pdf/2605.13759v1.pdf)

---

## [29. Min Generalized Sliced Gromov Wasserstein: A Scalable Path to Gromov Wasserstein](https://arxiv.org/abs/2605.13753v1)

**作者**：Ashkan Shahbazi, Xinran Liu, Ping He 等 4 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-05-13

### 📄 论文摘要

We propose min Generalized Sliced Gromov--Wasserstein (min-GSGW), a sliced formulation for the Gromov--Wasserstein (GW) problem using expressive generalized slicers. The key idea is to learn coupled nonlinear slicers that assign compatible push-forward values to both input measures, so that monotone coupling in the projected domain lifts to a transport plan evaluated against the GW objective in the original spaces. The resulting plan induces a GW objective value, and min-GSGW minimizes this cost directly in the original spaces. We further show that min-GSGW is rigid-motion invariant, a crucial property for geometric matching and shape analysis tasks. Our contributions are threefold: 1) we introduce generalized slicers into the sliced GW framework, 2) we construct a slicing-based efficient GW transport plan; and 3) we develop an amortized variant that replaces per-instance optimization with a learned slicer for unseen input pairs. We perform experiments on animal mesh matching, horse mesh interpolation, and ShapeNet part transfer. Results show that min-GSGW produces meaningful geometric correspondences and GW objective values at substantially lower computational cost than existing GW solvers.

### 🤖 AI 总结

**一句话总结**：We propose min Generalized Sliced Gromov--Wasserstein (min-GSGW), a sliced formulation for the Gromov--Wasserstein (GW) problem using expressive generalized slicers. The key idea is to learn coupled n...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Min, Generalized, Sliced, Gromov, Wasserstein, Scalable, Path

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13753v1) | [下载PDF](https://arxiv.org/pdf/2605.13753v1.pdf)

---

## [30. GHGbench: A Unified Multi-Entity, Multi-Task Benchmark for Carbon Emission Prediction](https://arxiv.org/abs/2605.13743v1)

**作者**：Yifan Duan, Siyuan Zheng, Lihuan Li 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-13

### 📄 论文摘要

Open datasets and benchmarks for entity-level carbon-emission prediction remain fragmented across access, scale, granularity, and evaluation. We introduce GHGbench, an open dataset and benchmark for company- and building-level greenhouse-gas prediction. The company track contains 32,000+ company-year records from 12,000+ firms with Scope 1+2 and Scope 3 disclosures and financial/sectoral signals; the building track harmonises 491,591 building-year records from 13 open sources into a single schema across 26 metropolitan areas (10 U.S., 15 Australian, 1 Singaporean), with climate covariates and multimodal remote-sensing embeddings. GHGbench defines canonical splits with in-distribution and cross-region/city transfer as primary tasks and temporal hold-out plus short-horizon forecasting as supplementary appendix evidence; headline baselines span gradient-boosted trees, a tabular foundation model, MLP, FT-Transformer, and multimodal fusion, with an LLM panel as auxiliary, all evaluated under multi-seed paired-bootstrap tests. Three benchmark-level findings emerge: (i) building emissions are structurally harder than company emissions; (ii) the in-distribution to out-of-distribution gap dwarfs any within-model gap across both the company track and the building track, and a tabular foundation model is, to our knowledge, the first baseline to open a paired-bootstrap-significant gap over tuned trees on a multi-city building-emissions task; (iii) multimodal remote-sensing embeddings help precisely where tabular generalisation breaks. GHGbench also exposes catastrophic city transfer and the sector-factor lookup ceiling as systematic failure modes. Code and reconstruction recipes are available at GHGbench.

### 🤖 AI 总结

**一句话总结**：Open datasets and benchmarks for entity-level carbon-emission prediction remain fragmented across access, scale, granularity, and evaluation. We introduce GHGbench, an open dataset and benchmark for c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GHGbench, Unified, Multi-Entity, Multi-Task, Benchmark, Carbon, Emission, Prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.13743v1) | [下载PDF](https://arxiv.org/pdf/2605.13743v1.pdf)

---

