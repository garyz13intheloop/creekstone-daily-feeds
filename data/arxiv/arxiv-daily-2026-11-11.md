# arXiv AI 论文日报 | 2026-11-11

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (8 篇)
- [cs.LG](#csLG) (13 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.CL](#csCL) (3 篇)

---

## cs.AI

## [1. Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations](https://arxiv.org/abs/2611.14514v1)

**作者**：Ziang Liu, James J. Kim, Yijia Dai 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-11-10

### 📄 论文摘要

LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternative the evidence supports. To recover that alternative, we introduce Contrastive Discovery, which replaces the single hypothesis with a contrast set, a scientific question paired with mutually exclusive and collectively exhaustive competing explanations. Each experiment is scored by how its evidence redistributes belief across the set, and the question is resolved when belief concentrates on one explanation. Because contrast sets change only the unit an agent proposes and scores, an existing agent can use them to re-evaluate evidence it has already collected or to guide its search. Across six domains, $89\%$ of the pointwise candidates with the largest belief shifts are rejections. On the same evidence, contrast sets resolve $73\%$ of these candidates to a specific alternative. When contrast sets guide search, the agent resolves $67\%$ more questions than pointwise surprisal under the same experiment budget. In a blinded study, $38$ human experts chose the same explanation on $78\%$ of resolved questions and on $82\%$ of questions where the pointwise agent rejected its hypothesis and stopped. Together, these results support explicit competing explanations as a way for discovery agents to resolve more scientific questions from the same evidence and validation budget.

### 🤖 AI 总结

**一句话总结**：LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Contrastive, Discovery, Open-Ended, Scientific, over, Competing, Explanations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14514v1) | [下载PDF](https://arxiv.org/pdf/2611.14514v1.pdf)

---

## [2. Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents](https://arxiv.org/abs/2611.14493v1)

**作者**：Howard Zhang, Chuck Arvin, Logan Brown 等 6 位作者  
**分类**：cs.AI, cs.CL, cs.LG, cs.SE  
**发布时间**：2026-11-10

### 📄 论文摘要

Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation paradigm (trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics), applied to two analytics agents in a controlled research setting using frozen execution traces. Phase 1 quantifies evaluation harness stability through repeated measurements, finding that 97% of configurations meet the stability threshold and that stability patterns are agent-independent. Phase 2 measures known risk detection on 72 ground-truth test cases, where the trace-based framework achieves the best precision-recall balance (F1=0.90) while text-only evaluation matches on recall but generates 5x more false alarms. Phase 3 evaluates unknown risk discovery, uncovering 24 novel failures with zero overlap between functional testing and security red-teaming. Our results demonstrate that (1) the information available to the evaluation harness determines evaluation quality, (2) functional and security evaluation are complementary, and (3) LLM-based evaluation harnesses surface subtle errors that human reviewers miss. We recommend a two-framework strategy: trace-based evaluation for functional assessment and adversarial red-teaming for security validation.

### 🤖 AI 总结

**一句话总结**：Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, Comparative, Analysis, Evaluation, Frameworks, Stability, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14493v1) | [下载PDF](https://arxiv.org/pdf/2611.14493v1.pdf)

---

## [3. ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows](https://arxiv.org/abs/2611.14492v1)

**作者**：Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya 等 9 位作者  
**分类**：cs.AI, cs.LG, cs.MA  
**发布时间**：2026-11-10

### 📄 论文摘要

Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scale. We present ReTrace, which turns an SOP and a few logged agent runs into a reusable workflow in which code, not an LLM, selects the next step. The agent's reasoning, the explanation it writes with each tool call, often states why it took an action; the tool calls alone do not. ReTrace extracts the condition behind each step, merges these conditions across runs into a compact rule document, and generates an executable workflow from it. Only this last stage depends on the platform, so rule documents can be compiled for different orchestration platforms. On $79$ procedures from our production platform, ReTrace workflows reach $93.8\%$ completion, against $96.8\%$ for the agent, at $24\%$ lower cost per task. On $τ^2$-Bench, they reach $75.8\%$ task success (agent: $80.6\%$) and run in $1.3$s instead of $170$s; three rounds of repair on training failures lift $k{=}2$ workflows from $66.7\%$ to $81.2\%$. On eight SOP-Bench procedures, ReTrace without repair trails few-shot generation ($80.6\%$ vs. $83.6\%$), but repair from labeled training failures lifts it to $87.8\%$ at $0.40$s per task, compared to $85.5\%$ in $46.6$s for the agent.

### 🤖 AI 总结

**一句话总结**：Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they ca...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, ReTrace, Distilling, Tool-Using, Planner-Free, Workflows, Business, process

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14492v1) | [下载PDF](https://arxiv.org/pdf/2611.14492v1.pdf)

---

## [4. Bits or permutations? Spending a fixed inference budget on weight precision or on option-order averaging in small local language models](https://arxiv.org/abs/2611.14413v1)

**作者**：Mohammed Nayeem Khan, Logesh L, Aliyas Ahmad Misri  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-11-10

### 📄 论文摘要

Local language models can save memory by storing weights in fewer bits, and they can reduce sensitivity to the order of answer options by averaging a few reorderings. We ask whether the first makes the second worse, and which is the cheaper way to spend a fixed budget. On Qwen3-0.6B and Qwen3-1.7B with simulated round-to-nearest weight quantization (8, 6, 4 and 3 bits, fp16 reference), read from the logits of the letters A to D on ARC-Easy, ARC-Challenge, MMLU and HellaSwag (300 items each), 6 bits lose no accuracy against fp16 (they score +1.8 (+1.0 to +2.5) and +0.9 (+0.3 to +1.5) points higher, which we do not explain), and 8 bits change it by -0.7 (-1.1 to -0.3) and -0.4 (-0.7 to -0.2) points. At 4 bits the answer-slot skew rises from 0.15 to 0.53 (0.6B) and from 0.07 to 0.12 (1.7B); Gaussian noise at the same weight SNR gives 0.15 and 0.37 (two draws) and 0.19 (one draw), so the control is inconclusive on whether rounding adds slot skew beyond equal-power noise. Flip rates rise but stay below an accuracy-matched baseline of independent uniform errors. Averaging four cyclic orders recovers +12.6 points at 4 bits for 0.6B (+5.3 at fp16). We price bits and passes in one machine-independent unit, weight bytes read times passes. In cost-matched pairs, extra orders beat extra bits only when the weights have 6 or more bits, and the decision table reduces to: use 6-bit weights and spend the rest of the budget on up to four orders, one pass each. Everything is simulated on two small models with the simplest quantizer; a title-level search found no earlier study of quantization together with option order.

### 🤖 AI 总结

**一句话总结**：Local language models can save memory by storing weights in fewer bits, and they can reduce sensitivity to the order of answer options by averaging a few reorderings. We ask whether the first makes th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：or, Bits, permutations?, Spending, fixed, inference, budget, weight

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14413v1) | [下载PDF](https://arxiv.org/pdf/2611.14413v1.pdf)

---

## [5. An Energy-Based Perspective on Machine Learning](https://arxiv.org/abs/2611.14383v1)

**作者**：Bo Dai, Yilun Du  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-11-10

### 📄 论文摘要

Energy-based models (EBMs) define a distribution through a scalar energy, $p_θ(x)\propto\exp(-E_θ(x))$, and are usually presented as one model family among many. This tutorial has a broader goal: beyond introducing EBMs, it uses them as a single lens that connects the different aspects of machine learning. Any EBM is specified by three choices, the energy, which determines what the model represents; the inference procedure, which samples from or optimizes the energy; and the learning method, which fits the energy to data. We first develop these components, including sampling, variational inference, and learning by maximum likelihood, noise contrastive estimation, pseudolikelihood, score matching, and adversarial training, and show that the learning methods share one contrastive structure. We then show that discriminative models, generative models such as GANs, normalizing flows, diffusion and autoregressive models, representation learning methods such as contrastive learning, word2vec, BERT, denoising auto-encoders, and diffusion representations, reinforcement learning with EBM policies and world models, inverse reinforcement learning, and planning, as well as inference-time computation with verifiers, are all EBMs that differ in these three choices, mostly in how they handle the partition function and sampling. This view explains existing methods, organizes them into a common framework, and suggests new algorithms by replacing one component while keeping the others, with composition of energies as a principled way to combine learned models at inference time.

### 🤖 AI 总结

**一句话总结**：Energy-based models (EBMs) define a distribution through a scalar energy, $p_θ(x)\propto\exp(-E_θ(x))$, and are usually presented as one model family among many. This tutorial has a broader goal: beyo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Energy-Based, Perspective, Machine, Learning, models, EBMs, define

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14383v1) | [下载PDF](https://arxiv.org/pdf/2611.14383v1.pdf)

---

## [6. Cognitive Mapping of Learning by Thinking Mechanisms in Large Language Models](https://arxiv.org/abs/2611.14382v1)

**作者**：Dong Han, Jin Zhang, Kunyue Yang  
**分类**：cs.AI  
**发布时间**：2026-11-10

### 📄 论文摘要

Large language models (LLMs) increasingly exhibit capabilities that resemble human Learning by Thinking (LbT), the acquisition of new insight through internal processes such as explanation and reasoning, without new external input. A systematic account of the cognitive mechanisms behind these capabilities, and of their limits, remains underdeveloped. This paper proposes a Cognitive LbT Framework that maps four mechanisms (Reflective Reasoning, Synthetic Memory Formation, Internal Simulation, and Conceptual Self-Organization) onto computational processes in LLMs. Drawing on representative methods, including chain-of-thought prompting, self-consistency, self-reflection, Tree-of-Thoughts search, Self-Instruct, and self-taught reasoning, the analysis argues that selected methods can functionally approximate aspects of these mechanisms and can improve performance on some tasks without additional labeled examples, although this does not always constitute durable learning in model parameters. For example, Self-Instruct generated approximately 52,000 instructions from 175 seed tasks and reported a 33% absolute improvement on Super-NaturalInstructions (Y. Wang et al., 2023). The same mechanisms also produce characteristic failures, including hallucination diffusion, model collapse, concept drift, and high computational cost. These failures are not isolated technical defects but follow from four structural asymmetries between LLMs and human cognition: the identity of generator and monitor, closed learning loops without external grounding, symbolic rather than sensorimotor simulation, and the cost of inference-time computation. The framework yields testable propositions about when LbT in LLMs should succeed or fail and offers a structured basis for designing more reliable autonomous learning systems.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) increasingly exhibit capabilities that resemble human Learning by Thinking (LbT), the acquisition of new insight through internal processes such as explanation and reasoni...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Cognitive, Mapping, Learning, Thinking, Mechanisms, Large, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14382v1) | [下载PDF](https://arxiv.org/pdf/2611.14382v1.pdf)

---

## cs.CL

## [7. Mechanistic Interpretability Needs a Logic of Inference](https://arxiv.org/abs/2611.14483v1)

**作者**：Zhimin Hu, Chen Jiang, Hanbo Xie 等 5 位作者  
**分类**：cs.CL, cs.CV  
**发布时间**：2026-11-10

### 📄 论文摘要

Neural networks are increasingly studied not merely as predictive systems, but as complex systems whose internal computations are themselves objects of scientific inquiry. Recent progress in mechanistic interpretability (MI) has made it possible to identify neurons, features, circuits, population structures, and dynamical patterns associated with model behavior. As these tools improve, attention is shifting from what can be observed inside a model to how those observations support mechanistic explanations. We examine the parallel efforts of neuroscience and MI to address this question and identify recurring inferential bottlenecks when inferring mechanisms from complex neural systems. We propose five principles and organize them into a recursive logic for a more rigorous procedure of mechanistic inference. These principles provide a framework that supports scientific discovery in two senses: it helps turn local interpretability findings into cumulative knowledge of mechanisms within models, and it makes those mechanisms sufficiently precise to generate testable hypotheses about domains beyond the models. Evidence beyond MI is ultimately required to establish what model mechanisms reveal about the world.

### 🤖 AI 总结

**一句话总结**：Neural networks are increasingly studied not merely as predictive systems, but as complex systems whose internal computations are themselves objects of scientific inquiry. Recent progress in mechanist...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Mechanistic, Interpretability, Needs, Logic, Inference, Neural, networks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14483v1) | [下载PDF](https://arxiv.org/pdf/2611.14483v1.pdf)

---

## [8. Pterodactyl: Pushing the Limits of Efficient Automated Translation Evaluation](https://arxiv.org/abs/2611.14480v1)

**作者**：Evelyn Y. Garland, Carola F. Berger  
**分类**：cs.CL  
**发布时间**：2026-11-10

### 📄 论文摘要

In this paper, we present 1020 Group's submission to the WMT26 shared task on automated quality evaluation. Our system, Pterodactyl, was engineered specifically for subtasks 2 and 3, that is, segment-level quality score prediction and the detection of error-free segments. Pterodactyl is a highly customizable, ultra-low cost system optimized for binary classification in translation triage and data curation. It is based on an LLM-as-a-judge approach, with prompt engineering and model selection guided by ROC analysis. We also developed several variants of Pterodactyl that were specifically adapted for subtasks 3.

### 🤖 AI 总结

**一句话总结**：In this paper, we present 1020 Group's submission to the WMT26 shared task on automated quality evaluation. Our system, Pterodactyl, was engineered specifically for subtasks 2 and 3, that is, segment-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Pterodactyl, Pushing, Limits, Efficient, Automated, Translation, Evaluation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14480v1) | [下载PDF](https://arxiv.org/pdf/2611.14480v1.pdf)

---

## [9. When does text encoding matter for language modeling?](https://arxiv.org/abs/2611.14459v1)

**作者**：Eugene Jang, Catherine Arnett, Terra Blevins  
**分类**：cs.CL  
**发布时间**：2026-11-10

### 📄 论文摘要

UTF-8's role as the de facto encoding standard in language models introduces cross-lingual inequities due to its variable-length design. However, the effect that this encoding choice has on model performance remains largely unexamined. In this work, we investigate how text encoding impacts the performance of byte-level language models, comparing UTF-8 with a wide range of other encoding strategies, including other Unicode-based approaches, language-specific encodings, and our own customized encodings. To facilitate our analysis, we propose Aether: a hybrid encoding scheme that uses script-specific encodings for our target setting while maintaining full Unicode coverage through UTF-8 fallbacks, using this framework to model four orthographically diverse languages. Surprisingly, we find that while languages with information-dense characters (Chinese, Korean) significantly benefit from compressive encodings, languages whose characters carry less information individually (Georgian, Tamil) are largely insensitive to encoding choice. In light of these findings, we argue that text encoding should be a language-specific design decision, rather than a universal default.

### 🤖 AI 总结

**一句话总结**：UTF-8's role as the de facto encoding standard in language models introduces cross-lingual inequities due to its variable-length design. However, the effect that this encoding choice has on model perf...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, does, text, encoding, matter, language, modeling?, UTF-8's

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14459v1) | [下载PDF](https://arxiv.org/pdf/2611.14459v1.pdf)

---

## cs.CV

## [10. Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training](https://arxiv.org/abs/2611.14519v1)

**作者**：Emre Kutlusan, Yongmin Li  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-10

### 📄 论文摘要

Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they will replace models trained for each task. Most comparisons, however, use data from the training distribution and a single task-specific baseline whose configuration is rarely justified, and therefore provide limited evidence of performance at new clinical sites. It also remains unclear how much of a foundation model must be adapted, and what determines this. We adapted a foundation model, DINOv2, with strategies ranging from tuning only its bias terms to full fine-tuning, and compared it with U-Nets and ResU-Nets trained from scratch. Experiments covered colonoscopy, breast ultrasound and dermoscopy, with testing on held-out data from the training source and on independent datasets from other institutions. The adapted foundation model generalised better on every external dataset. Within the training distribution, the task-specific models remained competitive when training data were abundant, and delineated boundaries more precisely, while the foundation model more often missed small lesions. Only a small fraction of the foundation model required adaptation, and the capacity needed was determined by the imaging domain rather than by the adaptation method. A widely used polyp test set was also found to duplicate images from another benchmark. Foundation-model adaptation is therefore warranted where models must work across sites, with capacity selected on the target domain.

### 🤖 AI 总结

**一句话总结**：Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they will replace models trained for each task. Most co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Medical, Image, Segmentation, Foundation, Model, Adaptation, versus, Task-Specific

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14519v1) | [下载PDF](https://arxiv.org/pdf/2611.14519v1.pdf)

---

## [11. Toward Foundation Detection Models via Example-Based Grounding in EM-DETR](https://arxiv.org/abs/2611.14518v1)

**作者**：Sheethal Bhat, Bogdan Georgescu, Awais Mansoor 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-10

### 📄 论文摘要

DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated datasets. In medical lesion detection, the scarcity of comprehensive, stan dardized annotations and the heterogeneity of existing datasets limit the development of robust foundation models. In this work, we introduce a novel approach to building a multi-domain foundation model for le sion detection by integrating diverse medical image datasets annotated for both anatomical structures and abnormalities. We first propose a student-teacher training strategy to effectively combine datasets with heterogeneous label spaces, mitigating catastrophic forgetting, and im proving feature learning. In addition, building on our previously pro posed example-based EM-DETR framework, we adapt it to jointly learn from multiple domain-specific datasets, enabling fine-grained, example driven detection across modalities. Our model achieves state-of-the-art (SOTA) results, with image-level AUC scores exceeding previous SOTA by 1% point on four key findings in CXRs. We achieve a leading mAP50 in CXRs and mammography, surpassing EM-DETR trained on a single dataset by 2-3% points. This approach paves the way for scalable foundation models in medical imaging that leverage heterogeneous data while maintaining robust and generalizable performance.

### 🤖 AI 总结

**一句话总结**：DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated da...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Toward, Foundation, Detection, Models, via, Example-Based, Grounding, EM-DETR

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14518v1) | [下载PDF](https://arxiv.org/pdf/2611.14518v1.pdf)

---

## [12. Measuring Robustness and Efficiency in a Connectome-Constrained Fly Visual System Model: Linking an Adversarial and a Perceptual Illusion](https://arxiv.org/abs/2611.14498v1)

**作者**：Alexandre Garcia-Duran, Alejandro Rodriguez-Garcia, Manuel Molano-Mazón 等 6 位作者  
**分类**：cs.CV, q-bio.NC  
**发布时间**：2026-11-10

### 📄 论文摘要

Biological visual systems compute reliably under tight metabolic and wiring constraints, whereas artificial vision systems consume far more energy and can be sensitive to adversarial perturbations. Whether networks with brain-like wiring are more robust at lower computational cost is unclear. We address this by benchmarking a task-optimized, continuous-time recurrent neural network of the fly visual system constrained by its synaptic connectome (FlyNet) against artificial neural networks. We compare it against CNNs, RAFT, and continuous-time recurrent neural networks without detailed connectome constraints (sCTRNN, CTRNN) on a collision-detection task within a differentiable 3D rendering pipeline. FlyNet is adversarially vulnerable but, relative to its compute, more robust to common video corruptions than RAFT, while using up to five orders of magnitude fewer FLOPs. The CTRNNs remain more robust than FlyNet across almost all tested perturbations, suggesting that connectome constraints benefit efficiency, through their low edge count, over robustness. Recurrence improves robustness to white-box attacks in RAFT and temporal context improves robustness to common corruptions. FlyNet's position and velocity representations degrade under adversarial textures but recover under counterfactual textures that restore correct classification while staying equally far from training, ruling out unfamiliar textures as the cause of failure. The reverse-phi illusion similarly disrupts these representations and inverts the same low-level motion statistic as the adversarial textures. Optimizing this input statistic alone, without access to the network, suffices to induce classification failure, attributing both perturbations to the same circuit vulnerability. Connectome-constrained models can thus surface adversarial failure mechanisms as testable hypotheses about biological perceptual vulnerabilities.

### 🤖 AI 总结

**一句话总结**：Biological visual systems compute reliably under tight metabolic and wiring constraints, whereas artificial vision systems consume far more energy and can be sensitive to adversarial perturbations. Wh...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Measuring, Robustness, Efficiency, Connectome-Constrained, Fly, Visual, System, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14498v1) | [下载PDF](https://arxiv.org/pdf/2611.14498v1.pdf)

---

## [13. RS-JEPA: Remote Sensing Joint-Embedding Predictive Architecture with Scan-Path Views for Cross-Sensor Image Retrieval](https://arxiv.org/abs/2611.14496v1)

**作者**：Tanishq Rachamalla, Srishti Kaushik, Muhammad Attique Khan 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-10

### 📄 论文摘要

Cross-sensor remote sensing image retrieval aims to find scenes with the same content across heterogeneous sensors, such as SAR and optical or panchromatic (PAN) and multispectral (MS) imagery, without manual labels. Existing self-supervised methods either reconstruct sensor-specific pixel detail, align each image only with its co-registered twin, or rely on large transformers with 118-173M parameters (and up to 398M). We introduce RS-JEPA, a compact joint-embedding predictive framework built on a Vision Mamba encoder shared by both sensors. Since a state-space encoder reads an image as an ordered sequence of patches, we propose scan-path views, which treat two reading orders of the same image as two views with identical pixels and predict the hidden patches in one order from the visible patches in the other.To keep this prediction challenging, we propose Adversarial View Coupling (AVC), which learns the hardest split of the visible patches, and a neighbourhood consensus loss that aligns the scene similarities of both sensors. Extensive experiments on SAR-optical (BEN-14K, CBRSIR-VS) and PAN-MS (DSRSID) benchmarks demonstrate that RS-JEPA achieves the highest F1@5 among twelve re-implemented methods (72.92, 80.35 and 94.43) with a retrieval network of only 3.88M parameters (14.57M in training, 8-16times fewer than prior JEPA retrievers). Like prior methods, RS-JEPA trains on co-registered pairs. Our results highlight reading order as a source of self-supervised views. code: https://github.com/Tanishq251/RSJEPA.

### 🤖 AI 总结

**一句话总结**：Cross-sensor remote sensing image retrieval aims to find scenes with the same content across heterogeneous sensors, such as SAR and optical or panchromatic (PAN) and multispectral (MS) imagery, withou...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RS-JEPA, Remote, Sensing, Joint-Embedding, Predictive, Architecture, Scan-Path, Views

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14496v1) | [下载PDF](https://arxiv.org/pdf/2611.14496v1.pdf)

---

## [14. BoviShift: A Six-Year Multi-Attribute Audit of Visual Cattle Phenotyping Across Animals and Time](https://arxiv.org/abs/2611.14476v1)

**作者**：Mobasshir Bhuiya Shagor, Nilambar Halder Tonmoy, Md Saef Ullah Miah  
**分类**：cs.CV  
**发布时间**：2026-11-10

### 📄 论文摘要

Computer vision offers a scalable, non-contact means of estimating livestock traits, but correlated images and video frames make reliable evaluation difficult. Image-random splitting can place views of the same animal in both training and test sets, while deployment further requires transfer to animals captured in future years. We introduce BoviShift, a corpus reconstructed from six consecutive annual cohorts of an operational cattle marketplace collected from 2021 to 2026. It contains 2{,}657 cattle, 10{,}610 still images, and 2{,}566 walk-around videos across nine recorded breed categories. We evaluate three splitting strategies through four configurations: image-random and pooled cattle-disjoint splits over the same development cohorts, followed by separate future-2025 and locked future-2026 evaluations. Using a fixed ResNet-50 multi-task baseline, we assess weight, age, height, breed, and coat color. Differences between image-random and cattle-disjoint splitting are task-dependent rather than a universal leakage penalty. Future-cohort behavior is also attribute- and cohort-specific: breed declines relative to pooled evaluation; mean weight and age performance fails to beat constant baselines in 2025; height remains above baseline; and color transfers well to 2025 but degrades in 2026. Multi-task training improves all five point estimates in a single-seed ablation, still-view aggregation helps selectively, and zero-shot video-frame aggregation exposes a still-to-video domain gap. To our knowledge, BoviShift is the longest-spanning cattle-vision resource combining consecutive annual cohorts with physical and visual attributes.

### 🤖 AI 总结

**一句话总结**：Computer vision offers a scalable, non-contact means of estimating livestock traits, but correlated images and video frames make reliable evaluation difficult. Image-random splitting can place views o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, BoviShift, Six-Year, Multi-Attribute, Audit, Visual, Cattle, Phenotyping

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14476v1) | [下载PDF](https://arxiv.org/pdf/2611.14476v1.pdf)

---

## [15. UGG: Unified Generative Geometry Model](https://arxiv.org/abs/2611.14440v1)

**作者**：Amani Kiruga, Zhiyi Li, Ruojin Cai 等 7 位作者  
**分类**：cs.CV, cs.LG, cs.RO  
**发布时间**：2026-11-10

### 📄 论文摘要

Understanding 4D scenes is a core challenge in visual intelligence, requiring models to jointly capture scene geometry, appearance, and dynamics from partial observations. However, existing approaches are subdivided into feedforward models for direct geometric prediction, and generative models for visual synthesis. We introduce UGG, a unified framework for 4D scene understanding that jointly models RGB video and geometric representations such as depth and camera pose. By assigning different noise levels across modalities and time, UGG formulates visual generation and geometric prediction as conditional completion within a single generative model. This flexible formulation enables the model to learn from diverse, heterogeneous datasets with different subsets of geometric and visual annotations. Furthermore, our generative formulation enables inference-time search over multiple plausible scene hypotheses, using geometric evidence extracted from observed RGB frames to improve geometric prediction without ground truth geometry. We demonstrate UGG's effectiveness over non-unified baselines across camera-controlled video generation, depth estimation, and camera pose prediction, including in challenging sparse observation settings. Code and visualizations are available at https://ugg-model.github.io/

### 🤖 AI 总结

**一句话总结**：Understanding 4D scenes is a core challenge in visual intelligence, requiring models to jointly capture scene geometry, appearance, and dynamics from partial observations. However, existing approaches...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, UGG, Unified, Generative, Geometry, Model, Understanding, scenes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14440v1) | [下载PDF](https://arxiv.org/pdf/2611.14440v1.pdf)

---

## [16. Metric-Aligned Group Relative Policy Optimization for Explainable Deepfake Detection](https://arxiv.org/abs/2611.14436v1)

**作者**：Luka Dragar, Peter Peer, Vitomir Štruc 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-10

### 📄 论文摘要

Deepfake detectors are commonly evaluated on real/fake classification alone, but real-world applications require explanations of the visual evidence behind each prediction. Joint vision-language models struggle with authenticity assessment, producing "real" narratives for manipulated images. To address this, we propose a decoupled predict-then-explain pipeline as our submission to the ACM Multimedia 2026 Explainable Deepfake Detection Challenge, with methods trained and evaluated on the XPlainVerse benchmark. A vision-foundation-model ensemble first classifies the image, then a Qwen3-VL-8B model generates a decision-conditioned explanation of the visual evidence. For fake images, a second Qwen3-VL-8B compresses that text into a short non-expert summary without using the image. We further apply metric-aligned Group Relative Policy Optimization (GRPO) to optimize both explainers against the challenge criteria. Under matched conditions, GRPO raises complex BERTScore-F1 from 0.686 to 0.712 and also improves grounding (entity and evidence F1); our submission ranked first on complex BERTScore-F1 and seventh overall.

### 🤖 AI 总结

**一句话总结**：Deepfake detectors are commonly evaluated on real/fake classification alone, but real-world applications require explanations of the visual evidence behind each prediction. Joint vision-language model...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Metric-Aligned, Group, Relative, Policy, Optimization, Explainable, Deepfake, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14436v1) | [下载PDF](https://arxiv.org/pdf/2611.14436v1.pdf)

---

## [17. What Factors Matter for Collection-Level Counting with Human-AI Collaboration?](https://arxiv.org/abs/2611.14380v1)

**作者**：Seoyun Jeong, Logan Lawrence, Owen L. Martin 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-10

### 📄 论文摘要

Many scientific and policy decisions require estimating the total number of target objects across a large image collection. Exhaustive human labeling is often infeasible, while raw model predictions can be biased, especially under domain shift. Recent human-AI estimation methods combine imperfect model predictions with limited human verification to obtain reliable collection-level estimates. However, existing work provides little guidance on how practitioners should choose among models, estimators, and adaptation strategies for a new deployment. We study these choices within a common human-in-the-loop counting framework across 12 tasks spanning biomedical microscopy, ground-level and aerial wildlife surveys, and overhead imagery of urban structures. Our results show that modern multimodal models provide a strong, training-free starting point for many tasks, while fine-tuned detectors become more advantageous at larger labeling budgets and across repeated deployments. Estimation efficiency improves further when model predictions are used to prioritize which units humans label, rather than sampling uniformly. We also find that each model's ranking quality can be estimated with a small pilot set, yielding practical guidance for selecting strategies on new counting tasks. In a field deployment on aerial pronghorn surveys, a task-specific adaptation of these methods meets the survey's $\pm 5\%$ tolerance after reviewing a median of only $3.2\%$ of collected images.

### 🤖 AI 总结

**一句话总结**：Many scientific and policy decisions require estimating the total number of target objects across a large image collection. Exhaustive human labeling is often infeasible, while raw model predictions c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：What, Factors, Matter, Collection-Level, Counting, Human-AI, Collaboration?, Many

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14380v1) | [下载PDF](https://arxiv.org/pdf/2611.14380v1.pdf)

---

## cs.LG

## [18. TorchCurves: Differentiable Parametric Curves](https://arxiv.org/abs/2611.14516v1)

**作者**：Alex Shtoff  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-11-10

### 📄 论文摘要

We present TorchCurves, a PyTorch library that treats vector-valued parametric curves as learnable primitives. Its central operation maps batches of scalar inputs to points on curves represented in B-spline or Legendre polynomial bases, with differentiation through both inputs and coefficients. Curve coefficients can be optimized jointly with the surrounding model or produced by another network. The library provides trainable modules, reusable basis modules, and a functional interface, supporting applications ranging from continuous feature embeddings to Kolmogorov-Arnold networks and functional regression. Its implementation combines classical evaluation algorithms with vectorized PyTorch operations, emphasizing readability and maintainability without custom hardware kernels. Timing experiments compare curve evaluation against NumPy and SciPy and KAN training against EfficientKAN across a range of problem sizes. The results illustrate where this generality remains computationally practical and where overhead is substantial. Library is available on GitHub at https://github.com/alexshtf/torchcurves.

### 🤖 AI 总结

**一句话总结**：We present TorchCurves, a PyTorch library that treats vector-valued parametric curves as learnable primitives. Its central operation maps batches of scalar inputs to points on curves represented in B-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, TorchCurves, Differentiable, Parametric, Curves, present, PyTorch, library

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14516v1) | [下载PDF](https://arxiv.org/pdf/2611.14516v1.pdf)

---

## [19. AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models](https://arxiv.org/abs/2611.14515v1)

**作者**：Zijian Zhang, Rizhen Hu, Jiangweizhi Peng 等 7 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-11-10

### 📄 论文摘要

Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way to turn this information into guidance, but their design and adaptation are largely left to humans and tailored to specific domains. We introduce AutoScaffold, a unified AI-for-AI framework that turns a student's training experience into adaptive scaffolds, with minimal domain-specific information and no human intervention during training. A frozen teacher periodically examines this experience, diagnoses bottlenecks, and designs scaffolds in two forms: (i) strategies shared across a class of tasks and (ii) hints for individual hard tasks, adjusting the content and amount of support as the student learns. The scaffolds are removed at evaluation. We apply the same framework to ALFWorld, search-based QA, mathematical reasoning, and GPU kernel generation. When evaluated without scaffolds, students trained with AutoScaffold outperform those trained with the corresponding RL baselines in all four domains, with gains of 7.2 points in ALFWorld success and 4.0 points in average QA exact match. On GPU kernel generation, AutoScaffold increases the fraction of tasks with a correct kernel that runs faster than the PyTorch reference by up to 5.0 points. On math, our student surpasses QuestA's reported accuracy using approximately one-third as many student training steps. Analyses show that the teacher identifies a different failure in each task class and shifts its scaffolds from step-by-step workflows to targeted fixes as the student improves, and that its revised scaffolds help the student learn more than keeping the previous scaffold or using no scaffold.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, AutoScaffold, AI-Guided, Scaffolding, Reinforcement, Learning, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14515v1) | [下载PDF](https://arxiv.org/pdf/2611.14515v1.pdf)

---

## [20. Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](https://arxiv.org/abs/2611.14511v1)

**作者**：Megha Srivastava, Michael H. Lim, Allison M. Keys 等 5 位作者  
**分类**：cs.LG, q-bio.QM  
**发布时间**：2026-11-10

### 📄 论文摘要

Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains challenging. We introduce Pyrite, a pairwise pose-ranking benchmark comprising 1,500 pose pairs across diverse protein-ligand complexes. Expert chemists equipped with 3D visualization tools and physics-based scores perform near chance, highlighting the difficulty of interpreting available chemical signals. To investigate automated ranking, we introduce PyriteRep, a structured representation of molecular geometry, protein-ligand interactions, and physicochemical scores, and develop two LLM-based agents: PyriteReasoner, which directly compares poses through text-based reasoning, and PyriteFeaturizer, which generates executable code to construct features for logistic regression, optionally incorporating features derived from LLM subcalls. These agents achieve up to 67% and 74% accuracy, respectively, exceeding observed expert performance. LLM-guided feature discovery generally outperforms direct reasoning, while Group Relative Policy Optimization (GRPO) improves open-weight models, enabling them to match or surpass closed-source frontier models in our evaluations. These results establish Pyrite as a challenging test of pose-ranking ability and highlight LLM-guided feature discovery as a promising approach to interpret and combine the outputs of computational chemistry tools.

### 🤖 AI 总结

**一句话总结**：Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains cha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Pyrite, Building, Benchmarking, Protein-Ligand, Pose, Ranking, Predicting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14511v1) | [下载PDF](https://arxiv.org/pdf/2611.14511v1.pdf)

---

## [21. When Does the Real Wiring Win? Testing connectome structure-function claims against unmeasured physiology](https://arxiv.org/abs/2611.14508v1)

**作者**：Yeyuan Liu  
**分类**：cs.LG, q-bio.NC  
**发布时间**：2026-11-10

### 📄 论文摘要

Connectome-constrained models are often used to argue that a measured wiring diagram outperforms shuffled or rewired wiring, and hence that structure shapes function. Such comparisons can confound wiring with how the models are tuned: a connectome fixes who connects to whom, not the excitability, gains or plasticity rates the model also needs, and modellers often tune these until the real-wiring model works. We separate three estimands: physiology tuned on the real wiring and transferred to nulls (P1), each wiring tuned on its own (P2), and P2 restricted to physiology consistent with independent data (P3). The biases involved are known in machine learning (under-tuned baselines, inherited weights, winner's curse); we measure what they do to biological conclusions, using synthetic ground truth, placebo nulls and three Drosophila circuit models. Some claims survive every protocol we test: segregated reward and punishment dopamine improves learning, and head-direction topography is required for a persistent bump. Others do not. In the mushroom body, the real Kenyon-cell output wiring beats a cross-subtype identity shuffle by 0.09 under P1 and P2 but loses to it by 0.09 under P3 (95% CIs exclude zero; held-out runs confirm). The verdict is set by the share of alpha'beta' cells among active Kenyon cells, which P1 selects low; at the share implied by imaging (about 44%) the real-wiring model fails to learn, exposing a model inadequacy rather than a deficit of the fly's wiring. In flyvis, P1 penalises a mirrored connectome, which has a constructed solution within 0.07 (median) of the real error, more than a spatially shuffled one in 50 of 50 members; the ranking survives ten-fold longer retraining but depends on the checkpoint at fifty-fold. A credible structural claim needs matched optimisation, data-constrained physiology and a model that still works there.

### 🤖 AI 总结

**一句话总结**：Connectome-constrained models are often used to argue that a measured wiring diagram outperforms shuffled or rewired wiring, and hence that structure shapes function. Such comparisons can confound wir...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Does, Real, Wiring, Win?, Testing, connectome, structure-function

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14508v1) | [下载PDF](https://arxiv.org/pdf/2611.14508v1.pdf)

---

## [22. Continual-ARC: Measuring Skill Acquisition over a Working Lifetime](https://arxiv.org/abs/2611.14505v1)

**作者**：Daniel Lenton  
**分类**：cs.LG  
**发布时间**：2026-11-10

### 📄 论文摘要

Agent harnesses have emerged as a promising mechanism for continual learning, alongside test-time parametric learning. However, the current benchmarks have several limitations: they generally focus on a single applied domain, serve each instance only once, and assume a single family of learner, so memory-based and weight-based systems are rarely compared on the same scale. We propose Continual-ARC, a lifelong stream built from the three ARC-AGI editions, whose tasks need no domain knowledge. The same tasks return after dormant gaps with fresh instances, while new tasks keep arriving. On each instance, the learner may pay for demonstrations, submit answers, or act inside the harness, with retries permitted on incorrect submissions, which are paid for. Each instance is scored based on the share of this feedback budget consumed. Since a learner may keep anything between instances, memory-based and weight-based systems are scored on the same scale. After the stream, the learner is frozen and tested on fresh instances of the tasks it met, which measures memorization, and on unseen tasks, which measures generalization. We run an agent harness with frozen weights, with and without persistence, on Qwen3.5-9B and GLM-5.3 Flash, comparing them with two prompting floors, a program-induction method and Qwen3.5-9B's weights trained to imitate GLM-5.3 Flash. Persistence in the harness generally does not improve memorization unless provided with explicit expert guidance. Most harness-based methods still learn less than a floor that simply caches each task's demonstrations, across all models we tested. No harness-based method gains on unseen tasks, whereas weight-based learning shows substantial gains. This opens the door to future weight-based continual learning that could teach models to drive harnesses in new domains.

### 🤖 AI 总结

**一句话总结**：Agent harnesses have emerged as a promising mechanism for continual learning, alongside test-time parametric learning. However, the current benchmarks have several limitations: they generally focus on...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Continual-ARC, Measuring, Skill, Acquisition, over, Working, Lifetime

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14505v1) | [下载PDF](https://arxiv.org/pdf/2611.14505v1.pdf)

---

## [23. TimeSeek: Multi-Task and Multi-Domain Pretraining for Generalized Time Series Analytics](https://arxiv.org/abs/2611.14491v1)

**作者**：Peng Chen, Yihang Wang, Zhongwen Rao 等 9 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-10

### 📄 论文摘要

Time series analytics has been widely applied across various domains. While existing time series foundation models (TSFMs) have demonstrated promising results, they still face two major challenges: 1) Most TSFMs mainly rely on stacking Transformer layers to increase parameter size, lacking the ability to adaptively model complex time series patterns from multi-domain data. 2) Current TSFMs are primarily pre-trained for specific tasks, e.g., forecasting or anomaly detection, and a few models support multiple tasks, but they fail to fully leverage task specificity and commonality, resulting in suboptimal performance. To address these challenges, we propose TimeSeek, a novel generalized time series analytics model that adaptively models time series patterns from multi-domain data and unifies multiple tasks in pre-training. Conceptually, TimeSeek is guided by selective information sharing under domain and task heterogeneity. From the perspective of multi-domain data, we propose a Multi-Domain Feature Extractor that adaptively captures temporal dependencies and channel correlations based on domain-specific characteristics, including progressive multi-scale modeling and adaptive slot channel modeling. From the perspective of the diversity of tasks, we propose multi-task collaborative training, which leverages task specificity and task commonality through task customization and cross-task training, effectively unifying multiple tasks in pre-training and better adapting to diverse downstream scenarios. After pre-training on large-scale time series data, TimeSeek achieves state-of-the-art performance in forecasting, anomaly detection, and classification tasks across both few-shot learning and zero-shot situations, together with favorable inference efficiency.

