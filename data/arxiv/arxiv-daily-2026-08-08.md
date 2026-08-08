# arXiv AI 论文日报 | 2026-08-08

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (7 篇)
- [cs.LG](#csLG) (11 篇)
- [cs.CV](#csCV) (7 篇)

---

## cs.AI

## [1. The Low Frequency Trap: Video Language Models Fail at Simple Event Bookkeeping](https://arxiv.org/abs/2608.06361v1)

**作者**：Sarvesh Baskar, Zikui Cai, Shayan Shabihi 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-06

### 📄 论文摘要

Real-world video benchmarks provide broad coverage, but their fixed clips entangle event count, rate, duration, and visual complexity, making failure modes hard to isolate. While existing programmatic benchmarks offer better control, they score only the final answer rather than auditing reported events against executable ground truth. To bridge this gap, we introduce trace-grounded parametric profiling for event counting in three controlled video tasks: bouncing-ball wall contacts, visual blinks, and categorical state transitions. Across 2,190 videos, we vary event count N and frequency F while holding rendering fixed. Each video includes an executable event trace for capability-surface estimation and timestamp-level evaluation. Our results reveal a staged temporal failure. At an 80% reliability threshold, Gemini 3.6 Flash reliably counts persistent state transitions up to 12 events at 0.5 and 1.0 Hz, yet demonstrates no reliable positive-count region for transient blinking events. Thus, event representation dictates whether a model initially accesses evidence -- a limitation that compounds as count and frequency increase. In the high-count, high-frequency regime, only 0.2% of final counts are correct and the model recovers just 18.1% of true events. To test if visual access is the primary bottleneck, we increase sampling rate. Although this boosts Bounce Ball accuracy from 19.6% to 29.3%, the reported sequence agrees with ground truth only 3.7% of the time. Extra frames can therefore inflate final scores without producing faithful event recovery. Different prompting strategies yield similarly limited gains, and real-world video evaluations show the same concentration of success at low event counts. Ultimately, trace-grounded profiling shifts video evaluation from aggregate accuracy metrics to a detailed diagnostic of where temporal reasoning fails.

### 🤖 AI 总结

**一句话总结**：Real-world video benchmarks provide broad coverage, but their fixed clips entangle event count, rate, duration, and visual complexity, making failure modes hard to isolate. While existing programmatic...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Low, Frequency, Trap, Video, Language, Models, Fail

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06361v1) | [下载PDF](https://arxiv.org/pdf/2608.06361v1.pdf)

---

## [2. Challenges in Evaluating Explanation Methods for Static and Evolving Data](https://arxiv.org/abs/2608.06351v1)

**作者**：Jerzy Stefanowski  
**分类**：cs.AI  
**发布时间**：2026-08-06

### 📄 论文摘要

This paper addresses the limitations of Explainable Artificial Intelligence (XAI) with respect to insufficient evaluation. They are illustrated through the DetoxAI image recognition system for bias detection and concept unlearning. Then, an example of a human-grounded evaluation of methods for explaining image classification is presented. The paper further explores methods for adapting explanations to evolving data streams with concept drift. Experiences with adapting counterfactuals for this problem are discussed. Finally it is related to the challenges of tracking the co-evolution of data, models, and explanations.\footnote{This paper has been accepted for a publication in J.Nalepa (ed) Explainable AI in Space. Proceedings of EASi 2026 Workshop at IJCAI-ECAI 2026 Bremen, Springer CCIS vol 3107 (2016).}

### 🤖 AI 总结

**一句话总结**：This paper addresses the limitations of Explainable Artificial Intelligence (XAI) with respect to insufficient evaluation. They are illustrated through the DetoxAI image recognition system for bias de...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Challenges, Evaluating, Explanation, Methods, Static, Evolving, Data, paper

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06351v1) | [下载PDF](https://arxiv.org/pdf/2608.06351v1.pdf)

---

## [3. TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories](https://arxiv.org/abs/2608.06346v1)

**作者**：Yunjia Qi, Zehua Yin, Xintong Shi 等 13 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-06

### 📄 论文摘要

LLM-based agentic systems have shown remarkable capabilities in complex domains, while suffering from cascading errors and difficulty in debugging. Critical error detection aims to locate the earliest error step in a failed trajectory that is responsible for the final failure. However, progress faces two main challenges. First, long trajectories make it difficult to identify individual errors, since the evidence for judging a step may be scattered across distant instructions, observations, and prior context. Second, failed trajectories often contain multiple local errors with different downstream effects, only some of which remain responsible for the final failure. In this work, we propose TrajDebug, an error-lifecycle tracing framework that addresses long-trajectory error discovery with multi-granularity history compression and evidence-based error identification, and supports critical attribution by tracing each error's resolution status and terminal impact. We further construct TrajErrBench, a benchmark of 486 manually annotated failed trajectories from Tau2Bench and SWE-Bench Pro, covering realistic tool-use and coding scenarios. Experiments across diverse agent benchmarks show that TrajDebug achieves the best overall performance over existing baselines, and application studies further demonstrate that its diagnoses provide actionable feedback for improving downstream agent success. We will release the codes and data to facilitate further research.

### 🤖 AI 总结

**一句话总结**：LLM-based agentic systems have shown remarkable capabilities in complex domains, while suffering from cascading errors and difficulty in debugging. Critical error detection aims to locate the earliest...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TRAJDEBUG, Tracing, Error, Lifecycle, Identify, Critical, Failures, Long-Horizon

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06346v1) | [下载PDF](https://arxiv.org/pdf/2608.06346v1.pdf)

---

## [4. Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations](https://arxiv.org/abs/2608.06305v1)

**作者**：Sagar Tamang, Ayush Vyas, Tabarakul Hazarika  
**分类**：cs.AI, cs.CL, cs.IR  
**发布时间**：2026-08-06

### 📄 论文摘要

Retrieval-augmented generation over long documents is dominated by one design: chunk the text, embed the chunks, and surface the top-k nearest neighbours of the query. We argue that for an important class of documents -- financial statements, audit reports, regulatory returns -- this design is structurally unsound, and we make the argument measurable. On a 780-page government financial report, 86.8% of content lines are table rows, thousands of near-identical figures compete in one embedding space, and a figure inherits its unit from a header a median of 13 lines above it -- so a chunk boundary routinely separates a number from whether it is in lakh or crore, an error of two orders of magnitude. A table-aware chunker built as a steelman fixes the unit problem but leaves 27-30% of numeric chunks with no fiscal-year header at every chunk size we tried. We propose READ (Reliable Embedding-free Agentic Document-search), in which an agent reads the raw document through three deterministic operations -- normalized lexical search, structural navigation, and bounded span reads -- exposed over the Model Context Protocol, so a trajectory is a replayable audit trail, not an opaque similarity score. On 51 verified questions READ answers 58.8% against dense retrieval's 15.7% (p_Holm = 2 x 10^-5) -- or 35.3% tuned, which READ still leads by 23.5 points (p_Holm = 0.017). An agent given the same loop but a top-k tool reaches only 27.5%, locating the gain in the interface rather than in iteration. We also report what the evidence does not support: BM25 is statistically indistinguishable from READ, so our result separates embedding-based from embedding-free retrieval, not agentic from lexical search.

### 🤖 AI 总结

**一句话总结**：Retrieval-augmented generation over long documents is dominated by one design: chunk the text, embed the chunks, and surface the top-k nearest neighbours of the query. We argue that for an important c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Top-K, Replacing, Black-Box, Retrieval, Interpretable, Agentic, Operations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06305v1) | [下载PDF](https://arxiv.org/pdf/2608.06305v1.pdf)

---

## [5. HarnessOpt-Bench: Evaluating LLMs at Harness Optimization](https://arxiv.org/abs/2608.06301v1)

**作者**：Varun Ursekar, Apaar Shanker, Yash Maurya 等 7 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-08-06

### 📄 论文摘要

As LLMs are increasingly deployed within agentic systems, their capabilities depend not only on the model weights but also on the harness: the prompts, tools, control flow, memory, and orchestration code surrounding them. This makes automated harness optimization -- the iterative and evaluation-guided improvement of a harness by an AI system -- both an important route to improving AI systems and a demanding capability for AI systems themselves. Yet the community lacks a common protocol for measuring how well frontier LLMs perform at this task. We introduce HarnessOpt-Bench, a benchmark for end-to-end harness optimization under expensive and stochastic evaluation. An optimizer, an LLM paired with a coding harness, receives a target agent's seed harness, graded evaluation feedback, and a fixed target-evaluation budget. It edits the harness and nominates a final candidate, which is scored by its normalized gain over the seed on a held-out test partition that remains inaccessible throughout search. A trusted execution environment enforces the evaluation boundary, meters target-agent resource use, and preserves candidate versions for audit. We evaluate 5 frontier LLMs as optimizers both under a shared coding harness and under their native harnesses across 4 downstream tasks, over 111 scored runs. Experiment results show that optimizer models separate more than the coding harnesses they act through, native harnesses are not consistently superior, and gains vary substantially across tasks and seed regimes. These results establish harness optimization as a measurable and discriminative capability with large space for improvement.

### 🤖 AI 总结

**一句话总结**：As LLMs are increasingly deployed within agentic systems, their capabilities depend not only on the model weights but also on the harness: the prompts, tools, control flow, memory, and orchestration c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, at, As, HarnessOpt-Bench, Evaluating, Harness, Optimization, increasingly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06301v1) | [下载PDF](https://arxiv.org/pdf/2608.06301v1.pdf)

---

## [6. Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors](https://arxiv.org/abs/2608.06300v1)

**作者**：Arya Labroo, Mengjie Qian, Kate Knill  
**分类**：cs.AI  
**发布时间**：2026-08-06

### 📄 论文摘要

Automatic speaking assessment systems are increasingly deployed in high-stakes settings to mark second language (L2) learners' speaking tests, making it critical to show that their scores depend on speaking proficiency rather than irrelevant speaker attributes such as first language (L1) or age. Transformer-based foundation models have improved the accuracy of these L2 speaking graders, but their black-box representations make fairness and interpretability analysis more difficult. Building on prior work that used Concept Activation Vectors (CAVs) to detect bias towards unwanted attributes (`concepts') in feature-based graders, we extend CAV-based analysis to two neural speaking assessment systems: a text-based BERT grader and a speech-and-text multimodal grader based on Whisper. CAVs represent human-interpretable concepts as directions in a model's activation space, allowing us to distinguish between whether a concept is encoded in a model's internal representations and whether it influences the predicted score, the latter quantified using a gradient-based sensitivity metric. Since CAVs rely on linear separability, which is less likely in complex neural embedding spaces, we also investigate whether sparse autoencoders (SAEs) provide cleaner concept directions by learning CAVs in a sparse latent space and mapping them back to activation space. Our analysis shows that concept recoverability depends strongly on the representation and architecture being probed, rather than on the concept alone. Sensitivity to concepts is also architecture-dependent. SAEs make concepts more linearly recoverable, but attenuate the original activation-space sensitivity, especially in low-dimensional layers. These findings highlight the need to distinguish concept recoverability from concept influence when auditing bias in speaking assessment systems.

### 🤖 AI 总结

**一句话总结**：Automatic speaking assessment systems are increasingly deployed in high-stakes settings to mark second language (L2) learners' speaking tests, making it critical to show that their scores depend on sp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, L2, Bias, Analysis, Speaking, Assessment, Systems, Concept

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06300v1) | [下载PDF](https://arxiv.org/pdf/2608.06300v1.pdf)

---

## [7. QuanTiMedAI: Quantum-Enhanced Time-Series Model guided by Agentic AI for Cardiac Arrest Mortality Prediction](https://arxiv.org/abs/2608.06294v1)

**作者**：Mutasim Fuad Sarker, Adiba Rahman Namira, Wafa Binte Alam 等 6 位作者  
**分类**：cs.AI, cs.ET  
**发布时间**：2026-08-06

### 📄 论文摘要

Cardiac arrest remains one of the most lethal conditions encountered in intensive care units. Despite the growing availability of electronic health record data, existing mortality prediction studies in this population largely depend on static summaries derived from early admission. Such approaches ignore the temporal progression of physiological deterioration and recovery that unfolds throughout a patient's ICU stay. To address this limitation, we introduce QuanTiMedAI, a quantum-agentic framework developed for cardiac arrest mortality prediction using agentic AI guided quantum enhancement time series model. The proposed system combines an agentic large language model (LLM) for clinically informed feature discovery with a compact quantum recurrent network for temporality aware mortality prediction. Our findings demonstrate that agentic LLM-guided feature selection consistently outperforms conventional feature selection approaches, and the proposed quantum architecture achieves competitive predictive performance through nonlinear feature enhancement while keeping the number of parameters very low. Through extensive experimentation on a MIMIC-IV cohort of cardiac arrest patients, QuanTiMedAI's quantum-enhanced architecture attains an AUROC of 0.852 using only 605 parameters, an improvement of approximately 2.9\% over a current state-of-the-art baseline for this task. A structured ablation study systematically validates the contribution of each architectural design choice. These results show that quantum-enhanced sequential modeling can exceed classical recurrent networks while using substantially fewer parameters.

### 🤖 AI 总结

**一句话总结**：Cardiac arrest remains one of the most lethal conditions encountered in intensive care units. Despite the growing availability of electronic health record data, existing mortality prediction studies i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：QuanTiMedAI, Quantum-Enhanced, Time-Series, Model, guided, Agentic, Cardiac, Arrest

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06294v1) | [下载PDF](https://arxiv.org/pdf/2608.06294v1.pdf)

---

## cs.CL

## [8. Learning When to Trust via Selective Context Preference Optimization](https://arxiv.org/abs/2608.06377v1)

**作者**：Xian Sun, Wei Chow, Yingshuo Wang 等 7 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-08-06

### 📄 论文摘要

Language models increasingly condition their answers on external signals, and a single misleading one can turn a correct answer wrong. The obvious remedy, training models to resist such signals, hides a failure mode: a model that ignores all context looks robust yet is useless when the context is worth trusting. We recast the problem as selective trust and introduce MIST, a human-annotated benchmark that renders each reasoning item under four matched conditions (clean, misleading, correct-context, and irrelevant-context), together with SC2W, a paired metric counting how often a misleading signal flips a clean-correct answer to wrong. Across a comprehensive benchmark study, we observe that such a susceptibility is universal. We then propose SCOPE, which mines clean-correct/misleading-wrong failures and optimizes a standard Direct Preference Optimization (DPO) objective over matched preference pairs balanced equally across all four conditions, rather than over misleading items alone. Our approach substantially reduces SC2W on popular open-sourced models while preserving accuracy when the added context is clean, correct, or irrelevant. With this work, we argue that models should be judged on selective trust, not on resistance alone.

### 🤖 AI 总结

**一句话总结**：Language models increasingly condition their answers on external signals, and a single misleading one can turn a correct answer wrong. The obvious remedy, training models to resist such signals, hides...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, When, Trust, via, Selective, Context, Preference, Optimization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06377v1) | [下载PDF](https://arxiv.org/pdf/2608.06377v1.pdf)

---

## [9. The Bitter Lesson of Tool Calling](https://arxiv.org/abs/2608.06370v1)

**作者**：Ishan Patel, Sahil Sen, Elias Lumer 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-06

### 📄 论文摘要

Tool use transforms LLMs into agents that act beyond their training data, and for code-capable models, programmatic tool calling extends this further by replacing rigid JSON calls with scripts that chain and parallelize naturally. However, a systematic evaluation of tools as code on an established benchmark across current and prior model generations under real-world task conditions has not been conducted. In this work, we empirically compare programmatic tool calling (PTC) to native JSON tool calling across 14 language models on BFCL v4. In the programmatic tool calling paradigm, tools are exposed as typed Python stubs that the model invokes through code, with execution and results handled in a single agent turn. Programmatic tool calling matches or exceeds native JSON tool calling in 11 of 14 models on BFCL v4, with the GPT-5.6 family achieving a 10.6% improvement over the JSON tool calling baseline. Further, it matches or outperforms baseline in 13 of 14 models under parallel fan-out, and holds stable under context rot conditions where baseline degrades 2.3% on average. Our results demonstrate that programmatic tool calling is a viable and robust alternative to JSON tool calling, with performance tracking model capability across release generations.

### 🤖 AI 总结

**一句话总结**：Tool use transforms LLMs into agents that act beyond their training data, and for code-capable models, programmatic tool calling extends this further by replacing rigid JSON calls with scripts that ch...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Bitter, Lesson, Tool, Calling, use, transforms

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06370v1) | [下载PDF](https://arxiv.org/pdf/2608.06370v1.pdf)

---

## [10. Benchmarking the Benchmarks: Evaluating Benchmarks for Conversational Agents](https://arxiv.org/abs/2608.06329v1)

**作者**：Noam Koren, Roy Bar-Haim, Abigail Goldsteen  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-06

### 📄 论文摘要

Task-oriented conversational agents are evaluated using curated or automatically generated benchmarks, yet benchmark quality is rarely assessed. Poor benchmarks may contain inconsistent tasks, simplistic scenarios, or limited policy coverage, leading to unreliable evaluations. We introduce a reference-free framework that uses LLM judges to assess benchmark consistency, complexity, and policy coverage, while providing actionable diagnostics of weaknesses. We validate the framework by demonstrating agreement with independent human annotations and by evaluating benchmarks generated by LLMs of varying capabilities, as well as benchmarks subjected to controlled quality-degrading perturbations. Across domains and judge models, the proposed metrics consistently distinguish between benchmark quality levels. We further demonstrate the framework's applicability to manually curated benchmarks. Our framework offers a practical approach for evaluating synthetic and manually curated conversational-agent benchmarks.

### 🤖 AI 总结

**一句话总结**：Task-oriented conversational agents are evaluated using curated or automatically generated benchmarks, yet benchmark quality is rarely assessed. Poor benchmarks may contain inconsistent tasks, simplis...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Benchmarking, Benchmarks, Evaluating, Conversational, Task-oriented, evaluated, curated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06329v1) | [下载PDF](https://arxiv.org/pdf/2608.06329v1.pdf)

---

## [11. Benchmarking and Enhancing LLMs for Rule-Intensive Review of National Standard Documents](https://arxiv.org/abs/2608.06312v1)

**作者**：Tao Wang, Qihao Yang, Rongjiao Liang 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-06

### 📄 论文摘要

Large language models (LLMs) increasingly support complex professional tasks, yet their capabilities in rule-intensive document review remain insufficiently evaluated. National standard documents, such as China GB/T standards, offer a representative testbed: they are lengthy, highly structured, and governed by explicit rules for scope, terminology, normative wording, and cross-section consistency. Existing benchmarks focus on domain knowledge and question answering, largely overlooking intrinsic quality review for professional documents. Such reviews rely heavily on human experts, making them costly and difficult to scale. To bridge this gap, we introduce GB/T-Bench, the first benchmark for the structured review of national standard documents. Its GB/T Review Taxonomy is a hierarchical schema covering document structure, scope alignment, normative modality, terminology consistency, and normative references, with 25 diagnosable error types. A controllable counterexample generation mechanism combines deterministic rules and constrained LLM rewriting to process 488 documents into 7,306 traceable review error instances for evaluation. We also develop a diagnosis-oriented evaluation protocol requiring exact matches on error location, review dimension, and error type, plus document-level coverage metrics. We further propose GB/T-Reviewer, a multi-agent framework that converts review knowledge into specialized skills and coordinates global inspection, targeted diagnosis, rule scanning, and result verification. Experiments with 14 mainstream LLMs reveal a substantial human-LLM gap: the strongest model achieves only 0.3280 CMCS versus 0.6640 for experts. GB/T-Reviewer raises the best CMCS to 0.5094, showing the value of structured skill coordination for rule-intensive document review. This work paves the way for trustworthy AI in standardization and other high-stakes document domains.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) increasingly support complex professional tasks, yet their capabilities in rule-intensive document review remain insufficiently evaluated. National standard documents, suc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, of, Benchmarking, Enhancing, Rule-Intensive, Review, National, Standard

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06312v1) | [下载PDF](https://arxiv.org/pdf/2608.06312v1.pdf)

---

## [12. NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering](https://arxiv.org/abs/2608.06292v1)

**作者**：Jonas Gann, Michael Gertz  
**分类**：cs.CL, cs.SC  
**发布时间**：2026-08-06

### 📄 论文摘要

Retrieval-augmented generation (RAG) improves question answering by grounding large language models (LLMs) in external knowledge such as text corpora. However, its reasoning process remains largely opaque: intermediate reasoning steps are difficult to verify and cannot be reliably attributed to specific evidence. Moreover, missing user-specific context is rarely detected systematically, often leading to incomplete or incorrect output.   We propose NeSy-RAG, a modular neuro-symbolic RAG framework that synthesizes attributable Prolog modules from retrieved text chunks. For each chunk, the system generates semantically meaningful predicates that encode Boolean claims, which may depend on user facts. Using joint natural language-code embeddings, predicates are retrieved and composed into Prolog queries. To address incomplete user context, we introduce a symbolic knowledge-gap detection mechanism that identifies missing user facts whose truth values affect the query outcome and automatically triggers follow-up interactions.   Executing the resulting Prolog queries yields deterministic answers together with transparent execution traces that link each reasoning step to its originating source. On the ShARC benchmark, without domain-specific training, NeSy-RAG achieves 61.1% accuracy, outperforming a same-model RAG baseline that achieves 42.8% accuracy.

### 🤖 AI 总结

**一句话总结**：Retrieval-augmented generation (RAG) improves question answering by grounding large language models (LLMs) in external knowledge such as text corpora. However, its reasoning process remains largely op...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RAG, NeSy-RAG, Neuro-Symbolic, Explainable, Question, Answering, Retrieval-augmented, generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06292v1) | [下载PDF](https://arxiv.org/pdf/2608.06292v1.pdf)

---

## cs.CV

## [13. Does FLAIR super-resolution erase or hallucinate small white-matter lesions?](https://arxiv.org/abs/2608.06311v1)

**作者**：Zahra Khodakarami, Yue Li, Pulkit Khandelwal 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-06

### 📄 论文摘要

White matter hyperintensities (WMH), bright regions on Fluid-attenuated Inversion Recovery (FLAIR) scans are associated with cerebrovascular pathology and neurodegeneration. FLAIR is usually acquired with thick slices in clinical settings, giving it poor through-plane resolution. Super-resolution (SR) is a widely used method for recovering an isotropic volume from an anisotropic scan. Yet whether applying it prior to WMH segmentation preserves lesion content remains unknown: a model may erase small real lesions or hallucinate absent ones. We used 1-mm isotropic high-resolution (HR) FLAIR scans from 29 individuals in the ADNI cohort, each manually segmented for WMH by an expert. Then, we degraded each to simulated 3 and 5 mm through-plane acquisitions. Multi-contrast implicit neural representation (INR), a single-contrast self-supervised model (ECLARE), and cubic interpolation were used to upsample them onto the HR grid. WMH segmentation from a simulated thick slice and the original HR FLAIR set the floor and ceiling, respectively, for the per-lesion analysis. Of four WMH segmentation methods (WMH-SynthSeg, segcsvd, MARS-WMH, TrUE-Net), we ran the analysis under the most sensitive one to small lesions on HR (MARS-WMH) with the evaluation metrics of detection sensitivity, erasure rate (HR-detected lesions lost after reconstruction), and hallucination rate (predicted components absent from both the manual and HR segmentation). The dominant effect of SR was erasure of small real lesions, not hallucination, and it increased with slice thickness, though every reconstruction still improved lesion detection over the raw thick slice. ECLARE recovered small lesion signal best at both thicknesses, while the INR was no better than cubic interpolation.

### 🤖 AI 总结

**一句话总结**：White matter hyperintensities (WMH), bright regions on Fluid-attenuated Inversion Recovery (FLAIR) scans are associated with cerebrovascular pathology and neurodegeneration. FLAIR is usually acquired ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：or, Does, FLAIR, super-resolution, erase, hallucinate, small, white-matter

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06311v1) | [下载PDF](https://arxiv.org/pdf/2608.06311v1.pdf)

---

## [14. UQ-Loc: Uncertainty-Aware LiDAR Scene Coordinate Regression](https://arxiv.org/abs/2608.06307v1)

**作者**：Jacek Komorowski  
**分类**：cs.CV  
**发布时间**：2026-08-06

### 📄 论文摘要

LiDAR-based Scene Coordinate Regression (SCR) maps point clouds directly to 3D scene coordinates, enabling precise 6-DoF localisation without explicit map retrieval. However, existing methods produce deterministic predictions, discarding aleatoric uncertainty that could improve robustness and downstream decision-making. We present UQ-Loc, which extends the LightLoc architecture with an anisotropic Gaussian covariance head that predicts a full 3x3 positive-definite covariance matrix per voxel. Training uses a Negative Log-Likelihood (NLL) loss augmented with a kNN-based spatial smoothness regulariser, while inference employs a modified SC2-PCR solver with uncertainty-weighted seed scoring and a Mahalanobis-distance inlier test. We adopt Expected Calibration Error (ECE) as a principled metric for evaluating the quality of the predicted uncertainty. Experiments demonstrate that UQ-Loc achieves consistent improvement in 6-DoF localization accuracy while producing well-calibrated covariances.

### 🤖 AI 总结

**一句话总结**：LiDAR-based Scene Coordinate Regression (SCR) maps point clouds directly to 3D scene coordinates, enabling precise 6-DoF localisation without explicit map retrieval. However, existing methods produce ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UQ-Loc, Uncertainty-Aware, LiDAR, Scene, Coordinate, Regression, LiDAR-based, SCR

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06307v1) | [下载PDF](https://arxiv.org/pdf/2608.06307v1.pdf)

---

## [15. TLNM: Externally Validated Tooth Detection, Numbering and Segmentation from Smartphone Photographs Using Mask R-CNN](https://arxiv.org/abs/2608.06275v1)

**作者**：Arash Nedaei, Henna Tiensuu, Elina Väyrynen 等 5 位作者  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-08-06

### 📄 论文摘要

Oral health issues affect billions globally, but the cost and limited access to professional dental care hinder preventive oral healthcare. Research relies on clinical-grade radiographs or intraoral camera images, unavailable for public self-screening. This study introduces a tooth localisation and numbering model for smartphone photographs. We developed a customised Mask Region-based Convolutional Neural Network (Mask R-CNN) pipeline trained on 1,272 annotated smartphone images. To address variability in patient-generated health data, the pipeline incorporates two domain-informed mechanisms: a masked gray-world white-balancing algorithm to mitigate artificial colour casts and an anatomically constrained detection layer to enforce structural validity and suppress false positives. Evaluation comprised four stages: internal held-out testing, independent external testing, a descriptive ablation study, and fold-based training stability analysis using the same internal test set. On the internal test set, the model achieved an instance-mask AP@50 of 0.818, class-aware PQ of 0.780, and operational F1 of 0.884. Training stability showed limited between-model variation: across ten runs, instance-mask AP@50 had a standard deviation of 0.009. On the external dataset, the model achieved an instance-mask AP@50 of 0.901, class-aware PQ of 0.832, and operational F1 of 0.928 despite differences in population, sensors, and acquisition protocols. The inference pipeline is available as an open-source, containerised API. These results demonstrate that consumer-grade smartphone imagery can support automated tooth-level anatomical mapping, offering a scalable, potentially low-cost foundation for remote screening and tele-dentistry in resource-constrained environments.

### 🤖 AI 总结

**一句话总结**：Oral health issues affect billions globally, but the cost and limited access to professional dental care hinder preventive oral healthcare. Research relies on clinical-grade radiographs or intraoral c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TLNM, Externally, Validated, Tooth, Detection, Numbering, Segmentation, Smartphone

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06275v1) | [下载PDF](https://arxiv.org/pdf/2608.06275v1.pdf)

---

## [16. OTLesMix: Wasserstein Barycenter and Optimal Transport Map for Synthetic Lesion Generation with Diverse Shapes and Locations](https://arxiv.org/abs/2608.06264v1)

**作者**：Robin Trombetta, Carole Lartizien  
**分类**：cs.CV, cs.LG, eess.IV  
**发布时间**：2026-08-06

### 📄 论文摘要

The development of deep learning over the past decade has revolutionized medical imaging segmentation, allowing the extraction of precise descriptors from large volumes to characterize pathologies. Data augmentation is a technique widely regarded as a way to improve model training. It includes simple transformations like spatial operations or intensity modifications, but also more advanced synthesis techniques. Their goal is to generate new realistic samples from an existing dataset to diversify the images used during training. Among them, several propose different mixing strategies to combine real samples. However, one of their major shortcomings is to yield limited variability in terms of generated lesion shapes and locations. In this work, we introduce a novel image synthesis method, called OTLesMix, that leverages Wasserstein barycenter and optimal transport plan to generate realistic and diverse samples. We evaluated our method on three brain lesion segmentation tasks, on which it improves the Dice score compared to a model trained without synthetic data by 2.9 to 6.6 points, and outperforms state-of-the-art mix-based methods.

### 🤖 AI 总结

**一句话总结**：The development of deep learning over the past decade has revolutionized medical imaging segmentation, allowing the extraction of precise descriptors from large volumes to characterize pathologies. Da...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OTLesMix, Wasserstein, Barycenter, Optimal, Transport, Map, Synthetic, Lesion

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06264v1) | [下载PDF](https://arxiv.org/pdf/2608.06264v1.pdf)

---

## [17. Toward Deployable Bangla Sign Language Recognition with Expert-Validated Data and a Lightweight Attention-Based Model](https://arxiv.org/abs/2608.06252v1)

**作者**：Saad Ahmed, Md Khalid Syfullaha  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-06

### 📄 论文摘要

Deaf and hard-of-hearing people in Bangladesh communicate mainly through Bangla Sign Language (BdSL). Automatic BdSL recognition on personal devices could widen access to education and services. Existing systems use controlled-setting datasets without expert verification and heavyweight pretrained backbones unsuited to on-device use. We introduce RSBdSL38, 10,874 expert-validated images spanning all 38 BdSL hand signs, representing the 51 letters of the Bangla alphabet, recorded from real signers at three special-needs schools across Bangladesh. We propose a lightweight attention based convolutional network of 298,470 parameters, built from grouped bottleneck residual blocks, channel and spatial attention, a multi-scale depthwise hand-feature block, dual pooling, and Swish activations. Trained from scratch, it attains 96.37% accuracy (95.72% +- 0.54% over five seeds), within 1.08 percentage points of the best of nine ImageNet-pretrained efficient architectures under an identical protocol, using 8.5 to 68x fewer parameters and 1.3 to 21.7x fewer MACs. Retrained, it reaches 92.95 to 98.33% on six public BdSL benchmarks, 97.04% on a merged corpus, and 76.25% zero-shot on BdSL-38. Removing any architectural stage costs 7.61 to 89.30 points, against at most 3.17 for the training recipe. Grad-CAM with deletion-insertion and weight-randomization checks confirms that predictions follow the signing hand. A signer-independent split holding out 6 of 36 signers yields 85.18%. Quantized to 0.48 MB, it runs at 3.98 ms per image within a 15.5 MB footprint on a commodity smartphone. Together, RSBdSL38 and our from-scratch model turn benchmark accuracy into deployable accessibility at a fraction of pretrained-backbone cost; dataset, code, and models are released.

### 🤖 AI 总结

**一句话总结**：Deaf and hard-of-hearing people in Bangladesh communicate mainly through Bangla Sign Language (BdSL). Automatic BdSL recognition on personal devices could widen access to education and services. Exist...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Toward, Deployable, Bangla, Sign, Language, Recognition, Expert-Validated, Data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06252v1) | [下载PDF](https://arxiv.org/pdf/2608.06252v1.pdf)

---

## [18. PRISM: Distribution-Gated Flow Matching for Controllable Unpaired Image Translation](https://arxiv.org/abs/2608.06240v1)

**作者**：Elad Yoshai, Natan T. Shaked  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-06

### 📄 论文摘要

Unpaired image-to-image translation must decide, per image, what to change and what to preserve without paired supervision. Many diffusion-based unpaired translators control preservation through a single global noise or guidance value applied across the image, which cannot separate content to keep from appearance to change. We present PRISM, a GAN-free flow-matching framework that replaces this global control with a learned per-feature gate. The gate's spatial prior is derived from each source feature's standardized distance to the target feature distribution, so features far from the target are freed while target-consistent features are preserved. The same gate controls both the initialization, which mixes the real source latent with a task-matched corruption, and the transport timing during Ordinary Differential Equation (ODE) integration. The corruption is matched to the task, content-anchored (AdaIN) for structure-preserving translation and partially anchored for structure-changing translation, and the gate can be overridden locally at inference from text or a detector without retraining, preserving important structures of the original image while still generating realistic results. We evaluate PRISM on five natural and biomedical benchmarks (AFHQ cat->dog, CelebA-HQ appearance translation, day->night relighting, virtual staining, and breast frozen->permanent histopathology). Among the evaluated methods under a shared same-split protocol, PRISM attains the best Inception FID and KID on four benchmarks and a competitive result on the fifth, and on histopathology yields the nuclei-count ratio closest to the ideal, supporting a favorable balance between target realism and structural preservation.

### 🤖 AI 总结

**一句话总结**：Unpaired image-to-image translation must decide, per image, what to change and what to preserve without paired supervision. Many diffusion-based unpaired translators control preservation through a sin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PRISM, Distribution-Gated, Flow, Matching, Controllable, Unpaired, Image, Translation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06240v1) | [下载PDF](https://arxiv.org/pdf/2608.06240v1.pdf)

---

## [19. Depth-Guided Video Object Counting in Crowded Scenes](https://arxiv.org/abs/2608.06236v1)

**作者**：Yuanjing Xu, Xinyan Liu, Weidong Chen 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-06

### 📄 论文摘要

Our primary objective is to advance video object counting in crowded scenes, aiming to robustly count all instances of a target category based on given text or visual prompts. Existing methods rely on RGB information, limiting their discriminative ability in crowded and occluded conditions. To address this, we propose a Depth-Guided Detector (DG-Det) along with a general post-processing pipeline. By integrating depth cues with multi-scale RGB-D cross-attention and explicit occlusion prediction, our method enhances spatial understanding and achieves robust detection in crowded and occluded scenes. Furthermore, we introduce a unified de-duplication framework to eliminate cross-frame redundant counting. To facilitate future research, we also release a new RGB-D Video Object Counting dataset featuring depth information and multiple object categories persequence. Extensive experiments demonstrate that our method achieves a 62.01\% reduction in MAE compared to existing baselines, and also produces consistent improvements in RMSE. We provide the source code at https://github.com/streamer-AP/DG-Net and the dataset at https://huggingface.co/datasets/aerospace123/RGBD-VideoCount.

### 🤖 AI 总结

**一句话总结**：Our primary objective is to advance video object counting in crowded scenes, aiming to robustly count all instances of a target category based on given text or visual prompts. Existing methods rely on...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Depth-Guided, Video, Object, Counting, Crowded, Scenes, Our, primary

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06236v1) | [下载PDF](https://arxiv.org/pdf/2608.06236v1.pdf)

---

## cs.LG

## [20. CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks](https://arxiv.org/abs/2608.06352v1)

**作者**：Fanzhe Meng, Guoxin Chen, Jiale Zhao 等 9 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-08-06

### 📄 论文摘要

Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation establishes feasibility, yet does not reveal how a task behaves relative to a given solver setting. In this paper, we present CalibForge, an autonomous terminal-task synthesis system that uses verified solver behavior to revise candidate tasks through adversarial solver calibration. Multi-solver calibration targets disagreement within a heterogeneous solver pool, whereas contrastive solver calibration targets a designated strong-pass/weak-fail relation; both operationalize a solver-relative learnable zone anchored in demonstrated solvability. Using CalibForge, we construct 5,431 calibrated terminal tasks. Our ablations show that both strategies yield more effective supervision than authoring and validation alone or ordinary single-solver feedback. Models trained on the full collection achieve 32.58% and 47.57% on Terminal-Bench 2.0. The largest improvements over the corresponding base model reach 24.71 percentage points on Terminal-Bench 2.0, 27.68 points on SWE-bench Pro, and 30.04 points on Doc2Repo. Together, these results support solver-relative learnability as a practical target for constructing effective and transferable agent training data.

### 🤖 AI 总结

**一句话总结**：Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation establishes feasibility, yet does not ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CalibForge, Adversarial, Solver, Calibration, Scaling, Learnable, Terminal, Tasks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06352v1) | [下载PDF](https://arxiv.org/pdf/2608.06352v1.pdf)

---

## [21. RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via Ranking-Based Reward Construction](https://arxiv.org/abs/2608.06310v1)

**作者**：Chenglong Wang, Ziming Zhu, Yifu Huo 等 12 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-08-06

### 📄 论文摘要

Recent advances in reward modeling show a paradigm shift from discriminative reward models to generative reward models. However, despite their strong capabilities in response ranking, generative reward models have not realized their potential in reinforcement learning (RL). Our analysis reveals that this limitation arises from a mismatch between the comparative nature of generative reward modeling and the scalar scoring paradigm adopted by existing RL algorithms. To bridge this gap, we propose a Ranking-based Reward Construction (RRC) approach, which enables generative reward models to provide more effective RL learning signals by deriving rewards from relative preference rankings. RRC introduces two complementary strategies: self-competitive ranking, which exploits comparisons among sampled responses, and anchor-guided ranking, which enables scalable ranking-based reward construction with a small set of reference responses. Experiments across open-ended chat and reasoning benchmarks demonstrate that RRC substantially improves RL training with generative reward models, achieving consistent gains over existing reward construction approaches. Our code can be found at https://github.com/wangclnlp/RRC.

### 🤖 AI 总结

**一句话总结**：Recent advances in reward modeling show a paradigm shift from discriminative reward models to generative reward models. However, despite their strong capabilities in response ranking, generative rewar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, RRC, Unlocking, Generative, Reward, Models, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06310v1) | [下载PDF](https://arxiv.org/pdf/2608.06310v1.pdf)

---

## [22. On-Policy Self-Distillation without Any Supervision](https://arxiv.org/abs/2608.06296v1)

**作者**：Yijiang Li, Bingyang Wang, Yijun Liang 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-06

### 📄 论文摘要

On-policy (Self-)Distillation (OPD / OPSD) has shown strong potential for post-training large language models (LLMs). However, existing methods still rely heavily on external supervision, including ground-truth signals, environmental feedback, or guidance from larger models, and therefore fall short of genuine "self"-distillation. In this study, we show that on-policy self-distillation can be achieved using only a model's own generations via internal consistency. We propose Unsupervised On-Policy Self-Distillation (U-OPSD). U-OPSD first samples multiple rollouts and constructs a pseudo-solution by majority vote under a self-consistency threshold. It then conditions a teacher distribution on the shortest pseudo-solution and distills it into prefixes of the model's longest incorrect completion, allowing the model to correct itself precisely where it is confidently wrong. Across diverse benchmarks, base models, and training settings, U-OPSD consistently improves over the base models and matches or surpasses supervised methods with ground truth (GT), such as OPSD and GRPO. On AIME24, AIME25, HMMT25, MATH500, and AMC23, U-OPSD improves over the base model by 8.5% and 10.7% on Qwen3 non-thinking mode at the 4B and 8B scales, respectively, and outperforms OPSD by an average of 3.2% and 2.3%. In thinking mode, U-OPSD remains on par with OPSD, outperforming it by 0.9% at 4B and matching it at 8B, while surpassing GRPO by 0.7% and 1.1%, respectively.

### 🤖 AI 总结

**一句话总结**：On-policy (Self-)Distillation (OPD / OPSD) has shown strong potential for post-training large language models (LLMs). However, existing methods still rely heavily on external supervision, including gr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：On-Policy, Self-Distillation, without, Any, Supervision, Self, Distillation, OPD

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06296v1) | [下载PDF](https://arxiv.org/pdf/2608.06296v1.pdf)

---

## [23. BaKron: Efficient Quantization with Kronecker-Factored Hessians](https://arxiv.org/abs/2608.06291v1)

**作者**：Johann Birnick, Rayan Saab  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-06

### 📄 论文摘要

We accelerate a family of algorithms for neural network quantization whose geometry is informed by any Kronecker-factored approximation of the Hessian. GPTQ-style adaptive rounding typically uses one-sided information derived from input activations. Two-sided Kronecker-factored Hessian approximations can additionally capture correlations across output coordinates, but applying GPTQ directly in the vectorized weight domain is computationally expensive. Building on the two-sided adaptive-rounding formulation used by BoA and YAQA, we introduce BaKron, an efficient solver that combines anti-diagonal parallelism with a recursive divide-and-conquer construction. For an $m\times n$ weight matrix, BaKron uses $O(m+n)$ sequential steps while reducing the total work from $O(m^2n^2)$ to $O(mn(m+n))$. Thus, it matches the cubic scaling of GPTQ while exploiting richer curvature information. Moreover, BaKron is modular with respect to both the base quantizer and the Hessian estimator. We also provide practical benchmarks, consider a range of Hessians that BaKron can be called with, find an efficient technique to compute these Hessians, and evaluate the algorithm experimentally.

### 🤖 AI 总结

**一句话总结**：We accelerate a family of algorithms for neural network quantization whose geometry is informed by any Kronecker-factored approximation of the Hessian. GPTQ-style adaptive rounding typically uses one-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, BaKron, Efficient, Quantization, Kronecker-Factored, Hessians, accelerate, family

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06291v1) | [下载PDF](https://arxiv.org/pdf/2608.06291v1.pdf)

---

## [24. Surv-IPTB: An Attention-Based Model for Estimating Individual Probability of Treatment Benefit with Survival Data](https://arxiv.org/abs/2608.06288v1)

**作者**：Lev V. Utkin, Stanislav K. Kogan, Andrei V. Konstantinov  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-08-06

### 📄 论文摘要

This work presents a novel attention-based framework for estimating the Individual Probability of Treatment Benefit (IPTB) in survival analysis contexts. The proposed model, called Surv-IPTB, directly quantifies the probability that a specific patient will experience extended survival time under treatment versus control. We reformulate IPTB estimation as a binary classification problem, leveraging pairwise patient comparisons across treatment and control cohorts. The framework incorporates a principled handling of right-censored observations through imprecise probability representations, where uncertain treatment effects are characterized by interval-valued probabilities. An attention mechanism with learnable query-key transformations enables flexible, data-driven aggregation of pairwise comparisons, while simultaneously learning soft class probabilities for censored cases. Through extensive experiments on synthetic datasets with complex nonlinear structures, including spiral, bell-shaped, and circular feature spaces, we demonstrate that our approach maintains robust performance across varying censoring rates and treatment effect strengths. The model consistently outperforms meta-learner baselines (T-learner and S-learner) equipped with random survival forests, Cox proportional hazards, and Beran estimators, particularly in challenging nonlinear scenarios where conventional methods exhibit significant degradation. The results establish the proposed attention-based framework as a scalable and statistically principled solution for personalized treatment benefit assessment in survival settings. The code implementing the model is publicly available.

### 🤖 AI 总结

**一句话总结**：This work presents a novel attention-based framework for estimating the Individual Probability of Treatment Benefit (IPTB) in survival analysis contexts. The proposed model, called Surv-IPTB, directly...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, of, Surv-IPTB, Attention-Based, Model, Estimating, Individual, Probability

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06288v1) | [下载PDF](https://arxiv.org/pdf/2608.06288v1.pdf)

---

## [25. The Tamed Subgradient Unadjusted Langevin Algorithm beyond Convexity](https://arxiv.org/abs/2608.06283v1)

**作者**：Iosif Lytras, Nikolaos Makras, Sotirios Sabanis  
**分类**：cs.LG, math.OC, math.PR, stat.ML  
**发布时间**：2026-08-06

### 📄 论文摘要

We study the problem of sampling from target distributions whose potentials are simultaneously non-smooth, subject to superlinear gradient growth, and non-convex. We introduce the Subgradient Tamed Unadjusted Langevin Algorithm (SG-TULA), a discretisation of the Langevin diffusion that operates directly on subgradients, without relying on computationally demanding smoothing procedures. To handle the superlinear regime, taming techniques are employed to produce a stable, explicit scheme. We derive non-asymptotic convergence bounds in Wasserstein-2 distance, with all constants tracked explicitly in terms of dimension and inverse temperature, improving upon the currently known rates for subgradient-based Langevin algorithms. We further provide excess risk estimates for the associated optimisation problem. We verify the assumptions, with explicit constants, for the regularized pretraining potential of a LLM in the GPT-2 lineage and the boosted coordinate-wise variant of SG-TULA pretrains the former competitively against finetuned AdamW and Muon, for which no comparable non-asymptotic guarantees are presently available.

### 🤖 AI 总结

**一句话总结**：We study the problem of sampling from target distributions whose potentials are simultaneously non-smooth, subject to superlinear gradient growth, and non-convex. We introduce the Subgradient Tamed Un...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Tamed, Subgradient, Unadjusted, Langevin, Algorithm, beyond, Convexity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06283v1) | [下载PDF](https://arxiv.org/pdf/2608.06283v1.pdf)

---

## [26. Hypothesis Testing with Conditional Queries: Learnability and the Value of Interaction](https://arxiv.org/abs/2608.06262v1)

**作者**：Zonghuan Xu  
**分类**：cs.LG, math.ST  
**发布时间**：2026-08-06

### 📄 论文摘要

Model evaluations may fix all tests before observing any responses or select later tests using earlier responses. We study this choice in a conditional-query model on a finite outcome space $\mathcal{X}$ with $|\mathcal{X}|=N$. We first ask which pairs of distribution classes can be reliably distinguished. We then ask how many additional queries are required to match an adaptive tester when all queried events must be fixed in advance. We show that learnability holds if and only if the two classes have positive separation in their pairwise conditional probabilities. When this separation is zero, the optimal worst-case error is exactly $1/2$ at every finite query budget. For any $T$-query adaptive policy and any $ρ\in (0,1)$, we construct a randomized non-adaptive procedure using $O(N^2(T + \log(1/ρ)))$ pair queries chosen before any response is observed. Its simulated transcript is within $ρ$ in total variation of the adaptive transcript, uniformly over all distributions in the model. We also construct a matching family with constant adaptive query complexity and $Ω_\varepsilon(N^2)$ non-adaptive query complexity. Consequently, the worst-case fixed-error adaptivity gap is $Θ_\varepsilon(N^2)$. Thus interaction can reduce the required number of tests by a quadratic factor, but the apparent exponential branching of an interactive evaluation does not yield an exponential query advantage.

### 🤖 AI 总结

**一句话总结**：Model evaluations may fix all tests before observing any responses or select later tests using earlier responses. We study this choice in a conditional-query model on a finite outcome space $\mathcal{...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Hypothesis, Testing, Conditional, Queries, Learnability, Value, Interaction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06262v1) | [下载PDF](https://arxiv.org/pdf/2608.06262v1.pdf)

---

## [27. RxnCLF: Contrastive Transformation-Aware Reaction Foundation Model for Improved Reactivity Prediction](https://arxiv.org/abs/2608.06259v1)

**作者**：Yiting Zheng, Cheng Fang, Anthony Donofrio 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-06

### 📄 论文摘要

Reaction yield prediction remains challenging because labeled data are scarce and reaction space is both combinatorially large and sparsely populated, limiting the generalization of existing reaction representations. String-, fingerprint-, and graph-based reaction encodings only partially capture chemical transformations, making accurate prediction difficult for reactions with complex substrates. We propose reaction contrastive learning foundation (RxnCLF), a self-supervised contrastive framework for reaction representation learning. RxnCLF is built on a condensed reaction graph (CRG) that unifies reactant and product information into a single graph, enabling the model to learn explicit and enriched transformation structure rather than disconnected graphs. Pretrained on 1.7 million Pistachio reactions, RxnCLF learns a compact and continuous latent space that captures both reaction-center features and broader side chain contexts, making it transformation-aware and chemically interpretable. Fine-tuned on multiple yield prediction benchmarks, including Buchwald-Hartwig, Pd-catalyzed BH coupling, and proprietary HTE C-N coupling and amide formation datasets, RxnCLF consistently outperforms graph and sequence-based baselines, improving R2 and achieving the best performance overall. Our results highlight the promise of CRG-based RxnCLF as a scalable reaction foundation model, with the potential to generalize across broader reaction spaces and support diverse downstream reaction informatics tasks, including regioselectivity prediction, enantioselectivity prediction, and reaction condition optimization.

### 🤖 AI 总结

**一句话总结**：Reaction yield prediction remains challenging because labeled data are scarce and reaction space is both combinatorially large and sparsely populated, limiting the generalization of existing reaction ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RxnCLF, Contrastive, Transformation-Aware, Reaction, Foundation, Model, Improved, Reactivity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06259v1) | [下载PDF](https://arxiv.org/pdf/2608.06259v1.pdf)

---

## [28. MetaboLLM: a metabolomics-specialized large language model for biochemical knowledge integration and predictive metabolite graph construction](https://arxiv.org/abs/2608.06253v1)

**作者**：Dohyun Ku, Min Gu Kwak, Francisco J. Pasquel 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-06

### 📄 论文摘要

Metabolomics knowledge is distributed across heterogeneous resources and remains difficult to translate into predictive representations. We developed MetaboLLM, a metabolomics-specialized large language model adapted through continual pretraining, supervised fine-tuning, and structured retrieval, together with MetaboLLM-GIN, which converts generated biochemical descriptions into metabolite graphs for patient-level prediction using a graph isomorphism network. Across four backbone families, MetaboLLM outperformed corresponding base and medically adapted models on metabolomics knowledge, relational, and description tasks, and transferred to an external public benchmark. MetaboLLM-GIN achieved the highest AUC for stress hyperglycemia prediction after coronary artery bypass grafting (0.8616) and postmenopausal hormone-regimen classification (0.8123), outperforming conventional models, alternative graph constructions, and graphs generated from unadapted or non-retrieval LLM configurations. Model interpretation further produced biologically meaningful findings in both applications. These results show that domain-specialized language models can organize heterogeneous biochemical knowledge into predictive and interpretable metabolite graph representations.

### 🤖 AI 总结

**一句话总结**：Metabolomics knowledge is distributed across heterogeneous resources and remains difficult to translate into predictive representations. We developed MetaboLLM, a metabolomics-specialized large langua...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MetaboLLM, metabolomics-specialized, large, language, model, biochemical, knowledge, integration

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06253v1) | [下载PDF](https://arxiv.org/pdf/2608.06253v1.pdf)

---

## [29. A Six-Dimensional Taxonomy of Post-Training Adaptation Techniques with Applications in AI Governance](https://arxiv.org/abs/2608.06246v1)

**作者**：Fardin Afdideh, Fernando Seoane, Farhad Abtahi  
**分类**：cs.LG  
**发布时间**：2026-08-06

### 📄 论文摘要

Post-training adaptation has become central to modern machine learning practice and includes techniques such as retraining, fine-tuning, parameter-efficient adaptation, alignment, retrieval augmentation, model editing, unlearning, calibration, and Multimodal Instruction Tuning. However, the literature remains fragmented across technique families, model classes, and deployment contexts, making it difficult to compare methods or describe how a trained model has been modified. This survey synthesizes the post-training adaptation literature and introduces a six-dimensional taxonomy organized by mechanism, goal, data requirement, persistence, structural scope, and model type. The taxonomy distinguishes commonly conflated terms such as fine-tuning, retrieval augmentation, and prompting, and shows how adaptation strategies evolve from traditional machine learning through deep learning, foundation models, large language models, and multimodal large language models. It also maps relationships among techniques, including inheritance, supersession, hybridization, and layered deployment stacks. The resulting vocabulary can support technical documentation, model-change tracking, and governance analysis. The survey concludes by identifying open challenges in evaluation, reproducibility, persistent inference-time adaptation, unlearning, multimodal adaptation, and governance-aware post-training workflows.

### 🤖 AI 总结

**一句话总结**：Post-training adaptation has become central to modern machine learning practice and includes techniques such as retraining, fine-tuning, parameter-efficient adaptation, alignment, retrieval augmentati...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Six-Dimensional, Taxonomy, Post-Training, Adaptation, Techniques, Applications, Governance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06246v1) | [下载PDF](https://arxiv.org/pdf/2608.06246v1.pdf)

---

## [30. Timestep-Conditioned Transformers for Global Weather Forecasting](https://arxiv.org/abs/2608.06241v1)

**作者**：Sam Levang, Fran Bartolic, Ty Dickinson 等 6 位作者  
**分类**：cs.LG, cs.OS  
**发布时间**：2026-08-06

### 📄 论文摘要

Existing machine-learning weather forecasting models rely on predetermined and fixed autoregressive timesteps. The choice of model timestep involves a fundamental trade-off: shorter timesteps (e.g. 1 to 6 hours) finely resolve atmospheric dynamics within the diurnal cycle but increase error accumulation for a given forecast horizon, while longer timesteps (e.g. 24 hours) reduce error accumulation but limit the usability of short-range forecasts where sub-daily predictability is high. In this work, we present GEM-3, a probabilistic global weather model that addresses this trade-off through explicit multi-timestep inference. With a single set of trained weights, the model timestep can be configured at inference time to balance predictability and usability across a broad forecast horizon. Additionally, we find that mixed-timestep training consistently improves rollout stability relative to timestep-specialist models. Under the hood, GEM-3 is a lightweight neighborhood-attention transformer with ~134M parameters on an equirectangular grid with a number of architectural advancements beyond its predecessor GEM-2. The result is a practical forecasting system that couples near-SOTA medium-range probabilistic skill, stable extended-range rollouts, efficient training and inference, and decision-relevant diagnostics.

### 🤖 AI 总结

**一句话总结**：Existing machine-learning weather forecasting models rely on predetermined and fixed autoregressive timesteps. The choice of model timestep involves a fundamental trade-off: shorter timesteps (e.g. 1 ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Timestep-Conditioned, Transformers, Global, Weather, Forecasting, Existing, machine-learning, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.06241v1) | [下载PDF](https://arxiv.org/pdf/2608.06241v1.pdf)

---

