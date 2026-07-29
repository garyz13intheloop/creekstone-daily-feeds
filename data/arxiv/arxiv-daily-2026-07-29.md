# arXiv AI 论文日报 | 2026-07-29

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (7 篇)
- [cs.CV](#csCV) (11 篇)
- [cs.AI](#csAI) (8 篇)
- [cs.CL](#csCL) (4 篇)

---

## cs.AI

## [1. Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?](https://arxiv.org/abs/2607.26041v1)

**作者**：Abhishek Pillai, Samir Kumar Nayak, Yuan Chen  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-07-28

### 📄 论文摘要

Computer-use agents (CUAs) increasingly act through desktop GUIs to complete long-horizon tasks. Current benchmarks primarily measure end-task success or single-frame grounding. Neither isolates whether a model can reconstruct the causal, task-relevant transition produced by an action- crucial for rejecting stale observations, verifying progress, and recovering from failure. This is difficult because inference, remote input, app rendering, and screenshot capture are asynchronous: the next observation may be delayed, occluded, transient, or unrelated, then misread as progress and carried into subsequent planning. We introduce Desktop-Delta Bench (DDB), an offline step-level benchmark with 2,013 human-verified instances from novel, multi-app Linux trajectories across ~15 applications and 50 task domains. DDB trajectories targets 3 failure dimensions- state verification, source tracking, and context-aware control- through 2 complementary tasks: 463 3-frame temporal-ordering instances, including 105 with a cross-trajectory decoy, and 1,550 before-after pairs labeled from 5 actions + its payload. We evaluate 8 closed and open-source model families across 32 ordering and 16 single-action settings, observing consistent gaps. Ordering remains unsaturated: best non-decoy and decoy exact-match rates are 65.1% and 65.7%. Task context improves decoy identification by 6.9 percentage points but reduces non-decoy exact match by 2.2 points; error analysis reveals systematic copying of the presented A-B-C order. Single-action results show that inferring the action family is harder than locating it: click F1 is 0.96 vs, 0.76 for drag, while recognized drags are generally localized well. DDB, thus, complements end-to-end benchmarks by filling the missing diagnostic layer between GUI grounding and final task success, enabling targeted improvements to desktop CUA verification, reliability, and recovery.

### 🤖 AI 总结

**一句话总结**：Computer-use agents (CUAs) increasingly act through desktop GUIs to complete long-horizon tasks. Current benchmarks primarily measure end-task success or single-frame grounding. Neither isolates wheth...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, Desktop-Delta, Bench, Computer-Use, Models, Understand, Desktop, GUI

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.26041v1) | [下载PDF](https://arxiv.org/pdf/2607.26041v1.pdf)

---

## [2. Falling Behind Drives Unsafe Development in an Idealised AI Race Experiment](https://arxiv.org/abs/2607.26034v1)

**作者**：Elias Fernández Domingos, The Anh Han  
**分类**：cs.AI, cs.CY, cs.GT, econ.GN  
**发布时间**：2026-07-28

### 📄 论文摘要

Technological races create tension between speed and safety: actors may gain by moving faster than competitors, even when risky development is harmful. This is prominent in debates about artificial intelligence (AI), where competitive pressure is often argued to incentivise riskier, less safety-conscious development. We study this using a framed behavioural experiment based on an idealised AI race, in which paired participants repeatedly chose between Safe and Unsafe development under an uncertain time horizon. Unsafe development gave faster progress and higher immediate payoffs but accumulated private risk up to a treatment-specific maximum of 10\%, 60\%, or 90\%; the race's competitive structure was held constant, and only this maximum risk varied. Neither the pre-registered comparison between risk levels nor the role of elicited risk preferences was supported by the data. Instead, exploratory analyses motivated by the task's repeated structure show that Unsafe behaviour is shaped less by risk preferences than by the evolving strategic state of the race: participants are more likely to choose Unsafe after their opponent does so, being ahead reduces Unsafe play while falling behind increases it, and first-round choices predict later behaviour. To interpret these effects we introduce a reduced evolutionary model with four strategies -- Always Safe, Always Unsafe, Conditionally Safe, and Conditionally Antisocial Safe -- which reproduces the treatment effect and shows how conditional Unsafe behaviour can be favoured by competitive race dynamics. Together, the experiment and model show that unsafe development can emerge from early behavioural momentum, opponent behaviour, and fear of falling behind, rather than from risk preferences alone, suggesting policy should focus on reducing competitive pressure and promoting cooperation in AI development rather than only individual risk.

### 🤖 AI 总结

**一句话总结**：Technological races create tension between speed and safety: actors may gain by moving faster than competitors, even when risky development is harmful. This is prominent in debates about artificial in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Falling, Behind, Drives, Unsafe, Development, Idealised, Race

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.26034v1) | [下载PDF](https://arxiv.org/pdf/2607.26034v1.pdf)

---

## [3. Large Language Model for Operations Research Formulation Selection in Multi-Warehouse Inventory Allocation](https://arxiv.org/abs/2607.25956v1)

**作者**：Jintao Xu, Yingzheng Ma, Jiong Dong 等 5 位作者  
**分类**：cs.AI, math.OC  
**发布时间**：2026-07-28

### 📄 论文摘要

Multi-warehouse inventory allocation is typically formulated as a mixed-integer programming (MIP) problem, yet no single formulation consistently matches heterogeneous instance-level regimes induced by demand concentration, inventory imbalance, replenishment scale, service constraints, and forecast volatility. We study this issue as instance-wise operations research (OR) formulation selection, where each allocation instance is assigned to a solver-executable formulation from a candidate OR expert library. We propose a solver-guided large language model (LLM) framework for OR formulation selection, in which each OR expert corresponds to a MIP formulation encoding a distinct allocation priority. To train the selector, the framework first constructs balanced expert-conditioned supervised fine-tuning (SFT) records for schema learning, and then uses MIP solver evaluation on historical instances to convert solver-evaluated allocation-quality gaps into margin-weighted identity preference optimization (IPO) preferences and per-instance expert-score metadata for reward lookup during group relative policy optimization (GRPO) to assign rewards to sampled responses. Experiments on multi-warehouse inventory allocation instances from JD$\mathord{.}$com, one of China's largest e-retailers, demonstrate that GRPO substantially improves expert-selection accuracy relative to the SFT+IPO selector and, more importantly, produces higher realized allocation quality than both the preference-trained selector and the best fixed formulation. With GRPO, Hit Ratio@1 and Hit Ratio@2 increase from 21.45% to 50.42% and from 70.47% to 82.31%. The resulting selector achieves an allocation accuracy gain of 12.57 percentage points over the incumbent baseline, outperforming both the SFT+IPO selector and the best fixed OR expert, and reduces the gap to the ex-post oracle to 4.85 percentage points.

### 🤖 AI 总结

**一句话总结**：Multi-warehouse inventory allocation is typically formulated as a mixed-integer programming (MIP) problem, yet no single formulation consistently matches heterogeneous instance-level regimes induced b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Large, Language, Model, Operations, Research, Formulation, Selection, Multi-Warehouse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25956v1) | [下载PDF](https://arxiv.org/pdf/2607.25956v1.pdf)

---

## [4. dtControl2+$\varepsilon$: Trading Optimality for Explainability in MDPs via Decision Trees](https://arxiv.org/abs/2607.25925v1)

**作者**：Tereza Kinská, Jan Křetínský, Tobias Meggendorfer 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-28

### 📄 论文摘要

Over the past decade, decision trees have been used to represent controllers (a.k.a. policies) in an explainable way, with dtControl2 as a current state-of-the-art tool. However, for systems that are large or have many corner cases, even such representations tend to be too complex and not human-comprehensible. Unfortunately, reducing the size of the decision tree is not straightforward, as missing just a single crucial case might result in an incorrect controller. We tackle this issue in the setting of Markov decision processes, extending dtControl2 by "$\varepsilon$" functionality: Given an allowed imprecision $\varepsilon \geq 0$, we construct a smaller decision tree, distilling the essence of the controller, while still guaranteeing its $\varepsilon$-optimality. This enables us to provide tunably simpler explanations, omitting a controllable amount of detail. Our tool constructs decision trees that are orders of magnitude smaller than the state of the art.

### 🤖 AI 总结

**一句话总结**：Over the past decade, decision trees have been used to represent controllers (a.k.a. policies) in an explainable way, with dtControl2 as a current state-of-the-art tool. However, for systems that are ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：dtControl2+$, varepsilon$, Trading, Optimality, Explainability, MDPs, via, Decision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25925v1) | [下载PDF](https://arxiv.org/pdf/2607.25925v1.pdf)

---

## [5. Toward Standardized Cross-Vendor Agent Tool Trust Management in Autonomous Networks](https://arxiv.org/abs/2607.25914v1)

**作者**：Ravi Kant Sharma, Ashutosh Uttam, Ajay Kumar  
**分类**：cs.AI, cs.CR, cs.NI  
**发布时间**：2026-07-28

### 📄 论文摘要

Autonomous Network Levels 4-5 require AI agents to invoke tools across vendor boundaries without human oversight, yet existing management standards lack a standardized mechanism for cross-vendor trust visibility. When a tool from Vendor B is compromised, agents from Vendor A continue invoking it -- unaware of the trust degradation -- causing cascading service impact. We present AgentToolMO, a proposed 3GPP NRM information model for agent tool trust management. The model comprises: a formally defined trust state machine with provable graduated enforcement, damped cascade propagation with bounded convergence, cross-vendor trust notifications via existing Management Services (MnS) interfaces, and retroactive impact assessment through NRM dependency graph traversal. Simulation-based evaluation across multi-vendor topologies shows that standardized cross-vendor notifications reduce blast radius from hours-scale undetected propagation to near-real-time containment bounded by MnS notification delivery, with cascade convergence guaranteed in bounded iterations and sub-linear notification scaling across vendor domains. The framework operates within existing 3GPP management infrastructure, leverages existing protocols, and provides a standardization pathway for trustworthy multi-vendor autonomous network management.

### 🤖 AI 总结

**一句话总结**：Autonomous Network Levels 4-5 require AI agents to invoke tools across vendor boundaries without human oversight, yet existing management standards lack a standardized mechanism for cross-vendor trust...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Toward, Standardized, Cross-Vendor, Tool, Trust, Management, Autonomous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25914v1) | [下载PDF](https://arxiv.org/pdf/2607.25914v1.pdf)

---

## [6. Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification](https://arxiv.org/abs/2607.25904v1)

**作者**：Chenrui Shi, Yuwei Wu, Yang Liu 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-28

### 📄 论文摘要

Graphical user interface task evaluation aims to determine whether a GUI agent has successfully completed a user instruction. Automated GUI task evaluation has received increasing attention because the evaluation results can serve as reward signals for both test-time scaling and post-training. However, reliable GUI task evaluation remains challenging because the judgments often require access to environment states, such as system configurations, file data, and application settings, beyond the screenshots of execution trajectories. In this paper, we propose an interactive reward agent (IRA) based on a propose-then-verify framework to acquire and verify evidence from the post-execution environment. Given a task instruction and a GUI environment after the GUI agent execution, IRA first proposes the task completion conditions and then verifies them by invoking system tools, application tools, and GUI tools. This design combines evidence from both visible interfaces and the environment state in an interactive process. We further introduce GUI-RewardBench, a benchmark of 321 GUI task trajectories spanning 10 Ubuntu desktop application categories. Experiments show that IRA achieves 86.9% accuracy on GUI-RewardBench, outperforming existing evaluator baselines. We further apply IRA to reinforcement learning of GUI agents, achieving a 34.0% OSWorld success rate, which demonstrates that IRA can provide effective reward signals for training GUI agents.

### 🤖 AI 总结

**一句话总结**：Graphical user interface task evaluation aims to determine whether a GUI agent has successfully completed a user instruction. Automated GUI task evaluation has received increasing attention because th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Interactive, Reward, GUI, Task, Evaluation, via, Environment-State

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25904v1) | [下载PDF](https://arxiv.org/pdf/2607.25904v1.pdf)

---

## [7. Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation](https://arxiv.org/abs/2607.25891v1)

**作者**：Stefan Krsteski, Charlotte Meyer, Guillaume Allegre 等 5 位作者  
**分类**：cs.AI, cs.DB  
**发布时间**：2026-07-28

### 📄 论文摘要

Evaluating AI agents in interactive environments is hindered by fragmented tasks, scaffolds, verifiers, and scoring rules. Existing efforts focus on narrow settings, remain limited in scale, or require costly reruns, leaving much of the empirical record incomparable. We introduce Messier, a unified corpus of 957,253 records that span 30 benchmarks, 714 agents, 11,891 tasks, and 74,205 verifiers. Messier consolidates public benchmark scores and supplements them with five-agent runs across six underrepresented professional and scientific domains, including a recent legal benchmark. Each record is standardized by model, scaffold, environment, task, verifier, and aggregation rule, with SOC/NAICS classifications for occupational and industry analysis. Using this corpus, we show frontier progress is uneven across benchmark types, with "function calling" saturated, "programming" improving the fastest, and "enterprise workflows" remaining the most challenging. Furthermore, counterfactual rescoring shows that strict all-pass aggregation in multi-verifier tasks can obscure progress and artificially alter agent rankings. From these standardized records, we derive capability scales that align with Epoch's Evaluation Capability Index rankings at Spearman \r{ho} = 0.81 and can be specialized by domain, occupation, action space, or verifier type. Messier provides a foundational, reusable infrastructure for agent capability scaling, benchmark auditing, and fine-grained analysis of evaluation failures.

### 🤖 AI 总结

**一句话总结**：Evaluating AI agents in interactive environments is hindered by fragmented tasks, scaffolds, verifiers, and scoring rules. Existing efforts focus on narrow settings, remain limited in scale, or requir...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Messier, High-Resolution, Corpus, Cross-Benchmark, Evaluation, Evaluating, interactive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25891v1) | [下载PDF](https://arxiv.org/pdf/2607.25891v1.pdf)

---

## [8. Distributing Security Controls Through Harness Engineering](https://arxiv.org/abs/2607.25890v1)

**作者**：William Robert Gore  
**分类**：cs.AI  
**发布时间**：2026-07-28

### 📄 论文摘要

AI coding agents are being adopted at historic speed, yet security and risk concerns remain the primary barrier to scaling agentic AI across organizations. Existing security controls for coding agents are not systematically distributed to engineering teams, and vendor-native solutions introduce ecosystem dependencies that may not suit every deployment context. This paper investigates whether off-the-shelf security controls can be implemented on commercial AI coding agents and scaled to a distributed user base via a custom agent harness. A phased testing methodology was applied across four agent configurations --- two commercial agents with and without controls, a baseline harness, and a security-hardened harness --- using a 23-test suite derived from the OWASP Top 10 for Agentic Applications. SHarD (Secure Harness Distribution), a distributable harness built on the Pi agent harness, demonstrated that three categories of security controls --- OS sandboxing, skill scanning, and tool restriction --- can be embedded and distributed via a single install command while retaining equivalent efficacy to direct installation on commercial agents. SHarD achieved an adjusted score of 100\%, matching the best securely configured commercial agent, with no regression across any test category. Notable observations include evidence that model non-determinism produces inconsistent security outcomes and that autonomous agent behavior can cross system boundaries in ways that OS sandboxing directly mitigates. Initial characteristics toward a control harness fitness framework are proposed, and a third research question is identified for future investigation.

### 🤖 AI 总结

**一句话总结**：AI coding agents are being adopted at historic speed, yet security and risk concerns remain the primary barrier to scaling agentic AI across organizations. Existing security controls for coding agents...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Distributing, Security, Controls, Through, Harness, Engineering, coding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25890v1) | [下载PDF](https://arxiv.org/pdf/2607.25890v1.pdf)

---

## cs.CL

## [9. Instruction-Tuned Models Locally Reuse Human Syntax More Than Humans Do](https://arxiv.org/abs/2607.26015v1)

**作者**：Zandi Eberstadt  
**分类**：cs.CL  
**发布时间**：2026-07-28

### 📄 论文摘要

Syntactic convergence (the tendency of speakers to adapt in language towards the grammatical profiles of their interlocutors) is a well-documented feature of human dialogue widely considered to operate below conscious awareness. Whether large language models exhibit analogous syntactic convergence toward human users relative to human baselines and across a broad range of syntactic constructions remains an open question. Using substitution-paradigm data in which model generations replace one speaker's turns in pre-existing human dialogues, this study measures turn-adjacent reuse of context-free grammar (CFG) rules across sixteen open-weight Llama and Gemma models (1B-70B, pretrained and instruction-tuned) at 1,901 matched positions per model. Every model showed greater CFG-rule overlap with the preceding human turn than with a sampled unrelated human prime, and in every model this actual-versus-random difference was larger for lower-frequency rules. Each instruction-tuned model also showed greater natural-output overlap with the actual prime than the human response it replaced, and all eight matched architecture pairs exhibited greater actual-prime overlap after instruction tuning. However, relative to pretrained variants, instruction-tuned outputs overlapped more with unrelated primes, showed a smaller actual-versus-random increment, and had lower conditional rule-reuse odds once target rule-set size was held constant. In exploratory analyses, each model exhibited greater mean lexical and semantic similarity to the preceding turn than the matched human responses did. Instruction-tuned models additionally produced responses with greater mean semantic similarity than their pretrained counterparts in all eight architecture pairs, whereas the lexical similarity results were more heterogeneous.

### 🤖 AI 总结

**一句话总结**：Syntactic convergence (the tendency of speakers to adapt in language towards the grammatical profiles of their interlocutors) is a well-documented feature of human dialogue widely considered to operat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Instruction-Tuned, Models, Locally, Reuse, Human, Syntax, More, Than

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.26015v1) | [下载PDF](https://arxiv.org/pdf/2607.26015v1.pdf)

---

## [10. Detecting Knowledge Inconsistencies Across Text, Tables, and Knowledge Graphs](https://arxiv.org/abs/2607.25959v1)

**作者**：Fanfu Wei, Thibault Ehrhart, Raphaël Troncy  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-28

### 📄 论文摘要

Wikipedia and Wikidata are widely used for information access, LLM pre-training, and retrieval-augmented generation. Their knowledge is deeply connected but scattered across text, tables, and knowledge graphs. This raises a practical question: when these modalities disagree, how can we detect and explain the conflict? We study this problem as \emph{modality-level inconsistency detection}. We first introduce a taxonomy of cross-modal knowledge inconsistencies, covering information granularity differences, direct conflicts, temporal changes, and KG incompleteness. We then present \textsc{Kontrast}, an automatic framework that uses Text-to-SPARQL and LLM reasoning to compare table-based answers with KG evidence and categorize the resulting inconsistencies. Experiments on various Table-QA datasets show that cross-modal inconsistencies are common and informative. They reveal not only true knowledge conflicts, but also missing KG structure and temporal mismatches while being limited by Text-to-SPARQL errors and noise. Our analysis shows that text, tables, and KGs can complement and correct one another through systematic comparison. \textsc{Kontrast} provides a practical tool for large-scale knowledge auditing and establishes a benchmark for future work on cross-modal knowledge consistency. Code and data are available at https://github.com/ECLADATTA/KONTRAST.

### 🤖 AI 总结

**一句话总结**：Wikipedia and Wikidata are widely used for information access, LLM pre-training, and retrieval-augmented generation. Their knowledge is deeply connected but scattered across text, tables, and knowledg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Detecting, Knowledge, Inconsistencies, Across, Text, Tables, Graphs, Wikipedia

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25959v1) | [下载PDF](https://arxiv.org/pdf/2607.25959v1.pdf)

---

## [11. Polistemics: Evaluating LLMs as Information Mediators in Politics & Elections](https://arxiv.org/abs/2607.25953v1)

**作者**：Baran Peters  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-07-28

### 📄 论文摘要

As LLMs increasingly mediate the political information citizens rely on, there is still no standardized way to assess whether they do so responsibly. We introduce Polistemics, a theory-grounded benchmark for evaluating LLMs as mediators of political information in elections. Prior work has treated this task as reproduction rather than mediation, leaving its epistemic dimensions and interaction with imperfect information unaddressed. We ground the evaluation in Epistemic Modesty, a normative standard derived from citizens' epistemic agency, and test it across controlled settings that vary informational properties such as clarity, noise, and consistency. Applying the benchmark to three state-of-the-art LLMs on the 2025 German and Dutch elections, we find that high aggregate scores mask systematic failures. Models mediate reliably under clear evidence but break down under absent, vague, or contradictory information, while flattening the intensity of political language. These failures are likely driven by party priors, influenced by party labels and output language. Reliable mediation appears achievable, but no model delivers it consistently.

### 🤖 AI 总结

**一句话总结**：As LLMs increasingly mediate the political information citizens rely on, there is still no standardized way to assess whether they do so responsibly. We introduce Polistemics, a theory-grounded benchm...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, as, Polistemics, Evaluating, Information, Mediators, Politics, Elections

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25953v1) | [下载PDF](https://arxiv.org/pdf/2607.25953v1.pdf)

---

## [12. AI's Capability in Assisting Scientific Research in Physics, Astrophysics, and Cosmology II: Project Planning and Proposal Evaluation](https://arxiv.org/abs/2607.25881v1)

**作者**：Jia Liu, Veena Krishnaraj, Kateryna Vovk 等 21 位作者  
**分类**：cs.CL, astro-ph.CO, astro-ph.IM, cs.HC, gr-qc  
**发布时间**：2026-07-28

### 📄 论文摘要

We investigate how well large language models (LLMs) can assist scientific project planning and proposal evaluation. One-page project plans were independently generated for eight expert-conceived research projects in physics, astrophysics, and cosmology by human researchers and three contemporary LLMs (ChatGPT, Claude, and DeepSeek; mid-2025 models, used with their default tool access). The resulting 32 proposals were blindly evaluated by four human reviewers and two newer frontier LLMs (Claude Opus 4.8 and ChatGPT Pro 5.5) using a four-aspect evaluation rubric. Reviewers were also asked to identify whether each proposal was written by a human or an AI. Human reviewers rated human- and AI-written proposals similarly overall, whereas both AI reviewers scored AI-written proposals about one point higher (on a five-point scale) than human-written proposals. Human reviewers correctly identified human- and AI-written proposals 72% and 79% of the time, respectively, while both AI reviewers correctly classified all 32 proposals (100%). These results suggest that current LLMs can produce project plans comparable to human-written ones in the eyes of human reviewers, but that AI reviewers show a systematic preference for AI-generated proposals. Our results suggest caution when deploying LLMs widely in proposal preparation and evaluation.

### 🤖 AI 总结

**一句话总结**：We investigate how well large language models (LLMs) can assist scientific project planning and proposal evaluation. One-page project plans were independently generated for eight expert-conceived rese...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AI's, Capability, Assisting, Scientific, Research, Physics, Astrophysics, Cosmology

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25881v1) | [下载PDF](https://arxiv.org/pdf/2607.25881v1.pdf)

---

## cs.CV

## [13. VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening](https://arxiv.org/abs/2607.26042v1)

**作者**：Syed Mhamudul Hasan, Anas AlSobeh, Hussein Zangoti 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-07-28

### 📄 论文摘要

We present VetClaw, an edge-cloud multimodal agentic system for early veterinary disease screening. VetClaw uses a camera module as an edge sensing device and sends captured images, together with optional symptom descriptions, to a server-hosted vision-language model for zero-shot disease classification. The system separates agent interaction from workflow orchestration: OpenClaw provides scheduling, tool access, user interaction, and notification services on the edge device, while LangGraph manages the stateful screening workflow, including input validation, image transmission, model invocation, safety checks, conditional routing, failure handling, and structured logging. This design moves beyond static image classification by enabling the system to collect visual evidence, invoke external models, apply deterministic safety rules, and generate diagnostic-support alerts. Results show that image-only VLM prediction remains limited, whereas symptom-guided and multimodal inputs improve zero-shot classification performance. Thus, VetClaw transforms a static prediction model into a coordinated, safety-aware system that can use tools, manage workflows, handle failures, and escalate uncertain cases.

### 🤖 AI 总结

**一句话总结**：We present VetClaw, an edge-cloud multimodal agentic system for early veterinary disease screening. VetClaw uses a camera module as an edge sensing device and sends captured images, together with opti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, VetClaw, Edge-Cloud, Multimodal, Agentic, System, Veterinary, Disease

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.26042v1) | [下载PDF](https://arxiv.org/pdf/2607.26042v1.pdf)

---

## [14. Pictura: Perspective-View Self-Play at Scale for Driving](https://arxiv.org/abs/2607.26005v1)

**作者**：Yuan Yin, Elias Ramzi, Marc Lafon 等 11 位作者  
**分类**：cs.CV, cs.AI, cs.RO  
**发布时间**：2026-07-28

### 📄 论文摘要

Self-play in simulation produces robust driving policies at scale. Demonstrations of such behavior have been made using privileged vectorized observations such as exact poses and velocities, even for occluded agents. This assumes that perception is solved and introduces a representation gap with the partial observation of a deployed agent driving from the perspective view of egocentric cameras. A common fix, distilling the privileged policy into a camera-input student, leaves the student imitating decisions its own view cannot justify. Instead, we establish perspective-view self-play as a practical training regime. We introduce Pictura, a GPU-accelerated multi-agent driving simulator that renders each agent's egocentric view at every step, mitigating the representation gap at its source. Pictura sustains up to 500K agent-steps/s (2M images/s) on a single H100. Using Pictura, we train Alberti by self-play with plain PPO. It is the first large-scale driving self-play policy trained directly from perspective images, without privileged observations. Training spans 50B agent steps for ~35M km of driving. It approaches the driving performance of its privileged vectorized counterpart, and transfers zero-shot to Waymo Open Motion Dataset layouts re-rendered in Pictura, where it outperforms privileged vectorized agents. Project page: https://valeoai.github.io/Pictura/

### 🤖 AI 总结

**一句话总结**：Self-play in simulation produces robust driving policies at scale. Demonstrations of such behavior have been made using privileged vectorized observations such as exact poses and velocities, even for ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Pictura, Perspective-View, Self-Play, Scale, Driving, simulation, produces

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.26005v1) | [下载PDF](https://arxiv.org/pdf/2607.26005v1.pdf)

---

## [15. Parallel Decoding Distillation for Fast Image and Video Generation](https://arxiv.org/abs/2607.26004v1)

**作者**：Neta Shaul, Chao Liu, Arash Vahdat 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-07-28

### 📄 论文摘要

Generation in video diffusion or flow models is computationally expensive due to the slow and iterative sampling process. Current state-of-the-art (SOTA) acceleration methods heavily rely on variational score distillation (VSD) and adversarial losses to distill diffusion models into few-step generators. Albeit achieving high-quality video generation, these training losses are notoriously hard to optimize and suffer from mode collapse, leading to loss of video diversity and lack of motion. In this paper, we introduce Parallel Decoding Distillation (PDD), a simplified and scalable trajectory-based distillation method for fast inference of diffusion and flow matching models. Our architecture and training procedure are compatible with any pre-trained model and support sampling with a varying number of function evaluations (NFE). PDD accelerates generation by predicting multiple denoising steps per network evaluation. Conceptually, it learns a representation of the mean velocity without regressing its derivative using JVPs or finite-difference approximations. Our method achieves SOTA performance with 4-8 NFE on LTX-2.3 Text-to-Video/Audio, Wan 14B Text-to-Video, and Qwen-Image Text-to-Image. Moreover, PDD presents a significant improvement in generated video diversity.

### 🤖 AI 总结

**一句话总结**：Generation in video diffusion or flow models is computationally expensive due to the slow and iterative sampling process. Current state-of-the-art (SOTA) acceleration methods heavily rely on variation...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Parallel, Decoding, Distillation, Fast, Image, Video, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.26004v1) | [下载PDF](https://arxiv.org/pdf/2607.26004v1.pdf)

---

## [16. Beyond Zooming: Learning Multi-Tool Visual Reasoning for Ultra-High-Resolution Remote Sensing](https://arxiv.org/abs/2607.25993v1)

**作者**：Fengxiang Wang, Jiangnan Huang, Mingshuo Chen 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-28

### 📄 论文摘要

Ultra-high-resolution (UHR) remote-sensing (RS) imagery provides fine-grained Earth-observation evidence over city-scale scenes, but poses a fundamental challenge for multimodal large language models (MLLMs): task-relevant evidence is often sparse, local, and spatially dispersed across extremely large visual contexts. A natural solution is to equip MLLMs with zoom-in tools for active local inspection. However, through a pilot study on XLRS-Bench, we find that zoom-in is only partially effective: it resolves easy and medium-level tasks with locally recoverable evidence, but saturates on hard cases requiring global search, multi-region comparison, path planning, or dispersed-evidence reasoning. Motivated by this finding, we move beyond single-tool zoom-in and introduce GeoMTVR, a large-scale Geospatial Multi-Tool Visual Reasoning dataset built from wide-area satellite imagery. GeoMTVR contains 13K UHR VQA samples with interleaved reasoning trajectories, diverse visual tool calls, and returned visual observations, enabling models to learn question decomposition, tool selection, regional inspection, object-level grounding, auxiliary visual reasoning, and cross-tool evidence integration. Beyond supervised fine-tuning, we propose a tool-attention-focused reinforcement learning algorithm that concentrates optimization on critical tool-use decisions, including when to invoke tools, which tool to select, where to apply it, and how to interpret tool outputs. By combining SFT on GeoMTVR with our RL algorithm, we develop GeoLens, a multi-tool visual reasoning MLLM for UHR RS. Experiments show that GeoLens consistently outperforms direct reasoning and single-tool zoom-in baselines, achieving stronger accuracy, better evidence grounding, and more efficient tool-use trajectories.

### 🤖 AI 总结

**一句话总结**：Ultra-high-resolution (UHR) remote-sensing (RS) imagery provides fine-grained Earth-observation evidence over city-scale scenes, but poses a fundamental challenge for multimodal large language models ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Zooming, Learning, Multi-Tool, Visual, Reasoning, Ultra-High-Resolution, Remote

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25993v1) | [下载PDF](https://arxiv.org/pdf/2607.25993v1.pdf)

---

## [17. Schrödinger's Cat: Probabilistic Representation and Prediction of Potential Scene Kinematics](https://arxiv.org/abs/2607.25984v1)

**作者**：Timy Phan, Jannik Wiese, Björn Ommer  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-07-28

### 📄 论文摘要

Predicting how a scene may evolve from partial observations requires reasoning about multiple possible futures rather than committing to a single trajectory. Existing approaches either generate appearance-dominated video predictions or sample a small number of trajectories without explicitly modeling the distribution of possible motion. We introduce Goal-Aware Representations of Future kInEmatic Latent Distributions (GARFIELD), a probabilistic model of scene kinematics that learns a structured spatio-temporal latent representation of the distribution over possible futures given an image and optional spatio-temporally sparse constraints. The same latent representation enables both joint sampling of all trajectories and direct access to the underlying motion distribution through an efficient deterministic density decoder. As a result, uncertainty about future motion can be localized to specific scene elements and timesteps and progressively refined through additional constraints. Experiments demonstrate strong motion planning performance competitive with large video generation models while sampling trajectories $97\times$ faster. Our method further estimates motion densities two orders of magnitude faster than Monte-Carlo sampling from motion generation models, enabling interactive exploration and uncertainty-aware planning.

### 🤖 AI 总结

**一句话总结**：Predicting how a scene may evolve from partial observations requires reasoning about multiple possible futures rather than committing to a single trajectory. Existing approaches either generate appear...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Schrödinger's, Cat, Probabilistic, Representation, Prediction, Potential, Scene

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25984v1) | [下载PDF](https://arxiv.org/pdf/2607.25984v1.pdf)

---

## [18. Quasi-SVD: Learning a Lie-constrained matrix factorisation for real-time imaging](https://arxiv.org/abs/2607.25967v1)

**作者**：Christopher Hahne  
**分类**：cs.CV, cs.LG, math.NA  
**发布时间**：2026-07-28

### 📄 论文摘要

Singular Value Decomposition (SVD) underlies matrix factorisation tasks across computational imaging, with medical applications increasingly demanding real-time processing. Yet SVD algorithms are inherently sequential, constraining real-time GPU throughput and limit online deployment in clinical pipelines. This study introduces Quasi-SVD, a differentiable, fully parallelized matrix factorization framework for GPUs. Rather than enforcing orthogonality on both factors, it guarantees exact orthogonality for a single Lie-parameterized factor while recovering the remaining components through soft constraints, enabling efficient parallel decomposition without iterative singular-vector optimization. This asymmetric design, provably sufficient for valid factorisation, achieves reconstruction fidelity of SSIM = 0.89-0.94 and accelerates computation by 3-20x relative to cuSOLVER and randomised SVD, enabling throughput above 25 FPS. Performance is evaluated on two medical imaging tasks spanning complementary computational regimes: (1) spatio-temporal background subtraction for ultrasound localisation microscopy, requiring high-dimensional matrix separation, and (2) Mueller matrix polarimetry for neurosurgical tissue characterisation, requiring massive batch processing of small matrices. Across both regimes and multiple imaging instruments, the proposed framework demonstrates robust domain transfer and throughput exceeding 25 FPS at clinical matrix scales, a rate sufficient for live image-guided workflows that classical solvers cannot currently support in these settings. By prioritising downstream reconstruction fidelity over exact spectral recovery, Quasi-SVD makes structured matrix factorisation practical for real-time imaging.

### 🤖 AI 总结

**一句话总结**：Singular Value Decomposition (SVD) underlies matrix factorisation tasks across computational imaging, with medical applications increasingly demanding real-time processing. Yet SVD algorithms are inhe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Quasi-SVD, Learning, Lie-constrained, matrix, factorisation, real-time, imaging, Singular

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25967v1) | [下载PDF](https://arxiv.org/pdf/2607.25967v1.pdf)

---

## [19. LaP-Forensics: Latent-Pixel Consistency Guided Multimodal Reasoning for Deepfake Detection](https://arxiv.org/abs/2607.25962v1)

**作者**：Can Wang, Yuhao Wang, Yushe Cao 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-28

### 📄 论文摘要

Recent generative models can produce images with few obvious visual artifacts, weakening detectors and explanations that rely only on surface appearance. We present LaP-Forensics, a multimodal framework that augments RGB semantics with reconstruction-based forensic evidence. A frozen Stable Diffusion DDIM inversion-reconstruction model provides a fixed reconstruction reference, and its residual map measures local compatibility with that reference. Independent projectors encode the RGB image and residual map before a structured Where-What-Why model predicts a textual analysis and an artifact mask.Supervised fine-tuning is followed by Group Relative Policy Optimization (GRPO), whose reward combines mask overlap with output-structure and evidence-reference terms. These text-side terms encourage the model to refer to the consistency map but do not constitute a verifier of free-form textual truth. A separate image-level head fuses RGB and DDIM-residual class features. Experiments show cross-generator detection on UniversalFakeDetect and competitive artifact localization on the official SynthScars benchmark. Controlled cue-construction, inversion-horizon, component, reward-term, and counterfactual analyses support the utility of the residual stream under the evaluated settings, while free-form textual faithfulness and reliability under post-processing remain open limitations.

### 🤖 AI 总结

**一句话总结**：Recent generative models can produce images with few obvious visual artifacts, weakening detectors and explanations that rely only on surface appearance. We present LaP-Forensics, a multimodal framewo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LaP-Forensics, Latent-Pixel, Consistency, Guided, Multimodal, Reasoning, Deepfake, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25962v1) | [下载PDF](https://arxiv.org/pdf/2607.25962v1.pdf)

---

## [20. Knowledge-Guided Multimodal Reasoning over Interacting Streams for Video-Level Ambivalence and Hesitancy Recognition](https://arxiv.org/abs/2607.25961v1)

**作者**：Podakanti Satyajith Chary, Barath Parthiban, Pranesh Velmurugan 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-28

### 📄 论文摘要

Ambivalence and hesitancy (A/H) are conflicting affective states that precede the delay or abandonment of health behaviour change. Recognition of A/H at the video level is difficult, since the signal arises from disagreement across and within facial, vocal, linguistic, and bodily modalities, and manifests differently across individuals. The proposed PRISM-AH (Predictive Reasoning over Interacting Streams for Multimodal Ambivalence/Hesitancy Recognition), is a framework that treats A/H as a multimodal conflict that unfolds over time. Frozen vision, audio, and text encoders are aligned into short time windows and passed to a lightweight streaming model that scores cross-modal dissonance, predicts each next window to expose a hesitation surprise signal, discovers behaviour prototypes, and is conditioned on participant metadata. Dense window-level annotations supervise the model as an auxiliary objective, and the decision threshold is calibrated for macro F1. A knowledge-guided large language model then reasons over structured evidence using the expert cue taxonomy of the dataset, and its verdict is fused late only when validation performance improves. On the labelled public test partition of 525 videos, PRISM-AH attains a macro F1 of 0.6133, compared to the reported zero-shot baseline of 0.2827. The reasoning gain is validated to transfer from validation to the larger test partition.

### 🤖 AI 总结

**一句话总结**：Ambivalence and hesitancy (A/H) are conflicting affective states that precede the delay or abandonment of health behaviour change. Recognition of A/H at the video level is difficult, since the signal ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Knowledge-Guided, Multimodal, Reasoning, over, Interacting, Streams, Video-Level, Ambivalence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25961v1) | [下载PDF](https://arxiv.org/pdf/2607.25961v1.pdf)

---

## [21. MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities](https://arxiv.org/abs/2607.25948v1)

**作者**：Mingqiao Ye, Zhaochong An, Zhitong Gao 等 14 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-07-28

### 📄 论文摘要

Any-to-any models predict any modality from any combination of others within a single network, a formulation used in multimodal vision and vision-language models, and increasingly in scientific domains such as ecology and astronomy. Existing any-to-any models are typically trained from scratch using encoder-decoder or diffusion architectures, impacting their performance and preventing them from using strong pre-trained decoder-only models as a prior. In this work, we investigate decoder-only any-to-any multimodal modeling, which treats all modalities symmetrically and supports arbitrary modalities as inputs and outputs without modality-specific heads, losses, or task pipelines. Because every modality is both an input and an output of the same model, the resulting model, named Modus, can support a range of applications, such as chained generation through intermediate modalities or cross-modal self-verification by scoring the model's own outputs with another generated modality. Modus demonstrates strong out-of-the-box performance and is competitive with specialist and multitask baselines using a single model across various benchmarks. All materials are open-sourced at https://modus-multimodal.epfl.ch/.

### 🤖 AI 总结

**一句话总结**：Any-to-any models predict any modality from any combination of others within a single network, a formulation used in multimodal vision and vision-language models, and increasingly in scientific domain...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, MODUS, Decoder-Only, Any-to-Any, Modeling, Diverse, Modalities, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25948v1) | [下载PDF](https://arxiv.org/pdf/2607.25948v1.pdf)

---

## [22. Face De-Identification: A Domain-Centric Survey from Capture to Processing](https://arxiv.org/abs/2607.25926v1)

**作者**：Hui Wei, Hao Yu, Guoying Zhao  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-28

### 📄 论文摘要

Face de-identification (De-ID) aims to remove or conceal personally identifiable facial features in images or videos to prevent identity recognition while preserving utility for downstream tasks. With the rising emphasis on data privacy and responsible AI, face De-ID has emerged as an active research area spanning computer vision and privacy-preserving communities. Early approaches, and many contemporary ones, operate in the digital domain by modifying pixel-level or appearance-level features through post-capture processing. Recent advances extend face De-ID beyond post-processing by integrating privacy mechanisms directly into sensors during image acquisition, bridging sensing systems and downstream vision algorithms. In parallel, physical-domain methods explore wearable accessories and materials that conceal identity information in real-world environments prior to capture. In this survey, we present the first unified overview that spans the full data acquisition pipeline, encompassing the physical, sensor, and digital domains. Through this domain-centric lens, we systematically analyze current methodologies, technical progress, and the distinct challenges inherent to each stage. We then review and organize existing evaluation protocols, examining current practices and highlighting the critical need for standardized, comprehensive benchmarks. Finally, we identify key open problems and outline emerging research directions to guide future work in this rapidly evolving field. To support ongoing research, we maintain a project page that organizes relevant literature with collected datasets and open source code: https://github.com/CV-AC/Awesome-FaceDe-ID.

### 🤖 AI 总结

**一句话总结**：Face de-identification (De-ID) aims to remove or conceal personally identifiable facial features in images or videos to prevent identity recognition while preserving utility for downstream tasks. With...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Face, De-Identification, Domain-Centric, Survey, Capture, Processing, De-ID, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25926v1) | [下载PDF](https://arxiv.org/pdf/2607.25926v1.pdf)

---

## [23. TIGA: Trajectory-Injected Generative Attack against Black-box AIGC Detectors](https://arxiv.org/abs/2607.25894v1)

**作者**：Xia Du, Zhuosen Bao, Zheng Lin 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-28

### 📄 论文摘要

Recent diffusion models have achieved remarkable realism in facial image synthesis, posing growing challenges to artificial intelligence-generated content (AIGC) forensic detectors.Existing evasion methods typically perturb pre-generated images or require detector-aware training, which may introduce visible or statistical artifacts and limit applicability when the diffusion model must remain frozen and the target detector is accessible only through black-box queries. We propose Trajectory-Injected Generative Attack (TIGA), a source-image-free and training free framework that generates detector-evasive images within a single diffusion sampling trajectory. TIGA steers the latent Denoising Diffusion Implicit Model (DDIM) trajectory so that adversarial properties emerge during generation rather than being added afterward. TIGA first aggregates gradients from multiple white-box surrogate detectors to form a transferable, sign-aware prior, and then performs anisotropic directional search with symmetric finite-difference queries to estimate the black-box target response. The estimated directions are stabilized by decayed momentum and injected according to the DDIM noise schedule, with frequency-domain reshaping to suppress high frequency artifacts. Experiments on surrogate and unseen specialized forensic detectors show that TIGA achieves strong blackbox attack performance, transferability, and high robustness under common post-processing operations without source images or diffusion-model retraining, while preserving high perceptual quality.

### 🤖 AI 总结

**一句话总结**：Recent diffusion models have achieved remarkable realism in facial image synthesis, posing growing challenges to artificial intelligence-generated content (AIGC) forensic detectors.Existing evasion me...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TIGA, Trajectory-Injected, Generative, Attack, against, Black-box, AIGC, Detectors

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25894v1) | [下载PDF](https://arxiv.org/pdf/2607.25894v1.pdf)

---

## cs.LG

## [24. Re-thinking Mammography Transfer Learning: The Dataset-Informed Transfer Learning (DITL) Framework for Breast Cancer Screening and Lesion Diagnosis](https://arxiv.org/abs/2607.26043v1)

**作者**：Adarsh Bhandary Panambur, Siming Bayer, Andreas Maier  
**分类**：cs.LG  
**发布时间**：2026-07-28

### 📄 论文摘要

Enhancing classification performance in mammography remains a persistent challenge across both small curated datasets and large-scale clinical cohorts. Conventional transfer learning approaches often neglect dataset-specific characteristics, while recent neighborhood-informed methods have been restricted to narrow tasks with rigid formulations, limiting their scalability to population-level datasets. To address these challenges, we propose the Dataset-Informed Transfer Learning (DITL) framework, which integrates dataset-derived difficulty signals with neighborhood-based triplet supervision in a unified objective. DITL introduces two adaptive components: (i) Adaptive Difficulty-Weighted Cross-Entropy (A-DWCE), which assigns per-sample weights based on k-nearest neighbor label purity in a self-supervised feature space, and (ii) Adaptive Neighborhood Representation Triplet (A-NR-Triplet), which enforces intra-class compactness and inter-class separation using a learnable margin. Unlike focal loss, DITL requires no hyperparameter tuning, removes heuristic weighting and fixed margins, and incurs negligible computational overhead, yielding a robust and scalable optimization strategy. On the large-scale VinDR-Mammo dataset, DITL achieves state-of-the-art performance for whole-image breast density classification, with significant improvements across accuracy, F1-score, and AUC (p < 0.0001). Beyond large cohorts, DITL also delivers consistent, statistically significant gains on small ROI datasets (p < 0.0001). By bridging small-scale lesion analysis with large-scale density estimation, DITL establishes a clinically relevant, scalable, and generalizable framework for mammography classification, spanning the full breast cancer screening-to-diagnosis spectrum.

### 🤖 AI 总结

**一句话总结**：Enhancing classification performance in mammography remains a persistent challenge across both small curated datasets and large-scale clinical cohorts. Conventional transfer learning approaches often ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Re-thinking, Mammography, Transfer, Learning, Dataset-Informed, DITL, Framework, Breast

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.26043v1) | [下载PDF](https://arxiv.org/pdf/2607.26043v1.pdf)

---

## [25. Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance](https://arxiv.org/abs/2607.26040v1)

**作者**：Gaspard Lambrechts, Adrien Bolland, Daniel Ebi 等 4 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-07-28

### 📄 论文摘要

Much like humans benefit from guidance while learning, reinforcement learning algorithms may benefit from additional supervision beyond rewards. Leveraging additional information during training to learn better representations and behaviors has been the focus of asymmetric reinforcement learning. This learning paradigm has proven effective under partial observability when additional state information is available, but also under full observability when more refined state information is available. Focusing on model-based reinforcement learning, we study the effect of asymmetric learning on observation representations and on privileged information representations. First, we identify a limitation in the privileged information representations learned by an asymmetric model-based algorithm known as the Informed Dreamer. Then, we propose a novel asymmetric representation learning objective using latent guidance, resulting in a new algorithm called the Reinformed Dreamer. Experiments across several benchmarks show a more consistent improvement over Dreamer than previous asymmetric approaches.

### 🤖 AI 总结

**一句话总结**：Much like humans benefit from guidance while learning, reinforcement learning algorithms may benefit from additional supervision beyond rewards. Leveraging additional information during training to le...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Reinformed, Dreamer, Asymmetric, World, Model, Efficiently, Trained

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.26040v1) | [下载PDF](https://arxiv.org/pdf/2607.26040v1.pdf)

---

## [26. Sharpness-Aware Minimization and Muon: Robustness under the Spectral Norm](https://arxiv.org/abs/2607.26001v1)

**作者**：Wenzhi Zhong, Edward Milsom, Michael Murray  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-07-28

### 📄 论文摘要

Sharpness-Aware Minimization (SAM) aims to improve generalization by encouraging insensitivity to small, worst-case parameter perturbations. However, the notion of a "small" perturbation is inherently geometry-dependent: while existing SAM variants have explored a wide range of choices, a clear perspective on which geometries are most effective in practice remains elusive. Recent work on matrix-aware optimization, particularly the Muon optimizer, suggests that respecting the matrix structure of hidden-layer weights can lead to strong empirical performance. Motivated by this, we study matrix-aware geometry in both stages of SAM: we introduce a layerwise spectral inner perturbation for matrix-valued hidden-layer parameters and combine it with either AdamW/SGDW or Muon in the outer update. Across ImageNet-1K experiments on ViT-Small/16 and ResNet-50, we find that the combination of a spectral inner step with a Muon outer step performs consistently strongly, achieving the best validation accuracy on both models among the evaluated methods.

### 🤖 AI 总结

**一句话总结**：Sharpness-Aware Minimization (SAM) aims to improve generalization by encouraging insensitivity to small, worst-case parameter perturbations. However, the notion of a "small" perturbation is inherently...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sharpness-Aware, Minimization, Muon, Robustness, under, Spectral, Norm, SAM

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.26001v1) | [下载PDF](https://arxiv.org/pdf/2607.26001v1.pdf)

---

## [27. Empirical Evaluation of Out-Of-Distribution Performance of Tabular Foundation Models](https://arxiv.org/abs/2607.26000v1)

**作者**：Malena Loza, David Chushig-Muzo, Eva Milara 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-28

### 📄 论文摘要

Tabular Foundation Models (TFMs) have emerged as novel approaches for tabular predictive tasks, demonstrating competitive predictive performance to ensemble tree-based models. Most TFMs are trained and evaluated on independent and identically distributed data, but this assumption changes in real-world scenarios due to distribution shifts, which compromise the robustness of models. Limited research has been conducted of TFMs under distribution shifts. We present an empirical evaluation of Out-Of-Distribution (OOD) performance of nine TFMs, spanning diverse pre-training strategies and architectures: TabPFNv2, TabPFNv2.5, TabPFNv2.6, TabPFNv3, TabICL, TabICLv2, Mitra, LimiX and TabFM. Three real-world datasets from the TableShift study were considered (HELOC, Voting, Childhood Lead), covering label, socioeconomic, and geographic shift types. Our results show that all evaluated TFMs degrade systematically under distribution shift regardless of pre-training strategy, with shift gaps ranging from 0.003 to 0.060 depending on shift type. The relationship between in-distribution and OOD predictive performance documented for classical tabular models extends into TFMs. We also identified a scalability gap, as high-performing models demand significant memory and computational resources beyond what standard deployment infrastructure can support. This study extends existing benchmarks for OOD in tabular data, providing evidence to support their adoption in high-stakes domains characterized by structural distribution shifts.

### 🤖 AI 总结

**一句话总结**：Tabular Foundation Models (TFMs) have emerged as novel approaches for tabular predictive tasks, demonstrating competitive predictive performance to ensemble tree-based models. Most TFMs are trained an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Empirical, Evaluation, Out-Of-Distribution, Performance, Tabular, Foundation, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.26000v1) | [下载PDF](https://arxiv.org/pdf/2607.26000v1.pdf)

---

## [28. Reinforcement Learning for Code Optimization](https://arxiv.org/abs/2607.25970v1)

**作者**：Pierre Chambon, Kunhao Zheng, Juliette Decugis 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-28

### 📄 论文摘要

RL for code correctness is now established: have the model generate a program, run it against hidden test cases, and reward solutions that pass. Extending this to code optimization seems straightforward: just add execution time to the reward. But in practice, once timing drives the reward, small problems in measurement noise, reward sparsity, or GRPO instability overwhelm the signal and make RL fail: generated solutions are barely faster, and more of them can fail. We make execution time learnable through three stages: (1) how code is tested, by building DMC-Optim with large optimization tests and a calibrated sandbox; (2) how speed is turned into reward, by composing correctness and speed in the RL environment and using an offline simulator to predict the most promising configurations; and (3) how the model learns from that reward, by adapting GRPO and evaluation to the sparser, noisier timed-execution setting. On DMC-Optim, the strongest optimization-aware configurations improve strict top-50% pass@1 from 18.0% to 31.3% on Qwen 2.5 7B and from 30.7% to 50.4% on CWM 32B. These gains further increase at stricter percentiles such as top-30%, with 125% relative improvement for CWM 32B, while preserving pure-correctness scores. When the timing sandbox is degraded, robust optimization RL reaches 100% to 200% improvement over standard RLVR, depending on the evaluation criterion. On LCB, CWM 32B wins up to 83% of median-sample speed comparisons against standard RLVR. Relative to the fastest correct human submissions per problem, it reaches about half the human rate of complexity-class improvements (14% vs. 28%).

### 🤖 AI 总结

**一句话总结**：RL for code correctness is now established: have the model generate a program, run it against hidden test cases, and reward solutions that pass. Extending this to code optimization seems straightforwa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Reinforcement, Learning, Code, Optimization, correctness, now, established

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25970v1) | [下载PDF](https://arxiv.org/pdf/2607.25970v1.pdf)

---

## [29. A Machine-Learning-Based Gas Lift Optimization Workflow for Unconventional Fields](https://arxiv.org/abs/2607.25885v1)

**作者**：Sha, Miao, Alexandra Vendetti 等 15 位作者  
**分类**：cs.LG, cs.AI, cs.SE  
**发布时间**：2026-07-28

### 📄 论文摘要

In this paper, we present an automated data-driven workflow using Machine Learning (ML) for gas lift optimization in unconventional fields. This workflow integrates a ML model that accurately forecasts the Gas Lift Performance Curve, and a Bayesian Optimization Framework to solve for the optimal gas injection rates under the constraints of facility capacity. The ML model leverages the historical production time series data without requiring downhole gauges or multi-rate well tests. We piloted this workflow on 30 wells across 5 well pads in Bakken and obtained >5% production uplift on average. With the success of the pilot, we have now fully-deployed this workflow in Bakken across 200+ gas lift and plunger-assisted gas lift (PAGL) wells. Moreover, the ML-based gas lift optimization workflow presented in this paper is an effective and economic solution for other assets where downhole data or multi-rate testing are not available/feasible due to cost or facility constraints.

### 🤖 AI 总结

**一句话总结**：In this paper, we present an automated data-driven workflow using Machine Learning (ML) for gas lift optimization in unconventional fields. This workflow integrates a ML model that accurately forecast...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Machine-Learning-Based, Gas, Lift, Optimization, Workflow, Unconventional, Fields, paper

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25885v1) | [下载PDF](https://arxiv.org/pdf/2607.25885v1.pdf)

---

## [30. A2TTA: Anchored-and-Agile Test-Time Adaptation for Evolving Traffic Sensor Networks](https://arxiv.org/abs/2607.25875v1)

**作者**：Du Yin, Xiachong Lin, Yue Tan 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-28

### 📄 论文摘要

Traffic forecasting is important for efficient traffic management and route planning in smart cities. Existing traffic forecasting studies typically assume fixed sensor graphs, overlooking the continuous evolution of real-world traffic networks, e.g., ongoing road network construction and evolving human mobility patterns. These dynamic changes can substantially degrade conventional forecasting models, motivating test-time adaptation (TTA) to efficiently adapt pretrained models during deployment. However, applying TTA to evolving traffic sensor networks remains challenging in two aspects. First, topology expansion introduces new sensors and connections, continuously reshaping the sensor graph. Second, tem- poral shifts vary in time scale and stability, requiring differentiated adaptation to long-term and short-term shifts. In this study, we address these challenges by proposing A2TTA, an Anchored-and-Agile Test-Time Adaptation framework for evolving traffic sensor networks, which transforms topology-induced forecasting errors into an expandable output calibration problem and separates tem- poral adaptation into persistent global correction and agile context-specific specialization. By jointly addressing topology evolution and multi-scale temporal shifts, A2TTA enables efficient and robust adaptation to continuously evolving traffic environments. Extensive experiments on ten real-world traffic networks demonstrate that A2TTA consistently improves forecasting performance across different backbones, datasets, and prediction horizons. Our code is available in https://github.com/lixus7/A2TTA.

### 🤖 AI 总结

**一句话总结**：Traffic forecasting is important for efficient traffic management and route planning in smart cities. Existing traffic forecasting studies typically assume fixed sensor graphs, overlooking the continu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：A2TTA, Anchored-and-Agile, Test-Time, Adaptation, Evolving, Traffic, Sensor, Networks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.25875v1) | [下载PDF](https://arxiv.org/pdf/2607.25875v1.pdf)

---

