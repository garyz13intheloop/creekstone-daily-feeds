# arXiv AI 论文日报 | 2026-07-09

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (5 篇)
- [cs.LG](#csLG) (14 篇)
- [cs.AI](#csAI) (3 篇)
- [cs.CV](#csCV) (8 篇)

---

## cs.AI

## [1. SkillCenter: A Large-Scale Source-Grounded Skill Library for Autonomous AI Agents](https://arxiv.org/abs/2607.07676v1)

**作者**：Tianming Sha, Yue Zhao, Lichao Sun 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-08

### 📄 论文摘要

Autonomous AI agents can execute complex tasks with limited human review, yet they often lack the grounded operational knowledge to make their outputs not just executable but correct, secure, and maintainable. We introduce SkillCenter, to our knowledge the largest open skill library for agents by total count: 216,938 structured skills across 24 domain bundles. A SkillGate-filtered pipeline contributes 114,565 source-grounded skills from peer-reviewed journals, ArXiv, and over 24,000 technical sources, integrated with 102,373 community skills from GitHub and the ClawHub marketplace. We present the end-to-end framework that builds the pipeline subset: multi-source acquisition, an LLM-based quality gate (SkillGate), template-driven generation, iterative source-grounding, and quality-controlled publishing. Source grounding is a traceability guarantee: each retained claim maps to an exact quotation in its source. All skills ship as offline-searchable SQLite FTS5 bundles.

### 🤖 AI 总结

**一句话总结**：Autonomous AI agents can execute complex tasks with limited human review, yet they often lack the grounded operational knowledge to make their outputs not just executable but correct, secure, and main...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SkillCenter, Large-Scale, Source-Grounded, Skill, Library, Autonomous, can

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07676v1) | [下载PDF](https://arxiv.org/pdf/2607.07676v1.pdf)

---

## [2. Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663v1)

**作者**：Mingguang Chen, Licheng Wang, Bo Qu  
**分类**：cs.AI  
**发布时间**：2026-07-08

### 📄 论文摘要

AI systems increasingly participate in their own improvement: revising their outputs, adapting their own harnesses during deployment, training on data they generate, and, increasingly, conducting AI research itself. This literature is described under a vocabulary ("self-refine," "self-reward," "self-play," "self-evolve") that conflates fundamentally different ambitions. We survey 1,250 arXiv papers (2024-2026) along two axes: what the system improves -- its behavior in deployment, its policy through training, its evaluator, or the research process itself -- and the degree of loop closure (human-in-the-loop to fully closed). The taxonomy separates bounded self-refinement -- convergent, evaluable, and already industrial practice -- from open-ended recursive self-improvement (RSI), which remains bounded by grounding requirements, collapse dynamics, and compute constraints on every measured axis. Its distinctive feature is a dedicated category for self-evaluation: every improvement loop is a claim that some signal can substitute for human judgment. We survey the evaluator design space -- judges, process reward models, verifiers, rubrics, meta-evaluation -- order the signals into a verification hierarchy from formal verifiers (strongest) to intrinsic self-assessment (weakest), and observe that demonstrated self-improvement strength tracks this hierarchy, that its failure modes (self-confirming loops, model collapse, diversity collapse) follow from its violations, and that the "research direction-setting" bottleneck keeping humans in the loop sits at the top of that hierarchy. We connect the technical literature to the theory of RSI limits and to the safety and governance questions raised by frontier-lab accounts of closing the loop, and identify governance-grade measurement of self-improvement as the field's most underpopulated niche.

### 🤖 AI 总结

**一句话总结**：AI systems increasingly participate in their own improvement: revising their outputs, adapting their own harnesses during deployment, training on data they generate, and, increasingly, conducting AI r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Recursive, Self-Improvement, Bounded, Self-Refinement, Autonomous, Research, Loops, systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07663v1) | [下载PDF](https://arxiv.org/pdf/2607.07663v1.pdf)

---

## [3. RL Post-Training Builds Compositional Reasoning Strategies](https://arxiv.org/abs/2607.07646v1)

**作者**：Azwar Abdulsalam, Nishil Patel, Andrew Saxe  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-07-08

### 📄 论文摘要

Does RL post-training merely amplify primitive skills already latent in a base model, or can it compose primitive skills into new higher-level strategies? We study this question in a fully observable rewrite-grammar environment where the pretraining distribution is known and every generated rewrite can be audited. A Transformer is pretrained on primitive symbol-rewrite chains and post-trained on a Trace-based reasoning task with only a binary final-answer reward. RL solves held-out problems that remain rarely solved by the pretrained model even under much larger sampling budgets, while rejection fine-tuning improves early but plateaus. Trace analysis shows that RL reorganizes primitive competence through a phased compositional mechanism: it first strengthens primitive reductions, then discovers valid composed procedures. These include sequential compositions, which collapse ordered chains of primitive contractions, and parallel compositions, which combine independent primitive contractions in a single step. The composed procedures are not isolated samples; they are reused and consolidated into a stable repertoire. Comparing RL with rejection fine-tuning shows that the key difference is not exploration volume but selectivity: RFT produces many shortcut-like rewrites, much of them invalid, whereas RL concentrates exploration into valid reusable structure. Pretraining ablations show that the emergence of compositional strategies is gated not by primitive exposure alone, but by whether pretraining organizes primitive competence into reduction procedures that RL can later compress. The base model provides weak procedural ingredients; RL builds them into reliable higher-level strategies.

### 🤖 AI 总结

**一句话总结**：Does RL post-training merely amplify primitive skills already latent in a base model, or can it compose primitive skills into new higher-level strategies? We study this question in a fully observable ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Post-Training, Builds, Compositional, Reasoning, Strategies, Does, merely

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07646v1) | [下载PDF](https://arxiv.org/pdf/2607.07646v1.pdf)

---

## cs.CL

## [4. Co-LMLM: Continuous-Query Limited Memory Language Models](https://arxiv.org/abs/2607.07707v1)

**作者**：Yair Feldman, Linxi Zhao, Nathan Godey 等 8 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-07-08

### 📄 论文摘要

Limited memory language models (LMLMs) externalize factual knowledge during pretraining to a knowledge base (KB), rather than memorizing it in their weights. During generation, the model then fetches knowledge from the KB as needed. This recently introduced paradigm provides multiple advantages, including knowledge control capabilities that remain beyond conventional LLMs. We propose continuous-query LMLM (CO-LMLM), where the KB pairs continuous keys with textual knowledge values, a significant departure from prior reliance on relational KB and queries. CO-LMLM generates flexible vector queries at minimal cost, while still integrating human-readable and attributable retrieved knowledge into its generation. We pair this design with an annotation pipeline that tags free-form factual spans in arbitrary text, removing prior work's restriction to Wikipedia. Across pretraining on Wikipedia and FineWeb-Edu and at multiple model scales, CO-LMLM outperforms prior LMLMs and vanilla LLMs in both perplexity and factual precision. At 360M scale, this includes lower perplexity than models pretrained on 40x more data, and SimpleQA-verified performance that is in line with gpt-4o-mini and higher than Claude Sonnet 4.5.

### 🤖 AI 总结

**一句话总结**：Limited memory language models (LMLMs) externalize factual knowledge during pretraining to a knowledge base (KB), rather than memorizing it in their weights. During generation, the model then fetches ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Co-LMLM, Continuous-Query, Limited, Memory, Language, Models, LMLMs, externalize

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07707v1) | [下载PDF](https://arxiv.org/pdf/2607.07707v1.pdf)

---

## [5. From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization](https://arxiv.org/abs/2607.07702v1)

**作者**：Ying Chang, Jiahang Xu, Xuan Feng 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-08

### 📄 论文摘要

The optimization of long-horizon agents increasingly relies on reflection-based mechanisms, where a large language model (LLM) acts as an optimizer to diagnose agent failures and improve agent policies. However, real execution traces are difficult to use directly for optimization: large trace collections are often redundant and heterogeneous, making optimization inefficient and prone to overfitting to low-value failures; meanwhile, each individual trajectory also contains many irrelevant steps, while naive context reduction methods such as truncation or sliding windows can discard causally important evidence and produce misleading optimization signals. To resolve this dilemma, we introduce STRACE (Structural TRajectory Analysis and Causal Extraction), a framework that constructs high signal-noise optimization contexts for more precise and effective optimization. At the batch level, STRACE mines failure patterns to filter redundant traces and retain representative failures; within each selected trace, it performs causal localization over a textual dependency graph to remove non-causal steps and identify the true root-cause module for optimization. Empirical results demonstrate that STRACE significantly outperforms standard context-filtering baselines. Notably, on a challenging formal verification task (VeruSAGE-Bench), it successfully optimizes human-expert designed agents, delivering $1.4\times$ success-rate improvement (42.5% to 58.5%). The code is available at https://github.com/moomight/STRACE .

### 🤖 AI 总结

**一句话总结**：The optimization of long-horizon agents increasingly relies on reflection-based mechanisms, where a large language model (LLM) acts as an optimizer to diagnose agent failures and improve agent policie...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Noisy, Traces, Root, Causes, Structural, Trajectory, Analysis, Causal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07702v1) | [下载PDF](https://arxiv.org/pdf/2607.07702v1.pdf)

---

## [6. DiaLLM: An Investigation into the Robustness-Generation Gap in English Dialect Adaptation](https://arxiv.org/abs/2607.07669v1)

**作者**：Jordan Painter, Dipankar Srirag, Adarsh Kappiyath 等 6 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-08

### 📄 论文摘要

Large language models increasingly \emph{understand} dialectal English, yet still \emph{produce} only standard, US-leaning English, leaving dialectal generation, the harder half of the problem, largely unaddressed. We introduce \textbf{DiaLLM}, which continually pretrains three open-weight language model families on the International Corpus of English and applies implicit and explicit post-training paradigms, each combined with three model alignment strategies, giving the first controlled comparison of these components across Australian, Indian, and Northern British English. Our results reveal that dialectal robustness and generation are \emph{dissociated}: benchmarks are shaped by continual pretraining and SFT, while alignment visibly reshapes generation in ways benchmarks do not capture. Explicit variety-targeted adaptation produces output reliably recognised as dialectal and preferred over broad alignment, yet the method that most aggressively optimises the dialectal reward is not preferred by human evaluators. Independent linguistic analysis corroborates this reward-quality gap, most clearly on two of the three families. No single alignment method dominates, and closing the gap will require richer reward designs and continued investment in dialectal resources. We release all code, checkpoints, and preference datasets.

### 🤖 AI 总结

**一句话总结**：Large language models increasingly \emph{understand} dialectal English, yet still \emph{produce} only standard, US-leaning English, leaving dialectal generation, the harder half of the problem, largel...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, DiaLLM, Investigation, Robustness-Generation, Gap, English, Dialect, Adaptation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07669v1) | [下载PDF](https://arxiv.org/pdf/2607.07669v1.pdf)

---

## [7. Future Confidence Distillation in Large Language Models](https://arxiv.org/abs/2607.07626v1)

**作者**：Sahil Kale  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-08

### 📄 论文摘要

Reliable confidence estimation is essential for deploying large language models (LLMs) in confidence-aware systems, where downstream decisions such as retrieval, tool use, and adaptive computation depend on accurately estimating answer reliability. Existing approaches, however, largely treat confidence as a property of completed responses, overlooking how confidence-related information evolves throughout the answering process. In this work, we investigate confidence from a temporal perspective by comparing pre-solution Feeling-of-Knowing (FOK) and post-solution Judgement-of-Learning (JOL) confidence estimates across frontier and open-source LLMs. We show that post-solution confidence is consistently better calibrated and more discriminative than pre-solution confidence, while linear probes trained on hidden representations recover substantially richer confidence-related information than models explicitly verbalise. Building on this observation, we introduce future confidence distillation, which trains predictors operating on pre-solution hidden representations using teacher confidence estimates produced by post-solution correctness probes. Despite requiring only pre-solution representations for inference, distilled predictors recover much of the calibration improvement achieved by post-solution confidence, remain highly sample efficient, and transfer across datasets within the same domain. Together, our findings demonstrate that confidence-related information evolves throughout the answering process and can be anticipated before answer generation is complete, enabling significantly more reliable yet low-cost confidence estimation.

### 🤖 AI 总结

**一句话总结**：Reliable confidence estimation is essential for deploying large language models (LLMs) in confidence-aware systems, where downstream decisions such as retrieval, tool use, and adaptive computation dep...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Future, Confidence, Distillation, Large, Language, Models, Reliable, estimation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07626v1) | [下载PDF](https://arxiv.org/pdf/2607.07626v1.pdf)

---

## [8. PALS: Percentile-Aware Layerwise Sparsity for LLM Pruning](https://arxiv.org/abs/2607.07557v1)

**作者**：Yazdan Jamshidi, Alexey Shvets  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-07-08

### 📄 论文摘要

One-shot pruning methods like Wanda and SparseGPT apply the same sparsity ratio to every layer of a transformer, ignoring known variation in layer importance. We propose PALS (Percentile-Aware Layerwise Sparsity), which adjusts per-layer sparsity based on the 99th percentile of activation magnitudes, bounded to $\pm 5\%$ around the target ratio. On LLaMA-2-7B at 50\% sparsity, PALS achieves 10.96 WikiText-2 perplexity versus 12.92 for uniform Wanda (mean over 9 runs, $p < 0.001$). The benefit is architecture-dependent: LLaMA-3-8B shows marginal gains and Mistral-7B shows none. We also find that gradient-based allocation -- the seemingly more principled approach -- produces results worse than random, suggesting that gradient magnitude does not predict the impact of discrete weight removal. PALS adds negligible cost to the pruning pipeline and requires no fine-tuning.

### 🤖 AI 总结

**一句话总结**：One-shot pruning methods like Wanda and SparseGPT apply the same sparsity ratio to every layer of a transformer, ignoring known variation in layer importance. We propose PALS (Percentile-Aware Layerwi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, PALS, Percentile-Aware, Layerwise, Sparsity, Pruning, One-shot, methods

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07557v1) | [下载PDF](https://arxiv.org/pdf/2607.07557v1.pdf)

---

## cs.CV

## [9. Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://arxiv.org/abs/2607.07675v1)

**作者**：Shuailei Ma, Jiaqi Liao, Xinyang Wang 等 27 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-08

### 📄 论文摘要

Despite the recent promise in robot control, video generative models suffer from a domain mismatch due to their primary focus on content creation. For example, their design inherently prioritizes visual fidelity and creativity over computational efficiency and physical realism. In this work, we present LingBot-Video, a DiT-based video pretraining paradigm specifically tailored for embodied intelligence. From the architecture perspective, we adopt the Mixture-of-Experts (MoE), instead of dense, framework to achieve a better trade-off between modeling capacity and inference efficiency, and manage to scale it up from scratch. From the data perspective, we construct a data profiling engine that augments standard internet videos with extensive robot-oriented footage, encompassing manipulation, navigation, and egocentric perspectives, to equip the base model with an intrinsic understanding of actions and world dynamics. From the training perspective, we develop a multi-dimensional reward system to enforce the alignment regarding physical rationality and task completion, going beyond standard criteria such as aesthetics, prompt-following, and motion consistency. Comprehensive evaluations validate its performance and efficiency as a video foundation model. We contribute LingBot-Video as the inaugural large-scale, open-source MoE video foundation model to the community, in a pioneering effort to bridge digital creativity and physical actuation.

### 🤖 AI 总结

**一句话总结**：Despite the recent promise in robot control, video generative models suffer from a domain mismatch due to their primary focus on content creation. For example, their design inherently prioritizes visu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Scaling, Mixture-of-Experts, Video, Pretraining, Embodied, Intelligence, Despite, recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07675v1) | [下载PDF](https://arxiv.org/pdf/2607.07675v1.pdf)

---

## [10. MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models](https://arxiv.org/abs/2607.07673v1)

**作者**：Hyunjae Kim, Dain Kim, Pan Xiao 等 28 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-07-08

### 📄 论文摘要

Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams. Yet the development of multimodal foundation models is constrained by limited access to large-scale, high-quality clinical data. Although PubMed Central (PMC) offers a complementary source of expert-authored image-text data, existing PMC-derived resources remain limited in fidelity, reproducibility, and clinical validation. We introduce MedPMC, an automated, continuously updatable framework that transforms permissively licensed literature into high-fidelity infrastructure for medical multimodal models. Applied to 6.1 million PMC articles, MedPMC curated 11 million medical image-text pairs. Component evaluations showed strong performance for initial screening (F1 = 93.2), multi-panel figure detection (F1 = 96.5), figure separation (mAP = 89.8), caption separation and alignment (F1 = 81.4; ROUGE-L = 85.3), and medical figure classification (F1 = 96.5). Manual review by five annotators, three with medical training, found 95.3% of MedPMC images medically relevant, versus 19.7% in a prior PMC-derived dataset. Across 26 benchmarks spanning 11 specialties, a MedPMC-trained CLIP-style model improved average zero-shot AUC by 7.1 percentage points over the strongest architecture-matched biomedical CLIP baseline despite using fewer than half as many image-text pairs. As the vision encoder in a multimodal large language model, it improved medical visual question-answering by 1.9 and 16.9 percentage points across two benchmarks. In 10,524 Yale New Haven Health System dermatology photographs, it improved morphology-to-image retrieval Recall@5 by 11.7 percentage points. These findings show that high-fidelity literature curation strengthens medical multimodal foundation models across benchmark and clinical settings. We publicly release the framework, corpus, benchmarks, and pretrained models.

### 🤖 AI 总结

**一句话总结**：Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams. Yet the development of multimodal foundation models is constrained by limited access to l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MedPMC, Systematic, Framework, Scaling, High-Fidelity, Medical, Multimodal, Data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07673v1) | [下载PDF](https://arxiv.org/pdf/2607.07673v1.pdf)

---

## [11. Cardiac MRI Through-Plane Super-Resolution Guided by Reference and Memory](https://arxiv.org/abs/2607.07581v1)

**作者**：Shaoming Pan, Chenchuhui Hu, Leon Axel 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-08

### 📄 论文摘要

Clinical cardiac MRI is commonly acquired with high in-plane resolution but coarse through-plane resolution to reduce scan time and accommodate breath-hold and cardiac-motion constraints, which limits 3D analysis and diagnostic accuracy. We propose STRMSR, a reference- and memory-guided through-plane super-resolution (SR) framework that reconstructs high-resolution (HR) cardiac volumes by leveraging HR reference views acquired from the same subject and intermediate SR results as the memory. Our method uses coarse-to-fine contextual matching to establish robust correspondence between low-resolution target and reference/memory images under spatial misalignment. A learnable patch-wise dynamic feature aggregation module predicts content-adaptive mixture weights for each local patch, effectively fusing dynamic information while suppressing unreliable feature transfers. The intermediate SR results stored in the memory bank ensure slice-to-slice consistency for the super-resolved 3D volume. Experiments on the WHS cardiac MRI dataset under two reference protocols, orthogonal-plane views and long-axis chamber views, demonstrate consistent improvements over baselines at 4x and 8x upsampling factors.

### 🤖 AI 总结

**一句话总结**：Clinical cardiac MRI is commonly acquired with high in-plane resolution but coarse through-plane resolution to reduce scan time and accommodate breath-hold and cardiac-motion constraints, which limits...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Cardiac, MRI, Through-Plane, Super-Resolution, Guided, Reference, Memory, Clinical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07581v1) | [下载PDF](https://arxiv.org/pdf/2607.07581v1.pdf)

---

## [12. Automatic Echocardiography Segmentation via Transition Probability Correlation for Stable Semantic Extraction](https://arxiv.org/abs/2607.07580v1)

**作者**：Xinran Chen, Xiyuan Wang, Guangquan Zhou 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-08

### 📄 论文摘要

While echocardiography is essential for cardiovascular diagnosis, inherent speckle noise and low signal-to-noise ratio often lead to ambiguous semantic features and fragmented boundaries. These limitations significantly hinder the segmentation accuracy of deep learning models in complex clinical cases. Moreover, temporal motion of the heart plays a critical role in recognizing anatomical structures. To address these challenges, we designed a STLSF module which comprises a window-matching-based semantic correction component and a semantics-guided texture enhancement component. By leveraging local transition probability correlations to correct semantics and employing semantics-guided texture enhancement, the STLSF module effectively mitigates texture instability and ambiguous semantic interpretations caused by disadvantaged echocardiography quality. Additionally, to facilitate the encoder's adaptation to the intrinsic priors of ultrasound-specific imaging patterns, we propose a frequency-aware denoising pre-training method. The entire work builds a convolution-based network with locality inductive bias and long-range dependencies. Extensive experiments confirm our SOTA performance, achieving 93.87\% Dice on CAMUS and 92.62\% on EchoNet-Dynamic, with respective HD95 values of 3.29mm and 2.73mm.

### 🤖 AI 总结

**一句话总结**：While echocardiography is essential for cardiovascular diagnosis, inherent speckle noise and low signal-to-noise ratio often lead to ambiguous semantic features and fragmented boundaries. These limita...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Automatic, Echocardiography, Segmentation, via, Transition, Probability, Correlation, Stable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07580v1) | [下载PDF](https://arxiv.org/pdf/2607.07580v1.pdf)

---

## [13. AA-ViT: Anatomically Aware Vision Transformer with Structural and Frequency Guidance for Contrast Enhanced Brain MRI Synthesis](https://arxiv.org/abs/2607.07553v1)

**作者**：Talha Meraj, Tom Flannery, Charlie Cummins 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-08

### 📄 论文摘要

Accurate tumour localization and diagnosis is a critical component of clinical care for brain cancers. Magnetic Resonance Imaging (MRI) is the most commonly used imaging modality due to its superior soft-tissue contrast. However, standard MRI often exhibits limited contrast and imaging artifacts, which necessitates the use of contrast agents to enhance lesion visibility. The administration of chemical contrast agents is not always feasible and may be contraindicated in patients with renal impairment or other health conditions. As a result, developing accurate and non-invasive contrast enhanced MRI (CEMRI) synthesis methods has clinical importance. In recent years, numerous approaches for CEMRI synthesis have been proposed, predominantly relying on generative artificial intelligence models. While these methods demonstrate promising performance, their dependence on implicit feature learning often limits their ability to preserve anatomical boundaries and tumour-specific fine structures. To address these challenges, we propose an anatomically aware frequency-and-structure-guided vision transformer (AA-ViT), for CEMRI synthesis using pre-contrast MRI modalities (T1, T2, and FLAIR). Experiments on the BraTS 2021 dataset demonstrate that the proposed method preserves anatomical and lesion boundaries, achieving higher PSNR and SSIM than state-of-the-art approaches. Clinical evaluation by three neuroradiologists and a neurosurgeon on 19 randomly selected cases across diverse gliomas yielded a mean score of 3.94/5, providing preliminary clinical validation rarely seen in prior studies. Synthetic post-contrast scans from our model could lower scanning costs, shorten imaging time, and avoid the potential risks of using gadolinium-based contrast agents.

### 🤖 AI 总结

**一句话总结**：Accurate tumour localization and diagnosis is a critical component of clinical care for brain cancers. Magnetic Resonance Imaging (MRI) is the most commonly used imaging modality due to its superior s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AA-ViT, Anatomically, Aware, Vision, Transformer, Structural, Frequency, Guidance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07553v1) | [下载PDF](https://arxiv.org/pdf/2607.07553v1.pdf)

---

## [14. Face-trace: Open-Set Attribution and Progressive Discovery of Synthetic Face Generators](https://arxiv.org/abs/2607.07545v1)

**作者**：Alessia Infantino, Claudio Schiavella, Irene Amerini  
**分类**：cs.CV  
**发布时间**：2026-07-08

### 📄 论文摘要

Recent advances in generative Artificial Intelligence have made synthetic face images increasingly realistic, creating new challenges for multimedia forensics. Source attribution methods should not only identify the generator of an image when the source is known, but also handle samples produced by previously unseen models. However, most existing approaches address synthetic face attribution in a closed-set setting, where all possible generators are available during training. This assumption does not hold in real-world scenarios, where new generators continuously appear and rejected samples should be organized rather than simply discarded. In this work we propose a pipeline for open-set synthetic face source attribution that combines known generator classification, energy-based OOD rejection, and unknown generator discovery. A classifier is trained on known generators using frozen I-JEPA embeddings, while rejected samples are represented by combining projected I-JEPA features with Forensic Self-Descriptors and then clustered to discover groups of unknown generators. We also extend the discovery stage to an incremental scenario, where rejected samples arrive over time. Experiments on the WILD dataset show that the proposed method achieves 96.73% closed-set attribution accuracy. In the open-set setting, energy-based rejection reaches 71.25% balanced accuracy, while rejected samples are clustered into meaningful unknown-generator groups, obtaining an ARI of 0.81, an NMI of 0.90, and an overall clustering purity of 87.74%. In the incremental setting, the discovered generator space is progressively extended while maintaining a final purity of 99.23%. Cross-dataset experiments suggest that the pipeline can operate beyond the original dataset distribution, although post-processing remains challenging.

### 🤖 AI 总结

**一句话总结**：Recent advances in generative Artificial Intelligence have made synthetic face images increasingly realistic, creating new challenges for multimedia forensics. Source attribution methods should not on...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Face-trace, Open-Set, Attribution, Progressive, Discovery, Synthetic, Face

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07545v1) | [下载PDF](https://arxiv.org/pdf/2607.07545v1.pdf)

---

## [15. Infinite Worlds with Versatile Interactions](https://arxiv.org/abs/2607.07534v1)

**作者**：Zelin Gao, Qiuyu Wang, Jiapeng Zhu 等 20 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-08

### 📄 论文摘要

We present LingBot-World 2.0 (also known as LingBot-World-Infinity), an advanced iteration of LingBot-World featuring four distinct upgrades. (1) Our model achieves an unbounded interaction horizon while maintaining consistent output quality, benefiting from a carefully crafted causal pretraining paradigm. (2) Through distilling a real-time variant from the base model, our system guarantees rapid response time, sufficient to drive 720p video streams at 60 fps. (3) Compared to the previous version, this update introduces highly diverse interactive elements, comprising a broader spectrum of actions (e.g., attacking, archery, spell-casting, and shooting) alongside a richer variety of text-driven events. (4) We pioneer the integration of an agentic harness within the domain of world modeling, wherein a pilot agent is tasked with planning and executing character behaviors, while a director agent is responsible for synthesizing novel environmental elements as the scene progresses. Additionally, to facilitate a shared experience, we develop an interface that permits multiple players to simultaneously immerse themselves in this vivid world simulator. We pair our primary 14B model with a lightweight 1.3B counterpart, which supports effortless deployment on a single GPU.

### 🤖 AI 总结

**一句话总结**：We present LingBot-World 2.0 (also known as LingBot-World-Infinity), an advanced iteration of LingBot-World featuring four distinct upgrades. (1) Our model achieves an unbounded interaction horizon wh...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Infinite, Worlds, Versatile, Interactions, present, LingBot-World, also

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07534v1) | [下载PDF](https://arxiv.org/pdf/2607.07534v1.pdf)

---

## [16. Context-Aware Slum Mapping in Sub-Saharan Africa Using Sentinel-1 Texture and Local Climate Zones](https://arxiv.org/abs/2607.07532v1)

**作者**：Peterson Chepkilot, Babak Memar, Paolo Gamba  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-07-08

### 📄 论文摘要

Accurate mapping of informal settlements remains a major challenge in Sub-Saharan African (SSA) cities because optical imagery often fails to distinguish Informal Settlements (defined here as LCZ 7) from spectrally similar formal Compact Low-Rise areas (LCZ 3). This study presents a context-aware, reproducible Optical-SAR framework that improves informal settlement delineation using Sentinel-2 spectral features and Sentinel-1 structural information within an adapted Local Climate Zone (LCZ) taxonomy. We implement a three-tier SAR integration strategy: calibrated backscatter, GLCM textures, and a physics-guided feature engineered to capture the high structural disorder and weak radar return characteristic of SSA informal settlements. Using reference data across Nairobi and Eldoret (Kenya), we evaluate performance via a stratified hold-out protocol and a season-aware ablation study. Results show that SAR textures provide the dominant performance gain for LCZ 7 detection. The Optical-SAR model achieves overall accuracy of 0.816 (dry) and 0.807 (wet), significantly outperforming the WUDAPT baseline (OA 0.704) and reducing the critical LCZ 3 - LCZ 7 confusion to 7%. Seasonal analysis indicates that while optical-only separability varies with phenology, SAR-derived textures stabilize informal settlement mapping across seasons. These findings demonstrate that the incorporation of SAR-derived features yields consistent improvements for urban morphology mapping in data-scarce environments across seasons and across the evaluated source cities, while cross-city transfer remains limited without local adaptation strategies.

### 🤖 AI 总结

**一句话总结**：Accurate mapping of informal settlements remains a major challenge in Sub-Saharan African (SSA) cities because optical imagery often fails to distinguish Informal Settlements (defined here as LCZ 7) f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Context-Aware, Slum, Mapping, Sub-Saharan, Africa, Sentinel-1, Texture, Local

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07532v1) | [下载PDF](https://arxiv.org/pdf/2607.07532v1.pdf)

---

## cs.LG

## [17. Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF](https://arxiv.org/abs/2607.07693v1)

**作者**：Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-07-08

### 📄 论文摘要

Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck. In this paper, we propose two complementary strategies that substantially improve the feedback efficiency of diffusion RLHF while preserving generalization to unseen prompts. Our key observation is that reward information in diffusion trajectories is unevenly distributed: not all denoising timesteps or trajectories contribute equally to learning from a reward signal. By emphasizing informative timesteps and trajectories during optimization, we obtain more effective gradient updates. First, we introduce a per-timestep weighting scheme that reweights denoising steps during policy optimization. We theoretically connect this weighting to the optimal convergence properties of proximal policy optimization (PPO) and approximate the resulting weighting trend empirically. Second, we introduce a replay mechanism that prioritizes informative trajectories, enabling the model to reuse past samples instead of repeatedly querying new rewards. Together, these strategies significantly improve the feedback efficiency of diffusion RLHF. Under identical hyperparameter settings, our approach achieves up to a 6$\times$ improvement in sample efficiency compared to widely used diffusion RLHF baselines.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly fe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Selective, Timestep, Weighting, Advantage-Based, Replay, Sample-Efficient, RLHF

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07693v1) | [下载PDF](https://arxiv.org/pdf/2607.07693v1.pdf)

---

## [18. Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning](https://arxiv.org/abs/2607.07690v1)

**作者**：Vladislav Beliaev  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-07-08

### 📄 论文摘要

Reinforcement learning from verifiable rewards (e.g. GRPO) is the engine behind today's reasoning models, yet it grades only the final answer. On hard problems this trains models to write more rather than to think better, since the trace itself is never graded and no label for good thinking exists. We introduce Agon, which makes two competing models each other's graders. Both attempt the same problem; in alternating roles, one drafts a solution and the other reads it while solving, and each is rewarded for out-solving the other. To win, a model must out-reason a rival that has seen its work, so reasoning is judged implicitly during training, with no process labels and no reward model. Because both models are optimized, each faces a progressively stronger rival, which single-model RL cannot provide. The two need only be comparably strong and behaviorally different. At inference the pair deploys as it trains, a two-stage cascade in which one model drafts and the other answers after reading the draft. On the hard split of DeepMath with Qwen3, this doubles GRPO's pass@1, roughly eight times the gain of an untrained Mixture-of-Agents pass over the same base. The ordering replicates on competitive-programming code and across model families (Qwen3.5, Gemma 4). For now the models talk in text; the next step is to let them reason together in latent space.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning from verifiable rewards (e.g. GRPO) is the engine behind today's reasoning models, yet it grades only the final answer. On hard problems this trains models to write more rather ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, of, Agon, Competitive, Cross-Model, Implicit, Rival, Grading

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07690v1) | [下载PDF](https://arxiv.org/pdf/2607.07690v1.pdf)

---

## [19. ECGLight: Compute-Light Framework For Paper ECG Digitization and Myocardial Infarction Screening](https://arxiv.org/abs/2607.07683v1)

**作者**：Shreyasvi Natraj, Cyrus Achtari, Felice Gragnano 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-08

### 📄 论文摘要

Electrocardiography (ECG) is one of the most widely used tests for diagnosing cardiovascular disease. Yet several remote clinics still utilize paper ECG printouts for their analysis due to limited connectivity and computational capacity. As a result, vast numbers of physical ECGs obtained in remote areas still remain incapable of being accessed by contemporary artificial-intelligence (AI)-based decision support as they require high computational resources or strong high-speed internet connectivity. This causes several cases where conditions like acute coronary occlusion (ACS) is overlooked and reperfusion therapy delayed. Although prior work has tackled digitization and diagnosis separately, and utilized advanced AI models for them, there still remains a lack of a compute-light, on-device framework that reconstructs paper ECGs at high fidelity, while accurately supporting multiple clinically relevant endpoints. We address this need with an end-to-end lightweight on-device digitization-to-diagnosis pipeline that converts a smartphone photo or scan of a paper ECG into a calibrated 12-lead signal and screens for Myocardial Infarction (MI) pathologies, with SHapley Additive exPlanations (SHAP) to support interpretability. Trained and evaluated on 21,799 ECGs from the PTB-XL dataset and further validated on hospital-acquired ECG-Matrix dataset, the complete system runs in <30 s per ECG on CPU-only resources, achieving 95.51% accuracy (F1 = 0.9519) for MI detection on PTB-XL and 88.89% accuracy (F1 = 0.8862) for OMI detection on ECG-Matrix. This work showcases that legacy paper records can be reliably democratized in any part of the world, providing a scalable decision support when digital ECG export, connectivity, or high-end compute are unavailable

### 🤖 AI 总结

**一句话总结**：Electrocardiography (ECG) is one of the most widely used tests for diagnosing cardiovascular disease. Yet several remote clinics still utilize paper ECG printouts for their analysis due to limited con...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ECGLight, Compute-Light, Framework, Paper, ECG, Digitization, Myocardial, Infarction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07683v1) | [下载PDF](https://arxiv.org/pdf/2607.07683v1.pdf)

---

## [20. Neural Operator-enabled Topology-informed Evolutionary Strategy for PDE-Constrained Optimization](https://arxiv.org/abs/2607.07682v1)

**作者**：Xiangming Huang, Guannan Zhang, Lu Lu 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-08

### 📄 论文摘要

The inverse design of physical systems governed by partial differential equations is computationally demanding due to the high dimensionality and non-convexity of design spaces. Generative models for inverse design often lack robustness and transferability, whereas evolutionary strategies are robust but struggle in high-dimensional spaces. This paper introduces a Neural Operator-enabled Topology-informed Evolutionary Strategy (NOTES) that integrates dimensionality reduction, representation learning, and evolutionary optimization for efficient and transferable inverse design. NOTES couples a DeepONet-based neural operator with the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) to perform global optimization in a compact latent space that encodes topology-aware priors while discovering high-performance designs for unseen operating conditions. Applied to nanophotonic beam-deflector inverse design governed by Maxwell's equations, NOTES reduces the design dimensionality from 256 to 25 and consistently achieves over 95 percent efficiency, outperforming CMA-ES, topology optimization, and other baselines. Applied to structural optimization, NOTES discovers designs that achieve compliance down to 246. By decoupling topology learning of a DeepONet from the governing physics in a PDE solver, NOTES provides a flexible and transferable framework for the inverse design of physical systems.

### 🤖 AI 总结

**一句话总结**：The inverse design of physical systems governed by partial differential equations is computationally demanding due to the high dimensionality and non-convexity of design spaces. Generative models for ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Neural, Operator-enabled, Topology-informed, Evolutionary, Strategy, PDE-Constrained, Optimization, inverse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07682v1) | [下载PDF](https://arxiv.org/pdf/2607.07682v1.pdf)

---

## [21. How Data Shapes RoPE Frequency Usage: From Positional Scale Matching to Length Generalization](https://arxiv.org/abs/2607.07678v1)

**作者**：Xinyi Wu, Siyuan Liu, Ali Jadbabaie  
**分类**：cs.LG  
**发布时间**：2026-07-08

### 📄 论文摘要

Rotary Position Embeddings (RoPE) provide transformers with a fixed grid of positional frequencies, yet trained models use these frequencies highly non-uniformly. We study what determines this frequency usage and propose a data-centered explanation: RoPE frequencies are selected to match the relative-distance structure of the training data. Viewing each frequency as a positional lens, we formalize a field-resolution tradeoff and show that, for a data-induced dependency profile of width $W$, the optimal frequency scales as $1/W$. This frequency-matching principle explains controlled observations on synthetic and text-based data, and suggests that the mid-low frequency bands observed in language models arise from the multi-scale dependency structure of natural language. We further connect frequency selection to position-interpolation-based length generalization: scaling frequencies down expands the effective field while reducing resolution. This helps when longer-context dependencies are approximate dilations of those seen during training, but can fail when relevant dependencies do not scale with context length. Empirically, we show that natural language exhibits approximate self-similarity across positional scales, explaining why test-time frequency scaling can support long-context generalization. Overall, our results identify a data-driven mechanism behind emergent RoPE frequency usage and show that long-context generalization depends on two forms of scale matching: between learned frequencies and training-time dependencies, and between frequency scaling and how those dependencies extend to longer contexts.

### 🤖 AI 总结

**一句话总结**：Rotary Position Embeddings (RoPE) provide transformers with a fixed grid of positional frequencies, yet trained models use these frequencies highly non-uniformly. We study what determines this frequen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：How, Data, Shapes, RoPE, Frequency, Usage, Positional, Scale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07678v1) | [下载PDF](https://arxiv.org/pdf/2607.07678v1.pdf)

---

## [22. PeTeR: Post-Training Robustification of Probabilistic Circuits](https://arxiv.org/abs/2607.07671v1)

**作者**：Adrian Ciotinga, Yeming Dai, YooJung Choi  
**分类**：cs.LG  
**发布时间**：2026-07-08

### 📄 论文摘要

Probabilistic circuits (PCs) can model complex joint distributions while supporting exact and efficient computation of many inference queries. However, standard likelihood-based PC learning is vulnerable to overfitting and fragile generalization when confronted with data noise, small sample sizes, or distribution shifts. This can be mitigated using distributionally-robust optimization which consider worst-case distributions within a Wasserstein ball of the empirical distribution, but current methods are limited to training a model from scratch in this framework. Instead, we propose PeTeR: a novel, data-free post-training framework designed to robustify pre-trained PCs against distribution shifts without retraining from scratch. Empirical evaluations across multiple density estimation benchmarks demonstrate that PeTeR effectively robustifies baseline models against both random and adversarial perturbations, achieving competitive or superior performance to data-dependent robust learning baselines.

### 🤖 AI 总结

**一句话总结**：Probabilistic circuits (PCs) can model complex joint distributions while supporting exact and efficient computation of many inference queries. However, standard likelihood-based PC learning is vulnera...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, PeTeR, Post-Training, Robustification, Probabilistic, Circuits, PCs, can

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07671v1) | [下载PDF](https://arxiv.org/pdf/2607.07671v1.pdf)

---

## [23. Guidance Breaks the Fitted Operator: A Terminal-Fitted Repair for Classifier-Free Guidance](https://arxiv.org/abs/2607.07665v1)

**作者**：Shiheng Zhang  
**分类**：cs.LG, math.NA  
**发布时间**：2026-07-08

### 📄 论文摘要

Classifier-free guidance (CFG) is the standard way to strengthen class-conditioning in diffusion and flow-matching samplers, yet at large guidance it oversaturates and destabilizes, symptoms practitioners suppress with more steps or limited-interval schedules. We analyze CFG through an asymptotic-preserving, numerical-analysis lens. Building on a recent result that the deterministic DDIM step is the unique fitted operator for the unguided terminal layer, exact on the final small-sigma stretch of sampling, we show that guidance re-stiffens exactly the discriminative subspace to an anomalous exponent 1+w. DDIM is therefore no longer fitted there, and on coarse meshes its guided residual diverges as sigma_min goes to zero. We prove a guided clock barrier with three ordered step-size thresholds, and read one-step oversaturation as its endpoint: a solver artifact on the calibration model rather than the continuous guided law. The same analysis yields a one-coefficient, zero-extra-NFE repair: replace CFG's w(r-1) by r^(1+w)-r on the guidance direction. On the calibration model's discriminative crossover, this removes CFG's sigma_min-divergent blow-up and is first-order accurate against the exact guided flow as sigma_min goes to zero. On learned CIFAR-10 checkpoints, and as a cross-domain smoke test on Stable Diffusion 1.5 DDIM, it acts as a high-guidance stabilizer at no extra cost rather than a universal quality knob: it cuts residual amplification and saturation, gives 9/9 point-FID wins over CFG on the tested grid, and preserves classifier-proxy target accuracy in the hard-cell blocks. We report the limits alongside: it is not a universal image-quality win, and against a dense vanilla-CFG reference it is not a uniformly better integrator of that field.

### 🤖 AI 总结

**一句话总结**：Classifier-free guidance (CFG) is the standard way to strengthen class-conditioning in diffusion and flow-matching samplers, yet at large guidance it oversaturates and destabilizes, symptoms practitio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Guidance, Breaks, Fitted, Operator, Terminal-Fitted, Repair, Classifier-Free, CFG

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07665v1) | [下载PDF](https://arxiv.org/pdf/2607.07665v1.pdf)

---

## [24. ALER-TI: Aligned Latent Embedding Retrieval for Time Series Imputation](https://arxiv.org/abs/2607.07640v1)

**作者**：Xuan-Thong Truong, Trung-Kien Le, Tung Kieu 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-08

### 📄 论文摘要

Deep learning has significantly advanced time series imputation, yet most existing architectures primarily rely on localized temporal context within the corrupted input sequence. This reliance can be limiting in real-world scenarios, where time series often exhibit non-stationary dynamics, weak temporal correlations, and infrequent patterns that are difficult to reconstruct from nearby observations alone. In this paper, we propose ALER-TI, Aligned Latent Embedding Retrieval for Time Series Imputation, a retrieval-augmented framework that explicitly leverages historical patterns to supplement degraded local context for more reliable missing-value reconstruction. The core of ALER-TI is Latent Embedding Alignment (LEA), which mitigates the representation mismatch between corrupted queries and complete historical candidates. By applying post-hoc masking in the latent space, LEA aligns candidates with the query's missingness pattern while allowing historical embeddings to be pre-computed and cached for efficient retrieval. ALER-TI is model-agnostic and can be integrated with various imputation backbones through a lightweight adaptation module. Extensive experiments on six real-world datasets under different missing rates demonstrate that ALER-TI consistently improves strong baseline models and enhances robustness across diverse imputation settings.

### 🤖 AI 总结

**一句话总结**：Deep learning has significantly advanced time series imputation, yet most existing architectures primarily rely on localized temporal context within the corrupted input sequence. This reliance can be ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ALER-TI, Aligned, Latent, Embedding, Retrieval, Time, Series, Imputation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07640v1) | [下载PDF](https://arxiv.org/pdf/2607.07640v1.pdf)

---

## [25. An optimal control approach for neural network architecture adaptation with a posteriori error estimation](https://arxiv.org/abs/2607.07637v1)

**作者**：C G Krishnanunni, Thomas Scott, Tan Bui-Thanh  
**分类**：cs.LG, math.NA, math.OC  
**发布时间**：2026-07-08

### 📄 论文摘要

This work presents a novel approach for adapting neural network architecture along the depth based on a posteriori error estimation. By formulating neural network training as a continuous-time optimal control problem, we derive rigorous error estimates that quantify how approximation error distributes across network layers. This error decomposition enables a principled depth adaptation strategy: new layers are inserted at locations of maximum estimated error, allowing the network to efficiently capture complex, nonlinear variations in the underlying problem. Our framework introduces a novel network architecture that treats weights and biases as piecewise linear functions varying across layers, with the error estimator bounding the discrepancy between this discrete representation and the true continuous optimal control solution. The approach leverages dual weighted residual methodology from finite element analysis to derive computable upper bounds on the functional error. A key theoretical contribution is the derivation of explicit error bounds that decompose the total approximation error into interval-wise contributions, providing a rigorous basis for targeted architecture refinement. We demonstrate the effectiveness of our method on scientific datasets, including learning the observable-to-parameter map for the Navier-Stokes equation. Numerical results reveal that our approach consistently outperforms existing architecture adaptation methods in terms of generalization performance.

### 🤖 AI 总结

**一句话总结**：This work presents a novel approach for adapting neural network architecture along the depth based on a posteriori error estimation. By formulating neural network training as a continuous-time optimal...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, optimal, control, approach, neural, network, architecture, adaptation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07637v1) | [下载PDF](https://arxiv.org/pdf/2607.07637v1.pdf)

---

## [26. Higher-Order Geometric Updates for Levenberg-Marquardt Method via Riemann Normal Coordinates](https://arxiv.org/abs/2607.07623v1)

**作者**：Jianing Liu, Dong H. Zhang  
**分类**：cs.LG, math.NA, physics.chem-ph, physics.comp-ph, physics.data-an  
**发布时间**：2026-07-08

### 📄 论文摘要

Nonlinear least-squares optimization is central to regression, physics-informed neural networks, and other machine-learning tasks. Such problems have a natural geometric interpretation, model predictions form a manifold in data space, while the chosen parameterization can introduce parameter-effects curvature that becomes a dominant source of nonlinearity. This exposes a limitation of the Levenberg-Marquardt (LM) method, its tangent-space step is applied as a straight update in parameter coordinates. Geodesic acceleration gives a second-order correction, but its removal of parameter-effect curvature is exact only in the infinitesimal-step limit. We propose a Riemann-normal-coordinate Levenberg-Marquardt method (RNC-LM) to improve this consistency for finite optimization steps. By reformulating the geodesic equation, RNC-LM extends geodesic acceleration to arbitrary-order corrections and constructs finite-step updates with progressively higher reparameterization consistency. A line search along the resulting RNC curve controls the traveled distance while keeping the cost close to standard LM. The method eliminates the tangential component of residual acceleration order by order in a moving tangent frame, making the actual objective reduction more consistent with the linear model prediction of LM. On classical nonlinear least-squares benchmarks, RNC-LM improves convergence and robustness in curved valleys and rank-deficient problems. On a reaction-diffusion PINN failure-mode benchmark, it reduces the relative L2 error to the order of 1e-3 and recovers a physically meaningful solution. On a large-scale machine-learning potential-energy-surface fitting task, it achieves a 34-fold speedup over standard LM.

### 🤖 AI 总结

**一句话总结**：Nonlinear least-squares optimization is central to regression, physics-informed neural networks, and other machine-learning tasks. Such problems have a natural geometric interpretation, model predicti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Higher-Order, Geometric, Updates, Levenberg-Marquardt, Method, via, Riemann, Normal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07623v1) | [下载PDF](https://arxiv.org/pdf/2607.07623v1.pdf)

---

## [27. Asymmetric Focal Loss Improves Graph Neural Network Prediction of Drug-Drug Interactions](https://arxiv.org/abs/2607.07611v1)

**作者**：Faranak Hatami, Mousa Moradi  
**分类**：cs.LG, physics.comp-ph  
**发布时间**：2026-07-08

### 📄 论文摘要

Background: Graph neural networks improve computational prediction of polypharmacy side effects, but standard binary cross-entropy training allocates equal capacity to well-classified and difficult examples, potentially missing clinically significant interactions. We evaluated whether an asymmetric focal objective could improve multi-relational drug-drug interaction (DDI) prediction by emphasizing difficult positive interactions. Methods: ClinicalFocal loss was integrated into a relation-aware graph convolutional network using molecular fingerprints, physicochemical descriptors, and learned embeddings. The model was evaluated on TWOSIDES using five-fold cross-validation with identical experimental conditions (architecture, features, data partitions, hyperparameters, and random seeds) for ClinicalFocal loss and binary cross-entropy baseline. Results: ClinicalFocal loss increased accuracy from 0.699 to 0.892 (+19.3 percentage points) and F1 score from 0.700 to 0.894 (+19.4 percentage points). AUROC increased from 0.766 to 0.914, and AUCPR increased from 0.714 to 0.860. The false-negative rate decreased from 29.8% to 9.1%, while specificity increased from 69.6% to 87.5%. Overall classification error decreased from 30.1% to 10.8%, corresponding to a 64.1% relative reduction. Improvements were consistent across all five folds. Conclusions: Asymmetric focal optimization improved classification and ranking performance while achieving 90.9% recall for observed interaction triples, without modifying the underlying architecture. Loss-function design is a direct, tunable lever for improving graph-based DDI prediction.

### 🤖 AI 总结

**一句话总结**：Background: Graph neural networks improve computational prediction of polypharmacy side effects, but standard binary cross-entropy training allocates equal capacity to well-classified and difficult ex...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Asymmetric, Focal, Loss, Improves, Graph, Neural, Network, Prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07611v1) | [下载PDF](https://arxiv.org/pdf/2607.07611v1.pdf)

---

## [28. Multi-Class vs. Multi-Label BERT for CVE-to-CWE Mapping: How Taxonomy Structure Shapes the Errors](https://arxiv.org/abs/2607.07573v1)

**作者**：Ana Schwengber Kelm, Christian Bockermann, Jörg Frochte  
**分类**：cs.LG, cs.CR  
**发布时间**：2026-07-08

### 📄 论文摘要

Assigning Common Weakness Enumeration (CWE) categories to Common Vulnerabilities and Exposures (CVE) records remains an important but largely manual step in vulnerability analysis. We study this task as a text classification problem and compare two modelling choices: a \emph{multi-class} formulation that predicts a single CWE per CVE and a \emph{multi-label} formulation that allows multiple assignments. Three transformer encoders (BERT Base, SecureBERT, and CySecBERT) are evaluated on three nested label spaces (83, 47, and 25 classes). Multi-class training achieves higher macro-F1 across all settings, although the gap to multi-label narrows from 21 to 2 percentage points as the label space shrinks. Post-hoc threshold optimisation on the multi-label side closes this gap on the 25-class setting. Confusion analysis shows that the dominant misclassification patterns follow the CWE hierarchy and are shared across all three encoders (Pearson $r > 0.92$), which suggests that the error structure is driven more by taxonomy design than by encoder choice. A hierarchy-relaxed evaluation that forgives within-family confusions raises macro-F1 from ${\sim}$81\% to ${\sim}$90\%, indicating that strict metrics understate branch-level classifier quality. CySecBERT achieves the strongest results overall, with statistically significant gains concentrated in the multi-label setting.

### 🤖 AI 总结

**一句话总结**：Assigning Common Weakness Enumeration (CWE) categories to Common Vulnerabilities and Exposures (CVE) records remains an important but largely manual step in vulnerability analysis. We study this task ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：vs, Multi-Class, Multi-Label, BERT, CVE-to-CWE, Mapping, How, Taxonomy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07573v1) | [下载PDF](https://arxiv.org/pdf/2607.07573v1.pdf)

---

## [29. Collaborative Synthetic Data Generation for Knowledge Transfer in Federated Learning](https://arxiv.org/abs/2607.07565v1)

**作者**：Maximilian Andreas Hoefler, Karsten Mueller, Wojciech Samek  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-08

### 📄 论文摘要

One-shot federated learning (OSFL) addresses the communication overhead of federated learning by limiting training to a single round, but doing so without sacrificing model quality is non-trivial, particularly when client data distributions diverge. Recent work has addressed this challenge by aggregating client knowledge on the server through the construction of transferable synthetic datasets or distillates. However, most of these methods lack formal privacy guarantees, leaving a gap in jointly achieving low communication, robustness to heterogeneity, and rigorous privacy. We propose FedKT-CSD (Federated Knowledge Transfer via Collaborative Synthetic Data), a framework inspired by neural image compression that closes this gap by leveraging publicly pretrained autoencoders as a shared latent space. Each client encodes its private data in a single forward pass, computes class-conditional latent statistics, and transmits these to the server. The server aggregates these statistics via secure aggregation, adds calibrated differential privacy noise, and decodes a synthetic dataset for training a global model and further downstream tasks. This design provides formal $(\varepsilon,δ)$-differential privacy by construction, while keeping client-side computation and communication lightweight. Despite operating under privacy constraints, FedKT-CSD is competitive with and even outperforms non-private baselines across diverse datasets and heterogeneity settings, and scales to a large number of clients. Our code is available at: https://github.com/an7123/FedKT-CSD

### 🤖 AI 总结

**一句话总结**：One-shot federated learning (OSFL) addresses the communication overhead of federated learning by limiting training to a single round, but doing so without sacrificing model quality is non-trivial, par...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Collaborative, Synthetic, Data, Generation, Knowledge, Transfer, Federated, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07565v1) | [下载PDF](https://arxiv.org/pdf/2607.07565v1.pdf)

---

## [30. Avoiding unsafe sets when training with Langevin Dynamics](https://arxiv.org/abs/2607.07538v1)

**作者**：Adam M. Oberman  
**分类**：cs.LG, math.AP, stat.ML  
**发布时间**：2026-07-08

### 📄 论文摘要

Training a model with noisy gradient descent can be idealized as overdamped Langevin dynamics on the loss landscape, and a natural safety question is to bound the probability $ν_t(\mathcal{A}_H) = \mathbb{P}(Q_t \in \mathcal{A}_H)$ that the trajectory lies in a designated failure region $\mathcal{A}_H$. We study this for a smooth, strongly convex loss in $d$ dimensions and a failure region separated from the minimizer by an energy gap. Three bounds emerge. At the end of training, the equilibrium mass $π(\mathcal{A}_H)$ is exponentially small in $d$, with a complementary energy-barrier rate when the noise is small. Along the trajectory, a shape-free bound $ν_t(\mathcal{A}_H) \le π(\mathcal{A}_H)(1 + \sqrt{χ_0^2/π(\mathcal{A}_H)}\,e^{-mt})$ shows that the in-set probability relaxes to (twice) the static value after a burn-in time of order $d$, using only the global spectral gap $m$ of the loss. A worked Ornstein-Uhlenbeck example shows this burn-in is necessary: an angular slice of the equilibrium shell can transiently swell by a factor exponential in $d$, even though its equilibrium mass is tiny. To rule such swelling out we introduce a local relaxation rate attached to the failure region, defined through the spectral measure of its centered indicator rather than a Dirichlet-form Rayleigh quotient. For geometrically isolated regions this rate exceeds the global one, shrinking the burn-in proportionally, and combined with a maximum-principle ceiling it caps the trajectory probability uniformly in time. The picture is that strong convexity sets how fast training relaxes, but the shape of the unsafe set decides whether the trajectory bulges through it on the way home.

### 🤖 AI 总结

**一句话总结**：Training a model with noisy gradient descent can be idealized as overdamped Langevin dynamics on the loss landscape, and a natural safety question is to bound the probability $ν_t(\mathcal{A}_H) = \ma...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Avoiding, unsafe, sets, when, training, Langevin, Dynamics, model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.07538v1) | [下载PDF](https://arxiv.org/pdf/2607.07538v1.pdf)

---

