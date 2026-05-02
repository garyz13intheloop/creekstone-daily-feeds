# arXiv AI 论文日报 | 2026-05-02

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (14 篇)
- [cs.LG](#csLG) (9 篇)
- [cs.AI](#csAI) (7 篇)

---

## cs.AI

## [1. Synthetic Computers at Scale for Long-Horizon Productivity Simulation](https://arxiv.org/abs/2604.28181v1)

**作者**：Tao Ge, Baolin Peng, Hao Cheng 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-04-30

### 📄 论文摘要

Realistic long-horizon productivity work is strongly conditioned on user-specific computer environments, where much of the work context is stored and organized through directory structures and content-rich artifacts. To scale synthetic data creation for such productivity scenarios, we introduce Synthetic Computers at Scale, a scalable methodology for creating such environments with realistic folder hierarchies and content-rich artifacts (e.g., documents, spreadsheets, and presentations). Conditioned on each synthetic computer, we run long-horizon simulations: one agent creates productivity objectives that are specific to the computer's user and require multiple professional deliverables and about a month of human work; another agent then acts as that user and keeps working across the computer -- for example, navigating the filesystem for grounding, coordinating with simulated collaborators, and producing professional artifacts -- until these objectives are completed.   In preliminary experiments, we create 1,000 synthetic computers and run long-horizon simulations on them; each run requires over 8 hours of agent runtime and spans more than 2,000 turns on average. These simulations produce rich experiential learning signals, whose effectiveness is validated by significant improvements in agent performance on both in-domain and out-of-domain productivity evaluations. Given that personas are abundant at billion scale, this methodology can in principle scale to millions or even billions of synthetic user worlds with sufficient compute, enabling broader coverage of diverse professions, roles, contexts, environments, and productivity needs. We argue that scalable synthetic computer creation, together with at-scale simulations, is highly promising as a foundational substrate for agent self-improvement and agentic reinforcement learning in long-horizon productivity scenarios.

### 🤖 AI 总结

**一句话总结**：Realistic long-horizon productivity work is strongly conditioned on user-specific computer environments, where much of the work context is stored and organized through directory structures and content...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Synthetic, Computers, Scale, Long-Horizon, Productivity, Simulation, Realistic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28181v1) | [下载PDF](https://arxiv.org/pdf/2604.28181v1.pdf)

---

## [2. LLM as Clinical Graph Structure Refiner: Enhancing Representation Learning in EEG Seizure Diagnosis](https://arxiv.org/abs/2604.28178v1)

**作者**：Lincan Li, Zheng Chen, Yushun Dong  
**分类**：cs.AI  
**发布时间**：2026-04-30

### 📄 论文摘要

Electroencephalogram (EEG) signals are vital for automated seizure detection, but their inherent noise makes robust representation learning challenging. Existing graph construction methods, whether correlation-based or learning-based, often generate redundant or irrelevant edges due to the noisy nature of EEG data. This significantly impairs the quality of graph representation and limits downstream task performance. Motivated by the remarkable reasoning and contextual understanding capabilities of large language models (LLMs), we explore the idea of using LLMs as graph edge refiners. Specifically, we propose a two-stage framework: we first verify that LLM-based edge refinement can effectively identify and remove redundant connections, leading to significant improvements in seizure detection accuracy and more meaningful graph structures. Building on this insight, we further develop a robust solution where the initial graph is constructed using a Transformer-based edge predictor and multilayer perceptron, assigning probability scores to potential edges and applying a threshold to determine their existence. The LLM then acts as an edge set refiner, making informed decisions based on both textual and statistical features of node pairs to validate the remaining connections. Extensive experiments on TUSZ dataset demonstrate that our LLM-refined graph learning framework not only enhances task performance but also yields cleaner and more interpretable graph representations.

### 🤖 AI 总结

**一句话总结**：Electroencephalogram (EEG) signals are vital for automated seizure detection, but their inherent noise makes robust representation learning challenging. Existing graph construction methods, whether co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, as, Clinical, Graph, Structure, Refiner, Enhancing, Representation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28178v1) | [下载PDF](https://arxiv.org/pdf/2604.28178v1.pdf)

---

## [3. Intern-Atlas: A Methodological Evolution Graph as Research Infrastructure for AI Scientists](https://arxiv.org/abs/2604.28158v1)

**作者**：Yujun Wu, Dongxu Zhang, Xinchen Li 等 13 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-30

### 📄 论文摘要

Existing research infrastructure is fundamentally document-centric, providing citation links between papers but lacking explicit representations of methodological evolution. In particular, it does not capture the structured relationships that explain how and why research methods emerge, adapt, and build upon one another. With the rise of AI-driven research agents as a new class of consumers of scientific knowledge, this limitation becomes increasingly consequential, as such agents cannot reliably reconstruct method evolution topologies from unstructured text. We introduce Intern-Atlas, a methodological evolution graph that automatically identifies method-level entities, infers lineage relationships among methodologies, and captures the bottlenecks that drive transitions between successive innovations. Built from 1,030,314 papers spanning AI conferences, journals, and arXiv preprints, the resulting graph comprises 9,410,201 semantically typed edges, each grounded in verbatim source evidence, forming a queryable causal network of methodological development. To operationalize this structure, we further propose a self-guided temporal tree search algorithm for constructing evolution chains that trace the progression of methods over time. We evaluate the quality of the resulting graph against expert-curated ground-truth evolution chains and observe strong alignment. In addition, we demonstrate that Intern-Atlas enables downstream applications in idea evaluation and automated idea generation. We position methodological evolution graphs as a foundational data layer for the emerging automated scientific discovery.

### 🤖 AI 总结

**一句话总结**：Existing research infrastructure is fundamentally document-centric, providing citation links between papers but lacking explicit representations of methodological evolution. In particular, it does not...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Intern-Atlas, Methodological, Evolution, Graph, Research, Infrastructure, Scientists

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28158v1) | [下载PDF](https://arxiv.org/pdf/2604.28158v1.pdf)

---

## [4. Normativity and Productivism: Ableist Intelligence? A Degrowth Analysis of AI Sign Language Translation Tools for Deaf People](https://arxiv.org/abs/2604.28125v1)

**作者**：Nina Seron-Abouelfadil, Poppy Fynes  
**分类**：cs.AI, cs.CY, cs.HC  
**发布时间**：2026-04-30

### 📄 论文摘要

Sign languages, of any geographical or accentual variation, understandably face continuous scrutiny under the ever present popularity of verbal dictation and audism. Through this, many potential problems arise with the current lack of accessible communication for those who rely on such sign languages for essential conversation. Such AI systems regularly take the form of recognition and interpretation models, designed to provide seamless and accurate translation. In reality these systems are built from biased data and created without any input from deaf communities. Such models are widely used and accepted by their hearing counterparts who remain ignorant to the inherent culture, semantics and colloquial language present in gestural language systems.   This phenomenon is best analysed under the scope of The Technological System and Technological bluff by Ellul. Indeed, what is at play here is the standardization of language by technicians into what can be captured by technique: data, statistics, a mathematical language. For that AI technique to exist, sign language must be rationalized, in a search for profit that annihilates the conditions for communication and fails to capture the human experience of the deaf person. By that process, it presents normative effects, creating a model of Man, standardized, massified, and who has to adapt to the tool and technical milieu instead of the other way around, which we assume should have been the goal of such a technology.   Technique thus reshapes what it means to be human, to submit deaf people to the goals of productivity and efficiency. In doing so, it exhibits clear counter productivity, alienating instead of emancipating, isolating instead of nourishing human relationships. Therefore this paper argues for the idea of AI as Ableist Intelligence, as such systems seek to emphasise the humiliated and marginalised nature of sign.

### 🤖 AI 总结

**一句话总结**：Sign languages, of any geographical or accentual variation, understandably face continuous scrutiny under the ever present popularity of verbal dictation and audism. Through this, many potential probl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Normativity, Productivism, Ableist, Intelligence?, Degrowth, Analysis, Sign

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28125v1) | [下载PDF](https://arxiv.org/pdf/2604.28125v1.pdf)

---

## [5. Mapping the Methodological Space of Classroom Interaction Research: Scale, Duration, and Modality in an Age of AI](https://arxiv.org/abs/2604.28098v1)

**作者**：Dorottya Demszky, Edith Bouton, Alison Twiner 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.CY  
**发布时间**：2026-04-30

### 📄 论文摘要

Research on classroom interaction has long been divided between large-scale observation and in-depth ethnographic work. We propose a framework mapping this methodological space along three dimensions--scale, duration, and modality--where a study's position shapes what it reveals and obscures. We illustrate it through contrasting studies of dialogic teaching--Howe et al. (2019) and Snell and Lefstein (2018)--and an interview with the lead researchers, organized around three questions: what can be operationalized, what mechanisms become visible, and what translates to practice. We then examine how AI is expanding this space and how the framework can guide research and tool design.

### 🤖 AI 总结

**一句话总结**：Research on classroom interaction has long been divided between large-scale observation and in-depth ethnographic work. We propose a framework mapping this methodological space along three dimensions-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Mapping, Methodological, Space, Classroom, Interaction, Research, Scale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28098v1) | [下载PDF](https://arxiv.org/pdf/2604.28098v1.pdf)

---

## [6. What Makes a Good Terminal-Agent Benchmark Task: A Guideline for Adversarial, Difficult, and Legible Evaluation Design](https://arxiv.org/abs/2604.28093v1)

**作者**：Ivan Bercovich  
**分类**：cs.AI  
**发布时间**：2026-04-30

### 📄 论文摘要

Terminal-agent benchmarks have become a primary signal for measuring the coding and system-administration capabilities of large language models. As the market for evaluation environments grows, so does the pressure to ship tasks quickly, often without thorough adversarial review of the verification logic. This paper is a guideline for writing good benchmark tasks, drawn from over a year of contributing to and reviewing tasks for Terminal Bench. Most people write benchmark tasks the way they write prompts. They shouldn't. A prompt is designed to help the agent succeed; a benchmark is designed to find out if it can. We argue that good tasks are adversarial, difficult, and legible, and that a large class of common failure modes -- AI-generated instructions, over-prescriptive specifications, clerical difficulty, oracle solutions that assume hidden knowledge, tests that validate the wrong things, and reward-hackable environments -- are predictable consequences of treating task authoring as prompt authoring. We catalog these failure modes, argue that real difficulty is conceptual rather than environmental, and discuss recent empirical evidence that over 15% of tasks in popular terminal-agent benchmarks are reward-hackable. We hope this serves as a useful reference for benchmark maintainers, task contributors, and researchers using benchmark scores as evidence.

### 🤖 AI 总结

**一句话总结**：Terminal-agent benchmarks have become a primary signal for measuring the coding and system-administration capabilities of large language models. As the market for evaluation environments grows, so doe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：What, Makes, Good, Terminal-Agent, Benchmark, Task, Guideline, Adversarial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28093v1) | [下载PDF](https://arxiv.org/pdf/2604.28093v1.pdf)

---

## [7. Characterizing the Consistency of the Emergent Misalignment Persona](https://arxiv.org/abs/2604.28082v1)

**作者**：Anietta Weckauff, Yuchen Zhang, Maksym Andriushchenko  
**分类**：cs.AI  
**发布时间**：2026-04-30

### 📄 论文摘要

Fine-tuning large language models (LLMs) on narrowly misaligned data generalizes to broadly misaligned behavior, a phenomenon termed emergent misalignment (EM). While prior work has found a correlation between harmful behavior and self-assessment in emergently misaligned models, it remains unclear how consistent this correspondence is across tasks and whether it varies across fine-tuning domains. We characterize the consistency of the EM persona by fine-tuning Qwen 2.5 32B Instruct on six narrowly misaligned domains (e.g., insecure code, risky financial advice, bad medical advice) and administering experiments including harmfulness evaluation, self-assessment, choosing between two descriptions of AI systems, output recognition, and score prediction. Our results reveal two distinct patterns: coherent-persona models, in which harmful behavior and self-reported misalignment are coupled, and inverted-persona models, which produce harmful outputs while identifying as aligned AI systems. These findings reveal a more fine-grained picture of the effects of emergent misalignment, calling into question the consistency of the EM persona.

### 🤖 AI 总结

**一句话总结**：Fine-tuning large language models (LLMs) on narrowly misaligned data generalizes to broadly misaligned behavior, a phenomenon termed emergent misalignment (EM). While prior work has found a correlatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Characterizing, Consistency, Emergent, Misalignment, Persona, Fine-tuning, large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28082v1) | [下载PDF](https://arxiv.org/pdf/2604.28082v1.pdf)

---

## cs.CV

## [8. HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196v1)

**作者**：Xin Zhou, Dingkang Liang, Xiwu Chen 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-30

### 📄 论文摘要

Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics. However, existing approaches predominantly focus on future scene generation, often overlooking comprehensive 3D scene understanding. Conversely, while Large Language Models (LLMs) demonstrate impressive reasoning capabilities, they lack the capacity to predict future geometric evolution, creating a significant disparity between semantic interpretation and physical simulation. To bridge this gap, we propose HERMES++, a unified driving world model that integrates 3D scene understanding and future geometry prediction within a single framework. Our approach addresses the distinct requirements of these tasks through synergistic designs. First, a BEV representation consolidates multi-view spatial information into a structure compatible with LLMs. Second, we introduce LLM-enhanced world queries to facilitate knowledge transfer from the understanding branch. Third, a Current-to-Future Link is designed to bridge the temporal gap, conditioning geometric evolution on semantic context. Finally, to enforce structural integrity, we employ a Joint Geometric Optimization strategy that integrates explicit geometric constraints with implicit latent regularization to align internal representations with geometry-aware priors. Extensive evaluations on multiple benchmarks validate the effectiveness of our method. HERMES++ achieves strong performance, outperforming specialist approaches in both future point cloud prediction and 3D scene understanding tasks. The model and code will be publicly released at https://github.com/H-EmbodVis/HERMESV2.

### 🤖 AI 总结

**一句话总结**：Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics. However, existing approaches predominantly focus on future scene generation, often overl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, HERMES++, Toward, Unified, Driving, World, Model, Scene

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28196v1) | [下载PDF](https://arxiv.org/pdf/2604.28196v1.pdf)

---

## [9. Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193v1)

**作者**：Vinayak Gupta, Chih-Hao Lin, Shenlong Wang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-30

### 📄 论文摘要

Reconstructing 3D scenes from sparse, unposed images remains challenging under real-world conditions with varying illumination and transient occlusions. Existing methods rely on scene-specific optimization using appearance embeddings or dynamic masks, which requires extensive per-scene training and fails under sparse views. Moreover, evaluations on limited scenes raise questions about generalization. We present GenWildSplat, a feed-forward framework for sparse-view outdoor reconstruction that requires no per-scene optimization. Given unposed internet images, GenWildSplat predicts depth, camera parameters, and 3D Gaussians in a canonical space using learned geometric priors. An appearance adapter modulates appearance for target lighting conditions, while semantic segmentation handles transient objects. Through curriculum learning on synthetic and real data, GenWildSplat generalizes across diverse illumination and occlusion patterns. Evaluations on PhotoTourism and MegaScenes benchmark demonstrate state-of-the-art feed-forward rendering quality, achieving real-time inference without test-time optimization

### 🤖 AI 总结

**一句话总结**：Reconstructing 3D scenes from sparse, unposed images remains challenging under real-world conditions with varying illumination and transient occlusions. Existing methods rely on scene-specific optimiz...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Generalizable, Sparse-View, Reconstruction, Unconstrained, Images, Reconstructing, scenes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28193v1) | [下载PDF](https://arxiv.org/pdf/2604.28193v1.pdf)

---

## [10. Representation Fréchet Loss for Visual Generation](https://arxiv.org/abs/2604.28190v1)

**作者**：Jiawei Yang, Zhengyang Geng, Xuan Ju 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-30

### 📄 论文摘要

We show that Fréchet Distance (FD), long considered impractical as a training objective, can in fact be effectively optimized in the representation space. Our idea is simple: decouple the population size for FD estimation (e.g., 50k) from the batch size for gradient computation (e.g., 1024). We term this approach FD-loss. Optimizing FD-loss reveals several surprising findings. First, post-training a base generator with FD-loss in different representation spaces consistently improves visual quality. Under the Inception feature space, a one-step generator achieves0.72 FID on ImageNet 256x256. Second, the same FD-loss repurposes multi-step generators into strong one-step generators without teacher distillation, adversarial training or per-sample targets. Third, FID can misrank visual quality: modern representations can yield better samples despite worse Inception FID. This motivates FDr$^k$, a multi-representation metric. We hope this work will encourage further exploration of distributional distances in diverse representation spaces as both training objectives and evaluation metrics for generative models.

### 🤖 AI 总结

**一句话总结**：We show that Fréchet Distance (FD), long considered impractical as a training objective, can in fact be effectively optimized in the representation space. Our idea is simple: decouple the population s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Representation, Fréchet, Loss, Visual, Generation, show, Distance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28190v1) | [下载PDF](https://arxiv.org/pdf/2604.28190v1.pdf)

---

## [11. Visual Generation in the New Era: An Evolution from Atomic Mapping to Agentic World Modeling](https://arxiv.org/abs/2604.28185v1)

**作者**：Keming Wu, Zuhao Yang, Kaichen Zhang 等 27 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-30

### 📄 论文摘要

Recent visual generation models have made major progress in photorealism, typography, instruction following, and interactive editing, yet they still struggle with spatial reasoning, persistent state, long-horizon consistency, and causal understanding. We argue that the field should move beyond appearance synthesis toward intelligent visual generation: plausible visuals grounded in structure, dynamics, domain knowledge, and causal relations. To frame this shift, we introduce a five-level taxonomy: Atomic Generation, Conditional Generation, In-Context Generation, Agentic Generation, and World-Modeling Generation, progressing from passive renderers to interactive, agentic, world-aware generators. We analyze key technical drivers, including flow matching, unified understanding-and-generation models, improved visual representations, post-training, reward modeling, data curation, synthetic data distillation, and sampling acceleration. We further show that current evaluations often overestimate progress by emphasizing perceptual quality while missing structural, temporal, and causal failures. By combining benchmark review, in-the-wild stress tests, and expert-constrained case studies, this roadmap offers a capability-centered lens for understanding, evaluating, and advancing the next generation of intelligent visual generation systems.

### 🤖 AI 总结

**一句话总结**：Recent visual generation models have made major progress in photorealism, typography, instruction following, and interactive editing, yet they still struggle with spatial reasoning, persistent state, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Visual, Generation, New, Era, Evolution, Atomic, Mapping

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28185v1) | [下载PDF](https://arxiv.org/pdf/2604.28185v1.pdf)

---

## [12. Stop Holding Your Breath: CT-Informed Gaussian Splatting for Dynamic Bronchoscopy](https://arxiv.org/abs/2604.28179v1)

**作者**：Andrea Dunn Beltran, Daniel Rho, Aarav Mehta 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-30

### 📄 论文摘要

Bronchoscopic navigation relies on registering endoscopic video to a preoperative CT scan, but respiratory motion deforms the airway by 5-20 mm, creating CT-to-body divergence that limits localization accuracy. In practice, this is mitigated through breath-hold protocols, which attempt to match the intraoperative anatomy to a static CT, but are difficult to reproduce and disrupt clinical workflow. We propose to eliminate the need for breath-hold protocols by leveraging patient-specific respiratory modeling. Paired inhale-exhale CT scans, already acquired for planning, implicitly define the patient-specific deformation space of the breathing airway. By registering these scans, we reduce respiratory motion to a single scalar breathing phase per frame, constraining all reconstructions to anatomically observed configurations. We embed this representation within a mesh-anchored Gaussian splatting framework, where a lightweight estimator infers breathing phase directly from endoscopic RGB, enabling continuous, deformation-aware reconstruction throughout the respiratory cycle without breath-holds or external sensing. To enable quantitative evaluation, we introduce RESPIRE, a physically grounded bronchoscopy simulation pipeline with per-frame ground truth for geometry, pose, breathing phase, and deformation. Experiments on RESPIRE show that our approach achieves geometrically faithful reconstruction, over 20x faster training, and 1.22 mm target localization accuracy (within the 3mm clinically relevant tolerances) outperforming unconstrained single-CT baselines. Please check out our website for additional visuals: https://asdunnbe.github.io/RESPIRE/

### 🤖 AI 总结

**一句话总结**：Bronchoscopic navigation relies on registering endoscopic video to a preoperative CT scan, but respiratory motion deforms the airway by 5-20 mm, creating CT-to-body divergence that limits localization...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Stop, Holding, Breath, CT-Informed, Gaussian, Splatting, Dynamic, Bronchoscopy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28179v1) | [下载PDF](https://arxiv.org/pdf/2604.28179v1.pdf)

---

## [13. AEGIS: A Holistic Benchmark for Evaluating Forensic Analysis of AI-Generated Academic Images](https://arxiv.org/abs/2604.28177v1)

**作者**：Bo Zhang, Tzu-Yen Ma, Zichen Tang 等 21 位作者  
**分类**：cs.CV, cs.CY  
**发布时间**：2026-04-30

### 📄 论文摘要

We introduce AEGIS, A holistic benchmark for Evaluating forensic analysis of AI-Generated academic ImageS. Compared to existing benchmarks, AEGIS features three key advances: (1) Domain-Specific Complexity: covering seven academic categories with 39 fine-grained subtypes, exposing intrinsic forensic difficulty, where even GPT-5.1 reaches 48.80% overall performance and expert models achieve only limited localization accuracy (IoU 30.09%); (2) Diverse Forgery Simulations: modeling four prevalent academic forgery strategies across 25 generative models, with 11 yielding average forensic accuracy below 50%, showing that forensics lag behind generative advances; and (3) Multi-Dimensional Forensic Evaluation: jointly assessing detection, reasoning, and localization, revealing complementary strengths between model families, with multimodal large language models (MLLMs) at 84.74% accuracy in textual artifact recognition and expert detectors peaking at 79.54% accuracy in binary authenticity detection. By evaluating 25 leading MLLMs, nine expert models, and one unified multimodal understanding and generation model, AEGIS serves as a diagnostic testbed exposing fundamental limitations in academic image forensics.

### 🤖 AI 总结

**一句话总结**：We introduce AEGIS, A holistic benchmark for Evaluating forensic analysis of AI-Generated academic ImageS. Compared to existing benchmarks, AEGIS features three key advances: (1) Domain-Specific Compl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, AEGIS, Holistic, Benchmark, Evaluating, Forensic, Analysis, AI-Generated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28177v1) | [下载PDF](https://arxiv.org/pdf/2604.28177v1.pdf)

---

## [14. PhyCo: Learning Controllable Physical Priors for Generative Motion](https://arxiv.org/abs/2604.28169v1)

**作者**：Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan 等 4 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-04-30

### 📄 论文摘要

Modern video diffusion models excel at appearance synthesis but still struggle with physical consistency: objects drift, collisions lack realistic rebound, and material responses seldom match their underlying properties. We present PhyCo, a framework that introduces continuous, interpretable, and physically grounded control into video generation. Our approach integrates three key components: (i) a large-scale dataset of over 100K photorealistic simulation videos where friction, restitution, deformation, and force are systematically varied across diverse scenarios; (ii) physics-supervised fine-tuning of a pretrained diffusion model using a ControlNet conditioned on pixel-aligned physical property maps; and (iii) VLM-guided reward optimization, where a fine-tuned vision-language model evaluates generated videos with targeted physics queries and provides differentiable feedback. This combination enables a generative model to produce physically consistent and controllable outputs through variations in physical attributes-without any simulator or geometry reconstruction at inference. On the Physics-IQ benchmark, PhyCo significantly improves physical realism over strong baselines, and human studies confirm clearer and more faithful control over physical attributes. Our results demonstrate a scalable path toward physically consistent, controllable generative video models that generalize beyond synthetic training environments.

### 🤖 AI 总结

**一句话总结**：Modern video diffusion models excel at appearance synthesis but still struggle with physical consistency: objects drift, collisions lack realistic rebound, and material responses seldom match their un...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PhyCo, Learning, Controllable, Physical, Priors, Generative, Motion, Modern

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28169v1) | [下载PDF](https://arxiv.org/pdf/2604.28169v1.pdf)

---

## [15. Continuous-tone Simple Points: An $\ell_0$-Norm of Cyclic Gradient for Topology-Preserving Data-Driven Image Segmentation](https://arxiv.org/abs/2604.28159v1)

**作者**：Wenxiao Li, Faqiang Wang, Yuping Duan 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-30

### 📄 论文摘要

Topological features play an essential role in ensuring geometric plausibility and structural consistency in image analysis tasks such as segmentation and skeletonization. However, integrating topology-preserving learning based on simple points into deep learning tasks remains challenging, as existing simple point detection methods are confined to binary images and are non-differentiable, rendering them incompatible with gradient-based optimization in modern deep learning. Moreover, morphological and purely data-driven approaches often fail to guaranty topological consistency. To address these limitations, we propose a novel method that directly computes simple points on continuous-valued images, enabling differentiable topological inference. Building on this theory, we develop an efficient skeleton extraction algorithm that preserves topological structures in binary and continuous-valued images. Furthermore, we design a variational model that enforces topological constraints by preserving topologically non-removable (i.e., non-simple) points, which can be seamlessly integrated into any deep neural network segmentation with softmax or sigmoid outputs. Experimental results demonstrate that the proposed approach effectively improves topological integrity and structural accuracy across multiple benchmarks. The codes are available in https://github.com/levnsio/CSP.

### 🤖 AI 总结

**一句话总结**：Topological features play an essential role in ensuring geometric plausibility and structural consistency in image analysis tasks such as segmentation and skeletonization. However, integrating topolog...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, of, Continuous-tone, Simple, Points, ell, 0$-Norm, Cyclic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28159v1) | [下载PDF](https://arxiv.org/pdf/2604.28159v1.pdf)

---

## [16. Beyond Pixel Fidelity: Minimizing Perceptual Distortion and Color Bias in Night Photography Rendering](https://arxiv.org/abs/2604.28136v1)

**作者**：Furkan Kınlı  
**分类**：cs.CV  
**发布时间**：2026-04-30

### 📄 论文摘要

Night Photography Rendering (NPR) poses a significant challenge due to the extreme contrast between dark and illuminated areas in scenes, stemming from concurrent capture of severely dark regions alongside intense point light sources. Existing methods, which are mainly tailored for fidelity metrics, reveal considerable perceptual gaps and often detract from visual quality. We introduce pHVI-ISPNet, a novel RAW-to-RGB framework built on the robust HVI color space. Our network integrates four distinct key refinements: RAW-domain feature processing and Wavelet-based feature propagation to mitigate high-frequency detail loss; sample-based dynamic loss coefficients to ensure stable learning across varying exposure levels; and loss term based on feature distributions to maintain rigorous color constancy. Evaluations on the dataset introduced in the NTIRE 2025 challenge on NPR confirm our approach achieves competitive fidelity while establishing new state-of-the-art results in both CIE2000 color difference and LPIPS. This validates our perceptually-driven design for high-quality nighttime imaging.

### 🤖 AI 总结

**一句话总结**：Night Photography Rendering (NPR) poses a significant challenge due to the extreme contrast between dark and illuminated areas in scenes, stemming from concurrent capture of severely dark regions alon...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Pixel, Fidelity, Minimizing, Perceptual, Distortion, Color, Bias

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28136v1) | [下载PDF](https://arxiv.org/pdf/2604.28136v1.pdf)

---

## [17. 3D-ReGen: A Unified 3D Geometry Regeneration Framework](https://arxiv.org/abs/2604.28134v1)

**作者**：Geon Yeong Park, Roman Shapovalov, Rakesh Ranjan 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-30

### 📄 论文摘要

We consider the problem of regenerating 3D objects from 2D images and initial 3D shapes. Most 3D generators operate in a one-shot fashion, converting text or images to a 3D object with limited controllability. We introduce instead 3D-ReGen, a 3D regenerator that is conditioned on an initial 3D shape. This conceptually simple formulation allows us to support numerous useful tasks, including 3D enhancement, reconstruction, and editing. 3D-ReGen uses a new conditioning mechanism based on VecSet, which allows the regenerator to update or improve the input geometry with consistent fine-grained details. 3D-ReGen learns a widely applicable regeneration prior from off-the-shelf 3D datasets via self-supervised pretext tasks and augmentations, without additional annotations. We evaluate both the geometric consistency and fine-grained quality of 3D-ReGen, achieving state-of-the-art performance in controllable 3D generation across several tasks.

### 🤖 AI 总结

**一句话总结**：We consider the problem of regenerating 3D objects from 2D images and initial 3D shapes. Most 3D generators operate in a one-shot fashion, converting text or images to a 3D object with limited control...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, We, 3D-ReGen, Unified, Geometry, Regeneration, Framework, consider

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28134v1) | [下载PDF](https://arxiv.org/pdf/2604.28134v1.pdf)

---

## [18. MoCapAnything V2: End-to-End Motion Capture for Arbitrary Skeletons](https://arxiv.org/abs/2604.28130v1)

**作者**：Kehong Gong, Zhengyu Wen, Dao Thien Phong 等 13 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-30

### 📄 论文摘要

Recent methods for arbitrary-skeleton motion capture from monocular video follow a factorized pipeline, where a Video-to-Pose network predicts joint positions and an analytical inverse-kinematics (IK) stage recovers joint rotations. While effective, this design is inherently limited, since joint positions do not fully determine rotations and leave degrees of freedom such as bone-axis twist ambiguous, and the non-differentiable IK stage prevents the system from adapting to noisy predictions or optimizing for the final animation objective. In this work, we present the first fully end-to-end framework in which both Video-to-Pose and Pose-to-Rotation are learnable and jointly optimized. We observe that the ambiguity in pose-to-rotation mapping arises from missing coordinate system information: the same joint positions can correspond to different rotations under different rest poses and local axis conventions. To resolve this, we introduce a reference pose-rotation pair from the target asset, which, together with the rest pose, not only anchors the mapping but also defines the underlying rotation coordinate system. This formulation turns rotation prediction into a well-constrained conditional problem and enables effective learning. In addition, our model predicts joint positions directly from video without relying on mesh intermediates, improving both robustness and efficiency. Both stages share a skeleton-aware Global-Local Graph-guided Multi-Head Attention (GL-GMHA) module for joint-level local reasoning and global coordination. Experiments on Truebones Zoo and Objaverse show that our method reduces rotation error from ~17 degrees to ~10 degrees, and to 6.54 degrees on unseen skeletons, while achieving ~20x faster inference than mesh-based pipelines. Project page: https://animotionlab.github.io/MoCapAnythingV2/

### 🤖 AI 总结

**一句话总结**：Recent methods for arbitrary-skeleton motion capture from monocular video follow a factorized pipeline, where a Video-to-Pose network predicts joint positions and an analytical inverse-kinematics (IK)...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：V2, MoCapAnything, End-to-End, Motion, Capture, Arbitrary, Skeletons, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28130v1) | [下载PDF](https://arxiv.org/pdf/2604.28130v1.pdf)

---

## [19. Beyond Gaussian Bottlenecks: Topologically Aligned Encoding of Vision-Transformer Feature Spaces](https://arxiv.org/abs/2604.28122v1)

**作者**：Andrew Bond, Ilkin Umut Melanlioglu, Erkut Erdem 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-04-30

### 📄 论文摘要

Modern visual world modeling systems increasingly rely on high-capacity architectures and large-scale data to produce plausible motion, yet they often fail to preserve underlying 3D geometry or physically consistent camera dynamics. A key limitation lies not only in model capacity, but in the latent representations used to encode geometric structure. We propose S$^2$VAE, a geometry-first latent learning framework that focuses on compressing and representing the latent 3D state of a scene, including camera motion, depth, and point-level structure, rather than modeling appearance alone. Building on representations from a Visual Geometry Grounded Transformer (VGGT), we introduce a novel type of variational autoencoder using a product of Power Spherical latent distributions, explicitly enforcing hyperspherical structure in the bottleneck to preserve directional and geometric semantics under strong compression. Across depth estimation, camera pose recovery, and point cloud reconstruction, we show that geometry-aligned hyperspherical latents consistently outperform conventional Gaussian bottlenecks, particularly in high-compression regimes. Our results highlight latent geometry as a first-class design choice for physically grounded visual and world models.

### 🤖 AI 总结

**一句话总结**：Modern visual world modeling systems increasingly rely on high-capacity architectures and large-scale data to produce plausible motion, yet they often fail to preserve underlying 3D geometry or physic...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Beyond, Gaussian, Bottlenecks, Topologically, Aligned, Encoding, Vision-Transformer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28122v1) | [下载PDF](https://arxiv.org/pdf/2604.28122v1.pdf)

---

## [20. UHR-Net: An Uncertainty-Aware Hypergraph Refinement Network for Medical Image Segmentation](https://arxiv.org/abs/2604.28095v1)

**作者**：Shuokun Cheng, Jinghao Shi, Kun Sun  
**分类**：cs.CV  
**发布时间**：2026-04-30

### 📄 论文摘要

Accurate lesion segmentation is crucial for clinical diagnosis and treatment planning. However, lesions often resemble surrounding tissues and exhibit ill-defined boundaries, leading to unstable predictions in boundary/transition regions. Moreover, small-lesion cues can be diluted by multi-scale feature extraction, causing under- or over-segmentation. To address these challenges, we propose an Uncertainty-Aware Hypergraph Refinement Network (UHR-Net). First, we introduce an Uncertainty-Oriented Instance Contrastive (UO-IC) pretraining strategy that couples geometry-aware copy-paste augmentation with hard-negative mining of lesion-like background regions to improve instance-level discrimination for small and visually ambiguous lesions. Second, we design an Uncertainty-Guided Hypergraph Refinement (UGHR) block, which derives an entropy-based uncertainty map from a coarse probability map to guide hypergraph refinement. By splitting hyperedge prototypes into foreground and background groups, UGHR decouples higher-order interactions and improves refinement in ambiguous regions. Experiments on five public benchmarks demonstrate consistent gains over strong baselines. Code is available at: https://github.com/CUGfreshman/UHR-Net.

### 🤖 AI 总结

**一句话总结**：Accurate lesion segmentation is crucial for clinical diagnosis and treatment planning. However, lesions often resemble surrounding tissues and exhibit ill-defined boundaries, leading to unstable predi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, UHR-Net, Uncertainty-Aware, Hypergraph, Refinement, Network, Medical, Image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28095v1) | [下载PDF](https://arxiv.org/pdf/2604.28095v1.pdf)

---

## [21. AesRM: Improving Video Aesthetics with Expert-Level Feedback](https://arxiv.org/abs/2604.28078v1)

**作者**：Yujin Han, Yujie Wei, Yefei He 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-30

### 📄 论文摘要

Despite rapid advances in photorealistic video generation, real-world applications such as filmmaking require video aesthetics, e.g., harmonious colors and cinematic lighting, beyond visual fidelity. Prior work on visual aesthetics largely focuses on images, often reducing aesthetics to coarse definitions, e.g., visual pleasure, without a rigorous and systematic evaluation. To improve video aesthetics, we propose a hierarchical rubric that decomposes video aesthetics into three core dimensions, Visual Aesthetics (VA), Visual Fidelity (VF), and Visual Plausibility (VP), with 15 fine-grained criteria, e.g., shot composition. This framework enables a large-scale expert-annotated preference dataset and an evaluation benchmark, AesVideo-Bench, containing about 2500 video pairs with expert annotations on VA, VF, and VP. We then build a family of Video Aesthetic Reward Models (AesRM): AesRM-Base, which directly predicts pairwise preferences on these dimensions to provide efficient post-training rewards, and AesRM-CoT, which additionally generates CoT aligned with all 15 criteria to improve assessment interpretability. Specifically, we train AesRM with a three-stage progressive scheme: (1) Atomic Aesthetic Capability Learning, which strengthens AesRM's recognition of fundamental aesthetic concepts, e.g., accurately identifying centered composition; (2) Cold-Start, aligning the model with structured reasoning protocols; and (3) GRPO, further improving evaluation accuracy. To enhance AesRM-CoT, we additionally propose self-consistency-based CoT synthesis to improve CoT quality and design CoT-based process rewards during GRPO. Extensive experiments show AesRM outperforms baselines on multiple aesthetics benchmarks and is more robust, with lower position bias. Finally, we align Wan2.2 with AesRM and observe clear aesthetic gains over existing aesthetic reward models.

### 🤖 AI 总结

**一句话总结**：Despite rapid advances in photorealistic video generation, real-world applications such as filmmaking require video aesthetics, e.g., harmonious colors and cinematic lighting, beyond visual fidelity. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AesRM, Improving, Video, Aesthetics, Expert-Level, Feedback, Despite, rapid

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28078v1) | [下载PDF](https://arxiv.org/pdf/2604.28078v1.pdf)

---

## cs.LG

## [22. Exploration Hacking: Can LLMs Learn to Resist RL Training?](https://arxiv.org/abs/2604.28182v1)

**作者**：Eyon Jang, Damon Falck, Joschka Braun 等 9 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-04-30

### 📄 论文摘要

Reinforcement learning (RL) has become essential to the post-training of large language models (LLMs) for reasoning, agentic capabilities and alignment. Successful RL relies on sufficient exploration of diverse actions by the model during training, which creates a potential failure mode: a model could strategically alter its exploration during training to influence the subsequent training outcome. In this paper we study this behavior, called exploration hacking. First, we create model organisms of selective RL resistance by fine-tuning LLMs to follow specific underperformance strategies; these models can successfully resist our RL-based capability elicitation in agentic biosecurity and AI R&D environments while maintaining performance on related tasks. We then use our model organisms to evaluate detection and mitigation strategies, including monitoring, weight noising, and SFT-based elicitation. Finally, we show that current frontier models can exhibit explicit reasoning about suppressing their exploration when provided with sufficient information about their training context, with higher rates when this information is acquired indirectly through the environment. Together, our results suggest exploration hacking is a possible failure mode of RL on sufficiently capable LLMs.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning (RL) has become essential to the post-training of large language models (LLMs) for reasoning, agentic capabilities and alignment. Successful RL relies on sufficient exploration ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, RL, Exploration, Hacking, Can, Learn, Resist, Training?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28182v1) | [下载PDF](https://arxiv.org/pdf/2604.28182v1.pdf)

---

## [23. An adaptive wavelet-based PINN for problems with localized high-magnitude source](https://arxiv.org/abs/2604.28180v1)

**作者**：Himanshu Pandey, Ratikanta Behera  
**分类**：cs.LG  
**发布时间**：2026-04-30

### 📄 论文摘要

In recent years, physics-informed neural networks (PINNs) have gained significant attention for solving differential equations, although they suffer from two fundamental limitations, namely, spectral bias inherent in neural networks and loss imbalance arising from multiscale phenomena. This paper proposes an adaptive wavelet-based PINN (AW-PINN) to address the extreme loss imbalance characteristic of problems with localized high-magnitude source terms. Such problems frequently arise in various physical applications, such as thermal processing, electro-magnetics, impact mechanics, and fluid dynamics involving localized forcing. The proposed framework dynamically adjusts the wavelet basis function based on residual and supervised loss. This adaptive nature makes AW-PINN handle problems with high-scale features effectively without being memory-intensive. Additionally, AW-PINN does not rely on automatic differentiation to obtain derivatives involved in the loss function, which accelerates the training process. The method operates in two stages, an initial short pre-training phase with fixed bases to select physically relevant wavelet families, followed by an adaptive refinement that adapts scales and translations without populating high-resolution bases across entire domains. Theoretically, we show that under certain assumptions, AW-PINN admits a Gaussian process limit and derive its associated NTK structure. We evaluate AW-PINN on several challenging PDEs featuring localized high-magnitude source terms with extreme loss imbalances having ratios up to $10^{10}:1$. Across these PDEs, including transient heat conduction, highly localized Poisson problems, oscillatory flow equations, and Maxwell equations with a point charge source, AW-PINN consistently outperforms existing methods in its class.

### 🤖 AI 总结

**一句话总结**：In recent years, physics-informed neural networks (PINNs) have gained significant attention for solving differential equations, although they suffer from two fundamental limitations, namely, spectral ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, adaptive, wavelet-based, PINN, problems, localized, high-magnitude, recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28180v1) | [下载PDF](https://arxiv.org/pdf/2604.28180v1.pdf)

---

## [24. Strait: Perceiving Priority and Interference in ML Inference Serving](https://arxiv.org/abs/2604.28175v1)

**作者**：Haidong Zhao, Nikolaos Georgantas  
**分类**：cs.LG  
**发布时间**：2026-04-30

### 📄 论文摘要

Machine learning (ML) inference serving systems host deep neural network (DNN) models and schedule incoming inference requests across deployed GPUs. However, limited support for task prioritization and insufficient latency estimation under concurrent execution may restrict their applicability in on-premises scenarios. We present \emph{Strait}, a serving system designed to enhance deadline satisfaction for dual-priority inference traffic under high GPU utilization. To improve latency estimation, Strait models potential contention during data transfer and accounts for kernel execution interference through an adaptive prediction model. By drawing on these predictions, it performs priority-aware scheduling to deliver differentiated handling. Evaluation results under intense workloads suggest that Strait reduces deadline violations for high-priority tasks by 1.02 to 11.18 percentage points while incurring acceptable costs on low-priority tasks. Compared to software-defined preemption approaches, Strait also exhibits more equitable performance.

### 🤖 AI 总结

**一句话总结**：Machine learning (ML) inference serving systems host deep neural network (DNN) models and schedule incoming inference requests across deployed GPUs. However, limited support for task prioritization an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ML, Strait, Perceiving, Priority, Interference, Inference, Serving, Machine

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28175v1) | [下载PDF](https://arxiv.org/pdf/2604.28175v1.pdf)

---

## [25. Explainable Load Forecasting with Covariate-Informed Time Series Foundation Models](https://arxiv.org/abs/2604.28149v1)

**作者**：Matthias Hertel, Alexandra Nikoltchovska, Sebastian Pütz 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-30

### 📄 论文摘要

Time Series Foundation Models (TSFMs) have recently emerged as general-purpose forecasting models and show considerable potential for applications in energy systems. However, applications in critical infrastructure like power grids require transparency to ensure trust and reliability and cannot rely on pure black-box models. To enhance the transparency of TSFMs, we propose an efficient algorithm for computing Shapley Additive Explanations (SHAP) tailored to these models. The proposed approach leverages the flexibility of TSFMs with respect to input context length and provided covariates. This property enables efficient temporal and covariate masking (selectively withholding inputs), allowing for a scalable explanation of model predictions using SHAP. We evaluate two TSFMs - Chronos-2 and TabPFN-TS - on a day-ahead load forecasting task for a transmission system operator (TSO). In a zero-shot setting, both models achieve predictive performance competitive with a Transformer model trained specifically on multiple years of TSO data. The explanations obtained through our proposed approach align with established domain knowledge, particularly as the TSFMs appropriately use weather and calendar information for load prediction. Overall, we demonstrate that TSFMs can serve as transparent and reliable tools for operational energy forecasting.

### 🤖 AI 总结

**一句话总结**：Time Series Foundation Models (TSFMs) have recently emerged as general-purpose forecasting models and show considerable potential for applications in energy systems. However, applications in critical ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Explainable, Load, Forecasting, Covariate-Informed, Time, Series, Foundation, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28149v1) | [下载PDF](https://arxiv.org/pdf/2604.28149v1.pdf)

---

## [26. Global Optimality for Constrained Exploration via Penalty Regularization](https://arxiv.org/abs/2604.28144v1)

**作者**：Florian Wolf, Ilyas Fatkhullin, Niao He  
**分类**：cs.LG, math.OC  
**发布时间**：2026-04-30

### 📄 论文摘要

Efficient exploration is a central problem in reinforcement learning and is often formalized as maximizing the entropy of the state-action occupancy measure. While unconstrained maximum-entropy exploration is relatively well understood, real-world exploration is often constrained by safety, resource, or imitation requirements. This constrained setting is particularly challenging because entropy maximization lacks additive structure, rendering Bellman-equation-based methods inapplicable. Moreover, scalable approaches require policy parameterization, inducing non-convexity in both the objective and the constraints. To our knowledge, the only prior model-free policy-gradient approach for this setting under general policy parameterization is due to Ying et al. (2025). Unfortunately, their guarantees are limited to weak regret and ergodic averages, which do not imply that the final output is a single deployable policy that is near-optimal and nearly feasible. In this work we take a different approach to this problem, and propose Policy Gradient Penalty (PGP) method, a single-loop policy-space method that enforces general convex occupancy-measure constraints via quadratic-penalty regularization. PGP constructs pseudo-rewards that yield gradient estimates of the penalized objective, subsequently exploiting the classical Policy Gradient Theorem. We further establish the regularity of the penalized objective, providing the smoothness properties needed to justify the convergence of PGP. Leveraging hidden convexity and strong duality, we then establish global last-iterate convergence guarantees, attaining an $ε$-optimal constrained entropy value with $ε$ bounded constraint violation despite policy-induced non-convexity. We validate PGP through ablations on a grid-world benchmark and further demonstrate scalability on two challenging continuous-control tasks.

### 🤖 AI 总结

**一句话总结**：Efficient exploration is a central problem in reinforcement learning and is often formalized as maximizing the entropy of the state-action occupancy measure. While unconstrained maximum-entropy explor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Global, Optimality, Constrained, Exploration, via, Penalty, Regularization, Efficient

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28144v1) | [下载PDF](https://arxiv.org/pdf/2604.28144v1.pdf)

---

## [27. Do Sparse Autoencoders Capture Concept Manifolds?](https://arxiv.org/abs/2604.28119v1)

**作者**：Usha Bhalla, Thomas Fel, Can Rager 等 12 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-30

### 📄 论文摘要

Sparse autoencoders (SAEs) are widely used to extract interpretable features from neural network representations, often under the implicit assumption that concepts correspond to independent linear directions. However, a growing body of evidence suggests that many concepts are instead organized along low-dimensional manifolds encoding continuous geometric relationships. This raises three basic questions: what does it mean for an SAE to capture a manifold, when do existing SAE architectures do so, and how? We develop a theoretical framework that answers these questions and show that SAEs can capture manifolds in two fundamentally different ways: globally, by allocating a compact group of atoms whose linear span contains the entire manifold, or locally, by distributing it across features that each selectively tile a restricted region of the underlying geometry. Empirically, we find that SAEs suboptimally recover continuous structures, mixing the global subspace and local tiling solutions in a fragmented regime we call dilution. This explains why manifold structure is rarely visible at the level of individual concepts and motivates post-hoc unsupervised discovery methods that search for coherent groups of atoms rather than isolated directions. More broadly, our results suggest that future representation learning methods should treat geometric objects, not just individual directions, as the basic units of interpretability.

### 🤖 AI 总结

**一句话总结**：Sparse autoencoders (SAEs) are widely used to extract interpretable features from neural network representations, often under the implicit assumption that concepts correspond to independent linear dir...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, Sparse, Autoencoders, Capture, Concept, Manifolds?, SAEs, widely

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28119v1) | [下载PDF](https://arxiv.org/pdf/2604.28119v1.pdf)

---

## [28. Auto-FlexSwitch: Efficient Dynamic Model Merging via Learnable Task Vector Compression](https://arxiv.org/abs/2604.28109v1)

**作者**：Junqi Gao, Dazhi Zhang, Zhichang Guo 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-30

### 📄 论文摘要

Model merging has attracted attention as an effective path toward multi-task adaptation by integrating knowledge from multiple task-specific models. Among existing approaches, dynamic merging mitigates performance degradation caused by conflicting parameter updates across tasks by flexibly combining task-specific parameters at inference time, thereby maintaining high performance. However, these methods require storing independent parameters for each task, resulting in prohibitive storage overhead. To address this issue, we first experimentally demonstrate that the fine-tuned weight increments (referred to as task vectors) exhibit an impulse-like activation pattern and high robustness to low-bit representations. Driven by this insight, we propose T-Switch, which decomposes task vectors into three compact components: a binary sparse mask, a sign vector, and a scalar scaling factor, achieving high-fidelity approximation at high compression ratios. We then introduce Auto-Switch, a training-free merging scheme that automatically composes task vectors via feature similarity retrieval. Building on this, we develop Auto-Switch, a training-free merging scheme that automatically assembles task vectors through feature similarity retrieval. Furthermore, to transform task vector sparsification and quantization from static rules to adaptive learning, we propose FlexSwitch, a learnable framework which jointly optimizes the compression strategy for each model unit via Learnable Gating Sparsification (LGS) and Bit-width Adaptive Selection (BAS), while employing the Sparsity-Aware Storage Strategy (SASS) to select the optimal storage encoding structure. Finally, by incorporating a K-Nearest Neighbor (KNN) inference scheme with a learnable low-rank metric, we present Auto-FlexSwitch, a dynamic model merging approach that supports highly efficient task vector compression.

### 🤖 AI 总结

**一句话总结**：Model merging has attracted attention as an effective path toward multi-task adaptation by integrating knowledge from multiple task-specific models. Among existing approaches, dynamic merging mitigate...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Auto-FlexSwitch, Efficient, Dynamic, Model, Merging, via, Learnable, Task

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28109v1) | [下载PDF](https://arxiv.org/pdf/2604.28109v1.pdf)

---

## [29. Neural Aided Kalman Filtering for UAV State Estimation in Degraded Sensing Environments](https://arxiv.org/abs/2604.28107v1)

**作者**：Akhil Gupta, Erhan Guven  
**分类**：cs.LG  
**发布时间**：2026-04-30

### 📄 论文摘要

Accurate state estimation of nonlinear dynamical systems is fundamental to modern aerospace operations across air, sea, and space domains. Online tracking of adversarial unmanned aerial vehicles (UAVs) is especially challenging due to agile nonlinear motion, noisy and sparse sensor measurements, and unknown control inputs; conditions that violate key assumptions of classical Kalman filter variants and degrade estimation performance. Neural networks (NNs) can learn complex nonlinear relationships from data, but lack principled uncertainty quantification, which is critical for state estimation tasks where confidence bounds drive downstream decisions. We address this with Bayesian Neural Networks (BNNs), which model uncertainty through distributions over network weights and produce predictive means and uncertainties via Monte Carlo sampling. Building on this, we propose the Bayesian Neural Kalman Filter (BNKF): a hybrid framework coupling a trained BNN with a Kalman correction step for robust online UAV state estimation. Unlike related neural Kalman approaches, BNKF produces full state predictions and incorporates Bayesian uncertainty directly into covariance propagation, improving robustness under high noise conditions. We evaluate BNKF under varying radar noise levels and sampling rates using synthetic nonlinear UAV flight data. Five fold cross validation demonstrates that BNKF outperforms Extended and Unscented Kalman Filters in accuracy, precision, and truth containment under degraded sensing. An ensemble variant (BNKFe) further improves precision in high-noise edge cases at a slight accuracy tradeoff. Runtime analysis confirms minimal inference overhead, supporting real-time deployment feasibility.

### 🤖 AI 总结

**一句话总结**：Accurate state estimation of nonlinear dynamical systems is fundamental to modern aerospace operations across air, sea, and space domains. Online tracking of adversarial unmanned aerial vehicles (UAVs...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Neural, Aided, Kalman, Filtering, UAV, State, Estimation, Degraded

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28107v1) | [下载PDF](https://arxiv.org/pdf/2604.28107v1.pdf)

---

## [30. FiLMMeD: Feature-wise Linear Modulation for Cross-Problem Multi-Depot Vehicle Routing](https://arxiv.org/abs/2604.28102v1)

**作者**：Arthur Corrêa, Paulo Nascimento, Samuel Moniz  
**分类**：cs.LG  
**发布时间**：2026-04-30

### 📄 论文摘要

Solving practical multi-depot vehicle routing problems (MDVRP) is a challenging optimization task central to modern logistics, increasingly driven by e-commerce. To address the MDVRP's computational complexity, neural-based combinatorial optimization methods offer a promising scalable alternative to traditional approaches. However, neural-based methods typically rely on rigid architectures and input encodings tailored to specific problem formulations. In real-world settings, heterogeneous constraints create multiple MDVRP variants, limiting the applicability of such models. While multi-task learning (MTL) has begun to accelerate the development of unified neural-based solvers, prior works focus almost exclusively on single-depot VRPs, leaving the MDVRP unaddressed. To bridge this gap, we propose Feature-wise Linear Modulation for Cross-Problem Multi-Depot Vehicle Routing (FiLMMeD), a novel unified neural-based model for 24 different MDVRP variants. We introduce three main contributions: (1) to improve the model's generalization, we augment the standard Transformer encoder with Feature-wise Linear Modulation (FiLM), which dynamically conditions learned internal representations based on the active set of constraints; (2) we provide an initial demonstration of Preference Optimization in the MTL setting, establishing it as a superior alternative to Reinforcement Learning for future MTL works; (3) to mitigate the generalization gap caused by the introduction of multi-depot constraints, we introduce a targeted curriculum learning strategy that progressively exposes the model to increasingly more complex constraint interactions. Extensive experiments on 24 MDVRP variants (including 8 novel formulations) and 16 single-depot VRPs confirm the effectiveness of FiLMMeD, which consistently outperforms state-of-the-art baselines. Our code is available at: https://github.com/AJ-Correa/FiLMMeD/tree/main

### 🤖 AI 总结

**一句话总结**：Solving practical multi-depot vehicle routing problems (MDVRP) is a challenging optimization task central to modern logistics, increasingly driven by e-commerce. To address the MDVRP's computational c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FiLMMeD, Feature-wise, Linear, Modulation, Cross-Problem, Multi-Depot, Vehicle, Routing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.28102v1) | [下载PDF](https://arxiv.org/pdf/2604.28102v1.pdf)

---

