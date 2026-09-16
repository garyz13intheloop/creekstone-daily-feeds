# arXiv AI 论文日报 | 2026-09-16

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.AI](#csAI) (7 篇)
- [cs.CV](#csCV) (9 篇)
- [cs.CL](#csCL) (7 篇)
- [cs.LG](#csLG) (7 篇)

---

## cs.AI

## [1. ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents](https://arxiv.org/abs/2609.17523v1)

**作者**：Shuhan Xue, Jianyuan Zhong, Ziyuan Nan 等 13 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-09-15

### 📄 论文摘要

We introduce and release ScienceBuddy, an interactive scientific research workspace that brings continually improving scientific agents into researchers' everyday workflows. ScienceBuddy supports researchers in carrying out scientific tasks while transforming their requests, feedback, and execution evidence into tasks and evaluation rubrics for continual learning. At its core is recursive-in-recursive self-improvement, a paradigm that couples harness evolution with model reinforcement learning: the inner recursion improves the harness with the model fixed, while the outer recursion trains the model under the improved harness. Harness evolution shapes training experience, and model learning creates new opportunities for harness adaptation. We present case studies of researcher interaction, harness refinement, and model learning, with the benchmark cases spanning four scientific task families. By releasing ScienceBuddy as a research product, we make this paradigm available to the scientific community and take a step toward discovery intelligence: scientific AI that advances through sustained collaboration with researchers and evolves alongside the research it supports. Website: http://science-buddy.io

### 🤖 AI 总结

**一句话总结**：We introduce and release ScienceBuddy, an interactive scientific research workspace that brings continually improving scientific agents into researchers' everyday workflows. ScienceBuddy supports rese...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, We, ScienceBuddy, Recursive-in-Recursive, Self-Improvement, Interactive, Scientific, introduce

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17523v1) | [下载PDF](https://arxiv.org/pdf/2609.17523v1.pdf)

---

## [2. Verifiable Social Reasoning for LLM Assistants](https://arxiv.org/abs/2609.17496v1)

**作者**：Amir Taubenfeld, Zorik Gekhman, Avigail Grinstein-Dabush 等 9 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-09-15

### 📄 论文摘要

LLM assistants are widely used for daily social advice, yet evaluating their social reasoning in such consultation settings remains challenging since (i) it requires setups where the assistant learns about social situations from subjective user narratives, and (ii) social properties, such as others' intentions, typically lack verifiable ground truth. To address these challenges, we introduce Fuse, a multi-agent simulation framework for studying user-mediated social reasoning. In Fuse, a target agent with a hidden motive interacts with other agents including one representing the user, who then consults the evaluated assistant to infer the target's motive, providing verifiable ground truth by construction. Simulation faithfulness is validated through a human study with 24k annotations. We apply Fuse to 12 LLMs and demonstrate its analytical utility by systematically isolating key factors, showing that (i) user mediation compounds the inherent difficulty of social reasoning; (ii) LLMs exhibit systematic sensitivity to biased user framing; (iii) models can require more details than humans need to reach a correct prediction; and (iv) longer conversations do not always improve performance despite providing opportunities for clarifying questions. We open-source Fuse and a dataset with 21k examples.

### 🤖 AI 总结

**一句话总结**：LLM assistants are widely used for daily social advice, yet evaluating their social reasoning in such consultation settings remains challenging since (i) it requires setups where the assistant learns ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Verifiable, Social, Reasoning, Assistants, widely, used, daily

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17496v1) | [下载PDF](https://arxiv.org/pdf/2609.17496v1.pdf)

---

## [3. LimiX-2: A Contextual Mechanism Network Towards General Structured-Data Intelligence](https://arxiv.org/abs/2609.17488v1)

**作者**：Xingxuan Zhang, Gang Ren, Hao Yuan 等 60 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-15

### 📄 论文摘要

We introduce LimiX-2, a new model in the LimiX family, developed through model and data scaling guided by our previously established scaling laws. LimiX-2 adopts the Contextual Mechanism Networks (CMNs) paradigm and is pretrained with Context-Conditional Masked Modeling (CCMM). CMNs shifts the organizing principle of in-context learning from target-centric prediction to mechanism-oriented joint modeling. Rather than centering the network on the $p(y \mid x, D_{\mathrm{context}})$ objective of conventional tabular PFNs, it is designed around learning $p(x, y \mid D_{\mathrm{context}})$, a context-dependent representation of the joint structure underlying data generation. Pretraining uses synthetic datasets generated by structural causal models (SCMs) spanning diverse graph structures, functional mechanisms, and observation processes. Evaluations on TabArena, TALENT, and BCCO show that LimiX-2 outperforms current dataset-specific models and tabular foundation models. Beyond predictive performance, the CMN paradigm also promotes causal awareness in LimiX-2: its feature attention encodes direct causal relationships, enabling accurate causal skeleton recovery.

### 🤖 AI 总结

**一句话总结**：We introduce LimiX-2, a new model in the LimiX family, developed through model and data scaling guided by our previously established scaling laws. LimiX-2 adopts the Contextual Mechanism Networks (CMN...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LimiX-2, Contextual, Mechanism, Network, Towards, General, Structured-Data, Intelligence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17488v1) | [下载PDF](https://arxiv.org/pdf/2609.17488v1.pdf)

---

## [4. FlashVector: Agent for Hierarchical Model Serving Stack Optimization](https://arxiv.org/abs/2609.17391v1)

**作者**：Qi Wu, Lohan Lemire, Kai Meng 等 11 位作者  
**分类**：cs.AI, cs.PF  
**发布时间**：2026-09-15

### 📄 论文摘要

Model serving is one of the largest cost drivers in production recommender systems. Maximizing its throughput requires navigating a deeply layered hierarchy: GPU kernels, the ML framework computation graph, the model server, and on-demand feature processing -- each demanding specialized domain expertise. Such cross-layer expertise is inherently difficult to acquire, and does not scale with a workload that continuously grows and evolves, leaving significant cost efficiency gains unrealized. While recent AI agents have demonstrated human expert level efficiency in standalone GPU kernel optimization, automated tuning and optimization for the rest of the serving stack remain largely unexplored. We present FlashVector, an agentic system that optimizes performance across all layers of the model serving stack. The key contribution is an extensible framework to generalize the single kernel optimization agent paradigm to heterogeneous technical stacks, and to deliver performance improvements holistically. After deployment in Unity's Vector advertising platform, FlashVector achieved up to 2x throughput increase and up to 1.98x latency speedup on model server, and up to 1.6x throughput increase on feature store. These optimizations were discovered not only at the GPU kernel and computation graph levels, but also across the other components of the model serving stack, such as the model server (NVIDIA Triton's C++ codebase) and the on-demand feature transformation service (Python codebase), demonstrating the extensibility of the framework to more complex system architectures.

### 🤖 AI 总结

**一句话总结**：Model serving is one of the largest cost drivers in production recommender systems. Maximizing its throughput requires navigating a deeply layered hierarchy: GPU kernels, the ML framework computation ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, FlashVector, Hierarchical, Model, Serving, Stack, Optimization, one

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17391v1) | [下载PDF](https://arxiv.org/pdf/2609.17391v1.pdf)

---

## [5. Self-Emergence Agent Architecture:Behavior-Inertia HMM, Reflexive Metacognition,and Social-Contrastive Self-Modeling](https://arxiv.org/abs/2609.17331v1)

**作者**：Xiaoyang Liu  
**分类**：cs.AI  
**发布时间**：2026-09-15

### 📄 论文摘要

Large language model (LLM) agents exhibit strong language-generation and problem-solving capabilities, yet suffer from three structural limitations: personality drift, non-evolutionary reflection, and the absence of a self-other boundary. Existing generative-agent simulations rely on static memory and fixed prompts, maintaining neither behavioral inertia nor endogenous self-evolution. We propose the Self-Emergence Agent Architecture (SEAA), which integrates three components: (i) a Hidden Markov Model (HMM) that encodes long-term behavioral and cognitive inertia as an editable state-transition matrix; (ii) a Reflexion-style verbal metacognition loop whose output updates the HMM parameters themselves, rather than merely being stored as text; and (iii) a multi-agent social environment in which initially identical agents continuously compare their behavior with others'. The three components form a closed loop: social action $\to$ feedback $\to$ self-reflection $\to$ inertia update $\to$ differentiated action. We state three falsifiable hypotheses and provide a reproducible experimental protocol with operational metrics. A language-model-free prototype shows the loop spontaneously breaks symmetry: initially identical agents consolidate distinct, stable personalities whereas matched controls do not. Experiments with a hosted LLM surface these differences as distinct first-person self-narratives, and a five-agent deliberation spontaneously develops social structure---a consensus hub and a unanimously rejected outlier---absent in the control. Following an epistemologically agnostic stance inspired by Zhuangzi, SEAA studies only observable behavioral emergence and makes no claim about subjective qualia. This work contributes a unified framework, a concrete architecture with pseudocode, mechanistic evidence, and a microscope-style sandbox for studying artificial-self emergence.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM) agents exhibit strong language-generation and problem-solving capabilities, yet suffer from three structural limitations: personality drift, non-evolutionary reflection, and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Self-Emergence, Architecture, Behavior-Inertia, HMM, Reflexive, Metacognition, Social-Contrastive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17331v1) | [下载PDF](https://arxiv.org/pdf/2609.17331v1.pdf)

---

## [6. From Transient Prompts to Persistent Control: Scientific Poster Generation via Recursive Semantic-Geometric Contracts](https://arxiv.org/abs/2609.17326v1)

**作者**：Runze Li, Yukun Zhao, Can Xu 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-15

### 📄 论文摘要

Scientific poster generation distills a multimodal paper into a single-page visual artifact, forcing strict trade-offs between informational coverage and readability under a fixed spatial budget. Existing methods pass plans as transient prompts and validate individual stages in isolation. This strategy causes requirements to drift across content and layout modules, and previous checks to be silently invalidated. We introduce PosterVisor, a control framework that shifts poster generation from transient prompts to persistent control. An Orchestrator grounds rubrics in the paper and visual assets, compiling them into a Semantic-Geometric Contract (SGC) that binds claims and sources to required visuals, budgets, and spatial commitments. Only fully instantiated records become executable assertions; other usable requirements remain soft guidance. Recursive Contract Enforcement (RCE) dynamically triggers checks across stages as evidence emerges. Crucially, during repairs, RCE rechecks affected checkpoint states, preventing repair-induced regressions from propagating silently. We instantiate PosterVisor in HTML/CSS and editable PPTX generators. On the 100-paper Paper2Poster benchmark, PosterVisor-PPT improves observed mean poster-grounded QA accuracy over PosterGen (64.47% vs. 58.53%) and is preferred by human judges in 72.5% of non-tied pairwise comparisons (95% CI, 61.6-83.4%). A secondary 30-paper study also yields higher VLM Overall and PaperQuiz means. These results support rubric-compiled contracts and stage-conditioned enforcement for controllable poster synthesis.

### 🤖 AI 总结

**一句话总结**：Scientific poster generation distills a multimodal paper into a single-page visual artifact, forcing strict trade-offs between informational coverage and readability under a fixed spatial budget. Exis...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Transient, Prompts, Persistent, Control, Scientific, Poster, Generation, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17326v1) | [下载PDF](https://arxiv.org/pdf/2609.17326v1.pdf)

---

## [7. Intrinsic Motivation in Reinforcement Learning: A Research Agenda for Adaptive Self-Organisation](https://arxiv.org/abs/2609.17325v1)

**作者**：Anatoly Belikov  
**分类**：cs.AI  
**发布时间**：2026-09-15

### 📄 论文摘要

Biological cells can be viewed as individual, interacting agents whose collective dynamics give rise to adaptive behaviour at multiple levels of organisation, from individual cells through tissues to whole multicellular organisms. In this perspective and tutorial article we discuss whether intrinsic rewards in artificial neural systems can support adaptation, functional specialisation and higher-level self-organisation without a shared external objective. We review empowerment, curiosity, learning progress, information gain, unsupervised skill discovery, mutual information estimation and the use of world models for intrinsic reward computation. Particular attention is given to failure modes showing when such objectives do not produce sustained exploration or increasingly complex behaviour. We argue that more capable systems may require complementary objectives, communication, memory, learning at multiple temporal scales and environmental constraints. Based on this perspective, we outline three experimental directions. These include a resource-constrained environment in which otherwise stable behavioural attractors become unsustainable, allowing us to test whether environmental constraints can mitigate characteristic failure modes of intrinsic objectives. The network of recurrent agents with per-agent intrinsic rewards, and a hierarchical world-model agent in which exploratory motor competence develops before goal-directed behaviour. These experiments are intended to test whether intrinsic learning can lead to adaptive organisation at progressively higher levels.

### 🤖 AI 总结

**一句话总结**：Biological cells can be viewed as individual, interacting agents whose collective dynamics give rise to adaptive behaviour at multiple levels of organisation, from individual cells through tissues to ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Intrinsic, Motivation, Reinforcement, Learning, Research, Agenda, Adaptive, Self-Organisation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17325v1) | [下载PDF](https://arxiv.org/pdf/2609.17325v1.pdf)

---

## cs.CL

## [8. When Should LLMs Abstain? Chain-of-Self-Questioning for Selective Risk Control](https://arxiv.org/abs/2609.17516v1)

**作者**：Ali Şenol  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-15

### 📄 论文摘要

Large language models can produce fluent answers when their factual support is weak. This paper introduces Chain-of-Self-Questioning (CoSQ), a prompt-only framework that makes answer commitment conditional on an explicit assessment of the information required to answer a question. We evaluate three CoSQ variants under seventeen conditions on the 817-item TruthfulQA multiple-choice validation set using eleven open-weight and hosted model families. In the final balanced-option protocol, Grounded-CoSQ at τ=0.90 reduces the mean unconditional wrong-commitment rate from 13.1% under chain-of-thought prompting to 8.9%, a 32.1% relative reduction, while increasing answered accuracy from 86.9% to 89.7% and answering 87.6% of questions. Both improvements hold for all eleven models and at every evaluated threshold. Critical-CoSQ and Adaptive-CoSQ provide neighboring operating points with 88.6% and 86.5% coverage, respectively, while remaining more reliable than the baseline. A secondary Natural Questions Short-Answer evaluation provides convergent open-form evidence. These findings show that self-assessment can support explicit, tunable answer-or-abstain decisions when an unsupported commitment is more costly than referral or review.

### 🤖 AI 总结

**一句话总结**：Large language models can produce fluent answers when their factual support is weak. This paper introduces Chain-of-Self-Questioning (CoSQ), a prompt-only framework that makes answer commitment condit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, When, Should, Abstain?, Selective, Risk, Control, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17516v1) | [下载PDF](https://arxiv.org/pdf/2609.17516v1.pdf)

---

## [9. What Breaks Under Pruning in Smart Homes, and When? Evaluating LLM Degradation Across Architectures and Task Complexity](https://arxiv.org/abs/2609.17515v1)

**作者**：Congjing Zhang, Vashishtha Patil, Henning Lange 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-15

### 📄 论文摘要

Pruning can reduce the deployment cost of large language models (LLMs), but its impact on context-grounded tool calling remains poorly understood. We systematically study pruning-induced degradation in smart-home tool calling across four LLMs spanning dense Transformer, dense hybrid, and mixture-of-experts (MoE) architectures, together with depth, width, hybrid, and expert pruning methods. After post-pruning supervised fine-tuning (SFT), we evaluate more than 19,500 instances from three smart-home datasets. Beyond aggregate task accuracy, we characterize degradation along two dimensions: action components (i.e., operation, device, argument, and value) and task complexity. Our results show that dense models have narrow safe pruning regions followed by sharp degradation, while MoE models tolerate substantially more pruning. Pruning degrades grounded specificity before schema-level intent, and aggressive dense pruning can induce systematic over-refusal. These findings highlight the importance of evaluating pruning beyond aggregate accuracy when selecting pruned LLMs for reliable tool execution.

### 🤖 AI 总结

**一句话总结**：Pruning can reduce the deployment cost of large language models (LLMs), but its impact on context-grounded tool calling remains poorly understood. We systematically study pruning-induced degradation i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：What, Breaks, Under, Pruning, Smart, Homes, When?, Evaluating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17515v1) | [下载PDF](https://arxiv.org/pdf/2609.17515v1.pdf)

---

## [10. Enhancing Accessibility of Medical Texts through Large Language Model-Driven Plain Language Adaptation](https://arxiv.org/abs/2609.17398v1)

**作者**：Ting-Wei Chang, Hen-Hsen Huang, Hsin-Hsi Chen  
**分类**：cs.CL  
**发布时间**：2026-09-15

### 📄 论文摘要

This paper addresses the challenge of making complex healthcare information more accessible through automated Plain Language Adaptation (PLA). PLA aims to simplify technical medical language, bridging a critical gap between the complexity of healthcare texts and patients' reading comprehension. Recent advances in Large Language Models (LLMs), such as GPT and BART, have opened new possibilities for PLA, especially in zero-shot and few-shot learning contexts where task-specific data is limited. In this work, we leverage the capabilities of LLMs such as GPT-4o-mini, Gemini-1.5-pro, and LLaMA for text simplification. Additionally, we incorporate Mixture-of-Agents (MoA) techniques to enhance adaptability and robustness in PLA tasks. Key contributions include a comparative analysis of prompting strategies, finetuning with QLoRA on different LLMs, and the integration of MoA technique. Our findings demonstrate the effectiveness of LLM-driven PLA, showcasing its potential in making healthcare information more comprehensible while preserving essential content.

### 🤖 AI 总结

**一句话总结**：This paper addresses the challenge of making complex healthcare information more accessible through automated Plain Language Adaptation (PLA). PLA aims to simplify technical medical language, bridging...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Enhancing, Accessibility, Medical, Texts, through, Large, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17398v1) | [下载PDF](https://arxiv.org/pdf/2609.17398v1.pdf)

---

## [11. ECHO: A Matched-Contrast Benchmark for Context-Sensitive Turn-Taking in Full-Duplex Dialogue](https://arxiv.org/abs/2609.17360v1)

**作者**：Shuofeng Zhao, Hongwei Cai, Wenke Fan 等 12 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-15

### 📄 论文摘要

Full-duplex spoken dialogue systems must distinguish interruptions that require yielding the floor from backchannels that permit continued speaking. Existing benchmarks typically evaluate events independently and may therefore reward fixed action preferences rather than context-sensitive decisions. We introduce ECHO, a paired diagnostic benchmark for Chinese full-duplex turn-taking. ECHO pairs examples with the same overlap transcript but contrasting preceding multi-turn dialogue contexts, with one requiring Yield and the other Keep. It additionally includes off-talk examples for diagnosing unnecessary yielding. We introduce pair accuracy, which requires correct decisions on both members of a pair and assigns no credit to constant-action policies. Experiments on multiple full-duplex systems show that most exhibit a pronounced bias toward \textsc{Yield}, performing substantially better on interruptions than on backchannels, while another system remains comparatively balanced. These findings demonstrate that interruption-only evaluation can overestimate practical turn-taking reliability. ECHO and its metadata will be publicly released.

### 🤖 AI 总结

**一句话总结**：Full-duplex spoken dialogue systems must distinguish interruptions that require yielding the floor from backchannels that permit continued speaking. Existing benchmarks typically evaluate events indep...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ECHO, Matched-Contrast, Benchmark, Context-Sensitive, Turn-Taking, Full-Duplex, Dialogue, spoken

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17360v1) | [下载PDF](https://arxiv.org/pdf/2609.17360v1.pdf)

---

## [12. Where Should a Document Live: Context, Representations, or Parameters?](https://arxiv.org/abs/2609.17346v1)

**作者**：Nathanaël Carraz Rakotonirina, Momchil Hardalov, Gonzalo Iglesias 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-15

### 📄 论文摘要

To answer questions outside of their pre-training data, large language models (LLMs) need access to new information, which can be presented in the context window as documents, encoded into the model's parameters, or injected as latent representations. However, each of these methods comes with different efficiency, cost, and performance trade-offs, with no single winner. We present a controlled comparison of representation-based (KV-cache based) and parametric (fine-tuning-based) adaptation methods on five knowledge-intensive benchmarks. We show that in the oracle setting, Cartridges (KV) are the most accurate injection method at nearly every storage budget, outperforming parametric methods by 10 points. Compaction (KV) matches Cartridges only at low compression rates, lagging behind the parametric methods by 10 points at rates higher than $50\times$. In the more realistic multi-document retrieval scenario, Cartridges are the only method that matches in-context learning (ICL), leading the parametric methods by 29 points and Compaction by 15 points. Nonetheless, Cartridges are also the only method, besides full fine-tuning and large MLP adapters, that suffers from catastrophic forgetting, i.e., a 6% performance degradation on control benchmarks, with 13% in coding.

### 🤖 AI 总结

**一句话总结**：To answer questions outside of their pre-training data, large language models (LLMs) need access to new information, which can be presented in the context window as documents, encoded into the model's...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：or, Where, Should, Document, Live, Context, Representations, Parameters?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17346v1) | [下载PDF](https://arxiv.org/pdf/2609.17346v1.pdf)

---

## [13. Towards Detecting AI-Assisted Responses in Online Surveys](https://arxiv.org/abs/2609.17317v1)

**作者**：Qizhou Wang, Bogdan Mamaev, Christopher Leckie  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-09-15

### 📄 论文摘要

The use of LLMs to complete online surveys impacts the validity of survey-based research, but detecting such usage remains underexplored. We introduce an initial benchmark dataset, namely ASURRE, for AI-assisted survey participation to capture usage strategies ranging from full generation and revision to persona-grounded agentic completion. Controlled by these strategies, LLM-assisted survey responses are generated using multiple LLMs on three real-world surveys in different disciplines, paired with genuine human responses. Our evaluation of existing machine-generated text (MGT) detectors shows that naive AI usage is readily detectable, whereas persona-grounded agents that mimic entire respondents push detector performance toward chance. We further show that agentic completion cannot fully replicate respondent-level behaviour and leaves distinctive behavioural traces. While individual cues can be circumvented by targeted prompting, a simple few-shot, training-free aggregator over these cues improves mean AUROC by +0.14 over the best existing detector across agentic settings. Our project is available at https://github.com/mike-qz-wang/ASURRE.

### 🤖 AI 总结

**一句话总结**：The use of LLMs to complete online surveys impacts the validity of survey-based research, but detecting such usage remains underexplored. We introduce an initial benchmark dataset, namely ASURRE, for ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Towards, Detecting, AI-Assisted, Responses, Online, Surveys, use

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17317v1) | [下载PDF](https://arxiv.org/pdf/2609.17317v1.pdf)

---

## [14. Zero-shot narrative detection in social messaging](https://arxiv.org/abs/2609.17310v1)

**作者**：Jesús M. Fraile-Hernández, Anselmo Peñas, Patrick Giedemann  
**分类**：cs.CL  
**发布时间**：2026-09-15

### 📄 论文摘要

This study investigates the zero-shot ability of large language models (LLMs) to identify and classify hidden narratives in social messages. Our research hypothesis is that LLMs' extensive contextual knowledge allows them to interpret messages on a deeper, pragmatic level, going beyond basic sentiment or topic analysis. Experiments on the Dipromats and SemEval datasets show that providing models with human-written narrative descriptions significantly improves performance, without the need of training examples. In contrast, automatically generated descriptions or the use of few examples (few-shot) often degrade accuracy due to subtle shifts in framing. The study also finds that ensemble methods, particularly majority voting, enhance robustness and that larger models perform best while also being less sensitive to prompt variations. The findings validate that LLMs can effectively detect strategic narratives in a zero-shot setting, and when combined with simple ensembling and human-written descriptions, they can rival supervised systems, offering a scalable solution for narrative detection, specially when there is no training data for the vast majority of domains.

### 🤖 AI 总结

**一句话总结**：This study investigates the zero-shot ability of large language models (LLMs) to identify and classify hidden narratives in social messages. Our research hypothesis is that LLMs' extensive contextual ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Zero-shot, narrative, detection, social, messaging, study, investigates, ability

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17310v1) | [下载PDF](https://arxiv.org/pdf/2609.17310v1.pdf)

---

## cs.CV

## [15. PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control](https://arxiv.org/abs/2609.17521v1)

**作者**：Chuhao Chen, Peter Wonka, Chaoyang Wang 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-09-15

### 📄 论文摘要

Interactive control for video generation is moving from coarse prompts toward fine-grained, physically meaningful manipulation of dynamic scenes. Yet existing controllable methods either require the full control schedule before generation starts, or use pixel-space signals that dictate object positions rather than physical dynamics. To address these limitations, we propose PhysStream, an autoregressive model for physics-grounded image-to-video synthesis that incorporates structured scene memory---positional maps and object tracking maps derived online from previously generated frames---and supports fine-grained motion control via sparse velocity-increment signals that encode physical quantities, letting the model learn the underlying dynamics. We train our model in two stages: a bidirectional model is first finetuned with motion-control conditioning, then a causal autoregressive model is trained with additional structured scene memory, further improving physical consistency. PhysStream enables interactive, mid-generation control over multi-object tabletop rigid-body scenes---a capability not supported by prior methods---reducing motion distribution distance (FVMD) by 33% and trajectory error by 12% over the strongest baselines on synthetic benchmarks, and is preferred by human evaluators in over 85% of in-the-wild comparisons. Please check our website for more details: https://czzzzh.github.io/PhysStream

### 🤖 AI 总结

**一句话总结**：Interactive control for video generation is moving from coarse prompts toward fine-grained, physically meaningful manipulation of dynamic scenes. Yet existing controllable methods either require the f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PhysStream, Streaming, Physics-Grounded, Video, Generation, Structured, Scene, Memory

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17521v1) | [下载PDF](https://arxiv.org/pdf/2609.17521v1.pdf)

---

## [16. Det-LIME: Detector-Aware, Multi-Instance Local Interpretable Model-Agnostic Explanations for Automated Marine Mammal Detection](https://arxiv.org/abs/2609.17479v1)

**作者**：Jiayi Zhou, David W. Johnston, Brinnae Bent  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-09-15

### 📄 论文摘要

Despite the rapid uptake of black-box object detectors in marine mammal research and monitoring, explainability techniques are rarely integrated into conservation workflows. Furthermore, most classification-oriented explainability tools are ill-suited to detection tasks involving imagery of social organisms or those with colonial life histories, as they ignore multiple detections within a scene and produce single-instance outputs that blur evidence across individuals. These methods also generate low-resolution, often biologically irrelevant visuals, limiting their utility for debugging, targeted data augmentation, and refined data collection.   We proposed Det-LIME, a detector-aware, multi-instance adaptation of Local Interpretable Model-Agnostic Explanations (LIME) that produced instance-specific, box-aligned explanations by combining per-detection weighting, a proximity kernel that emphasizes regions near each box, and Intersection-over-Union-based matching to track the same instance across perturbations. We evaluated Det-LIME on aerial drone imagery for harbor seal detection, with an additional seabird case study to assess generality, and compared it with vanilla LIME, Stabilized LIME, Deterministic LIME, and gradient-based attribution methods.   Using the Attribution Ratio and Max Saliency Hit Rate metrics, we showed that Det-LIME consistently improved multi-instance attribution. In practice, these higher-resolution, instance-aware explanations provide insight into model outputs and support post-processing, debugging, and actionable improvements in modeling and data collection or augmentation.

### 🤖 AI 总结

**一句话总结**：Despite the rapid uptake of black-box object detectors in marine mammal research and monitoring, explainability techniques are rarely integrated into conservation workflows. Furthermore, most classifi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Det-LIME, Detector-Aware, Multi-Instance, Local, Interpretable, Model-Agnostic, Explanations, Automated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17479v1) | [下载PDF](https://arxiv.org/pdf/2609.17479v1.pdf)

---

## [17. Tables Decoded: DELTA for Structure, TARQA for Understanding](https://arxiv.org/abs/2609.17458v1)

**作者**：Jahanvi Rajput, Dhruv Kudale, Saikiran Kasturi 等 5 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-09-15

### 📄 论文摘要

Table understanding is a core task in document intelligence, encompassing two key subtasks: table reconstruction and table visual question answering (TabVQA). While recent approaches predominantly rely on vision- language models (VLMs) operating on table images, we propose a more scalable and effective alternative based on structured textual representations. These representations are easier to process, align more naturally with LLMs, and eliminate the need for language-specific visual encoders, making them particularly suitable for multilingual documents. We present DELTA, which separates physical structure recognition, logical structure recognition, and OCR to extract both layout and content accurately. DELTA outputs tables in Optimised Table Structure Language (OTSL), a compact and unified format that encodes cell arrangements and textual content. On table structure recognition (TSR), DELTA achieves TEDS- Structure scores comparable with state-of-the-art methods across FinTabNet, PubTabNet, and PubTables-1M. We further establish its robustness on non-English tables through our curated Hindi benchmark, TORQUE. Building on this, we introduce TARQA, an LLM fine-tuned on OTSL sequences. Our approach yields gains of 9.3 p.p. on WTQ (TabQA) and 9.2 p.p. on FinTabNetQA (TabVQA), respectively. On TORQUE, our method ranks second among all VLMs and DELTA + LLM variants. We release our code, models, and benchmark at: https://github.com/Tihiitborg/Tables-Decoded

### 🤖 AI 总结

**一句话总结**：Table understanding is a core task in document intelligence, encompassing two key subtasks: table reconstruction and table visual question answering (TabVQA). While recent approaches predominantly rel...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Tables, Decoded, DELTA, Structure, TARQA, Understanding, Table, core

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17458v1) | [下载PDF](https://arxiv.org/pdf/2609.17458v1.pdf)

---

## [18. ORCA: Occlusion-Aware Refinement and Completion for Novel View Synthesis](https://arxiv.org/abs/2609.17450v1)

**作者**：Weronika Jakubowska, Maciej Zięba, Przemysław Spurek  
**分类**：cs.CV  
**发布时间**：2026-09-15

### 📄 论文摘要

Novel-view synthesis from a single image is a fundamentally ambiguous problem. As the camera moves away from the input viewpoint, previously hidden regions become visible, exposing missing geometry and holes in the reconstructed scene. Existing methods often rely on generative models to complete such regions. However, many of these artifacts are small gaps near depth boundaries and do not require generating new scene content.   In order to eliminate expensive process of generating image we introduce ORCA, an occlusion-aware method for reconstructing and completing explorable 3D scenes from a single image. ORCA first introduces 3D structure into a Gaussian-anchor representation using monocular depth while preserving the original camera-ray correspondence. During scene exploration, missing regions are handled based on their size and structure. Small disocclusions are repaired using RGB-D information already available in the reconstruction, while generative inpainting is reserved for larger regions that cannot be reliably recovered from the scene. New Gaussian anchors are added and optimized locally without modifying the existing representation. By reducing unnecessary reliance on generative inpainting, ORCA limits generation-induced hallucinations and better preserves the content and structure of the original scene.   On DIV2K, ORCA improves novel-view quality over VistaDream across all reported metrics, increasing MUSIQ from 61.60 to 68.71 and CLIP-IQA from 0.474 to 0.574. These results show that many novel-view artifacts can be repaired effectively by reusing information already present in the reconstructed scene.

### 🤖 AI 总结

**一句话总结**：Novel-view synthesis from a single image is a fundamentally ambiguous problem. As the camera moves away from the input viewpoint, previously hidden regions become visible, exposing missing geometry an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ORCA, Occlusion-Aware, Refinement, Completion, Novel, View, Synthesis, Novel-view

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17450v1) | [下载PDF](https://arxiv.org/pdf/2609.17450v1.pdf)

---

## [19. Tracking the Unseen: An Occlusion-Robust Framework for Target Tracking Under Full and Long-Term Occlusion](https://arxiv.org/abs/2609.17427v1)

**作者**：Mais Mohammed, Sharifa Mohammed, Hanan Awadh 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-09-15

### 📄 论文摘要

Real-time multi-object tracking systems remain highly vulnerable to full and long-term occlusion, where targets temporarily or completely disappear from the camera's field of view. Conventional trackers may terminate trajectories prematurely, resulting in identity loss and reduced situational awareness in applications such as defense and surveillance. This work proposes an occlusion-robust target tracking framework that maintains target identity and trajectory continuity through the integration of YOLOv11n object detection, Kalman Filter motion prediction, and occlusion-aware appearance-based re-identification. The framework consists of three stages: object detection, position estimation during occlusion, and identity recovery after target reappearance. Six Re-Identification (Re-ID) architectures were evaluated within the same tracking framework under identical conditions, with the Occlusion-Aware Mask Network (OAMN) achieving the best overall performance and therefore selected for the final pipeline. The framework was benchmarked against OccluTrack on the public OVIS dataset, achieving relative improvements of 18.1 percent in Multiple Object Tracking Accuracy (MOTA) and 25.1 percent in Identity F1 Score (IDF1), while reducing identity switches by 12.8 percent. On a custom military dataset simulating surveillance and battlefield-like environments with long-term occlusion, the framework achieved a MOTA of 0.734 and an IDF1 of 0.729, corresponding to relative improvements of 14.2 percent and 5.8 percent over OccluTrack. The system demonstrated strong tracking continuity, robust identity preservation, and reliable trajectory estimation under challenging occlusion conditions, highlighting its effectiveness for defense-related surveillance applications requiring continuous target tracking during visibility loss.

### 🤖 AI 总结

**一句话总结**：Real-time multi-object tracking systems remain highly vulnerable to full and long-term occlusion, where targets temporarily or completely disappear from the camera's field of view. Conventional tracke...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Tracking, Unseen, Occlusion-Robust, Framework, Target, Under, Full

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17427v1) | [下载PDF](https://arxiv.org/pdf/2609.17427v1.pdf)

---

## [20. SlotDiT: Object-Centric Representations for Diffusion Transformers](https://arxiv.org/abs/2609.17414v1)

**作者**：Gjergj Plepi, Sven Behnke  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-09-15

### 📄 论文摘要

Text-conditioned latent diffusion models perform strongly in video generation and are promising backbones for robotic applications. However, existing approaches rely on pixel-level or VAE-based latent representations that lack explicit semantic structure, leaving the impact of the representation space largely unexplored. Slot-based object-centric representations offer a structured alternative by decomposing scenes into object-level latents, or slots. While they have shown success in dynamics modeling and planning, they have not yet been explored for diffusion-based generative modeling. We introduce SlotDiT, a text-guided Diffusion Transformer (DiT) that operates in a slot-based latent space. Given a reference image and a language instruction, SlotDiT decomposes the scene into object-centric slots representing individual entities. Conditioned on the instruction and observed scene context, the model autoregressively denoises future slot trajectories to predict scene dynamics. To systematically investigate latent-space design for diffusion transformers, we compare slot-based representations against VAE-based and semantics-aligned alternatives within a unified DiT framework. Our experiments show that using slots as DiT latents yields competitive video generation quality while consistently improving task-completion rates across four robotic datasets. Furthermore, their compact representation provides a computationally efficient alternative to VAE-based and semantics-aligned latent spaces. Overall, our results demonstrate that object-centric structure is a powerful inductive bias for diffusion-based generative modeling in robotic environments. The project page is available at https://slot-dit.github.io/.

### 🤖 AI 总结

**一句话总结**：Text-conditioned latent diffusion models perform strongly in video generation and are promising backbones for robotic applications. However, existing approaches rely on pixel-level or VAE-based latent...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, SlotDiT, Object-Centric, Representations, Transformers, Text-conditioned, latent, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17414v1) | [下载PDF](https://arxiv.org/pdf/2609.17414v1.pdf)

---

## [21. SSC-Priors: Exploring Semantic and Visibility Priors to Boost Lidar Semantic Scene Completion](https://arxiv.org/abs/2609.17413v1)

**作者**：Tetiana Martyniuk, Jonathan Seele, Alexandre Boulch 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-15

### 📄 论文摘要

This paper investigates easy strategies to boost the performance of existing networks for lidar semantic scene completion (SSC) without requiring complex architectural redesigns. The fact is that, over the last years, SSC methods have mostly pursued architectural innovations, making the models heavier and more complex, e.g., by jointly training a point cloud semantic segmentation branch. In this work, we take a step back and explore two priors used as simple ingredients (possibly noisy) to improve existing approaches: semantic pseudo-labels and sensor visibility information. Concretely, we provide both kinds of information directly as additional inputs to a given SSC network, requiring only a minimal adaptation of the original architecture. We first demonstrate that endowing input point clouds with semantic pseudo-labels from off-the-shelf segmenters significantly improves the performance of existing SSC models. In fact, by evaluating these models against an oracle, we establish that high-quality semantic priors are a primary driver of semantic gains (mIoU), and that the SSC model can be trained just once with ground-truth semantics and then exploited without retraining using any segmenter. Furthermore, we equip the input lidar point cloud with visibility information that distinguishes between empty spaces (between the lidar and a scanned point) and unknown spaces (outside of lines of sight), providing a secondary performance boost across the tested architectures. We study the design space of data for representing visibility information and bound the remaining headroom with a ground-truth oracle on the free-space labels. On SemanticKITTI, these enhancements make older models competitive with state-of-the-art systems across four architectures, in one case even outperforming them. On the SSCBench-nuScenes benchmark, both priors also transfer with the sparser 32-beam sensor.

### 🤖 AI 总结

**一句话总结**：This paper investigates easy strategies to boost the performance of existing networks for lidar semantic scene completion (SSC) without requiring complex architectural redesigns. The fact is that, ove...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SSC-Priors, Exploring, Semantic, Visibility, Priors, Boost, Lidar, Scene

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17413v1) | [下载PDF](https://arxiv.org/pdf/2609.17413v1.pdf)

---

## [22. PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)

**作者**：Yongqi Mao, Hao Shi, Yufan Zhang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-15

### 📄 论文摘要

Real-time dense SLAM is a core capability for robotics applications that require robust localization and high- quality mapping in dynamic or fast-changing environments. Recent 3D Gaussian Splatting (3DGS)-based SLAM methods have shown promising performance, but most are designed for narrow-FoV pinhole cameras, where limited angular coverage weakens pose observability and often leads to unstable photo- metric optimization under rapid motion and large viewpoint changes. We present PanoGS-SLAM, the first panoramic dense SLAM system built on 3D Gaussian Splatting. Our method per- forms differentiable rendering and pose optimization directly in the spherical domain, enabling omnidirectional photometric constraints for more stable tracking. To improve geometric consistency and robustness, we introduce (1) a sphere-consistent photometric loss that compensates for the area distortion of equirectangular projection, and (2) a depth-guided Gaussian initialization strategy that stabilizes incremental mapping in newly observed regions. Extensive experiments on both real and synthetic panoramic benchmarks (PALVIO and SynPano) show that PanoGS-SLAM consistently outperforms geometric and GS-based baselines in tracking accuracy and rendering quality, while achieving fast front-end convergence and real-time perfor- mance. In addition, controlled field-of-view experiments reveal a clear monotonic improvement in optimization conditioning and convergence stability as angular coverage increases, high- lighting the fundamental role of sensing geometry in shaping the optimization landscape of differentiable Gaussian-based SLAM. The source code will be made publicly available.

### 🤖 AI 总结

**一句话总结**：Real-time dense SLAM is a core capability for robotics applications that require robust localization and high- quality mapping in dynamic or fast-changing environments. Recent 3D Gaussian Splatting (3...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, PanoGS-SLAM, Panoramic, Gaussian, Splatting, SLAM, Real-time, dense

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17387v1) | [下载PDF](https://arxiv.org/pdf/2609.17387v1.pdf)

---

## [23. Optical-Flow Wingbeat Counting in MuJoCo: A Comparison of Convolutional, Spiking, and Attention-Based Temporal Models](https://arxiv.org/abs/2609.17308v1)

**作者**：Zhang Nengbo  
**分类**：cs.CV  
**发布时间**：2026-09-15

### 📄 论文摘要

Visual monitoring of flapping-wing vehicles requires distinguishing individual wingbeats from motion strength and average frequency. This paper presents a controlled MuJoCo evaluation of wingbeat counting from signed optical flow observed by virtual cameras mounted on Crazyflie vehicles. Three flapping-wing models were recorded at optical distances of 1.5 and 3.0 m, producing 1,440 clips from 240 paired scene configurations with a scene-level 3:1 training-test split. A common spatial convolutional encoder was combined with a causal temporal convolutional network, a recurrent leaky integrate-and-fire spiking network, or causal self-attention. Each model predicted phase and activity, followed by the same directed-crossing event counter. The six existing convolutional models were retained, and all twelve new models were frozen before their test predictions were generated. Exact-count accuracies at 1.5 m were 96.67%, 95.00%, and 96.67%, respectively; at 3.0 m they were 94.44%, 92.22%, and 95.00%. All paired scene-bootstrap intervals for differences in exact-count accuracy included zero. Seven far-distance spiking-model clips had correct totals despite event-timing mismatches, demonstrating why total-count and event-level measurements must be reported together. The results support the feasibility of causal optical-flow counting in the tested setting and identify boundary-sensitive errors. They do not establish an architecture ranking across repeated training, real-flight robustness, or hardware efficiency.

### 🤖 AI 总结

**一句话总结**：Visual monitoring of flapping-wing vehicles requires distinguishing individual wingbeats from motion strength and average frequency. This paper presents a controlled MuJoCo evaluation of wingbeat coun...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Optical-Flow, Wingbeat, Counting, MuJoCo, Comparison, Convolutional, Spiking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17308v1) | [下载PDF](https://arxiv.org/pdf/2609.17308v1.pdf)

---

## cs.LG

## [24. ENCP: Episode-Normalized Conformal Prediction for Vision-and-Language Navigation](https://arxiv.org/abs/2609.17499v1)

**作者**：Vicky Feliren, A. Taufiq Asyhari, Muhamad Risqi U. Saputra  
**分类**：cs.LG, cs.AI, cs.RO  
**发布时间**：2026-09-15

### 📄 论文摘要

Uncertainty estimation for Vision-Language-Navigation (VLN) models is a critical task since it can help identify ambiguous and unreliable predictions, enabling agents to make safer navigation decisions. As one of the most advanced uncertainty estimation frameworks, conformal prediction (CP) offers a promising approach for uncertainty estimation in VLN. However, given that VLN agent requires a sequence of steps, standard calibration in conformal prediction fails to provide coverage guarantee it promises over a dependent, variable-length VLN episode. To this end, we propose Episode-Normalized Conformal Prediction (ENCP), which rescales a nonconformity score by the policy's residual confidence and calibrates one maximum score per episode. Under exchangeable calibration and test episodes, this construction covers the ground truth at every step with probability at least $1 - α$, while allowing dependence among steps within an episode. Across four VLN policies and three nonconformity scores on R2R and REVERIE dataset, ENCP meets all reported empirical step-coverage targets on the seen-to-unseen evaluation. These results demonstrate that ENCP can provide model-agnostic uncertainty estimates, which might be useful for determining when a VLN agent should defer to a more capable predictor, including human assistance.

### 🤖 AI 总结

**一句话总结**：Uncertainty estimation for Vision-Language-Navigation (VLN) models is a critical task since it can help identify ambiguous and unreliable predictions, enabling agents to make safer navigation decision...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ENCP, Episode-Normalized, Conformal, Prediction, Vision-and-Language, Navigation, Uncertainty, estimation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17499v1) | [下载PDF](https://arxiv.org/pdf/2609.17499v1.pdf)

---

## [25. FreqSpaNet: Frequency and Spatial Learning of SFPF for Physical Layer Hardware Integrity Detection](https://arxiv.org/abs/2609.17491v1)

**作者**：Xiaoxuan Huang, Jinlong Xu, YiZhe Wang 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-15

### 📄 论文摘要

Unauthorized hardware replacement can preserve a wireless device's logical identity while altering its physical implementation, posing a challenge to hardware integrity verification. Spatio-frequency polarization fingerprints (SFPFs) capture device-dependent responses across multiple frequencies and directions, but their frequency and spatial dimensions exhibit different structural dependencies. We propose FreqSpaNet, an SFPF representation learning network for open set hardware anomaly detection. A frequency branch captures local variations among neighboring frequencies, while a geometry-aware spatial branch models directional relationships using angular information. The two representations are combined through adaptive fusion, and complementary pretraining further captures shared information while preserving the distinct characteristics of the frequency and spatial representations. Experiments show that FreqSpaNet achieves a mean AUROC of 96.31\%, 9.05 points above the baseline. Results under seven hardware replacement scenarios further verify the effectiveness of FreqSpaNet.

### 🤖 AI 总结

**一句话总结**：Unauthorized hardware replacement can preserve a wireless device's logical identity while altering its physical implementation, posing a challenge to hardware integrity verification. Spatio-frequency ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, FreqSpaNet, Frequency, Spatial, Learning, SFPF, Physical, Layer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17491v1) | [下载PDF](https://arxiv.org/pdf/2609.17491v1.pdf)

---

## [26. Reduced-Space Multi-Fidelity Bayesian Optimization of Process Simulation Models](https://arxiv.org/abs/2609.17440v1)

**作者**：Niki Triantafyllou, Andrea Bernardi, Maria M. Papathanasiou  
**分类**：cs.LG, math.OC  
**发布时间**：2026-09-15

### 📄 论文摘要

Optimizing industrial process flowsheets is often computationally prohibitive due to the high cost of rigorous simulations and the curse of dimensionality inherent in complex design spaces. To address these challenges, we present a reduced-space multi-fidelity Bayesian optimization (RS-MFBO) framework designed for high-dimensional, expensive black-box functions. The approach integrates Global Sensitivity Analysis (GSA) for dimensionality reduction with a fidelity-augmented Gaussian process that captures correlations between low-cost approximations and expensive high-fidelity evaluations. A cost-aware acquisition strategy, augmented with cooldown and promotion mechanisms, adaptively guides the allocation of samples across fidelities. The framework is validated on two distinct industrial process simulators: a plasmid DNA bioprocess in SuperPro Designer and a green fuel synthesis plant in Aspen HYSYS. Results across diverse economic and physical objectives demonstrate that the proposed method substantially reduces the number of high-fidelity simulator evaluations while maintaining competitive optimization performance compared to single-fidelity baselines. These results highlight RS-MFBO as a scalable, simulator-agnostic approach for cost-constrained black-box optimization.

### 🤖 AI 总结

**一句话总结**：Optimizing industrial process flowsheets is often computationally prohibitive due to the high cost of rigorous simulations and the curse of dimensionality inherent in complex design spaces. To address...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Reduced-Space, Multi-Fidelity, Bayesian, Optimization, Process, Simulation, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17440v1) | [下载PDF](https://arxiv.org/pdf/2609.17440v1.pdf)

---

## [27. Learning-Guided Planning in Large Dynamic Action Spaces: Budgeted Tree Search for One-to-Many Mobile Charging](https://arxiv.org/abs/2609.17429v1)

**作者**：Liang-Ching Tao, Pi-Chung Wang  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-15

### 📄 论文摘要

Many learned sequential decision systems map the current state directly to an action. That shortcut becomes brittle when candidate actions are numerous, geometrically structured, and rebuilt with the state. One-to-many mobile charging makes this setting concrete: with N=250 sensors, the initial state induces about 1,125 candidate charging-stop actions; each chosen stop simultaneously serves its in-range sensors, and the action universe changes as sensors die. LP-BTS is a learning-guided planning architecture: a graph proposal policy concentrates a small candidate support, a learned value critic evaluates leaves, and edge-budgeted PUCT compares short simulated futures before committing an action. Because the policy scores this set without a fixed output head, a single frozen checkpoint covers every evaluated setting, spanning action universes from 736 to 2,813 stops. Matched ablations reveal complementary effects: uniform sampling costs 8.8 survival percentage points, while, with targeted support fixed, PUCT jointly retains 1.4 points (about 3.5 of 250 sensors) and direct policy selection travels 23% farther. On a prospectively specified, sealed 30-scenario confirmatory bank evaluated once, LP-BTS attains the highest observed survival (0.4545) and alive-AUC (0.8031). Its estimated survival advantage over the strongest domain-engineered comparator is +0.0066 (95% CI [-0.0037, +0.0184]), an unresolved difference, while it exceeds a deadline heuristic and two source-derived direct-policy reconstructions on every paired scenario. Both learned rows are trained, source-derived reconstructions of variants reported by Gong et al. In this setting, the results provide controlled evidence about learning-guided planning in a large, dynamic action space.

### 🤖 AI 总结

**一句话总结**：Many learned sequential decision systems map the current state directly to an action. That shortcut becomes brittle when candidate actions are numerous, geometrically structured, and rebuilt with the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning-Guided, Planning, Large, Dynamic, Action, Spaces, Budgeted, Tree

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17429v1) | [下载PDF](https://arxiv.org/pdf/2609.17429v1.pdf)

---

## [28. Bridging the Confidence Gap: Temperature Scaling for Calibrating Test-Time Prompt Tuning](https://arxiv.org/abs/2609.17386v1)

**作者**：Yuwei Liang, Jian Liang, Dapeng Hu 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-15

### 📄 论文摘要

Test-time prompt tuning (TPT) enables adaptation on a single test instance, achieving improved accuracy but often sacrificing calibration performance. Most existing calibration methods introduce additional regularization terms to promote dispersion across text embeddings and reduce calibration error, yet these methods often suffer from a drop in accuracy. Motivated by the well-calibrated nature of zero-shot predictions, we propose CoTS, a simple yet effective post-hoc calibration method that preserves accuracy. Specifically, CoTS applies temperature scaling to minimize the confidence gap between adapted and zero-shot predictions. To fully exploit the potential of multiple augmentations during adaptation, we introduce a weak-strong ensemble strategy that further boosts accuracy. We then apply CoTS to this ensemble, termed E-CoTS, to maintain its well-calibrated property. Extensive experiments on diverse datasets and backbones show that our approaches effectively mitigate miscalibration without compromising primary accuracy. For instance, E-CoTS reduces the average expected calibration error of TPT from 11.90% to 5.38% on ImageNet variants, while even increasing accuracy from 60.74% to 62.95%. Moreover, when integrated with existing calibration methods, E-CoTS usually enhances both accuracy and calibration simultaneously.

### 🤖 AI 总结

**一句话总结**：Test-time prompt tuning (TPT) enables adaptation on a single test instance, achieving improved accuracy but often sacrificing calibration performance. Most existing calibration methods introduce addit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bridging, Confidence, Gap, Temperature, Scaling, Calibrating, Test-Time, Prompt

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17386v1) | [下载PDF](https://arxiv.org/pdf/2609.17386v1.pdf)

---

## [29. OPEN-1B: A Fully Auditable Training Run](https://arxiv.org/abs/2609.17380v1)

**作者**：John Donaghy, Brian Wilcox, Oğuzhan Ersoy 等 9 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-15

### 📄 论文摘要

Open-source language models have a reproducibility problem. Despite releasing weights, training data, and recipes, none of them are provably reproducible due to the non-associativity of floating-point arithmetic. Deep learning frameworks often offer a deterministic execution mode, allowing reproducible operations on the same machines. Unfortunately, this determinism does not carry across hardware such that a user can verify that a released checkpoint was actually produced using the declared training recipe. This leaves room for undisclosed data, injected biases, or backdoors that existing techniques such as proof-of-learning or proof-of-training-data cannot rule out.   We introduce a new tier of model transparency, fully auditable, in which every operation on every data sample during training is independently reproducible on heterogeneous commodity hardware with bitwise certainty. By imposing a definite order on the sources of training nondeterminism, GPU kernel reductions, data batch ordering across a data-parallel cluster, and inter/intra-node collective communication, we make it possible to replay any individual step of a large, distributed training run on a single piece of commodity hardware and check it against the published trajectory.   Because replaying an entire run on one machine is infeasible, we support this with a collective verification scheme in which many independent auditors each certify individual steps, together covering the whole run. We release Open-1B, a model trained under this regime, together with its full pretraining dataset, every intermediate checkpoint, the training codebase, and the audit harness needed to reproduce and verify any step of its training.

### 🤖 AI 总结

**一句话总结**：Open-source language models have a reproducibility problem. Despite releasing weights, training data, and recipes, none of them are provably reproducible due to the non-associativity of floating-point...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OPEN-1B, Fully, Auditable, Training, Run, Open-source, language, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17380v1) | [下载PDF](https://arxiv.org/pdf/2609.17380v1.pdf)

---

## [30. Hybrid Variational Quantum Circuits for Multivariate Regression and High-Dimensional Data Reconstruction](https://arxiv.org/abs/2609.17358v1)

**作者**：Koffi Ognandon Ayena, Frédéric Holweck, Serge Iovleff 等 4 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-09-15

### 📄 论文摘要

Variational quantum circuits (VQCs) are parameterized quantum circuits optimized classically. We propose a hybrid variational quantum circuit (HVQC) extending VQCs with a classical affine post-measurement layer, enabling vector-valued regression without the linear overhead of independent scalar circuits. Theoretically, we show that elementary one-and two-qubit circuits can approximate quadratic functions and products via data re-uploading and entanglement, providing the foundations of the full architecture. Experimentally, on two synthetic image reconstruction datasets and the Friedman1 benchmark (40,568 test samples), our HVQC matches Gaussian Process Regression and outperforms XGBoost and Random Forest. An ablation study confirms that both quantum and classical components are essential, and results highlight the central role of the feature map in hybrid quantum-classical models.

### 🤖 AI 总结

**一句话总结**：Variational quantum circuits (VQCs) are parameterized quantum circuits optimized classically. We propose a hybrid variational quantum circuit (HVQC) extending VQCs with a classical affine post-measure...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hybrid, Variational, Quantum, Circuits, Multivariate, Regression, High-Dimensional, Data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.17358v1) | [下载PDF](https://arxiv.org/pdf/2609.17358v1.pdf)

---

