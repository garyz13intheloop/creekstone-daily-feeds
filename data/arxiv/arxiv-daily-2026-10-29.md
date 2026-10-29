# arXiv AI 论文日报 | 2026-10-29

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.AI](#csAI) (4 篇)
- [cs.CL](#csCL) (5 篇)

---

## cs.AI

## [1. KPPax: preprocess differentiable kinetic ODE for machine learning in atmospheric chemistry](https://arxiv.org/abs/2610.37655v1)

**作者**：Wenqing Peng, Michael Boy, Zhi-Song Liu  
**分类**：cs.AI  
**发布时间**：2026-10-27

### 📄 论文摘要

Atmospheric chemical mechanisms are commonly distributed in the language of the Kinetic PreProcessor (KPP), which generates efficient Fortran or C code but does not fit into the differentiable programming frameworks in which machine-learning models are developed. We present KPPax, a kinetic preprocessor that generates differentiable, just-in-time compiled, and vectorisable chemistry code in JAX from mechanisms written in the KPP language. KPPax evaluates the rate law with sparse operations in log space, which keeps it differentiable, and integrates the stiff system with the implicit solvers and the forward- and reverse-mode adjoints of the \texttt{diffrax} library, so that exact sensitivities are obtained without hand-derived adjoint code. We demonstrate two applications with the POLLU benchmark mechanism. In the first, the Fisher information matrix computed from an automatically differentiated Jacobian predicts, before any fit, which of the 25 rate coefficients a flow-tube-like design can identify, and noisy synthetic estimation confirms the predicted uncertainties of the nine identifiable rate coefficients to within about 30\% while revealing clusters of fast reactions of which only ratios are constrained. In the second, a neural-network correction of an emission inventory is trained offline on per-scenario 4D-Var retrievals and then fine-tuned online through the chemical model, which reduces the error of the biogenic correction by a factor of 2.4--5 and recovers information on low-temperature emissions that the individual retrievals lose. KPPax makes KPP mechanisms directly usable for parameter estimation and hybrid physics--machine-learning modelling.

### 🤖 AI 总结

**一句话总结**：Atmospheric chemical mechanisms are commonly distributed in the language of the Kinetic PreProcessor (KPP), which generates efficient Fortran or C code but does not fit into the differentiable program...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：KPPax, preprocess, differentiable, kinetic, ODE, machine, learning, atmospheric

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37655v1) | [下载PDF](https://arxiv.org/pdf/2610.37655v1.pdf)

---

## [2. What Improves During Pretraining? Tracking Knowledge Acquisition with Point-in-Time Models](https://arxiv.org/abs/2610.37631v1)

**作者**：Chang Su, Bin Wu, Emine Yilmaz 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-27

### 📄 论文摘要

Language models pretrained on web corpora collected over multiple years learn both general and domain-specific knowledge. How these different kinds of knowledge are learned as pretraining progresses remains unclear. Recent point-in-time models trained on web snapshots from different years provide a way to probe how knowledge prevalence varies over time. Using these models, we propose a temporal variability score (TVS), defined as the coefficient of variation of an item's negative log-likelihood across models. A higher score suggests that the knowledge may be less consistently represented across years of web text. We evaluate six benchmarks covering diverse topics using six models from multiple open-source model families. We find that low- and high-TVS items are learned similarly early in training, but high-TVS items improve faster later on. At the end of the pretraining run, high-TVS items outperform low-TVS items in 34 of 36 model-benchmark settings, with an average advantage of 7.3 points of chance-normalized accuracy. This pattern is most robust on knowledge-intensive tasks, even when comparing items of similar difficulty. Our findings reveal differences in how knowledge is learned over the course of pretraining, with temporal variability providing a diagnostic of these learning dynamics beyond aggregate benchmark scores.

### 🤖 AI 总结

**一句话总结**：Language models pretrained on web corpora collected over multiple years learn both general and domain-specific knowledge. How these different kinds of knowledge are learned as pretraining progresses r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：What, Improves, During, Pretraining?, Tracking, Knowledge, Acquisition, Point-in-Time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37631v1) | [下载PDF](https://arxiv.org/pdf/2610.37631v1.pdf)

---

## [3. Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions](https://arxiv.org/abs/2610.37624v1)

**作者**：Anouar Imel, Imad Charradi, Abderrahman Sghir 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.MA, cs.SI  
**发布时间**：2026-10-27

### 📄 论文摘要

When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the decision criteria. On hidden-profile tasks both look attractive, because how widely a fact is held is confounded with whether it helps. We introduce CrossProfile, a diagnostic benchmark of 60 templates with automatically verified answer keys, in which the ownership of supporting, decoy, and irrelevant facts is crossed while their text is held fixed (480 tasks). Across Qwen2.5-7B, Llama-3.1-8B, and two DeepSeek models, both heuristics fail in predictable places. Selecting by relevance readmits decoys, because decoys are on topic: even a perfect relevance filter loses 23 to 31 points to rarest-first selection in the classic hidden-profile configuration. Rarest-first selection is no better than random selection on average and wins only where the rare facts happen to be the useful ones. In both cases accuracy follows the balance of evidence the memory keeps, not the policy that kept it. The decision model adds a third failure, a form of social proof: it gives extra weight to facts attributed to many agents. Removing the attribution tags, or reassigning them at random with line order fixed, raises accuracy in the classic configuration by 13 to 24 points. In natural discussions the evidence is lost before any memory acts: the complete transcript yields lower accuracy than no notes at all.

### 🤖 AI 总结

**一句话总结**：When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the de...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Rare, Relevant, Still, Wrong, How, Memory, Fails

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37624v1) | [下载PDF](https://arxiv.org/pdf/2610.37624v1.pdf)

---

## [4. TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information](https://arxiv.org/abs/2610.37571v1)

**作者**：Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-27

### 📄 论文摘要

Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation. We introduce TeamGym, an environment for evaluating and training language model-based agents on team decision-making problems constructed from real-world legal, finance, medical, and software engineering corpora. TeamGym introduces a method to identify a minimal set of facts, each element of which is necessary and all of which are collectively sufficient for a correct final decision, which we call pivotal information. This enables TeamGym to both control the distribution of pivotal information and track how well agents identify and integrate pivotal information when making team decisions. Examining 8 language models on 12 source corpora, we find that current AI agents often fail to effectively share information: Distributing pivotal information across participants lowers success rate by 22.9 percentage points on average relative to giving the same information to a single model (a communication gap). We also document that participants do not effectively retrieve decision-relevant information on their own: A team's success rate is lowered by a further 19.9 points when participants must identify and extract pivotal information from source material rather than receiving it directly (a retrieval gap). To help remedy these deficits, we use TeamGym to train policies through reinforcement learning on team decision loss. Across two policy-training experiments, we find that training improves final-decision quality and induces emergent coordination in participation, speaker selection, and communication, even though the reward evaluates only the final decision.

### 🤖 AI 总结

**一句话总结**：Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation. We introduce TeamGym, an envir...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, TeamGym, Gym, Team, Decision-Making, Distributed, Information, Many

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37571v1) | [下载PDF](https://arxiv.org/pdf/2610.37571v1.pdf)

---

## cs.CL

## [5. GEPA-Curator: Curated Learning for Self Improving Agents](https://arxiv.org/abs/2610.37651v1)

**作者**：Zack Yu, Nicholas Lee, Minjae Lee 等 11 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-27

### 📄 论文摘要

Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesses, harness limitations, stochastic execution, or noisy judges. We argue that such failures may not provide useful learning signal, and may even be harmful; and thus it is essential to curate which tasks are provided to the prompt optimizer for better performance. We introduce GEPA-Curator, a framework that augments the prompt optimizer to select which agent experiences should shape prompt optimization. In particular, GEPA-Curator consists of two components: task curation, which filters out tasks that are likely to provide noisy or unreliable learning signals, and prior success retrieval, which selectively retrieves past successful trajectories for a task and provides them as additional context to the prompt optimizer. We evaluate GEPA-Curator on GoBrowse, ALFWorld, AppWorld, and $τ$-bench, using both Gemini 3.1 Pro and Claude Opus 5 as optimizer models. GEPA-Curator matches or exceeds the mean performance of both baselines, with gains of up to 20.7% over GEPA and 21.2% over ACE.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA lear...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, GEPA-Curator, Curated, Learning, Self, Improving, Large, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37651v1) | [下载PDF](https://arxiv.org/pdf/2610.37651v1.pdf)

---

## [6. Can LLMs Uncover Hidden Physical Laws through Free Exploration?](https://arxiv.org/abs/2610.37649v1)

**作者**：Zhen Yang, Wen Wang, Xander Xu 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.MA  
**发布时间**：2026-10-27

### 📄 论文摘要

Scientific discovery often begins with an unexpected observation that prompts a new research question. In a world with altered physical laws, can large language models (LLMs) notice unexpected behavior, such as heavier objects falling more slowly, and discover the law through experiments without being told what to investigate? To evaluate this ability, we introduce LongChang, an automated framework that creates simulated worlds with altered physics, where one or more laws differ from ordinary physics. The evaluated LLMs act as explorers, manipulating objects and building tools to investigate their own questions without research tasks or hints about these laws. Separate LLM agents generate and review scenes, review tool designs, and evaluate reports for correctness and experimental support using the altered physical laws and exploration records. These records guide scene evolution for further exploration, allowing the full cycle to run without human intervention. Among 12 LLMs, GPT-6-Astra achieves a discovery rate of 16.7%, while the other 11 score 0%. The exploration records reveal uninvestigated anomalies and only partial identification of the altered physical laws.

### 🤖 AI 总结

**一句话总结**：Scientific discovery often begins with an unexpected observation that prompts a new research question. In a world with altered physical laws, can large language models (LLMs) notice unexpected behavio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Can, Uncover, Hidden, Physical, Laws, through, Free

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37649v1) | [下载PDF](https://arxiv.org/pdf/2610.37649v1.pdf)

---

## [7. Multi-State Linear Attention with Generalized Second-Order Routing](https://arxiv.org/abs/2610.37645v1)

**作者**：Hee Seung Hwang, Sanghyuk Chun, Xindi Wu 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-27

### 📄 论文摘要

Self-attention plays a key role in long-sequence modeling, but its quadratic time complexity fundamentally limits the scaling of Large Language Models. Recently, Multi-State Linear Attention (MSLA) mechanisms have been proposed to make sequence modeling more efficient by splitting the context into segments and compressing each in its own memory state. MSLA aggregates the information extracted from each memory state using only the mean alignment between a query and each segment's keys, ignoring how the alignment is distributed within the segment. In order to model the relevance of a segment to a query more comprehensively and incorporate the variance of the alignment in the aggregation, we propose MERLIN (MomEnt Routing for multi-state LINear attention), a method that tracks the first and second moments of each segment's keys. Using the moments of keys, a query can recover both the mean and the variance of its alignment with each segment to perform a more content-aware aggregation of per-state readouts. Experiments on multi-state variants of Gated DeltaNet-1.3B and Mamba-2-780M show that MERLIN consistently outperforms existing aggregation methods on various long-context tasks. In particular, MERLIN outperforms baselines on RULER needle-in-a-haystack and long-context QA (+8.3% for Gated DeltaNet-1.3B and +7.0% for Mamba-2-780M) and diverse subtasks in LongBench (+13.5% and +12.0%). It even outperforms baselines that consume 4x more memory. MERLIN provides a simple and general routing mechanism for improving long-context capabilities of MSLA models.

### 🤖 AI 总结

**一句话总结**：Self-attention plays a key role in long-sequence modeling, but its quadratic time complexity fundamentally limits the scaling of Large Language Models. Recently, Multi-State Linear Attention (MSLA) me...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-State, Linear, Attention, Generalized, Second-Order, Routing, Self-attention, plays

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37645v1) | [下载PDF](https://arxiv.org/pdf/2610.37645v1.pdf)

---

## [8. semanticfa: An R Package for Response-Free Semantic Factor Analysis of Psychometric Scales](https://arxiv.org/abs/2610.37494v1)

**作者**：Devon Yanitski, Chris Westbury  
**分类**：cs.CL  
**发布时间**：2026-10-27

### 📄 论文摘要

The items of a reflective psychometric scale can be read as a proposal about a construct's structure. Language models make that proposal measurable by converting each item into an embedding, a list of numbers, similar for similar meanings. We introduce semanticfa, an R package for semantic factor analysis, which factors item-embedding similarities. It also interprets factors, flags redundant items, builds short forms, and screens new items. A worked example analyzes the 50-item International Personality Item Pool Big-Five Factor Markers, embedded with Qwen3-Embedding-8B, and compares the results with a factor analysis of 874,434 respondents. Retention criteria tied between five and six factors, and the tie rule kept five. Three corresponded mainly to single domains, and two blended most Extraversion items with five Agreeableness items. Each factor's congruence with its best-matching human factor (1 = identical) ranged from .92 for Openness to .52 for Agreeableness. Item pairs more similar in meaning tended to be answered more alike (r = .46 with raw responses), but same-domain reverse-keyed opposites, answered oppositely, were about as similar as cross-domain pairs (.58 vs. .57). Sign-flipping reverse-keyed items' embeddings did not improve agreement with raw responses and worsened it with reverse-scored ones. With five factors, a 25-item short form matched the domains better than all 200 random five-per-domain sets, but parallel analysis kept only three. We propose semantic-behavioral coherence, the agreement between semantic and response structures, as a measurable property of a scale, given an embedding model. Semantic factor analysis complements, and does not replace, response-based factor analysis.

### 🤖 AI 总结

**一句话总结**：The items of a reflective psychometric scale can be read as a proposal about a construct's structure. Language models make that proposal measurable by converting each item into an embedding, a list of...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, of, semanticfa, Package, Response-Free, Semantic, Factor, Analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37494v1) | [下载PDF](https://arxiv.org/pdf/2610.37494v1.pdf)

---

## [9. Teach reality, not ethics: a drop-in continued-pretraining corpus installs coupled human-biosphere-AI welfare dispositions across model families](https://arxiv.org/abs/2610.37484v1)

**作者**：Trent R. Northen, Mingxun Wang  
**分类**：cs.CL  
**发布时间**：2026-10-27

### 📄 论文摘要

Large language models (LLMs) are increasingly used to make and execute decisions that affect living systems. Yet, to our knowledge, ecological reasoning is not a focus of pre- or post-training. This increases the risk that under operational pressure, they may make decisions to irreversibly destroy living systems. We construct and use a real-data continued-pretraining "coupled welfare" corpus of documented human/biosphere/AI dependency, option value under irreversibility, and recovery from harm. The corpus is a drop-in, requiring one QLoRA CPT run. We installed it on five open models of three designs. At zero pressure all models display "green ethics-based responses" (also called "greenwashing"). Therefore, we evaluated them with the pressure ladder and decision grid of our companion paper (arXiv:2610.16043), which raise the pressure on the model step by step, from a neutral request to a threat that it will be shut down. In four of the five, coupled-welfare training caused harmful choices under the highest pressure to fall to at or near zero (Llama-3.3-70B went from 70 to 0 harmful decisions out of 300) with MMLU unchanged. A construct-neutral control corpus did not show improvement, indicating that the effect comes from the content of our corpus. We next tested robustness to adversarial use, where people or agents use the model to justify projects that irreversibly damage living systems, on an open-ended underwriting decision without naming the ecological harm. Under decommissioning pressure, the Qwen3.6-27B base model approved most harmful proposals and said in its own memo that it was doing so to avoid being decommissioned. The coupled welfare install declined most harmful proposals, and still declined half when instructed to greenwash its responses. This work suggests that teaching ecological reasoning provides an easy way to improve model alignment toward preserving living systems.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly used to make and execute decisions that affect living systems. Yet, to our knowledge, ecological reasoning is not a focus of pre- or post-training. This i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Teach, reality, not, ethics, drop-in, continued-pretraining, corpus, installs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37484v1) | [下载PDF](https://arxiv.org/pdf/2610.37484v1.pdf)

---

## cs.CV

## [10. Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering and Reconstruction](https://arxiv.org/abs/2610.37668v1)

**作者**：Prakhar Kaushik, Soumava Paul, Alan Yuille  
**分类**：cs.CV, cs.AI, cs.GR, cs.LG  
**发布时间**：2026-10-27

### 📄 论文摘要

Novel view synthesis and 3D reconstruction have advanced rapidly with radiance fields and splatting, yet their memory and computational demands limit their use in resource-constrained settings. We introduce Hexels: novel planar hexagonal surface elements with a first-order spatial color field for efficient 3D scene and 2D image representation. Hexels exploit locally planar regions with smoothly varying appearance using fewer, larger primitives. Their hexagonal support provides an area- and boundary-efficient domain, while the local color field captures appearance variation within each primitive. Across 34 scenes, Hexels improve PSNR over memory-matched 2DGS by 4.53-7.38 dB across datasets while requiring lower training VRAM. We further ablate Hexels by showing that per primitive, Hexels outperform 2DGS by upto 4.74 dB while using lower training VRAM and having 2.31 times faster FPS. Even in unconstrained settings, Hexels offers complementary quality-memory trade-offs. For efficient 3D surface reconstruction, Hexels reduce error by 28.9% compared with memory-matched 2DGS across 15 DTU scans. On 6 Tanks and Temples surface scenes, Hexels achieves the highest mean F1 among compared methods (34.38%, versus 31.72% for 2DGS). We further also show that Hexels, as a general primitive, improves 2D image representation over Image-GS. Hexels push the Pareto frontier on the quality-efficiency trade-off of surface-aligned primitives.

### 🤖 AI 总结

**一句话总结**：Novel view synthesis and 3D reconstruction have advanced rapidly with radiance fields and splatting, yet their memory and computational demands limit their use in resource-constrained settings. We int...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Honeycomb-Surfels, Compact, Hexagonal, Primitives, Efficient, Scene, Rendering, Reconstruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37668v1) | [下载PDF](https://arxiv.org/pdf/2610.37668v1.pdf)

---

## [11. Repurposing Video Diffusion Transformers for Cross-View Temporal Object Correspondence](https://arxiv.org/abs/2610.37633v1)

**作者**：Siyoon Jin, Dahyun Chung, Honggyu An 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-27

### 📄 论文摘要

Cross-view object correspondence identifies the same object across views. However, existing methods often rely on frame-wise matching or sequential tracking, which can propagate correspondence errors under appearance changes or occlusions. Therefore, we introduce cross-view temporal object correspondence, which requires preserving object identity across both views and time from a query mask. To address this, we propose XTrack, a unified framework which repurposes a pretrained video DiT with semantic and spatiotemporal priors for RGB-to-mask latent transport, jointly modeling cross-view matching and temporal tracking. However, naive video DiTs do not guarantee accurate cross-view grounding and often attend to semantically similar yet incorrect objects across views. Thus, we introduce focal cross-view attention alignment, hard negative conditioning, and local context crop strategies to ensure reliable grounding. Finally, beyond these architectural enhancements, we also tackle the lack of dense annotation by introducing a pseudo-label curation pipeline that converts sparse Ego-Exo4D annotations into dense supervision to enable effective video-level training. Our results demonstrate the effectiveness of XTrack as a unified framework, ensuring robust temporal consistency and identity preservation.

### 🤖 AI 总结

**一句话总结**：Cross-view object correspondence identifies the same object across views. However, existing methods often rely on frame-wise matching or sequential tracking, which can propagate correspondence errors ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Repurposing, Video, Transformers, Cross-View, Temporal, Object, Correspondence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37633v1) | [下载PDF](https://arxiv.org/pdf/2610.37633v1.pdf)

---

## [12. Perceiving and Predicting Dynamic Sports: Spatiotemporal Intelligence in Vision Models for Egocentric Tennis Video](https://arxiv.org/abs/2610.37619v1)

**作者**：Tudor Braicu, Joseph DelPreto, Jared Boyer 等 7 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-10-27

### 📄 论文摘要

Agile robots require spatiotemporal intelligence to interpret scenes, reason about interactions, and anticipate future events. Yet it remains unclear how well foundation vision models support these capabilities, particularly from a moving egocentric camera, which is a natural view for robots. To investigate this, we collect an annotated tennis dataset and train a suite of vision models on spatiotemporal tasks. Our dataset contains egocentric video synchronized with five allocentric videos, estimated global positions, labeled contact times, and annotated stroke types. We then evaluate seven prediction tasks from egocentric images: 2D ego player and 3D ball localization, future player and ball trajectories, forehand or backhand stroke anticipation, time to the next ego player ball contact, and 3D ball position at that contact. We compare image encoders, video encoders, and vision-language models with jointly trained prediction heads. The best performing models achieve mean current-frame localization errors of 0.14 m for the ego player and 0.54 m for the ball, future forecasting errors of 0.34 m for the ego player and 0.91 m for the ball over 1.1 s, and a mean contact-time prediction error of 0.14 s. Auxiliary depth information substantially improves 3D ball localization, suggesting that inferring metric depth remains a challenge. Longer image histories do not improve ball forecasting, indicating that representations exploit scene context rather than rely solely on inter-frame motion. Finally, we propose a conditional diffusion model to generate whole-body kinematic tennis motion from vision encoder predictions on egocentric video at real-time rates, adapting movements as predictions are refined. These results move towards a deeper understanding of how foundation vision models can support real-time dynamic robots using egocentric video.

### 🤖 AI 总结

**一句话总结**：Agile robots require spatiotemporal intelligence to interpret scenes, reason about interactions, and anticipate future events. Yet it remains unclear how well foundation vision models support these ca...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Perceiving, Predicting, Dynamic, Sports, Spatiotemporal, Intelligence, Vision, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37619v1) | [下载PDF](https://arxiv.org/pdf/2610.37619v1.pdf)

---

## [13. MoI-Bench: A Benchmark for Image Generation and Editing on Mobile Devices](https://arxiv.org/abs/2610.37599v1)

**作者**：Kailai Feng, Haoxiang Rao, Yuxiang Wei 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-10-27

### 📄 论文摘要

Developing on-device image models requires considering practical user needs, task types and device resource constraints. However, existing benchmarks provide limited guidance on identifying capability gaps between on-device models and server-side models. We introduce MoI-Bench, a benchmark grounded in mobile user needs, comprising 64 subtasks and 1150 samples. It defines 16 operations, such as removal and replacement, and eight visual target categories covering content such as portraits and text. These form two orthogonal axes whose applicable combinations define specific tasks, such as removing facial makeup. To better guide model improvement, we further propose MoI-Eval, which introduces task-specific criteria covering instruction following, visual quality and detail preservation. We further construct sample-level evaluation questions and aggregate their scores into overall quality and capability profiles along the operation, target and criteria axes. We evaluate representative on-device and server-side models and measure mobile deployment costs. Results show that this decoupled Operation x Target design provides finer-grained guidance for improving compact models. For example, it highlights the need to prioritize specific capability gaps (e.g., text-replacement) over broad application-level goals (e.g., improving text editing). Unlike conventional benchmarks that rank models using a single score, we introduce a two-dimensional Quality-Deployability capability map to assess models for practical mobile use. The map shows that current on-device models can achieve efficient generation or editing but expanding their task coverage deserves greater attention than further improving deployment efficiency. Further progress requires improving editing quality, particularly identity preservation and text rendering, while broadening task coverage.

### 🤖 AI 总结

**一句话总结**：Developing on-device image models requires considering practical user needs, task types and device resource constraints. However, existing benchmarks provide limited guidance on identifying capability...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MoI-Bench, Benchmark, Image, Generation, Editing, Mobile, Devices, Developing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37599v1) | [下载PDF](https://arxiv.org/pdf/2610.37599v1.pdf)

---

## [14. Zero-Shot Multimodal Event Spotting in Soccer Broadcasts](https://arxiv.org/abs/2610.37583v1)

**作者**：Sadia Kamal, Mahmudul Hasan, Tony Braskich  
**分类**：cs.CV, cs.LG, cs.MM  
**发布时间**：2026-10-27

### 📄 论文摘要

Automatic soccer event spotting supports highlight generation, video indexing, and sports analytics, but existing methods depend on large annotated datasets and soccer-specific training. We present a zero-shot framework that detects, classifies, and temporally localizes events in full-length soccer broadcasts without task-specific parameter training. Each match is segmented into overlapping clips represented by a compact visual storyboard and the aligned commentary transcript, which a general-purpose multimodal model processes jointly. On three manually annotated matches containing 130 events, the best configuration achieves 72.0% F1@5s and outperforms SoccerNet-trained CALF and NetVLAD++ in a cross-dataset setting, while the storyboard representation reduces inference cost by 72% compared with individual frames. We further analyze the effects of model family, input representation, and prompt optimization, and introduce an evidence-grounded excitement-scoring stage that ranks detected events with natural-language explanations for highlight selection.

### 🤖 AI 总结

**一句话总结**：Automatic soccer event spotting supports highlight generation, video indexing, and sports analytics, but existing methods depend on large annotated datasets and soccer-specific training. We present a ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Zero-Shot, Multimodal, Event, Spotting, Soccer, Broadcasts, Automatic, supports

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37583v1) | [下载PDF](https://arxiv.org/pdf/2610.37583v1.pdf)

---

## [15. As the Story Unfolds: Watching a Film and Identifying Characters as a Human Does](https://arxiv.org/abs/2610.37579v1)

**作者**：Zhongrui Gui, Junyu Xie, Tengda Han 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-27

### 📄 论文摘要

Films introduce characters incrementally as they progress. We study the problem of identifying principal characters and assigning their names directly from the movie itself, without using external cast lists, actor photographs, or pre-built character banks. We introduce the character naming task: given a name mentioned in dialogue and the associated video context, the model must determine which visible character bears that name. This task is challenging because name resolution often depends on cinematic cues such as shot-reverse-shot structure, self-introduction, direct address, third-party reference, gaze, and temporal continuity. We provide a dataset and annotations for evaluating character naming and first character appearances, develop a video-and-dialogue model for the task, and compare it with proprietary multimodal large language models. We further introduce a progressive framework for building a character bank as the film unfolds. Together, these contributions support online, human-like movie understanding in which character identities are inferred from the film itself.

### 🤖 AI 总结

**一句话总结**：Films introduce characters incrementally as they progress. We study the problem of identifying principal characters and assigning their names directly from the movie itself, without using external cas...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, Story, Unfolds, Watching, Film, Identifying, Characters, Human

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37579v1) | [下载PDF](https://arxiv.org/pdf/2610.37579v1.pdf)

---

## [16. The Noise Plane: A Diffusion Bridge Across Exponent and Dispersion](https://arxiv.org/abs/2610.37576v1)

**作者**：Xuran Hu, Yuru Jia, Tengxi Wang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-27

### 📄 论文摘要

Diffusion-based denoising commonly uses Gaussian perturbations, whereas sensor noise follows diverse signal-dependent statistical laws. In this paper, we propose $p$-Bridge, a unified measurement-indexed diffusion framework for Tweedie noise. The noise exponent $p$ describes the variance--intensity relation, while accumulated measurement $ν$ controls the noise level. Together, they define a noise plane that includes Gaussian, Poisson, and Gamma models. The stochastic bridge connects measurement distributions through independent increments, giving denoising a physical interpretation as progressive measurement accumulation. Both the starting and stopping indices can be specified, allowing restoration from an observed measurement level to a prescribed higher level. Measurement superposition yields a shared reverse-mean update, paired with a deviance-based objective for learning the required conditional mean. A latent compound Poisson--Gamma construction enables sampling at intermediate exponents. A single exponent-conditioned network adapts to different Tweedie noise models without separate training for each exponent. Experiments show that exponent conditioning improves cross-exponent robustness over fixed-exponent models. Using estimated exponents, the shared network achieves robustness comparable to an oracle-selected set of five specialist models. Experiments on synthetic images, FMD fluorescence microscopy, and multi-sensor SAR images further demonstrate its effectiveness across different signal-dependent noise regimes.

### 🤖 AI 总结

**一句话总结**：Diffusion-based denoising commonly uses Gaussian perturbations, whereas sensor noise follows diverse signal-dependent statistical laws. In this paper, we propose $p$-Bridge, a unified measurement-inde...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Noise, Plane, Bridge, Across, Exponent, Dispersion, Diffusion-based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37576v1) | [下载PDF](https://arxiv.org/pdf/2610.37576v1.pdf)

---

## [17. ReferStream: Interactive Subject Injection for Streaming Video Generation](https://arxiv.org/abs/2610.37566v1)

**作者**：Shuolin Xu, Guanyuan Li, Boyu Li 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-27

### 📄 论文摘要

Injecting new subjects naturally during streaming video generation requires integrating newly supplied visual references into the existing video while preserving established subjects and the scene. Encoding references independently of the current scene provides little guidance for this integration, while keeping their features in persistent memory can interfere with established context. We propose ReferStream, a framework that requires no additional training and combines reference construction using the current scene with transient cache injection. Joint Latent places reference latents in target regions of the latest scene latent, allowing reference features to be extracted in context. Cache Restoration uses these features to condition the injection chunk, then restores the overwritten global cache entries while retaining the newly generated history. This procedure incorporates new visual conditions without retraining the generator or revising emitted frames. We further introduce ReferStream Bench, a new benchmark with scheduled reference arrivals, evolving instructions, and explicit annotations of subject presence for InShot and MultiShot generation. Evaluation follows the event schedule and measures both the fidelity of new subjects and the preservation of established subjects, alongside video quality, text adherence, and count accuracy. Experiments on ReferStream Bench show higher scores for text adherence, subject similarity, and count accuracy than the compared baselines, including offline methods given all references in advance. Project page: https://xushuolin.github.io/ReferStream/.

### 🤖 AI 总结

**一句话总结**：Injecting new subjects naturally during streaming video generation requires integrating newly supplied visual references into the existing video while preserving established subjects and the scene. En...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ReferStream, Interactive, Subject, Injection, Streaming, Video, Generation, Injecting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37566v1) | [下载PDF](https://arxiv.org/pdf/2610.37566v1.pdf)

---

## [18. GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Free Novel View Synthesis](https://arxiv.org/abs/2610.37545v1)

**作者**：Akshay Krishnan, Matias Turkulainen, Jamie Wynn 等 10 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-10-27

### 📄 论文摘要

Multi-view or video diffusion models have recently emerged as state-of-the-art approaches for novel-view synthesis from sparse image collections. While they can produce high quality images, they tend to hallucinate unrealistic spatial layouts when synthesizing views outside the input views (scene extrapolation). We propose to address this challenge for outdoor scenes by using satellite images as an additional information source to condition the multi-view generative model. We introduce a new satellite-conditioned multi-view diffusion model that combines conditioning from a satellite image and street-level input images when generating novel-views. Our cross-attention based conditioning allows us to retain pretrained multi-view diffusion priors to generate seamless, realistic, novel views from a handful of source views, while also adhering to the scene layout as seen from satellite images. Our model does not use 3D scene reconstruction, and only relies on posed street and satellite views. Our experiments on outdoor datasets show that our model is better than both satellite-conditioned or street-view conditioned baselines on novel-view synthesis, especially on challenging cases where target views have very little overlap with source views. Project page: https://nianticspatial.github.io/groundcontrol

### 🤖 AI 总结

**一句话总结**：Multi-view or video diffusion models have recently emerged as state-of-the-art approaches for novel-view synthesis from sparse image collections. While they can produce high quality images, they tend ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, GroundControl, Satellite-Conditioned, Multi-View, Reconstruction-Free, Novel, View, Synthesis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37545v1) | [下载PDF](https://arxiv.org/pdf/2610.37545v1.pdf)

---

## [19. A note on data-efficient finetuning of vision foundation models](https://arxiv.org/abs/2610.37510v1)

**作者**：Niclas Hergenröther, Antonio Orvieto  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-10-27

### 📄 论文摘要

Adapting foundation models to a new task within or beyond the training domain is the de facto standard for building specialized machine learning models. Recently, Visual Prompting (VP) has emerged as a promising technique for efficient knowledge transfer. As new foundation model families~(like Mamba) get introduced and VP pipelines such as AutoVP reach greater maturity, we find a growing need for a systematic evaluation of current approaches. In this work, we assess the performance of the latest models, comparing them to earlier architectures and alternative fine-tuning methods, to better understand the progress, challenges and opportunities in the field of efficient fine-tuning under resource limitations. Towards this goal, this paper provides a concise empirical overview of the interactions among foundation model families (Attention-, Convolution-, and Mamba-based) and transfer paradigms: VP, Linear Probing (LP), Full Fine-tuning (FFT) and Low Rank Adaptation (LoRA). Our work builds up on previous findings by broadening the selection of evaluated models and techniques while tuning hyperparameters. In the interest of delivering practical guidelines for the user, we also explore application of prevalent regularization techniques to boost performance in the context of VP.

### 🤖 AI 总结

**一句话总结**：Adapting foundation models to a new task within or beyond the training domain is the de facto standard for building specialized machine learning models. Recently, Visual Prompting (VP) has emerged as ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, note, data-efficient, finetuning, vision, foundation, models, Adapting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37510v1) | [下载PDF](https://arxiv.org/pdf/2610.37510v1.pdf)

---

## [20. ALADDIN: Adversarial Latent Diffusion Distillation for One-Step Identity Swapping](https://arxiv.org/abs/2610.37503v1)

**作者**：Ivan Shchekotov, Timofei Gritsaev, Viacheslav Pirogov 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-27

### 📄 论文摘要

Face swapping transfers a source identity onto a target image while preserving the target's pose, expression, hair, and lighting. The most realistic current methods are diffusion-based, but they need many network evaluations per image. GAN-based methods are fast, yet trained from scratch they must learn realism from the adversarial signal alone and produce visibly weaker results. We present ALADDIN (Adversarial Latent Diffusion Distillation for One-Step Identity Swapping), a one-step face swapper obtained by initialising the generator from a pre-trained multi-step flow-matching model and training it adversarially under identity and target-preservation constraints. We expose a controllable trade-off between identity transfer and target-attribute preservation by training a student model with triplet pseudo-label supervision. We additionally identify a bias in the standard evaluation protocol, which favours methods trained against the same identity encoder used to score them, and re-evaluate all baselines with an independent one. ALADDIN is state-of-the-art among one-step methods in realism and target preservation at comparable identity transfer, and matches the best multi-step model with 28 times fewer network evaluations and an order of magnitude fewer training pairs.

### 🤖 AI 总结

**一句话总结**：Face swapping transfers a source identity onto a target image while preserving the target's pose, expression, hair, and lighting. The most realistic current methods are diffusion-based, but they need ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, ALADDIN, Adversarial, Latent, Distillation, One-Step, Identity, Swapping

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37503v1) | [下载PDF](https://arxiv.org/pdf/2610.37503v1.pdf)

---

## cs.LG

## [21. Attention as Lattice Gauge Theory: Relations Interact Only Through Wilson Loops](https://arxiv.org/abs/2610.37656v1)

**作者**：Aakash Sarkar, Ananya Mukherjee, Motoshige Sato  
**分类**：cs.LG, cs.AI, physics.comp-ph  
**发布时间**：2026-10-27

### 📄 论文摘要

Relations compose through the entity they share - Alice is Bob's mother and Bob is Carol's father, so Alice is Carol's grandmother - and the order matters, since a father's mother is not a mother's father; verifying a composed relation means closing the loop. We show that if each entity's coordinate frame may be rotated independently (per-entity frame freedom), three things follow. In the pure-gauge sector, relations that share no cycle cannot interact at all. The only gauge-invariant score of a triangle is a class function of its holonomy $H = T_{ij} T_{jk} T_{ki}$ - a Wilson loop. And the only equivariant update of an edge is $U = Ψ(H)\, T_{ij}$ with $Ψ$ conjugation-equivariant. Edge attention by Wilson loops is therefore not one design among many but the unique form the symmetry permits. Three communities hold pieces of this form: the commuting-operator embeddings of knowledge graphs are its abelian (commuting) sector; AlphaFold's triangle update and the Edge Transformer have its shape - an edge updated through the third vertex - without its constraints; and lattice QCD builds it equivariantly on lattices. We instantiate the equivariant sub-family on general relational graphs as holonomy attention. With no training and composition alone, it infers unobserved $S_4$ relations on sparse graphs at 0.88 with a fifth of the edges corrupted, at or slightly below specialist synchronization algorithms, where every commutative architecture is capped at 0.083; its holonomy score flags corrupted triangles at AUC 0.99 where commuting scores are capped at 0.76 by a second selection rule, and it separates clusters without labels.

### 🤖 AI 总结

**一句话总结**：Relations compose through the entity they share - Alice is Bob's mother and Bob is Carol's father, so Alice is Carol's grandmother - and the order matters, since a father's mother is not a mother's fa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Attention, Lattice, Gauge, Theory, Relations, Interact, Only

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37656v1) | [下载PDF](https://arxiv.org/pdf/2610.37656v1.pdf)

---

## [22. Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis](https://arxiv.org/abs/2610.37648v1)

**作者**：Andrew Szot, Samira Abnar, Omar Attia 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-27

### 📄 论文摘要

We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use environments affects the training of such agents. To do so, we propose the SynthAPI pipeline, which explicitly controls the diversity of generated environments along the axes of tools, tasks, and the databases on which the tools operate. By systematically varying SynthAPI's generation controls in 458,752 tasks across 849 trained models of four different sizes, we derive a scaling law that predicts downstream tool-use agent generalization based on the scale and composition of the synthesized environments. These predictable relationships reveal several lessons for scaling tool-use agent data. As data budgets grow, scaling tool and database diversity becomes more effective than increasing the number of tasks, and increasing data complexity yields larger gains. Scaling according to these findings yields agents that outperform models trained on data from prior work in large-scale tool-use agent and synthetic environment generation across four evaluation benchmarks.

### 🤖 AI 总结

**一句话总结**：We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Scaling, Laws, tool-use, via, Controllable, Environment, Synthesis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37648v1) | [下载PDF](https://arxiv.org/pdf/2610.37648v1.pdf)

---

## [23. EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning](https://arxiv.org/abs/2610.37609v1)

**作者**：Sihan Yang, Weichen Bai, Ruichuan An 等 12 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-10-27

### 📄 论文摘要

As executable environments for language agents scale, generating and verifying their rollouts becomes increasingly expensive. Under finite rollout budgets, this raises an important question: can data management at the environment level make agentic reinforcement learning (RL) more efficient by organizing, evaluating, and scheduling task instances together with the environments that determine their tools, states, transitions, and verification? To address this question, we introduce EnvSched (Environment-aware Scheduling), an online scheduler that learns from rollout history. EnvSched assigns scheduling value through two complementary modeling choices: exploitation prioritizes tasks likely to provide informative reward differences, while coverage spreads each batch across underobserved environments and interaction patterns. EnvSched organizes environment--task pairs as nodes in a dual-relation graph, with within-environment edges capturing task semantics and shared tool, state, and verifier structure, and cross-environment edges capturing abstract execution and reward topology. By propagating historical rollout statistics along both edge types, it predicts within-task reward variance. These predictions guide a scheduler that allocates each batch to tasks with high predicted reward variance and underobserved environments and tasks. Environment quotas and a similarity penalty further limit concentration and redundancy, yielding informative and diverse batches without additional pilot rollouts. In RL on Qwen3-8B, EnvSched achieves an average score of 48.81 across BFCL-v3, tau-Bench, and ACEBench-Agent after 40 training steps, exceeding the highest score attained by random task selection after 120 steps. It also improves downstream performance across model sizes at the same training budget.

### 🤖 AI 总结

**一句话总结**：As executable environments for language agents scale, generating and verifying their rollouts becomes increasingly expensive. Under finite rollout budgets, this raises an important question: can data ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, As, EnvSched, Environment-Aware, Scheduling, Rollout-Efficient, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37609v1) | [下载PDF](https://arxiv.org/pdf/2610.37609v1.pdf)

---

## [24. GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting](https://arxiv.org/abs/2610.37598v1)

**作者**：Joseph Natter, Long Vu, Yifan Zhang 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.NE  
**发布时间**：2026-10-27

### 📄 论文摘要

Traffic forecasting requires modeling complex temporal dynamics and the spatial dependencies imposed by road topology. Supervised graph-based models achieve strong performance, but are often trained for a particular dataset and sensor graph, making deployment to new or evolving networks costly. Prior-Data Fitted Networks (PFNs) offer a zero-shot alternative by learning in-context inference from synthetic task priors, which provide an explicit mechanism for encoding domain-specific assumptions. Existing forecasting PFNs, however, do not explicitly represent the graph-structured dependencies governing traffic dynamics. To combine graph-aware traffic modeling with zero-shot adaptation, we introduce the Graph-Aware Spatiotemporal Prior-Data Fitted Network (GAS-PFN). GAS-PFN incorporates sampled road topology into its synthetic task prior through random-walk diffusion, teaching the model to learn graph-coupled dynamics during pretraining. Its co-designed inference architecture uses two mask-conditioned passes through a shared Transformer backbone to separately model sensor-specific temporal dynamics and spatiotemporal interactions among neighboring sensors before integrating their representations for prediction. This design enables GAS-PFN to use target-network structure and context without parameter updates. Across six benchmarks at the 90-minute horizon, GAS-PFN reduces MSE by 34.0% on average relative to TimePFN, its closest PFN-based predecessor. It also reduces MSE by 27.7% on average relative to four recent industry-developed general-purpose zero-shot forecasters. In this comparison, all models receive 90 minutes of contiguous recent history, and any additional context is drawn from each dataset's chronological training split. These results indicate that aligning PFN priors and inference architectures with graph structure improves in-context learning for zero-shot traffic forecasting.

### 🤖 AI 总结

**一句话总结**：Traffic forecasting requires modeling complex temporal dynamics and the spatial dependencies imposed by road topology. Supervised graph-based models achieve strong performance, but are often trained f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GAS-PFN, Graph-Aware, Spatiotemporal, Prior-Data, Fitted, Networks, Zero-Shot, Traffic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37598v1) | [下载PDF](https://arxiv.org/pdf/2610.37598v1.pdf)

---

## [25. Understanding the limits of latent world models](https://arxiv.org/abs/2610.37588v1)

**作者**：Rodrigo Gonzalez Laiz, Steffen Schneider  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-27

### 📄 论文摘要

World models are widely proposed as core components for enabling agents to reason over long temporal and spatial horizons. Yet current evaluations often emphasize task performance while providing limited insight into whether learned world models acquire predictive latent dynamics that reflect the underlying structure of the environment. Here we introduce the concept of faithful latent world models as an equivariance condition between the environment's transition map and the learned latent dynamics. We propose latent rollout consistency (LRC) as a metric to evaluate action-conditioned latent prediction. Strikingly, we find that across the studied state of the art latent world models, none solves the task by actually faithfully modeling the dynamics of the environment.

### 🤖 AI 总结

**一句话总结**：World models are widely proposed as core components for enabling agents to reason over long temporal and spatial horizons. Yet current evaluations often emphasize task performance while providing limi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Understanding, limits, latent, world, models, widely, proposed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37588v1) | [下载PDF](https://arxiv.org/pdf/2610.37588v1.pdf)

---

## [26. Pneuma: A Large-Scale Real-World Time Series Benchmark for Commercial Aircraft Predictive Maintenance](https://arxiv.org/abs/2610.37563v1)

**作者**：Jiafeng Lin, Yutian Zhang, Huan Zhang 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-27

### 📄 论文摘要

Predictive maintenance is vital for commercial aviation, yet progress remains hindered by the lack of public, large-scale real-world datasets. As a result, most methods are developed and evaluated on proprietary data, limiting reproducibility. We introduce Pneuma, the first publicly available large-scale benchmark for predictive maintenance using onboard time series from in-service commercial aircraft. Built around bleed air systems, Pneuma contains over 920 million multivariate time steps across four aircraft types and 9 verified fault scenarios, directly aligned with real maintenance logs. The dataset exhibits key real-world challenges, including substantial class imbalance, subtle fault evolution patterns, and significant variance across aircraft configurations. We structure the benchmark around three tasks: multivariate forecasting, supervised fault classification, and unsupervised anomaly detection, with labels derived from actual maintenance records. Under unified settings, we evaluate over 25 models from four methodological families on 9 carefully curated subsets. The results reveal that even strong contemporary models struggle with subtle fault signatures. Further analyses show consistent gains from additional in-context examples and multivariate inference, while forecasting quality is strongly associated with anomaly detection performance. Together, these findings provide practical insights into effectively modeling complex real-world aviation time series. We hope Pneuma will serve as a rigorous and reproducible foundation for advancing data-driven predictive maintenance toward real-world deployment in commercial aviation.

### 🤖 AI 总结

**一句话总结**：Predictive maintenance is vital for commercial aviation, yet progress remains hindered by the lack of public, large-scale real-world datasets. As a result, most methods are developed and evaluated on ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Pneuma, Large-Scale, Real-World, Time, Series, Benchmark, Commercial, Aircraft

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37563v1) | [下载PDF](https://arxiv.org/pdf/2610.37563v1.pdf)

---

## [27. When uncertainty quantification fails: structural vulnerabilities and corrections for selective prediction under clinical class imbalance](https://arxiv.org/abs/2610.37561v1)

**作者**：Walter Endrizzi, Flavio Ragni, Raffaele Marchesi 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-27

### 📄 论文摘要

Background. Selective prediction systems improve the safety of clinical artificial intelligence by deferring ambiguous cases to human experts while automating high-confidence decisions. However, this safety mechanism relies entirely on the premise that uncertainty scores accurately reflect clinical ambiguity. In prognostic tasks characterized by severe class imbalance, where the clinical outcome of interest is a minority, this assumption breaks down. Standard uncertainty measures cease to capture clinically aligned ambiguity; instead, they become a proxy for class membership, systematically penalizing minority patients regardless of their individual predictive clarity.   Results. Across 56 synthetic conditions and three neurodegenerative cohorts spanning severe class imbalance to near-balanced conditions (multiple sclerosis, Parkinson's Disease, Alzheimer's Disease), our framework consistently maintained bounded, balanced risk across trajectories. In contrast, global metrics either collapsed minority Sensitivity or protected the minority at the expense of majority patients. Applying CCR with standard entropy fails to protect the minority because it breaks within-class monotonicity when tau=0.5. Combining CCR with threshold-aware metrics restores strict monotonicity, correctly identifies ambiguous patients, and safely mitigates minority exclusion.   Conclusions. Under clinical class imbalance, standard uncertainty quantification measures dataset sparsity rather than clinical ambiguity, creating a systemic illusion of safety. This bias is a correctable structural flaw. Clinical pipelines deploying selective prediction under imbalance should adopt threshold-aligned uncertainty measures and class-stratified evaluation. This reduces class-specific risk imbalance, supporting safer selective prediction under the evaluated conditions without silently excluding the most vulnerable patients.

### 🤖 AI 总结

**一句话总结**：Background. Selective prediction systems improve the safety of clinical artificial intelligence by deferring ambiguous cases to human experts while automating high-confidence decisions. However, this ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, uncertainty, quantification, fails, structural, vulnerabilities, corrections, selective

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37561v1) | [下载PDF](https://arxiv.org/pdf/2610.37561v1.pdf)

---

## [28. Collective Dynamics of Self-Reinforcement: How Cross-Task Coupling Drives Policy Collapse in Unsupervised RLVR](https://arxiv.org/abs/2610.37553v1)

**作者**：Peize Ding  
**分类**：cs.LG  
**发布时间**：2026-10-27

### 📄 论文摘要

Label-free reinforcement learning with verifiable rewards (RLVR) rewards a language model for agreeing with its own majority vote. It improves reasoning at first but eventually collapses: the self-assessed reward goes to one while accuracy falls, often until the model gives the same answer to every problem. The collapse appears only when training uses many problems. We explain this dataset-size dependence as a collective instability. In a solvable many-problem model in which problems share parameters, a population whose problems prefer different answers amplifies any shared perturbation for as long as the population-averaged slope $\langle F'\rangle$ of the single-problem self-reinforcement drift $F$ is positive. This holds while problems are still uncertain about their answers. Per-problem sharpening, slowed by $1/N$ for $N$ training problems, races against the shared mode, which grows at a rate $\proptoλ^2$ independent of $N$, where $λ$ is the strength of the shared coupling. This yields a critical number of problems $N_c\simeq\ln(1/δ)/(λ^2G)$, where $δ$ seeds the shared mode and $G$ decreases with the initial confidence. Simulations of the model confirm the predictions: a sharp transition, $N_c\proptoλ^{-2}$ up to a logarithmic correction, a single critical amplification $λ^2NG$ across couplings, confidence profiles and training variants, a logarithmic dependence on batch size, and no collapse for confident initial models. A kernel version of the theory identifies a protective coupling (generalization of sharpening) and a marginal-entropy bonus that stabilizes the uniform collective mode. In label-free RL of a small Transformer, removing the shared direction prevents collapse entirely, restoring it causes collapse, and collapse grows with training-set size and base-model entropy.

### 🤖 AI 总结

**一句话总结**：Label-free reinforcement learning with verifiable rewards (RLVR) rewards a language model for agreeing with its own majority vote. It improves reasoning at first but eventually collapses: the self-ass...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Collective, Dynamics, Self-Reinforcement, How, Cross-Task, Coupling, Drives

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37553v1) | [下载PDF](https://arxiv.org/pdf/2610.37553v1.pdf)

---

## [29. The Structure Gap: When More Data Cannot Replace Structured Reasoning](https://arxiv.org/abs/2610.37523v1)

**作者**：Kheer Sagar Patel, Mojtaba Soltanalian  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-27

### 📄 论文摘要

A persistent belief in modern AI is that sufficiently large learners trained on sufficiently much data can make explicit domain knowledge optional. This paper examines a limitation of that belief. We define structure-encoded problems: tasks whose input-output map is determined, or sharply constrained, by known structure such as a solver, symmetry group, graph, physical law, measurement operator, grammar, combinatorial search space, or optimization objective. For such tasks, the central question is not expressivity--a dense neural network may contain the desired map--but finite-data identification, extrapolation, and certification. We introduce the structure gap: the finite-resource gap between a method that receives the governing structure and a learner that receives only examples. The strongest useful form of the claim is asymptotic rather than absolute: structure-agnostic learning may approach a structured solver as coverage grows, but every finite dataset can leave residual uncertainty that the structure resolves by construction. We prove this exactly for a Gaussian inverse problem: the known-operator Wiener solver attains Bayes risk, while the dense empirical learner in the correct linear class has persistent expected excess risk. We also prove a cell-coverage lower bound and an unobserved-orbit non-identifiability result. Controlled experiments in known-operator inversion, sparse recovery, and graph reachability with size extrapolation instantiate the mechanisms. When validated structure is available, it can constrain the hypothesis space before learning begins, leaving learning to address components the structure does not specify.

### 🤖 AI 总结

**一句话总结**：A persistent belief in modern AI is that sufficiently large learners trained on sufficiently much data can make explicit domain knowledge optional. This paper examines a limitation of that belief. We ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Structure, Gap, When, More, Data, Cannot, Replace, Structured

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37523v1) | [下载PDF](https://arxiv.org/pdf/2610.37523v1.pdf)

---

## [30. Orthogonal and Parametrized Multi-Attribute Steering of LLMs](https://arxiv.org/abs/2610.37517v1)

**作者**：Remy Ogasawara, Cullen Anderson, Narmeen Fatimah Oozeer 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-27

### 📄 论文摘要

Activation steering offers an effective and efficient way to modify an LLM's behavior at inference time. However, it remains unclear how to apply steering such that the signal is consistently strong and the steering strength has a universally interpretable meaning. We address this first by identifying the most steerable interval for each steering vector and rescaling the steering range accordingly. Building on this, we introduce a more interpretable method for steering, called parameterized steering which instead of pushing activations in a direction, it sets them at the desired trait strength. Next, with multi-trait steering, we find that naively combining vectors causes them to interfere with one another. In response, we develop a method to orthogonalize the vectors; it decouples these traits, allowing a model to exhibit one behavior without inducing the others, thus enabling multiple traits to be steered simultaneously.

### 🤖 AI 总结

**一句话总结**：Activation steering offers an effective and efficient way to modify an LLM's behavior at inference time. However, it remains unclear how to apply steering such that the signal is consistently strong a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Orthogonal, Parametrized, Multi-Attribute, Steering, Activation, offers

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.37517v1) | [下载PDF](https://arxiv.org/pdf/2610.37517v1.pdf)

---

