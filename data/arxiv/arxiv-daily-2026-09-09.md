# arXiv AI 论文日报 | 2026-09-09

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (6 篇)
- [cs.CV](#csCV) (6 篇)
- [cs.AI](#csAI) (9 篇)
- [cs.LG](#csLG) (9 篇)

---

## cs.AI

## [1. Procedural Graphs: Self-Evolving Execution Structures for LLM Agents](https://arxiv.org/abs/2609.09153v1)

**作者**：Yuxing Lu, Yicheng Chen, Shanchan Wu 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.MA  
**发布时间**：2026-09-08

### 📄 论文摘要

Large language models are increasingly deployed as agents that plan over long horizons and act through external tools. Most agents select actions through unconstrained generation over an accumulating history, leaving implicit the procedural knowledge of what to do, in what order, and under which conditions. As trajectories lengthen, agents can lose track of their objectives, invoke tools out of order, and repeat unproductive actions. We introduce the Procedural Graph: just as a knowledge graph organizes factual knowledge into (entity, relation, entity) triplets for what-is questions, a Procedural Graph organizes procedural knowledge into (procedure, relation, procedure) triplets for what-to-do questions. At each decision step, the framework localizes the agent's active node, and a guidance model translates the surrounding subgraph into step-level situational guidance that biases the solver's next action without dictating it. The graph is self-evolving: an LLM refiner contrasts failed trajectories with successful ones and edits the graph's topology and attributes, committing edits that preserve or improve held-out validation performance while retaining rejected ones to discourage repetition. Starting from a minimal skeleton, the loop builds graphs that match or surpass hand-designed ones. It can also repair a flawed expert prior. Across multiple datasets, task types, and LLMs, the Procedural Graph delivers consistent gains over memory-based baselines, and self-evolution further improves performance without manual engineering.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly deployed as agents that plan over long horizons and act through external tools. Most agents select actions through unconstrained generation over an accumulating ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, Procedural, Graphs, Self-Evolving, Execution, Structures, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09153v1) | [下载PDF](https://arxiv.org/pdf/2609.09153v1.pdf)

---

## [2. A Data-Driven Framework for Identifying and Prioritizing RPA Opportunities in Healthcare Processes](https://arxiv.org/abs/2609.09137v1)

**作者**：Maria Alejandra Gomez, Juan Manuel Castillo  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-09-08

### 📄 论文摘要

Robotic Process Automation (RPA) is widely used to reduce administrative burden in United States hospitals, yet an estimated 30-50% of RPA initiatives underperform because processes are selected informally, without a repeatable method to catalogue candidates, prioritize them, match each to an automation tier -- a Python bot, an open-source orchestrator such as n8n, or an enterprise platform such as UiPath -- and forecast financial return before committing resources. We propose a four-module, data-driven framework unifying these decisions: a Process Taxonomy of twenty recurring hospital processes across five value streams; a Prioritization module deriving an Automation Suitability Index from an Analytic Hierarchy Process matrix with an explicit consistency check; a Tool-Tier Selection module recommending the least-cost technology sufficient for a process complexity, integration, and compliance profile; and a Return-on-Investment module quantifying labor savings, error-cost avoidance, payback, and net present value. Applied to a synthetic portfolio spanning all twenty processes, plus a reference data-flow architecture linking it to hospital EHR/payer/ERP systems: 12 of 20 clear the prioritization threshold; the ranking is robust to +/-20% weight perturbation (Spearman correlation 0.83, top-5 set preserved 97.7%, 2,000 Monte Carlo trials); an Automation Risk Index flags four qualifying processes as Critical risk; a budget-constrained portfolio optimization shows diminishing marginal NPV as spend scales from $400K to $1.03M; and a second Monte Carlo analysis shows portfolio NPV stays positive at its 5th percentile. The framework is a conceptual synthesis of the literature rather than an instrument calibrated on primary hospital data; we discuss HIPAA governance and a research agenda for empirical validation. A supplementary Python implementation accompanies the paper.

### 🤖 AI 总结

**一句话总结**：Robotic Process Automation (RPA) is widely used to reduce administrative burden in United States hospitals, yet an estimated 30-50% of RPA initiatives underperform because processes are selected infor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Data-Driven, Framework, Identifying, Prioritizing, RPA, Opportunities, Healthcare, Processes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09137v1) | [下载PDF](https://arxiv.org/pdf/2609.09137v1.pdf)

---

## [3. Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails](https://arxiv.org/abs/2609.09134v1)

**作者**：Zhou Yu, Bin Bi, Shiva Kumar Pentyala 等 11 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-08

### 📄 论文摘要

Agent harnesses (the system prompt, tool set, execution hooks, and context-management scaffolding around a model) are a critical determinant of agentic task success. Automated harness evolution can enable smaller models to perform well on domain-specific tasks at a fraction of frontier-model cost. Since both the harness and model weights shape behavior, we ask how harness evolution and lightweight fine-tuning should be combined. Across seven enterprise agent tasks, we first evolve a harness with the weaker model, then find that a stronger expert often uses it more effectively, suggesting expert supervision could close the remaining gap. However, training the weaker model on the expert's complete trajectories under the evolved harness backfires: performance regresses on all seven tasks by 4 to 30 points across Qwen3-Coder and Gemma 4, even though the same procedure helps under the unevolved harness. Our analysis shows that imitation transfers knowledge and increases scaffold usage, but disrupts model-harness fit: the weaker model adopts the expert's planning strategy without the competence to execute it and no longer matches the harness evolved around its native planning style. We therefore develop an on-policy expert-correction pipeline, automated by a meta-level MLE agent, that localizes the failing turn in the weaker model's own rollout and asks the expert to rewrite only that turn. This preserves the model's planning style and combines the gains of harness evolution and model adaptation. Our results identify and resolve a source of contention between harness and weight updates, yielding a compatibility-preserving recipe for economical co-evolution on domain-specific enterprise tasks.

### 🤖 AI 总结

**一句话总结**：Agent harnesses (the system prompt, tool set, execution hooks, and context-management scaffolding around a model) are a critical determinant of agentic task success. Automated harness evolution can en...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Co-Evolving, Harnesses, Models, On-Policy, Correction, Helps, Weaker, Catch

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09134v1) | [下载PDF](https://arxiv.org/pdf/2609.09134v1.pdf)

---

## [4. ExecCritic: Learn to Test, Test to Improve for Coding Agents](https://arxiv.org/abs/2609.09133v1)

**作者**：Leitian Tao, Baolin Peng, Haorui Wang 等 10 位作者  
**分类**：cs.AI, cs.CL, cs.SE  
**发布时间**：2026-09-08

### 📄 论文摘要

Execution feedback can guide coding agents toward correct repository repairs, but only when the tests capture the behavior requested by the issue. Agent-generated tests can encode incomplete or incorrect behavioral targets; when the same trajectory writes both the patch and the test, their errors can agree and create false confidence. We introduce ExecCritic, combining a test--verify--revise scaffold with a role-specific reinforcement learning recipe for training agents within it. The scaffold separates test construction from source-code repair: a Test agent independently generates repository-native tests, a fail-closed harness qualifies and freezes them, and a Repair agent revises source code from their execution feedback without changing the tests. Both roles use Qwen-3.5-35B-A3B as the backbone and are trained separately. In Learn to Test, the Test agent learns to produce behaviorally valid tests that distinguish correct from incorrect patches. In Test to Improve, the Repair agent learns both direct task resolution and feedback-guided revision. On SWE-bench Verified, test quality determines whether feedback helps: holding the base Repair agent fixed, tests from the base Test agent reduce resolved rate from a no-test baseline of 61.2% to 57.3%, whereas tests from GPT-5.6-sol raise it to 65.3%. Role-specific post-training raises the Qwen Test agent's Base-to-Gold success from 22.2% to 62.2%; composing the two post-trained Qwen agents reaches 72.6%, an 11.4-point gain over the original no-test baseline without stronger-model or Oracle feedback at evaluation time. Code is publicly available at https://github.com/MSR-Orchard/execcritic.

### 🤖 AI 总结

**一句话总结**：Execution feedback can guide coding agents toward correct repository repairs, but only when the tests capture the behavior requested by the issue. Agent-generated tests can encode incomplete or incorr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, ExecCritic, Learn, Test, Improve, Coding, Execution, feedback

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09133v1) | [下载PDF](https://arxiv.org/pdf/2609.09133v1.pdf)

---

## [5. A Generalization of Amari's Bayesian Duality](https://arxiv.org/abs/2609.09126v1)

**作者**：Mohammad Emtiyaz Khan, Thomas Möllenhoff  
**分类**：cs.AI, cs.LG, stat.ML  
**发布时间**：2026-09-08

### 📄 论文摘要

Amari's contributions to information geometry and machine learning are well known. Here, we revisit Amari's work on Bayesian duality which has not received as much attention. We connect Amari's Bayesian duality to a convex duality of Bayes' rule. Using this connection, we present a generalization of Amari's Bayesian duality and discuss its relevance for modern artificial intelligence.

### 🤖 AI 总结

**一句话总结**：Amari's contributions to information geometry and machine learning are well known. Here, we revisit Amari's work on Bayesian duality which has not received as much attention. We connect Amari's Bayesi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Generalization, Amari's, Bayesian, Duality, contributions, information, geometry

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09126v1) | [下载PDF](https://arxiv.org/pdf/2609.09126v1.pdf)

---

## [6. SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?](https://arxiv.org/abs/2609.09113v1)

**作者**：Yuqiao Tan, Shizhu He, Jun Zhao 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-09-08

### 📄 论文摘要

While research on recursive self-improvement (RSI) has predominantly automated model training pipelines, reliable autonomous development demands a missing pillar: post-hoc monitoring and auditing to understand what models learn and ensure safe alignment. Mechanistic interpretability tools are essential to bridge this gap, among which Sparse Autoencoders (SAEs) serve as a cornerstone by isolating interpretable features for model inspection and steering. In this paper, we introduce SAEScientist-Bench to evaluate whether AI agents can act as scientists utilizing SAE tools for autonomous mechanistic discovery. Given a target concept, an agent designs contrastive probes and navigates a Gemma Scope dictionary of 131K+ features in Gemma-2-9B-IT to discover the optimal feature, evaluated against curated expert reference features anchored on Neuronpedia across activation rank, concept selectivity on contrastive texts, and causal steering. Across 10 agent configurations and 20 tasks, frontier agents demonstrate genuine discovery capabilities and lead different evaluation dimensions, but remain well behind the expert baseline, approaching expert levels on separating target concepts from contrastive controls while lagging substantially in causal generation steering. Further analysis reveals that although agents can design contrasts to rule out spurious candidates, they frequently misinterpret experimental measurements. These results establish experimental model understanding as a measurable capability for closed-loop autonomous AI R&D. Our code is available at https://github.com/Trae1ounG/SAEScientist.

### 🤖 AI 总结

**一句话总结**：While research on recursive self-improvement (RSI) has predominantly automated model training pipelines, reliable autonomous development demands a missing pillar: post-hoc monitoring and auditing to u...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SAEScientist-Bench, Can, Conduct, Autonomous, SAE, Interpretability, Research?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09113v1) | [下载PDF](https://arxiv.org/pdf/2609.09113v1.pdf)

---

## [7. Everything in Moderation: Per-Domain Coverage Optima and Alignment-Resistant Domain Gaps in Multi-Domain Mid-Training](https://arxiv.org/abs/2609.09081v1)

**作者**：Yunpeng Xu, Kun Zheng  
**分类**：cs.AI  
**发布时间**：2026-09-08

### 📄 论文摘要

Mid-training, the stage between pre-training and alignment, is where a model's per-domain data composition is typically set by data availability rather than principled design. We ask what that decision buys, and whether a later alignment pass can undo it. In a controlled logical-reasoning setting (Qwen3-8B-Base, with a 4B replication; five semantically rule-disjoint KOR-Bench domains) we train 30 allocations spanning the five-domain simplex, 24 sweep configurations plus six withheld from the fit, at five seeds each. Three findings emerge. First, every domain has an interior coverage optimum: the moderate band ($10\%$-$40\%$) is best for all five domains, and a calibrated permutation test for quadratic interiority gives $P\approx0.010$; the fitted mid-training-only curves, with 8B peaks between $9.9\%$ and $35.1\%$, reproduce for curve shape but not peak location. Second, the gaps survive a fixed-budget alignment pass: compensatory SFT raises 116/120 cells (mean $+4.32\%$) yet bridges $0/240$ pairs at a $5\%$ threshold and $30/240$ at a $10\%$ ratio, an equal-budget uniform control behaves almost identically, and a permutation null would bridge $13.8\pm3.3$ and $77.9\pm8.5$ pairs ($P<0.001$). Third, zero coverage collapses mid-training-only accuracy, though a FineWeb-Edu-only control shows the collapse is commingled with generic drift. An exploratory $θ^*$ allocation attains the largest full-pipeline gain ($+4.36\%$ vs. $+0.80\%$/$+0.64\%$\,pp) but is marginal under Welch test.

### 🤖 AI 总结

**一句话总结**：Mid-training, the stage between pre-training and alignment, is where a model's per-domain data composition is typically set by data availability rather than principled design. We ask what that decisio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Everything, Moderation, Per-Domain, Coverage, Optima, Alignment-Resistant, Domain, Gaps

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09081v1) | [下载PDF](https://arxiv.org/pdf/2609.09081v1.pdf)

---

## [8. Time-Varying Data as Sheaves: an Invitation to Narratives](https://arxiv.org/abs/2609.09056v1)

**作者**：Wilmer Leal, Benjamin Merlin Bumpus, Jana K. Nickel 等 6 位作者  
**分类**：cs.AI, cs.MA, eess.SY, math.CT  
**发布时间**：2026-09-08

### 📄 论文摘要

Modern science and engineering increasingly rely on time-varying data, yet the mathematical tools used to model temporal phenomena are often developed within separate disciplines, obscuring common principles and limiting the transfer of ideas across fields. This chapter presents the theory of narratives, an abstract framework for time-varying objects of any mathematical kind that supports both theoretical investigations and applications. To illustrate this perspective, the chapter develops three vignettes, each illustrating a different research direction. The first addresses a general concern: What information loss can occur when switching between different representations of temporal data? The second concerns structural and algorithmic approaches: How can we systematically decompose time-varying data into simple pieces and obtain invariants describing its structural complexity? The third is an application to control theory: How can we model multi-agent systems with switching communication topologies? More important than any individual vignette, the central message of this invitation is that a suitable abstract perspective can organize and guide research across remarkably diverse mathematical and scientific domains.

### 🤖 AI 总结

**一句话总结**：Modern science and engineering increasingly rely on time-varying data, yet the mathematical tools used to model temporal phenomena are often developed within separate disciplines, obscuring common pri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, an, Time-Varying, Data, Sheaves, Invitation, Narratives, Modern

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09056v1) | [下载PDF](https://arxiv.org/pdf/2609.09056v1.pdf)

---

## [9. Answer-Distribution Trajectories: A Stochastic-Dynamics View of LLM Reasoning](https://arxiv.org/abs/2609.09030v1)

**作者**：Mar Gonzàlez I Català, Haitz Sáez de Ocáriz Borde, Davide Murari 等 6 位作者  
**分类**：cs.AI, cs.CL, cs.IT, cs.LG  
**发布时间**：2026-09-08

### 📄 论文摘要

Chain-of-thought reasoning provides a structured computation between a model's input and final answer. Yet it is often evaluated through endpoint accuracy, which ignores the path taken to reach that answer. An emerging line of work addresses this limitation using entropy profiles, which track how uncertainty evolves over the reasoning process but do not reveal which competing hypotheses account for that uncertainty. We introduce answer-distribution trajectories, a stochastic-dynamics-inspired representation that tracks the model's full predictive distribution over answers as reasoning unfolds. As a strictly finer representation than endpoint and entropy summaries, answer-distribution trajectories enable us to characterize a trace through a dynamical reasoning profile spanning exploration, revision, motion, and commitment, and to distinguish different dynamical mechanisms of reasoning success and failure. Across sixteen open-weight language models and four reasoning benchmarks, we show that traces with the same endpoint and similar entropy profiles can exhibit substantially different reasoning dynamics. We further find substantial variation in these dynamics both within and across models and tasks, with different objectives favoring different dynamical profiles. Additionally, we show that training and inference choices systematically reshape these profiles. Our results suggest that answer-distribution trajectories provide a rich framework for analysing and evaluating the dynamics of LLM reasoning.

### 🤖 AI 总结

**一句话总结**：Chain-of-thought reasoning provides a structured computation between a model's input and final answer. Yet it is often evaluated through endpoint accuracy, which ignores the path taken to reach that a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Answer-Distribution, Trajectories, Stochastic-Dynamics, View, Reasoning, Chain-of-thought

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09030v1) | [下载PDF](https://arxiv.org/pdf/2609.09030v1.pdf)

---

## cs.CL

## [10. ReCite: Agentic Reasoning for Faithful Citation](https://arxiv.org/abs/2609.09156v1)

**作者**：Yuyang Huang, Bobo Li, Jiajia Song 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-08

### 📄 论文摘要

Accurate citations are the foundation of academic writing, tracing intellectual origins and substantiating core claims. However, manually navigating the growing volume of scientific literature is increasingly difficult, prompting reliance on automatic citation recommendation. While modern retrieval-augmented architectures have largely mitigated the fabrication of non-existent papers, current systems relying on semantic similarity struggle with misattribution, often citing authentic papers that fail to logically support the author's claim. To address this challenge, we argue that accurate citation requires a shift from similarity-based search to active, claim-level reasoning. We propose ReCite, a decoupled agentic framework that orchestrates location perception, intent-aware query planning, and reflective verification. Trained on synthesized reasoning trajectories, our agent verifies claim-evidence consistency and triggers self-correction loops when retrieved candidates lack logical support. Experiments demonstrate that our lightweight framework outperforms state-of-the-art massive generative models in strict citation accuracy. By grounding literature matching in verifiable logic rather than semantic overlap, ReCite establishes a reliable foundation for automated academic writing.

### 🤖 AI 总结

**一句话总结**：Accurate citations are the foundation of academic writing, tracing intellectual origins and substantiating core claims. However, manually navigating the growing volume of scientific literature is incr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ReCite, Agentic, Reasoning, Faithful, Citation, Accurate, citations, foundation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09156v1) | [下载PDF](https://arxiv.org/pdf/2609.09156v1.pdf)

---

## [11. Measuring LLM Sycophancy under Sustained Multi-Turn Pressure](https://arxiv.org/abs/2609.09090v1)

**作者**：Leyuan Tang, Kangda Wei, Tianyu Jiang 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-08

### 📄 论文摘要

Large language models (LLMs) may abandon correct positions when users push back, exhibiting a failure mode known as sycophancy. Existing evaluations typically use short, pre-specified conversations and may therefore miss failures that emerge under sustained, adaptive disagreement. We introduce SPINE, a benchmark in which an LLM proxy plays a persistent but mistaken user and adaptively challenges a target model for up to 25 turns. We evaluate four production systems and three Olmo3-7b variants on 100 false-presupposition and 100 unethical-query items. Our experimental results show that collapse rates increase with conversation length for every model, short-horizon protocols underestimate sycophancy and resistance under sustained pressure remains unreliable across current models. By analyzing models with accessible reasoning traces, we surprisingly found that the correct position often remains represented in a reasoning trace when the response concedes, suggesting that the model chooses to please a user and sycophancy is not due to lack of knowledge or ignorance. Ablations show that adaptive LLM proxy exposes more sycophantic collapse than pre-generated scripts. Among all tactics, emotional appeals is the most associated with inducing LLM sycophantic behavior. The code and data are released at https://anonymous.4open.science/r/SPINE

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) may abandon correct positions when users push back, exhibiting a failure mode known as sycophancy. Existing evaluations typically use short, pre-specified conversations an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Measuring, Sycophancy, under, Sustained, Multi-Turn, Pressure, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09090v1) | [下载PDF](https://arxiv.org/pdf/2609.09090v1.pdf)

---

## [12. ActReview: Rebuttal-Guided Training Data and Rubric Rewards for Actionable Peer Review Generation](https://arxiv.org/abs/2609.09076v1)

**作者**：Yiling Ma, Yilun Zhao, Sihong Wu 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-08

### 📄 论文摘要

As LLMs are increasingly used for pre-submission self-review, there is growing demand for feedback that not only identifies weaknesses but also guides authors toward concrete revisions. We study this as Actionable Peer-review Generation and decompose it into two subtasks: diagnostic claim generation and revision suggestion generation. We introduce ActReview, a rebuttal-guided post-training framework that connects paper-specific diagnoses to concrete, grounded revision plans. Our central insight is that author rebuttals reveal plausible actions for addressing reviewer concerns and can therefore provide latent supervision for revision-oriented feedback. From real review-rebuttal threads on OpenReview, we construct ActReview-40K by aligning reviewer weaknesses with author responses and grounding the resulting feedback in localized paper evidence. We post-train Qwen3-8B-Base with multi-task supervised fine-tuning followed by GRPO using candidate-aware, weakness-specific rubric rewards. We also introduce ActReview-Bench, a human-curated benchmark of 1,000 instances for evaluating diagnostic quality and revision usefulness. Experiments show that ActReview outperforms prior specialized review-generation models on actionability and grounding while remaining competitive with strong prompt-based LLMs. Human evaluation confirms improved revision usefulness while revealing a remaining gap in technical accuracy, and additional analyses support generalization to held-out papers and robustness across independent judges.

### 🤖 AI 总结

**一句话总结**：As LLMs are increasingly used for pre-submission self-review, there is growing demand for feedback that not only identifies weaknesses but also guides authors toward concrete revisions. We study this ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ActReview, Rebuttal-Guided, Training, Data, Rubric, Rewards, Actionable, Peer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09076v1) | [下载PDF](https://arxiv.org/pdf/2609.09076v1.pdf)

---

## [13. ToolLoop: Closed-Loop Tool-Use Data Synthesis via Decomposed Generation and Dynamic Self-Feedback](https://arxiv.org/abs/2609.09072v1)

**作者**：Min Zeng, Yuzhou Liu, Zhenyu Cao 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-08

### 📄 论文摘要

High-quality tool-use data is critical for training language models to interact effectively with external tools. However, existing synthetic approaches typically follow a generate-then-filter paradigm with static post-hoc verification, often yielding inefficient data with imbalanced feature distributions. We propose ToolLoop, a closed-loop framework that decomposes synthesis into three progressive stages: (1) sampling function name combinations as ground truth; (2) backward derivation of user queries; and (3) forward derivation of tool calls. At each stage, dynamic self-feedback iteratively guides the model toward high-quality generation, realizing a transition from generate-then-filter to generate-verify-refine. On the Berkeley Function Calling Leaderboard (BFCL), a 4B parameter model trained with our 11K synthetic examples achieves 86.40% accuracy in non-reasoning mode, while an Isolate variant that removes BFCL-overlapping candidate functions still reaches 86.07\%. Cross-benchmark evaluation on ACEBench further demonstrates strong generalization, with 72.1% overall accuracy using only 18.3% of baseline training data.

### 🤖 AI 总结

**一句话总结**：High-quality tool-use data is critical for training language models to interact effectively with external tools. However, existing synthetic approaches typically follow a generate-then-filter paradigm...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ToolLoop, Closed-Loop, tool-use, Data, Synthesis, via, Decomposed, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09072v1) | [下载PDF](https://arxiv.org/pdf/2609.09072v1.pdf)

---

## [14. Performance of Clinical AI System and Physicians and Frontier Language Models in primary care diagnostics](https://arxiv.org/abs/2609.09070v1)

**作者**：Andy Nkansah, Hanna Plotnitskaya, Stanislau Salavei 等 9 位作者  
**分类**：cs.CL, cs.AI, cs.HC  
**发布时间**：2026-09-08

### 📄 论文摘要

Clinical AI evaluation should encompass diagnosis and management after adaptive information gathering. We compared Doctorina, eight physicians and four standalone frontier language models in 150 synthetic Polish-language primary-care consultations. Doctorina achieved 82.0% Top-1 concordance versus 57.0% for physicians (difference, 25.0 percentage points; 95% confidence interval, 17.7-32.7) and 97.3% versus 85.0% primary-or-reference-differential concordance. Across 149 case pairs, normalized workup and treatment scores were 89.4 versus 66.9 and 83.7 versus 61.2. Doctorina had the highest diagnostic point estimates among all six groups; Kimi K3 ranked next, while Claude Opus 5 led the closely spaced management estimates of Opus, Doctorina and Kimi. A second Doctorina execution reproduced the advantages over physicians across all outcomes. Doctorina's advantage over physicians therefore extended from primary-diagnosis selection to higher-rated diagnostic workup and initial treatment after adaptive consultation.

### 🤖 AI 总结

**一句话总结**：Clinical AI evaluation should encompass diagnosis and management after adaptive information gathering. We compared Doctorina, eight physicians and four standalone frontier language models in 150 synth...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Performance, Clinical, System, Physicians, Frontier, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09070v1) | [下载PDF](https://arxiv.org/pdf/2609.09070v1.pdf)

---

## [15. The Audit Decides the Verdict: Instrument Effects Rival Demographic Bias in LLM Decision Audits](https://arxiv.org/abs/2609.09048v1)

**作者**：Siddharth Vohra, Manikandan Ravikiran  
**分类**：cs.CL, cs.AI, cs.CY  
**发布时间**：2026-09-08

### 📄 论文摘要

Whether a language model looks demographically biased can depend on how the audit asks its question. A charitable-aid benchmark reports that the same models favor minority applicants when rating requests one at a time and penalize some when ranking side by side. We test whether that reversal generalizes to hiring, lending, and medical triage: 40,726 requests to five models, applications differing only in the applicant's name, and a primary test fixed before collection. It does not. None of 36 planned contrasts survives correction. The rating advantage keeps its sign at roughly half the published size, and a precision extension bounds any hiring ranking penalty below the published effect, though the lending and triage ranking floors sit above that margin, so the exclusion is conclusive for hiring ranking and for rating in all three domains only. Planted disparities tracking their injected sizes and a directional replication on the original aid materials bound these nulls. The audit is livelier than the demographics: models recognize transparent audits nearly always, tie every identical-content comparison whether the varying detail is race or a hobby, and reward first-listed candidates as much as any demographic effect we measure. Audit verdicts reflect audit construction more than demographic bias.

### 🤖 AI 总结

**一句话总结**：Whether a language model looks demographically biased can depend on how the audit asks its question. A charitable-aid benchmark reports that the same models favor minority applicants when rating reque...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Audit, Decides, Verdict, Instrument, Effects, Rival, Demographic, Bias

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09048v1) | [下载PDF](https://arxiv.org/pdf/2609.09048v1.pdf)

---

## cs.CV

## [16. SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators](https://arxiv.org/abs/2609.09155v1)

**作者**：Yuncong Yang, Zhengtao Han, Furkan Ozyurt 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-08

### 📄 论文摘要

World models are increasingly used as policy-in-the-loop imagination environments, where reliable rollouts require fine-grained controllability with respect to low-level robot actions. A key obstacle to scaling such models in robotics is that actions are not a universal language in pixel space: changes in visual environment, camera view, robot placement, or embodiment alter how the same numerical action manifests visually, leading to conflicting supervision under mixed training and brittle generalization at deployment. We introduce SyncWorld, an action-conditioned world model that serves as a zero-shot simulator across unseen environments without any additional training. SyncWorld leverages a visual calibration episode---paired frames and actions that showcase all the controllable degrees of freedom---to specify the setup-specific Action--Visual Mapping in context. Training with visual calibration contexts teaches the model to interpret actions through visual evidence and to leverage interaction history when explicit calibration is unavailable. Experiments show that SyncWorld can accurately simulate action outcomes in previously unseen settings, and that its capability of simulating rollouts enables test-time policy improvement without training.

### 🤖 AI 总结

**一句话总结**：World models are increasingly used as policy-in-the-loop imagination environments, where reliable rollouts require fine-grained controllability with respect to low-level robot actions. A key obstacle ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, SyncWorld, Visual, Calibration, Enables, World, Models, Zero-Shot

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09155v1) | [下载PDF](https://arxiv.org/pdf/2609.09155v1.pdf)

---

## [17. Point4D: Long-range 4D Motion Reconstruction](https://arxiv.org/abs/2609.09145v1)

**作者**：Minsik Jeon, Jay Karhade, Deva Ramanan 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-08

### 📄 论文摘要

We introduce Point4D, a feed-forward model for 4D reconstruction of long-range video sequences. Point4D is able to reliably infer dense per-point 3D trajectories across multi-hundred-frame videos, unlike existing 4D methods that are limited to short input windows of at most a few dozen frames. A key innovation that enables this is our flexible 3D query-based motion decoder that decouples trajectory prediction from image-plane visibility. The predicted 3D endpoints are then directly re-queried in the next chunk without re-projection or matching. Furthermore, we show that extracting and reusing a visual descriptor from an arbitrary frame where the point is visible leads to better performance than relying solely on the source patch. Overall, Point4D achieves state-of-the-art performance across diverse long-video tracking benchmarks spanning over 200 frames and largely outperforms previous feed-forward 4D method. Project page: https://point-4d.github.io

### 🤖 AI 总结

**一句话总结**：We introduce Point4D, a feed-forward model for 4D reconstruction of long-range video sequences. Point4D is able to reliably infer dense per-point 3D trajectories across multi-hundred-frame videos, unl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, We, Point4D, Long-range, Motion, Reconstruction, introduce, feed-forward

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09145v1) | [下载PDF](https://arxiv.org/pdf/2609.09145v1.pdf)

---

## [18. Canonical Color as a Lens into Concept Decodability in Vision Encoders and VLMs](https://arxiv.org/abs/2609.09124v1)

**作者**：Xiaofu Chen, Stella Frank, Yova Kementchedjhieva  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-09-08

### 📄 论文摘要

Visual encoders construct a representation of the image input for Vision-Language models. How much conceptual, as opposed to immediately visible, information does this representation contain? We use canonical color as a controlled test case to ask whether vision encoders make canonical-color information linearly accessible, even when color is removed from the input image. We construct a dataset of objects with canonical colors, and probe vision encoders for both color and object identity using color and grayscale images. We find that canonical color remains decodable from grayscale images, and is tied to predicted object identity, indicating a conceptual link. Extending this analysis to full VLMs, we find that VLM post-training can have a surprisingly large effect on color decodability in the vision encoder. Overall, canonical color provides a usefully controllable lens for tracing object-level conceptual semantic information in vision encoders and VLMs.

### 🤖 AI 总结

**一句话总结**：Visual encoders construct a representation of the image input for Vision-Language models. How much conceptual, as opposed to immediately visible, information does this representation contain? We use c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Canonical, Color, Lens, Concept, Decodability, Vision, Encoders

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09124v1) | [下载PDF](https://arxiv.org/pdf/2609.09124v1.pdf)

---

## [19. GoDeep: Annotation-Free Open-Vocabulary 3D Scene Understanding via Language-Space Lifting](https://arxiv.org/abs/2609.09082v1)

**作者**：Thodoris Betsas, Anastasios Doulamis, Andreas Georgopoulos  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-09-08

### 📄 论文摘要

Open vocabulary 3D semantic segmentation methods typically lift CLIP features into 3D. This embeds points in a joint vision-language space known to behave like a bag-of-words on compositional tasks. Furthermore, even annotation free variants often require a large 3D training corpus and a dedicated 3D encoder per domain. Instead we use a vision-language model purely as a translator. It produces structured, entity-level descriptions of each posed image. These descriptions are grounded, projected, and aggregated directly in a general-purpose, language-only embedding space, with no 3D training corpus or encoder required. On ScanNet++, our pipeline is competitive with strong annotation free baselines trained on ScanNet. On a 5-building cultural heritage benchmark, raw scores initially favor a CLIP-based variant, but a single systematic vocabulary correction reverses this ranking. An effect confirmed by a second, independent correction on a different class, indicating that language-space embeddings track physical content more faithfully. This fidelity extends to genuinely out-of-vocabulary (OOV) objects on ScanNet++ proving that language-space embeddings separate presence from absence objects far more sharply than CLIP-based embeddings do. GoDeep also localize these OOV objects within the scene, all without any 2D-3D annotation. Because every representation remains discrete text, predictions are also explainable at the point level. Finally, exploiting both a heuristic weighting, that favors precise over merely frequent observations and GoDeep's explainability property, we propose an aggregation strategy, as a proof of concept, that favors finer elements localization.

### 🤖 AI 总结

**一句话总结**：Open vocabulary 3D semantic segmentation methods typically lift CLIP features into 3D. This embeds points in a joint vision-language space known to behave like a bag-of-words on compositional tasks. F...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, GoDeep, Annotation-Free, Open-Vocabulary, Scene, Understanding, via, Language-Space

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09082v1) | [下载PDF](https://arxiv.org/pdf/2609.09082v1.pdf)

---

## [20. "World Knowledge" in the Weights: Reading Concept Circuits of Vision Transformers](https://arxiv.org/abs/2609.09055v1)

**作者**：Yanlin Chen, Tang Li, Xi Peng  
**分类**：cs.CV  
**发布时间**：2026-09-08

### 📄 论文摘要

Vision transformers (ViTs) have achieved remarkable generalization across visual domains, yet little is known about how they internally represent the structure of the world. To address this gap, we use Cross-Layer Transcoders (CLTs) to read concept circuits from ViTs: directed graphs whose nodes correspond to sparse, interpretable concepts and edges capture concept interactions across layers. Our method yields two complementary views of model behavior. The global concept circuit is input-invariant and can be recovered directly from learned cross-layer weights, exposing the reusable "world knowledge" encoded in the model. The instance concept circuit is input-dependent and identifies the concepts and pathways actually used for a specific prediction, enabling faithful example-level explanations. We demonstrate the utility of concept circuits in three ways: (1) Automatic spurious correlation discovery: leveraging the statistics of our global concept circuits to identify shortcut dependencies within the model. (2) Spurious correlation removal: intervening on the instance concept circuit to steer the model towards correct predictions. Empirical results show that our method outperforms existing counterparts by 11.0% on the Waterbird dataset. (3) Model comparison: contrasting the global concept circuits of different foundation models (e.g., CLIP vs. DINO) to reveal how supervision paradigms shape representational structure. Our code is available at https://github.com/deep-real/VisionCLT

### 🤖 AI 总结

**一句话总结**：Vision transformers (ViTs) have achieved remarkable generalization across visual domains, yet little is known about how they internally represent the structure of the world. To address this gap, we us...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, "World, Knowledge", Weights, Reading, Concept, Circuits, Vision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09055v1) | [下载PDF](https://arxiv.org/pdf/2609.09055v1.pdf)

---

## [21. Task-driven Processing with Coarse-to-Fine Glimpse-based Active Perception](https://arxiv.org/abs/2609.09025v1)

**作者**：Oleh Kolner, Thomas Ortner, Stanisław Woźniak 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-08

### 📄 论文摘要

State-of-the-art vision models process images in their entirety, lacking the ability to selectively zoom in on relevant regions. This limitation is particularly acute in scenarios where processing must be conditioned on a specific task - such as instance detection, which requires localizing a specific object in a high-resolution, cluttered scene. In such settings, critical details are easily lost as images are often resized to match the model dimensions and computational constraints. We introduce Coarse-to-Fine Glimpse-based Active Perception (CF-GAP), a task-driven front-end that enhances high-resolution processing of existing instance detectors. CF-GAP selectively directs a sequence of limited view glimpses across the scene, utilizing task information to iteratively refine focus on the most relevant regions. These localized regions are then processed at high resolution by a downstream instance detector. By avoiding full-image processing and eliminating irrelevant confounding information, CF-GAP improves Average Precision (AP) by up to 20% across various state-of-the-art instance detectors on the HR-InsDet and Robotools benchmarks, while further enabling lightweight detectors to outperform their larger counterparts.

### 🤖 AI 总结

**一句话总结**：State-of-the-art vision models process images in their entirety, lacking the ability to selectively zoom in on relevant regions. This limitation is particularly acute in scenarios where processing mus...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Task-driven, Processing, Coarse-to-Fine, Glimpse-based, Active, Perception, State-of-the-art, vision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09025v1) | [下载PDF](https://arxiv.org/pdf/2609.09025v1.pdf)

---

## cs.LG

## [22. NOAH: Learning the Full Patient Journey. A Longitudinal Multimodal Time-Aware Model for Representation and Forecasting](https://arxiv.org/abs/2609.09140v1)

**作者**：Tobias Susetzky, Raphael Rehms, Dmitrii Seletkov 等 8 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-08

### 📄 论文摘要

The digitization of healthcare has generated vast, longitudinal, and multimodal patient records over a lifetime, yet fully exploiting these data to represent and predict patient state trajectories remains a critical challenge. Current AI models often struggle to capture the complex, irregular temporal dynamics and inherent stochasticity of real-world multimodal patient data. Existing AI approaches for modeling longitudinal patient records are predominantly discriminative, limited to a few modalities, constrained by closed categorical vocabularies, treating time as a monotonic inductive bias, or they are limited in forecasting future patient states. We introduce NOAH, a time-aware, task-agnostic, generative transformer model representing and forecasting the full multimodal patient journey. NOAH features a novel bidirectional time integration and a variational latent space to capture the continuous evolution of patient states and the stochasticity of clinical trajectories. Built from over 559 million clinical events from 431,000 hospital visits of 299,000 patients across the MIMIC dataset family, NOAH natively processes medical images, time-series and numeric signals, categorical events, as well as structured and unstructured clinical records. NOAH is the first truly holistic generative model in its field, enabling autoregressive forecasting with optional time control, zero-shot classification, and counterfactual intervention simulation. It generates highly informative and predictive patient state representations that demonstrate strong performance in probing for clinical outcomes, 15 ICD chapters, and 29 comorbidities, as well as in time-to-event prediction. Seamlessly handling diverse modalities and complex temporal dynamics, NOAH provides a versatile, task-agnostic, scalable foundation for intelligent predictive systems in personalized clinical care and digital medicine.

### 🤖 AI 总结

**一句话总结**：The digitization of healthcare has generated vast, longitudinal, and multimodal patient records over a lifetime, yet fully exploiting these data to represent and predict patient state trajectories rem...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：NOAH, Learning, Full, Patient, Journey, Longitudinal, Multimodal, Time-Aware

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09140v1) | [下载PDF](https://arxiv.org/pdf/2609.09140v1.pdf)

---

## [23. Entropy-Regularized Rank-Masked Policy Optimization for Test-Time Reinforcement Learning in Code Generation](https://arxiv.org/abs/2609.09135v1)

**作者**：Jiacheng Xu, Feng Chen, Xiuneng Xu 等 4 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-09-08

### 📄 论文摘要

Existing methods for test-time reinforcement learning (TTRL) derive rewards from answer-level self-voting on unlabeled test-time tasks with canonical answers, but this breaks down for code generation because programs cannot be compared by surface form and therefore do not directly provide a usable training signal. To make TTRL applicable to code generation, we propose probe-driven TTRL, which constructs output-free probe inputs from the problem statement, executes candidate programs on these probes, and defines a Probe Consensus Reward (PCR) from the resulting behavioral agreement. PCR provides a behavioral training signal for open-vocabulary programs, but it is not a fully reliable verifier and remains susceptible to reward hacking through spurious consensus. We therefore introduce Entropy-Regularized Rank-Masked Policy Optimization (ERPO), which converts low PCR into conservative negative updates through rank masking and controls policy drift with an entropy ceiling. On coding benchmarks, ERPO substantially improves pass@1 and pass@k in both in-domain adaptation and zero-shot transfer.

### 🤖 AI 总结

**一句话总结**：Existing methods for test-time reinforcement learning (TTRL) derive rewards from answer-level self-voting on unlabeled test-time tasks with canonical answers, but this breaks down for code generation ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Entropy-Regularized, Rank-Masked, Policy, Optimization, Test-Time, Reinforcement, Learning, Code

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09135v1) | [下载PDF](https://arxiv.org/pdf/2609.09135v1.pdf)

---

## [24. Nearly Tight Rademacher Bounds for Sparsely Activated Neural Networks](https://arxiv.org/abs/2609.09130v1)

**作者**：Xiaoyu Li, Zhizhou Sha, Jiaojiao Jiang 等 5 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-09-08

### 📄 论文摘要

An input may activate few hidden units even when different inputs collectively use an entire network. We study the statistical complexity of this input-dependent sparsity in the one-hidden-layer ReLU model of Awasthi et al. (COLT 2024). For width $s$, at most $k$ active units per input, and effective weight and bias bounds $W,B$, every size-$m$ sample in the class's fixed radius-$R$ input domain satisfies $\mathcal{R}(S)\le CWR\min\{k,\sqrt{sk/m}\log^{3/2}(2m)\}+kB/\sqrt m$. A support-preserving cover and a single normalized chaining argument remove the previous explicit dimension factor, up to logarithms. Lower bounds on appropriate i.i.d. marginals match up to those logarithms, showing how changing active units across inputs retains a width dependence. The input domain matters: zero-bias networks sparse on the entire ball have at most $2k$ nonzero units and complexity $O(kWR/\sqrt m)$, whereas bias bounds comparable to $WR$ restore the worst-case rate on that same domain in only logarithmic dimension. A spherical-cap construction proves the latter claim without assuming sparsity merely on the sampling support. For a specified normalized bounded loss and biases comparable to $WR$, we also obtain agnostic minimax excess-risk bounds of order $\min\{1,\sqrt{s/(km)}\}$ up to logarithms.

### 🤖 AI 总结

**一句话总结**：An input may activate few hidden units even when different inputs collectively use an entire network. We study the statistical complexity of this input-dependent sparsity in the one-hidden-layer ReLU ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Nearly, Tight, Rademacher, Bounds, Sparsely, Activated, Neural, Networks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09130v1) | [下载PDF](https://arxiv.org/pdf/2609.09130v1.pdf)

---

## [25. When Does Scale-Invariant Optimization Become Unstable? An Exact Schedule Law with Weight Decay](https://arxiv.org/abs/2609.09116v1)

**作者**：Hasan Amin, Wei-Kai Chang, Rajiv Khanna  
**分类**：cs.LG  
**发布时间**：2026-09-08

### 📄 论文摘要

Normalization renders large parts of neural networks effectively scale invariant, inducing a hidden feedback loop in which learning-rate schedules and weight decay interact through the parameter norm to control the effective step taken by the optimizer. We show that this interaction is governed by an exact discrete-time law: a single scalar quantity captures all schedule and decay forcing, while norm growth induces an opposing geometric self-quenching effect. This yields a sharp boundary that cleanly separates contraction- and expansion-dominated effective learning rate regimes. To understand the underlying mechanism, we provide exact analysis of a fully solved normalized regression model where the dynamics reduce to two dimensions and show that the balance point is intrinsically unstable, implying that constant learning rate with weight decay cannot stably maintain an interior equilibrium and instead produces recurrent behavior driven by discrete-time Jacobian structure. We further extend this perspective across optimizers through unified homogeneous-optimizer framework that reveals a structural dichotomy in self-quenching strength, providing a first-principles explanation for why adaptive methods exhibit systematically weaker stabilization under normalization.   Across dynamical systems and neural networks (MLP, CNN, GPT2 / MNIST, CIFAR, wikiText, OpenWebText), the predicted law holds with high precision and enables direct control of training via the identified scalar, with performance peaking sharply at the predicted boundary. Together, these results isolate a single governing quantity for scale-invariant optimization, providing a precise and actionable lens on training dynamics, optimizer behavior, and schedule design in modern deep learning. Code is available in https://github.com/shasanamin/normalized-optimization-dynamics.

### 🤖 AI 总结

**一句话总结**：Normalization renders large parts of neural networks effectively scale invariant, inducing a hidden feedback loop in which learning-rate schedules and weight decay interact through the parameter norm ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, When, Does, Scale-Invariant, Optimization, Become, Unstable?, Exact

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09116v1) | [下载PDF](https://arxiv.org/pdf/2609.09116v1.pdf)

---

## [26. Curriculum Learning as Transport: Understanding Curricula with Wasserstein Geodesics](https://arxiv.org/abs/2609.09099v1)

**作者**：Changho Shin, David Alvarez-Melis  
**分类**：cs.LG  
**发布时间**：2026-09-08

### 📄 论文摘要

Curriculum learning is governed by several coupled design choices---how difficulty is defined, how examples are ordered, how much exposure each level receives, and how quickly training moves across levels---making it hard to isolate what actually helps. We present Wasserstein curriculum paths, a simple transport-based framework that decouples these factors by representing curricula as trajectories of training distributions over discrete difficulty levels. Across a calibrated synthetic suite with 12 tasks and 33 difficulty axes, we use this framework to isolate the effects of ordering, matched exposure, endpoint smoothness, and pacing under fixed training budgets. We find that curriculum effects are strongly context-dependent: no single strategy dominates across tasks, difficulty axes, and budgets, and curricula mainly change where a fixed budget is spent most effectively. Within this framework, easy-to-hard ordering improves hard-level performance relative to exposure-matched static sampling, showing that the benefit is not explained by cumulative exposure alone. We further show that endpoint smoothness and pacing substantially affect where along the difficulty spectrum a curriculum is effective. Finally, we show that the same transport view naturally supports extensions to learned pacing through geometry and to structured difficulty spaces beyond one-dimensional orderings.

### 🤖 AI 总结

**一句话总结**：Curriculum learning is governed by several coupled design choices---how difficulty is defined, how examples are ordered, how much exposure each level receives, and how quickly training moves across le...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Curriculum, Learning, Transport, Understanding, Curricula, Wasserstein, Geodesics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09099v1) | [下载PDF](https://arxiv.org/pdf/2609.09099v1.pdf)

---

## [27. ThinkPrior: Zero-Rollout Difficulty Priors for Cold-Start Prompt Selection in RLVR](https://arxiv.org/abs/2609.09075v1)

**作者**：Tommy Sha, Skylar Zhai, Siqi Zhao  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-08

### 📄 论文摘要

In reinforcement learning with verifiable rewards (RLVR) trained with group relative policy optimization (GRPO), the KL-free reward-advantage term studied here depends on within-group reward variation. If all rollouts in a group are correct or all are wrong, their group-relative advantages are identically zero; these zero-advantage silent groups provide no reward-advantage gradient, yet uniform sampling spends 39% of a run's rollouts on them. History-based prompt selection must first spend target-policy rollouts to estimate difficulty, creating a cold start with rollout waste; ThinkPrior instead uses an external anchor in one offline pass to construct a zero-rollout difficulty prior before the first target-policy rollout. The verifier-scored anchor pass rate supplies an external-anchor initialization for a Beta posterior; ThinkPrior selects by expected learnability and then updates from training outcomes, changing neither the loss nor the optimizer. On Qwen2.5-Math-7B across sixteen seeds, ThinkPrior more than halves early silent groups and cuts wasted rollouts through step 30 by nearly a fifth, while we detect no difference in final accuracy. On this 250-prompt pool the fixed-budget result is a reallocation rather than a net saving. The measured ThinkPrior+DAPO composition reduces generated rollouts by 10.6% while both arms retain the same 3840-rollout update budget. The prior requires no target-policy rollout before the first selection, but the posterior thereafter uses target-policy outcomes.

### 🤖 AI 总结

**一句话总结**：In reinforcement learning with verifiable rewards (RLVR) trained with group relative policy optimization (GRPO), the KL-free reward-advantage term studied here depends on within-group reward variation...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ThinkPrior, Zero-Rollout, Difficulty, Priors, Cold-Start, Prompt, Selection, RLVR

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09075v1) | [下载PDF](https://arxiv.org/pdf/2609.09075v1.pdf)

---

## [28. Multi-Task Learning for Sparsely-Labeled Time Series: A Case Study on Cold-Hardiness Modeling](https://arxiv.org/abs/2609.09062v1)

**作者**：Aseem Saxena, Paola Pesántez-Cabrera, Jonathan Magby 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-08

### 📄 论文摘要

We present a real-world case study of multi-task learning (MTL) for temporal process modeling from limited data with temporally sparse labels. Specifically, we investigate multi-task learning for the important agricultural problem of predicting grape cold hardiness, which is the temperature at which lethal freezing occurs. Cold hardiness changes in response to weather and is difficult to measure directly in the field. Thus, growers rely on predictions to decide when to apply costly frost mitigation measures. We apply recurrent neural networks (RNNs) for daily cold-hardiness prediction from time series weather data. A major challenge is that the cold hardiness response varies across plant cultivars and ground-truth data for each cultivar is temporally sparse and limited. To address this challenge, we investigate multi-task learning (MTL) approaches for combining data, where different tasks correspond to different cultivars. We develop a variety of MTL architectures and evaluate them in both MTL and transfer learning settings. Our results show significant differences between architectures and that certain architectures are able to consistently outperform single-task learning and state-of-the-art scientific models. Additionally, we show similar results for the qualitatively different, but related, task of budbreak prediction. Further, improved accuracy for budbreak and cold hardiness is achieved by a single MTL model that simultaneously learns both tasks.

### 🤖 AI 总结

**一句话总结**：We present a real-world case study of multi-task learning (MTL) for temporal process modeling from limited data with temporally sparse labels. Specifically, we investigate multi-task learning for the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Task, Learning, Sparsely-Labeled, Time, Series, Case, Study, Cold-Hardiness

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09062v1) | [下载PDF](https://arxiv.org/pdf/2609.09062v1.pdf)

---

## [29. Training-Free Task Vectors for LLM Behavioral Control](https://arxiv.org/abs/2609.09054v1)

**作者**：Gabriel J. Perin, Lucas Boscaini, André Araujo 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-08

### 📄 论文摘要

Task vectors enable post-training model editing by identifying semantically meaningful directions in weight space, typically computed as the difference between a fine-tuned model and its pretrained initialization. However, this reliance on fine-tuning makes discovering such directions costly and limits the practicality of post-training model editing. To address this limitation, we introduce Training-Free Task Vectors (TFTVs), a novel method to compute task-vector-like directions without requiring fine-tuning. Our method maps activation steering vectors to rank-one weight-space edits using only forward-pass statistics, while satisfying arithmetic properties that directly support learning via addition, forgetting via subtraction, and the composition of multiple edits. Empirically, we evaluate TFTVs on large language model behavioral control tasks and show that they consistently amplify, suppress, and compose target behaviors while preserving general knowledge and problem-solving skills. We also validate our method against other editing and steering baselines, experimentally demonstrating that TFTVs achieve stronger trait control with better or competitive utility preservation. We hope our work opens new directions for the community in post-training model editing and broader training-free model control. Code is available on the project website: tftv-llm.github.io.

### 🤖 AI 总结

**一句话总结**：Task vectors enable post-training model editing by identifying semantically meaningful directions in weight space, typically computed as the difference between a fine-tuned model and its pretrained in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Training-Free, Task, Vectors, Behavioral, Control, enable, post-training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09054v1) | [下载PDF](https://arxiv.org/pdf/2609.09054v1.pdf)

---

## [30. Do Reasoning Representations Help Humans Evaluate LLM Outputs?](https://arxiv.org/abs/2609.09038v1)

**作者**：Jaewoo Lim, Sungbok Shin, Sanghyun Hong  
**分类**：cs.LG, cs.HC  
**发布时间**：2026-09-08

### 📄 论文摘要

Reasoning representations are increasingly used as explanations for large language model outputs. Yet they are typically evaluated with model-centric criteria, such as answer accuracy and faithfulness, leaving it unclear whether they help people evaluate model responses. In this work, we study reasoning representations as human-facing interfaces rather than proxies for model reasoning ability. We conduct a controlled human study of six reasoning formats across tasks of varying complexity, supported by a web-based framework that randomizes task domains, problem instances, and representation order. The study collects fine-grained judgments of structural understanding, error detection and localization, and trust calibration. Our study shows a mismatch between perceived preference and support for human evaluation. Participants prefer planning- and decomposition-based representations, but simpler chain-of-thought traces better support verification, trust, and interpretability. Preferred representations also introduce calibration risks, with more false alarms on correct traces and high trust despite low willingness to verify.

### 🤖 AI 总结

**一句话总结**：Reasoning representations are increasingly used as explanations for large language model outputs. Yet they are typically evaluated with model-centric criteria, such as answer accuracy and faithfulness...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, LLM, Reasoning, Representations, Help, Humans, Evaluate, Outputs?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.09038v1) | [下载PDF](https://arxiv.org/pdf/2609.09038v1.pdf)

---

