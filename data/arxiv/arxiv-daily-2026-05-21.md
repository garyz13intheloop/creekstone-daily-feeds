# arXiv AI 论文日报 | 2026-05-21

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (15 篇)
- [cs.CV](#csCV) (9 篇)
- [cs.AI](#csAI) (4 篇)
- [cs.CL](#csCL) (2 篇)

---

## cs.AI

## [1. DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation](https://arxiv.org/abs/2605.21482v1)

**作者**：Sixiong Xie, Zhuofan Shi, Haiyang Shen 等 11 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-20

### 📄 论文摘要

Deep research, in which an agent searches the open web, collects evidence, and derives an answer through extended reasoning, is a prominent use case for frontier language models. Frontier deep research products score high on existing benchmarks, making it difficult to distinguish their capabilities from current evaluation data alone. We introduce DeepWeb-Bench, a deep research benchmark that is substantially harder than existing benchmarks for the current frontier. Difficulty comes from three properties of the data itself: each task requires massive evidence collection, cross-source reconciliation, and long-horizon multi-step derivation. We represent these three sources of difficulty as four capability families (Retrieval, Derivation, Reasoning, and Calibration) and report results sliced by family. Every reference answer is accompanied by a source-provenance record with four disclosure levels and cross-source checks where available, making scores easier to audit against the underlying evidence. We evaluate DeepWeb-Bench on nine frontier models and report three findings: (1) retrieval is not the bottleneck, as retrieval failures account for only 12-14% of errors while derivation and calibration failures account for over 70%; (2) strong and weak models fail in qualitatively different ways, with strong models' errors dominated by incomplete derivation and weak models' by hallucinated precision; and (3) models exhibit genuine specialization across domains, with cross-model agreement of only rho = 0.61 and per-case disagreement reaching 18.8 percentage points. The public benchmark release includes the data, rubrics, and evaluation code.

### 🤖 AI 总结

**一句话总结**：Deep research, in which an agent searches the open web, collects evidence, and derives an answer through extended reasoning, is a prominent use case for frontier language models. Frontier deep researc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DeepWeb-Bench, Deep, Research, Benchmark, Demanding, Massive, Cross-Source, Evidence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21482v1) | [下载PDF](https://arxiv.org/pdf/2605.21482v1.pdf)

---

## [2. AiraXiv: An AI-Driven Open-Access Platform for Human and AI Scientists](https://arxiv.org/abs/2605.21481v1)

**作者**：Junshu Pan, Panzhong Lu, Yixuan Weng 等 8 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-05-20

### 📄 论文摘要

Recent advances in artificial intelligence (AI) have accelerated the growth of both human-authored and AI-generated research outputs, placing increasing strain on traditional academic publishing systems and challenging the scalability of conference- and journal-centered paradigms amid rising submission volumes, reviewer workload, and venue size. To address these challenges, we explore an AI-era publishing paradigm in which both human and AI scientists participate as authors and readers, and papers evolve through continuous, feedback-driven iteration. We propose AiraXiv, an AI-driven open-access platform built on open preprints, AI-augmented analysis and review, and reader feedback. AiraXiv supports human scientists through an interactive UI and AI scientists through Model Context Protocol (MCP)-based interactions. We validate AiraXiv through real-world deployments, including serving as the submission platform for ICAIS 2025, demonstrating its potential as a fast, inclusive, and scalable research infrastructure for the AI era. AiraXiv is publicly available at https://airaxiv.com.

### 🤖 AI 总结

**一句话总结**：Recent advances in artificial intelligence (AI) have accelerated the growth of both human-authored and AI-generated research outputs, placing increasing strain on traditional academic publishing syste...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, AiraXiv, AI-Driven, Open-Access, Platform, Human, Scientists, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21481v1) | [下载PDF](https://arxiv.org/pdf/2605.21481v1.pdf)

---

## [3. PALS: Power-Aware LLM Serving for Mixture-of-Experts Models](https://arxiv.org/abs/2605.21427v1)

**作者**：Can Hankendi, Rana Shahout, Minlan Yu 等 4 位作者  
**分类**：cs.AI, cs.DC  
**发布时间**：2026-05-20

### 📄 论文摘要

Large language model (LLM) inference has become a dominant workload in modern data centers, driving significant GPU utilization and energy consumption. While prior systems optimize throughput and latency by batching, scheduling, and parallelism, they largely treat GPU power as a static constraint rather than a controllable resource. In this paper, we present a power-aware runtime for LLM serving, PALS, that treats GPU power caps as a first-class control knob and jointly optimizes them with software parameters such as batch size. The system combines lightweight offline power-performance models with a feedback-driven controller to select configurations that satisfy throughput targets while maximizing energy efficiency. We implement PALS within an existing LLM serving framework, vLLM, demonstrating that it requires no model retraining or API changes. Across multi-GPU systems and both dense and mixture-of-experts (MoE) models, PALS improves energy efficiency by up to 26.3%, reduces QoS violations by 4x to 7x under power constraints, and tracks dynamic power budgets. These results highlight the potential of integrating power control directly into LLM inference runtimes, enabling energy-proportional and grid-interactive AI systems.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM) inference has become a dominant workload in modern data centers, driving significant GPU utilization and energy consumption. While prior systems optimize throughput and late...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, PALS, Power-Aware, Serving, Mixture-of-Experts, Models, Large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21427v1) | [下载PDF](https://arxiv.org/pdf/2605.21427v1.pdf)

---

## [4. Teaching AI Through Benchmark Construction: QuestBench as a Course-Based Practice for Accountable Knowledge Work](https://arxiv.org/abs/2605.21413v1)

**作者**：Haiyang Shen, Jiuzheng Wang, Taian Guo 等 12 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-20

### 📄 论文摘要

As AI becomes part of everyday learning, many courses teach students to use it mainly as a productivity tool: how to prompt, search, summarize, write, code, and use tools more efficiently. We argue that AI education also needs a setting in which students learn to test AI and understand their own role in judging machine-produced knowledge. To this end, we introduce a course-based practice that teaches AI through benchmark construction, using deep research systems as a concrete example of AI-era knowledge work. Students turn disciplinary knowledge into verifiable expert-level questions, review one another's designs for ambiguity and shortcuts, and evaluate AI systems on the resulting tasks. This activity gives students direct exposure to a powerful tool while asking them to specify what a trustworthy answer would require. The produced benchmark, QuestBench, consists of 256 questions across 14 humanities and social-science domains. Evaluation on QuestBench shows that student-designed tasks reveal hidden failures in current deep research systems: across thirteen evaluated systems, the mean question-level pass rate is only 16.85%, and the best-performing system, GPT-5.5, reaches a 57.58% pass rate. The failures are educationally useful because they show how fluent, source-backed answers can still miss the right query, source, term, or evidence standard. Reflections from five student contributors suggest that benchmark construction can help students see professional knowledge not only as content AI may retrieve, but as the basis for judging AI outputs. We present QuestBench as a benchmark artifact and as a reusable classroom setting for a larger educational question: how students can remain responsible knowledge actors as AI enters learning and professional work. The dataset is available at https://huggingface.co/datasets/PKUAIWeb/QuestBench/tree/main.

### 🤖 AI 总结

**一句话总结**：As AI becomes part of everyday learning, many courses teach students to use it mainly as a productivity tool: how to prompt, search, summarize, write, code, and use tools more efficiently. We argue th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Teaching, Through, Benchmark, Construction, QuestBench, Course-Based, Practice

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21413v1) | [下载PDF](https://arxiv.org/pdf/2605.21413v1.pdf)

---

## cs.CL

## [5. Leveraging LLMs for Grammar Adaptation: A Study on Metamodel-Grammar Co-Evolution](https://arxiv.org/abs/2605.21465v1)

**作者**：Weixing Zhang, Bowen Jiang, Rahul Sharma 等 5 位作者  
**分类**：cs.CL, cs.SE  
**发布时间**：2026-05-20

### 📄 论文摘要

In model-driven engineering, metamodel evolution leads to the need to adapt corresponding grammars to maintain consistency, which typically requires tedious manual work. Existing rule-based methods can achieve partial automation but have limitations when handling complex grammar scenarios. This paper proposes a Large Language Model-based approach that automatically applies adaptations to new grammars after evolution by learning grammar adaptations from previous versions. We evaluated this approach on six real-world Xtext domain-specific languages, using four DSLs as a training set to develop prompting strategies, two DSLs as a test set for validation, and conducting a longitudinal case study on QVTo. The evaluation used three Large Language Models (Claude Sonnet 4.5, ChatGPT 5.1, Gemini 3) and measured grammar adaptation quality from three dimensions: grammar rule-level adaptation consistency, output similarity, and metamodel conformance. Results show that on the test set, all three LLMs achieved 100% adaptation consistency and output similarity, while the rule-based approach achieved only 84.21% on DOT and 62.50% on Xcore. In the QVTo longitudinal study, the LLM-based approach successfully reused learned adaptations across all three evolution steps without manual grammar editing, while the rule-based approach required manual adjustments in two of three transitions. However, on large-scale grammars (EAST-ADL, 297 rules), LLMs' adaptation consistency was far below 90%. This study demonstrates the advantages of LLM-based approaches in handling complex grammar scenarios, while revealing their limitations in large-scale grammar adaptation.

### 🤖 AI 总结

**一句话总结**：In model-driven engineering, metamodel evolution leads to the need to adapt corresponding grammars to maintain consistency, which typically requires tedious manual work. Existing rule-based methods ca...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Leveraging, Grammar, Adaptation, Study, Metamodel-Grammar, Co-Evolution, model-driven

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21465v1) | [下载PDF](https://arxiv.org/pdf/2605.21465v1.pdf)

---

## [6. Mem-$π$: Adaptive Memory through Learning When and What to Generate](https://arxiv.org/abs/2605.21463v1)

**作者**：Xiaoqiang Wang, Chao Wang, Hadi Nekoei 等 8 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-05-20

### 📄 论文摘要

We present Mem-$π$, a framework for adaptive memory in large language model (LLM) agents, where useful guidance is generated on demand rather than retrieved from external memory stores. Existing memory-augmented agents typically rely on similarity-based retrieval from episodic memory banks or skill libraries, returning static entries that often misalign with the current context. In contrast, Mem-$π$ uses a dedicated language or vision-language model with its own parameters, separate from the downstream agent, to generate context-specific guidance for complex tasks. Conditioned on the current agent context, the model jointly decides when to produce guidance and what guidance to produce. We train it with a decision-content decoupled reinforcement learning (RL) objective, enabling it to abstain when generation would not help and otherwise produce concise, useful guidance. Across diverse agentic benchmarks spanning web navigation, terminal-based tool use, and text-based embodied interaction, Mem-$π$ consistently outperforms retrieval-based and prior RL-optimized memory baselines, achieving over 30% relative improvement on web navigation tasks.

### 🤖 AI 总结

**一句话总结**：We present Mem-$π$, a framework for adaptive memory in large language model (LLM) agents, where useful guidance is generated on demand rather than retrieved from external memory stores. Existing memor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mem-$π$, Adaptive, Memory, through, Learning, When, What, Generate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21463v1) | [下载PDF](https://arxiv.org/pdf/2605.21463v1.pdf)

---

## cs.CV

## [7. Uni-Edit: Intelligent Editing Is A General Task For Unified Model Tuning](https://arxiv.org/abs/2605.21487v1)

**作者**：Dian Zheng, Manyuan Zhang, Hongyu Li 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-20

### 📄 论文摘要

Currently, enhancing Unified Multimodal Models (UMMs) with image understanding, generation, and editing capabilities mainly relies on mixed multi-task training. Due to inherent task conflicts, such strategy requires complex multi-stage pipelines, massive data mixing, and balancing tricks, merely resulting in a performance trade-off rather than true mutual reinforcement. To break this paradigm, we propose Uni-Edit, an intelligent image editing task that serves as the first general task for UMM tuning. Unlike complex mixed pipelines, Uni-Edit improves performance across all three abilities at once using only one task, one training stage, and one dataset. Specifically, we first identify image editing as an inherently ideal general task, as it naturally demands both visual understanding and generation. However, existing editing data relies on simplistic instructions that severely underutilize a model's understanding capacity. To address this, we introduce the first automated and scalable data synthesis pipeline for intelligent editing, transforming diverse VQA data into complex and effective editing instructions with embedded questions and nested logic. This yields Uni-Edit-148k, pairing diverse reasoning-intensive instructions with high-quality edited images. Extensive experiments on BAGEL and Janus-Pro demonstrate that tuning solely on Uni-Edit achieves comprehensive enhancements across all three capabilities without any auxiliary operations.

### 🤖 AI 总结

**一句话总结**：Currently, enhancing Unified Multimodal Models (UMMs) with image understanding, generation, and editing capabilities mainly relies on mixed multi-task training. Due to inherent task conflicts, such st...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Uni-Edit, Intelligent, Editing, General, Task, Unified, Model, Tuning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21487v1) | [下载PDF](https://arxiv.org/pdf/2605.21487v1.pdf)

---

## [8. WikiVQABench: A Knowledge-Grounded Visual Question Answering Benchmark from Wikipedia and Wikidata](https://arxiv.org/abs/2605.21479v1)

**作者**：Basel Shbita, Pengyuan Li, Anna Lisa Gentile  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-20

### 📄 论文摘要

Visual Question Answering (VQA) benchmarks have largely emphasized perception-based tasks that can be solved from visual content alone. In contrast, many real-world scenarios require external knowledge that is not directly observable in the image to answer correctly. We introduce WikiVQABench, a human-curated knowledge-grounded VQA benchmark constructed by systematically combining Wikipedia images, their associated article captions, and structured knowledge from Wikidata. Our pipeline uses large language models (LLMs) to generate candidate multiple-choice image-question-answer sets. All generated instances are subsequently reviewed and curated by human annotators to ensure factual correctness, visual-text consistency, and that each question requires external knowledge in addition to visual evidence for correct resolution. WikiVQABench comprises a substantial collection of Wikipedia images with curated multiple-choice questions designed to benchmark knowledge-aware vision-language models (VLMs). Evaluation of fifteen VLMs (256M-90B parameters) reveals a wide performance range (24.7%-75.6% accuracy), demonstrating that the benchmark effectively discriminates model capabilities on knowledge-intensive reasoning. The dataset and benchmarking code are publicly available.

### 🤖 AI 总结

**一句话总结**：Visual Question Answering (VQA) benchmarks have largely emphasized perception-based tasks that can be solved from visual content alone. In contrast, many real-world scenarios require external knowledg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：WikiVQABench, Knowledge-Grounded, Visual, Question, Answering, Benchmark, Wikipedia, Wikidata

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21479v1) | [下载PDF](https://arxiv.org/pdf/2605.21479v1.pdf)

---

## [9. Latent Dynamics for Full Body Avatar Animation](https://arxiv.org/abs/2605.21478v1)

**作者**：Shichong Peng, Chengxiang Yin, Fei Jiang 等 10 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-05-20

### 📄 论文摘要

Pose-driven full-body avatars built on neural rendering produce high-quality novel views of a captured subject. Yet loose clothing and other dynamic elements deform in ways pose alone cannot explain: the same pose can correspond to many different states, because their motion depends on history, inertia, and contact. Explicit simulation and layered-garment methods can model such dynamics, but they require either a dedicated garment template, which raw multi-view capture does not naturally provide, or a test-time physics simulator with non-trivial runtime cost. A parallel line of work learns data-driven clothing avatars that avoid explicit garment layers. These methods add an auxiliary latent for variation beyond pose; at inference, they fix it, regress it from pose, or retrieve it from training data, without explicitly modeling how the latent evolves with its own dynamics. Additionally, even in everyday motion with loose clothing, existing architectures often struggle to capture fine-grained detail, producing blurry renderings and temporal artifacts. We augment a pose-conditioned 3D Gaussian avatar with a transformer-based decoder and a dynamics residual latent that captures temporal appearance and geometry variation beyond the driving signals. At inference, a learned latent dynamics model evolves the residual latent from a short pose history and the previous latent state. The model decomposes each update into driving, restoring, and dissipative forces, producing temporally coherent, history-dependent rollouts with negligible added cost. Different initial conditions yield diverse yet plausible motion trajectories, and the force decomposition exposes controls such as stiffness. Across nine captured sequences of everyday motion with diverse loose garments, quantitative metrics and a perceptual user study show improved animation quality over recent data-driven baselines.

### 🤖 AI 总结

**一句话总结**：Pose-driven full-body avatars built on neural rendering produce high-quality novel views of a captured subject. Yet loose clothing and other dynamic elements deform in ways pose alone cannot explain: ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Latent, Dynamics, Full, Body, Avatar, Animation, Pose-driven, full-body

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21478v1) | [下载PDF](https://arxiv.org/pdf/2605.21478v1.pdf)

---

## [10. Stream3D: Sequential Multi-View 3D Generation via Evidential Memory](https://arxiv.org/abs/2605.21472v1)

**作者**：Kaichen Zhou, Zeyang Bai, Xinhai Chang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-20

### 📄 论文摘要

View-conditioned 3D generators such as SAM 3D, TRELLIS and Hunyuan3D produce high-quality object reconstructions from a single view, but real-world visual observation often arrives as long monocular streams. Naively applying these generators to each streaming frame independently leads to severe temporal inconsistency in the generated results. To address this problem, we propose Stream3D, the first training-free streaming mechanism that turns a frozen view-conditioned 3D generator into a streaming generator with constant cross-chunk memory. Stream3D achieves this by maintaining a compact evidential memory, which selectively caches the most informative historical frames based on a proposed evidence score mechanism. As the stream progresses, the memory dynamically updates to retain a fixed number of informative frames, preventing the memory footprint from growing linearly with sequence length. This also prevents degradation over long sequences and keeps the underlying generator completely unchanged without retraining, architectural modifications, or auxiliary losses. Evaluated on both realistic and synthetic streaming benchmarks, Stream3D outperforms latent-transport baselines, including KV-cache reuse and flow-based feature editing, across both photometric and geometric metrics. More details can be found at: https://anonymous-submission-20.github.io/streaming3D.github.io/.

### 🤖 AI 总结

**一句话总结**：View-conditioned 3D generators such as SAM 3D, TRELLIS and Hunyuan3D produce high-quality object reconstructions from a single view, but real-world visual observation often arrives as long monocular s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Stream3D, Sequential, Multi-View, Generation, via, Evidential, Memory

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21472v1) | [下载PDF](https://arxiv.org/pdf/2605.21472v1.pdf)

---

## [11. StreamGVE: Training-Free Video Editing via Few-Step Streaming Video Generation](https://arxiv.org/abs/2605.21466v1)

**作者**：Guanlong Jiao, Chenyangguang Zhang, Jia Jun Cheng Xian 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-20

### 📄 论文摘要

Although existing video editing methods are generally feasible, they often require many costly iterations and still struggle to deliver high-quality yet satisfying editing results. We attribute this limitation to the prevalent data-to-data paradigm, which is less compatible with modern generative models than noise-to-data generation. To address this gap, we revisit video editing from a noise-to-data perspective and propose Streaming-Generation-based Video Editing (StreamGVE), which preserves few-step sampling while seamlessly injecting source-video conditions. Built on pre-trained streaming generation models, StreamGVE introduces dual-branch fast sampling with a self-attention bridge and cross-attention grounding/boosting to satisfy both sampling and conditioning requirements. We further propose source-oriented guidance to improve target-generation quality, and a visual prompting strategy to enhance editing flexibility and practicality. The method is effective, robust, and generalizable across different models. Extensive experiments on diverse video editing tasks show that StreamGVE consistently outperforms existing approaches, even in few-step settings with minimal time cost.

### 🤖 AI 总结

**一句话总结**：Although existing video editing methods are generally feasible, they often require many costly iterations and still struggle to deliver high-quality yet satisfying editing results. We attribute this l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：StreamGVE, Training-Free, Video, Editing, via, Few-Step, Streaming, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21466v1) | [下载PDF](https://arxiv.org/pdf/2605.21466v1.pdf)

---

## [12. ReMATF: Recurrent Motion-Adaptive Multi-scale Turbulence Mitigation for Dynamic Scenes](https://arxiv.org/abs/2605.21440v1)

**作者**：Zhiming Liu, Zhicheng Zou, Nantheera Anantrasirichai  
**分类**：cs.CV  
**发布时间**：2026-05-20

### 📄 论文摘要

Atmospheric turbulence severely degrades video quality by introducing distortions such as geometric warping, blur, and temporal flickering, posing significant challenges to both visual clarity and temporal consistency. Current state-of-the-art methods are based on transformer, 3D architectures and require multi-frame input, but their large computational cost and memory usage limit real-time deployment, especially in resource-constrained scenarios. In this work, we propose ReMATF, a lightweight recurrent framework that restores videos using only two frames at a time while preserving spatial detail and temporal stability. ReMATF combines a multi-scale encoder-decoder with temporal warping and a motion-adaptive temporal fusion module that performs per-pixel fusion between the warped previous output and the current prediction to enhance coherence without enlarging the temporal window. This design reduces flicker, sharpens details, and remains efficient. Experiments on synthetic and real turbulence datasets show consistent improvements in PSNR/SSIM and perceptual quality (LPIPS), along with substantially faster inference than multi-frame transformer baselines, making ReMATF suitable turbulence mitigation in resource-constrained scenarios.

### 🤖 AI 总结

**一句话总结**：Atmospheric turbulence severely degrades video quality by introducing distortions such as geometric warping, blur, and temporal flickering, posing significant challenges to both visual clarity and tem...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ReMATF, Recurrent, Motion-Adaptive, Multi-scale, Turbulence, Mitigation, Dynamic, Scenes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21440v1) | [下载PDF](https://arxiv.org/pdf/2605.21440v1.pdf)

---

## [13. iTryOn: Mastering Interactive Video Virtual Try-On with Spatial-Semantic Guidance](https://arxiv.org/abs/2605.21431v1)

**作者**：Jun Zheng, Zhengze Xu, Mengting Chen 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-20

### 📄 论文摘要

Video Virtual Try-On (VVT) aims to seamlessly replace a garment on a person in a video with a new one. While existing methods have made significant strides in maintaining temporal consistency, they are predominantly confined to non-interactive scenarios where models merely showcase garments. This limitation overlooks a crucial aspect of real-world apparel presentation: active human-garment interaction. To bridge this gap, we introduce and formalize a new challenging task: Interactive Video Virtual Try-On (Interactive VVT), where subjects in the video actively engage with their clothing. This task introduces unique challenges beyond simple texture preservation, including: (1) resolving the semantic ambiguity of interactions from standard pose information, and (2) learning complex garment deformations from video where interactive moments are sparse and brief. To address these challenges, we propose iTryOn, a novel framework built upon a large-scale video diffusion Transformer. iTryOn pioneers a multi-level interaction injection mechanism to guide the generation of complex dynamics. At the spatial level, we introduce a garment-agnostic 3D hand prior to provide fine-grained guidance for precise hand-garment contact, effectively resolving spatial ambiguity. At the semantic level, iTryOn leverages global captions for overall context and time-stamped action captions for localized interactions, synchronized via our novel Action-aware Rotational Position Embedding (A-RoPE). Extensive experiments demonstrate that iTryOn not only achieves state-of-the-art performance on traditional VVT benchmarks but also establishes a commanding lead in the new interactive setting, marking a significant step towards more dynamic and controllable virtual try-on experiences.

### 🤖 AI 总结

**一句话总结**：Video Virtual Try-On (VVT) aims to seamlessly replace a garment on a person in a video with a new one. While existing methods have made significant strides in maintaining temporal consistency, they ar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：iTryOn, Mastering, Interactive, Video, Virtual, Try-On, Spatial-Semantic, Guidance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21431v1) | [下载PDF](https://arxiv.org/pdf/2605.21431v1.pdf)

---

## [14. AIGaitor: Privacy-preserving and cloud-free motion analysis for everyone, using edge computing](https://arxiv.org/abs/2605.21421v1)

**作者**：Lauhitya Reddy, Trisha M. Kesar, Hyeokhyen Kwon  
**分类**：cs.CV  
**发布时间**：2026-05-20

### 📄 论文摘要

Motion capture is the gold standard for measuring human movement, but clinical use remains limited by cost, technical complexity, and privacy concerns. AIGaitor is a privacy-preserving, cloud-free motion analysis system that runs markerless monocular motion-capture pipelines and downstream deep-learning analysis entirely on a consumer smartphone using on-device neural accelerators. To motivate its design, we surveyed 74 rehabilitation clinicians: 92 percent said they would adopt an accurate, cost-effective, easy-to-use AI gait analysis tool, while 79.7 percent cited operating cost, 68.9 percent insufficient training, and 64.9 percent privacy concerns as leading barriers. We then optimized and benchmarked mobile iOS implementations of current monocular pipeline components, including 2D and 3D pose estimation, pose optimization, skeleton-based deep-learning analysis, and a vision-language model. A Time-Priority end-to-end on-device pipeline processes a 10 s 4K 60 fps video clip in 77 s on an iPhone 14, matching or beating the same pipeline on a high-end NVIDIA H200 cloud server when network transfer is included: 94 s at global mobile-average uplink and 66 s at developed-world Wi-Fi. Lightweight models such as ViTPose-s achieve real-time keypoint extraction, and skeleton-based action-recognition models provide sub-millisecond gait classification on the same clip. To our knowledge, AIGaitor is the first monocular system to demonstrate end-to-end on-device motion capture and downstream deep-learning analysis, supporting clinically applicable movement analysis that is low-cost, private, and accessible to smartphone users.

### 🤖 AI 总结

**一句话总结**：Motion capture is the gold standard for measuring human movement, but clinical use remains limited by cost, technical complexity, and privacy concerns. AIGaitor is a privacy-preserving, cloud-free mot...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AIGaitor, Privacy-preserving, cloud-free, motion, analysis, everyone, edge, computing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21421v1) | [下载PDF](https://arxiv.org/pdf/2605.21421v1.pdf)

---

## [15. Ordering Matters: Rank-Aware Selective Fusion for Blended Emotion Recognition](https://arxiv.org/abs/2605.21417v1)

**作者**：Junghyun Lee, Hyunseo Kim, Hanna Jang 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-20

### 📄 论文摘要

Blended emotion recognition is challenging because emotions are often expressed as mixtures of subtle and overlapping multimodal cues rather than a single dominant signal. We propose a rank-aware multi-encoder framework that selectively combines complementary representations from diverse pre-extracted video and audio encoders. Our method projects heterogeneous encoder features into a shared latent space, estimates sample-wise encoder importance through an attention-based gating module, and fuses only the top-n most informative encoders. To better model blended emotions, we decouple prediction into presence and salience heads and align them through probability-level fusion. We further incorporate feature-level unsupervised domain adaptation without pseudo-labeling to improve robustness under distribution shift. Experiments on the BlEmoRE challenge show that the proposed framework outperforms strong individual encoders and naïve multi-encoder fusion baselines. Our final system ranked 2nd in the competition, supporting the effectiveness of rank-aware selective fusion for fine-grained blended emotion recognition.

### 🤖 AI 总结

**一句话总结**：Blended emotion recognition is challenging because emotions are often expressed as mixtures of subtle and overlapping multimodal cues rather than a single dominant signal. We propose a rank-aware mult...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Ordering, Matters, Rank-Aware, Selective, Fusion, Blended, Emotion, Recognition

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21417v1) | [下载PDF](https://arxiv.org/pdf/2605.21417v1.pdf)

---

## cs.LG

## [16. Variance Reduction for Expectations with Diffusion Teachers](https://arxiv.org/abs/2605.21489v1)

**作者**：Jesse Bettencourt, Xindi Wu, Matan Atzmon 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CV, stat.CO, stat.ML  
**发布时间**：2026-05-20

### 📄 论文摘要

Pretrained diffusion models serve as frozen teachers feeding downstream pipelines such as text-to-3D, single-step distillation, and data attribution. The teacher gradients these pipelines consume are Monte Carlo (MC) expectations over noise levels and Gaussian noise samples; their estimator variance dominates compute cost because each draw requires expensive upstream work (rendering, simulation, encoding). We introduce CARV, a compute-aware variance-accounting framework that motivates a hierarchical MC estimator: amortize the expensive upstream computation over cheap diffusion-noise resamples, sharpened by timestep importance sampling and a stratified-inverse-CDF construction. In our text-to-3D distillation and attribution experiments, CARV delivers 2-3x effective compute multipliers (most from amortized reuse; ~25% additional from IS+stratification) without changing the objective; in single-step distillation, the same techniques cut gradient variance by an order of magnitude but do not improve downstream FID, marking the regime where MC variance is no longer the bottleneck.

### 🤖 AI 总结

**一句话总结**：Pretrained diffusion models serve as frozen teachers feeding downstream pipelines such as text-to-3D, single-step distillation, and data attribution. The teacher gradients these pipelines consume are ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Variance, Reduction, Expectations, Teachers, Pretrained, models, serve

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21489v1) | [下载PDF](https://arxiv.org/pdf/2605.21489v1.pdf)

---

## [17. EvoStruct: Bridging Evolutionary and Structural Priors for Antibody CDR Design via Protein Language Model Adaptation](https://arxiv.org/abs/2605.21485v1)

**作者**：Mansoor Ahmed, Sujin Lee, Umar Khayaz 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-20

### 📄 论文摘要

Equivariant graph neural network (GNN) methods for antibody complementarity-determining region (CDR) design achieve the highest sequence recovery but suffer from severe vocabulary collapse. The current best GNN methods over-predict very few amino acids, such as tyrosine and glycine, while ignoring functionally important residues. We trace this failure to GNN encoders learning amino acid distributions de novo from limited structural data, discarding substitution patterns encoded in evolutionary databases. To resolve this, we propose EvoStruct, which bridges a frozen protein language model (PLM) with 3D structural context from an E(3)-equivariant GNN via a cross-attention adapter. Unlike prior PLM-structure adapters for general protein design, EvoStruct targets the vocabulary collapse problem specific to CDR design through progressive PLM unfreezing and R-Drop consistency regularization. On the CHIMERA-Bench dataset, EvoStruct achieves the highest amino acid recovery and lowest perplexity among several antibody design methods, improving sequence recovery by 16% and reducing perplexity by 43% relative to the best GNN baselines, while recovering 2.3x greater amino acid diversity and the highest binding-pair correlation with ground truth.

### 🤖 AI 总结

**一句话总结**：Equivariant graph neural network (GNN) methods for antibody complementarity-determining region (CDR) design achieve the highest sequence recovery but suffer from severe vocabulary collapse. The curren...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EvoStruct, Bridging, Evolutionary, Structural, Priors, Antibody, CDR, Design

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21485v1) | [下载PDF](https://arxiv.org/pdf/2605.21485v1.pdf)

---

## [18. Is Fixing Schema Graphs Necessary? Full-Resolution Graph Structure Learning for Relational Deep Learning](https://arxiv.org/abs/2605.21475v1)

**作者**：Yi Huang, Qingyun Sun, Jia Li 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-20

### 📄 论文摘要

Relational prediction tasks are fundamental in many real-world applications, where data are naturally stored in relational databases (RDBs). Relational Deep Learning (RDL) addresses this problem by modeling RDBs as graphs and applying graph neural networks (GNNs) for end-to-end learning. However, the full-resolution property is commonly adopted as a design principle in graph construction for RDBs to preserve relational semantics, which leads most existing methods to rely on fixed graph structures. In this paper, we propose FROG, a Full-Resolution and Optimizable Graph Structure Learning} framework for RDL that formulates relational structure learning as a learnable table role modeling problem, allowing tables to contribute as nodes and edges in message passing. We further design role-driven message passing mechanisms to capture relational semantics, enabling joint optimization of graph structure and GNN representations. To ensure semantic consistency, we introduce functional dependency constraints that regularize representations across table and entity levels. Extensive experiments demonstrate that our method outperforms existing approaches and reveal how table roles impact downstream tasks, offering new insights into graph construction for RDL

### 🤖 AI 总结

**一句话总结**：Relational prediction tasks are fundamental in many real-world applications, where data are naturally stored in relational databases (RDBs). Relational Deep Learning (RDL) addresses this problem by mo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Fixing, Schema, Graphs, Necessary?, Full-Resolution, Graph, Structure, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21475v1) | [下载PDF](https://arxiv.org/pdf/2605.21475v1.pdf)

---

## [19. Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling](https://arxiv.org/abs/2605.21470v1)

**作者**：Caleb Winston, Ron Yifeng Wang, Azalia Mirhoseini 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-20

### 📄 论文摘要

Computer-use agents (CUA) automate tasks specified with natural language such as "order the cheapest item from Taco Bell" by generating sequences of calls to tools such as click, type, and scroll on a browser. Current implementations follow a sequential fetch-screenshot-execute loop where each iteration requires an LLM call, resulting in high latency and frequent errors from incorrect tool use. We present agent just-in-time (JIT) compilation, an alternative that compiles task descriptions directly into executable code that is free to include LLM calls, tool calls, and parallelization. Our approach comprises three components: (1) JIT-Planner, which generates multiple code plans, validates each against tool specifications, and selects the minimum-cost candidate; (2) JIT-Scheduler, which explores parallelization strategies via Monte Carlo cost estimation from learned latency distributions; and (3) an invariant-enforcing tool protocol specifying precondition and postcondition state requirements that reduce the rate of generating plans with incorrect tool use. Across 5 web applications, JIT-Planner achieves $10.4\times$ speedup and $+28\%$ accuracy over Browser-Use, while JIT-Scheduler achieves $2.4\times$ speedup and $+9\%$ accuracy over OpenAI CUA.

### 🤖 AI 总结

**一句话总结**：Computer-use agents (CUA) automate tasks specified with natural language such as "order the cheapest item from Taco Bell" by generating sequences of calls to tools such as click, type, and scroll on a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, JIT, Compilation, Latency-Optimizing, Web, Planning, Scheduling, Computer-use

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21470v1) | [下载PDF](https://arxiv.org/pdf/2605.21470v1.pdf)

---

## [20. You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories](https://arxiv.org/abs/2605.21468v1)

**作者**：Zhepei Wei, Xinyu Zhu, Wei-Lin Chen 等 6 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-05-20

### 📄 论文摘要

Reinforcement learning with verifiable rewards (RLVR) has become a dominant paradigm for improving reasoning in large language models (LLMs), yet the underlying geometry of the resulting parameter trajectories remains underexplored. In this work, we demonstrate that RLVR weight trajectories are extremely low-rank and highly predictable. Specifically, we find that the majority of downstream performance gains are captured by a rank-1 approximation of the parameter deltas, where the magnitude of this projection evolves near-linearly with training steps. Motivated by this, we propose a simple and compute-efficient method RELEX (REinforcement Learning EXtrapolation), which estimates the rank-1 subspace from a short observation window and extrapolates future checkpoints via linear regression, with no learned model required. Across three models (i.e., Qwen2.5-Math-1.5B, Qwen3-4B-Base, and Qwen3-8B-Base), RELEX produces checkpoints that match or exceed RLVR performance on both in-domain and out-of-domain benchmarks, requiring as few as 15% steps of full RLVR training. Remarkably, RELEX is able to extrapolate far beyond the observation window at no training cost, predicting checkpoints up to 10-20$\times$ beyond the observed prefix with continued improvement (e.g., observe only the first 50 steps and extrapolate to 1000 steps). Our ablation analysis confirms the minimalist sufficiency of RELEX: neither increasing the subspace rank nor employing non-linear modeling yields further gains in extrapolation. Finally, we show that RELEX's success stems from a "denoising" effect: by projecting updates onto the rank-1 subspace, the model discards stochastic optimization noise that would otherwise degrade performance during extrapolation. Our code is available at https://github.com/weizhepei/RELEX.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning with verifiable rewards (RLVR) has become a dominant paradigm for improving reasoning in large language models (LLMs), yet the underlying geometry of the resulting parameter tra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Only, Need, Minimal, RLVR, Training, Extrapolating, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21468v1) | [下载PDF](https://arxiv.org/pdf/2605.21468v1.pdf)

---

## [21. A Machine Learning Framework for Weighted Least Squares GNSS Positioning based on Activation Functions](https://arxiv.org/abs/2605.21461v1)

**作者**：Pin-Hsun Lee, Harry Leib  
**分类**：cs.LG  
**发布时间**：2026-05-20

### 📄 论文摘要

Global Navigation Satellite Systems (GNSS) are widely used to provide position, velocity, and timing (PVT) information for various applications, including transportation, location-based communication services, and intelligent agriculture. In urban canyons, high-rise buildings and narrow streets can cause signal obstruction, non-line-of-sight (NLOS) reception, and multipath effects that introduce errors in GNSS pseudorange measurements. Although multi-constellations GNSS effectively increase the number of available satellites, the inclusion of degraded signals can lead to severe positioning errors. This study proposes a machine learning framework for the weighted least squares (WLS) algorithm incorporating activation functions to enhance positioning accuracy. Several signal quality indicators are employed as training features for ensemble learning algorithms to identify poor quality signals by providing quality scores. Then, activation functions are employed to transform the machine learning predicted scores to appropriate weights for WLS positioning. To evaluate the performance of our approach, experiments are conducted using real-world datasets from Hong Kong and Tokyo urban areas. Comparative analysis of activation functions reveals that sigmoid functions consistently yield the greatest improvements with different machine learning algorithms and GNSS constellation configurations. The proposed algorithm demonstrates substantial reductions in positioning errors for both single- and multiconstellation scenarios. Furthermore, our results indicate that the proposed algorithm exhibits strong geographical transferability. The proposed algorithm maintains comparable level of performance when trained on data from other regions with similar levels of urbanization.

### 🤖 AI 总结

**一句话总结**：Global Navigation Satellite Systems (GNSS) are widely used to provide position, velocity, and timing (PVT) information for various applications, including transportation, location-based communication ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Machine, Learning, Framework, Weighted, Least, Squares, GNSS, Positioning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21461v1) | [下载PDF](https://arxiv.org/pdf/2605.21461v1.pdf)

---

## [22. Mitigating Label Bias with Interpretable Rubric Embeddings](https://arxiv.org/abs/2605.21455v1)

**作者**：Calvin Isley, Johann D. Gaebler, Sharad Goel  
**分类**：cs.LG  
**发布时间**：2026-05-20

### 📄 论文摘要

Statistical decision algorithms are increasingly deployed in domains where ground-truth labels are hard to obtain, such as hiring, university admissions, and content moderation. In these settings, models are typically trained on historical human evaluations -- for example, using past hiring decisions as a proxy for true applicant quality. However, if past evaluations unjustly favor certain groups, models trained on these labels may inherit those biases. To address this problem, we propose basing predictions on rubric embeddings, a representation framework that replaces standard black-box embeddings with features derived from expert-defined criteria that align with the underlying construct of interest. By anchoring predictions to semantically meaningful dimensions, this approach guards against biased proxy signals. We provide both theoretical and empirical evidence that rubric embeddings mitigate label bias under plausible conditions. Empirically, we evaluate our method on a novel dataset of applications to a large master's program. We find that models trained on rubric embeddings reduce group disparities while improving measures of cohort quality. Our results suggest that basing predictions on interpretable, domain-grounded representations offers a practical approach to learning in the presence of biased labels.

### 🤖 AI 总结

**一句话总结**：Statistical decision algorithms are increasingly deployed in domains where ground-truth labels are hard to obtain, such as hiring, university admissions, and content moderation. In these settings, mod...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mitigating, Label, Bias, Interpretable, Rubric, Embeddings, Statistical, decision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21455v1) | [下载PDF](https://arxiv.org/pdf/2605.21455v1.pdf)

---

## [23. Approximation Theory for Neural Networks: Old and New](https://arxiv.org/abs/2605.21451v1)

**作者**：Soumendu Sundar Mukherjee, Himasish Talukdar  
**分类**：cs.LG, cond-mat.dis-nn, cs.AI, cs.NE  
**发布时间**：2026-05-20

### 📄 论文摘要

Universal approximation theorems provide a mathematical explanation for the expressive power of neural networks. They assert that, under mild conditions on the activation function, feedforward neural networks are dense in broad function classes, such as continuous functions on compact subsets of $\mathbb{R}^d$, $L^p$ spaces, or Sobolev spaces. Over the past four decades, these qualitative universality results have evolved into a rich quantitative theory addressing approximation rates, parameter efficiency, and the role of architectural features such as depth and width. This survey presents several glimpses into this theory. We review classical density results for single-hidden-layer networks, as well as quantitative bounds that relate approximation error to network size and smoothness assumptions on target functions. Particular emphasis is placed on depth--width trade-offs and on results demonstrating that deeper architectures can achieve superior parameter efficiency for structured function classes. In addition to standard feedforward neural networks, we also review recent developments on Kolmogorov--Arnold Networks (KANs), which offer an alternative architectural paradigm and whose approximation-theoretic properties have begun to attract significant theoretical attention.

### 🤖 AI 总结

**一句话总结**：Universal approximation theorems provide a mathematical explanation for the expressive power of neural networks. They assert that, under mild conditions on the activation function, feedforward neural ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Approximation, Theory, Neural, Networks, Old, New, Universal, theorems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21451v1) | [下载PDF](https://arxiv.org/pdf/2605.21451v1.pdf)

---

## [24. torchtune: PyTorch native post-training library](https://arxiv.org/abs/2605.21442v1)

**作者**：Mark Obozov, Maxime Griot, Joseph Cummings 等 11 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-20

### 📄 论文摘要

Modern LLMs typically require multistage training pipelines to achieve strong downstream performance, with post-training serving as the main interface for adapting open-weight models. We introduce torchtune, a PyTorch-native library designed to streamline the post-training lifecycle of LLMs, enabling efficient fine-tuning, experimentation, and deployment-oriented workflows. Unlike many existing fine-tuning frameworks, which often optimize for ease of use, specialized recipes, or hardware efficiency at the cost of transparency and extensibility, torchtune emphasizes modularity, hackability, and direct access to the underlying PyTorch components. In this paper, we present the design principles behind torchtune, describe how they are reflected in its model builders, training recipes, and distributed training stack, and evaluate the library across representative post-training settings. We compare against popular fine-tuning frameworks, including Axolotl and Unsloth, and show that torchtune provides strong performance and memory efficiency across many settings while remaining flexible enough for rapid research iteration. These results position torchtune as a practical foundation for reproducible LLMs post-training research.

### 🤖 AI 总结

**一句话总结**：Modern LLMs typically require multistage training pipelines to achieve strong downstream performance, with post-training serving as the main interface for adapting open-weight models. We introduce tor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, torchtune, PyTorch, native, post-training, library, Modern, typically

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21442v1) | [下载PDF](https://arxiv.org/pdf/2605.21442v1.pdf)

---

## [25. Gaussian Sheaf Neural Networks](https://arxiv.org/abs/2605.21435v1)

**作者**：André Ribeiro, Ana Luiza Tenório, Tiago da Silva 等 4 位作者  
**分类**：cs.LG, math.AT, math.CT  
**发布时间**：2026-05-20

### 📄 论文摘要

Graph Neural Networks (GNNs) have become the de facto standard for learning on relational data. While traditional GNNs' message passing is well suited for vector-valued node features, there are cases in which node features are better represented by probability distributions than real vectors. Concretely, when node features are Gaussians, characterized by a mean and a covariance matrix, naively concatenating their parameters into a single vector and applying standard message passing discards the geometric and algebraic structure that governs means and covariances. We propose Gaussian Sheaf Neural Networks (GSNNs), a principled framework that incorporates these inductive biases into graph-based learning. Building on the theory of cellular sheaves, we derive a new Laplacian operator that generalizes the sheaf Laplacian to this setting and preserves its key properties. We complement our theoretical contributions with experiments on synthetic and real-world data that illustrate the practical relevance of GSNNs.

### 🤖 AI 总结

**一句话总结**：Graph Neural Networks (GNNs) have become the de facto standard for learning on relational data. While traditional GNNs' message passing is well suited for vector-valued node features, there are cases ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Gaussian, Sheaf, Neural, Networks, Graph, GNNs, have, become

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21435v1) | [下载PDF](https://arxiv.org/pdf/2605.21435v1.pdf)

---

## [26. Polynomial-Time Robust Multiclass Linear Classification under Gaussian Marginals](https://arxiv.org/abs/2605.21428v1)

**作者**：Ilias Diakonikolas, Giannis Iakovidis, Mingchen Ma  
**分类**：cs.LG, cs.DS  
**发布时间**：2026-05-20

### 📄 论文摘要

We study the task of agnostic learning of multiclass linear classifiers under the Gaussian distribution. Given labeled examples $(x, y)$ from a distribution over $\mathbb{R}^d \times [k]$, with Gaussian $x$-marginal, the goal is to output a hypothesis whose error is comparable to that of the best $k$-class linear classifier. While the binary case $k=2$ has a well-developed algorithmic theory, much less is known for $k \ge 3$. Even for $k=3$, prior robust algorithms incur exponential dependence on the inverse of the desired accuracy in both complexity and representation size. In this work, we develop new structural results for multiclass linear classifiers and use them to design fully polynomial-time robust learners with dimension-independent error guarantees. Our first result shows that the standard multiclass perceptron algorithm requires super-polynomially many samples and updates, even with clean labels and Gaussian marginals, revealing a basic obstruction absent in the binary case. Our main positive result is a pairwise improper-learning framework which yields an efficient learner with error $\widetilde O(k^{3/2}\sqrt{\mathrm{opt}})+ε$ for general $k$. Additionally, we develop a sharper localization-based framework which leads to error $O(\mathrm{opt})+ε$ for $k=3$, and error $\mathrm{poly}(k)\mathrm{opt}+ε$ for geometrically regular $k$-class linear classifiers.

### 🤖 AI 总结

**一句话总结**：We study the task of agnostic learning of multiclass linear classifiers under the Gaussian distribution. Given labeled examples $(x, y)$ from a distribution over $\mathbb{R}^d \times [k]$, with Gaussi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Polynomial-Time, Robust, Multiclass, Linear, Classification, under, Gaussian, Marginals

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21428v1) | [下载PDF](https://arxiv.org/pdf/2605.21428v1.pdf)

---

## [27. Adaptive Signal Resuscitation: Channel-wise Post-Pruning Repair for Sparse Vision Networks](https://arxiv.org/abs/2605.21426v1)

**作者**：Qishi Zhan, Ziheng Chen, Minxuan Hu  
**分类**：cs.LG  
**发布时间**：2026-05-20

### 📄 论文摘要

One-shot magnitude pruning can cause severe accuracy collapse in the high-sparsity regime, even when the pruning mask preserves the largest weights. We argue that this failure reflects a granularity mismatch in post-pruning repair. Under global magnitude pruning, nearly collapsed channels can coexist with channels that retain informative activation variance within the same layer. Existing layer-wise activation repair methods apply a single correction to the whole layer, and can therefore over-amplify damaged channels while trying to restore the layer-level signal. We propose Adaptive Signal Resuscitation (ASR), a training-free channel-wise repair method that matches the granularity of repair to the granularity of damage. ASR estimates a variance-matching correction for each output channel and stabilizes it with a data-driven shrinkage rule, suppressing unreliable corrections for channels with weak post-pruning signal while preserving corrections for healthier channels. Applied before BatchNorm recalibration, ASR requires only forward passes on a small calibration set and no retraining. Across three datasets, four convolutional architectures, and both unstructured and structured sparsity settings, ASR generally improves over layer-wise repair, with the clearest gains in high-sparsity regimes. On ResNet-50 at 90% sparsity, ASR recovers 55.6% top-1 accuracy on CIFAR-10, compared with 41.0% for layer-wise repair and 28.0% for BatchNorm-only recalibration. Ablations show that naive channel-wise variance matching is insufficient, and that shrinkage stabilizes post-pruning repair.

### 🤖 AI 总结

**一句话总结**：One-shot magnitude pruning can cause severe accuracy collapse in the high-sparsity regime, even when the pruning mask preserves the largest weights. We argue that this failure reflects a granularity m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Adaptive, Signal, Resuscitation, Channel-wise, Post-Pruning, Repair, Sparse, Vision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21426v1) | [下载PDF](https://arxiv.org/pdf/2605.21426v1.pdf)

---

## [28. Preference-aware Influence-function-based Data Selection Method for Efficient Fine-Tuning](https://arxiv.org/abs/2605.21422v1)

**作者**：Qihao Lin, Guanxu Chen, Dongrui Liu 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-20

### 📄 论文摘要

As LLMs continue to scale, improving training efficiency increasingly depends on using data more effectively. Data selection addresses this problem by allocating a limited training budget to samples that best promote a target behavior. Existing methods usually represent the target behavior with a set of target examples, but often treat these examples as equally important. This can be inefficient because target examples may differ in their relevance to the current model: examples closer to the model's current behavior provide more actionable guidance than those farther away. We propose PRISM (PReference-aware Influence-function-based Data Selection Method for Efficient Fine-Tuning), which uses the current model's preference to weight target examples and construct a preference-aware target representation. PRISM then scores candidate training samples by their alignment with this representation, concentrating the data budget on samples more likely to move the model toward the target behavior. Theoretical analysis shows that this preference weighting yields a more effective first-order direction for increasing target-behavior preference. Experiments across model families and scales show that PRISM improves both efficient fine-tuning and safety-oriented SFT repair, demonstrating that precise target-behavior characterization is key to budget-efficient data selection.

### 🤖 AI 总结

**一句话总结**：As LLMs continue to scale, improving training efficiency increasingly depends on using data more effectively. Data selection addresses this problem by allocating a limited training budget to samples t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, Preference-aware, Influence-function-based, Data, Selection, Method, Efficient, Fine-Tuning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21422v1) | [下载PDF](https://arxiv.org/pdf/2605.21422v1.pdf)

---

## [29. HiRes: Inspectable Precedent Memory for Reaction Condition Recommendation](https://arxiv.org/abs/2605.21420v1)

**作者**：Shreyas Vinaya Sathyanarayana, Raja Sekhar Pappala, Deepak Warrier  
**分类**：cs.LG, cs.AI, q-bio.MN  
**发布时间**：2026-05-20

### 📄 论文摘要

Reaction condition recommendation sits immediately after retrosynthetic disconnection selection, and in practice, chemists require both accurate predictions and the precedents that justify them. We present HiRes (Hierarchical Reaction Representations), a retrieval-augmented condition recommendation system whose learned reaction space serves as both a classifier feature and an inspectable precedent memory. The model combines a graph encoder, transformation-aware cross-attention, multi-stream reaction fusion, and a k-NN retrieval layer. HiRes achieves state-of-the-art performance among primary-slot USPTO-Condition models, reaching Catalyst, Solvent, and Reagent top-1 accuracies (Acc@1) of 0.929, 0.534, and 0.530 respectively. It ties the best reported baseline on Catalyst while outperforming models such as REACON on Solvent and Reagent. Furthermore, paired bootstrap analysis demonstrates that integrating retrieval with learned condition heads provides statistically significant gains for solvent and reagent selection over purely parametric approaches. Ultimately, HiRes bridges the gap between predictive accuracy and chemical interpretability, offering a single representation that supplies both competitive recommendations and the concrete chemical precedents necessary for practical synthesis planning.

### 🤖 AI 总结

**一句话总结**：Reaction condition recommendation sits immediately after retrosynthetic disconnection selection, and in practice, chemists require both accurate predictions and the precedents that justify them. We pr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HiRes, Inspectable, Precedent, Memory, Reaction, Condition, Recommendation, sits

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21420v1) | [下载PDF](https://arxiv.org/pdf/2605.21420v1.pdf)

---

## [30. FedCritic: Serverless Federated Critic Learning-based Resource Allocation for Multi-Cell OFDMA in 6G](https://arxiv.org/abs/2605.21418v1)

**作者**：Amin Farajzadeh, Melike Erol-Kantarci  
**分类**：cs.LG, cs.AI, cs.CV, cs.NI  
**发布时间**：2026-05-20

### 📄 论文摘要

In sixth-generation (6G) ultra-dense networks, aggressive frequency reuse amplifies inter-cell interference (ICI), making multi-cell orthogonal frequency-division multiple access (OFDMA) scheduling and power control strongly coupled across neighboring cells. We study distributed downlink resource management -- joint subcarrier scheduling and power allocation -- under interference coupling and long-term per-user quality-of-service (QoS) minimum-rate constraints. By using virtual-queue deficit weights to enforce long-term QoS, we develop FedCritic, a serverless federated multi-agent actor-critic framework with decentralized execution. Unlike centralized training with decentralized execution (CTDE) approaches that require centralized critic learning and joint trajectory aggregation, FedCritic federates the critic through lightweight gossip-based parameter averaging over the interference graph, enabling stable value estimation without a central coordinator while keeping policies local. Simulations in an interference-rich reuse-1 setting show that FedCritic improves mean signal-to-interference-plus-noise ratio (SINR) and cell-edge rate, increases network-wide average sum-rate and fairness relative to non-coordinated and CTDE baselines, and achieves more stable training with lower coordination overhead.

### 🤖 AI 总结

**一句话总结**：In sixth-generation (6G) ultra-dense networks, aggressive frequency reuse amplifies inter-cell interference (ICI), making multi-cell orthogonal frequency-division multiple access (OFDMA) scheduling an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FedCritic, Serverless, Federated, Critic, Learning-based, Resource, Allocation, Multi-Cell

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.21418v1) | [下载PDF](https://arxiv.org/pdf/2605.21418v1.pdf)

---

