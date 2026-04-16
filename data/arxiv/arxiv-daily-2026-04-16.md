# arXiv AI 论文日报 | 2026-04-16

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (13 篇)
- [cs.LG](#csLG) (9 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration](https://arxiv.org/abs/2604.14116v1)

**作者**：Zerun Ma, Guoqiang Wang, Xinchen Xie 等 10 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-04-15

### 📄 论文摘要

While Large Language Models (LLMs) have empowered AI research agents to perform isolated scientific tasks, automating complex, real-world workflows, such as LLM training, remains a significant challenge. In this paper, we introduce TREX, a multi-agent system that automates the entire LLM training life-cycle. By orchestrating collaboration between two core modules-the Researcher and the Executor-the system seamlessly performs requirement analysis, open-domain literature and data research, formulation of training strategies, preparation of data recipes, and model training and evaluation. The multi-round experimental process is modeled as a search tree, enabling the system to efficiently plan exploration paths, reuse historical results, and distill high-level insights from iterative trials. To evaluate the capability of automated LLM training, we construct FT-Bench, a benchmark comprising 10 tasks derived from real-world scenarios, ranging from optimizing fundamental model capabilities to enhancing performance on domain-specific tasks. Experimental results demonstrate that the TREX agent consistently optimizes model performance on target tasks.

### 🤖 AI 总结

**一句话总结**：While Large Language Models (LLMs) have empowered AI research agents to perform isolated scientific tasks, automating complex, real-world workflows, such as LLM training, remains a significant challen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, TREX, Automating, Fine-tuning, via, Agent-Driven, Tree-based, Exploration

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14116v1) | [下载PDF](https://arxiv.org/pdf/2604.14116v1.pdf)

---

## [2. Hierarchical Reinforcement Learning with Runtime Safety Shielding for Power Grid Operation](https://arxiv.org/abs/2604.14032v1)

**作者**：Gitesh Malik  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-04-15

### 📄 论文摘要

Reinforcement learning has shown promise for automating power-grid operation tasks such as topology control and congestion management. However, its deployment in real-world power systems remains limited by strict safety requirements, brittleness under rare disturbances, and poor generalization to unseen grid topologies. In safety-critical infrastructure, catastrophic failures cannot be tolerated, and learning-based controllers must operate within hard physical constraints.   This paper proposes a safety-constrained hierarchical control framework for power-grid operation that explicitly decouples long-horizon decision-making from real-time feasibility enforcement. A high-level reinforcement learning policy proposes abstract control actions, while a deterministic runtime safety shield filters unsafe actions using fast forward simulation. Safety is enforced as a runtime invariant, independent of policy quality or training distribution.   The proposed framework is evaluated on the Grid2Op benchmark suite under nominal conditions, forced line-outage stress tests, and zero-shot deployment on the ICAPS 2021 large-scale transmission grid without retraining. Results show that flat reinforcement learning policies are brittle under stress, while safety-only methods are overly conservative. In contrast, the proposed hierarchical and safety-aware approach achieves longer episode survival, lower peak line loading, and robust zero-shot generalization to unseen grids.   These results indicate that safety and generalization in power-grid control are best achieved through architectural design rather than increasingly complex reward engineering, providing a practical path toward deployable learning-based controllers for real-world energy systems.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning has shown promise for automating power-grid operation tasks such as topology control and congestion management. However, its deployment in real-world power systems remains limit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hierarchical, Reinforcement, Learning, Runtime, Safety, Shielding, Power, Grid

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14032v1) | [下载PDF](https://arxiv.org/pdf/2604.14032v1.pdf)

---

## [3. Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents](https://arxiv.org/abs/2604.14004v1)

**作者**：Kangsan Kim, Minki Kang, Taeil Kim 等 6 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-04-15

### 📄 论文摘要

Memory-based self-evolution has emerged as a promising paradigm for coding agents. However, existing approaches typically restrict memory utilization to homogeneous task domains, failing to leverage the shared infrastructural foundations, such as runtime environments and programming languages, that exist across diverse real-world coding problems. To address this limitation, we investigate \textbf{Memory Transfer Learning} (MTL) by harnessing a unified memory pool from heterogeneous domains. We evaluate performance across 6 coding benchmarks using four memory representations, ranging from concrete traces to abstract insights. Our experiments demonstrate that cross-domain memory improves average performance by 3.7\%, primarily by transferring meta-knowledge, such as validation routines, rather than task-specific code. Importantly, we find that abstraction dictates transferability; high-level insights generalize well, whereas low-level traces often induce negative transfer due to excessive specificity. Furthermore, we show that transfer effectiveness scales with the size of the memory pool, and memory can be transferred even between different models. Our work establishes empirical design principles for expanding memory utilization beyond single-domain silos. Project page: https://memorytransfer.github.io/

### 🤖 AI 总结

**一句话总结**：Memory-based self-evolution has emerged as a promising paradigm for coding agents. However, existing approaches typically restrict memory utilization to homogeneous task domains, failing to leverage t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Memory, Transfer, Learning, How, Memories, Transferred, Across, Domains

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14004v1) | [下载PDF](https://arxiv.org/pdf/2604.14004v1.pdf)

---

## cs.CL

## [4. From Feelings to Metrics: Understanding and Formalizing How Users Vibe-Test LLMs](https://arxiv.org/abs/2604.14137v1)

**作者**：Itay Itzhak, Eliya Habba, Gabriel Stanovsky 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-04-15

### 📄 论文摘要

Evaluating LLMs is challenging, as benchmark scores often fail to capture models' real-world usefulness. Instead, users often rely on ``vibe-testing'': informal experience-based evaluation, such as comparing models on coding tasks related to their own workflow. While prevalent, vibe-testing is often too ad hoc and unstructured to analyze or reproduce at scale. In this work, we study how vibe-testing works in practice and then formalize it to support systematic analysis. We first analyze two empirical resources: (1) a survey of user evaluation practices, and (2) a collection of in-the-wild model comparison reports from blogs and social media. Based on these resources, we formalize vibe-testing as a two-part process: users personalize both what they test and how they judge responses. We then introduce a proof-of-concept evaluation pipeline that follows this formulation by generating personalized prompts and comparing model outputs using user-aware subjective criteria. In experiments on coding benchmarks, we find that combining personalized prompts and user-aware evaluation can change which model is preferred, reflecting the role of vibe-testing in practice. These findings suggest that formalized vibe-testing can serve as a useful approach for bridging benchmark scores and real-world experience.

### 🤖 AI 总结

**一句话总结**：Evaluating LLMs is challenging, as benchmark scores often fail to capture models' real-world usefulness. Instead, users often rely on ``vibe-testing'': informal experience-based evaluation, such as co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Feelings, Metrics, Understanding, Formalizing, How, Users, Vibe-Test

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14137v1) | [下载PDF](https://arxiv.org/pdf/2604.14137v1.pdf)

---

## [5. Correct Prediction, Wrong Steps? Consensus Reasoning Knowledge Graph for Robust Chain-of-Thought Synthesis](https://arxiv.org/abs/2604.14121v1)

**作者**：Zipeng Ling, Shuliang Liu, Shenghong Fu 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-15

### 📄 论文摘要

LLM reasoning traces suffer from complex flaws -- *Step Internal Flaws* (logical errors, hallucinations, etc.) and *Step-wise Flaws* (overthinking, underthinking), which vary by sample. A natural approach would be to provide ground-truth labels to guide LLMs' reasoning. Contrary to intuition, we show that this yields no improvement in reasoning ability. We then propose CRAFT, a unified framework that mitigates both types of Step flaws, which builds a Reasoning Knowledge Graph (RKG) based on the consensus parts of multiple candidate traces, and synthesizes a high-quality trace through topological generation. Our approach improves label-prediction accuracy by 10+% on average, and consistently outperforms all baselines across both logical and mathematical reasoning benchmarks. Further, detailed benchmark evaluation proves that our method also improves the quality of LLMs' reasoning traces in multiple dimensions.

### 🤖 AI 总结

**一句话总结**：LLM reasoning traces suffer from complex flaws -- *Step Internal Flaws* (logical errors, hallucinations, etc.) and *Step-wise Flaws* (overthinking, underthinking), which vary by sample. A natural appr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Correct, Prediction, Wrong, Steps?, Consensus, Reasoning, Knowledge, Graph

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14121v1) | [下载PDF](https://arxiv.org/pdf/2604.14121v1.pdf)

---

## [6. Interpretable Stylistic Variation in Human and LLM Writing Across Genres, Models, and Decoding Strategies](https://arxiv.org/abs/2604.14111v1)

**作者**：Swati Rallapalli, Shannon Gallagher, Ronald Yurko 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-15

### 📄 论文摘要

Large Language Models (LLMs) are now capable of generating highly fluent, human-like text. They enable many applications, but also raise concerns such as large scale spam, phishing, or academic misuse. While much work has focused on detecting LLM-generated text, only limited work has gone into understanding the stylistic differences between human-written and machine-generated text. In this work, we perform a large scale analysis of stylistic variation across human-written text and outputs from 11 LLMs spanning 8 different genres and 4 decoding strategies using Douglas Biber's set of lexicogrammatical and functional features. Our findings reveal insights that can guide intentional LLM usage. First, key linguistic differentiators of LLM-generated text seem robust to generation conditions (e.g., prompt settings to nudge them to generate human-like text, or availability of human-written text to continue the style); second, genre exerts a stronger influence on stylistic features than the source itself; third, chat variants of the models generally appear to be clustered together in stylistic space, and finally, model has a larger effect on the style than decoding strategy, with some exceptions. These results highlight the relative importance of model and genre over prompting and decoding strategies in shaping the stylistic behavior of machine-generated text.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) are now capable of generating highly fluent, human-like text. They enable many applications, but also raise concerns such as large scale spam, phishing, or academic misuse...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Interpretable, Stylistic, Variation, Human, Writing, Across, Genres

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14111v1) | [下载PDF](https://arxiv.org/pdf/2604.14111v1.pdf)

---

## [7. From Weights to Activations: Is Steering the Next Frontier of Adaptation?](https://arxiv.org/abs/2604.14090v1)

**作者**：Simon Ostermann, Daniil Gurgurov, Tanja Baeumel 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-15

### 📄 论文摘要

Post-training adaptation of language models is commonly achieved through parameter updates or input-based methods such as fine-tuning, parameter-efficient adaptation, and prompting. In parallel, a growing body of work modifies internal activations at inference time to influence model behavior, an approach known as steering. Despite increasing use, steering is rarely analyzed within the same conceptual framework as established adaptation methods.   In this work, we argue that steering should be regarded as a form of model adaptation. We introduce a set of functional criteria for adaptation methods and use them to compare steering approaches with classical alternatives. This analysis positions steering as a distinct adaptation paradigm based on targeted interventions in activation space, enabling local and reversible behavioral change without parameter updates. The resulting framing clarifies how steering relates to existing methods, motivating a unified taxonomy for model adaptation.

### 🤖 AI 总结

**一句话总结**：Post-training adaptation of language models is commonly achieved through parameter updates or input-based methods such as fine-tuning, parameter-efficient adaptation, and prompting. In parallel, a gro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Weights, Activations, Steering, Next, Frontier, Adaptation?, Post-training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14090v1) | [下载PDF](https://arxiv.org/pdf/2604.14090v1.pdf)

---

## [8. Diffusion Language Models for Speech Recognition](https://arxiv.org/abs/2604.14001v1)

**作者**：Davyd Naveriani, Albert Zeyer, Ralf Schlüter 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.LG, cs.NE  
**发布时间**：2026-04-15

### 📄 论文摘要

Diffusion language models have recently emerged as a leading alternative to standard language models, due to their ability for bidirectional attention and parallel text generation. In this work, we explore variants for their use in speech recognition. Specifically, we introduce a comprehensive guide to incorporating masked diffusion language models (MDLM) and uniform-state diffusion models (USDMs) for rescoring ASR hypotheses. Additionally, we design a new joint-decoding method that combines CTC and USDM by integrating the framewise probability distributions derived from CTC with the labelwise probability distributions computed by USDM at each decoding step, thereby generating new candidates that combine strong language knowledge from USDM and acoustic information from CTC. Our findings reveal that USDM, as well as MDLM, can significantly improve the accuracy of recognized text. We publish all our code and recipes.

### 🤖 AI 总结

**一句话总结**：Diffusion language models have recently emerged as a leading alternative to standard language models, due to their ability for bidirectional attention and parallel text generation. In this work, we ex...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Language, Models, Speech, Recognition, have, recently, emerged

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14001v1) | [下载PDF](https://arxiv.org/pdf/2604.14001v1.pdf)

---

## cs.CV

## [9. Seedance 2.0: Advancing Video Generation for World Complexity](https://arxiv.org/abs/2604.14148v1)

**作者**：Team Seedance, De Chen, Liyang Chen 等 171 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-15

### 📄 论文摘要

Seedance 2.0 is a new native multi-modal audio-video generation model, officially released in China in early February 2026. Compared with its predecessors, Seedance 1.0 and 1.5 Pro, Seedance 2.0 adopts a unified, highly efficient, and large-scale architecture for multi-modal audio-video joint generation. This allows it to support four input modalities: text, image, audio, and video, by integrating one of the most comprehensive suites of multi-modal content reference and editing capabilities available in the industry to date. It delivers substantial, well-rounded improvements across all key sub-dimensions of video and audio generation. In both expert evaluations and public user tests, the model has demonstrated performance on par with the leading levels in the field. Seedance 2.0 supports direct generation of audio-video content with durations ranging from 4 to 15 seconds, with native output resolutions of 480p and 720p. For multi-modal inputs as reference, its current open platform supports up to 3 video clips, 9 images, and 3 audio clips. In addition, we provide Seedance 2.0 Fast version, an accelerated variant of Seedance 2.0 designed to boost generation speed for low-latency scenarios. Seedance 2.0 has delivered significant improvements to its foundational generation capabilities and multi-modal generation performance, bringing an enhanced creative experience for end users.

### 🤖 AI 总结

**一句话总结**：Seedance 2.0 is a new native multi-modal audio-video generation model, officially released in China in early February 2026. Compared with its predecessors, Seedance 1.0 and 1.5 Pro, Seedance 2.0 adopt...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Seedance, Advancing, Video, Generation, World, Complexity, new, native

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14148v1) | [下载PDF](https://arxiv.org/pdf/2604.14148v1.pdf)

---

## [10. ROSE: Retrieval-Oriented Segmentation Enhancement](https://arxiv.org/abs/2604.14147v1)

**作者**：Song Tang, Guangquan Jie, Henghui Ding 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-15

### 📄 论文摘要

Existing segmentation models based on multimodal large language models (MLLMs), such as LISA, often struggle with novel or emerging entities due to their inability to incorporate up-to-date knowledge. To address this challenge, we introduce the Novel Emerging Segmentation Task (NEST), which focuses on segmenting (i) novel entities that MLLMs fail to recognize due to their absence from training data, and (ii) emerging entities that exist within the model's knowledge but demand up-to-date external information for accurate recognition. To support the study of NEST, we construct a NEST benchmark using an automated pipeline that generates news-related data samples for comprehensive evaluation. Additionally, we propose ROSE: Retrieval-Oriented Segmentation Enhancement, a plug-and-play framework designed to augment any MLLM-based segmentation model. ROSE comprises four key components. First, an Internet Retrieval-Augmented Generation module is introduced to employ user-provided multimodal inputs to retrieve real-time web information. Then, a Textual Prompt Enhancer enriches the model with up-to-date information and rich background knowledge, improving the model's perception ability for emerging entities. Furthermore, a Visual Prompt Enhancer is proposed to compensate for MLLMs' lack of exposure to novel entities by leveraging internet-sourced images. To maintain efficiency, a WebSense module is introduced to intelligently decide when to invoke retrieval mechanisms based on user input. Experimental results demonstrate that ROSE significantly boosts performance on the NEST benchmark, outperforming a strong Gemini-2.0 Flash-based retrieval baseline by 19.2 in gIoU.

### 🤖 AI 总结

**一句话总结**：Existing segmentation models based on multimodal large language models (MLLMs), such as LISA, often struggle with novel or emerging entities due to their inability to incorporate up-to-date knowledge....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ROSE, Retrieval-Oriented, Segmentation, Enhancement, Existing, models, multimodal, large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14147v1) | [下载PDF](https://arxiv.org/pdf/2604.14147v1.pdf)

---

## [11. SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments](https://arxiv.org/abs/2604.14144v1)

**作者**：Dinging Li, Yingxiu Zhao, Xinrui Cheng 等 19 位作者  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-04-15

### 📄 论文摘要

Spatial reasoning over three-dimensional scenes is a core capability for embodied intelligence, yet continuous model improvement remains bottlenecked by the cost of geometric annotation. The self-evolving paradigm offers a promising path, but its reliance on model consensus to construct pseudo-labels causes training to reinforce rather than correct the model's own geometric errors. We identify a property unique to 3D spatial reasoning that circumvents this limitation: ground truth is a deterministic consequence of the underlying geometry, computable exactly from point clouds and camera poses without any model involvement. Building on this insight, we present SpatialEvo, a self-evolving framework for 3D spatial reasoning, centered on the Deterministic Geometric Environment (DGE). The DGE formalizes 16 spatial reasoning task categories under explicit geometric validation rules and converts unannotated 3D scenes into zero-noise interactive oracles, replacing model consensus with objective physical feedback. A single shared-parameter policy co-evolves across questioner and solver roles under DGE constraints: the questioner generates physically valid spatial questions grounded in scene observations, while the solver derives precise answers against DGE-verified ground truth. A task-adaptive scheduler endogenously concentrates training on the model's weakest categories, producing a dynamic curriculum without manual design. Experiments across nine benchmarks demonstrate that SpatialEvo achieves the highest average score at both 3B and 7B scales, with consistent gains on spatial reasoning benchmarks and no degradation on general visual understanding.

### 🤖 AI 总结

**一句话总结**：Spatial reasoning over three-dimensional scenes is a core capability for embodied intelligence, yet continuous model improvement remains bottlenecked by the cost of geometric annotation. The self-evol...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SpatialEvo, Self-Evolving, Spatial, Intelligence, via, Deterministic, Geometric, Environments

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14144v1) | [下载PDF](https://arxiv.org/pdf/2604.14144v1.pdf)

---

## [12. Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141v1)

**作者**：Lin-Zhuo Chen, Jian Gao, Yihang Chen 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-15

### 📄 论文摘要

Streaming 3D reconstruction aims to recover 3D information, such as camera poses and point clouds, from a video stream, which necessitates geometric accuracy, temporal   consistency, and computational efficiency. Motivated by the principles of Simultaneous Localization and Mapping (SLAM), we introduce LingBot-Map, a feed-forward 3D foundation   model for reconstructing scenes from streaming data, built upon a geometric context transformer (GCT) architecture. A defining aspect of LingBot-Map lies in its carefully   designed attention mechanism, which integrates an anchor context, a pose-reference window, and a trajectory memory to address coordinate grounding, dense geometric cues, and   long-range drift correction, respectively. This design keeps the streaming state compact while retaining rich geometric context, enabling stable efficient inference at around   20 FPS on 518 x 378 resolution inputs over long sequences exceeding 10,000 frames. Extensive evaluations across a variety of benchmarks demonstrate that our approach   achieves superior performance compared to both existing streaming and iterative optimization-based approaches.

### 🤖 AI 总结

**一句话总结**：Streaming 3D reconstruction aims to recover 3D information, such as camera poses and point clouds, from a video stream, which necessitates geometric accuracy, temporal   consistency, and computational...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Geometric, Context, Transformer, Streaming, Reconstruction, aims, recover

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14141v1) | [下载PDF](https://arxiv.org/pdf/2604.14141v1.pdf)

---

## [13. Don't Let the Video Speak: Audio-Contrastive Preference Optimization for Audio-Visual Language Models](https://arxiv.org/abs/2604.14129v1)

**作者**：Ami Baid, Zihui Xue, Kristen Grauman  
**分类**：cs.CV  
**发布时间**：2026-04-15

### 📄 论文摘要

While Audio-Visual Language Models (AVLMs) have achieved remarkable progress over recent years, their reliability is bottlenecked by cross-modal hallucination. A particularly pervasive manifestation is video-driven audio hallucination: models routinely exploit visual shortcuts to hallucinate expected sounds, discarding true auditory evidence. To counteract this deeply ingrained visual dominance, we propose Audio-Contrastive Preference Optimization (ACPO). This dual-axis preference learning framework introduces an output-contrastive objective to penalize visual descriptions masquerading as audio facts, alongside an input-contrastive objective that swaps audio tracks to explicitly penalize generation invariant to the true auditory signal. Extensive experiments demonstrate that ACPO establishes highly faithful audio grounding and mitigates audio hallucination without compromising overarching multimodal capabilities.

### 🤖 AI 总结

**一句话总结**：While Audio-Visual Language Models (AVLMs) have achieved remarkable progress over recent years, their reliability is bottlenecked by cross-modal hallucination. A particularly pervasive manifestation i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Don't, Let, Video, Speak, Audio-Contrastive, Preference, Optimization, Audio-Visual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14129v1) | [下载PDF](https://arxiv.org/pdf/2604.14129v1.pdf)

---

## [14. HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System](https://arxiv.org/abs/2604.14125v1)

**作者**：Tianshuo Yang, Guanyu Chen, Yutian Chen 等 11 位作者  
**分类**：cs.CV, cs.AI, cs.RO  
**发布时间**：2026-04-15

### 📄 论文摘要

While end-to-end Vision-Language-Action (VLA) models offer a promising paradigm for robotic manipulation, fine-tuning them on narrow control data often compromises the profound reasoning capabilities inherited from their base Vision-Language Models (VLMs). To resolve this fundamental trade-off, we propose HiVLA, a visual-grounded-centric hierarchical framework that explicitly decouples high-level semantic planning from low-level motor control. In high-level part, a VLM planner first performs task decomposition and visual grounding to generate structured plans, comprising a subtask instruction and a precise target bounding box. Then, to translate this plan into physical actions, we introduce a flow-matching Diffusion Transformer (DiT) action expert in low-level part equipped with a novel cascaded cross-attention mechanism. This design sequentially fuses global context, high-resolution object-centric crops and skill semantics, enabling the DiT to focus purely on robust execution. Our decoupled architecture preserves the VLM's zero-shot reasoning while allowing independent improvement of both components. Extensive experiments in simulation and the real world demonstrate that HiVLA significantly outperforms state-of-the-art end-to-end baselines, particularly excelling in long-horizon skill composition and the fine-grained manipulation of small objects in cluttered scenes.

### 🤖 AI 总结

**一句话总结**：While end-to-end Vision-Language-Action (VLA) models offer a promising paradigm for robotic manipulation, fine-tuning them on narrow control data often compromises the profound reasoning capabilities ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HiVLA, Visual-Grounded-Centric, Hierarchical, Embodied, Manipulation, System, While, end-to-end

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14125v1) | [下载PDF](https://arxiv.org/pdf/2604.14125v1.pdf)

---

## [15. Training-Free Semantic Multi-Object Tracking with Vision-Language Models](https://arxiv.org/abs/2604.14074v1)

**作者**：Laurence Bonat, Francesco Tonini, Elisa Ricci 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-15

### 📄 论文摘要

Semantic Multi-Object Tracking (SMOT) extends multi-object tracking with semantic outputs such as video summaries, instance-level captions, and interaction labels, aiming to move from trajectories to human-interpretable descriptions of dynamic scenes. Existing SMOT systems are trained end-to-end, coupling progress to expensive supervision, limiting the ability to rapidly adapt to new foundation models and new interactions. We propose TF-SMOT, a training-free SMOT pipeline that composes pretrained components for detection, mask-based tracking, and video-language generation. TF-SMOT combines D-FINE and the promptable SAM2 segmentation tracker to produce temporally consistent tracklets, uses contour grounding to generate video summaries and instance captions with InternVideo2.5, and aligns extracted interaction predicates to BenSMOT WordNet synsets via gloss-based semantic retrieval with LLM disambiguation. On BenSMOT, TF-SMOT achieves state-of-the-art tracking performance within the SMOT setting and improves summary and caption quality compared to prior art. Interaction recognition, however, remains challenging under strict exact-match evaluation on the fine-grained and long-tailed WordNet label space; our analysis and ablations indicate that semantic overlap and label granularity substantially affect measured performance.

### 🤖 AI 总结

**一句话总结**：Semantic Multi-Object Tracking (SMOT) extends multi-object tracking with semantic outputs such as video summaries, instance-level captions, and interaction labels, aiming to move from trajectories to ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Training-Free, Semantic, Multi-Object, Tracking, Vision-Language, Models, SMOT, extends

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14074v1) | [下载PDF](https://arxiv.org/pdf/2604.14074v1.pdf)

---

## [16. Towards Unconstrained Human-Object Interaction](https://arxiv.org/abs/2604.14069v1)

**作者**：Francesco Tonini, Alessandro Conti, Lorenzo Vaquero 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-15

### 📄 论文摘要

Human-Object Interaction (HOI) detection is a longstanding computer vision problem concerned with predicting the interaction between humans and objects. Current HOI models rely on a vocabulary of interactions at training and inference time, limiting their applicability to static environments. With the advent of Multimodal Large Language Models (MLLMs), it has become feasible to explore more flexible paradigms for interaction recognition. In this work, we revisit HOI detection through the lens of MLLMs and apply them to in-the-wild HOI detection. We define the Unconstrained HOI (U-HOI) task, a novel HOI domain that removes the requirement for a predefined list of interactions at both training and inference. We evaluate a range of MLLMs on this setting and introduce a pipeline that includes test-time inference and language-to-graph conversion to extract structured interactions from free-form text. Our findings highlight the limitations of current HOI detectors and the value of MLLMs for U-HOI. Code will be available at https://github.com/francescotonini/anyhoi

### 🤖 AI 总结

**一句话总结**：Human-Object Interaction (HOI) detection is a longstanding computer vision problem concerned with predicting the interaction between humans and objects. Current HOI models rely on a vocabulary of inte...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Towards, Unconstrained, Human-Object, Interaction, HOI, detection, longstanding, computer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14069v1) | [下载PDF](https://arxiv.org/pdf/2604.14069v1.pdf)

---

## [17. Free Geometry: Refining 3D Reconstruction from Longer Versions of Itself](https://arxiv.org/abs/2604.14048v1)

**作者**：Yuhang Dai, Xingyi Yang  
**分类**：cs.CV  
**发布时间**：2026-04-15

### 📄 论文摘要

Feed-forward 3D reconstruction models are efficient but rigid: once trained, they perform inference in a zero-shot manner and cannot adapt to the test scene. As a result, visually plausible reconstructions often contain errors, particularly under occlusions, specularities, and ambiguous cues. To address this, we introduce Free Geometry, a framework that enables feed-forward 3D reconstruction models to self-evolve at test time without any 3D ground truth. Our key insight is that, when the model receives more views, it produces more reliable and view-consistent reconstructions. Leveraging this property, given a testing sequence, we mask a subset of frames to construct a self-supervised task. Free Geometry enforces cross-view feature consistency between representations from full and partial observations, while maintaining the pairwise relations implied by the held-out frames. This self-supervision allows for fast recalibration via lightweight LoRA updates, taking less than 2 minutes per dataset on a single GPU. Our approach consistently improves state-of-the-art foundation models, including Depth Anything 3 and VGGT, across 4 benchmark datasets, yielding an average improvement of 3.73% in camera pose accuracy and 2.88% in point map prediction. Code is available at https://github.com/hiteacherIamhumble/Free-Geometry .

### 🤖 AI 总结

**一句话总结**：Feed-forward 3D reconstruction models are efficient but rigid: once trained, they perform inference in a zero-shot manner and cannot adapt to the test scene. As a result, visually plausible reconstruc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, of, Free, Geometry, Refining, Reconstruction, Longer, Versions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14048v1) | [下载PDF](https://arxiv.org/pdf/2604.14048v1.pdf)

---

## [18. Decoding the Delta: Unifying Remote Sensing Change Detection and Understanding with Multimodal Large Language Models](https://arxiv.org/abs/2604.14044v1)

**作者**：Xiaohe Li, Jiahao Li, Kaixin Zhang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-15

### 📄 论文摘要

While Multimodal Large Language Models (MLLMs) excel in general vision-language tasks, their application to remote sensing change understanding is hindered by a fundamental "temporal blindness". Existing architectures lack intrinsic mechanisms for multi-temporal contrastive reasoning and struggle with precise spatial grounding. To address this, we first introduce Delta-QA, a comprehensive benchmark comprising 180k visual question-answering samples. Delta-QA unifies pixel-level segmentation and visual question answering across bi- and tri-temporal scenarios, structuring change interpretation into four progressive cognitive dimensions. Methodologically, we propose Delta-LLaVA, a novel MLLM framework explicitly tailored for multi-temporal remote sensing interpretation. It overcomes the limitations of naive feature concatenation through three core innovations: a Change-Enhanced Attention module that systematically isolates and amplifies visual differences, a Change-SEG module utilizing Change Prior Embedding to extract differentiable difference features as input for the LLM, and Local Causal Attention to prevent cross-temporal contextual leakage. Extensive experiments demonstrate that Delta-LLaVA decisively outperforms leading generalist MLLMs and specialized segmentation models in complex change deduction and high-precision boundary localization, establishing a unified framework for earth observation intelligence.

### 🤖 AI 总结

**一句话总结**：While Multimodal Large Language Models (MLLMs) excel in general vision-language tasks, their application to remote sensing change understanding is hindered by a fundamental "temporal blindness". Exist...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Decoding, Delta, Unifying, Remote, Sensing, Change, Detection, Understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14044v1) | [下载PDF](https://arxiv.org/pdf/2604.14044v1.pdf)

---

## [19. Seek-and-Solve: Benchmarking MLLMs for Visual Clue-Driven Reasoning in Daily Scenarios](https://arxiv.org/abs/2604.14041v1)

**作者**：Xiaomin Li, Tala Wang, Zichen Zhong 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-15

### 📄 论文摘要

Daily scenarios are characterized by visual richness, requiring Multimodal Large Language Models (MLLMs) to filter noise and identify decisive visual clues for accurate reasoning. Yet, current benchmarks predominantly aim at evaluating MLLMs' pre-existing knowledge or perceptual understanding, often neglecting the critical capability of reasoning. To bridge this gap, we introduce DailyClue, a benchmark designed for visual clue-driven reasoning in daily scenarios. Our construction is guided by two core principles: (1) strict grounding in authentic daily activities, and (2) challenging query design that necessitates more than surface-level perception. Instead of simple recognition, our questions compel MLLMs to actively explore suitable visual clues and leverage them for subsequent reasoning. To this end, we curate a comprehensive dataset spanning four major daily domains and 16 distinct subtasks. Comprehensive evaluation across MLLMs and agentic models underscores the formidable challenge posed by our benchmark. Our analysis reveals several critical insights, emphasizing that the accurate identification of visual clues is essential for robust reasoning.

### 🤖 AI 总结

**一句话总结**：Daily scenarios are characterized by visual richness, requiring Multimodal Large Language Models (MLLMs) to filter noise and identify decisive visual clues for accurate reasoning. Yet, current benchma...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Seek-and-Solve, Benchmarking, MLLMs, Visual, Clue-Driven, Reasoning, Daily, Scenarios

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14041v1) | [下载PDF](https://arxiv.org/pdf/2604.14041v1.pdf)

---

## [20. POINTS-Seeker: Towards Training a Multimodal Agentic Search Model from Scratch](https://arxiv.org/abs/2604.14029v1)

**作者**：Yikun Liu, Yuan Liu, Le Tian 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-15

### 📄 论文摘要

While Large Multimodal Models (LMMs) demonstrate impressive visual perception, they remain epistemically constrained by their static parametric knowledge. To transcend these boundaries, multimodal search models have been adopted to actively interact with the external environment for evidence retrieval. Diverging from prevailing paradigms that merely retrofit general LMMs with search tools as modular extensions, we explore the potential of building a multimodal agentic search model from scratch. Specifically, we make the following contributions: (i) we introduce Agentic Seeding, a dedicated phase designed to weave the foundational precursors necessary for eliciting agentic behaviors; (ii) we uncover a performance bottleneck in long-horizon interactions, where the increasing volume of interaction history overwhelms the model's ability to locate ground-truth evidence. To mitigate this, we propose V-Fold, an adaptive history-aware compression scheme that preserves recent dialogue turns in high fidelity while folding historical context into the visual space via rendering; and (iii) we develop POINTS-Seeker-8B, a state-of-the-art multimodal agentic search model that consistently outperforms existing models across six diverse benchmarks, effectively resolving the challenges of long-horizon, knowledge-intensive visual reasoning.

### 🤖 AI 总结

**一句话总结**：While Large Multimodal Models (LMMs) demonstrate impressive visual perception, they remain epistemically constrained by their static parametric knowledge. To transcend these boundaries, multimodal sea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：POINTS-Seeker, Towards, Training, Multimodal, Agentic, Search, Model, Scratch

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14029v1) | [下载PDF](https://arxiv.org/pdf/2604.14029v1.pdf)

---

## [21. Feed-Forward 3D Scene Modeling: A Problem-Driven Perspective](https://arxiv.org/abs/2604.14025v1)

**作者**：Weijie Wang, Qihang Cao, Sensen Gao 等 13 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-04-15

### 📄 论文摘要

Reconstructing 3D representations from 2D inputs is a fundamental task in computer vision and graphics, serving as a cornerstone for understanding and interacting with the physical world. While traditional methods achieve high fidelity, they are limited by slow per-scene optimization or category-specific training, which hinders their practical deployment and scalability. Hence, generalizable feed-forward 3D reconstruction has witnessed rapid development in recent years. By learning a model that maps images directly to 3D representations in a single forward pass, these methods enable efficient reconstruction and robust cross-scene generalization. Our survey is motivated by a critical observation: despite the diverse geometric output representations, ranging from implicit fields to explicit primitives, existing feed-forward approaches share similar high-level architectural patterns, such as image feature extraction backbones, multi-view information fusion mechanisms, and geometry-aware design principles. Consequently, we abstract away from these representation differences and instead focus on model design, proposing a novel taxonomy centered on model design strategies that are agnostic to the output format. Our proposed taxonomy organizes the research directions into five key problems that drive recent research development: feature enhancement, geometry awareness, model efficiency, augmentation strategies and temporal-aware models. To support this taxonomy with empirical grounding and standardized evaluation, we further comprehensively review related benchmarks and datasets, and extensively discuss and categorize real-world applications based on feed-forward 3D models. Finally, we outline future directions to address open challenges such as scalability, evaluation standards, and world modeling.

### 🤖 AI 总结

**一句话总结**：Reconstructing 3D representations from 2D inputs is a fundamental task in computer vision and graphics, serving as a cornerstone for understanding and interacting with the physical world. While tradit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Feed-Forward, Scene, Modeling, Problem-Driven, Perspective, Reconstructing, representations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14025v1) | [下载PDF](https://arxiv.org/pdf/2604.14025v1.pdf)

---

## cs.LG

## [22. From $P(y|x)$ to $P(y)$: Investigating Reinforcement Learning in Pre-train Space](https://arxiv.org/abs/2604.14142v1)

**作者**：Yuqiao Tan, Minzheng Wang, Bo Liu 等 8 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-04-15

### 📄 论文摘要

While reinforcement learning with verifiable rewards (RLVR) significantly enhances LLM reasoning by optimizing the conditional distribution P(y|x), its potential is fundamentally bounded by the base model's existing output distribution. Optimizing the marginal distribution P(y) in the Pre-train Space addresses this bottleneck by encoding reasoning ability and preserving broad exploration capacity. Yet, conventional pre-training relies on static corpora for passive learning, leading to a distribution shift that hinders targeted reasoning enhancement. In this paper, we introduce PreRL (Pre-train Space RL), which applies reward-driven online updates directly to P(y). We theoretically and empirically validate the strong gradient alignment between log P(y) and log P(y|x), establishing PreRL as a viable surrogate for standard RL. Furthermore, we uncover a critical mechanism: Negative Sample Reinforcement (NSR) within PreRL serves as an exceptionally effective driver for reasoning. NSR-PreRL rapidly prunes incorrect reasoning spaces while stimulating endogenous reflective behaviors, increasing transition and reflection thoughts by 14.89x and 6.54x, respectively. Leveraging these insights, we propose Dual Space RL (DSRL), a Policy Reincarnation strategy that initializes models with NSR-PreRL to expand the reasoning horizon before transitioning to standard RL for fine-grained optimization. Extensive experiments demonstrate that DSRL consistently outperforms strong baselines, proving that pre-train space pruning effectively steers the policy toward a refined correct reasoning subspace.

### 🤖 AI 总结

**一句话总结**：While reinforcement learning with verifiable rewards (RLVR) significantly enhances LLM reasoning by optimizing the conditional distribution P(y|x), its potential is fundamentally bounded by the base m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：$P, Investigating, Reinforcement, Learning, Pre-train, Space, While, verifiable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14142v1) | [下载PDF](https://arxiv.org/pdf/2604.14142v1.pdf)

---

## [23. Complex Interpolation of Matrices with an application to Multi-Manifold Learning](https://arxiv.org/abs/2604.14118v1)

**作者**：Adi Arbel, Stefan Steinerberger, Ronen Talmon  
**分类**：cs.LG, math.SP  
**发布时间**：2026-04-15

### 📄 论文摘要

Given two symmetric positive-definite matrices $A, B \in \mathbb{R}^{n \times n}$, we study the spectral properties of the interpolation $A^{1-x} B^x$ for $0 \leq x \leq 1$. The presence of `common structures' in $A$ and $B$, eigenvectors pointing in a similar direction, can be investigated using this interpolation perspective. Generically, exact log-linearity of the operator norm $\|A^{1-x} B^x\|$ is equivalent to the existence of a shared eigenvector in the original matrices; stability bounds show that approximate log-linearity forces principal singular vectors to align with leading eigenvectors of both matrices. These results give rise to and provide theoretical justification for a multi-manifold learning framework that identifies common and distinct latent structures in multiview data.

### 🤖 AI 总结

**一句话总结**：Given two symmetric positive-definite matrices $A, B \in \mathbb{R}^{n \times n}$, we study the spectral properties of the interpolation $A^{1-x} B^x$ for $0 \leq x \leq 1$. The presence of `common st...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, an, Complex, Interpolation, Matrices, application, Multi-Manifold, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14118v1) | [下载PDF](https://arxiv.org/pdf/2604.14118v1.pdf)

---

## [24. Momentum Further Constrains Sharpness at the Edge of Stochastic Stability](https://arxiv.org/abs/2604.14108v1)

**作者**：Arseniy Andreyev, Advikar Ananthkumar, Marc Walden 等 5 位作者  
**分类**：cs.LG, math.DS, math.OC, stat.ML  
**发布时间**：2026-04-15

### 📄 论文摘要

Recent work suggests that (stochastic) gradient descent self-organizes near an instability boundary, shaping both optimization and the solutions found. Momentum and mini-batch gradients are widely used in practical deep learning optimization, but it remains unclear whether they operate in a comparable regime of instability. We demonstrate that SGD with momentum exhibits an Edge of Stochastic Stability (EoSS)-like regime with batch-size-dependent behavior that cannot be explained by a single momentum-adjusted stability threshold. Batch Sharpness (the expected directional mini-batch curvature) stabilizes in two distinct regimes: at small batch sizes it converges to a lower plateau $2(1-β)/η$, reflecting amplification of stochastic fluctuations by momentum and favoring flatter regions than vanilla SGD; at large batch sizes it converges to a higher plateau $2(1+β)/η$, where momentum recovers its classical stabilizing effect and favors sharper regions consistent with full-batch dynamics. We further show that this aligns with linear stability thresholds and discuss the implications for hyperparameter tuning and coupling.

### 🤖 AI 总结

**一句话总结**：Recent work suggests that (stochastic) gradient descent self-organizes near an instability boundary, shaping both optimization and the solutions found. Momentum and mini-batch gradients are widely use...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, of, Momentum, Further, Constrains, Sharpness, Edge, Stochastic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14108v1) | [下载PDF](https://arxiv.org/pdf/2604.14108v1.pdf)

---

## [25. Neural architectures for resolving references in program code](https://arxiv.org/abs/2604.14073v1)

**作者**：Gergő Szalay, Gergely Zsolt Kovács, Sándor Teleki 等 5 位作者  
**分类**：cs.LG, cs.NE  
**发布时间**：2026-04-15

### 📄 论文摘要

Resolving and rewriting references is fundamental in programming languages. Motivated by a real-world decompilation task, we abstract reference rewriting into the problems of direct and indirect indexing by permutation. We create synthetic benchmarks for these tasks and show that well-known sequence-to-sequence machine learning architectures are struggling on these benchmarks. We introduce new sequence-to-sequence architectures for both problems. Our measurements show that our architectures outperform the baselines in both robustness and scalability: our models can handle examples that are ten times longer compared to the best baseline. We measure the impact of our architecture in the real-world task of decompiling switch statements, which has an indexing subtask. According to our measurements, the extended model decreases the error rate by 42%. Multiple ablation studies show that all components of our architectures are essential.

### 🤖 AI 总结

**一句话总结**：Resolving and rewriting references is fundamental in programming languages. Motivated by a real-world decompilation task, we abstract reference rewriting into the problems of direct and indirect index...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Neural, architectures, resolving, references, program, code, rewriting, fundamental

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14073v1) | [下载PDF](https://arxiv.org/pdf/2604.14073v1.pdf)

---

## [26. $π$-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data](https://arxiv.org/abs/2604.14054v1)

**作者**：Yaocheng Zhang, Yuanheng Zhu, Wenyue Chong 等 10 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-04-15

### 📄 论文摘要

Deep search agents have emerged as a promising paradigm for addressing complex information-seeking tasks, but their training remains challenging due to sparse rewards, weak credit assignment, and limited labeled data. Self-play offers a scalable route to reduce data dependence, but conventional self-play optimizes students only through sparse outcome rewards, leading to low learning efficiency. In this work, we observe that self-play naturally produces a question construction path (QCP) during task generation, an intermediate artifact that captures the reverse solution process. This reveals a new source of privileged information for self-distillation: self-play can itself provide high-quality privileged context for the teacher model in a low-cost and scalable manner, without relying on human feedback or curated privileged information. Leveraging this insight, we propose Privileged Information Self-Play ($π$-Play), a multi-agent self-evolution framework. In $π$-Play, an examiner generates tasks together with their QCPs, and a teacher model leverages QCP as privileged context to densely supervise a student via self-distillation. This design transforms conventional sparse-reward self-play into a dense-feedback self-evolution loop. Extensive experiments show that data-free $π$-Play surpasses fully supervised search agents and improves evolutionary efficiency by 2-3$\times$ over conventional self-play.

### 🤖 AI 总结

**一句话总结**：Deep search agents have emerged as a promising paradigm for addressing complex information-seeking tasks, but their training remains challenging due to sparse rewards, weak credit assignment, and limi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, $π$-Play, Self-Play, via, Privileged, Self-Distillation, without, External

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14054v1) | [下载PDF](https://arxiv.org/pdf/2604.14054v1.pdf)

---

## [27. A Complete Symmetry Classification of Shallow ReLU Networks](https://arxiv.org/abs/2604.14037v1)

**作者**：Pranavkrishnan Ramakrishnan  
**分类**：cs.LG, math.AG, math.CO  
**发布时间**：2026-04-15

### 📄 论文摘要

Parameter space is not function space for neural network architectures. This fact, investigated as early as the 1990s under terms such as ``reverse engineering," or ``parameter identifiability", has led to the natural question of parameter space symmetries\textemdash the study of distinct parameters in neural architectures which realize the same function. Indeed, the quotient space obtained by identifying parameters giving rise to the same function, called the \textit{neuromanifold}, has been shown in some cases to have rich geometric properties, impacting optimization dynamics. Thus far, techniques towards complete classifications have required the analyticity of the activation function, notably excising the important case of ReLU. Here, in contrast, we exploit the non-differentiability of the ReLU activation to provide a complete classification of the symmetries in the shallow case.

### 🤖 AI 总结

**一句话总结**：Parameter space is not function space for neural network architectures. This fact, investigated as early as the 1990s under terms such as ``reverse engineering," or ``parameter identifiability", has l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Complete, Symmetry, Classification, Shallow, ReLU, Networks, Parameter

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14037v1) | [下载PDF](https://arxiv.org/pdf/2604.14037v1.pdf)

---

## [28. First-See-Then-Design: A Multi-Stakeholder View for Optimal Performance-Fairness Trade-Offs](https://arxiv.org/abs/2604.14035v1)

**作者**：Kavya Gupta, Nektarios Kalampalikis, Christoph Heitz 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-15

### 📄 论文摘要

Fairness in algorithmic decision-making is often defined in the predictive space, where predictive performance - used as a proxy for decision-maker (DM) utility - is traded off against prediction-based fairness notions, such as demographic parity or equality of opportunity. This perspective, however, ignores how predictions translate into decisions and ultimately into utilities and welfare for both DM and decision subjects (DS), as well as their allocation across social-salient groups.   In this paper, we propose a multi-stakeholder framework for fair algorithmic decision-making grounded in welfare economics and distributive justice, explicitly modeling the utilities of both the DM and DS, and defining fairness via a social planner's utility that captures inequalities in DS utilities across groups under different justice-based fairness notions (e.g., Egalitarian, Rawlsian). We formulate fair decision-making as a post-hoc multi-objective optimization problem, characterizing the achievable performance-fairness trade-offs in the two-dimensional utility space of DM utility and the social planner's utility, under different decision policy classes (deterministic vs. stochastic, shared vs. group-specific). Using the proposed framework, we then identify conditions (in terms of the stakeholders' utilities) under which stochastic policies are more optimal than deterministic ones, and empirically demonstrate that simple stochastic policies can yield superior performance-fairness trade-offs by leveraging outcome uncertainty. Overall, we advocate a shift from prediction-centric fairness to a transparent, justice-based, multi-stakeholder approach that supports the collaborative design of decision-making policies.

### 🤖 AI 总结

**一句话总结**：Fairness in algorithmic decision-making is often defined in the predictive space, where predictive performance - used as a proxy for decision-maker (DM) utility - is traded off against prediction-base...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：First-See-Then-Design, Multi-Stakeholder, View, Optimal, Performance-Fairness, Trade-Offs, Fairness, algorithmic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14035v1) | [下载PDF](https://arxiv.org/pdf/2604.14035v1.pdf)

---

## [29. MAny: Merge Anything for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2604.14016v1)

**作者**：Zijian Gao, Wangwang Jia, Xingxing Zhang 等 9 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-15

### 📄 论文摘要

Multimodal Continual Instruction Tuning (MCIT) is essential for sequential task adaptation of Multimodal Large Language Models (MLLMs) but is severely restricted by catastrophic forgetting. While existing literature focuses on the reasoning language backbone, in this work, we expose a critical yet neglected dual-forgetting phenomenon across both perception drift in Cross-modal Projection Space and reasoning collapse in Low-rank Parameter Space. To resolve this, we present \textbf{MAny} (\textbf{M}erge \textbf{Any}thing), a framework that merges task-specific knowledge through \textbf{C}ross-modal \textbf{P}rojection \textbf{M}erging (\textbf{CPM}) and \textbf{L}ow-rank \textbf{P}arameter \textbf{M}erging (\textbf{LPM}). Specifically, CPM recovers perceptual alignment by adaptively merging cross-modal visual representations via visual-prototype guidance, ensuring accurate feature recovery during inference. Simultaneously, LPM eliminates mutual interference among task-specific low-rank modules by recursively merging low-rank weight matrices. By leveraging recursive least squares, LPM provides a closed-form solution that mathematically guarantees an optimal fusion trajectory for reasoning stability. Notably, MAny operates as a training-free paradigm that achieves knowledge merging via efficient CPU-based algebraic operations, eliminating additional gradient-based optimization beyond initial tuning. Our extensive evaluations confirm the superior performance and robustness of MAny across multiple MLLMs and benchmarks. Specifically, on the UCIT benchmark, MAny achieves significant leads of up to 8.57\% and 2.85\% in final average accuracy over state-of-the-art methods across two different MLLMs, respectively.

### 🤖 AI 总结

**一句话总结**：Multimodal Continual Instruction Tuning (MCIT) is essential for sequential task adaptation of Multimodal Large Language Models (MLLMs) but is severely restricted by catastrophic forgetting. While exis...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MAny, Merge, Anything, Multimodal, Continual, Instruction, Tuning, MCIT

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14016v1) | [下载PDF](https://arxiv.org/pdf/2604.14016v1.pdf)

---

## [30. Parameter Importance is Not Static: Evolving Parameter Isolation for Supervised Fine-Tuning](https://arxiv.org/abs/2604.14010v1)

**作者**：Zekai Lin, Chao Xue, Di Liang 等 11 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-04-15

### 📄 论文摘要

Supervised Fine-Tuning (SFT) of large language models often suffers from task interference and catastrophic forgetting. Recent approaches alleviate this issue by isolating task-critical parameters during training. However, these methods represent a static solution to a dynamic problem, assuming that parameter importance remains fixed once identified. In this work, we empirically demonstrate that parameter importance exhibits temporal drift over the course of training. To address this, we propose Evolving Parameter Isolation (EPI), a fine-tuning framework that adapts isolation decisions based on online estimates of parameter importance. Instead of freezing a fixed subset of parameters, EPI periodically updates isolation masks using gradient-based signals, enabling the model to protect emerging task-critical parameters while releasing outdated ones to recover plasticity. Experiments on diverse multi-task benchmarks demonstrate that EPI consistently reduces interference and forgetting compared to static isolation and standard fine-tuning, while improving overall generalization. Our analysis highlights the necessity of synchronizing isolation mechanisms with the evolving dynamics of learning diverse abilities.

### 🤖 AI 总结

**一句话总结**：Supervised Fine-Tuning (SFT) of large language models often suffers from task interference and catastrophic forgetting. Recent approaches alleviate this issue by isolating task-critical parameters dur...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Parameter, Importance, Not, Static, Evolving, Isolation, Supervised, Fine-Tuning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.14010v1) | [下载PDF](https://arxiv.org/pdf/2604.14010v1.pdf)

---

