# arXiv AI 论文日报 | 2026-10-22

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (6 篇)
- [cs.CV](#csCV) (8 篇)
- [cs.LG](#csLG) (11 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. Charts as Epistemic Actions for Experience-Driven Agentic Data Analysis](https://arxiv.org/abs/2610.30072v1)

**作者**：Xinzhe Wang, Xudong Weng, Zang Li 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-21

### 📄 论文摘要

Data agents built on ReAct-style loops now execute complex analytical workflows over structured data, yet their intermediate reasoning still runs almost entirely through text. Human analysts instead move between numbers, tables, and charts, reading visual evidence to expose trends and anomalies that text summaries drop. We ask whether charts can serve as internal epistemic actions inside a data agent's reasoning loop, and how to teach an agent to use them. We first build \probe{}, a suite of 200 controlled tasks under four matched interface conditions, and find a persistent gap between what agents can read and what they choose to use. Agents score as well from self-generated charts as from numeric output, yet plotting access alone does not translate into consistent use. Task slices show that charts lead on temporal, pattern, and anomaly reasoning, while text leads on precise reading and conditional verification. We then propose \method{}, which distils two families of experience from conditioned trajectory rollouts. One family records how to select and verify analytical operations, and the other records when to invoke text, charts, or both. A trajectory judge scores outcomes and labels intermediate steps, and a validation gate admits only experience that improves held-out performance. On three held-out benchmarks with four LLM backbones, \method{} raises analytical accuracy and visual evidence quality over matched baselines, and backbones that never drew charts begin using them, all without touching model parameters.

### 🤖 AI 总结

**一句话总结**：Data agents built on ReAct-style loops now execute complex analytical workflows over structured data, yet their intermediate reasoning still runs almost entirely through text. Human analysts instead m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Charts, Epistemic, Actions, Experience-Driven, Agentic, Data, Analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30072v1) | [下载PDF](https://arxiv.org/pdf/2610.30072v1.pdf)

---

## [2. Which Differences Matter? Controlled Tests of Rule Transfer, Joint Reliability, and Information Use in Decision Models](https://arxiv.org/abs/2610.30045v1)

**作者**：Tianyou Lai, Wentao Yue, Zhiwei Zuo 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-21

### 📄 论文摘要

Decision models map stated rules and observed states to discrete answers. Aggregate accuracy leaves unresolved which rule and information changes guide those answers. We connect controlled input changes to transfer, joint reliability, and directed information use through executable arithmetic rules. Semantic rule separation and crossed rule and state tests make transfer and joint success separately measurable. We compare equivalent wordings, calibrate joint correctness through marginal-preserving reassociation, and alter tables to define alternative answer targets. Adaptation gains increase with nearest-source answer agreement; fully conflicting quartets yield small pooled gains and different gain signs across source splits. Equivalent rewrites have opposing task-level effects, linking transfer gains to rule presentation. Joint-score departures depend on which rule and state associations the reference preserves. A decision service changes answers more across equivalent wordings than across identical-text repeats and usually follows the answer targets implied by altered table values or mappings.

### 🤖 AI 总结

**一句话总结**：Decision models map stated rules and observed states to discrete answers. Aggregate accuracy leaves unresolved which rule and information changes guide those answers. We connect controlled input chang...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Which, Differences, Matter?, Controlled, Tests, Rule, Transfer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30045v1) | [下载PDF](https://arxiv.org/pdf/2610.30045v1.pdf)

---

## [3. HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning](https://arxiv.org/abs/2610.30042v1)

**作者**：Sudipta Paul, Pengrui Quan, Aounon Kumar 等 6 位作者  
**分类**：cs.AI, cs.LG, cs.NE  
**发布时间**：2026-10-21

### 📄 论文摘要

Harness optimization, which improves an agent's prompts, tools, and workflows, is an increasingly effective way to enhance agents built on frozen or closed-source LLMs. Leading approaches such as the Darwin--Godel Machine and the Huxley--Godel Machine (HGM) rely on recursive self-improvement and were developed mainly for coding, where the competence needed to improve the agent coincides with the competence being improved. Planning tasks, in which an agent must produce a sequence of tool calls that jointly satisfies interacting constraints, break this alignment. There, open-ended self-modification repeatedly explores ineffective changes and consumes substantial evaluation budgets. We introduce HGM-Dual, a diagnostic-guided framework for budget-efficient harness evolution for planning agents. First, HGM-Dual represents agent evolution as lineage-aware context. This context records what each ancestor changed, which behaviors improved or regressed, and which modifications were ineffective, giving the editor explicit edit-outcome attribution instead of an unstructured archive of past agents. Second, HGM-Dual introduces error-conditioned dual-path child generation. For each selected parent, it generates a general child that preserves open-ended exploration and specialized children that target the harness components most likely responsible for the parent's highest-ranked constraint violations. HGM-Dual outperforms the strongest baseline by up to 14.45% relative improvement in case accuracy while matching HGM variants' final performance with 2x-4x fewer evaluation budget.

### 🤖 AI 总结

**一句话总结**：Harness optimization, which improves an agent's prompts, tools, and workflows, is an increasingly effective way to enhance agents built on frozen or closed-source LLMs. Leading approaches such as the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, HGM-Dual, Lineage-Aware, Guided, Harness, Optimization, Long-Horizon, Planning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30042v1) | [下载PDF](https://arxiv.org/pdf/2610.30042v1.pdf)

---

## [4. GuideEvolve: Self-Evolving Agent Framework with Expert Guidance and 3Ts Mechanisms](https://arxiv.org/abs/2610.30017v1)

**作者**：Meihong Jia, Yasemin Timar, Jonathan Taws  
**分类**：cs.AI  
**发布时间**：2026-10-21

### 📄 论文摘要

This study introduces GuideEvolve, a self-evolving agent framework incorporating expert guidance and three autonomous regulatory mechanisms, collectively termed the 3Ts: Think Fast and Slow, Throwback, and Termination by choice. The framework addresses critical limitations in extant self-evolving agent paradigms through dual innovations: (1) a task-specific expert-evaluation-driven evolutionary pipeline, and (2) the integration of 3Ts mechanisms to facilitate cognitive optimization, performance recovery via temporal rollback, and adaptive termination protocols. Empirical validation across the MGSM and MMLU benchmarks demonstrates that GuideEvolve attains performance metrics comparable to current state-of-the-art models (89.8% accuracy versus Gödel Agent's 90.6% on MGSM; 89.1% versus 87.9% on MMLU), while exhibiting notably reduced variance (25-59%) and enhanced robustness. Furthermore, the framework achieves a 100% evolution success rate, superior to the baseline's 82%, diminishes required optimization iterations by approximately 50% (from 30 iterations in baseline to 15.1 and 13.4 across tasks), and provides improved stability for production deployment.

### 🤖 AI 总结

**一句话总结**：This study introduces GuideEvolve, a self-evolving agent framework incorporating expert guidance and three autonomous regulatory mechanisms, collectively termed the 3Ts: Think Fast and Slow, Throwback...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, 3Ts, GuideEvolve, Self-Evolving, Framework, Expert, Guidance, Mechanisms

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30017v1) | [下载PDF](https://arxiv.org/pdf/2610.30017v1.pdf)

---

## [5. TIDE: Tree-Induced Fine-Grained Diagnostic Evaluation from Model Behaviors](https://arxiv.org/abs/2610.29985v1)

**作者**：Jiayi Chen, Hui Li, Yujiong Shen 等 15 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-10-21

### 📄 论文摘要

Benchmark performance is the dominant standard for comparing large language models (LLMs), typically summarized by a single aggregate score, such as accuracy, pass rate, or rubric score. This aggregate score provides limited information about a model's underlying capabilities, yet understanding these capabilities is crucial for model development and evaluation. To this end, we propose Tree-Induced Diagnostic Evaluation (TIDE), which recasts diagnostic evaluation as behavior-driven decision-tree induction to perform fine-grained capability diagnosis. TIDE recursively builds a hierarchical capability tree from benchmark samples and model scores: at each node, an LLM judge proposes candidate splits and performs sample-to-group classification, and behavior-based information gain selects among them. We apply TIDE to five models across four benchmarks to demonstrate its effectiveness, and find fine-grained capability contrasts invisible at the aggregate level: Claude Opus 4.6 achieves 100% on microeconomic market reasoning where GPT-5.4 scores 83.3%, but trails GPT-5.4 on contract law reasoning with 77.8% versus 88.9%. We hope TIDE can be extended to past and future benchmarks so that the rich behavioral signal in evaluation results is fully leveraged for understanding model capabilities.

### 🤖 AI 总结

**一句话总结**：Benchmark performance is the dominant standard for comparing large language models (LLMs), typically summarized by a single aggregate score, such as accuracy, pass rate, or rubric score. This aggregat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TIDE, Tree-Induced, Fine-Grained, Diagnostic, Evaluation, Model, Behaviors, Benchmark

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.29985v1) | [下载PDF](https://arxiv.org/pdf/2610.29985v1.pdf)

---

## cs.CL

## [6. LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data](https://arxiv.org/abs/2610.30132v1)

**作者**：Zhennan Wan, Jianfei Chen  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-10-21

### 📄 论文摘要

Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable. Human annotation of such data is expensive, naturally occurring data are too scarce to sustain RL, and existing synthesis methods depend on external corpora or stronger teacher models, which become harder to obtain as the trained models get stronger. Recently, RL from zero data, in which a model learns from tasks it proposes itself, has achieved excellent performance, but existing methods target short-context tasks. Therefore, we propose $\textbf{LongZero}$, a method that lets an LLM improve its own long-context reasoning without any external data. Instead of writing questions and answers over existing documents, LongZero first has the model synthesize the question and answer with its supporting evidence in a compact structured form, and only then separately expands the evidence into a long multi-document context. LongZero combines these self-written multi-hop reasoning tasks with self-written multi-round retrieval tasks and trains the model with GRPO. We evaluate LongZero on two LLMs across five long-context reasoning benchmarks and compare it with RL on data synthesized from external corpora. Experimental results show that LongZero can generalize to real tasks, and outperforms both baselines, suggesting a viable and promising path to improving long-context reasoning of LLMs.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, LongZero, Enhancing, Long-Context, Reasoning, Zero, Data, Reinforcement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30132v1) | [下载PDF](https://arxiv.org/pdf/2610.30132v1.pdf)

---

## [7. Environment Duels: A Microcosm of LLM Co-Evolution](https://arxiv.org/abs/2610.30116v1)

**作者**：Shibo Jin, Zhiqiu Xu, Yiling Zou 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-10-21

### 📄 论文摘要

Through a tangle of real-world interactions, from synthetic training pipelines to data shared on the open web, frontier LLMs absorb what their predecessors and competitors create. How well does each model play its role in this ecosystem, as a creator and as a solver? We introduce Environment Duels, a dynamic agentic benchmark that evaluates both capabilities on interactive environments. Each model writes environments, each with a privileged hint, aiming for tasks that capable solvers fail without the hint and pass with it. Across nine frontier LLMs, solving and authoring prove to be distinct skills: the strongest solvers are not the strongest authors, while smaller models learn more from how others played and write the hardest environments and the most useful hints. Beyond the scores, the pairwise interactions form a microcosm of how models affect one another. Head-to-head outcomes are transitive and so yield a stable ranking; independent authors converge on the same designs; and in a reinforcement-learning study with Qwen3.8-27B, the learner's hint lift on an author's environments tracks how much training on those environments improves it on held-out reasoning and agentic benchmarks, whether the environments are its own or another model's. Each of these patterns has a counterpart in how models shape one another outside the duel. By staging these interactions under controlled conditions, Environment Duels offers a window onto how LLMs teach, challenge and learn from one another. Code is available at https://github.com/LLM-Duels/EnvDuels.

### 🤖 AI 总结

**一句话总结**：Through a tangle of real-world interactions, from synthetic training pipelines to data shared on the open web, frontier LLMs absorb what their predecessors and competitors create. How well does each m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Environment, Duels, Microcosm, Co-Evolution, Through, tangle

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30116v1) | [下载PDF](https://arxiv.org/pdf/2610.30116v1.pdf)

---

## [8. Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](https://arxiv.org/abs/2610.30113v1)

**作者**：Houde Qian, Zheng Jiang, Wenyi Li 等 12 位作者  
**分类**：cs.CL, cs.AI, cs.CE  
**发布时间**：2026-10-21

### 📄 论文摘要

Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether large language models (LLMs) can complete this loop and produce strategies that work beyond the research period. We introduce Quant-Arena, a benchmark and public leaderboard for end-to-end quantitative research on real A-share market data. A model constructs features and stock-scoring code, receives feedback only on 2022--2023, and freezes one strategy for assessment on the sealed year 2024. A cash-account evaluator applies trading constraints and costs, including market impact estimated from a simulated order book. Scores are dominated by realized excess return and complemented by signal quality and the diversity of features used by the strategy. We evaluate nine frontier models, among which GPT-6 Astra scores highest; yet no model beats the equal-weight market in 2024. Quant-Arena is open to submissions from any model or agent harness.

### 🤖 AI 总结

**一句话总结**：Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, an, Quant-Arena, Benchmarking, Quantitative, Trading, Research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30113v1) | [下载PDF](https://arxiv.org/pdf/2610.30113v1.pdf)

---

## [9. Did the Problem Actually Get Harder? Testing LLMs on Paired P and NP-Complete Problems Hardened by Adversarial Multi-Agent Rewriting](https://arxiv.org/abs/2610.30103v1)

**作者**：Nurul Labib Sayeedi, Md. Faiyaz Abdullah Sayeedi, Zabir Al Nazi 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-21

### 📄 论文摘要

Many NP-complete (NPC) problems have a polynomial-time (P) twin that differs in a single structural detail, such as 3- versus 2-colouring a graph. A model that reasons rather than recalls should notice which side of this boundary a problem falls on, yet existing benchmarks either fix the wording of each task or ignore its complexity class, so they cannot separate the two. We introduce P2NPCBench, a benchmark of 12 problem families in which every NPC problem is paired with a P twin posed over the same surface. To remove the textbook cues that enable recall, we build it with AgentGAN, an adversarial multi-agent framework in which a generator rewrites each statement until a panel of frozen code models fails, while an executable validity gate keeps every rewrite answer- and class-preserving. The result is 2,114 hardened statements with hand-verified reference human solvers. Evaluating 12 proprietary and open-source models, we find that every model scores lower on NPC statements than on their P twins (35.4% vs. 63.8% pass@1), and that 95.1% of model-family pairs fail more often on the NPC side. A tenfold time limit raises NPC accuracy only from 28.5% to 31.9%, so failures stem from wrong or crashing programs rather than slow ones. Hardening also narrows the class gap from 24.8 to 14.6 points, showing that part of the apparent gap reflects familiarity with textbook phrasing rather than complexity class.

### 🤖 AI 总结

**一句话总结**：Many NP-complete (NPC) problems have a polynomial-time (P) twin that differs in a single structural detail, such as 3- versus 2-colouring a graph. A model that reasons rather than recalls should notic...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Did, Problem, Actually, Get, Harder?, Testing, Paired

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30103v1) | [下载PDF](https://arxiv.org/pdf/2610.30103v1.pdf)

---

## [10. Building Auditable AI Text Detectors with Sparse Autoencoders](https://arxiv.org/abs/2610.30006v1)

**作者**：Liam Dugan, Callum McDougall, Matthew Denton 等 6 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-10-21

### 📄 论文摘要

AI-generated text detectors are increasingly deployed in consequential settings---peer review, education, admissions, journalism, and content moderation---where their outputs directly affect individuals. Yet the strongest detectors are fine-tuned neural classifiers whose decisions are opaque, while transparent alternatives (stylometric and linguistic-feature classifiers) underperform them by wide margins. We present a pipeline that converts a fine-tuned neural detector into a classifier that operates on human-readable concepts. We accomplish this by training sparse autoencoders (SAEs) directly on a detector's residual stream, assigning auto-interpretation labels to each SAE feature, and retaining only features whose generated descriptions pass a global fidelity threshold. We then train a lightweight classifier on just the interpretable features. We find that our SAEs recover latent concepts that correspond to highly specific and predictive linguistic "tells" of AI-generated text. Classifiers built on these extracted features are not only highly interpretable but exhibit stronger performance on out-of-distribution texts than either neural or stylometric alternatives.

### 🤖 AI 总结

**一句话总结**：AI-generated text detectors are increasingly deployed in consequential settings---peer review, education, admissions, journalism, and content moderation---where their outputs directly affect individua...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Building, Auditable, Text, Detectors, Sparse, Autoencoders, AI-generated, increasingly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30006v1) | [下载PDF](https://arxiv.org/pdf/2610.30006v1.pdf)

---

## [11. Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents](https://arxiv.org/abs/2610.29995v1)

**作者**：Jielong Tang, Ling-An Zeng, Xujie Yuan 等 10 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-21

### 📄 论文摘要

Long-term memory for multimodal agents remains challenging, as it must preserve fine-grained visual evidence while tracking entity evolution across sessions. Existing abstraction-based memories compress images into text, often discarding visually discriminative details, whereas pixel-preserving memories retain raw observations but struggle to reliably associate diverse observations with persistent entity identities and track their evolving states. To address these limitations, we propose MHG-Mem, a multimodal hypergraph memory that jointly organizes entity identity, state evolution, and provenance to visual evidence. Specifically, MHG-Mem represents distinct entity mentions and their observed facts as individual nodes, grouping identity-consistent mentions and facts through occurrence hyperedges. It then synthesizes aspect-specific evolution states from these grouped observations and links them to supporting entities, facts, and source evidence through evolutionary and evidential hyperedges. To navigate this structured memory, we introduce hypergraph-based agentic search, which adaptively selects an entry layer, traverses typed hyperedges across memory levels, and inspects source observations when fine-grained verification is required. These designs support both detailed visual verification and reasoning over cross-session state changes. Extensive experiments across three benchmarks demonstrate the effectiveness of MHG-Mem, improving performance by 8.20-9.98% over the strongest baseline.

### 🤖 AI 总结

**一句话总结**：Long-term memory for multimodal agents remains challenging, as it must preserve fine-grained visual evidence while tracking entity evolution across sessions. Existing abstraction-based memories compre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Remembering, Through, Change, Provenance-Preserving, Hypergraph, Memory, Multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.29995v1) | [下载PDF](https://arxiv.org/pdf/2610.29995v1.pdf)

---

## cs.CV

## [12. VoxProg: 3D Spatial Reasoning through Voxel Programming](https://arxiv.org/abs/2610.30127v1)

**作者**：Zhichao Zhai, Menglei Zhao, Guikun Chen 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-21

### 📄 论文摘要

Language models' abilities to interpret tasks and generate programs offer a promising basis for 3D spatial reasoning. Yet following spatial instructions in 3D scenes requires programs to construct geometric references that language leaves implicit. In this work, we introduce VoxProg, which formulates 3D object placement through voxel programming: a language model translates task interpretations into executable programs over local voxel views of scene surfaces. Because these views index surface geometry on regular grids with explicit coordinates and neighborhood relations, an evidence program can isolate task-relevant regions and boundaries directly from scene meshes, and a downstream pose program can measure the resulting geometry to compute a target $SE(3)$ pose. Visual and numerical feedback from execution lets the model inspect intermediate selections and candidate placements to iteratively revise its code. To evaluate open-ended placement across functional use, geometric fit, and contextual arrangements, we introduce the 71-task VoxProg-Bench benchmark along with an evaluation suite pairing perceptual Intent Alignment and 3D Physical Validity. Across VoxProg-Bench and external benchmarks, VoxProg consistently outperforms relation-based, keypoint-based, and mesh-based baselines.

### 🤖 AI 总结

**一句话总结**：Language models' abilities to interpret tasks and generate programs offer a promising basis for 3D spatial reasoning. Yet following spatial instructions in 3D scenes requires programs to construct geo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, VoxProg, Spatial, Reasoning, through, Voxel, Programming, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30127v1) | [下载PDF](https://arxiv.org/pdf/2610.30127v1.pdf)

---

## [13. ProactEgoMem: Benchmarking Proactive Memory in Streaming Egocentric Video](https://arxiv.org/abs/2610.30089v1)

**作者**：Ruotong Liao, Meikel Kokowski, Xiaoxiao Sun 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-21

### 📄 论文摘要

Today's multimodal assistants are typically prompted to interpret the visual evidence presented to them. To offload the cognitive burden of remembering across long horizons, wearable assistants should instead proactively acquire and maintain useful memory as the user's surroundings evolve. Doing so on the user's behalf requires identifying what matters, understanding the scene in real time, and initiating memory maintenance in the background while the user stays focused on their activities. We introduce ProactEgoMem, a benchmark that evaluates proactive memory in streaming egocentric video. Three tasks ground the evaluation in ambient environmental needs: Information Capture (IC) preserves transient yet dense visual information, State Tracking (ST) follows changing object states, and Location Tracking (LT) records object movements. The benchmark defines its protocol at two levels of proactiveness: the Notification Level asks for a single timely notification that satisfies the user's intent, while the deeper Intervention Level asks the agent to maintain memory on the user's behalf through an active start-to-stop tool lifecycle. Parallel ProactEgoMem-Daily and ProactEgoMem-Sci tracks contain 300/100 clips covering daily and scientific use cases, paired with 1000/500 questions in ProactEgoMem-QA, which measures the quality of the proactively acquired memory. Across proprietary, open-source, video-language, and streaming baselines, even the strongest models fail to capture memory both timely and accurately. ProactEgoMem provides a rigorous evaluation foundation for proactive multimodal assistance and for video agents that co-exist with their users.

### 🤖 AI 总结

**一句话总结**：Today's multimodal assistants are typically prompted to interpret the visual evidence presented to them. To offload the cognitive burden of remembering across long horizons, wearable assistants should...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ProactEgoMem, Benchmarking, Proactive, Memory, Streaming, Egocentric, Video, Today's

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30089v1) | [下载PDF](https://arxiv.org/pdf/2610.30089v1.pdf)

---

## [14. Attn-Forcing: Learning Full-Context Attention Proxies for Streaming Video Generation](https://arxiv.org/abs/2610.30036v1)

**作者**：Junyao Gao, Sibo Liu, Jiaxing Li 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-21

### 📄 论文摘要

Increasing the attention context length significantly improves streaming video generation quality, while incurring prohibitive memory and computational costs as the context grows. Existing methods attempt to capture this contextual information through attention selection or compression, but remain limited by bounded representations and lack explicit attention-level supervision to retain historical contributions to current queries. To address this, we introduce Attn-Forcing, a novel framework that preserves full-context attention contributions for streaming video generation under bounded memory and computation. We achieve this by introducing attention proxies that continuously approximate the attention responses induced by the historical context. Specifically, we implement the proxies as learnable visual latents and employ a Proxy Update Module to incorporate visual context from historical latents. Moreover, we propose an Attention Matching Loss to explicitly constrain the attention behavior of the learned proxies using full-context attention supervision. Extensive qualitative and quantitative experiments demonstrate that Attn-Forcing consistently improves streaming video generation quality and achieves state-of-the-art performance over existing baseline methods.

### 🤖 AI 总结

**一句话总结**：Increasing the attention context length significantly improves streaming video generation quality, while incurring prohibitive memory and computational costs as the context grows. Existing methods att...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Attn-Forcing, Learning, Full-Context, Attention, Proxies, Streaming, Video, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30036v1) | [下载PDF](https://arxiv.org/pdf/2610.30036v1.pdf)

---

## [15. Plausible but Unimplantable: A Trustworthiness Audit of Shape Completion Foundation Models for Cranial Defect Reconstruction](https://arxiv.org/abs/2610.30035v1)

**作者**：Marek Wodzinski, Kamil Kwarciak, Daria Hemmerling 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-21

### 📄 论文摘要

A patient who has lost part of the skull vault needs an implant that fits the defect exactly, and such implants are still drawn by hand in CAD by specialists, which makes each case slow and expensive. The task can be considered as a shape completion problem, so pretrained completion models, and now the first shape completion foundation models, look like a way to remove that manual step. We audited three publicly released pretrained shape completion models, two of them foundation models, applied zero-shot to 239 cranial defects, some carved from public skull datasets and some real post-craniectomy cases. Each output was compared with simply returning the patient's own remaining bone, and tested for whether the predicted material could be placed without intersecting the bone that is still there. On the 210 carved defects none of the three improved on doing nothing, and on the 29 real cases only one did so beyond chance. Yet not one output, from any model in any configuration, was implantable: none managed both to stay clear of the bone the patient still has and to place more material than doing nothing, where a task-specific volumetric model, trained for this task and selected on these cases, was implantable on all but one. The output that most convincingly resembles a skull is no more placeable than the rest, and at these point densities implant thickness cannot be read off the emitted points at all, which is a property of the output representation rather than of any one model. On this evidence the shape completion foundation models we could obtain cannot be trusted and, used as released, are not usable in clinical practice. Substantial research towards trustworthy foundation models for shape completion is still needed.

### 🤖 AI 总结

**一句话总结**：A patient who has lost part of the skull vault needs an implant that fits the defect exactly, and such implants are still drawn by hand in CAD by specialists, which makes each case slow and expensive....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Plausible, but, Unimplantable, Trustworthiness, Audit, Shape, Completion

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30035v1) | [下载PDF](https://arxiv.org/pdf/2610.30035v1.pdf)

---

## [16. RealMe: Immersive Volumetric Video from Minimal Captures](https://arxiv.org/abs/2610.30023v1)

**作者**：Chenxu Zhou, Zhiyuan Yu, Yudong Jin 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-21

### 📄 论文摘要

This paper addresses the problem of creating immersive volumetric videos from sparse and low-resolution capture resources. Conventional dense multi-view reconstruction methods can produce high-quality volumetric videos, but their reliance on costly capture setups makes them impractical in real-world scenarios. Recent approaches use generative models to relax capture requirements, but still suffer from limited resolution and 4D inconsistency. To overcome these constraints, we propose RealMe, a unified framework built around a high-resolution video diffusion model that enhances limited captures into high-resolution (2K), 4D-consistent videos for volumetric video reconstruction. Specifically, RealMe constructs auxiliary data from capture videos and encodes them into latents along with layout-aware positional embeddings. The video diffusion model adapts factorized spatio-temporal attention to the multi-view capture layout, denoises these latents across viewpoints and time, and decodes them into enhanced videos to refine the 4D representation. This adaptation helps the model capture temporal dynamics and multi-view relationships, leading to more 4D-consistent generation. To reduce the data gap between generated videos and real captures, we apply a latent frequency loss that provides frequency-domain supervision in latent space. Extensive experiments on the public DNA-Rendering benchmark and our self-captured RealVV dataset demonstrate that RealMe is able to create immersive volumetric videos and outperforms state-of-the-art methods in visual fidelity and 4D consistency.

### 🤖 AI 总结

**一句话总结**：This paper addresses the problem of creating immersive volumetric videos from sparse and low-resolution capture resources. Conventional dense multi-view reconstruction methods can produce high-quality...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RealMe, Immersive, Volumetric, Video, Minimal, Captures, paper, addresses

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30023v1) | [下载PDF](https://arxiv.org/pdf/2610.30023v1.pdf)

---

## [17. ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization](https://arxiv.org/abs/2610.30013v1)

**作者**：Jian Xu, Yi Li, Ying Huang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-21

### 📄 论文摘要

Language 3D Gaussian Splatting enables open-vocabulary scene understanding by associating Gaussian primitives with language features. These semantic attributes increase model storage, while most existing 3DGS compression methods are designed mainly to preserve RGB rendering quality. One straightforward approach is to apply sparsification and quantization sequentially. However, pruning based only on rendering quality can remove Gaussians that have small RGB contributions but are important for semantic prediction. Once removed, their semantic information cannot be recovered by later quantization. We propose ClunoGS, a compact framework for Language 3DGS that combines semantics-aware Gaussian sparsification and vector quantization in a unified constrained objective. Semantic supervision is used during sparsification, and the objective jointly considers rendering quality, semantic accuracy, and compactness. We optimize the unified objective with alternating primal, sparsification, quantization, and dual updates. We evaluate ClunoGS on open-vocabulary localization and segmentation using the LERF and ScanNet-10 benchmarks. Under aggressive compression, our unified, semantics-aware formulation substantially alleviates the degradation of semantic representations caused by sequential compression and semantics-agnostic Gaussian sparsification. Ablations further show that jointly coordinating sparsification and quantization better preserves semantic accuracy than applying them independently.

### 🤖 AI 总结

**一句话总结**：Language 3D Gaussian Splatting enables open-vocabulary scene understanding by associating Gaussian primitives with language features. These semantic attributes increase model storage, while most exist...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, ClunoGS, Compact, Language, Gaussian, Splatting, via, Unified

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30013v1) | [下载PDF](https://arxiv.org/pdf/2610.30013v1.pdf)

---

## [18. Multiclass Boundary Refinement with Neural Cellular Automata for Remote Sensing Land Cover Segmentation](https://arxiv.org/abs/2610.30007v1)

**作者**：Pascoassis Souza Santos Meira, Gilson Antonio Giraldi, Rafael Duarte Coelho dos Santos  
**分类**：cs.CV  
**发布时间**：2026-10-21

### 📄 论文摘要

Semantic segmentation of remote sensing imagery often places class boundaries a few pixels away from where they truly lie, and this position error is concentrated in the thin band measured by Boundary IoU (BIoU). We treat boundary refinement as the iterated application of a small learned local rule: the Boundary Refinement Neural Cellular Automaton (BRNCA), that starts from the class probabilities of a frozen, pre-trained segmenter and corrects them cell by cell. We generalise the binary rNCA to the multiclass case by keeping the visible channels on the probability simplex through an Aitchison (log-space) update and by adding free hidden channels. The best configuration improves the mean BIoU over the base segmenter by 2.36 points (from 46.63 to 48.99). The gain is concentrated on the irregular woodland class (+8.5 points BIoU); this suggests that position error is correlated with the fractal dimension of the class boundaries.

### 🤖 AI 总结

**一句话总结**：Semantic segmentation of remote sensing imagery often places class boundaries a few pixels away from where they truly lie, and this position error is concentrated in the thin band measured by Boundary...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multiclass, Boundary, Refinement, Neural, Cellular, Automata, Remote, Sensing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30007v1) | [下载PDF](https://arxiv.org/pdf/2610.30007v1.pdf)

---

## [19. Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](https://arxiv.org/abs/2610.29989v1)

**作者**：Ruopeng Gao, Yukun Huang, Jiarui Hu 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-21

### 📄 论文摘要

Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve. Under teacher forcing, strong temporal redundancy may allow local visual continuity to serve as a shortcut for current-chunk denoising, reducing the pressure to model visual evolution. We introduce Future Chunk Prediction (FCP), an auxiliary objective jointly optimized with teacher-forced denoising that predicts temporally separated chunks without access to the intervening visual context. Drawing supervision directly from training videos, FCP requires no additional pretrained visual encoder and leaves autoregressive inference unchanged. Our method achieves superior physical plausibility over standard teacher-forced autoregressive training with a lower overall training compute budget, highlighting the effectiveness and efficiency of future-chunk supervision for modeling visual evolution. Intriguingly, our visualizations suggest that FCP fosters a more structured representation space, which may be valuable for building autoregressive world models.

### 🤖 AI 总结

**一句话总结**：Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve. Under teacher forcing, strong tempor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Looking, Ahead, Modeling, Future, Evolution, Autoregressive, Video, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.29989v1) | [下载PDF](https://arxiv.org/pdf/2610.29989v1.pdf)

---

## cs.LG

## [20. Self-normalized Bernstein Inequalities for Regenerative Processes and Applications to Learning Without Independence](https://arxiv.org/abs/2610.30119v1)

**作者**：Imon Banerjee, Pierre Alquier  
**分类**：cs.LG, math.PR, math.ST  
**发布时间**：2026-10-21

### 📄 论文摘要

We prove a self-normalized Bernstein inequality for bounded functions of a regenerative process with independent, identically distributed marked cycles of finite mean length. The bound uses observed cycle lengths and retains explicit terms for truncation and the cycle ending after the observation horizon. Selecting a tuning parameter from a finite deterministic collection gives a version of Bernstein inequality where all terms are empirical but one, related to the tails of the regeneration times. We then study this term in many regimes: it turns out that it is of second-order in many cases of interest. This is important for applications in machine learning: we prove generalization error bounds for classification with non-i.i.d., regenerative data. These bounds can be used to define learning objectives: by minimizing the first-order term only in the bound, we define agnostic classifiers that still satisfy oracle inequalities. We also show that the bound on the average deviation provided by our results is minimax-optimal in the sample size and in the expected regeneration time. Finally, we combine the Bernstein inequality with a regenerative strong approximation to obtain a Gaussian approximation using an observable block variance estimator.

### 🤖 AI 总结

**一句话总结**：We prove a self-normalized Bernstein inequality for bounded functions of a regenerative process with independent, identically distributed marked cycles of finite mean length. The bound uses observed c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Self-normalized, Bernstein, Inequalities, Regenerative, Processes, Applications, Learning, Without

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30119v1) | [下载PDF](https://arxiv.org/pdf/2610.30119v1.pdf)

---

## [21. The role of locality and weight sharing in convolutional neural networks](https://arxiv.org/abs/2610.30118v1)

**作者**：Francesco Mori, Melanie Weber  
**分类**：cs.LG, cond-mat.dis-nn, cond-mat.stat-mech, stat.ML  
**发布时间**：2026-10-21

### 📄 论文摘要

The success of convolutional neural networks is often attributed to locality and weight sharing. However, how these two properties separately shape learning, and how their effects depend on the spatial correlations of natural images, remain poorly understood. We address these questions in a teacher-student model with a convolutional teacher acting on $P$ input positions with correlation $c$ between positions. We compare convolutional and locally connected students trained by online stochastic gradient descent, and derive ordinary differential equations that describe their dynamics exactly in the limit of large feature dimension $D$. For uncorrelated positions ($c = 0$), the two students follow the same learning trajectory, with the convolutional student learning exactly $P$ times faster. We also find that locality affects the sample complexity: a student that matches the kernel size of the teacher recovers it from $\mathcal{O}_{D}(D)$ samples, whereas $\mathcal{O}_{D}(D\log(D))$ samples are needed with a larger kernel. For $c > 0$, spatial correlations can reduce the advantage of weight sharing. The asymptotic error of the convolutional student grows with $c$, whereas that of the locally connected student is independent of $c$ and overall lower when evaluated at the same learning rate. When the learning rate is instead tuned to the training horizon, however, the locally connected student wins at early times and the convolutional student at late times, with a transition that we predict analytically.

### 🤖 AI 总结

**一句话总结**：The success of convolutional neural networks is often attributed to locality and weight sharing. However, how these two properties separately shape learning, and how their effects depend on the spatia...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, role, locality, weight, sharing, convolutional, neural, networks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30118v1) | [下载PDF](https://arxiv.org/pdf/2610.30118v1.pdf)

---

## [22. Velocity Ambiguity Profiles: Time-Resolved Bayes-Risk Diagnostics for Flow Matching](https://arxiv.org/abs/2610.30107v1)

**作者**：Yunpeng Mei, Xiaowen Zhu, Chenyu Wang 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-21

### 📄 论文摘要

Flow matching trains a continuum of velocity regression problems but usually reports a loss averaged over interpolation time, obscuring which regions are limited by intrinsic ambiguity and which remain data-limited. We introduce the Velocity Ambiguity Profile (VAP), $\mathcal{A}_v(t)$, the time-local Bayes-risk floor of velocity prediction, and decompose time-resolved loss as $L_N(t)=\mathcal{A}_v(t)+R(t;N)$, where only the excess term $R(t;N)$ is reducible by more data or a different estimator. For $N$ training samples and a $K$-component mixture in the structured example, we prove two statistical benchmarks. In an intrinsic local-regression benchmark, $\mathcal{A}_v(t)$ enters the time-dependent noise factor of the standard nonparametric rate. In separated isotropic Gaussian mixtures, the Bayes velocity becomes locally affine, and a label-oracle residual-regression benchmark has parametric excess-risk scale $K\mathcal{A}_v(t)/N$, matched within the same separated residual Gaussian-location subproblem. Controlled Gaussian-mixture experiments validate this diagnostic through a dense transition sweep, calibrated oracle-to-blind and empirical-proxy audits, and a local controlled time-sampler stress test in which a frozen reducible-error proxy reduces reducible loss while cross-cell sensitivity delimits aggressive sampling. On CIFAR-100 DINOv2 feature flow, guided time sampling reduces uniformly evaluated velocity loss by $6.78\%$ and global feature Fréchet distance (FD) by $23.6\%$, while class-conditional kernel inception distance (KID) shows no improvement. VAP turns an averaged flow-matching objective into a time-resolved diagnostic for locating ambiguity-limited and data-limited regions.

### 🤖 AI 总结

**一句话总结**：Flow matching trains a continuum of velocity regression problems but usually reports a loss averaged over interpolation time, obscuring which regions are limited by intrinsic ambiguity and which remai...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Velocity, Ambiguity, Profiles, Time-Resolved, Bayes-Risk, Diagnostics, Flow, Matching

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30107v1) | [下载PDF](https://arxiv.org/pdf/2610.30107v1.pdf)

---

## [23. BatchBench: Benchmarking AI Robustness to Batch Effects and Domain Shift in Biomedical Images - A JUMP Cell Painting Leaderboard](https://arxiv.org/abs/2610.30104v1)

**作者**：Sonja Topf, Ana Sanchez-Fernandez, Günter Klambauer  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-21

### 📄 论文摘要

Despite recent advances, current AI systems remain highly susceptible to domain shifts, particularly in biomedical imaging, where images are usually acquired under substantially different experimental conditions. Although recent domain adaptation methods have made substantial progress, significant performance gaps under domain shift persist. To measure progress in this regard, we introduce BatchBench, a leaderboard that evaluates and compares the robustness of AI systems on biomedical images from unseen experimental batches and data sources. BatchBench is built on JUMP-CP, one of the largest publicly available biomedical imaging datasets. Generated using the Cell Painting assay, JUMP-CP exhibits pronounced batch effects and domain shifts, making it a challenging testbed for evaluating robustness to distributional changes.

### 🤖 AI 总结

**一句话总结**：Despite recent advances, current AI systems remain highly susceptible to domain shifts, particularly in biomedical imaging, where images are usually acquired under substantially different experimental...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BatchBench, Benchmarking, Robustness, Batch, Effects, Domain, Shift, Biomedical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30104v1) | [下载PDF](https://arxiv.org/pdf/2610.30104v1.pdf)

---

## [24. Differentially Private Sparse Reward Estimation with Preference Feedback](https://arxiv.org/abs/2610.30099v1)

**作者**：Meng Ding, Mingxi Lei, Jie Zhang 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-21

### 📄 论文摘要

Reinforcement Learning with Human Feedback (RLHF) has become a central paradigm for aligning Large Language Models with human values. However, the reliance on sensitive preference data necessitates rigorous differential privacy (DP) guarantees to prevent user information leakage. Existing private alignment methods typically assume dense reward parameterizations, resulting in estimation error bounds that scale polynomially with the ambient {model size $d$}. Such dependence is prohibitive in modern {overparameterized models} where $d$ is vast. In this work, we study \emph{Private Sparse RLHF} problem to address this limitation, assuming that human preferences (reward model) are governed by a subset of $s^* \ll d$ relevant features. We provide the first comprehensive theoretical framework for differentially private sparse reward estimation from pairwise preference feedback under the Bradley-Terry-Luce model, and introduce efficient algorithms for both Sample-DP and Label-DP settings. Theoretically, under the squared $\ell_2$ parameter estimation error, we establish upper bounds of $\widetilde{O}(s^*/n + {s^*}^2/n^2\varepsilon^2)$ for $(\varepsilon,δ)$-Sample-DP and $\widetilde{O}(s^*/n + s^*/n\varepsilon^2)$ for $\varepsilon$-Label-DP based on randomized response, where $n$ is the training data size. For the lower bounds, we show that the Sample-DP rate is nearly optimal, and that the guarantee for our Label-DP method cannot be further improved within the randomized-response framework. We also provide a general lower bound for the problem with Label-DP. Empirically, our framework demonstrates superior efficacy over dense baselines across sentiment generation and safety alignment benchmarks, offering a significantly more favorable privacy-utility trade-off.

### 🤖 AI 总结

**一句话总结**：Reinforcement Learning with Human Feedback (RLHF) has become a central paradigm for aligning Large Language Models with human values. However, the reliance on sensitive preference data necessitates ri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Differentially, Private, Sparse, Reward, Estimation, Preference, Feedback, Reinforcement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30099v1) | [下载PDF](https://arxiv.org/pdf/2610.30099v1.pdf)

---

## [25. Circuits of LLM Classifiers](https://arxiv.org/abs/2610.30076v1)

**作者**：Hadi Khalaf, Sajani Vithana, Kunal Talreja 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-21

### 📄 论文摘要

Language models make it easy to build classifiers by simply prompting a model with the sample to classify. However, their predictions are neither deterministic nor uniformly reliable across samples. How can we combine predictions from different models to improve reliability? We view LLM classifiers as noisy measurement instruments of an underlying target label. Our goal is to maximize average classification accuracy at a given average query cost. To this end, we introduce circuits that organize LLM classifiers into an adaptive sequence of queries and decisions. We then characterize the optimal circuit, obtain the fundamental limits of achievable accuracy, and provide practical insights on realizing the optimal circuit. Across seven classification tasks spanning safety, health, political science, human preference, agent evaluation, decision-making and reasoning, our method improves the cost-accuracy frontier over routing and cascading baselines.

### 🤖 AI 总结

**一句话总结**：Language models make it easy to build classifiers by simply prompting a model with the sample to classify. However, their predictions are neither deterministic nor uniformly reliable across samples. H...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, it, Circuits, Classifiers, Language, models, make

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30076v1) | [下载PDF](https://arxiv.org/pdf/2610.30076v1.pdf)

---

## [26. From Classifier Heads to Encoder Prototypes: Personalized Federated Learning with Head-Derived Clustering](https://arxiv.org/abs/2610.30075v1)

**作者**：Amirardalan Dehghanpour, Arian Noori, Ehsan Tanghatari 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-21

### 📄 论文摘要

Personalized federated learning must decide which clients should share representations. We introduce HDC-FL (Head-Derived Clustering for Personalized Federated Learning), which reads that decision off a signal shared-encoder training already produces: the client-specific classifi- er heads. At periodic refresh rounds the server projects the cached heads into a normalized low-rank descriptor space, groups the descriptors, builds one encoder prototype per group from the cached client encoders, and returns to each client a soft mixture of those prototypes paired with its own unchanged head. Client-specific heads are never averaged or distributed to oth- er clients; the shared-encoder trajectory is left intact; and no second optimization trajectory, additional local objective, or post-training fine-tuning stage is required. Across 11 CIFAR-10 and CIFAR-100 configurations covering label-subset, Dirichlet and rotation heterogeneity with ResNet-18 and MobileNetV2 encoders, HDC-FL is competitive with the strongest personalized and clustered baselines in macro-averaged mean accuracy and attains the numerically highest macro-averaged worst-client and bottom-20% accuracy among the evaluated methods. The tail results distinguish methods that look similar when only their means are compared. A controlled donor-swap diagnostic further finds positive donor-ranking associations between head similarity and encoder compatibility in all three settings tested, most clearly under covariate shift.

### 🤖 AI 总结

**一句话总结**：Personalized federated learning must decide which clients should share representations. We introduce HDC-FL (Head-Derived Clustering for Personalized Federated Learning), which reads that decision off...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Classifier, Heads, Encoder, Prototypes, Personalized, Federated, Learning, Head-Derived

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30075v1) | [下载PDF](https://arxiv.org/pdf/2610.30075v1.pdf)

---

## [27. ExGrad: Beyond Suppression - Explicit Clean-Gradient Subtraction in Adversarial Training](https://arxiv.org/abs/2610.30018v1)

**作者**：Zhiyuan Ye, Xiangyu Zhou, Ji Qi 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-21

### 📄 论文摘要

Adversarial training derives updates from surrogate losses, but source-loss descent does not directly characterize an update's effect on adversarial margins. We introduce ExGrad (extrapolative gradient recomposition), which constructs clean-input, adversarial-input, and adversarial-weight-perturbed (AWP) gradients. Virtual steps measure their margin responses, and a globally solvable three-variable problem selects coefficients over a bounded affine domain without nonnegativity constraints. Across affine radii on CIFAR-10, negative clean coefficients rapidly predominate and increase in magnitude with the radius. Cross-zero interventions show that setting the clean coefficient to zero is insufficient: mild subtraction improves PGD-20, while stronger subtraction trades clean accuracy for further PGD-20 gains. In CIFAR-10 WRN-28-4 controls, none of the three candidate-removal variants matches full ExGrad. Projection diagnostics show that negative clean coefficients usually coexist with positive net clean-axis projections, although both decrease as the radius grows. Norm-matched controls indicate that update magnitude alone does not explain the moderate-radius gains. Experiments on CIFAR-10, CIFAR-100, and ImageNet-100 show radius-dependent improvements over AWP. On CIFAR-100, ExGrad at $R=0.8$ improves all five reported metrics, including clean and AutoAttack accuracy by 3.84 and 1.75 percentage points. On ImageNet-100, the same radius improves all four robust metrics over both AWP and PGD-AT. These results identify clean-gradient subtraction as a response-revealed update preference whose strength and clean-robust operating point are controlled by the affine radius.

### 🤖 AI 总结

**一句话总结**：Adversarial training derives updates from surrogate losses, but source-loss descent does not directly characterize an update's effect on adversarial margins. We introduce ExGrad (extrapolative gradien...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ExGrad, Beyond, Suppression, Explicit, Clean-Gradient, Subtraction, Adversarial, Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30018v1) | [下载PDF](https://arxiv.org/pdf/2610.30018v1.pdf)

---

## [28. Agent Behavior Maps: Locating Agents by What They Would Do, Without Running Them](https://arxiv.org/abs/2610.30014v1)

**作者**：Shota Fujikawa, Takuya Tamura, Kosuke Akimoto 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-10-21

### 📄 论文摘要

LLM agents with similar success rates can follow different action sequences. An Agent Behavior Map represents LLM-harness combinations using centered action log-likelihoods on shared reference trajectories, without requiring new environment rollouts from the target agent. We derive error bounds relating squared coordinate distances to trajectory KL under explicit assumptions, and across eight cross-scored models the distances track the directly measured trajectory KL in rank order. Across 100 LLMs and four environments, ALFWorld-based coordinates support performance prediction and identify behavioral similarities. In ALFWorld, these similarities persist after controlling for success rates and model size, including across model families. As an extension, harness-component displacements approximately compose, with accuracy varying across components and environments.

### 🤖 AI 总结

**一句话总结**：LLM agents with similar success rates can follow different action sequences. An Agent Behavior Map represents LLM-harness combinations using centered action log-likelihoods on shared reference traject...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Do, Behavior, Maps, Locating, What, They, Would

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30014v1) | [下载PDF](https://arxiv.org/pdf/2610.30014v1.pdf)

---

## [29. Mitigating Model Collapse through Dreaming Learning](https://arxiv.org/abs/2610.30009v1)

**作者**：Matteo Benati, Alessandro Londei, Denise Lanzieri 等 5 位作者  
**分类**：cs.LG, cond-mat.dis-nn, stat.ML  
**发布时间**：2026-10-21

### 📄 论文摘要

Training generative models on synthetic data causes loss of diversity and a decrease in performance, a phenomenon known as model collapse. We study this degeneration spectrally in a controlled Markov setting. The eigenvalue spectrum of the learned transition operator offers a direct view of the process, since the subdominant eigenvalues set how fast the chain mixes and therefore how much of the state space it continues to explore. We find that sampling at temperature $T_s < 1$ acts on the operator like repeated sharpening, pushing it toward a deterministic system: the subdominant eigenvalues approach the unit circle and the spectral gap narrows. When $T_s < 1$, even data accumulation does not appear to arrest this drift. We then analyze Dreaming Learning, a regulariser that, in parallel with regular training, adds a loss term on the model's own samples drawn at a raised temperature $T_d > 1$. Because high-temperature samples flatten the predicted distribution, training on them keeps the entries of the learned operator from becoming vanishingly small, which in turn keeps the eigenvalues bounded away from the unit circle. Measurements of the spectra over 5000 generations are consistent with this picture, and the mitigation effect persists in more complex settings such as LSTM language models and a 124M-parameter GPT-2.

### 🤖 AI 总结

**一句话总结**：Training generative models on synthetic data causes loss of diversity and a decrease in performance, a phenomenon known as model collapse. We study this degeneration spectrally in a controlled Markov ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mitigating, Model, Collapse, through, Dreaming, Learning, Training, generative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.30009v1) | [下载PDF](https://arxiv.org/pdf/2610.30009v1.pdf)

---

## [30. SCDM: Scalable Causal Discovery in Nonlinear Temporal Systems with Meta-Learning](https://arxiv.org/abs/2610.29992v1)

**作者**：Jingbo Wang, Kegeng Tang, Zihao Wang 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-21

### 📄 论文摘要

Causal discovery from nonlinear multivariate time series is challenging in high-dimensional systems, where the number of candidate directed relations grows quadratically with the number of variables. Existing methods are often limited by target-wise model fitting, repeated conditional testing, or expensive graph-search procedures. We propose SCDM, a shared-parameter meta-learning framework for scalable temporal causal discovery. SCDM treats each target variable as a task while learning a shared temporal predictor and a shared causal-strength matrix across tasks. Each meta-episode updates only a subset of target-variable tasks, allowing the model to accumulate structural evidence across the full system without exhaustive target-wise optimization. After training, a post-training graph readout converts the learned predictor into continuous directed causal scores for threshold-independent evaluation. We also provide a finite-error recovery principle showing that, under fully observed delayed-system assumptions and a positive risk-gap condition, thresholding SCDM scores recovers the graph when statistical, meta-optimization, and readout errors are below the population margin. Experiments on controlled synthetic, neuroimaging-inspired, high-dimensional, and real-world temporal benchmarks demonstrate competitive causal recovery and improved scalability in large temporal systems.

### 🤖 AI 总结

**一句话总结**：Causal discovery from nonlinear multivariate time series is challenging in high-dimensional systems, where the number of candidate directed relations grows quadratically with the number of variables. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SCDM, Scalable, Causal, Discovery, Nonlinear, Temporal, Systems, Meta-Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.29992v1) | [下载PDF](https://arxiv.org/pdf/2610.29992v1.pdf)

---

