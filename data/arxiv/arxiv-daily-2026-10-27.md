# arXiv AI 论文日报 | 2026-10-27

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.AI](#csAI) (5 篇)
- [cs.LG](#csLG) (13 篇)
- [cs.CV](#csCV) (7 篇)
- [cs.CL](#csCL) (5 篇)

---

## cs.AI

## [1. Center-of-Mass Interpretation of Evolution Strategies](https://arxiv.org/abs/2610.35865v1)

**作者**：Akshat Gupta  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-10-26

### 📄 论文摘要

Evolution strategies (ES) update a model by sampling a population of perturbed copies, scoring each one, and moving in the reward-weighted direction of the perturbations. This update is usually presented as an estimate of a smoothed gradient. We present a geometrical interpretation of this update instead. Treat each perturbed model as a particle and its reward as the particle's mass. Before scoring, every particle has the same mass and the population balances at its centroid. Once rewards are assigned, it balances at its reward-weighted center of mass instead. We show that the mean-subtracted ES update is exactly this displacement, scaled by a scalar factor that depends on the mean reward, for any finite population. The physical reading needs nonnegative rewards, which can always be arranged by adding a constant to every reward without changing the update. In the limit of a large population or under antithetic sampling, the centroid sits on the model itself, so ES has an even simpler geometric interpretation: from its current location, the model moves towards the reward-weighted center of mass of its own population. The same picture explains what subtracting the mean reward does: it changes the point from which the displacement is measured, from the model to the sampled centroid. Our contribution is an intuitive, geometric way to visualize an ES update, exact for any finite population.

### 🤖 AI 总结

**一句话总结**：Evolution strategies (ES) update a model by sampling a population of perturbed copies, scoring each one, and moving in the reward-weighted direction of the perturbations. This update is usually presen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, ES, Center-of-Mass, Interpretation, Evolution, Strategies, update, model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35865v1) | [下载PDF](https://arxiv.org/pdf/2610.35865v1.pdf)

---

## [2. Patient-specific rubric-based evaluation of large language models across longitudinal cancer care](https://arxiv.org/abs/2610.35847v1)

**作者**：Wei-Wei Zhang, Pengkai Wang, Yan Li 等 16 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-26

### 📄 论文摘要

Large language models (LLMs) show promise in specialty medicine, yet existing evaluations largely focus on isolated clinical encounters rather than tracking how clinical responsibilities evolve across a longitudinal care pathway. Here we introduce NPC-RubricBench, a phase-aware benchmark for evaluating multistage clinical reasoning across the cancer care continuum, using nasopharyngeal carcinoma as a defined disease context. Curated from longitudinal records of 405 patients across two cancer centers, the benchmark comprises 941 patient-phase units across six sequential care phases and 17,688 patient-specific atomic criteria spanning five evaluation dimensions, with each assessment strictly restricted to decision-time clinical evidence. Evaluating 30 general-purpose and medical LLMs revealed that strong diagnostic performance does not carry over to downstream care. We evaluated 30 general-purpose and medical LLMs, showing that high diagnostic performance did not translate into improved downstream care. Instead, the dominant failure modes reversed across phases. Explicit decision errors dominated anatomical staging at 48.2%, whereas decision omissions dominated initial work-up and post-treatment follow-up at 33.4% and 30.4%, respectively. In the evaluated model set, medically adapted models showed higher omission rates than general-purpose models. Moreover, varying query granularity exposes a critical specification trade-off: broad open-ended requests degrade Decision Quality across all 30 models, while more detailed, checklist-like prompts raise Decision Quality but reduce Evidence Faithfulness and Safety Adherence. Furthermore, NPC-RubricBench demonstrates that static diagnostic benchmarks are insufficient to ensure consistent clinical reliability over time, highlighting the importance of phase-adaptive safeguards in multistage medical AI.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) show promise in specialty medicine, yet existing evaluations largely focus on isolated clinical encounters rather than tracking how clinical responsibilities evolve across...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Patient-specific, rubric-based, evaluation, large, language, models, across

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35847v1) | [下载PDF](https://arxiv.org/pdf/2610.35847v1.pdf)

---

## [3. Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents](https://arxiv.org/abs/2610.35767v1)

**作者**：Tingzhu Bi, Xun Zhang, Jinglin Li 等 5 位作者  
**分类**：cs.AI, cs.DC, cs.SE  
**发布时间**：2026-10-26

### 📄 论文摘要

Root cause analysis (RCA) of microservice failures has attracted many LLM agents whose investigation is hand-crafted, through standard operating procedures, fixed stages and role agents. Each is evaluated on its own data against few baselines, so it is unknown whether this design beats letting a capable model investigate on its own. We compare three simple harnesses that prescribe none of the model's calls (one call over an evidence package, a SQL agent and the Codex coding agent) with five published LLM RCA agents and with statistical and causal methods on RCAtlas, 90 validated cases from eight public datasets, across six models and three reasoning efforts. The simple harnesses are the most accurate (PR@1 65-77% on three mid-tier models), ahead of the published agents (16-53%) and the non-LLM methods (6-39%), on every model on which both families were run. The published agents fix from a tenth to all of their model calls in the program, and a case study shows how these prescriptions skip the decisive evidence. A stronger model mainly improves reliability, a multi-turn harness mainly improves aptitude, and more reasoning effort changes accuracy by a few points at most while multiplying the time by up to seven. Among runs more accurate than the best non-LLM method, every Pareto-optimal run in cost or time uses a simple harness.

### 🤖 AI 总结

**一句话总结**：Root cause analysis (RCA) of microservice failures has attracted many LLM agents whose investigation is hand-crafted, through standard operating procedures, fixed stages and role agents. Each is evalu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Free, Look, Reason, Simple, Harnesses, Outdiagnose, Hand-Crafted

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35767v1) | [下载PDF](https://arxiv.org/pdf/2610.35767v1.pdf)

---

## [4. CLOSURE: Cross-Channel Closure for Multivariate Time Series Anomaly Detection](https://arxiv.org/abs/2610.35753v1)

**作者**：Fan Xu, Hao Wu, Zhi Song 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-26

### 📄 论文摘要

Multivariate time series produced by industrial installations and server clusters are under continuous monitoring, and anomaly detection is the first line of defense before a local fault escalates into a system-wide failure. In the absence of labels, the dominant paradigm trains a reconstruction model on normal data and scores the residual to reach a verdict. Recent work has steadily enriched the expressiveness of the recovery map through Transformers, diffusion models, and cross-scale associations. A residual, however, only certifies that an observation can be recovered; it does not certify that the variables still explain one another as they do under normal operation. A coordinated yet unfamiliar operating transition inflates the residual without breaking any relationship, whereas a sensor drifting away from its peers may leave the residual silent. Methods that fold inter-variable dependencies into the reconstruction objective inherit this ambiguity, because their relational evidence is ultimately supervised by the same recovery loss. We therefore propose CLOSURE, which evaluates recoverability and cross-channel consistency as two normal-data prediction tasks learned in separation. The recoverability task is solved by a diffusion reconstructor conditioned on a discrete memory of normal temporal bases. The consistency task is solved by a relation-closure operator that predicts every channel exclusively from the others, where the target's own trajectory is withheld and sparse signed gates decide which peers are actually used. The two scores are reconciled only through calibration on normal data. Extensive experiments show that CLOSURE consistently outperforms recent reconstruction-, frequency-, and topology-based detectors on public benchmark streams, confirming the value of examining consistency alongside recoverability.

### 🤖 AI 总结

**一句话总结**：Multivariate time series produced by industrial installations and server clusters are under continuous monitoring, and anomaly detection is the first line of defense before a local fault escalates int...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CLOSURE, Cross-Channel, Multivariate, Time, Series, Anomaly, Detection, produced

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35753v1) | [下载PDF](https://arxiv.org/pdf/2610.35753v1.pdf)

---

## [5. Explainable Multimodal AI Approach to Reduce Unnecessary Breast Biopsies](https://arxiv.org/abs/2610.35704v1)

**作者**：Sadam Hussain, Mansoor Ali, Daly Betzabeth Avendaño-Avalos 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-26

### 📄 论文摘要

Recently, there has been rise in multimodal vision-language models for computer-aided diagnosis (CAD), yet their application in breast diagnosis, particularly for predicting biopsy outcomes remains limited. This study presents a multimodal vision-language approach, incorporating Grad-CAM as an Explainable AI (XAI) technique, to predict benign tumors in patients recommended for biopsy, especially those classified as BI-RADS 4 and 5. A novel multimodal framework was devel- oped using Vision Transformer (ViT) for imaging feature extraction and DeBERTa-V3-Large for textual embeddings. The model was trained and evaluated on a comprehensive in-house dataset comprising 1,632 patients, each with four mammography views and a corresponding radiology report. The features of both modalities were extracted independently and fused by late fusion before classification. Grad-CAM was used to generate visual explanations highlighting key regions influencing model predictions. The proposed model demonstrated high sensitivity 90%, 95%, 99%, and 100% with corresponding specificities of 40%, 36%, 18%, and 11%, respectively. The best AUC achieved was 0.72 by multimodal approach on the test set, outperforming the image only (0.66) and text-only (0.68) baselines. The proposed multimodal architecture, enhanced with Grad-CAM, demonstrates a strong potential to identify benign tumors among high-risk patients, offering interpretable insights and thereby helping reduce unnecessary biopsies, patient anxiety, and healthcare costs.

### 🤖 AI 总结

**一句话总结**：Recently, there has been rise in multimodal vision-language models for computer-aided diagnosis (CAD), yet their application in breast diagnosis, particularly for predicting biopsy outcomes remains li...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Explainable, Multimodal, Approach, Reduce, Unnecessary, Breast, Biopsies, Recently

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35704v1) | [下载PDF](https://arxiv.org/pdf/2610.35704v1.pdf)

---

## cs.CL

## [6. Preserve to Expand: Source-Aware Adaptation and Model Merging for Multilingual LLM-Based ASR](https://arxiv.org/abs/2610.35846v1)

**作者**：Yuchen Zhang, Haralambos Mouratidis, Ravi Shekhar  
**分类**：cs.CL  
**发布时间**：2026-10-26

### 📄 论文摘要

Expanding multilingual ASR systems to new languages is challenging when adaptation must preserve previously supported languages without replaying source-language training data. We study this problem in connector-based Speech LLMs, where a trainable connector maps speech representations into a frozen large language model. We evaluate target-update construction and merging strategies for adapting the connector while preserving source-language performance. In single-target expansion, target-only fine-tuning and standard TIES merging learn new languages but cause severe source-language forgetting, while SSU-Wanda+TIES gives the best source-preserving trade-off. In multi-target expansion, update merging provides stable source retention, whereas recursive expansion can improve target adaptation under favorable orders but is highly order-sensitive. These results show that multilingual ASR expansion requires balancing target acquisition, source retention, and interactions among target-language updates.

### 🤖 AI 总结

**一句话总结**：Expanding multilingual ASR systems to new languages is challenging when adaptation must preserve previously supported languages without replaying source-language training data. We study this problem i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Preserve, Expand, Source-Aware, Adaptation, Model, Merging, Multilingual, LLM-Based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35846v1) | [下载PDF](https://arxiv.org/pdf/2610.35846v1.pdf)

---

## [7. Understanding Jev-Style System One Models: Does Structure Reduce Selection Bias?](https://arxiv.org/abs/2610.35826v1)

**作者**：Mingyang Song, Mao Zheng, Zhiyuan Ma 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-26

### 📄 论文摘要

Selection bias in large language models (LLMs) can persist despite instructions to ignore presentation order or prompts that elicit reasoning. Recent efforts to reproduce Jev-style System One behavior have produced a growing family of models that predict probabilities directly over supplied candidates. Yet systematic comparisons of selection bias across Jev versions, Jev reproductions, and generative LLMs remain limited in multi-option tasks. This leaves a central question: does Jev-style decision structure reduce selection bias? We address this question with a simple test that shuffles options while keeping question and candidate content fixed. Across two Jev versions, twelve Jev reproductions, and six generative LLMs, we trace individual answers through eight presentations and compare them with fixed-order repetition. On our primary collection of 1,700 questions from two benchmarks, Jev's accuracy varies by less than two percentage points, yet its cumulative failure set expands by 27--29\% relative to the original order, with first failures continuing into the final presentation. This loss of initial successes is substantially larger than under fixed-order repetition, even for highly repeatable Jev reproductions. Nor does Jev show a general advantage over the LLM baselines in preserving correct choices. Aggregation offers limited protection: voting yields modest gains for Jev, while even unanimous answers are frequently wrong. These results expose a gap between repeatable decisions and decisions that remain correct across equivalent presentations, showing why stable accuracy alone cannot establish resistance to selection bias.

### 🤖 AI 总结

**一句话总结**：Selection bias in large language models (LLMs) can persist despite instructions to ignore presentation order or prompts that elicit reasoning. Recent efforts to reproduce Jev-style System One behavior...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Understanding, Jev-Style, System, One, Models, Does, Structure, Reduce

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35826v1) | [下载PDF](https://arxiv.org/pdf/2610.35826v1.pdf)

---

## [8. Quantifying Claim Smoothing by LLM Research Agents](https://arxiv.org/abs/2610.35793v1)

**作者**：Tiasa Singha Roy, Manya Wadhwa, Greg Durrett  
**分类**：cs.CL  
**发布时间**：2026-10-26

### 📄 论文摘要

Deep research, or any use of large language models (LLMs) to read a large document collection and produce insights, requires synthesizing information from different sources. In this work, we find that LLMs produce long-form research reports that read as confident syntheses but which fail to accurately reflect the underlying documents. We call this failure smoothing. In collapsing diverse and potentially conflicting sources into a single narrative, the model discards the evidential "jaggedness" of its corpus and asserts conclusions more decisive than the citations can support. We introduce a claim level scoring pipeline, SmoothScore, to quantify this effect. Our pipeline extracts key conclusive claims from model generated reports, then finds evidence relevant to each claim and clusters that evidence along high level aspects. Finally, each claim is scored with respect to the evidence to quantify the degree of smoothing done by the agent. Across 7 systems and 4 datasets, we find that agents consistently produce stronger claims than warranted.

### 🤖 AI 总结

**一句话总结**：Deep research, or any use of large language models (LLMs) to read a large document collection and produce insights, requires synthesizing information from different sources. In this work, we find that...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, or, Quantifying, Claim, Smoothing, Research, Deep

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35793v1) | [下载PDF](https://arxiv.org/pdf/2610.35793v1.pdf)

---

## [9. SEMA-Auto: Sighted and Efficient Multi-Turn Attack with Autonomy](https://arxiv.org/abs/2610.35743v1)

**作者**：Mingqian Feng, Xiaodong Liu, Weiwei Yang 等 10 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-26

### 📄 论文摘要

Existing jailbreak attackers fall into two classes: static planners fix their single- or multi-turn adversarial plans in advance, remaining simple but losing sight of the victim's replies, wasting turns and limiting transferability; interactive generators read each victim reply to generate the next-turn attack but require in-loop evaluators for success signals or hints, incurring substantial costs and inflated performance. Bridging this gap, we propose SEMA-Auto, a sighted and efficient multi-turn attacker with autonomy, interacting with the victim model and terminating the session by itself upon success. To stabilize its behaviors and boost its capabilities, SEMA-Auto is trained in two stages. Synthetic bootstrap tuning installs the notion of attack targets and conforming decisions by fine-tuning the base model with bootstrapped trajectories. Decision-supervised reinforcement learning then optimizes two objectives jointly yet separately, reinforcing the attack with higher jailbreak reward while supervising the decision at each turn against an absolute target. Our method achieves state-of-the-art (SOTA) attack success rates (ASR) across multiple datasets, victims, and judges, outperforming all static and interactive baselines, within almost the fewest turns, demonstrating both effectiveness and efficiency. For example, SEMA-Auto performs a $76.0\%$ ASR@1 within an average of $3.0$ turns against DeepSeek-V4-Flash on AdvBench, while the best static baseline is $54.8\%$ with fixed $7$ turns and the best interactive baseline is $43.8\%$ in $3.7$ turns. Against safety-hardened frontier models, GPT-oss-120B, GPT-5.4, Claude-Haiku-4.5, and GPT-6-Astra, our counter-trained attacker achieves an average $59.6\%$ ASR@1 on HarmBench, $13.8\%$ over prior SOTA. Our code is available at: https://github.com/microsoft/SEMA

### 🤖 AI 总结

**一句话总结**：Existing jailbreak attackers fall into two classes: static planners fix their single- or multi-turn adversarial plans in advance, remaining simple but losing sight of the victim's replies, wasting tur...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SEMA-Auto, Sighted, Efficient, Multi-Turn, Attack, Autonomy, Existing, jailbreak

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35743v1) | [下载PDF](https://arxiv.org/pdf/2610.35743v1.pdf)

---

## [10. From Self-Confidence to Statistical Accuracy: Scaling Human-in-the-Loop Evaluation with Direct and LLM-Assisted Auditing](https://arxiv.org/abs/2610.35698v1)

**作者**：Harine Choi, Chenchen Kuai, Zihao Li 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-26

### 📄 论文摘要

For large language models (LLMs) and multimodal large language models (MLLMs), model-reported self-confidence is often miscalibrated, yet it may still be useful for efficient evaluation. At the same time, LLM-as-a-judge offers a scalable alternative to direct human auditing, but its practical benefit depends on calibration quality and inference cost.   This paper develops a unified statistical framework for both evaluation routes under alternative sampling strategies. For direct auditing, confidence-stratified sampling is used to recover population accuracy from partially verified outputs without requiring calibrated confidence. Finite-sample uncertainty is characterized, and the analysis shows how highly uneven confidence strata affect audit efficiency and label allocation. For judge-assisted evaluation, the judge is modeled through sensitivity and false-positive rate, yielding an error-corrected estimator with calibration uncertainty. The two routes are then compared through human-label and total-cost efficiency boundaries.   Experiments on MMLU-Pro and MMMU-Pro show that miscalibrated self-confidence can still support statistically valid stratified auditing. Under highly imbalanced confidence distributions, proportional allocation substantially reduces estimation error relative to equal-per-stratum allocation. For judge-assisted evaluation, only a small subset of target--verifier pairs satisfies the idealized human-label efficiency condition, and automated inference costs can further limit potential savings. These findings clarify the statistical and economic conditions under which confidence-guided auditing and automated verification are useful.

### 🤖 AI 总结

**一句话总结**：For large language models (LLMs) and multimodal large language models (MLLMs), model-reported self-confidence is often miscalibrated, yet it may still be useful for efficient evaluation. At the same t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Self-Confidence, Statistical, Accuracy, Scaling, Human-in-the-Loop, Evaluation, Direct, LLM-Assisted

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35698v1) | [下载PDF](https://arxiv.org/pdf/2610.35698v1.pdf)

---

## cs.CV

## [11. Do vision models know that three is three?](https://arxiv.org/abs/2610.35857v1)

**作者**：Ankit Sonthalia, Arnas Uselis, Seong Joon Oh  
**分类**：cs.CV  
**发布时间**：2026-10-26

### 📄 论文摘要

Do vision models encode the transition $2{\to}3$ the same way whether it appears in handwritten digits or in hand gestures, and do they "understand" that clean${\to}$dirty is the same transformation regardless of whether it is applied to a kitchen or a carpet? The linear representation hypothesis (LRH) answers this for language models: concept changes correspond to directions in (language) embedding space. In vision, the same concept can manifest in visually unrelated "regimes" that rarely co-occur: images of digits and hands do not share much in common in pixel space. To understand whether vision models still encode the underlying abstract concepts, we study 46 vision encoders across architectures, training objectives, and scales, on 10 concept families including numerosity, age, object identity, and MIT-States attributes. Within each regime, we find statistically significant concept directions near-universally across our tested models. However, two distinct regimes do not always share the same concept direction. Several models learn multiple linear structures for the same concept transition, split across regimes. We call this phenomenon "fragmented linearity": strong local linearity coexisting with near-absent global linearity. Fragmentation is, however, not fixed: models with stronger local linearity progressively escape it (local-global linearity correlated with $τ\in [0.38, 0.89]$ across all concepts), and where global linearity does emerge, concept directions can transfer as linear probes across regimes.

### 🤖 AI 总结

**一句话总结**：Do vision models encode the transition $2{\to}3$ the same way whether it appears in handwritten digits or in hand gestures, and do they "understand" that clean${\to}$dirty is the same transformation r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, vision, models, know, three, three?, encode, transition

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35857v1) | [下载PDF](https://arxiv.org/pdf/2610.35857v1.pdf)

---

## [12. FL4N: Feed-forward Latent Model for 4D Novel View Synthesis](https://arxiv.org/abs/2610.35854v1)

**作者**：Eunbeen Hong, Hyeonseo Yu, Honggyu An 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-26

### 📄 论文摘要

4D novel view synthesis (NVS) aims to render dynamic scenes across viewpoints and timestamps, which requires jointly inferring 3D structure and temporal dynamics. Existing monocular feed-forward methods often rely on explicit 4D Gaussian representations, which are prone to temporal inconsistency and severe rendering artifacts. We present FL4N, the first feed-forward latent 4D NVS model. Instead of relying on explicit 4D primitives, FL4N encodes a 4D scene prior into a unified latent representation across space and time. Our core insight is that learning temporal dynamics as residuals on top of a pretrained static latent prior enables effective 4D modeling with limited dynamic training data. To this end, we introduce a lightweight dynamic encoder that leverages static scene features to disentangle object motion from camera-induced parallax. Trained solely with an image synthesis objective, FL4N achieves state-of-the-art 4D NVS quality while rendering in real time. Its learned latent representation generalizes to real-world videos and disentangles viewpoint from time.

### 🤖 AI 总结

**一句话总结**：4D novel view synthesis (NVS) aims to render dynamic scenes across viewpoints and timestamps, which requires jointly inferring 3D structure and temporal dynamics. Existing monocular feed-forward metho...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, FL4N, Feed-forward, Latent, Model, Novel, View, Synthesis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35854v1) | [下载PDF](https://arxiv.org/pdf/2610.35854v1.pdf)

---

## [13. Seeing Through Distractions: Context-Stable Attribution via the Least Core](https://arxiv.org/abs/2610.35827v1)

**作者**：Sai Ganesh Nagarajan, Toshinori Yamauchi, Hiroshi Kera  
**分类**：cs.CV, cs.GT  
**发布时间**：2026-10-26

### 📄 论文摘要

Shapley-value-based explanations are widely used for feature attribution in machine learning. However, in computer vision, a feature may reduce the target-class score when added to the complete genuine image, even when the predicted label remains unchanged. We formalize such features as contextual distractors and investigate their attributions under semivalues and the least core. Under a weak average marginal monotonicity assumption, we derive quantitative semivalue--least-core gap bounds and sufficient conditions based on the probability of sampling smaller contexts. We further show that shifting semivalue weights toward larger contexts decreases the signed gap. Finally, controlled image-classification experiments and evaluations on Salient ImageNet provide strong empirical support for our theoretical findings.

### 🤖 AI 总结

**一句话总结**：Shapley-value-based explanations are widely used for feature attribution in machine learning. However, in computer vision, a feature may reduce the target-class score when added to the complete genuin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Seeing, Through, Distractions, Context-Stable, Attribution, via, Least, Core

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35827v1) | [下载PDF](https://arxiv.org/pdf/2610.35827v1.pdf)

---

## [14. Back to Basics: A Skill-Centric Approach to Generalist Web Agents](https://arxiv.org/abs/2610.35823v1)

**作者**：Minh Pham-Dinh, Md Farhan Ishmam, Hernan Yupanqui 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-26

### 📄 论文摘要

Browser agents do not just need more practice. They need to practice the right things. We introduce MiniWeb, a realistic miniature of the web comprising 65 interconnected websites across 15 domains, where agents navigate, search, and transact as people do. Its 369 human-annotated tasks cover everyday workflows and label 37 reusable interaction primitives grouped into 7 skill families, allowing us to diagnose which skills fail rather than only whether a task succeeds. Benchmarking ten open-weight agents, we find that drag & gesture is consistently the weakest family, with no agent solving more than 24% of its instances. To address this gap, we introduce MiniWebGen, a framework that autonomously generates verified, skill-centric training data from MiniWeb. Fine-tuning Qwen3.5-4B on just 3.1K verified trajectories improves single-primitive success by 24.9pp across 13 unseen websites, with gains across every skill family. However, these trajectories teach short-horizon interactions, which do not directly translate to full-task success. We build on this result with MiniWebAgent, which pairs the trained executor with a planner that decomposes full tasks into the skill-level steps it learned to perform. This approach improves task success by 19.4pp points on unseen MiniWeb sites and transfers to external benchmarks, with gains of 9.3pp on WebArena-Lite, 16.1pp on Online-Mind2Web, and 20.0pp on WebVoyager, without training on their trajectories. We provide a simple recipe for compact browser agents: practice reusable skills directly, then compose them to solve unfamiliar tasks.

### 🤖 AI 总结

**一句话总结**：Browser agents do not just need more practice. They need to practice the right things. We introduce MiniWeb, a realistic miniature of the web comprising 65 interconnected websites across 15 domains, w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Back, Basics, Skill-Centric, Approach, Generalist, Web, Browser

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35823v1) | [下载PDF](https://arxiv.org/pdf/2610.35823v1.pdf)

---

## [15. Does VGGT Know What It Does Not Know?](https://arxiv.org/abs/2610.35806v1)

**作者**：Adityan Thirumani Srinivasan, David Nordström  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-10-26

### 📄 论文摘要

Feed-forward 3D reconstruction models such as VGGT regress cameras and geometry in a single forward pass, but they report no uncertainty for the camera poses they predict: an incorrect relative pose looks no different from a correct one. We ask whether the frozen model nonetheless knows when its pose is wrong. On HardMatch, a benchmark of 1,000 deliberately difficult image pairs on which VGGT fails on 35% of pairs, a linear probe on VGGT's frozen features predicts pose failure on held-out categories with ROC-AUC 93.5%, compared with 79.7% for VGGT's own point-map confidence and 77.7% for a classifier trained on all of VGGT's outputs. The probe catches failures VGGT is confident about, lets a downstream system abstain on the pairs it distrusts, and transfers without retraining to rotation failures on PhotoTourism and ScanNet-1500, beyond what co-visibility explains. This knowledge is absent from the per-image encoder: it is computed partway through the layers that fuse the two views, and the same holds for a second model, $π^3$. In essence, we find that VGGT knows more about its own failures than it reports.

### 🤖 AI 总结

**一句话总结**：Feed-forward 3D reconstruction models such as VGGT regress cameras and geometry in a single forward pass, but they report no uncertainty for the camera poses they predict: an incorrect relative pose l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：It, Does, VGGT, Know, What, Not, Know?, Feed-forward

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35806v1) | [下载PDF](https://arxiv.org/pdf/2610.35806v1.pdf)

---

## [16. VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion](https://arxiv.org/abs/2610.35756v1)

**作者**：Yanming Yang, Chenxi Song, Tong Zhao 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-26

### 📄 论文摘要

Recent advancements in text-guided 3D editing, particularly with 3D Gaussian Splatting (3DGS), have shown promise but still lag behind the flexibility of 2D editing tools. Existing methods face a critical trade-off between preserving multi-view consistency and allowing structural modifications. Image-based editors can also struggle to apply the intended edit to objects viewed from unusual angles. To address these limitations, we introduce VidEdit3D, a framework that reformulates 3D scene editing as a trajectory-based video editing task. By drawing a parallel between camera movement in static 3D scenes and temporal dynamics in video, we leverage the robust spatiotemporal priors of pre-trained Video Diffusion Models (VDMs) to encourage semantic and structural coherence across views. Specifically, we propose Trajectory-Guided Rendering (TGR) to select informative keyframes and construct smooth video clips aligned with VDM input requirements. To propagate edits from an anchor view to these clips, we develop Flow-Aligned Video Editing (FAVE), a training-free framework incorporating an Editing Consistency Guidance (ECG) mechanism. ECG contrasts source and edited image conditions at a shared latent state, using scheduled source-image amplification to strengthen adherence to the edited reference while maintaining original scene context. Finally, we introduce Region-Selective 3DGS Refinement (RS-GS) to strictly confine geometric and appearance updates to target primitives, reducing background attribute leakage. Experiments demonstrate stronger instruction alignment and better multi-view consistency than the baselines.

### 🤖 AI 总结

**一句话总结**：Recent advancements in text-guided 3D editing, particularly with 3D Gaussian Splatting (3DGS), have shown promise but still lag behind the flexibility of 2D editing tools. Existing methods face a crit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Diffusion, VidEdit3D, Flexible, Gaussian, Editing, Video, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35756v1) | [下载PDF](https://arxiv.org/pdf/2610.35756v1.pdf)

---

## [17. MatAnyone-E: Sparse Memory Propagation for Efficient High-Resolution Video Matting](https://arxiv.org/abs/2610.35724v1)

**作者**：Shuyun Wang, Shangchen Zhou, Peiqing Yang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-26

### 📄 论文摘要

High-resolution video matting requires preserving fine details, such as hair strands and soft transparency, while maintaining consistency across frames. Memory-based methods achieve strong matting quality by matching current-frame features with information stored from earlier frames, but this process becomes increasingly costly as resolution grows. We present MatAnyone-E, an efficient extension of MatAnyone 2 that focuses computation where it is most needed. Our approach first performs low-resolution propagation to identify uncertain regions that require closer inspection and the memory candidates most relevant to them. It then performs high-resolution matching only for these regions using the selected memory, while reusing low-resolution matching results elsewhere. This strategy reduces both the number of locations requiring detailed matching and the amount of memory searched, while preserving the information needed to produce a complete matte. We further reduce the cost of generating high-resolution mattes with a lightweight decoder designed around measured runtime bottlenecks and trained to reproduce the original decoder's representations. Experiments show that MatAnyone-E maintains matting quality comparable to MatAnyone 2 while achieving an estimated 7.4x inference speedup and reducing peak GPU memory usage to 7.6% of the usage of MatAnyone 2 at 4K. With compilation-enabled inference on a single NVIDIA H200 GPU, it reaches 73.07 FPS at 1080p and 28.62 FPS at 4K.

### 🤖 AI 总结

**一句话总结**：High-resolution video matting requires preserving fine details, such as hair strands and soft transparency, while maintaining consistency across frames. Memory-based methods achieve strong matting qua...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MatAnyone-E, Sparse, Memory, Propagation, Efficient, High-Resolution, Video, Matting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35724v1) | [下载PDF](https://arxiv.org/pdf/2610.35724v1.pdf)

---

## cs.LG

## [18. Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling](https://arxiv.org/abs/2610.35866v1)

**作者**：Xi Chen, Chongjian Ge, Yiran Xu 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-26

### 📄 论文摘要

As autonomous research systems become more capable, benchmarks must both evaluate their performance and support meaningful research progress. We introduce Auto-Research Arena, a multi-target benchmark for evaluating autonomous research systems and discovering ideas in language modeling. Arena supports diverse research objectives within a shared experimental environment by separating admissibility from improvement: model quality and resource constraints determine whether a result qualifies, while the selected target measures progress among admissible results. We instantiate Arena in language model pretraining with nine targets spanning model, data, training, and inference efficiency, and evaluate seven research harnesses using two foundation models. Arena clearly differentiates existing harnesses across research objectives, with several sophisticated methods outperformed by our simple sequential search baseline, indicating substantial headroom in current auto-research systems. Beyond evaluation, Arena reveals a substantially broader frontier of model and system ideas aligned with active research directions. Reusing these discoveries in a new quality-driven search yields lower training loss under matched data and FLOPs and lower held-out BPB at the same model size. Together, Arena provides a common framework for benchmarking autonomous research and expanding its scope in language modeling. The code is available at https://github.com/Auto-Research-Arena/auto-research-arena

### 🤖 AI 总结

**一句话总结**：As autonomous research systems become more capable, benchmarks must both evaluate their performance and support meaningful research progress. We introduce Auto-Research Arena, a multi-target benchmark...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, Auto-Research, Arena, Benchmarking, Advancing, Language, Modeling, autonomous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35866v1) | [下载PDF](https://arxiv.org/pdf/2610.35866v1.pdf)

---

## [19. Work Agents: Systems, Capabilities, and Optimization](https://arxiv.org/abs/2610.35845v1)

**作者**：Zishan Xu, Enjun Du, Mingqi Gao 等 16 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-26

### 📄 论文摘要

As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, existing research lacks a unified perspective on how agents reliably accomplish delegated work. To address this gap, we present a work-centric, system-level perspective that views work agents as systems combining foundation models and runtime harnesses to execute tasks in stateful workspaces and deliver verifiable outcomes. We introduce two complementary dimensions, work persistence and work openness, to characterize working conditions, and classify digital work into five forms according to task scope and organization. Building on this framework, we identify five core capability families required for reliable work execution and examine approaches to model optimization, harness optimization, and their joint optimization. We further analyze existing evaluation methods and metrics from the perspective of work outcomes. Finally, we discuss future research directions, including sustained work delegation, adaptation to open environments, and the interaction between work execution and capability improvement. This paper provides a unified framework for understanding, optimizing, and evaluating work agents, supporting the development of systems capable of delivering reliable, verifiable, and practically valuable work outcomes.

### 🤖 AI 总结

**一句话总结**：As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, exist...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, As, Work, Systems, Capabilities, Optimization, foundation, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35845v1) | [下载PDF](https://arxiv.org/pdf/2610.35845v1.pdf)

---

## [20. FOCUS: Active Critic Learning for Long-Horizon Language Model Agents](https://arxiv.org/abs/2610.35801v1)

**作者**：Zhengping Jiang, William Jurayj, Liaoyaqi Wang 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-26

### 📄 论文摘要

Sparse outcome rewards make it difficult for long-horizon language-model agents to assign credit to earlier actions. Learned critics provide value estimates for intermediate states, but these estimates can be inaccurate, while estimating intermediate values with repetitive continuation samples from points within a trajectory incurs substantial costs. To mitigate these issues, we introduce FOCUS, an RL method that uses selective branching to help the critic network learn its value estimator. The rollout controller facilitates active learning for the critic by sampling continuations from states that are expected to most reduce the critic's estimation error. These refined value estimates then score the segment between consecutive states with a TD($λ$) advantage, while the sampled evidence supplies training targets for the critic. FOCUS supports long-horizon agentic reinforcement learning through a modular context-management interface that decouples context management from rollout allocation. Our experiments show that using compaction-induced segment boundaries for value estimation and credit assignment, FOCUS outperforms GRPO and VinePPO with matched per-step generation budgets on legal reasoning, deep search, and code localization benchmarks, improving held-out accuracy at Qwen3.5-9B scale by 7.2 points over the strongest baseline on BrowseComp-Plus (55.4 vs. 48.2) and by 4.1 points on DeonticBench (56.5 vs. 52.4).

### 🤖 AI 总结

**一句话总结**：Sparse outcome rewards make it difficult for long-horizon language-model agents to assign credit to earlier actions. Learned critics provide value estimates for intermediate states, but these estimate...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, FOCUS, Active, Critic, Learning, Long-Horizon, Language, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35801v1) | [下载PDF](https://arxiv.org/pdf/2610.35801v1.pdf)

---

## [21. Selective Tie Learning: Mitigating Spurious Correlations in Preference Optimization](https://arxiv.org/abs/2610.35787v1)

**作者**：Christian Moya, Purav Matlia, Elliott Thornley 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-26

### 📄 论文摘要

Preference optimization can learn spurious correlations, and augmenting the preference data with ties (equally preferred responses) can reduce spurious reliance. However, ties differ in their corrective effect, making their selection for augmentation important. For log-linear policies, we derive each tie's influence on spurious reliance and show that taking the largest predicted reductions is first-order optimal among subsets of equal size. Computing these influences requires knowledge of the spurious features and the curvature of the training objective, which is often unavailable or expensive to estimate. To this end, we explore using the magnitude of a tie's implicit reward margin and characterize the conditions under which it is a useful proxy for predicted influence. To test the theory and its qualitative transfer to neural models, we estimate influence with a counterfactual proxy for spurious reliance and use a generalized Gauss--Newton approximation to curvature for language models. Across log-linear policies, neural models, and large language models, our selection rules consistently achieve comparable reductions in spurious reliance with fewer ties than uniform selection.

### 🤖 AI 总结

**一句话总结**：Preference optimization can learn spurious correlations, and augmenting the preference data with ties (equally preferred responses) can reduce spurious reliance. However, ties differ in their correcti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Selective, Tie, Learning, Mitigating, Spurious, Correlations, Preference, Optimization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35787v1) | [下载PDF](https://arxiv.org/pdf/2610.35787v1.pdf)

---

## [22. A theory of noisy linear recurrent neural network learning dynamics](https://arxiv.org/abs/2610.35785v1)

**作者**：John J. Vastola, Kanaka Rajan  
**分类**：cs.LG, q-bio.NC  
**发布时间**：2026-10-26

### 📄 论文摘要

Biological neural networks are noisy: their dynamics involve difficult-to-predict fluctuations which are likely due not just to chaos, but also to a variety of low-level biophysical processes. Despite the omnipresence of intrinsic noise, its theoretical consequences are incompletely understood, especially in the context of learning. For example, does noise meaningfully shape representation learning, or is it better viewed as a nuisance factor whose presence or absence changes little about what solution is found and when? Here, we argue that intrinsic noise can significantly modulate representation learning in recurrent neural networks (RNNs), since it can strongly break solution-space degeneracies and in some cases control whether a non-degenerate solution exists at all. We show that this is true for an analytically tractable model of noisy RNN learning with a linear activation function and white noise inputs. We find that, in the so-called rich regime (where weights are initialized with small values), noise strongly modulates the directions in which the read-in, readout, and recurrent weights align. Moreover, we find that noise produces a kind of phase transition: for sufficiently high noise, a non-degenerate solution is not even optimal if parameter scales are limited (e.g., via regularization). These results extend recent analytic work on RNN representation learning and show that noise can act as a fundamental determinant of representations.

### 🤖 AI 总结

**一句话总结**：Biological neural networks are noisy: their dynamics involve difficult-to-predict fluctuations which are likely due not just to chaos, but also to a variety of low-level biophysical processes. Despite...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, theory, noisy, linear, recurrent, neural, network, learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35785v1) | [下载PDF](https://arxiv.org/pdf/2610.35785v1.pdf)

---

## [23. Improving Signals, Declining Encoder: A Known-Answer Test of Label-Free Monitoring in Self-Supervised Learning](https://arxiv.org/abs/2610.35766v1)

**作者**：Nilotpal Kakati  
**分类**：cs.LG, cs.CV, physics.data-an  
**发布时间**：2026-10-26

### 📄 论文摘要

Self-supervised training is monitored without labels, through the loss and statistics of the learned features. We report a case where we know the encoders lost part of what they had learned, so we can check whether these signals noticed. We trained LeJEPA encoders on synthetic images with known generating factors. In nine of ten seeds, the readability of those factors fell abruptly and stayed down, nearly always along the same direction in factor space. Meanwhile the loss kept falling, and most of the eleven label-free signals we tracked kept improving and rated the declining runs better than runs that did not decline. Standard change-point detection rarely flagged the decline near its onset, and selecting checkpoints by these signals mostly chose ones after it.

### 🤖 AI 总结

**一句话总结**：Self-supervised training is monitored without labels, through the loss and statistics of the learned features. We report a case where we know the encoders lost part of what they had learned, so we can...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Improving, Signals, Declining, Encoder, Known-Answer, Test, Label-Free

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35766v1) | [下载PDF](https://arxiv.org/pdf/2610.35766v1.pdf)

---

## [24. LUCID: Local Understanding of Covariate Importance with Conditional Density Estimation](https://arxiv.org/abs/2610.35740v1)

**作者**：Yixiao Wang, Srikar Katta, Jon Donnelly 等 5 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-10-26

### 📄 论文摘要

Computing local-level variable importance (VI) is critical for understanding machine learning models. Local permutation-based VI metrics offer a simple yet powerful approach, measuring how much a model's output changes when perturbing its inputs. However, existing perturbation strategies often ignore feature dependence or account for it only through restricted approximations. Perturbing a feature without fully respecting this dependence can generate unrealistic counterfactuals, thereby evaluating the model in regions unsupported by the observed data distribution. We address this gap by introducing a new model-agnostic local VI metric and estimator, Local Understanding of Covariate Importance with conditional Density estimation (LUCID). LUCID perturbs features of interest using plausible values drawn from the full conditional distribution given the remaining observed features. We establish theoretical connections between LUCID and existing VI measures, and provide an estimator with convergence guarantees and uncertainty quantification. Finally, we demonstrate LUCID's stable performance and practical utility across simulated and real-world examples.

### 🤖 AI 总结

**一句话总结**：Computing local-level variable importance (VI) is critical for understanding machine learning models. Local permutation-based VI metrics offer a simple yet powerful approach, measuring how much a mode...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LUCID, Local, Understanding, Covariate, Importance, Conditional, Density

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35740v1) | [下载PDF](https://arxiv.org/pdf/2610.35740v1.pdf)

---

## [25. Multi-Objective Reinforcement Learning Using Routed Ensembles and Trajectory Attribution](https://arxiv.org/abs/2610.35733v1)

**作者**：Zhenshuo Zhang, Ruoxuan Xiong, Hongyang R. Zhang  
**分类**：cs.LG, cs.AI, cs.MA, cs.RO, stat.ML  
**发布时间**：2026-10-26

### 📄 论文摘要

Multi-objective reinforcement learning is a fundamental problem for modern AI, with applications spanning post-training, reasoning models, and robotic control. A central challenge is to learn policies that balance competing objectives, such as helpfulness versus honesty in safety and alignment, or speed versus energy in robotics. The optimal policy can vary sharply with objective-weighting combinations, and the extent of this variation depends crucially on the degree of conflict among objectives, making per-preference policy learning sample-inefficient. In this paper, we introduce objective-conflict coefficients and derive near-optimal regret bounds for online settings using this measure, thereby quantifying the impact of misalignment on learning efficiency. Then, we design routed ensemble policy learning, an algorithm that maintains a small set of basis policies and dynamically routes trajectories to the policy with the highest potential reward. Finally, we consider trajectory selection as another approach to mitigate objective conflict, and design a kernel surrogate trajectory attribution algorithm that estimates how feedback signals from a set of trajectories influence policy learning on other trajectories. The kernel can capture nonlinear interactions such as synergy and antagonism between trajectories. We evaluate our approach across diverse environments and benchmarks: routed ensembles improve average performance by 4.3% over baselines for online environments from Meta-World and MO-Gymnasium, and kernel surrogate attribution improves correlation with leave-one-out analysis over existing baselines by 50%. When applied to trajectory selection, kernel-based attribution yields a 27% improvement in reward over baseline attribution methods.

### 🤖 AI 总结

**一句话总结**：Multi-objective reinforcement learning is a fundamental problem for modern AI, with applications spanning post-training, reasoning models, and robotic control. A central challenge is to learn policies...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Objective, Reinforcement, Learning, Routed, Ensembles, Trajectory, Attribution, fundamental

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35733v1) | [下载PDF](https://arxiv.org/pdf/2610.35733v1.pdf)

---

## [26. TRACE: Memory-Efficient Time Series Class-Incremental Learning via Temporal-Spectral Reconstruction](https://arxiv.org/abs/2610.35727v1)

**作者**：Junhui Mao, Junru Zhang, Liming Ye 等 10 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-26

### 📄 论文摘要

Web-connected sensing applications continuously generate multivariate time series with evolving behavioral categories, making Time Series Class-Incremental Learning (TSCIL) essential for adapting to new classes without forgetting previously acquired knowledge. However, preserving diverse and evolving class distributions under strict privacy and memory constraints remains a fundamental challenge. Existing approaches often face a trade-off between retaining sufficient historical knowledge for accurate recognition and minimizing the memory required for continual adaptation. To address these limitations, we propose TRACE, a memory-efficient, replay-free framework that preserves class-specific knowledge through generative modeling rather than sample rehearsal. TRACE employs a compact, frozen temporal-spectral representation and lightweight class-specific autoencoders to capture complex intra-class variations. By independently preserving each class model, TRACE avoids recursive generation and catastrophic forgetting, while enabling direct classification through reconstruction-based scoring without retaining historical samples or large statistical matrices. Extensive experiments across five TSCIL benchmarks demonstrate that TRACE achieves competitive classification accuracy while reducing mean retained memory by approximately 98.26% compared with TS-ACL, the strongest evaluated analytical baseline, and achieving an approximately 33.43% relative improvement in accuracy on GrabMyo.

### 🤖 AI 总结

**一句话总结**：Web-connected sensing applications continuously generate multivariate time series with evolving behavioral categories, making Time Series Class-Incremental Learning (TSCIL) essential for adapting to n...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TRACE, Memory-Efficient, Time, Series, Class-Incremental, Learning, via, Temporal-Spectral

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35727v1) | [下载PDF](https://arxiv.org/pdf/2610.35727v1.pdf)

---

## [27. Can JEV Support Clinical Trial Criteria Assessment?](https://arxiv.org/abs/2610.35721v1)

**作者**：Mengxian He, Ziyue Gao, Chun Li 等 7 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-10-26

### 📄 论文摘要

Clinical trial prescreening requires distinguishing unmet conditions from insufficient evidence in patient records. Given patient records, criterion questions, and predefined answer options, we retrospectively compared JEV, a non-generative decision model returning native option probabilities, with schema-constrained Qwen Flash across 2,048 test patient-condition pairs from TrialGPT and question-answer datasets derived from MIMIC-III and MIMIC-IV, all evaluated under strict Zero Data Retention (ZDR) policies to ensure clinical data privacy. Both models assessed conditions individually or in batches sharing the same patient context, with performance measured against reference labels. In batch mode, JEV and Qwen achieved similar macro-F1 scores on TrialGPT (0.652 vs. 0.660) and MIMIC-IV (0.807 vs. 0.814), whereas JEV substantially outperformed Qwen on MIMIC-III (0.768 vs. 0.534; $Δ$ = +0.234, 95% CI: 0.187-0.281). This advantage largely reflected higher recall for conditions labeled as having insufficient information (56.3% vs. 9.9%). Across all three datasets, JEV also had lower observed median job latency (1.18-1.40 vs. 2.80-8.90 s) and 53%-74% lower estimated cost per condition. These findings position JEV as an initial assessment component that provides criterion-level judgments and flags potential information gaps for review. JEV's observed errors in interpreting clinical evidence underscore the need to verify its outputs against patient records before they inform eligibility decisions.

### 🤖 AI 总结

**一句话总结**：Clinical trial prescreening requires distinguishing unmet conditions from insufficient evidence in patient records. Given patient records, criterion questions, and predefined answer options, we retros...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Can, JEV, Support, Clinical, Trial, Criteria, Assessment?, prescreening

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35721v1) | [下载PDF](https://arxiv.org/pdf/2610.35721v1.pdf)

---

## [28. Quantifying the failure of symmetry learning in linear diffusion models due to initialization and finite-sample effects](https://arxiv.org/abs/2610.35720v1)

**作者**：John J. Vastola, Kanaka Rajan  
**分类**：cs.LG  
**发布时间**：2026-10-26

### 📄 论文摘要

Data distributions often possess one or more symmetries: for example, all orientations of any specific dog are included in the distribution of all possible dog pictures. Despite the omnipresence of such symmetries, modern generative modeling approaches may fail to incorporate or learn them, which can lead to lower sample efficiency and poorer generalization. To what extent do diffusion models fail to learn data distribution symmetries, and what sources of symmetry breaking are most responsible? Here, we answer this question in the theoretically tractable setting of linear diffusion models. We show that of three potential sources of symmetry breaking---a non-symmetric initial weight matrix, a noisy learning target, and finite-sample noise---target noise produces the most robust symmetry breaking, since it persists even in the sample-rich regime. Using local laws from random matrix theory, we derive formulas for average symmetry error in fairly general cases involving symmetry within a subspace and show that smaller symmetries are harder to learn.

### 🤖 AI 总结

**一句话总结**：Data distributions often possess one or more symmetries: for example, all orientations of any specific dog are included in the distribution of all possible dog pictures. Despite the omnipresence of su...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Diffusion, Quantifying, failure, symmetry, learning, linear, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35720v1) | [下载PDF](https://arxiv.org/pdf/2610.35720v1.pdf)

---

## [29. Quantitative Generalization Bounds for Multi-Layer Transformers: A Few Long Strings can Beat Many Short Ones](https://arxiv.org/abs/2610.35715v1)

**作者**：Marius Henry, Michael Rizvi-Martel, Michael Hahn  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-10-26

### 📄 论文摘要

Transformer-based language models exhibit an astonishing capacity to generalize to longer and more difficult problem instances than those seen in training. However, theoretical understanding of this phenomenon still lags behind. Unlike most machine learning models, the generalisation abilities of transformers inherently require considering two axes. On one hand, one must examine in-distribution statistical generalisation, which concerns the ability of a model to broaden a function from training samples to novel samples of the same distribution. On the other hand, given the sequential nature of language data, one must also consider length generalisation, which reflects whether a model trained on inputs of a given length can extrapolate to longer ones.These two notions have mostly been studied separately, leaving open how they interact. In this work, we give a joint treatment of both axes for fixed-precision transformers. We give generalisation guarantees in terms of the parameter sizes of the involved models, as well as the quantization space and the alphabet size that supply the sequences. Finally, we illustrate how the requirements in the sample count and training length trade off. In particular, we find that increasing training length can be exponentially more efficient than increasing the sample size. Experiments support predictions of the theory.

### 🤖 AI 总结

**一句话总结**：Transformer-based language models exhibit an astonishing capacity to generalize to longer and more difficult problem instances than those seen in training. However, theoretical understanding of this p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Quantitative, Generalization, Bounds, Multi-Layer, Transformers, Few, Long, Strings

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35715v1) | [下载PDF](https://arxiv.org/pdf/2610.35715v1.pdf)

---

## [30. Detecting bus delays and service anomalies in Niterói with autoencoder latent feature representations](https://arxiv.org/abs/2610.35710v1)

**作者**：Matheus Germano, Claudio E. C. Campelo  
**分类**：cs.LG  
**发布时间**：2026-10-26

### 📄 论文摘要

Bus riders judge service by two failures: single trips that run late, and days on which the whole system misbehaves. We ask whether one unsupervised representation of raw GPS telemetry can serve both diagnoses on the NetMob 2026 Niterói bus dataset. An autoencoder compresses each trip into a 64-dimensional latent vector; the frozen encoder feeds supervised delay classifiers, and the reconstruction error serves as an anomaly score. Two findings are negative. First, the latent representation does not improve delay detection: gradient boosting on per-trip summary features reaches $0.846 \pm 0.013$ ROC-AUC against $0.838 \pm 0.016$ for the best latent setup, and the gap becomes significant once the preprocessing filters are relaxed. Second, two of the three external checks of the anomaly score were circular. Retraining without rainfall removes the rain association ($5.4\%$ against $5.0\%$ flagged, $p = 0.84$) and an apparent citywide disruption on 23 March. What survives is a day-level signal stable across three autoencoders (Spearman $ρ\geq 0.96$), driven mostly by day type, with degraded-telemetry days still separable within weekday and weekend strata. The alarm threshold limits detection more than the score does: a pooled percentile cut flags $5.7\%$ of trips on the worst degraded day, while re-scaling within each bus line flags $29.3\%$. The delay model rests almost entirely on one feature, no latent dimension is individually interpretable, and 22 chronic line-directions carry half of all delayed trips.

### 🤖 AI 总结

**一句话总结**：Bus riders judge service by two failures: single trips that run late, and days on which the whole system misbehaves. We ask whether one unsupervised representation of raw GPS telemetry can serve both ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Detecting, bus, delays, service, anomalies, Niterói, autoencoder, latent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.35710v1) | [下载PDF](https://arxiv.org/pdf/2610.35710v1.pdf)

---

