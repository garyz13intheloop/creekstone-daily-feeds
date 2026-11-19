# arXiv AI 论文日报 | 2026-11-19

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (3 篇)
- [cs.CV](#csCV) (9 篇)
- [cs.LG](#csLG) (13 篇)

---

## cs.AI

## [1. Knowing What You Know: A Trait Theory of Reviewer Value in Human-AI Cognitive Systems](https://arxiv.org/abs/2611.24932v1)

**作者**：Priyanka Sinha, Sugam Pandey  
**分类**：cs.AI, cs.CE, cs.HC, cs.LG  
**发布时间**：2026-11-18

### 📄 论文摘要

When a capable model and a human reviewer cooperate on the same decision, which human still adds value? We argue this is a question about a single cognitive trait, metacognitive calibration: the alignment between a reviewer's behavioral confidence and the actual correctness of their judgments. We develop a trait theory of reviewer value to make it precise. The theory makes five claims: value is governed by calibration rather than by activity, speed, agreement, or tenure; calibration leaves observable traces in behavioral telemetry; those traces are non-diagnostic on their own, because the fast, low-revision signature of a calibrated expert is indistinguishable from that of a confident novice until it is gated by outcomes; human calibration and a model's self-knowledge are the same construct, so the joint system should defer to whichever agent is better calibrated on each item; and individual calibration is causally identifiable only above the level of the single judgment. We ground each claim in a six-month production window of an AI-assisted accounting system (541621 reviewer events, 483 reviewers), and find that a purely behavioral expertise profile inverts the ground truth, scoring an overconfident cohort (5.2 percent correction survival) higher than genuine experts (99.2 percent); that reviewer quality is flat across tenure, so the trait is not learned on the job; and that the same calibration logic that separates good from bad reviewers, applied to the model, concentrates 92.5 percent of human effort on genuine errors. We close with the boundary the theory must respect: under majority-vote aggregation, individual causal value is unidentifiable.

### 🤖 AI 总结

**一句话总结**：When a capable model and a human reviewer cooperate on the same decision, which human still adds value? We argue this is a question about a single cognitive trait, metacognitive calibration: the align...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Knowing, What, Know, Trait, Theory, Reviewer, Value

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24932v1) | [下载PDF](https://arxiv.org/pdf/2611.24932v1.pdf)

---

## [2. Choosing What to Observe: Budget-Paired Counterfactual Audits for Credible Evaluation of Visual Agents](https://arxiv.org/abs/2611.24867v1)

**作者**：Ruiqi Liu, Jinming Li, Mo Wang 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-18

### 📄 论文摘要

Visual agents that read dense documents must ration a finite observation budget across candidate regions, yet answer accuracy conflates where an agent looks, how it adapts to the reads that remain, and how it an?swers once observation stops. We introduce budget-paired counterfactual audits, an evaluation protocol that holds public evidence and region bindings fixed while perturbing only the remaining budget or de?clared task parameters, and credits every acquired history with exact continuation values. The resulting accounting decomposes lost expected accuracy into stepwise acquisition loss and terminal decision loss, separating planning from fixed-role heuristics. Across forty paired routing anchors, five open-weight

### 🤖 AI 总结

**一句话总结**：Visual agents that read dense documents must ration a finite observation budget across candidate regions, yet answer accuracy conflates where an agent looks, how it adapts to the reads that remain, an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Choosing, What, Observe, Budget-Paired, Counterfactual, Audits, Credible, Evaluation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24867v1) | [下载PDF](https://arxiv.org/pdf/2611.24867v1.pdf)

---

## [3. Vibe-Trading: Towards Agent-Native Trading](https://arxiv.org/abs/2611.24845v1)

**作者**：Haozhe Wu, Zhonghang Li, Chao Huang  
**分类**：cs.AI, cs.CL, cs.MA, q-fin.CP, q-fin.TR  
**发布时间**：2026-11-18

### 📄 论文摘要

Existing AI agents can retrieve information, call tools, run experiments, and produce multi-step outputs. Yet most are built around relatively static workflows and struggle to preserve reliable state as the environment changes. Financial trading makes this limitation especially consequential: prices, news, market conditions, portfolio positions, and available capital evolve continuously. A result is useful only when it remains tied to the correct time, data snapshot, and execution context. We present Vibe-Trading, a comprehensive agent-native trading framework and all-in-one workspace for building, evaluating, and evolving agents for financial trading. It unifies market research, financial data, strategy generation, backtesting, portfolio analysis, paper trading, multi-agent collaboration, and optional broker execution. Its central contribution is an architecture that keeps results, evidence, research history, and trading authority connected throughout the research-to-action process. Each result retains its source, temporal scope, configuration, and producing run. Shared evidence grounding enables verification, versioned research records support reproducible continuation, and an explicit authority gate separates strategy research from live execution. Together, these designs provide a practical foundation for trading agents whose results can be traced, reproduced, and acted on only under explicit authority.

### 🤖 AI 总结

**一句话总结**：Existing AI agents can retrieve information, call tools, run experiments, and produce multi-step outputs. Yet most are built around relatively static workflows and struggle to preserve reliable state ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Vibe-Trading, Towards, Agent-Native, Trading, Existing, can, retrieve

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24845v1) | [下载PDF](https://arxiv.org/pdf/2611.24845v1.pdf)

---

## cs.CL

## [4. Jailbreak Detection on Large Language Models via Contrastive Prototype Structures](https://arxiv.org/abs/2611.24936v1)

**作者**：Yan Qiu, Yuanyuan Li  
**分类**：cs.CL  
**发布时间**：2026-11-18

### 📄 论文摘要

Jailbreak attempts and harmful prompts remain a challenge for the safe deployment of large language models. We study whether contrastively learned representations can support safety detection without training an additional downstream classifier. We propose Jailbreak Detection with Prototype Inference (JDPI), which uses binary safety labels to construct harmful and benign prototypes and makes predictions from relative prototype distances. JDPI uses only binary safety labels for encoder adaptation, prototype construction, and validation. In our setup, it uses fewer labeled examples than the classifier baseline (Method A) by avoiding the separate split used to train the downstream classifier. Across four benchmarks covering different input formats, contrastive fine-tuning improves JDPI's detection accuracy by 9.1-18.0 percentage points. Using the same encoder, JDPI achieves slightly higher ROC-AUC on one benchmark and stays within 0.017 of the baseline across all four. With dataset-specific adaptation, JDPI exceeds the released Llama Guard 3-8B baseline by 0.173-0.310 in ROC-AUC across the four benchmarks. In multi-turn replay on TomGibbs, JDPI uses accumulated user history as the conversation unfolds, achieving higher conversation-level accuracy than when it uses the current turn alone. Across 12 directed transfers, JDPI outperforms the classifier by an average of 1.59 percentage points in accuracy, demonstrating stronger cross-dataset robustness.

### 🤖 AI 总结

**一句话总结**：Jailbreak attempts and harmful prompts remain a challenge for the safe deployment of large language models. We study whether contrastively learned representations can support safety detection without ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Jailbreak, Detection, Large, Language, Models, via, Contrastive, Prototype

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24936v1) | [下载PDF](https://arxiv.org/pdf/2611.24936v1.pdf)

---

## [5. Ground, Iterate, Trace: Decomposing AI Research Ideation](https://arxiv.org/abs/2611.24887v1)

**作者**：Samson Yu, Qiran Zou, Jing Yu Lim 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-11-18

### 📄 论文摘要

Large language models have been widely used to generate plausible research ideas, yet it remains unclear what makes automated ideation effective and how generated novel proposals arise from prior scientific work. We introduce the Creative AI Researcher (CAR), an agentic framework combining literature grounding, iterative development and explicit conceptual operators. CAR constructs a semantic knowledge graph from retrieved literature and equips an ideation agent with graph-retrieval tools and four operators: bisociation, analogy, exploration and elaboration. Each operator call is checked against structural acceptance conditions and recorded, producing a trace of intermediate transformations and declared literature sources. We evaluate CAR with two language-model backbones across 40 LiveIdeaBench research topics and two execution benchmarks. CAR achieves significantly higher methodological novelty (MN) than single-shot prompting and The AI Scientist. Its methodological novelty does not differ significantly from the Research Ideation Agent, while its feasibility scores are higher on both backbones. With a shared experiment executor, CAR achieves the highest pairwise win rate among the evaluated AI methods on FML-bench-Lite and BioXArena. In a ten-condition ablation study, MN point estimates favor CAR over one-step proposal on both backbones, but no MN contrast survives correction for multiple comparisons. The results do not establish a consistent quality benefit from explicit operators beyond free-form iteration. CAR makes the sequence of operations and declared literature sources inspectable, separating judged idea quality from procedural traceability.

### 🤖 AI 总结

**一句话总结**：Large language models have been widely used to generate plausible research ideas, yet it remains unclear what makes automated ideation effective and how generated novel proposals arise from prior scie...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Ground, Iterate, Trace, Decomposing, Research, Ideation, Large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24887v1) | [下载PDF](https://arxiv.org/pdf/2611.24887v1.pdf)

---

## [6. General progress substitutes for specific training data in language models](https://arxiv.org/abs/2611.24844v1)

**作者**：Mark Marosi, Peter Antal  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-11-18

### 📄 论文摘要

Language models acquire their capabilities from training data, and developers withhold data during training to keep models from learning capabilities that could be misused. How long this delays a capability, and how much data is needed to acquire it later, is unknown. Here we show that the general progress a model makes on the rest of its training data substitutes for the data that was withheld. We withheld the training signal for individual skills in models of chess, Othello, molecular strings, bracket languages and web text. The delay of a withheld skill in larger models was predicted from smaller ones. A chess model never explicitly trained to respond to check ranked the legal responses almost as well as a model that was. When models were then trained on the withheld data, they acquired the skill with a small fraction of the data needed from initialization, and this fraction decreased as the models progressed. A control rule of equal difficulty was learned much more slowly. A programming language withheld from the training text of a 7-billion-parameter model was regained in the same way. Data filtering therefore delays a capability, and the data required to regain it decreases as models improve.

### 🤖 AI 总结

**一句话总结**：Language models acquire their capabilities from training data, and developers withhold data during training to keep models from learning capabilities that could be misused. How long this delays a capa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：General, progress, substitutes, specific, training, data, language, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24844v1) | [下载PDF](https://arxiv.org/pdf/2611.24844v1.pdf)

---

## [7. A Foundation Model to Measure and Predict Human Behaviour](https://arxiv.org/abs/2611.24830v1)

**作者**：Haoran Ye, Tianrui Huo, Hangzhen Li 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.HC  
**发布时间**：2026-11-18

### 📄 论文摘要

Large language models (LLMs) are increasingly used to infer psychological attributes, predict individual behaviour, and simulate human populations. However, despite generating plausible responses, they often misrepresent individuals and distort population statistics. Here we introduce Chiron, a foundation model to measure and predict human behaviour. We jointly fine-tune an LLM to represent psychological constructs, predict individual behaviour, and align population response distributions with human statistics. The training and evaluation data span 36 behavioural domains and 78 social science experiments, comprising 288,307 person records, 1,411,750 atomic behavioural decisions, and 99,953 psychometric assessments over 109 psychological constructs. In our evaluations, Chiron's psychological measurements agree more closely with human self-reports and exhibit fewer biases that undermine psychometric validity. It predicts individual behaviour more accurately than frontier LLMs (up to 28.4% relative improvement). In simulations of social science experiments, it more accurately captures the direction and magnitude of human experimental effects (82.2--94.3% lower effect-size estimation error). Together, these results establish Chiron as a unified computational instrument for measuring and predicting human behaviour.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly used to infer psychological attributes, predict individual behaviour, and simulate human populations. However, despite generating plausible responses, the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Foundation, Model, Measure, Predict, Human, Behaviour, Large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24830v1) | [下载PDF](https://arxiv.org/pdf/2611.24830v1.pdf)

---

## [8. On-Policy Morphing into Hybrid Attention Models](https://arxiv.org/abs/2611.24809v1)

**作者**：Disen Lan, Xuanda Wang, Jianbin Zheng 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-11-18

### 📄 论文摘要

Hybrid attention models combine full and linear attention to achieve a better quality--efficiency trade-off. Converting pretrained Transformers into such models requires identifying which layers should retain full attention under a prescribed budget. We identify two off-policy mismatches in FlashMorph's layer selection: (i) continuous branch interpolation and teacher-forced hidden states differ from discrete hybrid computation; and (ii) frozen model weights fail to account for parameter adaptation during subsequent recovery. We introduce FlashMorph2, an on-policy layer-selection method that (I) evaluates sampled discrete hybrid architectures end to end using their own hidden states, and (II) jointly optimizes layer-selection scores and model weights under the recovery objective to reflect post-adaptation performance. Experiments across Qwen3 model scales and linear-attention variants show that FlashMorph2 consistently outperforms existing layer-selection methods, improving average scores over FlashMorph by $+2.42$ points on RULER, $+1.08$ on LongBench, and $+0.76$ on recall-intensive tasks, while completing layer selection in only $0.72$--$3.57$ GPU hours across 0.6B--8B models, demonstrating high efficiency and scalability.

### 🤖 AI 总结

**一句话总结**：Hybrid attention models combine full and linear attention to achieve a better quality--efficiency trade-off. Converting pretrained Transformers into such models requires identifying which layers shoul...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：On-Policy, Morphing, Hybrid, Attention, Models, combine, full, linear

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24809v1) | [下载PDF](https://arxiv.org/pdf/2611.24809v1.pdf)

---

## cs.CV

## [9. Unified Law for Visual Tasks (The Four Laws of Computer Vision)](https://arxiv.org/abs/2611.24917v1)

**作者**：Sen Fang, Yalin Feng, Yancheng Zhang 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-18

### 📄 论文摘要

In this paper, we propose a Unified Law for Visual Tasks, which could be further divided into Four Laws of Computer Vision, with the goal of enabling a single framework or method to uniformly train on and perform nearly all visual tasks. Our starting point is an inspiration and hypothesis: if the world information is encoded into image, which we call World Snapshots, then image processing is world processing, and image generation is World Snapshot generation. Furthermore, if all visual and visualization tasks can be reformulated as generation tasks, then a unified method, World Snapshot Models (WSMs), can perform the vast majority of visual tasks, much as large language models have largely unified natural language processing. This paper validates these laws across more than 1,000 trained and evaluated visual tasks (defined by distinct input-output mappings) and presents a unified training framework for future visual-task research and applications.

### 🤖 AI 总结

**一句话总结**：In this paper, we propose a Unified Law for Visual Tasks, which could be further divided into Four Laws of Computer Vision, with the goal of enabling a single framework or method to uniformly train on...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Unified, Law, Visual, Tasks, Four, Laws, Computer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24917v1) | [下载PDF](https://arxiv.org/pdf/2611.24917v1.pdf)

---

## [10. PrismRestore: A Compact Restoration Toolbox for Agentic Image Restoration](https://arxiv.org/abs/2611.24915v1)

**作者**：Zhaocheng Yu, Kui Jiang, Jing Cao 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-18

### 📄 论文摘要

Agentic image restoration composes operations to handle mixed degradations, yet its toolbox often requires storing multiple restoration networks. We propose PrismRestore, which constructs a compact bank of callable restoration actions from a single frozen all-in-one model. Our approach builds on task-dependent yet overlapping channel responses in the shared model. An offline task-prior search uses activation and gradient statistics to group channels with similar response profiles, then searches task-specific modulation coefficients over non-representative channels while leaving representative channels unmodulated. The resulting prior bank enables explicit action selection and composition without additional restoration backbones or task-specific adapter modules. A state-conditioned policy learns to compose these actions using Group Relative Policy Optimization. Its objective separately normalizes fidelity and perceptual feedback within groups of trajectories sampled for the same input, and combines terminal evaluation with return-to-go derived from stepwise quality changes. Experiments on synthetic composite-degradation and real-world multi-task benchmarks show improvements over the evaluated all-in-one baselines and restoration quality competitive with multi-model agents. PrismRestore achieves these results with a single restoration backbone and faster inference than the evaluated agentic baselines.

### 🤖 AI 总结

**一句话总结**：Agentic image restoration composes operations to handle mixed degradations, yet its toolbox often requires storing multiple restoration networks. We propose PrismRestore, which constructs a compact ba...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PrismRestore, Compact, Restoration, Toolbox, Agentic, Image, composes, operations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24915v1) | [下载PDF](https://arxiv.org/pdf/2611.24915v1.pdf)

---

## [11. ShadowTransfer: A Geographic Transfer Benchmark for Overhead Shadow Detection](https://arxiv.org/abs/2611.24904v1)

**作者**：Shagun Mittal, Raymond A. Yeh, Satish Ukkusuri  
**分类**：cs.CV  
**发布时间**：2026-11-18

### 📄 论文摘要

Overhead aerial imagery feeds dense-prediction pipelines that are routinely trained in one geographic region and deployed in another, yet no benchmark measures how shadow detection models transfer across regions. Existing overhead shadow datasets either lack a geographic transfer protocol or rely on automatically generated labels. We introduce ShadowTransfer, a benchmark of 4,500 human-verified shadow masks across three U.S. cities at two native resolutions, paired with a leave-one-city-out evaluation protocol. Under vanilla training, holding out the test city costs 3.5 to 7.8 mIoU across four architectures, the gap remains significant when the training set grows from 225 to 900 images, and six of eight adaptation methods degrade more than vanilla training on average. We propose a three-probe framework that diagnoses where and how the transfer breaks: the failure operates in feature space, beyond the reach of pixel-histogram matching, shows up as a confidence collapse on shadow pixels while background confidence stays intact, and is recoverable by retraining different architectural components depending on the model: encoder for some, decoder for others. These findings replicate on INRIA building footprints, suggesting they describe geographic transfer beyond shadows. Guided by the diagnosis, we build Spectral Information Bottleneck (SIB), a plug-in module with one component per finding. Across the 9 (architecture, held-out city) cells, SIB has the smallest mean gap to the within-city upper bound of the ten methods we evaluate (6.42 mIoU), level with FDA. The benchmark, LOCO protocol, code, and trained models are released to support reproducible evaluation of geographic transfer in overhead dense prediction.

### 🤖 AI 总结

**一句话总结**：Overhead aerial imagery feeds dense-prediction pipelines that are routinely trained in one geographic region and deployed in another, yet no benchmark measures how shadow detection models transfer acr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ShadowTransfer, Geographic, Transfer, Benchmark, Overhead, Shadow, Detection, aerial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24904v1) | [下载PDF](https://arxiv.org/pdf/2611.24904v1.pdf)

---

## [12. Gaspard: Expressive unified speech and gesture synthesis with continuous autoregressive flow-matching and decoupled classifier-free guidance](https://arxiv.org/abs/2611.24862v1)

**作者**：Téo Guichoux, Théodor Lemerle, Catherine Pelachaud 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-18

### 📄 论文摘要

Human communication involves highly coordinated multimodal signals such as speech and co-speech gestures. Existing approaches for generating both modalities commonly follow a cascaded pipeline, where speech is generated first and subsequently used to drive gesture generation; speech generation is therefore independent of gestures. We introduce Gaspard, a unified speech--gesture generation model based on continuous autoregressive generation with next-step flow-matching predictions, and trained on Seamless Interaction, a large-scale multimodal dataset. The heterogeneous temporal properties of speech and gesture motivate modality-specific prediction heads and decoupled classifier-free guidance over the two generation streams. This guidance rebalances the influence of speech and gesture at inference time, improving expressivity while mitigating dynamics collapse in continuous autoregressive gesture generation. Objective and perceptual evaluations show that Gaspard is a strong gesture generation model against unimodal baselines and that it produces highly synchronous speech and gestures compared to a matched cascaded system.

### 🤖 AI 总结

**一句话总结**：Human communication involves highly coordinated multimodal signals such as speech and co-speech gestures. Existing approaches for generating both modalities commonly follow a cascaded pipeline, where ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Gaspard, Expressive, unified, speech, gesture, synthesis, continuous, autoregressive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24862v1) | [下载PDF](https://arxiv.org/pdf/2611.24862v1.pdf)

---

## [13. Does the Action Matter? Probing Action-Conditioned Semantic Forecasting as a World Model for Autonomous Driving](https://arxiv.org/abs/2611.24840v1)

**作者**：Binay Kumar Singh, Niels Da Vitoria Lobo  
**分类**：cs.CV, cs.AI, cs.LG, cs.RO  
**发布时间**：2026-11-18

### 📄 论文摘要

World models are increasingly used in autonomous driving to predict how a scene evolves under the ego vehicle's actions, supporting counterfactual reasoning and model-based planning. However, existing evaluations focus on prediction fidelity and planning performance, and rarely verify that the predictions depend on the conditioning action. In this paper, we study action dependence in action-conditioned semantic forecasting, which predicts future semantic segmentation from past segmentations and the ego action. We compare a forecaster with feature-wise and input-level action conditioning against an identical model without action input, and measure action dependence with test-time action interventions scored by standard segmentation metrics. The evaluation is validated in a synthetic environment with known action-dependent dynamics and applied to Cityscapes and BDD100K, both within each dataset and across the two vehicle platforms. Experiments show that the executed action improves mid-term mIoU by at most 2.5 points on Cityscapes and 0.6 points on BDD100K, whereas a wrong action reduces it by up to 23.2 and 7.0 points, below the model without action input. On real data, feature-wise conditioning depends 1.6 times more on the action than input-level conditioning at similar accuracy, whereas both depend on it equally in the synthetic environment, where the history does not determine the action. These results show that an accuracy gain indicates that a driving world model uses its action, but not how strongly its forecasts depend on it. Code is available at https://github.com/binayksingh/does-action-matter.

### 🤖 AI 总结

**一句话总结**：World models are increasingly used in autonomous driving to predict how a scene evolves under the ego vehicle's actions, supporting counterfactual reasoning and model-based planning. However, existing...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Does, Action, Matter?, Probing, Action-Conditioned, Semantic, Forecasting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24840v1) | [下载PDF](https://arxiv.org/pdf/2611.24840v1.pdf)

---

## [14. ReCoCo: From Patches to Compositions for Visual Representation Learning](https://arxiv.org/abs/2611.24806v1)

**作者**：Juan Gutiérrez, Saman Zadtootaghaj, José Luis Blanco-Murillo 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-18

### 📄 论文摘要

Self-supervised learning has produced powerful visual representations, yet learning strong dense features remains challenging. While consistency between augmented views provides strong image-level supervision, extending this principle to local visual content is less straightforward. Existing approaches often match individual patches across views or identify coherent regions, introducing uncertainties in correspondence estimation and assumptions about how visual content should be grouped. We introduce ReCoCo (Regional Composition Consistency), a principled approach that extends cross-view consistency to the regional level without requiring such correspondences or semantic grouping. ReCoCo represents the content shared between augmented views through compositions of their patch-level predictions over learned visual prototypes. By aligning these compositions, the model learns from regions containing multiple visual concepts without requiring them to be separated beforehand. ReCoCo integrates naturally with teacher-student self-distillation and introduces no additional learned parameters. Extensive experiments demonstrate substantial improvements in frozen-feature segmentation, clustering, and regional retrieval while maintaining competitive image-level recognition, alleviating the trade-off between dense and global representation quality.

### 🤖 AI 总结

**一句话总结**：Self-supervised learning has produced powerful visual representations, yet learning strong dense features remains challenging. While consistency between augmented views provides strong image-level sup...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ReCoCo, Patches, Compositions, Visual, Representation, Learning, Self-supervised, has

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24806v1) | [下载PDF](https://arxiv.org/pdf/2611.24806v1.pdf)

---

## [15. Edge-Efficient Joint RAW Image Compression and Restoration for Smart Wearable Devices](https://arxiv.org/abs/2611.24805v1)

**作者**：Yunong Sun, Sicheng Chen, Fei Xia  
**分类**：cs.CV  
**发布时间**：2026-11-18

### 📄 论文摘要

Smart wearable devices, such as augmented reality glasses, increasingly rely on cameras to understand and interact with their surroundings. However, their compact sensors often capture noisy RAW images, while limited compute and power make high-quality on-device restoration difficult. This creates an emerging need to reduce both local computation and transmission cost without sacrificing image quality. Two common solutions are to offload restoration or to compress the raw data before transmission. The first makes RAW transmission costly; the second reduces the payload but can spend bitrate preserving sensor noise. We address this fundamental mismatch with an asymmetric framework for joint RAW compression and restoration that directly optimizes the transmitted representation for clean image reconstruction. A lightweight on-device encoder compresses noisy RAW measurements into a bitstream, while a higher-capacity backend decoder jointly denoises and demosaics the encoded representation. We use knowledge distillation to train a smaller encoder for tighter compute budgets. Experiments on real and synthetic data show improved rate-restoration performance over strong cascaded compression-restoration pipelines and learned compression baselines. On SIDD, our method improves PSNR by more than 1.5 dB over cascaded baselines at approximately 0.25 bits per pixel. We further validate the method on real 12 MP RAW images captured with commercial smart glasses and measure sender-side latency on both smartphone and smart-glasses hardware. The distilled encoder achieves a 27.6$\times$ NPU inference speedup over on-device NAFNet for 256$\times$256 output patches. The code is available at https://github.com/coolsyn2000/CRAW

### 🤖 AI 总结

**一句话总结**：Smart wearable devices, such as augmented reality glasses, increasingly rely on cameras to understand and interact with their surroundings. However, their compact sensors often capture noisy RAW image...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Edge-Efficient, Joint, RAW, Image, Compression, Restoration, Smart, Wearable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24805v1) | [下载PDF](https://arxiv.org/pdf/2611.24805v1.pdf)

---

## [16. Ultimate3D: Teaching Multimodal LLMs 3D Camera-Object Relations by Large-Scale Visual Instruction Data](https://arxiv.org/abs/2611.24795v1)

**作者**：Liu He, Yizhi Song, Ruiqi Xu 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-18

### 📄 论文摘要

Multimodal Large Language Models (MLLMs) struggle with accurately capturing camera-object relations, especially for object orientation, camera viewpoint, and camera shots. This stems from the fact that existing MLLMs are trained on images with limited diverse camera-object relations and corresponding textual descriptions. To address this, we propose a synthetic generation pipeline to create large-scale 3D visual instruction datasets. Our framework takes 3D assets as input and uses rendering and diffusion-based image generation models to create photorealistic images preserving precise camera-object relations. Additionally, large language models (LLMs) are used to generate text prompts for guiding visual instruction tuning and controlling image generation. We create Ultimate3D, a large-scale 3D-grounded 2D visual instruction dataset. Ultimate3D consists of 240K VQAs with precise camera-object annotations, and corresponding benchmark. MLLMs fine-tuned on our proposed dataset outperform commercial models by a large margin, achieving an average accuracy improvement of 29.7% on camera-object relation recognition tasks. Our code, dataset, and benchmark will contribute to broad MLLM applications.

### 🤖 AI 总结

**一句话总结**：Multimodal Large Language Models (MLLMs) struggle with accurately capturing camera-object relations, especially for object orientation, camera viewpoint, and camera shots. This stems from the fact tha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, 3D, Ultimate3D, Teaching, Multimodal, Camera-Object, Relations, Large-Scale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24795v1) | [下载PDF](https://arxiv.org/pdf/2611.24795v1.pdf)

---

## [17. Training-free motion statistics match self-supervised behavior encoders](https://arxiv.org/abs/2611.24792v1)

**作者**：Ziwen Chen  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-18

### 📄 论文摘要

Self-supervised encoders for animal behavior are often trained on, or fed, hand-built movement features. We ask whether they beat those ingredients when compared fairly. A training-free representation, made of generic per-frame measurements summarized over fixed time windows and reduced with PCA, is compared with retrained and released encoders (BAMS, hBehaveMAE) under a preregistered protocol: frozen representations of equal size and one shared classifier. On CalMS21 it reaches 85.8 macro F1 against 82.4 for the best encoder, ties with four labelled videos, and leads when the annotator changes or new behaviors must be learned from a few videos; the reading holds for encoders retrained with three seeds. On the MABe22 mouse triplets it scores 83.7 against 80.3 for the released hBehaveMAE (gap +3.4, 95% interval +2.1 to +4.7). On a second species, the MABe22 fly groups, the same recipe scores 51.6 mean F1 over 50 tasks against 48.2 for BAMS, the best published method. On Shot7M2, the synthetic basketball benchmark built by hBehaveMAE's authors, it scores 68.8 against 64.7 for hBehaveMAE, the best method in that paper, though hBehaveMAE remains better on the shortest movements. Short time windows carry most of the result. Raw keypoints in each body's own frame, summarized over the same windows, already match or beat the encoders on both mouse datasets and on Shot7M2; on the fly groups they fall short, and the measurements add 5.3 points. On these benchmarks, current behavior encoders have yet to beat the hand-built features they learn from, and such baselines should be reported alongside them.

### 🤖 AI 总结

**一句话总结**：Self-supervised encoders for animal behavior are often trained on, or fed, hand-built movement features. We ask whether they beat those ingredients when compared fairly. A training-free representation...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Training-free, motion, statistics, match, self-supervised, behavior, encoders, animal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24792v1) | [下载PDF](https://arxiv.org/pdf/2611.24792v1.pdf)

---

## cs.LG

## [18. Equivariant Modeling with Polynomial Features via Minimal Homogeneous Generators](https://arxiv.org/abs/2611.24896v1)

**作者**：Michael Liaofan Liu, Joe Kileel  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-11-18

### 📄 论文摘要

We present a general framework for modeling and learning equivariant functions between finite dimensional semisimple real group representations, unifying constructions developed across many application areas. Our model is a linear combination of equivariant polynomial features whose coefficients are arbitrary learnable functions of invariant polynomial features. We take as features minimal homogeneous generators for the invariant algebra and the covariant module over the invariant algebra, up to prescribed degrees. We provide a Python package that automatically computes these features and fits the resulting models to training data. The algorithm for feature computation requires explicit isotypic decompositions of the input and output representations, along with explicit Clebsch-Gordan decompositions of the tensor product of irreducible representations, and achieves speedups over alternative methods in computational algebra. Numerical experiments in scientific modeling demonstrate the full learning pipeline and yield accurate predictors with few trainable parameters, using the model both for end-to-end prediction and within layers of larger architectures.

### 🤖 AI 总结

**一句话总结**：We present a general framework for modeling and learning equivariant functions between finite dimensional semisimple real group representations, unifying constructions developed across many applicatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Equivariant, Modeling, Polynomial, Features, via, Minimal, Homogeneous, Generators

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24896v1) | [下载PDF](https://arxiv.org/pdf/2611.24896v1.pdf)

---

## [19. Cap-and-Track: Optimizing LLM Inference Request Dispatch Across Shifting Capacity](https://arxiv.org/abs/2611.24891v1)

**作者**：Benjamin Novotny, Doug Szeto, Chang Wang 等 9 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-18

### 📄 论文摘要

A fixed dispatch rate for LLM inference becomes stale as serving fleets resize and request sizes change. Generative output length is unknown at admission, and shared provider pools can lose capacity. We present Cap-and-Track, a design for asynchronous inference across provider capacity and internal GPUs. Meta's traffic shaper implements Cap-and-Track for post and live-video understanding. Refusals signal the backend's current admission ceiling. Durable priority queues hold excess work outside execution, including refused requests for retry. Cap is a fail-fast admission check at the saturated resource that refuses work before a long wait. Using only those refusals, the Track dispatcher probes upward and backs off. It follows the ceiling without output-length prediction or a fleet-level rate to retune. In a concurrent same-traffic production A/B, the shaper ran per-replica Cap plus Track. It served a classifier on 43% fewer H100s than its queued, fixed-rate precursor, though lower-priority work waited longer at backfill peaks. In steady-capacity real-engine replay, Track ran within 1% of the goodput of a fixed rate tuned above measured capacity, with about a quarter of that rate's refusal share. The shaper carries more than 300 million online requests and hundreds of terabytes of media a day. During a backfill, it handled 1.1 billion requests in its busiest 24 hours. Lessons include keeping queues inside inference engines just long enough to fill batches, steering dispatch by capacity refusals alone, keeping dispatch stateful, and sizing fleets by how long low-priority work can wait.

### 🤖 AI 总结

**一句话总结**：A fixed dispatch rate for LLM inference becomes stale as serving fleets resize and request sizes change. Generative output length is unknown at admission, and shared provider pools can lose capacity. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Cap-and-Track, Optimizing, Inference, Request, Dispatch, Across, Shifting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24891v1) | [下载PDF](https://arxiv.org/pdf/2611.24891v1.pdf)

---

## [20. Monoculture Robust Learning](https://arxiv.org/abs/2611.24881v1)

**作者**：Lee Cohen, Jon Kleinberg, Omer Reingold  
**分类**：cs.LG  
**发布时间**：2026-11-18

### 📄 论文摘要

We introduce a notion of monoculture robustness in Probably Approximately Correct (PAC) learning, as a way to mitigate the problem of algorithmic monoculture (Kleinberg and Raghavan, 2021): the tendency of models sharing the same components (e.g., training data) to fail on the same inputs. Specifically, we ask whether a learner with access to a single dataset can output $k$ individually accurate hypotheses whose joint failure probability is comparable to training on $k$ independent datasets. We say that such a learning procedure achieves monoculture robustness, and we quantify this by bounding the conjunctive error that all $k$ hypotheses misclassify points in an individual sense. We design methods for achieving this type of guarantee by drawing a surprising connection between replicability (Impagliazzo et al., 2022) and monoculture robustness. Specifically, we show that if the base learner is $ρ$-replicable, then running it independently $k$ times on the same sample yields individual monoculture error that shrinks exponentially with $k$, controlled by the single-run error of the base learner at the point and $ρ$. We complement these positive results with a lower bound: for individual monoculture robustness, we prove a worst-case lower bound showing that, for learners, driving the individual conjunctive error down to $γ$ can require a sample-size multiplier of $t = Ω(\log(1/γ))$.

### 🤖 AI 总结

**一句话总结**：We introduce a notion of monoculture robustness in Probably Approximately Correct (PAC) learning, as a way to mitigate the problem of algorithmic monoculture (Kleinberg and Raghavan, 2021): the tenden...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, of, Monoculture, Robust, Learning, introduce, notion, robustness

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24881v1) | [下载PDF](https://arxiv.org/pdf/2611.24881v1.pdf)

---

## [21. Auditing black-box clinical prediction models with a large language model through queries alone: a blinded test with planted flaws](https://arxiv.org/abs/2611.24877v1)

**作者**：Zhiyu Liu, Xinyu Yang  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-18

### 📄 论文摘要

Large language models (LLMs) are used to explain clinical prediction models, on the promise that they can say what a model computes, find its faults and even reveal new knowledge in it. We tested the three promises where the answers could be checked. From the International Stroke Trial we trained four kinds of model (logistic regression, explainable boosting machine, gradient-boosted trees, neural network) for two outcomes on patients randomised earlier, planted one flaw in each of 24 copies (an under-predicted subgroup, a reversed risk factor or an implausible step) and mixed them with the 8 clean models. GPT-6 Astra audited each model three times, blind, through a tool that only returned the model's predictions; the judging rules were committed before any run and applied by program. Its surrogate models, with a median of 128 terms, reproduced the audited models' log-odds with a mean $R^2$ of 0.976 (0.959 for an additive surrogate of 42 terms fitted by an analyst). It found the planted flaw in 69 of 72 runs (96%; 95% CI 80% to 99%); a script written for the purpose found all 24. It also reported many more problems: 60% of 1,089 checkable reports failed the pre-specified check against the model's average behaviour; post hoc, most of these were real but small steps, and 15% of the checkable reports were not found in the model. Of 601 unexpected relationships it read out of the clean models, 11% held in patients randomised later (random pairs 6%; a regression scan's shorter list of its strongest candidates, 28%); after a check on the training data, 33% against 30%. With query access alone, an LLM can describe a black-box model faithfully and find nearly every planted flaw, as a purpose-written script also did; its reports of problems must be checked on the model and its discoveries on data.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are used to explain clinical prediction models, on the promise that they can say what a model computes, find its faults and even reveal new knowledge in it. We tested the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Auditing, black-box, clinical, prediction, models, large, language, model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24877v1) | [下载PDF](https://arxiv.org/pdf/2611.24877v1.pdf)

---

## [22. TangentPDE: Learning Local Operator Responses with Sparse Finite-Difference Supervision](https://arxiv.org/abs/2611.24873v1)

**作者**：Xinjian Xie, Ruxuan Chen, Jiashu Li 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-18

### 📄 论文摘要

Neural PDE operators are often optimized through state reconstruction, which largely constrains operator values at observed inputs but does not fully characterize their sensitivity to local perturbations. A more faithful approximation of operator behavior requires not only accurate state predictions, but also correct variations along local perturbation directions. We present TangentPDE, which uses finite differences to approximate directional derivatives and constructs task-relevant finite-step responses from the state outputs of a reference solver at sparse paired inputs. Its objective jointly constrains state fidelity, response-direction alignment, and response-magnitude calibration, thereby learning both operator values and their local variations. Because the response labels are constructed solely from state outputs at paired inputs, the method requires neither explicit derivative labels, linearized or adjoint PDE solves, nor full Jacobians, and remains applicable to nonlinear solvers without derivative interfaces. Building on this, we additionally propose a selectively executed adaptation mechanism to strengthen local operator representations under finite-difference supervision. Budget-matched and correspondence-perturbed controls isolate the effect of relational supervision from improvements attributable to additional state observations or increased data volume. Designed as a plug-and-play training framework, TangentPDE integrates with diverse neural-operator backbones. Across four PDE systems and 20 task-backbone settings, TangentPDE lowers the three-seed mean state error in 18 settings and the corresponding Rollout@20 error in 18, while intrinsic finite-step response gains are strongest on DiffReact and remain task- and backbone-dependent elsewhere.

### 🤖 AI 总结

**一句话总结**：Neural PDE operators are often optimized through state reconstruction, which largely constrains operator values at observed inputs but does not fully characterize their sensitivity to local perturbati...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TangentPDE, Learning, Local, Operator, Responses, Sparse, Finite-Difference, Supervision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24873v1) | [下载PDF](https://arxiv.org/pdf/2611.24873v1.pdf)

---

## [23. Measuring and Improving Transfer of Neural Surrogates for Vehicle Aerodynamics](https://arxiv.org/abs/2611.24843v1)

**作者**：Favour Nerrise, Julian Busch, Gurpreet Singh Hora 等 6 位作者  
**分类**：cs.LG, physics.flu-dyn  
**发布时间**：2026-11-18

### 📄 论文摘要

Neural surrogates for external vehicle aerodynamics are fast alternatives to physics-based computational fluid dynamics (CFD) simulations. Their foundational limitation is a lack of zero-shot generalization across vehicle classes, which results in an expensive, custom training campaign for each new vehicle design. Similar to pretrained models in other fields, a pretrained surrogate should adapt to a new vehicle class using only a few simulations and stay accurate on its pretraining domain. No prior study has systematically tested this transfer behavior. We conduct a large-scale, controlled benchmarking study on five DrivAerML-pretrained surrogates across four independent target datasets. These datasets differ from the source in geometry, CFD solver, turbulence model, and flow conditions. We find that fine-tuning these surrogates outperforms training from scratch in fewer than half of the comparisons and lowers the accuracy of the surrogate on its source dataset. We introduce GeoReplay, a geometry- and gradient-aligned source replay that keeps source simulations resembling the target in training and applies their updates only when they agree with the target gradient. A risk bound separates geometric coverage from differences in the simulated physics, and we prove that every sufficiently small GeoReplay step decreases the target training objective. GeoReplay lowers the source error of fine-tuning in 77 of 80 settings and matches its target accuracy.

### 🤖 AI 总结

**一句话总结**：Neural surrogates for external vehicle aerodynamics are fast alternatives to physics-based computational fluid dynamics (CFD) simulations. Their foundational limitation is a lack of zero-shot generali...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Measuring, Improving, Transfer, Neural, Surrogates, Vehicle, Aerodynamics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24843v1) | [下载PDF](https://arxiv.org/pdf/2611.24843v1.pdf)

---

## [24. What Survival Benchmarks Don't Tell You: Impact of Model Selection and Dataset Regimes](https://arxiv.org/abs/2611.24837v1)

**作者**：Sandra Dening, Emre Kavak, Christian Wachinger 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-18

### 📄 论文摘要

Despite the proliferation of survival analysis methods, current benchmarks often operate under narrow conditions: they heavily rely on the concordance index (C-index) for evaluation and model selection, and frequently either exclude deep learning (DL) methods or underrepresent challenging dataset regimes. To address these limitations, we conduct a large-scale, neutral benchmark comparing 10 classical, tree-based, and DL methods across 49 diverse datasets. Crucially, we treat the model selection criterion (optimizing for C-index, Integrated Brier Score (IBS), or Mean Absolute Error (MAE-PO)) as an independent experimental variable. Using Bayesian mixed-effects modeling, we demonstrate that evaluation design heavily dictates conclusions. For complex DL and tree-based architectures, selecting hyperparameters to optimize for IBS instead of C-index yields substantial improvements in probabilistic accuracy and calibration at a negligible cost to discriminative ranking. Furthermore, method performance (C-index, IBS, MAE-PO, and X-CAL) is fundamentally governed by dataset characteristics. While DL models scale exceptionally well with larger sample sizes, they suffer notable performance drops in high-dimensional feature spaces. Additionally, we expose a structural vulnerability where heavy censoring artificially inflates absolute calibration metrics, creating overly conservative tests. Ultimately, our findings challenge the utility of global single-number performance summaries and advocate for survival analysis results that transparently report the evaluation setup. Our code is available at: https://github.com/sdening/surv-bench-study

### 🤖 AI 总结

**一句话总结**：Despite the proliferation of survival analysis methods, current benchmarks often operate under narrow conditions: they heavily rely on the concordance index (C-index) for evaluation and model selectio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, What, Survival, Benchmarks, Don't, Tell, Impact, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24837v1) | [下载PDF](https://arxiv.org/pdf/2611.24837v1.pdf)

---

## [25. Overlooked and Underutilized: Prototypes are the Missing Piece in Tabular XAI](https://arxiv.org/abs/2611.24831v1)

**作者**：Jacek Karolczak, Jerzy Stefanowski  
**分类**：cs.LG, cs.HC  
**发布时间**：2026-11-18

### 📄 论文摘要

Explainable AI (XAI) is frequently applied to high-stakes tabular data, yet the field relies heavily on feature attribution methods. While these approaches offer technical transparency, evaluating dozens of isolated features demands excessive cognitive effort from non-expert users. In this paper, we argue that prototypes remain overlooked and underutilized, and should be integrated as a complementary, intuitive gateway to auditing complex machine learning models. Although entire exemplars function as an intuitive baseline for prototype-based explanations, we highlight prototypical parts as particularly valuable for tabular data. By grouping related features into bounded subspaces, prototypical parts technically embody human-understandable concepts, replacing isolated features with cohesive semantic units. We support this integration through two primary lenses. Cognitively, these parts align with Rosch's categorization theory and Kahneman's System 1 thinking to naturally reduce cognitive load for humans. Then, we introduce a Geometric Validity Triad to conceptualize why prototypes validate the data manifold - a critical dimension often neglected by existing methods. We contend that making tabular XAI genuinely comprehensible requires shifting toward composite explanation pipelines that pair intuitive similarity-based reasoning with rigorous feature-level auditing. The paper concludes by outlining open challenges of prototype-based methods and discussing potential solutions to guide future research.

### 🤖 AI 总结

**一句话总结**：Explainable AI (XAI) is frequently applied to high-stakes tabular data, yet the field relies heavily on feature attribution methods. While these approaches offer technical transparency, evaluating doz...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Overlooked, Underutilized, Prototypes, Missing, Piece, Tabular, XAI, Explainable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24831v1) | [下载PDF](https://arxiv.org/pdf/2611.24831v1.pdf)

---

## [26. Synthesizing hyperspectral Data using generative Models to train spectral Unmixing Methods for low-cost Crop Residue Cover Mapping](https://arxiv.org/abs/2611.24827v1)

**作者**：Ege Artan, Shuo Chen, Andrew Peng 等 5 位作者  
**分类**：cs.LG, cs.CV, eess.SP  
**发布时间**：2026-11-18

### 📄 论文摘要

The spectral range of the Field Imaging Nanosatellite for Crop residue Hyperspectral Mapping (FINCH), developed by the University of Toronto Aerospace Team's Space System Division, poses significant challenges for hyperspectral unmixing to determine crop residue cover fractional abundances. The severe lack of standard indices necessitates the use of complex, data-driven unmixing models. Complex unmixing models require dense, well-distributed manifolds, whereas ground-truth datasets are sparse and expensive. To better leverage the information content in existing ground-truth datasets, this study presents a framework that decouples interpolation and abundance-mapping estimation via an intermediary conditional data generator, contrasting with traditional single-model unmixing pipelines. This decoupling enables the inclusion of physical prior knowledge about spectra, which is not natively accessible to unmixing models, thereby artificially expanding the dataset to serve as a Monte Carlo approximation of the population risk. To test this hypothesis, we have proposed two generator models: a 1D Conditional U-Net with Conformer Layers (GD-Streamline) and a Dual-Path Transformer Conditional Variational AutoEncoder (TCVAE), and two unmixing models: Multi-Layered Perceptrons (MLP) and Fourier Neural Operators (FNO). The results of the study indicate a need for rigorous integration and introduction of spectral priors within the scope of the proposed decoupling framework to prevent domain and mode collapse and hallucination by the generator models; otherwise, this leads to falsely approximated data manifolds, ultimately resulting in unsatisfactory and out-of-distribution unmixing performance.

### 🤖 AI 总结

**一句话总结**：The spectral range of the Field Imaging Nanosatellite for Crop residue Hyperspectral Mapping (FINCH), developed by the University of Toronto Aerospace Team's Space System Division, poses significant c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Synthesizing, hyperspectral, Data, generative, Models, train, spectral, Unmixing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24827v1) | [下载PDF](https://arxiv.org/pdf/2611.24827v1.pdf)

---

## [27. Prognosis Without Prediction: The Intrinsic Geometry of Survival](https://arxiv.org/abs/2611.24799v1)

**作者**：Atahan Karagoz  
**分类**：cs.LG, q-bio.QM  
**发布时间**：2026-11-18

### 📄 论文摘要

Modeling systemic failure in high-dimensional environments is fundamentally limited by supervised algorithms that attempt to predict sparse, noisy or censored endpoints. To break this reliance on explicit outcome regression, we engineered the Self-Organizing Survival Manifolds (SOSM) framework, a deep learning architecture that decouples unsupervised representation learning from survival labels and treats time-to-event progression as an emergent geometric property. The system projects heterogeneous multi-omics arrays into a unified latent space governed by a pseudotime-weighted, curvature-minimizing graph Laplacian, organizing patient trajectories along low-dissipation geodesic flows. To validate the framework, we applied this architecture to a 184-patient clear cell renal cell carcinoma multi-omics cohort. Across a deterministic 5-fold cross-validation pipeline, SOSM achieved a mean Concordance Index of $0.768 \pm 0.068$, while out-of-fold risk stratification yielded significant survival divergence (log-rank $p < 0.001$) accompanied by a 14.7% increase in local manifold dissipation among high-risk patients. Furthermore, interrogating the network's encoder weights confirmed that the model autonomously recovered canonical metabolic and microenvironmental drivers of disease progression without supervised feature selection. By demonstrating that systemic failure can be mapped as a geometric phase transition, SOSM establishes a generalizable computational engine for prognostic modeling across biological, industrial and financial complex systems.

### 🤖 AI 总结

**一句话总结**：Modeling systemic failure in high-dimensional environments is fundamentally limited by supervised algorithms that attempt to predict sparse, noisy or censored endpoints. To break this reliance on expl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Prognosis, Without, Prediction, Intrinsic, Geometry, Survival, Modeling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24799v1) | [下载PDF](https://arxiv.org/pdf/2611.24799v1.pdf)

---

## [28. Bias-Only Training Dynamics in ReLU Networks](https://arxiv.org/abs/2611.24797v1)

**作者**：Shreyas Chaudhari, Jose M. F. Moura  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-18

### 📄 论文摘要

Neural networks with randomly initialized, fixed weights and trainable biases are universal approximators, yet the dynamics of bias-only training remain largely unexplored. We study these dynamics in one-hidden-layer ReLU networks through activation codes, the binary patterns of active neurons that partition the input space into convex polyhedral regions. We show that the gradients with respect to the biases depend on each input only through its activation code, and hence the training dynamics can be characterized with these codes. In particular, as long as the activation codes remain fixed, training reduces to a linear least-squares problem with the codes as features. Training can then be understood as a sequence of least-squares problems, with transitions occurring when neurons change their activation states. We show that the fraction of switching neurons vanishes as the network widens, and the training dynamics approach those of linear least squares on the initial activation codes in the infinite-width limit. Our experiments support these theoretical findings, showing that while activation switches can noticeably affect training in narrower networks, their relative frequency and the associated changes in the dynamics diminish as the width increases.

### 🤖 AI 总结

**一句话总结**：Neural networks with randomly initialized, fixed weights and trainable biases are universal approximators, yet the dynamics of bias-only training remain largely unexplored. We study these dynamics in ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bias-Only, Training, Dynamics, ReLU, Networks, Neural, randomly, initialized

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24797v1) | [下载PDF](https://arxiv.org/pdf/2611.24797v1.pdf)

---

## [29. Learning Trajectories Leave Decodable Traces in Neural Network Weight Space and Internal Representations](https://arxiv.org/abs/2611.24782v1)

**作者**：Patrick Krauss, Achim Schilling, Andreas Maier 等 5 位作者  
**分类**：cs.LG, cs.AI, q-bio.NC  
**发布时间**：2026-11-18

### 📄 论文摘要

Neural networks trained on the same task develop related weight-space structures, yet remain distinguishable after learning. Do these differences merely reflect alternative solutions, or do they preserve information about individual learning histories? We tested whether final weights reveal initialization, task order, and earlier trajectory states. Training reorganized the ensemble: initial pairwise distances did not consistently predict final distances. Nevertheless, all 30 trained networks were correctly matched to their initial weights among ten candidates per dataset. Networks sharing an initialization also developed recognizable final hidden representations across different batch schedules, although direct comparisons with initial activity did not recover identity. Learning order remained readable as well. A linear probe decoded the order of two earlier tasks with 100% accuracy on 80 held-out networks after ten epochs of a common final task. Earlier intermediate weight states were partly predictable, but individual initial weights could not be reliably reconstructed. Final weights thus retain selective historical information rather than a complete trajectory record. Perturbed networks recovered classification performance without returning to their unperturbed training paths. This separation persisted across datasets, intervention times, and network layers. Moreover, 2,157 of 2,160 aligned endpoint pairs showed no positive loss barrier at sampled interpolation points, indicating low-loss connections between distinct solutions rather than convergence to one weight vector. Together, these findings show that a shared task constrains networks to related successful solutions without erasing their individual histories. Final weights reflect not only what a network has learned, but also where learning began and how it unfolded.

### 🤖 AI 总结

**一句话总结**：Neural networks trained on the same task develop related weight-space structures, yet remain distinguishable after learning. Do these differences merely reflect alternative solutions, or do they prese...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Trajectories, Leave, Decodable, Traces, Neural, Network, Weight

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24782v1) | [下载PDF](https://arxiv.org/pdf/2611.24782v1.pdf)

---

## [30. Reconstruction vs. Prediction Pre-Training of Discrete Video Representations for Continuous Control](https://arxiv.org/abs/2611.24781v1)

**作者**：Ron Kosova, Francesco Croce  
**分类**：cs.LG  
**发布时间**：2026-11-18

### 📄 论文摘要

Self-supervised video encoders are commonly trained to either reconstruct pixels or predict latent features, yet it remains unclear how these objectives shape representations for downstream dynamics. We present a capacity-matched study isolating this choice: two identical video encoders with a shared FSQ bottleneck are trained under autoencoding and V-JEPA objectives on a continuous control environment. We introduce a simple asymmetric discretization scheme to apply the same bottleneck to the predictive model. The resulting representations exhibit a clear trade-off: the autoencoder preserves substantially more physical state information and achieves slightly better one-step latent prediction, while the predictive encoder accumulates less error under autoregressive rollout. Structural probes suggest that this advantage is associated with greater robustness to low-level visual perturbations and stronger dependence on temporal context. These results indicate that predictive and reconstructive objectives induce distinct representations of dynamics, trading state fidelity for properties that may benefit long-horizon prediction.

### 🤖 AI 总结

**一句话总结**：Self-supervised video encoders are commonly trained to either reconstruct pixels or predict latent features, yet it remains unclear how these objectives shape representations for downstream dynamics. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：vs, of, Reconstruction, Prediction, Pre-Training, Discrete, Video, Representations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.24781v1) | [下载PDF](https://arxiv.org/pdf/2611.24781v1.pdf)

---

