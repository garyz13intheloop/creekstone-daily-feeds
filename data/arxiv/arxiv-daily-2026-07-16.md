# arXiv AI 论文日报 | 2026-07-16

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (8 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.CV](#csCV) (11 篇)

---

## cs.AI

## [1. Earthquaker-AI: A Retrieval-Augmented Generation Framework with Rubric-Based Assessment for Primary School Earthquake Education](https://arxiv.org/abs/2607.14046v1)

**作者**：Xanthi Kokkinou, Chaido Mizeli, Nafsika Koulaxidou 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-15

### 📄 论文摘要

This paper presents Earthquaker-AI, a hybrid educational framework building upon a previously implemented educational robotics project by integrating a conversational AI assistant based on Retrieval-Augmented Generation. It aims to enhance earthquake preparedness and conscious action among primary-school students. The system extends the award-winning STEM project Earthquaker moving from mechanical simulation with Lego WeDo2 to cognitive and metacognitive processing. The robotics component uses Lego WeDo2 automation to simulate seismic response, letting students interact with sensors and actuators as tangible representations of protective actions. The assistant operates as a guided learning mechanism aligning student responses with safety guidelines, while providing rubric-based verbal feedback that supports self-regulated learning and calmness under emergency conditions. Earthquaker-AI follows a progressive learning trajectory aligned with cognitive development. In early grades, the focus is on basic recognition of safety actions through multiple-choice questions, assessed via a two-dimensional rubric. In middle grades, students identify correct action sequences through multiple-choice questions, evaluated via a three-axis rubric. In upper grades, the approach shifts to verbal production, requiring short written responses assessed via a four-dimensional rubric that includes clarity of expression. The dialogic module uses RAG to match student queries semantically with official guidelines, generating safe, accurate responses. Experimental evaluation shows high groundedness and accuracy, with a low hallucination rate. Overall, Earthquaker-AI combines hands-on engagement, information processing, and reflective practice. Combining robotics, rubrics, and AI promotes technological literacy, self-regulation, and responsible use of digital systems, contributing to early crisis-management skills.

### 🤖 AI 总结

**一句话总结**：This paper presents Earthquaker-AI, a hybrid educational framework building upon a previously implemented educational robotics project by integrating a conversational AI assistant based on Retrieval-A...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Earthquaker-AI, Retrieval-Augmented, Generation, Framework, Rubric-Based, Assessment, Primary, School

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.14046v1) | [下载PDF](https://arxiv.org/pdf/2607.14046v1.pdf)

---

## [2. AI-accelerated End-to-End Framework for Rapid Professional Upskilling](https://arxiv.org/abs/2607.14044v1)

**作者**：Tam Nguyen, Hung Nguyen, Robert Ogburn  
**分类**：cs.AI  
**发布时间**：2026-07-15

### 📄 论文摘要

By 2030, 59 of every 100 workers will need reskilling or upskilling, yet the average time to close an enterprise skills gap grew from roughly 3 days in 2014 to 36 days in 2018. Most current frameworks accelerate single stages of upskilling programs and generally lack industry validation. We present an end-to-end framework that applies AI acceleration across five stages of knowledge acquisition, content development, content review and verification, teaching, and assessment development; with a strong focus on both production and learning efficiency. Three strong external signals validates the framework: the US National Association of State Boards of Accountancy reviewed and approved an upskilling program built on the framework for continuing-professional-education credits; 3 learners followed the program and passed the NVIDIA Certified Professional in Agentic AI exam in a significantly short amount of time, with 14 more in progress; the program's knowledge base supports complex downstream analysis such as the production of a robust 1,267 risk item dataset for managing multi-agent AI system risks.

### 🤖 AI 总结

**一句话总结**：By 2030, 59 of every 100 workers will need reskilling or upskilling, yet the average time to close an enterprise skills gap grew from roughly 3 days in 2014 to 36 days in 2018. Most current frameworks...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, AI-accelerated, End-to-End, Framework, Rapid, Professional, Upskilling, every

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.14044v1) | [下载PDF](https://arxiv.org/pdf/2607.14044v1.pdf)

---

## [3. Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0](https://arxiv.org/abs/2607.14004v1)

**作者**：Wenxiao Wang, Priyatham Kattakinda, Soheil Feizi  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-07-15

### 📄 论文摘要

Most reported gains from agent-optimization methods are one-shot: an agent is optimized against a fixed benchmark and the resulting improvement is reported as if it were a stable property of the method. This does not test the setting that matters for deployed agents, where optimization is applied recursively as new failures and new tasks appear over time. The central question this raises is whether optimizer-driven gains compound: after an agent has been optimized once, can it be optimized again on newly arrived tasks without eroding the gains the first round produced? We study this question with a two-phase continual-learning evaluation built from hard tasks in Terminal-Bench 2.0, comparing three approaches to agent-harness optimization (GEPA, Meta Harness, and RELAI's Verifiable Continual Learning, RELAI-VCL) under identical optimization budgets. All three methods improve over the baseline agent in the conventional, static, single-phase setting. However, once new tasks are introduced, the methods diverge sharply: GEPA's optimized agent transfers below the unoptimized baseline, Meta Harness transfers well but fails to improve further once given a second optimization budget, and RELAI-VCL is the only method that both transfers positively to unseen tasks and continues improving after those tasks are folded into the optimization objective, reaching the highest pass rate at every evaluated stage and the highest lifelong average pass rate overall (76.4% vs. 66.0% for GEPA, 64.6% for Meta Harness, and 58.7% for the baseline). Our key observation was that optimization gains compounded only when regression control was built into the optimization loop, providing an inductive bias against shortcut solutions that fail to generalize.

### 🤖 AI 总结

**一句话总结**：Most reported gains from agent-optimization methods are one-shot: an agent is optimized against a fixed benchmark and the resulting improvement is reported as if it were a stable property of the metho...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, Agent, Optimizers, Compound?, Continual-Learning, Evaluation, Terminal-Bench, Most

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.14004v1) | [下载PDF](https://arxiv.org/pdf/2607.14004v1.pdf)

---

## [4. A Self-Evolving Agent for Longitudinal Personal Health Management](https://arxiv.org/abs/2607.13940v1)

**作者**：Haoran Li, Jiebi Deng, Tong Jin 等 13 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-15

### 📄 论文摘要

Personal health management unfolds over repeated encounters, yet most health AI systems treat each request in isolation. We developed HealthClaw, an open-source agent architecture that updates support as a person's routines, preferences, measurements and risks change. It separates shared safety rules and medical knowledge from private longitudinal memory containing profile facts, reusable procedures and episodic traces. After each episode, induction determines what should update the profile, revise a procedure, remain episodic or be excluded. We evaluated HealthClaw with a synthetic year-long benchmark and nine 200-case biomedical tasks. Across 900 longitudinal support probes, answer accuracy increased from 0.2% with current-query prompting to 45.7% with HealthClaw, while prompt-side context exposure was 71.7% lower than with full-history prompting. In 100 privacy probes, HealthClaw produced higher privacy-aware answer quality and fewer unsafe disclosures than both baselines. Across the biomedical tasks, the mean absolute gain in the task-specific primary metric was 27.0 percentage points, and seven gains remained significant after false-discovery-rate correction. These offline benchmarks support governed, self-evolving memory for longitudinal personal health agents, although clinical effectiveness requires prospective evaluation. HealthClaw is publicly available at https://github.com/HC-Guo/HealthClaw.

### 🤖 AI 总结

**一句话总结**：Personal health management unfolds over repeated encounters, yet most health AI systems treat each request in isolation. We developed HealthClaw, an open-source agent architecture that updates support...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Self-Evolving, Longitudinal, Personal, Health, Management, unfolds, over

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13940v1) | [下载PDF](https://arxiv.org/pdf/2607.13940v1.pdf)

---

## [5. AIMO Interpretability Challenge](https://arxiv.org/abs/2607.13899v1)

**作者**：Michal Štefánik, Philipp Mondorf, Andreas Waldis 等 14 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-15

### 📄 论文摘要

We propose the AIMO Interpretability Challenge, a competition on distinguishing robust from spurious reasoning in frontier mathematical language models based on the models' internal mechanisms. The challenge is motivated by a central limitation of standard reasoning benchmarks: strong final-answer accuracy does not reveal whether a model relies on stable reasoning mechanisms or exploits brittle reasoning shortcuts. Building on AI Mathematical Olympiad (AIMO) problems and submissions, together with resources from the Fields Model Initiative, the competition will provide (1) newly-published olympiad-level math reasoning problems and their symbolic representations, allowing generation of novel functional variants, (2) access to frontier reasoning models, and (3) assessments of models' adversarial robustness on these problems. Participants will use these resources, along with our computing infrastructure support, to develop methods for identifying which models solve problems robustly. Our competition will also create a new, open robustness benchmark and baseline systems, aiming to provide a lasting foundation for standard benchmarking in mathematical reasoning and interpretability. Scientifically, the competition connects interpretability and generalization research around a central question in AI research: can we determine if, and to what extent, the decision-making of frontier AI models is generalizable and thus, reliable?

### 🤖 AI 总结

**一句话总结**：We propose the AIMO Interpretability Challenge, a competition on distinguishing robust from spurious reasoning in frontier mathematical language models based on the models' internal mechanisms. The ch...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, AIMO, Interpretability, Challenge, propose, competition, distinguishing, robust

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13899v1) | [下载PDF](https://arxiv.org/pdf/2607.13899v1.pdf)

---

## [6. Experience Memory Graph: One-Shot Error Correction for Agents](https://arxiv.org/abs/2607.13884v1)

**作者**：Wenjun Wang, Yuchen Fang, Fengrui Liu 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-15

### 📄 论文摘要

Large Language Model (LLM) agents have shown remarkable capabilities in autonomous decision-making by generating sequential trajectories of states, actions, and observations. However, in complex, long-horizon tasks, these agents frequently suffer from compounding errors and struggle to recover from failures. Existing self-correction mechanisms rely on prompt-based reflection, which is inherently brittle, incurs heavy time and API costs due to iterative trial-and-error loops, and produces task-specific memory that may be hard to generalize to new scenarios. To address this, we propose Experience Memory Graph (EMG), a framework that reformulates agent failure recovery as a graph matching problem. At training time, we convert both failed exploration trajectories and successful expert trajectories into directed action decision graphs. By matching these graphs, we extract common subgraphs (successful workflows) and graph edit paths that explicitly indicate how to correct failures (e.g., which actions to add, delete, or relabel under a given observation), and store them in a memory graph with intra-task nodes and cross-task edges. At test time, EMG retrieves relevant insights and guides the agent in a single, loop-free execution. Experiments on ALFWorld and ScienceWorld show that EMG consistently outperforms state-of-the-art reflection baselines in success rate and average reward, while requiring no test-time trial-and-error.

### 🤖 AI 总结

**一句话总结**：Large Language Model (LLM) agents have shown remarkable capabilities in autonomous decision-making by generating sequential trajectories of states, actions, and observations. However, in complex, long...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Experience, Memory, Graph, One-Shot, Error, Correction, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13884v1) | [下载PDF](https://arxiv.org/pdf/2607.13884v1.pdf)

---

## cs.CL

## [7. Hindcast: Replaying Prediction Markets to Evaluate LLM Forecasters](https://arxiv.org/abs/2607.14051v1)

**作者**：Xiao Ye, Jacob Dineen, Evan Zhu 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-15

### 📄 论文摘要

Forecasters are evaluated by backtesting, which replays resolved questions and grades the probability the system would have assigned before the outcome was known. For LLMs, two channels leak the answer into this test. A model that retrieves can surface reports written after the event, turning forecasting into a lookup, and each new model is trained on data closer to the event, so a question that lay in the future for last year's models sits inside this year's training data. Either way, the test grades recall while claiming to grade foresight. We introduce Hindcast, which closes both leaks by grading a model as if it stood at a chosen past date $t_0$, before the outcome existed in either channel. Hindcast replays resolved Polymarket prediction markets against a frozen snapshot of public Reddit, lets the model read only posts written before $t_0$, and scores each forecast against both what happened and the market's own price at $t_0$, itself a human forecast made from the same past information. Because the cutoff is set per market and the snapshot never changes, the evaluation re-runs on new markets as models improve, without going stale. Once the leak is closed, retrieval still helps most models, but only where Reddit discussed the event beforehand. Where the archive carried only speculation, retrieval hurts.

### 🤖 AI 总结

**一句话总结**：Forecasters are evaluated by backtesting, which replays resolved questions and grades the probability the system would have assigned before the outcome was known. For LLMs, two channels leak the answe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Hindcast, Replaying, Prediction, Markets, Evaluate, Forecasters, evaluated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.14051v1) | [下载PDF](https://arxiv.org/pdf/2607.14051v1.pdf)

---

## [8. Can an Old Dog Be Taught New Tricks? Taking LLMs Beyond Sentence Level Translation](https://arxiv.org/abs/2607.14040v1)

**作者**：Alaina Brandt  
**分类**：cs.CL  
**发布时间**：2026-07-15

### 📄 论文摘要

Automatic translation systems, from CAT tools to MT, overwhelmingly treat translation as a sentence-by-sentence act. This paper asks whether LLMs can be moved beyond that paradigm through whole-document, corpus-informed translation. We present PAT (Pragmatic Auto-Translator), a RAG-based system that pairs user-configured specifications with context from a comparable corpus of authentic longform texts in U.S. English and Latin American Spanish, passing retrieved paragraph-, section-, and document-level examples to an LLM for whole-document generation. The goal is draft translation for professional verification: target texts reformulated to fit their Spanish-language context, where discourse organization, rhetorical style, and pragmatic norms differ meaningfully from English. We evaluated six automatic translations of essays on generative AI across three projects using a customized MQM typology, assessed by two trained evaluators working from U.S. English into LATAM and Mexican Spanish. Results show that a limited prompt produced no meaningful reformulation, and specifications and corpus-informed translations at times showed substantial reformulation, though not always to effect. We find that LLMs can be moved toward reformulation and away from the sentence-by-sentence paradigm, though more work is needed to improve the effectiveness of those reformulations. In this paper, we discuss considerations related to automatic translation system design, corpus construction, and translation quality evaluation methodology and results.

### 🤖 AI 总结

**一句话总结**：Automatic translation systems, from CAT tools to MT, overwhelmingly treat translation as a sentence-by-sentence act. This paper asks whether LLMs can be moved beyond that paradigm through whole-docume...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Be, Can, Old, Dog, Taught, New, Tricks?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.14040v1) | [下载PDF](https://arxiv.org/pdf/2607.14040v1.pdf)

---

## [9. DeltaMerge-LowRes: Composing Language and Task Deltas for Low-Resource Adaptation](https://arxiv.org/abs/2607.13967v1)

**作者**：Son Ha Xuan, Xuan-Bach Le, Phat T. Tran-Truong  
**分类**：cs.CL  
**发布时间**：2026-07-15

### 📄 论文摘要

Adapting a multilingual encoder to a new language \emph{and} a new task with only a few hundred gold examples is a common low-resource NLP setting, yet the two axes are usually fused via an expensive language--task fine-tuning run. We ask whether they can instead be trained separately and recombined in weight space. \DeltaMergeLowRes{} learns a language delta $Δ_L$ from unlabeled monolingual text and a task delta $Δ_T$ from labeled English data, then composes them at inference under one of four rules: additive, activation-guided, sparsity-aware, and a novel \emph{cross-axis TIES}. The new rule adapts the TIES-Merging steps of trimming, sign election, and merging to the language and task axes rather than to two task axes. Holding $(Δ_L,Δ_T)$ fixed across rules on four task families and four African languages ($158$ evaluated cells, $10{,}000$-sample paired bootstrap per cell), we find: (i) cross-axis TIES wins summarisation on $3/4$ languages by $+4$ to $+7$ chrF (chrF $18.59$ vs.\ $13.80$ task-only); (ii) it improves QA F1 by $+2.32$ and EM by $+2.91$; and (iii) sparsity-aware merging cuts classification ECE by $36\%$ at parity macro-F1. The composition rule materially changes what the merged model preserves, suppresses, and calibrates. We release all JSON traces and a claim ledger.

### 🤖 AI 总结

**一句话总结**：Adapting a multilingual encoder to a new language \emph{and} a new task with only a few hundred gold examples is a common low-resource NLP setting, yet the two axes are usually fused via an expensive ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DeltaMerge-LowRes, Composing, Language, Task, Deltas, Low-Resource, Adaptation, Adapting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13967v1) | [下载PDF](https://arxiv.org/pdf/2607.13967v1.pdf)

---

## [10. DeepStress: Stress-Testing Deep Search Agents](https://arxiv.org/abs/2607.13920v1)

**作者**：Ismael Rousseau, Geraldine Damnati, Frederic Bechet  
**分类**：cs.CL  
**发布时间**：2026-07-15

### 📄 论文摘要

While search agents demonstrate impressive capabilities in multi-step question answering, their robustness to poor-quality evidence remains under-explored. This phenomenon occurs rarely in realistic benchmarks but can lead to dramatic failure in real life applications. Therefore in this study we propose DeepStress, a stress testing framework that controls the frequency of challenging evidence by replacing the retrieval module of search agents with a controlled synthetic environment. We use this framework to control three dimensions that can affect document reliability: trustworthiness, relevance, and factuality. Testing several search agents on HotpotQA and BrowseCompPlus, we demonstrate that agents exhibit substantial differences in their ability to handle unreliable information and propose new metrics that better document systems outcomes as well as the interactions between conflicting parametric and retrieved knowledge.

### 🤖 AI 总结

**一句话总结**：While search agents demonstrate impressive capabilities in multi-step question answering, their robustness to poor-quality evidence remains under-explored. This phenomenon occurs rarely in realistic b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, DeepStress, Stress-Testing, Deep, Search, While, demonstrate, impressive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13920v1) | [下载PDF](https://arxiv.org/pdf/2607.13920v1.pdf)

---

## [11. High-Order Question Generation in a Multilingual Educational Context](https://arxiv.org/abs/2607.13901v1)

**作者**：Suna-Şeyma Uçar, Itziar Aldabe, Nora Aranberri 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-15

### 📄 论文摘要

Critical thinking is a fundamental skill that helps learners move beyond simple memorization. One way to develop this skill is through high-order questioning. However, crafting such questions remains a challenge for educators, and classroom practices tend to rely on low-order questions. Large Language Models have demonstrated strong capabilities in generating high-order questions, especially when guided by prompts based on Bloom's Taxonomy. Yet, existing research has largely centered on this framework and focused only on English. This study addresses these gaps by introducing prompts grounded in two alternative frameworks: Claim-Evidence-Reasoning and Divergent Questioning within a multilingual context using Basque, Spanish, and English. Results indicate that while both an open-source and a proprietary model rather effectively generate questions in all three languages, only about half of the answerable questions are recognized by teachers as high-order. A positive finding is that the alternative frameworks produce structurally and conceptually varied questions, suggesting they could complement each other and provide viable alternatives to Bloom's Taxonomy.

### 🤖 AI 总结

**一句话总结**：Critical thinking is a fundamental skill that helps learners move beyond simple memorization. One way to develop this skill is through high-order questioning. However, crafting such questions remains ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：High-Order, Question, Generation, Multilingual, Educational, Context, Critical, thinking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13901v1) | [下载PDF](https://arxiv.org/pdf/2607.13901v1.pdf)

---

## cs.CV

## [12. Multi-Expert Routing for Multi-Domain Low-Resource OCR: A Manchu Case Study](https://arxiv.org/abs/2607.14041v1)

**作者**：Zhan Chen, Jiqiao Ma, Chih-wen Kuo  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-07-15

### 📄 论文摘要

Historical Manchu OCR must accommodate various visually distinct writing styles, including regular script, running script, and the semi-cursive chancery hand used in palace memorials, despite limited labeled data. We study a multi-expert system that reuses checkpoints from an iterative fine-tuning process as domain specialists and uses a lightweight page-level image classifier to dispatch pages by visual style. When the checkpoint pool lacks a suitable specialist, we train an additional expert for that domain. On three frozen test sets, the routed system matches the selected specialist for each style at two-decimal precision: 0.30 percent CER on regular script, 1.57 percent on memorials, and 4.83 percent on running script. The router achieves 99.3 percent page-level domain accuracy and matches the domain-label oracle at the same precision. Two of the three selected specialists were not trained specifically for their final domain; only the running-script expert was trained with that domain as its target. We report the evaluation protocol, router design, and per-page predictions to make the comparison reproducible.

### 🤖 AI 总结

**一句话总结**：Historical Manchu OCR must accommodate various visually distinct writing styles, including regular script, running script, and the semi-cursive chancery hand used in palace memorials, despite limited ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OCR, Multi-Expert, Routing, Multi-Domain, Low-Resource, Manchu, Case, Study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.14041v1) | [下载PDF](https://arxiv.org/pdf/2607.14041v1.pdf)

---

## [13. M$^\text{4}$World: A Multi-view Multimodal Driving World Model for Interactive Object Manipulation and Minute-long Streaming](https://arxiv.org/abs/2607.14005v1)

**作者**：Ke Cheng, Hanqiao Ye, Lei Shi 等 11 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-07-15

### 📄 论文摘要

Driving-world generation has emerged as a core capability for scalable autonomous-driving simulation, yet existing methods remain limited in object-level controllability and long-horizon stability. We present M$^\text{4}$World, a Multi-view and Multimodal generative driving world model that synthesizes future surround-view video streams and synchronized LiDAR scans while supporting interactive object Manipulation and stable Minute-long streaming. Fine-grained object manipulation is realized through a flexible conditioning interface that supports explicit control over both the spatial layout and visual appearance of individual objects. Stable minute-long streaming, on the other hand, is achieved through a multi-stage training framework that enables online causal generation in only four denoising steps while maintaining coherent world dynamics throughout extended rollouts. Building on these components, we introduce an efficient few-clip post-training as well as a suite of visual reference-conditioned generation models, preserving general generation ability while allowing rare-case customization for long-tail controllability. To assess controllability beyond realism, we further introduce an automated VLM-based judging pipeline that evaluates scene-level condition adherence, view-wise object controllability, and cross-view object consistency. Comprehensive experiments show that M$^\text{4}$World consistently delivers high generation quality, precise controllability, and stable minute-long streaming. Together with downstream long-tail augmentation and scene editing, these results demonstrate the potential of M$^\text{4}$World for controllable, scalable driving simulation.

### 🤖 AI 总结

**一句话总结**：Driving-world generation has emerged as a core capability for scalable autonomous-driving simulation, yet existing methods remain limited in object-level controllability and long-horizon stability. We...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：M$^, text, $World, Multi-view, Multimodal, Driving, World, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.14005v1) | [下载PDF](https://arxiv.org/pdf/2607.14005v1.pdf)

---

## [14. Task-Specific Feature Fusion Method for Multi-Task Affective Behavior Analysis](https://arxiv.org/abs/2607.13986v1)

**作者**：Jiajun Sun, Zhe Gao  
**分类**：cs.CV  
**发布时间**：2026-07-15

### 📄 论文摘要

The 11th Affective Behavior Analysis in-the-wild (ABAW11) Multi-Task Learning Challenge requires a unified system to predict valence-arousal, categorical expressions, and facial action units from the official s-Aff-Wild2 images. Although these tasks are naturally related through facial behavior, our validation experiments show that they benefit from different visual features, temporal processing strategies, fusion mechanisms, and calibration procedures. In this paper, we study task-adaptive feature fusion for ABAW11 multi-task affective behavior analysis. We first adapt two pretrained visual backbones, DINOv2 ViT-L and DINOv3 ConvNeXt-base, on an external expression-oriented facial image set and then freeze them to extract complementary frame-level features from the official ABAW11 data. On top of these frozen features, we systematically compare frame-level prediction heads, temporal convolutional heads, post-hoc temporal smoothing, LightGBM models, feature concatenation, gated fusion, residual fusion, late logit fusion, threshold calibration, and shared MTL structures. The final system selects task-specific fusion and prediction strategies rather than forcing all tasks to share a single architecture. On the ABAW11 validation set, the selected system achieves an EXPR macro-F1 of 0.4222, an AU macro-F1 of 0.5402, and a mean VA CCC of 0.6717, resulting in an overall validation score of 1.6341. The results suggest that task-adaptive fusion of frozen visual features is a simple and effective strategy for ABAW-style multi-task affective behavior analysis.

### 🤖 AI 总结

**一句话总结**：The 11th Affective Behavior Analysis in-the-wild (ABAW11) Multi-Task Learning Challenge requires a unified system to predict valence-arousal, categorical expressions, and facial action units from the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Task-Specific, Feature, Fusion, Method, Multi-Task, Affective, Behavior, Analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13986v1) | [下载PDF](https://arxiv.org/pdf/2607.13986v1.pdf)

---

## [15. Music-to-Dance Generation via Atomic Movements](https://arxiv.org/abs/2607.13978v1)

**作者**：Xinhao Cai, Yixuan Sun, Minghang Zheng 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-15

### 📄 论文摘要

Music-driven dance generation aims to produce human motion that is both rhythmically synchronized and semantically consistent with music. While recent neural approaches have achieved impressive visual realism, they typically model motion as a continuous signal and neglect its compositional nature, making generated dances structurally incoherent and difficult to control. In this work, we introduce a structure-aware framework that models choreography as a sequence of atomic movements-semantically interpretable motion events that serve as the building blocks of dance. To construct this atomic movement vocabulary, we first segment large-scale dance data and cluster them into atomic movement groups. We then employ a large language model to semantically relabel and refine the clusters, yielding a set of interpretable and reusable atomic movements. Based on these atomic movement annotations, we design a two-stage generation framework that mirrors the human choreography process. In the atomic movement planning stage, the model predicts the type, duration, and timing of atomic movements conditioned on the input music, forming a symbolic dance allocation. In the completion stage, a transition-aware generator synthesizes smooth and stylistically coherent motion conditioned on the planned structure. Extensive experiments demonstrate that our method produces dances with significantly improved structural coherence, rhythmic alignment, and perceptual naturalness compared to existing baselines, while providing enhanced interpretability and controllable editing through explicit structural representation.

### 🤖 AI 总结

**一句话总结**：Music-driven dance generation aims to produce human motion that is both rhythmically synchronized and semantically consistent with music. While recent neural approaches have achieved impressive visual...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Music-to-Dance, Generation, via, Atomic, Movements, Music-driven, dance, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13978v1) | [下载PDF](https://arxiv.org/pdf/2607.13978v1.pdf)

---

## [16. CF-Net: Conflict Fusion with Speaker Normalisation and Certainty Weighting for Ambivalence/Hesitancy Recognition](https://arxiv.org/abs/2607.13976v1)

**作者**：Tung Hung Bui, Hong Hai Nguyen, Van Thong Huynh  
**分类**：cs.CV  
**发布时间**：2026-07-15

### 📄 论文摘要

Detecting ambivalence and hesitancy (AH) in unconstrained video is challenging because the target signal is inherently ambiguous and expressed through subtle cross-modal incongruence rather than prototypical affect. We present CF-Net, a deep multimodal network submitted to the 3rd Edition of the AH Video Recognition Challenge (ABAW 11th, ECCV 2026), targeting the BAH dataset. CF-Net encodes visual, audio, and transcript streams with frozen SigLIP2, HuBERT, and DistilBERT backbones, normalises backbone features per speaker to reduce identity leakage, and fuses them via a ConflictFusion module that explicitly computes pairwise cross-modal incongruence. Training combines certainty-weighted focal loss, manifold mixup, and modality dropout; an auxiliary certainty-regression head leverages ambiguity annotations to stabilise learning on genuinely borderline samples. CF-Net achieves a Macro F1 of 0.7155 on the BAH validation set and 0.7364 (AP = 0.7492) on the private challenge test set.

### 🤖 AI 总结

**一句话总结**：Detecting ambivalence and hesitancy (AH) in unconstrained video is challenging because the target signal is inherently ambiguous and expressed through subtle cross-modal incongruence rather than proto...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CF-Net, Conflict, Fusion, Speaker, Normalisation, Certainty, Weighting, Ambivalence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13976v1) | [下载PDF](https://arxiv.org/pdf/2607.13976v1.pdf)

---

## [17. PlumeQuant: Uncertainty-aware consistency assessment of methane plume masks and emission-rate estimates](https://arxiv.org/abs/2607.13945v1)

**作者**：Parisa Masnadi Khiabani, Wolfgang Jentner, Alireza Rangrazjeddi 等 7 位作者  
**分类**：cs.CV, astro-ph.IM  
**发布时间**：2026-07-15

### 📄 论文摘要

Imaging spectrometers increasingly distribute source-resolved methane plume products in which the plume mask, integrated mass enhancement (IME), plume length, emission rate, and uncertainty are physically and algorithmically linked. Using 63 EMIT-derived Carbon Mapper plume records from 27 scenes, we show that these published scalar quantities do not uniquely constrain the plume boundary: substantially different yet plausible masks reproduce the same IME, plume length, and emission rate. Genetic-algorithm (GA) ensembles conditioned on the published IME and plume length make this equifinality explicit: the high-confidence core selected by nearly all target-consistent masks covers a median of 13% of the plausible footprint envelope, and ambiguity is largest for weak, low-overlap plumes. The diagnostics come from PlumeQuant, which recomputes IME, plume length, emission rate, and five-term uncertainty from distributed product components under stated conventions and evaluates four mask representations: the distributed reference mask, a transparent Carbon Mapper-informed analogue (CM-like), the GA ensemble, and optional expert edits. The CM-like mask is generated per plume without access to the reference mask or published quantities, with settings fixed once on a scene-disjoint 44-plume development split. It reproduced published IME with +0.72% median difference and emission rate with +0.16% (6.98% mean absolute), reached 0.843 median intersection-over-union against the reference masks, and matched the published uncertainty scale (median ratio 1.01). Holdout mean absolute errors were 7.6% (IME), 9.5% (length), and 6.1% (rate). These are product-level consistency diagnostics, not independent validation. They flag weak, offset, or ambiguous plumes for expert review.

### 🤖 AI 总结

**一句话总结**：Imaging spectrometers increasingly distribute source-resolved methane plume products in which the plume mask, integrated mass enhancement (IME), plume length, emission rate, and uncertainty are physic...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, PlumeQuant, Uncertainty-aware, consistency, assessment, methane, plume, masks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13945v1) | [下载PDF](https://arxiv.org/pdf/2607.13945v1.pdf)

---

## [18. Peak-End-Net: A Peak-End Rule Inspired Framework for Generalizable Video Aesthetic Assessment](https://arxiv.org/abs/2607.13941v1)

**作者**：Geng Li, Haiwen Li, Rui Chen 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-15

### 📄 论文摘要

Video aesthetic assessment (VAA) aims to predict how aesthetically pleasing a video is, yet remains far less explored than other visual assessment tasks. Its progress is hindered not only by the scarcity of large-scale benchmarks, but also by the intrinsic subjectivity of aesthetic judgment, which is shaped by human perception. In this paper, we revisit VAA from a psychological perspective and propose \textit{Peak-End-Net}, a lightweight and interpretable framework inspired by the \textit{peak-end rule}, which suggests that people tend to judge a temporal experience mainly according to its salient moments and the ending. Building on this intuition, we first transfer knowledge from image aesthetic assessment (IAA) to VAA by introducing a pretrained IAA head to produce frame-wise aesthetic priors, which serve as surrogate signals for identifying aesthetically salient moments and guiding \textit{peak-end rule}-based temporal aggregation. To further capture how a video evolves aesthetically over time, we design an aesthetic rhythm encoder that models temporal progression beyond isolated moments. Additionally, we refine the overall assessment through a dynamic gated fusion mechanism to improve robustness under distribution shift. Our method is built on a frozen vision transformer (ViT) and requires only a small number of trainable parameters, making it scalable and parameter-efficient. Extensive experiments on two existing VAA benchmarks, including in-domain evaluation on VADB and cross-domain testing on DIVIDE-3K, demonstrate that our approach achieves state-of-the-art performance, affirming the value of psychologically grounded modeling for VAA. Our code and models are available at https://github.com/AMAP-ML/Peak-End-Net.

### 🤖 AI 总结

**一句话总结**：Video aesthetic assessment (VAA) aims to predict how aesthetically pleasing a video is, yet remains far less explored than other visual assessment tasks. Its progress is hindered not only by the scarc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Peak-End-Net, Peak-End, Rule, Inspired, Framework, Generalizable, Video, Aesthetic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13941v1) | [下载PDF](https://arxiv.org/pdf/2607.13941v1.pdf)

---

## [19. A novel unsupervised machine learning strategy to handle multimodal cardiac PET/MRI data](https://arxiv.org/abs/2607.13936v1)

**作者**：Brunnhilde Ponsi, Thomas Carlier, Lara Marteau 等 8 位作者  
**分类**：cs.CV, cs.LG, physics.med-ph  
**发布时间**：2026-07-15

### 📄 论文摘要

Arrhythmogenic left ventricular cardiomyopathy is a genetic myocardial disease difficult to diagnose due to the lack of gold standard criteria. Simultaneous PET/MR imaging, combined with multiparametric quantitative analysis, could facilitate the identification of different profiles related to the phenotype and progression of cardiomyopathy. This preliminary study focuses on a methodological strategy for dealing with PET/MRI data, including inter-patient data linkage and regional analysis. Two-step clustering was applied to T1 and T2 maps, LGE, and 18F-FDG-PET images of 99 patients genetically diagnosed with arrhythmogenic left ventricular cardiomyopathy. Each patient's images were independently z-scored and summed into a single volume, which was clustered into supervoxels. Thirty-two inter-patient groups of supervoxels were obtained by spectral clustering. An "abnormality" score was assigned to each cluster and modality, and used to visualise abnormal regions likely associated with disease. They enabled the generation of automated textual and bullseye health reports for each patient, which were compared with cardiac imager assessments using balanced accuracy in repeated nested cross-validation. This approach was further validated on a larger cohort of 167 numerical phantoms. The reports generated by clustering accurately identified most of the cardiac physicians' observations (BA = 0.76 $\pm$ 0.04 in repeated nested cross-validation on patients, and BA $\ge$ 0.8 on phantoms). Furthermore, the identified abnormal clusters closely matched their visual observations, facilitating the identification of varying degrees of fibrosis or inflammation on the images. This approach enables a more systematic handling of multimodal PET/MRI data to characterise myocardial heterogeneity in arrhythmogenic left ventricular cardiomyopathy patients.

### 🤖 AI 总结

**一句话总结**：Arrhythmogenic left ventricular cardiomyopathy is a genetic myocardial disease difficult to diagnose due to the lack of gold standard criteria. Simultaneous PET/MR imaging, combined with multiparametr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：novel, unsupervised, machine, learning, strategy, handle, multimodal, cardiac

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13936v1) | [下载PDF](https://arxiv.org/pdf/2607.13936v1.pdf)

---

## [20. Cyclone: Diffusion Model for Cycle-Consistent Weather Editing from Unpaired Driving Data](https://arxiv.org/abs/2607.13927v1)

**作者**：Thang-Anh-Quan Nguyen, Moussab Bennehar, Luis Guillermo Roldao Jimenez 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-15

### 📄 论文摘要

Reliable perception under diverse weather conditions remains a major challenge for autonomous driving systems. A common strategy to improve robustness is either to synthesize adverse weather conditions for training perception models or to apply weather-removal techniques to recover clean inputs. However, existing approaches typically rely on synthetic data augmentation or physics-based, task-specific models that require paired training data and often struggle to generate realistic weather effects or generalize robustly to out-of-domain scenarios. Toward this problem, we present Cyclone, a unified framework for weather editing based on latent diffusion, equipped with cycle-consistent constraints and knowledge from image-text models. Cyclone enables the generation of multiple weather conditions across diverse scenes while eliminating the need for paired data. Experimental results show that our approach produces more realistic, structure-preserving outputs than existing baselines and leads to consistent improvements across several downstream driving perception tasks. Furthermore, we demonstrate that Cyclone can be distilled to a video diffusion model for temporally consistent weather editing.

### 🤖 AI 总结

**一句话总结**：Reliable perception under diverse weather conditions remains a major challenge for autonomous driving systems. A common strategy to improve robustness is either to synthesize adverse weather condition...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Cyclone, Model, Cycle-Consistent, Weather, Editing, Unpaired, Driving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13927v1) | [下载PDF](https://arxiv.org/pdf/2607.13927v1.pdf)

---

## [21. Thresholded Cross-Attention for Reliable Intensity-Chromaticity Fusion in Low-Light Image Enhancement](https://arxiv.org/abs/2607.13925v1)

**作者**：Yanyi Wu, Xu Zhang, Junkai Chen 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-15

### 📄 论文摘要

Low-Light Image Enhancement (LLIE) requires a careful balance among noise suppression, color fidelity, and efficiency. Recent HVI-based methods alleviate color entanglement by decoupling intensity and chromaticity, yet how reliably the two streams are fused again is an overlooked factor that largely determines the final quality. We observe that the confidence of cross-stream attention is strongly layer-dependent, so the fixed-quota selection of Top-K sparse attention is mismatched to it, discarding informative dependencies in some layers while retaining noisy ones in others. Motivated by this observation, we propose TCA-Net, a network built around Thresholded Cross-Attention that targets reliable intensity-chromaticity fusion in the HVI space rather than introducing yet another color representation. At its core, TCA replaces the rigid Top-K quota with a fixed confidence threshold whose retained cardinality is input- and layer-adaptive, retaining only high-confidence cross-stream interactions while suppressing unreliable ones. Around this core, two complementary designs clean up the fusion before and after it: a Phase-guided Fourier Interaction Module provides a structure-aware brightness initialization for the intensity stream prior to fusion, and a Decoupled Dual-Stream Guidance Module constructs residual intensity features to suppress chromaticity leakage during reconstruction. A Scale-Aware Consistency Regularization further improves structural robustness under scale perturbations during training. Extensive experiments on LOL-v1, LOL-v2, Sony-Total-Dark, and LSRW-Huawei demonstrate that TCA-Net delivers competitive restoration accuracy, improved color fidelity, and a compact parameter size.

### 🤖 AI 总结

**一句话总结**：Low-Light Image Enhancement (LLIE) requires a careful balance among noise suppression, color fidelity, and efficiency. Recent HVI-based methods alleviate color entanglement by decoupling intensity and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Thresholded, Cross-Attention, Reliable, Intensity-Chromaticity, Fusion, Low-Light, Image, Enhancement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13925v1) | [下载PDF](https://arxiv.org/pdf/2607.13925v1.pdf)

---

## [22. The 2nd International StepUP Competition for Biometric Footstep Recognition: From Steps to Strides](https://arxiv.org/abs/2607.13905v1)

**作者**：Robyn Larracy, Anant Gupta, Gourav Gupta 等 11 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-07-15

### 📄 论文摘要

The International StepUP Competition Series was launched to advance research in pressure-based footstep biometrics through a standardized and challenging evaluation framework. Using the large-scale StepUP-P150 dataset (with more than 200,000 high-resolution dynamic footsteps from 150 individuals) and a previously unreleased test set, the 2nd edition of the competition addressed three key challenges: (1) generalization to unseen users with limited enrollment data, (2) robustness to domain shift caused by variations in footwear and walking speed and (3) effective fusion of paired left-right footsteps. While the first two challenges built on the inaugural competition, this edition introduced more extreme cross-domain conditions and moved beyond isolated footsteps to stride-level verification, enabling new opportunities for representation learning and inter-step information fusion. The competition attracted 26 registrants from academia and industry, with a best equal error rate of 8.00% achieved by the ArogyaPandit Research Team using a spatiotemporal CNN combined with an ensemble-based scoring strategy. The top solutions showcase the value of harnessing temporal patterns and of incorporating inference-time normalization and calibration strategies to improve scoring. However, the results also reveal that recognizing users in unseen personal footwear remains a challenge, especially in the presence of distractors with similar characteristics.

### 🤖 AI 总结

**一句话总结**：The International StepUP Competition Series was launched to advance research in pressure-based footstep biometrics through a standardized and challenging evaluation framework. Using the large-scale St...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：2nd, International, StepUP, Competition, Biometric, Footstep, Recognition, Steps

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13905v1) | [下载PDF](https://arxiv.org/pdf/2607.13905v1.pdf)

---

## cs.LG

## [23. MetaPerch: Learning from metadata for bioacoustics foundation models](https://arxiv.org/abs/2607.14072v1)

**作者**：Mustafa Chasmai, Vincent Dumoulin, Jenny Hamer  
**分类**：cs.LG, cs.SD  
**发布时间**：2026-07-15

### 📄 论文摘要

Bioacoustic foundation models rely on large-scale citizen science platforms like Xeno-Canto for geographically and ecologically diverse data. Recent work has shown that supervision alone can produce SotA species detection models when trained on this large-scale data -- however, there remains unutilized potential in the form of recording metadata readily available within these community-driven data hubs. In this work, we explore the use of metadata -- such as location and time -- as auxiliary supervision signals, allowing the model to leverage species-metadata correlations in its learned representation. Auxiliary metadata losses provide additional information beyond vocalizations alone that can encourage a richer, more robust representation that generalizes better to species distribution and acoustic domain shifts -- important challenges for deployment in real-world passive acoustic monitoring (PAM) settings. We introduce MetaPerch, a new foundation model that achieves strong species identification performance across multiple challenging domains and present an extensive empirical study of the effects of 9 diverse metadata sources on 17 bioacoustic datasets.

### 🤖 AI 总结

**一句话总结**：Bioacoustic foundation models rely on large-scale citizen science platforms like Xeno-Canto for geographically and ecologically diverse data. Recent work has shown that supervision alone can produce S...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MetaPerch, Learning, metadata, bioacoustics, foundation, models, Bioacoustic, rely

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.14072v1) | [下载PDF](https://arxiv.org/pdf/2607.14072v1.pdf)

---

## [24. Improving Wind and Solar Power Prediction with Efficient Wrapper-based Feature Selection: An Empirical Study](https://arxiv.org/abs/2607.14024v1)

**作者**：Daniel Grillmeyer, Marius Hadry, Michael Stenger 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-15

### 📄 论文摘要

With rising global energy demand and growing awareness of climate change and its impacts, the share of renewable energies in the global energy mix continues to grow. Unlike conventional power generation, the output of renewable energy sources cannot be controlled as consistently due to their dependence on environmental conditions. Therefore, reliable prediction of current and future energy production is essential. In this paper, we report findings from two structured literature reviews on real-world renewable energy prediction tasks: wind turbine power curve modeling and photovoltaic power prediction. For the former, we conducted a comprehensive literature review ourselves, while for the latter, we synthesize the key findings regarding frequently selected input features based on an existing survey. Across both domains, our analysis reveals that despite the large number of available monitoring and environmental variables, only limited or unsystematic methods for feature selection exist. To address this gap, we propose Cluster-based Sequential Feature Selection (CSFS), a novel, model-agnostic, clustering-based wrapper method for automatic, efficient, and reliable feature selection in renewable energy prediction pipelines. To support reproducibility and reuse, we provide an open-source implementation of CSFS on GitHub. We empirically evaluate the proposed approach on both use cases and compare it with established feature selection techniques such as wrapper-based sequential feature selection (SFS), filter-based methods, and Random Forest's embedded feature importance. The results show that the wrapper-based methods overall provide better-performing selections of features. CSFS achieves a predictive performance comparable to SFS while reducing computational cost by an average of 21%.

### 🤖 AI 总结

**一句话总结**：With rising global energy demand and growing awareness of climate change and its impacts, the share of renewable energies in the global energy mix continues to grow. Unlike conventional power generati...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Improving, Wind, Solar, Power, Prediction, Efficient, Wrapper-based, Feature

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.14024v1) | [下载PDF](https://arxiv.org/pdf/2607.14024v1.pdf)

---

## [25. Transforming Rank: How Architecture Navigates the Spectral Pathologies of Depth](https://arxiv.org/abs/2607.14018v1)

**作者**：Katie Everett  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-15

### 📄 论文摘要

We investigate how each component of the Transformer feedforward block architecture design determines how much rank survives across depth at initialization. We reinterpret skip connections and normalization, long understood as controlling magnitude, as mechanisms for preserving gradient rank across depth, since the very matrix multiplications and nonlinear activations that make the network expressive also reduce the rank. We show that skip connections trade off rank collapse against ensemble-like behavior, controlled by the relative scales of the branch and the skip: skip connections route the gradient around the residual branch, where rank is lost, rather than along the long gradient paths that encourage the layers to compose. The placement of the normalization layer controls this same tradeoff by setting the branch-to-skip ratio across depth, unifying much of the normalization placement and depth scaling literature, in particular why rank collapses for Post-Norm but plateaus for Pre-Norm. Other aspects of the architecture, like the two-matrix structure that expands and contracts the width, use additional parameters to preserve the representation or branch Jacobian rank. The second matrix decorrelates a coherent mean spike that would grow across blocks with a single matrix and uncentered activation, preventing the residual representation from collapsing. The width expansion between the two matrices keeps the branch Jacobian full rank: applying the rank-reducing activation in this expanded space leaves enough directions to span the original, at a width that follows a Marchenko--Pastur law. The initialization rank of the input--output Jacobian predicts which networks train on CIFAR-10. Taken together, we recast architecture design for deep networks as navigating an intrinsic tradeoff among rank collapse, ensemble-like behavior, and parameter count.

### 🤖 AI 总结

**一句话总结**：We investigate how each component of the Transformer feedforward block architecture design determines how much rank survives across depth at initialization. We reinterpret skip connections and normali...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Transforming, Rank, How, Architecture, Navigates, Spectral, Pathologies

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.14018v1) | [下载PDF](https://arxiv.org/pdf/2607.14018v1.pdf)

---

## [26. Lighthouse RL: Sample-Efficient Circuit Optimization via Strategic Reset Points](https://arxiv.org/abs/2607.14008v1)

**作者**：Mustafa Emre Gürsoy, Stefan Uhlich, Ryoga Matsuo 等 9 位作者  
**分类**：cs.LG, cs.AR  
**发布时间**：2026-07-15

### 📄 论文摘要

In this paper, we introduce Lighthouse RL, a sample-efficient reinforcement learning (RL) approach for analog circuit sizing. Traditional methods lack generalization across different performance targets, while standard RL approaches waste resources exploring unpromising regions. Our method addresses these inefficiencies through a strategic reset strategy that initializes episodes from high-performing configurations discovered during training, called "lighthouses". These states, which are closer to the target objectives, guide exploration toward promising regions. When compared to RL and Bayesian optimization methods from the literature, we demonstrate the effectiveness of our approach on a 2D benchmark problem and on two analog circuits, showing significant improvements in sample efficiency (up to 1.72x faster), optimization performance (100% vs. 0-87% success rate), generalization (75% vs. 0-50% extrapolation success), and objective maximization. This efficiency is particularly valuable for computationally expensive black-box optimization problems, and our reset strategy can be used as a plug-and-play enhancement for any RL-based optimization approach.

### 🤖 AI 总结

**一句话总结**：In this paper, we introduce Lighthouse RL, a sample-efficient reinforcement learning (RL) approach for analog circuit sizing. Traditional methods lack generalization across different performance targe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Lighthouse, Sample-Efficient, Circuit, Optimization, via, Strategic, Reset

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.14008v1) | [下载PDF](https://arxiv.org/pdf/2607.14008v1.pdf)

---

## [27. Lyapunov Exponent as Physics-Informed Dense Reward: RL Discovery of Stabilization Beyond the Kapitza Pendulum](https://arxiv.org/abs/2607.14001v1)

**作者**：Slava Andrejev  
**分类**：cs.LG  
**发布时间**：2026-07-15

### 📄 论文摘要

We suggest using the Lyapunov characteristic exponent (LCE) as a dense reward signal for the reinforcement learning problem of stabilizing the inverted pendulum with vertical motion. With LCE, the agent not only successfully found the oscillatory motion known as the Kapitza pendulum but also damped the pendulum's pivoting, leaving it in a strictly upright position.

### 🤖 AI 总结

**一句话总结**：We suggest using the Lyapunov characteristic exponent (LCE) as a dense reward signal for the reinforcement learning problem of stabilizing the inverted pendulum with vertical motion. With LCE, the age...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, RL, Lyapunov, Exponent, Physics-Informed, Dense, Reward, Discovery

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.14001v1) | [下载PDF](https://arxiv.org/pdf/2607.14001v1.pdf)

---

## [28. TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents](https://arxiv.org/abs/2607.13988v1)

**作者**：Leitian Tao, Baolin Peng, Wenlin Yao 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-15

### 📄 论文摘要

Multi-turn agents solve complex tasks through extended sequences of tool interactions before producing a final answer, making credit assignment a fundamental challenge during post-training. Outcome rewards provide reliable supervision for short-horizon reasoning, but become sparse and high-variance as trajectories grow to tens or hundreds of tool calls. They can also be misleading: a failed rollout may contain many useful actions that move the agent closer to the goal, yet outcome-only training assigns them the same negative advantage as the eventual mistake. We propose TRACE (Turn-level Reward Assignment via Credit Estimation), a dense credit-assignment method for agentic reinforcement learning. TRACE represents rollouts as state transitions at tool-call boundaries, obtains gold-answer log-probabilities from a frozen reference model, transforms them into log-ratio state values, and derives per-action rewards as Temporal-Difference changes in those values. This requires no additional critic or process-label training, and its one-step log-ratio TD component telescopes across redundant tool calls. On long-horizon complex search, TRACE substantially improves base-model tool-use ability using pure RL, without a cold-start supervised fine-tuning stage, an agentic mid-training stage, or training on live-web data. On the closed-web BrowseComp-Plus benchmark, it raises Qwen3-4B from $7.2$ to $35.6$ and Qwen3-30B-A3B from $8.4$ to $42.6$. The learned search behavior also transfers to open-web benchmarks, and the learning curves show earlier improvement and faster convergence during RL training.

### 🤖 AI 总结

**一句话总结**：Multi-turn agents solve complex tasks through extended sequences of tool interactions before producing a final answer, making credit assignment a fundamental challenge during post-training. Outcome re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TRACE, Turn-level, Reward, Assignment, via, Credit, Estimation, Long-Horizon

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13988v1) | [下载PDF](https://arxiv.org/pdf/2607.13988v1.pdf)

---

## [29. RF Spectrogram Anomaly Detection with Quantum Kitchen Sinks: Architecture, Representation, and Hardware Validation](https://arxiv.org/abs/2607.13897v1)

**作者**：Abdallah Aaraba, Alexis Vieloszynski, Remon Polus 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-15

### 📄 论文摘要

The broadcast nature of wireless channels exposes radio-frequency (RF) networks to anomalous and malicious transmissions, making anomaly detection a fundamental requirement for secure spectrum management. Quantum Kitchen Sinks (QKS) offer a lightweight hybrid quantum feature map suitable for near-term quantum devices, yet their behavior on structured signal data remains poorly understood. In this paper, we extend the standard QKS template with multi-depth data re-uploading and ring entanglement, and evaluate the resulting pipeline on controlled RF spectrogram anomaly detection. We introduce a validation-locked five-stage ablation protocol that systematically separates the effects of shallow architecture, re-uploading depth, episode budget, input representation, and classical readout. Across the completed benchmark, Discrete Cosine Transform (DCT) representations consistently dominate raw and Principal Component Analysis (PCA) inputs, moderate-depth entangled QKS configurations form the strongest operating regime, and QKS improves over matched classical direct-readout baselines across all evaluated representation-readout pairs on the held-out test set, with the best configuration reaching a test Area Under the Receiver Operating Characteristic curve (AUROC) of 0.8778 and a test F1 of 0.7995. The study bridges two levels of realism: real measured sub-6\,GHz cellular signals on the data side and real-device validation on the ibm_quebec Quantum Processing Unit (QPU) on the computing side, with AUROC deviations below 0.013 relative to simulation. These results provide a practical, reproducible framework for deploying QKS-based anomaly detection in wireless networks.

### 🤖 AI 总结

**一句话总结**：The broadcast nature of wireless channels exposes radio-frequency (RF) networks to anomalous and malicious transmissions, making anomaly detection a fundamental requirement for secure spectrum managem...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RF, Spectrogram, Anomaly, Detection, Quantum, Kitchen, Sinks, Architecture

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13897v1) | [下载PDF](https://arxiv.org/pdf/2607.13897v1.pdf)

---

## [30. PiVoT: A Variational Solution for Real-time Large-scale Multi-object Detection and Tracking under Heavy Clutter](https://arxiv.org/abs/2607.13891v1)

**作者**：Runze Gan, Qing Li, Simon J. Godsill 等 5 位作者  
**分类**：cs.LG, cs.CV, eess.SP  
**发布时间**：2026-07-15

### 📄 论文摘要

Multi-object detection and tracking from noisy point clouds remain challenging in many data-scarce radar applications. Current Bayesian trackers based on Poisson measurement models offer a training-free solution but struggle to achieve accuracy and efficiency under severe clutter, large object populations, and full-resolution Doppler point clouds. We address this with PiVoT, a fast, clutter-resilient multi-object tracker for both positional and Doppler measurements. PiVoT performs end-to-end detection and tracking of a large and time-varying number of objects without external clustering or detectors, through joint inference of object states, shapes, existence probabilities, data association, and measurement rates. Its efficiency is driven by several variational inference innovations, such as theoretically justified birth pruning, quadratic-to-linear complexity reductions for exact updates, and a computationally efficient Doppler Poisson model. Experiments show that PiVoT substantially outperforms existing Bayesian trackers in challenging scenes, while also demonstrating exceptional scalability to a thousand objects, robustness to clutter visually inseparable from objects, and real-time operation on full-scale modern automotive radar datasets, where it attains performance comparable to a deep-learning detection benchmark as a training-free joint detector and tracker.

### 🤖 AI 总结

**一句话总结**：Multi-object detection and tracking from noisy point clouds remain challenging in many data-scarce radar applications. Current Bayesian trackers based on Poisson measurement models offer a training-fr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PiVoT, Variational, Solution, Real-time, Large-scale, Multi-object, Detection, Tracking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.13891v1) | [下载PDF](https://arxiv.org/pdf/2607.13891v1.pdf)

---

