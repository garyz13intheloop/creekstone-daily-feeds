# arXiv AI 论文日报 | 2026-04-23

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (5 篇)
- [cs.CV](#csCV) (7 篇)
- [cs.LG](#csLG) (11 篇)
- [cs.AI](#csAI) (7 篇)

---

## cs.AI

## [1. Diagnosing CFG Interpretation in LLMs](https://arxiv.org/abs/2604.20811v1)

**作者**：Hanqi Li, Lu Chen, Kai Yu  
**分类**：cs.AI  
**发布时间**：2026-04-22

### 📄 论文摘要

As LLMs are increasingly integrated into agentic systems, they must adhere to dynamically defined, machine-interpretable interfaces. We evaluate LLMs as in-context interpreters: given a novel context-free grammar, can LLMs generate syntactically valid, behaviorally functional, and semantically faithful outputs? We introduce RoboGrid, a framework that disentangles syntax, behavior, and semantics through controlled stress-tests of recursion depth, expression complexity, and surface styles. Our experiments reveal a consistent hierarchical degradation: LLMs often maintain surface syntax but fail to preserve structural semantics. Despite the partial mitigation provided by CoT reasoning, performance collapses under structural density, specifically deep recursion and high branching, with semantic alignment vanishing at extreme depths. Furthermore, "Alien" lexicons reveal that LLMs rely on semantic bootstrapping from keywords rather than pure symbolic induction. These findings pinpoint critical gaps in hierarchical state-tracking required for reliable, grammar-agnostic agents.

### 🤖 AI 总结

**一句话总结**：As LLMs are increasingly integrated into agentic systems, they must adhere to dynamically defined, machine-interpretable interfaces. We evaluate LLMs as in-context interpreters: given a novel context-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, As, Diagnosing, CFG, Interpretation, increasingly, integrated, agentic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20811v1) | [下载PDF](https://arxiv.org/pdf/2604.20811v1.pdf)

---

## [2. Automatic Ontology Construction Using LLMs as an External Layer of Memory, Verification, and Planning for Hybrid Intelligent Systems](https://arxiv.org/abs/2604.20795v1)

**作者**：Pavel Salovskii, Iuliia Gorshkova  
**分类**：cs.AI  
**发布时间**：2026-04-22

### 📄 论文摘要

This paper presents a hybrid architecture for intelligent systems in which large language models (LLMs) are extended with an external ontological memory layer. Instead of relying solely on parametric knowledge and vector-based retrieval (RAG), the proposed approach constructs and maintains a structured knowledge graph using RDF/OWL representations, enabling persistent, verifiable, and semantically grounded reasoning.   The core contribution is an automated pipeline for ontology construction from heterogeneous data sources, including documents, APIs, and dialogue logs. The system performs entity recognition, relation extraction, normalization, and triple generation, followed by validation using SHACL and OWL constraints, and continuous graph updates. During inference, LLMs operate over a combined context that integrates vector-based retrieval with graph-based reasoning and external tool interaction.   Experimental observations on planning tasks, including the Tower of Hanoi benchmark, indicate that ontology augmentation improves performance in multi-step reasoning scenarios compared to baseline LLM systems. In addition, the ontology layer enables formal validation of generated outputs, transforming the system into a generation-verification-correction pipeline.   The proposed architecture addresses key limitations of current LLM-based systems, including lack of long-term memory, weak structural understanding, and limited reasoning capabilities. It provides a foundation for building agent-based systems, robotics applications, and enterprise AI solutions that require persistent knowledge, explainability, and reliable decision-making.

### 🤖 AI 总结

**一句话总结**：This paper presents a hybrid architecture for intelligent systems in which large language models (LLMs) are extended with an external ontological memory layer. Instead of relying solely on parametric ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, as, an, Automatic, Ontology, Construction, External, Layer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20795v1) | [下载PDF](https://arxiv.org/pdf/2604.20795v1.pdf)

---

## [3. SWE-chat: Coding Agent Interactions From Real Users in the Wild](https://arxiv.org/abs/2604.20779v1)

**作者**：Joachim Baumann, Vishakh Padmakumar, Xiang Li 等 6 位作者  
**分类**：cs.AI, cs.CY, cs.SE  
**发布时间**：2026-04-22

### 📄 论文摘要

AI coding agents are being adopted at scale, yet we lack empirical evidence on how people actually use them and how much of their output is useful in practice. We present SWE-chat, the first large-scale dataset of real coding agent sessions collected from open-source developers in the wild. The dataset currently contains 6,000 sessions, comprising more than 63,000 user prompts and 355,000 agent tool calls. SWE-chat is a living dataset; our collection pipeline automatically and continually discovers and processes sessions from public repositories. Leveraging SWE-chat, we provide an initial empirical characterization of real-world coding agent usage and failure modes. We find that coding patterns are bimodal: in 41% of sessions, agents author virtually all committed code ("vibe coding"), while in 23%, humans write all code themselves. Despite rapidly improving capabilities, coding agents remain inefficient in natural settings. Just 44% of all agent-produced code survives into user commits, and agent-written code introduces more security vulnerabilities than code authored by humans. Furthermore, users push back against agent outputs -- through corrections, failure reports, and interruptions -- in 44% of all turns. By capturing complete interaction traces with human vs. agent code authorship attribution, SWE-chat provides an empirical foundation for moving beyond curated benchmarks towards an evidence-based understanding of how AI agents perform in real developer workflows.

### 🤖 AI 总结

**一句话总结**：AI coding agents are being adopted at scale, yet we lack empirical evidence on how people actually use them and how much of their output is useful in practice. We present SWE-chat, the first large-sca...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SWE-chat, Coding, Interactions, Real, Users, Wild, being

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20779v1) | [下载PDF](https://arxiv.org/pdf/2604.20779v1.pdf)

---

## [4. V-tableR1: Process-Supervised Multimodal Table Reasoning with Critic-Guided Policy Optimization](https://arxiv.org/abs/2604.20755v1)

**作者**：Yubo Jiang, Yitong An, Xin Yang 等 10 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-04-22

### 📄 论文摘要

We introduce V-tableR1, a process-supervised reinforcement learning framework that elicits rigorous, verifiable reasoning from multimodal large language models (MLLMs). Current MLLMs trained solely on final outcomes often treat visual reasoning as a black box, relying on superficial pattern matching rather than performing rigorous multi-step inference. While Reinforcement Learning with Verifiable Rewards could enforce transparent reasoning trajectories, extending it to visual domains remains severely hindered by the ambiguity of grounding abstract logic into continuous pixel space. We solve this by leveraging the deterministic grid structure of tables as an ideal visual testbed. V-tableR1 employs a specialized critic VLM to provide dense, step-level feedback on the explicit visual chain-of-thought generated by a policy VLM. To optimize this system, we propose Process-Guided Direct Alignment Policy Optimization (PGPO), a novel RL algorithm integrating process rewards, decoupled policy constraints, and length-aware dynamic sampling. Extensive evaluations demonstrate that V-tableR1 explicitly penalizes visual hallucinations and shortcut guessing. By fundamentally shifting multimodal inference from black-box pattern matching to verifiable logical derivation, V-tableR1 4B establishes state-of-the-art accuracy among open-source models on complex tabular benchmarks, outperforming models up to 18x its size and improving over its SFT baseline

### 🤖 AI 总结

**一句话总结**：We introduce V-tableR1, a process-supervised reinforcement learning framework that elicits rigorous, verifiable reasoning from multimodal large language models (MLLMs). Current MLLMs trained solely on...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：V-tableR1, Process-Supervised, Multimodal, Table, Reasoning, Critic-Guided, Policy, Optimization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20755v1) | [下载PDF](https://arxiv.org/pdf/2604.20755v1.pdf)

---

## [5. Where and What: Reasoning Dynamic and Implicit Preferences in Situated Conversational Recommendation](https://arxiv.org/abs/2604.20749v1)

**作者**：Dongding Lin, Jian Wang, Yongqi Li 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-22

### 📄 论文摘要

Situated conversational recommendation (SCR), which utilizes visual scenes grounded in specific environments and natural language dialogue to deliver contextually appropriate recommendations, has emerged as a promising research direction due to its close alignment with real-world scenarios. Compared to traditional recommendations, SCR requires a deeper understanding of dynamic and implicit user preferences, as the surrounding scene often influences users' underlying interests, while both may evolve across conversations. This complexity significantly impacts the timing and relevance of recommendations. To address this, we propose situated preference reasoning (SiPeR), a novel framework that integrates two core mechanisms: (1) Scene transition estimation, which estimates whether the current scene satisfies user needs, and guides the user toward a more suitable scene when necessary; and (2) Bayesian inverse inference, which leverages the likelihood of multimodal large language models (MLLMs) to predict user preferences about candidate items within the scene. Extensive experiments on two representative benchmarks demonstrate SiPeR's superiority in both recommendation accuracy and response generation quality. The code and data are available at https://github.com/DongdingLin/SiPeR.

### 🤖 AI 总结

**一句话总结**：Situated conversational recommendation (SCR), which utilizes visual scenes grounded in specific environments and natural language dialogue to deliver contextually appropriate recommendations, has emer...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Where, What, Reasoning, Dynamic, Implicit, Preferences, Situated, Conversational

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20749v1) | [下载PDF](https://arxiv.org/pdf/2604.20749v1.pdf)

---

## [6. AAC: Admissible-by-Architecture Differentiable Landmark Compression for ALT](https://arxiv.org/abs/2604.20744v1)

**作者**：An T. Le, Vien Ngo  
**分类**：cs.AI, cs.LG, cs.RO  
**发布时间**：2026-04-22

### 📄 论文摘要

We introduce \textbf{AAC} (Architecturally Admissible Compressor), a differentiable landmark-selection module for ALT (A*, Landmarks, and Triangle inequality) shortest-path heuristics whose outputs are admissible by construction: each forward pass is a row-stochastic mixture of triangle-inequality lower bounds, so the heuristic is admissible for \emph{every} parameter setting without requiring convergence, calibration, or projection. At deployment, the module reduces to classical ALT on a learned subset, composing end-to-end with neural encoders while preserving the classical toolchain. The construction is the first differentiable instance of the compress-while-preserving-admissibility tradition in classical heuristic search.   Under a matched per-vertex memory protocol, we establish that ALT with farthest-point-sampling landmarks (FPS-ALT) has provably near-optimal coverage on metric graphs, leaving at most a few percentage points of headroom for \emph{any} selector. AAC operates near this ceiling: the gap is $0.9$--$3.9$ percentage points on 9 road networks and ${\leq}1.3$ percentage points on synthetic graphs, with zero admissibility violations across $1{,}500+$ queries and all logged runs. At matched memory, AAC is also $1.2$--$1.5{\times}$ faster than FPS-ALT at the median query on DIMACS road networks, amortizing its offline cost within $170$--$1{,}924$ queries. A controlled ablation isolates the binding constraint: training-objective drift under default initialization, not architectural capacity; identity-on-first-$m$ initialization closes the expansion-count gap entirely. We release the module, a reusable matched-memory benchmarking protocol with paired two-one-sided-test (TOST) equivalence and pre-registration, and a reference compressed-differential-heuristics baseline.

### 🤖 AI 总结

**一句话总结**：We introduce \textbf{AAC} (Architecturally Admissible Compressor), a differentiable landmark-selection module for ALT (A*, Landmarks, and Triangle inequality) shortest-path heuristics whose outputs ar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, AAC, Differentiable, Landmark, Compression, ALT, introduce, textbf

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20744v1) | [下载PDF](https://arxiv.org/pdf/2604.20744v1.pdf)

---

## [7. Interval POMDP Shielding for Imperfect-Perception Agents](https://arxiv.org/abs/2604.20728v1)

**作者**：William Scarbro, Ravi Mangal  
**分类**：cs.AI, eess.SY  
**发布时间**：2026-04-22

### 📄 论文摘要

Autonomous systems that rely on learned perception can make unsafe decisions when sensor readings are misclassified. We study shielding for this setting: given a proposed action, a shield blocks actions that could violate safety. We consider the common case where system dynamics are known but perception uncertainty must be estimated from finite labeled data. From these data we build confidence intervals for the probabilities of perception outcomes and use them to model the system as a finite Interval Partially Observable Markov Decision Process with discrete states and actions. We then propose an algorithm to compute a conservative set of beliefs over the underlying state that is consistent with the observations seen so far.   This enables us to construct a runtime shield that comes with a finite-horizon guarantee: with high probability over the training data, if the true perception uncertainty rates lie within the learned intervals, then every action admitted by the shield satisfies a stated lower bound on safety. Experiments on four case studies show that our shielding approach (and variants derived from it) improves the safety of the system over state-of-the-art baselines.

### 🤖 AI 总结

**一句话总结**：Autonomous systems that rely on learned perception can make unsafe decisions when sensor readings are misclassified. We study shielding for this setting: given a proposed action, a shield blocks actio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Interval, POMDP, Shielding, Imperfect-Perception, Autonomous, systems, rely

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20728v1) | [下载PDF](https://arxiv.org/pdf/2604.20728v1.pdf)

---

## cs.CL

## [8. SpeechParaling-Bench: A Comprehensive Benchmark for Paralinguistic-Aware Speech Generation](https://arxiv.org/abs/2604.20842v1)

**作者**：Ruohan Liu, Shukang Yin, Tao Wang 等 9 位作者  
**分类**：cs.CL, cs.AI, cs.SD  
**发布时间**：2026-04-22

### 📄 论文摘要

Paralinguistic cues are essential for natural human-computer interaction, yet their evaluation in Large Audio-Language Models (LALMs) remains limited by coarse feature coverage and the inherent subjectivity of assessment. To address these challenges, we introduce SpeechParaling-Bench, a comprehensive benchmark for paralinguistic-aware speech generation. It expands existing coverage from fewer than 50 to over 100 fine-grained features, supported by more than 1,000 English-Chinese parallel speech queries, and is organized into three progressively challenging tasks: fine-grained control, intra-utterance variation, and context-aware adaptation. To enable reliable evaluation, we further develop a pairwise comparison pipeline, in which candidate responses are evaluated against a fixed baseline by an LALM-based judge. By framing evaluation as relative preference rather than absolute scoring, this approach mitigates subjectivity and yields more stable and scalable assessments without costly human annotation. Extensive experiments reveal substantial limitations in current LALMs. Even leading proprietary models struggle with comprehensive static control and dynamic modulation of paralinguistic features, while failure to correctly interpret paralinguistic cues accounts for 43.3% of errors in situational dialogue. These findings underscore the need for more robust paralinguistic modeling toward human-aligned voice assistants.

### 🤖 AI 总结

**一句话总结**：Paralinguistic cues are essential for natural human-computer interaction, yet their evaluation in Large Audio-Language Models (LALMs) remains limited by coarse feature coverage and the inherent subjec...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SpeechParaling-Bench, Comprehensive, Benchmark, Paralinguistic-Aware, Speech, Generation, Paralinguistic, cues

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20842v1) | [下载PDF](https://arxiv.org/pdf/2604.20842v1.pdf)

---

## [9. Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL](https://arxiv.org/abs/2604.20835v1)

**作者**：Zhaofeng Wu, Shiqi Wang, Boya Peng 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-22

### 📄 论文摘要

Modern language models demonstrate impressive coding capabilities in common programming languages (PLs), such as C++ and Python, but their performance in lower-resource PLs is often limited by training data availability. In principle, however, most programming skills are universal across PLs, so the capability acquired in one PL should transfer to others. In this work, we propose the task of zero-shot cross-programming-language transfer for code RL. We find that, for Llama-3.1, RL training for code generation in a source PL fails to improve, and sometimes even degrades, the performance on other target PLs. To address this, we hypothesize that effective RL transfer requires a generalizable SFT initialization before RL. We thus propose **Parallel-SFT**, an SFT strategy that incorporates "parallel programs" -- functionally equivalent code implemented in multiple PLs -- into the data mixture. We demonstrate that this improves transferability: when we subsequently perform RL on our Parallel-SFT model, we observe better generalization to unseen PLs. Analysis of the model internal representations reveals that Parallel-SFT leads to a more functionality-centric latent space, where equivalent programs across PLs are more tightly clustered, which we hypothesize to contribute to the improved transferability.

### 🤖 AI 总结

**一句话总结**：Modern language models demonstrate impressive coding capabilities in common programming languages (PLs), such as C++ and Python, but their performance in lower-resource PLs is often limited by trainin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Parallel-SFT, Improving, Zero-Shot, Transfer, Code, Modern, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20835v1) | [下载PDF](https://arxiv.org/pdf/2604.20835v1.pdf)

---

## [10. Can "AI" Be a Doctor? A Study of Empathy, Readability, and Alignment in Clinical LLMs](https://arxiv.org/abs/2604.20791v1)

**作者**：Mariano Barone, Francesco Di Serio, Roberto Moio 等 7 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-22

### 📄 论文摘要

Large Language Models (LLMs) are increasingly deployed in healthcare, yet their communicative alignment with clinical standards remains insufficiently quantified. We conduct a multidimensional evaluation of general-purpose and domain-specialized LLMs across structured medical explanations and real-world physician-patient interactions, analyzing semantic fidelity, readability, and affective resonance. Baseline models amplify affective polarity relative to physicians (Very Negative: 43.14-45.10% vs. 37.25%) and, in larger architectures such as GPT-5 and Claude, produce substantially higher linguistic complexity (FKGL up to 16.91-17.60 vs. 11.47-12.50 in physician-authored responses). Empathy-oriented prompting reduces extreme negativity and lowers grade-level complexity (up to -6.87 FKGL points for GPT-5) but does not significantly increase semantic fidelity. Collaborative rewriting yields the strongest overall alignment. Rephrase configurations achieve the highest semantic similarity to physician answers (up to mean = 0.93) while consistently improving readability and reducing affective extremity. Dual stakeholder evaluation shows that no model surpasses physicians on epistemic criteria, whereas patients consistently prefer rewritten variants for clarity and emotional tone. These findings suggest that LLMs function most effectively as collaborative communication enhancers rather than replacements for clinical expertise.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) are increasingly deployed in healthcare, yet their communicative alignment with clinical standards remains insufficiently quantified. We conduct a multidimensional evaluat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**："AI", Be, of, Can, Doctor?, Study, Empathy, Readability

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20791v1) | [下载PDF](https://arxiv.org/pdf/2604.20791v1.pdf)

---

## [11. Working Memory Constraints Scaffold Learning in Transformers under Data Scarcity](https://arxiv.org/abs/2604.20789v1)

**作者**：Pranava Madhyastha, Dagmar Adamcova  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-04-22

### 📄 论文摘要

We investigate the integration of human-like working memory constraints into the Transformer architecture and implement several cognitively inspired attention variants, including fixed-width windows based and temporal decay based attention mechanisms. Our modified GPT-2 models are trained from scratch on developmentally plausible datasets (10M and 100M words). Performance is evaluated on grammatical judgment tasks (BLiMP) and alignment with human reading time data. Our results indicate that these cognitively-inspired constraints, particularly fixed-width attention, can significantly improve grammatical accuracy especially when training data is scarce. These constrained models also tend to show a stronger alignment with human processing metrics. The findings suggest that such constraints may serve as a beneficial inductive bias, guiding models towards more robust linguistic representations, especially in data-limited settings.

### 🤖 AI 总结

**一句话总结**：We investigate the integration of human-like working memory constraints into the Transformer architecture and implement several cognitively inspired attention variants, including fixed-width windows b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Working, Memory, Constraints, Scaffold, Learning, Transformers, under, Data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20789v1) | [下载PDF](https://arxiv.org/pdf/2604.20789v1.pdf)

---

## [12. RespondeoQA: a Benchmark for Bilingual Latin-English Question Answering](https://arxiv.org/abs/2604.20738v1)

**作者**：Marisa Hudspeth, Patrick J. Burns, Brendan O'Connor  
**分类**：cs.CL  
**发布时间**：2026-04-22

### 📄 论文摘要

We introduce a benchmark dataset for question answering and translation in bilingual Latin and English settings, containing about 7,800 question-answer pairs. The questions are drawn from Latin pedagogical sources, including exams, quizbowl-style trivia, and textbooks ranging from the 1800s to the present. After automated extraction, cleaning, and manual review, the dataset covers a diverse range of question types: knowledge- and skill-based, multihop reasoning, constrained translation, and mixed language pairs. To our knowledge, this is the first QA benchmark centered on Latin. As a case study, we evaluate three large language models -- LLaMa 3, Qwen QwQ, and OpenAI's o3-mini -- finding that all perform worse on skill-oriented questions. Although the reasoning models perform better on scansion and literary-device tasks, they offer limited improvement overall. QwQ performs slightly better on questions asked in Latin, but LLaMa3 and o3-mini are more task dependent. This dataset provides a new resource for assessing model capabilities in a specialized linguistic and cultural domain, and the creation process can be easily adapted for other languages. The dataset is available at: https://github.com/slanglab/RespondeoQA

### 🤖 AI 总结

**一句话总结**：We introduce a benchmark dataset for question answering and translation in bilingual Latin and English settings, containing about 7,800 question-answer pairs. The questions are drawn from Latin pedago...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, RespondeoQA, Benchmark, Bilingual, Latin-English, Question, Answering, introduce

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20738v1) | [下载PDF](https://arxiv.org/pdf/2604.20738v1.pdf)

---

## cs.CV

## [13. DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation](https://arxiv.org/abs/2604.20841v1)

**作者**：Hyeonwoo Kim, Jeonghwan Kim, Kyungwon Cho 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-22

### 📄 论文摘要

Recent advances in video generative models enable the synthesis of realistic human-object interaction videos across a wide range of scenarios and object categories, including complex dexterous manipulations that are difficult to capture with motion capture systems. While the rich interaction knowledge embedded in these synthetic videos holds strong potential for motion planning in dexterous robotic manipulation, their limited physical fidelity and purely 2D nature make them difficult to use directly as imitation targets in physics-based character control. We present DeVI (Dexterous Video Imitation), a novel framework that leverages text-conditioned synthetic videos to enable physically plausible dexterous agent control for interacting with unseen target objects. To overcome the imprecision of generative 2D cues, we introduce a hybrid tracking reward that integrates 3D human tracking with robust 2D object tracking. Unlike methods relying on high-quality 3D kinematic demonstrations, DeVI requires only the generated video, enabling zero-shot generalization across diverse objects and interaction types. Extensive experiments demonstrate that DeVI outperforms existing approaches that imitate 3D human-object interaction demonstrations, particularly in modeling dexterous hand-object interactions. We further validate the effectiveness of DeVI in multi-object scenes and text-driven action diversity, showcasing the advantage of using video as an HOI-aware motion planner.

### 🤖 AI 总结

**一句话总结**：Recent advances in video generative models enable the synthesis of realistic human-object interaction videos across a wide range of scenarios and object categories, including complex dexterous manipul...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DeVI, Physics-based, Dexterous, Human-Object, Interaction, via, Synthetic, Video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20841v1) | [下载PDF](https://arxiv.org/pdf/2604.20841v1.pdf)

---

## [14. Global Offshore Wind Infrastructure: Deployment and Operational Dynamics from Dense Sentinel-1 Time Series](https://arxiv.org/abs/2604.20822v1)

**作者**：Thorsten Hoeser, Felix Bachofer, Claudia Kuenzer  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-04-22

### 📄 论文摘要

The offshore wind energy sector is expanding rapidly, increasing the need for independent, high-temporal-resolution monitoring of infrastructure deployment and operation at global scale. While Earth Observation based offshore wind infrastructure mapping has matured for spatial localization, existing open datasets lack temporally dense and semantically fine-grained information on construction and operational dynamics. We introduce a global Sentinel-1 synthetic aperture radar (SAR) time series data corpus that resolves deployment and operational phases of offshore wind infrastructure from 2016Q1 to 2025Q1. Building on an updated object detection workflow, we compile 15,606 time series at detected infrastructure locations, with overall 14,840,637 events as analysis-ready 1D SAR backscatter profiles, one profile per Sentinel-1 acquisition and location. To enable direct use and benchmarking, we release (i) the analysis ready 1D SAR profiles, (ii) event-level baseline semantic labels generated by a rule-based classifier, and (iii) an expert-annotated benchmark dataset of 553 time series with 328,657 event labels. The baseline classifier achieves a macro F1 score of 0.84 in event-wise evaluation and an area under the collapsed edit similarity-quality threshold curve (AUC) of 0.785, indicating temporal coherence. We demonstrate that the resulting corpus supports global-scale analyses of deployment dynamics, the identification of differences in regional deployment patterns, vessel interactions, and operational events, and provides a reference for developing and comparing time series classification methods for offshore wind infrastructure monitoring.

### 🤖 AI 总结

**一句话总结**：The offshore wind energy sector is expanding rapidly, increasing the need for independent, high-temporal-resolution monitoring of infrastructure deployment and operation at global scale. While Earth O...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Global, Offshore, Wind, Infrastructure, Deployment, Operational, Dynamics, Dense

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20822v1) | [下载PDF](https://arxiv.org/pdf/2604.20822v1.pdf)

---

## [15. OMIBench: Benchmarking Olympiad-Level Multi-Image Reasoning in Large Vision-Language Model](https://arxiv.org/abs/2604.20806v1)

**作者**：Qiguang Chen, Chengyu Luan, Jiajun Wu 等 10 位作者  
**分类**：cs.CV, cs.AI, cs.CL  
**发布时间**：2026-04-22

### 📄 论文摘要

Large vision-language models (LVLMs) have made substantial advances in reasoning tasks at the Olympiad level. Nevertheless, current Olympiad-level multimodal reasoning benchmarks for these models often emphasize single-image analysis and fail to exploit contextual information across multiple images. We present OMIBench, a benchmark designed to evaluate Olympiad-level reasoning when the required evidence is distributed over multiple images. It contains problems from biology, chemistry, mathematics, and physics Olympiads, together with manually annotated rationales and evaluation protocols for both exact and semantic answer matching. Across extensive experiments on OMIBench, we observe meaningful performance gaps in existing models. Even the strongest LVLMs, such as Gemini-3-Pro, attain only about 50% on the benchmark. These results position OMIBench as a focused resources for studying and improving multi-image reasoning in LVLMs.

### 🤖 AI 总结

**一句话总结**：Large vision-language models (LVLMs) have made substantial advances in reasoning tasks at the Olympiad level. Nevertheless, current Olympiad-level multimodal reasoning benchmarks for these models ofte...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OMIBench, Benchmarking, Olympiad-Level, Multi-Image, Reasoning, Large, Vision-Language, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20806v1) | [下载PDF](https://arxiv.org/pdf/2604.20806v1.pdf)

---

## [16. LEXIS: LatEnt ProXimal Interaction Signatures for 3D HOI from an Image](https://arxiv.org/abs/2604.20800v1)

**作者**：Dimitrije Antić, Alvaro Budria, George Paschalidis 等 5 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-04-22

### 📄 论文摘要

Reconstructing 3D Human-Object Interaction from an RGB image is essential for perceptive systems. Yet, this remains challenging as it requires capturing the subtle physical coupling between the body and objects. While current methods rely on sparse, binary contact cues, these fail to model the continuous proximity and dense spatial relationships that characterize natural interactions. We address this limitation via InterFields, a representation that encodes dense, continuous proximity across the entire body and object surfaces. However, inferring these fields from single images is inherently ill-posed. To tackle this, our intuition is that interaction patterns are characteristically structured by the action and object geometry. We capture this structure in LEXIS, a novel discrete manifold of interaction signatures learned via a VQ-VAE. We then develop LEXIS-Flow, a diffusion framework that leverages LEXIS signatures to estimate human and object meshes alongside their InterFields. Notably, these InterFields help in a guided refinement that ensures physically-plausible, proximity-aware reconstructions without requiring post-hoc optimization. Evaluation on Open3DHOI and BEHAVE shows that LEXIS-Flow significantly outperforms existing SotA baselines in reconstruction, contact, and proximity quality. Our approach not only improves generalization but also yields reconstructions perceived as more realistic, moving us closer to holistic 3D scene understanding. Code & models will be public at https://anticdimi.github.io/lexis.

### 🤖 AI 总结

**一句话总结**：Reconstructing 3D Human-Object Interaction from an RGB image is essential for perceptive systems. Yet, this remains challenging as it requires capturing the subtle physical coupling between the body a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, an, LEXIS, LatEnt, ProXimal, Interaction, Signatures, HOI

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20800v1) | [下载PDF](https://arxiv.org/pdf/2604.20800v1.pdf)

---

## [17. GeoRect4D: Geometry-Compatible Generative Rectification for Dynamic Sparse-View 3D Reconstruction](https://arxiv.org/abs/2604.20784v1)

**作者**：Zhenlong Wu, Zihan Zheng, Xuanxuan Wang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-22

### 📄 论文摘要

Reconstructing dynamic 3D scenes from sparse multi-view videos is highly ill-posed, often leading to geometric collapse, trajectory drift, and floating artifacts. Recent attempts introduce generative priors to hallucinate missing content, yet naive integration frequently causes structural drift and temporal inconsistency due to the mismatch between stochastic 2D generation and deterministic 3D geometry. In this paper, we propose GeoRect4D, a novel unified framework for sparse-view dynamic reconstruction that couples explicit 3D consistency with generative refinement via a closed-loop optimization process. Specifically, GeoRect4D introduces a degradation-aware feedback mechanism that incorporates a robust anchor-based dynamic 3DGS substrate with a single-step diffusion rectifier to hallucinate high-fidelity details. This rectifier utilizes a structural locking mechanism and spatiotemporal coordinated attention, effectively preserving physical plausibility while restoring missing content. Furthermore, we present a progressive optimization strategy that employs stochastic geometric purification to eliminate floaters and generative distillation to infuse texture details into the explicit representation. Extensive experiments demonstrate that GeoRect4D achieves state-of-the-art performance in reconstruction fidelity, perceptual quality, and spatiotemporal consistency across multiple datasets.

### 🤖 AI 总结

**一句话总结**：Reconstructing dynamic 3D scenes from sparse multi-view videos is highly ill-posed, often leading to geometric collapse, trajectory drift, and floating artifacts. Recent attempts introduce generative ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, GeoRect4D, Geometry-Compatible, Generative, Rectification, Dynamic, Sparse-View, Reconstruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20784v1) | [下载PDF](https://arxiv.org/pdf/2604.20784v1.pdf)

---

## [18. Amodal SAM: A Unified Amodal Segmentation Framework with Generalization](https://arxiv.org/abs/2604.20748v1)

**作者**：Bo Zhang, Zhuotao Tian, Xin Tao 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-22

### 📄 论文摘要

Amodal segmentation is a challenging task that aims to predict the complete geometric shape of objects, including their occluded regions. Although existing methods primarily focus on amodal segmentation within the training domain, these approaches often lack the generalization capacity to extend effectively to novel object categories and unseen contexts. This paper introduces Amodal SAM, a unified framework that leverages SAM (Segment Anything Model) for both amodal image and amodal video segmentation. Amodal SAM preserves the powerful generalization ability of SAM while extending its inherent capabilities to the amodal segmentation task. The improvements lie in three aspects: (1) a lightweight Spatial Completion Adapter that enables occluded region reconstruction, (2) a Target-Aware Occlusion Synthesis (TAOS) pipeline that addresses the scarcity of amodal annotations by generating diverse synthetic training data, and (3) novel learning objectives that enforce regional consistency and topological regularization. Extensive experiments demonstrate that Amodal SAM achieves state-of-the-art performance on standard benchmarks, while simultaneously exhibiting robust generalization to novel scenarios. We anticipate that this research will advance the field toward practical amodal segmentation systems capable of operating effectively in unconstrained real-world environments.

### 🤖 AI 总结

**一句话总结**：Amodal segmentation is a challenging task that aims to predict the complete geometric shape of objects, including their occluded regions. Although existing methods primarily focus on amodal segmentati...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Amodal, SAM, Unified, Segmentation, Framework, Generalization, challenging, task

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20748v1) | [下载PDF](https://arxiv.org/pdf/2604.20748v1.pdf)

---

## [19. Render-in-the-Loop: Vector Graphics Generation via Visual Self-Feedback](https://arxiv.org/abs/2604.20730v1)

**作者**：Guotao Liang, Zhangcheng Wang, Juncheng Hu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-22

### 📄 论文摘要

Multimodal Large Language Models (MLLMs) have shown promising capabilities in generating Scalable Vector Graphics (SVG) via direct code synthesis. However, existing paradigms typically adopt an open-loop "blind drawing" approach, where models generate symbolic code sequences without perceiving intermediate visual outcomes. This methodology severely underutilizes the powerful visual priors embedded in MLLMs vision encoders, treating SVG generation as a disjointed textual sequence modeling task rather than an integrated visuo-spatial one. Consequently, models struggle to reason about partial canvas states and implicit occlusion relationships, which are visually explicit but textually ambiguous. To bridge this gap, we propose Render-in-the-Loop, a novel generation paradigm that reformulates SVG synthesis as a step-wise, visual-context-aware process. By rendering intermediate code states into a cumulative canvas, the model explicitly observes the evolving visual context at each step, leveraging on-the-fly feedback to guide subsequent generation. However, we demonstrate that applying this visual loop naively to off-the-shelf models is suboptimal due to their inability to leverage incremental visual-code mappings. To address this, we first utilize fine-grained path decomposition to construct dense multi-step visual trajectories, and then introduce a Visual Self-Feedback (VSF) training strategy to condition the next primitive generation on intermediate visual states. Furthermore, a Render-and-Verify (RaV) inference mechanism is proposed to effectively filter degenerate and redundant primitives. Our framework, instantiated on a multimodal foundation model, outperforms strong open-weight baselines on the standard MMSVGBench. This result highlights the remarkable data efficiency and generalization capability of our Render-in-the-Loop paradigm for both Text-to-SVG and Image-to-SVG tasks.

### 🤖 AI 总结

**一句话总结**：Multimodal Large Language Models (MLLMs) have shown promising capabilities in generating Scalable Vector Graphics (SVG) via direct code synthesis. However, existing paradigms typically adopt an open-l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Render-in-the-Loop, Vector, Graphics, Generation, via, Visual, Self-Feedback, Multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20730v1) | [下载PDF](https://arxiv.org/pdf/2604.20730v1.pdf)

---

## cs.LG

## [20. FedSIR: Spectral Client Identification and Relabeling for Federated Learning with Noisy Labels](https://arxiv.org/abs/2604.20825v1)

**作者**：Sina Gholami, Abdulmoneam Ali, Tania Haghighi 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CV, cs.DC, eess.SP  
**发布时间**：2026-04-22

### 📄 论文摘要

Federated learning (FL) enables collaborative model training without sharing raw data; however, the presence of noisy labels across distributed clients can severely degrade the learning performance. In this paper, we propose FedSIR, a multi-stage framework for robust FL under noisy labels. Different from existing approaches that mainly rely on designing noise-tolerant loss functions or exploiting loss dynamics during training, our method leverages the spectral structure of client feature representations to identify and mitigate label noise.   Our framework consists of three key components. First, we identify clean and noisy clients by analyzing the spectral consistency of class-wise feature subspaces with minimal communication overhead. Second, clean clients provide spectral references that enable noisy clients to relabel potentially corrupted samples using both dominant class directions and residual subspaces. Third, we employ a noise-aware training strategy that integrates logit-adjusted loss, knowledge distillation, and distance-aware aggregation to further stabilize federated optimization. Extensive experiments on standard FL benchmarks demonstrate that FedSIR consistently outperforms state-of-the-art methods for FL with noisy labels. The code is available at https://github.com/sinagh72/FedSIR.

### 🤖 AI 总结

**一句话总结**：Federated learning (FL) enables collaborative model training without sharing raw data; however, the presence of noisy labels across distributed clients can severely degrade the learning performance. I...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FedSIR, Spectral, Client, Identification, Relabeling, Federated, Learning, Noisy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20825v1) | [下载PDF](https://arxiv.org/pdf/2604.20825v1.pdf)

---

## [21. Closing the Domain Gap in Biomedical Imaging by In-Context Control Samples](https://arxiv.org/abs/2604.20824v1)

**作者**：Ana Sanchez-Fernandez, Thomas Pinetz, Werner Zellinger 等 4 位作者  
**分类**：cs.LG, q-bio.QM  
**发布时间**：2026-04-22

### 📄 论文摘要

The central problem in biomedical imaging are batch effects: systematic technical variations unrelated to the biological signal of interest. These batch effects critically undermine experimental reproducibility and are the primary cause of failure of deep learning systems on new experimental batches, preventing their practical use in the real world. Despite years of research, no method has succeeded in closing this performance gap for deep learning models. We propose Control-Stabilized Adaptive Risk Minimization via Batch Normalization (CS-ARM-BN), a meta-learning adaptation method that exploits negative control samples. Such unperturbed reference images are present in every experimental batch by design and serve as stable context for adaptation. We validate our novel method on Mechanism-of-Action (MoA) classification, a crucial task for drug discovery, on the large-scale JUMP-CP dataset. The accuracy of standard ResNets drops from 0.939 $\pm$ 0.005, on the training domain, to 0.862 $\pm$ 0.060 on data from new experimental batches. Foundation models, even after Typical Variation Normalization, fail to close this gap. We are the first to show that meta-learning approaches close the domain gap by achieving 0.935 $\pm$ 0.018. If the new experimental batches exhibit strong domain shifts, such as being generated in a different lab, meta-learning approaches can be stabilized with control samples, which are always available in biomedical experiments. Our work shows that batch effects in bioimaging data can be effectively neutralized through principled in-context adaptation, which also makes them practically usable and efficient.

### 🤖 AI 总结

**一句话总结**：The central problem in biomedical imaging are batch effects: systematic technical variations unrelated to the biological signal of interest. These batch effects critically undermine experimental repro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Closing, Domain, Gap, Biomedical, Imaging, In-Context, Control, Samples

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20824v1) | [下载PDF](https://arxiv.org/pdf/2604.20824v1.pdf)

---

## [22. ParetoSlider: Diffusion Models Post-Training for Continuous Reward Control](https://arxiv.org/abs/2604.20816v1)

**作者**：Shelly Golan, Michael Finkelson, Ariel Bereslavsky 等 5 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-04-22

### 📄 论文摘要

Reinforcement Learning (RL) post-training has become the standard for aligning generative models with human preferences, yet most methods rely on a single scalar reward. When multiple criteria matter, the prevailing practice of ``early scalarization'' collapses rewards into a fixed weighted sum. This commits the model to a single trade-off point at training time, providing no inference-time control over inherently conflicting goals -- such as prompt adherence versus source fidelity in image editing. We introduce ParetoSlider, a multi-objective RL (MORL) framework that trains a single diffusion model to approximate the entire Pareto front. By training the model with continuously varying preference weights as a conditioning signal, we enable users to navigate optimal trade-offs at inference time without retraining or maintaining multiple checkpoints. We evaluate ParetoSlider across three state-of-the-art flow-matching backbones: SD3.5, FluxKontext, and LTX-2. Our single preference-conditioned model matches or exceeds the performance of baselines trained separately for fixed reward trade-offs, while uniquely providing fine-grained control over competing generative goals.

### 🤖 AI 总结

**一句话总结**：Reinforcement Learning (RL) post-training has become the standard for aligning generative models with human preferences, yet most methods rely on a single scalar reward. When multiple criteria matter,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, ParetoSlider, Models, Post-Training, Continuous, Reward, Control, Reinforcement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20816v1) | [下载PDF](https://arxiv.org/pdf/2604.20816v1.pdf)

---

## [23. Physics-Conditioned Synthesis of Internal Ice-Layer Thickness for Incomplete Layer Traces](https://arxiv.org/abs/2604.20783v1)

**作者**：Zesheng Liu, Maryam Rahnemoonfar  
**分类**：cs.LG  
**发布时间**：2026-04-22

### 📄 论文摘要

Internal ice layers imaged by radar provide key evidence of snow accumulation and ice dynamics, but radar-derived layer boundary observations are often incomplete, with discontinuous traces and sometimes entirely missing layers, due to limited resolution, sensor noise, and signal loss. Existing graph-based models for ice stratigraphy generally assume sufficiently complete layer profiles and focus on predicting deeper-layer thickness from reliably traced shallow layers. In this work, we address the layer-completion problem itself by synthesizing complete ice-layer thickness annotations from incomplete radar-derived layer traces by conditioning on colocated physical features synchronized from physical climate models. The proposed network combines geometric learning to aggregate within-layer spatial context with a transformer-based temporal module that propagates information across layers to encourage coherent stratigraphy and consistent thickness evolution. To learn from incomplete supervision, we optimize a mask-aware robust regression objective that evaluates errors only at observed thickness values and normalizes by the number of valid entries, enabling stable training under varying sparsity without imputation and steering completions toward physically plausible values. The model preserves observed thickness where available and infers only missing regions, recovering fragmented segments and even fully absent layers while remaining consistent with measured traces. As an additional benefit, the synthesized thickness stacks provide effective pretraining supervision for a downstream deep-layer predictor, improving fine-tuned accuracy over training from scratch on the same fully traced data.

### 🤖 AI 总结

**一句话总结**：Internal ice layers imaged by radar provide key evidence of snow accumulation and ice dynamics, but radar-derived layer boundary observations are often incomplete, with discontinuous traces and someti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Physics-Conditioned, Synthesis, Internal, Ice-Layer, Thickness, Incomplete, Layer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20783v1) | [下载PDF](https://arxiv.org/pdf/2604.20783v1.pdf)

---

## [24. Efficient Multi-Cohort Inference for Long-Term Effects and Lifetime Value in A/B Testing with User Learning](https://arxiv.org/abs/2604.20777v1)

**作者**：Dario Simionato, Andrea Tonon, Mingxue Wang 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-22

### 📄 论文摘要

In streaming platforms churn is extremely costly, yet A/B tests are typically evaluated using outcomes observed within a limited experimental horizon. Even when both short- and predicted long-term engagement metrics are considered, they may fail to capture how a treatment affects users' retention. Consequently, an intervention may appear beneficial in the short term and neutral in the long term while still generating lower total value than the control due to users churn.   To address this limitation, we introduce a method that estimates long-term treatment effects (LTE) and residual lifetime value change ($ΔERLV$) in short multi-cohort A/B tests under user learning. To estimate time-varying treatment effects efficiently, we introduce an inverse-variance weighted estimator that combines multiple cohorts estimates, reducing variance relative to standard approaches in the literature. The estimated treatment trajectory is then modeled as a parametric decay to recover both the asymptotic treatment effect and the cumulative value generated over time.   Our framework enables simultaneous evaluation of steady-state impact and residual user value within a single experiment. Empirical results show improved precision in estimating LTE and $ΔERLV$ and identify scenarios in which relying on either short-term or long-term metrics alone would lead to incorrect product decisions.

### 🤖 AI 总结

**一句话总结**：In streaming platforms churn is extremely costly, yet A/B tests are typically evaluated using outcomes observed within a limited experimental horizon. Even when both short- and predicted long-term eng...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Efficient, Multi-Cohort, Inference, Long-Term, Effects, Lifetime, Value, Testing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20777v1) | [下载PDF](https://arxiv.org/pdf/2604.20777v1.pdf)

---

## [25. Lifecycle-Aware Federated Continual Learning in Mobile Autonomous Systems](https://arxiv.org/abs/2604.20745v1)

**作者**：Beining Wu, Jun Huang  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-04-22

### 📄 论文摘要

Federated continual learning (FCL) allows distributed autonomous fleets to adapt collaboratively to evolving terrain types across extended mission lifecycles. However, current approaches face several key challenges: 1) they use uniform protection strategies that do not account for the varying sensitivities to forgetting on different network layers; 2) they focus primarily on preventing forgetting during training, without addressing the long-term effects of cumulative drift; and 3) they often depend on idealized simulations that fail to capture the real-world heterogeneity present in distributed fleets. In this paper, we propose a lifecycle-aware dual-timescale FCL framework that incorporates training-time (pre-forgetting) prevention and (post-forgetting) recovery. Under this framework, we design a layer-selective rehearsal strategy that mitigates immediate forgetting during local training, and a rapid knowledge recovery strategy that restores degraded models after long-term cumulative drift. We present a theoretical analysis that characterizes heterogeneous forgetting dynamics and establishes the inevitability of long-term degradation. Our experimental results show that this framework achieves up to 8.3\% mIoU improvement over the strongest federated baseline and up to 31.7\% over conventional fine-tuning. We also deploy the FCL framework on a real-world rover testbed to assess system-level robustness under realistic constraints; the testing results further confirm the effectiveness of our FCL design.

