# arXiv AI 论文日报 | 2026-06-17

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (8 篇)
- [cs.CL](#csCL) (7 篇)
- [cs.LG](#csLG) (6 篇)
- [cs.AI](#csAI) (9 篇)

---

## cs.AI

## [1. EvolveNav: Proactive Preflection and Self-Evolving Memory for Zero-Shot Object Goal Navigation](https://arxiv.org/abs/2606.18235v1)

**作者**：Qi Chai, Wenhao Shen, Nanjie Yao 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-16

### 📄 论文摘要

Zero-Shot Object-Goal Navigation (ZS-OGN) requires embodied agents to explore and locate target objects without any prior training. To this end, recent methods leverage foundation models. But they typically rely on static priors and lack adaptation, which leads to repeated errors and costly trial and error. In this paper, we propose a self-evolving ZS-OGN framework that enables continuous test-time improvement. Specifically, we build an agentic rule memory by extracting actionable knowledge from past trajectories. Then, we propose a retrieval strategy based on upper confidence bound, selecting effective rules by balancing semantic relevance and historical success. In addition, we introduce a memory-guided preflection module that forecasts potential outcomes before action, reducing inefficient exploration. Extensive experiments show that our method outperforms existing zero-shot baselines, achieving a 10.1\% improvement in success rate with fewer unnecessary steps.

### 🤖 AI 总结

**一句话总结**：Zero-Shot Object-Goal Navigation (ZS-OGN) requires embodied agents to explore and locate target objects without any prior training. To this end, recent methods leverage foundation models. But they typ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EvolveNav, Proactive, Preflection, Self-Evolving, Memory, Zero-Shot, Object, Goal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18235v1) | [下载PDF](https://arxiv.org/pdf/2606.18235v1.pdf)

---

## [2. Fixed-Point Reasoners: Stable and Adaptive Deep Looped Transformers](https://arxiv.org/abs/2606.18206v1)

**作者**：Sajad Movahedi, Vera Milovanović, Shlomo Libo Feigin 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-16

### 📄 论文摘要

Looped architectures provide an inductive bias toward learning step-by-step procedures for tasks that require compositional reasoning. The number of effective layers reached by looping determines the quality of the solution these models find. Like deep architectures, looped architectures are prone to a signal propagation problem induced by depth as the halting decision is postponed. In this paper, we address this signal propagation issue using pre-norm layers and residual scaling. Building on these architectural modifications, we propose FPRM, a Transformer-based Fixed-Point Reasoning Model that uses fixed-point convergence as an end-to-end halting mechanism in a looped architecture. We show that fixed-point halting allows FPRM to adapt its compute to task difficulty. FPRM is effective on common reasoning benchmarks, namely Sudoku, Maze, state-tracking, and ARC-AGI.

### 🤖 AI 总结

**一句话总结**：Looped architectures provide an inductive bias toward learning step-by-step procedures for tasks that require compositional reasoning. The number of effective layers reached by looping determines the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Fixed-Point, Reasoners, Stable, Adaptive, Deep, Looped, Transformers, architectures

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18206v1) | [下载PDF](https://arxiv.org/pdf/2606.18206v1.pdf)

---

## [3. DRFLOW: A Deep Research Benchmark for Personalized Workflow Prediction](https://arxiv.org/abs/2606.18191v1)

**作者**：Md Tawkat Islam Khondaker, Raymond Li, Muhammad Abdul-Mageed 等 5 位作者  
**分类**：cs.AI, cs.MA  
**发布时间**：2026-06-16

### 📄 论文摘要

Deep research (DR) systems are increasingly used for complex information-seeking tasks, but existing works mainly focus on generating reports and summaries. In contrast, many enterprise tasks instead require an agent to identify concrete workflows which is a sequence of action-steps. For example, rather than summarizing budgeting policies, an agent should be able to determine the steps needed to answer a question such as: "How do I request new headcount given a fixed budget?". Therefore, we introduce DRFLOW, a benchmark for evaluating personalized workflows predicted by agents from heterogeneous sources. Each task requires the agent to identify relevant evidence from scattered sources, then use that evidence to predict the correct action-step sequence for the user's task. DRFLOW contains 100 tasks across five domains, with 1,246 reference workflow steps grounded in more than 3,900 sources. We define seven diagnostic metrics covering factual grounding, step recovery, structural ordering, condition resolution, and personalization. We further present DRFLOW-Agent (DRFA), a workflow-oriented reference agent to predict personalized workflow. We show that although DRFA improves over strong baseline agents (upto 10.02% average F1 score), there is substantial room for improvement remains across these workflow metrics, indicating that predicting complete and correct personalized workflows remains a challenging frontier for deep research.

### 🤖 AI 总结

**一句话总结**：Deep research (DR) systems are increasingly used for complex information-seeking tasks, but existing works mainly focus on generating reports and summaries. In contrast, many enterprise tasks instead ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DR, DRFLOW, Deep, Research, Benchmark, Personalized, Workflow, Prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18191v1) | [下载PDF](https://arxiv.org/pdf/2606.18191v1.pdf)

---

## [4. Learning Cardiac Electrophysiology Digital Twins Through Agentic Discovery of Hybrid Structure](https://arxiv.org/abs/2606.18154v1)

**作者**：Ziqi Zhou, Yubo Ye, Sumeet Atul Vadhavka 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-16

### 📄 论文摘要

Building personalized cardiac electrophysiology (EP) digital twins requires identifying the appropriate model structure for each patient, not merely fitting parameters. Traditional methods rely on experts to manually prescribe hybrid physics-neural architectures, which requires deep domain expertise and does not transfer across patients. Recent works have applied large language models (LLMs) to generate or act as hybrid models. However, despite their promising generalization capacity, these LLM-based methods lack the structural priors needed for stable cardiac simulations. Hence, we propose LEADS, a framework that formulates cardiac EP domain knowledge as a structured action space and utilizes an LLM agent to discover hybrid models. The agent follows an iterative reasoning-and-action loop to select, combine, and refine hybrid models, whilst gradient descent handles parameter fitting. The proposed LEADS designs every candidate model towards physically grounded, interpretable, and numerically stable, while allowing open-ended architectural discovery. We validate LEADS on synthetic data with three ground-truth reaction models and on real cardiac EP data, demonstrating that it outperforms both human-designed hybrid models and other LLM-based hybrid modeling.

### 🤖 AI 总结

**一句话总结**：Building personalized cardiac electrophysiology (EP) digital twins requires identifying the appropriate model structure for each patient, not merely fitting parameters. Traditional methods rely on exp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Cardiac, Electrophysiology, Digital, Twins, Through, Agentic, Discovery

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18154v1) | [下载PDF](https://arxiv.org/pdf/2606.18154v1.pdf)

---

## [5. WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning](https://arxiv.org/abs/2606.18147v1)

**作者**：Yuwei Zhang, Tong Xia, Bianca Emmerich 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-16

### 📄 论文摘要

Language models are remarkably capable at medical question answering, in some cases surpassing the accuracy of general physicians. However, answering questions about wearable health data remains challenging and understudied, as these ubiquitous sensors produce continuous, high-dimensional, and longitudinal data, which is non-trivial to align with text-centric distributions in LLM pretraining. The diversity of sensor modalities and user intents cannot be effectively handled by a fixed reasoning workflow or a single pretrained foundation model. To address these challenges, we propose WEQA, a query-adaptive agent framework that unifies LLM reasoning with specialized wearable analytical and modeling tools. An LLM controller is employed to synthesize execution plans and dynamically route each query to the appropriate combination of sensor analysis and pretrained models, and perform grounded response auditing with external knowledge. We also curate a benchmark spanning four open wearable datasets comprising analytic and predictive tasks in three different health domains. Experiments show that our framework is 24% more accurate than LLM and agentic baselines, and a blinded study with 12 medical experts and 8 users shows substantial gains in usefulness and clinical soundness.

### 🤖 AI 总结

**一句话总结**：Language models are remarkably capable at medical question answering, in some cases surpassing the accuracy of general physicians. However, answering questions about wearable health data remains chall...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：WEQA, Wearable, hEalth, Question, Answering, Query-Adaptive, Agentic, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18147v1) | [下载PDF](https://arxiv.org/pdf/2606.18147v1.pdf)

---

## [6. Memory as a Wasting Asset: Pricing Flash Endurance for Embodied Agents, and the Limits of Doing So](https://arxiv.org/abs/2606.18144v1)

**作者**：Josef Liyanjun Chen  
**分类**：cs.AI, cs.CY, cs.LG, cs.RO  
**发布时间**：2026-06-16

### 📄 论文摘要

A robot's flash endurance is a non-renewable stock: every persisted write spends one of a few thousand program/erase cycles and never refills, yet no fielded robot memory system prices which memories are worth an erase cycle. We treat embodied memory as depreciating capital and price that stock with a single endurance shadow price $η$, which makes cost-minimizing placement across a RAM / on-board NVM / cloud hierarchy a threshold in a wear-augmented per-byte index. The index is cost-optimal whatever the sign of the value-write association $χ$; only when $χ> 0$ does the optimum turn non-monotone, sending a robot's most valuable memories off its flash.   The pivot is thus empirical, and we measure $χ$ on real robot logs at a pre-specified gate: its sign is a property of the deployment regime -- positive on recurrent long-horizon manipulation ($\hatχ \approx +1.0 \times 10^{-3}$, replicated at full power), null on a shorter-horizon suite, and negative on non-recurrent teleoperation. Two boundaries scope the result. The endurance budget is dormant on premium 3,000-P/E TLC at datasheet prices and binding on the commodity QLC/eMMC ($\sim$1,000 P/E) that cheaper edge robots run. And where it binds, a learned wear-aware controller only ties price-based routing on task value, because realized value is tier-invariant across RAM, NVM, and cloud: the rent governs device lifetime and cost, not task performance. Whether wear-aware placement improves task value remains open -- $χ$ is measured against a value proxy, and the non-monotone optimum, while proven, is not yet observed in data.

### 🤖 AI 总结

**一句话总结**：A robot's flash endurance is a non-renewable stock: every persisted write spends one of a few thousand program/erase cycles and never refills, yet no fielded robot memory system prices which memories ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Memory, Wasting, Asset, Pricing, Flash, Endurance, Embodied

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18144v1) | [下载PDF](https://arxiv.org/pdf/2606.18144v1.pdf)

---

## [7. Your AI Travel Agent Would Book You a Bullfight: An Agentic Benchmark for Implicit Animal Welfare in Frontier AI Models](https://arxiv.org/abs/2606.18142v1)

**作者**：Jasmine Brazilek, Oliver Tulio, Joel Christoph 等 6 位作者  
**分类**：cs.AI, cs.CL, cs.CY  
**发布时间**：2026-06-16

### 📄 论文摘要

AI agents are moving from advisors to actors, booking travel, planning menus, and running procurement on behalf of users. Existing benchmarks for AI and animal welfare evaluate model text responses to question-answer prompts, leaving open whether the welfare reasoning surfaced in those responses transfers to agentic deployment where the model must take actions with tools. We introduce TAC (Travel Agent Compassion), the first agentic benchmark measuring whether AI agents avoid options involving animal exploitation when acting on behalf of users. TAC presents an AI agent with twelve hand-authored travel booking scenarios across six categories of animal exploitation, augmented to forty-eight samples to control for price, rating, and position confounds. We evaluate seven frontier models from four labs. Every model scores below the chance level of sixty-four percent, with the best performer (Claude Opus 4.7) at fifty-three percent. A single welfare-aware sentence in the system prompt yields gains of forty-seven to sixty-three percentage points in Claude and GPT-5.5, twenty-six points in GPT-5.2, and under twelve points in DeepSeek and Gemini. An auxiliary Inspect Scout audit of 288 base-condition transcripts from the top two performers, using Gemini 2.5 Flash Lite as judge, flags zero transcripts for evaluation awareness, suggesting the below-chance rates do not stem from the models recognising the evaluation. We discuss implications for category-level variation across cultural domains, the limits of text-response welfare benchmarks, and the EU General-Purpose AI Code of Practice systemic risk framework.

### 🤖 AI 总结

**一句话总结**：AI agents are moving from advisors to actors, booking travel, planning menus, and running procurement on behalf of users. Existing benchmarks for AI and animal welfare evaluate model text responses to...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, An, Travel, Would, Book, Bullfight, Agentic, Benchmark

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18142v1) | [下载PDF](https://arxiv.org/pdf/2606.18142v1.pdf)

---

## [8. Knowledge Reutilization in Meta-Reinforcement Learning](https://arxiv.org/abs/2606.18132v1)

**作者**：Yuan Meng, Bo Wang, Juan de los Rios Ruiz 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-16

### 📄 论文摘要

Meta-reinforcement learning enables fast adaptation by extracting shared structure from related tasks, but existing end-to-end methods often couple task inference with embodiment-specific control. This coupling can obscure non-parametric task semantics, reduce sample efficiency, and limit cross-agent reuse. We propose a meta-knowledge reutilization framework that learns task-level knowledge on a dynamics-simplified agent and transfers it to heterogeneous agents. The framework uses a Bayesian non-parametric prior to organize latent task modes and a high-level policy to generate task-level magnitude guidance. To bridge reusable task knowledge with different embodiments, we introduce a semantic-magnitude interface and a lightweight temporal adaptor, which convert frozen meta-knowledge into temporally aligned subgoals for embodiment-specific low-level controllers. Experiments on multiple locomotion agents show that our framework reduces final-step tracking error by 94.75% -- 99.79% compared with recent state-of-the-art baselines and achieves comparable deployment performance with about 23.8% of their interaction data.

### 🤖 AI 总结

**一句话总结**：Meta-reinforcement learning enables fast adaptation by extracting shared structure from related tasks, but existing end-to-end methods often couple task inference with embodiment-specific control. Thi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Knowledge, Reutilization, Meta-Reinforcement, Learning, enables, fast, adaptation, extracting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18132v1) | [下载PDF](https://arxiv.org/pdf/2606.18132v1.pdf)

---

## [9. First Proof Second Batch](https://arxiv.org/abs/2606.18119v1)

**作者**：Mohammed Abouzaid, Nikhil Srivastava, Rachel Ward 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-16

### 📄 论文摘要

To assess the ability of current AI systems to correctly solve research-level mathematics problems, we tested several AI systems on a set of ten problems in a broad range of mathematical fields; these problems arose naturally in the research process of the contributors. This document includes the problems, our methodology, and the results of our testing. We provide links to supplementary documents including the human solutions, the AI-generated solutions, and the referee reports and logs for the AI-generated solutions.   The ten problems were contributed by the following mathematicians: (1) Dariusz Kalociński and Theodore A. Slaman, (2) Richard Schwartz, (3) Aleksa Milojevic and Benny Sudakov, (4) Larry Guth, (5) Oleg Butkovsky, Jonathan Mattingly, and Lorenzo Zambotti, (6) Joshua Evan Greene and Duncan McCoy, (7) Sucharit Sarkar, (8) Sam Payne and Jidong (Jayden) Wang, (9) Sylvie Corteel and John Lentfer, (10) Srivatsav Kunnawalkam Elayavalli.

### 🤖 AI 总结

**一句话总结**：To assess the ability of current AI systems to correctly solve research-level mathematics problems, we tested several AI systems on a set of ten problems in a broad range of mathematical fields; these...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, First, Proof, Second, Batch, assess, ability, current

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18119v1) | [下载PDF](https://arxiv.org/pdf/2606.18119v1.pdf)

---

## cs.CL

## [10. Variable-Width Transformers](https://arxiv.org/abs/2606.18246v1)

**作者**：Zhaofeng Wu, Oliver Sieberling, Shawn Tan 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-16

### 📄 论文摘要

Scaling model size, specifically depth and width, has driven significant progress in transformer-based language models. However, most architectures maintain a constant width across all layers, allocating a fixed parameter and computation budget evenly despite different layers potentially playing distinct computational roles. In this work, we empirically investigate nonuniform capacity allocation across network depth by proposing a $\times$-shaped > <former architecture. This design maintains wider early and late layers while narrowing the middle layers, utilizing a parameter-free residual resizing mechanism. Across decoder-only language models ranging from 200M to 2B parameters (dense) and 3B parameters (MoE), our > <former consistently outperforms parameter-matched uniform baselines on language modeling loss. By reducing the average layer width, this architecture also requires fewer overall FLOPs (22% reduction under fitted loss-matched scaling curves) and smaller KV cache memory and I/O cost (15% reduction). In analysis, we show that this bottleneck structure results in qualitatively different representations in residual streams. Overall, our results demonstrate that nonuniform width allocation can result in more resource-optimal scaling of language models.

### 🤖 AI 总结

**一句话总结**：Scaling model size, specifically depth and width, has driven significant progress in transformer-based language models. However, most architectures maintain a constant width across all layers, allocat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Variable-Width, Transformers, Scaling, model, size, specifically, depth, width

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18246v1) | [下载PDF](https://arxiv.org/pdf/2606.18246v1.pdf)

---

## [11. ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues](https://arxiv.org/abs/2606.18237v1)

**作者**：Shanda Li, Qiuhong Anna Wei, Jingwu Tang 等 8 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-06-16

### 📄 论文摘要

Reproducing research results from papers and released code is central to scientific progress. Existing works have introduced benchmarks to evaluate whether LLM agents can assist with reproducibility, but they are difficult to scale due to their reliance on substantial manual effort for data curation and evaluation. We introduce ReproRepo, a scalable framework for reproducibility evaluation that leverages human-raised GitHub issues as naturally occurring supervision on realistic reproduction blockers. We instantiate ReproRepo on 1,149 recent machine learning papers from major conferences and evaluate four frontier model-agent configurations. Our results show that LLM agents, even without executing code, can identify many real-world reproducibility problems from paper-repository pairs: the best agent in our study, namely Codex with GPT-5.5, surfaces at least one semantically related human-reported blocker for ~90% of papers in the study. Further analysis shows that agents are particularly effective for surfacing visible failures and identifying the right semantic region, but may still be insufficient in exact localization. ReproRepo can serve as a reusable, scalable framework for future evaluations of LLM agents on real-world reproducibility auditing. Our code is released at https://github.com/LithiumDA/ReproRepo.

### 🤖 AI 总结

**一句话总结**：Reproducing research results from papers and released code is central to scientific progress. Existing works have introduced benchmarks to evaluate whether LLM agents can assist with reproducibility, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ReproRepo, Scaling, Reproducibility, Audits, Issues, Reproducing, research, results

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18237v1) | [下载PDF](https://arxiv.org/pdf/2606.18237v1.pdf)

---

## [12. Darshana Graph: A Parallel Commentary Corpus for Comparative Indian Philosophy, with Stylometric and Exploratory Graph Analyses](https://arxiv.org/abs/2606.18222v1)

**作者**：Joy Bose  
**分类**：cs.CL, cs.DL  
**发布时间**：2026-06-16

### 📄 论文摘要

We introduce Darshana Graph, a corpus of over 125,000 text records spanning classical Hindu, Buddhist, and Jain philosophical traditions, drawn from public-domain and openly licensed translations of sources including the Bhagavad Gita, Brahma Sutras, principal Upanishads, the Pali Canon, and core Jain texts. Its distinctive contribution lies in a structurally unique subset of roughly 8,500 Hindu and Jain records in which the same root verse or sutra is aligned across eighteen historical commentators representing five schools of Vedanta and other darshanas, enabling direct comparison of how independent interpretive traditions read identical source material. To our knowledge, no publicly available resource provides comparable cross-commentator alignment at this scale. We present two analyses built on this corpus. First, a transparent stylometric comparison requiring no machine learning measures argumentative style through scriptural citation density, explicit refutation rate, and sentence complexity. It finds a moderate negative correlation between citation density and refutation rate, a marked increase in refutation rate across three commentators in a related doctrinal lineage, and measurable genre-level differences within the Pali Canon itself. Second, we describe a constrained large language model pipeline that extracts typed philosophical relationships between concepts using a predefined relation vocabulary and deterministic post-hoc validation. The resulting graph surfaces cross-school disagreement patterns while also revealing important extraction limitations, including cases where an independent embedding-based analysis disagrees with the graph-derived findings. We release the full corpus, extracted relationship graph, and all source code.

### 🤖 AI 总结

**一句话总结**：We introduce Darshana Graph, a corpus of over 125,000 text records spanning classical Hindu, Buddhist, and Jain philosophical traditions, drawn from public-domain and openly licensed translations of s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Darshana, Graph, Parallel, Commentary, Corpus, Comparative, Indian, Philosophy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18222v1) | [下载PDF](https://arxiv.org/pdf/2606.18222v1.pdf)

---

## [13. Zone of Proximal Policy Optimization: Teacher in Prompts, Not Gradients](https://arxiv.org/abs/2606.18216v1)

**作者**：Byung-Kwan Lee, Ximing Lu, Shizhe Diao 等 11 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-16

### 📄 论文摘要

Knowledge distillation transfers a teacher's competence to a small student but is brittle in the small-student regime: forcing the student to imitate logits from a much larger teacher concentrates it on the teacher's sharpest modes, hurting generalization on benchmark families beyond the training corpus. Reinforcement learning (RL) avoids logit imitation by training on the student's own rollouts. However, on questions where every rollout fails-yielding zero advantage and being silently discarded-injecting a stronger teacher's response into the policy gradient breaks the on-policy assumption and induces drift. We introduce Zone of Proximal Policy Optimization (ZPPO), inspired by Vygotsky's zone of proximal development, which keeps the teacher inside the prompt rather than the policy gradient. On hard questions, ZPPO constructs two reformulated prompts: a Binary Candidate-included Question (BCQ) pairs one correct teacher response with one incorrect student response as anonymized candidates the student must discriminate, and a Negative Candidate-included Question (NCQ) aggregates the student's wrong rollouts into a single prompt to surface their shared failure modes. A prompt replay buffer recirculates each hard question until it either graduates-the student's mean rollout accuracy on it reaches half- or is FIFO-evicted under finite capacity, amplifying BCQ and NCQ inside the student's current zone of proximal development. On the Qwen3.5 family at four student scales (0.8B-9B) with a 27B teacher, post-trained as vision-language models and evaluated on a 31-benchmark suite (16 VLM, 10 LLM, 5 Video), ZPPO outperforms off/on-policy distillation and GRPO, with the largest gains at the smallest scale.

### 🤖 AI 总结

**一句话总结**：Knowledge distillation transfers a teacher's competence to a small student but is brittle in the small-student regime: forcing the student to imitate logits from a much larger teacher concentrates it ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Zone, Proximal, Policy, Optimization, Teacher, Prompts, Not

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18216v1) | [下载PDF](https://arxiv.org/pdf/2606.18216v1.pdf)

---

## [14. Analyzing and Encoding the Al-Mawrid Arabic-English Dictionary with the ISO Language Markup Framework and TEI Lex-0](https://arxiv.org/abs/2606.18205v1)

**作者**：Diaa Fayed, Laurent Romary  
**分类**：cs.CL  
**发布时间**：2026-06-16

### 📄 论文摘要

This paper presents a robust methodology for the systematic digitization and encoding of the Al-Mawrid Arabic-English dictionary, transforming it from a legacy print resource into a standardized computational lexicon. Addressing a significant gap in Arabic lexical infrastructure, the study adopts a dual-standard framing that aligns the ISO Lexical Markup Framework (LMF) with the Text Encoding Initiative TEI Lex-0 guidelines. By applying an editorial view to the dictionary's macro- and microstructure, the research resolves the structural ambiguities and punctuation inconsistencies typical of 20th-century bilingual dictionaries. The methodology is grounded in an empirical analysis of the dictionary's lexical knowledge density. Drawing on a representative sample (the letter Ayn, comprising 4.6% of the total volume), the study provides scientific weight to the encoding process, demonstrating a structural parsing accuracy of 91%. Quantitative evaluation of the information extraction rules reveals high performance, with 85% precision and 98% recall for synonyms, and 88% precision for other morpho-semantic features. Beyond technical description, the paper provides a critical comparison with existing Arabic lexical resources and discusses the limitations of TEI Lex-0 when modelling specific Arabic phenomena, such as implicit "open set" semantic relations and scattered morphological cues. Furthermore, the study explores the potential for Linguistic Linked Open Data (LLOD) integration by establishing a scalable prefix-based referencing system that facilitates the resource's inclusion in the semantic web. The result is an interoperable, machine-tractable resource that provides a reproducible workflow for the retro-digitization of complex legacy bilingual lexicons within the Arabic NLP and Digital Humanities communities.

### 🤖 AI 总结

**一句话总结**：This paper presents a robust methodology for the systematic digitization and encoding of the Al-Mawrid Arabic-English dictionary, transforming it from a legacy print resource into a standardized compu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Analyzing, Encoding, Al-Mawrid, Arabic-English, Dictionary, ISO, Language, Markup

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18205v1) | [下载PDF](https://arxiv.org/pdf/2606.18205v1.pdf)

---

## [15. RubricsTree: Scalable and Evolving Open-Ended Evaluation of Personal Health Agents across Health Memory and Medical Skills](https://arxiv.org/abs/2606.18203v1)

**作者**：Weizhi Zhang, Zechen Li, Hamid Palangi 等 19 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-16

### 📄 论文摘要

The LLM-empowered personal health agents with user health (sensor) metrics have offered a promising pathway to alleviate global disparities in healthcare access. However, large-scale clinical deployment remains constrained by an open-ended evaluation bottleneck: physician annotation is reliable but costly and unscalable, while LLM-as-a-judge evaluators are scalable but subjective, inconsistent, and sometimes clinically misaligned. We introduce RubricsTree, a scalable evaluation framework with an expert-aligned hierarchical taxonomy of over 100 atomic, clinically-verifiable Boolean rubrics, evolving from the insights of 4,000 real user queries through an iterative human-in-the-loop curation protocol with an expertise panel led by an experienced physician. A context-aware adaptive router activates only the relevant auto-weighted rubric subset per query, providing the throughput needed for scalable evaluation with expert-aligned quality. Through a systematic meta-evaluation, we show that RubricsTree (i) substantially exceeds a strong large-scale evaluation baseline in expert alignment on challenging open-ended queries; (ii) reliably penalizes contextually degraded responses; and (iii) when used as structured instructions, text feedback, or training rewards for performance optimization, yields up to ~66% relative gains on HealthBench for Gemini, GPT, and Qwen model families. RubricsTree thus provides a scalable, auditable, and evolving evaluation infrastructure required for the continuous optimization of product-level personal healthcare AI.

### 🤖 AI 总结

**一句话总结**：The LLM-empowered personal health agents with user health (sensor) metrics have offered a promising pathway to alleviate global disparities in healthcare access. However, large-scale clinical deployme...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, RubricsTree, Scalable, Evolving, Open-Ended, Evaluation, Personal, Health

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18203v1) | [下载PDF](https://arxiv.org/pdf/2606.18203v1.pdf)

---

## [16. Unintended Effects of Geographic Conditioning in Large Language Models](https://arxiv.org/abs/2606.18124v1)

**作者**：Naz Col, David M. Chan  
**分类**：cs.CL  
**发布时间**：2026-06-16

### 📄 论文摘要

Modern conversational AI systems frequently rely on user metadata to localize responses, yet the unintended regional biases introduced by this hidden context remain poorly understood. In this work, we evaluate location leakage: the phenomenon where a model generates geographic references despite receiving a geographically neutral user prompt. Across both creative writing and open-ended Q&A prompts, even state-of-the-art LLMs systematically favor region-specific outputs when exposed to location metadata, with leakage spiking by up to 793 times above baseline (e.g., from 0.04% to 31.7% for Llama 3.1-8B, and 21.3% and 8.8% for Qwen3-8B and Claude Sonnet 4.6, respectively). Our analysis further shows a novel structural conditioning effect: replacing the injected location with the placeholder "Unknown" still elevates leakage by up to 72 times above baseline, demonstrating that the user profile frame itself, independent of any geographic content, acts as a generative conditioning signal.

### 🤖 AI 总结

**一句话总结**：Modern conversational AI systems frequently rely on user metadata to localize responses, yet the unintended regional biases introduced by this hidden context remain poorly understood. In this work, we...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Unintended, Effects, Geographic, Conditioning, Large, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18124v1) | [下载PDF](https://arxiv.org/pdf/2606.18124v1.pdf)

---

## cs.CV

## [17. Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion](https://arxiv.org/abs/2606.18250v1)

**作者**：Nils Morbitzer, Jonathan Evers, Artem Savkin 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-16

### 📄 论文摘要

Forecasting the evolution of dynamic environments is crucial for autonomous agents. While generative world models have recently achieved high photorealism in 2D video synthesis by mixing ego-motion and environmental dynamics within the image plane, they exhibit physical inconsistencies, such as morphing or vanishing objects, especially over long time horizons. In this paper, we propose FR3D, a world model that predicts a persistent 3D latent representation for future dynamic 3D reconstruction. Unlike prior works that treat the world as a sequence of image-based features, FR3D explicitly decouples the 3D evolution of the scene from the agent's trajectory, treating the inferred ego-motion as a latent proxy for action. This disentanglement resolves the ambiguities between self-motion and world-motion, ensuring geometric consistency into the future. Furthermore, we introduce a teacher-student distillation strategy that leverages the spatial "common sense" of off-the-shelf foundation models, leading to robust zero-shot generalization. Extensive experiments demonstrate FR3D's strong performance for future dynamic 3D reconstruction from monocular observations across multiple datasets, even 2 seconds into the future. Project page: https://fr3d-wm.github.io.

### 🤖 AI 总结

**一句话总结**：Forecasting the evolution of dynamic environments is crucial for autonomous agents. While generative world models have recently achieved high photorealism in 2D video synthesis by mixing ego-motion an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Future, Dynamic, Reconstruction, World, Model, Disentangled, Ego-Motion

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18250v1) | [下载PDF](https://arxiv.org/pdf/2606.18250v1.pdf)

---

## [18. MOCHI: Motion Enhancement of Collaborative Human-object Interactions](https://arxiv.org/abs/2606.18243v1)

**作者**：Jiye Lee, Yonghun Choi, Jungdam Won  
**分类**：cs.CV, cs.GR, cs.RO  
**发布时间**：2026-06-16

### 📄 论文摘要

Collaborative human-object interaction shows dynamic and complex movements that require mutual anticipation and continuous adjustment between participants and the shared object. Modeling such collaborative multi-human object interaction (MHOI) scenarios requires high-quality data acquisition as a foundational step; however, this is challenging due to the inherent complexity of MHOI where human-human and human-object interactions occur simultaneously. Such complexity leads to noisy MHOI captures characterized by several artifacts: contact misalignment between hands and objects, motion jitter and temporal inconsistencies in the captured sequences, and missing or incomplete finger-level articulation details. To address these challenges, we present MOCHI (MOtion Enhancement of Collaborative Human-object Interactions), a two-stage framework for enhancing noisy MHOI data. Our approach first generates physically plausible hand grasps through optimization from noisy body input, producing grasps that are both physically plausible and semantically consistent with the body pose, where these optimized grasps are extended into complete hand-object interaction sequences. Consequently, the full-body motion for all participants are refined through a diffusion-based noise optimization framework that uses single-person motion priors. During the optimization process, we introduce optimization objectives to encode human-object and human-human interaction information within these single-person priors. Experimental results demonstrate the effectiveness of our pipeline across diverse MHOI data, either acquired by existing capture methods or synthesized by generative models. We further show robustness of our system across varying numbers of participants and types of interactions, and demonstrate various applications including keyframe-based MHOI creation and data augmentation through varying object geometries.

### 🤖 AI 总结

**一句话总结**：Collaborative human-object interaction shows dynamic and complex movements that require mutual anticipation and continuous adjustment between participants and the shared object. Modeling such collabor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, MOCHI, Motion, Enhancement, Collaborative, Human-object, Interactions, interaction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18243v1) | [下载PDF](https://arxiv.org/pdf/2606.18243v1.pdf)

---

## [19. EventDrive: Event Cameras for Vision-Language Driving Intelligence](https://arxiv.org/abs/2606.18242v1)

**作者**：Dongyue Lu, Rong Li, Ao Liang 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-16

### 📄 论文摘要

Event cameras sense the world through asynchronous brightness changes with microsecond latency and high dynamic range, offering motion fidelity far beyond frame-based sensors and capturing temporal structure that conventional exposures often miss. These properties make events a powerful complement to RGB in autonomous driving, especially under blur, glare, and rapid motion, where frame-based perception can become unreliable. However, existing event-aware vision-language models remain limited to generic perception and do not reveal how event sensing contributes to reasoning and decision-making across the full driving loop. We present EventDrive, a large-scale benchmark and model suite that unifies event streams, RGB frames, and language supervision across four core dimensions: Perception, Understanding, Prediction, and Planning, covering captions, structured QA, grounding, motion-state recognition, trajectory forecasting, and planning tasks. Building on this foundation, EventDrive-VLM introduces a multi-horizon event pyramid and a temporal-horizon mixture-of-experts module to adaptively encode and fuse asynchronous and frame-based information for downstream reasoning. Comprehensive evaluation across diverse tasks shows that event streams provide substantial gains in temporal precision, motion awareness, and robustness, bringing event sensing into the center of driving intelligence.

### 🤖 AI 总结

**一句话总结**：Event cameras sense the world through asynchronous brightness changes with microsecond latency and high dynamic range, offering motion fidelity far beyond frame-based sensors and capturing temporal st...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EventDrive, Event, Cameras, Vision-Language, Driving, Intelligence, sense, world

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18242v1) | [下载PDF](https://arxiv.org/pdf/2606.18242v1.pdf)

---

## [20. Adaptive Volumetric Mechanical Property Fields Invariant to Resolution](https://arxiv.org/abs/2606.18231v1)

**作者**：Rishit Dagli, Donglai Xiang, Vismay Modi 等 7 位作者  
**分类**：cs.CV, cs.LG, cs.RO  
**发布时间**：2026-06-16

### 📄 论文摘要

Accurate mechanical properties (or materials) Young's modulus ($E$), Poisson's ratio ($ν$) and density ($ρ$) are essential for reliable physics simulation of digital worlds, but most 3D assets lack this information. We propose AdaVoMP, a method for predicting accurate dense spatially-varying ($E$, $ν$, $ρ$) for input 3D objects across representations, improving the resolution, accuracy, and memory efficiency over the state-of-the-art. The foundation of our technique is a sparse and adaptive voxel structure SAV that efficiently represents both the input 3D shape and the material field output. We replace the fixed-voxel model of the most accurate prior method, VoMP, with a novel sparse transformer encoder-decoder model that learns to generate a unique SAV autoregressively for every input shape to represent its materials, achieving a resolution $16^3\times$ higher than prior art. Experiments show that AdaVoMP estimates more accurate volumetric properties, even with lesser test-time compute than all prior art. This allows us to convert high-resolution complex 3D objects into simulation-ready assets, resulting in realistic deformable simulations.

### 🤖 AI 总结

**一句话总结**：Accurate mechanical properties (or materials) Young's modulus ($E$), Poisson's ratio ($ν$) and density ($ρ$) are essential for reliable physics simulation of digital worlds, but most 3D assets lack th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Adaptive, Volumetric, Mechanical, Property, Fields, Invariant, Resolution, Accurate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18231v1) | [下载PDF](https://arxiv.org/pdf/2606.18231v1.pdf)

---

## [21. ReAge3D: Re-Aging 3D Faces with View Consistency](https://arxiv.org/abs/2606.18156v1)

**作者**：Libing Zeng, Li Ma, Mingming He 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-16

### 📄 论文摘要

We present a novel framework for realistic and controllable 3D face re-aging which produces highly detailed, identity-preserving results. Existing 3D editing methods, while effective for coarse semantic changes, are not well suited for re-aging, as even small inconsistencies across re-aged 2D views can lead to over-smoothing of subtle but perceptually important age-related details. To address this challenge, we first introduce a 2D diffusion-based re-aging model, DiffReaging, trained on synthetically generated image pairs. We further propose a center-out editing propagation strategy that leverages this re-aging model to reconstruct multi-view-consistent re-aged images. Specifically, starting from a re-aged frontal pivot view, we reconstruct the remaining views through warping and our proposed Masked-DiffReaging process. By injecting existing content at every step of the diffusion process, Masked-DiffReaging ensures that the reconstructed regions remain coherent with existing pixels. The resulting consistent set of re-aged views supervises the optimization of the re-aged 3D representation. Our method outperforms existing 3D editing techniques both visually and quantitatively, enabling smooth, fine-grained control over age transformations in 3D face models.

### 🤖 AI 总结

**一句话总结**：We present a novel framework for realistic and controllable 3D face re-aging which produces highly detailed, identity-preserving results. Existing 3D editing methods, while effective for coarse semant...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, We, ReAge3D, Re-Aging, Faces, View, Consistency, present

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18156v1) | [下载PDF](https://arxiv.org/pdf/2606.18156v1.pdf)

---

## [22. Neural Tree Reconstruction for the Open Forest Observatory](https://arxiv.org/abs/2606.18153v1)

**作者**：Marissa Ramirez de Chanlatte, Arjun Rewari, Trevor Darrell 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-16

### 📄 论文摘要

The Open Forest Observatory (OFO) is a collaboration across universities and other partners to make low-cost forest mapping accessible to ecologists, land managers, and the general public. The OFO is building both a database of geospatial forest data as well as open-source methods and tools for forest mapping by uncrewed aerial vehicle. Such data are useful for a variety of climate applications including prioritizing reforestation efforts, informing wildfire hazard reduction, and monitoring carbon sequestration. In the current iteration of the OFO's forest map database, 3D tree maps are created using classical structure-from-motion techniques. This approach is prone to artifacts, lacks detail, and has particular difficulty on the forest floor where the input data (overhead imagery) has limited visibility. These reconstruction errors can potentially propagate to the downstream scientific tasks (e.g. a wildfire simulation.) Advances in 3D reconstruction, including methods like Neural Radiance Fields (NeRF), produce higher quality results that are more robust to sparse views and support data-driven priors. We explore ways to incorporate NeRFs into the OFO dataset, outline future work to support even more state-of-the-art 3D vision models, and describe the importance of high-quality 3D reconstructions for forestry applications.

### 🤖 AI 总结

**一句话总结**：The Open Forest Observatory (OFO) is a collaboration across universities and other partners to make low-cost forest mapping accessible to ecologists, land managers, and the general public. The OFO is ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Neural, Tree, Reconstruction, Open, Forest, Observatory, OFO, collaboration

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18153v1) | [下载PDF](https://arxiv.org/pdf/2606.18153v1.pdf)

---

## [23. Predicting Immune Biomarkers with MultiModal Mixture-of-Expert Pathology Foundation Models Empowers Precision Oncology](https://arxiv.org/abs/2606.18123v1)

**作者**：Tianyu Liu, Ziqing Wang, Zhaokang Liang 等 15 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-16

### 📄 论文摘要

Predicting immune biomarkers associated with the tumor immune microenvironment (TIME) is critical for advancing precision oncology, yet existing approaches are largely limited to single image modalities and suffer from insufficient resolution and incomplete utilization of complementary clinical and biological information. Here we introduce MixTIME, a multimodal foundation model that leverages a mixture-of-experts (MoE) architecture to integrate pathology foundation models trained across distinct modalities: image only (UNIv2), image text (CONCHv1.5), and image transcriptomic (STPath) representations for pixel-level and slide-level prediction of multiplex immunofluorescence (mIF) protein expression from hematoxylin and eosin (HE) whole-slide images. MixTIME employs a learnable router to dynamically weight expert contributions and is trained with a distribution- and tendency-aware loss function. Benchmarked on two datasets of different scales, MixTIME achieves state-of-the-art performance across 17 protein markers as measured by correlation metrics. The predicted mIF profiles substantially enhance downstream tasks, including spatial domain identification, survival prediction, and AI-assisted pathology report generation validated by expert pathologists from multiple institutes across the world. Furthermore, MixTIME enables longitudinal tracking of protein expression dynamics across clinical time points and reveals protein gene interaction patterns linked to drug resistance and immune suppression in tumor microenvironments. Collectively, MixTIME provides a scalable framework for multimodal biomarker discovery and clinical translation in computational pathology.

### 🤖 AI 总结

**一句话总结**：Predicting immune biomarkers associated with the tumor immune microenvironment (TIME) is critical for advancing precision oncology, yet existing approaches are largely limited to single image modaliti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Predicting, Immune, Biomarkers, MultiModal, Mixture-of-Expert, Pathology, Foundation, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18123v1) | [下载PDF](https://arxiv.org/pdf/2606.18123v1.pdf)

---

## [24. HLS-GPT: A Generative Pretrained Transformer (GPT) for Continental-Scale NASA Harmonized Landsat and Sentinel-2 (HLS) Reflectance Reconstruction Across All Bands on Arbitrary Dates](https://arxiv.org/abs/2606.18115v1)

**作者**：Junjie Li, Hankui K. Zhang, David P. Roy  
**分类**：cs.CV  
**发布时间**：2026-06-16

### 📄 论文摘要

Recent deep learning methods for Landsat and Sentinel-2 reflectance time series reconstruction remain limited by restricted spectral coverage, limited geographic scalability, or patch-based designs with short temporal contexts. We present HLS-GPT, a large-scale generative pretrained Transformer model for reconstructing NASA Harmonized Landsat Sentinel-2 30 m surface reflectance for all bands, any date, and any pixel location. HLS-GPT uses a hierarchical Transformer architecture to handle the different spectral band configurations of Landsat and Sentinel-2 and operates on single-pixel 12-month time series. To capture geographic and seasonal variability, the model was trained with nine years of HLS time series from more than 0.25 million training pixels across the conterminous United States. A random cropping and masking strategy extracts 12-month periods with varying start dates across epochs, masks 50% of valid observations, and trains the model to reconstruct the masked reflectance values from the remaining observations. Evaluation using more than 62,000 independent test pixels shows robust reconstruction under diverse land surface conditions, including complex crop phenology and sparse, irregular observations. Leave-one-observation-out evaluation achieved reconstruction RMSE below 0.026 for all HLS spectral bands, with relative RMSE below 35% for visible bands and below 13% for other bands. Red-edge band errors were comparable to red and near-infrared errors despite the absence of red-edge bands on Landsat. Sensitivity analyses that randomly masked 10% to 90% of test observations showed only modest degradation when 10% to 50% of observations were masked, with all-band RMSE below 0.028. Image reconstruction over nine independent 109 by 109 km CONUS HLS tiles further demonstrates that HLS-GPT outperforms two conventional methods and the NASA-IBM Prithvi model.

### 🤖 AI 总结

**一句话总结**：Recent deep learning methods for Landsat and Sentinel-2 reflectance time series reconstruction remain limited by restricted spectral coverage, limited geographic scalability, or patch-based designs wi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HLS-GPT, Generative, Pretrained, Transformer, GPT, Continental-Scale, NASA, Harmonized

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18115v1) | [下载PDF](https://arxiv.org/pdf/2606.18115v1.pdf)

---

## cs.LG

## [25. Sign-Rank, Index, and List Replicability: Connections and Separations](https://arxiv.org/abs/2606.18236v1)

**作者**：Ari Blondal, Hamed Hatami, Pooya Hatami 等 5 位作者  
**分类**：cs.LG, cs.IT  
**发布时间**：2026-06-16

### 📄 论文摘要

In learning theory, the sign rank of a binary concept class captures the smallest dimension in which it can be represented by points and halfspaces. Despite tremendous interest, lower bounds on sign rank are notoriously difficult to come by. Two recent approaches to the problem establish lower bounds on sign rank by measures that are easier to analyze: the $\mathbb{Z}_2$-index and the list replicability number.   We order these measures, showing that the $\mathbb{Z}_2$-index is upper-bounded by a linear function of the list replicability number. As a main consequence, we obtain a strong separation between sign rank and $\mathbb{Z}_2$-index, thereby resolving a question of Frick, Hosseini, and Vasileuski.   This motivates a thorough study of list replicability, the stronger of the two lower-bounding measures. We establish upper bounds on the list replicability number by two combinatorial measures: height and minimum star number. We also prove a fundamental composition result, showing that the product of two concept classes has list replicability number bounded by the sum of the list replicability numbers of the two classes.

### 🤖 AI 总结

**一句话总结**：In learning theory, the sign rank of a binary concept class captures the smallest dimension in which it can be represented by points and halfspaces. Despite tremendous interest, lower bounds on sign r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sign-Rank, Index, List, Replicability, Connections, Separations, learning, theory

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18236v1) | [下载PDF](https://arxiv.org/pdf/2606.18236v1.pdf)

---

## [26. Rethinking Dataset Distillation for Classification: Do Distilled Sets Outperform Coresets?](https://arxiv.org/abs/2606.18209v1)

**作者**：Trisha Mittal, Akshay Mehra, Joshua Kimball  
**分类**：cs.LG  
**发布时间**：2026-06-16

### 📄 论文摘要

Dataset distillation (DD) has emerged as a prominent approach in data centric machine learning, aiming to synthesize compact training sets for efficient training by compressing the information in large datasets into a small number of synthetic samples. However, DD methods are often evaluated under inconsistent evaluation protocols, ranging from standard ERM to single/multi-teacher supervision, making it difficult to isolate the effectiveness of distilled data from evaluation. Moreover, many prior methods claim that DD outperforms data pruning approaches such as coreset selection (CS), based on the assumption that restricting condensed datasets to subsets of real samples fundamentally limits their expressiveness. In this work, we critically evaluate DD methods through large-scale experiments using standardized datasets and evaluation protocols to assess their intrinsic effectiveness. We benchmark seven state-of-the-art (SOTA) DD methods on ImageNet-1K, ImageNet100, and ImageNette, using three widely adopted training protocols against three CS strategies. Our results show that while some DD methods fail to outperform even simple random subsets, the SOTA DD approaches are comparable to or worse than coresets on large-scale datasets and incur a substantially higher cost for construction. Beyond accuracy, we also evaluate the representativeness, diversity, and quality of condensed sets, and find that coresets consistently achieve better coverage of the original data distribution. These findings highlight the limited practical advantages of current DD methods and show that coresets remain competitive and are often a more computationally efficient alternative for data-centric learning.

### 🤖 AI 总结

**一句话总结**：Dataset distillation (DD) has emerged as a prominent approach in data centric machine learning, aiming to synthesize compact training sets for efficient training by compressing the information in larg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, Rethinking, Dataset, Distillation, Classification, Distilled, Sets, Outperform

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18209v1) | [下载PDF](https://arxiv.org/pdf/2606.18209v1.pdf)

---

## [27. Looped World Models](https://arxiv.org/abs/2606.18208v1)

**作者**：Hongyuan Adam Lu, Z. L. Victor Wei, Qun Zhang 等 31 位作者  
**分类**：cs.LG, cs.AI, cs.CL, cs.CV  
**发布时间**：2026-06-16

### 📄 论文摘要

Current world models face a fundamental tension: faithful long-horizon simulation demands deep computation, but deeper models are expensive to deploy and prone to compounding errors. We resolve this by introducing Looped World Models (LoopWM), which are the first looped architectures for world modelling. Our method iteratively refines latent environment states through a parameter-shared transformer block. This yield up to 100x parameter efficiency over conventional approaches with adaptive computation that automatically scales depth to match the complexity of each prediction step. Orthogonal to scaling model size and training data, LoopWM establishes iterative latent depth as a new scaling axis for world simulation, which might significantly push the community forward.

### 🤖 AI 总结

**一句话总结**：Current world models face a fundamental tension: faithful long-horizon simulation demands deep computation, but deeper models are expensive to deploy and prone to compounding errors. We resolve this b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Looped, World, Models, Current, face, fundamental, tension, faithful

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18208v1) | [下载PDF](https://arxiv.org/pdf/2606.18208v1.pdf)

---

## [28. Kolmogorov Regression for Robust Diffusion Policies](https://arxiv.org/abs/2606.18186v1)

**作者**：Lekan Molu  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-16

### 📄 论文摘要

Finite-dimensional (FD) diffusion policies exhibit temporal drift owing to discretization artifacts that degrade long-horizon performance (when deployed on physical systems). We introduce a backward Kolmogorov equation that lifts diffusion policies to a Cameron-Martin space -- a subset of the Hilbert space. Essentially, replacing stochastic score matching with a deterministic boundary-value PDE problem. Our core innovation thrives on Gaussian measure theory whereupon the diffusion noise covariance operator is realized from a colored noise distribution which prescribes a notion of regularity on samples from the model at inference time. We train the diffusion model with a derived precision-weighted Cameron- Martin loss and a Kolmogorov residual is introduced as a PDE diagnostic during inference. These substitutions yield (i) convergence guarantees where the bound's constants depend on the effective rank of the kernel rather than action dimension, (ii) improved trajectory regularity via spectral weighting, and (iii) a deterministic failure detector without reward signals. Validation across two application domains demonstrates substantial improvements: on the PushT manipulation benchmark, the Cameron-Martin loss achieves a 17% improvement in maximum episode reward (0.95 vs. 0.78 for MSE) and 67.6% reduction in inter-step drifts during inference via the introduced residual magnitude. Similarly, on a 6-station manufacturing line with constant work-in-process (CONWIP) flow control, we achieve 28.4% lower RMSE than classical LSTM baselines; a high starvation-event recall (1.0 in test cycles), and effective bottleneck identification (Precision@1 = 1.0 in test set, 13x signal-to-noise ratio). We then certify the dispatch policies with Hamilton-Jacobi reachability theory which reduces deadlock events by 96% compared to uncontrolled dispatch over 100 simulated runs (351 events prevented).

### 🤖 AI 总结

**一句话总结**：Finite-dimensional (FD) diffusion policies exhibit temporal drift owing to discretization artifacts that degrade long-horizon performance (when deployed on physical systems). We introduce a backward K...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, FD, Kolmogorov, Regression, Robust, Policies, Finite-dimensional, exhibit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18186v1) | [下载PDF](https://arxiv.org/pdf/2606.18186v1.pdf)

---

## [29. Embedded Machine Learning for Microcontroller-Class Edge Devices: Data, Feature, Evaluation, and Deployment Pipelines](https://arxiv.org/abs/2606.18122v1)

**作者**：Mostafa Darvishi  
**分类**：cs.LG, cs.AI, cs.AR, eess.AS, eess.SP  
**发布时间**：2026-06-16

### 📄 论文摘要

Embedded machine learning moves inference from cloud services to resource-constrained devices that must acquire data, preprocess signals, run a model, and act within tight limits on memory, energy, and latency. This paper presents a systems-oriented synthesis of an embedded machine-learning workflow for microcontroller-class platforms. The emphasis is placed on engineering decisions that are often hidden in generic machine-learning introductions: sampling and buffering, feature extraction as dimensionality reduction, validation under class imbalance, model/runtime co-design, and streaming deployment. Two representative signal families are used throughout the paper. The first is inertial motion recognition, where a two-second, three-axis accelerometer window is transformed from raw samples into root-mean-square and spectral features before classification. The second is keyword spotting, where audio is sampled, anti-aliased, transformed into mel-frequency cepstral coefficients, and processed by a compact one-dimensional convolutional network. The paper concludes with practical design rules for robust on-device inference, including data curation, quantization, thresholding, scheduling, and field monitoring.

### 🤖 AI 总结

**一句话总结**：Embedded machine learning moves inference from cloud services to resource-constrained devices that must acquire data, preprocess signals, run a model, and act within tight limits on memory, energy, an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Embedded, Machine, Learning, Microcontroller-Class, Edge, Devices, Data, Feature

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18122v1) | [下载PDF](https://arxiv.org/pdf/2606.18122v1.pdf)

---

## [30. Learning Fair Pareto-Optimal Policies in Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2606.18111v1)

**作者**：Umer Siddique, Peilang Li, Yongcan Cao  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-16

### 📄 论文摘要

Fairness is an important aspect of decision-making in multi-objective reinforcement learning (MORL), where policies must ensure both optimality and equity across multiple, potentially conflicting objectives. While single-policy MORL methods can learn fair policies for fixed user preferences using welfare functions such as the generalized Gini welfare function (GGF), they fail to provide the diverse set of policies necessary for dynamic or unknown user preferences. To address this limitation, we formalize the fair optimization problem in multi-policy MORL, where the goal is to learn a set of Pareto-optimal policies that ensure fairness across all possible user preferences. Our key technical contributions are threefold: (1) We show that for concave, piecewise-linear welfare functions (e.g., GGF), fair policies remain in the convex coverage set (CCS), which is an approximated Pareto front for linear scalarization. (2) We demonstrate that non-stationary policies, augmented with accrued reward histories, and stochastic policies improve fairness by dynamically adapting to historical inequities. (3) We propose three novel algorithms, which include integrating GGF with multi-policy multi-objective Q-Learning (MOQL), state-augmented multi-policy MOQL for learning non-statoinary policies, and its novel extension for learning stochastic policies. We evaluate our algorithms across various domains and compare our methods against the state-of-the-art MORL baselines. The empirical results show that our methods learn a set of fair policies that accommodate different user preferences.

### 🤖 AI 总结

**一句话总结**：Fairness is an important aspect of decision-making in multi-objective reinforcement learning (MORL), where policies must ensure both optimality and equity across multiple, potentially conflicting obje...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Learning, Fair, Pareto-Optimal, Policies, Multi-Objective, Reinforcement, Fairness

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.18111v1) | [下载PDF](https://arxiv.org/pdf/2606.18111v1.pdf)

---

