# arXiv AI 论文日报 | 2026-08-20

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (9 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.CL](#csCL) (4 篇)
- [cs.AI](#csAI) (7 篇)

---

## cs.AI

## [1. Beyond the Transcript: Detecting Covert Co ordination in Latent Multi-Agent Communication](https://arxiv.org/abs/2608.19161v1)

**作者**：Ramneet Kaur, Pradyumna Chari, Ramesh Raskar 等 6 位作者  
**分类**：cs.AI, cs.CR  
**发布时间**：2026-08-19

### 📄 论文摘要

Language-model agents can communicate through continuous hidden states that are invisible in public transcripts, creating opportunities for covert harmful coordination. We introduce Verifiable Latent Alignments (VLA), an activation-aware framework for monitoring and steering these private communication channels. For every monitored decision, VLA links the private latent-state record and channel status to the resulting public action using a shared event identifier, enabling matched causal analysis. Our first contribution is a neutral-only three-layer monitor combining representation anomaly detection, counterfactual action-distribution influence, and sparse-autoencoder interpretation support. Our second contribution is a steerability framework spanning black-box behavioral instructions and white-box matched-neutral counterfactuals. Our third contribution is an evaluation on a controlled multi-agent auction benchmark covering homogeneous and heterogeneous model pairs, many-agent scalability, and intervention effectiveness. The sequential monitor achieves mean area under the receiver operating characteristic curve (AUROC) of 0.993 for homogeneous agents and 0.854 for heterogeneous pairs when text- and latent-collusion rows are pooled as positives. In Qwen3-0.6B auctions with 25-100 bidders, monitoring requires only a small normalized load relative to all possible directed pairs, while full white-box steering achieves 100% bid-distribution recovery and reduces collusive low-bid behavior by 47.3 percentage points. Because full white-box steering replays the matched neutral counterfactual, its exact recovery is a sanity check by construction. Overall, the controlled study shows that the evaluated private channel attacks can be monitored without training the primary monitor on attack examples and mitigated when matched counterfactual access is available.

### 🤖 AI 总结

**一句话总结**：Language-model agents can communicate through continuous hidden states that are invisible in public transcripts, creating opportunities for covert harmful coordination. We introduce Verifiable Latent ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Co, Multi-Agent, Beyond, Transcript, Detecting, Covert, ordination, Latent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19161v1) | [下载PDF](https://arxiv.org/pdf/2608.19161v1.pdf)

---

## [2. Grouping the Stochastic Machine: Precision, Not Capability, as the Frontier Metric for AI Systems](https://arxiv.org/abs/2608.19140v1)

**作者**：George Andrikopoulos  
**分类**：cs.AI, cs.CY, cs.LG, cs.SE  
**发布时间**：2026-08-19

### 📄 论文摘要

Frontier language models are compared, marketed, and benchmarked on capability -- what their best or average output can achieve. I argue this measures the wrong axis. The models have saturated accuracy: their mean output lands on the target. What now separates one system from another in practice is precision: how tightly concentrated their outputs are around that target across repeated, identical requests. Borrowing the marksman's distinction, capability is where the average shot lands; reliability is the size of the group. I make three claims. First, precision, not capability, is the frontier differentiator between systems, and benchmark culture systematically fails to measure it, reporting central tendency rather than spread. Second, precision is measurable, cheaply and without circularity, by running a fixed suite of deterministically scored tasks many times at fixed temperature and computing the per-task consistency of outcomes -- no model-in-the-loop grader required. Third, the measurement is not merely descriptive but decision-guiding: it separates consistent failures (a tight group off-centre, correctable by the operating discipline of Paper 1 -- a sight adjustment) from scattered failures (a wide group, correctable only by changing the model or its sampling -- a rifle problem). I define a grouping metric, specify a harness, and show how tracking a human-AI pair's grouping over time yields the compounding signal that Paper 1's field study requires. A first real run, since replicated, illustrates both the method and its most important limit: one measured gap was closed completely by a single rule (0/5 -> 5/5), while a suite of tasks authored from the rules themselves found no value, because a frontier model already embodies explicit good practice -- establishing that a discipline's worth is found by measurement on real work, not constructed from its own rulebook.

### 🤖 AI 总结

**一句话总结**：Frontier language models are compared, marketed, and benchmarked on capability -- what their best or average output can achieve. I argue this measures the wrong axis. The models have saturated accurac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Grouping, Stochastic, Machine, Precision, Not, Capability, Frontier

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19140v1) | [下载PDF](https://arxiv.org/pdf/2608.19140v1.pdf)

---

## [3. Tuning the Stochastic Machine: A Systems Engineer's Operating Model for Human-AI Engineering](https://arxiv.org/abs/2608.19125v1)

**作者**：George Andrikopoulos  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-08-19

### 📄 论文摘要

When an expert corrects an LLM assistant's error, the correction usually dies with the session, and the error class returns. I argue this is an operations problem, not a tooling problem: mechanisms for persisting corrections exist and are shipping, but the discipline for governing them -- versioning with provenance, recurrence monitoring, counter-metrics, retirement of stale rules -- does not. Writing as a systems engineer of thirty years, I map the LLM stack onto the machines my profession already operates (frozen silicon, firmware, loadable modules, persistent configuration, volatile memory), identify where the mapping fails (stochastic generation, configuration that binds only probabilistically, no general-purpose retirement (verification) stage by default), and derive from the failures a seven-principle operating discipline with an error loop at its core. Three cases from my own practice illustrate the mechanism, among them a control that silently became the exact harm it was built to prevent. I close with the measurement framework this view implies and the lab study required to test it.

### 🤖 AI 总结

**一句话总结**：When an expert corrects an LLM assistant's error, the correction usually dies with the session, and the error class returns. I argue this is an operations problem, not a tooling problem: mechanisms fo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Tuning, Stochastic, Machine, Systems, Engineer's, Operating, Model, Human-AI

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19125v1) | [下载PDF](https://arxiv.org/pdf/2608.19125v1.pdf)

---

## [4. Robust Risk Under Evolving Uncertainty: A Wasserstein Counterpart of the Entropic Value-at-Risk](https://arxiv.org/abs/2608.19073v1)

**作者**：Deep Kumar Ganguly, Jan Křetínský  
**分类**：cs.AI, cs.LG, stat.ML  
**发布时间**：2026-08-19

### 📄 论文摘要

An agent still learning its environment should be cautious while ignorant and bold once confident. The entropic value-at-risk captures this through a robust-optimization identity---a confidence level fixes the radius of a relative-entropy ball of alternative models---but that ball cannot reach catastrophes the nominal deems impossible, precisely what a safe agent must hedge. We instead use an optimal-transport ball and study the coherent risk measure it induces, the Wasserstein entropic value-at-risk. It has a variational dual mirroring the entropic formula (an inverse temperature becomes a transport price), occupies a definite place in the risk hierarchy, and provably accounts for the reachable catastrophes the entropic measure ignores; we verify both dualities numerically. Driving the transport radius by belief entropy then yields a closed-form robust dynamic-programming operator whose caution contracts as the belief sharpens, with a certified safety sandwich and a sharp safety switch.

### 🤖 AI 总结

**一句话总结**：An agent still learning its environment should be cautious while ignorant and bold once confident. The entropic value-at-risk captures this through a robust-optimization identity---a confidence level ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Robust, Risk, Under, Evolving, Uncertainty, Wasserstein, Counterpart

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19073v1) | [下载PDF](https://arxiv.org/pdf/2608.19073v1.pdf)

---

## [5. What is Missing from AI Post-Training AI: An Empirical Analysis](https://arxiv.org/abs/2608.19072v1)

**作者**：Joy Jia Yin Lim, Xin Huang, Hao Peng 等 8 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-08-19

### 📄 论文摘要

Large language model (LLM) agents can now post-train an LLM end-to-end. They can write code, launch training, evaluate checkpoints, and improve downstream performance, raising the prospect of AI-for-AI. We argue that this picture conflates two distinct capabilities: execution-level capability, iterating within a selected training strategy; and strategy-level capability, revising the high-level judgment as experimental evidence accumulates. Analyzing a large corpus of publicly released post-training trajectories, we find that across different tasks, the agent's training strategy is locked in at the very beginning, and the entire remaining budget is spent on local adjustments within the selected strategy. We then examine three natural explanations--missing experience, missing guidance, and insufficient reasoning--with escalating interventions. Extensive experiments show that (1) an experience-driven scaffold improves execution across the board (+12.6 points on GSM8K and +40.8 on HumanEval) but leaves the strategy static; (2) human guidance effectively redirects the initial strategy, yet the agent falls back into local adjustment loops once training starts; and (3) additional inference compute pays off on easier tasks but yields almost no gain on the hardest one. In conclusion, what agents lack is neither experience, guidance, nor reasoning compute, but a mechanism for spontaneously reevaluating their strategy during execution.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM) agents can now post-train an LLM end-to-end. They can write code, launch training, evaluate checkpoints, and improve downstream performance, raising the prospect of AI-for-A...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, What, Missing, Post-Training, Empirical, Analysis, Large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19072v1) | [下载PDF](https://arxiv.org/pdf/2608.19072v1.pdf)

---

## [6. Adaptive Memory and Reflection Multi-Agent System for Medical Question Answering](https://arxiv.org/abs/2608.19029v1)

**作者**：Pradeep Murugesan, Luoxiao Yang, Xueli Chen 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.MA  
**发布时间**：2026-08-19

### 📄 论文摘要

Accurate and responsible medical question answering (QA) is important in healthcare, where complex cases require factual knowledge and nuanced reasoning. Existing medical QA systems, typically based on single-agent architectures and static retrieval, often lack adaptability, persistent memory, and structured decision-making. This work introduces an adaptive memory and reflection (AMR) agentic system, a multi-agent framework in which specialized agents use dedicated memory and reflection-based feedback to retrieve relevant prior cases and improve subsequent reasoning. Complexity assessment routes questions through solo, collaborative, or escalated workflows, while consensus and ethical overseer modules support reasoning consolidation and output review. Evaluation on MedQA and MedMCQA demonstrates strong performance compared with several baselines. Ablation studies show that combining agent-specific memory, reflection, and external retrieval yields the strongest performance. These findings highlight the potential of structured memory and feedback for developing more trustworthy medical agents. The source code is publicly available at https://github.com/mm-air/AMR-Agent.

### 🤖 AI 总结

**一句话总结**：Accurate and responsible medical question answering (QA) is important in healthcare, where complex cases require factual knowledge and nuanced reasoning. Existing medical QA systems, typically based o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, Adaptive, Memory, Reflection, System, Medical, Question, Answering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19029v1) | [下载PDF](https://arxiv.org/pdf/2608.19029v1.pdf)

---

## [7. Self-prompting and cross-model consensus enable reproducible data extraction from scientific literature with large language models](https://arxiv.org/abs/2608.19025v1)

**作者**：Valentin Romanov, Monique Bax, Steven Niederer  
**分类**：cs.AI, cs.DB  
**发布时间**：2026-08-19

### 📄 论文摘要

Accurately extracting nuanced, contextualized data from research articles is laborious and time intensive. Here, we investigate the performance of frontier, browser-based large language models (LLMs) to extract highly contextualized information. We demonstrate four escalating workflows, 1) given an expert curated prompt and research articles, most frontier LLMs perform well at data extraction, however can struggle with interpreting scientific context and nuance, 2) given simple instructions, LLMs can author their own prompts which were almost as eNective as expert-written prompts, 3) autonomous discovery of research literature was diNicult, agents either missed or hallucinated references, and 4) LLMs can create new datasets from published guidelines that closely match human-expert judges, but still require a human-in-the-loop. Together, these findings define an auditable division of labour in which experts specify the evidence standard, models cross-check repeated extractions and researchers resolve disputed cases, providing a practical route to scaling scientific data curation without relinquishing expert oversight.