### 🤖 AI 总结

**一句话总结**：Federated continual learning (FCL) allows distributed autonomous fleets to adapt collaboratively to evolving terrain types across extended mission lifecycles. However, current approaches face several ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Lifecycle-Aware, Federated, Continual, Learning, Mobile, Autonomous, Systems, FCL

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20745v1) | [下载PDF](https://arxiv.org/pdf/2604.20745v1.pdf)

---

## [26. F\textsuperscript{2}LP-AP: Fast \& Flexible Label Propagation with Adaptive Propagation Kernel](https://arxiv.org/abs/2604.20736v1)

**作者**：Yutong Shen, Ruizhe Xia, Jingyi Liu 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-22

### 📄 论文摘要

Semi-supervised node classification is a foundational task in graph machine learning, yet state-of-the-art Graph Neural Networks (GNNs) are hindered by significant computational overhead and reliance on strong homophily assumptions. Traditional GNNs require expensive iterative training and multi-layer message passing, while existing training-free methods, such as Label Propagation, lack adaptability to heterophilo\-us graph structures. This paper presents \textbf{F$^2$LP-AP} (Fast and Flexible Label Propagation with Adaptive Propagation Kernel), a training-free, computationally efficient framework that adapts to local graph topology. Our method constructs robust class prototypes via the geometric median and dynamically adjusts propagation parameters based on the Local Clustering Coefficient (LCC), enabling effective modeling of both homophilous and heterophilous graphs without gradient-based training. Extensive experiments across diverse benchmark datasets demonstrate that \textbf{F$^2$LP-AP} achieves competitive or superior accuracy compared to trained GNNs, while significantly outperforming existing baselines in computational efficiency.

### 🤖 AI 总结

**一句话总结**：Semi-supervised node classification is a foundational task in graph machine learning, yet state-of-the-art Graph Neural Networks (GNNs) are hindered by significant computational overhead and reliance ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：textsuperscript, LP-AP, Fast, Flexible, Label, Propagation, Adaptive, Kernel

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20736v1) | [下载PDF](https://arxiv.org/pdf/2604.20736v1.pdf)

---

## [27. Fast Bayesian equipment condition monitoring via simulation based inference: applications to heat exchanger health](https://arxiv.org/abs/2604.20735v1)

**作者**：Peter Collett, Alexander Johannes Stasik, Simone Casolo 等 4 位作者  
**分类**：cs.LG, eess.SY, physics.comp-ph  
**发布时间**：2026-04-22

### 📄 论文摘要

Accurate condition monitoring of industrial equipment requires inferring latent degradation parameters from indirect sensor measurements under uncertainty. While traditional Bayesian methods like Markov Chain Monte Carlo (MCMC) provide rigorous uncertainty quantification, their heavy computational bottlenecks render them impractical for real-time process control. To overcome this limitation, we propose an AI-driven framework utilizing Simulation-Based Inference (SBI) powered by amortized neural posterior estimation to diagnose complex failure modes in heat exchangers. By training neural density estimators on a simulated dataset, our approach learns a direct, likelihood-free mapping from thermal-fluid observations to the full posterior distribution of degradation parameters. We benchmark this framework against an MCMC baseline across various synthetic fouling and leakage scenarios, including challenging low-probability, sparse-event failures. The results show that SBI achieves comparable diagnostic accuracy and reliable uncertainty quantification, while accelerating inference time by a factor of82$\times$ compared to traditional sampling. The amortized nature of the neural network enables near-instantaneous inference, establishing SBI as a highly scalable, real-time alternative for probabilistic fault diagnosis and digital twin realization in complex engineering systems.

### 🤖 AI 总结

**一句话总结**：Accurate condition monitoring of industrial equipment requires inferring latent degradation parameters from indirect sensor measurements under uncertainty. While traditional Bayesian methods like Mark...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Fast, Bayesian, equipment, condition, monitoring, via, simulation, inference

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20735v1) | [下载PDF](https://arxiv.org/pdf/2604.20735v1.pdf)

---

## [28. Near-Future Policy Optimization](https://arxiv.org/abs/2604.20733v1)

**作者**：Chuanyu Qin, Chenxu Yang, Qingyi Si 等 9 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-22

### 📄 论文摘要

Reinforcement learning with verifiable rewards (RLVR) has become a core post-training recipe. Introducing suitable off-policy trajectories into on-policy exploration accelerates RLVR convergence and raises the performance ceiling, yet finding a source of such trajectories remains the key challenge. Existing mixed-policy methods either import trajectories from external teachers (high-quality but distributionally far) or replay past training trajectories (close but capped in quality), and neither simultaneously satisfies the strong enough (higher $Q$ , more new knowledge to learn) and close enough (lower $V$ , more readily absorbed) conditions required to maximize the effective learning signal $\mathcal{S} = Q/V$. We propose \textbf{N}ear-Future \textbf{P}olicy \textbf{O}ptimization (\textbf{NPO}), a simple mixed-policy scheme that learns from a policy's own near-future self: a later checkpoint from the same training run is a natural source of auxiliary trajectories that is both stronger than the current policy and closer than any external source, directly balancing trajectory quality against variance cost. We validate NPO through two manual interventions, early-stage bootstrapping and late-stage plateau breakthrough, and further propose \textbf{AutoNPO},an adaptive variant that automatically triggers interventions from online training signals and selects the guide checkpoint that maximizes $S$. On Qwen3-VL-8B-Instruct with GRPO, NPO improves average performance from 57.88 to 62.84, and AutoNPO pushes it to 63.15, raising the final performance ceiling while accelerating convergence.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning with verifiable rewards (RLVR) has become a core post-training recipe. Introducing suitable off-policy trajectories into on-policy exploration accelerates RLVR convergence and r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Near-Future, Policy, Optimization, Reinforcement, learning, verifiable, rewards, RLVR

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20733v1) | [下载PDF](https://arxiv.org/pdf/2604.20733v1.pdf)

---

## [29. Supplement Generation Training for Enhancing Agentic Task Performance](https://arxiv.org/abs/2604.20727v1)

**作者**：Young Min Cho, Daniele Bonadiman, Divya Bhargavi 等 11 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-22

### 📄 论文摘要

Training large foundation models for agentic tasks is increasingly impractical due to the high computational costs, long iteration cycles, and rapid obsolescence as new models are continuously released. Instead of post-training massive models for every new task or domain, we propose Supplement Generation Training (SGT), a more efficient and sustainable strategy. SGT trains a smaller LLM to generate useful supplemental text that, when appended to the original input, helps the larger LLM solve the task more effectively. These lightweight models can dynamically adapt supplements to task requirements, improving performance without modifying the underlying large models. This approach decouples task-specific optimization from large foundation models and enables more flexible, cost-effective deployment of LLM-powered agents in real-world applications.

### 🤖 AI 总结

**一句话总结**：Training large foundation models for agentic tasks is increasingly impractical due to the high computational costs, long iteration cycles, and rapid obsolescence as new models are continuously release...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Supplement, Generation, Training, Enhancing, Agentic, Task, Performance, large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20727v1) | [下载PDF](https://arxiv.org/pdf/2604.20727v1.pdf)

---

## [30. COMPASS: COntinual Multilingual PEFT with Adaptive Semantic Sampling](https://arxiv.org/abs/2604.20720v1)

**作者**：Noah Flynn  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-04-22

### 📄 论文摘要

Large language models (LLMs) often exhibit performance disparities across languages, with naive multilingual fine-tuning frequently degrading performance due to negative cross-lingual interference. To address this, we introduce COMPASS (COntinual Multilingual PEFT with Adaptive Semantic Sampling), a novel data-centric framework for adapting LLMs to target languages. COMPASS leverages parameter-efficient fine-tuning (PEFT) by training lightweight, language-specific adapters on a judiciously selected subset of auxiliary multilingual data. The core of our method is a distribution-aware sampling strategy that uses multilingual embeddings and clustering to identify semantic gaps between existing training data and a target usage distribution. By prioritizing auxiliary data from under-represented semantic clusters, COMPASS maximizes positive cross-lingual transfer while minimizing interference. We extend this into a continual learning framework, COMPASS-ECDA, which monitors for data distribution shifts in production and dynamically updates adapters to prevent model staleness, balancing adaptation to new data with the preservation of existing knowledge. Across three different model architectures (Phi-4-Mini, Llama-3.1-8B, and Qwen2.5-7B) and multiple challenging multilingual benchmarks (Global-MMLU, MMLU-ProX), including unseen long-context tasks (OneRuler), we demonstrate that COMPASS consistently outperforms baseline methods guided by linguistic similarity, providing an effective, efficient, and sustainable solution for developing and maintaining high-performing multilingual models in dynamic environments.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) often exhibit performance disparities across languages, with naive multilingual fine-tuning frequently degrading performance due to negative cross-lingual interference. To...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：COMPASS, COntinual, Multilingual, PEFT, Adaptive, Semantic, Sampling, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.20720v1) | [下载PDF](https://arxiv.org/pdf/2604.20720v1.pdf)

---

