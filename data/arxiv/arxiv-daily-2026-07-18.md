# arXiv AI 论文日报 | 2026-07-18

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (8 篇)
- [cs.CL](#csCL) (7 篇)
- [cs.AI](#csAI) (11 篇)
- [cs.LG](#csLG) (4 篇)

---

## cs.AI

## [1. Pretraining Data Can Be Poisoned through Computational Propaganda](https://arxiv.org/abs/2607.15267v1)

**作者**：Victoria Graf, Hannaneh Hajishirzi, Noah A. Smith 等 5 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-07-16

### 📄 论文摘要

Poisoning pretraining data can introduce harmful behaviors to LMs that are difficult to detect and mitigate. Prior work on poisoning pretraining data has largely exploited established data sources such as Wikipedia, which do not represent the large scale and heterogeneity typical of pretraining corpora, and has ignored the interaction between poisoned data and data curation pipelines. We demonstrate that poisoning attacks on pretraining data are feasible beyond this limited setting through an existing web-scale content injection mechanism: public discussion interfaces. Additionally, to measure whether malicious content is included after web crawling and data curation, we introduce HalfLife, a novel analysis for estimating adversarial content inclusion in web-crawl based LM training data. We use HalfLife to explore the feasibility of poisoning pretraining corpora at web scale through open discussion interfaces. Our analysis demonstrates the importance of estimating whether poison injections are included in pretraining data, and establishes third-party webpage content as a possible vector for attacking language model pretraining.

### 🤖 AI 总结

**一句话总结**：Poisoning pretraining data can introduce harmful behaviors to LMs that are difficult to detect and mitigate. Prior work on poisoning pretraining data has largely exploited established data sources suc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Be, Pretraining, Data, Can, Poisoned, through, Computational, Propaganda

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15267v1) | [下载PDF](https://arxiv.org/pdf/2607.15267v1.pdf)

---

## [2. SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration](https://arxiv.org/abs/2607.15257v1)

**作者**：Yuyao Zhang, Junjie Gao, Zhengxian Wu 等 14 位作者  
**分类**：cs.AI, cs.IR  
**发布时间**：2026-07-16

### 📄 论文摘要

Recent advances in Tool-Integrated Large Language Models have made web search a core capability of information-seeking agents. However, as interaction histories grow, agents increasingly struggle to track task progress. When search attempts fail to yield useful evidence, current single- and multi-agent systems can become trapped in repetitive loops, wasting search budgets and ultimately compromising the quality and completeness of the final output. We introduce SearchOS, a system-level multi-agent framework that turns fragile, implicit search progress into explicit, persistent, and shared state. First, we formulate open-domain information seeking as relational schema completion with grounded citations, where agents discover entities, populate attributes across linked tables, and anchor each value to source evidence. Then we design Search-Oriented Context Management (SOCM), which externalizes the evolving state into Frontier Task, an Evidence Graph, a Coverage Map, and Failure Memory. Built on SOCM, SearchOS applies a pipeline-parallel scheduling mechanism that overlaps the execution of sub-agents and continuously refills freed slots with tasks targeting unresolved coverage gaps to improve utilization and throughput. To schedule and control the execution of search agents, SearchOS introduces a Search Tool Middleware Harness that intercepts model and tool interactions to record grounded evidence and react to stalls or budget exhaustion, and provides a reusable hierarchical skill system comprising strategy and access skills to augment the agents' search process and avoid repeating failed search patterns across runs. On WideSearch and GISA, SearchOS leads all metrics among the evaluated single- and multi-agent baselines, paving the way toward robust information-seeking collaboration.

### 🤖 AI 总结

**一句话总结**：Recent advances in Tool-Integrated Large Language Models have made web search a core capability of information-seeking agents. However, as interaction histories grow, agents increasingly struggle to t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SearchOS-V1, Towards, Robust, Open-Domain, Information-Seeking, Collaboration, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15257v1) | [下载PDF](https://arxiv.org/pdf/2607.15257v1.pdf)

---

## [3. teLLMe Why (Ain't Nothing but a Jam): Exploratory Causal Analysis of Urban Driving Data](https://arxiv.org/abs/2607.15254v1)

**作者**：Qiwei Li, Jorge Ortiz  
**分类**：cs.AI, cs.HC  
**发布时间**：2026-07-16

### 📄 论文摘要

Traffic agencies now have access to large volumes of video-derived data for studying safety and congestion. Most of these data are observational and collected without interventions, which makes causal questions such as "How would rain change traffic density?" difficult to answer. We present teLLMe, a system for exploratory causal analysis of urban driving datasets. The system starts from a structured event table built from dashcam annotations and combines causal structure learning with the PC algorithm, bootstrap-based stability checks, and query-specific effect estimation using linear regression and DoWhy. Natural-language questions are mapped to structured causal queries through a schema-aware LLM, enabling users to specify treatments, outcomes, and subpopulations. teLLMe returns a "Causal Card" that summarizes effect estimates, adjustment sets, DAG support, and assumptions, followed by a short natural-language explanation. Case studies on BDD-derived traffic events show that the system can surface plausible relationships involving weather, peak hours, and traffic density, while making uncertainty and modeling choices explicit. The system is designed as a tool for hypothesis generation and expert reasoning rather than a source of definitive causal claims.

### 🤖 AI 总结

**一句话总结**：Traffic agencies now have access to large volumes of video-derived data for studying safety and congestion. Most of these data are observational and collected without interventions, which makes causal...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：teLLMe, Why, Ain't, Nothing, but, Jam, Exploratory, Causal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15254v1) | [下载PDF](https://arxiv.org/pdf/2607.15254v1.pdf)

---

## [4. AutoSynthesis: An agentic system for automated meta-analysis](https://arxiv.org/abs/2607.15247v1)

**作者**：Moein Taherinezhad, Sebastian Maier, Gerardo Vitagliano 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-16

### 📄 论文摘要

Evidence synthesis is crucial for turning primary research into reliable knowledge for science, medicine, education, and policy. Yet, quantitative evidence synthesis remains largely manual and difficult to scale. Here, we introduce AutoSynthesis, an end-to-end multi-agent system for automated meta-analysis. Given a research question in natural language, AutoSynthesis formulates a search strategy, retrieves scientific literature, screens candidate studies, assesses full-text eligibility, extracts quantitative statistics, computes standardized effect sizes, and finally performs random-effects meta-analysis. AutoSynthesis further supports heterogeneity analysis to examine how effect sizes vary across moderators, as well as risk-of-bias assessment. As output, AutoSynthesis produces a transparent report aligned with PRISMA guidelines. In our application, AutoSynthesis screened over 28 studies and extracted more than 20 quantitative claims. The pooled effect estimates produced by AutoSynthesis are similar to Hedges' $g$ of expert-conducted meta-analyses, indicating close agreement with manual evidence synthesis. Together, these results show that AutoSynthesis can make quantitative evidence synthesis more scalable, thereby supporting evidence-based decision-making across disciplines.

### 🤖 AI 总结

**一句话总结**：Evidence synthesis is crucial for turning primary research into reliable knowledge for science, medicine, education, and policy. Yet, quantitative evidence synthesis remains largely manual and difficu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, AutoSynthesis, agentic, system, automated, meta-analysis, Evidence, synthesis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15247v1) | [下载PDF](https://arxiv.org/pdf/2607.15247v1.pdf)

---

## [5. When Words Are Safe But Actions Kill: Probing Physical Danger Beyond Text Safety in Hidden-State Risk Space](https://arxiv.org/abs/2607.15218v1)

**作者**：Weimeng Wang, Ziqiang Wang, Zihang Zhan 等 6 位作者  
**分类**：cs.AI, cs.CR  
**发布时间**：2026-07-16

### 📄 论文摘要

Large language models (LLMs) increasingly serve as high-level planners for embodied agents, where linguistically benign instructions can become unsafe once grounded in the physical world. We study whether this physically grounded danger is the same safety problem as ordinary text-level content danger. Through hidden-state direction analysis and random-split null tests, we show that content danger (CD) and physical danger (PD) form separable signals in LLM representations across Qwen2.5-3B/7B/14B/32B, Phi-3.5 and SmolLM2. Building on the CD/PD separability, we propose PRISM, a single-layer L2-regularized logistic probe over full hidden states. PRISM achieves 86.2--87.7\% accuracy on SafeAgentBench with 11.7--13.7\% FPR, while same-scale LLM judges over-block safe tasks at 24.7--39.0\% FPR. We further introduce PhysicalSafetyBench-1K (PSB-1K), a contrastive benchmark of 1{,}000 physical-risk pairs without direct harm keywords, to test whether methods detect physically grounded danger rather than explicit unsafe wording. On PSB-1K, PRISM reaches 99.6\% accuracy and 0.7\% FPR, whereas a Qwen2.5-3B judge rejects 67.8\% of safe tasks. PRISM also replicates on SafeText and EARBench, supporting hidden-state probing as a representation-level method for physical safety beyond text moderation.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) increasingly serve as high-level planners for embodied agents, where linguistically benign instructions can become unsafe once grounded in the physical world. We study whe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Words, Safe, But, Actions, Kill, Probing, Physical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15218v1) | [下载PDF](https://arxiv.org/pdf/2607.15218v1.pdf)

---

## [6. Self-Evolving Human-Centered Framework for Explainable Depression Symptom Annotation](https://arxiv.org/abs/2607.15202v1)

**作者**：Hoang-Loc Cao, Van Pham, Truong Thanh Hung Nguyen 等 7 位作者  
**分类**：cs.AI, cs.HC, cs.MA, cs.MM  
**发布时间**：2026-07-16

### 📄 论文摘要

Annotation quality is a major bottleneck in building reliable and explainable artificial intelligence (XAI) systems for mental health research. In depression-related datasets, labels are often assigned without structured evidence, symptom-level justification, or traceable alignment with the criteria of the Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR), limiting both transparency and downstream model interpretability. We propose a self-evolving, expert-in-the-loop annotation framework for Major Depressive Disorder (MDD) that combines large language model (LLM)-assisted labeling with expert verification. The framework is intended to support the construction of explainable, DSM-5-TR-aligned datasets rather than to perform clinical diagnosis. It operates in three stages: candidate evidence selection from textual records, criterion-level DSM-5-TR analysis, and case-level synthesis that produces label-level diagnostic and severity annotations. A dual-memory architecture, composed of Example Memory and Reflection Memory, is designed to internalize expert feedback and iteratively improve future annotations without retraining. We describe this mechanism and leave its evaluation across multiple feedback cycles to future work. In addition to final labels, the framework exports clinical evidence, reasoning traces, and edit histories, enabling comprehensive auditability. In a pilot study using expert-reviewed samples, the proposed approach improves annotation consistency and explainability while reducing manual revision effort.

### 🤖 AI 总结

**一句话总结**：Annotation quality is a major bottleneck in building reliable and explainable artificial intelligence (XAI) systems for mental health research. In depression-related datasets, labels are often assigne...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Self-Evolving, Human-Centered, Framework, Explainable, Depression, Symptom, Annotation, quality

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15202v1) | [下载PDF](https://arxiv.org/pdf/2607.15202v1.pdf)

---

## [7. Plover: Steering GUI Agents through Plan-Centric Interaction](https://arxiv.org/abs/2607.15193v1)

**作者**：Madhumitha Venkatesan, Shicheng Wen, Jiajing Guo 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-16

### 📄 论文摘要

Graphical user interface (GUI) automation remains challenging in real-world environments, where dynamic layouts, unexpected dialogs, and evolving interface states can cause autonomous agents to drift from user intent. Recent vision-based multimodal agents improve flexibility by operating directly over screenshots and natural language instructions, but planning and adaptation often remain internal, limiting users' ability to inspect, supervise, or correct system behavior. We present Plover, a plan-centric vision-based GUI automation system that externalizes task plans and replanning as persistent, inspectable, and revisable artifacts. Through a planner--executor architecture, Plover supports explicit supervision of evolving execution, localized correction through editable plans, natural-language guidance, and screenshot-grounded interventions, while preserving prior progress during repair. A formative study with six participants informed the interaction design. We then evaluate Plover through benchmark failure-case repair and scenario-based workflow analyses. Our results show that many autonomous GUI-agent failures are structurally repairable when plans remain visible and interventions are localized, and that explicit replanning helps make GUI automation more transparent, controllable, and adaptable.

### 🤖 AI 总结

**一句话总结**：Graphical user interface (GUI) automation remains challenging in real-world environments, where dynamic layouts, unexpected dialogs, and evolving interface states can cause autonomous agents to drift ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Plover, Steering, GUI, through, Plan-Centric, Interaction, Graphical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15193v1) | [下载PDF](https://arxiv.org/pdf/2607.15193v1.pdf)

---

## [8. Can We Trust Item Response Theory for AI Evaluation?](https://arxiv.org/abs/2607.15190v1)

**作者**：Han Jiang, Sunbeom Kwon, Jinwen Luo 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-16

### 📄 论文摘要

AI benchmarks increasingly leverage item-level statistical models, particularly item response theory (IRT), to estimate model capabilities, rank systems, select informative examples, and diagnose benchmark quality. However, AI benchmark data often departs from the data regime of human testing, for which standard IRT estimation tools were originally developed: benchmarks typically involve fewer evaluated models, far more items, and capability distributions that may be skewed, clustered, or multimodal. We examine how these regime mismatches challenge the reliability of IRT modeling for AI evaluation. Using item parameters and capability distributions derived from six widely used LLM benchmarks, we simulate response matrices under three common IRT models and compare four estimation tools used in recent benchmark studies: marginal maximum likelihood, Markov chain Monte Carlo, variational inference, and a neural pseudo-Siamese estimator. Across 18,000 simulation conditions, we systematically evaluate computational feasibility, scalability, and the reliability of IRT inferences about model rankings, predicted performance, and item characteristics. Results show that classical estimators can become infeasible in large benchmark settings, whereas scalable estimators can produce unreliable item-level and ranking inferences with small or nonnormally distributed model sets. This study identifies when latent trait models reliably support or risk distorting AI benchmarking claims, and what sample sizes and diagnostics are needed for trustworthy use.

### 🤖 AI 总结

**一句话总结**：AI benchmarks increasingly leverage item-level statistical models, particularly item response theory (IRT), to estimate model capabilities, rank systems, select informative examples, and diagnose benc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Can, Trust, Item, Response, Theory, Evaluation?, benchmarks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15190v1) | [下载PDF](https://arxiv.org/pdf/2607.15190v1.pdf)

---

## [9. Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy](https://arxiv.org/abs/2607.15176v1)

**作者**：Patrick Phuoc Do, Chau M. Ta, Chaoli Wang  
**分类**：cs.AI, cs.CL, cs.HC  
**发布时间**：2026-07-16

### 📄 论文摘要

Multimodal large language models (MLLMs) are increasingly used to interpret visualizations, yet current evaluations remain largely chart-centric and provide limited evidence of understanding of scientific visualization (SciVis). We benchmark six MLLMs on the scientific visualization literacy assessment test, a standardized SciVis literacy assessment comprising 49 items based on 18 scientific visualizations and illustrations, spanning 8 techniques and 11 task types. We evaluate three closed-source and three open-source models under a closed-world protocol and compare their performance using data from 485 human participants. Results show that current MLLMs do not exhibit uniform SciVis literacy. Gemini is the strongest model overall, exceeding the human mean across the evaluated subsets, whereas the open-source models remain below the human baseline. Performance is highly uneven across techniques and tasks: models perform best on scientific illustration, search, and spatial understanding, but struggle on texture-based and integration-based visualizations and on quantitative estimation. Error analysis reveals recurring failures in fine-grained quantitative estimation, flow-direction interpretation, and grounded encoding interpretation. These findings position SciVis literacy as a necessary benchmark dimension for evaluating multimodal AI systems. Our code and model outputs are publicly available at https://github.com/patdmp/mllm-scivis-lit-benchmark.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) are increasingly used to interpret visualizations, yet current evaluations remain largely chart-centric and provide limited evidence of understanding of scient...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Benchmarking, Multimodal, Large, Language, Models, Scientific, Visualization, Literacy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15176v1) | [下载PDF](https://arxiv.org/pdf/2607.15176v1.pdf)

---

## [10. MedFailBench: A Clinician-Built Open-Source Benchmark for Medical AI Safety Boundary Inspection](https://arxiv.org/abs/2607.15166v1)

**作者**：Goktug Ozkan  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-07-16

### 📄 论文摘要

Most medical AI benchmarks measure whether a model knows the correct answer. MedFailBench asks a different question: which safety boundary failed? We present a clinician-built synthetic benchmark and failure atlas that labels medical AI errors by severity (1--5) and safety gate type (missed urgent escalation, unsafe remote dosing, unsafe discharge reassurance, evidence fabrication, unsafe protocol execution, source support gap). The current public release (v0.2.1) contains 44 clinician-reviewed synthetic cases with severity annotations, a live HuggingFace leaderboard preview, a safety gate taxonomy, a clinical severity rubric, and an automated pipeline for archiving model-response screening runs. No patient data, clinical validation claims, or model rankings are included. MedFailBench is released under Apache-2.0 and CC-BY-4.0 and carries the Zenodo DOI 10.5281/zenodo.21205535.

### 🤖 AI 总结

**一句话总结**：Most medical AI benchmarks measure whether a model knows the correct answer. MedFailBench asks a different question: which safety boundary failed? We present a clinician-built synthetic benchmark and ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MedFailBench, Clinician-Built, Open-Source, Benchmark, Medical, Safety, Boundary, Inspection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15166v1) | [下载PDF](https://arxiv.org/pdf/2607.15166v1.pdf)

---

## [11. The Industrialization of Research ; On AI-Driven Science and Its Consequences](https://arxiv.org/abs/2607.15164v1)

**作者**：Emmanuel Jeannot  
**分类**：cs.AI, cs.CY  
**发布时间**：2026-07-16

### 📄 论文摘要

Artificial intelligence is transforming scientific research -- not merely as a more powerful instrument, but as an autonomous participant in the research cycle itself. This transition constitutes, in the most precise sense of the term, the industrialization of research: a shift from a craft model, in which knowledge, method, and judgment are embedded in the researcher, to a pipeline model, in which these steps are decomposed, automated, and supervised. The US Department of Energy's Genesis Mission is the most ambitious current instantiation of this shift, but the fundamental questions it raises extend far beyond any single program. This essay examines seven such questions: the erosion of the intergenerational transmission of scientific competence; the growing opacity of AI-generated theories; the collapse of peer evaluation under a flood of machine-generated output; the unproven capacity of AI for paradigm-shifting discovery; the capture of the scientific agenda by political and industrial actors; the compounding of systematic errors in closed-loop pipelines; and the structural bifurcation of the global research community into incommensurable tiers. These concerns do not constitute an argument against AI-driven science -- whose demonstrated potential is real and significant. They constitute the conditions under which that potential can be responsibly pursued.

### 🤖 AI 总结

**一句话总结**：Artificial intelligence is transforming scientific research -- not merely as a more powerful instrument, but as an autonomous participant in the research cycle itself. This transition constitutes, in ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Industrialization, Research, AI-Driven, Science, Its, Consequences, Artificial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15164v1) | [下载PDF](https://arxiv.org/pdf/2607.15164v1.pdf)

---

## cs.CL

## [12. Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models](https://arxiv.org/abs/2607.15277v1)

**作者**：Patrik Wolf, Thomas Kleine Buening, Andreas Krause 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-16

### 📄 论文摘要

In-context learning is commonly interpreted as a form of conditional inference, in which the prompt specifies a context and the model's output is treated as an estimate of the corresponding conditional distribution. If this interpretation holds, then LLM estimates should satisfy basic probabilistic identities. In particular, the law of total probability asserts that prior-weighted conditional distributions aggregate into population-level marginals over any valid partition of the population. In this work, we investigate to what extent LLM estimates adhere to this self-consistency principle. We use binary trees as an evaluation scaffold to recursively partition a population into increasingly fine-grained subpopulations. We then prompt LLMs with verbalized subpopulation descriptions in context, aggregate the resulting estimates back into population-level estimates, and compare them across partitions of varying granularity. Applying this protocol across problem domains and state-of-the-art frontier models, we show widespread violations of basic consistency properties. An in-depth study of persona prompting reveals a pattern we call the macro fallacy: estimates reconstructed from more fine-grained subpopulation responses are often better aligned with human reference data than direct population-level estimates. This effect persists across variations in tree structure and estimation task, and can be partially recovered through implicit prompting. Together, these findings suggest that models possess relevant subpopulation knowledge but do not reliably propagate it into aggregate estimates. This gap establishes statistical self-consistency as an unsaturated, reference-free criterion for evaluating LLMs.

### 🤖 AI 总结

**一句话总结**：In-context learning is commonly interpreted as a form of conditional inference, in which the prompt specifies a context and the model's output is treated as an estimate of the corresponding conditiona...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Partition, Prompt, Aggregate, Statistical, Self-Consistency, Language, Models, In-context

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15277v1) | [下载PDF](https://arxiv.org/pdf/2607.15277v1.pdf)

---

## [13. SciDiagramEdit: Learning to Edit Scientific Diagrams from Paper Revisions](https://arxiv.org/abs/2607.15272v1)

**作者**：Yasheng Sun, Zezi Zeng, Yifan Yang 等 7 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-16

### 📄 论文摘要

Editing the figures in a research paper is a routine and time-consuming part of everyday research practice: authors relabel components, rearrange panels, and restyle visuals as they revise their manuscripts. Automating this editing workflow under a natural-language instruction, however, is challenging, because a scientific figure is a dense infographic in which heterogeneous visual elements such as schematics, plots, photos, captions, and arrows are composed under a tight visual grammar to advance a specific argument. To address this, we present SciDiagramEdit, a benchmark and skill-evolution framework that learns from natural paper revisions and operates on the figure's editable vector source, where users can inspect and co-edit individual primitives alongside the agent. Our benchmark mines before/after figure pairs from arXiv version histories, each grounded in the authors' own revision intent. To accommodate the diversity of editing instructions, we adopt agentic learning via skill evolution: an agentic proposer continually refines the agent's skill specification from execution traces over multiple epochs. The resulting skill progressively lifts edit accuracy on a held-out validation set, providing evidence that natural paper revisions are an effective training signal for instruction-driven figure editing.

### 🤖 AI 总结

**一句话总结**：Editing the figures in a research paper is a routine and time-consuming part of everyday research practice: authors relabel components, rearrange panels, and restyle visuals as they revise their manus...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SciDiagramEdit, Learning, Edit, Scientific, Diagrams, Paper, Revisions, Editing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15272v1) | [下载PDF](https://arxiv.org/pdf/2607.15272v1.pdf)

---

## [14. Beyond the Leaderboard: Design Lessons for Trustworthy Multimodal VQA](https://arxiv.org/abs/2607.15241v1)

**作者**：Sushant Gautam, Vajira Thambawita, Michael A. Riegler 等 5 位作者  
**分类**：cs.CL, cs.CV  
**发布时间**：2026-07-16

### 📄 论文摘要

Healthcare multimodal AI must combine visual and textual evidence while remaining reliable and interpretable. Using MediaEval Medico 2025 as a retrospective GI endoscopy case study, we analyze design choices across nine documented systems for question answering and explanation quality. Parameter-efficient adaptation of pretrained backbones provides strong challenge performance, but answer-level gains do not consistently translate into faithful and complete clinical reasoning. Methods enforcing structured reasoning and explicit grounding show more reliable behavior across heterogeneous question types, although the evidence is correlational rather than ablation-based. These results motivate evaluation beyond lexical overlap, standardized evidence-linked explanations, leakage-aware data governance, and lightweight robustness and calibration checks. The findings support trustworthy multimodal healthcare AI based on data fusion, explainability, and resilient evaluation.

### 🤖 AI 总结

**一句话总结**：Healthcare multimodal AI must combine visual and textual evidence while remaining reliable and interpretable. Using MediaEval Medico 2025 as a retrospective GI endoscopy case study, we analyze design ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Leaderboard, Design, Lessons, Trustworthy, Multimodal, VQA, Healthcare

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15241v1) | [下载PDF](https://arxiv.org/pdf/2607.15241v1.pdf)

---

## [15. TikStance: A Multimodal and Hierarchical Dataset for Multi-target Stance Analysis in TikTok Political Conversations](https://arxiv.org/abs/2607.15240v1)

**作者**：Yazhi Zhang, Fuqiang Niu, Bowen Zhang  
**分类**：cs.CL  
**发布时间**：2026-07-16

### 📄 论文摘要

Political discourse has increasingly moved to short-video platforms, yet computational analysis of such content remains constrained by the scarcity of datasets that jointly preserve audiovisual information and hierarchical conversations. Here we present TikStance, a multimodal and context-aware dataset comprising 161 videos and 13,876 comments from TikTok, designed for stance detection in political discussions. The dataset covers three major political figures in the 2024 U.S. election cycle--Donald Trump, Joe Biden, and Kamala Harris--with content collected between September 2023 and January 2025. Each discussion unit links a host video and its metadata to a parent-linked comment tree, enabling stance analysis within both audiovisual and conversational context. Each item was independently labeled by three annotators using a three-class scheme (Favor, Against, None) for video-to-target and comment-to-target stance; items with disagreement were re-annotated, and the final Krippendorff's \(α\) reached 0.743, 0.723, and 0.722 for the Trump, Biden, and Harris subsets, respectively. Descriptive analysis further reveals target-dependent differences in stance distributions and conversational depth, with nested replies accounting for 23.3\% of all comments. By combining multi-target coverage, hierarchical conversations, and reliable multi-level human annotations, TikStance supports research in multimodal stance detection, political communication, computational social science, and context-aware natural language processing.

### 🤖 AI 总结

**一句话总结**：Political discourse has increasingly moved to short-video platforms, yet computational analysis of such content remains constrained by the scarcity of datasets that jointly preserve audiovisual inform...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TikStance, Multimodal, Hierarchical, Dataset, Multi-target, Stance, Analysis, TikTok

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15240v1) | [下载PDF](https://arxiv.org/pdf/2607.15240v1.pdf)

---

## [16. Language Identification via Compositional Data Analysis: A Linear-Time Classifier Based on Log-Ratio Geometry](https://arxiv.org/abs/2607.15238v1)

**作者**：Paul-Andrei Pogăcean, Sanda-Maria Avram  
**分类**：cs.CL  
**发布时间**：2026-07-16

### 📄 论文摘要

Language identification is commonly addressed using either neural architectures or statistical n-gram models. Neural approaches typically require substantial computational resources, whereas classical frequency-based methods offer efficient linear-time performance, but rely on distance metrics that are not always appropriate for compositional data.   This work models character and bigram frequency distributions as compositional vectors constrained to the simplex and mapped via the centered log-ratio (CLR) transformation bijectively onto the $(D-1)$-dimensional zero-sum subspace of $\mathbb{R}^D$, where Euclidean distances correspond to Aitchison distances. A pipeline is proposed, combining CLR-transformed unigram and bigram features with Laplace smoothing to address sparsity. The method is evaluated on six languages.   Experimental results show that the proposed approach achieves robust accuracy across different text lengths, with strong performance for longer sequences. These findings indicate that compositional representations provide a deterministic and computationally efficient alternative for language identification, particularly in settings where interpretability and low resource consumption are essential.

### 🤖 AI 总结

**一句话总结**：Language identification is commonly addressed using either neural architectures or statistical n-gram models. Neural approaches typically require substantial computational resources, whereas classical...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Language, Identification, via, Compositional, Data, Analysis, Linear-Time, Classifier

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15238v1) | [下载PDF](https://arxiv.org/pdf/2607.15238v1.pdf)

---

## [17. Linear representations of grammaticality in neural language models](https://arxiv.org/abs/2607.15175v1)

**作者**：Jane Li, Najoung Kim  
**分类**：cs.CL  
**发布时间**：2026-07-16

### 📄 论文摘要

Whether neural language models (NLMs) possess the ability to distinguish strings on the basis of their grammaticality remains a debated topic in the computational linguistics literature. Existing evidence has largely relied on probability-based measures, testing whether models assign higher probabilities to grammatical than ungrammatical strings. However, probability comparisons have been criticized as a measure for grammatical knowledge based on the assumption that grammaticality is inherently entangled with likelihood. Model-assigned probability is a function of many related sentence properties, such as lexical frequency, plausibility, and world knowledge. In this work, we move beyond probability-based evaluations and investigate whether grammaticality is encoded in the internal representations of NLMs. Using mass-mean probing, we test whether grammatical and ungrammatical sentences are systematically separated in representational space. We further examine the extent to which these representations are independent of sentence properties that are correlated with grammaticality, as well as their generalization across grammatical phenomena and languages. Our results provide evidence that grammaticality is robustly encoded in sentence representations of a wide range of pretrained NLMs, yielding clear representational separation on the dimension of grammaticality that cannot be fully explained by alternative sentence-level factors. Moreover, this encoding generalizes across a broad range of grammatical phenomena and to some degree, across languages, suggesting that grammaticality constitutes a coherent representational dimension in contemporary NLMs. These findings contribute new evidence to debates about the nature of syntactic knowledge in language models and offer a complementary framework for evaluating grammatical competence that is not dependent on string probabilities alone.

### 🤖 AI 总结

**一句话总结**：Whether neural language models (NLMs) possess the ability to distinguish strings on the basis of their grammaticality remains a debated topic in the computational linguistics literature. Existing evid...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Linear, representations, grammaticality, neural, language, models, Whether

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15175v1) | [下载PDF](https://arxiv.org/pdf/2607.15175v1.pdf)

---

## [18. Grokipedia vs Wikipedia: An LLM-Based Audit of Political Neutrality along Ideologies](https://arxiv.org/abs/2607.15146v1)

**作者**：Filippos Vlahos, Guillaume Bied, Tijl De Bie  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-07-16

### 📄 论文摘要

Online encyclopedias shape political opinion and, through it, democratic discourse. In late 2025, Grokipedia was released, an encyclopedia written entirely by the LLM Grok. One motivation behind the project was to provide an unbiased alternative to Wikipedia, which has faced accusations of "left-wing" and "liberal" bias. But does an encyclopedia written by an LLM deliver greater neutrality, or does it simply embed a different ideology? We conduct a large-scale political bias study on Grokipedia and Wikipedia, analysing 1,394 article pairs describing members of government for neutrality along nine expert-coded ideology dimensions employing four LLM judges, Grok, Claude, Mistral, and DeepSeek. As the LLMs could themselves be biased, we also investigate patterns in their judgments. We find all LLM-judges, including Grok, to rate Grokipedia less neutral than Wikipedia. Both encyclopedias are rated as portraying politicians favourably overall, but towards different ideological groups. Grokipedia particularly favours economically right-wing politicians and penalises socially liberal ones, while Wikipedia is rated as favourably biased towards the latter.

### 🤖 AI 总结

**一句话总结**：Online encyclopedias shape political opinion and, through it, democratic discourse. In late 2025, Grokipedia was released, an encyclopedia written entirely by the LLM Grok. One motivation behind the p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：vs, An, of, Grokipedia, Wikipedia, LLM-Based, Audit, Political

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15146v1) | [下载PDF](https://arxiv.org/pdf/2607.15146v1.pdf)

---

## cs.CV

## [19. Hierarchical Denoising For Multi-Step Visual Reasoning](https://arxiv.org/abs/2607.15278v1)

**作者**：Zezhong Qian, Xiaowei Chi, Chak-Wing Mak 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-16

### 📄 论文摘要

Video models are evolving into vision foundation models, yet they still lack human-like multi-step reasoning. Streaming autoregressive diffusion models are efficient but limited in reasoning, while bidirectional diffusion enables global revision with high inference costs due to dense frame-level denoising. Both paradigms struggle to achieve logical consistency and low-latency streaming for complex reasoning tasks. We propose HDR (Hierarchical Denoising for Visual Reasoning), a unified framework that integrates hierarchical latents into causal video generation for multi-step reasoning. HDR organizes video latents into a tree-structured hierarchy, enabling coarse-to-fine reasoning before streaming output. Coarse denoising layers preserve uncertain hypotheses for global planning, while finer layers progressively refine them into concrete visual states. A sparse hierarchical attention pattern (SHAP) further reduces temporal attention costs. We introduce a level-stratified multi-step video reasoning benchmark with out-of-distribution cases, covering six tasks: maze navigation, Tower of Hanoi, one-line drawing, sliding puzzle, Sokoban, and water pouring. Compared with streaming autoregressive diffusion baselines, HDR improves success from 34.22 to 60.29 (76.2% relative gain) and increases average progress from 76.00 to 89.56, demonstrating more consistent reasoning trajectories. HDR maintains low-latency streaming at 0.70 seconds per latent, achieving 54.2 times faster inference than bidirectional diffusion. It also retains 82.9% of full-data performance with only 2% training data, compared with 52.0% for bidirectional diffusion. Real-world robot experiments further demonstrate HDR's potential for physical interaction and world modeling. Project demo: https://hierarchical-diffusion-reasoning.github.io/.

### 🤖 AI 总结

**一句话总结**：Video models are evolving into vision foundation models, yet they still lack human-like multi-step reasoning. Streaming autoregressive diffusion models are efficient but limited in reasoning, while bi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hierarchical, Denoising, Multi-Step, Visual, Reasoning, Video, models, evolving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15278v1) | [下载PDF](https://arxiv.org/pdf/2607.15278v1.pdf)

---

## [20. Online Neural Space Time Memory for Dynamic Novel View Synthesis](https://arxiv.org/abs/2607.15271v1)

**作者**：Baback Elmieh, Lynn Tsai, Zeman Li 等 11 位作者  
**分类**：cs.CV, cs.GR, cs.LG  
**发布时间**：2026-07-16

### 📄 论文摘要

Online novel view synthesis from multi-view streaming videos faces a fundamental trade-off: maintaining a persistent, long-horizon memory to reconstruct temporarily occluded regions while operating under strict real-time constraints. While Test-Time Training (TTT) offers a powerful memory mechanism, standard models mandate gradient-based memory updates at every frame to adapt to the changing motion in dynamic scenes. The computational cost of heavy memory updates precludes real-time application and can lead to instability over long contexts. Given that memory updates are more demanding than memory application and video content is largely redundant, we propose to decouple the frequencies of these two processes. Our approach performs periodic memory updates while applying the memory on a per-frame basis, using cross-view attention to manage deformations between the prior memory state and the current frame. To lock in the historical context, we introduce two critical mechanisms: an auxiliary Memory Loss that forces persistent internalization of the scene, and a Memory Caching strategy that regularizes active weights against catastrophic drift. Our method demonstrates real-time, state-of-the-art performance on scenes with dynamic human motion as well as minute-scale online memorization.

### 🤖 AI 总结

**一句话总结**：Online novel view synthesis from multi-view streaming videos faces a fundamental trade-off: maintaining a persistent, long-horizon memory to reconstruct temporarily occluded regions while operating un...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Online, Neural, Space, Time, Memory, Dynamic, Novel, View

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15271v1) | [下载PDF](https://arxiv.org/pdf/2607.15271v1.pdf)

---

## [21. Motion-Conditioned Multi-View Fusion for Myocardial Infarction Localization from Echocardiography](https://arxiv.org/abs/2607.15268v1)

**作者**：Guang Yang, Wentian Xu, Siyu Wang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-16

### 📄 论文摘要

Myocardial infarction (MI) remains a leading cause of mortality worldwide. Echocardiography (Echo) is a widely available modality for MI assessment, where regional wall motion abnormality is a key indicator. Prior learning based methods for myocardial motion analysis often use handcrafted descriptors or densely supervised estimation, but the need for extensive annotation limits applicability. Foundation models have recently improved vision-based Echo analysis; however, most methods operate on single views and segment-level localization remains unreliable under view-dependent ambiguity, especially in apical views. To address this, we propose MCF-Net, a novel motion-guided multi-view fusion framework that fuses myocardial motion cues with foundation model representations to localize infarction. Visual features are extracted using EchoPrime, a pretrained Echo foundation model shared across dual views. Cardiac motion is modeled with extremely sparse supervision: a single annotated template frame is transferred across videos to initialize point tracking, avoiding dense labels. Motion-derived segment-aware soft masks provide coarse spatial priors that selectively enhance features for challenging myocardial segments. A motion-conditioned fusion mechanism then integrates motion and vision across views, refining predictions without overriding strong appearance cues. On segment-level MI localization, MCF-Net achieves 72.4\% F1 and 84.9\% accuracy, outperforming state-of-the-art motion-only, vision-only, and fusion baselines.

### 🤖 AI 总结

**一句话总结**：Myocardial infarction (MI) remains a leading cause of mortality worldwide. Echocardiography (Echo) is a widely available modality for MI assessment, where regional wall motion abnormality is a key ind...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MI, Motion-Conditioned, Multi-View, Fusion, Myocardial, Infarction, Localization, Echocardiography

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15268v1) | [下载PDF](https://arxiv.org/pdf/2607.15268v1.pdf)

---

## [22. ARMOR++: Agentic Orchestration of a Multi-Domain Primitive Set for Transferable Attacks on Deepfake Detectors](https://arxiv.org/abs/2607.15246v1)

**作者**：Christos Korgialas, Gabriel Lee Jun Rong, Dion Jia Xu Ho 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-16

### 📄 论文摘要

The reliability of deepfake detectors frequently degrades under black-box adversarial transfer, as these models often rely on fragile, architecture-dependent forensic cues. Existing transfer attacks often lack semantic awareness and struggle to maintain effectiveness under strict no-query constraints, particularly when perturbations are transferred from convolutional surrogates to transformer-based targets. To address these limitations, this paper introduces ARMOR++, a robust multi-agent framework designed for high-transferability deepfake evasion. The framework leverages the Qwen2.5-VL Vision-Language Model (VLM) to supply spatial semantic priors, while the Qwen3 Large Language Model (LLM) orchestrates primitive selection, adaptive hyperparameter reparameterization, and entropy-regularized perturbation mixing. By integrating five complementary primitives, spanning dense optimization, saliency-based methods, spatial transformations, frequency-domain perturbations, and block-structured modifications, ARMOR++ effectively targets heterogeneous inductive biases. Rigorous evaluation on the AADD-2025 benchmark demonstrates that ARMOR++ significantly outperforms existing agentic and non-agentic baselines across both low- and high-quality image regimes. Statistical analysis confirms a substantial gain in blind-target Attack Success Rate (ASR) over the state-of-the-art agentic baseline, with further performance advantages evidenced against non-agentic benchmarks and under robust defensive configurations. These findings highlight a significant residual reliability gap in current deepfake detector deployments and demonstrate the efficacy of agentic orchestration in identifying latent vulnerabilities.

### 🤖 AI 总结

**一句话总结**：The reliability of deepfake detectors frequently degrades under black-box adversarial transfer, as these models often rely on fragile, architecture-dependent forensic cues. Existing transfer attacks o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, ARMOR++, Agentic, Orchestration, Multi-Domain, Primitive, Set, Transferable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15246v1) | [下载PDF](https://arxiv.org/pdf/2607.15246v1.pdf)

---

## [23. CRISP: Constrained Refinement via Iterative Squeezing Process for Robust Medical Image Segmentation under Domain Shift](https://arxiv.org/abs/2607.15231v1)

**作者**：Yizhou Fang, Pujin Cheng, Yixiang Liu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-16

### 📄 论文摘要

Distribution shift in medical imaging remains a central bottleneck for the clinical translation of medical AI. Failure to address it can lead to severe performance degradation in unseen environments and exacerbate health inequities. Existing methods for domain adaptation are inherently limited by exhausting predefined possibilities through simulated shifts or pseudo-supervision. Such strategies struggle in the open-ended and unpredictable real world, where distribution shifts are effectively infinite. To address this challenge, we adopt the "Rank Stability of Positive Regions" as a working assumption under distribution shift, and use it to derive robust spatial hints for source-only segmentation. Guided by this assumption, we propose CRISP, a model-agnostic framework that, unlike deployment-time adaptation, requires no test-time parameter updates and no target-domain data--a target-free, plug-in refinement framework that segments with frozen weights. Rather than using ranking to directly output masks, CRISP exploits the stability of probability rankings under distribution shift to derive robust spatial priors. Via latent feature perturbation, perturbation-invariant high-grade regions define a high-precision (HP) core, while voxels that remain potentially foreground under at least one perturbation define a high-recall (HR) support; these dual priors are then recursively refined under perturbation. We then design an iterative training framework that progressively squeezes HP and HR toward the final segmentation. Extensive evaluations on multi-center cardiac MRI and CT-based lung vessel segmentation demonstrate CRISP's superior robustness, significantly outperforming state-of-the-art methods with striking HD95 reductions of up to 0.14 (7.0% improvement), 1.90 (13.1% improvement), and 8.39 (38.9% improvement) pixels across multi-center, demographic, and modality shifts, respectively.

### 🤖 AI 总结

**一句话总结**：Distribution shift in medical imaging remains a central bottleneck for the clinical translation of medical AI. Failure to address it can lead to severe performance degradation in unseen environments a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CRISP, Constrained, Refinement, via, Iterative, Squeezing, Process, Robust

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15231v1) | [下载PDF](https://arxiv.org/pdf/2607.15231v1.pdf)

---

## [24. Structural-Semantic Reciprocal Learning for Unsupervised Visible-Infrared Person Re-Identification](https://arxiv.org/abs/2607.15220v1)

**作者**：Moyao Tian, Shijia Liu, Yan Yang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-16

### 📄 论文摘要

Unsupervised visible-infrared person re-identification (USVI-ReID) is challenging due to the large modality gap and the lack of cross-modal identity annotations. Progressive association paradigms have been proposed to gradually bridge the gap, but they suffer from two critical bottlenecks: reliance on ambiguous global representations and unchecked propagation of pseudo-label noise in an open-loop manner. To address these issues, we propose Structural-Semantic Reciprocal Learning (SSRL), a framework that transforms open-loop association into a self-correcting closed-loop system. Structurally, we introduce Fine-grained Structural Decoupling (FSD) to extract discriminative body-part primitives as reliable spatial anchors, complementing ambiguous holistic silhouettes with spatially consistent structural details. Semantically, we design a Closed-loop Semantic Calibration (CSC) mechanism that reconstructs shared semantic prototypes at each epoch and feeds them back into the training loop, effectively filtering pseudo-label noise before the next clustering cycle. Through the reciprocal interaction between structural and semantic learning, SSRL achieves robust cross-modal representation. Extensive experiments demonstrate the competitive performance of SSRL against state-of-the-art USVI-ReID methods on both SYSU-MM01 and RegDB, notably surpassing several supervised counterparts on RegDB.

### 🤖 AI 总结

**一句话总结**：Unsupervised visible-infrared person re-identification (USVI-ReID) is challenging due to the large modality gap and the lack of cross-modal identity annotations. Progressive association paradigms have...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Structural-Semantic, Reciprocal, Learning, Unsupervised, Visible-Infrared, Person, Re-Identification, USVI-ReID

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15220v1) | [下载PDF](https://arxiv.org/pdf/2607.15220v1.pdf)

---

## [25. Symbal: Detecting Systematic Misalignments in Model-Generated Captions](https://arxiv.org/abs/2607.15216v1)

**作者**：Maya Varma, Jean-Benoit Delbrouck, Sophie Ostmeier 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-16

### 📄 论文摘要

Multimodal large language models (MLLMs) often introduce errors when generating image captions, resulting in misaligned image-text pairs. Our work focuses on a class of captioning errors that we refer to as systematic misalignments, where a recurring error in MLLM-generated captions is closely associated with the presence of a specific visual feature in the paired image. Given a vision-language dataset with MLLM-generated captions, our aim in this work is to detect such errors, a task we refer to as systematic misalignment detection. As our first key contribution, we present Symbal, which utilizes a structured, dual-stage setup with off-the-shelf foundation models to identify systematic misalignments and summarize results in natural language. As our second key contribution, we introduce SymbalBench, a benchmark designed to evaluate automated methods on our proposed task. SymbalBench consists of 1.7 million image-text pairs from two domains (natural and medical images), organized into 420 vision-language datasets with annotated systematic misalignments. Symbal exhibits strong performance on this benchmark, correctly identifying systematic misalignments in 63.8% of datasets, a nearly 4x improvement over the closest baseline. We supplement our evaluations on SymbalBench with real-world evaluations, showing that (1) Symbal can accurately surface systematic misalignments in captions generated by four MLLMs and (2) Symbal is a powerful tool for auditing off-the-shelf image-caption datasets. Ultimately, our novel task, method, and benchmark can aid users with auditing MLLM-generated captions and identifying critical errors, without requiring access to the underlying MLLM. Code is available at https://github.com/Stanford-AIMI/Symbal.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) often introduce errors when generating image captions, resulting in misaligned image-text pairs. Our work focuses on a class of captioning errors that we refer...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Symbal, Detecting, Systematic, Misalignments, Model-Generated, Captions, Multimodal, large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15216v1) | [下载PDF](https://arxiv.org/pdf/2607.15216v1.pdf)

---

## [26. MAGiSt3R: Multi-Agent Feed-forward 3D Reconstruction from Monocular RGB Videos](https://arxiv.org/abs/2607.15211v1)

**作者**：Ziren Gong, Xiaohan Li, Fabio Tosi 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-16

### 📄 论文摘要

This paper presents MAGiSt3R, a multi-agent 3D reconstruction framework performing reconstruction and camera tracking for monocular RGB videos at almost 10 FPS. MAGiSt3R relies on a feed-forward model from the 3R family to process RGB videos and regress local point maps, and on a merging model, MAGMA, that combines local maps at both intra-agent and inter-agent levels to obtain the final global point map. Furthermore, MAGiSt3R performs pose graph optimization to mitigate cumulative camera drift occurring along the feed-forward pipeline. We evaluate MAGiSt3R on both synthetic and real-world datasets, demonstrating its superior reconstruction and camera tracking accuracy compared to state-of-the-art approaches.

### 🤖 AI 总结

**一句话总结**：This paper presents MAGiSt3R, a multi-agent 3D reconstruction framework performing reconstruction and camera tracking for monocular RGB videos at almost 10 FPS. MAGiSt3R relies on a feed-forward model...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, 3D, MAGiSt3R, Feed-forward, Reconstruction, Monocular, RGB, Videos

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15211v1) | [下载PDF](https://arxiv.org/pdf/2607.15211v1.pdf)

---

## cs.LG

## [27. Mutable Low-Rank Sketches for Retrain-Free Recommendation](https://arxiv.org/abs/2607.15242v1)

**作者**：Hector J. Garcia, Nick Clayton  
**分类**：cs.LG  
**发布时间**：2026-07-16

### 📄 论文摘要

A common bottleneck in two-stage recommendation is embedding staleness: when a user rates a new item, their embedding remains fixed until the next retrain cycle. We propose mutable sketches, which store each user's preferences in a KP-tree (a sparse segment tree with sum aggregation), fit a low-rank projection once, and recompute embeddings on-the-fly as ratings arrive. We prove that each new observation monotonically tightens the prediction error envelope (Theorem 1), a guarantee that FunkSVD and eALS lack. On KuaiRec, the mutable sketch achieves 0.810 RMSE at 1.8% data read vs. ALS 0.822 at 100%, with 8x faster per-batch updates. A new user receives personalized recommendations in <1 ms after their first rating, with no model retraining required. A comparison of sampling strategies across density regimes shows that the KP-tree's norm-proportional sampling provides 40-130% better item coverage on sparse data (<1% density), while uniform sampling suffices on dense matrices.

### 🤖 AI 总结

**一句话总结**：A common bottleneck in two-stage recommendation is embedding staleness: when a user rates a new item, their embedding remains fixed until the next retrain cycle. We propose mutable sketches, which sto...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mutable, Low-Rank, Sketches, Retrain-Free, Recommendation, common, bottleneck, two-stage

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15242v1) | [下载PDF](https://arxiv.org/pdf/2607.15242v1.pdf)

---

## [28. Data Driven Block Replacement Scheduling](https://arxiv.org/abs/2607.15229v1)

**作者**：Aniruddhan Ganesaraman, VIdyadhar Kulkarni  
**分类**：cs.LG, math.OC, stat.AP, stat.ML  
**发布时间**：2026-07-16

### 📄 论文摘要

We develop data-driven algorithms for maintaining $N$ independent identical machines under a \textit{block replacement policy}, in which each machine is replaced upon failure and all machines are jointly replaced at regular intervals of length $k$. The goal is to learn the cost-minimizing interval $k^*$ from operational data when the lifetime distribution is unknown. At each decision epoch, the operator selects $k \in \{1, 2, \ldots, K\}$, observes the resulting failure history (a mixture of complete and right-censored lifetimes) and incurs a per-unit-time cost governed by the renewal function. We formulate this as a stochastic multi-armed bandit and propose Hoeffding- and Bernstein-based lower-confidence-bound algorithms achieving $O(K \log T)$ regret, matching the Lai--Robbins lower bound. Exploiting a nested observation property unique to block replacement, correlated variants attain $O((K-k^*)\log T)$ regret and require only $O(1)$ direct pulls of suboptimal arms $k < k^*$. A complementary Kaplan--Meier renewal algorithm estimates the lifetime distribution nonparametrically from censored data, achieving almost-sure policy consistency and empirically near-zero incremental regret at long horizons. We additionally analyze two average-cost MDPs: a time-elapsed formulation establishing that block replacement is optimal within its policy class for any lifetime distribution, and an age-vector formulation proving a monotone threshold structure under increasing failure rate distributions and providing a gold-standard cost benchmark. Numerical experiments confirm the theoretical ordering and reveal structural cost gaps between optimal block and age-dependent replacement.

### 🤖 AI 总结

**一句话总结**：We develop data-driven algorithms for maintaining $N$ independent identical machines under a \textit{block replacement policy}, in which each machine is replaced upon failure and all machines are join...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Data, Driven, Block, Replacement, Scheduling, develop, data-driven

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15229v1) | [下载PDF](https://arxiv.org/pdf/2607.15229v1.pdf)

---

## [29. BadWAM: When World-Action Models Dream Right but Act Wrong](https://arxiv.org/abs/2607.15207v1)

**作者**：Qi Li, Xingyi Yang, Xinchao Wang  
**分类**：cs.LG, cs.RO  
**发布时间**：2026-07-16

### 📄 论文摘要

World-action models (WAMs) are emerging as a promising foundation for embodied control: rather than predicting actions alone, they learn representations that couple action generation with future world prediction. This coupling is often viewed as a source of robustness, interpretability, and safety, as a robot's action can in principle be checked against its imagined future. In this paper, we show that this assumption is fragile. We introduce BadWAM, a unified framework for modeling and evaluating World-Action Drift Attacks: a new class of WAM-specific adversarial attacks that use small visual perturbations to break the alignment between what a WAM imagines and what it executes. BadWAM characterizes this attack surface along two natural criteria: attack strength and stealthiness. When the adversary prioritizes disruption, BadWAM instantiates an action-only adversarial attack, which directly drives the model toward task-failing actions. When the adversary additionally prioritizes stealth, BadWAM instantiates an imagination-preserving adversarial attack, which seeks to induce harmful action shifts while keeping the model's predicted future close to its clean imagination. Together, these two attacks capture a spectrum of WAM-specific failures: from overt action hijacking to stealthier cases where the model appears to imagine a plausible future but executes a desynchronized action. We evaluate BadWAM across different variants of WAMs. Results show that our attacks substantially reduce task success rates under closed-loop execution. For example, our action-only attack reduces the model performance from 96.5% to 43.1% success. The results of our imagination-preserving attack further exposes a WAM-specific vulnerability: moderate future-preserving regularization can maintain strong attack performance while reducing future imagination drift.

### 🤖 AI 总结

**一句话总结**：World-action models (WAMs) are emerging as a promising foundation for embodied control: rather than predicting actions alone, they learn representations that couple action generation with future world...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BadWAM, When, World-Action, Models, Dream, Right, but, Act

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15207v1) | [下载PDF](https://arxiv.org/pdf/2607.15207v1.pdf)

---

## [30. RTS Smoother-Guided Learning of Physics-Based Neural Differential Models](https://arxiv.org/abs/2607.15180v1)

**作者**：Ahmet Demirkaya, Georgios Stratis, Tales Imbiriba 等 5 位作者  
**分类**：cs.LG, eess.SY  
**发布时间**：2026-07-16

### 📄 论文摘要

Ordinary differential equations (ODEs) are widely used to model dynamical systems in physics, biology, neuroscience, and physiology, but in many applications some equations of the dynamics are unknown and only a subset of the state variables are measured. We propose a hybrid neural--physics framework in which the known components of the ODE are kept explicit and the missing components are represented by a neural network. The proposed method consists of two stages where we alternate between state and parameter estimation and iterate until a predetermined criterion is met. Specifically, in the first step, we treat the model parameters as being known and we infer the latent states from the available measurements using a Rauch--Tung--Striebel (RTS) smoother. In the second stage, we treat the smoothed trajectories as being known and use them to estimate the neural networks' parameters through backpropagation. We evaluate the method on benchmark systems spanning linear, nonlinear, and stiff dynamics under partial state observation. Across these settings, the proposed method learns missing ODE components from incomplete measurements while exploiting and retaining interpretable mechanistic structure and improving latent-state reconstruction and long-horizon prediction.

### 🤖 AI 总结

**一句话总结**：Ordinary differential equations (ODEs) are widely used to model dynamical systems in physics, biology, neuroscience, and physiology, but in many applications some equations of the dynamics are unknown...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, RTS, Smoother-Guided, Learning, Physics-Based, Neural, Differential, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.15180v1) | [下载PDF](https://arxiv.org/pdf/2607.15180v1.pdf)

---

