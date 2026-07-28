# arXiv AI 论文日报 | 2026-07-28

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (13 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. ERUnderstand: Evaluating Vision-Language Models on Structured ER Diagrams](https://arxiv.org/abs/2607.24707v1)

**作者**：Ali Ansari, Yasmin Mohammadi, Farnoush Nili 等 6 位作者  
**分类**：cs.AI, cs.CV, cs.DB  
**发布时间**：2026-07-27

### 📄 论文摘要

Entity-Relationship Diagrams (ERDs) are central to conceptual database design, yet they are typically available only as rendered images rather than machine-readable schemas, limiting AI-assisted database engineering. We introduce ERUnderstand, the first large-scale benchmark for structured understanding of ER diagrams, comprising 2,960 diagrams collected from curated educational sources, real-world schemas, and synthetically generated examples spanning diverse domains, notations, complexity levels, and Extended Entity-Relationship (EER) constructs. Each diagram is paired with a standardized machine-readable representation for fine-grained evaluation of schema elements. Evaluating state-of-the-art Vision-Language Models (VLMs), we find that while common ERD elements are recovered reliably (F1 > 0.74), performance drops sharply on weak entities (as low as 0.28 F1), multivalued attributes (0.14 F1), and N-ary relationships (0.07 F1). Reasoning-augmented models improve overall performance by 15-25% but remain sensitive to linguistic priors and increasing diagram complexity. ERUnderstand provides a standardized benchmark for evaluating multimodal understanding of conceptual database schemas. The benchmark, dataset, evaluation toolkit, and generation code are publicly available at https://github.com/salinaria/ERUnderstand.

### 🤖 AI 总结

**一句话总结**：Entity-Relationship Diagrams (ERDs) are central to conceptual database design, yet they are typically available only as rendered images rather than machine-readable schemas, limiting AI-assisted datab...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ER, ERUnderstand, Evaluating, Vision-Language, Models, Structured, Diagrams, Entity-Relationship

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24707v1) | [下载PDF](https://arxiv.org/pdf/2607.24707v1.pdf)

---

## [2. Reason-Mediated Behavioral Models for Auditing LLM Social Simulators](https://arxiv.org/abs/2607.24649v1)

**作者**：Atharva Pandey, Gautam Jajoo  
**分类**：cs.AI  
**发布时间**：2026-07-27

### 📄 论文摘要

Large language models are increasingly used as social simulators, including as synthetic survey respondents. Most evaluations ask whether simulated outcomes resemble human outcomes. We argue that this is necessary but too weak: a simulator can match the final answer while using the wrong rationale-derived reason pattern. We study this problem through a 94-person sunscreen concept test in which each respondent evaluated three product concepts and wrote open-ended rationales. We map those rationales into signed reason states $Z$, where positive signs support adoption and negative signs block it. This gives a practical audit: holding respondent descriptors $D$, category context $K$, and concept treatment $X$ fixed, do human rationale-derived reasons help predict behavior $Y$, and can an LLM simulate the same reason state without seeing the human rationale or outcome? Human rationale-derived reasons substantially improve held-out prediction of purchase intent. LLM-simulated reasons are more brittle: they often sound plausible, but frequently echo the concept board rather than recover the respondent's acceptance or rejection path. The paper contributes an evaluation framework for social simulators. Reason states do not identify natural causal effects by themselves, but they provide an interpretable test of whether a simulator's stated reasons align with human evidence.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly used as social simulators, including as synthetic survey respondents. Most evaluations ask whether simulated outcomes resemble human outcomes. We argue that this...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Reason-Mediated, Behavioral, Models, Auditing, Social, Simulators, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24649v1) | [下载PDF](https://arxiv.org/pdf/2607.24649v1.pdf)

---

## [3. Efficiency Matters in Autonomous Research](https://arxiv.org/abs/2607.24647v1)

**作者**：Haiqian Yang, Yuan Cao  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-07-27

### 📄 论文摘要

AI-driven autonomous research (AR) systems are becoming increasingly effective across a broad range of tasks. Their performance, however, is still evaluated primarily by the quality of the final outcome. In this paper, we argue that the efficiency of the solution-search process is an equally important but often overlooked dimension of performance. A strong AR system should not only produce high-quality results, but also reach them with as small a budget as possible. Search efficiency will become increasingly important as AR expands from domains with inexpensive verification, such as mathematics and coding, to real-world scientific settings in which solution evaluation may require costly physical experiments. To capture this dimension, we propose evaluating AR systems using the area under the curve (AUC) of the Pareto frontier, alongside final outcome quality. We compare several families of search algorithms, including hill climbing, beam search, tree search, and evolutionary search, across twelve systems-optimization tasks. We find that no single search structure is consistently the most efficient. We also show that search efficiency and final outcome quality are distinct performance dimensions: a method that eventually achieves the best result may nevertheless improve slowly and consume substantially more evaluation budget before reaching that result. Because the most effective search policy is generally unknown in advance, we introduce an adaptive procedure called fluid search, which uses a portfolio bandit to dynamically allocate a fixed evaluation budget across a forest of search processes. Across the evaluated tasks, fluid search achieves the highest overall search efficiency, closely matching the performance of a per-task oracle that is given the best search structure for each task in advance.

### 🤖 AI 总结

**一句话总结**：AI-driven autonomous research (AR) systems are becoming increasingly effective across a broad range of tasks. Their performance, however, is still evaluated primarily by the quality of the final outco...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AR, Efficiency, Matters, Autonomous, Research, AI-driven, systems, becoming

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24647v1) | [下载PDF](https://arxiv.org/pdf/2607.24647v1.pdf)

---

## [4. Artificial Intelligence and Innovation Ecosystem: Evolutionary Developments, Challenges, and Future Directions](https://arxiv.org/abs/2607.24589v1)

**作者**：Zhimin Zhang, Chengzhen Ma, Jia Chai 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-27

### 📄 论文摘要

The development of the Innovative Ecosystem (IE) presents a new paradigm for economic integration, collaborative advancement, and shared achievements. The rise of Artificial Intelligence (AI) has significantly accelerated the global processes of digitization, informatization, and intelligence. Exploring how AI can leverage inherent characteristics to influence the development trajectory of IE is a topic that warrants further investigation. Given AI's increasing prominence and role within IE, the paper analyzes this new form, examining both AI's unique contributions to IE and its potential challenges. Firstly, the paper synthesizes the conceptual frameworks surrounding IE, decomposing them into manifestations in physical, social, and thinking spaces. Furthermore, the concept of Artificial Intelligence IE (AIIE) is introduced from a spatial perspective, with an exploration of the characteristics AI contributes to IE. Subsequently, the paper employs an evolutionary perspective to analyze the roles provided by AI during different development periods of AIIE. The paper then verifies the feasibility, effectiveness, and rationality of the AIIE's definition and analyzes AIIE development from an evolutionary perspective using enterprise development examples. Finally, acknowledging AI's inherent limitations, the paper examines potential challenges facing AIIE in the future from four perspectives, aiming to identify new research avenues for the further development of AIIE.

### 🤖 AI 总结

**一句话总结**：The development of the Innovative Ecosystem (IE) presents a new paradigm for economic integration, collaborative advancement, and shared achievements. The rise of Artificial Intelligence (AI) has sign...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Artificial, Intelligence, Innovation, Ecosystem, Evolutionary, Developments, Challenges, Future

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24589v1) | [下载PDF](https://arxiv.org/pdf/2607.24589v1.pdf)

---

## [5. SIREN: Towards End-to-End Extreme-Weather Early Warning with Experience-Grounded LLM Agents](https://arxiv.org/abs/2607.24588v1)

**作者**：Hang Ni, Weijia Zhang, Fan Liu 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-27

### 📄 论文摘要

Early warning of extreme weather is essential for mitigating the societal, economic, and environmental risks posed by hazardous weather events. However, expert-centered warning workflows are costly, labor-intensive, and difficult to scale throughout the warning-to-action process. Although recent advances in Large Language Model (LLM) agents have enabled the automation of weather-related tasks, existing studies remain centered on isolated scientific tasks and overlook the chain of interdependent processes required for operational extreme-weather early warning. To bridge this gap, this study investigates automated end-to-end extreme-weather early warning through LLM agents. We first develop SIREN-Bench, a comprehensive benchmark comprising 600 question-answer instances across 19 tasks, and covering four individual warning procedures and an end-to-end warning chain. Evaluation on SIREN-Bench reveals substantial capability gaps in existing weather agent frameworks. This motivates us to develop SIREN, an experience-grounded agent framework inspired by experts' use of historical cases, which combines an agentic execution environment integrating heterogeneous weather evidence and tools with a family of agent harnesses that exploit historical cases through retrieval, skill distillation, and predictive modeling. Extensive experiments demonstrate that SIREN outperforms weather-agent baselines on both individual warning procedures and end-to-end warning chains.

### 🤖 AI 总结

**一句话总结**：Early warning of extreme weather is essential for mitigating the societal, economic, and environmental risks posed by hazardous weather events. However, expert-centered warning workflows are costly, l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, SIREN, Towards, End-to-End, Extreme-Weather, Early, Warning, Experience-Grounded

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24588v1) | [下载PDF](https://arxiv.org/pdf/2607.24588v1.pdf)

---

## cs.CL

## [6. The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation](https://arxiv.org/abs/2607.24720v1)

**作者**：Tianyi Men, Zhuoran Jin, Kang Liu 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-07-27

### 📄 论文摘要

Multi-turn long-horizon planning is critical for foundation model agents, yet how to fundamentally improve it remains unclear. Existing models are trained on uncontrollable and opaque Internet data, making it difficult to identify how planning ability is acquired, shaped, and integrated. To address this challenge, we introduce a unified and controlled multi-turn environment that enables precise control. It allows systematically study long-horizon planning across three stages. (1) Planning ability acquisition during pre-training. We study data format, distribution, and quality. Explicit world model construction through CoT state transition modeling yields stronger long-horizon generalization. Atomic skills alone are insufficient for compositional generalization, whereas a litte long-horizon data works. Moreover, suboptimal trajectories severely impair performance because errors amplify over long horizons. (2) Planning ability shaping via GRPO and OPD post-training. Through mutual information, we distinguish general planning patterns from task-specific planning knowledge. For planning patterns, we identify three application regions of post-training: unnecessary, effective, and unsupported. OPD has a broader effective region than GRPO under low-quality and long-horizon settings, as it provides more consistent update directions. For planning knowledge, distilling unseen procedures from a teacher with different knowledge may impair student's prior world modeling without fully establishing new knowledge. (3) Planning ability integration through MOPD post-training. We show that multi-teacher on-policy distillation (MOPD) integrates capabilities by converging to shared planning-pattern across environments. Compatible patterns enable cross-environment generalization, partially shared patterns support continual learning, while completely conflicting patterns cause severe interference.

### 🤖 AI 总结

**一句话总结**：Multi-turn long-horizon planning is critical for foundation model agents, yet how to fundamentally improve it remains unclear. Existing models are trained on uncontrollable and opaque Internet data, m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Physics, Multi-Turn, Long-Horizon, Planning, Pre-training, Post-training, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24720v1) | [下载PDF](https://arxiv.org/pdf/2607.24720v1.pdf)

---

## [7. DataOrchestra: Learning to Orchestrate Per-Example Curation of Pretraining Data](https://arxiv.org/abs/2607.24717v1)

**作者**：Zhen Huang, Yikun Wang, Shijie Xia 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-27

### 📄 论文摘要

Pretraining data processing is critical to the downstream performance of Large Language Models (LLMs). However, many existing approaches define a fixed processing strategy at the corpus or domain level and apply it uniformly to many examples, without adapting to the needs of each example. We propose DataOrchestra, a framework that unifies different processing operations and orchestrates an example-specific pipeline for each example. Given a chunk of pretraining data, an orchestrator decides whether to drop, untouch, or clean it. For a chunk to be cleaned, it selects one or more downstream operations, ranging from programmatic editing to different forms of LLM-based rewriting. For each rewriting step, it further generates a concrete instruction, which is executed by the corresponding downstream tool model. We pretrain models from 0.5B to 7B from scratch on web data processed by DataOrchestra and observe stable average gains over individual data-processing methods across 11 benchmarks. DataOrchestra is also effective for math continued pretraining and outperforms stronger processing baselines, while reducing processing compute by skipping unnecessary downstream operations.

### 🤖 AI 总结

**一句话总结**：Pretraining data processing is critical to the downstream performance of Large Language Models (LLMs). However, many existing approaches define a fixed processing strategy at the corpus or domain leve...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, DataOrchestra, Learning, Orchestrate, Per-Example, Curation, Pretraining, Data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24717v1) | [下载PDF](https://arxiv.org/pdf/2607.24717v1.pdf)

---

## [8. Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair](https://arxiv.org/abs/2607.24604v1)

**作者**：Xueping Gao, Jianwei Yang, Qiang Yang  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-27

### 📄 论文摘要

Generate--test--revise loops are common in coding agents, but repetition alone provides no reliability guarantee. We study the gap between finding a correct patch and retaining, verifying, and submitting it. A sealed five-seed study over 30 HumanEval repairs produces 900 three-revision trajectories. Under forced revision, current correctness with current traces falls from 0.820 after one revision to 0.673 after two, although ever-correct rises to 0.847. Two common-state studies use 2,430 branches from identical frozen programs to remove post-treatment risk-set bias. In a prespecified 14B replication, stale traces harm 34/135 correct starts versus 4/135 with current traces, a 22.2-point increase (task-cluster 95\% CI $[8.9,37.0]$, exact Holm $p=0.0337$). A prospective 540-rollout policy eliminates observed correct-start harm but reduces wrong-start repair and fails its joint criterion. Repository experiments over 24 bugs and four coder stacks expose floor effects and component heterogeneity without Holm-significant effects. We therefore separate admission, preservation, grounded certification, competence, and liveness. We derive an evidence-bound typed loop contract and instantiate its mechanically enforceable subset in a reference implementation that binds verifier evidence to exact code states, preserves verified checkpoints, and emits auditable admission receipts. The implementation is an executable specification and conformance artifact, not evidence of improved repair competence or calibrated verifier dependence.

### 🤖 AI 总结

**一句话总结**：Generate--test--revise loops are common in coding agents, but repetition alone provides no reliability guarantee. We study the gap between finding a correct patch and retaining, verifying, and submitt...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Looping, Not, Reliability, State-Bound, Evidence, Typed, Revision, Contracts

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24604v1) | [下载PDF](https://arxiv.org/pdf/2607.24604v1.pdf)

---

## [9. D-Score: A Spectral Hidden-State Signal for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2607.24586v1)

**作者**：Bianca Raimondi, Davide Evangelista, Maurizio Gabbrielli 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-27

### 📄 论文摘要

Large Language Models can produce fluent text that is false, unsupported by the available evidence, or inconsistent with information that appears to be internally represented by the model. We study hallucination detection from the geometry of hidden activations and introduce the D-Score, a simple spectral statistic computed from a single forward pass. For a fixed model, layer, and tolerance parameter, the D-Score counts how many singular directions of the hidden activation matrix have singular values that remain close to the leading one. We use this quantity as a hallucination score, classifying an input text as hallucinated when its D-Score is larger than a pre-defined quantity. The motivation is that, when a model processes a text that conflicts with information available in its own internal state, the hidden representation may encode both the asserted content and some form of counter-evidence, uncertainty, correction, or lack of support; this can make the hidden trajectory spread across additional singular directions. We formalize this intuition through a lightweight spectral argument and evaluate the resulting detector on FAVA-Annotation and RAGTruth. The experiments indicate that the D-Score is a strong hidden-state signal for hallucination detection, while requiring no external verifier, no retrieval step, and no multiple generations.

### 🤖 AI 总结

**一句话总结**：Large Language Models can produce fluent text that is false, unsupported by the available evidence, or inconsistent with information that appears to be internally represented by the model. We study ha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：D-Score, Spectral, Hidden-State, Signal, Hallucination, Detection, Large, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24586v1) | [下载PDF](https://arxiv.org/pdf/2607.24586v1.pdf)

---

## [10. From Data to Device: ELMOD An Efficient German-First 2.7B Language Model for Mobile Inference](https://arxiv.org/abs/2607.24585v1)

**作者**：Darina Gold, Alexander Schwirjow, Viktor Haag 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-27

### 📄 论文摘要

We present ELMOD - Efficient Language Model for On-Device Deployment - a compact (2.7B) German language model designed for efficient inference on resource-constrained hardware. ELMOD was trained on a limited computational budget (55k H100 GPU hours) using exclusively publicly available data. We developed a suite of German-specific data pre-processing, which differ from English-oriented counterparts in their handling of morphological variation, compounding, and orthographic conventions. Furthermore, we introduced a quality filtering and rephrasing step, which increased the instructional quality of the data, improved performance during the annealing phase, and reduced overall compute requirements. Thanks to our architectural model and data choices, including prefiltering, our educational-quality filtering and rephrasal to raise the educational-quality, ELMOD is the strongest performer in its size class (<3B), matching the performance of 7B-parameter models in German.

### 🤖 AI 总结

**一句话总结**：We present ELMOD - Efficient Language Model for On-Device Deployment - a compact (2.7B) German language model designed for efficient inference on resource-constrained hardware. ELMOD was trained on a ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, 2.7B, Data, Device, ELMOD, Efficient, German-First, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24585v1) | [下载PDF](https://arxiv.org/pdf/2607.24585v1.pdf)

---

## cs.CV

## [11. ClinFusion: A Vision-Centric Multimodal LLM System for Holistic Medical Understanding](https://arxiv.org/abs/2607.24743v1)

**作者**：Hangjie Yuan, Yichen Qian, Zhiwei Tang 等 24 位作者  
**分类**：cs.CV, cs.AI, cs.CL  
**发布时间**：2026-07-27

### 📄 论文摘要

Multimodal large language models (MLLMs) hold immense potential to revolutionize clinical practice, yet deploying them in the medical domain is fundamentally a vision-centric challenge: models must absorb knowledge from heterogeneous 2D and 3D medical images, and evaluation protocols must align with radiologists' clinical practice and provide an accurate, fine-grained and factualness-driven assessment. In this paper, we introduce ClinFusion, a vision-centric MLLM designed for holistic medical understanding that systematically addresses these limitations. We propose a compositional and cascaded vision encoder architecture featuring a Cascade Spatial-Aware Locality Fusion operator that unifies diverse 2D and native 3D medical image understanding within a fused encoder. We further introduce a vision-grounded evaluation framework, including MedIF-Bench for instruction-following assessment and a region-of-interest-grounded method for clinically aligned and factualness-driven report generation evaluation. We show that ClinFusion sets a new state-of-the-art across a comprehensive suite of 2D and 3D multimodal medical benchmarks---spanning visual question answering, report generation, and instruction following---as well as textual medical tasks, outperforming leading open-source medical MLLMs (\textit{e.g.}, Hulu-Med, Lingshu) on 20 out of 24 benchmarks and demonstrating multimodal capabilities better than powerful proprietary models such as GPT-5.2 and Gemini-3-Flash on 13 out of 16 benchmarks, and can be further augmented with agentic tool use for retrieval-augmented and tool-assisted clinical workflows. A blinded evaluation by board-certified radiologists confirms that ClinFusion produces the highest-ranked reports, and validates our RoI-grounded metric as achieving the strongest correlation with expert judgment among all automatic evaluation metrics examined.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) hold immense potential to revolutionize clinical practice, yet deploying them in the medical domain is fundamentally a vision-centric challenge: models must ab...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, ClinFusion, Vision-Centric, Multimodal, System, Holistic, Medical, Understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24743v1) | [下载PDF](https://arxiv.org/pdf/2607.24743v1.pdf)

---

## [12. Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation](https://arxiv.org/abs/2607.24731v1)

**作者**：Bingnan Li, Haozhe Wang, Haozhong Xiong 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-07-27

### 📄 论文摘要

On-policy distillation (OPD) adapts diffusion models by querying a teacher along trajectories generated by the current student, but how it should behave under classifier-free guidance (CFG), a default component of modern diffusion systems, remains poorly understood. Existing OPD methods naturally extend velocity matching to the CFG-composed prediction, directly matching teacher and student guided velocities. We show that this objective is under-identified at the branch level: positive- and negative-branch errors can compensate in the guided prediction. Through two contrasting cases, we find that naive matching remains effective under shared negative conditioning, where both branch errors decrease jointly. When the model's native CFG schema retains privileged information in the teacher's negative branch that is unavailable to the student, however, this joint reduction breaks down and the composed objective induces antagonistic branch-error dynamics, reducing the positive-branch error while increasing the negative-branch error. We term this failure mode Negative Branch Asymmetry (NBA). To address NBA, we introduce Positive--Direction Matching (PDM), a branch-aware OPD objective that separately constrains the positive prediction and the CFG conditional direction. We apply PDM to dense-to-sparse video control, where naive guided matching is highly sensitive to inference guidance scales, while branch-aware supervision enables more robust and effective knowledge transfer.

### 🤖 AI 总结

**一句话总结**：On-policy distillation (OPD) adapts diffusion models by querying a teacher along trajectories generated by the current student, but how it should behave under classifier-free guidance (CFG), a default...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Rethinking, Classifier-Free, Guidance, On-Policy, Distillation, OPD, adapts

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24731v1) | [下载PDF](https://arxiv.org/pdf/2607.24731v1.pdf)

---

## [13. KANEx: Translating Kolmogorov-Arnold Networks' Interpretability to Medical Explainability](https://arxiv.org/abs/2607.24730v1)

**作者**：Krithi Shailya, Ananya Lakshmi Ravi, Venkatanathan K. V. 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-27

### 📄 论文摘要

Computer vision models have become highly effective for medical applications, yet their black-box nature continues to undermine clinician trust. In clinical workflows, chest X-ray classifiers are increasingly paired with Vision-Language Models (VLMs) to generate natural-language explanations. However, these systems add linguistic fluency without addressing the underlying opacity of the visual model. With the emergence of Kolmogorov-Arnold Networks (KANs), whose spline-based components provide inherently interpretable functional units, we investigate whether this architectural transparency can be leveraged to produce more trustworthy textual explanations. We introduce KANEx, the first ever framework that leverages the symbolic transparency of KANs to ground VLM reasoning. This interpretability also made it possible to design KAN-Map, a novel heatmap generation method derived directly from KAN models rather than gradient approximations. We feed these grounded contexts into downstream VLMs for enhanced explainability. Benchmarked on the MIMIC-CXR dataset, we demonstrate that KAN-based architectures with ResNet/ViT baselines demonstrate improved semantic similarity while producing significantly more faithful saliency maps. KAN architectures improve visual localization and downstream reasoning quality by 10%. Our findings suggest that grounding linguistic explanations and visual attributions in mathematically interpretable units is a necessary step toward trustworthy medical AI.

### 🤖 AI 总结

**一句话总结**：Computer vision models have become highly effective for medical applications, yet their black-box nature continues to undermine clinician trust. In clinical workflows, chest X-ray classifiers are incr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：KANEx, Translating, Kolmogorov-Arnold, Networks', Interpretability, Medical, Explainability, Computer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24730v1) | [下载PDF](https://arxiv.org/pdf/2607.24730v1.pdf)

---

## [14. MicroZoom: Structure-Preserving Detail Synthesis at Extreme Scale](https://arxiv.org/abs/2607.24729v1)

**作者**：Huy Huynh, Jingwei Ma, Brian Curless 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-27

### 📄 论文摘要

We introduce MicroZoom, a generative framework for gigapixel image synthesis at the microscopic scale. Given a standard photograph and a sparse set of consumer-grade microscope close-ups, MicroZoom synthesizes a seamless, gigapixel-resolution image grounded in the material character of the real references, enabling exploratory visualization of microscopic texture across the full spatial extent of an object. Our goal is plausible synthesis, not exact reconstruction. We focus on full-image, reference-based, extreme-scale super-resolution at magnification levels of up to 350x, a setting that introduces two major challenges: (1) recovering texture-specific detail from highly lossy inputs near ambiguous material boundaries, and (2) preserving correct large-scale pattern structure, such as the repeating geometry of a fabric weave, across millions of local predictions. We address these with a two-stage cascaded design, where the first stage recovers global pattern coherence and the second refines local texture detail, supplemented by a segmentation mask to guide synthesis at ambiguous boundaries. We verify our approach on a collection of self-captured everyday objects and demonstrate globally coherent, materially grounded gigapixel imagery.

### 🤖 AI 总结

**一句话总结**：We introduce MicroZoom, a generative framework for gigapixel image synthesis at the microscopic scale. Given a standard photograph and a sparse set of consumer-grade microscope close-ups, MicroZoom sy...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, We, MicroZoom, Structure-Preserving, Detail, Synthesis, Extreme, Scale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24729v1) | [下载PDF](https://arxiv.org/pdf/2607.24729v1.pdf)

---

## [15. Infrared Imaging Empowered by Artificial Intelligence for Pediatric Skeletal Triage: A Narrative Review and Future Perspectives](https://arxiv.org/abs/2607.24727v1)

**作者**：Sajad Amiri, Pardis Afshar, Elham Anjomshoa  
**分类**：cs.CV  
**发布时间**：2026-07-27

### 📄 论文摘要

Background. Pediatric musculoskeletal trauma represents up to 18% of pediatric ED visits, yet diagnosis still depends on ionizing radiography. Cumulative low-dose radiation in early life raises lifetime leukemia and brain malignancy risk, motivating radiation-free triage alternatives. Objective. To synthesize evidence for a hybrid framework coupling broad-spectrum infrared (IR) imaging with deep-learning cross-modal translation to generate clinically interpretable synthetic-radiograph reconstructions from non-ionizing data.   Approach. We review five IR spectral windows spanning 650 nm to 1 mm - NIR-I, NIR-II, SWIR, MIR/LWIR, and THz - and how dual-geometry (transmission/reflection) acquisition exploits wavelength-specific tissue depth and biochemical sensitivity. We summarize image-to-image translation networks (Pix2Pix, CycleGAN, Swin-Unet) and feature-matching algorithms (SuperPoint, SuperGlue, ALIKED, LightGlue) used to align and fuse IR data into radiograph-equivalent reconstructions.   Implications. Pediatric anatomy - smaller cross-sections, thinner cortical bone - favors IR penetration, enabling compact, portable, non-ionizing triage hardware. Feasibility is grounded in fNIRS and transcranial photobiomodulation evidence: near-infrared light passes through skin, skull, and cortex with sufficient signal for hemodynamic monitoring - a longer, more attenuating path than through a pediatric forearm or distal leg. Key barriers: paired IR/X-ray dataset construction, AI-as-medical-device regulatory pathways, generalization across body habitus and skin pigmentation, and acquisition-protocol standardization.   Conclusions. Integrated multi-spectral IR+AI imaging is a promising radiation-free complement to pediatric skeletal radiography. Progress requires multi-center paired datasets, externally validated models, and IR source safety qualification under IEC 60825-1.

### 🤖 AI 总结

**一句话总结**：Background. Pediatric musculoskeletal trauma represents up to 18% of pediatric ED visits, yet diagnosis still depends on ionizing radiography. Cumulative low-dose radiation in early life raises lifeti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Infrared, Imaging, Empowered, Artificial, Intelligence, Pediatric, Skeletal, Triage

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24727v1) | [下载PDF](https://arxiv.org/pdf/2607.24727v1.pdf)

---

## [16. SADe: Sparse-Atom Support Decontamination for Few-Shot Segmentation with Weak Support Annotations](https://arxiv.org/abs/2607.24706v1)

**作者**：Hang Xing, Guangjun Liu, Yan Xia 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-27

### 📄 论文摘要

Few-shot segmentation (FSS) commonly assumes clean pixel-level support masks, yet practical support supervision often uses boxes, scribbles, coarse masks, or pseudo-masks. These weak annotations may include texture-similar distractors and background context alongside the target, contaminating class prototypes or visual prompts before query prediction. We introduce SADe, a predictor-agnostic support decontamination layer that estimates the reliability of selected support patches without query information. Central to SADe is sparse autoencoder (SAE) atom evidence: dense similarity may respond to both target and texture-similar context, whereas contrasting atom activations inside and outside the weak-support region provides factor-level reliability cues. A lightweight router combines atom evidence with dense similarity and episode statistics to predict patch reliability and generate a cleaned support mask. Trained once on synthetic weak-support episodes from FSS-1000, the router is frozen for all target evaluations. The resulting mask supports standalone prediction or can be supplied to heterogeneous FSS models through native support interfaces without altering query-side inference. Under a matched weak-support protocol, SADe achieves the highest query mIoU in six of nine standalone prompt-shot combinations. With the same ProMi query head, it is within 0.03 mIoU of SAM3-derived masks under tight boxes and surpasses them by 11.17 and 19.49 points under box-r2 and box-r4, respectively. As a plug-in, SADe improves over raw support in 70 of 72 matched box-family comparisons across four frozen downstream models and two datasets. On point and scribble prompts, its average performance remains close to the corresponding raw-support baseline. Ablations and atom-removal controls show that atom evidence contributes reliability information beyond dense similarity.

### 🤖 AI 总结

**一句话总结**：Few-shot segmentation (FSS) commonly assumes clean pixel-level support masks, yet practical support supervision often uses boxes, scribbles, coarse masks, or pseudo-masks. These weak annotations may i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SADe, Sparse-Atom, Support, Decontamination, Few-Shot, Segmentation, Weak, Annotations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24706v1) | [下载PDF](https://arxiv.org/pdf/2607.24706v1.pdf)

---

## [17. Spatio-Temporal Conditional Denoising Transformer for Modality-Missing RGBT Tracking](https://arxiv.org/abs/2607.24701v1)

**作者**：Andong Lu, Ziyi Zha, Jiandong Jin 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-27

### 📄 论文摘要

Missing modalities in RGBT tracking often lead to incomplete and unstable multimodal feature representations that greatly degrade the performance. Existing methods typically attempt to recover missing modalities from available ones, but the quality of data generated in challenging scenarios might be unsatisfactory. In addition, current approaches exhibit limited flexibility in processing both missing and complete data. To overcome these limitations, we propose a Spatio-temporal Conditional Denoising Transformer (SCDT), which integrates the spatial cues and the temporal context to adaptively perform information reconstruction of missing modalities and feature enhancement of weak modalities in a unified framework, for robust modality-missing RGBT tracking. In particular, SCDT leverages the short-term temporal cues from recent historical frames to capture the fine-grained temporal correlations and the long-term temporal cues encoding modality evolution to capture the global context. By jointly exploiting long short-term temporal contexts as the conditions, SCDT progressively guides noisy features of available modalities to learn reliable and temporally consistent multimodal representations. Furthermore, SCDT introduces a noisemodulated adaptation mechanism that dynamically adjusts its behavior according to the modal availability, enabling a single framework to unify feature learning under both modality-missing and complete scenarios without changing the architecture or parameters. Extensive experiments on three public benchmark datasets demonstrate that our method consistently outperforms state-of-the-art methods. The code is available here.

### 🤖 AI 总结

**一句话总结**：Missing modalities in RGBT tracking often lead to incomplete and unstable multimodal feature representations that greatly degrade the performance. Existing methods typically attempt to recover missing...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Spatio-Temporal, Conditional, Denoising, Transformer, Modality-Missing, RGBT, Tracking, Missing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24701v1) | [下载PDF](https://arxiv.org/pdf/2607.24701v1.pdf)

---

## [18. Co-Learning for Missing Arbitrary Modalities in Multi-modal Classification](https://arxiv.org/abs/2607.24683v1)

**作者**：Francisco Mena, Dino Ienco, Roberto Interdonato 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-07-27

### 📄 论文摘要

Multi-modal classification leverages complementary information across diverse data sources to enhance predictive performance. However, real-world scenarios subject to operational constraints, such as sensor failures or privacy restrictions, lead to inconsistent modality availability between training and inference times. To handle missing modalities, prior studies have mainly covered bimodal data setups and focused on designing robust fusion processes. Instead, we adopt a multi-modal co-learning framework that prioritizes inter-modal collaboration rather than multi-modal fusion. Specifically, we consider that any subset of modalities may be absent, without assuming predefined missing-modality patterns, an inference scenario we refer to as missing arbitrary modalities. To address this challenge, we introduce two alternative approaches that leverage information at both feature- and decision-level. Experiments on two multi-modal classification benchmarks demonstrate significant robustness gains in various missing modality conditions. The first method shows more robust behavior under minimal missing conditions, where a single modality is absent, whereas the second performs better under extreme missing conditions, where all-but-one modalities are missing. Our code is available at https://github.com/fmenat/Co4Miss.

### 🤖 AI 总结

**一句话总结**：Multi-modal classification leverages complementary information across diverse data sources to enhance predictive performance. However, real-world scenarios subject to operational constraints, such as ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Co-Learning, Missing, Arbitrary, Modalities, Multi-modal, Classification, leverages, complementary

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24683v1) | [下载PDF](https://arxiv.org/pdf/2607.24683v1.pdf)

---

## [19. Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels](https://arxiv.org/abs/2607.24651v1)

**作者**：Zhuchenyang Liu, Yao Zhang, Yu Xiao  
**分类**：cs.CV, cs.CL, cs.IR  
**发布时间**：2026-07-27

### 📄 论文摘要

Reliable visual document understanding requires a model to attribute each answer to the evidence regions that support it. Recent benchmarks and systems express this step through a coordinate interface: the model outputs the coordinates of bounding boxes that mark the evidence regions in the document. Under this interface, vision-language models often fail to identify the right regions even when the answer is correct, a failure known as Attribution Hallucination. We present a study that investigates whether this failure is partially limited by what the model can express through coordinates. On a verified bilingual CiteVQA subset, we compare the coordinate interface with a language interface in which the model outputs only text, quoting its evidence verbatim, and a multimodal retriever returns the location of each quote as a page region proposed by a layout parser (tables and figures are quoted through their captions or notes); the comparison is repeated over six open vision-language models. Compared with the coordinate interface, evidence recall rises from at most 8 points to between 26 and 47 and the hallucination rate roughly halves, with little change in answer quality. Building on this comparison, we use the same quote-and-retrieve pipeline as a training scaffold: because region-level evidence labels are expensive to collect for long documents, we introduce a GRPO recipe whose reward is a judge's reading of the gold answer and crops of the retrieved regions, training the model to quote better evidence without any region labels and raising an 8B backbone's strict attributed accuracy from 22.4 to 33.8. These findings indicate a practical path to improve attribution"without a coordinate interface and without costly region-level supervision.

### 🤖 AI 总结

**一句话总结**：Reliable visual document understanding requires a model to attribute each answer to the evidence regions that support it. Recent benchmarks and systems express this step through a coordinate interface...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：or, Evidence, Attribution, Visual, Document, Understanding, without, Coordinates

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24651v1) | [下载PDF](https://arxiv.org/pdf/2607.24651v1.pdf)

---

## [20. Test-Time Adaptation via Dual Distillation for Videos Under Severe Distribution Shifts](https://arxiv.org/abs/2607.24611v1)

**作者**：André Sacilotti, Samuel Felipe dos Santos, Jurandy Almeida  
**分类**：cs.CV  
**发布时间**：2026-07-27

### 📄 论文摘要

Deep learning models have achieved state-of-the-art performance in several computer vision tasks. However, they experience severe performance degradation when applied to real-world scenarios due to unanticipated distribution shifts. Test-Time Adaptation (TTA) attempts to solve this problem by using unlabeled data from the target domain to dynamically adapt to the test distribution at inference time, without access to the source data. However, TTA remains a challenging problem when adapting to continuous, temporally correlated data, such as videos, and in scenarios where the target domain contains severe domain shifts. For this reason, few works in the literature explore TTA for videos under such extreme conditions. To overcome these limitations, we propose Test-time Adaptation via Dual Distillation (TADD), an online adaptation framework that relies on a lightweight projection adapter to bridge the domain gap. The adapter module is pre-trained on the source domain and then adapted to the target using our proposed complementary losses: (i) zero-shot distillation, which encourages alignment with the domain-agnostic features from a pre-trained vision-language model (VLM); and (ii) target distillation, which retains the source domain discriminative knowledge encoded in the pre-trained adapter. Built upon a frozen CLIP backbone, our method introduces this lightweight projection adapter as the sole updatable component during inference. We conducted extensive evaluations on three well-known video action recognition benchmarks: UCF-HMDB, Daily-DA, and Sports-DA. Our experiments in the closed-set scenario demonstrate that our method consistently outperforms state-of-the-art TTA baselines. Notably, our TTA approach improves upon previous methods by up to +3.81% on UCF-HMDB, +2.63% on Daily-DA, and +3.03% on Sports-DA.

### 🤖 AI 总结

**一句话总结**：Deep learning models have achieved state-of-the-art performance in several computer vision tasks. However, they experience severe performance degradation when applied to real-world scenarios due to un...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Test-Time, Adaptation, via, Dual, Distillation, Videos, Under, Severe

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24611v1) | [下载PDF](https://arxiv.org/pdf/2607.24611v1.pdf)

---

## [21. QueenVIS: Rethinking Image-Only Training for Video Instance Segmentation via Query Enrichment](https://arxiv.org/abs/2607.24598v1)

**作者**：Arian Kheirandish, Fardin Ayar, Ehsan Javanmardi 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-27

### 📄 论文摘要

Video instance segmentation (VIS) requires models to detect, segment, and track object identities across frames, and most methods enforce temporal consistency through video-level supervision. Image-only training approaches, with MinVIS as one prominent example, have challenged this assumption, reaching competitive VIS without video training by treating frames as independent images and associating instances only at inference. The field has nonetheless moved toward ever more elaborate video-trained trackers, which depend on costly identity-consistent annotations, leaving the image-only direction under-explored. A diagnostic analysis identifies object query quality as the bottleneck: queries trained only to localize objects within a frame drift apart across frames and destabilize association. QueenVIS introduces a query-centric framework for strengthening image-trained VIS. During single-frame training, we enrich Mask2Former queries with two auxiliary heads: a feature-prediction loss that aligns each query with the pooled backbone descriptor of its instance, and a center-prediction loss that injects spatial structure. Both heads are discarded at inference, adding zero parameters, and temporal identity is maintained by a training-free query-propagation and memory-bank scheme. On YouTube-VIS and OVIS with a ResNet-50 backbone, QueenVIS improves over MinVIS, up to +6.7 AP on YouTube-VIS, +4.8 AP on OVIS, and +10.3 AP on the long-sequence YouTube-VIS split. QueenVIS achieves 50.9 AP on YouTube-VIS and remains competitive with recent video-supervised state-of-the-art, without processing a single video clip during training. Our findings suggest that strengthening the discriminative power and temporal stability of object queries is an important, underexplored axis for VIS. Code and models: https://github.com/ArianKheir/QueenVIS

### 🤖 AI 总结

**一句话总结**：Video instance segmentation (VIS) requires models to detect, segment, and track object identities across frames, and most methods enforce temporal consistency through video-level supervision. Image-on...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：QueenVIS, Rethinking, Image-Only, Training, Video, Instance, Segmentation, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24598v1) | [下载PDF](https://arxiv.org/pdf/2607.24598v1.pdf)

---

## [22. CameraAnything: Refilming Videos with Arbitrary Camera Control](https://arxiv.org/abs/2607.24591v1)

**作者**：Yixuan Li, Yanhong Zeng, Ka Leong Cheng 等 14 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-27

### 📄 论文摘要

We introduce CameraAnything, the first unified framework for camera controlled video editing that enables joint control of both intrinsic and extrinsic camera parameters. Existing approaches either rely on expensive 3D reconstruction to achieve full camera functionality or restrict editing to extrinsic parameter manipulation. Moreover, the coupled influence of intrinsic and extrinsic parameters on video appearance makes disentangled modeling particularly challenging. To address this, we adopt per-pixel Plücker ray injection alongside resolution-aware 3D RoPE in self-attention, building both camera conditioning and spatial positional encoding on the target latent to jointly control camera position, focal length, and native resolution editing without cropping or outpainting. To overcome the scarcity of paired training data, we further develop a scalable synthetic pipeline that constructs diverse dynamic scenes through structured multi-camera recording and generates synchronized videos with varied camera configurations. With a tailored orthogonal training strategy, CameraAnything enables expressive video reshooting with arbitrary viewpoint control, focal length adjustment, resolution adaptation, and multi-shot transitions within a single generation process, offering strong practical value for cinematic video editing and cross-platform content adaptation in video production.

### 🤖 AI 总结

**一句话总结**：We introduce CameraAnything, the first unified framework for camera controlled video editing that enables joint control of both intrinsic and extrinsic camera parameters. Existing approaches either re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, CameraAnything, Refilming, Videos, Arbitrary, Camera, Control, introduce

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24591v1) | [下载PDF](https://arxiv.org/pdf/2607.24591v1.pdf)

---

## [23. CADER: Confidence-Aware Dynamic Evidence Reasoning for Long-Video Understanding](https://arxiv.org/abs/2607.24582v1)

**作者**：Jinlong Yang, Wenhao Zhang, Kuanwei Lin 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-27

### 📄 论文摘要

Long-video understanding increasingly relies on large vision-language models and tool-augmented reasoning, but most systems apply the same inference procedure to every example regardless of difficulty. This uniform strategy invokes unnecessary tool-assisted processing for easy questions and provides limited control when difficult questions require fine-grained temporal evidence. We propose CADER (Confidence-Aware Dynamic Evidence Reasoning), a training-free framework for adaptive and reliable long-video reasoning. CADER first performs global reasoning over uniformly sampled frames and estimates answer confidence with a logit-margin signal, allowing high-confidence examples to exit early. For uncertain examples, CADER activates a second-stage tool-augmented loop that combines temporal cropping, lightweight semantic verification, and Relevance-Guided Resampling to progressively localize question-relevant evidence. This design treats tool use as a sample-level decision: a single global pass handles easy cases, while additional reasoning is reserved for examples where uncertainty suggests that more evidence is needed. Experiments on multiple VideoQA benchmarks show that CADER improves long-video reasoning while bypassing Stage~2 for high-confidence samples. Moreover, when applied to a backbone trained only with tool-free chain-of-thought supervision, CADER achieves competitive performance against specialized tool-augmented frameworks, suggesting a practical inference-time route for adaptive long-video reasoning.

### 🤖 AI 总结

**一句话总结**：Long-video understanding increasingly relies on large vision-language models and tool-augmented reasoning, but most systems apply the same inference procedure to every example regardless of difficulty...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CADER, Confidence-Aware, Dynamic, Evidence, Reasoning, Long-Video, Understanding, increasingly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24582v1) | [下载PDF](https://arxiv.org/pdf/2607.24582v1.pdf)

---

## cs.LG

## [24. Global Convergence of DGM and PINN Algorithms for Solving Nonlinear PDEs](https://arxiv.org/abs/2607.24726v1)

**作者**：Justin Sirignano, Konstantinos Spiliopoulos, Samuel Cohen  
**分类**：cs.LG, math.NA  
**发布时间**：2026-07-27

### 📄 论文摘要

The Deep Galerkin Method (DGM) and Physics Informed Neural Networks (PINNs) have become widely-used methods for solving partial differential equations (PDEs) in the rapidly growing field of scientific machine learning. In these methods, a neural network is trained to approximate the PDE solution by using (stochastic) gradient descent to minimize the PDE residual of the neural network. Due to the non-convexity of the PDE residual objective function, the trained neural network may, in principle, only converge to a local minimizer of the objective function (which would not be a solution of the PDE). Therefore, there is a longstanding question regarding the mathematical foundations of these algorithms, and it is highly valuable to establish that the trained neural network will converge to the PDE solution. For a class of semi-linear PDEs (nonlinear in the solution and its first derivative), we prove that neural networks trained with gradient descent to minimize the PDE residual objective function will converge to the PDE solution.

### 🤖 AI 总结

**一句话总结**：The Deep Galerkin Method (DGM) and Physics Informed Neural Networks (PINNs) have become widely-used methods for solving partial differential equations (PDEs) in the rapidly growing field of scientific...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Global, Convergence, DGM, PINN, Algorithms, Solving, Nonlinear

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24726v1) | [下载PDF](https://arxiv.org/pdf/2607.24726v1.pdf)

---

## [25. Causal-TS: A Python Library for Causal Discovery in High-Dimensional and Nonstationary Time Series](https://arxiv.org/abs/2607.24673v1)

**作者**：Mohammad Fesanghary  
**分类**：cs.LG, stat.ME  
**发布时间**：2026-07-27

### 📄 论文摘要

We describe Causal-TS, an open-source Python library for causal discovery in high-dimensional and nonstationary multivariate time series. Causal-TS provides four specialized algorithms-CDNOTS, CDNOTS+, CEDAR, and GRACE-along with wrappers for GES, Granger, LASSO-VAR, and LGES, all sharing a unified conditional independence (CI) test layer with GPU acceleration via PyTorch. A regime discovery pipeline detects structural breaks via pluggable changepoint detectors and runs discovery per regime with regime-specific parameters. A command-line interface, synthetic data generators, and optional DoWhy integration provide an end-to-end pipeline from raw time series to causal effect estimates. The library is pip-installable, tested on Python 3.10--3.12, and available at https://github.com/bloomberg/causal-ts.

### 🤖 AI 总结

**一句话总结**：We describe Causal-TS, an open-source Python library for causal discovery in high-dimensional and nonstationary multivariate time series. Causal-TS provides four specialized algorithms-CDNOTS, CDNOTS+...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Causal-TS, Python, Library, Causal, Discovery, High-Dimensional, Nonstationary, Time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24673v1) | [下载PDF](https://arxiv.org/pdf/2607.24673v1.pdf)

---

## [26. Explainable Reinforcement Learning via Physics-Aware Policy Distillation](https://arxiv.org/abs/2607.24672v1)

**作者**：Shaker Al-Tamari, Waled Kadour  
**分类**：cs.LG  
**发布时间**：2026-07-27

### 📄 论文摘要

In safety-critical sectors such as robotics and automotive engineering, the deployment of Deep Reinforcement Learning (DRL) is often hindered by the black-box nature of deep neural networks. This lack of transparency poses significant challenges for regulatory compliance and human-agent trust. This paper presents an experimental study aimed at making high-performance continuous control DRL systems interpretable. A policy distillation framework is implemented using the classic Inverted Pendulum benchmark. A high-performance Twin Delayed DDPG (TD3) agent serves as an opaque, continuous teacher model, whose policy is distilled into an interpretable student surrogate based on a shallow Decision Tree. By leveraging a custom physics-aware feature and "Noisy Oracle Rollouts" for dataset generation, the distillation process achieves performance equivalent to the expert teacher. Furthermore, comparative control theory analysis reveals a fundamental trade-off: transitioning from continuous to discrete rule-based control induces high-frequency Bang-Bang actuation and a stable bimodal limit cycle. Simulation results indicate that Bounded-Input Bounded-Output (BIBO) stability is maintained while providing both global and local interpretability for safe autonomous systems.

### 🤖 AI 总结

**一句话总结**：In safety-critical sectors such as robotics and automotive engineering, the deployment of Deep Reinforcement Learning (DRL) is often hindered by the black-box nature of deep neural networks. This lack...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Explainable, Reinforcement, Learning, via, Physics-Aware, Policy, Distillation, safety-critical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24672v1) | [下载PDF](https://arxiv.org/pdf/2607.24672v1.pdf)

---

## [27. When Can You Correct Distribution Drift in Temporal Graph Generation? A Sharpening--Drift Tension and an Impossibility for Observation-Based Correction](https://arxiv.org/abs/2607.24662v1)

**作者**：Tianpeng Li, Xuan Guo, Wenjun Wang 等 5 位作者  
**分类**：cs.LG, cs.SI  
**发布时间**：2026-07-27

### 📄 论文摘要

Generative models of temporal graphs are trained on one stretch of an evolving network and deployed on the next, and they degrade badly in the gap. We show this degradation is derivable, general, and not fixable from observations. The masked flow-matching loss decomposes exactly, with no independence assumption, into an irreducible entropy plus a divergence whose derivative along the training path is positive precisely for structures rare during training and common at deployment, diverging as their training probability goes to zero. Empirically the trade-off is a power law with exponent $-0.605$ ($R^2=0.9977$), and drift raises the sampler's error floor without changing how many steps reach it: across seven well-powered conditions the drift-period marginal error varies by at most $6\%$ over a $50\times$ range of sampling budgets, while the floor sits $2.2\times$ to $34.3\times$ above the in-period floor. Because the deployment period is observed, correction looks like a matter of measurement. It is not. We prove that any corrector measurable with respect to past observations leaves at least the conditional variance of the statistic it tracks, and that trend extrapolation beats trusting the last observation only when $μ^2>v(1-2ρ)$. Both premises are measurable and both go the wrong way: the drift is trendless and mean-reverting, with a one-step innovation as large as the drift itself. An oracle removes $60\%$ of the error, the best observation-based corrector recovers $5.7\%$ of that, and extrapolation is strictly worse than doing nothing clever.

### 🤖 AI 总结

**一句话总结**：Generative models of temporal graphs are trained on one stretch of an evolving network and deployed on the next, and they degrade badly in the gap. We show this degradation is derivable, general, and ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Can, Correct, Distribution, Drift, Temporal, Graph, Generation?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24662v1) | [下载PDF](https://arxiv.org/pdf/2607.24662v1.pdf)

---

## [28. Sparse Autoencoders Encode Both Concepts and Functions: The Downstream Geometry of Feature Effects](https://arxiv.org/abs/2607.24645v1)

**作者**：Phu Gia Hoang, Anwoy Chatterjee, Tanmoy Chakraborty 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-07-27

### 📄 论文摘要

The wide-scale use of sparse autoencoders (SAEs) as interpretability tools is limited by inconsistent links between SAE features and model behavior. Features with clear activation descriptions may have weak or unexpected causal effects; steering can vary across prompts or oppose the intended direction; and activation-based feature selection can miss features that produce the desired output change. Prior work has studied feature geometry inside the model, where features are computed. We instead study the geometry of changes in model logits caused by feature interventions. We introduce Feature-Effect Geometry Analysis (FEGA), an unsupervised framework that removes the same active SAE feature across contexts and analyzes the resulting cloud of logit changes. Across SAE variants, consistent one-dimensional effects are rare: few features behave like reusable directions. To interpret this variation, we distinguish value-like features, tied to static information such as factual attributes, from pointer-like features, associated with context-dependent operations. Value-like features more often exhibit structured, low-dimensional effects, although these effects typically span several directions. Pointer-like features, by contrast, predominantly exhibit diffuse effects. Our results show that a feature can be interpretable and causally relevant without providing a stable direction for steering.

### 🤖 AI 总结

**一句话总结**：The wide-scale use of sparse autoencoders (SAEs) as interpretability tools is limited by inconsistent links between SAE features and model behavior. Features with clear activation descriptions may hav...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sparse, Autoencoders, Encode, Both, Concepts, Functions, Downstream, Geometry

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24645v1) | [下载PDF](https://arxiv.org/pdf/2607.24645v1.pdf)

---

## [29. Attribution and Uncertainty Behavior of Learned Residual Gyro Correction for Gyro-Stellar Estimation](https://arxiv.org/abs/2607.24608v1)

**作者**：Mariela De Lucas Álvarez, Melvin Laux, Arthur de Freitas Precht 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-27

### 📄 论文摘要

This work investigates uncertainty decomposition and explainability in a deep learning-based framework for gyroscope bias correction. A 1-D Convolutional Neural Network is trained to predict residual angular rate corrections from multi-sensor inputs, including gyroscope and star tracker measurements. The bias corrections are sent to a flight-representative Gyro-Stellar Estimator. The network produces both mean corrections and input-dependent (heteroscedastic) aleatoric uncertainty, while epistemic uncertainty is estimated via an ensemble of independently trained models.   The proposed approach is trained under nominal conditions and evaluated in both nominal and structured perturbations that include additive and temporally correlated noise. Gradient-based attribution methods are applied to both the correction and uncertainty outputs, enabling a decomposition of the evidence that drives state updates and uncertainty estimates. By aggregating attribution patterns across rotational axes and regimes, we reveal axis-specific behaviors and characterize how structured perturbations influence the collaboration between aleatoric and epistemic uncertainty.   Uncertainty analysis shows that aleatoric uncertainty increases with perturbation intensity, but the distributions overlap and the calibration is not consistent across regimes. On the other hand, epistemic uncertainty gives a clear signal that gets clearer as the distributional shift happens, showing that the models disagree more. These results show that aleatoric and epistemic uncertainty work well together and that epistemic uncertainty is better at distinguishing between nominal and perturbed operating conditions. The results provide insight into the behavior of hybrid learning-based state estimation components and motivate the use of uncertainty for downstream monitoring and fault detection.

### 🤖 AI 总结

**一句话总结**：This work investigates uncertainty decomposition and explainability in a deep learning-based framework for gyroscope bias correction. A 1-D Convolutional Neural Network is trained to predict residual ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Attribution, Uncertainty, Behavior, Learned, Residual, Gyro, Correction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24608v1) | [下载PDF](https://arxiv.org/pdf/2607.24608v1.pdf)

---

## [30. PYPM-GGD: Pitman-Yor Process Mixture with Generalized Gaussian Density using ADAM](https://arxiv.org/abs/2607.24583v1)

**作者**：Kart-Leong Lim  
**分类**：cs.LG  
**发布时间**：2026-07-27

### 📄 论文摘要

Large scale Bayesian nonparametrics (BNP) learner such as Stochastic Variational Inference (SVI) can handle datasets with large class number and large training size at fractional cost. Like its predecessor, SVI rely on the assumption of conjugate variational posterior to approximate the true posterior. A more challenging problem is to consider large scale learning on non-conjugate posterior. Recent works in this direction are mostly associated with using Monte Carlo methods for approximating the learner. However, these works are usually demonstrated on non-BNP related task and less complex models such as logistic regression, due to higher computational complexity. In order to overcome the issue faced by SVI, we develop a novel approach based on the recently proposed constant stepsize stochastic gradient ascent to allow large scale learning on non-conjugate posterior. Unlike SVI, our new learner does not require closed- form expression for the variational posterior expectatations. Our only requirement is that the variational posterior is differentiable. In order to ensure convergence in stochastic settings, SVI rely on decaying step-sizes to slow its learning. Inspired by SVI and Adam, we propose the novel use of adaptive stepsizes in our method to significantly improve its learning. We show that our proposed methods is compatible with ResNet features when applied to large class number datasets such as MIT67 and SUN397. Finally, we compare our proposed learner with several recent works such as deep clustering algorithms and showed we were able to produce on-par or outperform the state-of-the-art methods in terms of clustering measures.

### 🤖 AI 总结

**一句话总结**：Large scale Bayesian nonparametrics (BNP) learner such as Stochastic Variational Inference (SVI) can handle datasets with large class number and large training size at fractional cost. Like its predec...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PYPM-GGD, Pitman-Yor, Process, Mixture, Generalized, Gaussian, Density, ADAM

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.24583v1) | [下载PDF](https://arxiv.org/pdf/2607.24583v1.pdf)

---

