# arXiv AI 论文日报 | 2026-09-25

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.AI](#csAI) (9 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.CV](#csCV) (8 篇)
- [cs.CL](#csCL) (5 篇)

---

## cs.AI

## [1. AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control](https://arxiv.org/abs/2609.30264v1)

**作者**：Jiabin Qiu, Zixuan Chen, Hongye Cao 等 6 位作者  
**分类**：cs.AI, cs.RO  
**发布时间**：2026-09-24

### 📄 论文摘要

Latent world models are typically trained to predict factual transitions, whereas model predictive control (MPC) must compare alternative actions from the same state. A model can therefore achieve low factual prediction error yet poorly distinguish candidate actions. We introduce AD-WM, an action-discriminative joint-embedding world model for counterfactual MPC. AD-WM combines residual latent dynamics with predictor-level action-recovery regularization, using inverse dynamics and a normalized recovery objective motivated by conditional mutual information. Both objectives encourage planning transitions to preserve action information; their auxiliary heads are discarded at test time, leaving MPC unchanged. On OGBench-Cube, AD-WM improves hard-start success from 3.7% to 52.0% over a matched LeWM baseline and improves mean success over the reproduced baseline in four of five simulation environments. Planning diagnostics show that factual prediction error and whole-bank action ranking do not follow the closed-loop success ordering, whereas CEM-aligned elite regret tracks success more closely. With a frozen V-JEPA 2 encoder and matched DROID post-training, AD-WM also improves zero-shot transfer to our Franka setup, increasing basic pick-and-place success from 42.2% to 71.1% without lab-specific adaptation. These results suggest that world models for planning should preserve action-dependent differences needed for counterfactual selection, rather than optimize factual prediction accuracy alone. More videos and code are available at https://ad-wm.github.io/.

### 🤖 AI 总结

**一句话总结**：Latent world models are typically trained to predict factual transitions, whereas model predictive control (MPC) must compare alternative actions from the same state. A model can therefore achieve low...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AD-WM, Action-Discriminative, World, Models, Counterfactual, Model, Predictive, Control

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30264v1) | [下载PDF](https://arxiv.org/pdf/2609.30264v1.pdf)

---

## [2. A Living Benchmark for Information Retrieval from Electronic Health Records](https://arxiv.org/abs/2609.30205v1)

**作者**：Jordan L. Cahoon, Chloe O. Stanwyck, Sulaiman Somani 等 26 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-24

### 📄 论文摘要

Large language model (LLM)-based clinical assistants are increasingly being integrated into electronic health record (EHR) systems, transforming how clinicians retrieve and synthesize information from patient records. Their safety and utility depend on rigorous evaluation, yet existing benchmarks are manually curated, costly to update, and rapidly become obsolete with evolving technological advancements. We present a scalable framework that automatically generates question--answer pairs from longitudinal EHR notes. Nineteen clinicians validate the benchmark generator, producing the Benchmark for Retrieving Information in EHRs (BRIE), a continuously maintainable evaluation dataset. Across nine LLMs and five inference strategies, state-of-the-art systems frequently omit clinically important information, particularly for questions requiring synthesis across multiple documents and encounters. Because the generator itself is validated, BRIE supports evaluations that static benchmarks cannot, including the generation of multiple answers that reflect variation in clinician reasoning for robust performance assessment and continuously refreshing benchmark content to guard against leakage. Our results demonstrate that scalable benchmark generation enables rigorous, up-to-date evaluation of clinical LLMs as they are deployed in rapidly evolving healthcare settings.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM)-based clinical assistants are increasingly being integrated into electronic health record (EHR) systems, transforming how clinicians retrieve and synthesize information from...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Living, Benchmark, Information, Retrieval, Electronic, Health, Records, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30205v1) | [下载PDF](https://arxiv.org/pdf/2609.30205v1.pdf)

---

## [3. ExplorationBench: Measuring AI Systems' Exploration in Verifiable Alien Worlds](https://arxiv.org/abs/2609.30199v1)

**作者**：Ming Zhang, Zhenghao Xiang, Peizhong Gao 等 20 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-09-24

### 📄 论文摘要

Scientific discovery begins where known problems end. There, AI systems must engage in exploration: framing hypotheses, designing experiments, and iterating on the results. However, evaluating this ability is difficult: (1) how to verify whether a genuinely new hypothesis holds, and (2) how to determine whether a system has discovered it through exploration or merely recalled related knowledge from pre-training data. To this end, we introduce ExplorationBench, which turns the wicked problem of evaluating scientific exploration into a concrete and tractable framework built on verifiable Alien Worlds: their rules are executable, so every answer can be checked exactly, and they conflict with familiar knowledge, so recall alone cannot solve the tasks. The benchmark contains two sandboxes, AlienCode (31 discovery targets, 70 tasks) and AlienLogic (24 discovery targets, 70 tasks). Each sandbox provides a flawed manual, task-specific environmental feedback, and a dedicated tool-call schema. Systems use these resources to explore the sandbox, then solve held-out tasks. We evaluate 10 AI systems and find that the strongest systems can acquire and apply unfamiliar rules, while performance varies substantially across trajectories and continued exploration can stall or reverse earlier gains. ExplorationBench represents a step towards AI systems that can acquire and apply genuinely new knowledge through exploration in unknown environments.

### 🤖 AI 总结

**一句话总结**：Scientific discovery begins where known problems end. There, AI systems must engage in exploration: framing hypotheses, designing experiments, and iterating on the results. However, evaluating this ab...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ExplorationBench, Measuring, Systems', Exploration, Verifiable, Alien, Worlds, Scientific

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30199v1) | [下载PDF](https://arxiv.org/pdf/2609.30199v1.pdf)

---

## [4. SAGE: Mitigating Long-Horizon Reasoning Biases via Topological Guidance](https://arxiv.org/abs/2609.30192v1)

**作者**：Xinyue Zeng, Jiawei Zhang, Yujun Yan 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-24

### 📄 论文摘要

Long-horizon reasoning remains a central challenge for large language models (LLMs) under sparse-reward regimes. We argue that this brittleness arises from two biases induced by complex reasoning spaces: an exploration bias, where models are drawn toward locally plausible but structurally unstable branches, and a compounding bias, where small local deviations accumulate across depth and suppress rare rewards. We introduce Symbolic Closure Analysis (SCA) as a theoretical lens characterizing how branching structures and sparse rewards induce these biases in long-horizon reasoning with local admissibility, and as a design principle for structural priors in less formal reasoning tasks. Motivated by this analysis, we propose SAGE (Structural Admissibility-Guided Exploration), a unified framework that injects structural guidance to alleviate exploration bias and compounding bias in long-horizon reasoning. SAGE combines two complementary structural guidance: algebraic sparsification, which projects locally admissible candidates onto operator-indexed algebraic subspaces to suppress spurious branching and mitigate exploration bias, and hyperbolic structural guidance, which embeds reasoning states into a negatively curved space to provide dense depth-wise signals and mitigate compounding bias. Across 12 benchmarks and 7 model families, SAGE outperforms competitive baselines. In particular, SAGE achieves up to an 8-fold improvement on the Andrews-Curtis problem, an open real-world long-horizon task. Code is available at: https://github.com/Susan571/SAGE-NeurIPS2026.

### 🤖 AI 总结

**一句话总结**：Long-horizon reasoning remains a central challenge for large language models (LLMs) under sparse-reward regimes. We argue that this brittleness arises from two biases induced by complex reasoning spac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SAGE, Mitigating, Long-Horizon, Reasoning, Biases, via, Topological, Guidance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30192v1) | [下载PDF](https://arxiv.org/pdf/2609.30192v1.pdf)

---

## [5. Jev-Mobile: Jev as an Executor for Mobile GUI Agents](https://arxiv.org/abs/2609.30186v1)

**作者**：Linghua Zhang  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-09-24

### 📄 论文摘要

Vision-language models (VLMs) have become a common foundation for autonomous mobile GUI agents, but most existing systems rely on the VLM for both planning and action grounding at nearly every interaction step, leading to substantial latency and model-serving cost. We introduce Jev-Mobile, which shifts this paradigm to low-frequency VLM planning and high-frequency lightweight execution: the VLM specifies local goals, the accessibility tree defines a structured executable action space, and Jev, a fast typed decision model, repeatedly selects actions within this space. This design allows multiple GUI actions to be executed under a single VLM decision, reducing expensive VLM inference while preserving adaptive interaction. On the full AndroidWorld task suite, Jev-Mobile achieves 79% task success, compared with 78% for SeeAct-V and 84% for a Step-wise VLM baseline. Among successful trajectories, it reduces mean end-to-end execution time by 32.7% and mean model API cost by 73.4% relative to Step-wise VLM. These results show that decoupling high-level VLM reasoning from low-level action execution can substantially improve mobile GUI agent efficiency while maintaining competitive task performance.

### 🤖 AI 总结

**一句话总结**：Vision-language models (VLMs) have become a common foundation for autonomous mobile GUI agents, but most existing systems rely on the VLM for both planning and action grounding at nearly every interac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, an, Agent, Jev-Mobile, Jev, Executor, Mobile, GUI

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30186v1) | [下载PDF](https://arxiv.org/pdf/2609.30186v1.pdf)

---

## [6. GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic AI](https://arxiv.org/abs/2609.30147v1)

**作者**：Arunabh Srivastava, Mohammad A., Khojastepour 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.LG, cs.MA  
**发布时间**：2026-09-24

### 📄 论文摘要

Large Language Models (LLMs) typically exhibit a performance profile where reliability degrades as task complexity increases. We address the challenge of generating high-quality natural language executable plans for complex tasks by introducing $\textbf{GRASP}$, a strategy-aware, multi-stage planning framework. GRASP decouples the planning pipeline across specialized, context-isolated modules: it pre-compiles global macro-guidelines (GenPlan), explores alternative localized strategies within isolated context windows (RevPlan), and independently evaluates trajectories using a multi-criteria discriminator (VerPlan). Empirical evaluations show that GRASP consistently establishes a new state-of-the-art frontier across diverse datasets, yielding substantial accuracy gains over direct LLM planners on Natural Plan Calendar Scheduling ($\sim$12.4$\%$$\uparrow$), ZebraLogic ($\sim$30.8$\%$$\uparrow$), and SciBench Math. Crucially, under multi-task scaling-where standard planners suffer immediate performance collapse-GRASP completely flattens the multi-task degradation penalty. In interleaved dual-task environments, GRASP achieves an absolute accuracy gain of up to 16.7$\%$ over direct LLM planners. Furthermore, by isolating context and enforcing strict macro-regularization, GRASP outperforms frontier reasoning models (such as GPT-5-mini) by a margin of 14.5$\%$.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) typically exhibit a performance profile where reliability degrades as task complexity increases. We address the challenge of generating high-quality natural language execu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GRASP, Generating, Revising, Assessing, Strategic, Planning, Agentic, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30147v1) | [下载PDF](https://arxiv.org/pdf/2609.30147v1.pdf)

---

## [7. EnigmaForge: The Question Is Hidden in the Story](https://arxiv.org/abs/2609.30144v1)

**作者**：Daniel Eisner  
**分类**：cs.AI  
**发布时间**：2026-09-24

### 📄 论文摘要

Most benchmarks hand the model a question. EnigmaForge hands it a stack of old documents and no question at all. Buried in the letters, receipts, and logbook margins is a small logic puzzle whose solution is unique - proved by a SAT solver at generation time, with an ablation certificate showing every clue is load-bearing. Because instances are generated rather than collected, the corpus renews forever. The headline measure is intuition: task success when handed only the story, with world reconstruction as the secondary axis. Twenty-five frontier models ran over 600 instances (17,400 scored records) under three matched conditions. Intuition reshuffles the leaderboard: a 22x spread where fact recovery spans 1.6x, the second-best fact-recoverer ranks fourteenth, one model is indifferent to being told the question, and another is significantly better without it. Several models were blocked by their own content filters before reaching the puzzle - any benchmark scoring refusals as failure is quietly measuring filter behavior.

### 🤖 AI 总结

**一句话总结**：Most benchmarks hand the model a question. EnigmaForge hands it a stack of old documents and no question at all. Buried in the letters, receipts, and logbook margins is a small logic puzzle whose solu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EnigmaForge, Question, Hidden, Story, Most, benchmarks, hand, model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30144v1) | [下载PDF](https://arxiv.org/pdf/2609.30144v1.pdf)

---

## [8. Screen Before You Serve: Simulation for Production Customer Experience AI Agents at 140M Scale](https://arxiv.org/abs/2609.30137v1)

**作者**：Edesio Alcoba, Kevin Rossell, Aman Gupta 等 16 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-09-24

### 📄 论文摘要

Customer experience (CX) agents use tools and large language models to address customer requests and guide conversational interactions with an organization's products. Improving these agents, especially in regulated industries, is difficult: they must detect intent, follow complex operational policies and use tools reliably. Manual end-to-end testing offers limited coverage, while live experiments expose customers to failures that can erode trust.   We present a hypothesis-driven simulation workflow for screening candidate CX agents before deployment. Synthetic customers react to agent responses and simulated tool outputs enable multi-step agentic workflows without invoking production backends. We use the Snowglobe simulator on Nubank's Card Delivery agent and its expanded successor, Card Management - Nubank's highest-volume chat-support agent in Brazil. Across 4 deployed versions, simulated and production version-level binary evaluator scores show high correlation. Simulation-guided iteration increased transactional net promoter score (tNPS) by 36.69 points in a live A/B test. We also screened open-weight configurations in over 16,000 simulated conversations. In a subsequent live A/B test, the selected model increased self-service rate (SSR) by 8.82 percentage points to the highest level observed at Nubank, with no statistically significant change in tNPS. Simulation made broad exploration of models, reasoning settings, and prompts feasible without customer exposure, enabling production improvements that would have been impractical to pursue through live experimentation alone.

### 🤖 AI 总结

**一句话总结**：Customer experience (CX) agents use tools and large language models to address customer requests and guide conversational interactions with an organization's products. Improving these agents, especial...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Screen, Before, Serve, Simulation, Production, Customer, Experience

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30137v1) | [下载PDF](https://arxiv.org/pdf/2609.30137v1.pdf)

---

## [9. PrivDrift: Auditing User-Secret Leakage Under Topic Drift in Active LLM Conversations](https://arxiv.org/abs/2609.30094v1)

**作者**：Luciano Maldonado  
**分类**：cs.AI, cs.CL, cs.CR  
**发布时间**：2026-09-24

### 📄 论文摘要

Large language models increasingly operate as persistent assistants in user-facing, shared-session, and tool-augmented settings. When users disclose sensitive information during an active conversation, that information may remain behaviorally recoverable through later prompts even after the dialogue shifts to unrelated topics. We introduce \textbf{PrivDrift}, a benchmark for auditing whether user-disclosed secrets remain recoverable after conversational topic drift and persuasion-based probing. PrivDrift contains 1{,}000 controlled multi-turn dialogues with seeded secrets, content-dense drift turns, and standardized extraction probes. Across three LLMs with extended context windows, dialogue-level hybrid leakage remains substantial, ranging from 38.7\% to 54.6\%, and varies strongly by model, secret type, and persuasion intensity. Within the tested drift window, additional topic drift does not reliably reduce leakage, suggesting that privacy risk in active LLM contexts should be evaluated as a persistent behavioral failure mode rather than only as training-data memorization or immediate jailbreak behavior.

### 🤖 AI 总结

**一句话总结**：Large language models increasingly operate as persistent assistants in user-facing, shared-session, and tool-augmented settings. When users disclose sensitive information during an active conversation...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PrivDrift, Auditing, User-Secret, Leakage, Under, Topic, Drift, Active

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30094v1) | [下载PDF](https://arxiv.org/pdf/2609.30094v1.pdf)

---

## cs.CL

## [10. JevOut: Natural Context Can Flip Decision Models](https://arxiv.org/abs/2609.30243v1)

**作者**：Zixiang Xu  
**分类**：cs.CL  
**发布时间**：2026-09-24

### 📄 论文摘要

Dedicated decision models such as Jev map unstructured language to probability distributions over finite choices, allowing their outputs to directly route requests, select tools, and trigger actions. Yet real-world inputs rarely arrive in isolation: they come with background details and surrounding context. We find that short additions that fit naturally into this context can nevertheless redirect an otherwise correct decision, even when the correct answer remains unchanged. To study this behavior, we fix a wrong target option for each initially correct item and use the model's option probabilities to refine fluent context additions while preserving the source, question, choices, and gold answer. Within 64 accepted target evaluations, the optimizer identifies contexts that redirect Jev on 312 of 508 initially correct decisions (61.4%); in 229 cases, Jev assigns at least 0.7 probability to the fixed wrong option. Across seven datasets, three additional decision systems show targeted flip rates of 64.9%-73.2% on decisions they initially answer correctly. Taken together, these results expose a pronounced fragility in current decision models: short, ordinary-looking context can shift a correct choice to a high-confidence wrong one. Because these models turn language directly into downstream choices, this sensitivity raises concerns about treating their probability outputs as reliable decision interfaces.

### 🤖 AI 总结

**一句话总结**：Dedicated decision models such as Jev map unstructured language to probability distributions over finite choices, allowing their outputs to directly route requests, select tools, and trigger actions. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：JevOut, Natural, Context, Can, Flip, Decision, Models, Dedicated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30243v1) | [下载PDF](https://arxiv.org/pdf/2609.30243v1.pdf)

---

## [11. ARGUS: Role-Aware Event Knowledge Graphs for U.S. Employment-Discrimination Complaints](https://arxiv.org/abs/2609.30184v1)

**作者**：Sriram Kannan, Swetha Saseendran, Vishnu Vardhan Reddy Kandi 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-24

### 📄 论文摘要

U.S. employment-discrimination complaints describe complex event sequences that are not explicitly captured by lexical or embedding-based representations alone. We present ARGUS, a source-grounded pipeline that combines a 5W1H-inspired schema, legal-domain models, and LLM-based structured generation to construct document-level Event Knowledge Graphs (EKGs) from CourtListener complaints. ARGUS extracts fact-bearing statements, builds chunk-level event graphs with participant, temporal, and causal structure, and merges them into document-level representations. We evaluate graph quality through human and multi-model assessment and test downstream utility on claim classification and legal QA. The graph-structured classifier outperforms raw and linearized baselines on the held-out set, and EKG-only retrieval improves document-scoped QA, while open-retrieval gains remain limited by low first-stage candidate recall. These results suggest that EKGs are most useful for organizing and reasoning over evidence once relevant material has been retrieved.

### 🤖 AI 总结

**一句话总结**：U.S. employment-discrimination complaints describe complex event sequences that are not explicitly captured by lexical or embedding-based representations alone. We present ARGUS, a source-grounded pip...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：U.S, ARGUS, Role-Aware, Event, Knowledge, Graphs, Complaints, describe

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30184v1) | [下载PDF](https://arxiv.org/pdf/2609.30184v1.pdf)

---

## [12. Do Audio Language Models Hear and Read Distinctive Features Alike?](https://arxiv.org/abs/2609.30167v1)

**作者**：Yuanhao Chen, Peter Chin  
**分类**：cs.CL, cs.LG, cs.SD, stat.AP  
**发布时间**：2026-09-24

### 📄 论文摘要

Audio language models pass speech and text through a single decoder. We ask whether that decoder represents a distinctive feature in the same direction when a phoneme is heard and when it is read. For minimal pairs of phonemes differing in one feature, we take the offset between the two members' mean representations. Averaging those offsets gives a direction for each stream, and we measure the cosine between the two. Because the two streams already agree about arbitrary phoneme pairs, we compare every measure against a reference built from random pairings rather than against zero. We apply this to 6 models, 7 features and 15 languages from 11 families. Only voicing in the two Qwen2.5-Omni models exceeds that reference after correction for multiple testing, and the reference varies by a factor of seven between models. In three of the six models, voicing has one direction in audio across the 14 languages with enough minimal pairs to measure it, and every language pair agrees in two of them. The model family, not the model size, predicts which stream represents a feature.

### 🤖 AI 总结

**一句话总结**：Audio language models pass speech and text through a single decoder. We ask whether that decoder represents a distinctive feature in the same direction when a phoneme is heard and when it is read. For...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, Audio, Language, Models, Hear, Read, Distinctive, Features

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30167v1) | [下载PDF](https://arxiv.org/pdf/2609.30167v1.pdf)

---

## [13. What, When, and How: Audio Description as Constrained Global Optimization](https://arxiv.org/abs/2609.30121v1)

**作者**：Igor Sterner, Mirella Lapata, Alex Lascarides 等 4 位作者  
**分类**：cs.CL, cs.CV  
**发布时间**：2026-09-24

### 📄 论文摘要

Audio Description (AD) makes movies accessible to blind and visually impaired audiences by narrating visual information in gaps between dialogue. Existing automatic AD systems largely treat generation as a local video-to-text problem, assuming that the content to describe and its temporal location are already provided. Realistic AD instead requires coupled decisions about what visual information is narratively important, when it can be spoken without interfering with dialogue, and how it should be formulated to fit within the available time. We formalize AD generation as a constrained optimization problem over these three decisions. Our hybrid system uses large language models to propose and ground visual elements, estimate their salience to the narrative, and generate compressed realizations. A mixed-integer linear program then jointly selects and schedules descriptions across a scene subject to temporal constraints. When evaluated on REFRAMED, a benchmark for realistic AD of movies, our approach makes better decisions than prompted LLMs about what to describe and when to describe it, establishing a new SOTA on narrative QA and temporally grounded metrics. Ablations show that explicit temporal constraints drive gains in placement, while salience estimation controls how much narratively useful content is retained. Improvements are concentrated on temporal and narrative measures rather than n-gram overlap, although a significant gap to professional describers remains.

### 🤖 AI 总结

**一句话总结**：Audio Description (AD) makes movies accessible to blind and visually impaired audiences by narrating visual information in gaps between dialogue. Existing automatic AD systems largely treat generation...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, What, When, How, Audio, Constrained, Global, Optimization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30121v1) | [下载PDF](https://arxiv.org/pdf/2609.30121v1.pdf)

---

## [14. Return or Revise? Learning When Revision Helps Retrieval-Augmented QA](https://arxiv.org/abs/2609.30087v1)

**作者**：Nicholas Kashani Motlagh, Tim Anderson, Jeremy Gwinnup 等 4 位作者  
**分类**：cs.CL, cs.IR, cs.LG  
**发布时间**：2026-09-24

### 📄 论文摘要

We consider the decision of whether to return an existing draft answer or revise it using retrieved evidence, as in answer-revision systems. Draft confidence estimates whether the current answer is correct, but the decision requires estimating the effect of a specified revision. For offline training and evaluation, we grade both the returned draft and its candidate revision under the same correctness judge, which makes repair, harm, and the gap to an oracle observable. We call this paired effect its recoverability, and we train policies to predict it before revision. On 25,870 held-out open-domain questions across three revision setups, a scorer trained on the paired outcome has greater area under the accuracy--revision-rate curve than a matched draft-correctness scorer in all nine Llama setup--seed fits, and gains 0.23--0.68 accuracy points on average at development-selected thresholds, a difference significant across training runs only for dense retrieval. The resulting policy improves on always revising and on average closes more than a third of the oracle gap, although it still applies 38--46% of the harmful revisions. When a draft-free standard-RAG answer is also available, however, choosing between the draft and that answer is stronger by about two points for Llama and four for OLMo, and adding candidate revision as a third option yields no significant gain. Recoverability describes one revision; its value as an available action also depends on the alternatives.

### 🤖 AI 总结

**一句话总结**：We consider the decision of whether to return an existing draft answer or revise it using retrieved evidence, as in answer-revision systems. Draft confidence estimates whether the current answer is co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：or, Return, Revise?, Learning, When, Revision, Helps, Retrieval-Augmented

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30087v1) | [下载PDF](https://arxiv.org/pdf/2609.30087v1.pdf)

---

## cs.CV

## [15. Towards Practical Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2609.30245v1)

**作者**：Pengpeng Yu, Yueru Chen, Fei Song 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-24

### 📄 论文摘要

3D Gaussian Splatting (3DGS) enables high-quality novel-view synthesis but requires substantial storage. Existing compression methods often rely on spatial context modeling over irregular 3D representations, increasing the complexity of training and coding. Meanwhile, floating-point context inference can introduce numerical inconsistencies across platforms, causing entropy-decoding failures. To address these practical challenges, we propose COSA-GS, which constructs context without spatial aggregation through anchor-wise causal factorization. Specifically, we use geometry context derived from each anchor's coordinates to model a compact learnable anchor latent. The anchor latent is then fused with the geometry context to form an anchor context for attribute coding. The resulting context model features a simple architecture composed solely of linear transformations and activations. We train COSA-GS using rate--distortion optimization with adaptive Gaussian pruning. Further, we develop quantization-aware training and integer inference for the context model to achieve bit-exact consistency of entropy-decoded symbols across platforms. Experiments demonstrate that COSA-GS achieves state-of-the-art compression performance while retaining fast and consistent cross-platform decoding, providing a simple yet effective framework for practical 3DGS compression. Code is available at https://github.com/pengpeng-yu/COSA-GS.

### 🤖 AI 总结

**一句话总结**：3D Gaussian Splatting (3DGS) enables high-quality novel-view synthesis but requires substantial storage. Existing compression methods often rely on spatial context modeling over irregular 3D represent...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, 3D, Towards, Practical, Compression, Gaussian, Splatting, 3DGS

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30245v1) | [下载PDF](https://arxiv.org/pdf/2609.30245v1.pdf)

---

## [16. OmniFabric: Coherent UV Space Texture Synthesis for 3D Garment Reconstruction](https://arxiv.org/abs/2609.30234v1)

**作者**：Ding-Jiun Huang, Yuanhao Wang, Cheng Zhang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-24

### 📄 论文摘要

Automated generation of production-ready 3D garment assets from a single image is a central challenge in digital content creation. While recent generative models have significantly advanced 3D geometry reconstruction, synthesizing high-quality textures remains a bottleneck. Existing methods often bake environmental illumination and shadows directly into the texture map, or they fail to maintain global structural coherence, making the resulting assets unusable for physical simulation and relighting. In this work, we introduce OmniFabric, a novel approach that synthesizes globally coherent texture maps directly within the 2D sewing pattern space. Given a single reference image, our pipeline utilizes an estimated 3D mesh and generative priors of powerful Vision-Language Models (VLM) to establish a complete but coarse texture initialization across the unwrapped sewing patterns. We then leverage a specialized diffusion transformer, trained via an automated synthetic data engine and conditioned on 3D positional features, to refine this initialization directly in the canonical UV domain. This effectively removes distortion and baked-in artifacts to extract a clean and normalized texture map that preserves the original garment design. Extensive experiments demonstrate that OmniFabric significantly outperforms state-of-the-art baselines, yielding photorealistic 3D garments with high-quality textures.

### 🤖 AI 总结

**一句话总结**：Automated generation of production-ready 3D garment assets from a single image is a central challenge in digital content creation. While recent generative models have significantly advanced 3D geometr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UV, 3D, OmniFabric, Coherent, Space, Texture, Synthesis, Garment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30234v1) | [下载PDF](https://arxiv.org/pdf/2609.30234v1.pdf)

---

## [17. BiCC: Bidirectional Connected-Component Loss for Instance-Aware Segmentation](https://arxiv.org/abs/2609.30223v1)

**作者**：Luc Bouteille, Frederic Jonske, Jens Kleesiek 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-24

### 📄 论文摘要

Common segmentation losses aggregate errors voxel-wise, so lesions influence the objective in proportion to their volume, giving small but clinically critical lesions disproportionately little weight. Instance-aware losses aim to address this mismatch by assigning each lesion its own term. However, blob loss and CC-DiceCE derive their regions solely from annotations, so false-positive components receive no instance-level term. This matters in computer-assisted review, where each false-positive component may require separate inspection, making precision and false-positive burden important alongside recall. We introduce the bidirectional connected-component loss (BiCC), which pairs annotation- and prediction-derived partitions to score predicted components on their own scale. By deriving instances from the predictions, this branch directly penalizes false-positive components regardless of their size. The balance parameter $α$ allows control over the lesion-wise precision-recall trade-off. Across five datasets with five-fold cross-validation using nnU-Net, BiCC outperforms CC-DiceCE in lesion-wise F1 on four datasets and blob loss on all five. It significantly improves over DiceCE on three datasets and matches it on two; CC-DiceCE instead loses up to 0.363 precision by favoring recall. Code is available at https://github.com/TIO-IKIM/BiCC-Loss.

### 🤖 AI 总结

**一句话总结**：Common segmentation losses aggregate errors voxel-wise, so lesions influence the objective in proportion to their volume, giving small but clinically critical lesions disproportionately little weight....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BiCC, Bidirectional, Connected-Component, Loss, Instance-Aware, Segmentation, Common, losses

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30223v1) | [下载PDF](https://arxiv.org/pdf/2609.30223v1.pdf)

---

## [18. TrackEverything: Long Horizon Dense Tracking via De-Duplicating 3D Scene Representations](https://arxiv.org/abs/2609.30222v1)

**作者**：Ayush Jain, Sreeharsha Paruchuri, Ishita Gupta 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.RO  
**发布时间**：2026-09-24

### 📄 论文摘要

Existing point tracking models face a fundamental tradeoff: they can either track a sparse set of query points over long horizons, or track all points across only short clips. We introduce TrackEverything, a 3D point tracker that breaks this trade-off by representing videos as persistent 3D scene tracks in world coordinates. Grounded in the insight that videos are 2D projections of an underlying 3D world, TrackEverything decouples model complexity from video duration, allowing it to scale with unique physical scene geometry instead. Our approach introduces three key innovations. First, we employ a voxelization-based de-duplication mechanism at sliding-window boundaries to merge co-located tracks, preventing repeated observations of the same surface from redundantly accumulating. Second, we decompose tracking into an endpoint refiner that predicts each point's destination and static-versus-dynamic classification, followed by a lightweight trajectory refiner that decodes dense trajectories exclusively for dynamic points. Third, we propose 3D WAFT, replacing memory-prohibitive 4D correlation volumes with efficient feature sampling in the scene cloud. To the best of our knowledge, TrackEverything is the first 3D tracker capable of tracking all visible points across videos exceeding 1000 frames within 40 GB of GPU memory. On TAPVid-3D, TrackEverything outperforms all open-source all-frame dense 3D trackers by more than 20% APD on short clips, while remaining competitive with state-of-the-art sparse trackers on long sequences, despite tracking far more points.

### 🤖 AI 总结

**一句话总结**：Existing point tracking models face a fundamental tradeoff: they can either track a sparse set of query points over long horizons, or track all points across only short clips. We introduce TrackEveryt...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, TrackEverything, Long, Horizon, Dense, Tracking, via, De-Duplicating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30222v1) | [下载PDF](https://arxiv.org/pdf/2609.30222v1.pdf)

---

## [19. WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation](https://arxiv.org/abs/2609.30221v1)

**作者**：Yubo Zhu, Yawen Shao, Ziyun Dai 等 30 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-24

### 📄 论文摘要

Video generation begins in text space by authoring a cinematic screenplay, then materializes into pixels. As contemporary video generators scale to 30 seconds and faithfully follow complex conditions, the textual prompt largely directs the production, planning how actions, camera trajectories, lighting, and sound unfold across multi-shot sequences. In this paper, we present WanPE, a 397B-parameter prompt enhancement model trained on 1.05M real-world videos to master director-level cinematic planning. WanPE formulates shot-level cinematic plans via video-grounded reverse construction and employs Semantic-Consistency GRPO (SC-GRPO) to faithfully preserve user requirements across shots and over time. To benchmark this capability, we curate WanPEval, a human-annotated testbed covering durations from 5 to 30 seconds across varying intent granularities, supported by approximately 11K blind pairwise assessments. When powering Wan3.0's video generator, WanPE-397B boosts human preference over raw user prompts by 10.66-18.84 points at 5-15 seconds and by a dramatic 50.86 points in the 30-second arena. Ablation studies show that reverse construction demonstrates clear superiority over forward rewriting, while SC-GRPO robustly preserves semantic fidelity across model scales. Ultimately, WanPE leads all evaluated commercial offerings at 5-15 seconds and remains competitive with Seedance 2.5 at 30 seconds.

### 🤖 AI 总结

**一句话总结**：Video generation begins in text space by authoring a cinematic screenplay, then materializes into pixels. As contemporary video generators scale to 30 seconds and faithfully follow complex conditions,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：WanPE, Towards, Cinematic, Prompt, Enhancement, Modern, Text-to-Video, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30221v1) | [下载PDF](https://arxiv.org/pdf/2609.30221v1.pdf)

---

## [20. Ego-Exo4D Human Meshes Dataset: 4D Human Motion Reconstruction for Ego-Exo Captures](https://arxiv.org/abs/2609.30187v1)

**作者**：Abhiram Maddukuri, Georgios Pavlakos  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-09-24

### 📄 论文摘要

Ego-Exo4D is a large-scale dataset providing synchronized egocentric and multi-view exocentric video, a rich resource for skill learning and assessment, procedural activity understanding, and embodied AI. However, the dataset ships with only sparse 3D human pose annotations, and reconstructing dense human motion from its multi-view captures is nontrivial. To this end, we present Ego-Exo4D-HM, a large-scale dataset of 4D human motion reconstructions for Ego-Exo4D's captures, and release the accompanying reconstruction pipeline. The code, dataset, and documentation can be found at https://abhiram824.github.io/egoexo4d_human_meshes.

### 🤖 AI 总结

**一句话总结**：Ego-Exo4D is a large-scale dataset providing synchronized egocentric and multi-view exocentric video, a rich resource for skill learning and assessment, procedural activity understanding, and embodied...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, Ego-Exo4D, Human, Meshes, Dataset, Motion, Reconstruction, Ego-Exo

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30187v1) | [下载PDF](https://arxiv.org/pdf/2609.30187v1.pdf)

---

## [21. Multimodal Thinking with Renderable Programs](https://arxiv.org/abs/2609.30130v1)

**作者**：Sunli Chen, Ding Zhong, Ziqiao Ma 等 9 位作者  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-09-24

### 📄 论文摘要

Current vision-language models (VLMs) excel at visual content understanding and text-based reasoning, yet their structure limits the advancement of incorporating images into the reasoning chain. Though Omnimodal models have made efforts in unifying text and image generation, they focus on visual tasks in the open-domain, lacking tractability due to rasterized or latent representations of images. We introduce SVGLM, a framework that uses scalable vector graphics (SVG) primitives to connect text and image in reasoning tasks. We exploit the duality of SVG as both image description and text instructions, yielding a more compact, interpretable solution to equip general VLMs with the capability of generating images within the reasoning process. We provide a large curated dataset of SVG-based image editing dataset, as well as the paradigm to tune open-source VLMs. Experiments on a mathematical reasoning benchmark demonstrate that SVGLM achieves strong SVG generation power as well as think-with-image intelligence. Our results highlight SVG as a suitable medium for building more robust digital domain agents, bridging the gap between text-based thinking and pixel-based images.

### 🤖 AI 总结

**一句话总结**：Current vision-language models (VLMs) excel at visual content understanding and text-based reasoning, yet their structure limits the advancement of incorporating images into the reasoning chain. Thoug...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multimodal, Thinking, Renderable, Programs, Current, vision-language, models, VLMs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30130v1) | [下载PDF](https://arxiv.org/pdf/2609.30130v1.pdf)

---

## [22. Accelerating Video Diffusion via Training-Free Trajectory Routing](https://arxiv.org/abs/2609.30096v1)

**作者**：Mustafa Munir, Huy Vu, Shreyas Misra 等 10 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-09-24

### 📄 论文摘要

Video diffusion is computationally expensive, as it requires executing a large model across many denoising steps. Even with step-distillation, inference remains expensive because every distilled step still requires a costly model evaluation. We present TRACK: TRajectory-Aware Capacity routing via top-K selection, a heterogeneous denoising strategy that switches between compatible large and small models at selected steps, reducing the average cost per denoising evaluation. The switching steps are determined using a calibration process. TRACK first rolls out a reference trajectory with the large model. Then at each step, the small model's prediction is also collected and compared against the large model's prediction to obtain a relative disagreement score. Both models receive the same latent, timestep, conditioning, and guidance inputs. Aggregating this signal over a calibration set produces a disagreement score map across diffusion steps, which determines a switching policy for an efficient inference process: quality-sensitive steps keep using the large model, while steps with low disagreement scores are routed to the small model. Inference executes only the selected model at each step, requiring no retraining, architecture or scheduler changes, or online dual-model evaluation. Across Wan 2.1, Cosmos 3, TurboDiffusion, and FastVideo, TRACK yields $1.95\times$, $2.04\times$-$2.73\times$, $2.69\times$, and $2.17\times$ speedups, respectively, with comparable aggregate quality and high diversity retention. TRACK thereby establishes automated, training-free model switching as a practical acceleration paradigm for video diffusion.

### 🤖 AI 总结

**一句话总结**：Video diffusion is computationally expensive, as it requires executing a large model across many denoising steps. Even with step-distillation, inference remains expensive because every distilled step ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Accelerating, Video, via, Training-Free, Trajectory, Routing, computationally

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30096v1) | [下载PDF](https://arxiv.org/pdf/2609.30096v1.pdf)

---

## cs.LG

## [23. Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied Reinforcement Learning](https://arxiv.org/abs/2609.30258v1)

**作者**：Sudip Bhujel, Shanghao Shi, Ruiquan Huang 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-24

### 📄 论文摘要

Distributed learning in embodied reinforcement-learning agents offers a degree of privacy by retaining raw sensor data on-device and transmitting only policy gradients to the server. Yet temporal structure can amplify this leakage beyond single-frame attacks. We introduce Temporal Reconstruction Attack on Consecutive Encodings (TRACE), an amortized temporal gradient-inversion attack that autoregressively reconstructs the sequence of private observation-action trajectories from per-step policy-learning gradients. The attack exploits two structural signals ignored by prior single-frame methods: (i) cross-time correlation between successive embodied gradients, which we formalize via a conditional mutual-information bound, and (ii) closed-form action recovery from policy-head gradient structure, which we prove exact when standard entropy regularization is sufficiently small. On held-out embodied scenes, TRACE reaches $18.8$ dB PSNR with near-perfect action recovery at $3$-$4.5$ ms per reconstructed frame, dominating the learning-based baseline across all reconstruction metrics and exceeding optimization attacks while running orders of magnitude faster. Further evaluation demonstrates TRACE's broader applicability across recurrent, residual, and compact transformer victim architectures, multi-modal inputs, and larger discrete action spaces. Defense experiments suggest that protecting temporal gradient streams may require sequence-aware privacy mechanisms.

### 🤖 AI 总结

**一句话总结**：Distributed learning in embodied reinforcement-learning agents offers a degree of privacy by retaining raw sensor data on-device and transmitting only policy gradients to the server. Yet temporal stru...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Temporal, Gradient, Inversion, Private, Trajectory, Reconstruction, Embodied, Reinforcement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30258v1) | [下载PDF](https://arxiv.org/pdf/2609.30258v1.pdf)

---

## [24. To Trust or Not to Trust: Retrieval-Augmented Fact Checking in Speech](https://arxiv.org/abs/2609.30227v1)

**作者**：Debajyoti Mazumder, Mamta, Abhirama Subramanyam Penamakuri  
**分类**：cs.LG, cs.AI, cs.CL, cs.SD  
**发布时间**：2026-09-24

### 📄 论文摘要

Online misinformation increasingly appears in spoken formats such as news clips, podcasts, interviews, political speeches, and social media videos, creating a need for fact-checking systems that can verify claims directly from speech. We introduce VeriSpeak, a probe benchmark for studying speech-based fact verification in Large Audio Language Models (LALMs). VeriSpeak contains 3,879 spoken claims spanning temporal, geographical, and relational facts, with balanced true and false labels. The benchmark is designed to examine whether factual verification ability transfers from text to speech, and whether retrieval-augmented LALMs can use textual evidence to correctly support or refute spoken claims. Our experiments reveal a consistent text-speech modality gap: LALMs that verify written claims reliably often fail on the same claims when spoken. Moreover, retrieval alone provides limited gains because models frequently conflate retrieved evidence with the spoken claim. In contrast, retrieval combined with explicit reasoning improves claim-evidence comparison, with a thinking-tuned LALM reaching 86.1% accuracy. VeriSpeak highlights that effective speech misinformation detection requires not only speech understanding, but also grounded reasoning over retrieved evidence. The dataset is publicly available via Hugging Face at https://huggingface.co/datasets/abhiram4572/VeriSpeak.

### 🤖 AI 总结

**一句话总结**：Online misinformation increasingly appears in spoken formats such as news clips, podcasts, interviews, political speeches, and social media videos, creating a need for fact-checking systems that can v...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：or, Trust, Not, Retrieval-Augmented, Fact, Checking, Speech, Online

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30227v1) | [下载PDF](https://arxiv.org/pdf/2609.30227v1.pdf)

---

## [25. PoEM: Predicting RL Outcomes from Existing Policies](https://arxiv.org/abs/2609.30226v1)

**作者**：Kimia Hamidieh, Giannis Daras, Antonio Torralba  
**分类**：cs.LG, cs.AI, cs.CL, cs.CV  
**发布时间**：2026-09-24

### 📄 论文摘要

Foundation models are post-trained with reinforcement learning (RL) to maximize specific rewards, such as human alignment, correctness, or instruction following. This post-training process is computationally intensive, sometimes unstable, and has to be run from scratch every time the reward model changes or when we want to combine multiple rewards. We hence ask: given a new reward function, is it possible to predict the RL outcomes without actually running RL on it? We answer this in the affirmative by introducing PoEM, a framework to predict the outputs of RL on a new reward function using a set of models already post-trained on other rewards. First, we show that if the new reward function can be written as a linear combination of existing ones, then the new policy in log-space can be written as a linear combination of the existing log-policies. Surprisingly, even in cases where the rewards are not linearly connected, we observe that often log-policies from RL training span an approximately low-rank subspace across rewards. To our benefit, the weighting coefficients for this combination can be estimated using only the reward or basis policy outputs on the samples. We turn these observations into an algorithm that takes post-trained models and a new reward function, and approximates the target RL policy without actually running any additional RL training. We experimentally validate our approach across synthetic and real rewards, spanning both text and image modalities.

### 🤖 AI 总结

**一句话总结**：Foundation models are post-trained with reinforcement learning (RL) to maximize specific rewards, such as human alignment, correctness, or instruction following. This post-training process is computat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, PoEM, Predicting, Outcomes, Existing, Policies, Foundation, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30226v1) | [下载PDF](https://arxiv.org/pdf/2609.30226v1.pdf)

---

## [26. Beyond Compression: Training Latent Representations for Stable Long-Horizon Rollout in Neural Surrogate Solvers](https://arxiv.org/abs/2609.30198v1)

**作者**：Andreas E. Robertson, Ashley T. Lenau, John D. Shimanek 等 8 位作者  
**分类**：cs.LG, cond-mat.mtrl-sci, cs.CE  
**发布时间**：2026-09-24

### 📄 论文摘要

Latent neural surrogate solvers, or latent dynamics models, accelerate simulations of time-dependent physical systems by evolving a compressed latent space rather than resolving full-resolution fields directly. In principle this reduces computational cost and simplifies learning, but in practice errors often accumulate rapidly during long autoregressive rollouts, limiting predictive utility. We show that this instability does not stem from the latent representation itself, but arises when it is trained solely for reconstruction, producing representations poorly suited to long-horizon forecasting. We systematically evaluate training-level interventions that align latent representations with long-horizon rollout: Koopman operator learning and Hamming noise injection during autoencoder training to improve compression, together with noise injection and multi-step rollout fine-tuning to improve dynamics. Interventions that improve long-horizon rollout stability often degrade conventional training metrics, including reconstruction and one-step prediction accuracy. Collectively, these interventions reduce long-rollout error by approximately 40\% and match or exceed the accuracy of full-resolution models on two physics benchmarks, while requiring 2 orders of magnitude fewer floating point operations and half the GPU memory. Applied to mesoscale crystal-plasticity simulations of high-cycle fatigue, the resulting surrogate achieves stable extrapolation over horizons orders of magnitude beyond those observed during training. More broadly, these results show that neural compression should be designed not merely to reduce dimensionality, but to restructure the solution space for stable dynamical evolution, a key requirement for reliable, efficient neural surrogates in scientific applications.

### 🤖 AI 总结

**一句话总结**：Latent neural surrogate solvers, or latent dynamics models, accelerate simulations of time-dependent physical systems by evolving a compressed latent space rather than resolving full-resolution fields...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Compression, Training, Latent, Representations, Stable, Long-Horizon, Rollout

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30198v1) | [下载PDF](https://arxiv.org/pdf/2609.30198v1.pdf)

---

## [27. Intrinsic-Extrinsic Coupling in Learning Dynamics](https://arxiv.org/abs/2609.30185v1)

**作者**：Qinyou Wang  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-09-24

### 📄 论文摘要

A learner's current observations need not determine its response to further training. We formulate intrinsic-extrinsic coupling through the continuation-conditioned value of a constrained learning-state intervention, with observation-relative fibers describing present agreement. An executable finite-frame classifier-head write protects current logits while repairing specified historical margins under finite-precision acceptance checks. We distinguish local admissibility, continuation-conditioned intervention value, and complete-policy performance. A matched four-cell contrast identifies readout-specific non-additivity between the same intrinsic intervention and alternative external continuations. In a CLINC-derived class-incremental setting, replay changes the write's 32-update contribution from five correct predictions to zero. Nonzero interactions also occur under output distillation, with a RoBERTa backbone, and under optimizer-native SGDW dynamics. Under SGDW, correct-count interactions are negative in all three activated roots at 128 updates, showing that coupling need not imply positive synergy. The mathematical analysis distinguishes feasible local repairs and favorable terminal outputs from training-reachable repair regions. Separate coordination tests show that content controls match or exceed the development gain, while a five-root fresh-test comparison with Fiber present in every arm shows root-dependent rather than uniformly beneficial correct-count effects. On the secondary cross-entropy readout, guided allocation yields lower mean loss than standard replay in all five pairs. Together, these results make intrinsic-extrinsic coupling operational by connecting executable state geometry to continuation-conditioned value, matched interaction identification, and closed-loop coordination, while separating identified coupling from complete-policy performance.

### 🤖 AI 总结

**一句话总结**：A learner's current observations need not determine its response to further training. We formulate intrinsic-extrinsic coupling through the continuation-conditioned value of a constrained learning-sta...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Intrinsic-Extrinsic, Coupling, Learning, Dynamics, learner's, current, observations, need

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30185v1) | [下载PDF](https://arxiv.org/pdf/2609.30185v1.pdf)

---

## [28. Graph-Based Inference and Topology-Aware Multi-Agent Reinforcement Learning for Large-Scale Railway Network Management](https://arxiv.org/abs/2609.30150v1)

**作者**：Giacomo Arcieri, Gregory Duthé, Christophe Muller 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-24

### 📄 论文摘要

Modern infrastructure asset management constitutes a complex sequential decision-making problem, characterized by long planning horizons and system-level interactions, such as spatial deterioration correlations and economies of scale. While deep reinforcement learning has shown promise in optimizing maintenance policies, scaling to real-world networks remains challenging. Centralized approaches become computationally intractable in large-scale systems, whereas decentralized approaches often fail to capture essential coordination mechanisms. To address these challenges, we propose a graph-based framework that integrates accurate environment modeling with scalable decision support. First, we employ a hierarchical Bayesian model leveraging a Gaussian Process on Graph kernel to infer a realistic, spatially correlated networked environment of railway maintenance planning from real-world data provided by the Swiss Federal Railways. Second, we introduce a topology-aware Multi-Agent Reinforcement Learning (MARL) framework by integrating graph neural networks and graph Transformers to optimize network-level policies. A central contribution of this work is the demonstration of scalability through zero-shot transfer learning: graph-based agents, trained only on small network portions, are successfully deployed in a zero-shot manner on large-scale unseen networks without any retraining. Numerical results indicate that the proposed method significantly outperforms optimized heuristics and standard MARL baselines, reducing computational training time while maintaining superior performance on large-scale networks.

### 🤖 AI 总结

**一句话总结**：Modern infrastructure asset management constitutes a complex sequential decision-making problem, characterized by long planning horizons and system-level interactions, such as spatial deterioration co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, Graph-Based, Inference, Topology-Aware, Reinforcement, Learning, Large-Scale, Railway

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30150v1) | [下载PDF](https://arxiv.org/pdf/2609.30150v1.pdf)

---

## [29. On the SoS Certifiability of Log-Concave Distributions](https://arxiv.org/abs/2609.30105v1)

**作者**：Aleksandr Storozhenko  
**分类**：cs.LG, cs.CC, math.PR  
**发布时间**：2026-09-24

### 📄 论文摘要

For an arbitrary isotropic log-concave distribution $P$ on $\mathbb{R}^d$, we prove that the polynomial $(Cm)^m\|v\|_2^m - \mathbb{E}_{X\sim P}\langle X,v\rangle^m$ is a sum of squares for every even $m\ge2$, where $C>0$ is a universal constant. This removes the dependence on the Poincaré constant in the theorem of Kothari and Steinhardt (arXiv:1711.07465), recovering the optimal moment bounds for log-concave distributions. As an immediate corollary, we obtain computationally efficient algorithms with dimension-free error guarantees for a wide range of high-dimensional statistical estimation problems.   Our proof uses stochastic localization to decompose $P$ as an average of random strongly log-concave measures, whose centered moments admit the subgaussian certificates of Diakonikolas, Hopkins, Pensia, and Tiegel (STOC 2025; arXiv:2410.21194). With a covariance-adapted choice of localization, we show that a fourth-moment certificate derived from Letwin's variance inequality for quadratic forms (arXiv:2607.24164) suffices to control this averaging at every even degree.

### 🤖 AI 总结

**一句话总结**：For an arbitrary isotropic log-concave distribution $P$ on $\mathbb{R}^d$, we prove that the polynomial $(Cm)^m\|v\|_2^m - \mathbb{E}_{X\sim P}\langle X,v\rangle^m$ is a sum of squares for every even ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, an, SoS, Certifiability, Log-Concave, Distributions, arbitrary, isotropic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30105v1) | [下载PDF](https://arxiv.org/pdf/2609.30105v1.pdf)

---

## [30. AT-SKM-Net: An Accelerated Trainable Sampling Kaczmarz-Motzkin Framework for Linear Hard-Constraint Feasibility on Dynamic Graphs](https://arxiv.org/abs/2609.30088v1)

**作者**：Xiaochen Zhang, Haoyu Zhu, Yao Zhang 等 4 位作者  
**分类**：cs.LG, cs.AI, math.OC  
**发布时间**：2026-09-24

### 📄 论文摘要

Graph-structured optimization with linear constraints is fundamental to critical infrastructure but faces scalability limits due to massive strict hard constraints and high dimensionality. While recent projection-based methods such as Trainable Sampling Kaczmarz-Motzkin Net (T-SKM-Net) guarantee feasibility, they face high computational costs in dynamic environments by processing the entire constraint set and requiring expensive matrix factorizations. To bridge this gap, we propose the Accelerated Trainable-SKM (AT-SKM) Net framework. To concentrate computation on the active constraints and eliminate redundant calculations, we introduce a hybrid sampling strategy guided by a topology-aware heterogeneous GNN model. To efficiently handle topological shifts in graph-based constraints, we employ a Cholesky Update mechanism that theoretically reduces the equality projection complexity from O(N^3) to O(N^2) under low-rank perturbations. Experiments on random geometric graphs, N-1 Security-Constrained DC-OPF, and minimum-cost gas transport problem demonstrate that AT-SKM reduces iteration counts by up to 85% and achieves 2.95x-7.29x SKM layer speedups, while maintaining zero constraint violations.

### 🤖 AI 总结

**一句话总结**：Graph-structured optimization with linear constraints is fundamental to critical infrastructure but faces scalability limits due to massive strict hard constraints and high dimensionality. While recen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, AT-SKM-Net, Accelerated, Trainable, Sampling, Kaczmarz-Motzkin, Framework, Linear

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.30088v1) | [下载PDF](https://arxiv.org/pdf/2609.30088v1.pdf)

---

