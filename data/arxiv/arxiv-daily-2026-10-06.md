# arXiv AI 论文日报 | 2026-10-06

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (5 篇)
- [cs.AI](#csAI) (4 篇)
- [cs.LG](#csLG) (13 篇)
- [cs.CL](#csCL) (8 篇)

---

## cs.AI

## [1. BiasFlow: Geometric Monitoring and Backbone Regularization for Spurious Feature Reliance](https://arxiv.org/abs/2610.06846v1)

**作者**：Haojin Deng, Zhiping Lin, Yimin Yang  
**分类**：cs.AI  
**发布时间**：2026-10-05

### 📄 论文摘要

Worst-group accuracy (WGA) evaluates a trained predictor but does not characterize how its frozen backbone behaves when a new head is learned. We introduce BiasFlow, a hook-based toolkit for monitoring class-attribute centroid alignment (IBMI), within-class centroid separation (W-IBMI), and feature-projection sensitivity. IBMI is confounded by class-attribute correlation and is not a measure of causal feature reliance. We pair these diagnostics with BiasFlow Regularization (BFR), a supervised, composable class-conditional centroid-alignment penalty. W-IBMI verifies the quantity BFR optimizes; it is scale dependent and does not independently establish attribute removal. Across the reported small-scale benchmarks, adding BFR improves or preserves mean WGA, with gains up to +26.0 pp on UrbanCars. The principal independent stress test freezes CelebA-Std backbones and trains fresh heads on biased data: BFR+GroupDRO improves WGA from 40.7% to 64.1%, while Male probe accuracy decreases from 92.5% to 72.2%. Attribute information remains recoverable, and cross-task results are mixed. A controlled synthetic-watermark ImageNet experiment additionally improves watermark-shift accuracy by +23.0 pp under matched training. These results support evaluating centroid geometry and resistance to biased head retraining alongside WGA, within the tested protocols.

### 🤖 AI 总结

**一句话总结**：Worst-group accuracy (WGA) evaluates a trained predictor but does not characterize how its frozen backbone behaves when a new head is learned. We introduce BiasFlow, a hook-based toolkit for monitorin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BiasFlow, Geometric, Monitoring, Backbone, Regularization, Spurious, Feature, Reliance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06846v1) | [下载PDF](https://arxiv.org/pdf/2610.06846v1.pdf)

---

## [2. TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts](https://arxiv.org/abs/2610.06824v1)

**作者**：Oliver Jaffe, Dane Sherburn  
**分类**：cs.AI  
**发布时间**：2026-10-05

### 📄 论文摘要

We introduce TasteVal, a benchmark to evaluate the experimental research taste of frontier models. We define research taste as the ability to pick interesting problems to solve, design experiments, and interpret experimental results. TasteVal measures the experimental component of research taste; given a fixed research problem, we measure how well a model iteratively designs experiments and draws conclusions from their outcomes. We operationalize experimental research taste as compute efficiency; a Researcher who reaches the same score as an expert human using half the serial experimental compute has twice the experimental taste. Experimental taste thus acts as a multiplier on experimental compute, making it a key input to forecasts of AI progress. TasteVal consists of 8 novel, challenging, open-ended tasks representative of frontier AI R&D. To isolate taste from coding ability, the model under evaluation acts as a Researcher that iteratively designs experiments while a fixed Coder agent implements them and reports their results. The Researcher executes until either the 40 H100 hour or 120 wall-clock hour budgets are exhausted. We recruit 24 human experts, at least 2 per task, and take the best expert attempt per task as the expert baseline. We evaluate 20 models released between 2023 and 2026. The best-performing model, Opus 5.5, exceeds our expert baseline, with a compute multiplier of 2.3x (95% CI 1.15-4.37), at roughly 1/30 of our baseliners' average per-run cost. On TasteVal, the compute multiplier of frontier models has doubled approximately every 3.0 months since December 2025 (95% CI 1.7-5.0), up from every 14 months between 2023 and December 2025. Measured by final normalized performance, frontier models show no trend break, doubling every 14.6 months. To keep TasteVal uncontaminated, we do not release the tasks.

### 🤖 AI 总结

**一句话总结**：We introduce TasteVal, a benchmark to evaluate the experimental research taste of frontier models. We define research taste as the ability to pick interesting problems to solve, design experiments, an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, TasteVal, Measuring, Experimental, Research, Taste, Systems, Against

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06824v1) | [下载PDF](https://arxiv.org/pdf/2610.06824v1.pdf)

---

## [3. Back to the Future: Rethinking EDA Infrastructure for Agentic Systems in Chip Design Verification](https://arxiv.org/abs/2610.06790v1)

**作者**：Je Yang, Ivan Lobov, Thomas Karpati  
**分类**：cs.AI  
**发布时间**：2026-10-05

### 📄 论文摘要

The unprecedented computational scale of modern artificial intelligence depends on complex, multi-billion-transistor Systems-on-Chip, yet the workflows that verify these chips remain stubbornly manual. Although Large Language Models (LLMs) have made rapid inroads into Electronic Design Automation (EDA), approximately 74.6% of existing studies target static Register-Transfer Level (RTL) code generation, leaving post-simulation verification and interactive waveform debugging largely untouched. We introduce Back-to-the-Future (BTTF), an end-to-end agentic framework that closes this infrastructural gap. BTTF distills massive, unstructured simulation dumps into a normalized relational SQLite database and couples it with a collaborative multi-agent orchestration engine that translates natural-language verification queries into schema-aware SQL while correlating signal anomalies with versioned RTL repositories. Across a 150-query benchmark, BTTF attains 95.33% execution accuracy, charting a practical path toward autonomous EDA verification.

### 🤖 AI 总结

**一句话总结**：The unprecedented computational scale of modern artificial intelligence depends on complex, multi-billion-transistor Systems-on-Chip, yet the workflows that verify these chips remain stubbornly manual...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Back, Future, Rethinking, EDA, Infrastructure, Agentic, Systems, Chip

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06790v1) | [下载PDF](https://arxiv.org/pdf/2610.06790v1.pdf)

---

## [4. Conditional Rank Allocation for Taxonomy-Aware Medical Language Model Adaptation](https://arxiv.org/abs/2610.06765v1)

**作者**：Guangyuan Dong, Ziwei Hong, Xuehao Zhou 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-05

### 📄 论文摘要

Medical question answering spans specialties and clinical operations that may benefit from different adaptation directions. We propose ARBOR, a parameter-efficient method that selects rank-one components from a shared low-rank basis for each question. An additive gate combines question representations, specialty tags, operation tags, and their interaction; a learned coefficient scales the adapter residual. An illustrative separation under orthogonal, equiprobable subtasks shows how conditional selection can avoid an approximation floor faced by a fixed update with the same active rank. This result motivates the design without asserting a corresponding bound for medical corpora. On Qwen3-8B across CMB, CMExam, MedQA, and MedMCQA, five-seed experiments yield 69.69% mean accuracy across benchmarks, exceeding LoRA r16 and MoELoRA by 1.26 and 1.30 percentage points, respectively. The reported advantage over LoRA r16 increases from 0.08 to 1.94 points as training expands from one to seven specialties. Tag perturbations and atom masking support the usefulness of clinical routing, while atom clusters align with the supplied specialty labels (adjusted Rand index 0.62). Calibration, transfer, and measured costs further characterize the method. These findings support structured conditional adaptation for medical QA, while leaving clinical safety and broader deployment untested.

### 🤖 AI 总结

**一句话总结**：Medical question answering spans specialties and clinical operations that may benefit from different adaptation directions. We propose ARBOR, a parameter-efficient method that selects rank-one compone...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Conditional, Rank, Allocation, Taxonomy-Aware, Medical, Language, Model, Adaptation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06765v1) | [下载PDF](https://arxiv.org/pdf/2610.06765v1.pdf)

---

## cs.CL

## [5. MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents](https://arxiv.org/abs/2610.06830v1)

**作者**：Haozhen Zhang, Haodong Yue, Quanyu Long 等 9 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-10-05

### 📄 论文摘要

Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessing cost and discard details that later prove essential. Recent studies have begun shifting memory processing toward runtime adaptation, but typically specialize in particular operations or fixed processing schemes, leaving flexible control over performance, cost, and latency largely underexplored. To address this challenge, we present \textbf{MemPilot}, a flexible framework that orchestrates on-demand memory curation under different performance--cost--latency preferences. Specifically, we optimize a multi-step LLM policy via reinforcement learning to iteratively choose between retrieving from query-agnostic memory and delegating query-specific curation of raw multimodal history to heterogeneous LLMs and VLMs. The policy jointly controls evidence amount, curation instructions, model selection, and visual access, enabling fine-grained allocation of runtime computation. To optimize this policy under competing objectives, we adapt objective-wise advantage decoupling by separately estimating each objective's advantage before aggregation. Moreover, we introduce prefix-based marginal utility estimation for fine-grained credit assignment across multi-step rollouts. Experiments on five multimodal agent-memory benchmarks demonstrate favorable performance--cost--latency trade-offs across optimization preferences, with preference sweeps yielding broader frontiers than existing trade-off-aware baselines.

### 🤖 AI 总结

**一句话总结**：Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, MemPilot, Orchestrating, On-Demand, Multimodal, Memory, Curation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06830v1) | [下载PDF](https://arxiv.org/pdf/2610.06830v1.pdf)

---

## [6. CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling](https://arxiv.org/abs/2610.06829v1)

**作者**：Yifan Zhang, Yutong Dai, Viraj Prabhu 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-10-05

### 📄 论文摘要

Open-source web agents are now strong enough to execute realistic browser tasks, but training them with reinforcement learning still depends on weak supervision: binary task success is too sparse for credit assignment, while frontier-language-model judges are too expensive to call at every step and cannot be assumed available at deployment. We introduce CLIFT, a training and test-time scaling method built around conformal self-verification. During training, the agent answers natural-language verification questions about its own rollouts; a Compositional Conformal Certifier keeps only question signals whose URL-conditional evidence agrees with a training-time judge, assigns signed trust weights through polarity-aware lift, and blends the resulting verifier score into per-step rewards in a way that never subtracts from the judge baseline. At test time, the same certified bank is frozen and reused as structured evidence for Conformal Trajectory Selection (CTS): the agent samples a greedy rollout and one or more diverse retries, the self-verifier summarises each URL trace, and a conservative majority-vote rule chooses whether to swap away from the current incumbent without calling any external judge. This single mechanism supports three settings. On WebArena Infinity, CLIFT achieves state-of-the-art performance among open-source web agents. On VisualWebArena, a bank trained with the open model transfers to GPT-5.5 at test time and reaches state-of-the-art performance under the canonical harness. On Online Mind2Web, without training an agent on the benchmark, translating the certified question bank improves a live-web agent in zero-shot evaluation. Together these results position conformal self-verification as a way to turn costly judge feedback into a reusable training signal and a judge-free test-time scaling signal.

### 🤖 AI 总结

**一句话总结**：Open-source web agents are now strong enough to execute realistic browser tasks, but training them with reinforcement learning still depends on weak supervision: binary task success is too sparse for ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, CLIFT, Conformal, Self-Verification, Web, Training, Test-Time, Scaling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06829v1) | [下载PDF](https://arxiv.org/pdf/2610.06829v1.pdf)

---

## [7. PlotGround: Grounding Plot Digitization in Real Scientific Figures and Their Source Data](https://arxiv.org/abs/2610.06825v1)

**作者**：Yaohui Zhang, Binxu Li, Haoyi Duan 等 10 位作者  
**分类**：cs.CL, cs.CV  
**发布时间**：2026-10-05

### 📄 论文摘要

Scientific figures often encode quantitative results that are not readily available in machine-readable form, making accurate plot digitization important for verifying and reusing published findings. Yet it remains unclear how accurately current models recover plotted values from real scientific figures, as existing benchmarks rely largely on synthetic charts or cover only a limited range of chart types. We introduce PlotGround, an automated pipeline for building plot digitization benchmarks from real scientific figures and their author-released source data. PlotGround maps figures to source tables, identifies reconstructable panels, and generates quantitative questions with source-grounded reference values. We use PlotGround to construct PlotGround-1k, a human-verified benchmark of 1,119 questions from 1,066 bioRxiv preprints. Across sixteen multimodal models, the best reaches 87.5% accuracy at a $\pm 5\%$ relative-error tolerance. Tightening the tolerance to $\pm 2\%$ lowers every model's accuracy by 11-24 percentage points, revealing a gap between approximate visual reading and precise quantitative recovery. PlotGround's paired figure-source structure lets us compare how accurately the same values are recovered from figures and from source tables. Providing source tables instead of figures raises a coding agent's accuracy from 90.0% to 97.4% while cutting cost by 72%.

### 🤖 AI 总结

**一句话总结**：Scientific figures often encode quantitative results that are not readily available in machine-readable form, making accurate plot digitization important for verifying and reusing published findings. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PlotGround, Grounding, Plot, Digitization, Real, Scientific, Figures, Their

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06825v1) | [下载PDF](https://arxiv.org/pdf/2610.06825v1.pdf)

---

## [8. T-Search: An Open Agentic Retriever and Playground for Hard Multi-Step Search](https://arxiv.org/abs/2610.06782v1)

**作者**：Olga Tsymboi, Ramil Latypov, Aleksandr Medvedev 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-05

### 📄 论文摘要

We present T-Search, an open-weight agentic retriever for hard multi-step search. Given a question and a search tool over a fixed corpus, it runs a bounded multi-round search and returns a ranked list of evidence chunks with short justifications, leaving answer generation to a downstream model, so backend and generator can be swapped without retraining. T-Search is built on Qwen3.6-35B-A3B and trained on adversarially filtered synthetic search tasks with round-sliced supervised fine-tuning followed by GSPO on a recall reward. Averaged over seven English and Russian benchmarks with gold evidence annotations, it reaches 56.0 Recall@10 with one rollout, 14.4 points above its base, and 61.3 with three fused rollouts, outperforming larger open models. We release the model, harness, live demo, and three benchmarks, including TRuST, the first native-Russian hard-search benchmark.

### 🤖 AI 总结

**一句话总结**：We present T-Search, an open-weight agentic retriever for hard multi-step search. Given a question and a search tool over a fixed corpus, it runs a bounded multi-round search and returns a ranked list...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, T-Search, Open, Agentic, Retriever, Playground, Hard, Multi-Step

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06782v1) | [下载PDF](https://arxiv.org/pdf/2610.06782v1.pdf)

---

## [9. IdeaLens: Detecting AI Ideas in Long-form Writing](https://arxiv.org/abs/2610.06778v1)

**作者**：Rishanth Rajendhran, Minjoon Choi, Jenna Russell 等 8 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-10-05

### 📄 论文摘要

While modern AI detectors identify who wrote the words, emerging policies on AI use increasingly hinge on a different question: who came up with the ideas? We introduce IdeaLens, a detector that identifies whether a document's ideas came from a human or AI (idea provenance), regardless of who wrote its words. To focus IdeaLens on ideas rather than prose, we represent documents as outlines: lists of items that each pair a discourse role with a brief, paraphrased description of the content, minimizing word-level overlap with the raw text. We train IdeaLens on 1M FineWeb documents with silver labels from Pangram, a prose provenance detector. Since the outlines are largely stripped of surface-level information, the labels must be fit mainly through the ideas. In a controlled study, IdeaLens's AI flag rate drops from 95% to 7% as models write from increasingly detailed human plans, while Pangram 4 still flags 92%; from AI-derived plans, IdeaLens stays above 96%. Conversely, on a new dataset of 50 stories that human authors wrote from AI-generated plans, IdeaLens flags 68% of the stories as AI, compared to 8% for Pangram 4. On a comprehensive suite of 19 existing detection benchmarks, we show that IdeaLens maintains strong detection rates at low false positive rates, suggesting that ideas themselves provide a powerful discriminative signal, and its performance holds across domains, formats, and languages. Finally, we examine 90K predictions from IdeaLens to characterize systematic differences between human and AI ideation. We release our models and labeled datasets to facilitate future research on idea provenance detection.

### 🤖 AI 总结

**一句话总结**：While modern AI detectors identify who wrote the words, emerging policies on AI use increasingly hinge on a different question: who came up with the ideas? We introduce IdeaLens, a detector that ident...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IdeaLens, Detecting, Ideas, Long-form, Writing, While, modern, detectors

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06778v1) | [下载PDF](https://arxiv.org/pdf/2610.06778v1.pdf)

---

## [10. ufakzeka-karar: An Open Turkish Typed-Decision Model with Order-Invariant Option Scoring](https://arxiv.org/abs/2610.06744v1)

**作者**：Sait Furkan Teke  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-10-05

### 📄 论文摘要

ufakzeka-karar is an open Turkish decision model with 182,494,466 parameters. Given a Turkish text and questions of a fixed answer type (a choice, a level on an ordered scale, or yes or no), it returns a temperature-scaled probability for every option and an expected error that serves as a "not sure" signal, without generating text and in one CPU forward pass for up to ten options. Built on the lab's ufakzeka-1-base, its head scores each option blind to the others at shared positions, so the answer does not depend on option order. A sequential head trained with shuffled options was about as accurate but changed 2.3 to 2.8 percent of its answers when only the option order changed; REINFORCE lost 10.2 points (0.102) of macro F1 to cross-entropy. On the open set of HakemBench v1.0 (4,275 questions, 7 tracks) the released model ranks 7th of 16 rows with a composite of 0.660 (95% interval 0.642 to 0.677). Temperature scaling lowers calibration error (smooth ECE) on the development set but raises it on held-out support questions, from 0.027 to 0.045 for the first scored run, which never trained on them; the released model later trained on them, so its 0.036 to 0.064 is not an unseen-question test. The released model is the last of three runs scored on HakemBench, and its numbers are not blind. The second run's new training data was aimed at the first run's errors on the full test set in guardrails, moderation and customer support, and the released run was trained after the second run's guardrail results on the full test set were read, under a protocol fixed in writing before any of its data, code or runs. All its numbers come after these readings; its guardrail, moderation and customer support numbers carry the flag "shaped by reading the test results". With every model scored on the other four tracks only, its composite is 0.678, 6th of 16. Weights and code are under Apache-2.0.

### 🤖 AI 总结

**一句话总结**：ufakzeka-karar is an open Turkish decision model with 182,494,466 parameters. Given a Turkish text and questions of a fixed answer type (a choice, a level on an ordered scale, or yes or no), it return...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, ufakzeka-karar, Open, Turkish, Typed-Decision, Model, Order-Invariant, Option

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06744v1) | [下载PDF](https://arxiv.org/pdf/2610.06744v1.pdf)

---

## [11. Improving Diversity in LLM Short Story Generation](https://arxiv.org/abs/2610.06729v1)

**作者**：Zahra Solati Dehkordi, Vasileios Lampos  
**分类**：cs.CL  
**发布时间**：2026-10-05

### 📄 论文摘要

Large language models (LLMs) can generate accurate responses, but these are void of diversity. We attempt to address this for the task of creative short story generation. Drawing on established writing conventions and known LLM limitations, we target variation in genre, tone, style, and named entities. To promote diversity across these dimensions, we introduce DivLM, an LLM post-training framework consisting of two phases. First, we perform continued pre-training on a creative writing corpus and restore instruction-following capabilities using weight residuals. We then apply reinforcement learning with a custom, composite reward function that jointly maximizes diversity across the targeted narrative dimensions while maintaining response quality. Our empirical results on two LLM families show that DivLM increases diversity metrics by more than 9% on average compared to alternative approaches, while preserving instruction following, overall response quality, and similarity to human outputs.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) can generate accurate responses, but these are void of diversity. We attempt to address this for the task of creative short story generation. Drawing on established writin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Improving, Diversity, Short, Story, Generation, Large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06729v1) | [下载PDF](https://arxiv.org/pdf/2610.06729v1.pdf)

---

## [12. SAFE-MR: Evidence Sufficiency Learning for Selective Multimodal Rumor Detection](https://arxiv.org/abs/2610.06708v1)

**作者**：Shiwen Ni  
**分类**：cs.CL  
**发布时间**：2026-10-05

### 📄 论文摘要

Multimodal rumor detectors increasingly rely on retrieved evidence, yet relevant evidence is not necessarily sufficient for verification. Missing provenance, duplicated reports, and unresolved contradictions can produce confident predictions without adequate support. We introduce SAFE-MR, a framework that separates claim veracity from evidence sufficiency. The method decomposes image-text posts into verifiable claims, constructs a relation-aware claim-evidence graph, and aggregates evidence using provenance and contextual compatibility. Separate veracity and sufficiency heads support selective prediction, while evidence interventions encourage stability under irrelevant additions and sensitivity to evidence removal. On NewsCLIPpings, VERITE, and XFacta, SAFE-MR achieves macro-F1 scores of 91.2%, 75.8%, and 85.2%, respectively. Against the matched backbone with evidence, its macro-F1 gains are 2.2, 4.9, and 4.8 percentage points. On the diagnostic selection set, SAFE-MR reduces AURC from 0.105 for maximum-probability rejection to 0.075 and lowers error at 80% coverage from 13.8% to 8.5%. Evidence-perturbation and ablation results support the role of sufficiency learning and intervention training in improving selective verification.

### 🤖 AI 总结

**一句话总结**：Multimodal rumor detectors increasingly rely on retrieved evidence, yet relevant evidence is not necessarily sufficient for verification. Missing provenance, duplicated reports, and unresolved contrad...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SAFE-MR, Evidence, Sufficiency, Learning, Selective, Multimodal, Rumor, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06708v1) | [下载PDF](https://arxiv.org/pdf/2610.06708v1.pdf)

---

## cs.CV

## [13. One Figure, Every Canvas: Editable Flowchart Relayout via Agentic Pipeline](https://arxiv.org/abs/2610.06852v1)

**作者**：Shih-Chen Tseng, Chih-Hsuan Chen, Ryan Yang 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-10-05

### 📄 论文摘要

Pipeline figures in ML papers must be repurposed across many canvases, including paper columns, 16:9 slides, portrait posters, 1:1 social teasers, 9:16 phone previews. Each format imposes a different aspect ratio on the same computational graph, where any silently broken connection misrepresents the method. We formulate aspect-ratio-adaptive flowchart relayout as a distinct task: given a raster flowchart and a target ratio, produce a structurally faithful, hallucination-free, editable layout. Existing methods fail characteristically: image-to-image models stretch blocks and reject extreme ratios, text-to-image agentic systems hallucinate content, and parse-then-render systems mis-route edges. We propose an agentic pipeline factored into Parse, Style, and Layout stages, each pairing a main agent with a critic that combines deterministic constraint checks with VLM visual feedback so connectivity is explicitly checked and prevented from being silently broken. Outputs are draw.io-editable mxGraph XML. On a curated benchmark of 100 flowcharts at five aspect ratios, evaluated by Gemini 3.1 Pro and validated against human judgments, our method reaches 68.6% Content Fidelity versus 11.2-41.4% for prior work. Project page: https://onefigureeverycanvas.vercel.app/

### 🤖 AI 总结

**一句话总结**：Pipeline figures in ML papers must be repurposed across many canvases, including paper columns, 16:9 slides, portrait posters, 1:1 social teasers, 9:16 phone previews. Each format imposes a different ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：One, Figure, Every, Canvas, Editable, Flowchart, Relayout, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06852v1) | [下载PDF](https://arxiv.org/pdf/2610.06852v1.pdf)

---

## [14. Anatomy-aware Fine-grained Multimodal Fusion for Laryngopharyngeal Cancer T-Staging Prediction Using CT and Radiology Report](https://arxiv.org/abs/2610.06837v1)

**作者**：Xingyue Zhao, Yanzhou Su, Fang Zhang 等 15 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-05

### 📄 论文摘要

Accurate T-staging is crucial for guiding personalized treatment strategies for laryngopharyngeal cancer. However, current clinical practice relies on invasive biopsy procedures, whereas CT-based staging remains challenging due to the complex patterns of tumor invasion. Recent computer-aided approaches face two key challenges: 1) Structural relationship modeling: existing methods underrepresent anatomically structured patterns of tumor invasion, as they either process whole CT volumes without tumor-specific anatomical constraints or rely on labor-intensive tumor segmentation. 2) Fine-grained cross-modal alignment: while radiology reports contain organ-specific invasion details, current methods that apply global feature fusion struggle to accurately align individual anatomical structures with their corresponding textual descriptions. To address these issues, we propose an anatomy-aware multimodal framework that integrates organ-level CT context and radiology reports into a unified representation for laryngopharyngeal T-staging. The framework first constructs an Anatomy-Structured Organ Graph (AOG) that captures invasion patterns between primary sites and surrounding organs, then performs Organ-Anchored Cross-Modal Alignment (OCA) so that each organ node aggregates textual evidence from the radiology report, and finally refines this graph representation by injecting organ-specific invasion cues extracted from the report via Report-Enhanced Graph-Refinement (REG), yielding a multimodal organ graph that combines spatial and textual evidence. Extensive experiments demonstrate that the proposed framework achieves superior performance in T-staging of laryngopharyngeal cancer.

