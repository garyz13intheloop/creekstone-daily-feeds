# arXiv AI 论文日报 | 2026-08-13

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (18 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.AI](#csAI) (2 篇)
- [cs.CL](#csCL) (3 篇)

---

## cs.AI

## [1. Constructing Dynamic Master Logic Models as Knowledge Graphs for Complex System Diagnostics Using Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2608.12304v1)

**作者**：Saman Marandi, Yu-Shu Hu, Mohammad Modarres  
**分类**：cs.AI  
**发布时间**：2026-08-12

### 📄 论文摘要

Dynamic Master Logic (DML) provides a hierarchical framework for representing system behavior by linking functional objectives to underlying structural elements. However, DML construction typically relies on expert interpretation of technical documentation, limiting scalability for complex systems. This study presents a framework for automated construction of DML models from system descriptions and their representation as Knowledge Graphs (KG-DML), using Retrieval-Augmented Generation and Large Language Models as enabling tools. Building on prior work with small-scale systems, the framework extends automated KG-DML construction and evaluation to substantially larger and more complex systems. Model construction proceeds across the DML hierarchy using targeted retrieval while preserving functional dependencies and explicit logical relationships. The resulting KG-DML supports diagnostic reasoning, safety assessment, upward failure propagation, and downward dependency tracing. A multi-level validation methodology evaluates layer-specific precision and recall, logical gate consistency, and overall structural integrity. Application to the Low-Pressure Coolant Injection system of a decommissioned Boiling Water Reactor demonstrates consistent reconstruction across repeated runs. The results show that automated KG-DML construction can transform technical documentation into executable functional models for diagnostic and reliability analysis.

### 🤖 AI 总结

**一句话总结**：Dynamic Master Logic (DML) provides a hierarchical framework for representing system behavior by linking functional objectives to underlying structural elements. However, DML construction typically re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Constructing, Dynamic, Master, Logic, Models, Knowledge, Graphs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12304v1) | [下载PDF](https://arxiv.org/pdf/2608.12304v1.pdf)

---

## [2. How to Spend Your Oracle Budget: Practical Guidance for Protein Structure Prediction Models](https://arxiv.org/abs/2608.12192v1)

**作者**：Aleksandra Kalisz, Jack Simons, Krisztina Sinkovics 等 7 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-08-12

### 📄 论文摘要

Foundation models for protein structure prediction remain unreliable on certain targets. External oracles can flag and correct these failures, but biological oracles are expensive, making oracle budget a critical constraint. Existing guidance methods, such as FK-steering, DPO, and Best K-of-N sampling, differ in how they spend this budget, yet no systematic comparison exists to guide method selection. To bridge this gap, we benchmark these methods alongside the recently proposed Optimisation Over Outputs (O3), which applies off-the-shelf optimisers within a generative model's latent subspace. We extend the usage of O3 to protein structure prediction models. Overall, our work provides the first practical reference for oracle budget-aware guidance. Our evaluation on two protein targets, calmodulin (1CLL) and E. coli aspartate transcarbamoylase (9EEH), reveals that no single method consistently dominates across all budgets and oracles. Specifically, O3 proves most effective at low oracle budgets, while FK-steering and DPO demonstrate improved performance as the budget increases. We distil these findings into actionable recommendations for practitioners operating under real-world oracle-budget constraints.

### 🤖 AI 总结

**一句话总结**：Foundation models for protein structure prediction remain unreliable on certain targets. External oracles can flag and correct these failures, but biological oracles are expensive, making oracle budge...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：How, Spend, Oracle, Budget, Practical, Guidance, Protein, Structure

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12192v1) | [下载PDF](https://arxiv.org/pdf/2608.12192v1.pdf)

---

## cs.CL

## [3. A Cascaded Unsupervised-Supervised NLP Pipeline for Detecting Accusatory Language in Public Procurement](https://arxiv.org/abs/2608.12269v1)

**作者**：Bryan Torres, Daniel Riofrío, José Vega-Sánchez 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-12

### 📄 论文摘要

Public procurement involves the allocation of substantial financial resources; therefore, continuous oversight through audits, controls, and monitoring mechanisms is essential. However, stakeholder comments and publicly available government data are often underutilized, despite their potential to reveal procedural irregularities. To address this gap, this paper analyzes metadata from Ecuador's Sistema Oficial de Contratación Pública (SOCE, Official Public Procurement System), with particular emphasis on participant comments generated during the pre-contractual phase. We propose a hybrid modeling framework that integrates unsupervised clustering and supervised classification within a natural language processing (NLP) pipeline to uncover latent patterns and detect potentially irregular procurement processes. Semantic embeddings are generated using Word2Vec, LLaMA, and RoBERTa, followed by Gaussian Mixture Models (GMMs) for unsupervised clustering. A supervised classification stage is then applied to identify accusatory or whistleblowing-style comments. Experimental results show that the combination of domain-trained Word2Vec embeddings, GMM-based clustering, and a Random Forest classifier achieves high precision and recall, even under severe class imbalance. These findings demonstrate that lightweight, domain-adapted NLP architectures can effectively support risk identification and enhance transparency in public procurement systems without requiring large-scale computational infrastructure.

### 🤖 AI 总结

**一句话总结**：Public procurement involves the allocation of substantial financial resources; therefore, continuous oversight through audits, controls, and monitoring mechanisms is essential. However, stakeholder co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Cascaded, Unsupervised-Supervised, NLP, Pipeline, Detecting, Accusatory, Language, Public

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12269v1) | [下载PDF](https://arxiv.org/pdf/2608.12269v1.pdf)

---

## [4. One Frozen Simulator Is Not Enough: Simulator Collapse in Multi-Agent RL](https://arxiv.org/abs/2608.12253v1)

**作者**：Simon Yu, Nicholas Tomlin, Marwa Abdulhai 等 10 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-08-12

### 📄 论文摘要

Multi-agent reinforcement learning for human-AI interaction typically relies on a single large language model to simulate user behavior. We show that this approach systematically fails to generalize, and trace the failure to simulator collapse: because the simulator LLM is mode-collapsed, an LLM policy trained against it overfits to narrow strategies that exploit the simulator's dominant mode, and such a policy transfers poorly to unseen simulators and real users. We formalize this collapse theoretically and propose two complementary solutions, one at inference time and one at training time. The inference-time solution, Verbalized Sampling, broadens the simulator's behavior by sampling from a verbalized response distribution, reducing mode collapse. The training-time solution, Co-Training, jointly optimizes the policy against a population of trainable simulators, preventing it from overfitting to any single simulator's mode. We validate both solutions on three multi-turn benchmarks: Persuasion for Good, $τ^2$-bench, and CooperBench. Verbalized Sampling improves held-out success by up to 9% over single-simulator RL, and Co-Training pushes gains further to 14%; the human study shows similar gain on real users. Both solutions preserve the policy diversity that collapses under single-simulator RL. To support further work in this direction, we release SCOPE, an open-source framework for Population Co-Training multi-agent RL. More broadly, our results suggest that the diversity of the training environment, not only the policy, is critical to the generalization of multi-turn RL to real-world deployment.

### 🤖 AI 总结

**一句话总结**：Multi-agent reinforcement learning for human-AI interaction typically relies on a single large language model to simulate user behavior. We show that this approach systematically fails to generalize, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, RL, One, Frozen, Simulator, Not, Enough, Collapse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12253v1) | [下载PDF](https://arxiv.org/pdf/2608.12253v1.pdf)

---

## [5. Information Abundance Paradox: Long-Context Training Undermines Parametric Knowledge](https://arxiv.org/abs/2608.12218v1)

**作者**：Arda Uzunoglu, Benjamin van Durme, Daniel Khashabi  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-12

### 📄 论文摘要

Large language models are increasingly trained and deployed with long contexts that span documents, code repositories, and interaction histories. This scaling reflects the implicit assumption that training on longer contexts will only help the model by exposing it to richer evidence. We challenge this view by studying how the context window shapes a model's mode of learning, shifting it between parametric internalization and contextualization. We propose the Information Abundance Paradox, which hypothesizes that abundant relevant information in the training context can reduce the incentive to encode that information parametrically, thereby increasing reliance on context. In pretraining with long documents, increasing the context window improves language modeling, natural language understanding, and closed-book MCQA only up to an intermediate optimum, after which performance consistently declines. In supervised fine-tuning, more task-relevant train-time context improves performance with supporting context, but reduces robustness when context is absent or misleading at test time. Our analysis suggests that this behavior arises when longer context provides a lower complexity solution. Mechanistically, training with informative context shifts gradient pressure from feed-forward networks, often linked to parametric knowledge, toward attention modules, and causal interventions show that this shift increases reliance on context during inference. Overall, these findings support the Information Abundance Paradox and suggest that scaling toward near-infinite context is not simply a matter of supplying more data, even when high-quality long-context data is abundant.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly trained and deployed with long contexts that span documents, code repositories, and interaction histories. This scaling reflects the implicit assumption that tra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Information, Abundance, Paradox, Long-Context, Training, Undermines, Parametric, Knowledge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12218v1) | [下载PDF](https://arxiv.org/pdf/2608.12218v1.pdf)

---

## cs.CV

## [6. DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation](https://arxiv.org/abs/2608.12308v1)

**作者**：Yan Deng, Fei Xu  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-12

### 📄 论文摘要

Aerial vision-language navigation (VLN) requires an embodied agent to integrate visual evidence over time, plan future actions, and determine when it has reached a navigation goal under partial observability. Although recent VLA models offer a promising perception-to-action paradigm, adapting them to aerial navigation remains challenging due to limited historical context, short planning horizons, and unreliable implicit termination. To address these challenges, we propose DreamFly, a diffusion-based aerial VLN framework built on Dream-VLA. DreamFly introduces a causally aligned historical memory that augments the current visual representation using only observations preceding the current decision step, enabling temporal reasoning without future information leakage. We further formulate navigation as receding-horizon diffusion planning, where the policy predicts a $K$-step action chunk but executes only the first action before replanning. This plan-$K$, execute-one strategy uses future actions as auxiliary planning targets while preserving closed-loop visual feedback. Finally, LiteStop estimates the stop probability directly from action logits at the initial all-mask state, decoupling explicit termination from action generation. Experiments on the OpenFly benchmark demonstrate consistent improvements in seen and unseen environments. DreamFly achieves 32.04%/29.46% SR and 28.22%/23.54% SPL on the test-seen/test-unseen splits, respectively, outperforming all compared methods on both metrics while attaining the lowest navigation error. These results demonstrate the effectiveness of jointly modeling historical context, future action structure, and explicit termination for aerial VLN.

### 🤖 AI 总结

**一句话总结**：Aerial vision-language navigation (VLN) requires an embodied agent to integrate visual evidence over time, plan future actions, and determine when it has reached a navigation goal under partial observ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, DreamFly, Causal, Memory, Receding-Horizon, Planning, Aerial, Vision-Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12308v1) | [下载PDF](https://arxiv.org/pdf/2608.12308v1.pdf)

---

## [7. Beyond Trial-and-Error: Agentic Optimization for Image-to-Video Adherence](https://arxiv.org/abs/2608.12290v1)

**作者**：Aman Tyagi, Hemanth Boinpally, Jonathan Chen 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.MM  
**发布时间**：2026-08-12

### 📄 论文摘要

Modern black-box Image-to-Video (I2V) models offer powerful capabilities in automated content creation, yet their lack of fine-grained control and reliability presents significant challenges in professional workflows. Their inherent stochasticity causes minor variations in textual prompts or hyperparameters to yield drastically different outputs often necessitating inefficient, brute-force trial-and-error processes. To address these limitations, we introduce the ``Agentic Self-Improvement" framework, which reframes video synthesis into a closed-loop, goal-directed optimization. Our framework systematically navigates the generation parameter space using a novel two-stage approach. In the first stage, an iterative prompt optimization loop uses a multimodal Large Language Model (mLLM) to refine the input prompt. This refinement implements two automated evaluations: Davidsonian Scene Graph (DSG) queries ensure semantic adherence, and Common Mistake Questions (CMQ) for artifact detection. At the second stage, we use Bayesian optimization to efficiently co-optimize stochastic seeds and CFG scales. This search is guided by a suite of quality metrics, including the novel Video-Text Adherence (VTA) score derived from the DSG and CMQ evaluations. Our framework significantly outperforms unguided search methods: in human preference studies, videos generated via our agentic approach were strongly preferred over baseline outputs, achieving win rates up to 69\%. This work provides a practical and extensible methodology for enhancing the predictability and control of state-of-the-art video generation models, moving the field beyond speculative curiosities toward reliable, production-ready tools.

### 🤖 AI 总结

**一句话总结**：Modern black-box Image-to-Video (I2V) models offer powerful capabilities in automated content creation, yet their lack of fine-grained control and reliability presents significant challenges in profes...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Trial-and-Error, Agentic, Optimization, Image-to-Video, Adherence, Modern, black-box

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12290v1) | [下载PDF](https://arxiv.org/pdf/2608.12290v1.pdf)

---

## [8. Curvature-Aware Zeroth-Order Optimization for Memory-Efficient Test-Time Adaptation](https://arxiv.org/abs/2608.12279v1)

**作者**：Junming Zhang, Shuyu Yin, Peilin Liu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-12

### 📄 论文摘要

Test-time adaptation (TTA) aims to enhance the cross-domain performance of pre-trained models by adapting to unlabeled test data. While most existing TTA methods rely on backpropagation (BP) for finetuning, BP-free methods such as zeroth-order (ZO) methods are more desired in practical on-device scenarios. ZO methods rely only on forward computation, which can largely reduce the complexity and memory overhead of on-device deployment. However, ZO methods suffer from much higher variance compared with first-order methods in estimating the gradient. To address this, we propose an improved ZO method to substantially boost the performance of ZO optimization based TTA. First, we provide an observation to reveal the persistent low-rank Hessian structure of the loss during the adaptation process. Based on this insight, we then propose a loss-landscape curvature-aware zeroth-order (CAZO) method, which leverages a sliding-average estimation of the diagonal Hessian to construct a covariance matrix for anisotropic perturbation sampling. CAZO operates by freezing pretrained weights and optimizing minimal adapter parameters via forward-only passes based gradient estimation, which can substantially reduce the memory overhead compared to BP-based methods. Extensive experiments demonstrate that CAZO significantly outperforms existing TTA methods, achieving state-of-the-art performance while maintaining an excellent balance between accuracy and memory efficiency. Code is available at https://github.com/Hollyming/CAZO.

### 🤖 AI 总结

**一句话总结**：Test-time adaptation (TTA) aims to enhance the cross-domain performance of pre-trained models by adapting to unlabeled test data. While most existing TTA methods rely on backpropagation (BP) for finet...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Curvature-Aware, Zeroth-Order, Optimization, Memory-Efficient, Test-Time, Adaptation, TTA, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12279v1) | [下载PDF](https://arxiv.org/pdf/2608.12279v1.pdf)

---

## [9. XYZFlow:Scaling Multi dimensional Shortcut Flows for Efficient Generative Modeling](https://arxiv.org/abs/2608.12276v1)

**作者**：Jinxiu Liu, Xuanming Liu, Kangfu Mei 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-12

### 📄 论文摘要

High-fidelity image generation faces a trade-off between speed and quality. Diffusion models produce strong visuals but require costly iterative sampling. Existing efficient methods mainly distill pretrained models into few-step samplers, a challenging process that depends heavily on teacher-model quality. In this paper, we introduce XYZFlow, a framework that rethinks efficient generation through multidimensional scaling of flow matching. Unlike single-step mappings, XYZFlow enhances expressivity by making probability paths more identifiable and learnable through structured multidimensional conditioning. We view autoregressive modeling as implicit flow straightening, where richer context reduces trajectory ambiguity. XYZFlow realizes this idea through two orthogonal dimensions: temporal scaling, which uses non-Markovian conditioning on the full denoising history; and spatial scaling, enabled by Next Shortcut Prediction, which sequentially generates patches using preceding patches' denoising trajectories as priors. Experiments show that XYZFlow achieves state-of-the-art performance, with 7.2-8.5X teacher speedups and competitive FID, while Next Shortcut Prediction delivers superior quality-latency trade-offs over model scaling or step reduction.

### 🤖 AI 总结

**一句话总结**：High-fidelity image generation faces a trade-off between speed and quality. Diffusion models produce strong visuals but require costly iterative sampling. Existing efficient methods mainly distill pre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：XYZFlow, Scaling, Multi, dimensional, Shortcut, Flows, Efficient, Generative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12276v1) | [下载PDF](https://arxiv.org/pdf/2608.12276v1.pdf)

---

## [10. A Neighborhood Attention Transformer Network for Enhanced 3D Segmentation of the Left Anterior Descending Artery](https://arxiv.org/abs/2608.12274v1)

**作者**：Rafi Ibn Sultan, Chengyin Li, Yiannos Demetriou 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-12

### 📄 论文摘要

Background: Accurate segmentation of the Left Anterior Descending (LAD) artery in 3D free-breathing, non-contrast CT is critical for cardiac dose sparing in thoracic radiotherapy. The LAD is extremely small, has poor soft-tissue contrast, and varies substantially across patients; even manual contours show limited inter-observer agreement, underscoring the ambiguity of the vessel boundaries. Purpose: To develop a transformer-based framework that improves LAD delineation in low-contrast, imbalanced CT through local-global context modeling and uncertainty-guided optimization. Methods: We propose NA-UNETR, a 3D transformer-based segmentation model whose Neighborhood Attention (NA) and Dilated NA (DiNA) blocks jointly capture fine structural detail and long-range context. Given the scarcity of annotated LAD data, the model is pretrained on 1,000 CTA volumes of general coronary anatomy and fine-tuned with LoRA-based parameter-efficient adaptation on 20 free-breathing institutional CT scans. A composite Dice-Focal and Hausdorff loss, dynamically balanced via homoscedastic uncertainty, improves overlap and boundary accuracy. Results: NA-UNETR reached 45.64% Dice, 38.16 mm HD95, and 10.01 mm ASD, improving Dice by 3.10 percentage points over nnU-Net and reducing HD95 by 2.96 mm relative to Swin UNETR, with the strongest boundary accuracy among all models and improved centerline stability. On ImageCAS it achieved 79.49% Dice, 8.89 mm HD95, and 1.02 mm ASD. Ablations confirmed that residual blocks, variable kernels, and uncertainty-weighted loss each contributed. Conclusions: NA-UNETR balances local precision and global context for thin, low-contrast LAD structures, offering a computationally efficient framework for substructure-level cardiac segmentation in radiotherapy planning.

### 🤖 AI 总结

**一句话总结**：Background: Accurate segmentation of the Left Anterior Descending (LAD) artery in 3D free-breathing, non-contrast CT is critical for cardiac dose sparing in thoracic radiotherapy. The LAD is extremely...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, of, Neighborhood, Attention, Transformer, Network, Enhanced, Segmentation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12274v1) | [下载PDF](https://arxiv.org/pdf/2608.12274v1.pdf)

---

## [11. Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams](https://arxiv.org/abs/2608.12262v1)

**作者**：Weihao Bo, Shan Zhang, Yanpeng Sun 等 10 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-12

### 📄 论文摘要

Multimodal Large Language Models (MLLMs) have been growing the capability for scientific writing and collaboration. For example, OpenAI Prism is a free workspace for scientific writing and collaboration. One important feature in Prism is turning scientific diagrams directly into LaTeX TikZ code. In this paper, we build a benchmark, Diagram-MMU, a multi-modal benchmark designed to assess MLLMs' ability for scientific diagram parsing and understanding. Diagram-MMU features 3.7k curated diagrams and 18.3k human-validated questions across six domains. It evaluates MLLMs on three tasks common in vibe writing workspaces: diagram-to-code parsing, diagram-to-code editing, and diagram question answering, alongside agentic settings per task. The evaluation of 12 MLLMs reveals that diagram-to-code tasks are more challenging than diagram question answering: models can reason well over diagrams but struggle to parse and edit them, underscoring the need for methods to enhance MLLMs' capability in diagram-to-code generation. Under agentic settings, most models improve parsing and editing performance but degrade on question answering, while Claude-4.6 Opus consistently improves across all three tasks. Project Page: https://vi-ocean.github.io/projects/diagram-mmu.

### 🤖 AI 总结

**一句话总结**：Multimodal Large Language Models (MLLMs) have been growing the capability for scientific writing and collaboration. For example, OpenAI Prism is a free workspace for scientific writing and collaborati...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diagram-MMU, Multi-Modal, Benchmark, Scientific, Diagrams, Multimodal, Large, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12262v1) | [下载PDF](https://arxiv.org/pdf/2608.12262v1.pdf)

---

## [12. Automated Borehole Core Analysis with Report-Derived Weak Labels and Supervised Crack Segmentation](https://arxiv.org/abs/2608.12252v1)

**作者**：Usama Imdad, Ali Khan, Luke Lu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-12

### 📄 论文摘要

Borehole archives commonly contain core tray photographs and corresponding digital log reports, but no native pixel-level crack annotations. We investigate two complementary approaches for extracting defect-spacing information from these archives. First, structured spacing categories recovered from the report text layer provide weak interval-level labels for classification. A DINO encoder trained on unlabeled core crops supplies domain-specific representations, and a manually verified subset is used to identify label inconsistencies. Second, we manually annotate 5,087 extracted core-row images and evaluate fully supervised crack-segmentation models. Our gated U-Net combines PiDiNet edge maps with Mask R-CNN masks through a learned spatial gating mechanism. This configuration achieves an F1 score of 0.860 and a crack-class IoU of 0.754, the highest result among the evaluated segmentation configurations. Deterministic post-processing converts predicted crack locations into defect-spacing categories. Separate rule-based branches estimate core-relative bedding angles and lithological color descriptors; their predictions agree with log-report references on 75.4% and 84.7% of 1,200 evaluated images, respectively. Because these references are extracted from existing reports, the reported values measure agreement with recorded geological observations rather than independent physical accuracy. The resulting framework combines report-derived weak supervision for spacing classification with fully supervised segmentation for image-based crack localization.

### 🤖 AI 总结

**一句话总结**：Borehole archives commonly contain core tray photographs and corresponding digital log reports, but no native pixel-level crack annotations. We investigate two complementary approaches for extracting ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Automated, Borehole, Core, Analysis, Report-Derived, Weak, Labels, Supervised

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12252v1) | [下载PDF](https://arxiv.org/pdf/2608.12252v1.pdf)

---

## [13. HAMP-LIC: Hessian-Aware Mixed-Precision Post-Training Quantization for Learned Image Compression](https://arxiv.org/abs/2608.12239v1)

**作者**：Yuefeng Zhang  
**分类**：cs.CV, cs.AI, cs.MM  
**发布时间**：2026-08-12

### 📄 论文摘要

Use this plain-text version for the arXiv abstract field: Learned image compression (LIC) models achieve strong rate-distortion performance but are hindered by high computational complexity and encoding-decoding mismatches across heterogeneous hardware platforms. Uniform fixed-precision quantization alleviates these issues but suffers severe quality degradation at low bit widths because it ignores differences in the quantization sensitivities of individual layers. To enable efficient and accurate low-bit deployment of pretrained LIC models, we propose HAMP-LIC, a Hessian-aware mixed-precision post-training quantization (PTQ) framework with a four-stage optimization strategy. First, block-wise sensitivity is estimated from the Hessian trace to capture second-order importance. Second, a task-aware refinement module adjusts these sensitivities by jointly considering quantization distortion and rate-distortion performance. Third, guided by the refined sensitivity profile, bit widths are allocated under a global model-size constraint to balance efficiency and reconstruction quality. Finally, block-wise reconstruction using a small calibration set further suppresses quantization error. Experiments on representative LIC models, including Minnen2018 and Cheng2020, demonstrate that HAMP-LIC achieves up to 4.85x model compression with as little as 0.59% BD-rate loss. It consistently outperforms existing fixed- and mixed-precision PTQ methods across multiple datasets while completely eliminating cross-platform encoding-decoding errors.

### 🤖 AI 总结

**一句话总结**：Use this plain-text version for the arXiv abstract field: Learned image compression (LIC) models achieve strong rate-distortion performance but are hindered by high computational complexity and encodi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HAMP-LIC, Hessian-Aware, Mixed-Precision, Post-Training, Quantization, Learned, Image, Compression

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12239v1) | [下载PDF](https://arxiv.org/pdf/2608.12239v1.pdf)

---

## [14. ScaleVid: Geometry-Aware Video Object Scaling with Mesh-Free Inference](https://arxiv.org/abs/2608.12232v1)

**作者**：Youze Huang, Penghui Ruan, Bojia Zi 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-12

### 📄 论文摘要

Geometry-aware video object scaling aims to anisotropically resize the object along object-centric axes while preserving geometric plausibility, temporal coherence, and background consistency. Existing text-guided methods mainly operate in the 2D image plane, while depth-guided approaches provide coarse control and mesh-based methods require costly 3D reconstruction. We present a progressive two-stage training framework that decouples geometry-aware foreground transformation from background preservation and realistic video composition, without mesh-pixel alignment and explicit 3D reconstruction at inference. In both stages, geometrically perturbed pseudo-sources are constructed from real videos, while the original complete videos are retained as reconstruction targets. The first stage uses planar transformations to learn robust foreground-background composition, whereas the second introduces object-centric 3D deformation guidance for geometry-aware scaling. This pseudo-source reconstruction formulation enables real-video synthesis without paired real-world scaling targets. We construct complementary paired-geometry and real-background benchmarks and further evaluate on in-the-wild videos. Extensive experiments demonstrate superior geometric consistency, foreground fidelity, and background preservation, together with faster and more practical inference than methods requiring explicit 3D reconstruction.

### 🤖 AI 总结

**一句话总结**：Geometry-aware video object scaling aims to anisotropically resize the object along object-centric axes while preserving geometric plausibility, temporal coherence, and background consistency. Existin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ScaleVid, Geometry-Aware, Video, Object, Scaling, Mesh-Free, Inference, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12232v1) | [下载PDF](https://arxiv.org/pdf/2608.12232v1.pdf)

---

## [15. Few-Shot Ordinal Learning for Day-Wise Freshness Estimation with Hyperspectral Fish Images](https://arxiv.org/abs/2608.12230v1)

**作者**：Kazi Nabiul Alam, Pooneh Bagheri Zadeh, Akbar Sheikh-Akbari  
**分类**：cs.CV, cs.AI, eess.IV, eess.SP  
**发布时间**：2026-08-12

### 📄 论文摘要

Non-destructive food quality assessment has increasingly benefited from hyperspectral imaging (HSI), which captures spectral signatures linked to biochemical changes during storage. Estimating day-wise freshness, however, remains challenging owing to strong inter-fillet variability and scarce labelled data per product. All existing deep learning approaches for HSI-based freshness prediction operate under full supervision, requiring densely annotated training sets that are costly to obtain at the individual-product level. We introduce, to the best of our knowledge, the first few-shot learning framework for HSI-based food quality estimation. Each fillet defines a distinct episodic task, and a CORAL-style ordinal prediction head captures the ranked nature of freshness progression through cumulative threshold modelling. Biologically grounded monotonicity and embedding smoothness constraints further guide predictions toward plausible trajectories. On a 16-day salmon HSI dataset under a strict unseen-fillet protocol, our method achieves a mean absolute error of 1.58 days and 2-day accuracy of 72.3% with only three labelled days per fillet, substantially outperforming scalar regression and label-distribution baselines under an identical unseen-fillet protocol.

### 🤖 AI 总结

**一句话总结**：Non-destructive food quality assessment has increasingly benefited from hyperspectral imaging (HSI), which captures spectral signatures linked to biochemical changes during storage. Estimating day-wis...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Few-Shot, Ordinal, Learning, Day-Wise, Freshness, Estimation, Hyperspectral, Fish

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12230v1) | [下载PDF](https://arxiv.org/pdf/2608.12230v1.pdf)

---

## [16. SCOUT: Unlocking Enhanced Spatial Reasoning via Structured Chain-of-Thought and Multi-Objective Process Reward](https://arxiv.org/abs/2608.12220v1)

**作者**：Zile Zhou, Huining Yuan, Weichen Zhang 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-12

### 📄 论文摘要

Existing Vision-Language Models (VLMs) exhibits a critical bottleneck in robust spatial reasoning. Recent reinforcement learning (RL) methods aim to close this gap with verifiable outcomes, yet they suffer from poor credit assignment across intermediate reasoning steps. Concurrently, structured reasoning approaches overlook the critical depth perception necessary for comprehensive 3D understanding. To address these challenges, we propose SCOUT (Structured Chain-Of-Thought Utilizing Process-Supervised RL Training). Specifically, we design a structured Chain-of-Thought (CoT) framework that explicitly models 3D environmental perception to ensure robust spatial understanding and reasoning. Furthermore, we introduce a novel RL algorithm featuring multi-objective process rewards and a tailored advantage estimation method, facilitating fine-grained credit assignment across distinct segments of the reasoning trajectory. To support our framework, we develop SCOUT-24k, a structured spatial reasoning CoT dataset synthesized through a customized pipeline. Extensive evaluations demonstrate that SCOUT-3B improves upon baseline models by 16.85% and 6.3% on general spatial benchmarks and complex spatial reasoning tasks respectively. Notably, our larger SCOUT-7B even outperforms GPT-4o by a margin of 4.28%. Moreover, despite being trained exclusively on single image, SCOUT-7B exhibits robust out-of-domain generalization to multi-image and video scenarios. These empirical results render SCOUT as a critical step towards next generation of spatially-aware VLMs.

### 🤖 AI 总结

**一句话总结**：Existing Vision-Language Models (VLMs) exhibits a critical bottleneck in robust spatial reasoning. Recent reinforcement learning (RL) methods aim to close this gap with verifiable outcomes, yet they s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SCOUT, Unlocking, Enhanced, Spatial, Reasoning, via, Structured, Chain-of-Thought

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12220v1) | [下载PDF](https://arxiv.org/pdf/2608.12220v1.pdf)

---

## [17. GeoFlow: Efficient Driving Video Generation via Geometry-Aligned Priors](https://arxiv.org/abs/2608.12203v1)

**作者**：Jiazheng Liu, Hang Li, Jiawei Zhang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-12

### 📄 论文摘要

Generative models like Diffusion Models and Flow Matching have demonstrated remarkable capabilities in synthesizing high-fidelity driving videos, but are severely constrained by high inference latency due to the requirement of extensive sampling steps. We argue that this inefficiency stems from the prevailing reliance on a standard Gaussian source distribution, where consecutive frames are initialized as independent Gaussian noise. This paradigm disregards the rich spatiotemporal correlations inherent in driving videos, compelling the model to regenerate deterministic scene structures existing in previous frames from noise, which is both computationally redundant and prone to geometric inconsistency. To address this problem, we propose GeoFlow, a novel framework designed to achieve efficient driving video generation by harnessing explicit geometric priors. Instead of sampling from standard Gaussian noise, we leverage multi-view geometry and spatially-adaptive noise injection to construct a Geometry-Aligned Prior (GAP) distribution as starting point. This initialization bridges the gap between source distribution and data distribution, yielding a significantly straighter and shorter sampling trajectory. Extensive experiments demonstrate that GeoFlow can achieve remarkable efficiency of both training and inference: merely several hours of fine-tuning on baseline models can significantly boost few-step generation quality, while fully converged training drastically reduces number of inference steps required for state-of-the-art video generation.

### 🤖 AI 总结

**一句话总结**：Generative models like Diffusion Models and Flow Matching have demonstrated remarkable capabilities in synthesizing high-fidelity driving videos, but are severely constrained by high inference latency...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GeoFlow, Efficient, Driving, Video, Generation, via, Geometry-Aligned, Priors

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12203v1) | [下载PDF](https://arxiv.org/pdf/2608.12203v1.pdf)

---

## [18. M-Net: Integrating Spectral Features and Physical Field Operators into Deep Learning for Medical Image Segmentation](https://arxiv.org/abs/2608.12196v1)

**作者**：Jing Zhu, Ye Wang, Fumin Wang  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-12

### 📄 论文摘要

Purpose: Deep learning-based medical image segmentation has achieved remarkable success, yet purely data-driven approaches often fail to exploit the rich mathematical structure inherent in medical images. We investigate whether explicit mathematical inductive biases, specifically matrix spectral analysis and vector calculus operators, can enhance segmentation beyond data-driven learning alone. Methods: We propose M-Net (Math-Augmented Network), which integrates three complementary mathematical priors into U-Net: (1) continuous spectral features derived from the condition number of centered local pixel matrices, providing a differentiable measure of texture ill-conditioning; (2) physical field operators (divergence and a discrete curl-like boundary irregularity operator) computed from image gradient fields, capturing focal intensity extrema and edge non-smoothness; and (3) a Math-Attention Gate (MAG) that adaptively fuses mathematical features with CNN-extracted deep features at skip connections. Results: Experiments on three benchmarks (LiTS, KiTS, and BraTS) show that M-Net achieves Dice scores of 78.42%, 76.15%, and 83.67%, outperforming baseline U-Net by 12.37%, 3.52%, and 5.55% on liver, kidney, and brain tumor segmentation, respectively. Ablations reveal that the condition-number feature contributes a 2.14% gain over binary invertibility features, while MAG adds 1.45% over simple concatenation. Conclusion: M-Net establishes that mathematical inductive biases provide effective complementary information for medical image segmentation. The continuous condition-number feature offers superior gradient information over discrete alternatives, and MAG preserves these priors throughout the network. This work opens avenues for integrating linear algebra and vector calculus into deep architectures for medical imaging.

### 🤖 AI 总结

**一句话总结**：Purpose: Deep learning-based medical image segmentation has achieved remarkable success, yet purely data-driven approaches often fail to exploit the rich mathematical structure inherent in medical ima...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：M-Net, Integrating, Spectral, Features, Physical, Field, Operators, Deep

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12196v1) | [下载PDF](https://arxiv.org/pdf/2608.12196v1.pdf)

---

## [19. HSTGFormer: Hyper Spatial-Temporal Graph Transformer for 3D Human Pose Estimation](https://arxiv.org/abs/2608.12187v1)

**作者**：Ruochen Li, Shuang Chen, Wenke E 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-12

### 📄 论文摘要

Transformer-based methods have achieved strong performance in monocular 3D human pose estimation, but most existing approaches organise spatial and temporal reasoning as separate stages, which may weaken unified spatial-temporal interdependencies inherent in human motion and compress frame-level structural information before temporal modelling. In this paper, we propose HSTGFormer, a graph-enhanced Transformer framework that reformulates spatial-temporal reasoning as localised coupled graph aggregation over joint-time nodes. Specifically, HSTGFormer introduces a Hyper Spatial-Temporal Graph (HSTG), which decomposes global spatial-temporal reasoning into local spatial-temporal receptive fields around individual joint-time nodes by extending per-frame skeleton graphs into temporal neighbourhoods, thereby enabling structure-aware coupled reasoning while preserving local structural motion information. It further incorporates an Adaptive Dual-Scale Temporal Graph (ADSTG) to capture joint-specific temporal dependencies over complementary short- and long-range windows. A lightweight node-wise fusion module further adaptively integrates the two graph representations for each joint-time node. Experiments on Human3.6M and MPI-INF-3DHP show that HSTGFormer achieves strong accuracy with high computational efficiency.

### 🤖 AI 总结

**一句话总结**：Transformer-based methods have achieved strong performance in monocular 3D human pose estimation, but most existing approaches organise spatial and temporal reasoning as separate stages, which may wea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, HSTGFormer, Hyper, Spatial-Temporal, Graph, Transformer, Human, Pose

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12187v1) | [下载PDF](https://arxiv.org/pdf/2608.12187v1.pdf)

---

## [20. GenFAR: A generalized representation of brain structure, derived from 49,246 multi-cohort MRIs via deep learning](https://arxiv.org/abs/2608.12185v1)

**作者**：Vishnu M. Bashyam, Guray Erus, Junhao Wen 等 32 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-12

### 📄 论文摘要

Deep learning models for neuroimaging have largely been developed for individual tasks, limiting knowledge transfer across applications. Here we introduce GenFAR, a modular deep learning framework that learns general, clinically informed features from brain MRIs. We trained this modular architecture on 49,246 individuals across 11 cohorts, using 17 diverse classification and regression tasks spanning cognition, clinical, diagnosis, demographics, and biomarkers. This yields aggregated, focused feature sets that capture rich, clinically- and biologically-relevant brain representations. We developed a sequential learning approach where tasks progressively build on previously learned representations. Through an analysis of 5,000 task sequences, we identified an optimal sequence length of six tasks and introduced a Donor Score metric to quantify each task's contribution to downstream performance. This analysis revealed five consistently strong donor tasks (Age, AD/MCI, MMSE, Hypertension, Hyperlipidemia) that formed the base of our sequential model. We demonstrated the utility of our learned representation, in various tasks beyond those included in the training set, to serve as the foundation for specialized secondary predictors. We further showed that using the learned feature representation can substantially increase the sample efficiency of secondary deep learning training tasks and models, as well as improve their accuracy.

### 🤖 AI 总结

**一句话总结**：Deep learning models for neuroimaging have largely been developed for individual tasks, limiting knowledge transfer across applications. Here we introduce GenFAR, a modular deep learning framework tha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, GenFAR, generalized, representation, brain, structure, derived, multi-cohort

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12185v1) | [下载PDF](https://arxiv.org/pdf/2608.12185v1.pdf)

---

## [21. Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs](https://arxiv.org/abs/2608.12179v1)

**作者**：Yung-Hsu Yang, Luigi Piccinelli, Samuel Rota Bulò 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-12

### 📄 论文摘要

Metric 3D object detection is a core capability for embodied agents, yet most reliable systems lean on depth sensors, trading away cost, power, and integration simplicity. This motivates monocular 3D detection, which avoids additional constraints, yet it faces a major obstacle: from a single image, depth, and especially absolute scale, are underconstrained. As a result, the prevailing pattern of detecting in 2D and then predicting 3D attributes is often brittle, since modest range errors can dominate 3D localization, and the learned scale prior can fail when cameras, motion, or environments undergo domain shifts. To address this, we propose Map-Det3D, an online multi-view 3D object detection model that brings detection directly into a 3D space reconstructed from RGB. We map a short temporal window into multiple views and repurpose a feed-forward metric 3D reconstruction model as our geometric backbone while tuning its object-aware capabilities. Building on this representation, Map-Det3D directly predicts boxes in metric 3D space, without the widely used 2D-to-3D lifting. Experiments across different benchmarks show that this design supports strong online performance and robust transfer without adaptation, suggesting that training reconstruction priors for detection is a practical route to stable metric 3D detection from monocular video. Code and models are available at https://royyang0714.github.io/Map-Det3D.

### 🤖 AI 总结

**一句话总结**：Metric 3D object detection is a core capability for embodied agents, yet most reliable systems lean on depth sensors, trading away cost, power, and integration simplicity. This motivates monocular 3D ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Map-Det3D, Metric, Feed-Forward, Reconstruction, Prior, Multi-view, Object

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12179v1) | [下载PDF](https://arxiv.org/pdf/2608.12179v1.pdf)

---

## [22. TGRHuman: Text-Guided Realistic 3D Human Generation via Diffusion Renderer](https://arxiv.org/abs/2608.12175v1)

**作者**：Muxin Zhang, Chaohui Yu, Yuanwang Yang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-12

### 📄 论文摘要

Realistic 3D human generation plays a crucial role in many graphics applications. However, current methods still struggle to generate high-quality human geometry and texture while maintaining 3D consistency and inference efficiency. In this work, we address these limitations by introducing TGRHuman, a novel approach for generating realistic 3D humans from text. Our method decouples geometry and texture generation to alleviate the issues commonly encountered in NeRF-based methods. Instead of relying on slow, implicit score-distillation-based optimization, we directly use explicit multi-view observation generation and optimization for efficient 3D synthesis. For geometry generation, we propose a high-resolution generative module for multi-view normals together with a geometry-carving strategy that preserves view consistency and supports loose clothing. For texture generation, we produce spatially consistent RGB observations from densely sampled surrounding views using a carefully designed texture-prior acquisition strategy and a diffusion renderer, enabling detailed human texture synthesis. Experiments show that our method can generate high-quality and consistent 3D human geometry and texture efficiently. TGRHuman outperforms existing text-to-3D human methods in both geometry and texture quality.

### 🤖 AI 总结

**一句话总结**：Realistic 3D human generation plays a crucial role in many graphics applications. However, current methods still struggle to generate high-quality human geometry and texture while maintaining 3D consi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Diffusion, TGRHuman, Text-Guided, Realistic, Human, Generation, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12175v1) | [下载PDF](https://arxiv.org/pdf/2608.12175v1.pdf)

---

## [23. Context Blindness in DPO: Mitigating Object Hallucination in MLLMs via Context-Calibrated Preference Optimization](https://arxiv.org/abs/2608.12158v1)

**作者**：Byungoh Ko, Jinyoung Park, Jongha Kim 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-12

### 📄 论文摘要

Multimodal large language models (MLLMs) have made rapid progress, yet they still exhibit object hallucination, generating plausible but incorrect descriptions that are inconsistent with the visual input. Direct Preference Optimization (DPO) mitigates this by training models to prefer non-hallucinated responses over hallucinated ones, and recent efforts further enrich the preference data with relevant context. However, it remains unclear whether DPO actually leverages such context. To investigate this, we propose Contextual Preference Gain (CPG), a simple metric that measures how much a model's preference strengthens when relevant context is provided. We find that higher CPG consistently corresponds to lower hallucination, yet standard DPO and its variants exhibit only limited CPG, indicating that they underutilize contextual information and thus remain prone to hallucination. To address this, we propose Context-Calibrated DPO (C$^2$-DPO), which directly maximizes CPG while preserving the original preference ordering. Across multiple benchmarks, C$^2$-DPO substantially reduces hallucination without compromising general reasoning, relatively reducing the Object HalBench hallucination rate of Qwen2-VL-Instruct-2B by 36%. Code is available at https://github.com/mlvlab/C2-DPO

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) have made rapid progress, yet they still exhibit object hallucination, generating plausible but incorrect descriptions that are inconsistent with the visual in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Context, Blindness, DPO, Mitigating, Object, Hallucination, MLLMs, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12158v1) | [下载PDF](https://arxiv.org/pdf/2608.12158v1.pdf)

---

## cs.LG

## [24. Redistribution-based Cost Inference Improves Sparse Safe Offline RL](https://arxiv.org/abs/2608.12306v1)

**作者**：Ebenezer Gelo, Geraud Nangue Tasse, Steven James 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-12

### 📄 论文摘要

Safe offline RL typically assumes access to dense per-step cost annotations, but in practice supervisors provide only trajectory-level stop-feedback: a binary signal at the first unsafe transition, with no per-step attribution. We frame this as a temporal credit assignment problem and propose the Redistribution-based Cost Inference (RCI) framework, which converts sparse stop-feedback into dense per-step costs via return decomposition, then trains a constrained offline policy on the augmented dataset. We show that return-equivalent redistribution preserves the feasible policy set and the optimal Lagrangian in a CMDP, establishing that the transformation is lossless in theory while yielding better-conditioned cost critic learning in practice. Experiments on highway driving and robotic manipulation demonstrate substantially lower violation rates than sparse and classifier-based baselines, with robustness to heterogeneous dataset compositions and label noise.

### 🤖 AI 总结

**一句话总结**：Safe offline RL typically assumes access to dense per-step cost annotations, but in practice supervisors provide only trajectory-level stop-feedback: a binary signal at the first unsafe transition, wi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Redistribution-based, Cost, Inference, Improves, Sparse, Safe, Offline

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12306v1) | [下载PDF](https://arxiv.org/pdf/2608.12306v1.pdf)

---

## [25. A Framework for Designing Reward Functions: From Objectives to Features to Human-Aligned Reward Functions](https://arxiv.org/abs/2608.12302v1)

**作者**：Di Yang Shi, W. Bradley Knox  
**分类**：cs.LG  
**发布时间**：2026-08-12

### 📄 论文摘要

We present a formal process to enable non-experts to instantiate and iterate on human-aligned reward functions, i.e. reward functions that adhere to a given preference ordering over trajectories. Given a task described in natural language, our process produces a linear reward function in three steps: distill the task's objectives into a set of fundamental objectives and derive measurable outcome variables that capture those fundamental objectives, select a causally representative subset of outcome variables as the reward terms, and fit weights to those reward terms via preference elicitation. Our contributions describe the first step and formalize the latter two steps. The first is a guided workflow for deriving outcome variables. The second is a reduction of reward term selection to minimum-cost partial cover on a causal DAG, solved in polynomial time via max-flow. The third is a geometric framing of weight fitting as a convex feasibility problem iteratively narrowed by preference queries, solved by existing separation oracle methods. To the best of our knowledge, this is the first reward-design method that maintains a deterministically conflict-free feasible weight region, narrowed to a desired tolerance via a separation oracle with O(n log κ) preference queries.

### 🤖 AI 总结

**一句话总结**：We present a formal process to enable non-experts to instantiate and iterate on human-aligned reward functions, i.e. reward functions that adhere to a given preference ordering over trajectories. Give...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Framework, Designing, Reward, Functions, Objectives, Features, Human-Aligned

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12302v1) | [下载PDF](https://arxiv.org/pdf/2608.12302v1.pdf)

---

## [26. Earth observation embeddings are effective sub-grid descriptors for probabilistic weather downscaling](https://arxiv.org/abs/2608.12271v1)

**作者**：Pedro Sousa, Will Tebbutt, Sadiq Jaffer 等 6 位作者  
**分类**：cs.LG, physics.ao-ph  
**发布时间**：2026-08-12

### 📄 论文摘要

Global weather reanalyses and forecasts resolve the evolving atmospheric state on coarse grids, but site-specific applications require predictions at arbitrary locations where near-surface conditions also depend on unresolved terrain and land-surface properties. Existing probabilistic downscalers address this gap using hand-crafted topographic descriptors. We ask instead whether Earth observation foundation models can provide transferable sub-grid surface representations for probabilistic weather downscaling.   We augment a convolutional conditional neural process that downscales coarse ERA5 reanalysis fields at ~25 km resolution with a learned local surface descriptor, obtained by compressing a patch of TESSERA embeddings at 10 m resolution. Although these embeddings summarise surface conditions over annual timescales, they improve downscaling of instantaneous 2 m temperature and 10 m wind speed by encoding persistent surface properties that capture a location's departure from the coarse-grid atmospheric state. Across five climatically diverse regions, the embedding improves point and probabilistic skill at stations held out in both space and time, overall improving CRPS skill by 11.5% for 2 m temperature and 6.2% for 10 m wind speed. We further analyse how its contribution differs by variable, finding that topography explains more of temperature's sub-grid structure, while TESSERA provides additional surface information for wind speed.   These improvements persist when the coarse input is changed from ERA5 to forecasts from the Aurora AI forecasting model, and when predicting at newly deployed stations with no regional history. To our knowledge, this is the first evidence that long-timescale Earth-observation embeddings can support short-timescale weather downscaling where sub-grid departures are systematically structured by persistent surface properties.

### 🤖 AI 总结

**一句话总结**：Global weather reanalyses and forecasts resolve the evolving atmospheric state on coarse grids, but site-specific applications require predictions at arbitrary locations where near-surface conditions ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Earth, observation, embeddings, effective, sub-grid, descriptors, probabilistic, weather

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12271v1) | [下载PDF](https://arxiv.org/pdf/2608.12271v1.pdf)

---

## [27. Calibration Bets on the Past: Post-Training Quantization for Financial Time-Series Forecasting](https://arxiv.org/abs/2608.12259v1)

**作者**：Junyi Ye, Ivy Gateri Wanjiku  
**分类**：cs.LG, q-fin.ST  
**发布时间**：2026-08-12

### 📄 论文摘要

Financial forecasting models are typically developed in full precision, yet production deployment often requires low-precision inference to reduce memory and computational cost. Post-training quantization (PTQ) enables such deployment without retraining. However, reliable activation quantization requires calibration: activation ranges are estimated from historical data before deployment and then remain fixed during future inference. The importance of this deployment choice for financial forecasting remains poorly understood. We present a systematic study of activation calibration for PTQ in cross-sectional volatility forecasting on the S&P 500. Our evaluation covers seven representative neural architectures, eight walk-forward test years (2018-2025), and 560 trained models. We find that activation calibration has little effect at 8 bits but becomes the primary determinant of predictive performance at 4 bits. Under default absolute-maximum (abs-max) calibration, static 4-bit quantization of both weights and activations removes 11-62% of the full-precision mean information coefficient in affected architectures. Replacing abs-max with percentile calibration recovers 53-94% of this degradation in the four most affected architectures. The preferred activation range also varies across market periods. Narrow ranges improve resolution under typical market conditions but lose part of their advantage when test-period market dispersion exceeds the calibration history. These findings show that activation calibration is a first-class deployment decision for reliable 4-bit PTQ in financial forecasting. When substantial degradation remains, 8-bit activations or weight-only 4-bit quantization provide more robust deployment choices.

### 🤖 AI 总结

**一句话总结**：Financial forecasting models are typically developed in full precision, yet production deployment often requires low-precision inference to reduce memory and computational cost. Post-training quantiza...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Calibration, Bets, Past, Post-Training, Quantization, Financial, Time-Series, Forecasting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12259v1) | [下载PDF](https://arxiv.org/pdf/2608.12259v1.pdf)

---

## [28. An Efficient Near-Optimal Algorithm for Adversarial $m$-Set Bandits](https://arxiv.org/abs/2608.12231v1)

**作者**：Francesco Bacchiocchi, Tommaso Cesari, Roberto Colomboni  
**分类**：cs.LG  
**发布时间**：2026-08-12

### 📄 论文摘要

We study adversarial combinatorial bandits with $m$-set actions, where at each round the learner selects $m$ out of $d$ items and observes only the aggregate loss of the selected items. The resulting action set contains $K=\binom{d}{m}$ elements and can therefore be exponentially large. Nevertheless, the loss of every action is determined by the same $d$-dimensional vector of item losses. We propose a computationally efficient algorithm that exploits this structure without explicitly enumerating the action set. Against adaptive non-anticipating adversaries, it guarantees, with probability at least $1-δ$, regret against the best fixed action of \[   R_T =   O\left(\sqrt{dT\log(K/δ)}\right). \] This matches the high-probability regret bound of the finite-action EXP3-KW algorithm of Zimmert and Lattimore, whose direct implementation may require exponential space. Our algorithm instead represents each sampling distribution with $d$ parameters and runs in polynomial time without enumerating the action set. Thus, it resolves the open problem posed by Maiti et al.

### 🤖 AI 总结

**一句话总结**：We study adversarial combinatorial bandits with $m$-set actions, where at each round the learner selects $m$ out of $d$ items and observes only the aggregate loss of the selected items. The resulting ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, We, Efficient, Near-Optimal, Algorithm, Adversarial, $m$-Set, Bandits

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12231v1) | [下载PDF](https://arxiv.org/pdf/2608.12231v1.pdf)

---

## [29. ScreenShot: A Foundation Model for Few-Shot Combination Drug Screening](https://arxiv.org/abs/2608.12219v1)

**作者**：Antoine de Mathelin, Christopher Tosh, Wesley Tansey  
**分类**：cs.LG  
**发布时间**：2026-08-12

### 📄 论文摘要

Treating patients with combinations of drugs reduces the risk of resistance to any individual drug. Finding effective combinations is difficult because the large search space makes combinatorial screens prohibitively expensive, time consuming, and often technically infeasible. Predictive models can fill this gap, yet existing methods typically require molecular profiling of each sample and per-cohort training, limiting their applicability when time and tissue are scarce. To address this challenge, we introduce ScreenShot, a hierarchical transformer pretrained on 40 drug screening datasets covering 3,700 drugs and 6,000 biological samples, whose architecture mirrors the nested structure of screening data. Given a few-shot context of observations from a new patient, ScreenShot predicts the response of the sample to combination therapies through in-context learning, operating directly on functional measurements with no fine-tuning and no molecular profiling. On four held-out datasets, ScreenShot outperforms all baselines in both prediction accuracy and identification of selectively effective treatments. ScreenShot's internal representations are directly useful for experimental design: we use them to drive a weighted k-means++ active learning strategy that selects which experiments to run, achieving the same hit detection as uniform screening with a third of the budget. Source code and interactive dashboard: https://github.com/tansey-lab/screenshot.

### 🤖 AI 总结

**一句话总结**：Treating patients with combinations of drugs reduces the risk of resistance to any individual drug. Finding effective combinations is difficult because the large search space makes combinatorial scree...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ScreenShot, Foundation, Model, Few-Shot, Combination, Drug, Screening, Treating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12219v1) | [下载PDF](https://arxiv.org/pdf/2608.12219v1.pdf)

---

## [30. HYDRA: Hyperbolic Dynamic Representation Architecture for Kolmogorov-Arnold Networks](https://arxiv.org/abs/2608.12194v1)

**作者**：Zhao Su, Yuxin Xia, Haoran Li 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-12

### 📄 论文摘要

Kolmogorov-Arnold Networks (KANs) enhance nonlinear function approximation by replacing scalar weights with learnable univariate functions. However, assigning an independent function to every connection results in substantial parameter redundancy, limiting their scalability and efficiency. To reduce this redundancy, we introduce \textbf{HY}perbolic \textbf{D}ynamic \textbf{R}epresentation \textbf{A}rchitecture (HYDRA), a parameter-efficient hyperbolic extension of KAN that combines spline-based functional learning with representations in the Poincaré ball. HYDRA maps vector-valued inputs into a bounded hyperbolic latent space, performs KAN-style updates in tangent space, and employs a low-rank prototype block to share functional transformations across hidden dimensions. The resulting hyperbolic representations provide a structured radial coordinate for interpretation, while radius control improves training stability by preventing boundary saturation. Extensive experiments across eight benchmark datasets demonstrate that HYDRA consistently achieves competitive or superior predictive performance while improving parameter efficiency and representation interpretability.

### 🤖 AI 总结

**一句话总结**：Kolmogorov-Arnold Networks (KANs) enhance nonlinear function approximation by replacing scalar weights with learnable univariate functions. However, assigning an independent function to every connecti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HYDRA, Hyperbolic, Dynamic, Representation, Architecture, Kolmogorov-Arnold, Networks, KANs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.12194v1) | [下载PDF](https://arxiv.org/pdf/2608.12194v1.pdf)

---

