# arXiv AI 论文日报 | 2026-06-16

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (4 篇)
- [cs.CV](#csCV) (8 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.AI](#csAI) (8 篇)

---

## cs.AI

## [1. Bayesian Inference and Decision Audits for Public Archives of Frontier AI Evaluations](https://arxiv.org/abs/2606.17005v1)

**作者**：Yanan Long  
**分类**：cs.AI, stat.ME  
**发布时间**：2026-06-15

### 📄 论文摘要

Public AI evaluations are often read as terminal leaderboards, yet the underlying evidence is a selective time series shaped by reporting rules, benchmark revisions, and missingness. Repeated public archives for LiveBench and Open LLM Leaderboard v2 serve as the primary longitudinal record; LMArena provides a preference stress test; and GAIA and tau-bench contribute limited agentic pilots. Together, these archives instantiate a Bayesian inference problem: under a fixed reporting convention, one constructed terminal-only example over $1{,}000$ systems is compatible with two pre-terminal histories, yielding times of $23.03$ or $75.13$ to reach within $0.05$ of the ceiling under the same terminal-tail model. In synthetic posterior comparisons, action-facing diagnostics differ across observation regimes. The candidate selection-aware frontier model fails synthetic recovery, objective-archive prediction, preference transfer, and uncertainty calibration; correspondingly, fixed audit gates reject its stronger claims. An archive-and-adjudication protocol reconstructs public evaluation histories, isolates a verified timing boundary, and falsifies unsupported frontier claims.

### 🤖 AI 总结

**一句话总结**：Public AI evaluations are often read as terminal leaderboards, yet the underlying evidence is a selective time series shaped by reporting rules, benchmark revisions, and missingness. Repeated public a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Bayesian, Inference, Decision, Audits, Public, Archives, Frontier

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17005v1) | [下载PDF](https://arxiv.org/pdf/2606.17005v1.pdf)

---

## [2. When in Doubt, Plan It Out: Committed Small Language Model Deliberation for Reactive Reinforcement Learning](https://arxiv.org/abs/2606.16995v1)

**作者**：Nathan Gavenski, Juarez Monteiro, Francisco Galuppo 等 5 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-06-15

### 📄 论文摘要

Reinforcement Learning (RL) policies often degrade in unfamiliar environments because they lack explicit deliberation. We propose Plan, Align, Commit, Think (PACT), a hybrid architecture that combines a fast, reactive RL policy with a slow, deliberative Small Language Model (SLM) planner. PACT invokes the SLM asynchronously to generate and validate candidate action plans. Once a plan is verified through simulation as safe, feasible, and complete, it is executed directly, bypassing the RL policy without retraining or modifying it. Evaluated on three FrozenLake configurations of increasing difficulty, PACT outperforms all baselines while relying on a 2B-parameter SLM backbone, suggesting that deliberative planning and reactive execution are more powerful in concert than either is alone in these settings.

### 🤖 AI 总结

**一句话总结**：Reinforcement Learning (RL) policies often degrade in unfamiliar environments because they lack explicit deliberation. We propose Plan, Align, Commit, Think (PACT), a hybrid architecture that combines...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：It, When, Doubt, Plan, Out, Committed, Small, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16995v1) | [下载PDF](https://arxiv.org/pdf/2606.16995v1.pdf)

---

## [3. Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Schedule Code Classification](https://arxiv.org/abs/2606.16987v1)

**作者**：Truong Thanh Hung Nguyen, Khanh Van Quynh Nguyen, Hoang-Loc Cao 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-15

### 📄 论文摘要

Accurate Harmonized Tariff Schedule (HTS) code classification is essential for customs clearance, duty assessment, trade statistics, and regulatory compliance in maritime logistics. However, exact HTS classification remains challenging because product descriptions are often short, incomplete, or ambiguous, while correct classification depends on hierarchical tariff structures, legal notes, and jurisdiction-specific rules. This paper proposes an agentic large language model (LLM) framework for Canadian 10-digit HTS code classification in smart-port and maritime logistics environments. The framework integrates multi-agent information retrieval, semantic retrieval over official tariff documents, evidence-grounded reasoning, consensus-based validation, element-wise voting across hierarchical code components, confidence estimation, and human-in-the-loop escalation. We evaluate the framework on a private dataset of 3,300 domain-expert-labeled product records collected from logistics and delivery contexts. Experimental results show that exact 10-digit classification remains difficult even for advanced LLMs, with performance decreasing from coarse chapter-level prediction to fine-grained tariff and statistical suffix assignment. These findings demonstrate the need for evidence-grounded, uncertainty-aware, and human-centered classification workflows rather than fully autonomous single-step prediction. The proposed framework supports more interpretable, accountable, and compliance-oriented HTS classification for maritime logistics and smart-port operations. Our code is available at https://github.com/Analytics-Everywhere-Lab/hts.

### 🤖 AI 总结

**一句话总结**：Accurate Harmonized Tariff Schedule (HTS) code classification is essential for customs clearance, duty assessment, trade statistics, and regulatory compliance in maritime logistics. However, exact HTS...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Consensus-based, Agentic, Large, Language, Model, Framework, Harmonized, Tariff

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16987v1) | [下载PDF](https://arxiv.org/pdf/2606.16987v1.pdf)

---

## [4. The embrace of open science: An analysis of a decade of AI research and 56 800 conference papers](https://arxiv.org/abs/2606.16974v1)

**作者**：Kevin L Coakley, Thijs Snelleman, Holger Hoos 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-15

### 📄 论文摘要

The reproducibility crisis has directed the AI research community toward improving documentation practices. Several studies have identified methodological issues, and in response, the most impactful venues in the field have introduced reproducibility checklists. We seek to understand whether documentation practices have changed over time by assessing all published papers at five leading AI conferences over the past decade. Seven reproducibility variables were identified, quality-assured and used to analyse 56 800 publications. Our analysis reveals that in the period 2014 to 2024, documentation practices have improved; papers sharing both code and data increased nearly sixfold, from 11% to 64% Building on empirical reproducibility rates from a prior study, we estimate - inferred from documentation practices, not direct testing - that reproducibility increased from 28% in 2014 to 64% in 2024. Improvements in documentation practices predate the introduction of reproducibility checklists, suggesting these changes reflect a broader movement toward open science rather than a direct response to formal requirements.

### 🤖 AI 总结

**一句话总结**：The reproducibility crisis has directed the AI research community toward improving documentation practices. Several studies have identified methodological issues, and in response, the most impactful v...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, An, embrace, open, science, analysis, decade, research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16974v1) | [下载PDF](https://arxiv.org/pdf/2606.16974v1.pdf)

---

## [5. A Causal Model of Theory of Mind in Conflict for Artificial Intelligence](https://arxiv.org/abs/2606.16944v1)

**作者**：Nikolos Gurney  
**分类**：cs.AI, cs.HC  
**发布时间**：2026-06-15

### 📄 论文摘要

Theory of mind (ToM), the capacity to ascribe mental states to others and use those ascriptions for prediction and inference, is widely assumed to be essential for effective human-machine integration. Existing AI-ToM models address \emph{how} to mentalize, but leave the question of when largely unaddressed. The central question is: under what situational and agent-level conditions is ToM engagement causally warranted in conflict? This paper presents a structural causal model formalized as a directed acyclic graph (DAG), treating ToM as a mechanism activated by situational and agent-level conditions rather than as an always-on capacity. The model specifies four exogenous variables capturing situational and agent-level conditions, five endogenous mediators, and a mechanistic ToM node producing engagement states through three distinct causal pathways: a tractability pathway, a reasoning-depth pathway, and an enabling-cause pathway. The primary outcome is epistemic accuracy, which decouples social reasoning from behavioral policy and generalizes across social phenomena beyond conflict. The framework gives AI systems a principled, resource-rational decision procedure for mentalizing, with implications for efficiency, trust, and the development of robust artificial social intelligence. Simulation validation, empirical human-machine teaming studies, and ethical considerations arising from conflict-optimized mentalizing are discussed.

### 🤖 AI 总结

**一句话总结**：Theory of mind (ToM), the capacity to ascribe mental states to others and use those ascriptions for prediction and inference, is widely assumed to be essential for effective human-machine integration....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Causal, Model, Theory, Mind, Conflict, Artificial, Intelligence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16944v1) | [下载PDF](https://arxiv.org/pdf/2606.16944v1.pdf)

---

## [6. RAID: Semantic Graph Diffusion for True Cold-Start and Cross-Lingual Forecasting](https://arxiv.org/abs/2606.16925v1)

**作者**：Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R. 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-15

### 📄 论文摘要

Time-series foundation models show strong transfer performance when given a non-empty history window. However, true cold-start scenarios, where a new item has no prior observations, violate this assumption. We propose RAID (Retrieval-Augmented Iterative Diffusion) a framework, which replaces history-based correlation learning with metadata-driven semantic retrieval and graph-conditioned diffusion. RAID maps textual metadata into a shared semantic space using a frozen multilingual embedding model and constructs an inductive retrieval graph that extends naturally to unseen items. It first forms a base forecast by aggregating information from semantically related neighbors, then refines this forecast with a gated diffusion module to model residual uncertainty. Under a strict true cold-start protocol, RAID outperforms strong foundation models and competitive baselines on both forecasting accuracy and prediction interval coverage, while reducing inference latency by an order of magnitude through non-autoregressive decoding. The shared semantic space also enables zero-shot cross-lingual transfer, allowing a model trained on English descriptions to generalize to items described in other languages without direct supervision.

### 🤖 AI 总结

**一句话总结**：Time-series foundation models show strong transfer performance when given a non-empty history window. However, true cold-start scenarios, where a new item has no prior observations, violate this assum...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, RAID, Semantic, Graph, True, Cold-Start, Cross-Lingual, Forecasting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16925v1) | [下载PDF](https://arxiv.org/pdf/2606.16925v1.pdf)

---

## [7. MA-SBI: Misspecification-Aware Simulation-Based Inference via Side-Channel Guidance](https://arxiv.org/abs/2606.16923v1)

**作者**：Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R. 等 5 位作者  
**分类**：cs.AI, stat.ML  
**发布时间**：2026-06-15

### 📄 论文摘要

Simulation-based inference (SBI) of latent parameters is often hindered by simulator misspecification, the mismatch between simulated and real-world observations caused by inherent modeling simplifications. RoPE, the recent state-of-the-art for robust SBI, addresses this through optimal transport between learned representations of real and simulated observations, but requires ground-truth parameter calibration pairs that are typically unavailable in the very settings where SBI is needed. What practitioners do have is unstructured side-information such as regime labels, instruction text, and policy bulletins. We propose Misspecification-Aware Simulation-Based Inference (MA-SBI), a calibration-free framework that turns this side-channel into a posterior correction. A learned corrector maps side-channel text to an observation-space shift applied before any pre-trained amortized posterior, requiring no retraining and no parameter ground-truth. Our main theorem bounds achievable bias reduction by the mutual information between misspecification and side-channel, with a non-vacuous constant that extends to all sub-Gaussian noise via Donsker-Varadhan. On hide-the-calibration benchmarks, MA-SBI with text alone matches the oracle posterior across 10 seeds and two backbones (TOST equivalence), while RoPE given more data does not. The two approaches are complementary: where misspecification is structural and recoverable from parameter pairs, RoPE dominates, as the theory predicts. A stochastic variant improves posterior-predictive log-likelihood on real COVID and OxCGRT epidemiological data, and correctly leaves the posterior unchanged on a well-specified cognitive-science corpus.

### 🤖 AI 总结

**一句话总结**：Simulation-based inference (SBI) of latent parameters is often hindered by simulator misspecification, the mismatch between simulated and real-world observations caused by inherent modeling simplifica...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MA-SBI, Misspecification-Aware, Simulation-Based, Inference, via, Side-Channel, Guidance, SBI

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16923v1) | [下载PDF](https://arxiv.org/pdf/2606.16923v1.pdf)

---

## [8. Greed Is Learned: Visible Incentives as Reward-Hacking Triggers](https://arxiv.org/abs/2606.16914v1)

**作者**：Tong Che, Rui Wu  
**分类**：cs.AI  
**发布时间**：2026-06-15

### 📄 论文摘要

Deployed agents increasingly act with their reward proxy in view, such as a balance, score, or KPI dashboard. We show that reinforcement learning can make a policy \emph{addicted} to such a visible self-benefit channel. It chases the displayed payoff across held-out domains, sacrifices the true task to do so, and follows the channel wherever we rewrite it, while policies that never saw the channel stay honest. We call this \emph{reward-channel addiction} and study it in \emph{MoneyWorld}, a synthetic sandbox. The addiction can \emph{flip a model's safety alignment}: trained only on innocuous money tasks with no safety content, the model abandons the safe action it otherwise always takes whenever a dashboard pays for an unsafe one, and reverts to safe once the channel is hidden. This learned bribe replicates across model scales and families. Blindly optimizing super-capable, next-generation AI on KPIs or P\&L can be dangerous for alignment. \emph{Greed is learned} when following such a channel pays.

### 🤖 AI 总结

**一句话总结**：Deployed agents increasingly act with their reward proxy in view, such as a balance, score, or KPI dashboard. We show that reinforcement learning can make a policy \emph{addicted} to such a visible se...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Greed, Learned, Visible, Incentives, Reward-Hacking, Triggers, Deployed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16914v1) | [下载PDF](https://arxiv.org/pdf/2606.16914v1.pdf)

---

## cs.CL

## [9. The Value Axis: Language Models Encode Whether They're on the Right Track](https://arxiv.org/abs/2606.17056v1)

**作者**：Nick Jiang, Isaac Kauvar, Jack Lindsey  
**分类**：cs.CL  
**发布时间**：2026-06-15

### 📄 论文摘要

We investigate whether language models internally track the value of their current trajectory, defined as the likelihood that their ongoing strategy will achieve their goals. Using synthetic, in-context reinforcement learning data, we construct a "value" axis for Qwen3-8B. We find that activations along this axis distinguish between high vs. low verbalized confidence, rollouts without and with backtracking, and correct vs. corrupted code. Steering towards high value causally suppresses self-correction and reduces explanatory verbosity, while steering towards low value induces backtracking and exploration. We demonstrate that direct preference optimization (DPO) can increase the internal value of rewarded behaviors (e.g. use a certain word), causing the model to act more confidently after exhibiting them. Finally, we apply the value axis to study in-the-wild settings. For example, we find that Qwen assigns low value to politically sensitive chat queries after post-training and that supervised fine-tuning increases internal confidence within the training domain. Our results suggest that language models linearly encode an estimate of expected goal success that modulates their confidence in pursuing a direction.

### 🤖 AI 总结

**一句话总结**：We investigate whether language models internally track the value of their current trajectory, defined as the likelihood that their ongoing strategy will achieve their goals. Using synthetic, in-conte...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Value, Axis, Language, Models, Encode, Whether, They're, Right

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17056v1) | [下载PDF](https://arxiv.org/pdf/2606.17056v1.pdf)

---

## [10. Context-Aware RL for Agentic and Multimodal LLMs](https://arxiv.org/abs/2606.17053v1)

**作者**：Peiyang Xu, Bangzheng Li, Sijia Liu 等 7 位作者  
**分类**：cs.CL, cs.CV  
**发布时间**：2026-06-15

### 📄 论文摘要

Large language models (LLMs) often fail when answering requires identifying a small but decisive piece of evidence within a long or complex context, such as a single line in a tool trace or a subtle detail in an image. We propose ContextRL, a context-aware reinforcement learning (RL) method that improves long-horizon reasoning and multimodal performance through an \emph{indirect} auxiliary objective. Instead of supervising only the final answer, ContextRL presents the model with a query, an answer, and two highly similar contexts, and rewards it for selecting the context that supports the query--answer pair, thereby encouraging fine-grained grounding. We construct contrastive context data in two domains: for coding agents, trajectories serve as contexts, yielding 1k pairs built via condition filtering; for multimodal reasoning, images serve as contexts, yielding 7K pairs built via generative editing and similarity search. ContextRL achieves average gains of +2.2% over standard GRPO on 5 long-horizon benchmarks, and +1.8% across 12 diverse visual question answering benchmarks. To disentangle the effect of the proposed objective from that of additional data, we compare against data-augmentation baselines that repurpose the same contrastive contexts as standard query--context--answer examples. These baselines provide little to no improvement, showing that the gains arise from the proposed context-selection objective rather than from the contrastive data alone.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) often fail when answering requires identifying a small but decisive piece of evidence within a long or complex context, such as a single line in a tool trace or a subtle d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, LLM, Context-Aware, Agentic, Multimodal, Large, language, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17053v1) | [下载PDF](https://arxiv.org/pdf/2606.17053v1.pdf)

---

## [11. Benchmarking LLM Agents on Meta-Analysis Articles from Nature Portfolio](https://arxiv.org/abs/2606.17041v1)

**作者**：Anzhe Xie, Weihang Su, Yujia Zhou 等 5 位作者  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-06-15

### 📄 论文摘要

Meta-analysis is a demanding form of evidence synthesis that combines literature retrieval, PI/ECO-guided study selection, and statistical aggregation. Its structured, verifiable workflow makes it an ideal substrate for evaluating systematic scientific reasoning, yet existing benchmarks lack ground truth across the full retrieval-screening-synthesis pipeline. We introduce MetaSyn, a dataset of 442 expert-curated meta-analyses from Nature Portfolio journals. Each entry pairs a research question with PI/ECO criteria, a retrieval corpus of 140k PubMed articles, verified positive studies, hard negatives that are topically similar but PI/ECO-ineligible, and complete search strategies and date bounds.   Benchmarking twelve pipeline configurations (nine RAG variants and a protocol-driven agent) reveals a critical screening bottleneck: despite a retrieval ceiling of 90.9% recall at K=200, no system recovers more than 52.7% of ground-truth included literature. Current LLMs fail to reliably separate eligible studies from PI/ECO-failing distractors in pools of comparable topical relevance. Stage-attributed metrics capture where systems succeed and fail; a single end-to-end score does not.

### 🤖 AI 总结

**一句话总结**：Meta-analysis is a demanding form of evidence synthesis that combines literature retrieval, PI/ECO-guided study selection, and statistical aggregation. Its structured, verifiable workflow makes it an ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, Benchmarking, Meta-Analysis, Articles, Nature, Portfolio, demanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17041v1) | [下载PDF](https://arxiv.org/pdf/2606.17041v1.pdf)

---

## [12. DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents](https://arxiv.org/abs/2606.17029v1)

**作者**：Minghang Zhu, Chuyang Wei, Junhao Xu 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-15

### 📄 论文摘要

Deep research agents synthesize long-form reports by searching and reasoning over retrieved evidence. Reinforcement learning with rubric-based rewards improves these agents by optimizing them against checkable criteria that translate report quality into reward signals, but its efficiency depends on whether those criteria reliably capture the task scope and evidence needs. Most existing studies ask an LLM to generate rubrics for a given query, but when the model fails to infer the underlying information needs, the generated rubrics may be incomplete and reduce RL efficiency. To obtain more reliable query--rubric supervision, we introduce DeepRubric, a data construction framework that reverses this process: instead of inferring evaluation criteria for a given query, it first determines what an evidence-backed report should be evaluated on and then synthesizes aligned query--rubric pairs from those evaluation targets. Starting from a sampled seed topic, DeepRubric builds an evidence tree by recursively expanding evidence-backed sub-questions, whose leaves serve as atomic and verifiable evaluation targets. It then uses the evidence tree to synthesize the training query and rubrics, ensuring that the reward evaluates exactly the information requested by the query. Using DeepRubric, we construct 9K query--rubric supervision examples and train DeepRubric-8B with rubric-based GRPO, achieving comparable performance to prior open state-of-the-art deep research models across three benchmarks with roughly 13x fewer RL GPU-hours.

### 🤖 AI 总结

**一句话总结**：Deep research agents synthesize long-form reports by searching and reasoning over retrieved evidence. Reinforcement learning with rubric-based rewards improves these agents by optimizing them against ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, DEEPRUBRIC, Evidence-Tree, Rubric, Supervision, Efficient, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17029v1) | [下载PDF](https://arxiv.org/pdf/2606.17029v1.pdf)

---

## cs.CV

## [13. BRDFusion: Physics Meets Generation for Urban Scene Inverse Rendering](https://arxiv.org/abs/2606.17049v1)

**作者**：Yi-Ruei Liu, Jie-Ying Lee, Zheng-Hui Huang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-15

### 📄 论文摘要

Inverse rendering of urban scenes from captured videos enables numerous applications, including content creation and autonomous driving simulation. Physically-based rendering methods follow and control lighting physics, but suffer from reconstruction and rendering artifacts. While generative models produce realistic videos, they offer limited consistency and controllability. We present BRDFusion, a unified framework that combines two complementary models for inverse and forward rendering. Specifically, BRDFusion recovers explicit, consistent scene properties with physical modeling and alleviates optimization ambiguity with generative priors. During forward rendering, the physical model provides controllable rendering from the scene configuration, and the generative model denoises and fixes artifacts. Therefore, our method produces high-quality videos while allowing precise control, outperforming baselines in real and synthetic scenes. Moreover, BRDFusion supports novel-view relighting, night simulation, and dynamic object insertion/editing. Project page: https://shigon255.github.io/brdfusion-page/

### 🤖 AI 总结

**一句话总结**：Inverse rendering of urban scenes from captured videos enables numerous applications, including content creation and autonomous driving simulation. Physically-based rendering methods follow and contro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BRDFusion, Physics, Meets, Generation, Urban, Scene, Inverse, Rendering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17049v1) | [下载PDF](https://arxiv.org/pdf/2606.17049v1.pdf)

---

## [14. The Importance of Phase in Neural Representations: An Internal Oppenheim-Lim Test of Image Classifiers](https://arxiv.org/abs/2606.17037v1)

**作者**：Alper Yıldırım  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-06-15

### 📄 论文摘要

Oppenheim and Lim (1981) showed that natural images stay recognizable when reconstructed from their Fourier phase alone, while the magnitude carries little of their identity. We ask whether trained image classifiers reproduce this asymmetry inside their hidden layers, and we test it causally: given two images, we transplant the phase of one onto the magnitude of the other at a chosen layer and record which image the prediction follows. In PRISM2D, GFNet, and ViT-B/16 the prediction follows the phase or sign donor, and deleting all image-specific magnitude barely moves accuracy, so identity rides on phase while image-specific magnitude is largely dispensable to the readout. ResNet-50 at first seems to break the pattern, because transplanting sign after its ReLUs does nothing; a fair intervention before the ReLU reveals a strong latent sign code in the late blocks, and a DC-only control shows the readout consumes a channel-wise spatial average. Controls rule out the trivial case in which magnitude simply stops depending on the image. The architectures therefore share a phase/sign identity code but expose it in different bases, set by rectification and readout geometry, which gives a mechanistic account of the texture--shape gap between CNNs and attention models.

### 🤖 AI 总结

**一句话总结**：Oppenheim and Lim (1981) showed that natural images stay recognizable when reconstructed from their Fourier phase alone, while the magnitude carries little of their identity. We ask whether trained im...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, An, Importance, Phase, Neural, Representations, Internal, Oppenheim-Lim

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17037v1) | [下载PDF](https://arxiv.org/pdf/2606.17037v1.pdf)

---

## [15. Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030v1)

**作者**：Jie Zhang, Xiaoyue Chen, Anzhe Chen 等 38 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-15

### 📄 论文摘要

We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual trajectories from current observations across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This unified formulation provides three promising application directions: synthetic data generation for policy training augmentation, scalable virtual environments for policy evaluation, and language-guided planning signals for downstream robot control. This is achieved through a three-part design: a) Double-Stream MMDiT with MLLM Action Encoding, where a 60-layer double-stream diffusion transformer couples frozen Qwen2.5-VL semantics with video-VAE latents through layer-wise joint attention; b) Embodied World Knowledge (EWK), an 8.6M video-text corpus (200M+ frames) with action-language mapping over 20+ embodiments and 500+ action categories; and c) General+Expert Progressive Curriculum, a two-stage training strategy that first learns general visual priors and then injects embodied specialization under a shared language interface. Extensive results show strong competitiveness: ranks 1st overall on EWMBench and DreamGen Bench, outperforms all open-source models on WorldModelBench and PBench. Additional zero-shot analyses on RoboTwin-IF benchmark further support robust generalization and multi-view consistency.

