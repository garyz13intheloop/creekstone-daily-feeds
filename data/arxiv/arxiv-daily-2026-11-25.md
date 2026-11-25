# arXiv AI 论文日报 | 2026-11-25

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (10 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.LG](#csLG) (9 篇)

---

## cs.AI

## [1. MetaFORGE: A Meta-Learning Framework for Harness Optimization in Automated Code Generation for Parallel Computing](https://arxiv.org/abs/2611.33119v1)

**作者**：Scott Piersall, Yang Gao, Shenyang Liu 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-24

### 📄 论文摘要

Large language models (LLMs) can generate parallel programs, but their correctness and performance depend strongly on the instructions that guide generation. We present \textsc{MetaFORGE}, an execution-grounded meta-learning framework that iteratively optimizes persistent natural-language skill specifications for MPI C code generation. \textsc{MetaFORGE} combines correctness testing, compiler diagnostics, static-analysis findings, runtime measurements, and rank-level load-imbalance profiles into a scalar reward that drives textual-gradient refinement, while an external memory distills and retrieves reward-supported optimization knowledge across runs.   Across six MPI tasks and three workload sizes, \textsc{MetaFORGE} improves static-analysis quality, runtime, and load balance relative to zero-shot generation and generally exceeds the evaluated \textsc{TextGrad} iterative baseline. A model-matched refinement ablation shows that the MetaFORGE advantage persists when its refinement model is reduced to \texttt{gpt-4o}. An expanded retrieval ablation across all 18 task--workload configurations shows consistent runtime benefit and broad static-analysis and load-balance benefit from retrieved context. Leakage-controlled held-out and zero-update experiments further provide evidence that optimization knowledge persists in both the transferred skill and external memory under the evaluated protocol.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) can generate parallel programs, but their correctness and performance depend strongly on the instructions that guide generation. We present \textsc{MetaFORGE}, an executio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MetaFORGE, Meta-Learning, Framework, Harness, Optimization, Automated, Code, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33119v1) | [下载PDF](https://arxiv.org/pdf/2611.33119v1.pdf)

---

## [2. Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance](https://arxiv.org/abs/2611.33098v1)

**作者**：Lingwei Gu, Jimmy Lin  
**分类**：cs.AI, cs.IR  
**发布时间**：2026-11-24

### 📄 论文摘要

Agents built on frontier language models are expensive. At every step, the frontier model re-reads its entire context and executes every subtask regardless of its difficulty. This paper explores the simple thesis that much of this cost can be removed by delegating easy subtasks to a small language model, or SLM, that runs on hardware one already owns. To test it, we build Delegent, a simple and effective agent harness built on Claude Code, in which the frontier model stays in charge of every task but hands focused subtasks, such as investigating code, running tests, and searching a corpus, to SLM subagents. Existing approaches such as cascades and model routers usually choose which model executes the entire task, whereas in Delegent, the frontier model always leads the execution and delegates easy subtasks to the SLM. No router or model is trained, so either model can be swapped freely. With the help of a 27B FP8 SLM, Delegent reduces the frontier cost of long-horizon coding by 67% and of agentic search by 59%, with no loss in task performance, and even a 2B SLM that fits on a laptop reduces the coding cost by 66%. The savings grow with the legwork that the frontier model would otherwise do itself, and a short instruction, which leaves the main coding tasks to the frontier model, accounts for most of the saving and keeps the 2B SLM from losing tasks. Code: https://github.com/castorini/delegent

### 🤖 AI 总结

**一句话总结**：Agents built on frontier language models are expensive. At every step, the frontier model re-reads its entire context and executes every subtask regardless of its difficulty. This paper explores the s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, Delegent, Harness, Reduces, Cost, without, Sacrificing, Performance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33098v1) | [下载PDF](https://arxiv.org/pdf/2611.33098v1.pdf)

---

## [3. Uncertainty-Aware Candidate Generation for Entity Linking in Cyber Threat Intelligence](https://arxiv.org/abs/2611.33086v1)

**作者**：Nasser Alkhulaifi, Direnc Pekaslan, Christian Wagner  
**分类**：cs.AI  
**发布时间**：2026-11-24

### 📄 论文摘要

Entity Resolution (ER) pipelines often collapse ambiguity into early hard decisions: upstream Named Entity Recognition (NER) selects a single span and type, and downstream Entity Linking (EL) treats that choice as ground truth. This discards valuable information about the ambiguity of the underlying data (e.g., span boundary disagreement and type confusion), leading to brittle systems that fail unpredictably when faced with uncertainty in inputs. Therefore, this work presents a proof-of-concept for uncertainty-aware ER that treats uncertainty as native data that should be preserved and exploited throughout ER pipelines. We (i) capture uncertainty signals in the NER stage and (ii) leverage these signals into the EL stage to improve candidate retrieval under ambiguity. Using a BERT-based NER model augmented with two auxiliary span-boundary prediction heads, we apply Monte Carlo (MC) dropout at inference time to derive three mention-level proxy signals: the MC-averaged start-boundary probability, the MC-averaged end-boundary probability, and De Luca-Termini fuzzy entropy computed over the Begin-Inside-Outside (BIO) predictive distribution. These signals are used to adapt the fuzzy cutoff in candidate generation (CG) for EL. Because CG is treated as a blocking step, we evaluate retrieval recall. On the AnnoCTR dataset linked to the MITRE ATTCK knowledge base, the boundary-aware and dual-signal fuzzy linking approaches improve Recall@10 from 0.6186 to 0.7966. The contribution lies not in an end-to-end optimised ER pipeline but in establishing uncertainty preservation as a viable and beneficial component of ER pipelines, enabling downstream EL to make better-informed decisions under uncertainty.

### 🤖 AI 总结

**一句话总结**：Entity Resolution (ER) pipelines often collapse ambiguity into early hard decisions: upstream Named Entity Recognition (NER) selects a single span and type, and downstream Entity Linking (EL) treats t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Uncertainty-Aware, Candidate, Generation, Entity, Linking, Cyber, Threat, Intelligence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33086v1) | [下载PDF](https://arxiv.org/pdf/2611.33086v1.pdf)

---

## [4. Auditing the Judge: Human-Derived Bias Discovery, Quantification, and Mitigation in LLM Judges](https://arxiv.org/abs/2611.33065v1)

**作者**：Hamin Koo, Chanjoo Jung, Fangzhao Wu 等 4 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-11-24

### 📄 论文摘要

While Large Language Models (LLMs) are increasingly deployed as automated evaluators in evaluation and training pipelines, their judgements are often affected by systematic biases that conflict with human preferences. Although prior work has identified various biases and proposed methods for detecting and mitigating them, less attention has been paid to using human preferences to inform bias identification and mitigation. Moreover, these approaches rely heavily on pre-discovered bias lists, overlook bias strength, and depend on costly interventions. In this work, we propose HUB-J, an integrated framework based on human-derived bias factors that detects, quantifies, and mitigates biases in LLM-as-a-Judge systems. Our approach leverages human-LLM judgement disagreement cases to automatically discover interpretable bias factors, and utilizes agreement cases to quantify bias strength through controlled input modifications and resulting shifts in model decisions. Finally, building on these quantified biases, we introduce a lightweight, training-free regression-based mitigation strategy that estimates the influence of each bias factor on model judgments and corrects bias-influenced decisions by removing its estimated effect. Empirical results show that HUB-J uncovers both known and novel bias factors, reveals meaningful differences in model susceptibility, and consistently reduces bias-driven decision flips while generalizing across models.

### 🤖 AI 总结

**一句话总结**：While Large Language Models (LLMs) are increasingly deployed as automated evaluators in evaluation and training pipelines, their judgements are often affected by systematic biases that conflict with h...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Auditing, Judge, Human-Derived, Bias, Discovery, Quantification, Mitigation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33065v1) | [下载PDF](https://arxiv.org/pdf/2611.33065v1.pdf)

---

## [5. Hybrid AI for AI-Native RAN Control: A Functional Perspective](https://arxiv.org/abs/2611.33035v1)

**作者**：Sabrine Aroua, Osama Arouk, Pegah Alizadeh  
**分类**：cs.AI  
**发布时间**：2026-11-24

### 📄 论文摘要

AI-native radio access network (RAN) control involves interdependent decisions across network entities, protocol layers, and timescales. Understanding how AI and conventional methods can jointly support these decisions requires a common basis for comparing their functional roles. This survey introduces a technique-agnostic taxonomy of RAN decision-making organized around four complementary capabilities: Representation and Reasoning, Prediction and Simulation, Adaptive Control, and Decision Synthesis. These capabilities are defined by their roles in the control process, independently of the techniques used to implement them. Through this perspective, we examine representative AI and model-based approaches, including foundation models, world models, reinforcement learning, and optimization. We then apply the taxonomy to representative RAN control solutions across slow, medium, fast, and cross-timescale applications to identify which capabilities they implement and how these capabilities are combined in hybrid AI systems. We also review datasets, benchmarks, simulators, digital twins, and experimental platforms according to their support for the decision-making process and reproducible evaluation. The review highlights a gap between the availability of resources for closed-loop experimentation and the standardization of tasks, metrics, and evaluation protocols needed for meaningful comparisons.Finally, we identify research directions for hybrid AI in AI-native RAN, including capability integration, multi-agent and cross-timescale coordination, constraint handling, and reproducible closed-loop evaluation. A curated list of surveyed works and evaluation resources is available at https://github.com/pegahani/Hybrid-AI-RAN-Survey.

### 🤖 AI 总结

**一句话总结**：AI-native radio access network (RAN) control involves interdependent decisions across network entities, protocol layers, and timescales. Understanding how AI and conventional methods can jointly suppo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hybrid, AI-Native, RAN, Control, Functional, Perspective, radio, access

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33035v1) | [下载PDF](https://arxiv.org/pdf/2611.33035v1.pdf)

---

## [6. RecordRoute: Auditing Agent Failures with Localization-Guided Diagnosis](https://arxiv.org/abs/2611.33022v1)

**作者**：Yifan Duan, Lihuan Li, Chao Xue 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-24

### 📄 论文摘要

Auditing failed agent executions requires identifying the responsible actor, the earliest decisive step, and the error mode. Representative supervised methods either focus on step localization or predict multiple attribution targets from shared trajectory representations. These methods do not use the localization result to select the text for mode diagnosis. To address this limitation, we propose RecordRoute, which couples comparative localization with local diagnosis. Specifically, it represents each record with word and character features and learns to rank records through comparisons within each trajectory. The selected record supplies the actor and step, while its text and metadata drive mode prediction. On controlled-injection Who&When Pro, RecordRoute outperforms StepFinder and ASCon on all four official metrics. With actor and step predictions fixed, local diagnosis reaches 77.47% pooled joint accuracy versus 69.28% for full-trace diagnosis. On natural failures from TraceElephant and CatchBench POST, it outperforms these baselines and three open LLMs in localization.

### 🤖 AI 总结

**一句话总结**：Auditing failed agent executions requires identifying the responsible actor, the earliest decisive step, and the error mode. Representative supervised methods either focus on step localization or pred...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, RecordRoute, Auditing, Failures, Localization-Guided, Diagnosis, failed, executions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33022v1) | [下载PDF](https://arxiv.org/pdf/2611.33022v1.pdf)

---

## cs.CL

## [7. CoT-Proxy: Cross-Format Transfer for Distilling Long-Horizon Policies](https://arxiv.org/abs/2611.33148v1)

**作者**：Dawid J. Kopiczko, Tijmen Blankevoort, Yuki M. Asano  
**分类**：cs.CL  
**发布时间**：2026-11-24

### 📄 论文摘要

Reasoning models become long-horizon agents through reinforcement learning or, more cheaply, through fine-tuning on a stronger teacher's trajectories, which contain the teacher's chain-of-thought as well as its actions. The standard fine-tuning approach imitates both, yet the strongest teachers are closed models whose chain-of-thought is hidden behind an API. We show that the chain-of-thought can be left out altogether and that the long-horizon policy can be distilled from the teacher's actions alone. The student is trained on these trajectories with its reasoning block left empty, while a KL loss on a replay buffer of its own generations limits drift from its initial model. Surprisingly, the policy learned from these trajectories with an empty reasoning block carries over to inference with thinking enabled, where the student reasons in its own style while acting like the teacher, an effect we call cross-format transfer. Distilling the actions of Qwen3.6-27B raises the task success of Qwen3-4B on AppWorld from 7% to 18% and that of Qwen3-32B from 12% to 25%. We further introduce CoT-proxies, short summaries of the teacher's reasoning placed after the empty reasoning block, which raise Qwen3-4B further, to 35%. Since neither actions nor CoT-proxies need the hidden chain-of-thought, the recipe applies unchanged to closed teachers. Distilling GPT-5.6 Luna from its visible outputs and the reasoning summaries its API returns raises Qwen3-4B from 7% to 48% on AppWorld and from 3% to 28% on SWE-bench Verified.

### 🤖 AI 总结

**一句话总结**：Reasoning models become long-horizon agents through reinforcement learning or, more cheaply, through fine-tuning on a stronger teacher's trajectories, which contain the teacher's chain-of-thought as w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CoT-Proxy, Cross-Format, Transfer, Distilling, Long-Horizon, Policies, Reasoning, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33148v1) | [下载PDF](https://arxiv.org/pdf/2611.33148v1.pdf)

---

## [8. SAG-Mem-1.0 Technical Report](https://arxiv.org/abs/2611.33124v1)

**作者**：Yuchao Wu, XingCheng Liang, Xuanze Wang 等 5 位作者  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-11-24

### 📄 论文摘要

Long-term conversational memory requires retrieving complementary facts scattered across dialogue sessions, including intermediate evidence with limited similarity to the original question. Existing approaches often rely on derived memory representations or persistent relational structures, introducing construction costs and potentially losing source details. We present SAG-Mem, a conversational memory framework that preserves complete dialogue messages in non-overlapping chunks and discovers complementary evidence through query-time lexical expansion. Memory construction requires no model inference, using a lexical index without LLM-based extraction, summarization, or semantic relation construction. At query time, BM25 retrieves initial candidates, an evidence evaluator identifies useful chunks, and lexical cues from selected evidence guide an additional retrieval round. Retrieved dialogue is further annotated with calendar interpretations of supported relative-time expressions, preserving the original wording and temporal granularity. We also introduce SAG-Mem-Lite, an alternative configuration that replaces evidence scoring with embedding-based candidate scoring, achieving lower operational cost than Full Context and all memory-based baselines across both benchmarks with low query latency. On LoCoMo and LongMemEval, SAG-Mem achieves overall scores of 83.08 and 80.20, respectively, the highest among the evaluated methods on both benchmarks. On LongMemEval, it exceeds the strongest compared baseline by 7.20 points. SAG-Mem-Lite achieves scores of 77.09 and 77.20, respectively. These results support dialogue preservation and evidence-guided retrieval expansion as an effective design for long-term conversational memory.

### 🤖 AI 总结

**一句话总结**：Long-term conversational memory requires retrieving complementary facts scattered across dialogue sessions, including intermediate evidence with limited similarity to the original question. Existing a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SAG-Mem-1.0, Technical, Report, Long-term, conversational, memory, requires, retrieving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33124v1) | [下载PDF](https://arxiv.org/pdf/2611.33124v1.pdf)

---

## [9. FOL-Proof: Verifying LLM Text-to-Logic Translations via Deterministic Semantics](https://arxiv.org/abs/2611.33078v1)

**作者**：Yisrael Clark, Guy Katz  
**分类**：cs.CL, cs.LO  
**发布时间**：2026-11-24

### 📄 论文摘要

Large Language Models (LLMs) are increasingly used to translate natural-language statements into first-order logic (FOL) to improve reasoning. However, LLMs are prone to errors, and so a semantically unfaithful FOL formula could corrupt downstream reasoning. We present FOL-Proof, a semantic firewall pipeline that validates LLM-generated FOL translations against independently derived linguistic interpretations. FOL-Proof operates by deterministically obtaining a pool of candidate translations via semantic analysis tools, such as the English Resource Grammar and Minimal Recursion Semantics; then applying an SMT solver to check each derived reading for logical equivalence to the LLM-generated formula. If the translation is faithful it is accepted; otherwise, it is rejected, or optionally repaired via repeated invocations to the LLM. The procedure is conservative: incomplete search, unsupported constructions, or inconclusive checks yield abstention rather than false rejection. We evaluated FOL-Proof on established benchmarks (ProofWriter, RuleTaker and PrOntoQA), and also on a new adversarial benchmark (LongFaithCheck). Our experiments show that FOL-Proof attains near perfect selective accuracy, while direct LLM judges and round-trip baselines show substantially worse performance.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) are increasingly used to translate natural-language statements into first-order logic (FOL) to improve reasoning. However, LLMs are prone to errors, and so a semantically ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, FOL-Proof, Verifying, Text-to-Logic, Translations, via, Deterministic, Semantics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33078v1) | [下载PDF](https://arxiv.org/pdf/2611.33078v1.pdf)

---

## [10. Worth the Wait? How Response Time and Streaming Shape Judgments of Generative AI Answers and Chatbot Engagement](https://arxiv.org/abs/2611.33050v1)

**作者**：Zihan Chen, Di Zhu, Lei Nico Zheng  
**分类**：cs.CL, cs.CY, econ.GN  
**发布时间**：2026-11-24

### 📄 论文摘要

Answers from generative AI chatbots built on large language models (LLMs) now arrive at very different speeds: reasoning models deliberate before replying, while response caches can return a stored answer at once. Blind preference votes, which rank these models, are read as judgments of their text, and if delivery matters, faster answers are expected to gain. Research on the labor illusion and on how text appears on screen suggests instead that an answer which unfolds as it is written is credited over the same answer shown at once. We test these accounts with three sources of variation in natural use. First, compar:IA, a French government chatbot arena, answered repeated prompts, by a random draw, either with a fresh answer streamed as it was written or with a stored earlier answer from the same model, shown at once. Within the same prompt, a replay lowered an answer's chance of winning a decisive blind vote by 25.8 percentage points. The same stored text won 57% of its decisive votes when streamed and 29% when replayed, and voters called it less complete, more superficial and more often incorrect when replayed. Second, provider congestion slowed streamed answers. In 324,029 conversations, slower answers earned no detectable net credit in the vote, but a slower first exchange made visitors less likely to ask a follow-up question. Third, in 4,378,514 WildChat replies from everyday ChatGPT use, replies slowed by congestion made users less likely to continue. Delivery moved blind votes, in the direction opposite to the one the arena's designers expected, while waiting cost follow-up questions that a comparison between two answers cannot register when both are slow. The results bear on how AI services cache and stream answers, how they budget latency, and how preference leaderboards evaluate models.

### 🤖 AI 总结

**一句话总结**：Answers from generative AI chatbots built on large language models (LLMs) now arrive at very different speeds: reasoning models deliberate before replying, while response caches can return a stored an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Worth, Wait?, How, Response, Time, Streaming, Shape, Judgments

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33050v1) | [下载PDF](https://arxiv.org/pdf/2611.33050v1.pdf)

---

## [11. SALSA: Sampling Adversarial Suffixes from Learned Distributions for LLM Safety Assessment](https://arxiv.org/abs/2611.33030v1)

**作者**：Shivank Rajput, Himanshu Singh, A. V. Subramanyam  
**分类**：cs.CL, cs.CR  
**发布时间**：2026-11-24

### 📄 论文摘要

Large language models (LLMs) remain vulnerable to jailbreak attacks, where adversaries append optimized suffixes to otherwise benign looking prompts to bypass safety alignment. Existing optimization-based GCG-style attacks can be effective, but they are expensive at inference time, and suffer from poor transfer. We present, SALSA, a generative framework that learns a distribution over jailbreak suffixes from optimization-derived attack corpora. Once trained, the model supports efficient sampling-based attacks. On open-source targets, it achieves attack success rates comparable to state-of-the-art optimization baselines, while reducing generation time from 3.46s to 0.04s per prompt. In black-box transfer, it remains highly effective against proprietary systems, including 99% ASR on GPT-3.5-Turbo, and reaches 45% ASR on the substantially harder GPT-4o, more than doubling the strongest baseline at an equal sampling budget. We further offer an intuition for why generative sampling can preserve high attack success, when the learned suffix distribution is close to the distribution of optimization outputs. Overall, our results show that learning adversarial suffix distributions yields a scalable, and practically efficient foundation for continuous LLM vulnerability discovery.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) remain vulnerable to jailbreak attacks, where adversaries append optimized suffixes to otherwise benign looking prompts to bypass safety alignment. Existing optimization-b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, SALSA, Sampling, Adversarial, Suffixes, Learned, Distributions, Safety

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33030v1) | [下载PDF](https://arxiv.org/pdf/2611.33030v1.pdf)

---

## cs.CV

## [12. DiaCap: Jointly Learning Who Speaks When for Audiovisual Dialogue Captioning](https://arxiv.org/abs/2611.33153v1)

**作者**：Binfei Ji, Zhiwen Cao, Anqi Yang 等 8 位作者  
**分类**：cs.CV, cs.CL, cs.MM, cs.SD  
**发布时间**：2026-11-24

### 📄 论文摘要

We present DiaCap, an audiovisual LLM for comprehensive dialogue captioning, which produces the transcript, timestamps, and a visual description of the speaker for every utterance in a video. Considering that utterance timing and audiovisual diarization are tightly coupled, DiaCap unifies the tasks in a single model, trained in two complementary stages. First, we train DiaCap on 225K curated clips, using synthetic captions that densely label every utterance in detail. Second, we further refine the model via reinforcement learning on 2.9K human-corrected clips, using fine-grained feedback that directly evaluates utterance timing, speaker grouping, and speaker binding. On DiaDemBench, which we extend with utterance-level timestamps and subtitle redaction, both DiaCap with off-the-shelf transcripts and its end-to-end variant DiaCap-E2E achieve strong results. Specifically, DiaCap performs on par with Gemini 4 Argon in audiovisual diarization while clearly outperforming it in timestamp accuracy (76.59 vs. 42.76 TIME). It also maintains strong diarization on multilingual and minute-long videos, and transfers to audiovisual question answering.

### 🤖 AI 总结

**一句话总结**：We present DiaCap, an audiovisual LLM for comprehensive dialogue captioning, which produces the transcript, timestamps, and a visual description of the speaker for every utterance in a video. Consider...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DiaCap, Jointly, Learning, Who, Speaks, When, Audiovisual, Dialogue

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33153v1) | [下载PDF](https://arxiv.org/pdf/2611.33153v1.pdf)

---

## [13. BioLoom: Scaling Biomedical Vision-Language Models by Learning from the Structure of Scientific Articles](https://arxiv.org/abs/2611.33151v1)

**作者**：Yuwei Yang, Xiaoxiao Sun, Alejandro Lozano 等 7 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-24

### 📄 论文摘要

The development of biomedical vision-language models (VLMs) with contrastive image-text pretraining has been driven by scaling to increasingly large and diverse image-text datasets. Beyond scaling, further progress can come from learning richer representations from existing data. We hypothesize that the structure of scientific literature itself provides an additional source of supervision: figures, panels, captions, and accompanying article text encode rich relationships across modalities. Yet, treating these as independent image-text pairs overlooks their relationships. To address this limitation, we incorporate these structural relationships into contrastive image-text supervision. We preserve exact image-text matches while introducing weaker positive supervision for related pairs, such as a panel and the caption of a sibling panel. We upweight cross-article negatives of the same content type to encourage finer discrimination. We also enrich panel descriptions using visual content, original figure captions, and mentioning paragraphs. Pairing panels with these descriptions and whole figures with their original captions yields Loom52M, a dataset of 52.4 million image-text pairs spanning scientific charts and biomedical images. Using Loom52M, BioLoom (DFN-2B) achieves 56.82% domain-balanced mean accuracy across 67 zero-shot classification tasks from 43 datasets in 10 domains, compared with 48.77% for MedPMC-CLIP. On BioLoomBench with concise captions and BioMedFlickr, it achieves bidirectional mean Recall@1 of 63.20% and 10.59%, versus 46.37% and 7.55% for the respective strongest evaluated baselines, BiomedCLIP and MedPMC-CLIP. Code, datasets, benchmarks, and models are available at https://bioloom-clip.github.io/.

### 🤖 AI 总结

**一句话总结**：The development of biomedical vision-language models (VLMs) with contrastive image-text pretraining has been driven by scaling to increasingly large and diverse image-text datasets. Beyond scaling, fu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, BioLoom, Scaling, Biomedical, Vision-Language, Models, Learning, Structure

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33151v1) | [下载PDF](https://arxiv.org/pdf/2611.33151v1.pdf)

---

## [14. One Take, Many Cameras: Audio-Grounded Shot Synthesis for Dialogue Re-Cinematography](https://arxiv.org/abs/2611.33147v1)

**作者**：Anthony Chen, Naomi Ken Korem, Matan Ben-Yosef 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-24

### 📄 论文摘要

Creating a dialogue scene typically requires cutting between multiple views (e.g., close-ups, medium shots, and over-the-shoulder shots) of the actors. Yet capturing such coverage is costly and in many settings unavailable. We study dialogue re-cinematography: synthesizing additional shots from a single wide-angle dialogue video. Existing video generators can synthesize new shots, but rely on visual cues alone, so when the source video barely shows the lips, the generated lip motion fails to match the speech. Our key observation is that the speech audio is view-invariant: it constrains lip motion in any target view. Building on this insight, we adapt a pretrained audio-visual diffusion model to generate the new shot from a target frame that specifies the view, a source video that contains the performance, and the speech audio that drives lip motion. In multi-person scenes, however, pretrained audio-visual models drive every visible face with the same speech, causing speech leakage, where silent listeners mouth the speaker's words. We therefore introduce speaker-aware audio gating, a training-free module that lets the audio drive only the faces that speak in the target shot. On a cinematic paired-view benchmark spanning diverse viewpoints and framings, our method lowers perceptual error by 59%, landmark error by 56%, and speech leakage by 97% relative to the strongest baseline, Wan 3.0. Our method also remains robust on in-the-wild scenes, highlighting its potential for film post-production.

### 🤖 AI 总结

**一句话总结**：Creating a dialogue scene typically requires cutting between multiple views (e.g., close-ups, medium shots, and over-the-shoulder shots) of the actors. Yet capturing such coverage is costly and in man...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：One, Take, Many, Cameras, Audio-Grounded, Shot, Synthesis, Dialogue

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33147v1) | [下载PDF](https://arxiv.org/pdf/2611.33147v1.pdf)

---

## [15. Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](https://arxiv.org/abs/2611.33145v1)

**作者**：Zehan Zheng, Yanyuan Chen, Deming Li 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-24

### 📄 论文摘要

Embodied Spatial Reasoning (ESR) is central to deploying Vision-Language Models (VLMs) in real-world embodied tasks, yet remains inadequately evaluated. Existing benchmarks primarily assess spatial reasoning in static images or synthetic indoor environments, where semantic shortcuts often suffice, making it difficult to faithfully evaluate spatial reasoning capabilities in the wild. In light of this, we present Lost on Campus, a benchmark for evaluating ESR in large-scale real-world outdoor 3D environments reconstructed by 3D Gaussian Splatting. Our benchmark introduces a unified reasoning-action evaluation framework that seamlessly integrates diagnostic QA for isolated reasoning with closed-loop interactive navigation for active reasoning under multimodal instructions. To enable fine-grained diagnosis, we evaluate six capability aspects of ESR: action grounding, spatial foresight, metric awareness, goal-directed planning, ego-allocentric localization, and spatio-temporal consistency. Extensive experiments reveal that: (i) Compared to indoor settings, real-world outdoor environments impose substantially higher demands on spatial reasoning, where existing models exhibit poor performance; (ii) VLMs still struggle with fine-grained visual alignment, with failures in spatial foresight and ego-allocentric localization emerging as primary bottlenecks; (iii) Improving multimodal interaction capabilities and long-term spatial reasoning is crucial for advancing embodied intelligence. These findings highlight that faithful evaluation of ESR demands benchmarks tightly coupling perception, reasoning and action within realistic and continuous environments.

### 🤖 AI 总结

**一句话总结**：Embodied Spatial Reasoning (ESR) is central to deploying Vision-Language Models (VLMs) in real-world embodied tasks, yet remains inadequately evaluated. Existing benchmarks primarily assess spatial re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Lost, Campus, Evaluating, Embodied, Spatial, Reasoning, Vision-Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33145v1) | [下载PDF](https://arxiv.org/pdf/2611.33145v1.pdf)

---

## [16. Physicl Scenes: An Artist-created 3D Dataset for Learning Perception and Action](https://arxiv.org/abs/2611.33137v1)

**作者**：Yueh-Cheng Liu, Snehal Jauhri, Matthias Nießner 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-24

### 📄 论文摘要

We present Physicl Scenes, a high-quality artist-created and curated dataset of 6,499 3D scenes spanning household rooms, public interiors, and outdoor spaces. The dataset combines detailed geometry, physically based materials, and carefully composed environments with object- and part-level semantic annotations, providing rich, joint supervision for visual and embodied learning. We demonstrate its value as training data across inverse rendering, 3D reconstruction, scene understanding, and mobile manipulation. Across these tasks, training state-of-the-art methods with our scenes improves performance over alternative synthetic datasets. In addition, we introduce a mobile manipulation benchmark, evaluating vision-language-action models performing physical pick and place in diverse 3D scenes with realistic layouts, and using our part annotations to also score where each object is grasped. Our dataset will be released publicly to facilitate research in visual and embodied AI.

### 🤖 AI 总结

**一句话总结**：We present Physicl Scenes, a high-quality artist-created and curated dataset of 6,499 3D scenes spanning household rooms, public interiors, and outdoor spaces. The dataset combines detailed geometry, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, 3D, Physicl, Scenes, Artist-created, Dataset, Learning, Perception

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33137v1) | [下载PDF](https://arxiv.org/pdf/2611.33137v1.pdf)

---

## [17. EventDiffusion: Learning Native Event Stream Distribution from Videos](https://arxiv.org/abs/2611.33096v1)

**作者**：Karthik Sundar Senthilkumar, Christopher Thirgood, Simon Hadfield  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-24

### 📄 论文摘要

Event cameras capture asynchronous brightness changes at high temporal resolution, but scarce recordings constrain data-driven research. Sparse RGB observations cannot uniquely determine intervening events since identical frames may correspond to streams with different activity, polarities, and timing. Existing simulators largely rely on prescribed sensor dynamics and estimated brightness trajectories, whose assumptions limit the diversity and fidelity of plausible event streams. We introduce EventDiffusion, a hierarchical generative framework that directly learns the conditional distribution of native asynchronous event streams from real recordings. EventDiffusion decomposes generation into three probabilistic processes: Event Activity Diffusion (EAD) learns stochastic discrete event counts; Event Spatial Allocation (ESA) distributes these counts to individual pixels while preserving cardinality; and Event Timing Diffusion (ETD) learns continuous asynchronous timestamp distributions. We also introduce CEFS, an event-stream realism metric combining event activity and polarity with multiscale space-time structure and temporal fidelity. Across all datasets, EventDiffusion achieves double the accuracy of SOTA methods and demonstrates robustness across different cameras at any resolution.

### 🤖 AI 总结

**一句话总结**：Event cameras capture asynchronous brightness changes at high temporal resolution, but scarce recordings constrain data-driven research. Sparse RGB observations cannot uniquely determine intervening e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EventDiffusion, Learning, Native, Event, Stream, Distribution, Videos, cameras

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33096v1) | [下载PDF](https://arxiv.org/pdf/2611.33096v1.pdf)

---

## [18. SUPRA: Synthesizing Amyloid PET from MRI and Plasma Biomarkers with an Explicit Regional SUVR Prior](https://arxiv.org/abs/2611.33061v1)

**作者**：Hanwen Li, Fadi Deek, Zhi Wei 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-24

### 📄 论文摘要

Amyloid positron emission tomography (PET) quantifies brain amyloid-$β$ as a standardized uptake value ratio (SUVR), but is costly and not widely available. Structural magnetic resonance imaging (MRI) is routine, and plasma biomarkers such as phosphorylated tau 217 (p-tau217) are becoming practical. Synthesizing amyloid PET from MRI alone is ill-posed, because brain anatomy reveals little about amyloid burden. We present SUPRA (SUVR prior-guided amyloid synthesis), which divides this task between MRI and plasma biomarkers. A regression maps the plasma panel to regional SUVR levels, painted onto the subject's MRI segmentation as an explicit prior. A 3D network then adds a residual correction guided by MRI. The output is in absolute SUVR, and the model also runs on p-tau217 alone. On the Alzheimer's Disease Neuroimaging Initiative (ADNI) cohort (111 test pairs), SUPRA reaches a peak signal-to-noise ratio (PSNR) of 23.4 dB, against at most 20.7 dB for four published models, and rank correlations of 0.56 to 0.67 with true SUVR in the composite cortex, an early-accumulation region and the striatum, against at most 0.24. In a second, cognitively unimpaired cohort with other plasma platforms (143 test pairs), it reaches 22.8 dB and 0.32 to 0.61, against at most 21.4 dB and 0.20. Its area under the curve for amyloid positivity is 0.91 and 0.82, against at most 0.63. Ablations show that plasma supplies the amyloid information and the network the image quality. Combining MRI with a blood test yields synthetic amyloid PET that is realistic and tracks burden across regions.

### 🤖 AI 总结

**一句话总结**：Amyloid positron emission tomography (PET) quantifies brain amyloid-$β$ as a standardized uptake value ratio (SUVR), but is costly and not widely available. Structural magnetic resonance imaging (MRI)...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, SUPRA, Synthesizing, Amyloid, PET, MRI, Plasma, Biomarkers

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33061v1) | [下载PDF](https://arxiv.org/pdf/2611.33061v1.pdf)

---

## [19. Spectrify: Framework for Hyperspectral Image Generation Using Computer Graphics](https://arxiv.org/abs/2611.33042v1)

**作者**：Yasin Mamedov, Daniil Vladimirov, Sofiia Dorogova 等 5 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-11-24

### 📄 论文摘要

Hyperspectral images (HSIs) record the full spectrum of light at every pixel, so projecting an HSI through a camera's spectral sensitivities gives that camera's RAW image, and one HSI can supply training data for hyperspectral reconstruction and camera-pipeline methods. Real HSIs, however, are slow and expensive to capture, and the largest datasets hold only about 1,000 images. High-level vision commonly replaces scarce real data with images rendered from 3D scenes. Low-level tasks, however, need physically correct spectra, which requires spectral rendering with a measured spectrum for every material in a scene, and existing spectral renderings cover only a handful of scenes, mostly with a simplified image formation model. We present Spectrify, a framework that converts 3D scene datasets into HSIs, together with a library of reflectance spectra labeled by material and compiled from close-range hyperspectral datasets and spectrophotometer measurements. In Spectrify, spectra follow the material: each object receives a physically based optical model and measured reflectance spectra or optical constants from its material category, each lamp an emission spectrum of its type and the sky a modeled daylight spectrum, and Mitsuba 3 path-traces the full light transport of each scene per wavelength. We show that a hyperspectral reconstruction network trained only on our synthetic HSIs generalizes to unseen real datasets better than networks trained on the largest real HSI datasets on most test sets, and that assigning spectra by material category instead of by color alone improves this transfer on every test set. RAW images projected from our HSIs are also useful training data for color constancy, performing on par with existing synthetic RAW generators. We release the 4,500 rendered HSIs, the code of Spectrify and its material-labeled reflectance library.

### 🤖 AI 总结

**一句话总结**：Hyperspectral images (HSIs) record the full spectrum of light at every pixel, so projecting an HSI through a camera's spectral sensitivities gives that camera's RAW image, and one HSI can supply train...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Spectrify, Framework, Hyperspectral, Image, Generation, Computer, Graphics, images

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33042v1) | [下载PDF](https://arxiv.org/pdf/2611.33042v1.pdf)

---

## [20. SHARPnP: Self-Supervised and Plug-and-Play Hyperspectral Super-Resolution from Real Noisy Unaligned Camera Measurements](https://arxiv.org/abs/2611.33032v1)

**作者**：Mohamad Jouni, Brayan Monroy, Jorge Bacca 等 4 位作者  
**分类**：cs.CV, eess.IV, eess.SP  
**发布时间**：2026-11-24

### 📄 论文摘要

Affordable snapshot hyperspectral cameras capture spectral images in a single exposure but suffer from limited spatial resolution and sensor noise. Low-cost RGB cameras provide fine visible details to guide NIR reconstruction, but introduce spatially varying cross-camera misalignment. Supervised fusion methods require relatively large datasets of clean, high-resolution hyperspectral images, are sensitive to sensor noise, and generalize poorly across new sensors. We introduce SHARPnP, an interpretable, flexible framework coupling registration and reconstruction for RGB-guided hyperspectral super-resolution from noisy, unaligned measurements without clean references. We adapt a pretrained registration model via a cross-view loss backpropagated through a fixed plug-and-play fusion module. Temporal and recorrupted pairs enable reference-free self-supervision on noisy inputs. At test time, we calibrate cross-camera radiometry and refine alignment. Plug-and-play fusion employs sequential three-band denoising. On the REAL benchmark, SHARPnP outperforms supervised fusion baselines at $4\times$, $8\times$, and $16\times$ on clean inputs and at $4\times$ under Gaussian noise ($σ=5/255, 10/255$). On native RGB-HSI snapshot measurements, it reconstructs all 51 VIS-NIR bands, beyond the conventional 31-band VIS setting, without high-resolution references.

### 🤖 AI 总结

**一句话总结**：Affordable snapshot hyperspectral cameras capture spectral images in a single exposure but suffer from limited spatial resolution and sensor noise. Low-cost RGB cameras provide fine visible details to...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SHARPnP, Self-Supervised, Plug-and-Play, Hyperspectral, Super-Resolution, Real, Noisy, Unaligned

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33032v1) | [下载PDF](https://arxiv.org/pdf/2611.33032v1.pdf)

---

## [21. GRAPE-Bench: When Vision Degrades, Does Video Reasoning Hold?](https://arxiv.org/abs/2611.33020v1)

**作者**：Ce Zhang, Junyi He, Tianshi Ming 等 18 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-24

### 📄 论文摘要

Despite strong performance on standard benchmarks, video reasoning models remain vulnerable to visual degradation, raising concerns about their reliability in safety-critical scenarios. Existing benchmarks address this concern in part by simulating visual degradation or probing model reasoning with challenging questions, leaving open how well models handle naturally degraded video and whether they can make the simpler judgments that matter for safe driving. To this end, we introduce GRAPE-Bench, which jointly evaluates video reasoning across visual degradation conditions and question difficulty. It combines a synthetic set spanning twelve corruption types across daily-life and driving videos with real-world footage of driving at night or in rain, snow, or fog. Each video is paired with three progressively challenging questions, from fundamental judgments with potential safety implications to demanding reasoning stress tests. Across open-weight and frontier models, we observe ranking reversals between synthetic and real-world conditions and level-specific weaknesses obscured by overall accuracy. Synthetic-data fine-tuning improves Qwen3.5-9B's real-world accuracy from 76.7% to 81.1%, while clean-privileged on-policy distillation reaches 80.4% in a separate reasoning-enabled setting. Through preference steering, we further demonstrate continuous control over a frozen model's trade-off between safety-relevant judgments and challenging reasoning, with little change in overall accuracy. Together, GRAPE-Bench provides a unified testbed for evaluating, improving, and controlling video reasoning under degraded visual conditions.

### 🤖 AI 总结

**一句话总结**：Despite strong performance on standard benchmarks, video reasoning models remain vulnerable to visual degradation, raising concerns about their reliability in safety-critical scenarios. Existing bench...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GRAPE-Bench, When, Vision, Degrades, Does, Video, Reasoning, Hold?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33020v1) | [下载PDF](https://arxiv.org/pdf/2611.33020v1.pdf)

---

## cs.LG

## [22. Reinforcement Learning Can Be Recovered From Its Own Rollouts](https://arxiv.org/abs/2611.33102v1)

**作者**：Jiayi Sheng, Jingwen Gu, Guanning Zeng 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-24

### 📄 论文摘要

Broadly speaking, reinforcement learning (RL) post-training converts compute into model capabilities by training on model-generated data. Typically, the rollouts are discarded after each update, and the knowledge acquired during RL resides in the model weights. In this work, we investigate how much of this knowledge is retained in the rollouts themselves. A natural first attempt is to replay the original RL algorithm on archived rather than freshly generated rollouts, but this leads to catastrophic collapse. We provide a simple explanation for this phenomenon, which in turn suggests a remedy: maximum likelihood on the archived rollouts. Surprisingly, starting from the same base model and replaying the rollouts in the order in which they were generated, without any distinction between correct and incorrect responses, is sufficient to recover the performance of online RL. In fact, a single maximum likelihood update per rollout batch closely tracks the entire learning curve of online RL. Furthermore, maximum likelihood on the rollouts of the last few RL steps often suffices to recover the final model's performance. This suggests that much of the compute invested in RL goes into discovering an improved sampling distribution rather than learning it from samples.

### 🤖 AI 总结

**一句话总结**：Broadly speaking, reinforcement learning (RL) post-training converts compute into model capabilities by training on model-generated data. Typically, the rollouts are discarded after each update, and t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Be, Reinforcement, Learning, Can, Recovered, Its, Own, Rollouts

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33102v1) | [下载PDF](https://arxiv.org/pdf/2611.33102v1.pdf)

---

## [23. U-Statistics-Powered LLM Reasoning](https://arxiv.org/abs/2611.33064v1)

**作者**：Shijin Gong, Kai Ye, Victor Chernozhukov 等 5 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-11-24

### 📄 论文摘要

Since its introduction by DeepSeek, group relative policy optimization (GRPO) has been widely adopted for training large reasoning models and agents, spurring a proliferation of its variants. Yet the group size, a crucial hyperparameter in these GRPO-type algorithms, remains largely chosen by trial and error. Exploiting the U-statistic structure of GRPO's policy gradient, we recast the selection of the group size as a classical statistical problem of variance ratio estimation. This problem is particularly challenging when the denominator of the ratio is small, rendering naive plug-in estimators unstable. To address this challenge, we propose a pessimistic ratio estimator that accounts for the denominator's estimation uncertainty. We characterise the statistical properties of this estimator across three sample-size regimes. Empirically, using %a jackknife-based pessimistic rule on synthetic tasks from Reasoning Gym and real-world benchmarks covering both mathematical reasoning and code generation, we show that our adaptive group size selection reduces the mean squared error of the resulting policy gradient and improves policy optimisation over fixed-group-size baselines, with modest additional computational cost.

### 🤖 AI 总结

**一句话总结**：Since its introduction by DeepSeek, group relative policy optimization (GRPO) has been widely adopted for training large reasoning models and agents, spurring a proliferation of its variants. Yet the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, U-Statistics-Powered, Reasoning, Since, its, introduction, DeepSeek, group

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33064v1) | [下载PDF](https://arxiv.org/pdf/2611.33064v1.pdf)

---

## [24. Understanding Clipping In Zeroth-Order Optimization](https://arxiv.org/abs/2611.33062v1)

**作者**：Saket Gollapudi, Elisa Bertino, Sewoong Oh  
**分类**：cs.LG  
**发布时间**：2026-11-24

### 📄 论文摘要

Zeroth-order optimization has emerged as a resource-efficient alternative to Stochastic Gradient Descent (SGD) when fine-tuning LLMs, thanks to the inherent low dimensionality of the loss landscape. It relies on a two-point estimate of the gradient that only accesses the function value and not the gradient, bypassing the resource-heavy backpropagation. Recently, it was accidentally discovered that per-sample clipping can improve the performance of the trained model, while running a differentially private version of zeroth-order optimization \cite{zhang2024dpzero} with a very large privacy parameter $ε$ (corresponding to very little privacy). In this paper, we systematically investigate this phenomenon and demonstrate that ($i$) the optimal choice of learning rate $η$ is inversely proportional to the clipping threshold $c$, satisfying $ηc =$ constant; ($ii$) clipping drives the zeroth-order optimization to a different solution with higher test accuracy; and ($iii$) this phenomenon is only observed with per-sample clipped zeroth-order optimization and not other zeroth-order alternatives that also provide robust estimates of the gradient. Further analyses with artificially injected label noise reveals that clipping leads to more robust predictions, which stems from the implicit down weighting of hard-to-fit training examples. Our code is available at https://github.com/SewoongLab/ClipZero

### 🤖 AI 总结

**一句话总结**：Zeroth-order optimization has emerged as a resource-efficient alternative to Stochastic Gradient Descent (SGD) when fine-tuning LLMs, thanks to the inherent low dimensionality of the loss landscape. I...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Understanding, Clipping, Zeroth-Order, Optimization, has, emerged, resource-efficient

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33062v1) | [下载PDF](https://arxiv.org/pdf/2611.33062v1.pdf)

---

## [25. Local Indices Are Not Enough: Synchrony and Global Information in Bandit Algorithms](https://arxiv.org/abs/2611.33056v1)

**作者**：Aakash Gore, Shivaram Kalyanakrishnan  
**分类**：cs.LG  
**发布时间**：2026-11-24

### 📄 论文摘要

Standard index-based stochastic bandit algorithms such as KL-UCB and Thompson Sampling achieve optimal $O(\log T)$ regret over a horizon $T$. The former uses the global timestep to construct each arm's index, while the latter samples each arm's belief distribution at every timestep. The necessity of global information and synchronous index updates for achieving optimal regret has not been examined yet. In this paper, we investigate the fundamental limits of asynchronous local index algorithms---those that recalculate an arm's index only upon pulling it, using solely that arm's own reward history and a local randomness budget. We prove that no such algorithm can achieve $O(\log T)$ regret across all bandit instances. We then analyse the functional equations arising from asynchronous updates, and show that the achievable regret lies in a sub-polynomial, super-polylogarithmic regime. We propose an asynchronous local index policy whose regret upper bound also lies in this regime. Turning to synchronous local algorithms, which sample every arm's index at all timesteps as in Thompson Sampling, we show that a locally determined randomness budget per arm suffices to retain $O(\log T)$ regret, demonstrating that synchrony, albeit with some randomness, is essential to the optimality of Thompson Sampling.

### 🤖 AI 总结

**一句话总结**：Standard index-based stochastic bandit algorithms such as KL-UCB and Thompson Sampling achieve optimal $O(\log T)$ regret over a horizon $T$. The former uses the global timestep to construct each arm'...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Local, Indices, Not, Enough, Synchrony, Global, Information, Bandit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33056v1) | [下载PDF](https://arxiv.org/pdf/2611.33056v1.pdf)

---

## [26. When Is Product Decoding of ECOC MAP-Consistent? Pair Structure and the n-vs-Rest Codes](https://arxiv.org/abs/2611.33044v1)

**作者**：Gendo Kumoi  
**分类**：cs.LG, cs.IT  
**发布时间**：2026-11-24

### 📄 论文摘要

Error-Correcting Output Codes (ECOC) combine binary classifiers by the sum decoder, which totals probabilities, or the product decoder, which totals log-likelihoods. In the noiseless setting, where the binary classifiers output the true posteriors, we ask on which code matrices each decoder always agrees with the Bayes-optimal (MAP) class. For the sum decoder the answer is known: the code must be equidistant (James and Hastie, 1998). We answer the question for the product decoder. Two classes are compared through the votes of the columns on which they differ: the sum decoder decides by their sample mean, the product decoder by an M-estimator with influence function artanh, and each vote is the MAP margin plus a bias determined by the other classes alone. Our main theorem states that the product decoder is MAP-consistent if and only if, for every class pair, the columns on which the two classes differ are matched with the columns obtained by swapping the two classes (or their complements), and equivalently if and only if the code is a union of n-vs-Rest codes. Efficient equidistant codes are therefore excluded: Hadamard codes ($M\ge 8$), which meet the Plotkin bound with $M-1$ columns, have no such pairs, and for the Sylvester type the reversal margin can be at least a constant 0.0182 independent of $M$. All theorems are machine-checked in Lean 4. On six real datasets with estimated probabilities, the product decoder is slightly more accurate when each column is calibrated, and the sum decoder is better when the calibration error differs across columns; in either case the decoders disagree only near ties.

### 🤖 AI 总结

**一句话总结**：Error-Correcting Output Codes (ECOC) combine binary classifiers by the sum decoder, which totals probabilities, or the product decoder, which totals log-likelihoods. In the noiseless setting, where th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, When, Product, Decoding, ECOC, MAP-Consistent?, Pair, Structure

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33044v1) | [下载PDF](https://arxiv.org/pdf/2611.33044v1.pdf)

---

## [27. Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming?](https://arxiv.org/abs/2611.33031v1)

**作者**：Steffen Urban  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-11-24

### 📄 论文摘要

We give four large language models (LLMs) of the Claude family the complete weights of a 20k-parameter CIFAR-10 CNN as text and ask them to produce a 4-bit network without tools, data or the ability to run inference. Standard round-to-nearest (RTN) quantization to 4 bit lowers the test accuracy from 81.4% to 60.4%. We design four evaluation protocols that differ in the input and task description given to the LLMs and analyze their responses. In the first two protocols the LLMs are given the float and the 4-bit RTN network and are told that the accuracy has dropped significantly. In the last two they receive only the float network and the task to quantize it, which tests whether they apply an optimization on their own or fall back to plain RTN. Our analysis shows that a frontier LLM can recover most of the lost accuracy. Given one answer per layer, Opus 5.5 raises the accuracy of the 4-bit network to 77.95% by balancing the rounding errors within each 3x3 kernel, reasoning over the integer weights without tools. This is 3.5 pp below the float network and 2.8 pp below AdaRound, which learns the rounding from calibration data. Given only the float network, the LLMs name error-cancelling corrections but do not apply them and fall back to plain RTN, at most with mildly clipped scales, which still lifts Fable 5.2's quantized network to 70.0%. We analyze in detail what the LLMs did and why it works. Code and prompts can be found at https://github.com/urbste/weight-space-programming-ptq

### 🤖 AI 总结

**一句话总结**：We give four large language models (LLMs) of the Claude family the complete weights of a 20k-parameter CIFAR-10 CNN as text and ask them to produce a 4-bit network without tools, data or the ability t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Can, Frontier, Repair, Quantized, Network, Tool-Free, Weight-Space

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33031v1) | [下载PDF](https://arxiv.org/pdf/2611.33031v1.pdf)

---

## [28. Score-Based Diffusion for Hypergraph Signals in the t-Spectral Domain](https://arxiv.org/abs/2611.33026v1)

**作者**：Zhiyuan Dong, Carlos Mundo-Levano, Daniel L. Lau 等 4 位作者  
**分类**：cs.LG, eess.SP  
**发布时间**：2026-11-24

### 📄 论文摘要

We introduce the first score-based generative model for signals on a fixed hypergraph, formulated in the spectral domain of t-product hypergraph signal processing (t-HGSP). The naive tensor heat semigroup is ill-posed, since after palindromic symmetrization the spectral slices of the Laplacian tensor are no longer positive semidefinite. A per-mode frequency shift repairs it, yielding a forward Ornstein-Uhlenbeck diffusion that decouples per (eigenmode, slice) pair with closed-form marginals, exact score targets, and an exactly isotropic stationary law. A lightweight slice-conditioned denoiser is trained on the resulting real spectral grid. Sampling combines its score on data-active modes with the closed-form score elsewhere, which proves essential for stability at scale. A closed cosine-form observation operator turns missing-node recovery into linear-Gaussian guidance with stabilized posterior sampling. On hypergraphs of up to 500 nodes, our model beats a clique-expansion baseline by margins growing from $2\times$ to $27\times$ in covariance error, matches the graph-spectral statistics of the data better than the graph-basis model itself, and reaches the finite-sample estimation floor on data rotated off the t-spectral axes. Posterior sampling reduces missing-node NMSE to 0.28-0.64 (classical baselines 0.87-1.1) at conservative coverage, and cuts the framework's own denoising baseline by up to $3.6\times$.

### 🤖 AI 总结

**一句话总结**：We introduce the first score-based generative model for signals on a fixed hypergraph, formulated in the spectral domain of t-product hypergraph signal processing (t-HGSP). The naive tensor heat semig...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, We, Score-Based, Hypergraph, Signals, t-Spectral, Domain, introduce

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33026v1) | [下载PDF](https://arxiv.org/pdf/2611.33026v1.pdf)

---

## [29. Best Arm Identification with Unknown Post-Action Context Distribution](https://arxiv.org/abs/2611.33024v1)

**作者**：Amir Mohammad Abouei, Mohammad Shahverdikondori, Emad Emamjomeh 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-24

### 📄 论文摘要

We study best arm identification (BAI) with post-action context in the fixed-confidence setting. After choosing an action, the learner observes a post-action context together with a reward whose distribution depends only on this context. Incorporating such intermediate information can substantially reduce the sample complexity of identifying the best arm. While Shahverdikondori et al. (2026a) analyzed the case where the distribution of contexts given actions is known, we address the more challenging and practically relevant case where this distribution is unknown. We derive an instance-dependent sample complexity lower bound and propose a Track-and-Stop algorithm that matches it asymptotically with access to an optimization oracle. Our stopping rule uses a new concentration inequality that jointly controls uncertainty in the context distributions and reward means, removing the factor of two incurred by separate concentration bounds. Implementing the algorithm generally requires solving nonconvex optimization problems. We propose a convex relaxation with instance-dependent approximation guarantees, including asymptotic tightness on hard Gaussian instances. Experiments demonstrate that exploiting post-action context reduces the sample complexity relative to baselines that ignore it, even when the context distributions are unknown.

### 🤖 AI 总结

**一句话总结**：We study best arm identification (BAI) with post-action context in the fixed-confidence setting. After choosing an action, the learner observes a post-action context together with a reward whose distr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Best, Arm, Identification, Unknown, Post-Action, Context, Distribution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33024v1) | [下载PDF](https://arxiv.org/pdf/2611.33024v1.pdf)

---

## [30. PAC-style Bounds on the Conditional Validity of Conformal Predictors](https://arxiv.org/abs/2611.33023v1)

**作者**：Nicolo Colombo  
**分类**：cs.LG  
**发布时间**：2026-11-24

### 📄 论文摘要

Conformal prediction sets are guaranteed to be marginally valid over the attribute space, but local coverage can diverge from the user-defined target $1-α$. Constructing conditionally valid prediction sets with finite calibration data is impossible for a general data-generating distribution. We derive PAC-type probabilistic lower bounds on the input-conditional coverage of any conformal predictor, without assumptions on the data distribution. They are based on the Markov and Cantelli inequalities and adapt to both calibration-marginal and calibration-conditional setups. A tighter, model-dependent Cantelli bound depends on the variance of the conditional coverage and is estimable from data using a fully non-asymptotic Hoeffding argument. The results suggest conditional-coverage variance as a scalable and theoretically motivated empirical measure of conditional validity.

### 🤖 AI 总结

**一句话总结**：Conformal prediction sets are guaranteed to be marginally valid over the attribute space, but local coverage can diverge from the user-defined target $1-α$. Constructing conditionally valid prediction...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, PAC-style, Bounds, Conditional, Validity, Conformal, Predictors, prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.33023v1) | [下载PDF](https://arxiv.org/pdf/2611.33023v1.pdf)

---

