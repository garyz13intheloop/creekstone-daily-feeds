# arXiv AI 论文日报 | 2026-05-20

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (12 篇)
- [cs.CL](#csCL) (6 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.LG](#csLG) (6 篇)

---

## cs.AI

## [1. A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents](https://arxiv.org/abs/2605.20173v1)

**作者**：Vasundra Srinivasan  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-05-19

### 📄 论文摘要

Production LLM agents combine stochastic model outputs with deterministic software systems, yet the boundary between the two is rarely treated as a first-class architectural object. This paper names that boundary the stochastic-deterministic boundary (SDB): a four-part contract among a proposer, verifier, commit step, and reject signal that specifies how an LLM output becomes a system action. We argue that the SDB is the load-bearing primitive of production agent runtimes.   Around this primitive, we organize agent runtime design into three concerns: Coordination, State, and Control. We present a catalog of six runtime patterns that compose the SDB differently across conversational, autonomous, and long-horizon agents: hierarchical delegation, scatter-gather plus saga, event-driven sequencing, shared state machine, supervisor plus gate, and human in the loop. For each pattern, we trace its lineage to distributed-systems concepts and identify what changes when the worker is stochastic.   The paper contributes a five-step methodology for selecting runtime patterns, a diagnostic procedure that maps production failures to pattern weaknesses, and a failure mode called replay divergence, in which LLM-based consumers of a deterministic event log produce different downstream outputs under model-version or prompt changes. A stylized reliability decomposition separates per-call model variance from architectural momentum, motivating the claim that as model variance decreases, pattern choice and SDB strength become increasingly important levers for long-run reliability. We apply the methodology to five workloads and provide one runnable reference implementation for a 90-day contract-renewal agent.

### 🤖 AI 总结

**一句话总结**：Production LLM agents combine stochastic model outputs with deterministic software systems, yet the boundary between the two is rarely treated as a first-class architectural object. This paper names t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Methodology, Selecting, Composing, Runtime, Architecture, Patterns, Production

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20173v1) | [下载PDF](https://arxiv.org/pdf/2605.20173v1.pdf)

---

## [2. HaorFloodAlert: Deseasonalized ML Ensemble for 72-Hour Flood Prediction in Bangladesh Haor Wetlands](https://arxiv.org/abs/2605.20167v1)

**作者**：Salma Hoque Talukdar Koli, Fahima Haque Talukder Jely, Md. Samiul Alim 等 4 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-05-19

### 📄 论文摘要

Flash floods in Bangladesh's haor wetlands show up with almost no warning. They wreck the annual boro rice harvest. Current setups, built for riverine floods, miss backwater dynamics entirely. These basins are flat. Water does not behave like it does on the Brahmaputra.   We built HaorFloodAlert, a deseasonalized machine learning ensemble that forecasts 72-hour flood probability for the Sunamganj Haor (approximately 8,000 km2). Temperature was acting as a seasonal cheat code - it inflated accuracy by 6.9 pp just because floods happen in warm months. We caught that. We also built an upstream Barak River Sentinel-1 SAR proxy from Silchar, Assam, giving about 36 hours of lead time. Otsu-thresholded SAR change detection validates at 84-91 percent spatial match.   The operational ensemble (RF 0.5625 + XGBoost 0.4375) hits 89.6 percent LOOCV accuracy, 87.5 percent recall, and 0.943 AUC-ROC on 77 real Sentinel-1 events. A three-tier alert pipeline and a BRRI-calibrated boro rice damage estimator are included.

### 🤖 AI 总结

**一句话总结**：Flash floods in Bangladesh's haor wetlands show up with almost no warning. They wreck the annual boro rice harvest. Current setups, built for riverine floods, miss backwater dynamics entirely. These b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ML, HaorFloodAlert, Deseasonalized, Ensemble, 72-Hour, Flood, Prediction, Bangladesh

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20167v1) | [下载PDF](https://arxiv.org/pdf/2605.20167v1.pdf)

---

## [3. Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR](https://arxiv.org/abs/2605.20164v1)

**作者**：Utkarsh Tyagi, Xingang Guo, MohammadHossein Rezaei 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-19

### 📄 论文摘要

Reinforcement learning with verifiable rewards has made post-training highly effective when correctness can be checked automatically. However, many important model behaviors require satisfying several qualitative criteria at once. Rubric-based rewards address this setting by grading prompt-specific criteria and aggregating them into a scalar reward. Yet standard static aggregations conflate a criterion's human-assigned importance with its current usefulness as an optimization signal. We show that this assumption breaks down in rubric RL: many important criteria are already saturated or currently unreachable, while criteria that distinguish rollouts are not necessarily those with the largest human weights. We introduce POW3R, a policy-aware rubric reward framework that preserves human weights and category balance as the rubric objective while adapting criterion-level reward weights during training. POW3R uses rollout-level contrast to emphasize criteria that currently separate the policy's outputs, making the GRPO reward more informative without changing the underlying evaluation target. Across three base policies on two datasets spanning multimodal and text-only settings, POW3R wins $24$ of $30$ base-policy/metric comparisons, improving both mean rubric reward and strict completion (the fraction of prompts whose response satisfies every required rubric criterion) over vanilla GRPO with rubric rewards, and reaches the same plateau in $2.5$--$4\times$ fewer training steps. Rubric rewards should therefore distinguish what should matter in the final answer from what can teach the current policy.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning with verifiable rewards has made post-training highly effective when correctness can be checked automatically. However, many important model behaviors require satisfying several...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Not, Every, Rubric, Teaches, Equally, Policy-Aware, Rewards, RLVR

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20164v1) | [下载PDF](https://arxiv.org/pdf/2605.20164v1.pdf)

---

## [4. Using Aristotle API for AI-Assisted Theorem Proving in Lean 4: A Formalisation Case Study of the Grasshopper Problem](https://arxiv.org/abs/2605.20120v1)

**作者**：Gabriel Rongyang Lau  
**分类**：cs.AI, cs.LO  
**发布时间**：2026-05-19

### 📄 论文摘要

AI-assisted theorem proving can now generate substantial Lean developments for olympiad-level mathematics, but the evidential status of such developments depends on which declarations are actually verified. This paper reports a Lean 4 formalization case study of an Aristotle API proof attempt for the Grasshopper problem, originally posed as IMO 2009 Problem 6. The generated artifact states a generalized Lean version of the theorem, contains four verified helper lemmas for local components of a maximality and adjacent-swap exchange strategy, and leaves the main theorem grasshopper closed directly by one unresolved sorry. The verified components establish that the final partial sum equals the total sum, that an adjacent transposition can affect only the relevant intermediate partial sum, that the changed partial sum has the expected form, and that maximality at a position admitting an adjacent successor swap forces a corresponding forbidden-set membership fact. The Aristotle output summary identifies the intended remaining mathematical step as the global counting step needed to show that these membership facts produce at least n distinct forbidden values, contradicting the cardinality assumption |M| < n; the Lean source itself does not reduce the main theorem to a separately encoded counting lemma. This case study gives an inspectable example of a central limitation in AI-assisted formalization, namely that local proof search can succeed while the global combinatorial bookkeeping required for a theorem remains unresolved. The paper contributes a reproducible Lean artifact and a precise analysis of its verified and unverified proof content.

### 🤖 AI 总结

**一句话总结**：AI-assisted theorem proving can now generate substantial Lean developments for olympiad-level mathematics, but the evidential status of such developments depends on which declarations are actually ver...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：API, Aristotle, AI-Assisted, Theorem, Proving, Lean, Formalisation, Case

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20120v1) | [下载PDF](https://arxiv.org/pdf/2605.20120v1.pdf)

---

## [5. Neurosymbolic Learning for Inference-Time Argumentation](https://arxiv.org/abs/2605.20098v1)

**作者**：Gabriel Freedman, Adam Dejl, Adam Gould 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-19

### 📄 论文摘要

Claim verification is an important problem in high-stakes settings, including health and finance. When information underpinning claims is incomplete or conflicting, uncertain answers may be more appropriate than binary true or false classifications. In all cases, faithful explanations of the considerations determining the final verdict are crucial. We introduce inference-time argumentation (ITA), a trainable neurosymbolic framework for ternary claim verification in which a formal argumentation semantics giving the strength of claims is used both (i) to guide LLM training as models learn to generate arguments and assign them base scores (representing intrinsic strengths) and (ii) to compute ternary (true/false/uncertain) predictions from generated, scored arguments. As a result, at training time, argument generation and scoring can be optimised according to the quality of the induced argumentative predictions. Moreover, at inference time, the final prediction is faithful, by construction, to the arguments and scores determining the verdict, rather than being justified by a potentially unfaithful post-hoc reasoning trace as in conventional reasoning models. We finally show that, on two datasets for ternary claim verification, ITA improves upon argumentative baselines and can perform competitively against non-argumentative direct-prediction baselines, while providing verdicts that are computed deterministically from explicit, inspectable argumentative structures.

### 🤖 AI 总结

**一句话总结**：Claim verification is an important problem in high-stakes settings, including health and finance. When information underpinning claims is incomplete or conflicting, uncertain answers may be more appro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Neurosymbolic, Learning, Inference-Time, Argumentation, Claim, verification, important

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20098v1) | [下载PDF](https://arxiv.org/pdf/2605.20098v1.pdf)

---

## [6. Probing Embodied LLMs: When Higher Observation Fidelity Hurts Problem Solving](https://arxiv.org/abs/2605.20072v1)

**作者**：Oussama Zenkri, Oliver Brock  
**分类**：cs.AI, cs.RO  
**发布时间**：2026-05-19

### 📄 论文摘要

Large Language Models are increasingly proposed as cognitive components for robotic systems, yet their opaque decision processes make it difficult to explain success or failure in closed-loop embodied tasks. Following an empirical AI methodology, we study embodied LLM agents behaviorally by varying the information available to the agent and measuring the resulting changes in behavior. Using the Lockbox, a sequential mechanical puzzle with hidden interdependencies, we evaluate LLMs across RGB, RGB-D, and ground-truth symbolic observations in a physical robotic setup and use controlled simulation to probe the resulting behavior. Counterintuitively, agents perform best under raw RGB input and worst under perfect ground-truth observations. In simulation, we probe this effect by randomly flipping perceived action outcomes and find that moderate noise improves performance, peaking at a 40% flip probability with a 2.85-fold success rate increase over the noise-free baseline. Further analysis links this gain to a reduction in repetitive action loops. These findings suggest that success rates alone are insufficient for evaluating LLMs, as measured performance may reflect the interaction between perceptual errors and reasoning failures rather than robust problem solving.

### 🤖 AI 总结

**一句话总结**：Large Language Models are increasingly proposed as cognitive components for robotic systems, yet their opaque decision processes make it difficult to explain success or failure in closed-loop embodied...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Probing, Embodied, When, Higher, Observation, Fidelity, Hurts

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20072v1) | [下载PDF](https://arxiv.org/pdf/2605.20072v1.pdf)

---

## cs.CL

## [7. TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload](https://arxiv.org/abs/2605.20179v1)

**作者**：Zhiben Chen, Youpeng Zhao, Yang Sui 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-19

### 📄 论文摘要

Diffusion Large Language Models (dLLMs) have emerged as a competitive alternative to autoregressive (AR) models, offering better hardware utilization and bidirectional context through parallel block-level decoding. However, as dLLMs continue to scale up with mixture-of-experts (MoE) architectures, their deployment on resource-constrained devices remains an open challenge. Existing AR-based methods often incur either prohibitive I/O overhead or significant compute bottlenecks. In this work, we propose TIDE, a novel resource-efficient inference system that leverages the temporal stability of expert activations during the diffusion process within the block. Specifically, we leverage the temporal stability of expert activations during the diffusion process within the block and introduce an interval-based expert refresh strategy that updates the expert placement in an I/O-aware fashion. To ensure optimal performance, we formulate the inference scheduling as a mathematical programming problem, solving for the optimal interval that minimizes I/O traffic and CPU computation. Most importantly, TIDE is a lossless optimization that requires no model training, providing a "free lunch" acceleration for dLLM inference. In a single GPU-CPU system, we demonstrate that TIDE achieves up to 1.4$\times$ and 1.5$\times$ throughput improvements over prior baselines on LLaDA2.0-mini and LLaDA2.0-flash models, respectively.

### 🤖 AI 总结

**一句话总结**：Diffusion Large Language Models (dLLMs) have emerged as a competitive alternative to autoregressive (AR) models, offering better hardware utilization and bidirectional context through parallel block-l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, LLM, TIDE, Efficient, Lossless, MoE, Inference, O-aware

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20179v1) | [下载PDF](https://arxiv.org/pdf/2605.20179v1.pdf)

---

## [8. From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models](https://arxiv.org/abs/2605.20177v1)

**作者**：Juncheng Wu, Hardy Chen, Haoqin Tu 等 9 位作者  
**分类**：cs.CL, cs.CV  
**发布时间**：2026-05-19

### 📄 论文摘要

Recent advances in vision-language models (VLMs) emphasize long chain-of-thought reasoning; yet, we find that their performance on visual tasks is primarily limited by a lack of visual perception as opposed to reasoning itself. In this work, we systematically study the interplay between perception and reasoning in VLM post-training by decomposing their capabilities into three separate training stages: visual perception, visual reasoning, and textual reasoning, incorporating specialized training data. We demonstrate that visual perception (a) requires targeted optimization with specialized data; (b) serves as a fundamental scaffold that should be solidified through staged training before refining visual reasoning; and (c) is more effectively learned via RL than caption-based SFT. Our experiments across multiple VLMs demonstrate that staged training consistently improves both visual perception and reasoning performance over merged training. Notably, models trained with our approach achieve 1.5% higher reasoning accuracy with 20.8% shorter reasoning traces, suggesting that superior perception reduces the need for excessive reasoning. Furthermore, we show that this capability-based staging represents a new curriculum dimension orthogonal to traditional difficulty-based curricula, and combining both yields further additive gains. Our staged-training models achieve superior performance among open-weight VLMs, establishing advanced results on several visual math and perception (e.g., +5.2% on WeMath and +3.7% on RealWorldQA) tasks compared with the base counterpart.

### 🤖 AI 总结

**一句话总结**：Recent advances in vision-language models (VLMs) emphasize long chain-of-thought reasoning; yet, we find that their performance on visual tasks is primarily limited by a lack of visual perception as o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Seeing, Thinking, Decoupling, Perception, Reasoning, Improves, Post-Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20177v1) | [下载PDF](https://arxiv.org/pdf/2605.20177v1.pdf)

---

## [9. ClinSeekAgent: Automating Multimodal Evidence Seeking for Agentic Clinical Reasoning](https://arxiv.org/abs/2605.20176v1)

**作者**：Juncheng Wu, Letian Zhang, Yuhan Wang 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-19

### 📄 论文摘要

Large language models (LLMs) and agentic systems have shown promise for clinical decision support, but existing works largely assume that evidence has already been curated and handed to the model. Real-world clinical workflows instead require agents to actively seek, iteratively plan, and synthesize multimodal evidence from heterogeneous sources. In this paper, we introduce ClinSeekAgent, an automated agentic framework for dynamic multimodal evidence seeking that shifts the paradigm from passive evidence consumption to active evidence acquisition. Given only a clinical query and access to raw data sources, ClinSeekAgent gathers evidence by querying medical knowledge bases, navigating raw EHRs, and invoking medical imaging tools; refines its hypotheses as new information emerges; and integrates the collected evidence into grounded clinical decisions. ClinSeekAgent serves both as an inference-time agent for frontier LLMs and as a training-time pipeline for distilling high-quality agent trajectories into compact open-source models. To validate its inference-time effectiveness, we construct ClinSeek-Bench, which pairs Curated Input reasoning from fixed pre-selected evidence with Automated Evidence-Seeking over raw clinical data. On text-only EHR tasks, ClinSeekAgent improves Claude Opus 4.6 from 60.0 to 63.2 overall F1 and MiniMax M2.5 from 43.1 to 47.3, with positive risk-prediction gains in 7 out of 9 evaluated host models. On multimodal tasks, ClinSeekAgent improves Claude Opus 4.6 from 47.5 to 62.6 (+15.1); all evaluated models improve across the three CXR-related task groups. We further validate ClinSeekAgent as a training pipeline by distilling agentic evidence-seeking trajectories into ClinSeek-35B-A3B, which achieves 34.0 average F1 on existing AgentEHR-Bench, improving over its Qwen3.5-35B-A3B baseline by +11.9 points and approaching Claude Opus 4.6.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) and agentic systems have shown promise for clinical decision support, but existing works largely assume that evidence has already been curated and handed to the model. Rea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ClinSeekAgent, Automating, Multimodal, Evidence, Seeking, Agentic, Clinical, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20176v1) | [下载PDF](https://arxiv.org/pdf/2605.20176v1.pdf)

---

## [10. MixRea: Benchmarking Explicit-Implicit Reasoning in Large Language Models](https://arxiv.org/abs/2605.20128v1)

**作者**：Yuanqing Cai, Ziyi Huang, Minhao Liu 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-19

### 📄 论文摘要

Large language models (LLMs) are increasingly integrated into high-stakes decision-making. Inspired by the theory of \emph{inattentional blindness} in human cognition, we investigate whether LLMs, trained on human-preferred corpora that embed attentional biases, exhibit a similar limitation: \emph{failing to attend to subtle yet important contextual cues under explicit task instructions}. To evaluate this, we introduce the task of \textbf{explicit-implicit reasoning} and present \textbf{MixRea}, a benchmark of 2,246 multiple-choice questions across 9 reasoning types with varying distributions of explicit and implicit information. Evaluation of 21 advanced LLMs shows that even the best-performing reasoning model (Gemini 2.5 Pro) achieves only 42.8\% consistency, revealing widespread inattentional blindness. To mitigate this, we propose \textbf{Potential Relation Completion Prompting (PRCP)}, a prompting method that improves reasoning by recovering overlooked causal relations. Further analysis shows that this limitation persists across diverse multi-source reasoning tasks, highlighting the need for more cognitively aligned models.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly integrated into high-stakes decision-making. Inspired by the theory of \emph{inattentional blindness} in human cognition, we investigate whether LLMs, tra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, MixRea, Benchmarking, Explicit-Implicit, Reasoning, Large, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20128v1) | [下载PDF](https://arxiv.org/pdf/2605.20128v1.pdf)

---

## [11. ThoughtTrace: Understanding User Thoughts in Real-World LLM Interactions](https://arxiv.org/abs/2605.20087v1)

**作者**：Chuanyang Jin, Binze Li, Haopeng Xie 等 9 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-05-19

### 📄 论文摘要

Conversational AI has now reached billions of users, yet existing datasets capture only what people say, not what they think. We introduce ThoughtTrace, the first large-scale dataset that pairs real-world multi-turn human--AI conversations with users' self-reported thoughts: their reasons for sending prompts and reactions to assistant responses. ThoughtTrace comprises 1,058 users, 2,155 conversations, 17,058 turns, and 10,174 thought annotations collected across 20 language models. Our analysis shows that ThoughtTrace captures long-horizon, topically diverse interactions, and that thoughts are semantically distinct from messages, difficult for frontier LLMs to infer from context, diverse in content, and tied to conversation stages. We further demonstrate the utility of thoughts for downstream modeling. First, thoughts improve user-behavior prediction as inference-time context. Second, thought-guided rewrites provide fine-grained alignment signals for training personalized assistants. Together, ThoughtTrace establishes user thoughts as a new data modality for studying the cognitive dynamics behind human--AI interaction and provides a foundation for building assistants that better understand and adapt to users' latent goals, preferences, and needs.

### 🤖 AI 总结

**一句话总结**：Conversational AI has now reached billions of users, yet existing datasets capture only what people say, not what they think. We introduce ThoughtTrace, the first large-scale dataset that pairs real-w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, ThoughtTrace, Understanding, User, Thoughts, Real-World, Interactions, Conversational

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20087v1) | [下载PDF](https://arxiv.org/pdf/2605.20087v1.pdf)

---

## [12. BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation](https://arxiv.org/abs/2605.20084v1)

**作者**：Zijun Jia, Yuanchang Ye, Sen Jia 等 9 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-05-19

### 📄 论文摘要

Large language models (LLMs) can enhance factuality via retrieval-augmented generation (RAG), but applying RAG to every query is unnecessary when the model-only answer is reliable. This motivates cascaded RAG: each query is first handled by an LLM-only branch, escalated to a RAG fallback only if the primary branch is uncertain, and abstained from when neither branch is sufficiently trustworthy. However, calibrating such cascades stage by stage may be conservative, since the final utility depends on joint uncertainty thresholding of LLM-only and RAG. In this work, we develop BalanceRAG to certify threshold pairs at a target risk level. Given uncertainty scores from the two branches, BalanceRAG frames each threshold pair as an operating point on a two-dimensional lattice and identifies safe operating points using sequential graphical testing. This enables risk-adaptive threshold calibration, controlling the system-level error rate among accepted points, while retaining more examples. Furthermore, BalanceRAG extends to multi-risk calibration, allowing retrieval usage to be bounded together with the selection-conditioned risk. Experiments on three open-domain question answering (QA) benchmarks across multiple LLM backbones demonstrate that BalanceRAG meets prescribed risk levels, preserves higher coverage and more accepted correct examples, and reduces unnecessary retrieval calls compared with always-on RAG.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) can enhance factuality via retrieval-augmented generation (RAG), but applying RAG to every query is unnecessary when the model-only answer is reliable. This motivates casc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BalanceRAG, Joint, Risk, Calibration, Cascaded, Retrieval-Augmented, Generation, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20084v1) | [下载PDF](https://arxiv.org/pdf/2605.20084v1.pdf)

---

## cs.CV

## [13. MSAVBench: Towards Comprehensive and Reliable Evaluation of Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2605.20183v1)

**作者**：Yujie Wei, Yujin Han, Zhekai Chen 等 23 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-19

### 📄 论文摘要

Video generation is rapidly evolving from single-shot synthesis to complex multi-shot audio-video (MSAV) narratives to meet real-world demands. However, evaluating such frontier models remains a fundamental challenge. Existing benchmarks are limited in scope and data diversity, and rely on rigid evaluation pipelines, preventing systematic and reliable assessment of modern MSAV models. To bridge these gaps, we introduce MSAVBench, the first comprehensive benchmark and adaptive hybrid evaluation framework for multi-shot audio-video generation. Our benchmark spans four key dimensions, video, audio, shot, and reference, covering diverse task settings, varying shot counts of up to 15, and challenging non-realistic scenarios. Our evaluation framework improves robustness through an adaptive self-correction mechanism for shot segmentation, instance-wise rubrics for subjective metrics, and tool-grounded evidence extraction for complex judgments. Furthermore, MSAVBench achieves high alignment with human judgments, reaching a Spearman rank correlation of 91.5%. Our systematic evaluation of 19 state-of-the-art closed- and open-source models shows that current systems still struggle with director-level control and fine-grained audio-visual synchronization, while modular or agentic generation pipelines offer a promising path toward narrowing the gap between open- and closed-source models. We will release the benchmark data and evaluation code to facilitate future research.

### 🤖 AI 总结

**一句话总结**：Video generation is rapidly evolving from single-shot synthesis to complex multi-shot audio-video (MSAV) narratives to meet real-world demands. However, evaluating such frontier models remains a funda...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, MSAVBench, Towards, Comprehensive, Reliable, Evaluation, Multi-Shot, Audio-Video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20183v1) | [下载PDF](https://arxiv.org/pdf/2605.20183v1.pdf)

---

## [14. Multi-axis Analysis of Image Manipulation Localization](https://arxiv.org/abs/2605.20174v1)

**作者**：Keanu Nichols, Divya Appapogu, Giscard Biamby 等 6 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-05-19

### 📄 论文摘要

Advanced image editing software enables easy creation of highly convincing image manipulations, which has been made even more accessible in recent years due to advances in generative AI. Manipulated images, while often harmless, could spread misinformation, create false narratives, and influence people's opinions on important issues. Despite this growing threat, there is limited research on detecting advanced manipulations across different visual domains. Thus, we introduce Analysis Under Domain-shifts, qualIty, Type, and Size (AUDITS), a comprehensive benchmark designed for studying axes of analysis in image manipulation detection. AUDITS comprises over 530K images from two distinct sources (user and news photos). We curate our dataset to support analysis across multiple axes using recent diffusion-based inpaintings, spanning a diverse range of manipulation types and sizes. We conduct experiments under different types of domain shift to evaluate robustness of existing image manipulation detection methods. Our goal is to drive further research in this area by offering new insights that would help develop more reliable and generalizable image manipulation detection methods.

### 🤖 AI 总结

**一句话总结**：Advanced image editing software enables easy creation of highly convincing image manipulations, which has been made even more accessible in recent years due to advances in generative AI. Manipulated i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Multi-axis, Analysis, Image, Manipulation, Localization, Advanced, editing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20174v1) | [下载PDF](https://arxiv.org/pdf/2605.20174v1.pdf)

---

## [15. CaMo: Camera Motion Grounded Evaluation and Training for Vision-Language Models](https://arxiv.org/abs/2605.20165v1)

**作者**：Hsiang-Wei Huang, Junbin Lu, Kuang-Ming Chen 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-19

### 📄 论文摘要

Vision-Language Models (VLMs) achieve strong performance on spatial question answering benchmarks, yet it remains unclear whether such gains reflect genuine spatial intelligence. We show that existing spatial VLMs lack basic camera motion understanding, a key component of spatial cognition. We propose the Spatial Narrative Score (SNS), an evaluation framework that requires VLMs to generate explicit spatial narratives capturing both scene semantics and camera motion, followed by reasoning with a frozen proxy LLM. Under SNS, state-of-the-art spatial VLMs exhibit significant performance degradation despite high direct question answering accuracy. To address this gap, we introduce CaMo, a camera motion grounded VLM that achieves consistent performance across SNS evaluation and direct spatial question answering accuracy. Our results highlight the importance of explicit spatial narrative externalization for evaluating VLMs with transferable 3D spatial understanding. Our code, data, and model is available at https://github.com/hsiangwei0903/CaMo

### 🤖 AI 总结

**一句话总结**：Vision-Language Models (VLMs) achieve strong performance on spatial question answering benchmarks, yet it remains unclear whether such gains reflect genuine spatial intelligence. We show that existing...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CaMo, Camera, Motion, Grounded, Evaluation, Training, Vision-Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20165v1) | [下载PDF](https://arxiv.org/pdf/2605.20165v1.pdf)

---

## [16. Interpretable Computer Vision for Defect Detection in X-ray Tomography of Aerospace SiC/SiC Composites](https://arxiv.org/abs/2605.20159v1)

**作者**：Antonio Peña Corredor, Julien Lesseur, Romain Nunez 等 5 位作者  
**分类**：cs.CV, cond-mat.mtrl-sci, cs.LG  
**发布时间**：2026-05-19

### 📄 论文摘要

Non-destructive testing of aerospace SiC/SiC composites via X-ray computed tomography (XCT) relies on expert visual assessment, with current workflows offering limited traceability for accept/reject decisions. Deep convolutional networks can automate defect detection, yet their black-box nature conflicts with the transparency that industrial inspection practice demands. To close this gap, we introduce p-ResNet-50, a convolutional framework extended with a prototype layer that couples high detection accuracy with case-based explanations. Six learned prototypes are explicitly aligned with expert-defined semantic categories-healthy matrix, matrix--air interfaces, pores, line-like defects, and mixed morphologies-so that every classification is traceable to a physically meaningful reference. Two novel regularisation terms, anchor-based and medoid-based, tether prototypes to expert-selected patches and prevent prototype collapse, addressing a known limitation of prototype networks. Latent-space analysis via UMAP delineates semantically coherent sub-domains and maps zones of uncertainty where misclassifications concentrate, giving inspectors an explicit picture of where the model is-and is not-reliable. The framework is validated on an XCT patch dataset of approximately 12,000 patches extracted from four defect-rich SiC/SiC laboratory specimens. Taking a black-box ResNet-50 as a baseline (ROC-AUC = 0.991), the prototype extension achieves comparable performance (accuracy 0.957 vs. 0.959; ROC-AUC 0.994 vs. 0.993) while trading a slight reduction in sensitivity for higher precision and specificity. Each decision is backed by representative evidence patches, and the model explicitly flags its uncertainty regions. Beyond defect mapping, the framework establishes a reusable methodology for embedding domain-expert knowledge into prototype networks, applicable to other XCT inspection scenarios requiring traceable, auditable decisions.

### 🤖 AI 总结

**一句话总结**：Non-destructive testing of aerospace SiC/SiC composites via X-ray computed tomography (XCT) relies on expert visual assessment, with current workflows offering limited traceability for accept/reject d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Interpretable, Computer, Vision, Defect, Detection, X-ray, Tomography

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20159v1) | [下载PDF](https://arxiv.org/pdf/2605.20159v1.pdf)

---

## [17. TideGS: Scalable Training of Over One Billion 3D Gaussian Splatting Primitives via Out-of-Core Optimization](https://arxiv.org/abs/2605.20150v1)

**作者**：Chonghao Zhong, Linfeng Shi, Hua Chen 等 7 位作者  
**分类**：cs.CV, cs.PF  
**发布时间**：2026-05-19

### 📄 论文摘要

Training 3D Gaussian Splatting (3DGS) at billion-primitive scale is fundamentally memory-bound: each Gaussian primitive carries a large attribute vector, and the aggregate parameter table quickly exceeds GPU capacity, limiting prior systems to tens of millions of Gaussians on commodity single-GPU hardware. We observe that 3DGS training is inherently sparse and trajectory-conditioned: each iteration activates only the Gaussians visible from the current camera batch, so GPU memory can serve as a working-set cache rather than a persistent parameter store. Building on this insight, we introduce TideGS, an out-of-core training framework that manages parameters across an SSD-CPU-GPU hierarchy via three synergistic techniques: block-virtualized geometry for SSD-aligned spatial locality, a hierarchical asynchronous pipeline to overlap I/O with computation, and trajectory-adaptive differential streaming that transfers only incremental working-set deltas between iterations. Experiments show that TideGS enables training with over one billion Gaussians on a single 24 GB GPU while achieving the best reconstruction quality among evaluated single-GPU baselines on large-scale scenes, scaling beyond prior out-of-core baselines (e.g., approximately 100M Gaussians) and standard in-memory training (e.g., approximately 11M Gaussians).

### 🤖 AI 总结

**一句话总结**：Training 3D Gaussian Splatting (3DGS) at billion-primitive scale is fundamentally memory-bound: each Gaussian primitive carries a large attribute vector, and the aggregate parameter table quickly exce...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, 3D, TideGS, Scalable, Training, Over, One, Billion

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20150v1) | [下载PDF](https://arxiv.org/pdf/2605.20150v1.pdf)

---

## [18. PixVerve: Advancing Native UHR Image Generation to 100MP with a Large-Scale High-Quality Dataset](https://arxiv.org/abs/2605.20147v1)

**作者**：Haojun Chen, Haoyang He, Chengming Xu 等 14 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-19

### 📄 论文摘要

Text-to-Image (T2I) models have recently seen notable progress around 1K and 2K resolution. With the extreme desire for better visual experience and the rapid development of imaging technology, the demand for Ultra-High-Resolution (UHR) image generation has grown significantly. However, UHR image generation poses great challenges due to the scarcity and complexity of high-resolution content. In this paper, we first introduce PixVerve-95K, a high-quality, open-source UHR T2I dataset curated with a carefully designed data pipeline, which contains 95K images across diverse scenarios (each image has a minimum pixel-count of 100M) and seven-dimensional annotations. Based on our large-scale image-text dataset, we take a pioneering step to extend various T2I foundation models to native 100MP generation with three training schemes. Finally, leveraging both conventional metrics and multimodal large language model-based assessments, our proposed PixVerve-Bench benchmark establishes a comprehensive evaluation protocol for UHR images encompassing visual quality and semantic alignment. Extensive experimental results on our benchmark and the constructive exploration of training strategies collaboratively provide valuable insights for future breakthroughs.

### 🤖 AI 总结

**一句话总结**：Text-to-Image (T2I) models have recently seen notable progress around 1K and 2K resolution. With the extreme desire for better visual experience and the rapid development of imaging technology, the de...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：100MP, PixVerve, Advancing, Native, UHR, Image, Generation, Large-Scale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20147v1) | [下载PDF](https://arxiv.org/pdf/2605.20147v1.pdf)

---

## [19. MetaEarth-MM: Unified Multimodal Remote Sensing Image Generation with Scene-centered Joint Modeling](https://arxiv.org/abs/2605.20090v1)

**作者**：Zhiping Yu, Chenyang Liu, Jinqi Cao 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-19

### 📄 论文摘要

Multi-modal remote sensing images are vital for Earth observation, yet complete paired observations are often scarce in practice. Existing generative methods commonly address this problem through isolated pairwise modality translation, but their versatility and scalability remain limited as the number of modalities and generation tasks increases. Here, we develop a generative foundation model MetaEarth-MM for multi-modal remote sensing imagery, enabling paired joint generation and any-to-any translation across five modalities within a unified model. Recognizing the intrinsic scene consistency underlying multi-modal observations, we introduce a scene-centered joint modeling paradigm in MetaEarth-MM. Unlike previous methods that rely on direct appearance-level cross-modal mapping, our model organizes the generation around the underlying scene content. Specifically, MetaEarth-MM adopts a decoupled architecture that first infers a latent scene representation from available observations, and then generates target modalities conditioned on this intermediate state. To support training, we further construct EarthMM, a large-scale dataset comprising 2.8 million multi-resolution global images with 2.2 million aligned pairs. Extensive experiments demonstrate that MetaEarth-MM not only exhibits strong generative capability and robust generalization across diverse generation tasks, but also supports downstream tasks at both data and representation levels, highlighting its potential as a general foundation model for cross-modal Earth observation. The code and dataset will be available at https://github.com/YZPioneer/MetaEarth-MM.

### 🤖 AI 总结

**一句话总结**：Multi-modal remote sensing images are vital for Earth observation, yet complete paired observations are often scarce in practice. Existing generative methods commonly address this problem through isol...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MetaEarth-MM, Unified, Multimodal, Remote, Sensing, Image, Generation, Scene-centered

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20090v1) | [下载PDF](https://arxiv.org/pdf/2605.20090v1.pdf)

---

## [20. Spatially Prompted Visual Trajectory Prediction for Egocentric Manipulation](https://arxiv.org/abs/2605.20085v1)

**作者**：Yifan Li, Xinyu Zhou, Yunhao Ge 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-19

### 📄 论文摘要

Robotic manipulation is often specified through language instructions or task identifiers, yet cluttered environments with similar objects are better handled by spatially indicating what to move and where to place it. Addressing the vision-centric challenge of object and goal specification, we present, to the best of our knowledge, the first formalization of Spatially Prompted Visual Trajectory Prediction (SP-VTP). This novel setting utilizes initial spatial prompts (like bounding boxes or points) to define task objectives, tasking the model with forecasting future end-effector trajectories from egocentric streams. To study this problem, we collect and annotate EgoSPT, a dataset of egocentric spatially prompted manipulation trajectories with first-frame object and target grounding annotations and recovered 3D end-effector motion. SP-VTP is challenging because the task specification is static, while the scene configuration evolves over time. To solve this problem, we propose SPOT(Spatially Prompted Object-Target Policy), which combines a task encoder for first-frame visual and coordinate spatial prompts, an observation encoder for current visual and history context, and a trajectory generator for future end-effector motion. Experiments under strict scene-level splits show that SPOT improves cross-scene trajectory prediction over non-prompted or single-source prompted baselines. Together, EgoSPT and SPOT establish a new spatial prompting problem SP-VTP, as a simple and scalable task condition for egocentric manipulation.

### 🤖 AI 总结

**一句话总结**：Robotic manipulation is often specified through language instructions or task identifiers, yet cluttered environments with similar objects are better handled by spatially indicating what to move and w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Spatially, Prompted, Visual, Trajectory, Prediction, Egocentric, Manipulation, Robotic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20085v1) | [下载PDF](https://arxiv.org/pdf/2605.20085v1.pdf)

---

## [21. VL-DPO: Vision-Language-Guided Finetuning for Preference-Aligned Autonomous Driving](https://arxiv.org/abs/2605.20082v1)

**作者**：Zhefan Xu, Ghassen Jerfel, Marina Haliem 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-19

### 📄 论文摘要

The rapid growth of autonomous driving datasets has enabled the scaling of powerful motion forecasting models. While large-scale pretraining provides strong performance, the standard imitation objective may not fully capture the complex nuances of human driving preferences. Meanwhile, recent advances in vision-language models (VLMs) have demonstrated impressive reasoning and commonsense understanding. Building on these capabilities, this paper presents VL-DPO, a vision-language-guided framework that aligns ego-vehicle motion forecasting models with human preferences. Our approach leverages a VLM as a zero-shot reasoner to automatically generate preference pairs from a pretrained model's rollouts, which are then used to finetune the model via Direct Preference Optimization (DPO). We finetune our models on the Waymo Open End-to-End Driving Dataset (WOD-E2E) and evaluate performance against held-out human preference annotations using rater feedback score (RFS) and average displacement error (ADE). Our experiments confirm that the VLM's trajectory selection is a high-quality proxy for human preference. Our final model, VL-DPO, yields an 11.94% increase in RFS and a 10.01% reduction in ADE over the pretrained model.

### 🤖 AI 总结

**一句话总结**：The rapid growth of autonomous driving datasets has enabled the scaling of powerful motion forecasting models. While large-scale pretraining provides strong performance, the standard imitation objecti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VL-DPO, Vision-Language-Guided, Finetuning, Preference-Aligned, Autonomous, Driving, rapid, growth

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20082v1) | [下载PDF](https://arxiv.org/pdf/2605.20082v1.pdf)

---

## [22. Probability-Conserving Flow Guidance](https://arxiv.org/abs/2605.20079v1)

**作者**：Parsa Esmati, Junha Hyung, Amirhossein Dadashzadeh 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.LG, eess.IV  
**发布时间**：2026-05-19

### 📄 论文摘要

Diffusion and flow-based generative models dominate visual synthesis, with guidance aligning samples to user input and improving perceptual quality. However, Classifier-Free Guidance (CFG) and extrapolation-based methods are heuristic linear combinations of velocities/scores that ignore the generative manifold geometry, breaking probability conservation and driving samples off the learned manifold under strong guidance. We analyse guidance through the continuity equation and show its effect decomposes into a divergence term and a score-parallel term defined invariantly across parameterisations. We prove the divergence term blows up structurally as sampling approaches the data manifold, motivating a time-dependent schedule alongside score-parallel attenuation. The resulting plug-and-play rule, Adaptive Manifold Guidance (AdaMaG), bounds both terms at no additional inference cost. Finally, we show that most empirical heuristics for reducing saturation or improving generation quality correspond directly to the two terms in our decomposition. Across image generation benchmarks, AdaMaG improves realism, reduces hallucinations, and induces controlled desaturation in high-guidance regimes.

### 🤖 AI 总结

**一句话总结**：Diffusion and flow-based generative models dominate visual synthesis, with guidance aligning samples to user input and improving perceptual quality. However, Classifier-Free Guidance (CFG) and extrapo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Probability-Conserving, Flow, Guidance, flow-based, generative, models, dominate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20079v1) | [下载PDF](https://arxiv.org/pdf/2605.20079v1.pdf)

---

## [23. X-Ray cardiac angiographic vessel segmentation based on pixel classification using machine learning and region growing](https://arxiv.org/abs/2605.20073v1)

**作者**：E O Rodrigues, L O Rodrigues, J J Lima 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-19

### 📄 论文摘要

This work proposes a pixel-classification approach for vessel segmentation in x-ray angiograms. The proposal uses textural features such as anisotropic diffusion, features based on the Hessian matrix, mathematical morphology and statistics. These features are extracted from the neighborhood of each pixel. The approach also uses the ELEMENT methodology, which consists of creating a pixel-classification controlled by region-growing where the result of the classification affects further classifications of pixels. The Random Forests classifier is used to predict whether the pixel belongs to the vessel structure. The approach achieved the best accuracy in the literature (95.48%) outperforming unsupervised state-of-the-art approaches.

### 🤖 AI 总结

**一句话总结**：This work proposes a pixel-classification approach for vessel segmentation in x-ray angiograms. The proposal uses textural features such as anisotropic diffusion, features based on the Hessian matrix,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：X-Ray, cardiac, angiographic, vessel, segmentation, pixel, classification, machine

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20073v1) | [下载PDF](https://arxiv.org/pdf/2605.20073v1.pdf)

---

## [24. Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network](https://arxiv.org/abs/2605.20064v1)

**作者**：Guilherme Santos da Silva, Dalcimar Casanova, Jefferson Tales Oliva 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-19

### 📄 论文摘要

In recent years, research has highlighted the association between increased adipose tissue surrounding the human heart and elevated susceptibility to cardiovascular diseases such as atrial fibrillation and coronary heart disease. However, the manual segmentation of these fat deposits has not been widely implemented in clinical practice due to the substantial workload it entails for medical professionals and the associated costs. Consequently, the demand for more precise and time-efficient quantitative analysis has driven the emergence of novel computational methods for fat segmentation. This study presents a novel deep learning-based methodology that offers autonomous segmentation and quantification of two distinct types of cardiac fat deposits. The proposed approach leverages the pix2pix network, a generative conditional adversarial network primarily designed for image-to-image translation tasks. By applying this network architecture, we aim to investigate its efficacy in tackling the specific challenge of cardiac fat segmentation, despite not being originally tailored for this purpose. The two types of fat deposits of interest in this study are referred to as epicardial and mediastinal fats, which are spatially separated by the pericardium. The experimental results demonstrated an average accuracy of 99.08% and f1-score 98.73 for the segmentation of the epicardial fat and 97.90% of accuracy and f1-score of 98.40 for the mediastinal fat. These findings represent the high precision and overlap agreement achieved by the proposed methodology. In comparison to existing studies, our approach exhibited superior performance in terms of f1-score and run time, enabling the images to be segmented in real time.

### 🤖 AI 总结

**一句话总结**：In recent years, research has highlighted the association between increased adipose tissue surrounding the human heart and elevated susceptibility to cardiovascular diseases such as atrial fibrillatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Cardiac, fat, segmentation, computed, tomography, image-to-image, conditional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20064v1) | [下载PDF](https://arxiv.org/pdf/2605.20064v1.pdf)

---

## cs.LG

## [25. SAGE: Scalable Automatic Gating Ensemble for Confident Negative Harvesting in Fraud Detection](https://arxiv.org/abs/2605.20157v1)

**作者**：Sudheer Tubati, Amit Goyal  
**分类**：cs.LG, cs.CR, cs.IR  
**发布时间**：2026-05-19

### 📄 论文摘要

Music streaming fraud, where bad actors artificially inflate stream counts to manipulate chart rankings and royalty payments, poses a significant threat to streaming services and legitimate content creators. Traditional fraud detection approaches struggle with a critical challenge: many legitimate edge cases, including super-fans and sleep-music sessions, exhibit activity patterns that closely mimic those of coordinated fraud. We present SAGE, a novel counterfactual-aware negative harvesting approach that combines SimHash-based stratified sampling with a modular gating ensemble for confident negative identification from unlabeled data. Our ensemble architecture employs pluggable statistical gates (currently instantiated with Mahalanobis distance and k-NN density) with configurable voting thresholds enabling adaptive precision-recall trade-offs. This addresses the representation bias problem in Positive-Unlabeled learning by ensuring comprehensive coverage of rare behavioral cohorts through floor-constrained sampling. Evaluation demonstrates strong precision and recall on held-out data. The approach generalizes across fraud detection domains, achieving strong performance on both customer-level and artist-level fraud without modification to the core methodology.

### 🤖 AI 总结

**一句话总结**：Music streaming fraud, where bad actors artificially inflate stream counts to manipulate chart rankings and royalty payments, poses a significant threat to streaming services and legitimate content cr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SAGE, Scalable, Automatic, Gating, Ensemble, Confident, Negative, Harvesting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20157v1) | [下载PDF](https://arxiv.org/pdf/2605.20157v1.pdf)

---

## [26. When Does Model Collapse Occur in Structured Interactive Learning?](https://arxiv.org/abs/2605.20151v1)

**作者**：Yuchen Wu, Kangjie Zhou, Weijie Su  
**分类**：cs.LG, math.ST  
**发布时间**：2026-05-19

### 📄 论文摘要

The proliferation of generative artificial intelligence has given rise to an interactive learning environment, where model parameters are continuously updated using not only data generated by natural processes, but also synthetic outputs produced by other models. This paradigm introduces two major challenges: (1) training data are no longer drawn exclusively from the target population, undermining a core assumption of classical statistical learning, and (2) model training processes become inherently correlated, as models interact with one another through repeated exposure to each other's synthetic outputs in a potentially complex manner. Establishing reliable statistical inference in such structured interactive learning environments therefore remains an important open problem. In particular, there is growing concern about model collapse, a phenomenon in which the performance of generative models progressively degrades as they are trained on synthetic data produced by earlier model generations.   Prior work on model collapse primarily focuses on a single model trained on its own output, failing to capture model performance in multi-model interactive settings. In this work, we fill this gap by investigating the performance of generative models in an interactive learning environment with general interaction patterns. In particular, we formalize model interactions using directed graphs and show that the occurrence of model collapse depends critically on the topology of the interaction graph. We further derive an explicit necessary and sufficient condition characterizing when model collapse occurs, and establish finite-sample results for linear regression and asymptotic guarantees for general M-estimators. We support our theoretical findings through extensive numerical experiments.

### 🤖 AI 总结

**一句话总结**：The proliferation of generative artificial intelligence has given rise to an interactive learning environment, where model parameters are continuously updated using not only data generated by natural ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Does, Model, Collapse, Occur, Structured, Interactive, Learning?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20151v1) | [下载PDF](https://arxiv.org/pdf/2605.20151v1.pdf)

---

## [27. Toto 2.0: Time Series Forecasting Enters the Scaling Era](https://arxiv.org/abs/2605.20119v1)

**作者**：Emaad Khwaja, Chris Lettieri, Gerald Woo 等 13 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-19

### 📄 论文摘要

We show that time series foundation models scale: a single training recipe produces reliable forecast-quality improvements from 4M to 2.5B parameters. We release Toto 2.0, a family of five open-weights forecasting models trained under this recipe. The Toto 2.0 family sets a new state of the art on three forecasting benchmarks: BOOM, our observability benchmark; GIFT-Eval, the standard general-purpose benchmark; and the recent contamination-resistant TIME benchmark. This report describes our experimental results and details the design decisions behind Toto 2.0: its architecture and training recipe, training data, and the u-muP hyperparameter transfer pipeline. All five base checkpoints are released under Apache 2.0.

### 🤖 AI 总结

**一句话总结**：We show that time series foundation models scale: a single training recipe produces reliable forecast-quality improvements from 4M to 2.5B parameters. We release Toto 2.0, a family of five open-weight...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Toto, Time, Series, Forecasting, Enters, Scaling, Era

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20119v1) | [下载PDF](https://arxiv.org/pdf/2605.20119v1.pdf)

---

## [28. Optimal Representation Size: High-Dimensional Analysis of Pretraining and Linear Probing](https://arxiv.org/abs/2605.20105v1)

**作者**：Valentina Njaradi, Clémentine Dominé, Rachel Swanson 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-19

### 📄 论文摘要

Learning to generalise from limited data is a fundamental challenge for both artificial and biological systems. A common strategy is to extract reusable structure from abundant unlabelled data, enabling efficient adaptation to new tasks from limited labelled data. This two-stage paradigm is now standard in modern training pipelines, where pretraining is followed by fine-tuning or linear probing. We provide an analytical model of this process: structure extraction is formalized as principal component analysis on unlabelled data, and downstream learning as linear regression on a separate labelled dataset. In the high-dimensional regime, we derive exact expressions for training and generalisation error showcasing their dependence on representation dimensionality, unlabelled and labelled sample sizes, and task alignment. Our results show that pretrained representations strongly influence downstream generalisation, and we characterize the optimal representation size as a function of task parameters: with abundant pretraining data but scarce downstream data, maximally compressed representations are optimal, whereas with limited pretraining data, higher-dimensional representations generalise better. Furthermore, we establish an exact trade-off between pretraining and supervision, quantifying how much unlabelled data is required to replace a single labelled sample. Beyond our idealised model, we observe similar phenomenology in autoencoders and pretrained LLMs. Altogether, we highlight that optimising representation size is critical, giving conditions for when compression during pretraining improves generalisation.

### 🤖 AI 总结

**一句话总结**：Learning to generalise from limited data is a fundamental challenge for both artificial and biological systems. A common strategy is to extract reusable structure from abundant unlabelled data, enabli...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Optimal, Representation, Size, High-Dimensional, Analysis, Pretraining, Linear

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20105v1) | [下载PDF](https://arxiv.org/pdf/2605.20105v1.pdf)

---

## [29. Towards Distillation Guarantees under Algorithmic Alignment for Combinatorial Optimization](https://arxiv.org/abs/2605.20074v1)

**作者**：Thien Le, Melanie Weber  
**分类**：cs.LG  
**发布时间**：2026-05-19

### 📄 论文摘要

Distillation transfers knowledge from a large model trained on broad data to a smaller, more efficient model suitable for deployment. In structured prediction settings, prior knowledge about the task can guide the choice of a target architecture that is algorithmically aligned with the underlying problem. Building on recent learning-theoretic analyses of decision-tree (DT) distillation (Boix-Adsera, 2024), we study when distillation succeeds for combinatorial optimization tasks. We focus on the case where the target model is a graph neural network whose architecture is aligned with a dynamic programming (DP) algorithm for the task. Assuming that the source model is sufficiently rich, formalized through the linear representation hypothesis (LRH) (Elhage et al., 2022; Park et al., 2024), we show that the distillation problem can be solved efficiently in the complexity parameters of the DP transition function, represented as a DT. Our results provide a rigorous sufficient condition for successful distillation in the flavour of algorithmic alignment.

### 🤖 AI 总结

**一句话总结**：Distillation transfers knowledge from a large model trained on broad data to a smaller, more efficient model suitable for deployment. In structured prediction settings, prior knowledge about the task ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Towards, Distillation, Guarantees, under, Algorithmic, Alignment, Combinatorial, Optimization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20074v1) | [下载PDF](https://arxiv.org/pdf/2605.20074v1.pdf)

---

## [30. Smooth Partial Lotteries for Stable Randomized Selection](https://arxiv.org/abs/2605.20069v1)

**作者**：Alexander Goldberg, Giulia Fanti, Nihar B. Shah  
**分类**：cs.LG, cs.GT  
**发布时间**：2026-05-19

### 📄 论文摘要

Competitive selection processes, from scientific funding to admissions and hiring, use evaluations to score candidates, and eventually choose a subset of them based on those scores. Recently, many organizations have adopted partial lotteries, which randomize selection based on evaluation scores. However, existing lottery designs are inherently unstable, as a small change to a single candidate's score can cause large shifts in their selection probabilities. This instability undermines a key goal of lotteries: reducing the influence of fine-grained score distinctions near the decision boundary. We propose smoothness as a design principle for partial lotteries, formalizing it as a Lipschitz condition on the mapping from review scores over candidates to selection probabilities. We introduce the Clipped Linear Lottery, a simple mechanism in which selection probabilities scale linearly with estimated quality between an upper threshold, above which we always accept, and a lower threshold, below which we always reject. We prove that the Clipped Linear Lottery's worst-case regret matches a lower bound for any smooth selection rule up to a factor of $(1 - k/n)$, where $k/n$ is the acceptance rate. We compare smooth selection to other stability notions like Individual Fairness and Differential Privacy, showing that the Clipped Linear Lottery achieves a better smoothness-regret tradeoff than alternatives. Experiments on real peer review data from ICLR 2025, NeurIPS 2024, and the Swiss National Science Foundation demonstrate that existing lottery designs are highly unstable in practice even under perturbations to a single score. Our experiments also confirm the tightness of our theoretical analysis and show that our proposed Clipped Linear Lottery achieves a better smoothness-utility tradeoff than alternatives in practice.

### 🤖 AI 总结

**一句话总结**：Competitive selection processes, from scientific funding to admissions and hiring, use evaluations to score candidates, and eventually choose a subset of them based on those scores. Recently, many org...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Smooth, Partial, Lotteries, Stable, Randomized, Selection, Competitive, processes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.20069v1) | [下载PDF](https://arxiv.org/pdf/2605.20069v1.pdf)

---

