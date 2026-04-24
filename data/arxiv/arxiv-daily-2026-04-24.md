# arXiv AI 论文日报 | 2026-04-24

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.CL](#csCL) (9 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation](https://arxiv.org/abs/2604.21910v1)

**作者**：Bartosz Balis, Michal Orzechowski, Piotr Kica 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-23

### 📄 论文摘要

Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.

### 🤖 AI 总结

**一句话总结**：Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research ques...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Research, Question, Scientific, Workflow, Leveraging, Agentic, Science, Automation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21910v1) | [下载PDF](https://arxiv.org/pdf/2604.21910v1.pdf)

---

## [2. Bounding the Black Box: A Statistical Certification Framework for AI Risk Regulation](https://arxiv.org/abs/2604.21854v1)

**作者**：Natan Levy, Gadi Perl  
**分类**：cs.AI  
**发布时间**：2026-04-23

### 📄 论文摘要

Artificial intelligence now decides who receives a loan, who is flagged for criminal investigation, and whether an autonomous vehicle brakes in time. Governments have responded: the EU AI Act, the NIST Risk Management Framework, and the Council of Europe Convention all demand that high-risk systems demonstrate safety before deployment. Yet beneath this regulatory consensus lies a critical vacuum: none specifies what ``acceptable risk'' means in quantitative terms, and none provides a technical method for verifying that a deployed system actually meets such a threshold. The regulatory architecture is in place; the verification instrument is not.   This gap is not theoretical. As the EU AI Act moves into full enforcement, developers face mandatory conformity assessments without established methodologies for producing quantitative safety evidence - and the systems most in need of oversight are opaque statistical inference engines that resist white-box scrutiny.   This paper provides the missing instrument. Drawing on the aviation certification paradigm, we propose a two-stage framework that transforms AI risk regulation into engineering practice. In Stage One, a competent authority formally fixes an acceptable failure probability $δ$ and an operational input domain $\varepsilon$ - a normative act with direct civil liability implications. In Stage Two, the RoMA and gRoMA statistical verification tools compute a definitive, auditable upper bound on the system's true failure rate, requiring no access to model internals and scaling to arbitrary architectures. We demonstrate how this certificate satisfies existing regulatory obligations, shifts accountability upstream to developers, and integrates with the legal frameworks that exist today.

### 🤖 AI 总结

**一句话总结**：Artificial intelligence now decides who receives a loan, who is flagged for criminal investigation, and whether an autonomous vehicle brakes in time. Governments have responded: the EU AI Act, the NIS...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bounding, Black, Box, Statistical, Certification, Framework, Risk, Regulation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21854v1) | [下载PDF](https://arxiv.org/pdf/2604.21854v1.pdf)

---

## [3. Alignment has a Fantasia Problem](https://arxiv.org/abs/2604.21827v1)

**作者**：Nathanael Jo, Zoe De Simone, Mitchell Gordon 等 4 位作者  
**分类**：cs.AI, cs.HC  
**发布时间**：2026-04-23

### 📄 论文摘要

Modern AI assistants are trained to follow instructions, implicitly assuming that users can clearly articulate their goals and the kind of assistance they need. Decades of behavioral research, however, show that people often engage with AI systems before their goals are fully formed. When AI systems treat prompts as complete expressions of intent, they can appear to be useful or convenient, but not necessarily aligned with the users' needs. We call these failures Fantasia interactions. We argue that Fantasia interactions demand a rethinking of alignment research: rather than treating users as rational oracles, AI should provide cognitive support by actively helping users form and refine their intent through time. This requires an interdisciplinary approach that bridges machine learning, interface design, and behavioral science. We synthesize insights from these fields to characterize the mechanisms and failures of Fantasia interactions. We then show why existing interventions are insufficient, and propose a research agenda for designing and evaluating AI systems that better help humans navigate uncertainty in their tasks.

### 🤖 AI 总结

**一句话总结**：Modern AI assistants are trained to follow instructions, implicitly assuming that users can clearly articulate their goals and the kind of assistance they need. Decades of behavioral research, however...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Alignment, has, Fantasia, Problem, Modern, assistants, trained, follow

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21827v1) | [下载PDF](https://arxiv.org/pdf/2604.21827v1.pdf)

---

## cs.CL

## [4. Evaluation of Automatic Speech Recognition Using Generative Large Language Models](https://arxiv.org/abs/2604.21928v1)

**作者**：Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil 等 9 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-23

### 📄 论文摘要

Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.

### 🤖 AI 总结

**一句话总结**：Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human pe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Evaluation, Automatic, Speech, Recognition, Generative, Large, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21928v1) | [下载PDF](https://arxiv.org/pdf/2604.21928v1.pdf)

---

## [5. MathDuels: Evaluating LLMs as Problem Posers and Solvers](https://arxiv.org/abs/2604.21916v1)

**作者**：Zhiqiu Xu, Shibo Jin, Shreya Arya 等 4 位作者  
**分类**：cs.CL, cs.SE  
**发布时间**：2026-04-23

### 📄 论文摘要

As frontier language models attain near-ceiling performance on static mathematical benchmarks, existing evaluations are increasingly unable to differentiate model capabilities, largely because they cast models solely as solvers of fixed problem sets. We introduce MathDuels, a self-play benchmark in which models occupy dual roles: each authors math problems under adversarial prompting and solves problems authored by every other participant. Problems are produced through a three-stage generation pipeline (meta-prompting, problem generation, and difficulty amplification), and validated by an independent verifier that excludes ill-posed questions. A Rasch model (Rasch, 1993) jointly estimates solver abilities and problem difficulties; author quality is derived from the difficulties of each model's authored problems. Experiments across 19 frontier models reveal that authoring and solving capabilities are partially decoupled, and that dual-role evaluation reveals capability separations invisible in single-role benchmarks. As newer models enter the arena, they produce problems that defeat previously dominant solvers, so the benchmark's difficulty co-evolves with participant strength rather than saturating at a fixed ceiling. We host a public leaderboard that updates as new models are released.

### 🤖 AI 总结

**一句话总结**：As frontier language models attain near-ceiling performance on static mathematical benchmarks, existing evaluations are increasingly unable to differentiate model capabilities, largely because they ca...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, as, MathDuels, Evaluating, Problem, Posers, Solvers, frontier

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21916v1) | [下载PDF](https://arxiv.org/pdf/2604.21916v1.pdf)

---

## [6. GiVA: Gradient-Informed Bases for Vector-Based Adaptation](https://arxiv.org/abs/2604.21901v1)

**作者**：Neeraj Gangwar, Rishabh Deshmukh, Michael Shavlovsky 等 7 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-23

### 📄 论文摘要

As model sizes continue to grow, parameter-efficient fine-tuning has emerged as a powerful alternative to full fine-tuning. While LoRA is widely adopted among these methods, recent research has explored vector-based adaptation methods due to their extreme parameter efficiency. However, these methods typically require substantially higher ranks than LoRA to match its performance, leading to increased training costs. This work introduces GiVA, a gradient-based initialization strategy for vector-based adaptation. It achieves training times comparable to LoRA and maintains the extreme parameter efficiency of vector-based adaptation. We evaluate GiVA across diverse benchmarks, including natural language understanding, natural language generation, and image classification. Experiments show that our approach consistently outperforms or achieves performance competitive with existing vector-based adaptation methods and LoRA while reducing rank requirements by a factor of eight ($8\times$).

### 🤖 AI 总结

**一句话总结**：As model sizes continue to grow, parameter-efficient fine-tuning has emerged as a powerful alternative to full fine-tuning. While LoRA is widely adopted among these methods, recent research has explor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, GiVA, Gradient-Informed, Bases, Vector-Based, Adaptation, model, sizes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21901v1) | [下载PDF](https://arxiv.org/pdf/2604.21901v1.pdf)

---

## [7. Mapping the Political Discourse in the Brazilian Chamber of Deputies: A Multi-Faceted Computational Approach](https://arxiv.org/abs/2604.21897v1)

**作者**：Flávio Soriano, Victoria F. Mello, Pedro B. Rigueira 等 7 位作者  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-04-23

### 📄 论文摘要

Analyses of legislative behavior often rely on voting records, overlooking the rich semantic and rhetorical content of political speech. In this paper, we ask three complementary questions about parliamentary discourse: how things are said, what is being said, and who is speaking in discursively similar ways. To answer these questions, we introduce a scalable and generalizable computational framework that combines diachronic stylometric analysis, contextual topic modeling, and semantic clustering of deputies' speeches. We apply this framework to a large-scale case study of the Brazilian Chamber of Deputies, using a corpus of over 450,000 speeches from 2003 to 2025. Our results show a long-term stylistic shift toward shorter and more direct speeches, a legislative agenda that reorients sharply in response to national crises, and a granular map of discursive alignments in which regional and gender identities often prove more salient than formal party affiliation. More broadly, this work offers a robust methodology for analyzing parliamentary discourse as a multidimensional phenomenon that complements traditional vote-based approaches.

### 🤖 AI 总结

**一句话总结**：Analyses of legislative behavior often rely on voting records, overlooking the rich semantic and rhetorical content of political speech. In this paper, we ask three complementary questions about parli...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Mapping, Political, Discourse, Brazilian, Chamber, Deputies, Multi-Faceted

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21897v1) | [下载PDF](https://arxiv.org/pdf/2604.21897v1.pdf)

---

## [8. EVENT5Ws: A Large Dataset for Open-Domain Event Extraction from Documents](https://arxiv.org/abs/2604.21890v1)

**作者**：Praval Sharma, Ashok Samal, Leen-Kiat Soh 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-23

### 📄 论文摘要

Event extraction identifies the central aspects of events from text. It supports event understanding and analysis, which is crucial for tasks such as informed decision-making in emergencies. Therefore, it is necessary to develop automated event extraction approaches. However, existing datasets for algorithm development have limitations, including limited coverage of event types in closed-domain settings and a lack of large, manually verified dataset in open-domain settings. To address these limitations, we create EVENT5Ws , a large, manually annotated, and statistically verified open-domain event extraction dataset. We design a systematic annotation pipeline to create the dataset and provide empirical insights into annotation complexity. Using EVENT5Ws, we evaluate state-of-the-art pre-trained large language models and establish a benchmark for future research. We further show that models trained on EVENT5Ws generalize effectively to datasets from different geographical contexts, which demonstrates its potential for developing generalizable algorithms. Finally, we summarize the lessons learned during the dataset development and provide recommendations to support future large-scale dataset development.

### 🤖 AI 总结

**一句话总结**：Event extraction identifies the central aspects of events from text. It supports event understanding and analysis, which is crucial for tasks such as informed decision-making in emergencies. Therefore...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EVENT5Ws, Large, Dataset, Open-Domain, Event, Extraction, Documents, identifies

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21890v1) | [下载PDF](https://arxiv.org/pdf/2604.21890v1.pdf)

---

## [9. TingIS: Real-time Risk Event Discovery from Noisy Customer Incidents at Enterprise Scale](https://arxiv.org/abs/2604.21889v1)

**作者**：Jun Wang, Ziyin Zhang, Rui Wang 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-04-23

### 📄 论文摘要

Real-time detection and mitigation of technical anomalies are critical for large-scale cloud-native services, where even minutes of downtime can result in massive financial losses and diminished user trust. While customer incidents serve as a vital signal for discovering risks missed by monitoring, extracting actionable intelligence from this data remains challenging due to extreme noise, high throughput, and semantic complexity of diverse business lines. In this paper, we present TingIS, an end-to-end system designed for enterprise-grade incident discovery. At the core of TingIS is a multi-stage event linking engine that synergizes efficient indexing techniques with Large Language Models (LLMs) to make informed decisions on event merging, enabling the stable extraction of actionable incidents from just a handful of diverse user descriptions. This engine is complemented by a cascaded routing mechanism for precise business attribution and a multi-dimensional noise reduction pipeline that integrates domain knowledge, statistical patterns, and behavioral filtering. Deployed in a production environment handling a peak throughput of over 2,000 messages per minute and 300,000 messages per day, TingIS achieves a P90 alert latency of 3.5 minutes and a 95\% discovery rate for high-priority incidents. Benchmarks constructed from real-world data demonstrate that TingIS significantly outperforms baseline methods in routing accuracy, clustering quality, and Signal-to-Noise Ratio.

### 🤖 AI 总结

**一句话总结**：Real-time detection and mitigation of technical anomalies are critical for large-scale cloud-native services, where even minutes of downtime can result in massive financial losses and diminished user ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TingIS, Real-time, Risk, Event, Discovery, Noisy, Customer, Incidents

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21889v1) | [下载PDF](https://arxiv.org/pdf/2604.21889v1.pdf)

---

## [10. A Multimodal Text- and Graph-Based Approach for Open-Domain Event Extraction from Documents](https://arxiv.org/abs/2604.21885v1)

**作者**：Praval Sharma  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-23

### 📄 论文摘要

Event extraction is essential for event understanding and analysis. It supports tasks such as document summarization and decision-making in emergency scenarios. However, existing event extraction approaches have limitations: (1) closed-domain algorithms are restricted to predefined event types and thus rarely generalize to unseen types and (2) open-domain event extraction algorithms, capable of handling unconstrained event types, have largely overlooked the potential of large language models (LLMs) despite their advanced abilities. Additionally, they do not explicitly model document-level contextual, structural, and semantic reasoning, which are crucial for effective event extraction but remain challenging for LLMs due to lost-in-the-middle phenomenon and attention dilution. To address these limitations, we propose multimodal open-domain event extraction, MODEE , a novel approach for open-domain event extraction that combines graph-based learning with text-based representation from LLMs to model document-level reasoning. Empirical evaluations on large datasets demonstrate that MODEE outperforms state-of-the-art open-domain event extraction approaches and can be generalized to closed-domain event extraction, where it outperforms existing algorithms.

### 🤖 AI 总结

**一句话总结**：Event extraction is essential for event understanding and analysis. It supports tasks such as document summarization and decision-making in emergency scenarios. However, existing event extraction appr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multimodal, Text, Graph-Based, Approach, Open-Domain, Event, Extraction, Documents

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21885v1) | [下载PDF](https://arxiv.org/pdf/2604.21885v1.pdf)

---

## [11. Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms](https://arxiv.org/abs/2604.21882v1)

**作者**：Yuto Nishida, Naoki Shikoda, Yosuke Kishinami 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-23

### 📄 论文摘要

Understanding what kinds of factual knowledge large language models (LLMs) memorize is essential for evaluating their reliability and limitations. Entity-based QA is a common framework for analyzing non-verbatim memorization, but typical evaluations query each entity using a single canonical surface form, making it difficult to disentangle fact memorization from access through a particular name. We introduce RedirectQA, an entity-based QA dataset that uses Wikipedia redirect information to associate Wikidata factual triples with categorized surface forms for each entity, including alternative names, abbreviations, spelling variants, and common erroneous forms. Across 13 LLMs, we examine surface-conditioned factual memorization and find that prediction outcomes often change when only the entity surface form changes. This inconsistency is category-dependent: models are more robust to minor orthographic variations than to larger lexical variations such as aliases and abbreviations. Frequency analyses further suggest that both entity- and surface-level frequencies are associated with accuracy, and that entity frequency often contributes beyond surface frequency. Overall, factual memorization appears neither purely surface-specific nor fully surface-invariant, highlighting the importance of surface-form diversity in evaluating non-verbatim memorization.

### 🤖 AI 总结

**一句话总结**：Understanding what kinds of factual knowledge large language models (LLMs) memorize is essential for evaluating their reliability and limitations. Entity-based QA is a common framework for analyzing n...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Revisiting, Non-Verbatim, Memorization, Large, Language, Models, Role

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21882v1) | [下载PDF](https://arxiv.org/pdf/2604.21882v1.pdf)

---

## [12. Machine Behavior in Relational Moral Dilemmas: Moral Rightness, Predicted Human Behavior, and Model Decisions](https://arxiv.org/abs/2604.21871v1)

**作者**：Jiseon Kim, Jea Kwon, Luiz Felipe Vecchietti 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-23

### 📄 论文摘要

Human moral judgment is context-dependent and modulated by interpersonal relationships. As large language models (LLMs) increasingly function as decision-support systems, determining whether they encode these social nuances is critical. We characterize machine behavior using the Whistleblower's Dilemma by varying two experimental dimensions: crime severity and relational closeness. Our study evaluates three distinct perspectives: (1) moral rightness (prescriptive norms), (2) predicted human behavior (descriptive social expectations), and (3) autonomous model decision-making. By analyzing the reasoning processes, we identify a clear cross-perspective divergence: while moral rightness remains consistently fairness-oriented, predicted human behavior shifts significantly toward loyalty as relational closeness increases. Crucially, model decisions align with moral rightness judgments rather than their own behavioral predictions. This inconsistency suggests that LLM decision-making prioritizes rigid, prescriptive rules over the social sensitivity present in their internal world-modeling, which poses a gap that may lead to significant misalignments in real-world deployments.

### 🤖 AI 总结

**一句话总结**：Human moral judgment is context-dependent and modulated by interpersonal relationships. As large language models (LLMs) increasingly function as decision-support systems, determining whether they enco...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Machine, Behavior, Relational, Moral, Dilemmas, Rightness, Predicted, Human

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21871v1) | [下载PDF](https://arxiv.org/pdf/2604.21871v1.pdf)

---

## cs.CV

## [13. Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)

**作者**：Yen-Siang Wu, Rundong Luo, Jingsen Zhu 等 9 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-04-23

### 📄 论文摘要

How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.

### 🤖 AI 总结

**一句话总结**：How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Seeing, Fast, Slow, Learning, Flow, Time, Videos

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21931v1) | [下载PDF](https://arxiv.org/pdf/2604.21931v1.pdf)

---

## [14. Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs](https://arxiv.org/abs/2604.21926v1)

**作者**：Hao-Yu Hsu, Tianhang Cheng, Jing Wen 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-23

### 📄 论文摘要

Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.

### 🤖 AI 总结

**一句话总结**：Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, Seeing, Without, Eyes, Human-Scene, Understanding, Wearable, IMUs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21926v1) | [下载PDF](https://arxiv.org/pdf/2604.21926v1.pdf)

---

## [15. Context Unrolling in Omni Models](https://arxiv.org/abs/2604.21921v1)

**作者**：Ceyuan Yang, Zhijie Lin, Yang Zhao 等 19 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-23

### 📄 论文摘要

We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.

### 🤖 AI 总结

**一句话总结**：We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Context, Unrolling, Omni, Models, present, unified, multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21921v1) | [下载PDF](https://arxiv.org/pdf/2604.21921v1.pdf)

---

## [16. Vista4D: Video Reshooting with 4D Point Clouds](https://arxiv.org/abs/2604.21915v1)

**作者**：Kuan Heng Lin, Zhizheng Liu, Pablo Salamanca 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-23

### 📄 论文摘要

We present Vista4D, a robust and flexible video reshooting framework that grounds the input video and target cameras in a 4D point cloud. Specifically, given an input video, our method re-synthesizes the scene with the same dynamics from a different camera trajectory and viewpoint. Existing video reshooting methods often struggle with depth estimation artifacts of real-world dynamic videos, while also failing to preserve content appearance and failing to maintain precise camera control for challenging new trajectories. We build a 4D-grounded point cloud representation with static pixel segmentation and 4D reconstruction to explicitly preserve seen content and provide rich camera signals, and we train with reconstructed multiview dynamic data for robustness against point cloud artifacts during real-world inference. Our results demonstrate improved 4D consistency, camera control, and visual quality compared to state-of-the-art baselines under a variety of videos and camera paths. Moreover, our method generalizes to real-world applications such as dynamic scene expansion and 4D scene recomposition. See our project page for results, code, and models: https://eyeline-labs.github.io/Vista4D

### 🤖 AI 总结

**一句话总结**：We present Vista4D, a robust and flexible video reshooting framework that grounds the input video and target cameras in a 4D point cloud. Specifically, given an input video, our method re-synthesizes ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, We, Vista4D, Video, Reshooting, Point, Clouds, present

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21915v1) | [下载PDF](https://arxiv.org/pdf/2604.21915v1.pdf)

---

## [17. When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs](https://arxiv.org/abs/2604.21911v1)

**作者**：Pegah Khayatan, Jayneel Parekh, Arnaud Dapogny 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.CL, cs.LG  
**发布时间**：2026-04-23

### 📄 论文摘要

Despite impressive progress in capabilities of large vision-language models (LVLMs), these systems remain vulnerable to hallucinations, i.e., outputs that are not grounded in the visual input. Prior work has attributed hallucinations in LVLMs to factors such as limitations of the vision backbone or the dominance of the language component, yet the relative importance of these factors remains unclear. To resolve this ambiguity, We propose HalluScope, a benchmark to better understand the extent to which different factors induce hallucinations. Our analysis indicates that hallucinations largely stem from excessive reliance on textual priors and background knowledge, especially information introduced through textual instructions. To mitigate hallucinations induced by textual instruction priors, we propose HalluVL-DPO, a framework for fine-tuning off-the-shelf LVLMs towards more visually grounded responses. HalluVL-DPO leverages preference optimization using a curated training dataset that we construct, guiding the model to prefer grounded responses over hallucinated ones. We demonstrate that our optimized model effectively mitigates the targeted hallucination failure mode, while preserving or improving performance on other hallucination benchmarks and visual capability evaluations. To support reproducibility and further research, we will publicly release our evaluation benchmark, preference training dataset, and code at https://pegah-kh.github.io/projects/prompts-override-vision/ .

### 🤖 AI 总结

**一句话总结**：Despite impressive progress in capabilities of large vision-language models (LVLMs), these systems remain vulnerable to hallucinations, i.e., outputs that are not grounded in the visual input. Prior w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Prompts, Override, Vision, Prompt-Induced, Hallucinations, LVLMs, Despite

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21911v1) | [下载PDF](https://arxiv.org/pdf/2604.21911v1.pdf)

---

## [18. Directional Confusions Reveal Divergent Inductive Biases Through Rate-Distortion Geometry in Human and Machine Vision](https://arxiv.org/abs/2604.21909v1)

**作者**：Leyla Roksan Caglar, Pedro A. M. Mediano, Baihan Lin  
**分类**：cs.CV, cs.IT, q-bio.NC  
**发布时间**：2026-04-23

### 📄 论文摘要

Humans and modern vision models can reach similar classification accuracy while making systematically different kinds of mistakes - differing not in how often they err, but in who gets mistaken for whom, and in which direction. We show that these directional confusions reveal distinct inductive biases that are invisible to accuracy alone. Using matched human and deep vision model responses on a natural-image categorization task under 12 perturbation types, we quantify asymmetry in confusion matrices and link it to generalization geometry through a Rate-Distortion (RD) framework, summarized by three geometric signatures (slope (beta), curvature (kappa)) and efficiency (AUC). We find that humans exhibit broad but weak asymmetries, whereas deep vision models show sparser, stronger directional collapses. Robustness training reduces global asymmetry but fails to recover the human-like breadth-strength profile of graded similarity. Mechanistic simulations further show that different asymmetry organizations shift the RD frontier in opposite directions, even when matched for performance. Together, these results position directional confusions and RD geometry as compact, interpretable signatures of inductive bias under distribution shift.

### 🤖 AI 总结

**一句话总结**：Humans and modern vision models can reach similar classification accuracy while making systematically different kinds of mistakes - differing not in how often they err, but in who gets mistaken for wh...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Directional, Confusions, Reveal, Divergent, Inductive, Biases, Through, Rate-Distortion

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21909v1) | [下载PDF](https://arxiv.org/pdf/2604.21909v1.pdf)

---

## [19. UniGenDet: A Unified Generative-Discriminative Framework for Co-Evolutionary Image Generation and Generated Image Detection](https://arxiv.org/abs/2604.21904v1)

**作者**：Yanran Zhang, Wenzhao Zheng, Yifei Li 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-23

### 📄 论文摘要

In recent years, significant progress has been made in both image generation and generated image detection. Despite their rapid, yet largely independent, development, these two fields have evolved distinct architectural paradigms: the former predominantly relies on generative networks, while the latter favors discriminative frameworks. A recent trend in both domains is the use of adversarial information to enhance performance, revealing potential for synergy. However, the significant architectural divergence between them presents considerable challenges. Departing from previous approaches, we propose UniGenDet: a Unified generative-discriminative framework for co-evolutionary image Generation and generated image Detection. To bridge the task gap, we design a symbiotic multimodal self-attention mechanism and a unified fine-tuning algorithm. This synergy allows the generation task to improve the interpretability of authenticity identification, while authenticity criteria guide the creation of higher-fidelity images. Furthermore, we introduce a detector-informed generative alignment mechanism to facilitate seamless information exchange. Extensive experiments on multiple datasets demonstrate that our method achieves state-of-the-art performance. Code: \href{https://github.com/Zhangyr2022/UniGenDet}{https://github.com/Zhangyr2022/UniGenDet}.

### 🤖 AI 总结

**一句话总结**：In recent years, significant progress has been made in both image generation and generated image detection. Despite their rapid, yet largely independent, development, these two fields have evolved dis...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UniGenDet, Unified, Framework, Co-Evolutionary, Image, Generation, Generated, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21904v1) | [下载PDF](https://arxiv.org/pdf/2604.21904v1.pdf)

---

## [20. Addressing Image Authenticity When Cameras Use Generative AI](https://arxiv.org/abs/2604.21879v1)

**作者**：Umar Masud, Abhijith Punnappurath, Luxi Zhao 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-23

### 📄 论文摘要

The ability of generative AI (GenAI) methods to photorealistically alter camera images has raised awareness about the authenticity of images shared online. Interestingly, images captured directly by our cameras are considered authentic and faithful. However, with the increasing integration of deep-learning modules into cameras' capture-time hardware -- namely, the image signal processor (ISP) -- there is now a potential for hallucinated content in images directly output by our cameras. Hallucinated capture-time image content is typically benign, such as enhanced edges or texture, but in certain operations, such as AI-based digital zoom or low-light image enhancement, hallucinations can potentially alter the semantics and interpretation of the image content. As a result, users may not realize that the content in their camera images is not authentic. This paper addresses this issue by enabling users to recover the 'unhallucinated' version of the camera image to avoid misinterpretation of the image content. Our approach works by optimizing an image-specific multi-layer perceptron (MLP) decoder together with a modality-specific encoder so that, given the camera image, we can recover the image before hallucinated content was added. The encoder and MLP are self-contained and can be applied post-capture to the image without requiring access to the camera ISP. Moreover, the encoder and MLP decoder require only 180 KB of storage and can be readily saved as metadata within standard image formats such as JPEG and HEIC.

### 🤖 AI 总结

**一句话总结**：The ability of generative AI (GenAI) methods to photorealistically alter camera images has raised awareness about the authenticity of images shared online. Interestingly, images captured directly by o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Addressing, Image, Authenticity, When, Cameras, Use, Generative, ability

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21879v1) | [下载PDF](https://arxiv.org/pdf/2604.21879v1.pdf)

---

## [21. Grounding Video Reasoning in Physical Signals](https://arxiv.org/abs/2604.21873v1)

**作者**：Alibay Osmanli, Zixu Cheng, Shaogang Gong  
**分类**：cs.CV  
**发布时间**：2026-04-23

### 📄 论文摘要

Physical video understanding requires more than naming an event correctly. A model can answer a question about pouring, sliding, or collision from textual regularities while still failing to localize the event in time or space. We introduce a grounded benchmark for physical video understanding that extends the what--when--where evaluation structure of V-STaR to four video sources, six physics domains, three prompt families (physics, vstar_like, and neutral_rstr), and four input conditions (original, shuffled, ablated, and frame-masked). The benchmark contains 1,560 base video clips from SSV2, YouCook2, HoloAssist, and Roundabout-TAU. Each clip is first converted into a shared grounded event record, and the three query families are derived from that record. Temporal and spatial targets are shared across prompt families, while the non-physics families use deterministic family-appropriate semantic a_what targets derived from the same record. Across models and prompt families, physics remains the strongest regime overall, vstar_like is the clearest non-physics semantic comparison, and neutral_rstr behaves as a harder templated control. Prompt-family robustness is selective rather than universal, perturbation gains cluster in weak original cases, and spatial grounding is the weakest across settings. These results suggest that video Q&A reasoning benchmarks shall report physically grounded, prompt-aware, and perturbation-aware diagnostics alongside aggregate accuracy.

### 🤖 AI 总结

**一句话总结**：Physical video understanding requires more than naming an event correctly. A model can answer a question about pouring, sliding, or collision from textual regularities while still failing to localize ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Grounding, Video, Reasoning, Physical, Signals, understanding, requires, more

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21873v1) | [下载PDF](https://arxiv.org/pdf/2604.21873v1.pdf)

---

## [22. Divide-then-Diagnose: Weaving Clinician-Inspired Contexts for Ultra-Long Capsule Endoscopy Videos](https://arxiv.org/abs/2604.21814v1)

**作者**：Bowen Liu, Li Yang, Shanshan Song 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-23

### 📄 论文摘要

Capsule endoscopy (CE) enables non-invasive gastrointestinal screening, but current CE research remains largely limited to frame-level classification and detection, leaving video-level analysis underexplored. To bridge this gap, we introduce and formally define a new task, diagnosis-driven CE video summarization, which requires extracting key evidence frames that covers clinically meaningful findings and making accurate diagnoses from those evidence frames. This setting is challenging because diagnostically relevant events are extremely sparse and can be overwhelmed by tens of thousands of redundant normal frames, while individual observations are often ambiguous due to motion blur, debris, specular highlights, and rapid viewpoint changes. To facilitate research in this direction, we introduce VideoCAP, the first CE dataset with diagnosis-driven annotations derived from real clinical reports. VideoCAP comprises 240 full-length videos and provides realistic supervision for both key evidence frame extraction and diagnosis. To address this task, we further propose DiCE, a clinician-inspired framework that mirrors the standard CE reading workflow. DiCE first performs efficient candidate screening over the raw video, then uses a Context Weaver to organize candidates into coherent diagnostic contexts that preserve distinct lesion events, and an Evidence Converger to aggregate multi-frame evidence within each context into robust clip-level judgments. Experiments show that DiCE consistently outperforms state-of-the-art methods, producing concise and clinically reliable diagnostic summaries. These results highlight diagnosis-driven contextual reasoning as a promising paradigm for ultra-long CE video summarization.

### 🤖 AI 总结

**一句话总结**：Capsule endoscopy (CE) enables non-invasive gastrointestinal screening, but current CE research remains largely limited to frame-level classification and detection, leaving video-level analysis undere...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Divide-then-Diagnose, Weaving, Clinician-Inspired, Contexts, Ultra-Long, Capsule, Endoscopy, Videos

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21814v1) | [下载PDF](https://arxiv.org/pdf/2604.21814v1.pdf)

---

## [23. Multiscale Super Resolution without Image Priors](https://arxiv.org/abs/2604.21810v1)

**作者**：Daniel Fu, Gabby Litterio, Pedro Felzenszwalb 等 4 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-04-23

### 📄 论文摘要

We address the ambiguities in the super-resolution problem under translation. We demonstrate that combinations of low-resolution images at different scales can be used to make the super-resolution problem well posed. Such differences in scale can be achieved using sensors with different pixel sizes (as demonstrated here) or by varying the effective pixel size through changes in optical magnification (e.g., using a zoom lens). We show that images acquired with pairwise coprime pixel sizes lead to a system with a stable inverse, and furthermore, that super-resolution images can be reconstructed efficiently using Fourier domain techniques or iterative least squares methods. Our mathematical analysis provides an expression for the expected error of the least squares reconstruction for large signals assuming i.i.d. noise that elucidates the noise-resolution tradeoff. These results are validated through both one- and two-dimensional experiments that leverage charge-coupled device (CCD) hardware binning to explore reconstructions over a large range of effective pixel sizes. Finally, two-dimensional reconstructions for a series of targets are used to demonstrate the advantages of multiscale super-resolution, and implications of these results for common imaging systems are discussed.

### 🤖 AI 总结

**一句话总结**：We address the ambiguities in the super-resolution problem under translation. We demonstrate that combinations of low-resolution images at different scales can be used to make the super-resolution pro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Multiscale, Super, Resolution, without, Image, Priors, address

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21810v1) | [下载PDF](https://arxiv.org/pdf/2604.21810v1.pdf)

---

## cs.LG

## [24. Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability](https://arxiv.org/abs/2604.21930v1)

**作者**：Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-23

### 📄 论文摘要

Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutral preprocessing choice, but a structural component of evaluation: different valid splits of the same stream can induce different CL regimes and therefore different benchmark conclusions. To study this effect, we introduce a taskification-level framework based on plasticity and stability profiles, a profile distance between taskifications, and Boundary-Profile Sensitivity (BPS), which diagnoses how strongly small boundary perturbations alter the induced regime before any CL model is trained. We evaluate continual finetuning, Experience Replay, Elastic Weight Consolidation, and Learning without Forgetting on network traffic forecasting with CESNET-Timeseries24, keeping the stream, model, and training budget fixed while varying only the temporal taskification. Across 9-, 30-, and 44-day splits, we observe substantial changes in forecasting error, forgetting, and backward transfer, showing that taskification alone can materially affect CL evaluation. We further find that shorter taskifications induce noisier distribution-level patterns, larger structural distances, and higher BPS, indicating greater sensitivity to boundary perturbations. These results show that benchmark conclusions in streaming CL depend not only on the learner and the data stream, but also on how that stream is taskified, motivating temporal taskification as a first-class evaluation variable.

### 🤖 AI 总结

**一句话总结**：Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Temporal, Taskification, Streaming, Continual, Learning, Evaluation, Instability

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21930v1) | [下载PDF](https://arxiv.org/pdf/2604.21930v1.pdf)

---

## [25. Fine-Tuning Regimes Define Distinct Continual Learning Problems](https://arxiv.org/abs/2604.21927v1)

**作者**：Paul-Tiberiu Iordache, Elena Burceanu  
**分类**：cs.LG  
**发布时间**：2026-04-23

### 📄 论文摘要

Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.

### 🤖 AI 总结

**一句话总结**：Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CL, Fine-Tuning, Regimes, Define, Distinct, Continual, Learning, Problems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21927v1) | [下载PDF](https://arxiv.org/pdf/2604.21927v1.pdf)

---

## [26. The Sample Complexity of Multicalibration](https://arxiv.org/abs/2604.21923v1)

**作者**：Natalie Collina, Jiuyao Lu, Georgy Noarov 等 4 位作者  
**分类**：cs.LG, math.ST, stat.ML  
**发布时间**：2026-04-23

### 📄 论文摘要

We study the minimax sample complexity of multicalibration in the batch setting. A learner observes $n$ i.i.d. samples from an unknown distribution and must output a (possibly randomized) predictor whose population multicalibration error, measured by Expected Calibration Error (ECE), is at most $\varepsilon$ with respect to a given family of groups. For every fixed $κ> 0$, in the regime $|G|\le \varepsilon^{-κ}$, we prove that $\widetildeΘ(\varepsilon^{-3})$ samples are necessary and sufficient, up to polylogarithmic factors. The lower bound holds even for randomized predictors, and the upper bound is realized by a randomized predictor obtained via an online-to-batch reduction. This separates the sample complexity of multicalibration from that of marginal calibration, which scales as $\widetildeΘ(\varepsilon^{-2})$, and shows that mean-ECE multicalibration is as difficult in the batch setting as it is in the online setting, in contrast to marginal calibration which is strictly more difficult in the online setting. In contrast we observe that for $κ= 0$, the sample complexity of multicalibration remains $\widetildeΘ(\varepsilon^{-2})$ exhibiting a sharp threshold phenomenon.   More generally, we establish matching upper and lower bounds, up to polylogarithmic factors, for a weighted $L_p$ multicalibration metric for all $1 \le p \le 2$, with optimal exponent $3/p$. We also extend the lower-bound template to a regular class of elicitable properties, and combine it with the online upper bounds of Hu et al. (2025) to obtain matching bounds for calibrating properties including expectiles and bounded-density quantiles.

### 🤖 AI 总结

**一句话总结**：We study the minimax sample complexity of multicalibration in the batch setting. A learner observes $n$ i.i.d. samples from an unknown distribution and must output a (possibly randomized) predictor wh...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, We, Sample, Complexity, Multicalibration, study, minimax, batch

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21923v1) | [下载PDF](https://arxiv.org/pdf/2604.21923v1.pdf)

---

## [27. Low-Rank Adaptation Redux for Large Models](https://arxiv.org/abs/2604.21905v1)

**作者**：Bingcong Li, Yilang Zhang, Georgios B. Giannakis  
**分类**：cs.LG, eess.SP  
**发布时间**：2026-04-23

### 📄 论文摘要

Low-rank adaptation (LoRA) has emerged as the de facto standard for parameter-efficient fine-tuning (PEFT) of foundation models, enabling the adaptation of billion-parameter networks with minimal computational and memory overhead. Despite its empirical success and rapid proliferation of variants, it remains elusive which architectural choices, optimization techniques, and deployment constraints should guide practical method selection. This overview revisits LoRA through the lens of signal processing (SP), bridging modern adapter designs with classical low-rank modeling tools and inverse problems, as well as highlighting how SP principles can inform principled advances of fine-tuning approaches. Rather than providing a comprehensive enumeration and empirical comparisons of LoRA variants, emphasis is placed on the technical mechanisms underpinning these approaches to justify their effectiveness. These advances are categorized into three complementary axes: architectural design, efficient optimization, and pertinent applications. The first axis builds on singular value decomposition (SVD)-based factorization, rank-augmentation constructions, and cross-layer tensorization, while the second axis deals with initialization, alternating solvers, gauge-invariant optimization, and parameterization-aware methods. Beyond fine-tuning, emerging applications of LoRA are accounted across the entire lifecycle of large models, ranging from pre- and post-training to serving/deployment. Finally, open research directions are outlined at the confluence of SP and deep learning to catalyze a bidirectional frontier: classical SP tools provide a principled vocabulary for designing principled PEFT methods, while the unique challenges facing modern deep learning, especially the overwhelming scale and prohibitive overhead, also offer new research lines benefiting the SP community in return.

### 🤖 AI 总结

**一句话总结**：Low-rank adaptation (LoRA) has emerged as the de facto standard for parameter-efficient fine-tuning (PEFT) of foundation models, enabling the adaptation of billion-parameter networks with minimal comp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Low-Rank, Adaptation, Redux, Large, Models, LoRA, has, emerged

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21905v1) | [下载PDF](https://arxiv.org/pdf/2604.21905v1.pdf)

---

## [28. A Scale-Adaptive Framework for Joint Spatiotemporal Super-Resolution with Diffusion Models](https://arxiv.org/abs/2604.21903v1)

**作者**：Max Defez, Filippo Quarenghi, Mathieu Vrac 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-23

### 📄 论文摘要

Deep-learning video super-resolution has progressed rapidly, but climate applications typically super-resolve (increase resolution) either space or time, and joint spatiotemporal models are often designed for a single pair of super-resolution (SR) factors (upscaling spatial and temporal ratio between the low-resolution sequence and the high-resolution sequence), limiting transfer across spatial resolutions and temporal cadences (frame rates). We present a scale-adaptive framework that reuses the same architecture across factors by decomposing spatiotemporal SR into a deterministic prediction of the conditional mean, with attention, and a residual conditional diffusion model, with an optional mass-conservation (same precipitation amount in inputs and outputs) transform to preserve aggregated totals. Assuming that larger SR factors primarily increase underdetermination (hence required context and residual uncertainty) rather than changing the conditional-mean structure, scale adaptivity is achieved by retuning three factor-dependent hyperparameters before retraining: the diffusion noise schedule amplitude beta (larger for larger factors to increase diversity), the temporal context length L (set to maintain comparable attention horizons across cadences) and optionally a third, the mass-conservation function f (tapered to limit the amplification of extremes for large factors). Demonstrated on reanalysis precipitation over France (Comephore), the same architecture spans super-resolution factors from 1 to 25 in space and 1 to 6 in time, yielding a reusable architecture and tuning recipe for joint spatiotemporal super-resolution across scales.

### 🤖 AI 总结

**一句话总结**：Deep-learning video super-resolution has progressed rapidly, but climate applications typically super-resolve (increase resolution) either space or time, and joint spatiotemporal models are often desi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Scale-Adaptive, Framework, Joint, Spatiotemporal, Super-Resolution, Models, Deep-learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21903v1) | [下载PDF](https://arxiv.org/pdf/2604.21903v1.pdf)

---

## [29. GFlowState: Visualizing the Training of Generative Flow Networks Beyond the Reward](https://arxiv.org/abs/2604.21830v1)

**作者**：Florian Holeczek, Andreas Hinterreiter, Alex Hernandez-Garcia 等 5 位作者  
**分类**：cs.LG, cs.HC  
**发布时间**：2026-04-23

### 📄 论文摘要

We present GFlowState, a visual analytics system designed to illuminate the training process of Generative Flow Networks (GFlowNets or GFNs). GFlowNets are a probabilistic framework for generating samples proportionally to a reward function. While GFlowNets have proved to be powerful tools in applications such as molecule and material discovery, their training dynamics remain difficult to interpret. Standard machine learning tools allow metric tracking but do not reveal how models explore the sample space, construct sample trajectories, or shift sampling probabilities during training. Our solution, GFlowState, allows users to analyze sampling trajectories, compare the sample space relative to reference datasets, and analyze the training dynamics. To this end, we introduce multiple views, including a chart of candidate rankings, a state projection, a node-link diagram of the trajectory network, and a transition heatmap. These visualizations enable GFlowNet developers and users to investigate sampling behavior and policy evolution, and to identify underexplored regions and sources of training failure. Case studies demonstrate how the system supports debugging and assessing the quality of GFlowNets across application domains. By making the structural dynamics of GFlowNets observable, our work enhances their interpretability and can accelerate GFlowNet development in practice.

### 🤖 AI 总结

**一句话总结**：We present GFlowState, a visual analytics system designed to illuminate the training process of Generative Flow Networks (GFlowNets or GFNs). GFlowNets are a probabilistic framework for generating sam...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, GFlowState, Visualizing, Training, Generative, Flow, Networks, Beyond

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21830v1) | [下载PDF](https://arxiv.org/pdf/2604.21830v1.pdf)

---

## [30. Probably Approximately Consensus: On the Learning Theory of Finding Common Ground](https://arxiv.org/abs/2604.21811v1)

**作者**：Carter Blair, Ben Armstrong, Shiri Alouf-Heffetz 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.MA  
**发布时间**：2026-04-23

### 📄 论文摘要

A primary goal of online deliberation platforms is to identify ideas that are broadly agreeable to a community of users through their expressed preferences. Yet, consensus elicitation should ideally extend beyond the specific statements provided by users and should incorporate the relative salience of particular topics. We address this issue by modelling consensus as an interval in a one-dimensional opinion space derived from potentially high-dimensional data via embedding and dimensionality reduction. We define an objective that maximizes expected agreement within a hypothesis interval where the expectation is over an underlying distribution of issues, implicitly taking into account their salience. We propose an efficient Empirical Risk Minimization (ERM) algorithm and establish PAC-learning guarantees. Our initial experiments demonstrate the performance of our algorithm and examine more efficient approaches to identifying optimal consensus regions. We find that through selectively querying users on an existing sample of statements, we can reduce the number of queries needed to a practical number.

### 🤖 AI 总结

**一句话总结**：A primary goal of online deliberation platforms is to identify ideas that are broadly agreeable to a community of users through their expressed preferences. Yet, consensus elicitation should ideally e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Probably, Approximately, Consensus, Learning, Theory, Finding, Common

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.21811v1) | [下载PDF](https://arxiv.org/pdf/2604.21811v1.pdf)

---

