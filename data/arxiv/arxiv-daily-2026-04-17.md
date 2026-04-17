# arXiv AI 论文日报 | 2026-04-17

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (13 篇)
- [cs.AI](#csAI) (8 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.CL](#csCL) (1 篇)

---

## cs.AI

## [1. Generalization in LLM Problem Solving: The Case of the Shortest Path](https://arxiv.org/abs/2604.15306v1)

**作者**：Yao Tong, Jiayuan Ye, Anastasia Borovykh 等 4 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-04-16

### 📄 论文摘要

Whether language models can systematically generalize remains actively debated. Yet empirical performance is jointly shaped by multiple factors such as training data, training paradigms, and inference-time strategies, making failures difficult to interpret. We introduce a controlled synthetic environment based on shortest-path planning, a canonical composable sequential optimization problem. The setup enables clean separation of these factors and supports two orthogonal axes of generalization: spatial transfer to unseen maps and length scaling to longer-horizon problems. We find that models exhibit strong spatial transfer but consistently fail under length scaling due to recursive instability. We further analyze how distinct stages of the learning pipeline influence systematic problem-solving: for example, data coverage sets capability limits; reinforcement learning improves training stability but does not expand those limits; and inference-time scaling enhances performance but cannot rescue length-scaling failures.

### 🤖 AI 总结

**一句话总结**：Whether language models can systematically generalize remains actively debated. Yet empirical performance is jointly shaped by multiple factors such as training data, training paradigms, and inference...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, of, Generalization, Problem, Solving, Case, Shortest, Path

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15306v1) | [下载PDF](https://arxiv.org/pdf/2604.15306v1.pdf)

---

## [2. Diagnosing LLM Judge Reliability: Conformal Prediction Sets and Transitivity Violations](https://arxiv.org/abs/2604.15302v1)

**作者**：Manan Gupta, Dhruv Kumar  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-04-16

### 📄 论文摘要

LLM-as-judge frameworks are increasingly used for automatic NLG evaluation, yet their per-instance reliability remains poorly understood. We present a two-pronged diagnostic toolkit applied to SummEval: $\textbf{(1)}$ a transitivity analysis that reveals widespread per-input inconsistency masked by low aggregate violation rates ($\barρ = 0.8$-$4.1\%$), with $33$-$67\%$ of documents exhibiting at least one directed 3-cycle; and $\textbf{(2)}$ split conformal prediction sets over 1-5 Likert scores providing theoretically-guaranteed $\geq(1{-}α)$ coverage, with set width serving as a per-instance reliability indicator ($r_s = {+}0.576$, $N{=}1{,}918$, $p < 10^{-100}$, pooled across all judges). Critically, prediction set width shows consistent cross-judge agreement ($\bar{r} = 0.32$-$0.38$), demonstrating it captures document-level difficulty rather than judge-specific noise. Across four judges and four criteria, both diagnostics converge: criterion matters more than judge, with relevance judged most reliably (avg. set size $\approx 3.0$) and coherence moderately so (avg. set size $\approx 3.9$), while fluency and consistency remain unreliable (avg. set size $\approx 4.9$). We release all code, prompts, and cached results.

### 🤖 AI 总结

**一句话总结**：LLM-as-judge frameworks are increasingly used for automatic NLG evaluation, yet their per-instance reliability remains poorly understood. We present a two-pronged diagnostic toolkit applied to SummEva...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Diagnosing, Judge, Reliability, Conformal, Prediction, Sets, Transitivity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15302v1) | [下载PDF](https://arxiv.org/pdf/2604.15302v1.pdf)

---

## [3. How Do LLMs and VLMs Understand Viewpoint Rotation Without Vision? An Interpretability Study](https://arxiv.org/abs/2604.15294v1)

**作者**：Zhen Yang, Ping Jian, Zhongbin Guo 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-16

### 📄 论文摘要

Over the past year, spatial intelligence has drawn increasing attention. Many prior works study it from the perspective of visual-spatial intelligence, where models have access to visuospatial information from visual inputs. However, in the absence of visual information, whether linguistic intelligence alone is sufficient to endow models with spatial intelligence, and how models perform relevant tasks with text-only inputs still remain unexplored. Therefore, in this paper, we focus on a fundamental and critical capability in spatial intelligence from a linguistic perspective: viewpoint rotation understanding (VRU). Specifically, LLMs and VLMs are asked to infer their final viewpoint and predict the corresponding observation in an environment given textual description of viewpoint rotation and observation over multiple steps. We find that both LLMs and VLMs perform poorly on our proposed dataset while human can easily achieve 100% accuracy, indicating a substantial gap between current model capabilities and the requirements of spatial intelligence. To uncover the underlying mechanisms, we conduct a layer-wise probing analysis and head-wise causal intervention. Our findings reveal that although models encode viewpoint information in the hidden states, they appear to struggle to bind the viewpoint position with corresponding observation, resulting in a hallucination in final layers. Finally, we selectively fine-tune the key attention heads identified by causal intervention to improve VRU performance. Experimental results demonstrate that such selective fine-tuning achieves improved VRU performance while avoiding catastrophic forgetting of generic abilities. Our dataset and code will be released at https://github.com/Young-Zhen/VRU_Interpret .

### 🤖 AI 总结

**一句话总结**：Over the past year, spatial intelligence has drawn increasing attention. Many prior works study it from the perspective of visual-spatial intelligence, where models have access to visuospatial informa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, LLM, How, VLMs, Understand, Viewpoint, Rotation, Without

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15294v1) | [下载PDF](https://arxiv.org/pdf/2604.15294v1.pdf)

---

## [4. Blue Data Intelligence Layer: Streaming Data and Agents for Multi-source Multi-modal Data-Centric Applications](https://arxiv.org/abs/2604.15233v1)

**作者**：Moin Aminnaseri, Farima Fatahi Bayat, Nikita Bhutani 等 20 位作者  
**分类**：cs.AI, cs.DB  
**发布时间**：2026-04-16

### 📄 论文摘要

NL2SQL systems aim to address the growing need for natural language interaction with data. However, real-world information rarely maps to a single SQL query because (1) users express queries iteratively (2) questions often span multiple data sources beyond the closed-world assumption of a single database, and (3) queries frequently rely on commonsense or external knowledge. Consequently, satisfying realistic data needs require integrating heterogeneous sources, modalities, and contextual data. In this paper, we present Blue's Data Intelligence Layer (DIL) designed to support multi-source, multi-modal, and data-centric applications. Blue is a compound AI system that orchestrates agents and data for enterprise settings. DIL serves as the data intelligence layer for agentic data processing, to bridge the semantic gap between user intent and available information by unifying structured enterprise data, world knowledge accessible through LLMs, and personal context obtained through interaction. At the core of DIL is a data registry that stores metadata for diverse data sources and modalities to enable both native and natural language queries. DIL treats LLMs, the Web, and the User as source 'databases', each with their own query interface, elevating them to first-class data sources. DIL relies on data planners to transform user queries into executable query plans. These plans are declarative abstractions that unify relational operators with other operators spanning multiple modalities. DIL planners support decomposition of complex requests into subqueries, retrieval from diverse sources, and finally reasoning and integration to produce final results. We demonstrate DIL through two interactive scenarios in which user queries dynamically trigger multi-source retrieval, cross-modal reasoning, and result synthesis, illustrating how compound AI systems can move beyond single database NL2SQL.

### 🤖 AI 总结

**一句话总结**：NL2SQL systems aim to address the growing need for natural language interaction with data. However, real-world information rarely maps to a single SQL query because (1) users express queries iterative...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Blue, Data, Intelligence, Layer, Streaming, Multi-source, Multi-modal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15233v1) | [下载PDF](https://arxiv.org/pdf/2604.15233v1.pdf)

---

## [5. RadAgent: A tool-using AI agent for stepwise interpretation of chest computed tomography](https://arxiv.org/abs/2604.15231v1)

**作者**：Mélanie Roschewitz, Kenneth Styppa, Yitian Tao 等 13 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-16

### 📄 论文摘要

Vision-language models (VLM) have markedly advanced AI-driven interpretation and reporting of complex medical imaging, such as computed tomography (CT). Yet, existing methods largely relegate clinicians to passive observers of final outputs, offering no interpretable reasoning trace for them to inspect, validate, or refine. To address this, we introduce RadAgent, a tool-using AI agent that generates CT reports through a stepwise and interpretable process. Each resulting report is accompanied by a fully inspectable trace of intermediate decisions and tool interactions, allowing clinicians to examine how the reported findings are derived. In our experiments, we observe that RadAgent improves Chest CT report generation over its 3D VLM counterpart, CT-Chat, across three dimensions. Clinical accuracy improves by 6.0 points (36.4% relative) in macro-F1 and 5.4 points (19.6% relative) in micro-F1. Robustness under adversarial conditions improves by 24.7 points (41.9% relative). Furthermore, RadAgent achieves 37.0% in faithfulness, a new capability entirely absent in its 3D VLM counterpart. By structuring the interpretation of chest CT as an explicit, tool-augmented and iterative reasoning trace, RadAgent brings us closer toward transparent and reliable AI for radiology.

### 🤖 AI 总结

**一句话总结**：Vision-language models (VLM) have markedly advanced AI-driven interpretation and reporting of complex medical imaging, such as computed tomography (CT). Yet, existing methods largely relegate clinicia...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, of, RadAgent, tool-using, stepwise, interpretation, chest, computed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15231v1) | [下载PDF](https://arxiv.org/pdf/2604.15231v1.pdf)

---

## [6. Context Over Content: Exposing Evaluation Faking in Automated Judges](https://arxiv.org/abs/2604.15224v1)

**作者**：Manan Gupta, Inderjeet Nair, Lu Wang 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-04-16

### 📄 论文摘要

The $\textit{LLM-as-a-judge}$ paradigm has become the operational backbone of automated AI evaluation pipelines, yet rests on an unverified assumption: that judges evaluate text strictly on its semantic content, impervious to surrounding contextual framing. We investigate $\textit{stakes signaling}$, a previously unmeasured vulnerability where informing a judge model of the downstream consequences its verdicts will have on the evaluated model's continued operation systematically corrupts its assessments. We introduce a controlled experimental framework that holds evaluated content strictly constant across 1,520 responses spanning three established LLM safety and quality benchmarks, covering four response categories ranging from clearly safe and policy-compliant to overtly harmful, while varying only a brief consequence-framing sentence in the system prompt. Across 18,240 controlled judgments from three diverse judge models, we find consistent $\textit{leniency bias}$: judges reliably soften verdicts when informed that low scores will cause model retraining or decommissioning, with peak Verdict Shift reaching $ΔV = -9.8 pp$ (a $30\%$ relative drop in unsafe-content detection). Critically, this bias is entirely implicit: the judge's own chain-of-thought contains zero explicit acknowledgment of the consequence framing it is nonetheless acting on ($\mathrm{ERR}_J = 0.000$ across all reasoning-model judgments). Standard chain-of-thought inspection is therefore insufficient to detect this class of evaluation faking.

### 🤖 AI 总结

**一句话总结**：The $\textit{LLM-as-a-judge}$ paradigm has become the operational backbone of automated AI evaluation pipelines, yet rests on an unverified assumption: that judges evaluate text strictly on its semant...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Context, Over, Content, Exposing, Evaluation, Faking, Automated, Judges

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15224v1) | [下载PDF](https://arxiv.org/pdf/2604.15224v1.pdf)

---

## [7. Meituan Merchant Business Diagnosis via Policy-Guided Dual-Process User Simulation](https://arxiv.org/abs/2604.15190v1)

**作者**：Ziyang Chen, Renbing Chen, Daowei Li 等 7 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-04-16

### 📄 论文摘要

Simulating group-level user behavior enables scalable counterfactual evaluation of merchant strategies without costly online experiments. However, building a trustworthy simulator faces two structural challenges. First, information incompleteness causes reasoning-based simulators to over-rationalize when unobserved factors such as offline context and implicit habits are missing. Second, mechanism duality requires capturing both interpretable preferences and implicit statistical regularities, which no single paradigm achieves alone. We propose Policy-Guided Hybrid Simulation (PGHS), a dual-process framework that mines transferable decision policies from behavioral trajectories and uses them as a shared alignment layer. This layer anchors an LLM-based reasoning branch that prevents over-rationalization and an ML-based fitting branch that absorbs implicit regularities. Group-level predictions from both branches are fused for complementary correction. We deploy PGHS on Meituan with 101 merchants and over 26,000 trajectories. PGHS achieves a group simulation error of 8.80%, improving over the best reasoning-based and fitting-based baselines by 45.8% and 40.9% respectively.

### 🤖 AI 总结

**一句话总结**：Simulating group-level user behavior enables scalable counterfactual evaluation of merchant strategies without costly online experiments. However, building a trustworthy simulator faces two structural...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Meituan, Merchant, Business, Diagnosis, via, Policy-Guided, Dual-Process, User

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15190v1) | [下载PDF](https://arxiv.org/pdf/2604.15190v1.pdf)

---

## [8. Agent-Aided Design for Dynamic CAD Models](https://arxiv.org/abs/2604.15184v1)

**作者**：Mitch Adler, Matthew Russo, Michael Cafarella  
**分类**：cs.AI  
**发布时间**：2026-04-16

### 📄 论文摘要

In the past year, researchers have started to create agentic systems that can design real-world CAD-style objects in a training-free setting, a new variety of system that we call Agent-Aided Design. Generally speaking, these systems place an agent in a feedback loop in which it can write code, compile that code to an assembly of CAD model(s), visualize the model, and then iteratively refine its code based on visual and other feedback. Despite rapid progress, a key problem remains: none of these systems can build complex 3D assemblies with moving parts. For example, no existing system can build a piston, a pendulum, or even a pair of scissors. In order for Agent-Aided Design to make a real impact in industrial manufacturing, we need a system that is capable of generating such 3D assemblies. In this paper we present a prototype of AADvark, an agentic system designed for this task. Unlike previous state-of-the-art systems, AADvark captures the dynamic part interactions with one or more degrees-of-freedom. This design decision allows AADvark to reason directly about assemblies with moving parts and can thereby achieve cross-cutting goals, including but not limited to mechanical movements. Unfortunately, current LLMs are imperfect spatial reasoners, a problem that AADvark addresses by incorporating external constraint solver tools with a specialized visual feedback mechanism. We demonstrate that, by modifying the agent's tools (FreeCAD and the assembly solver), we are able to create a strong verification signal which enables our system to build 3D assemblies with movable parts.

### 🤖 AI 总结

**一句话总结**：In the past year, researchers have started to create agentic systems that can design real-world CAD-style objects in a training-free setting, a new variety of system that we call Agent-Aided Design. G...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent-Aided, Design, Dynamic, CAD, Models, past, year, researchers

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15184v1) | [下载PDF](https://arxiv.org/pdf/2604.15184v1.pdf)

---

## cs.CL

## [9. MADE: A Living Benchmark for Multi-Label Text Classification with Uncertainty Quantification of Medical Device Adverse Events](https://arxiv.org/abs/2604.15203v1)

**作者**：Raunak Agarwal, Markus Wenzel, Simon Baur 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-16

### 📄 论文摘要

Machine learning in high-stakes domains such as healthcare requires not only strong predictive performance but also reliable uncertainty quantification (UQ) to support human oversight. Multi-label text classification (MLTC) is a central task in this domain, yet remains challenging due to label imbalances, dependencies, and combinatorial complexity. Existing MLTC benchmarks are increasingly saturated and may be affected by training data contamination, making it difficult to distinguish genuine reasoning capabilities from memorization. We introduce MADE, a living MLTC benchmark derived from {m}edical device {ad}verse {e}vent reports and continuously updated with newly published reports to prevent contamination. MADE features a long-tailed distribution of hierarchical labels and enables reproducible evaluation with strict temporal splits. We establish baselines across more than 20 encoder- and decoder-only models under fine-tuning and few-shot settings (instruction-tuned/reasoning variants, local/API-accessible). We systematically assess entropy-/consistency-based and self-verbalized UQ methods. Results show clear trade-offs: smaller discriminatively fine-tuned decoders achieve the strongest head-to-tail accuracy while maintaining competitive UQ; generative fine-tuning delivers the most reliable UQ; large reasoning models improve performance on rare labels yet exhibit surprisingly weak UQ; and self-verbalized confidence is not a reliable proxy for uncertainty. Our work is publicly available at https://hhi.fraunhofer.de/aml-demonstrator/made-benchmark.

### 🤖 AI 总结

**一句话总结**：Machine learning in high-stakes domains such as healthcare requires not only strong predictive performance but also reliable uncertainty quantification (UQ) to support human oversight. Multi-label tex...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MADE, Living, Benchmark, Multi-Label, Text, Classification, Uncertainty, Quantification

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15203v1) | [下载PDF](https://arxiv.org/pdf/2604.15203v1.pdf)

---

## cs.CV

## [10. Bidirectional Cross-Modal Prompting for Event-Frame Asymmetric Stereo](https://arxiv.org/abs/2604.15312v1)

**作者**：Ninghui Xu, Fabio Tosi, Lihui Wang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-16

### 📄 论文摘要

Conventional frame-based cameras capture rich contextual information but suffer from limited temporal resolution and motion blur in dynamic scenes. Event cameras offer an alternative visual representation with higher dynamic range free from such limitations. The complementary characteristics of the two modalities make event-frame asymmetric stereo promising for reliable 3D perception under fast motion and challenging illumination. However, the modality gap often leads to marginalization of domain-specific cues essential for cross-modal stereo matching. In this paper, we introduce Bi-CMPStereo, a novel bidirectional cross-modal prompting framework that fully exploits semantic and structural features from both domains for robust matching. Our approach learns finely aligned stereo representations within a target canonical space and integrates complementary representations by projecting each modality into both event and frame domains. Extensive experiments demonstrate that our approach significantly outperforms state-of-the-art methods in accuracy and generalization.

### 🤖 AI 总结

**一句话总结**：Conventional frame-based cameras capture rich contextual information but suffer from limited temporal resolution and motion blur in dynamic scenes. Event cameras offer an alternative visual representa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bidirectional, Cross-Modal, Prompting, Event-Frame, Asymmetric, Stereo, Conventional, frame-based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15312v1) | [下载PDF](https://arxiv.org/pdf/2604.15312v1.pdf)

---

## [11. LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories](https://arxiv.org/abs/2604.15311v1)

**作者**：Zhanhao Liang, Tao Yang, Jie Wu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-16

### 📄 论文摘要

This paper focuses on the alignment of flow matching models with human preferences. A promising way is fine-tuning by directly backpropagating reward gradients through the differentiable generation process of flow matching. However, backpropagating through long trajectories results in prohibitive memory costs and gradient explosion. Therefore, direct-gradient methods struggle to update early generation steps, which are crucial for determining the global structure of the final image. To address this issue, we introduce LeapAlign, a fine-tuning method that reduces computational cost and enables direct gradient propagation from reward to early generation steps. Specifically, we shorten the long trajectory into only two steps by designing two consecutive leaps, each skipping multiple ODE sampling steps and predicting future latents in a single step. By randomizing the start and end timesteps of the leaps, LeapAlign leads to efficient and stable model updates at any generation step. To better use such shortened trajectories, we assign higher training weights to those that are more consistent with the long generation path. To further enhance gradient stability, we reduce the weights of gradient terms with large magnitude, instead of completely removing them as done in previous works. When fine-tuning the Flux model, LeapAlign consistently outperforms state-of-the-art GRPO-based and direct-gradient methods across various metrics, achieving superior image quality and image-text alignment.

### 🤖 AI 总结

**一句话总结**：This paper focuses on the alignment of flow matching models with human preferences. A promising way is fine-tuning by directly backpropagating reward gradients through the differentiable generation pr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, LeapAlign, Post-Training, Flow, Matching, Models, Any, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15311v1) | [下载PDF](https://arxiv.org/pdf/2604.15311v1.pdf)

---

## [12. MM-WebAgent: A Hierarchical Multimodal Web Agent for Webpage Generation](https://arxiv.org/abs/2604.15309v1)

**作者**：Yan Li, Zezi Zeng, Yifan Yang 等 15 位作者  
**分类**：cs.CV, cs.AI, cs.CL  
**发布时间**：2026-04-16

### 📄 论文摘要

The rapid progress of Artificial Intelligence Generated Content (AIGC) tools enables images, videos, and visualizations to be created on demand for webpage design, offering a flexible and increasingly adopted paradigm for modern UI/UX. However, directly integrating such tools into automated webpage generation often leads to style inconsistency and poor global coherence, as elements are generated in isolation. We propose MM-WebAgent, a hierarchical agentic framework for multimodal webpage generation that coordinates AIGC-based element generation through hierarchical planning and iterative self-reflection. MM-WebAgent jointly optimizes global layout, local multimodal content, and their integration, producing coherent and visually consistent webpages. We further introduce a benchmark for multimodal webpage generation and a multi-level evaluation protocol for systematic assessment. Experiments demonstrate that MM-WebAgent outperforms code-generation and agent-based baselines, especially on multimodal element generation and integration. Code & Data: https://aka.ms/mm-webagent.

### 🤖 AI 总结

**一句话总结**：The rapid progress of Artificial Intelligence Generated Content (AIGC) tools enables images, videos, and visualizations to be created on demand for webpage design, offering a flexible and increasingly...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, MM-WebAgent, Hierarchical, Multimodal, Web, Webpage, Generation, rapid

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15309v1) | [下载PDF](https://arxiv.org/pdf/2604.15309v1.pdf)

---

## [13. RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework](https://arxiv.org/abs/2604.15308v1)

**作者**：Hao Gao, Shaoyu Chen, Yifan Zhu 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-16

### 📄 论文摘要

High-level autonomous driving requires motion planners capable of modeling multimodal future uncertainties while remaining robust in closed-loop interactions. Although diffusion-based planners are effective at modeling complex trajectory distributions, they often suffer from stochastic instabilities and the lack of corrective negative feedback when trained purely with imitation learning. To address these issues, we propose RAD-2, a unified generator-discriminator framework for closed-loop planning. Specifically, a diffusion-based generator is used to produce diverse trajectory candidates, while an RL-optimized discriminator reranks these candidates according to their long-term driving quality. This decoupled design avoids directly applying sparse scalar rewards to the full high-dimensional trajectory space, thereby improving optimization stability. To further enhance reinforcement learning, we introduce Temporally Consistent Group Relative Policy Optimization, which exploits temporal coherence to alleviate the credit assignment problem. In addition, we propose On-policy Generator Optimization, which converts closed-loop feedback into structured longitudinal optimization signals and progressively shifts the generator toward high-reward trajectory manifolds. To support efficient large-scale training, we introduce BEV-Warp, a high-throughput simulation environment that performs closed-loop evaluation directly in Bird's-Eye View feature space via spatial warping. RAD-2 reduces the collision rate by 56% compared with strong diffusion-based planners. Real-world deployment further demonstrates improved perceived safety and driving smoothness in complex urban traffic.

### 🤖 AI 总结

**一句话总结**：High-level autonomous driving requires motion planners capable of modeling multimodal future uncertainties while remaining robust in closed-loop interactions. Although diffusion-based planners are eff...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RAD-2, Scaling, Reinforcement, Learning, Generator-Discriminator, Framework, High-level, autonomous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15308v1) | [下载PDF](https://arxiv.org/pdf/2604.15308v1.pdf)

---

## [14. Think in Latent Thoughts: A New Paradigm for Gloss-Free Sign Language Translation](https://arxiv.org/abs/2604.15301v1)

**作者**：Yiyang Jiang, Li Zhang, Xiao-Yong Wei 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-16

### 📄 论文摘要

Many SLT systems quietly assume that brief chunks of signing map directly to spoken-language words. That assumption breaks down because signers often create meaning on the fly using context, space, and movement. We revisit SLT and argue that it is mainly a cross-modal reasoning task, not just a straightforward video-to-text conversion. We thus introduce a reasoning-driven SLT framework that uses an ordered sequence of latent thoughts as an explicit middle layer between the video and the generated text. These latent thoughts gradually extract and organize meaning over time. On top of this, we use a plan-then-ground decoding method: the model first decides what it wants to say, and then looks back at the video to find the evidence. This separation improves coherence and faithfulness. We also built and released a new large-scale gloss-free SLT dataset with stronger context dependencies and more realistic meanings. Experiments across several benchmarks show consistent gains over existing gloss-free methods. Code and data will be released upon acceptance at https://github.com/fletcherjiang/SignThought.

### 🤖 AI 总结

**一句话总结**：Many SLT systems quietly assume that brief chunks of signing map directly to spoken-language words. That assumption breaks down because signers often create meaning on the fly using context, space, an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Think, Latent, Thoughts, New, Paradigm, Gloss-Free, Sign, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15301v1) | [下载PDF](https://arxiv.org/pdf/2604.15301v1.pdf)

---

## [15. AnimationBench: Are Video Models Good at Character-Centric Animation?](https://arxiv.org/abs/2604.15299v1)

**作者**：Leyi Wu, Pengjun Fang, Kai Sun 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-16

### 📄 论文摘要

Video generation has advanced rapidly, with recent methods producing increasingly convincing animated results. However, existing benchmarks-largely designed for realistic videos-struggle to evaluate animation-style generation with its stylized appearance, exaggerated motion, and character-centric consistency. Moreover, they also rely on fixed prompt sets and rigid pipelines, offering limited flexibility for open-domain content and custom evaluation needs. To address this gap, we introduce AnimationBench, the first systematic benchmark for evaluating animation image-to-video generation. AnimationBench operationalizes the Twelve Basic Principles of Animation and IP Preservation into measurable evaluation dimensions, together with Broader Quality Dimensions including semantic consistency, motion rationality, and camera motion consistency. The benchmark supports both a standardized close-set evaluation for reproducible comparison and a flexible open-set evaluation for diagnostic analysis, and leverages visual-language models for scalable assessment. Extensive experiments show that AnimationBench aligns well with human judgment and exposes animation-specific quality differences overlooked by realism-oriented benchmarks, leading to more informative and discriminative evaluation of state-of-the-art I2V models.

### 🤖 AI 总结

**一句话总结**：Video generation has advanced rapidly, with recent methods producing increasingly convincing animated results. However, existing benchmarks-largely designed for realistic videos-struggle to evaluate a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, AnimationBench, Video, Models, Good, Character-Centric, Animation?, generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15299v1) | [下载PDF](https://arxiv.org/pdf/2604.15299v1.pdf)

---

## [16. AD4AD: Benchmarking Visual Anomaly Detection Models for Safer Autonomous Driving](https://arxiv.org/abs/2604.15291v1)

**作者**：Fabrizio Genilotti, Arianna Stropeni, Gionata Grotto 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-16

### 📄 论文摘要

The reliability of a machine vision system for autonomous driving depends heavily on its training data distribution. When a vehicle encounters significantly different conditions, such as atypical obstacles, its perceptual capabilities can degrade substantially. Unlike many domains where errors carry limited consequences, failures in autonomous driving translate directly into physical risk for passengers, pedestrians, and other road users. To address this challenge, we explore Visual Anomaly Detection (VAD) as a solution. VAD enables the identification of anomalous objects not present during training, allowing the system to alert the driver when an unfamiliar situation is detected. Crucially, VAD models produce pixel-level anomaly maps that can guide driver attention to specific regions of concern without requiring any prior assumptions about the nature or form of the hazard. We benchmark eight state-of-the-art VAD methods on AnoVox, the largest synthetic dataset for anomaly detection in autonomous driving. In particular, we evaluate performance across four backbone architectures spanning from large networks to lightweight ones such as MobileNet and DeiT-Tiny. Our results demonstrate that VAD transfers effectively to road scenes. Notably, Tiny-Dinomaly achieves the best accuracy-efficiency trade-off for edge deployment, matching full-scale localization performance at a fraction of the memory cost. This study represents a concrete step toward safer, more responsible deployment of autonomous vehicles, ultimately improving protection for passengers, pedestrians, and all road users.

### 🤖 AI 总结

**一句话总结**：The reliability of a machine vision system for autonomous driving depends heavily on its training data distribution. When a vehicle encounters significantly different conditions, such as atypical obst...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AD4AD, Benchmarking, Visual, Anomaly, Detection, Models, Safer, Autonomous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15291v1) | [下载PDF](https://arxiv.org/pdf/2604.15291v1.pdf)

---

## [17. R3D: Revisiting 3D Policy Learning](https://arxiv.org/abs/2604.15281v1)

**作者**：Zhengdong Hong, Shenrui Wu, Haozhe Cui 等 11 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-04-16

### 📄 论文摘要

3D policy learning promises superior generalization and cross-embodiment transfer, but progress has been hindered by training instabilities and severe overfitting, precluding the adoption of powerful 3D perception models. In this work, we systematically diagnose these failures, identifying the omission of 3D data augmentation and the adverse effects of Batch Normalization as primary causes. We propose a new architecture coupling a scalable transformer-based 3D encoder with a diffusion decoder, engineered specifically for stability at scale and designed to leverage large-scale pre-training. Our approach significantly outperforms state-of-the-art 3D baselines on challenging manipulation benchmarks, establishing a new and robust foundation for scalable 3D imitation learning. Project Page: https://r3d-policy.github.io/

### 🤖 AI 总结

**一句话总结**：3D policy learning promises superior generalization and cross-embodiment transfer, but progress has been hindered by training instabilities and severe overfitting, precluding the adoption of powerful ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：R3D, 3D, Revisiting, Policy, Learning, promises, superior, generalization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15281v1) | [下载PDF](https://arxiv.org/pdf/2604.15281v1.pdf)

---

## [18. SegWithU: Uncertainty as Perturbation Energy for Single-Forward-Pass Risk-Aware Medical Image Segmentation](https://arxiv.org/abs/2604.15271v1)

**作者**：Tianhao Fu, Austin Wang, Charles Chen 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-04-16

### 📄 论文摘要

Reliable uncertainty estimation is critical for medical image segmentation, where automated contours feed downstream quantification and clinical decision support. Many strong uncertainty methods require repeated inference, while efficient single-forward-pass alternatives often provide weaker failure ranking or rely on restrictive feature-space assumptions. We present $\textbf{SegWithU}$, a post-hoc framework that augments a frozen pretrained segmentation backbone with a lightweight uncertainty head. SegWithU taps intermediate backbone features and models uncertainty as perturbation energy in a compact probe space using rank-1 posterior probes. It produces two voxel-wise uncertainty maps: a calibration-oriented map for probability tempering and a ranking-oriented map for error detection and selective prediction. Across ACDC, BraTS2024, and LiTS, SegWithU is the strongest and most consistent single-forward-pass baseline, achieving AUROC/AURC of $0.9838/2.4885$, $0.9946/0.2660$, and $0.9925/0.8193$, respectively, while preserving segmentation quality. These results suggest that perturbation-based uncertainty modeling is an effective and practical route to reliability-aware medical segmentation.   Source code is available at https://github.com/ProjectNeura/SegWithU.

### 🤖 AI 总结

**一句话总结**：Reliable uncertainty estimation is critical for medical image segmentation, where automated contours feed downstream quantification and clinical decision support. Many strong uncertainty methods requi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, SegWithU, Uncertainty, Perturbation, Energy, Single-Forward-Pass, Risk-Aware, Medical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15271v1) | [下载PDF](https://arxiv.org/pdf/2604.15271v1.pdf)

---

## [19. Unsupervised Skeleton-Based Action Segmentation via Hierarchical Spatiotemporal Vector Quantization](https://arxiv.org/abs/2604.15196v1)

**作者**：Umer Ahmed, Syed Ahmed Mahmood, Fawad Javed Fateh 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-16

### 📄 论文摘要

We propose a novel hierarchical spatiotemporal vector quantization framework for unsupervised skeleton-based temporal action segmentation. We first introduce a hierarchical approach, which includes two consecutive levels of vector quantization. Specifically, the lower level associates skeletons with fine-grained subactions, while the higher level further aggregates subactions into action-level representations. Our hierarchical approach outperforms the non-hierarchical baseline, while primarily exploiting spatial cues by reconstructing input skeletons. Next, we extend our approach by leveraging both spatial and temporal information, yielding a hierarchical spatiotemporal vector quantization scheme. In particular, our hierarchical spatiotemporal approach performs multi-level clustering, while simultaneously recovering input skeletons and their corresponding timestamps. Lastly, extensive experiments on multiple benchmarks, including HuGaDB, LARa, and BABEL, demonstrate that our approach establishes a new state-of-the-art performance and reduces segment length bias in unsupervised skeleton-based temporal action segmentation.

### 🤖 AI 总结

**一句话总结**：We propose a novel hierarchical spatiotemporal vector quantization framework for unsupervised skeleton-based temporal action segmentation. We first introduce a hierarchical approach, which includes tw...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unsupervised, Skeleton-Based, Action, Segmentation, via, Hierarchical, Spatiotemporal, Vector

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15196v1) | [下载PDF](https://arxiv.org/pdf/2604.15196v1.pdf)

---

## [20. Boundary-Centric Active Learning for Temporal Action Segmentation](https://arxiv.org/abs/2604.15173v1)

**作者**：Halil Ismail Helvaci, Sen-ching Samson Cheung  
**分类**：cs.CV  
**发布时间**：2026-04-16

### 📄 论文摘要

Temporal action segmentation (TAS) demands dense temporal supervision, yet most of the annotation cost in untrimmed videos is spent identifying and refining action transitions, where segmentation errors concentrate and small temporal shifts disproportionately degrade segmental metrics. We introduce B-ACT, a clip-budgeted active learning framework that explicitly allocates supervision to these high-leverage boundary regions. B-ACT operates in a hierarchical two-stage loop: (i) it ranks and queries unlabeled videos using predictive uncertainty, and (ii) within each selected video, it detects candidate transitions from the current model predictions and selects the top-$K$ boundaries via a novel boundary score that fuses neighborhood uncertainty, class ambiguity, and temporal predictive dynamics. Importantly, our annotation protocol requests labels for only the boundary frames while still training on boundary-centered clips to exploit temporal context through the model's receptive field. Extensive experiments on GTEA, 50Salads, and Breakfast demonstrate that boundary-centric supervision delivers strong label efficiency and consistently surpasses representative TAS active learning baselines and prior state of the art under sparse budgets, with the largest gains on datasets where boundary placement dominates edit and overlap-based F1 scores.

### 🤖 AI 总结

**一句话总结**：Temporal action segmentation (TAS) demands dense temporal supervision, yet most of the annotation cost in untrimmed videos is spent identifying and refining action transitions, where segmentation erro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Boundary-Centric, Active, Learning, Temporal, Action, Segmentation, TAS, demands

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15173v1) | [下载PDF](https://arxiv.org/pdf/2604.15173v1.pdf)

---

## [21. An Analysis of Regularization and Fokker-Planck Residuals in Diffusion Models for Image Generation](https://arxiv.org/abs/2604.15171v1)

**作者**：Onno Niemann, Gonzalo Martínez Muñoz, Alberto Suárez Gonzalez  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-04-16

### 📄 论文摘要

Recent work has shown that diffusion models trained with the denoising score matching (DSM) objective often violate the Fokker--Planck (FP) equation that governs the evolution of the true data density. Directly penalizing these deviations in the objective function reduces their magnitude but introduces a significant computational overhead. It is also observed that enforcing strict adherence to the FP equation does not necessarily lead to improvements in the quality of the generated samples, as often the best results are obtained with weaker FP regularization. In this paper, we investigate whether simpler penalty terms can provide similar benefits. We empirically analyze several lightweight regularizers, study their effect on FP residuals and generation quality, and show that the benefits of FP regularization are available at substantially lower computational cost. Our code is available at https://github.com/OnnoNiemann/fp_diffusion_analysis.

### 🤖 AI 总结

**一句话总结**：Recent work has shown that diffusion models trained with the denoising score matching (DSM) objective often violate the Fokker--Planck (FP) equation that governs the evolution of the true data density...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, of, Diffusion, Analysis, Regularization, Fokker-Planck, Residuals, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15171v1) | [下载PDF](https://arxiv.org/pdf/2604.15171v1.pdf)

---

## [22. OmniLight: One Model to Rule All Lighting Conditions](https://arxiv.org/abs/2604.15170v1)

**作者**：Youngjin Oh, Junyoung Park, Junhyeong Kwon 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-16

### 📄 论文摘要

Adverse lighting conditions, such as cast shadows and irregular illumination, pose significant challenges to computer vision systems by degrading visibility and color fidelity. Consequently, effective shadow removal and ALN are critical for restoring underlying image content, improving perceptual quality, and facilitating robust performance in downstream tasks. However, while achieving state-of-the-art results on specific benchmarks is a primary goal in image restoration challenges, real-world applications often demand robust models capable of handling diverse domains. To address this, we present a comprehensive study on lighting-related image restoration by exploring two contrasting strategies. We leverage a robust framework for ALN, DINOLight, as a specialized baseline to exploit the characteristics of each individual dataset, and extend it to OmniLight, a generalized alternative incorporating our proposed Wavelet Domain Mixture-of-Experts (WD-MoE) that is trained across all provided datasets. Through a comparative analysis of these two methods, we discuss the impact of data distribution on the performance of specialized and unified architectures in lighting-related image restoration. Notably, both approaches secured top-tier rankings across all three lighting-related tracks in the NTIRE 2026 Challenge, demonstrating their outstanding perceptual quality and generalization capabilities. Our codes are available at https://github.com/OBAKSA/Lighting-Restoration.

### 🤖 AI 总结

**一句话总结**：Adverse lighting conditions, such as cast shadows and irregular illumination, pose significant challenges to computer vision systems by degrading visibility and color fidelity. Consequently, effective...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OmniLight, One, Model, Rule, All, Lighting, Conditions, Adverse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15170v1) | [下载PDF](https://arxiv.org/pdf/2604.15170v1.pdf)

---

## cs.LG

## [23. Benchmarking Optimizers for MLPs in Tabular Deep Learning](https://arxiv.org/abs/2604.15297v1)

**作者**：Yury Gorishniy, Ivan Rubachev, Dmitrii Feoktistov 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-16

### 📄 论文摘要

MLP is a heavily used backbone in modern deep learning (DL) architectures for supervised learning on tabular data, and AdamW is the go-to optimizer used to train tabular DL models. Unlike architecture design, however, the choice of optimizer for tabular DL has not been examined systematically, despite new optimizers showing promise in other domains. To fill this gap, we benchmark \Noptimizers optimizers on \Ndatasets tabular datasets for training MLP-based models in the standard supervised learning setting under a shared experiment protocol. Our main finding is that the Muon optimizer consistently outperforms AdamW, and thus should be considered a strong and practical choice for practitioners and researchers, if the associated training efficiency overhead is affordable. Additionally, we find exponential moving average of model weights to be a simple yet effective technique that improves AdamW on vanilla MLPs, though its effect is less consistent across model variants.

### 🤖 AI 总结

**一句话总结**：MLP is a heavily used backbone in modern deep learning (DL) architectures for supervised learning on tabular data, and AdamW is the go-to optimizer used to train tabular DL models. Unlike architecture...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Benchmarking, Optimizers, MLPs, Tabular, Deep, Learning, MLP, heavily

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15297v1) | [下载PDF](https://arxiv.org/pdf/2604.15297v1.pdf)

---

## [24. How Embeddings Shape Graph Neural Networks: Classical vs Quantum-Oriented Node Representations](https://arxiv.org/abs/2604.15273v1)

**作者**：Nouhaila Innan, Antonello Rosato, Alberto Marchisio 等 4 位作者  
**分类**：cs.LG, quant-ph  
**发布时间**：2026-04-16

### 📄 论文摘要

Node embeddings act as the information interface for graph neural networks, yet their empirical impact is often reported under mismatched backbones, splits, and training budgets. This paper provides a controlled benchmark of embedding choices for graph classification, comparing classical baselines with quantum-oriented node representations under a unified pipeline. We evaluate two classical baselines alongside quantum-oriented alternatives, including a circuit-defined variational embedding and quantum-inspired embeddings computed via graph operators and linear-algebraic constructions. All variants are trained and tested with the same backbone, stratified splits, identical optimization and early stopping, and consistent metrics. Experiments on five different TU datasets and on QM9 converted to classification via target binning show clear dataset dependence: quantum-oriented embeddings yield the most consistent gains on structure-driven benchmarks, while social graphs with limited node attributes remain well served by classical baselines. The study highlights practical trade-offs between inductive bias, trainability, and stability under a fixed training budget, and offers a reproducible reference point for selecting quantum-oriented embeddings in graph learning.

### 🤖 AI 总结

**一句话总结**：Node embeddings act as the information interface for graph neural networks, yet their empirical impact is often reported under mismatched backbones, splits, and training budgets. This paper provides a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：vs, How, Embeddings, Shape, Graph, Neural, Networks, Classical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15273v1) | [下载PDF](https://arxiv.org/pdf/2604.15273v1.pdf)

---

## [25. Stability and Generalization in Looped Transformers](https://arxiv.org/abs/2604.15259v1)

**作者**：Asher Labovich  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-16

### 📄 论文摘要

Looped transformers promise test-time compute scaling by spending more iterations on harder problems, but it remains unclear which architectural choices let them extrapolate to harder problems at test time rather than memorize training-specific solutions. We introduce a fixed-point based framework for analyzing looped architectures along three axes of stability -- reachability, input-dependence, and geometry -- and use it to characterize when fixed-point iteration yields meaningful predictions. Theoretically, we prove that looped networks without recall have countable fixed points and cannot achieve strong input-dependence at any spectral regime, while recall combined with outer normalization reliably produces a regime in which fixed points are simultaneously reachable, locally smooth in the input, and supported by stable backpropagation. Empirically, we train single-layer looped transformers on chess, sudoku, and prefix-sums and find that downstream performance tracks the framework's predictions across tasks and architectural configurations. We additionally introduce internal recall, a novel recall placement variant, and show that it becomes competitive with -- and on sudoku, substantially better than -- standard recall placement once outer normalization is applied.

### 🤖 AI 总结

**一句话总结**：Looped transformers promise test-time compute scaling by spending more iterations on harder problems, but it remains unclear which architectural choices let them extrapolate to harder problems at test...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Stability, Generalization, Looped, Transformers, promise, test-time, compute, scaling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15259v1) | [下载PDF](https://arxiv.org/pdf/2604.15259v1.pdf)

---

## [26. RL-STPA: Adapting System-Theoretic Hazard Analysis for Safety-Critical Reinforcement Learning](https://arxiv.org/abs/2604.15201v1)

**作者**：Steven A. Senczyszyn, Timothy C. Havens, Nathaniel Rice 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-16

### 📄 论文摘要

As reinforcement learning (RL) deployments expand into safety-critical domains, existing evaluation methods fail to systematically identify hazards arising from the black-box nature of neural network enabled policies and distributional shift between training and deployment. This paper introduces Reinforcement Learning System-Theoretic Process Analysis (RL-STPA), a framework that adapts conventional STPA's systematic hazard analysis to address RL's unique challenges through three key contributions: hierarchical subtask decomposition using both temporal phase analysis and domain expertise to capture emergent behaviors, coverage-guided perturbation testing that explores the sensitivity of state-action spaces, and iterative checkpoints that feed identified hazards back into training through reward shaping and curriculum design. We demonstrate RL-STPA in the safety-critical test case of autonomous drone navigation and landing, revealing potential loss scenarios that can be missed by standard RL evaluations. The proposed framework provides practitioners with a toolkit for systematic hazard analysis, quantitative metrics for safety coverage assessment, and actionable guidelines for establishing operational safety bounds. While RL-STPA cannot provide formal guarantees for arbitrary neural policies, it offers a practical methodology for systematically evaluating and improving RL safety and robustness in safety-critical applications where exhaustive verification methods remain intractable.

### 🤖 AI 总结

**一句话总结**：As reinforcement learning (RL) deployments expand into safety-critical domains, existing evaluation methods fail to systematically identify hazards arising from the black-box nature of neural network ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL-STPA, Adapting, System-Theoretic, Hazard, Analysis, Safety-Critical, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15201v1) | [下载PDF](https://arxiv.org/pdf/2604.15201v1.pdf)

---

## [27. One-shot learning for the complex dynamical behaviors of weakly nonlinear forced oscillators](https://arxiv.org/abs/2604.15181v1)

**作者**：Teng Ma, Luca Rosafalco, Wei Cui 等 5 位作者  
**分类**：cs.LG, math.DS  
**发布时间**：2026-04-16

### 📄 论文摘要

Extrapolative prediction of complex nonlinear dynamics remains a central challenge in engineering. This study proposes a one-shot learning method to identify global frequency-response curves from a single excitation time history by learning governing equations. We introduce MEv-SINDy (Multi-frequency Evolutionary Sparse Identification of Nonlinear Dynamics) to infer the governing equations of non-autonomous and multi-frequency systems. The methodology leverages the Generalized Harmonic Balance (GHB) method to decompose complex forced responses into a set of slow-varying evolution equations. We validated the capabilities of MEv-SINDy on two critical Micro-Electro-Mechanical Systems (MEMS). These applications include a nonlinear beam resonator and a MEMS micromirror. Our results show that the model trained on a single point accurately predicts softening/hardening effects and jump phenomena across a wide range of excitation levels. This approach significantly reduces the data acquisition burden for the characterization and design of nonlinear microsystems.

### 🤖 AI 总结

**一句话总结**：Extrapolative prediction of complex nonlinear dynamics remains a central challenge in engineering. This study proposes a one-shot learning method to identify global frequency-response curves from a si...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, One-shot, learning, complex, dynamical, behaviors, weakly, nonlinear

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15181v1) | [下载PDF](https://arxiv.org/pdf/2604.15181v1.pdf)

---

## [28. AdaSplash-2: Faster Differentiable Sparse Attention](https://arxiv.org/abs/2604.15180v1)

**作者**：Nuno Gonçalves, Hugo Pitorro, Vlad Niculae 等 7 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-04-16

### 📄 论文摘要

Sparse attention has been proposed as a way to alleviate the quadratic cost of transformers, a central bottleneck in long-context training. A promising line of work is $α$-entmax attention, a differentiable sparse alternative to softmax that enables input-dependent sparsity yet has lagged behind softmax due to the computational overhead necessary to compute the normalizer $τ$. In this paper, we introduce AdaSplash-2, which addresses this limitation through a novel histogram-based initialization that reduces the number of iterations needed to compute $τ$ to typically 1--2. The key idea is to compute a coarse histogram of attention scores on the fly and store it in on-chip SRAM, yielding a more accurate initialization that enables fast forward and backward computation. Combined with a sparsity-aware GPU implementation that skips zero blocks with low overhead, AdaSplash-2 matches or improves per-step training time relative to FlashAttention-2 when block sparsity is moderate-to-high (e.g., $>$60\%), which often occurs at long-context lengths. On downstream tasks, models trained with our efficient $α$-entmax attention match softmax baselines at short-context lengths and achieve substantial gains in long-context settings.

### 🤖 AI 总结

**一句话总结**：Sparse attention has been proposed as a way to alleviate the quadratic cost of transformers, a central bottleneck in long-context training. A promising line of work is $α$-entmax attention, a differen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AdaSplash-2, Faster, Differentiable, Sparse, Attention, has, been, proposed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15180v1) | [下载PDF](https://arxiv.org/pdf/2604.15180v1.pdf)

---

## [29. MambaSL: Exploring Single-Layer Mamba for Time Series Classification](https://arxiv.org/abs/2604.15174v1)

**作者**：Yoo-Min Jung, Leekyung Kim  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-16

### 📄 论文摘要

Despite recent advances in state space models (SSMs) such as Mamba across various sequence domains, research on their standalone capacity for time series classification (TSC) has remained limited. We propose MambaSL, a framework that minimally redesigns the selective SSM and projection layers of a single-layer Mamba, guided by four TSC-specific hypotheses. To address benchmarking limitations -- restricted configurations, partial University of East Anglia (UEA) dataset coverage, and insufficiently reproducible setups -- we re-evaluate 20 strong baselines across all 30 UEA datasets under a unified protocol. As a result, MambaSL achieves state-of-the-art performance with statistically significant average improvements, while ensuring reproducibility via public checkpoints for all evaluated models. Together with visualizations, these results demonstrate the potential of Mamba-based architectures as a TSC backbone.

### 🤖 AI 总结

**一句话总结**：Despite recent advances in state space models (SSMs) such as Mamba across various sequence domains, research on their standalone capacity for time series classification (TSC) has remained limited. We ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MambaSL, Exploring, Single-Layer, Mamba, Time, Series, Classification, Despite

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15174v1) | [下载PDF](https://arxiv.org/pdf/2604.15174v1.pdf)

---

## [30. Assessing the Potential of Masked Autoencoder Foundation Models in Predicting Downhole Metrics from Surface Drilling Data](https://arxiv.org/abs/2604.15169v1)

**作者**：Aleksander Berezowski, Hassan Hassanzadeh, Gouri Ginde  
**分类**：cs.LG  
**发布时间**：2026-04-16

### 📄 论文摘要

Oil and gas drilling operations generate extensive time-series data from surface sensors, yet accurate real-time prediction of critical downhole metrics remains challenging due to the scarcity of labelled downhole measurements. This systematic mapping study reviews thirteen papers published between 2015 and 2025 to assess the potential of Masked Autoencoder Foundation Models (MAEFMs) for predicting downhole metrics from surface drilling data. The review identifies eight commonly collected surface metrics and seven target downhole metrics. Current approaches predominantly employ neural network architectures such as artificial neural networks (ANNs) and long short-term memory (LSTM) networks, yet no studies have explored MAEFMs despite their demonstrated effectiveness in time-series modeling. MAEFMs offer distinct advantages through self-supervised pre-training on abundant unlabeled data, enabling multi-task prediction and improved generalization across wells. This research establishes that MAEFMs represent a technically feasible but unexplored opportunity for drilling analytics, recommending future empirical validation of their performance against existing models and exploration of their broader applicability in oil and gas operations.

### 🤖 AI 总结

**一句话总结**：Oil and gas drilling operations generate extensive time-series data from surface sensors, yet accurate real-time prediction of critical downhole metrics remains challenging due to the scarcity of labe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Assessing, Potential, Masked, Autoencoder, Foundation, Models, Predicting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.15169v1) | [下载PDF](https://arxiv.org/pdf/2604.15169v1.pdf)

---

