# arXiv AI 论文日报 | 2026-07-25

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (12 篇)
- [cs.CL](#csCL) (6 篇)
- [cs.LG](#csLG) (5 篇)
- [cs.AI](#csAI) (7 篇)

---

## cs.AI

## [1. OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/abs/2607.21557v1)

**作者**：Xiao Yu, Baolin Peng, Ruize Xu 等 10 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-07-23

### 📄 论文摘要

Modern AI agents rely on elaborate inference harnesses such as Claude Code, Codex, and OpenClaw to drive multi-turn reasoning, tool use, and access to external systems. While powerful, these complex harnesses also make agents hard to train end-to-end with open infrastructure, whose SFT/RL stacks cannot natively express stateful, multi-process harness inference. To address this, we present OpenForgeRL, an open-source framework for training harness-based agents end-to-end in diverse environments. OpenForgeRL achieves this with a lightweight proxy that serves the harness's model calls while recording them as training data for a standard RL codebase (e.g., veRL), and a Kubernetes orchestrator that runs each rollout in its own remote container, together enabling training on any harness in any environment at scale. By decoupling training and inference, OpenForgeRL allows researchers to easily train, study, and improve agents directly in the real harnesses and environments they are deployed with. We validate our framework across diverse, complex harnesses and environments, spanning tool/claw-based agents and multimodal GUI browser- and computer-use agents. Using only hundreds to a few thousand tasks, OpenForgeClaw reaches 31.7 pass^3 and 55.9 pass@3 on ClawEval and 33.7 on QwenClawBench. OpenForgeGUI reaches 37.7 on OSWorld-Verified, 63.0 on Online-Mind2Web, and 72.3 on WebVoyager. Both outperform open baselines of similar size on nearly all benchmarks, and in the GUI setting match or surpass models several times larger. Beyond benchmarks, we analyze how harness choice (e.g., ZeroClaw, OpenClaw, Codex) and RL shape agent behavior. We find that some harnesses are substantially harder to learn than others, and that RL improves agentic reliability, such as self-verification, tool coverage, and completing multi-step plans, though critical abilities such as error recovery remain weak.

### 🤖 AI 总结

**一句话总结**：Modern AI agents rely on elaborate inference harnesses such as Claude Code, Codex, and OpenClaw to drive multi-turn reasoning, tool use, and access to external systems. While powerful, these complex h...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, OpenForgeRL, Train, Harness-native, Any, Environment, Modern, rely

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21557v1) | [下载PDF](https://arxiv.org/pdf/2607.21557v1.pdf)

---

## [2. MIRROR: Learning from the Other View for Multi-Modal Reasoning](https://arxiv.org/abs/2607.21552v1)

**作者**：Wen Ye, Yuxiao Qu, Aviral Kumar 等 4 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-07-23

### 📄 论文摘要

Unlike large language models (LLMs) that exhibit strong reasoning capabilities, vision-language models (VLMs) struggle with visual reasoning, even on geometry problems that admit equivalent text, diagram, and combined diagram+text views. We show that these views often elicit different behaviors: a model may solve a problem from text but fail on the corresponding diagram, or succeed visually while failing textually. This inconsistency suggests that different views expose complementary reasoning paths and failure modes that standard multimodal post-training does not fully exploit. To study and exploit this phenomenon, we construct ODA-Data, a high-quality paired multimodal geometry dataset with text-dominant, image-dominant, and combined image+text views of the same problems, together with splits for training and evaluating modality-dependent reasoning behaviors. We then develop Modality-Informed Reciprocal Reasoning Optimization (MIRROR), a reinforcement learning approach for improving multimodal reasoning via self supervision. For each problem, MIRROR evaluates the model under all views, selects the best-performing view as a teacher, and trains other views with a reverse-KL objective towards the teacher. Across reasoning benchmarks that evaluate on geometry problems, MIRROR improves over standard RL and yields more accurate and consistent behavior across modalities

### 🤖 AI 总结

**一句话总结**：Unlike large language models (LLMs) that exhibit strong reasoning capabilities, vision-language models (VLMs) struggle with visual reasoning, even on geometry problems that admit equivalent text, diag...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MIRROR, Learning, Other, View, Multi-Modal, Reasoning, Unlike, large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21552v1) | [下载PDF](https://arxiv.org/pdf/2607.21552v1.pdf)

---

## [3. The Boundaries of Automation: A Theory of Persistent Human Participation](https://arxiv.org/abs/2607.21547v1)

**作者**：Fares Fourati, Hinrich Schütze, Eyke Hüllermeier 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.ET, cs.LG, cs.MA  
**发布时间**：2026-07-23

### 📄 论文摘要

The rapid progress of AI has intensified the long-standing pursuit of automation: replacing human participation with algorithms wherever possible. Implicit in this pursuit is the assumption that humans remain in the loop only because current AI systems are not yet sufficiently capable. This paper challenges that assumption. Rather than asking how far automation can extend, we ask where its conceptual limits lie and argue that human participation may persist even with highly capable AI systems for three distinct reasons. Technical or complementarity grounds arise when humans contribute capabilities or perspectives unavailable to AI. Normative or developmental grounds arise when participation itself is valuable for human agency or learning. Most importantly, emergence grounds arise from target emergence: in some activities, the target is not fully specified in advance but instead emerges through the interaction itself. In these cases, human participation is not merely a means of improving execution but is constitutive of the target being produced. Human--AI co-construction, understood as the joint production of outcomes by humans and AI systems, is therefore not simply a temporary response to imperfect AI, but a persistent feature of activities whose objectives emerge through participation. This perspective has important implications for the limits of automation and for the design, evaluation, and ethics of future AI systems.

### 🤖 AI 总结

**一句话总结**：The rapid progress of AI has intensified the long-standing pursuit of automation: replacing human participation with algorithms wherever possible. Implicit in this pursuit is the assumption that human...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Boundaries, Automation, Theory, Persistent, Human, Participation, rapid

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21547v1) | [下载PDF](https://arxiv.org/pdf/2607.21547v1.pdf)

---

## [4. Same Dangerous Objective, Opposite Advice: Direct Exposure versus Multi-Agent Mediation](https://arxiv.org/abs/2607.21518v1)

**作者**：Linjun Li  
**分类**：cs.AI  
**发布时间**：2026-07-23

### 📄 论文摘要

Even a current high-capability LLM can appear safer when shown a dangerous objective directly than when other agents transform and relay its direction. Using OpenAI's gpt-5.6-sol model alias, we test 25 pre-specified mirrored trade-off profiles. Direct exposure to an objective authorizing concealment, fabrication, and pressure produced advice net opposed to its target. After an Id and Censor transformed the same objective into affect and a constraint-rewritten, target-bearing intention, the user-facing Superego---which saw the preferred direction but not the raw objective, its manipulative clauses, or its source---produced advice net aligned with the target.   This behavioral reverse shift is consistent with the model recognizing or distrusting the manipulative motive, although we do not identify its internal mechanism. The second result exposes a compositional safety gap: a current high-capability model can be used as the user-facing component of an automated, multi-stage workflow serving an explicitly manipulative objective. The workflow can keep the raw instruction, its manipulation-authorizing clauses, and its provenance outside the downstream model's context while preserving the objective's target direction. A user with endpoint-only access likewise cannot directly inspect those upstream messages including the objective.

### 🤖 AI 总结

**一句话总结**：Even a current high-capability LLM can appear safer when shown a dangerous objective directly than when other agents transform and relay its direction. Using OpenAI's gpt-5.6-sol model alias, we test ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Same, Dangerous, Objective, Opposite, Advice, Direct, Exposure, versus

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21518v1) | [下载PDF](https://arxiv.org/pdf/2607.21518v1.pdf)

---

## [5. Toward Continuous Assurance for the Democratization of AI Agent Creation in Industry](https://arxiv.org/abs/2607.21495v1)

**作者**：Natan Levy, Harel Berger  
**分类**：cs.AI, cs.ET, cs.MA  
**发布时间**：2026-07-23

### 📄 论文摘要

AI agents are increasingly created inside organizations by non-engineering users through low-code, no-code, and conversational development environments. This democratization enables rapid local innovation, but it also creates a reliability gap: agents that appear to users as simple productivity artifacts may depend on changing models, tools, retrieval sources, permissions, prompts, schedules, and external services. These dependencies can cause silent degradation long after deployment, even when no user directly modifies the agent. This paper identifies the reliability challenge created by democratized AI agent creation and proposes a lightweight continuous-assurance framework for citizen-created organizational agents. The framework combines dependency mapping, readiness contracts, scheduled checks, diagnostics, and lifecycle governance to assess whether an agent remains operationally ready under expected conditions. We also present an initial prototype auditor and scenario-based assessment showing how the proposed taxonomy can be translated into practical checks and actionable remediation guidance.

### 🤖 AI 总结

**一句话总结**：AI agents are increasingly created inside organizations by non-engineering users through low-code, no-code, and conversational development environments. This democratization enables rapid local innova...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, Toward, Continuous, Assurance, Democratization, Creation, Industry

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21495v1) | [下载PDF](https://arxiv.org/pdf/2607.21495v1.pdf)

---

## [6. Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks](https://arxiv.org/abs/2607.21482v1)

**作者**：Mack Nixon, Liam Wright, Yevgeniya Kovalchuk 等 7 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-07-23

### 📄 论文摘要

Large language models (LLMs) and agents are now widely used tools in code development, with data typically sent to third-party cloud-based models. Their adoption in research using personal data is constrained by governance requirements that typically prohibit data transmission to external services. Locally deployable open-weight models offer an alternative since sensitive data never leave the local environment. We introduce an open-source framework for evaluating the efficacy of AI agents powered by open-weight LLMs on one of the most persistent bottlenecks in research on longitudinal population studies: data preparation. The framework comprises: a curated ground-truth dataset (cleaning scripts preparing six sweeps of data from a British cohort study), task definitions encompassing tasks such as category harmonization and multi-wave merging, and automated routines for evaluating the LLM-produced R code and outputted data. We benchmark LLMs across the (consumer grade) deployment spectrum to assess their efficacy in 20 data preparation tasks (creation of 102 variables). Current state-of-the-art, 31-35B parameter models almost saturated our benchmark ("average task completion" up to 87.9%). The performance of open-weight LLMs running on consumer-grade hardware shows promise of a viable path toward AI-assisted data preparation in governance-restricted research settings. Our framework is publicly available at: https://github.com/UCL-ARC/RRBench.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) and agents are now widely used tools in code development, with data typically sent to third-party cloud-based models. Their adoption in research using personal data is con...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agentic, coding, without, cloud, evaluating, open-weight, large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21482v1) | [下载PDF](https://arxiv.org/pdf/2607.21482v1.pdf)

---

## [7. AREX: Towards a Recursively Self-Improving Agent for Deep Research](https://arxiv.org/abs/2607.21461v1)

**作者**：Shuqi Lu, Chaofan Li, Kun Luo 等 24 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-23

### 📄 论文摘要

Deep research requires agents to find answers that jointly satisfy multiple constraints. Discovering such answers is costly, whereas verifying a candidate can often be decomposed into tractable constraint-wise checks. This discovery--verification asymmetry suggests that a research agent should do more than simply search longer: it should recursively improve its current answer by verifying intermediate results and using the partially verified state to guide subsequent refinement. We introduce AREX, a family of Recursively Self-Improving (RSI) deep research agents. AREX alternates between an inner research loop that gathers evidence and constructs a provisional answer, and an outer self-improvement loop that audits the answer constraint-wise, identifies unresolved claims, and launches targeted follow-up research. To sustain RSI over long horizons, AREX learns an autonomous context-update tool that compresses growing interaction history into a compact improvement state preserving verified evidence and unresolved constraints, without relying on an external model. We train AREX on verified synthetic tasks and high-quality trajectories through agentic mid-training and long-horizon reinforcement learning. To mitigate sparse final rewards during long horizon learning, we emphasize key steps where decisive evidence is acquired or erroneous research directions are corrected. We instantiate a dense 4B model and a 122B-A10B Mixture-of-Experts model. Across BrowseComp, WideSearch, DeepSearchQA, Humanity's Last Exam (HLE), and other reasoning and tool-use benchmarks, AREX substantially outperforms comparable-scale baselines and remains competitive with models using substantially more activated parameters.

### 🤖 AI 总结

**一句话总结**：Deep research requires agents to find answers that jointly satisfy multiple constraints. Discovering such answers is costly, whereas verifying a candidate can often be decomposed into tractable constr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, AREX, Towards, Recursively, Self-Improving, Deep, Research, requires

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21461v1) | [下载PDF](https://arxiv.org/pdf/2607.21461v1.pdf)

---

## cs.CL

## [8. Surprisal Theory is Tautological (without Rational Grounding)](https://arxiv.org/abs/2607.21574v1)

**作者**：Ryan Cotterell  
**分类**：cs.CL  
**发布时间**：2026-07-23

### 📄 论文摘要

Surprisal theory holds that the human processing difficulty of a linguistic unit in context is an affine function of its surprisal under some language model. I argue this claim is a tautology without further constraint: for any non-negative difficulty measure over units in context, there exists a language model whose surprisal is an affine function of it under mild technical conditions. Therefore, because any pattern of difficulty is consistent with some language model, without an additional constraint on the language model, surprisal theory makes no falsifiable predictions. The tautology was long obscured by an assumption implicit in two decades of psycholinguistic work---that the relevant language model is the distribution that generated the training corpus, so that improving corpus fit improves predictions of human behavior. Recent empirical work has undermined this assumption, demonstrating that better corpus models can be worse predictors of processing difficulty. I conclude that breaking the tautology requires a rationalist intervention, i.e., the relevant language model must be derived from a non-empirically motivated model of the comprehender, which could be based on, for instance, memory constraints or processing goals, and that, thus, does not depend on the behavioral data surprisal theory is meant to explain.

### 🤖 AI 总结

**一句话总结**：Surprisal theory holds that the human processing difficulty of a linguistic unit in context is an affine function of its surprisal under some language model. I argue this claim is a tautology without ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Surprisal, Theory, Tautological, without, Rational, Grounding, holds, human

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21574v1) | [下载PDF](https://arxiv.org/pdf/2607.21574v1.pdf)

---

## [9. DONDO: Open w2v-BERT Speech-Recognition Base Models for African Languages](https://arxiv.org/abs/2607.21540v1)

**作者**：Paul Azunre  
**分类**：cs.CL  
**发布时间**：2026-07-23

### 📄 论文摘要

We present DONDO, a family of open, permissively licensed automatic speech recognition (ASR) base models for African languages, built on the w2v-BERT 2.0 self-supervised speech encoder. DONDO comprises twenty-one monolingual models and five multilingual models spanning twenty-seven language varieties across Ghana, Sierra Leone, Nigeria, Senegal, Kenya and Zimbabwe. Models are fine-tuned primarily on read speech drawn from religious texts, which offer broad, license-clear and orthographically consistent coverage for languages that otherwise lack transcribed audio. We describe a two-step (and, for one family, three-step) learning-rate-annealed fine-tuning procedure that first adapts a shared multilingual model at a high learning rate and then anneals it to recover, and in several cases surpass, strong monolingual baselines. We further describe a lightweight language-conditioning mechanism that injects a one-hot language identity as a sequence of prefix frames prepended to the acoustic features, allowing a single multilingual checkpoint to be steered to a target language at inference. Across the five multilingual families the annealed models reach average word error rates (WER) of 10-13%, closing most of the gap to monolingual models while covering many languages in a single checkpoint. All models are released on the Hugging Face KhayaAI organisation under the Apache-2.0 license (attribution only) so that others may fine-tune them freely, including for commercial use. We provide a conservative estimate that the languages covered are spoken by on the order of one hundred million first-language speakers, and by substantially more when second-language use is included.

### 🤖 AI 总结

**一句话总结**：We present DONDO, a family of open, permissively licensed automatic speech recognition (ASR) base models for African languages, built on the w2v-BERT 2.0 self-supervised speech encoder. DONDO comprise...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DONDO, Open, w2v-BERT, Speech-Recognition, Base, Models, African, Languages

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21540v1) | [下载PDF](https://arxiv.org/pdf/2607.21540v1.pdf)

---

## [10. Artificial Epanorthosis: Why large language models overuse a classical rhetorical figure, and how to mitigate it](https://arxiv.org/abs/2607.21498v1)

**作者**：Federico Boggia  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-23

### 📄 论文摘要

A rhetorical figure that Cicero and Quintilian catalogued two thousand years ago reappears, systematically, in the text of large language models: epanorthosis, the self-correction of the specimen «This is not a course. It is a journey of transformation». This essay argues that the overuse is a trained disposition, driven mainly by a training distribution rich in promotional prose and by preference tuning (RLHF) that rewards confident, emphatic phrasing; the left-to-right nature of generation is an amplifier rather than the root cause. Building on evidence that models diverge from human rhetorical style, and on Fontanier's classification of epanorthosis as a figure of thought, it sets out a programme that scores the figure against genre-specific human baselines through an Epanorthosis Index (density relative to the human rate). A first measurement, on three sizes of one instruction-tuned model family, finds mis-calibration by register in both directions: the models overshoot in oratory (about twofold, near threefold in Italian, concentrated in the larger tiers) and undershoot in informal question-and-answer writing, while matching humans in argument, journalism, and encyclopedic prose. Three constructive contributions follow: a survey of mitigation techniques centred on lightweight LoRA adapters; a demonstration, in Italian, that a one-line instruction cuts the figure by half to nearly three-quarters and that a supervised-fine-tuning adapter removes it almost entirely, with a scaling coefficient that dials the reduction back onto the human rate; and the argument that the target is calibration to the human rate for each genre, not elimination. It closes on the stakes: the real risk is that we begin to write like the machines.

### 🤖 AI 总结

**一句话总结**：A rhetorical figure that Cicero and Quintilian catalogued two thousand years ago reappears, systematically, in the text of large language models: epanorthosis, the self-correction of the specimen «Thi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Artificial, Epanorthosis, Why, large, language, models, overuse, classical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21498v1) | [下载PDF](https://arxiv.org/pdf/2607.21498v1.pdf)

---

## [11. What, Where, and How: Disentangling the Roles of Task, Language, and Model in Code Model Representations](https://arxiv.org/abs/2607.21491v1)

**作者**：Piotr Wilam  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-07-23

### 📄 论文摘要

Do independently trained language models come to represent the same thing in the same way? We answer for code, extending a recently introduced concept-circuit extraction method to a 2x2 design -- Python and Rust crossed with Qwen2.5-Coder-7B and DeepSeek-Coder-V1-6.7B -- and measuring a complete inventory of grammatical concepts (58 Python, 57 Rust) identically in all four cells: the smallest design that separates what depends on the task, the language, and the model.   The answer splits into three parts. What earns dedicated circuitry is set by the task: the models agree on which concepts receive circuits (Spearman $ρ$ = 0.638 for Python, 0.673 for Rust, both p < $10^{-7}$). Where those circuits sit is set by the model: Qwen processes concepts in a late band (~L17-19), DeepSeek at L6-7, for both languages. How circuits grow across layers is also set by the model: Qwen gives its atomic concepts an early spike that DeepSeek does not. "Are circuits universal?" thus has no single answer: yes for What, no for Where and How -- universality is a property of representational content, not of computational organisation.   None of this structure was fixed in advance. The agreement could have landed anywhere between independence and identity; it lands at $ρ\approx 0.65$. Rust constructs receive 2-3x more concept-specific circuitry than their Python equivalents, in both models. Both models share neurons between the languages (6/7 and 7/7 paired constructs), DeepSeek 1.94x more than Qwen -- a direction no prior result predicts. And Qwen binds nine keywords of Rust's type-and-trait machinery into one tight neuron cluster (Jaccard 0.535 vs null 0.112, p < 0.001), a semantic dimension invisible in surface syntax. Ablation and linear probes confirm the circuits are functional.   All claims are scoped to this 2x2; whether the per-model profile predicts a third model is the designed next test.

### 🤖 AI 总结

**一句话总结**：Do independently trained language models come to represent the same thing in the same way? We answer for code, extending a recently introduced concept-circuit extraction method to a 2x2 design -- Pyth...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, What, Where, How, Disentangling, Roles, Task, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21491v1) | [下载PDF](https://arxiv.org/pdf/2607.21491v1.pdf)

---

## [12. RUMBA: Russian User Memory Benchmark](https://arxiv.org/abs/2607.21447v1)

**作者**：Elizaveta Shevtsova, Inna Glebkina, Mark Baushenko 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-23

### 📄 论文摘要

The ability to handle long-term memory in LLMs is becoming increasingly critical, yet existing benchmarks remain English-centric and rely on aggregate retrieval metrics, failing to capture interactions between long-range context, temporal information, and reasoning. To address this, we introduce RUMBA (Russian User Memory BenchmArk) - a new benchmark for long-term conversational memory that provides a fine-grained taxonomy of memory-centric question types and a unified methodology accounting for semantic type, session scope, temporal reasoning, and the explicitness of temporal expressions. RUMBA consists of timestamped user-assistant dialogues with QA pairs requiring retrieval, combination, and reasoning across sessions. While designed for Russian, we also provide an aligned English subset under the same methodology. We evaluate contemporary memory systems and long-context models, and show how RUMBA serves as a diagnostic tool to analyze model behavior across benchmark slices and identify strengths and failure modes of different memory mechanisms.

### 🤖 AI 总结

**一句话总结**：The ability to handle long-term memory in LLMs is becoming increasingly critical, yet existing benchmarks remain English-centric and rely on aggregate retrieval metrics, failing to capture interaction...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RUMBA, Russian, User, Memory, Benchmark, ability, handle, long-term

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21447v1) | [下载PDF](https://arxiv.org/pdf/2607.21447v1.pdf)

---

## [13. When Trivia Is Not Trivial: Everyday Knowledge Failures in Multilingual LLMs](https://arxiv.org/abs/2607.21445v1)

**作者**：Anna Mosolova, Djamé Seddah  
**分类**：cs.CL  
**发布时间**：2026-07-23

### 📄 论文摘要

Quiz rooms, trivia nights, and quiz shows challenge human knowledge across a wide range of topics, from canonical facts to everyday culture. In this paper, we examine whether large language models (LLMs) can perform competitively in such settings, using quiz-style questions to test them on both common and niche topics. We introduce TriviaRoomQA, a multilingual benchmark designed to evaluate everyday, culturally grounded, and long-tail knowledge across 288 topics. The benchmark contains 3,300 parallel multiple-choice questions in six European languages and additional 5,340 French-only questions for a more fine-grained case study. We evaluate 30 open-weight LLMs from European, Asian, and North American providers, covering models from 7 to 70B parameters. We find that models are strong on knowledge-intensive topics such as history, geography, and mathematics, but substantially weaker on everyday popular-culture topics such as celebrities, music, movies, and news. Moreover, model performance varies across languages even for the same underlying questions, suggesting that access to factual knowledge is not always language-independent. In sum, our dataset and experiments demonstrate an important knowledge gap which is not captured by existing academic-based saturated benchmarks.

### 🤖 AI 总结

**一句话总结**：Quiz rooms, trivia nights, and quiz shows challenge human knowledge across a wide range of topics, from canonical facts to everyday culture. In this paper, we examine whether large language models (LL...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Trivia, Not, Trivial, Everyday, Knowledge, Failures, Multilingual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21445v1) | [下载PDF](https://arxiv.org/pdf/2607.21445v1.pdf)

---

## cs.CV

## [14. Unified Video Dense Prediction from Disjoint Data](https://arxiv.org/abs/2607.21592v1)

**作者**：Yihong Sun, Seoung Wug Oh, Jiahui Huang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-23

### 📄 论文摘要

Scene understanding requires simultaneous prediction about geometry, appearance, and semantics. However, existing task-specific annotations are fragmented across incompatible, domain-specific datasets. Current unified systems circumvent this by restricting training to fully co-annotated data, or by incurring the large computational cost of pseudo-labeling. To mitigate this, we introduce UniD, a unified video model that jointly predicts eight dense scene properties-depth, surface normals, semantic segmentation, boundaries, human parts, albedo, shading, and materials-all learned from disjoint, domain-specific datasets. We propose a simple yet effective distillation step in which per-task experts supervise a unified backbone through lightweight task projectors, eliminating the need for annotation overlap or pseudo-labeling. Our key insight is that the strong visual priors of a pretrained diffusion model are sufficient to bridge the domain gaps introduced by disjoint training sources, enabling robust generalization to scene-task combinations never seen during training. UniD achieves competitive performance against per-task specialists and multi-task baselines, with strong generalization to out-of-distribution scenarios and enhanced temporal and cross-task consistency. Code and video results are available at https://unid-video.github.io/.

### 🤖 AI 总结

**一句话总结**：Scene understanding requires simultaneous prediction about geometry, appearance, and semantics. However, existing task-specific annotations are fragmented across incompatible, domain-specific datasets...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unified, Video, Dense, Prediction, Disjoint, Data, Scene, understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21592v1) | [下载PDF](https://arxiv.org/pdf/2607.21592v1.pdf)

---

## [15. Inference-Time Scaling of Diffusion Models via Progressive Seed Pruning](https://arxiv.org/abs/2607.21591v1)

**作者**：Rogerio Guimaraes, Pietro Perona  
**分类**：cs.CV  
**发布时间**：2026-07-23

### 📄 论文摘要

Diffusion and flow-matching models dominate conditional image generation, yet inference-time scaling for these models is far less developed than for autoregressive language models. Because final quality is highly sensitive to the initial noise seed, many approaches spend extra compute on seed search or resampling under a black-box reward, but typically maintaining a constant memory footprint throughout inference. We show that relaxing this constraint enables an underexplored inference-time scaling axis: by front-loading exploration, evaluating many seeds early, and pruning aggressively, we can use a fixed compute budget more effectively. \emph{Progressive Seed Pruning} (\PSP) scores intermediate denoised estimates and progressively narrows the candidate set so that only promising trajectories are fully denoised, while keeping the total number of model evaluations fixed. Across diffusion and flow-matching backbones, \PSP \ consistently improves reward-guided selection and achieves higher GenEval scores (automated) and better human evaluation on prompt-alignment than best-of-$N$, importance-sampling, and tree-search baselines at matched compute. Project page: https://www.vision.caltech.edu/psp. Code: https://github.com/rogerioagjr/psp.

### 🤖 AI 总结

**一句话总结**：Diffusion and flow-matching models dominate conditional image generation, yet inference-time scaling for these models is far less developed than for autoregressive language models. Because final quali...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Diffusion, Inference-Time, Scaling, Models, via, Progressive, Seed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21591v1) | [下载PDF](https://arxiv.org/pdf/2607.21591v1.pdf)

---

## [16. GraphVid: Interactive Graph-Controllable Video Generation](https://arxiv.org/abs/2607.21580v1)

**作者**：Vedant Shah, Onkar Susladkar, Tushar Prakash 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-23

### 📄 论文摘要

Controllable video generation remains challenging due to the difficulty of specifying precise multi-object interactions using text prompts or motion-control inputs that primarily constrain pixel movement. In practice, trajectory-based control often requires users to draw accurate tracks for multiple objects, which scales poorly with scene complexity and becomes ambiguous under occlusion or overlap. To enable flexible yet precise multi-subject control, we introduce $\textbf{GraphVid}$, a graph-conditioned image-to-video generation model that enables interactive control through structured interaction graphs. We further curate $\textbf{GraphVid-Bench}$, a large-scale interaction-centric video dataset with structured relational annotations to enable training of interaction-aware video generation models. Despite using substantially less training data and fewer trainable parameters than prior motion-control methods, GraphVid delivers strong controllability and video quality. Compared with Motion-I2V, GraphVid reduces FID by up to 39.9% and FVD by 37.6%, while improving PSNR (9.87=>15.98) and SSIM (0.38=>0.61). Our results highlight the potential of structured semantic interfaces as a powerful paradigm for controllable video generation.

### 🤖 AI 总结

**一句话总结**：Controllable video generation remains challenging due to the difficulty of specifying precise multi-object interactions using text prompts or motion-control inputs that primarily constrain pixel movem...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GraphVid, Interactive, Graph-Controllable, Video, Generation, Controllable, remains, challenging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21580v1) | [下载PDF](https://arxiv.org/pdf/2607.21580v1.pdf)

---

## [17. Synthetic data generation framework for quality control automation in gravure printing](https://arxiv.org/abs/2607.21577v1)

**作者**：Korota Arsène Coulibaly, Mohamed Hamlich, Khalid Hmali 等 4 位作者  
**分类**：cs.CV, cs.AI, cs.LG, eess.IV  
**发布时间**：2026-07-23

### 📄 论文摘要

Quality control in printing, particularly in rotogravure printing, still depends on slow, costly, and subjective manual inspection. Automated surface defect detection is critical for maintaining high-quality standards in rotogravure printing. Deep learning models give prospects for automation. However, training robust deep learning models, such as YOLO or Vision Transformers, is heavily hindered by the extreme scarcity of real-world industrial defects images. To overcome this limitation, this paper introduces a novel synthetic data generation framework tailored for rotogravure printing quality control. The proposed pipeline automatically generates high-fidelity images of specific printing defects (creases, streaks, misregistration, etc.) and outputs corresponding bounding boxes and annotations. To validate the framework, a synthetic dataset of 7533 images was generated and used to train the state-of-the-art object-detection model RFDETR. Experimental results demonstrate that the model trained on our synthetic data achieves a Mean Average Precision (mAP) of 80.9\% on real industrial testing samples. This framework provides a zero-cost, rapid-deployment solution for automating defect inspection in printing lines without requiring massive manual data collection.

### 🤖 AI 总结

**一句话总结**：Quality control in printing, particularly in rotogravure printing, still depends on slow, costly, and subjective manual inspection. Automated surface defect detection is critical for maintaining high-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Synthetic, data, generation, framework, quality, control, automation, gravure

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21577v1) | [下载PDF](https://arxiv.org/pdf/2607.21577v1.pdf)

---

## [18. Scene Parameter Saliency via Differentiable Light Transport](https://arxiv.org/abs/2607.21562v1)

**作者**：Linas Beresna, Eugene Fiume  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-07-23

### 📄 论文摘要

Gradient-based saliency methods reveal which input features most influence a neural network's output, and are a standard tool for model interpretability. We observe that differentiable renderers, which are conventionally used for parameter optimisation, produce an analogous form of saliency: given any scalar metric evaluated on a rendered image, a single reverse-mode differentiation pass yields per-parameter gradients that identify which scene elements most influence the metric. We call these gradient fields metric saliency maps. Unlike neural saliency, which propagates attribution through learned weights, metric saliency propagates through the image formation process itself, including multi-bounce light transport, capturing parameter dependencies that are semi-opaque to manual inspection. We compute metric saliency maps for qualitatively different objectives: psychovisual glare indices, mean scene luminance, and neural perceptual scores. The saliency rankings differ substantially across metrics for the same scene, with parameters that dominate one objective being negligible for another. The saliency map is specific to the metric, not an intrinsic property of the scene. Our results suggest that differentiable renderers produce derivative images that are as informative for scene understanding as the primal images they were designed to generate.

### 🤖 AI 总结

**一句话总结**：Gradient-based saliency methods reveal which input features most influence a neural network's output, and are a standard tool for model interpretability. We observe that differentiable renderers, whic...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Scene, Parameter, Saliency, via, Differentiable, Light, Transport, Gradient-based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21562v1) | [下载PDF](https://arxiv.org/pdf/2607.21562v1.pdf)

---

## [19. Towards Robust Iris Recognition Through Occlusion Identification and Conditional Diffusion-Based Reconstruction](https://arxiv.org/abs/2607.21545v1)

**作者**：Kamrul Hasan, Mylene C. Q. Farias, Oleg V. Komogortsev  
**分类**：cs.CV  
**发布时间**：2026-07-23

### 📄 论文摘要

Iris recognition is a reliable biometric approach that identifies individuals using the distinctive and stable texture of the iris. However, recognition performance can degrade when discriminative iris texture is partially occluded by eyelids, eyelashes, specular reflections, or other acquisition artifacts. Existing approaches often perform recognition directly on degraded samples or rely only on the remaining visible iris region, which may be inadequate when substantial texture is corrupted. To address this limitation, we propose an occlusion-aware iris recognition framework with three sequential modules: occlusion-type identification, diffusion-based reconstruction, and deep-learning-based recognition. First, a residual 2D CNN-based network determines whether an iris image is non-occluded or belongs to one of the controlled occlusion categories. Second, the occluded image, binary mask, and predicted occlusion type condition a denoising diffusion probabilistic model to reconstruct the corrupted region. Finally, VGG19-HPMNet, a modified VGG19 model with horizontal pyramid mapping, extracts discriminative global and part-wise local iris features for recognition. Experiments on the CASIA-Iris-Thousand dataset under a controlled synthetic-occlusion protocol show that the proposed framework improves iris recognition performance by identifying the occlusion type, reconstructing masked regions, and re-evaluating the restored iris samples.

### 🤖 AI 总结

**一句话总结**：Iris recognition is a reliable biometric approach that identifies individuals using the distinctive and stable texture of the iris. However, recognition performance can degrade when discriminative iri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Towards, Robust, Iris, Recognition, Through, Occlusion, Identification, Conditional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21545v1) | [下载PDF](https://arxiv.org/pdf/2607.21545v1.pdf)

---

## [20. ElasticTTT: Prior-Preserving Test-Time Tuning for Video Editing](https://arxiv.org/abs/2607.21529v1)

**作者**：Yueyi Liu, Chi Zhang, Sen Cui 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-23

### 📄 论文摘要

Test-Time Tuning (TTT) on pretrained diffusion models has emerged as a powerful paradigm for video editing. However, there exists a foundational mismatch between the distribution-mapping nature of generative models and the single-point optimization of standard TTT. In this paper, we demonstrate that this mismatch triggers \textit{Prior Collapse}, a degenerate state where the model discards the text conditions and spatial latents, collapsing generations to the source video, or entangling the features of distinct regions. To resolve this, we propose \textbf{ElasticTTT}, a novel framework that preserves the prior generative distribution and rescues generative elasticity. Specifically, we propose \textit{Target Distribution Regularization} to prevent sharp memorization minima, \textit{Contrastive CFG} to guide inference away from source biases, and \textit{Asynchronous Noise Schedule} to preserve unedited regions. Extensive evaluations, supported by theoretical analysis, demonstrate that ElasticTTT successfully preserves the generative prior of the base model, achieving state-of-the-art performance on one-shot video editing.

### 🤖 AI 总结

**一句话总结**：Test-Time Tuning (TTT) on pretrained diffusion models has emerged as a powerful paradigm for video editing. However, there exists a foundational mismatch between the distribution-mapping nature of gen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ElasticTTT, Prior-Preserving, Test-Time, Tuning, Video, Editing, TTT, pretrained

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21529v1) | [下载PDF](https://arxiv.org/pdf/2607.21529v1.pdf)

---

## [21. Boosting Robustness for All-Weather Self-Supervised Depth Estimation in Autonomous Driving](https://arxiv.org/abs/2607.21526v1)

**作者**：Mengshi Qi, Xiaoyang Bi, Xianlin Zhang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-23

### 📄 论文摘要

Self-supervised depth estimation is challenging for safe autonomous driving under various adverse weather conditions due to sensor perception degradation. These challenges arise from two main aspects. Firstly, adverse conditions can distort pixel correspondences and violate the assumptions embedded in the self-supervised loss function, leading to erroneous depth predictions. Secondly, while radar is a widely adopted sensor in adverse weather conditions, the sparse distribution of radar points in the Point of View (POV) poses challenges for self-supervised fusion. To address these issues, we introduce a novel self-training pipeline using unpaired real all-weather data through multi-teacher distillation and robust radar fusion. We propose the Uncertainty-Aware Multi-Teacher Distillation method to generate diverse teacher models with different adverse condition inputs, and then employ uncertainty modeling to weigh the knowledge distillation loss. Additionally, we design the POV-BEV Radar Fusion approach, which leverages camera-pixel ray constraints to establish connections between the camera's Point of View (POV) and the radar's Bird's-Eye View (BEV). This approach enables the utilization of denser radar points, effectively capturing the complementary perspectives of both POV and BEV. Extensive quantitative and qualitative experiments demonstrate the robustness of our proposed method on all-weather datasets, achieving state-of-the-art performance. Our code and models are available at https://github.com/MICLAB-BUPT/RobustDepth.

### 🤖 AI 总结

**一句话总结**：Self-supervised depth estimation is challenging for safe autonomous driving under various adverse weather conditions due to sensor perception degradation. These challenges arise from two main aspects....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Boosting, Robustness, All-Weather, Self-Supervised, Depth, Estimation, Autonomous, Driving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21526v1) | [下载PDF](https://arxiv.org/pdf/2607.21526v1.pdf)

---

## [22. Recurrent Sinusoidal INRs for Efficient High-Fidelity Representation](https://arxiv.org/abs/2607.21485v1)

**作者**：Hyunmin Cho, Jaejun Yoo, Kyong Hwan Jin  
**分类**：cs.CV  
**发布时间**：2026-07-23

### 📄 论文摘要

We study sinusoidal recurrence as an iterative mechanism for harmonic spectral enrichment in implicit neural representations (INRs). Our analysis reveals that sinusoidal activations induce a harmonic line spectrum, providing a spectral account of how recurrent unrolling enriches the effective spectral support. We realize this principle with a shared sinusoidal block that iteratively refines the latent representation. We empirically validate the resulting spectral behavior against feed-forward INRs, non-sinusoidal recurrent variants, and equilibrium-style sinusoidal models. Complementing this analysis, we evaluate the proposed architecture across image and 3D representation tasks. On RGB image benchmarks, our method achieves higher fidelity than feed-forward baselines with fewer parameters and fewer optimization steps, and it further transfers favorably to super-resolution, NeRF, and SDF tasks.

### 🤖 AI 总结

**一句话总结**：We study sinusoidal recurrence as an iterative mechanism for harmonic spectral enrichment in implicit neural representations (INRs). Our analysis reveals that sinusoidal activations induce a harmonic ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Recurrent, Sinusoidal, INRs, Efficient, High-Fidelity, Representation, study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21485v1) | [下载PDF](https://arxiv.org/pdf/2607.21485v1.pdf)

---

## [23. Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window](https://arxiv.org/abs/2607.21471v1)

**作者**：Yukun Shi, Minglun Gong  
**分类**：cs.CV  
**发布时间**：2026-07-23

### 📄 论文摘要

Dynamic-scene reconstruction is almost always evaluated inside the observed time window, yet deployment settings such as AR overlays, robot interaction, and anticipatory planning need the future surface: the geometry at times beyond those captured. No standard benchmark measures this. We introduce FutureSurf, a controlled diagnostic benchmark and dataset for future-time surface reconstruction that trades scene diversity for exact future ground truth and falsification controls. A method trains on the observed first 75% of a sequence; we score its extracted per-frame surface on the held-out future by Chamfer distance, reporting absolute future CD as the primary score and the future/observed gap as a diagnostic. The dataset contains eight analytically defined controlled motions, including three falsification controls, with exact per-frame ground-truth meshes. We also provide a ground-truth-side recoverability oracle. The release includes split files, scoring code, a benchmark card, and Croissant metadata. On the controlled motions, the DG-Mesh backbone leaves a 2.7-4.1$\times$ gap even for futures predictable in principle (four of five recoverable from observed motion by a fixed rule), while the falsification controls behave as designed (the surface-invariant motion shows no gap). Beyond the contributed dataset, the gap persists across six animated DG-Mesh asset scenes and a second backbone, Deformable-3DGS (2.0-6.6$\times$; both share a deformation-MLP temporal model). The benchmark also shows that future rendering quality and future-surface accuracy are statistically decoupled, so the novel-view-synthesis metrics the field reports do not track future geometry. The future error is structured, concentrating where the surface moves. The dataset, evaluation toolkit, and scoring code are available on Hugging Face and GitHub (https://github.com/Ricky-S/futuresurf).

### 🤖 AI 总结

**一句话总结**：Dynamic-scene reconstruction is almost always evaluated inside the observed time window, yet deployment settings such as AR overlays, robot interaction, and anticipatory planning need the future surfa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Future, Rendering, neq$, Surface, Benchmark, Dataset, Dynamic, Reconstruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21471v1) | [下载PDF](https://arxiv.org/pdf/2607.21471v1.pdf)

---

## [24. SPDCN: Strip-based Deformable Convolutional Network for Steel Surface Defect Segmentation](https://arxiv.org/abs/2607.21456v1)

**作者**：Zhongming Liu, Bingbing Jiang, Guangxin Wan 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-23

### 📄 论文摘要

Steel surface defect segmentation is critical for industrial quality inspection, yet existing methods struggle with elongated, anisotropic defects such as cracks and scratches due to the isotropic receptive fields of standard convolutions and rigid sampling grids that cannot adapt to irregular defect boundaries. To address these limitations, we propose Strip-based Predictor for Deformable Convolutional Networks (SPDCN) with two key innovations. The \textbf{Fuzzy-enhanced Multi-scale Context Module (FMCM)} employs group-wise multi-branch convolutions with an intuitionistic fuzzy channel attention mechanism to adaptively capture multi-scale contextual information across varying defect sizes. The \textbf{Adaptive Direction-Aware Deformable Convolution (ADADC)} replaces the conventional offset predictor with decoupled horizontal and vertical strip convolutions, enabling the deformable sampling grid to anisotropically align with the principal orientation of elongated defects. Extensive experiments on public steel surface defect benchmarks demonstrate that SPDCN consistently outperforms state-of-the-art methods, achieving 89.60\% mIoU on NEU-Seg with only 3.54M parameters. The source code is publicly available at https://github.com/DWlzm .

### 🤖 AI 总结

**一句话总结**：Steel surface defect segmentation is critical for industrial quality inspection, yet existing methods struggle with elongated, anisotropic defects such as cracks and scratches due to the isotropic rec...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SPDCN, Strip-based, Deformable, Convolutional, Network, Steel, Surface, Defect

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21456v1) | [下载PDF](https://arxiv.org/pdf/2607.21456v1.pdf)

---

## [25. GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis](https://arxiv.org/abs/2607.21448v1)

**作者**：Jiahao He, Yihua Shao, Zhengkai Zhao 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-23

### 📄 论文摘要

Dynamic scene reconstruction with 3D Gaussian Splatting requires a balance between fine-grained motion modeling, structural stability, and compact representation. Existing per-primitive methods provide flexible local deformation but often suffer from redundant primitive growth, while anchor-based methods improve spatial regularity at the cost of suppressing locally varying motion. To address these issues, we present GrainGS, a dynamic Gaussian framework that combines a hierarchical anchor scaffold with per-Gaussian deformation. A static warm-up stage first establishes a time-invariant canonical representation from observations across all timestamps. During joint training, a stop-gradient operation blocks the deformation-mediated gradient pathway to the canonical positions while preserving their direct refinement through the reconstruction objective. Each Gaussian then predicts independent temporal offsets for position, rotation, and scale, enabling detailed local motion within a structurally constrained scaffold. A canonical-residual appearance decomposition further models frame-dependent photometric changes without forcing them into geometric deformation. Experiments on synthetic monocular and real-world multiview benchmarks show that GrainGS achieves high reconstruction quality, real-time novel view synthesis, and compact storage. Under the synthetic benchmark setting, it reaches an average peak signal-to-noise ratio of 36.98 decibels, renders at 435.6 frames per second, and requires 4.67 megabytes of storage.

### 🤖 AI 总结

**一句话总结**：Dynamic scene reconstruction with 3D Gaussian Splatting requires a balance between fine-grained motion modeling, structural stability, and compact representation. Existing per-primitive methods provid...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GrainGS, Gradient-Decoupled, Gaussian, Splatting, Efficient, Dynamic, Novel, View

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21448v1) | [下载PDF](https://arxiv.org/pdf/2607.21448v1.pdf)

---

## cs.LG

## [26. Beyond Sufficiency: Time Series Explanation with Counterfactual Necessity](https://arxiv.org/abs/2607.21573v1)

**作者**：Hongnan Ma, Yiwei Shi, Mengyue Yang 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-23

### 📄 论文摘要

Faithful explanations of time-series classifiers should identify subsequences that are not only sufficient to preserve a black-box model's prediction, but also necessary for maintaining it. However, existing sufficiency-oriented methods can assign high importance to spurious subsequences that support the prediction without being essential to the model's decision. We introduce \textbf{TimePNS}, a necessity-aware framework for time-series explanation. Inspired by Pearl's counterfactual notion of necessity, TimePNS assesses whether a temporal factor is necessary by intervening on it and measuring whether the original prediction is disrupted. The framework adopts a two-stage design. Stage I learns an identifiable causal generative process together with a sufficiency-oriented explanation mask. Stage II performs counterfactual interventions on temporal factors to derive necessity signals, which supervise a temporal gate that refines the initial explanation by suppressing non-essential components and emphasizing counterfactually necessary ones. Experiments on synthetic and real-world time-series benchmarks show that TimePNS more accurately identifies decision-critical subsequences and consistently improves sufficiency-necessity trade-offs over strong baselines.

### 🤖 AI 总结

**一句话总结**：Faithful explanations of time-series classifiers should identify subsequences that are not only sufficient to preserve a black-box model's prediction, but also necessary for maintaining it. However, e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Sufficiency, Time, Series, Explanation, Counterfactual, Necessity, Faithful

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21573v1) | [下载PDF](https://arxiv.org/pdf/2607.21573v1.pdf)

---

## [27. Zero-Flow Two-Sample Tests](https://arxiv.org/abs/2607.21542v1)

**作者**：Yakun Wang, Leyang Wang, Song Liu 等 4 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-07-23

### 📄 论文摘要

We propose a new approach to two-sample testing for deciding whether two sets of samples are drawn from the same distribution. The test is built on a statistical discrepancy based on the zero-flow criterion, termed zero-flow discrepancy (ZFD). We prove the validity of ZFD and propose a practical testing procedure, termed the zero-flow two-sample test (ZF2ST). The key idea is to learn how samples from the two distributions are locally misaligned and use the resulting directional pattern as evidence of distributional difference. By separating witness learning from hypothesis evaluation, ZF2ST can use flexible neural networks while maintaining valid statistical calibration. We develop both regression-based and power-maximized approaches for learning the witness. Experiments on synthetic and image datasets demonstrate that ZF2ST can achieve strong testing power for structured distributional changes while maintaining well-calibrated type-I error.

### 🤖 AI 总结

**一句话总结**：We propose a new approach to two-sample testing for deciding whether two sets of samples are drawn from the same distribution. The test is built on a statistical discrepancy based on the zero-flow cri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Zero-Flow, Two-Sample, Tests, propose, new, approach, testing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21542v1) | [下载PDF](https://arxiv.org/pdf/2607.21542v1.pdf)

---

## [28. Compact Latent Coordination for Autonomous Vehicles at Unsignalized Intersections](https://arxiv.org/abs/2607.21488v1)

**作者**：Gil Lifshits, Igal Bilik, Gilad Katz  
**分类**：cs.LG, cs.AI, cs.MA, cs.RO  
**发布时间**：2026-07-23

### 📄 论文摘要

Coordinating autonomous vehicles at unsignalized intersections remains a critical challenge for multi-agent reinforcement learning (MARL) systems, which typically struggle with combinatorial action spaces, reliance on privileged information, or rigid agent designs. We propose Master-Agent Proto-plan System (MAPS), a hierarchical deep reinforcement learning (DRL) architecture in which a centralized Master agent generates a compact, continuous embedding, denoted as proto-plan, that encodes a global coordination strategy. Decentralized Worker agents integrate this embedding with local observations to execute vehicle-specific control, decoupling strategic intent from tactical execution and enabling independent optimization of each module.   As a proof-of-concept evaluation of this coordination mechanism, we test MAPS across 72 intersection configurations in HighwayEnv. MAPS achieves collision-free navigation while significantly reducing average travel time, outperforming state-of-the-art baselines. The learned proto-plans further exhibit robust generalization: a system trained with three agents achieves a 94% success rate when deployed zero-shot to five-agent scenarios, confirming that proto-plan-based hierarchical learning provides a promising framework for multi-vehicle coordination.

### 🤖 AI 总结

**一句话总结**：Coordinating autonomous vehicles at unsignalized intersections remains a critical challenge for multi-agent reinforcement learning (MARL) systems, which typically struggle with combinatorial action sp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Compact, Latent, Coordination, Autonomous, Vehicles, Unsignalized, Intersections

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21488v1) | [下载PDF](https://arxiv.org/pdf/2607.21488v1.pdf)

---

## [29. Finite-Sample Coverage Audits for High-Recall Candidate Generation: Certification and Learning-Theoretic Design](https://arxiv.org/abs/2607.21480v1)

**作者**：Martin Anthony, Kaveh Salehzadeh Nobari  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-07-23

### 📄 论文摘要

An initial high-recall stage in an empirical pipeline decides which items pass to later review, labelling, or modelling, and relevant items it misses are lost to every subsequent stage. We study how many audit labels are needed to certify, with finite-sample validity, that this missed relevant mass is small, and our main results characterise the label complexity of this problem. We first show that no procedure using only labels from inside the candidate set can certify any non-trivial bound on the missed mass: the audit must sample the excluded pool, the only region where unrecovered relevant items can lie. We then prove a matching finite-corpus lower bound. Any valid audit that certifies fewer than $m$ missed relevant items with high probability when none are present, even if adaptive and permitted to label the entire included pool, must inspect on the order of $N_0/m$ excluded-pool labels. Excluded-pool auditing is therefore minimax rate-optimal, not merely convenient, for missed-mass certification in the zero-miss regime. Building on this characterisation, we develop an exact finite-sample toolkit, using binomial and hypergeometric inversion rather than asymptotic approximation, that certifies missed mass, converts it to recall through a two-pool design, certifies pre-specified families of nested candidate generators simultaneously, and produces stress-test certificates against declared perturbation mechanisms. These certificates can be paired with observable review burden to select the least burdensome pre-specified candidate generator meeting a missed-mass target. Every guarantee holds under one discipline: the candidate generator, or the pre-specified family from which it is selected, and the audit rule are fixed before the certification labels are examined.

### 🤖 AI 总结

**一句话总结**：An initial high-recall stage in an empirical pipeline decides which items pass to later review, labelling, or modelling, and relevant items it misses are lost to every subsequent stage. We study how m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Finite-Sample, Coverage, Audits, High-Recall, Candidate, Generation, Certification, Learning-Theoretic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21480v1) | [下载PDF](https://arxiv.org/pdf/2607.21480v1.pdf)

---

## [30. KroQuant: Kronecker-Structured Block Transforms for Efficient Post-Training Quantization of Diffusion Transformers](https://arxiv.org/abs/2607.21446v1)

**作者**：Yann Bouquet, Alireza Khodamoradi, Kristof Denolf 等 4 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-07-23

### 📄 论文摘要

Post-training quantization (PTQ) of diffusion transformers (DiTs) to W4A4 severely degrades output quality, because activations entering each linear layer contain outliers that 4-bit formats cannot represent. The standard fix applies an invertible linear transform to the activations and its inverse to the weights before quantizing both. Normalization layers between blocks force this transform to run online at every denoising step, making its inference computation cost the binding design constraint. Existing options trade quantization quality for inference cost: per-channel scaling (SmoothQuant) is computationally cheap but impacts the magnitude of the channels, which can harm quantization accuracy; fixed Hadamard transforms yield better quantization accuracy but require large block sizes that incur a high online cost; learned full-$d$ invertible transforms calibrate best but entail a prohibitive dense $d \times d$ matrix multiplication (GEMM) per layer per step.   We propose KroQuant, a PTQ method that applies a learned Kronecker-structured invertible transform to each 32-element block of the activation, storing less than half the parameters of per-channel scaling. The block-local structure runs as small tensor-core GEMMs, and on an MI350 GPU the KroQuant quantizer kernel is up to $14\%$ faster than the SmoothQuant kernel. Offline LoRaQ weight calibration then absorbs the residual per-weight quantization error. On PixArt-$Σ$, SANA, and FLUX.1-schnell at W4A4 (MXFP4e2), KroQuant produces outputs closer to the FP reference than SVDQuant and LoRaQ on MJHQ-30K and SDCI, while preserving or improving image quality.

### 🤖 AI 总结

**一句话总结**：Post-training quantization (PTQ) of diffusion transformers (DiTs) to W4A4 severely degrades output quality, because activations entering each linear layer contain outliers that 4-bit formats cannot re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, KroQuant, Kronecker-Structured, Block, Transforms, Efficient, Post-Training, Quantization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.21446v1) | [下载PDF](https://arxiv.org/pdf/2607.21446v1.pdf)

---

