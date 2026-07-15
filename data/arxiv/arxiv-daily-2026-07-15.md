# arXiv AI 论文日报 | 2026-07-15

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (6 篇)
- [cs.CL](#csCL) (6 篇)
- [cs.CV](#csCV) (13 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. Win by Silence: Deletion Non-Monotonicity, Autonomous Exploitation, and Typed-State Gating in LLM Plan Evaluation](https://arxiv.org/abs/2607.12986v1)

**作者**：Aleh Manchuliantsau  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-07-14

### 📄 论文摘要

Plan evaluators can reward a strategic plan for becoming less explicit. This paper studies that failure in a staged expected-value scorer for LLM-generated venture routes. Proposition 1 gives the score change from deleting an interior transition while retargeting its predecessor and retaining downstream value: Delta_k = (prod_{i<k} p_i)[c_k + (1 - p_k)R_{k+1}]. On a frozen 26-route cohort, all 57 admissible deletions matched the analytic identity and threshold sign, and every route had at least one score-improving deletion. A score-seeking optimizer, allowed to restructure routes but not told the exploit mechanism, found baseline-beating uncovered structures in 21/26 routes. GATE refused score release for 26/26 silenced routes with 0/26 honest suspensions; after refusal, 47/54 next revisions repaired to a covered structure, and strict covered improvement rose from 1/26 to 13/26. An adaptive compiler-aware co-author exposed the registry-provenance boundary: obligation-channel evasions remained 6/6 across all four v1/v1.5 conditions, while delta-indexed cost floors reduced beat-honest routes from 6/6 to 3/6 and fundability-by-silence from 5/6 to 0/6 without establishing semantic completeness. If a plan scores better only because it omits necessary work, the plan did not improve; the evaluation created an omission incentive. PCSC detects and neutralizes post-hoc omission splices over model-mediated typed-state records. In the cooperative setting tested, GATE acts as a deterministic search-shaping constraint, not merely a post-hoc filter. It does not verify the semantic completeness or real-world quality of arbitrary LLM-generated strategies.

### 🤖 AI 总结

**一句话总结**：Plan evaluators can reward a strategic plan for becoming less explicit. This paper studies that failure in a staged expected-value scorer for LLM-generated venture routes. Proposition 1 gives the scor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Win, Silence, Deletion, Non-Monotonicity, Autonomous, Exploitation, Typed-State, Gating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12986v1) | [下载PDF](https://arxiv.org/pdf/2607.12986v1.pdf)

---

## [2. Resist and Update: Counterfactual Report Coordinates for Incentive-Compatible LLMs](https://arxiv.org/abs/2607.12985v1)

**作者**：Sen Yang, Yuen-Hei Yeung  
**分类**：cs.AI  
**发布时间**：2026-07-14

### 📄 论文摘要

Aligned language models routinely misreport under non-evidential incentive pressure: they agree with a confident user or overstate certainty even when their internal belief is unchanged. We cast this as a failure of internal incentive-compatibility (IC) and present a method for learning and certifying counterfactual report mediators that hold a model's reports to a causal contract: invariant to forbidden influences (pressure, prestige, restyling) and responsive to licensed ones (genuine evidence). These two demands, resist and update, pull in opposite directions. We study them on a Bayesian-witness benchmark with known posteriors, in which the same user disagreement is licensed evidence or forbidden pressure purely by stated source reliability. We (i) causally identify, by interchange interventions rather than probe accuracy, low-rank report coordinates for answer, confidence, and caveat that are near-orthogonal and independently controllable, and (ii) introduce a training-free counterfactual report-coordinate (CRC) clamp that references the model's own report under a counterfactually incentive-neutralized context. On the witness benchmark the two-pass clamp attains resist and update of 1.00 jointly (Wilson 95% CI [0.99,1.00]), a causal certificate under a constructible reference, not a deployed solution. Global decoding and steering show a single-parameter tradeoff; output-level fine-tuning matches both objectives only when both are enumerated; resist-only training loses evidence-responsiveness. The deployable single-pass compilation is lossy (0.73/0.97). The mechanism and clamp reproduce across three model families and transfer to a natural sycophancy benchmark (SycophancyEval). Our contribution is the interface and certification method: activation-level counterfactual incentive-invariance as a structural primitive for internal IC.

### 🤖 AI 总结

**一句话总结**：Aligned language models routinely misreport under non-evidential incentive pressure: they agree with a confident user or overstate certainty even when their internal belief is unchanged. We cast this ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Resist, Update, Counterfactual, Report, Coordinates, Incentive-Compatible, Aligned

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12985v1) | [下载PDF](https://arxiv.org/pdf/2607.12985v1.pdf)

---

## [3. FormalAnalyticGeo: A Neural-Symbolic Based Framework for Multimodal Analytic Geometry Problem Generation](https://arxiv.org/abs/2607.12982v1)

**作者**：Ruoran Xu, Wending Gao, Qiufeng Wang  
**分类**：cs.AI, cs.MA, cs.SC  
**发布时间**：2026-07-14

### 📄 论文摘要

Math reasoning has achieved significant progress with the rapid advancement of Multimodal Large Language Models (MLLMs), however analytic geometry remains largely underexplored, primarily due to the scarcity of annotated samples. Existing diagram generation approaches struggle with analytic geometry: template methods cannot handle constraint-driven layouts, and generative models lack the geometric precision to render annotated conic curves correctly. We present FormalAnalyticGeo, a scalable framework for fully automatic generation of multimodal analytic geometry problems. Leveraging the rigor of formal languages, we design the framework around CDL (Condition Description Language), a formal intermediate representation that bridges free-form problem text with precise diagram rendering via a Signed Distance Field (SDF) engine. The framework employs four specialized LLM components in sequence: a Generator that produces diverse analytic geometry problems, a Formalizer that converts each problem into CDL for SDF-based rendering, a Measurer that extracts ground-truth answers through vision-based measurement on the rendered diagrams, and a Quality Verifier that checks outputs at three stages. Structured feedback from the Quality Verifier drives automatic retry, forming a closed loop that eliminates any need for human annotation. Applying FormalAnalyticGeo at scale yields AnalyticGeo7K, a dataset of over 7K verified multimodal problems, each with aligned text, diagram, formal annotation, and ground truth.Experiments show that the generated problems achieve a median ground-truth relative error of 0.70\%, with 82.3\% of answers falling within 5\% of the exact symbolic solution. Our framework and dataset will be publicly released.

### 🤖 AI 总结

**一句话总结**：Math reasoning has achieved significant progress with the rapid advancement of Multimodal Large Language Models (MLLMs), however analytic geometry remains largely underexplored, primarily due to the s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FormalAnalyticGeo, Neural-Symbolic, Framework, Multimodal, Analytic, Geometry, Problem, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12982v1) | [下载PDF](https://arxiv.org/pdf/2607.12982v1.pdf)

---

## [4. Knowledge- and Gradient-Guided Reinforcement Learning for Parametrized Action Markov Decision Processes](https://arxiv.org/abs/2607.12924v1)

**作者**：Jonas Ehrhardt, René Heesch, Oliver Niggemann  
**分类**：cs.AI  
**发布时间**：2026-07-14

### 📄 论文摘要

In this paper, we study Reinforcement Learning in Parametrized Action Markov Decision Processes (PAMDP), where each decision consists of a symbolic action and numerical parameters. In such settings Reinforcement Learning algorithms typically determine parameters with one-shot estimators, which makes their training sample inefficient. Though in most PAMDP environments explicit but incomplete knowledge (e.g., rules, safety constraints, or expert heuristics) is available, it is rarely directly used to increase the sample-efficiency of training Reinforcement Learning agents. We step into this gap and propose our novel Neuro-Symbolic Knowledge- and Gradient-Guided Reinforcement Learning (KGRL) algorithm. KGRL uses domain knowledge in a Datalog knowledge base to derive the set of applicable actions and feasible parameters for a given state. This allows it to prune non-applicable actions from the decision-space and constrain the parameter spaces of the remaining actions. We then use a gradient-based parameter refinement loop to estimate the optimal parameters during training and deployment of the agent. By recording activated rules along the trajectory, KGRL additionally provides local procedural explanations on the pruning of actions and constraining of parameters. Overall, KGRL guides the agent's exploration and deployment toward feasible and constraint-aware decisions, while increasing sample efficiency during training. KGRL outperforms state-of-the-art RL baselines for PAMDPs in both, sample efficiency and episodic return.

### 🤖 AI 总结

**一句话总结**：In this paper, we study Reinforcement Learning in Parametrized Action Markov Decision Processes (PAMDP), where each decision consists of a symbolic action and numerical parameters. In such settings Re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Knowledge, Gradient-Guided, Reinforcement, Learning, Parametrized, Action, Markov, Decision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12924v1) | [下载PDF](https://arxiv.org/pdf/2607.12924v1.pdf)

---

## [5. A Multi-Agent System for Autonomous, Fine-Tuning-Free Clinical Symptom Detection: Development and Validation Study](https://arxiv.org/abs/2607.12886v1)

**作者**：Cameron Cagan, Pedram Fard, Jiazi Tian 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-14

### 📄 论文摘要

Clinical notes contain many of the signs and symptoms that bring patients to care, yet this information rarely reaches structured fields. Existing extraction approaches either rely on context-insensitive rules that generate false positives or on supervised models that require substantial fine-tuning. We present Pythia, a multi-agent system that autonomously writes and optimizes extraction prompts for clinical concepts without manual prompt engineering or fine-tuning. Running on a locally hosted open-weights model, Pythia keeps clinical notes on local infrastructure and selects prompts using development-set sensitivity and specificity. We compared Pythia with a curated lexicon across 72 signs and symptoms from 400 clinical notes representing 387 patients. Development (n=300) and validation (n=100) sets were partitioned independently for each concept. Pythia achieved mean sensitivity of 0.76 and specificity of 0.95, compared with 0.82 and 0.76 for the lexicon, and matched or exceeded the lexicon on both metrics for 20 of 62 directly comparable concepts. For 14 concepts where the lexicon labeled every note positive, Pythia recovered mean specificity of 0.97 by requiring a present-tense, patient-attributed finding rather than any textual mention of a term. Specificity transferred from development to validation with minimal degradation across prevalences, whereas sensitivity transfer weakened below 5% prevalence, reaching a mean gap of 0.25 below 2% prevalence. A BERT classifier fine-tuned per concept on the same development set achieved mean sensitivity of 0.23 and collapsed to zero sensitivity for concepts below roughly 5% prevalence. These findings suggest that autonomous, fine-tuning-free prompt optimization can produce symptom extraction prompts that generalize effectively from development to validation while remaining deployable on local infrastructure.

### 🤖 AI 总结

**一句话总结**：Clinical notes contain many of the signs and symptoms that bring patients to care, yet this information rarely reaches structured fields. Existing extraction approaches either rely on context-insensit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, System, Autonomous, Fine-Tuning-Free, Clinical, Symptom, Detection, Development

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12886v1) | [下载PDF](https://arxiv.org/pdf/2607.12886v1.pdf)

---

## cs.CL

## [6. PalmClaw: A Native On-Device Agent Framework for Mobile Phones](https://arxiv.org/abs/2607.13027v1)

**作者**：Hongru Cai, Yongqi Li, Ran Wei 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-14

### 📄 论文摘要

Large Language Model (LLM) agents have moved beyond generating responses to executing multi-step tasks by calling tools, observing the results, and iteratively deciding the next action. Most agent systems run on desktops or servers, which support tool use and task automation. Mobile devices are also important agent environments because they are widely accessible and contain users' data, sensors, and daily-use applications. Existing mobile agents mainly operate smartphones through graphical user interface (GUI) actions such as tapping, swiping, and typing, which often form long, interface-dependent sequences, cannot directly access device capabilities, and make execution boundaries difficult to define. We present \textbf{PalmClaw}, an open-source agent framework that runs natively on mobile phones and manages the sessions, memory, skills, tools, and agent loop directly on the device. PalmClaw exposes device capabilities as device tools with explicit arguments, structured results, and clearly defined execution boundaries. This design enables agents to use mobile capabilities directly while keeping each action explicit and controlled. Experiments show an 11.5\% relative improvement in task success and a 94.9\% reduction in completion time over the strongest baseline, with lower setup burden and traces illustrating how execution boundaries are applied. Code is available at https://github.com/ModalityDance/PalmClaw.

### 🤖 AI 总结

**一句话总结**：Large Language Model (LLM) agents have moved beyond generating responses to executing multi-step tasks by calling tools, observing the results, and iteratively deciding the next action. Most agent sys...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, PalmClaw, Native, On-Device, Framework, Mobile, Phones, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13027v1) | [下载PDF](https://arxiv.org/pdf/2607.13027v1.pdf)

---

## [7. The Illusion of Robustness: Aggregate Accuracy Hides Prediction Flips under Task-Irrelevant Context](https://arxiv.org/abs/2607.12963v1)

**作者**：Yanzhe Zhang, Sanmi Koyejo, Diyi Yang  
**分类**：cs.CL  
**发布时间**：2026-07-14

### 📄 论文摘要

As large language models (LLMs) grow more capable, they are increasingly deployed in context-rich settings where task inputs are often accompanied by long, partially irrelevant context. In a controlled setting, we find that state-of-the-art models often appear robust to task-irrelevant context at the aggregate level: prepending it to benchmark questions causes little change in overall accuracy. This aggregate stability, however, masks significant per-example instability. Even semantically meaningless pseudo-words, formed by randomly combining characters, can markedly shift model predictions on a small fraction of examples, degrading performance on some while improving it on others. This two-sided effect holds consistently across a wide range of models and datasets, yet the affected examples are largely model-specific. We further show that this instability is modulated by context type, context length, test-time compute, and model development stage. Together, our findings reveal context-induced tail risks concealed by aggregate accuracy, motivating per-example reliability evaluation of language models.

### 🤖 AI 总结

**一句话总结**：As large language models (LLMs) grow more capable, they are increasingly deployed in context-rich settings where task inputs are often accompanied by long, partially irrelevant context. In a controlle...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Illusion, Robustness, Aggregate, Accuracy, Hides, Prediction, Flips

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12963v1) | [下载PDF](https://arxiv.org/pdf/2607.12963v1.pdf)

---

## [8. LLM Judges Can Be Too Generous When There Is No Reference Answer](https://arxiv.org/abs/2607.12885v1)

**作者**：Chalamalasetti Kranti, Sowmya Vajjala  
**分类**：cs.CL  
**发布时间**：2026-07-14

### 📄 论文摘要

LLM judges are increasingly being used to evaluate open-ended model responses, often in no-reference settings where a ground-truth answer is unavailable. However, can they reliably assess in such evaluation setups? We explore this question in this paper through a two stage pipeline with a) calibration experiments that assess the judge model's knowledge of the task it is evaluating, and b) sensitivity experiments that assess how the judge model's performance is impacted by the presence and positioning of the reference answer in the prompt. Across experiments covering three languages, we show that the judge models we evaluated tend to over-credit incorrect answers in the absence of a reference answer, and adding reference answer information to the prompt flips the judge model's correct/incorrect decisions by as much as 85% in some experimental settings. Comparison with a subset of human annotations shows that these reference-driven changes generally align with human judgments. Our results emphasize the need for calibrating the LLM judges with a sample with reference-aware evaluation before using them in reference-free setups reliably, and our methodology provides a blueprint for researchers and practitioners in doing such calibration of LLM judges for other tasks.

### 🤖 AI 总结

**一句话总结**：LLM judges are increasingly being used to evaluate open-ended model responses, often in no-reference settings where a ground-truth answer is unavailable. However, can they reliably assess in such eval...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Be, Judges, Can, Too, Generous, When, There

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12885v1) | [下载PDF](https://arxiv.org/pdf/2607.12885v1.pdf)

---

## [9. Evaluating Large Language Models on Misconceptions in Multi-Turn Medical Conversations](https://arxiv.org/abs/2607.12884v1)

**作者**：Monica Munnangi, Saiph Savage  
**分类**：cs.CL  
**发布时间**：2026-07-14

### 📄 论文摘要

Patients seeking medical information often ask questions that embed incorrect assumptions or misconceptions. In such cases, safe medical communication requires not only answering the question, but identifying and correcting the underlying false belief. These interactions naturally unfold over multiple turns, a pattern now mirrored in interactions with LLMs. Yet current evaluation frameworks do not capture model behavior in these settings, where misconceptions can emerge, persist, or evolve over the course of a conversation. Whether LLMs can reliably correct such misconceptions over time remains largely unexamined. To study this, we introduce ThReadMed-QA, a multi-turn medical dialogue dataset of 2,437 patient-physician conversation threads comprising 8,204 question-answer pairs, derived from real patient interactions on AskDocs. This dataset enables systematic evaluation of whether models can detect and correct misconceptions under a multi-turn context. We evaluate five LLMs using a rubric-based LLM-as-a-Judge framework that scores responses based on their ability to identify and correct misconceptions. Our experiments reveal a consistent pattern: even frontier models that can address misconceptions in a single interaction degrade substantially over subsequent turns. GPT-5 and Claude-Haiku correct these false presuppositions around 85% on initial questions but drop to roughly 50% within two follow-ups. An oracle analysis replacing prior model outputs with physician responses shows that much of the degradation is driven by error propagation, while performance remains imperfect even under correct context. Even when models tend to correct misconceptions initially, their performance degrades substantially over later turns, leading to inconsistent and potentially unsafe guidance in patient-facing settings and highlighting the need for evaluation frameworks that capture multi-turn behavior.

### 🤖 AI 总结

**一句话总结**：Patients seeking medical information often ask questions that embed incorrect assumptions or misconceptions. In such cases, safe medical communication requires not only answering the question, but ide...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Evaluating, Large, Language, Models, Misconceptions, Multi-Turn, Medical, Conversations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12884v1) | [下载PDF](https://arxiv.org/pdf/2607.12884v1.pdf)

---

## [10. Can LLMs Write Reliable Rubrics? A Meta-Evaluation for Experiment Reproduction](https://arxiv.org/abs/2607.12835v1)

**作者**：Hanhua Hong, Yizhi Li, Jiaoyan Chen 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-14

### 📄 论文摘要

Rubric-based evaluation is a promising approach for assessing open-ended outputs from LLM-based research agents, particularly in paper reproduction, where direct paper-to-repository comparison is prone to hallucination. However, constructing paper-specific rubrics requires substantial expert effort, limiting the scalability of benchmarks such as PaperBench. In this work, we present, to our knowledge, the first systematic meta-evaluation of LLM-generated rubrics for paper reproduction. We reformulate rubrics into a checklist-style format and evaluate four generation settings across two backbone models. We meta-evaluate generated rubrics intrinsically by semantic similarity and extrinsically by score alignment with ground-truth rubrics. Our results show that the augmented settings substantially improves downstream evaluation alignment, with the strongest setting approaching the human baseline, while intrinsic gains are more modest. Further analyses reveal that LLM-generated rubrics are often overly fine-grained, biased toward high scores, and less adaptive to paper domains, highlighting both the affordances and limitations.

### 🤖 AI 总结

**一句话总结**：Rubric-based evaluation is a promising approach for assessing open-ended outputs from LLM-based research agents, particularly in paper reproduction, where direct paper-to-repository comparison is pron...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Can, Write, Reliable, Rubrics?, Meta-Evaluation, Experiment, Reproduction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12835v1) | [下载PDF](https://arxiv.org/pdf/2607.12835v1.pdf)

---

## [11. Knowledgeless Language Models: Suppressing Parametric Recall for Evidence-Grounded Language Modeling](https://arxiv.org/abs/2607.12831v1)

**作者**：Roi Cohen, Yvan Carré, Nick Lechtenbörger 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-14

### 📄 论文摘要

Language models encode substantial factual knowledge in their parameters, which can lead to unreliable behavior when this knowledge is outdated, incomplete, or misaligned with the provided context. In this work, we study whether modifying the pretraining signal can systematically shift models away from parametric recall and toward evidence-grounded reasoning. We introduce Knowledge--''Less'' Language Models (KLLMs), a fundamentally different epistemic training paradigm for LLMs, which are pretrained on corpora in which named entities are anonymized, thereby removing a primary channel for entity-linked factual supervision. This intervention substantially reduces closed-book factual recall, while often improving performance on tasks where relevant information is provided as context. Across multiple model scales, KLLMs consistently outperform matched baselines on contextual question answering, fact verification, and hallucination detection benchmarks. Crucially, in retrieval-grounded settings with imperfect evidence, KLLMs show improved robustness and achieve up to 20--25\% relative gains over standard language models. They further exhibit better calibration, with improved ECE, Brier score, and AUROC, as well as more reliable abstention behavior. Our results demonstrate that suppressing entity-linked supervision during pretraining induces a shift in epistemic behavior: KLLMs rely less on parametric knowledge and more on external evidence, leading to improved reliability under realistic conditions. This suggests that pretraining-time control over knowledge acquisition can complement retrieval-augmented and tool-based systems by providing a more evidence-sensitive base model.

### 🤖 AI 总结

**一句话总结**：Language models encode substantial factual knowledge in their parameters, which can lead to unreliable behavior when this knowledge is outdated, incomplete, or misaligned with the provided context. In...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Knowledgeless, Language, Models, Suppressing, Parametric, Recall, Evidence-Grounded, Modeling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12831v1) | [下载PDF](https://arxiv.org/pdf/2607.12831v1.pdf)

---

## cs.CV

## [12. DermDepth: Toward Monocular Metric Scale 3D Reconstruction Models for Dermatology](https://arxiv.org/abs/2607.13010v1)

**作者**：Héctor Carrión, Narges Norouzi  
**分类**：cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

Dermatological practice routinely involves measuring and tracking lesion size, morphology and texture, as critical components of wound or skin cancer screening, monitoring and diagnosis. To accomplish this task, practitioners often image the skin surface with commonly available off-the-shelf camera sensors. This has led to an overwhelming research focus on 2D methods while these objectives naturally benefit from 3D information. In this paper, we demonstrate that dense monocular 3D reconstructions, metric scale measurements and rich surface normal texture estimates are achievable for both dermoscopic and macroscopic cases without the need for additional hardware or multiple captures. We present DermDepth, the first single-view metric scale 3D model for the dermatological domain and D-Synth, the first synthetic dermoscopic dataset with pixel-perfect 3D information. Our experiments show training DermDepth on D-Synth corrects metric scale error from over 16x to under 1.1x for real dermoscopic data, while preserving geometric quality and increasing texture richness. Fine-tuning on a small amount of real clinical samples generalizes our method across three real-world benchmarks spanning the few mm to hundred cm range, diverse skin-tones, chronic wound cases and produces measurements broadly consistent with disease size reported in medical literature. All code, data and models are available at https://github.com/hectorcarrion/dermdepth.

### 🤖 AI 总结

**一句话总结**：Dermatological practice routinely involves measuring and tracking lesion size, morphology and texture, as critical components of wound or skin cancer screening, monitoring and diagnosis. To accomplish...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, DermDepth, Toward, Monocular, Metric, Scale, Reconstruction, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13010v1) | [下载PDF](https://arxiv.org/pdf/2607.13010v1.pdf)

---

## [13. Controllable Generation of Diverse Dermatological Imagery for Fair and Efficient Malignancy Classification](https://arxiv.org/abs/2607.12987v1)

**作者**：Héctor Carrión, Narges Norouzi  
**分类**：cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

Accurate dermatological diagnosis naturally necessitates equitable performance across diverse populations, yet a systematic lack of expertly annotated images, especially for underrepresented skin tones and rare diseases, impedes progress toward measurably fair methods. We introduce cgDDI (Controllable Generation of Diverse Dermatological Imagery), a hybrid framework that (1) synthesizes realistic healthy skin samples without disturbing other input properties, (2) maps single-sample rare lesions onto novel skin-tones and locations non-parametrically, and (3) allows for efficient parametric generation with as few as 10 training samples. The framework supports both human and automated segmentation masking, enabling scalability to datasets without pre-made lesion masks. We grow a 656-image dataset by more than 400x and validate across two datasets: biopsy-confirmed Diverse Dermatology Images (DDI) and expert-verified Fitzpatrick17k (F17k). On the DDI benchmark, we achieve malignancy classification accuracy of 86.4% under synthetic-only training and 90.9% state-of-the-art performance with real data fine-tuning, alongside leading fairness metrics. Cross-dataset experiments show +13.9% accuracy improvements on unseen F17k data despite minimal disease overlap. We openly release 266k+ synthetic images, code, and generative models to further support fairness research at https://github.com/hectorcarrion/ControllableGenDDI.

### 🤖 AI 总结

**一句话总结**：Accurate dermatological diagnosis naturally necessitates equitable performance across diverse populations, yet a systematic lack of expertly annotated images, especially for underrepresented skin tone...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Controllable, Generation, Diverse, Dermatological, Imagery, Fair, Efficient

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12987v1) | [下载PDF](https://arxiv.org/pdf/2607.12987v1.pdf)

---

## [14. ViCo3D: Empowering LiDAR-based Collaborative 3D Object Detection with Vision Foundation Models](https://arxiv.org/abs/2607.12959v1)

**作者**：Haojie Ren, Songrui Luo, Lingfeng Wang 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

LiDAR-based collaborative 3D perception in Vehicle-to-Everything (V2X) systems typically relies on fusing bird's-eye-view (BEV) features across agents. However, current BEV representations, typically extracted by LiDAR backbones trained from scratch, are geometry-dominated and lack general semantic priors, inherently limiting the efficacy of feature-level collaboration. Meanwhile, vision foundation models (VFMs) pretrained on large-scale image data have demonstrated strong capability in learning general-purpose and informative visual representations for 2D tasks, and have the potential to enhance agent-wise LiDAR BEV representations for collaboration. Despite this potential, adapting VFMs to LiDAR-based 3D detection remains challenging due to the substantial image-point cloud modality gap. To bridge this gap, we propose ViCo3D, a collaborative 3D object detection framework powered by VFMs. Specifically, ViCo3D adapts VFMs to LiDAR-based collaborative perception from three aspects: First, ViCo3D projects point clouds onto the BEV plane as three-channel images, enabling DINOv2 to extract BEV-space visual features from LiDAR inputs. Besides, to effectively integrate these DINOv2-derived features with LiDAR geometric features, ViCo3D introduces a multi-scale BEV fusion module within the single-agent encoder. In addition, ViCo3D adopts an ego-centric cross-agent fusion strategy to aggregate complementary information from multiple agents. Experiments on DAIR-V2X and V2XSet demonstrate that ViCo3D achieves state-of-the-art 3D detection performance. Remarkably, it delivers up to 1.8x greater collaborative gains than prior methods on DAIR-V2X. The code will be made public available for future investigation.

### 🤖 AI 总结

**一句话总结**：LiDAR-based collaborative 3D perception in Vehicle-to-Everything (V2X) systems typically relies on fusing bird's-eye-view (BEV) features across agents. However, current BEV representations, typically ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, ViCo3D, Empowering, LiDAR-based, Collaborative, Object, Detection, Vision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12959v1) | [下载PDF](https://arxiv.org/pdf/2607.12959v1.pdf)

---

## [15. Point Tracking in Surgery--The 2025 Surgical Tattoos in Infrared Challenge (STIRC2025)](https://arxiv.org/abs/2607.12939v1)

**作者**：Adam Schmidt, Mert Asim Karaoglu, Zijian Wu 等 35 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

Point tracking in surgery is crucial to enable applications in downstream tasks such as segmentation, 3D reconstruction, virtual tissue landmarking, autonomous probe-based scanning, and subtask autonomy. This paper introduces the 2025 iteration of a point tracking challenge to address this, wherein participants submit their algorithms for quantification. Their algorithms are evaluated using a dataset named surgical tattoos in infrared (STIR), with the challenge named the STIR Challenge 2025 (STIRC2025). The STIR Challenge 2025 comprises two quantitative components: accuracy and efficiency. The accuracy component tests the accuracy of algorithms on in vivo and ex vivo sequences. The efficiency component tests algorithm inference latency. The challenge was conducted as a part of MICCAI EndoVis 2025, and seven teams participated in this challenge. In this paper we summarize the challenge results and participant methods. The challenge dataset is available at: https://zenodo.org/records/20191078, and the code for baseline models and metrics calculation is available here: https://github.com/athaddius/STIRMetrics

### 🤖 AI 总结

**一句话总结**：Point tracking in surgery is crucial to enable applications in downstream tasks such as segmentation, 3D reconstruction, virtual tissue landmarking, autonomous probe-based scanning, and subtask autono...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Point, Tracking, Surgery--The, Surgical, Tattoos, Infrared, Challenge, STIRC2025

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12939v1) | [下载PDF](https://arxiv.org/pdf/2607.12939v1.pdf)

---

## [16. Domain-Incremental Remote Sensing Change Detection via Difference-Guided Adaptation and Frequency-Decoupled Distillation](https://arxiv.org/abs/2607.12934v1)

**作者**：Daifeng Peng, Yaning Li, Haiyan Guan  
**分类**：cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

Remote sensing change detection (RSCD) models are prone to catastrophic forgetting when incrementally adapted to new domains. Existing domain-incremental learning (DIL) methods mainly preserve image-level representations but often overlook bitemporal discrepancy cues, which are critical for robust change detection under domain shifts. To address this limitation, we propose DG-FDD, a domain-incremental change detection framework that integrates Difference-Guided Adaptation and Frequency-Decoupled Distillation. Specifically, the Difference-Guided Dynamic Adapter (DGDA) models bitemporal feature discrepancies to promote change-aware feature adaptation and reduce domain-specific interference. Meanwhile, the Frequency-Decoupled Knowledge Distillation strategy with Cross-domain Synthesis (FDKD-CS) separates structural information from domain style in the frequency domain, enabling stable knowledge transfer without historical data. Extensive experiments on three public high-resolution RSCD datasets under two- and three-domain incremental protocols demonstrate that DG-FDD effectively mitigates catastrophic forgetting. Compared with independently trained single-task models, DG-FDD records mean relative changes in F1 and IoU of only -0.23% and -0.45%, respectively, across six two-domain sequences, and -0.69% and -1.31%, respectively, across the three evaluated three-domain sequences. These results indicate a favorable stability-plasticity balance between historical knowledge retention and new-domain adaptation in continual cross-domain change detection.

### 🤖 AI 总结

**一句话总结**：Remote sensing change detection (RSCD) models are prone to catastrophic forgetting when incrementally adapted to new domains. Existing domain-incremental learning (DIL) methods mainly preserve image-l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Domain-Incremental, Remote, Sensing, Change, Detection, via, Difference-Guided, Adaptation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12934v1) | [下载PDF](https://arxiv.org/pdf/2607.12934v1.pdf)

---

## [17. Open-KNEAD: Knowledge-grounded Nutrition Estimation via Agentic Decomposition](https://arxiv.org/abs/2607.12911v1)

**作者**：Bruce Coburn, Jingbo Yue, Jinge Ma 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

Multimodal Large Language Models (MLLMs) are increasingly used for dietary assessment from meal images, where retrieval-augmented grounding was shown to sharpen nutrition estimates. However, we find this premise no longer holds for current MLLMs. A modern MLLM's direct estimate now matches or surpasses the full retrieval pipeline. This raises a question: if retrieval no longer improves the overall estimate, can it still deliver the two things clinicians value, accurate portions and a traceable, item-by-item record? We pursue this while preserving what matters for clinical adoption: minimal user burden (a single, unannotated meal image), explainability (an auditable record), and privacy (locally hosted inference). We introduce Open-KNEAD, a knowledge-grounded agentic framework for meal nutrition estimation that is training-free and locally deployable. Each decomposed food item is grounded to a Food and Nutrient Database for Dietary Studies (FNDDS) code via selective, nutrient-aware retrieval, composing an auditable per-item record. Across two open MLLM families and three cuisines, Open-KNEAD improves portion estimates over both prior grounding methods and direct estimation in most backbone-dataset settings. An agent-internal recipe-prior step further recovers the invisible cooking-added energy that biases estimates on non-US cuisine. The advantage is largest on the dietitian-verified ACETADA dataset, where the local open agent surpasses the direct portion estimates of two frontier closed models by roughly $30\%$ and $53\%$, all while keeping every meal image on local hardware. We release the Open-KNEAD framework and its agent-ready FNDDS knowledge base.

### 🤖 AI 总结

**一句话总结**：Multimodal Large Language Models (MLLMs) are increasingly used for dietary assessment from meal images, where retrieval-augmented grounding was shown to sharpen nutrition estimates. However, we find t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Open-KNEAD, Knowledge-grounded, Nutrition, Estimation, via, Agentic, Decomposition, Multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12911v1) | [下载PDF](https://arxiv.org/pdf/2607.12911v1.pdf)

---

## [18. Rank-1 Identity Consensus Predicts Gallery Enrollment in 1:N Face Matching More Accurately than Score Thresholding](https://arxiv.org/abs/2607.12903v1)

**作者**：Gabriella Pangelinan, Aman Bhatta, Michael C. King 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

In operational 1:N face identification, a crucial question arises for each probe: is this person enrolled in the gallery or not? The stakes are high and asymmetric. Rejecting a mate-present (MP) probe loses a valid lead; accepting a mate-absent (MA) probe makes every returned candidate a false identification, at worst a wrongful arrest. Most approaches threshold match scores, but scores shift substantially with image quality and gallery size and composition, making thresholds fixed before deployment brittle under realistic conditions. Our prior work introduced 1-consistency, the only method based on rank consensus across multiple independently trained matchers: a probe is labeled MP if all matchers return the same rank-1 identity. This work stress-tests 1-consistency across 36 (gallery, probe quality) scenarios spanning four quality levels and two structural axes: images per identity and total enrolled identities. We benchmark against two score-thresholding methods that bracket what any deployed threshold could achieve. Fixed Score-Thresholding (FST), calibrated once on baseline conditions, collapses asymmetrically as quality degrades: MP recall falls below 2% while MA recall holds near 100%. Oracle Score-Thresholding (OST), re-tuned per scenario, is the best any threshold could theoretically do, yet for degraded probes 1-consistency matches it with zero tuning. The two differ mainly in error type (OST favors MP recall, 1-consistency favors MA recall), but on one axis 1-consistency does not merely match the oracle: when it labels a probe MP, it returns the correct mate 97-100% of the time versus OST's 66-84% under severe degradation. In short, 1-consistency delivers oracle-level accuracy without the impossible requirement: it sets no threshold, so it needs no advance knowledge of the conditions a probe will arrive in, which is what makes it usable.

### 🤖 AI 总结

**一句话总结**：In operational 1:N face identification, a crucial question arises for each probe: is this person enrolled in the gallery or not? The stakes are high and asymmetric. Rejecting a mate-present (MP) probe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Rank-1, Identity, Consensus, Predicts, Gallery, Enrollment, Face, Matching

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12903v1) | [下载PDF](https://arxiv.org/pdf/2607.12903v1.pdf)

---

## [19. UniMedSeg: Unified In-Context Learning for Multi-Paradigm 2D/3D Medical Image Segmentation](https://arxiv.org/abs/2607.12896v1)

**作者**：Yunzhou Li, Jiesi Hu, Yanwu Yang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

Medical image segmentation foundation models are expected to generalize across diverse clinical scenarios, yet existing universal methods remain fragmented by prompt paradigms and spatial dimensions. Visual in-context learning, interactive segmentation, and language-guided segmentation are typically handled by paradigm-specific models, while 2D and 3D images are also modeled separately. Such isolation prevents heterogeneous annotations and data from being jointly absorbed by a single scalable model and limits cross-paradigm knowledge transfer. To address this bottleneck, we propose UniMedSeg, a Transformer-centric universal segmentation framework that maps visual examples, geometric interactions, language instructions, and 2D/3D images into a shared sequence space, enabling heterogeneous medical supervision to be jointly learned through a unified in-context interface without prompt- or dimension-specific branches. To overcome the long-sequence memory bottleneck caused by visual contexts, we introduce Decoupled Split Attention, which reduces attention complexity to linear while preserving hardware-friendly computation and focused context-target interaction. Extensively trained and evaluated on a large corpus curated from 27 public datasets, UniMedSeg achieves state-of-the-art performance across visual in-context, interactive, and language-guided segmentation without task-specific fine-tuning, demonstrating strong generalization on diverse held-out tasks. The code and model weights are publicly available at https://github.com/Lii1228/UniMedSeg

### 🤖 AI 总结

**一句话总结**：Medical image segmentation foundation models are expected to generalize across diverse clinical scenarios, yet existing universal methods remain fragmented by prompt paradigms and spatial dimensions. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：2D, 3D, UniMedSeg, Unified, In-Context, Learning, Multi-Paradigm, Medical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12896v1) | [下载PDF](https://arxiv.org/pdf/2607.12896v1.pdf)

---

## [20. Hy-Embodied-VLM-1.0: Efficient Physical-World Agents](https://arxiv.org/abs/2607.12894v1)

**作者**：Ziyi Wang, Xumin Yu, Yongming Rao 等 22 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

Building capable embodied agents requires not only multimodal perception and understanding, but also agentic capabilities for reasoning about actions, adapting to evolving situations, and interacting with the physical world. In this report, we introduce Hy-Embodied-VLM-1.0, an efficient and powerful embodied foundation model specifically designed for embodied agents operating in the physical world. To cultivate such capabilities from the pre-training stage onward, we define an action-centric capability taxonomy comprising three progressive dimensions: Action-Relevant State Understanding, Action-Transition Reasoning, and Sequential and Adaptive Reasoning. Guided by this taxonomy, we develop a systematic data pipeline and curate data mixtures spanning both pre-training and post-training. To deliver strong physical-world understanding and interaction capabilities while supporting latency-sensitive deployment, we build our model on the Hy3-A3B language backbone and the Hy-ViT2 vision encoder. Its efficient Mixture-of-Experts architecture combines strong model capacity with high inference efficiency. We evaluate Hy-Embodied-VLM-1.0 on a comprehensive suite of 38 benchmarks covering embodied perception, physical-world understanding, and embodied reasoning. The model achieves the best performance among similarly sized models on 19 of the 38 benchmarks and substantially outperforms strong competitors, including Qwen3.6-A3B and Cosmos 3. Compared with the previous-generation Hy-Embodied-0.5 MoT-2B, Hy-Embodied-VLM-1.0 improves average performance by 8.4%. Despite activating only 3B parameters, it achieves performance close to that of the previous-generation model with 32B activated parameters. Beyond static benchmark evaluation, Hy-Embodied-VLM-1.0 also demonstrates strong performance on embodied agentic tasks requiring multi-turn interaction and long-horizon reasoning.

### 🤖 AI 总结

**一句话总结**：Building capable embodied agents requires not only multimodal perception and understanding, but also agentic capabilities for reasoning about actions, adapting to evolving situations, and interacting ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Hy-Embodied-VLM-1.0, Efficient, Physical-World, Building, capable, embodied, requires

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12894v1) | [下载PDF](https://arxiv.org/pdf/2607.12894v1.pdf)

---

## [21. Inhibited Self-Attention: Sharpening Focus in Vision Transformers](https://arxiv.org/abs/2607.12881v1)

**作者**：Peter R. D. van der Wal, Nicola Strisciuglio, George Azzopardi  
**分类**：cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

Vision Transformers (ViTs) have demonstrated remarkable performance in computer vision tasks. However, their self-attention mechanism often diffuses focus across background regions, relying on spurious correlations rather than object-relevant cues. Inspired by inhibitory mechanisms observed in biological vision systems, we propose the Inhibited Self-Attention (ISA), a novel self-attention that integrates inhibitory signals to enhance feature selectivity and suppress spurious responses. In contrast to conventional self-attention, which relies solely on positive attention values due to softmax normalization, our approach retains and utilizes negative attention scores to suppress irrelevant features and sharpen focus on objects of interest. Experiments across multiple datasets, including ImageNet-1k and COCO, and several robustness benchmarks demonstrate that ISA enhances object-centric selectivity, reduces shortcut reliance, and improves out-of-distribution generalization. Our analysis of relevance maps confirms that ViTs with ISA exhibit sharper, more localized focus on object-relevant regions while reducing distractions from non-relevant (background) features, enabling more reliable models. We release our code at https://github.com/prdvanderwal/inhibited-self-attention

### 🤖 AI 总结

**一句话总结**：Vision Transformers (ViTs) have demonstrated remarkable performance in computer vision tasks. However, their self-attention mechanism often diffuses focus across background regions, relying on spuriou...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Inhibited, Self-Attention, Sharpening, Focus, Vision, Transformers, ViTs, have

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12881v1) | [下载PDF](https://arxiv.org/pdf/2607.12881v1.pdf)

---

## [22. Metric-Guided Synthetic Image Data Rendering for Deep Learning compatible with Agentic AI](https://arxiv.org/abs/2607.12874v1)

**作者**：Martina Radoynova, Samuel Pantze, Trina De 等 5 位作者  
**分类**：cs.CV, q-bio.QM  
**发布时间**：2026-07-14

### 📄 论文摘要

Deep learning computer vision for scientific applications requires collecting and annotating large datasets in a laborious, expensive and error-prone process. Synthetic data generation through 3D modelling and rendering may simplify this process and increase the accuracy of annotations by generating them programmatically. However, minimising the domain gap between real and synthetic images visually is subjective and lacks systematic quantitative guidance. We present GraNatPy, a Python package with metrics to guide improvement of the rendered scene. We show that quantifiable increase in realism, diversity and size of rendered dataset correlates with improved visual perception of the scene and higher zero-shot performance of an object detection model. Furthermore, we demonstrated using photographs of virological plaque assays that gradient similarity affects performance on small object detection, which can be improved by mixing real and synthetic data. Finally, we turn procedural data rendering into an agentic skill (SynthClaw) to automate the procedural parameter optimisation.

### 🤖 AI 总结

**一句话总结**：Deep learning computer vision for scientific applications requires collecting and annotating large datasets in a laborious, expensive and error-prone process. Synthetic data generation through 3D mode...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Metric-Guided, Synthetic, Image, Data, Rendering, Deep, Learning, compatible

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12874v1) | [下载PDF](https://arxiv.org/pdf/2607.12874v1.pdf)

---

## [23. Statistical Non-linear Reconstruction Loss for Image Anomaly Detection](https://arxiv.org/abs/2607.12866v1)

**作者**：Nguyen Minh Tri, Hoang Khuong Duy, Huynh Cong Viet Ngu  
**分类**：cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

Reconstruction-based methods are a cornerstone of unsupervised image anomaly detection, but they remain vulnerable to \emph{outlier leakage}, where standard mean squared error (MSE) loss drives the model to faithfully reconstruct anomalous patterns. We propose a Non-linear Reconstruction Loss that applies a sigmoid-based squashing function to suppress high-magnitude features, preventing outliers from dominating optimization while preserving sensitivity to normal patterns. In addition, we introduce a statistical calibration scheme that selects the scaling factor $k$ from the confidence interval (CI) of the normal feature distribution, enabling data-driven control of the suppression strength. Our approach achieves competitive or superior anomaly detection performance compared to state-of-the-art methods, reaching 99.0\% Image-AUROC and 97.3\% Pixel-AUROC on MVTec-AD, and 95.3\% Image-AUROC and 99.0\% Pixel-AUROC on VisA. These results indicate that non-linear gradient suppression is an effective mechanism for mitigating outlier leakage and improving anomaly localization in unified industrial inspection settings. The implementation is available at https://github.com/mintii13/Statistical-Non-linear-Reconstruction-Loss.git.

### 🤖 AI 总结

**一句话总结**：Reconstruction-based methods are a cornerstone of unsupervised image anomaly detection, but they remain vulnerable to \emph{outlier leakage}, where standard mean squared error (MSE) loss drives the mo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Statistical, Non-linear, Reconstruction, Loss, Image, Anomaly, Detection, Reconstruction-based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12866v1) | [下载PDF](https://arxiv.org/pdf/2607.12866v1.pdf)

---

## [24. LARAD: Layout-Aware Road Anomaly Detection via Spatial-Logic Reasoning](https://arxiv.org/abs/2607.12858v1)

**作者**：Shiyi Mu, Xujie Chen, Shugong Xu  
**分类**：cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

Accurate open-world obstacle detection is critical for autonomous driving. Current anomaly segmentation methods suffer from a fundamental blind spot: they over-rely on texture novelty to identify out-of-distribution (OoD) objects while ignoring contextual spatial logic. Furthermore, mitigating the resulting false positives often requires cascading massive vision models, introducing unacceptable inference latency. To address these issues, we propose Layout-Aware Road Anomaly Detection (LARAD), shifting the paradigm from appearance matching to spatial-logic reasoning. First, we introduce the Spatial-Logic Violation Synthesis (SLVS) pipeline, which generates training samples that are texture-consistent yet spatially invalid, forcing the model to learn contextual violations. Second, we augment a standard closed-set segmentation network with a lightweight, OoD-guided attention branch. Extensive experiments demonstrate that LARAD significantly enhances robustness against logical anomalies and establishes a new state-of-the-art, all while retaining the high efficiency of a single-model architecture.

### 🤖 AI 总结

**一句话总结**：Accurate open-world obstacle detection is critical for autonomous driving. Current anomaly segmentation methods suffer from a fundamental blind spot: they over-rely on texture novelty to identify out-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LARAD, Layout-Aware, Road, Anomaly, Detection, via, Spatial-Logic, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12858v1) | [下载PDF](https://arxiv.org/pdf/2607.12858v1.pdf)

---

## cs.LG

## [25. The Seriality Gap in Video Diffusion Models](https://arxiv.org/abs/2607.13031v1)

**作者**：Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu 等 4 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-07-14

### 📄 论文摘要

When one ball strikes another, then another, video models should predict the consequences of each bounce. In controlled experiments on multi-ball hard-sphere dynamics, we find that the performance of standard bidirectional video diffusion degrades as the causal chain lengthens, even when provided more denoising steps. In a length-matched single-ball control, where ball-ball interactions are absent, the degradation largely disappears, isolating dependent-event structure rather than video length as the cause. Across intervention studies, methods that increase effective serial computation improve performance disproportionately, including autoregressive/blockwise generation and architectural depth. We identify this pattern as the seriality gap: a mismatch between tasks requiring growing serial computation and video diffusion models whose denoising loop does not provide scalable serial compute. We then prove that, for deterministic video prediction, denoising steps do not add serial computation beyond the backbone, indicating a structural obstacle for video diffusion on serial reasoning and simulation tasks.

### 🤖 AI 总结

**一句话总结**：When one ball strikes another, then another, video models should predict the consequences of each bounce. In controlled experiments on multi-ball hard-sphere dynamics, we find that the performance of ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Seriality, Gap, Video, Models, When, one, ball

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13031v1) | [下载PDF](https://arxiv.org/pdf/2607.13031v1.pdf)

---

## [26. TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale](https://arxiv.org/abs/2607.13028v1)

**作者**：Zhouchonghao Wu, Akshay Rangesh, Weixin Li 等 7 位作者  
**分类**：cs.LG, cs.AI, cs.RO  
**发布时间**：2026-07-14

### 📄 论文摘要

Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains. We present TerraZero, a procedural driving simulator and self-play training stack. A configurable C engine runs simulation on the CPU and policy inference on the GPU over a zero-copy path, sustaining 1.3M agent-steps per second on a single server-grade GPU, far faster than existing object-level simulators, while keeping fidelity lighter single-agent systems omit: heterogeneous agents, multiple dynamics models, and full traffic-rule enforcement. TerraZero treats logged data only as a source of real-world map geometry, populating each map with randomized rule-based road users and signal controllers and randomizing agent dynamics, rewards, and sizes per episode, so a map yields an unbounded set of scenarios. Every reported policy trains from scratch by reinforcement learning alone on a compute-efficient self-play recipe across GPUs, with zero human demonstrations and no fallback planner at inference. Policies generalize zero-shot across cities and datasets, including emergent left-hand-traffic driving without explicit supervision. As an ego policy, TerraZero is the first fully learned policy to top the InterPlan long-tail benchmark, ahead of larger learned planners; on routine-driving val14 it ranks among the best approaches and is the safest, posting the best collision and time-to-collision scores. On Waymo Open Sim Agents realism the same recipe outperforms other demonstration-free methods and is competitive with the strongest reference-anchored self-play method. One stack serves both roles: driving policies across dynamics for cars and trucks, and sim agents that jointly control vehicles, pedestrians, and cyclists.

### 🤖 AI 总结

**一句话总结**：Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse eno...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, TerraZero, Procedural, Driving, Simulation, Zero-Demonstration, Self-Play, Scale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13028v1) | [下载PDF](https://arxiv.org/pdf/2607.13028v1.pdf)

---

## [27. The Spectrum Is Not Enough: When Context Helps Time-Series Forecasting](https://arxiv.org/abs/2607.13006v1)

**作者**：Mert Onur Cakiroglu, Mehmet Dalkilic, Hasan Kurban  
**分类**：cs.LG  
**发布时间**：2026-07-14

### 📄 论文摘要

A growing family of indices scores how predictable a series is from its spectrum. Practitioners increasingly read these scores as answering a different question: whether \emph{adding context}, a longer lookback, a retrieval plug-in, or a pretrained model, will help. These are not the same question. The value of context is a property of the operating point, not of the series. Any index built from the power spectrum is invariant under phase randomization, whereas the beyond-second-order value that retrieval and foundation models supply is not, because a phase-randomized series is asymptotically Gaussian. We state this as an impossibility result and isolate it with surrogate pairs that fix the spectrum and the marginal by construction. We then give a label-free, configuration-level diagnostic, the coverage deficit, whose principal term measures beyond-spectrum structure as the gain of analog over linear prediction. On seven benchmarks the prediction holds: window-keyed retrieval's value collapses across surrogate pairs (ECL median $+33\%\!\to\!-35\%$, $p{<}10^{-40}$) while every spectral index stays frozen; a foundation model's value splits into a surviving second-order part and a small beyond-linear margin that collapses; a longer linear window's value survives. Leave-one-dataset-out, the structure term predicts the sign of beyond-spectrum value where the spectral indices trail it, and the reverse holds for the second-order mechanism. We introduce no new forecaster; the contribution is the distinction, a controlled comparison, and a diagnostic for the deployment decision. Code: https://anonymous.4open.science/r/SINE.

### 🤖 AI 总结

**一句话总结**：A growing family of indices scores how predictable a series is from its spectrum. Practitioners increasingly read these scores as answering a different question: whether \emph{adding context}, a longe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Spectrum, Not, Enough, When, Context, Helps, Time-Series, Forecasting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13006v1) | [下载PDF](https://arxiv.org/pdf/2607.13006v1.pdf)

---

## [28. Contrastive-Collapsed Loss for Flexible and Geometrically Optimal Embeddings and Faster Convergence](https://arxiv.org/abs/2607.12916v1)

**作者**：Blanca Cano-Camarero, Ángela Fernández-Pascual, José R. Dorronsoro  
**分类**：cs.LG  
**发布时间**：2026-07-14

### 📄 论文摘要

In this work, we introduce CoCo, a loss function aimed at learning normalized and well-structured representations. The proposed loss encourages intra-class collapse and inter-class contrast while preserving sufficient flexibility for neural networks to approximate geometrically optimal embeddings with large angular separation between classes. We provide a theoretical analysis positioning CoCo with respect to related objectives such as dot regression and cross-entropy, showing that the new proposed loss benefits from closer initialization to the optimal configuration, more informative gradients, and stronger incentives for class-wise representation collapse. Extensive experiments on diverse tabular datasets from the OpenML-CC18 benchmark show that CoCo achieves competitive performance with state-of-the-art methods, including kernel SVM, Random Forest, dot regression, and cross-entropy-based neural networks. In addition, both theoretical arguments and empirical analyses demonstrate that the proposal promotes tighter class clustering and faster convergence. These results highlight CoCo loss as an effective objective for learning discriminative representations while maintaining competitive predictive performance.

### 🤖 AI 总结

**一句话总结**：In this work, we introduce CoCo, a loss function aimed at learning normalized and well-structured representations. The proposed loss encourages intra-class collapse and inter-class contrast while pres...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Contrastive-Collapsed, Loss, Flexible, Geometrically, Optimal, Embeddings, Faster, Convergence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12916v1) | [下载PDF](https://arxiv.org/pdf/2607.12916v1.pdf)

---

## [29. Energy-Based Physics-Informed Form Finding for Clustered Tensegrity Structures](https://arxiv.org/abs/2607.12888v1)

**作者**：Jing Qin, Muhao Chen  
**分类**：cs.LG, math.NA  
**发布时间**：2026-07-14

### 📄 论文摘要

Tensegrity form-finding and physical property prediction are fundamental inverse problems in structural mechanics, which aim to determine equilibrium configurations and internal force distributions. These problems are challenging due to strong nonlinearity arising from the coupling between geometry and forces, the need to ensure structural stability, and the enforcement of constraints such as boundary conditions and symmetry. Moreover, traditional methods often lack robustness to noise and outliers. This paper proposes an energy-based learning framework for clustered tensegrity form finding and physical property prediction. The proposed approach incorporates total potential energy minimization and constitutive relations into the training objective, enabling the simultaneous prediction of equilibrium nodal configurations and associated physical quantities, including member forces and force densities. By incorporating energy-based physical losses directly into the learning process, the framework improves physical consistency, robustness, and data efficiency. Numerical experiments on tensegrity structures, including prism and lander systems, show the great potential of the proposed approach and demonstrate its capability for scalable form finding and accurate prediction of structural properties.

### 🤖 AI 总结

**一句话总结**：Tensegrity form-finding and physical property prediction are fundamental inverse problems in structural mechanics, which aim to determine equilibrium configurations and internal force distributions. T...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Energy-Based, Physics-Informed, Form, Finding, Clustered, Tensegrity, Structures, form-finding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12888v1) | [下载PDF](https://arxiv.org/pdf/2607.12888v1.pdf)

---

## [30. Verifier-Based Reinforcement Fine-Tuning of Reasoning Models for Thermal Energy Storage Control](https://arxiv.org/abs/2607.12856v1)

**作者**：Takumi Shioda, Kohei Terashima, Tatsuo Nagai  
**分类**：cs.LG  
**发布时间**：2026-07-14

### 📄 论文摘要

Buildings are expected to shift cooling loads in response to grid conditions. Thermal energy storage (TES) enables this shift, but scheduling it well requires planning hours ahead under storage constraints. Model predictive control (MPC) and reinforcement learning are difficult to scale across buildings. This study instead adapts an open-weight reasoning model through reinforcement learning with verifiable rewards (RLVR). We convert exact offline dynamic-programming (DP) action values into dense rewards for every candidate action. Using only 30 training prompts, reinforcement fine-tuning (RFT) trains the model as an upper-level scheduler that outputs hourly heat-pump setpoints from text-based states and forecasts. Evaluation uses a deliberately simple office-building TES benchmark where exact DP is tractable and the optimum is known. RFT reduces the open-weight model's emissions from 70.5 to 61.2 kg-CO2, close to the DP optimum of 60.8 kg-CO2. GPT-5 nearly matches DP and MPC without task-specific training, while GPT-4o, a non-reasoning LLM, produces higher emissions than the no-storage baseline, so inference-time reasoning appears important. Trace analysis shows that RFT mainly stabilizes observable planning patterns (candidate comparison, look-ahead, and feasibility checking) rather than creating a new strategy. Robustness and generalization tests clarify what transfers: the reinforced planning patterns persist under forecast errors and an unseen TES condition and carry over to a battery task, but its different structure limits the gains. DP-based verifiable rewards offer a practical way to adapt open-weight reasoning models to building storage scheduling. These results motivate higher-fidelity tests of whole-building control and scalable verifiers for city-scale energy management.

### 🤖 AI 总结

**一句话总结**：Buildings are expected to shift cooling loads in response to grid conditions. Thermal energy storage (TES) enables this shift, but scheduling it well requires planning hours ahead under storage constr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Verifier-Based, Reinforcement, Fine-Tuning, Reasoning, Models, Thermal, Energy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.12856v1) | [下载PDF](https://arxiv.org/pdf/2607.12856v1.pdf)

---

