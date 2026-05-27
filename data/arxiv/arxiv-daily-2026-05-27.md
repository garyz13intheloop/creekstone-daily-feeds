# arXiv AI 论文日报 | 2026-05-27

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (8 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.CL](#csCL) (9 篇)

---

## cs.AI

## [1. MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation](https://arxiv.org/abs/2605.27366v1)

**作者**：Huawei Lin, Peng Li, Jie Song 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.LG, cs.MA  
**发布时间**：2026-05-26

### 📄 论文摘要

Large language model (LLM) agents rely on reusable skills to solve complex tasks. However, existing skill creation approaches treat skills as isolated and static artifacts, limiting their reusability, reliability, and long-term improvement. We propose MUSE-Autoskill Agent (Memory-Utilizing Skill Evolution), a skill-centric agent framework that lets agents continuously improve their task-solving capability by creating, reusing, and refining skills under a unified lifecycle (creation, memory, management, evaluation, and refinement). Our framework enables agents to create skills on demand, store and reuse them across tasks, organize and select them efficiently, and evaluate them through unit tests and runtime feedback for continuous refinement. We further introduce skill-level memory that accumulates experience for each skill across tasks, enabling more effective reuse and adaptation over time. Experiments on SkillsBench provide initial evidence that lifecycle-managed skills can improve task success, efficiency, reuse, and cross-agent transfer, highlighting the importance of treating skills as long-lived, experience-aware, and testable assets.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM) agents rely on reusable skills to solve complex tasks. However, existing skill creation approaches treat skills as isolated and static artifacts, limiting their reusability,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, MUSE-Autoskill, Self-Evolving, via, Skill, Creation, Memory, Management

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27366v1) | [下载PDF](https://arxiv.org/pdf/2605.27366v1.pdf)

---

## [2. Natural Language Query to Configuration for Retrieval Agents](https://arxiv.org/abs/2605.27361v1)

**作者**：Melissa Z. Pan, Negar Arabzadeh, Mathew Jacob 等 6 位作者  
**分类**：cs.AI, eess.SY  
**发布时间**：2026-05-26

### 📄 论文摘要

Modern retrieval agents expose many configuration choices -- LLM, retriever, number of documents, number of hops, and synthesis strategy -- each shaping both answer quality and serving cost. Today, these pipelines are typically hand-tuned once per workload, leaving substantial per-query optimization untapped. We formulate the problem: given a natural-language query and either an accuracy or a budget target, select from a predefined pipeline catalog the configuration that minimizes cost or maximizes accuracy at inference time. We propose **BRANE**, which uses an LLM to convert each query into workload-specific characteristics, then trains a lightweight per-configuration predictor that estimates whether the pipeline will answer the query correctly. At inference time, **BRANE** selects the configuration that maximizes predicted correctness penalized by cost, exposing a tunable cost-quality tradeoff without retraining. Across MuSiQue, BrowseComp-Plus, and FinanceBench, **BRANE** consistently pushes the cost-quality Pareto frontier, matches the best fixed configuration's accuracy at up to 89% lower cost, and outperforms LLM-routing, rule-based, and fine-tuned Qwen3-4B baselines. These results show that per-query configuration of the full retrieval pipeline is a practical alternative to static workload-level tuning.

### 🤖 AI 总结

**一句话总结**：Modern retrieval agents expose many configuration choices -- LLM, retriever, number of documents, number of hops, and synthesis strategy -- each shaping both answer quality and serving cost. Today, th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Natural, Language, Query, Configuration, Retrieval, Modern, expose

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27361v1) | [下载PDF](https://arxiv.org/pdf/2605.27361v1.pdf)

---

## [3. Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases](https://arxiv.org/abs/2605.27355v1)

**作者**：Dongyoon Hahm, Dylan Hadfield-Menell, Kimin Lee  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-05-26

### 📄 论文摘要

Reinforcement Learning from Human Feedback (RLHF) is the standard method to align Large Language Models (LLMs) with human preferences. In this work, we introduce alignment tampering, a potential vulnerability where the LLM undergoing alignment influences the preference dataset, causing RLHF to amplify undesired behaviors. This arises from core limitations of RLHF: (1) preference datasets are constructed from the LLM's own outputs, allowing it to influence them, and (2) pairwise comparisons only indicate which response is better, not why. These limitations can be exploited to cause alignment tampering. For example, if an LLM generates biased responses with higher quality, annotators will prefer them based on quality. However, preference labels do not distinguish quality from bias, and the reward model inherits this limitation. Optimizing such rewards through reinforcement learning or best-of-N sampling can amplify misaligned biases. Our experiments demonstrate amplification across diverse biases: from keyword bias to propaganda (e.g., sexism), brand promotion, and instrumental goal-seeking. Mitigation remains challenging, as existing techniques for robust RLHF fail to fully resolve alignment tampering without sacrificing response quality. These findings reveal structural vulnerabilities of current RLHF and emphasize the need to prevent this vulnerability. Project page: https://alignment-tampering.github.io/

### 🤖 AI 总结

**一句话总结**：Reinforcement Learning from Human Feedback (RLHF) is the standard method to align Large Language Models (LLMs) with human preferences. In this work, we introduce alignment tampering, a potential vulne...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Alignment, Tampering, How, Reinforcement, Learning, Human, Feedback, Exploited

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27355v1) | [下载PDF](https://arxiv.org/pdf/2605.27355v1.pdf)

---

## [4. 2-ASP(Q) programs with weak constraints: Complexity and efficient implementation](https://arxiv.org/abs/2605.27338v1)

**作者**：Andrea Cuteri, Giuseppe Mazzotta, Francesco Ricca  
**分类**：cs.AI, cs.CC, cs.CL, cs.LO  
**发布时间**：2026-05-26

### 📄 论文摘要

ASP(Q) extends Answer Set Programming (ASP) with Quantifiers over answer sets. In this paper we focus on the class of ASP(Q) programs with two quantifiers and weak constraints, denoted as 2-ASP(Q)^w. 2-ASP(Q)^w is a practically relevant fragment of ASP(Q) that is expressive enough to capture optimization problems up to the class Delta_3^P. On the theoretical side, we provide a complete complexity characterization of the main computational tasks for 2-ASP(Q)^w programs, including tight completeness results and the analysis of nontrivial cases that have not been addressed in previous works. On the practical side, we introduce novel strategies for computing (optimal) quantified answer sets in the Casper system, that rely on a Counterexample-Guided Abstraction Refinement (CEGAR) technique tailored to ASP(Q). An experimental evaluation on hard benchmarks from different application domains shows that the proposed techniques are effective in practice.

### 🤖 AI 总结

**一句话总结**：ASP(Q) extends Answer Set Programming (ASP) with Quantifiers over answer sets. In this paper we focus on the class of ASP(Q) programs with two quantifiers and weak constraints, denoted as 2-ASP(Q)^w. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：2-ASP, programs, weak, constraints, Complexity, efficient, implementation, ASP

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27338v1) | [下载PDF](https://arxiv.org/pdf/2605.27338v1.pdf)

---

## [5. Maat: The Agentic Legal Research Assistant for Competition Protection](https://arxiv.org/abs/2605.27331v1)

**作者**：Basant Mounir, Farida Madkour, Amira Abdelaziz 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-26

### 📄 论文摘要

Competition law experts conducting legal research must review extensive volumes of cases, decisions, and judicial reports to identify precedents and assess key elements in competition and merger cases. Although general research assistants such as Claude and ChatGPT and legal assistants such as SaulLM-7B and LegalGPT are increasingly used to assist legal research, they remain inadequate for competition law analysis: they lack specialized domain expertise, provide insufficient official citations, or hallucinate competition law cases. We propose Maat, a ReAct agent that orchestrates tools corresponding to different tasks of the research process. Designed iteratively with competition law experts, Maat grounds cases and findings in official sources using RAG for reliability, provides rich in-line citations, falls back to web search when database coverage is insufficient, and prompts the user for clarification when queries are ambiguous. Maat significantly outperforms all baseline assistants on case-specific tasks and performs within range of the top baseline on theoretical question tasks. The dataset used is available on GitHub.

### 🤖 AI 总结

**一句话总结**：Competition law experts conducting legal research must review extensive volumes of cases, decisions, and judicial reports to identify precedents and assess key elements in competition and merger cases...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Maat, Agentic, Legal, Research, Assistant, Competition, Protection, law

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27331v1) | [下载PDF](https://arxiv.org/pdf/2605.27331v1.pdf)

---

## [6. Modeling Agentic Technical Debt and Stochastic Tax: A Standalone Framework for Measurement, Simulation, and Dashboarding](https://arxiv.org/abs/2605.27320v1)

**作者**：Muhammad Zia Hydari, Raja Iqbal, Narayan Ramasubbu  
**分类**：cs.AI, cs.CY, econ.GN  
**发布时间**：2026-05-26

### 📄 论文摘要

Agentic AI systems combine probabilistic reasoning with delegated action through tools, context, memory, orchestration, and external workflow integration. This note develops a formal and managerially usable model that distinguishes Agentic Technical Debt from Stochastic Tax. Agentic Technical Debt is a stock of accumulated design and governance liability. Stochastic Tax is a recurring flow of operating burden that arises when stochastic agents are used in business workflows. The two constructs are related, but they are not the same: debt can amplify the tax, while the tax can remain positive even when debt is minimized. The note starts from a compact dashboard expression, expands it into a fuller structural model, defines all variables and parameters, shows how each cost category can be estimated from operational data, and illustrates the framework with an accounts-payable simulation and companion spreadsheet.

### 🤖 AI 总结

**一句话总结**：Agentic AI systems combine probabilistic reasoning with delegated action through tools, context, memory, orchestration, and external workflow integration. This note develops a formal and managerially ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Modeling, Agentic, Technical, Debt, Stochastic, Tax, Standalone, Framework

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27320v1) | [下载PDF](https://arxiv.org/pdf/2605.27320v1.pdf)

---

## cs.CL

## [7. FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents](https://arxiv.org/abs/2605.27333v1)

**作者**：Haoxuan Jia, Yang Liu, Bin Chong 等 13 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-26

### 📄 论文摘要

Finance LLM agents must simultaneously block prompt-induced unauthorized actions and approve legitimate multi-step business workflows. However, boundary filters often miss irreversible mid-trajectory tool calls, while post-hoc LLM judges perform auditing only after termination -- too late for intervention and at a computational cost that scales linearly with trace length. We present FinHarness, an inline safety harness that wraps a finance agent end-to-end with three components: a Query Monitor that fuses single-turn intent with cross-turn drift, a Tool Monitor that evaluates each prospective tool call, and a Cascade module that integrates per-step risk and adaptively routes verification between a lightweight and an advanced-tier LLM judge. Fired risk factors are re-injected into the agent input as ex-ante evidence, enabling the agent to refuse, re-plan, or approve on its own. On FinVault, routed FinHarness cuts ASR from 38.3% to 15.0% while largely preserving benign approval ($41.1\% \to 39.3\%$), and uses $4.7\times$ fewer advanced-judge calls than an always-advanced ablation.

### 🤖 AI 总结

**一句话总结**：Finance LLM agents must simultaneously block prompt-induced unauthorized actions and approve legitimate multi-step business workflows. However, boundary filters often miss irreversible mid-trajectory ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, LLM, FinHarness, Inline, Lifecycle, Safety, Harness, Finance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27333v1) | [下载PDF](https://arxiv.org/pdf/2605.27333v1.pdf)

---

## [8. Semantic Gradients Interactions in SSD: A Case Study in Racial Identity and Hate Speech](https://arxiv.org/abs/2605.27322v1)

**作者**：Felix Ostrowicki, Hubert Plisiecki  
**分类**：cs.CL  
**发布时间**：2026-05-26

### 📄 论文摘要

We introduce interaction SSD, an extension of Supervised Semantic Differential that models how semantic meaning varies across moderators such as groups, traits, or conditions making this variation testable and interpretable. The method estimates a main semantic gradient, an interaction gradient, and conditional gradients, all interpretable through standard SSD tools. We illustrate it on the UC Berkeley Measuring Hate Speech corpus, testing whether annotator racial identity moderates hate-speech judgments of comments targeting people of color. The interaction model detects a significant moderation effect: the shared gradient contrasts dehumanizing hostility with counter-speech, while the interaction gradient reveals smaller group-linked differences in which semantic cues predict hate-speech ratings. Interaction SSD makes moderated meaning-outcome relationships statistically testable and interpretable.

### 🤖 AI 总结

**一句话总结**：We introduce interaction SSD, an extension of Supervised Semantic Differential that models how semantic meaning varies across moderators such as groups, traits, or conditions making this variation tes...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Semantic, Gradients, Interactions, SSD, Case, Study, Racial, Identity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27322v1) | [下载PDF](https://arxiv.org/pdf/2605.27322v1.pdf)

---

## [9. Real Images, Worse Judgments: Evaluating Vision-Language Models on Concreteness and Imagery](https://arxiv.org/abs/2605.27315v1)

**作者**：Yifan Jiang, Ruoxi Ning, Sheng Yao 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-26

### 📄 论文摘要

Visual inputs are often assumed to improve language understanding in multimodal models. We examine this assumption by asking whether vision-language models (VLMs) can distinguish useful visual evidence from incidental image context in lexical judgments. We use human concreteness and imagery ratings because they span words with varying expected visual relevance, from abstract and low-imagery words to concrete and high-imagery words. We find that real-image contexts do not yield consistent gains and often hurt alignment with human ratings, most sharply when visual evidence is least relevant. Through probing and canonical correlation analysis, complemented by an attribution case study, we find that real-image contexts are associated with representational shifts and greater sensitivity to spurious visual cues, coinciding with weaker recoverability of the targeted lexical properties. We further show that instructing models to focus solely on textual content at inference time can reduce this degradation, with the clearest gains on these vulnerable subsets. Our findings suggest that current instruction-tuned VLMs need better calibration of when visual context should inform lexical judgments.

### 🤖 AI 总结

**一句话总结**：Visual inputs are often assumed to improve language understanding in multimodal models. We examine this assumption by asking whether vision-language models (VLMs) can distinguish useful visual evidenc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Real, Images, Worse, Judgments, Evaluating, Vision-Language, Models, Concreteness

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27315v1) | [下载PDF](https://arxiv.org/pdf/2605.27315v1.pdf)

---

## [10. When Does Demographic Information Help? Data and Modeling Regimes for Perspective-Aware Hate Speech Detection](https://arxiv.org/abs/2605.27313v1)

**作者**：Weibin Cai, Reza Zafarani  
**分类**：cs.CL  
**发布时间**：2026-05-26

### 📄 论文摘要

Demographic information is often used to model annotator perspectives in subjective tasks such as hate speech detection, but its benefit is inconsistent: it improves performance in some settings and behaves as noise in others. This paper asks when demographic features help. We analyze demographic gain as a function of both data split properties and modeling frameworks. For data splits, we measure annotator disagreement, namely how often annotators assign different labels to the same example, along with training size and train-test demographic coverage. We find that demographic gains concentrate in regimes with low training disagreement, high test disagreement, fine-grained ambiguity measurement, sufficient training data, and greater demographic overlap. Motivated by these regimes, we introduce a gated demographic residual model that treats demographics as a selective adjustment to text-only predictions. Experiments on MHS and POPQUORN show that this design is effective, especially on high disagreement or low confidence examples. Overall, our results suggest that demographics should not be assumed useful by default; their value depends jointly on the data regime and the modeling framework.

### 🤖 AI 总结

**一句话总结**：Demographic information is often used to model annotator perspectives in subjective tasks such as hate speech detection, but its benefit is inconsistent: it improves performance in some settings and b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Does, Demographic, Information, Help?, Data, Modeling, Regimes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27313v1) | [下载PDF](https://arxiv.org/pdf/2605.27313v1.pdf)

---

## [11. Chartographer: Counterfactual Chart Generation for Evaluating Vision-Language Models](https://arxiv.org/abs/2605.27311v1)

**作者**：Yifan Jiang, Dae Yon Hwang, Jesse C. Cresswell 等 4 位作者  
**分类**：cs.CL, cs.CV  
**发布时间**：2026-05-26

### 📄 论文摘要

Chart question-answering (QA) benchmarks aim to pose questions that require visual reasoning to correctly answer, but models can often reach solutions through shortcuts or prior familiarity with a chart based on their own background knowledge. To strictly evaluate visual reasoning, we propose counterfactual charts where the chart-question task remains fixed, but underlying chart and the corresponding answer are varied. We introduce Chartographer, a framework to reverse engineer charts into executable code, validate reconstruction fidelity, generate seed-controlled counterfactual variants, and derive new answers from executable QA logic. We apply this framework to existing chart QA datasets and evaluate proprietary and open-source vision-language models (VLMs), measuring variation sensitivity and generalizability. Counterfactual charts reveal failures hidden by single-chart performance: VLMs often fail to generalize after answering the original chart correctly. We find failures are most prevalent when updated charts require novel visual reasoning pathways.

### 🤖 AI 总结

**一句话总结**：Chart question-answering (QA) benchmarks aim to pose questions that require visual reasoning to correctly answer, but models can often reach solutions through shortcuts or prior familiarity with a cha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Chartographer, Counterfactual, Chart, Generation, Evaluating, Vision-Language, Models, question-answering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27311v1) | [下载PDF](https://arxiv.org/pdf/2605.27311v1.pdf)

---

## [12. Self-Ensembling Vision-Language Models for Chart Data Extraction](https://arxiv.org/abs/2605.27298v1)

**作者**：Thomas Berkane, Qianyi Wang, Maimuna S. Majumder  
**分类**：cs.CL  
**发布时间**：2026-05-26

### 📄 论文摘要

Charts effectively convey quantitative information, but the underlying data are often locked in image form, hindering reuse and analysis. Manually digitizing charts is time-consuming and error-prone, motivating automatic chart-to-table extraction. Recent approaches use specialized vision-language models (VLMs), yet performance still lags on charts with many datapoints or substantial stylistic variation. We propose a VLM self-ensembling method that repeatedly samples multiple tabular outputs from the same VLM for a fixed chart image and aggregates them at the level of individual table cells. We align candidate tables and take per-cell medians over numerical values to produce a more accurate consensus table. Our method also includes convergence detection to stop sampling once the aggregated table stabilizes, and uncertainty estimation based on dispersion across samples to help users assess extraction reliability. Because existing chart extraction benchmarks contain relatively simple plots with limited room for improvement, we introduce WB-ChartExtract, a new benchmark built from World Bank data with more complex and stylistically diverse charts; on average, its charts contain 7 times more datapoints than those in the ChartQA benchmark. Across both ChartQA and WB-ChartExtract, our approach improves extraction accuracy over single-pass VLM outputs, yielding up to 23% relative improvement on WB-ChartExtract after ensembling. More broadly, our method helps unlock tabular data previously siloed in chart images, enabling downstream analysis and reuse.

### 🤖 AI 总结

**一句话总结**：Charts effectively convey quantitative information, but the underlying data are often locked in image form, hindering reuse and analysis. Manually digitizing charts is time-consuming and error-prone, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Self-Ensembling, Vision-Language, Models, Chart, Data, Extraction, Charts, effectively

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27298v1) | [下载PDF](https://arxiv.org/pdf/2605.27298v1.pdf)

---

## [13. Probing Cultural Awareness in LLMs: A Case Study of Cross-Culture Aesthetic Stylistics](https://arxiv.org/abs/2605.27296v1)

**作者**：Jiashuo Wang, Fenggang Yu, Jian Wang 等 9 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-26

### 📄 论文摘要

Large Language Models (LLMs) are increasingly deployed in diverse cultural contexts, yet their ability to master aesthetic stylistics, i.e., the strategic use of language to evoke cultural resonance, remains underexplored. We curate C4STYLI, a benchmark of highly stylized translated movie titles and advertising slogans from Hong Kong and the Chinese Mainland, to evaluate LLMs via the lens of behavioral recognition and productive competence. Extensive evaluations show that LLMs differ from humans in stylistic recognition, and this recognition ability varies across text domains. In addition, stylistic recognition and generation performance in LLMs are not consistently aligned. To further examine whether LLMs genuinely capture stylistic information in stylistic recognition, we conduct structural ablation with logistic regression probes. We find that, in the Hong Kong setting, stylistic recognition in LLMs relies primarily on surface-level linguistic information rather than stylistic structure. This suggests limited sensitivity to Hong Kong-specific stylistic structure.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) are increasingly deployed in diverse cultural contexts, yet their ability to master aesthetic stylistics, i.e., the strategic use of language to evoke cultural resonance, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, of, Probing, Cultural, Awareness, Case, Study, Cross-Culture

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27296v1) | [下载PDF](https://arxiv.org/pdf/2605.27296v1.pdf)

---

## [14. Separating Semantic Competition from Context Length in RAG Reading](https://arxiv.org/abs/2605.27294v1)

**作者**：Vyzantinos Repantis, Ameya Gawde, Harshvardhan Singh 等 7 位作者  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-05-26

### 📄 论文摘要

Retrieval-augmented generation (RAG) systems can respond incorrectly even when the correct passage was retrieved. The model must still read the retrieved passages and identify which one contains the answer among others that look relevant. This passage-reading model is called the reader. Does it fail simply because the context is longer or because the other passages genuinely compete with the correct one? We introduce and demonstrate a matched-control protocol for RAG reading: we keep the number and length of passages fixed, but replace hard competitors with less competitive real passages. We apply this control across two compact open models on SQuAD. This replacement partially restores performance, with the strongest effects on F1 and answer inclusion. For Phi-2, this recovers +6.0 EM points, +7.0 answer-inclusion points, and +0.057 F1. For Qwen2.5-1.5B, it recovers +4.5 EM points, +9.0 answer-inclusion points, and +0.068 F1. To track how performance changes as competitors accumulate, we also report retention curves and summarize them with a right-censored half-life when the curves do not cross half-retention. Together, these results show the protocol isolates a competition effect distinct from context length, though the effect is clearer for F1 and answer inclusion than for exact match, and also varies with snippet length.

### 🤖 AI 总结

**一句话总结**：Retrieval-augmented generation (RAG) systems can respond incorrectly even when the correct passage was retrieved. The model must still read the retrieved passages and identify which one contains the a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RAG, Separating, Semantic, Competition, Context, Length, Reading, Retrieval-augmented

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27294v1) | [下载PDF](https://arxiv.org/pdf/2605.27294v1.pdf)

---

## [15. It's Not Always Sycophancy: Measuring LLM Conformity as a Function of Epistemic Uncertainty](https://arxiv.org/abs/2605.27288v1)

**作者**：Kevin H. Guo, Chao Yan, Avinash Baidya 等 8 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-05-26

### 📄 论文摘要

Large language models (LLMs) are known to abandon their initial stance to conform to user pushback. While prior research largely attributes this behavior to sycophancy learned during reinforcement learning from human feedback, we hypothesize that conformity is also driven by a model's epistemic uncertainty at inference time. In this paper, we introduce MUSE, a two-stage evaluation framework to disentangle the mechanisms driving LLM conformity. Specifically, MUSE maps a model's epistemic uncertainty in responding to a query against its likelihood to yield to user pushback in a subsequent turn. We demonstrate that the mechanisms driving conformity extend beyond sycophancy alone. Specifically, we characterize two distinct factors that jointly drive conformity: sycophantic conformity, where a model aligns with user pushback even with absolute certainty in its initial response, and uncertainty-driven conformity, where a model's likelihood for conformity increases alongside its uncertainty. Furthermore, we conduct ablation studies to demonstrate that both sycophantic conformity and uncertainty-driven conformity grow with 1) the LLM's perceived expertise of the user and 2) the plausibility of the user's suggestions. More broadly, MUSE informs more targeted intervention strategies by distinguishing alignment-induced sycophancy and training-corpora-driven uncertainty.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are known to abandon their initial stance to conform to user pushback. While prior research largely attributes this behavior to sycophancy learned during reinforcement lea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, as, It's, Not, Always, Sycophancy, Measuring, Conformity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27288v1) | [下载PDF](https://arxiv.org/pdf/2605.27288v1.pdf)

---

## cs.CV

## [16. G3T Up! Gravity Aligned Coordinate Frames Simplify Pointmap Processing](https://arxiv.org/abs/2605.27372v1)

**作者**：Bharath Raj Nagoor Kani, Noah Snavely  
**分类**：cs.CV  
**发布时间**：2026-05-26

### 📄 论文摘要

Modern feed-forward 3D reconstruction methods like VGGT predict pixel-aligned pointmaps in camera-centric coordinate frames. However, this choice of coordinate frame is not always optimal. We propose instead to predict pointmaps in upright, gravity-aligned frames that exploit strong structural cues present in many real-world scenes. Unlike camera-centric frames, gravity-aligned frames share a common vertical axis across viewpoints, reducing the rotational degrees of freedom needed to relate pointmaps to one another. To this end, we introduce the Gravity Grounded Geometry Transformer (G3T), fine-tuned from existing models on gravity-aligned 3D data. G3T produces highly accurate gravity-aware predictions, including upright pointmaps and camera-to-gravity poses. We further introduce G3T-Long, a submap-based incremental 3D reconstruction pipeline that leverages the reduced rotational degrees of freedom afforded by upright frames to achieve significantly improved reconstruction accuracy.

### 🤖 AI 总结

**一句话总结**：Modern feed-forward 3D reconstruction methods like VGGT predict pixel-aligned pointmaps in camera-centric coordinate frames. However, this choice of coordinate frame is not always optimal. We propose ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：G3T, Up!, Gravity, Aligned, Coordinate, Frames, Simplify, Pointmap

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27372v1) | [下载PDF](https://arxiv.org/pdf/2605.27372v1.pdf)

---

## [17. SpatialBench: Is Your Spatial Foundation Model an All-Round Player?](https://arxiv.org/abs/2605.27367v1)

**作者**：Haosong Peng, Hao Li, Jiaqi Chen 等 13 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-26

### 📄 论文摘要

While spatial foundation models have demonstrated impressive performance on standard datasets, a critical question remains: are they truly all-round players capable of generalizing robustly across diverse downstream tasks, arbitrary viewpoints, shifting scene domains, varying input densities, and specific hardware constraints? Answering this overarching question requires a holistic assessment, yet current models are mainly evaluated on specific domains for which they were specifically designed or trained. Such evaluations are intrinsically limited by narrow paradigm coverage, limited scene domains, and arbitrary frame sampling, making it fundamentally difficult to assess their true generalization capabilities. To address this gap, we present SpatialBench, a cross-paradigm, domain-diverse benchmark for spatial foundation models with deterministic sampling. SpatialBench features unprecedented scale and rigorous deterministic design, comprising 19 datasets and 546 scenes across 5 diverse spatial domains. It comprehensively evaluates 41 models across 6 paradigms on 5 task suites under 4 different input density settings. Our extensive evaluation reveals that current models are not yet all-round players, and uncovers crucial insights for future advancement. Specifically, we demonstrate that full-context attention maximizes accuracy while bounded-memory strategies unlock long-sequence scalability. Moreover, our empirical evaluations in challenging embodied and egocentric tasks demonstrate that strict domain alignment and high data quality are far more critical to performance than simple dataset scaling. Furthermore, to address the largest data gap identified in our analysis, we go beyond evaluation by introducing a large-scale dataset, DA-Next-5M, and a strong baseline model, DA-Next, pushing the boundaries of spatial representation learning.

### 🤖 AI 总结

**一句话总结**：While spatial foundation models have demonstrated impressive performance on standard datasets, a critical question remains: are they truly all-round players capable of generalizing robustly across div...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, SpatialBench, Spatial, Foundation, Model, All-Round, Player?, While

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27367v1) | [下载PDF](https://arxiv.org/pdf/2605.27367v1.pdf)

---

## [18. Feedforward 3D Editing Learns from Semantic-Part Transformation](https://arxiv.org/abs/2605.27351v1)

**作者**：Jiawei Weng, Saining Zhang, Zhenxin Diao 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-26

### 📄 论文摘要

3D editing is a fundamental capability for scalable 3D content creation. While image editing has rapidly evolved toward large-scale feedforward generative paradigms, 3D AI generation remains dominated by training-free editing pipelines. A central challenge of feedforward 3D editing lies in the lack of high-quality paired supervision. Editable 3D assets require simultaneous preservation of geometry, multi-view consistency, structural coherence, and localized edit controllability. Existing 3D editing datasets often rely on independently generated assets, image-mediated reconstruction or narrow edit taxonomies, leading to inaccurate localization, weak preservation, blurred edit boundaries, and limited semantic consistency. In this work, we introduce a new perspective: scalable feedforward 3D editing should be learned from semantic-part transformations. Based on this insight, we propose Pxform, a high-quality 3D editing dataset with over 100K consistent before/after editing pairs across seven edit types. Instead of treating objects as unstructured shapes, our pipeline grounds edits directly in semantic 3D parts. Built upon Pxform, we further propose PartFlow, a feedforward 3D editing network that injects source-aware latent control into pretrained 3D generative priors. PartFlow introduces mask-aware velocity preservation and render-space consistency supervision to jointly improve edit fidelity and source preservation, while requiring no 3D edit mask during inference. Extensive experiments demonstrate that high-quality semantic-part supervision substantially improves scalable 3D editing, enabling PartFlow to achieve state-of-the-art performance on both geometric and appearance editing benchmarks.

### 🤖 AI 总结

**一句话总结**：3D editing is a fundamental capability for scalable 3D content creation. While image editing has rapidly evolved toward large-scale feedforward generative paradigms, 3D AI generation remains dominated...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Feedforward, Editing, Learns, Semantic-Part, Transformation, fundamental, capability

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27351v1) | [下载PDF](https://arxiv.org/pdf/2605.27351v1.pdf)

---

## [19. When Eyes Betray AI: Social Gaze Consistency as a Semantic Cue for AI-Generated Image Detection](https://arxiv.org/abs/2605.27348v1)

**作者**：Kim Jihyeon, Sohee Kim, Soosan Lee 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-26

### 📄 论文摘要

Recent generative models have largely closed the gap on low-level artifacts - pixel fingerprints, frequency anomalies, upsampling traces - particularly in person-centric and partial-edit settings where the manipulated region is small and surrounded by photometrically authentic content. We introduce Social Gaze Consistency, a high-level semantic cue defined as the mutual coherence of gaze direction, head-eye alignment, and pupil placement between interacting individuals, and show that it constitutes a previously underutilized detection axis orthogonal to existing low-level paradigms. We instantiate this insight through three coupled mechanisms: (i) a controlled diagnostic dataset with region-specific perturbations of gaze-consistent imagery, where strict pair-level grouping forecloses generator-fingerprint memorization as an optimization-time shortcut rather than relying on augmentation; (ii) Block-Compositional Caption Supervision, which holds a single 5-block reasoning skeleton invariant across 1,250 macro-combined captions, decoupling reasoning consistency from surface diversity; (iii) Cross-architecture validation showing the same supervision improves a vision-language backbone (FakeVLM) by +3.7 pp on the COCOAI Interaction subset (balanced accuracy 67.8 -> 71.5) and +1.3 pp on the COCOAI Person subset (83.0 -> 84.3), with consistent gains on a vision-only backbone (Effort), evidencing a backbone-agnostic cue. Real- and fake-class recalls rise simultaneously, ruling out a "predict-all-fake" artifact. A four-step mechanistic account - paired-edit shortcut blocking, hard-to-easy difficulty transfer, CLIP prior preservation, and diffusion-family shared spectral weakness in periocular structure - explains why training on a single inpainter (FLUX.1-Fill) transfers to multi-generator suites. We will release the code upon acceptance to facilitate reproducibility.

### 🤖 AI 总结

**一句话总结**：Recent generative models have largely closed the gap on low-level artifacts - pixel fingerprints, frequency anomalies, upsampling traces - particularly in person-centric and partial-edit settings wher...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, When, Eyes, Betray, Social, Gaze, Consistency, Semantic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27348v1) | [下载PDF](https://arxiv.org/pdf/2605.27348v1.pdf)

---

## [20. Towards Controllable Image Generation through Representation-Conditioned Diffusion Models](https://arxiv.org/abs/2605.27343v1)

**作者**：Nithesh Chandher Karthikeyan, Jonas Unger, Gabriel Eilertsen  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-05-26

### 📄 论文摘要

Diffusion models have emerged as powerful tools for high-quality image generation and editing, but guiding these models to produce specific outputs remains a challenge. Conventional approaches rely on conditioning mechanisms, such as text prompts or semantic maps, which require extensively annotated datasets. In this preliminary work, we explore diffusion models conditioned on representations from a pre-trained self-supervised model. The self-conditioning mechanism not only improves the quality of unconditional image generation, but also provides a representation space that can be used to control the generation. We explore this conditioning space by identifying directions of variations, and demonstrate promising properties in terms of smoothness and disentanglement.

### 🤖 AI 总结

**一句话总结**：Diffusion models have emerged as powerful tools for high-quality image generation and editing, but guiding these models to produce specific outputs remains a challenge. Conventional approaches rely on...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Towards, Controllable, Image, Generation, through, Models, have

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27343v1) | [下载PDF](https://arxiv.org/pdf/2605.27343v1.pdf)

---

## [21. PARE: Pruning and Adaptive Routing for Efficient Video Generation](https://arxiv.org/abs/2605.27336v1)

**作者**：Yutong Wang, Yunke Wang, Tianfan Xue 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-26

### 📄 论文摘要

Video Diffusion Transformers (DiTs) generate high-quality videos but demand substantial compute due to wide blocks, deep architectures, and iterative sampling. Recent methods reduce cost by compressing width, depth, or sampling steps, but typically commit to a fixed architecture that cannot adapt to individual inputs or denoising stages. We propose PARE (Pruning and Adaptive Routing for Efficient video generation), which jointly compresses width and depth with structure-aware pruning and input-adaptive routing. For width, we observe that attention heads specialize into spatial and temporal roles, and design importance scoring that accounts for this distinction to prevent motion-critical temporal heads from being pruned prematurely. For depth, we train a lightweight router conditioned on denoising timestep and visual content to dynamically select which blocks to execute at each step, enabling per-input compute adaptation rather than static block removal. A progressive pipeline first recovers width-pruned quality via distillation, then jointly optimizes the student and router to decouple the two learning objectives. Experiments on Wan2.1-14B for both image-to-video and text-to-video generation show that PARE substantially reduces per-step computation while preserving quality across VBench dimensions, and composes with step distillation for further acceleration.

### 🤖 AI 总结

**一句话总结**：Video Diffusion Transformers (DiTs) generate high-quality videos but demand substantial compute due to wide blocks, deep architectures, and iterative sampling. Recent methods reduce cost by compressin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, PARE, Pruning, Adaptive, Routing, Efficient, Video, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27336v1) | [下载PDF](https://arxiv.org/pdf/2605.27336v1.pdf)

---

## [22. PlayClass: Automated Play Behaviour Classification in Poultry](https://arxiv.org/abs/2605.27304v1)

**作者**：Prince Ravi Leow, Neil Scheidwasser, Rebecca Oscarsson 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-26

### 📄 论文摘要

Automated monitoring of animal welfare has largely targeted negative indicators, leaving positive welfare behaviours such as play underexplored. To address this gap, we present PlayClass, a pipeline for play-behaviour classification in poultry from top-down pen video. The pipeline leverages long-duration tracking with SAM 3 via YOLO-guided chunk boundaries to minimise identity errors in point-based prompting, and frozen embeddings from image and video foundation models for play action classification. Although handcrafted motion features from tracked masks alone achieved competitive accuracy, V-JEPA 2.1 consistently outperformed all other backbones across model scales, reaching 77.0 macro-averaged F$_1$ when combined with handcrafted features. Despite this result, the dataset remains challenging due to play sub-types sharing similar kinematic profiles with non-play and inter-bird occlusion. Overall, our work provides encouraging evidence towards automated frameworks for play behaviour classification in poultry.

### 🤖 AI 总结

**一句话总结**：Automated monitoring of animal welfare has largely targeted negative indicators, leaving positive welfare behaviours such as play underexplored. To address this gap, we present PlayClass, a pipeline f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, PlayClass, Automated, Play, Behaviour, Classification, Poultry, monitoring

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27304v1) | [下载PDF](https://arxiv.org/pdf/2605.27304v1.pdf)

---

## [23. Gemini Embedding 2: A Native Multimodal Embedding Model from Gemini](https://arxiv.org/abs/2605.27295v1)

**作者**：Madhuri Shanbhogue, Zhe Li, Shanfeng Zhang 等 89 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-26

### 📄 论文摘要

We introduce Gemini Embedding 2, a native multimodal embedding model that allows embedding video, audio, image, and text modalities in a unified representation space. We leverage the multimodal capabilities of Gemini to produce embeddings for arbitrary combinations of interleaved inputs across all these modalities that generalize well across a wide variety of tasks. Applying large-scale contrastive learning in a multi-task multi-stage training setup, we achieve state-of-the-art performance on key embedding benchmarks including unimodal, cross-modal, and multimodal retrieval spanning a diverse set of tasks. We show that our embedding model demonstrates strong performance (with a score of 62.9 R@1 on MSCOCO, 68.8 NDCG@10 on Vatex, 69.9 on MTEB multilingual and 84.0 on MTEB Code) across a variety of tasks surpassing the performance of specialized models. These unified capabilities make Gemini Embedding 2 a promising candidate for downstream use cases such as RAG, recommendation and search. Furthermore, its robust zero-shot performance across distinct fields - from astronomy and bioscience to fine arts and the culinary arts - establishes it as a highly reliable, out-of-the-box representation even for specialized domains.

### 🤖 AI 总结

**一句话总结**：We introduce Gemini Embedding 2, a native multimodal embedding model that allows embedding video, audio, image, and text modalities in a unified representation space. We leverage the multimodal capabi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Gemini, Embedding, Native, Multimodal, Model, introduce, allows

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27295v1) | [下载PDF](https://arxiv.org/pdf/2605.27295v1.pdf)

---

## cs.LG

## [24. MobileMoE: Scaling On-Device Mixture of Experts](https://arxiv.org/abs/2605.27358v1)

**作者**：Yanbei Chen, Hanxian Huang, Ernie Chang 等 8 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-05-26

### 📄 论文摘要

Mixture-of-Experts (MoE) has become the de facto architecture for hundred-billion-parameter language models, yet its advantages at sub-billion scales for on-device deployment remain largely unexplored. To close this gap, we present MobileMoE, a family of on-device MoE language models with sub-billion active parameters (0.3-0.9B active and 1.3-5.3B total) that establish a new Pareto frontier for on-device LLMs. We first formulate an on-device MoE scaling law that jointly optimizes MoE architecture under mobile memory and compute constraints, identifying an on-device sweet spot - moderate sparsity with fine-grained and shared experts - that is simultaneously memory and compute-optimal. Building on the derived architectures, we train MobileMoE with a four-stage recipe covering pre-training, mid-training, instruction fine-tuning, and quantization-aware training, all on open-source datasets. Across 14 benchmarks, MobileMoE matches or exceeds leading on-device dense LLMs with 2-4$\times$ fewer inference FLOPs, and matches or surpasses the state-of-the-art MoE OLMoE-1B-7B with up to 60% fewer parameters. To bridge the last mile to mobile deployment, we provide the first efficient MoE inference on commodity smartphones with comprehensive on-device profiling. At comparable INT4 weight memory, MobileMoE-S delivers $1.8$-$3.8\times$ faster prefill and $2.2$-$3.4\times$ faster decode than the dense baseline MobileLLM-Pro.

### 🤖 AI 总结

**一句话总结**：Mixture-of-Experts (MoE) has become the de facto architecture for hundred-billion-parameter language models, yet its advantages at sub-billion scales for on-device deployment remain largely unexplored...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, MobileMoE, Scaling, On-Device, Mixture, Experts, Mixture-of-Experts, MoE

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27358v1) | [下载PDF](https://arxiv.org/pdf/2605.27358v1.pdf)

---

## [25. Guiding LLM Post-training Data Engineering with Model Internals from Sparse Autoencoders](https://arxiv.org/abs/2605.27354v1)

**作者**：Yi Jing, Zao Dai, Jinwu Hu 等 7 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-05-26

### 📄 论文摘要

Model internals encode rich information about how a large language model (LLM) processes its training data; however, post-training data engineering largely relies on external signals and ignores rich intrinsic signals lying in model internals. We propose SAERL, a data engineering framework for LLM reinforcement learning (RL). It models three intrinsic data properties: diversity, difficulty, and quality, using model internals extracted with Sparse Autoencoder (SAE), an advanced mechanistic interpretability tool. Each property grounds a concrete data engineering operation: SAE-space clustering with moderate batch mixing for batch diversity control, a difficulty proxy for easy-to-hard curriculum ordering, and a quality probe for data filtering. SAERL improves average accuracy by 3.00% over vanilla GRPO and reaches target accuracy with 20% fewer training steps on Qwen2.5-Math-1.5B, with consistent gains across model scales and RL algorithms. Experiments show that SAE transfers effectively across model families and scales, serving as a lightweight and reusable data engineering tool. These results demonstrate that model internals are a powerful and practical source of signals for post-training data engineering.

### 🤖 AI 总结

**一句话总结**：Model internals encode rich information about how a large language model (LLM) processes its training data; however, post-training data engineering largely relies on external signals and ignores rich ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Guiding, Post-training, Data, Engineering, Model, Internals, Sparse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27354v1) | [下载PDF](https://arxiv.org/pdf/2605.27354v1.pdf)

---

## [26. From Scores to Gibbs Correctors: Accelerating Uniform-Rate Discrete Diffusion Models](https://arxiv.org/abs/2605.27352v1)

**作者**：Yuchen Liang, Ness Shroff, Yingbin Liang  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-05-26

### 📄 论文摘要

Discrete diffusion models have achieved strong empirical performance in text and other symbolic domains, but, especially for uniform-rate models, they often require many steps to generate a single sample. Existing acceleration methods either rely on training additional quantities or suffer from slow mixing. In this work, we propose a novel Gibbs-based corrector for discrete diffusion models, termed Gibbs-Accelerated Discrete Diffusion (GADD). GADD leverages the structure of the concrete score function to construct Gibbs posterior likelihoods directly, without requiring any additional training beyond standard score estimation. We show that GADD achieves an overall sampling complexity of $\mathcal{O}(\mathrm{polylog} (\varepsilon^{-1}))$, yielding the first such rate for diffusion-based samplers for uniform-rate discrete diffusion models. We also conduct numerical experiments demonstrating the practical advantages of GADD across synthetic data, zero-shot text sampling, and zero-shot conditional music generation. These results corroborate the theory and show that GADD consistently improves sample quality and wall-clock efficiency over standard baselines, including vanilla Euler methods and CTMC correctors. Beyond this, our theoretical analysis introduces a novel framework for analyzing predictor-corrector methods in discrete diffusion models, which may be of independent interest. Unlike existing approaches that rely on the Girsanov change-of-measure technique, our method is based on an induction argument that tracks error propagation across predictor iterations while accounting for inaccuracies in the corrector updates.

### 🤖 AI 总结

**一句话总结**：Discrete diffusion models have achieved strong empirical performance in text and other symbolic domains, but, especially for uniform-rate models, they often require many steps to generate a single sam...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Scores, Gibbs, Correctors, Accelerating, Uniform-Rate, Discrete, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27352v1) | [下载PDF](https://arxiv.org/pdf/2605.27352v1.pdf)

---

## [27. Greening AI Inference with Accuracy and Latency-aware User Incentives](https://arxiv.org/abs/2605.27309v1)

**作者**：Vasilios A. Siris, Adamantia Stamou, George D. Stamoulis 等 5 位作者  
**分类**：cs.LG, cs.OH  
**发布时间**：2026-05-26

### 📄 论文摘要

The widespread use of AI services has raised concerns for its environmental sustainability, towards which recent studies have identified carbon emissions of AI inference as the major contributor. This paper introduces a framework for designing AI inference incentives based on the users' valuation for inference quality and latency, together with their environmental consciousness, while accounting for the tradeoff between carbon emissions and the two QoE parameters. Our approach can accommodate different tradeoffs, that depend on the size and complexity of the AI models and the allocation of resources to serve inference requests. The incentives can be offered through a practical two-tier service subscription that offers users a discount in exchange for reduced carbon emissions. The discounted service option gives the AI provider the flexibility to serve some percentage of inference requests at a lower quality and higher latency during periods of high carbon intensity.

### 🤖 AI 总结

**一句话总结**：The widespread use of AI services has raised concerns for its environmental sustainability, towards which recent studies have identified carbon emissions of AI inference as the major contributor. This...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Greening, Inference, Accuracy, Latency-aware, User, Incentives, widespread, use

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27309v1) | [下载PDF](https://arxiv.org/pdf/2605.27309v1.pdf)

---

## [28. Normal Guidance is what Attention Needs](https://arxiv.org/abs/2605.27306v1)

**作者**：Ethan Harvey, Dennis Johan Loevlie, Michael C. Hughes  
**分类**：cs.LG  
**发布时间**：2026-05-26

### 📄 论文摘要

We consider training classifiers for 3D medical images using only one binary label for the entire volume rather than a label for each 2D slice. In such weakly supervised settings, can we learn accurate classifiers for slice-level predictions? Attention-based multiple instance learning (MIL) can produce an attention score for every slice. Yet recent work demonstrates that a simple center-focused baseline that ignores image content can outperform attention-based and transformer-based MIL at slice-level classification of 3D brain scans. We show this baseline also outperforms existing MIL at slice-level classification of thoracic and abdominal CT scans. Motivated by this baseline, we propose Normal Guidance, a regularization technique that encourages the learned attention distribution to follow a bell-shaped curve. Across three medical imaging datasets totaling over 4 million 2D slices, we show our Normal Guidance enables attention-based and transformer-based MIL methods to deliver significantly better slice-level localization than the state-of-the-art while remaining competitive at whole-scan classification.

### 🤖 AI 总结

**一句话总结**：We consider training classifiers for 3D medical images using only one binary label for the entire volume rather than a label for each 2D slice. In such weakly supervised settings, can we learn accurat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Normal, Guidance, what, Attention, Needs, consider, training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27306v1) | [下载PDF](https://arxiv.org/pdf/2605.27306v1.pdf)

---

## [29. BASIS: Batchwise Advantage Estimation from Single-Rollout Information Sharing for LLM Reasoning](https://arxiv.org/abs/2605.27293v1)

**作者**：Shijin Gong, Erhan Xu, Kai Ye 等 6 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-05-26

### 📄 论文摘要

Reinforcement learning with verifiable rewards has become a standard recipe for improving the reasoning abilities of large language models. Existing algorithms face a tradeoff between computational efficiency and sample efficiency in value estimation and policy learning. We introduce BASIS, a critic-free post-training algorithm designed to address this tradeoff. At each online training step, BASIS samples only one rollout per prompt, but leverages rich information across prompts in the entire batch to improve value function estimation. Our experiments demonstrate that BASIS reduces MSE in value function estimation by 69% compared to REINFORCE++, a representative single-rollout baseline, and achieves lower MSE with one rollout than group mean estimators with 8 rollouts. This improvement in value estimation translates to better policy optimization: using substantially less training time, BASIS achieves performance close to multi-rollout GRPO-type baselines and often outperforms single-rollout REINFORCE-type baselines.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning with verifiable rewards has become a standard recipe for improving the reasoning abilities of large language models. Existing algorithms face a tradeoff between computational ef...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, BASIS, Batchwise, Advantage, Estimation, Single-Rollout, Information, Sharing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27293v1) | [下载PDF](https://arxiv.org/pdf/2605.27293v1.pdf)

---

## [30. Detectability in Diversity: Improved Canary Crafting for Privacy Auditing in One Run](https://arxiv.org/abs/2605.27292v1)

**作者**：Mathieu Dagréou, Aurélien Bellet  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-05-26

### 📄 论文摘要

Privacy auditing aims to empirically assess privacy leakage in machine learning models using membership inference attacks (MIAs), and to derive lower bounds on differential privacy (DP) parameters. Recent one-run auditing methods address the high cost of standard approaches by relying on a single training run with multiple "canary" points whose inclusion or exclusion must be detected by the auditor. In this work, we study the problem of efficiently crafting canaries for one-run privacy auditing. Motivated by recent theoretical insights suggesting that interference between canaries contributes to weaker leakage estimates compared to multi-run methods, we propose to optimize canaries to be both highly detectable and minimally interfering. Our approach combines a greedy initialization based on influence functions with a bilevel optimization procedure that maximizes distinguishability while promoting diversity in embedding space, enabling the use of computationally efficient bilevel algorithms. Experiments show that our method achieves stronger privacy leakage estimates at a lower computational cost than existing canary crafting approaches.

### 🤖 AI 总结

**一句话总结**：Privacy auditing aims to empirically assess privacy leakage in machine learning models using membership inference attacks (MIAs), and to derive lower bounds on differential privacy (DP) parameters. Re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Detectability, Diversity, Improved, Canary, Crafting, Privacy, Auditing, One

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.27292v1) | [下载PDF](https://arxiv.org/pdf/2605.27292v1.pdf)

---

