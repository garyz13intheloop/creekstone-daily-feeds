# arXiv AI 论文日报 | 2026-05-19

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (13 篇)
- [cs.CL](#csCL) (3 篇)
- [cs.AI](#csAI) (8 篇)
- [cs.LG](#csLG) (6 篇)

---

## cs.AI

## [1. Actionable World Representation](https://arxiv.org/abs/2605.18743v1)

**作者**：Kunqi Xu, Jitao Li, Jianglong Ye 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-18

### 📄 论文摘要

Inspired by the emergent behaviors in large language models that generalized human intelligence, the research community is pursuing similar emergent capabilities within world models, with a emphasis on modeling the physical world. Within the scope of physical world model, objects are the fundamental primitives that constitute physical reality. From humans to computers, nearly everything we interact with is an object. These objects are rarely static; they are actionable entities with varying states determined by their intrinsic properties. While current methods approach object action states either via video generation or dynamic scene reconstruction, none explicitly model this basic element in a unified, principled way to build an actionable object representation. We propose WorldString, a neural architecture capable of modeling the state manifold of real-world objects by learning directly from point clouds or RGB-D video streams. Serving as a versatile digital twin, it acts as a foundational building block for physical world models; thus, we name it WorldString. Sweetly, its fully differentiable structure seamlessly enables future integration with policy learning and neural dynamics.

### 🤖 AI 总结

**一句话总结**：Inspired by the emergent behaviors in large language models that generalized human intelligence, the research community is pursuing similar emergent capabilities within world models, with a emphasis o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Actionable, World, Representation, Inspired, emergent, behaviors, large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18743v1) | [下载PDF](https://arxiv.org/pdf/2605.18743v1.pdf)

---

## [2. What Does the AI Doctor Value? Auditing Pluralism in the Clinical Ethics of Language Models](https://arxiv.org/abs/2605.18738v1)

**作者**：Payal Chandak, Victoria Alkin, David Wu 等 14 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-18

### 📄 论文摘要

Medicine is inherently pluralistic. Principles such as autonomy, beneficence, nonmaleficence, and justice routinely conflict, and such ethical dilemmas often sharply divide reasonable physicians. Good clinical practice navigates these tensions in concert with each patient's values rather than imposing a single ethical stance. The ethical values that large language models bring to medical advice, however, have not been systematically examined. We present a framework for auditing value pluralism in medical AI, comprising a benchmark of clinician-verified dilemmas and an attribution method that recovers value priorities directly from decisions. The ecosystem of frontier models spans physician-level value heterogeneity, and models discuss competing values in their reasoning (Overton pluralism) before committing to a decision. However, individual model decisions are near-deterministic across repeated sampling and semantic variations, failing to reproduce the distributional pluralism of the physician panel. Across benchmark cases, these consistent decisions reflect committed, systematic value preferences. While most model priorities fall within the natural range of inter-physician variation, some significantly underweight patient autonomy. A single LLM deployed without regard for its value priorities could amplify those priorities at scale to every patient it serves. Without explicit efforts to balance ethical perspectives with one or multiple models, these tools risk replacing clinical pluralism with a deployment monoculture.

### 🤖 AI 总结

**一句话总结**：Medicine is inherently pluralistic. Principles such as autonomy, beneficence, nonmaleficence, and justice routinely conflict, and such ethical dilemmas often sharply divide reasonable physicians. Good...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：What, Does, Doctor, Value?, Auditing, Pluralism, Clinical, Ethics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18738v1) | [下载PDF](https://arxiv.org/pdf/2605.18738v1.pdf)

---

## [3. SkillGenBench: Benchmarking Skill Generation Pipelines for LLM Agents](https://arxiv.org/abs/2605.18693v1)

**作者**：Yifan Zhou, Zhentao Zhang, Ziming Cheng 等 11 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-18

### 📄 论文摘要

As LLM agents are increasingly built around reusable skills, a central challenge is no longer only whether agents can use provided skills, but whether they can generate correct, reusable, and executable skills from repositories and documents. Existing benchmarks primarily evaluate the efficacy of given skills or the ability of agents to solve downstream tasks from raw context, but they do not isolate skill generation itself as the object of study. We introduce SkillGenBench, a benchmark for evaluating skill generation pipelines under a unified and controlled protocol. In SkillGenBench, a generator receives raw corpora and produces standardized skill artifacts, which are then executed under fixed harnesses and assessed with unified evaluation procedures. The benchmark covers two generation regimes: task-conditioned generation, where a task-specific skill is synthesized after the task is revealed, and task-agnostic generation, where a reusable skill library must be distilled before downstream tasks are known. It also spans two complementary procedural sources: repository-grounded instances, where procedures are distributed across code, configuration, and scripts, and document-grounded instances, where procedures and constraints must be distilled from long-form text. We provide standardized task specifications, pinned environments, and evaluation protocols centered on deterministic execution-based checks, supplemented by auxiliary signals for diagnosis. Experiments across a range of skill-generation methods and backbones show substantial performance variation, highlight the difficulty of reusable skill distillation, and reveal distinct failure modes in skill generation from software repositories versus long-form documents. SkillGenBench establishes a reproducible testbed for studying skill generation as an independent research problem in agent systems.

### 🤖 AI 总结

**一句话总结**：As LLM agents are increasingly built around reusable skills, a central challenge is no longer only whether agents can use provided skills, but whether they can generate correct, reusable, and executab...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, As, SkillGenBench, Benchmarking, Skill, Generation, Pipelines

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18693v1) | [下载PDF](https://arxiv.org/pdf/2605.18693v1.pdf)

---

## [4. Democratizing Large-Scale Re-Optimization with LLM-Guided Model Patches](https://arxiv.org/abs/2605.18692v1)

**作者**：Tinghan Ye, Arnaud Deza, Ved Mohan 等 5 位作者  
**分类**：cs.AI, math.OC  
**发布时间**：2026-05-18

### 📄 论文摘要

Optimization models developed by operations research (OR) experts are often deployed as decision-support systems in industrial settings. However, real-world environments are dynamic, with evolving business rules, previously overlooked constraints, and unforeseen perturbations. In such contexts, end users must rapidly re-optimize models to recover feasible and implementable solutions. This paper introduces an agentic re-optimization framework in which a large language model (LLM) acts as an OR expert, dynamically supporting end users through natural-language interaction. The LLM translates user prompts into structured updates of the underlying optimization model, selects suitable re-optimization techniques from an optimization toolbox, and solves the resulting instance to return implementable solutions. The toolbox leverages primal information, including historical solutions, valid inequalities, solver configurations, and metaheuristics, to accelerate re-optimization while preserving solution quality. The proposed framework enables interactive and continuous adaptation of deployed optimization models, reducing dependence on OR experts and improving the sustainability of decision-support systems. Extensive experiments on two complementary large-scale real-world case studies demonstrate the effectiveness and scalability of the proposed framework. The first considers online supply chain re-optimization, where solutions must be generated rapidly while remaining close to the deployed plan, whereas the second focuses on offline university exam scheduling, where solution quality is prioritized over runtime. Results show that the toolbox-driven architecture significantly improves computational efficiency through primal-based and solver-aware re-optimization techniques, while the structured patch-based updates improve interpretability and traceability of model modifications.

### 🤖 AI 总结

**一句话总结**：Optimization models developed by operations research (OR) experts are often deployed as decision-support systems in industrial settings. However, real-world environments are dynamic, with evolving bus...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Democratizing, Large-Scale, Re-Optimization, LLM-Guided, Model, Patches, Optimization, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18692v1) | [下载PDF](https://arxiv.org/pdf/2605.18692v1.pdf)

---

## [5. Learning Quantifiable Visual Explanations Without Ground-Truth](https://arxiv.org/abs/2605.18681v1)

**作者**：Amritpal Singh, Andrey Barsky, Mohamed Ali Souibgui 等 5 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-05-18

### 📄 论文摘要

Explainable AI (XAI) techniques are increasingly important for the validation and responsible use of modern deep learning models, but are difficult to evaluate due to the lack of good ground-truth to compare against. We propose a framework that serves as a quantifiable metric for the quality of XAI methods, based on continuous input perturbation. Our metric formally considers the sufficiency and necessity of the attributed information to the model's decision-making, and we illustrate a range of cases where it aligns better with human intuitions of explanation quality than do existing metrics.   To exploit the properties of this metric, we also propose a novel XAI method, considering the case where we fine-tune a model using a differentiable approximation of the metric as a supervision signal. The result is an adapter module that can be trained on top of any black-box model to output causal explanations of the model's decision process, without degrading model performance. We show that the explanations generated by this method outperform those of competing XAI techniques according to a number of quantifiable metrics.

### 🤖 AI 总结

**一句话总结**：Explainable AI (XAI) techniques are increasingly important for the validation and responsible use of modern deep learning models, but are difficult to evaluate due to the lack of good ground-truth to ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Quantifiable, Visual, Explanations, Without, Ground-Truth, Explainable, XAI

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18681v1) | [下载PDF](https://arxiv.org/pdf/2605.18681v1.pdf)

---

## [6. Efficient Lookahead Encoding and Abstracted Width for Learning General Policies in Classical Planning](https://arxiv.org/abs/2605.18674v1)

**作者**：Michael Aichmüller, Simon Ståhlberg, Martin Funkquist 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-18

### 📄 论文摘要

Generalized planning aims to learn policies that generalize across collections of instances within a classical planning domain. Recent Graph Neural Network (GNN) approaches have learned nearly perfect policies for several domains. This work improves on the recently published idea of Iterated Width (IW) policies. Therein, the policy broadens its successor scope through an IW-lookahead search that can "jump" over multiple transitions, simplifying the problem structure. Yet, each transition is evaluated individually, leading to unscalable compute costs and expressivity limitations. Furthermore, although IW(1) is attractive because it scales linearly with the number of atoms, it becomes inefficient once thousands of objects are considered, as in the International Planning Competition (IPC) 2023 benchmark. We address both limitations. First, we introduce a vastly more efficient holistic encoding of the entire search tree. It jointly represents IW(1)-reachable states only by their relational differences to the current state, enabling Relational GNNs (R-GNNs) to score all transitions in a single forward pass. Second, we define Abstracted IW(1) to improve scaling through relational abstraction during novelty checks. Rather than testing fully instantiated atoms, it abstracts each atom by replacing all but one argument with its type. The original atom is novel if any of its abstracted forms is novel. This structural compression shifts novelty search scaling from atoms to objects, while preserving meaningful subgoal structure. We evaluate our contributions on the hyperscaling IPC 2023 benchmark and across diverse domains, including domains requiring features beyond the $C_2$ logic fragment. Our policies achieve new state-of-the-art performance, significantly surpassing prior work, including the classical planner LAMA.

### 🤖 AI 总结

**一句话总结**：Generalized planning aims to learn policies that generalize across collections of instances within a classical planning domain. Recent Graph Neural Network (GNN) approaches have learned nearly perfect...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Efficient, Lookahead, Encoding, Abstracted, Width, Learning, General, Policies

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18674v1) | [下载PDF](https://arxiv.org/pdf/2605.18674v1.pdf)

---

## [7. Position: A Three-Layer Probabilistic Assume-Guarantee Architecture Is Structurally Required for Safe LLM Agent Deployment](https://arxiv.org/abs/2605.18672v1)

**作者**：S. Bensalem, Y. Dong, M. Franzle 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-18

### 📄 论文摘要

This position paper argues that enforcing LLM agent safety within a single abstraction layer is not merely suboptimal but categorically insufficient for deployed LLM agents -- a structural consequence of how agent execution works, not a contingent limitation of current systems. The three dimensions that jointly constitute safe operation -- semantic intent and policy compliance, environmental validity, and dynamical feasibility -- each depend on a strictly distinct set of information that becomes available at different stages of execution. No single guardrail can certify all three. We argue that the community must respond with a contract-based architecture in which each safety dimension is enforced by an independently certified layer whose probabilistic guarantee satisfies the next layer's assumption. We sketch such an architecture and derive the compositional system-level safety bounds it admits via the chain rule of probability. Three open problems stand between this and a deployable standard: bound estimation from non-i.i.d.\ traces, graceful degradation of contracts under deployment drift, and extension to multi-agent settings -- the most important unfinished business in LLM agent runtime assurance.

### 🤖 AI 总结

**一句话总结**：This position paper argues that enforcing LLM agent safety within a single abstraction layer is not merely suboptimal but categorically insufficient for deployed LLM agents -- a structural consequence...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Position, Three-Layer, Probabilistic, Assume-Guarantee, Architecture, Structurally, Required, Safe

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18672v1) | [下载PDF](https://arxiv.org/pdf/2605.18672v1.pdf)

---

## [8. GIM: Evaluating models via tasks that integrate multiple cognitive domains](https://arxiv.org/abs/2605.18663v1)

**作者**：Rohit Patel, Alexandre Rezende, Steven McClain  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-05-18

### 📄 论文摘要

As LLM benchmarks saturate, the evaluation community has pursued two strategies to increase difficulty: escalating knowledge demands (GPQA, HLE) or removing knowledge entirely in favor of abstract reasoning (ARC-AGI). The first conflates memorization with capability; the second divorces reasoning from the practical contexts in which it matters. We take a different approach. The Grounded Integration Measure (GIM) is a benchmark of 820 original problems (615 public, 205 private) where difficulty comes from integration; individual problems require coordinating multiple cognitive operations (constraint satisfaction, state tracking, epistemic vigilance, audience calibration) over broadly accessible knowledge, so that reasoning stays grounded in realistic tasks without being gated on specialized expertise. Each problem is an original expert-authored composition, majority with rubric-decomposed scoring (median 6 independently judged criteria). A balanced public--private split provides built-in contamination diagnostic. We calibrate a continuous response 2-parameter logistic (2PL) IRT model over >200k prompt-response pairs across 28 models, producing robust ability estimates that correctly order test-configurations even when raw accuracy is distorted by errors or missing data, addressing a common challenge in benchmark reporting. Using this framework, we present a comprehensive leaderboard spanning 22 models and 47 test-configurations (unique model, thinking-level pairs), and conduct what is to our knowledge the most extensive published study of how test-time compute trades off against model capability on a fixed benchmark: 11 models swept across 35 test-configurations. We observe that within-family configuration choices, such as thinking budget and quantization, matter as much as model selection. We release the evaluation framework, calibrated IRT parameters, and all public problems.

### 🤖 AI 总结

**一句话总结**：As LLM benchmarks saturate, the evaluation community has pursued two strategies to increase difficulty: escalating knowledge demands (GPQA, HLE) or removing knowledge entirely in favor of abstract rea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GIM, Evaluating, models, via, tasks, integrate, multiple, cognitive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18663v1) | [下载PDF](https://arxiv.org/pdf/2605.18663v1.pdf)

---

## cs.CL

## [9. Code as Agent Harness](https://arxiv.org/abs/2605.18747v1)

**作者**：Xuying Ning, Katherine Tieu, Dongqi Fu 等 42 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-05-18

### 📄 论文摘要

Recent large language models (LLMs) have demonstrated strong capabilities in understanding and generating code, from competitive programming to repository-level software engineering. In emerging agentic systems, code is no longer only a target output. It increasingly serves as an operational substrate for agent reasoning, acting, environment modeling, and execution-based verification. We frame this shift through the lens of agent harnesses and introduce code as agent harness: a unified view that centers code as the basis for agent infrastructure. To systematically study this perspective, we organize the survey around three connected layers. First, we study the harness interface, where code connects agents to reasoning, action, and environment modeling. Second, we examine harness mechanisms: planning, memory, and tool use for long-horizon execution, together with feedback-driven control and optimization that make harness reliable and adaptive. Third, we discuss scaling the harness from single-agent systems to multi-agent settings, where shared code artifacts support multi-agent coordination, review, and verification. Across these layers, we summarize representative methods and practical applications of code as agent harness, spanning coding assistants, GUI/OS automation, embodied agents, scientific discovery, personalization and recommendation, DevOps, and enterprise workflows. We further outline open challenges for harness engineering, including evaluation beyond final task success, verification under incomplete feedback, regression-free harness improvement, consistent shared state across multiple agents, human oversight for safety-critical actions, and extensions to multimodal environments. By centering code as the harness of agentic AI, this survey provides a unified roadmap toward executable, verifiable, and stateful AI agent systems.

### 🤖 AI 总结

**一句话总结**：Recent large language models (LLMs) have demonstrated strong capabilities in understanding and generating code, from competitive programming to repository-level software engineering. In emerging agent...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Agent, Code, Harness, Recent, large, language, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18747v1) | [下载PDF](https://arxiv.org/pdf/2605.18747v1.pdf)

---

## [10. Predictable Confabulations: Factual Recall by LLMs Scales with Model Size and Topic Frequency](https://arxiv.org/abs/2605.18732v1)

**作者**：Matthew L. Smith, Jonathan P. Shock, Samuel T. Segun 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-05-18

### 📄 论文摘要

While scaling laws govern aggregate large language model performance, no scaling law has linked factual recall to both model size and training-data composition. We evaluated 38 models on over 8,900 scholarly references evaluated by an automated reference verification system. Recall quality follows a sigmoid in the log-linear combination of model parameter count and topic representation in training data. These two variables alone explain 60% of the variance across 16 dense models from four families, rising to 74-94% within individual families. The form matches a superposition-inspired account in which recall is gated by a signal-to-noise ratio: signal strength scales with concept frequency and the noise floor with model capacity.

### 🤖 AI 总结

**一句话总结**：While scaling laws govern aggregate large language model performance, no scaling law has linked factual recall to both model size and training-data composition. We evaluated 38 models on over 8,900 sc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Predictable, Confabulations, Factual, Recall, Scales, Model, Size

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18732v1) | [下载PDF](https://arxiv.org/pdf/2605.18732v1.pdf)

---

## [11. EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL](https://arxiv.org/abs/2605.18703v1)

**作者**：Minrui Xu, Zilin Wang, Mengyi DENG 等 15 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-05-18

### 📄 论文摘要

Equipping LLMs with tool-use capabilities via Agentic Reinforcement Learning (Agentic RL) is bottlenecked by two challenges: the lack of scalable, robust execution environments and the scarcity of realistic training data that captures implicit human reasoning. Existing approaches depend on costly real-world APIs, hallucination-prone LLM simulators, or synthetic environments that are often single-turn or depend on pre-collected documents. Moreover, synthetic trajectories are frequently over-specified, resembling instruction sequences rather than natural human intents, reducing their effectiveness for RL training. We introduce EnvFactory, a fully automated framework that addresses both challenges. EnvFactory autonomously explores and verifies stateful, executable tool environments from authentic resources, and synthesizes natural multi-turn trajectories through topology-aware sampling and calibrated refinement, producing grounded queries with implicit intents. Using only 85 verified environments across 7 domains, EnvFactory generates 2,575 SFT and RL trajectories. Despite using significantly fewer environments than prior work, which are often 5 times more, EnvFactory achieves superior training efficiency and downstream performance, improving Qwen3-series models by up to +15% on BFCLv3, +8.6% on MCP-Atlas, and +6% on conversational benchmarks including $τ^2$-Bench and VitaBench. By fully automating both environment construction and trajectory synthesis, EnvFactory provides a scalable, extensible, and robust foundation for Agentic RL.

### 🤖 AI 总结

**一句话总结**：Equipping LLMs with tool-use capabilities via Agentic Reinforcement Learning (Agentic RL) is bottlenecked by two challenges: the lack of scalable, robust execution environments and the scarcity of rea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, EnvFactory, Scaling, tool-use, via, Executable, Environments, Synthesis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18703v1) | [下载PDF](https://arxiv.org/pdf/2605.18703v1.pdf)

---

## cs.CV

## [12. Can These Views Be One Scene? Evaluating Multiview 3D Consistency when 3D Foundation Models Hallucinate](https://arxiv.org/abs/2605.18754v1)

**作者**：Soumava Paul, Prakhar Kaushik, Alan Yuille  
**分类**：cs.CV  
**发布时间**：2026-05-18

### 📄 论文摘要

Multiview 3D evaluation assumes that the images being scored are observations of one static 3D scene. This assumption can fail in NVS and sparse-view reconstruction: inputs or generated outputs may contain artifacts, outlier frames, repeated views, or noise, yet still receive high 3D consistency scores. Existing reference-based metrics require ground truth, while ground-truth-free metrics such as MEt3R depend on learned reconstruction backbones whose failure modes are poorly characterized. We study this reliability problem by comparing neural reconstruction priors with classical geometric verification. We introduce \benchmark, a controlled robustness benchmark for multiview 3D consistency, and a parametric family that decomposes neural metrics into backbone, residual, and aggregation components. This family recovers MEt3R and yields variants up to $3\times$ more robust. Our analysis shows that VGGT, MASt3R, DUSt3R, and Fast3R can hallucinate dense geometry and cross-view support for unrelated scenes, repeated images, and random noise. We introduce COLMAP-based metrics that use matches, registration, dense support, and reconstruction failure as failure-aware consistency signals. On real NVS outputs and a structured human study, these metrics achieve up to $4\times$ higher correlation with human judgments than MEt3R.

### 🤖 AI 总结

**一句话总结**：Multiview 3D evaluation assumes that the images being scored are observations of one static 3D scene. This assumption can fail in NVS and sparse-view reconstruction: inputs or generated outputs may co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Be, Can, These, Views, One, Scene?, Evaluating, Multiview

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18754v1) | [下载PDF](https://arxiv.org/pdf/2605.18754v1.pdf)

---

## [13. Aurora: Unified Video Editing with a Tool-Using Agent](https://arxiv.org/abs/2605.18748v1)

**作者**：Yongsheng Yu, Ziyun Zeng, Zhiyuan Xiao 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-18

### 📄 论文摘要

Recent video editing models have converged on a unified conditioning design: a single diffusion transformer jointly consumes text, source video, and reference images, and one set of weights covers replacement, removal, style transfer, and reference-driven insertion. The design is flexible, but it assumes that the user already provides model-ready text, reference images, and spatial grounding for local edits, which real requests often omit. We present Aurora, an agentic video editing framework that pairs a tool-augmented vision-language model (VLM) agent with a unified video diffusion transformer. The VLM agent maps a raw user request to a structured edit plan aligned with the transformer's conditioning channels, thereby resolving textual and visual underspecification before generation. We train the VLM agent with supervised data for complete edit planning and reference-image selection, together with preference pairs for robust tool use and instruction refinement. We introduce AgentEdit-Bench to evaluate agent-enhanced video editing under textual and visual underspecification. Experiments on AgentEdit-Bench and two existing video editing benchmarks show that Aurora improves over instruction-only baselines and that the VLM agent transfers to compatible frozen video editing models. Project page: https://yeates.github.io/Aurora-Page

### 🤖 AI 总结

**一句话总结**：Recent video editing models have converged on a unified conditioning design: a single diffusion transformer jointly consumes text, source video, and reference images, and one set of weights covers rep...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Aurora, Unified, Video, Editing, Tool-Using, Recent, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18748v1) | [下载PDF](https://arxiv.org/pdf/2605.18748v1.pdf)

---

## [14. ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop](https://arxiv.org/abs/2605.18746v1)

**作者**：Yining Hong, Jiageng Liu, Han Yin 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.CL, cs.LG, cs.RO  
**发布时间**：2026-05-18

### 📄 论文摘要

Spatial intelligence unfolds through a perception-action loop: agents act to acquire observations, and reason about how observations vary as a function of action. Rather than passively processing what is seen, they actively uncover what is unseen - occluded structure, dynamics, containment, and functionality that cannot be resolved from passive sensing alone. We move beyond prior formulations of spatial intelligence that assume oracle observations by recasting the observer as an actor. We introduce ESI-BENCH, a comprehensive benchmark for embodied spatial intelligence spanning 10 task categories and 29 subcategories built on OmniGibson, grounded in Spelke's core knowledge systems. Agents must decide what abilities to deploy - perception, locomotion, and manipulation - and how to sequence them to actively accumulate task-relevant evidence. We conduct extensive experiments on state-of-the-art MLLMs and find that active exploration substantially outperforms passive counterparts, with agents spontaneously discovering emergent spatial strategies without explicit instructions, while random multi-view often adds noise rather than signal despite consuming far more images. Most failures stem not from weak perception but from action blindness: poor action choices lead to poor observations, which in turn drive cascading errors. While explicit 3D grounding stabilizes reasoning on depth-sensitive tasks, imperfect 3D representation proves more harmful than 2D baselines by distorting spatial relations. Human studies further reveal that unlike humans who seek falsifying viewpoints and revise beliefs under contradiction, models commit prematurely with high confidence regardless of evidence quality, exposing a metacognitive gap that neither better perception nor more embodied interaction alone can close.

### 🤖 AI 总结

**一句话总结**：Spatial intelligence unfolds through a perception-action loop: agents act to acquire observations, and reason about how observations vary as a function of action. Rather than passively processing what...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ESI-Bench, Towards, Embodied, Spatial, Intelligence, Closes, Perception-Action, Loop

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18746v1) | [下载PDF](https://arxiv.org/pdf/2605.18746v1.pdf)

---

## [15. LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://arxiv.org/abs/2605.18739v1)

**作者**：Yukang Chen, Luozhou Wang, Wei Huang 等 16 位作者  
**分类**：cs.CV, cs.DC  
**发布时间**：2026-05-18

### 📄 论文摘要

We present LongLive-2.0, an NVFP4-based parallel infrastructure throughout the full training and inference workflow of long video generation, addressing speed and memory bottlenecks. For training, we introduce sequence-parallel autoregressive (AR) training, instantiated as Balanced SP, which co-designs the efficient teacher-forcing layout with SP execution by pairing clean-history and noisy-target temporal chunks on each rank, enabling a natural teacher-forcing mask with SP-aware chunked VAE encoding. Combined with NVFP4 precision, it reduces GPU memory cost and accelerates GEMM computation during training, the proportion of which increases as video length grows. Moreover, we show that a high-quality infrastructure and dataset enable a remarkably clean training pipeline. Unlike existing Self-Forcing series methods that rely on ODE initialization and subsequent distribution matching distillation (DMD), LongLive-2.0 directly tunes a diffusion model into a long, multi-shot, interactive auto-regressive (AR) diffusion model. It can be further converted to real-time generation (4 to 2 denoising steps) with standalone LoRA weights. For inference on Blackwell GPUs, we enable W4A4 NVFP4 inference, quantize KV cache into NVFP4 for memory savings, and boost end-to-end throughput with asynchronous streaming VAE decoding. On non-Blackwell GPU architectures, we deploy SP inference to match the speed on Blackwell GPUs, while the quantized KV cache can lower inter-GPU communication of SP. Experiments show up to 2.15x speedup in training, and 1.84x in inference. LongLive-2.0-5B achieves 45.7 FPS inference while attaining strong performance on benchmarks. To our knowledge, LongLive-2.0 is the first NVFP4 training and inference system for long video generation.

### 🤖 AI 总结

**一句话总结**：We present LongLive-2.0, an NVFP4-based parallel infrastructure throughout the full training and inference workflow of long video generation, addressing speed and memory bottlenecks. For training, we ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, LongLive-2.0, NVFP4, Parallel, Infrastructure, Long, Video, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18739v1) | [下载PDF](https://arxiv.org/pdf/2605.18739v1.pdf)

---

## [16. Spectral Progressive Diffusion for Efficient Image and Video Generation](https://arxiv.org/abs/2605.18736v1)

**作者**：Howard Xiao, Brian Chao, Lior Yariv 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-18

### 📄 论文摘要

Diffusion models have been shown to implicitly generate visual content autoregressively in the frequency domain, where low-frequency components are generated earlier in the denoising process while high-frequency details emerge only in later timesteps. This structure offers a natural opportunity for efficient generation, as high-resolution computation on noise-dominated frequencies is largely redundant. We propose Spectral Progressive Diffusion, a general framework that progressively grows resolution along the denoising trajectory of pretrained diffusion models. To this end, we develop a spectral noise expansion mechanism and derive an optimal resolution schedule from the model's power spectrum. Our framework supports training-free acceleration and a novel fine-tuning recipe that further improves efficiency and quality. We demonstrate significant speedups on state-of-the-art pretrained image and video generation models while preserving visual quality.

### 🤖 AI 总结

**一句话总结**：Diffusion models have been shown to implicitly generate visual content autoregressively in the frequency domain, where low-frequency components are generated earlier in the denoising process while hig...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Spectral, Progressive, Efficient, Image, Video, Generation, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18736v1) | [下载PDF](https://arxiv.org/pdf/2605.18736v1.pdf)

---

## [17. PIXLRelight: Controllable Relighting via Intrinsic Conditioning](https://arxiv.org/abs/2605.18735v1)

**作者**：Miguel Farinha, Ronald Clark  
**分类**：cs.CV, cs.GR, cs.LG  
**发布时间**：2026-05-18

### 📄 论文摘要

We present PIXLRelight, a feed-forward approach for physically controllable single-image relighting. Existing methods either provide limited lighting control (e.g. through text or environment maps), accumulate errors when chaining inverse and forward rendering, or require costly per-image optimization. Our key idea is to bridge physically based rendering (PBR) and learned image synthesis through a shared intrinsic conditioning that can be obtained from either real photographs or PBR renders. At training time, paired multi-illumination photographs are decomposed into albedo, diffuse shading, and non-diffuse residuals, which condition the model. At inference time, the same conditioning is computed from a path-traced render of a coarse 3D reconstruction of the input under user-specified PBR lights. A transformer-based neural renderer then applies the target illumination to the source photograph, preserving fine image detail through a per-pixel affine modulation. PIXLRelight enables arbitrary PBR-style lighting control, achieves state-of-the-art relighting quality, and runs in under a tenth of a second per image. Code and models are available at https://mlfarinha.github.io/pixl-relight/.

### 🤖 AI 总结

**一句话总结**：We present PIXLRelight, a feed-forward approach for physically controllable single-image relighting. Existing methods either provide limited lighting control (e.g. through text or environment maps), a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, PIXLRelight, Controllable, Relighting, via, Intrinsic, Conditioning, present

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18735v1) | [下载PDF](https://arxiv.org/pdf/2605.18735v1.pdf)

---

## [18. EgoExoMem: Cross-View Memory Reasoning over Synchronized Egocentric and Exocentric Videos](https://arxiv.org/abs/2605.18734v1)

**作者**：Ruiping Liu, Junwei Zheng, Yufan Chen 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-18

### 📄 论文摘要

Egocentric memory is widely used in embodied intelligence, but it may be insufficient for comprehensive spatial-temporal reasoning. Inspired by human recall from both field and observer perspectives, we introduce EgoExoMem, the first benchmark for cross-view memory reasoning over synchronized egocentric and exocentric videos. EgoExoMem contains $2.6K$ high-quality MCQs across eight temporal, spatial, and cross-view QA types. To support dual-view retrieval, we propose E$^2$-Select, a training-free frame selection method for synchronized ego-exo videos. It combines relevance-based budget allocation with per-view k-DPP sampling to handle view asymmetry and cross-view temporal consistency. Experiments show that ego and exo views provide complementary memory cues, while existing MLLMs remain far from solving the benchmark: the best model reaches only $55.3\%$. E$^2$-Select achieves state-of-the-art performance of $58.2\%$ over frame-selection and RAG-based memory baselines. Further analysis reveals systematic view-preference conflicts between question framing and answer grounding, underscoring the novelty and challenge of cross-view memory reasoning.

### 🤖 AI 总结

**一句话总结**：Egocentric memory is widely used in embodied intelligence, but it may be insufficient for comprehensive spatial-temporal reasoning. Inspired by human recall from both field and observer perspectives, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EgoExoMem, Cross-View, Memory, Reasoning, over, Synchronized, Egocentric, Exocentric

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18734v1) | [下载PDF](https://arxiv.org/pdf/2605.18734v1.pdf)

---

## [19. Advancing Narrative Long Video Generation via Training-Free Identity-Aware Memory](https://arxiv.org/abs/2605.18733v1)

**作者**：Jinzhuo Liu, Jiangning Zhang, Wencan Jiang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-18

### 📄 论文摘要

Autoregressive video generation has improved rapidly in visual fidelity and interactivity, but it still suffers from long-term inconsistency and memory degradation. Most existing solutions either compress historical frames using predefined strategies or retrieve keyframes based on coarse implicit attention signals, both of which fail to handle evolving prompts with shifting entity references, leading to identity drift, character duplication, and attribute loss. To address this, we propose IAMFlow, a training-free identity-aware memory framework that explicitly models and tracks persistent entity identities, enabling consistent generation across prompt transitions. Specifically, an LLM extracts entities with visual attributes from each prompt and assigns unique global IDs for identity-aware memory, while a VLM asynchronously verifies and refines attributes from rendered frames, enabling explicit entity tracking in place of implicit similarity-based matching. To keep the proposed framework computationally practical, we design a systematic inference acceleration pipeline, including asynchronous visual verification, adaptive prompt transition, and model quantization, which achieves faster generation than existing baselines. Furthermore, we introduce NarraStream-Bench, a benchmark for narrative streaming video generation that features 324 multi-prompt scripts spanning six dimensions and a three-dimensional evaluation protocol that integrates both traditional metrics and multimodal large language model-based assessments. Extensive experiments show that IAMFlow, despite being training-free, achieves the best overall performance on NarraStream-Bench, outperforming the strongest baseline by 2.56 points, while achieving a 1.39$\times$ speedup over the most efficient baseline in the 60-second multi-prompt setting.

### 🤖 AI 总结

**一句话总结**：Autoregressive video generation has improved rapidly in visual fidelity and interactivity, but it still suffers from long-term inconsistency and memory degradation. Most existing solutions either comp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Advancing, Narrative, Long, Video, Generation, via, Training-Free, Identity-Aware

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18733v1) | [下载PDF](https://arxiv.org/pdf/2605.18733v1.pdf)

---

## [20. SafeDiffusion-R1: Online Reward Steering for Safe Diffusion Post-Training](https://arxiv.org/abs/2605.18719v1)

**作者**：Komal Kumar, Ankan Deria, Abhishek Basu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-18

### 📄 论文摘要

Diffusion models have been widely studied for removing unsafe content learned during pre-training. Existing methods require expensive supervised data, either unsafe-text paired with safe-image groundtruth or negative/positive image pairs, making them impractical to scale. Furthermore, offline reinforcement learning and supervised fine-tuning approaches that generate synthetic data offline suffer from catastrophic forgetting, degrading generation quality. We propose a novel online reinforcement learning framework that addresses both data scarcity and model degradation through post-training with Group Relative Policy Optimization (GRPO) on both negative and positive text prompts. To eliminate the need for fine-tuning specialized safe/unsafe reward models, we introduce a \textit{steering reward mechanism} that exploits an inherent property of CLIP embeddings: steering text representations toward positive safety directions and away from negative ones in the embedding space. Our online-policy approach enables the model to learn from diverse prompts, including explicit unsafe content, without catastrophic forgetting. Extensive experiments demonstrate that our method reduces inappropriate content to 18.07\% (vs. 48.9\% for SD v1.4) and nudity detections to 15 (vs. 646 baseline) while improving compositional generation quality from 42.08\% to 47.83\% on GenEval. Remarkably, these safety gains generalize to out-of-domain unsafe prompts across seven harm categories, achieving state-of-the-art performance without supervised paired data or reward tuning. Github: https://github.com/MAXNORM8650/SafeDiffusion-R1.

### 🤖 AI 总结

**一句话总结**：Diffusion models have been widely studied for removing unsafe content learned during pre-training. Existing methods require expensive supervised data, either unsafe-text paired with safe-image groundt...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, SafeDiffusion-R1, Online, Reward, Steering, Safe, Post-Training, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18719v1) | [下载PDF](https://arxiv.org/pdf/2605.18719v1.pdf)

---

## [21. Semantic Generative Tuning for Unified Multimodal Models](https://arxiv.org/abs/2605.18714v1)

**作者**：Songsong Yu, Yuxin Chen, Ying Shan 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-18

### 📄 论文摘要

Unified multimodal models (UMMs) strive to consolidate visual understanding and visual generation within a single architecture. However, prevailing training paradigms independently optimize understanding via sparse text signals and generation through dense pixel objectives. Such a decoupled strategy yields misaligned representation spaces, isolating visual understanding from generation and hindering their mutual reinforcement. This work presents the first systematic investigation into generative post-training, where we formulate hierarchical visual tasks as generative proxies to bridge the isolation in UMMs. Our empirical investigation reveals that high-level semantic tasks, particularly image segmentation, serve as optimal proxies. Unlike low-level tasks that distract models with texture details, segmentation provides structural semantics that significantly enhance both vision-centric perception and generative layout fidelity. Building upon these insights, we introduce Semantic Generative Tuning (SGT), a novel paradigm that leverages segmentation as a generative proxy to align and synergize multimodal capabilities. Mechanistic analyses further demonstrate that SGT fundamentally improves feature linear separability and optimizes visual-textual attention allocation pattern. Extensive evaluations show that SGT consistently improves both multimodal comprehension and generative fidelity across mainstream benchmarks. Our code is available on the https://song2yu.github.io/SGT/.

### 🤖 AI 总结

**一句话总结**：Unified multimodal models (UMMs) strive to consolidate visual understanding and visual generation within a single architecture. However, prevailing training paradigms independently optimize understand...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Semantic, Generative, Tuning, Unified, Multimodal, Models, UMMs, strive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18714v1) | [下载PDF](https://arxiv.org/pdf/2605.18714v1.pdf)

---

## [22. A Large-Scale Study on the Accuracy vs Cost Trade-offs of Training and Evaluation Settings in Fine-Grained Image Recognition](https://arxiv.org/abs/2605.18700v1)

**作者**：Edwin Arkel Rios, Augusto Christian Surya, Oswin Gosal 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-18

### 📄 论文摘要

Prior work on fine-grained image recognition (FGIR) has established the importance of the backbone selection, but has neglected the accuracy-vs-cost trade-offs under different training and evaluation settings. In this work we conduct a large-scale study with over 2000 experiments across 6 training and evaluation settings, 9 pretrained backbones, and 17 datasets. Preliminary observations on the effectiveness of data augmentation for fine-grained training motivate us to extend Counterfactual Attention Learning (CAL), a state-of-the-art method based on data-aware cropping and masking augmentations, with cross-image discriminative region mixing augmentation. We also propose an efficient evaluation-only variant that maintains competitive accuracy while reducing inference costs by forfeiting the forward pass on discriminative crops that is normally used by CAL and similar FGIR methods. Our results show that data-aware augmentations during training only can enable a model to achieve excellent accuracy even without crops, significantly reducing inference costs. To support future research we share our code and checkpoints at: \url{https://github.com/arkel23/FGIR-Backbones}

### 🤖 AI 总结

**一句话总结**：Prior work on fine-grained image recognition (FGIR) has established the importance of the backbone selection, but has neglected the accuracy-vs-cost trade-offs under different training and evaluation ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：vs, of, Large-Scale, Study, Accuracy, Cost, Trade-offs, Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18700v1) | [下载PDF](https://arxiv.org/pdf/2605.18700v1.pdf)

---

## [23. CMAG: Concept-Scaffolded Retrieval for Marketplace Avatar Generation](https://arxiv.org/abs/2605.18680v1)

**作者**：Rajeev Goel, Jason Ding, Phani Harish Wajjala 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-18

### 📄 论文摘要

Metaverse platforms rely on creator-driven marketplaces where avatars are assembled from discrete, taxonomy-labeled 3D assets (e.g., tops, bottoms, shoes, accessories) under strict category and topology constraints. While users increasingly expect free-form text control, text-only retrieval is brittle: natural language is ambiguous with respect to platform taxonomies, metadata is often noisy or informal, and independently retrieved components can be stylistically inconsistent or geometrically incompatible. We propose \textbf{CMAG}, a concept-scaffolded retrieval and verified composition framework for marketplace avatar generation. Given a prompt, CMAG first synthesizes an intermediate 3D concept scaffold that disambiguates intent beyond text by providing global spatial and stylistic context. In parallel, a view-aware part discovery module extracts localized visual evidence via prompt decomposition and text-grounded segmentation. A prompt-conditioned taxonomy router enforces category coverage and resolves semantic-to-taxonomic mismatch, after which a hybrid category-wise retriever combines part-based fusion with a concept-residual fallback using feature suppression. Finally, an agentic vision--language model filters and re-ranks candidates across categories and drives an iterative verification loop to assemble prompt-faithful, topologically consistent avatars from catalog assets. We evaluate CMAG on diverse compositional prompts and demonstrate improved retrieval robustness and compositional correctness compared to strong baselines, highlighting the importance of 3D concept scaffolding under prompt ambiguity.

### 🤖 AI 总结

**一句话总结**：Metaverse platforms rely on creator-driven marketplaces where avatars are assembled from discrete, taxonomy-labeled 3D assets (e.g., tops, bottoms, shoes, accessories) under strict category and topolo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CMAG, Concept-Scaffolded, Retrieval, Marketplace, Avatar, Generation, Metaverse, platforms

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18680v1) | [下载PDF](https://arxiv.org/pdf/2605.18680v1.pdf)

---

## [24. Better Together: Evaluating the Complementarity of Earth Embedding Models](https://arxiv.org/abs/2605.18667v1)

**作者**：Thijs L van der Plas, Jacob JW Bakermans, Vishal Nedungadi 等 6 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-05-18

### 📄 论文摘要

Earth embedding models transform Earth observation data into embeddings uniquely tied to locations on the Earth's surface. These models are typically evaluated in isolation, comparing the downstream task performance across different Earth embeddings. However, spatially aligned embeddings can naturally be fused, providing richer information per location, a capability that isolated evaluations fail to capture. We therefore propose assessing Earth embeddings by their complementarity: the performance gain of fused embeddings over the best single-model baseline. To operationalise this, we introduce an embedding complementarity index applicable to any embedding and task, and evaluate four Earth embedding models (AlphaEarth, Tessera, GeoCLIP, SatCLIP) in isolation, in all pairs, and jointly across six downstream tasks. Fused embeddings outperform the best single model in four out of six tasks, confirming that single-embedding evaluations often underestimate Earth embedding capabilities. Complementarity proves both task- and location-dependent. Further, for a land cover regression task, we find that complementarity is partially determined by the spatial scale of land cover classes. Complementarity reframes Earth embeddings: the greatest future gains may come not from any single Earth embedding model, but from combinations that are better together.

### 🤖 AI 总结

**一句话总结**：Earth embedding models transform Earth observation data into embeddings uniquely tied to locations on the Earth's surface. These models are typically evaluated in isolation, comparing the downstream t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Better, Together, Evaluating, Complementarity, Earth, Embedding, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18667v1) | [下载PDF](https://arxiv.org/pdf/2605.18667v1.pdf)

---

## cs.LG

## [25. General Preference Reinforcement Learning](https://arxiv.org/abs/2605.18721v1)

**作者**：Muhammad Umer, Muhammad Ahmed Mohsin, Ahsan Bilal 等 8 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-05-18

### 📄 论文摘要

Post-training has split large language model (LLM) alignment into two largely disconnected tracks. Online reinforcement learning (RL) with verifiable rewards drives emergent reasoning on math and code but depends on a programmatic verifier that cannot reach open-ended tasks, while preference optimization handles open-ended generation yet forgoes the continuous exploration that powers online RL. Closing this gap requires a verifier for open-ended quality, but a scalar reward model is the wrong shape for the job. Quality is multi-dimensional, and any scalar score is an incomplete proxy that lets online RL collapse onto whichever axis the score is most sensitive to. We turn instead to the General Preference Model (GPM), which embeds responses into $k$ skew-symmetric subspaces and represents preference as a structured, intransitivity-aware comparison. Building on this, we propose General Preference Reinforcement Learning (GPRL), which carries the $k$-way structure through to the policy update. GPRL computes per-dimension group-relative advantages, normalizes each on its own scale so no axis can dominate, and aggregates them with context-dependent eigenvalues. The same structure powers a closed-loop drift monitor that detects single-axis exploitation and corrects it on the fly by reweighting dimensions and tightening the trust region. Starting from $\texttt{Llama-3-8B-Instruct}$, GPRL reaches a length-controlled win rate of $56.51\%$ on AlpacaEval~2.0 while also outperforming SimPO and SPPO on Arena-Hard, MT-Bench, and WildBench by resisting reward hacking across extended training runs.

### 🤖 AI 总结

**一句话总结**：Post-training has split large language model (LLM) alignment into two largely disconnected tracks. Online reinforcement learning (RL) with verifiable rewards drives emergent reasoning on math and code...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：General, Preference, Reinforcement, Learning, Post-training, has, split, large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18721v1) | [下载PDF](https://arxiv.org/pdf/2605.18721v1.pdf)

---

## [26. Distilling Tabular Foundation Models for Structured Health Data](https://arxiv.org/abs/2605.18702v1)

**作者**：Aditya Tanna, Nassim Bouarour, Mohamed Bouadi 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-18

### 📄 论文摘要

Tabular foundation models (TFMs) achieve strong performance on health datasets, but their inference cost and infrastructure requirements limit practical use. We study whether their predictive behavior can be transferred to lightweight tabular models through knowledge distillation. Since in-context TFMs condition on the training set at inference time, naive distillation can introduce context leakage; we address this with stratified out-of-fold teacher labeling. Across $19$ healthcare datasets, $6$ TFM teachers, $4$ student families, and several multi-teacher ensembles, we find that distilled students retain at least $90\%$ of teacher AUC, outperforming teachers in some cases, while running at least $26\times$ faster on CPU and preserving calibration and fairness critical for health applications. Moreover, multi-teacher averaging does not consistently improve over the best single teacher. Leakage-aware distillation is thus a viable route for bringing TFM-quality predictions into inference-constrained health settings.

### 🤖 AI 总结

**一句话总结**：Tabular foundation models (TFMs) achieve strong performance on health datasets, but their inference cost and infrastructure requirements limit practical use. We study whether their predictive behavior...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Distilling, Tabular, Foundation, Models, Structured, Health, Data, TFMs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18702v1) | [下载PDF](https://arxiv.org/pdf/2605.18702v1.pdf)

---

## [27. Learning Normal Representations for Blood Biomarkers](https://arxiv.org/abs/2605.18701v1)

**作者**：Aashna P. Shah, Michelle M. Li, Yash Lal 等 12 位作者  
**分类**：cs.LG, q-bio.QM  
**发布时间**：2026-05-18

### 📄 论文摘要

Blood-based biomarkers underpin clinical diagnosis and management, yet their interpretation relies largely on fixed population reference intervals that ignore stable, intra-patient variability. As such, population-based interpretation can mask meaningful deviation from an individual's baseline, risking delayed disease detection. To remedy this, there have been increasing efforts to personalize blood biomarker interpretation using individual testing histories. However, these methods may overfit to sparse data, inflating false-positive rates and unnecessary follow-up, and can also unwittingly include unrecognized or subclinical disease. Here, we leverage nearly 2 billion longitudinal laboratory measurements from over 1.6 million individuals across North America, the Middle East, and East Asia, to show that while laboratory values are highly individual, purely personalized intervals routinely overfit, classifying up to 68% of measurements as abnormal, without corresponding associations with adverse clinical outcomes. We then introduce NORMA, a conditional transformer-based framework that generates reference intervals by conditioning on both a patient's history and population-level data about "normal" variation. NORMA-derived intervals achieve higher precision for predicting outcomes, including mortality, acute kidney injury, and chronic disease. These findings caution against over-personalization in laboratory medicine and demonstrate that anchoring individual trajectories to population-level priors outperforms either approach alone. To promote transparency, we publicly release the model, code, and an interactive user interface for accessible, individualized laboratory interpretation.

### 🤖 AI 总结

**一句话总结**：Blood-based biomarkers underpin clinical diagnosis and management, yet their interpretation relies largely on fixed population reference intervals that ignore stable, intra-patient variability. As suc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Normal, Representations, Blood, Biomarkers, Blood-based, underpin, clinical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18701v1) | [下载PDF](https://arxiv.org/pdf/2605.18701v1.pdf)

---

## [28. Ensembling Tabular Foundation Models - A Diversity Ceiling And A Calibration Trap](https://arxiv.org/abs/2605.18696v1)

**作者**：Aditya Tanna, Yash Desai, Pratinav Seth 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-18

### 📄 论文摘要

Tabular foundation models (TFMs) now match or beat tuned gradient-boosted trees on a growing fraction of tabular tasks, but no single TFM wins on every dataset. Ensembling is the go to fix here, and it works less well than expected. Six modern TFMs form a near-redundant pool: their mean pairwise Q-statistic is $0.961$, close enough to $1$ that any convex combination is bounded above. We benchmark six ensemble strategies over six TFMs on 153 OpenML classification tasks. The best ensemble, two-level cascade stacking, buys $+0.18\%$ accuracy over the strongest single TFM at $253\times$ the compute. A Friedman and Nemenyi analysis places three ensembles and the best base TFM in a single equivalence group; three other ensembles are significantly \emph{worse} than the best base. Stacking with a logistic-regression meta-learner is the most striking case: competitive accuracy and ROC-AUC, the worst log-loss rank among the ensembles. The meta-learner improves accuracy by sharpening class boundaries, which destroys calibration. We recommend greedy selection as the practical default.

### 🤖 AI 总结

**一句话总结**：Tabular foundation models (TFMs) now match or beat tuned gradient-boosted trees on a growing fraction of tabular tasks, but no single TFM wins on every dataset. Ensembling is the go to fix here, and i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Ensembling, Tabular, Foundation, Models, Diversity, Ceiling, Calibration, Trap

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18696v1) | [下载PDF](https://arxiv.org/pdf/2605.18696v1.pdf)

---

## [29. COOPO: Cyclic Offline-Online Policy Optimization Algorithm](https://arxiv.org/abs/2605.18675v1)

**作者**：Qisai Liu, Zhanhong Jiang, Joshua Russell Waite 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-18

### 📄 论文摘要

Offline reinforcement learning struggles with distributional shift and constrained performance due to static dataset limitations, while online RL demands prohibitive environment interactions. The recent advent of hybrid offline-to-online methods bridges these domains but suffers from distribution drift during transitions and catastrophic forgetting of offline knowledge. We introduce COOPO (Cyclic Offline-Online Policy Optimization), a generalized framework that repeatedly cycles between constrained offline training and online fine-tuning. Each cycle first anchors the policy to the dataset via KL-regularized advantage-weighted offline updates to minimize distributional shift and then fine-tunes it online using any policy optimization for stable exploration. Crucially, periodically returning to offline training eliminates forgetting and drift while maximizing dataset reuse. The cyclic behavior also helps reduce the online environment interactions. Theoretically, COOPO achieves better online sample efficiency, surpassing pure online RL, with guaranteed monotonic improvement under standard coverage assumptions. Extensive D4RL benchmarks demonstrate COOPO reduces online interactions versus state-of-the-art hybrids while improving final returns, maintaining robustness across diverse offline algorithms and online optimizers. This looped synergy sets new efficiency and performance standards for adaptive RL.

### 🤖 AI 总结

**一句话总结**：Offline reinforcement learning struggles with distributional shift and constrained performance due to static dataset limitations, while online RL demands prohibitive environment interactions. The rece...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：COOPO, Cyclic, Offline-Online, Policy, Optimization, Algorithm, Offline, reinforcement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18675v1) | [下载PDF](https://arxiv.org/pdf/2605.18675v1.pdf)

---

## [30. A No-Defense Defense Against Gradient-Based Adversarial Attacks on ML-NIDS: Is Less More?](https://arxiv.org/abs/2605.18666v1)

**作者**：Mohamed elShehaby, Ashraf Matrawy  
**分类**：cs.LG, cs.CR  
**发布时间**：2026-05-18

### 📄 论文摘要

Gradient-based adversarial attacks subtly manipulate inputs of Machine Learning (ML) models to induce incorrect predictions. This paper investigates whether careful architectural choices alone can yield an inherently robust Deep Neural Network (DNN)-based Network Intrusion Detection Systems (NIDS), without any additional explicit defenses. Through thousands of experiments, around 2200, varying network depth, feature dimensionality, activation functions, and dropout across FGSM, PGD, and BIM attacks, we show that shallower networks, reduced feature sets, and ReLU activation consistently and jointly reduce adversarial vulnerability. Moreover, a simple model following this recipe outperforms deeper, fully-featured adversarially trained models, while maintaining near-perfect clean-traffic detection and lower training times. Nevertheless, while less is more, the selection of the right less is what truly matters.

### 🤖 AI 总结

**一句话总结**：Gradient-based adversarial attacks subtly manipulate inputs of Machine Learning (ML) models to induce incorrect predictions. This paper investigates whether careful architectural choices alone can yie...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：No-Defense, Defense, Against, Gradient-Based, Adversarial, Attacks, ML-NIDS, Less

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.18666v1) | [下载PDF](https://arxiv.org/pdf/2605.18666v1.pdf)

---

