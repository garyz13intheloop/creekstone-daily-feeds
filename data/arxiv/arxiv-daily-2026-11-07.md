# arXiv AI 论文日报 | 2026-11-07

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (12 篇)
- [cs.CV](#csCV) (7 篇)
- [cs.AI](#csAI) (8 篇)
- [cs.CL](#csCL) (3 篇)

---

## cs.AI

## [1. SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization](https://arxiv.org/abs/2611.08483v1)

**作者**：Qile Jiang, George Em Karniadakis  
**分类**：cs.AI, cs.NE  
**发布时间**：2026-11-05

### 📄 论文摘要

LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow because the LLM generates a long textual chain of thought for each round and must repeat this generation many times to maintain population diversity. We present SwarmEvolve, a framework in which hundreds of low-cost agents per round work in swarms, reason in latent space without decoding to text, and share information by passing KV caches. Each swarm studies the problem from a different angle. A novelty filter keeps the most distinct agent ideas by directly measuring the distances between the agents' hidden state vectors. Crossover of ideas happens naturally in latent space, as a summarizer agent receives the combined KV caches of all swarm members. On 21 problems in mathematical discovery and scientific computing, SwarmEvolve gets the highest average score and needs a median of only 3 to 8 minutes to reach the best scores that other state-of-the-art frameworks reach in 60 minutes. On several problems, SwarmEvolve with Qwen3 8B improves on the solutions that AlphaEvolve first found with frontier LLMs. Our work shows that agent swarms that communicate in latent space offer a fast, low-cost approach to program search for scientific problems.

### 🤖 AI 总结

**一句话总结**：LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SwarmEvolve, Latent, Swarms, Evolutionary, Discovery, Optimization, LLM-guided

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08483v1) | [下载PDF](https://arxiv.org/pdf/2611.08483v1.pdf)

---

## [2. Scientist World: Grow a Research World for AI-Scientists](https://arxiv.org/abs/2611.08478v1)

**作者**：Taiming Lu, Sachin Konan, Zhuang Liu  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-11-05

### 📄 论文摘要

AI-Scientists arrived, but a world for them to grow in did not. Human scientists take theirs for granted $-$ centuries of open problems and shared ideas, waiting in the scientific literature. To AI-Scientists, that world is readable but not runnable, so we build Scientist World for them: every research paper becomes an executable environment. Our autonomous pipeline extracts each paper's open-ended research question and reproduces its proposed method as the baseline; an AI-Scientist entering the environment is evaluated against what the human authors achieved. We release the first 1,000 verified environments. With the world as an evaluation, we found that frontier AI-Scientists can already surpass the human researchers 74% of the time. As a record of how AI does science, it contains 6,400 hours of research traces, with every idea, experiment, failure, and success. As a training ground, we are able to raise (+158%) a small model to match frontier models in research ideation. At last, AI-Scientists' own world has arrived, grown from and growing with science itself.

### 🤖 AI 总结

**一句话总结**：AI-Scientists arrived, but a world for them to grow in did not. Human scientists take theirs for granted $-$ centuries of open problems and shared ideas, waiting in the scientific literature. To AI-Sc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Scientist, World, Grow, Research, AI-Scientists, arrived, but, them

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08478v1) | [下载PDF](https://arxiv.org/pdf/2611.08478v1.pdf)

---

## [3. ReproBridge: Building Reproducibility into ML Research Artifacts](https://arxiv.org/abs/2611.08452v1)

**作者**：Yubo Wang, Rui Meng, Jaehyun Nam 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-05

### 📄 论文摘要

Reproducing machine learning experiments requires reconstructing procedures from information scattered across papers, released code, and supporting artifacts. For coding agents, reproduction success can therefore depend on their ability to fill in missing details, rather than on the released artifacts alone. We ask whether preserving recovered procedures and decisions improves subsequent independent reproduction. We define a standardized artifact design comprising a refined codebase, environment setup, experiment launchers, and a reproduction guide, and introduce ReproBridge, an agent workflow for constructing these refined reproducible artifacts. ReproBridge-Bench provides 1,029 tasks from 387 experiments across 36 papers, anchored by five human-verified reference scores per task. Agents attempt tasks in fresh sessions with raw code or refined artifacts; a separate Auditor checks execution evidence. Across four evaluated models, refined artifacts raise mean reproduction success from 76.4% to 92.6% and reduce downstream API spending by 19.7% on average. The cross-model success-rate spread narrows from 21.6 to 3.9 percentage points, with all four models achieving mean success rates above 90%. Removing any component reduces success in the ablation study, with the largest losses from code and environment removal. These results suggest that preserving execution knowledge helps even models with lower raw-code success reproduce experiments more reliably and at lower API cost.

### 🤖 AI 总结

**一句话总结**：Reproducing machine learning experiments requires reconstructing procedures from information scattered across papers, released code, and supporting artifacts. For coding agents, reproduction success c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ML, ReproBridge, Building, Reproducibility, Research, Artifacts, Reproducing, machine

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08452v1) | [下载PDF](https://arxiv.org/pdf/2611.08452v1.pdf)

---

## [4. The Power of Meta Access in the Software of the Future --- Demonstrated on LLM Chat UIs and Chat AI](https://arxiv.org/abs/2611.08428v1)

**作者**：Julian Kunkel, Ali Doosthosseini  
**分类**：cs.AI  
**发布时间**：2026-11-05

### 📄 论文摘要

Chat remains the default surface for many large language model (LLM) tasks, even as agentic tools such as OpenCode excel at coding and automation. Yet the model sees the current dialogue but not the workspace around it. We explore meta access---giving the assistant a structured, permissioned view of the interface itself and propose a ladder of levels: feature tutoring; metadata, settings, and preference access; retrieval over summaries and messages, confirmed mutation, and full orchestration. Meta access can turn a chat client from many screens into one entry point for finding, navigating, organising, and operating it, while raising risks around grounding, privacy, prompt injection, and trust. General-purpose agentic harnesses are runtimes; because they can change their own settings, meta access becomes reflexive and needs a separate control-plane boundary. We ground this in the Meta Chat prototype of the Chat AI client. It builds bounded context from, e.g., summaries, settings, and relevant messages; links references to conversations, topics, and personas; supports confirmed, reversible changes; offers a browsable tutorial library; and recommends personas as user-started conversations. By exposing application state in structured form, meta access can extend screen readers from widget descriptions to semantic workspace operations. Meta access thus turns chat from a window onto one conversation into a control layer for the whole workspace, extending chat toward agentic capability without surrendering user control. As assistants become embedded in IDEs, dashboards, office suites, and operating systems, AI-era interfaces should expose a structured, permissioned model of their state and capabilities, ideally by opening their existing metamodels through a debugger-like interface.

### 🤖 AI 总结

**一句话总结**：Chat remains the default surface for many large language model (LLM) tasks, even as agentic tools such as OpenCode excel at coding and automation. Yet the model sees the current dialogue but not the w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Power, Meta, Access, Software, Future, Demonstrated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08428v1) | [下载PDF](https://arxiv.org/pdf/2611.08428v1.pdf)

---

## [5. Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks](https://arxiv.org/abs/2611.08417v1)

**作者**：E. Kelly Buchanan, Crystal Zhou, Scott W. Linderman 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-05

### 📄 论文摘要

Coding agents are among the most economically consequential deployments of LLMs to date, making reliable evaluation increasingly important. Yet even benchmarks that are carefully validated at release can become stale. As models improve, they can discover valid solutions that existing verifiers reject, while changes to evaluation infrastructure can invalidate assumptions embedded in tasks and tests. We call the resulting accumulation of defects benchmark maintenance debt: a growing gap between benchmark scores and the capabilities they are intended to measure. We introduce a continuous-validation workflow for agentic benchmarks that combines community reports, task artifacts, agent traces, automated oracle checks, and human-gated repairs. We apply this workflow to Terminal-Bench 2.0, a benchmark that underwent extensive human and LM-assisted review and red-teaming before release. Our audit identifies issues in roughly 30% of the benchmark, and we release the resulting repairs as Terminal-Bench 2.1. These repairs change evaluation results: accuracy increased by over 10 percentage points and leaderboard positions move by up to three ranks, even as the overall ranking remains highly correlated (Spearman rho = 0.958).   We evaluate how resource allocation shapes benchmark conclusions. We show that fixed wall-clock can materially change agent performance: For example, extending the time limit closes a 20pp harness gap on GPT 5.4 and shrinks a 30 pp gap on GPT 5.4 mini to 5 pp. Benchmark maintenance is therefore not only about repairing task artifacts: resource budgets are part of the measurement specification and must be validated alongside the tasks themselves.   More broadly, benchmark maintenance debt is not just accumulated implementation bugs: our results show that as models improve, both evaluation assumptions and resource settings may need to be revalidated.

### 🤖 AI 总结

**一句话总结**：Coding agents are among the most economically consequential deployments of LLMs to date, making reliable evaluation increasingly important. Yet even benchmarks that are carefully validated at release ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Agent, Benchmarks, Software, Terminal-Bench, Case, Continuous, Coding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08417v1) | [下载PDF](https://arxiv.org/pdf/2611.08417v1.pdf)

---

## [6. The Gold Rush in AI4Math, II: What are signatures of AI-assisted Proofs?](https://arxiv.org/abs/2611.08412v1)

**作者**：Yuanchuan Guo, Jiashun Jin, Zheng Tracy Ke 等 4 位作者  
**分类**：cs.AI, stat.AP  
**发布时间**：2026-11-05

### 📄 论文摘要

The growing use of AI in mathematics raises a question: can we detect AI involvement in proofs, separately from AI assistance with writing? Historical arXiv papers, recent papers disclosing substantive AI use, and manuscripts released by OpenAI provide a rich empirical basis for studying this question. However, several challenges remain: lack of matched case-control pairs; potential incompleteness of disclosure; and lack of ready-to-use features designed to capture signals of AI involvement in proofs.   To address these challenges, we construct five cohorts comprising 8,281 papers by combining existing manuscripts with those we produced using generative AI. These cohorts span different levels of AI involvement and include matched pairs of papers addressing the same research problems. We then introduce ProofTrace, a framework that represents each paper as a graph of immediate proof support (GIPS) and extracts interpretable features of mathematical organization.   Our study yields three discoveries. First, principal-component projections of our features reveal a qualitative gradient of AI involvement, where AI-reworded papers remain close to human papers, the two AI-generated cohorts depart in broadly shared directions, and papers disclosing substantive AI use occupy intermediate positions which shifts toward AI-generated cohorts over time. Second, we identify recurring signatures of AI-generated proofs, such as fewer externally cited results, greater reliance on intermediate conclusions, and altered graph connectivity; many of these signatures persist under controls for research field, manuscript length, or graph size. Finally, in a separate detection experiment, ProofTrace distinguishes human-written papers from those disclosing substantive AI use. Its performance remains stable under AI rewording, whereas the performance of state-of-the-art text-based detectors declines sharply.

### 🤖 AI 总结

**一句话总结**：The growing use of AI in mathematics raises a question: can we detect AI involvement in proofs, separately from AI assistance with writing? Historical arXiv papers, recent papers disclosing substantiv...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：II, of, Gold, Rush, AI4Math, What, signatures, AI-assisted

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08412v1) | [下载PDF](https://arxiv.org/pdf/2611.08412v1.pdf)

---

## [7. Learning a patient world model for health system simulation in intensive care](https://arxiv.org/abs/2611.08392v1)

**作者**：Yingtai Li, Ruoyan Wang, Yu Li 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-05

### 📄 论文摘要

Designing healthcare strategies requires anticipating their clinical and operational consequences before implementation, a task that often relies on health system simulation. Such a simulation necessitates modeling how patient states evolve and generate care demands. However, conventional approaches typically tailor compact state transitions to a single policy question and omit history-dependent dynamics, thus requiring the redefinition of states and transitions when there is a new question that entails different clinical information. We propose to learn a patient world model from longitudinal EHRs using a neural network to provide a shared clinical representation of patient trajectories that can serve simulation questions across scenarios. Taking ICU operations as an example, we train the model on MIMIC-IV, freeze it, and couple its time-queryable predictions to shared ICU calendars, resources, and queues via scenario-specific mappings, so that one model renders admission demand, care tasks, and discharge proposals across simulations evaluating ICU bed capacity, care dispatch, and post-ICU transfer capacity. Experiments show that our model matches Markov and semi-Markov comparators in aggregate occupancy and directional responses to capacity and dispatch policies. It also reproduces policy gains from replayed observed trajectories. For patients entering the same support state from different prior trajectories, the learned representation captures a 24-h recovery difference (-6.4 predicted versus -6.7 observed percentage points), a contrast missed by compact state models, which propagates into distinct simulated care demand, queue burden, and bed use. These results indicate that a learned world model of patient dynamics has the potential to replace question-specific state models, allowing new care policies to be evaluated by reconfiguring the scenario without model rebuilding.

### 🤖 AI 总结

**一句话总结**：Designing healthcare strategies requires anticipating their clinical and operational consequences before implementation, a task that often relies on health system simulation. Such a simulation necessi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, patient, world, model, health, system, simulation, intensive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08392v1) | [下载PDF](https://arxiv.org/pdf/2611.08392v1.pdf)

---

## [8. NPCBench: A Clinical Apprenticeship Benchmark for Multimodal Care-Pathway Reasoning in Nasopharyngeal Carcinoma](https://arxiv.org/abs/2611.08369v1)

**作者**：Pengkai Wang, Wei-Wei Zhang, Yan Li 等 16 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-05

### 📄 论文摘要

Current medical benchmarks typically break down clinical competence into isolated factual questions, single-image tasks, or static case vignettes. These tests score individual answers, but reveal less about whether a model can integrate subspecialty knowledge with multimodal evidence and track a patient's condition throughout a course of care. To close this gap, we introduce NPCBench, a clinical apprenticeship benchmark for nasopharyngeal carcinoma (NPC). NPCBench mirrors specialist training, from guideline and foundational knowledge to case planning, longitudinal review, CarePath integration, and open-ended consultation. It contains 4,777 component and consultation items and a 100-patient CarePath cohort with 417 scored diagnostic and care tasks. The episode-level evaluation tests whether diagnostic and care answers are jointly correct within a care pathway. By linking stepwise tasks to patient-level care trajectories, NPCBench evaluates whether models ground decisions in visual evidence, interpret changes in patient state, and meet clinical requirements in consultation. Across 30 evaluated models, we observe a composition gap: strong performance on individual tasks does not ensure jointly correct diagnostic and care answers for the same patient. Among 21 multimodal models, strict CarePath success reaches at most 23%. Paired controls and physician calibration further examine evidence grounding, longitudinal revision, and consultation judging. Overall, NPCBench broadens the evaluation of medical artificial intelligence beyond static question-answering paradigms to an apprenticeship-oriented assessment of clinical workflows, thereby offering a testbed for evidence-based and temporally coherent reasoning in oncology care.

### 🤖 AI 总结

**一句话总结**：Current medical benchmarks typically break down clinical competence into isolated factual questions, single-image tasks, or static case vignettes. These tests score individual answers, but reveal less...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：NPCBench, Clinical, Apprenticeship, Benchmark, Multimodal, Care-Pathway, Reasoning, Nasopharyngeal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08369v1) | [下载PDF](https://arxiv.org/pdf/2611.08369v1.pdf)

---

## cs.CL

## [9. Label-Wording Augmentation in a Typed-Decision Encoder: Gains on Unfamiliar Words, Not on Abbreviations or Codes](https://arxiv.org/abs/2611.08439v1)

**作者**：Vladimir Beskorovainyi  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-11-05

### 📄 论文摘要

Typed-decision models score options that the caller supplies at request time, so their accuracy depends on label wording that the model's developer does not control. We compare two releases of a 307M-parameter multilingual cross-encoder, Ru-Jev, trained on thirteen Russian-language tasks; the later release adds an augmentation that presents labels in several surface forms. Holding questions fixed and varying only how eighteen routing labels are worded, we evaluate ten label vocabularies, produced by three separate processes and checked for overlap with the training data, with five candidates per question and, for eight of them, also with eighteen. On held-out vocabularies made of ordinary or borrowed words (English-derived jargon, office slang, department names), the augmented release is more accurate in every setting, by up to 0.24. Eleven of these fourteen gains survive a Holm correction (slang with eighteen candidates and descriptive sentences with five do not), and for jargon on all labels the label-level interval excludes zero in both settings. On abbreviations and opaque codes it gives no usable gain: on abbreviations it is not better, and worse on the clean slice, and on opaque codes both releases stay at or below chance once labels related to training options are removed. In most cells where accuracy rises, the risk-coverage area falls, but with eighteen candidates confident errors rise on jargon and slang. On two datasets neither release saw, accuracy moves by -8.4 and +5.6 points. We also report four evaluation hazards from comparing the two releases.

### 🤖 AI 总结

**一句话总结**：Typed-decision models score options that the caller supplies at request time, so their accuracy depends on label wording that the model's developer does not control. We compare two releases of a 307M-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Label-Wording, Augmentation, Typed-Decision, Encoder, Gains, Unfamiliar, Words, Not

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08439v1) | [下载PDF](https://arxiv.org/pdf/2611.08439v1.pdf)

---

## [10. Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety](https://arxiv.org/abs/2611.08438v1)

**作者**：Fazl Barez, Tung-Yu Wu, Hunar Batra 等 27 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-11-05

### 📄 论文摘要

Neural networks are likely to be among the most consequential artefacts in human history. As these systems become more capable and autonomous, their potential to cause societal harm also grows, making AI safety one of the defining challenges of our time. Yet we continue to build increasingly powerful systems without fully understanding how they work, how they will behave in unfamiliar situations, or how to reliably control them. Mechanistic interpretability offers a path towards understanding these systems by studying their internal representations and computations, with the aim of evaluating, predicting, and controlling behaviour. We survey mechanistic interpretability for AI safety in order to answer the question: Does understanding how models work actually make them safer? We place mechanistic interpretability in the broader context of interpretability research and compare its mechanistic evidence with behavioural evaluation. We introduce the foundations of mechanistic interpretability, including features, polysemanticity, transformer computation, and circuits, and survey methods for feature extraction and analysis, circuit discovery and causal verification, explaining intermediate representations in natural language, learning dynamics, and training-data attribution. Beyond surveying existing methods, we propose a unified framework for evaluating mechanistic interpretability claims and characterise six research orientations by their goals, assumptions, and trade-offs. Finally, we examine how mechanistic understanding can support AI safety, including knowledge editing, steering, and monitoring, and assess its limitations, failure modes, open problems, and relationship to behavioural safety measures. We also release a repository of code notebooks with worked examples that reproduce key findings from surveyed methods, allowing readers to build intuition through hands-on experimentation.

### 🤖 AI 总结

**一句话总结**：Neural networks are likely to be among the most consequential artefacts in human history. As these systems become more capable and autonomous, their potential to cause societal harm also grows, making...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Understanding, Inside, State, Mechanistic, Interpretability, Safety, Neural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08438v1) | [下载PDF](https://arxiv.org/pdf/2611.08438v1.pdf)

---

## [11. MedGraph: Maintaining Patient State with Graph Memory for Long-Term Medical Dialogue](https://arxiv.org/abs/2611.08433v1)

**作者**：Donghua Zhang, Zizheng Wang, Ze Dong 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-11-05

### 📄 论文摘要

LLM-based medical assistants that follow a patient across visits need a memory that keeps the patient's clinical state correct as it changes. We examine the errors of five memory systems on longitudinal medical dialogue and find three recurring causes: the retrieved evidence gives an outdated state, includes another person's health facts, or lacks a safety fact the answer depends on. We present MedGraph, a graph memory built for these three cases. Construction extracts dated facts from each session, attributes each fact to the person it describes, and links medication, diagnosis, and measurement records into chains that keep earlier states. Retrieval ranks the patient's chains as units, reads each chain at the time the question asks about, and adds the original dialogue text; a patient profile lists every recorded safety fact with every question. On MedMemoryBench, MedGraph has the highest overall accuracy with both a GPT and a Qwen backbone, 10.5 and 10.4 points above the strongest of five baselines, with efficient memory construction and answering in the GPT setting.

### 🤖 AI 总结

**一句话总结**：LLM-based medical assistants that follow a patient across visits need a memory that keeps the patient's clinical state correct as it changes. We examine the errors of five memory systems on longitudin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MedGraph, Maintaining, Patient, State, Graph, Memory, Long-Term, Medical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08433v1) | [下载PDF](https://arxiv.org/pdf/2611.08433v1.pdf)

---

## cs.CV

## [12. Do You Miss the Nights We Spent Crafting Figures? Rethinking Teaser and Framework Figures in the Age of Generative AI](https://arxiv.org/abs/2611.08486v1)

**作者**：Xiaoqi Zhao, Youwei Pang, Kailai Zhou  
**分类**：cs.CV  
**发布时间**：2026-11-05

### 📄 论文摘要

Scientific figures give research ideas a visual form through choices of abstraction, composition, and emphasis. Generative AI offers new ways to realize these choices, raising questions about explanatory clarity and purposeful visual expression. We examine these questions through a visual retrospective of 371 motivation and framework figures from 200 papers. The corpus comprises a quota-based main sample of 160 papers spanning four temporal periods and a separate purposive style-contrast sample of 40 papers. A single multimodal judge evaluates six dimensions of communication and design, with three repeated judgments per figure. We attempt source-constrained revisions of all 371 figures, of which 369 pass the recorded fidelity checks. Original-figure ratings show no uniform decline across periods. Revisions increase mean clarity ratings by 0.428 points and decrease aesthetic coherence ratings by 0.111 points on a five-point scale. Gains in the six-dimension average are larger for main-sample motivation figures than for frameworks. Case analyses show that added explanation can clarify comparisons while leaving typographic hierarchy and visual economy unresolved. These model-based findings support researcher-led design, with AI assisting exploration and authors retaining responsibility for explanatory purpose, composition, and scientific relationships. The accompanying atlas and evaluation records are available at https://ntu-ai4x.github.io/Rethinking_Figures/index_en.html.

### 🤖 AI 总结

**一句话总结**：Scientific figures give research ideas a visual form through choices of abstraction, composition, and emphasis. Generative AI offers new ways to realize these choices, raising questions about explanat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, We, Miss, Nights, Spent, Crafting, Figures?, Rethinking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08486v1) | [下载PDF](https://arxiv.org/pdf/2611.08486v1.pdf)

---

## [13. Where and Why is Grounded Reasoning Useful?](https://arxiv.org/abs/2611.08485v1)

**作者**：David Yan, Le Xue, Forrest Huang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-05

### 📄 论文摘要

Grounded reasoning, where a model outputs text coordinates of relevant locations in chain-of-thought reasoning, is a common strategy for solving complex visual reasoning problems. However, the benefits and limitations of grounded reasoning are understudied. We study where and why grounded reasoning is most useful. To do so, we introduce a chain-of-thought analysis method to measure how much a model uses its outputted grounding in its thinking trace and perform a detailed ablation study of a grounded reasoning training recipe. We find that grounded reasoning improves counting but shows no significant gain over baselines without coordinate grounding across a wide range of spatial reasoning and perception benchmarks. Using several synthetic tasks, we show that grounded reasoning is most useful when a task requires undescribable references, which are visual concepts that are difficult to describe in language. However, we observe that many existing visual reasoning benchmarks are solvable with only describable text references. To close this gap, we introduce BrickVision, a new benchmark that requires undescribable visual references to solve.

### 🤖 AI 总结

**一句话总结**：Grounded reasoning, where a model outputs text coordinates of relevant locations in chain-of-thought reasoning, is a common strategy for solving complex visual reasoning problems. However, the benefit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Where, Why, Grounded, Reasoning, Useful?, model, outputs, text

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08485v1) | [下载PDF](https://arxiv.org/pdf/2611.08485v1.pdf)

---

## [14. EgoGeneralist: Unifying Egocentric Action-Video Tasks through Video-Native Modeling](https://arxiv.org/abs/2611.08477v1)

**作者**：Yanlin Jin, Bowen Yang, Cheng Zhang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-05

### 📄 论文摘要

Modern video models possess strong visual priors, yet do not natively represent human action in metric 3D space. We present EgoGeneralist, which adapts pretrained video generators to unify action-conditioned egocentric video generation, pose estimation, and joint action-video generation. Our role-adaptive action renderer provides video-native representations for multidirectional action-video learning, making metric motion usable as both a spatial control signal and a recoverable generation target. Cross-stream action-video coupling establishes close correspondence between metric motion and visual dynamics through lightweight adaptation while preserving the pretrained visual prior. Together, these designs establish a generalist framework spanning five action-video tasks. Despite adaptation only on controlled laboratory recordings, EgoGeneralist generalizes to diverse unseen scenes and interactions with effective action control and visual quality, bridging pretrained visual knowledge and metric 3D human motion.

### 🤖 AI 总结

**一句话总结**：Modern video models possess strong visual priors, yet do not natively represent human action in metric 3D space. We present EgoGeneralist, which adapts pretrained video generators to unify action-cond...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EgoGeneralist, Unifying, Egocentric, Action-Video, Tasks, through, Video-Native, Modeling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08477v1) | [下载PDF](https://arxiv.org/pdf/2611.08477v1.pdf)

---

## [15. Edge-Assisted Crowdsensing for Explainable Cyclist Safety Perception](https://arxiv.org/abs/2611.08441v1)

**作者**：Hongsen Cao, Chia-Yen Chiang, Mona Jaber 等 5 位作者  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-11-05

### 📄 论文摘要

Cyclist fatality rates remain high despite policy support for active travel, and autonomous vehicles add complexity to mixed traffic. Neither crash statistics nor multi-model detection pipelines scale to continuous monitoring of perceived safety along a route. We present an edge-assisted crowdsensing system: handlebar cameras supply street-level frames, a vision-language model (VLM) turns each frame into structured traffic attributes through a single prompt, and an explainable boosting machine (EBM) combines them with OpenStreetMap road infrastructure and on-bike kinematics to predict a crowdsourced 1-9 safety score. Extraction belongs at the network edge: the fastest self-hosted model needs 2.49 s per frame and scoring takes 0.4 ms on a CPU. On 1,362 annotated frames from two London routes, the EBM regressor reaches 72.2 percent binary accuracy and a mean absolute error of 1.011 under five-fold cross-validation. It is within one accuracy point of black-box ensembles. Its per-feature shape functions give exact attribution: physical lane separation is worth +0.97 rating points, a painted lane +0.70 and a construction site -0.65. Planners can therefore price an infrastructure change in rating points, and the results enter cost-benefit analysis directly. We also report inter-annotator agreement (alpha = 0.4695), an attribute audit, and a sensitivity analysis linking attribute error to accuracy. With re-encoding, a 20 s sampling interval serves 1,000 riders at 54 Mbit/s at a cost of 1.4 accuracy points, making continuous monitoring practical.

### 🤖 AI 总结

**一句话总结**：Cyclist fatality rates remain high despite policy support for active travel, and autonomous vehicles add complexity to mixed traffic. Neither crash statistics nor multi-model detection pipelines scale...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Edge-Assisted, Crowdsensing, Explainable, Cyclist, Safety, Perception, fatality, rates

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08441v1) | [下载PDF](https://arxiv.org/pdf/2611.08441v1.pdf)

---

## [16. Adaptive Low-Light Enhancement for Road Anomaly Detection: A Multi-Architecture Benchmark and Edge Deployment Study](https://arxiv.org/abs/2611.08393v1)

**作者**：Obed Honour Eje, Oluwatosin Kolade, Glory Bagai 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-05

### 📄 论文摘要

Road anomaly detection systems on autonomous vehicles must function reliably under degraded visual conditions including darkness, rain, and Harmattan dust haze. This paper benchmarks four object detection architectures, YOLOv8n, YOLOv12n, RT-DETR, and Faster R-CNN, under physically grounded lighting and weather degradation, and shows that uniform application of the SCI low-light enhancement network is actively harmful at dusk-level lighting (-16.1% to -30.7% mAP@50). We propose a lightweight, training-free luminance-adaptive router that selects between no enhancement, moderate SCI, and denoising plus strong SCI based on per-frame Rec. 601 luminance, recovering most of the dusk penalty while preserving low-light gains, and we validate the full pipeline on NVIDIA Jetson Nano edge hardware.

### 🤖 AI 总结

**一句话总结**：Road anomaly detection systems on autonomous vehicles must function reliably under degraded visual conditions including darkness, rain, and Harmattan dust haze. This paper benchmarks four object detec...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Adaptive, Low-Light, Enhancement, Road, Anomaly, Detection, Multi-Architecture, Benchmark

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08393v1) | [下载PDF](https://arxiv.org/pdf/2611.08393v1.pdf)

---

## [17. OraRefer: Segmentation-Guided Multi-Photograph Fusion for Oral Cancer Screening with Guaranteed Patient-Level Sensitivity](https://arxiv.org/abs/2611.08360v1)

**作者**：Rupam Mukherjee, Mehakdeep Singh, Shirin Dasgupta 等 4 位作者  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-11-05

### 📄 论文摘要

Oral cancer and the oral potentially malignant disorders (OPMD) that can precede it are visible on the oral mucosa, which makes smartphone photographs a promising tool for screening. Deep learning models for this task classify individual photographs. However, screening refers patients, not photographs: a patient is usually photographed several times, and the referral decision must miss no more than a set share of patients with disease. We propose OraRefer, a patient-level screening model that reads each photograph with a segmentation-guided foundation model that conditions its class decision on the predicted lesion, combines all photographs of a patient with risk factors, and refers through a threshold with a finite-sample sensitivity guarantee. The model localizes the mouth itself, so inference needs no annotation. On 3000 photographs of 714 patients, patient-level fusion reaches an AUROC of 0.919 and outperforms attention-based multiple-instance learning. At a 90% sensitivity target, OraRefer detects 95% of patients with OPMD or cancer and misses 3 of 61 patients with cancer, at a specificity of 0.610. Because the threshold is calibrated without retraining, each clinic can set its own guaranteed operating point on a local calibration sample.

### 🤖 AI 总结

**一句话总结**：Oral cancer and the oral potentially malignant disorders (OPMD) that can precede it are visible on the oral mucosa, which makes smartphone photographs a promising tool for screening. Deep learning mod...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OraRefer, Segmentation-Guided, Multi-Photograph, Fusion, Oral, Cancer, Screening, Guaranteed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08360v1) | [下载PDF](https://arxiv.org/pdf/2611.08360v1.pdf)

---

## [18. USB Gym: A Gymnasium Testbed for Closed-Loop Ultrasound View Matching](https://arxiv.org/abs/2611.08352v1)

**作者**：Thanapong Intharah, Zhichao Gao, Yiliang Liu 等 4 位作者  
**分类**：cs.CV, cs.LG, cs.RO  
**发布时间**：2026-11-05

### 📄 论文摘要

Background and Objective: Our main goal is ultrasound guidance: moving a probe until its image matches a target view. Published methods for each part of a guide are evaluated in separate simulators. We asked whether these methods, combined into one guide, are good enough.   Methods: We built USB Gym, a testbed whose standard engine simulates ultrasound from public patient CT, with a network drawing organ textures from CT labels. Its guide has three replaceable parts (slots), an organ segmenter, a controller and a reward, which received 20 published methods, each run on the same 60 episodes of six held-out patients. In each slot, a published method replaced ours only if detectably better on these patients. The better of this combination and our original guide on 20 new CTs is the benchmark baseline. A pose oracle, reading the exact probe pose available only in simulation, set the reference. The results below are exploratory.   Results: On these CTs, the probe started on average 16.0 mm from the target view; the pose oracle brought it to 1.5 mm. Of the results known when the combination was fixed, only an image-similarity reward (SSIM) was slightly but detectably better, so the combination was our guide with that reward. This combination was the benchmark baseline, ending at 13.7 mm (16% of the oracle's progress).   Conclusions: Combining untuned published methods with ours did not guide the probe near the target view; the task remains under-explored. The testbed accepts new methods; no guide was tested on hardware.

### 🤖 AI 总结

**一句话总结**：Background and Objective: Our main goal is ultrasound guidance: moving a probe until its image matches a target view. Published methods for each part of a guide are evaluated in separate simulators. W...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：USB, Gym, Gymnasium, Testbed, Closed-Loop, Ultrasound, View, Matching

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08352v1) | [下载PDF](https://arxiv.org/pdf/2611.08352v1.pdf)

---

## cs.LG

## [19. User Embeddings are Superpositions of Interpretable Behavioral Modes](https://arxiv.org/abs/2611.08487v1)

**作者**：Jonathan Kozaczuk, Zheng Dong, Noyan Evirgen 等 10 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-05

### 📄 论文摘要

User embeddings are central components of modern recommendation, personalization, and behavioral modeling systems. Though these embeddings can compactly encode rich behavioral information, they are inherently dense and opaque, limiting interpretability. To address this gap, we argue that user embeddings can be understood as sparse superpositions of interpretable behavioral modes. This structure is directly predicted by generative models of user behavior for linear embeddings and extends approximately to deep-learning representations by the superposition hypothesis. Superimposed modes can naturally be recovered by sparse dictionary learning methods, such as sparse autoencoders (SAEs), and recovered modes can be automatically named and queried in natural language. We validate mode recovery against known ground truth on synthetic data, where SAEs recover modes better than classical sparse baselines, including on transformer-encoded embeddings. We then apply the method to classical and transformer-based user embeddings from two real-world datasets. We also show how the corresponding natural-language labels enable zero-shot audience retrieval and characterization over embeddings never trained on text. The framework is post-hoc and model-agnostic, requiring no modification to the upstream embedding system.

### 🤖 AI 总结

**一句话总结**：User embeddings are central components of modern recommendation, personalization, and behavioral modeling systems. Though these embeddings can compactly encode rich behavioral information, they are in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, User, Embeddings, Superpositions, Interpretable, Behavioral, Modes, central

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08487v1) | [下载PDF](https://arxiv.org/pdf/2611.08487v1.pdf)

---

## [20. XStack: A Benchmark for ML Repo Migration](https://arxiv.org/abs/2611.08472v1)

**作者**：Linrong Cai, Taiming Lu, Haozhe Chen 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-05

### 📄 论文摘要

ML code should run where researchers choose, not where it was first written. Today, machine learning code mainly lives in two ecosystems, PyTorch on NVIDIA GPUs and JAX on Google TPUs. Migrating repositories between them means building and testing across frameworks and hardware. This migration is (1) a practical need, since it unlocks different hardware for researchers, and (2) a natural benchmark: it involves different frameworks and hardware, covers whole repositories, and is long-horizon and challenging. We introduce XStack, a benchmark that evaluates agents on migrating ML repositories between these two ecosystems. Each agent receives a PyTorch repository and a clean TPU machine and must deliver a JAX repository. Its output passes if it meets our grading criteria, based on the source repository's published result, authenticated and calibrated by us. Migration by agents remains unreliable: Claude Opus 5 passes 75%, GPT-5.6-sol 45%, and every other agent at most 40%. XStack is a step toward freeing ML code from its ecosystem. We release XStack to make progress toward reliable migration across frameworks and hardware measurable.

### 🤖 AI 总结

**一句话总结**：ML code should run where researchers choose, not where it was first written. Today, machine learning code mainly lives in two ecosystems, PyTorch on NVIDIA GPUs and JAX on Google TPUs. Migrating repos...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ML, XStack, Benchmark, Migration, code, should, run, where

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08472v1) | [下载PDF](https://arxiv.org/pdf/2611.08472v1.pdf)

---

## [21. Same Behavior, Different Mechanism: What Finite Experiments Can Certify About Integrated Information](https://arxiv.org/abs/2611.08469v1)

**作者**：Linqian Wu, Diaoxuan He  
**分类**：cs.LG, cs.AI, q-bio.NC  
**发布时间**：2026-11-05

### 📄 论文摘要

Interpretability, AI auditing and assessments of machine consciousness increasingly rest on mechanism-level quantities: functionals of a system's causal transition law that describe how it computes, not what it outputs. Experiments see that law only through finite, partial and noisy interventions. We ask when such a quantity is identifiable from an experiment's access, continuous in the mechanism and certifiable from finite data, and answer exactly for a deliberately demanding case - the integrated information $\varphi$ of integrated information theory - in stochastic networks of four and five units with known ground truth. Behavior can be silent: a recurrent and a feed-forward network with identical input-output laws at their response delay carry 0.28 and 0 bits, yet internal recordings separate them within 4-53 trials. Partial access can be just as blind: in our examples, units left out of a one-step recording impose precision floors of 0.30-1.02 bits that no sample size lowers, and in all-but-self parity networks, recordings of any length see several hidden units only through the product of their fidelities - a symmetry that one intervention broke in exact checks. The measure has sharp edges: because $\varphi$ selects a partition, and the cause and effect it specifies, by one criterion and reports another, infinitesimal changes of mechanism that cross an edge change it by 25-100% at 99% of the edges we found in random networks, and about 1% of surrogate models that fit interventional data almost perfectly misreport it by more than 20%. One-sided claims survive: the same data certify a lower bound on both sides of an edge, and we prove $\varphi>1.004$ bits throughout a 64-dimensional region of mechanisms and certify it from about $10^7$ controlled transitions with false-certificate probability at most $α$. Measurability is thus a design question with computable answers.

### 🤖 AI 总结

**一句话总结**：Interpretability, AI auditing and assessments of machine consciousness increasingly rest on mechanism-level quantities: functionals of a system's causal transition law that describe how it computes, n...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Same, Behavior, Different, Mechanism, What, Finite, Experiments, Can

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08469v1) | [下载PDF](https://arxiv.org/pdf/2611.08469v1.pdf)

---

## [22. Adversarial Training with Large Step Sizes: Implicit Bias, Optimization, and Sharpness](https://arxiv.org/abs/2611.08457v1)

**作者**：Yi Feng, Andrea Paudice  
**分类**：cs.LG, math.OC  
**发布时间**：2026-11-05

### 📄 论文摘要

Adversarial Training (AT) is an important method for improving model robustness. We study the dynamics of deterministic Gradient Descent (GD) in AT. Most existing works in this direction focus on the small or vanishing step sizes regime, where GD resembles a continuous-time flow. However, such step sizes can make training inefficient and are rarely used in practice. In this paper, we study the AT dynamics of GD with large constant step sizes. We first study GD in adversarial linear logistic regression, focusing on two aspects: where the model parameters converge (implicit bias) and how quickly the losses decrease (optimization). We then turn to neural networks training and study how the sharpness of losses evolve during AT. Our results advance the understanding of the behaviors of GD with large step sizes in AT and highlight three key differences from its behavior in Standard Training (ST): (i) the implicit bias gap between AT and ST, previously established only for small step sizes, persists for arbitrarily large constant step sizes, (ii) different from ST, there is no uniform rate of convergence for the optimization error in AT, and (iii) sharpness can exhibit two-stage dynamics that differ from the Edge-of-Stability behavior observed in ST.

### 🤖 AI 总结

**一句话总结**：Adversarial Training (AT) is an important method for improving model robustness. We study the dynamics of deterministic Gradient Descent (GD) in AT. Most existing works in this direction focus on the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Adversarial, Training, Large, Step, Sizes, Implicit, Bias, Optimization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08457v1) | [下载PDF](https://arxiv.org/pdf/2611.08457v1.pdf)

---

## [23. A Hidden Markov Preference Model for Online Prediction of Adversary Actions](https://arxiv.org/abs/2611.08445v1)

**作者**：Angel Daruna, Michael Cogswell, Tixiao Shan 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-05

### 📄 论文摘要

A defender anticipating an attacker needs a probability distribution over the attacker's next action from information available before that action occurs. Two structures complicate this: the attacker's behavioral regime persists and can switch within an episode, and each action combines an operation with state-dependent arguments whose feasible values change over time. We capture both with a hidden Markov model whose latent state is the active regime and whose regime-conditioned action law is defined on a feasibility-masked tree of executable actions. The same likelihood forms the next-action distribution and updates the regime belief once the action is seen, and a partially observed prefix contributes its resolved local factors. Estimation separates into convex logistic fits that Baum-Welch reuses when regimes are unlabeled. We derive a reach-weighted nodewise KL expression for regime information, a sequence-wise log-loss bound for switching regime paths, and a uniform fallback guarantee. On the CAGE 2 cyber defense benchmark the filtered latent state is worth 0.8 nats per step, and after a controller switch the loss begins to fall in three steps against ten for a recurrent baseline.

### 🤖 AI 总结

**一句话总结**：A defender anticipating an attacker needs a probability distribution over the attacker's next action from information available before that action occurs. Two structures complicate this: the attacker'...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Hidden, Markov, Preference, Model, Online, Prediction, Adversary

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08445v1) | [下载PDF](https://arxiv.org/pdf/2611.08445v1.pdf)

---

## [24. Data-driven discovery of intrinsic Lie point symmetries of differential equation systems](https://arxiv.org/abs/2611.08421v1)

**作者**：Ilker Gurcan, Kadir Ustun, Ramazan Gokberk Cinbis  
**分类**：cs.LG, math.DG, math.DS, math.GR, math.NA  
**发布时间**：2026-11-05

### 📄 论文摘要

Discovering continuous symmetries directly from differential-equation data can reveal geometric structure for model reduction and scientific machine learning without symbolic determining equations or a closed-form representation of the governing system. We formulate intrinsic Lie point-symmetry discovery as an operator-theoretic problem on sampled jet-space data. Admissible generators are identified from a sampled determining operator and separated from redundant, solution-dependent, and geometrically trivial directions. The framework combines prolongation, sequential subspace restrictions, and a fixed nonlinear dictionary linear in trainable coefficients. A rank-stabilization preflight test diagnoses systems whose represented intrinsic symmetry algebra does not stabilize under dictionary refinement. On a controlled differential-equation benchmark with an analytically known 11-dimensional represented intrinsic symmetry algebra, the method recovers the complete represented generator set, reproduces its Lie-bracket structure to numerical precision, and approximates a known generator beyond the training domain. Here we show that explicit intrinsic continuous-symmetry generators can be recovered from data obtained from exact or approximate differential systems.

### 🤖 AI 总结

**一句话总结**：Discovering continuous symmetries directly from differential-equation data can reveal geometric structure for model reduction and scientific machine learning without symbolic determining equations or ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Data-driven, discovery, intrinsic, Lie, point, symmetries, differential

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08421v1) | [下载PDF](https://arxiv.org/pdf/2611.08421v1.pdf)

---

## [25. On the limitations of molecular representations](https://arxiv.org/abs/2611.08420v1)

**作者**：Acer Blake, Fergus Imrie, Charlotte M. Deane  
**分类**：cs.LG  
**发布时间**：2026-11-05

### 📄 论文摘要

Molecular representations such as fingerprints and learned embeddings play a central role in cheminformatics and small-molecule machine learning. They serve as the primary input for a diverse array of tasks, including clustering, dataset splitting, and virtual screening, yet their evaluation is often limited to downstream model performance on narrow benchmark tasks. We carried out a systematic investigation of the quality of molecular representations, finding that none of the state-of-the-art molecular embedding models capture graph structure, 3D shape, or ADMET endpoint similarity better than fingerprints or physicochemical descriptors. However, classical fingerprints also revealed their own material limitations. For example, we show that depending on the representation, between 225M and $\sim$4B molecules have non-unique representations in the 10.8B Enamine REAL database, with implications for virtual screening. Our findings provide an insight into the current limitations of molecular representations, outlining future research directions for the development of more robust encodings of small molecules.

### 🤖 AI 总结

**一句话总结**：Molecular representations such as fingerprints and learned embeddings play a central role in cheminformatics and small-molecule machine learning. They serve as the primary input for a diverse array of...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, as, limitations, molecular, representations, such, fingerprints, learned

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08420v1) | [下载PDF](https://arxiv.org/pdf/2611.08420v1.pdf)

---

## [26. Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning](https://arxiv.org/abs/2611.08414v1)

**作者**：Chenruo Liu, Zihan Wang, Yijun Dong 等 4 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-11-05

### 📄 论文摘要

Low-rank adaptation (LoRA) is commonly used in both supervised fine-tuning (SFT) and reinforcement learning (RL), often under similar optimizer settings. Yet, how the different dynamics of the two stages manifest in the low-rank increment that LoRA optimizes remains unclear. Tracking the singular spectrum and subspaces of LoRA updates on mathematical reasoning tasks, we find that RL concentrates the spectrum at every learning rate, while SFT expands it at moderate learning rates; moreover, RL rotates the singular subspaces much faster than SFT at small learning rates. Interpolating between SFT and RL one ingredient at a time, we pinpoint group-mean baseline subtraction as the source of both contrasts. A quadratic multi-index model updated via LoRA unveils the underlying mechanism: group-mean baseline subtraction tilts the balance between two competing forces, coherent fitting and gradient noise, toward spectral concentration and faster subspace rotation, while forcing the risk-favorable learning rate to be low. Guided by these dynamics, we tailor LoRA updates to each stage: in SFT, we flatten the spectrum of the full update to spread adaptation across singular directions, whereas in RL, we flatten the part of the update outside the current LoRA increment span to promote subspace rotation. Experiments on mathematical reasoning tasks across multiple models show that the respective configurations for SFT and RL yield the best performance among the compared methods in most evaluated settings.

### 🤖 AI 总结

**一句话总结**：Low-rank adaptation (LoRA) is commonly used in both supervised fine-tuning (SFT) and reinforcement learning (RL), often under similar optimizer settings. Yet, how the different dynamics of the two sta...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Spectral, Subspace, Dynamics, LoRA, Supervised, Fine-Tuning, Reinforcement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08414v1) | [下载PDF](https://arxiv.org/pdf/2611.08414v1.pdf)

---

## [27. Synthesis of Ovarian Cancer Multi-Omics Datasets: A Biology-Informed Evaluation Framework](https://arxiv.org/abs/2611.08394v1)

**作者**：Déborah Boyenval, Alina Malyutina, Jaana Oikkonen 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-05

### 📄 论文摘要

Paired multi-omic cancer cohorts are costly to assemble and difficult to share, motivating synthetic cohorts as a complementary resource. As generative model development accelerates, we shift the focus from proposing yet another architecture to defining evaluation criteria that determine whether synthetic data preserve biologically relevant structure. We introduce a biology-informed and patient-disjoint framework for evaluating the generation of paired RNA expression and copy-number variation (CNV) profiles, and apply it to the longitudinal DECIDER high-grade serous ovarian cancer cohort. The framework assesses modality-specific fidelity and coherence between RNA and CNV pairs using agreement between real training and held-out data as a reference, alongside complementary training-data proximity diagnostics. We adapt three multi-omic integration architectures based on variational autoencoders to generate paired profiles. The model leading several fidelity and coherence measures also shows the strongest training-data proximity. The protocol and case study offer the community a reference for comparing future multi-omic generators.

### 🤖 AI 总结

**一句话总结**：Paired multi-omic cancer cohorts are costly to assemble and difficult to share, motivating synthetic cohorts as a complementary resource. As generative model development accelerates, we shift the focu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Synthesis, Ovarian, Cancer, Multi-Omics, Datasets, Biology-Informed, Evaluation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08394v1) | [下载PDF](https://arxiv.org/pdf/2611.08394v1.pdf)

---

## [28. Hybrid Machine Learning for Imbalanced Landing-Phase Safety Event Prediction from Flight Data](https://arxiv.org/abs/2611.08386v1)

**作者**：Taha Asghar, Bilal Mufti, Syed Qasim Zaheer 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-05

### 📄 论文摘要

Landing-phase safety-event prediction requires the detection of rare abnormal approaches within strongly imbalanced multivariate flight data. Capturing coupled temporal behavior while distinguishing event-specific signatures across airport operating contexts remains a central modeling challenge. This study proposes an interpretable hybrid feature-fusion framework for multiclass landing-phase safety-event prediction. A long short-term memory (LSTM) autoencoder trained on nominal flight windows characterizes deviations from routine approach behavior. Its continuous reconstruction-error descriptor is fused with parameter-specific statistical flight-history features and supplied to a class-weighted XGBoost classifier to distinguish Normal, Speed High, Path High, and Flaps Late windows. The framework is evaluated using 53,750 NASA DASHlink approach windows from three arrival airports. Pooled and airport-specific learning strategies are compared alongside component-level benchmarks, repeated pipeline retraining, and feature-attribution analysis. The results demonstrate strong class-balanced detection, with mean macro recall above 0.90 across all airports under repeated partitioning and retraining. Component comparisons establish the importance of class weighting and show that continuous feature fusion outperforms reconstruction-error-only and hard-gate alternatives. Airport-level comparisons reveal benefits from local specialization at the two airports with larger datasets and from pooled training at the airport with the smallest dataset. Feature attributions associate predictions with operationally relevant vertical-path, configuration, speed, and approach-context variables. The framework provides an interpretable approach to rare-event detection and practical guidance for adapting flight-data monitoring models to airport-level data availability.

### 🤖 AI 总结

**一句话总结**：Landing-phase safety-event prediction requires the detection of rare abnormal approaches within strongly imbalanced multivariate flight data. Capturing coupled temporal behavior while distinguishing e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hybrid, Machine, Learning, Imbalanced, Landing-Phase, Safety, Event, Prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08386v1) | [下载PDF](https://arxiv.org/pdf/2611.08386v1.pdf)

---

## [29. Module-Aware Optimization for Graph Neural Networks](https://arxiv.org/abs/2611.08379v1)

**作者**：Guy Hadad, Haggai Roitman, Moshe Eliasof 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-05

### 📄 论文摘要

Different optimizers impose different geometries on parameter updates. Adaptive methods such as Adam and AdamW use coordinate-wise updates, while matrix-aware optimizers such as Muon utilize weight-matrix structure through orthogonalized updates. For Graph Neural Networks (GNNs), however, the effective geometry of its weight matrices is shaped not only by its learned channel-mixing weights, but also by the graph-propagated representations it acts on. Thus, even if an update is well normalized as a matrix, its effect on the layer output can be amplified when applied to graph-propagated features. To address this gap, we introduce GraphMuon, a graph-aware optimizer that adapts Muon's matrix updates to the covariance structure of graph-propagated layer inputs. GraphMuon performs orthogonalization in a metric defined by these propagated representations and normalizes step sizes according to the update's induced effect on the layer representation. We show that theoretically, vanilla Muon can suffer from graph-induced update amplification, while our GraphMuon can mitigate this effect. As such, our GraphMuon yields a graph-metric analogue of Muon's polar update step. Empirically, GraphMuon achieves $1.32\times$-$2.42\times$ validation-loss time-to-target speedups over AdamW on three large-scale OGB benchmarks. Across 15 dataset-architecture configurations spanning node classification, inductive graph classification, and graph regression, it achieves lower time-to-target in 13 cases, while maintaining competitive or superior predictive performance. Code is available at https://github.com/guy-hadad/GraphMuon.

### 🤖 AI 总结

**一句话总结**：Different optimizers impose different geometries on parameter updates. Adaptive methods such as Adam and AdamW use coordinate-wise updates, while matrix-aware optimizers such as Muon utilize weight-ma...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Module-Aware, Optimization, Graph, Neural, Networks, Different, optimizers, impose

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08379v1) | [下载PDF](https://arxiv.org/pdf/2611.08379v1.pdf)

---

## [30. StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference](https://arxiv.org/abs/2611.08363v1)

**作者**：Jake Hyun, Ziyu Zhao, Jae-sun Seo 等 4 位作者  
**分类**：cs.LG, cs.DC  
**发布时间**：2026-11-05

### 📄 论文摘要

Quantization reduces the memory and bandwidth demands of large language model (LLM) inference but can degrade accuracy; offloading higher-precision data can instead stall generation. We introduce StrataFlux, a framework that challenges this tradeoff by recovering accuracy lost to low-bit weight and key-value (KV) cache quantization while retaining quantization's memory and speed advantages. StrataFlux co-designs refinement representation, selection, and delivery to make host RAM and solid-state drives useful sources of additional precision. Its selective precision streaming reduces transfer volume, overlaps delivery with computation, and reuses fetched precision across decoding steps so generation need not wait for every transfer. We evaluate 2-4-bit weights and 2-3-bit KV-cache on dedicated GPUs and unified-memory platforms. For 2-bit Llama-3.1-8B-Instruct weights, StrataFlux reduces WikiText-2 perplexity from 9.46 to 8.40 while maintaining 95.4% of the quantized base's throughput on RTX 5090. With 2-bit weights and KV, StrataFlux raises Qwen3-8B's AIME 2024/2025 accuracy from 11.0% to 47.1% at unchanged GPU memory use. At 128K context, Llama-3.1-8B-Instruct with 3-bit weights and 2-bit KV achieves comparable perplexity and speed to vLLM's 4-bit AWQ weights and 8-bit KV on RTX 5090, using approximately half the GPU memory. These results show that GPU-resident precision need not set the accuracy ceiling, nor offloading-tier latency dictate decoding speed.

### 🤖 AI 总结

**一句话总结**：Quantization reduces the memory and bandwidth demands of large language model (LLM) inference but can degrade accuracy; offloading higher-precision data can instead stall generation. We introduce Stra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, StrataFlux, Memory-Hierarchy-Native, Low-Bit, Inference, Quantization, reduces, memory

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.08363v1) | [下载PDF](https://arxiv.org/pdf/2611.08363v1.pdf)

---

