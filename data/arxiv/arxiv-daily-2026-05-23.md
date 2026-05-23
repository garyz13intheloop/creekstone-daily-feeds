# arXiv AI 论文日报 | 2026-05-23

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (5 篇)
- [cs.LG](#csLG) (14 篇)
- [cs.AI](#csAI) (7 篇)
- [cs.CL](#csCL) (4 篇)

---

## cs.AI

## [1. MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems](https://arxiv.org/abs/2605.22794v1)

**作者**：Qianshu Cai, Yonggang Zhang, Xianzhang Jia 等 7 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-05-21

### 📄 论文摘要

Autonomous agentic systems are largely static after deployment: they do not learn from user interactions, and recurring failures persist until the next human-driven update ships a fix. Self-evolving agents have emerged in response, but all confine evolution to text-mutable artifacts -- skill files, prompt configurations, memory schemas, workflow graphs -- and leave the agent harness untouched. Since routing, hook ordering, state invariants, and dispatch live in code rather than in any text artifact, an entire class of structural failure is physically unreachable from the text layer. We argue that source-level adaptation is a fundamentally more general medium: it is Turing-complete, a strict superset of every text-mutable scope, takes effect deterministically rather than through base-model compliance, and does not erode under long-context drift. We present MOSS, a system that performs self-rewriting at the source level on production agentic substrates. Each evolution is anchored to an automatically curated batch of production-failure evidence and proceeds through a deterministic multi-stage pipeline; code modification is delegated to a pluggable external coding-agent CLI while MOSS retains stage ordering and verdicts. Candidates are verified by replaying the batch against the candidate image in ephemeral trial workers, then promoted via user-consent-gated, in-place container swap with health-probe-gated rollback. On OpenClaw, MOSS lifts a four-task mean grader score from 0.25 to 0.61 in a single cycle without human intervention.

### 🤖 AI 总结

**一句话总结**：Autonomous agentic systems are largely static after deployment: they do not learn from user interactions, and recurring failures persist until the next human-driven update ships a fix. Self-evolving a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, MOSS, Self-Evolution, through, Source-Level, Rewriting, Autonomous, Systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22794v1) | [下载PDF](https://arxiv.org/pdf/2605.22794v1.pdf)

---

## [2. LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems](https://arxiv.org/abs/2605.22786v1)

**作者**：Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas 等 5 位作者  
**分类**：cs.AI, cs.ET, cs.LG, cs.MA  
**发布时间**：2026-05-21

### 📄 论文摘要

Large language model (LLM)-based multi-agent systems increasingly rely on intermediate communication to coordinate complex tasks. While most existing systems communicate through natural language, recent work shows that latent communication, particularly through transformer key-value (KV) caches, can improve efficiency and preserve richer task-relevant information. However, KV caches also encode contextual inputs, intermediate reasoning states, and agent-specific information, creating an opaque channel through which sensitive content may propagate across agents without explicit textual disclosure. To address this, we introduce \textbf{LCGuard} (Latent Communication Guard), a framework for safe KV-based latent communication in multi-agent LLM systems. LCGuard treats shared KV caches as latent working memory and learns representation-level transformations before cache artifacts are transmitted across agents. We formalize representation-level sensitive information leakage operationally through reconstruction: a shared cache artifact is unsafe if an adversarial decoder can recover agent-specific sensitive inputs from it. This leads to an adversarial training formulation in which the adversary learns to reconstruct sensitive inputs, while LCGuard learns transformations that preserve task-relevant semantics and reduce reconstructable information. Empirical evaluations across multiple model families and multi-agent benchmarks show that LCGuard consistently reduces reconstruction-based leakage and attack success rates while maintaining competitive task performance compared to standard KV-sharing baselines.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM)-based multi-agent systems increasingly rely on intermediate communication to coordinate complex tasks. While most existing systems communicate through natural language, rece...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：KV, Multi-Agent, LCGuard, Latent, Communication, Guard, Safe, Sharing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22786v1) | [下载PDF](https://arxiv.org/pdf/2605.22786v1.pdf)

---

## [3. Deep Reinforcement Learning for Flexible Job Shop Scheduling with Random Job Arrivals](https://arxiv.org/abs/2605.22773v1)

**作者**：Yu Tang, Muhammad Zakwan, Efe Balta 等 5 位作者  
**分类**：cs.AI, math.OC  
**发布时间**：2026-05-21

### 📄 论文摘要

The Flexible Job Shop Scheduling Problem (FJSP) is the optimal allocation of a set of jobs to machines. Two primary challenges persist in FJSP: the unpredictable arrival of future jobs and the combinatorial complexity of the problem, rendering it intractable for conventional mixed-integer linear programming solvers. This paper proposes an event-based \gls{DRL} approach to solve FJSP with random job arrivals. Specifically, we employ the Proximal Policy Optimization algorithm and use lightweight Multi-Layer Perceptrons to train the \gls{DRL} agent for minimizing the total completion time of all jobs. We design the state representation to be directly accessible from the environment, and limit the learning agent to selecting from among a set of well-established dispatching rules. Simulations show that our \gls{DRL} approach outperforms any of the individual dispatching rules on datasets with varying heterogeneity and job arrival rates. We benchmark our \gls{DRL} against an arrival-triggered mixed-integer linear programming solution and show that our method achieves good performance especially when the datasets are heterogeneous.

### 🤖 AI 总结

**一句话总结**：The Flexible Job Shop Scheduling Problem (FJSP) is the optimal allocation of a set of jobs to machines. Two primary challenges persist in FJSP: the unpredictable arrival of future jobs and the combina...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Deep, Reinforcement, Learning, Flexible, Job, Shop, Scheduling, Random

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22773v1) | [下载PDF](https://arxiv.org/pdf/2605.22773v1.pdf)

---

## [4. Advancing Mathematics Research with AI-Driven Formal Proof Search](https://arxiv.org/abs/2605.22763v1)

**作者**：George Tsoukalas, Anton Kovsharov, Sergey Shirobokov 等 20 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-21

### 📄 论文摘要

Large language models (LLMs) increasingly excel at mathematical reasoning, but their unreliability limits their utility in mathematics research. A mitigation is using LLMs to generate formal proofs in languages like Lean. We perform the first large-scale evaluation of this method's ability to solve open problems. Our most capable agent autonomously resolved 9 of 353 open Erdős problems at the per-problem cost of a few hundred dollars, proved 44/492 OEIS conjectures, and is being deployed in combinatorics, optimization, graph theory, algebraic geometry, and quantum optics research. A basic agent alternating LLM-based generation with Lean-based verification replicated the Erdős successes but proved costlier on the hardest problems. These findings demonstrate the power of AI-aided formal proof search and shed light on the agent designs that enable it.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) increasingly excel at mathematical reasoning, but their unreliability limits their utility in mathematics research. A mitigation is using LLMs to generate formal proofs in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Advancing, Mathematics, Research, AI-Driven, Formal, Proof, Search, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22763v1) | [下载PDF](https://arxiv.org/pdf/2605.22763v1.pdf)

---

## [5. Towards a General Intelligence and Interface for Wearable Health Data](https://arxiv.org/abs/2605.22759v1)

**作者**：Girish Narayanswamy, Maxwell A. Xu, A. Ali Heydari 等 40 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-21

### 📄 论文摘要

While ubiquitous wearable sensors capture a wealth of behavioral and physiological information, effectively transforming these signals into personalized health insights is challenging. Specifically, converting low-level sensor data into representations capable of characterizing higher-level states is difficult due to high phenotypic diversity and variation in individual baseline health, physiology, and lifestyle factors. Moreover, collecting wearable data paired with health outcome annotations is laborious and expensive, and retrospective annotation remains practically unfeasible, contributing to a scarcity of data with high-quality labels. To overcome these limitations, we propose a foundation model for wearable health that is pretrained on more than one trillion minutes of unlabeled sensor signals drawn from a large cohort of five million participants. We demonstrate that the joint scaling of model capacity and pretraining data volume leads to systematic improvements in performance, as evaluated on a diverse set of 35 health prediction tasks, spanning cardiovascular, metabolic, sleep, and mental health, as well as lifestyle choices and demographic factors. We find that this population scale representation unlocks label-efficient few-shot learning and generative capabilities for robust daily metric estimation. To further leverage this learned representation, we deploy a classroom of LLM agents to autonomously search the space of downstream predictive heads built on the model embeddings, showing broad performance improvements that increase with LLM model capacity. Finally, we show how integrating these downstream predictors into a Personal Health Agent can support model responses that are more relevant, contextually aware, and safe, and we validate this via 1,860 ratings from a cohort of clinicians.

### 🤖 AI 总结

**一句话总结**：While ubiquitous wearable sensors capture a wealth of behavioral and physiological information, effectively transforming these signals into personalized health insights is challenging. Specifically, c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Towards, General, Intelligence, Interface, Wearable, Health, Data, While

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22759v1) | [下载PDF](https://arxiv.org/pdf/2605.22759v1.pdf)

---

## [6. HarnessAPI: A Skill-First Framework for Unified Streaming APIs and MCP Tools](https://arxiv.org/abs/2605.22733v1)

**作者**：Edwin Jose  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-05-21

### 📄 论文摘要

Every Python function deployed as an LLM tool must today exist in two forms: an HTTP endpoint for human-facing clients and CI pipelines, and an MCP tool registration for agent runtimes such as Claude and Cursor. These representations share business logic yet diverge in all the surrounding machinery (routing, validation, serialisation, streaming, and schema maintenance), and they drift apart as the underlying code evolves. We present HarnessAPI, a Python framework that eliminates this duplication by treating a typed skill folder as the single source of truth. From one handler.py plus Pydantic schemas, the framework automatically derives a streaming HTTP endpoint with Server-Sent Events, an interactive OpenAPI/Swagger UI, and a zero-configuration MCP tool, all served from a single process. Dual-mode content negotiation lets the same handler serve SSE-streaming and JSON-returning clients with no handler changes. A dynamic code-generation mechanism ensures Pydantic type annotations propagate correctly to FastMCP's inspection layer, resolving a technical limitation that prevents naive closure-based registration. Measured across six representative skills using cloc, HarnessAPI reduces framework-facing boilerplate by 74% compared with a manually maintained dual-stack implementation (FastAPI server + FastMCP server). HarnessAPI subclasses FastAPI, inheriting its full middleware, dependency-injection, and deployment ecosystem. It is available at https://github.com/edwinjosechittilappilly/harnessapi and on PyPI (pip install harnessapi)

### 🤖 AI 总结

**一句话总结**：Every Python function deployed as an LLM tool must today exist in two forms: an HTTP endpoint for human-facing clients and CI pipelines, and an MCP tool registration for agent runtimes such as Claude ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HarnessAPI, Skill-First, Framework, Unified, Streaming, APIs, MCP, Tools

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22733v1) | [下载PDF](https://arxiv.org/pdf/2605.22733v1.pdf)

---

## [7. Beyond Acoustic Emotion Recognition: Multimodal Pathos Analysis in Political Speech Using LLM-Based and Acoustic Emotion Models](https://arxiv.org/abs/2605.22732v1)

**作者**：Juergen Dietrich  
**分类**：cs.AI, cs.CL, cs.HC, cs.SD, eess.AS  
**发布时间**：2026-05-21

### 📄 论文摘要

We investigate whether acoustic emotion recognition models can serve as proxies for the Pathos dimension in political speech analysis, as operationalised by the TRUST multi-agent large language model (LLM) pipeline. Using a Bundestag plenary speech by Felix Banaszak (51 segments, 245 s) as a case study, we compare three analysis modalities: (1) emotion2vec_plus_large, an acoustic speech emotion recognition (SER) model whose continuous Arousal and Valence values are derived via post-hoc Russell Circumplex projection; (2) Gemini 2.5 Flash, an LLM analysing the full speech audio together with its transcript in an open-ended, context-aware fashion; and (3) TRUST-Pathos scores from a three-advocate LLM supervisor ensemble. Spearman rank correlations reveal that Gemini Valence correlates strongly with TRUST-Pathos (rho = +0.664, p < 0.001), whereas emotion2vec Valence does not (rho = +0.097, p = 0.499). We further demonstrate, via a systematic quality evaluation of the Berlin Database of Emotional Speech (EMO-DB) using Gemini in an open-ended annotation paradigm, that standard SER benchmark corpora suffer from acted speech, cultural bias, and category incompatibility. Our results suggest that LLM-based multimodal analysis captures semantically defined political emotion substantially better than acoustic models alone, while acoustic features remain informative for low-level Arousal estimation. Future work will extend this approach to video-based analysis incorporating facial expression and gaze.

### 🤖 AI 总结

**一句话总结**：We investigate whether acoustic emotion recognition models can serve as proxies for the Pathos dimension in political speech analysis, as operationalised by the TRUST multi-agent large language model ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Acoustic, Emotion, Recognition, Multimodal, Pathos, Analysis, Political

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22732v1) | [下载PDF](https://arxiv.org/pdf/2605.22732v1.pdf)

---

## cs.CL

## [8. Evaluating Commercial AI Chatbots as News Intermediaries](https://arxiv.org/abs/2605.22785v1)

**作者**：Mirac Suzgun, Emily Shen, Federico Bianchi 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-21

### 📄 论文摘要

AI chatbots are rapidly shaping how people encounter the news, yet no prior study has systematically measured how accurately these systems, with their proprietary search integrations and retrieval-synthesis pipelines, handle emerging facts across languages and regions. We present a 14-day (February 9-22, 2026) evaluation of six AI chatbots (Gemini 3 Flash and Pro, Grok 4, Claude 4.5 Sonnet, GPT-5 and GPT-4o mini) on 2,100 factual questions derived from same-day BBC News reporting across six regional services (US & Canada, Arabic, Afrique, Hindi, Russian, Turkish). The best systems achieve over 90% multiple-choice accuracy on questions about events reported hours earlier. The same systems, however, lose 11-13% under free-response evaluation, and 16-17% across the cohort. We further characterize three failure patterns. First, every model achieves its lowest accuracy on Hindi (79% vs. 89-91% elsewhere) and citations indicate an Anglophone retrieval bias (e.g., models answering Hindi queries cite English Wikipedia more than any Hindi outlet). Second, retrieval, not reasoning, failures drive over 70% of all errors. When models retrieve a correct source, they often extract the correct answer; the problem is to land on the right source in the first place. Third, models achieving 88-96% accuracy on well-formed questions drop to 19-70% when questions contain subtle false premises, with the most vulnerable model accepting fabricated facts 64% of the time. We also identify a detection-accuracy paradox: the best false-premise detector ranks second in adversarial accuracy (abstention rate), while a weaker detector ranks first, showing that premise detection and answer recovery are partially independent capabilities. Overall, these suggest that high accuracy can mask systematic regional inequity, near-total dependence on retrieval infrastructure, and vulnerability to imperfect queries real users pose.

### 🤖 AI 总结

**一句话总结**：AI chatbots are rapidly shaping how people encounter the news, yet no prior study has systematically measured how accurately these systems, with their proprietary search integrations and retrieval-syn...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Evaluating, Commercial, Chatbots, News, Intermediaries, rapidly, shaping

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22785v1) | [下载PDF](https://arxiv.org/pdf/2605.22785v1.pdf)

---

## [9. Reducing Political Manipulation with Consistency Training](https://arxiv.org/abs/2605.22771v1)

**作者**：Long Phan, Devin Kim, Alexander Pan 等 6 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-05-21

### 📄 论文摘要

Large language models (LLMs) exhibit systematic political bias across a variety of sensitive contexts. We find that LLMs handle counterpart topics from opposing political sides asymmetrically. We refer to this phenomenon as covert political bias and identify 7 categories of techniques through which it operates. We propose two metrics for covert bias: Sentiment Consistency measures symmetry in rhetoric and framing across paired political prompts; Helpfulness Consistency measures symmetric depth and engagement. To reduce both types of covert bias, we introduce Political Consistency Training (PCT), an RL training method with two complementary paradigms: Sentiment Consistency Training and Helpfulness Consistency Training. We show that PCT preserves overall helpfulness, substantially reduces covert political bias, and generalizes to held-out benchmarks. We release our work at https://political-manipulation.ai

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) exhibit systematic political bias across a variety of sensitive contexts. We find that LLMs handle counterpart topics from opposing political sides asymmetrically. We refe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Reducing, Political, Manipulation, Consistency, Training, Large, language, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22771v1) | [下载PDF](https://arxiv.org/pdf/2605.22771v1.pdf)

---

## [10. Understanding Data Temporality Impact on Large Language Models Pre-training](https://arxiv.org/abs/2605.22769v1)

**作者**：Pilchen Hippolyte, Fabre Romain, Signe Talla Franck 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-05-21

### 📄 论文摘要

Large language models (LLMs) are typically trained on shuffled corpora, yielding models whose knowledge is frozen at train time and whose temporal grounding remains poorly understood. In this work, we study the impact of pre-training dynamics on the acquisition of time-sensitive factual knowledge, focusing specifically on data ordering. Our main contributions are twofold. First, we introduce a comprehensive benchmark of over 7,000 temporally grounded questions and an evaluation protocol that enables analysis of whether models correctly associate facts with their corresponding time periods. Second, we pretrain 6B-parameter models on temporally ordered Common Crawl snapshots and compare them against standard shuffled pre-training. Our results show that sequentially trained models match shuffled baselines on general language understanding and common knowledge while consistently exhibiting more up-to-date and temporally precise knowledge. Temporally ordered pre-training yields improved factual freshness, while shuffled pre-training peaks on older data, possibly due to increased factual repetition. These findings, along with the release of our code at https://github.com/kyutai-labs/kairos , checkpoints, and datasets at https://huggingface.co/collections/kyutai/kairos provide a foundation for future research on continual learning for LLMs.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are typically trained on shuffled corpora, yielding models whose knowledge is frozen at train time and whose temporal grounding remains poorly understood. In this work, we...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Understanding, Data, Temporality, Impact, Large, Language, Models, Pre-training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22769v1) | [下载PDF](https://arxiv.org/pdf/2605.22769v1.pdf)

---

## [11. ChronoMedKG: A Temporally-Grounded Biomedical Knowledge Graph and Benchmark for Clinical Reasoning](https://arxiv.org/abs/2605.22734v1)

**作者**：Md Shamim Ahmed, Farzaneh Firoozbakht, Lukas Galke Poech 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-21

### 📄 论文摘要

Biomedical knowledge graphs (KGs) treat disease associations as static facts, but temporal information is crucial for clinical reasoning, e.g., a symptom diagnostic of one disease at age 3 may imply a different disease at age 13. Existing KGs such as PrimeKG, Hetionet, and iKraph do not encode when a finding becomes clinically relevant over the course of a disease. This limits their usefulness for longitudinal clinical reasoning and retrieval augmentation.   We introduce ChronoMedKG, a temporal biomedical knowledge graph that contains 460,497 evidence-linked triples (filtered from 13M raw extractions) covering 13,431 diseases. Each association is tied to temporal components like onset window or progression stage, which are backed by PMID-traceable evidence and a multi-signal credibility score. The graph is constructed through a disease-autonomous multi-agent pipeline in which multiple frontier LLMs independently extract knowledge from PubMed and PMC literature. Only those relations are kept that are supported by multi-model consensus, survive credibility filtering, as well as ontology alignment.   ChronoMedKG scored 92.7% agreement against Orphadata and adds temporal grounding for 6,250 diseases absent from HPOA, Orphadata, and Phenopackets, including 1,657 Orphanet-coded rare diseases. We further introduce ChronoTQA, a benchmark of 3,341 questions across eight task types (six temporal plus two static controls), with a 12-question supplementary probe. Frontier LLMs lose roughly 30 points moving from static to temporal questions; ChronoMedKG retrieval rescues 47-65% of their long-tail failures, against 17-29% for HPOA-RAG. As such, ChronoMedKG provides a crucial temporal axis for retrieval-augmented clinical systems that was previously absent.

### 🤖 AI 总结

**一句话总结**：Biomedical knowledge graphs (KGs) treat disease associations as static facts, but temporal information is crucial for clinical reasoning, e.g., a symptom diagnostic of one disease at age 3 may imply a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ChronoMedKG, Temporally-Grounded, Biomedical, Knowledge, Graph, Benchmark, Clinical, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22734v1) | [下载PDF](https://arxiv.org/pdf/2605.22734v1.pdf)

---

## cs.CV

## [12. Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness in Video-LLMs](https://arxiv.org/abs/2605.22823v1)

**作者**：Jongseo Lee, Hyuntak Lee, Sunghun Kim 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-21

### 📄 论文摘要

Video Large Language Models (Video-LLMs) have made rapid progress on temporal video understanding, yet many fail at a basic perceptual primitive: signed image-plane motion direction. On simple videos of a single object moving left, right, up, or down, most Video-LLMs perform near chance, with above-chance cases largely attributable to prediction biases rather than genuine direction understanding. We call this failure directional motion blindness. We localize the failure by tracing motion direction information through the Video-LLM pipeline. Motion direction remains linearly accessible from the vision encoder, projector, and LLM hidden states, but the readout fails to bind this signal to the correct verbal answer option, revealing a direction binding gap. Although synthetic motion direction instruction tuning reduces this gap on the source domain, motion direction concept vector analysis shows that visual complexity weakens the signal magnitude and limits out-of-domain generalization. We introduce MoDirect, a dataset family for motion direction instruction tuning and evaluation, and DeltaDirect, a diagnosis-driven, projector-level objective that predicts normalized 2-D motion vectors from adjacent-frame feature deltas. On MoDirect-SynBench, instruction tuning with DeltaDirect improves motion direction accuracy from 25.9% to 85.4%. On MoDirect-RealBench, DeltaDirect improves real-world motion direction accuracy by 21.9 points over the vanilla baseline without real-world tuning data, while preserving standard video-understanding performance. Code: https://github.com/KHU-VLL/DeltaDirect

### 🤖 AI 总结

**一句话总结**：Video Large Language Models (Video-LLMs) have made rapid progress on temporal video understanding, yet many fail at a basic perceptual primitive: signed image-plane motion direction. On simple videos ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：It, Which, Way, Did, Move?, Diagnosing, Overcoming, Directional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22823v1) | [下载PDF](https://arxiv.org/pdf/2605.22823v1.pdf)

---

## [13. MotiMotion: Motion-Controlled Video Generation with Visual Reasoning](https://arxiv.org/abs/2605.22818v1)

**作者**：Lee Hsin-Ying, Hanwen Jiang, Yiqun Mei 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-21

### 📄 论文摘要

Current motion-controlled image-to-video generation models rigidly follow user-provided trajectories that are often sparse, imprecise, and causally incomplete. Such reliance often yields unnatural or implausible outcomes, especially by missing secondary causal consequences. To address this, we introduce MotiMotion, a novel framework that reformulates motion control as a reasoning-then-generation problem. To encourage causally grounded and commonsense-consistent interactions, we leverage a training-free vision-language reasoner to refine image-space coordinates of primary trajectories and to hallucinate plausible secondary motions. To further improve motion naturalness, we propose a confidence-aware control scheme that modulates guidance strength, enabling the model to closely follow high-confidence plans while correcting artifacts under low-confidence inputs with its internal generative priors. To support systematic evaluation, we curate a new image-to-video benchmark, MotiBench, consisting of interaction-centric scenes where new events are triggered by motion. Both VLM-based evaluation and a human study on MotiBench demonstrate that MotiMotion produces videos with more plausible object behaviors and interaction, and is preferred over existing approaches.

### 🤖 AI 总结

**一句话总结**：Current motion-controlled image-to-video generation models rigidly follow user-provided trajectories that are often sparse, imprecise, and causally incomplete. Such reliance often yields unnatural or ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MotiMotion, Motion-Controlled, Video, Generation, Visual, Reasoning, Current, image-to-video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22818v1) | [下载PDF](https://arxiv.org/pdf/2605.22818v1.pdf)

---

## [14. Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving](https://arxiv.org/abs/2605.22809v1)

**作者**：Jiahao Wang, Bo Sun, Yijing Bai 等 15 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-21

### 📄 论文摘要

Robust training and validation of Autonomous Driving Systems (ADS) require massive, diverse datasets. Proprietary data collected by Autonomous Vehicle (AV) fleets, while high-fidelity, are limited in scale, diversity of sensor configurations, as well as geographic and long-tail-behavioral coverage. In contrast, in-the-wild data from sources like dashcams offers immense scale and diversity, capturing critical long-tail scenarios and novel environments. However, this unstructured, in-the-wild video data is incompatible with ADS expecting structured, multi-modal sensor inputs for validation and training. To bridge this data gap, we propose Sensor2Sensor, a novel generative modeling paradigm that translates in-the-wild monocular dashcam videos into a high-fidelity, multi-modal sensor suite (AV logs) comprising multi-view camera images and LiDAR point clouds. A core challenge is the lack of paired training data. We address this by converting real AV logs into dashcam-style videos via 4D Gaussian Splatting (4DGS) reconstruction and novel-view rendering. Sensor2Sensor then utilizes a diffusion architecture to perform the generative conversion. We perform comprehensive quantitative evaluations on the fidelity and realism of the generated sensor data. We demonstrate Sensor2Sensor's practical utility by converting challenging in-the-wild internet and dashcam footage into realistic, multi-modal data formats, further unlocking vast external data sources for AV development.

### 🤖 AI 总结

**一句话总结**：Robust training and validation of Autonomous Driving Systems (ADS) require massive, diverse datasets. Proprietary data collected by Autonomous Vehicle (AV) fleets, while high-fidelity, are limited in ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sensor2Sensor, Cross-Embodiment, Sensor, Conversion, Autonomous, Driving, Robust, training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22809v1) | [下载PDF](https://arxiv.org/pdf/2605.22809v1.pdf)

---

## [15. Synthetic Data Alone is Enough? Rethinking Data Scarcity in Pediatric Rare Disease Recognition](https://arxiv.org/abs/2605.22767v1)

**作者**：Ganlin Feng, Yuxi Long, Erin Lou 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-21

### 📄 论文摘要

Children with rare genetic diseases often exhibit distinctive facial phenotypes, yet developing computer vision systems for early diagnosis remains challenging due to extreme data scarcity, privacy constraints, and limited data sharing in pediatric settings. These challenges not only hinder automated diagnosis but also restrict the availability of visual resources for clinical genetic counseling. While prior work has shown that synthetic data can augment real datasets and preserve phenotype-level semantics, it remains unclear whether synthetic data alone is sufficient for learning in ultra-low-resource pediatric settings. In this work, we study the synthetic-only regime for pediatric rare disease recognition. Under a controlled experimental setup, models are trained exclusively on phenotype-aware synthetic facial images at increasing scales. We find that synthetic-only training achieves performance comparable to real-data-only baselines at sufficient scale across multiple backbones, suggesting that high-fidelity synthetic data can approximate clinically meaningful distributions. These findings together further enable the use of synthetic pediatric facial images as privacy-preserving resources for genetic education and counseling, supporting clinician training and patient communication. Our results highlight the potential of computer vision to improve data efficiency and expand accessible visual tools in children's healthcare.

### 🤖 AI 总结

**一句话总结**：Children with rare genetic diseases often exhibit distinctive facial phenotypes, yet developing computer vision systems for early diagnosis remains challenging due to extreme data scarcity, privacy co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Synthetic, Data, Alone, Enough?, Rethinking, Scarcity, Pediatric, Rare

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22767v1) | [下载PDF](https://arxiv.org/pdf/2605.22767v1.pdf)

---

## [16. Spectral Tail Auxiliary Learning for AI-Generated Image Detection](https://arxiv.org/abs/2605.22751v1)

**作者**：Xingyi Li, Jiahui Zhang, Yiheng Li 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-21

### 📄 论文摘要

As generative image models evolve rapidly, the perceptual gap between generated and real images continues to narrow, making AI-generated image detection increasingly challenging. Many existing methods exploit frequency-domain cues for detection, typically described as frequency-domain artifacts or high-frequency discrepancies. However, the specific and recurring spectral regularities remain insufficiently understood and characterized. In this paper, we systematically analyze the one-dimensional radial log-power spectra of real and generated images. We find that generated images do not necessarily exhibit higher or lower energy across the entire spectrum or high-band range. Instead, their spectra deviate from the power-law decay and show an anomalous uplift in the ultra-high-frequency tail. We term this phenomenon spectral tail uplift. We further attribute this phenomenon to nonlinear harmonic accumulation in trained generative models, suggesting that it can serve as a structural cue across generative architectures. Based on this observation, we propose Spectral Tail Auxiliary Learning (STAL), a frequency-domain auxiliary supervision framework for generalizable AI-generated image detection. STAL transfers spectral-tail cues from a tail-aware frequency teacher to a spatial detector during training, while all frequency-domain modules are discarded at inference time. Consequently, STAL introduces no inference overhead. Extensive experiments on 9 public datasets show that STAL achieves strong generalization and stability across generators, data distributions, and real-world scenarios.

### 🤖 AI 总结

**一句话总结**：As generative image models evolve rapidly, the perceptual gap between generated and real images continues to narrow, making AI-generated image detection increasingly challenging. Many existing methods...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, Spectral, Tail, Auxiliary, Learning, AI-Generated, Image, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22751v1) | [下载PDF](https://arxiv.org/pdf/2605.22751v1.pdf)

---

## cs.LG

## [17. Integrable Elasticity via Neural Demand Potentials](https://arxiv.org/abs/2605.22820v1)

**作者**：Carlos Heredia, Daniel Roncel  
**分类**：cs.LG  
**发布时间**：2026-05-21

### 📄 论文摘要

We propose the Integrable Context-Dependent Demand Network (ICDN), a demand-first neural model for multiproduct retail demand. The model learns log-demand as a smooth, context-conditioned function of log-prices, allowing elasticities to be derived exactly from the learned demand surface. On the Dominick's beer dataset, ICDN improves out-of-sample generalization over a directed log-log benchmark and yields more stable, economically plausible elasticity estimates, especially for weakly identified cross-price effects.

### 🤖 AI 总结

**一句话总结**：We propose the Integrable Context-Dependent Demand Network (ICDN), a demand-first neural model for multiproduct retail demand. The model learns log-demand as a smooth, context-conditioned function of ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Integrable, Elasticity, via, Neural, Demand, Potentials, propose

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22820v1) | [下载PDF](https://arxiv.org/pdf/2605.22820v1.pdf)

---

## [18. Vector Policy Optimization: Training for Diversity Improves Test-Time Search](https://arxiv.org/abs/2605.22817v1)

**作者**：Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld 等 9 位作者  
**分类**：cs.LG, cs.AI, cs.CL, cs.NE  
**发布时间**：2026-05-21

### 📄 论文摘要

Language models must now generalize out of the box to novel environments and work inside inference-scaling search procedures, such as AlphaEvolve, that select rollouts with a variety of task-specific reward functions. Unfortunately, the standard paradigm of LLM post-training optimizes a pre-specified scalar reward, often leading current LLMs to produce low-entropy response distributions and thus to struggle at displaying the diversity that inference-time search will require. We propose Vector Policy Optimization (VPO), an RL algorithm that explicitly trains policies to anticipate diverse downstream reward functions and to produce diverse solutions. VPO exploits that rewards are often vector-valued in practice, like per-test-case correctness in code generation or, say, multiple different user personas or reward models. VPO is essentially a drop-in replacement for the GRPO advantage estimator, but it trains the LLM to output a set of solutions where individual solutions specialize to different trade-offs in the vector reward space. Across four tasks, VPO matches or beats the strongest scalar RL baselines on test-time search (e.g. pass@k and best@k), with the gap widening as the search budget grows. For evolutionary search, VPO models unlock problems that GRPO models cannot solve at all. As test-time search becomes more standardized, optimizing for diversity may need to become the default post-training objective.

### 🤖 AI 总结

**一句话总结**：Language models must now generalize out of the box to novel environments and work inside inference-scaling search procedures, such as AlphaEvolve, that select rollouts with a variety of task-specific ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Vector, Policy, Optimization, Training, Diversity, Improves, Test-Time, Search

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22817v1) | [下载PDF](https://arxiv.org/pdf/2605.22817v1.pdf)

---

## [19. Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration](https://arxiv.org/abs/2605.22814v1)

**作者**：Lily Goli, Justin Kerr, Daniele Reda 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-21

### 📄 论文摘要

Exploration is a prerequisite for learning useful behaviors in sparse-reward, long-horizon tasks, particularly within 3D environments. Curiosity-driven reinforcement learning addresses this via intrinsic rewards derived from the mismatch between the agent's predictive model of the world and reality. However, translating this intrinsic motivation to complex, photorealistic environments remains difficult, as agents can become trapped in local loops and receive fresh rewards for revisiting forgotten states. In this work, we demonstrate that this failure stems from a lack of spatial persistence and episodic context. We show that effective curiosity requires a model of the world that is persistent and continuously updated, paired with an agent that maintains an episodic trajectory history to navigate toward novel regions. We achieve this using an online 3D reconstruction as a persistent model of the world, while the agent policy is parameterized as a sequence model over RGB observations to maintain episodic context. This design enables effective exploration during training while allowing the agent to navigate using solely RGB frames at deployment. Trained purely via curiosity on HM3D, our agent outperforms RL-based active mapping baselines and generalizes zero-shot to Gibson and AI-generated worlds. Our end-to-end policy enables efficient adaptation to downstream tasks, such as apple picking and image-goal navigation, outperforming from-scratch baselines. Please see video results at https://recuriosity.github.io/.

### 🤖 AI 总结

**一句话总结**：Exploration is a prerequisite for learning useful behaviors in sparse-reward, long-horizon tasks, particularly within 3D environments. Curiosity-driven reinforcement learning addresses this via intrin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：be, 3D, Remember, Curious, Episodic, Context, Persistent, Worlds

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22814v1) | [下载PDF](https://arxiv.org/pdf/2605.22814v1.pdf)

---

## [20. The Matching Principle: A Geometric Theory of Loss Functions for Nuisance-Robust Representation Learning](https://arxiv.org/abs/2605.22800v1)

**作者**：Vishal Rajput  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-05-21

### 📄 论文摘要

Robustness, domain adaptation, photometric and occlusion invariance, compositional generalisation, temporal robustness, alignment safety, and classical anisotropic regularisation are usually treated as separate problems with separate method families. This paper argues that much of their shared structure is one statistical problem: estimate the covariance of label-preserving deployment nuisance, then regularise the encoder Jacobian along a matrix whose range covers that covariance (the matching principle). CORAL, adversarial training, IRM, augmentation, metric learning, Jacobian penalties, and alignment-style constraints are different estimators of that object, not independent robustness tricks.   In the linear-Gaussian model we prove closed-form optimality (Theorem A), including cube-root water-filling within the matched range; necessity of range coverage for quadratic Jacobian penalties (Theorem G); the same range dichotomy at deep global minima; and two falsification controls (Lemma C; Corollaries E), with seven conditional consistency lemmas (D1-D7) for estimation under standard identifiability assumptions.   We introduce the Trajectory Deviation Index (TDI), a label-free probe of embedding sensitivity when task accuracy or Jacobian Frobenius norm is insufficient.   Thirteen pre-registered blocks from classical ML through Qwen2.5-7B test the predicted matched, then isotropic, then wrong-W ordering on geometry and deployment drift; twelve pass, and the sole exception (Office-31) is an eigengap failure named before the run. At 7B scale, matched style-PMH improves selective honesty and preserves Style TDI where standard DPO degrades it.   The contribution is naming the deployment nuisance covariance, stating what the regulariser must do, and supplying a closed-form falsifiable theory once that object is identified, not universality on every leaderboard.

### 🤖 AI 总结

**一句话总结**：Robustness, domain adaptation, photometric and occlusion invariance, compositional generalisation, temporal robustness, alignment safety, and classical anisotropic regularisation are usually treated a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Matching, Principle, Geometric, Theory, Loss, Functions, Nuisance-Robust

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22800v1) | [下载PDF](https://arxiv.org/pdf/2605.22800v1.pdf)

---

## [21. SDPM: Survival Diffusion Probabilistic Model for Continuous-Time Survival Analysis](https://arxiv.org/abs/2605.22776v1)

**作者**：Stanislav R. Kirpichenko, Andrei V. Konstantinov, Lev V. Utkin  
**分类**：cs.LG, cs.AI, stat.CO, stat.ML  
**发布时间**：2026-05-21

### 📄 论文摘要

Survival analysis aims to estimate a time-to-event distribution from data with censored observations. Many existing methods either impose structural assumptions on the hazard function or discretize the time axis, which may limit flexibility and introduce approximation errors. We propose the Survival Diffusion Probabilistic Model (SDPM), a generative approach to continuous-time survival analysis. SDPM models the conditional distribution of the survival outcome, represented by the pair of observed time and censoring indicator, $\mathbb{P}(T,δ\mid \mathbf{x})$, using a denoising diffusion model. Under the assumption of conditionally independent censoring, conditional samples generated by the model can be transformed into survival function estimates using the Kaplan-Meier estimator. This formulation avoids parametric assumptions on the event-time distribution and does not require a discretization of the output time space. The model operates in a transformed target space, using standardized log-times and a continuous Gaussian-mixture representation of the censoring indicator. We evaluate SDPM on ten real survival datasets and compare it with five strong baselines, including tree-based, boosting-based, and neural survival models. Results show that SDPM achieves competitive predictive performance across C-index, integrated time-dependent AUC, and integrated Brier score. A study on synthetic Cox-Weibull data demonstrates that SDPM can recover the shape of an underlying continuous survival distribution more accurately than a strong nonparametric baseline when sufficiently many samples are generated. An ablation study confirms the importance of the proposed target-space transformations, which improve event-rate calibration, reduce invalid generated times, and provide consistent gains in predictive discrimination. Codes implementing the proposed model are publicly available.

### 🤖 AI 总结

**一句话总结**：Survival analysis aims to estimate a time-to-event distribution from data with censored observations. Many existing methods either impose structural assumptions on the hazard function or discretize th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, SDPM, Survival, Probabilistic, Model, Continuous-Time, Analysis, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22776v1) | [下载PDF](https://arxiv.org/pdf/2605.22776v1.pdf)

---

## [22. MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive Load Assessment from Eye-Gaze Tracking Data](https://arxiv.org/abs/2605.22775v1)

**作者**：Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh 等 8 位作者  
**分类**：cs.LG, cs.AI, cs.HC  
**发布时间**：2026-05-21

### 📄 论文摘要

Real-time cognitive load assessment from eye-tracking signals could potentially enable adaptive human-centered-AI such as safety-critical applications such as driver vigilance monitoring or automated flight deck assistance, yet two challenges persist: handling frequent data missingness from blinks and tracking failures, and efficiently modeling long-range temporal dependencies. We propose MambaGaze, a framework that addresses these challenges through 1) XMD encoding, which augments raw features with observation masks and time-deltas to explicitly model data uncertainty, and 2) bidirectional Mamba-2, which captures temporal dependencies with linear computational complexity. Experiments on CLARE and CL-Drive datasets under leave-one-subject-out evaluation show that MambaGaze achieves 76.8% and 73.1% accuracy, respectively, outperforming CNN, Transformer, ResNet, and VGG baselines by 4-12 percentage points. Edge deployment benchmarks on NVIDIA Jetson platforms demonstrate real-time inference at 43-68 FPS with power consumption below 7.5W, confirming feasibility for wearable cognitive load monitoring.

