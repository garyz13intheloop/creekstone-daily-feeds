# arXiv AI 论文日报 | 2026-11-26

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (17 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (1 篇)

---

## cs.AI

## [1. Knowledge-Base Gradient Descent: Self-Structuring Learning through Question Answering](https://arxiv.org/abs/2611.34841v1)

**作者**：Masahiro Kato  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-11-25

### 📄 论文摘要

We consider the problem of constructing knowledge bases for applications based on large language models, in which the structure of a knowledge base determines how an application can retrieve and connect the information needed to answer a question. We study Self-Structuring Learning, a setting in which questions and expected answers guide the construction of a persistent knowledge base whose editable structure can be a graph schema or the organization of linked knowledge documents. We propose Knowledge-Base Gradient Descent, which diagnoses discrepancies between expected answers and responses obtained through the current knowledge base. At each round, the method proposes a structural edit, rebuilds the knowledge base, and adopts the edit when the learning loss decreases. The retained structure is evaluated on other questions about the same sources. By randomizing over candidate edits, we express the loss change of an edit as a derivative with respect to the probability of selecting it, and we evaluate joint edits as single candidates because their changes interact. Schema Descent instantiates the method for graph schemas. In experiments on large documents, each a bundle of research papers, the updated knowledge cards and graph schemas obtain higher mean Answer F1 on held-out generated questions than their initial structures, with schema gains in every document. On human questions, mean F1 rises for schemas and falls for cards: the updated structures serve the kind of question they were learned from.

### 🤖 AI 总结

**一句话总结**：We consider the problem of constructing knowledge bases for applications based on large language models, in which the structure of a knowledge base determines how an application can retrieve and conne...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Knowledge-Base, Gradient, Descent, Self-Structuring, Learning, through, Question, Answering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34841v1) | [下载PDF](https://arxiv.org/pdf/2611.34841v1.pdf)

---

## cs.CL

## [2. Diverse Alternative Reasoning Traces for Hard Math Problems](https://arxiv.org/abs/2611.34928v1)

**作者**：Lukas Aichberger, Adam Golinski, Arno Blaas 等 8 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-11-25

### 📄 论文摘要

Post-training large language models (LLMs) for mathematical reasoning often relies on accepted traces whose final answers pass a verifier. For hard math problems, however, such traces can be rare under independent Monte Carlo (MC) sampling. To address this, we propose Diverse Alternative Reasoning Traces (DART), a trace-mining method that starts from a rejected trace, decomposes it into reasoning steps, and ranks them by position-weighted uncertainty. It then generates deliberately distinct alternative candidates for highly ranked steps using reference-answer guidance and a meta-thought before completing the resulting traces. On greedy-unsolved DeepMath-103K problems, DART recovers 37% more problems than MC sampling at a matched number of generated traces. Its estimated generation cost per recovered problem is nearly identical, while its cost per accepted trace is 30% lower. Post-training Llama-3.1-8B-Instruct on traces mined by DART achieves the highest point estimate in five of six evaluations across MATH-500 and AIME benchmarks. These results demonstrate that revisiting rejected traces with DART can expand problem coverage and provide effective post-training data.

### 🤖 AI 总结

**一句话总结**：Post-training large language models (LLMs) for mathematical reasoning often relies on accepted traces whose final answers pass a verifier. For hard math problems, however, such traces can be rare unde...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diverse, Alternative, Reasoning, Traces, Hard, Math, Problems, Post-training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34928v1) | [下载PDF](https://arxiv.org/pdf/2611.34928v1.pdf)

---

## [3. $μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents](https://arxiv.org/abs/2611.34920v1)

**作者**：Qihao Lin, Guanxu Chen, Shuhang Zheng 等 10 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-11-25

### 📄 论文摘要

Voice agents in shared spaces must satisfy interdependent multi-user requests while upholding per-user authority, privacy, and task constraints. Existing evaluations offer limited coverage when participants react throughout a session. We introduce $μ$-Bench, a benchmark for joint task completion in closed-loop, full-duplex multi-user voice interaction. Simulated participants act from isolated profiles of goals, knowledge, and permissions, adapting to the agent's speech and tool outcomes. Across 20 domains, 100 scenarios vary group size, acoustics, and follow-up demands to form 800 cases (408 tool-augmented, 392 tool-free). Joint Task Success (JTS) requires all user goals, privacy boundaries, and terminal states to hold jointly, while Pure JTS further disallows unauthorized tool calls; Attribution, Threading, and Coordination (ATC) diagnostics localize failures. Across 13 voice agents, proprietary systems peak at 62.24\% tool-free and 65.44\% tool-augmented success, while open-weight models remain below 20\%. ATC diagnostics show that open-weight models lag primarily in multi-turn attribution and threading, and controlled contrasts reveal that larger groups consistently degrade joint task success across capable systems. By coupling reactive multi-user simulation with verifiable session-level outcomes, $μ$-Bench provides a rigorous testbed for shared voice agents.

### 🤖 AI 总结

**一句话总结**：Voice agents in shared spaces must satisfy interdependent multi-user requests while upholding per-user authority, privacy, and task constraints. Existing evaluations offer limited coverage when partic...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：$μ$-Bench, Benchmarking, Multi-User, Task, Completion, Shared, Interaction, Voice

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34920v1) | [下载PDF](https://arxiv.org/pdf/2611.34920v1.pdf)

---

## [4. DRBench Pro: A Knowledge-Centric Benchmark for Professional Deep Research Agents](https://arxiv.org/abs/2611.34852v1)

**作者**：Han Huang, Yuchen Yan, Xingyu Wu 等 8 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-11-25

### 📄 论文摘要

Deep research agents gather information from multiple sources and synthesize it into reports on complex, open-ended questions. Existing benchmarks assess report quality along several dimensions, but lack a dedicated knowledge-centric evaluation of which research directions a report covers and how deeply it explores them. We introduce DRBench Pro, a benchmark that makes structured knowledge coverage the primary evaluation target. Our automated pipeline builds local knowledge trees from Wikipedia and uses sampled subgraphs to generate research queries and evidence-grounded rubrics. Each rubric corresponds to a relation in the tree, preserving the structure of the knowledge being evaluated. Agents receive only the research query. This structure allows us to measure breadth across major research directions and depth along related knowledge chains, with their geometric mean giving overall coverage. The benchmark includes 144 cases across 24 domains and 44,102 rubrics. Evaluating 16 deep research agents reveals different strengths in breadth and depth, with the best-performing agent reaching 57.04% overall coverage. Rubric judgments agree closely with human annotations, and agent rankings remain stable across the tested metric configurations.

### 🤖 AI 总结

**一句话总结**：Deep research agents gather information from multiple sources and synthesize it into reports on complex, open-ended questions. Existing benchmarks assess report quality along several dimensions, but l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, DRBench, Pro, Knowledge-Centric, Benchmark, Professional, Deep, Research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34852v1) | [下载PDF](https://arxiv.org/pdf/2611.34852v1.pdf)

---

## [5. Proverbs As A Window On Collective Prescriptions](https://arxiv.org/abs/2611.34832v1)

**作者**：Tomás Lejarraga, Dirk U. Wulff, Ralph Hertwig  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-11-25

### 📄 论文摘要

Proverbs, as repositories of traditional wisdom, have informed human reasoning for millennia. Yet the collective prescriptions they encode have remained largely unquantified. We introduce a computational framework to analyze nearly 50,000 English-language proverbs. Using large language models, validated against human judgments, we map the topical landscape of proverbs, assess their prescriptive power, and quantify their recommendations on key dimensions of human judgment and behavior. We find that most proverbs are prescriptive, offering guidance in domains under individual control, such as preparation and prudent action, whereas proverbs about uncontrollable circumstances, such as fate and mortality, tend to describe rather than prescribe. When prescriptive proverbs take a consistent stance, they favor caution over risk, long-term over short-term outcomes, honesty over deception, and kindness over malice, and show a moderate tendency toward suspicion over trust. On dimensions involving genuine trade-offs, especially autonomy versus compliance, proverbs provide contradicting advice rather than a single recommendation. This analysis provides a quantitative map of the collective prescriptions in a culture's proverbial wisdom, revealing a core of prudent, honest, and forward-looking guidance alongside varied advice where circumstances dictate the best course of action.

### 🤖 AI 总结

**一句话总结**：Proverbs, as repositories of traditional wisdom, have informed human reasoning for millennia. Yet the collective prescriptions they encode have remained largely unquantified. We introduce a computatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, of, Proverbs, Window, Collective, Prescriptions, repositories, traditional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34832v1) | [下载PDF](https://arxiv.org/pdf/2611.34832v1.pdf)

---

## [6. Repairing the Trustworthiness of Distilled Language Models](https://arxiv.org/abs/2611.34831v1)

**作者**：Kumar Shubham, Devendra Vyas, Vidushi Agarwal 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-11-25

### 📄 论文摘要

Knowledge distillation enables the deployment of large language models through smaller student models, but the compression process can introduce regressions in trustworthiness even when downstream performance is preserved. Repairing such failures is challenging because the original distillation corpus is often unavailable, while direct preference optimization may alter capabilities inherited from the teacher. We propose a targeted repair framework based on the proximal Bregman response function (PBRF) that addresses both limitations. We estimate the curvature required for PBRF using a surrogate proxy dataset, removing dependence on the original transfer corpus, and extend the framework to preference-based supervision through an odds-ratio objective. This enables the use of preferred and dispreferred response pairs while constraining changes to the distilled model. Our results show that the proposed approach improves targeted trustworthiness behaviors for both pre-training and post-training models while largely preserving downstream performance, providing a practical alternative to re-distillation or unconstrained preference optimization. Our experiment results show that across different distilled models, the trustworthy regression can be improved by up to 8% with less than 1% decrement in perplexity.

### 🤖 AI 总结

**一句话总结**：Knowledge distillation enables the deployment of large language models through smaller student models, but the compression process can introduce regressions in trustworthiness even when downstream per...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Repairing, Trustworthiness, Distilled, Language, Models, Knowledge, distillation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34831v1) | [下载PDF](https://arxiv.org/pdf/2611.34831v1.pdf)

---

## cs.CV

## [7. AnyCam: Anything Can Represent Camera for Video Generation](https://arxiv.org/abs/2611.34944v1)

**作者**：Weijie Lyu, Zhixin Shu, Yuntian Ke 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-25

### 📄 论文摘要

Camera-controlled video generation re-renders a video along a target camera trajectory, yet moving the camera around an object, the most natural way to change the viewpoint of an object-centric scene, remains difficult. Existing methods condition either on camera parameters, which are scale-ambiguous in monocular video, or on explicit geometry such as warped point clouds or depth, which breaks down under large viewpoint changes. We present AnyCam, a method that represents the camera with an anchor object in the scene: we reconstruct it in 3D and render it along the target trajectory, a camera signal that is scale-aware, view-complete and easy to specify relative to the object. A video diffusion model transfers the content and dynamics of the source video to the new viewpoint. Its H-Concat layout aligns source and target frames in time, so the model can be distilled into AnyCam-AR, a streaming few-step generator for on-the-fly camera control. Both models are trained on paired videos with pixel-aligned anchor renderings from multi-camera videos and static-scene captures. Experiments on diverse datasets and trajectories show that AnyCam performs favorably against camera-controlled video generation and 3D reconstruction methods in camera control and visual quality.

### 🤖 AI 总结

**一句话总结**：Camera-controlled video generation re-renders a video along a target camera trajectory, yet moving the camera around an object, the most natural way to change the viewpoint of an object-centric scene,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AnyCam, Anything, Can, Represent, Camera, Video, Generation, Camera-controlled

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34944v1) | [下载PDF](https://arxiv.org/pdf/2611.34944v1.pdf)

---

## [8. Tracking Any Point with Agentic Visual Reasoning](https://arxiv.org/abs/2611.34943v1)

**作者**：Xuweiyi Chen, Jin Yao, Linzhan Mou 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-25

### 📄 论文摘要

A general-purpose Vision-Language Model (VLM) has surpassed expert vision models in many domains such as object detection and video recognition. However, point correspondence is known to be challenging for VLMs since it goes beyond object-level recognition: it requires pixel-level localization of the same physical surface point across observations, even when appearance changes or the point disappears and later reappears. In this paper, we introduce AgenTAP, a VLM-based agent that directly predicts point coordinates and visibility and actively reasons over videos. Starting from its own estimate, the agent autonomously chooses what to inspect and uses the resulting evidence to verify point identity and refine its predictions. With GPT-6 Astra, it surpasses expert vision models in both point localization and visibility prediction, without correspondence-specific fine-tuning. We further use AgenTAP to re-identify physical points after disappearance and reconnect fragmented tracks, constructing EgoTAP-4D, a dataset of 3D point trajectories in long real-world egocentric videos. On sampled reappearing points, its predictions approach human agreement, and adding EgoTAP-4D to D4RT training improves average 3D tracking performance.

### 🤖 AI 总结

**一句话总结**：A general-purpose Vision-Language Model (VLM) has surpassed expert vision models in many domains such as object detection and video recognition. However, point correspondence is known to be challengin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Tracking, Any, Point, Agentic, Visual, Reasoning, general-purpose, Vision-Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34943v1) | [下载PDF](https://arxiv.org/pdf/2611.34943v1.pdf)

---

## [9. Improving and Expanding Video Editing Capabilities Without Videos](https://arxiv.org/abs/2611.34941v1)

**作者**：Ji Xie, Yanhao Jia, Xiangpeng Yang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-25

### 📄 论文摘要

Image editing models can follow a wide range of instructions, but video editing models still lag behind, limited in part by the difficulty of collecting paired source and edited videos. Is it possible to transfer advanced image editing capabilities to video editors without new paired videos? We introduce Image-to-Video Transfer (I2VT), which improves pretrained video editors and expands them to new editing tasks using an image editor. It enables efficient post-training with no architectural changes and no new videos, using only individual images. Our key idea is to let the video editor role-play as an image editor: it edits an image as a one-frame video, with the image editor guiding the video editor's predictions at each denoising step. Although the video editor sees only single images during training, at test time it applies the improved and expanded capabilities to whole video clips while preserving temporal consistency. To push the boundaries of video editing, we introduce OpenVE++, an extension of OpenVE-Bench that adds four new editing tasks useful for video production, including action changes, expression changes, body movements, and scene relighting. Our experiments across three different video editors show that I2VT improves existing editing capabilities and expands them to new tasks, and our models achieve state-of-the-art (SOTA) performance on both OpenVE-Bench and OpenVE++.

### 🤖 AI 总结

**一句话总结**：Image editing models can follow a wide range of instructions, but video editing models still lag behind, limited in part by the difficulty of collecting paired source and edited videos. Is it possible...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Improving, Expanding, Video, Editing, Capabilities, Without, Videos, Image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34941v1) | [下载PDF](https://arxiv.org/pdf/2611.34941v1.pdf)

---

## [10. LuxAvatar: Real-Time Relightable Head Avatars via Causal Neural Shading of 3D Intrinsic Proxies](https://arxiv.org/abs/2611.34940v1)

**作者**：Yipengjing Sun, Chenyang Wang, Boyao Zhou 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-25

### 📄 论文摘要

We present LuxAvatar, a feed-forward framework for real-time head avatar animation and relighting from a single portrait. To achieve both 3D controllability and complex facial light transport, we factorize avatar synthesis into an animatable 3D intrinsic Gaussian proxy and a causal autoregressive neural shader. This proxy disentangles canonical geometry and reflectance attributes, rapidly rasterizing deformed Gaussians into view- and motion-consistent PBR buffers. Conditioned on these buffers, our neural shader formulates forward rendering as a conditional video diffusion process, bypassing explicit PBR computation to synthesize realistic shading effects under target illumination. We achieve real-time streaming through heterogeneous distillation from a pretrained multi-step bidirectional relighting teacher to a two-step causal autoregressive neural shader, inheriting broad synthetic lighting priors while minimizing conditioning and decoding latency. To further specialize these priors to human heads, we construct a hybrid relighting dataset for domain-specific fine-tuning, capturing authentic facial dynamics and physically grounded light transport. Extensive experiments show that our framework enables 3D-controllable, real-time portrait animation and relighting, outperforming state-of-the-art methods in visual fidelity, motion control, and lighting accuracy.

### 🤖 AI 总结

**一句话总结**：We present LuxAvatar, a feed-forward framework for real-time head avatar animation and relighting from a single portrait. To achieve both 3D controllability and complex facial light transport, we fact...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LuxAvatar, Real-Time, Relightable, Head, Avatars, via, Causal, Neural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34940v1) | [下载PDF](https://arxiv.org/pdf/2611.34940v1.pdf)

---

## [11. A Mesh for Every Moment](https://arxiv.org/abs/2611.34939v1)

**作者**：Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-11-25

### 📄 论文摘要

We present MEMO (a Mesh for Every MOment), a method that reconstructs the geometry of complete dynamic scenes, captured by multiple synchronized cameras, and extracts a mesh at every frame. Existing dynamic Gaussian splatting methods either model appearance alone or target isolated objects segmented by foreground masks, and all of them recover meshes by TSDF fusion or Poisson reconstruction, whose fixed grids limit the detail they can capture. At the core of MEMO is a per-Gaussian motion model inspired by Gaussian processes, which represents each Gaussian's position and rotation over time as a combination of temporal Gaussian kernels. The model keeps every Gaussian a valid surface element throughout the sequence and carries an implicit representation of the dynamic geometry, so a mesh can be derived at any time from a field defined by the Gaussians. Although common in real captures, large and fast motion poses a challenge that dynamic Gaussian splatting methods usually overlook. To account for it, we design a track-based initialization scheme that fits each Gaussian's initial trajectory to point tracks in closed form. We evaluate MEMO on Blender-Moments, a new benchmark of nine animated scenes with ground-truth meshes at every frame, and on two real-world datasets. MEMO reconstructs the most accurate geometry among state-of-the-art methods, and remains competitive in novel-view synthesis and training time. Project page: https://memo-4d.github.io

### 🤖 AI 总结

**一句话总结**：We present MEMO (a Mesh for Every MOment), a method that reconstructs the geometry of complete dynamic scenes, captured by multiple synchronized cameras, and extracts a mesh at every frame. Existing d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Mesh, Every, Moment, present, MEMO, method, reconstructs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34939v1) | [下载PDF](https://arxiv.org/pdf/2611.34939v1.pdf)

---

## [12. DynMF2: Rigid Motion Factorization by Expectation-Maximization for Monocular 4D Reconstruction and Motion Segmentation](https://arxiv.org/abs/2611.34931v1)

**作者**：Agelos Kratimenos, Yile Hua, Kostas Daniilidis  
**分类**：cs.CV  
**发布时间**：2026-11-25

### 📄 论文摘要

A single casual video leaves a moving scene under-determined: a point seen once from each place can slide toward or away from the camera and still match every frame. We constrain the reconstruction with the structure of the motion itself. Building on DynMF, we model a scene's motion as a handful of SE(3) trajectories, each rigid, and let every point follow one of them alone, never a blend. DynMF2 computes this factorization directly from 3D point trajectories, with no rendering, by Expectation-Maximization (EM). Its M-step fits, in closed form, every rigid motion to the points assigned to it, and its E-step reassigns every point to the motion that explains it with the least error. The background is simply one more motion, the camera's, so no masks are needed. Three tools then revise the factorization: requery adds trajectories where the rendering shows parts the tracker missed, merge joins motions that move together, and split separates those that do not. Thus the number of motions follows the scene. Without masks, DynMF2 clearly outperforms the mask-based baselines in view synthesis on iPhone and NVIDIA and in 3D tracking on iPhone. It recovers what masks leave out, from thin parts and details to small movers far in the background. Its motions segment the moving parts of MOVi-F and iTACO scenes competitively, although DynMF2 is never trained to segment. What moves in a scene is not decided in advance: it emerges from the rigid motions themselves.

### 🤖 AI 总结

**一句话总结**：A single casual video leaves a moving scene under-determined: a point seen once from each place can slide toward or away from the camera and still match every frame. We constrain the reconstruction wi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, DynMF2, Rigid, Motion, Factorization, Expectation-Maximization, Monocular, Reconstruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34931v1) | [下载PDF](https://arxiv.org/pdf/2611.34931v1.pdf)

---

## [13. LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE](https://arxiv.org/abs/2611.34912v1)

**作者**：Jiachen An, Sijie Zhao, Le Li 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-25

### 📄 论文摘要

While video diffusion models have grown faster and increasingly streamable, the video VAE remains a primary latency bottleneck across interactive generation and editing pipelines. Existing VAEs and their acceleration methods rely mainly on heavy convolutions or full frame attention, and most focus only on decoding, leaving encoding costly for streaming conditional generation and editing. This raises a natural question: Do video VAE encoding and decoding actually require such global spatiotemporal modeling? By analyzing the effective receptive fields of pretrained video VAEs, we find that both encoding and decoding a patch rely almost entirely on its spatial and temporal neighbors. To exploit this strong locality, we introduce LiveVAE, a streaming encoder and decoder built on causal window attention, which cuts per frame compute while keeping the temporal KV cache bounded for streaming. Decoupled encoder/decoder distillation followed by joint finetuning preserves the pretrained latent space, making LiveVAE a drop-in replacement for the original VAE. On MiniMax-H3, LiveVAE achieves 5.2-6.2x faster encoding and 3.0-3.3x faster decoding than the official VAE with higher PSNR. Paired with our dedicated inference infrastructure, LiveVAE pushes the speedup to 13.4x with almost no quality loss. Code and models will be released.

### 🤖 AI 总结

**一句话总结**：While video diffusion models have grown faster and increasingly streamable, the video VAE remains a primary latency bottleneck across interactive generation and editing pipelines. Existing VAEs and th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LiveVAE, Causal, Window, Attention, Makes, Efficient, Streaming, Video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34912v1) | [下载PDF](https://arxiv.org/pdf/2611.34912v1.pdf)

---

## [14. Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation](https://arxiv.org/abs/2611.34907v1)

**作者**：Shaoteng Liu, Shuai Yang, Wei Huang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-25

### 📄 论文摘要

Real-time autoregressive video generators stream minutes of video and accept new prompts on the fly, but struggle to keep people, objects, and places consistent over a long interactive story. Agent systems provide such memory for offline multi-shot generation, yet they read the whole script in advance, plan each shot before generating it, and regenerate failed shots, which a live stream does not allow. We present Agentic LongLive, an asynchronous agentic memory for long video generation. A memory agent on separate GPUs reads only the prompts revealed so far, never the generated video, and keeps a text state and evolving images for every person, object, and scene. From this entity memory it composes a global image and a per-shot memory image, which an auxiliary GPU prefills into the generator's attention sink before the next shot starts, and writes entity cards for the prompts that name them, so the video never waits for memory and video errors are not written back. A small language model, trained with reinforcement learning and an image reward calibrated using downstream video outcomes, decides what to remember before the next prompt is known. On LongStory-Online, a new benchmark of 25 stories (857 shots) revealed one shot at a time, Agentic LongLive improves persistent-state accuracy of LongLive-2.0, its base generator, by 26.3 points, protagonist identity by 44.9, and revisited-place consistency by 40.4, at about 1% extra generation time on H100. The full system streams faster than real time on one 8xB200 node with the generator in BF16 (34.3 FPS), keeps image quality stable over 14-minute stories, and improves identity on two MiniMax-H3 generators, one of which, LongLive-H3, also runs in real time with it. To our knowledge, it is the first real-time video generator with text and image memory kept by an LLM agent.

### 🤖 AI 总结

**一句话总结**：Real-time autoregressive video generators stream minutes of video and accept new prompts on the fly, but struggle to keep people, objects, and places consistent over a long interactive story. Agent sy...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agentic, LongLive, Asynchronous, Memory, Long, Video, Generation, Real-time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34907v1) | [下载PDF](https://arxiv.org/pdf/2611.34907v1.pdf)

---

## [15. ProbFaS: Probabilistic Video Frame Selection for MLLMs via Multi-Fidelity Calibration](https://arxiv.org/abs/2611.34903v1)

**作者**：Tianru Zhang, Mayank Nautiyal, Hugo Eidmann 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-25

### 📄 论文摘要

Processing long videos with multimodal large language models (MLLMs) is prohibitively expensive, making informative frame selection essential for accurate video understanding. The default uniform sampling often misses task-relevant keyframes, while recent training-free selectors instead pick frames by how well each one matches the question under an image-text alignment (ITA) score. However, we show that ITA signals correspond poorly with the MLLM's true needs: their rankings correlate weakly with downstream accuracy and are even negatively correlated on over 40% of questions, whereas the MLLM's internal yes/no judgment yields a much stronger signal. We present ProbFaS, a training- and label-free probabilistic pipeline that fuses both signals for key frame selection. ProbFaS treats dense ITA scores as cheap, biased measurements and sparse MLLM judgments as accurate, costly ones, unifying them via co-kriging, a multi-fidelity Gaussian process, to calibrate relevance across all frames. A temporal determinantal point process then selects frames capturing relevance peaks while preserving temporal coverage. Across Video-MME, MLVU and LongVideoBench, ProbFaS is the most accurate among fourteen state-of-the-art training-free selectors and uniform sampling in 13 of 15 settings (8-128 frames), outperforming the strongest baseline by up to 3.1 percentage points. On MLVU and LongVideoBench, 32 ProbFaS frames match or surpass the top baseline at 128 frames and uniform sampling with up to 768 frames.

### 🤖 AI 总结

**一句话总结**：Processing long videos with multimodal large language models (MLLMs) is prohibitively expensive, making informative frame selection essential for accurate video understanding. The default uniform samp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ProbFaS, Probabilistic, Video, Frame, Selection, MLLMs, via, Multi-Fidelity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34903v1) | [下载PDF](https://arxiv.org/pdf/2611.34903v1.pdf)

---

## [16. Enhancing Maritime Domain Awareness using Latent Space Representations](https://arxiv.org/abs/2611.34899v1)

**作者**：Rikard Vinge, Miguel A. Belenguer-Plomer, Isabelle Wittmann 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-11-25

### 📄 论文摘要

This work presents a novel application of Earth Observation (EO) embeddings for Maritime Domain Awareness (MDA) from the perspective of the geospatial foundation model TerraMind. By operating directly on compressed latent-space representations rather than on the original Sentinel-1 imagery, this approach directly addresses the data gravity bottleneck that increasingly constrains operational EO processing, in line with the objectives of the Embed2Scale project. In particular, linear and non-linear probing of compressed embeddings, latent space representations of synthetic aperture radar (SAR) imagery, is used to detect, localise, and characterise vessels from Sentinel-1 GRD images. Vessel detection achieves a ROC-AUC of 0.95, while vessel localisation has a median error of around 300 m for vessels longer than 100 m, and vessel AIS type-code classification achieves 62% accuracy for the majority classes. The latter, however, is highly correlated with vessel length. These results reveal both the potential and current limitations of Geospatial Foundation Models (GeoFMs) when applied to fine-grained MDA understanding in real-world scenarios.   Additionally, a new maritime remote sensing dataset is released, pairing about 2,000 Sentinel-1 images with temporally aligned AIS signals from commercial vessels. Through manual inspection, each candidate sample was verified for bounding-box quality and for consistency between the AIS-reported vessel length and the observed vessel extent, cross-checking vessel identity and location against publicly available vessel records and, where available, photographs. The dataset was made ready for use with the NeuCo-Bench neural compression benchmark framework, publicly available on HuggingFace through https://huggingface.co/datasets/embed2scale/S1-single-ship-downstream .

### 🤖 AI 总结

**一句话总结**：This work presents a novel application of Earth Observation (EO) embeddings for Maritime Domain Awareness (MDA) from the perspective of the geospatial foundation model TerraMind. By operating directly...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Enhancing, Maritime, Domain, Awareness, Latent, Space, Representations, work

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34899v1) | [下载PDF](https://arxiv.org/pdf/2611.34899v1.pdf)

---

## [17. What a Drop Reveals: Sim-to-Real Material Estimation for Deformable Objects from Video](https://arxiv.org/abs/2611.34894v1)

**作者**：Ziyue Peng, Yanxi Hu, Junyoung Kim 等 10 位作者  
**分类**：cs.CV, cs.GR, cs.LG  
**发布时间**：2026-11-25

### 📄 论文摘要

How an object deforms when it hits the ground reveals what it is made of. From a single real video of a drop, we estimate a deformable object's density-normalized stiffness $E/ρ$, and its yield stress $σ_Y/ρ$ when the impact causes plastic deformation, with a feed-forward predictor trained only in simulation. Real videos carry no material labels, so such predictors are developed and validated on synthetic data alone. We show that synthetic validation ranks their geometric inputs in the wrong order. Material acts through 3D deformation, and tracklets lifted to 3D with estimated depth are indeed the most accurate input in simulation. However, on real drops they are the least accurate, and better depth does not repair them: the failure persists with simulator depth in training, LiDAR depth at test time, and exact depth on rendered replays of the real drops. Short 2D optical-flow tracklets do the opposite: they improve nothing in simulation, yet they transfer best. Material is therefore better read from what perception measures consistently in both domains than from what is most informative in simulation. Our predictor, PhysReader, reads the video and 2D tracklets and learns the lift to 3D in simulation by matching a teacher that sees exact 3D deformation. To measure transfer, we introduce PhysReader-Real: 16 everyday objects dropped five times each, with reference materials fit jointly to each object's drops and checked against tensile tests. On PhysReader-Real, PhysReader is closer to the reference materials than every other input and baseline. The one exception is a per-scene optimizer started from PhysReader's prediction, which ends slightly closer but takes 49 minutes per video instead of 12 seconds.

### 🤖 AI 总结

**一句话总结**：How an object deforms when it hits the ground reveals what it is made of. From a single real video of a drop, we estimate a deformable object's density-normalized stiffness $E/ρ$, and its yield stress...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：What, Drop, Reveals, Sim-to-Real, Material, Estimation, Deformable, Objects

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34894v1) | [下载PDF](https://arxiv.org/pdf/2611.34894v1.pdf)

---

## [18. Stranger Things: When Objects Appear Without Their Typical Neighbors](https://arxiv.org/abs/2611.34881v1)

**作者**：Siddhartha Gairola, Jiahao Xie, Anna Kukleva 等 5 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-25

### 📄 论文摘要

Visual context is a powerful cue for object recognition: scenes inform what, where, and at what scale objects are likely to appear. Yet over-reliance on context becomes a failure mode when models predict objects based on their typical neighbors rather than the objects' own visual features, which we call typicality bias. While extensively studied in the pre-Transformer era, it has often been assumed that architectural and scale improvements would naturally solve it, and a systematic diagnostic across the modern vision stack remains absent. We provide such a diagnostic framework. We measure typicality bias via normalized pointwise mutual information (NPMI) over object pairs, and introduce STRANGE-Bench (Synthetic Typicality-RANked Grounded Evaluation Benchmark): a photorealistic, layout-controlled benchmark spanning 17 sub-tiers from typical to never-co-occurring object pairs. Across five model families (specialist detectors, open-vocabulary detectors, self-supervised, vision-language, and multimodal large language models) and three recognition tasks (supervised detection, open-vocabulary detection, and classification), the bias is prevalent: gaps of 5-11 p.p. persist when objects appear outside their typical company, and do not consistently shrink with scale. To mitigate it, we turn to data augmentation: existing augmentations are designed for visual diversity, not for breaking co-occurrence shortcuts, and sample from the very distribution that produces typicality bias. We propose Anchor-Atypicality Sampling (AAS), a simple sampling rule for paste-based augmentations that uses the NPMI signal to tilt the training-time co-occurrence distribution toward atypical partners. AAS reduces the typicality gap by up to 1.6 p.p. on natural-image COCO splits and 23.0 p.p. on synthetic STRANGE-Bench across three model families, without sacrificing overall performance.

### 🤖 AI 总结

**一句话总结**：Visual context is a powerful cue for object recognition: scenes inform what, where, and at what scale objects are likely to appear. Yet over-reliance on context becomes a failure mode when models pred...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Stranger, Things, When, Objects, Appear, Without, Their, Typical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34881v1) | [下载PDF](https://arxiv.org/pdf/2611.34881v1.pdf)

---

## [19. BOP-Refer: Benchmark for Monocular 3D and 2D Object Grounding](https://arxiv.org/abs/2611.34862v1)

**作者**：Tomas Hodan, Vineet Bhat, Martin Sundermeyer 等 15 位作者  
**分类**：cs.CV, cs.AI, cs.RO  
**发布时间**：2026-11-25

### 📄 论文摘要

We introduce BOP-Refer, the first benchmark for monocular 3D and 2D grounding of everyday and industrial objects sourced from 9 diverse BOP datasets. We pair images from these datasets with VLM-generated and human-verified referring expressions, and derive accurate ground-truth 3D and 2D bounding boxes of the referred objects from their 3D models and 6DoF pose annotations. Our systematic evaluation of 17 frontier VLMs across the major proprietary and open-weight families (Gemini, GPT, Claude, Qwen, Gemma) shows that the best model, Gemini 4 Carbon, reaches 72.6% AP_IoU2D in 2D but only 12.4% AP_IoU3D in 3D, despite the more lenient IoU thresholds in 3D. The predicted 3D boxes are usually centered on the target objects in the image but often off in depth by more than the object's size, suggesting that metric scale estimation, which needs reliable object size priors, is currently by far the main source of error.

### 🤖 AI 总结

**一句话总结**：We introduce BOP-Refer, the first benchmark for monocular 3D and 2D grounding of everyday and industrial objects sourced from 9 diverse BOP datasets. We pair images from these datasets with VLM-genera...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, 2D, We, BOP-Refer, Benchmark, Monocular, Object, Grounding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34862v1) | [下载PDF](https://arxiv.org/pdf/2611.34862v1.pdf)

---

## [20. DocDUR-Net: Degradation-Aware Unified Document Image Restoration](https://arxiv.org/abs/2611.34860v1)

**作者**：Haowei Xu, Peirong Zhang, Xuhan Zheng 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-25

### 📄 论文摘要

Captured document images often suffer from diverse degradations caused by uncontrolled imaging conditions, which reduce readability and obscure fine text structures. Single-degradation restoration methods are usually trained and deployed for individual degradation types, and therefore require model selection before restoration. Unified restoration models alleviate the need to maintain multiple restoration networks by sharing one network across tasks, but representative unified document image restoration methods still depend on external task selection. This dependency limits automatic document image restoration. We propose DocDUR-Net, a degradation-aware unified restoration network that derives restoration guidance directly from the input image. It introduces a Degradation Perception Module (DPM) to extract degradation representations and predict degradation weights, and Degradation Prior-guided Adaptive Feature Fusion (DP-AFF) to combine learnable degradation priors with degradation features extracted from the input. The resulting guidance is injected into a shared restoration backbone, enabling adaptive restoration without external task selection. DocDUR-Net also supports a manual mode with explicit task selection. Experiments on document image restoration benchmarks show that DocDUR-Net achieves the best average PSNR of 29.405 dB and SSIM of 0.960 among unified methods while remaining competitive with single-degradation methods.

### 🤖 AI 总结

**一句话总结**：Captured document images often suffer from diverse degradations caused by uncontrolled imaging conditions, which reduce readability and obscure fine text structures. Single-degradation restoration met...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DocDUR-Net, Degradation-Aware, Unified, Document, Image, Restoration, Captured, images

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34860v1) | [下载PDF](https://arxiv.org/pdf/2611.34860v1.pdf)

---

## [21. Probing Visual Idiosyncrasies in Text-to-Image Models](https://arxiv.org/abs/2611.34843v1)

**作者**：Yongqian Peng, Hongjie Li, Yichao Zhou 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-25

### 📄 论文摘要

Text-to-Image (T2I) models turn short text descriptions into images, and the leading models now produce images of comparable visual quality. Whether their outputs still carry model-specific characteristics matters for attribution, for model comparison beyond aggregate quality, and for evaluations that assume anonymity. We ask whether images from frontier T2I models can still be classified by source, and which visual properties make this possible. Here we show that a standard ResNet-50 identifies the source of an image among HiDream-O1-Dev, FLUX.2-dev, HunyuanImage-3.0, and Qwen-Image-2512, the four highest-ranked open-source models on the Text-to-Image Arena, with 100.00% accuracy on held-out prompts. Human participants reach only 62.61% on the pairwise version of this task, so the distinguishing cues are not visually obvious. They are also not tied to a particular classifier and survive severe image corruptions and out-of-distribution prompts. We trace them to visual idiosyncrasies at three levels. Low-level texture statistics alone let a lightweight multi-layer perceptron match ResNet-50. Object layout, depth, and albedo estimated from the images each carry a source signal. Image captions reveal model-specific preferences in style and background that the prompts never specify. A one-sentence hint about these cues raises human accuracy by 9.03 percentage points. These idiosyncrasies make source classification a tool for measuring similarity between models and between real and generated images, and they caution against assuming anonymity in human preference evaluation of T2I models.

### 🤖 AI 总结

**一句话总结**：Text-to-Image (T2I) models turn short text descriptions into images, and the leading models now produce images of comparable visual quality. Whether their outputs still carry model-specific characteri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：T2I, Probing, Visual, Idiosyncrasies, Text-to-Image, Models, turn, short

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34843v1) | [下载PDF](https://arxiv.org/pdf/2611.34843v1.pdf)

---

## [22. Diffusion Steering via Adaptive Reward Estimation and Resampling](https://arxiv.org/abs/2611.34839v1)

**作者**：Abinitha Gourabathina, Sana Tonekaboni, Marzyeh Ghassemi 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-25

### 📄 论文摘要

Text-to-image diffusion models can generate images that satisfy complex prompts, yet often produce images that omit requested objects, attributes, or relationships. We ask if models can more reliably generate text-aligned images by redistributing probability toward their more successful outcomes. We propose TrailMix, a training-free method that uses the base model's distribution of possible outcomes to adaptively guide generation toward better text alignment. During denoising, TrailMix generates inexpensive lookahead images from parallel trajectories (trails) and scores their alignment with the prompt using an external judge. The resulting distribution of reward scores allows us to estimate how strongly to steer generation toward a desired alignment level. We use these estimates to reweight and resample trajectories, favoring more promising outcomes. Across three text-to-image benchmarks, TrailMix outperforms existing baselines, with particularly strong gains on rare multi-object compositions. We further extend TrailMix to targeted image editing and introduce SEAM-Bench (Semantic Editing and Attribute Maintenance), a systematic benchmark evaluating whether semantic edits preserve other image content. Experiments on SEAM-Bench and existing benchmark PIE-Bench demonstrate the effectiveness of our approach for controlled image editing. Our results show how a model's own possible outcomes can inform reliable and controllable generation.

### 🤖 AI 总结

**一句话总结**：Text-to-image diffusion models can generate images that satisfy complex prompts, yet often produce images that omit requested objects, attributes, or relationships. We ask if models can more reliably ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Steering, via, Adaptive, Reward, Estimation, Resampling, Text-to-image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34839v1) | [下载PDF](https://arxiv.org/pdf/2611.34839v1.pdf)

---

## [23. Beyond Feature Fusion: Sensor-Grounded Semantic-Spiking Learning for Robust Object Detection](https://arxiv.org/abs/2611.34828v1)

**作者**：Hanwen Liang, Wenxuan Liu, Wenxin Huang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-25

### 📄 论文摘要

Underexposure weakens object details, and overexposure obscures boundaries. Spike cameras encode light into high-frequency binary streams. Long-window spike counts give stable appearance cues, while short observations reveal changes in firing rates from sparse measurements. We propose SPIRE, a sensor-grounded semantic-spiking framework for illumination-robust object detection from a single spike stream. SPIRE builds an appearance view from the full packet through detection-oriented illumination adaptation and constructs a sequence of cumulative views from progressively longer prefixes. Each prefix supplies a rate map, an edge map, and a rate difference that tracks changes as spikes accumulate. At selected scales, ANN features and spike-derived initialization jointly set the initial membrane potentials and firing thresholds, allowing semantic cues to shape the responses during temporal encoding. Local spike-count contrasts supervise both branches during training. The residual between measured and ANN-predicted contrasts combines with the spiking features to produce a bounded correction to the fused feature pyramid. On simulated VOC and COCO, SPIRE-D outperforms the strongest baseline by 4.00-5.50 AP50 points across the four under- and overexposure settings. On real PKU-Vidar-DVS recordings, it achieves 67.07 AP50 and 40.10 AP75. SPIRE-D also uses 50.4% fewer MACs than SPFD.

### 🤖 AI 总结

**一句话总结**：Underexposure weakens object details, and overexposure obscures boundaries. Spike cameras encode light into high-frequency binary streams. Long-window spike counts give stable appearance cues, while s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Feature, Fusion, Sensor-Grounded, Semantic-Spiking, Learning, Robust, Object

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34828v1) | [下载PDF](https://arxiv.org/pdf/2611.34828v1.pdf)

---

## cs.LG

## [24. Can image generation help visual reasoning? An empirical study](https://arxiv.org/abs/2611.34935v1)

**作者**：Xueyang Yu, Yifan Jing, Taiming Lu 等 8 位作者  
**分类**：cs.LG, cs.CL, cs.CV  
**发布时间**：2026-11-25

### 📄 论文摘要

Language models think in words; then multimodal models might think in images. We test whether a generated helper improves the answer to a visual question. A model describes the helper it needs and then answers using the original and generated images together. Across 13 vision-language model and generator pairs, generation lowers mean accuracy by 3.7 percentage points, with declines on nine of ten tasks. Two unified models, BAGEL and Janus-Pro-7B, each lose accuracy on eight tasks. On VSTAR, adding a generated image to the same planning hint lowers accuracy by 10.47 points. Repeated image edits yield different outcomes across tasks. ChartQAPro and MathVista stay below their no-generation baselines, while ERQA gains three points after ten edits.

### 🤖 AI 总结

**一句话总结**：Language models think in words; then multimodal models might think in images. We test whether a generated helper improves the answer to a visual question. A model describes the helper it needs and the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Can, image, generation, help, visual, reasoning?, empirical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34935v1) | [下载PDF](https://arxiv.org/pdf/2611.34935v1.pdf)

---

## [25. Attack Policy Selection can Mislead Monitor Evaluators](https://arxiv.org/abs/2611.34934v1)

**作者**：Charlie Griffin, Oliver Makins, Asa Cooper Stickland 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-25

### 📄 论文摘要

AI monitors, classifiers that flag dangerous behaviour by AI agents, are often evaluated against transcripts generated by attack policies acting as proxies for dangerous behaviour in deployment. We evaluate an ex-production OpenAI monitor as a case study and find that measured false negative rate is highly sensitive to both the method used to generate attack policies and the level of optimisation applied within that method. This rate ranged from 0.5\% to 20.8\% across optimisation levels of a single method (reinforcement learning), and from 6.4\% to 23.0\% across methods at their best observed optimisation level (optimised prompting vs.\ transcript editing). Every attack policy was developed against proxy monitors only: all reported results show attacks transferring to the held-out GPT-5.4 target monitor. Our results suggest that monitor evasion evaluations can easily mislead: an evaluation using only basic attack methods may give false confidence that a monitor is strong.   The sensitivity to attack-policy choice raises a problem: interpreting any particular result as evidence about deployment performance requires justification. The transcripts produced by attack policies are proxies for the dangerous behaviour a monitor must flag in deployment. These proxies can introduce visible artefacts, such as reasoning about a ``side task'' absent from the instructions shown to the monitor, that affect monitor judgements. Given the sensitivity above, the choice of proxy can change an evaluation's conclusion. Reading these results as evidence about deployment therefore requires a separate legitimacy argument for why the proxies are informative, including any justification of conservativeness. Making convincing arguments remains an open problem.

### 🤖 AI 总结

**一句话总结**：AI monitors, classifiers that flag dangerous behaviour by AI agents, are often evaluated against transcripts generated by attack policies acting as proxies for dangerous behaviour in deployment. We ev...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Attack, Policy, Selection, can, Mislead, Monitor, Evaluators, monitors

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34934v1) | [下载PDF](https://arxiv.org/pdf/2611.34934v1.pdf)

---

## [26. A gene informed benchmark for BioScoring of pathology foundation models](https://arxiv.org/abs/2611.34930v1)

**作者**：Paul Vilars, Vincent Quoc-Huy Trinh, Maria Vakalopoulou 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-25

### 📄 论文摘要

Pathology foundation models are usually compared by their performance on downstream tasks such as classification and retrieval. While such benchmarks measure how useful a model is, they provide no insight into the biology it represents. We introduce BioScore, a benchmark that quantifies how well an image encoder captures cell identities, with spatial transcriptomics of the same tissue as the reference. A sparse autoencoder splits the encoder's patch embeddings into sparse features, which we cluster into a fixed number of groups. BioScore then measures, for each of 52 cell identities defined by marker genes, how specifically one group follows the identity's expression over the tissue. Because the autoencoder training is fully unsupervised, a match shows that the model represents the cell identity from the image alone. We score 8 pathology foundation models and 3 natural-image models. Every pathology model scores above every natural-image model (0.299--0.371 \vs 0.214--0.232), and paired tests separate three tiers among the pathology models. Unlike a supervised probe, BioScore needs no labels, builds its reference from the data and scores even from few sections, yet it ranks the encoders as a probe does. Its per-identity breakdown indicates which cell identities each encoder captures or misses.

### 🤖 AI 总结

**一句话总结**：Pathology foundation models are usually compared by their performance on downstream tasks such as classification and retrieval. While such benchmarks measure how useful a model is, they provide no ins...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, gene, informed, benchmark, BioScoring, pathology, foundation, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34930v1) | [下载PDF](https://arxiv.org/pdf/2611.34930v1.pdf)

---

## [27. Interpretable and Accurate Hybrid Decision Trees with Selective Case-Based Splits](https://arxiv.org/abs/2611.34887v1)

**作者**：Cristiano Landi, Alessio Cascione, Riccardo Guidotti  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-25

### 📄 论文摘要

Decision trees are among the most well-known interpretable models in Machine Learning. Over the years, a wide variety of strategies have been proposed to define split conditions within the greedy learning framework, aiming to guide instance routing and enhance predictive performance. These strategies range from axis-parallel and oblique splits based on feature values to proximity-based splits using exemplar instances and more complex hybrid approaches. However, no single method has emerged as universally superior. In this work, we present two key contributions to the construction of greedy decision trees. First, we propose a hybrid tree architecture that integrates both feature-based and case-based splits, allowing for heterogeneous splits throughout the tree. Second, we introduce a novel type of split that leverages a selective case-based approach: when a split is needed, our method searches for the most informative subset of features to define the split, effectively balancing the specificity of case-based methods with the simplicity of feature-based ones. Experiments on a diverse set of tabular datasets show that our method outperforms standard decision trees and achieves performance on par with ensemble methods, while producing shallow trees that retain or even improve predictive accuracy.

### 🤖 AI 总结

**一句话总结**：Decision trees are among the most well-known interpretable models in Machine Learning. Over the years, a wide variety of strategies have been proposed to define split conditions within the greedy lear...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Interpretable, Accurate, Hybrid, Decision, Trees, Selective, Case-Based, Splits

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34887v1) | [下载PDF](https://arxiv.org/pdf/2611.34887v1.pdf)

---

## [28. Put the World Back: Timestamps Matter in Time Series Reasoning](https://arxiv.org/abs/2611.34848v1)

**作者**：Tingrui Huang, Yuanyuan Deng, Qingren Yao 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-25

### 📄 论文摘要

Large language models (LLMs) are increasingly applied to time series reasoning. However, current evaluations often give models events in chronological order and already matched to the time series. This makes it unclear whether models use timestamps to connect events with observations or simply take shortcuts. To expose this ambiguity, we reformulate time series reasoning from a world-to-series projection perspective, viewing timestamps as explicit indices that connect numerical observations and external events to shared world states. We identify three structures that timestamps can make explicit: temporal causal structure, time semantics, and event-series alignment. Building on this perspective, we develop a diagnostic protocol that distinguishes timestamp-grounded reasoning from correlational shortcuts, a distinction that accuracy-based benchmarks cannot make. Controlled interventions on 310 questions from two tasks show that high accuracy can persist when timestamps are replaced by relative offsets or removed, while breaking event-series alignment induces systematic failures. When context is pre-aligned, models barely need timestamps. When order is missing, they use dates to recall world knowledge. Without dates, they rely on correlational shortcuts and rarely notice incorrect timestamps. These findings show that high accuracy on pre-aligned, ordered inputs does not establish that a model uses timestamps to synchronize observations with the world. We release our code, model outputs, and trajectory labels at https://github.com/tingrui-huang/timestamps-matter.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly applied to time series reasoning. However, current evaluations often give models events in chronological order and already matched to the time series. Thi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Put, World, Back, Timestamps, Matter, Time, Series, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34848v1) | [下载PDF](https://arxiv.org/pdf/2611.34848v1.pdf)

---

## [29. Provably Efficient Offline Discounted Reinforcement Learning under Recursive Entropic Risk](https://arxiv.org/abs/2611.34840v1)

**作者**：Amirparsa Bahrami, Oliver Mortensen, Mohammad Sadegh Talebi  
**分类**：cs.LG, eess.SY, stat.ML  
**发布时间**：2026-11-25

### 📄 论文摘要

We study risk-sensitive reinforcement learning in finite discounted infinite-horizon Markov Decision Processes with recursive entropic risk measures (ERM), parameterized by $β\neq 0$. We consider both risk-averse ($β>0$) and risk-seeking ($β<0$) settings. We consider the offline RL setting, where the agent is provided with a fixed dataset and wishes to learn a near-optimal policy using this dataset. We introduce a model-based algorithm, called ERM Value Iteration Lower Confidence Bound (ERM-VI-LCB) and derive a PAC-type bound on its sample complexity. We also establish a corresponding lower bound, demonstrating that exponential dependence on $|β|/(1-γ)$ asserted by the upper bound is unavoidable in the worst case. The presented bounds provide the first rigorous sample complexity guarantees for offline RL under recursive ERM across both risk-averse and risk-seeking regimes.

### 🤖 AI 总结

**一句话总结**：We study risk-sensitive reinforcement learning in finite discounted infinite-horizon Markov Decision Processes with recursive entropic risk measures (ERM), parameterized by $β\neq 0$. We consider both...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Provably, Efficient, Offline, Discounted, Reinforcement, Learning, under, Recursive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34840v1) | [下载PDF](https://arxiv.org/pdf/2611.34840v1.pdf)

---

## [30. Not all world models can doubt: how training objective and architecture shape epistemic uncertainty in JEPA and RSSM world models](https://arxiv.org/abs/2611.34830v1)

**作者**：Simon Baur, Wojciech Samek, Jackie Ma  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-25

### 📄 论文摘要

World models predict how an environment responds to actions, so that candidate actions can be evaluated before execution. Executed actions, or decisions, taken in this manner are only as reliable as the model's predictive capabilities, and predictions in turn are only reliable within the model's experience. Epistemic uncertainty (EU) is the signal that marks where that experience ends. In this work we offer an extensive empirical study on how training objectives and architectures shape epistemic uncertainty of world models. More precisely, we present a controlled comparison of post-hoc EU (last-layer Laplace and ensembles) between two dominant models of different paradigms: 1) LeWorldModel (LeWM): A joint-embedding predictive architecture (JEPA), which predicts the next embedding without a decoder, and 2) DreamerV3: A recurrent state-space model (RSSM), which reconstructs the observation from a recurrent latent state. In ten simulated visual-control environments, we follow a controlled state perturbation of the environment state through every stage of the models up to the final EU estimate. We find that the RSSM attenuates the state perturbation through two mechanisms before it reaches an estimator on the predictor feature. Its recurrent update averages over context, so a change in a single frame reaches the state at a fraction of its size and recovers only as the change persists. Its reconstruction objective weights an entity by the pixels it covers, so a small object can be lost due to the training objective. The JEPA has neither mechanism and passes the change through all stages to the uncertainty. We further show that this translates to gaps in five uncertainty related downstream tasks, from unfamiliar-state detection to uncertainty-penalised planning: the RSSM uncertainty misses deviations that its own posterior registers, whereas the JEPA uncertainty reports what its model sees.

### 🤖 AI 总结

**一句话总结**：World models predict how an environment responds to actions, so that candidate actions can be evaluated before execution. Executed actions, or decisions, taken in this manner are only as reliable as t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Not, all, world, models, can, doubt, how, training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.34830v1) | [下载PDF](https://arxiv.org/pdf/2611.34830v1.pdf)

---

