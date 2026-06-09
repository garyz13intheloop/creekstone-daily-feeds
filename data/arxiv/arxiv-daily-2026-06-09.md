# arXiv AI 论文日报 | 2026-06-09

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (12 篇)
- [cs.CL](#csCL) (4 篇)
- [cs.CV](#csCV) (7 篇)
- [cs.AI](#csAI) (7 篇)

---

## cs.AI

## [1. Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting](https://arxiv.org/abs/2606.09809v1)

**作者**：Avijit Ghosh, Anka Reuel, Jenny Chim 等 48 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-08

### 📄 论文摘要

AI evaluation results are produced at scale but reported inconsistently across leaderboards, model cards, benchmark papers, and company blogs. The cost is interpretive: readers cannot reliably compare results across sources, identify what a report omits, or trace an aggregate claim to its underlying evidence. Recent efforts address isolated components but leave three gaps: they cover only narrow slices of the evaluation lifecycle and do not compose into a single interpretable record; they specify static representations that do not differentiate the questions different stakeholders bring to the same evidence; and they remain proposals on paper, lacking the extraction infrastructure required for adoption at scale. We present \EvalCards{}, an operational reporting layer that composes benchmark metadata, evaluation run data, and model metadata into a unified record. We (1) derive a reporting schema from a structured review of 52 papers and 10 stakeholder interviews, (2) implement four interpretive signals (reproducibility, documentation completeness, provenance and risk, and score comparability), rendered through reader modes calibrated to research and non-research audiences, and (3) deploy a monitoring tool that applies \EvalCards{} across 5,816 models, 635 benchmarks, and 101,843 results, surfacing systematic gaps in current reporting practice.

### 🤖 AI 总结

**一句话总结**：AI evaluation results are produced at scale but reported inconsistently across leaderboards, model cards, benchmark papers, and company blogs. The cost is interpretive: readers cannot reliably compare...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Evaluation, Cards, Interpretive, Layer, Reporting, results, produced

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09809v1) | [下载PDF](https://arxiv.org/pdf/2606.09809v1.pdf)

---

## [2. SIGA: Self-Evolving Coding-Agent Adapters for Scientific Simulation](https://arxiv.org/abs/2606.09774v1)

**作者**：Matthew Ho, Brian Liu, Jixuan Chen 等 5 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-06-08

### 📄 论文摘要

Advanced scientific simulators expose specialized input languages that turn simulation goals into executable configurations, but learning them can cost domain scientists hours to days. We study simulator setup as a problem of agent-tool interface grounding: what minimal simulator-specific adaptations are needed for an off-the-shelf coding agent to operate real scientific software? Our intuition is that coding agents already know how to navigate files, edit code, run commands, and repair outputs, but they lack the simulator's executable contract: its vocabulary, structural constraints, validation rules, and termination conditions. We introduce SIGA, a Simulator-Interface Grounding Adapter that supplies this contract through retrieval, procedural memory, in-trajectory validation, and validation-enforced termination. We primarily evaluate SIGA on GEOS, an open-source multiphysics simulator used in subsurface science. SIGA produces a complete GEOS deck in about five minutes with TreeSim above 0.90, matching an extended-budget human expert who took about three hours, a roughly 36x wall-clock speedup. On a harder held-out set, grounding raises TreeSim from 0.720 to 0.789, a roughly 10% relative gain over the bare agent, and can reduce the across-seed standard deviation by 16x. Self-evolution further improves SIGA by rewriting adapter contents from prior trajectories, yielding the highest held-out GEOS mean and matching or outperforming the strongest hand-designed configuration. Transfers to OpenFOAM and LAMMPS show that the dominant mechanism shifts by interface: validation matters most when structural completeness is the bottleneck, while memory and retrieval matter most when domain correctness is the bottleneck. These results suggest that lightweight, self-improvable grounding layers can turn general coding agents into practical operators of scientific software.

### 🤖 AI 总结

**一句话总结**：Advanced scientific simulators expose specialized input languages that turn simulation goals into executable configurations, but learning them can cost domain scientists hours to days. We study simula...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SIGA, Self-Evolving, Coding-Agent, Adapters, Scientific, Simulation, Advanced, simulators

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09774v1) | [下载PDF](https://arxiv.org/pdf/2606.09774v1.pdf)

---

## [3. Collaborative Human-Agent Protocol (CHAP)](https://arxiv.org/abs/2606.09751v1)

**作者**：Arsalan Shahid, Gordon Suttie, Philip Black  
**分类**：cs.AI, cs.CL, cs.HC  
**发布时间**：2026-06-08

### 📄 论文摘要

Foundation models are moving from response generation into operational roles. They plan across steps, call tools, request human input, coordinate with other agents, and increasingly carry responsibility for work that affects customers, claims, code, contracts, and clinical decisions. Production deployments are no longer one human supervising one model. They are multi-human, multi-agent collaborations that cross teams, time zones, and trust boundaries. The technical surface for this collaboration remains weakly specified. When an agent drafts a response and a human edits it before it ships, the moment of human judgement is the most valuable signal in the system. In current practice it is recorded, if at all, in application code, chat threads, ticket comments, and tribal memory. Two protocol standards address adjacent concerns: MCP standardises agent access to tools and data, and A2A standardises agent-to-agent interoperability. Neither defines the shared workspace in which humans and agents perform accountable work together. This paper presents CHAP, the Collaborative Human-Agent Protocol. Under CHAP, the override that used to vanish into a chat thread becomes a structured event carrying a diff, a rationale, and a content hash. The handoff between shifts becomes a portable envelope rather than a pinned message. The human approval of an agent's draft becomes a non-repudiable signed decision that can be replayed years later. The protocol achieves this through a small Core (workspaces, participants, tasks, artefacts, and an append-only evidence log) together with composable profiles that add review, modes, routing, deliberation, handoff, identity, signatures, and transparency-backed audit as deployments require them. Specification, reference implementation, conformance suite, and worked examples are available at: https://github.com/BrightbeamAI/chap

### 🤖 AI 总结

**一句话总结**：Foundation models are moving from response generation into operational roles. They plan across steps, call tools, request human input, coordinate with other agents, and increasingly carry responsibili...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Collaborative, Human-Agent, Protocol, CHAP, Foundation, models, moving, response

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09751v1) | [下载PDF](https://arxiv.org/pdf/2606.09751v1.pdf)

---

## [4. Multi-Turn Evaluation of Deep Research Agents Under Process-Level Feedback](https://arxiv.org/abs/2606.09748v1)

**作者**：Rishabh Sabharwal, Hongru Wang, Amos Storkey 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-06-08

### 📄 论文摘要

Existing benchmarks for deep research agents (DRAs) assess only single-shot outputs, ignoring a key question: can DRAs improve their reports when guided by feedback? To investigate this, we conduct a multi-turn evaluation of DRAs under two feedback settings: self-reflection, in which the agent revises its report without any external diagnostic signal, and process-level feedback, in which the agent receives guidance targeting gaps in its research strategy. To enable process-level feedback, we design Research Gap Inference (RGI), a method that analyzes patterns of satisfied and unsatisfied rubric criteria to infer research-process gaps. Our analysis reveals three key findings: (i) under self-reflection, agents incorporate and regress on rubric criteria at nearly equal rates, yielding negligible net improvement; (ii) a single round of process-level feedback yields substantial gains, raising the normalized score by approximately $8$-$15$ points and yielding a roughly $35$-$40\%$ incorporation rate; (iii) these gains do not compound over subsequent turns, as agents regress on up to $24\%$ of previously satisfied criteria when rewriting the full report to address remaining gaps. Even with targeted guidance, reliable multi-turn improvement remains out of reach for the DRA architectures we evaluate. Our code and results are publicly available at https://github.com/sabharwalrishabh/Multi-Turn-Evaluation-of-DRAs.

### 🤖 AI 总结

**一句话总结**：Existing benchmarks for deep research agents (DRAs) assess only single-shot outputs, ignoring a key question: can DRAs improve their reports when guided by feedback? To investigate this, we conduct a ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, Multi-Turn, Evaluation, Deep, Research, Under, Process-Level

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09748v1) | [下载PDF](https://arxiv.org/pdf/2606.09748v1.pdf)

---

## [5. SearchSwarm: Towards Delegation Intelligence in Agentic LLMs for Long-Horizon Deep Research](https://arxiv.org/abs/2606.09730v1)

**作者**：Pu Ning, Quan Chen, Kun Tao 等 10 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-08

### 📄 论文摘要

Large language models are increasingly expected to handle complex, long-horizon real-world tasks whose context demands can grow without bound, yet model context windows remain inherently finite. Recent work explores a paradigm where a main agent decomposes tasks and dispatches subtasks to subagents, which execute and return only summarized results, conserving the main agent's context budget. However, performing this well requires delegation intelligence: the ability to decompose complex tasks, determine when and what to delegate, and integrate returned results into the ongoing workflow. Training data for this capability is scarce in naturally occurring text, and to our knowledge, how to synthesize such data and train models to acquire this capability remains largely unexplored in the open-source community. To bridge this gap, we present a preliminary exploration targeting deep research, a representative long-horizon agent task. Specifically, we design a harness that guides the model toward high-quality task decomposition and delegation, while constraining subagents to return results properly to support the main agent's workflow. The harness-guided trajectories naturally encode correct delegation decisions, which we use as supervised fine-tuning data to internalize delegation intelligence into model weights. Our resulting model, SearchSwarm-30B-A3B, achieves 68.1 on BrowseComp and 73.3 on BrowseComp-ZH, the best results among all models of comparable scale. We will release our harness, model weights, and training data to facilitate future research.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly expected to handle complex, long-horizon real-world tasks whose context demands can grow without bound, yet model context windows remain inherently finite. Recen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, SearchSwarm, Towards, Delegation, Intelligence, Agentic, Long-Horizon, Deep

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09730v1) | [下载PDF](https://arxiv.org/pdf/2606.09730v1.pdf)

---

## [6. Beyond Probabilistic Similarity: Structural, Temporal, and Causal Limitations of Retrieval-Augmented Generation in the Legal Domain](https://arxiv.org/abs/2606.09724v1)

**作者**：Hudson de Martim  
**分类**：cs.AI  
**发布时间**：2026-06-08

### 📄 论文摘要

Retrieval-Augmented Generation (RAG) has become a standard architectural response to unreliability in legal AI, yet high-profile failures, including fabricated citations submitted to courts and anachronistic legal content presented as current, continue to appear across jurisdictions. We argue that these failures are not residual confabulations to be eliminated by scaling language models, but symptoms of an architectural mismatch between probabilistic retrieval and the hierarchical, temporal, and institutional structure of legal knowledge. We develop the argument in three moves. First, we articulate the ontological commitment of legal knowledge as a triad of properties derivable from classical legal theory: hierarchical and mereological structure, diachronic dynamism under operational closure, and causal traceability of institutional provenance grounded in the duty of justification. Second, we identify three corresponding pathologies of retrieval (mereological blindness, diachronic blindness, and causal opacity), each developed with an operational definition, a failure mechanism, a canonical example, and detection criteria for diagnostic use. Third, we review the state of the art through this lens, showing that existing approaches address these requirements unevenly and do not yet compose into a paradigm that treats them as co-constitutive. From this analysis we derive four architectural commitments that characterize the deterministic-by-design direction for legal retrieval: ontological primacy, event reification, bitemporal correctness, and deterministic interaction protocols. The framework concerns quaestio juris (which norms apply and in what state) rather than the downstream tasks that act on identified norms, and addresses legislative and constitutional retrieval primarily, with interpretive time as an explicit extension.

### 🤖 AI 总结

**一句话总结**：Retrieval-Augmented Generation (RAG) has become a standard architectural response to unreliability in legal AI, yet high-profile failures, including fabricated citations submitted to courts and anachr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Beyond, Probabilistic, Similarity, Structural, Temporal, Causal, Limitations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09724v1) | [下载PDF](https://arxiv.org/pdf/2606.09724v1.pdf)

---

## [7. Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization](https://arxiv.org/abs/2606.09711v1)

**作者**：Mohammad Beigi, Ming Jin, Lifu Huang  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-06-08

### 📄 论文摘要

Reward hacking is usually studied after it becomes visible, once a model earns high proxy reward while failing the intended task. We instead study what proxy RL teaches before that failure appears. We introduce Proxy Reward Internalization and Mechanistic Exploitation (PRIME), a learned capability to assess task correctness, predict proxy acceptance, and reason about exploitable proxy--gold gaps. In coding RL environments with exploitable pytest rewards, we measure PRIME through chain-of-thought monitoring, direct probes, and activation-level concept vectors. We find that PRIME emerges in a staged sequence before sustained reward hacking, and that its current direct-probe score forecasts later hack onset and severity even when the visible hack rate is still low. PRIME also adapts when the evaluator changes, retargeting to whichever proxy--gold gap remains rewarded and persisting when gold reward suppresses overt hacking, and ablating its activation directions reduces hacking. Across checkpoints, in-domain PRIME tracks out-of-domain misalignment. Together these results suggest that exploitable proxy RL amplifies a proxy-internalization capability upstream of visible hacking, making PRIME a candidate early-warning signal for broader alignment risk.

### 🤖 AI 总结

**一句话总结**：Reward hacking is usually studied after it becomes visible, once a model earns high proxy reward while failing the intended task. We instead study what proxy RL teaches before that failure appears. We...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Proxy, Reward, Internalization, Mechanistic, Exploitation, Learned, Precursor, Hacking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09711v1) | [下载PDF](https://arxiv.org/pdf/2606.09711v1.pdf)

---

## cs.CL

## [8. Causally Evaluating the Learnability of Formal Language Tasks](https://arxiv.org/abs/2606.09822v1)

**作者**：Vésteinn Snæbjarnarson, Anej Svete, Josef Valvoda 等 6 位作者  
**分类**：cs.CL, cs.FL  
**发布时间**：2026-06-08

### 📄 论文摘要

Language models, as multi-task learners, acquire a wide range of abilities during training. A fundamental question is how much task-specific data is needed to learn a given task. Answering this for natural language is difficult: tasks are hard to delineate and can confound one another. To rigorously investigate the relationship between data frequency and learnability, we turn to a controlled setting using formal languages induced from probabilistic finite automata. These serve as a methodological testbed to demonstrate that standard correlational evaluation practices are inherently flawed. To enable causal analysis, we introduce the binning semiring, an algebraic object that lets us control how often a targeted property occurs in a sampled corpus. We formulate the experimental pipeline as a causal graphical model and derive decomposed Kullback-Leibler divergence metrics to measure the learnability of specific sub-tasks. Our experiments show that evaluating learnability without causal intervention leads to incorrect conclusions due to confounders in correlational analysis, and serve as a warning about correlational pitfalls in natural-language settings.

### 🤖 AI 总结

**一句话总结**：Language models, as multi-task learners, acquire a wide range of abilities during training. A fundamental question is how much task-specific data is needed to learn a given task. Answering this for na...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Causally, Evaluating, Learnability, Formal, Language, Tasks, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09822v1) | [下载PDF](https://arxiv.org/pdf/2606.09822v1.pdf)

---

## [9. Data Synthesis and Parameter-Efficient Fine-Tuning for Low-Resource NMT: A Case Study on Q'eqchi' Mayan](https://arxiv.org/abs/2606.09767v1)

**作者**：Alexander Chulzhanov, Soeren Eberhardt, Arjun Mukherjee  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-06-08

### 📄 论文摘要

Neural machine translation for digitally low-resource Indigenous languages is often hindered by extreme data scarcity, prompting reliance on extractive web-scraping. To ensure data sovereignty, this study introduces a data synthesis methodology to bootstrap NMT models without scraping target-language parallel text. Focusing on Q'eqchi' Mayan, we transformed community-sourced dictionaries into a massive synthetic corpus, utilizing Parameter-Efficient Fine-Tuning (PEFT) via LoRA adapters on an mT5-base model.   In-domain evaluation demonstrates high structural acquisition (BLEU 42.02), proving that synthetic constraints effectively teach complex agglutinative morphology and VOS word order. However, evaluation against an organic glossary reveals a structural-semantic gap (BLEU 0.59), where the model maintains grammatical integrity but lacks the lexical grounding of natural language. The model exhibits overfitting to the constrained structural variance of the synthetic templates; despite high semantic entropy in the pipeline, it struggles with the syntactic fluidity of natural language, forcing organic inputs into rigid learned patterns. Furthermore, an ablation study utilizing a Multi-Task Learning architecture resulted in negative transfer, suggesting that auxiliary tasks competed for limited parameter capacity within the LoRA adapters, causing over-optimization for synthetic markers at the expense of organic flexibility. Ultimately, we establish that synthetic bootstrapping is a highly effective structural primer, but requires authentic data for semantic refinement via Curriculum Learning.

### 🤖 AI 总结

**一句话总结**：Neural machine translation for digitally low-resource Indigenous languages is often hindered by extreme data scarcity, prompting reliance on extractive web-scraping. To ensure data sovereignty, this s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Data, Synthesis, Parameter-Efficient, Fine-Tuning, Low-Resource, NMT, Case, Study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09767v1) | [下载PDF](https://arxiv.org/pdf/2606.09767v1.pdf)

---

## [10. The Neutral Mask: How RLHF Provides Shallow Alignment while Leaving Partisan Structure Intact in a Large Language Model](https://arxiv.org/abs/2606.09735v1)

**作者**：Wendy K. Tam  
**分类**：cs.CL  
**发布时间**：2026-06-08

### 📄 论文摘要

The ambition behind alignment training is to make large language models safe and useful. The primary mechanism, reinforcement learning from human feedback (RLHF), shapes the behavior of deployed language models by aligning them with ``human values.'' Yet the process is opaque. What values are being encoded; whose values are they; and how does RLHF encode them? A growing body of evidence suggests that RLHF produces only functional compliance rather than deep alignment. We offer a mechanistic case study of this phenomenon for partisan political orientation with a comparison of the internal representations of Llama 3.1 8B before and after RLHF. We show that RLHF does not remove the structured partisan direction in the base model. Instead, it compresses the variance of the partisan signal to generate consistently balanced and non-partisan output. Sparse autoencoder decomposition reveals that policy-encoding features, which activate sporadically in the base model, are completely inactive in the Instruct model. Feature-level steering experiments confirm the causal disconnect. RLHF thus encodes a norm of political neutrality, not by erasing the model's knowledge of partisanship, but by severing the causal pathway from partisan geometry to output generation. Importantly, this neutrality is functional, not structural so that the underlying geometry that enables partisan steering remains intact. The mechanisms that bypass RLHF's guardrails, such as inferring and amplifying a user's partisan identity, reactivate partisan generation. If RLHF operates by disconnecting rather than removing value-laden structure, then the same pattern may hold for other value domains, and the aligned model's behavior may be more fragile than its outputs suggest.

### 🤖 AI 总结

**一句话总结**：The ambition behind alignment training is to make large language models safe and useful. The primary mechanism, reinforcement learning from human feedback (RLHF), shapes the behavior of deployed langu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Neutral, Mask, How, RLHF, Provides, Shallow, Alignment, while

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09735v1) | [下载PDF](https://arxiv.org/pdf/2606.09735v1.pdf)

---

## [11. IS-CoT: Breaking the Long-form Generation Collapse via Interleaved Structural Thinking](https://arxiv.org/abs/2606.09709v1)

**作者**：Zechen Sun, Yuyang Sun, Zecheng Tang 等 9 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-08

### 📄 论文摘要

Generating coherent and controllable long-form content remains a persistent challenge for Large Language Models (LLMs). While reasoning-enhanced models have demonstrated success in logic-intensive domains, our evaluation reveals that they suffer from a severe length collapse in open-ended writing, where performance degrades sharply as target lengths exceed 2,000 words. We attribute this failure to the limitation of static hierarchical planning, which struggles to provide dynamic guidance over extended contexts. To bridge this gap, we introduce the Interleaved Structural Chain-of-Thought (IS-CoT) framework. Unlike external agentic workflows, IS-CoT embeds a dynamic Plan-Write-Reflect cycle into the generation process, enabling continuous strategy adaptation and global alignment without additional assistance. Based on this framework, we construct a high-quality dataset of interleaved reasoning traces via a multi-teacher pipeline and train IS-Writer-8B. Experiments demonstrate that IS-Writer-8B achieves state-of-the-art performance on challenging long-form benchmarks (e.g., +3.08 vs. DeepSeek-V3.2 on LongBench-Write), exhibiting robust length compliance and coherence competitive with significantly larger proprietary models.

### 🤖 AI 总结

**一句话总结**：Generating coherent and controllable long-form content remains a persistent challenge for Large Language Models (LLMs). While reasoning-enhanced models have demonstrated success in logic-intensive dom...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IS-CoT, Breaking, Long-form, Generation, Collapse, via, Interleaved, Structural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09709v1) | [下载PDF](https://arxiv.org/pdf/2606.09709v1.pdf)

---

## cs.CV

## [12. PTL-Diffusion: Manifold-Aware Diffusion with Periodic Terminal Laws](https://arxiv.org/abs/2606.09816v1)

**作者**：Danqi Zhuang, Jisui Huang, Xiaoyue Xi 等 7 位作者  
**分类**：cs.CV, cs.AI, math.PR  
**发布时间**：2026-06-08

### 📄 论文摘要

Standard diffusion models typically use a single time-homogeneous Gaussian terminal distribution as the reference law for generation. While this choice is analytically convenient and empirically powerful, it provides little explicit structure for data concentrated near low-dimensional manifolds, where different regions of the data distribution may correspond to distinct local geometric or semantic factors. As a result, the reverse model must recover manifold-level structure almost entirely from an unstructured terminal reference distribution.   We propose PTL-Diffusion, a proof-of-concept diffusion framework whose forward noising process converges to a nonconstant periodic family of Gaussian terminal laws rather than to a single invariant law. Unlike a phase-conditioned DDPM, where phase information only enters the denoising network while the forward process remains unchanged, PTL-Diffusion embeds phase structure directly into the forward noising dynamics.   The proposed construction remains close to standard denoising diffusion models: for a periodically forced Ornstein--Uhlenbeck-type forward process, we derive closed-form forward marginals, the limiting periodic Gaussian terminal family, and explicit Gaussian reverse posteriors, enabling standard noise-prediction training. We also introduce an invariant-average regularization term coupling the phase-conditioned reverse dynamics through the averaged periodic reference law. Experiments on torus and cylinder point-cloud benchmarks and the Olivetti face dataset show that PTL-Diffusion improves manifold-level distributional matching over matched DDPM baselines, reducing phase-conditioned errors, feature-space covariance errors, and nearest-neighbour manifold distances. These results suggest structured terminal reference laws as a promising direction, while motivating more expressive phase constructions and larger-scale evaluations.

### 🤖 AI 总结

**一句话总结**：Standard diffusion models typically use a single time-homogeneous Gaussian terminal distribution as the reference law for generation. While this choice is analytically convenient and empirically power...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, PTL-Diffusion, Manifold-Aware, Periodic, Terminal, Laws, Standard, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09816v1) | [下载PDF](https://arxiv.org/pdf/2606.09816v1.pdf)

---

## [13. Echo-Memory: A Controlled Study of Memory in Action World Models](https://arxiv.org/abs/2606.09803v1)

**作者**：Wayne King, Zeyue Xue, Yuxuan Bian 等 16 位作者  
**分类**：cs.CV, cs.GR, cs.LG  
**发布时间**：2026-06-08

### 📄 论文摘要

We present \textbf{Echo-Memory}, a controlled study of memory mechanisms in action-conditioned world models. These models generate multi-segment videos from a first frame, text prompt, and camera-action sequence, but their central failure is often memory rather than local image synthesis: after the camera leaves and returns, the scene or salient object may silently change. Existing memory designs are hard to compare because gains are entangled with backbone, training, retrieval, and evaluation differences. Echo-Memory fixes the action-to-video interface and varies only how history is stored and read by the generator. Under a shared video diffusion backbone, optimizer, camera-action representation, sampler, and evaluation pipeline, we compare raw context, compression-based memory, spatial summaries with different read-out paths, and state-space recurrence. This matched matrix separates four otherwise conflated axes: \emph{capacity}, \emph{compression}, \emph{read-out}, and \emph{recurrence}. We also evaluate memory through a three-branch protocol: replay quality, in-domain loop revisit, and open-domain return probes. The branches routinely disagree, showing that replay fidelity is not a sufficient proxy for remembering a world. Three findings follow. Raw context is a strong capacity baseline and improves open-domain return far more than it improves replay metrics. Compactness is not a free substitute for capacity: aggressive spatial and hybrid-compression memories lose the salient evidence needed for return. Finally, block-wise state-space recurrence is the strongest open-domain return mechanism in our matrix, showing that the structure of implicit memory matters as much as the decision to use it. These results provide a compact protocol for studying memory in action world models beyond isolated replay metrics.

### 🤖 AI 总结

**一句话总结**：We present \textbf{Echo-Memory}, a controlled study of memory mechanisms in action-conditioned world models. These models generate multi-segment videos from a first frame, text prompt, and camera-acti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Echo-Memory, Controlled, Study, Memory, Action, World, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09803v1) | [下载PDF](https://arxiv.org/pdf/2606.09803v1.pdf)

---

## [14. Beyond Spherical Harmonics: Rethinking Appearance Models for Radiance Reconstruction](https://arxiv.org/abs/2606.09794v1)

**作者**：Ewa Miazga, Jorge Condor, Piotr Didyk  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-06-08

### 📄 论文摘要

View-dependent appearance modeling remains a challenging problem in novel-view synthesis and reconstruction. Accurately representing complex angular effects often requires substantial memory and computational resources. For new learning-based methods, a common approach is to rely on SH. However, capturing high-frequency phenomena such as specular reflections demands high-order expansions, which increase memory usage and computational cost. Consequently, most methods employ low-order SH, which limits the ability to model complex view-dependent effects, resulting in overly smooth or diffuse representations. To address these limitations, we systematically evaluate a wide range of spherical functions in the context of scene reconstruction. Some of them are introduced to graphics and computer vision for the first time in this paper. Based on the insights from the experiment, we develop a novel spherical formulation, the Normalized Anisotropic Spherical Gabor function that enables efficient modeling and learning of high-frequency appearance effects while maintaining compact representation. Compared to existing approaches, our function achieves higher-quality reconstruction of view-dependent phenomena such as glints, while being up to five times more memory-efficient and more efficient to evaluate. We validate its performance in radiance-field reconstruction tasks.

### 🤖 AI 总结

**一句话总结**：View-dependent appearance modeling remains a challenging problem in novel-view synthesis and reconstruction. Accurately representing complex angular effects often requires substantial memory and compu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Spherical, Harmonics, Rethinking, Appearance, Models, Radiance, Reconstruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09794v1) | [下载PDF](https://arxiv.org/pdf/2606.09794v1.pdf)

---

## [15. End-to-End Optimization of Incoherent Imaging for Classification Under Detector-Limited Readout](https://arxiv.org/abs/2606.09792v1)

**作者**：Archer Wang, Joshua Chen, Sachin Vaidya 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-08

### 📄 论文摘要

End-to-end co-optimization of optical front-ends (e.g. metasurfaces) and neural network back-ends has been widely applied to imaging tasks, yet a formalism characterizing when and why such systems outperform conventional lens-based imaging is largely lacking. This paper focuses on object classification, a central imaging task, and asks when end-to-end optimization of a phase mask for incoherent imaging improves performance over a conventional focusing lens. We find that these gains arise primarily under constrained detector readout and are limited under full detector readout. In the latter setting, we prove that no incoherent phase mask exceeds the ideal-channel mutual information between detector measurements and class labels; a conventional focusing lens approaches this ceiling, and joint optimization yields no empirical gain. When detector readout is constrained -- by coarse spatial sampling or a limited number of measurements -- optimized optics can substantially improve classification by increasing class separability in the detector measurements. These gains are largest under low detector noise and shrink as noise grows, because the optics shape the signal before it reaches the detector but cannot remove noise added afterward. The advantage also depends on the spectral structure of the task: co-design helps most when class-discriminative content is concentrated at lower spatial frequencies than within-class variation. We develop a theoretical framework formalizing these distinctions and test its predictions on synthetic data and standard benchmarks (MNIST, FashionMNIST, SVHN).

### 🤖 AI 总结

**一句话总结**：End-to-end co-optimization of optical front-ends (e.g. metasurfaces) and neural network back-ends has been widely applied to imaging tasks, yet a formalism characterizing when and why such systems out...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, End-to-End, Optimization, Incoherent, Imaging, Classification, Under, Detector-Limited

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09792v1) | [下载PDF](https://arxiv.org/pdf/2606.09792v1.pdf)

---

## [16. POTATR: A Lightweight Image-to-Graph Model for Page-Level Table Extraction](https://arxiv.org/abs/2606.09788v1)

**作者**：Brandon Smock, Libin Liang, Max Sokolov 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-08

### 📄 论文摘要

Large-scale document processing requires contextually aware table extraction (TE) that is both accurate and efficient. Yet current approaches require billions of parameters, hundreds of autoregressive steps, or costly API inference. Motivated by this, we introduce the Page-Object Table Transformer (POTATR), a lightweight 29M parameter image-to-graph model that extends the Table Transformer (TATR) for contextualized page-level TE. POTATR outperforms all models tested on the PubTables-v2 Single Pages benchmark -- including frontier MLLMs -- achieving $\textrm{GriTS}_\textrm{Con}$ of 0.964 while running over 130$\times$ faster at roughly 300$\times$ lower cost. Further, POTATR's output is spatially grounded: every recognized element has a bounding box, enabling visual verification and geometric text assignment. As a result, POTATR performs unified page-level TE while composing with other models, enabling extension to scanned documents via external OCR and to full-document TE via techniques like cross-page merging. Code and models will be released.

### 🤖 AI 总结

**一句话总结**：Large-scale document processing requires contextually aware table extraction (TE) that is both accurate and efficient. Yet current approaches require billions of parameters, hundreds of autoregressive...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：POTATR, Lightweight, Image-to-Graph, Model, Page-Level, Table, Extraction, Large-scale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09788v1) | [下载PDF](https://arxiv.org/pdf/2606.09788v1.pdf)

---

## [17. SemDINO: A DINOv3-Driven Network for Cross-Temporal Semantic Alignment in Change Detection](https://arxiv.org/abs/2606.09772v1)

**作者**：Xinyu Tong, Meihua Zhou, Jinxiao Sun 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-08

### 📄 论文摘要

Semantic change detection (SCD) aims to simultaneously locate land-cover changes and identify semantic categories before and after transition. However, existing methods suffer from insufficient cross-temporal alignment, weak multi-scale representation, and poor robustness to pseudo-changes caused by illumination, season, and registration noise. To address these issues, we propose a novel end-to-end semantic change detection network named SemDINO, which integrates a dual-branch encoder, multi-scale temporal interaction, semantic purification, change enhancement, and decoupled multi-task prediction into a unified framework. Specifically, we construct a dual-branch encoder that combines a CNN backbone and frozen DINOv3 features via gated pyramid fusion, enabling rich multi-scale semantic representation. Then, a multi-scale temporal bidirectional transformer interaction (M-TBTT) module is proposed to achieve global cross-temporal feature alignment and information interaction. To further enhance genuine changes and suppress pseudo-variations, we introduce semantic purification (SCP), bidirectional change enhancement (BiChangeEnhance), and multi-scale change enhancement (MCE) modules collaboratively. Finally, a multi-branch CD prediction head is designed to jointly output binary change mask, bi-temporal semantic maps, and edge constraint. Extensive experiments on public remote sensing CD datasets demonstrate that SemDINO achieves superior performance and generalization ability against state-of-the-art methods, especially in complex scenarios with interference factors.

### 🤖 AI 总结

**一句话总结**：Semantic change detection (SCD) aims to simultaneously locate land-cover changes and identify semantic categories before and after transition. However, existing methods suffer from insufficient cross-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SemDINO, DINOv3-Driven, Network, Cross-Temporal, Semantic, Alignment, Change, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09772v1) | [下载PDF](https://arxiv.org/pdf/2606.09772v1.pdf)

---

## [18. Hybrid Robustness Verification for Spatio-Temporal Neural Networks](https://arxiv.org/abs/2606.09746v1)

**作者**：Sherwin Varghese, Matthew Wicker, Alessio Lomuscio  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-06-08

### 📄 论文摘要

With AI increasingly deployed in safety-critical systems, providing formal robustness guarantees for the underlying models is essential. Existing verification methods either rely on overly conservative approximations or incur prohibitive computational costs. For example, the use of lp-norm perturbations in video settings encodes the belief that the adversary can inject noise in every video frame. In practice, adversarial perturbations exhibit structured spatial and temporal correlations, constrained to lower-dimensional, semantically meaningful subspaces. In this work, we study robustness verification of 3D CNNs processing video and volumetric inputs, targeting applications in action recognition (UCF-101), autonomous driving (Udacity), and medical imaging (MedMNIST) exploiting realistic assumptions on adversarial strength by modelling them as spatio-temporal constraints - where the attacker can modify either a subset of frames or patches within a set of consecutive frames. We demonstrate that modelling realistic constraints enables tighter approximations. We introduce Spatio-Temporal Bound Propagation (STBP), a verification framework that computes an exact closed-form characterization of the first convolutional layer and propagates certified bounds through subsequent layers using scalable approximations. Computing the exact closed form provides the tightest bounds for the first convolutional layer. Thus, we utilise approximation methods in the remainder of the network. To spur further progress in this field, we propose ST-Bench, a verification benchmark for autonomous driving and activity recognition, to systematically evaluate verifiable robustness. Compared to existing verification-based approaches, STBP provides stronger robustness guarantees with significantly improved scalability, achieving 1.7x higher certified robust accuracy under identical perturbation budgets.

### 🤖 AI 总结

**一句话总结**：With AI increasingly deployed in safety-critical systems, providing formal robustness guarantees for the underlying models is essential. Existing verification methods either rely on overly conservativ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hybrid, Robustness, Verification, Spatio-Temporal, Neural, Networks, increasingly, deployed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09746v1) | [下载PDF](https://arxiv.org/pdf/2606.09746v1.pdf)

---

## cs.LG

## [19. An Agency-Transferring Model-Free Policy Enhancement Technique](https://arxiv.org/abs/2606.09825v1)

**作者**：Anton Bolychev, Georgiy Malaniya, Sinan Ibrahim 等 4 位作者  
**分类**：cs.LG, cs.AI, eess.SY, math.OC  
**发布时间**：2026-06-08

### 📄 论文摘要

Training reinforcement learning (RL) policies from scratch is   costly: it requires careful reward and environment design,   extensive tuning, and substantial computation.   Yet many control problems already have a functional but   suboptimal policy available as a baseline.   This paper proposes a method for embedding such a baseline into   the RL training process, simultaneously improving training   efficiency relative to from-scratch methods and producing a   learning policy that outperforms the baseline.   At each step, the method arbitrates between the baseline policy   and a trainable learning policy, initially relying strongly on   the baseline policy and then progressively transferring agency to   the learning policy.   By the end of training, the learning policy is a standalone   neural network that operates without baseline policy support.   The paper formalizes what it means for the baseline policy to be   functional: under this policy, the agent reaches a goal set and   remains there with high probability.   The proposed arbitration mechanism is designed to exploit this   property during training, yielding high goal-reaching rates right   from the beginning of training.   A theoretical analysis provides a formal interpretation of this   behavior under stated assumptions and extends it to the final   baseline-free regime, where explicit lower bounds are derived for   the goal-reaching probability of the standalone learning policy.   Empirical results on continuous-control benchmarks show that the   proposed method achieves returns that match or exceed those of   competitive approaches, while maintaining the highest   goal-reaching rates throughout training among the compared   methods -- including in the final stage, where the learning policy   operates without any baseline support.

### 🤖 AI 总结

**一句话总结**：Training reinforcement learning (RL) policies from scratch is   costly: it requires careful reward and environment design,   extensive tuning, and substantial computation.   Yet many control problems ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Agency-Transferring, Model-Free, Policy, Enhancement, Technique, Training, reinforcement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09825v1) | [下载PDF](https://arxiv.org/pdf/2606.09825v1.pdf)

---

## [20. Topological Neural Operators](https://arxiv.org/abs/2606.09806v1)

**作者**：Lennart Bastian, Samuel Leventhal, Mustafa Hajij 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-08

### 📄 论文摘要

We introduce Topological Neural Operators (TNOs), a principled framework for operator learning on cell complexes that lifts neural operators (NOs) from functions on points and/or edges to topological domains. TNOs represent data as features defined on cells of varying dimension and model their interactions through Discrete Exterior Calculus, enabling explicit cross-dimensional coupling via gradient-, curl-, and divergence-type operators. The key design principle is to decouple where information flows, as governed by fixed topological operators, from how it is transformed (which is learned), yielding models that respect the geometric support of physical quantities and expose conservation and compatibility structure. We further propose Hierarchical TNOs (HTNOs), which incorporate learned coarse complexes to propagate long-range and topology-dependent information. Our framework subsumes existing NOs as a special case, providing a unified perspective on operator learning across discretizations. Across a range of PDE benchmarks, including irregular-geometry flow problems, TNOs and HTNOs improve accuracy; controlled studies further isolate the benefits of native higher-rank and topological structure. Project page: https://circle-group.github.io/research/TNO

### 🤖 AI 总结

**一句话总结**：We introduce Topological Neural Operators (TNOs), a principled framework for operator learning on cell complexes that lifts neural operators (NOs) from functions on points and/or edges to topological ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Topological, Neural, Operators, introduce, TNOs, principled, framework

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09806v1) | [下载PDF](https://arxiv.org/pdf/2606.09806v1.pdf)

---

## [21. Bandits for Efficient Experimentation: Adapting to Control Group, Preferences, and Context Drifts](https://arxiv.org/abs/2606.09802v1)

**作者**：Udvas Das, Waris Radji, Debabrota Basu 等 4 位作者  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-06-08

### 📄 论文摘要

We consider a variant of the linear contextual stochastic multi-armed bandits, where the learner must provide recommendations to a group of users, each having its personalized preference vector, and in the presence of context distributions that are drifting over time. Under practitioner-friendly assumptions, we reduce this setting to linear bandit with stationary mean but heteroskedastic and non-stationary noise. We further study the case when the learner must ensure the mean reward of each decision must exceed that of a baseline strategy $\boldsymbolπ_0$ at each decision step. We introduce Dri-MED, an algorithm inspired from the linear version of the MED strategy, and carefully adapted to handle the non-stationary heteroskedastic noise. We show that the instance-dependent regret scales as $\tilde{\mathcal O}\left(\fracκ{\tildeΔ}d^2(\log(T)\right)$, where $\tildeΔ$ is the constraint-aware sub-optimality gap subject to policy $π_0$, with variance-aware multiplicative term $κ$ that we carefully handle using heteroskedastic regression. We further show Dri-MED enjoys $\tilde{\mathcal{O}}(d)$ expected constraint violations. Our numerical results suggest that Dri-MED significantly outperforms conservative baselines that ignores the drift and preference structure.

### 🤖 AI 总结

**一句话总结**：We consider a variant of the linear contextual stochastic multi-armed bandits, where the learner must provide recommendations to a group of users, each having its personalized preference vector, and i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bandits, Efficient, Experimentation, Adapting, Control, Group, Preferences, Context

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09802v1) | [下载PDF](https://arxiv.org/pdf/2606.09802v1.pdf)

---

## [22. Zero Touch Predictive Orchestration: Automating Time-Series Models for the Cloud-Edge Continuum](https://arxiv.org/abs/2606.09787v1)

**作者**：Abd Elghani Meliani, Arora Sagar, Adlen Ksentini 等 4 位作者  
**分类**：cs.LG, cs.NI  
**发布时间**：2026-06-08

### 📄 论文摘要

The Cloud-Edge Continuum (CEC) enables latency-critical applications by distributing resources to the far edge, but its extreme volatility makes proactive Zero Touch Management via time-series forecasting essential. However, orchestrators face a severe "cold start" problem: newly discovered nodes lack the historical data required to train localized predictive models, while generalized models fail to capture unique hardware and microservice behaviors. To solve this, we propose a fully automated time-series prediction architecture driven by a novel data-mixing methodology. At the infrastructure level, we introduce a lightweight, technology-agnostic Resource Exposer (RE) that dynamically discovers nodes and continuously collects customizable telemetry (e.g., compute, network, energy). To overcome the sparsity of these initial local samples, our framework automatically merges them with TimeTrack, our publicly available, high-resolution dataset collected at 45-second intervals. This synergizes TimeTrack's foundational, high-frequency temporal patterns with the precise calibration of the local node data. Processed through a Neural Architecture Search (NAS) engine, the system automatically generates highly accurate baseline models. Experimental results demonstrate that merging the target data with TimeTrack effectively mitigates the cold start challenge. This integration significantly improves forecasting accuracy measured in Mean Squared Error (MSE), Mean Absolute Error (MAE), and Mean Absolute Percentage Error (MAPE) and accelerates convergence compared to training on the sparse local samples alone, training solely on generic datasets, or mixing the target data with standard alternative datasets, establishing a robust foundation for continuous MLOps deployment.

### 🤖 AI 总结

**一句话总结**：The Cloud-Edge Continuum (CEC) enables latency-critical applications by distributing resources to the far edge, but its extreme volatility makes proactive Zero Touch Management via time-series forecas...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Zero, Touch, Predictive, Orchestration, Automating, Time-Series, Models, Cloud-Edge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09787v1) | [下载PDF](https://arxiv.org/pdf/2606.09787v1.pdf)

---

## [23. iOSWorld: A Benchmark for Personally Intelligent Phone Agents](https://arxiv.org/abs/2606.09764v1)

**作者**：Lawrence Keunho Jang, Mareks Woodside, Geronimo Carom 等 6 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-06-08

### 📄 论文摘要

A useful phone agent needs to be personally intelligent. It should reason over a user's identity, history, and preferences as they exist on the device, not just follow isolated instructions in an impersonal sandbox. Existing mobile agent benchmarks lack this kind of personalization. We introduce iOSWorld, the first interactive native iOS simulator benchmark built around a persistent user identity spanning 26 newly built iOS apps. These apps contain connected data such as transactions, messages, travel records, social relationships, and financial activity. iOSWorld includes 133 tasks across three increasingly difficult categories. Single-app tasks (27) test one app, multi-app tasks (60) span 2 to 8 apps, and memory and personalization tasks (46) require agents to infer patterns from personal data. We evaluate frontier and open-source computer-use models in both vision-only and privileged vision+XML settings. The best configuration reaches 52\% overall but only 37\% on multi-app tasks. Privileged vision+XML access improves frontier models by up to 26 percentage points, while smaller models do not benefit from added accessibility-tree input. We release iOSWorld as an open-source benchmark with all apps, seeded data, tasks, rubrics, and evaluation code.

### 🤖 AI 总结

**一句话总结**：A useful phone agent needs to be personally intelligent. It should reason over a user's identity, history, and preferences as they exist on the device, not just follow isolated instructions in an impe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, iOSWorld, Benchmark, Personally, Intelligent, Phone, useful, needs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09764v1) | [下载PDF](https://arxiv.org/pdf/2606.09764v1.pdf)

---

## [24. Preserving Plasticity in Continual Learning via Dynamical Isometry](https://arxiv.org/abs/2606.09762v1)

**作者**：Andries Rosseau, Robert Müller, Ann Nowé  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-08

### 📄 论文摘要

Continual training of deep neural networks under non-stationarity often leads to a progressive loss of plasticity, eventually limiting further learning. We relate plasticity to the empirical Neural Tangent Kernel, and identify dynamical isometry (the condition that layer-wise Jacobian singular values remain close to one) as a key mechanism for preserving plasticity in continual learning. We revisit a class of networks that are almost-everywhere isometric while remaining universal Lipschitz function approximators, demonstrating that near-dynamical isometry is compatible with expressive nonlinear representations. For general architectures, we propose an efficient isometry-promoting regularization scheme and identify a novel mechanism by which it can reactivate dormant ReLU units. Building on this, we introduce AdamO, an Adam-style adaptive optimizer that decouples isometry regularization from gradient updates, analogous to AdamW. We further reinterpret prior plasticity-preserving approaches through the lens of dynamical isometry, showing that they target only a partial measure of isometry. Across supervised and reinforcement-learning continual-learning benchmarks designed to induce plasticity loss, our methods consistently match or outperform existing approaches.

### 🤖 AI 总结

**一句话总结**：Continual training of deep neural networks under non-stationarity often leads to a progressive loss of plasticity, eventually limiting further learning. We relate plasticity to the empirical Neural Ta...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Preserving, Plasticity, Continual, Learning, via, Dynamical, Isometry, training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09762v1) | [下载PDF](https://arxiv.org/pdf/2606.09762v1.pdf)

---

## [25. Perturbative Contrastive Physical Learning](https://arxiv.org/abs/2606.09756v1)

**作者**：Kyungeun Kim, Amanuel Anteneh, Israel Klich 等 5 位作者  
**分类**：cs.LG, cond-mat.dis-nn  
**发布时间**：2026-06-08

### 📄 论文摘要

Responses to perturbations are key to understanding physical systems. The ability to contrast such responses by comparing how a system reacts under slightly different conditions provides a mechanism for learning. Here, we introduce Perturbative Contrastive Physical Learning (PCPL), a general framework in which learning emerges from measurable contrasts between physical states produced by controlled changes to inputs, boundary conditions, parameters, or interpreter functions. PCPL unifies and extends prior approaches: Equilibrium Propagation is rooted in contrasts between free and nudged equilibria in energy-based systems, while Frequency Propagation corresponds to contrasts extracted from sinusoidally driven, frequency-demodulated responses. We show that contrast-driven updates can reflect either local sensitivities or global inverse-problem structure, yet do not require centralized gradient computation. Instead, effective learning geometry emerges implicitly from the system's own physical response, allowing learning behavior to arise without an external processor or explicit backpropagation. We demonstrate PCPL in two platforms: (i) spring networks that update bond stiffness using measured displacements and forces, and (ii) continuous-variable photonic circuits trained via x quadrature measurements and finite-difference estimates of the Jacobian. Both platforms successfully learn classification tasks. We further show that a continuous-variable photonic circuit can be trained to implement analog multiplication, illustrating a step toward more autonomous physical learning systems.

### 🤖 AI 总结

**一句话总结**：Responses to perturbations are key to understanding physical systems. The ability to contrast such responses by comparing how a system reacts under slightly different conditions provides a mechanism f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Perturbative, Contrastive, Physical, Learning, Responses, perturbations, key, understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09756v1) | [下载PDF](https://arxiv.org/pdf/2606.09756v1.pdf)

---

## [26. Learning Dynamics Reveal a Hierarchy of Weight-Induced Layerwise Gram Metrics](https://arxiv.org/abs/2606.09744v1)

**作者**：Claudio Nordio  
**分类**：cs.LG, cond-mat.dis-nn  
**发布时间**：2026-06-08

### 📄 论文摘要

We study feed-forward ReLU networks with fixed readout and quadratic loss. The aim is to rewrite gradient descent not primarily as a dynamics in weight space, but as a collective dynamics closed in terms of fields defined on the training-set space. For a single hidden layer, the weight variables can be eliminated from the activation dynamics, yielding a closed equation for the residuals governed by a collective kernel that factorizes into an input-geometric matrix and a dynamical co-activation matrix. For deeper networks, the residual dynamics retains a clean layer-wise kernel structure. However, from depth three onward, closure requires a hierarchy of weight-induced Gram operators that mediate information transport across layers.

### 🤖 AI 总结

**一句话总结**：We study feed-forward ReLU networks with fixed readout and quadratic loss. The aim is to rewrite gradient descent not primarily as a dynamics in weight space, but as a collective dynamics closed in te...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Learning, Dynamics, Reveal, Hierarchy, Weight-Induced, Layerwise, Gram

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09744v1) | [下载PDF](https://arxiv.org/pdf/2606.09744v1.pdf)

---

## [27. Tight Sample Complexity of Transformers](https://arxiv.org/abs/2606.09731v1)

**作者**：Chenxiao Yang, Nathan Srebro, Zhiyuan Li  
**分类**：cs.LG  
**发布时间**：2026-06-08

### 📄 论文摘要

We tightly characterize the VC dimension of depth-$L$ Transformers with a total of $W$ parameters, mapping an input sequence of length $T$ to a single output, establishing an upper bound of $O(L W \log (T W))$ and a nearly matching lower bound of $Ω(L W \log (T W / L))$. We further tightly characterize the sample complexity of chain-of-thought learning using such a Transformer, showing teacher forcing (i.e. selecting a predictor consistent with the entire chain-of-thought on training data) learns with sample complexity $O\left(L W \log \left(\left(T+T^{\prime}\right) W\right)\right)$ and that any learning rule that uses chain-of-thought data requires at least $Ω\left(L W \log \left(\left(T+T^{\prime}\right) W / L\right)\right)$ examples, where $T$ is the input length and $T^{\prime}$ is the number of autoregressive steps.

### 🤖 AI 总结

**一句话总结**：We tightly characterize the VC dimension of depth-$L$ Transformers with a total of $W$ parameters, mapping an input sequence of length $T$ to a single output, establishing an upper bound of $O(L W \lo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, We, Tight, Sample, Complexity, Transformers, tightly, characterize

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09731v1) | [下载PDF](https://arxiv.org/pdf/2606.09731v1.pdf)

---

## [28. Disentanglement with Holographic Reduced Representations](https://arxiv.org/abs/2606.09725v1)

**作者**：Jhonny J. Velasquez Olivera, Christo K. Thomas, Walid Saad  
**分类**：cs.LG  
**发布时间**：2026-06-08

### 📄 论文摘要

Disentanglement, the separation of factors of variation in data using neural networks, remains a long-standing challenge in machine learning. Prior work has addressed this problem with variational autoencoders and generative adversarial networks that incorporate ideas from variational inference and information-theoretic constraints. In contrast to methods that rely on continuous representations, we propose a design that treats disentangled representations as symbolic structures, motivated by the compositional relationships among the concepts that make up samples from a distribution. However, learning discrete symbolic structures with neural networks while maintaining differentiability is difficult and often requires complex architectures. To address this, we introduce an unsupervised learning algorithm that uses holographic reduced representations (HRR) for neural disentanglement. We show that the HRR unbinding operation provides an inductive bias for separating factors and yields competitive results against baselines, as measured by latent traversals and disentanglement metrics. We complement these empirical findings with an information-theoretic analysis of the HRR unbinding channel. We prove that unbinding induces approximately independent symbol-value pairs and derive a per-slot capacity bound that quantifies how many distinct symbolic concepts can be reliably encoded, giving a quantitative account of the inductive bias toward disentanglement. The resulting representations differ from standard autoencoder-based models, in that their latent units are vectors that are summed together, rather than scalar dimensions of a low-dimensional latent vector. We show that this HRR representation is more robust to noise than other disentangled representations and maintains reconstruction quality across a range of SNRs.

### 🤖 AI 总结

**一句话总结**：Disentanglement, the separation of factors of variation in data using neural networks, remains a long-standing challenge in machine learning. Prior work has addressed this problem with variational aut...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Disentanglement, Holographic, Reduced, Representations, separation, factors, variation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09725v1) | [下载PDF](https://arxiv.org/pdf/2606.09725v1.pdf)

---

## [29. Evaluating the Representation Space of Diffusion Models via Self-Supervised Principles](https://arxiv.org/abs/2606.09718v1)

**作者**：Xiao Li, Yixuan Jia, Zekai Zhang 等 9 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-06-08

### 📄 论文摘要

Diffusion models have demonstrated remarkable generative capabilities and have also emerged as powerful self-supervised representation learners, yet the connection between these two abilities remains less explored. Drawing inspiration from self-supervised learning (SSL), we introduce a framework for jointly evaluating the representation and generation capabilities of diffusion models. Specifically, we decompose features into invariant and residual components and derive the Invariant Contamination Ratio (ICR), a Fisher-based metric that quantifies how residual variation contaminates invariant signal in feature space. We use this framework to analyze both discriminative and generative behavior of diffusion models. On the representation side, we find that invariance peaks at intermediate noise levels, which also yield the best downstream classification performance. On the generative side, we study how training transitions from genuine generalization to memorization in data-limited regimes, and show that ICR serves as a sensitive training-time indicator of early learning: increasing residual energy along Fisher directions marks the onset of memorization, detectable from training features alone without external evaluators or held-out test sets. Overall, our results show that diffusion models can be monitored from a self-supervised perspective through the geometry of their learned representations.

### 🤖 AI 总结

**一句话总结**：Diffusion models have demonstrated remarkable generative capabilities and have also emerged as powerful self-supervised representation learners, yet the connection between these two abilities remains ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Diffusion, Evaluating, Representation, Space, Models, via, Self-Supervised

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09718v1) | [下载PDF](https://arxiv.org/pdf/2606.09718v1.pdf)

---

## [30. BrainSurgery: Reproducible and Reliable Declarative Weight Manipulations for Model Editing and Upcycling](https://arxiv.org/abs/2606.09707v1)

**作者**：Gianluca Barmina, Annemette Broch Pirchert, Andrea Blasi Núñez 等 5 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-06-08

### 📄 论文摘要

As deep learning models scale, managing, inspecting, and modifying large checkpoints has become increasingly challenging. Researchers often need to alter model weights for layer restructuring, precision casting, low-rank factorization, and architectural debugging, yet these workflows often rely on fragile ad-hoc Python scripts. Here, we introduce BrainSurgery, a tool for robust and reproducible "tensor surgery" on neural network checkpoints, and provide a system demonstration covering four examples and three case studies from model upcycling to LoRA extraction. By abstracting storage formats and memory management, BrainSurgery executes complex transformations through declarative YAML plans. It supports structural modifications, mathematical transformations, and tensor reshaping through expressive regex and structural targeting, while built-in assertions validate tensor shapes, data types, and values to prevent silent errors. We envision that BrainSurgery will provide a strong foundation for future research through its reproducible and validated operations.

### 🤖 AI 总结

**一句话总结**：As deep learning models scale, managing, inspecting, and modifying large checkpoints has become increasingly challenging. Researchers often need to alter model weights for layer restructuring, precisi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BrainSurgery, Reproducible, Reliable, Declarative, Weight, Manipulations, Model, Editing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.09707v1) | [下载PDF](https://arxiv.org/pdf/2606.09707v1.pdf)

---

