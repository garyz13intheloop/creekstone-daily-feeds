# arXiv AI 论文日报 | 2026-09-03

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (5 篇)
- [cs.CV](#csCV) (12 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.CL](#csCL) (7 篇)

---

## cs.AI

## [1. Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885v1)

**作者**：Kelvin Li, Dhruv Pendharkar, Anish Pahilajani 等 9 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-09-02

### 📄 论文摘要

Recent web agents use world models for test-time action selection by sampling candidate actions, predicting the resulting web states, and ranking them with a ranker model or a Process Reward Model (PRM). These world models are typically trained via supervised next-state prediction to generate fixed representations like HTML or AXTree snapshots. However, this objective is misaligned with the downstream ranker, which relies on predicted states being discriminative across candidates to accurately score them. To address this, we introduce predicted-state matching, a training objective where the predicted representation must distinguish the true resulting state from those reached by alternative actions. We train these models using a branching web-agent dataset derived from WebArena Go-Browse trajectories, where every decision point contains multiple alternative actions and their resulting states. Experiments on our held-out predicted-state matching benchmark show that our approach outperforms world models trained with supervised next-state prediction. We further show that our approach improves PRM-style action ranking on WebPRMBench compared with action-only PRMs and PRMs augmented with supervised-next-state world models. Finally, on WebArena-Lite, using our world model for test-time action selection improves end-to-end task success. Our project page is available at: https://dhruvpendharkar.github.io/dwm/.

### 🤖 AI 总结

**一句话总结**：Recent web agents use world models for test-time action selection by sampling candidate actions, predicting the resulting web states, and ranking them with a ranker model or a Process Reward Model (PR...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Discriminative, World, Models, Web, Recent, use, test-time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02885v1) | [下载PDF](https://arxiv.org/pdf/2609.02885v1.pdf)

---

## [2. AI Contextual Measurement for Recovering Individual and Group-Level Effects: Validation Against Survey Measures and an Occupational Application](https://arxiv.org/abs/2609.02821v1)

**作者**：Wenxin Jiang, Xuyang Wang, Yuxiao Wu  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-09-02

### 📄 论文摘要

Researchers increasingly use artificial intelligence to construct measures of social, organizational, and occupational characteristics that are absent from conventional surveys. We propose AICOME, AI COntextual MEasurement, a framework for evaluating whether AI-derived respondent-level measures can recover individual and group-level effects in contextual models. The key idea is that an AI measure constructed at the respondent level can be used to derive its group-level aggregate and its individual deviation, allowing researchers to estimate both between-group and within-group associations rather than treating AI measurement as response prediction alone.   We validate the framework using the 2022 China Family Panel Studies (CFPS), where occupations provide the empirical grouping structure and several job-related survey variables provide validation benchmarks. For computer use, foreign-language use, weekly hours, and management responsibilities, we compare survey measures with AI-derived measures in response-level, model-level, contextual, and boundary-condition validations. The results show that AI contextual measurement can recover much of the contextual-model information contained in observed survey variables when rich respondent and job characteristics are available. Weekly hours provides the strongest validation case, with AI-derived measures reproducing the large negative between- and within-occupation associations with satisfaction observed in CFPS. The framework also identifies clear boundary conditions: performance deteriorates when information is restricted to occupation and basic demographics, and recovery is weaker when several related concepts are treated as simultaneously unobserved. The findings suggest that AICOME is most useful for recovering a limited number of theoretically important constructs from rich existing datasets.

### 🤖 AI 总结

**一句话总结**：Researchers increasingly use artificial intelligence to construct measures of social, organizational, and occupational characteristics that are absent from conventional surveys. We propose AICOME, AI ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Contextual, Measurement, Recovering, Individual, Group-Level, Effects, Validation, Against

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02821v1) | [下载PDF](https://arxiv.org/pdf/2609.02821v1.pdf)

---

## [3. Large Language Models (LLMs) for Telecom Root Cause Analysis (RCA): A Structured Reasoning Framework for Evidence-Grounded Diagnosis](https://arxiv.org/abs/2609.02805v1)

**作者**：Hao Zhou, Mandar Kulkarni, Hao Chen 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-02

### 📄 论文摘要

Root cause analysis (RCA) is a critical task in telecom network operations, but diagnosing performance degradations in modern 5G and emerging 6G networks remains challenging due to complex cross-layer dependencies. While large language models (LLMs) offer promising capabilities for reasoning and knowledge integration, directly applying vanilla LLMs to telecom RCA often leads to hallucination, unstable reasoning, and poor alignment with structured network evidence. This work first reviews the evolution of telecom RCA from rule-based and machine learning (ML) approaches to emerging LLM-enabled techniques, and provides an overview of recent paradigms, including structured reasoning, retrieval-augmented knowledge grounding, agentic orchestration, and verifiable reasoning. Building upon these insights, we propose a structured reasoning framework for LLM-enabled telecom RCA that aligns diagnostic reasoning with telecom-specific evidence and domain knowledge. The proposed approach first organizes heterogeneous network telemetry into canonical contexts, and then enforces decision-path reasoning during diagnosis, and finally generates evidence-grounded explanations for reliable fault identification. Experimental results on two 5G RCA datasets, TeleLogs and TelecomTS, demonstrate that the proposed framework consistently improves diagnostic accuracy and decision consistency compared with baseline techniques. These cross-dataset results highlight the importance of structured reasoning design for practical LLM-based RCA systems in next-generation telecom networks.

### 🤖 AI 总结

**一句话总结**：Root cause analysis (RCA) is a critical task in telecom network operations, but diagnosing performance degradations in modern 5G and emerging 6G networks remains challenging due to complex cross-layer...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Large, Language, Models, Telecom, Root, Cause, Analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02805v1) | [下载PDF](https://arxiv.org/pdf/2609.02805v1.pdf)

---

## [4. SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment](https://arxiv.org/abs/2609.02786v1)

**作者**：Qinghua Mao, Wanying Qu, Dadi Guo 等 11 位作者  
**分类**：cs.AI, cs.CR  
**发布时间**：2026-09-02

### 📄 论文摘要

The performance of LLM-based agents is jointly shaped by the base model and the harness used when interacting with the environment. This exposes them to safety risks in both harmful final responses and multi-step execution trajectories. Existing safety alignment mechanisms often rely on either external harness updates or policy optimization, yet applying either paradigm in isolation fails to bridge runtime control with intrinsic safety. We propose SafeEvolve, an experience-driven self-evolving framework for agent safety alignment. SafeEvolve leverages safety experience from completed on-policy trajectories to drive a continual loop of harness-policy co-evolution. On the harness side, SafeEvolve converts trajectory-level safety evidence into bounded, component-level updates across safety prompt and hierarchical skills, yielding auditable and reversible harness artifacts. On the policy side, SafeEvolve follows a two-stage SFT-RL paradigm, where harness-use SFT bootstraps the policy to actively leverage evolved harness artifacts, and harness-augmented RL further shapes autonomous safety behaviors during multi-step exploration via verifier-decomposed rewards. Through harness-policy co-evolution, SafeEvolve converts safety experience into an evolved runtime harness and improved policy behavior. Experiments on agentic safety benchmarks show that SafeEvolve achieves a stronger safety-utility tradeoff than existing baselines. For Qwen3.5-4B, SafeEvolve achieves a $3\times$ ASR reduction on AgentDojo while improving benign utility from 59.79% to 61.86%.

### 🤖 AI 总结

**一句话总结**：The performance of LLM-based agents is jointly shaped by the base model and the harness used when interacting with the environment. This exposes them to safety risks in both harmful final responses an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SafeEvolve, Harness-Policy, Co-Evolution, Experience, Safety, Alignment, performance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02786v1) | [下载PDF](https://arxiv.org/pdf/2609.02786v1.pdf)

---

## [5. Measurement-Driven Sub-Network Selection for On-Premise Retrieval-Augmented Factory Agents](https://arxiv.org/abs/2609.02760v1)

**作者**：Vasileios Rizeakos, Georgios Paisios, Alexandros Machairas 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-02

### 📄 论文摘要

On-premise assistants can give factory workers conversational access to machine documentation, but models capable of the task rarely fit shop-floor hardware. We show that after structural compression and retrieval-grounded adaptation, model size is no longer a reliable predictor of adapted answer quality: general capability falls almost linearly with parameter count, while judged retrieval-augmented answer quality does not. We therefore treat deployment as a post-adaptation selection problem, committing one sub-network per device on judged answer quality and measured on-device throughput under a configurable general-capability floor and memory budget; rules that optimize size, speed, or quality alone each give up capability or throughput. A weight-shared supernetwork trained with sandwich-style in-place distillation keeps this selection inexpensive. In a manufacturing-manual case study, extraction costs 13.7 percent of the unpruned model's judged quality and retrieval-grounded distillation returns it to within 4.6 percent, recovering two thirds of the loss, and the same assistant runs across three heterogeneous edge tiers at 1.3 to 5 watts standby.

### 🤖 AI 总结

**一句话总结**：On-premise assistants can give factory workers conversational access to machine documentation, but models capable of the task rarely fit shop-floor hardware. We show that after structural compression ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Measurement-Driven, Sub-Network, Selection, On-Premise, Retrieval-Augmented, Factory, assistants

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02760v1) | [下载PDF](https://arxiv.org/pdf/2609.02760v1.pdf)

---

## [6. Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills](https://arxiv.org/abs/2609.02749v1)

**作者**：Jianlyu Chen, Yuyang Hu, Hongjin Qian 等 11 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-09-02

### 📄 论文摘要

Autonomous agents are beginning to carry out machine-learning (ML) research end to end. These agents combine a model backbone with a harness for planning, execution, memory, and verification, but this architecture still leaves domain-specific know-how outside the agent. We call this missing layer operational knowledge, the know-how that separates knowing a method from making it work. That knowledge is not absent from the field. It appears in repositories and papers, but in forms written for human readers and too large to load during a task. Once distilled into compact, verified skills, this knowledge can be reused across tasks rather than rediscovered during each run.   We present DisCo, a skill-powered research agent that creates skills and uses them during research. Its distillation runs in two complementary forms: task-agnostic, condensing the field's widely used repositories into reusable skills, and task-oriented, producing the skills a concrete task calls for. The former, applied across the open ecosystem, yields the AREX-Skill Library, with 5,000+ verified skills distilled from 1,000 widely used ML repositories and organized into 20 areas and 178 capability families. With the GPT-5.5 backbone, research harness, and downstream execution budget held fixed, the skill-equipped research agent scores 134.3% higher on MLE-bench, 34.4% higher on PaperBench, 9.2% higher on FrontierCS, and 14.0% higher on PassNet than the same agent without skills. These gains come from adding distilled operating context under that fixed setup.

### 🤖 AI 总结

**一句话总结**：Autonomous agents are beginning to carry out machine-learning (ML) research end to end. These agents combine a model backbone with a harness for planning, execution, memory, and verification, but this...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Repo-To-Skill, Distilling, Repositories, AI4AI, Skills, Autonomous, beginning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02749v1) | [下载PDF](https://arxiv.org/pdf/2609.02749v1.pdf)

---

## cs.CL

## [7. User Feedback Provides a Unique Signal that LLMs Can not Detect](https://arxiv.org/abs/2609.02859v1)

**作者**：Shachar Don-Yehiya, Leshem Choshen, Omri Abend  
**分类**：cs.CL  
**发布时间**：2026-09-02

### 📄 论文摘要

Harnessing naturally occurring feedback from user interactions offers a promising learning signal for Large Language Models (LLMs). However, recent studies suggest this feedback is inherently noisy and difficult to leverage effectively. We challenge this conception by demonstrating that user feedback is a highly actionable signal for improvement, and that its perceived ineffectiveness stems from a systematic bias in current evaluation paradigms. To isolate the usefulness of feedback, we construct synthetic data with a definitive ground truth, alongside naturalistic data to validate that our findings hold in real-world scenarios. By comparing model revisions generated with and without access to feedback across both settings, we show that feedback-informed revisions resolve targeted issues at significantly higher rates than baseline revisions. Finally, we expose the root of the evaluation bias: when a model successfully fixes an issue exclusively due to feedback, LLM judges frequently fail to identify the genuinely corrected response, systematically preferring inferior baseline outputs instead.

### 🤖 AI 总结

**一句话总结**：Harnessing naturally occurring feedback from user interactions offers a promising learning signal for Large Language Models (LLMs). However, recent studies suggest this feedback is inherently noisy an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, User, Feedback, Provides, Unique, Signal, Can, not

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02859v1) | [下载PDF](https://arxiv.org/pdf/2609.02859v1.pdf)

---

## [8. DiscoSign: Discourse-Aware Text to Sign Language Gloss Translation](https://arxiv.org/abs/2609.02796v1)

**作者**：Vasileios Baltatzis, Mert Inan, Connor Gillis 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-02

### 📄 论文摘要

Sign language processing systems have traditionally operated at the sentence level, ignoring critical discourse phenomena fundamental to sign language comprehension. We introduce DiscoSign, a computational approach for discourse-aware text to sign language gloss translation grounded in linguistic research. We address three key phenomena within our modular Large Language Model (LLM)-based translation framework: (i) spatial coreference resolution, where entities maintain consistent spatial locations throughout discourse; (ii) Question-Answer Clauses (QACs), pseudocleft structures serving specific discourse functions; and (iii) concept-gloss consistency, ensuring stable mappings between English concepts and American Sign Language (ASL) signs. Traditional translation metrics fail to capture discourse-level quality, so we introduce a suite of novel evaluation metrics designed to assess each dimension of discourse coherence addressed by our framework. Experiments on sentence-level and discourse-level datasets show that our approach for discourse-aware processing significantly improves spatial consistency and entity tracking relative to sentence-only translation, while maintaining competitive single-sentence gloss translation quality. Our work establishes the first systematic framework for discourse-level text to sign language gloss translation with corresponding evaluation methodology.

### 🤖 AI 总结

**一句话总结**：Sign language processing systems have traditionally operated at the sentence level, ignoring critical discourse phenomena fundamental to sign language comprehension. We introduce DiscoSign, a computat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DiscoSign, Discourse-Aware, Text, Sign, Language, Gloss, Translation, processing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02796v1) | [下载PDF](https://arxiv.org/pdf/2609.02796v1.pdf)

---

## [9. HyperStyler: Low-resource Authorship Style Transfer via Context-aware Style Navigation and Hypernetworks](https://arxiv.org/abs/2609.02772v1)

**作者**：Jongkyung Shin, Minguk Jeon, Chanwoo Park 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-02

### 📄 论文摘要

Low-resource authorship style transfer (LAST) aims to rewrite text into the style of an arbitrary target author using only a few reference examples while preserving the original meaning. Existing methods often struggle to achieve both high style fidelity and semantic preservation because they compress diverse references into a single static author embedding, which averages out context-dependent stylistic variation, and rely on hidden representations for style control, which entangle style with content. We propose HyperStyler, a novel architecture that decouples LAST into style selection and style realization. Stylo-navigator predicts style coordinates by jointly modeling the source context and target-author references, and Stylo-hypernet realizes them via dynamic parameter modulation instead of hidden-state injection. Our experiments on Reddit, Blog, and News datasets demonstrate that HyperStyler consistently outperforms prior methods including LLM-based approaches and generalizes robustly across domains. Notably, HyperStyler achieves superior performance with as few as 2.4% additional parameters over T5-large, while being over 1.8x faster than LLMs at inference.

### 🤖 AI 总结

**一句话总结**：Low-resource authorship style transfer (LAST) aims to rewrite text into the style of an arbitrary target author using only a few reference examples while preserving the original meaning. Existing meth...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HyperStyler, Low-resource, Authorship, Style, Transfer, via, Context-aware, Navigation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02772v1) | [下载PDF](https://arxiv.org/pdf/2609.02772v1.pdf)

---

## [10. From Reweighting to Rewriting: Unlocking the Intervention Effects of Influential Samples in Training Data Attribution](https://arxiv.org/abs/2609.02771v1)

**作者**：Yuzhang Luo, Chenpeng Wang, Jianhui Chen 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-09-02

### 📄 论文摘要

Training data attribution (TDA) aims to identify training examples that shape model behavior, but its intervention value depends on both which examples are selected and how they are modified. Influence functions (IF) estimate behavioral changes under infinitesimal reweighting, yet IF-selected examples often show limited advantages over random selection under conventional weight-based interventions. This raises the question of whether influential examples lack intervention value or whether reweighting fails to realize their behavioral leverage.We introduce influence-guided response rewriting, which uses IF to identify intervention targets and replaces their responses with behavior-aligned or behavior-opposed supervision while keeping instructions fixed. Across four open-weight LLMs, we compare rewriting and reweighting on the same influence-selected examples using epistemic abstention as our primary testbed. Response rewriting produces stronger, more persistent, and bidirectional behavioral shifts, while reweighting the same examples yields weak and inconsistent effects. Further analyses show that influence-selected examples provide greater rewriting leverage than alternative selectors, with changes remaining concentrated on target-relevant behaviors. The same qualitative contrast extends to safety refusal. These results distinguish the local reweighting effects captured by influence estimates from the broader intervention leverage of the examples they identify, motivating intervention-aware evaluation of TDA methods.

### 🤖 AI 总结

**一句话总结**：Training data attribution (TDA) aims to identify training examples that shape model behavior, but its intervention value depends on both which examples are selected and how they are modified. Influenc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Reweighting, Rewriting, Unlocking, Intervention, Effects, Influential, Samples

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02771v1) | [下载PDF](https://arxiv.org/pdf/2609.02771v1.pdf)

---

## [11. Untangling the Mechanisms of Misleading Context in Medical Question Answering](https://arxiv.org/abs/2609.02754v1)

**作者**：Robin Linzmayer, Noémie Elhadad  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-09-02

### 📄 论文摘要

Large language models now answer medical questions with expert-level performance. However, the context these systems act on can be misleading, and misleading context can corrupt a model's medical judgment. To understand how misleading context corrupts this judgment, we examine the model's susceptibility to the context, disclosure of it, mechanism of corrupted reasoning, and monitorability of the decision. On the medical reasoning subset of MedMisBench, a clinician-reviewed question-answering benchmark of 8,627 questions, we inject two types of misleading context cues, fabricated evidence and a bare assertion. We test three reasoning models, two that expose their full reasoning trace and one frontier model that exposes only its response. All three are more susceptible to the assertion than to the fabricated evidence, adopting the asserted answer 10 to 27 points more often. The misleading cues are disclosed in 81 to 98% of traces but only 7 to 90% of responses, and the assertion is disclosed less often than evidence based cues. Resampling from reasoning traces without disclosure shows the two cues corrupt reasoning differently, evidence entering early and accumulating while the assertion redirects the conclusion near its end. An LLM monitor catches 78% of corrupted decisions at 5% false positives when reading an open model's trace with guidance, against at most 32% from any response. The misleading context that models are most susceptible to is disclosed least, and was caught reliably only from an open reasoning trace, which frontier providers withhold.

### 🤖 AI 总结

**一句话总结**：Large language models now answer medical questions with expert-level performance. However, the context these systems act on can be misleading, and misleading context can corrupt a model's medical judg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Untangling, Mechanisms, Misleading, Context, Medical, Question, Answering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02754v1) | [下载PDF](https://arxiv.org/pdf/2609.02754v1.pdf)

---

## [12. Choosing a PEFT Variant for Per-Patient Dysarthric ASR: A Single-Speaker Case Study on Two ASR Bases](https://arxiv.org/abs/2609.02735v1)

**作者**：Bernard Muller, László Tóth, LaVonne Roberts  
**分类**：cs.CL, cs.SD  
**发布时间**：2026-09-02

### 📄 论文摘要

Per-patient adapters are the preferred production architecture for dysarthric automatic speech recognition (ASR), yet parameter-efficient fine-tuning (PEFT) variants have not been compared in the speaker-dependent, per-patient regime. We present a single-speaker case study comparing seven LoRA-family methods (LoRA, QLoRA, AdaLoRA, DoRA, LoHA, VeRA, VB-LoRA) on two production bases (Whisper-large-v3 with Hungarian fine-tuning, and a multilingual Qwen3-ASR-1.7B checkpoint) for one post-stroke Hungarian male speaker (S1, 409 utterances; severe dysarthria on auditory-perceptual clinical assessment). Attention-projection adapters substantially improve CER on both bases. Across three seeds, a paired bootstrap detects no significant LoRA-DoRA difference (p>0.5; 13.86/13.90 % CER on Whisper, 28.10/28.33 % on Qwen3-ASR), so we adopt the simpler, cheaper LoRA. Real 4-bit (NF4) QLoRA is worse on every seed and both bases (14.56/30.09 % CER) with no memory saving at this scale, and LoHA, VeRA, VB-LoRA and AdaLoRA do not reach the LoRA family, though LoHA still gives an 18.6 % relative CER reduction on Whisper. On the same base, full fine-tuning is more accurate (11.43 % CER), but a 115 MB LoRA that also adapts the feed-forward blocks reaches within 0.66 pp of it at approximately 3.7 % of the per-patient storage. A 6-point enrollment grid shows about 5 min of patient audio captures 45.6 % of the zero-shot-to-30-min CER reduction, with further gains at 10 and 30 min (caveat: one speaker, one language, severe post-stroke dysarthria). Training scripts and recipes will be released, source-available under a research-use licence, on publication.

### 🤖 AI 总结

**一句话总结**：Per-patient adapters are the preferred production architecture for dysarthric automatic speech recognition (ASR), yet parameter-efficient fine-tuning (PEFT) variants have not been compared in the spea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Choosing, PEFT, Variant, Per-Patient, Dysarthric, ASR, Single-Speaker, Case

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02735v1) | [下载PDF](https://arxiv.org/pdf/2609.02735v1.pdf)

---

## [13. CORAL: An LLM-Native Harness for Production Recommender Systems](https://arxiv.org/abs/2609.02730v1)

**作者**：Muhammad Rafay Azhar, Yuhang Zhou, Gilbert Jiang 等 10 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-02

### 📄 论文摘要

Production recommender systems shape what billions of people see, and sustaining their performance requires continual optimization: as content, user behavior, and upstream models shift, the choices governing retrieval, ranking, and serving must be revisited. Traditionally, human engineers test such changes through online experiments--a slow, reactive process limited by engineering effort, leaving parts of the system unrevised as conditions change. Although large language models have been applied to ranking, user modeling, and offline model development, few systems place an agent in a continual closed loop that acts on a live recommender and learns from the measured effects of its decisions. We present CORAL (Constraint-Optimized Recommender via an Agentic Loop), an LLM-native harness that closes this loop: each cycle, the agent observes operating signals, reasons over a memory of past decisions and outcomes, and invokes tools--including a numerical optimizer that keeps changes within a fixed operating budget--to reconfigure the recommender, with measured outcomes informing the next cycle. We formulate this as a partially observed, non-stationary, constrained optimization problem in which the policy improves in context, without parameter updates, from its prior actions. Across two large-scale social platforms, evaluated with A/B experiments, the same harness improves engagement at no additional serving cost on one and reduces serving cost without degrading engagement on the other, spanning the engagement-efficiency frontier. Performance improves as the loop iterates, suggesting that a single agentic loop can automate continual optimization work traditionally performed by human algorithm engineers under explicit guardrails.

### 🤖 AI 总结

**一句话总结**：Production recommender systems shape what billions of people see, and sustaining their performance requires continual optimization: as content, user behavior, and upstream models shift, the choices go...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, CORAL, LLM-Native, Harness, Production, Recommender, Systems, shape

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02730v1) | [下载PDF](https://arxiv.org/pdf/2609.02730v1.pdf)

---

## cs.CV

## [14. SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](https://arxiv.org/abs/2609.02886v1)

**作者**：Junchao Huang, Guian Fang, Shengju Qian 等 18 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-02

### 📄 论文摘要

We introduce SolarWM, a fully open foundation for building interactive video world models from data preparation through long-horizon inference. Training across heterogeneous data sources and video backbones is challenging: datasets differ in temporal scale, camera geometry, visual quality, motion, and captioning styles, while video generators use distinct representations and architectures. Naive data mixing and model-specific implementations therefore produce inconsistent supervision and make results difficult to reproduce and compare. SolarWM addresses this coupling with a reconfigurable multi-source data engine and a backbone-native adaptation framework. The engine converts 1.43 million canonical clips from 10 datasets into a unified, frame-aligned contract covering visual observations, metric camera geometry, captions, quality metadata, selection decisions, and provenance, while decoupling source processing from mixture construction. Under shared camera-conditioning, training, and inference interfaces, we instantiate four 5B--33B models based on Wan2.2, LTX-2.5, and MiniMax-H3 while preserving their native representations and objectives. A unified three-stage recipe combines bidirectional adaptation, teacher-forced autoregressive initialization, and distribution matching distillation. The resulting causal models enable real-time interaction over rollouts ranging from minutes to hours after being trained on only 5s sequences. By releasing the resulting data, pipeline, recipes, weights, and framework, SolarWM provides a reproducible and extensible foundation for interactive world-model research.

### 🤖 AI 总结

**一句话总结**：We introduce SolarWM, a fully open foundation for building interactive video world models from data preparation through long-horizon inference. Training across heterogeneous data sources and video bac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SolarWM, Open, Data, Scalable, Training, Long-Horizon, Video, World

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02886v1) | [下载PDF](https://arxiv.org/pdf/2609.02886v1.pdf)

---

## [15. Thinking in Pictures: A Systematic Benchmark for Reasoning-driven Image Generation](https://arxiv.org/abs/2609.02864v1)

**作者**：Yutong Liu, Nan Huang, Xu Cao 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-02

### 📄 论文摘要

Recent advancements in unified generative models (UGMs) and world simulators have achieved unprecedented results in visual perception and synthesis. However, these models primarily rely on surface-level event alignment, leaving the capacity for high-level visual reasoning underexplored. True visual generative intelligence demands "Reasoning-to-Generation", an ability to infer latent rules from visual inputs and manifest solutions through precise, logically constrained visual outcomes. We introduce RIG-BENCH, a novel comprehensive benchmark that systematically evaluates Reasoning-driven Image Generation (RIG) across four cognitively demanding domains: Concept-based, Transformation-based, Pattern & Structure, and Scenario-based. Featuring 2000 curated samples, RIG-BENCH serves as a rigorous stress test for RIG. Our extensive evaluations of state-of-the-art UGMs and image/video generation models reveal a significant reasoning-generation gap, wherein models frequently produce locally plausible but globally illogical outputs. RIG-BENCH provides a vital diagnostic framework to guide the development of next-generation, logically grounded UGMs and world simulators.

### 🤖 AI 总结

**一句话总结**：Recent advancements in unified generative models (UGMs) and world simulators have achieved unprecedented results in visual perception and synthesis. However, these models primarily rely on surface-lev...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Thinking, Pictures, Systematic, Benchmark, Reasoning-driven, Image, Generation, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02864v1) | [下载PDF](https://arxiv.org/pdf/2609.02864v1.pdf)

---

## [16. PlantC2USeg: Cross-Scale Consistent Pre-Training for Few-Shot Unified Plant Point Cloud Segmentation](https://arxiv.org/abs/2609.02860v1)

**作者**：Yu Tian, Xintong Jiang, Jan Franklin Adamowski 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-02

### 📄 论文摘要

Modern crop breeding demands precise organ-level analysis for trait quantification, making plant point cloud segmentation (PPCS) increasingly important. However, conventional deep learning approaches rely heavily on densely annotated datasets that are labor-intensive to acquire. Unified PPCS adaptation from distribution-shifted examples with minimal additional training remains challenging. To address this, we propose PlantC2USeg, a deep transfer learning framework featuring cross-scale consistency learning to explicitly align features across spatial scales and an information-restricted decoding strategy that prevents reconstruction shortcuts and promotes robust adaptation. The resulting pre-training enables stable few-shot generalization across species and sensing conditions, while unified fine-tuning with inherited thresholds further reduces adaptation overhead. Under full supervision on Soybean3D, PlantC2USeg achieves the highest semantic IoU and instance mWCov among compared methods, at 91.91% and 94.62%. With 20 labeled samples, it leads both metrics at 89.78% and 90.27%; with only 10 samples, it retains the highest mWCov of 83.23% while achieving 83.19% IoU. Across HR3D, 10-shot transfer to tobacco, tomato, and sorghum averages 78.41% IoU and 79.42% mWCov, while 22-shot transfer to SYAU-Maize achieves the highest IoU and mRec at 92.75% and 93.51%. Furthermore, a leading category-averaged mIoU of 85.0% on ShapeNet Part demonstrates the framework's capability to handle diverse shape variations beyond agricultural domains. These results demonstrate that PlantC2USeg reduces overall adaptation effort under distribution shifts, enabling scalable plant phenotyping and transferable 3D representation learning beyond agriculture.

### 🤖 AI 总结

**一句话总结**：Modern crop breeding demands precise organ-level analysis for trait quantification, making plant point cloud segmentation (PPCS) increasingly important. However, conventional deep learning approaches ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PlantC2USeg, Cross-Scale, Consistent, Pre-Training, Few-Shot, Unified, Plant, Point

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02860v1) | [下载PDF](https://arxiv.org/pdf/2609.02860v1.pdf)

---

## [17. MuyBridge: Mobile Human Center-of-Mass Estimation from Monocular Video via Sparse Fusion](https://arxiv.org/abs/2609.02854v1)

**作者**：Aidan Bradshaw, Marco Giordano, David Rode 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-02

### 📄 论文摘要

The 3D center of mass (CoM) is a primary quantity in the biomechanical analysis of sport, rehabilitation, and clinical movement, yet existing 3D pose tracking, mesh recovery, and multi-view triangulation methods either optimize 3D keypoint accuracy without anatomical constraints or carry compute and capture infrastructure too heavy to deploy where CoM tracking is most useful. As a result, the metric CoM remains difficult for coaches and movement analysts to measure from a single camera where athletes train and compete. In this work, we introduce MuyBridge, an on-device system that estimates the athlete's segmental center of mass trajectory from a single phone camera video stream. MuyBridge couples a compact 2D pose network and a distilled single-step monocular depth network through an analytic metric fusion that uses anatomical and physical priors to anchor the metric CoM, requiring no 3D or task-specific supervision. Evaluated on the athletic movements of AthletePose3D (running, track and field, and figure skating), MuyBridge achieves 33-41 mm vertical CoM error and 2.3-6.6% absolute-relative range error (AbsRel) under a one-time calibration, and produces CoM estimates at the 63 FPS pose-estimation rate using asynchronous 2.86 Hz depth updates on iPhone 15. Code is available at: https://github.com/Abradshaw1/Muybridge

### 🤖 AI 总结

**一句话总结**：The 3D center of mass (CoM) is a primary quantity in the biomechanical analysis of sport, rehabilitation, and clinical movement, yet existing 3D pose tracking, mesh recovery, and multi-view triangulat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MuyBridge, Mobile, Human, Center-of-Mass, Estimation, Monocular, Video, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02854v1) | [下载PDF](https://arxiv.org/pdf/2609.02854v1.pdf)

---

## [18. Efficient All-in-One Weather Restoration using Spectral Harmonization](https://arxiv.org/abs/2609.02839v1)

**作者**：Paula Garrido-Mellado, Daniel Feijoo, Yuning Cui 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-02

### 📄 论文摘要

Adverse weather conditions such as rain, haze, and snow significantly degrade image quality, posing challenges for both human perception and physical AI. Existing restoration methods require large computational budgets, struggling to process high-resolution images and handle different degradations. In this paper, we present Frequency Reconstruction via Spectral Harmonization, a novel lightweight all-in-one restoration method that explicitly decomposes feature representations into high- and low-frequency components at each scale of a hierarchical encoder-decoder architecture. By combining spectral decomposition with spatial processing through Fourier-based skip connections, FReSH-IR captures complementary frequency information without sacrificing spatial detail. Our approach achieves similar restoration quality with 80% fewer parameters and operations than transformer-based models. Extensive experiments demonstrate that our method offers a great efficiency-performance trade-off, highlighting its practical applications in constrained-resource systems.

### 🤖 AI 总结

**一句话总结**：Adverse weather conditions such as rain, haze, and snow significantly degrade image quality, posing challenges for both human perception and physical AI. Existing restoration methods require large com...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Efficient, All-in-One, Weather, Restoration, Spectral, Harmonization, Adverse, conditions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02839v1) | [下载PDF](https://arxiv.org/pdf/2609.02839v1.pdf)

---

## [19. Benchmarking RAW and RGB Restoration in Image Signal Processors](https://arxiv.org/abs/2609.02831v1)

**作者**：Zihao Lu, Radu Timofte, Marcos V. Conde  
**分类**：cs.CV  
**发布时间**：2026-09-02

### 📄 论文摘要

Modern cameras transform RAW sensor measurements into sRGB images through an image signal processor (ISP). We benchmark two placements for blind restoration around a fixed ISP: (A) pre-ISP restoration in the RAW domain and (B) post-ISP restoration in the sRGB domain. The benchmark covers four smartphone device groups, two learned ISPs, three degradation regimes--noise, blur, and joint noise and blur--, and several representative RAW and RGB restoration models. Our results show that placement alone does not determine performance. The RAW restoration strategy outperforms the best generic RGB restoration models. However, RGB restoration models trained considering the ISP transformations, achieve the best overall performance. Our novel benchmark demonstrates that the image reconstruction performance strongly depends on the alignment between the restoration model and the target imaging pipeline. We consequently recommend reporting restoration placement and ISP-aware supervision as key experimental factors. Our code is available at https://github.com/mv-lab/AISP

### 🤖 AI 总结

**一句话总结**：Modern cameras transform RAW sensor measurements into sRGB images through an image signal processor (ISP). We benchmark two placements for blind restoration around a fixed ISP: (A) pre-ISP restoration...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Benchmarking, RAW, RGB, Restoration, Image, Signal, Processors, Modern

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02831v1) | [下载PDF](https://arxiv.org/pdf/2609.02831v1.pdf)

---

## [20. GDB-Reward: From Evaluation Metrics to Training Rewards for Graphic Design](https://arxiv.org/abs/2609.02813v1)

**作者**：Adrienne Deganutti, Purvanshi Mehta, Simon Hadfield 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-02

### 📄 论文摘要

Text-to-image models excel at natural image synthesis but struggle with graphic design, where success depends on satisfying precise constraints on typography, layout, color, and visual communication. While prompt optimization offers an attractive alternative to expensive diffusion model fine-tuning, learning prompts for frozen image generators requires informative reward functions despite the entirely non-differentiable generation process. Reinforcement learning does not require differentiable objectives; it requires only scalar rewards capable of ranking candidate outputs. This raises a simple question: can design evaluation metrics themselves become reinforcement learning rewards? Our central contribution is GDB-Reward, a framework that systematically transforms heterogeneous graphic design evaluation metrics into a unified reinforcement learning reward. Experiments demonstrate that GDB-Reward provides an effective optimization objective, substantially improving adherence to the design specification in perceptual quality, rendering fidelity, and spatial accuracy while keeping the image generator entirely frozen. More broadly, our results demonstrate that heterogeneous, non-differentiable evaluation metrics can move beyond passive benchmarking to become effective optimization objectives for reinforcement learning in domains where differentiable supervision is unavailable.

### 🤖 AI 总结

**一句话总结**：Text-to-image models excel at natural image synthesis but struggle with graphic design, where success depends on satisfying precise constraints on typography, layout, color, and visual communication. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GDB-Reward, Evaluation, Metrics, Training, Rewards, Graphic, Design, Text-to-image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02813v1) | [下载PDF](https://arxiv.org/pdf/2609.02813v1.pdf)

---

## [21. AutoCompass: Accurate Visual Localization on Public Maps by Learning from Weak Labels](https://arxiv.org/abs/2609.02798v1)

**作者**：Javier Tirado-Garín, Alan Savio Paul, Shuai Chen 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-02

### 📄 论文摘要

Neural map matchers estimate an image's 3-DoF pose relative to a 2D map. These models are trained on large-scale datasets of geo-referenced images, whose position and heading labels often contain noise that affects the trained models. To address this, we present AutoCompass, a supervision approach for training neural map matchers from inaccurate absolute pose labels. First, we show that heading labels are unnecessary: trained from raw GPS labels, models learn to predict accurate headings, automatically. Second, defining a tolerance region around raw GPS improves positional accuracy. Third, if available, our supervision uses relative poses between training images, obtained via SLAM or SfM, which provide a more accurate training signal. Across driving and egocentric benchmarks, AutoCompass consistently outperforms counterparts trained with the usual strong reliance on absolute pose labels.

### 🤖 AI 总结

**一句话总结**：Neural map matchers estimate an image's 3-DoF pose relative to a 2D map. These models are trained on large-scale datasets of geo-referenced images, whose position and heading labels often contain nois...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AutoCompass, Accurate, Visual, Localization, Public, Maps, Learning, Weak

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02798v1) | [下载PDF](https://arxiv.org/pdf/2609.02798v1.pdf)

---

## [22. Video-Based Palm-Vein Authentication under Challenging Conditions](https://arxiv.org/abs/2609.02776v1)

**作者**：Xiaofeng Yan, Kechen Liu, Abhilash Venkatesh 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-02

### 📄 论文摘要

Palm-vein biometrics are increasingly used for secure, contactless authentication. Yet real-world deployment exposes them to surface noise (sweat, dirt), illumination and motion variation, and temperature-driven changes in vascular visibility, which remain underexplored for lack of data captured under such conditions. To study these effects, we introduce the Columbia University Palm-vein (CUP) dataset, to our knowledge the first public video-based palm-vein dataset. CUP records every palm under four surface conditions (a clean baseline, warm, wet, and dirty) and pairs each subject with physiological and demographic metadata. On it we benchmark twenty-one recognizers spanning static, video, and multi-frame aggregation architectures. Models that verify reliably on clean palms lose most of their accuracy on dirty ones, and the mean equal error rate (EER) roughly quadruples. We recover much of that robustness along both axes of the capture. Temporally, a consensus over the few frames the sensor already returns cancels transient corruption; spatially, a test-time matcher that adds no learned parameters fuses the global cosine with a saliency-steered region-level optimal transport that routes the comparison around corrupted regions. The full design leads on every surface of CUP in EER, TAR@FAR=0.01, and Rank-1, at 4.3M parameters and 3.1 GFLOPs, a fraction of the video models' cost. Attached to four frozen state-of-the-art backbones it cuts their mean EER by 29-37% without retraining, and on four public single-image datasets the regional matching alone still helps. A preliminary audit across ten demographic and physiological traits finds two warm-condition gaps, along body water and gender, that survive multiple-comparison correction. CUP will be released for non-commercial research use at https://github.com/MobileX-CU/CUP_v1 upon publication.

### 🤖 AI 总结

**一句话总结**：Palm-vein biometrics are increasingly used for secure, contactless authentication. Yet real-world deployment exposes them to surface noise (sweat, dirt), illumination and motion variation, and tempera...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Video-Based, Palm-Vein, Authentication, under, Challenging, Conditions, biometrics, increasingly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02776v1) | [下载PDF](https://arxiv.org/pdf/2609.02776v1.pdf)

---

## [23. Multi-Tool Image Editing Attribution in Facial Forgery](https://arxiv.org/abs/2609.02751v1)

**作者**：Sheng Liu, Qiang Sheng, Danding Wang 等 6 位作者  
**分类**：cs.CV, cs.MM  
**发布时间**：2026-09-02

### 📄 论文摘要

As generative AI tools become increasingly powerful and easy to use, people can easily edit portrait images with a prompt, necessitating the task of image editing attribution, which predicts the involved editing tools from the given image. Existing attribution methods hold the single-tool assumption and can only attribute a specific editing tool, but struggle to handle the more complex and increasingly common multi-tool editing scenarios, where artifacts left by different editing tools are composite and overlapped. To address this gap, we explore Multi-Tool Image Editing Attribution (MIEA), which aims to identify multiple editing tools involved in a multi-tool edited facial image. To simulate the real-life editing operations on facial images, we then construct a new dataset, MultiEdit, which contains 500k+ edited facial images and covers six types of editing tools that support face swapping (Deepfake) and various facial enhancements. Inspired by the findings from data analysis, we design DPEC, a multi-tool attribution method that can capture distinguishable, locality-aware editing tool traces from both spatial and frequency domains with the support of an error-based curriculum learning strategy. Experiments show \Method\ outperforms nine methods for facial images edited in at most five steps.

### 🤖 AI 总结

**一句话总结**：As generative AI tools become increasingly powerful and easy to use, people can easily edit portrait images with a prompt, necessitating the task of image editing attribution, which predicts the invol...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, Multi-Tool, Image, Editing, Attribution, Facial, Forgery, generative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02751v1) | [下载PDF](https://arxiv.org/pdf/2609.02751v1.pdf)

---

## [24. Balancing Frequencies and Pixels in Flow Matching](https://arxiv.org/abs/2609.02748v1)

**作者**：Lucas Degeorge, Paul Couairon, Arijit Ghosh 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-02

### 📄 论文摘要

Natural images follow a $1/f^2$ spectral distribution: most signal energy lies in the low spatial frequencies, while the perceptually important structures such as textures and edges occupy sparse high-frequency bands. Pixel-space reconstruction objectives, however, treat all spatial errors uniformly, causing low frequencies to dominate the optimization signal and delaying the learning of fine-scale details. In this work, we identify this objective-level spectral imbalance as a key inefficiency in training pixel-space flow models. To address it, we propose a Focal Log-Frequency Loss (f-loss), a spectrally balanced objective that equalizes the learning signal across frequencies, emphasizing high-frequency components that are otherwise underrepresented in pixel-space objectives. Building on this, we introduce a simple training strategy that combines frequency and pixel supervision: we first emphasize frequency-domain learning early to capture all frequencies, and then transition to standard pixel-space v-loss for spatial refinement. This balancing mitigates the low-frequency bias of pixel losses and aligns the training signal with the evolving needs of the model. Our approach is conceptually simple, requires no architectural changes, and acts as a drop-in replacement for flow matching losses. Across multiple model scales, it accelerates convergence by up to 40% while consistently improving FID and perceptual fidelity. We will release code and models.

### 🤖 AI 总结

**一句话总结**：Natural images follow a $1/f^2$ spectral distribution: most signal energy lies in the low spatial frequencies, while the perceptually important structures such as textures and edges occupy sparse high...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Balancing, Frequencies, Pixels, Flow, Matching, Natural, images, follow

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02748v1) | [下载PDF](https://arxiv.org/pdf/2609.02748v1.pdf)

---

## [25. InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under Unstructured View Sampling](https://arxiv.org/abs/2609.02747v1)

**作者**：Tianheng Lu, Guangyu Wang, Ruqi Huang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-02

### 📄 论文摘要

Achieving truly immersive large-scale scene digitization necessitates consistent and visually pleasing rendering across all possible viewing perspectives. However, collecting multi-view images covering every fine detail of a large-scale scene is prohibitive due to scene complexity, capture cost, negligence, or accessibility constraints. As a result, the sampled views tend to be highly unstructured -- the majority of the scene is well covered yet certain regions inevitably lack sufficient observations. Existing reconstruction based methods are vulnerable to view scarcity while generation based approaches suffer from generalization, controllability, and 3D consistency issues. To address this challenge, we propose InceptionGS, which bootstraps Gaussian splatting by subtly balancing reconstruction and generation. Starting from an initial Gaussian splatting, InceptionGS reasonably rethinks and repairs problematic regions caused by view scarcity while preserving the quality elsewhere, by softly incorporating scene- and view-adaptive generative priors. Extensive experiments on real-world large-scale scenes demonstrate the superiority and broad applicability of our approach in handling unstructured imagery and boosting high-fidelity Gaussian splatting. Please refer to the supplementary video for better visual demonstrations.

### 🤖 AI 总结

**一句话总结**：Achieving truly immersive large-scale scene digitization necessitates consistent and visually pleasing rendering across all possible viewing perspectives. However, collecting multi-view images coverin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：InceptionGS, Generative, Bootstrapping, Large-Scale, Gaussian, Splatting, under, Unstructured

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02747v1) | [下载PDF](https://arxiv.org/pdf/2609.02747v1.pdf)

---

## cs.LG

## [26. A Common Measure of Communication for Speech Brain-Computer Interfaces](https://arxiv.org/abs/2609.02887v1)

**作者**：Dulhan Jayalath, Benjamin Ballyk, Oiwi Parker Jones  
**分类**：cs.LG, q-bio.NC  
**发布时间**：2026-09-02

### 📄 论文摘要

Speech brain-computer interfaces (speech BCIs) translate neural activity into language, offering a path towards restoring speech for people with paralysis and, more broadly, enabling new forms of natural human-computer interaction. Despite this promise, the field lacks a common measure of progress because systems use different datasets, recording methods, types of speech, and vocabularies, so their reported scores are rarely comparable. Underlying this measurement problem are two unresolved questions: (i) what distribution of words should a speech BCI enable a user to communicate, and (ii) how much information from this distribution can a system convey. We address both by deriving open-vocabulary mutual information (OVMI), an information-theoretic quantity that measures the information conveyed by a decoder relative to a reference distribution over the words a user may wish to communicate. This allows capabilities measured under different conditions, such as distinct vocabularies, to be evaluated on a common communication scale. We show that ordinarily reported accuracy, word error rate (WER), and other metrics computed only over the words a system supports can overstate how much of a user's intended speech the system can communicate. We then use OVMI to compare existing systems, expose trade-offs between how much of the user's language a system supports and how accurately it decodes those words, show that these comparisons depend on what the user is expected to communicate, and demonstrate that selecting a vocabulary to maximise OVMI yields up to 16.3% relative improvement in accuracy across three speech domains. OVMI therefore provides the speech BCI community with a principled way to compare heterogeneous systems, improve vocabulary design, and measure progress in the field.

### 🤖 AI 总结

**一句话总结**：Speech brain-computer interfaces (speech BCIs) translate neural activity into language, offering a path towards restoring speech for people with paralysis and, more broadly, enabling new forms of natu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Common, Measure, Communication, Speech, Brain-Computer, Interfaces, BCIs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02887v1) | [下载PDF](https://arxiv.org/pdf/2609.02887v1.pdf)

---

## [27. The Implications of Linguistic Illegibility for LLM Security](https://arxiv.org/abs/2609.02852v1)

**作者**：James Mickens  
**分类**：cs.LG, cs.CR  
**发布时间**：2026-09-02

### 📄 论文摘要

LLMs are trained to generate natural language. However, various strands of evidence indicate that an LLM's externalized linguistic outputs and mechanistically-extracted linguistic features can be an unreliable lens for understanding internal model computation. We introduce the term ``linguistic illegibility'' to broadly refer to scenarios in which an LLM's externalized or mechanistically-probed language artifacts fail to represent how the model actually thinks. We argue that the specter of linguistic illegibility is unavoidable for LLMs whose internal computations are not directly expressed via language, but rather math over activation spaces (with lossy translations between activation spaces and natural language happening at the bookends). If linguistic illegibility is always possible, then security mechanisms that rely on a model's linguistic self-reporting (e.g., chain-of-thought monitoring, constitutional self-critique, activation probing for linguistically-defined feature vectors) can never be completely sound; the model sandbox will always need isolation techniques whose guarantees do not depend on reading a model's linguistic state at all. We argue that observing a model's outputs using taint tracking is a promising approach for an effective sandbox: regardless of how a model linguistically self-reports, a taint tracking policy can define, a priori, various pieces of system state that should never be influenced by model-produced data. We also discuss several additional sandboxing mechanisms (e.g., robust virtualization, third-party auditing of sandboxing configurations) which collectively provide a critical floor beneath linguistic monitoring, and would have mitigated recent sandbox exploits by frontier models.

### 🤖 AI 总结

**一句话总结**：LLMs are trained to generate natural language. However, various strands of evidence indicate that an LLM's externalized linguistic outputs and mechanistically-extracted linguistic features can be an u...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Implications, Linguistic, Illegibility, Security, trained, generate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02852v1) | [下载PDF](https://arxiv.org/pdf/2609.02852v1.pdf)

---

## [28. Post-Training Language Models for Gold-Medal Performance in Coding Competitions](https://arxiv.org/abs/2609.02849v1)

**作者**：Aleksander Ficek, Sean Narenthiran, Mehrzad Samadi 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CL, cs.MA, cs.SE  
**发布时间**：2026-09-02

### 📄 论文摘要

Competitive programming has become a key test of large language model reasoning, with international competitions such as IOI and ICPC representing its most challenging settings. We present an end-to-end specialization pipeline combining large-scale problem curation, synthetic reasoning traces, supervised fine-tuning (SFT), and reinforcement learning (RL). Using 22,000 curated problems, we train Nemotron-3-Nano-CC (30B-A3B) with SFT and RL and Nemotron-3-Ultra-CC (550B-A55B) with SFT alone. We further introduce GenCorrect, a feedback-driven test-time compute strategy that iteratively generates, evaluates, and refines diverse solutions. On IOI 2025, Nano-CC improves from 130 points to 291 after post-training and to 468 with GenCorrect, exceeding the gold threshold of 438.3 while Ultra-CC reaches 502. Guided by these results, we develop a competition-specific Ultra-CC system and evaluate it prospectively during IOI 2026. Under the same time, internet-access, and submission constraints as human contestants, it scores 535.4 out of 600, exceeding both the gold threshold of 361.12 and the top human score of 498.27. To our knowledge, this is the first AI system to outscore the highest-scoring human contestant on an IOI problem set.

### 🤖 AI 总结

**一句话总结**：Competitive programming has become a key test of large language model reasoning, with international competitions such as IOI and ICPC representing its most challenging settings. We present an end-to-e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Post-Training, Language, Models, Gold-Medal, Performance, Coding, Competitions, Competitive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02849v1) | [下载PDF](https://arxiv.org/pdf/2609.02849v1.pdf)

---

## [29. Do Tabular Foundation Models Know Physics? Contamination, Units, and the Deterministic Limit](https://arxiv.org/abs/2609.02766v1)

**作者**：Wassim Tenachi, Yashar Hezaveh, Laurence Perreault Levasseur 等 4 位作者  
**分类**：cs.LG, astro-ph.IM  
**发布时间**：2026-09-02

### 📄 论文摘要

Tabular foundation models (TFMs) learn to fill in tables the way language models fill in text, and tables are arguably the format in which most physical measurement arrives. Did they learn any physics in the process? They are Bayesian by construction, so the question is what their prior contains. We probe it directly, evaluating four of them (TabPFN-3, TabICLv2, TabDPT and Real-TabPFN-2.5) against six baselines on datasets sampled from 316 physical equations, in and out of domain. TFMs dominate, out of the box and after tuning. But we show that their prior can represent neither a noiseless mechanism nor physical units, which is why they interpolate physics without yet being able to act as physical models.

### 🤖 AI 总结

**一句话总结**：Tabular foundation models (TFMs) learn to fill in tables the way language models fill in text, and tables are arguably the format in which most physical measurement arrives. Did they learn any physics...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, Tabular, Foundation, Models, Know, Physics?, Contamination, Units

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02766v1) | [下载PDF](https://arxiv.org/pdf/2609.02766v1.pdf)

---

## [30. LoRA-TSD: Tangent-Space Spectral Descent for LoRA via Muon-Style Updates](https://arxiv.org/abs/2609.02734v1)

**作者**：Dmitrii Andriianov, Andrey Veprikov, Aleksandr Beznosikov  
**分类**：cs.LG  
**发布时间**：2026-09-02

### 📄 论文摘要

Low-rank adaptation (LoRA) is the standard way to fine-tune large models, yet when its two factors are trained independently, the update ignores the geometry of the low-rank weight change it induces. We introduce LoRA-TSD, an optimizer that treats every LoRA step as a tangent vector of the fixed-rank matrix manifold and takes the spectral-norm steepest-descent step of Muon inside that tangent space, mapping the result back to the factors through a retraction native to the LoRA parametrization. The step avoids expensive operations on full weight matrices, and its retraction is up to $2.8\times$ cheaper than the truncated-SVD retraction used by prior manifold methods. We prove that the Frobenius-norm version of our surrogate recovers LoRA-Pro, and we identify the tangent-projected gradient, the Riemannian gradient of the manifold, as the stationarity measure natural to LoRA training and computable from the factor gradients alone. Under this measure we give the first global convergence guarantees for both LoRA-Pro and LoRA-TSD, with rates that drive the factor-gradient norms to zero. Across six commonsense and natural-language-inference benchmarks with Llama-3.2-1B, Llama-3.1-8B and Qwen3-32B, LoRA-TSD outperforms every competing LoRA optimizer and stays robust to the adapter rank. Code is available at https://github.com/brain-lab-research/LoRA-TSD.

### 🤖 AI 总结

**一句话总结**：Low-rank adaptation (LoRA) is the standard way to fine-tune large models, yet when its two factors are trained independently, the update ignores the geometry of the low-rank weight change it induces. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LoRA-TSD, Tangent-Space, Spectral, Descent, LoRA, via, Muon-Style, Updates

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.02734v1) | [下载PDF](https://arxiv.org/pdf/2609.02734v1.pdf)

---

