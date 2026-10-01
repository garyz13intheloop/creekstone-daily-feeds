# arXiv AI 论文日报 | 2026-10-01

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (8 篇)
- [cs.CV](#csCV) (12 篇)
- [cs.CL](#csCL) (4 篇)
- [cs.AI](#csAI) (6 篇)

---

## cs.AI

## [1. Turbo Harness: Instance-Adaptive Harness Optimization](https://arxiv.org/abs/2609.40330v1)

**作者**：Tunyu Zhang, Hao Wang, Kai Xu 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-30

### 📄 论文摘要

Automating the search for effective harnesses is an important step toward enabling agents to recursively self-improve. Existing harness optimizations typically produce a single global harness that is applied uniformly across task instances. However, a harness that works well on average may not be optimal for every instance. We introduce Turbo Harness, a framework that can adapt a globally optimized harness to each instance by reusing information generated during the original optimization process. Specifically, Turbo Harness recycles artifacts produced during a completed global harness optimization run, and summarizes them into a structured playbook. We train a harness editor to leverage this prior optimization experience to generate instance-specific patches to the global harness. At inference time, the editor uses the instance and the playbook to construct a tailored harness in which the execution model operates. Through numerical experiments, we show that Turbo Harness consistently outperforms existing harness optimization baselines across seven benchmarks spanning interactive agent tasks, software engineering, and long-horizon terminal tasks.

### 🤖 AI 总结

**一句话总结**：Automating the search for effective harnesses is an important step toward enabling agents to recursively self-improve. Existing harness optimizations typically produce a single global harness that is ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Turbo, Harness, Instance-Adaptive, Optimization, Automating, search, effective, harnesses

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40330v1) | [下载PDF](https://arxiv.org/pdf/2609.40330v1.pdf)

---

## [2. WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents](https://arxiv.org/abs/2609.40325v1)

**作者**：Ziyan Jiang, Jingbo Yang, Jiabao Ji 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-30

### 📄 论文摘要

As interactive 3D worlds are increasingly used to study intelligent behavior, it becomes important to develop efficient pipelines for identifying anomalies in these simulated environments, such as floating objects, traversable walls, or objects inconsistent with the surrounding scene. Multimodal AI systems, including vision-language models (VLMs) and vision-language-action models (VLAs), have shown potential for automating this task. However, 3D world auditing is complex, requiring the close coupling of two distinct capabilities: action, to navigate the 3D world and search for anomalies systematically and efficiently; and visual reasoning, to understand the environment and identify anomalies from multimodal observations. It remains largely unexplored whether multimodal agents can effectively couple these two capabilities, using visual reasoning to identify potential anomalies while taking actions to validate them. In this paper, we introduce WorldAuditBench, a benchmark for 3D world auditing comprising 213 anomaly tasks across 13 environments built with Unreal Engine 5 and Three.js, spanning five anomaly families. We evaluate five frontier models under a fixed exploration budget using two auditing paradigms: VLA-based exploration followed by VLM-based anomaly identification, and an end-to-end VLM agent in which visual reasoning directly guides action selection. Across the evaluated models and two paradigms, success rates range from 6.6% to 42.3%, substantially below human performance (83.4%). Through the task of world auditing, WorldAuditBench provides a testbed for studying how multimodal agents couple action and visual reasoning in interactive 3D environments, while highlighting current limitations in their ability to gather and interpret evidence during exploration.

### 🤖 AI 总结

**一句话总结**：As interactive 3D worlds are increasingly used to study intelligent behavior, it becomes important to develop efficient pipelines for identifying anomalies in these simulated environments, such as flo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Agent, As, WorldAuditBench, Interactive, World, Auditing, Multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40325v1) | [下载PDF](https://arxiv.org/pdf/2609.40325v1.pdf)

---

## [3. Cogentic: Multi-Agent Orchestration for Automated Proof Discovery](https://arxiv.org/abs/2609.40324v1)

**作者**：Yang Cai, Vineet Gupta, Yanchen Jiang 等 7 位作者  
**分类**：cs.AI, cs.GT  
**发布时间**：2026-09-30

### 📄 论文摘要

We present Cogentic, a multi-agent harness for automated proof discovery on open research problems. While frontier language models can generate strong mathematical ideas in a single shot, single-shot generation is often insufficient for open problems that require exploring multiple competing conjectures, overcoming subtle technical obstructions, and retaining intermediate progress over a long horizon. Cogentic addresses these challenges through an iterative prove--verify loop in which an orchestrator allocates a population of independent provers across distinct proof directions, subjects their output to adversarial verification by several specialized components, and promotes confirmed intermediate results into a persistent verified ledger that later rounds build on. The harness is designed to be able to solve research-level math and theoretical computer science problems. Using Gemini as the base model, Cogentic produced novel results on five open problems across online learning, auction theory, and mechanism design. Each result was independently verified by domain experts and is developed in full in companion papers. We list these results, and new ones as they are verified, at https://sites.google.com/view/cogentic .

### 🤖 AI 总结

**一句话总结**：We present Cogentic, a multi-agent harness for automated proof discovery on open research problems. While frontier language models can generate strong mathematical ideas in a single shot, single-shot ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, We, Cogentic, Orchestration, Automated, Proof, Discovery, present

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40324v1) | [下载PDF](https://arxiv.org/pdf/2609.40324v1.pdf)

---

## [4. How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?](https://arxiv.org/abs/2609.40303v1)

**作者**：Kirill Brilliantov, Alejandro Hernández-Cano, Emmanuel Abbé  
**分类**：cs.AI  
**发布时间**：2026-09-30

### 📄 论文摘要

Recent autonomous machine learning engineering (MLE) agents have made significant progress on public leaderboards. Often motivated by progress stagnation over long-horizon cycles and limited Large Language Model (LLM) primitives, modern MLE agents are deployed on top of increasingly elaborate machinery: multi-agent orchestrators, dedicated retrieval subagents, and more. While such harnesses expand, the use of more primitive but improved coding agents - where LLMs have direct access to the execution environment through read, write, and bash primitives - has received little attention in the field. In this paper we find that, under an equal time budget and the same frontier LLM backbone, open-source state-of-the-art harnesses provide no advantages over a single session of a minimal-harness coding agent baseline, pointing to the backbone as the primary driver for performance. Via a series of large-scale systematic ablation studies, we argue that the machinery layers become redundant in the coding agent setting. We conclude that the effort spent elaborating hand-crafted harnesses around strong models yields poor returns for current MLE benchmarks.

### 🤖 AI 总结

**一句话总结**：Recent autonomous machine learning engineering (MLE) agents have made significant progress on public leaderboards. Often motivated by progress stagnation over long-horizon cycles and limited Large Lan...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, How, Much, Harness, Does, Strong, Need

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40303v1) | [下载PDF](https://arxiv.org/pdf/2609.40303v1.pdf)

---

## [5. PivotOPD: Learning to Recover from Pivotal Mistakes in Multi-Turn Agents](https://arxiv.org/abs/2609.40285v1)

**作者**：Yinghui He, Yapei Chang, Khushi Bhardwaj 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-30

### 📄 论文摘要

On-policy distillation (OPD) is a promising approach for training language agents, providing dense teacher supervision on student-generated trajectories. However, in multi-turn interaction, an incorrect action changes the states the student encounters later, so errors compound across turns. In preliminary experiments across three Qwen3 models (8B to 235B), we find that more than half of the failed rollouts contain a pivotal mistake, an action that moves the agent farther from completing the task, and this mistake typically occurs early. These pivotal mistakes often remain recoverable: guiding the model for only a few turns after the pivotal turn can restore task success. We therefore propose PivotOPD, an on-policy distillation framework that jointly trains the student to prevent pivotal mistakes and to recover from the states they create. At each pivotal mistake, a teacher model provides a gold action and then names a recovery action at each of the next few turns. Preventive distillation uses the gold action with reverse KL to steer the student away from the pivotal mistake, while recovery distillation uses the recovery actions with forward KL to transfer recovery behaviors that the student rarely samples. Against 13 baselines on ALFWorld, WebShop, and Search-based QA, PivotOPD achieves the strongest average performance for both Qwen3-1.7B and Qwen3-8B students, improving over the strongest baseline on ALFWorld by +5.5% with the 1.7B student. The gains also transfer to another model family on the software engineering domain, where PivotOPD raises the resolve rate of a Nemotron-3.5 student on SWE-Bench Verified by +3.2%. Project page: https://research.nvidia.com/labs/lpr/pivotopd/

### 🤖 AI 总结

**一句话总结**：On-policy distillation (OPD) is a promising approach for training language agents, providing dense teacher supervision on student-generated trajectories. However, in multi-turn interaction, an incorre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, PivotOPD, Learning, Recover, Pivotal, Mistakes, Multi-Turn, On-policy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40285v1) | [下载PDF](https://arxiv.org/pdf/2609.40285v1.pdf)

---

## [6. Belief-Aware Multi-Agent Path Finding under Map Uncertainty](https://arxiv.org/abs/2609.40269v1)

**作者**：Viraj Parimi, Shao-Hung Chan, Han Zhang 等 5 位作者  
**分类**：cs.AI, cs.MA, cs.RO  
**发布时间**：2026-09-30

### 📄 论文摘要

Multi-Agent Path Finding (MAPF) aims to find collision-free paths for multiple agents in a shared environment. Classical MAPF assumes that all static obstacles are known in advance, but real-world environments can change unexpectedly due to fallen objects, spills, or other local disturbances. When such changes are spatially correlated, an observation can inform traversability estimates beyond the observed location. Prior approaches address uncertainty in traversability through contingent plans or replanning based on direct observations, but do not leverage this spatial dependence to infer the traversability of nearby unobserved locations. As a result, they cannot use one observation to anticipate nearby unobserved obstacles that may cause costly rerouting later. We focus on Belief-Aware MAPF, where map discrepancies are fixed during execution but initially unknown, and observations can be informative beyond the observed location. We propose Multi-Agent Gaussian belief Inference for Coordination (MAGIC), a framework that updates a shared belief about traversability online based on agents' observations. MAGIC uses a Gaussian Markov Random Field and Gaussian Belief Propagation to approximately infer traversability and construct detour-aware costs for standard MAPF planners. Our experiments on MAPF benchmarks show that MAGIC reduces the executed sum of costs compared to existing approaches on 96.3% of instances, across several planner families and teams of up to 800 agents, demonstrating its applicability to large-scale MAPF problems.

### 🤖 AI 总结

**一句话总结**：Multi-Agent Path Finding (MAPF) aims to find collision-free paths for multiple agents in a shared environment. Classical MAPF assumes that all static obstacles are known in advance, but real-world env...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, Belief-Aware, Path, Finding, under, Map, Uncertainty, MAPF

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40269v1) | [下载PDF](https://arxiv.org/pdf/2609.40269v1.pdf)

---

## cs.CL

## [7. EvoDuet: Bilevel Co-Evolution of Web Searching and Task Solving for Scientific Discovery](https://arxiv.org/abs/2609.40340v1)

**作者**：Young-Jun Lee, Jinheon Baek, Soyeong Jeong 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-30

### 📄 论文摘要

Evolutionary search with large language models (LLMs) can stall when progress requires external knowledge the model lacks. Supplying relevant documents helps, but simply adding web search tool can keep returning the same pages as solutions change. We introduce EvoDuet, a bi-level optimization method that co-evolves solutions and search queries with fixed model parameters. At each iteration, a retrieval gate lets the LLM assess its knowledge gap and choose to retrieve new documents, reuse stored ones, or proceed without them. An inner loop refines queries and ranks documents by the solution scores they are predicted to yield; an outer loop generates candidates in parallel from these documents and records the evaluated outcomes for later searches. Across 21 optimization tasks with one candidate per iteration, EvoDuet raises OpenEvolve's normalized discovery gain from 74.1% to 78.0% with GPT-5.6-Luna and from 61.3% to 82.3% with Gemini-3.8-Flash, whereas Qwen3.5-9B does not benefit. Our best runs surpass the previously reported best scores on eight tasks, including Swap Reduction on Q20 and Rosetta, and match them on three more. EvoDuet also improves with other scaffolds (e.g., Top-K, EvoX) on Sums/Diffs and Denoising, demonstrating its applicability across evolutionary search scaffolds.

### 🤖 AI 总结

**一句话总结**：Evolutionary search with large language models (LLMs) can stall when progress requires external knowledge the model lacks. Supplying relevant documents helps, but simply adding web search tool can kee...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, EvoDuet, Bilevel, Co-Evolution, Web, Searching, Task, Solving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40340v1) | [下载PDF](https://arxiv.org/pdf/2609.40340v1.pdf)

---

## [8. Linguistic Loopholes in LLM Unlearning: From a 174-Language Benchmark to Coverage-Aware Unlearning](https://arxiv.org/abs/2609.40286v1)

**作者**：Tyler Skow, Shravan Chaudhari, Rama Chellappa 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-30

### 📄 论文摘要

Unlearning a fact in one language does not guarantee its removal in others as changing the query or even the requested answer language can reopen seemingly forgotten knowledge -- a cross-lingual loophole. The most straightforward solution to this challenge -- unlearning in all languages -- is neither scalable nor desirable as it amplifies damage to unrelated model capabilities. We introduce the task of language budgeted multilingual unlearning where the goal is to select a subset of languages that maximizes cross-lingual erasure. To study this task we introduce the Cross-Lingual Unlearning Tensor, an unlearning benchmark that spans 174 language--script pairs and 25 atomic paraphrase types to examine when forgetting generalizes across linguistic expressions of the same knowledge. We further propose COVER, which selects source languages to maximize predicted COVERage of languages receiving no forget supervision, enabling unlearning on a language budget. Surprisingly, we find naively selecting strong individual sources does not reliably compose into strong source sets motivating our development of COVER. At deployment COVER only requires benign calibration data and access to the frozen model. Across three model families and two disjoint forget sets, COVER reduces mean held-out residual access by 7.8--27.3% relative to uniform source selection. We find these gains extend beyond synthetic benchmarks to real news documents in low-resource language settings using human translated data from the Low Resource Languages for Emergent Incidents (LORELEI) corpus.

### 🤖 AI 总结

**一句话总结**：Unlearning a fact in one language does not guarantee its removal in others as changing the query or even the requested answer language can reopen seemingly forgotten knowledge -- a cross-lingual looph...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Linguistic, Loopholes, Unlearning, 174-Language, Benchmark, Coverage-Aware, fact

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40286v1) | [下载PDF](https://arxiv.org/pdf/2609.40286v1.pdf)

---

## [9. Comparison of techniques for fine-tuning open-weight models for entity extraction from radiology reports](https://arxiv.org/abs/2609.40236v1)

**作者**：Aawez Mansuri, Kush Mehta, Mohammadreza Chavoshi 等 13 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-09-30

### 📄 论文摘要

Converting free-text radiology reports into structured labels supports cohort building, quality assurance, and monitoring of clinical imaging models, but the strongest label extractors are hosted proprietary models whose use raises privacy, cost, and reproducibility concerns. We asked whether a fine-tuned open-weight model (Gemma-3-12B) can match GPT-4o at multi-label intracranial hemorrhage (ICH) acuity extraction from non-contrast head-CT reports, and which ingredients matter. Using a 2x2 design, we crossed two adaptation strategies (a discriminative classification head, CH; generative instruction fine-tuning, IFT) with two training-data sources (distillation of real GPT-4o-labeled reports; synthetic reports generated by GPT-4o from real exemplars), across five training sizes, benchmarked on 100 expert-adjudicated reports against GPT-4o and the un-tuned open-weight base. The distilled instruction-tuned model (DIFT) matched GPT-4o (macro-F1 0.845 vs 0.850; p = 1.000) and exceeded the base model by 0.178. The decisive factor was the training-data source, not the fine-tuning method: both synthetic-data models failed to exceed the un-tuned open-weight base at any training size and underperformed the distilled models across all acuity classes. Fine-tuning and inference fit within the memory envelope of a single 24 GB consumer GPU. For narrow, high-value clinical label-extraction tasks, distilling real reports, rather than generating synthetic ones, is what closes the gap to a hosted model, enabling a private, low-cost, version-stable on-premises alternative.

### 🤖 AI 总结

**一句话总结**：Converting free-text radiology reports into structured labels supports cohort building, quality assurance, and monitoring of clinical imaging models, but the strongest label extractors are hosted prop...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Comparison, techniques, fine-tuning, open-weight, models, entity, extraction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40236v1) | [下载PDF](https://arxiv.org/pdf/2609.40236v1.pdf)

---

## [10. SCB: SpeechConversationBench for Evaluating Multi-Turn Reasoning in Speech-to-Speech Models](https://arxiv.org/abs/2609.40198v1)

**作者**：Kanpat Vesessook, Saksorn Ruangtanusak  
**分类**：cs.CL, cs.AI, cs.SD  
**发布时间**：2026-09-30

### 📄 论文摘要

Speech-to-speech systems must solve tasks whose requirements emerge across conversational turns. We introduce SpeechConversationBench (SCB), a focused evaluation of spoken mathematical reasoning using 103 sharded GSM8K problems. The framework compares the original problem delivered in one turn (full), its concatenated information shards delivered together (concat), and incremental spoken disclosure across turns (sharded). We report final-answer accuracy for four commercial speech systems and LEGO, a proprietary speech pipeline developed internally by the SCBX Innovation Lab team with explicit conversational context management. Relative to concat, sharded accuracy decreases by 5.0-25.3 percentage points across the four commercial systems. LEGO achieves 77.5 percent accuracy in all three conditions, compared with 76.6 percent sharded accuracy for GPT-4o Realtime. The two single-turn baselines distinguish sensitivity to problem reformulation from the additional challenges introduced by incremental spoken interaction.

### 🤖 AI 总结

**一句话总结**：Speech-to-speech systems must solve tasks whose requirements emerge across conversational turns. We introduce SpeechConversationBench (SCB), a focused evaluation of spoken mathematical reasoning using...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SCB, SpeechConversationBench, Evaluating, Multi-Turn, Reasoning, Speech-to-Speech, Models, systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40198v1) | [下载PDF](https://arxiv.org/pdf/2609.40198v1.pdf)

---

## cs.CV

## [11. Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model](https://arxiv.org/abs/2609.40358v1)

**作者**：Liming Lu, Xianzheng Ma, Wenkun He 等 17 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-30

### 📄 论文摘要

Video world models are expected to predict how the physical world evolves, yet they often produce visually plausible videos that violate basic physical principles. Existing approaches commonly assume that natural language is insufficient to represent the physical knowledge required for reliable generation, and therefore introduce additional visual, latent, numerical, or planning-based signals. We revisit this assumption and introduce Physis-Lang, a self-evolving framework that treats physical language as a shared and optimizable representation across data curation, model training, and video generation. Physis-Lang represents physical processes through language that describes their relevant entities, causes, interactions, governing principles, temporal evolution, and effects. To improve this representation, we construct PhysCapBench, which decomposes physical processes into atomic assertions and evaluates captions using recall and precision. An agentic loop iteratively analyzes assertion-level errors and refines the instruction used to produce physical captions. Physis-Lang further converts model deficiencies into textual descriptions and uses language-guided retrieval to identify visually diverse videos that cover missing physical processes. Experiments on four widely used physical video benchmarks with Wan and Cosmos backbones demonstrate consistent improvements in physical plausibility. Notably, starting from open-source Cosmos3-Nano backbones, our Physis-Lang-enhanced models surpass the leading proprietary Veo 3.1 model.

### 🤖 AI 总结

**一句话总结**：Video world models are expected to predict how the physical world evolves, yet they often produce visually plausible videos that violate basic physical principles. Existing approaches commonly assume ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Physis-Lang, Self-Evolving, Language, Physical, Representation, Video, World

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40358v1) | [下载PDF](https://arxiv.org/pdf/2609.40358v1.pdf)

---

## [12. ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing](https://arxiv.org/abs/2609.40356v1)

**作者**：Xinghao Chen, Xiangbo Gao, Jiongze Yu 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-09-30

### 📄 论文摘要

Recent video generation is increasingly realistic and controllable, yet video editing remains less developed, particularly for precise local edits that must preserve the original scene dynamics. Video scene text editing replaces text on scene surfaces, such as storefront signs, whiteboards, and product labels, while preserving the surrounding content, motion, and camera dynamics. Although scene text editing is well studied for images, video scene text editing that achieves high visual quality, temporal consistency, and edit locality remains underexplored. Existing resources offer limited paired real-video data, and general video-editing metrics do not directly measure whether the requested text remains correct over time. We introduce ViTeX-Bench, a benchmark suite comprising ViTeX-Dataset and a three-axis evaluation protocol. The dataset contains 387 real-world 720p videos with text-region masks and editing instructions: 230 provide reviewed, pipeline-generated paired edits for training, and 157 form a frozen evaluation split. The protocol evaluates text correctness, visual and temporal quality, and edit locality through 13 metrics, with one primary metric per axis and a Pareto comparison of their trade-offs. OCR calibration, human evaluation, and annotation-sensitivity analyses support the interpretation of these scores. Across eight baselines from four editing families, accurate text, temporal stability, and scene preservation remain difficult to achieve together. We also release ViTeX-Edit-14B, an open-source reference editor fine-tuned on the paired training split with motion-aligned glyph-video conditioning. It achieves CharAcc 0.688, the highest mean among the evaluated video-native editors, and the lowest comparable text-crop Warp among raw editor outputs. ViTeX-Bench provides a reproducible foundation for studying these trade-offs in video scene text editing.

### 🤖 AI 总结

**一句话总结**：Recent video generation is increasingly realistic and controllable, yet video editing remains less developed, particularly for precise local edits that must preserve the original scene dynamics. Video...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ViTeX-Bench, Benchmarking, High-Fidelity, Video, Scene, Text, Editing, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40356v1) | [下载PDF](https://arxiv.org/pdf/2609.40356v1.pdf)

---

## [13. AssemblyWorld: Rethinking 3D Assembly with General-Purpose Agents](https://arxiv.org/abs/2609.40353v1)

**作者**：Jiahao Zhang, Yeying Fan, Moitreya Chatterjee 等 8 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-09-30

### 📄 论文摘要

The task of 3D assembly requires translating an understanding of parts and their relationships into precise spatial arrangements. Can pretrained general-purpose agents assemble objects through visual interaction without additional assembly-specific fine-tuning? To investigate this question, we introduce AssemblyWorld, an interactive 3D environment in which agents inspect rendered views and manipulate supplied rigid parts, guided by images or assembly manuals when available. Agents perceive part geometry through 2D views rather than direct access to mesh vertices or faces, while their resulting assemblies are evaluated geometrically. Building on this environment, we construct AssemblyWorldBench, comprising 100 assembly tasks across 80 objects spanning furniture, industrial assembly, and fracture reassembly. Evaluating eight agent systems reveals substantial differences in their capabilities. The strongest system achieves 80.9% part accuracy but 59.4% complete-assembly success. The evaluated open-source systems lag substantially behind their stronger closed-source peers in both execution reliability and assembly accuracy. Analyses of visual references, interaction trajectories, and failures show how agents revise assemblies while leaving residual positioning errors. AssemblyWorld provides a common setting for both assessing the capabilities of interactive assembly agents and characterizing the gap between approximate structure recovery and precise reconstruction.

### 🤖 AI 总结

**一句话总结**：The task of 3D assembly requires translating an understanding of parts and their relationships into precise spatial arrangements. Can pretrained general-purpose agents assemble objects through visual ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Agent, of, AssemblyWorld, Rethinking, Assembly, General-Purpose, task

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40353v1) | [下载PDF](https://arxiv.org/pdf/2609.40353v1.pdf)

---

## [14. Image Classifiers are Efficient Self-Supervised Video Representation Learners](https://arxiv.org/abs/2609.40347v1)

**作者**：Owais Iqbal, Sudipta Sarkar, Shyam Marjit 等 6 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-09-30

### 📄 论文摘要

We introduce VideoMSN, a Masked Siamese Network framework for efficient self-supervised spatio-temporal representation learning in videos. Instead of relying on heavy 3D architectures or reconstruction-based autoencoders for learning with unlabeled data, we repurpose standard image Vision Transformers by representing videos as super images which are grids composed of frames sampled from videos. From each super image, we construct two views: one with spatial patch masking and the other with temporal frame masking, ensuring no information leakage across frames. A shared Vision Transformer (ViT) encoder aligns their embeddings using a masked Siamese loss, capturing both motion and appearance cues without reconstruction. Our decoder-free formulation leverages an image foundation model towards efficient video representation learning. Starting from pretrained DINO-v3 and DeiT-v3 image encoders, VideoMSN achieves state-of-the-art performance on Kinetics-400, UCF101, and HMDB51 while requiring up to $32\times$ fewer and $160\times$ fewer video pretraining epochs compared to prior video self-supervised learning methods. Our proposed approach also shows strong performance in low-shot classification, confirming the transferability of the learned representations in a label-scarce scenario. Project Page: https://cvir.github.io/projects/videomsn.

### 🤖 AI 总结

**一句话总结**：We introduce VideoMSN, a Masked Siamese Network framework for efficient self-supervised spatio-temporal representation learning in videos. Instead of relying on heavy 3D architectures or reconstructio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Image, Classifiers, Efficient, Self-Supervised, Video, Representation, Learners

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40347v1) | [下载PDF](https://arxiv.org/pdf/2609.40347v1.pdf)

---

## [15. I Have a Stream: Making Self-Supervised Learning Work on Continuous Video](https://arxiv.org/abs/2609.40333v1)

**作者**：Ivan Martinović, Lukas Knobel, Yuki M. Asano  
**分类**：cs.CV  
**发布时间**：2026-09-30

### 📄 论文摘要

Self-supervised learning draws inspiration from infant visual development, yet standard training pipelines bear little resemblance to it: images are independently sampled and globally shuffled across epochs. We study self-supervised learning from continuous video streams, where frames are consumed in temporal order using strict sliding-window batches, without global reshuffling or multi-epoch replay. To this end, we construct WT++, a 95-hour urban walking-tour video dataset for streaming pretraining. Combined with a comprehensive evaluation suite we find that contrastive and distillation-based methods struggle in this setting, while MAE is more robust but still falls short of standard i.i.d. pretraining. We find that high inter-batch similarity, caused by sliding-window consumption across consecutive batches, does not explain this gap. The main challenge is high intra-batch similarity, where frames within each batch are near-duplicates. To mitigate this, we propose StreamMAE, which preserves the core MAE reconstruction objective while adapting the input pipeline with stream-aware regularization and motion-biased crop selection. StreamMAE outperforms streaming baselines, matches i.i.d. MAE trained on the same video data, remains competitive with ImageNet-pretrained MAE, and scales positively as the pretraining stream grows from 12 to 95 hours.

### 🤖 AI 总结

**一句话总结**：Self-supervised learning draws inspiration from infant visual development, yet standard training pipelines bear little resemblance to it: images are independently sampled and globally shuffled across ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Have, Stream, Making, Self-Supervised, Learning, Work, Continuous, Video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40333v1) | [下载PDF](https://arxiv.org/pdf/2609.40333v1.pdf)

---

## [16. MatLoom: Layered Text-to-Material Generation in a Compact Program Space](https://arxiv.org/abs/2609.40322v1)

**作者**：Anson Y. Lam, Shuqing Li, Michael R. Lyu  
**分类**：cs.CV, cs.AI, cs.CL, cs.MM  
**发布时间**：2026-09-30

### 📄 论文摘要

Material generation should produce not only an appearance, but also the rules that construct it. We introduce MatLoom, a compact, layer-oriented language for text-to-material generation with pretrained language models. Each program composes alpha-masked layers whose shared spatial expressions define coverage and physically based rendering (PBR) channels, making dependencies between patterns, color, and relief explicit. A standalone interpreter evaluates the program into material maps, while the source retains named fields and layer parameters for subsequent authoring. Without task-specific fine-tuning, our pipeline uses parser-guided repair and preview-based critique to revise material designs, then searches noise seeds while keeping each candidate's remaining source fixed. On a curated benchmark of 141 prompts evaluated with six backbones, our best-performing configuration achieves higher mean scores than three diffusion baselines on all four flat-layout prompt-alignment metrics. Its initial programs already exceed all three baselines on mean BLIPScore, before critique or seed search. Retained programs have a median length of 21 lines when pooled across backbones. In a blind four-way comparison involving 30 participants and 20 prompts, our renders receive 59.2% of choices, compared with 19.3% for the most-preferred baseline. Compact executable programs thus offer a way to generate prompt-aligned materials while retaining their construction as part of the asset.

### 🤖 AI 总结

**一句话总结**：Material generation should produce not only an appearance, but also the rules that construct it. We introduce MatLoom, a compact, layer-oriented language for text-to-material generation with pretraine...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MatLoom, Layered, Text-to-Material, Generation, Compact, Program, Space, Material

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40322v1) | [下载PDF](https://arxiv.org/pdf/2609.40322v1.pdf)

---

## [17. Atomizer-IO: Beyond Pixels, Patches and Grids](https://arxiv.org/abs/2609.40320v1)

**作者**：Hugo Riffaud de Turckheim, Sylvain Lobry, Nicolas Houdré 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-30

### 📄 论文摘要

Most vision architectures assume that observations lie on a regular grid, an effective abstraction for natural images but a restrictive one for sensing data whose channels, temporal sampling, spatial resolution, and geometry can vary. Generic set-based architectures remove the grid, but also remove useful spatial inductive biases. We introduce Atomizer-IO, an architecture that places observations first and derives structure from their physical relationships. Building on top of an atomic representation of the data, each observation is described by its measurement and acquisition metadata, while local cross-attention maps observations to anchor points that can be arbitrarily placed. We evaluate this design by progressively relaxing the grid assumption, from varying input raster configurations and incomplete channel sets to flexible output density and, ultimately, inputs without a raster grid. Atomizer-IO is competitive with flexible EO-specific architectures on most tasks, while offering post-training control over inference cost and competitive compute--performance trade-offs. The same formulation extends without architectural redesign to unordered 3D point clouds, showing that the atomic interface generalizes beyond regular raster inputs. These results suggest that pixels, patches, and grids do not need to define the interface of a sensing architecture.

### 🤖 AI 总结

**一句话总结**：Most vision architectures assume that observations lie on a regular grid, an effective abstraction for natural images but a restrictive one for sensing data whose channels, temporal sampling, spatial ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Atomizer-IO, Beyond, Pixels, Patches, Grids, Most, vision, architectures

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40320v1) | [下载PDF](https://arxiv.org/pdf/2609.40320v1.pdf)

---

## [18. GLARE: Generating Listening Heads with Appropriate Reactions](https://arxiv.org/abs/2609.40317v1)

**作者**：Zikai Liao, Yumin Suh, Yi Ouyang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-30

### 📄 论文摘要

While talking head generation has advanced rapidly, generating natural listener behavior in dyadic conversations, which know when to react, how to react, and with what type of response, remains underexplored. Existing dyadic datasets lack fine-grained listener reaction annotations, and prevailing evaluation metrics inherited from talking-head and video generation measure visual realism rather than whether a listener reacted appropriately. We address these gaps along three aspects. First, we curate a listening-head-specific dataset built from RealTalk and Seamless Interaction, comprising approximately 147 hours of paired speaker-listener videos with 64,557 event-level reaction annotations across six categories: nodding, head shaking, smiling, laughing, frowning, and surprised. Second, we introduce an audio-driven baseline built on a flow-matching transformer, namely GLARE, with prosody conditioning derived from Qwen2-Audio and a temporal reaction loss that explicitly supervises frame-wise reactions. Third, we propose a reaction-oriented evaluation protocol that jointly measures reaction occurrence (R-F1), temporal alignment (R-tIoU), asymmetric temporal deviation (R-ATD), and reaction-region visual quality (R-FID), giving a more behaviorally grounded assessment than visual-quality-only metrics. Experiment results show consistent gains over prior listening-head methods in both visual fidelity and reaction-level metrics, suggesting that reaction-aware data, modeling, and evaluation are critical for natural listening behavior.

### 🤖 AI 总结

**一句话总结**：While talking head generation has advanced rapidly, generating natural listener behavior in dyadic conversations, which know when to react, how to react, and with what type of response, remains undere...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GLARE, Generating, Listening, Heads, Appropriate, Reactions, While, talking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40317v1) | [下载PDF](https://arxiv.org/pdf/2609.40317v1.pdf)

---

## [19. StreamRig: Exploiting Intra-Rig Geometry for Streaming Multi-Camera Odometry](https://arxiv.org/abs/2609.40244v1)

**作者**：Yufei Wei, Shuhao Ye, Qi Wang 等 7 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-09-30

### 📄 论文摘要

Mobile robots and vehicles carry synchronized multi-camera rigs, yet many streaming 3D foundation models are designed for monocular input, leaving efficient use of rig geometry a challenge. We present StreamRig, a freeze-and-stream framework that builds causal streaming odometry for calibrated rigs on a frozen multi-view 3D foundation model. The frozen front-end jointly perceives the synchronized views using rig calibration. A Rig-Resampler compresses their features, a CausalBridge applies causal attention with a key-value cache, and a lightweight head regresses rig poses. A periodic re-anchoring protocol supports stable pose estimation over long sequences. Only these modules are trained, 74.6M parameters in total, with relative poses as the sole supervision. Our two-stage training strategy combines group relocalization pretraining with causal rig training to transfer the geometric priors of the frozen front-end and the alignment ability of the pretrained modules to streaming odometry. We evaluate on NCLT, TartanGround, KITTI-360, and our self-collected humanoid-robot dataset ZJH, where training uses only simulation and real-world evaluation is zero-shot. Across all four datasets, StreamRig achieves lower translation and rotation drift than the evaluated non-oracle monocular streaming and rig-aware offline models, while maintaining low inference cost. Ablations and controlled camera-count experiments identify the sources of these gains. We further examine how longer training windows affect inference over longer horizons. Code has been released at https://github.com/WeiYuFei0217/StreamRig.

### 🤖 AI 总结

**一句话总结**：Mobile robots and vehicles carry synchronized multi-camera rigs, yet many streaming 3D foundation models are designed for monocular input, leaving efficient use of rig geometry a challenge. We present...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：StreamRig, Exploiting, Intra-Rig, Geometry, Streaming, Multi-Camera, Odometry, Mobile

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40244v1) | [下载PDF](https://arxiv.org/pdf/2609.40244v1.pdf)

---

## [20. EviRover: Reinforcing Agentic Perception Beyond a Glance](https://arxiv.org/abs/2609.40230v1)

**作者**：Kaixuan Fan, Kaituo Feng, Tianshuo Peng 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-09-30

### 📄 论文摘要

Visual perception is conventionally formulated as a one-shot prediction from a single glance at the image, under the assumption that the image content and the model's parametric knowledge suffice to resolve the query. This assumption often fails in real-world scenarios that hinge on fine-grained visual details or require knowledge-intensive and up-to-date information. We term such cases \textit{perception under insufficient evidence} and formulate perception as an agentic process that can obtain information beyond a single glance. To address the absence of data for this setting, we design two dedicated data generation pipelines, yielding EviRover-SFT-5K and EviRover-RL-12K for training. We further construct EviLens, a human-verified benchmark comprising 688 instances across five perception categories. Building on these data, we present EviRover, to our knowledge the first perception agent explicitly trained to resolve perceptual queries through interaction, using supervised fine-tuning followed by agentic reinforcement learning. Experiments show that the 4B EviRover outperforms its backbone by 30 points on average on EviLens, reaching performance comparable to advanced proprietary models. The gains transfer beyond EviLens to WebEyes, conventional perception benchmarks, and general multimodal benchmarks, including a 15-point improvement on BrowseComp-VL. All code, models, and data are released.

### 🤖 AI 总结

**一句话总结**：Visual perception is conventionally formulated as a one-shot prediction from a single glance at the image, under the assumption that the image content and the model's parametric knowledge suffice to r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EviRover, Reinforcing, Agentic, Perception, Beyond, Glance, Visual, conventionally

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40230v1) | [下载PDF](https://arxiv.org/pdf/2609.40230v1.pdf)

---

## [21. LOCI: Spatial Linear Memory for Streaming World Models](https://arxiv.org/abs/2609.40222v1)

**作者**：Ji Xia, Tingting Liao, Xuezhi Liang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-30

### 📄 论文摘要

When a camera revisits a previously observed region, a video world model should reproduce what was there before. This requires both remembering past observations and retrieving the right one for the current viewpoint. Key-value caches preserve visual detail but grow with video length; recurrent memory is compact but compresses history into a fixed-size state, so individual past observations are no longer directly accessible. We introduce LOCI, a hybrid spatial-memory architecture that keeps both representations. In half of the transformer blocks, main attention keeps a key-value cache of past observations; in the other half, it is restricted to the current chunk and complemented by a recurrent linear-attention memory whose reads and writes are conditioned on projective camera geometry, so viewpoint enters both memory addressing and stored content. Recurrent readouts flow into subsequent cache-backed blocks and supply their queries with accumulated scene context. On the public MIND memory benchmark and on held-out recorded trajectories, LOCI reproduces revisited content more faithfully than representative world models and a same-recipe full-softmax model; with full history, it lowers peak memory at equal length by about 30% relative to full softmax. With a bounded bank of retained observations, it streams long videos at constant memory and remains more faithful than full softmax under the same budget.

### 🤖 AI 总结

**一句话总结**：When a camera revisits a previously observed region, a video world model should reproduce what was there before. This requires both remembering past observations and retrieving the right one for the c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LOCI, Spatial, Linear, Memory, Streaming, World, Models, When

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40222v1) | [下载PDF](https://arxiv.org/pdf/2609.40222v1.pdf)

---

## [22. Recognition of Urbanized Areas in UAV-Derived Very-High-Resolution Visible-Light Imagery](https://arxiv.org/abs/2609.40212v1)

**作者**：Edyta Puniach, Wojciech Gruszczyński, Paweł Ćwiąkała 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-30

### 📄 论文摘要

This study compared classifiers that differentiate between urbanized and non-urbanized areas based on unmanned aerial vehicle (UAV)-acquired RGB imagery. The tested solutions in-cluded numerous vegetation indices (VIs) thresholding and neural networks (NNs). The analysis was conducted for two study areas for which surveys were carried out using different UAVs and cameras. The ground sampling distances for the study areas were 10 mm and 15 mm, respectively. Reference classification was performed manually, obtaining approximately 24 million classified pix-els for the first area and approximately 3.8 million for the second. This research study included an analysis of the impact of the season on the threshold values for the tested VIs and the impact of image patch size provided as inputs for the NNs on classification accuracy. The results of the con-ducted research study indicate a higher classification accuracy using NNs (about 96%) compared with the best of the tested VIs, i.e., Excess Blue (about 87%). Due to the highly imbalanced nature of the used datasets (non-urbanized areas constitute approximately 87% of the total datasets), the Mat-thews correlation coefficient was also used to assess the correctness of the classification. The analysis based on statistical measures was supplemented with a qualitative assessment of the classification results, which allowed the identification of the most important sources of differences in classification between VIs thresholding and NNs.

### 🤖 AI 总结

**一句话总结**：This study compared classifiers that differentiate between urbanized and non-urbanized areas based on unmanned aerial vehicle (UAV)-acquired RGB imagery. The tested solutions in-cluded numerous vegeta...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Recognition, Urbanized, Areas, UAV-Derived, Very-High-Resolution, Visible-Light, Imagery

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40212v1) | [下载PDF](https://arxiv.org/pdf/2609.40212v1.pdf)

---

## cs.LG

## [23. Ranking-Aware Prompt Optimization for Multimodal Clinical Diagnosis](https://arxiv.org/abs/2609.40361v1)

**作者**：Tian Xia, Minghao Liu, Yiqing Liang 等 5 位作者  
**分类**：cs.LG, cs.CL, cs.CV  
**发布时间**：2026-09-30

### 📄 论文摘要

Multimodal large language models (MLLMs) are rapidly advancing clinical diagnosis, yet their adaptation pipelines remain anchored to accuracy-based objectives. Clinical data are heavily class-imbalanced: a constant-majority predictor can score above 90% accuracy while being clinically useless. We therefore evaluate and optimize for AUROC, a threshold-free score that ranks positives above negatives and is invariant to class balance. We focus on prompt optimization in MLLMs. Reflective methods such as GEPA use a binary scores matrix with one row per evaluation instance and one column per candidate prompt; cells record per-instance correctness, so the column average is accuracy and drives candidate selection. We introduce pair-level Pareto prompt evolution (Ranking-PE), which replaces each correctness row with a pairwise-ordering row over (positive, negative) instance pairs: the cell is 1 if the candidate scores the positive higher than the paired negative. The column average then equals empirical AUROC (by the Wilcoxon-Mann-Whitney identity). We apply this swap at all three layers the prompt evolution search reads from - the scores matrix that decides Pareto dominance, the per-example feedback to the reflection LM, and final candidate selection - at no extra model calls and with no surrogate loss. Across three diseases on MIMIC, accuracy-based prompt evolution can degrade ranking; Ranking-PE reverses this, beating the accuracy-based recipe by +5.8 AUROC pp on fine-tuned Qwen3-VL-8B and +16.2 pp on MedGemma-4B. Ablations examine each design component and show that a medical-grade visual backbone - via vision-encoder-tuned SFT or medical pretraining - is a prerequisite that prompt search cannot replace - our recipe extends reflective prompt evolution from text-only data to multimodal clinical decision-making.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) are rapidly advancing clinical diagnosis, yet their adaptation pipelines remain anchored to accuracy-based objectives. Clinical data are heavily class-imbalanc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Ranking-Aware, Prompt, Optimization, Multimodal, Clinical, Diagnosis, large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40361v1) | [下载PDF](https://arxiv.org/pdf/2609.40361v1.pdf)

---

## [24. Removing Timing Shortcuts Improves Non-Invasive Brain-to-Text](https://arxiv.org/abs/2609.40359v1)

**作者**：Dulhan Jayalath, Oiwi Parker Jones  
**分类**：cs.LG, q-bio.NC  
**发布时间**：2026-09-30

### 📄 论文摘要

We find that major reported improvements in decoding words from non-invasive brain recordings are largely reproducible without any brain data. In the influential work of d'Ascoli et al. (2025), time series of brain activity from subjects perceiving continuous speech are segmented into fixed-length windows starting at each word. A neural network then generates predictions for all of the words in a sentence together. Neighbouring windows partially overlap, implicitly revealing the interval between words. Since these intervals indicate the duration of the words spoken, and different words tend to have different durations - for example, "the" is much shorter than "supercalifragilisticexpialidocious" - the neural network can improve its predictions of words without relying on the underlying brain activity. Consistent with this, the method reaches 22.0% balanced accuracy on synthetic signals containing no brain information, compared with 22.3% on real brain recordings. To prevent the network from learning this shortcut, we make a single, simple change. Instead of jointly encoding all windows in a sentence, we process each independently. As a result, the neural network achieves better performance by learning underlying word-specific information from brain recordings. This makes two existing strategies become much more effective than before. Both aggregating predictions from distinct neural responses to the same word and using a pretrained LLM as a linguistic prior now substantially improve results. On our perceived speech benchmark, this simple recipe (SimpleB2T) achieves a word error rate of 36.6% with five observations per word, approaching past invasive speech decoding performance, albeit under different conditions. The results in this work expose an important shortcut in brain-to-text decoding and show that removing it leads to a simple and considerably more effective strategy.

### 🤖 AI 总结

**一句话总结**：We find that major reported improvements in decoding words from non-invasive brain recordings are largely reproducible without any brain data. In the influential work of d'Ascoli et al. (2025), time s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Removing, Timing, Shortcuts, Improves, Non-Invasive, Brain-to-Text, find

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40359v1) | [下载PDF](https://arxiv.org/pdf/2609.40359v1.pdf)

---

## [25. Is Weight Tying Still Beneficial for Decoder-Only LLMs in Private Settings Under DP-SGD?](https://arxiv.org/abs/2609.40335v1)

**作者**：Razan El Mais, Ali Chehab, Ibrahim Issa 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-30

### 📄 论文摘要

Differentially Private Stochastic Gradient Descent (DP-SGD) is a leading approach for privacy-preserving fine-tuning of large language models (LLMs). Many decoder-only LLMs employ weight tying between input and output embeddings, a design choice originally introduced for parameter efficiency and improved language modeling performance in the non-private setting. However, the impact of weight tying under differentially private training remains largely unexplored. In this work, we investigate the role of weight tying in the DP setting using GPT2 and DistilGPT2 as representative decoder-only architectures. Interestingly, we find that untied embeddings consistently outperform weight-tied models under DP-SGD, achieving gains of up to 4.74% points in accuracy on SST-2, QNLI, and QQP. Beyond improved utility, untying embeddings enables the use of memory-efficient ghost clipping for DP-SGD. By contrast, weight tying introduces shared-parameter interactions that complicate standard ghost norm computation and largely negate its computational advantages. As a result, untied models achieve over 60% lower memory usage while preserving the benefits of ghost clipping. Our results indicate that untied embeddings provide a more effective and scalable design for differentially private training of decoder-only LLMs and highlight the need to revisit standard LLM architectural choices in the privacy-preserving setting.

### 🤖 AI 总结

**一句话总结**：Differentially Private Stochastic Gradient Descent (DP-SGD) is a leading approach for privacy-preserving fine-tuning of large language models (LLMs). Many decoder-only LLMs employ weight tying between...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Weight, Tying, Still, Beneficial, Decoder-Only, Private, Settings

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40335v1) | [下载PDF](https://arxiv.org/pdf/2609.40335v1.pdf)

---

## [26. Disentangling Computation in Multi-Task Neural Networks with the Green's Operator](https://arxiv.org/abs/2609.40292v1)

**作者**：James Hazelden  
**分类**：cs.LG, q-bio.NC  
**发布时间**：2026-09-30

### 📄 论文摘要

How is computation organized and reused across tasks and time in a trained recurrent network? Most analyses emphasize the geometry of neural activity, dynamical motifs, or local perturbation growth. We instead study the network's global first-order perturbation response. The finite-horizon Green's operator maps perturbations at each source along a trajectory to their downstream state-space responses and therefore directly represents perturbation routing. Simple reductions of this operator provide task-to-task and time-to-time views of the same computation, while matrix-free products make these views accessible without constructing the full operator. In a flexible multitask recurrent network, task reductions reveal structured reuse of known computational motifs, while temporal reductions reveal causal pathways and how they emerge during training. Our main point is simple: the Green's operator provides a global response geometry for mapping the organization of learned dynamical computation.

### 🤖 AI 总结

**一句话总结**：How is computation organized and reused across tasks and time in a trained recurrent network? Most analyses emphasize the geometry of neural activity, dynamical motifs, or local perturbation growth. W...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Disentangling, Computation, Multi-Task, Neural, Networks, Green's, Operator, How

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40292v1) | [下载PDF](https://arxiv.org/pdf/2609.40292v1.pdf)

---

## [27. PMosFM: Preconditioned Manifold Matching for One-Step Physics-Constrained Generation](https://arxiv.org/abs/2609.40287v1)

**作者**：Zhangyong Liang, Haibin Ling  
**分类**：cs.LG  
**发布时间**：2026-09-30

### 📄 论文摘要

Physics-constrained generative models aim to generate physical fields that match a target distribution and satisfy prescribed constraints. However, enforcing these constraints often increases sampling costs through iterative corrections or training costs through residual optimization and trajectory unrolling. To address this issue, we introduce \textbf{P}reconditioned \textbf{M}anifold \textbf{o}ne-\textbf{s}tep \textbf{F}low \textbf{M}atching (\textbf{PMosFM}), a preconditioned manifold matching framework for one-step physics-constrained generation. By encoding constraints in a manifold decoder, PMosFM learns transport in intrinsic coordinates without separate residual losses or terminal residual unrolling. A geometric preconditioner rescales coordinates using the decoder-induced metric, while a regularized covariance transform approximately whitens the interpolation-state inputs. A finite-interval objective couples velocity supervision with consistency between decoded endpoints in physical space. We show that exact parameterization removes residual-induced Gauss--Newton curvature, that geometric and covariance effects separate in a local conditioning bound, and that physical flow-map error bounds endpoint distributional error. Controlled ablations examine conditioning, and experiments evaluate optimizer-update time and memory footprint. At inference, PMosFM uses one neural transport evaluation followed by physical decoding. Experiments across benchmarks show lower training and sampling time than the multi-step baselines at comparable physical and distributional fidelity. Code and datasets will be released publicly.

### 🤖 AI 总结

**一句话总结**：Physics-constrained generative models aim to generate physical fields that match a target distribution and satisfy prescribed constraints. However, enforcing these constraints often increases sampling...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PMosFM, Preconditioned, Manifold, Matching, One-Step, Physics-Constrained, Generation, generative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40287v1) | [下载PDF](https://arxiv.org/pdf/2609.40287v1.pdf)

---

## [28. cua-speedrun: Standardized Benchmarking of the Speed of Computer-Use Agents](https://arxiv.org/abs/2609.40284v1)

**作者**：Pranjal Aggarwal, Lawrence Keunho Jang, Sean Welleck 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-09-30

### 📄 论文摘要

Computer use agents (CUAs), which use graphical user interfaces (GUIs) to complete tasks on a computer, have recently surpassed human performance on many standard benchmarks, including difficult long-horizon tasks. Their capabilities are undoubtedly impressive, however, a key barrier to the widespread adoption and deployment of CUAs remains their speed and cost. Progress towards faster yet capable CUAs requires reliable evaluation of their speed, but many CUA benchmarks currently face a reproducibility crisis. Benchmarks are based on complex infrastructure with varying machine and container configurations that confound the evaluation of the execution speed of CUAs. Towards addressing this gap, we propose cua-speedrun, which introduces standardized infrastructure and task sets, with a focus on evaluating the speed and efficiency of CUAs. cua-speedrun uses a uniform virtual machine setup and execution pipeline, along with a common agent interface that enables single-agent implementations to operate seamlessly across different benchmarks. Across four different CUA benchmarks, we evaluate how reasoning effort, agent harnesses, and environment latency affect performance, speed, and cost. We find no single model family is optimal for all three; none of the open-weight models are on the frontier, and also, unintuitively, for some models increasing the reasoning effort can speed up task completion, while faster environment input-output can slow down overall task completion time. We also demonstrate that we can effectively reduce the evaluation task set of most CUA benchmarks without degrading overall statistical power, allowing for more efficient benchmarking and comparison. We believe cua-speedrun will enable structured progress towards fast, efficient CUAs, unlocking new real-world use cases and applications. All code, infrastructure, and analysis are available at https://cuaspeedrun.com.

### 🤖 AI 总结

**一句话总结**：Computer use agents (CUAs), which use graphical user interfaces (GUIs) to complete tasks on a computer, have recently surpassed human performance on many standard benchmarks, including difficult long-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, cua-speedrun, Standardized, Benchmarking, Speed, Computer-Use, Computer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40284v1) | [下载PDF](https://arxiv.org/pdf/2609.40284v1.pdf)

---

## [29. OpenTSLM TeeMoE: A Unified Time-Series Language Model for Forecasting, Contextual Prediction, and Reasoning](https://arxiv.org/abs/2609.40265v1)

**作者**：Tony Chen, Timo Stoffregen, Maxwell Xu 等 11 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-30

### 📄 论文摘要

Real-world time-series applications increasingly require models that can handle time series forecasting, context-conditioned prediction, and language-based temporal reasoning. Yet current time-series foundation models remain fragmented across these capabilities: numerical specialists often provide the strongest forecasts, while language-based models offer broader contextual understanding and analysis. A central challenge is to unify these heterogeneous capabilities without reducing their individual performance. We introduce OpenTSLM TeeMoE, a generalist time-series language model that can forecast directly from observed time series, reason over textual context and temporal patterns, and synthesize and refine predictions from external numerical forecasting specialists. We independently train three low-rank experts for forecast aggregation, native forecasting, and temporal analysis over a shared backbone. A learned LoRA mixture-of-experts controller then weights their frozen parameter updates for each request. Our proposed model achieves strong performance on widely used benchmarks for time series forecasting, context-conditioned prediction, and language-based temporal reasoning, ranking among the top three on GIFT-Eval by mean MASE rank, Context is Key by RCRPS, and TimeSeriesExam by accuracy.

### 🤖 AI 总结

**一句话总结**：Real-world time-series applications increasingly require models that can handle time series forecasting, context-conditioned prediction, and language-based temporal reasoning. Yet current time-series ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OpenTSLM, TeeMoE, Unified, Time-Series, Language, Model, Forecasting, Contextual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40265v1) | [下载PDF](https://arxiv.org/pdf/2609.40265v1.pdf)

---

## [30. PhantomEnvironments: Training LLM Agents in Fictional Worlds](https://arxiv.org/abs/2609.40221v1)

**作者**：Anmol Kabra, Swathi Saravana Selvam, Albert Gong 等 8 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-09-30

### 📄 论文摘要

Training LLM agents with reinforcement learning (RL) is bottlenecked by environments, which must provide verifiable rewards, support long-horizon interaction, and scale cheaply. Existing approaches rely on costly human-curated data or on LLM-generated environments that risk hallucinations and benchmark contamination. We show that LLMs can instead be trained into capable search agents using synthetic environments generated entirely by rules, whose generation requires no LLM and has zero marginal cost. We build PhantomEnvironments, multi-turn RL environments from fictional worlds, where agents must search a corpus of templated articles to answer multi-hop questions. Despite sharing no facts with the real world, these strikingly simple environments yield agents that transfer to real-world multi-hop search benchmarks, often outperforming real-world training data on newer benchmarks. Trained agents generalize to unseen fictional universes, and Qwen models learn to scale their search budget roughly linearly with question difficulty, suggesting emergent search scaling from environment interaction alone. Ablating environment complexity reveals that hop count drives transfer more than constraints or comparisons: even the simplest rule-generated environments are a surprisingly effective, free resource for training generalizable LLM agents.

### 🤖 AI 总结

**一句话总结**：Training LLM agents with reinforcement learning (RL) is bottlenecked by environments, which must provide verifiable rewards, support long-horizon interaction, and scale cheaply. Existing approaches re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, PhantomEnvironments, Training, Fictional, Worlds, reinforcement, learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.40221v1) | [下载PDF](https://arxiv.org/pdf/2609.40221v1.pdf)

---