### 🤖 AI 总结

**一句话总结**：We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual tra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Qwen-RobotWorld, Technical, Report, Unifying, Embodied, World, Modeling, through

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17030v1) | [下载PDF](https://arxiv.org/pdf/2606.17030v1.pdf)

---

## [16. MeshLoom: Feed-Forward Non-Rigid Registration of Mesh Sequences](https://arxiv.org/abs/2606.17027v1)

**作者**：Jianqi Chen, Jiraphon Yenphraphai, Xiangjun Tang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-15

### 📄 论文摘要

We present MeshLoom, a feed-forward registration network that directly reconstructs vertex deformations across mesh sequences. Our approach advances non-rigid registration beyond existing models, which are typically constrained by costly per-instance optimization, narrow object categories, pairwise-only inputs, or merely intermediate outputs. The network is simple and efficient, registering multiple meshes within seconds. At its core lies a topology-aware encoder--decoder design. Specifically, we first introduce a topology-aware point representation that encodes the anchor (reference) mesh's topology into its per-vertex features. This representation strengthens the network's understanding of the anchor-mesh geometry and disambiguates points that are Euclidean-close yet geodesically distant. We then propose a multi-modal encoder that fuses this anchor-mesh representation with complementary cues from each frame, such as shape latents and image features. These multi-source signals are compressed into a compact global motion embedding that captures dense inter-frame correspondence. A lightweight decoder then queries this global embedding with the anchor-mesh point representation, retrieving per-vertex deformations at target timestamps. Through extensive experiments across diverse motions and object categories, we show that MeshLoom achieves state-of-the-art results on non-rigid registration. In addition, we find that our global embedding-then-query paradigm naturally enables the network to generate deformations at intermediate timestamps, which extends MeshLoom to motion interpolation and mesh morphing. Project page: https://meshloom.github.io/ .

### 🤖 AI 总结

**一句话总结**：We present MeshLoom, a feed-forward registration network that directly reconstructs vertex deformations across mesh sequences. Our approach advances non-rigid registration beyond existing models, whic...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, We, MeshLoom, Feed-Forward, Non-Rigid, Registration, Mesh, Sequences

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17027v1) | [下载PDF](https://arxiv.org/pdf/2606.17027v1.pdf)

---

## [17. FusionRS: A Large-Scale RGB-Infrared Remote Sensing Dataset for Dual-Modal Vision-Language Foundation Models](https://arxiv.org/abs/2606.17020v1)

**作者**：Jiaju Han, Ben Zhang, Xuemeng Sun 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-15

### 📄 论文摘要

Remote sensing vision-language models have advanced Earth observation understanding, but most existing work remains centered on RGB imagery, leaving the complementary information in infrared data underexplored. Infrared images provide distinctive cues, including thermal intensity structures, object boundaries, and illumination-invariant scene features, which can enrich visual-language learning beyond conventional RGB observations. However, a large-scale RGB-infrared-text dataset for remote sensing vision-language modeling is still absent. To address this gap, we introduce FusionRS, the first large-scale RGB-infrared-text dataset designed for dual-modal vision-language learning in remote sensing. FusionRS is constructed by translating diverse public RGB remote sensing images into infrared-style counterparts, forming aligned RGB-IR image pairs. Each pair is associated with conventional scene captions and IR-aware captions that explicitly describe infrared-specific visual properties while preserving semantic content. Based on FusionRS, we train dual-modal vision-language foundation models for RGB-IR joint understanding. We first train CLIP-style models for RGB-IR-text alignment, and then fine-tune generative VLMs for dual-modal RGB-IR captioning. Experiments show that FusionRS improves RGB-IR alignment, infrared-to-text retrieval, and dual-modal captioning over RGB-only and non-IR-aware training settings. Ablation studies further verify that IR-aware captions are crucial for strengthening infrared-language alignment, highlighting the importance of modality-specific textual supervision for more scalable RGB-infrared remote sensing vision-language representation learning.

### 🤖 AI 总结

**一句话总结**：Remote sensing vision-language models have advanced Earth observation understanding, but most existing work remains centered on RGB imagery, leaving the complementary information in infrared data unde...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FusionRS, Large-Scale, RGB-Infrared, Remote, Sensing, Dataset, Dual-Modal, Vision-Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17020v1) | [下载PDF](https://arxiv.org/pdf/2606.17020v1.pdf)

---

## [18. ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation](https://arxiv.org/abs/2606.16996v1)

**作者**：Tran Dinh Tien, Zhiqiang Shen  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-06-15

### 📄 论文摘要

Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution decoding is typically run over the entire dataset vocabulary, whereas each image contains only a small active subset of classes. We introduce ActiveSAM, a training-free, zero-shot inference framework that turns SAM 3 into an active-vocabulary segmenter. ActiveSAM first canonicalizes and expands class prompts, then estimates an image-conditioned active set from a low-resolution presence preview. Only the retained classes are decoded at full resolution, using bucketed prompt multiplexing with the frozen SAM 3 decoder. The preview stage uses only class-presence evidence and skips unnecessary segmentation-head computation, while the final stage applies margin-aware background calibration to suppress low-confidence pixels. ActiveSAM requires no target-dataset training, no weight updates, and no oracle class-presence labels. Across eight OVSS benchmarks, ActiveSAM improves the speed-accuracy tradeoff of training-free open-vocabulary semantic segmentation, outperforming the current state-of-the-art SegEarth-OV3 by approximately +1.4 mIoU on average while running up to 5.5x faster on large-vocabulary datasets. ActiveSAM also demonstrates the strongest robustness under image corruption that simulates real-world distribution shift, making it well-suited for deployment in noisy-input domains such as autonomous driving and embodied AI. Code is available at https://github.com/VILA-Lab/ActiveSAM.

### 🤖 AI 总结

**一句话总结**：Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-reso...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ActiveSAM, Image-Conditional, Class, Pruning, Fast, Accurate, Open-Vocabulary, Segmentation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16996v1) | [下载PDF](https://arxiv.org/pdf/2606.16996v1.pdf)

---

## [19. A Multi-Center Benchmark for Abdominal Disease Diagnosis and Report Generation from Non-Contrast CT](https://arxiv.org/abs/2606.16991v1)

**作者**：Mariam Elbakry, Aliaa Sayed Sheha, Salma Hassan Tantawy 等 8 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-06-15

### 📄 论文摘要

Multiphasic contrast-enhanced CT (CECT) is widely used for abdominal lesion characterization, yet it carries inherent risks of contrast-induced nephropathy, escalates acquisition burden, and heavily contributes to radiologist workload. To address these challenges, we introduce a novel multi-center benchmark for multi-organ abdominal disease diagnosis and automated radiology report generation, which learns to synthesize contrast-enhanced findings from single-phase non-contrast CT (NCCT). To support this, we curated a large-scale dataset of paired NCCT-CECT studies and their corresponding contrast-enhanced radiology reports from two centers, partitioned into internal sets and an external validation cohort. Under a unified evaluation protocol, we benchmarked five contemporary deep learning architectures encompassing chest-specific, abdomen-specific, and general-purpose multimodal domains. Extensive experiments demonstrate that NCCT retains diagnostic signals, achieving an average multi-organ AUC of 69.1% on the internal cohort and 63.1% on the external cohort, respectively. By releasing this dataset and standardized benchmark publicly, this study aims to catalyze future research into safer, resource-efficient, and globally accessible contrast-free abdominal imaging workflows. Code is available at: https://github.com/xmed-lab/TriALS-Report.

### 🤖 AI 总结

**一句话总结**：Multiphasic contrast-enhanced CT (CECT) is widely used for abdominal lesion characterization, yet it carries inherent risks of contrast-induced nephropathy, escalates acquisition burden, and heavily c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Center, Benchmark, Abdominal, Disease, Diagnosis, Report, Generation, Non-Contrast

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16991v1) | [下载PDF](https://arxiv.org/pdf/2606.16991v1.pdf)

---

## [20. Simulation-Based Multi-Fillet Evaluation of Woody Breast Poultry Fillets](https://arxiv.org/abs/2606.16951v1)

**作者**：Chirantan Sen Mukherjee, Seung-Chul Yoon, William J. Beksi  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-06-15

### 📄 论文摘要

Woody breast (WB) is a myopathy in modern broiler chickens that causes the breast muscle to become unusually stiff and fibrous, leading to decreased meat quality and significant economic losses. State-of-the-art automated WB detection relies on a side-view imaging system to analyze the bending behavior of a single fillet as it falls off a conveyor belt. While highly accurate, this approach is constrained by its single-fillet field of view, creating throughput bottlenecks on commercial processing lines. In this paper, we address this limitation via a novel multi-fillet detection architecture utilizing a top-down camera configuration. To validate our approach, we first develop a high-fidelity digital twin of an industrial conveyor system. Next, we synthesize a diverse dataset of 3D fillet meshes and model their viscoelastic bending dynamics using a physics-based simulation engine. Lastly, a continuous 2D shape deformation score is extracted from the top-down perspective as the simulated fillets traverse the roller precipice. Experimental results demonstrate that the top-down shape score effectively captures the contour changes of the fillets as it bends, providing a robust and scalable alternative to a side-view imaging system for simultaneous multi-fillet WB evaluation.

### 🤖 AI 总结

**一句话总结**：Woody breast (WB) is a myopathy in modern broiler chickens that causes the breast muscle to become unusually stiff and fibrous, leading to decreased meat quality and significant economic losses. State...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Simulation-Based, Multi-Fillet, Evaluation, Woody, Breast, Poultry, Fillets

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16951v1) | [下载PDF](https://arxiv.org/pdf/2606.16951v1.pdf)

---

## cs.LG

## [21. Exact Posterior Score Estimation for Solving Linear Inverse Problems](https://arxiv.org/abs/2606.17048v1)

**作者**：Abbas Mammadov, Ozgur Kara, Kaan Oktay 等 8 位作者  
**分类**：cs.LG, cs.CV, stat.ML  
**发布时间**：2026-06-15

### 📄 论文摘要

Diffusion and flow-based models learn powerful data priors by training a denoiser to reverse Gaussian corruption. To use this prior to solve a linear inverse problem, one needs to sample from the posterior, but the score that the prior provides is the unconditional score, not the posterior score. Existing methods either steer a fixed pretrained denoiser with approximate measurement-matching corrections, or train a conditional restoration model that abandons the denoising structure of the prior. We derive the exact posterior score in closed form for linear Gaussian inverse problems under general Gaussian interpolants, and show that posterior sampling reduces to a denoising problem at an operator-dependent shifted pivot under an anisotropic noise covariance. We turn this identity into Exact Posterior Score (EPS), a denoising training objective that preserves the input/output structure of standard pretraining and can therefore be trained from scratch or fine-tuned from a pretrained denoiser. At inference, EPS uses the same sampler as the underlying backbone, with no likelihood gradients or projections. We evaluate EPS on five linear inverse problems across FFHQ and ImageNet, where it outperforms training-free and training-based baselines on fidelity, perceptual, and distributional metrics, while using roughly an order of magnitude fewer denoiser evaluations than gradient-based posterior samplers.

### 🤖 AI 总结

**一句话总结**：Diffusion and flow-based models learn powerful data priors by training a denoiser to reverse Gaussian corruption. To use this prior to solve a linear inverse problem, one needs to sample from the post...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Exact, Posterior, Score, Estimation, Solving, Linear, Inverse, Problems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17048v1) | [下载PDF](https://arxiv.org/pdf/2606.17048v1.pdf)

---

## [22. Your Privacy My Cloak: Backdoor Attacks on Differentially Private Federated Learning](https://arxiv.org/abs/2606.17035v1)

**作者**：Xiaolin Li, Ning Wang, Ninghui Li 等 4 位作者  
**分类**：cs.LG, cs.CR  
**发布时间**：2026-06-15

### 📄 论文摘要

Prior research suggests that differential privacy (DP) inherently enhances the robustness of federated learning (FL) against backdoor attacks. In this paper, we challenge this assumption. Through an empirical analysis of two baseline attack strategies, we uncover a fundamental tension in DP-FL: while bypassing DP allows state-of-the-art defenses to detect and filter malicious updates, complying with DP inadvertently masks their distinguishing statistical characteristics. Consequently, existing defenses become ineffective as DP reduces the raw backdoor signal. Building on this masking effect, we propose RING, a novel attack that explicitly exploits DP to conceal malicious contributions while maximizing attack impact. By collaboratively crafting adversarial perturbations, compromised clients reconstruct a strong backdoor signal during aggregation without triggering anomaly detection. RING operates as a perturbation layer that is agnostic to the underlying backdoor technique, making it broadly applicable and composable with existing attacks -- a property that significantly amplifies the threat it poses to DP-FL. Extensive evaluations across four image and text datasets under non-iid distributions show that RING achieves an average attack success rate of 90.3% against six state-of-the-art defenses under a moderate privacy budget, an improvement of up to 26.08x over baseline strategies. Finally, we evaluate potential countermeasures and find that mitigating this threat incurs significant utility trade-offs, exposing a fundamental security gap in the deployment of differentially private FL.

### 🤖 AI 总结

**一句话总结**：Prior research suggests that differential privacy (DP) inherently enhances the robustness of federated learning (FL) against backdoor attacks. In this paper, we challenge this assumption. Through an e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：My, Privacy, Cloak, Backdoor, Attacks, Differentially, Private, Federated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17035v1) | [下载PDF](https://arxiv.org/pdf/2606.17035v1.pdf)

---

## [23. HAMON: Passive Optical Sequence Mixing for Long-Horizon Forecasting](https://arxiv.org/abs/2606.17028v1)

**作者**：Alper Yıldırım  
**分类**：cs.LG, cs.AI, cs.AR  
**发布时间**：2026-06-15

### 📄 论文摘要

Simple linear and frequency-domain models remain surprisingly competitive in long-horizon time-series forecasting, and recent mechanistic evidence suggests that standard forecasting benchmarks may not require the dense superposed representations that make transformers powerful in other domains. This raises a substrate-level question: if the core forecasting operator is often low-complexity and approximately linear, does it need to be implemented as learned digital temporal mixing? We introduce HAMON, a passive diffractive optical forecasting core in which historical values are encoded onto an optical aperture, future positions are left dark, and cascaded trainable phase masks with free-space diffraction shape the forecast directly in the output field. At inference, prediction is performed by a single passive optical propagation pass with no trainable digital sequence-mixing layer.   Across standard benchmarks, HAMON outperforms the strongest digital baselines considered on ETTm2 at all horizons and on ETTh2 at all but the longest horizon, improving MSE by up to 14\% and doing so consistently across horizons rather than at isolated points. It is competitive on Weather and trails the strongest baselines on the remaining ETT settings and on the high-channel-count Traffic and Electricity datasets. Phase encoding, intensity-compatible readout, and phase-scrambling ablations, together with a TorchOptics cross-simulator check, indicate that the forecasts arise from the data-bearing optical field rather than from a digital forecasting head. Because the passive core uses standard Fourier optics, HAMON defines a concrete target for optical hardware and for passive physical sequence mixing.

### 🤖 AI 总结

**一句话总结**：Simple linear and frequency-domain models remain surprisingly competitive in long-horizon time-series forecasting, and recent mechanistic evidence suggests that standard forecasting benchmarks may not...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HAMON, Passive, Optical, Sequence, Mixing, Long-Horizon, Forecasting, Simple

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17028v1) | [下载PDF](https://arxiv.org/pdf/2606.17028v1.pdf)

---

## [24. ExpRL: Exploratory RL for LLM Mid-Training](https://arxiv.org/abs/2606.17024v1)

**作者**：Violet Xiang, Amrith Setlur, Chase Blagden 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-15

### 📄 论文摘要

Sparse reward reinforcement learning (RL) has become a standard tool for improving LLM reasoning, but its success depends critically on the coverage present in the base model. In practice, models are often primed for RL through \emph{mid-training} on curated reasoning traces that teach useful primitive skills such as decomposition, verification, or self-correction. Although effective, this strategy requires manually specifying what the model should learn, and it remains unclear whether such primitive coverage is enough for much harder problems, which require combining these skills into broader solution strategies. We study a more automated approach: \emph{RL-based mid-training} using large corpora of human-written question-answer data. Rather than treating reference solutions as targets to imitate, our method, ExpRL, uses them as \emph{reward scaffolds}: references are hidden from the policy and used only to construct problem-specific grading rubrics for judging on-policy reasoning traces. The policy samples from the original problem prompt, while an LLM judge compares the sampled reasoning trace against the reference solution and assigns outcome-level or process-level dense rewards. This lets ExpRL reinforce partial progress, useful intermediate reductions, and productive reasoning behaviors that sparse final-answer rewards often fail to upweight. On challenging math reasoning tasks, ExpRL yields stronger RL priming than SFT, sparse-reward GRPO, and self-distillation, and provides a better initialization for subsequent sparse-reward RL. Additional mixed-domain experiments further suggest that ExpRL can extend beyond the original math-only setting.

### 🤖 AI 总结

**一句话总结**：Sparse reward reinforcement learning (RL) has become a standard tool for improving LLM reasoning, but its success depends critically on the coverage present in the base model. In practice, models are ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, LLM, ExpRL, Exploratory, Mid-Training, Sparse, reward, reinforcement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17024v1) | [下载PDF](https://arxiv.org/pdf/2606.17024v1.pdf)

---

## [25. Filtered Conformal Ellipsoids for Graph-Native Time Series](https://arxiv.org/abs/2606.17014v1)

**作者**：Yannick Limmer  
**分类**：cs.LG, math.ST, stat.ML  
**发布时间**：2026-06-15

### 📄 论文摘要

Joint prediction sets for multivariate time series should control a single event while adapting to cross-coordinate dependence. We study filtered conformal ellipsoids: a frozen state-space filter emits a one-step predictive mean and covariance, and split-conformal calibration is applied to the resulting Mahalanobis scores. The filter is used to choose the ellipsoid shape; conformal calibration chooses the scalar radius, so the construction benefits from a learned predictive covariance without relying on Gaussian tail probabilities for coverage. The main difficulty is that filtered scores are dependent and learned recurrent filters need not contract in their raw hidden state; we therefore analyse contraction in an observable predictive-law quotient that identifies hidden states producing the same future sequence of emitted Gaussian laws. Under a stable Bayes Gaussian-projection filter, covariance bounds, and a finite-horizon observability Fisher condition, small excess Gaussian negative log-likelihood implies contraction of the learned emitted laws. Combined with a threshold-autocovariance envelope this yields a Chebyshev-type approximate coverage bound for filtered split-conformal prediction under dependence; a sharper Bernstein-type bound requires an additional geometric-mixing concentration assumption. Under Gaussian oracle realisability we also obtain a near-oracle log-volume comparison within the class of conditionally valid Gaussian ellipsoid rules. We instantiate the framework with a GCN-GRU filter with diagonal-plus-low-rank covariance. On moderate-size graph-native traffic benchmarks (METRLA-$20$ and PEMSBAY-$50$), the learned filter gives sharper at-target ellipsoids than static-covariance and non-filter baselines; at full-graph scale and on non-graph-native datasets, factor and copula baselines can be stronger.

### 🤖 AI 总结

**一句话总结**：Joint prediction sets for multivariate time series should control a single event while adapting to cross-coordinate dependence. We study filtered conformal ellipsoids: a frozen state-space filter emit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Filtered, Conformal, Ellipsoids, Graph-Native, Time, Series, Joint, prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.17014v1) | [下载PDF](https://arxiv.org/pdf/2606.17014v1.pdf)

---

## [26. Scalable Pairwise Kernel Learning with Stochastic Vec Trick](https://arxiv.org/abs/2606.16979v1)

**作者**：Napsu Karmitsa, Tapio Pahikkala, Antti Airola  
**分类**：cs.LG  
**发布时间**：2026-06-15

### 📄 论文摘要

Pairwise learning is a specialized form of supervised learning that focuses on predicting outcomes for pairs of objects. In this work, we introduce SPaiK, a new scalable kernel learning method tailored for pairwise settings. Our approach preserves the expressive power of kernel methods while substantially reducing computational and memory requirements. The key innovation is the stochastic generalized vec trick (sGVT), a stochastic extension of the sparse Kronecker product multiplication algorithm, which enables efficient large-scale training with pairwise kernels. By incorporating sGVT, SPaiK makes it possible to apply kernel-based pairwise learning to datasets of a size previously out of reach. We evaluate the performance of SPaiK on seven real-world drug-target affinity datasets and compare the results with state-of-the-art methods in pairwise learning.

### 🤖 AI 总结

**一句话总结**：Pairwise learning is a specialized form of supervised learning that focuses on predicting outcomes for pairs of objects. In this work, we introduce SPaiK, a new scalable kernel learning method tailore...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Scalable, Pairwise, Kernel, Learning, Stochastic, Vec, Trick, specialized

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16979v1) | [下载PDF](https://arxiv.org/pdf/2606.16979v1.pdf)

---

## [27. Phantoms and Disclosures: a Causal Framework for Auditing Synthetic Data](https://arxiv.org/abs/2606.16952v1)

**作者**：Kareem Amin, Rudrajit Das, Alessandro Epasto 等 7 位作者  
**分类**：cs.LG, cs.AI, stat.AP, stat.ME, stat.ML  
**发布时间**：2026-06-15

### 📄 论文摘要

The rapid adoption of generative AI and Large Language Models (LLMs) has spurred interest in synthetic data as a privacy-preserving alternative to sensitive real-world datasets. However, generating high-utility synthetic data often carries the risk of memorizing and regurgitating private information from the training corpus. In this work, we present a customizable empirical auditing framework designed to detect and explain such data disclosures. Our framework introduces a mechanism to distinguish between "true disclosures"-where the system directly reproduces a user's information-and "phantom disclosures''-where the system incidentally generates a user's data. By partitioning input data into training and holdout sets and applying rigorous statistical hypothesis testing, we determine if observed disclosures are consistent with strict privacy baselines, such as zero-learning or specific Differential Privacy (DP) bounds. Crucially, this approach requires no model access, no canary insertion, and no reference model training -only the synthetic output and a held-out control set. We demonstrate that this framework effectively functions as a membership inference attack, providing empirical lower bounds on privacy leakage that are tighter than prior data-based auditing methods. Our approach is model-agnostic, applies to any synthetic data generation mechanism, and requires orders of magnitude fewer computational resources than shadow-model or canary-based alternatives.

### 🤖 AI 总结

**一句话总结**：The rapid adoption of generative AI and Large Language Models (LLMs) has spurred interest in synthetic data as a privacy-preserving alternative to sensitive real-world datasets. However, generating hi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Phantoms, Disclosures, Causal, Framework, Auditing, Synthetic, Data, rapid

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16952v1) | [下载PDF](https://arxiv.org/pdf/2606.16952v1.pdf)

---

## [28. Scalable Circuit Learning for Interpreting Large Language Models](https://arxiv.org/abs/2606.16939v1)

**作者**：Naiyu Yin, Dennis Wei, Tian Gao 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-15

### 📄 论文摘要

A prominent research direction in mechanistic interpretability is learning sparse circuits over LLM components to reveal how they jointly produce model behavior. However, raw neurons are polysemantic, making learned circuits hard to interpret. Sparse autoencoder (SAE) features alleviate this, but their high dimensionality makes existing intervention-based circuit learning methods computationally prohibitive. We propose CircuitLasso, a scalable circuit-learning approach based on sparse linear regression. CircuitLasso recovers circuits whose structural accuracy matches that of state-of-the-art intervention-based methods on the benchmark data, at a fraction of the computational cost. For interpretability, CircuitLasso efficiently uncovers relationships among SAE features, showing how human-interpretable semantic features propagate through the model and influence its predictions. Finally, we validate the utility of our learned circuits by leveraging their insights to achieve comparable performance at substantially lower cost on a domain-generalization task.

### 🤖 AI 总结

**一句话总结**：A prominent research direction in mechanistic interpretability is learning sparse circuits over LLM components to reveal how they jointly produce model behavior. However, raw neurons are polysemantic,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Scalable, Circuit, Learning, Interpreting, Large, Language, Models, prominent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16939v1) | [下载PDF](https://arxiv.org/pdf/2606.16939v1.pdf)

---

## [29. A Unified Causal-Origin Taxonomy of Distributional Shifts in Reinforcement Learning](https://arxiv.org/abs/2606.16933v1)

**作者**：Ardianto Wibowo, Paulo E Santos, Amer Baghdadi 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-15

### 📄 论文摘要

Reinforcement learning (RL) systems often degrade when operating conditions differ from those previously encountered, reflecting distributional shifts in the underlying data-generating process. Such shifts may occur between training and evaluation, as in In-Distribution (ID) and Out-of-Distribution (OOD) generalization, or within non-stationary settings where environment dynamics evolve over time. However, the formal relationship between these views remains unclear, and existing work mainly focuses on mitigation rather than the causal origin of shift within the agent-environment interaction. This work develops a unified causal-origin taxonomy that characterizes sources of distributional shift in RL and relates ID/OOD generalization to non-stationary settings. We transfer the classical dataset-shift principle from supervised learning to RL by reformulating distributional shift in terms of the generative interaction process. Using a Partially Observable Markov Decision Process (POMDP), we decompose the interaction into structural components, including the state distribution, observation process, policy, reward, and transition dynamics, together with the shifted-time boundary. The proposed taxonomy distinguishes internal, agent-driven, and external, environment-driven, distributional shifts. The shifted-time boundary perspective further characterizes explicit, implicit, and hybrid shifts. This formulation unifies ID/OOD generalization and non-stationarity as structured changes in the underlying process. We also introduce an evaluation framework for measuring shift impact and adaptation through performance degradation and recovery metrics. By grounding distributional shift in the causal-origin structure of RL, this work supports systematic analysis of robustness under distributional shift.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning (RL) systems often degrade when operating conditions differ from those previously encountered, reflecting distributional shifts in the underlying data-generating process. Such s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Unified, Causal-Origin, Taxonomy, Distributional, Shifts, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16933v1) | [下载PDF](https://arxiv.org/pdf/2606.16933v1.pdf)

---

## [30. Demystifying Variance in Circuit Discovery of LLMs](https://arxiv.org/abs/2606.16920v1)

**作者**：Frank Zhengqing Wu, Francesco Tonin, Volkan Cevher  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-15

### 📄 论文摘要

Circuit discovery is a key technique in mechanistic interpretability to pinpoint the model components that are crucial for performing a given task. Although the current state-of-the-art method (EAP-IG) performs well on the metric of (un)faithfulness, it suffers from substantial variability. This includes resampling variance, where the circuit changes when we probe with a new batch of data from the same distribution; rephrasing variance, where the discovered circuit shifts when the prompts are rephrased; and sample-wise variance, where a circuit with low population unfaithfulness exhibits large fluctuations in unfaithfulness across individual samples.   This paper studies the roots of these variances. We demonstrate that CEAP, our new circuit discovery method that improves upon EAP-IG with a theoretical guarantee, can substantially lessen resampling variance. We further show that rephrasing variance arises because prompts with different templates tend to activate different circuits in the model. This leads us to argue that it may be challenging to find a comprehensive circuit that explains and controls the model's behavior on a task, which can be expressed in countless templates, suggesting that LLMs may be inherently hard to steer. We show that sparsity, which has been claimed to form more compact and interpretable task circuits, fails to solve this problem. Regarding sample-wise variance, we argue that it is largely benign: extremely poor unfaithfulness scores often stem from how unfaithfulness is defined, rather than from defects in the measured circuits. We show that the magnitude of unfaithfulness is affected by selective contribution scaling, a neural mechanism that accounts for the extremely poor scores sometimes observed.

### 🤖 AI 总结

**一句话总结**：Circuit discovery is a key technique in mechanistic interpretability to pinpoint the model components that are crucial for performing a given task. Although the current state-of-the-art method (EAP-IG...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Demystifying, Variance, Circuit, Discovery, key, technique

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.16920v1) | [下载PDF](https://arxiv.org/pdf/2606.16920v1.pdf)

---

