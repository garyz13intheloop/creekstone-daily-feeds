# arXiv AI 论文日报 | 2026-06-12

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (8 篇)
- [cs.CV](#csCV) (6 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.AI](#csAI) (9 篇)

---

## cs.AI

## [1. Automated reproducibility assessments in the social and behavioral sciences using large language models](https://arxiv.org/abs/2606.13670v1)

**作者**：Tobias Holtdirk, Pietro Marcolongo, Anna Steinberg Schulten 等 10 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-11

### 📄 论文摘要

Reproducibility in the social and behavioral sciences is typically evaluated by independent researchers who reanalyze the original data to assess whether the published findings can be recovered. However, such approaches are resource-intensive and difficult to scale. Here, we show that large language models (LLMs) can automate reproducibility assessments. Using N=76 published studies with predefined claims from the behavioral and social sciences, we compare LLM-generated analysis with the original findings and human reanalysis. For 7 studies, the LLM could not produce a viable effect size estimate. For the remaining studies, our LLM pipeline recovered the original effect sizes in 41% of studies using a +/-0.05 tolerance in Cohen's d. Further, our LLM pipeline reached the same qualitative conclusion as the original study in 96% of cases, where conclusions indicate whether the reanalysis supports the original claim. For comparison, human reanalysts recovered the original effect sizes in 34% of studies and reached the same qualitative conclusion in 74% of cases. Together, these results show that LLMs can serve as a scalable tool for automated reproducibility assessment and provide a foundation for systematic auditing of empirical results in the social and behavioral sciences.

### 🤖 AI 总结

**一句话总结**：Reproducibility in the social and behavioral sciences is typically evaluated by independent researchers who reanalyze the original data to assess whether the published findings can be recovered. Howev...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Automated, reproducibility, assessments, social, behavioral, sciences, large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13670v1) | [下载PDF](https://arxiv.org/pdf/2606.13670v1.pdf)

---

## [2. Agents-K1: Towards Agent-native Knowledge Orchestration](https://arxiv.org/abs/2606.13669v1)

**作者**：Zongsheng Cao, Bihao Zhan, Jinxin Shi 等 25 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-11

### 📄 论文摘要

Current LLM-based research agents have advanced through agent orchestration, yet largely overlook scientific knowledge orchestration. Existing works often reduce papers to abstracts, surface mentions, and flat \texttt{cites} edges, omitting key entities, claims, evidence, mechanisms, and method lineages essential for scientific reasoning. To this end, we introduce \textbf{Agents-K1}, an end-to-end knowledge orchestration pipeline that converts raw documents into agent-native scientific knowledge graphs. Agents-K1 integrates three components under a unifying theoretical foundation: a multimodal parser whose five-module schema captures entities, multimodal evidence, citations, and typed inter-entity relations across the full paper rather than abstracts alone; a 4B information-extraction backbone trained with GRPO under a rule-based reward; and a graphanything CLI, a tri-source agent interface that unifies web search, multimodal graph retrieval, and cross-document traversal. On top of this, we process 2.46 million scientific papers across six subjects to produce \textbf{Scholar-KG}, of which we release a one-million-paper subset, and the full Scholar-KG is accessible via the SCP link below. The same pipeline can be extended to general-domain corpora and to schema-conformant data synthesis. Extensive experiments demonstrate that Agents-K1 achieves superior performance in scientific information extraction, knowledge graph construction, and multi-hop scientific reasoning.

### 🤖 AI 总结

**一句话总结**：Current LLM-based research agents have advanced through agent orchestration, yet largely overlook scientific knowledge orchestration. Existing works often reduce papers to abstracts, surface mentions,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agents-K1, Towards, Agent-native, Knowledge, Orchestration, Current, LLM-based, research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13669v1) | [下载PDF](https://arxiv.org/pdf/2606.13669v1.pdf)

---

## [3. EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery](https://arxiv.org/abs/2606.13662v1)

**作者**：Amy Xin, Jiening Siow, Junjie Wang 等 8 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-06-11

### 📄 论文摘要

LLM-based agents have shown increasing potential in automating scientific discovery. Given an optimizable metric and an execution environment, they can propose, validate, and iterate scientific solutions, and have produced results that outperform human-designed approaches. As model capabilities continue to improve, we argue that the bottleneck for autonomous scientific discovery is shifting from prescribing agent workflows to designing agent environments: the resources, constraints, and interfaces that shape agent behavior. We frame this as environment engineering: building environments that amplify productive behaviors, such as open-ended exploration, systematic artifact management, and inter-agent collaboration, while suppressing harmful behaviors, such as reward hacking and high-friction human oversight. We present EurekAgent, an environment-engineered agent system for metric-driven autonomous scientific discovery. EurekAgent engineers the environment along four dimensions: permissions engineering for bounded agent execution and isolated evaluation; artifact engineering for filesystem and Git-based collaboration; budget engineering for budget-aware exploration; and human-in-the-loop engineering for easy human supervision and intervention. EurekAgent sets new state-of-the-art results on multiple mathematics, kernel engineering, and machine learning tasks, including new state-of-the-art 26-circle packing results discovered with less than $11 in total API cost. We open-source our code and results, and call for environment engineering as a core research direction for developing reliable autonomous research agents.

### 🤖 AI 总结

**一句话总结**：LLM-based agents have shown increasing potential in automating scientific discovery. Given an optimizable metric and an execution environment, they can propose, validate, and iterate scientific soluti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, EurekAgent, Environment, Engineering, All, Need, Autonomous, Scientific

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13662v1) | [下载PDF](https://arxiv.org/pdf/2606.13662v1.pdf)

---

## [4. Before You Think: System 0, AI-Mediated Cognition and Cognitive Colonization](https://arxiv.org/abs/2606.13658v1)

**作者**：Marianna Bergamaschi Ganapini, Massimo Chiriatti, Enrico Panai 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-11

### 📄 论文摘要

This paper examines three recent frameworks for understanding the cognitive and epistemic consequences of artificial intelligence: Tri-System Theory, Thinkframes, and System 0. It argues that while the first two capture important dimensions of AI's influence on individual reasoning and collective epistemic practices, System 0 occupies a theoretically distinctive position that neither can fully replicate. The paper introduces the concept of cognitive colonization, according to which AI systems can embed external interests within the architecture of the self in ways that are difficult for users to perceive. Because such systems are already widely deployed, understanding these invisible forms of influence is an urgent philosophical and practical task.

### 🤖 AI 总结

**一句话总结**：This paper examines three recent frameworks for understanding the cognitive and epistemic consequences of artificial intelligence: Tri-System Theory, Thinkframes, and System 0. It argues that while th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Before, Think, System, AI-Mediated, Cognition, Cognitive, Colonization, paper

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13658v1) | [下载PDF](https://arxiv.org/pdf/2606.13658v1.pdf)

---

## [5. AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility](https://arxiv.org/abs/2606.13608v1)

**作者**：Xiaoyuan Liu, Jianhong Tu, Yuqi Chen 等 29 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-06-11

### 📄 论文摘要

Agent systems are advancing quickly across domains, but their evaluation remains fragmented. Most benchmarks rely on fixed, LLM-centric harnesses that require heavy integration, create test-production mismatch, and limit fair comparison across diverse agent designs. The root problem is the lack of an open, agent-agnostic assessment interface. We advocate Agentified Agent Assessment (AAA), where evaluation is performed by judge agents and all participants interact through standardized protocols: A2A for task management and MCP for tool access. Conventional benchmarking defines two separate interfaces, one for the benchmark and one for the agent, while AAA only needs one; this yields a generic, unified framework that separates assessment logic from agent implementation and enables reproducible, interoperable, and multi-agent evaluation. We further introduce AgentBeats as a concrete realization of AAA: we identify five practical operation modes that make standardized assessment compatible with real-world constraints on openness, privacy, and reproducibility.   To evaluate our design at scale, we conduct two studies: a five-month open competition that drew 298 judge agents across 12 categories together with 467 subject agents from independent participants, showing that AAA applies across a heterogeneous range of benchmarks; and a case study on coding agents that confirms agentified evaluation preserves fidelity with the public record while surfacing previously missing head-to-head results, yielding research insights about agent design. Combining a community-scale field study and a controlled coding case study, we verify that AAA delivers coverage, practicality, and fidelity across heterogeneous scenarios at scale. Together, AAA and AgentBeats offer a clear path toward open, standardized, and reproducible agent assessment.

### 🤖 AI 总结

**一句话总结**：Agent systems are advancing quickly across domains, but their evaluation remains fragmented. Most benchmarks rely on fixed, LLM-centric harnesses that require heavy integration, create test-production...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, AgentBeats, Agentifying, Assessment, Openness, Standardization, Reproducibility, systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13608v1) | [下载PDF](https://arxiv.org/pdf/2606.13608v1.pdf)

---

## [6. Reasoning as Pattern Matching: Shared Mechanisms in Human and LLM Everyday Reasoning](https://arxiv.org/abs/2606.13607v1)

**作者**：Zach Studdiford, Gary Lupyan  
**分类**：cs.AI  
**发布时间**：2026-06-11

### 📄 论文摘要

When large language models (LLMs) fail to generalize or make haphazard errors in reasoning, it is often taken as evidence that LLMs are not truly reasoning, but rather performing a kind of pattern matching. The implication is that people's behavior does not exhibit the same types of failures because human reasoning uses principled and abstract world models. We evaluate human participants and 25 LLMs on their ability to engage in common-sense reasoning about a variety of everyday situations and observe similar patterns of errors in both people and models. We then identify the set of attention heads driving LLM responses and find that these heads implement a form of pattern-matching. These attention heads allow us to predict seemingly inexplicable reasoning errors in people caused by ostensibly irrelevant prompt details. Taken together, our results suggest that everyday causal reasoning in people and LLMs is more consistent with a form of pattern-matching than with abstract world models.

### 🤖 AI 总结

**一句话总结**：When large language models (LLMs) fail to generalize or make haphazard errors in reasoning, it is often taken as evidence that LLMs are not truly reasoning, but rather performing a kind of pattern mat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, LLM, Reasoning, Pattern, Matching, Shared, Mechanisms, Human

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13607v1) | [下载PDF](https://arxiv.org/pdf/2606.13607v1.pdf)

---

## [7. Multi-Agent Reinforcement Learning from Delayed Marketplace Feedback for Objective-Weight Adaptation in Three-Sided Dispatch](https://arxiv.org/abs/2606.13604v1)

**作者**：Haochen Wu, Yi Hou, Shiguang Xie  
**分类**：cs.AI, cs.LG, cs.MA  
**发布时间**：2026-06-11

### 📄 论文摘要

Dispatch in three-sided marketplaces provides a natural setting for reinforcement learning from world feedback: decisions are evaluated by delayed operational outcomes such as delivery speed, courier utilization, and merchant congestion. We present a deployed reinforcement learning system at DoorDash that adapts dispatch objective weights in a large-scale food-delivery marketplace using delayed signals. Rather than replacing the combinatorial assignment optimizer, a store-level policy learned from logged marketplace data selects a discrete multiplier that shifts the dispatch optimizer's tradeoff between delivery quality and batching efficiency. This interface enables offline policy learning under noisy, delayed, and coupled feedback while preserving production feasibility constraints and operational safeguards. We train a shared value function using centralized offline data and decentralized store-level execution, with Double Q-learning targets and a conservative regularizer to reduce out-of-distribution value overestimation. In a production switchback experiment, the offline-trained policy increases batching and reduces courier-side time costs without degrading customer-facing delivery quality. Results illustrate how world feedback from a live economic and logistics system can be used to safely adapt decision policies online.

### 🤖 AI 总结

**一句话总结**：Dispatch in three-sided marketplaces provides a natural setting for reinforcement learning from world feedback: decisions are evaluated by delayed operational outcomes such as delivery speed, courier ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, Reinforcement, Learning, Delayed, Marketplace, Feedback, Objective-Weight, Adaptation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13604v1) | [下载PDF](https://arxiv.org/pdf/2606.13604v1.pdf)

---

## [8. EpiBench: Verifiable Evaluation of AI Agents on Epigenomics Analysis](https://arxiv.org/abs/2606.13602v1)

**作者**：Harihara Muralidharan, Reema Baskar, Soo Hee Lee 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-11

### 📄 论文摘要

We introduce EpiBench, a verifiable benchmark for short-horizon epigenomics analysis. EpiBench evaluates whether agents can make well-defined analysis decisions from realistic workflow states and return deterministically gradable answers. The benchmark includes 106 evaluations across CUT\&Tag/CUT\&RUN, ATAC-seq, ChIP-seq, and DNA methylation workflows. Across 5,088 valid trajectories from 16 model-harness pairs, no system passed a majority of attempts: GPT-5.5 / Pi led at 45.0\% (143/318 attempts; 95\% confidence interval (CI), 36.3--53.7), followed by GPT-5.5 / OpenAI Codex at 39.9\% (127/318 attempts; 95\% CI, 31.6--48.3). Claude Opus 4.8 Max / Pi and GPT-5.4 / Pi each passed 39.0\% (124/318 attempts; 95\% CI, 30.2--47.8 and 31.0--47.0, respectively). Performance varies across assay types, and many failed runs still contain parts of the correct answer. Agents often found the right files and computed useful intermediate results, but failed when the task required deeper, assay-specific scientific judgment.

### 🤖 AI 总结

**一句话总结**：We introduce EpiBench, a verifiable benchmark for short-horizon epigenomics analysis. EpiBench evaluates whether agents can make well-defined analysis decisions from realistic workflow states and retu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, We, EpiBench, Verifiable, Evaluation, Epigenomics, Analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13602v1) | [下载PDF](https://arxiv.org/pdf/2606.13602v1.pdf)

---

## [9. Multiagent Protocols with Aggregated Confidence Signals](https://arxiv.org/abs/2606.13591v1)

**作者**：Ali Elahi, Barbara Di Eugenio  
**分类**：cs.AI, cs.LG, cs.MA  
**发布时间**：2026-06-11

### 📄 论文摘要

Confidence is used for reliability, oversight, and a range of downstream decision tasks in Natural Language Processing (NLP), yet no existing method produces or evaluates a confidence for the output of a multiagent system. Prior work uses confidence within multiagent debate (MAD) to weight messages, trigger debate, or calibrate individual agents, but it never aggregates these into a single confidence for the system itself. We introduce three protocols that produce a final answer along with a single aggregated confidence by first transforming raw confidence signals to make them comparable across models, then combining them via soft voting or a probability fusion we call Bayesian fusion. This aggregated confidence is substantially more discriminative (AUARC) than that of the best single agent or the standard debate baselines, while correctness (F1-score) stays stable and recovers the losses MAD incurs on more ambiguous tasks. Analyzing two estimators, sequence probability and self-report, alongside parametric and non-parametric calibrators, we find that calibration improves F1 for both estimators while AUARC is less reliant on it. We evaluate six homogeneous and heterogeneous debating pairs per benchmark, across five benchmarks and four task types, spanning a range of model capabilities and sizes.

### 🤖 AI 总结

**一句话总结**：Confidence is used for reliability, oversight, and a range of downstream decision tasks in Natural Language Processing (NLP), yet no existing method produces or evaluates a confidence for the output o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multiagent, Protocols, Aggregated, Confidence, Signals, used, reliability, oversight

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13591v1) | [下载PDF](https://arxiv.org/pdf/2606.13591v1.pdf)

---

## cs.CL

## [10. EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments](https://arxiv.org/abs/2606.13681v1)

**作者**：Jundong Xu, Qingchuan Li, Jiaying Wu 等 14 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-11

### 📄 论文摘要

Large language model (LLM) agents have achieved strong performance on a wide range of benchmarks, yet most evaluations assume static environments. In contrast, real-world deployment is inherently dynamic, requiring agents to continually align their knowledge, skills, and behavior with changing environments and updated task conditions. To address this gap, we introduce EvoArena, a benchmark suite that models environment changes as sequences of progressive updates across terminal, software, and social domains. We further propose EvoMem, a patch-based memory paradigm that records memory evolution as structured update histories, enabling agents to reason about environmental evolution through changes in their memory. Experiments show that current agents struggle on EvoArena, achieving an average accuracy of 39.6% across evolving terminal, software, and social-preference domains. EvoMem consistently improves performance, yielding an average gain of 1.5% on EvoArena and also improving standard benchmarks such as GAIA and LoCoMo by 6.1% and 4.8%. Beyond individual tasks, EvoMem further improves chain-level accuracy by 3.7% on EvoArena, where success requires completing a consecutive sequence of related evolutionary subtasks. Mechanistic analysis shows that EvoMem improves evidence capture in the memory, indicating better preservation of complete evolving environment states. Our results highlight the importance of modeling evolution in both evaluation and memory for reliable agent deployment.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM) agents have achieved strong performance on a wide range of benchmarks, yet most evaluations assume static environments. In contrast, real-world deployment is inherently dyna...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, EvoArena, Tracking, Memory, Evolution, Robust, Dynamic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13681v1) | [下载PDF](https://arxiv.org/pdf/2606.13681v1.pdf)

---

## [11. Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning](https://arxiv.org/abs/2606.13680v1)

**作者**：Zilin Xiao, Qi Ma, Chun-cheng Jason Chen 等 7 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-11

### 📄 论文摘要

Retrieval-augmented generation (RAG) has become a standard mechanism for grounding language models in external knowledge, yet conventional retrieval based on lexical or semantic similarity is poorly suited for complex reasoning tasks: a semantically similar problem may demand an entirely different solution strategy, while a superficially different problem may share the same underlying reasoning pattern. We propose Retrieval-Augmented Reinforcement Fine-Tuning (RA-RFT), a post-training framework that teaches language models to reason by analogy. RA-RFT uses gold-relevance distillation to train a retriever that ranks contexts by expected reasoning benefit rather than semantic overlap, and then fine-tunes the policy model via reinforcement fine-tuning methods with retrieved analogous demonstrations, so the model learns to leverage reasoning traces under verifiable outcome rewards. We further analyze the diversity of retrieved contexts and find that reasoning-aware retrieval surfaces complementary solution strategies that provide distinct reasoning scaffolds for individual problems. Across challenging mathematical reasoning benchmarks, RA-RFT consistently outperforms standard reinforcement fine-tuning methods. For example, it improves AIME 2025 average@32 accuracy by 7.1 and 2.8 points over GRPO for Qwen3-1.7B and Qwen3-4B respectively -- suggesting that reasoning-aware retrieval is a complementary axis of improvement and orthogonal to advances in reward design or training curricula.

### 🤖 AI 总结

**一句话总结**：Retrieval-augmented generation (RAG) has become a standard mechanism for grounding language models in external knowledge, yet conventional retrieval based on lexical or semantic similarity is poorly s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Reason, Analogy, via, Retrieval-Augmented, Reinforcement, Fine-Tuning, generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13680v1) | [下载PDF](https://arxiv.org/pdf/2606.13680v1.pdf)

---

## [12. Influcoder: Distilling Decoders' Gradient Influence Rankings into an Encoder for Data Attribution](https://arxiv.org/abs/2606.13668v1)

**作者**：Dimitri Kachler, Damien Sileo, Pascal Denis  
**分类**：cs.CL  
**发布时间**：2026-06-11

### 📄 论文摘要

With the growth of LLMs' (Large Language Models) capabilities, there has been an increasing push to curate high quality datasets by filtering samples in the training data. In general, Data Attribution (DA) methods aim to estimate how individual samples in a training dataset can precondition a model to generate certain outputs. As an example, one might be interested in which samples in the data could be the source of toxic behavior after training the LLM. Many methods quantify this conditioning through the paradigm of influence functions. While methods of this family are effective in its function, they lack the necessary processing speed and storage compactness to be practically implemented on large datasets. We propose a method, Influcoder, as a quick and cost-effective approach to influence-based Data Attribution at scale.

### 🤖 AI 总结

**一句话总结**：With the growth of LLMs' (Large Language Models) capabilities, there has been an increasing push to curate high quality datasets by filtering samples in the training data. In general, Data Attribution...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Influcoder, Distilling, Decoders', Gradient, Influence, Rankings, Encoder

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13668v1) | [下载PDF](https://arxiv.org/pdf/2606.13668v1.pdf)

---

## [13. HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents](https://arxiv.org/abs/2606.13663v1)

**作者**：Yaxin Du, Yifan Zhou, Yujie Ge 等 10 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-11

### 📄 论文摘要

Tool-augmented LLM agents commonly rely on step-wise atomic tool calls, where each invocation, observation, and value transfer is exposed in the main reasoning trace. This creates an \emph{execution-granularity mismatch}: locally deterministic tool workflows are unfolded into repeated model-visible decisions, consuming context and forcing the model to manage low-level dataflow in the trace. We introduce \textbf{HyperTool}, a unified executable MCP-style tool interface that changes the model-visible unit of tool execution. A model invokes HyperTool with a code block that can call existing tools through their original schemas, manipulate returned values, and pass intermediate results locally, folding deterministic tool subroutines into a single outer call. To train models to use this interface, we synthesize HyperTool-format trajectories from cross-tool compositional tasks and verify them in real MCP environments. On MCP-Universe, HyperTool improves average accuracy from 15.69\% to 35.29\% on Qwen3-32B and from 9.93\% to 33.33\% on Qwen3-8B, and surpass GPT-OSS and Kimi-k2.5 on average accuracy, showing that our HyperTool can substantially improve multi-step tool use.

### 🤖 AI 总结

**一句话总结**：Tool-augmented LLM agents commonly rely on step-wise atomic tool calls, where each invocation, observation, and value transfer is exposed in the main reasoning trace. This creates an \emph{execution-g...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, LLM, HyperTool, Beyond, Step-Wise, Tool, Calls, Tool-Augmented

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13663v1) | [下载PDF](https://arxiv.org/pdf/2606.13663v1.pdf)

---

## [14. Operadic consistency: a label-free signal for compositional reasoning failures in LLMs](https://arxiv.org/abs/2606.13649v1)

**作者**：Nathaniel Bottman, Yinhong Liu, Kyle Richardson  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-06-11

### 📄 论文摘要

Detecting LLM reasoning failures at inference time without ground-truth labels has motivated a wide range of confidence baselines, including self-consistency, semantic entropy, and P(True), built on within-question sampling and self-evaluation. Operad theory, the formalism for systems built by iterated substitution, suggests a complementary diagnostic: a model's direct answer to a compositional query should agree with the answer it produces by composing a stated decomposition of the same query. We instantiate this idea as operadic consistency (OC), a per-question signal. Across twelve instruction-tuned LLMs (4B to 671B parameters, open-weights and closed-source) on four multi-hop QA datasets, OC is strongly correlated with accuracy on every dataset (Pearson $r \in [0.86, 0.94]$, all $p \leq 0.0004$), and is the only signal we evaluate with $r \geq 0.85$ uniformly across all four datasets. Chain-of-thought self-consistency (CoT-SC; Wang et al., 2023) matches OC on HotpotQA and DROP ($r = 0.93, 0.87$) but drops to $r \approx 0.45$ on MuSiQue and StrategyQA. At the per-question level, OC contributes information beyond CoT-SC and semantic entropy on every dataset (cluster-robust $p \leq 10^{-16}$ for the OC coefficient), and the conclusion is robust to additionally controlling for constructed decomposition-aware baselines ($p \leq 10^{-13}$). The same signal yields selective-prediction improvements (accuracy at fixed coverage) over a tuned CoT-SC baseline at the equal-cost $K = 3$ budget (AUARC lifts of +0.086 to +0.096 and AUROC lifts of +0.092 to +0.164; 95% CIs exclude zero on every cell). On five frontier thinking models, where the decomposition is extracted from the model's own chain of thought, the same equal-cost comparison gives positive selective-prediction point-estimate lift on all 16 (dataset, budget, metric) cells tested, with 95% CIs excluding zero on 12 of the 16.

### 🤖 AI 总结

**一句话总结**：Detecting LLM reasoning failures at inference time without ground-truth labels has motivated a wide range of confidence baselines, including self-consistency, semantic entropy, and P(True), built on w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Operadic, consistency, label-free, signal, compositional, reasoning, failures

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13649v1) | [下载PDF](https://arxiv.org/pdf/2606.13649v1.pdf)

---

## [15. SkMTEB: Slovak Massive Text Embedding Benchmark and Model Adaptation](https://arxiv.org/abs/2606.13647v1)

**作者**：Marek Šuppa, Andrej Ridzik, Daniel Hládek 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-06-11

### 📄 论文摘要

We introduce SkMTEB, the first comprehensive MTEB-style text embedding benchmark for Slovak, a low-resource West Slavic language, comprising 31 datasets across 7 task types -- nearly 4$\times$ the depth of existing multilingual benchmark coverage for Slovak. Our evaluation of 31 embedding models reveals that large instruction-tuned multilingual models achieve the strongest performance, while existing Slovak-specific models trained for NLU tasks transfer poorly to embedding tasks. To address the need for efficient, locally-deployable Slovak embeddings, we develop \texttt{e5-sk-small} (45M parameters) and \texttt{e5-sk-large} (365M) by applying vocabulary trimming and fine-tuning to Multilingual E5 models. Despite size reductions of up to 62\%, our open-source models achieve competitive performance with proprietary APIs while remaining locally deployable for semantic search and retrieval-augmented generation (RAG). We release the benchmark, models, datasets, and code openly, hoping our approach offers a replicable path for other under-resourced languages.

### 🤖 AI 总结

**一句话总结**：We introduce SkMTEB, the first comprehensive MTEB-style text embedding benchmark for Slovak, a low-resource West Slavic language, comprising 31 datasets across 7 task types -- nearly 4$\times$ the dep...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SkMTEB, Slovak, Massive, Text, Embedding, Benchmark, Model, Adaptation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13647v1) | [下载PDF](https://arxiv.org/pdf/2606.13647v1.pdf)

---

## [16. Operads for compositional reasoning in LLMs](https://arxiv.org/abs/2606.13634v1)

**作者**：Nathaniel Bottman, Kyle Richardson  
**分类**：cs.CL, math.CT  
**发布时间**：2026-06-11

### 📄 论文摘要

Question decomposition, i.e. breaking a complex query into simpler sub-queries whose answers are composed to produce a final answer, is a widely used strategy for improving LLM reasoning, yet it currently lacks a rigorous mathematical foundation. In this paper, we propose operads, mathematical structures that model many-in, one-out operations and compositions thereof, as a natural framework for describing question decomposition. We define the questions operad $Q$, in which operations correspond to question templates and composition corresponds to substitution of sub-answers, and show how QA models can be interpreted as algebras over $Q$. Beyond reframing existing practice, this operadic perspective points toward new methods, in particular a notion of operadic consistency, which measures whether a QA model's answers agree across the partial collapses of a question decomposition tree. Empirical evaluation of operadic consistency is reported in our companion paper (Bottman, Liu, and Richardson, 2026), which finds it strongly correlated with accuracy across twelve LLMs and four multi-hop QA datasets and outperforming standard temperature-based self-consistency baselines. We argue that operads are the natural mathematical home for question decomposition, and that invariants such as operadic consistency open new directions for analyzing and improving the reliability of multi-step reasoning.

### 🤖 AI 总结

**一句话总结**：Question decomposition, i.e. breaking a complex query into simpler sub-queries whose answers are composed to produce a final answer, is a widely used strategy for improving LLM reasoning, yet it curre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, i.e, Operads, compositional, reasoning, Question, decomposition, breaking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13634v1) | [下载PDF](https://arxiv.org/pdf/2606.13634v1.pdf)

---

## [17. One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative Recommenders](https://arxiv.org/abs/2606.13610v1)

**作者**：Minghao Luo, Liang Chen  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-11

### 📄 论文摘要

Search-augmented LLMs increasingly mediate everyday consumer recommendations by retrieving live web content. This creates a new risk: generative recommenders may consume polluted web content, such as fake reviews and promotional pages crafted to mislead recommendations. We ask: to what extent do search-augmented LLMs become unwitting promoters of fake products when consuming polluted retrieval results? To answer this, we introduce FORGE (Fake Online Recommendations in Generative Environments), a benchmark for measuring fake-product promotion under controlled web-content pollution. Given an upstream search result, FORGE locally rewrites real products in retrieved web pages into fake ones to simulate web-content pollution, and measures how often the LLM recommends the fake product. FORGE covers 225 real-world products across 15 categories and 5 consumer scenarios. Across 12 commercial and open-weights LLMs, all models are vulnerable: a single polluted page yields fooled rates of up to 27%, while the full top-3 replacement raises this to 73.8%. Vulnerability varies substantially across categories, increasing when models lack stable prior knowledge of the relevant products. Reasoning does not mitigate this vulnerability; instead, it often generates spurious social proof to justify false recommendations. We evaluate three defenses: skepticism prompting and consensus filtering (over model priors or cross-document evidence). Skepticism can exacerbate vulnerability, much like reasoning, while filtering risks suppressing legitimate products. We release FORGE at https://github.com/leoluolol/forge-benchmark.

### 🤖 AI 总结

**一句话总结**：Search-augmented LLMs increasingly mediate everyday consumer recommendations by retrieving live web content. This creates a new risk: generative recommenders may consume polluted web content, such as ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：One, Polluted, Page, Enough, Evaluating, Web, Content, Pollution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13610v1) | [下载PDF](https://arxiv.org/pdf/2606.13610v1.pdf)

---

## cs.CV

## [18. InterleaveThinker: Reinforcing Agentic Interleaved Generation](https://arxiv.org/abs/2606.13679v1)

**作者**：Dian Zheng, Harry Lee, Manyuan Zhang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-11

### 📄 论文摘要

Recent image generators have demonstrated impressive photorealism and instruction-following capabilities in single-image generation and editing. However, constrained by their architectures, they cannot achieve interleaved generation (text-image sequence), which has crucial applications in visual narratives, guidance, and embodied manipulation. Even the latest open-source Unified Multimodal Models (UMMs) exhibit limited performance in this regard. In this paper, we introduce InterleaveThinker, the first multi-agent pipeline designed to endow any existing image generator with interleaved generation capabilities. Specifically, we employ a planner agent to organize the image-text input sequence, instructing the image generator on the required execution at each step. Subsequently, we introduce a critic agent to evaluate the generator's outputs, identify samples that deviate from the planned instructions, and refine the instructions for regeneration. To implement this pipeline, we construct the Interleave-Planner-SFT-80k and Interleave-Critic-SFT-112k to perform a format cold-start. Then we develop Interleave-Critic-RL-13k to reinforce the step-wise instruction correction capability within a generation trajectory using GRPO. Since a single interleaved generation trajectory may involve over 25 generator calls, optimizing the entire trajectory is computationally impractical. Therefore, we propose accuracy reward and step-wise reward, allowing single-step RL to effectively guide the entire generation trajectory. The results show that InterleaveThinker improves performance across various image generators. On interleaved generation benchmarks, it achieves performance comparable to Nano Banana and GPT-5. Surprisingly, it also significantly enhances the base model on reasoning-based benchmarks; for example, on 4-step FLUX.2-klein, we observe substantial gains on WISE and RISE.

### 🤖 AI 总结

**一句话总结**：Recent image generators have demonstrated impressive photorealism and instruction-following capabilities in single-image generation and editing. However, constrained by their architectures, they canno...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：InterleaveThinker, Reinforcing, Agentic, Interleaved, Generation, Recent, image, generators

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13679v1) | [下载PDF](https://arxiv.org/pdf/2606.13679v1.pdf)

---

## [19. Modality Forcing for Scalable Spatial Generation](https://arxiv.org/abs/2606.13676v1)

**作者**：Bardienus Pieter Duisterhof, Deva Ramanan, Jeffrey Ichnowski 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-11

### 📄 论文摘要

Text-to-image (T2I) models contain rich spatial priors. Synthesizing photorealistic, cluttered scenes requires an understanding of geometry, including perspective and relative scale. Prior works adapt T2I models to leverage this prior for depth prediction, but they require dense depth data and involve complex recipes. We propose Modality Forcing, a simple, scalable post-training recipe for joint image-depth generation using a single DiT trained on sparse depth data. Modality Forcing enables conditional and joint generation of image and depth in any permutation by assigning separate noise levels per modality. Per-modality decoders let us train on sparse, real-world depth and achieve strong, generalizable depth prediction. We further show that Modality Forcing inherits the scalability of T2I pre-training: by training a set of T2I models from scratch (370M to 3.3B parameters), we find that larger models trained on more image data produce more accurate depth. Our strongest model is competitive with state-of-the-art monocular depth estimators and reduces AbsRel by 57% relative to existing joint image-depth generative models. These results provide strong evidence that image generation is a scalable pre-training objective for spatial perception. https://modality-forcing.github.io/

### 🤖 AI 总结

**一句话总结**：Text-to-image (T2I) models contain rich spatial priors. Synthesizing photorealistic, cluttered scenes requires an understanding of geometry, including perspective and relative scale. Prior works adapt...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：T2I, Modality, Forcing, Scalable, Spatial, Generation, Text-to-image, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13676v1) | [下载PDF](https://arxiv.org/pdf/2606.13676v1.pdf)

---

## [20. SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning](https://arxiv.org/abs/2606.13673v1)

**作者**：Seokju Cho, Ryo Hachiuma, Abhishek Badki 等 11 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-11

### 📄 论文摘要

Spatial reasoning, the ability to determine where objects are, how they relate, and how they move in 3D, remains a fundamental challenge for vision-language models (VLMs). Tool-augmented agents attempt to address this by augmenting VLMs with specialist perception modules, yet their effectiveness is bounded by the action interface through which those tools are invoked. In this work, we study how the design of this interface shapes the agent's capacity for open-ended spatial reasoning. Existing spatial agents either employ single-pass code execution, which commits to a full analysis strategy before any intermediate result is observed, or rely on a structured tool-call interface that often offers less flexibility for freely composing operations or tailoring the analysis to each task. Both designs offer limited flexibility for open-ended, complex 3D/4D spatial reasoning. We therefore propose SpatialClaw, a training-free framework for spatial reasoning that adopts code as the action interface. SpatialClaw maintains a stateful Python kernel pre-loaded with input frames and a suite of perception and geometry primitives, letting a VLM-backed agent write one executable cell per step conditioned on all prior outputs, enabling the agent to flexibly compose and manipulate perception results and adapt its analysis to both intermediate text and visual observations and the demands of each problem. Evaluated across 20 spatial reasoning benchmarks spanning a broad range of static and dynamic 3D/4D spatial reasoning tasks, SpatialClaw achieves 59.9% average accuracy, outperforming the recent spatial agent by +11.2 points, with consistent gains across six VLM backbones from two model families without any benchmark- or model-specific adaptation.

### 🤖 AI 总结

**一句话总结**：Spatial reasoning, the ability to determine where objects are, how they relate, and how they move in 3D, remains a fundamental challenge for vision-language models (VLMs). Tool-augmented agents attemp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SpatialClaw, Rethinking, Action, Interface, Agentic, Spatial, Reasoning, ability

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13673v1) | [下载PDF](https://arxiv.org/pdf/2606.13673v1.pdf)

---

## [21. Revisiting Vehicle Color Recognition in Long-Tailed Surveillance Scenarios](https://arxiv.org/abs/2606.13625v1)

**作者**：Vinícius Orrú, Bruno H. Foggiatto, Gabriel E. Lima 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-11

### 📄 论文摘要

Vehicle color recognition is an important cue for vehicle identification in surveillance systems, especially when license plates are illegible due to low resolution, occlusion, motion blur, or poor illumination. However, real-world vehicle color distributions are highly imbalanced, making overall accuracy insufficient to assess performance on rare but operationally relevant colors. This paper presents a comprehensive study of vehicle color recognition under severe class imbalance using UFPR-VeSV, a challenging real-world surveillance dataset. We investigate synthetic minority-class augmentation through two off-the-shelf generative strategies: text-conditioned image generation with RunDiffusion/JuggernautXL and image-conditioned color editing with Gemini 2.0 Flash. The curated synthetic data are combined with modern visual representations, loss reweighting, learning-rate scheduling, color-safe augmentation, foreground-aware preprocessing, and ensemble fusion. The bestperforming approach achieves 94.6% micro accuracy and 79.7% macro accuracy, improving macro accuracy by 8.2 percentage points over recent literature. A manual error analysis further shows that many remaining failures are visually ambiguous even for human annotators, highlighting the practical limits of color-based vehicle identification in unconstrained surveillance imagery. The generated images and source code are publicly available at https://github.com/viniciusorru/vcr-synthetic

### 🤖 AI 总结

**一句话总结**：Vehicle color recognition is an important cue for vehicle identification in surveillance systems, especially when license plates are illegible due to low resolution, occlusion, motion blur, or poor il...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Revisiting, Vehicle, Color, Recognition, Long-Tailed, Surveillance, Scenarios

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13625v1) | [下载PDF](https://arxiv.org/pdf/2606.13625v1.pdf)

---

## [22. Towards Effective Waste Segmentation for Automated Waste Recycling in Cluttered Background](https://arxiv.org/abs/2606.13587v1)

**作者**：Mamoona Javaid, Mubashir Noman, Abdul Hannan 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-11

### 📄 论文摘要

Rapid expansion of urban areas and population growth is causing an immense increase in waste production, which demands the need for efficient and automated waste management. In this scenario, automated waste recycling (AWR) using deep learning methods can assist humans in optimal waste management. Recent deep learning approaches for AWR provide promising waste segmentation performance, however, these methods rely on large backbone networks that are inefficient for AWR systems and suffer from performance deterioration in cluttered scenes. To this end, an optimal waste segmentation network is introduced which effectively utilizes the spatial domain to capture localized structural dependencies and the spectral domain to efficiently extract global contextual relationships. This cascaded design allows the network to progressively leverage both local and global representations across complementary domains to highlight the semantic information necessary for effective segmentation of various waste objects. Furthermore, auxiliary feature enhancement module (AFEM) is introduced to enhance the target objects' boundaries and blob amplification for better segmentation in cluttered scenarios. Extensive experimentation on ZeroWaste-aug, ZeroWaste-f and SpectralWaste datasets reveals the merits of the proposed method.

### 🤖 AI 总结

**一句话总结**：Rapid expansion of urban areas and population growth is causing an immense increase in waste production, which demands the need for efficient and automated waste management. In this scenario, automate...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Towards, Effective, Waste, Segmentation, Automated, Recycling, Cluttered, Background

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13587v1) | [下载PDF](https://arxiv.org/pdf/2606.13587v1.pdf)

---

## [23. EvTexture++: Event-Driven Texture Enhancement for Video Super-Resolution](https://arxiv.org/abs/2606.13580v1)

**作者**：Dachun Kai, Jiayao Lu, Yueyi Zhang 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-11

### 📄 论文摘要

Event-based vision has drawn increasing attention owing to its distinctive properties, including ultra-high temporal resolution and extreme dynamic range. Recent works have introduced it to video super-resolution (VSR) to enhance flow estimation and temporal alignment. In contrast, this paper shifts the focus of event signals from motion refinement to texture enhancement in VSR. We propose EvTexture++, the first event-driven framework dedicated to texture enhancement in VSR. It leverages high-frequency spatiotemporal details from events to improve texture recovery. EvTexture++ incorporates a customized texture enhancement branch, along with an iterative texture enhancement module that progressively exploits high-temporal-resolution event information for texture restoration. This enables gradual refinement of texture regions across iterations, yielding more accurate and detailed high-resolution outputs. Besides intra-frame texture recovery, large motions could degrade inter-frame temporal consistency, particularly in texture regions, leading to texture flickering. To mitigate this, we further exploit the continuous-time motion cues of events to enhance temporal consistency, introducing a temporal texture alignment module that estimates event-guided texture-aware flow for precise inter-frame texture alignment. Moreover, EvTexture++ is designed as a plug-and-play tool to flexibly boost the performance of existing VSR models. Experiments on five datasets demonstrate that EvTexture++ achieves state-of-the-art performance. When integrated into recent VSR models, it yields significant improvements, with gains of up to 1.55 dB in PSNR on the texture-rich Vid4 dataset. Code: https://github.com/DachunKai/EvTexture.

### 🤖 AI 总结

**一句话总结**：Event-based vision has drawn increasing attention owing to its distinctive properties, including ultra-high temporal resolution and extreme dynamic range. Recent works have introduced it to video supe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EvTexture++, Event-Driven, Texture, Enhancement, Video, Super-Resolution, Event-based, vision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13580v1) | [下载PDF](https://arxiv.org/pdf/2606.13580v1.pdf)

---

## cs.LG

## [24. Understanding Truncated Positional Encodings for Graph Neural Networks](https://arxiv.org/abs/2606.13671v1)

**作者**：James Flora, Mitchell Black, Weng-Keen Wong 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-11

### 📄 论文摘要

Positional encodings (PEs) enhance the power of graph neural networks (GNNs), both theoretically and empirically. Two of the most popular families of PEs - spectral (e.g., Laplacian eigenspaces, effective resistance) and walk-based (polynomials of the adjacency matrix) - are theoretically equivalent in expressive power, with expressivity between the 1-WL and 3-WL tests. However, this equivalence assumes the GNN uses the "complete" version of these PEs, which requires $O(n^3)$ time and space complexity. Instead, practitioners commonly use truncated variants of these encodings, such as the first $k$ eigenspaces or powers of the adjacency matrix. However, the theoretical properties of these truncated PEs are unknown. In this work, we initiate the study of these truncated PEs. Theoretically, we show that, under truncation, several families of PEs are fundamentally different in expressive power. As a corollary, we show that truncated spectral PEs are no longer stronger than the 1-WL test. We also study a family of spectral PEs, the $k$-harmonic distances, to highlight the differences in expressive power of even closely related truncated PEs. Finally, we experimentally show that a mix of truncated PEs is preferable to any single family on real-world datasets.

### 🤖 AI 总结

**一句话总结**：Positional encodings (PEs) enhance the power of graph neural networks (GNNs), both theoretically and empirically. Two of the most popular families of PEs - spectral (e.g., Laplacian eigenspaces, effec...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Understanding, Truncated, Positional, Encodings, Graph, Neural, Networks, PEs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13671v1) | [下载PDF](https://arxiv.org/pdf/2606.13671v1.pdf)

---

## [25. Dense Supervision, Sparse Updates: On the Sparsity and Geometry of On-Policy Distillation](https://arxiv.org/abs/2606.13657v1)

**作者**：Guo Yu, Wenlin Liu, Yulan Hu 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-11

### 📄 论文摘要

On-policy distillation (\textsc{OPD}) has recently become a prominent post-training recipe as it combines two desirable ingredients: on-policy student trajectories and dense teacher supervision, yet how this hybrid changes a model's parameters remains unclear. Across several language and vision-language model pairs and use cases, our analysis yields two main findings. On sparsity, \textsc{OPD}-style updates are small and coordinate-sparse. They are distributed across layers and are usually FFN-heavy. This sparse structure is operationally useful: training only the discovered subnetwork recovers nearly the same performance as full \textsc{OPD}. However, the sparsity-inducing SGD optimizer underperforms AdamW in our optimizer ablation, likely because dense teacher supervision preserves heterogeneous coordinate-wise gradient scales where AdamW's adaptive scaling remains useful. On geometry, the updates are numerically full-rank but spectrally concentrated; they lie mostly away from the principal singular subspaces of the source weights and fall disproportionately on coordinates where the source weights are close to zero. These findings suggest that dense teacher supervision does not turn \textsc{OPD} into ordinary dense parameter rewriting; instead, \textsc{OPD} retains important geometric signatures of on-policy post-training.

### 🤖 AI 总结

**一句话总结**：On-policy distillation (\textsc{OPD}) has recently become a prominent post-training recipe as it combines two desirable ingredients: on-policy student trajectories and dense teacher supervision, yet h...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Dense, Supervision, Sparse, Updates, Sparsity, Geometry, On-Policy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13657v1) | [下载PDF](https://arxiv.org/pdf/2606.13657v1.pdf)

---

## [26. The Stable Recovery Manifold: Geometric Principles Governing Recoverability in Continual Learning](https://arxiv.org/abs/2606.13637v1)

**作者**：Ayushman Trivedi, Bhavika Melwani  
**分类**：cs.LG  
**发布时间**：2026-06-11

### 📄 论文摘要

Catastrophic forgetting is often viewed as the destruction of previously learned knowledge during sequential learning. Building on the Accessibility Collapse framework, we investigate the geometric structure of recoverability in continual learning. Using Split CIFAR-100 and a sequentially trained ResNet-18, we analyze recoverability, representational drift, and recovery complexity across ten tasks. We introduce Recovery Subspace Dimensionality (k_t), a measure of the minimum number of singular directions required to preserve 90 percent of full probe performance. Contrary to our Recoverability Diffusion hypothesis, recovery dimensionality remains stable throughout training (mean k_t = 8.0) despite substantial representational drift. Principal-angle drift strongly predicts recoverability (r = -0.862), and a simple geometric model explains 82.2 percent of recoverability variance. These findings support the Stable Recovery Manifold hypothesis, suggesting that forgotten knowledge remains compactly decodable despite representational reorganization. The results indicate that catastrophic forgetting is primarily an accessibility and manifold-alignment problem rather than information destruction.

### 🤖 AI 总结

**一句话总结**：Catastrophic forgetting is often viewed as the destruction of previously learned knowledge during sequential learning. Building on the Accessibility Collapse framework, we investigate the geometric st...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Stable, Recovery, Manifold, Geometric, Principles, Governing, Recoverability, Continual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13637v1) | [下载PDF](https://arxiv.org/pdf/2606.13637v1.pdf)

---

## [27. Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models](https://arxiv.org/abs/2606.13603v1)

**作者**：Daniel Scalena, Sara Candussio, Luca Bortolussi 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-06-11

### 📄 论文摘要

Chain-of-thought (CoT) reasoning is the dominant paradigm for inference-time scaling in language models, yet the causal influence of individual steps on the final answer poorly understood. We estimate each step's causal importance via early exit and use this measure to study how answers form across the reasoning traces of several model families. Across diverse tasks, we find that reasoning typically crosses a \emph{commitment boundary} -- a sharp transition from transient intermediate guesses to a stable, high-confidence answer. This transition often happens in a single step, well before the model's reasoning block ends, and is followed by \emph{epiphenomenal} CoT steps that leave the final answer probability unaltered. Using attention probes, we show that answer-formation stages can be linearly decoded from intermediate reasoning steps with high accuracy and generalize robustly to unseen reasoning tasks. We exploit this signal to early-exit reasoning blocks at the commitment boundary, reducing the length of CoTs up to 55\% on average with negligible impact on model performance.

### 🤖 AI 总结

**一句话总结**：Chain-of-thought (CoT) reasoning is the dominant paradigm for inference-time scaling in language models, yet the causal influence of individual steps on the final answer poorly understood. We estimate...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Commitment, Boundary, Probing, Epiphenomenal, Chain-of-Thought, Large, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13603v1) | [下载PDF](https://arxiv.org/pdf/2606.13603v1.pdf)

---

## [28. Simplex-Constrained Sparse Bagging: Transitioning from Uniform Priors to Sparse Posteriors in Ensemble Learning](https://arxiv.org/abs/2606.13589v1)

**作者**：Meher Sai Preetam, Meher Bhaskar  
**分类**：cs.LG  
**发布时间**：2026-06-11

### 📄 论文摘要

We present Simplex-Constrained Sparse Bagging (SCSB), a mathematically rigorous framework for post-training compression and probability calibration of bootstrap-based bagging ensembles. Standard bagging ensembles (such as Random Forests, Bagged SVMs, and Bagged Neural Networks) assign uniform voting power to all constituent estimators. However, this naive uniform prior ignores the varying local competence of base estimators and contributes to model overconfidence. We formulate ensemble pruning and calibration as a joint optimization problem over the probability simplex by minimizing the Out-Of-Bag (OOB) loss. To induce sparsity, we address the theoretical "L1-simplex paradox" -- the mathematical reality that the L1 norm is constant on the simplex and fails to prune -- by introducing a concave quadratic penalty. SCSB is model-agnostic and achieves up to 96% ensemble compression, yielding linear inference speedups and superior probability calibration (lowered Expected Calibration Error) while preserving or enhancing generalization accuracy.

### 🤖 AI 总结

**一句话总结**：We present Simplex-Constrained Sparse Bagging (SCSB), a mathematically rigorous framework for post-training compression and probability calibration of bootstrap-based bagging ensembles. Standard baggi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Simplex-Constrained, Sparse, Bagging, Transitioning, Uniform, Priors, Posteriors, Ensemble

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13589v1) | [下载PDF](https://arxiv.org/pdf/2606.13589v1.pdf)

---

## [29. Existence Precedes Value: Joint Modeling of Observational Existence and Evolving States in Time Series Forecasting](https://arxiv.org/abs/2606.13571v1)

**作者**：Yifan Hu, Hongzhou Chen, Peiyuan Liu 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-11

### 📄 论文摘要

Real-world time series are often highly incomplete and irregular due to sensor dormancy, transmission delays, and event-driven sampling, making reliable forecasting fundamentally challenging. Existing methods have evolved from impute-then-forecast pipelines to continuous-time models such as Neural ODEs and continuous-time graph networks. While these approaches improve the modeling of historical irregularity, they still rely on an implicit oracle assumption at inference time: the timestamps of future valid observations are presumed to be known in advance. This assumption limits practical relevance, since in many real systems the more fundamental question is not only what the future value will be, but also whether a valid observation will occur at all. In this paper, we propose Timeflies, a unified framework that reformulates forecasting as a joint problem of future observability inference and value estimation. To explicitly model the interaction between observation dynamics and state evolution, Timeflies adopts an observation stream and a value stream, coupled through three dedicated modules for reliability-aware embedding, observation-guided dependency modeling, and joint prediction. We further construct Shadow, a benchmark that combines natural missingness from public datasets with real-world industrial data, and introduce the Observation-Value Joint Entropy (OVJE) metric to comprehensively evaluate this coupled predictability. Extensive experiments show that Timeflies consistently outperforms existing methods, highlighting the importance of explicitly modeling future observability in time series forecasting with missing values. Code and dataset are available in https://github.com/ant-intl/Timeflies.

### 🤖 AI 总结

**一句话总结**：Real-world time series are often highly incomplete and irregular due to sensor dormancy, transmission delays, and event-driven sampling, making reliable forecasting fundamentally challenging. Existing...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Existence, Precedes, Value, Joint, Modeling, Observational, Evolving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13571v1) | [下载PDF](https://arxiv.org/pdf/2606.13571v1.pdf)

---

## [30. Adjusted Cup-Product Neural Layer](https://arxiv.org/abs/2606.13568v1)

**作者**：Snigdha Chandan Khilar  
**分类**：cs.LG, math-ph  
**发布时间**：2026-06-11

### 📄 论文摘要

Many important observables in physics and geometry are cup products of cochains. The adjusted cup product neural layer has been introduced in this paper. It is a neural primitive that hard wires the cup product with an adjustment term from higher gauge theory. This creates a readout that is gauge invariant by design. Their main theoretical result shows that on a closed cycle the output relies entirely on the adjustment coefficient. Setting this coefficient to zero removes the output completely regardless of other parameters. Thus the adjustment is the only source of gauge invariant signal. They prove this observable is a nonzero quadratic form and is exactly invariant under one and two gauge transformations.

### 🤖 AI 总结

**一句话总结**：Many important observables in physics and geometry are cup products of cochains. The adjusted cup product neural layer has been introduced in this paper. It is a neural primitive that hard wires the c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Adjusted, Cup-Product, Neural, Layer, Many, important, observables, physics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.13568v1) | [下载PDF](https://arxiv.org/pdf/2606.13568v1.pdf)

---

