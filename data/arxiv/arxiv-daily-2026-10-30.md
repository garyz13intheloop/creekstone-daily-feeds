# arXiv AI 论文日报 | 2026-10-30

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (8 篇)
- [cs.CV](#csCV) (10 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (7 篇)

---

## cs.AI

## [1. Collaborative AI agents for autonomous experimental research with solid-state quantum spins](https://arxiv.org/abs/2610.40589v1)

**作者**：El Mustapha Mansouri, Eikichi Kimura, Masato Koga 等 4 位作者  
**分类**：cs.AI, cs.MA, quant-ph  
**发布时间**：2026-10-29

### 📄 论文摘要

An autonomous research laboratory could conduct an entire study, from formulating questions to preparing manuscripts. Artificial intelligence (AI) offers one route towards this goal. Recent AI systems take on several research roles, but may draw conclusions that the evidence does not support. Here, we present an autonomous research laboratory in which agents based on large language models assess one another's work and can stop or redirect investigations. They can generate and reject research questions, require separate theoretical checks and conduct experiments designed to challenge their claims. We demonstrate these capabilities by investigating ensembles of quantum spins in diamond. The agents derived the minimum number of calibration settings needed to predict responses to a defined family of microwave pulse sequences. They checked the result computationally and designed experiments to distinguish competing predictions. An initial experiment agreed with the theoretical predictions, but repeated reference measurements showed that the signal was drifting during data collection. The agents therefore treated the result as inconclusive and revised the measurement protocol without relaxing the acceptance criteria. The revised experiment met those criteria and supported the theoretical predictions. This study demonstrates that collaborating AI agents can select research questions, derive theoretical results and test their predictions experimentally.

### 🤖 AI 总结

**一句话总结**：An autonomous research laboratory could conduct an entire study, from formulating questions to preparing manuscripts. Artificial intelligence (AI) offers one route towards this goal. Recent AI systems...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Collaborative, autonomous, experimental, research, solid-state, quantum, spins

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40589v1) | [下载PDF](https://arxiv.org/pdf/2610.40589v1.pdf)

---

## [2. VeriCUA: Verification as Agentic Exploration for Computer-Using Agents](https://arxiv.org/abs/2610.40578v1)

**作者**：Qiushi Sun, Da Yu, Alexander Knop 等 8 位作者  
**分类**：cs.AI, cs.CL, cs.CV  
**发布时间**：2026-10-29

### 📄 论文摘要

Building and scaling computer-using agents (CUAs) across desktop, mobile, and web environments requires reliable task-completion verification for data curation, evaluation, and reinforcement learning. Typical automated approaches prompt vision-language models (VLMs) to judge trajectories or generate programs to inspect application state. However, both rely on partial views of complex digital environments. VLM judges are restricted to supplied observations, while generated programs depend on accessible state. These views can omit decisive evidence or leave completion judgments unsupported. Tailoring separate verifiers to different platforms and access settings adds further engineering cost. We present VeriCUA, a platform-agnostic framework for verification through agentic exploration. It treats verification as dynamic evidence gathering and assessment within a shared procedure for online and offline settings across platforms and observation modalities. After inspecting the available context to construct a task rubric, the verifier selects GUI or code checks for unresolved requirements and combines their findings under explicit evidence rules. Experiments show improved agreement with reference labels over the compared baselines across these settings, with the largest offline gains on hard cases and stronger rejection of false completion claims online. Further analyses connect these gains to complementary evidence and test-time exploration.

### 🤖 AI 总结

**一句话总结**：Building and scaling computer-using agents (CUAs) across desktop, mobile, and web environments requires reliable task-completion verification for data curation, evaluation, and reinforcement learning....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Agent, VeriCUA, Verification, Agentic, Exploration, Computer-Using, Building

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40578v1) | [下载PDF](https://arxiv.org/pdf/2610.40578v1.pdf)

---

## [3. Comparing Human Role-Players and LLM-Simulated Clients in Online Counselling Training: An Analysis of Counselling Patterns](https://arxiv.org/abs/2610.40563v1)

**作者**：Eric Rudolph, Philipp Steigerwald, Jens Albrecht  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-10-29

### 📄 论文摘要

This study investigates the capabilities of Large Language Models to simulate counselling clients in educational role-plays in comparison to human role-players. Initially, we recorded role-playing sessions, where novice counsellors interacted with human peers acting as clients, followed by role-plays between humans and clients simulated by Mistrals Mixtral 8x7b using 4-bit quantization. These interactions were analysed with a counselling communication pattern system at sentence level. We investigated two key questions: (1) to what extent LLM-generated responses replicate authentic conversational dynamics and (2) whether counsellors' communication behaviour differs when interacting with human versus LLM-simulated clients. The findings highlight both similarities and differences in the application of counselling patterns across scenarios, showing the potential of LLM-based role-playing exercises to enhance counselling competencies and to identify areas for further refinement in virtual client simulations.

### 🤖 AI 总结

**一句话总结**：This study investigates the capabilities of Large Language Models to simulate counselling clients in educational role-plays in comparison to human role-players. Initially, we recorded role-playing ses...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Comparing, Human, Role-Players, LLM-Simulated, Clients, Online, Counselling, Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40563v1) | [下载PDF](https://arxiv.org/pdf/2610.40563v1.pdf)

---

## [4. FARMS: A Verifiable Foundation for Automated Computational Science](https://arxiv.org/abs/2610.40560v1)

**作者**：Di Wu, Ling Liang, Haizhao Yang  
**分类**：cs.AI, cs.LO  
**发布时间**：2026-10-29

### 📄 论文摘要

Automated computational science could accelerate discovery by selecting, adapting and developing numerical methods. This prospect requires mathematical knowledge that AI systems can interpret and reuse with explicit guarantees. Here we present FARMS, a faithful and efficient foundation that transforms computational mathematics into AI-ready computing knowledge. FARMS connects formal statements to source context, algorithmic meaning and quantitative guarantees through source preparation, reusable representations and semantic review. Across 171 targets in randomized numerical linear algebra and numerical partial differential equations, 157 were accepted by the pipeline, with mean estimated costs of US \$0.85-2.29 per target across sources. Lean-checked implications from explicit source premises connect selected statements to computational skills, illustrated by a heat-flow solve and wave-response compression. FARMS therefore supports an affordable, reusable knowledge foundation for trustworthy automated computational science.

### 🤖 AI 总结

**一句话总结**：Automated computational science could accelerate discovery by selecting, adapting and developing numerical methods. This prospect requires mathematical knowledge that AI systems can interpret and reus...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FARMS, Verifiable, Foundation, Automated, Computational, Science, could, accelerate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40560v1) | [下载PDF](https://arxiv.org/pdf/2610.40560v1.pdf)

---

## [5. Advancing Clinical Genomic Analysis with a Skill-Centred Agent](https://arxiv.org/abs/2610.40556v1)

**作者**：Qiaoyu Zheng, Weike Zhao, Yanjie Fan 等 13 位作者  
**分类**：cs.AI, q-bio.GN  
**发布时间**：2026-10-29

### 📄 论文摘要

Clinical genomic analysis requires experts to integrate evolving guidelines, databases, and computational evidence. As sequencing has become increasingly accessible, this complex and labor-intensive process has become a major bottleneck to the timely use of genomic information in clinical decision-making. To fill this gap, we developed ClinGeX, a large-language-model agent that composes 105 curated executable skills through task-specific retrieval and dependency-aware orchestration. On 223 temporally held-out benchmark cases, ClinGeX achieved 71.7\% macro-averaged task-level concordance with expert reference classifications, compared with 45.7\% for the strongest comparator. In a three-condition, counterbalanced human-AI collaboration study, 45 clinical genomic professionals assessed 135 clinically derived cases under routine (no AI assistance), DeepSeek-assisted and ClinGeX-assisted conditions. ClinGeX assistance increased raw case-level concordance across criterion-level variant analysis, genomic interpretation in rare disease and molecular oncology decision-making (51.1\%, 57.8\%, 64.4\% versus 15.6\%, 31.1\%, 20.0\% in comparator conditions) and reduced reported interpretation time in all scenarios. During an exploratory one-month real-world non-interventional assessment, 11 experienced professionals submitted feedback on 96 self-selected analysis episodes and reported frequent conclusion adoption and time savings. These findings support executable domain skills as a promising approach to augment specialist genomic interpretation.

### 🤖 AI 总结

**一句话总结**：Clinical genomic analysis requires experts to integrate evolving guidelines, databases, and computational evidence. As sequencing has become increasingly accessible, this complex and labor-intensive p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Advancing, Clinical, Genomic, Analysis, Skill-Centred, requires, experts

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40556v1) | [下载PDF](https://arxiv.org/pdf/2610.40556v1.pdf)

---

## [6. Ramanujan Challenge Results: AI-Assisted Evaluation Pipeline for Multi-Format Proofs](https://arxiv.org/abs/2610.40551v1)

**作者**：Alan Sorani, Ashvni Narayanan, Michael Shalyt 等 11 位作者  
**分类**：cs.AI, cs.CL, cs.SC, math.NT  
**发布时间**：2026-10-29

### 📄 论文摘要

As AI's mathematical capabilities rapidly improve, meaningful benchmarks are shifting from university-level problems and math olympiads to research-level mathematics. The Ramanujan Challenge is a benchmark comprised of research-level problems in number theory, including unpublished results and open conjectures. It presented concrete formulas for mathematical constants whose correctness can be checked numerically, while their proofs may require non-obvious mathematics. Here, we analyze the Challenge submissions, measuring the relative success of different AI models, Computer Algebra Systems (CAS), and formal tools. We find correct submissions that are conceptually distinct from the official solutions, and a proof of one of the published open conjectures. Evaluating the submissions exposed a second challenge: judging complex proofs reliably at scale. We introduce an AI-assisted evaluation pipeline for natural language proofs, CAS code, and Lean formalizations that assesses semantic and logical correctness. Compared with the conventional one-shot LLM judgment, our pipeline reduces false-positive verdicts on natural language proofs from 23% to 6% and improves judgment accuracy on supporting code from 46% to 58%. This approach provides a methodology for evaluating research-level mathematics at scale, with potential applications across mathematics and AI for science.

### 🤖 AI 总结

**一句话总结**：As AI's mathematical capabilities rapidly improve, meaningful benchmarks are shifting from university-level problems and math olympiads to research-level mathematics. The Ramanujan Challenge is a benc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Ramanujan, Challenge, Results, AI-Assisted, Evaluation, Pipeline, Multi-Format, Proofs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40551v1) | [下载PDF](https://arxiv.org/pdf/2610.40551v1.pdf)

---

## [7. Agentic University: Collaborative Agents for Personalized Learning](https://arxiv.org/abs/2610.40492v1)

**作者**：Jingru Fan, Tianle Zhou, Yunjie Zhou 等 13 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-10-29

### 📄 论文摘要

Large language models support personalized tutoring, content generation, and adaptive learning paths. However, capability development requires these resources and interactions to form a coherent learning process that evolves with the learner. A central challenge is to align goals, activities, and assessment while using learning evidence to decide what should follow. We introduce Human-Participatory Multi-Agent Organization and instantiate it in Agentic University (AU). In AU, learners participate as organization members and work with specialized agents to maintain a revisable Capability Program. The program connects personal goals, learning activities across modalities, and layered assessment, while learner feedback and performance guide subsequent support. Our evaluation shows advantages in program organization, assessment design, and revision quality. Users achieved larger mean assessment gains (12.19 versus 5.61 points on a 50-point scale) and reported stronger cognitive support. This work contributes an organizational approach to adaptive learning that makes learner participation a continuing basis for multi-agent coordination. The Agentic University project is available at \href{https://github.com/AgenticOrgLab/AgenticUniversity.git}.

### 🤖 AI 总结

**一句话总结**：Large language models support personalized tutoring, content generation, and adaptive learning paths. However, capability development requires these resources and interactions to form a coherent learn...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Agentic, University, Collaborative, Personalized, Learning, Large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40492v1) | [下载PDF](https://arxiv.org/pdf/2610.40492v1.pdf)

---

## cs.CL

## [8. Testimony from Timelines: Evidence-Grounded Significance Testing of Temporal Clinical Hypotheses](https://arxiv.org/abs/2610.40619v1)

**作者**：Chengyang He, Wenlong Zhang, Koduvayur Subbalakshmi 等 4 位作者  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-10-29

### 📄 论文摘要

Ask a language model whether sales tend to dip after a product recall, or whether one side effect tends to follow another after a vaccine, and it answers in a fluent sentence that reads like a finding, with no test behind it. Assertions about how events unfold across many cases fill the Web, and each is a temporal hypothesis that only a significance test over the right records can settle. The verifier must specify the null, select the test and decide which records bear on the hypothesis, and any of these choices can go wrong while the conclusion still comes out right. Yet benchmarks for language-model data analysis grade only the conclusion, with the relevant data handed over. We study the problem in health, where a wrong verdict is costly, and present STRATA, a benchmark that grades every decision on the way to a verdict: 8,735 hypotheses over the clinical timelines of vaccine adverse-event reports, with gold plans, evidence sets, p-values and verdicts derived under a released codebook and reproduced by a deterministic oracle. We also propose ART (articulate, retrieve, test), a staged paradigm that exposes each decision as an inspectable output. Extensive experiments with five model configurations show that systems fail mostly at choosing which records count, a verdict-evidence gap that accuracy alone conceals. ART closes most of this gap and brings a 31B open model to within 0.01 of the frontier models under the same paradigm; the frontier models succeed once given the codebook.

### 🤖 AI 总结

**一句话总结**：Ask a language model whether sales tend to dip after a product recall, or whether one side effect tends to follow another after a vaccine, and it answers in a fluent sentence that reads like a finding...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Testimony, Timelines, Evidence-Grounded, Significance, Testing, Temporal, Clinical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40619v1) | [下载PDF](https://arxiv.org/pdf/2610.40619v1.pdf)

---

## [9. When to Assist and What to Suggest: Joint Gating and Memory-Grounded Hint Generation in One Compact Decoder](https://arxiv.org/abs/2610.40611v1)

**作者**：A. J. A. Jubayer Talukder, Mohammad Ariful Haque  
**分类**：cs.CL, cs.AI, cs.HC  
**发布时间**：2026-10-29

### 📄 论文摘要

Proactive assistants offer short, memory-grounded hints during a conversation, deciding when to assist and what to suggest. Current systems split this between a gate and a larger generator; we evaluate both together on 28,058 decision points. Stage-wise generation scores are oracle-gate ceilings: behind a real gate, end-to-end exact match is 0.2619 against a ceiling of 0.2971, and end-to-end precision is 0.2387, leaving substantial headroom. A gate pays off through precision and compute, whose saving falls from 4.39x with an 8B generator to 1.38x with a 1B one. The memory profile drives hint quality: removing it costs 24.7 exact-match points (rescaled BERTScore 0.57 to 0.35), while retrieval and a larger generator add nothing on exact match. One 1B decoder can do both, gating from an intermediate layer and generating in the same pass. At its final checkpoint it matches or exceeds the two-model pipelines on automatic end-to-end measures with 1.31-1.76x less wall-clock time than the matched 1B pipeline; across three seeds, its deeper exit ties the separate gate. A human evaluation (1,144 ratings over 32 dialogues) supports the memory effect and rates the single model level with the matched 1B pipeline and below the 8B one. Graded metrics and LlamaPIE's native judge track human ratings more closely than exact match, which we report as a strict lower bound.

### 🤖 AI 总结

**一句话总结**：Proactive assistants offer short, memory-grounded hints during a conversation, deciding when to assist and what to suggest. Current systems split this between a gate and a larger generator; we evaluat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Assist, What, Suggest, Joint, Gating, Memory-Grounded, Hint

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40611v1) | [下载PDF](https://arxiv.org/pdf/2610.40611v1.pdf)

---

## [10. How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates](https://arxiv.org/abs/2610.40516v1)

**作者**：Max Neuwinger, Hanna Yukhymenko, Imanol Schlag  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-10-29

### 📄 论文摘要

Safety alignment for Large Language Models is heavily focused on English with limited multilingual representation, particularly damaging low-resource language performance. Related open training datasets are often limited in size or do not follow region-localized harmful topics to broaden the scope of alignment beyond cultures. We propose a scalable template-based augmentation pipeline to produce massive multilingual refusal and benign corpora, extracting safe templates from harmful prompts, translating them and then filling in the slots with culturally authentic entities, both harmful and benign. As a result, we release MSafeTemp, a validated corpus spanning 60 languages useful for multilingual safety alignment and evaluation. Using the dataset, we show that English-only evaluation misjudges multilingual safety: for several models, attacks that fail in English succeed once translated, while culturally localized variants expose further failures that translation alone misses. We also confirm that augmenting safety training data through templates allows for higher diversity and quality of alignment, resulting in improved safety performance beyond English. MSafeTemp and the respective pipeline are aimed at facilitating research and development of safer and more responsible models for less-represented cultures.

### 🤖 AI 总结

**一句话总结**：Safety alignment for Large Language Models is heavily focused on English with limited multilingual representation, particularly damaging low-resource language performance. Related open training datase...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Up, How, Aligned, Model, Scaling, Multilingual, Safety, Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40516v1) | [下载PDF](https://arxiv.org/pdf/2610.40516v1.pdf)

---

## [11. A Low-Rank Space Captures Linear Alignment Between LLM and Human Neural Activity During Naturalistic Language Listening](https://arxiv.org/abs/2610.40511v1)

**作者**：Zach Paris, Emily Finn  
**分类**：cs.CL, q-bio.NC  
**发布时间**：2026-10-29

### 📄 论文摘要

Large language models (LLMs) are increasingly used as computational models of human language processing, yet it remains unclear which components of their representations drive alignment with neural activity. Here, we use ridge reduced-rank regression to identify the brain-predictive subspace of LLM representations: the representational directions that support linear prediction of neural responses. Across three naturalistic language-listening datasets spanning intracranial electrophysiology and fMRI, and six model conditions spanning autoregressive, bidirectional masked, and randomly initialized language models, we find that full linear encoding performance can be recovered using only 1-3% of the original embedding dimensionality. These low-dimensional subspaces generalize across held-out participants and, to a lesser extent, across datasets, suggesting that neural predictivity is concentrated in a compact and partially shared representational space. We next compare these brain-predictive directions with the principal axes of variation in the embeddings. Principal component analysis requires substantially more dimensions to recover neural prediction, demonstrating that the directions most useful for predicting neural activity are distinct from those capturing the most overall variance within LLM representations themselves. Finally, characterizing the learned subspaces allows us to surface interpretable features that are overrepresented in neural activity above and beyond the LLM representations. Together, these results show that LLM-brain alignment is supported by a small, structured subset of model representations and provides a framework for better understanding exactly why these representations align. Code can be found at: https://github.com/thefinnlab/low-rank-alignment

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly used as computational models of human language processing, yet it remains unclear which components of their representations drive alignment with neural ac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Low-Rank, Space, Captures, Linear, Alignment, Between, Human

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40511v1) | [下载PDF](https://arxiv.org/pdf/2610.40511v1.pdf)

---

## [12. rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment](https://arxiv.org/abs/2610.40488v1)

**作者**：Art Kanke  
**分类**：cs.CL  
**发布时间**：2026-10-29

### 📄 论文摘要

Do research agents have taste, the judgment of which experiments are worth running before their outcomes are known? We give six frontier models seven recent NLP papers. Each model, working as a research agent alone or as a team, proposes minimum viable experiments (MVEs), forecasts whether each will pass a threshold it sets and ranks them. A separate executor then attempts every MVE, including those ranked last, and three model auditors judge the results. Of 415 MVEs, 194 are judged sound, valuable and new, but fewer than half of these (73) are also judged beyond the seed paper and non obvious. The agents' first choices match the auditors' most valued experiment more often than a random pick, but are not shown to improve on choosing the experiment written first. Their forecasts beat a base rate but are not measurably more accurate than those of a fresh instance of the same model given only the paper and registrations. Teams cost more without a clear overall improvement in proposal quality. The agents produce many worthwhile experiments, but the evidence that their rankings improve the choice of which to run remains limited. The evaluation harness and a dataset of all 415 MVEs, with their forecasts and audited outcomes, are available at https://github.com/ArtKanke/rTaste.

### 🤖 AI 总结

**一句话总结**：Do research agents have taste, the judgment of which experiments are worth running before their outcomes are known? We give six frontier models seven recent NLP papers. Each model, working as a resear...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, Agent, rTaste, Research, Have, Taste?, Evaluating, Early

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40488v1) | [下载PDF](https://arxiv.org/pdf/2610.40488v1.pdf)

---

## cs.CV

## [13. Luggage re-identification: A study of strategies towards a real-world application](https://arxiv.org/abs/2610.40643v1)

**作者**：Quentin Dhôte, Romaric Audigier  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-10-29

### 📄 论文摘要

Luggage re-identification (ReID) is a critical task in video surveillance for forensics, security or border management (suspicious or abandoned luggage recognition), as well as luggage management (lost luggage recovery). It enables the association of observations of the same luggage across disjoint camera views in complex environments such as airports, train stations and border crossing. While existing approaches primarily focus on appearance-based cropped image matching under relatively clean conditions, real-world scenarios are characterized by frequent occlusions, cluttered background and crowded scenes which significantly degrade performance. Yet, strategies leveraging the complementarity of multiple shots and views from different video streams is overlooked. In this paper, we study strategies for an end-to-end pipeline that operates from multiple video streams to detect and re-identify luggage. We evaluate different variants on a benchmark dataset acquired in real-world environments to address the questions of selecting and merging different views and shots of the same luggage as well as training on different environment datasets for an overall ReID performance improvement in practical applications.

### 🤖 AI 总结

**一句话总结**：Luggage re-identification (ReID) is a critical task in video surveillance for forensics, security or border management (suspicious or abandoned luggage recognition), as well as luggage management (los...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Luggage, re-identification, study, strategies, towards, real-world, application

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40643v1) | [下载PDF](https://arxiv.org/pdf/2610.40643v1.pdf)

---

## [14. SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization](https://arxiv.org/abs/2610.40640v1)

**作者**：Derong Jin, Xiyi Chen, Ming C. Lin 等 4 位作者  
**分类**：cs.CV, cs.SD  
**发布时间**：2026-10-29

### 📄 论文摘要

Recent progress in visual scene generation has extended beyond static 3D scenes toward the more challenging problem of generating dynamic 4D scenes from minimal input. However, sound, despite being intrinsically coupled with dynamic objects and events, remains largely unmodeled in prior work. We introduce Video-to-4DAVScene, a new task that turns a video into an explorable, time-varying 4D audio-visual scene, and present the SonoWorld4D framework for this task. Given a monocular video, our method generates a 360 static background, reconstructs explicit motion trajectories of dynamic, sound-emitting foreground objects, and synthesizes a physically-grounded sound field consistent across multiple sources through dual-space audio diffusion synchronization. The resulting 4D scene supports real-time novel-view visual and spatial audio rendering. Evaluation on real-world dynamic scenes and a user study demonstrates SonoWorld4D generates 4D audio-visual scenes with perceptually realistic, physically grounded spatial audio consistent with scene geometry and visual content.

### 🤖 AI 总结

**一句话总结**：Recent progress in visual scene generation has extended beyond static 3D scenes toward the more challenging problem of generating dynamic 4D scenes from minimal input. However, sound, despite being in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, Diffusion, SonoWorld4D, One, Video, Audio-Visual, Scene, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40640v1) | [下载PDF](https://arxiv.org/pdf/2610.40640v1.pdf)

---

## [15. Probing Spatial State Representations in Visual Foundation Models](https://arxiv.org/abs/2610.40636v1)

**作者**：Baiqiao Yin, Zhongang Cai, Ruisi Wang 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-10-29

### 📄 论文摘要

An observer sees only part of the surrounding world, yet must keep track of what lies beyond the current view. Spatial perception therefore involves more than recognizing individual images: it calls for a persistent spatial state that is updated under self-motion and used to guide action. Do visual foundation models provide representations that support such a state? We study this question through four levels of spatial capability---spatial structure, object persistence, predictive spatial update, and actionability---using frozen-feature probes on ten representations under streaming egocentric observations of static indoor environments. The resulting capability profiles vary across tasks, network layers, and prefix lengths: strong readout of the visible scene does not ensure accurate object persistence or future-feature retrieval. Matched controls separate readout accuracy from reliance on visual history and motion. Native future prediction retains recoverable spatial structure, but a spatial reader trained on real features does not transfer to predicted features unchanged. Finally, goal-dependent candidate selection does not establish reliable continuous action utility: predicted actions respond to goal changes, yet supplying the correct goal does not reliably improve progress. Across the four levels, object persistence and actionability build on camera-pose readout, whereas feature prediction builds on visible-scene readout. Together, these findings motivate evaluating spatial representations not only by what can be decoded from them, but by whether that information is maintained beyond observation, updated predictively, and used for goal-directed action.

### 🤖 AI 总结

**一句话总结**：An observer sees only part of the surrounding world, yet must keep track of what lies beyond the current view. Spatial perception therefore involves more than recognizing individual images: it calls f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Probing, Spatial, State, Representations, Visual, Foundation, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40636v1) | [下载PDF](https://arxiv.org/pdf/2610.40636v1.pdf)

---

## [16. Difficulty Calibration Across Time for Membership Inference in Diffusion Models](https://arxiv.org/abs/2610.40616v1)

**作者**：Michael Joseph, Yedid Hoshen  
**分类**：cs.CV, cs.CR, cs.LG  
**发布时间**：2026-10-29

### 📄 论文摘要

Modern diffusion models are trained on massive datasets that often include copyrighted or private images. Membership inference attacks (MIAs) address this by testing whether a given image was in a model's training set. The standard approach scores an image by its reconstruction loss and flags low-loss images as members. This often fails because some images are simply easier to reconstruct than others, so a simple unseen image can score a lower loss than a complex training image. Difficulty calibration separates memorization from how difficult an image is to begin with. We show how to calibrate along two axes of time: training time and diffusion time. First, across training time, we introduce Reference-Model Calibration (RMC), which compares a fine-tuned model's loss against an earlier checkpoint. This cleanly isolates newly memorized data and gives near-perfect auditing, even without text captions. Since earlier checkpoints are not always available, we next present Temporal Self-Calibration (TSC), which calibrates across diffusion time using only a single model. Our key observation is that an image's difficulty persists across noise levels, whereas memorization is localized in time. By comparing the loss at a target timestep against neighboring timesteps from the same model, TSC attenuates image difficulty using the model's own trajectory. Empirically, our methods beat the state of the art by a wide margin, and unlike most existing attacks, generalize across different model parameterizations such as $x$-, $v$-, and $ε$-prediction models. Code is available at https://github.com/MichaelJoseph777/TSC.

### 🤖 AI 总结

**一句话总结**：Modern diffusion models are trained on massive datasets that often include copyrighted or private images. Membership inference attacks (MIAs) address this by testing whether a given image was in a mod...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Difficulty, Calibration, Across, Time, Membership, Inference, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40616v1) | [下载PDF](https://arxiv.org/pdf/2610.40616v1.pdf)

---

## [17. L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](https://arxiv.org/abs/2610.40614v1)

**作者**：Jinhyeok Choi, JoungBin Lee, Jongmin Lee 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-29

### 📄 论文摘要

Interactive world models generate visual content conditioned on user actions, yet maintaining spatial consistency over long-horizon exploration in real time remains challenging. Existing approaches rely on either temporal context or explicit 3D memory, both of which scale poorly because memory grows with the length of the generated stream. Moreover, explicit 3D memories condition latent video generators by re-encoding RGB renderings, which precludes real-time generation. In this paper, we introduce a Latent 3D Gaussian Memory (L3G) that combines the efficiency of feed-forward reconstruction with a compact, rapidly renderable scene representation. Building on this memory, we propose L3G-World, in which a memory updater and a video diffusion transformer (DiT) alternate autoregressively to generate spatially consistent worlds. The memory updater spawns Gaussians in newly observed regions and refines existing ones, so that the memory grows with scene extent rather than stream length. Each Gaussian further stores a VAE latent feature, allowing the memory to be rendered directly into the DiT's latent space without VAE re-encoding. Experiments show that L3G-World achieves state-of-the-art generation quality and long-horizon spatial consistency, with up to $38.6\times$ fewer 3D primitives, $3.2\times$ faster memory updates, and $359\times$ faster memory rendering relative to the most efficient prior 3D-memory baseline for each metric, enabling real-time world generation at 9 FPS.

### 🤖 AI 总结

**一句话总结**：Interactive world models generate visual content conditioned on user actions, yet maintaining spatial consistency over long-horizon exploration in real time remains challenging. Existing approaches re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, L3G-World, Real-Time, Infinite, World, Generation, Latent, Gaussian

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40614v1) | [下载PDF](https://arxiv.org/pdf/2610.40614v1.pdf)

---

## [18. Beyond Ground Truth: A Heuristic Unsupervised Quality Assurance Engine for Diagnosing Calibrational Blindness in Dental Segmentation](https://arxiv.org/abs/2610.40587v1)

**作者**：Fatematuj Johura Mim  
**分类**：cs.CV  
**发布时间**：2026-10-29

### 📄 论文摘要

In real-world clinical settings, dental X-ray segmentation using deep learning methods suffers from reliability issues. Even when the segmentation quality is bad, deep learning models show high confidence in their predictions (calibrational blindness). Moreover, in real use, doctors do not have ground-truth masks to check their accuracy. To address this problem, we introduce a simple quality-checking engine called HUS-QA with three stages. We train it on the PRAD (Periapical Dental X-ray) dataset to build our SimCLR self-supervised ResNet-18 U-Net model, which generates the segmentation mask and then evaluates its quality. Our HUS-QA checks the segmentation mask quality without a ground-truth mask. Prediction confidence, edge sharpness, shape connectivity, and area-size penalty are the simple indicators considered in this research. Results show that standard confidence methods fail (r = -0.1394, p = 1.7864e-3, ROC AUC = 0.4275). By contrast, our HUS-QA shows a positive correlation with actual Dice scores (r = 0.4647, p = 3.7510e-28) and achieves a strong ROC-AUC of 0.8405. Therefore, HUS-QA serves as a practical tool for clinical quality control.

### 🤖 AI 总结

**一句话总结**：In real-world clinical settings, dental X-ray segmentation using deep learning methods suffers from reliability issues. Even when the segmentation quality is bad, deep learning models show high confid...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Ground, Truth, Heuristic, Unsupervised, Quality, Assurance, Engine

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40587v1) | [下载PDF](https://arxiv.org/pdf/2610.40587v1.pdf)

---

## [19. PhysCount: Do MLLMs Count Visual Appearances or Physical Entities?](https://arxiv.org/abs/2610.40530v1)

**作者**：Lidong Lu, Jiaxin Lv, Liangrui Dong 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-29

### 📄 论文摘要

Images reveal appearances, but counting often asks about physical objects. A single entity may be visible directly, in several reflections, or through glass, so detecting every visible occurrence does not determine how many entities are present. Existing visual counting benchmarks rarely separate these two operations. We introduce PhysCount, a benchmark for evaluating whether multimodal large language models (MLLMs) can distinguish what appears in an image from what physically exists in the scene. PhysCount contains 546 real-world images and 4,595 human-written questions organized into 651 target-specific groups. For each group, annotators locate the relevant appearances, label how each is observed, and identify appearances of the same entity. Four complementary question families test the enumeration of appearances, the enumeration of physical entities, image-formation-specific counting, and appearance--entity correspondence. We measure both accuracy on each family and the proportion of groups answered entirely correctly. Across 40 MLLMs, counting visible appearances is substantially easier than recovering the identities that connect them. Even the strongest model answers every question correctly in only 13.36\% of groups. Performance declines when one entity produces many appearances or when its appearances cross observation modes. Higher image resolution improves access to visual evidence but brings limited gains in complete-group accuracy, whereas answering related questions jointly produces a marked improvement. These results expose a gap between recognizing what is visible and correctly recovering the physical entities behind those observations.

### 🤖 AI 总结

**一句话总结**：Images reveal appearances, but counting often asks about physical objects. A single entity may be visible directly, in several reflections, or through glass, so detecting every visible occurrence does...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, or, PhysCount, MLLMs, Count, Visual, Appearances, Physical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40530v1) | [下载PDF](https://arxiv.org/pdf/2610.40530v1.pdf)

---

## [20. CrossWeave: Cross-Modal Scene and Instance Retrieval from Sparse 2D-3D Alignment](https://arxiv.org/abs/2610.40525v1)

**作者**：Aadith Warrier, Gnana Prakash Punnavajhala, Siddharth Tourani 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-29

### 📄 论文摘要

Cross-modal scene and instance retrieval aims to retrieve a corresponding 3D environment or object given query 2D images, serving as a foundational mechanism for spatial reasoning in robotics and AR/VR. Existing methods achieve this by learning alignment only at the level of whole scenes or objects, which provides no supervision for the fine-grained local structure within them. In this work, we show that supervision on a set of sparse 2D-3D correspondences, without scene- or instance-level contrastive objectives, is sufficient to train a single model for both scene- and instance-level retrieval. Specifically, we propose $\textbf{CrossWeave}$, a novel framework for cross-modal retrieval that learns sparse patch-point alignment, which alone outperforms existing methods. An optimal transport-based aggregator over the aligned features gives further gains by clustering structurally redundant regions, freeing descriptor capacity for semantically distinct local features. CrossWeave achieves state-of-the-art performance on both scene- and instance-level retrieval on ScanNet and 3RScan with a $\textit{single model}$, whereas existing methods require separate models for each task. Our results suggest that whole-scene encoding is unnecessary for cross-modal retrieval and that sparse local correspondence supervision is a more effective and flexible alternative.

### 🤖 AI 总结

**一句话总结**：Cross-modal scene and instance retrieval aims to retrieve a corresponding 3D environment or object given query 2D images, serving as a foundational mechanism for spatial reasoning in robotics and AR/V...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：2D-3D, CrossWeave, Cross-Modal, Scene, Instance, Retrieval, Sparse, Alignment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40525v1) | [下载PDF](https://arxiv.org/pdf/2610.40525v1.pdf)

---

## [21. LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation](https://arxiv.org/abs/2610.40495v1)

**作者**：Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-29

### 📄 论文摘要

We present LucidLyra, a framework that makes generatively reconstructed 3D scenes directly queryable for semantics and instances in a feed-forward manner from video latents. While generative 3D reconstruction can synthesize virtual environments from a single image, downstream applications in robotics and physical AI require not only visual realism but also access to scene semantics and object identities. Existing 3D understanding approaches, however, require captured multi-view scenes, have limited generalization capabilities, or rely on expensive per-scene processing and optimization. To bridge this gap, our method distills complementary knowledge from a camera-controlled video diffusion model and frozen 2D vision foundation models into a unified model to jointly infer 3D Gaussians encoding geometry, appearance, open-vocabulary semantics, and class-agnostic instance cues. The resulting scenes support novel-view rendering, open-vocabulary segmentation, and object grouping without per-scene optimization, while training requires neither manual 3D annotations nor captured multi-view data. Our method outperforms baselines combining state-of-the-art 3DGS segmentation approaches with generative 3D scene reconstruction on curated synthetic and real-image-conditioned benchmarks, while preserving reconstruction quality. Furthermore, our latent formulation naturally extends to monocular video, reconstructing structured dynamic 3D scenes across time. By turning renderable but unstructured outputs into queryable 3D worlds, LucidLyra enables downstream applications including 3D scene editing, 3D asset mining, and robotic simulation.

### 🤖 AI 总结

**一句话总结**：We present LucidLyra, a framework that makes generatively reconstructed 3D scenes directly queryable for semantics and instances in a feed-forward manner from video latents. While generative 3D recons...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, LucidLyra, Feed-Forward, Generative, Scene, Reconstruction, Joint, Understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40495v1) | [下载PDF](https://arxiv.org/pdf/2610.40495v1.pdf)

---

## [22. MetaRefine: Score Refinement with Multi-Level Features for Image Assessment](https://arxiv.org/abs/2610.40487v1)

**作者**：Chuanzhi Xu, Chengkun Yue, Haolan Guo 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-10-29

### 📄 论文摘要

An image's original dimensions, aspect ratio, and composition provide important cues that can affect its technical and aesthetic quality. Image assessment methods use resizing, cropping, padding, or patch sampling to accommodate different input sizes. However, these operations can alter or obscure original geometric and compositional cues. Existing assessment models also encode rich multi-level visual evidence that can be further extracted and exploited to improve existing models. This motivates us to combine visual evidence with original-image geometry for score refinement without changing the original scoring pipelines. In this paper, we introduce MetaRefine, a metadata-aware score refinement architecture whose lightweight residual heads predict score corrections from geometry, multi-level visual features, and the frozen model's original score. Across 100 configurations on 21 datasets, MetaRefine improves PLCC in 88 configurations and SRCC in 85, with average relative gains of 7.55% and 7.10%, respectively. It reduces MAE in 90 configurations and RMSE in 89, with average relative reductions of 23.27% and 21.93%, respectively. The median parameter overhead is only 1.11%. MetaRefine can further improve state-of-the-art (SOTA) assessment models on multiple benchmarks.

### 🤖 AI 总结

**一句话总结**：An image's original dimensions, aspect ratio, and composition provide important cues that can affect its technical and aesthetic quality. Image assessment methods use resizing, cropping, padding, or p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, MetaRefine, Score, Refinement, Multi-Level, Features, Image, Assessment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40487v1) | [下载PDF](https://arxiv.org/pdf/2610.40487v1.pdf)

---

## cs.LG

## [23. Propose-Filter-Release: Scaling Noise to Typical Sensitivity via Private Filtering](https://arxiv.org/abs/2610.40654v1)

**作者**：Moshe Shenfeld, Eliad Tsfadia, Katrina Ligett  
**分类**：cs.LG  
**发布时间**：2026-10-29

### 📄 论文摘要

An estimator can be accurate and stable on typical data, yet sensitive to a few possible records. Differentially private mechanisms commonly scale their noise to the worst-case influence of a single record, which lets these records dictate the noise even when the remaining data would allow far less. Removing them first would restore the smaller scale, but the removal must itself be private.   We introduce \emph{propose-filter-release} (PFR), which, by privately filtering its input, turns a mechanism that protects the addition or removal of a typical record, one that fits the remaining data, into one that is differentially private in the standard sense, on every input. Using our novel filtering step, PFR requires only a concave friendliness score, which measures how well a record fits a dataset, and a release mechanism that is friendly-DP, that is, private when the changed record fits the remaining data. For every such score and release mechanism, it guarantees differential privacy under public conditions on the number of records, so it is a general privacy primitive, comparable to propose-test-release, and FriendlyCore can be viewed as one of its implementations.   We illustrate the generality of PFR by instantiating it for scalar statistics, principal subspace estimation, the KL divergence of user histograms, the effective resistances of a graph, and treatment-rule selection.

### 🤖 AI 总结

**一句话总结**：An estimator can be accurate and stable on typical data, yet sensitive to a few possible records. Differentially private mechanisms commonly scale their noise to the worst-case influence of a single r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Propose-Filter-Release, Scaling, Noise, Typical, Sensitivity, via, Private, Filtering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40654v1) | [下载PDF](https://arxiv.org/pdf/2610.40654v1.pdf)

---

## [24. Rethinking Neural Thickets Without Weight Perturbations](https://arxiv.org/abs/2610.40649v1)

**作者**：Nicolas Dufour, Elouan Gardès, Amil Dravid 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-10-29

### 📄 论文摘要

The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce the reported gains, but show that they do not require this geometric explanation. Perturbing a single decoder block already recovers much of the improvement, while keeping the model entirely frozen and adding a random bias to its output logits matches or exceeds full-weight perturbations on most reasoning tasks. This suggests an alternative explanation based on output diversity, validation-based selection, and voting. We formalize this view as Perturb-Select-Vote (PSV), a general procedure that generates perturbed predictors, selects high-performing members on a small validation set, and aggregates their predictions.   This interpretation connects Neural Thickets to established inference-time methods, including sampling, self-consistency, and verifier-guided selection. A first-order analysis further shows that small weight perturbations act primarily through their induced logit shifts. We extend this analysis to vision, where logit PSV substantially improves performance under domain shift, including on Earth observation, while full-weight perturbations provide little additional benefit. Together, these results suggest that the gains attributed to nearby weight-space experts can instead be obtained through output diversity, selection, and voting. Logit PSV realizes these benefits with a fully frozen model, providing a simple, training-free alternative to full-weight perturbation ensembles across language and vision.

### 🤖 AI 总结

**一句话总结**：The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Rethinking, Neural, Thickets, Without, Weight, Perturbations, hypothesis, posits

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40649v1) | [下载PDF](https://arxiv.org/pdf/2610.40649v1.pdf)

---

## [25. world2vec: Mechanistic world models through latent dynamics learning](https://arxiv.org/abs/2610.40637v1)

**作者**：Tobias Schmidt, Rodrigo Gonzalez Laiz, Krisztián Szuppinger 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-29

### 📄 论文摘要

World models can achieve strong control performance without faithfully capturing the dynamics of their environment, limiting their potential for mechanistic interpretability and scientific discovery. Here, we introduce world2vec to learn mechanistic world models without reward information directly from observations and actions. World2vec learns latent dynamics that faithfully reproduce the true system over long prediction horizons, with at least one order of magnitude fewer parameters than DreamerV3, TD-MPC2 and LeWM. This enables state of the art performance in controlling continuous environments from pixels and accurate system identification across a benchmark of 71 attractors, demonstrating how world models are amenable to scientific discovery.

### 🤖 AI 总结

**一句话总结**：World models can achieve strong control performance without faithfully capturing the dynamics of their environment, limiting their potential for mechanistic interpretability and scientific discovery. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：world2vec, Mechanistic, world, models, through, latent, dynamics, learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40637v1) | [下载PDF](https://arxiv.org/pdf/2610.40637v1.pdf)

---

## [26. Training Foundation Models with a Single Algorithm](https://arxiv.org/abs/2610.40564v1)

**作者**：Yuda Song, Alvin Zhang, Fahim Tajwar 等 10 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-29

### 📄 论文摘要

Foundation models are typically trained in stages: pretraining, midtraining, supervised fine-tuning (SFT), and reinforcement learning (RL), with changes in both data and learning algorithms. We show that this algorithmic separation is not fundamental. By deriving suitable RL objectives as maximum-likelihood fitting to model-generated target distributions, we place all of these stages under a single likelihood-based training algorithm, unified training. This perspective turns the foundation-model training lifecycle into a problem of choosing which data to train on, in what proportions, and when, with conventional staged training as a special case. We instantiate this framework in a unified training system that mixes static data and RL generations within a single trainer. Across controlled and real-world experiments, unified training improves the accuracy-compute tradeoff and task coverage while preserving broader capabilities, and provides a stronger starting point for continual learning. This work lays the groundwork for a unified science of foundation-model training, connecting mathematical principles, training infrastructure, and the development of model capabilities.

### 🤖 AI 总结

**一句话总结**：Foundation models are typically trained in stages: pretraining, midtraining, supervised fine-tuning (SFT), and reinforcement learning (RL), with changes in both data and learning algorithms. We show t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Training, Foundation, Models, Single, Algorithm, typically, trained, stages

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40564v1) | [下载PDF](https://arxiv.org/pdf/2610.40564v1.pdf)

---

## [27. Machine Learning-Based Detection of Mobile Money Scan Messages in Ghana: A Comparative Evaluation of Naive Bayes, Support Vector Machine, and Randon Forest Classifiers](https://arxiv.org/abs/2610.40544v1)

**作者**：Ibrahim Salifu, Muhaisin Tiyumba Nantogmah  
**分类**：cs.LG  
**发布时间**：2026-10-29

### 📄 论文摘要

Mobile money (MoMo) is Ghana's preferred retail payment channel, recording GHC518.4 billion in transactions in December 2025 and over 26.7 million active accounts (Graphic Online, 2026). This growth has coincided with increased social-engineering fraud over Short Message Service (SMS) and Unstructured Supplementary Service Data (USSD), where fraudsters impersonate network operators, agents, relatives, or regulators to obtain personal identification numbers (PINs), identity data, or funds. We present a supervised machine-learning pipeline for classifying scam and legitimate Ghanaian MoMo SMS messages using a labelled corpus of 220 messages across 18 scam and legitimate subcategories. Domain-specific normalisation of currency amounts, phone numbers, and USSD codes preceded TF-IDF vectorisation of unigrams and bigrams. Using stratified five-fold cross-validation and a 20% held-out test set, we trained and evaluated Multinomial Naive Bayes, linear support vector machine (SVM), and Random Forest classifiers using accuracy, precision, recall, F1-score, Matthews correlation coefficient (MCC), and area under the receiver operating characteristic curve (AUC-ROC). Held-out accuracy, F1, and AUC were 1.00 for Naive Bayes and linear SVM; cross-validated accuracy averaged 96.6% (+/-3.3), 94.9% (+/-4.6), and 92.0% (+/-4.2). Discriminative n-grams reflected imperative urgency ("send," "claim," "please send") and PIN solicitation ("PIN," "pincode"); legitimate messages featured confirmatory and cautionary language ("balance," "successful," "do not share"). Findings are contextualised in Sub-Saharan African SMS fraud detection, small template-based corpus ceiling effects, and a pathway toward larger naturalistic multilingual corpora. Interpretable classical classifiers achieve high accuracy on structured MoMo scam text and suit carrier- or handset-level filtering in low-resource, on-device settings.

### 🤖 AI 总结

**一句话总结**：Mobile money (MoMo) is Ghana's preferred retail payment channel, recording GHC518.4 billion in transactions in December 2025 and over 26.7 million active accounts (Graphic Online, 2026). This growth h...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Machine, Learning-Based, Detection, Mobile, Money, Scan, Messages

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40544v1) | [下载PDF](https://arxiv.org/pdf/2610.40544v1.pdf)

---

## [28. Numerical Integration on Bounded Domains via Learned Reflected Diffusions](https://arxiv.org/abs/2610.40499v1)

**作者**：Kirill Korolev, Artur Goldman, Timofei Gritsaev 等 5 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-10-29

### 📄 论文摘要

We study high-dimensional integration on bounded convex domains. Given a non-negative integrand $r$, the goal is to estimate $Z=\int_{D}r(x)\,\mathrm dx$ on $D\subset\mathbb R^d$. Standard Quasi-Monte Carlo does not adapt its evaluation points to the integrand, while effective importance sampling requires a proposal that captures its concentration. Learned diffusion samplers can supply such a proposal, but existing methods are formulated on $\mathbb R^d$ and do not respect the domain constraint $x\in D$. We instead build the proposal from reflected dynamics that stay in $D$ by construction. A reflected diffusion progressively transforms the target distribution toward the uniform distribution on $D$, and a neural score model is trained to reverse this process. A change-of-measure formula for reflected diffusions yields a training objective without additional boundary terms and an unbiased importance-sampling estimator of $Z$. For non-smooth integrands, where reparameterization gradients may be undefined or uninformative, we derive a REINFORCE estimator of the training gradient using Gaussian proposal densities before reflection, without evaluating reflected transition densities or differentiating $r$. We evaluate on numerous synthetic targets and real-world problems, demonstrating strong performance of the proposed method, as well as favorable scaling with the dimension of the problem and the number of points used for the Monte Carlo estimate.

### 🤖 AI 总结

**一句话总结**：We study high-dimensional integration on bounded convex domains. Given a non-negative integrand $r$, the goal is to estimate $Z=\int_{D}r(x)\,\mathrm dx$ on $D\subset\mathbb R^d$. Standard Quasi-Monte...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Numerical, Integration, Bounded, Domains, via, Learned, Reflected, Diffusions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40499v1) | [下载PDF](https://arxiv.org/pdf/2610.40499v1.pdf)

---

## [29. The Precision Wall: An Optimizer-Dependent Boundary for Optimization under Power-Law Measurement Spectra](https://arxiv.org/abs/2610.40485v1)

**作者**：Lngel Kyo  
**分类**：cs.LG  
**发布时间**：2026-10-29

### 📄 论文摘要

In low-rank matrix sensing of a rank-$D$ factor $U^\ast \in \mathbb{R}^{V \times D}$, replacing isotropic Gaussian designs with power-law measurement covariance $Σ= \mathrm{diag}(j^{-s})_{j=1}^V$ leaves the Burer--Monteiro landscape free of spurious local minima, yet division-normalised first-order optimizers stall above a critical exponent $s^\ast$. We trace this failure to a numerical precision wall. At the ground truth, the smallest non-gauge expected Hessian eigenvalue scales at leading order as $V^{-(s+1)}D^{-s}$. When this curvature drops below the effective denominator floor $ε_O$ of optimizer $O$, normalisation noise overwhelms rare-direction gradients, yielding the leading-order boundary $s^\ast_O(V, D) = [\log(1/ε_O) - \log V]/\log(VD) + δ_O$, where $δ_O$ is a metric-dependent detection lag. With $δ_{\mathrm{Adam}}$ calibrated on four configurations and frozen, this formula predicts Adam's onset within $0.45$ across all 16 cells of a held-out grid ($V \in \{64,128,256,512\} \times D \in \{4,8,16,32\}$), separates fixed-$VD$ pairs, and distinguishes denominator-precision walls from conditioning and sign-quantisation walls. The approximation fails at $D = 2$, reflects a finite-$D$ spectral crossover, and saturates below $\varepsilon_0 = 10^{-8}$ at a dynamical floor.

### 🤖 AI 总结

**一句话总结**：In low-rank matrix sensing of a rank-$D$ factor $U^\ast \in \mathbb{R}^{V \times D}$, replacing isotropic Gaussian designs with power-law measurement covariance $Σ= \mathrm{diag}(j^{-s})_{j=1}^V$ leav...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Precision, Wall, Optimizer-Dependent, Boundary, Optimization, under, Power-Law

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40485v1) | [下载PDF](https://arxiv.org/pdf/2610.40485v1.pdf)

---

## [30. Preserving Utility in Continual LLM Unlearning via Orthogonal Projections](https://arxiv.org/abs/2610.40483v1)

**作者**：Juan Belieni, Ana Carolina Erthal, Eliezer de Souza da Silva 等 4 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-10-29

### 📄 论文摘要

Unlearning concerns the task of removing the influence of a sensitive portion of the training data, such as protected, copyrighted or private text, from a model without retraining it from scratch. While unlearning requests happen continuously during a model's lifetime, the vast majority of LLM unlearning methods are ill-suited for iterated removal, yielding steep decay in forgetting and utility upon sequential unlearning. This decay stems from interference between successive updates, as each new deletion can undo earlier ones or push the model further along directions already degraded by them. To address this, we introduce Continual Orthogonal Projection (COP), a gradient-projection scheme that restricts each update to the orthogonal complement of activation subspaces cached from prior forget sets. This approach provably guarantees first-order non-interference with earlier deletions. COP stores only a low-rank basis per layer, requiring neither past gradients nor previous forget sets, and plugs into unlearning methods that update the model through gradient steps on a differentiable loss without modifying its objective. Experiments on standard LLM unlearning benchmarks (TOFU and RWKU) show that COP preserves utility across sequential requests without weakening forgetting, preventing the collapse of standard objectives and forgetting more effectively than continual-specific baselines.

### 🤖 AI 总结

**一句话总结**：Unlearning concerns the task of removing the influence of a sensitive portion of the training data, such as protected, copyrighted or private text, from a model without retraining it from scratch. Whi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Preserving, Utility, Continual, Unlearning, via, Orthogonal, Projections

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.40483v1) | [下载PDF](https://arxiv.org/pdf/2610.40483v1.pdf)

---

