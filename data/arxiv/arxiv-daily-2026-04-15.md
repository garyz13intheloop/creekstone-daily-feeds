# arXiv AI 论文日报 | 2026-04-15

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (15 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. PAL: Personal Adaptive Learner](https://arxiv.org/abs/2604.13017v1)

**作者**：Megha Chakraborty, Darssan L. Eswaramoorthi, Madhur Thareja 等 8 位作者  
**分类**：cs.AI, cs.HC  
**发布时间**：2026-04-14

### 📄 论文摘要

AI-driven education platforms have made some progress in personalisation, yet most remain constrained to static adaptation--predefined quizzes, uniform pacing, or generic feedback--limiting their ability to respond to learners' evolving understanding. This shortfall highlights the need for systems that are both context-aware and adaptive in real time. We introduce PAL (Personal Adaptive Learner), an AI-powered platform that transforms lecture videos into interactive learning experiences. PAL continuously analyzes multimodal lecture content and dynamically engages learners through questions of varying difficulty, adjusting to their responses as the lesson unfolds. At the end of a session, PAL generates a personalized summary that reinforces key concepts while tailoring examples to the learner's interests. By uniting multimodal content analysis with adaptive decision-making, PAL contributes a novel framework for responsive digital learning. Our work demonstrates how AI can move beyond static personalization toward real-time, individualized support, addressing a core challenge in AI-enabled education.

### 🤖 AI 总结

**一句话总结**：AI-driven education platforms have made some progress in personalisation, yet most remain constrained to static adaptation--predefined quizzes, uniform pacing, or generic feedback--limiting their abil...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PAL, Personal, Adaptive, Learner, AI-driven, education, platforms, have

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.13017v1) | [下载PDF](https://arxiv.org/pdf/2604.13017v1.pdf)

---

## [2. Cycle-Consistent Search: Question Reconstructability as a Proxy Reward for Search Agent Training](https://arxiv.org/abs/2604.12967v1)

**作者**：Sohyun An, Shuibenyang Yuan, Hayeon Lee 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-14

### 📄 论文摘要

Reinforcement Learning (RL) has shown strong potential for optimizing search agents in complex information retrieval tasks. However, existing approaches predominantly rely on gold supervision, such as ground-truth answers, which is difficult to scale. To address this limitation, we propose Cycle-Consistent Search (CCS), a gold-supervision-free framework for training search agents, inspired by cycle-consistency techniques from unsupervised machine translation and image-to-image translation. Our key hypothesis is that an optimal search trajectory, unlike insufficient or irrelevant ones, serves as a lossless encoding of the question's intent. Consequently, a high-quality trajectory should preserve the information required to accurately reconstruct the original question, thereby inducing a reward signal for policy optimization. However, naive cycle-consistency objectives are vulnerable to information leakage, as reconstruction may rely on superficial lexical cues rather than the underlying search process. To reduce this effect, we apply information bottlenecks, including exclusion of the final response and named entity recognition (NER) masking of search queries. These constraints force reconstruction to rely on retrieved observations together with the structural scaffold, ensuring that the resulting reward signal reflects informational adequacy rather than linguistic redundancy. Experiments on question-answering benchmarks show that CCS achieves performance comparable to supervised baselines while outperforming prior methods that do not rely on gold supervision. These results suggest that CCS provides a scalable training paradigm for training search agents in settings where gold supervision is unavailable.

### 🤖 AI 总结

**一句话总结**：Reinforcement Learning (RL) has shown strong potential for optimizing search agents in complex information retrieval tasks. However, existing approaches predominantly rely on gold supervision, such as...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Agent, Cycle-Consistent, Search, Question, Reconstructability, Proxy, Reward

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12967v1) | [下载PDF](https://arxiv.org/pdf/2604.12967v1.pdf)

---

## [3. Modeling Co-Pilots for Text-to-Model Translation](https://arxiv.org/abs/2604.12955v1)

**作者**：Serdar Kadioglu, Karthik Uppuluri, Akash Singirikonda  
**分类**：cs.AI  
**发布时间**：2026-04-14

### 📄 论文摘要

There is growing interest in leveraging large language models (LLMs) for text-to-model translation and optimization tasks. This paper aims to advance this line of research by introducing \textsc{Text2Model} and \textsc{Text2Zinc}. \textsc{Text2Model} is a suite of co-pilots based on several LLM strategies with varying complexity, along with an online leaderboard. \textsc{Text2Zinc} is a cross-domain dataset for capturing optimization and satisfaction problems specified in natural language, along with an interactive editor with built-in AI assistant. While there is an emerging literature on using LLMs for translating combinatorial problems into formal models, our work is the first attempt to integrate \textit{both} satisfaction and optimization problems within a \textit{unified architecture} and \textit{dataset}. Moreover, our approach is \textit{solver-agnostic} unlike existing work that focuses on translation to a solver-specific model. To achieve this, we leverage \textsc{MiniZinc}'s solver-and-paradigm-agnostic modeling capabilities to formulate combinatorial problems. We conduct comprehensive experiments to compare execution and solution accuracy across several single- and multi-call strategies, including; zero-shot prompting, chain-of-thought reasoning, intermediate representations via knowledge-graphs, grammar-based syntax encoding, and agentic approaches that decompose the model into sequential sub-tasks. Our co-pilot strategies are competitive, and in parts improve, recent research in this domain. Our findings indicate that while LLMs are promising they are not yet a push-button technology for combinatorial modeling. We contribute \textsc{Text2Model} co-pilots and leaderboard, and \textsc{Text2Zinc} and interactive editor to open-source to support closing this performance gap.

### 🤖 AI 总结

**一句话总结**：There is growing interest in leveraging large language models (LLMs) for text-to-model translation and optimization tasks. This paper aims to advance this line of research by introducing \textsc{Text2...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Modeling, Co-Pilots, Text-to-Model, Translation, There, growing, interest, leveraging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12955v1) | [下载PDF](https://arxiv.org/pdf/2604.12955v1.pdf)

---

## cs.CL

## [4. Toward Autonomous Long-Horizon Engineering for ML Research](https://arxiv.org/abs/2604.13018v1)

**作者**：Guoxin Chen, Jie Chen, Lei Chen 等 10 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-14

### 📄 论文摘要

Autonomous AI research has advanced rapidly, but long-horizon ML research engineering remains difficult: agents must sustain coherent progress across task comprehension, environment setup, implementation, experimentation, and debugging over hours or days. We introduce AiScientist, a system for autonomous long-horizon engineering for ML research built on a simple principle: strong long-horizon performance requires both structured orchestration and durable state continuity. To this end, AiScientist combines hierarchical orchestration with a permission-scoped File-as-Bus workspace: a top-level Orchestrator maintains stage-level control through concise summaries and a workspace map, while specialized agents repeatedly re-ground on durable artifacts such as analyses, plans, code, and experimental evidence rather than relying primarily on conversational handoffs, yielding thin control over thick state. Across two complementary benchmarks, AiScientist improves PaperBench score by 10.54 points on average over the best matched baseline and achieves 81.82 Any Medal% on MLE-Bench Lite. Ablation studies further show that File-as-Bus protocol is a key driver of performance, reducing PaperBench by 6.41 points and MLE-Bench Lite by 31.82 points when removed. These results suggest that long-horizon ML research engineering is a systems problem of coordinating specialized work over durable project state, rather than a purely local reasoning problem.

### 🤖 AI 总结

**一句话总结**：Autonomous AI research has advanced rapidly, but long-horizon ML research engineering remains difficult: agents must sustain coherent progress across task comprehension, environment setup, implementat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ML, Toward, Autonomous, Long-Horizon, Engineering, Research, has, advanced

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.13018v1) | [下载PDF](https://arxiv.org/pdf/2604.13018v1.pdf)

---

## [5. PolicyLLM: Towards Excellent Comprehension of Public Policy for Large Language Models](https://arxiv.org/abs/2604.12995v1)

**作者**：Han Bao, Penghao Zhang, Yue Huang 等 12 位作者  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-04-14

### 📄 论文摘要

Large Language Models (LLMs) are increasingly integrated into real-world decision-making, including in the domain of public policy. Yet, their ability to comprehend and reason about policy-related content remains underexplored. To fill this gap, we present \textbf{\textit{PolicyBench}}, the first large-scale cross-system benchmark (US-China) evaluating policy comprehension, comprising 21K cases across a broad spectrum of policy areas, capturing the diversity and complexity of real-world governance. Following Bloom's taxonomy, the benchmark assesses three core capabilities: (1) \textbf{Memorization}: factual recall of policy knowledge, (2) \textbf{Understanding}: conceptual and contextual reasoning, and (3) \textbf{Application}: problem-solving in real-life policy scenarios. Building on this benchmark, we further propose \textbf{\textit{PolicyMoE}}, a domain-specialized Mixture-of-Experts (MoE) model with expert modules aligned to each cognitive level. The proposed models demonstrate stronger performance on application-oriented policy tasks than on memorization or conceptual understanding, and yields the highest accuracy on structured reasoning tasks. Our results reveal key limitations of current LLMs in policy understanding and suggest paths toward more reliable, policy-focused models.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) are increasingly integrated into real-world decision-making, including in the domain of public policy. Yet, their ability to comprehend and reason about policy-related con...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, PolicyLLM, Towards, Excellent, Comprehension, Public, Policy, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12995v1) | [下载PDF](https://arxiv.org/pdf/2604.12995v1.pdf)

---

## [6. GlotOCR Bench: OCR Models Still Struggle Beyond a Handful of Unicode Scripts](https://arxiv.org/abs/2604.12978v1)

**作者**：Amir Hossein Kargaran, Nafiseh Nikeghbal, Jana Diesner 等 5 位作者  
**分类**：cs.CL, cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

Optical character recognition (OCR) has advanced rapidly with the rise of vision-language models, yet evaluation has remained concentrated on a small cluster of high- and mid-resource scripts. We introduce GlotOCR Bench, a comprehensive benchmark evaluating OCR generalization across 100+ Unicode scripts. Our benchmark comprises clean and degraded image variants rendered from real multilingual texts. Images are rendered using fonts from the Google Fonts repository, shaped with HarfBuzz and rasterized with FreeType, supporting both LTR and RTL scripts. Samples of rendered images were manually reviewed to verify correct rendering across all scripts. We evaluate a broad suite of open-weight and proprietary vision-language models and find that most perform well on fewer than ten scripts, and even the strongest frontier models fail to generalize beyond thirty scripts. Performance broadly tracks script-level pretraining coverage, suggesting that current OCR systems rely on language model pretraining as much as on visual recognition. Models confronted with unfamiliar scripts either produce random noise or hallucinate characters from similar scripts they already know. We release the benchmark and pipeline for reproducibility. Pipeline Code: https://github.com/cisnlp/glotocr-bench, Benchmark: https://hf.co/datasets/cis-lmu/glotocr-bench.

### 🤖 AI 总结

**一句话总结**：Optical character recognition (OCR) has advanced rapidly with the rise of vision-language models, yet evaluation has remained concentrated on a small cluster of high- and mid-resource scripts. We intr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OCR, GlotOCR, Bench, Models, Still, Struggle, Beyond, Handful

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12978v1) | [下载PDF](https://arxiv.org/pdf/2604.12978v1.pdf)

---

## [7. MoshiRAG: Asynchronous Knowledge Retrieval for Full-Duplex Speech Language Models](https://arxiv.org/abs/2604.12928v1)

**作者**：Chung-Ming Chien, Manu Orsini, Eugene Kharitonov 等 6 位作者  
**分类**：cs.CL, eess.AS  
**发布时间**：2026-04-14

### 📄 论文摘要

Speech-to-speech language models have recently emerged to enhance the naturalness of conversational AI. In particular, full-duplex models are distinguished by their real-time interactivity, including handling of pauses, interruptions, and backchannels. However, improving their factuality remains an open challenge. While scaling the model size could address this gap, it would make real-time inference prohibitively expensive. In this work, we propose MoshiRAG, a modular approach that combines a compact full-duplex interface with selective retrieval to access more powerful knowledge sources. Our asynchronous framework enables the model to identify knowledge-demanding queries and ground its responses in external information. By leveraging the natural temporal gap between response onset and the delivery of core information, the retrieval process can be completed while maintaining a natural conversation flow. With this approach, MoshiRAG achieves factuality comparable to the best publicly released non-duplex speech language models while preserving the interactivity inherent to full-duplex systems. Moreover, our flexible design supports plug-and-play retrieval methods without retraining and demonstrates strong performance on out-of-domain mathematical reasoning tasks.

### 🤖 AI 总结

**一句话总结**：Speech-to-speech language models have recently emerged to enhance the naturalness of conversational AI. In particular, full-duplex models are distinguished by their real-time interactivity, including ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MoshiRAG, Asynchronous, Knowledge, Retrieval, Full-Duplex, Speech, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12928v1) | [下载PDF](https://arxiv.org/pdf/2604.12928v1.pdf)

---

## [8. MetFuse: Figurative Fusion between Metonymy and Metaphor](https://arxiv.org/abs/2604.12919v1)

**作者**：Saptarshi Ghosh, Tianyu Jiang  
**分类**：cs.CL  
**发布时间**：2026-04-14

### 📄 论文摘要

Metonymy and metaphor often co-occur in natural language, yet computational work has studied them largely in isolation. We introduce a framework that transforms a literal sentence into three figurative variants: metonymic, metaphoric, and hybrid. Using this framework, we construct MetFuse, the first dedicated dataset of figurative fusion between metonymy and metaphor, containing 1,000 human-verified meaning-aligned quadruplets totaling 4,000 sentences. Extrinsic experiments on eight existing benchmarks show that augmenting training data with MetFuse consistently improves both metonymy and metaphor classification, with hybrid examples yielding the largest gains on metonymy tasks. Using this dataset, we also analyze how the presence of one figurative type impacts another. Our findings show that both human annotators and large language models better identify metonymy in hybrid sentences than in metonymy-only sentences, demonstrating that the presence of a metaphor makes a metonymic noun more explicit. Our dataset is publicly available at: https://github.com/cincynlp/MetFuse.

### 🤖 AI 总结

**一句话总结**：Metonymy and metaphor often co-occur in natural language, yet computational work has studied them largely in isolation. We introduce a framework that transforms a literal sentence into three figurativ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MetFuse, Figurative, Fusion, between, Metonymy, Metaphor, often, co-occur

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12919v1) | [下载PDF](https://arxiv.org/pdf/2604.12919v1.pdf)

---

## cs.CV

## [9. Lyra 2.0: Explorable Generative 3D Worlds](https://arxiv.org/abs/2604.13036v1)

**作者**：Tianchang Shen, Sherwin Bahmani, Kai He 等 15 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

Recent advances in video generation enable a new paradigm for 3D scene creation: generating camera-controlled videos that simulate scene walkthroughs, then lifting them to 3D via feed-forward reconstruction techniques. This generative reconstruction approach combines the visual fidelity and creative capacity of video models with 3D outputs ready for real-time rendering and simulation. Scaling to large, complex environments requires 3D-consistent video generation over long camera trajectories with large viewpoint changes and location revisits, a setting where current video models degrade quickly. Existing methods for long-horizon generation are fundamentally limited by two forms of degradation: spatial forgetting and temporal drifting. As exploration proceeds, previously observed regions fall outside the model's temporal context, forcing the model to hallucinate structures when revisited. Meanwhile, autoregressive generation accumulates small synthesis errors over time, gradually distorting scene appearance and geometry. We present Lyra 2.0, a framework for generating persistent, explorable 3D worlds at scale. To address spatial forgetting, we maintain per-frame 3D geometry and use it solely for information routing -- retrieving relevant past frames and establishing dense correspondences with the target viewpoints -- while relying on the generative prior for appearance synthesis. To address temporal drifting, we train with self-augmented histories that expose the model to its own degraded outputs, teaching it to correct drift rather than propagate it. Together, these enable substantially longer and 3D-consistent video trajectories, which we leverage to fine-tune feed-forward reconstruction models that reliably recover high-quality 3D scenes.

### 🤖 AI 总结

**一句话总结**：Recent advances in video generation enable a new paradigm for 3D scene creation: generating camera-controlled videos that simulate scene walkthroughs, then lifting them to 3D via feed-forward reconstr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Lyra, Explorable, Generative, Worlds, Recent, advances, video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.13036v1) | [下载PDF](https://arxiv.org/pdf/2604.13036v1.pdf)

---

## [10. SceneCritic: A Symbolic Evaluator for 3D Indoor Scene Synthesis](https://arxiv.org/abs/2604.13035v1)

**作者**：Kathakoli Sengupta, Kai Ao, Paola Cascante-Bonilla  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-04-14

### 📄 论文摘要

Large Language Models (LLMs) and Vision-Language Models (VLMs) increasingly generate indoor scenes through intermediate structures such as layouts and scene graphs, yet evaluation still relies on LLM or VLM judges that score rendered views, making judgments sensitive to viewpoint, prompt phrasing, and hallucination. When the evaluator is unstable, it becomes difficult to determine whether a model has produced a spatially plausible scene or whether the output score reflects the choice of viewpoint, rendering, or prompt. We introduce SceneCritic, a symbolic evaluator for floor-plan-level layouts. SceneCritic's constraints are grounded in SceneOnto, a structured spatial ontology we construct by aggregating indoor scene priors from 3D-FRONT, ScanNet, and Visual Genome. SceneOnto traverses this ontology to jointly verify semantic, orientation, and geometric coherence across object relationships, providing object-level and relationship-level assessments that identify specific violations and successful placements. Furthermore, we pair SceneCritic with an iterative refinement test bed that probes how models build and revise spatial structure under different critic modalities: a rule-based critic using collision constraints as feedback, an LLM critic operating on the layout as text, and a VLM critic operating on rendered observations. Through extensive experiments, we show that (a) SceneCritic aligns substantially better with human judgments than VLM-based evaluators, (b) text-only LLMs can outperform VLMs on semantic layout quality, and (c) image-based VLM refinement is the most effective critic modality for semantic and orientation correction.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) and Vision-Language Models (VLMs) increasingly generate indoor scenes through intermediate structures such as layouts and scene graphs, yet evaluation still relies on LLM ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, SceneCritic, Symbolic, Evaluator, Indoor, Scene, Synthesis, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.13035v1) | [下载PDF](https://arxiv.org/pdf/2604.13035v1.pdf)

---

## [11. Visual Preference Optimization with Rubric Rewards](https://arxiv.org/abs/2604.13029v1)

**作者**：Ya-Qi Yu, Fangyu Hong, Xiangyang Qu 等 18 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-14

### 📄 论文摘要

The effectiveness of Direct Preference Optimization (DPO) depends on preference data that reflect the quality differences that matter in multimodal tasks. Existing pipelines often rely on off-policy perturbations or coarse outcome-based signals, which are not well suited to fine-grained visual reasoning. We propose rDPO, a preference optimization framework based on instance-specific rubrics. For each image-instruction pair, we create a checklist-style rubric of essential and additional criteria to score responses from any possible policies. The instruction-rubric pool is built offline and reused during the construction of on-policy data. On public reward modeling benchmarks, rubric-based prompting massively improves a 30B-A3B judge and brings it close to GPT-5.4. On public downstream benchmarks, rubric-based filtering raises the macro average to 82.69, whereas outcome-based filtering drops it to 75.82 from 81.14. When evaluating scalability on a comprehensive benchmark, rDPO achieves 61.01, markedly outperforming the style-constrained baseline (52.36) and surpassing the 59.48 base model. Together, these results show that visual preference optimization benefits from combining on-policy data construction with instance-specific criterion-level feedback.

### 🤖 AI 总结

**一句话总结**：The effectiveness of Direct Preference Optimization (DPO) depends on preference data that reflect the quality differences that matter in multimodal tasks. Existing pipelines often rely on off-policy p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Visual, Preference, Optimization, Rubric, Rewards, effectiveness, Direct

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.13029v1) | [下载PDF](https://arxiv.org/pdf/2604.13029v1.pdf)

---

## [12. Conflated Inverse Modeling to Generate Diverse and Temperature-Change Inducing Urban Vegetation Patterns](https://arxiv.org/abs/2604.13028v1)

**作者**：Baris Sarper Tezcan, Hrishikesh Viswanath, Rubab Saher 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

Urban areas are increasingly vulnerable to thermal extremes driven by rapid urbanization and climate change. Traditionally, thermal extremes have been monitored using Earth-observing satellites and numerical modeling frameworks. For example, land surface temperature derived from Landsat or Sentinel imagery is commonly used to characterize surface heating patterns. These approaches operate as forward models, translating radiative observations or modeled boundary conditions into estimates of surface thermal states. While forward models can predict land surface temperature from vegetation and urban form, the inverse problem of determining spatial vegetation configurations that achieve a desired regional temperature shift remains largely unexplored. This task is inherently underdetermined, as multiple spatial vegetation patterns can yield similar aggregated temperature responses. Conventional regression and deterministic neural networks fail to capture this ambiguity and often produce averaged solutions, particularly under data-scarce conditions. We propose a conflated inverse modeling framework that combines a predictive forward model with a diffusion-based generative inverse model to produce diverse, physically plausible image-based vegetation patterns conditioned on specific temperature goals. Our framework maintains control over thermal outcomes while enabling diverse spatial vegetation configurations, even when such combinations are absent from training data. Altogether, this work introduces a controllable inverse modeling approach for urban climate adaptation that accounts for the inherent diversity of the problem. Code is available at the GitHub repository.

### 🤖 AI 总结

**一句话总结**：Urban areas are increasingly vulnerable to thermal extremes driven by rapid urbanization and climate change. Traditionally, thermal extremes have been monitored using Earth-observing satellites and nu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Conflated, Inverse, Modeling, Generate, Diverse, Temperature-Change, Inducing, Urban

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.13028v1) | [下载PDF](https://arxiv.org/pdf/2604.13028v1.pdf)

---

## [13. Representation geometry shapes task performance in vision-language modeling for CT enterography](https://arxiv.org/abs/2604.13021v1)

**作者**：Cristian Minoccheri, Emily Wittrup, Kayvan Najarian 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-14

### 📄 论文摘要

Computed tomography (CT) enterography is a primary imaging modality for assessing inflammatory bowel disease (IBD), yet the representational choices that best support automated analysis of this modality are unknown. We present the first study of vision-language transfer learning on abdominal CT enterography and identify two main findings. First, mean pooling of slice embeddings gives better categorical disease assessment (59.2\% three-class accuracy), whereas attention pooling gives better cross-modal retrieval (0.235 text-to-image MRR). This pattern holds across all LoRA configurations tested and suggests that the two aggregators emphasize different properties of the learned representation. Second, per-slice tissue contrast matters more than broader spatial coverage: multi-window RGB encoding, which maps complementary Hounsfield Unit windows to RGB channels, outperforms all strategies that increase spatial coverage through multiplanar sampling, and in this setting adding coronal and sagittal views reduces classification performance. For report generation, fine-tuning without retrieval context yields within-1 severity accuracy at the prevalence-matched chance level (70.4\% vs.\ 71\% random), suggesting little learned ordering beyond the class distribution. Retrieval-augmented generation (RAG) improves this across all configurations, scoring 7--14 percentage points above the chance baseline and improving ordinal MAE from 0.98 to 0.80--0.89. A three-teacher pseudolabel framework enables all comparisons without expert annotations. Together, these findings provide the first baselines for this underexplored modality and offer practical guidance for building vision-language systems for volumetric medical imaging.

### 🤖 AI 总结

**一句话总结**：Computed tomography (CT) enterography is a primary imaging modality for assessing inflammatory bowel disease (IBD), yet the representational choices that best support automated analysis of this modali...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CT, Representation, geometry, shapes, task, performance, vision-language, modeling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.13021v1) | [下载PDF](https://arxiv.org/pdf/2604.13021v1.pdf)

---

## [14. See, Point, Refine: Multi-Turn Approach to GUI Grounding with Visual Feedback](https://arxiv.org/abs/2604.13019v1)

**作者**：Himangi Mittal, Gaurav Mittal, Nelson Daniel Troncoso 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

Computer Use Agents (CUAs) fundamentally rely on graphical user interface (GUI) grounding to translate language instructions into executable screen actions, but editing-level grounding in dense coding interfaces, where sub-pixel accuracy is required to interact with dense IDE elements, remains underexplored. Existing approaches typically rely on single-shot coordinate prediction, which lacks a mechanism for error correction and often fails in high-density interfaces. In this technical report, we conduct an empirical study of pixel-precise cursor localization in coding environments. Instead of a single-step execution, our agent engages in an iterative refinement process, utilizing visual feedback from previous attempts to reach the target element. This closed-loop grounding mechanism allows the agent to self-correct displacement errors and adapt to dynamic UI changes. We evaluate our approach across GPT-5.4, Claude, and Qwen on a suite of complex coding benchmarks, demonstrating that multi-turn refinement significantly outperforms state-of-the-art single-shot models in both click precision and overall task success rate. Our results suggest that iterative visual reasoning is a critical component for the next generation of reliable software engineering agents. Code: https://github.com/microsoft/precision-cua-bench.

### 🤖 AI 总结

**一句话总结**：Computer Use Agents (CUAs) fundamentally rely on graphical user interface (GUI) grounding to translate language instructions into executable screen actions, but editing-level grounding in dense coding...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：See, Point, Refine, Multi-Turn, Approach, GUI, Grounding, Visual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.13019v1) | [下载PDF](https://arxiv.org/pdf/2604.13019v1.pdf)

---

## [15. Agentic Discovery with Active Hypothesis Exploration for Visual Recognition](https://arxiv.org/abs/2604.12999v1)

**作者**：Jaywon Koo, Jefferson Hernandez, Ruozhen He 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

We introduce HypoExplore, an agentic framework that formulates neural architecture discovery for visual recognition as a hypothesis-driven scientific inquiry. Given a human-specified high-level research direction, HypoExplore ideates, implements, evaluates, and improves neural architectures through evolutionary branching. New hypotheses are created using a large language model by selecting a parent hypothesis to build upon, guided by a dual strategy that balances exploiting validated principles with resolving uncertain ones. Our proposed framework maintains a Trajectory Tree that records the lineage of all proposed architectures, and a Hypothesis Memory Bank that actively tracks confidence scores acquired through experimental evidence. After each experiment, multiple feedback agents analyze the results from different perspectives and consolidate their findings into hypothesis confidence updates. Our framework is tested on discovering lightweight vision architectures on CIFAR-10, with the best achieving 94.11% accuracy evolved from a root node baseline that starts at 18.91%, and generalizes to CIFAR-100 and Tiny-ImageNet. We further demonstrate applicability to a specialized domain by conducting independent architecture discovery runs on MedMNIST, which yield a state-of-the-art performance. We show that hypothesis confidence scores grow increasingly predictive as evidence accumulates, and that the learned principles transfer across independent evolutionary lineages, suggesting that HypoExplore not only discovers stronger architectures, but can help build a genuine understanding of the design space.

### 🤖 AI 总结

**一句话总结**：We introduce HypoExplore, an agentic framework that formulates neural architecture discovery for visual recognition as a hypothesis-driven scientific inquiry. Given a human-specified high-level resear...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Agentic, Discovery, Active, Hypothesis, Exploration, Visual, Recognition

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12999v1) | [下载PDF](https://arxiv.org/pdf/2604.12999v1.pdf)

---

## [16. AbdomenGen: Sequential Volume-Conditioned Diffusion Framework for Abdominal Anatomy Generation](https://arxiv.org/abs/2604.12969v1)

**作者**：Yubraj Bhandari, Lavsen Dahal, Paul Segars 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

Computational phantoms are widely used in medical imaging research, yet current systems to generate controlled, clinically meaningful anatomical variations remain limited. We present AbdomenGen, a sequential volume-conditioned diffusion framework for controllable abdominal anatomy generation. We introduce the \textbf{Volume Control Scalar (VCS)}, a standardized residual that decouples organ size from body habitus, enabling interpretable volume modulation. Organ masks are synthesized sequentially, conditioning on the body mask and previously generated structures to preserve global anatomical coherence while supporting independent, multi-organ control. Across 11 abdominal organs, the proposed framework achieves strong geometric fidelity (e.g., liver dice $0.83 \pm 0.05$), stable single-organ calibration over $[-3,+3]$ VCS, and disentangled multi-organ modulation. To showcase clinical utility with a hepatomegaly cohort selected from MERLIN, Wasserstein-based VCS selection reduces distributional distance of training data by 73.6\% . These results demonstrate calibrated, distribution-aware anatomical generation suitable for controllable abdominal phantom construction and simulation studies.

### 🤖 AI 总结

**一句话总结**：Computational phantoms are widely used in medical imaging research, yet current systems to generate controlled, clinically meaningful anatomical variations remain limited. We present AbdomenGen, a seq...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, AbdomenGen, Sequential, Volume-Conditioned, Framework, Abdominal, Anatomy, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12969v1) | [下载PDF](https://arxiv.org/pdf/2604.12969v1.pdf)

---

## [17. Boosting Visual Instruction Tuning with Self-Supervised Guidance](https://arxiv.org/abs/2604.12966v1)

**作者**：Sophia Sirko-Galouchenko, Monika Wysoczanska, Andrei Bursuc 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

Multimodal large language models (MLLMs) perform well on many vision-language tasks but often struggle with vision-centric problems that require fine-grained visual reasoning. Recent evidence suggests that this limitation arises not from weak visual representations, but from under-utilization of visual information during instruction tuning, where many tasks can be partially solved using language priors alone. We propose a simple and lightweight approach that augments visual instruction tuning with a small number of visually grounded self-supervised tasks expressed as natural language instructions. By reformulating classical self-supervised pretext tasks, such as rotation prediction, color matching, and cross-view correspondence, as image-instruction-response triplets, we introduce supervision that cannot be solved without relying on visual evidence. Our approach requires no human annotations, no architectural modifications, and no additional training stages. Across multiple models, training regimes, and benchmarks, injecting only a small fraction (3-10%) of such visually grounded instructions consistently improves performance on vision-centric evaluations. Our findings highlight instruction tuning with visually grounded SSL tasks as a powerful lever for improving visual reasoning in MLLMs through simple adjustments to the training data distribution. Code available at: https://github.com/sirkosophia/V-GIFT

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) perform well on many vision-language tasks but often struggle with vision-centric problems that require fine-grained visual reasoning. Recent evidence suggests...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Boosting, Visual, Instruction, Tuning, Self-Supervised, Guidance, Multimodal, large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12966v1) | [下载PDF](https://arxiv.org/pdf/2604.12966v1.pdf)

---

## [18. Distorted or Fabricated? A Survey on Hallucination in Video LLMs](https://arxiv.org/abs/2604.12944v1)

**作者**：Yiyang Huang, Yitian Zhang, Yizhou Wang 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-14

### 📄 论文摘要

Despite significant progress in video-language modeling, hallucinations remain a persistent challenge in Video Large Language Models (Vid-LLMs), referring to outputs that appear plausible yet contradict the content of the input video. This survey presents a comprehensive analysis of hallucinations in Vid-LLMs and introduces a systematic taxonomy that categorizes them into two core types: dynamic distortion and content fabrication, each comprising two subtypes with representative cases. Building on this taxonomy, we review recent advances in the evaluation and mitigation of hallucinations, covering key benchmarks, metrics, and intervention strategies. We further analyze the root causes of dynamic distortion and content fabrication, which often result from limited capacity for temporal representation and insufficient visual grounding. These insights inform several promising directions for future work, including the development of motion-aware visual encoders and the integration of counterfactual learning techniques. This survey consolidates scattered progress to foster a systematic understanding of hallucinations in Vid-LLMs, laying the groundwork for building robust and reliable video-language systems. An up-to-date curated list of related works is maintained at https://github.com/hukcc/Awesome-Video-Hallucination .

### 🤖 AI 总结

**一句话总结**：Despite significant progress in video-language modeling, hallucinations remain a persistent challenge in Video Large Language Models (Vid-LLMs), referring to outputs that appear plausible yet contradi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：or, LLM, Distorted, Fabricated?, Survey, Hallucination, Video, Despite

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12944v1) | [下载PDF](https://arxiv.org/pdf/2604.12944v1.pdf)

---

## [19. Direct Discrepancy Replay: Distribution-Discrepancy Condensation and Manifold-Consistent Replay for Continual Face Forgery Detection](https://arxiv.org/abs/2604.12941v1)

**作者**：Tianshuo Zhang, Haoyuan Zhang, Siran Peng 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

Continual face forgery detection (CFFD) requires detectors to learn emerging forgery paradigms without forgetting previously seen manipulations. Existing CFFD methods commonly rely on replaying a small amount of past data to mitigate forgetting. Such replay is typically implemented either by storing a few historical samples or by synthesizing pseudo-forgeries from detector-dependent perturbations. Under strict memory budgets, the former cannot adequately cover diverse forgery cues and may expose facial identities, while the latter remains strongly tied to past decision boundaries. We argue that the core role of replay in CFFD is to reinstate the distributions of previous forgery tasks during subsequent training. To this end, we directly condense the discrepancy between real and fake distributions and leverage real faces from the current stage to perform distribution-level replay. Specifically, we introduce Distribution-Discrepancy Condensation (DDC), which models the real-to-fake discrepancy via a surrogate factorization in characteristic-function space and condenses it into a tiny bank of distribution discrepancy maps. We further propose Manifold-Consistent Replay (MCR), which synthesizes replay samples through variance-preserving composition of these maps with current-stage real faces, yielding samples that reflect previous-task forgery cues while remaining compatible with current real-face statistics. Operating under an extremely small memory budget and without directly storing raw historical face images, our framework consistently outperforms prior CFFD baselines and significantly mitigates catastrophic forgetting. Replay-level privacy analysis further suggests reduced identity leakage risk relative to selection-based replay.

### 🤖 AI 总结

**一句话总结**：Continual face forgery detection (CFFD) requires detectors to learn emerging forgery paradigms without forgetting previously seen manipulations. Existing CFFD methods commonly rely on replaying a smal...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Direct, Discrepancy, Replay, Distribution-Discrepancy, Condensation, Manifold-Consistent, Continual, Face

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12941v1) | [下载PDF](https://arxiv.org/pdf/2604.12941v1.pdf)

---

## [20. Task Alignment: A simple and effective proxy for model merging in computer vision](https://arxiv.org/abs/2604.12935v1)

**作者**：Pau de Jorge, César Roberto de Souza, Björn Michele 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

Efficiently merging several models fine-tuned for different tasks, but stemming from the same pretrained base model, is of great practical interest. Despite extensive prior work, most evaluations of model merging in computer vision are restricted to image classification using CLIP, where different classification datasets define different tasks. In this work, our goal is to make model merging more practical and show its relevance on challenging scenarios beyond this specific setting. In most vision scenarios, different tasks rely on trainable and usually heterogeneous decoders. Differently from previous studies with frozen decoders, where merged models can be evaluated right away, the non-trivial cost of decoder training renders hyperparameter selection based on downstream performance impractical. To address this, we introduce the task alignment proxy, and show how it can be used to speed up hyperparameter selection by orders of magnitude while retaining performance. Equipped with the task alignment proxy, we extend the applicability of model merging to multi-task vision models beyond CLIP-based classification.

### 🤖 AI 总结

**一句话总结**：Efficiently merging several models fine-tuned for different tasks, but stemming from the same pretrained base model, is of great practical interest. Despite extensive prior work, most evaluations of m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Task, Alignment, simple, effective, proxy, model, merging, computer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12935v1) | [下载PDF](https://arxiv.org/pdf/2604.12935v1.pdf)

---

## [21. Grasp in Gaussians: Fast Monocular Reconstruction of Dynamic Hand-Object Interactions](https://arxiv.org/abs/2604.12929v1)

**作者**：Ayce Idil Aytekin, Xu Chen, Zhengyang Shen 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

We present Grasp in Gaussians (GraG), a fast and robust method for reconstructing dynamic 3D hand-object interactions from a single monocular video. Unlike recent approaches that optimize heavy neural representations, our method focuses on tracking the hand and the object efficiently, once initialized from pretrained large models. Our key insight is that accurate and temporally stable hand-object motion can be recovered using a compact Sum-of-Gaussians (SoG) representation, revived from classical tracking literature and integrated with generative Gaussian-based initializations. We initialize object pose and geometry using a video-adapted SAM3D pipeline, then convert the resulting dense Gaussian representation into a lightweight SoG via subsampling. This compact representation enables efficient and fast tracking while preserving geometric fidelity. For the hand, we adopt a complementary strategy: starting from off-the-shelf monocular hand pose initialization, we refine hand motion using simple yet effective 2D joint and depth alignment losses, avoiding per-frame refinement of a detailed 3D hand appearance model while maintaining stable articulation. Extensive experiments on public benchmarks demonstrate that GraG reconstructs temporally coherent hand-object interactions on long sequences 6.4x faster than prior work while improving object reconstruction by 13.4% and reducing hand's per-joint position error by over 65%.

### 🤖 AI 总结

**一句话总结**：We present Grasp in Gaussians (GraG), a fast and robust method for reconstructing dynamic 3D hand-object interactions from a single monocular video. Unlike recent approaches that optimize heavy neural...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Grasp, Gaussians, Fast, Monocular, Reconstruction, Dynamic, Hand-Object

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12929v1) | [下载PDF](https://arxiv.org/pdf/2604.12929v1.pdf)

---

## [22. Radar-Camera BEV Multi-Task Learning with Cross-Task Attention Bridge for Joint 3D Detection and Segmentation](https://arxiv.org/abs/2604.12918v1)

**作者**：Ahmet İnanç, Özgür Erkent  
**分类**：cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

Bird's-eye-view (BEV) representations are the dominant paradigm for 3D perception in autonomous driving, providing a unified spatial canvas where detection and segmentation features are geometrically registered to the same physical coordinate system. However, existing radar-camera fusion methods treat these tasks in isolation, missing the opportunity to share complementary information between them: detection features encode object-level geometry that can sharpen segmentation boundaries, while segmentation features provide dense semantic context that can anchor detection. We propose \textbf{CTAB} (Cross-Task Attention Bridge), a bidirectional module that exchanges features between detection and segmentation branches via multi-scale deformable attention in shared BEV space. CTAB is integrated into a multi-task framework with an Instance Normalization-based segmentation decoder and learnable BEV upsampling to provide a more detailed BEV representation. On nuScenes, CTAB improves segmentation on 7 classes over the joint multi-task baseline at essentially neutral detection. On a 4-class subset (drivable area, pedestrian crossing, walkway, vehicle), our joint multi-task model reaches comparable mIoU on 4 classes while simultaneously providing 3D detection.

### 🤖 AI 总结

**一句话总结**：Bird's-eye-view (BEV) representations are the dominant paradigm for 3D perception in autonomous driving, providing a unified spatial canvas where detection and segmentation features are geometrically ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Radar-Camera, BEV, Multi-Task, Learning, Cross-Task, Attention, Bridge, Joint

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12918v1) | [下载PDF](https://arxiv.org/pdf/2604.12918v1.pdf)

---

## [23. M3D-Stereo: A Multiple-Medium and Multiple-Degradation Dataset for Stereo Image Restoration](https://arxiv.org/abs/2604.12917v1)

**作者**：Deqing Yang, Yingying Liu, Qicong Wang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

Image restoration under adverse conditions, such as underwater, haze or fog, and low-light environments, remains a highly challenging problem due to complex physical degradations and severe information loss. Existing datasets are predominantly limited to a single degradation type or heavily rely on synthetic data without stereo consistency, inherently restricting their applicability in real-world scenarios. To address this, we introduce M3D-Stereo, a stereo dataset with 7904 high-resolution image pairs for image restoration research acquired in multiple media with multiple controlled degradation levels. It encompasses four degradation scenarios: underwater scatter, haze/fog, underwater low-light, and haze low-light. Each scenario forms a subset, and is divided into six levels of progressive degradation, allowing fine-grained evaluations of restoration methods with increasing severity of degradation. Collected via a laboratory setup, the dataset provides aligned stereo image pairs along with their pixel-wise consistent clear ground truths. Two restoration tasks, single-level and mixed-level degradation, were performed to verify its validity. M3D-Stereo establishes a better controlled and more realistic benchmark to evaluate image restoration and stereo matching methods in complex degradation environments. It is made public under LGPLv3 license.

### 🤖 AI 总结

**一句话总结**：Image restoration under adverse conditions, such as underwater, haze or fog, and low-light environments, remains a highly challenging problem due to complex physical degradations and severe informatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：M3D-Stereo, Multiple-Medium, Multiple-Degradation, Dataset, Stereo, Image, Restoration, under

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12917v1) | [下载PDF](https://arxiv.org/pdf/2604.12917v1.pdf)

---

## cs.LG

## [24. CLAD: Efficient Log Anomaly Detection Directly on Compressed Representations](https://arxiv.org/abs/2604.13024v1)

**作者**：Benzhao Tang, Shiyu Yang  
**分类**：cs.LG, cs.DB  
**发布时间**：2026-04-14

### 📄 论文摘要

The explosive growth of system logs makes streaming compression essential, yet existing log anomaly detection (LAD) methods incur severe pre-processing overhead by requiring full decompression and parsing. We introduce CLAD, the first deep learning framework to perform LAD directly on compressed byte streams. CLAD bypasses these bottlenecks by exploiting a key insight: normal logs compress into regular byte patterns, while anomalies systematically disrupt them. To extract these multi-scale deviations from opaque bytes, we propose a purpose-built architecture integrating a dilated convolutional byte encoder, a hybrid Transformer--mLSTM, and four-way aggregation pooling. This is coupled with a two-stage training strategy of masked pre-training and focal-contrastive fine-tuning to effectively handle severe class imbalance. Evaluated across five datasets, CLAD achieves a state-of-the-art average F1-score of 0.9909 and outperforms the best baseline by 2.72 percentage points. It delivers superior accuracy while completely eliminating decompression and parsing overheads, offering a robust solution that generalizes to structured streaming compressors.

### 🤖 AI 总结

**一句话总结**：The explosive growth of system logs makes streaming compression essential, yet existing log anomaly detection (LAD) methods incur severe pre-processing overhead by requiring full decompression and par...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CLAD, Efficient, Log, Anomaly, Detection, Directly, Compressed, Representations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.13024v1) | [下载PDF](https://arxiv.org/pdf/2604.13024v1.pdf)

---

## [25. Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation](https://arxiv.org/abs/2604.13010v1)

**作者**：Yecheng Wu, Song Han, Hai Cai  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-14

### 📄 论文摘要

On-policy distillation (OPD) has emerged as an efficient post-training paradigm for large language models. However, standard OPD requires a live teacher inference server throughout training, resulting in substantial infrastructure overhead. In this work, we investigate whether on-policy distillation can be performed offline. A natural approach is to precompute teacher log-probabilities once over SFT rollouts and reuse them during training. In practice, however, this offline variant fails to reliably match the performance of standard OPD. To understand this discrepancy, we identify a previously overlooked condition that is critical for any OPD pipeline, which we term teacher consistency. This condition requires that the same teacher model be used for both supervised fine-tuning and OPD. We show that violating teacher consistency introduces an irreducible gradient bias, causing both offline and online OPD to converge to a suboptimal fixed point regardless of training duration. Building on this insight, we propose Lightning OPD, an offline on-policy distillation framework that enforces teacher consistency by precomputing teacher log-probabilities over SFT rollouts. This design eliminates the need for a live teacher server entirely. We further show that, under teacher consistency, Lightning OPD shares the same optimum as standard OPD, with bounded gradient discrepancy and an implicit regularization effect that helps prevent policy drift. Extensive experiments on mathematical reasoning and code generation demonstrate that Lightning OPD achieves state-of-the-art performance with significantly improved efficiency. Starting from an SFT-initialized Qwen3-8B-Base model, Lightning OPD reaches 69.9% on AIME 2024 in just 30 GPU hours, achieving a 4.0x speedup over standard OPD and substantially lowering the barrier to entry for academic research on LLM post-training.

### 🤖 AI 总结

**一句话总结**：On-policy distillation (OPD) has emerged as an efficient post-training paradigm for large language models. However, standard OPD requires a live teacher inference server throughout training, resulting...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Lightning, OPD, Efficient, Post-Training, Large, Reasoning, Models, Offline

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.13010v1) | [下载PDF](https://arxiv.org/pdf/2604.13010v1.pdf)

---

## [26. Evolution of Optimization Methods: Algorithms, Scenarios, and Evaluations](https://arxiv.org/abs/2604.12968v1)

**作者**：Tong Zhang, Jiangning Zhang, Zhucun Xue 等 12 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

Balancing convergence speed, generalization capability, and computational efficiency remains a core challenge in deep learning optimization. First-order gradient descent methods, epitomized by stochastic gradient descent (SGD) and Adam, serve as the cornerstone of modern training pipelines. However, large-scale model training, stringent differential privacy requirements, and distributed learning paradigms expose critical limitations in these conventional approaches regarding privacy protection and memory efficiency. To mitigate these bottlenecks, researchers explore second-order optimization techniques to surpass first-order performance ceilings, while zeroth-order methods reemerge to alleviate memory constraints inherent to large-scale training. Despite this proliferation of methodologies, the field lacks a cohesive framework that unifies underlying principles and delineates application scenarios for these disparate approaches. In this work, we retrospectively analyze the evolutionary trajectory of deep learning optimization algorithms and present a comprehensive empirical evaluation of mainstream optimizers across diverse model architectures and training scenarios. We distill key emerging trends and fundamental design trade-offs, pinpointing promising directions for future research. By synthesizing theoretical insights with extensive empirical evidence, we provide actionable guidance for designing next-generation highly efficient, robust, and trustworthy optimization methods. The code is available at https://github.com/APRIL-AIGC/Awesome-Optimizer.

### 🤖 AI 总结

**一句话总结**：Balancing convergence speed, generalization capability, and computational efficiency remains a core challenge in deep learning optimization. First-order gradient descent methods, epitomized by stochas...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Evolution, Optimization, Methods, Algorithms, Scenarios, Evaluations, Balancing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12968v1) | [下载PDF](https://arxiv.org/pdf/2604.12968v1.pdf)

---

## [27. An Optimal Sauer Lemma Over $k$-ary Alphabets](https://arxiv.org/abs/2604.12952v1)

**作者**：Steve Hanneke, Qinglin Meng, Shay Moran 等 4 位作者  
**分类**：cs.LG, math.CO, stat.ML  
**发布时间**：2026-04-14

### 📄 论文摘要

The Sauer-Shelah-Perles Lemma is a cornerstone of combinatorics and learning theory, bounding the size of a binary hypothesis class in terms of its Vapnik-Chervonenkis (VC) dimension. For classes of functions over a $k$-ary alphabet, namely the multiclass setting, the Natarajan dimension has long served as an analogue of VC dimension, yet the corresponding Sauer-type bounds are suboptimal for alphabet sizes $k>2$.   In this work, we establish a sharp Sauer inequality for multiclass and list prediction. Our bound is expressed in terms of the Daniely--Shalev-Shwartz (DS) dimension, and more generally with its extension, the list-DS dimension -- the combinatorial parameters that characterize multiclass and list PAC learnability. Our bound is tight for every alphabet size $k$, list size $\ell$, and dimension value, replacing the exponential dependence on $\ell$ in the Natarajan-based bound by the optimal polynomial dependence, and improving the dependence on $k$ as well. Our proof uses the polynomial method. In contrast to the classical VC case, where several direct combinatorial proofs are known, we are not aware of any purely combinatorial proof in the DS setting. This motivates several directions for future research, which are discussed in the paper.   As consequences, we obtain improved sample complexity upper bounds for list PAC learning and for uniform convergence of list predictors, sharpening the recent results of Charikar et al.~(STOC~2023), Hanneke et al.~(COLT~2024), and Brukhim et al.~(NeurIPS~2024).

### 🤖 AI 总结

**一句话总结**：The Sauer-Shelah-Perles Lemma is a cornerstone of combinatorics and learning theory, bounding the size of a binary hypothesis class in terms of its Vapnik-Chervonenkis (VC) dimension. For classes of f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Optimal, Sauer, Lemma, Over, $k$-ary, Alphabets, Sauer-Shelah-Perles

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12952v1) | [下载PDF](https://arxiv.org/pdf/2604.12952v1.pdf)

---

## [28. The Verification Tax: Fundamental Limits of AI Auditing in the Rare-Error Regime](https://arxiv.org/abs/2604.12951v1)

**作者**：Jason Z Wang  
**分类**：cs.LG  
**发布时间**：2026-04-14

### 📄 论文摘要

The most cited calibration result in deep learning -- post-temperature-scaling ECE of 0.012 on CIFAR-100 (Guo et al., 2017) -- is below the statistical noise floor. We prove this is not a failure of the experiment but a law: the minimax rate for estimating calibration error with model error rate epsilon is Theta((Lepsilon/m)^{1/3}), and no estimator can beat it. This "verification tax" implies that as AI models improve, verifying their calibration becomes fundamentally harder -- with the same exponent in opposite directions. We establish four results that contradict standard evaluation practice: (1) self-evaluation without labels provides exactly zero information about calibration, bounded by a constant independent of compute; (2) a sharp phase transition at mepsilon approx 1 below which miscalibration is undetectable; (3) active querying eliminates the Lipschitz constant, collapsing estimation to detection; (4) verification cost grows exponentially with pipeline depth at rate L^K. We validate across five benchmarks (MMLU, TruthfulQA, ARC-Challenge, HellaSwag, WinoGrande; ~27,000 items) with 6 LLMs from 5 families (8B-405B parameters, 27 benchmark-model pairs with logprob-based confidence), 95% bootstrap CIs, and permutation tests. Self-evaluation non-significance holds in 80% of pairs. Across frontier models, 23% of pairwise comparisons are indistinguishable from noise, implying that credible calibration claims must report verification floors and prioritize active querying once gains approach benchmark resolution.

### 🤖 AI 总结

**一句话总结**：The most cited calibration result in deep learning -- post-temperature-scaling ECE of 0.012 on CIFAR-100 (Guo et al., 2017) -- is below the statistical noise floor. We prove this is not a failure of t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Verification, Tax, Fundamental, Limits, Auditing, Rare-Error, Regime

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12951v1) | [下载PDF](https://arxiv.org/pdf/2604.12951v1.pdf)

---

## [29. Parcae: Scaling Laws For Stable Looped Language Models](https://arxiv.org/abs/2604.12946v1)

**作者**：Hayden Prairie, Zachary Novack, Taylor Berg-Kirkpatrick 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-14

### 📄 论文摘要

Traditional fixed-depth architectures scale quality by increasing training FLOPs, typically through increased parameterization, at the expense of a higher memory footprint, or data. A potential alternative is looped architectures, which instead increase FLOPs by sending activations through a block of layers in a loop. While promising, existing recipes for training looped architectures can be unstable, suffering from residual explosion and loss spikes. We address these challenges by recasting looping as a nonlinear time-variant dynamical system over the residual stream. Via a linear approximation to this system, we find that instability occurs in existing looped architectures as a result of large spectral norms in their injection parameters. To address these instability issues, we propose Parcae, a novel stable, looped architecture that constrains the spectral norm of the injection parameters via discretization of a negative diagonal parameterization. As a result, Parcae achieves up to 6.3% lower validation perplexity over prior large-scale looped models. Using our stable looped architecture, we investigate the scaling properties of looping as a medium to improve quality by increasing FLOPs in training and test-time. For training, we derive predictable power laws to scale FLOPs while keeping parameter count fixed. Our initial scaling laws suggest that looping and data should be increased in tandem, given a fixed FLOP budget. At test-time, we find that Parcae can use looping to scale compute, following a predictable, saturating exponential decay. When scaled up to 1.3B parameters, we find that Parcae improves CORE and Core-Extended quality by 2.99 and 1.18 points when compared to strong Transformer baselines under a fixed parameter and data budget, achieving a relative quality of up to 87.5% a Transformer twice the size.

### 🤖 AI 总结

**一句话总结**：Traditional fixed-depth architectures scale quality by increasing training FLOPs, typically through increased parameterization, at the expense of a higher memory footprint, or data. A potential altern...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Parcae, Scaling, Laws, Stable, Looped, Language, Models, Traditional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12946v1) | [下载PDF](https://arxiv.org/pdf/2604.12946v1.pdf)

---

## [30. Adaptive Data Dropout: Towards Self-Regulated Learning in Deep Neural Networks](https://arxiv.org/abs/2604.12945v1)

**作者**：Amar Gahir, Varshil Patel, Shreyank N Gowda  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-04-14

### 📄 论文摘要

Deep neural networks are typically trained by uniformly sampling large datasets across epochs, despite evidence that not all samples contribute equally throughout learning. Recent work shows that progressively reducing the amount of training data can improve efficiency and generalization, but existing methods rely on fixed schedules that do not adapt during training. In this work, we propose Adaptive Data Dropout, a simple framework that dynamically adjusts the subset of training data based on performance feedback. Inspired by self-regulated learning, our approach treats data selection as an adaptive process, increasing or decreasing data exposure in response to changes in training accuracy. We introduce a lightweight stochastic update mechanism that modulates the dropout schedule online, allowing the model to balance exploration and consolidation over time. Experiments on standard image classification benchmarks show that our method reduces effective training steps while maintaining competitive accuracy compared to static data dropout strategies. These results highlight adaptive data selection as a promising direction for efficient and robust training. Code will be released.

### 🤖 AI 总结

**一句话总结**：Deep neural networks are typically trained by uniformly sampling large datasets across epochs, despite evidence that not all samples contribute equally throughout learning. Recent work shows that prog...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Adaptive, Data, Dropout, Towards, Self-Regulated, Learning, Deep, Neural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.12945v1) | [下载PDF](https://arxiv.org/pdf/2604.12945v1.pdf)

---

