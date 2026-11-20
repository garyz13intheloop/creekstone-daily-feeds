# arXiv AI 论文日报 | 2026-11-20

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (15 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.CL](#csCL) (3 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. MM-SystemOneBias: Evaluating Bias in Multimodal Jev-Style System One Decision Models](https://arxiv.org/abs/2611.26557v1)

**作者**：Jinzhe Li, Qi Wang, Dandan Guo 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-19

### 📄 论文摘要

When multimodal decision models determine actions, moderation outcomes, or quality judgments, their reliability depends on preserving semantic decisions across presentation changes, ignoring irrelevant additions, and distinguishing information consistent with task evidence from information that conflicts with it. Existing evaluations study decision-interface biases and multimodal model behavior in separate settings, leaving no common protocol to compare multimodal decision models with their backbones on practical tasks. We introduce \textbf{MM-SystemOneBias}, which evaluates 13 models on 5,323 original instances from nine public datasets and 11 task scenarios using six paired interventions: option order, option label, external judgment, image--text description, irrelevant information, and rating scale. Across seven matched decision-model--backbone pairs, decision models are more stable under option-label, irrelevant-information, and rating-scale changes in all seven pairs; six pairs also show lower option-order flip rates. They incur smaller accuracy losses under incorrect external judgments in all seven pairs and conflicting descriptions in six. In six pairs, they gain less accuracy from correct external judgments and show less favorable accuracy changes under consistent descriptions. Among pairs with unchanged semantic decisions, mean absolute changes in answer probabilities range from 4.56 to 11.55 percentage points, revealing input effects that accuracy alone misses.

### 🤖 AI 总结

**一句话总结**：When multimodal decision models determine actions, moderation outcomes, or quality judgments, their reliability depends on preserving semantic decisions across presentation changes, ignoring irrelevan...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MM-SystemOneBias, Evaluating, Bias, Multimodal, Jev-Style, System, One, Decision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26557v1) | [下载PDF](https://arxiv.org/pdf/2611.26557v1.pdf)

---

## [2. The Geometry of Lies: Knowledge and Persona Directions for Detecting Deception in Large Language Models](https://arxiv.org/abs/2611.26545v1)

**作者**：Md. Abdullah Al Zami, Suraiya Shanaz, Mahdi Hasan 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-19

### 📄 论文摘要

Linear probes are the cheapest LLM lie detectors but often fail to transfer across kinds of lie. Label-free directions from honest and deceptive role-play are untested at 70B scale and on lies about knowledge, where a lie and an honest denial can be identical. We widen a published persona bank with roles that deny knowledge they have, plus honest counterparts. At each model's middle layer the resulting persona direction ranks lies across Liars' Bench better than single-dataset probes on three of its four models; it fails on Qwen, even when Qwen stays in role far more often. On Llama-3.3-70B-Instruct it beats directions from a random persona bank, but its gain over the published direction is within the range of random widenings. On lies about knowledge, persona directions mainly track a reply's wording: where lies and honest denials share their words, our three main contrasts stay inside the random-direction band on Llama and Qwen and reach only its edge on Gemma, though on Mistral one clears it. A knowledge direction contrasts questions the model can answer with ones nobody can, each followed by the same scripted denial. It separates lies from identical honest denials on two models and narrowly on a third, but not on the fourth; its other results partly depend on the benchmark's wording. On the Gender-Secret fine-tune it clears the band by a few hundredths on Llama and fails on Mistral. The sum of the two directions ranks lies better than a supervised probe at the same depth on all four models (on one, both near chance) but is level with the persona direction on Llama's average and behind that probe on held-out lies. More varied role-play questions do not help the persona direction on Liars' Bench.

### 🤖 AI 总结

**一句话总结**：Linear probes are the cheapest LLM lie detectors but often fail to transfer across kinds of lie. Label-free directions from honest and deceptive role-play are untested at 70B scale and on lies about k...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Geometry, Lies, Knowledge, Persona, Directions, Detecting, Deception

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26545v1) | [下载PDF](https://arxiv.org/pdf/2611.26545v1.pdf)

---

## [3. LLM GerryMandering: Separating Interactions from Additive Effects in LLM Audits](https://arxiv.org/abs/2611.26538v1)

**作者**：George Rahul, Ronit Jahilal, Bhaskara Hanuma Vedula 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-19

### 📄 论文摘要

Intersectional bias arises when a model treats people who hold several marginalised identities at once differently from what their separate identities would predict. Auditing such intersectional subgroups remains a challenge: their number grows quadratically, and there is no agreed baseline for what independent attributes would predict. Without such a baseline, many existing audits flag a subgroup when it exceeds each attribute alone, a condition that attributes acting independently already satisfy. We test this standard criterion on 150 synthetic datasets built with no interaction. With the shuffle null, it flags 66.1 false subgroups per dataset on average, and at least one in every dataset. When we plant interactions of known size into these datasets, a repaired null lets the criterion recover only 32% of them. We introduce ADDIS (Additive Intersectional Screen), which fits an additive model over all attributes, scores each subgroup by its Additive Residual Distance (ARD) from that model's prediction, and tests it against a Freedman-Lane null. On our synthetic benchmark, ADDIS flags 0.09 false subgroups per dataset and recovers 84% of the same planted interactions. We then build IndiPersona, 10,000 synthetic Indian personas with six identity attributes, and audit 13 open language models. The standard criterion flags 7.1% of the 738 tested subgroups on average; ADDIS flags 3.0%. Gender identity crossed with sexual orientation is the largest pairing in every model, and counterfactual personas confirm it and additionally reveal a caste x class interaction in all but one model that the observational test lacked the data to detect. Much of what audits report as intersectional bias can thus arise from independent single-attribute effects alone, yet a small core of interactions survives.

### 🤖 AI 总结

**一句话总结**：Intersectional bias arises when a model treats people who hold several marginalised identities at once differently from what their separate identities would predict. Auditing such intersectional subgr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, GerryMandering, Separating, Interactions, Additive, Effects, Audits, Intersectional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26538v1) | [下载PDF](https://arxiv.org/pdf/2611.26538v1.pdf)

---

## [4. FLUID: Flexible, Evidence-Grounded Situated Task Guidance](https://arxiv.org/abs/2611.26491v1)

**作者**：Yunqi Zhao, Run Peng, Ze Dong 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-19

### 📄 论文摘要

Real-time task guidance is inherently flexible: when an agent guides a user through a task, multiple responses and timings can be appropriate, and sometimes the best action is to remain silent. Existing benchmarks often miss this flexibility by treating synthesized dialogues as fixed targets for what to say and when to say it. We introduce FLUID (Flexible, Evidence-Grounded Situated Task Guidance), a unified framework for modeling, evaluating, and enabling flexible interaction in multimodal task guidance. Using naturally occurring human-human guidance from WTaG and HoloAssist, FLUID grounds interventions in their supporting evidence, necessity, and timing flexibility, and uses this representation both to evaluate flexible guidance and to build a real-time agent for task guidance. Our agent achieves the strongest overall balance of response correctness, intervention precision, timely guidance, and response latency among evaluated systems, while still leaving room for improvement in avoiding speech overlap. Together, FLUID moves situated task guidance beyond rigid reference matching toward more natural and adaptive human-AI interaction. Project page: https://fluid-guidance.github.io.

### 🤖 AI 总结

**一句话总结**：Real-time task guidance is inherently flexible: when an agent guides a user through a task, multiple responses and timings can be appropriate, and sometimes the best action is to remain silent. Existi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FLUID, Flexible, Evidence-Grounded, Situated, Task, Guidance, Real-time, inherently

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26491v1) | [下载PDF](https://arxiv.org/pdf/2611.26491v1.pdf)

---

## [5. Monte Carlo Pass Search for Setpieces](https://arxiv.org/abs/2611.26464v1)

**作者**：Andrew Kang  
**分类**：cs.AI  
**发布时间**：2026-11-19

### 📄 论文摘要

Set pieces produce about a third of non-penalty expected goals (xG), yet they are usually evaluated by what happened next. We present Monte Carlo Pass Search (MCPS) for set pieces, which treats a corner or a lofted free kick as a distribution over plausible executions and plausible futures instead of a single realised event. From the pre-kick state, MCPS proposes counterfactual deliveries and counterfactual set-ups (where the attackers stand at the kick), plays each out many times in a world model (3D ball physics, a generative model of all 22 players, the keeper's come-or-stay decision and a Player-to-Touch model) and scores every future with a value model. On 249 deliveries from 30 Serie A 2025/26 matches, with every model applied only to matches it never saw, the best available delivery is worth 0.0085 xG more than the one kicked (+28 %), mainly because it reaches an attacker before the keeper. Searching where the attackers stand as well adds +0.0027 xG with the observed ball and +0.0033 on top of the best ball; designing their runs too adds +0.0007 more. We show how to keep such a search honest, and estimate how much more data each component needs before a club could rely on it.

### 🤖 AI 总结

**一句话总结**：Set pieces produce about a third of non-penalty expected goals (xG), yet they are usually evaluated by what happened next. We present Monte Carlo Pass Search (MCPS) for set pieces, which treats a corn...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Monte, Carlo, Pass, Search, Setpieces, Set, pieces, produce

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26464v1) | [下载PDF](https://arxiv.org/pdf/2611.26464v1.pdf)

---

## cs.CL

## [6. Represented but misread: Post-training changes how language models read out what they represent](https://arxiv.org/abs/2611.26584v1)

**作者**：Jochen Laubrock  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-11-19

### 📄 论文摘要

Does post-training change what a language model represents, or how this representation is read out into an answer? We compared linear probes with the models' own answers, analyzed with signal detection theory, in six open-weight base models and their post-trained versions. For judgments of whether German texts were written by a human or an AI, probes and word n-gram classifiers separated the classes well, but the answers did not and often ordered the texts inversely. Post-training lowered the sensitivity of the answers on average ($Δd' = -0.34$ across model families; -0.29 across three prompts). It also changed the use of a stated base rate: Base models shifted their log-odds by less than the stated change in prior odds, most post-trained models by more. In two models with stage-wise checkpoints, the change occurred during supervised fine-tuning, model stitching implicated the early layers, and from mid-depth on internal states at positions after the text, not those of the text, transferred the change between checkpoints. Our corpora cannot be shared, so we add a case reproducible from public data, the truth of negated statements. Here, post-training acted in the opposite direction: Probes decoded truth at or near ceiling in every model, the answers of several base models did not use it, and post-training repaired them; by mid-depth the repair resided at the positions after the statement; below it, the representation of the statement contributed, strongly in one of four models. In a training study, adding 2,000 correctly labeled authorship judgments of news texts to otherwise identical fine-tuning data improved the answers on our newspaper and textbook corpora and inverted them on the chats, where they followed a news-trained probe of the base model. Post-training thus changed how a judgment is read out of what a model represents, and a small training signal can set its direction.

### 🤖 AI 总结

**一句话总结**：Does post-training change what a language model represents, or how this representation is read out into an answer? We compared linear probes with the models' own answers, analyzed with signal detectio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Represented, but, misread, Post-training, changes, how, language, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26584v1) | [下载PDF](https://arxiv.org/pdf/2611.26584v1.pdf)

---

## [7. AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher](https://arxiv.org/abs/2611.26510v1)

**作者**：Guoxin Chen, Shuang Sun, Fanzhe Meng 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-11-19

### 📄 论文摘要

Task success alone does not specify which behaviors post-training should reinforce. Even successful teacher trajectories can contain unsupported assumptions, unproductive repetition, or superficial verification. We propose Skill-FT (Skill-Guided Fine-Tuning), which uses natural-language skills to suppress undesirable habits and elicit underrepresented effective behaviors during teacher rollouts, then fine-tunes a target model on the resulting trajectories. We introduce AutoMaster, an autonomous post-training system in which an LLM agent develops these interventions through trajectory analysis, skill design, data selection, and feedback from rollouts and target-model evaluation. Across Terminal, Search, and software engineering tasks with 4B and 9B target models, AutoMaster improves mean performance over Vanilla SFT on successful unguided teacher trajectories by 1.42-8.99 percentage points, with the teacher, task pool, training set size, and SFT recipe held fixed. Together with the ablations and trajectory analyses, these results suggest that behavioral shaping can make a fixed model a more effective teacher. We further find that retaining skill instructions during SFT yields higher mean performance than removing them across all six settings, despite their absence at evaluation and identical supervised outputs. These findings suggest that preserving skill context as part of a training demonstration can support better behavioral internalization.

### 🤖 AI 总结

**一句话总结**：Task success alone does not specify which behaviors post-training should reinforce. Even successful teacher trajectories can contain unsupported assumptions, unproductive repetition, or superficial ve...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AutoMaster, Autonomous, Post-Training, Making, Same, Model, Better, Teacher

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26510v1) | [下载PDF](https://arxiv.org/pdf/2611.26510v1.pdf)

---

## [8. Multimodal Error Detection in Chest X-ray Reports: A Large Language Model Reading Image Evidence](https://arxiv.org/abs/2611.26492v1)

**作者**：Yanda Cheng, Bo Wen, Yuhao Lu  
**分类**：cs.CL  
**发布时间**：2026-11-19

### 📄 论文摘要

Rad-Linter checks chest X-ray reports against image-derived evidence to flag potential errors for review. A pretrained image classifier supplies scores for nine pathologies, and a 1.5B-parameter language model, fine-tuned with LoRA on 1,816 examples, checks their consistency with the report. We compare it with a keyword-and-negation rule baseline given the same reports and scores. Evaluation uses controlled report-score pairings from OpenI, with consistency labels derived from automatic report labels and score thresholds. Each counterfactual quad crosses two real reports with two real score vectors from other patients, creating two consistent and two inconsistent pairs. Every report and score vector occurs in both conditions, so either input alone permits only 50% accuracy. On 131 quads, Rad-Linter achieves 98.5% pair accuracy versus 80.5% for the rule baseline, and classifies all four pairs correctly in 94.4% of quads versus 56.5%. The checkers perform similarly on omission items, including unmentioned and negated findings; larger differences occur on the remaining item types, which require interpreting how findings are described. The same language model without fine-tuning remains near 50% accuracy. On a second set of 181 quads that also includes reports on which the automatic labelers disagree, pair accuracy is 93.4% versus 75.3%. These controlled results show that, given the same image-derived scores, a trained language model detects report-score inconsistencies more accurately than the tested rule baseline, with the advantage concentrated in interpreting how findings are worded.

### 🤖 AI 总结

**一句话总结**：Rad-Linter checks chest X-ray reports against image-derived evidence to flag potential errors for review. A pretrained image classifier supplies scores for nine pathologies, and a 1.5B-parameter langu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multimodal, Error, Detection, Chest, X-ray, Reports, Large, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26492v1) | [下载PDF](https://arxiv.org/pdf/2611.26492v1.pdf)

---

## cs.CV

## [9. Posterior Matching Distillation](https://arxiv.org/abs/2611.26629v1)

**作者**：Hidir Yesiltepe, Julius Berner, Arash Vahdat 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-19

### 📄 论文摘要

Diffusion distillation accelerates image and video generation by compressing a pretrained teacher's iterative sampling process into a few network evaluations. Distribution-based methods achieve this by matching the student's output distribution to the teacher's. This matching is often driven by reverse-KL objectives, whose mode-seeking bias favors dominant teacher modes at the expense of diversity across samples. We introduce Posterior Matching Distillation (PMD), a new member of the distribution-based distillation family that combines mode-covering posterior sampling with any-step generation. At zero population loss, PMD recovers the teacher's full posterior of clean images at each trained noise level. Its stochastic student supports any-step sampling budgets within the trained timestep grid without further training. To learn these posteriors, PMD matches exponentially reweighted averages of student samples conditioned on a fixed noisy state to corresponding teacher posterior means. Under Gaussian corruption, exponentially tilted posterior mean is a single teacher evaluation at a shifted input. We prove that, matching tilted means over an open neighborhood uniquely identifies the full posterior. PMD thus supervises the entire conditional distribution through a family of mean constraints, without any auxiliary student-score network. Experiments on SDXL and FLUX.2 [klein] 4B demonstrate that PMD achieves the best FID among 4-step methods on both models, while maintaining competitive or leading performance across prompt-alignment and perceptual-quality metrics.

### 🤖 AI 总结

**一句话总结**：Diffusion distillation accelerates image and video generation by compressing a pretrained teacher's iterative sampling process into a few network evaluations. Distribution-based methods achieve this b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Posterior, Matching, Distillation, accelerates, image, video, generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26629v1) | [下载PDF](https://arxiv.org/pdf/2611.26629v1.pdf)

---

## [10. One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning](https://arxiv.org/abs/2611.26617v1)

**作者**：Yuxin Jiang, Wenqiang Sun, Jiaqi Li 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.LG, cs.RO  
**发布时间**：2026-11-19

### 📄 论文摘要

Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action learning recovers such supervision from visual transitions, yet often learns the underlying dynamics largely from scratch. We ask whether a pretrained video generator can instead provide the prior for both inverse and forward dynamics. We introduce O$^{2}$LaF, built on a simple principle: one prior, two dynamics. We initialize both models from the same pretrained video DiT and adapt them to their distinct roles: a feed-forward transition encoder with learnable action queries for inverse dynamics, and a causal, action-conditioned video generator for forward dynamics. By controlling information access and optimizing both dynamics end-to-end through a compact bottleneck, O$^{2}$LaF learns transferable actions from unlabeled videos. Across navigation and robotic manipulation, O$^{2}$LaF sets a new state of the art in few-shot action probing and enables stronger zero-shot action transfer across visual contexts and embodiments. Beyond generative video priors, we further extend our framework to predictive representation priors such as V-JEPA2, achieving competitive performance. Our findings suggest a broader paradigm for latent-action learning: repurposing pretrained video models to discover transferable actions and predict their consequences.

### 🤖 AI 总结

**一句话总结**：Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action learning recovers such supervision from visual transitions, yet often learns the underlying dynamics...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, One, Prior, Two, Dynamics, Repurposing, Video, Transformers

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26617v1) | [下载PDF](https://arxiv.org/pdf/2611.26617v1.pdf)

---

## [11. ScaleWorld: High-Resolution World Generation through Shared Prediction and Refinement](https://arxiv.org/abs/2611.26615v1)

**作者**：Yansong Qu, Wesker Zheng, Quanjian Song 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-19

### 📄 论文摘要

High-resolution generation enables video world models to render fine-grained scene structures and textures, but directly generating high-resolution video incurs substantial computational and memory costs. We present ScaleWorld, a causal video model that unifies low-resolution world prediction and high-resolution refinement within a single shared backbone. By refining its own predictions, ScaleWorld produces high-resolution world videos without requiring a separate refinement model. For each video chunk, the shared backbone first completes a low-resolution prediction and then performs one-step high-resolution refinement conditioned on that prediction. To support efficient streaming generation, we maintain separate causal states with a long low-resolution history for prediction and a short high-resolution history for refinement. To address task interference during distillation, we separate specialist optimization from capability consolidation and introduce task-asymmetric on-policy distillation (TA-OPD). This procedure transfers prediction and refinement behaviors from specialized teachers into a shared student through local velocity matching under their respective sampling and history policies. {Extensive experiments demonstrate that ScaleWorld achieves high-quality world generation with improved computational and memory efficiency.

### 🤖 AI 总结

**一句话总结**：High-resolution generation enables video world models to render fine-grained scene structures and textures, but directly generating high-resolution video incurs substantial computational and memory co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ScaleWorld, High-Resolution, World, Generation, through, Shared, Prediction, Refinement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26615v1) | [下载PDF](https://arxiv.org/pdf/2611.26615v1.pdf)

---

## [12. Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://arxiv.org/abs/2611.26603v1)

**作者**：Peiyun Hu, Marko Mihajlovic, Lyndon Duong 等 8 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-19

### 📄 论文摘要

We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. By analyzing prior methods for monocular depth estimation, we find that they commonly trade off temporal consistency and boundary sharpness: multi-frame methods favor consistency, single-frame methods favor sharpness. To overcome this trade-off, we train a single, scalable network that processes both images and video and predicts depth maps at native resolution. Depth Pro 2 produces depth maps that are metrically accurate, sharp, and temporally consistent all at once, outperforming prior work in all of these dimensions. We release a family of models that define a new Pareto frontier in terms of metric accuracy, sharpness, temporal consistency, and runtime. We release code and weights at https://apple-aiml-research.github.io/ml-depth-pro-2/

### 🤖 AI 总结

**一句话总结**：We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. By analyzing prior methods for monocular depth estimation, we find that they commonly trad...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Depth, Pro, Sharp, Temporally, Consistent, Metric, Monocular

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26603v1) | [下载PDF](https://arxiv.org/pdf/2611.26603v1.pdf)

---

## [13. Coda-DaVinci: Reimagining Video Generation with Code2Video](https://arxiv.org/abs/2611.26595v1)

**作者**：Yiyan Ji, Qixun Wang, Yang Shi 等 23 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-19

### 📄 论文摘要

Code2Video uses agent-authored 3D proxies to guide video generation, enabling explicit control over structure and dynamics. However, how to construct proxies and prompts for optimal downstream quality remains underexplored, as do the capabilities and limitations of this paradigm. Through controlled experiments and blinded human evaluation, we study proxy granularity, physics simulation, and prompting. The results reveal task-dependent trade-offs: coarse proxies favor natural motion, while medium-grained proxies favor consistency. Physics simulation and proxy-aligned prompting further improve average quality. Guided by these findings, we introduce Coda-DaVinci, a task-adaptive agentic framework for Code2Video generation that selects between proxy-guided and direct generation, adapts modeling granularity to each entity, and coordinates simulation with proxy-grounded prompting. Its multi-agent harness preserves scene assets and guides repairs through visual inspection and independent review. Experiments demonstrate leading instruction following on VTR and scene consistency on R2M, improved physical plausibility over direct generation, and higher visual realism than the compared Code2Video baselines. Long-video evaluations further show gains in event structure and consistency across successive interactions, while revealing limitations in transition stability and adherence to scene settings.

### 🤖 AI 总结

**一句话总结**：Code2Video uses agent-authored 3D proxies to guide video generation, enabling explicit control over structure and dynamics. However, how to construct proxies and prompts for optimal downstream quality...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Coda-DaVinci, Reimagining, Video, Generation, Code2Video, uses, agent-authored

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26595v1) | [下载PDF](https://arxiv.org/pdf/2611.26595v1.pdf)

---

## [14. Multi-institutional grading of Barrett's esophagus dysplasia without stain normalization using a pathology foundation model and multiple instance learning](https://arxiv.org/abs/2611.26562v1)

**作者**：Amirali Khosravi, Jaidip M. Jagtap, D. Chamil Codipilly 等 14 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-19

### 📄 论文摘要

Barrett's esophagus dysplasia grading suffers substantial inter-observer variability, particularly for low-grade dysplasia, complicating clinical decision-making. We conducted a retrospective multi-institutional diagnostic accuracy study of a foundation model-based deep learning system for dysplasia grading, using 969 H\&E-stained whole slide images from four institutions. Patch-level classifiers trained on expert annotations identified diagnostically relevant regions, followed by attribute-aware multiple instance learning for slide-level classification as non-dysplastic Barrett's esophagus (NDBE), low-grade dysplasia, or high-grade dysplasia. On a held-out test set (n = 130), macro-averaged AUC was 0.96 (95\% CI 0.93--0.98). For binary dysplasia detection, sensitivity was 98\% (80/82) and specificity 81\% (39/48), with a negative likelihood ratio of 0.030 and quadratic-weighted \kap{} of 0.83 against expert consensus. No high-grade dysplasia case was misclassified as NDBE. Performance was consistent across institutions without stain normalization, indicating that stain-robust foundation-model representations may remove the site-specific preprocessing that has constrained prior systems to institution-specific deployment.

### 🤖 AI 总结

**一句话总结**：Barrett's esophagus dysplasia grading suffers substantial inter-observer variability, particularly for low-grade dysplasia, complicating clinical decision-making. We conducted a retrospective multi-in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Multi-institutional, grading, Barrett's, esophagus, dysplasia, without, stain

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26562v1) | [下载PDF](https://arxiv.org/pdf/2611.26562v1.pdf)

---

## [15. AURA: AUdio-dRiven streaming Avatar](https://arxiv.org/abs/2611.26540v1)

**作者**：Nathaniel Cohen, Nicolas Dufour, Amélie Royer 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-19

### 📄 论文摘要

Current audio-driven video diffusion models can synthesize realistic talking-head videos but generally require dozens of diffusion denoising steps over multi-second video chunks, making them unsuitable for streaming applications such as voice assistants and virtual avatars, where low-latency and online causal generation are required properties. AURA generates video chunk by chunk with a rolling KV cache, requiring only the audio of the current chunk to start generating, rather than a multi-second audio look-ahead like bidirectional models. It comes in two sizes: AURA 1.3B streams 576p video in real time on a single GPU (20.7 fps for a 16 Hz playback rate), making it suited to interactive avatar applications, and AURA 5B streams 720p video at 9.7 fps. Our two-stage distillation pipeline first aligns the causal student with the teacher, by training it to match the teacher's trajectories with fewer diffusion steps and a chunk-wise sliding window causal attention mask, then applies Distribution Matching Distillation (DMD) with backward simulation to close the remaining quality gap. On standard talking-head benchmarks, AURA 1.3B runs 23x faster than its own bidirectional teacher and reaches a quality comparable to TalkVerse at a lower resolution, and AURA 5B matches its TalkVerse teacher at 720p while running 17x faster. To support reproducibility and further research on streaming avatar generation, we release the weights of both models along with a dataset of 30K synthetic videos and their precomputed teacher trajectories.

### 🤖 AI 总结

**一句话总结**：Current audio-driven video diffusion models can synthesize realistic talking-head videos but generally require dozens of diffusion denoising steps over multi-second video chunks, making them unsuitabl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, AURA, AUdio-dRiven, streaming, Avatar, Current, video, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26540v1) | [下载PDF](https://arxiv.org/pdf/2611.26540v1.pdf)

---

## [16. Deterministic Temporal Embedding for Calcium Imaging Trace Extraction](https://arxiv.org/abs/2611.26522v1)

**作者**：Qi Gao, Julius Beichert, Miriam Ratliff 等 4 位作者  
**分类**：cs.CV, cs.LG, eess.IV  
**发布时间**：2026-11-19

### 📄 论文摘要

Reliable extraction of calcium-dependent fluorescence traces in calcium imaging sequences requires identifying pixels whose fluorescence intensity reflects the same underlying cellular activity. We present a deterministic temporal embedding framework that maps pixel-wise fluorescence traces to a low-dimensional representation in which temporally coherent sources form spatially coherent regions. Starting from a fuzzy-neighborhood graph and spectral initialization, we optimize a class-balanced cross-entropy objective using exact sparse attraction and a deterministic particle-mesh decomposition of the dense repulsive interaction with sparse edge compensation, avoiding stochastic negative sampling. The resulting latent representation is spatially decoded into reliable source supports for trace extraction without imposing an explicit cellular shape prior. Experiments on synthetic and in vivo two-photon calcium imaging data demonstrate robust recovery of irregular and spatially touching sources together with efficient deterministic embedding optimization.

### 🤖 AI 总结

**一句话总结**：Reliable extraction of calcium-dependent fluorescence traces in calcium imaging sequences requires identifying pixels whose fluorescence intensity reflects the same underlying cellular activity. We pr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Deterministic, Temporal, Embedding, Calcium, Imaging, Trace, Extraction, Reliable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26522v1) | [下载PDF](https://arxiv.org/pdf/2611.26522v1.pdf)

---

## [17. Plan4D: Generative Plannable 4D Worlds](https://arxiv.org/abs/2611.26516v1)

**作者**：Hangwei Zhang, Rujing Dang, Ruimin Lin 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-19

### 📄 论文摘要

Most world models for future prediction prioritize aestetic quality of generated videos, but offer only weak physical grounding and limited geometric consistency over time, due to the lack of explicit 4D modeling. In this paper, we introduce plan4d, a possible next milestone towards building a generative plannable 4D world model that predicts future RGB videos together with dense 4D geometry, including depth, cameras, point clouds, and scene flow from an observed scene context and text-specified actions. Since training data with paired actions and dense 4D annotations is inherently scarce, plan4d leverages the complementary priors of foundational video generators and 3D reconstructors. Specifically, we propose a model-stitching architecture that couples Depth Anything 3 with LongCat-Video and augments it with an auxiliary DPT head for scene-flow prediction. The resulting model allows us to plan and generate complex, long-horizon, and fine-grained actions in a dynamic 3D scenes, while substantially improving both visual fidelity and geometric accuracy of the generated future videos. Extensive experiments on both synthetic and real-world datasets demonstrate that plan4d achieves state-of-the-art performance in generative 4D modeling of environmental reactions. Project Page: https://fogradio.github.io/plan4d-project

### 🤖 AI 总结

**一句话总结**：Most world models for future prediction prioritize aestetic quality of generated videos, but offer only weak physical grounding and limited geometric consistency over time, due to the lack of explicit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, Plan4D, Generative, Plannable, Worlds, Most, world, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26516v1) | [下载PDF](https://arxiv.org/pdf/2611.26516v1.pdf)

---

## [18. Direct3D-V3: Latent-Free Diffusion Transformers in the Native Voxel Domain](https://arxiv.org/abs/2611.26511v1)

**作者**：Shuang Wu, Jiachen Qian, Youtian Lin 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-19

### 📄 论文摘要

Native 3D generation has largely been built around latent diffusion, with recent advances concentrating on stronger variational autoencoders (VAE) and increasingly elaborate latent representations, from vecset and triplanes to structured sparse voxels. Despite their architectural differences, these methods all share the same premise: geometry is first compressed into a latent space and only then modeled by the generator. We take a different route and propose Direct3D-V3, a latent-free diffusion transformer (DiT) framework that discards the VAE altogether and operates in the native voxel domain, directly modeling raw SDF voxel grids during both training and sampling. To make this direct voxel formulation geometrically reliable, we introduce an implicit manifold regularization over neighboring voxels to suppress non-watertight surfaces, and convert predicted SDF grids into meshes via Marching Cubes so that rendered normal losses can supervise the model directly from its predicted SDF. To improve alignment between the conditioning image and generated geometry, Direct3D-V3 also predicts the camera parameters of the conditioning image as an auxiliary task, encouraging the DiT to learn the mapping from image observations to 3D shape. This latent-free design removes the reconstruction bottleneck, brings training under an objective in the native voxel domain, and yields meshes with substantially richer local detail. The predicted camera and native SDF voxel output further make Direct3D-V3 extensible to generative reconstruction, where diffusion is interleaved with normal-guided refinement to improve alignment with the observed view while the generative prior completes unseen regions. Project page: https://dreamtechai.github.io/Direct3D-V3.

### 🤖 AI 总结

**一句话总结**：Native 3D generation has largely been built around latent diffusion, with recent advances concentrating on stronger variational autoencoders (VAE) and increasingly elaborate latent representations, fr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, 3D, Direct3D-V3, Latent-Free, Transformers, Native, Voxel, Domain

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26511v1) | [下载PDF](https://arxiv.org/pdf/2611.26511v1.pdf)

---

## [19. SHUSH: Emission-Aware Reward Design for Proactive Video Assistants](https://arxiv.org/abs/2611.26478v1)

**作者**：Shawn Liang, Soamar Homsi, Gourav Datta  
**分类**：cs.CV  
**发布时间**：2026-11-19

### 📄 论文摘要

Proactive video assistants must decide not only what to say, but also when to speak. Existing reinforcement-learning objectives can reward timely, correct responses without accounting for response volume, thereby encouraging unnecessary or repeated emissions. We identify this failure mode in MMDuet2, whose proactive area-under-the-curve (PAUC) reward promotes timely responses but does not price the number of emissions. We show analytically that this makes additional responses weakly penalized or effectively free, systematically encouraging over-emission. We then propose an emission-aware F1 reward for interval-valued annotations, using exclusive span--emission matching to price false emissions and missed spans. Under MMDuet2's training recipe, our policy on the visual subset of OmniPro replies 2.5x less often than MMDuet2 while raising timing F1 from 0.259 to 0.396 and content-aware F1 from 0.103 to 0.154; a more conservative variant cuts replies by 82.5% and raises precision from 0.161 to 0.418. On ProactiveVideoQA, the same reward adds replies where the baseline is nearly silent, and PAUC ranks a heavily over-emitting policy second despite near-last F1, because it is insensitive to response count. Our results indicate that proactive assistants should be trained and evaluated with objectives that price emissions.

### 🤖 AI 总结

**一句话总结**：Proactive video assistants must decide not only what to say, but also when to speak. Existing reinforcement-learning objectives can reward timely, correct responses without accounting for response vol...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SHUSH, Emission-Aware, Reward, Design, Proactive, Video, Assistants, must

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26478v1) | [下载PDF](https://arxiv.org/pdf/2611.26478v1.pdf)

---

## [20. Fixing the Last Mile: Failure-Aware Image Restoration with Region-Specific Guidance](https://arxiv.org/abs/2611.26456v1)

**作者**：Hongyu An, Fanghua Yu, Kainan Yan 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-19

### 📄 论文摘要

Recent advances in image restoration have greatly improved global image fidelity, producing visually plausible results across most regions of an image. Nevertheless, even high-quality restorations often exhibit localized failures, including artifacts in semantically important regions such as faces and text, structural inconsistencies, and texture mismatches. Although these errors typically affect only a small portion of the image, they often dominate the overall perceptual quality of the result. In this work, we propose Failure-Aware Image Restoration (FAIR) to address the "last-mile" problem in image restoration. Rather than applying one uniform generative prior over the whole image, we condition a single-pass restoration model on both where local failures are likely to occur and what corrective guidance each region requires. This region-bound conditioning enables fine-grained and controllable restoration that improves semantic accuracy and stylistic consistency in critical regions while maintaining faithful, high-quality restoration elsewhere. Our method complements existing restoration pipelines by shifting the emphasis from global fidelity to local perceptual acceptability. Extensive experiments show that the proposed approach resolves common failure cases and improves perceptual quality, bridging the gap between technical accuracy and practical usability.

### 🤖 AI 总结

**一句话总结**：Recent advances in image restoration have greatly improved global image fidelity, producing visually plausible results across most regions of an image. Nevertheless, even high-quality restorations oft...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Fixing, Last, Mile, Failure-Aware, Image, Restoration, Region-Specific, Guidance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26456v1) | [下载PDF](https://arxiv.org/pdf/2611.26456v1.pdf)

---

## [21. Asuka-FM: A System-Architectural Co-Design Framework for Efficient Text-to-Image Pretraining on Consumer Hardware](https://arxiv.org/abs/2611.26437v1)

**作者**：Víctor Rodrigo González, Pablo M. Olmos, Ignacio Peis 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-19

### 📄 论文摘要

Frontier text-to-image (T2I) foundation models predominantly rely on multi-billion parameter Diffusion Transformers (DiTs) pretrained across massive compute clusters, creating an accessibility barrier for academic laboratories. When training DiTs from scratch on single consumer GPUs (e.g., an NVIDIA RTX 4090 with 24\,GB VRAM), practitioners encounter three primary bottlenecks: quadratic attention sequence costs, Just-In-Time (JIT) compilation graph breaks induced by variable aspect-ratio bucketing, and an autoencoder throughput wall where frozen Variational Autoencoder (VAE) operations dominate step latency. In this work, we introduce \textbf{Asuka-FM}, an end-to-end system and architectural framework demonstrating that competitive dual-stream DiTs ($\sim$206M parameters) can be pretrained from scratch on a single consumer GPU in $\sim$160 GPU hours for under \$55. Asuka-FM integrates four core designs: (i) an AdaLN-free dual-stream DiT backbone reducing parameter count; (ii) structured sequence sparsification via Sparse-Dense Residual Fusion (SPRINT) to cut attention FLOPs by over 50\%; (iii) continuous aspect-normalized Rotary Position Embeddings (RoPE) coupled with shifted square crop training, guaranteeing static tensor shapes while unlocking zero-shot virtual camera control; and (iv) a pixel adaptation phase utilizing a lightweight (10M parameter) Patch Detailer Head operating under velocity regression ($v$-prediction). Evaluated on open-domain benchmarks without benchmark-specific fine-tuning, Asuka-FM achieves GenEval 0.588 / DPG 78.96 scores at 256px and GenEval 0.609 / DPG 78.51 scores at 512px, setting a new Pareto-optimal efficiency standard for democratic foundation modeling.

### 🤖 AI 总结

**一句话总结**：Frontier text-to-image (T2I) foundation models predominantly rely on multi-billion parameter Diffusion Transformers (DiTs) pretrained across massive compute clusters, creating an accessibility barrier...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Asuka-FM, System-Architectural, Co-Design, Framework, Efficient, Text-to-Image, Pretraining, Consumer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26437v1) | [下载PDF](https://arxiv.org/pdf/2611.26437v1.pdf)

---

## [22. HumanCOIN: A 12,500-Hour Dataset for Human Intent in Egocentric Manipulation](https://arxiv.org/abs/2611.26434v1)

**作者**：Shihan Wu, You Liu, Chunyu He 等 51 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-11-19

### 📄 论文摘要

First-person manipulation datasets treat the observation-action pair as the atomic unit and compress the generation and execution of an action into a policy network's weights, rendering the intent state behind the action unobservable. Human motor control research shows that intent mediates between observation and action and leaves observable traces along the intent pathway from decision to effect: gaze reaches the target before the hand, muscle load builds before contact, and cortical activity precedes the motor command. To record this pathway at scale, we present HumanCOIN, a first-person manipulation dataset built around human intent: 12,500 hours across 38 scene classes with three tiers of proxies. At the output end, the L1 attention tier (10,000 h) infers gaze from headband camera video, exposing the operator's next object of attention and reach before the hand moves. Midway, the L2 exertion tier (2,000 h) records surface EMG from armbands, making load expectations readable before execution is complete. At the origin, the L3 cognition tier (500 h) records scalp EEG, giving early readouts of task decisions and monitoring. Each tier inherits all proxies from the tiers below. The dataset further provides multi-view RGB images, depth maps and point clouds, 6-DoF head and wrist pose, and step-level action and object annotations. The controlled L3 setting additionally measures gaze, hand pose and finger kinematics directly. Clock and calibration data are released with the dataset so that any read rate can be re-aligned. The three tiers cover three stations, from visual orienting to cortical preparation, making the process behind visual-action pairs available for modeling at dataset scale. Project page: https://flagopen.github.io/HumanCOIN.

### 🤖 AI 总结

**一句话总结**：First-person manipulation datasets treat the observation-action pair as the atomic unit and compress the generation and execution of an action into a policy network's weights, rendering the intent sta...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HumanCOIN, 500-Hour, Dataset, Human, Intent, Egocentric, Manipulation, First-person

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26434v1) | [下载PDF](https://arxiv.org/pdf/2611.26434v1.pdf)

---

## [23. AdaPixFlow: Learning Continuous-Time 3D Dynamics Across Scenes from Sparse Multi-view Observations](https://arxiv.org/abs/2611.26433v1)

**作者**：Hrishikesh Viswanath, Aniket Bera  
**分类**：cs.CV  
**发布时间**：2026-11-19

### 📄 论文摘要

Understanding how objects move in dynamic scenes requires recovering their 3D motion from visual observations and predicting their positions at unobserved times. Existing methods either optimize scene-specific velocity fields or impose predefined physical and kinematic assumptions. We instead study learning a continuous-time dynamics operator across scenes, mapping multi-view visual observations to 3D object kinematics. We introduce Adaptive Pixel Flows (\ours{}), which learns this operator from multi-view RGB-D observations without per-scene optimization or predefined motion models. The method fuses observations from all cameras into a shared voxel grid in world coordinates, from which the network predicts a continuous-time velocity field. Because the operator is trained across scenes, it learns motion priors that carry over to unseen scenes. The field can then be integrated from observed states to predict object positions between observations and beyond the observed sequence. On held-out PhysInOne scenes, \ours{} improves F1 over the strongest competing method by 2.5\% for in-between prediction and 15\% for future prediction. Compared with per-scene velocity-field methods, the improvements are 30\% and 85\%, respectively. Applied zero-shot to Spring-Gaus, it improves future-prediction F1 by 12\%.

### 🤖 AI 总结

**一句话总结**：Understanding how objects move in dynamic scenes requires recovering their 3D motion from visual observations and predicting their positions at unobserved times. Existing methods either optimize scene...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, AdaPixFlow, Learning, Continuous-Time, Dynamics, Across, Scenes, Sparse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26433v1) | [下载PDF](https://arxiv.org/pdf/2611.26433v1.pdf)

---

## cs.LG

## [24. Active Feature Acquisition by Distilling an Oracle Teacher](https://arxiv.org/abs/2611.26598v1)

**作者**：Yang Meng, Zixin Ding, Robert L. Grossman 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-19

### 📄 论文摘要

Acquiring every feature of an instance is often costly: a measurement can carry a monetary price, a time delay, or a privacy cost. Active Feature Acquisition (AFA) addresses this by learning a policy that decides, per instance, which features to acquire under a budget. Existing AFA methods train this policy by optimizing a self-constructed utility target rather than distilling an explicit teacher. We construct this teacher explicitly. At training time the label and the unobserved feature values are available, and together they determine the teacher in closed form: an oracle that ranks every candidate by its effect on the downstream predictor's error. OracleImitator distills this ranking into a deployable policy by soft-target imitation. Across multimodal medical diagnosis and the AFABench benchmark, OracleImitator matches or outperforms existing AFA methods across the budget range, recovering 90% of the attainable accuracy gain at under a quarter of the acquisition cost. Because the teacher is an explicit algorithmic object rather than an implicit optimization target, we can also measure directly how much of its ranking is recoverable by a policy restricted to what is visible at deployment.

### 🤖 AI 总结

**一句话总结**：Acquiring every feature of an instance is often costly: a measurement can carry a monetary price, a time delay, or a privacy cost. Active Feature Acquisition (AFA) addresses this by learning a policy ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Active, Feature, Acquisition, Distilling, Oracle, Teacher, Acquiring

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26598v1) | [下载PDF](https://arxiv.org/pdf/2611.26598v1.pdf)

---

## [25. The Window Lever: Longer Observation Windows Outweigh the Observed Effects of Data, Capacity, and Architecture in Customer Behavior Forecasting](https://arxiv.org/abs/2611.26521v1)

**作者**：Tara Sowrirajan, Yanqiao Wang  
**分类**：cs.LG, cs.IR  
**发布时间**：2026-11-19

### 📄 论文摘要

In our experiments on long-horizon customer-behavior forecasting, a longer observation window outweighed the observed effects of more data, more capacity and newer architectures. The window is the weeks of history a model sees before the week it forecasts from. Going from an 8- to a 16-week window adds a raw +0.070 to 0.107 log-space $R^2$ in every family at 1M. Matched test cohorts, which score the same customer-weeks at every window, show this raw comparison understates the gain in every family they cover. The direction holds on five public datasets, four spanning over a year (ridge and our transformer on all five). On our internal data, longer windows admit up to 10% more and colder training customers, which matching does not fix. Our design does not separate window length from calendar coverage, because every test anchor (the week a forecast is made from) falls in one eight-week band. On training-period anchors, the weekly ridge probe's gain persists outside the holiday season, keeping about 72% of it. We therefore report a robust positive association with longer windows and do not identify the magnitude of a calendar-independent history effect. Of four internally registered predictions, the only fully blind one failed. An activity-mixture model predicted +0.014 from 24 to 32 weeks; the weekly-aggregate probe returned -0.0004. For the sequence families, the other three levers are about an order of magnitude smaller, bounded and unresolved. Their observed effects are at most 0.006 between the nominal 1M and 10M tiers and 0.0052 among five sequence families at 16 weeks with clocks as built, both single-seed on the full test split, and 0.006 for capacity on three-seed means. These are observed intervals, not equivalence bounds. Our claim is the order-of-magnitude contrast between the window and those bounds. A team building on this class of data should start by lengthening the window.

### 🤖 AI 总结

**一句话总结**：In our experiments on long-horizon customer-behavior forecasting, a longer observation window outweighed the observed effects of more data, more capacity and newer architectures. The window is the wee...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Window, Lever, Longer, Observation, Windows, Outweigh, Observed, Effects

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26521v1) | [下载PDF](https://arxiv.org/pdf/2611.26521v1.pdf)

---

## [26. Hybrid Retrieval for Government Scheme Search in English and Marathi](https://arxiv.org/abs/2611.26514v1)

**作者**：Aishwarya Gunjal, Kanchan Khemnar, Pawan Poojary 等 6 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-11-19

### 📄 论文摘要

Retrieving government schemes requires matching citizens' information needs to formal administrative descriptions, often across languages and terminology. We present a bilingual search system for Maharashtra government schemes and public services that combines BM25 retrieval with sentence-embedding similarity through equal-weight score fusion. The system indexes aligned English-Marathi scheme descriptions and supports multilingual, Marathi-focused, and translation-mediated semantic configurations. Evaluation on manually curated bilingual queries compares BM25, dense retrieval, and hybrid retrieval using IndicSBERT and MahaSBERT. BM25 provides a strong baseline with a mean reciprocal rank (MRR) of 0.864. Hybrid retrieval increases MRR to 0.872 with IndicSBERT and 0.879 with MahaSBERT, whereas the corresponding dense-only systems achieve 0.663 and 0.655. MahaSBERT-based fusion also increases precision from 0.781 to 0.808 while matching BM25 recall at 0.946. These results support the complementary use of lexical and semantic signals in this collection, while showing that improvements over a strong lexical baseline are modest and metric-dependent. The study provides an application-focused analysis of hybrid retrieval for bilingual public-service information access.

### 🤖 AI 总结

**一句话总结**：Retrieving government schemes requires matching citizens' information needs to formal administrative descriptions, often across languages and terminology. We present a bilingual search system for Maha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hybrid, Retrieval, Government, Scheme, Search, English, Marathi, Retrieving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26514v1) | [下载PDF](https://arxiv.org/pdf/2611.26514v1.pdf)

---

## [27. Grid Cells as Spectral Successor Features: A Reusable Basis for Continual Reinforcement Learning](https://arxiv.org/abs/2611.26504v1)

**作者**：Élodie Côté-Gauthier, Doina Precup, Isabeau Prémont-Schwarz  
**分类**：cs.LG  
**发布时间**：2026-11-19

### 📄 论文摘要

Continual reinforcement learning requires agents to adapt when the task changes while reusing what they know about the environment. Successor features separate dynamics from task-specific reward, but their effectiveness depends on the choice of base features. Taking the identification of entorhinal grid cells with eigenvectors of the successor representation as a design principle, we build this basis from eigenvectors of the transition matrix of a fixed reference policy. With such a basis, the successor features at a state-action pair are a linear combination of the base features at that same pair, which is not true in general, and the coefficients are known in closed form: each successor feature is its base feature multiplied by $θ_i = 1/(1-γλ_i)$, where $λ_i$ is its eigenvalue. The long-term return is thus predicted from the same features as the immediate reward, no successor-feature network or replay buffer is needed, and adapting to a new task reduces to a linear regression on the reward. The agent acts greedily on the action values of the reference policy, which is one step of policy improvement over it and suffices to reach a single goal. In a two-goal gridworld, with the uniform random walk as reference policy, whose eigenvectors are the low-frequency Laplacian eigenvectors, agents built this way maintain near-maximal return across every change of goal, whereas SimpleSF and DQN lose most of their return at each change.

### 🤖 AI 总结

**一句话总结**：Continual reinforcement learning requires agents to adapt when the task changes while reusing what they know about the environment. Successor features separate dynamics from task-specific reward, but ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Grid, Cells, Spectral, Successor, Features, Reusable, Basis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26504v1) | [下载PDF](https://arxiv.org/pdf/2611.26504v1.pdf)

---

## [28. A new algorithmic approach for finding flat minima: critically damped Polyak stepsizes](https://arxiv.org/abs/2611.26475v1)

**作者**：Francesco Caporali, Jason M. Altschuler, Boris Hanin  
**分类**：cs.LG, cs.AI, math.OC  
**发布时间**：2026-11-19

### 📄 论文摘要

We present a new adaptive stepsize rule that biases gradient descent toward flatter minima in both theory and practice, and establish the first uniform-in-time guarantees for both sharpness and loss reduction for a broad class of locally quadratic objectives. Our critically damped Polyak (CDP) stepsizes multiply the classical Polyak rule by $4$ and a mild damping factor. The factor $4$ is critical in that it produces equioscillations around the manifold of minimizers $\mathcal{M}$ to leading order. Damping provably drives convergence to $\mathcal{M}$. CDP thus operates at the edge of stability by adapting its stepsizes to local curvature. Once the loss is small, its projected iterates follow gradient descent on $\log{λ_1(\nabla^2 \mathcal{L})}$ along $\mathcal{M}$ to leading order, paralleling the flatness bias of normalized gradient descent (Arora et al., 2022). Unlike normalized gradient descent, CDP step lengths shrink with the distance to $\mathcal{M}$, enabling convergence to an interpolating solution that locally minimizes sharpness at finite learning rate. We establish our theory for a broad class of non-negative losses with locally quadratic Morse-Bott structure near $\mathcal{M}$, capturing regular interpolation regimes in smooth overparameterized neural networks. Empirically, CDP stepsizes produce a flattening effect similar to that of Sharpness-Aware Minimization (SAM, Foret et al., 2021), reducing sharpness even in settings beyond our theory, including nonlinear teacher-student networks and fine-tuning of pre-trained LLMs.

### 🤖 AI 总结

**一句话总结**：We present a new adaptive stepsize rule that biases gradient descent toward flatter minima in both theory and practice, and establish the first uniform-in-time guarantees for both sharpness and loss r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：new, algorithmic, approach, finding, flat, minima, critically, damped

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26475v1) | [下载PDF](https://arxiv.org/pdf/2611.26475v1.pdf)

---

## [29. Neural Conditional Gaussian Model: Efficient Data Assimilation with Sequential Uncertainty Quantification for Nonlinear Dynamics](https://arxiv.org/abs/2611.26463v1)

**作者**：Chuanqi Chen, Nan Chen  
**分类**：cs.LG, math.DS  
**发布时间**：2026-11-19

### 📄 论文摘要

Data assimilation (DA) in partially observed nonlinear systems requires repeated estimation of both hidden states and their uncertainty. Conventional nonlinear filtering can be computationally expensive and often relies on an explicit dynamical model. In this paper, we develop the Neural Conditional Gaussian Model (Neural CGM), a data-driven dynamical model that maps unobserved physical states into a learned latent space, where the dynamics of the latent states follow a conditional Gaussian structure. This structure allows closed-form DA updates in the latent space, while nonlinear encoder-decoder mappings retain the flexibility needed to represent complex dynamics in physical space. A key feature of Neural CGM is its treatment of uncertainty in DA. The latent posterior mean and covariance are mapped to the physical variables through a Gaussian decoder that combines local moment propagation with learned nonlinear corrections. The resulting physical-space posterior statistics depend on the sequentially updated latent distribution rather than on a separate post-processing estimate. The same statistics enter a Gaussian negative log-likelihood during training, so both the posterior mean and uncertainty affect the learned model. Because Neural CGM learns the dynamical model itself, it can also be used for state forecasting and simulation without explicit knowledge of the governing equations. Numerical experiments on benchmark nonlinear dynamical systems show accurate state estimation and forecasting while substantially reducing online assimilation cost relative to conventional nonlinear DA methods. Neural CGM is therefore suited to repeated state estimation, uncertainty quantification, and prediction from partial observations.

### 🤖 AI 总结

**一句话总结**：Data assimilation (DA) in partially observed nonlinear systems requires repeated estimation of both hidden states and their uncertainty. Conventional nonlinear filtering can be computationally expensi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Neural, Conditional, Gaussian, Model, Efficient, Data, Assimilation, Sequential

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26463v1) | [下载PDF](https://arxiv.org/pdf/2611.26463v1.pdf)

---

## [30. Learning to Defer under Expert Drift](https://arxiv.org/abs/2611.26440v1)

**作者**：Ziyao Mou, Andrea Wynn, Eric Nalisnick  
**分类**：cs.LG  
**发布时间**：2026-11-19

### 📄 论文摘要

The learning to defer (L2D) framework enables safety in machine learning and AI systems by allocating difficult or critical decisions to a human expert. However, most prior work on L2D assumes fixed expert reliability, overlooking temporal fluctuations in human performance due to factors such as fatigue and cognitive biases. Humans commonly exhibit such substantial, systematic performance shifts across a wide range of domains, from high-stakes settings such as radiology, aviation, and judicial decision-making, to everyday tasks such as crowdsourced image annotation. We propose Expert-Drift-Adapted Learning-to-Defer (EDA-L2D), a novel expert-aware L2D framework that explicitly models these temporal shifts by conditioning the deferral head on recent histories of expert outcomes via a sequence model. This history-aware approach enables adaptive deferral policies that anticipate reliability fluctuations and better allocate decisions between human and machine over time. We provide comprehensive experiments across three diverse tasks -- image classification, medical diagnosis, and hate speech detection -- including generalization analyses under realistic deferral conditions and irregular shifts in expert reliability. Our results show that EDA-L2D adapts more effectively than prior L2D methods to diverse temporal patterns of expert reliability, resulting in improved system performance and more effective deferral decisions. Code is available at https://github.com/ZiyaoMou/L2D-Expert-Drift.

### 🤖 AI 总结

**一句话总结**：The learning to defer (L2D) framework enables safety in machine learning and AI systems by allocating difficult or critical decisions to a human expert. However, most prior work on L2D assumes fixed e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：L2D, Learning, Defer, under, Expert, Drift, framework, enables

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.26440v1) | [下载PDF](https://arxiv.org/pdf/2611.26440v1.pdf)

---

