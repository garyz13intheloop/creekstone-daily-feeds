# arXiv AI 论文日报 | 2026-10-21

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.CL](#csCL) (2 篇)
- [cs.AI](#csAI) (9 篇)

---

## cs.AI

## [1. Value-Rich, Differently Organized: Measuring Value Expression and Organization in AI-Generated Debates](https://arxiv.org/abs/2610.28604v1)

**作者**：Maoyuan Li, Haoyuan Li, Zhongsheng Wang 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-20

### 📄 论文摘要

Current evaluation of LLM-generated debate largely focuses on argumentative quality, leaving the value structure of generated arguments underexamined. We introduce a diagnostic metric framework for comparing how values are expressed and organized in human-reference and AI-generated debates. The framework separates value expression, the range of recognizable values a debate invokes, from value organization, how those values are distributed and sustained across turns. Grounded in Schwartz's Basic-10 value theory, it represents debates as multi-level value distributions over argumentative units, utterances, stances, and full debates, enabling metrics for value coverage, alignment, diffusion, and cross-turn dynamics. Across multiple generation systems, AI-generated debates are broadly value-expressive, often activating as many or more value dimensions than matched human references, but they organize these values differently. Their utterances are more locally value-diffuse, and source-blind judges distinguish value clarity from value focus. These findings show that debate evaluation should consider not only value presence, but also value organization. Code and supplementary materials are available at https://github.com/Maoyuan-li/Value-Expression-and-Organization.

### 🤖 AI 总结

**一句话总结**：Current evaluation of LLM-generated debate largely focuses on argumentative quality, leaving the value structure of generated arguments underexamined. We introduce a diagnostic metric framework for co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Value-Rich, Differently, Organized, Measuring, Value, Expression, Organization, AI-Generated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28604v1) | [下载PDF](https://arxiv.org/pdf/2610.28604v1.pdf)

---

## [2. Evolving Agent Interfaces](https://arxiv.org/abs/2610.28601v1)

**作者**：Saaket Agashe, Yuzhe Yang, Gonzalo Gonzalez-Pumariega 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-20

### 📄 论文摘要

Computer-use agents are limited by the interfaces humans give them. An agent may type a spreadsheet cell by cell when a single line of code would do, or print all two thousand lines of a file through a shell to find one function. Both the interfaces and the knowledge of when to use each are built by hand, which cannot keep pace with new applications, workflows, and models. We argue that interface design should itself be an agent capability. We introduce Agent S4, an autonomous computer-use scientist that builds Evolving Agent Interfaces from task experience. A meta-agent examines task agents' trajectories on synthetic training tasks, without success labels, and constructs and revises interfaces and usage knowledge in a repository. Population-based evolution then selects which repositories to develop further by their performance on validation tasks the meta-agent never sees, favoring changes that generalize beyond the seen tasks. On OSWorld V2, Agent S4, with Qwen3.8-27B and the evolved repository of interfaces, sets a new state of the art in open-source computer-use agents, reaching 21.3% binary score, 3.8 times the same model with fixed interfaces. This is above both GPT-5.5 (13.0%) and Claude Opus 4.8 (20.6%), at about 4.3% and 1.5% of their respective costs. On ScienceBoard, the evolved interfaces improve the success rate from 41.4% to 58.6% with the same model. These results suggest that useful interfaces can be evolved from experience, making autonomous interface design a source of improvement complementary to advances in models and harnesses. We open-source our code at https://github.com/simular-ai/agent-s.

### 🤖 AI 总结

**一句话总结**：Computer-use agents are limited by the interfaces humans give them. An agent may type a spreadsheet cell by cell when a single line of code would do, or print all two thousand lines of a file through ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Evolving, Interfaces, Computer-use, limited, humans, give, them

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28601v1) | [下载PDF](https://arxiv.org/pdf/2610.28601v1.pdf)

---

## [3. What Do RTL Repair Benchmarks Actually Measure?](https://arxiv.org/abs/2610.28595v1)

**作者**：Yeyin Eva Zhu, Rishabh Ranawat  
**分类**：cs.AI  
**发布时间**：2026-10-20

### 📄 论文摘要

RTL repair benchmarks should measure whether a model can fix broken RTL given a specification. To this end, we construct and hash-bind RTLRepairDataset, 5,784 (broken, fixed) training pairs; RTLRepairBench, 459 held-out cases with 374 syntactic and 85 behavioral mutations; and an evaluation harness supporting simulation and formal equivalence. We then use this infrastructure to identify two measurement confounds. First, simulation and formal scoring give opposite signs for the apparent effect of providing a specification in one evaluated cohort; reset-aware rescoring attributes almost all of the simulation-formal disagreement to reset and first-cycle comparison semantics. Second, on 274 mined model failures, the specification-only minus specification-conditioned recovery point estimate ranges from -8.5 to +18.3 percentage points across six models. Thus, a conventional repair score need not isolate whether the model used the faulty RTL. We translate these findings into evaluation controls: report initialization, reset, first-cycle, and unknown-value semantics; disclose oracle coverage and undecided cases; and include a specification-only baseline. Together, the resources and audit provide both a benchmark for behavioral repair and a protocol for diagnosing what contributes to its measured score. We release the benchmark, the training set, construction code, sanitized aggregate evidence, and reproduction materials at https://github.com/Evaaaz/RTLRepairBench.

### 🤖 AI 总结

**一句话总结**：RTL repair benchmarks should measure whether a model can fix broken RTL given a specification. To this end, we construct and hash-bind RTLRepairDataset, 5,784 (broken, fixed) training pairs; RTLRepair...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, What, RTL, Repair, Benchmarks, Actually, Measure?, should

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28595v1) | [下载PDF](https://arxiv.org/pdf/2610.28595v1.pdf)

---

## [4. Beyond the Sequentiality Bottleneck: A Hybrid Diffusion-Autoregressive Framework for Efficient Multimodal Reasoning](https://arxiv.org/abs/2610.28584v1)

**作者**：Wei Cai, Jian Zhao, Yuchen Yuan 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-20

### 📄 论文摘要

Autoregressive models (ARMs) face a "Sequentiality Bottleneck" in reasoning, while diffusion language models (DLMs) offer parallelism but lack semantic coherence. To addresses both limitations, we propose Collaborative Reasoning Asymmetric Learning (CoRAL), a hybrid framework via an Asymmetric Planner-Executor (APE) architecture: a DLM Planner generates K diverse reasoning trajectories in parallel, while a large ARM Executor selects the optimal plan and synthesizes the final answer. To train the Planner effectively, we introduce Reward-Guided Denoising for CoT (RDC), which integrates outcome-based rewards into the diffusion process to steer it toward goal-directed reasoning. Experiments on vision-language benchmarks show that CoRAL significantly outperforms prior diffusion-based methods and achieves competitive performance against strong ARMs, achieving both superior efficiency and quality.

### 🤖 AI 总结

**一句话总结**：Autoregressive models (ARMs) face a "Sequentiality Bottleneck" in reasoning, while diffusion language models (DLMs) offer parallelism but lack semantic coherence. To addresses both limitations, we pro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Sequentiality, Bottleneck, Hybrid, Diffusion-Autoregressive, Framework, Efficient, Multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28584v1) | [下载PDF](https://arxiv.org/pdf/2610.28584v1.pdf)

---

## [5. Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition](https://arxiv.org/abs/2610.28578v1)

**作者**：Wenjie Lou, Tianshuo Peng, Shiyang Feng 等 99 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-20

### 📄 论文摘要

In this report, we introduce Sage-A1.5, a 35B Mixture-of-Experts agentic model that builds on A1 to advance long-horizon problem solving through adaptive capability composition. Compared with A1, Sage-A1.5 learns not only to solve individual tasks, but also to organize work and revise its approach during execution. Sage-A1.5 highlights three improvements: agentic orchestration, verification, and open scientific discovery. First, agentic orchestration extends single-agent execution through task delegation and parallel collaboration among subagents with isolated contexts, enabling complex tasks to be decomposed and addressed concurrently and supporting efficient execution while reducing interference across concurrent subagents. Second, agentic verification strengthens long-horizon reliability through progress checking, evidence validation, and reflective strategy revision, allowing the agent to recognize unproductive search paths and pursue alternative approaches. Third, open scientific discovery extends agentic capabilities beyond answering predefined questions to conducting exploratory research, connecting scientific inquiry with interactive analysis and inspectable research artifacts. We showcase these capabilities through complicated agentic tasks and multidisciplinary scientific applications. Besides, we hope Sage-A1.5 provides the community with an accessible foundation for open scientific discovery, offering a practical path from long-horizon task execution to collaborative, verifiable, and inspectable scientific exploration.

### 🤖 AI 总结

**一句话总结**：In this report, we introduce Sage-A1.5, a 35B Mixture-of-Experts agentic model that builds on A1 to advance long-horizon problem solving through adaptive capability composition. Compared with A1, Sage...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sage-A1.5, Long-Horizon, Execution, Scientific, Exploration, Capability, Composition, report

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28578v1) | [下载PDF](https://arxiv.org/pdf/2610.28578v1.pdf)

---

## [6. Evolving Semantic Indexes for Generative Retrieval](https://arxiv.org/abs/2610.28568v1)

**作者**：Jinming Nian, Jyun-Yu Jiang, Henry Tsai 等 5 位作者  
**分类**：cs.AI, cs.IR, cs.LG  
**发布时间**：2026-10-20

### 📄 论文摘要

Generative retrieval (GR) casts search and recommendation as autoregressive generation of discrete semantic identifiers (SIDs). SID design largely determines GR quality, but its discrete, interdependent components (SID construction, collision handling, decoding, and training) cannot be optimized end-to-end with gradients and remain largely hand-designed. We introduce a framework that improves these components through LLM-driven evolutionary program search, to our knowledge the first application of this approach to GR. A locally served, open-weight 31B model mutates executable GR components, so no proprietary LLM API is used, and a 1M-parameter proxy decoder provides fast feedback in place of repeatedly training the 1B target generator. Across 21 SID programs on NQ320K, proxy and target Recall@100 show strong rank correlation (Spearman $ρ= 0.90$). Guided by this proxy, evolution improves the seed GR on NQ320K, MSMARCO300K, and a multilingual e-commerce dataset under a fixed training recipe. On NQ320K, jointly evolving SID construction and collision handling improves Recall@1 from 55.8% to 59.3% and Recall@100 from 85.8% to 90.6%. A component study shows that proxy reliability depends on what is evolved: improvements transfer reliably for the semantic index but not for the generator's training objective or the full pipeline. LLM-driven evolutionary search is thus a practical tool for GR design, provided proxy reliability is established for the chosen search space.

### 🤖 AI 总结

**一句话总结**：Generative retrieval (GR) casts search and recommendation as autoregressive generation of discrete semantic identifiers (SIDs). SID design largely determines GR quality, but its discrete, interdepende...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GR, Evolving, Semantic, Indexes, Generative, Retrieval, casts, search

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28568v1) | [下载PDF](https://arxiv.org/pdf/2610.28568v1.pdf)

---

## [7. Agentic Ensemble with Vision-Language Models for Visual Anomaly Detection](https://arxiv.org/abs/2610.28560v1)

**作者**：Shangquan Sun, Wenjun Luo, Xu He 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-20

### 📄 论文摘要

Visual anomaly detection aims to detect abnormal objects, while anomaly samples are often scarce during model training. Assembling multiple pretrained detectors can help by leveraging their transferable image scores and anomaly maps. However, most existing ensemble methods apply fixed fusion rules over saved predictions which struggle when pretrained detectors clearly disagree due to different training objectives, priors, and visual representations. To this end, we design AnomalyAgent, a post-training fusion framework for accurate visual anomaly detection. AnomalyAgent aligns heterogeneous scores and maps, summarizes score- and region-level disagreement, and treats fusion as a finite action-selection problem. It implements two types of actions: 1) score actions that determine how to fuse image-level detector confidence via consensus, robust aggregation, detector weighting, or score-map consistency; 2) map actions that fuse dense anomaly responses via consensus, detector weighting, geometric aggregation, or disagreement correction. A constrained vision-language model (VLM) is introduced to inspect high-conflict samples and select valid score action and map action to produce the final prediction. We evaluate AnomalyAgent on MVTec AD and VisA as primary benchmarks, together with seven additional public anomaly benchmarks and Real-IAD for large-scale score-level evaluation. Across these benchmarks, AnomalyAgent consistently improves over equal-weight fusion and achieves the best mean image AUROC and pixel AP among the compared fusion methods on MVTec AD and VisA, while demonstrating robust transfer across additional anomaly domains.

