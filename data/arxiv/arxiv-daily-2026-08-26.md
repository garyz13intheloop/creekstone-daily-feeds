# arXiv AI 论文日报 | 2026-08-26

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (9 篇)
- [cs.AI](#csAI) (9 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.CL](#csCL) (5 篇)

---

## cs.AI

## [1. Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses](https://arxiv.org/abs/2608.24876v1)

**作者**：Zhaochen Yu, Yingcheng Wu, Zhenfei Yin 等 8 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-08-25

### 📄 论文摘要

Recursive self-improvement (RSI) remains hard in long-horizon tasks, where growing histories obscure the task state and misalign skill invocation. We introduce Recuris, a recursive Experiential-Working Memory architecture for long-horizon agent harnesses, in which Working Memory tracks task progress and guides skill selection from Experiential Memory, grounding skill use in current needs rather than the full history. This coupling also turns execution into structured evidence that localizes failures to specific memory components. Across tasks, a fixed Meta-Agent turns that evidence into localized, validation-gated updates to Skill Memory that reshape execution and yield new evidence, forming a bounded recursive memory-evolution loop. Across four long-horizon benchmarks and ten models, Recuris improves task success in 35 of the 37 completed model-benchmark pairs, carrying frontier models to SOTA-level task success: on tau-bench it adds +17.8 points to GPT-5.6 Sol and +15.6 to Claude Opus 5, taking Opus 5 to 87.9%, and +16.6/+13.5 points on Qwen3.6-27B/35B on SkillFlow. The advantage widens as the interaction horizon grows, to +32.2 points on the longest tasks, and common long-horizon failures fall by up to 80%. These results position recursively evolving memory as a scalable foundation for RSI, enabling agents to continuously transform accumulated experience into increasingly effective long-horizon behavior. Code: https://github.com/Gen-Verse/Recuris

### 🤖 AI 总结

**一句话总结**：Recursive self-improvement (RSI) remains hard in long-horizon tasks, where growing histories obscure the task state and misalign skill invocation. We introduce Recuris, a recursive Experiential-Workin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Recursive, Experiential-Working, Memory, Evolution, Long-Horizon, Harnesses, self-improvement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24876v1) | [下载PDF](https://arxiv.org/pdf/2608.24876v1.pdf)

---

## [2. FedV-KGQA: Multi-Hop Question Answering over Vertically Partitioned Knowledge Graphs](https://arxiv.org/abs/2608.24846v1)

**作者**：Md Saikat Islam Khan Bappy, Oshani Seneviratne  
**分类**：cs.AI  
**发布时间**：2026-08-25

### 📄 论文摘要

Real-world data for knowledge graph question answering is often distributed across different organizations due to governance and data sovereignty constraints. While centralized systems exist, they cannot answer multi-hop questions when the required facts are split across vertically partitioned silos. In this paper, we propose FedV-KGQA, a framework for multi-hop reasoning over knowledge graphs in which organizations share entities but own disjoint sets of relations. Our approach combines local graph enrichment and knowledge graph embeddings to ensure raw triples and relation parameters never leave each silo, establishing a structural data boundary without requiring centralized graph access. We further introduce a topic entity anchoring mechanism that grounds questions in the correct graph neighborhood without any runtime inter-silo communication. We evaluate 12 model configurations across three benchmarks and show that FedV-KGQA performs strongly, remains close to centralized performance, generalizes to 3-hop reasoning, and is robust to embedding perturbations.

### 🤖 AI 总结

**一句话总结**：Real-world data for knowledge graph question answering is often distributed across different organizations due to governance and data sovereignty constraints. While centralized systems exist, they can...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FedV-KGQA, Multi-Hop, Question, Answering, over, Vertically, Partitioned, Knowledge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24846v1) | [下载PDF](https://arxiv.org/pdf/2608.24846v1.pdf)

---

## [3. A Dual-Dimensional LLM Framework for Automated Item Incidental Content Similarity Analysis in Large-Scale Assessments](https://arxiv.org/abs/2608.24825v1)

**作者**：Jing Huang, Jihong Zhang, Hua-Hua Chang  
**分类**：cs.AI  
**发布时间**：2026-08-25

### 📄 论文摘要

The rapid expansion of large-scale assessments and the growing adoption of automatic item generation have intensified concerns about incidental content redundancy, where construct-irrelevant elements such as wording or contextual framing become unintentionally repetitive across items. Traditional similarity metrics like BLEU or cosine similarity, often fail to capture the nuanced structural and semantic layers that drive perceived redundancy simultaneously. This study proposes a dual-dimensional framework for Automated Item Similarity Analysis (AISA) powered by Large Language Models (LLMs), operationalizing similarity through Structured Decomposition and Semantic Relatedness. Psychometric validation indicates that LLM-derived metrics align more closely with indicators of construct-irrelevant local dependence and yield more coherent item parameter groupings than traditional text-based measures. The framework is further evaluated through its application in Computerized Adaptive Testing (CAT). Simulations reveal that incorporating LLM-based similarity constraints into item selection improves estimation stability and reduces bias with minimal efficiency trade-offs, outperforming constraints based on conventional metrics. These findings highlight the potential of LLM-powered AISA to support scalable bank curation, content-aware test assembly, and experience-sensitive adaptive testing across diverse assessment contexts.

### 🤖 AI 总结

**一句话总结**：The rapid expansion of large-scale assessments and the growing adoption of automatic item generation have intensified concerns about incidental content redundancy, where construct-irrelevant elements ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Dual-Dimensional, Framework, Automated, Item, Incidental, Content, Similarity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24825v1) | [下载PDF](https://arxiv.org/pdf/2608.24825v1.pdf)

---

## [4. Constrained Entity Selection under Partial Knowledge for LLM-Based Knowledge Graph QA](https://arxiv.org/abs/2608.24824v1)

**作者**：Emanuel Kitzelmann  
**分类**：cs.AI  
**发布时间**：2026-08-25

### 📄 论文摘要

Large language models are increasingly used for knowledge graph question answering (KGQA), but can fail to correctly ground answers in the underlying graph. Current approaches to LLM-based KGQA either rely on full semantic parsing into executable queries such as SPARQL, which is brittle in practice due to complex schemas or incompleteness of real-world KGs, or on LLM-reasoning and answer generation over KGs, which can be more robust but lacks formal guarantees. In this work, we study a complementary setting in which \emph{candidate} answers are generated by an LLM-based system and subsequently verified using lightweight symbolic constraints derived from the question. We introduce \emph{Constrained Entity Selection under Partial Knowledge (CES-PK)}, a problem formulation that focuses on eliminating invalid answers and providing symbolic support for valid ones without requiring construction of executable logical forms. To account for incomplete KGs, we employ a three-valued constraint semantics (\emph{satisfied, violated, unknown}) that avoids incorrect rejections under open-world assumptions. To demonstrate the effects of our method, we instantiate this framework over the Hetionet biomedical knowledge graph and evaluate the impact of type, relation, and exclusion constraints. Experiments show that precision improves by filtering invalid candidates, while recall is preserved due to retaining candidates whose constraints are not explicitly violated. Satisfied constraints provide additional positive symbolic evidence to rank remaining candidates.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly used for knowledge graph question answering (KGQA), but can fail to correctly ground answers in the underlying graph. Current approaches to LLM-based KGQA either...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Constrained, Entity, Selection, under, Partial, Knowledge, LLM-Based, Graph

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24824v1) | [下载PDF](https://arxiv.org/pdf/2608.24824v1.pdf)

---

## [5. Strictly Causal Streaming Video Anomaly Detection with a Theoretically-Grounded State-Space Core](https://arxiv.org/abs/2608.24810v1)

**作者**：Yogesh Kumar  
**分类**：cs.AI  
**发布时间**：2026-08-25

### 📄 论文摘要

Recent work has applied Mamba style state space models (SSMs) to video anomaly detection, yet existing approaches still rely on buffering clips or windows internally, lack a theoretical account of how temporal memory relates to detection latency, and benchmark efficiency only through GPU throughput rather than the edge hardware these methods are intended to target. We introduce a strictly causal streaming anomaly detector whose fixed size state is updated in O(1) time and memory per incoming frame, with no lookahead and no clip buffering. Its temporal core is a diagonal linear state space recurrence with an input and state dependent decay gate, trained self supervised through causal next embedding prediction on a frozen visual backbone. We derive a closed form relationship between the recurrence decay spectrum and both detection delay and the shortest anomaly it can reliably capture, then validate empirically on UCSD Ped2 and CUHK Avenue. The settling delay bound predicted from the learned base decay (57 to 59 frames) sits far above the measured detection delay (1.6 and 18.4 frames), showing that the event boundary gate, not the base decay, governs responsiveness. We further report end to end latency and throughput measured directly on Apple M3 Pro hardware, 0.74 ms and 0.77 ms per frame (over 1300 FPS), rather than simulated GPU numbers. With an untuned initial configuration the method reaches 67.9 percent and 70.2 percent frame level AUC on Ped2 and Avenue, trailing prior non causal SSM baselines in accuracy. Ablations over decay rate, state size, and gating reveal that the gate contribution is dataset size dependent, hurting accuracy on the smaller Ped2 training set but helping on the larger Avenue one. Closing this accuracy gap and extending evaluation to a third, larger benchmark are immediate next steps.

### 🤖 AI 总结

**一句话总结**：Recent work has applied Mamba style state space models (SSMs) to video anomaly detection, yet existing approaches still rely on buffering clips or windows internally, lack a theoretical account of how...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Strictly, Causal, Streaming, Video, Anomaly, Detection, Theoretically-Grounded, State-Space

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24810v1) | [下载PDF](https://arxiv.org/pdf/2608.24810v1.pdf)

---

## [6. StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments](https://arxiv.org/abs/2608.24804v1)

**作者**：Esakkivel Esakkiraja, Denis Akhiyarov, Vikas Yadav 等 7 位作者  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-08-25

### 📄 论文摘要

We present StarHarness, a framework for evolving environment-specific agent harnesses while keeping model weights fixed. The evolved harness can include prompt and task framing, tool interfaces, skills, MCP-backed providers, subagent structure, and agent-loop configuration. StarHarness constructs a compact evolution pool by stratifying tasks according to baseline failure behavior, separates proposer-visible search tasks from proposer-hidden selection tasks, and reserves held-out tasks for evaluating generalization. Across ITBench SRE, EnterpriseOps-Gym ITSM, and AutomationBench Finance, harness evolution improves full-benchmark performance by 20-35 percentage points over the default harness after 4-12 accepted changes per environment. These gains persist on tasks excluded from evolution and transfer without re-evolution across GPT and Qwen model families. Trace analysis links the improvements to interface repairs, environment conventions, and operational knowledge that compresses search, with fewer false-positive diagnoses and shorter trajectories in several settings. StarHarness therefore offers a practical way to reduce persistent model-environment mismatch in tool-rich enterprise tasks.

### 🤖 AI 总结

**一句话总结**：We present StarHarness, a framework for evolving environment-specific agent harnesses while keeping model weights fixed. The evolved harness can include prompt and task framing, tool interfaces, skill...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, StarHarness, Evolving, Harnesses, Stratified, Search, Enterprise, Environments

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24804v1) | [下载PDF](https://arxiv.org/pdf/2608.24804v1.pdf)

---

## [7. Right Diagnoses, Decorative Reasoning:A Perturbation Audit of Medical Chain-of-Thought](https://arxiv.org/abs/2608.24790v1)

**作者**：Mengzhu Xu, Jifan Gao, Xia Jiang 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-25

### 📄 论文摘要

Clinicians read chain-of-thought (CoT) rationales as evidence of medical reasoning, but whether the visible chain plays that role is rarely tested. General-domain CoT-faithfulness probes ignore clinical cost, and medical LLM evaluations treat the chain as a black box. We close this gap with a medical perturbation audit: a 30-operator battery edits both the chain and the question with clinically motivated operators (severity reversal, negation flip, demographic swap, evidence ablation), paired with a chain-update times answer-flip joint analysis that classifies each model by its failure mode. Applied to 14 LLMs on four medical QA benchmarks, three independent tests converge: the Chain-Decoupling Rate (CDR; chain does not register the edit and the answer does not flip) is 72.9% panel-wide on clinically meaningful destructive edits, chain corruption leaves accuracy unchanged, and removing CoT prompting does not reduce accuracy. Two board-certified clinicians re-annotate N=197 perturbed questions; 98.5% leave the gold defensible. The pattern holds across medical and reasoning fine-tuning and scale; on the closed-source tier, where the chain text is unavailable, the answer-side signals are consistent with the same decoupling. Our framework and CDR provide a reusable yardstick for auditing whether medical CoT is faithful or merely documentation.

### 🤖 AI 总结

**一句话总结**：Clinicians read chain-of-thought (CoT) rationales as evidence of medical reasoning, but whether the visible chain plays that role is rarely tested. General-domain CoT-faithfulness probes ignore clinic...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Right, Diagnoses, Decorative, Reasoning, Perturbation, Audit, Medical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24790v1) | [下载PDF](https://arxiv.org/pdf/2608.24790v1.pdf)

---

## [8. StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-Utility Balancing](https://arxiv.org/abs/2608.24777v1)

**作者**：Zhijie Zheng, Yu Li, Chen Qian 等 8 位作者  
**分类**：cs.AI, cs.CR  
**发布时间**：2026-08-25

### 📄 论文摘要

LLM-based agents can interact with external environments through tool invocation, but this capability also introduces security risks such as file modification, information leakage, and unauthorized actions. Existing guardrails often evaluate completed trajectories, leaving pre-execution monitoring of step-level actions underexplored. We propose StepGuard, a step-level guard model that can audit completed agent trajectories and check tool actions before they are executed. To train StepGuard, we introduce StepGen, an automatic data engine that generates safe and unsafe trajectories with the same context but different actions at the risky step. To further reduce over-defense and under-defense, we propose Balance-GRPO, which dynamically balances learning between safe and unsafe actions based on their observed accuracy. Experiments show that StepGuard achieves the highest average accuracy among open-weight guard models, with performance comparable to GPT-5.4. When used to guard agents on AgentDojo and AgentDyn, StepGuard reduces mean attack success rate by 77.3% relative to the no-guard setting, while mean utility drops by only 2.8 percentage points.

### 🤖 AI 总结

**一句话总结**：LLM-based agents can interact with external environments through tool invocation, but this capability also introduces security risks such as file modification, information leakage, and unauthorized ac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：StepGuard, Learning, Step-Level, Guardrails, Scalable, Supervision, Safety-Utility, Balancing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24777v1) | [下载PDF](https://arxiv.org/pdf/2608.24777v1.pdf)

---

## [9. Evidence Blindness in Direct Corpus Interaction: Persistent Navigation with AtlasNav](https://arxiv.org/abs/2608.24764v1)

**作者**：Hongyu Guo, Zhiyu Zheng, Zhao Cao  
**分类**：cs.AI  
**发布时间**：2026-08-25

### 📄 论文摘要

Large language model agents are moving beyond conventional retrieval-augmented generation toward direct interaction with external corpora. Direct Corpus Interaction (DCI) keeps the full corpus accessible, yet reachable evidence can remain unusable under finite interaction budgets. Required evidence may fail to surface, a surfaced supporting document may remain unopened, or an opened document may fail to expose its decisive fragment. We call this progressive silent loss Evidence Blindness and quantify it through stage-wise evidence realization. Within the DCI paradigm, raw interaction adds little reusable corpus organization, while dynamic-workspace methods reconstruct a query-conditioned interaction space from each query and trajectory. In both cases, useful structure is recovered largely online. We instead formulate large-scale agentic search as finite-budget navigation over reusable corpus structure. We introduce AtlasNav, a persistent multi-view corpus-navigation framework that retains direct corpus interaction but organizes the corpus once into a Corpus Atlas, allowing each query to navigate adaptively rather than reconstruct shared structure. On BrowseComp-Plus, AtlasNav achieves 92.05% strict accuracy while reducing recorded online inference cost by 30.21% relative to the prior dynamic-workspace state of the art. Under matched budgets, it realizes the complete required evidence earlier and approaches the same model's evidence-supplied empirical reference more rapidly. The same representation principle remains effective under PhantomWiki's distinct corpus organization and controlled 10K-1M scaling, and transfers competitively to heterogeneous enterprise knowledge. These results show that agentic search depends not only on accessible evidence, but also on how the corpus is represented so that limited interaction becomes effective navigation.

### 🤖 AI 总结

**一句话总结**：Large language model agents are moving beyond conventional retrieval-augmented generation toward direct interaction with external corpora. Direct Corpus Interaction (DCI) keeps the full corpus accessi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Evidence, Blindness, Direct, Corpus, Interaction, Persistent, Navigation, AtlasNav

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24764v1) | [下载PDF](https://arxiv.org/pdf/2608.24764v1.pdf)

---

## cs.CL

## [10. Structurally-bounded Agentic Graph Exploration for Evidence-Grounded Scholarly DeepSearch](https://arxiv.org/abs/2608.24809v1)

**作者**：Rima Hazra, Sayan Layek, Somnath Banerjee 等 5 位作者  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-08-25

### 📄 论文摘要

We present Crase, a bounded and inspectable alternative to deep research agents for scholarly search. Instead of an open-ended search loop, Crase queries a search engine once for seed papers, expands them along their 1.5-hop citation neighborhood, prunes citation edges whose claims lack entailment support, and ranks the remaining papers with a recency-aware random walk. This makes the candidate set, the reason each paper is kept, and the stopping condition explicit and fixed before inference. On LitSearch and one further benchmarks over a 500K-paper arXiv corpus, Crase outperforms deep research agents built on proprietary models by up to 3$\times$ recall@50 at roughly a third of the cost.

### 🤖 AI 总结

**一句话总结**：We present Crase, a bounded and inspectable alternative to deep research agents for scholarly search. Instead of an open-ended search loop, Crase queries a search engine once for seed papers, expands ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Structurally-bounded, Agentic, Graph, Exploration, Evidence-Grounded, Scholarly, DeepSearch

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24809v1) | [下载PDF](https://arxiv.org/pdf/2608.24809v1.pdf)

---

## [11. Linear Probing Provides Robust and Efficient Detection of Machine-Generated Text](https://arxiv.org/abs/2608.24780v1)

**作者**：Gerrit Quaremba, Hanqi Yan, Elizabeth Black 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-25

### 📄 论文摘要

Distinguishing machine-generated text (MGT) from human-written text (HWT) becomes increasingly important due to potential misuse. However, most supervised detectors often degrade out-of-domain (OOD) and require large, diverse training sets. In this work, we analyze the linearity and quality of MGT representations and show that simple linear probes outperform a wide range of detectors while being substantially more sample-efficient. We first show that MGT and HWT latent representations are linearly separable in low-dimensional space, and provide a plausible explanation for this separability through systematic differences in their representation quality. Motivated by these insights, we train two variants of simple linear probes and evaluate them across 4 benchmarks against 16 baselines. Probes consistently improve OOD detection (+11 AUC), requiring solely ${<}100$ samples to reach near-peak performance. We show that this transferability arises because probes recover a shared latent MGT direction that generalizes across diverse settings. Finally, we demonstrate that probing vectors capture a continuous spectrum of ``machineness'', highlighting their potential for fine-grained estimation of AI-edited text. Overall, our work provides insights into latent-space differences between MGT and HWT and demonstrates the potential of linear probes as as robust and sample-efficient MGT detectors. We release our code on~\href{https://github.com/gerritq/mgt_probes}{github}.

### 🤖 AI 总结

**一句话总结**：Distinguishing machine-generated text (MGT) from human-written text (HWT) becomes increasingly important due to potential misuse. However, most supervised detectors often degrade out-of-domain (OOD) a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Linear, Probing, Provides, Robust, Efficient, Detection, Machine-Generated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24780v1) | [下载PDF](https://arxiv.org/pdf/2608.24780v1.pdf)

---

## [12. ExpConCAD: Experience-Guided Text-to-CAD Generation from Shape Descriptions with Implicit Spatial Constraints](https://arxiv.org/abs/2608.24760v1)

**作者**：Jingyao Liu, Jinkang Tang, Chen Huang 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-25

### 📄 论文摘要

Text-to-CAD aims to generate executable CAD programs from natural-language descriptions. However, real-world descriptions are often underspecified and omit critical spatial constraints required for valid CAD construction, a challenge that has been largely overlooked by existing methods. In this paper, we argue that missing spatial constraints should be inferred with respect to the underlying construction structure and informed by reusable design experience. Based on this insight, we propose ExpConCAD, an experience-enhanced framework for implicit spatial constraint completion. ExpConCAD first recovers the intended construction structure and constraint scopes, then retrieves relevant constraint-completion experience for similar scopes to complete the missing spatial constraints, and finally generates executable CadQuery programs. Extensive experiments demonstrate the effectiveness of ExpConCAD and provide insights into the role of construction structure understanding and experience memory in spatial constraint completion. Our code is available at: https://github.com/Hotjiashell/ExpConCAD.

### 🤖 AI 总结

**一句话总结**：Text-to-CAD aims to generate executable CAD programs from natural-language descriptions. However, real-world descriptions are often underspecified and omit critical spatial constraints required for va...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ExpConCAD, Experience-Guided, Text-to-CAD, Generation, Shape, Descriptions, Implicit, Spatial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24760v1) | [下载PDF](https://arxiv.org/pdf/2608.24760v1.pdf)

---

## [13. The RAT: A Unified Bayesian Model for RAG Evaluation](https://arxiv.org/abs/2608.24753v1)

**作者**：Pius von Däniken, Felix Matthias Saaro, Mark Cieliebak 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-25

### 📄 论文摘要

Evaluating Retrieval-Augmented Generation (RAG) systems requires assessing not only end-to-end correctness but also how individual components interact and how errors propagate through the pipeline. We introduce a Bayesian evaluation framework that jointly models retrieval success, abstention behavior, and answer correctness, factorized according to the pipeline's information flow. The model distinguishes task success. Whether the user received a correct answer (from generator success) and whether the generator behaved appropriately given the retrieval outcome. We apply the framework to 27 RAG configurations across three datasets, three retrievers, and three generators, and show that the conditional decomposition reveals substantial behavioral differences between systems that appear equivalent under marginal metrics. We further analyze the annotation allocation problem, demonstrating that retrieval-success annotations are more informative than task-success annotations for estimating policy adherence, and provide an information-theoretic explanation for this asymmetry. Finally, we extend the model to incorporate LLM-as-a-judge annotations as calibrated noisy observations, enabling practitioners to combine limited human judgments with cheaper automated assessments within a unified probabilistic model.

### 🤖 AI 总结

**一句话总结**：Evaluating Retrieval-Augmented Generation (RAG) systems requires assessing not only end-to-end correctness but also how individual components interact and how errors propagate through the pipeline. We...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RAG, RAT, Unified, Bayesian, Model, Evaluation, Evaluating, Retrieval-Augmented

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24753v1) | [下载PDF](https://arxiv.org/pdf/2608.24753v1.pdf)

---

## [14. SkillForge: Evolving Verifiable Skills for Reinforcement Learning Agents](https://arxiv.org/abs/2608.24747v1)

**作者**：Shidong Yang, Ziyu Ma, Tongwen Huang 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-25

### 📄 论文摘要

Large language model (LLM) agents are trained with reinforcement learning (RL) for complex decision-making tasks. However, most RL-trained agents remain episodic and cannot accumulate reusable knowledge across episodes. Recent skill-based approaches, such as SkillRL, attempt to address this issue by extracting skills from raw trajectories, but treat the skill bank as an append-only repository without verifying whether stored skills remain effective. In this paper, we propose SkillForge, a framework for continuous skill evolution that enables skills to be verified and refined through environment interaction. By making skill usage explicit during agent interaction, RL can directly optimize both environment actions and skill invocation decisions. SkillForge further introduces evidence-based skill verification and multi-pathway skill induction, allowing the skill bank to continuously grow while maintaining its quality. Extensive experiments on ALFWorld, WebShop, and AppWorld show that SkillForge consistently outperforms SkillRL, demonstrating the effectiveness of continuously verified skills in training stronger LLM agents.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM) agents are trained with reinforcement learning (RL) for complex decision-making tasks. However, most RL-trained agents remain episodic and cannot accumulate reusable knowled...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SkillForge, Evolving, Verifiable, Skills, Reinforcement, Learning, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24747v1) | [下载PDF](https://arxiv.org/pdf/2608.24747v1.pdf)

---

## cs.CV

## [15. From Seeing to Acting: Smart Glasses as First-Person Intelligence Platforms](https://arxiv.org/abs/2608.24877v1)

**作者**：Jiangning Zhang, Haojun Chen, Yong Liu  
**分类**：cs.CV  
**发布时间**：2026-08-25

### 📄 论文摘要

Smart glasses are evolving from capture and display accessories into first-person intelligence platforms that connect human perception, persistent context, and digital or physical action. Their on-body viewpoint aligns with the wearer's vision, audition, motion, and hand-object interaction, but must operate under tight energy, thermal, privacy, and feedback constraints. Despite rapid progress in augmented reality, egocentric vision, multimodal models, human-computer interaction, and embodied intelligence, the literature remains fragmented across devices, tasks, and benchmarks. \textit{The key challenge is not whether a model can recognize, answer, remember, or act in isolation, but whether a complete system can sustain a reliable, temporally valid, correctable, and governable perception-state-interaction-action loop.} This survey is \textit{the \textbf{first} to systematically study smart glasses through such a unified framework}. We formalize first-person data flow and constrained task utility, characterize devices along eight verifiable hardware capability axes, organize the literature around seven interdependent foundational capabilities, and introduce an L0-L5 framework spanning capture, reactive perception, contextual assistance, persistent state, governed action, and embodied coupling. Across nine application scenes, we connect tasks with datasets, systems, products, stakeholders, failure consequences, and evidence gaps. We further present a nine-dimensional deployment framework, a claim-conditioned evaluation protocol, and an evidence ladder from controlled measurement to longitudinal field validation and audit. Together, these elements make smart glasses more comparable, deployable, and reproducibly evaluated, while outlining a roadmap toward trustworthy first-person intelligence.

### 🤖 AI 总结

**一句话总结**：Smart glasses are evolving from capture and display accessories into first-person intelligence platforms that connect human perception, persistent context, and digital or physical action. Their on-bod...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Seeing, Acting, Smart, Glasses, First-Person, Intelligence, Platforms

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24877v1) | [下载PDF](https://arxiv.org/pdf/2608.24877v1.pdf)

---

## [16. LeFlow: Generative Latent Flow Planning for World Models](https://arxiv.org/abs/2608.24855v1)

**作者**：Hsiang-Wei Huang, Jianxu Shangguan, Junbin Lu 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-25

### 📄 论文摘要

Latent world models are inherently strong encoders that transform image pixel to latent embedding, yet existing world models still rely on online trajectory optimization for action planning: for every state-goal pair, an iterative optimizer is run from scratch to search for optimal action sequences, treating the world model as a black-box simulator. This approach pays the full iterative optimization cost anew at every replanning step and reuses no planning experience across queries. In this work, we ask whether planning itself can be amortized once a latent world model has been learned. We present LeFlow, which learns a reusable latent trajectory prior operating directly in the latent dynamics space from the world model. LeFlow recasts planning as conditional latent trajectory generation: a rectified-flow model imagines a future latent path between the current and goal embeddings, an inverse dynamics decoder turns latent transitions into action chunks, and the frozen world model verifies each candidate by autoregressive rollout. Across four major goal-conditioned pixel-control benchmarks, LeFlow replaces iterative action-space optimization with amortized latent planning and fixed-budget rollout selection, achieving consistent success-rate gains with an order-of-magnitude reduction in planning time. Our results argue that latent world models should support not only prediction but reusable planning priors. Our code is available at https://github.com/hsiangwei0903/LeFlow.

### 🤖 AI 总结

**一句话总结**：Latent world models are inherently strong encoders that transform image pixel to latent embedding, yet existing world models still rely on online trajectory optimization for action planning: for every...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LeFlow, Generative, Latent, Flow, Planning, World, Models, inherently

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24855v1) | [下载PDF](https://arxiv.org/pdf/2608.24855v1.pdf)

---

## [17. LAION-BVD: A 10-Million-Hour Open Video Dataset for Multimodal Pre-training](https://arxiv.org/abs/2608.24845v1)

**作者**：Andreas Hochlehnert, Marianna Nezhurina, Mehdi Cherti 等 12 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-08-25

### 📄 论文摘要

We present LAION-BVD, a large-scale open video dataset for multimodal learning, which contains 1.3B platform-specific video URLs collected from CommonCrawl. From these, we download 80M videos with a total duration of 10 million hours. The dataset is designed for multimodal pre-training across the video, audio, and image modalities. Using content-aware scene detection, we extract clips for which we synthetically generate video and audio captions. Models trained on these data achieve competitive performance on standard video-text and audio-text benchmarks, with consistent improvements as training or model scale increases. Additionally, we explore video frames as an alternative source of image-text data by extracting scene-changing frames. These frames exhibit a visual distribution distinct from standard web image corpora, and models trained on this dataset achieve strong image-text retrieval performance. We release LAION-BVD to the research community. It significantly expands open access to multimodal videos at an unprecedented scale.

### 🤖 AI 总结

**一句话总结**：We present LAION-BVD, a large-scale open video dataset for multimodal learning, which contains 1.3B platform-specific video URLs collected from CommonCrawl. From these, we download 80M videos with a t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, LAION-BVD, 10-Million-Hour, Open, Video, Dataset, Multimodal, Pre-training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24845v1) | [下载PDF](https://arxiv.org/pdf/2608.24845v1.pdf)

---

## [18. EMFE: A lightweight, explainable machine learning framework for malaria cell classification](https://arxiv.org/abs/2608.24793v1)

**作者**：Md Abdullah Al Kafi, Walayat Hussain, Mousumi Karmakar 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-25

### 📄 论文摘要

Automated malaria diagnosis from stained blood-smear microscopy is dominated by deep convolutional neural networks that are accurate but computationally expensive, poorly interpretable, and rarely validated with patient-level rigor. We present EMFE (Efficient Mathematical Feature Extraction), a five-feature framework for classifying single red-blood-cell images as parasitized or uninfected using Gray World color normalization, adaptive green-channel thresholding, morphological spot detection, and classical machine learning. Using the NIH LHNCBC malaria dataset (27,558 images from 200 patients), we evaluate Random Forest, Histogram Gradient Boosting, and Support Vector Machine classifiers under patient-grouped nested cross-validation (K_outer=20, K_inner=3), ensuring that cells from each patient remain within a single fold. The optimized Random Forest achieves 94.6% pooled out-of-fold accuracy (95% CI [93.6, 95.7]), corroborated by an untouched 40-patient holdout test (94.3%) and a patient-level permutation test (p<0.001, 1,000 permutations). Ablation experiments quantify the contribution of individual features and pipeline stages. Hardware-matched comparisons with retrained DenseNet121, ResNet50, and MobileNetV2 models assess the accuracy-efficiency trade-off. Synthetic perturbations characterize three failure modes, while explainability analysis identifies spot saturation as the dominant discriminative feature. Patient-level aggregation further quantifies sensitivity-specificity trade-offs and false-positive accumulation. These results demonstrate a statistically rigorous, interpretable, and computationally lightweight alternative to deep learning, while explicitly quantifying its limitations.

### 🤖 AI 总结

**一句话总结**：Automated malaria diagnosis from stained blood-smear microscopy is dominated by deep convolutional neural networks that are accurate but computationally expensive, poorly interpretable, and rarely val...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EMFE, lightweight, explainable, machine, learning, framework, malaria, cell

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24793v1) | [下载PDF](https://arxiv.org/pdf/2608.24793v1.pdf)

---

## [19. MoE-based Feature Adapter for Prompt-free Binary Coronary Artery Segmentation in X-ray Angiography](https://arxiv.org/abs/2608.24783v1)

**作者**：Lin Xi, Yingliang Ma  
**分类**：cs.CV  
**发布时间**：2026-08-25

### 📄 论文摘要

Accurate segmentation of coronary arteries in X-ray angiography videos is essential for quantitative coronary analysis and image-guided interventions. However, accurate segmentation remains challenging because coronary vessels are thin and exhibit low contrast, while the presence of catheters, guidewires, and complex anatomical background structures can further interfere with vessel delineation. Existing U-Net- and Transformer-based models provide strong baselines, but their shared feature-adaptation pathways may be insufficient for heterogeneous angiographic appearances. In this paper, we propose a prompt-free mixture-of-experts (MoE) feature adapter for binary coronary artery segmentation. Built upon parameter-efficient Vision Transformer adapters, the proposed method uses multiple lightweight experts with input-dependent top-$k$ routing to adaptively refine vessel-related features while limiting active computational cost. Experiments on MOSXAV and external evaluation on XACV show that the proposed method outperforms representative baselines and improves cross-dataset generalisation. These results suggest that MoE-based adapter learning is effective for robust coronary artery segmentation in X-ray angiography videos.

### 🤖 AI 总结

**一句话总结**：Accurate segmentation of coronary arteries in X-ray angiography videos is essential for quantitative coronary analysis and image-guided interventions. However, accurate segmentation remains challengin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MoE-based, Feature, Adapter, Prompt-free, Binary, Coronary, Artery, Segmentation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24783v1) | [下载PDF](https://arxiv.org/pdf/2608.24783v1.pdf)

---

## [20. Image Difference Quantification Using Autoencoder-Based Latent Representations](https://arxiv.org/abs/2608.24782v1)

**作者**：Manish Sharma, Timothy Yim, Clifton Forlines  
**分类**：cs.CV  
**发布时间**：2026-08-25

### 📄 论文摘要

Traditional image similarity metrics such as Mean Squared Error (MSE), Peak Signal-to-Noise Ratio (PSNR), and the Structural Similarity Index Measure (SSIM) rely on pixel-level comparisons and often fail to capture perceptually meaningful differences between images. In contrast, latent representations learned by deep neural networks encode high-level semantic information that is more closely aligned with human visual perception. This paper proposes a convolutional autoencoder-based framework for quantifying image differences using cosine similarity in latent space. The learned compact embeddings enable robust differentiation between visually distinct images under variations in illumination, pose, and background. Extensive evaluation on dog-cat images and additional cross-domain datasets demonstrates clear class-wise clustering and strong inter-class separability in the latent space, with 98.4% of dog-cat image pairs exhibiting similarity scores below 0.5. Further validation using the TID2013 dataset shows that latent-space distance correlates positively with human Mean Opinion Scores (MOS), demonstrating sensitivity to perceptually relevant image distortions. The proposed approach provides a computationally efficient and semantically grounded alternative to conventional pixel-based similarity metrics, with potential applications in content-based retrieval, perceptual quality assessment, and semantic similarity analysis.

### 🤖 AI 总结

**一句话总结**：Traditional image similarity metrics such as Mean Squared Error (MSE), Peak Signal-to-Noise Ratio (PSNR), and the Structural Similarity Index Measure (SSIM) rely on pixel-level comparisons and often f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Image, Difference, Quantification, Autoencoder-Based, Latent, Representations, Traditional, similarity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24782v1) | [下载PDF](https://arxiv.org/pdf/2608.24782v1.pdf)

---

## [21. Ensemble of Convolutional Neural Networks for StrokePrediction: Towards Improved Diagnostic Accuracy](https://arxiv.org/abs/2608.24771v1)

**作者**：Md Shahriar Sajid  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-25

### 📄 论文摘要

Brain stroke, known for its high mortality and incidence rates, poses significant health risks and requires rapid intervention for survival. Early diagnosis and preventive measures can greatly reduce life loss and disabilities. Recent advancements in deep learning have led to novel computer-aided diagnostic techniques for early stroke detection. This study proposes an intelligent system that predicts potential strokes using eleven features, evaluated through seven supervised machine learning algorithms. The process includes a literature review, dataset visualization, data preprocessing, and model evaluation. Ensemble methods like Random Forest, Stacking Classifier, and Bagging Classifier achieved high accuracies of 99.52%, while Decision Tree reached 98.24%. Other models, including KNN and TabNet, demonstrated reliable performance, achieving accuracies of 96.73% and 96.49%, respectively. The custom feedforward model achieved 94.91%, while SVC and logistic regression had lower accuracies at 88.06% and 77.03%. The results highlight the effectiveness of ensemble methods in stroke classification.

### 🤖 AI 总结

**一句话总结**：Brain stroke, known for its high mortality and incidence rates, poses significant health risks and requires rapid intervention for survival. Early diagnosis and preventive measures can greatly reduce ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Ensemble, Convolutional, Neural, Networks, StrokePrediction, Towards, Improved

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24771v1) | [下载PDF](https://arxiv.org/pdf/2608.24771v1.pdf)

---

## [22. IDeaL: Data-Free Multi-Teacher Distillation via Improved Dead Leaves](https://arxiv.org/abs/2608.24759v1)

**作者**：Feyza Yavuz, Mert Bülent Sarıyıldız, Diane Larlus  
**分类**：cs.CV  
**发布时间**：2026-08-25

### 📄 论文摘要

Multi-teacher distillation has emerged as a way to combine complementary teacher models into a single student model that exhibits the strengths of all its teachers. The student is trained to mimic the output of the teachers on a set of images, typically the union of the individual teacher's training sets, assuming this data is available. In this paper, we question that assumption and explore alternative options. We first study how far one can go when distilling from teachers fed with different types of noise. Then, we show that information contained in the teachers can be leveraged to tailor the noise for multi-teacher distillation: we propose a method that, thanks to decorrelation losses at both patch and image levels, generates teacher-specific, improved samples optimized for data-free distillation. Experiments show that our most effective samples, IDeaL, lead to strong students that successfully capture complementary information from the teachers, yielding surprisingly competitive results that substantially narrow the gap with students distilled from real images. Moreover, given a limited budget of 1K images for distillation, students distilled using our IDeaL samples match or surpass the performance of those distilled using a 1K-image subset of ImageNet.

### 🤖 AI 总结

**一句话总结**：Multi-teacher distillation has emerged as a way to combine complementary teacher models into a single student model that exhibits the strengths of all its teachers. The student is trained to mimic the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IDeaL, Data-Free, Multi-Teacher, Distillation, via, Improved, Dead, Leaves

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24759v1) | [下载PDF](https://arxiv.org/pdf/2608.24759v1.pdf)

---

## [23. Weakly Supervised Seafloor Segmentation for Seagrass Habitat Mapping in Side-Scan Sonar Imagery](https://arxiv.org/abs/2608.24756v1)

**作者**：Hayat Rajani, Nuno Gracias, Rafael Garcia  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-08-25

### 📄 论文摘要

Seagrass meadows are crucial blue-carbon habitats, and mapping their extent is a prerequisite for coastal management and carbon inventory. Optical satellite sensors cover large areas but cannot reach deep or turbid water, whereas side-scan sonar (SSS) images the seabed at high resolution and at any depth. Interpreting SSS, however, still relies on dense manual annotation, which is slow and costly. We address this by adapting a weakly supervised semantic segmentation framework to SSS benthic habitat mapping, so that pixel-level maps are learned from image-level labels alone. The framework couples a ViT-based encoder-decoder with a classification branch, extracts class activation maps, and refines them into pseudo-labels with a dense conditional random field that we tune for the noise and weak boundaries of acoustic imagery. It follows an iterative self-training scheme, together with a sampling strategy to cope with the strong class imbalance of the data. We also study the effect of different loss functions on segmentation quality, finding Lovász-Softmax loss the most effective. On a held-out transect, the refined pseudo-labels reached an mIoU of 89.3\% against the ground truth, and the segmentation branch, trained without any pixel-level labels, reached 87.6\%. Self-supervised pretraining on unlabelled SSS added a further 3\% in mean intersection-over-union. Field trials further demonstrate the generalizability of the trained model. These results show that accurate and label-efficient benthic habitat mapping from side-scan sonar is feasible at the scale needed for coast-wide seagrass monitoring.

### 🤖 AI 总结

**一句话总结**：Seagrass meadows are crucial blue-carbon habitats, and mapping their extent is a prerequisite for coastal management and carbon inventory. Optical satellite sensors cover large areas but cannot reach ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Weakly, Supervised, Seafloor, Segmentation, Seagrass, Habitat, Mapping, Side-Scan

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24756v1) | [下载PDF](https://arxiv.org/pdf/2608.24756v1.pdf)

---

## cs.LG

## [24. Improving Cross-Problem Vehicle Routing with Locally Augmented Preferences and Representation Disentanglement](https://arxiv.org/abs/2608.24859v1)

**作者**：Arthur Corrêa, Paulo Nascimento, Samuel Moniz  
**分类**：cs.LG  
**发布时间**：2026-08-25

### 📄 论文摘要

Multi-task vehicle routing problem (VRP) solvers seek to handle multiple VRP variants within a single unified model, avoiding the need to train a separate model for every variant. In spite of recent progress, current approaches remain limited on two fronts. On the training side, reinforcement learning suffers from reward-scale disparities and shrinking advantage signals as policies improve, whereas preference optimization stagnates once sampled tours become near-identical and thus fundamentally limited by the quality of the policy's own generated solutions, leaving both paradigms with weak supervision as training progresses. On the architecture side, existing fully shared encoders entangle constraint-dependent representations across heterogeneous variants, which limits generalization. We address these gaps with two model-agnostic contributions. First, we propose Preference Optimization with Locally Augmented Refinement (POLAR), a novel training algorithm that applies a local search refinement pass to the best decoded tour before forming preference pairs, yielding much more informative pairwise margins. Second, a Progressive Layered Extraction (PLE) encoder routes each encoder layer through one shared expert and a set of task-specific experts via a gating mechanism, progressively separating common routing structure from constraint-specific encodings. Through extensive experiments on various VRP variants, we show that POLAR and PLE together elevate the current state-of-the-art among neural multi-task solvers. We reduce the average gap to reference solutions by 21.3% relative to the strongest published baseline on 16 in-distribution variants, and outperform prior neural methods on 27 out of 32 unseen variants. Ablation studies confirm the efficacy of each contribution, showing that both improve cross-problem generalization across multiple backbone model architectures.

### 🤖 AI 总结

**一句话总结**：Multi-task vehicle routing problem (VRP) solvers seek to handle multiple VRP variants within a single unified model, avoiding the need to train a separate model for every variant. In spite of recent p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Improving, Cross-Problem, Vehicle, Routing, Locally, Augmented, Preferences, Representation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24859v1) | [下载PDF](https://arxiv.org/pdf/2608.24859v1.pdf)

---

## [25. Bellman Calibration for Marginalized Importance Weighting in Offline Reinforcement Learning](https://arxiv.org/abs/2608.24858v1)

**作者**：Lars van der Laan, Nathan Kallus  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-08-25

### 📄 论文摘要

Marginalized importance weighting evaluates a target policy by reweighting offline state-action samples with its discounted occupancy ratio, characterized by an adjoint Bellman equation. Existing minimax, primal-dual, and fitted fixed-point estimators can leave residual occupancy-balance violations because of function-class approximation, regularization, or incomplete optimization. These violations are difficult to diagnose and reduce because the objectives generally lack a direct supervised validation loss for hyperparameter tuning, model selection, and early stopping. We introduce isotonic Bellman calibration, a one-dimensional, model-agnostic post-processing method that reduces these violations while preserving the ranking information in any initial occupancy-ratio estimate. The method corrects the estimate's scale and shape by applying fitted occupancy-ratio evaluation (FORE) over a one-dimensional class of nondecreasing transformations. We characterize Bellman calibration as a conditional fixed-point property equivalent to occupancy-balance against every test function of the calibrated ratio. More generally, we derive a calibration-refinement bound showing that any fitted ratio with small calibration error performs nearly as well as the best post-processing based on its fitted values. For isotonic Bellman calibration, we establish finite-sample calibration guarantees and a KL oracle inequality relative to the best monotone transformation of the initial estimate. Consequently, isotonic Bellman calibration achieves small calibration error and KL risk within statistical error of the best monotone correction, with guarantees for downstream target-occupancy functionals, including policy-value estimation.

### 🤖 AI 总结

**一句话总结**：Marginalized importance weighting evaluates a target policy by reweighting offline state-action samples with its discounted occupancy ratio, characterized by an adjoint Bellman equation. Existing mini...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bellman, Calibration, Marginalized, Importance, Weighting, Offline, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24858v1) | [下载PDF](https://arxiv.org/pdf/2608.24858v1.pdf)

---

## [26. BioKERN: Biological Kernel Regularization for Histology-to-Transcriptomics Neighborhood Retrieval](https://arxiv.org/abs/2608.24823v1)

**作者**：Seungik Cho, Betul Orcan-Ekmekci  
**分类**：cs.LG, q-bio.QM  
**发布时间**：2026-08-25

### 📄 论文摘要

Spatially resolved biology requires representations that preserve biological neighborhood structure rather than only exact cross-modal correspondences. Existing histology--transcriptomics objectives can emphasize instance-level matching even when non-paired spots share molecular or spatial context. We introduce BioKERN, a multimodal spatial representation-learning framework that incorporates biological structure as an explicit, learnable inductive bias. BioKERN constructs a training-time biological kernel by combining transcriptomic similarity and spatial proximity, then uses it to provide graded neighborhood supervision and regularize embedding geometry. Evaluation uses a fixed, model-independent biological neighborhood definition shared by all methods. Across Mouse Brain Visium and Human Liver GSE240429, BioKERN consistently improves biological-neighborhood retrieval over BLEEP in both single- and multi-scale settings. Controlled shared-architecture experiments show that most of the improvement arises from biological-kernel regularization rather than increased model capacity. These results support explicit biological geometry as an interpretable inductive bias for multimodal learning in spatial biology.

### 🤖 AI 总结

**一句话总结**：Spatially resolved biology requires representations that preserve biological neighborhood structure rather than only exact cross-modal correspondences. Existing histology--transcriptomics objectives c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BioKERN, Biological, Kernel, Regularization, Neighborhood, Retrieval, Spatially, resolved

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24823v1) | [下载PDF](https://arxiv.org/pdf/2608.24823v1.pdf)

---

## [27. A Geometric Theory of Robust Fairness Audits](https://arxiv.org/abs/2608.24818v1)

**作者**：Binita Maity  
**分类**：cs.LG  
**发布时间**：2026-08-25

### 📄 论文摘要

Neighborhood-based fairness audits evaluate individual fairness by comparing predictions among similar individuals in feature space. Despite their widespread use, little is known about the robustness of the auditing procedure itself. Because these audits rely on nearest neighbor relationships, small perturbations in feature space can alter local neighborhoods and produce different fairness assessments even when model predictions remain unchanged. We develop a geometric framework for analyzing the robustness of neighborhood-based fairness audits under bounded perturbations. Our analysis establishes sufficient conditions for neighborhood invariance, quantifies how neighborhood replacement propagates to audit instability, and introduces audit volatility, a measure of the expected sensitivity of fairness audits under repeated perturbations. Experiments on benchmark datasets support the theoretical analysis and show that the proposed framework explains the observed stability of neighborhood-based fairness audits.

### 🤖 AI 总结

**一句话总结**：Neighborhood-based fairness audits evaluate individual fairness by comparing predictions among similar individuals in feature space. Despite their widespread use, little is known about the robustness ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Geometric, Theory, Robust, Fairness, Audits, Neighborhood-based, evaluate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24818v1) | [下载PDF](https://arxiv.org/pdf/2608.24818v1.pdf)

---

## [28. Effective Learning Rate Governs Loss Dynamics in Language Model Pretraining](https://arxiv.org/abs/2608.24814v1)

**作者**：Zihan Liu, Ruiheng Zheng, Shaobo Zhang 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-25

### 📄 论文摘要

We uncover ELR collapse in language model pretraining: learning rate (LR) and parameter norm govern loss dynamics primarily through their ratio, the effective learning rate (ELR). When ELR is matched across runs, their loss trajectories collapse throughout training despite substantially different LRs and parameter norms. Across optimizers, architectures, datasets, and model scales, mean collapse errors are typically a few x 10^-3, below the seed-to-seed variation measured in a representative configuration. Systematic ablations identify normalization design and the timescale of LR-norm variation as key determinants of collapse precision. Controlled interventions further show that weight decay and Hyperball shape loss dynamics primarily through the ELR schedules they induce. Replacing LR with ELR enables a fitted functional scaling law (FSL) to transfer across norm-control methods. The resulting ELR-based FSL also explains delayed acceleration, a recurring effect of norm control. Together, these results establish ELR as a common coordinate linking LR scheduling, norm control, and loss dynamics.

### 🤖 AI 总结

**一句话总结**：We uncover ELR collapse in language model pretraining: learning rate (LR) and parameter norm govern loss dynamics primarily through their ratio, the effective learning rate (ELR). When ELR is matched ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Effective, Learning, Rate, Governs, Loss, Dynamics, Language, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24814v1) | [下载PDF](https://arxiv.org/pdf/2608.24814v1.pdf)

---

## [29. MDTE: Minority-Aware Diffusion over Temporal Edge Events for Imbalanced Node Classification](https://arxiv.org/abs/2608.24812v1)

**作者**：Zhou Zelong, Zhang Tianming, Yang Zhengyi 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-25

### 📄 论文摘要

Class-imbalanced node classification on temporal graphs is challenging because majority-dominated temporal propagation progressively assimilates minority representations, while conventional node and neighborhood information provides insufficient discriminative evidence for minority classes. To address these issues, we propose MDTE, a minority-aware diffusion framework that reconstructs stable and discriminative temporal edge-event representations through conditional diffusion denoising. Specifically, MDTE introduces Distribution-Aware Selective Propagation, which combines Local Outlier Factor (LOF)-based propagation filtering with cluster-aware low-frequency propagation. The module preserves informative neighborhood dependencies while mitigating harmful propagation and majority-class information assimilation. It further develops Multi-View Discriminative Fusion, which exploits feature reconstruction and topology prediction to characterize class-wise differences in distribution learning and extracts complementary discriminability signals to guide denoising. Experiments on five real-world datasets demonstrate that MDTE consistently achieves the best performance on minority-class-oriented metrics, improving minority-class recall by up to 23.53 percentage points, minority-class F1 by 8.68 percentage points, and AUPRC by 2.67 percentage points over the strongest baselines.

### 🤖 AI 总结

**一句话总结**：Class-imbalanced node classification on temporal graphs is challenging because majority-dominated temporal propagation progressively assimilates minority representations, while conventional node and n...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, MDTE, Minority-Aware, over, Temporal, Edge, Events, Imbalanced

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24812v1) | [下载PDF](https://arxiv.org/pdf/2608.24812v1.pdf)

---

## [30. Beyond Uniform Local Isometry and Topology: FactoMap for Disentangled Representations](https://arxiv.org/abs/2608.24762v1)

**作者**：Sohini Gupta, Bahareh Tolooshams  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-25

### 📄 论文摘要

Many disentanglement methods represent generative factors using Euclidean product coordinates, although the underlying factor spaces may wrap, collapse, or have position-dependent geometry. We introduce factor-space structure, combining factor domains, generator-induced identifications, and position-dependent scales to distinguish topologically equivalent spaces with different factor geometries. We show that statistically independent factors need not be geometrically separable: hue and scale produce effects that grow at different rates, yielding anisotropy that no fixed rescaling removes. We propose the Factor-Space Topographic Map (FactoMap), which learns interpretable prototypes indexed by a factor-space lattice. Topographic learning transfers the lattice's periodicity, collapses, and non-uniform extent to the representation. Experiments show that matching this structure preserves factor continuity and enables disentanglement of the underlying factors.

### 🤖 AI 总结

**一句话总结**：Many disentanglement methods represent generative factors using Euclidean product coordinates, although the underlying factor spaces may wrap, collapse, or have position-dependent geometry. We introdu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Uniform, Local, Isometry, Topology, FactoMap, Disentangled, Representations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.24762v1) | [下载PDF](https://arxiv.org/pdf/2608.24762v1.pdf)

---

