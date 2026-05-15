# arXiv AI 论文日报 | 2026-05-15

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (15 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.CL](#csCL) (4 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation](https://arxiv.org/abs/2605.15177v1)

**作者**：Shang Zhou, Wenhao Chai, Kaiyuan Liu 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-14

### 📄 论文摘要

Test-time compute scaling is a primary axis for improving LLM reasoning. Existing methods primarily scale depth by extending a single reasoning trace. Scaling breadth by sampling multiple candidates in parallel is straightforward, but introduces a selection bottleneck: choosing the best candidate without a ground-truth verifier, since pointwise LLM judging is noisy and biased. To address this, we introduce OpenDeepThink, a population-based test-time compute framework that selects via pairwise Bradley-Terry comparison. Each generation, the LLM judges random pairs of candidates and aggregates votes via Bradley-Terry into a global ranking; top-ranked candidates are preserved and the top three quarters are mutated using the natural-language critiques produced during comparison; the bottom quarter is discarded. OpenDeepThink raises Gemini 3.1 Pro's effective Codeforces Elo by +405 points in eight sequential LLM-call rounds (~27 minutes wall-clock). The pipeline transfers across weaker and stronger models without retuning, and on the multi-domain HLE benchmark, gains appear concentrated in objectively verifiable domains and reverse in subjective ones. We release CF-73, a curated set of 73 expert-rated Codeforces problems with International Grandmaster annotation and 99% local-evaluation agreement against the official verdict.

### 🤖 AI 总结

**一句话总结**：Test-time compute scaling is a primary axis for improving LLM reasoning. Existing methods primarily scale depth by extending a single reasoning trace. Scaling breadth by sampling multiple candidates i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OpenDeepThink, Parallel, Reasoning, via, Bradley--Terry, Aggregation, Test-time, compute

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15177v1) | [下载PDF](https://arxiv.org/pdf/2605.15177v1.pdf)

---

## [2. APWA: A Distributed Architecture for Parallelizable Agentic Workflows](https://arxiv.org/abs/2605.15132v1)

**作者**：Evan Rose, Tushin Mallick, Matthew D. Laws 等 5 位作者  
**分类**：cs.AI, cs.DC, cs.MA  
**发布时间**：2026-05-14

### 📄 论文摘要

Autonomous multi-agent systems based on large language models (LLMs) have demonstrated remarkable abilities in independently solving complex tasks in a wide breadth of application domains. However, these systems hit critical reasoning, coordination, and computational scaling bottlenecks as the size and complexity of their tasks grow. These limitations hinder multi-agent systems from achieving high-throughput processing for highly parallelizable tasks, despite the availability of parallel computing and reasoning primitives in the underlying LLMs. We introduce the Agent-Parallel Workload Architecture (APWA), a distributed multi-agent system architecture designed for the efficient processing of heavily parallelizable agentic workloads. APWA facilitates parallel execution by decomposing workflows into non-interfering subproblems that can be processed using independent resources without cross-communication. It supports heterogeneous data and parallel processing patterns, and it accommodates tasks from a wide breadth of domains. In our evaluation, we demonstrate that APWA can dynamically decompose complex queries into parallelizable workflows and scales on larger tasks in settings where prior systems fail completely.

### 🤖 AI 总结

**一句话总结**：Autonomous multi-agent systems based on large language models (LLMs) have demonstrated remarkable abilities in independently solving complex tasks in a wide breadth of application domains. However, th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, APWA, Distributed, Architecture, Parallelizable, Agentic, Workflows, Autonomous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15132v1) | [下载PDF](https://arxiv.org/pdf/2605.15132v1.pdf)

---

## [3. Why Neighborhoods Matter: Traversal Context and Provenance in Agentic GraphRAG](https://arxiv.org/abs/2605.15109v1)

**作者**：Riccardo Terrenzi, Maximilian von Zastrow, Serkan Ayvaz  
**分类**：cs.AI, cs.IR  
**发布时间**：2026-05-14

### 📄 论文摘要

Retrieval-Augmented Generation can improve factuality by grounding answers in external evidence, but Agentic GraphRAG complicates what it means for citations to be faithful. In these systems, an agent explores a knowledge graph before producing an answer and a small set of citations. We frame citation faithfulness as a trajectory-level problem: final citations should not only support the answer, but also account for the graph traversal, structure, and visited-but-uncited entities that may influence it. Through controlled ablation experiments, we compare the effects of isolating, removing, and masking cited and uncited graph entities. Our results show that cited evidence is often necessary, as removing it substantially changes answers and reduces accuracy. However, citations are not sufficient, because accurate answers can also depend on uncited traversal context and surrounding graph structure. These findings suggest that citation evaluation in Agentic GraphRAG should move beyond source support toward provenance over the broader retrieval trajectory.

### 🤖 AI 总结

**一句话总结**：Retrieval-Augmented Generation can improve factuality by grounding answers in external evidence, but Agentic GraphRAG complicates what it means for citations to be faithful. In these systems, an agent...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Why, Neighborhoods, Matter, Traversal, Context, Provenance, Agentic, GraphRAG

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15109v1) | [下载PDF](https://arxiv.org/pdf/2605.15109v1.pdf)

---

## cs.CL

## [4. Is Grep All You Need? How Agent Harnesses Reshape Agentic Search](https://arxiv.org/abs/2605.15184v1)

**作者**：Sahil Sen, Akhil Kasturi, Elias Lumer 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-14

### 📄 论文摘要

Recent advances in Large Language Model (LLM) agents have enabled complex agentic workflows where models autonomously retrieve information, call tools, and reason over large corpora to complete tasks on behalf of users. Despite the growing adoption of retrieval-augmented generation (RAG) in agentic search systems, existing literature lacks a systematic comparison of how retrieval strategy choice interacts with agent architecture and tool-calling paradigm. Important practical dimensions, including how tool outputs are presented to the model and how performance changes when searches must cope with more irrelevant surrounding text, remain under-explored in agent loops. This paper reports an empirical study organized into two experiments. Experiment 1 compares grep and vector retrieval on a 116-question sample from LongMemEval, using a custom agent harness (Chronos) and provider-native CLI harnesses (Claude Code, Codex, and Gemini CLI), for both inline tool results and file-based tool results that the model reads separately. Experiment 2 compares grep-only and vector-only retrieval while progressively mixing in additional unrelated conversation history, so that each query is embedded in more distracting material alongside the passages that matter. Across Chronos and the provider CLIs, grep generally yields higher accuracy than vector retrieval in our comparisons in experiment 1; at the same time, overall scores still depend strongly on which harness and tool-calling style is used, even when the underlying conversation data are the same.

### 🤖 AI 总结

**一句话总结**：Recent advances in Large Language Model (LLM) agents have enabled complex agentic workflows where models autonomously retrieve information, call tools, and reason over large corpora to complete tasks ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Grep, All, Need?, How, Harnesses, Reshape, Agentic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15184v1) | [下载PDF](https://arxiv.org/pdf/2605.15184v1.pdf)

---

## [5. Text Knows What, Tables Know When: Clinical Timeline Reconstruction via Retrieval-Augmented Multimodal Alignment](https://arxiv.org/abs/2605.15168v1)

**作者**：Sayantan Kumar, Shahriar Noroozizadeh, Juyong Kim 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.LG, stat.ML  
**发布时间**：2026-05-14

### 📄 论文摘要

Reconstructing precise clinical timelines is essential for modeling patient trajectories and forecasting risk in complex, heterogeneous conditions like sepsis. While unstructured clinical narratives offer semantically rich and contextually complete descriptions of a patient's course, they often lack temporal precision and contain ambiguous event timing. Conversely, structured electronic health record (EHR) data provides precise temporal anchors but misses a substantial portion of clinically meaningful events. We introduce a retrieval-augmented multimodal alignment framework that bridges this gap to improve the temporal precision of absolute clinical timelines extracted from text. Our approach formulates timeline reconstruction as a graph-based multistep process: it first extracts central anchor events from narratives to build an initial temporal scaffold, places non-central events relative to this backbone, and then calibrates the timeline using retrieved structured EHR rows as external temporal evidence. Evaluated using instruction-tuned large language models on the i2m4 benchmark spanning MIMIC-III and MIMIC-IV, our multimodal pipeline consistently improves absolute timestamp accuracy (AULTC) and improves temporal concordance across nearly all evaluated models over unimodal text-only reconstruction, without compromising event match rates. Furthermore, our empirical gap analysis reveals that 34.8% of text-derived events are entirely absent from tabular records, demonstrating that aligning these modalities can produce a more temporally faithful and clinically informative reconstruction of patient trajectories than either source alone.

### 🤖 AI 总结

**一句话总结**：Reconstructing precise clinical timelines is essential for modeling patient trajectories and forecasting risk in complex, heterogeneous conditions like sepsis. While unstructured clinical narratives o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Text, Knows, What, Tables, Know, When, Clinical, Timeline

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15168v1) | [下载PDF](https://arxiv.org/pdf/2605.15168v1.pdf)

---

## [6. MeMo: Memory as a Model](https://arxiv.org/abs/2605.15156v1)

**作者**：Ryan Wei Heng Quek, Sanghyuk Lee, Alfred Wei Lun Leong 等 9 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-05-14

### 📄 论文摘要

Large language models (LLMs) achieve strong performance across a wide range of tasks, but remain frozen after pretraining until subsequent updates. Many real-world applications require timely, domain-specific information, motivating the need for efficient mechanisms to incorporate new knowledge. In this paper, we introduce MeMo (Memory as a Model), a modular framework that encodes new knowledge into a dedicated memory model while keeping the LLM parameters unchanged. Compared to existing methods, MeMo offers several advantages: (a) it captures complex cross-document relationships, (b) it is robust to retrieval noise, (c) it avoids catastrophic forgetting in the LLM, (d) it does not require access to the LLM's weights or output logits, enabling plug-and-play integration with both open and proprietary closed-source LLMs, and (e) its retrieval cost is independent of corpus size at inference time. Our experimental results on three benchmarks, BrowseComp-Plus, NarrativeQA, and MuSiQue, show that MeMo achieves strong performance compared to existing methods across diverse settings.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) achieve strong performance across a wide range of tasks, but remain frozen after pretraining until subsequent updates. Many real-world applications require timely, domain-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, LLM, MeMo, Memory, Model, Large, language, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15156v1) | [下载PDF](https://arxiv.org/pdf/2605.15156v1.pdf)

---

## [7. From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents](https://arxiv.org/abs/2605.15104v1)

**作者**：Md Tahmid Rahman Laskar, Xue-Yong Fu, Seyyed Saeed Sarfjoo 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-14

### 📄 论文摘要

Voice agents increasingly require reliable tool use from speech, whereas prominent tool-calling benchmarks remain text-based. We study whether verified text benchmarks can be converted into controlled audio-based tool calling evaluations without re-annotating the tool schema and gold labels. Our dataset-agnostic framework uses text-to-speech, speaker variation, and environmental noise to create paired text-audio instances while preserving the original dataset annotations. Based on extensive evaluation of 7 omni-modal models on audio-converted versions of Confetti and When2Call, our framework demonstrates that the performance is strongly model- and task-dependent: Gemini-3.1-Flash-Live obtains the highest Confetti score (70.4), whereas GPT-Realtime-1.5 performs best on When2Call (71.9). On Confetti, the text-to-voice gap ranges from 1.8 points for Qwen3-Omni to 4.8 points for GPT-Realtime-1.5. A targeted analysis of failure cases demonstrates that degradations most often reflect misunderstandings of argument values in the speech. Considering real-world deployment scenarios, we further report text-only results, an ambiguity-based reformulation stress test, and a reference-free LLM-as-judge protocol validated against human preferences. Notably, we find that open-source Qwen3 judges with at least 8B parameters exceed 80% agreement with proprietary judges, supporting privacy-preserving evaluation. Overall, our framework provides a verifiable and reproducible first-stage diagnostic that complements purpose-built audio corpora.

### 🤖 AI 总结

**一句话总结**：Voice agents increasingly require reliable tool use from speech, whereas prominent tool-calling benchmarks remain text-based. We study whether verified text benchmarks can be converted into controlled...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Text, Voice, Reproducible, Verifiable, Framework, Evaluating, Tool, Calling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15104v1) | [下载PDF](https://arxiv.org/pdf/2605.15104v1.pdf)

---

## cs.CV

## [8. EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation](https://arxiv.org/abs/2605.15199v1)

**作者**：Ruozhen He, Meng Wei, Ziyan Yang 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-14

### 📄 论文摘要

Multi-shot video generation extends single-shot generation to coherent visual narratives, yet maintaining consistent characters, objects, and locations across shots remains a challenge over long sequences. Existing evaluations typically use independently generated prompt sets with limited entity coverage and simple consistency metrics, making standardized comparison difficult. We introduce EntityBench, a benchmark of 140 episodes (2,491 shots) derived from real narrative media, with explicit per-shot entity schedules tracking characters, objects, and locations simultaneously across easy / medium / hard tiers of up to 50 shots, 13 cross-shot characters, 8 cross-shot locations, 22 cross-shot objects, and recurrence gaps spanning up to 48 shots. It is paired with a three-pillar evaluation suite that disentangles intra-shot quality, prompt-following alignment, and cross-shot consistency, with a fidelity gate that admits only accurate entity appearances into cross-shot scoring. As a baseline, we propose EntityMem, a memory-augmented generation system that stores verified per-entity visual references in a persistent memory bank before generation begins. Experiments show that cross-shot entity consistency degrades sharply with recurrence distance in existing methods, and that explicit per-entity memory yields the highest character fidelity (Cohen's d = +2.33) and presence among methods evaluated. Code and data are available at https://github.com/Catherine-R-He/EntityBench/.

### 🤖 AI 总结

**一句话总结**：Multi-shot video generation extends single-shot generation to coherent visual narratives, yet maintaining consistent characters, objects, and locations across shots remains a challenge over long seque...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EntityBench, Towards, Entity-Consistent, Long-Range, Multi-Shot, Video, Generation, extends

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15199v1) | [下载PDF](https://arxiv.org/pdf/2605.15199v1.pdf)

---

## [9. VGGT-$Ω$](https://arxiv.org/abs/2605.15195v1)

**作者**：Jianyuan Wang, Minghao Chen, Shangzhan Zhang 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-14

### 📄 论文摘要

Recent feed-forward reconstruction models, such as VGGT, have proven competitive with traditional optimization-based reconstructors while also providing geometry-aware features useful for other tasks. Here, we show that the quality of these models scales predictably with model and data size. We do so by introducing VGGT-$Ω$, which substantially improves reconstruction accuracy, efficiency, and capabilities for both static and dynamic scenes. To enable training this model at an unprecedented scale, we introduce architectural changes that improve training efficiency, a high-quality data annotation pipeline that supports dynamic scenes, and a self-supervised learning protocol. We simplify VGGT's architecture by using a single dense prediction head with multi-task supervision and removing the expensive high-resolution convolutional layers. We also use registers to aggregate scene information into a compact representation and introduce register attention, which restricts inter-frame information exchange to these registers, in part replacing global attention. In this way, during training, VGGT-$Ω$ uses only about 30% of the GPU memory of its predecessor, allowing us to train with 15x more supervised data than prior work and to leverage vast amounts of unlabeled video data. VGGT-$Ω$ achieves strong results for reconstruction of static and dynamic scenes across multiple benchmarks, for example, improving over the previous best camera estimation accuracy on Sintel by 77%. We also show that the learned registers can improve vision-language-action models and support alignment with language, suggesting that reconstruction can be a powerful and scalable proxy task for spatial understanding. Project Page: http://vggt-omega.github.io/

### 🤖 AI 总结

**一句话总结**：Recent feed-forward reconstruction models, such as VGGT, have proven competitive with traditional optimization-based reconstructors while also providing geometry-aware features useful for other tasks....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, VGGT-$Ω$, Recent, feed-forward, reconstruction, models, such, VGGT

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15195v1) | [下载PDF](https://arxiv.org/pdf/2605.15195v1.pdf)

---

## [10. RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO](https://arxiv.org/abs/2605.15190v1)

**作者**：Yanzuo Lu, Ronglai Zuo, Jiankang Deng  
**分类**：cs.CV  
**发布时间**：2026-05-14

### 📄 论文摘要

Causal autoregressive video diffusion models support real-time streaming generation by extrapolating future chunks from previously generated content. Distilling such generators from high-fidelity bidirectional teachers yields competitive few-step models, yet a persistent gap between the history distributions encountered during training and those arising at inference constrains generation quality over long horizons. We introduce the Real-time Autoregressive Video Extrapolation Network (RAVEN), a training-time test framework that repacks each self rollout into an interleaved sequence of clean historical endpoints and noisy denoising states. This formulation aligns training attention with inference-time extrapolation and allows downstream chunk losses to supervise the history representations on which future predictions depend. We further propose Consistency-model Group Relative Policy Optimization (CM-GRPO), which reformulates a consistency sampling step as a conditional Gaussian transition and applies online Reinforcement Learning (RL) directly to this kernel, avoiding the Euler-Maruyama auxiliary process adopted in prior flow-model RL formulations. Experiments demonstrate that RAVEN surpasses recent causal video distillation baselines across quality, semantic, and dynamic degree evaluations, and that CM-GRPO provides further gains when combined with RAVEN.

### 🤖 AI 总结

**一句话总结**：Causal autoregressive video diffusion models support real-time streaming generation by extrapolating future chunks from previously generated content. Distilling such generators from high-fidelity bidi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RAVEN, Real-time, Autoregressive, Video, Extrapolation, Consistency-model, GRPO, Causal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15190v1) | [下载PDF](https://arxiv.org/pdf/2605.15190v1.pdf)

---

## [11. Articraft: An Agentic System for Scalable Articulated 3D Asset Generation](https://arxiv.org/abs/2605.15187v1)

**作者**：Matt Zhou, Ruining Li, Xiaoyang Lyu 等 9 位作者  
**分类**：cs.CV, cs.GR, cs.RO  
**发布时间**：2026-05-14

### 📄 论文摘要

A bottleneck in learning to understand articulated 3D objects is the lack of large and diverse datasets. In this paper, we propose to leverage large language models (LLMs) to close this gap and generate articulated assets at scale. We reduce the problem of generating an articulated 3D asset to that of writing a program that builds it. We then introduce a new agentic system, Articraft, that writes such programs automatically. We design a programmatic interface and harness to help the LLM do so effectively. The LLM writes code against a domain-specific SDK for defining parts, composing geometry, specifying joints, and writing tests to validate the resulting assets. The harness exposes a restricted workspace and interface to the LLM, validates the resulting assets, and returns structured feedback. In this way, the LLM is not distracted by details such as authoring a URDF file or managing a complex software environment. We show that this produces higher-quality assets than both state-of-the-art articulated-asset generators and general-purpose coding agents. Using Articraft, we build Articraft-10K, a curated dataset of over 10K articulated assets spanning 245 categories, and show its utility both for training models of articulated assets and in downstream applications such as robotics simulation and virtual reality.

### 🤖 AI 总结

**一句话总结**：A bottleneck in learning to understand articulated 3D objects is the lack of large and diverse datasets. In this paper, we propose to leverage large language models (LLMs) to close this gap and genera...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, 3D, Articraft, Agentic, System, Scalable, Articulated, Asset

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15187v1) | [下载PDF](https://arxiv.org/pdf/2605.15187v1.pdf)

---

## [12. VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction](https://arxiv.org/abs/2605.15186v1)

**作者**：Kaixin Zhu, Yiwen Tang, Yifan Yang 等 12 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-14

### 📄 论文摘要

High-quality 3D scene reconstruction has recently advanced toward generalizable feed-forward architectures, enabling the generation of complex environments in a single forward pass. However, despite their strong performance in static scene perception, these models remain limited in responding to dynamic human instructions, which restricts their use in interactive applications. Existing editing methods typically rely on a 2D-lifting strategy, where individual views are edited independently and then lifted back into 3D space. This indirect pipeline often leads to blurry textures and inconsistent geometry, as 2D editors lack the spatial awareness required to preserve structure across viewpoints. To address these limitations, we propose VGGT-Edit, a feed-forward framework for text-conditioned native 3D scene editing. VGGT-Edit introduces depth-synchronized text injection to align semantic guidance with the backbone's spatial poses, ensuring stable instruction grounding. This semantic signal is then processed by a residual transformation head, which directly predicts 3D geometric displacements to deform the scene while preserving background stability. To ensure high-fidelity results, we supervise the framework with a multi-term objective function that enforces geometric accuracy and cross-view consistency. We also construct the DeltaScene Dataset, a large-scale dataset generated through an automated pipeline with 3D agreement filtering to ensure ground-truth quality. Experiments show that VGGT-Edit substantially outperforms 2D-lifting baselines, producing sharper object details, stronger multi-view consistency, and near-instant inference speed.

### 🤖 AI 总结

**一句话总结**：High-quality 3D scene reconstruction has recently advanced toward generalizable feed-forward architectures, enabling the generation of complex environments in a single forward pass. However, despite t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, VGGT-Edit, Feed-forward, Native, Scene, Editing, Residual, Field

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15186v1) | [下载PDF](https://arxiv.org/pdf/2605.15186v1.pdf)

---

## [13. Quantitative Video World Model Evaluation for Geometric-Consistency](https://arxiv.org/abs/2605.15185v1)

**作者**：Jiaxin Wu, Yihao Pi, Yinling Zhang 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-14

### 📄 论文摘要

Generative video models are increasingly studied as implicit world models, yet evaluating whether they produce physically plausible 3D structure and motion remains challenging. Most existing video evaluation pipelines rely heavily on human judgment or learned graders, which can be subjective and weakly diagnostic for geometric failures. We introduce PDI-Bench (Perspective Distortion Index), a quantitative framework for auditing geometric coherence in generated videos. Given a generated clip, we obtain object-centric observations via segmentation and point tracking (e.g., SAM 2, MegaSaM, and CoTracker3), lift them to 3D world-space coordinates via monocular reconstruction, and compute a set of projective-geometry residuals capturing three failure dimensions: scale-depth alignment, 3D motion consistency, and 3D structural rigidity. To support systematic evaluation, we build PDI-Dataset, covering diverse scenarios designed to stress these geometric constraints. Across state-of-the-art video generators, PDI reveals consistent geometry-specific failure modes that are not captured by common perceptual metrics, and provides a diagnostic signal for progress toward physically grounded video generation and physical world model. Our code and dataset can be found at https://pdi-bench.github.io/.

### 🤖 AI 总结

**一句话总结**：Generative video models are increasingly studied as implicit world models, yet evaluating whether they produce physically plausible 3D structure and motion remains challenging. Most existing video eva...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Quantitative, Video, World, Model, Evaluation, Geometric-Consistency, Generative, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15185v1) | [下载PDF](https://arxiv.org/pdf/2605.15185v1.pdf)

---

## [14. From Plans to Pixels: Learning to Plan and Orchestrate for Open-Ended Image Editing](https://arxiv.org/abs/2605.15181v1)

**作者**：Anirudh Sundara Rajan, Krishna Kumar Singh, Yong Jae Lee  
**分类**：cs.CV  
**发布时间**：2026-05-14

### 📄 论文摘要

Modern image editing models produce realistic results but struggle with abstract, multi step instructions (e.g., ``make this advertisement more vegetarian-friendly''). Prior agent based methods decompose such tasks but rely on handcrafted pipelines or teacher imitation, limiting flexibility and decoupling learning from actual editing outcomes. We propose an experiential framework for long-horizon image editing, where a planner generates structured atomic decompositions and an orchestrator selects tools and regions to execute each step. A vision language judge provides outcome-based rewards for instruction adherence and visual quality. The orchestrator is trained to maximize these rewards, and successful trajectories are used to refine the planner. By tightly coupling planning with reward driven execution, our approach yields more coherent and reliable edits than single-step or rule-based multistep baselines.

### 🤖 AI 总结

**一句话总结**：Modern image editing models produce realistic results but struggle with abstract, multi step instructions (e.g., ``make this advertisement more vegetarian-friendly''). Prior agent based methods decomp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Plans, Pixels, Learning, Plan, Orchestrate, Open-Ended, Image, Editing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15181v1) | [下载PDF](https://arxiv.org/pdf/2605.15181v1.pdf)

---

## [15. SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer](https://arxiv.org/abs/2605.15178v1)

**作者**：Haoyi Zhu, Haozhe Liu, Yuyang Zhao 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-14

### 📄 论文摘要

We introduce SANA-WM, an efficient 2.6B-parameter open-source world model natively trained for one-minute generation, synthesizing high-fidelity, 720p, minute-scale videos with precise camera control. SANA-WM achieves visual quality comparable to large-scale industrial baselines such as LingBot-World and HY-WorldPlay, while significantly improving efficiency. Four core designs drive our architecture: (1) Hybrid Linear Attention combines frame-wise Gated DeltaNet (GDN) with softmax attention for memory-efficient long-context modeling. (2) Dual-Branch Camera Control ensures precise 6-DoF trajectory adherence. (3) Two-Stage Generation Pipeline applies a long-video refiner to stage-1 outputs, improving quality and consistency across sequences. (4) Robust Annotation Pipeline extracts accurate metric-scale 6-DoF camera poses from public videos to yield high-quality, spatiotemporally consistent action labels. Driven by these designs, SANA-WMdemonstrates remarkable efficiency across data, training compute, and inference hardware: it uses only $\sim$213K public video clips with metric-scale pose supervision, completes training in 15 days on 64 H100s, and generates each 60s clip on a single GPU; its distilled variant can be deployed on a single RTX 5090 with NVFP4 quantization to denoise a 60s 720p clip in 34s. On our one-minute world-model benchmark, SANA-WM demonstrates stronger action-following accuracy than prior open-source baselines and achieves comparable visual quality at $36\times$ higher throughput for scalable world modeling.

### 🤖 AI 总结

**一句话总结**：We introduce SANA-WM, an efficient 2.6B-parameter open-source world model natively trained for one-minute generation, synthesizing high-fidelity, 720p, minute-scale videos with precise camera control....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, SANA-WM, Efficient, Minute-Scale, World, Modeling, Hybrid, Linear

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15178v1) | [下载PDF](https://arxiv.org/pdf/2605.15178v1.pdf)

---

## [16. Evidential Reasoning Advances Interpretable Real-World Disease Screening](https://arxiv.org/abs/2605.15171v1)

**作者**：Chenyu Lian, Hong-Yu Zhou, Jing Qin  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-05-14

### 📄 论文摘要

Disease screening is critical for early detection and timely intervention in clinical practice. However, most current screening models for medical images suffer from limited interpretability and suboptimal performance. They often lack effective mechanisms to reference historical cases or provide transparent reasoning pathways. To address these challenges, we introduce EviScreen, an evidential reasoning framework for disease screening that leverages region-level evidence from historical cases. The proposed EviScreen offers retrospection interpretability through regional evidence retrieved from dual knowledge banks. Using this evidential mechanism, the subsequent evidence-aware reasoning module makes predictions using both the current case and evidence from historical cases, thereby enhancing disease screening performance. Furthermore, rather than relying on post-hoc saliency maps, EviScreen enhances localization interpretability by leveraging abnormality maps derived from contrastive retrieval. Our method achieves superior performance on our carefully established benchmarks for real-world disease screening, yielding notably higher specificity at clinical-level recall. Code is publicly available at https://github.com/DopamineLcy/EviScreen.

### 🤖 AI 总结

**一句话总结**：Disease screening is critical for early detection and timely intervention in clinical practice. However, most current screening models for medical images suffer from limited interpretability and subop...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Evidential, Reasoning, Advances, Interpretable, Real-World, Disease, Screening, critical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15171v1) | [下载PDF](https://arxiv.org/pdf/2605.15171v1.pdf)

---

## [17. Does Synthetic Layered Design Data Benefit Layered Design Decomposition?](https://arxiv.org/abs/2605.15167v1)

**作者**：Kam Man Wu, Haolin Yang, Qingyu Chen 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-14

### 📄 论文摘要

Recent advances in image generation have made it easy to produce high-quality images. However, these outputs are inherently flattened, entangling foreground elements, background, and text within a fixed canvas. As a result, flexible post-generation editing remains challenging, revealing a clear last-mile gap toward practical usability. Existing approaches either rely on scarce proprietary layered assets or construct partially synthetic data from limited structural priors. However, both strategies face fundamental challenges in scalability. In this work, we investigate whether pure synthetic layered data can improve graphic design decomposition. We make the assumption that, in graphic design, effective decomposition does not require modeling inter-layer dependencies as precisely as in natural-image composition, since design elements are often intentionally arranged as modular and semantically separable components. Concretely, we conduct a data-centric study based on CLD baseline, which is a state-of-the-art layer decomposition framework. Based on the baseline, we construct our own synthetic dataset, SynLayers, generate textual supervision using vision language models, and automate inference inputs with VLM-predicted bounding boxes. Our study reveals three key findings: (1) even training with purely synthetic data can outperform non-scalable alternatives such as the widely used PrismLayersPro dataset, demonstrating its viability as a scalable and effective substitute; (2) performance consistently improves with increased training data scale, while gains begin to saturate at around 50K samples; and (3) synthetic data enables balanced control over layer-count distributions, avoiding the layer-count imbalance commonly observed in real-world datasets. We hope this data-centric study encourages broader adoption of synthetic data as a practical foundation for layered design editing systems.

### 🤖 AI 总结

**一句话总结**：Recent advances in image generation have made it easy to produce high-quality images. However, these outputs are inherently flattened, entangling foreground elements, background, and text within a fix...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Does, Synthetic, Layered, Design, Data, Benefit, Decomposition?, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15167v1) | [下载PDF](https://arxiv.org/pdf/2605.15167v1.pdf)

---

## [18. Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141v1)

**作者**：Min Zhao, Hongzhou Zhu, Kaiwen Zheng 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-14

### 📄 论文摘要

Real-time interactive video generation requires low-latency, streaming, and controllable rollout. Existing autoregressive (AR) diffusion distillation methods have achieved strong results in the chunk-wise 4-step regime by distilling bidirectional base models into few-step AR students, but they remain limited by coarse response granularity and non-negligible sampling latency. In this paper, we study a more aggressive setting: frame-wise autoregression with only 1--2 sampling steps. In this regime, we identify the initialization of a few-step AR student as the key bottleneck: existing strategies are either target-misaligned, incapable of few-step generation, or too costly to scale. We propose \textbf{Causal Forcing++}, a principled and scalable pipeline that uses \emph{causal consistency distillation} (causal CD) for few-step AR initialization. The core idea is that causal CD learns the same AR-conditional flow map as causal ODE distillation, but obtains supervision from a single online teacher ODE step between adjacent timesteps, avoiding the need to precompute and store full PF-ODE trajectories. This makes the initialization both more efficient and easier to optimize. The resulting pipeline, \ours, surpasses the SOTA 4-step chunk-wise Causal Forcing under the \textit{\textbf{frame-wise 2-step setting}} by 0.1 in VBench Total, 0.3 in VBench Quality, and 0.335 in VisionReward, while reducing first-frame latency by 50\% and Stage 2 training cost by $\sim$$4\times$. We further extend the pipeline to action-conditioned world model generation in the spirit of Genie3. Project Page: https://github.com/thu-ml/Causal-Forcing and https://github.com/shengshu-ai/minWM .

### 🤖 AI 总结

**一句话总结**：Real-time interactive video generation requires low-latency, streaming, and controllable rollout. Existing autoregressive (AR) diffusion distillation methods have achieved strong results in the chunk-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Causal, Forcing++, Scalable, Few-Step, Autoregressive, Distillation, Real-Time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15141v1) | [下载PDF](https://arxiv.org/pdf/2605.15141v1.pdf)

---

## [19. MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory](https://arxiv.org/abs/2605.15128v1)

**作者**：Minghao Guo, Qingyue Jiao, Zeru Shi 等 17 位作者  
**分类**：cs.CV, cs.CL, cs.IR  
**发布时间**：2026-05-14

### 📄 论文摘要

Long-term agent memory is increasingly multimodal, yet existing evaluations rarely test whether agents preserve the visual evidence needed for later reasoning. In prior work, many visually grounded questions can be answered using only captions or textual traces, allowing answers to be inferred without preserving the fine-grained visual evidence. Meanwhile, harder cases that require reasoning over changing visual states are largely absent. Therefore, we introduce MemEye, a framework that evaluates memory capabilities from two dimensions: one measures the granularity of decisive visual evidence (from scene-level to pixel-level evidence), and the other measures how retrieved evidence must be used (from single evidence to evolutionary synthesis). Under this framework, we construct a new benchmark across 8 life-scenario tasks, with ablation-driven validation gates for assessing answerability, shortcut resistance, visual necessity, and reasoning structure. By evaluating 13 memory methods across 4 VLM backbones, we show that current architectures still struggle to preserve fine-grained visual details and reason about state changes over time. Our findings show that long-term multimodal memory depends on evidence routing, temporal tracking, and detail extraction.

### 🤖 AI 总结

**一句话总结**：Long-term agent memory is increasingly multimodal, yet existing evaluations rarely test whether agents preserve the visual evidence needed for later reasoning. In prior work, many visually grounded qu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, MemEye, Visual-Centric, Evaluation, Framework, Multimodal, Memory, Long-term

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15128v1) | [下载PDF](https://arxiv.org/pdf/2605.15128v1.pdf)

---

## [20. DriveCtrl: Conditioned Sim-to-Real Driving Video Generation](https://arxiv.org/abs/2605.15116v1)

**作者**：Haonan Zhao, Yiting Wang, Jingkun Chen 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-14

### 📄 论文摘要

Large-scale labelled driving video data is essential for training autonomous driving systems. Although simulation offers scalable and fully annotated data, the domain gap between synthetic and real-world driving videos significantly limits its utility for downstream deployment. Existing video generation methods are not well-suited for this task, as they fail to simultaneously preserve scene structure, object dynamics, temporal consistency, and visual realism, all of which are critical for maintaining annotation validity in generated data. In this paper, we present DriveCtrl, a depth-conditioned controllable sim-to-real video generation framework for realistic driving video synthesis. Built upon a pretrained video foundation model, DriveCtrl introduces a structure-aware adapter that enables depth-guided generation while preserving the scene layout and motion patterns of the source simulation, producing temporally coherent driving videos that remain aligned with the original simulated sequences. We further introduce a scalable data generation pipeline that transforms simulator videos into realistic driving footage matching the visual style of a target real-world dataset. The pipeline supports three conditioning signals: structural depth, reference-dataset style, and text prompts, while preserving frame-level annotations for downstream perception tasks. To better assess this task, we propose a driving-domain-specific knowledge-informed evaluation metric called Driving Video Realism Score (DVRS) that assesses the realism of generated videos. Experiments demonstrate that DriveCtrl consistently outperforms the base model and competing alternatives in realism, temporal quality, and perception task performance, substantially narrowing the sim-to-real gap for driving video generation.

### 🤖 AI 总结

**一句话总结**：Large-scale labelled driving video data is essential for training autonomous driving systems. Although simulation offers scalable and fully annotated data, the domain gap between synthetic and real-wo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DriveCtrl, Conditioned, Sim-to-Real, Driving, Video, Generation, Large-scale, labelled

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15116v1) | [下载PDF](https://arxiv.org/pdf/2605.15116v1.pdf)

---

## [21. CoralLite: μCT Reconstruction of Coral Colonies from Individual Corallites](https://arxiv.org/abs/2605.15093v1)

**作者**：Jess Jones, Leonardo Bertini, Kenneth Johnson 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-14

### 📄 论文摘要

The life history of an individual coral is archived within the accreting skeleton of the colony. While reef-forming coral colonies (e.g. massive \emph{Porites} sp.) may live for hundreds of years and deposit calcareous structures many metres in height and width, their living tissue is a thin outer surface layer comprised of asexually-dividing polyps that only survive a few years. To understand the rate and timing of polyp division and the consequences for colony skeletal growth, scientists need to track the skeletal corallite deposited around each polyp. Here we propose CoralLite, an annotated μCT scan dataset of entire calcareous skeletons and an associated, first corallite deep learning reconstruction baseline. CoralLite combines fully quantified volumetric segmentations with cross-slice linking for visualisations of 3D models for each corallite up to colony scale. For segmentation, we propose and evaluate in detail a hybrid V-Trans-UNet architecture applicable to segmenting tiled μCT virtual slabs of \emph{Porites} sp. colonies. The model is pre-trained on weakly annotated data and topology-aware fine-tuned using fully annotated slice sections with 8k+ manual corallite region annotations. On unseen slices of the same colony, the resulting model reaches 0.94 topological accuracy at mean Dice scores of 0.77 on the same colony and projection axis, and 0.63 mean Dice scores on a different, biologically unrelated specimen. Whilst our experiments are limited in scale and context, our results show for the first time that visual machine learning can effectively support full 3D individual corallite modelling from μCT scans of coral skeletons alone. For reproducibility and as a baseline for future research we publish our full dataset of 697 μCT slices, 37 partial or full slice annotations, and all network weights and source code with this paper.

### 🤖 AI 总结

**一句话总结**：The life history of an individual coral is archived within the accreting skeleton of the colony. While reef-forming coral colonies (e.g. massive \emph{Porites} sp.) may live for hundreds of years and ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：μCT, of, CoralLite, Reconstruction, Coral, Colonies, Individual, Corallites

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15093v1) | [下载PDF](https://arxiv.org/pdf/2605.15093v1.pdf)

---

## [22. SAGE3D: Soft-guided attention and graph excitation for 3D point cloud corner detection](https://arxiv.org/abs/2605.15088v1)

**作者**：Batuhan Arda Bekar, Can Sarı, Hüseyin Can Gülkan 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-14

### 📄 论文摘要

We present SAGE3D, a hybrid Transformer-based model for corner detection in airborne LiDAR point clouds. We propose a multi-stage solution built on a hierarchical encoder-decoder architecture that progressively downsamples point clouds through Set Abstraction layers and recovers per-point predictions via Feature Propagation. We introduce two innovations: Soft-Guided Attention, which injects ground-truth corner labels as a log-prior into attention logits during training to improve precision; then an Excitatory Graph Neural Network positioned at strategic resolutions in the hierarchy, employing positive-only message passing where high-confidence corners reinforce predictions through learned boosting, optimizing for recall. The hierarchical design enables multi-scale feature extraction while our guided attention and excitatory modules ensure corner signals are amplified rather than diluted across scales.

### 🤖 AI 总结

**一句话总结**：We present SAGE3D, a hybrid Transformer-based model for corner detection in airborne LiDAR point clouds. We propose a multi-stage solution built on a hierarchical encoder-decoder architecture that pro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, SAGE3D, Soft-guided, attention, graph, excitation, point, cloud

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15088v1) | [下载PDF](https://arxiv.org/pdf/2605.15088v1.pdf)

---

## cs.LG

## [23. FutureSim: Replaying World Events to Evaluate Adaptive Agents](https://arxiv.org/abs/2605.15188v1)

**作者**：Shashwat Goel, Nikhil Chandak, Arvindh Arun 等 8 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-05-14

### 📄 论文摘要

AI agents are being increasingly deployed in dynamic, open-ended environments that require adapting to new information as it arrives. To efficiently measure this capability for realistic use-cases, we propose building grounded simulations that replay real-world events in the order they occurred. We build FutureSim, where agents forecast world events beyond their knowledge cutoff while interacting with a chronological replay of the world: real news articles arriving and questions resolving over the simulated period. We evaluate frontier agents in their native harness, testing their ability to predict world events over a three-month period from January to March 2026. FutureSim reveals a clear separation in their capabilities, with the best agent's accuracy being 25%, and many having worse Brier skill score than making no prediction at all. Through careful ablations, we show how FutureSim offers a realistic setting to study emerging research directions like long-horizon test-time adaptation, search, memory, and reasoning about uncertainty. Overall, we hope our benchmark design paves the way to measure AI progress on open-ended adaptation spanning long time-horizons in the real world.

### 🤖 AI 总结

**一句话总结**：AI agents are being increasingly deployed in dynamic, open-ended environments that require adapting to new information as it arrives. To efficiently measure this capability for realistic use-cases, we...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, FutureSim, Replaying, World, Events, Evaluate, Adaptive, being

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15188v1) | [下载PDF](https://arxiv.org/pdf/2605.15188v1.pdf)

---

## [24. When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability](https://arxiv.org/abs/2605.15183v1)

**作者**：ML Nissen Gonzalez, Melwina Albuquerque, Laurence Wroe 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-14

### 📄 论文摘要

Mechanistic interpretability aims to break models into meaningful parts; verifying that two such parts implement the same computation is a prerequisite. Existing similarity measures evaluate either empirical behaviour, leaving them blind to out-of-distribution mechanisms, or basis-dependent parameters, meaning they disregard weight-space symmetries. To address these issues for the class of tensor-based models, we introduce a weight-based metric, tensor similarity, that is invariant to such symmetries. This metric captures global functional equivalence and accounts for cross-layer mechanisms using an efficient recursive algorithm. Empirically, tensor similarity tracks functional training dynamics, such as grokking and backdoor insertion, with higher fidelity than existing metrics. This reduces measuring similarity and verifying faithfulness into a solved algebraic problem rather than one of empirical approximation.

### 🤖 AI 总结

**一句话总结**：Mechanistic interpretability aims to break models into meaningful parts; verifying that two such parts implement the same computation is a prerequisite. Existing similarity measures evaluate either em...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Two, Networks, Same?, Tensor, Similarity, Mechanistic, Interpretability

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15183v1) | [下载PDF](https://arxiv.org/pdf/2605.15183v1.pdf)

---

## [25. Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands](https://arxiv.org/abs/2605.15164v1)

**作者**：Pratinav Seth, Vinay Kumar Sankarapu  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-14

### 📄 论文摘要

This position paper argues that behavioural assurance, even when carefully designed, is being asked to carry safety claims it cannot verify. AI governance frameworks enacted between 2019 and early 2026 require reviewable evidence of properties such as the absence of hidden objectives, resistance to loss-of-control precursors, and bounded catastrophic capability; current assurance methodologies (primarily behavioural evaluations and red-teaming) are epistemically limited to observable model outputs and cannot verify the latent representations or long-horizon agentic behaviours these frameworks presume to regulate. We formalize this structural mismatch as the audit gap, the divergence between required and achievable verification access, and introduce the concept of fragile assurance to describe cases where the evidential structure does not support the asserted safety claim. Through an analysis of a 21-instrument inventory, we identify an incentive gradient where geopolitical and industrial pressures systematically reward surface-level behavioral proxies over deep structural verification. Finally, we propose a technical pivot: bounding the weight of behavioral evidence in legal text and extending voluntary pre-deployment access with mechanistic-evidence classes, specifically linear probes, activation patching, and before/after-training comparisons.

### 🤖 AI 总结

**一句话总结**：This position paper argues that behavioural assurance, even when carefully designed, is being asked to carry safety claims it cannot verify. AI governance frameworks enacted between 2019 and early 202...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Position, Behavioural, Assurance, Cannot, Verify, Safety, Claims, Governance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15164v1) | [下载PDF](https://arxiv.org/pdf/2605.15164v1.pdf)

---

## [26. Widening the Gap: Exploiting LLM Quantization via Outlier Injection](https://arxiv.org/abs/2605.15152v1)

**作者**：Xiaohua Zhan, Kazuki Egashira, Robin Staab 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-14

### 📄 论文摘要

LLM quantization has become essential for memory-efficient deployment. Recent work has shown that quantization schemes can pose critical security risks: an adversary may release a model that appears benign in full precision but exhibits malicious behavior once quantized by users. However, existing quantization-conditioned attacks have been limited to relatively simple quantization methods, where the attacker can estimate weight regions that remain invariant under the target quantization. Notably, prior attacks have consistently failed to compromise more popular and sophisticated schemes, limiting their practical impact. In this work, we introduce the first quantization-conditioned attack that consistently induces malicious behavior that can be triggered by a broad range of advanced quantization techniques, including AWQ, GPTQ, and GGUF I-quants. Our attack exploits a simple property shared by many modern quantization methods: large outliers can cause other weights to be rounded to zero. Consequently, by injecting outliers into specific weight blocks, an adversary can therefore induce a targeted, predictable weight collapse in the model. This effect can be used to craft seemingly benign full-precision models that exhibit a wide range of malicious behaviors after quantization. Through extensive evaluation across three attack scenarios and LLMs, we show that our attack achieves high success rates against a broad range of quantization methods on which prior attacks fail. Our results demonstrate, for the first time, that the security risks of quantization are not restricted to simpler schemes but are broadly relevant across complex, widely-used quantization methods.

### 🤖 AI 总结

**一句话总结**：LLM quantization has become essential for memory-efficient deployment. Recent work has shown that quantization schemes can pose critical security risks: an adversary may release a model that appears b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Widening, Gap, Exploiting, Quantization, via, Outlier, Injection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15152v1) | [下载PDF](https://arxiv.org/pdf/2605.15152v1.pdf)

---

## [27. Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution](https://arxiv.org/abs/2605.15138v1)

**作者**：Saisab Sadhu, Pratinav Seth, Vinay Kumar Sankarapu  
**分类**：cs.LG, cs.CL, cs.ET  
**发布时间**：2026-05-14

### 📄 论文摘要

Standard unlearning evaluations measure behavioral suppression in full precision, immediately after training, despite every deployed language model being quantized first. Recent work has shown that 4-bit post-training quantization can reverse machine unlearning; we show this is not a tuning artefact but a systematic dual failure: gradient-based methods that achieve meaningful forgetting lose it under compression, while methods that survive quantization barely change the model. Both failures trace to the same root cause: across all baselines, per-parameter updates lie 47-828x below the NF4 quantization bin width; updates diffused across billions of parameters cannot clear quantization bin boundaries, a consequence we formalize as a sparsity-permanence tradeoff. We present MANSU (Mechanistic-Aligned Null-Space Unlearning), which resolves both modes by combining causal circuit attribution to isolate the minimal forget-set subgraph, circuit-restricted null-space projection with a diagonal-Fisher retain bound, and a per-parameter magnitude floor guaranteeing quantization survival by construction. We additionally introduce Circuit Attribution Divergence (CAD), a mechanistic verification metric distinguishing structural erasure from behavioral suppression, a distinction existing metrics cannot make. Across multiple model families and hazard benchmarks, MANSU is the first method to jointly satisfy all four properties with margin on each (meaningful forgetting, retain preservation, non-positive PTQ gap, and structural erasure), while gradient-based baselines recover up to +0.05 accuracy under compression.

### 🤖 AI 总结

**一句话总结**：Standard unlearning evaluations measure behavioral suppression in full precision, immediately after training, despite every deployed language model being quantized first. Recent work has shown that 4-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Forgetting, Sticks, Quantization-Permanent, Unlearning, via, Circuit, Attribution, Standard

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15138v1) | [下载PDF](https://arxiv.org/pdf/2605.15138v1.pdf)

---

## [28. Causal Foundation Models with Continuous Treatments](https://arxiv.org/abs/2605.15133v1)

**作者**：Christopher Stith, Medha Barath, Vahid Balazadeh 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-14

### 📄 论文摘要

Causal inference, estimating causal effects from observational data, is a fundamental tool in many disciplines. Of particular importance across a variety of domains is the continuous treatment setting, where the variable of intervention has a continuous range. This setting is far less explored and represents a substantial shift from the binary treatment setting, with models needing to represent effects across a continuum of treatment values. In this paper, we present the first causal foundation model for the continuous treatment setting. Our model meta-learns the ability to predict causal effects across a wide variety of unseen tasks without additional training or fine-tuning. First, we design a novel prior over data-generating processes with continuous treatment variables in order to generate a rich causal training corpus. We then train a transformer to reconstruct individual treatment-response curves given only observational data, leveraging in-context learning to amortize expensive Bayesian posterior inference. Our model achieves state-of-the-art performance on individual treatment-response curve reconstruction tasks compared to causal models which are trained specifically for those tasks.

### 🤖 AI 总结

**一句话总结**：Causal inference, estimating causal effects from observational data, is a fundamental tool in many disciplines. Of particular importance across a variety of domains is the continuous treatment setting...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Causal, Foundation, Models, Continuous, Treatments, inference, estimating, effects

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15133v1) | [下载PDF](https://arxiv.org/pdf/2605.15133v1.pdf)

---

## [29. Natural Synthesis: Outperforming Reactive Synthesis Tools with Large Reasoning Models](https://arxiv.org/abs/2605.15131v1)

**作者**：Frederik Schmitt, Matthias Cosler, Niklas Metzger 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-14

### 📄 论文摘要

Reactive synthesis, the problem of automatically constructing a hardware circuit from a logical specification, is a long-standing challenge in formal verification. It is elusive for two reasons: It is algorithmically hard, and writing formal specifications by hand is notoriously difficult. In this paper, we tackle both sides of the problem. For the algorithmic side, we present a neuro-symbolic approach to reactive synthesis that couples large reasoning models with model checkers to iteratively repair a synthesized Verilog implementation via sound symbolic feedback. Our approach solves more benchmarks than the best dedicated tools in the annual synthesis competition and extends to constructing parameterized systems, a problem known to be undecidable. On the specification side, we introduce an autoformalization step that shifts the specification task from temporal logic to natural language by introducing a hand-authored dataset of natural-language specifications for evaluation. We demonstrate performance comparable to that of starting from formal specifications, establishing natural synthesis as a viable end-to-end workflow.

### 🤖 AI 总结

**一句话总结**：Reactive synthesis, the problem of automatically constructing a hardware circuit from a logical specification, is a long-standing challenge in formal verification. It is elusive for two reasons: It is...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Natural, Synthesis, Outperforming, Reactive, Tools, Large, Reasoning, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15131v1) | [下载PDF](https://arxiv.org/pdf/2605.15131v1.pdf)

---

## [30. Proposal and study of statistical features for string similarity computation and classification](https://arxiv.org/abs/2605.15110v1)

**作者**：E. O. Rodrigues, D. Casanova, M. Teixeira 等 8 位作者  
**分类**：cs.LG, cs.CL, cs.IT  
**发布时间**：2026-05-14

### 📄 论文摘要

Adaptations of features commonly applied in the field of visual computing, co-occurrence matrix (COM) and run-length matrix (RLM), are proposed for the similarity computation of strings in general (words, phrases, codes and texts). The proposed features are not sensitive to language related information. These are purely statistical and can be used in any context with any language or grammatical structure. Other statistical measures that are commonly employed in the field such as longest common subsequence, maximal consecutive longest common subsequence, mutual information and edit distances are evaluated and compared. In the first synthetic set of experiments, the COM and RLM features outperform the remaining state-of-the-art statistical features. In 3 out of 4 cases, the RLM and COM features were statistically more significant than the second best group based on distances (P-value < 0.001). When it comes to a real text plagiarism dataset, the RLM features obtained the best results.

### 🤖 AI 总结

**一句话总结**：Adaptations of features commonly applied in the field of visual computing, co-occurrence matrix (COM) and run-length matrix (RLM), are proposed for the similarity computation of strings in general (wo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Proposal, study, statistical, features, string, similarity, computation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.15110v1) | [下载PDF](https://arxiv.org/pdf/2605.15110v1.pdf)

---

