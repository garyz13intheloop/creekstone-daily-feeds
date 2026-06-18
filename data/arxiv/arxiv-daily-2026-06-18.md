# arXiv AI 论文日报 | 2026-06-18

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (6 篇)
- [cs.LG](#csLG) (11 篇)
- [cs.CV](#csCV) (10 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. NeSyCat Torch: A Differentiable Tensor Implementation of Categorical Semantics for Neurosymbolic Learning](https://arxiv.org/abs/2606.19279v1)

**作者**：Daniel Romero Schellhorn, Till Mossakowski, Björn Gehrke  
**分类**：cs.AI, cs.LG, cs.LO, math.CT, math.LO, math.PR  
**发布时间**：2026-06-17

### 📄 论文摘要

Neurosymbolic semantics is fragmented: classical, fuzzy, probabilistic and neural systems each define truth by their own inductive rules. NeSyCat, extending ULLER, subsumes them under a single inductive definition of truth, parametric in a strong monad and an aggregation structure on truth-values. NeSyCat has so far lacked an account of predicates and functions learned by neural networks.   We provide NeSyCat Torch as the missing link and interpret computational symbols via neural networks, implementing the framework in probabilistic programming and tensor-based backends. We use the distribution monad for reference semantics and metric evaluation, and complement it by a monad for numerically stable, differentiable training: the lazy log-tensor monad over the log-semiring. For efficient training in batches, we furthermore employ a batch monad. The axioms are the source code: written once in monad-based do-notation, monadic bind performs marginalisation, lazily pruning unneeded branches.   On MNIST addition, our HaskTorch, JAX, and PyTorch implementations outperform LTN and DeepProbLog in speed and accuracy, while achieving nearly the accuracy of DeepStochLog. However, unlike DeepStochLog, we stay in a uniform framework that applies to many first-order NeSy approaches. Namely, the construction is parametric in the monad; instantiating it with, e.g., the Giry monad extends the approach to continuous probability (working out a neural representation here is left for future work).

### 🤖 AI 总结

**一句话总结**：Neurosymbolic semantics is fragmented: classical, fuzzy, probabilistic and neural systems each define truth by their own inductive rules. NeSyCat, extending ULLER, subsumes them under a single inducti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, NeSyCat, Torch, Differentiable, Tensor, Implementation, Categorical, Semantics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19279v1) | [下载PDF](https://arxiv.org/pdf/2606.19279v1.pdf)

---

## [2. X+Slides: Benchmarking Audience-Conditioned Slide Generation](https://arxiv.org/abs/2606.19256v1)

**作者**：Haodong Chen, Xuanhe Zhou, Wei Zhou 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-17

### 📄 论文摘要

Automatically generating slide decks from source documents is an important application of large language models (LLMs). Existing benchmarks primarily assess slide completeness and technical depth, while overlooking the target audience as a critical real-world factor. For instance, specialists demand rigorous proofs, whereas decision-makers prioritize actionable conclusions. To bridge this gap, we introduce X+Slides, a benchmark specifically designed for audience-conditioned slide generation. Built on a diverse corpus spanning 113 topics and seven presentation scenes, X+Slides employs a dynamic evaluation framework constructed from 8,133 deduplicated, source-grounded probes. By assigning audience-specific utility weights to the same source-grounded probes, X+Slides reports four complementary metrics: Audience Coverage measures how much audience-essential information is conveyed, Domain-wise Coverage shows which information types are covered, Efficiency measures delivered utility per unit of attention cost, and Correctness verifies whether slide claims are supported by the source. Experiments on DeepPresenter, SlideTailor, and NotebookLM show that current systems can recover a substantial but still incomplete part of audience-essential information: at $τ_A=0.7$, DeepPresenter reaches a best Audience Coverage of 0.714, SlideTailor reaches 0.594, and the NotebookLM ablation reaches 0.853 while showing clear grounding differences. These results indicate that visual quality and broad topic coverage should not be treated as evidence support without source-grounded evaluation.

### 🤖 AI 总结

**一句话总结**：Automatically generating slide decks from source documents is an important application of large language models (LLMs). Existing benchmarks primarily assess slide completeness and technical depth, whi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：X+Slides, Benchmarking, Audience-Conditioned, Slide, Generation, Automatically, generating, decks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19256v1) | [下载PDF](https://arxiv.org/pdf/2606.19256v1.pdf)

---

## [3. TxBench-PP: Analyzing AI Agent Performance on Small-Molecule Preclinical Pharmacology](https://arxiv.org/abs/2606.19245v1)

**作者**：Hannah Le, Ramesh Ramasamy, Alex Urrutia 等 6 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-06-17

### 📄 论文摘要

Artificial intelligence (AI) agents promise to accelerate drug discovery by compressing interpretation and decision-making loops, but practical deployment requires trusted evaluation on realistic program decisions. We introduce TherapeuticsBench Preclinical Pharmacology (TxBench-PP), a verifiable benchmark for small-molecule preclinical pharmacology and the first focused slice of a broader TherapeuticsBench effort across drug-discovery stages and therapeutic modalities. TxBench-PP tests whether agents can recover accurate conclusions from real-world assay data rather than memorized facts from literature. The benchmark contains 100 evaluations indexed by program stage, assay type, and task structure, spanning mechanism-of-action (MoA) and pharmacodynamic (PD) reasoning, compound-target engagement, causal target validation, developability and safety, and translational efficacy. Agents receive realistic workflow snapshots, inspect files in a coding environment, and return structured answers graded deterministically. Across 16 model-harness configurations, comprising 11 models and 4,800 trajectories, no system reliably recovered preclinical pharmacology decisions. The strongest configuration, Claude Opus 4.8 / Pi, passed 59.3\% of endpoint attempts (178/300; 95\% CI, 51.1-67.6), followed by GPT-5.5 / Pi at 55.3\% (166/300; 47.0-63.6).

### 🤖 AI 总结

**一句话总结**：Artificial intelligence (AI) agents promise to accelerate drug discovery by compressing interpretation and decision-making loops, but practical deployment requires trusted evaluation on realistic prog...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, TxBench-PP, Analyzing, Performance, Small-Molecule, Preclinical, Pharmacology, Artificial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19245v1) | [下载PDF](https://arxiv.org/pdf/2606.19245v1.pdf)

---

## cs.CL

## [4. Learning User Simulators with Turing Rewards](https://arxiv.org/abs/2606.19336v1)

**作者**：Yingshan Susan Wang, Cedegao E. Zhang, Linlu Qiu 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-17

### 📄 论文摘要

Learning to simulate human users in interactive settings could advance the training of agent assistants, evaluation of personalization systems, research in the social sciences, and more. Existing approaches generally do so by training a large language model (LLM) to match a single ground truth response, either by maximizing the log probability or by using a similarity reward. We instead propose {Turing-RL}: a Turing-Test-based reinforcement learning approach for training user simulator models. {Turing-RL} uses a discriminative Turing reward with an LLM judge to score how indistinguishable a generated response is from the real user's given the user's history, and the user simulator LLM learns to produce responses indistinguishable from what the user could have said with such rewards. Across two different domains--conversational chat and Reddit forum discussion--we find that {Turing-RL} consistently outperforms baseline methods on both LLM and human evaluation metrics. Our study suggests that optimizing for indistinguishability, rather than response matching, is effective for learning user simulators.

### 🤖 AI 总结

**一句话总结**：Learning to simulate human users in interactive settings could advance the training of agent assistants, evaluation of personalization systems, research in the social sciences, and more. Existing appr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, User, Simulators, Turing, Rewards, simulate, human, users

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19336v1) | [下载PDF](https://arxiv.org/pdf/2606.19336v1.pdf)

---

## [5. Freeing the Law with LOCUS: A Local Ordinance Corpus for the United States](https://arxiv.org/abs/2606.19334v1)

**作者**：Denis Peskoff, Joe Barrow, Christopher Vu 等 4 位作者  
**分类**：cs.CL, cs.CY, cs.LG  
**发布时间**：2026-06-17

### 📄 论文摘要

Progress in legal AI increasingly depends on access to authoritative legal text at scale. Yet one of the most consequential layers of American law remains largely absent from existing machine-readable corpora: local ordinances. Local codes govern zoning, housing, business licensing, public health, noise, animal control, and many other domains of everyday regulation, but they are fragmented across vendor platforms designed for human browsing rather than bulk research access. We introduce LOCUS - the Local Ordinance Corpus for the United States - a comprehensive corpus and county-harmonized access layer for U.S. municipal and county ordinance codes. The raw corpus, available for release to researchers, represents nearly all publicly available municipal and county ordinance codes. The resulting raw corpus contains codes from 9,239 cities and counties. A smaller county-harmonized LOCUS access layer provides coverage for the largest 2,309 of 3,144 U.S. counties, accounting for a majority of the population. We use OCR to handle the myriad of document formats that have kept the law from being a public resource. We release the corpus with coverage metadata to support reproducibility, downstream legal AI research, and the incremental expansion of machine-readable access to local law. We train a collection of ModernBERT-based classifiers and scorers to facilitate analyzing U.S. local law among several dimensions, such as opacity and paternalism, that have not previously been studied at this scale. LOCUS-v1 and its derivative models are available at: https://huggingface.co/datasets/LocalLaws/LOCUS-v1

### 🤖 AI 总结

**一句话总结**：Progress in legal AI increasingly depends on access to authoritative legal text at scale. Yet one of the most consequential layers of American law remains largely absent from existing machine-readable...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Freeing, Law, LOCUS, Local, Ordinance, Corpus, United, States

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19334v1) | [下载PDF](https://arxiv.org/pdf/2606.19334v1.pdf)

---

## [6. Trade-offs in Medical LLM Adaptation: An Empirical Study in French QA](https://arxiv.org/abs/2606.19266v1)

**作者**：Ikram Belmadani, Oumaima El Khettari, Carlos Ramisch 等 6 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-17

### 📄 论文摘要

The development of large language models (LLMs) has led to an increased focus on their adaptation to specialized domains and languages, yet the effectiveness of domain adaptation strategies remains unclear. We present a study of medical domain adaptation using French medical question-answering (QA) as a case study. We compare continual pretraining (CPT), supervised fine-tuning (SFT), and their combination across three model families, multiple sizes, and three initialization types, explicitly disentangling adaptation effects from base model choice. We evaluate both multiple-choice (MCQA) and open-ended QA (OEQA) under greedy and constrained decoding using automatic metrics and LLM-as-a-Judge evaluation. For MCQA, CPT+SFT most often achieves the best scores, but gains over SFT are small and frequently not statistically significant, making SFT a strong and cost-effective default. For OEQA, CPT consistently improves overlap-based metrics, while SFT often degrades generation quality; instruction tuning and CPT+SFT are preferred by LLM-based evaluation. Cross-lingual experiments further show effective transfer from French adaptation to English benchmarks. Overall, we provide practical guidelines for selecting adaptation strategies under computational constraints.

### 🤖 AI 总结

**一句话总结**：The development of large language models (LLMs) has led to an increased focus on their adaptation to specialized domains and languages, yet the effectiveness of domain adaptation strategies remains un...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, An, Trade-offs, Medical, Adaptation, Empirical, Study, French

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19266v1) | [下载PDF](https://arxiv.org/pdf/2606.19266v1.pdf)

---

## [7. DreamReasoner-8B: Block-Size Curriculum Learning for Diffusion Reasoning Models](https://arxiv.org/abs/2606.19257v1)

**作者**：Zirui Wu, Lin Zheng, Jiacheng Ye 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-17

### 📄 论文摘要

Block diffusion language models accelerate decoding through parallel block-wise denoising, yet whether they can be reliably scaled for long chain-of-thought (CoT) reasoning remains unresolved. To this end, we develop DreamReasoner-8B, an open-source block diffusion reasoning model, and conduct a systematic study of how training and inference block sizes affect long-CoT reasoning. Our analysis reveals a stark performance disparity: training with large block sizes yields remarkably poor reasoning, whereas small block sizes preserve effective reasoning. To bridge this granularity gap, we propose block-size curriculum learning, which gradually transitions training from fine-grained to coarse-grained block sizes, thereby overcoming this limitation and enabling strong reasoning performance that generalizes across diverse inference block sizes. On mathematical and code reasoning benchmarks, DreamReasoner-8B achieves results competitive with leading open autoregressive models such as Qwen3-8B. This work establishes a practical foundation for efficient, reasoning-capable diffusion language models. We release our model at https://github.com/DreamLM/DreamReasoner.

### 🤖 AI 总结

**一句话总结**：Block diffusion language models accelerate decoding through parallel block-wise denoising, yet whether they can be reliably scaled for long chain-of-thought (CoT) reasoning remains unresolved. To this...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, DreamReasoner-8B, Block-Size, Curriculum, Learning, Reasoning, Models, Block

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19257v1) | [下载PDF](https://arxiv.org/pdf/2606.19257v1.pdf)

---

## [8. RECOM: A Validity Discrimination Tradeoff in Automatic Metrics for Open Ended Reddit Question Answering](https://arxiv.org/abs/2606.19218v1)

**作者**：Pushwitha Krishnappa, Amit Das, Vinija Jain 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-17

### 📄 论文摘要

Automatic metrics are the default for evaluating LLM-generated text, yet a metric is quietly asked to do two jobs: tell genuine content alignment from surface coincidence (validity), and tell a better system from a worse one (discriminative power). On open-ended, opinion-driven question answering, the two are in tension. We introduce RECOM (Reddit Evaluation for Correspondence of Models), a contamination-free evaluation dataset of 15,000 r/AskReddit questions (September 2025), each paired with its authentic community replies, which postdate every evaluated model's training cutoff. Scoring five open-source LLMs (7--10B) against every reply each metric paired with a random-derangement noise floor we find that no metric does both jobs well. Cosine similarity separates real from random answers (Cohen's $d \approx 2$) but cannot rank the five models ($|d| < 0.1$); BERTScore precision appears to rank the models (raw $|d|$ up to 0.63), but once response length is controlled this collapses to $|d| = 0.09$ and its validity is weak ($d \approx 0.8$, versus cosine's $\approx 2$). Because every metric scores the same outputs, this validity--discrimination tradeoff is a property of the metrics, not the models, and we argue it stems from representation design. Three independent LLM judges reproduce the validity gap and likewise separate the five models only weakly. We recommend reporting metrics on both axes, with an explicit random-baseline floor. RECOM is publicly available at https://anonymous.4open.science/r/recom-D4B0

### 🤖 AI 总结

**一句话总结**：Automatic metrics are the default for evaluating LLM-generated text, yet a metric is quietly asked to do two jobs: tell genuine content alignment from surface coincidence (validity), and tell a better...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RECOM, Validity, Discrimination, Tradeoff, Automatic, Metrics, Open, Ended

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19218v1) | [下载PDF](https://arxiv.org/pdf/2606.19218v1.pdf)

---

## [9. Language Models as Interfaces, Not Oracles: A Hybrid LLM-ML System for Pediatric Appendicitis](https://arxiv.org/abs/2606.19183v1)

**作者**：Soheyl Bateni, Maryam Abdolali  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-17

### 📄 论文摘要

Large language models (LLMs) can make clinical decision support more accessible by interpreting free-text documentation, but their direct use as diagnostic engines is limited by sensitivity to prompts, information order, and plausible but incorrect outputs. Structured machine-learning models offer more stable risk prediction, yet they require tabular inputs that are difficult to integrate with narrative clinical workflows. We present ClaMPAPP (Clinical Language-assisted Machine-learning Pipeline for Appendicitis), a hybrid system that uses an LLM as an interface rather than as the final decision-maker. ClaMPAPP extracts schema-constrained clinical features from note-like narratives, applies deterministic plausibility checks, and passes validated features to an XGBoost classifier trained on clinical, laboratory, and ultrasound variables. We evaluated ClaMPAPP on two independent pediatric appendicitis cohorts from German hospitals and compared it with end-to-end LLM baselines, including open-source and proprietary models. To preserve ground truth while testing free-text input, narratives were generated from structured electronic health records through template rendering and constrained LLM rewriting, with additional sentence-order permutation to assess positional robustness. ClaMPAPP achieved the strongest overall diagnostic performance in both internal and external validation while minimizing missed appendicitis cases, the key safety concern in acute triage. End-to-end LLMs showed unstable sensitivity-specificity trade-offs and greater degradation under narrative reordering. These results support an LLM-as-interface, ML-as-predictor design that separates natural-language usability from predictive inference and provides a more auditable pathway for clinical decision support.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) can make clinical decision support more accessible by interpreting free-text documentation, but their direct use as diagnostic engines is limited by sensitivity to prompts...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Language, Models, Interfaces, Not, Oracles, Hybrid, LLM-ML

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19183v1) | [下载PDF](https://arxiv.org/pdf/2606.19183v1.pdf)

---

## cs.CV

## [10. NeuMesh++: Towards Versatile and Efficient Volumetric Editing with Disentangled Neural Mesh-based Implicit Field](https://arxiv.org/abs/2606.19316v1)

**作者**：Chong Bao, Yuan Li, Bangbang Yang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-17

### 📄 论文摘要

Recently neural implicit rendering techniques have evolved rapidly and demonstrated significant advantages in novel view synthesis and 3D scene reconstruction. However, existing neural rendering methods for editing purposes offer limited functionalities, e.g., rigid transformation and category-specific editing. In this paper, we present a novel mesh-based representation by encoding the neural radiance field with disentangled geometry, texture, and semantic codes on mesh vertices, which empowers a set of efficient and comprehensive editing functionalities, including mesh-guided geometry editing, designated texture editing with texture swapping, filling and painting operations, and semantic-guided editing. To this end, we develop several techniques including a novel local space parameterization to enhance rendering quality and training stability, a learnable modification color on vertex to improve the fidelity of texture editing, a spatial-aware optimization strategy to realize precise texture editing, and a semantic-aided region selection to ease the laborious annotation of implicit field editing. Extensive experiments and editing examples on both real and synthetic datasets demonstrate the superiority of our method on representation quality and editing ability. Project page: https://zju3dv.github.io/neumeshplusplus/

### 🤖 AI 总结

**一句话总结**：Recently neural implicit rendering techniques have evolved rapidly and demonstrated significant advantages in novel view synthesis and 3D scene reconstruction. However, existing neural rendering metho...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：NeuMesh++, Towards, Versatile, Efficient, Volumetric, Editing, Disentangled, Neural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19316v1) | [下载PDF](https://arxiv.org/pdf/2606.19316v1.pdf)

---

## [11. Confidence is Not Reliability: Rethinking MC Dropout in Brain Tumour Segmentation](https://arxiv.org/abs/2606.19300v1)

**作者**：Xin Ci Wong, Duygu Sarikaya, Kieran Zucker 等 5 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-06-17

### 📄 论文摘要

Glioma segmentation in multiparametric MRI is a critical component of treatment planning. A segmentation model that fails silently on treatment-critical sub-regions represents a patient safety risk that overlap-based metrics such as Dice scores cannot expose. We ask whether voxel-level uncertainty estimation via Monte Carlo (MC) Dropout can reliably identify segmentation errors in clinically critical sub-regions, and whether calibration failure modes are detectable from standard reporting metrics alone. In an empirical two-model case study on 126 BraTS21 patients, we evaluate a high-performance pretrained SegResNet and a locally trained UNet with residual units (UNet-Res). MC dropout preserved segmentation accuracy ($|Δ\text{Dice}|$ $<0.01$) while achieving strong uncertainty-error alignment (AUROC for entropy (H) $\approx$0.97), indicating uncertainty correctly ranks erroneous voxels above correct ones. Entropy-based patient stratification identified a high-uncertainty subgroup with substantially lower segmentation performance (median whole-tumour Dice $0.835$ vs. $0.925$), supporting uncertainty as a practical triage signal. However, global alignment can mask important region-specific differences. Despite similar AUROC, UNet-Res exhibited near-zero enhancing tumour entropy ($0.054$) and Expected Calibration Error (ECE) of $0.915$, with a Dice of only $0.714$, indicating severely miscalibrated confidence on the most clinically critical sub-region, a failure mode invisible to standard Dice and AUROC reporting. These findings demonstrate that strong uncertainty-error alignment is necessary but insufficient for clinical safety: sub-region-specific calibration assessment must accompany AUROC evaluation when selecting models for clinical deployment.

### 🤖 AI 总结

**一句话总结**：Glioma segmentation in multiparametric MRI is a critical component of treatment planning. A segmentation model that fails silently on treatment-critical sub-regions represents a patient safety risk th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MC, Confidence, Not, Reliability, Rethinking, Dropout, Brain, Tumour

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19300v1) | [下载PDF](https://arxiv.org/pdf/2606.19300v1.pdf)

---

## [12. A Unified Framework for Efficient Remote Sensing Visual Question Answering: Adapting Dual, Hybrid, and Encoder-Decoder Architectures](https://arxiv.org/abs/2606.19277v1)

**作者**：Timothy Agboada, Shikha Chandel, Yadav Raj Ghimire 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-17

### 📄 论文摘要

Visual Question Answering (VQA) in the Remote Sensing (RS) domain presents unique challenges due to the high resolution, multi scale object distribution, and semantic complexity of aerial imagery. While general domain Foundation Models have achieved remarkable success, their direct application to RSVQA is hindered by massive domain shifts and the computationally prohibitive nature of full fine tuning. This study presents a comparative analysis of RS Adapter, a Parameter Efficient Fine Tuning (PEFT) strategy, applied across three distinct Vision Language Model (VLM) architectures: the Dual Encoder CLIP, the Encoder Decoder BLIP, and the Hybrid FLAVA. We introduce a unified architectural surgery pipeline that injects lightweight bottleneck adapters into the attention and MLP layers of frozen backbones, enabling rapid adaptation with less than 5 percent of trainable parameters. Experimental results on the high resolution RSVQA x dataset demonstrate that while all adapted models achieve convergence, the Hybrid FLAVA architecture offers a superior balance of multimodal reasoning and retrieval capabilities compared to its unimodal counterparts. Our findings establish a new baseline for resource efficient VQA in disaster assessment and urban monitoring.

### 🤖 AI 总结

**一句话总结**：Visual Question Answering (VQA) in the Remote Sensing (RS) domain presents unique challenges due to the high resolution, multi scale object distribution, and semantic complexity of aerial imagery. Whi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unified, Framework, Efficient, Remote, Sensing, Visual, Question, Answering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19277v1) | [下载PDF](https://arxiv.org/pdf/2606.19277v1.pdf)

---

## [13. A Multi-Domain Benchmark for Detecting AI-Generated Text-Rich Images from GPT-Image-2](https://arxiv.org/abs/2606.19259v1)

**作者**：Yijin Wang, Shuyi Wang, Wenhan Zhang 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-17

### 📄 论文摘要

Text-rich images often contain privacy-sensitive, transactional, or decision-relevant information. As recent multimodal image generation models become increasingly capable of synthesizing realistic textual content and structured visual designs, detecting AI-generated text-rich images has become an important challenge for digital trust and content authenticity. Existing benchmarks, however, largely focus on object-centric images and provide limited coverage of scenarios where textual semantics and layout organization are central. In this paper, we introduce a multi-domain benchmark for detecting text-rich images generated by OpenAI's GPT Image 2. The benchmark contains 8,602 images across six representative categories: commercial posters, infographics, academic posters, receipts, tables, and UI screenshots. Using this benchmark, we evaluate five representative AI-generated image detectors in a zero-shot setting and analyze their overall, category-wise, and post-processing robustness. Our results show that detector performance is highly domain-dependent: methods that perform well in some categories often fail on others, and even the strongest conventional detector exhibits severe sensitivity to JPEG compression. We further conduct an exploratory evaluation with a multimodal vision-language model, revealing both its promise and its limitations on structured formats. These findings highlight the need for text- and layout-aware detection methods for modern AI-generated images. Our dataset is released at XXX.

### 🤖 AI 总结

**一句话总结**：Text-rich images often contain privacy-sensitive, transactional, or decision-relevant information. As recent multimodal image generation models become increasingly capable of synthesizing realistic te...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Domain, Benchmark, Detecting, AI-Generated, Text-Rich, Images, GPT-Image-2, often

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19259v1) | [下载PDF](https://arxiv.org/pdf/2606.19259v1.pdf)

---

## [14. CABLE: Cloud-Assisted Bandwidth-efficient LMM-based Encoding for V2X Systems](https://arxiv.org/abs/2606.19258v1)

**作者**：Haohua Que, Zhipeng Bao, Qianyi Wu 等 4 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-06-17

### 📄 论文摘要

Cloud-hosted large multimodal models (LMMs) can provide strong open-vocabulary perception for Vehicle-to-Everything systems, but naively transmitting full-resolution frames from edge to cloud causes severe communication overhead and high cloud-side prefill latency. We present CABLE, a cloud-assisted bandwidth-efficient LMM-based encoding framework for edge-cloud perception. CABLE propagates the previous cloud segmentation mask on the edge using ego-motion compensation, refines it with residual-motion cues, and consolidates disconnected regions via a corridor envelope to form a robust region of interest (ROI). Only ROI-masked images are uploaded, while the cloud segmentation output is fed back as the prior for the next frame, forming a mask-to-ROI-to-LMM feedback loop. Experiments on five datasets (nuScenes, WOD-ZB, Waymo, KITTI, and CADC) show consistent communication savings while largely preserving perception, achieving $73$--$87\%$ ROI pixel-coverage reduction with $5$--$8\times$ estimated LMM prefill speedup at a modest detection-quality trade-off relative to full-frame inference.

### 🤖 AI 总结

**一句话总结**：Cloud-hosted large multimodal models (LMMs) can provide strong open-vocabulary perception for Vehicle-to-Everything systems, but naively transmitting full-resolution frames from edge to cloud causes s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：V2X, CABLE, Cloud-Assisted, Bandwidth-efficient, LMM-based, Encoding, Systems, Cloud-hosted

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19258v1) | [下载PDF](https://arxiv.org/pdf/2606.19258v1.pdf)

---

## [15. OneCanvas: 3D Scene Understanding via Panoramic Reprojection](https://arxiv.org/abs/2606.19253v1)

**作者**：Bartłomiej Baranowski, Dave Zhenyu Chen, Matthias Nießner  
**分类**：cs.CV, cs.AI, cs.LG, cs.RO  
**发布时间**：2026-06-17

### 📄 论文摘要

Existing approaches to 3D scene understanding in Vision-Language Models (VLMs) either rely on complex, model-specific geometry encoders or large training budgets in pursuit of spatial reasoning. Instead, OneCanvas aggregates patch features from all views onto a single equirectangular panoramic canvas. Namely, each patch is unprojected to a 3D world coordinate using its depth and camera pose, then placed on the canvas at the continuous longitude and latitude of that point as seen from the canvas origin, with no rasterization or aggregation across overlapping views. A 3D position embedding of the patch's metric coordinates is added to its feature, restoring the depth lost when collapsing the world position to an angular canvas coordinate. Patches from all frames thus share one spatial coordinate system with no fusion or major architectural modifications of the backbone. The pretrained VLM consumes this representation as if it were an ordinary image. Because the canvas can be centered on any pose of interest, the same representation directly supports situated reasoning from a specific viewpoint, a common requirement in robotics and embodied AI. Thanks to this representation, we can also introduce a spatial pretraining curriculum: by procedurally placing patch features of objects, drawn from real images, at chosen 3D world positions on an otherwise empty canvas, we generate on-the-fly supervision spanning a broad range of spatial reasoning tasks, with answer distributions controlled to reduce spatial reasoning shortcuts. OneCanvas achieves state-of-the-art accuracy on SQA3D and VSI-Bench, and generalizes to out-of-distribution data on SPBench, using an order of magnitude less training compute than the strongest competing methods.

### 🤖 AI 总结

**一句话总结**：Existing approaches to 3D scene understanding in Vision-Language Models (VLMs) either rely on complex, model-specific geometry encoders or large training budgets in pursuit of spatial reasoning. Inste...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, OneCanvas, Scene, Understanding, via, Panoramic, Reprojection, Existing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19253v1) | [下载PDF](https://arxiv.org/pdf/2606.19253v1.pdf)

---

## [16. GUMP-Net: An interpretable model-data-driven intelligent algorithm for multi-class pelvic segmentation](https://arxiv.org/abs/2606.19215v1)

**作者**：Liheng Wang, Yinghui Zhang, Licheng Zhang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-17

### 📄 论文摘要

Pelvic segmentation is one of the most important and fundamental research problems in precise and intelligent diagnosis and treatment, as well as surgical planning and navigation for pelvic fractures. By combining an improved geodesic active contour model with deep neural networks, we propose GUMP-Net, an interpretable model-data-driven intelligent algorithm for multi-class pelvic segmentation, in which three network modules are designed to constitute the overall segmentation framework together: the object detection module for automatic level set initialization, the edge detector module for learning an anatomy-aware edge detector function and the iteration module for deep level set evolution. Leveraging the advantages of level set representation and deep learning, GUMP-Net shows more accurate, robust and consistent segmentation performance, especially in small training data situation, compared to the state-of-the-art methods. Extensive experiments on pelvic datasets demonstrate the rationality and effectiveness of the proposed algorithm. Further experiments extended to ankle dataset indicate broader applications to other anatomies. The proposed algorithm not only provides an efficient segmentation method for complex fracture reduction, but also gives an interpretable geometric perspective for understanding deep learning segmentation.

### 🤖 AI 总结

**一句话总结**：Pelvic segmentation is one of the most important and fundamental research problems in precise and intelligent diagnosis and treatment, as well as surgical planning and navigation for pelvic fractures....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, GUMP-Net, interpretable, model-data-driven, intelligent, algorithm, multi-class, pelvic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19215v1) | [下载PDF](https://arxiv.org/pdf/2606.19215v1.pdf)

---

## [17. ROSA-TFormer: A Radar-Optical Sensor-Aware Temporal Transformer for Pinus sylvestris Plantation Classification in Northern Shaanxi Using GEE-Derived Sentinel-1/2 Time Series](https://arxiv.org/abs/2606.19204v1)

**作者**：Nengbo Zhang, Chang sheng  
**分类**：cs.CV  
**发布时间**：2026-06-17

### 📄 论文摘要

Accurate identification of Pinus sylvestris var. mongolica plantations is important for monitoring afforestation quality and ecological restoration in northern Shaanxi. This paper proposes ROSA-TFormer, a radar-optical sensor-aware temporal Transformer for P. sylvestris classification using Sentinel-1/2 time-series data generated on Google Earth Engine. The model integrates separate SAR and optical embedding branches, a sensor-aware gate, and temporal attention pooling to capture multi-source seasonal features. Experiments on monthly and half-month point-level datasets show that ROSA-TFormer achieves strong classification performance, with 99.67% overall accuracy, 99.56% macro F1, and 98.91% P. sylvestris F1 on the HalfMonth-dataBig dataset. Spatial block validation and ablation results further indicate the effectiveness of radar-optical temporal fusion and sensor-aware modeling. The results demonstrate the potential of ROSA-TFormer for point-level P. sylvestris plantation classification, while broader wall-to-wall validation remains necessary.

### 🤖 AI 总结

**一句话总结**：Accurate identification of Pinus sylvestris var. mongolica plantations is important for monitoring afforestation quality and ecological restoration in northern Shaanxi. This paper proposes ROSA-TForme...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ROSA-TFormer, Radar-Optical, Sensor-Aware, Temporal, Transformer, Pinus, sylvestris, Plantation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19204v1) | [下载PDF](https://arxiv.org/pdf/2606.19204v1.pdf)

---

## [18. Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance](https://arxiv.org/abs/2606.19195v1)

**作者**：Kangsheng Duan, Ziyang Xu, Wenyu Liu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-17

### 📄 论文摘要

While 10B-level industrial foundation models have pushed the boundaries of image inpainting, their prohibitive computational costs severely hinder practical deployment. Constructing a highly optimized task-specific specialist offers a promising solution; however, extreme structural compression inevitably triggers a severe representation bottleneck. To conquer this, we propose Moebius, a highly efficient lightweight inpainting framework. We systematically reconstruct the diffusion backbone by introducing the Local-$λ$ Mix Interaction ($LλMI$) block. Comprising Local-$λ$ and Interactive-$λ$ modules, it elegantly summarizes spatial contexts and global semantic priors into fixed-size linear matrices, preserving complex latent interactions while drastically shedding parameters. Furthermore, to unlock the full representational capacity of this highly compact architecture, we synergistically pair it with an adaptive multi-granularity distillation strategy. Operating strictly within the latent space to avoid expensive pixel-space decoding, this strategy dynamically balances multiple gradient-based losses to achieve high-fidelity alignment. Extensive experiments across natural and portrait benchmarks demonstrate that this optimal synergy enables Moebius to rival or even surpass the generation quality of the 10B-level industrial generalist FLUX.1-Fill-Dev. Remarkably, Moebius achieves this using less than 2\% of the parameters (0.22B vs. 11.9B) while delivering a $>15\times$ acceleration in total inference time, setting a new efficiency standard for high-fidelity inpainting. Project page at https://hustvl.github.io/Moebius.

### 🤖 AI 总结

**一句话总结**：While 10B-level industrial foundation models have pushed the boundaries of image inpainting, their prohibitive computational costs severely hinder practical deployment. Constructing a highly optimized...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：0.2B, Moebius, Lightweight, Image, Inpainting, Framework, 10B-Level, Performance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19195v1) | [下载PDF](https://arxiv.org/pdf/2606.19195v1.pdf)

---

## [19. When AUC Misleads: Polarization-Aware Evaluation of Deepfake Detectors under Domain Shift](https://arxiv.org/abs/2606.19184v1)

**作者**：Dat Nguyen, Cosmin Radoi, Romain Hermary 等 7 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-06-17

### 📄 论文摘要

Recent advances in generative AI, such as diffusion models and face-swapping tools, have enabled the creation of highly realistic deepfakes, leading to real-world harms including financial fraud and non-consensual explicit content. In response, deepfake detection has become an active research area, with recent methods increasingly focusing on improving generalization to unseen manipulations. This is typically evaluated using the Area Under the ROC Curve (AUC) measured separately across multiple datasets. However, such an evaluation fails to reflect real-world scenarios where detectors face a mixture of data sources and varying artifact types. To address this limitation, we introduce a novel metric, Cross-dataset AUC (Cross-AUC) that averages per-domain AUCs with a measure of prediction polarization for taking into account the robustness to domain shift. The polarization extent is quantified by the Wasserstein Distance between class score distributions. Cross-AUC not only assesses the generalization capabilities of deepfake detectors under domain shifts more realistically, but it is also interpretable as it better explains the reason behind a drop in performance. Experiments performed on seven benchmark datasets demonstrate its practical relevance.

### 🤖 AI 总结

**一句话总结**：Recent advances in generative AI, such as diffusion models and face-swapping tools, have enabled the creation of highly realistic deepfakes, leading to real-world harms including financial fraud and n...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, When, AUC, Misleads, Polarization-Aware, Evaluation, Deepfake, Detectors

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19184v1) | [下载PDF](https://arxiv.org/pdf/2606.19184v1.pdf)

---

## cs.LG

## [20. UBP2: Uncertainty-Balanced Preference Planning for Efficient Preference-based Reinforcement Learning](https://arxiv.org/abs/2606.19328v1)

**作者**：Mohamed Nabail, Leo Cheng, Jingmin Wang 等 4 位作者  
**分类**：cs.LG, cs.AI, cs.RO  
**发布时间**：2026-06-17

### 📄 论文摘要

Preference-based RL provides an approach to learning reward models from pairwise comparisons of behaviors, bypassing the need for explicit reward design. However, existing methods typically rely on passive data collection and suffer from poor sample efficiency, especially during the early stages of learning. We introduce a model-based approach that actively directs exploration by jointly reasoning over uncertainties in the reward, dynamics, and value functions. Our method, Uncertainty-Balanced Preference Planning (UBP2), uses ensembles of reward, dynamics, and value function models to evaluate candidate trajectories according to a unified score that combines expected reward, terminal value, and epistemic uncertainty. Planning under this objective yields an explicit tradeoff between exploitation and information acquisition without requiring ad hoc exploration heuristics. Under standard regularity assumptions, we establish sublinear regret guarantees for both finite-horizon and infinite-horizon settings. Empirically, experiments on the Meta-World benchmark show UBP2 achieves substantially higher sample efficiency than model-free preference-based methods and non-optimistic model-based baselines.

### 🤖 AI 总结

**一句话总结**：Preference-based RL provides an approach to learning reward models from pairwise comparisons of behaviors, bypassing the need for explicit reward design. However, existing methods typically rely on pa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UBP2, Uncertainty-Balanced, Preference, Planning, Efficient, Preference-based, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19328v1) | [下载PDF](https://arxiv.org/pdf/2606.19328v1.pdf)

---

## [21. Explaining Attention with Program Synthesis](https://arxiv.org/abs/2606.19317v1)

**作者**：Amiri Hayes, Belinda Li, Jacob Andreas  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-17

### 📄 论文摘要

A longstanding goal of research on interpretable deep learning is to replace opaque neural computations with human-meaningful symbolic descriptions. In this paper, we propose an approach for approximating the behavior of components of deep networks with executable programs. We focus on attention heads in transformer language models. For a given head, we first compute its associated attention matrices on a collection of randomly selected training examples. Next, we prompt a pre-trained language model with a summary of these matrices, and instruct it to generate a set of Python programs that can reproduce the associated attention patterns given only text from the input sentence. Finally, we re-rank programs according to how well our final set of programs predict behavior on held-out inputs. We demonstrate that a set of fewer than 1,000 such generated programs can reproduce the attention patterns of heads in GPT-2, TinyLlama-1.1B, and Llama-3B, achieving an average Intersection-over-Union similarity above 75% on TinyStories. Moreover, the best-fit programs can replace neural attention heads without substantially affecting model behavior: replacing 25% of attention heads with programmatic surrogates across the three models incurs only a 16% average perplexity increase, while maintaining performance on a variety of downstream question answering benchmarks. This work contributes a scalable pipeline for reverse-engineering attention heads in transformer models using human-readable, executable code, advancing a path toward symbolic transparency in neural models.

### 🤖 AI 总结

**一句话总结**：A longstanding goal of research on interpretable deep learning is to replace opaque neural computations with human-meaningful symbolic descriptions. In this paper, we propose an approach for approxima...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Explaining, Attention, Program, Synthesis, longstanding, goal, research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19317v1) | [下载PDF](https://arxiv.org/pdf/2606.19317v1.pdf)

---

## [22. P-K-GCN: Physics-augmented Koopman-enhanced Graph Convolutional Network for Deep Spatiotemporal Super-resolution](https://arxiv.org/abs/2606.19303v1)

**作者**：Xizhuo, Zhang, Zekai Wang 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-17

### 📄 论文摘要

High-fidelity simulation of spatiotemporal dynamics is computationally prohibitive, necessitating efficient super-resolution techniques to reconstruct high-resolution data from coarse-grained inputs. Traditional data-driven methods often lack physical constraints, and simple physics-informed learning struggles with irregular spatial geometries and intricately evolving temporal dynamics. To tackle these challenges, we propose a Physics-augmented Koopman-enhanced Graph Convolutional Network (P-K-GCN) for spatiotemporal super-resolution on irregular geometries. Specifically, a continuous spline-based GCN is first designed to extract spatial dependencies directly from coarse graph, and Koopman operator theory is incorporated to project the nonlinear dynamics into a compact latent space where temporal progression is linearized. Second, we augment the optimization objective with a physics-based loss to force the data-driven reconstructions to adhere to physical laws for improving predictive fidelity and robustness. Finally, we provide a rigorous theoretical analysis, establishing that the physics augmentation and Koopman regularization mathematically guarantees a reduction in super-resolution error by diminishing Rademacher complexity and tightening generalization bounds. We evaluate our framework on reconstructing spatially high-resolution cardiac electrodynamics across a 3D heart geometry from sparse low-resolution measurements. Numerical experiments demonstrate that our method achieves superior accuracy compared to baseline models.

### 🤖 AI 总结

**一句话总结**：High-fidelity simulation of spatiotemporal dynamics is computationally prohibitive, necessitating efficient super-resolution techniques to reconstruct high-resolution data from coarse-grained inputs. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：P-K-GCN, Physics-augmented, Koopman-enhanced, Graph, Convolutional, Network, Deep, Spatiotemporal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19303v1) | [下载PDF](https://arxiv.org/pdf/2606.19303v1.pdf)

---

## [23. Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models](https://arxiv.org/abs/2606.19297v1)

**作者**：Nikita Kachaev, Andrey Moskalenko, Matvey Skripkin 等 13 位作者  
**分类**：cs.LG, cs.RO  
**发布时间**：2026-06-17

### 📄 论文摘要

Embodied Vision-Language-Action (VLA) models are typically obtained by fine-tuning powerful pretrained VLMs on robotics data, yet it is unclear how much commonsense and factual knowledge they retain after adaptation. Failures on knowledge-sensitive tasks are ambiguous, conflating missing knowledge with poor generalization of low-level control. We introduce Act2Answer, a lightweight protocol that adapts VLM knowledge benchmarks to VLA evaluation by requiring agents to answer through action. Each question becomes a short tabletop episode where the agent performs a single object-placement action to select among candidate answers, yielding an action-grounded success rate with reduced control confounds. We curate a test suite of such environments across diverse commonsense and world-knowledge categories and introduce layerwise intent probing to localize answer-relevant information across the VLM backbone and action head. In a large-scale study of 7 VLA models and 9 VLM baselines, we systematically rank models across categories, finding that VLAs show solid performance on simple concepts while exhibiting larger gaps on richer semantic categories relative to their source VLMs, that VQA co-training is associated with better knowledge retention, and that answer-relevant signals peak in middle VLA layers but attenuate in upper layers. Act2Answer is available at https://tttonyalpha.github.io/act2answer/.

### 🤖 AI 总结

**一句话总结**：Embodied Vision-Language-Action (VLA) models are typically obtained by fine-tuning powerful pretrained VLMs on robotics data, yet it is unclear how much commonsense and factual knowledge they retain a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Does, VLA, Even, Know, Basics?, Measuring, Commonsense, World

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19297v1) | [下载PDF](https://arxiv.org/pdf/2606.19297v1.pdf)

---

## [24. Risk Stratification for ICU Delirium using Pervasive Ambient Sensing Information](https://arxiv.org/abs/2606.19292v1)

**作者**：Jiaqing Zhang, Sabyasachi Bandyopadhyay, Miguel Contreras 等 11 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-17

### 📄 论文摘要

Delirium is a common and serious complication in the Intensive Care Unit (ICU), associated with increased morbidity, prolonged hospital stays, and higher healthcare costs. Despite its prevalence, early prediction and prevention remain challenging. Environmental factors such as ambient sound and light may influence the onset of delirium, yet they are often overlooked in risk assessments. In this study, we examined whether light intensity and sound pressure levels can independently predict delirium across multiple prediction horizons. We evaluated four efficient sequential neural network models on data collected from 9 ICUs across 309 patients to predict delirium for 10 prediction-window sizes. We reported feature importance and direction of influence using Shapley Additive Explanations analysis. The convolutional model achieved the strongest discrimination, with AUC = 0.80 on sound data and on combined data. Sound features were the dominant predictors overall. Integrating sound with light improved short-term ($<1$ week) prediction, with the combined model assigning the highest risk immediately after the sensing period. These findings suggest that passive ambient sensing, especially sound, can add a clinically meaningful, interpretable signal for delirium risk estimation and offer a practical pathway to enrich multimodal ICU prediction and prevention strategies.

### 🤖 AI 总结

**一句话总结**：Delirium is a common and serious complication in the Intensive Care Unit (ICU), associated with increased morbidity, prolonged hospital stays, and higher healthcare costs. Despite its prevalence, earl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Risk, Stratification, ICU, Delirium, Pervasive, Ambient, Sensing, Information

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19292v1) | [下载PDF](https://arxiv.org/pdf/2606.19292v1.pdf)

---

## [25. Detecting Hidden ML Training With Zero-Overhead Telemetry](https://arxiv.org/abs/2606.19262v1)

**作者**：Robi Rahman, Sabiha Tajdari  
**分类**：cs.LG  
**发布时间**：2026-06-17

### 📄 论文摘要

Hardware-enabled monitoring of GPU workloads underpins many proposals for AI compute governance, but if developers can defeat monitoring mechanisms, such schemes are unworkable. We evaluate the adversarial robustness of GPU workload classification using only zero-overhead, privacy-preserving NVML telemetry: content-agnostic signals that observe physical effects of computation without accessing model weights, training data, or hyperparameters. Across 5 rounds of monitor-evader iteration, we evaluate 20 evasion strategy families on 9 GPU models spanning 4 architecture generations. We develop a classifier that achieves 98.2% binary accuracy at identifying training workloads across the whole corpus, and 43-87% accuracy against the most challenging unexpected workloads even when they are adversarially disguised.

### 🤖 AI 总结

**一句话总结**：Hardware-enabled monitoring of GPU workloads underpins many proposals for AI compute governance, but if developers can defeat monitoring mechanisms, such schemes are unworkable. We evaluate the advers...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ML, Detecting, Hidden, Training, Zero-Overhead, Telemetry, Hardware-enabled, monitoring

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19262v1) | [下载PDF](https://arxiv.org/pdf/2606.19262v1.pdf)

---

## [26. SCAN: Enhance Time Series Anomaly Detection via Multi-Scale Neighborhood-Centered Clustering](https://arxiv.org/abs/2606.19255v1)

**作者**：Xingze Zheng, Hanyin Cheng, Siyuan Wang 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-17

### 📄 论文摘要

Time series anomaly detection plays a crucial role in a wide range of real-world applications. Reconstruction-based methods have become the mainstream paradigm, but they suffer from over-generalization and under-generalization problems, which are challenging to balance. To address this, we introduce multi-scale clustering to enhance reconstruction-based methods. At the representation level, we integrate the cluster center representations of normal patterns to constrain the model to target representative normal patterns for reconstruction, preventing dominance of powerful capacity and representation capability. At the anomaly criterion level, we derive anomaly confidence score based on cluster membership probability and combine it with reconstruction error, providing dual criteria for detection. Furthermore, the effectiveness of the cluster center representations and anomaly confidence score depends on the clustering performance. Accordingly, we extract neighborhood-centered representations for multi-view clustering to improve clustering performance. Extensive experiments on multiple real-world datasets from diverse application domains demonstrate the state-of-the-art performance of SCAN.

### 🤖 AI 总结

**一句话总结**：Time series anomaly detection plays a crucial role in a wide range of real-world applications. Reconstruction-based methods have become the mainstream paradigm, but they suffer from over-generalizatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SCAN, Enhance, Time, Series, Anomaly, Detection, via, Multi-Scale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19255v1) | [下载PDF](https://arxiv.org/pdf/2606.19255v1.pdf)

---

## [27. A Human-in-the-Loop Bayesian Optimization Framework for Constraint-Aware Bioprocess Development](https://arxiv.org/abs/2606.19230v1)

**作者**：Samuel Stricker, Claus Wirnsperger, Alessandro Butté 等 7 位作者  
**分类**：cs.LG, cs.HC, stat.ML  
**发布时间**：2026-06-17

### 📄 论文摘要

This work presents an extension to Pareto Front Guided Sampling (PFGS), a Human-in-the-Loop (HitL) Bayesian Optimization (BO) framework in which Gaussian process (GP) surrogate-derived quantities are reformulated as objectives of a multi-objective optimization problem, and the resulting Pareto front is exposed to a domain expert for interactive candidate selection rather than returning a single automated recommendation. The framework is extended in two directions: constrained optimization is addressed by incorporating the posterior probability of satisfying output specification limits as an explicit Pareto objective, computed analytically from the GP posterior distribution; robust optimization is addressed by a Monte Carlo sampling strategy that estimates expected lower-confidence performance over a user-defined variability of input perturbations, capturing performance degradation under likely implementation deviations. The resulting multi-dimensional Pareto representation renders trade-offs between predicted performance, model uncertainty, probabilistic constraint satisfaction, and input robustness simultaneously visible through pairwise two-dimensional projections on an interactive dashboard, enabling selection criteria to be iteratively refined as the surrogate model improves and development objectives evolve. The framework is showcased on an eight-dimensional fed-batch Chinese Hamster Ovary (CHO) cell culture simulator demonstrating systematic identification of high-performing, feasibility-compliant, and perturbation-resilient operating conditions, and illustrating how expert-defined requirements provide a principled stopping criterion and support informed allocation of experimental resources.

### 🤖 AI 总结

**一句话总结**：This work presents an extension to Pareto Front Guided Sampling (PFGS), a Human-in-the-Loop (HitL) Bayesian Optimization (BO) framework in which Gaussian process (GP) surrogate-derived quantities are ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Human-in-the-Loop, Bayesian, Optimization, Framework, Constraint-Aware, Bioprocess, Development, work

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19230v1) | [下载PDF](https://arxiv.org/pdf/2606.19230v1.pdf)

---

## [28. Machine Unlearning for the XGBoost Model with Network Intrusion Datasets](https://arxiv.org/abs/2606.19220v1)

**作者**：Diana Magalhães, Eva Maia, João Vitorino 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-17

### 📄 论文摘要

Machine Unlearning (MU) has emerged as an important technique for removing specific data points from trained models without requiring full retraining. However, most existing MU research focuses on deep learning and image data, leaving a gap in the domain of network intrusion detection, which relies heavily on tabular data. This work introduces XGBoost-Forget, an unlearning approach for the XGBoost model, to address this gap. The approach is evaluated on two tabular Network Intrusion (NI) datasets, IoT-23 and GeNIS, using multiple metrics to assess model performance, unlearning efficiency, and forgetting quality. The results show that XGBoost-Forget maintains predictive performance close to the original model while providing significantly faster unlearning, demonstrating its potential for MU in tabular NI settings.

### 🤖 AI 总结

**一句话总结**：Machine Unlearning (MU) has emerged as an important technique for removing specific data points from trained models without requiring full retraining. However, most existing MU research focuses on dee...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MU, Machine, Unlearning, XGBoost, Model, Network, Intrusion, Datasets

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19220v1) | [下载PDF](https://arxiv.org/pdf/2606.19220v1.pdf)

---

## [29. Forecasting what Matters: Decision-Focused RL for Controlled EV Charging with Unknown Departure Times](https://arxiv.org/abs/2606.19199v1)

**作者**：Giuseppe Gabriele, Fabio Pavirani, Seyed Soroush Karimi Madahi 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-17

### 📄 论文摘要

The recent growth of EV adoption poses challenges for power systems, including increased peak demand and potential grid instability. Smart control of EV charging -- e.g., based on reinforcement learning (RL) -- can alleviate these issues by learning temporal and contextual patterns from historical data. Yet, in real-world scenarios, key features, such as departure time, often are unavailable. This, in turn, makes it harder for an RL agent to learn and execute an effective charging policy. To mitigate this uncertainty, a trained forecaster can approximate the unknown features from available data. However, since these forecasting models are typically trained for accuracy (rather than their impact on a downstream agent's decision quality), their errors may propagate and hinder the overall performance of a controller that is using the forecasts. To avoid this, we propose a decision-focused RL (DF-RL) framework in which the forecaster is trained end-to-end, i.e., with feedback from the charging policy actions taken by the RL agent. Such joint training of both the forecaster and controller ultimately results in higher-quality actions: our proposed DF-RL method yields superior charging decisions compared to other baselines, achieving up to a 14% improvement in total reward and a 55% reduction of unsupplied energy (i.e., charging that failed to happen because the EV already left), relative to the RL method without departure time forecasting.

### 🤖 AI 总结

**一句话总结**：The recent growth of EV adoption poses challenges for power systems, including increased peak demand and potential grid instability. Smart control of EV charging -- e.g., based on reinforcement learni...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, EV, Forecasting, what, Matters, Decision-Focused, Controlled, Charging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19199v1) | [下载PDF](https://arxiv.org/pdf/2606.19199v1.pdf)

---

## [30. AGDN: Learning to Solve Traveling Salesman Problem with Anisotropic Graph Diffusion Network](https://arxiv.org/abs/2606.19185v1)

**作者**：Bolin Shen, Ziwei Huang, Zhiguang Cao 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-17

### 📄 论文摘要

The Traveling Salesman Problem (TSP) is a cornerstone of combinatorial optimization and arises in many practical scenarios. Although graph-based learning approaches have been explored for TSP, the question of how to exploit graph structure more effectively remains open. We present the Anisotropic Graph Diffusion Network (AGDN), a new Graph Neural Network framework designed to solve TSP. Our method tackles two central difficulties: (1) the lack of informative topological prior in fully connected TSP graphs, and (2) losing connected nodes in the optimal solution after the commonly used graph sparsification techniques. To overcome these issues, we construct a MixScore transition matrix that merges node similarity with pairwise distance, and we develop an anisotropic graph diffusion strategy that supports efficient information exchange across multiple hops. Comprehensive experiments spanning diverse instance sizes and node distributions show that AGDN consistently outperforms existing methods while keeping computation time competitive. Furthermore, AGDN generalizes well to problem sizes and distributions beyond those seen during training. The implementation is publicly available at: https://github.com/LabRAI/AGDN.

### 🤖 AI 总结

**一句话总结**：The Traveling Salesman Problem (TSP) is a cornerstone of combinatorial optimization and arises in many practical scenarios. Although graph-based learning approaches have been explored for TSP, the que...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AGDN, Learning, Solve, Traveling, Salesman, Problem, Anisotropic, Graph

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.19185v1) | [下载PDF](https://arxiv.org/pdf/2606.19185v1.pdf)

---

