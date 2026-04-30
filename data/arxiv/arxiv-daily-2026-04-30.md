# arXiv AI 论文日报 | 2026-04-30

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (12 篇)
- [cs.LG](#csLG) (13 篇)
- [cs.CL](#csCL) (4 篇)
- [cs.AI](#csAI) (1 篇)

---

## cs.AI

## [1. Bian Que: An Agentic Framework with Flexible Skill Arrangement for Online System Operations](https://arxiv.org/abs/2604.26805v1)

**作者**：Bochao Liu, Zhipeng Qian, Yang Zhao 等 13 位作者  
**分类**：cs.AI, cs.MA  
**发布时间**：2026-04-29

### 📄 论文摘要

Operating and maintaining (O&M) large-scale online engine systems (search, recommendation, advertising) demands substantial human effort for release monitoring, alert response, and root cause analysis. While LLM-based agents are a natural fit for these tasks, the deployment bottleneck is not reasoning capability but orchestration: selecting, for each operational event, the relevant data (metrics, logs, change events) and the applicable operational knowledge (handbook rules and practitioner experience). Feeding all signals indiscriminately causes dilution and hallucination, while manually curating the event-to-(data, knowledge) mapping is intractable under dozens of daily releases. We present Bian Que, an agentic framework with three contributions: (i) a \emph{unified operational paradigm} abstracting day-to-day O&M into three canonical patterns: release interception, proactive inspection, and alert root cause analysis; (ii) \emph{Flexible Skill Arrangement}, where each Skill specifies which data and knowledge to retrieve for a given business-module context and can be automatically generated and updated by LLMs or iteratively refined through natural-language instructions from on-call engineers; (iii) a \emph{unified self-evolving mechanism} in which one correction signal drives two parallel pathways, case-memory-to-knowledge distillation and targeted Skill refinement. Deployed on the e-commerce search engine of KuaiShou, the major short-video platform in China, Bian Que reduces alert volume by 75%, achieves 80% root-cause analysis accuracy, and cuts mean time to resolution by over 50%. Our framework achieves 99.0% pass rate on offline evaluations. Our code is available at https://github.com/benchen4395/BianQue_Assistant.

### 🤖 AI 总结

**一句话总结**：Operating and maintaining (O&M) large-scale online engine systems (search, recommendation, advertising) demands substantial human effort for release monitoring, alert response, and root cause analysis...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Bian, Que, Agentic, Framework, Flexible, Skill, Arrangement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26805v1) | [下载PDF](https://arxiv.org/pdf/2604.26805v1.pdf)

---

## cs.CL

## [2. ClawGym: A Scalable Framework for Building Effective Claw Agents](https://arxiv.org/abs/2604.26904v1)

**作者**：Fei Bai, Huatong Song, Shuang Sun 等 13 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-04-29

### 📄 论文摘要

Claw-style environments support multi-step workflows over local files, tools, and persistent workspace states. However, scalable development around these environments remains constrained by the absence of a systematic framework, especially one for synthesizing verifiable training data and integrating it with agent training and diagnostic evaluation. To address this challenge, we present ClawGym, a scalable framework that supports the full lifecycle of Claw-style personal agent development. Concretely, we construct ClawGym-SynData, a diverse dataset of 13.5K filtered tasks synthesized from persona-driven intents and skill-grounded operations, paired with realistic mock workspaces and hybrid verification mechanisms. We then train a family of capable Claw-style models, termed ClawGym-Agents, through supervised fine-tuning on black-box rollout trajectories, and further explore reinforcement learning via a lightweight pipeline that parallelizes rollouts across per-task sandboxes.To support reliable evaluation, we further construct ClawGym-Bench, a benchmark of 200 instances calibrated through automated filtering and human-LLM review. Relevant resources will be soon released at https://github.com/ClawGym.

### 🤖 AI 总结

**一句话总结**：Claw-style environments support multi-step workflows over local files, tools, and persistent workspace states. However, scalable development around these environments remains constrained by the absenc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, ClawGym, Scalable, Framework, Building, Effective, Claw, Claw-style

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26904v1) | [下载PDF](https://arxiv.org/pdf/2604.26904v1.pdf)

---

## [3. HealthNLP_Retrievers at ArchEHR-QA 2026: Cascaded LLM Pipeline for Grounded Clinical Question Answering](https://arxiv.org/abs/2604.26880v1)

**作者**：Md Biplob Hosen, Md Alomgeer Hussein, Md Akmol Masud 等 6 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-04-29

### 📄 论文摘要

Patient portals now give individuals direct access to their electronic health records (EHRs), yet access alone does not ensure patients understand or act on the complex clinical information contained in these records. The ArchEHR-QA 2026 shared task addresses this challenge by focusing on grounded question answering over EHRs, and this paper presents the system developed by the HealthNLP_Retrievers team for this task. The proposed approach uses a multi-stage cascaded pipeline powered by the Gemini 2.5 Pro large language model to interpret patient-authored questions and retrieve relevant evidence from lengthy clinical notes. Our architecture comprises four integrated modules: (1) a few-shot query reformulation unit which summarizes verbose patient queries; (2) a heuristic-based evidence scorer which ranks clinical sentences to prioritize recall; (3) a grounded response generator which synthesizes professional-caliber answers restricted strictly to identified evidence; and (4) a high-precision many-to-many alignment framework which links generated answers to supporting clinical sentences. This cascaded approach achieved competitive results. Across the individual tracks, the system ranked 1st in question interpretation, 5th in answer generation, 7th in evidence identification, and 9th in answer-evidence alignment. These results show that integrating large language models within a structured multi-stage pipeline improves grounding, precision, and the professional quality of patient-oriented health communication. To support reproducibility, our source code is publicly available in our GitHub repository

### 🤖 AI 总结

**一句话总结**：Patient portals now give individuals direct access to their electronic health records (EHRs), yet access alone does not ensure patients understand or act on the complex clinical information contained ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, LLM, HealthNLP, Retrievers, ArchEHR-QA, Cascaded, Pipeline, Grounded

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26880v1) | [下载PDF](https://arxiv.org/pdf/2604.26880v1.pdf)

---

## [4. What Kind of Language is Easy to Language-Model Under Curriculum Learning?](https://arxiv.org/abs/2604.26844v1)

**作者**：Nadine El-Naggar, Tatsuki Kuribayashi, Ted Briscoe  
**分类**：cs.CL  
**发布时间**：2026-04-29

### 📄 论文摘要

Many of the thousands of attested languages share common configurations of features, creating a spectrum from typologically very rare (e.g., object-verb-subject word order) or impossible languages to very common combinations of features (e.g., subject-object-verb word order). One central question is under what conditions such typological tendencies can be predicted, and specifically whether the learning bias of language models (LMs) is sufficient to reproduce such patterns. In this study, we add one dimensionality to such analysis -- the learning scenario for LMs -- to explore its interaction with the inductive bias of LMs. Specifically, as a first study, we examine the effect of curriculum learning (CL), as a developmentally motivated learning scenario, i.e., starting with simpler sentences rather than randomly-ordered input. We expand existing LM-based exploration (El-Naggar et al., 2025a,b) with a simple CL variant and find that CL substantially impacts the apparent inductive bias of LMs.

### 🤖 AI 总结

**一句话总结**：Many of the thousands of attested languages share common configurations of features, creating a spectrum from typologically very rare (e.g., object-verb-subject word order) or impossible languages to ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, What, Kind, Language, Easy, Language-Model, Under, Curriculum

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26844v1) | [下载PDF](https://arxiv.org/pdf/2604.26844v1.pdf)

---

## [5. HalluCiteChecker: A Lightweight Toolkit for Hallucinated Citation Detection and Verification in the Era of AI Scientists](https://arxiv.org/abs/2604.26835v1)

**作者**：Yusuke Sakai, Hidetaka Kamigaito, Taro Watanabe  
**分类**：cs.CL, cs.AI, cs.DL  
**发布时间**：2026-04-29

### 📄 论文摘要

We introduce HalluCiteChecker, a toolkit for detecting and verifying hallucinated citations in scientific papers. While AI assistant technologies have transformed the academic writing process, including citation recommendation, they have also led to the emergence of hallucinated citations that do not correspond to any existing work. Such citations not only undermine the credibility of scientific papers but also impose an additional burden on reviewers and authors, who must manually verify their validity during the review process. In this study, we formalize hallucinated citation detection as an NLP task and provide a corresponding toolkit as a practical foundation for addressing this problem. Our package is lightweight and can perform verification in seconds on a standard laptop. It can also be executed entirely offline and runs efficiently using only CPUs. We hope that HalluCiteChecker will help reduce reviewer workload and support organizers by enabling systematic pre-review and publication checks. Our code is released under the Apache 2.0 license on GitHub and is distributed as an installable package via PyPI. A demonstration video is available on YouTube.

### 🤖 AI 总结

**一句话总结**：We introduce HalluCiteChecker, a toolkit for detecting and verifying hallucinated citations in scientific papers. While AI assistant technologies have transformed the academic writing process, includi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HalluCiteChecker, Lightweight, Toolkit, Hallucinated, Citation, Detection, Verification, Era

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26835v1) | [下载PDF](https://arxiv.org/pdf/2604.26835v1.pdf)

---

## cs.CV

## [6. Three-Step Nav: A Hierarchical Global-Local Planner for Zero-Shot Vision-and-Language Navigation](https://arxiv.org/abs/2604.26946v1)

**作者**：Wanrong Zheng, Yunhao Ge, Laurent Itti  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-04-29

### 📄 论文摘要

Breakthrough progress in vision-based navigation through unknown environments has been achieved by using multimodal large language models (MLLMs). These models can plan a sequence of motions by evaluating the current view at each time step against the task and goal given to the agent. However, current zero-shot Vision-and-Language Navigation (VLN) agents powered by MLLMs still tend to drift off course, halt prematurely, and achieve low overall success rates. We propose Three-Step Nav to counteract these failures with a three-view protocol: First, "look forward" to extract global landmarks and sketch a coarse plan. Then, "look now" to align the current visual observation with the next sub-goal for fine-grained guidance. Finally, "look backward" audits the entire trajectory to correct accumulated drift before stopping. Requiring no gradient updates or task-specific fine-tuning, our planner drops into existing VLN pipelines with minimal overhead. Three-Step Nav achieves state-of-the-art zero-shot performance on the R2R-CE and RxR-CE dataset. Our code is available at https://github.com/ZoeyZheng0/3-step-Nav.

### 🤖 AI 总结

**一句话总结**：Breakthrough progress in vision-based navigation through unknown environments has been achieved by using multimodal large language models (MLLMs). These models can plan a sequence of motions by evalua...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Three-Step, Nav, Hierarchical, Global-Local, Planner, Zero-Shot, Vision-and-Language, Navigation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26946v1) | [下载PDF](https://arxiv.org/pdf/2604.26946v1.pdf)

---

## [7. ProcFunc: Function-Oriented Abstractions for Procedural 3D Generation in Python](https://arxiv.org/abs/2604.26943v1)

**作者**：Alexander Raistrick, Karhan Kayan, Jack Nugent 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-29

### 📄 论文摘要

We introduce ProcFunc, a library for Blender-based procedural 3D generation in Python. ProcFunc provides a library of easy-to-use Python functions, which streamline creating, combining, analyzing, and executing procedural generation code. ProcFunc makes it easy to create large-scale diverse training data, by combinatorial compositions of semantic components. VLMs can use ProcFunc to edit procedural material and geometry code and can create new procedural code with significantly fewer coding errors. Finally, as an example use case, we use ProcFunc to develop a new procedural generator of indoor rooms, which includes a collection of new compositional procedural materials. We demonstrate the detail, runtime efficiency, and diversity of this room generator, as well as its use for 3D synthetic data generation. Please visit https://github.com/princeton-vl/procfunc for source code.

### 🤖 AI 总结

**一句话总结**：We introduce ProcFunc, a library for Blender-based procedural 3D generation in Python. ProcFunc provides a library of easy-to-use Python functions, which streamline creating, combining, analyzing, and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, We, ProcFunc, Function-Oriented, Abstractions, Procedural, Generation, Python

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26943v1) | [下载PDF](https://arxiv.org/pdf/2604.26943v1.pdf)

---

## [8. World2VLM: Distilling World Model Imagination into VLMs for Dynamic Spatial Reasoning](https://arxiv.org/abs/2604.26934v1)

**作者**：Wanyue Zhang, Wenxiang Wu, Wang Xu 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-29

### 📄 论文摘要

Vision-language models (VLMs) have shown strong performance on static visual understanding, yet they still struggle with dynamic spatial reasoning that requires imagining how scenes evolve under egocentric motion. Recent efforts address this limitation either by scaling spatial supervision with synthetic data or by coupling VLMs with world models at inference time. However, the former often lacks explicit modeling of motion-conditioned state transitions, while the latter incurs substantial computational overhead. In this work, we propose World2VLM, a training framework that distills spatial imagination from a generative world model into a vision-language model. Given an initial observation and a parameterized camera trajectory, we use a view-consistent world model to synthesize geometrically aligned future views and derive structured supervision for both forward (action-to-outcome) and inverse (outcome-to-action) spatial reasoning. We post-train the VLM with a two-stage recipe on a compact dataset generated by this pipeline and evaluate it on multiple spatial reasoning benchmarks. World2VLM delivers consistent improvements over the base model across diverse benchmarks, including SAT-Real, SAT-Synthesized, VSI-Bench, and MindCube. It also outperforms the test-time world-model-coupled methods while eliminating the need for expensive inference-time generation. Our results suggest that world models can serve not only as inference-time tools, but also as effective training-time teachers, enabling VLMs to internalize spatial imagination in a scalable and efficient manner.

### 🤖 AI 总结

**一句话总结**：Vision-language models (VLMs) have shown strong performance on static visual understanding, yet they still struggle with dynamic spatial reasoning that requires imagining how scenes evolve under egoce...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：World2VLM, Distilling, World, Model, Imagination, VLMs, Dynamic, Spatial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26934v1) | [下载PDF](https://arxiv.org/pdf/2604.26934v1.pdf)

---

## [9. AnimateAnyMesh++: A Flexible 4D Foundation Model for High-Fidelity Text-Driven Mesh Animation](https://arxiv.org/abs/2604.26917v1)

**作者**：Zijie Wu, Chaohui Yu, Fan Wang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-29

### 📄 论文摘要

Recent advances in 4D content generation have attracted increasing attention, yet creating high-quality animated 3D models remains challenging due to the complexity of modeling spatio-temporal distributions and the scarcity of 4D training data. We present AnimateAnyMesh++, a feed-forward framework for text-driven animation of arbitrary 3D meshes with substantial upgrades in data, architecture, and generative capability. First, we expand the DyMesh-XL dataset by mining dynamic content from Objaverse-XL, increasing the number of unique identities from 60K to 300K and substantially broadening category and motion diversity. Second, we redesign DyMeshVAE-Flex with power-law topology-aware attention and vertex-normal enhanced features, which significantly improves trajectory reconstruction, local geometry preservation, and mitigates trajectory-sticking artifacts. Third, we introduce architectural changes to both DyMeshVAE-Flex and the rectified-flow (RF) generator to support variable-length sequence training and generation, enabling longer animations while preserving reconstruction fidelity. Extensive experiments demonstrate that AnimateAnyMesh++ generates semantically accurate and temporally coherent mesh animations within seconds, surpassing prior approaches in quality and efficiency. The enlarged DyMesh-XL, the upgraded DyMeshVAE-Flex, and variable-length RF together deliver consistent gains across benchmarks and in-the-wild meshes. We will release code, models, and the expanded DyMesh-XL upon acceptance of this manuscript to facilitate research in 4D content creation.

### 🤖 AI 总结

**一句话总结**：Recent advances in 4D content generation have attracted increasing attention, yet creating high-quality animated 3D models remains challenging due to the complexity of modeling spatio-temporal distrib...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, AnimateAnyMesh++, Flexible, Foundation, Model, High-Fidelity, Text-Driven, Mesh

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26917v1) | [下载PDF](https://arxiv.org/pdf/2604.26917v1.pdf)

---

## [10. Graph-based Semantic Calibration Network for Unaligned UAV RGBT Image Semantic Segmentation and A Large-scale Benchmark](https://arxiv.org/abs/2604.26893v1)

**作者**：Fangqiang Fan, Zhicheng Zhao, Xiaoliang Ma 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-29

### 📄 论文摘要

Fine-grained RGBT image semantic segmentation is crucial for all-weather unmanned aerial vehicle (UAV) scene understanding. However, UAV RGBT semantic segmentation faces two coupled challenges: cross-modal spatial misalignment caused by sensor parallax and platform vibration, and severe semantic confusion among fine-grained ground objects under top-down aerial views. To address these issues, we propose a Graph-based Semantic Calibration Network (GSCNet) for unaligned UAV RGBT image semantic segmentation. Specifically, we design a Feature Decoupling and Alignment Module (FDAM) that decouples each modality into shared structural and private perceptual components and performs deformable alignment in the shared subspace, enabling robust spatial correction with reduced modality appearance interference. Moreover, we propose a Semantic Graph Calibration Module (SGCM) that explicitly encodes the hierarchical taxonomy and co-occurrence regularities among ground-object categories in UAV scenes into a structured category graph, and incorporates these priors into graph-attention reasoning to calibrate predictions of visually similar and rare categories.In addition, we construct the Unaligned RGB-Thermal Fine-grained (URTF) benchmark, to the best of our knowledge, the largest and most fine-grained benchmark for unaligned UAV RGBT image semantic segmentation, containing over 25,000 image pairs across 61 categories with realistic cross-modal misalignment. Extensive experiments on URTF demonstrate that GSCNet significantly outperforms state-of-the-art methods, with notable gains on fine-grained categories. The dataset is available at https://github.com/mmic-lcl/Datasets-and-benchmark-code.

### 🤖 AI 总结

**一句话总结**：Fine-grained RGBT image semantic segmentation is crucial for all-weather unmanned aerial vehicle (UAV) scene understanding. However, UAV RGBT semantic segmentation faces two coupled challenges: cross-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Graph-based, Semantic, Calibration, Network, Unaligned, UAV, RGBT, Image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26893v1) | [下载PDF](https://arxiv.org/pdf/2604.26893v1.pdf)

---

## [11. Uncertainty-Aware Pedestrian Attribute Recognition via Evidential Deep Learning](https://arxiv.org/abs/2604.26873v1)

**作者**：Zhuofan Lou, Shihang Zhang, Fangle Zhu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-29

### 📄 论文摘要

We propose UAPAR, an Uncertainty-Aware Pedestrian Attribute Recognition framework. To the best of our knowledge, this is the first EDL-based uncertainty-aware framework for pedestrian attribute recognition (PAR). Unlike conventional deterministic methods, which fail to assess prediction reliability on low-quality samples, UAPAR effectively identifies unreliable predictions and thus enhances system robustness in complex real-world scenarios. To achieve this, UAPAR incorporates Evidential Deep Learning (EDL) into a CLIP-based architecture. Specifically, a Region-Aware Evidence Reasoning module employs cross-attention and spatial prior masks to capture fine-grained local features, which are further processed by an evidence head to estimate attribute-wise epistemic uncertainty. To further enhance training robustness, we develop an uncertainty-guided dual-stage curriculum learning strategy to alleviate the adverse effects of severe label noise during training. Extensive experiments on the PA100K, PETA, RAPv1, and RAPv2 datasets demonstrate that UAPAR achieves competitive or superior performance. Furthermore, qualitative results confirm that the proposed framework generates uncertainty estimates that are predictive of challenging or erroneous samples.

### 🤖 AI 总结

**一句话总结**：We propose UAPAR, an Uncertainty-Aware Pedestrian Attribute Recognition framework. To the best of our knowledge, this is the first EDL-based uncertainty-aware framework for pedestrian attribute recogn...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Uncertainty-Aware, Pedestrian, Attribute, Recognition, via, Evidential, Deep, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26873v1) | [下载PDF](https://arxiv.org/pdf/2604.26873v1.pdf)

---

## [12. Breaking the Rigid Prior: Towards Articulated 3D Anomaly Detection](https://arxiv.org/abs/2604.26868v1)

**作者**：Jinye Gan, Bozhong Zheng, Xiaohao Xu 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-29

### 📄 论文摘要

Existing 3D anomaly detection methods are built on a rigid prior: normal geometry is pose-invariant and can be canonicalized through registration or alignment. This prior does not hold for articulated objects with hinge or sliding joints, where valid pose changes induce structured geometric variations that cannot be collapsed to a single canonical template, causing pose-induced deformations to be misidentified as anomalies while true structural defects are obscured. No existing benchmark addresses this challenge. We introduce ArtiAD, the first large-scale benchmark for articulated 3D anomaly detection, comprising 15,229 point clouds across 39 object categories with dense joint-angle variations and six structural anomaly types. Each sample is annotated with its joint configuration and part-level motion labels, enabling explicit disentanglement of pose-induced geometry from structural defects. ArtiAD also provides a seen/unseen articulation split to evaluate both interpolation and extrapolation to novel joint configurations. We propose Shape-Pose-Aware Signed Distance Field (SPA-SDF), a baseline that replaces the rigid prior with a continuous pose-conditioned implicit field, factorized into an articulation-independent structural prior and a Fourier-encoded joint embedding. At inference, the articulation state is recovered by minimizing reconstruction energy, and anomalies are identified as point-wise deviations from the learned manifold. SPA-SDF achieves 0.884 object-level AUROC on seen configurations and 0.874 on unseen configurations, substantially outperforming all rigid-based baselines. Our code and benchmark will be publicly released to facilitate future research.

### 🤖 AI 总结

**一句话总结**：Existing 3D anomaly detection methods are built on a rigid prior: normal geometry is pose-invariant and can be canonicalized through registration or alignment. This prior does not hold for articulated...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Breaking, Rigid, Prior, Towards, Articulated, Anomaly, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26868v1) | [下载PDF](https://arxiv.org/pdf/2604.26868v1.pdf)

---

## [13. Edge AI for Automotive Vulnerable Road User Safety: Deployable Detection via Knowledge Distillation](https://arxiv.org/abs/2604.26857v1)

**作者**：Akshay Karjol, Darrin M. Hanna  
**分类**：cs.CV, cs.LG, cs.RO, eess.IV  
**发布时间**：2026-04-29

### 📄 论文摘要

Deploying accurate object detection for Vulnerable Road User (VRU) safety on edge hardware requires balancing model capacity against computational constraints. Large models achieve high accuracy but fail under INT8 quantization required for edge deployment, while small models sacrifice detection performance. This paper presents a knowledge distillation (KD) framework that trains a compact YOLOv8-S student (11.2M parameters) to mimic a YOLOv8-L teacher (43.7M parameters), achieving 3.9x compression while preserving quantization robustness. We evaluate on full-scale BDD100K (70K training images) with Post-Training Quantization to INT8. The teacher suffers catastrophic degradation under INT8 (-23% mAP), while the KD student retains accuracy (-5.6% mAP). Analysis reveals that KD transfers precision calibration rather than raw detection capacity: the KD student achieves 0.748 precision versus 0.653 for direct training at INT8, a 14.5% gain at equivalent recall, reducing false alarms by 44% versus the collapsed teacher. At INT8, the KD student exceeds the teacher's FP32 precision (0.748 vs. 0.718) in a model 3.9x smaller. These findings establish knowledge distillation as a requirement for deploying accurate, safety-critical VRU detection on edge hardware.

### 🤖 AI 总结

**一句话总结**：Deploying accurate object detection for Vulnerable Road User (VRU) safety on edge hardware requires balancing model capacity against computational constraints. Large models achieve high accuracy but f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Edge, Automotive, Vulnerable, Road, User, Safety, Deployable, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26857v1) | [下载PDF](https://arxiv.org/pdf/2604.26857v1.pdf)

---

## [14. Bridge: Basis-Driven Causal Inference Marries VFMs for Domain Generalization](https://arxiv.org/abs/2604.26820v1)

**作者**：Mingbo Hong, Feng Liu, Caroline Gevaert 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-29

### 📄 论文摘要

Detectors often suffer from degraded performance, primarily due to the distributional gap between the source and target domains. This issue is especially evident in single-source domains with limited data, as models tend to rely on confounders (e.g., illumination, co-occurrence, and style) from the source domain, leading to spurious correlations that hinder generalization. To this end, this paper proposes a novel Basis-driven framework for domain generalization, namely \textbf{\textit{Bridge}}, that incorporates causal inference into object detection. By learning the low-rank bases for front-door adjustment, \textbf{\textit{Bridge}} blocks confounders' effects to mitigate spurious correlations, while simultaneously refining representations by filtering redundant and task-irrelevant components. \textbf{\textit{Bridge}} can be seamlessly integrated with both discriminative (e.g., DINOv2/3, SAM) and generative (e.g., Stable Diffusion) Vision Foundation Models (VFMs). Extensive experiments across multiple domain generalization object detection datasets, i.e., Cross-Camera, Adverse Weather, Real-to-Artistic, Diverse Weather Datasets, and Diverse Weather DroneVehicle (our newly augmented real-world UAV-based benchmark), underscore the superiority of our proposed method over previous state-of-the-art approaches. The project page is available at: https://mingbohong.github.io/Bridge/.

### 🤖 AI 总结

**一句话总结**：Detectors often suffer from degraded performance, primarily due to the distributional gap between the source and target domains. This issue is especially evident in single-source domains with limited ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bridge, Basis-Driven, Causal, Inference, Marries, VFMs, Domain, Generalization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26820v1) | [下载PDF](https://arxiv.org/pdf/2604.26820v1.pdf)

---

## [15. ViCrop-Det: Spatial Attention Entropy Guided Cropping for Training-Free Small-Object Detection](https://arxiv.org/abs/2604.26806v1)

**作者**：Hui Wang, Hongze Li, Wei Chen 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-29

### 📄 论文摘要

Transformer-based architectures have established a dominant paradigm in global semantic perception; however, they remain fundamentally constrained by the profound spatial heterogeneity inherent in natural images. Specifically, the imposition of a uniform global receptive field across regions of varying information density inevitably leads to local feature degradation, particularly in dense conflict zones populated by microscopic targets. To address this mechanistic limitation, we propose ViCrop-Det, a training-free inference framework that introduces adaptive spatial trust region shrinkage. Inspired by the use of attention entropy in anomaly segmentation, ViCrop-Det leverages the detection decoder's cross-attention distribution as an endogenous probe. By utilizing Spatial Attention Entropy (SAE) to heuristically evaluate local spatial ambiguity, the framework executes dynamic spatial routing, allocating a fixed computational budget exclusively to regions exhibiting both high target saliency and high cognitive uncertainty. By shrinking the spatial trust region and injecting high-frequency localized observations, ViCrop-Det actively resolves spatial ambiguity and recovers fine-grained features without requiring architectural modifications. Extensive evaluations on VisDrone and DOTA-v1.5 demonstrate that ViCrop-Det yields competitive performance enhancements, consistently adding +1-3 mAP@50 to RT-DETR-R50 and Deformable DETR with a marginal 20-23\% latency overhead. On MS COCO, $AP_{S}$ improves while $AP_{M}/AP_{L}$ remains stable, indicating precise fine-scale refinement without compromising the global spatial prior. Under compute-matched settings, our adaptive routing strategy comprehensively surpasses uniform slicing baselines, achieving a highly optimized accuracy-speed trade-off.

### 🤖 AI 总结

**一句话总结**：Transformer-based architectures have established a dominant paradigm in global semantic perception; however, they remain fundamentally constrained by the profound spatial heterogeneity inherent in nat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ViCrop-Det, Spatial, Attention, Entropy, Guided, Cropping, Training-Free, Small-Object

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26806v1) | [下载PDF](https://arxiv.org/pdf/2604.26806v1.pdf)

---

## [16. MesonGS++: Post-training Compression of 3D Gaussian Splatting with Hyperparameter Searching](https://arxiv.org/abs/2604.26799v1)

**作者**：Shuzhao Xie, Junchen Ge, Weixiang Zhang 等 13 位作者  
**分类**：cs.CV, cs.GR, cs.MM  
**发布时间**：2026-04-29

### 📄 论文摘要

3D Gaussian Splatting (3DGS) achieves high-quality novel view synthesis with real-time rendering, but its storage cost remains prohibitive for practical deployment. Existing post-training compression methods still rely on many coupled hyperparameters across pruning, transformation, quantization, and entropy coding, making it difficult to control the final compressed size and fully exploit the rate-distortion trade-off. We propose MesonGS++, a size-aware post-training codec for 3D Gaussian compression. On the codec side, MesonGS++ combines joint importance-based pruning, octree geometry coding, attribute transformation, selective vector quantization for higher-degree spherical harmonics, and group-wise mixed-precision quantization with entropy coding. On the configuration side, it treats the reserve ratio and bit-width allocation as the dominant rate-distortion knobs and jointly optimizes them under a target storage budget via discrete sampling and 0--1 integer linear programming. We further propose a linear size estimator and a CUDA parallel quantization operator to accelerate the hyperparameter searching process. Extensive experiments show that MesonGS++ achieves over 34$\times$ compression while preserving rendering fidelity, outperforming state-of-the-art post-training methods and accurately meeting target size budgets. Remarkably, without any training, MesonGS++ can even surpass the PSNR of vanilla 3DGS at a 20$\times$ compression rate on the Stump scene. Our code is available at https://github.com/mmlab-sigs/mesongs_plus

### 🤖 AI 总结

**一句话总结**：3D Gaussian Splatting (3DGS) achieves high-quality novel view synthesis with real-time rendering, but its storage cost remains prohibitive for practical deployment. Existing post-training compression ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, 3D, MesonGS++, Post-training, Compression, Gaussian, Splatting, Hyperparameter

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26799v1) | [下载PDF](https://arxiv.org/pdf/2604.26799v1.pdf)

---

## [17. Virtual-reality based patient-specific simulation of spine surgical procedures: A fast, highly automated and high-fidelity system for surgical education and planning](https://arxiv.org/abs/2604.26781v1)

**作者**：Raj Kumar Ranabhat, Tayler D Ross, Tony Jiao 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-29

### 📄 论文摘要

Surgical training involves didactic teaching, mentor-led learning, surgical skills laboratories, and direct exposure to surgery; however, increasing clinical pressures have limited operating room (OR) exposure. This work leverages virtual reality (VR) to provide a safe and immersive training environment. Existing VR training is often based on standardized scenarios not tailored to individual clinical cases. This study addresses this limitation using artificial intelligence (AI) based computer vision methods to generate patient-specific simulations from computed tomography (CT) and magnetic resonance imaging (MRI). This study focuses on patient-specific spinal decompression simulation for spinal stenosis in a virtual operating room. The objectives were (1) automatic creation of 3D anatomical models and (2) VR simulation of spinal decompression procedures including laminectomy, disc resection, and foraminotomy. Model construction required multimodal fusion (registration) of CT and MRI and segmentation of relevant structures. Segmentation was evaluated using the Dice Similarity Coefficient (DSC), and registration accuracy using Target Registration Error (TRE). Qualitative feedback was obtained from surgeons and trainees. High-fidelity patient-specific 3D models were generated efficiently (approximately 2.5 minutes per case, N = 15). Segmentation accuracy was high, with a DSC of 0.95 (+/- 0.03) for vertebral bone and 0.895 (+/- 0.02) for soft tissue structures. Registration accuracy showed a mean TRE of 1.73 (+/- 0.42) mm. Semi-structured interviews indicated improved spatial understanding, increased procedural confidence, and strong perceived educational value. This platform significantly reduced the time and costs of patient-specific modelling, thereby facilitating pre-operative planning, post-procedural assessments, and comprehensive surgical simulation.

### 🤖 AI 总结

**一句话总结**：Surgical training involves didactic teaching, mentor-led learning, surgical skills laboratories, and direct exposure to surgery; however, increasing clinical pressures have limited operating room (OR)...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Virtual-reality, patient-specific, simulation, spine, surgical, procedures, fast

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26781v1) | [下载PDF](https://arxiv.org/pdf/2604.26781v1.pdf)

---

## cs.LG

## [18. Hyper Input Convex Neural Networks for Shape Constrained Learning and Optimal Transport](https://arxiv.org/abs/2604.26942v1)

**作者**：Shayan Hundrieser, Insung Kong, Johannes Schmidt-Hieber  
**分类**：cs.LG, math.ST, q-bio.GN, stat.ME, stat.ML  
**发布时间**：2026-04-29

### 📄 论文摘要

We introduce Hyper Input Convex Neural Networks (HyCNNs), a novel neural network architecture designed for learning convex functions. HyCNNs combine the principles of Maxout networks with input convex neural networks (ICNNs) to create a neural network that is always convex in the input, theoretically capable of leveraging depth, and performs reliable when trained at scale compared to ICNNs. Concretely, we prove that HyCNNs require exponentially fewer parameters than ICNNs to approximate quadratic functions up to a given precision. Throughout a series of synthetic experiments, we demonstrate that HyCNNs outperform existing ICNNs and MLPs in terms of predictive performance for convex regression and interpolation tasks. We further apply HyCNNs to learn high-dimensional optimal transport maps for synthetic examples and for single-cell RNA sequencing data, where they oftentimes outperform ICNN-based neural optimal transport methods and other baselines across a wide range of settings.

### 🤖 AI 总结

**一句话总结**：We introduce Hyper Input Convex Neural Networks (HyCNNs), a novel neural network architecture designed for learning convex functions. HyCNNs combine the principles of Maxout networks with input convex...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hyper, Input, Convex, Neural, Networks, Shape, Constrained, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26942v1) | [下载PDF](https://arxiv.org/pdf/2604.26942v1.pdf)

---

## [19. Causal Learning with Neural Assemblies](https://arxiv.org/abs/2604.26919v1)

**作者**：Evangelia Kopadi, Dimitris Kalles  
**分类**：cs.LG, cs.AI, cs.NE  
**发布时间**：2026-04-29

### 📄 论文摘要

Can Neural Assemblies -- groups of neurons that fire together and strengthen through co-activation -- learn the direction of causal influence between variables? While established as a computationally general substrate for classification, parsing, and planning, neural assemblies have not yet been shown to internalize causal directionality. We demonstrate that the inherent operations of neural assemblies -- projection, local plasticity control, and sparse winner selection -- are sufficient for directional learning. We introduce DIRECT (DIRectional Edge Coupling/Training), a mechanism that co-activates source and target assemblies under an adaptive gain schedule to internalize directed relations. Unlike backpropagation-based methods, DIRECT relies solely on local plasticity, making the resulting causal claims auditable at the mechanism level. Our findings are verified through a dual-readout validation strategy: (i) synaptic-strength asymmetry, measuring the emergent weight gap between forward and reverse links, and (ii) functional propagation overlap, quantifying the reliability of directional signal flow. Across multiple domains, the framework achieves perfect structural recovery under a supervised, known-structure setting. These results establish neural assemblies as an auditable bridge between biologically plausible dynamics and formal causal models, offering an "explainable by design" framework where causal claims are traceable to specific neural winners and synaptic asymmetries.

### 🤖 AI 总结

**一句话总结**：Can Neural Assemblies -- groups of neurons that fire together and strengthen through co-activation -- learn the direction of causal influence between variables? While established as a computationally ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Causal, Learning, Neural, Assemblies, Can, groups, neurons

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26919v1) | [下载PDF](https://arxiv.org/pdf/2604.26919v1.pdf)

---

## [20. Multiple Additive Neural Networks for Structured and Unstructured Data](https://arxiv.org/abs/2604.26888v1)

**作者**：Janis Mohr, Jörg Frochte  
**分类**：cs.LG  
**发布时间**：2026-04-29

### 📄 论文摘要

This paper extends and explains the Multiple Additive Neural Networks (MANN) methodology, an enhancement to the traditional Gradient Boosting framework, utilizing nearly shallow neural networks instead of decision trees as base learners. This innovative approach leverages neural network architectures, notably Convolutional Neural Networks (CNNs) and Capsule Neural Networks, to extend its application to both structured data and unstructured data such as images and audio. For structured data the advantages of capsule neural networks as feature extractors are used and combined with MANN as a classifier. MANN's unique architecture promotes continuous learning and integrates advanced heuristics to combat overfitting, ensuring robustness and reducing sensitivity to hyperparameter settings like learning rate and iterations. Our empirical studies reveal that MANN surpasses traditional methods such as Extreme Gradient Boosting (XGB) in accuracy across well-known datasets. This research demonstrates MANN's superior precision and generalizability, making it a versatile tool for diverse data types and complex learning environments.

### 🤖 AI 总结

**一句话总结**：This paper extends and explains the Multiple Additive Neural Networks (MANN) methodology, an enhancement to the traditional Gradient Boosting framework, utilizing nearly shallow neural networks instea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multiple, Additive, Neural, Networks, Structured, Unstructured, Data, paper

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26888v1) | [下载PDF](https://arxiv.org/pdf/2604.26888v1.pdf)

---

## [21. KAYRA: A Microservice Architecture for AI-Assisted Karyotyping with Cloud and On-Premise Deployment](https://arxiv.org/abs/2604.26869v1)

**作者**：Attila Pintér, Javier Rico, Attila Répai 等 8 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-04-29

### 📄 论文摘要

We present KAYRA, an end-to-end karyotyping system that operates inside the operational constraints of a clinical cytogenetic laboratory. KAYRA is architected as a containerized microservice pipeline whose ML stack combines an EfficientNet-B5 + U-Net semantic segmenter, a Mask R-CNN (ResNet-50 + FPN) instance detector, and a ResNet-18 classifier, orchestrated through a cascaded ROI-narrowing strategy that focuses each downstream model on the chromosome-bearing region. The same container images are deployed both as a cloud service and as an on-premise installation, supporting clinical environments where patient-data egress is not permitted as well as those where it is. A pilot clinical evaluation against two commercial reference karyotyping systems on 459 chromosomes from 10 metaphase spreads shows segmentation accuracy of 98.91 % (vs. 78.21 % / 40.52 %), classification accuracy of 89.1 % (vs. 86.9 % / 54.5 %), and rotation accuracy of 89.76 % (vs. 94.55 % / 78.43 %). KAYRA improves over the older density-thresholding reference on all three axes (p < 0.0001 for segmentation and classification by Fisher's exact test on chromosome-level counts), and on segmentation also against the modern AI- supported reference (p < 0.0001); on classification the difference vs. the modern AI reference is not statistically significant at the present test-set size (p = 0.34). The system reaches TRL 6 maturity and integrates the human-in-the-loop expert-review workflow that diagnostic cytogenetic practice requires. The thesis of this paper is that a multi-model cytogenetic AI service can be packaged as a microservice architecture supporting flexible deployment - cloud-hosted or on-premise - while delivering strong empirical performance on a pilot clinical evaluation.

### 🤖 AI 总结

**一句话总结**：We present KAYRA, an end-to-end karyotyping system that operates inside the operational constraints of a clinical cytogenetic laboratory. KAYRA is architected as a containerized microservice pipeline ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：KAYRA, Microservice, Architecture, AI-Assisted, Karyotyping, Cloud, On-Premise, Deployment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26869v1) | [下载PDF](https://arxiv.org/pdf/2604.26869v1.pdf)

---

## [22. Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving](https://arxiv.org/abs/2604.26837v1)

**作者**：Zihan Zhao, Baotong Lu, Shengjie Lin 等 11 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-29

### 📄 论文摘要

Long-context LLM serving is bottlenecked by the cost of attending over ever-growing KV caches. Dynamic sparse attention promises relief by accessing only a small, query-dependent subset of the KV state per decoding step and extending the KV storage to CPU memory. In practice, however, these algorithmic savings rarely translate into end-to-end system-level gains because sparse methods typically operate at different granularities and thus rely on ad hoc, per-algorithm implementations. At the same time, hierarchical KV storage introduces a new systems bottleneck: retrieving fine-grained, irregular KV subsets across the GPU-CPU boundary can easily erase the benefits of sparsity.   We present SPIN, a sparse-attention-aware inference framework that co-designs the execution pipeline with hierarchical KV storage through three techniques: (1) a unified partition abstraction that maps different sparsity granularities onto a shared page-based KV substrate; (2) a locality-aware KV cache manager that dynamically sizes per-request HBM budgets and uses a GPU-friendly bucketed LRU policy to cut PCIe round-trips; and (3) a two-level hierarchical metadata layout sized to the active working set rather than the worst-case address space. Built on vLLM with three representative sparse attention algorithms, SPIN delivers 1.66-5.66x higher end-to-end throughput and 7-9x lower TTFT than vLLM, and reduces TPOT by up to 58% over the original sparse-attention implementations.

### 🤖 AI 总结

**一句话总结**：Long-context LLM serving is bottlenecked by the cost of attending over ever-growing KV caches. Dynamic sparse attention promises relief by accessing only a small, query-dependent subset of the KV stat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Unifying, Sparse, Attention, Hierarchical, Memory, Scalable, Long-Context

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26837v1) | [下载PDF](https://arxiv.org/pdf/2604.26837v1.pdf)

---

## [23. Uncertainty-Aware Predictive Safety Filters for Probabilistic Neural Network Dynamics](https://arxiv.org/abs/2604.26836v1)

**作者**：Bernd Frauenknecht, Lukas Kesper, Daniel Mayfrank 等 5 位作者  
**分类**：cs.LG, eess.SY  
**发布时间**：2026-04-29

### 📄 论文摘要

Predictive safety filters (PSFs) leverage model predictive control to enforce constraint satisfaction during deep reinforcement learning (RL) exploration, yet their reliance on first-principles models or Gaussian processes limits scalability and broader applicability. Meanwhile, model-based RL (MBRL) methods routinely employ probabilistic ensemble (PE) neural networks to capture complex, high-dimensional dynamics from data with minimal prior knowledge. However, existing attempts to integrate PEs into PSFs lack rigorous uncertainty quantification. We introduce the Uncertainty-Aware Predictive Safety Filter (UPSi), a PSF that provides rigorous safety predictions using PE dynamics models by formulating future outcomes as reachable sets. UPSi introduces an explicit certainty constraint that prevents model exploitation and integrates seamlessly into common MBRL frameworks. We evaluate UPSi within Dyna-style MBRL on standard safe RL benchmarks and report substantial improvements in exploration safety over prior neural network PSFs while maintaining performance on par with standard MBRL. UPSi bridges the gap between the scalability and generality of modern MBRL and the safety guarantees of predictive safety filters.

### 🤖 AI 总结

**一句话总结**：Predictive safety filters (PSFs) leverage model predictive control to enforce constraint satisfaction during deep reinforcement learning (RL) exploration, yet their reliance on first-principles models...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Uncertainty-Aware, Predictive, Safety, Filters, Probabilistic, Neural, Network, Dynamics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26836v1) | [下载PDF](https://arxiv.org/pdf/2604.26836v1.pdf)

---

## [24. Random Cloud: Finding Minimal Neural Architectures Without Training](https://arxiv.org/abs/2604.26830v1)

**作者**：Javier Gil Blázquez  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-29

### 📄 论文摘要

I propose the \emph{Random Cloud} method, a training-free approach to neural architecture search that discovers minimal feedforward network topologies through stochastic exploration and progressive structural reduction. Unlike post-training pruning methods that require a full train-prune-retrain cycle, this method evaluates randomly initialized networks without backpropagation, progressively reduces their topology, and only trains the best minimal candidate at the end. I evaluate on 7 classification benchmarks against magnitude pruning and random pruning baselines. The Random Cloud matches or outperforms both baselines in 6 of 7 datasets, achieving statistically significant improvements on Sonar ($+4.9$pp accuracy, $p{=}0.017$ vs magnitude pruning) with 87\% parameter reduction. Crucially, the method is faster than both pruning baselines in 4 of 5 datasets (0.67--0.94$\times$ the cost of full training), since it avoids training the full-size network entirely.

### 🤖 AI 总结

**一句话总结**：I propose the \emph{Random Cloud} method, a training-free approach to neural architecture search that discovers minimal feedforward network topologies through stochastic exploration and progressive st...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Random, Cloud, Finding, Minimal, Neural, Architectures, Without, Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26830v1) | [下载PDF](https://arxiv.org/pdf/2604.26830v1.pdf)

---

## [25. Semi-supervised learning with max-margin graph cuts](https://arxiv.org/abs/2604.26818v1)

**作者**：Branislav Kveton, Michal Valko, Ali Rahimi 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-29

### 📄 论文摘要

This paper proposes a novel algorithm for semisupervised learning. This algorithm learns graph cuts that maximize the margin with respect to the labels induced by the harmonic function solution. We motivate the approach, compare it to existing work, and prove a bound on its generalization error. The quality of our solutions is evaluated on a synthetic problem and three UCI ML repository datasets. In most cases, we outperform manifold regularization of support vector machines, which is a state-of-the-art approach to semi-supervised max-margin learning.

### 🤖 AI 总结

**一句话总结**：This paper proposes a novel algorithm for semisupervised learning. This algorithm learns graph cuts that maximize the margin with respect to the labels induced by the harmonic function solution. We mo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Semi-supervised, learning, max-margin, graph, cuts, paper, proposes, novel

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26818v1) | [下载PDF](https://arxiv.org/pdf/2604.26818v1.pdf)

---

## [26. Asynchronous Federated Unlearning with Invariance Calibration for Medical Imaging](https://arxiv.org/abs/2604.26809v1)

**作者**：Zhaoyuan Cai, Xinglin Zhang  
**分类**：cs.LG  
**发布时间**：2026-04-29

### 📄 论文摘要

Federated Unlearning (FU) is an emerging paradigm in Federated Learning (FL) that enables participating clients to fully remove their contributions from a trained global model, driven by data protection regulations that mandate the right to be forgotten. However, existing FU methods mostly rely on synchronous coordination. This requirement forces the entire federation to halt and wait for stragglers to complete erasure, creating significant delays due to device heterogeneity. Furthermore, these methods often face the problem that the influence of erased data is merely suppressed temporarily and resurfaces during subsequent training, rather than being genuinely removed. To overcome these limitations, this paper proposes Asynchronous Federated Unlearning with Invariance Calibration (AFU-IC), a novel framework for medical imaging that decouples the erasure process from the global training workflow. This enables the target client to perform unlearning asynchronously without interrupting global training. Meanwhile, a server-side invariance calibration mechanism prevents the model from relearning the erased data. Extensive experiments on three medical benchmarks demonstrate that AFU-IC achieves unlearning efficacy and model fidelity comparable to gold-standard retraining while significantly reducing wall-clock latency compared to synchronous baselines. AFU-IC ensures efficient, compliant and reliable FL in cross-silo medical environments.

### 🤖 AI 总结

**一句话总结**：Federated Unlearning (FU) is an emerging paradigm in Federated Learning (FL) that enables participating clients to fully remove their contributions from a trained global model, driven by data protecti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FU, Asynchronous, Federated, Unlearning, Invariance, Calibration, Medical, Imaging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26809v1) | [下载PDF](https://arxiv.org/pdf/2604.26809v1.pdf)

---

## [27. A Multi-Dataset Benchmark of Multiple Instance Learning for 3D Neuroimage Classification](https://arxiv.org/abs/2604.26807v1)

**作者**：Ethan Harvey, Dennis Johan Loevlie, Amir Ali Satani 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-29

### 📄 论文摘要

Despite being resource-intensive to train, 3D convolutional neural networks (CNNs) have been the standard approach to classify CT and MRI scans. Recent work suggests that deep multiple instance learning (MIL) may be a more efficient alternative for 3D brain scans, especially when the pre-trained image encoder used to embed each 2D slice is frozen and only the pooling operation and classifier are trained. In this paper, we provide a systematic comparison of simple MIL, attention-based MIL, 3D CNNs, and 3D ViTs across three CT and four MRI datasets, including two large datasets of at least 10,000 scans. Our goal is to help resource-constrained practitioners understand which neural networks work well for 3D neuroimages and why. We further compare design choices for attention-based MIL, including different encoders, pooling operations, and architectural orderings. We find that simple mean pooling MIL, without any learnable attention, matches or outperforms recent MIL or 3D CNN alternatives on 4 of 6 moderate-sized tasks. This baseline remains competitive on two large datasets while being 25x faster to train. To explain mean pooling's success, we examine per-slice attention quality and a semi-synthetic dataset where we can derive the best possible classifier via a Bayes estimator. This analysis reveals the limits of existing MIL approaches and suggests routes for future improvements.

### 🤖 AI 总结

**一句话总结**：Despite being resource-intensive to train, 3D convolutional neural networks (CNNs) have been the standard approach to classify CT and MRI scans. Recent work suggests that deep multiple instance learni...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, 3D, Multi-Dataset, Benchmark, Multiple, Instance, Learning, Neuroimage

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26807v1) | [下载PDF](https://arxiv.org/pdf/2604.26807v1.pdf)

---

## [28. Super-resolution Multi-signal Direction-of-Arrival Estimation by Hankel-structured Sensing and Decomposition](https://arxiv.org/abs/2604.26793v1)

**作者**：Georgios I. Orfanidis, Dimitris A. Pados, George Sklivanitis 等 4 位作者  
**分类**：cs.LG, eess.SP  
**发布时间**：2026-04-29

### 📄 论文摘要

Motivated by sensing modalities in modern autonomous systems that involve hardware-constrained spatial sampling over large arrays with limited coherence time, we develop a novel framework for rapid super-resolution multi-signal direction-of-arrival (DoA) estimation based on Hankel-structured sensing and data matrix decomposition of arbitrary rank, under both the $L_2$ and $L_1$-norm formulation. The resulting $L_2$-norm estimator is shown to be maximum-likelihood optimal in white Gaussian noise. The $L_1$-norm estimator is shown to be maximum-likelihood optimal in independent, identically distributed (i.i.d.) isotropic Laplace noise, offering broad robustness to impulsive interference and corrupted measurements commonly encountered in practice. Extensive simulations demonstrate that the proposed methods exhibit powerful super-resolution capabilities, requiring significantly lower SNR and achieving substantially higher resolution probability than recent competing approaches.

### 🤖 AI 总结

**一句话总结**：Motivated by sensing modalities in modern autonomous systems that involve hardware-constrained spatial sampling over large arrays with limited coherence time, we develop a novel framework for rapid su...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Super-resolution, Multi-signal, Direction-of-Arrival, Estimation, Hankel-structured, Sensing, Decomposition, Motivated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26793v1) | [下载PDF](https://arxiv.org/pdf/2604.26793v1.pdf)

---

## [29. Hankel and Toeplitz Rank-1 Decomposition of Arbitrary Matrices with Applications to Signal Direction-of-Arrival Estimation](https://arxiv.org/abs/2604.26787v1)

**作者**：Georgios I. Orfanidis, Dimitris A. Pados, George Sklivanitis 等 4 位作者  
**分类**：cs.LG, eess.SP  
**发布时间**：2026-04-29

### 📄 论文摘要

We consider the problems of computing the optimal rank-$1$ Hankel and Toeplitz-structured approximation of arbitrary matrices under $L_2$ and $L_1$-norm error. Such problems arise naturally in engineered systems, including the basic few-shot signal Direction-of-Arrival (DoA) estimation problem that is of importance to modern autonomous systems applications. We develop accurate and computationally efficient structured matrix decomposition algorithms for both formulations and then derive analytically grounded small-sample-support DoA estimators for practical sensing system deployments. The resulting estimators under the $L_2$ and $L_1$ norms are formally shown to be maximum-likelihood optimal under white Gaussian and Laplace noise, respectively. The estimators are further validated through extensive simulation studies and real-world data experiments in few-shot DoA inference.

### 🤖 AI 总结

**一句话总结**：We consider the problems of computing the optimal rank-$1$ Hankel and Toeplitz-structured approximation of arbitrary matrices under $L_2$ and $L_1$-norm error. Such problems arise naturally in enginee...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Hankel, Toeplitz, Rank-1, Decomposition, Arbitrary, Matrices, Applications

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26787v1) | [下载PDF](https://arxiv.org/pdf/2604.26787v1.pdf)

---

## [30. Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding](https://arxiv.org/abs/2604.26779v1)

**作者**：Hayate Iso, Tiyasa Mitra, Sudipta Mondal 等 18 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-04-29

### 📄 论文摘要

RL post-training of frontier language models is increasingly bottlenecked by autoregressive rollout generation, making rollout acceleration a central systems challenge. Many existing efficiency methods improve throughput by changing the rollout or optimization regime, for example, through off-policy execution, replay, or lower-precision generation. We study speculative decoding as a lossless acceleration primitive for RL rollouts that preserves the target model's output distribution. We implement speculative decoding in NeMo-RL with a vLLM backend, supporting both synchronous and asynchronous pipelines and enabling speculation during RL rollouts. This benefit is realizable across speculation mechanisms, such as pretrained MTP heads, small external draft models or even techniques such as Eagle3, which are traditionally applied after RL phase. This yields a deployment path for state-of-the-art speculative decoding inside RL training. In a reasoning post-training workload at 8B scale under synchronous RL, speculative decoding improves rollout throughput by 1.8x. Using a high-fidelity performance simulator, we project that combining speculative decoding with asynchronous RL yields up to 2.5x end-to-end training speedup at 235B scale.

### 🤖 AI 总结

**一句话总结**：RL post-training of frontier language models is increasingly bottlenecked by autoregressive rollout generation, making rollout acceleration a central systems challenge. Many existing efficiency method...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Accelerating, Post-Training, Rollouts, via, System-Integrated, Speculative, Decoding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.26779v1) | [下载PDF](https://arxiv.org/pdf/2604.26779v1.pdf)

---