### 🤖 AI 总结

**一句话总结**：Real-time cognitive load assessment from eye-tracking signals could potentially enable adaptive human-centered-AI such as safety-critical applications such as driver vigilance monitoring or automated ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MambaGaze, Bidirectional, Mamba, Explicit, Missing, Data, Modeling, Cognitive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22775v1) | [下载PDF](https://arxiv.org/pdf/2605.22775v1.pdf)

---

## [23. CogAdapt: Transferring Clinical ECG Foundation Models to Wearable Cognitive Load Assessment via Lead Adaptation](https://arxiv.org/abs/2605.22774v1)

**作者**：Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh 等 8 位作者  
**分类**：cs.LG, cs.AI, cs.HC  
**发布时间**：2026-05-21

### 📄 论文摘要

Real-time cognitive load assessment is essential for adaptive human-computer interaction but remains challenging due to limited labeled data and poor cross-subject generalization. Recent ECG foundation models pre-trained on millions of clinical recordings offer rich representations, but cannot be directly applied to wearable devices due to sensor configuration mismatch and task differences. In this paper, we propose CogAdapt, a framework that adapts clinical ECG foundation models to wearable cognitive load assessment. CogAdapt introduces LeadBridge, a learnable adapter that transforms 3-lead wearable signals into anatomically consistent 12-lead representations, and ProFine, a progressive fine-tuning strategy that gradually unfreezes encoder layers while preventing catastrophic forgetting. Evaluations on two public datasets (CLARE and CL-Drive) under leave-one-subject-out cross-validation show that CogAdapt substantially outperforms baselines trained from scratch, achieving macro-F1 scores of 0.626 and 0.768. These results demonstrate the promise of foundation model adaptation for subject-independent cognitive load assessment from wearable sensors.

### 🤖 AI 总结

**一句话总结**：Real-time cognitive load assessment is essential for adaptive human-computer interaction but remains challenging due to limited labeled data and poor cross-subject generalization. Recent ECG foundatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CogAdapt, Transferring, Clinical, ECG, Foundation, Models, Wearable, Cognitive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22774v1) | [下载PDF](https://arxiv.org/pdf/2605.22774v1.pdf)

---

## [24. Lumberjack: Better Differentially Private Random Forests through Heavy Hitter Detection in Trees](https://arxiv.org/abs/2605.22756v1)

**作者**：Christian Janos Lebeda, David Erb, Tudor Cebere 等 4 位作者  
**分类**：cs.LG, cs.DS  
**发布时间**：2026-05-21

### 📄 论文摘要

Random forests are widely used in fields involving sensitive tabular data, but existing approaches to enforcing differential privacy (DP) typically degrade performance to the point of impracticality. In this paper, we introduce Lumberjack, a differentially private random forest algorithm that achieves substantially higher utility by constructing large random decision trees and then applying aggressive, privacy-preserving pruning to retain only sufficiently populated nodes. A key component of our approach is a novel $(\varepsilon,δ)$-DP heavy hitter detection algorithm for hierarchical data, whose error is $O_{\varepsilon,δ}(\sqrt{\log h})$ for trees of height $h$ and may be of independent interest. This favorable scaling enables the use of significantly deeper trees than in prior work, leading to improved expressiveness under privacy constraints. Our empirical evaluation on benchmark datasets shows that Lumberjack consistently outperforms prior DP random forest methods, establishing a new state of the art. In particular, our approach yields substantial improvements in the privacy-utility trade-off for practical privacy budgets. Our findings suggest that carefully designed DP random forests can close much of the utility gap, highlighting a promising and underexplored direction for future research.

### 🤖 AI 总结

**一句话总结**：Random forests are widely used in fields involving sensitive tabular data, but existing approaches to enforcing differential privacy (DP) typically degrade performance to the point of impracticality. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Lumberjack, Better, Differentially, Private, Random, Forests, through, Heavy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22756v1) | [下载PDF](https://arxiv.org/pdf/2605.22756v1.pdf)

---

## [25. Cyber-Physical Anomaly Detection in IoT-Enabled Smart Grids Using Machine Learning and Metaheuristic Feature Optimization](https://arxiv.org/abs/2605.22749v1)

**作者**：Adis Alihodžić, Eva Tuba, Milan Tuba  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-21

### 📄 论文摘要

Modern smart grids rely on dense measurement infrastructures, communication links, and intelligent field devices. Although this improves supervision and control, it also increases vulnerability to cyber-physical disruptions. Operators must distinguish physical incidents, such as faults or line disturbances, from malicious actions, such as false data injection or unauthorized command execution. This chapter investigates this problem using the well-known MSU/ORNL Power System Attack Dataset. The proposed method combines machine learning with genetic-algorithm-based feature selection. The objective is twofold: to classify attack and natural events accurately, and to determine whether a reduced set of physically informative PMU/IED measurements can support reliable detection. Several baseline models are evaluated, including logistic regression, RBF-SVM, XGBoost, Random Forest, and Extra Trees. The results show that tree-based ensemble models are the most effective for the considered dataset, with Extra Trees providing the strongest full-feature baseline. After feature selection, the GA + Extra Trees model reduces the clean PMU feature space from 112 attributes to an average of 27.4 attributes over five runs, while increasing macro-F1 from 0.9118 to 0.9212 and ROC-AUC from 0.9791 to 0.9837. These results indicate that many synchronized electrical measurements are redundant. A compact subset of phasor-based features can still provide accurate and interpretable anomaly detection in smart grids.

### 🤖 AI 总结

**一句话总结**：Modern smart grids rely on dense measurement infrastructures, communication links, and intelligent field devices. Although this improves supervision and control, it also increases vulnerability to cyb...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Cyber-Physical, Anomaly, Detection, IoT-Enabled, Smart, Grids, Machine, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22749v1) | [下载PDF](https://arxiv.org/pdf/2605.22749v1.pdf)

---

## [26. Plug-in Losses for Evidential Deep Learning: A Simplified Framework for Uncertainty Estimation that Includes the Softmax Classifier](https://arxiv.org/abs/2605.22746v1)

**作者**：Berk Hayta, Hannah Laus, Simon Mittermaier 等 4 位作者  
**分类**：cs.LG, eess.AS, stat.ML  
**发布时间**：2026-05-21

### 📄 论文摘要

Real-world sensor-based learning systems require uncertainty estimation that is both reliable and computationally efficient. Evidential Deep Learning (EDL) provides single-pass uncertainty estimation by modeling the class probabilities via Dirichlet distributions, where the Dirichlet parameters are predicted by a learned neural network mapping. However, this approach can lead to computational challenges, as Dirichlet expected objectives are more complex than standard supervised learning losses, complicating their analysis and implementation. We address this issue by approximating the objective of the first-order empirical risk minimization problem induced by EDL with a plug-in loss evaluated at the Dirichlet mean and show that, under mild assumptions, the approximation error decays with growing evidence for a broad class of loss functions, including mean-squared error and cross-entropy loss. As a special case, our analysis provides justification for the use of softmax in the context of uncertainty estimation, since under a particular evidence-to-Dirichlet mapping, our framework includes the standard softmax classifier. We validate the proposed simplified objectives on the Google Speech Commands dataset and show that they achieve predictive accuracy and selective prediction performance comparable to classical EDL, while being simpler to implement using standard deep learning losses and training pipelines. To the best of our knowledge, this empirical analysis is the first to obtain coverage-accuracy trade-offs for speech recognition tasks through EDL.

### 🤖 AI 总结

**一句话总结**：Real-world sensor-based learning systems require uncertainty estimation that is both reliable and computationally efficient. Evidential Deep Learning (EDL) provides single-pass uncertainty estimation ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Plug-in, Losses, Evidential, Deep, Learning, Simplified, Framework, Uncertainty

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22746v1) | [下载PDF](https://arxiv.org/pdf/2605.22746v1.pdf)

---

## [27. SeqLoRA: Bilevel Orthogonal Adaptation for Continual Multi-Concept Generation](https://arxiv.org/abs/2605.22743v1)

**作者**：Javad Parsa, Enis Simsar, Amir Joudaki 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-21

### 📄 论文摘要

Parameter-efficient fine-tuning enables fast personalization of text-to-image diffusion models, but composing multiple custom concepts remains challenging due to representation interference. Existing modular methods either rely on expensive post-hoc fusion or freeze adaptation subspaces, which limit expressiveness and concept fidelity. To address this trade-off, we propose Sequential regularized LoRA (SeqLoRA), a constrained continual learning framework that jointly optimizes both LoRA factors via bilevel optimization. Theoretically, we establish strong convergence guarantees for our algorithm and model the residual layer activations as a matrix sub-Gaussian process to derive high-probability bounds on catastrophic forgetting. We further prove that learning the LoRA basis from data minimizes residual interference energy more effectively than frozen-basis methods. Experiments on multi-concept image generation demonstrate that SeqLoRA improves identity preservation and scalability across up to 101 concepts, while avoiding costly fusion and reducing attribute interference in composed generations.

### 🤖 AI 总结

**一句话总结**：Parameter-efficient fine-tuning enables fast personalization of text-to-image diffusion models, but composing multiple custom concepts remains challenging due to representation interference. Existing ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SeqLoRA, Bilevel, Orthogonal, Adaptation, Continual, Multi-Concept, Generation, Parameter-efficient

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22743v1) | [下载PDF](https://arxiv.org/pdf/2605.22743v1.pdf)

---

## [28. Ternary Decision Trees with Locally-Adaptive Uncertainty Zones](https://arxiv.org/abs/2605.22740v1)

**作者**：William Smits  
**分类**：cs.LG  
**发布时间**：2026-05-21

### 📄 论文摘要

Decision trees partition the feature space using hard binary thresholds, assigning identical confidence to instances far from a decision boundary and to those directly on it. We introduce ternary decision trees, which augment each split node with an uncertainty zone of half-width delta centered on the optimal threshold. Instances in this zone receive predictions formed by weighted blending of both child subtrees and are flagged as boundary-uncertain, signaling that downstream applications may treat these predictions differently. Crucially, delta is computed locally at each node from statistics already available during standard CART split finding, requiring no external noise specification. We propose and evaluate five delta-estimation methods: quality-plateau (plateau width of the split criterion curve), class-overlap (empirical class-distribution overlap), gain-ratio (split quality relative to split entropy), node-bootstrap (threshold variance under node-level resampling), and margin (SVM-inspired distance to the nearest cross-class training example). Evaluated across 72 OpenML-CC18 datasets with 5-fold cross-validation, all five methods with probabilistic routing significantly outperform standard CART on decided accuracy (Wilcoxon signed-rank, p < 0.001). The margin method achieves the best efficiency (0.104 accuracy gain per unit of boundary-uncertain flagging rate), wins on 42 of 72 datasets, and requires zero additional hyperparameters. Analysis on three Breiman synthetic benchmarks reveals that margin is self-calibrating on clean data while node-bootstrap and quality-plateau best track theoretical irreducible error. Experiments on four medical and financial datasets demonstrate practical value: on mammography, node-bootstrap achieves +0.71% decided accuracy by flagging 10.8% of screening cases as boundary-uncertain.

### 🤖 AI 总结

**一句话总结**：Decision trees partition the feature space using hard binary thresholds, assigning identical confidence to instances far from a decision boundary and to those directly on it. We introduce ternary deci...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Ternary, Decision, Trees, Locally-Adaptive, Uncertainty, Zones, partition, feature

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22740v1) | [下载PDF](https://arxiv.org/pdf/2605.22740v1.pdf)

---

## [29. Proxy-Based Approximation of Shapley and Banzhaf Interactions](https://arxiv.org/abs/2605.22738v1)

**作者**：Santo M. A. R. Thies, Hubert Baniecki, R. Teal Witter 等 6 位作者  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-05-21

### 📄 论文摘要

Shapley and Banzhaf interactions capture the complex dynamics inherent in modern machine learning applications. However, current estimators for these higher-order interactions trade off between speed and accuracy. To overcome this limitation, we introduce ProxySHAP. ProxySHAP reconciles the high sample efficiency of tree-based proxy models with a principled path to consistency via residual correction. On a theoretical level, we derive a polynomial-time generalization of interventional TreeSHAP to compute exact interaction indices for tree ensembles, successfully bypassing exponential tree-depth dependencies in prior methods. Furthermore, we formally analyze the residual adjustment strategy, characterizing the specific conditions under which Maximum Sample Reuse (MSR) corrects proxy bias without its variance scaling exponentially with interaction size. Extensive benchmarking demonstrates that ProxySHAP sets a new state-of-the-art standard for approximation quality, including in large-scale applications with thousands of features. By achieving the lowest error in both small- and large-budget regimes, ProxySHAP significantly outperforms the prior best estimators ProxySPEX and KernelSHAP-IQ, while also delivering superior performance on downstream explainability tasks.

### 🤖 AI 总结

**一句话总结**：Shapley and Banzhaf interactions capture the complex dynamics inherent in modern machine learning applications. However, current estimators for these higher-order interactions trade off between speed ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Proxy-Based, Approximation, Shapley, Banzhaf, Interactions, capture, complex

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22738v1) | [下载PDF](https://arxiv.org/pdf/2605.22738v1.pdf)

---

## [30. The Value of Covariance Matching in Gaussian DDPMs and the Lanczos Sampler](https://arxiv.org/abs/2605.22723v1)

**作者**：Md Sahil Akhtar, Aymane El Gadarri, Vivek F. Farias 等 4 位作者  
**分类**：cs.LG, cs.AI, cs.IT  
**发布时间**：2026-05-21

### 📄 论文摘要

A central error measure in Gaussian DDPMs is the path-space KL divergence between the exact reverse chain and the learned Gaussian reverse process. This quantity is especially relevant for procedures such as classifier guidance, which perturb the entire reverse trajectory rather than only the terminal sample. Prior analyses show that standard isotropic reverse covariances suffer an unavoidable $Ω(1/T)$ path-KL error as the number of denoising steps $T$ grows. We show that matching the full posterior covariance breaks this barrier, yielding an order-wise improvement that reduces the path KL to $O(1/T^2)$. To make full covariance matching practical, we introduce the Lanczos Gaussian sampler (LGS), a training-free, matrix-free method for sampling from the optimal reverse covariance using only covariance-vector products, which are available through Jacobian-vector products of the posterior mean. LGS avoids dense covariance storage and auxiliary covariance models. We prove that LGS approximation error decays exponentially in the number of Lanczos steps, where each Lanczos step requires a single Jacobian-vector product. Empirically, using only just three such steps improves sample quality over strong diagonal-covariance baselines, including OCM-DDPM, across standard image benchmarks. This identifies full covariance matching as both theoretically valuable and practically accessible for fast DDPM sampling.

### 🤖 AI 总结

**一句话总结**：A central error measure in Gaussian DDPMs is the path-space KL divergence between the exact reverse chain and the learned Gaussian reverse process. This quantity is especially relevant for procedures ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Value, Covariance, Matching, Gaussian, DDPMs, Lanczos, Sampler

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.22723v1) | [下载PDF](https://arxiv.org/pdf/2605.22723v1.pdf)

---

