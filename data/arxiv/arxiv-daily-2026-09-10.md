# arXiv AI 论文日报 | 2026-09-10

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (5 篇)
- [cs.CV](#csCV) (14 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. JarvisGUI: Towards Cross-Device GUI Agents with Dynamic Task Composition](https://arxiv.org/abs/2609.10451v1)

**作者**：Zixiang Chen, Yuheng Lu, Zihao Cheng 等 11 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-09

### 📄 论文摘要

Real-world GUI usage frequently involves workflows that span multiple devices and platforms, requiring the transfer of intermediate results, maintenance of shared state, and coordination across heterogeneous environments. However, existing GUI benchmarks overwhelmingly evaluate agents on single-device, statically defined tasks, thus leaving such cross-device capabilities largely unexamined, resulting in an overly optimistic assessment of agents' readiness for real-world usage. We introduce JarvisGUI, a dynamic benchmark that evaluates GUI agents on cross-device workflows requiring coordinated interaction across heterogeneous platforms, including Android, Windows, and Ubuntu. Specifically, JarvisGUI formulates GUI tasks as input-output transformations under a lightweight type system, which allows us to automatically compose multi-step, cross-device workflows and dynamically evaluate agent performance within a unified framework. By evaluating agents in virtual environments spanning multiple operating systems, JarvisGUI reveals that state-of-the-art open-source GUI agents struggle with the state-transfer awareness, cross-platform contextual reasoning, and long-horizon dependency management required for real-world workflows, exposing a critical capability gap invisible to existing benchmarks.

### 🤖 AI 总结

**一句话总结**：Real-world GUI usage frequently involves workflows that span multiple devices and platforms, requiring the transfer of intermediate results, maintenance of shared state, and coordination across hetero...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, JarvisGUI, Towards, Cross-Device, GUI, Dynamic, Task, Composition

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10451v1) | [下载PDF](https://arxiv.org/pdf/2609.10451v1.pdf)

---

## [2. Fortunate Recall: Ontology-Driven Memory Lifecycle Management for Persistent Coherence in LLMs](https://arxiv.org/abs/2609.10413v1)

**作者**：Ansuman Mullick, Eray Tüzün  
**分类**：cs.AI  
**发布时间**：2026-09-09

### 📄 论文摘要

Current LLM memory systems treat all personal facts identically, so stores grow without bound while retrieval precision degrades. The core challenge is lifecycle management: which memories should persist, which should be replaced, and at what rate, conditioned on the behavioral type of each fact. Fortunate Recall (FR) is a composable policy layer that classifies personal facts into a 10+1 behavioral ontology and applies category-specific lifecycle policies (differential temporal decay, slot-key supersession, event-time validity, and category-aware retrieval routing) as deterministic functions over LLM-extracted metadata. FR-Bank, our infrastructure-independent implementation, reaches a 76.9% pass rate on LifecycleBench, a new 516-question temporal-disambiguation benchmark, ahead of Mem0, A-MEM, Memory-R1, and MemoryOS (61% to 70.5%), and 75.2% on the full LongMemEval-S under the canonical Wu et al. judge protocol, so lifecycle policies impose no measurable cost on standard retrieval. A pre-registered ablation locates the gains: replacing the typed layer with three generic lifecycle primitives leaves correctness statistically unchanged (-1.7pp, 95% CI [-6.0, +2.7]), so the generic lifecycle metadata carries the correctness advantage, while the behavioral ontology carries calibration, halving downstream confabulation (12.0% vs 24.2%, p<0.001). End-to-end, FR-Bank cuts confabulation from Mem0's 45.1% to 22.4% over answered queries and from 32.2% to 13.0% over all queries while answering more of them correctly (31.2% vs 18.6%); the ranking replicates on the open-weight Kimi K2.5. The decomposition transfers to BEAM, an independently built benchmark: 46.8% correct vs Mem0's 32.9% over 280 questions, with the ontology's benefit concentrated in contradiction resolution and saturating near seven policy clusters. The ontology, benchmark, and code are released.

### 🤖 AI 总结

**一句话总结**：Current LLM memory systems treat all personal facts identically, so stores grow without bound while retrieval precision degrades. The core challenge is lifecycle management: which memories should pers...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Fortunate, Recall, Ontology-Driven, Memory, Lifecycle, Management, Persistent, Coherence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10413v1) | [下载PDF](https://arxiv.org/pdf/2609.10413v1.pdf)

---

## [3. Cyber-Financial Contagion: Modeling the Propagation of an AI Vendor Compromise Through the Banking System](https://arxiv.org/abs/2609.10350v1)

**作者**：Alex Leytes  
**分类**：cs.AI, cs.CY, cs.LG  
**发布时间**：2026-09-09

### 📄 论文摘要

The banking system now depends on a small set of shared artificial intelligence vendors for fraud screening, credit decisioning, anti-money-laundering triage, customer analytics, and internal decision support. This paper studies how a compromise inside one of those vendors can propagate along a chain of operational, informational, and financial linkages until it triggers losses that look, from the outside, like a classical banking crisis. We build a four-layer heterogeneous network that couples AI vendors, financial institutions, interbank exposures, and customer accounts, and we propose CFC-Prop, a stochastic epidemic-and-clearing model that runs on that network. On a synthetic dataset with 60 vendors, 220 banks, roughly 2,500 vendor-bank service edges, and 1,400 interbank exposures, CFC-Prop reproduces the heavy-tailed loss distributions and the sharp dependence on patch latency that are consistent with prior cyber-financial evidence. We also train an early-warning model, CFC-GNN, that uses vendor-side incident telemetry and graph structure to flag high-cascade-risk vendors before impact. Across four baselines the proposed model reaches AUROC 0.82 and AUPRC 0.60 while keeping calibration errors bounded. We release the full code, synthetic data, and reproducible scripts. The results argue that cyber concentration among AI vendors is a first-order financial-stability problem and give supervisors a concrete quantitative tool for reasoning about it.

### 🤖 AI 总结

**一句话总结**：The banking system now depends on a small set of shared artificial intelligence vendors for fraud screening, credit decisioning, anti-money-laundering triage, customer analytics, and internal decision...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, an, Cyber-Financial, Contagion, Modeling, Propagation, Vendor, Compromise

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10350v1) | [下载PDF](https://arxiv.org/pdf/2609.10350v1.pdf)

---

## cs.CL

## [4. IdeaAMBIG: Benchmarking Implementation-Critical Gaps in Research-Idea Specifications](https://arxiv.org/abs/2609.10539v1)

**作者**：Yiling Ma, Yilun Zhao, Sihong Wu 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-09

### 📄 论文摘要

A research idea may be novel, coherent, and scientifically plausible, yet its proposed method may remain insufficiently specified for faithful implementation. We study the codification readiness of implementation-facing research-method specifications, defined by whether they provide sufficient methodological information for a competent implementer or coding agent to construct the intended method without unsupported assumptions. We construct evidence-grounded specifications and their supported resolutions from papers, codebases, issue threads, and reproduction artifacts. We introduce IdeaAMBIG, a benchmark of 660 evidence-grounded instances: 163 real-world gaps from reproducibility reports and GitHub issues, and 497 controlled synthetic gaps injected into codification-ready references. IdeaAMBIG evaluates three capabilities: codification-readiness assessment, defect localization, and clarification action generation. Defect localization receives only the specification, whereas clarification additionally receives the annotated defect. Across 13 LLMs, the best model achieves 9.6% Macro Defect Recovery Rate on real-world instances but 80.6% Macro Clarification Action Success Rate when given the defect. In an oracle study, supplying the gold resolution raises the downstream codification-ready rate from 14% to 98%. Across all evaluated models, defect localization is the main bottleneck, with stronger clarification given the defect.

### 🤖 AI 总结

**一句话总结**：A research idea may be novel, coherent, and scientifically plausible, yet its proposed method may remain insufficiently specified for faithful implementation. We study the codification readiness of im...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IdeaAMBIG, Benchmarking, Implementation-Critical, Gaps, Research-Idea, Specifications, research, idea

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10539v1) | [下载PDF](https://arxiv.org/pdf/2609.10539v1.pdf)

---

## [5. IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not Model Identifier](https://arxiv.org/abs/2609.10494v1)

**作者**：Blake Stenstrom, Charangan Vasantharajan, Brian Sathianathan  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-09-09

### 📄 论文摘要

Enterprises deploy systems, not checkpoints. Usable capability depends jointly on weights, serving route, precision, output contract, and harness, yet all 18 audited benchmarks score advertised model identifiers. We treat this as measurement error and give a protocol that makes it reportable. It has three parts. A gold-blind capability-binding preflight verifies that a route can execute the evaluation contract before any task reaches it; a reliability-inclusive first-pass scoring rule keeps failure in the score while keeping unsupported capability out; and adjudication is structurally score-blind. We call the protocol IB2 and release its algorithms, classification tables, request contract, and manifest schemas. Its reference instantiation, 128 locked tasks and 987 assertions over document, spreadsheet, chart, tool and database work, stays sealed: the procedure is the artifact, not the corpus. Across eleven systems, four results. Capability availability is measurable: two complete single-route runs on identical weights later failed distinct predicates of the finalized binding gate, while a third passed that gate before a fresh run. The advertised identifier exposed neither limit. Discrimination is not uniform: four of seven suites saturate under a six-system band, with the spread almost entirely from governed database work and multi-tab joins, so we report interval-backed resolution groups, not ranks; two of the nominal five-label output's four cuts fail multiplicity adjustment. Serving-arm choice moved one declared revision and precision from 77.38 to 82.54, paired interval [0.11,10.60], though the arms differ in access mode, harness generation, and the serving tool-call parser, and harness generation is a property of our evaluator, not any endpoint. Excluding failed responses from denominators changes the point ordering, so reliability inclusion changes a conclusion, not its wording.

### 🤖 AI 总结

**一句话总结**：Enterprises deploy systems, not checkpoints. Usable capability depends jointly on weights, serving route, precision, output contract, and harness, yet all 18 audited benchmarks score advertised model ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IBIB, Protocol, Measuring, Enterprise, Systems, Serving, Route, Not

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10494v1) | [下载PDF](https://arxiv.org/pdf/2609.10494v1.pdf)

---

## [6. Building Multilingual Bridges: Data Mixing as the Pillar of Generalization for In-Language Reasoning](https://arxiv.org/abs/2609.10445v1)

**作者**：Mehrnaz Mofakhami, Ananya Sahu, Alejandro R. Salamanca 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-09

### 📄 论文摘要

Reasoning language models have made substantial advances on a variety of complex tasks, yet their capabilities remain overwhelmingly English-centric: models primarily reason in English regardless of the language they are prompted in. This is inaccessible for non-English-speaking users, risks losing the intent of the original question, and forgoes knowledge more readily expressed in the target language. In this work, we advance L2 reasoning, the ability of a model to reason consistently in the language of the user's prompt, thus building an in-language bridge between the prompt and the answer. We approach this problem from a data-centric angle, investigating how to optimize data composition and scheduling in SFT for reasoning generalization. Building Tiny Aya L2-Thinker at 3.35B scale, we achieve an L2 reasoning rate above 93% across 60 languages on 6 benchmarks spanning math, commonsense reasoning, instruction following, open-ended generation, and cultural reasoning while keeping performance strong. We show the path to generalizing L2 reasoning to held-out languages goes through broader language coverage, readily available multilingual non-reasoning data, and a sufficient English reasoning backbone. These findings indicate that reasoning is a language-agnostic behavior that can be transferred across typologically diverse languages through careful data mixing and without requiring reasoning supervision in every target language. We release our model weights and multilingual reasoning data to support further research on accessible, in-language reasoning.

### 🤖 AI 总结

**一句话总结**：Reasoning language models have made substantial advances on a variety of complex tasks, yet their capabilities remain overwhelmingly English-centric: models primarily reason in English regardless of t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, of, Building, Multilingual, Bridges, Data, Mixing, Pillar

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10445v1) | [下载PDF](https://arxiv.org/pdf/2609.10445v1.pdf)

---

## [7. Can Foundation Models Moderate Online Content? Evaluating Instruction- vs. Example-Driven Policy Operationalization](https://arxiv.org/abs/2609.10410v1)

**作者**：Ayan Majumdar, Shounak Paul, Pushpdeep Singh 等 9 位作者  
**分类**：cs.CL, cs.AI, cs.CY  
**发布时间**：2026-09-09

### 📄 论文摘要

The growing complexity of content moderation policies presents a critical challenge for their consistent operationalization. While foundation models possess the basic capabilities needed to confront this challenge, whether they can reliably moderate online content remains an unanswered question. In this paper, we systematically compare two competing paradigms for Vision-Language Model (VLM) guidance: an instruction-driven approach where models reason from policy precepts, and an example-driven approach where they generalize from prior precedents. We ground this investigation in ModerationBench, a new benchmark of 4,000 manually annotated, in-the-wild posts from the Bluesky platform. Our experiments reveal that foundation models can substantially outperform Bluesky's deployed moderation system, nearly tripling its $F_1$ score (0.60 vs. 0.22) on Random Posts in the benchmark, with both instruction- and example-driven paradigms achieving comparable peak effectiveness. Our findings thus chart a path toward reliable and adaptable policy operationalization at scale.

### 🤖 AI 总结

**一句话总结**：The growing complexity of content moderation policies presents a critical challenge for their consistent operationalization. While foundation models possess the basic capabilities needed to confront t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Can, Foundation, Models, Moderate, Online, Content?, Evaluating, Instruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10410v1) | [下载PDF](https://arxiv.org/pdf/2609.10410v1.pdf)

---

## [8. Rosetta at AlexandriaX-2026: LoRA-Adapted NileChat for Context-Aware Dialectal Arabic Dialogue Translation](https://arxiv.org/abs/2609.10395v1)

**作者**：Nada Esmaeil, Fathima Rena, Sibi Subhash 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-09

### 📄 论文摘要

This paper describes the Rosetta system for Subtask 1 (Context-Aware English-to-Dialectal Arabic Dialogue Translation) of the AlexandriaX shared task, participating in both constrained and unconstrained tracks. The approach fine-tunes a LoRA adapter on NileChat-3B using structured system/user prompts that condition generation on dialect and dialogue context. For the unconstrained track, the adapter is additionally pretrained on MADAR and PADIC. Rosetta ranked 4th in the constrained track (spBLEU 26.10) and 5th in the unconstrained track (spBLEU 25.09). The experimental results demonstrate that external pretraining helps only two of thirteen dialects while slightly hurting overall performance, suggesting negative transfer.

### 🤖 AI 总结

**一句话总结**：This paper describes the Rosetta system for Subtask 1 (Context-Aware English-to-Dialectal Arabic Dialogue Translation) of the AlexandriaX shared task, participating in both constrained and unconstrain...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Rosetta, AlexandriaX-2026, LoRA-Adapted, NileChat, Context-Aware, Dialectal, Arabic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10395v1) | [下载PDF](https://arxiv.org/pdf/2609.10395v1.pdf)

---

## cs.CV

## [9. Guiding Image-to-3D Generation with Test-Time Partial Observations](https://arxiv.org/abs/2609.10531v1)

**作者**：Jerred Chen, Simon Weber, Ronald Clark  
**分类**：cs.CV  
**发布时间**：2026-09-09

### 📄 论文摘要

Image-to-3D models can generate visually compelling 3D assets from a single RGB image, but their geometry is often only loosely constrained by the available observations, limiting their use in applications that require geometric fidelity. In many real-world settings, however, partial geometric observations of the object may be available at test time. We introduce a training-free framework for incorporating such evidence into pretrained image-to-3D generative models without retraining or finetuning. To do this, we guide generation using a ray-consistent observation likelihood defined over the model's occupancy representation, combining surface occupancy and free-space evidence. Applied to SAM 3D and its multi-view extension, our approach substantially improves geometric fidelity across different levels of observability, as well as visual quality. Our results demonstrate that pretrained image-to-3D models can effectively integrate partial geometric observations through explicit test-time guidance, complementing their learned generative priors without modifying the underlying model.

### 🤖 AI 总结

**一句话总结**：Image-to-3D models can generate visually compelling 3D assets from a single RGB image, but their geometry is often only loosely constrained by the available observations, limiting their use in applica...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Guiding, Image-to-3D, Generation, Test-Time, Partial, Observations, models, can

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10531v1) | [下载PDF](https://arxiv.org/pdf/2609.10531v1.pdf)

---

## [10. Precision in Rice Variety Classification using Stacking-Based Ensemble Learning](https://arxiv.org/abs/2609.10524v1)

**作者**：Md. Masudul Islam, Galib Muhammad Shahriar Himel, Md. Golam Moazzam 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-09

### 📄 论文摘要

Rice, a staple food for a significant portion of the global population, exhibits remarkable diversity in its varieties, presenting substantial challenges for accurate identification by consumers, traders, and farmers. This complexity often facilitates fraudulent practices, such as the unauthorized mixing of rice types, which undermines quality and trust in the supply chain. Despite its critical importance, existing research falls short of providing robust and efficient methods for precise rice variety classification based on external characteristics like color, size, and texture. To address this gap, our study introduces a comprehensive rice variety identification framework designed to enhance transparency and quality assurance. We developed a stacked ensemble model tailored for rice variety classification and curated a comprehensive dataset comprising 20 rice varieties, each distinguished by unique visual attributes. The proposed approach achieved an unprecedented classification accuracy of 100%. Furthermore, we integrated our model into a mobile application, enabling even novice users to effortlessly identify rice varieties using grain images from a smartphone camera. These findings underscore the transformative potential of advanced machine learning techniques in mitigating fraudulent practices and ensuring stringent rice quality control. Our work holds significant implications for agricultural stakeholders, paving the way for automated crop identification systems and advancing precision agriculture practices.

### 🤖 AI 总结

**一句话总结**：Rice, a staple food for a significant portion of the global population, exhibits remarkable diversity in its varieties, presenting substantial challenges for accurate identification by consumers, trad...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Precision, Rice, Variety, Classification, Stacking-Based, Ensemble, Learning, staple

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10524v1) | [下载PDF](https://arxiv.org/pdf/2609.10524v1.pdf)

---

## [11. BrainTaskonomy: Learning How to Pretrain and What to Transfer in fMRI Foundation Models](https://arxiv.org/abs/2609.10518v1)

**作者**：Junfeng Xia, Wenhao Ye, Junxiang Zhang 等 6 位作者  
**分类**：cs.CV, q-bio.NC  
**发布时间**：2026-09-09

### 📄 论文摘要

fMRI foundation models increasingly aggregate heterogeneous data across brain states, cohorts, and acquisition settings, yet pretraining domains are commonly treated as a flat mixture and downstream tasks are adapted independently. We study whether measured learning relations can organize both stages without modifying the backbone. During pretraining, a lightweight Brain-DiT proxy estimates difficulty and directed facilitation across ten fMRI domains, yielding a priority-guided cumulative domain curriculum combined with high-to-low-noise timestep scheduling and joint consolidation. During adaptation, controlled first- and higher-order transfer across fifteen tasks constructs a directed taskonomy, from which budgeted integer programming (BIP) selects directly supervised source tasks and target-specific routes. The joint priority-domain and high-to-low-timestep curriculum reduces v-NMSE, PSD-NMSE, and FC-MSE by 6.5%, 16.3%, and 10.5%, respectively, relative to uniform sampling over both dimensions, and shows strong downstream performance across six in- and out-of-domain tasks. The taskonomy reveals asymmetric, target-dependent transfer, while exploratory sealed-test evaluation shows larger descriptive gains for BIP policies when higher-order route spaces are available than for matched random controls. Together, these findings support organizing fMRI pretraining and adaptation by measured learning relations rather than treating domains and tasks as independent flat sets.

### 🤖 AI 总结

**一句话总结**：fMRI foundation models increasingly aggregate heterogeneous data across brain states, cohorts, and acquisition settings, yet pretraining domains are commonly treated as a flat mixture and downstream t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BrainTaskonomy, Learning, How, Pretrain, What, Transfer, fMRI, Foundation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10518v1) | [下载PDF](https://arxiv.org/pdf/2609.10518v1.pdf)

---

## [12. Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts](https://arxiv.org/abs/2609.10498v1)

**作者**：Simon Khan, Laurent Gajny, Jennyfer Lecompte 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-09

### 📄 论文摘要

Recovering 3D human pose from monocular sports broadcasts remains challenging when players must be localized in a shared metric world coordinate system rather than only reconstructed relative to their own body. We introduce Field Converter, a geometry-initialized temporal residual framework for world-grounded 3D player pose estimation from calibrated soccer broadcasts. Our method first uses camera and pitch geometry to initialize the player root through ray-ground intersection, then predicts a temporal residual correction from pose, image, camera, and geometric cues. On match-disjoint evaluation sequences, residual refinement reduces root error from 49cm with geometry alone to 14cm with a frame-wise MLP and 10cm with a TCN, while a Transformer achieves a comparable 11cm. The resulting world-space MPJPE reaches 13.2cm, and ablations show that residual prediction clearly outperforms direct global-root regression while temporal context matters more than the specific temporal backbone. Failure analysis further identifies airborne motion as the main limitation of the ground-based geometric initialization.

### 🤖 AI 总结

**一句话总结**：Recovering 3D human pose from monocular sports broadcasts remains challenging when players must be localized in a shared metric world coordinate system rather than only reconstructed relative to their...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Field, Converter, Geometry-Initialized, Temporal, Residual, Refinement, World-Grounded, Player

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10498v1) | [下载PDF](https://arxiv.org/pdf/2609.10498v1.pdf)

---

## [13. Cross-Model Agreement as a Deployment-Time Reliability Signal for Automatic Polyp Segmentation](https://arxiv.org/abs/2609.10495v1)

**作者**：Siddharth Gupta, Jitin Singla  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-09-09

### 📄 论文摘要

In real-time colonoscopy, ground-truth annotations are unavailable at inference, so polyp segmentation models can fail silently. We propose Referee-Based Quality Estimation (RBQE), a reference-free framework measuring agreement between a primary segmentation model and an independently trained referee on the same image. RBQE is evaluated on a standardized 1,223-image external benchmark drawn from four public datasets, using four referee configurations chosen to separate two design axes: referee independence and architectural diversity. Using a common Agreement Dice descriptor, a same-architecture referee differing from the primary model only in random initialization already yields a useful reliability signal (ROC-AUC = 0.923), showing that independent training alone is sufficient. Cross-architecture referees improve further: SegFormer-B0 achieves the strongest performance (ROC-AUC = 0.960), significantly outperforming the same-architecture control and UNet++, and exceeding a representative Test-Time Augmentation baseline by 0.055 ROC-AUC under an identical protocol, whereas a prompt-coupled MedSAM referee underperforms despite maximal architectural diversity. Because empty-mask agreement is trivially separable, we also report a restricted evaluation excluding such cases: ROC-AUC falls to 0.876 (SegFormer-B0, 1,046 images) and 0.783 (same-architecture control, 975 images), yet RBQE's margin over both baselines widens on this identical subset. RBQE additionally increases the mean Dice of retained predictions as low-agreement cases are progressively rejected, supporting selective prediction, and requires only one additional deterministic referee forward pass at inference. Our study therefore supports cross-model agreement as a practical, interpretable reliability framework for automated polyp segmentation.

### 🤖 AI 总结

**一句话总结**：In real-time colonoscopy, ground-truth annotations are unavailable at inference, so polyp segmentation models can fail silently. We propose Referee-Based Quality Estimation (RBQE), a reference-free fr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Cross-Model, Agreement, Deployment-Time, Reliability, Signal, Automatic, Polyp

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10495v1) | [下载PDF](https://arxiv.org/pdf/2609.10495v1.pdf)

---

## [14. Artificial Intelligence Literacy and Sustainable Development: An Ethical Governance and Development Goals Framework](https://arxiv.org/abs/2609.10489v1)

**作者**：Md. Masudul Islam, Mirza Niaz Morshed, Md. Shafiqul Islam  
**分类**：cs.CV  
**发布时间**：2026-09-09

### 📄 论文摘要

AI literacy provides foundational competencies that support ethical, transparent, and sustainable technological development, although higher-order capabilities such as governance, critical evaluation, and strategic decision-making extend beyond basic literacy into advanced levels of AI competency. This study positions AI literacy as a governance capacity that complements and strengthens all 17 SDGs. It introduces a six-level taxonomy of artificial intelligence reasoning and ethics that extends traditional learning models by incorporating ethical judgement and strategic foresight. This taxonomy forms the foundation of an integrated framework linking education, governance, and sustainable development. A survey of 300 participants from diverse professional backgrounds within a national context which reveals strong technical awareness but limited ethical and governance readiness, highlighting critical gaps in public capacity to manage artificial intelligence responsibly. Findings show that ethical reasoning and reflective thinking are the strongest predictors of sustainable and trustworthy artificial intelligence use. The study proposed to embed literacy-based competencies into curricula, institutional policies, and governance mechanisms to accelerate equitable and responsible progress toward sustainable development goals

### 🤖 AI 总结

**一句话总结**：AI literacy provides foundational competencies that support ethical, transparent, and sustainable technological development, although higher-order capabilities such as governance, critical evaluation,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Artificial, Intelligence, Literacy, Sustainable, Development, Ethical, Governance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10489v1) | [下载PDF](https://arxiv.org/pdf/2609.10489v1.pdf)

---

## [15. AgroVisNet: A lightweight Convolutional Network and the BD-PlantDX Expert-Validated Benchmark for Radish, Potato and Pointed Gourd Disease Classification](https://arxiv.org/abs/2609.10469v1)

**作者**：Md. Abdullah Mandal, Saad Ahmed, Md. Khalid Syfullah  
**分类**：cs.CV  
**发布时间**：2026-09-09

### 📄 论文摘要

Automated plant disease diagnosis is increasingly deployed on farmer-held devices in regions where agronomic expertise is scarce and network connectivity is unreliable. Three obstacles limit its practical value: public benchmarks are dominated by a small set of non-native crops, region-specific datasets are rarely validated by domain experts, and the architectures that reach competitive accuracy carry parameter budgets that are unsuited to low-cost hardware. We propose AgroVisNet, a compact convolutional network trained from scratch, together with BD-PlantDX, an expert-validated benchmark of 12,432 field images spanning 12 classes of radish, potato and pointed gourd in healthy and diseased states, collected across the Bogura and Nilphamari districts of Bangladesh. AgroVisNet couples grouped bottleneck residual blocks carrying sequential channel and spatial attention with multi-scale depthwise blocks and a dual-pooling classification head, reaching 290,572 trainable parameters. On BD-PlantDX the model attains 99.52% test accuracy and 99.52% weighted F1, exceeding all six ImageNet-pretrained lightweight backbones evaluated under an identical protocol while using 8.7 to 16.8 times fewer parameters and 1.3 to 8.5 times fewer multiply-accumulate operations. Exported for deployment, the model quantises to a 0.46 MB full-integer network at a 0.22 percentage-point accuracy cost and classifies an image in 8.40 ms on a single CPU. Across five random seeds accuracy remains at 99.57 +- 0.10%, a ten-variant ablation isolates the contribution of each component, and the same architecture transfers without redesign to two independently collected datasets at 98.71% and 99.05% accuracy. Grad-CAM evidence indicates that predictions rest on lesion-bearing leaf regions rather than on background cues.

### 🤖 AI 总结

**一句话总结**：Automated plant disease diagnosis is increasingly deployed on farmer-held devices in regions where agronomic expertise is scarce and network connectivity is unreliable. Three obstacles limit its pract...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AgroVisNet, lightweight, Convolutional, Network, BD-PlantDX, Expert-Validated, Benchmark, Radish

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10469v1) | [下载PDF](https://arxiv.org/pdf/2609.10469v1.pdf)

---

## [16. Advanced Brain Tissue Imaging with Data-Consistent Diffusion Priors in Laminographic X-Ray Nanoimaging](https://arxiv.org/abs/2609.10456v1)

**作者**：Wenxuan Fang, Abraham L. Levitan, Ana Diaz 等 13 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-09

### 📄 论文摘要

Nanoscale imaging of mammalian brains is critical for connectomics. X-ray laminography enables high-throughput imaging of extended, plate-like biological specimens. However, the tilted acquisition geometry leads to incomplete Fourier-space coverage, giving rise to a missing-cone of information. Conventional reconstruction methods cannot recover unmeasured information within the cone, resulting in artifacts that distort fine brain structures. While resolving these requires modeling 3D structure, direct 3D deep learning approaches are limited by data scarcity and computational cost. Here we introduce LUCID (Laminography with Unified Consistent Diffusion), a framework that combines multi-view diffusion priors with projection-domain data consistency. LUCID integrates complementary 3D structural information while enforcing strict alignment with the laminography forward model. On simulated datasets, LUCID substantially improves spatial fidelity and restores missing Fourier components, outperforming baseline methods. Applied to experimental laminography data, LUCID generalizes robustly despite being trained exclusively on fully sampled tomographic volumes, and effectively recovers unmeasured Fourier information.

### 🤖 AI 总结

**一句话总结**：Nanoscale imaging of mammalian brains is critical for connectomics. X-ray laminography enables high-throughput imaging of extended, plate-like biological specimens. However, the tilted acquisition geo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Advanced, Brain, Tissue, Imaging, Data-Consistent, Priors, Laminographic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10456v1) | [下载PDF](https://arxiv.org/pdf/2609.10456v1.pdf)

---

## [17. Enhanced Deformable Convolution with Center-invariant Offset and Edge-aware Mask](https://arxiv.org/abs/2609.10387v1)

**作者**：Yixiao Li, Xiaoyuan Yang, Jin Jiang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-09

### 📄 论文摘要

Deformable convolution networks have recently become popular for many computer vision tasks, especially for semantic segmentation, because of their exceptional capabilities in dynamic spatial modeling. However, due to the dense deformable offsets and the lack of longer-range dependencies, they can not fully adopt proper and precise deformations for feature representations. To tackle the issues, in this paper, we propose Enhanced Deformable ConvNets (EDCN) for semantic segmentation. Specifically, a novel Enhanced Deformable Convolution (EDC) is exploited in the decoder, which integrates the Center-invariant Offset Module (COM) and Edge-aware Mask Module (EMM). The COM employs larger kernels and eliminates deformations at the kernel center, obtaining offsets that are more in line with the target from richer spatial information. Concurrently, the EMM obtains the significance of image content via Sobel edge detection, then selectively applies deformations based on the content significance, minimizing unnecessary deformations associated with relatively less important information, thereby avoiding impact from less informative regions. Experiments show that EDC outperforms state-of-the-art deformable convolution variants, including Deformable ConvNets V1-V4 and Entire Deformable ConvNets, across mainstream segmentation datasets with various decoder settings. Moreover, ablation studies confirm the effectiveness of each component. In addition, visualizations illustrate that EDC enhances spatial adaptation and target focus. We further analyze the extendibility of EDC to larger kernels on the image classification benchmark. Code will be publicly released.

### 🤖 AI 总结

**一句话总结**：Deformable convolution networks have recently become popular for many computer vision tasks, especially for semantic segmentation, because of their exceptional capabilities in dynamic spatial modeling...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Enhanced, Deformable, Convolution, Center-invariant, Offset, Edge-aware, Mask, networks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10387v1) | [下载PDF](https://arxiv.org/pdf/2609.10387v1.pdf)

---

## [18. Shape-guided Gaussian Splatting for Sparse-View X-ray 3D Reconstruction](https://arxiv.org/abs/2609.10376v1)

**作者**：Pranav Poudel, Florence Dell'Aniello Picard, Nairouz Shehata 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-09

### 📄 论文摘要

Sparse-view X-ray 3D reconstruction is essential for reducing radiation exposure, but recovering a density field from a handful of X-ray projections is severely ill-posed. Recently, 3D Gaussian Splatting has achieved state-of-the-art performance in sparse-view reconstruction by representing the volume using explicit, optimized primitives, but it requires dozens of projected views. With fewer views, reconstruction quality degrades severely since the explicit primitives are optimized freely without any anatomical information. Anatomical structures, in contrast, share similar geometry and density across a population. Their variations are bounded within a limited range that statistical shape models can capture. This paper proposes a shape-guided Gaussian splatting framework for sparse-view X-ray 3D reconstructions. Our contribution lies in driving Gaussian positions toward anatomically valid configurations, alongside atlas-based density regularization. Our method ensures anatomically consistent reconstruction and improves PSNR by 2.83 dB over a state-of-the-art Gaussian splatting baseline with as few as 5 views. Code Available: https://github.com/polyshape-lab/ShapeGuidedGaussian

### 🤖 AI 总结

**一句话总结**：Sparse-view X-ray 3D reconstruction is essential for reducing radiation exposure, but recovering a density field from a handful of X-ray projections is severely ill-posed. Recently, 3D Gaussian Splatt...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Shape-guided, Gaussian, Splatting, Sparse-View, X-ray, Reconstruction, essential

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10376v1) | [下载PDF](https://arxiv.org/pdf/2609.10376v1.pdf)

---

## [19. PACE: Perceived-Latency-Aware Cascading Service Routing and Filler Control for QoE-Efficient Retrieval-Augmented Dialogue Serving](https://arxiv.org/abs/2609.10372v1)

**作者**：Lin Huang, Yujuan Tan, Weisheng Li 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.RO  
**发布时间**：2026-09-09

### 📄 论文摘要

We present the PACE, a framework for retrieval-augmented dialogue serving that formalizes Perceived Time-to-First-Response (PTFR) as a QoE objective and minimizes it under quality/cost constraints. Unlike prior work on cascaded routing, semantic caching, or adaptive retrieval, PACE jointly controls which answer source composes the response and what fills the waiting window. Deployed on a humanoid-robot sales service, it combines three mechanisms: a load-adaptive cascading router, a joint path-filler controller, and volatility-aware cache admission. On 75k CarQA requests, the cascade halves pure-LLM PTFR at P95 (0.29 vs 0.53s at c16). The adaptive controller reaches 0.41s P95, outperforming RAG by 2.4 times at high load with equal quality. The filler controller cuts calls by 94% with zero conflict. Volatility-aware admission reduces stale answers from 86% to 0%. A gating rule ensures the controller never worse than the baseline, with exposure bounded by one hold period. This is the first quantification of filler-answer conflict risk in deployed services.

### 🤖 AI 总结

**一句话总结**：We present the PACE, a framework for retrieval-augmented dialogue serving that formalizes Perceived Time-to-First-Response (PTFR) as a QoE objective and minimizes it under quality/cost constraints. Un...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PACE, Perceived-Latency-Aware, Cascading, Service, Routing, Filler, Control, QoE-Efficient

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10372v1) | [下载PDF](https://arxiv.org/pdf/2609.10372v1.pdf)

---

## [20. Beyond Weak Labels: Prompt-Guided Local Refinement for Weakly Supervised Water Segmentation in High-Resolution Multispectral Imagery](https://arxiv.org/abs/2609.10371v1)

**作者**：Muhammad Farhan Humayun, Mohammad Imangholiloo, Afifah Shah 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-09

### 📄 论文摘要

High-resolution water mapping supports environmental monitoring and related applications, but accurate pixel-level labels are difficult and costly to produce. Official hydrographic vectors provide scalable weak supervision, but they contain artifacts like boundary noise, temporal mismatch, and omissions of small water structures. We propose a two-stage framework for weakly supervised water segmentation in high resolution multispectral imagery. Stage 1 learns initial masks from rasterized vector pseudo-labels, and Stage 2 converts these masks into structured component-wise prompts for localized refinement. On a manually corrected validation set, refinement improves SegFormer-B0 from 0.9509 to 0.9535 IoU and U-Net from 0.9408 to 0.9486 IoU, with corresponding F1 gains from 0.9749 to 0.9762 and 0.9695 to 0.9736. It leads to sharper shorelines, reduced boundary spillover, and better thin-structure delineation. The results indicate that prompt-guided refinement can improve pseudo-label-based water segmentation by targeting local errors that are poorly captured by global training supervision.

### 🤖 AI 总结

**一句话总结**：High-resolution water mapping supports environmental monitoring and related applications, but accurate pixel-level labels are difficult and costly to produce. Official hydrographic vectors provide sca...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Weak, Labels, Prompt-Guided, Local, Refinement, Weakly, Supervised

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10371v1) | [下载PDF](https://arxiv.org/pdf/2609.10371v1.pdf)

---

## [21. SceneHI: High-Resolution 3D-Consistent Scene Texturing with Controllable Illumination](https://arxiv.org/abs/2609.10363v1)

**作者**：Athanasios Tragakis, Marco Aversa, Daniela Ivanova 等 7 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-09-09

### 📄 论文摘要

SceneHI is a framework that lifts high-resolution, illumination-aware priors from 2D diffusion models to perform 3D texture synthesis. It is the first to demonstrate that high-resolution textures, previously limited to 2D synthesis, can be generated directly on 3D objects without model fine-tuning or optimization. Designed for complex, multi-object environments, SceneHI uniquely combines 3D-consistency, high-resolution fidelity, and physically plausible baked shadows within a single generative pipeline. To enforce strict geometric coherence, we introduce an exact analytical pixel-to-texel mapping that aligns diffusion trajectories across multiple viewpoints. We utilize High-Resolution Latent Textures (HRLTs) as a persistent canvas for gradually denoised textures, while camera views perform the denoising steps in latent pixel space. This ensures a shared base texture that can be subsequently refined to high resolution without compromising multi-view consistency. Finally, a light-aware generative pass embeds realistic geometry-consistent shadows directly into the atlases, bridging the gap to production workflows. SceneHI achieves high visual fidelity while reducing generation time by 80% compared to existing scene-level methods.

### 🤖 AI 总结

**一句话总结**：SceneHI is a framework that lifts high-resolution, illumination-aware priors from 2D diffusion models to perform 3D texture synthesis. It is the first to demonstrate that high-resolution textures, pre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SceneHI, High-Resolution, 3D-Consistent, Scene, Texturing, Controllable, Illumination, framework

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10363v1) | [下载PDF](https://arxiv.org/pdf/2609.10363v1.pdf)

---

## [22. Spot-the-shift: Evaluating Grounded Image Difference Captioning of Long-term Changes](https://arxiv.org/abs/2609.10356v1)

**作者**：Benedetta Liberatori, Nermin Samet, Paolo Rota 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-09

### 📄 论文摘要

Long-term change understanding from images of the same place revisited over time is a challenging task with applications in map maintenance and urban infrastructure monitoring. Prior work addresses it either through pixel-level prediction or difference captioning, neither of which is sufficient to reliably measure how well models detect and describe such changes. We introduce SPOT-THE-SHIFT, a human-verified benchmark for grounded image difference captioning of long-term changes in real-world driving scenes. Our benchmark provides natural language captions and spatial masks for structural changes across each image pair. We further propose an evaluation protocol that reliably assesses models' captioning ability, validated through human studies. Benchmarking state-of-the-art MLLMs, we find that models struggle with the fine-grained multi-image spatial capability required for this task. Finally, we develop a synthetic data generation pipeline that improves an off-the-shelf MLLM without sacrificing general capabilities.

### 🤖 AI 总结

**一句话总结**：Long-term change understanding from images of the same place revisited over time is a challenging task with applications in map maintenance and urban infrastructure monitoring. Prior work addresses it...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Spot-the-shift, Evaluating, Grounded, Image, Difference, Captioning, Long-term

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10356v1) | [下载PDF](https://arxiv.org/pdf/2609.10356v1.pdf)

---

## cs.LG

## [23. A positive resolution of the gap-entropy conjecture](https://arxiv.org/abs/2609.10529v1)

**作者**：P. M. Aronow, Nathan Kallus, Patrick Lopatto  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-09-09

### 📄 论文摘要

We prove the gap-entropy conjecture for fixed-confidence best-arm identification with independent unit-variance Gaussian arms, means in $[0,1]$, and a unique optimal arm. For each suboptimal arm $i$, let $Δ_i=μ_*-μ_i$ be its gap from the optimal mean, and write $H=\sum_{i\ne *}Δ_i^{-2}$. Let $p_r$ be the fraction of $H$ contributed by arms with $2^{-(r+1)}<Δ_i\le2^{-r}$, and let $\mathrm{Ent}(I)=\sum_{r:p_r>0} p_r\log(1/p_r)$. Among all algorithms that identify the optimal arm with probability at least $1-δ$ on every Gaussian instance, the optimal expected number of samples on a given instance, averaged over all permutations of the arm labels, is within absolute constant factors of $H(\log(1/δ)+\mathrm{Ent}(I))$. Moreover, there is an algorithm, independent of the instance, whose expected number of samples is bounded by a constant multiple of this quantity plus $g^{-2}\log\log(e^e/g)$, where $g=\min_{i\ne *}Δ_i$ is the gap to the closest competitor.

### 🤖 AI 总结

**一句话总结**：We prove the gap-entropy conjecture for fixed-confidence best-arm identification with independent unit-variance Gaussian arms, means in $[0,1]$, and a unique optimal arm. For each suboptimal arm $i$, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, We, positive, resolution, gap-entropy, conjecture, prove, fixed-confidence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10529v1) | [下载PDF](https://arxiv.org/pdf/2609.10529v1.pdf)

---

## [24. Quantum Feature Engineering for Credit Default Prediction: When and Why IQP Circuits Help Linear Classifiers](https://arxiv.org/abs/2609.10505v1)

**作者**：Menachem Finkelstein, Diana Legziel Levy, Zohar Yakhini 等 4 位作者  
**分类**：cs.LG, quant-ph  
**发布时间**：2026-09-09

### 📄 论文摘要

Credit default prediction is a tabular classification problem in which modest gains in F1 translate directly into reduced financial exposure. We ask whether Instantaneous Quantum Polynomial-time (IQP) circuits can produce features that improve a classifier over both its raw classical baseline and Kernel PCA - the strongest unsupervised classical non-linear alternative - at an equal feature budget. The dataset provides 23 financial attributes per client; for an n-qubit circuit we select n of them, encode each as a rotation angle, and read 2n expectation values back out as new features. The motivation for using a quantum circuit is computational: an n-qubit IQP circuit runs in constant depth and encodes feature correlations in a 2^n-dimensional Hilbert space, whereas classical simulation of its exact output statistics scales exponentially in n. Using the UCI Default of Credit Card Clients dataset and five-fold cross-validation, we find that appending 16 IQP features (n = 8 qubits) to a Logistic Regression model raises F1 from 0.462 to 0.517 (+0.055, p < 0.0001). Kernel PCA, the next-best method, reaches only 0.493 at the same feature count; the gap survives Benjamini-Hochberg correction across 12 tests (p = 0.00007). No other classifier - Random Forest, SVM, XGBoost, or k-NN - benefits, which points to a linear-expressivity mechanism rather than a generic improvement. We also show that how the 8 input features are chosen matters: Random Forest importance-guided selection reaches F1 = 0.523, while encoding maximally uncorrelated features drops it to 0.496, demonstrating that the circuit amplifies informative structure rather than creating it from scratch.

### 🤖 AI 总结

**一句话总结**：Credit default prediction is a tabular classification problem in which modest gains in F1 translate directly into reduced financial exposure. We ask whether Instantaneous Quantum Polynomial-time (IQP)...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Quantum, Feature, Engineering, Credit, Default, Prediction, When, Why

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10505v1) | [下载PDF](https://arxiv.org/pdf/2609.10505v1.pdf)

---

## [25. Learning with Covariance Matrices: Principal Component Analysis Meets Learning with Graphs](https://arxiv.org/abs/2609.10490v1)

**作者**：Saurabh Sihag, Andrea Cavallo, Elvin Isufi 等 5 位作者  
**分类**：cs.LG, eess.SP  
**发布时间**：2026-09-09

### 📄 论文摘要

This feature article provides an overview of the theoretical foundations for coVariance neural networks (VNNs), i.e., graph neural networks (GNNs) operating on covariance matrices as graphs. Covariance matrices are ubiquitous across domains, and hence, the deployment of GNNs often leverages graphs of pairwise statistical dependencies. Existing theoretical contributions on GNNs consider abstract graph representations and cannot accommodate the data-driven nuances associated with covariance matrices. This tutorial brings into focus various novel theoretical insights via mathematical analyses of VNNs that have broad signal processing implications, including: (i) a conceptual equivalence between VNNs and principal component analysis (PCA)-based information processing; (ii) refined stability bounds on predictive outcomes in the presence of finite sample-induced covariance matrix perturbations; and (iii) refined characterization of transferability of VNNs across multiscale datasets. The theoretical insights discussed herein provide the underlying principles and justification towards adopting VNNs over workhorse PCA-based learning pipelines, in applications where covariance matrices are useful descriptors of data structure. We also convey how impact of these foundational advances permeates to \textit{principled} designs and applications of learning methods across broad domains where covariance matrices emerge. Notably, we elucidate the conceptual insights facilitated by VNNs to the specific task of characterizing brain age gap for neurodegenerative conditions using neuroimaging datasets, a timely problem in computational neuroscience. Broader impacts to other application domains are discussed as well.

### 🤖 AI 总结

**一句话总结**：This feature article provides an overview of the theoretical foundations for coVariance neural networks (VNNs), i.e., graph neural networks (GNNs) operating on covariance matrices as graphs. Covarianc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Covariance, Matrices, Principal, Component, Analysis, Meets, Graphs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10490v1) | [下载PDF](https://arxiv.org/pdf/2609.10490v1.pdf)

---

## [26. Nonmaximal sums of maximally monotone operators under Rockafellar's constraint qualification](https://arxiv.org/abs/2609.10487v1)

**作者**：Weifeng Yang  
**分类**：cs.LG, math.FA  
**发布时间**：2026-09-09

### 📄 论文摘要

We construct counterexamples to Rockafellar's sum conjecture in which two maximally monotone operators satisfy the interior-domain condition but their sum is not maximally monotone. We give one counterexample on $c_0$ and another on $\ell^1$ with its usual norm. We establish a general construction theorem that computes the entire monotone polar of a class of graphs, gives a necessary and sufficient condition for their maximal monotonicity, and shows how a positive rank-one perturbation yields a nonmaximal sum under this condition. We verify the theorem's hypotheses and its maximality criterion on $c_0$, thereby obtaining a counterexample to the conjecture. Furthermore, we construct a bounded linear surjection from $\ell^1$ onto $c_0$ and use it to obtain the counterexample on $\ell^1$.

### 🤖 AI 总结

**一句话总结**：We construct counterexamples to Rockafellar's sum conjecture in which two maximally monotone operators satisfy the interior-domain condition but their sum is not maximally monotone. We give one counte...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Nonmaximal, sums, maximally, monotone, operators, under, Rockafellar's

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10487v1) | [下载PDF](https://arxiv.org/pdf/2609.10487v1.pdf)

---

## [27. Semigroup-JEPA: Latent Dynamics Consistency for Zero-Shot Physics Generalization](https://arxiv.org/abs/2609.10464v1)

**作者**：Andy Zeyi Liu, Haoran Sun, Lucas Baker 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-09-09

### 📄 论文摘要

Joint-Embedding Predictive Architecture (JEPA) world models learn a compact latent representation of the world that supports prediction and planning, but their capability to learn physics and generate physically realistic dynamics remains hitherto untested. In this work, we introduce SemiGroup-JEPA (SG-JEPA), which extends the LeWorldModel framework by supplying the parameter governing the physics to the temporal model via action-conditioning and jointly training an encoder and predictor through an autoregressive latent rollout. To evaluate the model's ability to generalize out of distribution, we design dynamical tasks under different gravitational fields that, despite obeying the same physical law, exhibit qualitatively different dynamics, ranging from floating motion in weak gravitational fields to rapid bouncing in strong ones. In contrast to DINO-WM, SG-JEPA reduces open-loop prediction error by up to 2 times on two-dimensional datasets, and increases control success rate up to 2.5 times for three-dimensional robotic datasets, for which we train independent diffusion policies. To explain this advantage, we develop a linear feature model that separates local law-conditioned error from its recursive amplification under rollout. Guided by this model, we find that back-propagating the multi-step rollout loss into the representation trains the encoder to keep the features that the predictor can carry forward, and that those are the features the dynamics depend on, so most of the gain comes from the encoder learning better features rather than from the predictor learning better dynamics. See project page at https://sg-jepa.github.io.

### 🤖 AI 总结

**一句话总结**：Joint-Embedding Predictive Architecture (JEPA) world models learn a compact latent representation of the world that supports prediction and planning, but their capability to learn physics and generate...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Semigroup-JEPA, Latent, Dynamics, Consistency, Zero-Shot, Physics, Generalization, Joint-Embedding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10464v1) | [下载PDF](https://arxiv.org/pdf/2609.10464v1.pdf)

---

## [28. Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs](https://arxiv.org/abs/2609.10439v1)

**作者**：Ravi Ranjan, Olivera Kotevska, Agoritsa Polyzou  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-09

### 📄 论文摘要

Large Language Models (LLMs) can memorize and reproduce sensitive, copyrighted, or otherwise undesirable training content, creating privacy, safety, and regulatory concerns. Machine unlearning offers a practical alternative to full retraining, but many existing methods apply broad or fixed parameter updates that can degrade utility and remain brittle under deployment changes such as post-training quantization, where forgotten knowledge may partially re-emerge. We propose Forgetting Only What Matters via Unlearning Layers (FOM-UL), a layer-level unlearning framework that selects transformer layers using a forget-to-retain significance score. This score identifies layers with high influence on the forget set and low sensitivity to the retain set, allowing FOM-UL to concentrate updates where they are most effective while leaving most of the model unchanged. This targeted update strategy improves the forgetting-utility trade-off and provides an empirical path toward quantization-resilient unlearning by reducing the chance that small, diffuse updates are erased by low-bit rounding. Across TOFU, KnowUnDo, and MUSE-style evaluations, FOM-UL reduces residual memorization compared with strong GA, NPO, KLD, SURE, ReLearn, and LUNAR-based baselines while preserving retain-set utility close to the vanilla model. Under 8-bit and 4-bit post-training quantization, FOM-UL maintains stronger memorization suppression and utility preservation than competing methods, and adversarial prompt evaluations show lower recovery of forgotten content. Overall, FOM-UL provides an efficient unlearning strategy that improves targeted forgetting, utility preservation, and deployment robustness without claiming formal guarantees of erasure.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) can memorize and reproduce sensitive, copyrighted, or otherwise undesirable training content, creating privacy, safety, and regulatory concerns. Machine unlearning offers ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Forgetting, Only, What, Matters, Layer-Selective, Unlearning, toward, Robust

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10439v1) | [下载PDF](https://arxiv.org/pdf/2609.10439v1.pdf)

---

## [29. OmniMed-FL: A Robust Multimodal Federated Learning Framework for Clinical Diagnosis](https://arxiv.org/abs/2609.10364v1)

**作者**：Ayush Debnath, Ruelia Saha, Sudip Misra  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-09

### 📄 论文摘要

Simultaneous assessment of medical imaging and patient records is often required in clinical diagnosis. However, standard machine learning algorithms cannot analyze these data types together. Meanwhile, compliance with HIPAA and GDPR can constrain centralized aggregation of sensitive patient data. This leaves a crucial void of secure fusion of visual and textual context across distant networks. Thus, we present OmniMed-FL, a controlled systems study of multimodal federated learning for five-class clinical condition classification (Normal, Pneumonia, COVID-19, Pleural Effusion, Cardiomegaly). Our proxy corpus pairs 3,000 public chest radiographs with 3,000 class-conditioned synthetic notes, matched by class, not by patient. The framework benchmarks eight fusion strategies, three initializations, four missing-text imputation rules, and matched federated baselines under non-IID Dirichlet partitioning across 3 to 20 hospital clients. As all notes are synthetic and pairing is not patient-level, these are descriptive proxy comparisons, not estimates of diagnostic performance or deployment readiness. Within those limits with clients ($K=5$) and severe skew ($α=0.1$), local-only training achieves a macro-F1 score of 0.297, FedAvg achieves $0.662\pm0.074$, FedProx $0.737\pm0.085$, a matched FedMME-style one-shot ensemble $0.647\pm0.080$, and our SCAFFOLD-AdamW adaptation $0.070\pm0.015$, the 0.075 FedProx-FedAvg gap falling inside the wider of the two two-seed standard deviations. Over a $4\times3$ grid, label skew costs up to 0.27 F1 whereas a near-sevenfold client increase costs at most 0.10, while bidirectional volume grows linearly to 183.5 GiB at $K=20$. Multimodal fusion leads on both corpora, scoring 0.956 against 0.934 for text and 0.664 for images on the synthetic corpus and 0.906 against 0.880 and 0.737 on the radiograph corpus, for $2.3\times$ the model state of text alone.

### 🤖 AI 总结

**一句话总结**：Simultaneous assessment of medical imaging and patient records is often required in clinical diagnosis. However, standard machine learning algorithms cannot analyze these data types together. Meanwhil...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OmniMed-FL, Robust, Multimodal, Federated, Learning, Framework, Clinical, Diagnosis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10364v1) | [下载PDF](https://arxiv.org/pdf/2609.10364v1.pdf)

---

## [30. A Later Test Set Is Not a New Domain: Pretraining Familiarity Survives a Contamination-Free Hold-Out](https://arxiv.org/abs/2609.10357v1)

**作者**：Mahdi Naser Moghadasi, Faezeh Ghaderi  
**分类**：cs.LG  
**发布时间**：2026-09-09

### 📄 论文摘要

Time-series foundation models are evaluated almost exclusively on public archives that predate them, so a strong score cannot be separated from having seen the test set during pretraining. The obvious remedy is a hold-out that postdates the models. We build one: thirteen forecasters -- four classical, three trained per dataset, six pretrained -- on seven groups drawn from five domains, every observation published after the last model was released, and every dataset rebuildable without an API key. Under this protocol pretrained models win 5 of 7 groups, lose one to a Theta baseline, and on daily exchange rates are indistinguishable from a seasonal naive forecast, along with every other method tested.   We then ask what separates the wins from the losses, and report a negative result: the two intrinsic properties one would reach for -- seasonal strength and spectral entropy, measured on the input window -- do not account for the pattern, and seasonal strength is if anything negatively associated with the advantage. What does track it is corpus familiarity. Our largest gain (28% lower MASE than the best classical method, on weekly Wikipedia pageviews) falls on Wikipedia pageviews, the domain TimesFM's authors describe as the bulk of its pretraining corpus, at the same granularities and differing only in time window. Within the pretrained family, where every model forecasts identical series so that series difficulty cancels, the TimesFM family outranks the Chronos family by -0.53 ranks on Wikipedia against -0.09 everywhere else (1,500 vs. 754 series, Mann-Whitney p < 1e-5). We conclude that a temporal hold-out removes memorisation of a window but not familiarity with a domain, that benchmarks therefore need domain hold-outs stated relative to disclosed corpora, and that the practitioner's question is less which model is better than whether their domain is one the model was raised on.

### 🤖 AI 总结

**一句话总结**：Time-series foundation models are evaluated almost exclusively on public archives that predate them, so a strong score cannot be separated from having seen the test set during pretraining. The obvious...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Later, Test, Set, Not, New, Domain, Pretraining, Familiarity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.10357v1) | [下载PDF](https://arxiv.org/pdf/2609.10357v1.pdf)

---

