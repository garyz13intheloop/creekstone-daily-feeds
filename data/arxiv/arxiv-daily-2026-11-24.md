# arXiv AI 论文日报 | 2026-11-24

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.AI](#csAI) (9 篇)
- [cs.CL](#csCL) (3 篇)

---

## cs.AI

## [1. Seeking in Space: Benchmarking Purposeful Active Exploration of Vision-Language Models for Spatial Reasoning](https://arxiv.org/abs/2611.31215v1)

**作者**：Xiwei Liu, Yulong Li, Xuhui Li 等 10 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-23

### 📄 论文摘要

Humans explore unfamiliar spaces with purpose, deciding where to look until they have gathered the evidence a spatial question requires. However, can vision-language models (VLMs), which reason increasingly well over curated images and videos, also seek in space when the evidence is not handed to them? We present ActSpace-Bench, a benchmark of 994 questions across 234 exploration episodes in 72 real-scanned indoor scenes, where a model starts from a single view, navigates real captured frames, and must gather evidence before answering. To assess whether such exploration is purposeful, we introduce a controlled evaluation protocol that fixes each model as the reasoner and compares its own exploration against a same-budget random walk and an oracle route, separating evidence seeking from spatial reasoning. Every question is verified to require exploration and answered from 3D annotations, masked-evidence questions test whether models know when to abstain, and over 95% of sampled questions are confirmed correct by human verification. Evaluations of 23 proprietary, open-weight, and spatially specialized VLMs reveal that the strongest models do seek evidence with purpose but lose much of it to limited memory, whereas weaker and specialized models explore no better than a random walk or fail to reason over the evidence they are given, pointing to memory and evidence-grounded reasoning as the next targets for active spatial intelligence.

### 🤖 AI 总结

**一句话总结**：Humans explore unfamiliar spaces with purpose, deciding where to look until they have gathered the evidence a spatial question requires. However, can vision-language models (VLMs), which reason increa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Seeking, Space, Benchmarking, Purposeful, Active, Exploration, Vision-Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31215v1) | [下载PDF](https://arxiv.org/pdf/2611.31215v1.pdf)

---

## [2. Needwise: Generation-Free Conversational Recommendation from Need-Level Typed Decisions](https://arxiv.org/abs/2611.31175v1)

**作者**：Sungchul Kim, Weixiao Huang, Mekala Raja Sekhar Reddy 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-23

### 📄 论文摘要

Conversational recommenders must rank items against needs that catalogs record only in part, while users add, withdraw and reverse needs and switch between requests. LLM rankers re-read the dialogue at every turn: they are slow, and their ordering does not show which needs an item meets. We show that a conversational recommender can be built from typed decisions instead: named questions over fixed options, answered with option probabilities rather than generated text. On each turn, one typed request maps the message onto the catalog's fields, keeps what no field expresses in the user's words, and decides how the turn changes each earlier need. Needwise then ranks candidates must-first: the needs on the kind of item, its place and its price form a tier, and within it one holistic decision and need-level verdicts (supported, contradicted or unknown) are combined with equal weight (Needwise-HF). With the graded attributes withheld from the records, so that needs must be inferred from names, descriptions and reviews, Needwise-HF ranks Google Local requests significantly better than GPT-6 Sol (0.383 against 0.343 nDCG@10) and is not significantly different from the strongest LLM ranker on Google Local and Yelp; these comparisons keep their sign under every treatment of unrecorded attributes we test. It costs a fraction of GPT-6 Sol's API price and answers in 2.5 s at the median on Google Local, against 5.6 s for GPT-6 Sol. In conversations, the typed state keeps the ranking across switches and returns, but it recognizes only 19-27% of withdrawn needs.

### 🤖 AI 总结

**一句话总结**：Conversational recommenders must rank items against needs that catalogs record only in part, while users add, withdraw and reverse needs and switch between requests. LLM rankers re-read the dialogue a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Needwise, Generation-Free, Conversational, Recommendation, Need-Level, Typed, Decisions, recommenders

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31175v1) | [下载PDF](https://arxiv.org/pdf/2611.31175v1.pdf)

---

## [3. Reducing Order Sensitivity in Decision Models](https://arxiv.org/abs/2611.31174v1)

**作者**：Bodong Liu, Dongyoung Go, Sofian Zalouk 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-23

### 📄 论文摘要

Decision models are emerging as fast components of larger AI systems. Yet recent decision models, such as Jev, process options sequentially, leading to different predictions based on their ordering. Across ten open- and closed-source decision models, we find that \emph{order-sensitivity} is pervasive, causing substantial accuracy degradation and unreliable decision-making. These effects become more pronounced as the number of options grows and can compound across multi-step decisions. To address this problem, we systematically compare eight methods for mitigating order sensitivity in terms of robustness, predictive accuracy, and inference efficiency. Among these methods, we find that \emph{tree attention} is a surprisingly effective and efficient method. It achieves order invariance by processing options as parallel branches of a shared context. When used during training, it matches the baseline's average accuracy. Applied to the baseline without retraining, it also eliminates order sensitivity with only a 1.1-point drop in accuracy. Our findings demonstrate that order invariance can be enforced directly in decision models with little or no loss in predictive accuracy.

### 🤖 AI 总结

**一句话总结**：Decision models are emerging as fast components of larger AI systems. Yet recent decision models, such as Jev, process options sequentially, leading to different predictions based on their ordering. A...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Reducing, Order, Sensitivity, Decision, Models, emerging, fast

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31174v1) | [下载PDF](https://arxiv.org/pdf/2611.31174v1.pdf)

---

## [4. When Does Overriding the Majority Vote Help?](https://arxiv.org/abs/2611.31165v1)

**作者**：Terry Ma, Aidan Zhang  
**分类**：cs.AI  
**发布时间**：2026-11-23

### 📄 论文摘要

When should additional reasoning or verification replace a majority-vote answer? We call such a replacement an override. We examine two obstacles: the availability of correct alternatives and the reliability of methods that produce or select them. We compare additional reasoning, executed programs, and cross-model reasoning on 150 competition-mathematics questions with three open reasoning models. Starting from a majority vote over 16 responses, we measure how often overrides occur and how many errors they correct or introduce across agreement thresholds. When the vote is incorrect, the correct answer is often absent from the original responses. Additional same-model reasoning rarely overrides, while executed programs correct more errors than they introduce at every evaluated threshold. Cross-model overrides improve some weaker baselines but do not establish an advantage over the more accurate model alone, even with only eight standalone responses. Stricter agreement reduces how often overrides occur but does not consistently increase the fraction that correct errors. At the strictest thresholds, overrides occur on few distinct questions, limiting conclusions about their reliability.

### 🤖 AI 总结

**一句话总结**：When should additional reasoning or verification replace a majority-vote answer? We call such a replacement an override. We examine two obstacles: the availability of correct alternatives and the reli...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Does, Overriding, Majority, Vote, Help?, should, additional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31165v1) | [下载PDF](https://arxiv.org/pdf/2611.31165v1.pdf)

---

## [5. Habitats: A Framework for Open-Ended Evolution of Agent Objectives](https://arxiv.org/abs/2611.31160v1)

**作者**：Nicolas Bolouri, Gaya Mehenni, Daniel Toyama  
**分类**：cs.AI  
**发布时间**：2026-11-23

### 📄 论文摘要

Designing what an agent should optimize can be as difficult as optimizing the agent itself. Existing language-model-based reward-generation methods typically refine objectives for predefined tasks and couple the decision of what to explore with the synthesis of how to implement it, potentially narrowing the resulting behavioral repertoire. We introduce Habitats, a framework for open-ended evolution of executable agent objectives. Habitats maintains a population of reward-policy pairs and evaluates every policy under every population reward, producing a cross-fitness matrix that exposes self-mastery, transfer, and functional diversity. A population-level Planner uses this information to select parent rewards and issue targeted mutation directives, while a separate Mutator translates those directives into validated reward programs. We evaluate Habitats in a discrete Card Sandbox and three continuous-control environments (Cart-Pole, Hopper, and Cheetah) against Independent Generation and Direct Mutation baselines. Across four environments and three random seeds, Habitats achieves the highest macro-averaged final Specialist Quality and Behavioral Diversity, with final diversity reaching 1.8x that of Direct Mutation and 2.5x that of Independent Generation. Finally, across ten downstream objectives unseen during evolution, frozen Habitats policy libraries achieve higher paired win rates than size-matched Direct Mutation and Independent Generation libraries at 10,000 adaptation episodes, while also surpassing task-specific policies trained from scratch for 20,000 episodes. These results suggest that separating population-level planning from reward synthesis enables the discovery of diverse, learnable, and reusable behaviors.

### 🤖 AI 总结

**一句话总结**：Designing what an agent should optimize can be as difficult as optimizing the agent itself. Existing language-model-based reward-generation methods typically refine objectives for predefined tasks and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, Habitats, Framework, Open-Ended, Evolution, Objectives, Designing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31160v1) | [下载PDF](https://arxiv.org/pdf/2611.31160v1.pdf)

---

## [6. Genome-to-Image Translation: Reconstructing Escherichia coli Morphology from Genomic Sequences](https://arxiv.org/abs/2611.31132v1)

**作者**：Son T. Huynh, Thuy T. Le, Thu H. A. Huynh 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-23

### 📄 论文摘要

Antimicrobial resistance in Escherichia coli is established in routine practice by culture-based susceptibility testing, which is slow relative to the clinical need for an early treatment decision. Resistance status also leaves a measurable trace in cell morphology, and whole-genome sequencing of clinical isolates is increasingly available, which raises the question of whether colony appearance can be predicted directly from an isolate's genome. We formulate this as a conditional image-generation problem. The assembled contigs of each isolate are encoded into a single 768-dimensional vector by a frozen genomic language model through a segment-contig-isolate aggregation hierarchy, and a conditional Wasserstein GAN with gradient penalty synthesizes colony images from this embedding together with the applied antibiotic and the resistance label. We train on 167,356 single-cell images from 22 clinical blood isolates imaged under azithromycin, ciprofloxacin, tetracycline, and a no-drug control, compare seven pretrained convolutional backbones inside the generator, and select ConvNeXt-Tiny on distributional image-quality metrics. The synthetic images are then assessed extrinsically: added to a reduced real training set, they improve per-antibiotic resistance classification, with a significant gain in resistant-class recall.

### 🤖 AI 总结

**一句话总结**：Antimicrobial resistance in Escherichia coli is established in routine practice by culture-based susceptibility testing, which is slow relative to the clinical need for an early treatment decision. Re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Genome-to-Image, Translation, Reconstructing, Escherichia, coli, Morphology, Genomic, Sequences

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31132v1) | [下载PDF](https://arxiv.org/pdf/2611.31132v1.pdf)

---

## [7. Preflight: Agentic Last-Mile Verification for AI Software Supply Chains](https://arxiv.org/abs/2611.31110v1)

**作者**：Yaman Jandali, Nojan Sheybani, Farinaz Koushanfar 等 4 位作者  
**分类**：cs.AI, cs.CR  
**发布时间**：2026-11-23

### 📄 论文摘要

Software dependencies execute within the trust boundary of downstream applications, yet provenance, static analysis, and package-level behavioral approaches do not directly determine how a released artifact behaves for a specific program. We present Preflight, a program-scoped pre-execution verifier for Python dependencies that extracts application-referenced symbols, iteratively synthesizes and validates function-level harnesses, executes resolved artifacts in a restricted environment, records behavioral fingerprints, and compares target behavior against prior versions when suitable baselines exist. We evaluate Preflight on four real software-supply-chain incidents under five application contexts, a 100-package benign corpus, and a controlled function-level versus import-only ablation. Preflight returns malicious verdicts in four incident contexts and a clean verdict in the LiteLLM client context, where the affected proxy-server path is not exercised. All 100 evaluated benign packages receive clean verdicts, with zero observed false positives. In a controlled ablation on Ultralytics and ctx, function-level harnesses expose malicious behavior in both incidents, whereas import-only probing exposes neither. Together, these results show that conditioning behavioral verification on the downstream program can expose security-relevant dependency behavior while remaining selective on benign workloads.

### 🤖 AI 总结

**一句话总结**：Software dependencies execute within the trust boundary of downstream applications, yet provenance, static analysis, and package-level behavioral approaches do not directly determine how a released ar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Preflight, Agentic, Last-Mile, Verification, Software, Supply, Chains, dependencies

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31110v1) | [下载PDF](https://arxiv.org/pdf/2611.31110v1.pdf)

---

## [8. SayWhen: Set-Valued Semantic Commitment for Low-Regret Early Speech](https://arxiv.org/abs/2611.31101v1)

**作者**：Tianyi Huang, Lucas Su, Fred Zhang 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-23

### 📄 论文摘要

Speaking early turns a prediction into an irreversible public commitment. We introduce SayWhen, a test-time controller that selects a task-directed act shared across typed continuation plans and controls its release as speech. A persistent veto blocks playback when intervening transcripts invalidate the candidate. We define regret-free early speech (RFES) to measure supported pre-endpoint releases without scored incompatibility. On a 72-prefix branching diagnostic, the generated-plan frontier attains 6.0% RFES with zero observed mean regret, versus 8.2% RFES and 0.068 regret for Matched Top-One. Measured planner latency constrains this path; a deterministic retail schema attains 31.7% RFES, compared with 32.0% for the complete policy. In a separate 30-task $τ$-Voice simulation, schema-derived candidates with cached text-to-speech (TTS) audio attain 21/30 task-level RFES. Eligible audio begins 1.51 seconds before the user-audio endpoint among the 22 tasks with early speech, or 1.11 seconds over all 30 tasks with zero for tasks without eligible early speech. Semantic veto and endpoint waiting each pass 16/30 tasks. Together, the studies demonstrate a controlled coverage-compatibility trade-off and schema-based pre-endpoint operation, making the supported public commitment an explicit unit of voice-agent control.

### 🤖 AI 总结

**一句话总结**：Speaking early turns a prediction into an irreversible public commitment. We introduce SayWhen, a test-time controller that selects a task-directed act shared across typed continuation plans and contr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SayWhen, Set-Valued, Semantic, Commitment, Low-Regret, Early, Speech, Speaking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31101v1) | [下载PDF](https://arxiv.org/pdf/2611.31101v1.pdf)

---

## [9. Tradeoffs between objective outcomes and human enjoyment of work in human-AI task allocation](https://arxiv.org/abs/2611.31095v1)

**作者**：Katherine M. Collins, Elizabeth Mieczkowski, Raja Marjieh 等 8 位作者  
**分类**：cs.AI, cs.HC  
**发布时间**：2026-11-23

### 📄 论文摘要

For people, tasks at work are defined by more than their outcome: they are colored by the experience of engaging in that task. As AI systems become increasingly capable of performing human-level work they may be deployed to tasks that people find enjoyable while simultaneously creating comparatively more aversive tasks such as monitoring AI outputs. This creates a thorny tradeoff for managers: whether work should be assigned purely based on the expected performance of the workers in question, or also account for the subjective experience of the person potentially doing the task. Most economic accounts focus on expected utility calculations based on the former. Here, we assess how people balance objective outcomes and more subjective qualities like enjoyment. In a series of large-scale (N=800) behavioral studies in which people allocate tasks to either an AI or human worker we find that people's allocation decisions are best captured by a model that systematically balances relative objective performance with the human worker's expected enjoyment, weighting human experience higher when a task is framed as inducing less enjoyment and adjusting based on the stakes of the task. As AI also makes decisions about work allocation, we compare a set of LLMs. We find many models also deviate from purely objective decisions, particularly when the project stakes are low, but there is wide heterogeneity as to how much and in what manner they weigh enjoyment. These results raise questions about what role human experience may play in decisions around where and how to integrate AI into workplaces. Integration may be jagged across settings due to consideration not only of the relative capabilities of workers, but also the human experience of work, the valence of that experience (e.g., more strongly weighing aversion), the context (e.g., stakes), and who is making or guiding such choices (human or LLM).

### 🤖 AI 总结

**一句话总结**：For people, tasks at work are defined by more than their outcome: they are colored by the experience of engaging in that task. As AI systems become increasingly capable of performing human-level work ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Tradeoffs, between, objective, outcomes, human, enjoyment, work

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31095v1) | [下载PDF](https://arxiv.org/pdf/2611.31095v1.pdf)

---

## cs.CL

## [10. ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents](https://arxiv.org/abs/2611.31198v1)

**作者**：Rui Sun, Junhua Huang, Luca Zancato 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.CV  
**发布时间**：2026-11-23

### 📄 论文摘要

Recent multimodal search agents use reasoning, vision, and live web search across many turns to answer questions beyond parametric knowledge by orchestrating a small library of hand-crafted search and visual tools. However, the library is laborious to create and maintain, and frozen when new query types, evidence formats, and failure modes are encountered in the wild. Human practitioners, by contrast, cope with insufficient tools by fashioning new ones from familiar parts and reusing them across tasks. Inspired by this, we propose ToolSmith, an automatic tool-generation framework that grows and reuses modules on top of a lean base tool library. We evaluate ToolSmith on three in-domain multimodal search benchmarks and ten out-of-domain benchmarks under a VLM-as-a-Judge protocol. ToolSmith consistently improves over the base library across deployed agents of varying scales, with larger backbones reaping greater gains, demonstrating the scalability of the approach. Our code and data are available at https://threesr.github.io/toolsmith/.

### 🤖 AI 总结

**一句话总结**：Recent multimodal search agents use reasoning, vision, and live web search across many turns to answer questions beyond parametric knowledge by orchestrating a small library of hand-crafted search and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Agent, ToolSmith, Automatic, Tool-Generation, Framework, Multimodal, Search

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31198v1) | [下载PDF](https://arxiv.org/pdf/2611.31198v1.pdf)

---

## [11. Serialization and the Character-System: Measuring Narrative Concentration in French Fiction (1800--1940)](https://arxiv.org/abs/2611.31133v1)

**作者**：Jean Barré, Antoine Bourgois, Thierry Poibeau  
**分类**：cs.CL  
**发布时间**：2026-11-23

### 📄 论文摘要

Every novel divides a finite quantity of narrative attention among its characters, and whether the shape of that division, between a narrative organized around a single figure and one spread across a crowd, has a history is far less settled than the abundance of critical commentary on protagonists might suggest. We operationalize Woloch's notion of the character-system, the distribution of narrative attention across a novel's cast structured by the tension between "the one" and "the many", as the inequality (Gini coefficient) of the PageRank distribution over a character network. We trace this measure of structural concentration across 12,011 French novels published between 1800 and 1940, drawn from the Hors d'usage corpus of Gallica fiction. Over the long nineteenth century the trajectory is U-shaped, with concentration declining to a trough in the 1850s-1860s and rising again through the turn of the century. The change is small, comparable to the difference between a novel built on two co-equal protagonists and one built on a single protagonist, but it is robust to the character cutoff, corpus density, cast size, and author effects. Detective and adventure fiction are less concentrated than the average novel of their period. Literary history reads the roman-feuilleton either as the novel of a superior hero or as a form of proliferating episodes, and on this structural measure our results support the second reading. Across the age of the feuilleton (1840-1914), authors whose careers were structured by newspaper serialization distribute centrality more evenly than a literary control, net of period, genre, and canon. Because such claims are only as trustworthy as the networks they rest on, we also evaluate the extraction pipeline against manually annotated novels, at the levels of cast and character identity.

### 🤖 AI 总结

**一句话总结**：Every novel divides a finite quantity of narrative attention among its characters, and whether the shape of that division, between a narrative organized around a single figure and one spread across a ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：1800--1940, Serialization, Character-System, Measuring, Narrative, Concentration, French, Fiction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31133v1) | [下载PDF](https://arxiv.org/pdf/2611.31133v1.pdf)

---

## [12. Unlocking the Power of Loops in Pretrained LLMs with Loop Residuals](https://arxiv.org/abs/2611.31094v1)

**作者**：Xuanlei Zhao, Hailun Xu, Kai Wang 等 11 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-11-23

### 📄 论文摘要

Looped Transformers iterate a shared block of layers to increase computation without adding parameters, offering stronger performance and test-time scaling. However, this power has so far required training from scratch and yielded only modest gains for LLMs. Finetuning existing models into loops is far cheaper, yet also brings only marginal gains over SFT. We propose LoopRes, an effective, scalable, and simple approach that turns loops into significant and consistent gains for pretrained LLMs. Building on Attention Residuals, LoopRes lets each looped layer attend directly to the outputs of earlier loops. Since these outputs are iterates of the same layers and become harder to tell apart, we give each a trainable loop-aware key that encodes its structural identity. Attending to all earlier loops also lets layers skip intermediate ones, so we restrict each layer to a residual window of the latest W loops, forcing every loop to build incrementally on recent ones. Across 6 pretrained LLMs from 3 model families and 9 benchmarks, LoopRes delivers significant and consistent gains: at 2x compute, it improves Qwen3-1.7B-Base by 29.1% over SFT, more than doubling the gain of the state-of-the-art baseline. The gains hold on larger models up to 30B and across all three families. More importantly, from 1.7B to 8B, LoopRes scales more steeply than SFT as compute grows, reaching a higher ceiling while needing less compute on long outputs. These results establish LoopRes as an effective looping approach, delivering both better performance and better test-time scaling.

### 🤖 AI 总结

**一句话总结**：Looped Transformers iterate a shared block of layers to increase computation without adding parameters, offering stronger performance and test-time scaling. However, this power has so far required tra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Unlocking, Power, Loops, Pretrained, Loop, Residuals

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31094v1) | [下载PDF](https://arxiv.org/pdf/2611.31094v1.pdf)

---

## cs.CV

## [13. Pruning Autonomous Driving VLAs: What to Preserve for Reasoning and Action](https://arxiv.org/abs/2611.31240v1)

**作者**：Seongchan Kim, Soowon Son, Sangoh Kim 等 12 位作者  
**分类**：cs.CV, cs.LG, cs.RO  
**发布时间**：2026-11-23

### 📄 论文摘要

Reasoning vision-language-action (VLA) models for autonomous driving use chain-of-thought (CoT) reasoning to guide action generation, but incur substantial memory and computational costs. We study structured pruning for these models, focusing on preserving both scene understanding and trajectory prediction. Our analysis of Taylor importance in Alpamayo-1.5-10B shows that reasoning and trajectory objectives assign different importance to the same vision-language model (VLM) structures. In the action expert, MLP channels exhibit more stable importance rankings across denoising steps than query heads, and a small fraction of channels accounts for most of the measured importance. Based on these findings, we propose MoOP, which combines importance ranks from both objectives for VLM pruning and aggregates stepwise importance to select a fixed subset of expert MLP channels. At 24.0% total parameter reduction, VLM-only pruning with MoOP performs comparably to or slightly better than the strongest baselines in driving, while retaining 94.0% of the dense model's LingoQA score, far above all other methods. At a higher reduction of 30.0%, MoOP degrades much less than every other method, as it is the only one whose reasoning does not collapse. Removing 93.75% of expert MLP channels increases total parameter reduction to 39.4%, with nearly unchanged open-loop errors relative to VLM-only pruning and competitive closed-loop performance. The resulting model achieves a 1.37x end-to-end inference speedup and 36.6% lower peak memory than the dense model, without post-pruning fine-tuning.

### 🤖 AI 总结

**一句话总结**：Reasoning vision-language-action (VLA) models for autonomous driving use chain-of-thought (CoT) reasoning to guide action generation, but incur substantial memory and computational costs. We study str...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Pruning, Autonomous, Driving, VLAs, What, Preserve, Reasoning, Action

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31240v1) | [下载PDF](https://arxiv.org/pdf/2611.31240v1.pdf)

---

## [14. Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory](https://arxiv.org/abs/2611.31239v1)

**作者**：Chen Wang, Jiahui Huang, Riccardo de Lutio 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-23

### 📄 论文摘要

Exploring a scene from as little as a single photo requires generating a long, camera-controlled walkthrough that extends far beyond what was captured, yet remains consistent upon return. Memory-based video generation methods preserve what they have already seen, but have no anchor beyond it, where the camera drifts from its path and a text prompt can name objects but not place them. Layout-conditioned methods provide such an anchor and precise control over what appears where, but rely on layouts that are typically authored by hand. Both limitations arise because, beyond what was captured, nothing anchors the video model unless a human authors one. To overcome both, we propose Lyris, a long video generation framework that never leaves the video model without an anchor: a persistent point-cloud memory where the scene has been observed or generated, and a 3D layout that a vision-language model authors where it has not. Our key insight is that the interface between the two models can be surprisingly coarse. A layout of one labeled 3D box per object is simple enough for a vision-language model to author (and for a user to edit), yet expressive enough for a video model to follow once rendered along the camera path. We demonstrate walkthroughs of over three minutes and 50 meters from a single photo, passing through doorways into rooms it never shows. When evaluated on minute-long round trips across four datasets, Lyris outperforms state-of-the-art methods by a wide margin, reducing camera error by 3.8x and improving consistency upon return by 22% on average.

### 🤖 AI 总结

**一句话总结**：Exploring a scene from as little as a single photo requires generating a long, camera-controlled walkthrough that extends far beyond what was captured, yet remains consistent upon return. Memory-based...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Lyris, Layout-Guided, Long, Video, Generation, Persistent, Memory

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31239v1) | [下载PDF](https://arxiv.org/pdf/2611.31239v1.pdf)

---

## [15. Modern Self-Supervised Vision Transformers Are Pareidolic](https://arxiv.org/abs/2611.31238v1)

**作者**：Zihang Lin, Huaiyuan Qin, Liangli Zhen 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-23

### 📄 论文摘要

In human perception, pareidolia is the tendency to perceive a meaningful pattern, such as a face, in a random or ambiguous stimulus.We find a similar phenomenon in modern self-supervised Vision Transformers (ViTs): on white noise, which contains neither objects nor spatial structure, a few directions of their features still form spatially coherent patterns across the patches, imposed by the features themselves.We call this behavior pareidolia, and the span of these directions the pareidolic subspace.On natural images, it holds most of the feature variance in DINOv2 and DINOv3 but little in DINO.This excess explains why DINOv2 and DINOv3, despite stronger dense features, fall far behind DINO in object emergence, the hallmark ability of self-supervised ViTs to identify the patches of an object on their own.Our experiments further show that scaling down their pareidolic subspaces steadily restores their ability to discover objects, so their object emergence is hindered rather than lost.These findings naturally lead to a training-free calibration: Pareidolia Subspace Calibration(PSC) measures the pareidolic subspace only on a noise input and then calibrates the features of natural inputs by scaling its directions down to the variance level of the remaining directions.Across diverse object emergence tasks, PSC improves DINOv2 and DINOv3 by up to 31.7 CorLoc on object discovery, 30.2 maxF on saliency detection and 59.9~$\mathcal{J}$ on video object segmentation.To identify the cause of pareidolia, we trace it block by block and find that it forms in the middle blocks of every self-supervised model we examine but stays strong to the last block only in models trained with a patch-level loss; controlled training confirms that an image-level loss alone lets it fade.

### 🤖 AI 总结

**一句话总结**：In human perception, pareidolia is the tendency to perceive a meaningful pattern, such as a face, in a random or ambiguous stimulus.We find a similar phenomenon in modern self-supervised Vision Transf...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Modern, Self-Supervised, Vision, Transformers, Pareidolic, human, perception, pareidolia

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31238v1) | [下载PDF](https://arxiv.org/pdf/2611.31238v1.pdf)

---

## [16. TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming](https://arxiv.org/abs/2611.31233v1)

**作者**：Hani Alomari, Md Atabuzzaman, Chris Thomas  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-23

### 📄 论文摘要

CLIP-style dual encoders map images and text through two separate towers into a shared embedding space, where the two modalities occupy distinct regions separated by a modality gap. Retrieval fails when wrong matches, or hard negatives, outrank the correct one, and the gap is the usual suspect. Yet removing it post hoc degrades retrieval on every CLIP checkpoint we test. We introduce a paired statistic that identifies directions where the two towers agree more on hard negatives than on matched pairs. Mildly attenuating these directions improves retrieval while largely preserving the gap. We arrive at this correction through weight-space programming: guided by the statistic, an LLM agent inspects both towers and writes closed-form weight edits without backpropagation. Free to edit any component, the agent improves COCO test retrieval on all 13 CLIP checkpoints and edits an output projection in 12 of the 13. We distill and refine its recurring correction into TowerBridge, a closed-form recipe motivated by a first-order analysis of the hard-negative margin. Computed in seconds from 25,000 labelled pairs, it requires no model-specific tuning and leaves the architecture and inference cost unchanged. TowerBridge improves COCO test retrieval by 16.8 RSUM and Flickr30k test retrieval by 6.6 on average across all 21 evaluated CLIP checkpoints, including 8 unseen by the agent, while limiting any drop in ImageNet zero-shot accuracy to 0.5 points. It also reduces hubness on all 21 checkpoints and improves retrieval on 4 of 5 dual encoders from other families.

### 🤖 AI 总结

**一句话总结**：CLIP-style dual encoders map images and text through two separate towers into a shared embedding space, where the two modalities occupy distinct regions separated by a modality gap. Retrieval fails wh...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TowerBridge, Bridging, Dual-Encoder, Modality, Gap, via, Weight-Space, Programming

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31233v1) | [下载PDF](https://arxiv.org/pdf/2611.31233v1.pdf)

---

## [17. Self-Supervised Dataset Distillation via Mutual Information Maximization](https://arxiv.org/abs/2611.31225v1)

**作者**：Mohammad Hossein Moslemi, Mahdi Beitollahi, Zhimin Mei 等 6 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-23

### 📄 论文摘要

Dataset distillation (DD) aims to compress a large dataset into a small synthetic one that remains effective for training neural networks. Despite its success in supervised learning, DD remains underexplored in self-supervised learning (SSL), where distilled data must preserve the information needed to learn representations that remain consistent across augmentations. To bridge this gap, we introduce Mutual Information Prototype Alignment (MIPA), an efficient SSL dataset distillation approach that optimizes synthetic images to preserve augmentation-invariant information. Specifically, MIPA treats synthetic images as learnable prototypes and uses a frozen encoder to assign real samples to them based on feature similarity. A synthetic dataset that preserves such augmentation invariance should yield stable prototype assignments across multiple augmented views of the same real image. MIPA encourages this by maximizing mutual information between cross-view assignments while avoiding trivial solutions in which all real samples are assigned to only a few synthetic prototypes. Evaluations on image classification benchmarks show that synthetic data generated by MIPA yield higher-quality representations than existing distillation approaches while reducing time and storage demands during distillation.

### 🤖 AI 总结

**一句话总结**：Dataset distillation (DD) aims to compress a large dataset into a small synthetic one that remains effective for training neural networks. Despite its success in supervised learning, DD remains undere...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DD, Self-Supervised, Dataset, Distillation, via, Mutual, Information, Maximization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31225v1) | [下载PDF](https://arxiv.org/pdf/2611.31225v1.pdf)

---

## [18. CTLink: A Text-Prompted Segmentation Model for Linking Radiology Report Findings to 3D Chest CT Scans](https://arxiv.org/abs/2611.31222v1)

**作者**：Mohammed Baharoon, Sung Eun Kim, Mahmoud Hussain Alabbad 等 36 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-23

### 📄 论文摘要

Radiology reports describe findings in text only, without visually marking them on the scan, so readers cannot directly see which abnormality each reported finding refers to. We introduce CTLink, a text-prompted 3D segmentation model that segments findings described in a chest CT report. CTLink was trained on 4123 noncontrast chest CT scans with 9547 segmented report findings, including ReXGroundingCTv2, a newly annotated dataset of 1134 scans and 1895 findings with every instance of each finding segmented. On the 200 ReXGroundingCT validation scans, CTLink achieved a hit rate of 0.816, an instance F1 score of 0.456, and a mean Dice score of 0.400, compared with 0.533, 0.175, and 0.234 for VoxTell, a publicly available text-prompted segmentation model (P < .001 for all). On the test set of the MICCAI 2026 ReXGrounding challenge, an ensemble of seven CTLink models achieved the highest hit rate (0.782) and instance F1 score (0.386) of all 48 participating teams. On 50 test scans segmented twice by independent radiologists, CTLink matched or exceeded inter-rater agreement. Diffuse non-focal findings remained the main limitation, partly because their extent is outlined inconsistently even between radiologists. The CTLink model weights are available at https://huggingface.co/rajpurkarlab/CTLink, and the dataset at https://huggingface.co/datasets/rajpurkarlab/ReXGroundingCT.

### 🤖 AI 总结

**一句话总结**：Radiology reports describe findings in text only, without visually marking them on the scan, so readers cannot directly see which abnormality each reported finding refers to. We introduce CTLink, a te...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CTLink, Text-Prompted, Segmentation, Model, Linking, Radiology, Report, Findings

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31222v1) | [下载PDF](https://arxiv.org/pdf/2611.31222v1.pdf)

---

## [19. LeJEPA Features Are Not Isotropic, and Should Not Be](https://arxiv.org/abs/2611.31216v1)

**作者**：Richeek Das, Pratik Chaudhari  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-23

### 📄 论文摘要

The SIGReg term in LeJEPA regularizes features to have an isotropic Gaussian distribution. Our first result is to show that this regularizer, in practice, cannot achieve its goal. We design a modified regularizer to enforce the objective better. This leads to slightly improved performance. For example, on ImageNet-100, our modified regularizer reaches the final accuracy of SIGReg in 1.3$\times$ fewer epochs. Our second result argues that self-supervised encoders should not have isotropic Gaussian features. We show that the alignment term in LeJEPA conflicts with SIGReg, because it couples the magnitude of the features with their directions. In contrast, isotropic Gaussian features would entail independent magnitude and directions. Features obtained with LeJEPA are, in fact, not isotropic. So LeJEPA has two issues. Its regularizer is weak, and the isotropic Gaussian target is too strict. Our third result is about reformulating the isotropic Gaussian regularizer to enforce only the marginal distributions of the magnitude and direction, without enforcing independence. This leads to a simple regularization term, PolarReg, that can be optimized reliably across many different datasets, batch sizes and embedding dimensions without any hyper-parameter changes. On ImageNet-1k, our technique matches the accuracy of LeJEPA and its variants in 4.7$\times$ fewer epochs. It improves the final accuracy by 1.8 points.

### 🤖 AI 总结

**一句话总结**：The SIGReg term in LeJEPA regularizes features to have an isotropic Gaussian distribution. Our first result is to show that this regularizer, in practice, cannot achieve its goal. We design a modified...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Be, LeJEPA, Features, Not, Isotropic, Should, SIGReg, term

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31216v1) | [下载PDF](https://arxiv.org/pdf/2611.31216v1.pdf)

---

## [20. SPROUT: Predicting Objective-Grounded Prompt Utility for Efficient Text-to-Image Preference Tuning](https://arxiv.org/abs/2611.31163v1)

**作者**：Kangping Hu, Akshay Mehra, Stephen Mussmann  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-23

### 📄 论文摘要

Preference tuning of text-to-image diffusion models spends most of its compute generating candidate images, yet training prompts are typically sampled uniformly at random, wasting compute generating images that provide too little signal for model alignment. To best utilize the available compute, we study prompt selection, where at each iteration we identify the most useful prompts for preference tuning. We separate prompt selection into a utility score, an estimator of that utility score, and batch selection. Within this framework, we propose Selection by PRedicting Objective-grounded UTility (SPROUT). The utility score is predicted on every prompt in the pool, including unseen prompts, by a text-only model, refit after every iteration on all utilities observed so far. A randomized acceptance rule then turns these predictions into a batch, so no images are generated beyond those used for training. For direct group preference optimization (DGPO), the objective-grounded utility is the norm of the gradient that the objective produces from a prompt's group of images. Fine-tuning Stable Diffusion 1.5 with DGPO on GenEval, SPROUT matches the final score of uniform sampling in about 44% of the iterations and improves the area under the learning curve with respect to both uniform sampling and CGPO, a recent variance-based prompt sampler. The efficiency gains hold under four held-out reward models never used in training, and the ranking of methods carries over to DPG-Bench and T2I-CompBench++. Our code is available at https://github.com/ADDAPT-ML/SPROUT.

### 🤖 AI 总结

**一句话总结**：Preference tuning of text-to-image diffusion models spends most of its compute generating candidate images, yet training prompts are typically sampled uniformly at random, wasting compute generating i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SPROUT, Predicting, Objective-Grounded, Prompt, Utility, Efficient, Text-to-Image, Preference

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31163v1) | [下载PDF](https://arxiv.org/pdf/2611.31163v1.pdf)

---

## [21. Analyzing and Improving FlowMap Distillation of Autoregressive Video Models](https://arxiv.org/abs/2611.31164v1)

**作者**：Yong-Hyun Park, Guande He, Joon Hyeok Kim 等 8 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-23

### 📄 论文摘要

FlowMap distillation offers a natural route to few-step generative modeling by directly learning a teacher's denoising trajectories. Yet for autoregressive (AR) video generation, existing few-step models still rely on distribution matching distillation (DMD) to remain competitive, sacrificing sample diversity and requiring a large bidirectional teacher. In this work, we analyze what limits standalone AR FlowMap distillation and introduce two complementary guidance mechanisms to close this gap: (1) anti-drifting guidance, which helps the AR teacher correct drifted student rollouts by training an auxiliary model to mimic student drift and using it as a negative guidance branch; and (2) motion-aware guidance, which makes motion easier for a FlowMap student to learn by locating motion patches and selectively applying skip-layer guidance. Empirically, our approach applies to $π$-Flow, MeanFlow, and consistency distillation with 1.3B AR teachers, improving generation quality and reducing drift over 30 s rollouts. Notably, our 4-step $π$-Flow students match DMD students distilled from 14B teachers on VBench while preserving the sample diversity of their AR teachers, demonstrating that pure FlowMap distillation is effective for few-step autoregressive video generation.

### 🤖 AI 总结

**一句话总结**：FlowMap distillation offers a natural route to few-step generative modeling by directly learning a teacher's denoising trajectories. Yet for autoregressive (AR) video generation, existing few-step mod...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Analyzing, Improving, FlowMap, Distillation, Autoregressive, Video, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31164v1) | [下载PDF](https://arxiv.org/pdf/2611.31164v1.pdf)

---

## [22. CrownFusion: 3D Dental Crown Generation Using Geometry Images and Latent Diffusion](https://arxiv.org/abs/2611.31128v1)

**作者**：Johan Ziruo Ye, Xingguang Yan, Søren Hauberg 等 6 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-11-23

### 📄 论文摘要

We introduce CrownFusion, a latent diffusion model to generate 3D dental crown designs from geometry images, a 2D-grid encoding of surface coordinates. Departing from traditional approaches that use point clouds, our "CrownImage" representation not only unlocks the full power of image-based generative architectures, but also preserves fine geometric detail by operating at far higher spatial resolutions than point clouds to alleviate smoothing artifacts in the 3D generation. Conditioned on jointly learned embeddings of the surrounding dentition, our probabilistic diffusion model produces anatomically plausible crowns with morphological variations tailored to individual patient cases. To accommodate multiple valid designs, we propose an occlusal fit metric based on proximity to the antagonist teeth. We evaluate our method through quantitative experiments and qualitative studies involving expert testimonials. We also release the FDI 16 Crown Dataset, comprising 11,513 annotated intra-oral scans, to support future research in dental CAD.

### 🤖 AI 总结

**一句话总结**：We introduce CrownFusion, a latent diffusion model to generate 3D dental crown designs from geometry images, a 2D-grid encoding of surface coordinates. Departing from traditional approaches that use p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, CrownFusion, Dental, Crown, Generation, Geometry, Images, Latent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31128v1) | [下载PDF](https://arxiv.org/pdf/2611.31128v1.pdf)

---

## [23. Leakage-Safe Auditing of Attribution-Driven Data Curation in Medical Imaging](https://arxiv.org/abs/2611.31096v1)

**作者**：Malay Phadke, Akshay Gokhale  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-23

### 📄 论文摘要

When can an attribution-derived anomaly justify changing a medical-imaging training set? We formulate attribution-driven curation as three separately testable claims: anomaly detection, harmfulness estimation, and intervention utility. We test the first and third using a patient-disjoint, identifier-preserving audit of a 3D convolutional classifier for computed tomography angiography aneurysm candidates. We identify 232 exactly zero-valued arrays among 1,201 positive patches, including 170 training positives, and invalidate a historical 321-patch attention-failure subgroup whose identifier-free records were joined to files by position. On the held-out test set, GradCAM++ spatial concentration is central for every candidate class, reversing the historical pattern. GradCAM++ and Integrated Gradients show negative rank-order agreement for positives, limiting method-independent anatomical interpretation. Across five paired training seeds, removing the 170 corrupted training positives yields AUC 0.9617 +/- 0.0044 versus 0.9652 +/- 0.0039 for full-data training (difference -0.0035; 95% CI -0.0082 to 0.0007). Excluding 34 raw-zero test positives widens rather than closes the gap, countering a blank-memorization explanation. Budget-matched random-removal controls suggest the result is not simply an effect of reducing training size. Input corruption does not necessarily imply that deletion improves generalization. Our framework makes leakage control, sample identity, and intervention testing explicit in attribution-driven medical-imaging data curation.

### 🤖 AI 总结

**一句话总结**：When can an attribution-derived anomaly justify changing a medical-imaging training set? We formulate attribution-driven curation as three separately testable claims: anomaly detection, harmfulness es...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Leakage-Safe, Auditing, Attribution-Driven, Data, Curation, Medical, Imaging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31096v1) | [下载PDF](https://arxiv.org/pdf/2611.31096v1.pdf)

---

## cs.LG

## [24. How Far Can Linear Go? BiPert, a Unified Framework for Single-Cell Perturbation Modelling](https://arxiv.org/abs/2611.31227v1)

**作者**：Abhishek Sharma, Aleksej Zelezniak  
**分类**：cs.LG, q-bio.CB, q-bio.GN, q-bio.QM  
**发布时间**：2026-11-23

### 📄 论文摘要

Understanding how genetic perturbations affect cellular behaviour is essential for studying gene function and regulatory mechanisms. Large-scale CRISPR screens measure these effects across thousands of genes, but cover relatively few cellular contexts. Predicting perturbation responses in unseen cell types and identifying perturbed genes from their transcriptional effects therefore remain challenging. Here, we show that both tasks can be addressed through a common linear decomposition of transcriptional responses into shared and perturbation-specific components. Building on this principle, we introduce BiPert, a simple linear framework for both forward perturbation prediction and inverse identification. For forward prediction, BiPert outperforms existing methods that use no external biological knowledge when predicting gene expression changes in unseen cell lines. Its few-shot extension, BiPert-FS, adapts to new cell lines using as few as ten measured perturbations. For inverse identification, BiPert-ID identifies perturbed genes from single-cell expression profiles, outperforming deep-learning methods in unseen cell lines and donors. We further show that perturbations whose effects transfer more consistently across cellular contexts are also easier to identify, even after controlling for perturbation effect size. Together, these results establish a connection between perturbation transfer and identification, and demonstrate that simple linear models provide strong, interpretable baselines for both tasks.

### 🤖 AI 总结

**一句话总结**：Understanding how genetic perturbations affect cellular behaviour is essential for studying gene function and regulatory mechanisms. Large-scale CRISPR screens measure these effects across thousands o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Go?, How, Far, Can, Linear, BiPert, Unified, Framework

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31227v1) | [下载PDF](https://arxiv.org/pdf/2611.31227v1.pdf)

---

## [25. Agentic AI for Intent Management and Control in Autonomous Communication Networks](https://arxiv.org/abs/2611.31223v1)

**作者**：Burak Demirel, Yu Wang, Pablo Soldati  
**分类**：cs.LG  
**发布时间**：2026-11-23

### 📄 论文摘要

Artificial intelligence (AI)-driven automation will help future mobile networks translate high-level network intents into concrete network optimization or control actions. However, existing approaches often focus on intent management and orchestration, leaving the adaptation of underlying network optimization and control functions largely unaddressed. This article proposes a triadic agentic AI framework that co-designs intent management and intent fulfillment through three agents: an interpreter, powered by a language model, that translates and refines intents into machine-readable optimization templates; an optimizer that adapts controller policies to intent specifications; and a controller that performs fast decision-making. We discuss the design space of each agent and how the workflow can be embedded across network architectural domains. Finally, we develop a concrete realization combining a language-model interpreter with Bayesian optimization for the optimizer and multi-objective reinforcement learning for the controller, and evaluate it in a radio resource management case study for differentiated connectivity. Results demonstrate how the agentic AI framework can connect high-level intents with runtime network control, showing adaptability of intent specifications and control policies to service requirements and changing network conditions.

### 🤖 AI 总结

**一句话总结**：Artificial intelligence (AI)-driven automation will help future mobile networks translate high-level network intents into concrete network optimization or control actions. However, existing approaches...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agentic, Intent, Management, Control, Autonomous, Communication, Networks, Artificial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31223v1) | [下载PDF](https://arxiv.org/pdf/2611.31223v1.pdf)

---

## [26. Matching Under Metric Privacy](https://arxiv.org/abs/2611.31208v1)

**作者**：Hongyi B. Hu, Dung Nguyen, M. Amin Rahimian  
**分类**：cs.LG, cs.CR, cs.SI, math.PR  
**发布时间**：2026-11-23

### 📄 论文摘要

We study how to represent and randomize points in $d$-dimensional Euclidean space to obtain accurate bipartite matchings under metric privacy. Given $n$ private and $n$ public points, we analyze local mechanisms that randomize each private point or its distances to the public points. Using the public points' affine span, we construct a smaller representation that preserves all matching costs. When a trusted server receives the private points, we establish privacy and utility guarantees for Gumbel matching, which randomizes edge costs and releases only the assignment. Through upper bounds and worst-case constructions, we establish the tight rate $Θ\!\left(n\min\{d,\log n\}/\varepsilon\right)$ for expected cost above the nonprivate optimum. Benchmark experiments support $d\approx\log n$ as a practical guide to the transition between directly randomizing point coordinates and using Gumbel matching. Extensions to squared Euclidean costs enable private nonparametric two-sample hypothesis testing. These results show how the application's trust model guides representation and dimension choices for better utility: under local privacy, low-dimensional point representations reduce excess cost, while under central privacy, distance representations achieve the optimal rate even in high dimension.

### 🤖 AI 总结

**一句话总结**：We study how to represent and randomize points in $d$-dimensional Euclidean space to obtain accurate bipartite matchings under metric privacy. Given $n$ private and $n$ public points, we analyze local...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Matching, Under, Metric, Privacy, study, how, represent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31208v1) | [下载PDF](https://arxiv.org/pdf/2611.31208v1.pdf)

---

## [27. Learning Neurovascular Codes for EEG-to-fMRI Synthesis](https://arxiv.org/abs/2611.31194v1)

**作者**：Yiming Sun, Yifan Wang, Aosong Feng 等 14 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-23

### 📄 论文摘要

In this paper, we introduce Neurovascular Codes as shared EEG representations for fMRI generation. We first train a separate EEG encoder to predict each fMRI signal, learning target-specific temporal and spectral features from the same EEG window. After training, we freeze the encoders and project their concatenated hidden features into a shared neurovascular code. Conditioned on this code, stochastic interpolant transforms Gaussian noise into a vector of fMRI signals, allowing different responses to be sampled for the same EEG window. We evaluate our approach on eight public simultaneous EEG-fMRI datasets, including four resting-state and four task-based datasets with 61,646 volume-level pairs. Under within-subject and held-out-subject evaluation, our model improves average Pearson correlation over the strongest encoder baselines by 19.1% and 19.8%, respectively. The corresponding improvements over the strongest generator baselines are 18.8% and 47.9%. Beyond reconstruction accuracy, we also evaluate the generated signals using subject-identification classifiers trained on real fMRI. Our method achieves the highest mean accuracy among the evaluated generators. We hope that our work opens up new opportunities for cross-modal brain modeling.

### 🤖 AI 总结

**一句话总结**：In this paper, we introduce Neurovascular Codes as shared EEG representations for fMRI generation. We first train a separate EEG encoder to predict each fMRI signal, learning target-specific temporal ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：we, Learning, Neurovascular, Codes, EEG-to-fMRI, Synthesis, paper, introduce

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31194v1) | [下载PDF](https://arxiv.org/pdf/2611.31194v1.pdf)

---

## [28. Precision-Aware Learning Rate Transfer Across Block Count in LLM Post-Training](https://arxiv.org/abs/2611.31166v1)

**作者**：Nan Chen, Soledad Villar, Soufiane Hayou  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-11-23

### 📄 论文摘要

The post-training of pretrained large language models, including supervised finetuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable reward (RLVR), is very sensitive to the learning rate, and tuning it through grid search is costly in both computation and memory. In this work, we propose \textbf{TipSweep}, a method to transfer the learning rate across the number of trainable transformer blocks. To do so efficiently, we search for the best learning rate by training only the last $k_0$ blocks (in our experiments, typically $k_0=1$), and provide scaling rules that predict the optimal learning rate when training any set of $k$ blocks, including when $k=L$ (the full transformer). Across experiments with models ranging from 1 to 7 billion parameters, we observe that the optimal learning rate follows precision-dependent scaling rules: the optimal rate scales approximately as $k^{-1}$ with float32 (FP32) master weights, but as $k^{-1/2}$ when updates are applied directly to bfloat16 (BF16) weights without a master copy. We explain both rules using an analytical model that accounts for update rounding, under assumptions supported by profiling experiments. Finally, we develop two prototypes of the learning rate search for a 6.7-billion-parameter model. The first fits the search on a single consumer GPU with 16 GiB of memory. The second speeds up the search on a high-end GPU by evaluating all candidate learning rates in a single pass over the data, so that a five-candidate search takes about half the GPU hours of one full-depth ($k=L$) run.

### 🤖 AI 总结

**一句话总结**：The post-training of pretrained large language models, including supervised finetuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable reward (RLVR), is very se...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Precision-Aware, Learning, Rate, Transfer, Across, Block, Count

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31166v1) | [下载PDF](https://arxiv.org/pdf/2611.31166v1.pdf)

---

## [29. Site-Conditioned Boundary Closure for Subsurface Seepage Forecasting and Relief Placement](https://arxiv.org/abs/2611.31125v1)

**作者**：Edward Holmberg, Elias Ioup, Mahdi Abdelguerfi  
**分类**：cs.LG  
**发布时间**：2026-11-23

### 📄 论文摘要

Truncating a large heterogeneous diffusion model around a localized, threshold-activated outlet saves degrees of freedom but severs exterior feedback that governs when the outlet opens and how much it discharges. By separating forcing-driven background head from local withdrawal drawdown, Site-Conditioned Boundary Closure (SCBC) maps local physical descriptors to positive exchange coefficients at the cut boundary. Supervised on unforced donor-domain withdrawal responses, these coefficients yield a passivity-preserving reduced operator that generalizes across unseen forcing histories without refitting. We evaluate SCBC on flood-driven subsurface seepage beneath levee foundations against full-grid reference simulations (MODFLOW~6). Across three held-out foundation panels, a single frozen SCBC tree estimator reduced peak-discharge log RMSE by 26.1%, 30.9% and 42.6% relative to identical local patches using a shared boundary coefficient. We then test whether better screening forecasts improve constrained placement, minimizing peak landside toe head subject to a discharge capacity limit and a budget of three sequential full-grid checks. On a separate 36-foundation test using a coarser 30-state ring operator, a neural SCBC estimator improved discharge forecasts across candidates yet selected four over-capacity placements before checks, compared with one for a shared-coefficient ring, which recovered all 144 reference optima after three checks.

### 🤖 AI 总结

**一句话总结**：Truncating a large heterogeneous diffusion model around a localized, threshold-activated outlet saves degrees of freedom but severs exterior feedback that governs when the outlet opens and how much it...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Site-Conditioned, Boundary, Closure, Subsurface, Seepage, Forecasting, Relief, Placement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31125v1) | [下载PDF](https://arxiv.org/pdf/2611.31125v1.pdf)

---

## [30. Attention Temperature Confounds Zero-Shot Context Extension](https://arxiv.org/abs/2611.31113v1)

**作者**：Ruben Navasardyan  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-11-23

### 📄 论文摘要

A training-time attention change is usually judged for zero-shot context extension against a dense baseline beyond the training length at the default temperature, $τ= 1$. The outcome depends on how miscalibrated the baseline is there: the share of perplexity it recovers when its logits are sharpened by one scalar. Under the standard recipe (fp32 master weights), an 8k-trained baseline is 8-15% miscalibrated at 30k in three seed-paired 365M twins; in one of them this makes the block-sparse-trained twin look 7% better, which calibration removes. In pure-bf16 training without master weights the miscalibration is several times larger: an AdamW step ($β_2 = 0.95$) on a gain initialised at 1.0 is below half the bf16 spacing at peak learning rates under $1.7\times10^{-3}$, so gains never move (22 checkpoints), the baseline is 37-58% miscalibrated, and block-sparse pretraining, attention dropout and ALiBi look 6-35% better. Calibrating one temperature per model and length removes all three advantages, leaves ALiBi 5% behind RoPE and keeps part of the gain of a positive control, NTK-aware scaling. Unfreezing the gains reverses the block-sparse advantage at 365M and removes 71-89% of it at 1.2B. We recommend reporting extension results at calibrated temperatures and checking that normalisation gains moved.

### 🤖 AI 总结

**一句话总结**：A training-time attention change is usually judged for zero-shot context extension against a dense baseline beyond the training length at the default temperature, $τ= 1$. The outcome depends on how mi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Attention, Temperature, Confounds, Zero-Shot, Context, Extension, training-time, change

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.31113v1) | [下载PDF](https://arxiv.org/pdf/2611.31113v1.pdf)

---

