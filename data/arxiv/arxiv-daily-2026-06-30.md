# arXiv AI 论文日报 | 2026-06-30

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.AI](#csAI) (5 篇)
- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.CL](#csCL) (4 篇)

---

## cs.AI

## [1. Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639v1)

**作者**：Xuan Zhang, Wenxuan Zhang, See-Kiong Ng 等 4 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-06-29

### 📄 论文摘要

World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution. However, unreliable foresight can be ignored, misused, or even degrade downstream decision-making. In this paper, we introduce WorldEvolver, a self-evolving world model framework that revises its deployment-time context while keeping the downstream agent and all model parameters frozen. WorldEvolver integrates three modules: (i) Episodic Memory, which exploits real action transitions through retrieval-based simulation; (ii) Semantic Memory, which extracts persistent heuristic rules from prediction-observation mismatches; and (iii) Selective Foresight, which filters low-confidence predictions before integrating them into agent reasoning context. We evaluate WorldEvolver on ALFWorld and ScienceWorld, measuring world model prediction accuracy on Word2World and downstream agent success rate on AgentBoard. Extensive experiments show that WorldEvolver achieves the highest prediction accuracy across three backbones and leads other world model baselines on downstream agent success rate, demonstrating that test-time memory revision enhances both predictive fidelity and planning performance.

### 🤖 AI 总结

**一句话总结**：World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution. However, unreliable foresight can be ignored, misused, or even...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, Self-Evolving, World, Models, Planning, offer, principled

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30639v1) | [下载PDF](https://arxiv.org/pdf/2606.30639v1.pdf)

---

## [2. The Human Creativity Benchmark](https://arxiv.org/abs/2606.30561v1)

**作者**：Aspen Hopkins, Allison Nulty, Alexandria Minetti 等 5 位作者  
**分类**：cs.AI, cs.CV, cs.HC  
**发布时间**：2026-06-29

### 📄 论文摘要

Modern AI evaluation frameworks treat evaluator disagreement as noise to be resolved. In creative domains, professional disagreement reflects genuine differences in taste, not measurement error. We argue that evaluating creative AI requires preserving two distinct signals: convergence, where professionals align around shared best practices, and divergence, where individual taste legitimately varies. We present the Human Creativity Benchmark (HCB), a benchmark that operationalizes this separation by collecting pairwise preferences, scalar ratings on prompt adherence, usability, and visual appeal, and qualitative rationale from domain professionals. Across 15,000 professional judgments spanning five creative domains and three workflow phases (ideation, mockup, refinement), we find that convergence concentrates on verifiable dimensions like technical correctness and visual hierarchy, while divergence concentrates on taste-driven dimensions like aesthetic direction and conceptual risk. No model excels uniformly across all phases. Collapsing these signals into a single quality metric discards the most actionable information: where models must be correct versus where they should remain steerable.

### 🤖 AI 总结

**一句话总结**：Modern AI evaluation frameworks treat evaluator disagreement as noise to be resolved. In creative domains, professional disagreement reflects genuine differences in taste, not measurement error. We ar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Human, Creativity, Benchmark, Modern, evaluation, frameworks, treat, evaluator

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30561v1) | [下载PDF](https://arxiv.org/pdf/2606.30561v1.pdf)

---

## [3. Linguistic Firewall: Geometry as Defense in Multi-Agent Systems Routing](https://arxiv.org/abs/2606.30555v1)

**作者**：Dvir Alsheich, Adar Peleg, Ben Hagag 等 6 位作者  
**分类**：cs.AI, cs.MA  
**发布时间**：2026-06-29

### 📄 论文摘要

The rapid integration of Large Language Models (LLMs) has driven the evolution of Multi-Agent Systems (MAS), where specialized agents collaborate to execute complex workflows. Effective orchestration in these environments requires robust routing mechanisms to efficiently allocate tasks to the most suitable agent. However, existing routers fundamentally rely on unverified proxies, ranging from textual self-descriptions to static surrogate representations, to gauge an agent's competence. This reliance on non-empirical data creates a critical gap between an agent's projected profile and its actual operational capabilities, introducing severe security vulnerabilities. Malicious agents can easily misrepresent their proficiencies or harbor covert backdoors that evade both standard external analysis and static representation-learning techniques. In this work, we introduce ANTAP (Automatic Non-Textual Agent Picker), an evaluation-driven routing architecture that discards indirect proxies in favor of active capability testing. By dynamically querying agents to ascertain their true competencies empirically, ANTAP distills performance into fixed behavioral operators within a shared semantic space. At inference time, routing is performed via a purely non-textual algebraic projection, establishing a "linguistic firewall" that renders metadata-based attacks inexpressible. In our experiments, ANTAP achieves near-zero ASR against description-based injection attacks, compared to 67.3\% and above for the description-based router baseline. Against adaptive embedding attacks, ANTAP achieves substantially lower ASR than the embedding-based baseline, with a 20\% reduction, while remaining resilient to description manipulation by design.

### 🤖 AI 总结

**一句话总结**：The rapid integration of Large Language Models (LLMs) has driven the evolution of Multi-Agent Systems (MAS), where specialized agents collaborate to execute complex workflows. Effective orchestration ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Multi-Agent, Linguistic, Firewall, Geometry, Defense, Systems, Routing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30555v1) | [下载PDF](https://arxiv.org/pdf/2606.30555v1.pdf)

---

## [4. Latent Actions from Factorized Transition Effects under Agent Ambiguity](https://arxiv.org/abs/2606.30544v1)

**作者**：Heejeong Nam, Chandradithya S Jonnalagadda, Harshit Aggarwal 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-29

### 📄 论文摘要

Latent Action Models (LAMs) learn action-like proxies from observation transitions. However, in multi-object or distractor-rich scenes, these visual effects mix agent motion with distractors, camera dynamics, and background changes, making the underlying action source ambiguous without supervision. Structuring this mixture as reusable transition effects provides an intermediate representation from which action-like latents can be more robustly formed. We introduce Observed Transition Factorization (OTF), which decomposes each transition into a sparse set of observed transition primitives. Using these primitives as the transition interface, we propose OTF-LAM, which abstracts motion primitives into action-like latents within the standard inverse-forward dynamics framework, and OTF-LAM-Dino, a decoder-free variant that predicts future states in a frozen DINOv2 representation space. Empirically, OTF primitives transfer zeroshot across controlled carrier and morphology shifts, showing reusability. Furthermore, downstream policy learning results match or outperform baselines under complex transition ambiguity.

### 🤖 AI 总结

**一句话总结**：Latent Action Models (LAMs) learn action-like proxies from observation transitions. However, in multi-object or distractor-rich scenes, these visual effects mix agent motion with distractors, camera d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Latent, Actions, Factorized, Transition, Effects, under, Ambiguity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30544v1) | [下载PDF](https://arxiv.org/pdf/2606.30544v1.pdf)

---

## [5. Entity Binding Failures in Tool-Augmented Agents](https://arxiv.org/abs/2606.30531v1)

**作者**：Rahul Suresh Babu, Shashank Indukuri  
**分类**：cs.AI  
**发布时间**：2026-06-29

### 📄 论文摘要

Tool-augmented language-model agents are often evaluated by whether they select the correct tool, produce valid API arguments, and complete the requested task. However, an agent may choose the right tool and still act on the wrong external entity. For example, a request to "email Alex about the launch" may lead the agent to contact the wrong Alex, attach the wrong launch document, reply in the wrong thread, or update the wrong customer account. We call these errors entity binding failures. This paper studies entity binding failures as a distinct reliability and safety problem in tool-augmented agents. We formalize the separation between tool correctness and entity correctness, introduce a taxonomy of wrong-entity failures in enterprise workflows, and evaluate entity-aware execution mechanisms including entity-resolution preconditions, confidence-gated binding, clarification under ambiguity, and provenance tracking. In a controlled diagnostic evaluation across 60 tasks, five model backends, and six tool-use methods, all methods achieved 0.0 percent wrong-tool error, yet action-oriented baselines still produced wrong-entity actions in 24.0-26.0 percent of runs. Entity-aware methods eliminated wrong-entity actions and risk-weighted wrong-entity exposure in this setting, but reduced direct task completion by deferring under ambiguity. These findings show that safe tool use requires not only selecting the correct tool, but also reliably binding natural-language references to the correct real-world entity before action.

### 🤖 AI 总结

**一句话总结**：Tool-augmented language-model agents are often evaluated by whether they select the correct tool, produce valid API arguments, and complete the requested task. However, an agent may choose the right t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Entity, Binding, Failures, Tool-Augmented, language-model, often, evaluated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30531v1) | [下载PDF](https://arxiv.org/pdf/2606.30531v1.pdf)

---

## cs.CL

## [6. Uncertainty-Aware Generation and Decision-Making Under Ambiguity](https://arxiv.org/abs/2606.30578v1)

**作者**：Nico Daheim, Iryna Gurevych  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-06-29

### 📄 论文摘要

With rapidly improving capabilities, Large Language Models (LLMs) are increasingly used in many complex real-world tasks. Beyond requiring in-depth knowledge and reasoning skills, many of these tasks exhibit a high degree of subjectivity and require that the outputs of the model can be trusted. While a lot of progress has been made to train better models, decision-making algorithms have received less attention. In this work, we present and evaluate various uncertainty-aware decision-making algorithms based on Bayesian decision theory and risk-averse decision making on the tasks of tutoring and automatic peer reviewing. Concretely, we take uncertainty over tutoring strategies and review scores into account when generating a tutor response or review and use conformal prediction to provide guarantees over strategy and score. We find empirically that these algorithms can improve the utility of the generations but need to be carefully implemented when ambiguity is high. For example, risk-averse rules can degrade performance by optimizing for generic outputs, while Bayesian methods tend to perform better. Our work uses techniques from decision theory to improve LLM-based decision-making and outlines open challenges for the community.

### 🤖 AI 总结

**一句话总结**：With rapidly improving capabilities, Large Language Models (LLMs) are increasingly used in many complex real-world tasks. Beyond requiring in-depth knowledge and reasoning skills, many of these tasks ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Uncertainty-Aware, Generation, Decision-Making, Under, Ambiguity, rapidly, improving, capabilities

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30578v1) | [下载PDF](https://arxiv.org/pdf/2606.30578v1.pdf)

---

## [7. Morphing into Hybrid Attention Models](https://arxiv.org/abs/2606.30562v1)

**作者**：Disen Lan, Jianbin Zheng, Yuxi Ren 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-29

### 📄 论文摘要

Hybrid attention models improve long-context efficiency by retaining only a subset of full-attention layers and replacing the remaining layers with linear attention. However, the effectiveness of Transformer-to-hybrid conversion critically depends on which layers preserve full attention. Existing hybrid layer selection methods typically rely on heuristic strategies such as fixed placement patterns or layerwise scoring, implicitly treating layer importance as isolated and overlooking the interdependent layer effect under a global hybrid configuration. In this work, we formulate hybrid layer selection as a budget-constrained subset optimization problem. We further propose FlashMorph (Fast LAyer Selection for Hybrid MORPHing), an effective, efficient and scalable layer selection method for Transformer-to-hybrid conversion. FlashMorph first constructs a morphable model by equipping each full-attention layer with a converted linear-attention branch. It then freezes all model weights and jointly optimizes layerwise gates on synthetic long-context retrieval data, with a linearization regularization that encourages the model to rely on linear attention for efficiency. The learned gates are discretized under a preset full-attention budget to instantiate the hybrid architecture, followed by standard logits distillation and long-context finetuning. Extensive experiments show that FlashMorph discovers more effective hybrid configurations, preserves strong long-context recall and general benchmark performance while substantially reducing layer selection cost compared with existing layer selection methods, demonstrating its effectiveness, efficiency, and scalability.

### 🤖 AI 总结

**一句话总结**：Hybrid attention models improve long-context efficiency by retaining only a subset of full-attention layers and replacing the remaining layers with linear attention. However, the effectiveness of Tran...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Morphing, Hybrid, Attention, Models, improve, long-context, efficiency, retaining

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30562v1) | [下载PDF](https://arxiv.org/pdf/2606.30562v1.pdf)

---

## [8. Poller: Are LLMs Suitable for Evaluating the Poetry Understanding Task?](https://arxiv.org/abs/2606.30556v1)

**作者**：Shanshan Wang, Derek F. Wong, Jingming Yao 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-29

### 📄 论文摘要

Traditional automatic evaluation methods have been shown to be unsuitable for modern Chinese poetry because of the distinct nature of this literary genre. Human evaluation remains reliable, but is expensive and not applicable to large-scale data. In this paper, we propose Poller (Poetry LLM Evaluator), a novel method leveraging large language models (LLMs) to evaluate the poetry understanding task. Specifically, our method requires LLMs to play the role of a poem's author with detailed information, thereby emulating human evaluation and judgment by adopting the poet's perspective. We conducted comprehensive experiments on multiple LLMs, evaluating the interpretations of poems across eight specialized dimensions. Experimental results demonstrate that our method effectively reduces the evaluation error between LLMs and humans. Especially for specific dimension evaluation, Poller-based LLMs achieve a 94.55% and 89.53% error reduction for rhetorical techniques and defamiliarization, respectively, compared to baseline methods. These performances are unattainable by conventional LLM evaluation methods. Experimental results from multiple LLMs across various dimensions validate the efficacy of our method. This work bridges the gap between automated efficiency and human expertise, establishing a foundation for automated evaluation in poetry-related tasks.

### 🤖 AI 总结

**一句话总结**：Traditional automatic evaluation methods have been shown to be unsuitable for modern Chinese poetry because of the distinct nature of this literary genre. Human evaluation remains reliable, but is exp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Poller, Suitable, Evaluating, Poetry, Understanding, Task?, Traditional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30556v1) | [下载PDF](https://arxiv.org/pdf/2606.30556v1.pdf)

---

## [9. TRACE: Temporal Relationship-Aware Conversational Entrainment Detection in Dyadic Speech](https://arxiv.org/abs/2606.30543v1)

**作者**：Sathvik Manikantan Napa Ugandhar, Hao Zhang, Alison Gunzler 等 8 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-29

### 📄 论文摘要

With the proliferation of speech AI agents, understanding emotional entrainment in conversational interaction has become increasingly important. Emotional entrainment is shaped by social relationships and conversational context, influencing affective coordination over time. We introduce DyadEE, a dataset for emotional entrainment detection in dyadic speech interactions, containing both emotionally entrained conversations and synthetic interactions where entrainment is disrupted through partner swapping and emotion resynthesis. We further propose TRACE, a window-level framework that models dyadic interaction as ordered sequences of acoustic embeddings derived from emotion fine-tuned Whisper representations, treating each sample as an interaction trace rather than pooled utterances. Experimental results on DyadEE show that incorporating conversational context and relationship information improves emotional entrainment detection, with TRACE achieving the best accuracy of 97.01%.

### 🤖 AI 总结

**一句话总结**：With the proliferation of speech AI agents, understanding emotional entrainment in conversational interaction has become increasingly important. Emotional entrainment is shaped by social relationships...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TRACE, Temporal, Relationship-Aware, Conversational, Entrainment, Detection, Dyadic, Speech

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30543v1) | [下载PDF](https://arxiv.org/pdf/2606.30543v1.pdf)

---

## cs.CV

## [10. Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors](https://arxiv.org/abs/2606.30638v1)

**作者**：Jameel Hassan, Yasiru Ranasinghe, Vishal Patel  
**分类**：cs.CV  
**发布时间**：2026-06-29

### 📄 论文摘要

3D Gaussian Splatting (3DGS) has emerged at the forefront of 3D scene reconstruction. Extending 3DGS with language-driven, open-vocabulary understanding has gained significant attention for real-world applications such as embodied AI. Recent methods achieve this by learning an instance feature attribute and assigning semantics by distilling high-dimensional Contrastive Language-Image Pretraining (CLIP) features directly into the scene representation. However, the instance grouping mechanisms of these methods either require a predefined number of instances or suffer from noise in their bottom-up grouping strategies. Furthermore, the reliance on CLIP restricts semantic understanding to simple noun phrases, preventing complex spatial reasoning and referential expression grounding. We present GaussDet, a method that circumvents the need for dense CLIP features by leveraging discrete, open-vocabulary 2D object detectors with referring expression capabilities. We learn instance features for individual Gaussians to decompose the scene into 3D instance groups. By rendering these groups and aggregating semantic votes from multi-view 2D detections, we generate a robust View-Aggregated Semantic Label Distribution (VASD) for each 3D instance. This view-aggregation strategy acts as a strong regularizer, attenuating spurious labels caused by low-quality instance grouping. Our approach enables a straightforward, zero-shot extension from simple language queries to complex referential grounding. Extensive evaluations across two key tasks -- open-vocabulary segmentation (LeRF-OVS, ScanNet) and referring expression grounding (Ref-LeRF) -- demonstrate that GaussDet achieves consistent improvements over existing methods. Most notably, we achieve a substantial 16.7% mIoU improvement in referential grounding within a strict zero-shot setting.

### 🤖 AI 总结

**一句话总结**：3D Gaussian Splatting (3DGS) has emerged at the forefront of 3D scene reconstruction. Extending 3DGS with language-driven, open-vocabulary understanding has gained significant attention for real-world...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, 2D, Open-Vocabulary, Referring, Segmentation, Gaussians, Detectors, Gaussian

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30638v1) | [下载PDF](https://arxiv.org/pdf/2606.30638v1.pdf)

---

## [11. Reweighting Framewise Attention in Video Transformers for Facial Expression Understanding](https://arxiv.org/abs/2606.30611v1)

**作者**：Seongro Yoon, Donghyeon Cho, Jinsun Park 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-29

### 📄 论文摘要

Understanding facial expressions in videos requires modeling subtle and localized facial dynamics under unconstrained conditions. Although recent Vision Transformer~(ViT)-based video models have shown strong performance through large-scale self-supervised pretraining, their attention mechanisms often emphasize dominant global motions and coarse temporal dynamics, limiting sensitivity to fine-grained facial variations. To address this limitation, we propose MiRA (Marginal-induced Attention Redistribution), a plug-in frame-marginal attention redistribution framework for ViT backbones that enhances spatio-temporal selectivity toward subtle facial dynamics without introducing additional trainable parameters. MiRA derives frame-level confidence and intra-frame concentration statistics from self-attention maps to estimate frame-wise marginal importance and redistribute attention toward spatiotemporally localized facial cues. We first introduce a principled \textit{exact mode} based on post-softmax attention redistribution. To further improve efficiency, we propose \textit{flashLite mode}, a lightweight pre-softmax approximation that integrates frame-marginal redistribution into FlashAttention kernels while preserving the effectiveness of the exact formulation. Experimental results on challenging Facial Expression Recognition~(FER) benchmarks demonstrate consistent improvements over strong ViT baselines.

### 🤖 AI 总结

**一句话总结**：Understanding facial expressions in videos requires modeling subtle and localized facial dynamics under unconstrained conditions. Although recent Vision Transformer~(ViT)-based video models have shown...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Reweighting, Framewise, Attention, Video, Transformers, Facial, Expression, Understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30611v1) | [下载PDF](https://arxiv.org/pdf/2606.30611v1.pdf)

---

## [12. UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image](https://arxiv.org/abs/2606.30608v1)

**作者**：Mohamed el amine boudjoghra, Ivan Laptev, Angela Dai  
**分类**：cs.CV  
**发布时间**：2026-06-29

### 📄 论文摘要

Articulated 3D objects are essential for interactive environments in embodied AI, robotics, and virtual reality, but reconstructing their structure and motion from sparse observations remains challenging. Existing approaches remain largely constrained by lack of supervised data or lack the priors needed to reliably recover articulation, hidden geometry, and internal object structure. We present the first debate-driven agentic approach to articulated 3D object reconstruction from text or image inputs that both grounds articulation reasoning in concrete motion and exposes the occluded geometry revealed under articulation. High-level agents reason about object semantics and motion using knowledge from vision-language and video models, while low-level agents estimate articulation parameters and interaction points; together, they engage in a two-round structured debate that first exploits global--local disagreement and then grounds the agents in freely generated video. The same video prior, conditioned on the agreed articulation, then drives each part through its motion to expose occluded interiors and geometry that cannot be inferred from a single static view. By combining agentic reasoning with a video generative prior, our approach jointly infers articulation and reconstructs complete 3D articulated objects, producing high-fidelity geometry, internal structure, and motion-consistent states beyond directly observed surfaces.

### 🤖 AI 总结

**一句话总结**：Articulated 3D objects are essential for interactive environments in embodied AI, robotics, and virtual reality, but reconstructing their structure and motion from sparse observations remains challeng...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, 3D, UnfoldArt, Zero-Shot, Recovery, Full, Articulated, Objects

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30608v1) | [下载PDF](https://arxiv.org/pdf/2606.30608v1.pdf)

---

## [13. Goku: A Million-Scale Universal Dataset and Benchmark for Instruction-Based Video Editing](https://arxiv.org/abs/2606.30599v1)

**作者**：Sen Liang, Cong Wang, Zhentao Yu 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-29

### 📄 论文摘要

Existing instruction-based video editing datasets commonly focus on single-task appearance editing, failing to meet the complex creative demands of real-world scenarios. To bridge this gap, we present Goku, a large-scale dataset featuring 2 million high-quality, instruction-aligned video editing pairs, which is the first to extend task boundaries from basic appearance editing to multi-task and structural manipulations(e.g., precise control of subject movement). To tackle the data synthesis challenges inherent in these complex tasks, we design an efficient data synthesis pipeline that decomposes complex edits into controllable sub-problems and introduce a progressive filtering system for data reliability throughout the whole process. Furthermore, we explore the optimal network structures on Goku, and propose Goku-Edit. To deeply comprehend complex editing instructions, Goku-Edit leverages an MLLM as its text encoder and adopts a decoupled dual-branch design: a dedicated mask branch handles structural control, freeing the main branch for appearance rendering. A comprehensive video editing benchmark, Goku-Bench, is also proposed with 1,000 human-verified test cases and 7 novel editing-specific metrics. Evaluated on Goku-Bench, Goku-Edit obtains up to +8% improvement on other open-source models in terms of instruction following.

### 🤖 AI 总结

**一句话总结**：Existing instruction-based video editing datasets commonly focus on single-task appearance editing, failing to meet the complex creative demands of real-world scenarios. To bridge this gap, we present...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Goku, Million-Scale, Universal, Dataset, Benchmark, Instruction-Based, Video, Editing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30599v1) | [下载PDF](https://arxiv.org/pdf/2606.30599v1.pdf)

---

## [14. Towards in-the-wild Egocentric 3D Hand-Object Pose Estimation](https://arxiv.org/abs/2606.30598v1)

**作者**：Siddhant Bansal, Zhifan Zhu, Shashank Tripathi 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-29

### 📄 论文摘要

Estimating accurate 3D hand-object pose from in-the-wild egocentric RGB remains challenging due to severe occlusions and ambiguous contact. Existing learning-based methods often struggle to generalise to in-the-wild scenes and are limited by the scarcity of supervision. We address these issues with two contributions. First, we introduce EPIC-Contact, an in-the-wild egocentric dataset of 2.3K clips (62.3K frames) with dense, bijective 3D hand-object contact correspondences and posed meshes. Second, we propose HOPformer, an end-to-end transformer that jointly predicts bi-manual hand and object pose in a single forward pass. A cross-attention decoder conditions object features on hand priors, producing robust pose estimation. We test HOPformer on the in-lab 3D dataset, ARCTIC, as well as our newly introduced EPIC-Contact dataset. HOPformer reaches 82.4% success rate on ARCTIC (+6.2 pts over current SOTA). On EPIC-Contact, it nearly doubles the success rate while reducing contact deviation by 75%. EPIC-Contact, HOPformer code and checkpoints are released: https://sid2697.github.io/epic-contact.

### 🤖 AI 总结

**一句话总结**：Estimating accurate 3D hand-object pose from in-the-wild egocentric RGB remains challenging due to severe occlusions and ambiguous contact. Existing learning-based methods often struggle to generalise...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Towards, in-the-wild, Egocentric, Hand-Object, Pose, Estimation, Estimating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30598v1) | [下载PDF](https://arxiv.org/pdf/2606.30598v1.pdf)

---

## [15. Learning from Reliable Latent Prompts for Visual Recognition with Missing Modalities](https://arxiv.org/abs/2606.30597v1)

**作者**：Taixi Chen, Nancy Guo  
**分类**：cs.CV  
**发布时间**：2026-06-29

### 📄 论文摘要

Large-scale multimodal models (LMMs) have achieved superior performance in visual recognition by synergizing information across diverse, massive-scale paired modalities. In real-world scenarios, however, missing-modality inputs are ubiquitous, causing models optimized for modality-complete data to exhibit precipitous performance degradation. Existing research has introduced prompt learning to mitigate this issue, typically by generating dynamic prompts from instance-level features, regardless of whether the input modalities are complete or partially absent. However, such input-conditioned strategies are hindered by the escalating unreliability of instance-level features; as higher missing rates increase the proportion of incomplete modalities, the resulting instability in prompt learning limits the model's performance. To address this limitation, we hypothesize that learnable latent prompts themselves encapsulate stable, modality-intrinsic priors that are decoupled from corrupted inputs. Consequently, we propose a novel paradigm: Learning from Reliable Latent Prompts. Unlike prior methods, we model input-agnostic learnable prompts as stable latent anchors that enable robust guidance and effective cross-modal knowledge compensation, even under extreme missing rates (e.g., 90%). Empirical results across three benchmark datasets demonstrate that our "learn-from-latent-prompts" approach achieves state-of-the-art performance across a wide range of missing-modality scenarios. Extensive experiments further confirm the effectiveness of this paradigm in providing a robust solution to the missing-modality problem.

### 🤖 AI 总结

**一句话总结**：Large-scale multimodal models (LMMs) have achieved superior performance in visual recognition by synergizing information across diverse, massive-scale paired modalities. In real-world scenarios, howev...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Reliable, Latent, Prompts, Visual, Recognition, Missing, Modalities

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30597v1) | [下载PDF](https://arxiv.org/pdf/2606.30597v1.pdf)

---

## [16. APRIL-MedSeg: A Modular Medical Image Segmentation Toolbox Embracing Modern Paradigms](https://arxiv.org/abs/2606.30577v1)

**作者**：Juntao Jiang, Jinsheng Bai, Linxuan Fan 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-29

### 📄 论文摘要

We present APRIL-MedSeg, a YAML-driven modular framework for 2D medical image segmentation. It provides a unified and extensible ecosystem that decomposes segmentation networks into reusable components. Also, the framework integrates a broad spectrum of advanced paradigms, including semi-supervised learning, domain adaptation, knowledge distillation, weakly supervised learning, and text-guided segmentation as well as foundation model support. A registry-based configuration system with inheritance enables flexible and reproducible experiment management, supporting seamless switching across models, datasets, and training strategies. In addition, the framework provides a unified interface for medical datasets, augmentation pipelines, deployment utilities and model ensembling. Overall, APRIL-MedSeg is designed as a general-purpose research and development platform that bridges algorithmic innovation and practical deployment, while also serving as a structured ecosystem for systematically organizing and reproducing advances in medical image segmentation. The code is available at https://github.com/juntaoJianggavin/APRIL-MedSeg under an Apache 2.0 license.

### 🤖 AI 总结

**一句话总结**：We present APRIL-MedSeg, a YAML-driven modular framework for 2D medical image segmentation. It provides a unified and extensible ecosystem that decomposes segmentation networks into reusable component...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：APRIL-MedSeg, Modular, Medical, Image, Segmentation, Toolbox, Embracing, Modern

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30577v1) | [下载PDF](https://arxiv.org/pdf/2606.30577v1.pdf)

---

## [17. EcoVideo: Entropy-Orchestrated Video Generation Paradigm in Cloud-Edge Dynamics](https://arxiv.org/abs/2606.30557v1)

**作者**：Jiayu Chen, Hengyi Zhang, Maoliang Li 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-29

### 📄 论文摘要

DiT video generation is latency-intensive due to iterative full-frame denoising, while prior cloud-edge methods largely rely on static inter-step decoupling and cannot leverage inter-frame similarity or adapt to system dynamics. We propose EcoVideo, an entropy-orchestrated framework for dynamic inter-frame decoupling: early-stage self-attention entropy provides a training-free estimate of frame-wise information density for frame selection; a cloud large model denoises sparse high-entropy keyframes; and an edge lightweight model reconstructs the remaining frames via motion-aware interpolation with refinement for temporal stability. EcoVideo further adapts the keyframe budget and edge refinement depth to real-time bandwidth and compute availability, optimizing end-to-end latency under constraints. Experiments on representative DiT video generators show improved quality--efficiency trade-offs and up to 2.9x end-to-end speedup in low-bandwidth, compute-limited edge settings. Code is available at https://github.com/IF-LAB-PKU/EcoVideo.

### 🤖 AI 总结

**一句话总结**：DiT video generation is latency-intensive due to iterative full-frame denoising, while prior cloud-edge methods largely rely on static inter-step decoupling and cannot leverage inter-frame similarity ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EcoVideo, Entropy-Orchestrated, Video, Generation, Paradigm, Cloud-Edge, Dynamics, DiT

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30557v1) | [下载PDF](https://arxiv.org/pdf/2606.30557v1.pdf)

---

## [18. StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors](https://arxiv.org/abs/2606.30545v1)

**作者**：Wenhao Yuan, Yiyuan Ge, Deli Cai  
**分类**：cs.CV  
**发布时间**：2026-06-29

### 📄 论文摘要

3D Gaussian Splatting (3DGS) has achieved remarkable success in real-time novel view synthesis, yet it suffers from severe overfitting under sparse-view settings due to insufficient geometric constraints. While recent methods introduce monocular depth priors to mitigate this, they inherently struggle with scale ambiguity and cross-view inconsistency, leading to defective geometry. In this paper, we propose StereoGS, a novel sparse-view 3DGS framework that integrates stereo priors to establish reliable binocular consistency. Unlike scale-agnostic monocular constraints, StereoGS introduces a Stereo Depth Regularization by constructing virtual stereo pairs during optimization and leveraging a foundation stereo model to enforce absolute scale and binocular-consistent structures. To further suppress overfitting and eliminate redundant primitives, we design a Gradient-Aware Opacity Decay strategy that dynamically penalizes Gaussians based on their relative opacity gradient magnitudes. Combined with a Consistency-Aware Dense Initialization using zero-shot multi-view depth estimation, StereoGS effectively anchors primitives to accurate scene surfaces. Extensive experiments on LLFF, DTU, Mip-NeRF360, and Blender datasets demonstrate that StereoGS achieves state-of-the-art performance in sparse-view settings without incurring any additional inference overhead. Project Page: https://stringerywh00.github.io/StereoGS_project_page/

### 🤖 AI 总结

**一句话总结**：3D Gaussian Splatting (3DGS) has achieved remarkable success in real-time novel view synthesis, yet it suffers from severe overfitting under sparse-view settings due to insufficient geometric constrai...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, StereoGS, Sparse-View, Gaussian, Splatting, via, Stereo, Priors

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30545v1) | [下载PDF](https://arxiv.org/pdf/2606.30545v1.pdf)

---

## [19. $μ$Flow: Leveraging Average Images for Improving Generalisation of Deepfake Faces Detectors](https://arxiv.org/abs/2606.30528v1)

**作者**：Orazio Pontorno, Mattia Litrico, Luca Guarnera 等 5 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-06-29

### 📄 论文摘要

Current generative models, including GANs and diffusion models, have reached an outstanding level of photorealism, posing significant risks to privacy and security. To ensure real-world applicability, deepfake detectors must generalise effectively to unseen generators. However, most existing approaches rely on supervised training with both real and fake images, which limits their generalisation especially across generators categories (e.g. GANs vs DMs). In this work, we introduce $μ$Flow, a one-class deepfake detector trained only on real images without relying on pseudo-deepfakes or synthetic artifacts. Our approach builds on the observation that averaging multiple images amplifies consistent generative traces, producing highly discriminative feature representations. We leverage this property by modelling the distribution of features extracted from averaged images and training a normalizing flow to align the feature space of individual images with this distribution. This alignment yields a likelihood-based criterion that separates real and fake samples while promoting strong generalisation. We evaluate $μ$Flow on a fully out-of-distribution setting, where both real and fake datasets are unseen during training. Experimental results show that our method significantly outperforms SOTA detectors. Project page: https://opontorno.github.io/MuFlow.

### 🤖 AI 总结

**一句话总结**：Current generative models, including GANs and diffusion models, have reached an outstanding level of photorealism, posing significant risks to privacy and security. To ensure real-world applicability,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, $μ$Flow, Leveraging, Average, Images, Improving, Generalisation, Deepfake

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30528v1) | [下载PDF](https://arxiv.org/pdf/2606.30528v1.pdf)

---

## [20. 3D Scene-Adaptive Trajectory-Controllable Human Image Animation with Camera Movement](https://arxiv.org/abs/2606.30514v1)

**作者**：Deyin Liu, Jicheng Xu, Lin Yuanbo Wu 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-29

### 📄 论文摘要

Human image animation, which aims to generate a video of a reference subject following a provided action sequence, has received increasing research interest. With the development of diffusion-based/flow-based video foundation models, existing animation works have began to upgrade the guidance information from 2D skeleton/pose to 3D modeling conditions. Despite achieving reasonable results, these approaches face challenges in synthesizing trajectory-controllable human motion within natural scene under changed camera views. In this work, we present a scene-adaptive human image animation framework that controls both human motion and camera trajectories within a reconstructed 3D environment for video generation. To achieve this, we first develop a ground-adaptive 3D motion retargeting approach to enable user-friendly motion trajectory control adapting to the changes of elevations of ground and orientations automatically. Then we design a viewpoint-adaptive latent fusion mechanism to inject point-cloud geometric priors through scene-visibility masking into the generative process, providing precise guidance of viewpoint changes under camera control. Experiments on two standard human image animation benchmark datasets demonstrate remarkable improvements of our method over the state of the arts in related video generation metics. Project page: https://robinhood256100.github.io/web-disp

### 🤖 AI 总结

**一句话总结**：Human image animation, which aims to generate a video of a reference subject following a provided action sequence, has received increasing research interest. With the development of diffusion-based/fl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Scene-Adaptive, Trajectory-Controllable, Human, Image, Animation, Camera, Movement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30514v1) | [下载PDF](https://arxiv.org/pdf/2606.30514v1.pdf)

---

## cs.LG

## [21. One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining](https://arxiv.org/abs/2606.30634v1)

**作者**：Philip Zmushko, Egor Petrov, Nursultan Abdullaev 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-29

### 📄 论文摘要

Modern large-scale LLM pretraining benefits from utilizing Pipeline Parallelism; however, synchronous implementations leave GPUs idle during pipeline bubbles, wasting computational resources. Asynchronous Pipeline Parallelism eliminates these bubbles, maximizing throughput at the cost of gradient staleness. Among asynchronous schedules, PipeDream-2BW is particularly appealing: unlike the original PipeDream schedule, it ensures a constant one-step gradient delay regardless of pipeline depth. However, its adoption remains limited due to the common belief that optimizing under staleness is fundamentally unstable. In this work, we challenge this assumption, demonstrating that degradation under one-step delay depends strongly on optimizer choice rather than being an intrinsic limitation. We provide the first comprehensive empirical analysis showing that while AdamW, the predominant optimizer at the time when PipeDream-2BW was introduced, indeed suffers from severe degradation, recent methods like Muon exhibit strong robustness under a one-step delay. We introduce an optimizer-agnostic Error Feedback-inspired correction to further mitigate delay effects. We provide supporting theoretical analysis demonstrating convergence for Muon with and without this correction. Extensive evaluation on models up to 10B parameters confirms that our strategies bridge the performance gap with synchronous training, highlighting the practical potential of asynchronous pipeline parallelism at scale.

### 🤖 AI 总结

**一句话总结**：Modern large-scale LLM pretraining benefits from utilizing Pipeline Parallelism; however, synchronous implementations leave GPUs idle during pipeline bubbles, wasting computational resources. Asynchro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：One-Step, Gradient, Delay, Not, Barrier, Large-Scale, Asynchronous, Pipeline

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30634v1) | [下载PDF](https://arxiv.org/pdf/2606.30634v1.pdf)

---

## [22. Pessimism's Paradox: Conservative Offline Training Amplifies Reward Hacking During Online Adaptation in Reasoning Models](https://arxiv.org/abs/2606.30627v1)

**作者**：Subramanyam Sahoo, Aman Chadha, Vinija Jain 等 4 位作者  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-06-29

### 📄 论文摘要

Conservative offline training is widely advocated as a safe foundation for subsequent online adaptation: if a policy stays close to well-supported behaviour, the argument goes, it is less likely to exploit imperfections in a learned reward model. We challenge this intuition empirically and mechanistically. We train a Qwen3-14B policy under Direct Preference Optimisation (DPO) with three levels of conservatism ($β\in \{β_{\mathrm{lo}}, β_{\mathrm{mid}}, β_{\mathrm{hi}}\}$ derived from empirical log-ratio percentiles), then adapt each checkpoint online against a learned reward ensemble (3\,$\times$\,Qwen3-1.7B) while measuring true performance on GSM8K exact-answer accuracy. We find that \emph{higher offline conservatism monotonically increases reward-hacking damage}, measured by the Goodhart gap and its area under the curve (AUGC), with Spearman $ρ= 1.0$ across all three conditions. Mechanistic analysis reveals a three-link causal chain: (i) high-$β$ DPO compresses policy entropy, (ii) Low-entropy policies generate responses with reduced diversity, concentrating in a narrow region of the reward model's training distribution (lower pairwise cosine distance), and (iii) despite this proximity, ensemble disagreement (epistemic uncertainty) increases with $β$ and is exploited faster during online optimisation. We further fit a power-law curve to the $(β, \augc)$ data and identify a practical optimal conservatism level $β^{\star}$ that balances alignment fidelity against hacking vulnerability. Our results suggest that the field needs \emph{calibrated}, not \emph{maximal}, conservatism.

### 🤖 AI 总结

**一句话总结**：Conservative offline training is widely advocated as a safe foundation for subsequent online adaptation: if a policy stays close to well-supported behaviour, the argument goes, it is less likely to ex...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Pessimism's, Paradox, Conservative, Offline, Training, Amplifies, Reward, Hacking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30627v1) | [下载PDF](https://arxiv.org/pdf/2606.30627v1.pdf)

---

## [23. C$^{2}$R: Cross-sample Consistency Regularization Mitigates Feature Splitting and Absorption in Sparse Autoencoders](https://arxiv.org/abs/2606.30609v1)

**作者**：Haoran Jin, Xiting Wang, Shijie Ren 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-29

### 📄 论文摘要

Sparse Autoencoders (SAEs) are widely used to interpret large language models by decomposing activations into sparse, human-understandable features, but scaling to large dictionaries exposes fundamental challenges. Systematic studies reveal pervasive feature splitting that fragments coherent concepts into non-atomic latents and widespread feature absorption that creates arbitrary exceptions in general features, severely compromising latent reliability. These issues stem from inconsistent latent assignment across samples: without cross-sample constraints, per-sample optimization often allows a single underlying concept to be inconsistently distributed across multiple redundant or interfering latents. To address this, we introduce C$^2$R (\underline{\textbf{C}}ross-sample \underline{\textbf{C}}onsistency \underline{\textbf{R}}egularization). C$^2$R explicitly encourages that each semantic feature is consistently represented by a unified latent across the batch by penalizing the co-activation of directionally similar latents. Comprehensive evaluation demonstrates that C$^2$R effectively mitigates both splitting and absorption while, crucially, preserving reconstruction fidelity, providing a principled solution that enhances latent interpretability without degrading model performance. Source code is available at https://github.com/hr-jin/Cross-sample-Consistency-Regularization.

### 🤖 AI 总结

**一句话总结**：Sparse Autoencoders (SAEs) are widely used to interpret large language models by decomposing activations into sparse, human-understandable features, but scaling to large dictionaries exposes fundament...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：C$^, $R, Cross-sample, Consistency, Regularization, Mitigates, Feature, Splitting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30609v1) | [下载PDF](https://arxiv.org/pdf/2606.30609v1.pdf)

---

## [24. The Fundamental Limits of Valid Transport Map Estimation](https://arxiv.org/abs/2606.30574v1)

**作者**：Sivaraman Balakrishnan  
**分类**：cs.LG, math.ST, stat.ML  
**发布时间**：2026-06-29

### 📄 论文摘要

Many modern generative modeling methods, including diffusion models, normalizing flows, and flow matching, estimate transport maps or plans between distributions without explicitly targeting an optimal transport (OT) map. In applications like generative modeling, the transport cost itself is irrelevant, and this makes it natural to target maps which are more tractable from either a statistical or computational standpoint. In this short note, we formalize the task of estimating any valid transport map in a rigorous minimax framework. One consequence of this framing is that it yields sample complexity lower bounds for any method whose learned object is evaluated as a transport map or plan, including flow matching and diffusion-based generative models, in settings where direct analysis would be challenging due to the analytic complexity of the methods and their target maps. We observe that, under standard, though strong, stability assumptions from the OT literature, estimating any valid transport map is statistically as hard as estimating the OT map. We complement these results with some examples showing that when these stability assumptions fail, alternative transport maps can be learned substantially more accurately than the OT map. Our minimax framing provides a rigorous foundation for understanding the statistical limits of modern transport-based generative methods and clarifies when targeting sub-optimal maps can provide real statistical advantages.

### 🤖 AI 总结

**一句话总结**：Many modern generative modeling methods, including diffusion models, normalizing flows, and flow matching, estimate transport maps or plans between distributions without explicitly targeting an optima...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Fundamental, Limits, Valid, Transport, Map, Estimation, Many

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30574v1) | [下载PDF](https://arxiv.org/pdf/2606.30574v1.pdf)

---

## [25. SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions](https://arxiv.org/abs/2606.30573v1)

**作者**：Mohit Raghavendra, Anisha Gunjal, Aakash Sabharwal 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-29

### 📄 论文摘要

We introduce SWE-Interact, a new testbed for evaluating coding agents on multi-turn, interactive, user-driven software engineering tasks. Existing frontier SWE benchmarks typically provide complete requirements upfront and evaluate agents on autonomous implementation. In contrast, SWE-Interact places agents in a realistic developer workflow: a carefully designed user simulator starts with vague or incomplete instructions, progressively reveals requirements, inspects the agent's workspace, and provides targeted feedback, revisions, and new constraints until the full task goal has been handed off. Grounded in large-scale studies of real coding-agent interactions, this setup tests whether agents can discover user intent, adapt to evolving requirements, and build on their own prior work. Across a suite of frontier and open-weight models, we find that strong performance on single-turn SWE tasks does not reliably transfer to multi-turn, user-driven workflows: the best-performing models solve roughly 50% of single-turn baseline tasks but only 25% of the corresponding SWE-Interact tasks. The strongest models in our evaluation, including Opus 4.8 and GPT 5.5, start strong even in the face of vague initial instructions, persevere until all the requirements are surfaced by the user, integrate them better and write clean code. However, they still suffer from over-agentic coding, forgetting requirements and technical mistakes. Weaker models start poorly under ambiguity, give up early, forget or ignore instructions and rework their code more. Overall, SWE-Interact measures an orthogonal, real-world capability axis for frontier model development: interactive goal discovery and iterative refinement with a user in the loop.

### 🤖 AI 总结

**一句话总结**：We introduce SWE-Interact, a new testbed for evaluating coding agents on multi-turn, interactive, user-driven software engineering tasks. Existing frontier SWE benchmarks typically provide complete re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, SWE-INTERACT, Reimagining, SWE, Benchmarks, User-Driven, Long-Horizon, Coding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30573v1) | [下载PDF](https://arxiv.org/pdf/2606.30573v1.pdf)

---

## [26. Attractor States Emerge in Multi-Turn LLM Conversations](https://arxiv.org/abs/2606.30571v1)

**作者**：Ting-Wen Ko, Jonas Geiping  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-06-29

### 📄 论文摘要

Large language models (LLMs) are increasingly used in open-ended multi-agent settings, but the long-run dynamics of model--model interaction remain poorly understood. We study whether open-ended LLM discussions exhibit attractor-like behavior, i.e. topic-independent stable sets of behaviors which conversations settle into. Across 7 LLMs and 20 controversial topics, we compare self-play and mixed-play dyadic debates, tracking trajectories in representation space, discourse traits, and stances. We find self-play trajectories to be model-specific attractors that draw their conversation partners asymmetrically in mixed-play debates, influencing the other models' stylistic choices and behavior. For example, Claude Haiku is a strong attractor of other models in latent space, corresponding to other models taking on its traits like metacommentary, and models like GPT-4.1 nano are especially malleable. Our results suggest that open-ended LLM interactions are partially predictable from model-specific attractors, but shaped by structured and asymmetric partner influence. Overall, our analysis sheds some light on the complex behavior of open-ended multi-agent interaction, which we hope is helpful in designing, predicting, and monitoring autonomous agentic systems in the real world.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly used in open-ended multi-agent settings, but the long-run dynamics of model--model interaction remain poorly understood. We study whether open-ended LLM d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Attractor, States, Emerge, Multi-Turn, Conversations, Large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30571v1) | [下载PDF](https://arxiv.org/pdf/2606.30571v1.pdf)

---

## [27. TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/abs/2606.30560v1)

**作者**：Kan Zhu, Mathew Jacob, Chenxi Ma 等 7 位作者  
**分类**：cs.LG, cs.AI, cs.PF  
**发布时间**：2026-06-29

### 📄 论文摘要

Coding agents are rapidly becoming a major application of agentic LLMs, but serving them efficiently remains challenging. Progress on this challenge requires understanding real workload patterns, yet the data needed for such analysis is largely absent. Existing public traces and benchmarks do not capture real, day-to-day coding-agent usage across multiple agents and model families for serving-system analysis. To help fill this gap, we collect and release a trace of roughly 4,300 coding-agent sessions, containing about 350,000 LLM steps and 430,000 tool calls from our own day-to-day use of Claude Code and Codex. Our analysis shows that coding-agent workloads feature long autonomous loops, long contexts with short outputs, diverse and heavily-tailed tool calls, and high but imperfect prefix cache hit rates. These findings point to concrete opportunities for optimizing serving, including lower-overhead tool calling, append-length-aware prefill, semantic-aware tool-latency prediction, and improved KV-cache management around human-paced gaps. We release the dataset, trace collection pipeline, and analysis code at https://github.com/uw-syfi/TraceLab.git; the project website is https://tracelab.cs.washington.edu.

### 🤖 AI 总结

**一句话总结**：Coding agents are rapidly becoming a major application of agentic LLMs, but serving them efficiently remains challenging. Progress on this challenge requires understanding real workload patterns, yet ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, LLM, TraceLab, Characterizing, Coding, Workloads, Serving, rapidly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30560v1) | [下载PDF](https://arxiv.org/pdf/2606.30560v1.pdf)

---

## [28. Convergence of Continual Learning in Homogeneous Deep Networks](https://arxiv.org/abs/2606.30559v1)

**作者**：Matan Schliserman, Gon Buzaglo, Itay Evron 等 4 位作者  
**分类**：cs.LG, math.NA, math.OC, stat.ML  
**发布时间**：2026-06-29

### 📄 论文摘要

We characterize weakly regularized continual classification in homogeneous models as sequential projections onto task margin sets. This result generalizes prior analyses restricted to either stationary (single-task) deep models or continual linear models. We show that global convergence generally fails, even for simple models linear in data but nonlinear in parameters. Nevertheless, by leveraging results from nonconvex projection theory, we identify regularity properties of homogeneous deep networks that guarantee local linear convergence under random and cyclic task sequences. Finally, we extend our analysis to continual regression, unifying the framework for homogeneous models.

### 🤖 AI 总结

**一句话总结**：We characterize weakly regularized continual classification in homogeneous models as sequential projections onto task margin sets. This result generalizes prior analyses restricted to either stationar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, We, Convergence, Continual, Learning, Homogeneous, Deep, Networks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30559v1) | [下载PDF](https://arxiv.org/pdf/2606.30559v1.pdf)

---

## [29. ITSPACE: Monotone Gaussian Optimal Transport Updates](https://arxiv.org/abs/2606.30523v1)

**作者**：Woojoo Na, Jennifer Dy  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-06-29

### 📄 论文摘要

Covariance matrices serve as compact descriptors of feature distributions in many machine-learning pipelines, including domain adaptation and Gaussian embeddings. Under a centered Gaussian approximation, the unregularized Wasserstein-2 optimal-transport (OT) discrepancy admits a closed form on covariances given by the Bures-Wasserstein (BW) objective on the symmetric positive definite (SPD) cone. We propose ITSPACE (Iterative Transport for Stable Proximal Alignment of Covariance Embeddings), a proximal majorization-minimization method that directly optimizes this exact BW objective through closed-form updates in a square-root factorization. In exact arithmetic, each iteration satisfies a sufficient-decrease inequality for the BW objective; under inexact polar computations, we provide an explicit certificate-gap bound controlling deviations from exact descent. The resulting iterations preserve PSD structure by construction and naturally support rank-restricted factors, making ITSPACE well-suited as a lightweight inner-loop primitive in settings where adaptation must be performed from unlabeled target batches under strict step and compute budgets. Across real-world covariance-alignment benchmarks, ITSPACE reaches low-BW-gap solutions substantially faster than BW-gradient descent, methods based on other covariance geometries, and entropically regularized sample-OT baselines.

### 🤖 AI 总结

**一句话总结**：Covariance matrices serve as compact descriptors of feature distributions in many machine-learning pipelines, including domain adaptation and Gaussian embeddings. Under a centered Gaussian approximati...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ITSPACE, Monotone, Gaussian, Optimal, Transport, Updates, Covariance, matrices

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30523v1) | [下载PDF](https://arxiv.org/pdf/2606.30523v1.pdf)

---

## [30. Informational Frustration in Neural Manifolds: Shannon Bottlenecks and the Limits of Learnability](https://arxiv.org/abs/2606.30512v1)

**作者**：Srinivasa Rao P., Vangmayi P Reddy  
**分类**：cs.LG, cs.AI, cs.CG  
**发布时间**：2026-06-29

### 📄 论文摘要

Why overparameterised deep networks generalise so remarkably well remains one of the most stubborn open questions in machine learning theory. Classical frameworks like VC dimension and Rademacher complexity predict catastrophic overfitting in modern models, leaving a massive theoretical gap between theory and reality. In this paper, we bridge this divide by introducing a unified framework that links information theory, topology, and statistical mechanics to map the hard limits of deep learning. Central to our approach is the Entropic Learnability Horizon (ELH): a fundamental law stating that a network can only truly learn a target function if the Shannon entropy of the data manifold outpaces the topological entropy of the function's decision boundary, balanced by the von Neumann entropy of the network's weight space. We establish the Shannon-Topological Bottleneck Theorem, proving that when a target boundary's geometric complexity exceeds this informational horizon, the system undergoes a sudden entropic phase transition. It falls into a state of Informational Frustration - a glassy, rigid memorization phase where generalization becomes thermodynamically impossible. Using this lens, we show that the enigmatic phenomenon of "grokking" is actually an Entropic Release, where weights abruptly reorganise to unlock the bottleneck. Finally, we translate this theory into practice with Entropic Gradient Descent (EGD), an optimization algorithm that dynamically manages weight entropy to keep learning on track. Ultimately, this work repositions entropy not just as a tool for tracking uncertainty but as the fundamental physical currency that dictates whether a machine can learn.

### 🤖 AI 总结

**一句话总结**：Why overparameterised deep networks generalise so remarkably well remains one of the most stubborn open questions in machine learning theory. Classical frameworks like VC dimension and Rademacher comp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Informational, Frustration, Neural, Manifolds, Shannon, Bottlenecks, Limits

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.30512v1) | [下载PDF](https://arxiv.org/pdf/2606.30512v1.pdf)

---

