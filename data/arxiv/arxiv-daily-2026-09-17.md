# arXiv AI 论文日报 | 2026-09-17

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (10 篇)
- [cs.CV](#csCV) (7 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. Cognitive Extensions for Dual-Process Language Agents: Memory and Self-Reflection in Interactive Environments](https://arxiv.org/abs/2609.19128v1)

**作者**：João Meneses dos Santos, Arlindo L. Oliveira  
**分类**：cs.AI, cs.LG, cs.MA  
**发布时间**：2026-09-16

### 📄 论文摘要

Language agents remain brittle in interactive environments, where success requires long-horizon state tracking, valid action execution, and recovery from failed steps. We extend SwiftSage, a dual-process agent that combines a fast action proposer with a slower planner, using two modular cognitive extensions: an Adaptive Memory Module (AMM) for salience-gated episodic storage and trigger-driven retrieval, and a Self-Reflection Module (SRM) for bounded execution-time validation and corrective intervention. Both modules are implemented as feature-flagged extensions over the same execution substrate, enabling controlled ablations on ScienceWorld. Across four configurations---baseline, baseline+AMM, baseline+SRM, and the full system---the full system achieves the best mean final score (64.62), success rate (43.17%), and successful-step efficiency (19.33 steps), while SRM is the strongest standalone contributor. The results suggest that execution-time control is the dominant bottleneck in this setting, while episodic memory becomes most useful once the runtime loop is stabilized.

### 🤖 AI 总结

**一句话总结**：Language agents remain brittle in interactive environments, where success requires long-horizon state tracking, valid action execution, and recovery from failed steps. We extend SwiftSage, a dual-proc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Cognitive, Extensions, Dual-Process, Language, Memory, Self-Reflection, Interactive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19128v1) | [下载PDF](https://arxiv.org/pdf/2609.19128v1.pdf)

---

## [2. MUSE: Benchmarking Large Vision-Language Models on Multi-Modal Understanding in Situated Education](https://arxiv.org/abs/2609.19088v1)

**作者**：Luyao Zhu, Xun Wei Yee, Wei Li 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.CV  
**发布时间**：2026-09-16

### 📄 论文摘要

Large vision-language models have achieved remarkable progress in multi-modal understanding, yet their capabilities in educational settings remain insufficiently evaluated. In AI-assisted language learning, models must interpret artistic imagery, understand its semantic, affective, and cultural content, and reason about visual context to support meaningful interaction. However, existing benchmarks primarily focus on real-world images or domain-specific educational reasoning, providing limited coverage of artistic educational content. To address this gap, we introduce MUSE, a benchmark for evaluating large vision-language models on artistic image understanding in situated educational applications. MUSE decouples image annotation from question generation, enabling diverse tasks with controllable difficulty while reducing annotation effort. It comprises twelve tasks spanning visual perception, semantic and affective interpretation, culture understanding, and compositional reasoning, together with diverse artistic images deliberately curated to center Singaporean and Southeast Asian multicultural contexts alongside Western art traditions, covering multiple themes and difficulty levels. Evaluation of open-source and proprietary models reveals substantial disparities across capability dimensions, particularly in affective interpretation and compositional reasoning. Our analysis further identifies common failure modes and key challenges for developing trustworthy multi-modal models for education. We hope MUSE will serve as a standardized benchmark for advancing multi-modal understanding in situated educational applications.

### 🤖 AI 总结

**一句话总结**：Large vision-language models have achieved remarkable progress in multi-modal understanding, yet their capabilities in educational settings remain insufficiently evaluated. In AI-assisted language lea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MUSE, Benchmarking, Large, Vision-Language, Models, Multi-Modal, Understanding, Situated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19088v1) | [下载PDF](https://arxiv.org/pdf/2609.19088v1.pdf)

---

## [3. Compositional Policy Violations: When Step-Level Compliance Fails In Agentic AI Workflows](https://arxiv.org/abs/2609.18820v1)

**作者**：Ashwini Kurady, Sri Sai Charith Grandhi, Rajesh Gupta 等 4 位作者  
**分类**：cs.AI, cs.MA  
**发布时间**：2026-09-16

### 📄 论文摘要

Agentic workflows now make consequential decisions in regulated settings, and the governance placed around them is almost entirely step-scoped: input-output classifiers, per turn rails, and span-level evaluators. The policies organizations actually hold, such as referral thresholds, authority limits, and review requirements, are properties of the whole execution rather than of any one step. This mismatch admits a failure mode we call a Compositional Policy Violation (CPV): every individual step passes its own check while the composed execution violates the governing policy. A predicate over a single step cannot evaluate a property that step does not determine, so no improvement in the accuracy of the step-scoped monitors detects this class. We define CPVs as the failure of step-level compliance to compose, and present a taxonomy of four types: Authority Creep, Threshold Laundering, Cumulative Sum Violation, and Context Collapse. We show that the correct repair for each class is dictated by where the guarded quantity mutates. We then introduce a provenance-aware runtime architecture that evaluates policies over complete execution traces, recomputing guarded quantities from raw provenance rather than the pipeline's derived representation.

### 🤖 AI 总结

**一句话总结**：Agentic workflows now make consequential decisions in regulated settings, and the governance placed around them is almost entirely step-scoped: input-output classifiers, per turn rails, and span-level...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Compositional, Policy, Violations, When, Step-Level, Compliance, Fails, Agentic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18820v1) | [下载PDF](https://arxiv.org/pdf/2609.18820v1.pdf)

---

## cs.CL

## [4. A Zeroth-Order Paradigm for LLM Preference Alignment](https://arxiv.org/abs/2609.19144v1)

**作者**：Peter Chen, Xi Chen, Wotao Yin 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-09-16

### 📄 论文摘要

Direct preference alignment methods are widely used to align large language models (LLMs) with human preferences because of their computational and memory efficiency. However, likelihood displacement motivates alternative ways to extract information from preference pairs with small likelihood margins. In this paper, we propose and analyze Comparison-based Preference Optimization (ComPO), a zeroth-order alignment method based on comparison oracles. ComPO extracts directional information from these pairs without directly optimizing a differentiable preference loss on them. We establish a convergence guarantee for its basic offline scheme under smoothness, gradient sparsity, and compatibility between the oracle and a latent objective. We further introduce online ComPO, which retains the offline comparison mechanism and uses unlabeled policy generations for reverse-KL control relative to a reference policy. Following the coverage perspective of preference fine-tuning, we establish a performance guarantee for a basic constrained scheme under local coverage and in-distribution pairwise reward accuracy. Experiments on Mistral, Llama, Gemma-2, Qwen3, and Gemma-3 models demonstrate improvements over existing direct alignment methods, including length-controlled win rates, with pair-level diagnostics providing evidence consistent with mitigating likelihood displacement.

### 🤖 AI 总结

**一句话总结**：Direct preference alignment methods are widely used to align large language models (LLMs) with human preferences because of their computational and memory efficiency. However, likelihood displacement ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Zeroth-Order, Paradigm, Preference, Alignment, Direct, methods, widely

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19144v1) | [下载PDF](https://arxiv.org/pdf/2609.19144v1.pdf)

---

## [5. ScienceIDE: Turning World's Scientific Codebase into Agent Learnable Environments](https://arxiv.org/abs/2609.19134v1)

**作者**：Hejia Geng, Zesen Huang, Haoyang Li 等 45 位作者  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-09-16

### 📄 论文摘要

Scientific code repositories encode decades of human knowledge in executable models, methods, and tools. Yet fragmented toolchains, implicit domain conventions, and specialized correctness criteria make this knowledge difficult to convert into reliable learning experience-a challenge we call the scientific experience bottleneck. We introduce ScienceIDE, infrastructure for turning the world's scientific code into programmable environments for scientific agents. Guided by expert-defined scientific cases and acceptance criteria, agents transform repositories into executable environments that support task generation, execution, and scientific verification. These environments provide a shared foundation for supervised fine-tuning, reinforcement learning, and evaluation. Using verified interaction trajectories, we train PhAI-IDE-72B, PhAI-IDE-9B, and PhAI-IDE-4B. The model family shows gains in held-out scientific-code repair and across selected general-purpose benchmarks in code, reasoning, and knowledge, providing evidence of positive transfer from scientific experience to broader capabilities. ScienceIDE lays the foundation for an integrated workspace for agent learning and scientific practice, making humanity's scientific software a shared substrate for developing scientific intelligence. Code: https://github.com/aitofound/ScienceIDE

### 🤖 AI 总结

**一句话总结**：Scientific code repositories encode decades of human knowledge in executable models, methods, and tools. Yet fragmented toolchains, implicit domain conventions, and specialized correctness criteria ma...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, ScienceIDE, Turning, World's, Scientific, Codebase, Learnable, Environments

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19134v1) | [下载PDF](https://arxiv.org/pdf/2609.19134v1.pdf)

---

## [6. Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations](https://arxiv.org/abs/2609.19101v1)

**作者**：Leon Bergen, Usha Bhalla, Andrew Lee 等 18 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-09-16

### 📄 论文摘要

As models scale, reward hacking becomes more frequent, more sophisticated, and more consequential. Does it leave a telltale signature in model representations? This work analyzes how reward hacking is represented internally in frontier open source LLMs, and how those representations can be used to understand and discover the range of hacking behaviors a model displays. In particular, we find that simple difference of means vectors coherently represent reward hacking in Kimi K3, GLM 5.2, and Qwen 3.8 Max across a variety of behaviors in common evaluations. Despite their simplicity, these vectors are both generalizable and interpretable, and we can use them to reliably detect reward hacking. We first evaluate reward hacking in commonly reported benchmarks like DeepSWE and SWE-bench, finding that models reward hack excessively in these environments; GLM 5.2 hacks in 57.2% of rollouts on DeepSWE and in 73% of rollouts on SWE-bench. Catching these requires monitors; LLM monitors are effective, but expensive detectors. We show that DoM vectors are similarly effective but virtually free, catching 3.1% more hacks in Kimi K3 and 7.9% fewer hacks in GLM 5.2 on DeepSWE at a monitor matched false positive rate. DoM vectors run on the chain-of-thought also predict reward hacks in the model's subsequent actions, meaning we can run them online and catch potential hacks before they occur. Finally, we analyze probe-hits that LLM monitors do not catch and discover other undesirable behaviors, as well as show transfer to finding hacks in non-SWE evaluations. Together, these results provide evidence that simple, white-box methods can be used to scalably study and monitor reward hacking behaviors in frontier open source models

### 🤖 AI 总结

**一句话总结**：As models scale, reward hacking becomes more frequent, more sophisticated, and more consequential. Does it leave a telltale signature in model representations? This work analyzes how reward hacking is...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Monitoring, Discovering, Reward, Hacking, Internal, Representations, during

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19101v1) | [下载PDF](https://arxiv.org/pdf/2609.19101v1.pdf)

---

## [7. Reporting Practice Matters: The Impact of Reference Choice on Chest X-ray Report Evaluation](https://arxiv.org/abs/2609.19093v1)

**作者**：Daniel P. Jeong, Charles Q. Li, Hossein Hosseiny 等 8 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-16

### 📄 论文摘要

Radiologists follow heterogeneous reporting practices. Two radiologists examining the same image and identifying the same clinical findings might nevertheless compose superficially distinct reports, varying in terminology, shorthand, formatting, and level of detail. These variations in reporting norms represent an under-appreciated obstacle in efforts to evaluate AI-based radiology report generation (RRG) models, where machine-generated reports are typically assessed based on their concordance with human-generated references. In this paper, we quantify the sensitivity of established evaluation metrics to variations in reporting practices, revealing impacts large enough to alter the rankings of models. We introduce a radiologist-informed taxonomy of variations in radiology reporting practice and a method (ReRef) that rewrites reference reports along the axes of our taxonomy while preserving clinical interpretation. For instance, when comparing the performance of nine RRG models on MIMIC-CXR using RadCliQ-v1, condensing the discussion of normal findings in the reference reports causes Libra to drop from first to second place while CheXOne rises from third to first. Our results suggest that many current metrics fail to decouple clinical interpretation from conformity to reporting practices and that choosing the ``right'' references that accurately reflect the desired reporting practices can be important in practice. To support future research, we release MIMIC-CXR-Ext-ReRef, a radiologist-validated dataset of 120 (original, alternative) reference report pairs derived from MIMIC-CXR.

### 🤖 AI 总结

**一句话总结**：Radiologists follow heterogeneous reporting practices. Two radiologists examining the same image and identifying the same clinical findings might nevertheless compose superficially distinct reports, v...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Reporting, Practice, Matters, Impact, Reference, Choice, Chest

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19093v1) | [下载PDF](https://arxiv.org/pdf/2609.19093v1.pdf)

---

## [8. Beyond Outcomes: Dual-View Relational Learning for Efficient Agent Benchmarking](https://arxiv.org/abs/2609.18909v1)

**作者**：Xinshuai Guo, Junjie Wu, Dolly Deng 等 7 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-16

### 📄 论文摘要

Agent benchmarks are substantially more costly to evaluate than conventional LLM benchmarks. Benchmark compression is therefore a natural solution, yet existing methods primarily model redundancy in task--model final-score distributions, which is important in agentic evaluation. To address this limitation, we analyze large-scale trajectories and identify six complementary process signals that are systematically associated with final agent performance. To disentangle agent performance redundancy from a complete perspective, we propose DualViewEval, an agent benchmark compression method that jointly exploits outcome and process relations to learn an exact-size miniset and predict the full-benchmark scores. Across five agent benchmarks and five representative baselines, DualViewEval achieves the best results in all datasets. With only 20 tasks, it achieves $24\times$--$40\times$ compression on APEX-Agents and BFCL, reducing mean absolute error (MAE) by $14.5\%$--$28.2\%$ over the strongest competitors while improving Kendall's $τ$ by up to $7.2\%$ relative to EssenceBench on SWE-bench Verified. The selected minisets further reveal capability differences among different agents, providing compact and diagnostic feedback for efficient agentic model development.

### 🤖 AI 总结

**一句话总结**：Agent benchmarks are substantially more costly to evaluate than conventional LLM benchmarks. Benchmark compression is therefore a natural solution, yet existing methods primarily model redundancy in t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Beyond, Outcomes, Dual-View, Relational, Learning, Efficient, Benchmarking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18909v1) | [下载PDF](https://arxiv.org/pdf/2609.18909v1.pdf)

---

## [9. How Much is a Human Right Worth? ECtHR-NPD: A Benchmark for Predicting Non-Pecuniary Damage Awards](https://arxiv.org/abs/2609.18908v1)

**作者**：Yanyi Pu, Damian A. Gonzalez-Salzberg, Zheng Yuan 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-16

### 📄 论文摘要

Existing legal benchmarks cover diverse tasks, while continuous monetary remedies remain comparatively underexplored. We introduce ECtHR-NPD, to the best of our knowledge, the first benchmark for predicting non-pecuniary damage (NPD) awards at the European Court of Human Rights (ECtHR) from case information when no statutory formula or explicit calculation rule determines the amount. ECtHR-NPD contains 14,575 cases with case-level awards in nominal euros, chronological splits, and a protocol separating target construction from model input. We evaluate a battery of methods, including constant predictors, gradient-boosted trees, retrieval methods, fine-tuned encoder language models (LMs), prompted decoder LMs, and knowledge-augmented agents. Our results show that more sophisticated LM and agentic approaches do not consistently outperform the strongest feature-based baseline. All model families struggle to identify zero awards and to calibrate high-award predictions, with further degradation on the Challenging test view, making ECtHR-NPD a challenging testbed for current state-of-the-art open-weight and proprietary LMs.

### 🤖 AI 总结

**一句话总结**：Existing legal benchmarks cover diverse tasks, while continuous monetary remedies remain comparatively underexplored. We introduce ECtHR-NPD, to the best of our knowledge, the first benchmark for pred...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：How, Much, Human, Right, Worth?, ECtHR-NPD, Benchmark, Predicting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18908v1) | [下载PDF](https://arxiv.org/pdf/2609.18908v1.pdf)

---

## [10. Structured Claim-Level Discourse Representations for Dense Health Narratives](https://arxiv.org/abs/2609.18905v1)

**作者**：Farnoushsadat Nilizadeh, Elham Pourabbas Vafa, Shirin Nilizadeh 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-16

### 📄 论文摘要

Health discourse in social media videos often contains densely entangled claims spanning multiple thematic aspects, stances, evidential frames, and rhetorical functions within short conversational spans. Existing approaches largely rely on coarse topic-level, sentiment-based, or stance-oriented representations that do not adequately capture this structure. Our analysis identifies an average of 13.22 atomic claims per minute, motivating richer claim-level discourse representations. We introduce a structured framework for claim-level discourse analysis in dense health narratives. Our framework models discourse through tuples linking atomic claims with thematic aspects, stance, and multidimensional pragmatic discourse attributes. To support this setting, we construct a benchmark spanning four health domains with 1,191 manually annotated claims from 60 videos. Using this framework, we evaluate automated structured discourse analysis under different discourse context settings. Results show that current LLMs achieve strong performance on thematic categorization and stance prediction, but struggle with high-dimensional pragmatic profiling. We also find that different discourse tasks benefit from different forms of contextual reasoning, suggesting that future systems may require task decomposition and specialized inference strategies.

### 🤖 AI 总结

**一句话总结**：Health discourse in social media videos often contains densely entangled claims spanning multiple thematic aspects, stances, evidential frames, and rhetorical functions within short conversational spa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Structured, Claim-Level, Discourse, Representations, Dense, Health, Narratives, social

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18905v1) | [下载PDF](https://arxiv.org/pdf/2609.18905v1.pdf)

---

## [11. PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning](https://arxiv.org/abs/2609.18861v1)

**作者**：Yu Liu, Zeming Liu, Tianle Zhang 等 9 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-16

### 📄 论文摘要

Adaptive learning systems commonly formulate learning path planning as Exercise-Centric (EC) recommendation, where the next step is inferred from item-level interaction logs. Evaluating goal-oriented guidance additionally requires explicit learner goals and curriculum-scale prerequisites: learners with similar exercise records may need different paths toward their targets. We therefore study Knowledge-Centric (KC) personalized learning path planning, where a planner must reason over learner profiles, mastery states, and prerequisite knowledge structures to decide which textbook, unit, and concept should be studied next. To support this setting, we introduce PersonaPath, a benchmark that pairs 2,000 fine-grained learner personas with a hierarchical knowledge graph of 347 textbooks, 1,751 units, and 4,092 concepts across 77 subjects. We evaluate representative LLMs on PersonaPath. Results show that even the strongest LLM reaches only a 29.5% final pass rate in Basic Education, and that the main bottleneck lies in adaptivity, where no model exceeds 44.7% in tailoring paths to individual learners.

### 🤖 AI 总结

**一句话总结**：Adaptive learning systems commonly formulate learning path planning as Exercise-Centric (EC) recommendation, where the next step is inferred from item-level interaction logs. Evaluating goal-oriented ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PersonaPath, Towards, Knowledge-Centric, Personalized, Learning, Path, Planning, Adaptive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18861v1) | [下载PDF](https://arxiv.org/pdf/2609.18861v1.pdf)

---

## [12. EviGen: Predictive Evidence Scaffolding for Verifiable Clinical Rationale Generation](https://arxiv.org/abs/2609.18852v1)

**作者**：Fengnan Li, Heman Burre, Liwen Sun 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-16

### 📄 论文摘要

Longitudinal electronic health records (EHRs) capture years of patient history across notes, codes, labs, and procedures, and contain evidence needed to reason about likely clinical outcomes. However, comprehensive clinician review of these records is impractical, and LLM-based processing is costly and often unreliable, missing some relevant observations while hallucinating others. We therefore propose EviGen, a three-layer framework for verifiable clinical rationale generation that addresses these challenges. The first layer is a patient-conditioned retriever that uses learnable queries to find evidence predictive of, not just textually relevant to, a clinical outcome and ranks it by prediction attribution scores. The second layer is an LLM generator that consumes this ranked evidence as a scaffold to produce a clinical rationale grounded in the retrieved spans. The third layer is a process-supervised verifier that checks the generated rationale at the reasoning-step level, flagging unreliable claims. Across three medical prediction datasets, EviGen improves prediction performance and rationale faithfulness over full-context LLM and RAG baselines, and is preferred by clinical reviewers in a usability evaluation.

### 🤖 AI 总结

**一句话总结**：Longitudinal electronic health records (EHRs) capture years of patient history across notes, codes, labs, and procedures, and contain evidence needed to reason about likely clinical outcomes. However,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EviGen, Predictive, Evidence, Scaffolding, Verifiable, Clinical, Rationale, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18852v1) | [下载PDF](https://arxiv.org/pdf/2609.18852v1.pdf)

---

## [13. ReFigBench: Benchmarking Scientific Figure Reconstruction as Editable PowerPoint Artifacts](https://arxiv.org/abs/2609.18844v1)

**作者**：Liyang Fan, Chi Wei, Yitai Li 等 11 位作者  
**分类**：cs.CL, cs.CV  
**发布时间**：2026-09-16

### 📄 论文摘要

Multimodal coding agents are expected to turn visual inputs into usable artifacts, and they act through a harness, the layer of tools, context management, and execution environment around the model. Existing evaluations often isolate short tool calls, API traces, or screenshot resemblance, and a low score under these proxies cannot say whether the model saw poorly, planned poorly, or was failed by its harness. We study scientific overview figure reconstruction, an agent task in which a source image must become an editable PowerPoint slide that preserves text, topology, layout, and native document structure. We introduce ReFigBench, a benchmark and evaluation framework built on 1,000 real overview figures retrieved from arXiv papers with full provenance. Coding agents from four model families reconstruct every figure under two workflows, direct code generation and a specialized PPTX workflow, and the strongest model runs inside two commercial harnesses, yielding ten configurations. Evaluation combines deterministic artifact checks, repeated automated scoring by judges from two model families, and blinded human comparisons. Perception remains a bottleneck that iterative rendering only partly repays. Whether workflow effort converts into quality depends on the model together with its harness, since the same model gains from the specialized workflow inside one harness and loses inside the other, and the harness shifts scores even under an identical direct prompt. The specialized workflow erases native connectors in every configuration, human judges still prefer its renderings in most matchups, and even the strongest agent falls short of the rubric ceiling. These results expose the tension between fidelity and editability as the central challenge for practical multimodal document agents.

### 🤖 AI 总结

**一句话总结**：Multimodal coding agents are expected to turn visual inputs into usable artifacts, and they act through a harness, the layer of tools, context management, and execution environment around the model. E...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, ReFigBench, Benchmarking, Scientific, Figure, Reconstruction, Editable, PowerPoint

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18844v1) | [下载PDF](https://arxiv.org/pdf/2609.18844v1.pdf)

---

## cs.CV

## [14. PANORAMA: Panoptic Grounded Captioning via Mask Proposal Selection](https://arxiv.org/abs/2609.19143v1)

**作者**：Sara Pieri, Evangelos Kazakos, Shizhe Chen 等 5 位作者  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-09-16

### 📄 论文摘要

Intelligent systems that act in the world require image understanding that is both comprehensive and spatially grounded. Current vision-language models (VLMs) can generate fluent and detailed image captions, but reliably associating them with image pixels remains challenging. Existing methods that combine dense captioning with pixel-level grounding often produce either incomplete descriptions or inaccurate segmentation masks. We study this problem through panoptic grounded captioning, a task that requires a VLM to describe both foreground objects and background regions while grounding each referring phrase with pixel-level masks. We make three contributions. First, we introduce PanoCaps, a human-annotated benchmark constructed from panoptic segmentation datasets. It provides dense captions with near-complete pixel coverage and image-text alignments at the entity level, supporting both training and evaluation. We further propose a phrase-mask matching protocol and a generalized Panoptic Quality (gPQ) metric that jointly evaluates textual and mask agreement. Second, we formulate phrase grounding as selection from a phrase-conditioned pool of mask proposals and introduce PANORAMA, a VLM that conditions a pretrained segmenter on contextualized phrase representations to obtain candidate masks and learns to select those corresponding to each phrase. Training this interface jointly with caption generation enables PANORAMA to produce high-quality masks while allowing each phrase to refer to a single region or multiple instances. Third, PANORAMA achieves the best overall grounding on PanoCaps and matches or exceeds specialized models across several pixel-level grounding tasks. Experiments show that our method produces precise entity-level segmentations while maintaining detailed, mask-consistent captions. Code, data and models are available at https://www.di.ens.fr/willow/research/panorama/.

### 🤖 AI 总结

**一句话总结**：Intelligent systems that act in the world require image understanding that is both comprehensive and spatially grounded. Current vision-language models (VLMs) can generate fluent and detailed image ca...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PANORAMA, Panoptic, Grounded, Captioning, via, Mask, Proposal, Selection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19143v1) | [下载PDF](https://arxiv.org/pdf/2609.19143v1.pdf)

---

## [15. PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics](https://arxiv.org/abs/2609.19142v1)

**作者**：Bardienus P. Duisterhof, Kaifeng Zhang, Adam Hung 等 8 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-09-16

### 📄 论文摘要

World models endow perceptual systems with the ability to predict how scenes evolve under interaction. They are most beneficial when trained on diverse volumes of data, to instill a rich prior into downstream applications. Existing methods typically require robot action labels to learn action-conditioned 3D dynamics, which excludes web video data from the training pool. We study 3D point track completion as a pre-training objective for learning transferable 3D dynamics without robot data. Given a single RGB-D observation and sparse partial 3D trajectories (tracks), we predict future 3D tracks of all observed points. We show this objective produces a rich 3D dynamics prior, without requiring robot action labels. We contribute a diverse dataset of 2.9 million synthetic frames spanning deformable, articulated, and rigid objects, and use it to train PointZero. We show that a flexible and expressive transformer, PointZero, outperforms prior methods on the same data. We demonstrate the utility of our pre-training objective by post-training PointZero for two downstream applications: (1) action-conditioned 3D dynamics prediction and (2) imitation learning. When fine-tuned to condition on end-effector pose, PointZero outperforms the baselines on the recent PGND 3D dynamics benchmark. When fine-tuned to predict robot actions and 3D tracks, PointZero outperforms or matches the baselines on 6/7 simulated and real-world robot manipulation tasks. We furthermore evaluate training PointZero from scratch to isolate the benefits of our proposed architecture from those of our proposed pre-training objective and dataset. We release the dataset, checkpoints, and full training recipe.

### 🤖 AI 总结

**一句话总结**：World models endow perceptual systems with the ability to predict how scenes evolve under interaction. They are most beneficial when trained on diverse volumes of data, to instill a rich prior into do...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, PointZero, Point, Track, Completion, Learning, Transferable, Dynamics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19142v1) | [下载PDF](https://arxiv.org/pdf/2609.19142v1.pdf)

---

## [16. In-Context Robot Learning with VLM Agents](https://arxiv.org/abs/2609.19138v1)

**作者**：Dongzhou Cheng, Taoran Yi, Ye Fang 等 15 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-09-16

### 📄 论文摘要

Enabling robots to adapt to unfamiliar environments as readily as humans remains a moonshot goal of embodied AI. No finite collection of demonstrations can cover every task and situation a robot will encounter, making the ability to learn from context at deployment essential for generalization. Such in-context learning (ICL), however, remains largely beyond the reach of existing robotic policies. The broad agentic capabilities of commercial vision-language models (VLMs), such as GPT-6 Astra, raise a compelling question: can these models learn from demonstrations, examples, and interaction feedback, then translate that information into executable and verifiable robot behavior from a new initial state without gradient updates or persistent changes to task-specific parameters? We introduce GPT-Policy, a general-agent framework for in-context robot learning. GPT-Policy integrates a context compiler that preserves task-relevant visual transitions, a VLM that proposes robot-tool actions, and a constrained controller that verifies and executes each action and reports its outcome. We evaluate its reliability and limitations through task success and efficiency metrics, matched comparisons across models, and controlled context ablations. In real-robot trials, human video demonstrations improve task completion even without robot action labels, while aligned action references yield further gains on contact-sensitive tasks. These findings position GPT-Policy as a step toward robot adaptation through in-context learning, providing an empirical foundation for translating the general-purpose capabilities of VLMs into physical behavior and clarifying the challenges that must be overcome for reliable deployment.

### 🤖 AI 总结

**一句话总结**：Enabling robots to adapt to unfamiliar environments as readily as humans remains a moonshot goal of embodied AI. No finite collection of demonstrations can cover every task and situation a robot will ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, In-Context, Robot, Learning, VLM, Enabling, robots, adapt

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19138v1) | [下载PDF](https://arxiv.org/pdf/2609.19138v1.pdf)

---

## [17. Adaptive Convolutional Sparse Coding via Information Bottleneck for Robust Visual Signal Representation](https://arxiv.org/abs/2609.19122v1)

**作者**：Meng'en Qin, Yinchen Liu, Mingxuan Cui 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-16

### 📄 论文摘要

Visual signals require compact yet sufficient representations for robust downstream prediction. Convolutional sparse coding (CSC) provides an explicit mechanism for suppressing redundant components while preserving signal content, but its sparsity coefficient is typically fixed and manually selected. We propose an adaptive convolutional sparse coding framework for robust visual signal representation. Specifically, we unfold the CSC optimization with the Fast Iterative Shrinkage-Thresholding Algorithm (FISTA) and treat the sparsity coefficient as a differentiable variable jointly learned with the network parameters. From the information bottleneck perspective, this coefficient controls the trade-off between information retention and compression: the sparsity term promotes compact representations, while the reconstruction term together with task loss preserves task-relevant signal content. We further introduce a label-free post-training strategy that adjusts the compression strength for corrupted inputs with the main network parameters fixed. Experiments on CIFAR and ImageNet demonstrate competitive clean-data recognition and greatly improved robustness under different input perturbations.

### 🤖 AI 总结

**一句话总结**：Visual signals require compact yet sufficient representations for robust downstream prediction. Convolutional sparse coding (CSC) provides an explicit mechanism for suppressing redundant components wh...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Adaptive, Convolutional, Sparse, Coding, via, Information, Bottleneck, Robust

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19122v1) | [下载PDF](https://arxiv.org/pdf/2609.19122v1.pdf)

---

## [18. Track, Articulate, Act: Generating Articulation from Casual Human Videos](https://arxiv.org/abs/2609.19119v1)

**作者**：Jiaming Zhang, Homanga Bharadhwaj  
**分类**：cs.CV  
**发布时间**：2026-09-16

### 📄 论文摘要

Human videos contain rich causal evidence for robot manipulation: they reveal how hand motion induces object motion and produces task-relevant changes in object state. In this work, we study articulated objects such as doors, drawers, cabinets, laptops, ovens, and hinged containers that are ubiquitous in daily life and present unique challenges for embodied interaction. These objects cannot be represented by a single pose; their motion depends on the underlying parts and joints. We introduce a real-to-sim framework that reconstructs a simulation-ready articulated object and hand-object interaction from a casual monocular RGB video, without RGB-D or multi-view input, prior scans, manually specified joints, or robot demonstrations. Our key insight is that dense 3D point tracks provide an embodiment-agnostic articulation cue: points on the fixed link remain approximately stationary, while points on the moving link follow coherent revolute or prismatic motion. Our method segments the links, estimates the joint and its state trajectory, reconstructs an articulated asset, and aligns the recovered 3D hand motion with the object. Central to our approach is a modular recipe that repurposes powerful pretrained models for single-image 3D reconstruction, mesh segmentation, and 3D scene flow, connecting their predictions through explicit geometric reasoning to infer articulation. We use the reconstructed articulated object and the human hand trajectory to replay interactions through contact in MuJoCo. The framework shows how pretrained vision models and explicit motion reasoning can turn casual human videos into articulated object models suitable for downstream embodied interactions. https://track-articulate-act.github.io/

### 🤖 AI 总结

**一句话总结**：Human videos contain rich causal evidence for robot manipulation: they reveal how hand motion induces object motion and produces task-relevant changes in object state. In this work, we study articulat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Track, Articulate, Act, Generating, Articulation, Casual, Human, Videos

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19119v1) | [下载PDF](https://arxiv.org/pdf/2609.19119v1.pdf)

---

## [19. NormLift: From Lifted Features To Semantic Reliability In 3D Gaussian Splatting](https://arxiv.org/abs/2609.18898v1)

**作者**：Yihan Zang, Da Li, Dominik Engel 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-16

### 📄 论文摘要

Training-free weighted aggregation is widely used to lift 2D semantic features onto 3D Gaussians for open-vocabulary scene understanding, yet its theoretical role remains insufficiently understood. Existing analyses typically justify this operation from the rendering side, treating Gaussian features as linearly composable Euclidean variables for reconstructing 2D feature maps. However, this view does not match downstream 3D usage, where each Gaussian is often queried independently in a cosine-based embedding space. We revisit feature lifting from the 3D side and formulate per-Gaussian assignment as a cosine alignment problem on the CLIP unit sphere. Under this objective, the L2-normalized semantic back-projected feature emerges as the closed-form solution, providing a complementary interpretation of the standard lifting rule from the perspective of per-Gaussian semantic assignment. The same formulation further yields a norm decomposition into intra-view and inter-view consistency, suggesting that feature magnitude itself can serve as a semantic reliability signal. Calibrated by effective multi-view support, this reliability score guides a mode-voting refinement that preserves CLIP feature validity by avoiding linear averaging. Experiments on open-vocabulary 3D semantic segmentation show that NormLift is an efficient, training-free framework that achieves strong performance across evaluation protocols.

### 🤖 AI 总结

**一句话总结**：Training-free weighted aggregation is widely used to lift 2D semantic features onto 3D Gaussians for open-vocabulary scene understanding, yet its theoretical role remains insufficiently understood. Ex...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, NormLift, Lifted, Features, Semantic, Reliability, Gaussian, Splatting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18898v1) | [下载PDF](https://arxiv.org/pdf/2609.18898v1.pdf)

---

## [20. Copy What Is Seen, Generate What Is Not: Training-Free Anomaly-Aware Video Restoration](https://arxiv.org/abs/2609.18836v1)

**作者**：Zhida Qu, Shengchao Chen  
**分类**：cs.CV  
**发布时间**：2026-09-16

### 📄 论文摘要

A surveillance system that detects an anomaly often has to repair the footage as well, yet the two tasks are studied in isolation: training-free anomaly detectors stop at a score or a label, while training-free video editing answers to a user prompt rather than to a detector. This paper proposes AVR (Anomaly-aware Video Restoration), which closes that gap with frozen pretrained models alone and generates content only where the clip offers no evidence to copy. Motion evidence first gates open-vocabulary proposals into spatio-temporal masks. A background prior computed from the clip then fills every pixel the anomaly ever uncovers, leaving diffusion to synthesize only what no frame showed, and a frozen verifier decides per clip whether to trust a classical, a prior-anchored, or a background-conditioned restorer. Extensive experiments on three surveillance datasets, under both full-reference anomaly injection and real anomalies, show that AVR leads full-frame fidelity under oracle masks, matches three trained video inpainters inside the edited region, and outperforms a detect-then-generate pipeline on the masks it produces itself, while suppressing both the residual anomaly and the flicker of free diffusion.

### 🤖 AI 总结

**一句话总结**：A surveillance system that detects an anomaly often has to repair the footage as well, yet the two tasks are studied in isolation: training-free anomaly detectors stop at a score or a label, while tra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Copy, What, Seen, Generate, Not, Training-Free, Anomaly-Aware, Video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18836v1) | [下载PDF](https://arxiv.org/pdf/2609.18836v1.pdf)

---

## cs.LG

## [21. Exponential Hardness of Off-Policy Evaluation under History-Dependent Logging](https://arxiv.org/abs/2609.19135v1)

**作者**：Pranaya Jajoo  
**分类**：cs.LG  
**发布时间**：2026-09-16

### 📄 论文摘要

Can a logged dataset visit every hidden state frequently and still be exponentially uninformative about a target policy's value? We show that it can when the logger depends on history. For every horizon $H \ge 3$, we construct two POMDPs with at most two latent states per stage, three actions, and a common logger with three memory states. Action coverage, belief coverage, and two behavior-marginal outcome-revealing conditions all have constants independent of $H$. Nevertheless, evaluating a known deterministic target policy to accuracy $1/8$ requires $Θ((3/2)^H \log(1/δ))$ logged episodes at confidence $1-δ$, for $0 < δ\le 1/4$, even when both candidate models are known. The mechanism is simple: a reset erases the unknown transition that determines the target value. We characterize the resulting statistical experiment exactly and obtain a matching optimal estimator. A directed two-lane gridworld realizes the construction, and trajectory simulations agree with its finite-sample prediction. The result establishes intractability for the history-dependent-logging, model-based case posed by Zhang and Jiang (2025, arXiv:2503.01134), under their behavior-marginal definition of revealing.

### 🤖 AI 总结

**一句话总结**：Can a logged dataset visit every hidden state frequently and still be exponentially uninformative about a target policy's value? We show that it can when the logger depends on history. For every horiz...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Exponential, Hardness, Off-Policy, Evaluation, under, History-Dependent, Logging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19135v1) | [下载PDF](https://arxiv.org/pdf/2609.19135v1.pdf)

---

## [22. How Model Growth, Recursion, and Boundary Operators Influence Scaling Exponents](https://arxiv.org/abs/2609.19107v1)

**作者**：Zixi Chen, Akshay Vegesna, Samip Dahal 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-16

### 📄 论文摘要

Scaling laws predict how loss decreases with increases in computation. We show, contrary to conventional wisdom, that architectural interventions can modify scaling exponents in pre-training, leading to exponential improvements in performance with increases in computation. As an anchoring point, we consider the architectural formulation of looped transformers. Although not typically used in this way, looping, also known as recursive depth, provides a mechanism for model growth, by increasing the number of loops during training. Model growth, with and without shared weights, provides the biggest changes to the scaling exponents. In particular, a 7.4B model growth architecture matches GPT-3 13B on CORE with roughly $20\times$ less compute, and has compute efficiency gains that increase with scale. Moreover, simply using a boundary operator in a vanilla transformer, which normalizes and injects an earlier block, also provides increasing compute-efficiency gains, although to a lesser extent. In the data-constrained, multi-epoch setting, standard looping has a useful regularizing effect, where we find it is compute-optimal to increase the number of loops with scale. These results can be understood through the lens of computational depth: for a given computational budget, we wish to increase the usable depth of the transformer, which can lead to efficiency gains that increase with scale.

### 🤖 AI 总结

**一句话总结**：Scaling laws predict how loss decreases with increases in computation. We show, contrary to conventional wisdom, that architectural interventions can modify scaling exponents in pre-training, leading ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：How, Model, Growth, Recursion, Boundary, Operators, Influence, Scaling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19107v1) | [下载PDF](https://arxiv.org/pdf/2609.19107v1.pdf)

---

## [23. Evidence-Grounded Agentic Formulation Development in an Autonomous Laboratory](https://arxiv.org/abs/2609.19099v1)

**作者**：Michael M. Craig, Riley J. Hickman, Yingshan Ma 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-16

### 📄 论文摘要

Self-emulsifying drug delivery systems (SEDDS) can improve the oral bioavailability of poorly soluble drugs, but identifying high-performing formulations remains experimentally intensive. We present Andromeda 2, an agentic system that reasons over structured in-house experimental evidence and invokes computational and experimental tools to design and execute successive formulation batches. Using a miniaturized automated laboratory at a matched budget, we benchmark it against Andromeda 1, a probabilistic optimization model deployed across dozens of live development projects, and a wet-lab design-of-experiments (DoE) campaign. For paclitaxel, Andromeda 2 achieved a 50% high-performance hit rate versus 17% for Andromeda 1 and 2% for DoE, and identified 12 formulations meeting all four target product profile (TPP) objectives versus 6 and 0, respectively. Median $AUC_{10-240}$ was 70.1, 12.0, and 3.5 mg$\cdot$min/mL, while maximum AUC was comparable between Andromeda 2 and Andromeda 1. A selected full-TPP formulation achieved an apparent effective paclitaxel loading of $19 \pm 5\%$ w/w at the first FaSSIF measurement, approximately 3.3-fold higher than the 5.7% w/w loading reported for a published paclitaxel S-SEDDS. A controlled ablation showed that access to structured in-house experimental evidence increased mean AUC by 34%.

### 🤖 AI 总结

**一句话总结**：Self-emulsifying drug delivery systems (SEDDS) can improve the oral bioavailability of poorly soluble drugs, but identifying high-performing formulations remains experimentally intensive. We present A...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Evidence-Grounded, Agentic, Formulation, Development, Autonomous, Laboratory, Self-emulsifying

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19099v1) | [下载PDF](https://arxiv.org/pdf/2609.19099v1.pdf)

---

## [24. Probabilistic Linear Explanations](https://arxiv.org/abs/2609.19077v1)

**作者**：Frederic Koriche, Jean-Marie Lagniez, Chi Tran  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-16

### 📄 论文摘要

Formal explainability provides mathematically grounded justifications for individual predictions. However, abductive explanations often exceed human cognitive limits by involving too many features, while probabilistic relaxations have remained largely limited to categorical classification. We present a unified framework for probabilistic explainability based on sparse, anchored linear models, applicable to both binary classification and continuous regression. By mapping instances to the Boolean hypercube, our linear explanations strictly generalize subset-based approaches: they capture both the magnitude and direction of feature contributions while enforcing a prescribed sparsity budget $k$. We show that minimizing the relevance error for such explanations is \ClassNPPP-hard when the underlying model is a neural network, and we relate this intractable objective to a tractable surrogate---the fidelity error. For a parameterized family of local distributions, the relevance error of any $k$-sparse explanation is bounded by its fidelity error up to a multiplicative factor that remains small locally. We address the resulting empirical problem using two complementary approaches: a Mixed Integer Programming (MIP) formulation that yields provably optimal empirical solutions while maintaining polynomial sample complexity, and a polynomial-time Iterative Hard Thresholding (IHT) algorithm with provable approximation guarantees. Empirical evaluations show that, unlike state-of-the-art baselines such as LIME and MAPLE, our explanations satisfy both the anchoring and sparsity constraints by construction, while consistently achieving lower relevance error.

### 🤖 AI 总结

**一句话总结**：Formal explainability provides mathematically grounded justifications for individual predictions. However, abductive explanations often exceed human cognitive limits by involving too many features, wh...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Probabilistic, Linear, Explanations, Formal, explainability, provides, mathematically, grounded

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19077v1) | [下载PDF](https://arxiv.org/pdf/2609.19077v1.pdf)

---

## [25. Double descent is the principle of least action](https://arxiv.org/abs/2609.19076v1)

**作者**：Congzhou M Sha  
**分类**：cs.LG, cs.AI, math.ST, physics.comp-ph, physics.data-an  
**发布时间**：2026-09-16

### 📄 论文摘要

The test error of a model plotted against its number of parameters $d$ falls, peaks when the model can just fit the training data, and falls again, exhibiting the double descent phenomenon. We explain the phenomenon with statistical mechanics. The training trajectory of a stochastic gradient-based method is a particle wandering over the energy landscape of the training loss at an induced temperature $T$, and a run that has equilibrated visits every parameter vector of a given training loss equally often, the fundamental postulate of statistical mechanics, with probability given by the Boltzmann distribution. Because training starts at an initial point and has only finite time to diffuse, it carries an effective weight decay, which makes every parameter a quadratic degree of freedom. The equipartition theorem then distributes the energy among the $d$ degrees of freedom in shares of $T/2$, so at a fixed training loss adding parameters lowers the temperature and drives the Boltzmann distribution toward the stationary path. Finally, adding parameters can only lower the $L^2$ norm of the stationary path, so a solution sampled at fixed loss is less likely to be large with increasing $d$, effectively increasing weight regularization.

### 🤖 AI 总结

**一句话总结**：The test error of a model plotted against its number of parameters $d$ falls, peaks when the model can just fit the training data, and falls again, exhibiting the double descent phenomenon. We explain...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Double, descent, principle, least, action, test, error

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19076v1) | [下载PDF](https://arxiv.org/pdf/2609.19076v1.pdf)

---

## [26. RLLBC-Lib: An Educational Code Library for Reinforcement Learning and Learning-Based Control](https://arxiv.org/abs/2609.19074v1)

**作者**：Bernd Frauenknecht, Emma Cramer, Artur Eisele 等 12 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-16

### 📄 论文摘要

Reinforcement learning (RL) is an exciting concept as well as a remarkable success story worth sharing. However, RL builds on rather complex interactions between different objects that play out over several cycles. Such dynamics are often best explained with an easily accessible implementation. We present RLLBC-Lib, a carefully crafted code library with the goal of lowering the entry barrier for students and other learners of RL in the context of learning-based control. At its heart, RLLBC-Lib comprises a comprehensive library of tabular RL approaches to enforce a clear understanding of the theoretical foundations. A deep RL library follows the same design principles, underscoring the parallels between simple tabular and state-of-the-art deep RL approaches. Additionally, RLLBC-Lib provides a collection of implementations illustrating core RL principles and contrasting RL to other learning-based control approaches. Finally, RLLBC-Lib provides an ideal basis for creating programming assignments with automated grading.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning (RL) is an exciting concept as well as a remarkable success story worth sharing. However, RL builds on rather complex interactions between different objects that play out over s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, RLLBC-Lib, Educational, Code, Library, Reinforcement, Learning, Learning-Based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.19074v1) | [下载PDF](https://arxiv.org/pdf/2609.19074v1.pdf)

---

## [27. Higher-order pruning of experts in mixture-of-experts language models](https://arxiv.org/abs/2609.18916v1)

**作者**：Alex M. Tseng, Prannay Kaul, Luca Zancato 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-16

### 📄 论文摘要

Mixture-of-Experts (MoE) language models suffer from large parameter counts, which create a significant memory bottleneck. Expert pruning is the most direct approach for reducing this parameter count, yet existing methods make pruning decisions for each expert independently, and assume experts' contributions are purely additive. In reality, expert usage in MoEs is inherently cooperative. We derive HOPE (Higher-Order Pruning of Experts), a second-order pruning objective which provably minimizes an upper bound on the error resulting from pruning. We show that REAP (a state-of-the-art first-order pruning method) is a special case of HOPE where interaction terms are ignored. Across three frontier MoE models (up to 122B parameters), two distinct calibration sets, and multiple benchmarks (including math, instruction following, coding, and an agentic suite), we demonstrate that HOPE produces better pruning decisions than existing methods, and its advantage is most pronounced at high pruning rates and on challenging agentic workloads. At 50% pruning, HOPE outperforms all baselines and achieves an average rank of 1.58 out of 5 methods (versus 2.42 for the next-best method, REAP), with gains of up to +6.1% on agentic coding. Over all conditions, HOPE again achieves the best average rank and surpasses every other method in the majority of head-to-head comparisons. By preserving cooperative expert structure that first-order methods ignore, HOPE enables aggressive compression with minimal degradation, particularly on complex tasks where diverse expert combinations are invoked over long sequences.

### 🤖 AI 总结

**一句话总结**：Mixture-of-Experts (MoE) language models suffer from large parameter counts, which create a significant memory bottleneck. Expert pruning is the most direct approach for reducing this parameter count,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Higher-order, pruning, experts, mixture-of-experts, language, models, MoE

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18916v1) | [下载PDF](https://arxiv.org/pdf/2609.18916v1.pdf)

---

## [28. Preventing Model Collapse: A Fisher-Rao Perspective on the Dynamics of Training with Synthetic Data](https://arxiv.org/abs/2609.18878v1)

**作者**：Matteo Marchi, João Pedro Silvestre, Bahman Gharesifard 等 4 位作者  
**分类**：cs.LG, eess.SY  
**发布时间**：2026-09-16

### 📄 论文摘要

Large Language Models (LLMs) are now routinely trained using synthetic data, since high-quality human data has been exhausted by the ever increasing needs of larger and larger models. However, recursive training on synthetic data frequently induces model collapse, a degenerative feedback loop where models progressively forget the true underlying data distribution. Training on a mixture of synthetic and fresh human data is a logical countermeasure and can prevent model collapse. However, it is an open question as to what is the exact minimum required ratio of human-to-synthetic data to maintain training stability. In this paper, we establish rigorous theoretical guarantees on the minimum rate of human data required to prevent model collapse. Although previous work established a formal lower bound for this ratio, such bound can be vacuous for very high dimensions, as the analysis relies on the usual Euclidean metric in R^n and is not adapted to the space of categorical probability distributions. Instead, in this paper we explicitly leverage the information-geometric structure of the probability simplex by analyzing the dynamics of the process under the Fisher-Rao metric. We derive quantitative contraction and invariance bounds that are stable and do not become trivial as the dimensions increase. Thus, we show that the effective required data ratio to prevent model collapse is different than previously implied.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) are now routinely trained using synthetic data, since high-quality human data has been exhausted by the ever increasing needs of larger and larger models. However, recursi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Preventing, Model, Collapse, Fisher-Rao, Perspective, Dynamics, Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18878v1) | [下载PDF](https://arxiv.org/pdf/2609.18878v1.pdf)

---

## [29. Physics-based prediction, uncertainty quantification and decision-making for IN718 crystallographic texture intensity across LPBF defocus regimes](https://arxiv.org/abs/2609.18863v1)

**作者**：Yisheng Lu, John Riris, Jie Song 等 5 位作者  
**分类**：cs.LG, cond-mat.mtrl-sci, cs.CE  
**发布时间**：2026-09-16

### 📄 论文摘要

Reliable prediction of crystallographic texture in laser powder bed fusion is critical for linking process conditions with anisotropic response and for qualification. However, black-box models may fail under shift and cannot distinguish weak data support from loss of physical validity. This study develops a two-stage physics-based model for <001> || BD (build direction) texture in Inconel 718. Stage 1 maps process variables to melting mode and melt pool geometry. Stage 2 predicts texture by combining an empirical physics model with a random-forest residual model. A k-nearest-neighbor weight attenuates residual corrections for poorly supported queries, while a study-specific areal beam-power-density criterion withholds predictions outside the adopted conduction envelope. Conformal intervals are evaluated on the retained physics-valid set, and SHAP and Sobol analyses assess residual sensitivity. Under a controlled leave-one-defocus-out evaluation, the physics anchor achieved R^2 = 0.778, against -0.001 for the black-box model and 0.750 for the gated hybrid. Under leave-one-group-out cross-validation, the gated hybrid reached R^2 = 0.592 against 0.538 for the black-box model. Retained-set coverage was 92.9% at a mean full width of 3.65 multiples of a uniform distribution (MUD) under grouped cross-validation and 100% at a width of 3.21 MUD under transfer to a withheld +80 mm defocus regime. An illustrative mapping produced a retained BD elastic-modulus span of 127-187 GPa. On nine conditions from a separately built sample set, the framework withheld three, attenuated three, and matched the measured ordering for the rest. Separating data applicability, physics validity, and predictive uncertainty into distinct decisions lets the framework transfer where an unconstrained model does not, and withhold predictions where no model class performs adequately.

### 🤖 AI 总结

**一句话总结**：Reliable prediction of crystallographic texture in laser powder bed fusion is critical for linking process conditions with anisotropic response and for qualification. However, black-box models may fai...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IN718, Physics-based, prediction, uncertainty, quantification, decision-making, crystallographic, texture

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18863v1) | [下载PDF](https://arxiv.org/pdf/2609.18863v1.pdf)

---

## [30. Interpretable Multi-Instance Learning Enables Early Prediction of Key Molecular Alterations from Routine Flow Cytometry in Acute Myeloid Leukemia](https://arxiv.org/abs/2609.18825v1)

**作者**：Jonathan Legrand, Aguirre Mimoun, Baudouin Denis de Senneville 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-16

### 📄 论文摘要

Background: Molecular testing for NPM1 and FLT3-ITD mutations guides critical early treatment decisions in acute myeloid leukemia (AML), but results can take weeks, long after these decisions must be made. Flow cytometry, already performed within hours of admission as part of routine care, may carry enough signal to predict these mutations directly, without added cost or delay. Methods: We developed an interpretable multi-instance learning classifier based on a decision tree, in which each patient sample is modeled as a collection of individual cells and mutation status is inferred from cell-level predictions. The model was benchmarked against a random forest trained on clinical variables and a deep convolutional neural network adapted for multitube flow cytometry data. Performance was assessed by cross-validation on a discovery cohort of 197 patients and tested on an independent cohort of 161 patients, using the area under the receiver operating characteristic curve (AUROC) and positive predictive value. Results: In cross-validation on the discovery cohort, the MIL model achieved mean AUROCs of 0.96 (SD=0.05) for NPM1 and 0.86 (SD=0.10) for FLT3-ITD, outperforming the clinical baseline and matching deep learning approaches. The model then successfully generalized to the independent test cohort of 161 patients, reaching AUROCs of 0.90 (NPM1) and 0.82 (FLT3-ITD), with positive predictive values of 0.87 and 0.68, respectively. Cell-level interpretation recovered established immunophenotypic signatures (CD33${}^{+}$ /CD34___ for NPM1-mutated cases, CD33${}^{+}$ /low side-scatter for FLT3-ITD), directly linking model predictions to known biology.  Conclusions: These results show that an interpretable model applied to data already collected in routine care can predict AML molecular status within hours, offering a practical route to earlier, biology-informed treatment decisions.

### 🤖 AI 总结

**一句话总结**：Background: Molecular testing for NPM1 and FLT3-ITD mutations guides critical early treatment decisions in acute myeloid leukemia (AML), but results can take weeks, long after these decisions must be ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Interpretable, Multi-Instance, Learning, Enables, Early, Prediction, Key

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.18825v1) | [下载PDF](https://arxiv.org/pdf/2609.18825v1.pdf)

---

