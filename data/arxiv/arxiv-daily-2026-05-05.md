# arXiv AI 论文日报 | 2026-05-05

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (13 篇)
- [cs.LG](#csLG) (6 篇)
- [cs.AI](#csAI) (10 篇)
- [cs.CL](#csCL) (1 篇)

---

## cs.AI

## [1. Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection](https://arxiv.org/abs/2605.02860v1)

**作者**：Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata  
**分类**：cs.AI, cs.LG, cs.SE  
**发布时间**：2026-05-04

### 📄 论文摘要

Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels.   To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate.   Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.

### 🤖 AI 总结

**一句话总结**：Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Standing, Shoulders, Giants, Stabilized, Knowledge, Distillation, Cross--Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02860v1) | [下载PDF](https://arxiv.org/pdf/2605.02860v1.pdf)

---

## [2. HAAS: A Policy-Aware Framework for Adaptive Task Allocation Between Humans and Artificial Intelligence Systems](https://arxiv.org/abs/2605.02832v1)

**作者**：Vicente Pelechanoa, Antoni Mestre, Manoli Albert 等 4 位作者  
**分类**：cs.AI, cs.HC, cs.SE  
**发布时间**：2026-05-04

### 📄 论文摘要

Deciding how to distribute work between humans and AI systems is a central challenge in organisational design. Most approaches treat this as a binary choice, yet the operational reality is richer: humans and AI routinely share tasks or take complementary roles depending on context, fatigue, and the stakes involved. Governing that distribution -- balancing efficiency, oversight, and human capability -- remains an open problem. This paper presents Human-AI Adaptive Symbiosis (HAAS), an implemented framework for adaptive task allocation in software engineering and manufacturing. HAAS combines two coupled components: a rule-based expert system that enforces governance constraints before any learning occurs, and a contextual-bandit learner that selects among feasible collaboration modes from outcome feedback. Task-agent fit is represented through five auditable cognitive dimensions and a five-mode autonomy spectrum -- from human-only to fully autonomous -- embedded in a reproducible benchmark spanning both domains. Three empirical findings emerge. First, governance is not a binary switch but a tunable design variable: tighter constraints predictably convert autonomous AI assignments into supervised collaborations, with domain-specific costs and benefits. Second, in manufacturing, stronger governance can improve operational performance and reduce fatigue simultaneously -- a workload-buffering effect that contradicts the usual framing of governance as pure overhead. Third, no single governance setting dominates across all contexts; moderate governance becomes increasingly competitive as the learner accumulates experience within the governed action space. Together, these findings position HAAS as a pre-deployment workbench for comparing and inspecting human--AI allocation policies before organisational commitment.

### 🤖 AI 总结

**一句话总结**：Deciding how to distribute work between humans and AI systems is a central challenge in organisational design. Most approaches treat this as a binary choice, yet the operational reality is richer: hum...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HAAS, Policy-Aware, Framework, Adaptive, Task, Allocation, Between, Humans

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02832v1) | [下载PDF](https://arxiv.org/pdf/2605.02832v1.pdf)

---

## [3. Compress Then Adapt? No, Do It Together via Task-aware Union of Subspaces](https://arxiv.org/abs/2605.02829v1)

**作者**：Jingze Ge, Yun Liu, Xue Geng 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-04

### 📄 论文摘要

Adapting large pretrained models to diverse tasks is now routine, yet the two dominant strategies of parameter-efficient fine-tuning (PEFT) and low-rank compression are typically composed in sequence. This decoupled practice first compresses and then fine-tunes adapters, potentially misaligning the compressed subspace with downstream objectives and squandering a global parameter budget. To overcome this limitation, we introduce JACTUS (Joint Adaptation and Compression with a Task-aware Union of Subspaces), a single framework that unifies compression and adaptation. From a small calibration set, JACTUS estimates input and pre-activation gradient covariances, forms their orthogonal union with the pretrained weight subspace, performs a projected low-rank approximation inside this union, allocates rank globally by marginal gain per parameter, and trains only a compact core matrix. This explicitly mitigates the potential misalignment between the compressed subspace and downstream objectives by coupling the directions preserved for compression with those required for adaptation, yielding a deployable low-rank model that avoids retaining full frozen weights while enabling fast and robust tuning. On vision, JACTUS attains an average 89.2% accuracy on ViT-Base across eight datasets at 80% retained parameters, surpassing strong 100% PEFT baselines (e.g., DoRA 87.9%). On language, JACTUS achieves an 80.9% average on Llama2-7B commonsense QA at the same 80% retained-parameter budget, outperforming 100% PEFT (e.g., DoRA 79.7%) and exceeding prior compress-then-finetune pipelines under the same ratained-parameter budget. We will release code.

### 🤖 AI 总结

**一句话总结**：Adapting large pretrained models to diverse tasks is now routine, yet the two dominant strategies of parameter-efficient fine-tuning (PEFT) and low-rank compression are typically composed in sequence....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：No, Do, It, Compress, Then, Adapt?, Together, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02829v1) | [下载PDF](https://arxiv.org/pdf/2605.02829v1.pdf)

---

## [4. First-Order Efficiency for Probabilistic Value Estimation via A Statistical Viewpoint](https://arxiv.org/abs/2605.02827v1)

**作者**：Ziqi Liu, Kiljae Lee, Yuan Zhang 等 4 位作者  
**分类**：cs.AI, stat.ME, stat.ML  
**发布时间**：2026-05-04

### 📄 论文摘要

Probabilistic values, including Shapley values and semivalues, provide a model-agnostic framework to attribute the behavior of a black-box model to data points or features, with a wide range of applications including explainable artificial intelligence and data valuation. However, their exact computation requires utility evaluations over exponentially many coalitions, making Monte Carlo approximation essential in modern machine learning applications. Existing estimators are often developed through different identification strategies, including weighted averages, self-normalized weighting, regression adjustment, and weighted least squares. Our key observation is that these seemingly distinct constructions share a common first-order error structure, in which the leading term is an augmented inverse-probability weighted influence term determined by the sampling law and a working surrogate function. This first-order representation yields an explicit expression for the leading mean squared error (MSE), which characterizes how the sampling law and the surrogate jointly determine statistical efficiency. Guided by this criterion, we propose an Efficiency-Aware Surrogate-adjusted Estimator (EASE) that directly chooses the sampling law and surrogate to minimize the first-order MSE. We demonstrate that EASE consistently outperforms state-of-the-art estimators for various probabilistic values.

### 🤖 AI 总结

**一句话总结**：Probabilistic values, including Shapley values and semivalues, provide a model-agnostic framework to attribute the behavior of a black-box model to data points or features, with a wide range of applic...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：First-Order, Efficiency, Probabilistic, Value, Estimation, via, Statistical, Viewpoint

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02827v1) | [下载PDF](https://arxiv.org/pdf/2605.02827v1.pdf)

---

## [5. SCPRM: A Schema-aware Cumulative Process Reward Model for Knowledge Graph Question Answering](https://arxiv.org/abs/2605.02819v1)

**作者**：Jiujiu Chen, Yazheng Liu, Sihong Xie 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-04

### 📄 论文摘要

Large language models excel at complex reasoning, yet evaluating their intermediate steps remains challenging. Although process reward models provide step-wise supervision, they often suffer from a risk compensation effect, where incorrect steps are offset by later correct ones, assigning high rewards to flawed reasoning paths. This issue is further exacerbated in knowledge graph (KG) reasoning, as there may exist multiple paths between the start and end entities in the KGs, and a risky step can make the reasoning path flawed. Those limitations are problematic in risk-sensitive tasks such as medical and legal KG reasoning. To address the issues, we propose a Schema-aware Cumulative Process Reward Model (SCPRM) that evaluates reasoning paths by conditioning on the reasoning prefix , and incorporating schema distance between current reasoning step and the implicit target parsed from the query, which provides cumulative and future rewards to guide the path explorations. We further integrate SCPRM into Monte Carlo Tree Search (MCTS) as SCPRM-MCTS to conduct multi-hop reasoning on KGs for question answering (QA) tasks. Across medical and legal KGQA and CWQ, SCPRM-MCTS improves the performance of Hits@k by an average of 1.18% over strong baselines, demonstrating more accurate and risk-sensitive reasoning evaluation.

### 🤖 AI 总结

**一句话总结**：Large language models excel at complex reasoning, yet evaluating their intermediate steps remains challenging. Although process reward models provide step-wise supervision, they often suffer from a ri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SCPRM, Schema-aware, Cumulative, Process, Reward, Model, Knowledge, Graph

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02819v1) | [下载PDF](https://arxiv.org/pdf/2605.02819v1.pdf)

---

## [6. AIs and Humans with Agency](https://arxiv.org/abs/2605.02810v1)

**作者**：David Mumford  
**分类**：cs.AI  
**发布时间**：2026-05-04

### 📄 论文摘要

This paper compares agency in humans with potential agency in AI programs. Human agency takes many years to develop, as the frontal lobe is activated. Early attempts to endow LLMs agency have met serious obstacles. Progress requires a new architecture where actions and plans are formulated jointly with the human actors in each real world setting.

### 🤖 AI 总结

**一句话总结**：This paper compares agency in humans with potential agency in AI programs. Human agency takes many years to develop, as the frontal lobe is activated. Early attempts to endow LLMs agency have met seri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AIs, Humans, Agency, paper, compares, potential, programs, Human

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02810v1) | [下载PDF](https://arxiv.org/pdf/2605.02810v1.pdf)

---

## [7. When Audio-Language Models Fail to Leverage Multimodal Context for Dysarthric Speech Recognition](https://arxiv.org/abs/2605.02782v1)

**作者**：Pehuén Moure, Niclas Pokel, Bilal Bounajma 等 7 位作者  
**分类**：cs.AI, cs.CL, eess.AS  
**发布时间**：2026-05-04

### 📄 论文摘要

Automatic speech recognition (ASR) systems remain brittle on dysarthric and other atypical speech. Recent audio-language models raise the possibility of improving performance by conditioning on additional clinical context at inference time, but it is unclear whether these models can make use of such information. We introduce a benchmark built on the Speech Accessibility Project (SAP) dataset that tests whether diagnosis labels, clinician-derived speech ratings, and progressively richer clinical descriptions improve transcription accuracy for dysarthric speech. Across matched comparisons on nine models, we find that current models do not meaningfully use this context: diagnosis-informed and clinically detailed prompts yield negligible improvements and often degrade word error rate. We complement the prompting analysis with context-dependent fine-tuning, showing that LoRA adaptation with a mixture of clinical prompt formats achieves a WER of 0.066, a 52% relative reduction over the frozen baseline, while preserving performance when context is unavailable. Subgroup analyses reveal significant gains for Down syndrome and mild-severity speakers. These results clarify where current models fall short and provide a testbed for measuring progress toward more inclusive ASR.

### 🤖 AI 总结

**一句话总结**：Automatic speech recognition (ASR) systems remain brittle on dysarthric and other atypical speech. Recent audio-language models raise the possibility of improving performance by conditioning on additi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Audio-Language, Models, Fail, Leverage, Multimodal, Context, Dysarthric

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02782v1) | [下载PDF](https://arxiv.org/pdf/2605.02782v1.pdf)

---

## [8. Fine-Grained Graph Generation through Latent Mixture Scheduling](https://arxiv.org/abs/2605.02780v1)

**作者**：Nidhi Vakil, Hadi Amiri  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-05-04

### 📄 论文摘要

Structure aware graph generation aims to generate graphs that satisfy given topological properties. It has applications in domains such as drug discovery, social network modeling, and knowledge graph construction. Unlike existing methods that only provide coarse control over graph properties, we introduce a novel conditional variational autoencoder for fine-grained structural control in graph generation. The approach refines the decoder's latent space by dynamically aligning graph- and property-driven representations to improve both graph fidelity and control satisfaction. Specifically, the approach implements a mixture scheduler that progressively integrates graph and control priors. Experiments on five real-world datasets show the efficacy of the proposed model compared to recent baselines, achieving high generation quality while maintaining high controllability.

### 🤖 AI 总结

**一句话总结**：Structure aware graph generation aims to generate graphs that satisfy given topological properties. It has applications in domains such as drug discovery, social network modeling, and knowledge graph ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Fine-Grained, Graph, Generation, through, Latent, Mixture, Scheduling, Structure

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02780v1) | [下载PDF](https://arxiv.org/pdf/2605.02780v1.pdf)

---

## [9. U-Define: Designing User Workflows for Hard and Soft Constraints in LLM-Based Planning](https://arxiv.org/abs/2605.02765v1)

**作者**：Christine P Lee, Xinyu Jessica Wang, Aws Albarghouthi 等 5 位作者  
**分类**：cs.AI, cs.HC, cs.LG  
**发布时间**：2026-05-04

### 📄 论文摘要

LLMs are increasingly used for end-user task planning, yet their black-box nature limits users' ability to ensure reliability and control. While recent systems incorporate verification techniques, it remains unclear how users can effectively apply such rigid constraints to represent intent or adapt to real-world variability. For example, prior work finds that hard-only constraints are too rigid, and numeric flexibility weights confuse users. We investigate how interaction workflows can better support users in applying constraints to guide LLM-generated plans, examining whether abstracting strictness into high-level types (i.e., hard and soft) paired with distinct verification mechanisms helps users more reliably express and align intent. We present U-Define, a system that lets users define constraints in natural language and categorize them as either hard rules that must not be violated or soft preferences that allow flexibility. U-Define verifies these types through complementary methods: formal model checking for hard constraints and LLM-as-judge evaluation for soft ones. Through a technical evaluation and user studies with general and expert participants, we find that user-defined constraint types improve perceived usefulness, performance, and satisfaction while maintaining usability. These findings provide insights for designing flexible yet reliable constraint-based workflows.

### 🤖 AI 总结

**一句话总结**：LLMs are increasingly used for end-user task planning, yet their black-box nature limits users' ability to ensure reliability and control. While recent systems incorporate verification techniques, it ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：U-Define, Designing, User, Workflows, Hard, Soft, Constraints, LLM-Based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02765v1) | [下载PDF](https://arxiv.org/pdf/2605.02765v1.pdf)

---

## [10. Triple Spectral Fusion for Sensor-based Human Activity Recognition](https://arxiv.org/abs/2605.02743v1)

**作者**：Ye Zhang, Longguang Wang, Qing Gao 等 6 位作者  
**分类**：cs.AI, cs.CV, cs.HC  
**发布时间**：2026-05-04

### 📄 论文摘要

The field of sensor-based human activity recognition (HAR) mainly uses posture, motion and context data of Inertial Measurement Units (IMUs) to identify daily activities. Despite the advancements in learning-based methods, it is challenging to perform information fusion from the temporal perspective due to the complexities in fusing heterogeneous sensor data and establishing long-term context correlations. This paper proposes a novel triple spectral fusion framework tailored for HAR. First, we develop an adaptive complementary filtering technique for noise suppression and organize each IMU's sensors into posture and motion modality nodes. Given that IMU nodes form a dynamic heterogeneous graph, we then apply adaptive filtering within the graph Fourier domain to merge both homogeneous and heterogeneous node information. Furthermore, an adaptive wavelet frequency selection approach is implemented to suppress context redundancy and shorten the length of features. This approach enhances both timestamp-based graph aggregation and the correlation of long-term contexts. Our framework uses adaptive filtering in the Fourier, graph Fourier, and wavelet domains, enabling effective multi-sensor fusion and context correlation. Extensive experiments on ten benchmark datasets demonstrate the superior performance of our framework. Project page: https://github.com/crocodilegogogo/TSF-TPAMI2026.

### 🤖 AI 总结

**一句话总结**：The field of sensor-based human activity recognition (HAR) mainly uses posture, motion and context data of Inertial Measurement Units (IMUs) to identify daily activities. Despite the advancements in l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Triple, Spectral, Fusion, Sensor-based, Human, Activity, Recognition, field

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02743v1) | [下载PDF](https://arxiv.org/pdf/2605.02743v1.pdf)

---

## cs.CL

## [11. FlexSQL: Flexible Exploration and Execution Make Better Text-to-SQL Agents](https://arxiv.org/abs/2605.02815v1)

**作者**：Quang Hieu Pham, Yang He, Ping Nie 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-04

### 📄 论文摘要

Text-to-SQL over large analytical databases requires navigating complex schemas, resolving ambiguous queries, and grounding decisions in actual data. Most current systems follow a fixed pipeline where schema elements are retrieved once upfront and the database is only revisited for post-hoc repair, limiting recovery from early mistakes. We present FlexSQL, a text-to-SQL agent whose core design principle is flexible database interaction: the agent can explore schema structure, inspect data values, and run verification queries at any point during reasoning. FlexSQL generates diverse execution plans to cover multiple query interpretations, implements each plan in either SQL or Python depending on the task, and uses a two-tiered repair mechanism that can backtrack from code-level errors to plan-level revisions. On Spider2-Snow, using gpt-oss-120b, FlexSQL achieves a 65.4\% score, outperforming strong open-source baselines that use stronger, larger models such as gpt-o3 and DeepSeek-R1. When integrated into a general-purpose coding agent (as skills in Claude Code), our approach yields over 10\% relative improvement on Spider2-Snow. Further analysis shows that flexible exploration and flexible execution jointly contribute to the effectiveness of our approach, highlighting flexibility as a key design principle. Our code is available at: https://github.com/StringNLPLAB/FlexSQL

### 🤖 AI 总结

**一句话总结**：Text-to-SQL over large analytical databases requires navigating complex schemas, resolving ambiguous queries, and grounding decisions in actual data. Most current systems follow a fixed pipeline where...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, FlexSQL, Flexible, Exploration, Execution, Make, Better, Text-to-SQL

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02815v1) | [下载PDF](https://arxiv.org/pdf/2605.02815v1.pdf)

---

## cs.CV

## [12. AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion](https://arxiv.org/abs/2605.02892v1)

**作者**：Yu-Ju Tsai, Brian Price, Qing Liu 等 8 位作者  
**分类**：cs.CV, cs.IR  
**发布时间**：2026-05-04

### 📄 论文摘要

Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/

### 🤖 AI 总结

**一句话总结**：Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AlbumFill, Album-Guided, Reasoning, Retrieval, Personalized, Image, Completion, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02892v1) | [下载PDF](https://arxiv.org/pdf/2605.02892v1.pdf)

---

## [13. Laplacian Frequency Interaction Network for Rural Thematic Road Extraction](https://arxiv.org/abs/2605.02866v1)

**作者**：Baiyan Chen, Weixin Zhai  
**分类**：cs.CV  
**发布时间**：2026-05-04

### 📄 论文摘要

Rural thematic road network construction aims to extract topological road structures from movement trajectory images of agricultural machinery. However, this task faces challenges where downsampling methods commonly used in existing studies tend to blur the sparse high-frequency road structures, and the heavy noise from dense field operations often leads to fragmented or redundant topologies in the extracted networks. To address these challenges, we propose LFINet, a Laplacian Frequency Interaction Network. The network begins with a Laplacian Multi-scale Separator (LMS) to decouple the image into low-frequency semantic contexts and high-frequency structural details. These components are then processed by the Cross-Frequency Interaction Block (CFIB) through a dual-pathway architecture in which a High-Frequency Block (HFB) refines local structures while a Spatial Transformer (ST) captures global semantics. Subsequently, a Frequency Gated Modulation (FGM) mechanism integrates the features from pathways by leveraging semantic contexts to calibrate the structural details. Finally, a Progressive Reconstruction Decoder iteratively fuses multi-scale features to ensure topological consistency. Experiments conducted on a real-world agricultural trajectories dataset from Henan Province, China, show that LFINet establishes a new state-of-the-art. Specifically, it achieves an F1-score of 92.54% and an IoU of 86.12%, surpassing the second-ranked method by 0.64% and 1.1%, respectively. This confirms its capability to effectively construct topological road networks from noisy and sparse field data.

### 🤖 AI 总结

**一句话总结**：Rural thematic road network construction aims to extract topological road structures from movement trajectory images of agricultural machinery. However, this task faces challenges where downsampling m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Laplacian, Frequency, Interaction, Network, Rural, Thematic, Road, Extraction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02866v1) | [下载PDF](https://arxiv.org/pdf/2605.02866v1.pdf)

---

## [14. Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions](https://arxiv.org/abs/2605.02863v1)

**作者**：Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-04

### 📄 论文摘要

Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.

### 🤖 AI 总结

**一句话总结**：Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image di...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Pixel, Perfect, Relational, Image, Quality, Assessment, Spatially-Aware, Distortions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02863v1) | [下载PDF](https://arxiv.org/pdf/2605.02863v1.pdf)

---

## [15. Active Sampling for Ultra-Low-Bit-Rate Video Compression via Conditional Controlled Diffusion](https://arxiv.org/abs/2605.02849v1)

**作者**：Amirhosein Javadi, Shirin Saeedi Bidokhti, Tara Javidi  
**分类**：cs.CV  
**发布时间**：2026-05-04

### 📄 论文摘要

Diffusion models provide a powerful generative prior for perceptual reconstruction at ultra-low bitrates, but effective video compression requires controlling the generative process using highly compact conditioning signals. In this work, we present ActDiff-VC, a diffusion-based video compression framework for the ultra-low-bitrate regime. Our method partitions videos into variable-length segments, transmits keyframes only when needed, and summarizes temporal dynamics using a compact set of tracked point trajectories. Conditioned on these sparse signals, a conditional diffusion decoder synthesizes the remaining frames, enabling perceptually realistic reconstruction under severe rate constraints. To support this design, we introduce two mechanisms: content-adaptive keyframe selection and budget-aware sparse trajectory selection, which together enable compact yet effective conditioning for generative reconstruction. Experiments on the UVG and MCL-JCV benchmarks show that ActDiff-VC achieves up to 64.6\% bitrate reduction at matched NIQE, improves KID by up to 64.6\% and FID by up to 37.7\% at comparable bitrates against strong learned codecs, and delivers favorable perceptual rate--distortion trade-offs relative to learned and diffusion-based baselines in the ultra-low-bitrate regime.

### 🤖 AI 总结

**一句话总结**：Diffusion models provide a powerful generative prior for perceptual reconstruction at ultra-low bitrates, but effective video compression requires controlling the generative process using highly compa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Active, Sampling, Ultra-Low-Bit-Rate, Video, Compression, via, Conditional, Controlled

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02849v1) | [下载PDF](https://arxiv.org/pdf/2605.02849v1.pdf)

---

## [16. VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition](https://arxiv.org/abs/2605.02834v1)

**作者**：Tanush Yadav, Mohammadreza Salehi, Jae Sung Park 等 9 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-05-04

### 📄 论文摘要

Videos are unique in their ability to capture actions which transcend multiple frames. Accordingly, for many years action recognition was the quintessential task for video understanding. Unfortunately, due to a lack of sufficiently diverse and challenging data, modern vision-language models (VLMs) are no longer evaluated on their action recognition capabilities. To revitalize action recognition in the era of VLMs, we advocate for a returned focus on domain-specific actions. To this end, we introduce VideoNet, a domain-specific action recognition benchmark covering 1,000 distinct actions from 37 domains. We begin with a multiple-choice evaluation setting, where the difference between closed and open models is stark: Gemini 3.1 Pro attains 69.9% accuracy while Qwen3-VL-8B gets a mere 45.0%. To understand why VLMs struggle on VideoNet, we relax the questions into a binary setting, where random chance is 50%. Still, Qwen achieves only 59.2% accuracy. Further relaxing the evaluation setup, we provide $k\in\{1,2,3\}$ in-context examples of the action. Some models excel in the few-shot setting, while others falter; Qwen improves $+7.0\%$, while Gemini declines $-4.8\%$. Notably, these gains fall short of the $+13.6\%$ improvement in non-expert humans when given few-shot examples. Finding that VLMs struggle to fully exploit in-context examples, we shift from test-time improvements to the training side. We collect the first large-scale training dataset for domain-specific actions, totaling nearly 500k video question-answer pairs. Fine-tuning a Molmo2-4B model on our data, we surpass all open-weight 8B models on the VideoNet benchmark.

### 🤖 AI 总结

**一句话总结**：Videos are unique in their ability to capture actions which transcend multiple frames. Accordingly, for many years action recognition was the quintessential task for video understanding. Unfortunately...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VideoNet, Large-Scale, Dataset, Domain-Specific, Action, Recognition, Videos, unique

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02834v1) | [下载PDF](https://arxiv.org/pdf/2605.02834v1.pdf)

---

## [17. IConFace: Identity-Structure Asymmetric Conditioning for Unified Reference-Aware Face Restoration](https://arxiv.org/abs/2605.02814v1)

**作者**：Axi Niu, Jinyang Zhang, Senyan Qing  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-04

### 📄 论文摘要

Blind face restoration is highly ill-posed under severe degradation, where identity-critical details may be missing from the degraded input. Same-identity references reduce this ambiguity, but mismatched pose, expression, illumination, age, makeup, or local facial states can lead to overuse of reference appearance. We propose \textbf{IConFace}, a unified reference-aware and no-reference framework with identity--structure asymmetric conditioning. References are distilled into a norm-weighted global AdaFace identity anchor for image-only modulation, while the degraded image is reinforced as the spatial structure anchor through low-rank residuals and block-wise degraded cross-attention with two-route memory. The resulting single checkpoint exploits references when available and falls back to no-reference restoration when absent, improving identity consistency, fine-detail recovery, and degraded-only restoration quality in a unified model.

### 🤖 AI 总结

**一句话总结**：Blind face restoration is highly ill-posed under severe degradation, where identity-critical details may be missing from the degraded input. Same-identity references reduce this ambiguity, but mismatc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IConFace, Identity-Structure, Asymmetric, Conditioning, Unified, Reference-Aware, Face, Restoration

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02814v1) | [下载PDF](https://arxiv.org/pdf/2605.02814v1.pdf)

---

## [18. Edge-Efficient Image Restoration: Transformer Distillation into State-Space Models](https://arxiv.org/abs/2605.02794v1)

**作者**：Srinivas Soumitri Miriyala, Sowmya Vajrala, Sravanth Kodavanti 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-04

### 📄 论文摘要

We propose a modular framework for hybrid image restoration that integrates transformer and state-space model (SSM) blocks with a focus on improving runtime efficiency on edge hardware. While transformers provide strong global modeling through self-attention, their attention kernels incur substantial latency on mobile devices, especially for high-resolution inputs. In contrast, SSMs such as Mamba offer lineartime sequence modeling with lower runtime overhead but may underperform on fine grained restoration tasks. To balance accuracy and efficiency, we train lightweight SSM blocks as feature-distilled surrogates of transformer blocks and use them to construct hybrid U-Net-style architectures. To automatically discover effective block combinations, we introduce Efficient Network Search (ENS), a multi-objective search strategy that selects task-specific hybrid configurations from pre-aligned components. ENS optimizes restoration quality while penalizing transformer usage, serving as a lightweight proxy for latency and enabling architecture discovery without repeated hardware profiling. On a Snapdragon 8 Elite CPU, the Restormer baseline requires 10119.52 ms for inference. In contrast, ENS-discovered hybrids significantly reduce runtime: ENS-Deblurring runs in 2973 ms (3.4x faster), ENS-Deraining in 5816 ms (1.74x faster), and ENS-Denoising in 8666 ms (1.17x faster), while maintaining competitive restoration quality.

### 🤖 AI 总结

**一句话总结**：We propose a modular framework for hybrid image restoration that integrates transformer and state-space model (SSM) blocks with a focus on improving runtime efficiency on edge hardware. While transfor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Edge-Efficient, Image, Restoration, Transformer, Distillation, State-Space, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02794v1) | [下载PDF](https://arxiv.org/pdf/2605.02794v1.pdf)

---

## [19. HumanSplatHMR: Closing the Loop Between Human Mesh Recovery and Gaussian Splatting Avatar](https://arxiv.org/abs/2605.02784v1)

**作者**：Yeheng Zong, Pou-Chun Kung, Yike Pan 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-04

### 📄 论文摘要

Accurately recovering human pose and appearance from video is an essential component of scene reconstruction, with applications to motion capture, motion prediction, virtual reality, and digital twinning. Despite significant interest in building realistic human avatars from video, this paper demonstrates that existing methods do not accurately recover the 3D geometry of humans. ViT-based approaches are not consistently reliable and can overfit to 2D views, while NeRF- and Gaussian Splatting-based avatars treat pose and appearance separately, limiting rendering generalization to new poses. To resolve these shortcomings, this paper proposes HumanSplatHMR, a joint optimization framework that refines 3D human poses while simultaneously learning a high-fidelity avatar for novel-view and novel-pose synthesis. Our key insight is to close the loop between geometric pose estimation and differentiable rendering. Unlike prior human avatar methods that rely on accurate human pose obtained through motion capture systems or offline refinement, which are impractical in in-the-wild scenarios, our approach uses only human mesh estimates from a state-of-the-art human pose estimator to better reflect real-world conditions. Therefore, instead of using the human pose only as a deformation prior, HumanSplatHMR backpropagates photometric, segmentation, and depth losses through a differentiable renderer to the pose parameters and global position. This coupling refines the global 3D pose over time, improving accuracy and alignment while producing better renderings from novel views. Experiments show consistent improvements over pose recovery baselines that omit image-level refinement and avatar baselines that decouple pose estimation from avatar reconstruction.

### 🤖 AI 总结

**一句话总结**：Accurately recovering human pose and appearance from video is an essential component of scene reconstruction, with applications to motion capture, motion prediction, virtual reality, and digital twinn...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HumanSplatHMR, Closing, Loop, Between, Human, Mesh, Recovery, Gaussian

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02784v1) | [下载PDF](https://arxiv.org/pdf/2605.02784v1.pdf)

---

## [20. Linearizing Vision Transformer with Test-Time Training](https://arxiv.org/abs/2605.02772v1)

**作者**：Yining Li, Dongchen Han, Zeyu Liu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-04

### 📄 论文摘要

While linear-complexity attention mechanisms offer a promising alternative to Softmax attention for overcoming the quadratic bottleneck, training such models from scratch remains prohibitively expensive. Inheriting weights from pretrained Transformers provides an appealing shortcut, yet the fundamental representational gap between Softmax and linear attention prevents effective weight transfer. In this work, we address this conversion challenge from two perspectives: architectural alignment and representational alignment. We identify Test-Time Training (TTT) as a linear-complexity architecture whose two-layer dynamic formulation is structurally aligned with Softmax attention, enabling direct inheritance of pretrained attention weights. To further align representational properties, including key shift-invariance and locality, we introduce key instance normalization and a lightweight locality enhancement module. We validate our approach by linearizing Stable Diffusion 3.5 and introduce SD3.5-T$^5$ (Transformer To Test Time Training). With only 1 hour of fine-tuning on 4$\times$H20 GPUs, SD3.5-T$^5$ achieves comparable text-to-image quality to the fine-tuned Softmax model, while accelerating inference by 1.32$\times$ and 1.47$\times$ at 1K and 2K resolutions.

### 🤖 AI 总结

**一句话总结**：While linear-complexity attention mechanisms offer a promising alternative to Softmax attention for overcoming the quadratic bottleneck, training such models from scratch remains prohibitively expensi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Linearizing, Vision, Transformer, Test-Time, Training, While, linear-complexity, attention

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02772v1) | [下载PDF](https://arxiv.org/pdf/2605.02772v1.pdf)

---

## [21. TOC-SR: Task-Optimal Compact diffusion for Image Super Resolution](https://arxiv.org/abs/2605.02767v1)

**作者**：Sowmya Vajrala, Akshay Bankar, Manjunath Arveti 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-04

### 📄 论文摘要

Diffusion models have recently demonstrated strong performance for image restoration tasks, including super-resolution. However, their large model size and iterative sampling procedures make them computationally expensive for practical deployment. In this work, we present TOC-SR, a framework for building efficient one-step super-resolution models by first discovering a compact diffusion backbone. Starting from a sixteen-channel latent diffusion model, we construct parameter-efficient surrogate blocks using feature-wise generative distillation and perform architecture discovery using epsilon-constrained Bayesian Optimization to minimize model complexity while preserving generative fidelity. The resulting compact diffusion backbone achieves a 6.6x reduction in parameters and a 2.8x reduction in GMACs compared to the expanded diffusion model. We then adapt this backbone for super-resolution and distill the diffusion process into a single-step generator. Experiments demonstrate that the proposed approach enables efficient super-resolution while maintaining strong reconstruction quality.

### 🤖 AI 总结

**一句话总结**：Diffusion models have recently demonstrated strong performance for image restoration tasks, including super-resolution. However, their large model size and iterative sampling procedures make them comp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, TOC-SR, Task-Optimal, Compact, Image, Super, Resolution, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02767v1) | [下载PDF](https://arxiv.org/pdf/2605.02767v1.pdf)

---

## [22. FoR-Net: Learning to Focus on Hard Regions for Efficient Semantic Segmentation](https://arxiv.org/abs/2605.02764v1)

**作者**：Hsin-Jui Pan, Sheng-Wei Chan, Meng-Qian Li 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-04

### 📄 论文摘要

We present FoR-Net, a lightweight architecture for semantic segmentation that focuses on identifying and enhancing hard regions. Instead of relying on heavy global modeling, FoR-Net adopts an efficient strategy that selectively emphasizes informative regions through a learned importance map and a Top-K activation mechanism. Specifically, a selector module predicts region-wise importance, enabling the model to focus on challenging areas such as thin structures and object boundaries. Multi-scale reasoning is achieved using convolutional branches with different receptive fields, allowing diverse spatial context aggregation. We evaluate FoR-Net on the Cityscapes benchmark under limited computational resources. Despite its lightweight design and standard training configuration, FoR-Net achieves competitive performance and demonstrates improved consistency in challenging regions. These results suggest that region-focused reasoning provides a simple yet effective inductive bias for efficient semantic segmentation.

### 🤖 AI 总结

**一句话总结**：We present FoR-Net, a lightweight architecture for semantic segmentation that focuses on identifying and enhancing hard regions. Instead of relying on heavy global modeling, FoR-Net adopts an efficien...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FoR-Net, Learning, Focus, Hard, Regions, Efficient, Semantic, Segmentation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02764v1) | [下载PDF](https://arxiv.org/pdf/2605.02764v1.pdf)

---

## [23. Does it Really Count? Assessing Semantic Grounding in Text-Guided Class-Agnostic Counting](https://arxiv.org/abs/2605.02752v1)

**作者**：Giacomo Pacini, Luca Ciampi, Nicola Messina 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-04

### 📄 论文摘要

Open-world text-guided class-agnostic counting (CAC) has emerged as a flexible paradigm for counting arbitrary object classes by using natural language prompts. However, current evaluation protocols primarily focus on standard counting errors within single-category images, overlooking a fundamental requirement: the ability to correctly ground the textual prompt in the visual scene. In this paper, we show that several state-of-the-art CAC models often struggle to determine which object class should be counted based on the given prompt, revealing a misalignment between textual semantics and visual object representations. This limitation leads to spurious counting responses and reduced reliability in real-world scenarios. To systematically address these limitations, we propose a new evaluation framework focused on model robustness and trustworthiness. Our contribution is two-fold: (i) we introduce PrACo++ (Prompt-Aware Counting++), a novel test suite featuring two dedicated evaluation protocols -- the negative-label test and the distractor test -- paired with new specialized metrics; and (ii) we present the MUCCA (MUlti-Category Class-Agnostic counting) evaluation dataset, a new collection of real-world images featuring multiple annotated object categories per scene, unlike existing CAC benchmarks that typically include a single category per image. Our extensive experimental evaluation of 10 state-of-the-art methods shows that, despite strong performance under standard counting metrics, current models exhibit significant weaknesses in understanding and grounding object class descriptions. Finally, we provide a quantitative analysis of how semantic similarity between prompts influences these failures. Overall, our results underscore the need for more semantically grounded architectures and offer a reliable framework for future assessment in open-world text-guided CAC methods.

### 🤖 AI 总结

**一句话总结**：Open-world text-guided class-agnostic counting (CAC) has emerged as a flexible paradigm for counting arbitrary object classes by using natural language prompts. However, current evaluation protocols p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：it, Does, Really, Count?, Assessing, Semantic, Grounding, Text-Guided

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02752v1) | [下载PDF](https://arxiv.org/pdf/2605.02752v1.pdf)

---

## [24. Virtual Scanning for NSCLC Histology: Investigating the Discriminatory Power of Synthetic PET](https://arxiv.org/abs/2605.02746v1)

**作者**：Fatih Aksu, Laura Ciuffetti, Francesco Di Feola 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-04

### 📄 论文摘要

Accurate histological differentiation between adenocarcinoma (ADC) and squamous cell carcinoma (SCC) is critical for personalized treatment in non-small cell lung cancer (NSCLC). While [$^{18}$F]FDG PET/CT is a standard tool for the clinical evaluation of lung cancer, its utility is often limited by high costs and radiation exposure. In this paper, we investigate the feasibility of "virtual scanning" as a feature-enhancement strategy by evaluating whether synthetic PET data can provide complementary feature representations to supplement anatomical CT scans in histological subtype classification.   We propose a framework that leverages a 3D Pix2Pix Generative Adversarial Network (GAN), pretrained on the FDG-PET/CT Lesions dataset, to synthesize pseudo-PET volumes from anatomical CT scans. These synthetic volumes are integrated with structural CT data within the MINT framework, a multi-stage intermediate fusion architecture.   Our experiments, conducted on a multi-center dataset of 714 subjects, demonstrate that the inclusion of synthetic metabolic features significantly improves classification performance over a CT-only baseline. The multimodal approach achieved a statistically significant increase in the Area Under the Curve (AUC) from 0.489 to 0.591 and improved the Geometric Mean (GMean) from 0.305 to 0.524. These results suggest that synthetic PET scans provide discriminatory metabolic cues that enable deep learning models to exploit complementary cross-modal information, offering a potential feature-enhancement strategy for clinical scenarios where physical PET scans are unavailable.

### 🤖 AI 总结

**一句话总结**：Accurate histological differentiation between adenocarcinoma (ADC) and squamous cell carcinoma (SCC) is critical for personalized treatment in non-small cell lung cancer (NSCLC). While [$^{18}$F]FDG P...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Virtual, Scanning, NSCLC, Histology, Investigating, Discriminatory, Power

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02746v1) | [下载PDF](https://arxiv.org/pdf/2605.02746v1.pdf)

---

## cs.LG

## [25. Unsupervised Machine Learning for Detecting Structural Anomalies in European Regional Statistics](https://arxiv.org/abs/2605.02884v1)

**作者**：Bogdan Oancea  
**分类**：cs.LG  
**发布时间**：2026-05-04

### 📄 论文摘要

Ensuring the coherence of regional socio-economic statistics is a central task for national statistical institutes. Traditional validation tools, such as range edits, ratio checks, or univariate outlier detection, are effective for identifying extreme values in individual series but are less suited for detecting unusual combinations of indicators in high-dimensional settings. This paper proposes an unsupervised machine learning framework for identifying structurally atypical regional profiles within Europe using publicly available Eurostat data. We construct a cross-sectional dataset of NUTS2 regions (2022) covering four key indicators: GDP per capita in PPS, unemployment rate, tertiary educational attainment, and population density. We apply and compare five anomaly detection techniques, univariate z-scores, Mahalanobis distance, Isolation Forest, Local Outlier Factor, and One-Class SVM, and classify a region as a structural anomaly if it is flagged by at least three of the five methods. The findings show that machine learning methods identify a consistent set of regions whose multivariate profiles diverge substantially from the EU-wide pattern. These include both highly developed metropolitan economies (Brussels, Vienna, Berlin, Prague) and regions with persistent socio-economic disadvantages (Central and Western Slovakia, Northern Hungary, Castilla-La Mancha, Extremadura), as well as Istanbul, whose profile differs markedly from EU capital regions. Importantly, these anomalies do not necessarily signal data quality issues; rather, they reflect meaningful structural divergence that warrants analytical or policy attention. The proposed framework is fully reproducible, scalable, and compatible with existing validation workflows, offering a flexible tool for early detection of unusual regional configurations within the European Statistical System.

### 🤖 AI 总结

**一句话总结**：Ensuring the coherence of regional socio-economic statistics is a central task for national statistical institutes. Traditional validation tools, such as range edits, ratio checks, or univariate outli...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unsupervised, Machine, Learning, Detecting, Structural, Anomalies, European, Regional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02884v1) | [下载PDF](https://arxiv.org/pdf/2605.02884v1.pdf)

---

## [26. Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters](https://arxiv.org/abs/2605.02867v1)

**作者**：Lingxiao Kong, Cong Yang, Oya Deniz Beyan 等 4 位作者  
**分类**：cs.LG, cs.AI, cs.RO  
**发布时间**：2026-05-04

### 📄 论文摘要

Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.

### 🤖 AI 总结

**一句话总结**：Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, of, Enhancing, Generalizability, Robotics, through, SHAP, Analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02867v1) | [下载PDF](https://arxiv.org/pdf/2605.02867v1.pdf)

---

## [27. Trust, but Verify: Peeling Low-Bit Transformer Networks for Training Monitoring](https://arxiv.org/abs/2605.02853v1)

**作者**：Arian Eamaz, Farhang Yeganegi, Mojtaba Soltanalian  
**分类**：cs.LG  
**发布时间**：2026-05-04

### 📄 论文摘要

Understanding whether deep neural networks are effectively optimized remains challenging, as training occurs in highly nonconvex landscapes and standard metrics provide limited visibility into layer-wise learning quality. This challenge is particularly acute for transformer-based language models, where training is expensive, models are often reused in frozen form, and poorly optimized layers can silently degrade performance. We propose a layer-wise peeling framework for monitoring training dynamics, in which each transformer layer is locally optimized against intermediate representations of the trained model. By constructing lightweight, layer-specific reference solutions and projecting layers onto multiple intermediate outputs via different permutations, we obtain achievable baselines that enable fine-grained diagnosis of under-optimized layers. Experiments on decoder-only transformer models show that these layer-wise reference bounds can match or even surpass the trained model at various stages of training, exposing inefficiencies that remain hidden in aggregate loss curves. We further demonstrate that this analysis remains effective under binarization and quantized settings, where training dynamics are particularly fragile. Across all numerical results, the proposed bounds consistently separate apparent convergence from effective optimality, highlighting optimization opportunities that are invisible when relying on training loss alone.

### 🤖 AI 总结

**一句话总结**：Understanding whether deep neural networks are effectively optimized remains challenging, as training occurs in highly nonconvex landscapes and standard metrics provide limited visibility into layer-w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Trust, but, Verify, Peeling, Low-Bit, Transformer, Networks, Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02853v1) | [下载PDF](https://arxiv.org/pdf/2605.02853v1.pdf)

---

## [28. A Closed-Form Persistence-Landmark Pipeline for Certified Point-Cloud and Graph Classification](https://arxiv.org/abs/2605.02836v1)

**作者**：Sushovan Majhi, Atish Mitra, Žiga Virk 等 4 位作者  
**分类**：cs.LG, math.AT  
**发布时间**：2026-05-04

### 📄 论文摘要

We introduce PLACE (Persistence-Landmark Analytic Classification Engine), a closed-form pipeline for classifying point clouds and graphs through their persistent-homology signatures. Three quantitative guarantees -- a margin-based excess-risk rate, a closed-form descriptor-selection rule, and a per-prediction certificate -- are derived from training labels alone, with no learned weights or held-out calibration. The embedding sums Mitra-Virk single-point coordinate functions over a sparse landmark grid; closed-form weights maximize a structural distortion constant $λ(ν)$ (a Lipschitz lower bound on $\mathcal{D}_n$ under non-interference). (i) An $O(kR/(Δ\sqrt{m_{\min}}))$ margin bound, driven by class-mean separation $Δ$ and embedding radius $R$, matched by a sample-starved minimax lower bound. (ii) The Mahalanobis margin under Ledoit-Wolf-shrunk covariance is the strongest closed-form descriptor selector on a heterogeneous 64-descriptor chemical-graph pool (mean Spearman $ρ\approx +0.54$ across 10 benchmarks, positive on 9 of 10); the isotropic surrogate $Δ/\sqrt\ell$ admits a closed-form selection-consistency rate on homogeneous (14-15 descriptor) protein/social pools. (iii) A training-time-decided certificate with no per-prediction overhead, in non-asymptotic Pinelis and asymptotic Gaussian plug-in forms. Empirically, PLACE is the strongest diagram-based method on Orbit5k and matches the strongest topology-based baseline within statistical noise on MUTAG and COX2. The remaining gaps fall into two diagnosable regimes: descriptor blindness on NCI1/NCI109, and pool-coverage limits elsewhere. Both radii exceed the firing threshold $\hatΔ/2$ on every benchmark at our training-set sizes, dominated by the $\sqrt\ell$ scaling of the multivariate-norm bound; the per-prediction certificate is constructive but not yet operational at these sizes.

### 🤖 AI 总结

**一句话总结**：We introduce PLACE (Persistence-Landmark Analytic Classification Engine), a closed-form pipeline for classifying point clouds and graphs through their persistent-homology signatures. Three quantitativ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Closed-Form, Persistence-Landmark, Pipeline, Certified, Point-Cloud, Graph, Classification

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02836v1) | [下载PDF](https://arxiv.org/pdf/2605.02836v1.pdf)

---

## [29. A decoupled diffusion planner that adapts to changing cost limits by using cost-conditioned generation for safety and reward gradients for performance](https://arxiv.org/abs/2605.02777v1)

**作者**：Rufeng Chen, Zhaofan Zhang, Zhejiang Yang 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-04

### 📄 论文摘要

Offline safe reinforcement learning often requires policies to adapt at deployment time to safety budgets that vary across episodes or change within a single episode. While diffusion-based planners enable flexible trajectory generation, existing guidance schemes often treat reward improvement and constraint satisfaction as competing gradient objectives, which can lead to unreliable safety compliance under cost limits. We reinterpret adaptive safe trajectory generation as sampling from a constrained trajectory distribution, where the budget restricts the trajectory region, and reward shapes preferences within that region. This perspective motivates Safe Decoupled Guidance Diffusion (SDGD), which conditions classifier-free guidance on the cost limit to bias sampling toward trajectories satisfying the specified limit, while using reward-gradient guidance to refine trajectories for higher return. Because direct reward guidance can increase return while also steering samples toward trajectories with higher cumulative cost, we introduce Feasible Trajectory Relabeling (FTR) to reshape reward targets and discourage such directions. We further provide a first-order sampling-time analysis showing that FTR suppresses reward-induced cost drift under a prefix-restorative alignment condition. Extensive evaluations on the DSRL benchmark show that SDGD achieves the strongest safety compliance among baselines, satisfying the constraint on 94.7% of tasks (36/38), while obtaining the highest reward among safe methods on 21 tasks.

### 🤖 AI 总结

**一句话总结**：Offline safe reinforcement learning often requires policies to adapt at deployment time to safety budgets that vary across episodes or change within a single episode. While diffusion-based planners en...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, decoupled, planner, adapts, changing, cost, limits, cost-conditioned

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02777v1) | [下载PDF](https://arxiv.org/pdf/2605.02777v1.pdf)

---

## [30. Bolek: A Multimodal Language Model for Molecular Reasoning](https://arxiv.org/abs/2605.02745v1)

**作者**：Frederic Grabowski, Jacek Szczerbiński, Maciej Jaśkowski 等 7 位作者  
**分类**：cs.LG, cs.AI, q-bio.BM  
**发布时间**：2026-05-04

### 📄 论文摘要

Molecular property models increasingly support high-stakes drug-discovery decisions, but their outputs are often difficult to audit: classical predictors return scores without rationale, while language models can produce fluent explanations weakly grounded in the input molecule.   We introduce Bolek, a compact multimodal language model that grounds natural-language reasoning in molecular structure by injecting a Morgan fingerprint embedding into an instruction-tuned text decoder. Bolek is fine-tuned on molecular alignment tasks, including molecule description, RDKit descriptor prediction, and substructure detection, and on downstream reasoning over 15 TDC binary classification tasks using synthetic chains-of-thought anchored in concrete molecular features.   Across these tasks, Bolek outperforms its Qwen3-4B-Instruct base on all endpoints in yes/no mode and on 13 of 15 in chain-of-thought mode, raising mean ROC/PR AUC from 0.55 to 0.76. It also outperforms TxGemma-9B-Chat on 13 of 15 binary classification tasks despite being less than half its size. Bolek's explanations are more grounded than those of the baseline LLMs: it cites numerical descriptors 10-100x more often per chain-of-thought, and the cited values agree strongly with RDKit for key descriptors such as TPSA, MolLogP, and MolWt (Spearman rho = 0.87-0.91). Generalisation extends beyond the training panel: on 15 unseen TDC classification endpoints, Bolek matches TxGemma on five, and it produces non-trivial rank correlations on three held-out regression endpoints despite never seeing downstream regression during training.   These results suggest that targeted modality injection and reasoning supervision tied to verifiable molecular features can yield compact, auditable molecular reasoning models.

### 🤖 AI 总结

**一句话总结**：Molecular property models increasingly support high-stakes drug-discovery decisions, but their outputs are often difficult to audit: classical predictors return scores without rationale, while languag...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bolek, Multimodal, Language, Model, Molecular, Reasoning, property, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.02745v1) | [下载PDF](https://arxiv.org/pdf/2605.02745v1.pdf)

---

