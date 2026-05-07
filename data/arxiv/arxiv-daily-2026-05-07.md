# arXiv AI 论文日报 | 2026-05-07

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (9 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (1 篇)
- [cs.LG](#csLG) (15 篇)

---

## cs.AI

## [1. LongSeeker: Elastic Context Orchestration for Long-Horizon Search Agents](https://arxiv.org/abs/2605.05191v1)

**作者**：Yijun Lu, Rui Ye, Yuwen Du 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-06

### 📄 论文摘要

Long-horizon search agents must manage a rapidly growing working context as they reason, call tools, and observe information. Naively accumulating all intermediate content can overwhelm the agent, increasing costs and the risk of errors. We propose that effective context management should be adaptive: parts of the agent's trajectory are maintained at different levels of detail depending on their current relevance to the task. To operationalize this principle, we introduce Context-ReAct, a general agentic paradigm for elastic context orchestration that integrates reasoning, context management, and tool use in a unified loop. Context-ReAct provides five atomic operations: Skip, Compress, Rollback, Snippet and Delete, which allow the agent to dynamically reshape its working context, preserving important evidence, summarizing resolved information, discarding unhelpful branches, and controlling context size. We prove that the Compress operator is expressively complete, while the other specialized operators provide efficiency and fidelity guarantees that reduce generation cost and hallucination risk. Building on this paradigm, we develop LongSeeker, a long-horizon search agent fine-tuned from Qwen3-30B-A3B on 10k synthesized trajectories. Across four representative search benchmarks, LongSeeker achieves 61.5% on BrowseComp and 62.5% on BrowseComp-ZH, substantially outperforming Tongyi DeepResearch (43.2% and 46.7%) and AgentFold (36.2% and 47.3%). These results highlight the potential of adaptive context management, showing that agents can achieve more reliable and efficient long-horizon reasoning by actively shaping their working memory.

### 🤖 AI 总结

**一句话总结**：Long-horizon search agents must manage a rapidly growing working context as they reason, call tools, and observe information. Naively accumulating all intermediate content can overwhelm the agent, inc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, LongSeeker, Elastic, Context, Orchestration, Long-Horizon, Search, must

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05191v1) | [下载PDF](https://arxiv.org/pdf/2605.05191v1.pdf)

---

## cs.CL

## [2. Implicit Representations of Grammaticality in Language Models](https://arxiv.org/abs/2605.05197v1)

**作者**：Yingshan Susan Wang, Linlu Qiu, Zhaofeng Wu 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-06

### 📄 论文摘要

Grammaticality and likelihood are distinct notions in human language. Pretrained language models (LMs), which are probabilistic models of language fitted to maximize corpus likelihood, generate grammatically well-formed text and discriminate well between grammatical and ungrammatical sentences in tightly controlled minimal pairs. However, their string probabilities do not sharply discriminate between grammatical and ungrammatical sentences overall. But do LMs implicitly acquire a grammaticality distinction distinct from string probability? We explore this question through studying internal representations of LMs, by training a linear probe on a dataset of grammatical and (synthetic) ungrammatical sentences obtained by applying perturbations to a naturalistic text corpus. We find that this simple grammaticality probe generalizes to human-curated grammaticality judgment benchmarks and outperforms LM probability-based grammaticality judgments. When applied to semantic plausibility benchmarks, in which both members of a minimal pair are grammatical and differ in only plausibility, the probe however performs worse than string probability. The English-trained probe also exhibits nontrivial cross-lingual generalization, outperforming string probabilities on grammaticality benchmarks in numerous other languages. Additionally, probe scores correlate only weakly with string probabilities. These results collectively suggest that LMs acquire to some extent an implicit grammaticality distinction within their hidden layers.

### 🤖 AI 总结

**一句话总结**：Grammaticality and likelihood are distinct notions in human language. Pretrained language models (LMs), which are probabilistic models of language fitted to maximize corpus likelihood, generate gramma...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Implicit, Representations, Grammaticality, Language, Models, likelihood, distinct

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05197v1) | [下载PDF](https://arxiv.org/pdf/2605.05197v1.pdf)

---

## [3. PSK at SemEval-2026 Task 9: Multilingual Polarization Detection Using Ensemble Gemma Models with Synthetic Data Augmentation](https://arxiv.org/abs/2605.05159v1)

**作者**：Srikar Kashyap Pulipaka  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-05-06

### 📄 论文摘要

We present our system for SemEval-2026 Task 9: Multilingual Polarization Detection, a binary classification task spanning 22 languages. Our approach fine-tunes separate Gemma~3 models (12B and 27B parameters) per language using Low-Rank Adaptation (LoRA), augmented with synthetic data generated by a large language model (LLM). We employ three synthetic data strategies (direct generation, paraphrasing, and contrastive pair creation) using GPT-4o-mini, with a multi-stage quality filtering pipeline including embedding-based deduplication. We find that per-language threshold tuning on the development set yields 2 to 4\% F1 improvements without retraining. We also use weighted ensembles of 12B and 27B model predictions with per-language strategy selection. Our final system achieves a mean macro-F1 of 0.811 across all 22 languages, ranking 2nd overall of the participating teams, with 1st place finishes in 3 languages and top-3 in 8 languages. We also find that alternative architectures (XLM-RoBERTa, Qwen3) that showed strong development set performance suffered 30 to 50\% F1 drops on the test set, highlighting the importance of generalization.

### 🤖 AI 总结

**一句话总结**：We present our system for SemEval-2026 Task 9: Multilingual Polarization Detection, a binary classification task spanning 22 languages. Our approach fine-tunes separate Gemma~3 models (12B and 27B par...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, PSK, SemEval-2026, Task, Multilingual, Polarization, Detection, Ensemble

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05159v1) | [下载PDF](https://arxiv.org/pdf/2605.05159v1.pdf)

---

## [4. Beyond Semantics: An Evidential Reasoning-Aware Multi-View Learning Framework for Trustworthy Mental Health Prediction](https://arxiv.org/abs/2605.05121v1)

**作者**：Yucheng Ruan, Ling Huang, Qika Lin 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-06

### 📄 论文摘要

Automated mental health prediction using textual data has shown promising results with deep learning and large language models. However, deploying these models in high-stakes real-world settings remains challenging, as existing approaches largely rely on semantic representations and often produce overconfident predictions under ambiguous, noisy, or shifted data. Moreover, most methods lack reliable uncertainty estimation, undermining trust in risk-sensitive mental health applications. To address these limitations, we formulate the task as a multi-view learning problem that integrates semantic information from encoder-only models with higher-level reasoning information from decoder-only models, where reasoning-aware representations and uncertainty modeling are obtained in a trustworthy manner. To ensure reliable fusion, we adopt an evidential learning framework based on Subjective Logic to explicitly model uncertainty and introduce an evidential fusion strategy that balances complementary views while discounting unreliable evidence. Benchmarking on three real-world datasets, Dreaddit, SDCNL, and DepSeverity, reports accuracies of 0.835, 0.731, and 0.751, respectively, demonstrating its potential for reliable mental health prediction. Additional experiments on robustness to noise and case studies for interpretability confirm that our proposed framework not only improves predictive performance but also provides trustworthy uncertainty estimates and human-understandable reasoning signals, making it suitable for risk-sensitive applications in mental health assessment.

### 🤖 AI 总结

**一句话总结**：Automated mental health prediction using textual data has shown promising results with deep learning and large language models. However, deploying these models in high-stakes real-world settings remai...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Beyond, Semantics, Evidential, Reasoning-Aware, Multi-View, Learning, Framework

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05121v1) | [下载PDF](https://arxiv.org/pdf/2605.05121v1.pdf)

---

## [5. Text Corpora as Concept Fields: Black-Box Hallucination and Novelty Measurement](https://arxiv.org/abs/2605.05103v1)

**作者**：Nicholas S. Kersting, Vittorio Castelli, Chieh Ting Yeh 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.CY  
**发布时间**：2026-05-06

### 📄 论文摘要

We introduce the **Concept Field** of a text corpus: a local drift field with pointwise uncertainty, estimated in sentence-embedding space from the deltas between consecutive sentences. Given a candidate sentence transition, we score its agreement with the field by $ζ$, the mean absolute z-distance between the observed delta and the field's local Gaussian estimate. The score is black-box (no model internals), corpus-attributable (every score traces to nearby corpus sentences), and admits a direct probabilistic reading. We support the computation with the introduction of a **Vector Sequence Database (VSDB)** that stores embeddings together with sequence-position and next-delta metadata. We evaluate this approach on two large-scale settings: hallucination-style groundedness detection over the U.S. Code of Federal Regulations, and novelty detection over Project Gutenberg. Using controlled LLM-generated rewrites, Concept Fields achieve strong selective classification performance under a grounded / ungrounded / unsure triage policy, which unlike retrieval-centric baselines have similar coverage-risk behavior across both domains, supporting a probability-based interpretation that transfers across domains. We also sketch how divergence and curl of the Concept Field, computed on dense clusters, surface qualitatively meaningful semantic patterns (logic sources, sinks, and implicit topics), which we offer as hypothesis-generating rather than as a quantitative result. Concept Fields provide a fast, lightweight, and interpretable signal for groundedness and novelty, complementary to LLM-as-judge and white-box detectors.

### 🤖 AI 总结

**一句话总结**：We introduce the **Concept Field** of a text corpus: a local drift field with pointwise uncertainty, estimated in sentence-embedding space from the deltas between consecutive sentences. Given a candid...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Text, Corpora, Concept, Fields, Black-Box, Hallucination, Novelty

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05103v1) | [下载PDF](https://arxiv.org/pdf/2605.05103v1.pdf)

---

## [6. The Pinocchio Dimension: Phenomenality of Experience as the Primary Axis of LLM Psychometric Differences](https://arxiv.org/abs/2605.05080v1)

**作者**：Hubert Plisiecki, Sabina Siudaj, Kacper Dudzic 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-06

### 📄 论文摘要

We administer 45 validated psychometric questionnaires to 50 large language models (LLMs) to identify the dimensions along which LLMs differ psychometrically. Using Supervised Semantic Differential (SSD), we find that the primary axis of between-model variance separates items describing phenomenally rich experience, including embodied sensation, felt affect, inner speech, imagery, and empathy, from items describing stimulus-driven behavioral reactivity ($R^2_{adj}=.037$, $p<.0001$). To test this hypothesis at the item level, we introduce the Pinocchio score ($π_i$), the ratio of inter-model response variance under neutral prompting to that under a human-simulation prompt, as an annotation-free measure of each item's experiential demand. $π_i$ predicts condition-induced shifts in primary factor loading magnitudes ($ρ=-.215$, $p<.0001$, $n=1292$--$1310$ items), confirming that between-model divergence on experiential items is structured rather than noisy. Applying PCA to per-model EFA scores across all questionnaires reveals one dominant dimension, the Pinocchio Axis ($Π$): the degree to which a model presents itself as a locus of phenomenal experience rather than a system of behavioral responses. This axis captures 47.1% of cross-questionnaire between-model variance in primary factor scores and converges with item-level Pinocchio scores ($r=.864$). Marked within-provider divergence across closely related model variants is consistent with post-training fine-tuning as a key contributor, supporting the interpretation that $Π$ reflects a training-shaped self-representational tendency governing how a model treats experiential language as self-applicable. The dominant axis of between-model psychometric variation is therefore not a conventional personality trait but a self-representational stance toward one's own nature as an experiencer.

### 🤖 AI 总结

**一句话总结**：We administer 45 validated psychometric questionnaires to 50 large language models (LLMs) to identify the dimensions along which LLMs differ psychometrically. Using Supervised Semantic Differential (S...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, as, Pinocchio, Dimension, Phenomenality, Experience, Primary, Axis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05080v1) | [下载PDF](https://arxiv.org/pdf/2605.05080v1.pdf)

---

## cs.CV

## [7. Syn4D: A Multiview Synthetic 4D Dataset](https://arxiv.org/abs/2605.05207v1)

**作者**：Zeren Jiang, Yushi Lan, Yihang Luo 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-06

### 📄 论文摘要

Dense 3D reconstruction and tracking of dynamic scenes from monocular video remains an important open challenge in computer vision. Progress in this area has been constrained by the scarcity of high-quality datasets with dense, complete, and accurate geometric annotations. To address this limitation, we introduce Syn4D, a multiview synthetic dataset of dynamic scenes that includes ground-truth camera motion, depth maps, dense tracking, and parametric human pose annotations. A key feature of Syn4D is the ability to unproject any pixel into 3D to any time and to any camera. We conduct extensive evaluations across multiple downstream tasks to demonstrate the utility and effectiveness of the proposed dataset, including 4D scene reconstruction, 3D point tracking, geometry-aware camera retargeting, and human pose estimation. The experimental results highlight Syn4D's potential to facilitate research in dynamic scene understanding and spatiotemporal modeling.

### 🤖 AI 总结

**一句话总结**：Dense 3D reconstruction and tracking of dynamic scenes from monocular video remains an important open challenge in computer vision. Progress in this area has been constrained by the scarcity of high-q...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, 3D, Syn4D, Multiview, Synthetic, Dataset, Dense, reconstruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05207v1) | [下载PDF](https://arxiv.org/pdf/2605.05207v1.pdf)

---

## [8. D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models](https://arxiv.org/abs/2605.05204v1)

**作者**：Dengyang Jiang, Xin Jin, Dongyang Liu 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-06

### 📄 论文摘要

The landscape of high-performance image generation models is currently shifting from the inefficient multi-step ones to the efficient few-step counterparts (e.g, Z-Image-Turbo and FLUX.2-klein). However, these models present significant challenges for directly continuous supervised fine-tuning. For example, applying the commonly used fine-tuning technique would compromises their inherent few-step inference capability. To address this, we propose D-OPSD, a novel training paradigm for step-distilled diffusion models that enables on-policy learning during supervised fine-tuning. We first find that the modern diffusion model where the LLM/VLM serves as the encoder can inherit its encoder's in-context capabilities. This enables us to make the training as an on-policy self-distillation process. Specifically, during training, we make the model acts as both the teacher and the student with different contexts, where the student is conditioned only on the text feature, while the teacher is conditioned on the multimodal feature of both the text prompt and the target image. Training minimizes the two predicted distributions over the student's own roll-outs. By optimized on the model's own trajectory and under it's own supervision, D-OPSD enables the model to learn new concept, style, etc. without sacrificing the original few-step capacity.

### 🤖 AI 总结

**一句话总结**：The landscape of high-performance image generation models is currently shifting from the inefficient multi-step ones to the efficient few-step counterparts (e.g, Z-Image-Turbo and FLUX.2-klein). Howev...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, D-OPSD, On-Policy, Self-Distillation, Continuously, Tuning, Step-Distilled, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05204v1) | [下载PDF](https://arxiv.org/pdf/2605.05204v1.pdf)

---

## [9. LoViF 2026 The First Challenge on Holistic Quality Assessment for 4D World Model (PhyScore)](https://arxiv.org/abs/2605.05187v1)

**作者**：Wei Luo, Yiting Lu, Xin Li 等 35 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-06

### 📄 论文摘要

This paper reports on the LoViF 2026 PhyScore challenge, a competition on holistic quality assessment of world-model-generated videos across both 2D and 4D generation settings. The challenge is motivated by a central gap in current evaluation practice: perceptual quality alone is insufficient to judge whether generated dynamics are physically plausible, temporally coherent, and consistent with input conditions. Participants are required to build a metric that jointly predicts four dimensions, i.e., Video Quality, Physical Realism, Condition-Video Alignment, and Temporal Consistency. Depart from that, participants also need to localize physical anomaly timestamps for fine-grained diagnosis.   The benchmark dataset contains 1,554 videos generated by seven representative world generative models, organized into three tracks (text-2D, image-to-4D, and video-to-4D) and spanning 26 categories. These categories explicitly cover physics-relevant scenarios, including dynamics, optics, and thermodynamics, together with diverse real-world and creative content. To ensure label reliability, scores and anomaly timestamps are produced through trained human annotation with an additional automated quality-control pass.   Evaluation is based on both score prediction and anomaly localization, with a composite protocol that combines TimeStamp_IOU and SRCC/PLCC. This report summarizes the challenge design and provides method-level insights from submitted solutions.

### 🤖 AI 总结

**一句话总结**：This paper reports on the LoViF 2026 PhyScore challenge, a competition on holistic quality assessment of world-model-generated videos across both 2D and 4D generation settings. The challenge is motiva...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, LoViF, First, Challenge, Holistic, Quality, Assessment, World

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05187v1) | [下载PDF](https://arxiv.org/pdf/2605.05187v1.pdf)

---

## [10. Geometry-Aware State Space Model: A New Paradigm for Whole-Slide Image Representation](https://arxiv.org/abs/2605.05164v1)

**作者**：Enhui Chai, Sicheng Chen, Tianyi Zhang 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-06

### 📄 论文摘要

Accurate analysis of histopathological images is critical for disease diagnosis and treatment planning. Whole-slide images (WSIs), which digitize tissue specimens at gigapixel resolution, are fundamental to this process but require aggregating thousands of patches for slide-level predictions. Multiple Instance Learning (MIL) tackles this challenge with a two-stage paradigm, decoupling tile-level embedding and slide-level prediction. However, most existing methods implicitly embed patch representations in homogeneous Euclidean spaces, overlooking the hierarchical organization and regional heterogeneity of pathological tissues. This limits current models' ability to capture global tissue architecture and fine-grained cellular morphology. To address this limitation, we introduce a hybrid hyperbolic-Euclidean representation that embeds WSI features in dual geometric spaces, enabling complementary modeling of hierarchical tissue structures and local morphological details. Building on this formulation, we develop BatMIL, a WSI classification framework that leverages both geometric spaces. To model long-range dependencies among thousands of patches, we employ a structured state space sequence model (S4) backbone that encodes patch sequences with linear computational complexity. Furthermore, to account for regional heterogeneity, we introduce a chunk-level mixture-of-experts (MoE) module that groups patches into regions and dynamically routes them to specialized subnetworks, improving representational capacity while reducing redundant computation. Extensive experiments on seven WSI datasets spanning six cancer types demonstrate that BatMIL consistently outperforms state-of-the-art MIL approaches in slide-level classification tasks. These results indicate that geometry-aware representation learning offers a promising direction for next-generation computational pathology.

### 🤖 AI 总结

**一句话总结**：Accurate analysis of histopathological images is critical for disease diagnosis and treatment planning. Whole-slide images (WSIs), which digitize tissue specimens at gigapixel resolution, are fundamen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Geometry-Aware, State, Space, Model, New, Paradigm, Whole-Slide, Image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05164v1) | [下载PDF](https://arxiv.org/pdf/2605.05164v1.pdf)

---

## [11. PhysForge: Generating Physics-Grounded 3D Assets for Interactive Virtual World](https://arxiv.org/abs/2605.05163v1)

**作者**：Yunhan Yang, Chunshi Wang, Junliang Ye 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-06

### 📄 论文摘要

Synthesizing physics-grounded 3D assets is a critical bottleneck for interactive virtual worlds and embodied AI. Existing methods predominantly focus on static geometry, overlooking the functional properties essential for interaction. We propose that interactive asset generation must be rooted in functional logic and hierarchical physics. To bridge this gap, we introduce PhysForge, a decoupled two-stage framework supported by PhysDB, a large-scale dataset of 150,000 assets with four-tier physical annotations. First, a VLM acts as a "physical architect" to plan a "Hierarchical Physical Blueprint" defining material, functional, and kinematic constraints. Second, a physics-grounded diffusion model realizes this blueprint by synthesizing high-fidelity geometry alongside precise kinematic parameters via a novel KineVoxel Injection (KVI) mechanism. Experiments demonstrate that PhysForge produces functionally plausible, simulation-ready assets, providing a robust data engine for interactive 3D content and embodied agents.

### 🤖 AI 总结

**一句话总结**：Synthesizing physics-grounded 3D assets is a critical bottleneck for interactive virtual worlds and embodied AI. Existing methods predominantly focus on static geometry, overlooking the functional pro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, PhysForge, Generating, Physics-Grounded, Assets, Interactive, Virtual, World

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05163v1) | [下载PDF](https://arxiv.org/pdf/2605.05163v1.pdf)

---

## [12. Wasserstein-Aligned Localisation for VLM-Based Distributional OOD Detection in Medical Imaging](https://arxiv.org/abs/2605.05161v1)

**作者**：Bernhard Kainz, Johanna P Mueller, Matthew Baugh 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-06

### 📄 论文摘要

Zero-shot anomaly localisation via vision-language models (VLMs) offers a compelling approach for rare pathology detection, yet its performance is fundamentally limited by the absence of healthy anatomical context. We reformulate zero-shot localisation as a comparative inference problem in which anomalies are identified through structured comparison against reference distributions of normal anatomy. We introduce WALDO, a training-free framework grounded in optimal transport theory that enables comparative reasoning through: (i) entropy-weighted Sliced Wasserstein distances for anatomically-aware reference selection from DINOv2 patch distributions, (ii) Goldilocks zone sampling exploiting the non-monotonic relationship between reference similarity and localisation accuracy, and (iii) self-consistency aggregation via weighted non-maximum suppression. We theoretically analyse the Goldilocks effect through distributional divergence, and show that references with moderate similarity minimize a bias-variance trade-off in comparative visual reasoning. On the NOVA brain MRI benchmark, WALDO with Qwen2.5-VL-72B achieves $43.5_{\pm1.6}\%$ mAP@30 (95\% CI: [40.4, 46.7]), representing a 19\% relative improvement over zero-shot baselines. Cross-model evaluation shows consistent gains: GPT-4o achieves $32.0_{\pm6.5}\%$ and Qwen3-VL-32B achieves $32.0_{\pm6.6}\%$ mAP@30. Paired McNemar tests confirm statistical significance ($p<0.01$). Source code is available at https://github.com/bkainz/WALDO_MICCAI26_demo .

### 🤖 AI 总结

**一句话总结**：Zero-shot anomaly localisation via vision-language models (VLMs) offers a compelling approach for rare pathology detection, yet its performance is fundamentally limited by the absence of healthy anato...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Wasserstein-Aligned, Localisation, VLM-Based, Distributional, OOD, Detection, Medical, Imaging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05161v1) | [下载PDF](https://arxiv.org/pdf/2605.05161v1.pdf)

---

## [13. Aes3D: Aesthetic Assessment in 3D Gaussian Splatting](https://arxiv.org/abs/2605.05155v1)

**作者**：Chuanzhi Xu, Boyu Wei, Haoxian Zhou 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-06

### 📄 论文摘要

As 3D Gaussian Splatting (3DGS) gains attention in immersive media and digital content creation, assessing the aesthetics of 3D scenes becomes important in helping creators build more visually compelling 3D content. However, existing evaluation methods for 3D scenes primarily emphasize reconstruction fidelity and perceptual realism, largely overlooking higher-level aesthetic attributes such as composition, harmony, and visual appeal. This limitation comes from two key challenges: (1) the absence of general 3DGS datasets with aesthetic annotations, and (2) the intrinsic nature of 3DGS as a low-level primitive representation, which makes it difficult to capture high-level aesthetic features. To address these challenges, we propose Aes3D, the first systematic framework for assessing the aesthetics of 3D neural rendering scenes. Aes3D includes Aesthetic3D, the first dataset dedicated to 3D scene aesthetic assessment, built on our proposed annotation strategy for 3D scene aesthetics. In addition, we present Aes3DGSNet, a lightweight model that directly predicts scene-level aesthetic scores from 3DGS representations. Notably, our model operates solely on 3D Gaussian primitives, eliminating the need for rendering multi-view images and thus reducing computational cost and hardware requirements. Through aesthetics-supervised learning on multi-view 3DGS scene representations, Aes3DGSNet effectively captures high-level aesthetic cues and accurately regresses aesthetic scores. Experimental results demonstrate that our approach achieves strong performance while maintaining a lightweight design, establishing a new benchmark for 3D scene aesthetic assessment. Code and datasets will be made available in a future version.

### 🤖 AI 总结

**一句话总结**：As 3D Gaussian Splatting (3DGS) gains attention in immersive media and digital content creation, assessing the aesthetics of 3D scenes becomes important in helping creators build more visually compell...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, As, Aes3D, Aesthetic, Assessment, Gaussian, Splatting, 3DGS

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05155v1) | [下载PDF](https://arxiv.org/pdf/2605.05155v1.pdf)

---

## [14. What Matters in Practical Learned Image Compression](https://arxiv.org/abs/2605.05148v1)

**作者**：Kedar Tatwawadi, Parisa Rahimzadeh, Zhanghao Sun 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-05-06

### 📄 论文摘要

One of the major differentiators unlocked by learned codecs relative to their hard-coded traditional counterparts is their ability to be optimized directly to appeal to the human visual system. Despite this potential, a perceptual yet practical image codec is yet to be proposed.   In this work, we aim to close this gap. We conduct a comprehensive study of the key modeling choices that govern the design of a practical learned image codec, jointly optimized for perceptual quality and runtime -- including within the ablations several novel techniques. We then perform performance-aware neural architecture search over millions of backbone configurations to identify models that achieve the target on-device runtime while maximizing compression performance as captured by perceptual metrics.   We combine the various optimizations to construct a new codec that achieves a significantly improved tradeoff between speed and perceptual quality. Based on rigorous subjective user studies, it provides 2.3-3x bitrate savings against AV1, AV2, VVC, ECM and JPEG-AI, and 20-40% bitrate savings against the best learned codec alternatives. At the same time, on an iPhone 17 Pro Max, it encodes 12MP images as fast as 230ms, and decodes them in 150ms -- faster than most top ML-based codecs run on a V100 GPU.

### 🤖 AI 总结

**一句话总结**：One of the major differentiators unlocked by learned codecs relative to their hard-coded traditional counterparts is their ability to be optimized directly to appeal to the human visual system. Despit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, What, Matters, Practical, Learned, Image, Compression, One

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05148v1) | [下载PDF](https://arxiv.org/pdf/2605.05148v1.pdf)

---

## [15. CPCANet: Deep Unfolding Common Principal Component Analysis for Domain Generalization](https://arxiv.org/abs/2605.05136v1)

**作者**：Yu-Hsi Chen, Abd-Krim Seghouane  
**分类**：cs.CV  
**发布时间**：2026-05-06

### 📄 论文摘要

Domain Generalization (DG) aims to learn representations that remain robust under out-of-distribution (OOD) shifts and generalize effectively to unseen target domains. While recent invariant learning strategies and architectural advances have achieved strong performance, explicitly discovering a structured domain-invariant subspace through second-order statistics remains underexplored. In this work, we propose CPCANet, a novel framework grounded in Common Principal Component Analysis (CPCA), which unrolls the iterative Flury-Gautschi (FG) algorithm into fully differentiable neural layers. This approach integrates the statistical properties of CPCA into an end-to-end trainable framework, enforcing the discovery of a shared subspace across diverse domains while preserving interpretability. Experiments on four standard DG benchmarks demonstrate that CPCANet achieves state-of-the-art (SOTA) performance in zero-shot transfer. Moreover, CPCANet is architecture-agnostic and requires no dataset-specific tuning, providing a simple and efficient approach to learning robust representations under distribution shift. Code is available at https://github.com/wish44165/CPCANet.

### 🤖 AI 总结

**一句话总结**：Domain Generalization (DG) aims to learn representations that remain robust under out-of-distribution (OOD) shifts and generalize effectively to unseen target domains. While recent invariant learning ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CPCANet, Deep, Unfolding, Common, Principal, Component, Analysis, Domain

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05136v1) | [下载PDF](https://arxiv.org/pdf/2605.05136v1.pdf)

---

## cs.LG

## [16. Estimating the expected output of wide random MLPs more efficiently than sampling](https://arxiv.org/abs/2605.05179v1)

**作者**：Wilson Wu, Victor Lecomte, Michael Winer 等 6 位作者  
**分类**：cs.LG, cond-mat.dis-nn, stat.ML  
**发布时间**：2026-05-06

### 📄 论文摘要

By far the most common way to estimate an expected loss in machine learning is to draw samples, compute the loss on each one, and take the empirical average. However, sampling is not necessarily optimal. Given an MLP at initialization, we show how to estimate its expected output over Gaussian inputs without running samples through the network at all. Instead, we produce approximate representations of the distributions of activations at each layer, leveraging tools such as cumulants and Hermite expansions. We show both theoretically and empirically that for sufficiently wide networks, our estimator achieves a target mean squared error using substantially fewer FLOPs than Monte Carlo sampling. We find moreover that our methods perform particularly well at estimating the probabilities of rare events, and additionally demonstrate how they can be used for model training. Together, these findings suggest a path to producing models with a greatly reduced probability of catastrophic tail risks.

### 🤖 AI 总结

**一句话总结**：By far the most common way to estimate an expected loss in machine learning is to draw samples, compute the loss on each one, and take the empirical average. However, sampling is not necessarily optim...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Estimating, expected, output, wide, random, MLPs, more

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05179v1) | [下载PDF](https://arxiv.org/pdf/2605.05179v1.pdf)

---

## [17. Understanding In-Context Learning for Nonlinear Regression with Transformers: Attention as Featurizer](https://arxiv.org/abs/2605.05176v1)

**作者**：Alexander Hsu, Zhaiming Shen, Wenjing Liao 等 4 位作者  
**分类**：cs.LG, math.NA  
**发布时间**：2026-05-06

### 📄 论文摘要

Pre-trained transformers are able to learn from examples provided as part of the prompt without any weight updates, a remarkable ability known as in-context learning (ICL). Despite its demonstrated efficacy across various domains, the theoretical understanding of ICL is still developing. Whereas most existing theory has focused on linear models, we study ICL in the nonlinear regression setting. Through the interaction mechanism in attention, we explicitly construct transformer networks to realize nonlinear features, such as polynomial or spline bases, which span a wide class of functions. Based on this construction, we establish a framework to analyze end-to-end in-context nonlinear regression with the constructed features. Our theory provides finite-sample generalization error bounds in terms of context length and training set size. We numerically validate the theory on synthetic regression tasks.

### 🤖 AI 总结

**一句话总结**：Pre-trained transformers are able to learn from examples provided as part of the prompt without any weight updates, a remarkable ability known as in-context learning (ICL). Despite its demonstrated ef...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Understanding, In-Context, Learning, Nonlinear, Regression, Transformers, Attention

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05176v1) | [下载PDF](https://arxiv.org/pdf/2605.05176v1.pdf)

---

## [18. Superposition Is Not Necessary: A Mechanistic Interpretability Analysis of Transformer Representations for Time Series Forecasting](https://arxiv.org/abs/2605.05151v1)

**作者**：Alper Yıldırım  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-06

### 📄 论文摘要

Transformer architectures have been widely adopted for time series forecasting, yet whether the representational mechanisms that make them powerful in NLP actually engage on time series data remains unexplored. The persistent competitiveness of simple linear models such as DLinear has fueled ongoing debate, but no mechanistic explanation for this phenomenon has been offered. We address this gap by applying sparse autoencoders (SAEs), a tool from mechanistic interpretability, to probe the internal representations of PatchTST. We first establish that a single-layer, narrow-dimensional transformer matches the forecasting performance of deeper configurations across commonly used benchmarks. We then train SAEs on the post-GELU intermediate FFN activations with dictionary sizes ranging from 0.5x to 4.0x the native dimensionality. Expanding the dictionary yields negligible downstream performance change (average 0.214%), with large portions of overcomplete dictionaries remaining inactive. Targeted causal interventions on dominant latent features produce minimal forecast perturbation. Across all evaluated settings, we observe no empirical evidence that the analyzed FFN representations rely on strong superposition. Instead, the representations remain sparse, stable under aggressive dictionary expansion, and largely insensitive to latent interventions. These results demonstrate that superposition is not necessary for competitive performance on standard forecasting benchmarks, suggesting they may not demand the rich compositional representations that drive transformer success in language modeling, and helping explain the persistent competitiveness of simple linear models

### 🤖 AI 总结

**一句话总结**：Transformer architectures have been widely adopted for time series forecasting, yet whether the representational mechanisms that make them powerful in NLP actually engage on time series data remains u...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Superposition, Not, Necessary, Mechanistic, Interpretability, Analysis, Transformer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05151v1) | [下载PDF](https://arxiv.org/pdf/2605.05151v1.pdf)

---

## [19. Human-AI Co-Mentorship in Project-Based Learning: A Case Study in Financial Forecasting](https://arxiv.org/abs/2605.05144v1)

**作者**：Freyaa Chawla, Ahan Chawla, Rishi Singh 等 5 位作者  
**分类**：cs.LG, cs.CY  
**发布时间**：2026-05-06

### 📄 论文摘要

This paper reflects on a AI research project carried out by a team of high-school and early-undergraduate students under the mentorship of graduate researchers and ably assisted by AI tools. We share our experience in not only on the learning experience for the high school students, but also on how AI tools accelerated the process that enabled the high school students to focus on higher order problem formulation and solution. Although the participants entered the project with limited background in both AI and finance, they showed strong enthusiasm for technical market analysis and ETF price prediction. Traditional learning settings would first teach the necessary methods in a classroom setting and only later let students apply them. In contrast, our project emphasized workflow design: students identified the sequence of steps needed to address the problem and then used AI-driven tools to execute each step.   We note that the high school students developed the necessary code through iterating with the AI tools, and we used our daily stand-ups to debug and answer conceptual questions. Each of the student was able to dig deeper into their area of interest whether computer science or finance, while collaboratively making a significant advance over the summer of 2025. This project was an important pedagogical exercise on how AI tools can be used for mentoring high school students, allowing them to focus on their specific interests and using the daily stand-ups to focus on problem definition and conceptual understanding. Despite their limited technical qualifications, the students were able to leverage AI tools to build meaningful models with real-world application.

### 🤖 AI 总结

**一句话总结**：This paper reflects on a AI research project carried out by a team of high-school and early-undergraduate students under the mentorship of graduate researchers and ably assisted by AI tools. We share ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Human-AI, Co-Mentorship, Project-Based, Learning, Case, Study, Financial, Forecasting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05144v1) | [下载PDF](https://arxiv.org/pdf/2605.05144v1.pdf)

---

## [20. Low-Cost Black-Box Detection of LLM Hallucinations via Dynamical System Prediction](https://arxiv.org/abs/2605.05134v1)

**作者**：Dan Wilson, Mohamed Akrout  
**分类**：cs.LG, math.DS  
**发布时间**：2026-05-06

### 📄 论文摘要

Large Language Models (LLMs) frequently generate plausible but non-factual content, a phenomenon known as hallucination. While existing detection methods typically rely on computationally expensive sampling-based consistency checks or external knowledge retrieval, we propose a new method that treats the LLM as a black-box dynamical system. By projecting LLM responses into a high-dimensional manifold via an embedding model, we characterize the resulting vector sequences as observable realizations of the model's latent state-space dynamics. Leveraging Koopman operator theory, we fit the transition operators for both factual and hallucinated regimes and define a differential residual score based on their respective prediction errors. To accommodate varying user requirements and domain-specific sensitivities, we introduce a preference-aware calibration mechanism that optimizes the classification threshold based on a small set of demonstrations. This approach enables low-cost hallucination detection in a single-sample pass, avoiding the need for secondary sampling or external grounding. Extensive testing across three data benchmarks demonstrates that our method achieves state-of-the-art performance with reduced resource overhead.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) frequently generate plausible but non-factual content, a phenomenon known as hallucination. While existing detection methods typically rely on computationally expensive sa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Low-Cost, Black-Box, Detection, Hallucinations, via, Dynamical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05134v1) | [下载PDF](https://arxiv.org/pdf/2605.05134v1.pdf)

---

## [21. Transformed Latent Variable Multi-Output Gaussian Processes](https://arxiv.org/abs/2605.05133v1)

**作者**：Xiaoyu Jiang, Xinxing Shi, Sokratia Georgaka 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-06

### 📄 论文摘要

Multi-Output Gaussian Processes (MOGPs) provide a principled probabilistic framework for modelling correlated outputs but face scalability bottlenecks when applied to datasets with high-dimensional output spaces. To maintain tractability, existing methods typically resort to restrictive assumptions, such as employing low-rank or sum-of-separable kernels, which can limit expressiveness. We propose the Transformed Latent Variable MOGP (T-LVMOGP), a novel framework that scales MOGPs to a massive number of outputs while preserving the capacity to capture meaningful inter-output dependencies. T-LVMOGP constructs a flexible multi-output deep kernel by mapping inputs and output-specific latent variables into an embedding space using a Lipschitz-regularised neural network. Combined with stochastic variational inference, our model effectively scales to high-dimensional output settings. Across diverse benchmarks, including climate modelling with over 10,000 outputs and zero-inflated spatial transcriptomics data, T-LVMOGP outperforms baselines in both predictive accuracy and computational efficiency.

### 🤖 AI 总结

**一句话总结**：Multi-Output Gaussian Processes (MOGPs) provide a principled probabilistic framework for modelling correlated outputs but face scalability bottlenecks when applied to datasets with high-dimensional ou...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Transformed, Latent, Variable, Multi-Output, Gaussian, Processes, MOGPs, provide

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05133v1) | [下载PDF](https://arxiv.org/pdf/2605.05133v1.pdf)

---

## [22. Adaptive Policy Selection and Fine-Tuning under Interaction Budgets for Offline-to-Online Reinforcement Learning](https://arxiv.org/abs/2605.05123v1)

**作者**：Alper Kamil Bozkurt, Xiaoan Xu, Shangtong Zhang 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-06

### 📄 论文摘要

In offline-to-online reinforcement learning (O2O-RL), policies are first safely trained offline using previously collected datasets and then further fine-tuned for tasks via limited online interactions. In a typical O2O-RL pipeline, candidate policies trained with offline RL are evaluated via either off-policy evaluation (OPE) or online evaluation (OE). The policy with the highest estimated value is then deployed and continually fine-tuned. However, this setup has two main issues. First, OPE can be unreliable, making it risky to deploy a policy based solely on those estimates, whereas OE may identify a viable policy with substantial online interaction, which could have been used for fine-tuning. Second--and more importantly--it is also often not possible to determine a priori whether a pretrained policy will improve with post-deployment fine-tuning, especially in non-stationary environments. As a result, procedures committing to a single deployed policy are impractical in many real-world settings. Moreover, a naive remedy that exhaustively fine-tunes all candidates would violate interaction budget constraints and is likewise infeasible. In this paper, we propose a novel adaptive approach for policy selection and fine-tuning under online interaction budgets in O2O-RL. Following the standard pipeline, we first train a set of candidate policies with different offline RL algorithms and hyperparameters; we then perform OPE to obtain initial performance estimates. We next adaptively select and fine-tune the policies based on their predicted performance via an upper-confidence-bound approach thereby making efficient use of online interactions. We demonstrate that our approach improves upon O2O-RL baselines with various benchmarks.

### 🤖 AI 总结

**一句话总结**：In offline-to-online reinforcement learning (O2O-RL), policies are first safely trained offline using previously collected datasets and then further fine-tuned for tasks via limited online interaction...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Adaptive, Policy, Selection, Fine-Tuning, under, Interaction, Budgets, Offline-to-Online

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05123v1) | [下载PDF](https://arxiv.org/pdf/2605.05123v1.pdf)

---

## [23. Conditional outlier detection for clinical alerting](https://arxiv.org/abs/2605.05124v1)

**作者**：Milos Hauskrecht, Michal Valko, Shyam Visweswaran 等 6 位作者  
**分类**：cs.LG, cs.CY  
**发布时间**：2026-05-06

### 📄 论文摘要

We develop and evaluate a data-driven approach for detecting unusual (anomalous) patient-management actions using past patient cases stored in an electronic health record (EHR) system. Our hypothesis is that patient-management actions that are unusual with respect to past patients may be due to a potential error and that it is worthwhile to raise an alert if such a condition is encountered. We evaluate this hypothesis using data obtained from the electronic health records of 4,486 post-cardiac surgical patients. We base the evaluation on the opinions of a panel of experts. The results support that anomaly-based alerting can have reasonably low false alert rates and that stronger anomalies are correlated with higher alert rates.

### 🤖 AI 总结

**一句话总结**：We develop and evaluate a data-driven approach for detecting unusual (anomalous) patient-management actions using past patient cases stored in an electronic health record (EHR) system. Our hypothesis ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Conditional, outlier, detection, clinical, alerting, develop, evaluate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05124v1) | [下载PDF](https://arxiv.org/pdf/2605.05124v1.pdf)

---

## [24. On the Wasserstein Gradient Flow Interpretation of Drifting Models](https://arxiv.org/abs/2605.05118v1)

**作者**：Arthur Gretton, Li Kevin Wenliang, Alexandre Galashov 等 6 位作者  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-05-06

### 📄 论文摘要

Recently, Deng et al. (2026) proposed Generative Modeling via Drifting (GMD), a novel framework for generative tasks. This note presents an analysis of GMD through the lens of Wasserstein Gradient Flows (WGF), i.e., the path of steepest descent for a functional in the space of probability measures, equipped with the geometry of optimal transport. Unlike previous WGF-based contributions, GMD can be thought of as directly targeting a fixed point of a specific WGF flow. We demonstrate three main results: first, that one algorithm proposed by Deng et al. (2026) corresponds to finding the limiting point of a WGF on the KL divergence, with Parzen smoothing on the densities. Second, that the algorithm actually implemented by Deng et al. (2026) corresponds to a different procedure, which bears some resemblance to the fixed point of a WGF on the Sinkhorn divergence, but lacks certain desirable properties of the latter. Third, the same same idea can be extended to the limiting point of other WGFs, including the Maximum Mean Discrepancy (MMD), the sliced Wasserstein distance, and GAN critic functions.

### 🤖 AI 总结

**一句话总结**：Recently, Deng et al. (2026) proposed Generative Modeling via Drifting (GMD), a novel framework for generative tasks. This note presents an analysis of GMD through the lens of Wasserstein Gradient Flo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Wasserstein, Gradient, Flow, Interpretation, Drifting, Models, Recently

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05118v1) | [下载PDF](https://arxiv.org/pdf/2605.05118v1.pdf)

---

## [25. Manifold Steering Reveals the Shared Geometry of Neural Network Representation and Behavior](https://arxiv.org/abs/2605.05115v1)

**作者**：Daniel Wurgaft, Can Rager, Matthew Kowal 等 16 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-06

### 📄 论文摘要

Neural representations carry rich geometric structure; but does that structure causally shape behavior? To address this question, we intervene along paths through activation space defined by different geometries, and measure the behavioral trajectories they induce. In particular, we test whether interventions that respect the geometry of activation space will yield behaviors close to those the model exhibits naturally. Concretely, we first fit an activation manifold $M_h$ to representations and a behavior manifold $M_y$ to output probability distributions. We then test the link $M_h \leftrightarrow M_y$ via interventions: we find that steering along $M_h$, which we term manifold steering, yields behavioral trajectories that follow $M_y$, while linear steering -- which assumes a Euclidean geometry -- cuts through off-manifold regions and hence produces unnatural outputs. Moreover, optimizing interventions in activation space to produce paths along $M_y$ recovers activation trajectories that trace the curvature of $M_h$. We demonstrate this bidirectional relationship between the geometry of representation and behavior across tasks and modalities. In language models, we use reasoning tasks with cyclic and sequential geometries as well as in-context learning tasks with more complex graph geometries. In a video world model, we use a task with geometry corresponding to physical dynamics. Overall, our work shows that geometry in neural representation is not merely incidental, but is in fact the proper object for enabling principled control via intervention on internals. This recasts the core problem of steering from finding the right direction to finding the right geometry.

### 🤖 AI 总结

**一句话总结**：Neural representations carry rich geometric structure; but does that structure causally shape behavior? To address this question, we intervene along paths through activation space defined by different...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Manifold, Steering, Reveals, Shared, Geometry, Neural, Network

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05115v1) | [下载PDF](https://arxiv.org/pdf/2605.05115v1.pdf)

---

## [26. How Long Does Infinite Width Last? Signal Propagation in Long-Range Linear Recurrences](https://arxiv.org/abs/2605.05113v1)

**作者**：Mariia Seleznova  
**分类**：cs.LG  
**发布时间**：2026-05-06

### 📄 论文摘要

We study signal propagation in linear recurrent models at finite width. While existing signal propagation theory relies predominantly on the infinite-width limit, it remains unclear for how long that approximation remains accurate when recurrent depth $t$ grows jointly with width $n$. This question is especially relevant for modern recurrent sequence models, whose natural operating regime involves long input sequences, i.e., large $t$. We derive exact finite-width formulas for the hidden state signal energies in linear recurrences under complex Gaussian initialization. Using these formulas, we identify the joint depth-width scaling regimes that govern signal propagation: (i) a subcritical regime $t=o(\sqrt n)$, in which the infinite-width approximation remains valid; (ii) a critical regime $t\sim c\sqrt n$, in which non-negligible deviations from infinite-width predictions appear and a nontrivial joint scaling limit emerges; and (iii) a supercritical regime $t\gg \sqrt n$, in which finite-width effects dominate. Thus, our results pinpoint the precise recurrent depth scale at which infinite-width theory breaks down in long-range linear recurrences. In turn, this shows when standard initialization schemes, such as Glorot, become unstable. More broadly, our results demonstrate that finite-width effects accumulate more rapidly with depth in recurrent models than in feedforward ones, leading to qualitatively different signal propagation behavior.

### 🤖 AI 总结

**一句话总结**：We study signal propagation in linear recurrent models at finite width. While existing signal propagation theory relies predominantly on the infinite-width limit, it remains unclear for how long that ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：How, Long, Does, Infinite, Width, Last?, Signal, Propagation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05113v1) | [下载PDF](https://arxiv.org/pdf/2605.05113v1.pdf)

---

## [27. Unified Framework of Distributional Regret in Multi-Armed Bandits and Reinforcement Learning](https://arxiv.org/abs/2605.05102v1)

**作者**：Harin Lee, Min-hwan Oh  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-05-06

### 📄 论文摘要

We study the distribution of regret in stochastic multi-armed bandits and episodic reinforcement learning through a unified framework. We formalize a distributional regret bound as a probabilistic guarantee that holds uniformly over all confidence levels $δ\in (0,1]$, thereby characterizing the regret distribution across the full range of $δ$. We present a simple UCBVI-style algorithm with exploration bonus $\min\{c_{1,k}/N, c_{2,k}/\sqrt{N}\}$, where $N$ denotes the visit count and $(c_{1,k},c_{2,k})$ are user-specified parameters. For arbitrary parameter sequences, we derive general gap-independent and gap-dependent distributional regret bounds, yielding a principled characterization of how the parameters control the trade-off between expected performance, tail risk, and instance-dependent behavior. In particular, our bounds achieve optimal trade-offs between expected and distributional regret in both minimax and instance-dependent regimes. As a special case, for multi-armed bandits with $A$ arms and horizon $T$, we obtain a distributional regret bound of order $\mathcal{O}(\sqrt{AT}\log(1/δ))$, confirming the conjecture of Lattimore & Szepesvári (2020, Section 17.1) for the first time.

### 🤖 AI 总结

**一句话总结**：We study the distribution of regret in stochastic multi-armed bandits and episodic reinforcement learning through a unified framework. We formalize a distributional regret bound as a probabilistic gua...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Unified, Framework, Distributional, Regret, Multi-Armed, Bandits, Reinforcement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05102v1) | [下载PDF](https://arxiv.org/pdf/2605.05102v1.pdf)

---

## [28. Gated Multimodal Learning for Interpretable Property Energy Performance Prediction and Retrofit Scenario Analysis](https://arxiv.org/abs/2605.05088v1)

**作者**：Yunfei Bai, Aaron Tesfa Tsion, Raul Rosales 等 5 位作者  
**分类**：cs.LG, physics.soc-ph  
**发布时间**：2026-05-06

### 📄 论文摘要

Achieving resilient and sustainable cities requires scalable approaches to decarbonising residential buildings, which account for about 20% of UK greenhouse gas emissions and 25% of energy-related emissions in the European Union. Energy Performance Certificates (EPCs) support regulation and retrofit planning, but their reliance on on-site inspections limits timely city-scale assessment. This study introduces a gated multimodal model to predict Standard Assessment Procedure (SAP) energy efficiency and Environmental Impact (EI) scores by integrating EPC tabular variables, assessor-written free text, and Geographic Information System (GIS)-derived spatial features describing footprint geometry, height, area, and orientation. Sample-wise gating learns property-specific modality weights, while an auxiliary band classification head stabilises training. In a Westminster, London case study, the model predicts SAP and EI scores with MAEs of 4.03 and 4.76 points and R2 values of 0.757 and 0.748, respectively, achieving a mean MAE of 4.39. Ablation results show that full multimodal fusion outperforms unimodal and bimodal baselines for both score prediction and band-level classification. Interpretability analyses provide decision-relevant evidence: gating weights indicate strong reliance on assessor text; SHAP highlights main fuel, built form, and construction age band; text occlusion prioritises roof and wall fields; and spatial attribution is dominated by height and footprint area, with sensitivity to footprint shape. The validated framework is further applied to retrofit scenarios for wall insulation, roof insulation, and window glazing upgrades, indicating projected improvements in SAP, EI, annual energy cost, and equivalent CO2 emissions. Overall, the framework provides scalable property-level evidence for retrofit screening, intervention prioritisation, and net-zero housing transitions.

### 🤖 AI 总结

**一句话总结**：Achieving resilient and sustainable cities requires scalable approaches to decarbonising residential buildings, which account for about 20% of UK greenhouse gas emissions and 25% of energy-related emi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Gated, Multimodal, Learning, Interpretable, Property, Energy, Performance, Prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05088v1) | [下载PDF](https://arxiv.org/pdf/2605.05088v1.pdf)

---

## [29. Order Matters: Improving Domain Adaptation by Reordering Data](https://arxiv.org/abs/2605.05084v1)

**作者**：Andrea Napoli, Paul White  
**分类**：cs.LG  
**发布时间**：2026-05-06

### 📄 论文摘要

Domain shift remains a key challenge in deploying machine learning models to the real world. Unsupervised domain adaptation (UDA) aims to address this by minimising domain discrepancy during training, but the discrepancy estimates suffer from high variance in stochastic settings, which can stifle the theoretical benefits of the method. This paper proposes Optimal Reordering of Data for Error-Reduced Estimation of Discrepancy (ORDERED), a novel unbiased stochastic variance reduction technique which reduces the discrepancy estimation error by optimising the order in which the training data are sampled. We consider two specific domain discrepancy losses (correlation alignment and the maximum mean discrepancy), formulate their stochastic estimation error as a function of the data sampling order, and propose a practical optimisation algorithm. Our simulations demonstrate reduced variance compared to related methods, and experiments on two domain shift image classification benchmarks show improved target domain accuracy.

### 🤖 AI 总结

**一句话总结**：Domain shift remains a key challenge in deploying machine learning models to the real world. Unsupervised domain adaptation (UDA) aims to address this by minimising domain discrepancy during training,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Order, Matters, Improving, Domain, Adaptation, Reordering, Data, shift

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05084v1) | [下载PDF](https://arxiv.org/pdf/2605.05084v1.pdf)

---

## [30. Provable imitation learning for control of instability in partially-observed Vlasov--Poisson equations](https://arxiv.org/abs/2605.05081v1)

**作者**：Xiaofan Xia, Qin Li, Wenlong Mou  
**分类**：cs.LG, math.AP, math.OC, physics.plasm-ph  
**发布时间**：2026-05-06

### 📄 论文摘要

We consider the stabilization of Vlasov--Poisson plasma dynamics, a central control problem in nuclear fusion. Our focus is the gap between what an ideal controller would use and what experiments can actually observe: while optimal policy may rely on the full phase-space state, practical feedback is typically limited to sparse macroscopic diagnostics. We therefore study imitation learning methods that distill a fully observed expert policy into controllers operating only on macroscopic measurements. We show the stability guarantees of the learned policy, where the error floor depends on the minimal behavior cloning loss achievable under the observation constraints. We further characterize this minimal loss in terms of a notion of entropy that quantifies the complexity of the initial distribution. Our results demonstrates the theoretical feasibility of learning stabilizing feedback policies for kinetic plasma dynamics from macroscopic observations, and exhibits the adaptivity of the learning approach to low-complexity structures. Through extensive numerical experiments, we validate our theory and show that the learned policies can stabilize the system using only macroscopic observations, within a significantly longer time horizon than non-adaptive baseline controllers.

### 🤖 AI 总结

**一句话总结**：We consider the stabilization of Vlasov--Poisson plasma dynamics, a central control problem in nuclear fusion. Our focus is the gap between what an ideal controller would use and what experiments can ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Provable, imitation, learning, control, instability, partially-observed, Vlasov--Poisson

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.05081v1) | [下载PDF](https://arxiv.org/pdf/2605.05081v1.pdf)

---