### 🤖 AI 总结

**一句话总结**：Accurate T-staging is crucial for guiding personalized treatment strategies for laryngopharyngeal cancer. However, current clinical practice relies on invasive biopsy procedures, whereas CT-based stag...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Anatomy-aware, Fine-grained, Multimodal, Fusion, Laryngopharyngeal, Cancer, T-Staging, Prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06837v1) | [下载PDF](https://arxiv.org/pdf/2610.06837v1.pdf)

---

## [15. UniSlider: Perceptually Uniform Sliders for Continuous Image Editing](https://arxiv.org/abs/2610.06831v1)

**作者**：David Serrano-Lozano, Duygu Ceylan, Yannick Hold-Geoffroy 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-10-05

### 📄 论文摘要

Sliders provide an intuitive interface for continuous image editing. In current generative approaches, however, the slider is simply a rescaling of the method's strength parameter, such as an adapter coefficient, a prompt weight, or an interpolation factor. This strength relates poorly to perceptual change. The image can partially revert as the slider moves, long stretches of the range produce no visible difference, and short intervals transform the image abruptly. Remapping the strength could fix this uneven pace, but only if the trajectory is monotone, which current methods do not enforce. We therefore distinguish the slider from the strength, and require perceptual distance from the input to grow linearly with the slider value. We introduce UniSlider, a lightweight LoRA trained on a few-step editing backbone so that its strength approximates this ideal slider. Few-step sampling lets us impose this objective in pixel space without intermediate ground truth, and the backbone's output is preserved at full strength. However, a low-rank adapter cannot make the strength fully uniform. Our slider is thus an inference-time remapping of the strength, obtained by adaptive sampling. Since training optmizes to make the trajectory monotone, this remapping closes the remaining gap without extra training or parameters. On a new benchmark of 300 continuous edits evaluating uniformity, monotonicity, edit fidelity, and identity preservation, UniSlider outperforms all prior methods and is preferred in a user study.

### 🤖 AI 总结

**一句话总结**：Sliders provide an intuitive interface for continuous image editing. In current generative approaches, however, the slider is simply a rescaling of the method's strength parameter, such as an adapter ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UniSlider, Perceptually, Uniform, Sliders, Continuous, Image, Editing, provide

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06831v1) | [下载PDF](https://arxiv.org/pdf/2610.06831v1.pdf)

---

## [16. TAPDreamer: Transferable Adversarial Patches for World Action Models](https://arxiv.org/abs/2610.06814v1)

**作者**：Xuanyu Lu, Fengqing Jiang, Kaiyuan Zheng 等 11 位作者  
**分类**：cs.CV, cs.AI, cs.RO  
**发布时间**：2026-10-05

### 📄 论文摘要

World models learn to predict how their environment will evolve, making them an important foundation for general-purpose robotic control. Yet world action models depend on camera inputs whose manipulation can corrupt the visual representations used across tasks and action policies. Existing attacks on these models optimize against the victim's actions or predicted futures and therefore require access to target-model outputs. In this paper, we propose an attack, TAPDreamer, against world action models that instead uses a public encoder alone to construct a fixed local perturbation that transfers across tasks and action architectures. TAPDreamer requires no target-policy queries. Our key insight is that interactions between patch-induced changes in attention weights and value vectors broadcast a nearly identical representation shift far beyond the patch footprint, and this shift remains stable across task observations. Guided by this insight, TAPDreamer uses six frames from one source task to maximize the global L1 distance between clean and patched encoder representations. In closed-loop evaluation, one frozen patch per benchmark, covering about 6.5% of the input, reduces FastWAM's success rate from 97.7% to 0.0% across 40 LIBERO tasks and from 90.8% to 0.0% across 50 RoboTwin tasks; matched random patches retain 81.5% and 79.2% success. The same patches reduce success to 2.1% and 0.8% on two DreamWAM configurations and to 10.0% on Motus. These results show that protecting downstream action generation alone is insufficient: defenses for world action models must also secure shared visual encoders against persistent local perturbations.

### 🤖 AI 总结

**一句话总结**：World models learn to predict how their environment will evolve, making them an important foundation for general-purpose robotic control. Yet world action models depend on camera inputs whose manipula...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TAPDreamer, Transferable, Adversarial, Patches, World, Action, Models, learn

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06814v1) | [下载PDF](https://arxiv.org/pdf/2610.06814v1.pdf)

---

## [17. Extending Dynamic World Surface Water Mapping to Sentinel-1 with AlphaEarth Embeddings](https://arxiv.org/abs/2610.06704v1)

**作者**：Rohit Mukherjee, Frederick Policelli, Beth Tellman 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-05

### 📄 论文摘要

Dynamic World (DW) maps land use and land cover globally at 10 m from Sentinel-2 (S2) imagery, but only for cloud-free observations, which limits where and when surface water can be mapped. We use the DW water class as weak supervision for a Sentinel-1 (S1) synthetic aperture radar (SAR) model so that DW-like water maps can be produced for every S1 acquisition. Google's AlphaEarth Foundations (AEF) annual embedding supplies spatial context, while S1 backscatter supplies the acquisition-time observation. On 53 globally distributed scenes with independent annotations of 3 m PlanetScope imagery acquired within 48 h of the S1 overpass, the S1-only model already reaches a pooled water intersection over union (IoU) of 0.77, comparable to 0.75 for the operational OPERA DSWx-S1 product, and adding AEF raises it to 0.85. The fused model improves on the S1-only model on 44 of 53 scenes and exceeds OPERA on 48, and on the independent S1S2-Water benchmark it reaches 0.94, compared with 0.87 for OPERA. Optical land-cover products can thus provide scalable training labels for SAR surface water mapping.

### 🤖 AI 总结

**一句话总结**：Dynamic World (DW) maps land use and land cover globally at 10 m from Sentinel-2 (S2) imagery, but only for cloud-free observations, which limits where and when surface water can be mapped. We use the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Extending, Dynamic, World, Surface, Water, Mapping, Sentinel-1, AlphaEarth

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06704v1) | [下载PDF](https://arxiv.org/pdf/2610.06704v1.pdf)

---

## cs.LG

## [18. Towards Looped Models Done Right, Part II: Rethinking at Fixed Points](https://arxiv.org/abs/2610.06833v1)

**作者**：Benhao Huang, Chufan Shi, Junlin Chen 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-05

### 📄 论文摘要

Every recurrence of a looped language model adds cost in training, decoding, prefill, and reinforcement learning (RL). The closer recurrent states get to fixed points, the less the path to them matters. This enables truncated backpropagation in training; terminal key-value (KV) sharing for decoding with almost no loss in accuracy; a distilled student that prefills up to 1.79x faster; and RL updates that compute gradients from saved rollout states, 2x faster than backpropagating through the replayed trajectory. We therefore improve the two components of training that shape these fixed points: the depth prior and input injection. Fixed-depth training breaks KV sharing, and Huginn's broad depth prior supports sharing but dilutes supervision at the target depth more than sharing requires; we learn the prior from prediction feedback, with an entropy term that keeps it broad. Existing injection schemes let the state's component along the input amplify or cancel the injection; we remove this component with orthogonal injection. From 100M to 1.6B parameters, the learned prior and orthogonal injection lower perplexity at every scale relative to Huginn's prior and existing injection schemes, respectively. At 1.6B, the learned prior with a 3x smaller KV cache matches the downstream average of fixed-depth training with the full cache.

### 🤖 AI 总结

**一句话总结**：Every recurrence of a looped language model adds cost in training, decoding, prefill, and reinforcement learning (RL). The closer recurrent states get to fixed points, the less the path to them matter...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：II, Towards, Looped, Models, Done, Right, Part, Rethinking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06833v1) | [下载PDF](https://arxiv.org/pdf/2610.06833v1.pdf)

---

## [19. Deep Learning for Sleep Heart Rate Estimation from Accelerometers: Toward Population-Scale Cardiac Insight Without Optical Sensors](https://arxiv.org/abs/2610.06823v1)

**作者**：Tanbin Islam Rohan, Pranjol Sen Gupta, Tanusree Debi 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-05

### 📄 论文摘要

Large longitudinal cohorts often contain wrist accelerometry without optical heart-rate sensing, motivating recovery of cardiac information from motion signals already collected during sleep. We present SeqSmoother, a transformer-based temporal corrector for sleep heart rate (HR) estimation from wrist accelerometry. SeqSmoother combines spectral descriptors with an intermediate Nightbeat-derived frequency anchor and a physics-motivated sub-harmonic feature designed to identify harmonic frequency lock-on. All inference-time features are derived from wrist accelerometry, while ECG is used only to construct reference HR labels and training-label quality weights. We evaluate SeqSmoother using 13 participant-disjoint held-out folds and compare it with the official Nightbeat implementation under a matched 60-s window and 15-s step protocol. Across all out-of-fold predictions, SeqSmoother achieved a participant-macro MAE of 1.60 bpm. On Nightbeat-retained matched intervals, Nightbeat achieved lower absolute error than SeqSmoother (0.615 versus 1.091 bpm), while SeqSmoother provided estimates over a larger portion of the eligible recording; Nightbeat produced final estimates for 72.85% of the SeqSmoother-eligible out-of-fold grid. Separately, the proposed sub-harmonic ratio achieved an AUROC of 0.972 for identifying reference-defined harmonic lock-on candidates. These findings reveal an accuracy-availability trade-off between learned temporal modeling and quality-gated signal processing while providing empirical support for a physics-informed approach to identifying frequency-tracking failures in accelerometer-based sleep HR estimation.

### 🤖 AI 总结

**一句话总结**：Large longitudinal cohorts often contain wrist accelerometry without optical heart-rate sensing, motivating recovery of cardiac information from motion signals already collected during sleep. We prese...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Deep, Learning, Sleep, Heart, Rate, Estimation, Accelerometers, Toward

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06823v1) | [下载PDF](https://arxiv.org/pdf/2610.06823v1.pdf)

---

## [20. Private online learning and prediction for Littlestone classes](https://arxiv.org/abs/2610.06822v1)

**作者**：Amartya Sanyal  
**分类**：cs.LG, cs.CR, stat.ML  
**发布时间**：2026-10-05

### 📄 论文摘要

We study mistake bounds for differentially private online learning and online prediction under oblivious realisable adversaries. Online learning requires the learner to release a hypothesis at each time step whereas in online prediction, the learner only needs to make predictions without releasing a hypothesis. Using a novel lower bound for private online learning and an upper bound for private prediction, we show that the sample complexity of these two problems are separated by a factor that grows with the time horizon for every class of finite Littlestone dimension $d$. First, we prove that every $\br{ε,δ}$-private online learner has a deterministic realisable stream of length $T$ on which the mistake bound is at least $\bE\bs{M_T}=\Om{\frac dε\log\br{ T}^{2/3}}$. In particular, this is the first non-trivial lower in the range $1/T<δ<1/\log T)$ left open in earlier works[SR22,DSS24,LWY24]. Second, we prove that for every class of of Littlestone dimension $d$, there exists an $(ε,δ)$-jointly private predictor with at most $2^{2^{cd^2}}ε^{-2}\log^2\br{2/\br{εδ}}$ expected mistakes, independently of $T$, for some absolute constant $c>0$. Thus, for every fixed class of finite Littlestone dimension when $δ=Θ\br{1/\log T}$, private learning requires $\Om{\br{\log T}^{2/3}}$ expected mistakes, whereas private prediction admits $\bigO{\br{\log\log T}^2}$.

