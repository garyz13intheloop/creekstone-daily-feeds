# arXiv AI 论文日报 | 2026-06-24

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (17 篇)
- [cs.AI](#csAI) (8 篇)
- [cs.LG](#csLG) (2 篇)
- [cs.CL](#csCL) (3 篇)

---

## cs.AI

## [1. OpenThoughts-Agent: Data Recipes for Agentic Models](https://arxiv.org/abs/2606.24855v1)

**作者**：Negin Raoof, Richard Zhuang, Marianna Nezhurina 等 50 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-23

### 📄 论文摘要

Agentic language models dramatically expand the applications of AI yet little is publicly known about how to curate training data for broadly capable agents. Existing open efforts such as SWE-Smith, SERA, and Nemotron-Terminal typically target a single benchmark, leaving open the question of how to train models that generalize across diverse agentic tasks. The OpenThoughts-Agent (OT-Agent) project addresses this gap with a fully open data curation pipeline for training agentic models. We conduct more than 100 controlled ablation experiments to systematically investigate each stage of the pipeline, yielding insights on the importance of task sources and diversity. We then assemble a training set of 100K examples from our pipeline and fine-tune Qwen3-32B on this dataset, which yields an average accuracy of 44.8% across seven agentic benchmarks and a 3.9 percentage point improvement over the strongest existing open data agentic model (Nemotron-Terminal-32B, 40.9%). Moreover, our training data exhibits strong scaling properties, outperforming alternative open datasets at every training set size in compute-controlled comparisons. We publicly release our training sets, data pipeline, experimental data, and models at openthoughts.ai to support future open research on agentic model training.

### 🤖 AI 总结

**一句话总结**：Agentic language models dramatically expand the applications of AI yet little is publicly known about how to curate training data for broadly capable agents. Existing open efforts such as SWE-Smith, S...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OpenThoughts-Agent, Data, Recipes, Agentic, Models, language, dramatically, expand

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24855v1) | [下载PDF](https://arxiv.org/pdf/2606.24855v1.pdf)

---

## [2. World Models in Pieces: Structural Certification for General Agents](https://arxiv.org/abs/2606.24842v1)

**作者**：Yikai Lu, Yifei Wu, Xinyu Lu 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-23

### 📄 论文摘要

In the big-world regime, agents cannot be universally capable and their ability is inevitably specialized across a world model in pieces. Consequently, standard uniform guarantees fail to distinguish between the understanding of critical bottlenecks and irrelevant failures. We first formalize this limitation by proving that general agents are not universal, rendering standard worst-case analysis uninformative. To overcome this, we introduce structural certification, a transition-local framework that maps bounded goal-conditioned performance to entry-wise guarantees on the agent's internal world model. Our main contribution is constructive. We provide algorithms that filter specific transitions using deep compositional goals and prove that a general agent on these goals has a structural world model with a $\mathcal{O}(1/n) + \mathcal{O}(δ)$ error bound. Conversely, this bound is tight in the small-$δ$ regime, whose existence is explicitly guaranteed by our certification. These results enable the certifiable deployment of general agents by localizing the specific transitions where long-horizon planning is reliable.

### 🤖 AI 总结

**一句话总结**：In the big-world regime, agents cannot be universally capable and their ability is inevitably specialized across a world model in pieces. Consequently, standard uniform guarantees fail to distinguish ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, World, Models, Pieces, Structural, Certification, General, big-world

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24842v1) | [下载PDF](https://arxiv.org/pdf/2606.24842v1.pdf)

---

## [3. Matching Tasks to Objectives: Fine-Tuning and Prompt-Tuning Strategies for Encoder-Decoder Pre-trained Language Models](https://arxiv.org/abs/2606.24841v1)

**作者**：Ahmad Pouramini, Hesham Faili  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-06-23

### 📄 论文摘要

Prompt-based learning has emerged as a dominant paradigm in natural language processing. This study explores the impact of diverse pre-training objectives on the performance of encoder-decoder pre-trained language models across generation and question answering tasks, with a focus on commonsense knowledge retrieval and completion. We highlight the benefits of incorporating multiple objectives during both pre-training and fine-tuning stages. We introduce the Match Task to Objective (MTO) framework and methods for determining the appropriate objective for a given task. This framework offers automated methods to prepare task-related data for adaptation through unsupervised training, based on the identified objective. In the fine-tuning stage, we design novel templates that align with the objectives of the pre-training and adaptation stages. When aligned with task requirements, these strategies can achieve a performance gain of over 120\% compared to conventional methods in few-shot settings. They significantly outperform related works in few-shot settings and exceed the baseline even in full-dataset scenarios. Furthermore, we extend this approach to include prompt-tuning methodologies, providing guidance for more effective soft prompt engineering and optimization. Our strategies significantly enhance prompt-tuning performance as well. These insights hold substantial value, precisely guiding the selection and optimization of models customized for specific tasks. Code is available at https://github.com/puraminy/MTO/

### 🤖 AI 总结

**一句话总结**：Prompt-based learning has emerged as a dominant paradigm in natural language processing. This study explores the impact of diverse pre-training objectives on the performance of encoder-decoder pre-tra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Matching, Tasks, Objectives, Fine-Tuning, Prompt-Tuning, Strategies, Encoder-Decoder, Pre-trained

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24841v1) | [下载PDF](https://arxiv.org/pdf/2606.24841v1.pdf)

---

## [4. Grading the Grader: Lessons from Evaluating an Agentic Data Analysis System](https://arxiv.org/abs/2606.24839v1)

**作者**：Tian Zheng, Kai-Tai Hsu  
**分类**：cs.AI, stat.AP  
**发布时间**：2026-06-23

### 📄 论文摘要

Agentic data analysis systems produce rich outputs, including code, numerical results, and verbal diagnostics. This makes them more challenging to evaluate than single-turn LLM responses. It is therefore necessary to distinguish genuine disagreement between an agent's output and a ground-truth answer from grading artifacts. We investigate how reliably automated graders assess such a system and what strategies improve grading quality by applying LAMBDA, a multi-agent data-analysis system, on 153 numerical QRData tasks from DSGym. We develop and evaluate a three-layer human-AI grading cascade: strict regex matching, LLM-based lenient grading, and snippet-based human inspection, which combines non-GenAI and GenAI strategies with different failure profiles. Both automated graders achieve 100% observed precision (0/70 false positives). The lenient grader's recall is 97% against human labels. A keyword-anchored extraction pipeline raises the strict grader's recall by 60 percentage points over a last-number heuristic; the lenient grader is architecturally parser-independent. An iterative nudge mechanism raises grading run success from 36% to 97% and lenient-pass rates from 16% to 46%; comparing nudging with and without original-question re-injection shows that re-injection offers no benefit, confirming the nudge as an answer template cue. We further observe in this case study that variable type is the task metadata field most consistently associated with grading pipeline dynamics and observed outcome grades.

### 🤖 AI 总结

**一句话总结**：Agentic data analysis systems produce rich outputs, including code, numerical results, and verbal diagnostics. This makes them more challenging to evaluate than single-turn LLM responses. It is theref...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Grading, Grader, Lessons, Evaluating, Agentic, Data, Analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24839v1) | [下载PDF](https://arxiv.org/pdf/2606.24839v1.pdf)

---

## [5. Accuracy and Satisfaction in Multi-Turn LLM Dialogues for NFR Assessment](https://arxiv.org/abs/2606.24834v1)

**作者**：Ali Pourghasemi Fatideh, Wilder Baldwin, Maria Dhakal 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-23

### 📄 论文摘要

LLM-based dialogue assistants have become mainstream tools for software developers, yet current evaluation benchmarks focus exclusively on functional correctness. This leaves a critical gap in assessing the quality and accuracy of these conversations when handling Non-Functional Requirements (NFRs), which are inherently vague, context-dependent, and involve many parts of a program. Evaluating how well these systems support collaborative reasoning about NFRs requires methods that go beyond single-turn accuracy to capture both the correctness of the system's outputs and the quality of the multi-turn interaction. In this paper, we investigate the accuracy and quality of multi-turn conversations between developers and an LLM-based agent in the domain of Health Insurance Portability and Accountability Act (HIPAA) regulatory compliance. We hired 49 programmers to interact with GitHub Copilot to assess 148 HIPAA-derived NFRs against the iTrust codebase, a system designed to comply with HIPAA regulations, across three dimensions: requirement satisfaction level, reasoning, and code localization. We find that developers tend to agree with LLM assessments, but accuracy against expert ground truth is low. We model user satisfaction and find that longer system responses and more information-providing turns negatively affect user satisfaction, whereas proactive interactions positively affect it. Our findings provide insights for designing LLM-based dialogue systems that support NFR assessment.

### 🤖 AI 总结

**一句话总结**：LLM-based dialogue assistants have become mainstream tools for software developers, yet current evaluation benchmarks focus exclusively on functional correctness. This leaves a critical gap in assessi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Accuracy, Satisfaction, Multi-Turn, Dialogues, NFR, Assessment, LLM-based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24834v1) | [下载PDF](https://arxiv.org/pdf/2606.24834v1.pdf)

---

## [6. Solving Inverse Problems of Chaotic Systems with Bidirectional Conditional Flow Matching](https://arxiv.org/abs/2606.24824v1)

**作者**：Peiyan Hu, Jian Zhang, Jiashu Pan 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-23

### 📄 论文摘要

Modeling chaotic systems is crucial yet challenging. Inverse problems in chaotic dynamics, namely inferring initial conditions from final states, remain largely unsolved because of ill-posedness, non-uniqueness, instability, and potentially chaotic time-reverse dynamics. We address this open problem with Bidirectional Conditional Flow Matching (Bi-CFM), which learns bidirectional mappings between distributions of initial and final states to capture the stochasticity of chaotic evolution and mitigate exponential error accumulation over time. Furthermore, for systems with conservation laws, we extend it to Conservation-constrained Bi-CFM (CBi-CFM). Across the classic Lorenz, Circuit, and high-dimensional Lorenz 96 systems, Bi-CFM improves five distribution-level metrics over baselines while achieving a speedup of more than two orders of magnitude. In the three-body planet-planet scattering problem in planetary dynamics, CBi-CFM better respects conservation laws, with conservation errors comparable to those of the ground truth. Finally, on real observations of globular clusters, collisional million-body systems shaped by $\sim 10^{10}$ years (10 Gyr) of evolution, our method represents an advance in accuracy, establishing a scalable route to solving inverse problems of long-timescale real-world chaotic dynamics.

### 🤖 AI 总结

**一句话总结**：Modeling chaotic systems is crucial yet challenging. Inverse problems in chaotic dynamics, namely inferring initial conditions from final states, remain largely unsolved because of ill-posedness, non-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Solving, Inverse, Problems, Chaotic, Systems, Bidirectional, Conditional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24824v1) | [下载PDF](https://arxiv.org/pdf/2606.24824v1.pdf)

---

## [7. Assessing Distribution Shift in Human Activity Recognition for Domain Generalization](https://arxiv.org/abs/2606.24781v1)

**作者**：Rebecca Adaimi, Edison Thomaz  
**分类**：cs.AI, cs.HC  
**发布时间**：2026-06-23

### 📄 论文摘要

While the field of Human Activity Recognition (HAR) continues to draw interest from researchers and advance in important ways, some key challenges remain. One of the most difficult aspects of building HAR models that show good performance in real-world settings is dealing with data diversity from device and sensor heterogeneity, and contextual changes that are intrinsic to real-world applications. While data diversity in HAR has been well-acknowledged in the literature, there remains a gap in understanding the effect of various types of distribution shifts on HAR models and the domain generalization problem that arises. Towards that end, this paper systematically evaluates 4 different types of distribution shifts, including variations in device type, sensor placement, sampling rate, and user behavior. Quantifying their effects, we illustrate that diversity shifts predominantly define all types of shifts, indicating the existence of unique features that are not shared across different domains. We then introduce a uniform HAR-based distribution shift benchmarks and conduct a comprehensive evaluation of up to 28 domain generalization methods. Our analysis exposes the limitations of current domain generalization algorithms in achieving model generalizability, marginally outperforming the empirical risk minimization baseline. This work represents the first systematic exploration of domain generalization and adaptation concerning specific distribution shifts in sensor-based HAR, offering an open-source benchmark platform and datasets to spur further research.

### 🤖 AI 总结

**一句话总结**：While the field of Human Activity Recognition (HAR) continues to draw interest from researchers and advance in important ways, some key challenges remain. One of the most difficult aspects of building...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Assessing, Distribution, Shift, Human, Activity, Recognition, Domain, Generalization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24781v1) | [下载PDF](https://arxiv.org/pdf/2606.24781v1.pdf)

---

## [8. Can Scale Save Us From Plasticity Loss in Large Language Models?](https://arxiv.org/abs/2606.24752v1)

**作者**：J. Fernando Hernandez-Garcia, Tomás Figliolia, Beren Millidge  
**分类**：cs.AI  
**发布时间**：2026-06-23

### 📄 论文摘要

The loss of plasticity - the ability of a network to learn new information after having already learned older information - is a fundamental challenge in creating artificial neural networks capable of continual learning. Although this phenomenon has been known for decades, it has mostly been studied in older, relatively small architectures and rarely in natural-language domains. To determine whether loss of plasticity remains a problem in the modern transformer-based LLM paradigm, we study plasticity loss in GPT-style Transformer models trained on a multilingual continual learning problem. Consistent with prior work, we find evidence of plasticity loss across models ranging from 5M to 314M non-embedding parameters, as measured by deterioration on a held-out Vietnamese probing task. We further find that the onset of plasticity loss follows a predictable scaling law, growing sublinearly with model size. These results suggest that larger models may delay the measurable effects of plasticity loss, but that increasing parameter count alone is likely to be insufficient to completely prevent it. We also find evidence of plasticity loss under stationary multilingual training, challenging the view that the phenomenon is exclusive to continual learning with abrupt task changes. Overall, our results suggest that even large Transformer language models trained on natural-language will eventually lose the ability to efficiently adapt to new data after sufficiently long training, in both continual and stationary settings.

### 🤖 AI 总结

**一句话总结**：The loss of plasticity - the ability of a network to learn new information after having already learned older information - is a fundamental challenge in creating artificial neural networks capable of...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Us, Can, Scale, Save, Plasticity, Loss, Large, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24752v1) | [下载PDF](https://arxiv.org/pdf/2606.24752v1.pdf)

---

## cs.CL

## [9. Less is More: Quality-Aware Training Data Selection for Scientific Summarization](https://arxiv.org/abs/2606.24828v1)

**作者**：Maria Nefeli Paraskevopoulou, Tatiana Passali, Grigorios Tsoumakas  
**分类**：cs.CL  
**发布时间**：2026-06-23

### 📄 论文摘要

Scientific long-document summarization datasets commonly treat author-written abstracts as gold reference summaries, although their quality and alignment with the source article vary. At the same time, publicly available scientific summarization datasets remain limited in scale and structure for modern long-context models. In this work, we address both challenges by a) constructing and releasing one of the largest biomedical and life science datasets for long-document summarization, containing 1.88 million PMC articles, and b) analyzing the reference quality of author-written abstracts with source-grounded and model-based metrics. We show that author-written abstracts vary in their alignment with the full article and that these quality signals can guide training-data selection. Training on selected high-quality subsets outperforms random sampling at matched training sizes and can match or exceed larger random subsets on factuality-oriented metrics. Our findings suggest that reference quality is an important factor in scientific summarization and that quality-aware data selection can improve training efficiency.

### 🤖 AI 总结

**一句话总结**：Scientific long-document summarization datasets commonly treat author-written abstracts as gold reference summaries, although their quality and alignment with the source article vary. At the same time...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Less, More, Quality-Aware, Training, Data, Selection, Scientific, Summarization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24828v1) | [下载PDF](https://arxiv.org/pdf/2606.24828v1.pdf)

---

## [10. Paying to Know: Micro-Transaction Markets for Verified Product Information in Agentic E-Commerce](https://arxiv.org/abs/2606.24783v1)

**作者**：Filippos Ventirozos, Matthew Shardlow  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-23

### 📄 论文摘要

Commercial NLP treats the shopping chatbot as a recommender or a conversion tool: its job is to match a user to a catalogue entry and close a sale. We argue that the arrival of agent-native micro-payment rails (e.g., x402, AP2) changes what is scarce. When the buyer is an autonomous agent that can investigate exhaustively, the bottleneck is no longer matching products but acquiring trustworthy, decision-relevant information about them. We envision agentic e-commerce as a micro-transaction market for verified information: buyer agents spend fractions of a cent to progressively unlock seller- and reviewer-supplied data -- service histories, third-party test reports, bills of materials, audited sales and support metrics -- paid for a la carte under a freemium model, with reviewer trust scored reputationally. We sketch the architecture of such a market and argue that it rewards genuine product quality and yields truer competition than ranking-based storefronts. We then translate the vision into concrete NLP problems -- cost-optimal information acquisition, data pricing and negotiation, real-time entity resolution, grounded value exchange, and privacy-preserving persona modelling -- and argue that these, not chat fluency, deserve the field's attention.

### 🤖 AI 总结

**一句话总结**：Commercial NLP treats the shopping chatbot as a recommender or a conversion tool: its job is to match a user to a catalogue entry and close a sale. We argue that the arrival of agent-native micro-paym...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Paying, Know, Micro-Transaction, Markets, Verified, Product, Information, Agentic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24783v1) | [下载PDF](https://arxiv.org/pdf/2606.24783v1.pdf)

---

## [11. Are We Ready For An Agent-Native Memory System?](https://arxiv.org/abs/2606.24775v1)

**作者**：Wei Zhou, Xuanhe Zhou, Shaokun Han 等 8 位作者  
**分类**：cs.CL, cs.DB, cs.IR  
**发布时间**：2026-06-23

### 📄 论文摘要

Memory for large language model (LLM) agents has rapidly evolved from simple retrieval-augmented mechanisms into a data management system that supports persistent information storage, retrieval, update, consolidation, and dynamic lifecycle governance throughout agent execution. Despite this evolution, existing evaluations still benchmark agent memory mainly through end-to-end task success metrics (e.g., F1, BLEU), while treating the underlying system as a monolithic black box. As a result, critical system-level concerns, including operational costs, architectural trade-offs across memory modules, and robustness under dynamic knowledge updates, remain insufficiently explored. In this paper, we present a systematic experimental study of agent memory from a data management perspective. We propose an analytical framework that decomposes agent memory into four core modules: memory representation and storage, extraction, retrieval and routing, and maintenance. Under this framework, we evaluate 12 representative memory systems and two reference baselines across five benchmark workloads spanning 11 datasets. Our extensive end-to-end evaluation shows that no single architecture dominates across all scenarios; instead, effectiveness depends heavily on how well the memory structure aligns with the workload bottleneck. Furthermore, through fine-grained ablation studies, we quantify their individual effects on representation fidelity, retrieval precision, update correctness, and long-horizon stability. Finally, we reveal cost-performance trade-offs under realistic workloads, showing localized maintenance is more cost-efficient than global reorganization. Based on these findings, we identify promising directions towards building truly agent-native memory systems. The code is publicly available at https://github.com/OpenDataBox/MemoryData.

### 🤖 AI 总结

**一句话总结**：Memory for large language model (LLM) agents has rapidly evolved from simple retrieval-augmented mechanisms into a data management system that supports persistent information storage, retrieval, updat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, An, Ready, Agent-Native, Memory, System?, large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24775v1) | [下载PDF](https://arxiv.org/pdf/2606.24775v1.pdf)

---

## cs.CV

## [12. DiffusionBench: On Holistic Evaluation of Diffusion Transformers](https://arxiv.org/abs/2606.24888v1)

**作者**：Xingjian Leng, Jaskirat Singh, Zhanhao Liang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-23

### 📄 论文摘要

Diffusion transformer (DiT) research on image generation has converged to a single evaluation setup: class-conditional generation on ImageNet. While methods improve the FID and related metrics, it is increasingly unclear whether they reflect real progress in generative modeling. The natural alternative, i.e., text-to-image (T2I) generation, is perceived as too costly or inconvenient to train and evaluate and is often skipped. We argue that this perception no longer holds. We introduce NanoGen, a unified DiT training and evaluation framework. NanoGen matches state-of-the-art DiT baselines on ImageNet and, with 12 lines of configuration change, also trains competitive text-to-image models. It currently supports RAE, VAE, pixel-space, and MeanFlow diffusion methods under both ImageNet and T2I setups. Under NanoGen, training T2I requires comparable compute to ImageNet. After training 21 latent diffusion models with NanoGen, we observe that method ranking shows no strong correlation between ImageNet and T2I generation: Pearson correlation is between -0.377 and -0.580 across three metrics. This suggests that a method which improves class-conditional ImageNet FID may show no corresponding improvement on T2I, clearly indicating the necessity of evaluating DiTs on both tasks. To this end, we summarize ImageNet and text-to-image results, which yields DiffusionBench, a holistic benchmark for DiT research. We recommend reporting DiffusionBench in place of ImageNet alone: methods that improve DiffusionBench are more likely to reflect broader progress.

### 🤖 AI 总结

**一句话总结**：Diffusion transformer (DiT) research on image generation has converged to a single evaluation setup: class-conditional generation on ImageNet. While methods improve the FID and related metrics, it is ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Diffusion, DiffusionBench, Holistic, Evaluation, Transformers, transformer, DiT

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24888v1) | [下载PDF](https://arxiv.org/pdf/2606.24888v1.pdf)

---

## [13. BenchX: Benchmarking AI Models for Cancer Detection and Localization with Demographic and Protocol Biases](https://arxiv.org/abs/2606.24883v1)

**作者**：Qi Chen, Wenxuan Li, Pedro R. A. S. Bassi 等 17 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-23

### 📄 论文摘要

Artificial intelligence (AI) has achieved remarkable success in medical imaging, but it is widely recognized that these models often perform inconsistently across real-world clinical settings. Such inconsistencies occur when patient demographics and imaging protocols vary, for example, in detecting small tumors, analyzing scans from different contrast phases, or evaluating patients of different ages or sexes. To quantify these inconsistencies, we develop a large-scale, open benchmark of 85,355 CT scans that systematically evaluates 12 tumor-detection AI models across tumor size, location, patient subgroup, and imaging protocol. We leverage large language models (LLMs) to extract and organize subgroup information from clinical data, which makes the analysis both scalable and reproducible. Our benchmark reveals that current state-of-the-art AI models, optimized for average accuracy, perform poorly in rare or underrepresented subgroups, such as young, female African Americans. However, collecting sufficient annotated data for these rare cases is often impractical. The benchmark provides a foundation for building more reliable and robust AI models for tumor detection and highlighting the need for rigorous, subgroup-level evaluation in medical imaging and computer vision. Datasets, code

### 🤖 AI 总结

**一句话总结**：Artificial intelligence (AI) has achieved remarkable success in medical imaging, but it is widely recognized that these models often perform inconsistently across real-world clinical settings. Such in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BenchX, Benchmarking, Models, Cancer, Detection, Localization, Demographic, Protocol

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24883v1) | [下载PDF](https://arxiv.org/pdf/2606.24883v1.pdf)

---

## [14. IV-CoT: Implicit Visual Chain-of-Thought for Structure-Aware Text-to-Image Generation](https://arxiv.org/abs/2606.24849v1)

**作者**：Zixuan Li, Haokun Lin, Yicheng Xiao 等 13 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-23

### 📄 论文摘要

Unified multi-modal large language models (MLLMs) have achieved strong text-to-image generation quality, but still struggle with structure-aware prompt following, where object counts, spatial relations, attribute bindings, and coarse layouts must be preserved. We attribute this limitation in part to the entanglement of structural planning and appearance rendering within a single conditioning stream. To address this issue, we propose Implicit Visual Chain-of-Thought (IV-CoT), a latent visual reasoning framework for query-conditioned image generation. IV-CoT decomposes the visual conditioning queries into a structural-to-semantic cascade, where structural queries first form a latent visual plan and semantic queries then render appearance conditioned on this plan. To guide the structural queries, we introduce training-only sketch supervision, which encourages them to capture structure from sketches without requiring sketch extraction or intermediate decoding at inference time. IV-CoT performs implicit CoT reasoning in a single forward pass and achieves superior results on GenEval and T2I-CompBench. Visualizations and analyses demonstrate that the learned structural and semantic queries play complementary roles in structure-aware generation.

### 🤖 AI 总结

**一句话总结**：Unified multi-modal large language models (MLLMs) have achieved strong text-to-image generation quality, but still struggle with structure-aware prompt following, where object counts, spatial relation...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IV-CoT, Implicit, Visual, Chain-of-Thought, Structure-Aware, Text-to-Image, Generation, Unified

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24849v1) | [下载PDF](https://arxiv.org/pdf/2606.24849v1.pdf)

---

## [15. Spherical-to-ERP Epipolar Rectification for Single-Axis Disparity in 360 Stereo](https://arxiv.org/abs/2606.24847v1)

**作者**：Sahereh Obeidavi, Dieter Landes  
**分类**：cs.CV  
**发布时间**：2026-06-23

### 📄 论文摘要

Omnidirectional stereo images provide full-surround perception but violate the geometric assumptions of classical disparity estimation: in spherical or fisheye views, epipolar correspondences follow curved great-circle paths, producing two-dimensional displacements that cannot be treated as single-axis disparity before geometric rectification. In this work, we adopt a standard spherical-to-equirectangular (ERP) projection as a preprocessing step, which straightens epipolar curves and restores a one-dimensional disparity structure - horizontal for left-right rigs and vertical for top-bottom rigs. Building on our previously introduced RAFT + Epipolar-Aligned Channel Selection (EACS) framework, originally developed for rectilinear and ERP stereo, we examine whether the same modular pipeline remains accurate when the input originates from spherical stereo imagery. After ERP projection, dense optical flow from RAFT is reduced to disparity by retaining only the baseline-aligned flow component. Experiments on synthetic fisheye stereo datasets show that this spherical-to-ERP-to-RAFT+EACS pipeline produces accurate, smooth, and structurally consistent disparity maps at real-time speed. These findings confirm that established ERP preprocessing can be effectively combined with our earlier RAFT+EACS method to enable practical, interpretable, and efficient disparity estimation from spherical stereo, providing a straightforward pathway for extending conventional stereo pipelines to 360 imaging.

### 🤖 AI 总结

**一句话总结**：Omnidirectional stereo images provide full-surround perception but violate the geometric assumptions of classical disparity estimation: in spherical or fisheye views, epipolar correspondences follow c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Spherical-to-ERP, Epipolar, Rectification, Single-Axis, Disparity, Stereo, Omnidirectional, images

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24847v1) | [下载PDF](https://arxiv.org/pdf/2606.24847v1.pdf)

---

## [16. Bridging the Manifold Gap: Riemannian Residual Line Search for One-Step Image Editing](https://arxiv.org/abs/2606.24844v1)

**作者**：Hongzhu Yi, Zhongtian Luo, Tong Li 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-23

### 📄 论文摘要

One-step diffusion editors are fast because they avoid inversion and iterative optimization, but a single transport update must be aggressive enough to realize the target prompt and conservative enough to preserve the source image--and no fixed update strength satisfies both demands across edit types. We treat this tension as a post-hoc candidate-selection problem on top of energy-field transport rather than as a new editing model. Our proposed method, Riemannian Residual Line Search, first builds a stronger edit by estimating the local time curvature of the prompt-delta field and projecting the corrected direction back onto the update norm of the original first-order energy-field transport estimation. It then forms a small residual path from the source image to this strong edit, retains the original first-order output as one candidate, and picks the final image by maximizing target-prompt CLIP alignment. On a 700-sample PIE-Bench++ evaluation across 10 edit type IDs, our method achieves state-of-the-art (SOTA) performance among current one-step update algorithms.

### 🤖 AI 总结

**一句话总结**：One-step diffusion editors are fast because they avoid inversion and iterative optimization, but a single transport update must be aggressive enough to realize the target prompt and conservative enoug...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bridging, Manifold, Gap, Riemannian, Residual, Line, Search, One-Step

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24844v1) | [下载PDF](https://arxiv.org/pdf/2606.24844v1.pdf)

---

## [17. GeoT2V-Bench: Benchmarking 3D Consistency in Text-to-Video Models via 3D Reconstruction](https://arxiv.org/abs/2606.24829v1)

**作者**：Chenrui Fan, Paolo Favaro  
**分类**：cs.CV  
**发布时间**：2026-06-23

### 📄 论文摘要

Camera-prompted text-to-video (T2V) models are increasingly used to synthesize virtual camera captures, such as orbiting objects or moving through static scenes. For these outputs, visual plausibility is insufficient: the generated frames should also provide coherent multi-view evidence for a single static 3D scene. We introduce GeoT2V-Bench, a reconstruction-based diagnostic benchmark for evaluating whether camera-prompted T2V clips can support explicit rigid 3D reconstruction. Our pipeline estimates per-frame camera intrinsics and poses with VGGT-style geometry estimation, fits DeformableGS, derives a static MedianGS proxy by temporal-median aggregation, and renders this proxy along the estimated camera path. Instead of producing a pass/fail label or a single scalar score, GeoT2V-Bench reports a continuous reconstruction profile covering apparent image motion, estimated trajectory behavior, MedianGS static rendering error, static-render flow agreement, and the gap between flexible and static fits. On a fair-format four-seed evaluation with 3,840 completed reconstructions from 12 open-weight model configurations and 80 GeCo-Eval static-scene prompts, we find that visible motion, static rendering error, flow agreement, and flexible-vs-static behavior often disagree. GeoT2V-Bench therefore captures complementary failure modes that emerge when generated videos are tested as global static-scene acquisitions.

### 🤖 AI 总结

**一句话总结**：Camera-prompted text-to-video (T2V) models are increasingly used to synthesize virtual camera captures, such as orbiting objects or moving through static scenes. For these outputs, visual plausibility...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, GeoT2V-Bench, Benchmarking, Consistency, Text-to-Video, Models, via, Reconstruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24829v1) | [下载PDF](https://arxiv.org/pdf/2606.24829v1.pdf)

---

## [18. High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology](https://arxiv.org/abs/2606.24817v1)

**作者**：Johannes Boehm, Bappaditya Dey  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-06-23

### 📄 论文摘要

Advanced semiconductor nodes drastically increased demand for Transmission Electron Microscopy (TEM), yet destructive sample preparation, slow imaging and high costs severely limit the availability of diverse datasets needed for downstream machine learning (ML). Synthetic data generation is becoming essential, but current generative models often miss TEM-specific noise, structural detail, and stochastic variability crucial for evaluation. We present a Denoising Diffusion Probabilistic Model (DDPM) framework for synthetic TEM image generation under extreme data scarcity. A progressive patch-based training strategy scales from low-resolution patches to full images, enabling from-scratch training with only 15 samples. We integrate a custom TrivialAugment adaptation, cross-process domain transfer, classifier guidance, and RePaint-style inpainting, culminating in full-image generation that preserves global structural and spatial relationships in compliance with FAB metrology requirements. Beyond synthesis, we repurpose DDPM feature representations for segmentation, partitioning encoder feature maps to obtain coherent region masks. Our synthetic images achieve up to MS-SSIM > 0.98 and qualitative expert assessment consistent with structural similarity results, facilitating downstream ML training for defect detection, segmentation, and metrology while preserving statistical and physical realism.

### 🤖 AI 总结

**一句话总结**：Advanced semiconductor nodes drastically increased demand for Transmission Electron Microscopy (TEM), yet destructive sample preparation, slow imaging and high costs severely limit the availability of...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, High-Fidelity, Synthetic, Transmission, Electron, Microscopy, Image, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24817v1) | [下载PDF](https://arxiv.org/pdf/2606.24817v1.pdf)

---

## [19. DDStereo: Efficient Dual Decoder Transformers for Stereo 3D Road Anomaly Detection](https://arxiv.org/abs/2606.24805v1)

**作者**：Shiyi Mu, Zichong Gu, Zhiqi Ai 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-23

### 📄 论文摘要

Stereo-based 3D object detection still faces two critical safety challenges: real-time performance and open-set generalization. Existing stereo 3D methods typically achieve twice the accuracy of monocular methods but suffer from significantly lower inference speeds, making them unsuitable for real-time applications. Meanwhile, recent advances in open-world detection have introduced open-set and open-vocabulary algorithms in monocular 2D and 3D settings, yet stereo-based open-set detection remains largely unexplored. To bridge this gap, we propose DDStereo, a novel Dual-Decoder Stereo Transformer for real-time open-set 3D object detection. DDStereo features two lightweight decoder branches: one for open-set foreground 2D detection and the other for 3D attribute regression. These decoders share object-level queries to achieve unified target-level alignment. To enhance inference efficiency, we designed a compact disparity feature extractor and a streamlined decoder architecture. Experiments on public stereo 3D benchmarks demonstrate that DDStereo achieves state-of-the-art accuracy under both closed-set and open-set protocols. Notably, our method surpasses existing stereo 3D detectors in inference speed and, for the first time, achieves real-time performance comparable to monocular approaches.

### 🤖 AI 总结

**一句话总结**：Stereo-based 3D object detection still faces two critical safety challenges: real-time performance and open-set generalization. Existing stereo 3D methods typically achieve twice the accuracy of monoc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, DDStereo, Efficient, Dual, Decoder, Transformers, Stereo, Road

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24805v1) | [下载PDF](https://arxiv.org/pdf/2606.24805v1.pdf)

---

## [20. OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis](https://arxiv.org/abs/2606.24799v1)

**作者**：Chenrui Fan, Paolo Favaro  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-23

### 📄 论文摘要

Generic text-to-video models can be used as rich open-world scene priors. Despite the high quality of today's generated videos, they do not directly yield reliable 3D assets: camera motion is difficult to control, view coverage is partial, and frames often contain inconsistencies across time. We introduce OrbitForge, an adapter built from frozen video priors and per-prompt Gaussian Splatting reconstruction optimization that converts a single text-generated video into a canonical closed-orbit 3D Gaussian Splatting scene. We use 3D reconstruction as an anchor to improve the 3D consistency of the generated video. We obtain a preliminary 3D reconstruction from a first generated video via Deformable Gaussian Splatting with a robust MedianGS proxy. We render views from a prescribed orbit to detect missing viewpoints. OrbitForge uses the text-to-video model to complete only the missing views, and reconstructs the completed orbit into a final Gaussian Splatting scene. This design requires no task-specific video or multiview fine-tuning, avoids per-prompt score-distillation optimization, and does not progressively generate views one step at a time. We further argue that this setting demands coverage-aware evaluation: local smoothness alone rewards methods that never attempt a full orbit. On a frozen 300-prompt T3Bench-derived audit, OrbitForge reconstruction attains a 359.0-degree measured median span, raises originally unsupported-bin Q10 ImageReward from 8.07 to 16.36 relative to MedianGS-only reconstruction, while remaining competitive with VideoMV on the coverage-quality.

### 🤖 AI 总结

**一句话总结**：Generic text-to-video models can be used as rich open-world scene priors. Despite the high quality of today's generated videos, they do not directly yield reliable 3D assets: camera motion is difficul...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OrbitForge, Text-to-3D, Scene, Generation, via, Reconstruction-Anchored, Video, Synthesis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24799v1) | [下载PDF](https://arxiv.org/pdf/2606.24799v1.pdf)

---

## [21. EG-VQA: Benchmarking Verifiable Video Question Answering with Grounded Temporal Evidence](https://arxiv.org/abs/2606.24797v1)

**作者**：Linpeng Huang, Weixing Chen, Zexin Chen 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-23

### 📄 论文摘要

Recent advances in Video Large Language Models (Video-LLMs) have yielded promising performance on video question answering (VideoQA). Nevertheless, existing benchmarks are predominantly evaluated through answer correctness, while the grounding of predictions in relevant video evidence remains largely unexamined. This disconnect between answer generation and evidence understanding motivates the construction of the Evidence-Grounded Video Question Answering Benchmark (EG-VQA), an open-ended evaluation protocol in which each QA pair is explicitly annotated with supporting temporal evidence, thereby requiring joint reasoning and precise evidence localization. EG-VQA is comprised of 2,067 videos and 11,838 QA pairs with fine-grained evidence annotations. To evaluate predicted evidence, Evidence-Grounded F1 (EG-F1) is introduced as a unified metric in which temporal alignment and semantic consistency against ground-truth evidence are jointly measured. Experimental evaluation reveals that even strong proprietary models struggle to accurately ground their predictions, exposing a fundamental discrepancy between answer correctness and faithful evidence localization. To bridge this gap, EG-Reasoner, an evidence-grounded reasoning model trained with explicit supervision, is proposed. State-of-the-art performance is achieved among open-source models, with results competitive against proprietary systems, particularly pronounced gains are observed on reasoning-intensive tasks such as counterfactual questions. These findings demonstrate that scaling alone is insufficient for robust video understanding and that structured evidence supervision is essential for the development of more reliable and interpretable VideoQA systems.

### 🤖 AI 总结

**一句话总结**：Recent advances in Video Large Language Models (Video-LLMs) have yielded promising performance on video question answering (VideoQA). Nevertheless, existing benchmarks are predominantly evaluated thro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EG-VQA, Benchmarking, Verifiable, Video, Question, Answering, Grounded, Temporal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24797v1) | [下载PDF](https://arxiv.org/pdf/2606.24797v1.pdf)

---

## [22. Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)

**作者**：Leshu Li, Jie Peng, Yang Zhao  
**分类**：cs.CV  
**发布时间**：2026-06-23

### 📄 论文摘要

3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views. For SLAM in large-scale scenes, such as autonomous driving, 3DGS-SLAM faces a critical limitation: memory consumption increases continuously over time as Gaussian points accumulate, leading to poor memory efficiency and limiting its applicability. In this work, we propose a rendering-area-aware pruning strategy that selectively removes Gaussians based on their contribution to the effective rendering area, rather than solely relying on Gaussian-level heuristics such as opacity or gradient magnitude. This perspective directly targets the sources of memory redundancy, effectively reducing the peak memory footprint of 3DGS-SLAM during runtime. Evaluations on the EuRoC and KITTI datasets demonstrate that our method consistently outperforms existing pruning approaches in large-scale outdoor scenes, achieving over 60% memory reduction and more than 2 times FPS improvement while preserving localization and mapping accuracy. These results highlight rendering-area-aware pruning as a promising direction for scaling 3DGS-SLAM to real-world autonomous driving scenarios. Our code is publicly available at https://github.com/UMN-ZhaoLab/Pocket-SLAM.git.

### 🤖 AI 总结

**一句话总结**：3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel v...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Pocket-SLAM, Rendering-Area-Aware, Pruning, Memory-Efficient, 3DGS-SLAM, Gaussian, Splatting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24796v1) | [下载PDF](https://arxiv.org/pdf/2606.24796v1.pdf)

---

## [23. Counting Trees from Satellite Imagery with Noisy Supervision](https://arxiv.org/abs/2606.24786v1)

**作者**：Dimitri Gominski, Maurice Mugabowindekwe, Qiue Xu 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-23

### 📄 论文摘要

Counting individual trees is a fundamental task for environmental monitoring, yet remains largely unexplored with satellite imagery. At these resolutions, isolated trees may still be identifiable, but crown boundaries become ambiguous in dense forests, making the notion of an individual tree inherently ill-defined. Moreover, large-scale manual annotations of individual trees are prohibitively expensive. While scalable supervision can be derived from airborne LiDAR, the resulting annotations are noisy and difficult to exploit effectively.   We address these challenges by formulating tree counting as a spatial density matching problem supervised through Unbalanced Optimal Transport. This formulation naturally accommodates both precise localization of isolate trees and robust density estimation in dense forests. We further introduce a self-correction mechanism that leverages transport residuals to progressively refine noisy supervision during training.   We evaluate our approach on TinyTrees, a new benchmark spanning three continents and three satellite sensors, comprising over 215 million tree annotations (including 773K manually verified instances) across 23,000 sq.km. Our method consistently outperforms detection-based, regression-based, and transport-based distribution-matching baselines, demonstrating the effectiveness of unbalanced transport and reliability-aware supervision for large-scale tree counting from satellite imagery. Code, data and models are available at https://github.com/dgominski/treematch.

### 🤖 AI 总结

**一句话总结**：Counting individual trees is a fundamental task for environmental monitoring, yet remains largely unexplored with satellite imagery. At these resolutions, isolated trees may still be identifiable, but...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Counting, Trees, Satellite, Imagery, Noisy, Supervision, individual, fundamental

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24786v1) | [下载PDF](https://arxiv.org/pdf/2606.24786v1.pdf)

---

## [24. AerialFusionMapNet: Online HD Map Construction with Aerial-Onboard BEV Fusion](https://arxiv.org/abs/2606.24784v1)

**作者**：Daniel Lengerer, Mathias Pechinger, Klaus Bogenberger 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-23

### 📄 论文摘要

High-resolution aerial imagery has recently emerged as a complementary modality for automated driving perception and has shown potential to improve birds-eye-view (BEV) scene understanding when fused with onboard sensors. Prior work demonstrated performance gains for online high-definition (HD) map construction through aerial-onboard fusion; however, conventional end-to-end fusion does not fully exploit the structural information contained in aerial representations. In this work, we introduce AerialFusionMapNet, a fusion-based mapping framework with a structured two-stage training strategy that explicitly enhances the contribution of aerial features within a unified pipeline. The proposed training scheme enables more effective integration of structural aerial priors. On the nuScenes geographic split, AerialFusionMapNet achieves up to 54.7 mAP, improving over prior aerial-onboard fusion baselines from 48.8 mAP by +5.9 absolute and +12.1% relative. The results suggest that structured training design, rather than increased architectural complexity, plays a more decisive role in unlocking the full potential of aerial imagery for online HD map construction. Code and trained models are available at https://github.com/DriverlessMobility/AerialFusionMapNet.

### 🤖 AI 总结

**一句话总结**：High-resolution aerial imagery has recently emerged as a complementary modality for automated driving perception and has shown potential to improve birds-eye-view (BEV) scene understanding when fused ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HD, AerialFusionMapNet, Online, Map, Construction, Aerial-Onboard, BEV, Fusion

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24784v1) | [下载PDF](https://arxiv.org/pdf/2606.24784v1.pdf)

---

## [25. Revealing Training Data Exposure in Vision Language Large Models via Parameter Gradients](https://arxiv.org/abs/2606.24774v1)

**作者**：Zhihao Zhu, Hongyi Tang, Yi Yang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-23

### 📄 论文摘要

Vision-Language Large Models (VLLMs) trained on massive crawled corpora raise pressing copyright and data-provenance concerns. These concerns are particularly acute in healthcare, where patient medical images paired with clinical reports demand rigorous privacy safeguards. However, existing training data detection methods either fail in cross-modal scenarios or rely on superficial output signals with insufficient discriminative power. We introduce GradAudit, a gradient-based auditing framework that examines internal optimization dynamics rather than treating VLLMs as black boxes. Our approach builds on a key observation: model parameters converge to regions where gradients on training samples become stable and well-aligned, whereas gradients on non-training samples remain noisy and inconsistent. By analyzing these gradient signatures, GradAudit achieves strong separability and detects genuine image-text associations learned during training, not merely individual modality membership. Empirically, across both medical and general-domain datasets, GradAudit substantially outperforms state-of-the-art baselines in both pretraining and fine-tuning VLLMs. In a case study employing copyrighted content, we show that existing training data detection methods not only underestimate the extent of unauthorized data usage, but that this underestimation becomes more pronounced as models become more recent and more advanced.

### 🤖 AI 总结

**一句话总结**：Vision-Language Large Models (VLLMs) trained on massive crawled corpora raise pressing copyright and data-provenance concerns. These concerns are particularly acute in healthcare, where patient medica...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Revealing, Training, Data, Exposure, Vision, Language, Large, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24774v1) | [下载PDF](https://arxiv.org/pdf/2606.24774v1.pdf)

---

## [26. Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization](https://arxiv.org/abs/2606.24767v1)

**作者**：Zhaopeng Cui, Jiarui Hu, Jingbo Liu 等 10 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-06-23

### 📄 论文摘要

Indoor visual relocalization plays a critical role in emerging spatial and embodied AI applications. However, prior research was predominantly devoted to low-level vision schemes, struggling to perceive scene semantics and compositions, which limits both interpretability and applicability. In this paper, we explore the issue of how to organize rich object information in a scene, including semantics, layout, and geometry, into a structured map representation, thereby utilizing object units exclusively to drive the camera relocalization task. To this end, we propose OpenReLoc, a camera relocalization system designed to provide scene understanding and accurate pose estimation capabilities. Leveraging recent foundation models, we first introduce a multi-modal mechanism to integrate open-vocabulary semantic knowledge for effective 2D-3D object matching. Additionally, we design object-oriented reference frames as position priors, paired with a reference frame selection strategy based on the Distance-IoU (DIOU), enabling extension to scalable scenes. Moreover, to ensure stable and accurate pose optimization, we also propose a dual-path 2D Iterative Closest Pixel loss guided by object shape. Experimental results demonstrate that OpenReLoc achieves superior relocalization recall and accuracy across various datasets. Our source code will be released upon acceptance.

### 🤖 AI 总结

**一句话总结**：Indoor visual relocalization plays a critical role in emerging spatial and embodied AI applications. However, prior research was predominantly devoted to low-level vision schemes, struggling to percei...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Compact, Object-Level, Representations, Open-Vocabulary, Understanding, Indoor, Visual, Relocalization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24767v1) | [下载PDF](https://arxiv.org/pdf/2606.24767v1.pdf)

---

## [27. UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving](https://arxiv.org/abs/2606.24759v1)

**作者**：Xiaowei Gao, Pengxiang Li, Yitai Cheng 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-23

### 📄 论文摘要

Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and spatial precision. Models that rely on single-frame or low-resolution inputs often miss small, distant, or partially occluded hazards, while language-centric driving models frequently provide limited grounded evidence for their explanations. To address this gap, we propose UniDrive, a unified visual-language and grounding framework for interpretable risk understanding in autonomous driving. UniDrive combines a temporal reasoning branch that models scene dynamics from multi-frame visual input with a high-resolution perception branch that preserves fine-grained spatial details from the latest frame. The two branches are integrated through a gated cross-attention fusion module, enabling dynamic context to be aligned with precise spatial evidence. Based on the fused representation, UniDrive jointly generates natural-language risk descriptions and grounded bounding-box outputs for risk objects. Experiments on the DRAMA-Reasoning benchmark show that UniDrive outperforms representative image-based and video-based baselines in both captioning and risk-object grounding. In particular, UniDrive achieves the best overall performance on the validation split and demonstrates clear advantages in small-object localization, zero-shot generalization to NuScenes and BDD100K, and human-rated interpretability and trustworthiness. These results suggest that explicitly combining temporal semantics and high-resolution perception provides a stronger foundation for interpretable and safety-oriented autonomous driving systems. The code is available at https://github.com/pixeli99/unidrive-dev.

### 🤖 AI 总结

**一句话总结**：Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoni...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UniDrive, Unified, Vision-Language, Grounding, Framework, Interpretable, Risk, Understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24759v1) | [下载PDF](https://arxiv.org/pdf/2606.24759v1.pdf)

---

## [28. Adaptive Hebbian Memory Routing in Vision Transformers for Few-Shot Learning](https://arxiv.org/abs/2606.24756v1)

**作者**：Mohammed Yusuf Mujawar, Noorbakhsh Amiri Golilarz  
**分类**：cs.CV  
**发布时间**：2026-06-23

### 📄 论文摘要

Few-shot image recognition requires models to adapt to new classes from a small labeled support set. Hebbian fast-weight memory can provide temporary associative information during an episode, but fixed memory behavior may not be appropriate for every few-shot task. In this work, we propose Adaptive Hebbian Routing for few-shot Vision Transformers. The method uses a lightweight MLP router to control the contribution of Hebbian memory, the strength of memory updates, and the retention of previous memory from support-set features. We study Adaptive Placement, Adaptive Plasticity, and Fully Adaptive Hebbian Routing. Experiments use ViT-Small, DeiT-Small, and Swin-Tiny under 5-way 1-shot evaluation on Omniglot, CIFAR-FS, and cross-domain transfer from CIFAR-FS to Omniglot. In the direct Swin comparison, fixed and adaptive Hebbian variants use the same memory location. Adaptive Plasticity improves the fixed Hebbian result from 96.74\% to 96.92\%, while Fully Adaptive Routing achieves the best result at 96.94\%. The fully adaptive Swin model also reduces inference time from 16.51 ms to 14.05 ms relative to fixed Hebbian Swin. On CIFAR-FS, adaptive variants improve performance across all three backbones, and the multi-shot evaluation shows that these gains remain useful as the number of support examples increases. These results show that adaptive plasticity and adaptive memory activation can improve few-shot Transformer representations beyond fixed Hebbian behavior.

### 🤖 AI 总结

**一句话总结**：Few-shot image recognition requires models to adapt to new classes from a small labeled support set. Hebbian fast-weight memory can provide temporary associative information during an episode, but fix...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Adaptive, Hebbian, Memory, Routing, Vision, Transformers, Few-Shot, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24756v1) | [下载PDF](https://arxiv.org/pdf/2606.24756v1.pdf)

---

## cs.LG

## [29. Real vs. Complex Spectral Bases for Neural Operators: The Role of Green's Function Alignment](https://arxiv.org/abs/2606.24851v1)

**作者**：Jason Sulskis, Sathya Ravi  
**分类**：cs.LG  
**发布时间**：2026-06-23

### 📄 论文摘要

Fourier Neural Operators (FNO) learn solution operators of partial differential equations by parameterizing global convolutions in the complex Fourier domain. For real-valued PDE solutions, the complex FFT carries representational redundancy through conjugate symmetry. We introduce the Hartley Neural Operator (HNO), the exact real-valued mirror of FNO: it replaces the FFT with the purely real Discrete Hartley Transform and learns a single real multiplier per retained spectral mode, with no complex arithmetic. Because the real Hartley spectrum is not halved by conjugate symmetry, HNO retains twice as many frequency corners as FNO but one real weight where FNO carries a complex pair, so the two operators are iso-parametric at equal width and differ only in spectral basis. Our central thesis is that the best basis is a property of the operator. Self-adjoint elliptic operators (Poisson, biharmonic) have real, symmetric Green's functions that the real Hartley multiplier diagonalizes exactly, and HNO is favored there. Time-dependent operators carry phase, from oscillation in the wave equation to transport in advection, Burgers, and Navier-Stokes, which a real diagonal multiplier cannot represent, so FNO is favored there, and increasingly so with the operator's phase content, leaving the phaseless heat equation as the borderline case. Training both operators identically and benchmarking across PDE classes, initial-condition families, and boundary conditions, we find an elliptic-versus-time-dependent split that is monotone in operator phase content and matches the Green's-function theory we develop. Rather than a universal winner, our findings give a predictive rule: match the spectral basis to the symmetry of the solution operator.

### 🤖 AI 总结

**一句话总结**：Fourier Neural Operators (FNO) learn solution operators of partial differential equations by parameterizing global convolutions in the complex Fourier domain. For real-valued PDE solutions, the comple...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：vs, Real, Complex, Spectral, Bases, Neural, Operators, Role

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24851v1) | [下载PDF](https://arxiv.org/pdf/2606.24851v1.pdf)

---

## [30. Grad Detect: Gradient-Based Hallucination Detection in LLMs](https://arxiv.org/abs/2606.24790v1)

**作者**：Anand Kamat, Daniel Blake, Brent M. Werness  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-23

### 📄 论文摘要

Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks, yet they remain prone to generating hallucinations. Detecting these hallucinations is critical for deploying LLMs reliably in high-stakes applications. We present Grad Detect, a gradient-based approach for predicting hallucinations by analyzing layer-wise gradient patterns from a single forward-backward pass during inference. Our method shows that the internal gradient structure of a model carries rich information about the correctness of its output. This information is not accessible through output-level signals alone. We evaluate Grad Detect on several Q&A benchmarks across both hallucination detection and model abstention prediction, where it consistently outperforms confidence-based and sampling-based baselines. Through comprehensive layer ablation studies across all eleven models from four architectural families, we find that the final five layers concentrate over 97% of the discriminative gradient signal, enabling efficient deployment with minimal performance loss. Grad Detect provides a unified framework for predicting multiple dimensions of LLM reliability, offering strong predictive performance alongside interpretable insights into where and how model failures originate.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks, yet they remain prone to generating hallucinations. Detecting these hallucinations is critical for deployin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Grad, Detect, Gradient-Based, Hallucination, Detection, Large, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.24790v1) | [下载PDF](https://arxiv.org/pdf/2606.24790v1.pdf)

---

