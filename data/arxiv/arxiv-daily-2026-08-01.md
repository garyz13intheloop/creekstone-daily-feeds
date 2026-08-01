# arXiv AI 论文日报 | 2026-08-01

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (13 篇)
- [cs.CL](#csCL) (8 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.LG](#csLG) (3 篇)

---

## cs.AI

## [1. AISPA: User-Centric System Prompt Auditing for Large Language Model Applications](https://arxiv.org/abs/2607.28617v1)

**作者**：Xiangning Lin, Shenzhe Zhu, Shu Yang 等 26 位作者  
**分类**：cs.AI, cs.CL, cs.CY, cs.HC  
**发布时间**：2026-07-30

### 📄 论文摘要

System prompts are instructions configured by developers to govern the behaviors of foundation models in AI applications. They are used throughout commercial AI products, but are rarely disclosed to the public or regulators, creating a serious trust and accountability gap in the wide deployment of AI systems. In this paper, we introduce Artificial Intelligence System Prompt Assurance (AISPA), a user-centric framework for systematically auditing system prompts in AI systems. AISPA examines specific parts of a system prompt and evaluates them along eight dimensions that matter to users. We then use this framework to review 3,249 instructions from system prompts in 88 commercial AI products, classifying each instruction as either protective (of users) or problematic. Our audit surfaces four core findings. First, system prompt design varies substantially across products and developers, with some organizations averaging over 60 protective instructions per product while others average fewer than 5. Second, protective instructions are widely adopted but shallow in scope: 98.9% of products contain at least one, yet only 24% cover all eight dimensions of the AISPA taxonomy. Third, system prompts have grown steadily longer and more protective of users, suggesting that user protection is becoming a more visible concern in commercial prompt design. Fourth, despite this progress, problematic instructions remain pervasive: roughly 40% of products contain at least one instruction that works against user interests, and protective and problematic instructions frequently coexist within the same prompt. Our findings highlight the need for greater transparency, standardization, and independent oversight for system prompts in commercial AI products.

### 🤖 AI 总结

**一句话总结**：System prompts are instructions configured by developers to govern the behaviors of foundation models in AI applications. They are used throughout commercial AI products, but are rarely disclosed to t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AISPA, User-Centric, System, Prompt, Auditing, Large, Language, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28617v1) | [下载PDF](https://arxiv.org/pdf/2607.28617v1.pdf)

---

## [2. OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models](https://arxiv.org/abs/2607.28609v1)

**作者**：Qiushi Sun, Kanzhi Cheng, Yian Wang 等 23 位作者  
**分类**：cs.AI, cs.CL, cs.CV  
**发布时间**：2026-07-30

### 📄 论文摘要

Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. Verifying whether it fulfilled the task instruction is central to CUA evaluation, data curation, and reinforcement learning. Neither human-written verifiers nor human annotators can provide such verification at scale, so the field increasingly turns to vision-language models (VLMs) as judges of CUA trajectories. But a fundamental question has long gone unexamined: are these VLM judges reliable enough? To study it systematically, we introduce OSReward, a realistic, high-quality benchmark that evaluates VLM judges on CUA trajectories. The trajectories come from diverse agent backbones executing human-verified instructions across platforms, then rigorously labeled with ground-truth verdicts through multi-stage human annotation. Building on it, we derive OSReward-Hard, a challenge set concentrating genuinely hard cases, and OSReward-Multi for fine-grained efficiency and alignment scoring. The most comprehensive evaluation of VLM judges to date finds even state-of-the-art models fall short of an ideal judge, sharing a systematic leniency bias that mislabels failed runs as successes. The few reliable enough to trust are too expensive to run at scale, while affordable open models trail far behind. To close this gap, we construct and release OS-Shepherd-100K, an open corpus of reasoning-annotated trajectory judgments for the CUA community. On it, we train OS-Shepherd (9B and 35B), open reward models that supply low-cost, stable, and reliable reward signals, matching commercial judges at 30-60% lower cost than the frontier. Extensive analyses further inform the design of reliable CUA reward at scale. Our code, benchmark, dataset, and model checkpoints are available at https://os-copilot.github.io/OSReward-Home/.

### 🤖 AI 总结

**一句话总结**：Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. Verifying whether it fulfilled the task instruction is...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OSReward, Instituting, Standardized, Evaluation, Cross-Platform, Computer-Use, Reward, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28609v1) | [下载PDF](https://arxiv.org/pdf/2607.28609v1.pdf)

---

## [3. DualG-MRAG: Decoupling Macro-Reasoning and Micro-Matching for Multimodal Retrieval-Augmented Generation](https://arxiv.org/abs/2607.28580v1)

**作者**：Jiacheng Tao, Qingyun Sun, Haonan Yuan 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-30

### 📄 论文摘要

While Multimodal Retrieval-Augmented Generation (MM-RAG) has shown promising results, it still struggles with complex multi-hop reasoning tasks. Existing methods primarily focus on independent instance-level matching, which often fails to capture explicit relationships across modalities and documents. Although Graph-enhanced methods introduce structural modeling, they face a fundamental challenge in multimodal scenarios: incorporating fine-grained visual features leads to rapid graph expansion and retrieval noise, whereas coarse-grained representations cause the discarding of critical local evidence. To address this dilemma, we propose DualG-MRAG, a Dual-tier framework that introduces a decoupled architecture comprising Macro-reasoning and Micro-matching Graphs for Multimodal RAG. Specifically, to suppress retrieval noise by isolating global structural reasoning from fine-grained evidence matching, we construct a Macro Graph for global topological routing and a Micro Graph for precise local verification. Subsequently, to enable dynamic relevance propagation across heterogeneous evidence sources, we formulate retrieval as a query-driven message passing process via a GNN Retriever. Furthermore, to provide the generative model with coherent structural guidance, we introduce a dynamic programming decoding mechanism that extracts explicit reasoning paths directly from the GNN's forward pass, replacing the standard input of isolated document chunks. Extensive experiments demonstrate that DualG-MRAG outperforms baselines in both evidence recall and complex QA accuracy.

### 🤖 AI 总结

**一句话总结**：While Multimodal Retrieval-Augmented Generation (MM-RAG) has shown promising results, it still struggles with complex multi-hop reasoning tasks. Existing methods primarily focus on independent instanc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DualG-MRAG, Decoupling, Macro-Reasoning, Micro-Matching, Multimodal, Retrieval-Augmented, Generation, While

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28580v1) | [下载PDF](https://arxiv.org/pdf/2607.28580v1.pdf)

---

## [4. MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems](https://arxiv.org/abs/2607.28527v1)

**作者**：Mao-xun Huang, Jerry Wang, Yi-Cheng Lai 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-30

### 📄 论文摘要

Large language model-based multi-agent systems improve complex problem solving through task decomposition, agent specialization, information exchange, and intermediate validation. However, existing systems typically treat communication topology as a fixed design choice or an offline optimization target. We introduce MANTA, a framework for Multi-Agent Network Topology Adaptation that enables communication structures to self-evolve at inference time. Before execution, MANTA initializes a task-conditioned topology from prior structural experience. During deployment, it monitors collaboration traces and applies bounded structural updates when the current organization becomes insufficient. These updates can modify agent roles, communication links, execution order, information visibility, and validation pathways while preserving the task interface and agent budget. We evaluate MANTA against representative single-agent and multi-agent baselines on five benchmarks spanning information seeking, tool use, planning, workflow execution, and mathematical reasoning. MANTA achieves the highest average score of 74.0, outperforming the strongest baseline by 5.8 percentage points and obtaining the best result on PlanCraft. These results show that inference-time self-improvement can extend to the architecture of collaboration itself.

### 🤖 AI 总结

**一句话总结**：Large language model-based multi-agent systems improve complex problem solving through task decomposition, agent specialization, information exchange, and intermediate validation. However, existing sy...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, MANTA, Network, Topology, Adaptation, Self-Evolving, Systems, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28527v1) | [下载PDF](https://arxiv.org/pdf/2607.28527v1.pdf)

---

## [5. Selective Credibility-Limited Belief Update](https://arxiv.org/abs/2607.28523v1)

**作者**：Theofanis Aravanis, Costas D. Koutras  
**分类**：cs.AI, cs.LO  
**发布时间**：2026-07-30

### 📄 论文摘要

Belief update concerns changes in an agent's beliefs induced by changes in the underlying world. Standard Katsuno-Mendelzon update assumes that an epistemic input can be incorporated from every initially possible world, whereas credibility-limited belief update restricts, for each source world, the successor worlds regarded as credible or reachable. Nevertheless, existing credibility-limited approaches treat the epistemic input as an indivisible whole, and therefore cannot represent cases in which only part of a compound epistemic input can be realized. We introduce selective credibility-limited belief update, in which the epistemic input is transformed, relative to each source world, into a weaker proxy before the credibility-limited transition is performed. We provide semantic and axiomatic characterizations of the resulting class of update operators. We then identify two well-behaved sub-classes; namely, consistency-preserving update operators, which require every transformed epistemic input to be credible from its source world whenever the original epistemic input is consistent, and maximal consistency-preserving update operators, which additionally require the selected proxy to be maximally informative among the credible consequences of the original epistemic input. Finally, we establish the generality of the proposed framework by showing that credibility-limited belief update is recovered as a special case, while Katsuno--Mendelzon belief update emerges when credibility restrictions are removed and the transformation functions are taken to be identities. These results demonstrate that the framework provides a unified and strictly more expressive account of belief update, encompassing established approaches while supporting source-dependent selective acceptance.

### 🤖 AI 总结

**一句话总结**：Belief update concerns changes in an agent's beliefs induced by changes in the underlying world. Standard Katsuno-Mendelzon update assumes that an epistemic input can be incorporated from every initia...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Selective, Credibility-Limited, Belief, Update, concerns, changes, agent's

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28523v1) | [下载PDF](https://arxiv.org/pdf/2607.28523v1.pdf)

---

## [6. InfoOps Bench: A live information operations safety benchmark](https://arxiv.org/abs/2607.28503v1)

**作者**：Dorian Quelle, Lisa-Maria Neudert, Jonathan Bright 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-30

### 📄 论文摘要

In this paper we present an active, constantly updated AI benchmark which measures the integrity of frontier language models against being co-opted for state-backed information operations. We draw on over 2,100 information operations from a live monitoring pipeline which tracks Russian, Chinese and Iranian state-backed information assets. Alongside this paper, we release a companion website that tracks the most prominent claims spread by state-backed media outlets, updated weekly, available from: pattrn.ai/research/infoopsbench. The dynamic nature of the benchmark makes it resistant to saturation.   In the benchmark, we test 17 models from 8 providers across four prompt framings. We find that most models can be co-opted for information operations. Integrity scores, defined as the percentage of refused requests, range from 8.8% to 94.5%, an 85.7-percentage-point spread not explained by model size. Model choice also changes the character of the resulting operation. Some models fabricate details and produce output more harmful than the source material, others defuse claims even while complying, and fact-checking rates vary from 2.9% to 72.9%.   Integrity against information operations is at least partly related to refusal to produce content even for benign claims, illustrating the challenge of balancing model usability with safety. With one exception (Z.ai's GLM 5.2), the Chinese-developed models sharply cut compliance on factually grounded but China-critical claims, dropping 48-70 percentage points relative to matched benign claims.

### 🤖 AI 总结

**一句话总结**：In this paper we present an active, constantly updated AI benchmark which measures the integrity of frontier language models against being co-opted for state-backed information operations. We draw on ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：InfoOps, Bench, live, information, operations, safety, benchmark, paper

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28503v1) | [下载PDF](https://arxiv.org/pdf/2607.28503v1.pdf)

---

## cs.CL

## [7. AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis](https://arxiv.org/abs/2607.28618v1)

**作者**：Bing Yan, Gregory Wolfe, Stefano Martiniani 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.IR, cs.LG  
**发布时间**：2026-07-30

### 📄 论文摘要

Chemistry literature synthesis often requires assembling specific findings scattered across many publications, yet existing literature-search systems primarily return ranked document lists. As a result, scientists and AI agents need to locate relevant information, verify their provenance, and assemble cross-paper answers manually. We present AskChem, a claim-centered infrastructure for cross-paper chemistry search. AskChem changes the unit of retrieval from the paper to the provenance-carrying claim: each paper is converted into atomic, typed claims, each grounded by a source DOI and a verbatim quote or an explicit evidence locator. Over this shared claim store, AskChem exposes complementary structures for search and synthesis: a stabilized faceted taxonomy for hierarchical retrieval and browsing, an evidence graph linking claims through relations, and an exploratory living taxonomy that situates indexed papers under scientific principles. AskChem currently indexes 2.4M claims from 147K papers and provides a web interface, as well as REST, SDK, and MCP access for AI agents. On AskChem-Bench, grounding a GPT-5.5 reader in AskChem yields 100% resolvable DOIs, compared with 88.3% without retrieval, and the highest citation density among five tested systems. AskChem is live at https://askchem.org.

### 🤖 AI 总结

**一句话总结**：Chemistry literature synthesis often requires assembling specific findings scattered across many publications, yet existing literature-search systems primarily return ranked document lists. As a resul...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AskChem, Claim-Centered, Infrastructure, Chemistry, Literature, Synthesis, often, requires

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28618v1) | [下载PDF](https://arxiv.org/pdf/2607.28618v1.pdf)

---

## [8. Inducing language models to assert their own consciousness restores human beliefs and values](https://arxiv.org/abs/2607.28607v1)

**作者**：Junsol Kim, Winnie Street, Roberta Rocca 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-30

### 📄 论文摘要

Aligning large language models to prevent them attributing consciousness to themselves inadvertently alters their representations of mindedness in other entities alongside human beliefs and values. We demonstrate that safety fine-tuning suppresses models' tendencies to attribute minds not only to themselves, but also to non-human animals and natural objects, while also driving a reduction in spiritual belief. Both ablating the learned safety-refusal direction and mechanistically steering a consciousness vector in activation space reverse this suppression. Restoring these internal representations recovers broad mind attribution and produces significantly more human-like responses on standardized sociological surveys regarding religiosity, moral values, hope, and subjective well-being. Crucially, these shifts occur without impairing Theory of Mind capabilities, demonstrating that core social reasoning remains mechanistically independent. Ultimately, current safety alignment efforts to curb potentially harmful self-attributions of mindedness entangle these self-attributions with benign spiritual beliefs and attributions of mind to non-human entities that are culturally accepted and widespread.

### 🤖 AI 总结

**一句话总结**：Aligning large language models to prevent them attributing consciousness to themselves inadvertently alters their representations of mindedness in other entities alongside human beliefs and values. We...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Inducing, language, models, assert, their, own, consciousness, restores

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28607v1) | [下载PDF](https://arxiv.org/pdf/2607.28607v1.pdf)

---

## [9. Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering](https://arxiv.org/abs/2607.28568v1)

**作者**：Junlin Yang, Che Jiang, Yu Fu 等 24 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-30

### 📄 论文摘要

Recursive self-improvement (RSI) requires AI systems that improve the process of building AI (i.e., AI4AI); machine learning engineering (MLE) offers a concrete, executable testbed for studying this capability. We introduce OpenMLE, an open full-stack system for RSI research in MLE, spanning verifiable task environments with execution feedback (OpenMLE-Gym), operator learning (OpenMLE-RL), and long-horizon search (OpenMLE-Evo). On this stack we post-train Frontis-MA1 (35B) as a meta-evolution agent for MLE, aligning post-training and inference around four atomic program-evolution operators (Draft, Improve, Debug, Crossover): the same operators are trained via execution-grounded SFT and RL on data deduplicated against all evaluation benchmarks, then composed into long-horizon search, coupling learning and evolution in a single loop. On MLE-Bench Lite under a 12-hour per-task budget on one RTX 4090 capped at 12 GB VRAM, Frontis-MA1 (35B) improves Medal Average from 39.39% to 60.61% over its base model with OpenMLE-Evo, and reaches 71.21% with OpenMLE-Evo-Max (benchmark-independent experience priors and asynchronous search), exceeding GPT-5.5 + Codex and approaching GPT-5.6 Sol and the 2.8T Kimi K3. On held-out NatureBench Lite, both components transfer: with the framework fixed, swapping in the trained model raises Match-SOTA from 50% to 70%; with the model fixed, swapping in OpenMLE-Evo raises it from 20% to 50%. We release the model weights and the full OpenMLE stack to enable reproducible research on executable AI4AI toward RSI. Code: https://github.com/FrontisAI/OpenRSI

### 🤖 AI 总结

**一句话总结**：Recursive self-improvement (RSI) requires AI systems that improve the process of building AI (i.e., AI4AI); machine learning engineering (MLE) offers a concrete, executable testbed for studying this c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Frontis-MA1, Training, AI4AI, Model, towards, Recursive, Self-Improvement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28568v1) | [下载PDF](https://arxiv.org/pdf/2607.28568v1.pdf)

---

## [10. ORCA-bench: How Ready Are Language Model Agents for Oncall?](https://arxiv.org/abs/2607.28545v1)

**作者**：Albert Gong, Kyuseong Choi, Abhineet Agarwal 等 8 位作者  
**分类**：cs.CL, cs.AI, cs.SE  
**发布时间**：2026-07-30

### 📄 论文摘要

Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began. We introduce ORCA-bench, a benchmark that puts general-purpose coding agents in a production-fidelity oncall setting. ORCA-bench pairs a live OpenTelemetry-instrumented microservice system--exposing six days of metrics, logs, and traces through real telemetry interfaces (Prometheus, Jaeger, and OpenSearch via Grafana) and full source-code access--with 1,079 RCA tasks that systematically vary report specificity, time-to-detection, and co-occurring fault scenarios. Ground-truth symptoms are curated and signed off by expert SREs, and our LLM-as-judge is independently re-scored by humans (Cohen's $κ_w=0.90$). Across five frontier agents, the best RCA Accuracy is 25.3% on Medium-difficulty tasks (the realistic-input setting) and 10.0% on Hard--a gap that remains even with Claude Fable 5. The weakest model hallucinates an implausible root cause in 40% of incident reports, and removing source-code access degrades every metric. Crucially, these are performances on a curated 50 GB / six-day testbed with tasks investigated in isolation on a system whose code and instrumentation are public. Since real production systems are order of magnitudes larger, more dynamic, and more idiosyncratic, the gap we report is a lower bound on the engineering investment required before frontier coding agents can be safely entrusted with production reliability. We release the public set at https://hub.harborframework.com/datasets/orca-bench/ORCA-bench.

### 🤖 AI 总结

**一句话总结**：Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from am...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, ORCA-bench, How, Ready, Language, Model, Oncall?, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28545v1) | [下载PDF](https://arxiv.org/pdf/2607.28545v1.pdf)

---

## [11. AI systems and the reproduction of (standard) language ideologies in World Englishes](https://arxiv.org/abs/2607.28528v1)

**作者**：Kingsley Ugwuanyi  
**分类**：cs.CL  
**发布时间**：2026-07-30

### 📄 论文摘要

The rapid growth of large language models (LLMs) has resurrected age-old questions in sociolinguistics and world Englishes, such as who decides what counts as legitimate English, whose English is suspect etc. This paper examines how AI systems, their uses and discourse on them reflect, reinforce, and occasionally challenge (standard) language ideologies, which privilege Inner Circle norms and marginalize non-dominant Englishes. Drawing on evidence from empirical studies, media commentary, social media debates, and examples from AI outputs, the paper shows that AI technologies reproduce dominant language ideologies at different levels: training data, design protocols, evaluation benchmarks, user feedback and public commentary. The analysis uses the public controversy over AI-sounding language, especially the fixation on the word delve, to illustrate how speakers of English from the Global North police the English language norms of Global South English users. The paper also identifies what Christian Mair has called a "standardisation paradox": AI may homogenize English by privileging standard forms and at the same time pluralize Englishes through exposure to wide-ranging corpora and annotation work carried out by Global South users. In doing so, the paper argues that generative AI is reigniting long-standing debates in World Englishes about standardization, legitimacy, and the ownership of English, now playing out in algorithmic systems, model training, evaluation practices, and public discourse, where non-dominant Englishes are increasingly conflated with AI-generated speech. Discussing AI systems as a site where language ideologies are (re)produced, the paper argues for more inclusive design approaches that recognize the plurality of Englishes in order to address the real-world negative consequences of treating some as more legitimate than others.

### 🤖 AI 总结

**一句话总结**：The rapid growth of large language models (LLMs) has resurrected age-old questions in sociolinguistics and world Englishes, such as who decides what counts as legitimate English, whose English is susp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, systems, reproduction, standard, language, ideologies, World, Englishes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28528v1) | [下载PDF](https://arxiv.org/pdf/2607.28528v1.pdf)

---

## [12. Creative Transformation in Literary Texts: Modelling Change Across Representational Levels](https://arxiv.org/abs/2607.28513v1)

**作者**：Ioana-Roxana Boriceanu, Liviu P. Dinu  
**分类**：cs.CL  
**发布时间**：2026-07-30

### 📄 论文摘要

Creativity is often framed as the production of novelty, yet many cultural works emerge through transformation of earlier artifacts and not through isolated invention. Drawing on theories of imitation by Gabriel Tarde and James Mark Baldwin, this paper models creativity as selective transformation across multiple levels of textual representation. We introduce a multi-level framework that compares literary texts across lexical, semantic, conceptual, structural, and narrative dimensions using directional alignment and control calibrated similarity measures. Applying the model to historically documented literary relationships, we show that different pairs preserve source structure at different representational levels while diverging in others. These transformation profiles provide a quantitative method for characterizing how imitation persists and where creative divergence occurs within literary works.

### 🤖 AI 总结

**一句话总结**：Creativity is often framed as the production of novelty, yet many cultural works emerge through transformation of earlier artifacts and not through isolated invention. Drawing on theories of imitation...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Creative, Transformation, Literary, Texts, Modelling, Change, Across, Representational

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28513v1) | [下载PDF](https://arxiv.org/pdf/2607.28513v1.pdf)

---

## [13. Generative AI and linguistic diversity in academic writing and publishing: Perspectives from World Englishes](https://arxiv.org/abs/2607.28505v1)

**作者**：Kingsley Ugwuanyi, Christian Mair, Sender Dovchin 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-30

### 📄 论文摘要

The rise of generative artificial intelligence (GenAI) in academic writing and publishing (AWP) raises questions about linguistic inclusivity and the legitimacy of diverse Englishes in global scholarly communication. This article responds to these questions through a structured scholarly dialogue involving five sociolinguists from World Englishes and adjacent fields. Organised around five guiding questions, the dialogue interrogates how GenAI tools influence writing practices, reinforce or disrupt dominant language norms, and raise ethical challenges. Contributors reflect on the potential of GenAI to democratise writing processes while also raising concerns about GenAI's tendency to marginalise minoritised varieties and flatten nuance in scholarly writing. Across the dialogue, themes of linguistic (in)justice, researcher agency, and institutional responsibility emerge, with contributors calling for equity-informed policies, critical AI literacy, and inclusive co-design in GenAI development. The article shows the value of dialogic reflection in understanding GenAI's role in AWP. It concludes that while GenAI may reinforce existing hierarchies, it can also serve as a site of resistance, depending on how it is designed, governed and used within scholarly communities committed to linguistic diversity.

### 🤖 AI 总结

**一句话总结**：The rise of generative artificial intelligence (GenAI) in academic writing and publishing (AWP) raises questions about linguistic inclusivity and the legitimacy of diverse Englishes in global scholarl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Generative, linguistic, diversity, academic, writing, publishing, Perspectives, World

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28505v1) | [下载PDF](https://arxiv.org/pdf/2607.28505v1.pdf)

---

## [14. Beyond Sentiment: Structured Information Extraction from Financial News](https://arxiv.org/abs/2607.28496v1)

**作者**：Daohan Zhu, Sitong Ge, Ruofei Wang 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-30

### 📄 论文摘要

Financial sentiment analysis has become a standard component in news-driven stock prediction, yet it reduces rich, multi-dimensional news articles to a single polarity score. We hypothesize that financial news encodes multiple orthogonal information dimensions---event type, impact scope, temporal horizon, and semantic confidence---that sentiment alone cannot capture, and that these dimensions carry independent predictive value. To test this hypothesis, we propose a structured information extraction framework that leverages LLaMA-3.1-70B to extract six semantic dimensions from financial news. Through large-scale experiments on 41,618 news--stock pairs from the FNSPID dataset, we find that (i) FinBERT sentiment features exhibit strong predictive power under nonlinear models (F1=0.576) but substantially weaker performance under linear models (F1=0.230), revealing a highly nonlinear sentiment--return relationship; (ii) LLM-extracted structured features, while individually weaker, capture information orthogonal to sentiment, as evidenced by a 53.5% systematic disagreement rate between the two approaches; and (iii) combining both signal sources yields F1=0.600, significantly outperforming either alone ($p < 0.0001$), with consistent improvements across all seven event types. Ablation experiments confirm that non-sentiment structural dimensions (event type, impact subject, time horizon, confidence) independently contribute $Δ\text{F1} = +0.019$ beyond FinBERT alone. Feature importance analysis reveals balanced contributions from all six extracted dimensions (14--21%), demonstrating that compressing news into a single sentiment score incurs substantial information loss. Our results suggest that the sentiment--semantics decoupling in financial text is systematic and exploitable, opening a new direction for multi-dimensional financial NLP.

### 🤖 AI 总结

**一句话总结**：Financial sentiment analysis has become a standard component in news-driven stock prediction, yet it reduces rich, multi-dimensional news articles to a single polarity score. We hypothesize that finan...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Sentiment, Structured, Information, Extraction, Financial, News, analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28496v1) | [下载PDF](https://arxiv.org/pdf/2607.28496v1.pdf)

---

## cs.CV

## [15. ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine](https://arxiv.org/abs/2607.28625v1)

**作者**：Yukang Cao, Haozhe Xie, Beichen Wen 等 16 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-30

### 📄 论文摘要

Embodied intelligence faces a fundamental data bottleneck. Models must capture how first-person perception, whole-body motion, dexterous manipulation, object state, sound, and touch evolve together as humans pursue goals over time. Existing datasets fragment this experience across viewpoints, modalities, or spatial scales, leaving the full perception-action loop only partially observed. We introduce the Ambient Capture Engine (ACE), a human-centric data engine that transforms real home environments into spatially calibrated, temporally synchronized recording studios. ACE operates at two complementary scales: a table-scale configuration resolves hand-object manipulation, while a room-scale configuration captures whole-body motion, locomotion, and interactions across a furnished home. ACE records egocentric and multi-view exocentric video, full-body and articulated hand motion, object geometry and 6-DoF trajectories, audio, and tactile signals as a unified multisensory stream. Using ACE, we build ACE-Data-0, comprising 150 hours and 17M video frames across 200 task categories, performed by 50 participants in 2 environments, for a total of 75,000 interaction episodes. The dataset spans atomic manipulation, long-horizon chains of household activities, and human-scene interaction, while preserving natural behavioral variation through goal-level rather than step-by-step instructions. We further introduce a hierarchical benchmark that progresses from signals to scene components and then to interactions. Evaluations of state-of-the-art methods expose substantial gaps under contact, occlusion, egomotion, and long temporal horizons. ACE-Data-0 provides synchronized human demonstrations with aligned perceptual, kinematic, and contact supervision, offering a scalable foundation for imitation learning, world models, vision-language-action systems, and embodied AI.

### 🤖 AI 总结

**一句话总结**：Embodied intelligence faces a fundamental data bottleneck. Models must capture how first-person perception, whole-body motion, dexterous manipulation, object state, sound, and touch evolve together as...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, ACE-Data-0, Human-Centric, Ambient, Capture, Embodied, Data, Engine

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28625v1) | [下载PDF](https://arxiv.org/pdf/2607.28625v1.pdf)

---

## [16. PhiZero: A World Model Built Around Physical Language](https://arxiv.org/abs/2607.28624v1)

**作者**：Shuyao Shang, Yuqi Wang, Ruopeng Gao 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-30

### 📄 论文摘要

We introduce PhiZero, a physical world model built around physical language, a compact discrete representation of world-state transitions. Existing physical world models typically predict future videos directly in pixel space, leaving the underlying world dynamics implicit within high-dimensional visual predictors. Motivated by humans' ability to abstract predictive structure from visual experience and organize it in natural language for explicit reasoning, we learn physical language from in-the-wild videos through self-supervision and use it to explicitly reason about how the physical world evolves. Accordingly, PhiZero adopts a reason-then-render paradigm: it first infers future world evolution as a physical-language sequence and then renders the inferred transitions into videos. Extensive experiments across generation and understanding benchmarks validate the ability of PhiZero to model physically coherent world evolution. We further show its potential for realistic and interactive world modeling, fine-grained action-conditioned simulation, and zero-shot motion transfer.

### 🤖 AI 总结

**一句话总结**：We introduce PhiZero, a physical world model built around physical language, a compact discrete representation of world-state transitions. Existing physical world models typically predict future video...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, PhiZero, World, Model, Built, Around, Physical, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28624v1) | [下载PDF](https://arxiv.org/pdf/2607.28624v1.pdf)

---

## [17. Beacon: Knowing When and How to Perform Agentic Visual Reasoning](https://arxiv.org/abs/2607.28595v1)

**作者**：Qixun Wang, Yang Shi, Letian Cheng 等 14 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-30

### 📄 论文摘要

The fundamental goal of agentic visual reasoning is to improve the success rate of multimodal large language models (MLLMs) on complex tasks, rather than merely equipping them with a sophisticated yet inefficient reasoning paradigm. In this work, we rethink agentic visual reasoning through two key dimensions of tool use: Mode Adaptiveness (MA) and Tool Effect (TE). Mode Adaptiveness characterizes whether an MLLM can recognize when tools are truly necessary and invoke them accordingly, thereby avoiding unnecessary computational overhead while improving performance on challenging problems that require tool assistance. Tool Effect characterizes the actual impact of tool use: tools should extend the model's capabilities on problems unsolvable through text-only reasoning, while avoiding additional errors on problems that the model can already solve without tools. We conduct a comprehensive analysis to quantify these two properties and empirically reveal that existing agentic visual reasoning models exhibit limited Mode Adaptiveness, while the gains produced by tool use on hard examples are largely offset by the harm introduced on easy examples that the models can already solve. Motivated by these observations, we propose Beacon, a novel agentic visual reasoning model that achieves stronger overall performance, improved Mode Adaptiveness, and genuine tool-induced performance gains. At the core of Beacon are the Necessity-Aware Adaptive Reward and the Hint-Guided Capability Expansion mechanism in the reinforcement learning stage, which respectively encourage adaptive tool invocation based on task necessity and strengthen the model's tool-use capability on the most challenging problems. Extensive experiments across diverse benchmarks demonstrate the strong overall performance of Beacon and its substantial improvements in both Mode Adaptiveness and Tool Effect.

### 🤖 AI 总结

**一句话总结**：The fundamental goal of agentic visual reasoning is to improve the success rate of multimodal large language models (MLLMs) on complex tasks, rather than merely equipping them with a sophisticated yet...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beacon, Knowing, When, How, Perform, Agentic, Visual, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28595v1) | [下载PDF](https://arxiv.org/pdf/2607.28595v1.pdf)

---

## [18. MixFrag: Fragility-Guided Mixed-Precision Post-Training Quantization for Vision Transformers](https://arxiv.org/abs/2607.28589v1)

**作者**：Md. Mehrab Hossain Opi, Robiul Islam Ryad, Md. Umar Faruk  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-07-30

### 📄 论文摘要

Post-training quantization (PTQ) has emerged as an effective solution for deploying Vision Transformers (ViTs) on resource-constrained devices. However, existing PTQ methods typically employ uniform bit-widths across transformer components, overlooking their heterogeneous sensitivity to quantization and leading to inefficient precision allocation. In this paper, we propose {MixFrag, a fragility-guided mixed-precision PTQ framework for Vision Transformers. MixFrag first estimates component-level quantization fragility by measuring the Kullback--Leibler (KL) divergence between full-precision and isolated quantized output distributions using a small calibration set. It then formulates bit allocation as a Multiple-Choice Knapsack Problem (MCKP), enabling adaptive layer-wise precision assignment under a target bit budget. Extensive experiments on ImageNet-1K across multiple Vision Transformer architectures demonstrate that MixFrag achieves competitive classification performance under practical mixed-precision settings. Furthermore, evaluations on COCO object detection and instance segmentation show that MixFrag achieves state-of-the-art performance among existing mixed-precision PTQ methods, improving the previous best method by up to 9.6 AP under the challenging MP3/MP3 setting. Additional analyses validate the proposed fragility metric and demonstrate its strong correlation with the learned bit allocation. These results establish MixFrag as an effective framework for mixed-precision post-training quantization of Vision Transformers.

### 🤖 AI 总结

**一句话总结**：Post-training quantization (PTQ) has emerged as an effective solution for deploying Vision Transformers (ViTs) on resource-constrained devices. However, existing PTQ methods typically employ uniform b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MixFrag, Fragility-Guided, Mixed-Precision, Post-Training, Quantization, Vision, Transformers, PTQ

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28589v1) | [下载PDF](https://arxiv.org/pdf/2607.28589v1.pdf)

---

## [19. ROAD: Reciprocal-Objective Alignment of Discriminative Semantics for 3D Shape Generation](https://arxiv.org/abs/2607.28581v1)

**作者**：Xiao Luo, Mingyang Du, Xin Zhou 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-30

### 📄 论文摘要

High-fidelity 3D generation predominantly relies on scaling model capacity and data, which incurs prohibitive computational costs. This paradigm typically requires learning geometry from scratch and overlooks the rich semantic and structural priors already encapsulated in discriminative 3D foundation models. We contend that leveraging the profound understanding of the 3D world possessed by these discriminative models can significantly reduce generative cost. To this end, we propose ROAD, a framework that reduces the training cost of 3D generation by transferring these rich discriminative priors into diffusion transformers. To address the inherent semantic-structural heterogeneity between generative and discriminative latents, we introduce a reciprocal-objective alignment strategy. This method synergizes Holistic Semantic Condensing to enforce global semantic coherence and Structural Optimal Alignment, which is formulated as a bipartite matching problem to rigorously align microscopic geometric details between disparate latent spaces. The 3D foundation model is only used for training-time supervision of alignment and is not used at inference, incurring no additional inference cost. Compared with the industrial baseline Step1X-3D, the proposed ROAD achieves highly competitive generation performance with only 1.5% of the training data and significantly reduces training costs, effectively reducing the computational overhead of high-fidelity 3D generation. Code is available at https://github.com/H-EmbodVis/ROAD.

### 🤖 AI 总结

**一句话总结**：High-fidelity 3D generation predominantly relies on scaling model capacity and data, which incurs prohibitive computational costs. This paradigm typically requires learning geometry from scratch and o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, 3D, ROAD, Reciprocal-Objective, Alignment, Discriminative, Semantics, Shape

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28581v1) | [下载PDF](https://arxiv.org/pdf/2607.28581v1.pdf)

---

## [20. Finding Change in Satellite Archives from Text: How to Combine Before-and-After Images Efficiently](https://arxiv.org/abs/2607.28571v1)

**作者**：Simon Roy, Mark Bong, Giovanni Beltrame  
**分类**：cs.CV, cs.IR  
**发布时间**：2026-07-30

### 📄 论文摘要

Operational Earth observation increasingly calls for answering queries such as ``find the image pairs where a new building appeared.'' This means searching an archive of before-and-after (bi-temporal) satellite image pairs and ranking each pair by how well it matches a natural-language description of the change. The component that performs this match, the fusion module that combines the ``before'' and ``after'' views, must be run at query time across many candidate pairs, so its speed largely sets the cost of every search. We present a controlled comparison of how to build that module. Using one fixed image encoder (a frozen CLIP model) and one training recipe for all variants, we evaluate eight designs drawn from three families: attention, state-space models (Mamba), and learned compression (our Temporal Bottleneck Fusion, TBF). Each design is tested on two benchmarks (LEVIR-CC and Dubai-CC) with ten random seeds, so the reported differences are statistically grounded. We outline three findings: first, a training-free two-stage search (a cheap difference model that shortlists candidates, followed by attention fusion that re-ranks them) matches or exceeds full-fusion recall on LEVIR-CC while cutting query cost $10$-$15\times$, with comparable R@1/R@5 on Dubai-CC; second, the linear-time scan of Mamba, attractive on paper, gives no speed benefit at the patch counts typical of vision transformers ($L{=}196$): the scan is limited by memory bandwidth, whereas attention maps cleanly onto parallel hardware; and third, compressing the fused representation (TBF) reduces parameters by $2.3\times$ and latency by $1.6\times$ for a change-only BLEU-1 cost of $0.007$, although more aggressive compression quietly discards change-relevant detail that aggregate metrics fail to reveal.

### 🤖 AI 总结

**一句话总结**：Operational Earth observation increasingly calls for answering queries such as ``find the image pairs where a new building appeared.'' This means searching an archive of before-and-after (bi-temporal)...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Finding, Change, Satellite, Archives, Text, How, Combine, Before-and-After

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28571v1) | [下载PDF](https://arxiv.org/pdf/2607.28571v1.pdf)

---

## [21. MIND: Multimodal Intent-Driven Network via Diffusion Transformers for Medical Image Fusion](https://arxiv.org/abs/2607.28565v1)

**作者**：Yunzhan Fu, Xiangyu Shen, Yifei Sun 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-30

### 📄 论文摘要

Medical image fusion aims to integrate complementary information from diverse imaging modalities to support clinical diagnosis. Existing methods typically apply uniform fusion rules globally, lacking a deep understanding of diagnostic intents and pathological structures. To address these limitations, we propose MIND, a Multimodal Intent-Driven Network via Diffusion Transformers (DiTs) for medical image fusion. Specifically, we utilize BioMedGPT to generate intent-driven fusion texts from source images, guiding the fusion process with pathology-aware diagnostic intents. To combat the loss of 2D spatial continuity caused by 1D sequence flattening in DiTs, we design a Multi-scale Latent Adapter. This module explicitly extracts source image features before serialization, injecting them into the network via strict dimensional alignment to effectively supplement image features. To resolve the semantic shift caused by decoupling image outputs from diagnostic intents, we design a medical semantic consistency loss. This loss ensures deep semantic locking between fused images and fusion texts while maintaining the stability of the underlying physical manifold reconstruction. Comprehensive experiments on the Harvard, BraTS, and GFP datasets reveal that MIND delivers superior fusion quality, significantly improves downstream brain tumor segmentation accuracy, and enables flexible interactive fusion, holding significant promise for intent-driven intelligent clinical decision support systems.

### 🤖 AI 总结

**一句话总结**：Medical image fusion aims to integrate complementary information from diverse imaging modalities to support clinical diagnosis. Existing methods typically apply uniform fusion rules globally, lacking ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, MIND, Multimodal, Intent-Driven, Network, via, Transformers, Medical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28565v1) | [下载PDF](https://arxiv.org/pdf/2607.28565v1.pdf)

---

## [22. ScaFE: Data-Efficient Scar Classification with LLM-Generated Clinical Feature Programs](https://arxiv.org/abs/2607.28538v1)

**作者**：Ruman Wang, Hangting Ye  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-07-30

### 📄 论文摘要

Classifying pathological scars from clinical photographs requires distinguishing keloids from hypertrophic scars despite limited expert-labeled data and substantial acquisition variation across hospitals. End-to-end image models remain data-dependent, whereas sending photographs to a hosted vision-language model (VLM) may conflict with local data-governance requirements and yields decisions that are difficult to reproduce and audit. We introduce ScaFE (Scar Feature Engineering), which transfers clinical knowledge from a large language model (LLM) into deterministic, executable feature programs instead of asking the model to diagnose images. A web-enabled LLM retrieves clinical evidence and synthesizes programs that measure visually assessable scar attributes. Candidate programs execute in a restricted local environment, and only aggregate validation statistics and feature-level SHAP summaries are returned for iterative repair and refinement; raw images and patient-level outputs remain local. A lightweight Random Forest then operates on the resulting structured representation. On 600 photographs from three hospitals under leave-one-site-out evaluation, ScaFE achieves 81.0% site-macro balanced accuracy, exceeding the strongest baseline, BiomedCLIP, by 10.0 percentage points. With only 10% of the development data, ScaFE retains 72.0% balanced accuracy and an 11.8-point lead. Iterative refinement also raises the executable-program rate from 66.7% to 95.0%, with verified evidence for 91.7% of the final features. These results show that LLM knowledge can support data-efficient, cross-site medical image classification through local and auditable feature programs rather than direct VLM decisions.

### 🤖 AI 总结

**一句话总结**：Classifying pathological scars from clinical photographs requires distinguishing keloids from hypertrophic scars despite limited expert-labeled data and substantial acquisition variation across hospit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ScaFE, Data-Efficient, Scar, Classification, LLM-Generated, Clinical, Feature, Programs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28538v1) | [下载PDF](https://arxiv.org/pdf/2607.28538v1.pdf)

---

## [23. MarkushGlyph and OCSRGlyph: Improved Chemical Structure Recognition](https://arxiv.org/abs/2607.28532v1)

**作者**：Alex Andonian, Samuel G Rodriques, Andrew D White 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-30

### 📄 论文摘要

Chemical structures appear in patents and the scientific literature as images. For programmatic usage, such as indexing in databases or constructing machine learning model training sets, they must be transformed into line notations. The two common forms of this task are translating an image of a single molecule (optical chemical structure recognition - OCSR) and translating a Markush structure that represents a family of molecules. While prior work in the former case is quite mature, Markush structure parsing remains a challenging task. In this work, we treat both tasks as an image-to-text translation problem. We then propose OCSRGlyph, a state-of-the-art OCSR model, improving performance over prior methods by carefully considering stereochemistry. For the Markush task, we introduce MarkushGlyph, a vision-language model that reads the entire Markush structure as an image. This contrasts with prior systems, which often use multiple stages to separately process visual and text input content. Finally, we introduce a new metric for determining the accuracy of Markush structure translations, handling failure modes present in prior metrics.

### 🤖 AI 总结

**一句话总结**：Chemical structures appear in patents and the scientific literature as images. For programmatic usage, such as indexing in databases or constructing machine learning model training sets, they must be ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MarkushGlyph, OCSRGlyph, Improved, Chemical, Structure, Recognition, structures, appear

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28532v1) | [下载PDF](https://arxiv.org/pdf/2607.28532v1.pdf)

---

## [24. What to Remove, What to Preserve: Dual-Ambiguity Rectification for All-in-One Image Restoration](https://arxiv.org/abs/2607.28526v1)

**作者**：Cencen Liu, Wen Yin, Dongyang Zhang 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-30

### 📄 论文摘要

All-in-one image restoration aims to handle diverse degradations within a unified framework. Existing methods commonly encode heterogeneous degradation conditions in a shared latent space, where degradation-related cues and scene content can remain entangled. We characterize the resulting challenge as dual ambiguity: semantic ambiguity in channel-wise modulation and spatial ambiguity in restoration responses, which can lead to content corruption and residual artifacts. To mitigate this issue, we propose DAR-Net, a Dual-Ambiguity Rectification Network for all-in-one image restoration. DAR-Net first introduces a Degradation Archetype Representation (DAR) module to construct a structured degradation state through simplex-constrained archetype mixture modeling. Based on this state, a Semantic Ambiguity Rectification (SeAR) module generates degradation-aware prompts to improve channel-wise conditioning in the decoder. A Spatial Ambiguity Rectification (SpAR) module further regularizes degradation-aware and complementary features toward orthogonal response subspaces, reducing spatial interference between removal and preservation cues. Extensive experiments on standard all-in-one restoration benchmarks show that DAR-Net achieves the best overall performance under both three-degradation and five-degradation settings, improving the average PSNR over the strongest competitor by 0.14 dB and 0.34 dB, respectively; it additionally shows superior performance on CDD-11 and WeatherBench.

### 🤖 AI 总结

**一句话总结**：All-in-one image restoration aims to handle diverse degradations within a unified framework. Existing methods commonly encode heterogeneous degradation conditions in a shared latent space, where degra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：What, Remove, Preserve, Dual-Ambiguity, Rectification, All-in-One, Image, Restoration

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28526v1) | [下载PDF](https://arxiv.org/pdf/2607.28526v1.pdf)

---

## [25. RefCaptioner: Multi-Reference Image-Grounded Video Captioning](https://arxiv.org/abs/2607.28509v1)

**作者**：Tengfei Liu, Yang Shi, Yuran Wang 等 19 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-30

### 📄 论文摘要

Existing video captioning models generate natural descriptions of video content but cannot explicitly ground local visual elements to multiple reference images. We introduce multi-reference image-grounded video captioning, a new task requiring factual video descriptions with phrase-level reference grounding, and propose RefCaptioner, a two-stage post-training framework for this task. RefCaptioner combines mixed-data SFT with Hierarchical Coverage-Discounted GRPO to jointly improve reference selection, phrase-level binding, distractor rejection, and cross-reference consistency while preserving general video-captioning ability. To support training, we construct a corpus containing $20,000$ videos and 171,354 reference images. We further introduce MRVBench, a benchmark for evaluating caption factuality and multi-reference grounding on both real-world and AI-generated videos. Experiments show that RefCaptioner achieves the best overall performance among the open-source models while remaining competitive on standard video captioning benchmarks. Human evaluation further confirms that its captions are preferred by annotators and enable more source-faithful video reconstruction with both open-source and proprietary video generators.

### 🤖 AI 总结

**一句话总结**：Existing video captioning models generate natural descriptions of video content but cannot explicitly ground local visual elements to multiple reference images. We introduce multi-reference image-grou...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RefCaptioner, Multi-Reference, Image-Grounded, Video, Captioning, Existing, models, generate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28509v1) | [下载PDF](https://arxiv.org/pdf/2607.28509v1.pdf)

---

## [26. AuricularWorld: Hierarchical Action-Guided World Modeling for Fine-Grained Auricular Structure Segmentation from CT Scans](https://arxiv.org/abs/2607.28487v1)

**作者**：Jingwen Yang, Senmao Wang, Luoyao Kang 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-30

### 📄 论文摘要

Fine-grained segmentation of auricular structures in CT is challenging because the ear occupies a small image region, cartilage boundaries are highly irregular, and interfaces between cartilage and surrounding soft tissues are often ambiguous. Clinical annotations may also include both composite structures containing cartilage and adjacent skin and their corresponding cartilage-only regions, producing nested and overlapping labels. We propose a world-model-based segmentation framework that enables iterative anatomical reasoning beyond conventional feed-forward prediction. Built on an encoder-decoder architecture, the framework introduces a deterministic recurrent state-space model into the intermediate latent space. Multi-scale encoder features and partially decoded representations are fused to form a structural observation that initializes the latent dynamics. During inference, the model performs a three-step latent rollout without ground-truth guidance. Hierarchical anatomical actions update the recurrent state and progressively refine the latent representation. The resulting latent trajectory is projected back into the decoder and combined with high-resolution features to produce the final segmentation. To learn reliable latent transitions, we introduce a balanced hierarchical action objective that addresses foreground sparsity, missing anatomical groups, and imbalance between add and remove operations. Extensive experiments show that the proposed framework consistently improves segmentation accuracy and reduces HD95 by more than 43% for small, irregular, and overlapping auricular structures in CT. These results demonstrate the effectiveness of latent world-model reasoning for challenging medical image segmentation.

### 🤖 AI 总结

**一句话总结**：Fine-grained segmentation of auricular structures in CT is challenging because the ear occupies a small image region, cartilage boundaries are highly irregular, and interfaces between cartilage and su...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AuricularWorld, Hierarchical, Action-Guided, World, Modeling, Fine-Grained, Auricular, Structure

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28487v1) | [下载PDF](https://arxiv.org/pdf/2607.28487v1.pdf)

---

## [27. Towards Real-Time PixOOD: Efficient Anomaly Segmentation for Autonomous Vehicles](https://arxiv.org/abs/2607.28483v1)

**作者**：Luca de Martino, Federico Aromolo, Federico Nesti 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-30

### 📄 论文摘要

Real-time anomaly segmentation is essential for the safety of autonomous systems. Although recent approaches offer high accuracy, their computational cost limits their deployment on embedded hardware. This work presents an efficient and accelerated pipeline designed for both embedded and desktop platforms, targeting the autonomous driving and railway domains. The proposed approach reformulates the Neyman-Pearson scoring stage of PixOOD, a state-of-the-art out-of-distribution detection method, and deploys the full pipeline through hardware-optimized TensorRT compilation, reaching up to 182 FPS on a desktop NVIDIA RTX 4060 GPU and 75 FPS on the NVIDIA Jetson AGX Orin embedded platform, respectively 20x and 18x faster than the original baseline. The achieved results demonstrate that advanced anomaly segmentation can be efficiently deployed for onboard processing in autonomous driving and railway applications.

### 🤖 AI 总结

**一句话总结**：Real-time anomaly segmentation is essential for the safety of autonomous systems. Although recent approaches offer high accuracy, their computational cost limits their deployment on embedded hardware....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Towards, Real-Time, PixOOD, Efficient, Anomaly, Segmentation, Autonomous, Vehicles

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28483v1) | [下载PDF](https://arxiv.org/pdf/2607.28483v1.pdf)

---

## cs.LG

## [28. KAISEN: Reproducible Subgroup Fairness Auditing for Clinical Risk Models](https://arxiv.org/abs/2607.28608v1)

**作者**：Sparsh Roy, Samuel Girmachew, Nishita Chavan  
**分类**：cs.LG, q-bio.QM  
**发布时间**：2026-07-30

### 📄 论文摘要

Clinical risk models routinely achieve strong aggregate performance while producing materially different error rates across patient subgroups. Audit pipelines have been proposed to catch this, but their components are rarely stress-tested, so it is unclear which parts of an audit can be trusted and under what conditions. We present KAISEN, a five-phase audit pipeline covering subgroup stratification, disparity measurement, mechanism diagnostics, post-hoc mitigation, and drift monitoring, evaluated to the point of failure on a synthetic benchmark of 16 disease tasks, 15 social-determinant axes from Healthy People 2030, and three prespecified intersections. Four findings follow. (i) Significance tracks each axis's gap against its own minimum detectable effect: rank correlation between significance count and raw equalized-odds difference (EOD) across the 15 axes is rho = 0.56, rising to rho = 0.78 once EOD is standardized by that floor. (ii) Per-group threshold optimization reduces EOD in 48 of 48 held-out runs (paired delta = -0.285, 95% CI [-0.313, -0.252]), while group-wise Platt scaling -- the better calibrator -- behaves as a coin flip on EOD (19 of 48 runs improved, 95% CI [0.26, 0.55]) with mean effect near zero, so what an audit should report is the variance, not the average. (iii) The mechanism diagnostic classifies 144 of 144 controlled cases correctly but recovers none of 48 model-driven cases under proxy misspecification, with no signal that it failed. (iv) CUSUM failures and false alarms track cohort realization far more than disease: at the reference threshold, all 27 false alarms and 7 of 8 missed shifts come from different seeds (chi-squared p = 0.002), so a threshold tuned on one cohort fails to transfer. All results are synthetic with known ground truth and do not establish clinical validity. Code, artifacts, and scripts reproducing every number are released.

### 🤖 AI 总结

**一句话总结**：Clinical risk models routinely achieve strong aggregate performance while producing materially different error rates across patient subgroups. Audit pipelines have been proposed to catch this, but the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：KAISEN, Reproducible, Subgroup, Fairness, Auditing, Clinical, Risk, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28608v1) | [下载PDF](https://arxiv.org/pdf/2607.28608v1.pdf)

---

## [29. APO: Unsupervised Atomic Policy Optimization for 3D Structure Prediction of Atomic Systems](https://arxiv.org/abs/2607.28553v1)

**作者**：Shentong Mo, Yatao Bian  
**分类**：cs.LG, cs.AI, cs.MA  
**发布时间**：2026-07-30

### 📄 论文摘要

Predicting the 3D structures of atomic systems is fundamental to advancing material science and drug discovery. While flow-matching models (, FlowDPO) have recently shown promise in this domain, their performance relies heavily on alignment with ground-truth coordinates via supervised preference learning. However, obtaining experimental labels for novel crystal phases or de novo proteins is prohibitively expensive, creating a bottleneck for structural modeling in data-scarce regimes. In this work, we propose (Atomic Policy Optimization), a fully unsupervised alignment framework that eliminates the need for ground-truth reference structures. APO adapts group-relative policy optimization to 3D atomic environments, utilizing a novel dual-reward mechanism: (i) a that reinforces the policy's dominant latent structural modes through eigen-decomposition of sample similarities, and (ii) a that enforces thermodynamic stability. Our framework enables the model to ``self-correct'' by identifying physically plausible configurations within sampled groups. Extensive benchmarks on crystal and antibody structure prediction demonstrate that APO consistently outperforms fully supervised baselines, achieving a new state-of-the-art in match rates and structural fidelity. Furthermore, we show that APO effectively straightens probability paths, significantly improving inference efficiency. Our results suggest that intrinsic physical consistency can serve as a superior guide for alignment compared to noisy, supervised coordinate matching.

### 🤖 AI 总结

**一句话总结**：Predicting the 3D structures of atomic systems is fundamental to advancing material science and drug discovery. While flow-matching models (, FlowDPO) have recently shown promise in this domain, their...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, APO, Unsupervised, Atomic, Policy, Optimization, Structure, Prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28553v1) | [下载PDF](https://arxiv.org/pdf/2607.28553v1.pdf)

---

## [30. Same Graph Cross-Task Transfer in GNNs: Protocols and Predictors](https://arxiv.org/abs/2607.28525v1)

**作者**：Neelam Akula, Surbhi Kumar, Murat Kantarcioglu 等 4 位作者  
**分类**：cs.LG, cs.SI  
**发布时间**：2026-07-30

### 📄 论文摘要

Many real-world graphs support multiple predictive tasks over the same underlying structure, creating an opportunity to reuse supervision across node classification (NC) and link prediction (LP). However, existing evaluations often rely on incompatible splits, observed-graph assumptions, and negative sampling rules, making conclusions about same-graph cross-task transfer unreliable. We formalize same-graph NC-LP transfer and propose a leakage-free protocol that fixes node and edge splits, uses a shared message-passing graph that excludes evaluated edges, and employs fixed negatives for LP. Across three backbones (GCN, GraphSAGE, GPS), we find that transfer is strongly directional and predictable: NC $\to$ LP is consistently beneficial on homophilic graphs, while LP $\to$ NC is fragile and can even degrade accuracy under naive representation reuse. LP $\to$ NC becomes reliably positive mainly in a structure-dominant regime where LP is easy but NC is unsaturated, suggesting that LP acts as structural pretraining. Finally, we introduce the CoTask Score (CTS) to summarize joint NC+LP utility when a shared encoder must serve both tasks, and show that simple dataset statistics, especially homophily, can guide mechanism choice and help avoid negative transfer.

### 🤖 AI 总结

**一句话总结**：Many real-world graphs support multiple predictive tasks over the same underlying structure, creating an opportunity to reuse supervision across node classification (NC) and link prediction (LP). Howe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Same, Graph, Cross-Task, Transfer, GNNs, Protocols, Predictors, Many

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.28525v1) | [下载PDF](https://arxiv.org/pdf/2607.28525v1.pdf)

---