### 🤖 AI 总结

**一句话总结**：Visual anomaly detection aims to detect abnormal objects, while anomaly samples are often scarce during model training. Assembling multiple pretrained detectors can help by leveraging their transferab...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agentic, Ensemble, Vision-Language, Models, Visual, Anomaly, Detection, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28560v1) | [下载PDF](https://arxiv.org/pdf/2610.28560v1.pdf)

---

## [8. Humans Correct Their Judgments Through Debate, but Weaker AI Models Do Not](https://arxiv.org/abs/2610.28539v1)

**作者**：Maria Victoria Carro, Denise Alejandra Mester, Facundo Nieto 等 17 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-20

### 📄 论文摘要

How can we effectively oversee AI systems that surpass human intelligence? AI Safety via Debate proposes that two AI systems argue opposing positions and a judge, either a human or a weaker model, decides which is correct. By facilitating supervisors in providing high-quality training signals, debate aims to encourage truthful and safe behavior from AI systems whose capabilities exceed our own. However, human judgment is not neutral: people often rely on biases which advanced AI systems may learn to exploit. Drawing on insights from collective intelligence and social cognition, this paper investigates whether debate can guide human and LLM supervisors toward the truth despite their prior beliefs. We evaluate several protocol configurations. We also explore setups inspired by the wisdom of the crowd such as the number and diversity of judges, as well as interaction mechanisms including deliberation and voting. Overall, we find that debate increases accuracy relative to prior beliefs for human judges, whereas the consultancy baseline, in which a single expert argues for one answer, does not. For weaker language models, however, the results are mixed: debate provides no comparable gains in most settings and can even reduce accuracy. Among multi-judge protocols, weighted voting produces the highest accuracy for human supervisors, whereas for LLMs none of them significantly improves group accuracy, even as the number of judges increases. Notably, the behavior of minority judges in non-diverse deliberation protocols suggests that, under symmetric settings, incorrect positions could be more persuasive than correct ones. These findings support debate as a viable path toward scalable human oversight, but cast doubt on its benefits for weaker AI supervisors, raising concerns about fully automated training and control pipelines in high-stakes settings.

### 🤖 AI 总结

**一句话总结**：How can we effectively oversee AI systems that surpass human intelligence? AI Safety via Debate proposes that two AI systems argue opposing positions and a judge, either a human or a weaker model, dec...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Humans, Correct, Their, Judgments, Through, Debate, but, Weaker

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28539v1) | [下载PDF](https://arxiv.org/pdf/2610.28539v1.pdf)

---

## [9. Beyond 4 bits: Data-Centric Post-training Quantization and Recovery](https://arxiv.org/abs/2610.28537v1)

**作者**：Rhea Sanjay Sukthanker, Riccardo Grazzi, James Hensman 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-20

### 📄 论文摘要

Post-training quantization (PTQ) compresses the weights of a trained model with limited compute and data. Down to 4 bits it is near-lossless, but at 2 bits scalar PTQ configurations fall to chance-level accuracy. We study three choices usually treated as implementation details that matter little at 4 bits but decide 2-bit quality: the quantization representation, the calibration data, and the recovery fine-tuning data, across six dense and mixture-of experts models (ranging from $3.8$ to $32$B parameters). Representation is the largest factor and vector codebooks restore usable models where scalar PTQ pipelines collapse. Most of the remaining loss in accuracy is on \emph{generative} tasks, and the amount of performance drop is model-dependent. Furthermore, at a short recovery budget, calibration and recovery data are coupled. The best recovery data depends on the calibration data, so the two must be chosen jointly. The resulting recipe involves a vector codebook representation, a small task-aligned calibration mixture, and an inexpensive codebook-only recovery stage. Including codebooks, it uses about $2.3$ effective bits per weight and retains $89$ to $97\%$ of full-precision question-answering (QA) accuracy where scalar PTQ is at chance, and, including recovery, uses $1.4$ to $30\times$ less compute than the strongest quantization-aware-training (QAT) baseline.

### 🤖 AI 总结

**一句话总结**：Post-training quantization (PTQ) compresses the weights of a trained model with limited compute and data. Down to 4 bits it is near-lossless, but at 2 bits scalar PTQ configurations fall to chance-lev...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, bits, Data-Centric, Post-training, Quantization, Recovery, PTQ, compresses

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28537v1) | [下载PDF](https://arxiv.org/pdf/2610.28537v1.pdf)

---

## cs.CL

## [10. NarraSpace: Multimodal Scene-Grounded Evidence for Picture-Description Dementia Classification](https://arxiv.org/abs/2610.28616v1)

**作者**：Qingming Li, Ruiyan Sun, Satoshi Nakamura  
**分类**：cs.CL  
**发布时间**：2026-10-20

### 📄 论文摘要

Picture-description dementia classification uses a shared visual scene, but a transcript-level prediction alone does not identify the scene evidence underlying its inputs. NarraSpace links words and speech times to named picture elements and retrieves utterances for predefined scene events. Narrative-spatial descriptors summarize coverage and temporal organization. A frozen language model contrasts each event's text under examples from Alzheimer's disease and healthy-control training participants, alongside transcript surprisal and coverage measurements. Retained source records link event scores to their source utterances, speech intervals, and lexical matches. On the official 48-participant test set of the Alzheimer's Dementia Recognition through Spontaneous Speech benchmark, a fixed support vector classifier achieves $80.88\%\pm2.56\%$ mean accuracy over fifty seeds; averaged probabilities yield $81.25\%$ accuracy and $91.32\%$ area under the receiver operating characteristic curve. NarraSpace makes the construction of scene-linked classification inputs explicit and inspectable by connecting event-indexed language-model measurements to their source utterances, speech timing, and extraction records. Such source-linked measurements could support clinician review of picture descriptions by presenting quantitative summaries alongside the original speech evidence.

### 🤖 AI 总结

**一句话总结**：Picture-description dementia classification uses a shared visual scene, but a transcript-level prediction alone does not identify the scene evidence underlying its inputs. NarraSpace links words and s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：NarraSpace, Multimodal, Scene-Grounded, Evidence, Picture-Description, Dementia, Classification, uses

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28616v1) | [下载PDF](https://arxiv.org/pdf/2610.28616v1.pdf)

---

## [11. Benchmarking Arabic Dialects for Math Problems](https://arxiv.org/abs/2610.28607v1)

**作者**：Noor Abo Mokh, Teresa Lynn, Nizar Habash 等 8 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-10-20

### 📄 论文摘要

Mathematical reasoning remains underexplored for low-resource languages, including Dialectal Arabic. To bridge this gap, we introduce the DAR-MGSM (Dialectal Arabic Multilingual Grade School Math) Benchmark, the first manually curated benchmark for evaluating mathematical reasoning in Dialectal Arabic. DAR-MGSM consists of math word problems (MWPs) requiring multi-step reasoning and covers five major Arabic dialects alongside Modern Standard Arabic (MSA). The benchmark comprises two parallel versions: translated-only and translated & culturally localized. The latter version adapts entities and references to regional varieties. We evaluate eleven Arabic-centric and multilingual large language models on DAR-MGSM. The results show that the performance generally declines on the localized version, highlighting the challenges introduced by culturally grounded adaptations. However, the magnitude of this effect varies across models, with Arabic-centric models exhibiting different levels of sensitivity to localization. A mechanistic interpretability analysis shows that translated and localized variants of the same MWPs often induce distinct internal reasoning trajectories, even when aggregate accuracy remains similar. Overall, our results show that mathematical reasoning performance depends on both linguistic variety and cultural context.

### 🤖 AI 总结

**一句话总结**：Mathematical reasoning remains underexplored for low-resource languages, including Dialectal Arabic. To bridge this gap, we introduce the DAR-MGSM (Dialectal Arabic Multilingual Grade School Math) Ben...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Benchmarking, Arabic, Dialects, Math, Problems, Mathematical, reasoning, remains

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28607v1) | [下载PDF](https://arxiv.org/pdf/2610.28607v1.pdf)

---

## cs.CV

## [12. Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs](https://arxiv.org/abs/2610.28632v1)

**作者**：Noam Rotstein, Yoad Tewel, Chen Tessler 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.GR, cs.LG, cs.RO  
**发布时间**：2026-10-20

### 📄 论文摘要

Video generation models can now depict remarkably realistic motion. Yet it is unclear how to use this motion beyond pixels: to animate a specific 3D asset and replay the animation in its 3D scene. For instance, a video model can show a monkey jumping over a crossbar, but it cannot return that jump as replayable 3D motion placed in the 3D scene. Here we present a model that directly co-generates the video and 3D motion for any supplied rig, along with a camera that registers this motion to the scene. Prior video-motion models either handle only human skeletons, often adding billions of parameters, or triangulate 3D motion from generated 2D pose maps. We instead keep 3D motion in a separate model that supports arbitrary skeletons, and connect it to a pretrained video model through a small set of cross-attention layers. This separation lets the motion model first learn how skeletons move from motion-only data, which is easier to obtain and augment than paired video. Additionally, our model learns to locate each joint in the video frames, which lets us recover the camera and place the 3D motion in the scene. To train across many skeletons, we use a generative video editor to place animated 3D assets in scenes suited to their actions, curating the edits so their known motion remains valid. Together with human and robot video, this yields nearly 200K training pairs. Our evaluations demonstrate that our model animates diverse rigs from text more faithfully than video-first pipelines, and its motion responds to the surrounding scene. It also turns video into rig motion, rig motion into video, and enables keyframe-based control of the 3D motion. Videos and additional results are available on our project page: https://research.nvidia.com/labs/par/projects/jca/.

### 🤖 AI 总结

**一句话总结**：Video generation models can now depict remarkably realistic motion. Yet it is unclear how to use this motion beyond pixels: to animate a specific 3D asset and replay the animation in its 3D scene. For...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Joints, Camera, Action!, Co-Generating, Motion, Video, Arbitrary

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28632v1) | [下载PDF](https://arxiv.org/pdf/2610.28632v1.pdf)

---

## [13. AEON: Unifying Video and 3D World Models](https://arxiv.org/abs/2610.28631v1)

**作者**：Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-20

### 📄 论文摘要

Current world models for explicit world simulation typically follow two distinct pathways: (1) video generative models (e.g., Sora), which simulate realistic appearances but fail to preserve 3D consistency; and (2) 3D generative models (e.g., Marble), which generate geometrically consistent scenes but often yield static, less realistic observations. We present AEON, a unified framework that bridges video-based and 3D-based world models and combines the benefits of both. The key insight of AEON lies in a generative model that operates within the text- or image-conditioned video latent space while producing renderable 4D graphics primitives---specifically, 4D Gaussian Splatting (4DGS)---as the explicit world representation. We train a 4D reconstruction model to predict both 4DGS and camera poses from monocular videos, serving as our initialized 4D decoder. Furthermore, we design a domain adapter that translates generative video latents into reconstructive 4D latents through a distillation process on the video VAE. AEON naturally supports video-based world modeling by rendering 4DGS at predicted camera trajectories, and constructs a persistent 4D environment with scene dynamics for realistic world simulation. Consequently, AEON empowers a diverse range of world modeling applications and achieves state-of-the-art performance on standard benchmarks. Project Page: https://weiqi-zhang.github.io/AEON

### 🤖 AI 总结

**一句话总结**：Current world models for explicit world simulation typically follow two distinct pathways: (1) video generative models (e.g., Sora), which simulate realistic appearances but fail to preserve 3D consis...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, AEON, Unifying, Video, World, Models, Current, explicit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28631v1) | [下载PDF](https://arxiv.org/pdf/2610.28631v1.pdf)

---

## [14. PsycheMME: A Psychology-Informed Benchmark for Social Understanding and Interaction in Videos](https://arxiv.org/abs/2610.28625v1)

**作者**：Heran Hu, Yuhang Dong, Zhucun Xue 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-20

### 📄 论文摘要

Understanding human needs and selecting responses require distinct judgments that aggregate accuracy can obscure. We introduce PsycheMME, a video benchmark informed by psychology, with eight capabilities spanning grounding, states, needs, interaction decisions, memory, and risk. Drawing on Social Information Processing and the Perception-Action Cycle, this organization separates human understanding from response selection. We construct 1,000 questions from 630 episodes through independent answering with proposed references withheld and expert review. Our Reasoning-Verified protocol weights answer credit by the support and logical consistency of explicit rationales against annotated cues. Across 17 models, Timing has the lowest Verified scores and credit retention, with weaker support judgments for correct Timing answers. Models with similar Need scores still differ in answer completeness on open questions. Input controls and SFT/GRPO examine context dependence and adaptation. Evaluating answers alongside rationales locates where models fail across understanding, response selection, and justification.

### 🤖 AI 总结

**一句话总结**：Understanding human needs and selecting responses require distinct judgments that aggregate accuracy can obscure. We introduce PsycheMME, a video benchmark informed by psychology, with eight capabilit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PsycheMME, Psychology-Informed, Benchmark, Social, Understanding, Interaction, Videos, human

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28625v1) | [下载PDF](https://arxiv.org/pdf/2610.28625v1.pdf)

---

## [15. MindView: Benchmarking Generative Multi-View Spatial Intelligence](https://arxiv.org/abs/2610.28622v1)

**作者**：Yanbo Wang, Siqi Luo, Siyu Zhang 等 12 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-10-20

### 📄 论文摘要

Spatial intelligence has recently been assessed through generative tasks such as spatially grounded image editing, yet language-guided generation of spatially consistent views from partial multi-view observations remains underexplored. We introduce MindView, a benchmark for generative multi-view spatial intelligence with 1,500 samples from 513 scenes across three indoor datasets. Its seven tasks form two families: geometry-dominant tasks specify changes in camera position and orientation, while semantics-dominant tasks require inferring target viewpoints by grounding referred objects and interpreting spatial relations and reference-frame cues. Evaluation of eleven generators reveals substantial room for improvement on MindView. A paired context analysis further shows that all eleven generators obtain lower overall scores under the expanded context setting. These findings motivate us to investigate whether task-specific supervision can improve target-view generation and whether models can use additional multi-view evidence effectively. We therefore fine-tune BAGEL on the MindView training dataset, improving its overall score by 24.3 points and yielding gains across all seven MindView tasks. Beyond these generation gains, the fine-tuned model also yields higher scores on three spatial-understanding benchmarks without training on their annotations, suggesting that learning to generate spatially grounded views may benefit spatial understanding. To improve evidence utilization under expanded context, we propose MindCue, a training-free spatial evidence selector guided by a target-view hypothesis. MindCue reverses the drop in overall score under expanded context and outperforms the standard-context baseline. Overall, MindView provides a concrete testbed for generative multi-view spatial intelligence.

### 🤖 AI 总结

**一句话总结**：Spatial intelligence has recently been assessed through generative tasks such as spatially grounded image editing, yet language-guided generation of spatially consistent views from partial multi-view ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MindView, Benchmarking, Generative, Multi-View, Spatial, Intelligence, has, recently

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28622v1) | [下载PDF](https://arxiv.org/pdf/2610.28622v1.pdf)

---

## [16. KoalaGS: Complexity-Aware Continuous Level of Detail for Gaussian Splatting](https://arxiv.org/abs/2610.28615v1)

**作者**：Radu Beche, Raoul de Charette  
**分类**：cs.CV  
**发布时间**：2026-10-20

### 📄 论文摘要

Deploying a trained 3D Gaussian Splatting scene under shrinking compute budgets requires one primitive set to remain effective when rendered at smaller prefixes. In this continuous level of detail (LoD) setting, the challenge is to decide which Gaussians should retain capacity as the budget decreases. A pilot study on 3DGS-MCMC reconstructions shows that image complexity, computed from the input views before optimization, predicts where reconstruction error concentrates in image and 3D space. It also reveals that simple regions contain too many Gaussians and degrade as much as complex ones at lower budgets, despite being inherently cheaper to represent. Subsequently, in KoalaGS, during training we use this complexity prior to bias relocation toward poorly reconstructed areas while ensuring smooth degradation across LoDs. A primitive importance score then enables inference at low-capacity, while preserving the scene structure. Tested across three datasets, KoalaGS maintains competitive full-capacity quality while significantly improving quality across the budget spectrum, yielding smoother transitions across LoDs, and enabling faster progressive streaming.

### 🤖 AI 总结

**一句话总结**：Deploying a trained 3D Gaussian Splatting scene under shrinking compute budgets requires one primitive set to remain effective when rendered at smaller prefixes. In this continuous level of detail (Lo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, KoalaGS, Complexity-Aware, Continuous, Level, Detail, Gaussian, Splatting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28615v1) | [下载PDF](https://arxiv.org/pdf/2610.28615v1.pdf)

---

## [17. Neural Implicit Energy Optimization for LiDAR Mapping](https://arxiv.org/abs/2610.28598v1)

**作者**：Hrishikesh Viswanath, Md Ashiqur Rahman, Chi Lin 等 5 位作者  
**分类**：cs.CV, cs.GR, cs.LG  
**发布时间**：2026-10-20

### 📄 论文摘要

Neural implicit representations provide memory-efficient signed distance field (SDF) parameterizations for large-scale LiDAR scenes, but the geometry recovered from sparse and often noisy inputs carries jitter and artifacts. Classical geometric optimization techniques resolve such artifacts with surface energy functionals, whose minimizers correspond to smooth surfaces. Motivated by this principle, we formulate neural LiDAR mapping as the optimization of energy functionals over the parameter space of neural implicit representations. Specifically, we regularize the signed distance field with an energy functional defined on the shape operator of its level set, which represents the curvature of the surface, thus encouraging smoothness along the surface. This adapts classical geometric priors to the scale of million-point LiDAR maps. Experiments on large-scale datasets show reconstructions with improved smoothness at preserved geometric fidelity, and no additional inference-time cost. The code is publicly available at \href{https://github.com/HrishikeshVish/nieo}{https://github.com/HrishikeshVish/nieo}

### 🤖 AI 总结

**一句话总结**：Neural implicit representations provide memory-efficient signed distance field (SDF) parameterizations for large-scale LiDAR scenes, but the geometry recovered from sparse and often noisy inputs carri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Neural, Implicit, Energy, Optimization, LiDAR, Mapping, representations, provide

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28598v1) | [下载PDF](https://arxiv.org/pdf/2610.28598v1.pdf)

---

## [18. Can a Display Be Used for Rapid LiDAR-Camera Extrinsic Calibration?](https://arxiv.org/abs/2610.28571v1)

**作者**：Zuhao Zou, Xiangcheng Hu, Jianhao Jiao 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-20

### 📄 论文摘要

ScreenCalib enables light detection and ranging (LiDAR)--camera extrinsic calibration using an ordinary programmable display, providing known visual markers and controlled geometry while reducing dedicated target preparation. The camera observes displayed AprilTags, whereas the LiDAR measures the physical screen surface and boundary, requiring indirect cross-modal association. Display geometry introduces association ambiguities, while indoor clutter complicates extraction. ScreenCalib addresses these challenges through tag-guided display extraction, geometric hypothesis generation and refinement, and surrounding scene edges for ambiguity resolution. The single-pose mode requires only one static placement. The joint multi-pose mode combines independent static observations through cross-pose consensus and jointly refines the shared extrinsics and tag scale, reducing sensitivity to tag-size measurement errors without requiring continuous motion or inter-pose trajectory estimation. Experiments in simulation and on three different sensor platforms cover mechanical and nonrepetitive LiDARs in clean and cluttered environments. Benchmark results show that ScreenCalib outperforms competitive calibration-board-based methods in translation accuracy. Joint multi-pose refinement further reduces mean rotation and translation errors across the three platforms and improves rendered-map alignment. Evaluation across readily available displays, including cell phones, tablets, laptops, computer monitors, and televisions, further examines ScreenCalib's versatility as a practical alternative to dedicated calibration targets. The source code is available at https://github.com/ZuhaoZou2026/ScreenCalib.

### 🤖 AI 总结

**一句话总结**：ScreenCalib enables light detection and ranging (LiDAR)--camera extrinsic calibration using an ordinary programmable display, providing known visual markers and controlled geometry while reducing dedi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Be, Can, Display, Used, Rapid, LiDAR-Camera, Extrinsic, Calibration?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28571v1) | [下载PDF](https://arxiv.org/pdf/2610.28571v1.pdf)

---

## [19. Continual Concept Personalization in Diffusion Models via Residual-Space Adaptation](https://arxiv.org/abs/2610.28567v1)

**作者**：Yuzhi Liu, Enis Simsar, Giulia Lanzillotta 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-10-20

### 📄 论文摘要

Text-to-image personalization aims to equip pretrained diffusion models with the ability to learn user-specific concepts from only a few reference images. Existing methods, however, typically train each concept independently or assume that all concepts are available simultaneously. In practical applications, concepts often arrive sequentially, requiring models to continually learn new subjects, objects, or styles while minimizing interference with previously acquired concepts. We address this continual concept personalization setting by extending residual-space adaptation to the stochastic adaptation process of pretrained diffusion models. Our work achieves the highest concept fidelity among competing continual personalization methods while maintaining near-zero forgetting. Beyond these empirical gains, the learned residual-space dynamics reveal where adaptation capacity is concentrated within the diffusion model. Restricting adaptation to the identified layers by our method preserves nearly the same performance while reducing the number of trainable parameters by up to 72\%, demonstrating that residual-space dynamics can identify the layers that contribute most to continual concept personalization and directly guide more parameter-efficient adaptation.

### 🤖 AI 总结

**一句话总结**：Text-to-image personalization aims to equip pretrained diffusion models with the ability to learn user-specific concepts from only a few reference images. Existing methods, however, typically train ea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Continual, Concept, Personalization, Models, via, Residual-Space, Adaptation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28567v1) | [下载PDF](https://arxiv.org/pdf/2610.28567v1.pdf)

---

## [20. CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding](https://arxiv.org/abs/2610.28530v1)

**作者**：Om Shivam Verma, Shaya Farahmand, Lingjun Zhao 等 4 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-10-20

### 📄 论文摘要

Collaborative perception enables agents to retrieve the scene semantics and geometry beyond the field of view of any individual agent. This broader scene understanding enhances transportation safety and improves efficiency in multi-robot systems. However, existing collaborative semantic occupancy methods rely on dense 3D voxel annotations and are limited to recognizing objects within a predefined set of semantic classes. To overcome these limitations, we present CoGaussian, an open-vocabulary Gaussian-based collaborative semantic occupancy prediction framework. CoGaussian represents a scene as a set of foundation model-aligned sparse 3D Gaussians, which serve as a compact representation for communicating and fusing geometric and semantic information across multiple agents. On the Semantic-OPV2V benchmark, our method outperforms existing open-vocabulary single-agent approaches, highlighting the effectiveness of open-vocabulary collaborative scene understanding.

### 🤖 AI 总结

**一句话总结**：Collaborative perception enables agents to retrieve the scene semantics and geometry beyond the field of view of any individual agent. This broader scene understanding enhances transportation safety a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, CoGaussian, Open-Vocabulary, Gaussian-based, Collaborative, Scene, Understanding, perception

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28530v1) | [下载PDF](https://arxiv.org/pdf/2610.28530v1.pdf)

---

## [21. Copyright Leakage Detection in AI Generated Videos](https://arxiv.org/abs/2610.28524v1)

**作者**：Shaif Chowdhury, Moshiur Rahman Tonmoy  
**分类**：cs.CV  
**发布时间**：2026-10-20

### 📄 论文摘要

Video generation models can create realistic-looking video footage from images and text prompts. Some of the recent advances have raised concerns about the reproduction of copyrighted visual content. However, copyright leakage detection in generated videos remains largely unexplored.   In this paper, we introduce a new benchmark data set for copyright leakage detection, comprising 50 copyrighted concepts, each with 5 images. For each concept, we have 5 videos created using the image+prompt video generation model and the prompt-only video generation model. Following that, we develop an AI toolset based on a contrastive retrieval framework that formulates copyright leakage detection as a video-to-image retrieval problem by matching aggregated video frame embeddings against a database of copyrighted image embeddings. Our method uses a single similarity threshold and retrieves the most similar copyrighted reference as supporting evidence.   We conducted experiments showing strong retrieval and detection performance, achieving 99.6\% detection accuracy with only a single false negative. These results show the effectiveness of the retrieval-based method for scalable and explainable copyright leakage detection in AI-generated videos. Data can be accessed publicly from https://zenodo.org/records/21386117 and the source code for this project is publicly available at https://github.com/Shaif95/video-cp-Leakage.

### 🤖 AI 总结

**一句话总结**：Video generation models can create realistic-looking video footage from images and text prompts. Some of the recent advances have raised concerns about the reproduction of copyrighted visual content. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Copyright, Leakage, Detection, Generated, Videos, Video, generation, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28524v1) | [下载PDF](https://arxiv.org/pdf/2610.28524v1.pdf)

---

## [22. Latent Bridge: From Video Latents to 3D Geometry via Feature Alignment](https://arxiv.org/abs/2610.28521v1)

**作者**：Shuai Zhang, Zhanpeng Ouyang, Zhengqing Chen 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-20

### 📄 论文摘要

Video generation and feed-forward 3D reconstruction typically use separate representations, requiring RGB decoding and visual re-encoding to recover geometry from generated latents. We propose Latent Bridge, which connects video generative latent spaces with geometric feature spaces to directly predict 3D geometry from video latents. We develop representation-specific bridges for Wan2.1 and V-RAE, enabling feed-forward prediction of cameras, depth, and 3D point clouds without the intermediate RGB pathway. Each bridge is trained on RGB videos through feature distillation, while the video encoder and geometry model remain frozen. Training requires neither ground-truth geometry nor execution of the downstream geometric aggregator or prediction heads. At inference, the same video latents support both RGB decoding and geometry prediction. The same trained bridge can be reused for image-to-video and text-to-video generation within the same video latent space, without bridge retraining. Experiments on Co3Dv2 and WildRGB-D demonstrate competitive geometric reconstruction quality, efficient end-to-end generation and reconstruction, and faster latent-to-geometry decoding, highlighting latent alignment as a practical and reusable interface between video generation and 3D reconstruction. Our code is available at: https://github.com/hustvl/Latent-Bridge.

### 🤖 AI 总结

**一句话总结**：Video generation and feed-forward 3D reconstruction typically use separate representations, requiring RGB decoding and visual re-encoding to recover geometry from generated latents. We propose Latent ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Latent, Bridge, Video, Latents, Geometry, via, Feature

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28521v1) | [下载PDF](https://arxiv.org/pdf/2610.28521v1.pdf)

---

## cs.LG

## [23. Planning under Noise with Neural Operators](https://arxiv.org/abs/2610.28623v1)

**作者**：Michael Chen, Hong Chul Nam, Xi Deng 等 4 位作者  
**分类**：cs.LG, cs.RO  
**发布时间**：2026-10-20

### 📄 论文摘要

Planning under uncertain control execution noise requires reliable feedback policies across diverse environments. We introduce Planning Under Noise (PUN), a neural operator that learns noise-aware value fields for planning in unseen geometries. Building on an established screened-Poisson formulation of stochastic optimal control, we address two challenges: specifying boundary conditions that support navigation across varying geometries and efficiently computing fields with reliable gradients. Zero-Dirichlet obstacle boundaries terminate sampled paths at walls, weakening the goal signal along long routes and making it harder to estimate reliably. We instead impose reflecting Neumann conditions on obstacles and a Dirichlet condition at the goal, allowing sampled paths to continue exploring free space until they reach the target. To solve the resulting PDE without a configuration-space mesh, we extend a Monte Carlo (MC) solver, Walk on Stars (WoSt), to higher dimensions. However, local MC fluctuations can reverse estimated gradient directions and cause planning failures, making direct planning require costly sampling. PUN amortizes this computation by learning geometry-to-field mappings from noisy, partially converged Monte Carlo labels, avoiding expensive convergence for every training example. At inference, test-time scaling uses bounded local search guided by the predicted global field. We evaluate PUN on planning tasks across dimensions. Across four noise levels, PUN matches or outperforms all compared planners, achieving 95-100% success on the 4D replanning benchmark while maintaining the lowest runtime. At the highest tested noise level in 4D, PUN achieves 10.7-60.6% relative gains in success rate over other methods while running 3.29-32.15 times faster.

### 🤖 AI 总结

**一句话总结**：Planning under uncertain control execution noise requires reliable feedback policies across diverse environments. We introduce Planning Under Noise (PUN), a neural operator that learns noise-aware val...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Planning, under, Noise, Neural, Operators, uncertain, control, execution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28623v1) | [下载PDF](https://arxiv.org/pdf/2610.28623v1.pdf)

---

## [24. PaPi: Parallel Picard-Duhamel Integration for Fast Neuro-Spectral Architectures](https://arxiv.org/abs/2610.28591v1)

**作者**：Arthur Bizzi, Márcio Marques, Kleyton Da Costa 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-20

### 📄 论文摘要

Neuro-spectral architectures (NeuSA) are a class of physics-informed neural networks (PINNs) that have proven effective for solving time-dependent PDEs in the frequency domain. However, training and inference often rely on costly numerical integration of the learned vector field, typically using sequential Runge-Kutta time stepping, which limits temporal parallelism. We introduce PaPi, an integration scheme inspired by weakly nonlinear flows that enables time-Parallel inference through exponential integration and a Duhamel-Picard scheme. We show that the Duhamel-Picard iteration converges exponentially for all flows, and provide explicit error bounds that depend on how close the flow is to linear. Experiments show that PaPi accelerates training and inference by up to two orders of magnitude, achieving training times of under one second for low-dimensional PDE learning problems, while maintaining competitive predictive accuracy.

### 🤖 AI 总结

**一句话总结**：Neuro-spectral architectures (NeuSA) are a class of physics-informed neural networks (PINNs) that have proven effective for solving time-dependent PDEs in the frequency domain. However, training and i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PaPi, Parallel, Picard-Duhamel, Integration, Fast, Neuro-Spectral, Architectures, NeuSA

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28591v1) | [下载PDF](https://arxiv.org/pdf/2610.28591v1.pdf)

---

## [25. The Dynamics of Collapse and Recovery in Clustered Federated Learning](https://arxiv.org/abs/2610.28565v1)

**作者**：Priyanka Sinha, Snigdhansu Chatterjee  
**分类**：cs.LG, math.DS  
**发布时间**：2026-10-20

### 📄 论文摘要

Clustered federated learning (CFL) can suffer from cluster collapse. In particular, under unfavorable initialization, early client assignments concentrate heterogeneous groups on one cluster model, which is then trained toward a pooled compromise, while another model receives no updates. Since the current models determine client routing and routing determines subsequent model updates, we formulate clustered federated learning as control of an unknown dynamical system, with cluster models as the evolving state, client routing patterns as the control input, and routing interventions as state dependent controllers. In a two group linear model, we identify an initialization region in which greedy routing makes collapse self reinforcing. We then derive finite horizon error dynamics showing how routing interventions can reverse collapse by repeatedly training the starved model, primarily with updates from its compatible group. Motivated by this condition, each client uses blocked EXP3 to choose between greedy routing and interventions that redirect updates toward unused models. Experiments show that with simpler predictors and faster specialist formation, autonomous controller selection recovers usable specialists from unfavorable starts that trap standard CFL baselines. In transformed FEMNIST, the synchronized-entry configuration with persistent commitment recovers usable specialists in settings where the autonomous controller configuration often does not. Code and scripts for reproducing the experiments and figures are available at https://github.com/prsinha1/FedRecover.

### 🤖 AI 总结

**一句话总结**：Clustered federated learning (CFL) can suffer from cluster collapse. In particular, under unfavorable initialization, early client assignments concentrate heterogeneous groups on one cluster model, wh...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Dynamics, Collapse, Recovery, Clustered, Federated, Learning, CFL

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28565v1) | [下载PDF](https://arxiv.org/pdf/2610.28565v1.pdf)

---

## [26. Asymmetric Bidirectional Predictive Dynamics in Google Search and COVID-19 Time Series: A Multi-Horizon Forecast-Error Analysis](https://arxiv.org/abs/2610.28563v1)

**作者**：Andrei Velichko, Imen Mahmoud  
**分类**：cs.LG  
**发布时间**：2026-10-20

### 📄 论文摘要

Online search activity is widely used as a digital trace of information seeking during epidemics, but its predictive value is often reduced to correlation, a selected lag, or a single forecast-error score. We examine eight pre-specified Google Trends-COVID-19 pairs in both directions using matched LightGBM forecasts over rolling 400-day windows and horizons of 1-14 days. Log-RMSE gain is combined with forecast-error distribution entropy (FEDE), which captures horizon-dependent changes in the signed error distribution. The resulting directional predictive signature comprises response class, RMSE effect, FEDE endpoint and early-slope responses, persistence across rolling regimes, and horizon profile. For screening candidate directions, we also introduce a relative persistence-weighted directional predictive response strength (DPRS) on a within-study 0-100 scale; 100 denotes the strongest observed response in the comparison set, not an absolute coupling maximum. The pairs show concordant, RMSE-only, FEDE-only, and mixed responses. "loss of smell" -> reported cases is accuracy-dominant, with mean log-RMSE gain 0.104 (about 9.9% equivalent RMSE reduction) and DPRS 100, whereas the reverse direction is FEDE-dominant (D_FEDE=0.048; DPRS=42). "covid test" -> positive rate is FEDE-dominant (D_FEDE=0.039; positive in 72% of windows; DPRS=98) despite negative RMSE gain, while "lockdown" -> stringency is the clearest concordant case (DPRS=78). World-level symptom/case pairs are less persistent. Thus, forecast accuracy and error-distribution dynamics are complementary, predictive effects can be direction- and metric-dependent, and forecast horizon is part of the relationship. Aggregated regime-level patterns should not be extrapolated to individual time points or interpreted as evidence of causality.

### 🤖 AI 总结

**一句话总结**：Online search activity is widely used as a digital trace of information seeking during epidemics, but its predictive value is often reduced to correlation, a selected lag, or a single forecast-error s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Asymmetric, Bidirectional, Predictive, Dynamics, Google, Search, COVID-19, Time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28563v1) | [下载PDF](https://arxiv.org/pdf/2610.28563v1.pdf)

---

## [27. Convergence of stochastic gradient descent for learning linear neural networks](https://arxiv.org/abs/2610.28561v1)

**作者**：Gabin Maxime Nguegnang, Bubacarr Bah, Holger Rauhut 等 4 位作者  
**分类**：cs.LG, math.OC  
**发布时间**：2026-10-20

### 📄 论文摘要

Stochastic gradient descent (SGD) is the cornerstone of modern deep learning, yet its theoretical convergence properties remain poorly understood in non-convex settings. To address this gap, we study SGD dynamics in deep linear neural networks - simplified models that retain key non-convex characteristics while remaining analytically tractable. Building on recent results for gradient descent, we extend convergence guarantees to SGD under regularized squared loss. We establish almost sure boundedness of SGD iterates. Using the framework of asymptotic pseudotrajectories from stochastic approximation theory, our analysis establishes then, for both deterministic and adaptive step-size choices, convergence of SGD to the set of critical points under mild conditions (without relying on Lipschitz properties or whitened data). To our knowledge, this is the first work providing almost sure convergence guarantees for SGD in deep linear networks, bridging the gap between theoretical optimization and practical stochastic training.

### 🤖 AI 总结

**一句话总结**：Stochastic gradient descent (SGD) is the cornerstone of modern deep learning, yet its theoretical convergence properties remain poorly understood in non-convex settings. To address this gap, we study ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Convergence, stochastic, gradient, descent, learning, linear, neural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28561v1) | [下载PDF](https://arxiv.org/pdf/2610.28561v1.pdf)

---

## [28. When Do LLMs Help with Feature Selection? A Systematic Empirical Study](https://arxiv.org/abs/2610.28556v1)

**作者**：Fateme Memar, Dongjie Wang, Arvin Agah  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-20

### 📄 论文摘要

Large language models (LLMs) can leverage semantic feature names alongside summary statistics for tabular feature selection, yet it remains unclear when such information improves subset selection relative to established statistical methods. We investigate this question within an 18-dataset framework comprising 10 datasets for Group Relative Policy Optimization (GRPO) training, 2 for checkpoint validation, and 6 held-out evaluation datasets. We compare five classical baselines, frozen Qwen2.5-7B and Llama-3.3-70B selectors, and two GRPO-adapted Qwen2.5-7B models, reporting classification ROC-AUC and regression R^2 separately and using dataset-wise ranks for cross-task comparison. Across five seeded evaluation partitions, classical selectors generally achieve higher predictive performance than the tested 7B LLM/RL selectors, including under a pre-specified ~33% feature budget with strict train-only classical fitting, while the 7B selectors retain compact subsets. A cardinality-matched semantic sensitivity experiment shows that, for Zero-shot Qwen-7B, informative feature names improve regression performance over anonymized and shuffled alternatives (+0.1964 and +0.1606 mean R^2), whereas aggregate classification differences are smaller (+0.0159 and +0.0084 ROC-AUC) and dataset-dependent. These results characterize when semantic information benefits LLM-based feature selection and show that classical selectors remain strong baselines for predictive tabular feature selection.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) can leverage semantic feature names alongside summary statistics for tabular feature selection, yet it remains unclear when such information improves subset selection rela...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, LLM, When, Help, Feature, Selection?, Systematic, Empirical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28556v1) | [下载PDF](https://arxiv.org/pdf/2610.28556v1.pdf)

---

## [29. Learning Computational Structure for Sample-Efficient Prediction](https://arxiv.org/abs/2610.28555v1)

**作者**：Hangyu Zhou, Constantine Dovrolis, Stephen Mussmann  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-20

### 📄 论文摘要

Statistical learning in high dimensions suffers from the curse of dimensionality. Fortunately, many functions of practical interest are compositionally sparse, meaning they admit a composition of local functions, each depending on only a few variables, allowing sample complexity to depend on local arity rather than ambient dimension. Yet realizing this benefit requires exploiting hidden compositional structure, which theory does not establish for practical gradient-based training. We study this gap with CSFRBench, a controlled benchmark that hides the target's compositional computation during training but retains it for diagnosis, and find that dense networks and sparsity-based baselines leave much of that benefit unrealized. Inspired by the spatial organization of biological neural circuits, we introduce Learned Wiring (LeWi): each neuron has a learned low-dimensional embedding, only nearby neurons connect, and embeddings and weights are trained jointly. LeWi improves sample efficiency on targets with hierarchical structure, intermediate reuse, or independent modules. Across 32 additional targets generated by independently sampled computation graphs, LeWi is the most sample-efficient method not given the target graph, with 27% lower mean learning-curve area than dense networks. Dense networks perform better on targets with a single high-arity function. LeWi's representations and connectivity align with the target computation. On 17 world-model prediction tasks spanning control, navigation, and manipulation, LeWi beats the dense baseline on 16 and wins 99/119 baseline comparisons. These results show that jointly learning connectivity and weights can exploit computational structure to improve sample efficiency.

### 🤖 AI 总结

**一句话总结**：Statistical learning in high dimensions suffers from the curse of dimensionality. Fortunately, many functions of practical interest are compositionally sparse, meaning they admit a composition of loca...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Computational, Structure, Sample-Efficient, Prediction, Statistical, high, dimensions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28555v1) | [下载PDF](https://arxiv.org/pdf/2610.28555v1.pdf)

---

## [30. Discount Yourself: Self-inclusive Freshness-weighted Gossip for Decentralised Learning under Client Outages](https://arxiv.org/abs/2610.28545v1)

**作者**：Qiyuan Wang, Ke Xiao, Christos Anagnostopoulos  
**分类**：cs.LG, cs.DC  
**发布时间**：2026-10-20

### 📄 论文摘要

Decentralised federated learning (DFL) trains personalised models on devices that average with their neighbours rather than with a central server. Real devices, however, are often offline for hours or days, and a client returning from an outage can recover only by aggregating the models its neighbourhood holds. We observe that the stalest of these models is usually the client's own, a case that existing staleness-aware rules, which discount only the models a client receives, do not address. We formalise aggregation after an outage as estimating the state of a fully available network and derive three principles. First, the receiver must be discounted like any neighbour. Every rule that weights it at least as much as each neighbour has an error that grows without bound with the outage, whereas discounting all candidates by relative staleness keeps the error bounded. Second, staleness must be measured as inherited lag rather than age, since local training resets a model's age but not the lag it absorbed from stale neighbours. We introduce the effective lag, which tracks this quantity at the cost of one scalar per message. Third, the discount must be steep, because absorbed lag persists in every later round. These principles define Self-inclusive Freshness-weighted Gossip (SFG), a family of drop-in aggregation rules with the communication and computation of decentralised federated averaging, whose guarantees hold for the stale receiver itself. On three image benchmarks and eight outage processes, including real smartphone availability traces, the lag-based members SFG-L and SFG-Cut consistently outperform decentralised federated averaging and recent age-of-information rules, and ablations show that each principle is necessary. The analysis also explains why tuned limited merging from gossip learning is effective.

### 🤖 AI 总结

**一句话总结**：Decentralised federated learning (DFL) trains personalised models on devices that average with their neighbours rather than with a central server. Real devices, however, are often offline for hours or...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Discount, Yourself, Self-inclusive, Freshness-weighted, Gossip, Decentralised, Learning, under

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.28545v1) | [下载PDF](https://arxiv.org/pdf/2610.28545v1.pdf)

---

