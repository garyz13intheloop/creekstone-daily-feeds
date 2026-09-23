# arXiv AI 论文日报 | 2026-09-23

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (13 篇)
- [cs.CL](#csCL) (6 篇)
- [cs.AI](#csAI) (5 篇)
- [cs.LG](#csLG) (6 篇)

---

## cs.AI

## [1. SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving](https://arxiv.org/abs/2609.26777v1)

**作者**：Jennifer Williams, Dave Farris, Jeff Farris 等 4 位作者  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-09-22

### 📄 论文摘要

We introduce SWE-Serve, a benchmark for evaluating agents on production inference engineering tasks. Implementing an inference feature can require coordinating multiple changes across the serving stack, including model support, runtime execution, and public APIs. Existing benchmarks provide limited coverage of production inference engineering: repository-level software engineering benchmarks do not target inference, while general terminal-agent benchmarks include only a few inference tasks. Dedicated inference benchmarks, meanwhile, focus primarily on isolated kernel generation or performance optimization rather than repository-scale production feature implementation. SWE-Serve provides 53 repository-grounded tasks derived from recent production changes to SGLang, spanning six inference engineering families. Each task executes on either CPU or a single GPU (H100) and is evaluated with hidden functional and regression tests, including, where applicable, end-to-end (E2E) serving tests and calibrated performance gates. Executable no-op and oracle controls, adversarial verifier review, and closed-book execution support task validity and evaluation integrity. Across 11 models and 31 model-effort configurations, the best-performing configuration achieves 75% mean pass@1. SWE-Serve exposes a substantial gap between completing tasks locally and achieving production correctness. On 19 tasks with end-to-end coverage, model-serving E2E tests reject roughly one-third of patches that pass every other test (45.9% under the verifier versus 69.4% with E2E tests excluded from scoring), with pass rate increasing for each model's best-performing configuration. By making the production correctness gap directly measurable, SWE-Serve enables the field to track whether future agents move beyond completing tasks locally to achieving production correctness.

### 🤖 AI 总结

**一句话总结**：We introduce SWE-Serve, a benchmark for evaluating agents on production inference engineering tasks. Implementing an inference feature can require coordinating multiple changes across the serving stac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, SWE-Serve, Benchmarking, Agentic, Engineering, Production, Inference, Serving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26777v1) | [下载PDF](https://arxiv.org/pdf/2609.26777v1.pdf)

---

## [2. Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents](https://arxiv.org/abs/2609.26760v1)

**作者**：Laizhen Li, Jiarui Li, Juanjuan Zhao 等 7 位作者  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-09-22

### 📄 论文摘要

Large language model (LLM) agents often handle streams of related tasks, yet standard harnesses repeatedly ask the model to reconstruct the same control decisions inside each task's context. We study whether task feedback can instead turn recurring control into reusable executable code, while reserving LLM calls for task-specific semantic reasoning. We introduce Growing Harness, a failure-guided training paradigm that learns the agent harness itself from a strategy-free scaffold that exposes fixed model and tool interfaces but encodes no task-solving controller. Function-level execution traces localize each failure to a bounded code surface, an optimizer repairs a window of failures jointly, and a success-first held-out gate rolls back repair sequences that harm prior capability. Accepted edits accumulate in one shared harness, allowing its control structure to emerge from task feedback. Across BrowseComp-Plus and WebArena-Verified with three deployment models from 4B to 120B parameters, Growing Harness achieves the highest mean success in five of six benchmark-model settings and trails the best mean by 0.7 pp. in the sixth. Relative to a Tool-Calling agent, it reduces LLM calls by 76.0-91.8% and deployed-agent inference cost by 74.4-98.6%. On WebArena-Verified, its success remains 44.7-45.3% across model scales, whereas Tool-Calling falls to 6.7% with the 4B model. Ablations show that trace-local edits, joint repair, and gate-based rollback each improve final success. These results show that persistent program growth can move recurring control out of model context and into low-cost code, yielding reusable specialist agents that remain effective with smaller deployment models.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM) agents often handle streams of related tasks, yet standard harnesses repeatedly ask the model to reconstruct the same control decisions inside each task's context. We study ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Grow, Harness, Not, Context, Strategy-Free, Scaffolds, Reusable, Specialist

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26760v1) | [下载PDF](https://arxiv.org/pdf/2609.26760v1.pdf)

---

## [3. Type-Safe Is Not Error-Free: A Constrained Decision Head Follows the Option Name, Not the Rubric Bound to It](https://arxiv.org/abs/2609.26758v1)

**作者**：Yu Sun, Junhao Xu  
**分类**：cs.AI  
**发布时间**：2026-09-22

### 📄 论文摘要

Typed decision models are built for settings where model outputs are consumed directly by software. Instead of generating free-form text, they return a decision over a predefined set of options. By construction, every output conforms to the required schema. Yet this guarantee does not tell us whether the model interprets the options as intended. We study Jev and two Jev-like models with open weights by changing how option names are assigned to rubrics. Each option consists of an option name and a textual rubric that defines what the option means. We change only which option name is assigned to each rubric; the question, state, rubric wording, and set of option names remain exactly the same. On 1200 workflow decisions with task-specific rubrics, renaming the two options from 0/1 to no/yes changes 70.4 more answers per hundred (95% CI: [67.6, 73.1]) and shifts AUC from .94 to .23, revealing a systematic reversal in the decision ranking rather than simple uncertainty. The same operation has little effect with neutral option names. This pattern holds across all 4 predicates, where the effect is at least 7.4x larger than under the neutral control, and becomes stronger as the number of options increases. The effect also depends on the read-out geometry: a second model family that mean-pools over the full option span flips 4.1x less often. The hosted model exhibits the same behavior: the swap changes AUC from .8146 to .5806 and produces 24x as many answer flips as its test-retest floor. In contrast, replacing the option names with random character strings returns all model families to the neutral-control regime without reducing accuracy. The failure therefore depends on the semantic polarity of the option names rather than on the renaming operation itself. Across all conditions, the type-error rate remains 0%, even when decision accuracy degrades substantially.

### 🤖 AI 总结

**一句话总结**：Typed decision models are built for settings where model outputs are consumed directly by software. Instead of generating free-form text, they return a decision over a predefined set of options. By co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Type-Safe, Not, Error-Free, Constrained, Decision, Head, Follows, Option

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26758v1) | [下载PDF](https://arxiv.org/pdf/2609.26758v1.pdf)

---

## [4. The Delegation Blind Spot: Auditing Product Decisions from Agent Choices](https://arxiv.org/abs/2609.26642v1)

**作者**：Shivam Gupta  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-09-22

### 📄 论文摘要

Successful agent execution need not identify which future product improvement its user would value. We present a decision-specific audit that maps a declared observation channel and product-value contrast to compatible intervals and witness populations. Its foundations are established identification and decision theory; the contribution is an executable measurement workflow and a controlled study of its limits. A frozen experiment makes 4,800 requests to two pinned model snapshots on shared synthetic tasks. All 36 conservative primary intervals remain unresolved despite different execution accuracy. An exploratory 2,400-call follow-up records supplied preferences and resolves three of nine comparisons per model. A deterministic extractor resolves seven of nine without model calls or calibration observations, exposing unnecessary uncertainty introduced by model-generated reports. A further 14,400 controlled multinomial simulations distinguish structural ambiguity from weak identification and finite calibration precision. We propose a source-labeled decision receipt and provide an offline viewer for inspecting the audit. These results motivate preserving decision-relevant structured input and diagnosing why a decision is unresolved before collecting more telemetry. The study contains no human participants or real customer outcomes. Full proofs, raw model provenance, controlled experiments, and reproducible analyses accompany the report.

### 🤖 AI 总结

**一句话总结**：Successful agent execution need not identify which future product improvement its user would value. We present a decision-specific audit that maps a declared observation channel and product-value cont...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Delegation, Blind, Spot, Auditing, Product, Decisions, Choices

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26642v1) | [下载PDF](https://arxiv.org/pdf/2609.26642v1.pdf)

---

## [5. Quantum-Aided Active Device Detection in Energy-Harvesting Symbiotic Radio Networks](https://arxiv.org/abs/2609.26565v1)

**作者**：Remon Polus, Deemah Tashman, Soumaya Cherkaoui  
**分类**：cs.AI  
**发布时间**：2026-09-22

### 📄 论文摘要

Massive connectivity in next-generation networks demands energy- and spectrum-efficient solutions for large-scale Internet of Things (IoT) deployments. Symbiotic radio (SR) enables passive IoT devices to communicate by backscattering existing cellular transmissions. A key challenge in uplink SR is active device detection (ADD), which directly affects decoding reliability, interference management, and system throughput. We propose an energy-harvesting code-domain non-orthogonal multiple access (NOMA)-SR system in which IoT devices harvest energy from ambient uplink signals and backscatter information using low-density spreading (LDS) codes. To reduce the complexity of ADD, Grover's quantum search algorithm is employed, providing a quadratic reduction in oracle-query complexity over exhaustive maximum-likelihood (ML) search. Numerical results show that the proposed approach closely approaches ML performance while substantially reducing the number of search iterations, demonstrating its potential for scalable ambient IoT systems.

### 🤖 AI 总结

**一句话总结**：Massive connectivity in next-generation networks demands energy- and spectrum-efficient solutions for large-scale Internet of Things (IoT) deployments. Symbiotic radio (SR) enables passive IoT devices...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Quantum-Aided, Active, Device, Detection, Energy-Harvesting, Symbiotic, Radio, Networks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26565v1) | [下载PDF](https://arxiv.org/pdf/2609.26565v1.pdf)

---

## cs.CL

## [6. Agensh: Scaling Organizational Intelligence to 1,024 Agents](https://arxiv.org/abs/2609.26781v1)

**作者**：Zhihao Zhan, Ting Song, Li Dong 等 7 位作者  
**分类**：cs.CL, cs.MA  
**发布时间**：2026-09-22

### 📄 论文摘要

A multi-agent system can reduce latency on complex tasks by executing work concurrently. Several pioneering harness frameworks support multi-agent systems. However, the scalability of current multi-agent harnesses is often constrained by a central orchestrator's capacity to allocate tasks and coordinate workers. To address this limitation, we introduce Agensh, a scalable self-organized multi-agent harness without a central orchestrator: concurrent workers execute a multi-agent cooperation loop, continuously gathering context, claiming and self-assigning sub-tasks, taking action and sharing findings, verifying results, and merging progress in an asynchronous manner. The loop is supported by the agentic organization infrastructure comprising three components: a shared workspace holds proposed, ongoing, and completed work; a message interface lets workers communicate; and shared context retains reusable findings and work intentions. To test the scalability of Agensh, we evaluate it on the five hardest ProgramBench tasks with GPT-5.6-sol (high). Scaling from 1 to 128 agents raises the mean final test-pass rate from 19.31% to 28.78%, an approximately 49% relative improvement. Larger organizations reach comparable test-pass rates earlier. On pandoc, scaling from 1 to 1,024 agents raises the final test-pass rate from 33.89% to 55.06%. Worker trajectories further show that different forms of self-organized cooperation gradually emerges and standardizes as the organization grows. These results reveal the number of agents as a new scaling dimension for multi-agent organizations to expand the frontier of general intelligence, offering a practical solution for complex tasks under hard latency constraints or time budgets.

### 🤖 AI 总结

**一句话总结**：A multi-agent system can reduce latency on complex tasks by executing work concurrently. Several pioneering harness frameworks support multi-agent systems. However, the scalability of current multi-ag...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Multi-Agent, Agensh, Scaling, Organizational, Intelligence, system, can

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26781v1) | [下载PDF](https://arxiv.org/pdf/2609.26781v1.pdf)

---

## [7. Beyond Repeated Sampling: Learning Search Policies for LLM Reasoning](https://arxiv.org/abs/2609.26704v1)

**作者**：Ismail Labiad, Matthieu Kowalski, Marc Schoenauer 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-22

### 📄 论文摘要

Large language models increasingly tackle hard reasoning problems by spending more test-time compute, yet the dominant strategy remains naive repeated sampling: draw many independent solutions and hope one is correct. Because such sampling explores only through local decoding noise, it tends to produce many near duplicate attempts rather than genuinely different ideas. We ask whether exploration can instead be steered at a semantic level, by first sampling problem specific concepts, hints, or strategies and then conditioning answer generation on them. We refine this into a simple, more exploratory procedure that emits many diverse concepts in a single trajectory, and evaluate it on hard problems where repeated sampling struggles. We then go a step further and make concept generation trainable: a small concept generator is optimized with reinforcement learning so that its concepts maximize the downstream success of a larger, frozen answer generator. On hard mathematical reasoning problems, the trained concept generator substantially improves the answer generator's pass@k over naive repeated sampling at the same answer generation allocation, surpasses concepts drawn from much larger untuned models, and transfers to answer generators it was never trained against, including a model from a different family. A small model can thus be trained into an effective, reusable search policy for a much larger one.

### 🤖 AI 总结

**一句话总结**：Large language models increasingly tackle hard reasoning problems by spending more test-time compute, yet the dominant strategy remains naive repeated sampling: draw many independent solutions and hop...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Beyond, Repeated, Sampling, Learning, Search, Policies, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26704v1) | [下载PDF](https://arxiv.org/pdf/2609.26704v1.pdf)

---

## [8. Measuring the Serving Stack Instead of the Model: Hidden Confounds in Local Tool-Use Evaluation](https://arxiv.org/abs/2609.26693v1)

**作者**：Lijuan Tang, Yuemeng Zheng  
**分类**：cs.CL, cs.AI, cs.SE  
**发布时间**：2026-09-22

### 📄 论文摘要

A coding agent must emit a valid tool call--a parseable invocation of a tool in the provided schema--before the harness can execute its chosen action. We study how local serving stacks affect this protocol step and show that measured outcomes can depend on the serving layer rather than model behavior alone. In Ollama, the default tools= request is gated per model by a static template flag: some models are accepted and return calls as text, some return native tool_calls, while Phi-3 and Gemma-3 are rejected before inference. In our harness, rejection and retry exhaustion are not preserved as structured failure metadata, so downstream analysis can misclassify them as model non-calls and naively report 0% fidelity. Adding a text tool list while retaining the native channel recovers much of the measured fidelity for accepted models, whereas a uniform text protocol reduces fidelity for Llama-3.2, which has native tool-call support. Cross-stack probes on Ollama, llama.cpp, vLLM, and SGLang show different handling of the same request. Constrained decoding removes parse failures but can induce non-termination, and turn-pooled versus per-instance estimates differ by up to about 55 points. We conclude with a checklist for treating serving behavior as part of the evaluation protocol.

### 🤖 AI 总结

**一句话总结**：A coding agent must emit a valid tool call--a parseable invocation of a tool in the provided schema--before the harness can execute its chosen action. We study how local serving stacks affect this pro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Measuring, Serving, Stack, Instead, Model, Hidden, Confounds

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26693v1) | [下载PDF](https://arxiv.org/pdf/2609.26693v1.pdf)

---

## [9. Detecting GPT-Assisted Writing Using Interpretable Stylometric Features](https://arxiv.org/abs/2609.26687v1)

**作者**：Rajesh Kumar, Nabeel Siddiqui, Alexander Fuchsberger  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-09-22

### 📄 论文摘要

Distinguishing GPT-assisted from independently authored student writing has become a critical challenge in academia. This paper evaluates the discriminative capability of interpretable stylometric features extracted solely from submitted text. Using data from 90 participants who wrote both independently and with ChatGPT assistance, we evaluate eight machine learning classifiers while keeping data from the same participant together during validation. On the held-out test set, Random Forest achieved an ROC-AUC of 0.87 and an F1-score of 0.84, with False Positive and False Negative rates of 22.2% and 11.1%, respectively. SHAP analysis shows that lexical and grammatical characteristics drive the resulting predictions. The findings suggest that transparent, text-intrinsic features provide measurable signal for detecting GPT-assisted writing.

### 🤖 AI 总结

**一句话总结**：Distinguishing GPT-assisted from independently authored student writing has become a critical challenge in academia. This paper evaluates the discriminative capability of interpretable stylometric fea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Detecting, GPT-Assisted, Writing, Interpretable, Stylometric, Features, Distinguishing, independently

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26687v1) | [下载PDF](https://arxiv.org/pdf/2609.26687v1.pdf)

---

## [10. Semantic Abstraction for Natural Language Inference: a Methodological Framework for Discovering and Compensating Semantic Knowledge and Reasoning Gaps in Large Language Models](https://arxiv.org/abs/2609.26610v1)

**作者**：David Torres-Moreno, Jorge Hermosillo-Valadez  
**分类**：cs.CL  
**发布时间**：2026-09-22

### 📄 论文摘要

Despite their outstanding performance on many NLP tasks, LLMs face serious challenges related to semantic abstraction. In this study, we are interested in understanding how LLMs leverage abstract semantic knowledge in natural language inference (NLI), which requires sophisticated linguistic capabilities to interpret implicit meanings, contextual conceptual relationships, and semantic connections between words and phrases. To this end, we propose a methodological framework for constructing new semantic knowledge at a higher level of abstraction, which we define under the notions of semantic compatibility and incompatibility for NLI. In this framework, the meaning of the lexical-semantic relations between the premise and the hypothesis is reconfigured to achieve a more flexible semantic network that induces different reasoning paths in LLMs. These new pathways show a consistent pattern of responses that allows agreement on a single response. The results demonstrate that our proposal allows to discover and compensate for LLMs' semantic knowledge gaps in NLI, achieving significant improvements in accuracy, exceeding 10% for some models, and in particular for the non-entailment class. It is essential to note that LLMs need structured knowledge and not just more data to bridge reasoning gaps. Our hybrid approach directs attention to overlooked word relationships, allowing models to synthesize missing information. We believe that the future lies not in increasing model size, but in creating a semantic scafolding that mimics the flexibility of human thinking. Hopefully, our proposal will enable the development of more robust agents and interpretable reasoning, guiding AI toward reliable language understanding.

### 🤖 AI 总结

**一句话总结**：Despite their outstanding performance on many NLP tasks, LLMs face serious challenges related to semantic abstraction. In this study, we are interested in understanding how LLMs leverage abstract sema...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Semantic, Abstraction, Natural, Language, Inference, Methodological, Framework, Discovering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26610v1) | [下载PDF](https://arxiv.org/pdf/2609.26610v1.pdf)

---

## [11. Receptiveness, Not Sycophancy: Distinguishing Engagement from Deference in Language Models](https://arxiv.org/abs/2609.26579v1)

**作者**：Calvin Isley, Johann Gaebler, Max Lamparth 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.HC  
**发布时间**：2026-09-22

### 📄 论文摘要

A central concern with language models is sycophancy: their tendency to defer to users' views at the expense of independent substantive judgment. In parallel, work on social sycophancy has focused on behaviors such as validation and positivity that may signal inappropriate deference. Yet the markers of social sycophancy are also characteristic of conversational receptiveness, a construct from social psychology shown to improve interactions across disagreement. We argue that this overlap creates a construct-validity problem for social sycophancy evaluations. Using a popular moral-advice dataset, we find that responses classified as more socially sycophantic are also more receptive. Further, increasing the receptiveness of human-written responses---while preserving their substantive conclusions---causes them to be classified as more socially sycophantic. This tight coupling raises the possibility that social sycophancy evaluations inadvertently penalize desirable behavior. In a preregistered experiment comparing substantively equivalent responses, participants prefer the more receptive responses, expect users to be more likely to listen to them, and are more willing to seek advice from their authors. The same overall pattern persists even among participants who believe the original question asker is in the wrong. Finally, we introduce a simple approach that substantially increases receptiveness without increasing substantive deference, demonstrating that conversational receptiveness and substantive independence can be achieved together.

### 🤖 AI 总结

**一句话总结**：A central concern with language models is sycophancy: their tendency to defer to users' views at the expense of independent substantive judgment. In parallel, work on social sycophancy has focused on ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Receptiveness, Not, Sycophancy, Distinguishing, Engagement, Deference, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26579v1) | [下载PDF](https://arxiv.org/pdf/2609.26579v1.pdf)

---

## cs.CV

## [12. HARMONY: Hierarchical Agentic Reasoning for MONocular Image-to-Scene Synthesis](https://arxiv.org/abs/2609.26793v1)

**作者**：Shufan Sun, Chen Wang, Enxin Song 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-22

### 📄 论文摘要

Compositional 3D scene reconstruction has recently been explored from two directions: agentic reasoning that provides semantic understanding of spatial relationships but lacks precise alignment with input images; and visual geometry foundation models that predict dense point maps from input images but the reconstruction quality is limited. Therefore, recovering a complete 3D scene from a single monocular image with accurate inter-object relationships and high-fidelity reconstruction quality remains challenging. In this paper, we present HARMONY, a hierarchical chain-of-thought framework that leverages both agentic reasoning and visual geometry foundation. Given an image of an indoor scene, starting from an empty 3D floorplan, HARMONY first calibrates the camera against the reference image to establish a semantically-grounded spatial frame, then uses agentic VLM reasoning to recover the 3D room layout and an initial placement order. It then places the objects in a hierarchical order, from wall-mounted elements, free-standing furniture, to dependent decorations on top of furniture. We also use depth-first traversal for furniture so each placement conditions on previously resolved structure and a reflective feedback loop to avoid error accumulation. After each object placement by VLM, we use the point cloud estimations to perform geometry-based refinement so that the rendered image aligns better with the input. HARMONY can produce 3D scenes that are semantically consistent and perceptually aligned with the reference image, extending single-image compositional reconstruction to complex indoor scene images. Experiments on synthetic and real-world images demonstrate that HARMONY outperforms the evaluated reconstruction baselines, while qualitative comparisons with GPT-6 Astra suggest more faithful object arrangements and better preservation of scene details.

### 🤖 AI 总结

**一句话总结**：Compositional 3D scene reconstruction has recently been explored from two directions: agentic reasoning that provides semantic understanding of spatial relationships but lacks precise alignment with i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HARMONY, Hierarchical, Agentic, Reasoning, MONocular, Image-to-Scene, Synthesis, Compositional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26793v1) | [下载PDF](https://arxiv.org/pdf/2609.26793v1.pdf)

---

## [13. FleXray: Universal Clinical X-ray Segmentation](https://arxiv.org/abs/2609.26756v1)

**作者**：Victor Ion Butoi, Vivek Gopalakrishnan, John V. Guttag 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-09-22

### 📄 论文摘要

X-ray is medicine's most widely used imaging modality, yet remains among its least quantitative. Unlike volumetric modalities like CT or MRI, X-ray collapses 3D anatomy into a 2D projection, causing structures to overlap and anatomical boundaries to be ambiguous, even to experts. As a result, labeling X-ray databases for training general-purpose segmentation systems is impractical, leaving morphometric and functional X-ray analysis confined to narrow anatomical regions and applications. To this end, we present FleXray, a generalist model for anatomical segmentation across the entire body in clinical X-rays. Instead of curating large, manually annotated X-ray datasets, we build a scalable, physics-based generative X-ray data engine. Using existing 3D whole-body CT segmentation datasets and generative image-editing models, we simulate fully-annotated 2D X-rays with diverse appearances, physiological properties, and imaging geometries. Trained on these simulations, FleXray accurately segments 60 anatomical structures across unseen research datasets and in-the-wild X-rays. We further show that FleXray makes X-rays directly amenable to quantitative analysis, enabling automated measurements for disease grading, robust navigation during X-ray-guided interventions, and data-efficient learning of pathological targets. We release the model, code, a full-body X-ray segmentation dataset, and a local, easy-to-use browser-based tool at https://flexray.csail.mit.edu .

### 🤖 AI 总结

**一句话总结**：X-ray is medicine's most widely used imaging modality, yet remains among its least quantitative. Unlike volumetric modalities like CT or MRI, X-ray collapses 3D anatomy into a 2D projection, causing s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FleXray, Universal, Clinical, X-ray, Segmentation, medicine's, most, widely

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26756v1) | [下载PDF](https://arxiv.org/pdf/2609.26756v1.pdf)

---

## [14. Evaluating the Semantic-to-Geometric Gap in Adversarial Defenses Against Vision-Language Model-Based Plagiarism](https://arxiv.org/abs/2609.26733v1)

**作者**：Christopher Burger, Christina Trotter, Joseph Carlisle 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-22

### 📄 论文摘要

The rapidly advancing capabilities of vision-language models (VLMs) present a systemic challenge to academic integrity. VLMs now allow students to bypass meaningful engagement by capturing and submitting graphical problems as singular images, a practice we define as trivial plagiarism. To provide educators with actionable data on VLM limitations, we investigate the efficacy of heuristic adversarial image transformations designed to degrade model performance while remaining human-interpretable. Through a two-phase evaluation of introductory assessments, we manually assess baseline VLM performance on circuit diagrams, followed by an automated large-scale evaluation of topological structures (logic gates) and coordinate geometry (Karnaugh maps). We find that while highly capable VLMs can exhibit appreciable robustness, all models suffer vulnerability to adversarial perturbations. We conclude that while visual perturbations act as a viable near-term stopgap, long-term assessment security requires educators to reapproach assessment design given continually increasing VLM performance.

### 🤖 AI 总结

**一句话总结**：The rapidly advancing capabilities of vision-language models (VLMs) present a systemic challenge to academic integrity. VLMs now allow students to bypass meaningful engagement by capturing and submitt...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Evaluating, Semantic-to-Geometric, Gap, Adversarial, Defenses, Against, Vision-Language, Model-Based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26733v1) | [下载PDF](https://arxiv.org/pdf/2609.26733v1.pdf)

---

## [15. ASTRA-SR: Atmospheric Seeing and Turbulence Restoration for Astronomical Image Super-Resolution](https://arxiv.org/abs/2609.26731v1)

**作者**：Xining Ge, Ziteng Cui, Shuhong Liu  
**分类**：cs.CV  
**发布时间**：2026-09-22

### 📄 论文摘要

Ground-based planetary imaging suffers from atmospheric turbulence, sensor noise, and limited sampling, making restoration a joint denoising, deblurring, and super-resolution problem. We present ASTRA-SR, a blind single-frame restoration framework trained on a physics-grounded synthetic dataset. High-dynamic-range spacecraft RAW observations serve as clean sources, and paired LR inputs are synthesized using measured layer-integrated turbulence strengths, propagated moving phase screens, exposure-averaged spatially varying PSFs, and sensor noise.ASTRA-SR first estimates a noise-suppressed but blur-retaining LR image, then restores spatial structure through multiscale processing and reconstructs HR detail with serial spatial-amplitude refinement. It yields a 0.49 dB foreground PSNR gain over the strongest baseline approaches.

### 🤖 AI 总结

**一句话总结**：Ground-based planetary imaging suffers from atmospheric turbulence, sensor noise, and limited sampling, making restoration a joint denoising, deblurring, and super-resolution problem. We present ASTRA...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ASTRA-SR, Atmospheric, Seeing, Turbulence, Restoration, Astronomical, Image, Super-Resolution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26731v1) | [下载PDF](https://arxiv.org/pdf/2609.26731v1.pdf)

---

## [16. GAD-MambaUNet: Direction-Group Mamba with Gradient-Adaptive DINOv3 Distillation for Lightweight Medical Image Segmentation](https://arxiv.org/abs/2609.26729v1)

**作者**：Fang Wang, Huitao Li, Wenhan Chao 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-22

### 📄 论文摘要

In this paper, we proposed GAD-MambaUNet, a lightweight medical image segmentation network that combines efficient local modeling, direction--group state-space interaction, and training-time foundation-model supervision. To improve contextual modeling in compact segmentation networks, we introduced Direction-Group Graph Selective Scan (DG-GSS), which treated scan-direction and channel-group responses as graph nodes and enabled structured information exchange before multi-directional fusion. We further incorporated DINOv3-GAD supervision, where a frozen DINOv3 teacher provided semantic guidance during training, and Gradient-Adaptive Distillation dynamically regulated the distillation strength. GAD-MambaUNet achieves a favorable accuracy--efficiency balance compared with representative lightweight and general segmentation methods. Ablation studies further verify the effectiveness of DG-GSS and training-time DINOv3-GAD supervision. In future work, we will explore more flexible teacher--student alignment strategies and extend the proposed framework to more diverse medical segmentation scenarios, such as multi-class and multi-modal segmentation tasks.

### 🤖 AI 总结

**一句话总结**：In this paper, we proposed GAD-MambaUNet, a lightweight medical image segmentation network that combines efficient local modeling, direction--group state-space interaction, and training-time foundatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GAD-MambaUNet, Direction-Group, Mamba, Gradient-Adaptive, DINOv3, Distillation, Lightweight, Medical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26729v1) | [下载PDF](https://arxiv.org/pdf/2609.26729v1.pdf)

---

## [17. DIFTA-3D: Depth-Consistent Instance-Level Feature Transfer and Adaptation of DINOv3 for 3D Detection](https://arxiv.org/abs/2609.26702v1)

**作者**：Linman Wang, ZiFei Zhang, Chunran Zheng 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-22

### 📄 论文摘要

RGB-D 3D instance detectors benefit from visual semantics, but the task-specific Faster R-CNN/ResNet branch used by IIFNet3D couples feature extraction to a separately trained 2D detector and its image-domain labels. Replacing that branch with a frozen vision foundation model removes this task-specific dependency, but may introduce occlusion noise and a mismatch between patch features and geometry-aware detection features. In this work, we investigate this replacement through an adaptation of DINOv3 to the instance-level fusion pipeline of IIFNet3D. At the core of our approach is a depth-consistent feature pipeline that projects scene points into calibrated RGB-D frames, applies a metric depth-residual check, averages the accepted DINOv3 features into an offline point cache, and aggregates the cached features inside proposal-aligned RoI grids. The geometric and bidirectional instance-fusion paths are preserved, while Conservative VAID is evaluated as a low-strength, support-weighted semantic distillation recipe applied only to positive RoIs. We conduct extensive evaluations on ScanNetV2 to assess the proposed transfer recipes. On ScanNetV2, our DINOv3 control achieves mAP scores of 76.15 and 60.93 at IoU thresholds of 0.25 and 0.50, respectively. The Conservative VAID setting achieves mAP scores of 76.59 and 62.16, corresponding to numerical gains of 0.44 and 1.23 points over the control, respectively, in this checkpoint-level recipe comparison. The reported IIFNet3D result of 75.7/63.8 is used only as an external reference because the visual branch and processing protocol differ. Accordingly, we interpret these results as evidence for a controlled transfer recipe rather than as a causal estimate of the individual contributions of VAID or depth filtering.

### 🤖 AI 总结

**一句话总结**：RGB-D 3D instance detectors benefit from visual semantics, but the task-specific Faster R-CNN/ResNet branch used by IIFNet3D couples feature extraction to a separately trained 2D detector and its imag...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, DIFTA-3D, Depth-Consistent, Instance-Level, Feature, Transfer, Adaptation, DINOv3

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26702v1) | [下载PDF](https://arxiv.org/pdf/2609.26702v1.pdf)

---

## [18. Longitudinal Retinal Vascular Remodeling in Myopic Children Treated with Orthokeratology or Defocus Lenses: A Two-Year Comparative Study](https://arxiv.org/abs/2609.26662v1)

**作者**：Zhihao Zhao, Yinzheng Zhao, Jie Zhang 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-22

### 📄 论文摘要

Purposes: To characterize longitudinal retinal vascular changes in myopic children treated with orthokeratology (OK) or multifocal defocus lenses (Defocus) and to examine their association with axial elongation. Methods: In this retrospective cohort study, 43 myopic children underwent comprehensive clinical examination and fundus photography at baseline, 12 months, and 24 months. Axial length (AL) and spherical equivalent refraction (SER) were recorded at baseline, 6, 12, and 24 months. An automated segmentation model extracted vascular parameters, main vessel angle (MA), branching angle (BA), bifurcation edge angle (BEA), crossover point (COP), and terminal vessel count (TVC). Repeated-measures ANOVA assessed temporal changes. Pearson or Spearman correlations evaluated associations between AL and vascular metrics. Results: Over 24 months, the OK group exhibited significantly slower axial elongation than the Defocus group (0.214 mm and 0.522 mm, p < 0.01). In the OK group, MA and BA decreased modestly, BEA in arteries declined gradually, but COP and TVC remained relatively stable. The Defocus group demonstrated more pronounced decreases in MA and BA, an increase in BEA, and significant reductions in COP and TVC (p < 0.05). Correlation analysis revealed stronger associations between AL and vascular parameters, especially COP and TVC, in the Defocus group at all time points, whereas only BA and BEA correlated with AL in the OK group. Conclusions: OK lenses mitigate axial elongation and induce milder retinal vascular remodeling compared to Defocus lenses. Distinct temporal patterns of vascular metrics changes were observed between the two interventions, and correlate differentially with axial growth.

### 🤖 AI 总结

**一句话总结**：Purposes: To characterize longitudinal retinal vascular changes in myopic children treated with orthokeratology (OK) or multifocal defocus lenses (Defocus) and to examine their association with axial ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Longitudinal, Retinal, Vascular, Remodeling, Myopic, Children, Treated, Orthokeratology

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26662v1) | [下载PDF](https://arxiv.org/pdf/2609.26662v1.pdf)

---

## [19. Laryngeal Structure Segmentation in High-Speed Videoendoscopy Using Deep Learning](https://arxiv.org/abs/2609.26636v1)

**作者**：Sardar Nafis Bin Ali, Mohsen Zayernouri, Dimitar D. Deliyski 等 4 位作者  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-09-22

### 📄 论文摘要

Laryngeal high-speed videoendoscopy (HSV) offers an effective means of observing the motion of different laryngeal structures along with vibratory behaviors of the vocal folds under various voicing conditions. Segmentation of laryngeal tissues enables analysis of different tissue structures and their dynamics, helping characterize the involvement of laryngeal muscles in voice production. Given the large number of HSV frames, automating this task is imperative. While deep learning-based methods have been implemented in previous studies to segment laryngeal structures, they have not been applied to HSV data during connected speech, which poses significant challenges due to excessive tissue movements and image quality limitations associated with fiberoptic image acquisition. The application of deep learning to connected speech data is critical for capturing nonstationary laryngeal behaviors and identifying anomalous patterns associated with voice disorders. The present study aims to address these gaps by training U-Net models to detect the aryepiglottic folds and arytenoid cartilages, vocal folds, epiglottis, and glottal area, using HSV data from both sustained vowel phonation and connected speech obtained from normophonic and disordered voices. Image pre-processing techniques, including noise removal and histogram equalization, were applied to improve the quality of the training HSV images and enhance network performance. Finally, to evaluate the accuracy and reliability of the networks, quantitative performance metrics were used alongside qualitative visual inspection of the test images. The high performance of the developed networks, with overall accuracies exceeding 95%, establishes their potential as reliable tools for automated laryngeal image analysis, quantitative characterization of laryngeal dynamics, and future detection of anomalous laryngeal behaviors in clinical settings.

### 🤖 AI 总结

**一句话总结**：Laryngeal high-speed videoendoscopy (HSV) offers an effective means of observing the motion of different laryngeal structures along with vibratory behaviors of the vocal folds under various voicing co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Laryngeal, Structure, Segmentation, High-Speed, Videoendoscopy, Deep, Learning, HSV

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26636v1) | [下载PDF](https://arxiv.org/pdf/2609.26636v1.pdf)

---

## [20. A Data-Interventional Framework for Auditing Privacy and Fairness in Generative Medical Imaging](https://arxiv.org/abs/2609.26623v1)

**作者**：Mischa Dombrowski, Bernhard Kainz  
**分类**：cs.CV  
**发布时间**：2026-09-22

### 📄 论文摘要

Diffusion-based synthetic data generation offers a promising route for sharing medical imaging data without releasing sensitive patient records. However, generative models face a fundamental tension between privacy and fairness: they may memorize rare training samples, leading to privacy risks, or fail to reproduce underrepresented features, resulting in unfair synthetic distributions. While prior work has largely focused on either memorization or fairness in isolation, their interaction remains insufficiently understood. In this work, we introduce a data-interventional framework to systematically analyze privacy and fairness in diffusion models. We discuss synthetic anatomical fingerprints (SAFs), rare and manually injected image features, as controlled probes to study whether models generalize sensitive attributes across identities, memorize training samples, or suppress rare signals entirely. Across multiple conditioning modalities, we observe a consistent behavior: models either forget these fingerprints or memorize the entire image in which they appear, but do not generalize them to novel images. To support large-scale auditing where explicit sample extraction is infeasible, we further introduce the indicator metric t', which estimates a model's susceptibility to memorization by exploiting the internal structure of the diffusion process. By comparing conditioning signals of varying surprisal, we reveal a clear relationship between conditioning rarity and memorization behavior. Highly surprising conditioning signals act as retrieval keys that amplify memorization, whereas low-surprisal conditioning signals systematically suppress rare features, even when these appear repeatedly in the training data. Our findings provide actionable insights and concrete mitigation strategies for safe and fair synthetic medical data sharing. Code is available at https://github.com/MischaD/Privacy.

### 🤖 AI 总结

**一句话总结**：Diffusion-based synthetic data generation offers a promising route for sharing medical imaging data without releasing sensitive patient records. However, generative models face a fundamental tension b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Data-Interventional, Framework, Auditing, Privacy, Fairness, Generative, Medical, Imaging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26623v1) | [下载PDF](https://arxiv.org/pdf/2609.26623v1.pdf)

---

## [21. GeoComposer: Geometry-Grounded Photographic Composition Instruction](https://arxiv.org/abs/2609.26620v1)

**作者**：Shuangzhi Li, Qiaoqiao Jia, Xingxin Chen 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-22

### 📄 论文摘要

Photographic composition aims to provide visual guidance for improving the framing, viewpoint, and spatial arrangement of an image. Early methods primarily rely on image cropping to enhance composition, which is restricted to the viewpoint and spatial arrangement of the input image. Recent methods have explored image understanding and editing to improve composition, but they mainly focus on instruction following and aesthetic quality, overlooking the importance of 3D scene geometry consistency for photographic composition. In this work, we propose GeoComposer, a novel geometry-grounded photographic composition framework that analyzes the composition of a given image to generate textual guidance and synthesizes a visual exemplar that enhances the composition of the given image. To promote geometry-grounded composition, we propose a geometry-aware representation learning mechanism that leverages geometric priors from a visual geometry foundation model to shape the intermediate representations of the composition editing model. This mechanism preserves both global structural relationships and local fine-grained correspondences for geometry-grounded composition. Furthermore, we propose a reinforcement learning strategy guided by a hybrid reward that jointly optimizes instruction following, aesthetic quality, and geometric consistency. This enables the model to generate visual exemplars that faithfully follow the composition instructions while remaining visually appealing and geometrically consistent. Extensive experiments show the superiority of our approach over state-of-the-art methods, highlighting its effectiveness in generating visually appealing and geometrically consistent composition.

### 🤖 AI 总结

**一句话总结**：Photographic composition aims to provide visual guidance for improving the framing, viewpoint, and spatial arrangement of an image. Early methods primarily rely on image cropping to enhance compositio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GeoComposer, Geometry-Grounded, Photographic, Composition, Instruction, aims, provide, visual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26620v1) | [下载PDF](https://arxiv.org/pdf/2609.26620v1.pdf)

---

## [22. Foundation model embeddings capture pre-diagnostic changes on screening mammograms](https://arxiv.org/abs/2609.26605v1)

**作者**：Kalina P. Slavkova, Eric Brattain, Aditya Gowd 等 9 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-09-22

### 📄 论文摘要

Foundation model embeddings of screening mammograms may encode pre-diagnostic tissue change without task-specific adaptation. We tested whether embeddings move faster along a data-derived "cancer direction" in women later biopsied for cancer than in matched screen-negative controls, and whether this depends on pretraining domain. We studied 1,773 biopsied women (785 malignant, 988 biopsy-negative) and 1,773 matched controls, each with at least two annual screening exams before their index exam. An identical pipeline was applied to four 2D models: Mammo-CLIP (MC, out-of-distribution mammography), HOPPR (in-distribution mammography), MedImageInsight (MII, general medical imaging), and BiomedCLIP (biomedical vision-language pretraining on literature figures). Breast-level embeddings quantified longitudinal movement along the cancer direction. We compared cases and controls using a between-patient design with complementary mixed-effects analysis, and biopsied versus healthy contralateral breasts within patients. Under matched modality in MII embedding space, malignant cases drifted significantly faster than controls in the first two screening intervals preceding the index exam; biopsy-negative cases showed significance only in the first. MC differences were significant in the first interval for both biopsy groups. Within-patient comparisons showed a broadly similar pattern, with MC significance extending to the second interval in both groups and HOPPR showing significance at interval 1. BiomedCLIP showed no significant differences in either design or biopsy group. Overall, directional embedding velocity emerges as a property of clinically grounded rather than general biomedical pretraining, showing that foundation model embeddings can encode pre-diagnostic mammographic change without task-specific adaptation.

### 🤖 AI 总结

**一句话总结**：Foundation model embeddings of screening mammograms may encode pre-diagnostic tissue change without task-specific adaptation. We tested whether embeddings move faster along a data-derived "cancer dire...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Foundation, model, embeddings, capture, pre-diagnostic, changes, screening, mammograms

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26605v1) | [下载PDF](https://arxiv.org/pdf/2609.26605v1.pdf)

---

## [23. Radiomics--Foundation Fusion for Interpretable RCC Classification: Internal Benchmarking and Exploratory External Transfer](https://arxiv.org/abs/2609.26578v1)

**作者**：Yuan Liang, Fangyijie Wang, Kathleen M. Curran 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-22

### 📄 论文摘要

Accurate preoperative subtype classification of renal cell carcinoma (RCC) from contrast-enhanced CT remains clinically challenging because clear cell RCC (ccRCC) and non-clear cell RCC often show overlapping imaging appearances. This study evaluates whether foundation representations reduce reliance on handcrafted radiomics, or whether radiomics remains complementary for interpretable tumour characterisation. We compared radiomics, conventional CNN features, MedicalNet-pretrained features, MedVAE representations, and fusion variants for binary ccRCC classification on KiTS23, reporting area under the receiver operating characteristic curve (AUC) with bootstrap confidence intervals and average precision (AP) as a complementary class-imbalance-sensitive metric. We further assessed branch-removal ablation, TCGA/AIMI external transfer, and interpretability using radiomics permutation importance and gate-level analysis. Internally, 3D MedVAE gated fusion achieved the best performance, with an AUC of 82.7% and AP of 92.2%. On the external TCGA cohort, the same model achieved an AUC of 79.5% and AP of 98.9%, although specificity remains uncertain because only two external non-ccRCC cases were available. Gate analysis showed a radiomics-dominant fusion regime, suggesting that foundation representations acted as case-dependent refinement signals rather than replacements for structured tumour descriptors. These findings support radiomics as a complementary and clinically interpretable component of CT-based RCC characterisation in the foundation-model era.

### 🤖 AI 总结

**一句话总结**：Accurate preoperative subtype classification of renal cell carcinoma (RCC) from contrast-enhanced CT remains clinically challenging because clear cell RCC (ccRCC) and non-clear cell RCC often show ove...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Radiomics--Foundation, Fusion, Interpretable, RCC, Classification, Internal, Benchmarking, Exploratory

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26578v1) | [下载PDF](https://arxiv.org/pdf/2609.26578v1.pdf)

---

## [24. Vision Foundation Models with Synthetic-Only Training for Monocular Spacecraft Pose Estimation](https://arxiv.org/abs/2609.26561v1)

**作者**：John Church, Vazghen Nikolian  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-09-22

### 📄 论文摘要

We present an improvement on previous spacecraft pose estimation architectures that results in the lowest published mean rotation errors we know of on the SPEED+ lightbox and sunlamp test sets for a known, non-cooperative spacecraft. By using a previously established heatmap-based pose estimation architecture and adapting a large self-supervised ViT foundation model (DINOv3) in place of the smaller convolutional and ViT encoders of previous work, we show that pose estimation accuracy improves from 300M to 840M parameters with no saturation yet observed. We also evaluate our 840M model on a Jetson Orin NX 16GB, measuring single-pass network inference at 133.8 ms per crop with a board draw of 32.0 W. These measurements demonstrate embedded inference feasibility on a processor family with orbital flight heritage. Our resulting model outperforms previous models across lightbox and sunlamp domains while training only on synthetic data. Our best model, using DINOv3 840M adapted with LoRA as the encoder (rank 64, three-seed ensemble with four-rotation test-time augmentation), results in $1.56^\circ$ mean rotation error on sunlamp and $1.17^\circ$ on lightbox, compared to the previous best mean rotation errors we know of on these test sets, $2.66^\circ$ and $1.75^\circ$ by EagerNet.

### 🤖 AI 总结

**一句话总结**：We present an improvement on previous spacecraft pose estimation architectures that results in the lowest published mean rotation errors we know of on the SPEED+ lightbox and sunlamp test sets for a k...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Vision, Foundation, Models, Synthetic-Only, Training, Monocular, Spacecraft, Pose

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26561v1) | [下载PDF](https://arxiv.org/pdf/2609.26561v1.pdf)

---

## cs.LG

## [25. EquivSVA: A Formally Verified Dataset of Behavioral Assertions Across Equivalent RTL Implementations](https://arxiv.org/abs/2609.26751v1)

**作者**：FNU Aditi  
**分类**：cs.LG  
**发布时间**：2026-09-22

### 📄 论文摘要

Large language models are increasingly used to generate SystemVerilog Assertions from natural-language specifica- tions and register-transfer-level designs. Existing datasets and benchmarks support important goals such as large- scale training, formal evaluation, specification-to-assertion generation, and mutation-based testing. A complemen- tary need is to study whether a generated assertion cap- tures externally observable behavior or depends on inci- dental details of one RTL implementation. We present EquivSVA, a formally verified dataset organized around behavior families. Each family contains four structurally distinct RTL implementations of the same externally ob- servable behavior, shared interface-level gold properties, three controlled mutants, and formal-validation evidence. EquivSVA contains 120 behavior families across 12 cat- egories, 480 reference RTL implementations, 914 gold properties, and 360 mutants. Every final family passes a fixed 17-job validation suite covering RTL equivalence, gold-property proofs, property reachability, mutant dis- tinguishability, and gold-property checks on mutants. We also provide fixed family-safe train, development, and test splits. As a small demonstration of the analyses en- abled by the dataset, we evaluate the publicly released, Apache-2.0-licensed Qwen2.5-Coder-7B-Instruct model on the held-out test split. Of 293 interface-only generated properties, 93 are formally sound, and the number of sound properties varies across equivalent implementations for 14 of 24 test families. These results illustrate how behavior-family organization can support controlled stud- ies of assertion-generation robustness without requiring changes in intended functionality. The dataset, generators, validation scripts, and case-study artifacts are publicly released at https://github.com/aditigupta96/EquivSVA.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly used to generate SystemVerilog Assertions from natural-language specifica- tions and register-transfer-level designs. Existing datasets and benchmarks support im...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, EquivSVA, Formally, Verified, Dataset, Behavioral, Assertions, Across

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26751v1) | [下载PDF](https://arxiv.org/pdf/2609.26751v1.pdf)

---

## [26. The Sirens' Song: When Proximal Background Context Overshadows Distant Evidence](https://arxiv.org/abs/2609.26718v1)

**作者**：Xiaoyu Yang, Jie Lu, Wei Duan 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-22

### 📄 论文摘要

Long-context LLMs focus on retrieving distant evidence from extensive context, yet existing work has largely focused on overcoming distance alone. In this work, we identify the Proximity Trap, insufficient attention to distant evidence often arises less from distance itself than from cumulative competition with abundant, task-irrelevant proximal background. To address the Proximity Trap, we introduce LYRA (Long-context heavY-tailed Relevance Alignment), a t-distributed directional matching mechanism that reshapes the context retrieval distribution, directing more attention mass toward task-relevant evidence, while preserving the relative positional information encoded. Extensive experiments on LongBench-v2, RULER, and LongBench demonstrate consistent improvements across context lengths and task categories. We further introduce ProxBench, a multi-level fine-grained benchmark for evaluating distant evidence utilization under increasing proximal background interference. Project page: https://xiaoyuyoung.github.io/LYRA/

### 🤖 AI 总结

**一句话总结**：Long-context LLMs focus on retrieving distant evidence from extensive context, yet existing work has largely focused on overcoming distance alone. In this work, we identify the Proximity Trap, insuffi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sirens', Song, When, Proximal, Background, Context, Overshadows, Distant

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26718v1) | [下载PDF](https://arxiv.org/pdf/2609.26718v1.pdf)

---

## [27. A Spectral Theory of Grokking: Weight Decay induces Feature Learning](https://arxiv.org/abs/2609.26679v1)

**作者**：Lenz Pracher, Pascal de Jong, Oskar Lieshaus 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-22

### 📄 论文摘要

In grokking an early fit to the training data separates from a much later improvement in generalization. During this delay, training can move from a fixed neural tangent kernel (NTK) regime to one in which task-relevant kernel eigendirections continue to evolve. We provide a quantitative theory for how this transition from lazy to rich learning can produce delayed generalization. For homogeneous networks trained with squared loss and $L_2$ weight decay, we show that a finite residual remains after memorization, with larger residual fractions in target components associated with smaller NTK eigenvalues. These residuals feed back into the dynamics of the NTK itself, and projecting the resulting dynamics onto task-relevant spectral directions yields a reduced system in which residual-driven kernel growth competes with weight decay. This system predicts that the grokking timescale is controlled by the product of learning rate and weight decay, that feature learning slows logarithmically near a critical decay above which task-aligned NTK structure can no longer support generalization, and that stronger decay can prevent fitting altogether. We test these predictions in modular addition. In a homogeneous MLP, task-aligned Fourier structure continues to emerge in the NTK after training accuracy has saturated, and an 84$\times$90-grid of trained networks across varying learning rate and weight decay recovers the predicted phase geometry and inverse-product scaling of the generalization time with learning rate and weight decay. A one-block Transformer shows similar macroscopic phase structure in a 42$\times$45-grid, as well as the same transition-time scaling despite violating exact homogeneity. Together, these results provide a mechanistic derivation connecting post-fit feature learning to both the onset of generalization and its phase structure in the learning rate and weight decay plane.

### 🤖 AI 总结

**一句话总结**：In grokking an early fit to the training data separates from a much later improvement in generalization. During this delay, training can move from a fixed neural tangent kernel (NTK) regime to one in ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Spectral, Theory, Grokking, Weight, Decay, induces, Feature

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26679v1) | [下载PDF](https://arxiv.org/pdf/2609.26679v1.pdf)

---

## [28. MAGIC: Mixed-Granularity Agent Graphs via Incremental Construction with Dense-Reward Reinforcement Learning](https://arxiv.org/abs/2609.26667v1)

**作者**：Kairui Yang, Ziheng Yi, Xunkai Li 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-22

### 📄 论文摘要

Collaboration topology shapes both the performance and execution cost of LLM-based multi-agent systems. Because tasks differ in complexity and required capabilities, recent approaches generate task-specific collaboration graphs that specify agent participation and information flow. However, representative topology generators use either individual agents or predefined groups throughout an organization, overlooking differing collaboration needs across subtasks. Our key insight is to select granularity locally for each functional role, combining fine-grained control with reusable collaboration patterns within one organization. Learning such organizations requires exploring a combinatorial construction space with limited intermediate feedback from final-answer rewards. Therefore, we propose MAGIC, a dense-reward reinforcement learning framework for mixed-granularity graph generation. Specifically, MAGIC constructs a mixed-granularity agent graph by sequentially selecting a functional role, instantiating it as a single agent or reusable group, and connecting it to existing units. We directly optimize the construction policy using returns from trajectories sampled under the current policy and use potential-based reward shaping to provide intermediate feedback from probe-based utility and structural signals while preserving the cumulative task reward. MAGIC outperforms state-of-the-art baselines across eight benchmarks and demonstrates strong inference efficiency in our efficiency study.

### 🤖 AI 总结

**一句话总结**：Collaboration topology shapes both the performance and execution cost of LLM-based multi-agent systems. Because tasks differ in complexity and required capabilities, recent approaches generate task-sp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, MAGIC, Mixed-Granularity, Graphs, via, Incremental, Construction, Dense-Reward

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26667v1) | [下载PDF](https://arxiv.org/pdf/2609.26667v1.pdf)

---

## [29. Label-Efficient Learning for Ground-Based Sky-Image Classification: A Benchmark of Transfer Learning, Active Learning, and Pseudo-Labeling on GCD](https://arxiv.org/abs/2609.26631v1)

**作者**：Esther Bou Dagher, Viktoriya Bu-Dager, Boguslaw Zegarlinski  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-09-22

### 📄 论文摘要

Accurate ground-based cloud classification is important for atmospheric monitoring, solar-energy forecasting, aviation weather assessment, and climate observation systems. However, reliable sky-image annotation is time-consuming, especially when cloud types are visually similar or mixed. We study the label efficiency of deep learning for ground-based cloud classification using the Ground-based Cloud Dataset (GCD). Rather than proposing a new architecture, we benchmark three practical strategies under limited annotation budgets: supervised transfer learning, uncertainty-based active learning, and high-confidence pseudo-labeling. An ImageNet-pretrained ResNet50 is used as a common frozen backbone, with experiments repeated over five random seeds for label budgets from $1\%$ to $100\%$ of the training labels. Supervised transfer learning is already highly label-efficient: test accuracy increases from $0.635 \pm 0.018$ with $1\%$ labels to $0.730 \pm 0.002$ with $40\%$ labels, approaching the full-label result of $0.735 \pm 0.003$. Active learning and pseudo-labeling are competitive with supervised sampling and provide small improvements for some metrics and budgets, but neither gives a large or consistent aggregate gain. Diagnostic analyses show that accepted pseudo-labels are reliable, with accuracy from $0.946$ to $0.977$, but biased toward easier high-confidence sky-type groups. In contrast, uncertainty sampling preferentially queries visually challenging groups, including Mixed and the confusable Stratocumulus and Cumulonimbus groups, but these targeted acquisitions yield only modest gains. Overall, transfer learning substantially reduces annotation requirements for GCD, while simple active and semi-supervised strategies provide limited additional benefit over a strong supervised baseline.

### 🤖 AI 总结

**一句话总结**：Accurate ground-based cloud classification is important for atmospheric monitoring, solar-energy forecasting, aviation weather assessment, and climate observation systems. However, reliable sky-image ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Label-Efficient, Learning, Ground-Based, Sky-Image, Classification, Benchmark, Transfer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26631v1) | [下载PDF](https://arxiv.org/pdf/2609.26631v1.pdf)

---

## [30. Towards Hierarchical GNNs for multi-grid power flow: generalization across operating scenarios](https://arxiv.org/abs/2609.26603v1)

**作者**：Carmine Delle Femine, Leire Garin Atxaga, Asier Diaz-Iglesias 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-22

### 📄 论文摘要

Hierarchical latent communication improves the generalization of a multi-grid power-flow model to new operating scenarios. The module exchanges information through two reduced graphs within a GENCO-based corrective network. We compare Kron-derived transports, a same-anchor Quotient construction and a flat backbone in preliminary trainings of 200 epochs on three grid topologies, with three initialization seeds per model. Evaluation uses 200 newly generated, preselected scenarios per grid. On the training topologies, Kron reduces the macro family-balanced voltage error from 5.660 +- 0.899 to 0.851 +- 0.110: an 85.0% reduction relative to Flat GENCO and 31.0% relative to Quotient, which reaches 1.235 +- 0.225. Both hierarchical models outperform a per-bus mean fitted on training solutions on every training topology in all three seeds. These results demonstrate generalization across operating scenarios within the studied topologies, with one set of learned parameters shared across grids. Evaluation on two additional topologies distinguishes this achievement from cross-topology generalization: the current models do not yet outperform the fitted reference in that calibrated- transfer setting. This preprint presents the architecture and preliminary evidence for hierarchical communication as a component of multi-grid power-flow learning, with generalization to unseen topologies as the next development objective.

### 🤖 AI 总结

**一句话总结**：Hierarchical latent communication improves the generalization of a multi-grid power-flow model to new operating scenarios. The module exchanges information through two reduced graphs within a GENCO-ba...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Towards, Hierarchical, GNNs, multi-grid, power, flow, generalization, across

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.26603v1) | [下载PDF](https://arxiv.org/pdf/2609.26603v1.pdf)

---

