# arXiv AI 论文日报 | 2026-05-29

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.AI](#csAI) (5 篇)
- [cs.CV](#csCV) (14 篇)
- [cs.CL](#csCL) (4 篇)
- [cs.LG](#csLG) (7 篇)

---

## cs.AI

## [1. Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software](https://arxiv.org/abs/2605.30353v1)

**作者**：Nhat-Minh Nguyen  
**分类**：cs.AI, astro-ph.CO, cs.HC, cs.SE  
**发布时间**：2026-05-28

### 📄 论文摘要

Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level.   The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology.   The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]

### 🤖 AI 总结

**一句话总结**：Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Physics, All, Need?, Case, Study, Physicist-Supervised, Development

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30353v1) | [下载PDF](https://arxiv.org/pdf/2605.30353v1.pdf)

---

## [2. SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations](https://arxiv.org/abs/2605.30345v1)

**作者**：Qinpei Luo, Ruichun Ma, Xinyu Zhang 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-05-28

### 📄 论文摘要

Printed circuit board (PCB) schematic design defines nearly all electronic hardware, but it remains manual and expertise-intensive. While generative AI has advanced digital and analog IC design, PCB schematic generation from natural-language intent is largely unexplored. This paper presents SchGen, the first large language model that generates editable PCB schematics from natural-language requests. The key challenge lies in the lack of an LLM-suited representation and a large-scale dataset. Current schematic formats are dominated by verbose, tool-specific syntax and geometry-heavy descriptions, making them difficult to generate reliably. We introduce a semantically grounded code representation that encodes schematic editing primitives with relative placement and pin-name-based wiring, transforming a geometry-driven generation problem into a semantics-driven matching task amenable to LLMs. We further construct a large-scale dataset of PCB schematics paired with user prompts via a human-agent collaborative pipeline that converts open-source hardware designs into our representation. Experiments show that SchGen significantly outperforms alternative representations and even larger general-purpose LLMs on wire connectivity accuracy and functional correctness. Our results highlight the critical role of representation design in enabling generative models for complex hardware design tasks.

### 🤖 AI 总结

**一句话总结**：Printed circuit board (PCB) schematic design defines nearly all electronic hardware, but it remains manual and expertise-intensive. While generative AI has advanced digital and analog IC design, PCB s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SchGen, PCB, Schematic, Generation, Semantic-Grounded, Code, Representations, Printed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30345v1) | [下载PDF](https://arxiv.org/pdf/2605.30345v1.pdf)

---

## [3. Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection](https://arxiv.org/abs/2605.30344v1)

**作者**：Xiaona Zhou, Muntasir Wahed, Tianjiao Yu 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-28

### 📄 论文摘要

Recent advances in Vision-Language Models (VLMs) have achieved impressive performance across many tasks, yet prior studies report unsatisfactory performance when applying large language or multimodal models to finding abnormal patterns in sequential data. Public anomaly detection benchmarks typically provide interval annotations but not natural-language rationales, making it difficult to fine-tune VLMs to produce grounded, interpretable decisions. To address this gap, we construct VisAnomBench, a curated benchmark built from public time-series datasets and augmented with high-quality anomaly explanations selected from multiple large VLMs using fine-grained, task-specific rewards. Through fine-tuning on this benchmark, we develop VisAnomReasoner, a parameter-efficient VLM for time-series anomaly detection. Experimental results on VisAnomBench show that VisAnomReasoner achieves more accurate anomaly localization and consistently outperforms all baselines, with improvements of at least 21.23 and 23.87 percentage points in precision and F1, respectively. Additional experiments on the TSB-AD-U benchmark demonstrate strong cross-benchmark generalization, with VisAnomReasoner improving precision and F1 by 9.57 and 13.39 percentage points, respectively.

### 🤖 AI 总结

**一句话总结**：Recent advances in Vision-Language Models (VLMs) have achieved impressive performance across many tasks, yet prior studies report unsatisfactory performance when applying large language or multimodal ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Tiny, but, Trusted, Efficient, Vision-Language, Reasoning, Time-Series, Anomaly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30344v1) | [下载PDF](https://arxiv.org/pdf/2605.30344v1.pdf)

---

## [4. Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents](https://arxiv.org/abs/2605.30335v1)

**作者**：Anany Kotawala  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-05-28

### 📄 论文摘要

Multi-component LLM agents assemble probabilistic claims from components that each see only part of a joint problem; the composition can violate basic probability axioms even when every component is locally coherent. We formalise this locally coherent, globally incoherent failure via the compositional residual eps*, the L2 distance from the composed quote to the joint coherent polytope, computable at runtime from system output and the declared cross-component coupling constraints. A product-structure dichotomy characterises when local coherence suffices, and a Rayleigh-quotient prediction matches the observed residual within 7% on three of four relation classes. A hierarchical Boyle-Dykstra projection repairs the composition deterministically; an anytime-valid e-process gives sequential coherence monitoring. Across 1,876 ensemble cliques on a four-LLM mid-tier panel (frontier-panel rerun in Section 5.5), eps* > 0 on 33-94% of cliques, translating to +0.115 nats per bet of regret on 1,770 resolved bets under the proportional allocation rule (the gain collapses to +0.006 under bettors that themselves coherentise). Three intuitive LLM-side mitigations(retrieval, partition-aware prompting, aggregator-LLM) each fail or regress.

### 🤖 AI 总结

**一句话总结**：Multi-component LLM agents assemble probabilistic claims from components that each see only part of a joint problem; the composition can violate basic probability axioms even when every component is l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Locally, Coherent, Globally, Incoherent, Bounding, Compositional, Incoherence, Multi-Component

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30335v1) | [下载PDF](https://arxiv.org/pdf/2605.30335v1.pdf)

---

## [5. Demystifying Data Organization for Enhanced LLM Training](https://arxiv.org/abs/2605.30334v1)

**作者**：Yalun Dai, Yangyu Huang, Tongshen Yang 等 11 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-05-28

### 📄 论文摘要

Large Language Models (LLMs) have revolutionized various fields, yet their training efficiency is heavily reliant on effective data curation. While data selection has been widely studied, the strategic data organization for enhanced training remains an underexplored area, particularly since current LLMs are often trained for only one or a few epochs. This paper systematically explores the influence of data organization on LLM training by reusing pre-computed sample-level scores originally generated for data efficiency, thereby incurring minimal additional computational overhead. We identify and formalize four key guidelines for optimizing data organization: Boundary Sharpening, Cyclic Scheduling, Curriculum Continuity, and Local Diversity. Guided by them, we introduce two novel data ordering methods termed STR and SAW. Extensive experiments across different model scales and data sizes, encompassing both pre-training and SFT stages, validate the effectiveness of our summarized guidelines. They also demonstrate the robustness of our proposed data ordering methods in enhancing the stability and performance of LLM training. Github Link: https://github.com/microsoft/data-efficacy/

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) have revolutionized various fields, yet their training efficiency is heavily reliant on effective data curation. While data selection has been widely studied, the strategi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Demystifying, Data, Organization, Enhanced, Training, Large, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30334v1) | [下载PDF](https://arxiv.org/pdf/2605.30334v1.pdf)

---

## cs.CL

## [6. LLMSurgeon: Diagnosing Data Mixture of Large Language Models](https://arxiv.org/abs/2605.30348v1)

**作者**：Yaxin Luo, Jiacheng Cui, Xiaohan Zhao 等 8 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-05-28

### 📄 论文摘要

The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.

### 🤖 AI 总结

**一句话总结**：The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLMSurgeon, Diagnosing, Data, Mixture, Large, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30348v1) | [下载PDF](https://arxiv.org/pdf/2605.30348v1.pdf)

---

## [7. COMPOSE: Composing Future Theorems from Citations and Formal Structure](https://arxiv.org/abs/2605.30333v1)

**作者**：David Busbib, Michael Werman  
**分类**：cs.CL  
**发布时间**：2026-05-28

### 📄 论文摘要

A plausible future mathematical claim must satisfy two constraints: it should follow the direction of prior work and respect the formal dependencies that constrain what can validly follow. Existing approaches typically model only one of these sources, producing claims that are either weakly grounded or insufficiently motivated. We introduce grounded future mathematical generation, where the goal is to generate a plausible future theorem-like claim for an anchor paper using two complementary sources of context: its scientific citation graph and aligned formal theorem dependency graph. To address this setting, we propose COMPOSE, a dual-graph framework that conditions a language model on both scientific citation context and formal theorem structure. To support this setting, we construct a dataset of 108K paired scientific-formal graph examples from arXiv and Mathlib, together with a benchmark of 47K future papers from 2024--2025. Experiments show that COMPOSE outperforms strong baselines on retrieval to real future papers and achieves the best overall performance under LLM-judge evaluation, producing more grounded and mathematically richer outputs. These results show that future mathematical generation benefits from combining scientific context with formal structure. Project page is available at https://david-busbib.github.io/COMPOSE-page/.

### 🤖 AI 总结

**一句话总结**：A plausible future mathematical claim must satisfy two constraints: it should follow the direction of prior work and respect the formal dependencies that constrain what can validly follow. Existing ap...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：COMPOSE, Composing, Future, Theorems, Citations, Formal, Structure, plausible

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30333v1) | [下载PDF](https://arxiv.org/pdf/2605.30333v1.pdf)

---

## [8. Resolution Diagnostics for Paired LLM Evaluation](https://arxiv.org/abs/2605.30315v1)

**作者**：Anany Kotawala  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-05-28

### 📄 论文摘要

Across two public LLM leaderboards, many displayed pairwise rankings do not meet a conventional paired-test resolution target under the actual paired evaluation design: 11 of 40 Open LLM Leaderboard v1 pairwise comparisons and 4 of 9 MMLU-Pro top-10 adjacent-rank pairs are unresolved at (alpha, 1-beta) = (0.05, 0.8). The MMLU-Pro count rises to 6/9 under real subject-level clustering and stays at 5-6 out of 9 in 99.9% of category-bootstrap resamples. We frame paired LLM evaluation as a hypothesis-testing problem, invert level-alpha, power-(1-beta) tests, and report a per-pair resolution ratio q = N/N* as the primary diagnostic. A sharp small-effect expansion with an explicit second-order constant shows that the widely-used unpaired Cohen-h-plus-(1-rho) shortcut deviates from the correct N* by approximately a factor of two in the close-comparison regime, a deficit that three of five off-the-shelf calculators(Cohen 1988, G*Power, R pwr) silently inherit when the user post-multiplies their per-arm output by (1-rho). The unresolved-pair pattern remains under multiplicity correction and anytime-valid sequential testing.

### 🤖 AI 总结

**一句话总结**：Across two public LLM leaderboards, many displayed pairwise rankings do not meet a conventional paired-test resolution target under the actual paired evaluation design: 11 of 40 Open LLM Leaderboard v...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Resolution, Diagnostics, Paired, Evaluation, Across, two, public

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30315v1) | [下载PDF](https://arxiv.org/pdf/2605.30315v1.pdf)

---

## [9. MedCase-Structured: A Text-to-FHIR Dataset for Benchmarking Diagnostic Reasoning in Clinically Realistic EHR Settings](https://arxiv.org/abs/2605.30295v1)

**作者**：Valentina Bui Muti, Eugénie Dulout, Ziquan Fu  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-05-28

### 📄 论文摘要

Large language models (LLMs) show promise for clinical reasoning and decision support, but evaluation in realistic, electronic health record-congruent settings remains limited. Existing benchmarks often rely on static datasets or unstructured inputs that do not reflect the structured, interoperable data formats used in clinical systems. We introduce a pipeline for generating clinically realistic HL7 FHIR R4 bundles from unstructured text, enabling controllable evaluation of clinical decision support systems. The pipeline combines staged LLM generation with terminology-grounded validation and repair to reduce hallucinated codes and enforce structural and semantic consistency. Applying this approach to MedCaseReasoning, we construct MedCase-Structured, a synthetic dataset aligned with clinician-authored diagnostic cases, achieving valid FHIR generation for 82.5% of cases. Evaluation on MedCase-Structured reveals consistently lower diagnostic accuracy for LLMs on structured FHIR inputs than with plain text, highlighting the importance of deployment-aligned benchmarking.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) show promise for clinical reasoning and decision support, but evaluation in realistic, electronic health record-congruent settings remains limited. Existing benchmarks oft...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MedCase-Structured, Text-to-FHIR, Dataset, Benchmarking, Diagnostic, Reasoning, Clinically, Realistic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30295v1) | [下载PDF](https://arxiv.org/pdf/2605.30295v1.pdf)

---

## cs.CV

## [10. GMOS: Grounding Moving Object Segmentation in 3D Space and Time](https://arxiv.org/abs/2605.30352v1)

**作者**：Junyu Xie, Tengda Han, Weidi Xie 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-28

### 📄 论文摘要

Moving Object Segmentation (MOS) aims to discover, segment, and track objects that move independently of the camera. Current MOS methods, however, exhibit two fundamental limitations: they rely on pre-computed 2D auxiliary modalities such as optical flow or point trajectories that lack 3D geometric information, and they treat motion as a sequence-level attribute, overlooking the instantaneous motion state of each object. We address both by grounding MOS in 3D space and time, and propose GMOS, a framework that operates directly on RGB video to produce 3D-aware, temporally fine-grained segmentation of multiple moving objects, alongside a foreground--background variant GMOS-S for faster deployment. To support training and evaluation in this regime, we curate GMOS-2K, a dataset of 2,210 real-world videos with per-object temporal motion annotations drawn from five established Video Object Segmentation (VOS) benchmarks, and formalise MOS-I ("I" for instantaneous), a temporally fine-grained evaluation protocol with three complementary metrics. GMOS achieves state-of-the-art results across MOS, MOS-I, and Unsupervised VOS benchmarks, while running significantly faster than prior multi-object MOS methods and supporting online inference for streaming deployment.

### 🤖 AI 总结

**一句话总结**：Moving Object Segmentation (MOS) aims to discover, segment, and track objects that move independently of the camera. Current MOS methods, however, exhibit two fundamental limitations: they rely on pre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, GMOS, Grounding, Moving, Object, Segmentation, Space, Time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30352v1) | [下载PDF](https://arxiv.org/pdf/2605.30352v1.pdf)

---

## [11. AdaState: Self-Evolving Anchors for Streaming Video Generation](https://arxiv.org/abs/2605.30349v1)

**作者**：Yusuf Dalva, Pinar Yanardag  
**分类**：cs.CV  
**发布时间**：2026-05-28

### 📄 论文摘要

Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.

### 🤖 AI 总结

**一句话总结**：Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, AdaState, Self-Evolving, Anchors, Streaming, Video, Generation, Autoregressive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30349v1) | [下载PDF](https://arxiv.org/pdf/2605.30349v1.pdf)

---

## [12. NeuROK: Generative 4D Neural Object Kinematics](https://arxiv.org/abs/2605.30347v1)

**作者**：Chen Geng, Guangzhao He, Yue Gao 等 6 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-05-28

### 📄 论文摘要

Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal deformations of static objects under various physical conditions -- remains challenging and often ad hoc, despite its importance in building comprehensive 3D world models. Most existing methods assume a predefined physical model and use system identification to estimate parameters, restricting these methods to specific categories and small-scale datasets. We propose that these restrictions can be overcome by learning a data-driven kinematic state parameterization for object-centric physical systems. Specifically, we learn both a latent space representing all possible states of the object and a decoder that maps any sampled latent to a plausibly deformed shape of the object. We refer to this parameterization as Neural Object Kinematics (NeuROK), and learn a transformer-based encoder-decoder model on a curated large-scale 4D dataset. This formulation and the learned model significantly simplify the generation of simulative dynamics since we only need to consider the dynamics within a low-dimensional latent space from the Lagrangian mechanics' perspective in classical physics. We demonstrate the effectiveness and generality of this neural simulation framework across diverse dynamic object types, showing clear advantages over prior works. Project page: https://chen-geng.com/neurok

### 🤖 AI 总结

**一句话总结**：Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, NeuROK, Generative, Neural, Object, Kinematics, Data-driven, approaches

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30347v1) | [下载PDF](https://arxiv.org/pdf/2605.30347v1.pdf)

---

## [13. YoCausal: How Far is Video Generation from World Model? A Causality Perspective](https://arxiv.org/abs/2605.30346v1)

**作者**：You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-28

### 📄 论文摘要

As video diffusion models (VDMs) advance toward world models, a key question arises: do they truly understand causality, or merely overfit to statistical temporal patterns? Existing benchmarks mostly rely on synthetic data, limiting real-world generalization due to the sim-to-real gap. We present YoCausal, a two-level benchmark inspired by the Violation of Expectation (VoE) paradigm from cognitive science. By temporally reversing real-world videos at zero cost as natural counterfactual samples, YoCausal establishes an arbitrarily extensible evaluation protocol. Level 1 introduces the Reverse Surprise Index (RSI), quantifying arrow-of-time perception via denoising loss. Level 2 introduces the Causality Cognition Index (CCI), which leverages a VLM to stratify datasets into causal and non-causal subsets, disentangling genuine causal reasoning from temporal bias. Evaluation of 13 state-of-the-art VDMs reveals that perceiving the arrow of time does not imply understanding causality, and a significant gap persists relative to human-level causal cognition.

### 🤖 AI 总结

**一句话总结**：As video diffusion models (VDMs) advance toward world models, a key question arises: do they truly understand causality, or merely overfit to statistical temporal patterns? Existing benchmarks mostly ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：YoCausal, How, Far, Video, Generation, World, Model?, Causality

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30346v1) | [下载PDF](https://arxiv.org/pdf/2605.30346v1.pdf)

---

## [14. Uncertainty-driven 3D Gaussian Splatting Active Mapping via Anisotropic Visibility Field](https://arxiv.org/abs/2605.30342v1)

**作者**：Shangjie Xue, Jesse Dill, Dhruv Ahuja 等 6 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-05-28

### 📄 论文摘要

We present Gaussian Splatting Anisotropic Visibility Field (GAVIS), a novel framework for uncertainty quantification and active mapping in 3DGS. Our key insight is that regions unseen from the training views yield unreliable predictions from the 3DGS. To address this, we introduce a principled and efficient method for quantifying the visibility field in 3DGS, defined as the anisotropic visibility of each particle with respect to the training views, and represented using spherical harmonics. The resulting visibility field is integrated into a Bayesian Network-based uncertainty-aware 3DGS rasterizer, enabling real-time (200 FPS) uncertainty quantification for synthesized views. Active mapping is further performed within a maximum information gain framework building on this formulation. Extensive experiments across diverse environments demonstrate that GAVIS consistently and significantly outperforms prior approaches in both accuracy and efficiency. Moreover, beyond standalone use, our method can be applied post-hoc to improve the performance of existing approaches.

### 🤖 AI 总结

**一句话总结**：We present Gaussian Splatting Anisotropic Visibility Field (GAVIS), a novel framework for uncertainty quantification and active mapping in 3DGS. Our key insight is that regions unseen from the trainin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Uncertainty-driven, Gaussian, Splatting, Active, Mapping, via, Anisotropic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30342v1) | [下载PDF](https://arxiv.org/pdf/2605.30342v1.pdf)

---

## [15. GPIC: A Giant Permissive Image Corpus for Visual Generation](https://arxiv.org/abs/2605.30341v1)

**作者**：Keshigeyan Chandrasegaran, Kyle Sargent, Suchir Agarwal 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-28

### 📄 论文摘要

Studying scalable methods for visual generative modeling requires large, accessible, and stable datasets. We introduce GPIC, a Giant Permissive Image Corpus of approximately 28 trillion pixels. GPIC comprises diverse internet images captioned by a state-of-the-art vision-language model, including 100M training, 200K validation, and 1M test examples. Moreover, all GPIC images are permissively licensed for both research and commercial use. GPIC is safety-filtered, deduplicated, and centrally hosted on Hugging Face. We provide a benchmarking protocol for generative modeling on GPIC. Finally, we provide a reference baseline for pixel-space flow matching on GPIC. Our dataset, benchmark, and models are available at https://huggingface.co/datasets/stanford-vision-lab/gpic. Evaluation toolkit and code are available at https://gpic.stanford.edu

### 🤖 AI 总结

**一句话总结**：Studying scalable methods for visual generative modeling requires large, accessible, and stable datasets. We introduce GPIC, a Giant Permissive Image Corpus of approximately 28 trillion pixels. GPIC c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GPIC, Giant, Permissive, Image, Corpus, Visual, Generation, Studying

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30341v1) | [下载PDF](https://arxiv.org/pdf/2605.30341v1.pdf)

---

## [16. Benchmarking Single-Factor Physical Video-to-Audio Generation](https://arxiv.org/abs/2605.30339v1)

**作者**：Tingle Li, Siddharth Gururani, Kevin J. Shih 等 9 位作者  
**分类**：cs.CV, cs.MM, cs.SD, eess.AS  
**发布时间**：2026-05-28

### 📄 论文摘要

Generative video-to-audio (V2A) models produce highly plausible soundtracks, but it remains unclear whether they capture the underlying physical processes. Existing evaluations emphasize perceptual realism and overlook physical correctness under controlled interventions. In this paper, we introduce FlatSounds, a benchmark that audits the physical reasoning of V2A models through: 1) controlled counterfactual pairs in which a single physical factor is varied, and 2) single-video pattern tests that probe internal consistency and directional trends. These settings test whether the generated audio correctly reflects specific physical properties and timings. Our evaluation of state-of-the-art models reveals a consistent trade-off: models rely more on text captions than the visual stream to infer physics and semantics. Captions generally improve physical and semantic accuracy, but paradoxically degrade temporal alignment. Our results highlight the need to move beyond audio quality toward learning physical processes directly from pixels. Finally, we find that our physics-based metrics correlate strongly with human preference tests on our own data. Project webpage: https://research.nvidia.com/labs/cosmos-lab/flatsounds/

