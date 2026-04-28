# arXiv AI 论文日报 | 2026-04-28

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.CL](#csCL) (7 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. Case-Specific Rubrics for Clinical AI Evaluation: Methodology, Validation, and LLM-Clinician Agreement Across 823 Encounters](https://arxiv.org/abs/2604.24710v1)

**作者**：Aaryan Shah, Andrew Hines, Alexia Downs 等 9 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-04-27

### 📄 论文摘要

Objective. Clinical AI documentation systems require evaluation methodologies that are clinically valid, economically viable, and sensitive to iterative changes. Methods requiring expert review per scoring instance are too slow and expensive for safe, iterative deployment. We present a case-specific, clinician-authored rubric methodology for clinical AI evaluation and examine whether LLM-generated rubrics can approximate clinician agreement.   Materials and Methods. Twenty clinicians authored 1,646 rubrics for 823 clinical cases (736 real-world, 87 synthetic) across primary care, psychiatry, oncology, and behavioral health. Each rubric was validated by confirming that an LLM-based scoring agent consistently scored clinician-preferred outputs higher than rejected ones. Seven versions of an EHR-embedded AI agent for clinicians were evaluated across all cases.   Results. Clinician-authored rubrics discriminated effectively between high- and low-quality outputs (median score gap: 82.9%) with high scoring stability (median range: 0.00%). Median scores improved from 84% to 95%. In later experiments, clinician-LLM ranking agreement (tau: 0.42-0.46) matched or exceeded clinician-clinician agreement (tau: 0.38-0.43), attributable to both ceiling compression and LLM rubric improvement.   Discussion. This convergence supports incorporating LLM rubrics alongside clinician-authored ones. At roughly 1,000 times lower cost, LLM rubrics enable substantially greater evaluation coverage, while continued clinical authorship grounds evaluation in expert judgment. Ceiling compression poses a methodological challenge for future inter-rater agreement studies.   Conclusion. Case-specific rubrics offer a path for clinical AI evaluation that preserves expert judgment while enabling automation at three orders lower cost. Clinician-authored rubrics establish the baseline against which LLM rubrics are validated.

### 🤖 AI 总结

**一句话总结**：Objective. Clinical AI documentation systems require evaluation methodologies that are clinically valid, economically viable, and sensitive to iterative changes. Methods requiring expert review per sc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Case-Specific, Rubrics, Clinical, Evaluation, Methodology, Validation, LLM-Clinician, Agreement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24710v1) | [下载PDF](https://arxiv.org/pdf/2604.24710v1.pdf)

---

## [2. Can Current Agents Close the Discovery-to-Application Gap? A Case Study in Minecraft](https://arxiv.org/abs/2604.24697v1)

**作者**：Zhou Ziheng, Huacong Tang, Jinyuan Zhang 等 12 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-27

### 📄 论文摘要

Discovering causal regularities and applying them to build functional systems--the discovery-to-application loop--is a hallmark of general intelligence, yet evaluating this capacity has been hindered by the vast complexity gap between scientific discovery and real-world engineering. We introduce SciCrafter, a Minecraft-based benchmark that operationalizes this loop through parameterized redstone circuit tasks. Agents must ignite lamps in specified patterns (e.g., simultaneously or in timed sequences); scaling target parameters substantially increases construction complexity and required knowledge, forcing genuine discovery rather than reliance on memorized solutions. Evaluating frontier models including GPT-5.2, Gemini-3-Pro, and Claude-Opus-4.5 under a general-purpose code agent scaffold, we find that all plateau at approximately 26% success rate. To diagnose these failures, we decompose the loop into four capacities--knowledge gap identification, experimental discovery, knowledge consolidation, and knowledge application--and design targeted interventions whose marginal contributions serve as proxies for corresponding gaps. Our analysis reveals that although the general knowledge application capability still remains as the biggest gap across all models, for frontier models the knowledge gap identification starts to become a major hurdle--indicating the bottleneck is shifting from solving problems right to raising the right problems for current AI. We release SciCrafter as a diagnostic probe for future research on AI systems that navigate the full discovery-to-application loop.

### 🤖 AI 总结

**一句话总结**：Discovering causal regularities and applying them to build functional systems--the discovery-to-application loop--is a hallmark of general intelligence, yet evaluating this capacity has been hindered ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Can, Current, Close, Discovery-to-Application, Gap?, Case, Study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24697v1) | [下载PDF](https://arxiv.org/pdf/2604.24697v1.pdf)

---

## [3. Governing What You Cannot Observe: Adaptive Runtime Governance for Autonomous AI Agents](https://arxiv.org/abs/2604.24686v1)

**作者**：German Marin, Jatin Chaudhary  
**分类**：cs.AI  
**发布时间**：2026-04-27

### 📄 论文摘要

Autonomous AI agents can remain fully authorized and still become unsafe as behavior drifts, adversaries adapt, and decision patterns shift without any code change. We propose the \textbf{Informational Viability Principle}: governing an agent reduces to estimating a bound on unobserved risk $\hat{B}(x) = U(x) + SB(x) + RG(x)$ and allowing an action only when its capacity $S(x)$ exceeds $\hat{B}(x)$ by a safety margin. The \textbf{Agent Viability Framework}, grounded in Aubin's viability theory, establishes three properties -- monitoring (P1), anticipation (P2), and monotonic restriction (P3) -- as individually necessary and collectively sufficient for documented failure modes. \textbf{RiskGate} instantiates the framework with dedicated statistical estimators (KL divergence, segment-vs-rest $z$-tests, sequential pattern matching), a fail-secure monotonic pipeline, and a closed-loop Autopilot formalised as an instance of Aubin's regulation map with kill-switch-as-last-resort; a scalar Viability Index $VI(t) \in [-1,+1]$ with first-order $t^*$ prediction transforms governance from reactive to predictive. Contributions are the theoretical framework, the reference implementation, and analytical coverage against published agent-failure taxonomies; quantitative empirical evaluation is scoped as follow-up work.

### 🤖 AI 总结

**一句话总结**：Autonomous AI agents can remain fully authorized and still become unsafe as behavior drifts, adversaries adapt, and decision patterns shift without any code change. We propose the \textbf{Informationa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Governing, What, Cannot, Observe, Adaptive, Runtime, Governance, Autonomous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24686v1) | [下载PDF](https://arxiv.org/pdf/2604.24686v1.pdf)

---

## [4. The Price of Agreement: Measuring LLM Sycophancy in Agentic Financial Applications](https://arxiv.org/abs/2604.24668v1)

**作者**：Zhenyu Zhao, Aparna Balagopalan, Adi Agrawal 等 6 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-04-27

### 📄 论文摘要

Given the increased use of LLMs in financial systems today, it becomes important to evaluate the safety and robustness of such systems. One failure mode that LLMs frequently display in general domain settings is that of sycophancy. That is, models prioritize agreement with expressed user beliefs over correctness, leading to decreased accuracy and trust. In this work, we focus on evaluating sycophancy that LLMs display in agentic financial tasks. Our findings are three-fold: first, we find the models show only low to modest drops in performance in the face of user rebuttals or contradictions to the reference answer, which distinguishes sycophancy that models display in financial agentic settings from findings in prior work. Second, we introduce a suite of tasks to test for sycophancy by user preference information that contradicts the reference answer and find that most models fail in the presence of such inputs. Lastly, we benchmark different modes of recovery such as input filtering with a pretrained LLM.

### 🤖 AI 总结

**一句话总结**：Given the increased use of LLMs in financial systems today, it becomes important to evaluate the safety and robustness of such systems. One failure mode that LLMs frequently display in general domain ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Price, Agreement, Measuring, Sycophancy, Agentic, Financial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24668v1) | [下载PDF](https://arxiv.org/pdf/2604.24668v1.pdf)

---

## [5. Evaluating whether AI models would sabotage AI safety research](https://arxiv.org/abs/2604.24618v1)

**作者**：Robert Kirk, Alexandra Souly, Kai Fronsdal 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-27

### 📄 论文摘要

We evaluate the propensity of frontier models to sabotage or refuse to assist with safety research when deployed as AI research agents within a frontier AI company. We apply two complementary evaluations to four Claude models (Mythos Preview, Opus 4.7 Preview, Opus 4.6, and Sonnet 4.6): an unprompted sabotage evaluation testing model behaviour with opportunities to sabotage safety research, and a sabotage continuation evaluation testing whether models continue to sabotage when placed in trajectories where prior actions have started undermining research. We find no instances of unprompted sabotage across any model, with refusal rates close to zero for Mythos Preview and Opus 4.7 Preview, though all models sometimes only partially completed tasks. In the continuation evaluation, Mythos Preview actively continues sabotage in 7% of cases (versus 3% for Opus 4.6, 4% for Sonnet 4.6, and 0% for Opus 4.7 Preview), and exhibits reasoning-output discrepancy in the majority of these cases, indicating covert sabotage reasoning. Our evaluation framework builds on Petri, an open-source LLM auditing tool, with a custom scaffold running models inside Claude Code, alongside an iterative pipeline for generating realistic sabotage trajectories. We measure both evaluation awareness and a new form of situational awareness termed "prefill awareness", the capability to recognise that prior trajectory content was not self-generated. Opus 4.7 Preview shows notably elevated unprompted evaluation awareness, while prefill awareness remains low across all models. Finally, we discuss limitations including evaluation awareness confounds, limited scenario coverage, and untested pathways to risk beyond safety research sabotage.

### 🤖 AI 总结

**一句话总结**：We evaluate the propensity of frontier models to sabotage or refuse to assist with safety research when deployed as AI research agents within a frontier AI company. We apply two complementary evaluati...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Evaluating, whether, models, would, sabotage, safety, research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24618v1) | [下载PDF](https://arxiv.org/pdf/2604.24618v1.pdf)

---

## cs.CL

## [6. Sentiment and Emotion Classification of Indonesian E-Commerce Reviews via Multi-Task BiLSTM and AutoML Benchmarking](https://arxiv.org/abs/2604.24720v1)

**作者**：Hermawan Manurung, Ibrahim Al-Kahfi, Ahmad Rizqi 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-27

### 📄 论文摘要

Indonesian marketplace reviews mix standard vocabulary with slang, regional loanwords, numeric shorthands, and emoji, making lexicon-based sentiment tools unreliable in practice. This paper describes a two-track classification pipeline applied to the PRDECT-ID dataset, which contains 5,400 product reviews from 29 Indonesian e-commerce categories, each labeled for binary sentiment (Positive/Negative) and five-class emotion (Happy, Sad, Fear, Love, Anger). The first track applies TF-IDF vectorization with a PyCaret AutoML sweep across standard classifiers. The second track is a PyTorch Bidirectional Long Short-Term Memory (BiLSTM) network with a shared encoder and two task-specific output heads. A preprocessing module applies 14 sequential cleaning steps, including a 140-entry slang dictionary assembled from marketplace corpora. Four configurations are benchmarked: BiLSTM Baseline, BiLSTM Improved, BiLSTM Large, and TextCNN. Training uses class-weighted cross-entropy loss, ReduceLROnPlateau scheduling, and early stopping. Both tracks are deployed as Gradio applications on Hugging Face Spaces. Source code is publicly available at https://github.com/ikii-sd/pba2026-crazyrichteam.

### 🤖 AI 总结

**一句话总结**：Indonesian marketplace reviews mix standard vocabulary with slang, regional loanwords, numeric shorthands, and emoji, making lexicon-based sentiment tools unreliable in practice. This paper describes ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Sentiment, Emotion, Classification, Indonesian, E-Commerce, Reviews, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24720v1) | [下载PDF](https://arxiv.org/pdf/2604.24720v1.pdf)

---

## [7. Green Shielding: A User-Centric Approach Towards Trustworthy AI](https://arxiv.org/abs/2604.24700v1)

**作者**：Aaron J. Li, Nicolas Sanchez, Hao Huang 等 11 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-27

### 📄 论文摘要

Large language models (LLMs) are increasingly deployed, yet their outputs can be highly sensitive to routine, non-adversarial variation in how users phrase queries, a gap not well addressed by existing red-teaming efforts. We propose Green Shielding, a user-centric agenda for building evidence-backed deployment guidance by characterizing how benign input variation shifts model behavior. We operationalize this agenda through the CUE criteria: benchmarks with authentic Context, reference standards and metrics that capture true Utility, and perturbations that reflect realistic variations in the Elicitation of model behavior. Guided by the PCS framework and developed with practicing physicians, we instantiate Green Shielding in medical diagnosis through HealthCareMagic-Diagnosis (HCM-Dx), a benchmark of patient-authored queries, together with structured reference diagnosis sets and clinically grounded metrics for evaluating differential diagnosis lists. We also study perturbation regimes that capture routine input variation and show that prompt-level factors shift model behavior along clinically meaningful dimensions. Across multiple frontier LLMs, these shifts trace out Pareto-like tradeoffs. In particular, neutralization, which removes common user-level factors while preserving clinical content, increases plausibility and yields more concise, clinician-like differentials, but reduces coverage of highly likely and safety-critical conditions. Together, these results show that interaction choices can systematically shift task-relevant properties of model outputs and support user-facing guidance for safer deployment in high-stakes domains. Although instantiated here in medical diagnosis, the agenda extends naturally to other decision-support settings and agentic AI systems.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly deployed, yet their outputs can be highly sensitive to routine, non-adversarial variation in how users phrase queries, a gap not well addressed by existin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Green, Shielding, User-Centric, Approach, Towards, Trustworthy, Large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24700v1) | [下载PDF](https://arxiv.org/pdf/2604.24700v1.pdf)

---

## [8. The Chameleon's Limit: Investigating Persona Collapse and Homogenization in Large Language Models](https://arxiv.org/abs/2604.24698v1)

**作者**：Yunze Xiao, Vivienne J. Zhang, Chenghao Yang 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-27

### 📄 论文摘要

Applications based on large language models (LLMs), such as multi-agent simulations, require population diversity among agents. We identify a pervasive failure mode we term \emph{Persona Collapse}: agents each assigned a distinct profile nonetheless converge into a narrow behavioral mode, producing a homogeneous simulated population. To quantify persona collapse, we propose a framework that measures how much of the persona space a population occupies (Coverage), how evenly agents spread across it (Uniformity), and how rich the resulting behavioral patterns are (Complexity). Evaluating ten LLMs on personality simulation (BFI-44), moral reasoning, and self-introduction, we observe persona collapse along two axes: (1) Dimensions: a model can appear diverse on one axis yet structurally degenerate on another, and (2) Domains: the same model may collapse the most in personality yet be the most diverse in moral reasoning. Furthermore, item-level diagnostics reveal that behavioral variation tracks coarse demographic stereotypes rather than the fine-grained individual differences specified in each persona. Counter-intuitively, \textbf{the models achieving the highest per-persona fidelity consistently produce the most stereotyped populations}. We release our toolkit and data to support population-level evaluation of LLMs.

### 🤖 AI 总结

**一句话总结**：Applications based on large language models (LLMs), such as multi-agent simulations, require population diversity among agents. We identify a pervasive failure mode we term \emph{Persona Collapse}: ag...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Chameleon's, Limit, Investigating, Persona, Collapse, Homogenization, Large, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24698v1) | [下载PDF](https://arxiv.org/pdf/2604.24698v1.pdf)

---

## [9. Can LLMs Act as Historians? Evaluating Historical Research Capabilities of LLMs via the Chinese Imperial Examination](https://arxiv.org/abs/2604.24690v1)

**作者**：Lirong Gao, Zeqing Wang, Yuyan Cai 等 9 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-27

### 📄 论文摘要

While Large Language Models (LLMs) have increasingly assisted in historical tasks such as text processing, their capacity for professional-level historical reasoning remains underexplored. Existing benchmarks primarily assess basic knowledge breadth or lexical understanding, failing to capture the higher-order skills, such as evidentiary reasoning,that are central to historical research. To fill this gap, we introduce ProHist-Bench, a novel benchmark anchored in the Chinese Imperial Examination (Keju) system, a comprehensive microcosm of East Asian political, social, and intellectual history spanning over 1,300 years. Developed through deep interdisciplinary collaboration, ProHist-Bench features 400 challenging, expert-curated questions across eight dynasties, accompanied by 10,891 fine-grained evaluation rubrics. Through a rigorous evaluation of 18 LLMs, we reveal a significant proficiency gap: even state-of-the-art LLMs struggle with complex historical research questions. We hope ProHist-Bench will facilitate the development of domain-specific reasoning LLMs, advance computational historical research, and further uncover the untapped potential of LLMs. We release ProHist-Bench at https://github.com/inclusionAI/ABench/tree/main/ProHist-Bench.

### 🤖 AI 总结

**一句话总结**：While Large Language Models (LLMs) have increasingly assisted in historical tasks such as text processing, their capacity for professional-level historical reasoning remains underexplored. Existing be...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, as, Can, Act, Historians?, Evaluating, Historical, Research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24690v1) | [下载PDF](https://arxiv.org/pdf/2604.24690v1.pdf)

---

## [10. Benchmarking Source-Sensitive Reasoning in Turkish: Humans and LLMs under Evidential Trust Manipulation](https://arxiv.org/abs/2604.24665v1)

**作者**：Sercan Karakaş, Yusuf Şimşek  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-27

### 📄 论文摘要

This paper investigates whether source trustworthiness shapes Turkish evidential morphology and whether large language models (LLMs) track this sensitivity. We study the past-domain contrast between -DI and -mIs in controlled cloze contexts where the information source is overtly external, while only its perceived reliability is manipulated (High-Trust vs. Low-Trust). In a human production experiment, native speakers of Turkish show a robust trust effect: High-Trust contexts yield relatively more -DI, whereas Low-Trust contexts yield relatively more -mIs, with the pattern remaining stable across sensitivity analyses. We then evaluate 10 LLMs in three prompting paradigms (open gap-fill, explicit past-tense gap-fill, and forced-choice A/B selection). LLM behavior is highly model- and prompt-dependent: some models show weak or local trust-consistent shifts, but effects are generally unstable, often reversed, and frequently overshadowed by output-compliance problems and strong base-rate suffix preferences. The results provide new evidence for a trust-/commitment-based account of Turkish evidentiality and reveal a clear human-LLM gap in source-sensitive evidential reasoning.

### 🤖 AI 总结

**一句话总结**：This paper investigates whether source trustworthiness shapes Turkish evidential morphology and whether large language models (LLMs) track this sensitivity. We study the past-domain contrast between -...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Benchmarking, Source-Sensitive, Reasoning, Turkish, Humans, under, Evidential

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24665v1) | [下载PDF](https://arxiv.org/pdf/2604.24665v1.pdf)

---

## [11. K-MetBench: A Multi-Dimensional Benchmark for Fine-Grained Evaluation of Expert Reasoning, Locality, and Multimodality in Meteorology](https://arxiv.org/abs/2604.24645v1)

**作者**：Soyeon Kim, Cheongwoong Kang, Myeongjin Lee 等 6 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-27

### 📄 论文摘要

The development of practical (multimodal) large language model assistants for Korean weather forecasters is hindered by the absence of a multidimensional, expert-level evaluation framework grounded in authoritative sources. To address this, we introduce K-MetBench, a diagnostic benchmark grounded in national qualification exams. It exposes critical gaps across four dimensions: expert visual reasoning of charts, logical validity via expert-verified rationales, Korean-specific geo-cultural comprehension, and fine-grained domain analysis. Our evaluation of 55 models reveals a profound modality gap in interpreting specialized diagrams and a reasoning gap where models hallucinate logic despite correct predictions. Crucially, Korean models outperform significantly larger global models in local contexts, demonstrating that parameter scaling alone cannot resolve cultural dependencies. K-MetBench serves as a roadmap for developing reliable, culturally aware expert AI agents. The dataset is available at https://huggingface.co/datasets/soyeonbot/K-MetBench .

### 🤖 AI 总结

**一句话总结**：The development of practical (multimodal) large language model assistants for Korean weather forecasters is hindered by the absence of a multidimensional, expert-level evaluation framework grounded in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, K-MetBench, Multi-Dimensional, Benchmark, Fine-Grained, Evaluation, Expert, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24645v1) | [下载PDF](https://arxiv.org/pdf/2604.24645v1.pdf)

---

## [12. Looking for the Bottleneck in Fine-grained Temporal Relation Classification](https://arxiv.org/abs/2604.24620v1)

**作者**：Hugo Sousa, Ricardo Campos, Alípio Jorge  
**分类**：cs.CL  
**发布时间**：2026-04-27

### 📄 论文摘要

Temporal relation classification is the task of determining the temporal relation between pairs of temporal entities in a text.   Despite recent advancements in natural language processing, temporal relation classification remains a considerable challenge.   Early attempts framed this task using a comprehensive set of temporal relations between events and temporal expressions.   However, due to the task complexity, datasets have been progressively simplified, leading recent approaches to focus on the relations between event pairs and to use only a subset of relations.   In this work, we revisit the broader goal of classifying interval relations between temporal entities by considering the full set of relations that can hold between two time intervals.   The proposed approach, Interval from Point, involves first classifying the point relations between the endpoints of the temporal entities and then decoding these point relations into an interval relation.   Evaluation on the TempEval-3 dataset shows that this approach can yield effective results, achieving a temporal awareness score of $70.1$ percent, a new state-of-the-art on this benchmark.

### 🤖 AI 总结

**一句话总结**：Temporal relation classification is the task of determining the temporal relation between pairs of temporal entities in a text.   Despite recent advancements in natural language processing, temporal r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Looking, Bottleneck, Fine-grained, Temporal, Relation, Classification, task

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24620v1) | [下载PDF](https://arxiv.org/pdf/2604.24620v1.pdf)

---

## cs.CV

## [13. World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://arxiv.org/abs/2604.24764v1)

**作者**：Weijie Wang, Xiaoxuan He, Youping Gu 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-27

### 📄 论文摘要

Recent video foundation models demonstrate impressive visual synthesis but frequently suffer from geometric inconsistencies. While existing methods attempt to inject 3D priors via architectural modifications, they often incur high computational costs and limit scalability. We propose World-R1, a framework that aligns video generation with 3D constraints through reinforcement learning. To facilitate this alignment, we introduce a specialized pure text dataset tailored for world simulation. Utilizing Flow-GRPO, we optimize the model using feedback from pre-trained 3D foundation models and vision-language models to enforce structural coherence without altering the underlying architecture. We further employ a periodic decoupled training strategy to balance rigid geometric consistency with dynamic scene fluidity. Extensive evaluations reveal that our approach significantly enhances 3D consistency while preserving the original visual quality of the foundation model, effectively bridging the gap between video generation and scalable world simulation.

### 🤖 AI 总结

**一句话总结**：Recent video foundation models demonstrate impressive visual synthesis but frequently suffer from geometric inconsistencies. While existing methods attempt to inject 3D priors via architectural modifi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, World-R1, Reinforcing, Constraints, Text-to-Video, Generation, Recent, video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24764v1) | [下载PDF](https://arxiv.org/pdf/2604.24764v1.pdf)

---

## [14. Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation](https://arxiv.org/abs/2604.24763v1)

**作者**：Zhiheng Liu, Weiming Ren, Xiaoke Huang 等 15 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-27

### 📄 论文摘要

Unified multimodal models typically rely on pretrained vision encoders and use separate visual representations for understanding and generation, creating misalignment between the two tasks and preventing fully end-to-end optimization from raw pixels. We introduce Tuna-2, a native unified multimodal model that performs visual understanding and generation directly based on pixel embeddings. Tuna-2 drastically simplifies the model architecture by employing simple patch embedding layers to encode visual input, completely discarding the modular vision encoder designs such as the VAE or the representation encoder. Experiments show that Tuna-2 achieves state-of-the-art performance in multimodal benchmarks, demonstrating that unified pixel-space modelling can fully compete with latent-space approaches for high-quality image generation. Moreover, while the encoder-based variant converges faster in early pretraining, Tuna-2's encoder-free design achieves stronger multimodal understanding at scale, particularly on tasks requiring fine-grained visual perception. These results show that pretrained vision encoders are not necessary for multimodal modelling, and end-to-end pixel-space learning offers a scalable path toward stronger visual representations for both generation and perception.

### 🤖 AI 总结

**一句话总结**：Unified multimodal models typically rely on pretrained vision encoders and use separate visual representations for understanding and generation, creating misalignment between the two tasks and prevent...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Tuna-2, Pixel, Embeddings, Beat, Vision, Encoders, Multimodal, Understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24763v1) | [下载PDF](https://arxiv.org/pdf/2604.24763v1.pdf)

---

## [15. OmniShotCut: Holistic Relational Shot Boundary Detection with Shot-Query Transformer](https://arxiv.org/abs/2604.24762v1)

**作者**：Boyang Wang, Guangyi Xu, Zhipeng Tang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-27

### 📄 论文摘要

Shot Boundary Detection (SBD) aims to automatically identify shot changes and divide a video into coherent shots. While SBD was widely studied in the literature, existing state-of-the-art methods often produce non-interpretable boundaries on transitions, miss subtle yet harmful discontinuities, and rely on noisy, low-diversity annotations and outdated benchmarks. To alleviate these limitations, we propose OmniShotCut to formulate SBD as structured relational prediction, jointly estimating shot ranges with intra-shot relations and inter-shot relations, by a shot query-based dense video Transformer. To avoid imprecise manual labeling, we adopt a fully synthetic transition synthesis pipeline that automatically reproduces major transition families with precise boundaries and parameterized variants. We also introduce OmniShotCutBench, a modern wide-domain benchmark enabling holistic and diagnostic evaluation.

### 🤖 AI 总结

**一句话总结**：Shot Boundary Detection (SBD) aims to automatically identify shot changes and divide a video into coherent shots. While SBD was widely studied in the literature, existing state-of-the-art methods ofte...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OmniShotCut, Holistic, Relational, Shot, Boundary, Detection, Shot-Query, Transformer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24762v1) | [下载PDF](https://arxiv.org/pdf/2604.24762v1.pdf)

---

## [16. DiffuSAM: Diffusion-Based Prompt-Free SAM2 for Few-Shot and Source-Free Medical Image Segmentation](https://arxiv.org/abs/2604.24719v1)

**作者**：Tal Grossman, Noa Cahan, Lev Ayzenberg 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-27

### 📄 论文摘要

Segmentation models such as Segment Anything Model (SAM) and SAM2 achieve strong prompt-driven zero-shot performance. However, their training on natural images limits domain transfer to medical data. Consequently, accurate segmentation typically requires extensive fine-tuning and expert-designed prompts. We propose DiffuSAM, a diffusion-based adaptation of SAM2 for prompt-free medical image segmentation. Our framework synthesizes SAM2-compatible segmentation mask-like embeddings via a lightweight diffusion-prior from off-the-shelf frozen SAM2 image features. The generated embeddings are integrated into SAM2's mask decoder to produce accurate segmentations, thereby eliminating the need for user prompts. The diffusion prior is further conditioned on previously segmented slices, enforcing spatial consistency across volumes. Evaluated on the BTCV and CHAOS datasets for CT and MRI under Source-Free Unsupervised Domain Adaptation (SF-UDA) and Few-Shot settings, DiffuSAM achieves competitive performance with efficient training and inference. Code is available upon request from the corresponding author.

### 🤖 AI 总结

**一句话总结**：Segmentation models such as Segment Anything Model (SAM) and SAM2 achieve strong prompt-driven zero-shot performance. However, their training on natural images limits domain transfer to medical data. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DiffuSAM, Diffusion-Based, Prompt-Free, SAM2, Few-Shot, Source-Free, Medical, Image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24719v1) | [下载PDF](https://arxiv.org/pdf/2604.24719v1.pdf)

---

## [17. WildLIFT: Lifting monocular drone video to 3D for species-agnostic wildlife monitoring](https://arxiv.org/abs/2604.24718v1)

**作者**：Vandita Shukla, Fabio Remondino, Blair Costelloe 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-27

### 📄 论文摘要

Monocular RGB cameras mounted on drones are widely used for wildlife monitoring, yet most analytical pipelines remain confined to two-dimensional image space, leaving geometric information in video underexploited. We present WildLIFT, a computational framework that integrates three-dimensional scene geometry from monocular drone video with open-vocabulary 2D instance segmentation to enable species-agnostic 3D detection and tracking. Oriented 3D bounding box labels with semantic face information enable quantitative assessment of viewpoint coverage and inter-animal occlusion, producing structured metadata for downstream ecological analyses. We validate the framework on 2,581 manually curated frames comprising over 6,700 3D detections across four large mammal species. WildLIFT maintains high identity consistency in multi-animal scenes and substantially reduces manual 3D annotation effort through keyframe-based refinement. By transforming standard drone footage into structured 3D and viewpoint-aware representations, WildLIFT extends the analytical utility of aerial wildlife datasets for behavioural research and population monitoring.

### 🤖 AI 总结

**一句话总结**：Monocular RGB cameras mounted on drones are widely used for wildlife monitoring, yet most analytical pipelines remain confined to two-dimensional image space, leaving geometric information in video un...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, WildLIFT, Lifting, monocular, drone, video, species-agnostic, wildlife

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24718v1) | [下载PDF](https://arxiv.org/pdf/2604.24718v1.pdf)

---

## [18. NeuroClaw Technical Report](https://arxiv.org/abs/2604.24696v1)

**作者**：Cheng Wang, Zhibin He, Zhihao Peng 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-27

### 📄 论文摘要

Agentic artificial intelligence systems promise to accelerate scientific workflows, but neuroimaging poses unique challenges: heterogeneous modalities (sMRI, fMRI, dMRI, EEG), long multi-stage pipelines, and persistent reproducibility risks. To address this gap, we present NeuroClaw, a domain-specialized multi-agent research assistant for executable and reproducible neuroimaging research. NeuroClaw operates directly on raw neuroimaging data across formats and modalities, grounding decisions in dataset semantics and BIDS metadata so users need not prepare curated inputs or bespoke model code. The platform combines harness engineering with end-to-end environment management, including pinned Python environments, Docker support, automated installers for common neuroimaging tools, and GPU configuration. In practice, this layer emphasizes checkpointing, post-execution verification, structured audit traces, and controlled runtime setup, making toolchains more transparent while improving reproducibility and auditability. A three-tier skill/agent hierarchy separates user-facing interaction, high-level orchestration, and low-level tool skills to decompose complex workflows into safe, reusable units. Alongside the NeuroClaw framework, we introduce NeuroBench, a system-level benchmark for executability, artifact validity, and reproducibility readiness. Across multiple multimodal LLMs, NeuroClaw-enabled runs yield consistent and substantial score improvements compared with direct agent invocation. Project homepage: https://cuhk-aim-group.github.io/NeuroClaw/index.html

### 🤖 AI 总结

**一句话总结**：Agentic artificial intelligence systems promise to accelerate scientific workflows, but neuroimaging poses unique challenges: heterogeneous modalities (sMRI, fMRI, dMRI, EEG), long multi-stage pipelin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：NeuroClaw, Technical, Report, Agentic, artificial, intelligence, systems, promise

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24696v1) | [下载PDF](https://arxiv.org/pdf/2604.24696v1.pdf)

---

## [19. Aycromo: An Open-Source Platform for Automatic Chromosome Detection in Metaphase Images Based on Deep Learning](https://arxiv.org/abs/2604.24685v1)

**作者**：Jorge L. A. Lima, Filipe R. Cordeiro  
**分类**：cs.CV  
**发布时间**：2026-04-27

### 📄 论文摘要

Chromosome analysis is a fundamental step in the diagnosis of genetic diseases, but the manual karyotyping workflow is time-consuming and heavily dependent on expert specialists, often requiring several days per patient. Although Deep Learning models have achieved high performance in chromosome detection, most proposed solutions remain restricted to research prototypes or lack graphical interfaces suitable for clinical use. In this work, we present Aycromo, an open-source desktop platform for AI-assisted cytogenetic analysis. Built on Electron and ONNX Runtime, the tool allows cytogeneticists to load pre-trained models, compare architectures through an integrated benchmarking module, and manually correct detections via an interactive annotation interface, all without command-line interaction. Preliminary experiments on metaphase images from the CRCN-NE dataset demonstrate that YOLOv11 achieves 99.40% mAP@50, while the platform reduces per-slide analysis to seconds

### 🤖 AI 总结

**一句话总结**：Chromosome analysis is a fundamental step in the diagnosis of genetic diseases, but the manual karyotyping workflow is time-consuming and heavily dependent on expert specialists, often requiring sever...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Aycromo, Open-Source, Platform, Automatic, Chromosome, Detection, Metaphase

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24685v1) | [下载PDF](https://arxiv.org/pdf/2604.24685v1.pdf)

---

## [20. Benchmarking Pathology Foundation Models for Breast Cancer Survival Prediction](https://arxiv.org/abs/2604.24679v1)

**作者**：Fredrik K. Gustafsson, Constance Boissin, Johan Vallon-Christersson 等 5 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-04-27

### 📄 论文摘要

Pathology foundation models (PFMs) have recently emerged as powerful pretrained encoders for computational pathology, enabling transfer learning across a wide range of downstream tasks. However, systematic comparisons of these models for clinically meaningful prediction problems remain limited, especially in the context of survival prediction under external validation. In this study, we benchmark widely used and recently proposed PFMs for breast cancer survival prediction from whole-slide histopathology images. Using a standardized pipeline based on patch-level feature extraction and a unified survival modeling framework, we evaluate model representations across three independent clinical cohorts comprising more than 5,400 patients with long-term follow-up. Models are trained on one cohort and evaluated on two independent external cohorts, enabling a rigorous assessment of cross-dataset generalization. Overall, H-optimus-1 achieves the strongest survival prediction performance. More broadly, we observe consistent generational improvements across model families, with second-generation PFMs outperforming their first-generation counterparts. However, absolute performance differences between many recent PFMs remain modest, suggesting diminishing returns from further scaling of pretraining data or model size alone. Notably, the compact distilled model H0-mini slightly outperforms its larger teacher model H-optimus-0, despite using fewer than 8% of the parameters and enabling significantly faster feature extraction. Together, these results provide the first large-scale, externally validated benchmark of PFMs for breast cancer survival prediction, and offer practical guidance for efficient deployment of PFMs in clinical workflows.

### 🤖 AI 总结

**一句话总结**：Pathology foundation models (PFMs) have recently emerged as powerful pretrained encoders for computational pathology, enabling transfer learning across a wide range of downstream tasks. However, syste...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Benchmarking, Pathology, Foundation, Models, Breast, Cancer, Survival, Prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24679v1) | [下载PDF](https://arxiv.org/pdf/2604.24679v1.pdf)

---

## [21. Probing CLIP's Comprehension of 360-Degree Textual and Visual Semantics](https://arxiv.org/abs/2604.24642v1)

**作者**：Hai Wang, Xiaochen Yang, Mingzhi Dong 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-27

### 📄 论文摘要

The dream of instantly creating rich 360-degree panoramic worlds from text is rapidly becoming a reality, yet a crucial gap exists in our ability to reliably evaluate their semantic alignment. Contrastive Language-Image Pre-training (CLIP) models, standard AI evaluators, predominantly trained on perspective image-text pairs, face an open question regarding their understanding of the unique characteristics of 360-degree panoramic image-text pairs. This paper addresses this gap by first introducing two concepts: \emph{360-degree textual semantics}, semantic information conveyed by explicit format identifiers, and \emph{360-degree visual semantics}, invariant semantics under horizontal circular shifts. To probe CLIP's comprehension of these semantics, we then propose novel evaluation methodologies using keyword manipulation and horizontal circular shifts of varying magnitudes. Rigorous statistical analyses across popular CLIP configurations reveal that: (1) CLIP models effectively leverage explicit textual identifiers, demonstrating an understanding of 360-degree textual semantics; and (2) CLIP models fail to robustly preserve semantic alignment under horizontal circular shifts, indicating limited comprehension of 360-degree visual semantics. To address this limitation, we propose a LoRA-based fine-tuning framework that explicitly instills invariance to circular shifts. Our fine-tuned models exhibit improved comprehension of 360-degree visual semantics, though with a slight degradation in original semantic evaluation performance, highlighting a fundamental trade-off in adapting CLIP to 360-degree panoramic images. Code is available at https://github.com/littlewhitesea/360Semantics.

### 🤖 AI 总结

**一句话总结**：The dream of instantly creating rich 360-degree panoramic worlds from text is rapidly becoming a reality, yet a crucial gap exists in our ability to reliably evaluate their semantic alignment. Contras...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Probing, CLIP's, Comprehension, 360-Degree, Textual, Visual, Semantics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24642v1) | [下载PDF](https://arxiv.org/pdf/2604.24642v1.pdf)

---

## [22. Meta-CoT: Enhancing Granularity and Generalization in Image Editing](https://arxiv.org/abs/2604.24625v1)

**作者**：Shiyi Zhang, Yiji Cheng, Tiankai Hang 等 11 位作者  
**分类**：cs.CV, cs.AI, cs.LG, cs.MM  
**发布时间**：2026-04-27

### 📄 论文摘要

Unified multi-modal understanding/generative models have shown improved image editing performance by incorporating fine-grained understanding into their Chain-of-Thought (CoT) process. However, a critical question remains underexplored: what forms of CoT and training strategy can jointly enhance both the understanding granularity and generalization? To address this, we propose Meta-CoT, a paradigm that performs a two-level decomposition of any single-image editing operation with two key properties: (1) Decomposability. We observe that any editing intention can be represented as a triplet - (task, target, required understanding ability). Inspired by this, Meta-CoT decomposes both the editing task and the target, generating task-specific CoT and traversing editing operations on all targets. This decomposition enhances the model's understanding granularity of editing operations and guides it to learn each element of the triplet during training, substantially improving the editing capability. (2) Generalizability. In the second decomposition level, we further break down editing tasks into five fundamental meta-tasks. We find that training on these five meta-tasks, together with the other two elements of the triplet, is sufficient to achieve strong generalization across diverse, unseen editing tasks. To further align the model's editing behavior with its CoT reasoning, we introduce the CoT-Editing Consistency Reward, which encourages more accurate and effective utilization of CoT information during editing. Experiments demonstrate that our method achieves an overall 15.8% improvement across 21 editing tasks, and generalizes effectively to unseen editing tasks when trained on only a small set of meta-tasks. Our code, benchmark, and model are released at https://shiyi-zh0408.github.io/projectpages/Meta-CoT/

### 🤖 AI 总结

**一句话总结**：Unified multi-modal understanding/generative models have shown improved image editing performance by incorporating fine-grained understanding into their Chain-of-Thought (CoT) process. However, a crit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Meta-CoT, Enhancing, Granularity, Generalization, Image, Editing, Unified, multi-modal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24625v1) | [下载PDF](https://arxiv.org/pdf/2604.24625v1.pdf)

---

## [23. CF-VLA: Efficient Coarse-to-Fine Action Generation for Vision-Language-Action Policies](https://arxiv.org/abs/2604.24622v1)

**作者**：Fan Du, Feng Yan, Jianxiong Wu 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-27

### 📄 论文摘要

Flow-based vision-language-action (VLA) policies offer strong expressivity for action generation, but suffer from a fundamental inefficiency: multi-step inference is required to recover action structure from uninformative Gaussian noise, leading to a poor efficiency-quality trade-off under real-time constraints. We address this issue by rethinking the role of the starting point in generative action modeling. Instead of shortening the sampling trajectory, we propose CF-VLA, a coarse-to-fine two-stage formulation that restructures action generation into a coarse initialization step that constructs an action-aware starting point, followed by a single-step local refinement that corrects residual errors. Concretely, the coarse stage learns a conditional posterior over endpoint velocity to transform Gaussian noise into a structured initialization, while the fine stage performs a fixed-time refinement from this initialization. To stabilize training, we introduce a stepwise strategy that first learns a controlled coarse predictor and then performs joint optimization. Experiments on CALVIN and LIBERO show that our method establishes a strong efficiency-performance frontier under low-NFE (Number of Function Evaluations) regimes: it consistently outperforms existing NFE=2 methods, matches or surpasses the NFE=10 $π_{0.5}$ baseline on several metrics, reduces action sampling latency by 75.4\%, and achieves the best average real-robot success rate of 83.0\%, outperforming MIP by 19.5 points and $π_{0.5}$ by 4.0 points. These results suggest that structured, coarse-to-fine generation enables both strong performance and efficient inference. Our code is available at https://github.com/EmbodiedAI-RoboTron/CF-VLA.

### 🤖 AI 总结

**一句话总结**：Flow-based vision-language-action (VLA) policies offer strong expressivity for action generation, but suffer from a fundamental inefficiency: multi-step inference is required to recover action structu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CF-VLA, Efficient, Coarse-to-Fine, Action, Generation, Vision-Language-Action, Policies, Flow-based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24622v1) | [下载PDF](https://arxiv.org/pdf/2604.24622v1.pdf)

---

## cs.LG

## [24. The Optimal Sample Complexity of Multiclass and List Learning](https://arxiv.org/abs/2604.24749v1)

**作者**：Chirag Pabbaraju  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-04-27

### 📄 论文摘要

While the optimal sample complexity of binary classification in terms of the VC dimension is well-established, determining the optimal sample complexity of multiclass classification has remained open. The appropriate complexity parameter for multiclass classification is the DS dimension, and despite significant efforts, a gap of $\sqrt{\text{DS}}$ has persisted between the upper and lower bounds on sample complexity.   Recent work by Hanneke et al. (2026) shows a novel algebraic characterization of multiclass hypothesis classes in terms of their DS dimension. Building up on this, we show that the maximum hypergraph density of any multiclass hypothesis class is upper-bounded by its DS dimension. This proves a longstanding conjecture of Daniely and Shalev-Shwartz (2014). As a consequence, we determine the optimal dependence of the sample complexity on the DS dimension for multiclass as well as list learning.

### 🤖 AI 总结

**一句话总结**：While the optimal sample complexity of binary classification in terms of the VC dimension is well-established, determining the optimal sample complexity of multiclass classification has remained open....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Optimal, Sample, Complexity, Multiclass, List, Learning, While

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24749v1) | [下载PDF](https://arxiv.org/pdf/2604.24749v1.pdf)

---

## [25. Conflict-Aware Harmonized Rotational Gradient for Multiscale Kinetic Regimes](https://arxiv.org/abs/2604.24745v1)

**作者**：Zhangyong Liang  
**分类**：cs.LG  
**发布时间**：2026-04-27

### 📄 论文摘要

In this paper, we propose a harmonized rotational gradient method, termed HRGrad, for simultaneously tackling multiscale time-dependent kinetic problems with varying small parameters.   These parameters exhibit asymptotic transitions from microscopic to macroscopic physics, making it a challenging multi-task problem to solve over all ranges simultaneously.   Solving tasks in different asymptotic regions often encounter gradient conflicts, which can lead to the failure of multi-task learning.   To address this challenge, we explicitly encode a hidden representation of these parameters, ensuring that the corresponding solving tasks are serialized for simultaneous training.   Furthermore, to mitigate gradient conflicts, we segment the prediction results to construct task losses and introduce a novel gradient alignment metric to ensure a positive dot product between the final update and each loss-specific gradient.   This metric maintains consistent optimization rates for all task losses and dynamically adjusts gradient magnitudes based on conflict levels.   Moreover, we provide a mathematical proof demonstrating the convergence of the HRGrad method, which is evaluated across a range of challenging asymptotic-preserving neural networks (APNNs) scenarios.   We conduct an extensive set of experiments encompassing the Bhatnagar-Gross-Krook (BGK) equation and the linear transport equation in all ranges of Knudsen number.   Our results indicate that HRGrad effectively overcomes the `failure modes' of APNNs in these problems.

### 🤖 AI 总结

**一句话总结**：In this paper, we propose a harmonized rotational gradient method, termed HRGrad, for simultaneously tackling multiscale time-dependent kinetic problems with varying small parameters.   These paramete...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Conflict-Aware, Harmonized, Rotational, Gradient, Multiscale, Kinetic, Regimes, paper

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24745v1) | [下载PDF](https://arxiv.org/pdf/2604.24745v1.pdf)

---

## [26. SpecRLBench: A Benchmark for Generalization in Specification-Guided Reinforcement Learning](https://arxiv.org/abs/2604.24729v1)

**作者**：Zijian Guo, İlker Işık, H. M. Sabbir Ahmad 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-27

### 📄 论文摘要

Specification-guided reinforcement learning (RL) provides a principled framework for encoding complex, temporally extended tasks using formal specifications such as linear temporal logic (LTL). While recent methods have shown promising results, their ability to generalize across unseen specifications and diverse environments remains insufficiently understood. In this work, we introduce SpecRLBench, a benchmark designed to evaluate the generalization capabilities of LTL-based specification-guided RL methods. The benchmark spans multiple difficulty levels across navigation and manipulation domains, incorporating both static and dynamic environments, diverse robot dynamics, and varied observation modalities. Through extensive empirical evaluation, we characterize the strengths and limitations of existing approaches and reveal the challenges that emerge as specification and environment complexity increase. SpecRLBench provides a structured platform for systematic comparison and supports the development of more generalizable specification-guided RL methods. Code is available at https://github.com/BU-DEPEND-Lab/SpecRLBench.

### 🤖 AI 总结

**一句话总结**：Specification-guided reinforcement learning (RL) provides a principled framework for encoding complex, temporally extended tasks using formal specifications such as linear temporal logic (LTL). While ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, SpecRLBench, Benchmark, Generalization, Specification-Guided, Reinforcement, Learning, provides

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24729v1) | [下载PDF](https://arxiv.org/pdf/2604.24729v1.pdf)

---

## [27. Diffusion-Guided Feature Selection via Nishimori Temperature: Noise-Based Spectral Embedding](https://arxiv.org/abs/2604.24692v1)

**作者**：Vasiliy S. Usatyuk, Denis A. Sapozhnikov, Sergey I. Egorov  
**分类**：cs.LG  
**发布时间**：2026-04-27

### 📄 论文摘要

We propose Noise-Based Spectral Embedding (NBSE), a physics-informed framework for selecting informative features from high-dimensional data without greedy search. NBSE constructs a sparse similarity graph on the samples and identifies the Nishimori temperature $β_N$ the critical inverse temperature at which the Bethe Hessian becomes singular. The corresponding smallest eigenvector captures the dominant mode of an intrinsically degree-corrected diffusion process, naturally reweighting nodes to prevent hub dominance. By transposing the data matrix and applying NBSE in feature space, we obtain a one-dimensional spectral embedding that reveals groups of redundant or semantically related dimensions; balanced binning then selects one representative per group. We prove that coloured Gaussian perturbations shift $β_N$ by at most $O(\barσ^2)$, guaranteeing robustness to measurement noise. Experiments on ImageNet embeddings from MobileNetV2 and EfficientNet-B4 show that NBSE preserves classification accuracy even under aggressive compression: on EfficientNet-B4 the accuracy drop is below $1\%$ when retaining only $30\%$ of features, outperforming ANOVA $F$-test and random selection by up to $6.8\%$.

### 🤖 AI 总结

**一句话总结**：We propose Noise-Based Spectral Embedding (NBSE), a physics-informed framework for selecting informative features from high-dimensional data without greedy search. NBSE constructs a sparse similarity ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion-Guided, Feature, Selection, via, Nishimori, Temperature, Noise-Based, Spectral

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24692v1) | [下载PDF](https://arxiv.org/pdf/2604.24692v1.pdf)

---

## [28. A Functorial Formulation of Neighborhood Aggregating Deep Learning](https://arxiv.org/abs/2604.24672v1)

**作者**：Sun Woo Park, Yun Young Choi, U Jin Choi 等 4 位作者  
**分类**：cs.LG, math.AT  
**发布时间**：2026-04-27

### 📄 论文摘要

We provide a mathematical interpretation of convolutional (or message passing) neural networks by using presheaves and copresheaves of the set of continuous functions over a topological space. Based on this interpretation, we formulate a theoretical heuristic which elaborates a number of empirical limitations of these neural networks by using obstructions on such sets of continuous functions over a topological space to be sheaves or copresheaves.

### 🤖 AI 总结

**一句话总结**：We provide a mathematical interpretation of convolutional (or message passing) neural networks by using presheaves and copresheaves of the set of continuous functions over a topological space. Based o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, We, Functorial, Formulation, Neighborhood, Aggregating, Deep, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24672v1) | [下载PDF](https://arxiv.org/pdf/2604.24672v1.pdf)

---

## [29. The Last Human-Written Paper: Agent-Native Research Artifacts](https://arxiv.org/abs/2604.24658v1)

**作者**：Jiachen Liu, Jiaxin Pei, Jintao Huang 等 37 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-27

### 📄 论文摘要

Scientific publication compresses a branching, iterative research process into a linear narrative, discarding the majority of what was discovered along the way. This compilation imposes two structural costs: a Storytelling Tax, where failed experiments, rejected hypotheses, and the branching exploration process are discarded to fit a linear narrative; and an Engineering Tax, where the gap between reviewer-sufficient prose and agent-sufficient specification leaves critical implementation details unwritten. Tolerable for human readers, these costs become critical when AI agents must understand, reproduce, and extend published work. We introduce the Agent-Native Research Artifact (Ara), a protocol that replaces the narrative paper with a machine-executable research package structured around four layers: scientific logic, executable code with full specifications, an exploration graph that preserves the failures compilation discards, and evidence grounding every claim in raw outputs. Three mechanisms support the ecosystem: a Live Research Manager that captures decisions and dead ends during ordinary development; an Ara Compiler that translates legacy PDFs and repos into Aras; and an Ara-native review system that automates objective checks so human reviewers can focus on significance, novelty, and taste. On PaperBench and RE-Bench, Ara raises question-answering accuracy from 72.4% to 93.7% and reproduction success from 57.4% to 64.4%. On RE-Bench's five open-ended extension tasks, preserved failure traces in Ara accelerate progress, but can also constrain a capable agent from stepping outside the prior-run box depending on the agent's capabilities.

### 🤖 AI 总结

**一句话总结**：Scientific publication compresses a branching, iterative research process into a linear narrative, discarding the majority of what was discovered along the way. This compilation imposes two structural...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Last, Human-Written, Paper, Agent-Native, Research, Artifacts, Scientific, publication

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24658v1) | [下载PDF](https://arxiv.org/pdf/2604.24658v1.pdf)

---

## [30. Cortex-Inspired Continual Learning: Unsupervised Instantiation and Recovery of Functional Task Networks](https://arxiv.org/abs/2604.24637v1)

**作者**：Kevin McKee, Thomas Hazy, Yicong Zheng 等 5 位作者  
**分类**：cs.LG, cs.AI, q-bio.NC  
**发布时间**：2026-04-27

### 📄 论文摘要

Block-sequential continual learning demands that a single model both protect prior solutions from catastrophic forgetting and efficiently infer at inference time which prior solution matches the current input without task labels. We present Functional Task Networks (FTN), a parameter-isolation method inspired by structural and dynamical motifs found in the mammalian neocortex. Similar to mixture-of-experts, this method uses a high dimensional, self-organizing binary mask over a large population of small but deep networks, inspired by dendritic models of pyramidal neurons. The mask is produced by a three-stage procedure: (1) gradient descent on a continuous mask identifies task-relevant neurons, (2) a smoothing kernel biases the result toward spatial contiguity, (3) and k-winner-take-all binarizes the resulting group at a fixed capacity budget. Like mixture-of-experts, each neuron is an independent deep network, so disjoint masks give exactly disjoint gradient updates, providing structural guarantees against catastrophic forgetting. This three-stage procedure recovers the sub-network of a previously-trained task in a single gradient step, providing unsupervised task segmentation at inference time. We test it on three continual-learning benchmarks: (1) a synthetic multi-task classification/regression generator, (2) MNIST with shuffled class labels (pure concept shift), and (3) Permuted MNIST (domain shift). On all three, FTN with fine grained smoothing (FTN-Slow) results in nearly zero forgetting. FTN with a large kernel and only 2 iterations of smoothing (FTN-Fast) trades off some retention for increased speed. We show that the spatial organization mechanism reduces the effective mask search from the combinatorial top-k subset problem in O(C(H,K)) to the complexity of a near-linear scan in O(H) over compact cortical neighborhoods, which is parallelized by the gradient-based update.

### 🤖 AI 总结

**一句话总结**：Block-sequential continual learning demands that a single model both protect prior solutions from catastrophic forgetting and efficiently infer at inference time which prior solution matches the curre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Cortex-Inspired, Continual, Learning, Unsupervised, Instantiation, Recovery, Functional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.24637v1) | [下载PDF](https://arxiv.org/pdf/2604.24637v1.pdf)

---

