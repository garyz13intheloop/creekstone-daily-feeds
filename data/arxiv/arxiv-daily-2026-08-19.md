# arXiv AI 论文日报 | 2026-08-19

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (10 篇)
- [cs.CL](#csCL) (6 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.LG](#csLG) (8 篇)

---

## cs.AI

## [1. On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification](https://arxiv.org/abs/2608.18066v1)

**作者**：Qinyuan Ye, Yu Li, Yada Pruksachatkun 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-08-18

### 📄 论文摘要

Memory-based self-improving agents--those that learn from an online stream of tasks and improve over time by maintaining a textual memory bank--have shown great promise in recent literature. However, the reliability aspects of these methods have been critically overlooked. In this work, we conduct a comprehensive re-evaluation of two memory-based methods, broadening the scope of evaluation along two axes: (1) including multiple runs to quantify variance, and (2) randomly shuffling the tasks to investigate the effect of task order. Through these experiments, we make two observations that expose the fragility of current methods: First, agent evaluation is inherently noisy in complex environments and on multi-step tasks, and stacking a self-improving loop on top can further amplify this noise. Second, the agent's improvement is highly dependent on task order. Prior works often adopt default orderings that impose an implicit curriculum, acting as a hidden prerequisite for success.   To better understand this fragility, we manually examine the agents' memory and hypothesize that task and environment underspecification contribute to this fragility. We validate this hypothesis by incorporating information that enables better specification, such as detailed rubrics and environment feedback, into the memory construction process. While this added information partially closes the performance degradation in previous experiments, significant gaps still remain, suggesting that other uncharacterized factors contribute to this fragility. Looking ahead, our work advocates for more rigorous evaluation protocols for self-improving agents by reporting results across multiple runs and stress-testing them under challenging conditions. Moreover, our findings on underspecification call for systems and interfaces that enable effective human oversight, preventing agents from failing in unforeseeable ways.

### 🤖 AI 总结

**一句话总结**：Memory-based self-improving agents--those that learn from an online stream of tasks and improve over time by maintaining a textual memory bank--have shown great promise in recent literature. However, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, Fragility, Self-Improving, Variance, Task, Order, Underspecification

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18066v1) | [下载PDF](https://arxiv.org/pdf/2608.18066v1.pdf)

---

## [2. HLSR: Hybrid Live Forecast Selective Dynamic Vehicle Rerouting for Real-Time Congestion Avoidance](https://arxiv.org/abs/2608.18056v1)

**作者**：Xiao Wang, Shun Ren Yang, Hui Nien Hung  
**分类**：cs.AI  
**发布时间**：2026-08-18

### 📄 论文摘要

Urban traffic congestion reduces productivity and increases travel cost and emissions. Network-wide live travel-time shortest-path rerouting can be highly effective in simulation, but assumes that essentially every on-road vehicle is replanned every decision period. We propose HLSR, a selective hybrid live--forecast vehicle rerouting framework that fuses live edge speeds with short-horizon forecasts under limited intervention scope. Building on dual-threshold congestion detection, calibrated upstream selection, and driver-tailored travel-time prediction, HLSR further introduces approaching-vehicle expansion, travel-time-weighted k-shortest-path generation, and a horizon-dependent hybrid live--forecast segment speed used in multi-cost route allocation.

### 🤖 AI 总结

**一句话总结**：Urban traffic congestion reduces productivity and increases travel cost and emissions. Network-wide live travel-time shortest-path rerouting can be highly effective in simulation, but assumes that ess...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HLSR, Hybrid, Live, Forecast, Selective, Dynamic, Vehicle, Rerouting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18056v1) | [下载PDF](https://arxiv.org/pdf/2608.18056v1.pdf)

---

## [3. StagedWorkspace: A Versioned Workspace for Knowledge-Work Agents](https://arxiv.org/abs/2608.18050v1)

**作者**：Yining Hua, Hongbin Na, Yifan Zhou 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-18

### 📄 论文摘要

AI agents increasingly perform knowledge work (i.e., produce and modify persistent digital artifacts such as code repositories, documents, spreadsheets, slides, reports), yet the parsed views they search, the native files they edit, the changes they review, and the artifacts they submit can refer to different versions of the same work product. We formulate this as a workspace-state contract: every view should be explicitly tied to a version of the evolving workspace state. Coding agents partly address this need through repository contracts for search, diffs, and tests, whereas an analogous contract is less explicit for PDFs, spreadsheets, slides, notebooks, and mixed-format project folders. We propose StagedWorkspace, a versioned workspace for knowledge-work agents. The workspace binds parsed records and review diffs to content hashes of the native files as they change. In fixed-harness ablations on OfficeQA Pro and APEX-Agents, dual parsed/native access has the highest point estimate for every tested model; relative to the more limiting single view, it improves OfficeQA Pass@1 by 8.3-12.1 points and APEX mean rubric score by 4.7-9.2 points. SW-AGENT scores 63.9% with Gemini 3.1 Pro on OfficeQA and 42.1 with GPT-5.4 Nano on APEX, compared with published same-model scores of 29.3% and 25.5, respectively. A paired review-axis ablation on 57 file-editing tasks further finds higher observed scores when diffs are visible. These results identify workspace state as an experimental variable in knowledge-work agents and motivate benchmarks that score evidence, staged edits, and submitted artifacts as explicit state transitions.

### 🤖 AI 总结

**一句话总结**：AI agents increasingly perform knowledge work (i.e., produce and modify persistent digital artifacts such as code repositories, documents, spreadsheets, slides, reports), yet the parsed views they sea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, StagedWorkspace, Versioned, Workspace, Knowledge-Work, increasingly, perform, knowledge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18050v1) | [下载PDF](https://arxiv.org/pdf/2608.18050v1.pdf)

---

## [4. Can Large Language Models Explain Flight Safety Events? A Prior-Guided Semantic LLM-based Approach](https://arxiv.org/abs/2608.18017v1)

**作者**：Lu Xu, Xu Li, Linjiang Zheng 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-18

### 📄 论文摘要

Improving flight safety with flight data requires not only accurate detection of risk events, but more importantly, clear interpretation of their underlying causes at the level of pilot control behavior. Existing explainable AI techniques, such as feature importance maps, often require considerable domain knowledge to translate them into operationally meaningful explanations. Large Language Models (LLMs), which excel at language reasoning, bring a promising solution to this issue. However, applying LLMs in this domain presents key challenges such as modal inconsistency, limited classification ability, scarcity of task-specific data for fine-tuning, and lack of domain knowledge. To overcome these challenges, we propose FlightLLM, a prior-guided semantic LLM-based approach for interpretable flight safety analysis. Specifically, we first perform feature engineering to address modal inconsistency, combining statistical descriptors with physically meaningful flight indicators. This representation is further processed by a Semantic Discretization module, which converts abstract numerical patterns into qualitative descriptions that are more compatible with language reasoning. In addition, since LLMs are not inherently strong classifiers, CatBoost is incorporated as a statistical expert, and its prediction results are injected into the prompt as prior guidance. A contrastive few-shot learning strategy is further adopted to compensate for limited data. Finally, we design structured prompts to embed aviation-specific knowledge into the inference process. Using hard landing, a representative risk event with complex causal mechanisms, as an anchor point, we evaluate FlightLLM on a dataset of 704 real-world A320 flight samples. Experimental results show that the proposed approach achieves competitive classification performance while generating direct and reasonable explanations for event causes.

### 🤖 AI 总结

**一句话总结**：Improving flight safety with flight data requires not only accurate detection of risk events, but more importantly, clear interpretation of their underlying causes at the level of pilot control behavi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Can, Large, Language, Models, Explain, Flight, Safety, Events?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18017v1) | [下载PDF](https://arxiv.org/pdf/2608.18017v1.pdf)

---

## [5. Towards Zero-Shot Task Transfer with Neurosymbolic World Models](https://arxiv.org/abs/2608.17959v1)

**作者**：Isidoro Tamassia, Lennert De Smet, Giuseppe Marra  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-08-18

### 📄 论文摘要

State-of-the-art model-based reinforcement learning methods learn neural world models that allow policy improvement by planning in a latent space, without assumptions on the structure of the underlying environment. While expressive, these models are generally task-dependent: they learn uninterpretable latent representations that are tied to the training task and thus hard to generalize to new tasks. In this work, we present a novel world model formulation where the reward prediction only depends on a subset of structured, symbolic components of the whole latent state. Decoupling observation reconstruction and reward prediction allows us to learn world models that can adapt zero-shot, i.e. without further environment interactions, to new reward functions defined over the same symbolic state space. We discuss the main advantages and challenges of learning these neurosymbolic world models and demonstrate the strong generalisation properties of our approach over purely neural methods.

### 🤖 AI 总结

**一句话总结**：State-of-the-art model-based reinforcement learning methods learn neural world models that allow policy improvement by planning in a latent space, without assumptions on the structure of the underlyin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Towards, Zero-Shot, Task, Transfer, Neurosymbolic, World, Models, State-of-the-art

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17959v1) | [下载PDF](https://arxiv.org/pdf/2608.17959v1.pdf)

---

## [6. Procedural Content Metageneration via Program Search and Continual Abstraction Discovery](https://arxiv.org/abs/2608.17947v1)

**作者**：Matthew Siper, Ahmed Khalifa, Julian Togelius  
**分类**：cs.AI, cs.LG, cs.NE  
**发布时间**：2026-08-18

### 📄 论文摘要

Large language models can generate executable programs, which makes it possible to search directly over procedural content generators rather than individual levels. We study this approach in Sokoban, Zelda, Dangerous Dave, and Lode Runner. Each run evolves complete Python generators through language-model mutation and crossover. We introduce Continual Abstraction Discovery, or CAD, which extracts reusable primitives from high-fitness programs into a run-specific helper module. A 2x2 experiment crosses CAD with access to a fixed hand-written domain API. The completed data set contains 160 complete runs, with at least ten 50-generation runs in every cell. CAD raises mean final best fitness in all eight domain and API comparisons. Across all CAD runs, learned libraries are adopted by most later programs and repeatedly rediscover validation, reachability, and structural utilities. These results support that discovering reusable primitives improves evolutionary program search for content generators.

### 🤖 AI 总结

**一句话总结**：Large language models can generate executable programs, which makes it possible to search directly over procedural content generators rather than individual levels. We study this approach in Sokoban, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Procedural, Content, Metageneration, via, Program, Search, Continual, Abstraction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17947v1) | [下载PDF](https://arxiv.org/pdf/2608.17947v1.pdf)

---

## cs.CL

## [7. Multi-Agent AI System for Radiology Report Structuring and Quality Assurance with Independent Radiologist Evaluation](https://arxiv.org/abs/2608.18072v1)

**作者**：Iryna Hartsock, Cesar Lam, Christopher Otteni 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-18

### 📄 论文摘要

Purpose: To develop and evaluate a locally deployed multi-agent AI system for radiology report structuring and quality assurance. Materials and Methods: This retrospective study included 638 radiology reports from CT examinations of the chest, abdomen, and pelvis dictated by 15 board-certified radiologists in 2023 and 2024. A multi-agent AI pipeline was developed to perform report structuring and quality assurance (QA). The system structured the report into standardized anatomical sections at the sentence level using regex rules and local large language models. It also detected mismatches between the Findings and Impression sections, or within sections; gender-anatomy conflicts; and undocumented communication of critical findings. Two board-certified radiologists independently evaluated a 45-report subset. Results: The multi-agent system structured the Findings sections of all reports (22,270 sentences) into a predefined anatomical format while retaining the original report content. The system flagged 90 (14.1%) reports, most commonly for section mismatches (80 reports, 12.5%). In the radiologist evaluation, both reviewers agreed that 31 (69%) were correctly restructured, 2 reports (4%) were incorrectly restructured, and disagreed on the remaining 12 reports (27%). Both reviewers agreed that no clinically important information was omitted and no fabricated content was introduced. Overall QA performance was rated as "excellent" or "good" in 84% of the evaluated reports, with the remaining reports rated as "fair". Conclusion: A locally deployed multi-agent AI system combined radiology report structuring and quality assurance within a single workflow. The system demonstrated favorable performance in radiologist evaluation. Such systems may support standardization of reporting and quality assurance in radiology practice.

### 🤖 AI 总结

**一句话总结**：Purpose: To develop and evaluate a locally deployed multi-agent AI system for radiology report structuring and quality assurance. Materials and Methods: This retrospective study included 638 radiology...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, System, Radiology, Report, Structuring, Quality, Assurance, Independent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18072v1) | [下载PDF](https://arxiv.org/pdf/2608.18072v1.pdf)

---

## [8. Language Has Two Parameters: Narrative-Induced Semantic Plasticity and Phase-Sensitive Interpretation](https://arxiv.org/abs/2608.18041v1)

**作者**：Hollis Robbins  
**分类**：cs.CL  
**发布时间**：2026-08-18

### 📄 论文摘要

Language has two parameters. Count how often words occur together and you estimate amplitude, the strength of association. Word embeddings and attention weights refine that count, which sums every writer in the corpus together. This paper claims a second parameter, phase, which signed weights learned from a corpus do not supply. Phase exists only between meanings: it determines how coactivated meanings combine, and it can reverse what a meaning contributes while that meaning stays fully present. A speaker can set phase in the signal through linguistic form; encounters install phase relations and history distributes them. Population averaging deletes history-indexed phase: agent-deindexed corpora identify the population marginal state and determine no individual or dyadic state, at any scale. The standard transformer has no explicit representation for phase in frozen inference, and the interpretability program measuring progress by monosemanticity is optimizing against it: the coexistence it treats as a defect is the condition of allusion, irony, and quotation. Six predictions test whether a suppressed meaning stays active, whether encounter order changes what a phrase does, whether marking the signal changes how a shared phrase is taken, and whether a model given a history is changed by it or only informed about it. The claim defended is the weak version: interpretation requires a second relational parameter, signed, persistent, and indexed to individuals and dyads. Quantum probability is one notation for the parameter; nothing in the formalism claims quantum processes in the brain. The strong version, that the quantum calculus constrains these phenomena as signed classical models do not, rests on an encounter-order constraint not yet derived. The architecture the theory calls for is a language model with agent-indexed, phase-bearing semantic states.

### 🤖 AI 总结

**一句话总结**：Language has two parameters. Count how often words occur together and you estimate amplitude, the strength of association. Word embeddings and attention weights refine that count, which sums every wri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Language, Has, Two, Parameters, Narrative-Induced, Semantic, Plasticity, Phase-Sensitive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18041v1) | [下载PDF](https://arxiv.org/pdf/2608.18041v1.pdf)

---

## [9. The IOL-AI Challenge: An Open Challenge towards Advancing Linguistic Reasoning](https://arxiv.org/abs/2608.18011v1)

**作者**：Eduardo Sánchez, Rita Berrada, Dan-Mircea Mirea 等 11 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-18

### 📄 论文摘要

Reasoning in LLMs is overwhelmingly studied in domains that provide a model with rules: mathematics and code. Linguistic puzzles invert this: the solver must first discover the system before reasoning within it. We present the IOL-AI Challenge, an open-science competition run on the unseen problems of the International Linguistics Olympiad (IOL) 2026 Individual Contest, evaluated both automatically and, for the first time, by members of the official IOL Jury under the same rubrics applied to human contestants. The challenge drew 731 submissions from 46 teams under a strict compute budget (one T4, 30 mins). We additionally benchmark 15 unconstrained frontier and open models, with Claude Opus 4.8 earning a jury score equivalent to a gold medal, while both resource-constrained systems we submitted for jury grading scored in the range of the bottom 5% of contestants. Capability was not determined by scale: 14B submissions outperform models twice their size, and gains come from decoding and output-handling rather than model capacity. We also found that automatic metrics rank systems exactly as the jury does, but compress the scale, upscoring weak systems by ~13 points and understating strong ones. Our analysis shows that while frontier models might have prior knowledge about some of the problem languages, it does not significantly help them solve the linguistic reasoning tasks, leaving linguistic reasoning as a strong benchmarking proxy for generalizable reasoning skills.

### 🤖 AI 总结

**一句话总结**：Reasoning in LLMs is overwhelmingly studied in domains that provide a model with rules: mathematics and code. Linguistic puzzles invert this: the solver must first discover the system before reasoning...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, IOL-AI, Challenge, Open, towards, Advancing, Linguistic, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18011v1) | [下载PDF](https://arxiv.org/pdf/2608.18011v1.pdf)

---

## [10. Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees](https://arxiv.org/abs/2608.17994v1)

**作者**：Sher Badshah, Ali Emami, Hassan Sajjad  
**分类**：cs.CL  
**发布时间**：2026-08-18

### 📄 论文摘要

Using LLMs as judges has become standard practice for evaluating model outputs at scale. This is particularly common for subjective, open-ended tasks such as assessing helpfulness or alignment, where no single reference answer exists. However, objective tasks introduce a distinct reliability challenge for reference-free LLM judging. In the absence of a reference answer, the judge evaluates factual correctness either through its parametric knowledge or through tool augmentation. Although the former enables efficient evaluation, the judge may hallucinate or lack sufficient evidence for its verdict. Conversely, tool augmentation can provide additional evidence but introduces extra computational cost and requires an appropriate mechanism to determine when and how that evidence should be used reliably. More importantly, neither approach alone provides formal control over the risk of accepted verdicts or guarantees their reliability at a specified level. We propose a risk-controlled framework that calibrates uncertainty thresholds on a held-out set so that the false discovery rate among accepted verdicts remains below a user-specified level~$α$ with high probability, using finite-sample Clopper--Pearson intervals. When the parametric mode is not sufficiently confident, the instance is routed to a retrieval-augmented mode, where the judge gathers web evidence and re-evaluates the instance under a second calibrated threshold. The finite-sample guarantee carries over to this two-threshold routing without additional assumptions. Across open-domain QA benchmarks and judges of varying scales, the framework maintains the target error rate while achieving substantially higher coverage than single-mode baselines.

### 🤖 AI 总结

**一句话总结**：Using LLMs as judges has become standard practice for evaluating model outputs at scale. This is particularly common for subjective, open-ended tasks such as assessing helpfulness or alignment, where ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：or, LLM, Judge, Retrieve, Abstain, Uncertainty-Guarded, Judging, Provable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17994v1) | [下载PDF](https://arxiv.org/pdf/2608.17994v1.pdf)

---

## [11. When Writing Style Drifts: Benchmarking Authorship Verification under Distribution Shifts in Genre, Time and the AI-Era](https://arxiv.org/abs/2608.17979v1)

**作者**：Lotta Kiefer, Brisca Balthes, Christoph Leiter 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-18

### 📄 论文摘要

Authorship verification (AV) assumes that an author's writing style remains sufficiently stable to distinguish it from that of other writers. In practice, however, this assumption is challenged by distribution shifts caused by changes in genre, time, and AI-assisted writing. Existing AV benchmarks typically study these factors in isolation and focus predominantly on English, limiting our understanding of model robustness under realistic conditions. We introduce AVShift, the first German benchmark for systematically evaluating AV under multiple distribution shifts. AVShift comprises over 150,000 text pairs spanning three genres and 21 years, enabling controlled evaluation of cross-genre, temporal, and AI-era shifts within a unified framework. We benchmark representative feature-based, embedding-based, and LLM-based approaches. Our experiments show that fine-tuned LLMs generalize best across genres and benefit substantially from stylistically diverse training data. We further demonstrate that temporal drift is one of the strongest factors affecting AV, with performance degrading significantly as the time gap between documents increases. In contrast, we find no evidence of a measurable AI-era distribution shift within AVShift. Finally, our feature analysis reveals stylistic features that remain stable across genres, while their relative importance varies depending on the specific genre transition. We release AVShift and our code for future research.

### 🤖 AI 总结

**一句话总结**：Authorship verification (AV) assumes that an author's writing style remains sufficiently stable to distinguish it from that of other writers. In practice, however, this assumption is challenged by dis...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Writing, Style, Drifts, Benchmarking, Authorship, Verification, under

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17979v1) | [下载PDF](https://arxiv.org/pdf/2608.17979v1.pdf)

---

## [12. Do Large Language Models Play Six Degrees of Separation? Measuring Topological Compression in Long-Context Manifolds](https://arxiv.org/abs/2608.17950v1)

**作者**：Md. Faiyaz Abdullah Sayeedi  
**分类**：cs.CL  
**发布时间**：2026-08-18

### 📄 论文摘要

Large Language Models (LLMs) demonstrate remarkable multi-hop reasoning capabilities over long contexts, yet the internal mechanisms enabling these distant cognitive leaps remain poorly understood. Traditional attention-based interpretability often fails to capture true semantic proximity due to routing artifacts like attention sinks. In this paper, we bypass attention weights to directly analyze the dynamic geometry of the hidden state manifold, proving that deep LLM latent spaces natively organize into Small-World networks. By sparsifying the continuous similarity matrices of long-context representations into unweighted graphs, we trace the connectivity between highly disjoint semantic anchors across two distinct architectures. Our findings reveal a sharp topological phase transition: while early syntactic layers remain entirely fractured, deep reasoning layers abruptly compress massive conceptual distances into highly navigable pathways strictly bounded by the "Six Degrees of Separation" limit (=< 6 semantic hops). Furthermore, we demonstrate the practical efficacy of this framework by applying it to zero-shot hallucination detection within Retrieval-Augmented Generation (RAG) using the RAGognize dataset. We show that factually grounded generations maintain structural integrity with their source context (approximately 3 hops), whereas hallucinations induce severe topological collapse. Ultimately, this work mathematically formalizes how transformers execute abstract reasoning and provides a novel, strictly geometric signature for evaluating factual reliability.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) demonstrate remarkable multi-hop reasoning capabilities over long contexts, yet the internal mechanisms enabling these distant cognitive leaps remain poorly understood. Tr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, of, Large, Language, Models, Play, Six, Degrees

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17950v1) | [下载PDF](https://arxiv.org/pdf/2608.17950v1.pdf)

---

## cs.CV

## [13. From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for Generalist Image Generation](https://arxiv.org/abs/2608.18076v1)

**作者**：Xingjian Wang, Zhao Wang, Taihang Hu 等 17 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-18

### 📄 论文摘要

Large-scale image generation has benefited from advances in data scale, quality, rebalancing, and recaptioning, yet conventional pipelines typically optimize task-specific datasets in isolation. A central challenge is not only how to curate each task-specific corpus, but also how to organize heterogeneous supervision according to the dependencies among generative capabilities. We present a \textbf{capability-driven data infrastructure} that couples capability-specific supervision construction with capability-aligned curriculum scheduling. Its three specialized yet interoperable data engines build complementary relational supervision for text-image grounding, inter-image transformation, and image-knowledge association, while caption experts align T2I and editing supervision across tasks and granularities. A multi-stage curriculum jointly evolves task composition, visual-concept distribution, data quality, and image resolution along the dependency order of capability acquisition, with capability-aware evaluation closing the loop through targeted retrieval, expert construction, and gap-aware resampling. At scale, the framework curates a 440M-image T2I corpus, 120M editing pairs, and over 27M image-entity pairs. With this infrastructure, we train multimodal diffusion models at two scales from scratch, with 3B and 6B sizes respectively. We conduct quantitative evaluation on CPI-Bench, along with qualitative evaluations across diverse text-to-image and editing scenarios. Experimental results present broad visual coverage, versatile rendering, and effective transfer across generative capabilities.

### 🤖 AI 总结

**一句话总结**：Large-scale image generation has benefited from advances in data scale, quality, rebalancing, and recaptioning, yet conventional pipelines typically optimize task-specific datasets in isolation. A cen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Corpora, Co-Evolving, Capabilities, Capability-Centric, Data, Design, Generalist, Image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18076v1) | [下载PDF](https://arxiv.org/pdf/2608.18076v1.pdf)

---

## [14. EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing](https://arxiv.org/abs/2608.18063v1)

**作者**：Jiayi Song, Shijie Huang, Fangtai Wu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-18

### 📄 论文摘要

High-resolution image editing is increasingly demanded in professional workflows, yet existing diffusion-based models remain constrained to resolutions below 1K due to quadratic attention complexity and prohibitive memory requirements. A prevalent workaround employs a two-stage pipeline: editing at low resolution followed by independent super-resolution. However, this approach suffers from two critical issues: information divergence, where hallucinated details contradict the original high-resolution (HR) source, and texture degradation, manifesting as over-smoothed or over-sharpened artifacts. We propose EditBridge, a diffusion bridge framework for efficient ultra high-resolution editing. Unlike conventional diffusion that regenerates from noise, we formulate refinement as structured data-to-data translation from the low-resolution (LR) edited result to its HR counterpart, explicitly conditioned on the original HR source to preserve authentic details. To efficiently incorporate HR source guidance, we introduce a prior-guided block-wise sparse attention mechanism that exploits semantic correspondence from first-stage editing to constrain cross-image interactions to spatially aligned regions, significantly reducing computational overhead. Extensive experiments demonstrate that EditBridge achieves high-fidelity editing with superior perceptual quality at resolutions up to 4K, delivering 3.6--8.4$\times$ speedup at 2K and enabling practical 4K editing in 61 seconds.

### 🤖 AI 总结

**一句话总结**：High-resolution image editing is increasingly demanded in professional workflows, yet existing diffusion-based models remain constrained to resolutions below 1K due to quadratic attention complexity a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EDITBRIDGE, Towards, Faithful, Efficient, Ultra-High-Resolution, Image, Editing, High-resolution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18063v1) | [下载PDF](https://arxiv.org/pdf/2608.18063v1.pdf)

---

## [15. Plug-and-Play Traffic Element Awareness for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.18035v1)

**作者**：Zongzheng Zhang, Jijun Wang, Saining Zhang 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-18

### 📄 论文摘要

Traffic elements such as traffic lights and road signs play a fundamental role in human driving decisions and should naturally influence end-to-end driving performance. However, existing end-to-end driving research predominantly focuses on dynamic road participants (e.g., vehicles and pedestrians), while the role of traffic elements remains largely unexplored. The community still lacks a systematic study quantifying their impact, largely because public datasets rarely provide structured traffic-element annotations and modern driving systems vary widely in architecture and training paradigm. In this work, we present the first systematic investigation of traffic element awareness for end-to-end autonomous driving. We construct a unified research infrastructure by augmenting multiple public driving datasets with comprehensive traffic-element annotations. To support diverse model families, we adopt a minimal and universal integration design that incorporates traffic-element signals into existing pipelines in a plug-and-play manner with negligible architectural modification. We evaluate this design across modern paradigms, including perception-prediction-planning pipelines, vision-language-action models (VLA), regression-based planners, diffusion-based policies, and trajectory-scoring frameworks, on nuScenes, NAVSIM-v1, NAVSIM-v2, and Bench2Drive. Across all paradigms and datasets, this simple integration consistently improves driving performance, demonstrating that traffic element awareness provides a robust and generalizable signal for end-to-end driving systems. Notably, on the challenging NAVSIM-v2 benchmark, our approach significantly improves state-of-the-art architectures and data pipelines, establishing a new state of the art.

### 🤖 AI 总结

**一句话总结**：Traffic elements such as traffic lights and road signs play a fundamental role in human driving decisions and should naturally influence end-to-end driving performance. However, existing end-to-end dr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Plug-and-Play, Traffic, Element, Awareness, End-to-End, Autonomous, Driving, elements

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18035v1) | [下载PDF](https://arxiv.org/pdf/2608.18035v1.pdf)

---

## [16. Deep Academic Survey: Stateful Agentic Closed-Loop Paradigm for Academic Survey Automation](https://arxiv.org/abs/2608.18034v1)

**作者**：Zhikai Xu, Zhucun Xue, Teng Hu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-18

### 📄 论文摘要

Academic surveys play a central role in organizing rapidly expanding scholarly literature, yet their construction requires extensive paper analysis, coherent knowledge organization, fine-grained citation support, and reliable manuscript assembly. Existing Deep Research and automated survey generation systems address parts of this process, but typically do not coordinate paper understanding, literature organization, evidence-grounded drafting, and manuscript validation through a shared, revisable state. We introduce DAS, a stateful agentic framework for generating publication-oriented academic surveys. Its key idea is to separate reusable paper analysis from topic-specific manuscript construction. DAS builds on DAS-2M, a dynamically updated metadata lake containing survey-oriented representations of approximately two million papers. Its agents maintain explicit literature, organization, writing, and finalization states through candidate-grounded taxonomy planning, reverse paper-to-section routing, and hierarchical claim and citation planning. Semantic review reactivates only the affected writing states for repair and reevaluation, forming a scoped closed loop with deterministic validation. We further introduce DAS-Bench, a 30-topic benchmark, together with DAS-Eval, which assesses scholarly citation quality, taxonomic synthesis, hierarchical discourse, and manuscript assembly reliability through 16 criteria. Among systems evaluated on all 30 topics, DAS achieves the highest average in all four dimensions, with an overall score of 4.34 compared with 4.03 for the strongest competitor, and the same ordering is preserved on the matched 21-topic CS subset. Blinded expert evaluation further prefers DAS to Naive RAG on 27 of 30 topics and to AutoSurvey on 19 of 21 shared CS topics. The project page is available at https://zhikaixu24.github.io/projects/DAS/.

### 🤖 AI 总结

**一句话总结**：Academic surveys play a central role in organizing rapidly expanding scholarly literature, yet their construction requires extensive paper analysis, coherent knowledge organization, fine-grained citat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Deep, Academic, Survey, Stateful, Agentic, Closed-Loop, Paradigm, Automation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18034v1) | [下载PDF](https://arxiv.org/pdf/2608.18034v1.pdf)

---

## [17. Initialization-Free Bundle Adjustment Revisited: A Controlled Experimental Study](https://arxiv.org/abs/2608.18028v1)

**作者**：Simon Weber, Mateo de Mayo, Je Hyeong Hong 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-18

### 📄 论文摘要

Initialization-free bundle adjustment (InitFree BA) aims to recover camera poses and scene structure directly from image observations, avoiding the geometric initialization stages of conventional structure-from-motion pipelines. Recent methods based on Object-Space Error (OSE) formulations and Variable Projection (VarPro) show encouraging optimization behavior from random camera configurations. However, existing evaluations primarily measure optimization success, leaving unclear whether a low OSE objective yields a valid metric 3D reconstruction. We revisit InitFree BA experimentally through a unified evaluation framework combining a C++ implementation of existing OSE formulations with a Blender-based dataset generator providing exact ground truth and controlled camera configurations and observation densities. Our experiments reveal a previously overlooked optimization--reconstruction gap: projective solutions with similarly low OSE values can lead to substantially different Euclidean reconstructions after metric upgrade. We identify initialization priors, landmark observation density, and metric-upgrade stability as key factors governing reconstruction success. Overall, our results suggest that the main challenge of InitFree BA is not merely minimizing OSE objectives, but obtaining projective reconstructions that admit reliable metric upgrade. We believe that the proposed benchmark, implementation, and analysis establish stronger experimental foundations for future research on initialization-free bundle adjustment, a problem largely unexplored within the computer vision community. Project page is available at https://github.com/simonwebertum/InitFreeBA.git.

### 🤖 AI 总结

**一句话总结**：Initialization-free bundle adjustment (InitFree BA) aims to recover camera poses and scene structure directly from image observations, avoiding the geometric initialization stages of conventional stru...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Initialization-Free, Bundle, Adjustment, Revisited, Controlled, Experimental, Study, InitFree

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18028v1) | [下载PDF](https://arxiv.org/pdf/2608.18028v1.pdf)

---

## [18. Memory Tree Guided Key Frame Querying for Efficient 3D Question Answering](https://arxiv.org/abs/2608.18009v1)

**作者**：Hsiang-Wei Huang, Fu-Chen Chen, Li-Wu Tsao 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-18

### 📄 论文摘要

Answering questions accurately and efficiently in embodied scenarios presents significant challenges due to limited computational and memory resources for Vision Language Model (VLM) inference. Existing methods adopt visual search key frame retrieval method to select critical question-related key frames for VLM input. However, visual search methods are inefficient because they require visual search among thousands of video frames for each individual user query. In this work, we propose a memory tree guided key frame selection paradigm for efficient 3D question answering in embodied scenarios. Our method leverages a compact and reusable 3D scene representation, termed MemTree3D, which supports real-time online construction leveraging camera 6-DoF poses. MemTree3D captures multi-level 3D scene information, enabling a Large Language Model to efficiently query and retrieve question-relevant key frames through our scoring-based frame selection without reprocessing the entire video stream. On OpenEQA, our method improves the LLM-Match of GPT-4o by 17.4%, LLaVA-OneVision-7B by 5.8%, outperforms existing visual search methods. Our code is available at https://github.com/hsiangwei0903/MemTree3D

### 🤖 AI 总结

**一句话总结**：Answering questions accurately and efficiently in embodied scenarios presents significant challenges due to limited computational and memory resources for Vision Language Model (VLM) inference. Existi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Memory, Tree, Guided, Key, Frame, Querying, Efficient

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18009v1) | [下载PDF](https://arxiv.org/pdf/2608.18009v1.pdf)

---

## [19. GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation](https://arxiv.org/abs/2608.17988v1)

**作者**：Ming Qian, Zijian Wang, Minchao Sun 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-18

### 📄 论文摘要

Many scalable latent 3D generators operate on structured tensors, whereas pre-optimized 3D Gaussian Splatting (3DGS) reconstructions are unordered, spatially irregular, and vary widely in primitive count. We present GS-Voxel, a fitting-free structured latent framework, and evaluate it for large-scale aerial 3D Gaussian scene generation. GS-Voxel deterministically converts a compatible pre-optimized 3DGS reconstruction into sparse active voxels without additional per-scene optimization, retaining the sub-voxel positions and rendering attributes of the selected primitives. A GS-specific factorized VAE then separately encodes voxel geometry and local Gaussian attributes into sparse 3D latents whose size grows with the number of occupied voxels rather than being limited by a fixed scene-wide primitive count. We train image-conditioned flow models in the GS-Voxel latent space to generate aerial 3DGS scenes. A key application enabled by GS-Voxel is large-area scene generation: overlap-aware tiled inference extends synthesis beyond a single training crop conditioned on satellite-view images. Our results show that GS-Voxel provides structured latents for pre-optimized aerial 3DGS reconstructions, with latent capacity that grows with the number of occupied voxels.

### 🤖 AI 总结

**一句话总结**：Many scalable latent 3D generators operate on structured tensors, whereas pre-optimized 3D Gaussian Splatting (3DGS) reconstructions are unordered, spatially irregular, and vary widely in primitive co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GS-Voxel, Fitting-Free, Structured, Latents, Large-Scale, 3DGS, Generation, Many

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17988v1) | [下载PDF](https://arxiv.org/pdf/2608.17988v1.pdf)

---

## [20. Dual Co-Train: Cross-Dataset Ultrasound Tongue Segmentation Under Extreme Data Scarcity](https://arxiv.org/abs/2608.17983v1)

**作者**：Alisher Myrgyyassov, Zhen Song, Bruce Xiao Wang 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-18

### 📄 论文摘要

Ultrasound tongue contour segmentation remains challenging under cross-dataset domain shift, where limited annotations, probe variability, and acquisition noise often degrade model generalization. We present a source-free domain adaptation framework for robust ultrasound tongue segmentation built on a lightweight UltraUNet backbone. Starting from a checkpoint pretrained on only five labeled source images, simulating an underfitted constrained source model, the proposed method adapts to a fully-unlabeled target domain by iteratively refining pseudo-labels, filtering unreliable masks with a contour-based quality-control module, and generating target-style synthetic image-mask pairs through a segmentation-guided conditional GAN. The student model is then trained on a mixture of clean pseudo-labeled target images, noisy pseudo-labels with consistency regularization, and synthetic samples, enabling closed-loop adaptation without access to source data. We evaluate the method on 12 source-target transfer pairs across eight ultrasound tongue imaging datasets, and conduct source-size scaling experiments and ablation studies. Across all comparisons, the proposed framework improves segmentation overlap and contour accuracy over the baselines, including supervised ones. These results suggest that task-specific pseudo-label refinement and synthetic target-style augmentation can substantially improve source-free adaptation for ultrasound tongue imaging.

### 🤖 AI 总结

**一句话总结**：Ultrasound tongue contour segmentation remains challenging under cross-dataset domain shift, where limited annotations, probe variability, and acquisition noise often degrade model generalization. We ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Dual, Co-Train, Cross-Dataset, Ultrasound, Tongue, Segmentation, Under, Extreme

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17983v1) | [下载PDF](https://arxiv.org/pdf/2608.17983v1.pdf)

---

## [21. LinCa: Accelerating Diffusion Models via Learnable Decomposed Feature Caching](https://arxiv.org/abs/2608.17973v1)

**作者**：Jinshan Liu, Haoran Qin, Xiaobing Tu 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-18

### 📄 论文摘要

Diffusion models have achieved remarkable success in image and video generation, yet the high computational cost of iterative sampling remains a critical bottleneck for practical deployment. Feature caching has emerged as a promising acceleration paradigm by reusing or predicting intermediate features across timesteps. However, existing training-free methods apply uniform prediction strategies that cannot adapt to the heterogeneous feature dynamics, causing significant quality degradation under high acceleration ratios. We propose LinCa, a feature caching framework based on learnable invertible networks. LinCa decomposes cached features into sub-components with distinct continuity properties via a lightweight invertible network and applies differentiated prediction orders matched to each component. The strict invertibility guarantees lossless reconstruction back to the original feature space, forming a unified Decompose-Predict-Reconstruct pipeline. By training separate predictors for different models and timestep segments, LinCa adapts to heterogeneous feature dynamics. Experiments on FLUX, Qwen-Image, and HunyuanVideo demonstrate that LinCa, with less than 0.2% additional parameters, significantly outperforms existing methods and maintains near-lossless quality at 5-7x speedup. Code: https://github.com/QHR69/LinCa

### 🤖 AI 总结

**一句话总结**：Diffusion models have achieved remarkable success in image and video generation, yet the high computational cost of iterative sampling remains a critical bottleneck for practical deployment. Feature c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, LinCa, Accelerating, Models, via, Learnable, Decomposed, Feature

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17973v1) | [下载PDF](https://arxiv.org/pdf/2608.17973v1.pdf)

---

## [22. Cross-Domain Generalization in Machine Unlearning via Label-Conditioned Energy Magnitude Regularization](https://arxiv.org/abs/2608.17942v1)

**作者**：Syed Ali Ahmed, Syed Bilal Ahsan, Muhammad Zaigham Zaheer  
**分类**：cs.CV  
**发布时间**：2026-08-18

### 📄 论文摘要

Machine unlearning removes the influence of specific data from a trained model. However, most methods treat the forgotten concept as isolated. In this paper, we study what happens to the rest of the model when a class is forgotten, using a label-conditioned energy-based model (EBM) that assigns per-class energies, making the effect directly observable. We forget a class by raising the energy of its image-label pairs, training with a forget term, a retain anchor to the pretrained model, a global margin, and an energy regularizer that stops the energy magnitudes from growing without limit. A propagation term applies the same forget signal to retain samples, weighted by each sample's DINOv2 similarity to the forget class, so forgetting reaches images that resemble it and leaves the rest untouched. We evaluate on two benchmark datasets: 1) On a subset of DomainNet across four visual domains, we forget tiger, lion, and scissors one at a time. Forgetting a class in the sketch domain also erases it from real, clipart, and painting, with forgetting error reaching 98% and 99% for lion and scissors, and the effect carrying over to the most similar class. 2) On CIFAR-10, we turn off the propagation term and forget each of the ten classes on its own. Forgetting is complete (100%), while the other nine classes retain 98.5% of their pre-unlearning accuracy on average.

### 🤖 AI 总结

**一句话总结**：Machine unlearning removes the influence of specific data from a trained model. However, most methods treat the forgotten concept as isolated. In this paper, we study what happens to the rest of the m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Cross-Domain, Generalization, Machine, Unlearning, via, Label-Conditioned, Energy, Magnitude

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17942v1) | [下载PDF](https://arxiv.org/pdf/2608.17942v1.pdf)

---

## cs.LG

## [23. Optimize Your Sampling: Tuned Diffusion Sampling with Bayesian Optimization](https://arxiv.org/abs/2608.18040v1)

**作者**：Travis Zhang, Christian Belardi, Justin Lovelace 等 7 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-08-18

### 📄 论文摘要

Sampling from a diffusion model typically requires many forward passes through a large neural network, making generation computationally expensive. While much work has focused on efficient solvers and samplers, comparatively little attention has been paid to selecting the sampling timesteps themselves. A recent line of work optimizes theoretically derived surrogates for sample quality rather than the quality metric itself. We propose Optimizing Your Sampling (OYS), which instead treats timestep selection as a black-box optimization problem, optimizing the target metric directly with Bayesian optimization. OYS outperforms both the default schedules and those of Align Your Steps on text-to-image generation, and improves over the default schedules on inpainting and other image tasks, in both quantitative and human evaluations. OYS requires no additional training, is applicable even to distilled models, and improves both simple and sophisticated samplers such as Euler and DPM-Solver++. A 5-step OYS schedule retains 89%-94% of the quality of a 50-step schedule while reducing inference cost by 10x.

### 🤖 AI 总结

**一句话总结**：Sampling from a diffusion model typically requires many forward passes through a large neural network, making generation computationally expensive. While much work has focused on efficient solvers and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Optimize, Sampling, Tuned, Bayesian, Optimization, model, typically

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18040v1) | [下载PDF](https://arxiv.org/pdf/2608.18040v1.pdf)

---

## [24. Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents](https://arxiv.org/abs/2608.18008v1)

**作者**：Christophe D. Hounwanou, John Emeka Eze, Yaé U. Gaba  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-18

### 📄 论文摘要

Combining large language models with reinforcement learning is increasingly explored, yet the theoretical status of LLM-derived reward signals is often left implicit. We formalize the hybrid LLM-planner and RL-controller architecture as a Goal-Augmented Markov Decision Process and show that when the LLM per-state progress score is used as a bounded potential function, the resulting shaping term preserves the optimal policy set even when the LLM scores are inaccurate. This guarantee is stronger than what general LLM-as-reward approaches provide. We verify the result numerically on a small MDP under four potential configurations, including an adversarial one scaled to twenty times the base reward magnitude.

### 🤖 AI 总结

**一句话总结**：Combining large language models with reinforcement learning is increasingly explored, yet the theoretical status of LLM-derived reward signals is often left implicit. We formalize the hybrid LLM-plann...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, RL, Policy-Invariant, Reward, Shaping, Feedback, Framework, Hybrid

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18008v1) | [下载PDF](https://arxiv.org/pdf/2608.18008v1.pdf)

---

## [25. Composing Flow-Matching Energies with Known Physics: Generation, OOD Detection, and Inversion on PDE Fields](https://arxiv.org/abs/2608.18004v1)

**作者**：Yixuan Sun, Anirban Samaddar, Sandeep Madireddy  
**分类**：cs.LG, physics.comp-ph  
**发布时间**：2026-08-18

### 📄 论文摘要

Probabilistic modeling of physical fields benefits from both a data-driven prior and known physical structure such as the governing equations. Energy-based models (EBMs) are a natural fit since energies compose additively, which enables augmenting physics information during inference. However, EBMs have been difficult to train and sample from due to the intractable partition function. We show in this work that flow matching models with a potential-induced velocity yield an explicit scalar energy at all transport times, whose gradient is exactly the converted learned score and which recovers the marginal negative log-density at the population optimum. The time-dependent energy functions are obtained purely from the matching regression objective on an independent linear Gaussian interpolation, without a variational form or additional MCMC steps, and the sampling retains the flow ODE. Access to the energy function from a trained model serves three roles: energy-corrected data generation, energy as a scoring function for out-of-distribution (OOD) detection, and energy compositional posterior sampling for inverse problems. In particular, we show the explicit energy permits general MCMC samplers in the predictor-corrector sampling framework, reducing PDE residual and spectral distance compared to the flow ODE baseline. Furthermore, we demonstrate utilizing the data energy and physics-based energy (e.g., PDE residuals) as complementary mechanisms to improve detection accuracy for OOD tasks. In addition, we explore the connection to MCMC-based inference for inverse problems by composing the energy with a quadratic observational likelihood that yields a posterior energy, used as an explicitly chosen family of inference-time targets.

### 🤖 AI 总结

**一句话总结**：Probabilistic modeling of physical fields benefits from both a data-driven prior and known physical structure such as the governing equations. Energy-based models (EBMs) are a natural fit since energi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Composing, Flow-Matching, Energies, Known, Physics, Generation, OOD, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.18004v1) | [下载PDF](https://arxiv.org/pdf/2608.18004v1.pdf)

---

## [26. Recirculation](https://arxiv.org/abs/2608.17981v1)

**作者**：Michael C. Mozer, Shoaib Ahmed Siddiqui, Danny Sawyer 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-18

### 📄 论文摘要

We describe an inference-time architectural enhancement for off-the-shelf foundation models that markedly reduces perplexity and boosts accuracy across generation and reasoning tasks. Our approach incurs essentially no additional latency during generation, though it requires serial processing in the prefill phase. Motivated by the fundamental limitation that state updates in feedforward transformers are bounded by model depth, our technique, recirculation, introduces a specific form of recurrence that allows the model to act as a dynamical system and track belief states. We distinguish this technique from chain-of-thought computation---which is better reserved for complex inferences rather than basic state tracking---as well as from popular depth-recurrence techniques (looping) and the costly training of recurrent transformers. We also propose and evaluate an adaptive variant of recirculation which requires only light tuning of hyperparameters while freezing the original model weights. Relative to the off-the-shelf baseline, adaptive recirculation achieves remarkable gains on the Gemma3 family, including a 23% reduction in perplexity on a suite of datasets, a 21% increase in accuracy on GSM8k, and reliable improvements in accuracy on other downstream tasks. Our training-free approach succeeds by leveraging the model itself to inform architectural modifications, suggesting a route to architectural evolution guided by a trained network's properties rather than forced, arbitrary design choices.

### 🤖 AI 总结

**一句话总结**：We describe an inference-time architectural enhancement for off-the-shelf foundation models that markedly reduces perplexity and boosts accuracy across generation and reasoning tasks. Our approach inc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, an, Recirculation, describe, inference-time, architectural, enhancement, off-the-shelf

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17981v1) | [下载PDF](https://arxiv.org/pdf/2608.17981v1.pdf)

---

## [27. Evaluating and improving crop-yield forecasting methods during extreme drought](https://arxiv.org/abs/2608.17971v1)

**作者**：Shrey Gupta, Yi Ming, George Mohler  
**分类**：cs.LG  
**发布时间**：2026-08-18

### 📄 论文摘要

The impact of climate variability on food production has led to the creation of various forecasting models that uses machine learning (ML), numerical weather predictors (NWP) or a hybrid of ML-NWP models to identify structural and physical relationships between meteorological drivers and crop growth, in order to predict crop yield. Droughts, for example the 2012 Midwestern US (Corn Belt) drought, are extreme events that affect crop production and test the limits of these forecasting models. Using 16 meteorological drivers as predictors, we compare ML (non-deep learning) and deep learning forecasting models to predict the county-level corn yield for the extreme drought year, 2012. This forecasting problem is characterized by a dissimilarity between the feature distributions of the training and test data, where the meteorological conditions of the extreme drought year fall outside the range of historically observed values. Additionally, the dataset consists of spatial and temporal irregularities where counties with missing yields introduce spatial sparsity and the use of only a subset of daily values per year introduce temporal sparsity. To overcome this, we use sample weighting and feature selection as modifications to improve our forecasting models. These modifications lead to an improvement for ML models; however, the deep learning model VITA shows little to no improvement. While VITA outperforms the ML models with or without modifications, our current study sheds light on the effect of dissimilarity between train and test feature distributions on forecasting models, compares deep learning versus non-deep learning models, and introduces modifications that are effective for non-deep learning models.

### 🤖 AI 总结

**一句话总结**：The impact of climate variability on food production has led to the creation of various forecasting models that uses machine learning (ML), numerical weather predictors (NWP) or a hybrid of ML-NWP mod...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Evaluating, improving, crop-yield, forecasting, methods, during, extreme, drought

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17971v1) | [下载PDF](https://arxiv.org/pdf/2608.17971v1.pdf)

---

## [28. Too Sure to Be Safe: Model Calibration for Reliable Log Anomaly Detection](https://arxiv.org/abs/2608.17965v1)

**作者**：Bin Li, Dongdong Wang, Siyang Lu  
**分类**：cs.LG, cs.AI, cs.SE  
**发布时间**：2026-08-18

### 📄 论文摘要

Online log anomaly detection is critical for maintaining the reliability of large-scale computing systems. Although recent language model-based log anomaly detectors achieve strong detection performance, their confidence estimates remain poorly calibrated. We show that these detectors frequently assign excessive confidence to incorrect predictions, particularly for anomalous logs under severe class imbalance. Moreover, confidence on erroneous predictions remains persistently high even when conventional calibration metrics indicate good calibration, creating a critical reliability gap for operational monitoring systems. To address this issue, we propose Log Reconstruction and Distance (LoRD), a lightweight post-hoc calibration framework for reliable log anomaly detection. LoRD learns prediction-route-specific reliability models from latent representations of correctly classified validation samples and estimates prediction reliability through route-wise reconstruction distances. Based on the estimated reliability, LoRD selectively recalibrates high-risk predictions to suppress overconfident errors while preserving reliable predictions. Extensive experiments on four large-scale log benchmark datasets and multiple language model-based detectors demonstrate that LoRD consistently improves confidence reliability and substantially reduces overconfident anomaly-related errors without sacrificing anomaly detection performance.

### 🤖 AI 总结

**一句话总结**：Online log anomaly detection is critical for maintaining the reliability of large-scale computing systems. Although recent language model-based log anomaly detectors achieve strong detection performan...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Be, Too, Sure, Safe, Model, Calibration, Reliable, Log

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17965v1) | [下载PDF](https://arxiv.org/pdf/2608.17965v1.pdf)

---

## [29. An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models](https://arxiv.org/abs/2608.17956v1)

**作者**：Javier Aguilar Martín  
**分类**：cs.LG, cs.AI, eess.SY  
**发布时间**：2026-08-18

### 📄 论文摘要

In the Code World Model paradigm an LLM synthesizes an executable world model that a classical planner searches, and the model is accepted when it reproduces sampled transitions. We ask what that acceptance certifies in continuous control. We define the pipeline's danger as an expected risk and isolate its exact factor: the probability that N i.i.d. gate rollouts all miss a critical event of probability r is exactly (1-r)^N; an independent acceptance sample adds its budget to the exponent. On three hybrid instruments the accepted mode-blind model is exploited: the planner is pinned at the mode boundary at a regret of nearly the whole attainable return. We prove a localization budget, valid at boundary points: models with Lipschitz constant at most L differing by eta at a point disagree above tolerance eps on a region of volume at least kappa((eta-eps)/L)^(d+m); the discontinuous reset modes studied pay no such budget. With real LLM synthesis, GPT-5.x repairs an omitted 1D clamp in 105 of 111 mode-containing draws -- every attempt exact on 50 of 56 instrument-stream blocks (95% CI [0.781, 0.960]). On 2D regions no artifact recovers the rule (0/156); eight targeted interventions leave the failure in place, and positive controls locate it: a located rule is not induced, while given form and location the constants follow exactly. A version-space certificate proves identification is class-relative: at the widest dose the declared fit succeeds in 20/20 blocks and every sample-consistent circle is within tolerance in 18/20. We prove a class of entry rules exactly consistent with every sample yet harmless at play, so identifiability is a measurable property of the instrument. Re-scoring all 1034 artifacts on independent samples confirms acceptance certifies sample consistency and no more: where the gate is provably informative it covers about two percent of the exploited planner's queries.

### 🤖 AI 总结

**一句话总结**：In the Code World Model paradigm an LLM synthesizes an executable world model that a classical planner searches, and the model is accepted when it reproduces sampled transitions. We ask what that acce...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Omitted, Mode, Rare, Rule, Sampling-Verification, Danger, Law

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17956v1) | [下载PDF](https://arxiv.org/pdf/2608.17956v1.pdf)

---

## [30. SIGMA: SHAP-Guided Implicit-Trajectory Generation for Metadata-Free LLM-Based AutoFE](https://arxiv.org/abs/2608.17948v1)

**作者**：Xuan Zheng, Kento Uchida, Shinichi Shirakawa  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-18

### 📄 论文摘要

Recent research has leveraged Large Language Models (LLMs) to enhance Automated Feature Engineering (AutoFE) through semantic descriptions and trajectory-based prompting. However, there exist two challenges that limit their applicability and scalability in long-horizon optimization: (1) semantic metadata is unavailable in many practical settings, and (2) trajectory accumulation increases the risk of exceeding the context window, while without it, the generation process can become unstable, leading to becoming stuck in the local optima and a high duplicate rate of generated features. To this end, we propose a SHAP-enhanced Implicit-trajectory Generation for Metadata-free AutoFE (SIGMA), a scalable constant-context optimization framework. SIGMA leverages SHAP values to provide task-aware signals for guiding group feature generation instead of semantic information. In addition, we adopt an EXposed-feature Implicit Trajectory (EXIT) approach, where the exposed features in the prompt implicitly represent the trajectory. Empirical results demonstrate that SIGMA achieves performance comparable to the state-of-the-art (SOTA) LLM baselines with a nearly constant prompt length. Notably, EXIT significantly reduces the duplicate ratio of generated features from 37.2% to 6.8%. At the same time, SIGMA matches traditional SOTA performance with only 5.4 features on average, demonstrating substantial efficiency gains in feature utilization.

### 🤖 AI 总结

**一句话总结**：Recent research has leveraged Large Language Models (LLMs) to enhance Automated Feature Engineering (AutoFE) through semantic descriptions and trajectory-based prompting. However, there exist two chal...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SIGMA, SHAP-Guided, Implicit-Trajectory, Generation, Metadata-Free, LLM-Based, AutoFE, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.17948v1) | [下载PDF](https://arxiv.org/pdf/2608.17948v1.pdf)

---