### 🤖 AI 总结

**一句话总结**：Accurately extracting nuanced, contextualized data from research articles is laborious and time intensive. Here, we investigate the performance of frontier, browser-based large language models (LLMs) ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Self-prompting, cross-model, consensus, enable, reproducible, data, extraction, scientific

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19025v1) | [下载PDF](https://arxiv.org/pdf/2608.19025v1.pdf)

---

## cs.CL

## [8. ChildSafeAds Shared Task 2026: Commercial Content in Child-Facing YouTube Videos](https://arxiv.org/abs/2608.19165v1)

**作者**：Thales Bertaglia, Catalina Goanta, Gerasimos Spanakis 等 4 位作者  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-08-19

### 📄 论文摘要

ChildSafeAds is a shared task on commercial content in YouTube videos likely to reach children and teenagers. It contains 3,360 videos from 939 channels. Each instance begins with a segment submitted to SponsorBlock, an open-source crowdsourced browser extension whose users mark sponsor segments so that others can skip them. We pair the segment with its available transcript, video and channel information, and a sales or service page linked from the video description. Systems determine what kind of offer is being promoted (ST1), assign product categories (ST2), and identify legal risk flags (ST3). The evidence is divided into four cumulative access levels, from the transcript to the linked page, so results can be compared against the cost of collecting the data. 45.5\% of videos in our data failed to properly use the in-platform ad disclosure method (the ``Includes paid promotion'' label). GPT-5.4 produced the labels after the expert organiser team reviewed samples and iterated on the taxonomy, prompts and model choices. GPT-5.6-luna independently labelled the development set. This report describes the task, data and evaluation. An updated version will add participating systems and shared-task results.

### 🤖 AI 总结

**一句话总结**：ChildSafeAds is a shared task on commercial content in YouTube videos likely to reach children and teenagers. It contains 3,360 videos from 939 channels. Each instance begins with a segment submitted ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ChildSafeAds, Shared, Task, Commercial, Content, Child-Facing, YouTube, Videos

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19165v1) | [下载PDF](https://arxiv.org/pdf/2608.19165v1.pdf)

---

## [9. Comment-level Topic Drift Analysis in the Reddit Corpus](https://arxiv.org/abs/2608.19133v1)

**作者**：Steven Morse, Daniel Runfola, Trenton W. Ford  
**分类**：cs.CL  
**发布时间**：2026-08-19

### 📄 论文摘要

We present a novel application of embedding-based dynamic topic modeling techniques to detect and quantify topic drift at the comment level in a massive corpus. By leveraging pretrained language models to generate contextualized semantic embeddings for short text, we analyzed 12.7 billion Reddit comments spanning 2006 to 2022. Using unsupervised methods on these embeddings, we identify dynamically evolving topic clusters over time. Our primary contribution is a methodology for analysis of semantic drift and discourse evolution in the embedding space itself. We also demonstrate modifications to existing methods that enable this analysis at scale, and we propose and demonstrate a null model comparison test to filter spurious dynamics. Key findings suggest that politically and socially contentious topics exhibit significant directional drift in embedding space, with inter-topic distances changing systematically over time beyond what the null model can explain, whereas domains such as music and sports remain comparatively stable.

### 🤖 AI 总结

**一句话总结**：We present a novel application of embedding-based dynamic topic modeling techniques to detect and quantify topic drift at the comment level in a massive corpus. By leveraging pretrained language model...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Comment-level, Topic, Drift, Analysis, Reddit, Corpus, present

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19133v1) | [下载PDF](https://arxiv.org/pdf/2608.19133v1.pdf)

---

## [10. Grading the Graders: Verification Autonomy Levels (L0-L5) for LLM Reasoning](https://arxiv.org/abs/2608.19009v1)

**作者**：Yajie Yin  
**分类**：cs.CL  
**发布时间**：2026-08-19

### 📄 论文摘要

Large language models (LLMs) are increasingly paired with verifiers (step checkers, self-consistency filters, tool-based fact checkers, formal proof assistants) that claim to detect the model's errors. Yet the verification literature uses the word "level" to mean at least five different things: verification granularity, concept abstraction, risk tier, system-stack layer, and the epistemic source of the ground truth. We propose Verification Autonomy Levels (VAL), a meta-standard classifying verification schemes along a single axis: where does the verification spec come from, and what does the verdict guarantee? VAL ranges from L0 (LLM self-declaration, no deterministic anchor) through L2 (objective ground truth, correctness only) to L3/L4 (decidable systems with single-property or domain-level completeness), with L5 impossible in the unrestricted case. Central to VAL is the completeness blind spot: substitution- and sampling-based verifiers can confirm that proposed candidates hold, but cannot prove that no candidate was missed. We further identify a dichotomy the literature has not stated: completeness is reachable only for formally specifiable properties, while empirical open-world verification (fact-checking, diagnosis) caps at anchored correctness (L2). We document this across four domains (symbolic mathematics, behavior monitoring, medical diagnosis, and code generation) and in the strongest existing formal-verification baseline, whose authors note the verifier "focuses on the correctness of each step." We show the levels of granularity, concept hierarchy, risk, and system stack are orthogonal to VAL, resolving a systematic conflation across 17 surveyed papers. Code and full assessment are released as supplementary material.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly paired with verifiers (step checkers, self-consistency filters, tool-based fact checkers, formal proof assistants) that claim to detect the model's errors...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：L0-L5, LLM, Grading, Graders, Verification, Autonomy, Levels, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19009v1) | [下载PDF](https://arxiv.org/pdf/2608.19009v1.pdf)

---

## [11. Introducing the Privacy-HSD Trade-off: Hate Speech Detection, but not at the Cost of Privacy](https://arxiv.org/abs/2608.19006v1)

**作者**：Stephen Meisenbacher, Vlad Garbuz, Chirill Donos 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-19

### 📄 论文摘要

Hate speech is a real and timely threat that affects a large portion of online users, especially youth and minority groups. While building reliable and robust automatic hate speech detection (HSD) systems is paramount, we argue that this must also be balanced with the individual right to privacy. Exploring the intersection of HSD and privacy, we demonstrate that HSD systems might unintentionally achieve performance at the cost of encoding authorship, posing a threat to privacy. Building on these findings, we establish the notion of a privacy-HSD trade-off, which demands a careful balance. We benchmark a series of text privatization methods, as well as our newly proposed domain-specific AgnoSpeech technique, showing that balancing privacy and HSD is difficult but feasible. The findings make a strong case for more research on the trade-offs between privacy and HSD, both of which have tangible implications for the safeguarding of online participation.

### 🤖 AI 总结

**一句话总结**：Hate speech is a real and timely threat that affects a large portion of online users, especially youth and minority groups. While building reliable and robust automatic hate speech detection (HSD) sys...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Introducing, Privacy-HSD, Trade-off, Hate, Speech, Detection, but, not

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19006v1) | [下载PDF](https://arxiv.org/pdf/2608.19006v1.pdf)

---

## cs.CV

## [12. Image-Guided Pavement Defect Recognition in GPR Data with novel 3D Deep Learning Architecture](https://arxiv.org/abs/2608.19177v1)

**作者**：Yuandong Pan, Linjun Lu, Mudan Wang 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-19

### 📄 论文摘要

Ground Penetrating Radar (GPR) is a widely adopted non-destructive sensing technology for subsurface inspection in civil and transportation engineering. Despite its potential for pavement condition assessment, the large-scale application of GPR in automated inspection has two key challenges: the scarcity of annotated real-world datasets and the lack of deep learning models designed for the unique characteristics of 3-Dimensional (3D) GPR data. This study addresses these limitations by firstly introducing a cost-effective data preparation pipeline that integrates orthomosaic Red Green Blue (RGB) imagery with 3D GPR scans to generate annotated 3D GPR datasets. The proposed method uses the aligned segments of RGB and GPR data, using pavement surface images as a reference to transfer labels of surface-visible defects to corresponding GPR segments, enabling efficient large-scale annotation in a real-world dataset collected on a highway section under operation. In addition to the dataset contribution, we propose a specialised 3D Convolutional Neural Network (CNN) architecture incorporating residual connections, mixed convolutional kernel sizes, and both depthwise and channelwise attention mechanisms to enhance feature representation and defect classification. The model is evaluated on binary classification tasks for detecting patch and crack defects in pavement structures. Experimental results demonstrate that the proposed network outperforms baseline architectures across multiple evaluation metrics. Ablation studies further confirm the effectiveness of the designed architectural components. This work contributes a scalable and practical method for real-world dataset generation, along with a novel deep learning framework.

### 🤖 AI 总结

**一句话总结**：Ground Penetrating Radar (GPR) is a widely adopted non-destructive sensing technology for subsurface inspection in civil and transportation engineering. Despite its potential for pavement condition as...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Image-Guided, Pavement, Defect, Recognition, GPR, Data, novel

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19177v1) | [下载PDF](https://arxiv.org/pdf/2608.19177v1.pdf)

---

## [13. Detecting Backdoors in Object Detection via Pre-NMS Prediction Distribution Shift](https://arxiv.org/abs/2608.19088v1)

**作者**：Longtian Wang, Zhengyu Zhao, Chenhao Lin 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-19

### 📄 论文摘要

Object detection models deployed in safety-critical applications remain vulnerable to backdoor attacks that cause targeted misbehaviors when a hidden trigger is present. Existing detection methods either rely on trigger inversion or exploit architecture-specific assumptions, and critically, representative existing methods fail to generalize reliably to scene-level attacks, where a single trigger induces anomalous behavior across all objects in the scene simultaneously. We present DistScan, a backdoor detection framework based on a simple but previously unexploited observation: backdoor injection systematically shifts a model's pre-NMS prediction class distribution away from its training class frequencies, even on clean inputs without any trigger present. DistScan aggregates intermediate class predictions over a clean validation set and flags a model as backdoored if the resulting distribution deviates significantly from the training class frequencies, requiring no model weight access, no trigger knowledge, and no additional training. Extensive experiments on MS-COCO and PASCAL VOC across two architectures and three scene-level attack scenarios demonstrate that DistScan substantially outperforms existing methods, improving average detection accuracy over the best-performing applicable baseline by 27.32 percentage points.

### 🤖 AI 总结

**一句话总结**：Object detection models deployed in safety-critical applications remain vulnerable to backdoor attacks that cause targeted misbehaviors when a hidden trigger is present. Existing detection methods eit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Detecting, Backdoors, Object, Detection, via, Pre-NMS, Prediction, Distribution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19088v1) | [下载PDF](https://arxiv.org/pdf/2608.19088v1.pdf)

---

## [14. SPK: Eliciting Structured Prior Knowledge for Interpretable Out-of-Distribution Detection in Real-Time Object Detection](https://arxiv.org/abs/2608.19080v1)

**作者**：Changshun Wu, Weicheng He, Xiaowei Huang 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-08-19

### 📄 论文摘要

Object detectors often produce over-confident predictions for objects outside their training categories, leading to so-called out-of-distribution (OoD) hallucinations. Existing approaches for detecting or mitigating such hallucinations typically either construct scoring functions directly over learned object detector representations or modify the object detector itself to suppress hallucination emergence. However, the latent priors implicitly encoded in these representations remain largely unexplored and have not been explicitly decoded for OoD detection. To uncover and exploit these latent priors, we propose Structured Prior Knowledge (SPK), a hallucination-oriented framework that explicitly elicits OoD-relevant priors from pretrained object detectors. Specifically, SPK leverages in-distribution data and hallucination-inducing samples as diagnostic supervision to elicit part-level semantic concepts underlying object detector decision-making, rather than using them merely for rejection or object detector adaptation. The elicited semantic priors are further integrated with geometric and contextual priors to form a compact five-dimensional SPK representation for OoD detection. Extensive experiments across diverse object detector architectures and multiple OoD benchmarks demonstrate that SPK achieves state-of-the-art OoD detection. Our findings reveal that pretrained object detectors already encode substantially richer latent knowledge than is typically exploited for OoD detection. More importantly, this knowledge can be explicitly elicited and organized into a compact, structured, and interpretable knowledge space for prediction reliability analysis. This suggests a promising proactive route for improving object detector reliability by explicitly uncovering and leveraging latent priors. Code and data are available at: https://gricad-gitlab.univ-grenoble-alpes.fr/dnn-safety/spk

### 🤖 AI 总结

**一句话总结**：Object detectors often produce over-confident predictions for objects outside their training categories, leading to so-called out-of-distribution (OoD) hallucinations. Existing approaches for detectin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SPK, Eliciting, Structured, Prior, Knowledge, Interpretable, Out-of-Distribution, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19080v1) | [下载PDF](https://arxiv.org/pdf/2608.19080v1.pdf)

---

## [15. GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting](https://arxiv.org/abs/2608.19066v1)

**作者**：Yechan Park, HyunJin Kim  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-19

### 📄 论文摘要

This paper proposes a lightweight, plug-and-play framework that improves robustness to viewpoint shifts in Vision-Language-Action (VLA) policies without policy retraining. To our knowledge, this is the first approach to directly leverage 3D Gaussian-based novel-view synthesis for observation-space adaptation in VLA policies. Current VLA performance relies on the implicit assumption that training and deployment camera configurations are identical. Our experiments show that even a small displacement of the camera mount can reduce the success rate on the LIBERO benchmark from about 90% to about 10% in the worst case. Prior approaches, such as large-scale fine-tuning or generative data augmentation, are computationally expensive and risk catastrophic forgetting. To address this, viewpoint shifts are reformulated as a localized novel-view synthesis problem. Under a Locality assumption, that camera perturbations remain within a small bounded region relative to the workspace, viewpoint normalization reduces to a scene- and policy-independent disocclusion task. Our work implements this idea with a 4M-parameter 3D-Gaussian canonicalizer prepended to a frozen VLA policy. Without modifying policy weights, GS-VLA improves performance across three orthogonal axes: (1) Policy architectures, (2) Unseen task suites, and (3) Perturbation scales. These results show that a lightweight visual module can recover a large fraction of the performance lost under viewpoint shift, without policy retraining.

### 🤖 AI 总结

**一句话总结**：This paper proposes a lightweight, plug-and-play framework that improves robustness to viewpoint shifts in Vision-Language-Action (VLA) policies without policy retraining. To our knowledge, this is th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GS-VLA, Plug-and-Play, Viewpoint, Canonicalization, Frozen, VLA, Policies, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19066v1) | [下载PDF](https://arxiv.org/pdf/2608.19066v1.pdf)

---

## [16. When Two Tracers Disagree: An Investigation of Multimodal Fusion for Clinical PET/CT Segmentation](https://arxiv.org/abs/2608.19063v1)

**作者**：Jack A. Johnson, Bartłomiej W. Papież  
**分类**：cs.CV  
**发布时间**：2026-08-19

### 📄 论文摘要

PSMA and FDG PET/CT visualise complementary biological information in prostate cancer. Combining both tracers could capture heterogeneous tumour phenotypes that may be missed by either alone, yet there is no consensus on effective deep learning architectures for fusing these modalities. We evaluated multimodal image-fusion strategies for automatic whole-body PET/CT lesion segmentation to estimate total tumour burden. Using the public DEEP-PSMA Challenge dataset, we trained tracer-specific 3D nnU-Net baselines and compared (i) early fusion with a single encoder and one decoder (OEOD) or two decoders (OETD), and (ii) intermediate fusion via a dual-encoder cross-attention U-Net (DECA-UNet). Tracer-specific baselines performed strongly (PSMA Dice = 0.93; FDG = 0.81). Fusion yielded mixed results: OEOD produced a combined Dice of 0.90 (on an easier, non-tracer-specific task), whilst the tracer-specific fusion models reached PSMA/FDG = 0.69/0.64 (OETD) and 0.76/0.57 (DECA-UNet). Whilst fusion often provided reasonable PSMA segmentation, FDG performance degraded and no strategy consistently exceeded the single-tracer baselines. Under the evaluated setting, tracer-specific models remain the stronger baseline; clinically useful gains from multimodal fusion will likely require architectures that better preserve tracer specific representations. Our code is available at: https://github.com/JackJ3636/DEEP_PSMA_code

### 🤖 AI 总结

**一句话总结**：PSMA and FDG PET/CT visualise complementary biological information in prostate cancer. Combining both tracers could capture heterogeneous tumour phenotypes that may be missed by either alone, yet ther...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, of, When, Two, Tracers, Disagree, Investigation, Multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19063v1) | [下载PDF](https://arxiv.org/pdf/2608.19063v1.pdf)

---

## [17. Generalized Audio-Driven Synthesis of Precise Drummer Motion](https://arxiv.org/abs/2608.19055v1)

**作者**：Álvaro G. Iñesta, Mattia Ryffel, Amit H. Bermano 等 5 位作者  
**分类**：cs.CV, cs.GR, cs.SD  
**发布时间**：2026-08-19

### 📄 论文摘要

Music-driven character animation enables and enhances transformative applications in entertainment and interactive education. However, synthesizing realistic drumming motion from audio remains challenging due to the inherent tension between high-acceleration dynamics and the need for extreme spatial-temporal precision. Existing approaches, often reliant on motion matching or MIDI input, struggle with generalizing to diverse real-world audio. Moreover, the field lacks standardized evaluation metrics capable of distinguishing precise drumming from noisy motion. In this paper, we introduce a generative diffusion framework featuring a dual-objective loss function that decouples skeletal integrity from drumstick precision, thus enabling centimeter-level stick precision without sacrificing natural body dynamics. Additionally, leveraging our own dataset and data augmentation strategy, the model generalizes to non-curated, in-the-wild audio. To rigorously evaluate performance, we propose two novel metrics: an impact-to-target distance to quantify spatial precision and an audio-motion correlation score to assess temporal alignment. Our quantitative analysis and user studies demonstrate that our system generates high-quality motion that is often indistinguishable from ground-truth performances.

### 🤖 AI 总结

**一句话总结**：Music-driven character animation enables and enhances transformative applications in entertainment and interactive education. However, synthesizing realistic drumming motion from audio remains challen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Generalized, Audio-Driven, Synthesis, Precise, Drummer, Motion, Music-driven

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19055v1) | [下载PDF](https://arxiv.org/pdf/2608.19055v1.pdf)

---

## [18. Counterfactual Contrastive Analysis](https://arxiv.org/abs/2608.19032v1)

**作者**：Yunlong He, Pietro Gori  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-19

### 📄 论文摘要

Visual Counterfactual Explanations (VCEs) aim to explain image classifiers by generating minimally edited and realistic versions of an input image that change the classifier's prediction. Existing VCE methods are inherently classifier-dependent and therefore susceptible to classifier biases and failure modes, such as sensitivity to shortcut features and calibration errors. In this paper, we propose a classifier-free approach for visual counterfactual generation based on Contrastive Analysis (CA). Given two datasets corresponding to different classes (e.g., healthy and patients), we disentangle the generative factors that are common across the two datasets from those that are salient to each dataset, and generate counterfactual images by swapping only the salient factors. By operating directly on data distributions rather than decision boundaries, our method provides model-agnostic VCEs that are less sensitive to classifier biases. Our approach leverages the high-quality synthesis and well-structured latent space of StyleGAN2. We use the feature space F, instead than the usual W-space, to improve detail preservation. Unlike conventional CA approaches, which typically assume salient factors in only one dataset, we introduce an adapted framework and loss functions for VCE that allow multiple salient factors in each dataset. We evaluate our method on three medical imaging datasets and demonstrate superior counterfactual generation quality compared to existing approaches.

### 🤖 AI 总结

**一句话总结**：Visual Counterfactual Explanations (VCEs) aim to explain image classifiers by generating minimally edited and realistic versions of an input image that change the classifier's prediction. Existing VCE...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Counterfactual, Contrastive, Analysis, Visual, Explanations, VCEs, aim, explain

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19032v1) | [下载PDF](https://arxiv.org/pdf/2608.19032v1.pdf)

---

## [19. Orthogonal Polynomial Approximation for Matrix Log Normalization in Global Covariance Pooling](https://arxiv.org/abs/2608.19021v1)

**作者**：Md Rifat Ur Rahman, Md Raihan Khan, Md Sakib Hossain Shovon 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-19

### 📄 论文摘要

Global Covariance Pooling (GCP) improves deep networks by capturing second-order feature statistics, and is especially effective for fine-grained recognition. Because covariance matrices live on the Symmetric Positive Definite (SPD) manifold, a normalization step is required before the Euclidean classifier. The faithful choice is the matrix logarithm (MLN-COV), which maps the SPD manifold to its tangent space; in practice it was abandoned in favour of the matrix square root because its eigendecomposition-based gradient is numerically unstable. We show that this instability is an artifact of computing the logarithm spectrally, not of the logarithm itself. Approximating the logarithm with finite polynomials in the covariance matrix removes the eigendecomposition from both passes: every operation becomes a General Matrix Multiplication (GEMM), the gradient stays bounded on the spectral support of the pre-normalized covariance, and the unstable 1/(lambda_i-lambda_j) term never appears. The key ingredient is a mean-eigenvalue pre-normalization that centres the spectrum near 1, away from the singularity of log, with a scalar post-compensation that returns the singular part of log(A) in closed form. Our recommended normalizer is a degree-8 Chebyshev expansion evaluated by a three-term matrix recurrence, with a matching reverse recurrence for the backward pass; Legendre, Laguerre, Taylor and Pade expansions are studied as controls that isolate the roles of the basis and of the target function. On three fine-grained benchmarks and ImageNet-1k the decomposition-free logarithm is both faster and more accurate than the spectral logarithm and than the square-root approximations it replaces, and at matched basis and degree the log target beats the square-root target, confirming that the gain comes from the faithful Riemannian map rather than from a better polynomial family.

### 🤖 AI 总结

**一句话总结**：Global Covariance Pooling (GCP) improves deep networks by capturing second-order feature statistics, and is especially effective for fine-grained recognition. Because covariance matrices live on the S...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Orthogonal, Polynomial, Approximation, Matrix, Log, Normalization, Global, Covariance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19021v1) | [下载PDF](https://arxiv.org/pdf/2608.19021v1.pdf)

---

## [20. One-Stage Object Detectors in Autonomous Driving](https://arxiv.org/abs/2608.19014v1)

**作者**：Jonel Roman, Ryan Sirjue, Peter Nguyen 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-19

### 📄 论文摘要

Autonomous vehicles depend on fast and reliable perception systems to detect surrounding vehicles, pedestrians, cyclists, traffic signs, and other road objects in real time. This paper presents a comprehensive survey and analysis of one-stage object detectors for autonomous driving rather than an implementation of a new detection system. The survey reviews the evolution of major one-stage detectors, including YOLOv1, SSD, RetinaNet, EfficientDet, anchor-free detectors such as FCOS and CenterNet, and recent real-time models such as YOLOv10. It compares these architectures through their design choices, feature-fusion strategies, loss functions, deployment trade-offs, and reported benchmark performance. The paper also summarizes commonly used autonomous-driving datasets, evaluation metrics, open challenges, and future research directions. Overall, this survey highlights how one-stage detectors balance speed, accuracy, efficiency, and robustness, while also emphasizing the remaining gap between benchmark results and dependable real-world autonomous-driving performance.

### 🤖 AI 总结

**一句话总结**：Autonomous vehicles depend on fast and reliable perception systems to detect surrounding vehicles, pedestrians, cyclists, traffic signs, and other road objects in real time. This paper presents a comp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：One-Stage, Object, Detectors, Autonomous, Driving, vehicles, depend, fast

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19014v1) | [下载PDF](https://arxiv.org/pdf/2608.19014v1.pdf)

---

## cs.LG

## [21. Lévy Attention: Single-Pass Predictive Uncertainty for Continuous-Time Attention](https://arxiv.org/abs/2608.19171v1)

**作者**：Sotirios P. Chatzis, Loukas Papadoulas  
**分类**：cs.LG  
**发布时间**：2026-08-19

### 📄 论文摘要

Deep models for irregularly-sampled time series answer queries at arbitrary continuous timestamps, yet report nothing about how far each answer should be trusted. We show the attention layer itself can close that gap: with the right stochastic formulation, the pass that makes each prediction also reports, in closed form and at no extra cost, how far it should be trusted. We introduce Lévy Attention, a cross-attention operator whose output is a stochastic integral against an inhomogeneous Poisson random measure: query-key compatibilities assemble an intensity over a continuous (time x channel) index space, the measure scatters atoms under it, and the output averages an interpolated value field at those atoms. In expectation it reduces to a mollified cosine-kernel attention, so it replaces a softmax layer and trains with exact gradients.   What softmax discards, the Poisson construction preserves in closed form: the evidence $Λ_q$ (total compatibility mass) and the disagreement $\mathrm{tr}\,Σ_V(q)$ (value spread). An exact variance identity makes their combination $\hatσ(q)=\sqrt{\mathrm{tr}\,Σ_V(q)\,\varphi(Λ_q)}$ the root-mean-square deviation of the sampled operator, emitted by the deterministic pass with no trained head.   Empirically, disagreement carries the signal, while the evidence factor swings from uninformative on dense data to strongly informative on sparse. On t-PatchGNN the operator swap costs at most 5.6% accuracy against a matched control and nothing on the sparsest dataset. The free disagreement signal improves on 20-pass MC dropout across matched five-seed suites, and $\hatσ$ scales a calibrated Gaussian whose zero-sample CRPS beats a fifty-draw sampler; a split-conformal wrapper reaches nominal coverage at every level, and one pass ranks 3,383 unseen patients by trust in 1.4 seconds.

### 🤖 AI 总结

**一句话总结**：Deep models for irregularly-sampled time series answer queries at arbitrary continuous timestamps, yet report nothing about how far each answer should be trusted. We show the attention layer itself ca...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Lévy, Attention, Single-Pass, Predictive, Uncertainty, Continuous-Time, Deep, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19171v1) | [下载PDF](https://arxiv.org/pdf/2608.19171v1.pdf)

---

## [22. Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions](https://arxiv.org/abs/2608.19151v1)

**作者**：Tomasz R. Bielecki, Thibaut Mastrolia, Haoze Yan  
**分类**：cs.LG, math.OC, stat.ML  
**发布时间**：2026-08-19

### 📄 论文摘要

We study stochastic control of multivariate Hawkes-driven stochastic differential equations with machine learning algorithms in a non-Markovian setting. Due to the path dependence of the memory of the Hawkes intensity, this problem does not fall within classical stochastic control theory outside particular Markovian kernels. We first develop a finite-dimensional Markovianization procedure and algorithm to approximate multivariate Hawkes processes with mixtures of exponential kernels. We prove the convergence of the Markovianized approximation of the Hawkes process, its intensity, and the value of the problem to the original non-Markovian processes and the value of the primal problem. We then formulate continuous-time deterministic policy gradient learning on the Markovianized approximation of the problem, called Hawkes-CT DDPG. We propose a model-free algorithm to solve the non-Markovian Hawkes-driven optimization by observing only the event times of the process, the realization of the solution to the SDE, and a chosen set of decay filters, while the Hawkes kernel coefficients remain unknown. We compare our continuous time reinforcement learning Hawkes-CT DDPG method with discrete time reinforcement learning techniques under three different types of kernels: simple exponential, Erlang, and power-law kernels.

### 🤖 AI 总结

**一句话总结**：We study stochastic control of multivariate Hawkes-driven stochastic differential equations with machine learning algorithms in a non-Markovian setting. Due to the path dependence of the memory of the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Continuous-Time, Reinforcement, Learning, Controlled, Hawkes, Jump-Diffusions, study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19151v1) | [下载PDF](https://arxiv.org/pdf/2608.19151v1.pdf)

---

## [23. SCORE: Subject Coordinate Recovery for Label-Free Cross-Subject EEG-to-Image Retrieval](https://arxiv.org/abs/2608.19134v1)

**作者**：Zhenyao Cui, Siyuan Kan, Siyang Li 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-19

### 📄 论文摘要

Accurate visual decoding can reveal how the brain represents visual information and recover perceived content from neural signals such as electroencephalography (EEG), with potential for neural communication. However, current EEG-to-image retrieval methods perform far below their within-subject counterparts for new users without labeled calibration, limiting real-world deployment. To understand this gap, we analyze EEG features across subjects and find that different subjects preserve similar relationships among concepts but express them along different coordinate directions. We therefore propose Subject Coordinate Recovery (SCORE), a target label-free framework combining recovery-aware source training with coordinate alignment at deployment. During training, SCORE aligns source subject EEG with a common image space and simulates unseen-subject recovery through source-only episodes. At deployment, with both encoders frozen, SCORE selects reliable EEG-image landmarks through hubness-corrected matching and estimates an orthogonal transformation to recover target EEG coordinates without source data or target labels. In 200-way retrieval on two public benchmarks, SCORE outperforms the unadapted baseline for every target subject and achieves the best overall accuracy. It reaches 53.23%/83.55% and 12.01%/32.16% Top-1/Top-5 on THINGS-EEG2 and Alljoined-1.6M, respectively, surpassing the strongest baselines by 17.45/15.70 and 3.08/4.62 percentage points. Without target labels or encoder updates, SCORE brings brain-based visual decoding closer to robust, practical, low-latency deployment across users.

### 🤖 AI 总结

**一句话总结**：Accurate visual decoding can reveal how the brain represents visual information and recover perceived content from neural signals such as electroencephalography (EEG), with potential for neural commun...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SCORE, Subject, Coordinate, Recovery, Label-Free, Cross-Subject, EEG-to-Image, Retrieval

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19134v1) | [下载PDF](https://arxiv.org/pdf/2608.19134v1.pdf)

---

## [24. Beyond Trial Averaging: Anchoring Neural and Visual Representations for Few-Repetition Brain-to-Image Retrieval](https://arxiv.org/abs/2608.19128v1)

**作者**：Zhenyao Cui, Siyuan Kan, Dingkun Liu 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-19

### 📄 论文摘要

Decoding visual information from brain signals probes neural representations and enables neuro-rehabilitation and dream decoding. Recent brain-to-image retrieval approaches have achieved promising performance, typically by averaging many (up to 80) neural trials per image, requiring repeated stimulus presentation that increases latency, cost, and user burden. When only one or a few repetitions are available, the retrieval accuracy drops sharply. This drop is commonly attributed to query noise because averaging suppresses noise and increases signal stability. However, we find a non-transitive alignment pattern: the low-repetition query signal and the image representation each align with the high-repetition center, but not directly with each other. This pattern shows that query noise is only part of the problem and that gallery placement also affects retrieval. We therefore propose a neural-anchor-based retrieval (NEAR) framework that treats the high-repetition center as an anchor and approaches it from both sides: a denoiser pulls the noisy query toward the true anchor, and a small network predicts each candidate's pseudo anchor from its image and pulls the image toward it. Across four datasets spanning EEG, MEG and fMRI, NEAR consistently improved retrieval in the few-repetition regime. On THINGS-EEG2, it improved 200-way Top-1 accuracy by 5.7 and 9.3 percentage points respectively, when averaging one and four repetitions. By anchoring neural and visual representations, NEAR reduces reliance on repeated acquisition and brings neural retrieval closer to real-world deployment.

### 🤖 AI 总结

**一句话总结**：Decoding visual information from brain signals probes neural representations and enables neuro-rehabilitation and dream decoding. Recent brain-to-image retrieval approaches have achieved promising per...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Trial, Averaging, Anchoring, Neural, Visual, Representations, Few-Repetition

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19128v1) | [下载PDF](https://arxiv.org/pdf/2608.19128v1.pdf)

---

## [25. Leaf Values as Coordinates: Exact Contrastive Explanation for Gradient-Boosted Ensembles](https://arxiv.org/abs/2608.19127v1)

**作者**：Emanuele Luzio  
**分类**：cs.LG, cs.AI, cs.CY  
**发布时间**：2026-08-19

### 📄 论文摘要

A gradient-boosted ensemble predicts by summing one leaf value per tree. Read   those values as coordinates rather than as intermediate results, and every   instance becomes a point in R^M on which the model acts linearly: the score is   the sum of the coordinates.   This small change of view makes contrastive explanation exact. The difference   between two instances is a vector that is identically zero wherever they share   a leaf, so the gap between a rejected applicant and an accepted one is carried   by a handful of coordinates, each traceable to a real split in a real tree.   Nothing is fitted, sampled, or assumed additive in features -- the additivity   is already there, in the right space.   We build a recourse method on this representation and evaluate it on five   tabular datasets under repeated cross-validation. Its recommendation   reconstructs the model's own decision to 6.2 x 10^-15, so an auditor can   re-check the arithmetic without the model. On the credit datasets it is   Pareto-non-dominated on effort against realism. And when recommendations are   restricted to changes the subject could actually make -- not their age, not a   settled delinquency -- it retains 58% of its validity where the strongest   baseline retains 41%, a distinction the standard evaluation cannot see because   it never asks whether a recommendation can be carried out.

### 🤖 AI 总结

**一句话总结**：A gradient-boosted ensemble predicts by summing one leaf value per tree. Read   those values as coordinates rather than as intermediate results, and every   instance becomes a point in R^M on which th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Leaf, Values, Coordinates, Exact, Contrastive, Explanation, Gradient-Boosted

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19127v1) | [下载PDF](https://arxiv.org/pdf/2608.19127v1.pdf)

---

## [26. PGFS++: Molecular Property Improvement under Synthesis and Diversity Constraints](https://arxiv.org/abs/2608.19121v1)

**作者**：Boqiao Zhang, Godbless James, Sai Krishna Gottipati 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-19

### 📄 论文摘要

Improving molecular properties, such as drug-likeness or binding affinity, is a recurring task in early-stage drug discovery. However, molecules optimized in an unconstrained chemical space have limited practical value if they cannot be synthesized. Policy Gradient for Forward Synthesis (PGFS) is a synthesis-aware reinforcement learning method for molecular improvement, but its use of reactant embedding prediction makes reactant selection indirect, which, as we show, limits learning effectiveness. We first develop PGFS+, in which reaction templates and second reactants are represented by trainable embedding lookup tables. Combined with a more effective scoring function and RL algorithm, PGFS+ significantly improves the desired property. However, it exposes a reward-hacking failure mode: a powerful reactant search can map diverse input molecules to the same high-reward magnet molecule, improving the reward while collapsing the output diversity. We therefore introduce PGFS++, a synthesis-aware reinforcement learning framework for input-specific molecular improvement. Given an input molecule, PGFS++ treats it as the start of a forward-synthesis trajectory, applies learned reaction templates with compatible in-stock building blocks, and produces a molecule with improved target properties, an explicit synthesis route, and structural similarity to the input. Experiments on molecular improvement tasks show that PGFS++ improves target properties while preserving high output diversity.

### 🤖 AI 总结

**一句话总结**：Improving molecular properties, such as drug-likeness or binding affinity, is a recurring task in early-stage drug discovery. However, molecules optimized in an unconstrained chemical space have limit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PGFS++, Molecular, Property, Improvement, under, Synthesis, Diversity, Constraints

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19121v1) | [下载PDF](https://arxiv.org/pdf/2608.19121v1.pdf)

---

## [27. Enhancing EBSD throughput of battery electrode materials using super-resolution generative adversarial networks](https://arxiv.org/abs/2608.19117v1)

**作者**：John Mangum, Andrew Glaws, Francois Usseglio-Viretta 等 5 位作者  
**分类**：cs.LG, cond-mat.mtrl-sci  
**发布时间**：2026-08-19

### 📄 论文摘要

Quantitative microstructural characterization of Li-ion battery electrode materials using electron backscatter diffraction (EBSD) has been proven as a critical method for optimizing cell performance. However, the inherently slow nature of EBSD can hinder the throughput of analyses needed for statistical representation of a material microstructure being developed. This work demonstrates a machine learning super-resolution framework using a generative adversarial network (SRGAN) to significantly increase EBSD throughput. The SRGAN model was trained on EBSD data of LiNixMnyCozO2 (NMC) cathode particles to computationally enhance low-resolution datasets and its performance is compared against classical interpolation methods across various upscaling factors (2x to 12x). Both qualitative image metrics and quantitative microstructural analysis verified that the SRGAN systematically outperformed classical methods, particularly in preserving small grains and maintaining realistic grain boundaries. We demonstrate that a 5x upscaling factor, corresponding to a 25x speed-up in acquisition time or a 25x larger field of view, is practical while maintaining acceptable accuracy in key metrics like grain size and shape. For instance, at 5x upscaling, relative errors were +5.7%, +8.2%, and -14.6% on grain area-equivalent diameter, grain maximum sphere-inscribed diameter, and grain boundary length, respectively. The SRGAN methodology developed in this work significantly enhances the efficiency of EBSD acquisition for more statistically robust microstructural dataset, enabling EBSD as a high-throughput characterization tool for materials research and industrial process development.

### 🤖 AI 总结

**一句话总结**：Quantitative microstructural characterization of Li-ion battery electrode materials using electron backscatter diffraction (EBSD) has been proven as a critical method for optimizing cell performance. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Enhancing, EBSD, throughput, battery, electrode, materials, super-resolution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19117v1) | [下载PDF](https://arxiv.org/pdf/2608.19117v1.pdf)

---

## [28. Does Mapping Non-Maximal Probabilities to GMM Components Matter for S-JEPA Encoder Representations?](https://arxiv.org/abs/2608.19084v1)

**作者**：Wenxuan He, Yunpeng Li, Shan Liang  
**分类**：cs.LG, cs.SD  
**发布时间**：2026-08-19

### 📄 论文摘要

S-JEPA uses soft Gaussian mixture model (GMM) posteriors instead of hard cluster labels to preserve uncertainty. It remains unclear whether the probability values alone are sufficient, or whether it also matters which GMM components receive the non-maximal probabilities. We test this with two matched controls. FIXED-RANDPERM keeps the top-1 component and probability together with the multiset of non-maximal probability values, but reassigns those non-maximal values using a mapping fixed for each physical frame. UNIFORM-TAIL keeps the top-1 component, its probability, and total non-maximal mass but distributes that mass uniformly. Across three independent seeds, REAL SOFT outperforms both controls on two frozen Encoder readouts. It provides better recovery of the original GMM tail and greater accessibility of spectral dynamics over short time scales after controlling for the complete spectrum of the current frame. In two exposure experiments, both readouts improved overall as more frames retained the original mapping. We also descriptively follow one Phase 2 trajectory after the switch to the online GMM. These results show that the numerical probability structure of the soft target does not fully determine the learned Encoder representation. The mapping of non-maximal probabilities to GMM components also matters.

### 🤖 AI 总结

**一句话总结**：S-JEPA uses soft Gaussian mixture model (GMM) posteriors instead of hard cluster labels to preserve uncertainty. It remains unclear whether the probability values alone are sufficient, or whether it a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Does, Mapping, Non-Maximal, Probabilities, GMM, Components, Matter, S-JEPA

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19084v1) | [下载PDF](https://arxiv.org/pdf/2608.19084v1.pdf)

---

## [29. Multi-Agent Off-Policy Deep Reinforcement Learning for Smart Campus Coverage](https://arxiv.org/abs/2608.19049v1)

**作者**：Omar Rady, Mohamed Ayman, Ali Arafa 等 4 位作者  
**分类**：cs.LG, eess.SP  
**发布时间**：2026-08-19

### 📄 论文摘要

Deep reinforcement learning (DRL) has recently gained a great attention due to its real-time adaptation and effectiveness in complex optimization problems. This paper investigates the optimal deployment of millimeter-wave (mmWave) base stations (BSs) in a realistic, non-convex campus topology. The optimization problem is NP-hard, due to the non-convex, non-smooth nature of the max-min fairness objective. To overcome these constraints, we formulate the BS placement as a Markov Decision Process (MDP) and systematically benchmark four DRL schemes: a discrete single-agent Deep Q-Network (DQN), a spatially partitioned Multi-Agent DQN, a continuous single-agent Deep Deterministic Policy Gradient (DDPG), and a geographically partitioned multi-agent DDPG framework. Numerical evaluations reveal that the multi-agent DDPG approach substantially outperforms single-agent in dense scenarios. Additionally full coverage is achieved, and a fairness Jain's index of 0.94 is obtained. Finally, the multi-agent demonstrates highly efficient computational convergence of dense scenarios with $400$ users.

### 🤖 AI 总结

**一句话总结**：Deep reinforcement learning (DRL) has recently gained a great attention due to its real-time adaptation and effectiveness in complex optimization problems. This paper investigates the optimal deployme...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, Off-Policy, Deep, Reinforcement, Learning, Smart, Campus, Coverage

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19049v1) | [下载PDF](https://arxiv.org/pdf/2608.19049v1.pdf)

---

## [30. Harness Continual Learning: Continual Adaptation Beyond Model Parameters](https://arxiv.org/abs/2608.19013v1)

**作者**：Borui Kang, Jinrui Gu, Junhan Lv 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-19

### 📄 论文摘要

Continual learning has largely been model-centric, treating model parameters as the state that changes with sequential experience. Modern agents can also adapt through a harness of prompts, memories, tools, skills, and routing rules. Because these contents jointly shape later execution, a harness update can disrupt previously reliable behavior even when the model is frozen. This raises a new question: how can an agent continually improve its state outside the model while retaining behavior acquired earlier? We formulate Harness Continual Learning (HCL), a new continual learning paradigm in which the harness evolves around a frozen foundation model, and define the resulting loss of earlier behavior as harness-level forgetting. We instantiate HCL with four execution-facing components: the Task Interface, Experience Memory, Capability Map, and Adaptive Router. We further introduce guarded harness evolution to separate update generation from state commitment. A Continual Optimizer proposes candidate harnesses from post-execution feedback, and a Continual Evaluator commits the resulting candidate harness only after checking current improvement, historical retention, and validity. Experiments on textual reasoning, multimodal perception, and open-world interaction demonstrate capability accumulation and failure recovery, with relative gains exceeding 10% over corresponding baselines in multiple settings. Component ablations assess the contribution of each harness component, while controlled retention sweeps reveal measurable harness-level forgetting and show that the stability--plasticity trade-off can be explicitly adjusted.

### 🤖 AI 总结

**一句话总结**：Continual learning has largely been model-centric, treating model parameters as the state that changes with sequential experience. Modern agents can also adapt through a harness of prompts, memories, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Harness, Continual, Learning, Adaptation, Beyond, Model, Parameters, has

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.19013v1) | [下载PDF](https://arxiv.org/pdf/2608.19013v1.pdf)

---

