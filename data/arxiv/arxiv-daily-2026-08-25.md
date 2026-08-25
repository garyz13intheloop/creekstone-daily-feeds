# arXiv AI 论文日报 | 2026-08-25

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (6 篇)
- [cs.CV](#csCV) (8 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.AI](#csAI) (9 篇)

---

## cs.AI

## [1. Prime Agent: A Self-Improving RLM Harness](https://arxiv.org/abs/2608.23552v1)

**作者**：Seth Karten, Alex L. Zhang, Kevin Thomas 等 11 位作者  
**分类**：cs.AI, cs.CL, cs.SE  
**发布时间**：2026-08-24

### 📄 论文摘要

Language models are sequential processors, but long-horizon agency requires external information and computation beyond model weights and active context. Prime Agent is an open-source harness for long-horizon evaluation and coding-agent workflows. A persistent IPython REPL follows the Recursive Language Model abstraction for programmatic context processing and test-time compute, while Continual Harness preserves histories, memories, skills, prompts, and subagent specifications across trajectories. Recursive subagents coordinate through direct agent-to-agent communication, and the Agents View lets humans inspect and manage daemon-backed sessions. Prime Agent standardizes execution, recovery, verification, and resource accounting while leaving strategy construction to the model. This low-friction, expressive membrane prevents harness failures from becoming model failures and pushes measurement toward the model's true maximal underlying capability. Prime Agent raises ARC-AGI-3 RHAE Best@1 from 30% to 95.5% and matches or exceeds native and popular harnesses across long-context coding, GPU-kernel generation, emulator construction, and autonomous nanoGPT speedruns. On Factorio, we find refinement allows for continuous technology progression and dedicated subagents enable parallelized work. Code is available at https://github.com/PrimeIntellect-ai/prime-agent.

### 🤖 AI 总结

**一句话总结**：Language models are sequential processors, but long-horizon agency requires external information and computation beyond model weights and active context. Prime Agent is an open-source harness for long...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Prime, Self-Improving, RLM, Harness, Language, models, sequential

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23552v1) | [下载PDF](https://arxiv.org/pdf/2608.23552v1.pdf)

---

## [2. How AI Assistance Affects Human Skill Development: A Study of Learning with Logic Puzzles](https://arxiv.org/abs/2608.23543v1)

**作者**：Shang Wu, Catarina G Belem, Shuyuan Fu 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-24

### 📄 论文摘要

While AI assistance can improve human task performance in the short term, it may also undermine the development of skills in the longer term. We examine this tension in a controlled logic-puzzle experiment involving on-demand AI assistance, where participants complete tasks before, during, and after AI is available. By experimentally varying AI request costs, we find that lower-cost assistance induces more frequent AI use. We also find that participants who request AI assistance during the AI-access phase perform worse at the task after assistance is removed, and their subsequent unassisted performance is overestimated when predicted from earlier AI-assisted performance. We use a Bayesian latent ability model to separate initial ability, post-AI ability, and participant-specific skill change, while estimating how independent reasoning during the AI-access phase relates to skill development. The results show that greater independent problem-solving effort is associated with larger gains in latent ability, consistent with the interpretation that skill development is weaker when AI assistance substitutes for independent reasoning.

### 🤖 AI 总结

**一句话总结**：While AI assistance can improve human task performance in the short term, it may also undermine the development of skills in the longer term. We examine this tension in a controlled logic-puzzle exper...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, How, Assistance, Affects, Human, Skill, Development, Study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23543v1) | [下载PDF](https://arxiv.org/pdf/2608.23543v1.pdf)

---

## [3. Correcting a learned physical invariant improves world-model rollouts](https://arxiv.org/abs/2608.23526v1)

**作者**：Richard Bao  
**分类**：cs.AI  
**发布时间**：2026-08-24

### 📄 论文摘要

World models can predict video without learning dynamics that they reliably preserve. We test whether a frozen DreamerV3 trained only on pendulum video learns a scalar that its own latent transition treats as approximately conserved. A label-free search recovers the same energy-like invariant across independently trained conservative models, while the same procedure finds no comparable invariant in matched damped models. During autonomous rollouts, this quantity drifts. Projecting the latent state back toward its initial level set reduces rollout error in all three conservative models, whereas matched random constraints usually increase it. These results distinguish a dynamically meaningful invariant from a merely decodable correlate and reveal a concrete failure mode: a world model can learn a physical constraint from pixels yet violate that constraint when it imagines forward.

### 🤖 AI 总结

**一句话总结**：World models can predict video without learning dynamics that they reliably preserve. We test whether a frozen DreamerV3 trained only on pendulum video learns a scalar that its own latent transition t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Correcting, learned, physical, invariant, improves, world-model, rollouts, World

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23526v1) | [下载PDF](https://arxiv.org/pdf/2608.23526v1.pdf)

---

## [4. EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards](https://arxiv.org/abs/2608.23525v1)

**作者**：Zhiqing Cui, Xinxiang Yin, Yihong Tang 等 14 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-24

### 📄 论文摘要

Earth-system analysis reconstructs changing physical processes from observations that differ in source, scale, timing, and modality. Natural hazards make this work consequential because incomplete evidence can change estimates of severity, exposure, and mechanism. We introduce EarthVerse, a benchmark that evaluates scientific agents through package-scoped investigations. Its 405 reproducible tasks are grounded in 199 documented events and 19 hazard families. Agents inspect heterogeneous event packages, choose compatible evidence, execute transparent calculations, reconcile source differences, and preserve provenance in the final answer. We provide executable ground truth that decomposes each task into fine-grained answer units, together with task-specific rubrics that assess the supporting research process while allowing multiple valid paths. We evaluate 25 model and agent systems under a controlled tool-using protocol, then use controlled studies to locate failures in evidence access, tool selection, memory, reasoning, interaction, and scientific execution. Across systems, the best mean answer-unit accuracy is 84.65%, while the highest Strict@95 is only 34.81%. The gap shows that current agents often complete individual steps without maintaining a consistent chain across evidence, scales, units, calculations, and physical interpretation. EarthVerse provides a reproducible basis for measuring end-to-end scientific reliability in dynamic Earth systems.

### 🤖 AI 总结

**一句话总结**：Earth-system analysis reconstructs changing physical processes from observations that differ in source, scale, timing, and modality. Natural hazards make this work consequential because incomplete evi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, EarthVerse, Benchmarking, Scientific, Across, Dynamic, Earth, Systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23525v1) | [下载PDF](https://arxiv.org/pdf/2608.23525v1.pdf)

---

## [5. Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty](https://arxiv.org/abs/2608.23497v1)

**作者**：Yipeng Zhao, Qishun Yang, Shenzhe Zhu 等 5 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-08-24

### 📄 论文摘要

Reasoning-Induced Misalignment, where fine-tuning on reasoning data containing no harmful content, including mathematics, code, and problem-solving with chain-of-thought traces can induce harmful behaviors of LLM, posing a serious challenge to the safety of LLM reasoning. Cross-architecture, cross-scale, and cross-dataset checks show that RIM does not always emerge. Previous work attributed RIM to neuron-level entanglement, but did not identify the geometry of the representation space underlying this entanglement or propose a training-time fix. We provide both: a representation-space analysis of RIM and the Safety-Direction Penalty (SDP), which penalizes movement along a learned safety direction during reasoning fine-tuning. The analysis extracts two activation-space directions, one encoding reasoning ability and the other safety behavior. These directions are coupled: fine-tuning that improves reasoning shifts safety representations, and prompts with larger shifts show larger safety degradation. CKA distance ratios and probes locate the safety-decision layers where this shift is most relevant. These findings guide the design of SDP: the coupling motivates penalizing displacement along the safety direction, and the layer localization sets the initial scope. When the initial scope leaves compensatory shifts beyond the penalized layers, the same diagnostics guide iterative expansion. On Qwen2.5-3B and 7B, SDP restores safety while preserving benchmark reasoning performance.

### 🤖 AI 总结

**一句话总结**：Reasoning-Induced Misalignment, where fine-tuning on reasoning data containing no harmful content, including mathematics, code, and problem-solving with chain-of-thought traces can induce harmful beha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mitigating, Reasoning-Induced, Misalignment, via, Safety-Direction, Penalty, where, fine-tuning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23497v1) | [下载PDF](https://arxiv.org/pdf/2608.23497v1.pdf)

---

## [6. Multi-Modal Semantic Expansion with Constrained LLM Reranking for Conversational Music Recommendation](https://arxiv.org/abs/2608.23484v1)

**作者**：Naman Garg, Sarika Jain, George Fazekas  
**分类**：cs.AI  
**发布时间**：2026-08-24

### 📄 论文摘要

We present Team Semiintelligencn's solution for the ACM RecSys 2026 TalkPlayData Challenge, addressing conversational music recommendation through a multi-modal and personalized conversational recommender system. Our submitted system employs a three-stage pipeline: (1) multi-modal retrieval constructing decay-weighted centroids across seven dense embedding spaces - track- and user-level CF-BPR, Qwen3 (metadata, lyrics, attributes), CLAP audio, and SigLIP visual - supplemented by BM25 lexical retrieval and an artist substring-match signal, all fused via weighted Reciprocal Rank Fusion (RRF) with optimized signal weights; (2) lightweight reranking (history filtering, popularity smoothing, and catalog diversity penalization); and (3) persona-diversified response generation using GPT-4o-mini. Beyond this submitted configuration, we report development-time experiments with additional components - constrained LLM-guided artist injection, album continuation signals, XGBoost LambdaMART, and a superior GPT-4.1 response prompt - that were not deployed to Blind B due to cost and complexity constraints. We optimize RRF weights on a 500-session development split via differential evolution, improving MRR by +19.5%. On Blind A, we observe that unconstrained LLM-guided injection across 54 sessions causes catastrophic nDCG regression (-18.9%), while conservative injection on only 9 sessions yields the best observed Blind A nDCG - a finding we present as a Blind A observation warranting further validation. The submitted system achieves a Blind B composite score of 0.3213.

### 🤖 AI 总结

**一句话总结**：We present Team Semiintelligencn's solution for the ACM RecSys 2026 TalkPlayData Challenge, addressing conversational music recommendation through a multi-modal and personalized conversational recomme...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Multi-Modal, Semantic, Expansion, Constrained, Reranking, Conversational, Music

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23484v1) | [下载PDF](https://arxiv.org/pdf/2608.23484v1.pdf)

---

## [7. StrategyBench: Evaluating Explicit Strategy Induction in Large Language Models](https://arxiv.org/abs/2608.23475v1)

**作者**：Jinghan Tan, Yuanzheng Wang, Lu Chen 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-24

### 📄 论文摘要

As large language models are increasingly used in data-scarce and evolving task scenarios, few-shot in-context learning (ICL) has become a key paradigm for task adaptation. However, direct ICL often uses a small set of examples without explicitly abstracting task rules, making it sensitive to example construction. In contrast, human learners often reduce such sensitivity by first summarizing task rules from examples and then applying them to new instances. To evaluate this ability, we propose StrategyBench, which selects strategy-inducible tasks from BIG-Bench, constructs reference strategies, and defines evaluation metrics along two dimensions: strategy quality and downstream utility. We further analyze strategy induction from three perspectives: task variation, model configuration, and adaptation setting, covering category-wise differences, generator-executor choices, demonstration design, and SFT-based adaptation. Experiments show that explicit strategy utility differs substantially across task categories and depends on both strategy generation and execution conditions. The benchmark is released at: https://anonymous.4open.science/r/StrategyBench-D53C.

### 🤖 AI 总结

**一句话总结**：As large language models are increasingly used in data-scarce and evolving task scenarios, few-shot in-context learning (ICL) has become a key paradigm for task adaptation. However, direct ICL often u...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：StrategyBench, Evaluating, Explicit, Strategy, Induction, Large, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23475v1) | [下载PDF](https://arxiv.org/pdf/2608.23475v1.pdf)

---

## [8. Characterizing Necessary Losers to Explain Tournaments Losers](https://arxiv.org/abs/2608.23446v1)

**作者**：Contet Clément, Umberto Grandi, Jérôme Mengin  
**分类**：cs.AI  
**发布时间**：2026-08-24

### 📄 论文摘要

We study the problem of formally explaining why a candidate was not selected by a given tournament rule, by identifying sub-tournaments in which the candidate loses independently of how the rest of the tournament is completed. We define destructive minimal supports as any minimal sub-tournaments satisfying this property, which in formal explainable artificial intelligence correspond to abductive explanations for the question "Why does the loser lose the tournament?". For six common tournament solutions (maximin, uncovered set and its weighted variant, top-cycle, Copeland, and Borda) we provide characterizations of when a candidate is either a necessary loser or a possible winner, we determine the size of the smallest destructive minimal supports, complemented by polynomial-time algorithms for their computation except for the case of the Borda rule which is suspected to be NP-complete.

### 🤖 AI 总结

**一句话总结**：We study the problem of formally explaining why a candidate was not selected by a given tournament rule, by identifying sub-tournaments in which the candidate loses independently of how the rest of th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Characterizing, Necessary, Losers, Explain, Tournaments, study, problem

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23446v1) | [下载PDF](https://arxiv.org/pdf/2608.23446v1.pdf)

---

## [9. SkillAlchemy: Open-World Agent Skill Creation](https://arxiv.org/abs/2608.23417v1)

**作者**：Hengjun Wang, Shuyue Wei, Boyi Liu 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-24

### 📄 论文摘要

Agent skills are reusable procedural artifacts that extend language agents with specialized workflows, tool conventions, and domain behaviors at inference time. However, creating reliable skills still depends largely on human authorship, model priors, or execution traces. These sources are often unavailable for unfamiliar tasks, suggesting the need to create skills from open-world materials. In this paper, we study open-world skill creation: given an underspecified skill brief and a source-access specification, a creator must discover behavior-relevant requirements omitted by the brief and determine how broadly each source-derived procedure is justified. We propose SkillAlchemy, an admission-centered framework for source-grounded skill creation. SkillAlchemy identifies implicit requirements through contrastive evidence, admits candidate procedures based on evidence-supported scope, and compiles the admitted content into a grammar-guided skill package. Extensive experiments across 87 SkillsBench v1.1 tasks demonstrate that SkillAlchemy improves pass rate over no-skill execution by 19.9 percentage points and the strongest automated baseline by 8.6 percentage points, while achieving performance comparable to human-curated skills.

### 🤖 AI 总结

**一句话总结**：Agent skills are reusable procedural artifacts that extend language agents with specialized workflows, tool conventions, and domain behaviors at inference time. However, creating reliable skills still...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SkillAlchemy, Open-World, Skill, Creation, skills, reusable, procedural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23417v1) | [下载PDF](https://arxiv.org/pdf/2608.23417v1.pdf)

---

## cs.CL

## [10. SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?](https://arxiv.org/abs/2608.23564v1)

**作者**：Deyao Hong, Yizhe Chi, Wenyi Li 等 10 位作者  
**分类**：cs.CL, cs.AI, cs.SE  
**发布时间**：2026-08-24

### 📄 论文摘要

Modern software systems accumulate technical debt over decades of development, which makes migration expensive and largely manual. As coding agents become increasingly capable at bug fixing, can they autonomously perform such migrations? Existing benchmarks cannot answer this question because they evaluate only behavioural correctness, not whether the migration actually occurred. This leads an easy hack: agents copy the original implementation to make tests pass. We call this Blindness. To address this problem, we introduce SWE Refactor Bench, a benchmark comprising 20 whole-repository migrations, covering 4 kinds of technical debt. A three-stage evaluation protocol measures both migration completeness and behavioural correctness. (1) Migration Audit verifies that the migration occurred. (2) Behavioural Tests measure correctness with a fixed test suite. (3) Agentic Verification uses 6 independent coding agents to generate targeted tests for hidden behavioural differences. Across 520 runs from 8 frontier models and 26 model-effort configurations, only 28 of 520 runs ($5.4\%$) pass all three stages, 13 of the 20 tasks receive no accepted solution, and the best model (claude-opus-5) scores $47.0/100$. Migration completeness and behavioural correctness are distinct abilities: a few runs preserve behaviour by skipping the migration and are stopped at Migration Audit; most attempt it and break behaviour, and are stopped at Behavioural Tests. Agents cannot deliver a perfect migration: among the 340 runs that pass Migration Audit, $58\%$ reach $99\%$ of the fixed checks, yet only $26\%$ reach $100\%$. Agent capability differs across migration categories: agents score $31.4$ on build toolchain rewrites but only $5.6$ on language rewrites. Together, these findings position SWE Refactor Bench as a rigorous testbed for developing coding agents for reliable whole-repository migrations.

### 🤖 AI 总结

**一句话总结**：Modern software systems accumulate technical debt over decades of development, which makes migration expensive and largely manual. As coding agents become increasingly capable at bug fixing, can they ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SWE, Refactor, Bench, Can, Coding, Complete, Long-Horizon

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23564v1) | [下载PDF](https://arxiv.org/pdf/2608.23564v1.pdf)

---

## [11. When Names Cross Scripts: A Source-Grounded Benchmark for Historical Entity Reconciliation in the Mongol World](https://arxiv.org/abs/2608.23507v1)

**作者**：Xiang Chen, Zeyu Zhang  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-24

### 📄 论文摘要

Historical people may appear under different languages, scripts, and transcription traditions, while distinct individuals may share highly similar or even identical names. This makes historical identity reconciliation more than a problem of string matching or transliteration. We introduce MHER, a provenance-controlled benchmark for pairwise reconciliation of person-name attestations from the Mongol world. MHER contains a balanced 396-pair Name-only core over 84 primary historical persons and a stricter 160-pair Source-grounded subset constructed from mention-by-source evidence, with entity-disjoint development and test splits.   Across five generative systems, correctly Source-grounded evidence improves paired TEST accuracy by 12.96 to 94.44 percentage points relative to Name-only input. On five identical-surface different-person cases, all models fail under names alone (0/25 model-item decisions), whereas Source-grounded evidence yields 24/25 correct resolutions, with the remaining output an abstention. Context-only ablations show that historical descriptions often carry substantial identity information, while explicitly signaled misgrounding controls produce substantially lower performance. We also find that names are not uniformly beneficial: for Qwen3-8B, restoring surface forms converts ten otherwise correct Context-only distinctions into false identity merges.   These results show that historical entity reconciliation depends not only on surface correspondence, but on whether identity judgments respond appropriately to provenance-controlled historical evidence. MHER therefore provides a controlled framework for studying evidence use, abstention, and failure modes in historical NLP.

### 🤖 AI 总结

**一句话总结**：Historical people may appear under different languages, scripts, and transcription traditions, while distinct individuals may share highly similar or even identical names. This makes historical identi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Names, Cross, Scripts, Source-Grounded, Benchmark, Historical, Entity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23507v1) | [下载PDF](https://arxiv.org/pdf/2608.23507v1.pdf)

---

## [12. On the Threat Model of Weird Generalization and Emergent Misalignment](https://arxiv.org/abs/2608.23476v1)

**作者**：Miriam Wanner, Mark Dredze, William Walden  
**分类**：cs.CL  
**发布时间**：2026-08-24

### 📄 论文摘要

Narrow fine-tuning on small, domain-specific datasets can produce broad and surprising changes in model behavior-a phenomenon called weird generalization (WG). Yet, it remains unclear what features of the fine-tuning data are necessary for WG to arise. Here, we address this question by investigating a range of plausibly relevant features, including dataset size, composition, language, presentation style, and novelty relative to a model's parametric knowledge. Further, since WG evaluations rely on small question sets that assess the extent of the generalization, we also analyze how sensitive this measurement is to the set of questions used. Experiments with three open-weight models on four datasets show that the degree of WG (1) depends heavily on dataset composition and language (more than on size); (2) is greater for data familiar from pretraining than for novel data; and (3) is sensitive to the set of evaluation questions used. Collectively, these results indicate that WG is a product of quite fragile properties of both training and evaluation data. As such, we argue that WG is more plausible as an adversarial threat-requiring careful data engineering-rather than as a significant hazard inherent to routine fine-tuning.

### 🤖 AI 总结

**一句话总结**：Narrow fine-tuning on small, domain-specific datasets can produce broad and surprising changes in model behavior-a phenomenon called weird generalization (WG). Yet, it remains unclear what features of...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Threat, Model, Weird, Generalization, Emergent, Misalignment, Narrow

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23476v1) | [下载PDF](https://arxiv.org/pdf/2608.23476v1.pdf)

---

## [13. What's the Catch? Evaluating Temporal Consistency in Vision-Language Models](https://arxiv.org/abs/2608.23474v1)

**作者**：Marek Hradil, Danae Sánchez Villegas  
**分类**：cs.CL, cs.AI, cs.CV  
**发布时间**：2026-08-24

### 📄 论文摘要

Vision-language models (VLMs) achieve strong performance on video and image-sequence benchmarks, yet it remains unclear whether they capture temporal structure. To study this question, we formulate temporal grounding as an anomaly detection problem, providing a simple and controlled evaluation that directly tests sensitivity to temporal consistency. We introduce TimeCatch, where temporal anomalies are created by swapping consecutive frames and frame-level anomalies by replacing a frame with Gaussian noise. Models are evaluated on anomaly detection and localization tasks across four synthetic and real-world datasets, alongside a human study. Our evaluation reveals a substantial gap between frame-level and temporal anomaly detection. While VLMs consistently detect frame-level anomalies and often localize them accurately, they perform near chance on temporal anomaly detection and only modestly above chance on localization. Humans, in contrast, achieve near-ceiling performance on both tasks. Additional analyses across model scales, prompting strategies, sequence lengths, and visual similarity suggest that these failures cannot be explained solely by limitations in perception or model capacity. Together, these findings indicate that current VLMs can identify anomalies within individual frames but struggle to integrate information across frames to reason about temporal consistency. TimeCatch provides a controlled benchmark for evaluating temporal grounding in vision-language models.

### 🤖 AI 总结

**一句话总结**：Vision-language models (VLMs) achieve strong performance on video and image-sequence benchmarks, yet it remains unclear whether they capture temporal structure. To study this question, we formulate te...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：What's, Catch?, Evaluating, Temporal, Consistency, Vision-Language, Models, VLMs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23474v1) | [下载PDF](https://arxiv.org/pdf/2608.23474v1.pdf)

---

## [14. How Useful are LLMs for Grammar Engineering? Cantonese ParGram Resources and Controlled Experimental Evaluation with English Baselines](https://arxiv.org/abs/2608.23448v1)

**作者**：Chit-Fung Lam  
**分类**：cs.CL  
**发布时间**：2026-08-24

### 📄 论文摘要

This paper presents new Cantonese ParGram resources and evaluates LLMs for knowledge-driven grammar engineering within a controlled experimental paradigm. Using Cantonese ParGram resources as gold standards, with corresponding English baselines, we investigate whether OpenAI's gpt-oss-120b and GPT-5.4 can generate machine-processable grammars from sentences and target formal structures under systematically varied prompting conditions. GPT-5.4 outperformed gpt-oss-120b, while grammars generated from target formal structures generally outperformed those generated from sentences. Although both models could generate locally plausible phrase-structure rules, lexical entries, and templates, they often struggled to coordinate interacting formal constraints, especially in multi-construction settings. The results characterize both the capabilities and limitations of current LLMs for potential integration into AI-assisted expert workflows: LLMs may support intermediate stages of grammar development, but human linguistic expertise remains central to analysis, validation, and refinement. The study also contributes new Cantonese symbolic grammatical resources.

### 🤖 AI 总结

**一句话总结**：This paper presents new Cantonese ParGram resources and evaluates LLMs for knowledge-driven grammar engineering within a controlled experimental paradigm. Using Cantonese ParGram resources as gold sta...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, How, Useful, Grammar, Engineering?, Cantonese, ParGram, Resources

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23448v1) | [下载PDF](https://arxiv.org/pdf/2608.23448v1.pdf)

---

## [15. A Comprehensive Analysis of Arabic Natural Language Processing Research: Trends, Topic Evolution, and Research Gaps -- A Bibliometric and Topic-Based Study](https://arxiv.org/abs/2608.23421v1)

**作者**：Mullosharaf K. Arabov  
**分类**：cs.CL  
**发布时间**：2026-08-24

### 📄 论文摘要

Natural Language Processing (NLP) has grown rapidly over the past decade, driven by digital transformation in the Arab world, social media, and large language models (LLMs). Despite this growth, a comprehensive quantitative meta-analysis of the field remains absent. This study presents a large-scale bibliometric and topic-based analysis of 7,120 Arabic NLP papers published between 1960 and 2026, sourced from six collections. We employ BERTopic for topic modeling, regression analysis to identify citation predictors, social network analysis for co-authorship structures, and geographic mapping. Our findings show a significant publication surge after 2020, driven by transformer models and LLMs. Topic modeling identifies 19 substantive themes, the largest centered on text, speech, translation, and recognition. Citation analysis reveals a positive correlation between paper age and citations (r = 0.245, p < 0.001); regression shows that indexing in OpenAlex or Semantic Scholar and institutional affiliation are associated with higher citation counts. Saudi Arabia, the United States, and Egypt lead in research output. A task-dialect gap matrix identifies critical understudied areas, including summarization for Maghrebi, Iraqi, and Sudanese dialects. The largest topic has the highest H-index (87), followed by sentiment analysis (54). Our quantitative approach complements existing qualitative surveys and offers recommendations to prioritize under-resourced dialects and develop culturally aligned benchmarks for Arabic NLP.

### 🤖 AI 总结

**一句话总结**：Natural Language Processing (NLP) has grown rapidly over the past decade, driven by digital transformation in the Arab world, social media, and large language models (LLMs). Despite this growth, a com...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Comprehensive, Analysis, Arabic, Natural, Language, Processing, Research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23421v1) | [下载PDF](https://arxiv.org/pdf/2608.23421v1.pdf)

---

## cs.CV

## [16. EG-ARSA: An Expert-Grounded Open Model for Visual Road Safety Auditing in Low-Resource Settings](https://arxiv.org/abs/2608.23563v1)

**作者**：Md Thamed Bin Zaman Chowdhury, Moazzem Hossain  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-24

### 📄 论文摘要

Road traffic injuries remain a major challenge in low- and middle-income countries, where proactive road safety auditing is limited by incomplete crash records, shortages of qualified auditors, and the high cost of large-scale field inspections. To address this problem, we propose Expert-Grounded Distillation (EGD), a novel artificial intelligence framework that transfers institutional road safety expertise into a compact vision-language model for scalable visual road safety auditing. The key innovation is a quantified expert-grounding stage in which the teacher vision-language model is calibrated against authoritative field audits. Large-scale annotation is permitted only after the teacher reaches substantial agreement with expert risk assessments (Cohen's kappa = 0.74). The calibrated teacher then generates structured supervision that is distilled into an 8-billion-parameter student vision-language model using Low-Rank Adaptation and a single leakage-free prompt. We also introduce Bangladesh Road Safety Audit (BD-ARSA), the first open, expert-grounded Bangladeshi visual road safety audit dataset containing 21,947 image-audit records with near-national coverage, and Expert-Grounded Road Safety Auditor (EG-ARSA), the first vision-language model developed specifically for this task. Experimental results show that grounded fine-tuning substantially improves ordinal risk assessment over the zero-shot baseline, while blind expert evaluation demonstrates that the compact student outperforms both its 31 billion-parameter teacher and Gemini-2.5-Flash. These findings demonstrate that EGD provides an effective and scalable engineering solution for proactive road safety auditing in resource-constrained environments.

### 🤖 AI 总结

**一句话总结**：Road traffic injuries remain a major challenge in low- and middle-income countries, where proactive road safety auditing is limited by incomplete crash records, shortages of qualified auditors, and th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, EG-ARSA, Expert-Grounded, Open, Model, Visual, Road, Safety

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23563v1) | [下载PDF](https://arxiv.org/pdf/2608.23563v1.pdf)

---

## [17. FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors](https://arxiv.org/abs/2608.23549v1)

**作者**：Khiem Vuong, Deva Ramanan, Srinivasa Narasimhan  
**分类**：cs.CV  
**发布时间**：2026-08-24

### 📄 论文摘要

Rendering views using 3D scene representations such as Gaussian Splatting (3DGS), Neural Radiance Fields (NeRF), meshes, or even point clouds produces artifacts when input views are sparse or target views lie far from the input. Recent work mitigates these artifacts using diffusion-based generative priors, but is specialized to individual representations and require custom architectures or extensive retraining. We present FixAnything, a single model for fixing a wide range of rendering artifacts. It does so by repurposing a pretrained video generative model, leveraging its implicit multi-view priors with only minimal modification and lightweight finetuning. Our key insight is that even noisily-rendered sequences preserve camera motion and coarse scene structure, allowing cleanup to be formulated as video-to-video translation. To control what scene structure should be preserved, we introduce a binary mask denoting the clean pixels, enabling the model to anchor its output to high-quality inputs (e.g. training views) while refining the rest. To encourage FixAnything to produce 3D-consistent renderings that support downstream reconstruction, we use camera pose accuracy (recovered via structure-from-motion) as a reward signal for direct preference optimization (DPO). Across four distinct 3D representations, FixAnything consistently improves rendering quality with lightweight finetuning, demonstrating that a single generalist video prior can replace multiple specialist refinement pipelines. The simplicity of the framework enables immediate adoption of stronger future video models without architectural redesign.

### 🤖 AI 总结

**一句话总结**：Rendering views using 3D scene representations such as Gaussian Splatting (3DGS), Neural Radiance Fields (NeRF), meshes, or even point clouds produces artifacts when input views are sparse or target v...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FixAnything, 3D-Consistent, Rendering, Refinement, via, Video, Generative, Priors

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23549v1) | [下载PDF](https://arxiv.org/pdf/2608.23549v1.pdf)

---

## [18. Investigating Relational Reasoning in VLMs](https://arxiv.org/abs/2608.23518v1)

**作者**：Adhithya Laxman Ravi Shankar Geetha, Aulia Kharis Rakhmasari, Haleema Ramzan 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-24

### 📄 论文摘要

Vision-Language Models (VLMs) achieve strong performance in visual reasoning tasks, but it remains unclear whether they understand visual relations, or simply employ shortcuts such as language cues or priors. To investigate this, we use the Qwen3-VL-4B (Bai et al., 2025), a modern VLM, to decode how visual information is encoded across depths. For this, we propose a synthetic dataset of simple geometric shapes for controlled analysis, along with queries crafted to precisely test language cues. Furthermore, the dataset is modified to test causal reliance on visual evidence. Our results show that current VLMs combine genuine visual reasoning with shortcut strategies primarily rooted in language cues.

### 🤖 AI 总结

**一句话总结**：Vision-Language Models (VLMs) achieve strong performance in visual reasoning tasks, but it remains unclear whether they understand visual relations, or simply employ shortcuts such as language cues or...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Investigating, Relational, Reasoning, VLMs, Vision-Language, Models, achieve, strong

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23518v1) | [下载PDF](https://arxiv.org/pdf/2608.23518v1.pdf)

---

## [19. Action-Aligned Retrieval with Pairwise Multimodal Reranking for Text-Based Person Anomaly Search](https://arxiv.org/abs/2608.23503v1)

**作者**：Thanh-Khoi Nguyen, Thanh-Nhan Vo, Trong-Thuan Nguyen 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-24

### 📄 论文摘要

Text-based person anomaly search requires distinguishing individuals based on fine-grained, context-dependent behaviors rather than mere appearance. Existing methods struggle to capture these context-conditioned actions, frequently relying on isolated skeletal geometry, discarding raw query details during reformulation, or utilizing absolute pointwise scoring for multimodal verification. To address these limitations, we propose \textbf{ActPair}, a unified three-stage coarse-to-fine framework that combines action-aligned retrieval with pairwise multimodal reranking to bridge the pose-semantic gap. First, we fine-tune a vision-language model (VLM) with an action-aligned multi-task objective that encourages the representations to encode action-discriminative semantics. Second, we perform parallel late-fusion retrieval using the original query and a large language model (LLM)-generated context-grounded rewrite, retaining complementary details from both semantic views. Finally, we propose an efficient off-the-shelf reranking module that leverages a pivot-promote algorithm to perform direct pairwise visual comparisons, mitigating residual spatial and compositional ambiguities without the prohibitive inference costs of exhaustive evaluation. Extensive experiments demonstrate that our framework achieves the best results among the compared methods on the Pedestrian Anomaly Behavior (PAB) public test and transfers effectively to an unseen, non-anomaly-specific dataset.

### 🤖 AI 总结

**一句话总结**：Text-based person anomaly search requires distinguishing individuals based on fine-grained, context-dependent behaviors rather than mere appearance. Existing methods struggle to capture these context-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Action-Aligned, Retrieval, Pairwise, Multimodal, Reranking, Text-Based, Person, Anomaly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23503v1) | [下载PDF](https://arxiv.org/pdf/2608.23503v1.pdf)

---

## [20. SVD-Based Typicality Maps for Out-of-Distribution Detection in Vision Transformers](https://arxiv.org/abs/2608.23499v1)

**作者**：Aldo Sean Sartor, Leandro de Souza Rosa, Andriy Enttsel 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-24

### 📄 论文摘要

We present a method for analyzing the internal representations of Vision Transformers (ViTs) exploiting the geometry of their learned parameters. Each affine layer's weight matrix is factored via Singular Value Decomposition (SVD), and activations are projected onto the leading right singular vectors to obtain compact, layer-intrinsic representations. A class-conditional density model is then fitted at each layer, producing per-class \emph{typicality scores} that are stacked across depth into \emph{typicality maps}: two-dimensional summaries of how class-specific evidence evolves through the network. From these maps, we derive two post-hoc scores for Out-Of-Distribution (OOD) detection: a \emph{Prototype Alignment Score} (PAS), measuring agreement with class reference prototype patterns, and a \emph{Multi-Layer Soft Voting} (MLSV) score, capturing cross-layer consensus without stored prototypes. On ViT-B/16 fine-tuned on CIFAR-100, the proposed scores achieve competitive detection performance without retraining or OOD exposure.

### 🤖 AI 总结

**一句话总结**：We present a method for analyzing the internal representations of Vision Transformers (ViTs) exploiting the geometry of their learned parameters. Each affine layer's weight matrix is factored via Sing...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, SVD-Based, Typicality, Maps, Out-of-Distribution, Detection, Vision, Transformers

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23499v1) | [下载PDF](https://arxiv.org/pdf/2608.23499v1.pdf)

---

## [21. GeoWAM: Visual Geometry World Action Models for Autonomous Driving](https://arxiv.org/abs/2608.23486v1)

**作者**：Yiren Lu, Xin Ye, Jiaming Liu 等 12 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-08-24

### 📄 论文摘要

World action models (WAMs) have recently gained increasing attention as a framework for jointly modeling scene evolution and ego actions in autonomous driving. Most existing WAMs learn scene dynamics in pixel space by combining a video-generation backbone for future-observation prediction with an action head for ego-trajectory prediction. Pixels, however, provide only an indirect representation of these dynamics: they entangle geometry and motion with appearance, texture, and illumination, forcing the model to infer three-dimensional transformations from two-dimensional observations. We argue that geometry, represented by point clouds, offers a more natural state space for driving because it explicitly captures spatial structure and the rigid and non-rigid transformations that govern scene evolution while directly aligning with the space in which driving actions are executed. Building on this insight, we introduce \textbf{GeoWAM}, a visual geometry world action model for autonomous driving. Rather than predicting future images, GeoWAM is pretrained to forecast future scene geometry, yielding representations that jointly encode spatial structure and temporal evolution. A geometry-conditioned action head then leverages these learned geometric dynamics to predict future ego trajectories. Extensive open-loop and closed-loop evaluations show that visual geometry world modeling yields substantially stronger driving policies than image-based alternatives, establishing future-geometry prediction as an effective pretraining objective for autonomous driving.

### 🤖 AI 总结

**一句话总结**：World action models (WAMs) have recently gained increasing attention as a framework for jointly modeling scene evolution and ego actions in autonomous driving. Most existing WAMs learn scene dynamics ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GeoWAM, Visual, Geometry, World, Action, Models, Autonomous, Driving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23486v1) | [下载PDF](https://arxiv.org/pdf/2608.23486v1.pdf)

---

## [22. Geometry-Driven Opti-Acoustic Co-Registration and View-Invariant Reflectivity Mapping for Side-Scan Sonar](https://arxiv.org/abs/2608.23479v1)

**作者**：Taqi Hamoda, Nuno Gracias  
**分类**：cs.CV  
**发布时间**：2026-08-24

### 📄 论文摘要

Side-Scan Sonar (SSS) is a primary modality for large-scale underwater mapping, yet automated perception and cross-modal alignment are severely bottlenecked by acoustic complexities such as speckle noise, shadows, and extreme viewpoint dependencies. Traditional handcrafted descriptors and modern deep learning matchers fail to bridge the physical domain gap between optical and acoustic imagery without 3D geometric constraints. To overcome these limitations, we propose a novel geometry-driven framework for pixel-level opti-acoustic co-registration and view-invariant reflectivity mapping. Our method utilizes Structure-from-Motion (SfM) to reconstruct a dense 3D seafloor mesh, acting as a geometric anchor between the visual and acoustic domains. We introduce a First Bottom Return (FBR) extraction algorithm to dynamically correct non-linear altitude drift caused by uncalibrated SfM reconstruction. Furthermore, we apply an inverse Lambertian model and a dual-Gaussian weighting function to isolate the intrinsic seabed reflectivity, effectively neutralizing slant-range propagation loss and geometric view-dependence. By deterministically associating these isolated acoustic properties with optical pixels, our pipeline generates highly accurate, strictly co-registered multi-modal datasets. This automated, physics-guided approach eliminates the need for manual annotation and paves the way for advanced self-supervised learning in benthic habitat mapping.

### 🤖 AI 总结

**一句话总结**：Side-Scan Sonar (SSS) is a primary modality for large-scale underwater mapping, yet automated perception and cross-modal alignment are severely bottlenecked by acoustic complexities such as speckle no...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Geometry-Driven, Opti-Acoustic, Co-Registration, View-Invariant, Reflectivity, Mapping, Side-Scan, Sonar

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23479v1) | [下载PDF](https://arxiv.org/pdf/2608.23479v1.pdf)

---

## [23. Image-Conditioned Diffusion Models for Quality Assurance of Organ-at-Risk Segmentations in Radiotherapy](https://arxiv.org/abs/2608.23432v1)

**作者**：Clea Dronne, Catharine H Clark, Xavier Loizeau 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-24

### 📄 论文摘要

Accurate organ-at-risk segmentation is essential for radiotherapy planning, but reviewing segmentations is time-consuming and subjective. We investigate normative modelling for segmentation error detection in head-and-neck CT, comparing a VAE framework with an image-conditioned segmentation diffusion model. Models were evaluated on RADCURE brainstem and spinal cord segmentations using simulated boundary and width perturbations. Error detection was assessed using the Dice similarity coefficient and the Distance to Agreement (DTA) between the input and reconstructed segmentations. While both models detected some simulated errors, regional DTA showed that the diffusion model localised subtle boundary errors more consistently. These results support image-conditioned diffusion reconstruction as a promising framework for localised, anatomy-aware segmentation QA.

### 🤖 AI 总结

**一句话总结**：Accurate organ-at-risk segmentation is essential for radiotherapy planning, but reviewing segmentations is time-consuming and subjective. We investigate normative modelling for segmentation error dete...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, of, Image-Conditioned, Models, Quality, Assurance, Organ-at-Risk, Segmentations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23432v1) | [下载PDF](https://arxiv.org/pdf/2608.23432v1.pdf)

---

## cs.LG

## [24. Provably adaptive sampling with uniform and remasking discrete diffusion models](https://arxiv.org/abs/2608.23554v1)

**作者**：Daniil Dmitriev, Zhihan Huang, Yuting Wei  
**分类**：cs.LG, cs.IT, math.ST, stat.ML  
**发布时间**：2026-08-24

### 📄 论文摘要

Discrete diffusion models offer a promising alternative to autoregressive generation by enabling parallel updates, but their sampling efficiency can depend strongly on the choice of the forward process and the sampler. For the uniform forward process, existing lower bounds for the standard $τ$-leaping sampler scale linearly with the ambient dimension $d$, raising the question of whether this dependence is intrinsic to the forward process. We answer this question in the negative. We consider a first-order sampler based on the leave-one-out denoiser for uniform and remasking processes whose coordinate updates can be performed in parallel. In both cases, the sampler can correct denoising mistakes during the sampling process, which becomes necessary when many coordinates are updated together. Our main result establishes an adaptive sampling guarantee: up to logarithmic factors, $N = O(\mathrm{DTC}(X_0) / \varepsilon)$ discretization steps suffice to achieve sampling error $O(\varepsilon_{\mathrm{score}}+\varepsilon)$, where $\varepsilon_{\mathrm{score}}$ is the error in score estimation. Thus, the sampling complexity is governed by the intrinsic dependence structure of the target distribution, as measured by its dual total correlation $\mathrm{DTC}(X_0)$, rather than directly by the ambient dimension $d$. Our analysis proceeds through a Bayes-optimal auxiliary sampler that separates discretization error from score-estimation error. We also derive an exact information-theoretic representation of the discretization error in terms of the mutual information between different coordinates of the forward process at different times. This representation applies to general forward processes and, in the uniform and remasking cases, can be controlled by $\mathrm{DTC}(X_0)$. Numerical experiments on structured synthetic distributions illustrate the predicted dimension-adaptive behavior.

### 🤖 AI 总结

**一句话总结**：Discrete diffusion models offer a promising alternative to autoregressive generation by enabling parallel updates, but their sampling efficiency can depend strongly on the choice of the forward proces...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Provably, adaptive, sampling, uniform, remasking, discrete, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23554v1) | [下载PDF](https://arxiv.org/pdf/2608.23554v1.pdf)

---

## [25. MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning of Lightweight Time Series Forecasters](https://arxiv.org/abs/2608.23473v1)

**作者**：ChengAo Shen, Wenchao Yu, Fangyu Wu 等 9 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-24

### 📄 论文摘要

Time series forecasting (TSF) is evolving toward multimodal and agentic settings, yet using foundation models remains uneconomical in resource-constrained scenarios, where compact, specialized forecasters are more desirable. However, lightweight forecasters typically require substantial training data, limiting their use in domains with scarce, slowly accumulated, or privacy-sensitive time series. To address this dilemma, we investigate the challenging problem of few-shot learning for lightweight forecasters. We propose MetaCaster, a meta-harness-optimized multi-agent framework that uses agentic data generation to automatically train specialized lightweight forecasters from only a few examples and textual contexts. Our work highlights a new TSF paradigm in which agents act not as forecasters but as intermediary engineers that prepare efficient, task-specific forecasters for deployment. Experiments on 18 datasets, 23 state-of-the-art lightweight forecasters, and 14 baselines demonstrate that MetaCaster achieves both data efficiency and computational efficiency while maintaining high-quality TSF performance.

### 🤖 AI 总结

**一句话总结**：Time series forecasting (TSF) is evolving toward multimodal and agentic settings, yet using foundation models remains uneconomical in resource-constrained scenarios, where compact, specialized forecas...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, of, MetaCaster, Meta-Harness-Optimized, End-to-End, Few-Shot, Learning, Lightweight

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23473v1) | [下载PDF](https://arxiv.org/pdf/2608.23473v1.pdf)

---

## [26. RAD: Rule-Augmented Relational Anomaly Detection](https://arxiv.org/abs/2608.23468v1)

**作者**：Noah Dahle, Anne Tumlin, Ngoc Tran 等 5 位作者  
**分类**：cs.LG, cs.CR, cs.DB  
**发布时间**：2026-08-24

### 📄 论文摘要

Anomaly detection is often applied to data stored in relational databases, yet most existing methods require flattening multiple tables into a single feature matrix. This flattening can obscure entity identity, schema structure, and multi-hop dependencies, limiting the detection of anomalies that depend on relational context rather than isolated feature values. Beyond preserving relational structure, relational anomaly detection raises an additional challenge: how to incorporate symbolic behavioral evidence into learned relational representations. To address these challenges, we study relational anomaly detection, where the goal is to identify anomalous entities or events in a multi-table database. We propose RAD, a rule-augmented relational anomaly detector that combines heterogeneous graph representation learning with refined symbolic rule signals. RAD derives candidate rules from random-forest paths over flattened summaries of the entities or events being scored, refines them into compact interpretable predicates, injects the resulting rule features into the graph model, and learns anomaly scores using reconstruction-based and pairwise-ranking supervision. To evaluate this setting, we introduce a relational anomaly detection benchmark spanning three settings: LANL cybersecurity event detection and two unexpected user-churn anomaly tasks derived from Amazon and H&M relational databases. Experiments show that RAD improves anomaly ranking over flattened tabular detectors and relational baselines under natural class imbalance, achieving the best average rank on AUROC and AUPRC across the benchmark. Ablations show that direct rule injection and ranking-based supervision are key contributors to performance, while edge reconstruction is not uniformly beneficial. Our code and data are available at: https://github.com/noahd15/RAD_RelationalAnomalyDetection.

### 🤖 AI 总结

**一句话总结**：Anomaly detection is often applied to data stored in relational databases, yet most existing methods require flattening multiple tables into a single feature matrix. This flattening can obscure entity...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RAD, Rule-Augmented, Relational, Anomaly, Detection, often, applied, data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23468v1) | [下载PDF](https://arxiv.org/pdf/2608.23468v1.pdf)

---

## [27. Diversity-Based Active Learning: An Evaluation of Metric Spaces for Active Learning Selection](https://arxiv.org/abs/2608.23461v1)

**作者**：Siddharth Chilamkur, Dorit S. Hochbaum  
**分类**：cs.LG  
**发布时间**：2026-08-24

### 📄 论文摘要

With rapid advancement over the last few years, many different methods are now widely used for classification. However, training these models requires substantial labeled data. Active Learning is a potential solution to this problem. Pool-based active learning minimizes costs by querying only the most informative samples from an unlabeled dataset. Diversity-based approaches, on the other hand, attempt to select a representative subset of the data. There are many different objectives for determining the selection process, including exact K-center, exact K-median, and Greedy K-center. In this paper, we will focus on evaluating the performance of Greedy K-center across a variety of metric spaces: the raw feature space, a Linear Discriminant Analysis (LDA) space, and a model-derived probability space (with and without entropy-based weighting). Using Random Forest classifiers as a baseline evaluator, our empirical results on synthetic and real-world datasets demonstrate that mapping unlabeled instances into a predictive probability space and weighting the result by entropy often dominates the other options for active learning selection with Greedy K-center.

### 🤖 AI 总结

**一句话总结**：With rapid advancement over the last few years, many different methods are now widely used for classification. However, training these models requires substantial labeled data. Active Learning is a po...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, of, Diversity-Based, Active, Learning, Evaluation, Metric, Spaces

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23461v1) | [下载PDF](https://arxiv.org/pdf/2608.23461v1.pdf)

---

## [28. Traceable Spectral Inference via Influence Functions: Efficient Data Attribution and Error Proxies for the Ariel Mission](https://arxiv.org/abs/2608.23458v1)

**作者**：Nikki Grens, Luís F. Simões, Kai Hou Yip 等 4 位作者  
**分类**：cs.LG, astro-ph.IM, stat.ML  
**发布时间**：2026-08-24

### 📄 论文摘要

Interpretability is critical for machine learning models deployed in scientific space missions such as ESA's Ariel, where ground truth is unavailable during operations and physical plausibility must be assessed. While most explainable AI methods focus on feature attribution, this work investigates training data attribution through influence functions and introduces three key contributions for operational spectroscopy pipelines. First, influence is reformulated in terms of prediction rather than loss, enabling label-free deployment. Second, by leveraging the closed-form ridge solution of an Extreme Learning Machine, infinitesimal prediction influence is efficiently computed. Third, an influence-based conservative error proxy is derived by propagating training residuals through the influence sensitivities. Evaluated against simulated spectra, the proposed proxy correlates strongly with scale and shape-based spectral errors. Furthermore, influence functions enable the identification of the most influential samples and the approximation of the most harmful ones. Together, these results suggest that this approach can serve as an operational framework for scientific machine learning.

### 🤖 AI 总结

**一句话总结**：Interpretability is critical for machine learning models deployed in scientific space missions such as ESA's Ariel, where ground truth is unavailable during operations and physical plausibility must b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Traceable, Spectral, Inference, via, Influence, Functions, Efficient, Data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23458v1) | [下载PDF](https://arxiv.org/pdf/2608.23458v1.pdf)

---

## [29. ChebBooster: A Training-Free Approach for Efficient Diffusion Transformer Inference via Chebyshev-Inspired Extrapolation](https://arxiv.org/abs/2608.23429v1)

**作者**：Chengjie Lu, Tianchi Deng, Zhengqi He 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-24

### 📄 论文摘要

Diffusion Transformers (DiTs) have shown strong performance in high-fidelity image generation, but their sampling process remains computationally intensive due to full model execution at every timestep. While cache-based acceleration has been explored to mitigate inference cost, naive reuse schemes suffer from low accuracy over long intervals, and Taylor-series-based extrapolation methods often face instability caused by Runge oscillations. In this paper, we propose ChebBooster, a training-free extrapolation framework based on Chebyshev polynomial theory that achieves stable and efficient acceleration for DiTs. Specifically, we adopt the Barycentric formulation to evaluate Chebyshev approximants with high numerical stability and minimal overhead, and further decouple the extrapolation into an offline weight precomputation phase and a lightweight online application stage. Extensive experiments across three representative DiT-based models, including DiT-XL/2, PixArt-$Σ$, and FLUX.1-dev, demonstrate that ChebBooster achieves consistent improvements in visual quality and inference efficiency, reaching up to $3.68\times$ latency speedup and $5.12\times$ FLOPs reduction, outperforming existing training-free baselines under diverse generation tasks and resolutions.

### 🤖 AI 总结

**一句话总结**：Diffusion Transformers (DiTs) have shown strong performance in high-fidelity image generation, but their sampling process remains computationally intensive due to full model execution at every timeste...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, ChebBooster, Training-Free, Approach, Efficient, Transformer, Inference, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23429v1) | [下载PDF](https://arxiv.org/pdf/2608.23429v1.pdf)

---

## [30. The Axiomatic Trader: Latent Regularity, Information Budgets, and the Canonical Form of a Quantitative Investment System](https://arxiv.org/abs/2608.23416v1)

**作者**：Jiayu Li  
**分类**：cs.LG, q-fin.PM  
**发布时间**：2026-08-24

### 📄 论文摘要

Systematic trading rests on one article of faith: that regularities found in the past persist. We state it as a time-invariant mechanism driven by an unobserved latent state, and show that it leaves a researcher five constants to declare --- the recurrence bound $Lambda$ at a block length $b$, the invariance defect $epsilon_0$ of the representation it is declared of, the coherence times $ell_i$ of the state's coordinates, the signal ceiling $rho$ and the fraction $kappa$ of it contingent on the regime --- after which the architecture of a correct quantitative investment system is nearly forced.

### 🤖 AI 总结

**一句话总结**：Systematic trading rests on one article of faith: that regularities found in the past persist. We state it as a time-invariant mechanism driven by an unobserved latent state, and show that it leaves a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Axiomatic, Trader, Latent, Regularity, Information, Budgets, Canonical, Form

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.23416v1) | [下载PDF](https://arxiv.org/pdf/2608.23416v1.pdf)

---

