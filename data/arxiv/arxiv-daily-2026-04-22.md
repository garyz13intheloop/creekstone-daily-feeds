# arXiv AI 论文日报 | 2026-04-22

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (13 篇)
- [cs.LG](#csLG) (11 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (1 篇)

---

## cs.AI

## [1. A-MAR: Agent-based Multimodal Art Retrieval for Fine-Grained Artwork Understanding](https://arxiv.org/abs/2604.19689v1)

**作者**：Shuai Wang, Hongyi Zhu, Jia-Hong Huang 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-21

### 📄 论文摘要

Understanding artworks requires multi-step reasoning over visual content and cultural, historical, and stylistic context. While recent multimodal large language models show promise in artwork explanation, they rely on implicit reasoning and internalized knowl- edge, limiting interpretability and explicit evidence grounding. We propose A-MAR, an Agent-based Multimodal Art Retrieval framework that explicitly conditions retrieval on structured reasoning plans. Given an artwork and a user query, A-MAR first decomposes the task into a structured reasoning plan that specifies the goals and evidence requirements for each step. Retrieval is then conditionedon this plan, enabling targeted evidence selection and supporting step-wise, grounded explanations. To evaluate agent-based multi- modal reasoning within the art domain, we introduce ArtCoT-QA. This diagnostic benchmark features multi-step reasoning chains for diverse art-related queries, enabling a granular analysis that extends beyond simple final answer accuracy. Experiments on SemArt and Artpedia show that A-MAR consistently outperforms static, non planned retrieval and strong MLLM baselines in final explanation quality, while evaluations on ArtCoT-QA further demonstrate its advantages in evidence grounding and multi-step reasoning ability. These results highlight the importance of reasoning-conditioned retrieval for knowledge-intensive multimodal understanding and position A-MAR as a step toward interpretable, goal-driven AI systems, with particular relevance to cultural industries. The code and data are available at: https://github.com/ShuaiWang97/A-MAR.

### 🤖 AI 总结

**一句话总结**：Understanding artworks requires multi-step reasoning over visual content and cultural, historical, and stylistic context. While recent multimodal large language models show promise in artwork explanat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：A-MAR, Agent-based, Multimodal, Art, Retrieval, Fine-Grained, Artwork, Understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19689v1) | [下载PDF](https://arxiv.org/pdf/2604.19689v1.pdf)

---

## cs.CL

## [2. Discovering a Shared Logical Subspace: Steering LLM Logical Reasoning via Alignment of Natural-Language and Symbolic Views](https://arxiv.org/abs/2604.19716v1)

**作者**：Feihao Fang, My T. Thai, Yuanyuan Lei  
**分类**：cs.CL  
**发布时间**：2026-04-21

### 📄 论文摘要

Large Language Models (LLMs) still struggle with multi-step logical reasoning. Existing approaches either purely refine the reasoning chain in natural language form or attach a symbolic solver as an external module. In this work, we instead ask whether LLMs contain a shared internal logical subspace that simultaneously aligns natural-language and symbolic-language views of the reasoning process. Our hypothesis is that this logical subspace captures logical reasoning capabilities in LLMs that are shared across views while remaining independent of surface forms. To verify this, we employ Canonical Correlation Analysis on the paired residual activations from natural-language and symbolic-language reasoning chains, learning a low-dimensional subspace with maximum cross-view correlation. Furthermore, we design a training-free approach that steers LLMs reasoning chain along this logical subspace, thereby leveraging the complementary reasoning signals from both views. Experiments on four logical reasoning benchmarks demonstrate the effectiveness of our approach, improving accuracy by up to 11 percentage points and generalizing well on out-of-domain problems.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) still struggle with multi-step logical reasoning. Existing approaches either purely refine the reasoning chain in natural language form or attach a symbolic solver as an e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Discovering, Shared, Logical, Subspace, Steering, Reasoning, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19716v1) | [下载PDF](https://arxiv.org/pdf/2604.19716v1.pdf)

---

## [3. Epistemic orientation in parliamentary discourse is associated with deliberative democracy](https://arxiv.org/abs/2604.19699v1)

**作者**：Segun Aroyehun, Stephan Lewandowsky, David Garcia  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-04-21

### 📄 论文摘要

The pursuit of truth is central to democratic deliberation and governance, yet political discourse reflects varying epistemic orientations, ranging from evidence-based reasoning grounded in verifiable information to intuition-based reasoning rooted in beliefs and subjective interpretation. We introduce a scalable approach to measure epistemic orientation using the Evidence--Minus--Intuition (EMI) score, derived from large language model (LLM) ratings and embedding-based semantic similarity. Applying this approach to 15 million parliamentary speech segments spanning 1946 to 2025 across seven countries, we examine temporal patterns in discourse and its association with deliberative democracy and governance. We find that EMI is positively associated with deliberative democracy within countries over time, with consistent relationships in both contemporaneous and lagged analyses. EMI is also positively associated with the transparency and predictable implementation of laws as a dimension of governance. These findings suggest that the epistemic nature of political discourse is crucial for both the quality of democracy and governance.

### 🤖 AI 总结

**一句话总结**：The pursuit of truth is central to democratic deliberation and governance, yet political discourse reflects varying epistemic orientations, ranging from evidence-based reasoning grounded in verifiable...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Epistemic, orientation, parliamentary, discourse, associated, deliberative, democracy, pursuit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19699v1) | [下载PDF](https://arxiv.org/pdf/2604.19699v1.pdf)

---

## [4. An Answer is just the Start: Related Insight Generation for Open-Ended Document-Grounded QA](https://arxiv.org/abs/2604.19685v1)

**作者**：Saransh Sharma, Pritika Ramu, Aparna Garimella 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-21

### 📄 论文摘要

Answering open-ended questions remains challenging for AI systems because it requires synthesis, judgment, and exploration beyond factual retrieval, and users often refine answers through multiple iterations rather than accepting a single response. Existing QA benchmarks do not explicitly support this refinement process. To address this gap, we introduce a new task, document-grounded related insight generation, where the goal is to generate additional insights from a document collection that help improve, extend, or rethink an initial answer to an open-ended question, ultimately supporting richer user interaction and a better overall question answering experience. We curate and release SCOpE-QA (Scientific Collections for Open-Ended QA), a dataset of 3,000 open-ended questions across 20 research collections. We present InsightGen, a two-stage approach that first constructs a thematic representation of the document collection using clustering, and then selects related context based on neighborhood selection from the thematic graph to generate diverse and relevant insights using LLMs. Extensive evaluation on 3,000 questions using two generation models and two evaluation settings shows that InsightGen consistently produces useful, relevant, and actionable insights, establishing a strong baseline for this new task.

### 🤖 AI 总结

**一句话总结**：Answering open-ended questions remains challenging for AI systems because it requires synthesis, judgment, and exploration beyond factual retrieval, and users often refine answers through multiple ite...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Answer, just, Start, Related, Insight, Generation, Open-Ended

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19685v1) | [下载PDF](https://arxiv.org/pdf/2604.19685v1.pdf)

---

## [5. Chat2Workflow: A Benchmark for Generating Executable Visual Workflows with Natural Language](https://arxiv.org/abs/2604.19667v1)

**作者**：Yi Zhong, Buqiang Xu, Yijun Wang 等 7 位作者  
**分类**：cs.CL, cs.AI, cs.CV, cs.LG, cs.MA  
**发布时间**：2026-04-21

### 📄 论文摘要

At present, executable visual workflows have emerged as a mainstream paradigm in real-world industrial deployments, offering strong reliability and controllability. However, in current practice, such workflows are almost entirely constructed through manual engineering: developers must carefully design workflows, write prompts for each step, and repeatedly revise the logic as requirements evolve-making development costly, time-consuming, and error-prone. To study whether large language models can automate this multi-round interaction process, we introduce Chat2Workflow, a benchmark for generating executable visual workflows directly from natural language, and propose a robust agentic framework to mitigate recurrent execution errors. Chat2Workflow is built from a large collection of real-world business workflows, with each instance designed so that the generated workflow can be transformed and directly deployed to practical workflow platforms such as Dify and Coze. Experimental results show that while state-of-the-art language models can often capture high-level intent, they struggle to generate correct, stable, and executable workflows, especially under complex or changing requirements. Although our agentic framework yields up to 5.34% resolve rate gains, the remaining real-world gap positions Chat2Workflow as a foundation for advancing industrial-grade automation. Code is available at https://github.com/zjunlp/Chat2Workflow.

### 🤖 AI 总结

**一句话总结**：At present, executable visual workflows have emerged as a mainstream paradigm in real-world industrial deployments, offering strong reliability and controllability. However, in current practice, such ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Chat2Workflow, Benchmark, Generating, Executable, Visual, Workflows, Natural, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19667v1) | [下载PDF](https://arxiv.org/pdf/2604.19667v1.pdf)

---

## [6. Pause or Fabricate? Training Language Models for Grounded Reasoning](https://arxiv.org/abs/2604.19656v1)

**作者**：Yiwen Qiu, Linjuan Wu, Yizhou Liu 等 12 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-21

### 📄 论文摘要

Large language models have achieved remarkable progress on complex reasoning tasks. However, they often implicitly fabricate information when inputs are incomplete, producing confident but unreliable conclusions -- a failure mode we term ungrounded reasoning. We argue that this issue arises not from insufficient reasoning capability, but from the lack of inferential boundary awareness -- the ability to recognize when the necessary premises for valid inference are missing. To address this issue, we propose Grounded Reasoning via Interactive Reinforcement Learning (GRIL), a multi-turn reinforcement learning framework for grounded reasoning under incomplete information. GRIL decomposes the reasoning process into two stages: clarify and pause, which identifies whether the available information is sufficient, and grounded reasoning, which performs task solving once the necessary premises are established. We design stage-specific rewards to penalize hallucinations, enabling models to detect gaps, stop proactively, and resume reasoning after clarification. Experiments on GSM8K-Insufficient and MetaMATH-Insufficient show that GRIL significantly improves premise detection (up to 45%), leading to a 30% increase in task success while reducing average response length by over 20%. Additional analyses confirm robustness to noisy user responses and generalization to out-of-distribution tasks.

### 🤖 AI 总结

**一句话总结**：Large language models have achieved remarkable progress on complex reasoning tasks. However, they often implicitly fabricate information when inputs are incomplete, producing confident but unreliable ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：or, Pause, Fabricate?, Training, Language, Models, Grounded, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19656v1) | [下载PDF](https://arxiv.org/pdf/2604.19656v1.pdf)

---

## cs.CV

## [7. Tstars-Tryon 1.0: Robust and Realistic Virtual Try-On for Diverse Fashion Items](https://arxiv.org/abs/2604.19748v1)

**作者**：Mengting Chen, Zhengrui Chen, Yongchao Du 等 19 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-21

### 📄 论文摘要

Recent advances in image generation and editing have opened new opportunities for virtual try-on. However, existing methods still struggle to meet complex real-world demands. We present Tstars-Tryon 1.0, a commercial-scale virtual try-on system that is robust, realistic, versatile, and highly efficient. First, our system maintains a high success rate across challenging cases like extreme poses, severe illumination variations, motion blur, and other in-the-wild conditions. Second, it delivers highly photorealistic results with fine-grained details, faithfully preserving garment texture, material properties, and structural characteristics, while largely avoiding common AI-generated artifacts. Third, beyond apparel try-on, our model supports flexible multi-image composition (up to 6 reference images) across 8 fashion categories, with coordinated control over person identity and background. Fourth, to overcome the latency bottlenecks of commercial deployment, our system is heavily optimized for inference speed, delivering near real-time generation for a seamless user experience. These capabilities are enabled by an integrated system design spanning end-to-end model architecture, a scalable data engine, robust infrastructure, and a multi-stage training paradigm. Extensive evaluation and large-scale product deployment demonstrate that Tstars-Tryon1.0 achieves leading overall performance. To support future research, we also release a comprehensive benchmark. The model has been deployed at an industrial scale on the Taobao App, serving millions of users with tens of millions of requests.

### 🤖 AI 总结

**一句话总结**：Recent advances in image generation and editing have opened new opportunities for virtual try-on. However, existing methods still struggle to meet complex real-world demands. We present Tstars-Tryon 1...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Tstars-Tryon, Robust, Realistic, Virtual, Try-On, Diverse, Fashion, Items

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19748v1) | [下载PDF](https://arxiv.org/pdf/2604.19748v1.pdf)

---

## [8. AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model](https://arxiv.org/abs/2604.19747v1)

**作者**：Yutian Chen, Shi Guo, Renbiao Jin 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-21

### 📄 论文摘要

Sparse-view 3D reconstruction is essential for modeling scenes from casual captures, but remain challenging for non-generative reconstruction. Existing diffusion-based approaches mitigates this issues by synthesizing novel views, but they often condition on only one or two capture frames, which restricts geometric consistency and limits scalability to large or diverse scenes. We propose AnyRecon, a scalable framework for reconstruction from arbitrary and unordered sparse inputs that preserves explicit geometric control while supporting flexible conditioning cardinality. To support long-range conditioning, our method constructs a persistent global scene memory via a prepended capture view cache, and removes temporal compression to maintain frame-level correspondence under large viewpoint changes. Beyond better generative model, we also find that the interplay between generation and reconstruction is crucial for large-scale 3D scenes. Thus, we introduce a geometry-aware conditioning strategy that couples generation and reconstruction through an explicit 3D geometric memory and geometry-driven capture-view retrieval. To ensure efficiency, we combine 4-step diffusion distillation with context-window sparse attention to reduce quadratic complexity. Extensive experiments demonstrate robust and scalable reconstruction across irregular inputs, large viewpoint gaps, and long trajectories.

### 🤖 AI 总结

**一句话总结**：Sparse-view 3D reconstruction is essential for modeling scenes from casual captures, but remain challenging for non-generative reconstruction. Existing diffusion-based approaches mitigates this issues...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Diffusion, AnyRecon, Arbitrary-View, Reconstruction, Video, Model, Sparse-view

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19747v1) | [下载PDF](https://arxiv.org/pdf/2604.19747v1.pdf)

---

## [9. CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)

**作者**：Gene Chou, Charles Herrmann, Kyle Genova 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-21

### 📄 论文摘要

We address the problem of generating a 3D-consistent, navigable environment that is spatially grounded: a simulation of a real location. Existing video generative models can produce a plausible sequence that is consistent with a text (T2V) or image (I2V) prompt. However, the capability to reconstruct the real world under arbitrary weather conditions and dynamic object configurations is essential for downstream applications including autonomous driving and robotics simulation. To this end, we present CityRAG, a video generative model that leverages large corpora of geo-registered data as context to ground generation to the physical scene, while maintaining learned priors for complex motion and appearance changes. CityRAG relies on temporally unaligned training data, which teaches the model to semantically disentangle the underlying scene from its transient attributes. Our experiments demonstrate that CityRAG can generate coherent minutes-long, physically grounded video sequences, maintain weather and lighting conditions over thousands of frames, achieve loop closure, and navigate complex trajectories to reconstruct real-world geography.

### 🤖 AI 总结

**一句话总结**：We address the problem of generating a 3D-consistent, navigable environment that is spatially grounded: a simulation of a real location. Existing video generative models can produce a plausible sequen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, CityRAG, Stepping, City, via, Spatially-Grounded, Video, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19741v1) | [下载PDF](https://arxiv.org/pdf/2604.19741v1.pdf)

---

## [10. Generative Drifting for Conditional Medical Image Generation](https://arxiv.org/abs/2604.19736v1)

**作者**：Zirong Li, Siyuan Mei, Weiwen Wu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-21

### 📄 论文摘要

Conditional medical image generation plays an important role in many clinically relevant imaging tasks. However, existing methods still face a fundamental challenge in balancing inference efficiency, patient-specific fidelity, and distribution-level plausibility, particularly in high-dimensional 3D medical imaging. In this work, we propose GDM, a generative drifting framework that reformulates deterministic medical image prediction as a multi-objective learning problem to jointly promote distribution-level plausibility and patient-specific fidelity while retaining one-step inference. GDM extends drifting to 3D medical imaging through an attractive-repulsive drift that minimizes the discrepancy between the generator pushforward and the target distribution. To enable stable drifting-based learning in 3D volumetric data, GDM constructs a multi-level feature bank from a medical foundation encoder to support reliable affinity estimation and drifting field computation across complementary global, local, and spatial representations. In addition, a gradient coordination strategy in the shared output space improves optimization balance under competing distribution-level and fidelity-oriented objectives. We evaluate the proposed framework on two representative tasks, MRI-to-CT synthesis and sparse-view CT reconstruction. Experimental results show that GDM consistently outperforms a wide range of baselines, including GAN-based, flow-matching-based, and SDE-based generative models, as well as supervised regression methods, while improving the balance among anatomical fidelity, quantitative reliability, perceptual realism, and inference efficiency. These findings suggest that GDM provides a practical and effective framework for conditional 3D medical image generation.

### 🤖 AI 总结

**一句话总结**：Conditional medical image generation plays an important role in many clinically relevant imaging tasks. However, existing methods still face a fundamental challenge in balancing inference efficiency, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Generative, Drifting, Conditional, Medical, Image, Generation, plays

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19736v1) | [下载PDF](https://arxiv.org/pdf/2604.19736v1.pdf)

---

## [11. ReImagine: Rethinking Controllable High-Quality Human Video Generation via Image-First Synthesis](https://arxiv.org/abs/2604.19720v1)

**作者**：Zhengwentai Sun, Keru Zheng, Chenghong Li 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-21

### 📄 论文摘要

Human video generation remains challenging due to the difficulty of jointly modeling human appearance, motion, and camera viewpoint under limited multi-view data. Existing methods often address these factors separately, resulting in limited controllability or reduced visual quality. We revisit this problem from an image-first perspective, where high-quality human appearance is learned via image generation and used as a prior for video synthesis, decoupling appearance modeling from temporal consistency. We propose a pose- and viewpoint-controllable pipeline that combines a pretrained image backbone with SMPL-X-based motion guidance, together with a training-free temporal refinement stage based on a pretrained video diffusion model. Our method produces high-quality, temporally consistent videos under diverse poses and viewpoints. We also release a canonical human dataset and an auxiliary model for compositional human image synthesis. Code and data are publicly available at https://github.com/Taited/ReImagine.

### 🤖 AI 总结

**一句话总结**：Human video generation remains challenging due to the difficulty of jointly modeling human appearance, motion, and camera viewpoint under limited multi-view data. Existing methods often address these ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ReImagine, Rethinking, Controllable, High-Quality, Human, Video, Generation, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19720v1) | [下载PDF](https://arxiv.org/pdf/2604.19720v1.pdf)

---

## [12. A Network-Aware Evaluation of Distributed Energy Resource Control in Smart Distribution Systems](https://arxiv.org/abs/2604.19715v1)

**作者**：Houchao Gan  
**分类**：cs.CV, eess.SY  
**发布时间**：2026-04-21

### 📄 论文摘要

Distribution networks with high penetration of Distributed Energy Resources (DERs) increasingly rely on communication networks to coordinate grid-interactive control. While many distributed control schemes have been proposed, they are often evaluated under idealized communication assumptions, making it difficult to assess their performance under realistic network conditions. This work presents an implementation-driven evaluation of a representative virtual power plant (VPP) dispatch algorithm using a co-simulation framework that couples a linearized distribution-system model with packet-level downlink emulation in ns-3. The study considers a modified IEEE~37-node feeder with high photovoltaic penetration and a primal--dual VPP dispatch that simultaneously targets feeder-head active power tracking and voltage regulation. Communication effects are introduced only on the downlink path carrying dual-variable updates, where per-DER packet delays and a hold-last-value strategy are modeled. Results show that, under ideal communication, the dispatch achieves close tracking of the feeder-head power reference while maintaining voltages within the prescribed limits at selected buses. When realistic downlink delay is introduced, the same controller exhibits large oscillations in feeder-head power and more frequent voltage limit violations. These findings highlight that distributed DER control performance can be strongly influenced by communication behavior and motivate evaluation frameworks that explicitly incorporate network dynamics into the assessment of grid-interactive control schemes.

### 🤖 AI 总结

**一句话总结**：Distribution networks with high penetration of Distributed Energy Resources (DERs) increasingly rely on communication networks to coordinate grid-interactive control. While many distributed control sc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Network-Aware, Evaluation, Distributed, Energy, Resource, Control, Smart

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19715v1) | [下载PDF](https://arxiv.org/pdf/2604.19715v1.pdf)

---

## [13. SpanVLA: Efficient Action Bridging and Learning from Negative-Recovery Samples for Vision-Language-Action Model](https://arxiv.org/abs/2604.19710v1)

**作者**：Zewei Zhou, Ruining Yang, Xuewei 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-21

### 📄 论文摘要

Vision-Language-Action (VLA) models offer a promising autonomous driving paradigm for leveraging world knowledge and reasoning capabilities, especially in long-tail scenarios. However, existing VLA models often struggle with the high latency in action generation using an autoregressive generation framework and exhibit limited robustness. In this paper, we propose SpanVLA, a novel end-to-end autonomous driving framework, integrating an autoregressive reasoning and a flow-matching action expert. First, SpanVLA introduces an efficient bridge to leverage the vision and reasoning guidance of VLM to efficiently plan future trajectories using a flow-matching policy conditioned on historical trajectory initialization, which significantly reduces inference time. Second, to further improve the performance and robustness of the SpanVLA model, we propose a GRPO-based post-training method to enable the VLA model not only to learn from positive driving samples but also to learn how to avoid the typical negative behaviors and learn recovery behaviors. We further introduce mReasoning, a new real-world driving reasoning dataset, focusing on complex, reasoning-demanding scenarios and negative-recovery samples. Extensive experiments on the NAVSIM (v1 and v2) demonstrate the competitive performance of the SpanVLA model. Additionally, the qualitative results across diverse scenarios highlight the planning performance and robustness of our model.

### 🤖 AI 总结

**一句话总结**：Vision-Language-Action (VLA) models offer a promising autonomous driving paradigm for leveraging world knowledge and reasoning capabilities, especially in long-tail scenarios. However, existing VLA mo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SpanVLA, Efficient, Action, Bridging, Learning, Negative-Recovery, Samples, Vision-Language-Action

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19710v1) | [下载PDF](https://arxiv.org/pdf/2604.19710v1.pdf)

---

## [14. Face Anything: 4D Face Reconstruction from Any Image Sequence](https://arxiv.org/abs/2604.19702v1)

**作者**：Umut Kocasari, Simon Giebenhain, Richard Shaw 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-21

### 📄 论文摘要

Accurate reconstruction and tracking of dynamic human faces from image sequences is challenging because non-rigid deformations, expression changes, and viewpoint variations occur simultaneously, creating significant ambiguity in geometry and correspondence estimation. We present a unified method for high-fidelity 4D facial reconstruction based on canonical facial point prediction, a representation that assigns each pixel a normalized facial coordinate in a shared canonical space. This formulation transforms dense tracking and dynamic reconstruction into a canonical reconstruction problem, enabling temporally consistent geometry and reliable correspondences within a single feed-forward model. By jointly predicting depth and canonical coordinates, our method enables accurate depth estimation, temporally stable reconstruction, dense 3D geometry, and robust facial point tracking within a single architecture. We implement this formulation using a transformer-based model that jointly predicts depth and canonical facial coordinates, trained using multi-view geometry data that non-rigidly warps into the canonical space. Extensive experiments on image and video benchmarks demonstrate state-of-the-art performance across reconstruction and tracking tasks, achieving approximately 3$\times$ lower correspondence error and faster inference than prior dynamic reconstruction methods, while improving depth accuracy by 16%. These results highlight canonical facial point prediction as an effective foundation for unified feed-forward 4D facial reconstruction.

### 🤖 AI 总结

**一句话总结**：Accurate reconstruction and tracking of dynamic human faces from image sequences is challenging because non-rigid deformations, expression changes, and viewpoint variations occur simultaneously, creat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, Face, Anything, Reconstruction, Any, Image, Sequence, Accurate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19702v1) | [下载PDF](https://arxiv.org/pdf/2604.19702v1.pdf)

---

## [15. Unveiling Fine-Grained Visual Traces: Evaluating Multimodal Interleaved Reasoning Chains in Multimodal STEM Tasks](https://arxiv.org/abs/2604.19697v1)

**作者**：Jing Jin, Hao Liu, Yan Bai 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-21

### 📄 论文摘要

Multimodal large language models (MLLMs) have shown promising reasoning abilities, yet evaluating their performance in specialized domains remains challenging. STEM reasoning is a particularly valuable testbed because it provides highly verifiable feedback, but existing benchmarks often permit unimodal shortcuts due to modality redundancy and focus mainly on final-answer accuracy, overlooking the reasoning process itself. To address this challenge, we introduce StepSTEM: a graduate-level benchmark of 283 problems across mathematics, physics, chemistry, biology, and engineering for fine-grained evaluation of cross-modal reasoning in MLLMs. StepSTEM is constructed through a rigorous curation pipeline that enforces strict complementarity between textual and visual inputs. We further propose a general step-level evaluation framework for both text-only chain-of-thought and interleaved image-text reasoning, using dynamic programming to align predicted reasoning steps with multiple reference solutions. Experiments across a wide range of models show that current MLLMs still rely heavily on textual reasoning, with even Gemini 3.1 Pro and Claude Opus 4.6 achieving only 38.29% accuracy. These results highlight substantial headroom for genuine cross-modal STEM reasoning and position StepSTEM as a benchmark for fine-grained evaluation of multimodal reasoning. Source code is available at https://github.com/lll-hhh/STEPSTEM.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) have shown promising reasoning abilities, yet evaluating their performance in specialized domains remains challenging. STEM reasoning is a particularly valuabl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unveiling, Fine-Grained, Visual, Traces, Evaluating, Multimodal, Interleaved, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19697v1) | [下载PDF](https://arxiv.org/pdf/2604.19697v1.pdf)

---

## [16. IR-Flow: Bridging Discriminative and Generative Image Restoration via Rectified Flow](https://arxiv.org/abs/2604.19680v1)

**作者**：Zihao Fan, Xin Lu, Jie Xiao 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-21

### 📄 论文摘要

In image restoration, single-step discriminative mappings often lack fine details via expectation learning, whereas generative paradigms suffer from inefficient multi-step sampling and noise-residual coupling. To address this dilemma, we propose IR-Flow, a novel image restoration method based on Rectified Flow that serves as a unified framework bridging the gap between discriminative and generative paradigms. Specifically, we first construct multilevel data distribution flows, which expand the ability of models to learn from and adapt to various levels of degradation. Subsequently, cumulative velocity fields are proposed to learn transport trajectories across varying degradation levels, guiding intermediate states toward the clean target, while a multi-step consistency constraint is presented to enforce trajectory coherence and boost few-step restoration performance. We show that directly establishing a linear transport flow between degraded and clean image domains not only enables fast inference but also improves adaptability to out-of-distribution degradations. Extensive evaluations on deraining, denoising and raindrop removal tasks demonstrate that IR-Flow achieves competitive quantitative results with only a few sampling steps, offering an efficient and flexible framework that maintains an excellent distortion-perception balance. Our code is available at https://github.com/fanzh03/IR-Flow.

### 🤖 AI 总结

**一句话总结**：In image restoration, single-step discriminative mappings often lack fine details via expectation learning, whereas generative paradigms suffer from inefficient multi-step sampling and noise-residual ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IR-Flow, Bridging, Discriminative, Generative, Image, Restoration, via, Rectified

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19680v1) | [下载PDF](https://arxiv.org/pdf/2604.19680v1.pdf)

---

## [17. MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation](https://arxiv.org/abs/2604.19679v1)

**作者**：Liyang Li, Wen Wang, Canyu Zhao 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-21

### 📄 论文摘要

Recent advances in Diffusion Transformers (DiTs) have enabled high-quality joint audio-video generation, producing videos with synchronized audio within a single model. However, existing controllable generation frameworks are typically restricted to video-only control. This restricts comprehensive controllability and often leads to suboptimal cross-modal alignment. To bridge this gap, we present MMControl, which enables users to perform Multi-Modal Control in joint audio-video generation. MMControl introduces a dual-stream conditional injection mechanism. It incorporates both visual and acoustic control signals, including reference images, reference audio, depth maps, and pose sequences, into a joint generation process. These conditions are injected through bypass branches into a joint audio-video Diffusion Transformer, enabling the model to simultaneously generate identity-consistent video and timbre-consistent audio under structural constraints. Furthermore, we introduce modality-specific guidance scaling, which allows users to independently and dynamically adjust the influence strength of each visual and acoustic condition at inference time. Extensive experiments demonstrate that MMControl achieves fine-grained, composable control over character identity, voice timbre, body pose, and scene layout in joint audio-video generation.

### 🤖 AI 总结

**一句话总结**：Recent advances in Diffusion Transformers (DiTs) have enabled high-quality joint audio-video generation, producing videos with synchronized audio within a single model. However, existing controllable ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MMControl, Unified, Multi-Modal, Control, Joint, Audio-Video, Generation, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19679v1) | [下载PDF](https://arxiv.org/pdf/2604.19679v1.pdf)

---

## [18. MedFlowSeg: Flow Matching for Medical Image Segmentation with Frequency-Aware Attention](https://arxiv.org/abs/2604.19675v1)

**作者**：Zhi Chen, Runze Hu, Le Zhang  
**分类**：cs.CV  
**发布时间**：2026-04-21

### 📄 论文摘要

Flow matching has recently emerged as a principled framework for learning continuous-time transport maps, enabling efficient deterministic generation without relying on stochastic diffusion processes. While generative modeling has shown promise for medical image segmentation, particularly in capturing uncertainty and complex anatomical variability, existing approaches are predominantly built upon diffusion models, which incur substantial computational overhead due to iterative sampling and are often constrained by UNet-based parameterizations. In this work, we introduce MedFlowSeg, a conditional flow matching framework that formulates medical image segmentation as learning a time-dependent vector field that transports a simple prior distribution to the target segmentation distribution. This formulation enables one-step deterministic inference while preserving the expressiveness of generative modeling. We further develop a dual-conditioning mechanism to incorporate structured priors into the learned flow. Specifically, we propose a Dual-Branch Spatial Attention module that injects multi-scale structural information into the flow field, and a Frequency-Aware Attention module that models cross-domain interactions between spatial and spectral representations via discrepancy-aware fusion and time-dependent modulation. Together, these components provide an effective parameterization of conditional flows that capture both global anatomical structure and fine-grained boundary details. We provide extensive empirical validation across multiple medical imaging modalities, demonstrating that MedFlowSeg achieves state-of-the-art performance while significantly reducing computational cost compared to diffusion-based methods. Our results highlight the potential of flow matching as a theoretically grounded and computationally efficient alternative for generative medical image segmentation.

### 🤖 AI 总结

**一句话总结**：Flow matching has recently emerged as a principled framework for learning continuous-time transport maps, enabling efficient deterministic generation without relying on stochastic diffusion processes....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MedFlowSeg, Flow, Matching, Medical, Image, Segmentation, Frequency-Aware, Attention

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19675v1) | [下载PDF](https://arxiv.org/pdf/2604.19675v1.pdf)

---

## [19. InHabit: Leveraging Image Foundation Models for Scalable 3D Human Placement](https://arxiv.org/abs/2604.19673v1)

**作者**：Nikita Kister, Pradyumna YM, István Sárándi 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-21

### 📄 论文摘要

Training embodied agents to understand 3D scenes as humans do requires large-scale data of people meaningfully interacting with diverse environments, yet such data is scarce. Real-world motion capture is costly and limited to controlled settings, while existing synthetic datasets rely on simple geometric heuristics that ignore rich scene context. In contrast, 2D foundation models trained on internet-scale data have implicitly acquired commonsense knowledge of human-environment interactions. To transfer this knowledge into 3D, we introduce InHabit, a fully automatic and scalable data generator for populating 3D scenes with interacting humans. InHabit follows a render-generate-lift principle: given a rendered 3D scene, a vision-language model proposes contextually meaningful actions, an image-editing model inserts a human, and an optimization procedure lifts the edited result into physically plausible SMPL-X bodies aligned with the scene geometry. Applied to Habitat-Matterport3D, InHabit produces the first large-scale photorealistic 3D human-scene interaction dataset, containing 78K samples across 800 building-scale scenes with complete 3D geometry, SMPL-X bodies, and RGB images. Augmenting standard training data with our samples improves RGB-based 3D human-scene reconstruction and contact estimation, and in a perceptual user study our data is preferred in 78% of cases over the state of the art.

### 🤖 AI 总结

**一句话总结**：Training embodied agents to understand 3D scenes as humans do requires large-scale data of people meaningfully interacting with diverse environments, yet such data is scarce. Real-world motion capture...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, InHabit, Leveraging, Image, Foundation, Models, Scalable, Human

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19673v1) | [下载PDF](https://arxiv.org/pdf/2604.19673v1.pdf)

---

## cs.LG

## [20. Generalization at the Edge of Stability](https://arxiv.org/abs/2604.19740v1)

**作者**：Mario Tuci, Caner Korkmaz, Umut Şimşekli 等 4 位作者  
**分类**：cs.LG, cs.AI, cs.CV, stat.ML  
**发布时间**：2026-04-21

### 📄 论文摘要

Training modern neural networks often relies on large learning rates, operating at the edge of stability, where the optimization dynamics exhibit oscillatory and chaotic behavior. Empirically, this regime often yields improved generalization performance, yet the underlying mechanism remains poorly understood. In this work, we represent stochastic optimizers as random dynamical systems, which often converge to a fractal attractor set (rather than a point) with a smaller intrinsic dimension. Building on this connection and inspired by Lyapunov dimension theory, we introduce a novel notion of dimension, coined the `sharpness dimension', and prove a generalization bound based on this dimension. Our results show that generalization in the chaotic regime depends on the complete Hessian spectrum and the structure of its partial determinants, highlighting a complexity that cannot be captured by the trace or spectral norm considered in prior work. Experiments across various MLPs and transformers validate our theory while also providing new insights into the recently observed phenomenon of grokking.

### 🤖 AI 总结

**一句话总结**：Training modern neural networks often relies on large learning rates, operating at the edge of stability, where the optimization dynamics exhibit oscillatory and chaotic behavior. Empirically, this re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, of, Generalization, Edge, Stability, Training, modern, neural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19740v1) | [下载PDF](https://arxiv.org/pdf/2604.19740v1.pdf)

---

## [21. Safe Continual Reinforcement Learning in Non-stationary Environments](https://arxiv.org/abs/2604.19737v1)

**作者**：Austin Coursey, Abel Diaz-Gonzalez, Marcos Quinones-Grueiro 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-21

### 📄 论文摘要

Reinforcement learning (RL) offers a compelling data-driven paradigm for synthesizing controllers for complex systems when accurate physical models are unavailable; however, most existing control-oriented RL methods assume stationarity and, therefore, struggle in real-world non-stationary deployments where system dynamics and operating conditions can change unexpectedly. Moreover, RL controllers acting in physical environments must satisfy safety constraints throughout their learning and execution phases, rendering transient violations during adaptation unacceptable. Although continual RL and safe RL have each addressed non-stationarity and safety, respectively, their intersection remains comparatively unexplored, motivating the study of safe continual RL algorithms that can adapt over the system's lifetime while preserving safety. In this work, we systematically investigate safe continual reinforcement learning by introducing three benchmark environments that capture safety-critical continual adaptation and by evaluating representative approaches from safe RL, continual RL, and their combinations. Our empirical results reveal a fundamental tension between maintaining safety constraints and preventing catastrophic forgetting under non-stationary dynamics, with existing methods generally failing to achieve both objectives simultaneously. To address this shortcoming, we examine regularization-based strategies that partially mitigate this trade-off and characterize their benefits and limitations. Finally, we outline key open challenges and research directions toward developing safe, resilient learning-based controllers capable of sustained autonomous operation in changing environments.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning (RL) offers a compelling data-driven paradigm for synthesizing controllers for complex systems when accurate physical models are unavailable; however, most existing control-orie...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Safe, Continual, Reinforcement, Learning, Non-stationary, Environments, offers

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19737v1) | [下载PDF](https://arxiv.org/pdf/2604.19737v1.pdf)

---

## [22. FASTER: Value-Guided Sampling for Fast RL](https://arxiv.org/abs/2604.19730v1)

**作者**：Perry Dong, Alexander Swerdlow, Dorsa Sadigh 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-21

### 📄 论文摘要

Some of the most performant reinforcement learning algorithms today can be prohibitively expensive as they use test-time scaling methods such as sampling multiple action candidates and selecting the best one. In this work, we propose FASTER, a method for getting the benefits of sampling-based test-time scaling of diffusion-based policies without the computational cost by tracing the performance gain of action samples back to earlier in the denoising process. Our key insight is that we can model the denoising of multiple action candidates and selecting the best one as a Markov Decision Process (MDP) where the goal is to progressively filter action candidates before denoising is complete. With this MDP, we can learn a policy and value function in the denoising space that predicts the downstream value of action candidates in the denoising process and filters them while maximizing returns. The result is a method that is lightweight and can be plugged into existing generative RL algorithms. Across challenging long-horizon manipulation tasks in online and batch-online RL, FASTER consistently improves the underlying policies and achieves the best overall performance among the compared methods. Applied to a pretrained VLA, FASTER achieves the same performance while substantially reducing training and inference compute requirements. Code is available at https://github.com/alexanderswerdlow/faster .

### 🤖 AI 总结

**一句话总结**：Some of the most performant reinforcement learning algorithms today can be prohibitively expensive as they use test-time scaling methods such as sampling multiple action candidates and selecting the b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, of, FASTER, Value-Guided, Sampling, Fast, Some, most

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19730v1) | [下载PDF](https://arxiv.org/pdf/2604.19730v1.pdf)

---

## [23. FB-NLL: A Feature-Based Approach to Tackle Noisy Labels in Personalized Federated Learning](https://arxiv.org/abs/2604.19729v1)

**作者**：Abdulmoneam Ali, Ahmed Arafa  
**分类**：cs.LG, cs.IT, eess.SP  
**发布时间**：2026-04-21

### 📄 论文摘要

Personalized Federated Learning (PFL) aims to learn multiple task-specific models rather than a single global model across heterogeneous data distributions. Existing PFL approaches typically rely on iterative optimization-such as model update trajectories-to cluster users that need to accomplish the same tasks together. However, these learning-dynamics-based methods are inherently vulnerable to low-quality data and noisy labels, as corrupted updates distort clustering decisions and degrade personalization performance. To tackle this, we propose FB-NLL, a feature-centric framework that decouples user clustering from iterative training dynamics. By exploiting the intrinsic heterogeneity of local feature spaces, FB-NLL characterizes each user through the spectral structure of the covariances of their feature representations and leverages subspace similarity to identify task-consistent user groupings. This geometry-aware clustering is label-agnostic and is performed in a one-shot manner prior to training, significantly reducing communication overhead and computational costs compared to iterative baselines.   Complementing this, we introduce a feature-consistency-based detection and correction strategy to address noisy labels within clusters. By leveraging directional alignment in the learned feature space and assigning labels based on class-specific feature subspaces, our method mitigates corrupted supervision without requiring estimation of stochastic noise transition matrices. In addition, FB-NLL is model-independent and integrates seamlessly with existing noise-robust training techniques. Extensive experiments across diverse datasets and noise regimes demonstrate that our framework consistently outperforms state-of-the-art baselines in terms of average accuracy and performance stability.

### 🤖 AI 总结

**一句话总结**：Personalized Federated Learning (PFL) aims to learn multiple task-specific models rather than a single global model across heterogeneous data distributions. Existing PFL approaches typically rely on i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FB-NLL, Feature-Based, Approach, Tackle, Noisy, Labels, Personalized, Federated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19729v1) | [下载PDF](https://arxiv.org/pdf/2604.19729v1.pdf)

---

## [24. Benign Overfitting in Adversarial Training for Vision Transformers](https://arxiv.org/abs/2604.19724v1)

**作者**：Jiaming Zhang, Meng Ding, Shaopeng Fu 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-21

### 📄 论文摘要

Despite the remarkable success of Vision Transformers (ViTs) across a wide range of vision tasks, recent studies have revealed that they remain vulnerable to adversarial examples, much like Convolutional Neural Networks (CNNs). A common empirical defense strategy is adversarial training, yet the theoretical underpinnings of its robustness in ViTs remain largely unexplored. In this work, we present the first theoretical analysis of adversarial training under simplified ViT architectures. We show that, when trained under a signal-to-noise ratio that satisfies a certain condition and within a moderate perturbation budget, adversarial training enables ViTs to achieve nearly zero robust training loss and robust generalization error under certain regimes. Remarkably, this leads to strong generalization even in the presence of overfitting, a phenomenon known as \emph{benign overfitting}, previously only observed in CNNs (with adversarial training). Experiments on both synthetic and real-world datasets further validate our theoretical findings.

### 🤖 AI 总结

**一句话总结**：Despite the remarkable success of Vision Transformers (ViTs) across a wide range of vision tasks, recent studies have revealed that they remain vulnerable to adversarial examples, much like Convolutio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Benign, Overfitting, Adversarial, Training, Vision, Transformers, Despite, remarkable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19724v1) | [下载PDF](https://arxiv.org/pdf/2604.19724v1.pdf)

---

## [25. Adaptive MSD-Splitting: Enhancing C4.5 and Random Forests for Skewed Continuous Attributes](https://arxiv.org/abs/2604.19722v1)

**作者**：Jake Lee  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-21

### 📄 论文摘要

The discretization of continuous numerical attributes remains a persistent computational bottleneck in the induction of decision trees, particularly as dataset dimensions scale. Building upon the recently proposed MSD-Splitting technique -- which bins continuous data using the empirical mean and standard deviation to dramatically improve the efficiency and accuracy of the C4.5 algorithm -- we introduce Adaptive MSD-Splitting (AMSD). While standard MSD-Splitting is highly effective for approximately symmetric distributions, its rigid adherence to fixed one-standard-deviation cutoffs can lead to catastrophic information loss in highly skewed data, a common artifact in real-world biomedical and financial datasets. AMSD addresses this by dynamically adjusting the standard deviation multiplier based on feature skewness, narrowing intervals in dense regions to preserve discriminative resolution. Furthermore, we integrate AMSD into ensemble methods, specifically presenting the Random Forest-AMSD (RF-AMSD) framework. Empirical evaluations on the Census Income, Heart Disease, Breast Cancer, and Forest Covertype datasets demonstrate that AMSD yields a 2-4% accuracy improvement over standard MSD-Splitting, while maintaining near-identical O(N) time complexity reductions compared to the O(N log N) exhaustive search. Our Random Forest extension achieves state-of-the-art accuracy at a fraction of standard computational costs, confirming the viability of adaptive statistical binning in large-scale ensemble learning architectures.

### 🤖 AI 总结

**一句话总结**：The discretization of continuous numerical attributes remains a persistent computational bottleneck in the induction of decision trees, particularly as dataset dimensions scale. Building upon the rece...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：C4.5, Adaptive, MSD-Splitting, Enhancing, Random, Forests, Skewed, Continuous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19722v1) | [下载PDF](https://arxiv.org/pdf/2604.19722v1.pdf)

---

## [26. On two ways to use determinantal point processes for Monte Carlo integration](https://arxiv.org/abs/2604.19698v1)

**作者**：Guillaume Gautier, Rémi Bardenet, Michal Valko  
**分类**：cs.LG, math.ST  
**发布时间**：2026-04-21

### 📄 论文摘要

The standard Monte Carlo estimator $\widehat{I}_N^{\mathrm{MC}}$ of $\int fdω$ relies on independent samples from $ω$ and has variance of order $1/N$. Replacing the samples with a determinantal point process (DPP), a repulsive distribution, makes the estimator consistent, with variance rates that depend on how the DPP is adapted to $f$ and $ω$. We examine two existing DPP-based estimators: one by Bardenet & Hardy (2020) with a rate of $\mathcal{O}(N^{-(1+1/d)})$ for smooth $f$, but relying on a fixed DPP. The other, by Ermakov & Zolotukhin (1960), is unbiased with rate of order $1/N$, like Monte Carlo, but its DPP is tailored to $f$. We revisit these estimators, generalize them to continuous settings, and provide sampling algorithms.

### 🤖 AI 总结

**一句话总结**：The standard Monte Carlo estimator $\widehat{I}_N^{\mathrm{MC}}$ of $\int fdω$ relies on independent samples from $ω$ and has variance of order $1/N$. Replacing the samples with a determinantal point ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：two, ways, use, determinantal, point, processes, Monte, Carlo

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19698v1) | [下载PDF](https://arxiv.org/pdf/2604.19698v1.pdf)

---

## [27. PREF-XAI: Preference-Based Personalized Rule Explanations of Black-Box Machine Learning Models](https://arxiv.org/abs/2604.19684v1)

**作者**：Salvatore Greco, Jacek Karolczak, Roman Słowiński 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-21

### 📄 论文摘要

Explainable artificial intelligence (XAI) has predominantly focused on generating model-centric explanations that approximate the behavior of black-box models. However, such explanations often overlook a fundamental aspect of interpretability: different users require different explanations depending on their goals, preferences, and cognitive constraints. Although recent work has explored user-centric and personalized explanations, most existing approaches rely on heuristic adaptations or implicit user modeling, lacking a principled framework for representing and learning individual preferences. In this paper, we consider Preference-Based Explainable Artificial Intelligence (PREF-XAI), a novel perspective that reframes explanation as a preference-driven decision problem. Within PREF-XAI, explanations are not treated as fixed outputs, but as alternatives to be evaluated and selected according to user-specific criteria. In the PREF-XAI perspective, here we propose a methodology that combines rule-based explanations with formal preference learning. User preferences are elicited through a ranking of a small set of candidate explanations and modeled via an additive utility function inferred using robust ordinal regression. Experimental results on real-world datasets show that PREF-XAI can accurately reconstruct user preferences from limited feedback, identify highly relevant explanations, and discover novel explanatory rules not initially considered by the user. Beyond the proposed methodology, this work establishes a connection between XAI and preference learning, opening new directions for interactive and adaptive explanation systems.

### 🤖 AI 总结

**一句话总结**：Explainable artificial intelligence (XAI) has predominantly focused on generating model-centric explanations that approximate the behavior of black-box models. However, such explanations often overloo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, PREF-XAI, Preference-Based, Personalized, Rule, Explanations, Black-Box, Machine

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19684v1) | [下载PDF](https://arxiv.org/pdf/2604.19684v1.pdf)

---

## [28. Budgeted Online Influence Maximization](https://arxiv.org/abs/2604.19672v1)

**作者**：Pierre Perrault, Jennifer Healey, Zheng Wen 等 4 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-04-21

### 📄 论文摘要

We introduce a new budgeted framework for online influence maximization, considering the total cost of an advertising campaign instead of the common cardinality constraint on a chosen influencer set. Our approach better models the real-world setting where the cost of influencers varies and advertisers want to find the best value for their overall social advertising budget. We propose an algorithm assuming an independent cascade diffusion model and edge level semi-bandit feedback, and provide both theoretical and experimental results. Our analysis is also valid for the cardinality constraint setting and improves the state of the art regret bound in this case.

### 🤖 AI 总结

**一句话总结**：We introduce a new budgeted framework for online influence maximization, considering the total cost of an advertising campaign instead of the common cardinality constraint on a chosen influencer set. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Budgeted, Online, Influence, Maximization, introduce, new, framework

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19672v1) | [下载PDF](https://arxiv.org/pdf/2604.19672v1.pdf)

---

## [29. HardNet++: Nonlinear Constraint Enforcement in Neural Networks](https://arxiv.org/abs/2604.19669v1)

**作者**：Andrea Goertzen, Kaveh Alim, Navid Azizan  
**分类**：cs.LG  
**发布时间**：2026-04-21

### 📄 论文摘要

Enforcing constraint satisfaction in neural network outputs is critical for safety, reliability, and physical fidelity in many control and decision-making applications. While soft-constrained methods penalize constraint violations during training, they do not guarantee constraint adherence during inference. Other approaches guarantee constraint satisfaction via specific parameterizations or a projection layer, but are tailored to specific forms (e.g., linear constraints), limiting their utility in other general problem settings. Many real-world problems of interest are nonlinear, motivating the development of methods that can enforce general nonlinear constraints. To this end, we introduce HardNet++, a constraint-enforcement method that simultaneously satisfies linear and nonlinear equality and inequality constraints. Our approach iteratively adjusts the network output via damped local linearizations. Each iteration is differentiable, admitting an end-to-end training framework, where the constraint satisfaction layer is active during training. We show that under certain regularity conditions, this procedure can enforce nonlinear constraint satisfaction to arbitrary tolerance. Finally, we demonstrate tight constraint adherence without loss of optimality in a learning-for-optimization context, where we apply this method to a model predictive control problem with nonlinear state constraints.

### 🤖 AI 总结

**一句话总结**：Enforcing constraint satisfaction in neural network outputs is critical for safety, reliability, and physical fidelity in many control and decision-making applications. While soft-constrained methods ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HardNet++, Nonlinear, Constraint, Enforcement, Neural, Networks, Enforcing, satisfaction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19669v1) | [下载PDF](https://arxiv.org/pdf/2604.19669v1.pdf)

---

## [30. Disentangling Damage from Operational Variability: A Label-Free Self-Supervised Representation Learning Framework for Output-Only Structural Damage Identification](https://arxiv.org/abs/2604.19658v1)

**作者**：Xudong Jian, Charikleia Stoura, Simon Scandella 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-21

### 📄 论文摘要

Damage identification is a core task in structural health monitoring. In practice, however, its reliability is often compromised by confounding non-damage effects, such as variations in excitation and environmental conditions, which can induce changes comparable to or larger than those caused by structural damage. To address this challenge, this study proposes a self-supervised label-free disentangled representation learning framework for robust vibration-based structural damage identification. The proposed framework employs an autoencoder with two latent representations to learn directly from raw vibration acceleration signals. A self-supervised invariance regularization, implemented via Variance-Invariance-Covariance Regularization (VICReg), is imposed on one latent representation using baseline data where structural damage is assumed constant but operational and environmental conditions vary. In addition, a frequency-domain constraint is introduced to enforce agreement between the power spectral density reconstructed from the latent representation and that computed from the corresponding input time series. Together, these mechanisms promote disentanglement, enabling the learned representation to be sensitive to damage-related characteristics while remaining invariant to nuisance variability. The framework is trained in a fully end-to-end and label-free manner, requiring no prior information on damage, excitation, or environmental conditions, making it well-suited for real-world applications. Its effectiveness is validated on two distinct real-world vibration datasets, including a bridge and a gearbox. The results demonstrate robustness to operational variability, strong generalization capability, and good performance in both damage detection and quantification.

### 🤖 AI 总结

**一句话总结**：Damage identification is a core task in structural health monitoring. In practice, however, its reliability is often compromised by confounding non-damage effects, such as variations in excitation and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Disentangling, Damage, Operational, Variability, Label-Free, Self-Supervised, Representation, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.19658v1) | [下载PDF](https://arxiv.org/pdf/2604.19658v1.pdf)

---

