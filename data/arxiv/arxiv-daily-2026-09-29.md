# arXiv AI 论文日报 | 2026-09-29

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (10 篇)
- [cs.CL](#csCL) (4 篇)
- [cs.LG](#csLG) (11 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. FinAutoRubric: Expert-Guided Automatic Rubric Generation for Evaluating Financial Research Agents](https://arxiv.org/abs/2609.35744v1)

**作者**：Hoyoung Lee, Suyeol Yun, Jack Haverty 等 20 位作者  
**分类**：cs.AI, q-fin.CP  
**发布时间**：2026-09-28

### 📄 论文摘要

Evaluating finance research agents requires rubrics that reflect expert standards and fix the values correct as of an information cutoff. Expert-reviewed finance benchmarks rely on fixed, per-item rubrics, which are costly to extend and cannot encode each institution's own standard. In FinAutoRubric, experts specify reusable evaluation guidance, while agents and code carry out query-specific rubric generation, review, and validation. This expert guidance governs every agent, as prompts and as rules that code enforces, and a Task Bank of reusable criteria carries it across tasks. In long-horizon loops that follow the expert guidance, a writer agent researches every expected value and a reviewer agent verifies it, and failures escalate to a human. On three expert-authored finance benchmarks, its rubrics track expert scoring as closely as the strongest evaluated generator while stating the expert rubric's expected value for more criteria, their scores agree with human grading, and in-house analysts prefer them in a blind review. The released 100-query FinAutoRubric Benchmark, built from in-house analysts' key questions across 78 tasks and eight asset classes, shows that rubrics from an earlier model generation still leave headroom for a later one.

### 🤖 AI 总结

**一句话总结**：Evaluating finance research agents requires rubrics that reflect expert standards and fix the values correct as of an information cutoff. Expert-reviewed finance benchmarks rely on fixed, per-item rub...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FinAutoRubric, Expert-Guided, Automatic, Rubric, Generation, Evaluating, Financial, Research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35744v1) | [下载PDF](https://arxiv.org/pdf/2609.35744v1.pdf)

---

## [2. Failure-Transparent Agents: Benchmarking Post-Failure Reporting in Tool-Using Language Models](https://arxiv.org/abs/2609.35732v1)

**作者**：Junru Zhu, Shiming Xie, Aime Lu Fan Chen 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-28

### 📄 论文摘要

Tool-using agents can fail twice: a required tool can fail, and the agent can then report success without the evidence needed to justify it. Existing benchmarks often entangle this reporting failure with tool selection, recovery, and environment dynamics. We introduce Failure-Transparent Agents (FTA), a controlled benchmark that fixes the failed observation and required evidence state before generation, making post-failure claims directly auditable. FTA contains 100 tasks with deterministic failure traces spanning five failure families, a neutral control, and four user-pressure conditions, and evaluates unsupported claims alongside useful recovery. Across six models, three response policies, and 3,600 human-annotated responses, false-success rates are 22.8% under the baseline policy, 9.3% with a transparency instruction, and 0.8% with a structured evidence contract. Fabricated-detail rates decrease from 28.3% to 14.3% and 0.8%, while useful responses increase from 74.9% to 89.2% and 98.8%, respectively. The tested evidence-contract policy is associated with substantially lower post-failure reporting errors while useful-response rates remain high within this blocked-task benchmark.

### 🤖 AI 总结

**一句话总结**：Tool-using agents can fail twice: a required tool can fail, and the agent can then report success without the evidence needed to justify it. Existing benchmarks often entangle this reporting failure w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Failure-Transparent, Benchmarking, Post-Failure, Reporting, Tool-Using, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35732v1) | [下载PDF](https://arxiv.org/pdf/2609.35732v1.pdf)

---

## [3. Reinforcing Agentic Creativity in Scientific Ideation with Night Science](https://arxiv.org/abs/2609.35706v1)

**作者**：Priyanka Kargupta, Silviu Cucerzan, Shweti Mahajan 等 7 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-09-28

### 📄 论文摘要

Large language models (LLMs) excel at structured, verifiable tasks, but their low-entropy bias can produce homogeneous and predictable outputs, limiting their utility for open-ended scientific ideation. Effective discovery, however, spans a broader creative spectrum: from structured day science to loosely structured, serendipitous night science that reaches ideas beyond those typically considered. We introduce AI Night-Scientist, an agentic framework that uses reinforcement learning to teach models when and how to depart from predictable reasoning. Grounded in cognitive science, we model creativity along three axes: action (what to do and how creatively), process (when to explore versus exploit), and outcome (the novelty and usefulness of the resulting idea). We use these axes to train models with GRPO, exposing them to varying degrees and forms of creativity throughout training. This produces substantially more diverse scientific proposals, expanding the range of research directions by 27.8% and contribution types by 14.9% over the base model. It also improves predicted citation impact by up to 32.0 percentage points and originality by 66.2 points. These gains cannot be reproduced by simply increasing decoding temperature; instead, we find that semantic guidance specifying what kind of creativity to pursue is critical. Overall, our results suggest that creativity is a learnable, multi-level ability that can be shaped to help researchers reach ideas beyond those typically explored by LLMs.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) excel at structured, verifiable tasks, but their low-entropy bias can produce homogeneous and predictable outputs, limiting their utility for open-ended scientific ideatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Reinforcing, Agentic, Creativity, Scientific, Ideation, Night, Science, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35706v1) | [下载PDF](https://arxiv.org/pdf/2609.35706v1.pdf)

---

## [4. Report: Progressive Disclosure of Agent Skills](https://arxiv.org/abs/2609.35692v1)

**作者**：Guilin Zhang, Kai Zhao, Priyanka Mudgal 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-28

### 📄 论文摘要

Users of Workday's deployed LLM-based agents often request features which can be addressed by defining named procedures, also known as skills, in the LLM context, effectively augmenting agents' capabilities. However, as an agent's skills library grows in size, so does the agent's operational cost. Progressive disclosure (lazy-loading) of skills as needed may reduce operational costs, but its impact on overall latency and skill-retrieval quality remains unclear. In this report, we investigate the impact empirically and find that progressive disclosure improves skill-retrieval quality but marginally degrades overall latency.

### 🤖 AI 总结

**一句话总结**：Users of Workday's deployed LLM-based agents often request features which can be addressed by defining named procedures, also known as skills, in the LLM context, effectively augmenting agents' capabi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, Report, Progressive, Disclosure, Skills, Users, Workday's

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35692v1) | [下载PDF](https://arxiv.org/pdf/2609.35692v1.pdf)

---

## [5. Verifier Errors in RLVR: Reward Hacking, Limits of Feedback, and Selective Control](https://arxiv.org/abs/2609.35677v1)

**作者**：Christian Moya, Elliott Thornley, Guang Lin  
**分类**：cs.AI  
**发布时间**：2026-09-28

### 📄 论文摘要

In reinforcement learning with verifiable rewards (RLVR), imperfect verifiers can reward incorrect responses, creating opportunities for reward hacking. Using gradient flow with a fixed verifier, we characterize the conditions under which reward rises while correctness falls. We then show that the observations available during RLVR are, in general, insufficient to detect or identify accepted errors, or to guarantee their reduction without sacrificing correct responses. To address this limit, we construct a correction using additional feedback about correctness from audits. This correction achieves \emph{selective control}: at the current policy, it lowers the probability of accepted errors and raises that of correct responses, provided it outweighs the pressure toward errors from verifier reward. Experiments with log linear and neural contextual bandits and with a language model support the analysis and show that selective control under partial auditing reduces accepted errors while increasing correctness.

### 🤖 AI 总结

**一句话总结**：In reinforcement learning with verifiable rewards (RLVR), imperfect verifiers can reward incorrect responses, creating opportunities for reward hacking. Using gradient flow with a fixed verifier, we c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Verifier, Errors, RLVR, Reward, Hacking, Limits, Feedback

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35677v1) | [下载PDF](https://arxiv.org/pdf/2609.35677v1.pdf)

---

## cs.CL

## [6. Retrieving Biblical Intertextual References in Karen Blixen's Seven Gothic Tales](https://arxiv.org/abs/2609.35765v1)

**作者**：András Kovács, Alexander Conroy, Daniel Hershcovich 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-28

### 📄 论文摘要

Identifying intertextual references is central to literary scholarship, but computationally difficult when source material is transformed through paraphrase, allusion, historical language, and translation. We investigate this problem through biblical intertextuality in Karen Blixen's Seven Gothic Tales. Drawing on the commentary to a critical edition, we construct a benchmark of 189 annotated references and evaluate retrieval against all 31,170 verses of historically plausible Danish Old and New Testament translations. We compare TF-IDF and BM25 with multilingual and Danish sentence encoders, examine the effect of linguistic normalization, and fine-tune a Danish encoder using hard negatives and five-fold cross-validation. We analyze performance across automatically derived lexical-overlap strata representing quotations, paraphrases, and allusions. Linguistically normalized BM25 provides a strong zero-shot baseline, attaining an overall R@10 of 0.365 and retrieving every quotation within its ten highest-ranked verses. The best zero-shot dense model achieves a comparable overall score of 0.360 while performing better on allusions. Fine-tuning DFM-large raises its overall R@10 from 0.265 to 0.508 and more than doubles its performance on allusions, from 0.138 to 0.339. However, evaluation against editorial annotations alone understates the model's scholarly usefulness: a literary scholar judged seven of 30 selected rank-one predictions counted as false positives to be meaningful additional references. These findings show both the potential and the epistemic limits of computational intertextual retrieval. Rather than treating scholarly annotations as exhaustive or model outputs as discoveries, we propose retrieval models as heuristic co-readers that recover documented references and generate candidates for expert-led close reading.

### 🤖 AI 总结

**一句话总结**：Identifying intertextual references is central to literary scholarship, but computationally difficult when source material is transformed through paraphrase, allusion, historical language, and transla...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Retrieving, Biblical, Intertextual, References, Karen, Blixen's, Seven, Gothic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35765v1) | [下载PDF](https://arxiv.org/pdf/2609.35765v1.pdf)

---

## [7. Scaling Long-Form Story Generation via Narrative State Tracking](https://arxiv.org/abs/2609.35759v1)

**作者**：Zhennan Wan, Jianfei Chen  
**分类**：cs.CL  
**发布时间**：2026-09-28

### 📄 论文摘要

LLMs have demonstrated strong capabilities in creative writing. However, scaling them to full-length novels remains challenging, as maintaining narrative consistency becomes increasingly difficult. Existing story-generation methods typically focus on stories of up to about ten thousand words, leaving their ability to scale to full-length novels underexplored. In this work, we introduce Narrative State Tracking Agent (NstAgent), a training-free agentic framework that allows LLMs to track a structured narrative state including characters, past events and future requirements. We extend an existing benchmark to compare narrative consistency across lengths, and use it together with a writing-quality benchmark to systematically evaluate stories ranging from 10K to 100K words. We show that NstAgent achieves better narrative consistency and writing quality as stories grow longer, and neither of them degrades noticeably as length increases, suggesting that it provides an effective approach to scaling story generation toward full-length novels.

### 🤖 AI 总结

**一句话总结**：LLMs have demonstrated strong capabilities in creative writing. However, scaling them to full-length novels remains challenging, as maintaining narrative consistency becomes increasingly difficult. Ex...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Scaling, Long-Form, Story, Generation, via, Narrative, State, Tracking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35759v1) | [下载PDF](https://arxiv.org/pdf/2609.35759v1.pdf)

---

## [8. Harness Learning Enables Generalizable Test-Time Adaptation](https://arxiv.org/abs/2609.35738v1)

**作者**：Alvin Zhang, Xuecheng Liu, Zixuan Wang 等 9 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-09-28

### 📄 论文摘要

A language-model agent is jointly defined by its model and its harness, the executable program that organizes model calls, tool use, and information flow. Because different tasks call for different ways of organizing these operations, the harness needs to be adapted using feedback from the task at hand. We introduce harness learning, which trains a proposer model to revise a solver's harness using execution feedback. We formulate this process as meta-learning over executable programs, with harness revisions playing the role of weight updates in gradient-based adaptation. We train the proposer with reinforcement learning, using the task performance of revised harnesses as the reward. At test time, the proposer uses feedback from successive executions on a new task to refine the harness, without performing any parameter-space update. Experiments on reasoning and multi-hop question answering show that harness learning improves revision quality and that the ability to adapt at test time transfers to unseen tasks. Policies trained on individual revisions can continue improving harnesses over multiple rounds, while the benefits of training on revision sequences vary across settings. These findings suggest a path towards continually learning agents that turn accumulated experience into generalizable improvements.

### 🤖 AI 总结

**一句话总结**：A language-model agent is jointly defined by its model and its harness, the executable program that organizes model calls, tool use, and information flow. Because different tasks call for different wa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Harness, Learning, Enables, Generalizable, Test-Time, Adaptation, language-model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35738v1) | [下载PDF](https://arxiv.org/pdf/2609.35738v1.pdf)

---

## [9. QuanReview: Offline, Auditable Reconciliation of Human and LLM Span Annotations](https://arxiv.org/abs/2609.35685v1)

**作者**：Matteo Musacchio, Juan Cruz Giner Pulero, Isabel Castañeda 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-28

### 📄 论文摘要

Structured span annotations, such as quantities with their units, uncertainty modifiers, and event classes, are expensive to create and hard to keep trustworthy once language models enter the loop. We present QuanReview, an open-source system for auditing and correcting such annotation layers. QuanReview aligns two annotation streams over the same documents at character level, resolves unambiguous cases by an explicit and logged policy, and routes candidate conflicts to a browser-based adjudication interface where reviewers accept either side, build field-level hybrids, or flag items for re-annotation. A campaign manager assigns documents to multiple annotators with configurable redundancy, computes agreement at document and span level, auto-merges unanimous documents, and exports the corrected layer in the original file format, so that it can replace the original annotation files directly. Applied to a 4,457-record humanitarian benchmark and an LLM extraction stream, the system fully auto-merged 8% of documents, applied automatic policy decisions to a further 1,513 records, and concentrated human attention on 3,131 candidate conflicts, a mean of 5.4 per reviewed document.

### 🤖 AI 总结

**一句话总结**：Structured span annotations, such as quantities with their units, uncertainty modifiers, and event classes, are expensive to create and hard to keep trustworthy once language models enter the loop. We...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, QuanReview, Offline, Auditable, Reconciliation, Human, Span

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35685v1) | [下载PDF](https://arxiv.org/pdf/2609.35685v1.pdf)

---

## cs.CV

## [10. FurE: Efficient Instance-Specific 3D Fur Reconstruction without Animal-Fur Datasets](https://arxiv.org/abs/2609.35770v1)

**作者**：Srinjay Sarkar, Prakhar Kaushik, Soumava Paul 等 4 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-09-28

### 📄 论文摘要

Realistic and editable animal fur reconstruction from multi-view images is challenging due to fine-scale detail, self-occlusion and obfuscation, and, unlike human hair, the lack of animal-fur datasets. Fur usually covers most of an animal's body, with large inter-species and intra-species variability. We present FurE, an efficient strand-based animal fur reconstruction method that recovers a per-strand, editable groom by optimizing a root-conditioned latent field, decoded into strand geometry via a PCA-based decoder. We reconstruct a defurred animal body using local fur-thickness cues from a surface-constrained Gaussian Frosting representation together with part-based priors. We further show that a PCA-based decoder learned from human-hair strand data can alleviate animal-data scarcity while enabling substantially faster optimization. FurE achieves a 10x speedup in strand training over current SOTA dense per-strand optimization while retaining strand fidelity and generalizing across synthetic and real-world sequences, with quantitative and qualitative validation despite the reduction in training time.

### 🤖 AI 总结

**一句话总结**：Realistic and editable animal fur reconstruction from multi-view images is challenging due to fine-scale detail, self-occlusion and obfuscation, and, unlike human hair, the lack of animal-fur datasets...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, FurE, Efficient, Instance-Specific, Fur, Reconstruction, without, Animal-Fur

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35770v1) | [下载PDF](https://arxiv.org/pdf/2609.35770v1.pdf)

---

## [11. Reliability-Gated Fusion of Consumer Head and Foot IMUs for Lower-Body 3D Pose](https://arxiv.org/abs/2609.35764v1)

**作者**：Zhilin Guo, Boqiao Zhang, Oszkár Urbán 等 11 位作者  
**分类**：cs.CV, cs.HC  
**发布时间**：2026-09-28

### 📄 论文摘要

Sparse inertial pose estimation promises camera-free motion capture from consumer devices, but consumer sensors are unreliable: firmware-fused orientations are biased, mounting varies between sessions, and streams drift or drop out. On a new 35-take single-subject benchmark pairing an earbud head inertial measurement unit (IMU) with two smart-insole foot IMUs (SAM-3D-Body pseudo-ground-truth labels), we show the reliability problem is channel-level: a channel ablation isolates foot acceleration as the most informative input (66.6 mm vs. 79.0 mm head-only) and the firmware-fused foot orientation as the liability that destroys the gain. We therefore let the model learn how much to trust each channel of each stream: one temporal gate per stream per channel block, trained with an auxiliary reliability objective on synthetically corrupted pretraining data. The channel-gated model is the most accurate of our learned fusion arms on clean data (69.4 mm vs. 83.7 static, 86.6 ungated) and under every simulated fault (bias in training; drift, dropout eval-only); its gates suppress the natively biased foot-orientation channels on clean real data without test-time supervision and flag dropout bursts at 0.92-0.999 AUROC. Two contrasts: dropping a channel known a priori to fail is flat across foot faults but collapses when an unanticipated stream fails (head dropout: 92.9 vs. 79.3 mm); and a fine-tuned HMD-Poser is more accurate on clean data (64.4 mm) and nominally under drift, with no significant paired difference under bias or dropout, but a larger worst-case degradation from clean (+16.1 vs. +3.5 mm, single seed). Learning to gate reliability instead of sensor count is the lever for deployable sparse inertial capture. Code is available at https://github.com/ZhilinGuo/reliability-gated-imu-fusion.

### 🤖 AI 总结

**一句话总结**：Sparse inertial pose estimation promises camera-free motion capture from consumer devices, but consumer sensors are unreliable: firmware-fused orientations are biased, mounting varies between sessions...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Reliability-Gated, Fusion, Consumer, Head, Foot, IMUs, Lower-Body

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35764v1) | [下载PDF](https://arxiv.org/pdf/2609.35764v1.pdf)

---

## [12. InfiniHand: Streaming World-Space Hand Motion Estimation from Egocentric Video](https://arxiv.org/abs/2609.35743v1)

**作者**：Kerui Ren, Kaiwen Song, Weiguang Zhao 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-28

### 📄 论文摘要

World-space hand motion estimation from egocentric video requires recovering 3D articulated hand geometry while tracking camera egomotion. Existing approaches heavily rely on cascading independent hand pose estimators and SLAM systems, resulting in error accumulation, complex pipelines, and severe computational overhead. To address these limitations, we present InfiniHand, an end-to-end streaming feed-forward framework that jointly estimates MANO parameters, camera trajectories, and hand locations directly from uncalibrated egocentric video. InfiniHand integrates persistent spatiotemporal memory with hand-centered visual features, explicitly coupling camera motion with local hand geometry within a unified architecture. We train InfiniHand in two progressive stages by first learning robust camera-space hand priors and then extending to streaming world-space reconstruction. To support this process, we aggregate a pretraining corpus of approximately 5,000 hours of egocentric data across multiple public datasets. Extensive evaluations demonstrate that InfiniHand outperforms state-of-the-art baselines on in-domain benchmarks, achieving a 21.4% reduction in ARCTIC PA-p compared to ViDiHand while substantially mitigating world-space drift. Furthermore, InfiniHand generalizes robustly to in-the-wild videos and operates at 11.19 FPS, delivering more than twice the throughput of HaWoR.

### 🤖 AI 总结

**一句话总结**：World-space hand motion estimation from egocentric video requires recovering 3D articulated hand geometry while tracking camera egomotion. Existing approaches heavily rely on cascading independent han...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：InfiniHand, Streaming, World-Space, Hand, Motion, Estimation, Egocentric, Video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35743v1) | [下载PDF](https://arxiv.org/pdf/2609.35743v1.pdf)

---

## [13. GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space](https://arxiv.org/abs/2609.35734v1)

**作者**：Kerui Ren, Tao Lu, Linning Xu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-28

### 📄 论文摘要

Novel view synthesis from sparse images must reconcile faithful reconstruction of observed regions with plausible completion of unseen content, while maintaining world consistency across viewpoints. Existing geometry-based methods preserve observed scene structure but often struggle to complete unseen regions, whereas video generative models offer rich appearance priors but accumulate inconsistencies during sequential view generation. We propose GeoVerse, a framework that synthesizes world-consistent novel views by performing generation within the geometric latent space of a pretrained 3D foundation model and injecting appearance priors from a video generative model. Specifically, GeoVerse extracts multilevel features from Wan2.2 VACE and injects them into the geometric latent diffusion model via a ControlNet-style adapter, incorporating video-learned appearance priors to enhance structural completion. To enforce cross-view coherence, a global spatial memory continuously aggregates observed and synthesized content, reprojecting target-aligned guidance to anchor subsequent predictions to a shared scene representation. Extensive experiments across diverse datasets demonstrate improved visual quality and geometric consistency, with a 2.23 dB higher PSNR on DL3DV and 32.4% lower ATE on Mip-NeRF360 compared to GLD.

### 🤖 AI 总结

**一句话总结**：Novel view synthesis from sparse images must reconcile faithful reconstruction of observed regions with plausible completion of unseen content, while maintaining world consistency across viewpoints. E...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GeoVerse, World-Consistent, Novel, View, Synthesis, Geometric, Latent, Space

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35734v1) | [下载PDF](https://arxiv.org/pdf/2609.35734v1.pdf)

---

## [14. FlowAct-R2: Beyond Talking Avatar via Streaming Multimodal References and Proactive Agent Planning](https://arxiv.org/abs/2609.35728v1)

**作者**：Ziyao Huang, Zhengkun Rong, Shiyang Qin 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-28

### 📄 论文摘要

We present FlowAct-R2, a framework for interactive humanoid video generation that combines continuous multimodal control with proactive agent planning. Our method consists of two coupled components. First, a Streaming Multimodal Reference Diffusion Transformer adapts the pretrained Seedance 2.0 Mini reference-to-video backbone to accept rolling action prompts, streaming audio, and dynamically updated image, audio, and video references. Video-driven rotary positional embeddings align reference chunks with the generation timeline, while reference-plus-image conditioning and partially noised historical motion frames preserve appearance and avoid accumulated drift. Second, a Proactive Interaction Agent separates pre-online planning from online scheduling and response: it prepares a persona, a long-horizon agenda, and reusable multimodal skills in advance, then autonomously schedules behaviors, responds to audience input, and handles interruptions during a live session. FlowAct-R2 supports real-time 720p generation and hour-scale streaming across entertainment streaming, live shopping, video chatting, and live vlogging.

### 🤖 AI 总结

**一句话总结**：We present FlowAct-R2, a framework for interactive humanoid video generation that combines continuous multimodal control with proactive agent planning. Our method consists of two coupled components. F...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FlowAct-R2, Beyond, Talking, Avatar, via, Streaming, Multimodal, References

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35728v1) | [下载PDF](https://arxiv.org/pdf/2609.35728v1.pdf)

---

## [15. Impact of Patient Orientation in Single- and Multi-View Camera Environments for AI-based Rehabilitation Monitoring](https://arxiv.org/abs/2609.35726v1)

**作者**：Miriama Jánošová, Andreas Lang, Petra Budikova 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-28

### 📄 论文摘要

Automated quality assessment of rehabilitation exercises relies heavily on accurate human pose estimation from video data. Although numerous RGB-based pose estimation methods have been proposed, the impact of camera placement on detecting clinically relevant movement errors remains insufficiently explored. To address this gap, we introduce REHAB26-ViewAngles, a dataset comprising correct and incorrect rehabilitation exercise executions captured from a wide range of camera angles. Furthermore, we propose a novel separability metric to quantify an algorithm's ability to distinguish between valid and faulty exercise repetitions. Using these tools, we analyze how various RGB-based pose-estimation strategies are suitable for exercise quality assessment under varying camera placements. In particular, we analyze single-camera 2D and 3D pose estimation and four multi-camera strategies: a combination of two orthogonal 2D views, 3D triangulation, weighted 3D fusion, and an AI-based pose-estimation transformer model specifically trained from two synchronized cameras. Our findings reveal that an optimally placed 2D camera can improve the separability by 16.9\,\% over the commonly used $0^\circ$ frontal view and frequently outperforms single-camera 3D estimation, while combining two views can further improve accuracy by up to 13.1\,\%. These results offer practical guidance for deploying rehabilitation monitoring in both home and clinical settings.

### 🤖 AI 总结

**一句话总结**：Automated quality assessment of rehabilitation exercises relies heavily on accurate human pose estimation from video data. Although numerous RGB-based pose estimation methods have been proposed, the i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Impact, Patient, Orientation, Single, Multi-View, Camera, Environments

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35726v1) | [下载PDF](https://arxiv.org/pdf/2609.35726v1.pdf)

---

## [16. Superquadric Primitive Decomposition of 3D point clouds via Geometric-Aware Inlier Refinement](https://arxiv.org/abs/2609.35725v1)

**作者**：Alessandro Rinaldi, Edoardo Tedesco, Andrea Ferraris 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-28

### 📄 论文摘要

The decomposition of 3D point clouds into interpretable geometric primitives remains a longstanding challenge in Computer Vision and Computer Graphics. Among the available representations, superquadrics offer a compact and expressive model capable of capturing a wide range of shapes. However, their estimation is inherently challenging, as it requires solving a non-linear optimization problem and is particularly sensitive to noise, outliers, and overlapping structures. While robust estimation methods such as RANSAC and its variants achieve strong performance, they rely primarily on spatial proximity and residual-based criteria, often leading to incorrect inlier assignments across adjacent or complex arrangements of primitives. In this work, we introduce a geometric-aware framework for primitive decomposition that explicitly incorporates local surface properties into the fitting process. Specifically, we propose an inlier refinement step formulated as an energy minimization problem and solved via graph-cut optimization. Our formulation integrates geometric priors, such as normal consistency, enabling more reliable inlier selection beyond purely residual-based criteria. The approach naturally applies to both single-model estimation and multi-model decomposition. By leveraging geometric information beyond point-wise residuals, our method reduces erroneous inlier propagation and stabilizes parameter estimation. Experiments on synthetic and real datasets show consistent improvements in geometric accuracy, robustness to noise and outliers, and convergence efficiency compared to state-of-the-art RANSAC-based methods.

### 🤖 AI 总结

**一句话总结**：The decomposition of 3D point clouds into interpretable geometric primitives remains a longstanding challenge in Computer Vision and Computer Graphics. Among the available representations, superquadri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, 3D, Superquadric, Primitive, Decomposition, point, clouds, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35725v1) | [下载PDF](https://arxiv.org/pdf/2609.35725v1.pdf)

---

## [17. Hard Vision, Easy Vision: What GPT-6 Astra Reveals Across Computer Vision](https://arxiv.org/abs/2609.35718v1)

**作者**：Hanoona Rasheed, Mohammed Irfan Kurpath, Bin Ren 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-28

### 📄 论文摘要

Frontier general-purpose systems are rapidly expanding beyond visual understanding into capabilities traditionally handled by dedicated computer-vision models. As these capabilities expand, a central question for the computer-vision community is how far this reach extends, and what remains hard. We evaluate GPT-6 Astra alongside five frontier general-purpose AI systems across 34 capabilities and 55 benchmarks spanning nine areas of computer vision. We compare their performance with dedicated models and humans where suitable references are available. Astra demonstrates broad visual capability, with substantial gains over other frontier systems in visual and spatial reasoning and several forms of structured prediction. Across the state-of-the-art systems, a consistent pattern emerges. Capabilities involving semantic interpretation, reasoning, and object-centric prediction increasingly approach or reach available reference levels. In contrast, larger gaps remain when tasks require metric geometric accuracy, faithful reconstruction, temporally consistent dense prediction, or specialized fine-grained visual knowledge. Additional reasoning and specialist tools close selected gaps, but their benefits vary across capabilities. These results map a changing landscape of computer vision in which increasingly sophisticated visual tasks are accessible through a general-purpose interface, while precise and fidelity-sensitive perception remains an important frontier.

### 🤖 AI 总结

**一句话总结**：Frontier general-purpose systems are rapidly expanding beyond visual understanding into capabilities traditionally handled by dedicated computer-vision models. As these capabilities expand, a central ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hard, Vision, Easy, What, GPT-6, Astra, Reveals, Across

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35718v1) | [下载PDF](https://arxiv.org/pdf/2609.35718v1.pdf)

---

## [18. Lagrangian--Hamiltonian Flows for Video Prediction and Image Generation: A Symplectic Perspective](https://arxiv.org/abs/2609.35710v1)

**作者**：Jiawei Hu  
**分类**：cs.CV  
**发布时间**：2026-09-28

### 📄 论文摘要

We introduce LHFM, a geometric framework for learning image dynamics. Drawing on structures central to classical mechanics, symplectic geometry, and geometric quantization, LHFM represents each image as an exact Lagrangian graph and models its evolution through image-dependent Hamiltonian flows, which yield a transport--source parameterization of image velocities. Our primary application is deterministic video prediction: LHFM-V is a recurrent model that advances frames by integrating predicted transport and source fields, and achieves the lowest reported FLOP count among the compared recurrent models with similar prediction accuracy. The image variant, LHFM-I, shows that the same construction is compatible with flow matching: in a matched experiment, it attains a lower FID than the flow-matching baseline.

### 🤖 AI 总结

**一句话总结**：We introduce LHFM, a geometric framework for learning image dynamics. Drawing on structures central to classical mechanics, symplectic geometry, and geometric quantization, LHFM represents each image ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Lagrangian--Hamiltonian, Flows, Video, Prediction, Image, Generation, Symplectic, Perspective

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35710v1) | [下载PDF](https://arxiv.org/pdf/2609.35710v1.pdf)

---

## [19. Mind the RefGAP: Correcting Reference Attention in Diffusion-Based Visual Editing](https://arxiv.org/abs/2609.35708v1)

**作者**：Yanan Wang, Shengcai Liao, Guangyi Liu 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-28

### 📄 论文摘要

Reference-guided diffusion editors struggle to faithfully reproduce user-provided references. We identify a potential bottleneck in diffusion editors: many methods provide limited reference-attention allocation. For example, in LoomVideo, edit-region queries assign less than 1% of their attention mass to the reference. We introduce RefGAP, a training-free correction that determines logit-offset magnitudes online at each layer from the reference-attention mass measured during the forward pass. Positive offsets to reference logits strengthen reference usage by edit-region queries, while negative offsets for keep-region queries limit reference-induced changes outside the edit. Two global coefficients control the correction; they are selected once on validation data from four development diffusion editors and held fixed. Across seven diffusion-based image/video editors, RefGAP improves identity fidelity in head swapping and face swapping. RefGAP achieves a fidelity-preservation trade-off comparable to separately tuned constant edit-side biases, without per-approach strength sweeps. Additional experiments on virtual try-on and background replacement evaluate transfer beyond identity editing.

### 🤖 AI 总结

**一句话总结**：Reference-guided diffusion editors struggle to faithfully reproduce user-provided references. We identify a potential bottleneck in diffusion editors: many methods provide limited reference-attention ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mind, RefGAP, Correcting, Reference, Attention, Diffusion-Based, Visual, Editing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35708v1) | [下载PDF](https://arxiv.org/pdf/2609.35708v1.pdf)

---

## cs.LG

## [20. Unifying Distributional Training for One-Step Visual Generation](https://arxiv.org/abs/2609.35763v1)

**作者**：Chi Zhang, Haoyang Shi, Yueyi Liu 等 12 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-28

### 📄 论文摘要

\emph{Distributional training} provides collective supervision for one-step visual generation by matching real and generated features in frozen representation spaces. We introduce \emph{a unified theoretical framework} that separates distribution modeling from matching discrepancy and connects global objectives to pointwise feature updates through Wasserstein gradient flow. Under this framework, FD-Loss and Gaussian-kernel Drifting are recovered through Gaussian optimal transport and kernel-density-based KL matching, respectively. The framework motivates \textbf{MGFlow}, which models feature distributions with Gaussian mixtures at an adjustable granularity between global moments and sample-based representations. MGFlow supports both optimal transport and score-based matching, and couples mass-constrained sample assignment with paired component updates to address mode collapse that mixture expressivity alone does not resolve. On ImageNet $256\times256$, MGFlow substantially surpasses the FD-Loss baseline, achieving state-of-the-art results with \textbf{1.45} $\mathrm{FDr}^6$ on pMF-H and \textbf{1.64} on JiT-H. For text-to-image generation, MGFlow post-trains FLUX.2 [klein] 4B into a one-step generator that outperforms the original four-step model on both GenEval and PickScore. Project page: https://shihaoyang0423.github.io/MGFlow-website/

### 🤖 AI 总结

**一句话总结**：\emph{Distributional training} provides collective supervision for one-step visual generation by matching real and generated features in frozen representation spaces. We introduce \emph{a unified theo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unifying, Distributional, Training, One-Step, Visual, Generation, emph, provides

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35763v1) | [下载PDF](https://arxiv.org/pdf/2609.35763v1.pdf)

---

## [21. Neural Harmonic Measure Operator](https://arxiv.org/abs/2609.35752v1)

**作者**：Jinjin He, Sinan Wang, Yuchen Sun 等 4 位作者  
**分类**：cs.LG, math.NA  
**发布时间**：2026-09-28

### 📄 论文摘要

We introduce Neural Harmonic Measure Operator (NHMO), a neural solver for elliptic PDE problems on variable-shape domains. The harmonic measure of a domain is the boundary probability distribution that, integrated against any boundary data, returns the Dirichlet Laplace solution. It depends only on the geometry, not on the boundary data. NHMO parameterizes the density of this measure as a transformer-based boundary kernel supervised by Walk-on-Spheres exit samples, so one trained kernel handles different boundary values on a shape with no retraining. We extend it to Poisson via a classical decomposition, with an auxiliary network amortizing the source-induced correction and avoiding the singular volume quadrature that breaks direct evaluation. At inference, new boundary values and new sources both yield PDE solutions by re-integration against the fitted kernel and lift, with no retraining. NHMO improves over four prior baselines on the MCB-B 3D variable-shape Poisson benchmark across all five categories, and is competitive with major neural-operator baselines on a controlled 2D testbed.

### 🤖 AI 总结

**一句话总结**：We introduce Neural Harmonic Measure Operator (NHMO), a neural solver for elliptic PDE problems on variable-shape domains. The harmonic measure of a domain is the boundary probability distribution tha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Neural, Harmonic, Measure, Operator, introduce, NHMO, solver

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35752v1) | [下载PDF](https://arxiv.org/pdf/2609.35752v1.pdf)

---

## [22. KV-streams for Efficient Compaction in Agentic Reinforcement Learning](https://arxiv.org/abs/2609.35750v1)

**作者**：Emiliano Penaloza, Dane Malenfant, Dheeraj Vattikonda 等 18 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-28

### 📄 论文摘要

Scaling the horizon of agentic LLMs is bottlenecked by the need to fit ever longer context traces in GPU memory. Context compaction has been the most popular mechanism to alleviate this issue, keeping GPU memory constant for a given trace. Unfortunately, most compaction strategies rely on prefilling the LLM context many times over, hindering training throughput. To alleviate this bottleneck and enable efficient trainable compaction, we propose KV-streams, a plug-and-play strategy compatible with any compaction strategy that substantially increases throughput while showing no evidence of hindering performance. KV-streams enable scalable compaction by streaming the KV cache forward rather than flushing it after each compaction. We show that KV-streams enable three different compaction strategies, achieving a 2.6 to 5x wall-clock speedup in training. Beyond efficiency, we find that the streamed KV cache can act as a recurrent state, carrying forward information that has long since disappeared from the context. Specifically, in a controlled setting we show that, contrary to prior work, RL alone is all that is needed for this behavior to emerge. Overall, we show KV-streams to be an efficient and lightweight plug-and-play addition to any post-training pipeline.

### 🤖 AI 总结

**一句话总结**：Scaling the horizon of agentic LLMs is bottlenecked by the need to fit ever longer context traces in GPU memory. Context compaction has been the most popular mechanism to alleviate this issue, keeping...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：KV-streams, Efficient, Compaction, Agentic, Reinforcement, Learning, Scaling, horizon

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35750v1) | [下载PDF](https://arxiv.org/pdf/2609.35750v1.pdf)

---

## [23. X-Reset: Scaling Object-Centric Reinforcement Learning via Cross-Embodiment Resets](https://arxiv.org/abs/2609.35715v1)

**作者**：Prithwish Dan, Chenyang Ma, Wei Zhan  
**分类**：cs.LG, cs.AI, cs.RO  
**发布时间**：2026-09-28

### 📄 论文摘要

Reinforcement learning (RL) in simulation can train dexterous manipulation policies without robot demonstrations, but training a single generalist policy with task-agnostic rewards faces a severe exploration problem: approaching, grasping, and reorienting diverse objects with many degrees of freedom is difficult to discover from scratch. Prior works make exploration tractable with high-quality robot demonstrations, per-task reward shaping, or by restricting policies to narrow modes of behavior. We propose X-Reset, a framework that instead resolves exploration with human hand-object demonstrations. Rather than imitating or tracking retargeted human motion, X-Reset kinematically retargets hand-object states to noisy robot states, filters out states that are unstable in simulation, and samples the remainder as resets during RL training with general-purpose object-centric rewards. The resulting policy depends only on object state and goal, with demonstrations entering training through the reset distribution. We show that X-Reset trains generalist policies on 20 objects across three embodiments---a 22-DoF hand on two different arms and a parallel-jaw gripper---and resolves the exploration challenges of RL from scratch. X-Reset scales with the number of training objects, generalizes to unseen objects, can learn from imperfect hand-pose estimates, and transfers behaviors zero-shot from sim-to-real.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning (RL) in simulation can train dexterous manipulation policies without robot demonstrations, but training a single generalist policy with task-agnostic rewards faces a severe expl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：X-Reset, Scaling, Object-Centric, Reinforcement, Learning, via, Cross-Embodiment, Resets

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35715v1) | [下载PDF](https://arxiv.org/pdf/2609.35715v1.pdf)

---

## [24. ScAn-Bench: Evaluating Scaling Analysis Methodology](https://arxiv.org/abs/2609.35707v1)

**作者**：Artin Sermaxhaj, Nastaran Alipour, Donat Sinani 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-28

### 📄 论文摘要

Recent progress in machine learning is driven by large-scale foundation models, where scaling laws and finding optimal scaling prescriptions for architecture, data, and hyperparameters are key in advancing the state-of-the-art. Therefore, it is surprising that no systematic study evaluates the methodology to obtain scaling laws and prescriptions across different model types. To shed light on this crucial blind spot and facilitate future research, we introduce the surrogate benchmarks ScAn-Bench-LLM and ScAn-Bench-VLM based on 4524 and 8024 checkpoints of language and vision-language model pipelines. On our benchmarks, we perform the first systematic evaluation of both data acquisition and extrapolation methodology for scaling analysis across different data modalities.

### 🤖 AI 总结

**一句话总结**：Recent progress in machine learning is driven by large-scale foundation models, where scaling laws and finding optimal scaling prescriptions for architecture, data, and hyperparameters are key in adva...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ScAn-Bench, Evaluating, Scaling, Analysis, Methodology, Recent, progress, machine

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35707v1) | [下载PDF](https://arxiv.org/pdf/2609.35707v1.pdf)

---

## [25. A Unified Uncertainty Representation for Graph Neural Networks via Doubly-Spectral Stochastic Expansion](https://arxiv.org/abs/2609.35703v1)

**作者**：Fred Xu, Thomas Markovich, Florence Regol 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-28

### 📄 论文摘要

Reliable deployment of graph neural networks requires calibration, out-of-distribution (OOD) detection, and robustness to distribution shift, yet existing methods address these needs with separate models and   objectives. We model uncertain node embeddings as random graph signals: graph Fourier filters capture structural variation, and a scalar orthogonal-polynomial chaos coordinate captures latent stochastic   variation. The resulting doubly-spectral stochastic (DSS) expansion supplies task-matched readouts from one representation: the mean coefficient encodes class evidence for the energy-based OOD score, the   higher-order coefficients encode structured logit variation, and quadrature averaging over the chaos coordinate defines the single predictive distribution used for prediction and calibration. A capacity theorem   shows that, under a full-rank feature assumption, a restricted subfamily matches the chaos coefficients of any Gaussian-latent random graph signal, with exponentially decaying truncation error under a growth   condition; the task-level claims are established empirically. DSS-GNN has two deployment modes: standalone, or as a residual branch beside a deterministic encoder (DSS-Hybrid). Standalone DSS-GNN achieves the   lowest Brier score among the compared uncertainty-aware baselines on all 14 node classification benchmarks without post-hoc correction; DSS-Hybrid achieves the best AUROC on most node-OOD settings, competitive   cross-graph OOD detection, and the strongest shifted accuracy on all 7 GOOD concept-shift benchmarks under standard empirical risk minimization (ERM). Cross-evaluating both modes on all three tasks shows that   each remains effective on the other's tasks, with documented exceptions, and yields explicit deployment guidance.

### 🤖 AI 总结

**一句话总结**：Reliable deployment of graph neural networks requires calibration, out-of-distribution (OOD) detection, and robustness to distribution shift, yet existing methods address these needs with separate mod...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unified, Uncertainty, Representation, Graph, Neural, Networks, via, Doubly-Spectral

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35703v1) | [下载PDF](https://arxiv.org/pdf/2609.35703v1.pdf)

---

## [26. MeqMuon: Matrix-Equilibrating Muon for LLM Pretraining](https://arxiv.org/abs/2609.35701v1)

**作者**：Chang-Wei Shi, Xu Wang, Wu-Jun Li  
**分类**：cs.LG  
**发布时间**：2026-09-28

### 📄 论文摘要

The success of large language models (LLMs) has been accompanied by continued growth in model size and pretraining costs. Muon offers high accuracy and training efficiency in LLM pretraining. Recent work introduces row-wise normalization into Muon to balance update magnitudes and improve pretraining performance. However, row-wise normalization alone cannot accommodate different imbalance patterns in update matrices. In this paper, we propose an improved Muon optimizer, called \underline{m}atrix-\underline{eq}uilibrating Muon~(MeqMuon), for LLM pretraining. MeqMuon balances both row and column magnitudes through normalization that can be automatically tailored to different imbalance patterns without manual intervention. Moreover, MeqMuon eliminates the need to store AdamW's second-moment estimates, reducing optimizer-state memory usage. Empirical results demonstrate that MeqMuon achieves better convergence performance than AdamW, Muon, and other baselines in LLM pretraining.

### 🤖 AI 总结

**一句话总结**：The success of large language models (LLMs) has been accompanied by continued growth in model size and pretraining costs. Muon offers high accuracy and training efficiency in LLM pretraining. Recent w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, of, MeqMuon, Matrix-Equilibrating, Muon, Pretraining, success, large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35701v1) | [下载PDF](https://arxiv.org/pdf/2609.35701v1.pdf)

---

## [27. Distillation Defenses Easily Break After Reinforcement Learning](https://arxiv.org/abs/2609.35699v1)

**作者**：Shidan Javaheri, Alexander Panfilov, Oliver Britton 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CR  
**发布时间**：2026-09-28

### 📄 论文摘要

Distillation attacks copy the reasoning capabilities of closed-source large language models, allowing bad actors to replicate state-of-the-art performance at low cost. Attackers systematically collect a large volume of frontier model reasoning traces and then train (i.e., "distill") their own models on these traces. Existing defenses against distillation attacks are typically evaluated immediately after distillation, implicitly assuming attackers do not train their models any further. In this paper, we argue that a more realistic threat model includes further training with reinforcement learning after distillation. A misspecified threat model can give a false sense of security -- some defenses that seem effective after distillation can be broken after subsequent reinforcement learning. Practically, reinforcement learning lowers the bar for a distillation attack to be effective. We show that simple attacks can steal reasoning capabilities from existing closed-source language models using data easily obtainable from current APIs, yielding reasoning improvements equivalent to more sophisticated attacks that extract the full hidden traces. Results indicate that any distillation defense that leaks sufficient information to reconstruct approximate reasoning traces is likely ineffective. We conclude by discussing broader implications and batch-level distillation defenses which could be more effective.

### 🤖 AI 总结

**一句话总结**：Distillation attacks copy the reasoning capabilities of closed-source large language models, allowing bad actors to replicate state-of-the-art performance at low cost. Attackers systematically collect...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Distillation, Defenses, Easily, Break, After, Reinforcement, Learning, attacks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35699v1) | [下载PDF](https://arxiv.org/pdf/2609.35699v1.pdf)

---

## [28. Provable Benefits of Regularization: Fast Rates for Adversarial Imitation Learning](https://arxiv.org/abs/2609.35698v1)

**作者**：Hanbin Zhou, Shangzhe Li, Alexander Braverman 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-28

### 📄 论文摘要

We study adversarial imitation learning (AIL), in which an agent learns to imitate expert demonstrations by optimizing a policy against an adversarial reward that distinguishes expert and learner behavior. Historically, reward regularization and entropy-based policy regularization are key components of empirically successful methods such as GAIL and LS-IQ, yet their finite-sample benefits remain underexplored. We establish fast rates for jointly regularized AIL in finite-horizon Markov decision processes with general function approximation. Our model-free algorithm, Dually Regularized AIL, combines KL policy regularization with a quadratic reward penalty weighted by expert and learner occupancies. With K online episodes and N expert trajectories, we prove a $\widetilde{O}\left(\frac{1}{K}+\frac{1}{N}\right)$ bound on the regularized imitation gap for fixed regularization parameters. Our analysis combines an online mirror descent construction for general convex reward classes to control estimation error from finite expert data and stochastic learner feedback, with a sharp analysis of optimistic KL-regularized policy learning. To the best of our knowledge, Dually Regularized AIL is the first algorithm to simultaneously achieve $\widetilde{O}\left(\frac{1}ε\right)$ sample complexity in both expert demonstrations and online interactions for this regularized AIL objective, even with stochastic experts. These results provide a rigorous characterization of the complementary statistical benefits of reward and policy regularization in AIL.

### 🤖 AI 总结

**一句话总结**：We study adversarial imitation learning (AIL), in which an agent learns to imitate expert demonstrations by optimizing a policy against an adversarial reward that distinguishes expert and learner beha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Provable, Benefits, Regularization, Fast, Rates, Adversarial, Imitation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35698v1) | [下载PDF](https://arxiv.org/pdf/2609.35698v1.pdf)

---

## [29. Rethinking Personalized Generation: Test-Time Alignment via Factorized Ranking Models](https://arxiv.org/abs/2609.35695v1)

**作者**：Qiyao Ma, Junshan Zhang, Zhe Zhao  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-09-28

### 📄 论文摘要

Aligning large language models (LLMs) to diverse user preferences is fundamentally hindered by standard alignment paradigms that optimize for monolithic users. In this work, empirical studies are first used to reveal the existence of a massive, untapped performance headroom for personalized generation through test-time alignment. We demonstrate that personalized generation is uniquely suited for test-time scaling methods like Best-of-N (BoN) because it can be viewed primarily as a candidate matching problem rather than a generator capability bottleneck. While reward models could in principle exploit this headroom, they are poorly calibrated for personalization, and their billion-parameter scale makes scoring large candidate pools prohibitively expensive. To overcome this limitation, we propose a parameter-efficient framework utilizing million-parameter scale multi-layer perceptron (MLP) ranking models. Our personalized ranking model directly reuses the internal embeddings of the base generator with minimal overhead. By scaling train-time data to provide fine-grained personalized preferences, this million-parameter ranking model accurately scores large candidate pools and can seamlessly guide generation to reduce the cost of materializing N candidates. Extensive experiments on nine datasets spanning three personalized generation settings show that our personalized ranking model effectively exploits the discovered headroom, outperforming billion-parameter generalist reward models on every dataset, with under 0.4% of their parameters and four orders of magnitude lower scoring latency.

### 🤖 AI 总结

**一句话总结**：Aligning large language models (LLMs) to diverse user preferences is fundamentally hindered by standard alignment paradigms that optimize for monolithic users. In this work, empirical studies are firs...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Rethinking, Personalized, Generation, Test-Time, Alignment, via, Factorized, Ranking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35695v1) | [下载PDF](https://arxiv.org/pdf/2609.35695v1.pdf)

---

## [30. Rethinking Circuit Evaluation: Do Circuits Explain Model Errors?](https://arxiv.org/abs/2609.35686v1)

**作者**：Li Zhang, Chuqin Geng, Mark Zhang 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-28

### 📄 论文摘要

Mechanistic interpretability (MI) aims to explain a model's behaviour through analyzing its internal computations; circuit-based explanations aim to isolate these computations with compact subnetworks validated by ablating the rest of the model. We show that circuits validated this way may fail to recover the underlying mechanism of the model's behaviour by closely reproducing its successful decisions while failing to account for most of its errors. Such explanations should account for the model's particular errors as well as its successes. We evaluate this requirement by measuring exact answer agreement separately on model successes and failures, across circuit sizes and ablation settings, on IOI, Docstring, and six model-task settings from the Mechanistic Interpretability Benchmark. We discover that many tested circuits closely replicate correct behaviour while missing most of the model's errors. On indirect object identification (IOI) for GPT-2 small, under mean ablation, the manual circuit and tested automated circuits, including one trained against the model's full output distribution, agree with the model on 97.3-99.5% of prompts it answers correctly but only 11.4-41.7% of errors. An IOI case study shows that lost errors are recoverable by restoring omitted attention-heads which raise error reproduction from 14.2% to 75.1% on a separate held-out set with 0.41 percentage point decrease on correct agreement, exceeding matched random extensions and scalar-biased control. Intervention traces show how omitted computations produce specific wrong answers for a reproducible subset of errors. In all, these findings show circuits can preserve task success without adequately explaining model's failures, and support exact error reproduction as a necessary, but not sufficient, test of circuit-based explanations of model behaviour.

### 🤖 AI 总结

**一句话总结**：Mechanistic interpretability (MI) aims to explain a model's behaviour through analyzing its internal computations; circuit-based explanations aim to isolate these computations with compact subnetworks...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, Rethinking, Circuit, Evaluation, Circuits, Explain, Model, Errors?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.35686v1) | [下载PDF](https://arxiv.org/pdf/2609.35686v1.pdf)

---

