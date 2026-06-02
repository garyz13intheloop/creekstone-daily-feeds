# arXiv AI 论文日报 | 2026-06-02

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (16 篇)
- [cs.AI](#csAI) (3 篇)
- [cs.LG](#csLG) (4 篇)
- [cs.CL](#csCL) (7 篇)

---

## cs.AI

## [1. ClinEnv: An Interactive Multi-Stage Long Horizon EHR Environment for Agents](https://arxiv.org/abs/2606.02568v1)

**作者**：Yuxing Lu, Yushuhong Lin, Wenqi Shi 等 7 位作者  
**分类**：cs.AI, cs.CL, cs.ET, cs.MA  
**发布时间**：2026-06-01

### 📄 论文摘要

Clinical practice is not the selection of an answer from enumerated options: a physician gathers heterogeneous information incrementally and commits to sequential, irreversible decisions under uncertainty. Static benchmarks cannot probe and existing interactive medical benchmarks each compromise on at least one of them. We present ClinEnv, an interactive benchmark that evaluates LLMs as attending physicians over real inpatient admissions under a paradigm we term Longitudinal Inpatient Simulation. Each case is automatically constructed into an ordered sequence of decision stages; at every stage the model must actively query four specialized agents before committing to medications, procedures, and diagnoses. ClinEnv scores both what the model decides, through deterministic ontology-grounded matching, and how it gathers information. Across seven models, the strongest reaches only 0.31 decision F1, and outcome quality is sharply decoupled from process quality. Difficulty concentrates in management decisions and later stages, where models recover discharge diagnoses far more reliably than management actions (0.51 vs. 0.17 F1) and continue to issue redundant queries as cases progress. ClinEnv makes this information-acquisition gap, invisible to outcome-only evaluation, directly measurable.

### 🤖 AI 总结

**一句话总结**：Clinical practice is not the selection of an answer from enumerated options: a physician gathers heterogeneous information incrementally and commits to sequential, irreversible decisions under uncerta...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, ClinEnv, Interactive, Multi-Stage, Long, Horizon, EHR, Environment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02568v1) | [下载PDF](https://arxiv.org/pdf/2606.02568v1.pdf)

---

## [2. Tracking the Behavioral Trajectories of Adapting Agents](https://arxiv.org/abs/2606.02536v1)

**作者**：Jonah Leshin, Manish Shah, Ian Timmis  
**分类**：cs.AI  
**发布时间**：2026-06-01

### 📄 论文摘要

Text files such as skill files, memory files, and behavioral configuration files play a central role in defining how modern agents act. Through edits by humans or the agents themselves, these files may evolve over time, directly steering the agent's behavior in future interactions. We present a methodology and framework for measuring agent $traits$ by defining traits as directions in the embedding space of a text embedding model. We train a linear model on labeled "before" versus "after" skill file diffs to learn a trait vector, then score arbitrary skill edits by projecting their embedding diffs onto this vector. Evaluated on 68 labeled skill diff pairs for the trait of propensity to seek sensitive data, our method achieves 91.2% sign classification accuracy and a Spearman rank correlation of $ρ= 0.82$ under leave-one-out cross-validation. We build this trait evaluation into a broader agent-to-agent protocol that enables one agent to evaluate another's skill file updates through a trusted intermediary.

### 🤖 AI 总结

**一句话总结**：Text files such as skill files, memory files, and behavioral configuration files play a central role in defining how modern agents act. Through edits by humans or the agents themselves, these files ma...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, Tracking, Behavioral, Trajectories, Adapting, Text, files

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02536v1) | [下载PDF](https://arxiv.org/pdf/2606.02536v1.pdf)

---

## [3. Bridging the Last Mile of Time Series Forecasting with LLM Agents](https://arxiv.org/abs/2606.02497v1)

**作者**：Yuhua Liao, Zetian Wang, Qiangqiang Nie 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-01

### 📄 论文摘要

Time series forecasting has advanced rapidly, especially with the emergence of foundation models that show strong zero-shot performance on numerical extrapolation. However, in real-world forecasting settings, a statistically plausible baseline is rarely the final forecast used in practice. Before a forecast becomes decision-ready, it often needs to be revised using weakly structured business context such as holiday effects, campaign plans, external events, historical analogs, and expert feedback. This practical stage remains underexplored in the forecasting literature. In this paper, we formulate this stage as the \textbf{last-mile forecasting} problem and present an LLM-agent framework that sits on top of a forecasting backbone. Our system maintains a unified forecast workspace, invokes tools to retrieve contextual evidence, and converts reasoning trajectories into explicit forecast revision actions under structural safety constraints. It also supports long-horizon forecasting through map-reduce-style decomposition and post-hoc reflection through a memory bank. The resulting system is designed to be controllable and auditable. Through real-world case studies, we show how LLM agents can bridge the gap between statistical prediction and business-ready forecasting.

### 🤖 AI 总结

**一句话总结**：Time series forecasting has advanced rapidly, especially with the emergence of foundation models that show strong zero-shot performance on numerical extrapolation. However, in real-world forecasting s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Bridging, Last, Mile, Time, Series, Forecasting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02497v1) | [下载PDF](https://arxiv.org/pdf/2606.02497v1.pdf)

---

## cs.CL

## [4. From Layers to Submodules: Rethinking Granularity in Replacement-Based LLM Compression](https://arxiv.org/abs/2606.02559v1)

**作者**：Elia Cunegatti, Marcus Vukojevic, Erik Nielsen 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-01

### 📄 论文摘要

Post-training compression of Large Language Models (LLMs) removes entire architectural components, either deleting them or replacing them with fitted modules. Existing replacement-based methods share two design constraints: full-layer granularity and contiguous selection. We argue that this is overly restrictive: in fact, redundancy in pretrained transformers is not confined to contiguous regions, nor does it evenly distribute between Attention and FeedForward outputs, implying that different strategies best approximate different submodule types and that removable components need not cluster within contiguous depth ranges. Based on this intuition, we introduce SubFit (Submodule-level Fitted residual replacement), which compresses LLMs at the submodule level: Attention and FeedForward submodules are selected non-contiguously, and each receives its own lightweight fitted residual bypass. SubFit operates post-training and requires only calibration data. Across ten LLMs (five base, five instruction-tuned), five sparsity levels from 12.5% to 37.5%, and four replacement-based baselines, SubFit achieves the best aggregate perplexity-accuracy trade-off across the evaluated sparsity levels, with larger gains under aggressive compression. At 25% sparsity, it retains 84.6% of dense downstream accuracy and incurs 2.42x perplexity degradation, against 81.6% and 4.34x for the strongest baselines, while delivering measurable inference speedup and KV-cache savings. Code is available at https://github.com/eliacunegatti/SubFit.

### 🤖 AI 总结

**一句话总结**：Post-training compression of Large Language Models (LLMs) removes entire architectural components, either deleting them or replacing them with fitted modules. Existing replacement-based methods share ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Layers, Submodules, Rethinking, Granularity, Replacement-Based, Compression, Post-training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02559v1) | [下载PDF](https://arxiv.org/pdf/2606.02559v1.pdf)

---

## [5. Transferable Self-Harm Surveillance from Emergency Department Triage Notes Using an Evidence-Augmented Machine Learning Approach](https://arxiv.org/abs/2606.02545v1)

**作者**：Liuliu Chen, Gowri Rajaram, Eleanor Bailey 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-01

### 📄 论文摘要

Self-harm is a major public health concern, but current surveillance relying on hospital presentations is inadequate due to the low sensitivity of diagnostic codes. Emergency Department (ED) triage notes, recorded at the initial point of contact, provide a succinct summary of presentations and an opportunity to identify self-harm. We developed a three-stage approach, augmenting traditional machine learning with large language model-based screening and evidence extraction to detect self-harm in ED triage notes. We assessed model transferability across three Australian hospitals. Our approach showed AUPRCs of 0.887 +/- 0.016 and 0.884 +/- 0.012 during internal and external validation. Prospectively, it achieved AUPRC of 0.881 +/- 0.008 at the development site, and 0.879 +/- 0.012 and 0.816 +/- 0.015 at two external sites without site-specific retraining. A key advantage of the approach is that it enables identification of the primary self-harm method with an accuracy of 95%, supporting more granular surveillance beyond binary classification.

### 🤖 AI 总结

**一句话总结**：Self-harm is a major public health concern, but current surveillance relying on hospital presentations is inadequate due to the low sensitivity of diagnostic codes. Emergency Department (ED) triage no...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Transferable, Self-Harm, Surveillance, Emergency, Department, Triage, Notes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02545v1) | [下载PDF](https://arxiv.org/pdf/2606.02545v1.pdf)

---

## [6. SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction](https://arxiv.org/abs/2606.02540v1)

**作者**：Yuting Ning, Zhehao Zhang, Yash Kumar Lal 等 11 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-01

### 📄 论文摘要

Agent skills occupy a privileged position in the agent workflow, as agents are expected to implicitly follow and execute them, rendering third-party skills a vulnerable attack surface. Existing studies have revealed unsafe agent behaviors induced by skill-based attacks, but they primarily evaluate poisoned skills within a single task execution and enumerate harms through ad-hoc risk lists. To bridge these gaps, we introduce SkillHarm, a benchmark of skill-based attacks across the skill-use lifecycle, paired with a systematic taxonomy of skill-relevant risks. SkillHarm evaluates two attack scenarios: Fixed-Payload Poisoning (FPP), where a fixed poisoned skill package directly compromises any task session that invokes it, and Self-Mutating Poisoning (SMP), where an initially benign execution silently mutates persistent skill content, deferring harm until a subsequent reuse. It further defines 12 risk types based on the agent workflow component targeted by the harm: data pipelines, system environments, and agent autonomy. To instantiate these attacks at scale, we build AutoSkillHarm, an automated construction pipeline with coding agents driven by natural-language harnesses. The resulting benchmark contains 879 attack samples across 71 skills. Experiments show that current agents remain vulnerable with attack success rates up to 86.3% in FPP and 69.3% in SMP. Our analysis further reveals a latent risk: many apparent attack failures stem from the agent failing to engage with the poisoned file rather than genuine resistance, and current defenses still fail to reliably mitigate the threat.

### 🤖 AI 总结

**一句话总结**：Agent skills occupy a privileged position in the agent workflow, as agents are expected to implicitly follow and execute them, rendering third-party skills a vulnerable attack surface. Existing studie...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SkillHarm, Lifecycle-Aware, Skill-Based, Attacks, via, Automated, Construction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02540v1) | [下载PDF](https://arxiv.org/pdf/2606.02540v1.pdf)

---

## [7. FigSIM: A Dataset for Fine-grained Suicide Severity and Figurative Language in Suicide Memes](https://arxiv.org/abs/2606.02523v1)

**作者**：Liuliu Chen, Elise R. Carrotte, Brian E. Chapman 等 5 位作者  
**分类**：cs.CL, cs.CV, cs.CY  
**发布时间**：2026-06-01

### 📄 论文摘要

Suicide memes are memes used to express suicide-related thoughts or comment on suicide-related issues. Suicide memes are increasingly common on social media, yet remain poorly understood and potentially harmful. There is an urgent need to better understand their characteristics and to develop appropriate content moderation strategies that limits users' exposure to potentially harmful content. Currently, the absence of annotated datasets of suicide memes remains a key barrier to developing and evaluating automated moderation approaches. In this paper, we introduce FigSIM, the first dataset designed for fine-grained analysis of suicide memes. The dataset consists of 1049 memes, each annotated for (1) fine-grained suicide severity levels, (2) figurative phenomena (e.g., metaphors), and (3) suicide-related content (e.g., suicide method depiction). We benchmark 16 unimodal and multimodal models across three tasks: figurative language, suicide severity, and suicide-related content detection. Overall, FigSIM demonstrates that suicide memes pose unique challenges for both modeling and content moderation. Analysis revealed biases, such as underprediction of higher suicide severity levels, especially for figurative memes. The dataset (including splits used for analyses) is publicly available. Content Warning: This paper contains suicide-related content that may be triggering.

### 🤖 AI 总结

**一句话总结**：Suicide memes are memes used to express suicide-related thoughts or comment on suicide-related issues. Suicide memes are increasingly common on social media, yet remain poorly understood and potential...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FigSIM, Dataset, Fine-grained, Suicide, Severity, Figurative, Language, Memes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02523v1) | [下载PDF](https://arxiv.org/pdf/2606.02523v1.pdf)

---

## [8. When Rating Scales Fall Short: LLM-Assisted Discovery of ADHD Signals in Turkish Teacher Narratives](https://arxiv.org/abs/2606.02509v1)

**作者**：Baris Karacan, Irem Aktar Songur, Ahmet Ozaslan 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-01

### 📄 论文摘要

Attention Deficit Hyperactivity Disorder (ADHD) is one of the most common neurodevelopmental disorders in childhood, and its diagnosis relies on assessments combining clinician judgment with standardized rating scales and reports from parents and teachers. While structured instruments such as the Conners' Teacher Rating Scale-Revised Short Form (CTRS-R:S) quantify ADHD-related behaviors, teachers also provide open-ended narratives that may contain complementary signals not captured by structured assessments. However, it remains unclear to what extent teacher narratives encode signals overlooked by rating scales. In this study, we analyze de-identified Turkish teacher evaluation forms collected during clinical ADHD assessments, including both CTRS-R:S scores and open-ended teacher narratives. We compare predictive signals from structured scores and narrative text and identify cases where structured assessments fail to clearly distinguish ADHD from non-ADHD students while narrative-based models capture distinct behavioral patterns. Notably, these cases show minimal overlap with those missed by the narrative model, suggesting that structured and narrative information encode complementary signals. To interpret these differences, we apply a large language model (LLM)-assisted theme discovery pipeline that reveals distinct attention, behavioral, and family-related patterns, highlighting the potential of natural language processing (NLP) to uncover clinically relevant signals from teacher narratives and to complement traditional ADHD screening tools.

### 🤖 AI 总结

**一句话总结**：Attention Deficit Hyperactivity Disorder (ADHD) is one of the most common neurodevelopmental disorders in childhood, and its diagnosis relies on assessments combining clinician judgment with standardi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, When, Rating, Scales, Fall, Short, LLM-Assisted, Discovery

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02509v1) | [下载PDF](https://arxiv.org/pdf/2606.02509v1.pdf)

---

## [9. CRAM: Centroid-Routing and Adaptive MoE for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2606.02502v1)

**作者**：Jun-Tao Tang, Zhen-Hao Xie, Yu-Cheng Shi 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-01

### 📄 论文摘要

Multimodal Large Language Models (MLLMs) unify heterogeneous vision-language tasks under a shared generative framework via instruction tuning, yet real-world deployment demands continuous capability expansion, making Multimodal Continual Instruction Tuning (MCIT) essential. Existing methods either update all tasks with a shared parameter set or allocate dedicated modules for each new task. Shared updates force heterogeneous tasks to compete, causing forgetting of learned capabilities. Conversely, isolated expansion prevents interference but severely limits parameter efficiency over long task streams. To address this dilemma, we propose CRAM. Specifically, by isolating task-specific patterns into independent modules, CRAM mitigates catastrophic forgetting across tasks. To further boost parameter efficiency, we utilize adaptive-rank instantiation to identify the capability gap between existing expert capability and new task demands, and dynamically allocate only the necessary parameters. To ensure stable reuse among tasks, centroid-guided routing recognizes and activates existing experts' capabilities, while an orthogonality penalty confines new updates to task-specific directions, preventing re-learning general capability. Extensive experiments across diverse benchmarks consistently demonstrate its superiority over existing methods.

### 🤖 AI 总结

**一句话总结**：Multimodal Large Language Models (MLLMs) unify heterogeneous vision-language tasks under a shared generative framework via instruction tuning, yet real-world deployment demands continuous capability e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CRAM, Centroid-Routing, Adaptive, MoE, Multimodal, Continual, Instruction, Tuning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02502v1) | [下载PDF](https://arxiv.org/pdf/2606.02502v1.pdf)

---

## [10. Not What, But How: A Communicative Audit of LLM Response Framing](https://arxiv.org/abs/2606.02493v1)

**作者**：Siddhesh Milind Pawar, Sarah Masud, Haneul Yoo 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-01

### 📄 论文摘要

Large language models (LLMs) are being increasingly used to answer subjective, information-seeking questions, where users are sensitive to how responses are communicated, not just whether the answers are correct. Existing LLM evaluations for subjective cultural queries largely focus on factual correctness, ignoring how the response is framed. To this end, we introduce FRANZ, an automated FRAmework for respoNse characteriZation to conduct communicative audit of LLM responses along four dimensions: cultural positioning, use of generalizing language, anthropomorphic cues, and adherence to conversational maxims. To enable this evaluation, we contribute SQUARE - a corpus of 376k subjective questions sourced from 57 subreddits, and mapped to 7 countries and 19 question categories. We demonstrate FRANZ's applicability by scoring responses from three open-weight LLMs. We observe that LLMs show statistically significant differences in the frequency with which they employ each response characteristic. Unlike single-dimensional audits, FRANZ reveals that insider positioning and anthropomorphism are positively coupled, with the degree of coupling varying by country, providing a diagnostic lens for identifying framing divergences.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are being increasingly used to answer subjective, information-seeking questions, where users are sensitive to how responses are communicated, not just whether the answers ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Not, What, But, How, Communicative, Audit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02493v1) | [下载PDF](https://arxiv.org/pdf/2606.02493v1.pdf)

---

## cs.CV

## [11. Thinking in Blender: Staged Executable Inverse Graphics with Vision-Language Models](https://arxiv.org/abs/2606.02580v1)

**作者**：Guangzhao He, Rundong Luo, Wei-Chiu Ma 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-01

### 📄 论文摘要

Inverse graphics is a longstanding and highly underconstrained problem that seeks to reconstruct images as editable 3D scenes which can be rendered, relit, and manipulated. In this work, we investigate whether pretrained vision-language models (VLMs) can perform executable inverse graphics directly from a single image by reconstructing a scene as an editable Blender program, without relying on specialized 2D or 3D foundation models, differentiable rendering, or multi-view supervision. We introduce Staged Executable Inverse Graphics (SEIG), an agentic framework that reconstructs a 3D scene from a single image by progressively refining scene factors including geometry, materials, composition, and lighting directly in executable Blender code space. We evaluate our framework across diverse scenes using a range of reconstruction metrics spanning pixel-level, perceptual, and semantic fidelity. Our experiments show that staged reconstruction substantially improves reconstruction fidelity, highlighting the importance of task decomposition for executable inverse graphics with general-purpose VLMs. Finally, we showcase various downstream applications enabled by the reconstructed editable Blender scenes.

### 🤖 AI 总结

**一句话总结**：Inverse graphics is a longstanding and highly underconstrained problem that seeks to reconstruct images as editable 3D scenes which can be rendered, relit, and manipulated. In this work, we investigat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Thinking, Blender, Staged, Executable, Inverse, Graphics, Vision-Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02580v1) | [下载PDF](https://arxiv.org/pdf/2606.02580v1.pdf)

---

## [12. Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling](https://arxiv.org/abs/2606.02578v1)

**作者**：Seojeong Park, Jiho Choi, Junyong Kang 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-01

### 📄 论文摘要

Recent multimodal large language models have demonstrated strong reasoning ability, yet their reliability as automated evaluators remains limited by a critical weakness: when visual evidence conflicts with textual cues, MLLM judges tend to reward plausible narratives over perceptually correct answers. We identify and systematically analyze this phenomenon, which we term Perceptual Judgment Bias. Through controlled visual perturbations, existing multimodal judges frequently anchor on the response text instead of their own visual perception, leading to inconsistent and non-verifiable evaluations. To address this issue, we introduce the Perceptually Perturbed Judgment Dataset, which constructs minimally edited counterfactual responses that isolate perceptual errors and enable verifiable supervision. Building on this dataset, we develop a unified training framework that combines a structured GRPO-based reward with a batch-ranking objective, achieving coherent global ordering without explicit pairwise labels. Experiments across diverse MLLM-as-a-Judge benchmarks show that our approach substantially improves perceptual fidelity, ranking coherence, and alignment with human evaluation. Our results establish a scalable and generalizable pathway for training multimodal judges that are perceptually grounded, interpretable, and robust to visual-reasoning conflicts.

### 🤖 AI 总结

**一句话总结**：Recent multimodal large language models have demonstrated strong reasoning ability, yet their reliability as automated evaluators remains limited by a critical weakness: when visual evidence conflicts...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mitigating, Perceptual, Judgment, Bias, Multimodal, LLM-as-a-Judge, via, Perturbation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02578v1) | [下载PDF](https://arxiv.org/pdf/2606.02578v1.pdf)

---

## [13. ProtoAda: Prototype-Guided Adaptive Adapter Expansion and Geometric Consolidation for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2606.02576v1)

**作者**：Yu-Cheng Shi, Zhen-Hao Xie, Jun-Tao Tang 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-06-01

### 📄 论文摘要

Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, but real-world deployment requires them to continually acquire new vision-language capabilities, making Multimodal Continual Instruction Tuning (MCIT) essential. To reduce inter-task interference and promote collaboration, recent methods often employ sparse architectures like Mixture of LoRA Experts with image-text similarity routing. However, tasks with distinct response structures could share highly similar visual-linguistic semantics and thus be wrongly routed to the same expert; image-text similarity alone is insufficient for reliable task assignment. For example, an expert in a grounding task requiring coordinate prediction may be biased toward producing short textual answers after learning semantically similar VQA tasks. This format-blind task assignment integrates heterogeneous response types into shared parameters, inducing gradient interference and ineffective expert collaboration. To address this problem, we propose ProtoAda, a prototype-guided adaptive tuning framework. ProtoAda introduces format-aware task prototypes to align task assignment and routing with both task semantics and output structure, and further consolidates format-compatible updates in a geometry-aware manner to effectively reuse and progressively refine existing parameters. Extensive experiments on multiple benchmarks demonstrate that ProtoAda achieves superior performance, especially on tasks whose answer structures are easily corrupted by sequential tuning.

### 🤖 AI 总结

**一句话总结**：Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, but real-world deployment requires them to continually acquire new vision-language capabilities, making ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ProtoAda, Prototype-Guided, Adaptive, Adapter, Expansion, Geometric, Consolidation, Multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02576v1) | [下载PDF](https://arxiv.org/pdf/2606.02576v1.pdf)

---

## [14. VISReg: Variance-Invariance-Sketching Regularization for JEPA training](https://arxiv.org/abs/2606.02572v1)

**作者**：Haiyu Wu, Randall Balestriero, Morgan Levine  
**分类**：cs.CV  
**发布时间**：2026-06-01

### 📄 论文摘要

Self-supervised learning methods prevent embedding collapse via modeling heuristics or explicit regularization of the embedding space. Among the latter, VICReg decomposes regularization into variance and covariance objectives, offering flexibility and interpretability. However, covariance captures only second-order statistics -- encouraging decorrelation but failing to enforce the full distributional shape needed for stable training. Sketching-based methods such as SIGReg address this by aligning embeddings to an isotropic Gaussian, but lack flexibility and suffer from vanishing gradients under collapse. We propose Variance-Invariance-Sketching Regularization (VISReg), which replaces covariance with a Sliced-Wasserstein-based sketching objective that enforces full distributional shape, while retaining a variance term for scale control. By decoupling scale and shape, VISReg combines VICReg's flexibility with the distributional rigor of sketching methods, providing robust gradients even under collapse. We show that VISReg scales linearly, outperforms existing regularization on low-quality datasets, and is resilient to long-tailed and low-rank regimes. Pre-trained on ImageNet-1K, VISReg achieves state-of-the-art performance on out-of-distribution datasets. Pre-trained on ImageNet-22K, it matches DINOv2's OOD performance despite the latter using 10x more data (LVD-142M). Project and code: https://haiyuwu.github.io/visreg.

### 🤖 AI 总结

**一句话总结**：Self-supervised learning methods prevent embedding collapse via modeling heuristics or explicit regularization of the embedding space. Among the latter, VICReg decomposes regularization into variance ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VISReg, Regularization, JEPA, training, Self-supervised, learning, methods, prevent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02572v1) | [下载PDF](https://arxiv.org/pdf/2606.02572v1.pdf)

---

## [15. Policy-based Foveated Imaging and Perception](https://arxiv.org/abs/2606.02565v1)

**作者**：Howard Xiao, Jan Ackermann, Boyang Deng 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-01

### 📄 论文摘要

Ultra-high-resolution image sensors offer the potential to capture fine spatial details critical for many visual perception tasks, but acquiring and processing all pixels at full resolution is often infeasible under realistic bandwidth, latency, and power constraints. Existing approaches address this challenge through acquisition strategies such as spatial or temporal downsampling, which irrevocably discard information before task relevance can be assessed. In this work, we introduce a real-time, predictive, and task-aware foveated imaging system that operates directly at image acquisition time. Leveraging emerging dual-stream sensor architectures, our method dynamically allocates limited pixel bandwidth to task-relevant regions of interest while maintaining a low-resolution global context. We formulate foveated acquisition as a sensor attention policy-learning problem, in which past observations guide actions that determine future measurements, closing the perception-acquisition loop. Through extensive simulation across multiple perception tasks, we demonstrate that our approach achieves high task performance under strict pixel budgets and significantly outperforms relevant baselines operating at the same bandwidth. We further validate our system on a 200-megapixel dual-stream sensor, capturing real-world videos under realistic bandwidth and latency constraints, demonstrating the practical feasibility of task-driven, acquisition-time foveated imaging.

### 🤖 AI 总结

**一句话总结**：Ultra-high-resolution image sensors offer the potential to capture fine spatial details critical for many visual perception tasks, but acquiring and processing all pixels at full resolution is often i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Policy-based, Foveated, Imaging, Perception, Ultra-high-resolution, image, sensors, offer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02565v1) | [下载PDF](https://arxiv.org/pdf/2606.02565v1.pdf)

---

## [16. VLMs are Good Teachers for Video Reasoning via Adaptive Test-Time Optimization](https://arxiv.org/abs/2606.02564v1)

**作者**：Junhao Cheng, Liang Hou, Tianxiong Zhong 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-01

### 📄 论文摘要

The recent "Reasoning with Video" paradigm utilizes Video Generation Models (VGMs) to generate temporally coherent visual trajectories to complete reasoning tasks. Although state-of-the-art VGMs excel at visual quality, they often struggle to understand and follow task-specific rules, leading to logical failures across diverse reasoning scenarios. Existing efforts try to utilize Vision-Language Models (VLMs) as problem pre-solvers to produce or refine textual guidance for the VGM. However, textual descriptions fail to capture intricate spatiotemporal details, and VGMs often struggle to faithfully execute fine-grained or long-tail instructions even with a valid plan. While VLMs struggle as solvers, they possess strong perception capabilities to evaluate process-constraint satisfaction and final-goal achievement. Leveraging this strength, we introduce a paradigm shift that transitions the role of VLMs to "teachers". Specifically, a VLM teacher extracts task-specific rules to formulate differentiable rewards, guiding a VGM Reasoner via test-time online optimization of a lightweight LoRA module. This strategy enables adaptive test-time optimization and extends the reasoning capabilities beyond the VGM's intrinsic boundaries. Evaluations on symbolic (VBVR-Bench) and general-purpose (RULER-Bench) video reasoning benchmarks show that the proposed method yields a 16.7-point average performance gain, outperforming the VLM-as-Solver paradigm (+0.4 points) and Best-of-N scaling (+2.2 points) by a large margin at comparable test-time cost. These findings reveal that integrating VLMs as test-time teachers offers a promising paradigm for achieving generalizable video reasoning. Project Page: https://VLM-as-Teacher.github.io/

### 🤖 AI 总结

**一句话总结**：The recent "Reasoning with Video" paradigm utilizes Video Generation Models (VGMs) to generate temporally coherent visual trajectories to complete reasoning tasks. Although state-of-the-art VGMs excel...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VLMs, Good, Teachers, Video, Reasoning, via, Adaptive, Test-Time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02564v1) | [下载PDF](https://arxiv.org/pdf/2606.02564v1.pdf)

---

## [17. LongLive-RAG: A General Retrieval-Augmented Framework for Long Video Generation](https://arxiv.org/abs/2606.02553v1)

**作者**：Qixin Hu, Shuai Yang, Wei Huang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-01

### 📄 论文摘要

Autoregressive (AR) video diffusion enables variable-length synthesis, but long-horizon generation often suffers from accumulated errors and identity drift. For efficiency, existing methods commonly adopt sliding-window attention during generation. This creates an irreversible generation trajectory: once the active window accumulates appearance errors, subsequent generations can only condition on this degraded trajectory and drift further away. We address this limitation by formulating long video generation as a retrieval-augmented generation (RAG) problem. Rather than relying solely on the recent window, we treat previously generated latents as a dynamic, searchable history. We propose LongLive-RAG, a general retrieval framework for AR video generation. At each new block, LongLive-RAG uses a query embedding to retrieve relevant historical latents. This lightweight retrieval step adds only a small overhead relative to generation and lets the generator condition on non-local context instead of only the recent window. To make retrieval more discriminative, we introduce the Window Temporal Delta Loss that suppresses redundant local similarity and encourages embeddings to capture meaningful temporal changes. Together, these components help reduce error accumulation caused by sliding-window attention. Experiments across multiple AR backbones and generation lengths show improved long-video quality and the best average VBench-Long rank. To our knowledge, among open-ended AR long video generation methods, LongLive-RAG is the first to formulate self-generated latent history as content-addressable retrieval memory. Code is available at https://github.com/qixinhu11/LongLive-RAG.

### 🤖 AI 总结

**一句话总结**：Autoregressive (AR) video diffusion enables variable-length synthesis, but long-horizon generation often suffers from accumulated errors and identity drift. For efficiency, existing methods commonly a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LongLive-RAG, General, Retrieval-Augmented, Framework, Long, Video, Generation, Autoregressive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02553v1) | [下载PDF](https://arxiv.org/pdf/2606.02553v1.pdf)

---

## [18. Modeling Depth Ambiguity: A Mixture-Density Representation for Flying-Point-Free Depth Estimation](https://arxiv.org/abs/2606.02552v1)

**作者**：Siyuan Bian, Congrong Xu, Jun Gao  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-01

### 📄 论文摘要

Despite advances in depth estimation, flying points remain a persistent failure mode: near object boundaries, depth estimators often predict spurious 3D points in the empty space between foreground and background surfaces. We trace this artifact to a standard modeling choice: assigning each pixel a single depth hypothesis. At boundaries, a pixel can straddle a foreground and a background surface, so its true depth is ambiguous between the two. A model that predicts a single depth cannot keep both possibilities, so training instead pulls the prediction toward an intermediate depth that lies on neither surface. We address this with MDA, a mixture-density representation that lets the model predict multiple depth hypotheses and their associated probabilities for each pixel. Near boundaries, different hypotheses can align with different surfaces, and the decoded depth is selected from one of these hypotheses rather than placed in the empty space between them. Across different backbones, MDA substantially improves boundary reconstruction and largely removes flying-point artifacts even under severe input blur, while adding negligible runtime overhead. The same mixture-density framework naturally extends to transparent objects, where it predicts multiple depth layers at transparent pixels, and to sky regions, where a dedicated component separates the unbounded sky from finite-depth regions, producing flying-point-free skylines. Project Page: https://biansy000.github.io/mda-site/.

### 🤖 AI 总结

**一句话总结**：Despite advances in depth estimation, flying points remain a persistent failure mode: near object boundaries, depth estimators often predict spurious 3D points in the empty space between foreground an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Modeling, Depth, Ambiguity, Mixture-Density, Representation, Flying-Point-Free, Estimation, Despite

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02552v1) | [下载PDF](https://arxiv.org/pdf/2606.02552v1.pdf)

---

## [19. LL-Bench: Rethinking Low-Level Vision Evaluation in the Era of Large-Scale Generative Models](https://arxiv.org/abs/2606.02535v1)

**作者**：Lu Liu, Huiyu Duan, Chenxin Zhu 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-01

### 📄 论文摘要

Large-scale generative models have demonstrated remarkable capabilities across image generation and editing tasks. However, their performance in low-level vision tasks, which require pixel-wise control, remains insufficiently studied. To address this gap, we introduce \textbf{LL-Bench}, a comprehensive \textbf{Benchmark} for evaluating the capabilities of large-scale generative models on \textbf{L}ow-\textbf{L}evel vision tasks. The benchmark comprises 2,469 real-world degraded images covering 16 low-level degradation tasks, and 28,919 restored images produced by 10 state-of-the-art large-scale generative models and 21 conventional restoration models, which are annotated with 152,020 expert-level pairwise human preferences and 28,334 quality scores. Built upon LL-Bench, we present a systematic diagnosis that reveals the performance boundaries and unique failure modes of large-scale generative models across diverse low-level vision tasks, compared with conventional representative restoration approaches. Moreover, we investigate the effectiveness of current quality evaluation metrics on LL-Bench, which exhibit significant discrepancy with human ratings. To better align restored-image quality assessment with human preferences, we further propose \textbf{LL-Score}, an MLLM-based evaluator that captures both restoration quality and hallucination existence. Extensive experiments demonstrate that LL-score not only outperforms existing image quality assessment metrics, but also serves as a promising reward model for training generative models on low-level vision tasks.

### 🤖 AI 总结

**一句话总结**：Large-scale generative models have demonstrated remarkable capabilities across image generation and editing tasks. However, their performance in low-level vision tasks, which require pixel-wise contro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LL-Bench, Rethinking, Low-Level, Vision, Evaluation, Era, Large-Scale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02535v1) | [下载PDF](https://arxiv.org/pdf/2606.02535v1.pdf)

---

## [20. Improving Combined Detection and Classification of TEM Defects via Mask-Conditioned Latent Diffusion Augmentation](https://arxiv.org/abs/2606.02532v1)

**作者**：Ni Li, Nuohao Liu, Ryan Jacobs 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-01

### 📄 论文摘要

Analyzing microstructural defects in transmission electron microscopy (TEM) images, particularly in irradiated metal alloys, is often limited by the availability of high-quality, labeled data. To address this, we introduce a generative data augmentation approach using a mask-conditioned latent diffusion model (LDM) for synthesizing realistic TEM images with controllable, automatically labeled multi-class defect masks. Without requiring manual annotations for generation, our method enables the creation of synthetic image-mask pairs by sampling distributions learned from experimental masks. These generated data were used to augment small experimental datasets of varying sizes (10, 50, and 100 labeled experimental images) to train a Mask Regional Convolutional Neural Network (R-CNN) model for defect detection and classification. Our results show that generative augmentation yields small overall model performance improvements, with up to a 0.02 gain in the harmonic mean of detection and classification F1 scores. However, we also find that the relative contributions to detection and classification improvement depend on the specific train/test data split. These findings highlight the potential of targeted generative models to enhance deep learning performance in data-scarce microscopy-based image quantification tasks.

### 🤖 AI 总结

**一句话总结**：Analyzing microstructural defects in transmission electron microscopy (TEM) images, particularly in irradiated metal alloys, is often limited by the availability of high-quality, labeled data. To addr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Improving, Combined, Detection, Classification, TEM, Defects, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02532v1) | [下载PDF](https://arxiv.org/pdf/2606.02532v1.pdf)

---

## [21. Why Not Hyperparameter-Friendly Optimisation? A Monotonic Adaptive Norm Rescaling Approach For Long-Tailed Recognition](https://arxiv.org/abs/2606.02526v1)

**作者**：Shuo Zhang, Chenqi Li, Tingting Zhu  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-01

### 📄 论文摘要

Long-tailed recognition poses a significant challenge for deep learning. The two-stage decoupling paradigm, which separates representation learning from classifier retraining, offers a promising solution. During the classifier retraining stage, adaptive norm rescaling is a popular technique. It adjusts the per-class weight norms via parameter regularization, which inevitably introduces hyperparameters. However, many studies report that long-tailed recognition is sensitive to these hyperparameters, as their setup significantly impacts performance. In this paper, we first provide a class-conditional distribution perspective to support norm rescaling methods. Furthermore, we propose a simple but effective approach called Self-Adaptive Monotonic Normalization (SAMN). SAMN avoids the need for parameter regularization. It directly enforces monotonicity on per-class weight norms using the Pool Adjacent Violators Algorithm, making the method hyperparameter-friendly. SAMN is a universal strategy that integrates seamlessly with other methods for enhanced performance. Experiments on benchmark datasets demonstrate that our method significantly boosts long-tailed recognition performance, often achieving state-of-the-art results.

### 🤖 AI 总结

**一句话总结**：Long-tailed recognition poses a significant challenge for deep learning. The two-stage decoupling paradigm, which separates representation learning from classifier retraining, offers a promising solut...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Why, Not, Hyperparameter-Friendly, Optimisation?, Monotonic, Adaptive, Norm, Rescaling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02526v1) | [下载PDF](https://arxiv.org/pdf/2606.02526v1.pdf)

---

## [22. ToolFG: Towards Well-Grounded Fine-Grained Image Classification](https://arxiv.org/abs/2606.02518v1)

**作者**：Yu Xue, Haoxuan Qu, Zhuoling Li 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-01

### 📄 论文摘要

Fine-grained image classification (FGIC) has broad applications and has attracted significant research attention. In this paper, we explore a novel paradigm for solving FGIC by proposing \textbf{ToolFG}, the first tool-integrated MLLM-based framework tailored to FGIC. ToolFG enables MLLMs to autonomously and flexibly use external tools during the reasoning process, actively interact with images, and collect verifiable visual cues for distinguishing highly similar categories in a more \textit{reliable} and \textit{well-grounded} manner. To equip the model with such tool-use ability, we design a novel \textbf{MCTS-guided tool-use knowledge distillation mechanism}, which effectively mines tool-use- and FGIC-relevant knowledge from advanced proprietary MLLMs for model training. Furthermore, we propose a \textbf{model-tool co-evolution mechanism} that jointly refines the toolset and the model's tool-use policy, driving them toward a mutually adapted and FGIC-specialized state. Extensive experiments demonstrate the effectiveness of our framework.

### 🤖 AI 总结

**一句话总结**：Fine-grained image classification (FGIC) has broad applications and has attracted significant research attention. In this paper, we explore a novel paradigm for solving FGIC by proposing \textbf{ToolF...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ToolFG, Towards, Well-Grounded, Fine-Grained, Image, Classification, FGIC, has

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02518v1) | [下载PDF](https://arxiv.org/pdf/2606.02518v1.pdf)

---

## [23. Not All Points Are Equal: Uncertainty-Aware 4D LiDAR Scene Synthesis](https://arxiv.org/abs/2606.02510v1)

**作者**：Xiang Xu, Alan Liang, Youquan Liu 等 8 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-06-01

### 📄 论文摘要

Constructing faithful 4D worlds from LiDAR-acquired sequences is crucial for embodied AI, yet current generative frameworks apply uniform modeling capacity across all spatial regions. This ignores that perceptual difficulty varies dramatically within a single scan: distant surfaces, occluded boundaries, and small-scale objects carry far higher uncertainty than well-observed structures. We present U4D, a new framework that explicitly leverages spatial uncertainty to guide LiDAR scene generation in a "hard-to-easy" schedule. U4D derives per-point uncertainty maps via Shannon Entropy from a pretrained segmentor, then applies an unconditional diffusion stage to synthesize high-entropy areas with precise geometry, followed by a conditional completion stage that fills in the remaining regions using these structures as priors. A MoST (Mixture of Spatio-Temporal) block further maintains cross-frame coherence by dynamically balancing spatial detail and temporal continuity. Extensive experiments on nuScenes and SemanticKITTI demonstrate state-of-the-art scene fidelity, temporal consistency, and downstream performance.

### 🤖 AI 总结

**一句话总结**：Constructing faithful 4D worlds from LiDAR-acquired sequences is crucial for embodied AI, yet current generative frameworks apply uniform modeling capacity across all spatial regions. This ignores tha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, Not, All, Points, Equal, Uncertainty-Aware, LiDAR, Scene

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02510v1) | [下载PDF](https://arxiv.org/pdf/2606.02510v1.pdf)

---

## [24. Question-Aware Evidence Ledgers for Video Relational Reasoning](https://arxiv.org/abs/2606.02506v1)

**作者**：Yilin Ou, Mengshi Qi, Huadong Ma  
**分类**：cs.CV  
**发布时间**：2026-06-01

### 📄 论文摘要

The VRR-QA challenge evaluates visual relational reasoning in videos, where answers often depend on implicit spatial relations, event boundaries, target identity, and dialogue context rather than a single salient frame. We present a test-time reasoning pipeline built around a strong GPT-5.5 video QA solver and a set of question-aware evidence ledgers. The initial solver answers each question from a uniform video representation, while routed ledgers are prompted to make the required targets, count units, reference frames, and temporal or spatial scope explicit for counting, spatial, endpoint, viewpoint, and dialogue reasoning. External tools such as open-vocabulary detection, depth cues, pair crops, ASR, and scene-graph ledgers are used only as evidence sources. A conservative gate keeps the current answer unless independent evidence uniquely supports a different option. The final evidence-gated pipeline achieves 92.95% overall accuracy and 93.79% macro accuracy on the challenge test split.

### 🤖 AI 总结

**一句话总结**：The VRR-QA challenge evaluates visual relational reasoning in videos, where answers often depend on implicit spatial relations, event boundaries, target identity, and dialogue context rather than a si...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Question-Aware, Evidence, Ledgers, Video, Relational, Reasoning, VRR-QA, challenge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02506v1) | [下载PDF](https://arxiv.org/pdf/2606.02506v1.pdf)

---

## [25. GloResNet: A lightweight 3D CNN with global topological features for preterm brain injury prediction](https://arxiv.org/abs/2606.02498v1)

**作者**：Boyu Yuan, Jiamiao Lu, Weichuan Zhang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-01

### 📄 论文摘要

This study introduces an automated deep learning framework for predicting brain injury (BI) in preterm infants from T2-weighted MRI (dHCP dataset). We propose GloResNet, a lightweight 3D CNN based on ResNet-10, pretrained on MedicalNet to address data scarcity. A global manifold mapping strategy first resamples each 3D volume to 128x128x128 and then applies subject-wise z-score intensity normalization, thereby preserving global topology while standardizing appearance. Training integrates mixup, class weighting, and test-time augmentation for robustness. In 5-fold cross-validation, GloResNet achieved 75.18% average accuracy (peak 81.82%), with specificity 0.81 and sensitivity 0.76. Results demonstrate that a topology-aware lightweight CNN has the capability to effectively predict neonatal BI, offering a non-invasive screening tool. The source code of this paper can be obtained from the GitHub repository: https://github.com/ICL-SUST/GloResNet-Preterm-Brain

### 🤖 AI 总结

**一句话总结**：This study introduces an automated deep learning framework for predicting brain injury (BI) in preterm infants from T2-weighted MRI (dHCP dataset). We propose GloResNet, a lightweight 3D CNN based on ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, GloResNet, lightweight, CNN, global, topological, features, preterm

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02498v1) | [下载PDF](https://arxiv.org/pdf/2606.02498v1.pdf)

---

## [26. MORPHOS: Autoregressive 4D Generation with Temporal Structured Latents](https://arxiv.org/abs/2606.02491v1)

**作者**：Minkyung Kwon, Jinhyeok Choi, Youngjin Shin 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-01

### 📄 论文摘要

We present MORPHOS, a novel autoregressive framework that generates dynamic 3D assets from videos across diverse representations, including meshes, 3D Gaussians, and radiance fields. Existing methods are typically limited to a single representation, struggle to model topological changes, or fail to maintain temporal consistency over long videos. To address these limitations, we introduce the Temporal Structured Latents (T-SLAT), a unified 4D representation that jointly encodes geometry and appearance along the temporal dimension. Leveraging T-SLAT, MORPHOS autoregressively generates dynamic 3D assets via causal attention, conditioning each frame on its preceding history to ensure temporal consistency while handling evolving topologies. We also propose a temporal-structural augmentation to mitigate error accumulation in autoregressive generation. MORPHOS achieves state-of-the-art performance in appearance and competitive results in geometry across multiple benchmarks, demonstrating superior generalization across various representations and robustness in long-horizon generation.

### 🤖 AI 总结

**一句话总结**：We present MORPHOS, a novel autoregressive framework that generates dynamic 3D assets from videos across diverse representations, including meshes, 3D Gaussians, and radiance fields. Existing methods ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, We, MORPHOS, Autoregressive, Generation, Temporal, Structured, Latents

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02491v1) | [下载PDF](https://arxiv.org/pdf/2606.02491v1.pdf)

---

## cs.LG

## [27. IntraShuffler: A Privacy Preserving Framework for Heterogeneous DP Federated Learning](https://arxiv.org/abs/2606.02563v1)

**作者**：Farhin Farhad Riya, Olivera Kotevska, Jinyuan Stella Sun  
**分类**：cs.LG, cs.CR, cs.DC  
**发布时间**：2026-06-01

### 📄 论文摘要

Heterogeneous Differential Privacy (HDP) in Federated Learning (FL) allows clients to select individual privacy budgets ($\varepsilon_i$) according to institutional policies and data sensitivity. In practice, many HDP-FL systems employ $\varepsilon$-aware server aggregation to improve model utility by re-weighting client updates according to their declared privacy budgets. However, gradient updates in FL retain structural patterns induced by non-independent and identically-distributed (non-IID) data, and these additional signals exposed by $\varepsilon$-aware aggregation create new opportunities for inference by an honest-but-curious server. In this work, we first show that a server equipped with gradient denoising and surrogate modeling can mount a \emph{Privacy Inference Attack} that infers distributional attributes of clients and links updates from the same client across training rounds, measured via surrogate inference accuracy and linkage success, under realistic knowledge constraints.   The Shuffle-Model has been widely studied as a defense against such inference risks by anonymizing update sources, but it is fundamentally incompatible with HDP-FL $\varepsilon$-aware aggregation. To address this challenge, we propose \textbf{IntraShuffler}, a middleware defense framework designed for HDP-FL systems. IntraShuffler introduces a privacy-aware shuffling mechanism that groups clients into privacy-compatible buckets and performs parameter-level shuffling within each bucket to disrupt persistent gradient structure while preserving $\varepsilon$-aware aggregation. Experiments across four different datasets show that IntraShuffler reduces gradient recoverability by over 60% and decreases surrogate inference accuracy from 0.78 to 0.33 while maintaining comparable model utility across multiple FL aggregation rules.

### 🤖 AI 总结

**一句话总结**：Heterogeneous Differential Privacy (HDP) in Federated Learning (FL) allows clients to select individual privacy budgets ($\varepsilon_i$) according to institutional policies and data sensitivity. In p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DP, IntraShuffler, Privacy, Preserving, Framework, Heterogeneous, Federated, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02563v1) | [下载PDF](https://arxiv.org/pdf/2606.02563v1.pdf)

---

## [28. Drifting Preference Optimization for One-Step Generative Models](https://arxiv.org/abs/2606.02521v1)

**作者**：Zhou Jiang, Yandong Wen, Zhen Liu  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-06-01

### 📄 论文摘要

One-step text-to-image generators are attractive for deployment because they generate an image with a single forward pass, but preference finetuning them remains difficult: standard alignment methods often rely on policy likelihoods, denoising trajectories, differentiable reward gradients, or test-time optimization. We propose Drifting Preference Optimization (DrPO), an online preference-finetuning method for deterministic one-step generators. For each prompt, DrPO samples candidates from the current generator, ranks them with a target reward, and uses high- and low-scoring samples to synthesize a feature-space update direction. The update is a non-parametric dipole preference field plus a reference drift estimated from the frozen base generator, and is optimized through a detached feature-space regression target. The target reward is used only for ranking, so DrPO can train with large, black-box, or non-differentiable rewards while inference remains a single generator call. We evaluate DrPO on SD-Turbo and SDXL-Turbo with multiple target rewards and benchmarks, including HPSv3 and GenEval. DrPO improves alignment over reward-gradient-free one-step preference baselines and reduces HPSv3 training computation by $3.51\times$ under the matched effective-batch setting by removing reward-model backpropagation. Initial offline experiments suggest that sample-based gradient synthesis can also be used beyond online reward ranking.

### 🤖 AI 总结

**一句话总结**：One-step text-to-image generators are attractive for deployment because they generate an image with a single forward pass, but preference finetuning them remains difficult: standard alignment methods ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Drifting, Preference, Optimization, One-Step, Generative, Models, text-to-image, generators

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02521v1) | [下载PDF](https://arxiv.org/pdf/2606.02521v1.pdf)

---

## [29. A Biconvex Formulation for Stable Transport of Mixture Models with a Unique Solution](https://arxiv.org/abs/2606.02515v1)

**作者**：Yeganeh Marghi, Kelly Jin, Uygar Sümbül  
**分类**：cs.LG  
**发布时间**：2026-06-01

### 📄 论文摘要

Optimal transport (OT) provides a principled framework for mapping between probability distributions. Despite extensive progress, applying OT to large-scale data remains computationally demanding, and the resulting pointwise transport plans are often difficult to interpret. We introduce Optimal Mixture Transport (OMT), a scalable framework that shifts the transport paradigm from individual samples to mixtures of subpopulations, reformulating the transport problem as a strictly biconvex optimization with a unique global minimizer. We further establish theoretical guarantees on the stability of the OMT map, showing that bounded perturbations of the underlying distributions lead to bounded changes in the transport plan. By formulating subpopulations as exponential-family distributions, OMT decouples computational complexity from the sample size, scaling solely with the number of mixture components. We demonstrate the effectiveness and practicality of OMT on a wide range of synthetic benchmarks and real-world datasets, including image data and large-scale single-cell RNA sequencing measurements.

### 🤖 AI 总结

**一句话总结**：Optimal transport (OT) provides a principled framework for mapping between probability distributions. Despite extensive progress, applying OT to large-scale data remains computationally demanding, and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Biconvex, Formulation, Stable, Transport, Mixture, Models, Unique

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02515v1) | [下载PDF](https://arxiv.org/pdf/2606.02515v1.pdf)

---

## [30. Expressivity of congruence-based architectures for DNNs on positive-definite matrices](https://arxiv.org/abs/2606.02490v1)

**作者**：Antonin Oswald, Estelle Massart  
**分类**：cs.LG  
**发布时间**：2026-06-01

### 📄 论文摘要

This work studies neural architectures for classifying symmetric positive-definite matrices, focusing on congruence-like layers, in which the input matrix is multiplied on the left and right by a (possibly rectangular) weight matrix $W$ and its transpose. Such layers lie at the core of the celebrated SPDNet and have also been employed independently for dimensionality reduction on positive-definite data. We show that the (semi)-orthogonality constraint commonly imposed on $W$ limits the expressivity of these layers: for certain activation functions, the resulting architecture collapses to a one-hidden-layer equivalent. This lack of expressivity follows from a loss of spectral diversity in congruence-like layers for semi-orthogonal $W$ and is a direct consequence of Poincaré's separation theorem. We then examine the choice of the final classifier, comparing several Riemannian classifiers and discussing their compatibility with the feature maps produced by congruence-like layers.

### 🤖 AI 总结

**一句话总结**：This work studies neural architectures for classifying symmetric positive-definite matrices, focusing on congruence-like layers, in which the input matrix is multiplied on the left and right by a (pos...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Expressivity, congruence-based, architectures, DNNs, positive-definite, matrices, work

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.02490v1) | [下载PDF](https://arxiv.org/pdf/2606.02490v1.pdf)

---

