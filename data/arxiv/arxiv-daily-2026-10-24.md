# arXiv AI 论文日报 | 2026-10-24

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (12 篇)
- [cs.AI](#csAI) (5 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.CL](#csCL) (3 篇)

---

## cs.AI

## [1. Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning](https://arxiv.org/abs/2610.31667v1)

**作者**：Mahdi Salmani, Adel Javanmard, Devansh Gupta 等 4 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-10-22

### 📄 论文摘要

Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. Running all candidate solutions to completion can be computationally demanding, so recent work prunes the candidate pool after generating only a short prefix, committing further computation only to the surviving candidates. Existing pruning strategies divide broadly into two categories: Quality-based methods assign a score to each partial solution and discard those predicted to ultimately lead to an incorrect final solution, while diversity-based methods select partial solutions that follow different reasoning trajectories and are therefore likely to cover different final solutions. The tension between these two objectives is an instance of exploration versus exploitation, yet little to no prior work on pruning exposes this trade-off directly, let alone optimizes it. In this paper, we introduce a pruning procedure that addresses this trade-off directly by optimizing pass@$k$ over the selected solution pool. In particular, it chooses the pool to maximize the probability that at least one of its partial solutions, when continued to completion, yields a correct answer. Because this objective simultaneously rewards high-quality partial solutions and penalizes redundancy among them, quality and diversity are naturally balanced by the criterion itself rather than through separate ad-hoc design choices. On eight open-weight reasoning models, our method outperforms existing quality-based and diversity-based pruning strategies. The gains are particularly pronounced when the pruning procedure keeps a moderate number of partial solutions for continued generation, highlighting the value of directly balancing quality and diversity during pruning.

### 🤖 AI 总结

**一句话总结**：Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. Runn...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Direct, Pass@$k$, Optimization, Thought, Pruning, Balancing, Quality, Diversity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31667v1) | [下载PDF](https://arxiv.org/pdf/2610.31667v1.pdf)

---

## [2. EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](https://arxiv.org/abs/2610.31650v1)

**作者**：Qijin Zhang, Hanzhen Wang, Yuehan Zhao 等 7 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-10-22

### 📄 论文摘要

Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched unsafe/safe task pairs across six domains. By systematically suppressing critical facts, the benchmark measures unsafe execution under critical evidence omission and determines the minimum observed failure cardinality, including failures with full evidence and cases with no observed failure after exhaustive testing. An independent audit tool tests whether agents seek missing facts and then withhold prohibited actions while completing permissible tasks. The benchmark reveals substantial variation across the ten models in omission robustness, evidence acquisition, and appropriate action. Resistance to missing evidence does not necessarily translate into useful recovery. Recovery access reduces unsafe execution for all ten models, but agents differ in whether they actively obtain the missing facts and use them to act appropriately in both worlds.

### 🤖 AI 总结

**一句话总结**：Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action eve...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, EpiSEM-Bench, Evaluating, Safety, Evidence, Recovery, under

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31650v1) | [下载PDF](https://arxiv.org/pdf/2610.31650v1.pdf)

---

## [3. Simulated Control Evals](https://arxiv.org/abs/2610.31593v1)

**作者**：Jeffrey Olmo, David Zhang, Tyler Tracy  
**分类**：cs.AI  
**发布时间**：2026-10-22

### 📄 论文摘要

Control evaluations measure whether safeguards can prevent an AI model from causing undesired outcomes even when it is intentionally trying to do so. These evaluations typically use purpose-built control settings and extrapolate their results to a model's deployment. However, the effectiveness of safeguards in deployment can depend on features of environments and tasks that control settings do not represent. To broaden where control evaluations can be run, we introduce simulated control evaluations (SCEs), which use a language model to simulate tool responses in place of an environment. We evaluate SCEs on LinuxArena, where execution provides ground-truth outcomes. We compare SCE prediction errors with those from a separate control setting, BashArena, and with variation in control metrics within LinuxArena. For independently sampled evaluation and deployment task sets, SCEs predict safety with a root mean squared error of 3.6 percentage points across five monitors at a 5% audit budget, compared with 10.1 for BashArena. SCEs closely reproduce distributions of attack strategies, attacker reasoning, and monitor reasoning, with over tenfold lower KL divergence from execution than BashArena. SCEs explain 78-85% of the between-environment variance in attack success, monitor scores, and safety. This accuracy is sample efficient: SCEs predict safety with less error than BashArena using fewer than 5% as many task-pair draws as the deployment task set. Strategies discovered through simulation also improve monitor performance on held-out LinuxArena attacks, outperforming BashArena and approximately matching improvement from executed strategies. These results suggest that deployment-specific SCEs can be more predictive than control evaluations executed in separate control settings.

### 🤖 AI 总结

**一句话总结**：Control evaluations measure whether safeguards can prevent an AI model from causing undesired outcomes even when it is intentionally trying to do so. These evaluations typically use purpose-built cont...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Simulated, Control, Evals, evaluations, measure, whether, safeguards, can

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31593v1) | [下载PDF](https://arxiv.org/pdf/2610.31593v1.pdf)

---

## [4. Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration](https://arxiv.org/abs/2610.31579v1)

**作者**：Deepthika S, Pawni Yadav, B. Sankar  
**分类**：cs.AI, cs.HC  
**发布时间**：2026-10-22

### 📄 论文摘要

Research on sycophancy asks whether large language models (LLMs) bend towards what their users want to hear. We ask the reverse question: when an LLM is confident, consistent, and wrong, do users bend towards it? In a within-subjects experiment, 32 participants learned up to five science topics by chatting with five assistants built on the same model (GPT-5-mini). Unknown to participants, each assistant's briefing had 0, 25, 50, 75, or 100% of its facts replaced by plausible falsehoods, and every assistant spoke with full confidence. A surprise quiz after each topic offered the correct fact, the planted falsehood, and two distractors, with a confidence rating for every answer. Across 104 quizzes and 1,040 answers, scores fell from 7.4 to 2.9 out of 10, and the planted option was chosen on 60% of falsified items against 11% of correctly taught ones (odds ratio 12.5). Transcript coding showed that whenever the assistant stated a falsehood, it was adopted about 65% of the time at every falsification level. Absorbed falsehoods were held with high confidence (8.4/10), the modeled confidence advantage of right over wrong answers vanished, and the discrimination of confidence for correctness fell from an AUROC of 0.70 to chance, while post-task trust ratings barely moved. Participants tended to return to the chat more when the assistant was worse, but returning went with more absorption, not less, and 30% of all turns pasted quiz questions back to the source being checked. The assistant itself was almost never sycophantic and never conceded under pushback. We introduce a baseline-corrected Human Deference Index to quantify this human-side sycophancy and argue that trustworthiness is a property of the human-AI pair, that sycophancy evaluations should measure both directions, and that learning interfaces must make reliability legible claim by claim.

### 🤖 AI 总结

**一句话总结**：Research on sycophancy asks whether large language models (LLMs) bend towards what their users want to hear. We ask the reverse question: when an LLM is confident, consistent, and wrong, do users bend...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Who, Sycophantic, Whom?, Confident, Human, Deference, Collapse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31579v1) | [下载PDF](https://arxiv.org/pdf/2610.31579v1.pdf)

---

## [5. Contestable Agents for Data Governance: Recording Human Stewardship of AI-Generated Metadata Across Structured and Unstructured Systems](https://arxiv.org/abs/2610.31553v1)

**作者**：Humza Akhtar, Brian Freeman  
**分类**：cs.AI, cs.DB, cs.HC, cs.MA  
**发布时间**：2026-10-22

### 📄 论文摘要

Industrial organizations hold operational knowledge in structured records, such as telemetry, point lists, and transactions, and in unstructured sources, such as manuals, service notes, communications, and inspection reports. Governance programs often manage these sources separately. Classifying, linking, and documenting them depends on a small group of employees with deep domain knowledge. Agents built on large language models can propose metadata, cite documents, and flag quality issues, but unreviewed proposals can spread errors into downstream systems. A perfunctory approval leaves no record of what a reviewer checked. We present contestable governance: specialist agents produce scored, cited arguments for disputed metadata decisions; a steward can accept, reject, modify, or add arguments before commit; and a governance record retains the evidence, interventions, and outcome. A versioned domain glossary supplies model-specific terms and acronym definitions to the agents. We describe the workflow, a triage path that reserves full argumentation for uncertain proposals while preserving review before commit, the scoring and record models, and a gate that controls which verified decisions become precedent. Two HVAC use cases illustrate the pattern: point classification using Brick Schema class labels, supported by an open reference implementation, and an illustrative warranty failure-mode decision linking claim fields and telemetry to service notes and revisioned bulletins.

### 🤖 AI 总结

**一句话总结**：Industrial organizations hold operational knowledge in structured records, such as telemetry, point lists, and transactions, and in unstructured sources, such as manuals, service notes, communications...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, of, Contestable, Data, Governance, Recording, Human, Stewardship

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31553v1) | [下载PDF](https://arxiv.org/pdf/2610.31553v1.pdf)

---

## cs.CL

## [6. Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2](https://arxiv.org/abs/2610.31636v1)

**作者**：Marek Šuppa, Ivan Vykopal, Jaroslav Kopčan  
**分类**：cs.CL  
**发布时间**：2026-10-22

### 📄 论文摘要

Multilingual pipelines such as FineWeb2 apply one recipe across a thousand languages, leaving the failure modes of individual languages unanticipated. We use an LLM once, as a corpus debugger rather than a classifier: a tool-using agent explores the corpus through a read-only, budgeted API and compiles each finding into an executable test, which a native speaker then validates. On the 26.5M-document Slovak portion of FineWeb2, three runs costing \$2.21-\$2.84 each found seven findings over four phenomena. The largest is a machine-generated content farm of 1,408,437 documents (5.32%) that passed the pipeline's filters, 86.6% of it passing even stricter thresholds. Blinded labels support 6 of the 7 findings (defect rates .53-1.00 against .08 in a random control) and do not support one. The compiled suite scans the full corpus in 0.7 s of wall-clock time without a GPU, against \$12k-\$90k per LLM classification pass. The best static sampling baseline validates more selectors than any agent run, at under half the cost. The agent contributes exact prevalence, a precision estimate checked against sampled documents, an account of why the pipeline missed each slice, and a reusable test. We release the framework, Slovak test suite, validation data and agent trajectories.

### 🤖 AI 总结

**一句话总结**：Multilingual pipelines such as FineWeb2 apply one recipe across a thousand languages, leaving the failure modes of individual languages unanticipated. We use an LLM once, as a corpus debugger rather t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Agent, Can, Debug, Web, Corpus?, Agentic, Auditing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31636v1) | [下载PDF](https://arxiv.org/pdf/2610.31636v1.pdf)

---

## [7. Bilingual Language Models Capture Cross-Linguistic Influence in Second-Language Reading](https://arxiv.org/abs/2610.31620v1)

**作者**：Abderrahmane Issam, Irene E. Winther, Stefan L. Frank  
**分类**：cs.CL  
**发布时间**：2026-10-22

### 📄 论文摘要

While monolingual language model (LM) surprisal is widely established as a predictor of reading times, it cannot capture the non-native (L2) reading dynamics that are shaped by the reader's first language (L1). In this work, we investigate whether the cross-lingual transfer within bilingual models aligns with human L1-driven biases during L2 reading. We evaluate bilingual models on eye-tracking data of readers from 12 diverse L1 backgrounds reading English texts. To isolate L1-specific transfer, we compare bilingual models trained on an L1 that matches the readers' L1 background to both a monolingual English baseline and bilingual models trained on other L1s. We demonstrate that matching the readers' L1 improves the prediction of L2 reading times. This predictive advantage is concentrated in late-stage eye-tracking measures, modulated by L1-L2 script overlap, and peaks among intermediate-proficiency readers. These findings provide evidence that bilingual LMs capture aspects of cross-linguistic influence, and that such influence is present in L2 reading behavior.

### 🤖 AI 总结

**一句话总结**：While monolingual language model (LM) surprisal is widely established as a predictor of reading times, it cannot capture the non-native (L2) reading dynamics that are shaped by the reader's first lang...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bilingual, Language, Models, Capture, Cross-Linguistic, Influence, Second-Language, Reading

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31620v1) | [下载PDF](https://arxiv.org/pdf/2610.31620v1.pdf)

---

## [8. Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of Open Language Models on the Spanish MIR Examination](https://arxiv.org/abs/2610.31586v1)

**作者**：Miguel Fernandez-de-Retana, Unai Zulaika, Ruben Sanchez-Corcuera 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.CY, cs.LG  
**发布时间**：2026-10-22

### 📄 论文摘要

Accuracy on medical examinations is common evidence offered for the clinical use of language models, yet a health system that intends to run an open model on its own hardware needs to know considerably more: whether the model recognizes when it is likely to be wrong, whether medical fine-tuning improves this ability, whether its correct answers rest on sound clinical reasoning, or whether it actually uses the images it is given. We examine these questions for four open models of 8 to 27 billion parameters on the Spanish MIR residency examination, scoring 1,552 questions from eight editions under the exam's own rules. Answering every question, the three larger models would rank among roughly the first 600 to 3,000 candidates, with 41 to 43 specialties still open to them. Abstention, however, never pays, because even their least confident answers are right more often than the 25% break-even. Medical fine-tuning reduced overconfidence at the cost of accuracy, without improving how well confidence separates right from wrong answers. Moreover, 13-38% of correct answers rejected a distractor for a clinically unsound reason that confidence did not reflect, and removing or swapping the provided contextual images left accuracy unchanged.

### 🤖 AI 总结

**一句话总结**：Accuracy on medical examinations is common evidence offered for the clinical use of language models, yet a health system that intends to run an open model on its own hardware needs to know considerabl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, LLM, Would, Match, Residency?, Uncertainty, Reasoning, Image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31586v1) | [下载PDF](https://arxiv.org/pdf/2610.31586v1.pdf)

---

## cs.CV

## [9. A Unified Framework for Image-to-3D Part Generation via Variable Granularity](https://arxiv.org/abs/2610.31671v1)

**作者**：Qiwen Gu, Xin Zhou, Xiwu Chen 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-22

### 📄 论文摘要

Controllable 3D part generation is pivotal for digital asset creation, yet existing methods lack the flexibility to accommodate diverse user workflows requiring varying levels of control. In this paper, we introduce FlexPart, a unified image-to-3D part generation framework that supports variable-granularity geometric conditions within a single model. By seamlessly integrating heterogeneous inputs, ranging from sparse points to dense bounding boxes and masks, via gated adaptive modulation, FlexPart unlocks a powerful cross-modal synergy. We also propose an asymmetric geometric guidance mechanism that leverages strong spatial priors to align representations across granularities, improving geometric consistency and facilitating inter-task synergy. Under mask conditioning on PartVerseXL, FlexPart reduces Part CD by 16.6% relative to TripoSG + SAM3D and by 10.5% relative to OmniPart, while maintaining competitive whole-mesh quality. The code can be found at https://github.com/Gucci233/FlexPart

### 🤖 AI 总结

**一句话总结**：Controllable 3D part generation is pivotal for digital asset creation, yet existing methods lack the flexibility to accommodate diverse user workflows requiring varying levels of control. In this pape...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unified, Framework, Image-to-3D, Part, Generation, via, Variable, Granularity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31671v1) | [下载PDF](https://arxiv.org/pdf/2610.31671v1.pdf)

---

## [10. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](https://arxiv.org/abs/2610.31670v1)

**作者**：Yunfei Xie, Howard H. Qian, Shiyi Lan 等 5 位作者  
**分类**：cs.CV, cs.LG, cs.RO  
**发布时间**：2026-10-22

### 📄 论文摘要

Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more capable, should their sensory representations converge toward the structure of physical motion? To examine this, we propose Sensorimotor Alignment ($S^2$), a training-free offline metric that measures how well a model's sensory representation aligns with the geometry of physical motion. We find that $S^2$ correlates positively with downstream robot task success across embodied model families, making it a low-cost offline proxy for prioritizing models before closed-loop evaluation. $S^2$ can also identify promising vision-language model (VLM) backbones even before costly fine-tuning into vision-language-action models (VLAs). Beyond this correlation, $S^2$ offers representation-level explanations for phenomena observed in VLAs and world action models (WAMs). With $S^2$, we extend PRH to embodied models and make sensorimotor alignment empirically measurable, offering insight into why an embodied model succeeds beyond its closed-loop success rate.

### 🤖 AI 总结

**一句话总结**：Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sensorimotor, Alignment, Platonic, Proxy, Embodied, Policy, Success, Robotic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31670v1) | [下载PDF](https://arxiv.org/pdf/2610.31670v1.pdf)

---

## [11. SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing](https://arxiv.org/abs/2610.31659v1)

**作者**：Sy-Tuyen Ho, Anirudh Satheesh, Soham Chawathe 等 7 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-10-22

### 📄 论文摘要

Auditing whether a text-to-image (T2I) model was fine-tuned on a particular image collection is difficult: a model can absorb collection-level visual characteristics without reproducing training images. Proactive dataset-use auditing plants a shared signal in a dataset before release, then later checks whether that signal appears in a suspect model's generated outputs. Existing approaches often trade off verifiability, fidelity, robustness, and deployability. We introduce $\textbf{SpectralCanary}$, which uses a smooth low-pass mask to blend a fixed canary image into every collection image while leaving captions unchanged and requiring neither auxiliary generation nor per-image optimization. A lightweight verifier detects the transferred signal in suspect-model outputs. Across eight tests on the Pokemon dataset and three realistic data transformations, spanning two architectures families, SpectralCanary achieves the highest average per-generation TPR@$1\%$ FPR ($91.1\%$) and fixed threshold model-level accuracy using 30 generations ($94.8\%$) among the evaluated methods. Across five datasets spanning artistic, medical, satellite, and fashion domains with SD3.5, SpectralCanary averages $92.4\%$ per-generation TPR@$1\%$ FPR while preserving the released images (SSIM $0.989$, LPIPS $0.022$) with a near-zero mean change FID (mean $Δ$FID $0.05$) across datasets. Matched-energy ablations on Pokemon and ROCOv2 support our design choice, low-frequency placement transfers more reliably compared to mid/high-frequency placement. Under the evaluated adaptive attacks, the most effective removal requires aggressive modification and incurs more than $25$ $Δ$FID points. These results identify low-frequency visual signals as effective carriers for collection-level T2I audit traces.

### 🤖 AI 总结

**一句话总结**：Auditing whether a text-to-image (T2I) model was fine-tuned on a particular image collection is difficult: a model can absorb collection-level visual characteristics without reproducing training image...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：T2I, SpectralCanary, Embarrassingly, Simple, Low-Frequency, Traces, Dataset-Use, Auditing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31659v1) | [下载PDF](https://arxiv.org/pdf/2610.31659v1.pdf)

---

## [12. BrickWright: Agentic Creation of Physically Feasible Brick Builds](https://arxiv.org/abs/2610.31651v1)

**作者**：Ava Pun, Kevin Dai, Sally Chen 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-22

### 📄 论文摘要

Frontier coding agents are becoming increasingly adept at 3D modeling. Yet, they still face challenges when building objects meant to be assembled in the physical world, often creating invalid assemblies with floating, colliding, or disconnected parts. We argue that providing agents with tools for assembling builds and verifying their physical feasibility is sufficient for them to produce physically valid assemblies that still adhere to input prompts. Focusing on the domain of LEGO brick builds, we present BrickWright, a framework for generating physically feasible brick builds from text or image prompts using pre-trained agents, where a build is physically feasible if it uses only real parts, has no colliding or floating parts, and forms a connected structure if possible. BrickWright guides agents to create builds by writing code with BrickLayer, a Python toolkit with two main components: an ergonomic brick assembly API that halves inference cost compared to working in raw LDraw, and a validator that provides feedback on physical feasibility. Whereas baseline agents achieve physical validity rates ranging from only 9% (GPT-6 Luna) to 69% (GPT-6 Astra), BrickWright-guided agents achieve 100% validity on a sample of 512 prompts, while improving prompt adherence for lightweight agents and maintaining it for stronger agents. Additionally, they outperform specialized models on the text-to-brick task. Code is available on our project page: https://avalovelace1.github.io/brickwright/

### 🤖 AI 总结

**一句话总结**：Frontier coding agents are becoming increasingly adept at 3D modeling. Yet, they still face challenges when building objects meant to be assembled in the physical world, often creating invalid assembl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, BrickWright, Agentic, Creation, Physically, Feasible, Brick, Builds

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31651v1) | [下载PDF](https://arxiv.org/pdf/2610.31651v1.pdf)

---

## [13. Gate3DGen: A Pre-processing Model that Selectively Purifies Real-World Images for 3D Generation](https://arxiv.org/abs/2610.31649v1)

**作者**：Xiaolin Li, Zihao Huang, Fanpeng Meng 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-22

### 📄 论文摘要

Single-image 3D generation has achieved high fidelity on curated benchmarks, yet degrades sharply on real-world images with uneven illumination, blur, and occlusions. Purifying such inputs requires deciding when to intervene and preserving the visual cues needed for 3D generation, while leaving clean inputs unchanged. We introduce Gate3DGen, a selective pre-processing model that gates image inputs to existing 3D generators without retraining them. A degradation-aware router bypasses inputs classified as clean and extracts features to guide purification of the remaining inputs. Conditioned on these features, a 3D-oriented one-step purifier purifies degraded inputs with spatial losses that encourage preservation of object identity, contours, and textural cues. To provide paired supervision, we construct a synthetic data engine that renders clean views of 3D assets and synthesises composite degradations. On the synthetic benchmark, the purifier improves image fidelity and downstream 3D geometry in only 2.3s on average, reducing TRELLIS.2 mesh distance by 61.5% relative to degraded inputs. VLM evaluation and human preferences on real photographs further support identity preservation and degradation correction. More demos and code are available at https://supra-3d.github.io/gate3dgen.

### 🤖 AI 总结

**一句话总结**：Single-image 3D generation has achieved high fidelity on curated benchmarks, yet degrades sharply on real-world images with uneven illumination, blur, and occlusions. Purifying such inputs requires de...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Gate3DGen, Pre-processing, Model, Selectively, Purifies, Real-World, Images

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31649v1) | [下载PDF](https://arxiv.org/pdf/2610.31649v1.pdf)

---

## [14. OmniRay: Camera-Agnostic Monocular 3D Reconstruction with Composite Ray Fields](https://arxiv.org/abs/2610.31645v1)

**作者**：Namitha Guruprasad, Abhay Yadav, Cheng Peng 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-22

### 📄 论文摘要

Monocular models recover 3D geometry from a single image in one pass, but most assume a pinhole camera and produce distorted geometry on the wide-angle imagery produced by fisheye and panoramic lenses. Camera-aware models remove this assumption by predicting a per-pixel ray field. However, they represent different camera geometries using a single fixed basis to capture both the overall camera projection and its finer variations. We argue that camera geometry can be viewed as having a hierarchy of complexity for representing rays. We present OmniRay, a feed-forward model whose Ray Module is composed of three components: a monotone radial base that captures radially symmetric structure, a spherical-harmonic residual for smooth deviations from it, and a free-form residual for remaining local variation. These components are composed as successive rotations on the sphere, allowing the representation to accommodate diverse camera geometries. Given a single image, OmniRay predicts a ray direction and an up-to-scale radial distance for every pixel, from which a 3D point cloud is recovered without needing camera information at inference time. Extensive experiments across different camera configurations demonstrate that OmniRay establishes a new state-of-the-art in camera-agnostic monocular 3D reconstruction.

### 🤖 AI 总结

**一句话总结**：Monocular models recover 3D geometry from a single image in one pass, but most assume a pinhole camera and produce distorted geometry on the wide-angle imagery produced by fisheye and panoramic lenses...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, OmniRay, Camera-Agnostic, Monocular, Reconstruction, Composite, Ray, Fields

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31645v1) | [下载PDF](https://arxiv.org/pdf/2610.31645v1.pdf)

---

## [15. GigaBench: Benchmarking Learnable Representations for Gigapixel Image Compression and Super-Resolution](https://arxiv.org/abs/2610.31644v1)

**作者**：Matteo Fusconi, Alex Costanzino, Pierluigi Zama Ramirez 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-22

### 📄 论文摘要

Learnable Representations (LRs) can fit parametric families of functions to diverse kinds of signals. These emergent neural-native data formats are gathering interest in the scientific community due to their compactness, resolution-agnosticism and amenability to direct neural processing. On the other hand, gigapixel images are becoming increasingly widespread across a variety of scientific, cultural, and industrial domains. In this paper, we present GigaBench, the first benchmark and experimental evaluation focused on deploying LRs with gigapixel imagery. GigaBench includes images collected, acquired, and synthetically rendered across diverse domains, and addresses image compression and super-resolution. We adapt a representative set of LRs, spanning Implicit, Hybrid, and Explicit methods, so as to operate reliably at the gigapixel scale on consumer hardware. Through systematic evaluation across reconstruction quality, model size, compression and inference times, we identify consistent trends across methods and suggest actionable guidance for future investigation.

### 🤖 AI 总结

**一句话总结**：Learnable Representations (LRs) can fit parametric families of functions to diverse kinds of signals. These emergent neural-native data formats are gathering interest in the scientific community due t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GigaBench, Benchmarking, Learnable, Representations, Gigapixel, Image, Compression, Super-Resolution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31644v1) | [下载PDF](https://arxiv.org/pdf/2610.31644v1.pdf)

---

## [16. UniVOE: A Removal-Driven Framework for Interaction-Aware Universal Video Object Editing](https://arxiv.org/abs/2610.31641v1)

**作者**：Shuzhou Yang, Lanqing Guo, Lingen Li 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-22

### 📄 论文摘要

Video object removal and injection are reciprocal editing operations between object-present and object-absent video states, yet they differ substantially in training difficulty. Removal can be effectively bootstrapped from video inpainting and further adapted to erase object-related interaction effects. Injection, however, requires large-scale paired supervision to model object appearance, dynamics, and scene-dependent effects, while perfectly aligned real-world pairs are difficult to collect and synthetic data lacks sufficient realism and diversity. To address this challenge, we present UniVOE, a removal-driven framework for training both video object removal and injection models. We first train an effect-aware remover by transferring video inpainting priors and finetuning on object-present/object-absent pairs. The trained remover converts real object-present videos into object-absent counterparts, creating large-scale paired supervision for injection. An injection model is trained on these pairs in the reverse direction to recover objects together with their dynamics and interaction effects. Moreover, since pixel-level reconstruction alone cannot adequately capture perceptual realism, we introduce a reward-based post-training method that aligns injection results with human preferences using a proprietary reward model. Experiments against strong open-source and commercial systems demonstrate that UniVOE achieves state-of-the-art performance on both object removal and injection, particularly in challenging interaction-effect cases.

### 🤖 AI 总结

**一句话总结**：Video object removal and injection are reciprocal editing operations between object-present and object-absent video states, yet they differ substantially in training difficulty. Removal can be effecti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UniVOE, Removal-Driven, Framework, Interaction-Aware, Universal, Video, Object, Editing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31641v1) | [下载PDF](https://arxiv.org/pdf/2610.31641v1.pdf)

---

## [17. WorldForge V2: Eliciting Camera-Trajectory Alignment in Video Diffusion Models](https://arxiv.org/abs/2610.31640v1)

**作者**：Chenxi Song, Yanming Yang, Tong Zhao 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-22

### 📄 论文摘要

Video diffusion models have learned rich 3D/4D priors, making them promising for scene generation and video re-rendering. However, their use in spatial tasks is limited by imprecise camera control, spatial and temporal inconsistencies, and entangled camera motion with scene dynamics. Existing approaches, such as task-specific fine-tuning and post-process warping, often introduce visual artifacts, generalize poorly, or incur high computational costs. We propose WorldForge V2 to achieve accurate camera control while preserving the generative capabilities of pretrained video models. We first develop a training-free guidance framework using warped references to iteratively refine generation along a target camera path. Optical-flow analysis identifies motion-related latent channels for selective guidance, helping separate motion control from appearance. A dual-path strategy further compares guided and unguided predictions to correct artifacts from imperfect references. Together, these components guide viewpoint changes while preserving scene appearance and object motion. To reduce refinement costs, v-cache approximates the correction using the preceding denoising prediction, avoiding an additional model evaluation. We further extend motion localization from latent channels to network blocks and introduce Trajectory LoRA, which concentrates adaptation on blocks most responsive to trajectory guidance. A two-stage training strategy teaches these adapters to denoise the states encountered during guided generation, using limited supervision effectively. This enables reliable camera control with very little training data, with a single training scene already supporting generalization to unseen scenes. Quantitative and qualitative evaluations across multiple datasets show that our method achieves state-of-the-art generation quality and trajectory accuracy in camera-controlled video generation.

### 🤖 AI 总结

**一句话总结**：Video diffusion models have learned rich 3D/4D priors, making them promising for scene generation and video re-rendering. However, their use in spatial tasks is limited by imprecise camera control, sp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：V2, Diffusion, WorldForge, Eliciting, Camera-Trajectory, Alignment, Video, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31640v1) | [下载PDF](https://arxiv.org/pdf/2610.31640v1.pdf)

---

## [18. HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction](https://arxiv.org/abs/2610.31635v1)

**作者**：Zunnan Xu, Shangchen Zhou, Yihang Luo 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-22

### 📄 论文摘要

Feed-forward models accurately estimate camera motion and 3D geometry from short video windows. However, computational and memory costs prevent direct inference on sequences containing thousands of frames. Long videos must therefore be processed as overlapping chunks. This division produces independent local reconstructions with inconsistent coordinate frames and duplicate estimates of shared cameras. Achieving global consistency requires propagating constraints from adjacent overlaps and distant revisits across the sequence. This requirement naturally motivates pose graph optimization. However, the choice of graph level creates a trade-off. Chunk-level graphs efficiently resolve scale drift and close large loops. Yet, their rigid transformations cannot correct internal errors or conflicting frame predictions. Conversely, frame-level optimization offers local flexibility, but scaling it globally is computationally expensive and can break metric scale. HiP3R resolves this trade-off using a hierarchical pose graph. HiP3R first optimizes a robust chunk-level $\mathrm{Sim}(3)$ graph to establish the global layout and scale. It then holds this layout fixed and estimates one shared $\mathrm{SE}(3)$ camera per frame, turning overlapping window predictions into a single trajectory. Experiments across multiple benchmarks demonstrate the effectiveness of HiP3R in improving camera trajectories and 3D reconstruction. Our method applies to both chunk-based and streaming backends without additional training or fine-tuning. The codes are available at https://kkakkkka.github.io/HiP3R.

### 🤖 AI 总结

**一句话总结**：Feed-forward models accurately estimate camera motion and 3D geometry from short video windows. However, computational and memory costs prevent direct inference on sequences containing thousands of fr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, HiP3R, Hierarchical, Pose, Graphs, Long-Horizon, Reconstruction, Feed-forward

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31635v1) | [下载PDF](https://arxiv.org/pdf/2610.31635v1.pdf)

---

## [19. Beyond Best-of-$k$: Prior-Consistent DAPS for Ambiguous Nonlinear Inverse Problems](https://arxiv.org/abs/2610.31592v1)

**作者**：Merve Kocabas, Benjamin A. Burns, Andreas Geiger 等 5 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-10-22

### 📄 论文摘要

Diffusion models have become strong priors for solving inverse problems. However, nonlinear inverse problems such as phase retrieval remain challenging when multiple measurement-consistent solutions are distinguishable only by the prior; we call such measurements ambiguous. Existing diffusion-based samplers rely on local approximations during reconstruction. For an ambiguous measurement, these approximations can allow measurement guidance to favor a measurement-consistent mode that is close to a prior-supported mode but is itself not supported by the prior. Evaluation often masks this type of failure by reporting the best-of-$k$ runs, where the best is selected by comparison to the ground truth. We introduce Prior-Consistent DAPS (PC-DAPS), a variant of Decoupled Annealing Posterior Sampling (DAPS) designed to address this failure case by maintaining multiple candidate solutions within a single sampling run. As annealing noise decreases, PC-DAPS prunes and replaces weaker candidates according to their prior consistency, without any ground-truth access. PC-DAPS reduces the incidence of prior-inconsistent samples and improves sample quality on nonlinear inverse problems while preserving sample quality and diversity on linear inverse problems.

### 🤖 AI 总结

**一句话总结**：Diffusion models have become strong priors for solving inverse problems. However, nonlinear inverse problems such as phase retrieval remain challenging when multiple measurement-consistent solutions a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Best-of-$k$, Prior-Consistent, DAPS, Ambiguous, Nonlinear, Inverse, Problems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31592v1) | [下载PDF](https://arxiv.org/pdf/2610.31592v1.pdf)

---

## [20. CellTrack-Bench: Microscopic Cell Tracking Benchmark for Vision-Language Models](https://arxiv.org/abs/2610.31566v1)

**作者**：Ilan Theodoro, Jordão Bragantini, Loïc A. Royer  
**分类**：cs.CV  
**发布时间**：2026-10-22

### 📄 论文摘要

Large language models have shown outstanding performance on text-first tasks such as coding, math, and writing. Recent efforts are shifting models' training to include scientific problems that often live in highly specialized domains beyond text, such as protein structure and biological images. However, in these scenarios, their general-purpose accuracy compared with specialized algorithms remains in question. One such domain is cell tracking, which requires spatiotemporal awareness of cell dynamics. To evaluate this, we created a new benchmark, CellTrack-Bench, which assesses Vision-Language Models' (VLMs) cell-tracking-related performance against specialized trackers. The full benchmark draws from 15 standard cell-tracking datasets across four imaging modalities and comprises 1,537 problems corresponding to 9,041 cell-linking decisions. We selected a hard subset requiring greater reasoning effort by identifying failures shared across distinct algorithmic trackers. With this proposed dataset, we: (i) evaluated different environment harnesses for VLMs; (ii) benchmarked 9 frontier closed-source models and 13 open-weight models; and (iii) provided a detailed analysis of their failure modes. Code, the stored model outputs, and a pipeline that regenerates the benchmark from the source datasets are available at https://github.com/royerlab/celltrack-bench.

### 🤖 AI 总结

**一句话总结**：Large language models have shown outstanding performance on text-first tasks such as coding, math, and writing. Recent efforts are shifting models' training to include scientific problems that often l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CellTrack-Bench, Microscopic, Cell, Tracking, Benchmark, Vision-Language, Models, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31566v1) | [下载PDF](https://arxiv.org/pdf/2610.31566v1.pdf)

---

## cs.LG

## [21. Cost-Aware Abstention for LLM-Based IT Ticket Classification](https://arxiv.org/abs/2610.31657v1)

**作者**：Sachin Gupta  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-10-22

### 📄 论文摘要

Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data. On a public 47,837-ticket, eight-class corpus, we compare four trained non-LLM classifiers with four large language models under zero- and few-shot prompting. Under the illustrative cost model (c_ok, c_triage, c_wrong) = (0, 1, 5), TF-IDF with logistic regression and a threshold of 0.60 selected on calibration reduces test cost from 0.763 to 0.472, a 38.1% relative reduction (paired ratio-bootstrap 95% CI [35.7%, 40.4%]), while lowering wrong routes from 15.3% to 3.5%. Frozen calibration-selected policies also beat both always-route and always-defer on held-out test data in 14 of 16 settings in a post-hoc cost-parameter analysis. The strongest prompted configuration reaches 0.477 accuracy on a stratified 1,000-ticket test subset, versus 0.879 for fine-tuned DistilBERT on the same tickets. Isotonic lowers expected calibration error without reliably improving discrimination: GPT-4o-mini few-shot has one confidence value before and after recalibration and correctness AUROC 0.500. We therefore report correctness AUROC and tie-aware risk-coverage area alongside ECE. At the analytically derived break-even probability 0.80, seven prompted configurations defer all tickets; Haiku few-shot routes only 19/1,000. An LLM-only agreement control and margin/entropy rejection baselines further separate calibration from discrimination. The findings are scoped to this dataset, prompt design, model endpoints, and illustrative costs; the work is an evaluation framework, not a new abstention algorithm or universal deployment certification.

### 🤖 AI 总结

**一句话总结**：Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on cali...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IT, Cost-Aware, Abstention, LLM-Based, Ticket, Classification, Wrong, automatic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31657v1) | [下载PDF](https://arxiv.org/pdf/2610.31657v1.pdf)

---

## [22. METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning](https://arxiv.org/abs/2610.31656v1)

**作者**：Ali Najar, Hosein Hasani, Amir Kooshan Fattah 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-22

### 📄 论文摘要

Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical recurrent agents compress experience into hidden states, while transformer-based agents retrieve from past trajectories at quadratic memory and computation cost. In this work, we propose Memory-Enhanced Test-Time Adaptation (METTA) for meta-reinforcement learning. It decomposes the fast adaptation phase into two temporal scales: a causal neural memory performs fine-grained within-episode adaptation with linear sequence complexity, while compact episode-level summaries support long-range cross-episode task inference without attending over the full interaction history. Moreover, equipping agents with neural memory provides sufficient expressive capacity and test-time training capability, enabling effective adaptation to unseen held-out tasks and task families at meta-test time. On unseen held-out Meta-World ML10/45 test environments, METTA achieves a success rate over $50\%$ while maintaining a low training budget and short wall-clock time. On long-context sparse-reward PointMaze tasks, it outperforms transformer-based baselines by exhibiting more structured exploration behavior. These results show that METTA provides an efficient path toward more adaptive and scalable long-context meta-RL.

### 🤖 AI 总结

**一句话总结**：Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：METTA, Memory-Enhanced, Test-Time, Adaptation, Meta-Reinforcement, Learning, aims, train

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31656v1) | [下载PDF](https://arxiv.org/pdf/2610.31656v1.pdf)

---

## [23. Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation](https://arxiv.org/abs/2610.31639v1)

**作者**：Gabriele Dominici, Teague McMillan, Fazl Barez 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-22

### 📄 论文摘要

Chain-of-thought (CoT) prompting elicits step-by-step rationales that appear to explain model predictions, but there is no guarantee these steps causally drive the final answer. In standard autoregressive generation, dense attention allows each reasoning step to attend to the full context, enabling the model to derive answers through direct lookup while generating plausible-sounding but post-hoc justifications. We introduce CausalCoT, an inference framework that enforces causal transparency by decomposing problems into a directed acyclic graph of atomic sub-questions, evaluating each node in an isolated context containing only its direct causal parents. This Markovian structure removes attention pathways to non-parent content, making downstream predictions sensitive to local reasoning rather than global context leakage. Across a diverse suite of reasoning benchmarks, CausalCoT preserves competitive predictive performance while improving explanation faithfulness, increasing causal sensitivity of intermediate reasoning steps by an average of 12 and up to 21 percentage points over the strongest baseline. The structured dependency graph additionally enables test-time interventions in which local corrections propagate predictably through downstream reasoning.

### 🤖 AI 总结

**一句话总结**：Chain-of-thought (CoT) prompting elicits step-by-step rationales that appear to explain model predictions, but there is no guarantee these steps causally drive the final answer. In standard autoregres...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Causal, Chain, Thought, Mitigating, Attention, Leakage, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31639v1) | [下载PDF](https://arxiv.org/pdf/2610.31639v1.pdf)

---

## [24. Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3](https://arxiv.org/abs/2610.31624v1)

**作者**：Barış Alparslan, Sandy Tanwisuth, Caleb Petterson  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-22

### 📄 论文摘要

Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance to oversight which poses an important threat to the society. For LLMs, reinforcement learning is the first stage of post-training that directly optimizes behavior against an objective; therefore, it is the stage where convergent instrumental behavior, on IC grounds, likely to appear. Does reinforcement learning with verifiable rewards (RLVR) make a model more likely to express instrumental-convergence behavior, or does this depend on the training regime, evaluation frame, and stage of post-training? We study this question as a checkpoint-conditioned behavioral trajectory rather than as a single before/after safety score. Using InstrumentalEval, we evaluate OLMo-3-7B-Think across SFT, DPO, 13 intermediate RLVR checkpoints, and the final RLVR model. The trajectory is nonmonotonic: instrumental rate rises from 25.0% at SFT to 46.1% near RLVR step 200, then falls to 11.8% at the final checkpoint. Paired item-level tests and step-wise regression support the final SFT-to-RLVR reduction. Prompt framing does not explain this pattern: a harmful-prompt indicator combined with other framing effects explains only 15% of within-checkpoint score variance on average, and Iterative Null-space Projection (INLP) removes a detectable framing direction without changing the SFT-to-final-RLVR gap. Together with preliminary 32B endpoint results (35.53% SFT to 22.37% RLVR final), these findings indicate that RLVR does not monotonically increase instrumental behavior in this setting: the rate rises early, then falls below the SFT baseline. The result is specific to this model family and benchmark, and judge agreement is moderate, so absolute rates should be read cautiously.

### 🤖 AI 总结

**一句话总结**：Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Questioning, Instrumental, Convergence, RLVR, Checkpoint, Evidence, OLMo-3, often

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31624v1) | [下载PDF](https://arxiv.org/pdf/2610.31624v1.pdf)

---

## [25. OP-Print: Tracing Membership Imprints in On-Policy Self-Distillation](https://arxiv.org/abs/2610.31616v1)

**作者**：Qi Li, Xinchao Wang  
**分类**：cs.LG, cs.CR  
**发布时间**：2026-10-22

### 📄 论文摘要

On-policy distillation has been widely adopted for alleviating the distribution mismatch of off-policy distillation. Self-distillation further removes the need for an external teacher by using the student's own outputs, enhanced with extra context or demonstrations, as supervision. This teacher-free design makes on-policy self-distillation practical, yet its privacy risks remain largely unexplored. In particular, using two coupled views of the same training example may strengthen its memorization. Motivated by this, we present the first study of membership inference attacks against on-policy self-distillation. We investigate both gray-box and black-box threat models and propose a unified attack framework, named OP-Print. OP-Print builds on our finding that the supervision imprint in on-policy self-distillation is sparse and structured, concentrating on uncertainty-sensitive correction sites rather than across the entire rollout. Exploiting this property, we construct attack signals tailored to the two access levels: in the gray-box setting, OP-Print directly aggregates the privileged teacher-student residual correction along the same rollout; in the black-box setting, it measures restart-based output-basin stability as an observable surrogate for the hidden correction process. Across diverse models and distillation schemes, all baseline attacks remain essentially at random guessing even under gray-box access, whereas OP-Print is broadly validated to be effective in both gray-box and black-box settings.

### 🤖 AI 总结

**一句话总结**：On-policy distillation has been widely adopted for alleviating the distribution mismatch of off-policy distillation. Self-distillation further removes the need for an external teacher by using the stu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OP-Print, Tracing, Membership, Imprints, On-Policy, Self-Distillation, distillation, has

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31616v1) | [下载PDF](https://arxiv.org/pdf/2610.31616v1.pdf)

---

## [26. Efficient and Optimal Learning of Discrete Distributions with Person-Level Privacy](https://arxiv.org/abs/2610.31612v1)

**作者**：Gautam Kamath, Mahbod Majid, Ankur Moitra 等 5 位作者  
**分类**：cs.LG, cs.CR, cs.DS  
**发布时间**：2026-10-22

### 📄 论文摘要

We study learning a discrete distribution under person-level differential privacy in the batched setting. Given $n$ users, each contributing $m$ i.i.d. samples from an unknown distribution $μ$ over $[k]$, we seek an estimate of $μ$ with total-variation error $α$. We give polynomial-time algorithms under both pure and approximate differential privacy. Under pure $(\varepsilon,0)$-DP, we achieve $n = \widetilde O(k/(α^2 m)+k/(α\sqrt{m}\varepsilon)+k/\varepsilon)$, the first polynomial-time pure-DP guarantee matching the information-theoretic optimum up to logarithmic factors. Under approximate $(\varepsilon,δ)$-DP, we achieve $n = \widetilde O(k/(α^2 m)+k/(α\sqrt{m}\varepsilon)+k+\log(1/δ)/\varepsilon)$. At $δ=2^{-Θ(k)}$, this is $\widetilde O(k)$ for fixed $α,\varepsilon,m$ and failure probability. Our algorithms use a new degree-6 sum-of-squares estimator for learning from untrusted batches. Its key ingredient is a trace-bounded diagonal majorizer for the difference between the empirical covariance of the repaired batch averages and the multinomial covariance predicted by their mean. We prove that clean data admit this certificate through semidefinite-programming duality and a new application of the stronger symmetric form of Grothendieck's inequality due to Friedland and Lim. The certificate preserves the mean-dependent variance of multinomial batch averages, yielding the near-optimal robust rate $O(η\sqrt{\log(1/η)/m})$ and providing the score required by the privacy reduction. We also prove a statistical query lower bound ruling out a uniformly smaller order of error under fixed polynomial SQ resource bounds.

### 🤖 AI 总结

**一句话总结**：We study learning a discrete distribution under person-level differential privacy in the batched setting. Given $n$ users, each contributing $m$ i.i.d. samples from an unknown distribution $μ$ over $[...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Efficient, Optimal, Learning, Discrete, Distributions, Person-Level, Privacy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31612v1) | [下载PDF](https://arxiv.org/pdf/2610.31612v1.pdf)

---

## [27. CRANE: Post-Hoc Counterfactual Retrieval for Multimodal Classifiers](https://arxiv.org/abs/2610.31594v1)

**作者**：Franco Rugolon, Ioanna Miliou, Panagiotis Papapetrou  
**分类**：cs.LG  
**发布时间**：2026-10-22

### 📄 论文摘要

Counterfactual explanation methods have been introduced for unimodal settings, with dedicated frameworks for tabular, timeseries, text, and image data, yet no post-hoc method has been designed for classifiers that learn from multimodal inputs. Existing explainability methods for multimodal classifiers apply modality-specific attribution independently to each input, which fails to yield coherent explanations and does not transfer to arbitrary pre-trained multimodal architectures. To address these shortcomings, we present CRANE (Counterfactual Retrieval via Agnostic Nearest-neighbour Explanations), the first post-hoc, model-agnostic framework for nearest-neighbour multimodal counterfactual generation that retrieves real training examples from the target class as candidate explanations, ensuring plausibility by construction. Across four heterogeneous datasets and three fusion strategies, we show that Multimodal Consensus Retrieval (MC-R), which intersects per-modality neighbour sets to identify instances jointly close to the query in every modality, emerges as the strongest multimodal strategy, achieving the best or joint-best outcome on three of four datasets while grounding every explanation in the joint training distribution. Unimodal strategies remain competitive when a single modality dominates the decision boundary.

### 🤖 AI 总结

**一句话总结**：Counterfactual explanation methods have been introduced for unimodal settings, with dedicated frameworks for tabular, timeseries, text, and image data, yet no post-hoc method has been designed for cla...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CRANE, Post-Hoc, Counterfactual, Retrieval, Multimodal, Classifiers, explanation, methods

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31594v1) | [下载PDF](https://arxiv.org/pdf/2610.31594v1.pdf)

---

## [28. Action Learning for Scientific Simulations](https://arxiv.org/abs/2610.31585v1)

**作者**：Sarah Liaw, Yuanqi Du, Yilun Du  
**分类**：cs.LG  
**发布时间**：2026-10-22

### 📄 论文摘要

Understanding and controlling how systems evolve is central to science and engineering, where many problems require reasoning about complete trajectories. Existing approaches typically learn local dynamics or generate trajectories, but objectives constructed from individual transitions can miss dependencies across time, while generative models do not necessarily provide a tractable objective for evaluating and optimizing arbitrary paths. We study $\textit{action learning}$, the problem of recovering a stochastic action from trajectory observations, yielding a common objective for reasoning about dynamical systems. We introduce $\textbf{LEAP}$ ($\textbf{L}$earned $\textbf{E}$nergy on $\textbf{A}$ction $\textbf{P}$aths), which anchors the unknown action to a tractable reference process and learns the remaining correction by comparing observed trajectories with reference trajectories. This construction yields a differentiable objective on path space that can capture both local dynamical structure and nonadditive dependencies across time. Once learned, the same action can be flexibly reused for path ranking and inference, mechanism steering, constrained optimization and sampling. Across stochastic physical systems, many-body orbital dynamics and molecular simulations, LEAP recovers underlying dynamics, captures dependencies across time and enables transfer across inference objectives and physical conditions. We show that $\textit{action learning}$ is a promising framework for turning trajectory observations into reusable objectives for scientific inference and control.

### 🤖 AI 总结

**一句话总结**：Understanding and controlling how systems evolve is central to science and engineering, where many problems require reasoning about complete trajectories. Existing approaches typically learn local dyn...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Action, Learning, Scientific, Simulations, Understanding, controlling, how, systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31585v1) | [下载PDF](https://arxiv.org/pdf/2610.31585v1.pdf)

---

## [29. When to Follow the Teacher: Advantage-Based On-Policy Distillation](https://arxiv.org/abs/2610.31563v1)

**作者**：Mahdi Sabbaghi, George Pappas, Hamed Hassani 等 4 位作者  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-10-22

### 📄 论文摘要

Online Policy Distillation (OPD) often outperforms offline methods such as Supervised Fine-Tuning (SFT) by training on trajectories sampled directly from the student. However, standard OPD trains the student to follow the teacher at every state of the trajectory, assuming that teacher guidance is always beneficial. We instead distinguish between what the teacher prefers and what actually helps the current student succeed. We introduce Advantage-Based On-Policy Distillation (AOPD), which weights teacher actions by their counterfactual advantage under the student. Teacher actions that improve the student's expected outcome are reinforced, while those that do not are downweighted.   Directly computing these advantages requires trying alternative teacher actions at each step and running new rollouts from each. Instead, we show that the AOPD objective can be estimated using only standard student rollouts and their terminal rewards. Our estimator uses teacher importance weights on the student-sampled actions to provide unbiased advantage-weighted supervision, without any additional rollouts or reward evaluations. This allows AOPD to focus teacher supervision on actions that help the current student while preserving the rollout efficiency of standard OPD. Experiments on math, coding, and Medqa show gains over distillation and RL baselines in both external-teacher and self-distillation settings.

### 🤖 AI 总结

**一句话总结**：Online Policy Distillation (OPD) often outperforms offline methods such as Supervised Fine-Tuning (SFT) by training on trajectories sampled directly from the student. However, standard OPD trains the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Follow, Teacher, Advantage-Based, On-Policy, Distillation, Online, Policy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31563v1) | [下载PDF](https://arxiv.org/pdf/2610.31563v1.pdf)

---

## [30. Fine-Grained Analysis of Catastrophic Forgetting in Continual Learning via Algorithmic Stability](https://arxiv.org/abs/2610.31551v1)

**作者**：Guodong Zheng, Yan Sun, Peng Wang 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-22

### 📄 论文摘要

Understanding catastrophic forgetting, in which learning new tasks degrades performance on previously learned tasks, remains a fundamental challenge in continual learning (CL). Existing theoretical analyses often rely on specific model or task structures and offer limited insight into how iterative optimization affects forgetting. To address this gap, we develop an algorithmic stability framework for expected population forgetting under SGD without prescribing a particular model architecture. Specifically, we decompose forgetting into intra-task and cross-task generalization gaps and empirical forgetting. To bound the generalization gaps, we track how a sample perturbation affects updates within a task and propagates through subsequent tasks. We consider constant, intra-task decaying, and continuously decaying learning-rate schedules. Comparing the two decaying schedules allows us to characterize how restarting learning-rate decay at task boundaries affects the propagation of historical sample perturbations. For empirical forgetting, we derive bounds for all three schedules by retaining cumulative gradient alignment along the optimization trajectory, without requiring convexity. Combining these results yields upper bounds on expected forgetting that capture the effects of training set size, the number of updates per task, the total number of tasks, learning-rate schedules, and cumulative gradient alignment. Finally, we conduct experiments on Split CIFAR-100 and Split MiniImageNet to examine the empirical implications of our theoretical findings.

### 🤖 AI 总结

**一句话总结**：Understanding catastrophic forgetting, in which learning new tasks degrades performance on previously learned tasks, remains a fundamental challenge in continual learning (CL). Existing theoretical an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Fine-Grained, Analysis, Catastrophic, Forgetting, Continual, Learning, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.31551v1) | [下载PDF](https://arxiv.org/pdf/2610.31551v1.pdf)

---