### 🤖 AI 总结

**一句话总结**：Generative video-to-audio (V2A) models produce highly plausible soundtracks, but it remains unclear whether they capture the underlying physical processes. Existing evaluations emphasize perceptual re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：V2A, Benchmarking, Single-Factor, Physical, Video-to-Audio, Generation, Generative, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30339v1) | [下载PDF](https://arxiv.org/pdf/2605.30339v1.pdf)

---

## [17. REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image](https://arxiv.org/abs/2605.30338v1)

**作者**：Xiaoxuan Ma, Jiashun Wang, Nicolas Ugrinovic 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-28

### 📄 论文摘要

Reconstructing physically stable 3D scenes from a single RGB image enables casual images to be converted into simulation-ready digital assets for applications such as immersive interaction and content creation. However, existing single-image reconstruction methods fall short in capturing the physical structure of a scene. As a result, they often produce geometrically plausible but physically inconsistent results, including object floating and penetration, which lead to unstable behavior in physics simulations. Image-conditioned scene generation methods improve physical plausibility but often rely on strong scene priors, yielding plausible yet inaccurate object arrangements that fail to match the input image. We propose REST3D, a single-image reconstruction framework that can reconstruct physically stable 3D scenes by integrating physical scene understanding with physics-constrained refinement. We first introduce an agentic physical scene understanding technique that constructs a scene-tree representation capturing object physical states and inter-object relationships from a gravity-support perspective, providing a structural prior for reconstruction. Leveraging this structure, we initialize the scene using image-to-3D models, followed by scene-tree-guided alignment and physics-constrained optimization to resolve physical violations while preserving visual consistency with the input image. Experiments show that our method significantly reduces physical errors and improves simulation stability on both synthetic and real-world datasets while maintaining strong reconstruction quality. We further demonstrate the reconstructed scenes in VR-based human-object interaction, showing their potential for immersive applications.

### 🤖 AI 总结

**一句话总结**：Reconstructing physically stable 3D scenes from a single RGB image enables casual images to be converted into simulation-ready digital assets for applications such as immersive interaction and content...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, REST3D, Reconstructing, Physically, Stable, Scenes, Single, Image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30338v1) | [下载PDF](https://arxiv.org/pdf/2605.30338v1.pdf)

---

## [18. Colored Noise Diffusion Sampling](https://arxiv.org/abs/2605.30332v1)

**作者**：Hadar Davidson, Noam Issachar, Sagie Benaim  
**分类**：cs.CV  
**发布时间**：2026-05-28

### 📄 论文摘要

Diffusion models achieve state-of-the-art image synthesis, with their generative trajectories fundamentally exhibiting a spectral bias, resolving low-frequency global structures early and high-frequency fine details later. Conventional stochastic differential equation (SDE) solvers fail to account for this dynamic, naively injecting uniform white noise throughout the entire process and misusing the finite energy budget. In this work, we establish a mathematical framework that reconsiders SDE inference as a targeted, frequency-decoupled energy transfer. Leveraging this framework, we introduce Colored Noise Sampling (CNS), a novel, training-free stochastic solver. Rather than injecting uniform white noise, CNS utilizes a dynamic, timestep- and frequency-dependent schedule that more efficiently allocates injected energy toward structurally unresolved frequency bands. By actively exploiting the model's inherent spectral bias, CNS systematically steers the generated distribution toward the true data manifold. Extensive experiments demonstrate that CNS significantly outperforms standard ODE and SDE baselines as a strictly plug-and-play, inference-time sampler substitution across diverse architectures (SiT, JiT, FLUX). Compared to standard sampling on ImageNet-256, CNS achieves substantial unguided FID reductions, improving from 8.26 to 6.27 on SiT-XL/2, 32.39 to 26.69 on JiT-B/16, and 11.88 to 8.31 on JiT-H/16, while yielding consistent relative FID improvements with Classifier-Free Guidance. Project page is available at https://hadardavidson.github.io/CNS/.

### 🤖 AI 总结

**一句话总结**：Diffusion models achieve state-of-the-art image synthesis, with their generative trajectories fundamentally exhibiting a spectral bias, resolving low-frequency global structures early and high-frequen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Colored, Noise, Sampling, models, achieve, state-of-the-art, image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30332v1) | [下载PDF](https://arxiv.org/pdf/2605.30332v1.pdf)

---

## [19. Supercharging Thermal Gaussian Splatting with Depth Estimation](https://arxiv.org/abs/2605.30328v1)

**作者**：Manoj Biswanath, Chenxin Cai, Hannah Schieber 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-28

### 📄 论文摘要

Efficient and robust 3D scene representation is crucial in autonomous driving, robotics, and related fields. While RGB images provide valuable content for 3D reconstruction, other modalities like thermal or depth can enable additional information on the environment. Lately, novel view synthesis methods like 3D Gaussian Splatting have started using multiple modalities to further boost their performance. But fusing or combining multimodal data can make the process slower and can bring in additional challenges. Therefore, our project aims to use single modality based on thermal infrared domain, by removing the reliance on visible light as much as possible. This single modality can be expected to be faster as it does not rely on multimodal data. We propose a method, Thermal-to-Depth Gaussian Splatting (TDg), that uses only thermal images and depth estimation in its architecture to derive the radiance fields. Our TDg method outperforms the MSMG (Multiple Single-Modal Gaussians) baseline in most cases on our test datasets, RGBT-Scenes and ThermalMix. On average, the rendering quality metrics such as learned perceptual image patch similarity (LPIPS), structural similarity index measure (SSIM), and peak signal-to-noise ratio (PSNR) of TDg are 1.12%, 0.034%, and 0.01% better than the baseline MSMG values. It also reduces the training time significantly, by 12 mins 47 secs (55% improvement). Overall, our method is successful in deriving these thermal radiance fields, which can ultimately have several applications, such as identifying heat sources critical in surveillance, search or rescue operations, and industrial inspections where temperature is widely used to monitor machines.

### 🤖 AI 总结

**一句话总结**：Efficient and robust 3D scene representation is crucial in autonomous driving, robotics, and related fields. While RGB images provide valuable content for 3D reconstruction, other modalities like ther...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Supercharging, Thermal, Gaussian, Splatting, Depth, Estimation, Efficient, robust

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30328v1) | [下载PDF](https://arxiv.org/pdf/2605.30328v1.pdf)

---

## [20. Veda: Scalable Video Diffusion via Distilled Sparse Attention](https://arxiv.org/abs/2605.30325v1)

**作者**：Shihao Han, Hao Yang, Xinting Hu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-28

### 📄 论文摘要

Scaling Diffusion Transformers to generate high-resolution, long videos is constrained by the quadratic cost of self-attention, and existing sparse attention methods degrade under high sparsity. We show empirically that generation quality is determined not by the sparsity ratio itself, but by how well the sparse mask aligns with the tile-wise geometry of full attention. Based on this insight, we propose Veda, a distilled sparse attention framework that formulates tile selection as an explicit reconstruction problem from full attention. Veda integrates statistics-aware tile scoring with head-aware tiling to reduce estimation error and structural mismatch, enabling aggressive sparsity. A hardware-efficient tile-skipping kernel converts theoretical sparsity into practical wall-clock speedups. Experiments on large video diffusion models, including Waver and Wan2.1, demonstrate substantial acceleration with no noticeable degradation in generation quality. To generate 720P 10-second videos on Waver-T2V-12B, Veda achieves a 5.1$\times$ end-to-end speedup and a 10.5$\times$ self-attention speedup, reducing attention overhead from 92% to 50%. Notably, the gains increase with sequence length, indicating that Veda scales favorably with spatiotemporal resolution across models.

### 🤖 AI 总结

**一句话总结**：Scaling Diffusion Transformers to generate high-resolution, long videos is constrained by the quadratic cost of self-attention, and existing sparse attention methods degrade under high sparsity. We sh...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Veda, Scalable, Video, via, Distilled, Sparse, Attention

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30325v1) | [下载PDF](https://arxiv.org/pdf/2605.30325v1.pdf)

---

## [21. MonoPhysics: Estimating Geometry, Appearance, and Physical Parameters from Monocular Videos](https://arxiv.org/abs/2605.30320v1)

**作者**：Daniel Rho, Jun Myeong Choi, Matthew Thornton 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-28

### 📄 论文摘要

Existing inverse physics methods recover physical parameters from multi-view videos, where geometric constraints across views resolve scale and 3D structure. In monocular settings, however, such constraints are absent, leading to severe scale ambiguity, inaccurate geometry, and weak coupling between appearance optimization and physical simulation. We propose MonoPhysics, a framework for monocular inverse physics estimation of deformable objects using differentiable MPM simulation and 3D Gaussian Splatting, which jointly optimizes geometry, appearance, and physical parameters from a single camera view. We address these challenges through three visual-physical bridges: global scale alignment, physics-aware geometry refinement, and a differentiable position map, which together enable accurate optimization from monocular observations alone. We evaluate on Vid2Sim and our new dataset of elastic and plastic objects, showing that MonoPhysics outperforms existing baselines in monocular settings and achieves performance comparable to multi-view baselines using only a single camera. Our project page is available at https://daniel03c1.github.io/MonoPhysics/

### 🤖 AI 总结

**一句话总结**：Existing inverse physics methods recover physical parameters from multi-view videos, where geometric constraints across views resolve scale and 3D structure. In monocular settings, however, such const...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MonoPhysics, Estimating, Geometry, Appearance, Physical, Parameters, Monocular, Videos

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30320v1) | [下载PDF](https://arxiv.org/pdf/2605.30320v1.pdf)

---

## [22. VPG: Visual Prefix Guidance for Autoregressive Image and Video Generation](https://arxiv.org/abs/2605.30317v1)

**作者**：Xinyao Liao, Qiyuan He, Yicong Li 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-28

### 📄 论文摘要

Autoregressive image and video generators are trained with teacher-forced histories but must sample from their own generated prefixes at inference time, making them vulnerable to exposure bias and prefix drift. Existing remedies either modify training or apply sampling-time guidance aimed primarily at external semantic conditions, such as class labels or text prompts, rather than testing whether a next-step prediction provides strong posterior support for the generated prefix itself. We propose Visual Prefix Guidance (VPG), a training-free inference-time guidance method for autoregressive image and video generation. VPG improves next-step prediction by contrasting the model's output under the generated prefix with its output under a corrupted prefix, then extrapolating logits toward candidates that strengthen the posterior support of the generated prefix. Across class-conditional image generation with VAR, text-to-image generation with Infinity, and text-to-video generation with InfinityStar, VPG improves generation quality without retraining the base model, reducing FID on VAR by 0.36 on average and improving benchmark performance on both image and video generation.

### 🤖 AI 总结

**一句话总结**：Autoregressive image and video generators are trained with teacher-forced histories but must sample from their own generated prefixes at inference time, making them vulnerable to exposure bias and pre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VPG, Visual, Prefix, Guidance, Autoregressive, Image, Video, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30317v1) | [下载PDF](https://arxiv.org/pdf/2605.30317v1.pdf)

---

## [23. City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.30310v1)

**作者**：Sayan Paul, Sourav Ghosh, Siddharth Katageri 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-05-28

### 📄 论文摘要

City-scale 3D surface reconstruction from multiview images for downstream 3D simulation, poses highly challenging problems due to the scale and complexity of urban scenes. Existing city-scale 3D reconstruction methods based on NeRF, Gaussian Splatting etc. often fail to recover 3D meshes ready for simulation due to incomplete/missing geometry and irregular, noisy surfaces. Scaling existing small-scale 3D reconstruction methods to arbitrarily large urban scenes is highly infeasible due to their computational complexity. We present City-Mesh3R, a scalable framework for reconstructing watertight surface meshes directly from large unordered image collections. Unlike recent methods which use global sparse SfM point-cloud initialization followed by a distributed 3D dense reconstruction of large-scale scenes, our method follows an end-to-end images-to-mesh 3D reconstruction approach using a divide-and-conquer strategy. The sparse city map is reconstructed via topological image clustering, cluster-wise independent sparse SfM and map merging, without need for exhaustive image feature matching. Then this map is partitioned spatially to perform geometry-aware camera selection, followed by dense surface reconstruction and surface refinement using curvature-aware adaptive vertex density remeshing. These partition meshes are then stitched together to produce the global mesh of the city. The proposed end-to-end framework is evaluated on city-scale reconstruction datasets. As demonstrated by our qualitative and quantitative results, our proposed method yields high-fidelity watertight 3D meshes with regular geometry, capturing fine surface details, and is suitable for scaling to arbitrarily large scenes owing to the end-to-end processing in a distributed setting.

### 🤖 AI 总结

**一句话总结**：City-scale 3D surface reconstruction from multiview images for downstream 3D simulation, poses highly challenging problems due to the scale and complexity of urban scenes. Existing city-scale 3D recon...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, City-Mesh3R, Simulation-Ready, City-Scale, Mesh, Reconstruction, Multi-View, Images

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30310v1) | [下载PDF](https://arxiv.org/pdf/2605.30310v1.pdf)

---

## cs.LG

## [24. Fairness-Aware Federated Learning with Trajectory Shapley Value](https://arxiv.org/abs/2605.30336v1)

**作者**：Daniel Kuznetsov, Ziqi Wang  
**分类**：cs.LG  
**发布时间**：2026-05-28

### 📄 论文摘要

Federated learning is an emerging distributed paradigm that addresses the challenges posed by heterogeneous, privacy-sensitive data. It enables multiple clients to train a model collaboratively by aggregating their local updates at a server. However, conventional aggregation schemes typically use fixed weights that fail to reflect unequal and time-varying client contributions, leading to biased and unstable learning. To improve fairness and stability, we propose the Trajectory Shapley Value (TSV), a contribution metric that evaluates how each client influences the optimization trajectory of the global model using a validation-based, temporally consistent utility. Building on TSV, we design FedTSV, an adaptive aggregation method that converts per-round evaluations into dynamic client weights, allowing the server to respond to heterogeneous and adversarial participation in real time. Experiments on benchmark datasets show that FedTSV accelerates convergence, improves robustness, and yields more equitable contribution assessments, thereby providing a principled foundation for fairness-aware federated optimization.

### 🤖 AI 总结

**一句话总结**：Federated learning is an emerging distributed paradigm that addresses the challenges posed by heterogeneous, privacy-sensitive data. It enables multiple clients to train a model collaboratively by agg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Fairness-Aware, Federated, Learning, Trajectory, Shapley, Value, emerging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30336v1) | [下载PDF](https://arxiv.org/pdf/2605.30336v1.pdf)

---

## [25. When, why, and how do diffusion posterior samplers fail? A finite-sample lens](https://arxiv.org/abs/2605.30330v1)

**作者**：Benjamin A. Burns, Sara Fridovich-Keil  
**分类**：cs.LG  
**发布时间**：2026-05-28

### 📄 论文摘要

Diffusion models have excellent capacity to model complex distributions of natural data, which has made them a popular and effective choice for posterior sampling in imaging inverse problems. Existing methods can incorporate any measurement model at inference time but must use an inexact approximation for the likelihood at intermediate timesteps for computational tractability. Although these approximations can often work well empirically, their downstream effect on the sampled posterior is poorly understood and can result in unexplained failures. To understand when, why, and how these likelihood approximations propagate to erroneous posterior distributions, we introduce a finite-sample perspective on posterior sampling that approximates the posterior to arbitrary precision as training set size tends towards infinity, for any forward model and prior distribution. Using this finite-sample lens, we observe that popular posterior sampling approximations tend to under- or over-estimate the spread of the posterior at intermediate timesteps, causing downstream consequences including sensitivity to early stopping time, inaccurate relative weighting of posterior modes, and hallucination, both of prior modes that are not in the posterior and likelihood modes that are not supported by the prior. Moreover, we find that the cause of these posterior errors requires neither a nonlinear measurement model nor a multimodal posterior, but can arise solely due to a multimodal prior and inaccurate posterior spread at intermediate sampling times. Our finite-sample posterior sampling approach is agnostic to the type of likelihood approximation and the type of (linear or nonlinear) forward model, and can thus serve as a drop-in diagnostic to evaluate the accuracy and failure modes of existing and future posterior samplers.

### 🤖 AI 总结

**一句话总结**：Diffusion models have excellent capacity to model complex distributions of natural data, which has made them a popular and effective choice for posterior sampling in imaging inverse problems. Existing...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：do, Diffusion, When, why, how, posterior, samplers, fail?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30330v1) | [下载PDF](https://arxiv.org/pdf/2605.30330v1.pdf)

---

## [26. SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?](https://arxiv.org/abs/2605.30329v1)

**作者**：Sy-Tuyen Ho, Minghui Liu, Huy Nghiem 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-28

### 📄 论文摘要

Autonomous AI research agents aim to accelerate scientific discovery by automating the research pipeline, from hypothesis generation to peer review. However, existing benchmarks rarely test a fundamental bottleneck: whether Large Language Models can judge the methodological viability of a research idea before expending time and computational resources. We introduce SoundnessBench, a curated benchmark of 1,099 machine-learning research proposals reconstructed from ICLR submissions, labeled with reviewer soundness sub-scores, and audited against source papers. SoundnessBench should be interpreted as a benchmark for recoverable proposal-stage soundness rather than exact prediction of full-paper review outcomes. Across 12 frontier LLMs, we find a pervasive optimism bias: under standard prompting, models frequently rate low-soundness proposals as sound, while aggressive prompting largely shifts errors from false positives to false negatives. Additional controls for public-corpus contamination, paper-identifying phrases, surface features, and human audit quality suggest that this behavior is not explained by a single confounder. Our results indicate that current LLMs are not yet reliable as standalone first-gate evaluators for scientific rigor.

### 🤖 AI 总结

**一句话总结**：Autonomous AI research agents aim to accelerate scientific discovery by automating the research pipeline, from hypothesis generation to peer review. However, existing benchmarks rarely test a fundamen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SoundnessBench, Can, Scientist, Really, Tell, Good, Research, Ideas

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30329v1) | [下载PDF](https://arxiv.org/pdf/2605.30329v1.pdf)

---

## [27. In-Context Reward Adaptation for Robust Preference Modeling](https://arxiv.org/abs/2605.30323v1)

**作者**：Zhenyu Sun, Zheng Xu, Ermin Wei  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-28

### 📄 论文摘要

Reinforcement Learning from Human Feedback (RLHF) typically relies on static reward models to align Large Language Models with human preferences. However, human values are inherently diverse and heterogeneous, and a single reward model often lacks the robustness required to generalize to unseen preference domains. While existing multi-reward frameworks attempt to address this, they are often restricted to a fixed set of known domains and fail to adapt to unseen human distributions without costly retraining. In this work, we propose In-Context Reward Adaptation, a transformer-based framework designed to model diverse and unseen human preferences on the fly. By leveraging the in-context learning capabilities of transformers, our approach adaptively infers the underlying reward structure from a small set of preference demonstrations. We demonstrate that while a standard transformer architecture is insufficient for this task by characterizing an asymptotic bias to the ground-truth, incorporating human response time as an auxiliary input signal enables the model to successfully adapt to preferences from previously unseen domains. Our findings show that this approach provides a more robust foundation for preference modeling, allowing for the representation of heterogeneous rewards and preference distribution shift, and offering a scalable path toward more flexible human-AI alignment.

### 🤖 AI 总结

**一句话总结**：Reinforcement Learning from Human Feedback (RLHF) typically relies on static reward models to align Large Language Models with human preferences. However, human values are inherently diverse and heter...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：In-Context, Reward, Adaptation, Robust, Preference, Modeling, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30323v1) | [下载PDF](https://arxiv.org/pdf/2605.30323v1.pdf)

---

## [28. Gram: Assessing sabotage propensities via automated alignment auditing](https://arxiv.org/abs/2605.30322v1)

**作者**：David Lindner, Victoria Krakovna, Sebastian Farquhar  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-28

### 📄 论文摘要

We introduce Gram, an automated alignment auditing framework to assess the propensity of AI agents to engage in sabotage. We evaluate Gemini models across 17 simulated agentic deployment scenarios that incentivize sabotage. We find Gemini models misbehave in about 2-3% of our simulated trajectories. Many of these cases are explained by "overeagerness" in Gemini models resulting in both excessive role-playing and goal-seeking behavior. In contrast to other alignment auditing approaches, Gram is designed to specifically evaluate misalignment and intentional sabotage in agentic coding and research agents. We additionally introduce an experimental investigator agent pipeline which enables fine-grained targeted experiments to identify the drivers of misbehavior. We find that increasing realism of environments and removing nudges to misbehave tends to reduce sabotage rates close to zero.

### 🤖 AI 总结

**一句话总结**：We introduce Gram, an automated alignment auditing framework to assess the propensity of AI agents to engage in sabotage. We evaluate Gemini models across 17 simulated agentic deployment scenarios tha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Gram, Assessing, sabotage, propensities, via, automated, alignment, auditing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30322v1) | [下载PDF](https://arxiv.org/pdf/2605.30322v1.pdf)

---

## [29. Self-Trained Verification for Training- and Test-Time Self-Improvement](https://arxiv.org/abs/2605.30290v1)

**作者**：Chen Henry Wu, Aditi Raghunathan  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-05-28

### 📄 论文摘要

Self-improvement at scale has been a longstanding goal for reasoning models, and there are two natural places to do it: at test time, through verification-refinement (V-R) loops; and at training time, through self-training methods. Both are gated by the same bottleneck: the verifier. V-R loops stall when verifier scores inflate while accuracy stagnates, and when feedback is too generic to act on; self-training fails similarly when bad self-generated data are added to training. Better verification would unlock both, but the capability we want to train, i.e., catching self-generated errors, lacks training signal. To address this challenge, we propose self-trained verification (STV). Our key observation is that, while a model cannot catch these errors alone, it can when shown the reference solution. We turn this asymmetry into a supervision target and train the verifier to imitate a more informed version of itself. At test time, STV substantially improves V-R loops on hard problems, while alternatives (e.g., SFT, RL on verifier scores, and even meta-verifiers) do not. STV roughly doubles accuracy on hard math and lifts it 14x on scientific reasoning tasks (1.5% to 21%). At training time, we additionally train the generator using RL with STV verifier's feedback inside the V-R loop - a procedure we call verifier-in-the-loop training (ViL). Starting from an RL-converged generator, ViL yields a further 33% gain in pass@1. More notably, the generator's standalone pass@1, with no verifier at test time, climbs 30% relative past where standard RL had converged. Hence, the next frontier in reasoning on hard problems may lie in how we train for and with verification.

### 🤖 AI 总结

**一句话总结**：Self-improvement at scale has been a longstanding goal for reasoning models, and there are two natural places to do it: at test time, through verification-refinement (V-R) loops; and at training time,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Self-Trained, Verification, Training, Test-Time, Self-Improvement, scale, has

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30290v1) | [下载PDF](https://arxiv.org/pdf/2605.30290v1.pdf)

---

## [30. Statistical Embeddings for Similarity, Retrieval, and Interpretable Alignment of Numeric Tabular Datasets](https://arxiv.org/abs/2605.30289v1)

**作者**：M. Ross Kunz, John Merickel, Keith Wilson  
**分类**：cs.LG, stat.AP, stat.ML  
**发布时间**：2026-05-28

### 📄 论文摘要

Numeric tabular datasets are the dominant data format in scientific practice, yet large language models lack native mechanisms for representing numeric datasets in a meaningful way across heterogeneous feature spaces. Existing approaches either target predictive modeling over individual datasets, which requires a shared set of variable definitions, or lack mechanisms for interpretable cross-dataset alignment. The proposed methodology characterizes numeric tabular datasets through structured exploratory data analysis descriptors, embeds those descriptors into a shared vector space using a pretrained sentence transformer, and quantifies cross-dataset similarity via Canonical Correlation Analysis (CCA). Furthermore, a penalized formulation of CCA is applied to recover sparse, interpretable variable-level correspondences between datasets, identifying which statistical descriptors or variable-level quantities drive cross-dataset alignment without requiring shared variable names or feature conventions. Differential privacy is optionally applied to the descriptor set prior to embedding, supporting deployment in sensitive data contexts without requiring access to raw observations at time of comparison. The methodology is evaluated across 15 datasets spanning general-purpose benchmarks, materials informatics, and nuclear-grade graphite characterization. Results demonstrate a total P@1 score of 0.9, with known nearest-neighbor retrieval and cluster structure remaining robust across embedding ablations and differential privacy budgets. The proposed framework provides a principled pathway for integrating heterogeneous numeric data into retrieval-augmented generation pipelines while preserving statistical context, with direct applications to data-driven algorithm selection and simulation model initialization for unknown datasets.

### 🤖 AI 总结

**一句话总结**：Numeric tabular datasets are the dominant data format in scientific practice, yet large language models lack native mechanisms for representing numeric datasets in a meaningful way across heterogeneou...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Statistical, Embeddings, Similarity, Retrieval, Interpretable, Alignment, Numeric

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.30289v1) | [下载PDF](https://arxiv.org/pdf/2605.30289v1.pdf)

---