### 🤖 AI 总结

**一句话总结**：Time series analytics has been widely applied across various domains. While existing time series foundation models (TSFMs) have demonstrated promising results, they still face two major challenges: 1)...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TimeSeek, Multi-Task, Multi-Domain, Pretraining, Generalized, Time, Series, Analytics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14491v1) | [下载PDF](https://arxiv.org/pdf/2611.14491v1.pdf)

---

## [24. A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets](https://arxiv.org/abs/2611.14467v1)

**作者**：Audrey Huang, Nan Jiang, Sham M. Kakade 等 6 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-11-10

### 📄 论文摘要

Policy optimization is central to language model post-training, yet principled guidance remains limited. We revisit its theoretical foundations to identify algorithms that learn near-optimal policies using total samples and gradient steps governed by the base model's response coverage, a measure of how readily it generates optimal responses. We call such algorithms coverage-preserving. This guarantee captures the goal of amplifying capabilities accessible through sampling from the base model.   (1) Coverage collapse. REINFORCE, the basis for PPO and GRPO, can drive the probability of optimal responses to near zero, even as reward improves. This coverage collapse stalls optimization, and convergence can require exponentially many steps despite good initial coverage. The failure arises even with exact gradients and persists under KL regularization to the base model.   (2) Reference resets. We show that repeatedly resetting the KL reference to the most recent policy mitigates coverage collapse. We formalize this intervention in Approximate Policy Mirror Descent (APMD), a meta-algorithm that approximately solves a sequence of KL-regularized RL subproblems. APMD enables stronger regularization, making each subproblem easier to solve, while reference resets allow convergence to global optimality.   (3) Coverage-preserving algorithms. For softmax linear policies over pretrained features, we use APMD to establish the first global convergence guarantees showing that widely used families of post-training algorithms are coverage-preserving. These include stylized PPO and GRPO variants with explicit KL regularization and reference resets, and squared-loss algorithms that implement them implicitly, including those used to train the Kimi models.   These results clarify how regularization, clipping, and objective choice affect the sampling and optimization costs of post-training.

### 🤖 AI 总结

**一句话总结**：Policy optimization is central to language model post-training, yet principled guidance remains limited. We revisit its theoretical foundations to identify algorithms that learn near-optimal policies ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Theory, Policy, Optimization, Post-Training, Coverage, Collapse, Reference

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14467v1) | [下载PDF](https://arxiv.org/pdf/2611.14467v1.pdf)

---

## [25. Accurate predictions of properties of energetic materials with tabular foundation models](https://arxiv.org/abs/2611.14462v1)

**作者**：Vagn Krister Nes Glomsrud, Mathias Bynke, Lars Henry Berge Olsen 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-10

### 📄 论文摘要

We use TabPFN, a recently developed tabular foundation model, to predict three properties of energetic materials: impact sensitivity, decomposition temperature and crystal density. Without any hyperparameter tuning, TabPFN outperforms the best published models for all three properties. It also substantially outperforms a wide range of established machine-learning models, including tuned gradient boosting (XGBoost), random forests and Gaussian processes. This holds both when the models are given hand-crafted molecular descriptors and when they are given learned representations from Chemprop's message-passing neural network. In particular, for all three properties, TabPFN applied to Chemprop's own embedding is more accurate than Chemprop's predictions. TabPFN is also among the fastest models we consider, more than an order of magnitude faster than XGBoost. As TabPFN predicts the entire distribution of the target rather than just a single value, it offers built-in uncertainty quantification, which we compare with the empirical distributions of compounds with repeated measurements. Finally, we interpret the predictions using Shapley values, which rank the features by their importance.

### 🤖 AI 总结

**一句话总结**：We use TabPFN, a recently developed tabular foundation model, to predict three properties of energetic materials: impact sensitivity, decomposition temperature and crystal density. Without any hyperpa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Accurate, predictions, properties, energetic, materials, tabular, foundation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14462v1) | [下载PDF](https://arxiv.org/pdf/2611.14462v1.pdf)

---

## [26. Quantifying the Sampling Frequency Invariance of Time-Series Foundation Models for Sensor Data Applications](https://arxiv.org/abs/2611.14425v1)

**作者**：Sourish Gunesh Dhekane, Abinaya Kumar, Torsten Woertwein 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-10

### 📄 论文摘要

Time-Series Foundation Models (TSFMs) are increasingly used in sensor applications, where sampling frequency (SF) varies across sensors, devices, and operating modes (e.g., power saving). Ideally, TSFMs must remain effective during such SF changes, provided the SF retains task-critical bandwidth. In this paper, we stress-test 4 prominent TSFMs: MOMENT, Chronos-2, Moirai-MoE, and TimesFM, to quantify their SF-invariance and investigate whether their behavior tracks the resulting loss of information bandwidth rather than the SF value itself. Our stress-test probes 3 dimensions: (i) the shift in embeddings, (ii) the degradation in forecasting performance, and (iii) the degradation in downstream performance, quantified by three novel metrics: FSI, FDI, and CDI, respectively. To our knowledge, this is the first study to place SF-invariance at the core of TSFM evaluations. Our results characterize: (i) how SF-invariance depends on the margin between signal's native-SF and the bandwidth its task requires, (ii) how much of that invariance the choice of TSFM explains, and (iii) how much of TSFM's performance degradation under a lower SF reflects information loss rather than a limitation of their abilities. These findings reframe SF-invariance as a measurable, signal-aware property of the (signal X TSFM) pair, and guide practitioners on when TSFMs display SF-invariance.

### 🤖 AI 总结

**一句话总结**：Time-Series Foundation Models (TSFMs) are increasingly used in sensor applications, where sampling frequency (SF) varies across sensors, devices, and operating modes (e.g., power saving). Ideally, TSF...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Quantifying, Sampling, Frequency, Invariance, Time-Series, Foundation, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14425v1) | [下载PDF](https://arxiv.org/pdf/2611.14425v1.pdf)

---

## [27. DnNP: Denoising Input Uncertainty in Neural Processes](https://arxiv.org/abs/2611.14424v1)

**作者**：Fatemeh Tohidian, Chengzhi Shi, Soomi Lee 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-10

### 📄 论文摘要

Neural Processes (NPs) are flexible meta-learning models capable of uncertainty quantification across diverse applications. However, the standard NP framework assumes access to noise-free inputs. This is unrealistic in many practical settings, where sensor noise or measurement errors are unavoidable. This discrepancy between model assumptions and real-world data can significantly degrade prediction quality and uncertainty estimates. We introduce Denoising Neural Processes (DnNPs), a principled extension of the NP framework that explicitly models input uncertainty. We train DnNPs via variational inference. DnNPs jointly learn to denoise corrupted inputs and perform meta-learning, making them robust to noisy training data. We demonstrate DnNPs' effectiveness on both synthetic and real-world datasets, showing consistent improvements in prediction and uncertainty quantification compared to standard NPs. On PM2.5 spatial interpolation from real-world air quality sensors, DnNP reduces RMSE by up to 30% and NLL by up to 73% relative to standard NPs. We also provide theoretical grounding: we show that the Bayes-optimal predictor under noisy inputs belongs to the DnNP model class, and that plug-in models with fixed observation variance incur an irreducible KL divergence gap that DnNP provably avoids.

### 🤖 AI 总结

**一句话总结**：Neural Processes (NPs) are flexible meta-learning models capable of uncertainty quantification across diverse applications. However, the standard NP framework assumes access to noise-free inputs. This...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DnNP, Denoising, Input, Uncertainty, Neural, Processes, NPs, flexible

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14424v1) | [下载PDF](https://arxiv.org/pdf/2611.14424v1.pdf)

---

## [28. Causal Concept Explanations for Deep Neural Models](https://arxiv.org/abs/2611.14407v1)

**作者**：Josh Rountree, Pulkit Verma, Oswin So 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-10

### 📄 论文摘要

Concept-based explanations in neural models are important for the development, certification, and adoption of autonomous systems. Yet, interpretability remains correlational. Without methods to guide and quantify causal relationships between explanations, a concept explanation can be provided without being necessary or sufficient for the observed output thereby appearing correct while misleading. We introduce Causal Concept Wrapper Network (CCW-Net), the first use of interventional mediation analysis from fields such as economics, medicine, and epidemiology as a training objective to align causal effects of concept-based explanations with a model's output. We further apply mediation analysis as an evaluation tool to quantify, per concept label combination, how much of any model's output is causally attributable to each concept explanation. As a training objective, CCW-Net shapes a model's concept representations such that they are both necessary and sufficient for the outputs they are credited with and independent of other concepts' contributions. Counterfactual concept representations anchor a set of causal alignment criteria: necessity, sufficiency, and independence. Necessity drives irrelevant concept effects toward zero, sufficiency ensures relevant concept representations fully reconstruct a model's output, and independence enforces the total effect decomposes linearly across concepts. We evaluate CCW-Net across aircraft control, driving, and image classification. CCW-Net provides a step toward concept-based explanations that are not merely interpretable, but quantifiably causal, supporting safer evaluation, certification, and deployment of transparent and trustworthy neural models.

### 🤖 AI 总结

**一句话总结**：Concept-based explanations in neural models are important for the development, certification, and adoption of autonomous systems. Yet, interpretability remains correlational. Without methods to guide ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Causal, Concept, Explanations, Deep, Neural, Models, Concept-based, important

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14407v1) | [下载PDF](https://arxiv.org/pdf/2611.14407v1.pdf)

---

## [29. Discovering Equations for the Thermodynamics of South Asian Monsoon Precipitation](https://arxiv.org/abs/2611.14401v1)

**作者**：Savannah L. Ferretti, Jane W. Baldwin, Michael S. Pritchard 等 4 位作者  
**分类**：cs.LG, physics.ao-ph  
**发布时间**：2026-11-10

### 📄 论文摘要

South Asian monsoon precipitation depends on the thermodynamic structure of the lower troposphere, but how its ingredients combine to shape precipitation remains unclear, partly because this dependence is nonlocal in the vertical. We use symbolic distillation, which combines neural networks and symbolic regression, to discover interpretable precipitation equations from 21 years of June-August reanalysis data. Neural networks first learn the vertical thermodynamic structure most relevant to precipitation, condensing each variable into a single interpretable feature not tied to a particular vertical grid. Then, symbolic regression derives closed-form equations from these features and the surface state. Our best equation explains 1.5 times as much precipitation variance as a widely used buoyancy-based diagnostic and recovers about 85% of neural network skill while using about a thousand times fewer parameters. Unlike the buoyancy diagnostic, which adds moisture and instability, the equations treat them as competing controls, with the heaviest precipitation occurring when the lower free troposphere is humid. Over ocean, sensible heating is associated with additional precipitation mainly when near-surface air is warm and moist, improving predicted precipitation and its diurnal cycle. Although the learned features were optimized only for precipitation prediction, the equations largely respond to each feature as expected from convective physics, consistent with the reanalysis. These responses reduce the dependence of monsoon precipitation on the entire vertical column to a few simple, testable constraints that could guide data-driven precipitation models to make them more physically consistent.

### 🤖 AI 总结

**一句话总结**：South Asian monsoon precipitation depends on the thermodynamic structure of the lower troposphere, but how its ingredients combine to shape precipitation remains unclear, partly because this dependenc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Discovering, Equations, Thermodynamics, South, Asian, Monsoon, Precipitation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14401v1) | [下载PDF](https://arxiv.org/pdf/2611.14401v1.pdf)

---

## [30. A Margin Perspective on LoRA: Robustness to Catastrophic Forgetting and Adapter Merging (MaLoRA)](https://arxiv.org/abs/2611.14397v1)

**作者**：Ziqing Xu, Hancheng Min, Lachlan Ewen MacDonald 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-10

### 📄 论文摘要

Low-rank adaptation (LoRA) is the de facto method for parameter-efficient fine-tuning of large neural networks, achieving strong task adaptation with minimal trainable parameters and low optimization cost. Beyond this efficiency, practitioners have observed two striking properties: \textit{robustness to catastrophic forgetting} and the ability to \textit{merge independently trained adapters} into a single model that performs competitively across multiple tasks. These properties are central to continual and multi-task learning, yet remain poorly understood. In this work, we provide a theoretical explanation through a unified \textit{margin-based perspective}. We analyze LoRA in multiclass linear classification under a near-orthogonal task regime with $\ell_2$-regularization, and characterize the optimal LoRA adapter across regularization regimes. Our analysis shows that, in an intermediate regime of regularization parameters, the optimal adapter aligns with the \emph{max-margin solution} on the fine-tuning data. Building on this characterization, we derive two key consequences. First, we obtain closed-form expressions for the margins on pre-training and fine-tuning data, revealing a precise margin trade-off: the regularization parameter controls the balance between retention and adaptation. Second, we analyze adapter merging, proving that merged models achieve positive margin on each task and deriving optimal mixing coefficients that balance margins across tasks and maximize the margin over their union. These results lead to a simple, training-free merging rule, which we term \textit{margin-based LoRA merging} (MaLoRA). Experiments on modern architectures and real datasets validate our theoretical predictions, showing that MaLoRA matches or outperforms several adapter-merging baselines across a range of vision and language classification tasks.

### 🤖 AI 总结

**一句话总结**：Low-rank adaptation (LoRA) is the de facto method for parameter-efficient fine-tuning of large neural networks, achieving strong task adaptation with minimal trainable parameters and low optimization ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Margin, Perspective, LoRA, Robustness, Catastrophic, Forgetting, Adapter, Merging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.14397v1) | [下载PDF](https://arxiv.org/pdf/2611.14397v1.pdf)

---