### 🤖 AI 总结

**一句话总结**：We study mistake bounds for differentially private online learning and online prediction under oblivious realisable adversaries. Online learning requires the learner to release a hypothesis at each ti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Private, online, learning, prediction, Littlestone, classes, study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06822v1) | [下载PDF](https://arxiv.org/pdf/2610.06822v1.pdf)

---

## [21. Block Disentanglement in CRL: Bridging Identifiability and Visual State Estimation](https://arxiv.org/abs/2610.06809v1)

**作者**：Emre Acartürk, Pranamya Kulkarni, Puranjay Datta 等 6 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-10-05

### 📄 论文摘要

Causal representation learning (CRL) is the process of recovering causally-related latent variables from high-dimensional observations. As a label-free inference method, CRL is particularly attractive for applications where data labels are unavailable or impractical to obtain. While there has been significant progress in understanding the identifiability guarantees of CRL, such guarantees often hold under highly stylized assumptions, which temper the direct application to real-world problems. This paper has a two-fold objective for interventional CRL. First, it establishes identifiability guarantees for substantially weaker interventional assumptions, resulting in block disentanglement of the causal variables, where the block structure depends on the realistically available intervention mechanisms. Secondly, the block disentanglement framework is used for embodied visual state estimation, in which the objective is to recover the latent physical variables of a robotic system directly from visual data (images and videos) without labeled data. These two components are critically complementary. The block disentanglement theory delineates identifiability guarantees under weakened assumptions, and the application demonstrates that the resulting objective remains effective in a controlled embodied setting despite further assumption violations, providing a theory-to-practice bridge needed to translate the promise of label-free CRL into practical problems.

### 🤖 AI 总结

**一句话总结**：Causal representation learning (CRL) is the process of recovering causally-related latent variables from high-dimensional observations. As a label-free inference method, CRL is particularly attractive...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Block, Disentanglement, CRL, Bridging, Identifiability, Visual, State, Estimation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06809v1) | [下载PDF](https://arxiv.org/pdf/2610.06809v1.pdf)

---

## [22. H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning](https://arxiv.org/abs/2610.06805v1)

**作者**：Wancong Zhang, Basile Terver, Michael Rabbat 等 5 位作者  
**分类**：cs.LG, cs.RO  
**发布时间**：2026-10-05

### 📄 论文摘要

Long-horizon planning with latent world models requires reasoning across timescales and levels of abstraction. Existing task-agnostic JEPA world models predict and plan at a single timescale or with multiple horizons in one shared latent space. We introduce H-JEPA, an end-to-end recipe for training a hierarchy of action-conditioned JEPAs in which each level predicts farther ahead in its own learned latent space. Planning proceeds top-down: the top level optimizes progress toward the goal, and each level's predictions become subgoals for the planner below it. When factors in the data evolve at separated timescales, higher levels discard fast, unpredictable detail and retain slower task-relevant state. Across four simulated navigation and manipulation environments, hierarchical planning improves over a flat JEPA; on Visual AntMaze, a three-level hierarchy raises success from 18% to 73% using less planner compute. Ablations attribute these gains to both temporal decomposition and higher-level goal representations. With inverse-dynamics supervision, the approach extends to diverse real-robot videos from DROID, where hierarchy improves offline planning fidelity at lower planner compute.

### 🤖 AI 总结

**一句话总结**：Long-horizon planning with latent world models requires reasoning across timescales and levels of abstraction. Existing task-agnostic JEPA world models predict and plan at a single timescale or with m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, H-JEPA, End-to-End, Learning, Hierarchical, World, Models, Visual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06805v1) | [下载PDF](https://arxiv.org/pdf/2610.06805v1.pdf)

---

## [23. Sharpen Without Search: On-Policy Distillation of Sequence-Level Power Distribution](https://arxiv.org/abs/2610.06804v1)

**作者**：Erfan Baghaei Potraghloo, Seyedarmin Azizi, Arya Fayyazi 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-05

### 📄 论文摘要

A language model can give a correct answer more probability than any single incorrect answer and still usually sample an incorrect one, because the incorrect answers together hold more probability. The power distribution raises each complete answer's probability to a power above one and renormalizes, shifting probability toward answers the model finds most likely (sharpening). Sampling from it improves reasoning without changing parameters, but needs many scored candidates per query. We show that a model can instead be trained to produce such answers in one generation. On-policy power distillation (OPPD) runs a sequential Monte Carlo sampler in which the model being trained generates candidates and a frozen teacher's power distribution weights them; the same probabilities weight each answer in a maximum-likelihood update. Training raises single-generation accuracy by up to 23.0 points on MATH500 and 27.3 on GSM8K over the untrained model at the same temperature, and one generation scores 2.4 and 3.5 points above published power sampling with 64 candidates, recovering 94 percent of the gain that 16 candidates give the untrained model. For context, against GRPO trained with verified rewards from the same checkpoint and budget, OPPD scores 3.8, 4.0 and 5.4 points higher on MATH500, GSM8K and AIME using no reference answers; the two are complementary, and OPPD applied after GRPO adds up to 9.3 points. Trained only on mathematics, OPPD raises HumanEval accuracy by up to 5.3 points. One loss coefficient moves the sharpening exponent the model absorbs between 1.19 and 2.02, against 1.14 for ordinary on-policy distillation, and it rises mostly on the model's own answers. Gains hold across model families and sizes, including a model already trained with verified rewards, where lowering the temperature gives nothing and OPPD adds 4.4 points on MATH500. Code: https://github.com/ArminAzizi98/OPPD.

### 🤖 AI 总结

**一句话总结**：A language model can give a correct answer more probability than any single incorrect answer and still usually sample an incorrect one, because the incorrect answers together hold more probability. Th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Sharpen, Without, Search, On-Policy, Distillation, Sequence-Level, Power

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06804v1) | [下载PDF](https://arxiv.org/pdf/2610.06804v1.pdf)

---

## [24. Round-Trip KNN Clustering: multiscale hierarchical cluster detection on directed nearest-neighbour graphs](https://arxiv.org/abs/2610.06795v1)

**作者**：Eraldo Pereira Marinho, Caetano Mazzoni Ranieri, Fabricio Aparecido Breve  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-10-05

### 📄 论文摘要

We introduce Round-Trip KNN Clustering (RTKNNC), a graph-based method for finding cluster structure at several neighbourhood scales without requiring the number of clusters in advance. Unlike approaches that first make a $k$-nearest-neighbour (KNN) graph undirected, RTKNNC keeps both directions of the neighbour relation: which points a given point selects and which points select it. Incoming selections are treated as weighted votes that help decide which local connections remain visible during a recursive forward-and-reverse traversal. Repeating the procedure for increasing $K$ reveals how groups persist or merge as the neighbourhood scale grows; for the reference inverse-square model before structural refinement, clusters can merge but do not split. Because graph connectivity can occasionally join distinct groups through a sparse bridge or a small region of overlap, we add an optional label-free refinement. It first tests whether an already formed component is better described by two or three Gaussian subpopulations, and accepts a subdivision only when the proposed groups are large enough and consistent with the visible KNN graph. Across eight synthetic datasets and $K=2,\ldots,16$, independent C and Python implementations produced identical partitions in all 120 reference runs. Refinement increased adjusted Rand index from $0.7817$ to $0.9627$ on a variable-density benchmark and from $0.8083$ to $0.9853$ on a sparse-bridge benchmark. Comparisons with seven external clustering methods show competitive performance while preserving a label-free cluster-construction process.

### 🤖 AI 总结

**一句话总结**：We introduce Round-Trip KNN Clustering (RTKNNC), a graph-based method for finding cluster structure at several neighbourhood scales without requiring the number of clusters in advance. Unlike approach...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Round-Trip, KNN, Clustering, multiscale, hierarchical, cluster, detection, directed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06795v1) | [下载PDF](https://arxiv.org/pdf/2610.06795v1.pdf)

---

## [25. MatrixFormer: A Foundation Model for Matrix Completion](https://arxiv.org/abs/2610.06751v1)

**作者**：Dwaipayan Saha, Jacob Feitelberg, Kyuseong Choi 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-05

### 📄 论文摘要

Matrix completion underlies problems from tabular imputation to causal inference, yet existing tabular foundation models treat it as entry-by-entry prediction, repeating context for every target and discarding the matrix's two-dimensional structure. We introduce MatrixFormer, a pre-trained matrix-native transformer that predicts a full distribution for every missing entry in a single forward pass. MatrixFormer is trained entirely on synthetic low-rank and latent-factor matrices under diverse missingness patterns. Applied zero-shot and with the same model weights, MatrixFormer achieves competitive performance on causal inference panel-data tasks, language-model benchmark-score completion, tabular imputation, and recommendation systems matrix completion. These results position MatrixFormer as a general-purpose foundation model for matrix completion.

### 🤖 AI 总结

**一句话总结**：Matrix completion underlies problems from tabular imputation to causal inference, yet existing tabular foundation models treat it as entry-by-entry prediction, repeating context for every target and d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MatrixFormer, Foundation, Model, Matrix, Completion, underlies, problems, tabular

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06751v1) | [下载PDF](https://arxiv.org/pdf/2610.06751v1.pdf)

---

## [26. Hyperbolic Graph Representation Learning: Embed in One Metric, Optimize with Another](https://arxiv.org/abs/2610.06745v1)

**作者**：Federico Larroca, Paola Bermolen, Marcelo Fiori 等 4 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-10-05

### 📄 论文摘要

Hierarchical graphs embed in hyperbolic space with lower distortion than in Euclidean space owing to its negative curvature. However, their gradient-based learning is hampered at large radii, where the Poincaré ball and the Lorentz hyperboloid models fail numerically. Polar coordinates avoid this problem, but the hyperbolic metric scales the angular step by the hyperbolic sine of the radius, freezing angular motion. We observe that this factor is a choice, silently fixed by existing implementations: the Euclidean tangent parametrization, for instance, uses the radius itself. We show that other choices are not only possible but preferable. They are endpoints of a one-parameter family of optimization preconditioners with curvatures from $-1$ to $0$, while the embedding remains at curvature $-1$. We show that since the Euclidean preconditioner rearranges a layout but refines it poorly, while an intermediate one refines far better once a layout is in place, combining them in two stages reduces the loss on real-world trees by 46-74% over the best single curvature.

### 🤖 AI 总结

**一句话总结**：Hierarchical graphs embed in hyperbolic space with lower distortion than in Euclidean space owing to its negative curvature. However, their gradient-based learning is hampered at large radii, where th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hyperbolic, Graph, Representation, Learning, Embed, One, Metric, Optimize

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06745v1) | [下载PDF](https://arxiv.org/pdf/2610.06745v1.pdf)

---

## [27. Decoupling Time and Space: A Temporally Conditioned Refinement for EEG Source Imaging](https://arxiv.org/abs/2610.06726v1)

**作者**：Marco Morik, Jesse Palarus, Carmen Vidaurre 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-05

### 📄 论文摘要

Electroencephalography (EEG) offers millisecond temporal resolution, but inferring underlying neural sources is a severely ill-posed spatial inverse problem. While deep learning has advanced spatial reconstruction, current architectures face a critical dilemma: frame-by-frame models discard vital temporal context, whereas full 4D spatiotemporal networks introduce an architectural trade-off between reconstruction accuracy and inference cost. We propose a novel two-stream framework that explicitly decouples global temporal representation learning from per-time-point spatial refinement. A Transformer-based Temporal Condition Encoder processes the entire EEG sequence via factorized spatiotemporal attention, retaining sensor-resolved features. A fixed inverse then maps these features into source-indexed conditioning for a per-timestep Source-Space Transformer or volumetric convolutional refiner. Extensive evaluations on realistic synthetic data demonstrate that this temporal prior dramatically improves spatial localization, outperforming classical and spatiotemporal baselines, particularly in high-noise and multi-source regimes. Training across diverse leadfields and explicit operator mismatches improves transfer to unseen head geometries and brings template-based reconstruction closer to subject-specific inversion. Furthermore, we apply the model trained only on synthetic EEG data to real-world EEG. A logistic regressor fit on source power differences in eyes-open, eyes-closed conditions successfully decodes age groups.

### 🤖 AI 总结

**一句话总结**：Electroencephalography (EEG) offers millisecond temporal resolution, but inferring underlying neural sources is a severely ill-posed spatial inverse problem. While deep learning has advanced spatial r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Decoupling, Time, Space, Temporally, Conditioned, Refinement, EEG, Imaging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06726v1) | [下载PDF](https://arxiv.org/pdf/2610.06726v1.pdf)

---

## [28. BRANCH-MoE: Balance-Aware Tree Routing for Large Embedding Models](https://arxiv.org/abs/2610.06725v1)

**作者**：Gang Fu, Adel Javanmard, MohammadHossein Bateni 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-05

### 📄 论文摘要

Mixture-of-experts (MoE) layers increase model capacity without a proportional increase in per-example computation. However, conventional flat routers can yield imbalanced expert utilization and treat experts as an unstructured collection, whose indices carry no topological meaning. We introduce {\bf BRANCH-MoE}, a routing architecture that places \(E\) experts at the leaves of a binary decision tree of depth \(\log_2 E\). At each internal node the branching probability is centered on the arrival-weighted mean score of the traffic reaching that node. This mean is estimated using an exponential moving average, which promotes utilization of both child subtrees without an auxiliary load-balancing loss. We show that this moving-average estimate admits an explicit noise-lag trade-off. We prove that for linear node maps and log-concave arrival distributions, this mechanism prevents routing-mass collapse. We further establish that, under a frozen router, an expert's execution frequency controls its stochastic-gradient convergence rate, and that confident decisions near the root bound cross-device communication when experts are assigned to devices by tree prefix. We evaluate BRANCH-MoE against Switch softmax, DeepSeek-V3 dynamic-bias, Skywork logit-normalized, and deterministic hash routing on Criteo click-through-rate prediction, Forest Covertype, HIGGS, and YearPredictionMSD, using \(E=16\), top-\(4\) routing, and five random seeds. Our results show that hierarchical routing can preserve task quality and balanced utilization while inducing a topology that supports localized expert co-activation and reduced communication.

### 🤖 AI 总结

**一句话总结**：Mixture-of-experts (MoE) layers increase model capacity without a proportional increase in per-example computation. However, conventional flat routers can yield imbalanced expert utilization and treat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BRANCH-MoE, Balance-Aware, Tree, Routing, Large, Embedding, Models, Mixture-of-experts

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06725v1) | [下载PDF](https://arxiv.org/pdf/2610.06725v1.pdf)

---

## [29. To Learn is to Wander: Learning Across Graphs and Tasks with Random Walks](https://arxiv.org/abs/2610.06694v1)

**作者**：Louis Tichelman, Xingyue Huang, Jinwoo Kim 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-05

### 📄 论文摘要

Graph foundation models aim to transfer across graphs, feature spaces, relational schemas, and prediction tasks, yet existing approaches typically generalize only within particular graph modalities or tasks. We propose Wander, a graph foundation model designed to operate across these settings within a single pretrained checkpoint. Following the prior-predictive perspective, we formulate graph learning as completion of a partially observed graph. We realize this task-general view through a common interface based on random walks, allowing the same model to operate across homogeneous and multi-relational graphs with varying features, labels, and relational schemas. Wander can increase its structural context at inference time without changing its learned parameters and, under suitable assumptions, universally approximates the corresponding Bayes-optimal predictor on bounded connected graphs. Empirically, a single pretrained checkpoint achieves state-of-the-art or highly competitive results across node classification, homogeneous link prediction, and knowledge-graph link prediction. Moreover, joint pretraining across graph modalities and tasks preserves performance in specialized settings while enabling positive transfer and the composition of separately learned capabilities at inference time.

### 🤖 AI 总结

**一句话总结**：Graph foundation models aim to transfer across graphs, feature spaces, relational schemas, and prediction tasks, yet existing approaches typically generalize only within particular graph modalities or...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learn, Wander, Learning, Across, Graphs, Tasks, Random, Walks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06694v1) | [下载PDF](https://arxiv.org/pdf/2610.06694v1.pdf)

---

## [30. Adapting prior-data fitted networks for tabular anomaly detection](https://arxiv.org/abs/2610.06693v1)

**作者**：Maximilian Bershtman, Niv Cohen  
**分类**：cs.LG  
**发布时间**：2026-10-05

### 📄 论文摘要

While deep features have transformed anomaly detection in images and video, their impact on tabular data has been less substantial, partly due to the limited availability of strong deep representations. Recently, prior-data fitted networks (PFNs) have emerged as a promising source of such representations for tabular data. In this work, we investigate how PFN representations can be adapted and leveraged for anomaly detection. The question is harder than it looks. No anomalies are available before deploy- ment, so model parameters cannot be tuned with supervision, and the reference set that defines normal behavior may itself contain the very anomalies it is supposed to reveal. We begin our study using frozen TabPFN features. Scoring each sam- ple by its distance to its nearest neighbors in feature space already gives strong results. We identify which layers to use and a feature-extraction procedure suited to the task. Next, to further improve performance, we use the reference set to fine- tune the model, so that the resulting features better separate normal samples from anomalies. On the ADBench benchmark, our fine-tuning free approach (ZEN) reaches a higher mean AUROC than every baseline, and our fine-tuned method (FOCUS) improves on it further. Our approach also generalizes across PFN models.

### 🤖 AI 总结

**一句话总结**：While deep features have transformed anomaly detection in images and video, their impact on tabular data has been less substantial, partly due to the limited availability of strong deep representation...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Adapting, prior-data, fitted, networks, tabular, anomaly, detection, While

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.06693v1) | [下载PDF](https://arxiv.org/pdf/2610.06693v1.pdf)

---

