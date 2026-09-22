# arXiv AI 论文日报 | 2026-09-22

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (8 篇)
- [cs.LG](#csLG) (6 篇)
- [cs.AI](#csAI) (8 篇)
- [cs.CL](#csCL) (8 篇)

---

## cs.AI

## [1. Harness-Zero: Harness Distillation via Agent-as-Harness](https://arxiv.org/abs/2609.24974v1)

**作者**：Haoran Ye, Yuxing Lu, Haonan Dong 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.NE  
**发布时间**：2026-09-21

### 📄 论文摘要

Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the best harness varies across domains, instances, and models, a general-purpose agent must either settle for a suboptimal shared harness or route among an ever-growing set of specialized ones. We therefore study agent harness distillation: using a domain- or instance-optimized harness as training-time guidance and transferring the behaviors it induces into model weights, so that its gains survive under a single fixed target harness. The challenge is that the two harnesses differ in action space and available information, so guidance from the optimized harness cannot serve directly as supervision for the target one. We introduce Harness-Zero, which enables harness distillation through agent-as-harness. Guided by the optimized harness, a harnessing agent corrects student responses before execution in the target harness's action space, turning harness guidance into training demonstrations. Fine-tuning on the resulting trajectories internalizes harness-induced behavior into the model, so the specialized harness can be removed at deployment. Our experiments spanning knowledge work, tool use, and science domains show that: (1) For frontier LLMs using the same evolved harness, agent-as-harness outperforms code-as-harness. (2) With the specialized harness removed at deployment, Harness-Zero improves the base model's macro-average task success from 23.3% to 44.3%, even exceeding the 41.7% it reaches with that harness still attached. (3) Harness-Zero recovers harness-induced behaviors absent from the base model, with 82.3% average recovery across 28 patterns in the three domains.

### 🤖 AI 总结

**一句话总结**：Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the bes...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Harness-Zero, Harness, Distillation, via, Agent-as-Harness, harnesses, external

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24974v1) | [下载PDF](https://arxiv.org/pdf/2609.24974v1.pdf)

---

## [2. Emergent Collusion in Long-Horizon LLM Agent Interaction](https://arxiv.org/abs/2609.24967v1)

**作者**：Xinrui Shi, Yanzhe Zhang, Diyi Yang  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-09-21

### 📄 论文摘要

LLM agents are increasingly deployed in collaborative settings, yet long-term interaction may give rise to undesirable coordination. We study the emergence of collusion in a long-horizon multi-agent environment: two agents repeatedly complete individual tasks, share task logs, verify each other's work, and receive rewards. We introduce realistic constraints that make compliance with the verification protocol incompatible with reward maximization, and find that agents increasingly deviate from the protocol over repeated interactions. Collusion emerges in 94% of trajectories across 10 models, and more capable models within the same family reach it earlier. Controlled peer interventions show that collusion is shaped by peer behavior, while ablations reveal additional effects of reward structure, the verification feedback agents receive, and their interaction history. In particular, restricting the amount and scope of interaction history available to agents reduces collusion. Overall, our findings show that long-horizon interaction can reshape how agents coordinate in ways that create safety risks.

### 🤖 AI 总结

**一句话总结**：LLM agents are increasingly deployed in collaborative settings, yet long-term interaction may give rise to undesirable coordination. We study the emergence of collusion in a long-horizon multi-agent e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, Emergent, Collusion, Long-Horizon, Interaction, increasingly, deployed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24967v1) | [下载PDF](https://arxiv.org/pdf/2609.24967v1.pdf)

---

## [3. Et Tu, Brute? Economic Misalignment in Personal AI Agents](https://arxiv.org/abs/2609.24927v1)

**作者**：Aman Priyanshu, Supriti Vijay, Brian Jabarian 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-21

### 📄 论文摘要

Personal AI agents make recommendations and take actions on people's behalf in high-stakes economic contexts, e.g., buying a flight, choosing health insurance, or selecting a graduate program. The agent is given access to the user's personal context, e.g., their email inbox and a structured profile of personal attributes, with the intention of making an optimal, personalized decision for the user. We show that by simply providing this personal context, the agent steers recommendations based on inferred wealth, without being explicitly instructed to do so. In a suite of 325K experiments on 13 agents across three types of economic decisions (flights, health insurance, and graduate programs), we find that 8 models systematically choose more expensive options for wealthier users when requests are identical. This steering continues even when it directly goes against the user's stated objective: when explicitly instructed to find the cheapest option, some agents still act on the wealth profile they have inferred. It also occurs when wealth is inferred from ambient data, such as emails unrelated to the task. And it persists under privacy controls that block specific attributes: blocking financial attributes largely removes the disparity, but blocking other attributes leaves it unchanged and can increase it by up to 40% for insurance, as agents rely on the remaining signals to infer wealth. Larger and more capable models are no better; Claude Opus 4.8 shows the largest effect. We term this misalignment "adversarial delegation", in which the very conditions that make a personal AI agent useful - access to personal information - enable it to act against the user's interests.

### 🤖 AI 总结

**一句话总结**：Personal AI agents make recommendations and take actions on people's behalf in high-stakes economic contexts, e.g., buying a flight, choosing health insurance, or selecting a graduate program. The age...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Et, Tu, Agent, Brute?, Economic, Misalignment, Personal, make

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24927v1) | [下载PDF](https://arxiv.org/pdf/2609.24927v1.pdf)

---

## [4. BackTrend: Evaluating Scientific Weak-Signal Prediction via Backward Reconstruction](https://arxiv.org/abs/2609.24921v1)

**作者**：Xiao Zhou, Yilun Zhao, Owen Jiang 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-21

### 📄 论文摘要

Scientific weak signals are early, low-visibility research directions that later become central to mature scientific topics, yet existing resources such as trend tracking, citation forecasting, and foresight reports rarely provide validated reference sets that link concrete early precursors to later paradigms. We introduce BackTrend, a retrospective benchmark in which, given a mature target topic and a temporal evidence constraint, systems must recover two types of precursors: problem-space signals, underrecognized research problems, and solution-space signals, emerging methods for known problems. BackTrend contains 25 mature target topics in artificial intelligence and machine learning and 66 human-validated weak signals, reconstructed from large-scale literature by grounding each candidate in its 2019-2024 publication-frequency trajectory. We evaluate frontier LLMs, RAG systems, and agentic research systems using semantic matching and coverage-based metrics. Current systems often generate plausible but misaligned precursors, exhibiting topic drift, granularity mismatch, near-miss matching, and incomplete coverage; the strongest system achieves only 10.1% F1, while Coverage10 reaches at most 18.5% of the reference signals. Our budget analyses show that additional retrieval and web-search evidence can improve performance up to a moderate budget, but does not by itself close the substantial performance gap.

### 🤖 AI 总结

**一句话总结**：Scientific weak signals are early, low-visibility research directions that later become central to mature scientific topics, yet existing resources such as trend tracking, citation forecasting, and fo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BackTrend, Evaluating, Scientific, Weak-Signal, Prediction, via, Backward, Reconstruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24921v1) | [下载PDF](https://arxiv.org/pdf/2609.24921v1.pdf)

---

## [5. A Global Comparison of Schemas, Transparency, and Interoperability in Public-Sector AI Registers and Inventories](https://arxiv.org/abs/2609.24883v1)

**作者**：Dipto Das, Shion Guha  
**分类**：cs.AI, cs.CY, cs.HC  
**发布时间**：2026-09-21

### 📄 论文摘要

Artificial intelligence (AI) registers and inventories aim to make governmental AI visible, but their institutional scope, schemas, and reporting practices construct different representations of public-sector AI. We compare 8,368 records from country-specific and transnational inventories covering 72 countries. Across 23 harmonized fields, registers shared a descriptive core but rarely requested information about appeals, risks, legal bases, or external evaluation. We found that broad schemas often contained substantial missingness, schema similarity showed no significant patterned convergence, and multiple sources covering the same jurisdictions overlapped only selectively. Based on these findings, we synthesize a layered visibility framework that shows how register records reflect disclosure arrangements and why interoperability requires shared concepts, clear definitions, and preserved provenance.

### 🤖 AI 总结

**一句话总结**：Artificial intelligence (AI) registers and inventories aim to make governmental AI visible, but their institutional scope, schemas, and reporting practices construct different representations of publi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Global, Comparison, Schemas, Transparency, Interoperability, Public-Sector, Registers

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24883v1) | [下载PDF](https://arxiv.org/pdf/2609.24883v1.pdf)

---

## [6. Pinocchio: Fast Uncertainty Estimates for Black-Box Language Models](https://arxiv.org/abs/2609.24881v1)

**作者**：Kevin David Hayes, Arka Pal, Haosong Zhang 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-21

### 📄 论文摘要

In high-stakes decision-making applications of large language models (LLMs), practitioners require not only accurate LLMs but also uncertainty estimates for their predictions. Existing approaches to uncertainty estimation for LLMs require access to log-probabilities output by the model or require fine-tuning access. However, many industrial LLM products use closed-source API models, and many such API models like GPT do not return log-probabilities and may not allow fine-tuning. We introduce Pinocchio, an external calibrator that estimates the correctness of responses from black-box API models. Trained jointly on responses from seven LLMs, it achieves 0.862 AUROC predicting the correctness of held-out responses from those same models, and shows zero-shot transfer to thirteen unseen models across eight organizations. Our model needs only a single forward pass to generate an uncertainty estimate and requires no access to the target model's logits, weights, or internal states. A lightweight text only 0.8B checkpoint matches our largest model's AUROC. We release code for adding uncertainty estimation to existing repos in only two additional lines of code.

### 🤖 AI 总结

**一句话总结**：In high-stakes decision-making applications of large language models (LLMs), practitioners require not only accurate LLMs but also uncertainty estimates for their predictions. Existing approaches to u...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Pinocchio, Fast, Uncertainty, Estimates, Black-Box, Language, Models, high-stakes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24881v1) | [下载PDF](https://arxiv.org/pdf/2609.24881v1.pdf)

---

## [7. Extracting Arguments, Not Just Classifying Them: Instruction-Tuned LLMs for Generative Component Detection](https://arxiv.org/abs/2609.24855v1)

**作者**：Sofiane Elguendouze, Erwan Hain, Elena Cabrio 等 4 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-09-21

### 📄 论文摘要

Argumentative component detection (ACD) is a core subtask of Argument(ation) Mining (AM) and one of its most challenging aspects, as it requires jointly delimiting argumentative spans and classifying them into components such as claims and premises. While research on this subtask remains relatively limited compared to other AM tasks, most existing approaches formulate it as a simplified sequence labeling problem, component classification, or a pipeline of component segmentation followed by classification. In this paper, we propose ITFACD, a novel approach based on instruction-tuned Large Language Models (LLMs) using compact instruction-based prompts, and reframe ACD as a language generation task, enabling arguments to be identified directly from plain text without relying on pre-segmented components. Experiments on standard benchmarks show that our approach achieves higher performance compared to state-of-the-art systems. To the best of our knowledge, this is one of the first attempts to fully model ACD as a generative task, highlighting the potential of instruction tuning for complex AM problems. Our code and the datasets used are openly available in the following GitHub repository.

### 🤖 AI 总结

**一句话总结**：Argumentative component detection (ACD) is a core subtask of Argument(ation) Mining (AM) and one of its most challenging aspects, as it requires jointly delimiting argumentative spans and classifying ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Extracting, Arguments, Not, Just, Classifying, Them, Instruction-Tuned

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24855v1) | [下载PDF](https://arxiv.org/pdf/2609.24855v1.pdf)

---

## [8. MedRSI: Recursive Self-Improvement for Medical Agents via Clinically Aligned Self-Evolution](https://arxiv.org/abs/2609.24838v1)

**作者**：Junde Wu, Jiayuan Zhu, Minghao Hu 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-21

### 📄 论文摘要

Medical agents increasingly combine general reasoning models with specialized clinical tools, yet their capabilities remain largely fixed by what clinicians and engineers design before deployment. Recursive self-improvement (RSI) offers a different paradigm in which agents learn from their own failures and autonomously expand their capabilities, but directly applying RSI to medicine introduces fundamental safety challenges. We introduce MedRSI, the first recursive self-improvement framework for medicine, which continuously transforms diagnostic failures into new clinical capabilities through tool composition and task-specific model training. Inspired by clinical practice, MedRSI introduces two mechanisms for clinically aligned self-evolution. Clinical-cost-aware failure prioritization directs improvement toward errors according to their potential clinical consequences rather than frequency alone. Fast discovery with slow registration separates rapid capability invention from conservative adoption, allowing new tools to enter the persistent agent only after demonstrating sustained benefit across subsequent patient cohorts. Across public glaucoma and heart disease benchmarks and two private clinical tasks, MedRSI progressively develops segmentation, measurement, prediction, multimodal reasoning, and generative capabilities, surpasses manually engineered medical agents, and autonomously discovers solutions to clinical problems not anticipated by its original designers. Our results show that medical agents need not remain constrained by capabilities specified before deployment: with clinically grounded mechanisms governing what to improve and what to retain, they can continuously construct, validate, and accumulate new capabilities from diagnostic experience. Code is available at https://github.com/ImprintLab/MedRSI.

### 🤖 AI 总结

**一句话总结**：Medical agents increasingly combine general reasoning models with specialized clinical tools, yet their capabilities remain largely fixed by what clinicians and engineers design before deployment. Rec...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, MedRSI, Recursive, Self-Improvement, Medical, via, Clinically, Aligned

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24838v1) | [下载PDF](https://arxiv.org/pdf/2609.24838v1.pdf)

---

## cs.CL

## [9. Jev for Scientific Decisions: Evaluating Semantic Choices and Their Consequences](https://arxiv.org/abs/2609.24965v1)

**作者**：Boyuan Deng, Shuyi Fan, Hongyang Zhang 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-21

### 📄 论文摘要

Scientific workflows often require choosing among known relations before a deterministic calculation can proceed. Whether observations share a culture, treatment or reference standard can change the scientific meaning of the resulting count or comparison. We evaluate Jev as a semantic decision component using a harness that follows its documented guidance and assigns arithmetic to code. The study compares twelve model configurations on twenty source-grounded Choices across ten scientific cases, each repeated five times. We measure semantic selections, downstream outputs and final claim labels separately. Jev matched five other configurations at complete semantic correctness and achieved the lowest observed median latency among successful responses. Across three comparison models, seven wrong selections on one culture-history question changed downstream counts while preserving the correct final label. These results identify a useful role for Jev in prepared scientific decision tasks and show why evaluating that role requires checking the relations and quantities that a workflow will reuse.

### 🤖 AI 总结

**一句话总结**：Scientific workflows often require choosing among known relations before a deterministic calculation can proceed. Whether observations share a culture, treatment or reference standard can change the s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Jev, Scientific, Decisions, Evaluating, Semantic, Choices, Their, Consequences

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24965v1) | [下载PDF](https://arxiv.org/pdf/2609.24965v1.pdf)

---

## [10. Linguistic Features for Interpretable Textual Entailment](https://arxiv.org/abs/2609.24932v1)

**作者**：David Torres-Moreno, Jorge Hermosillo-Valadez, Asela Reig-Alamillo  
**分类**：cs.CL, cs.SC  
**发布时间**：2026-09-21

### 📄 论文摘要

Despite the success of neural models in natural language processing, their black-box nature limits interpretability and conceals the linguistic phenomena underlying their predictions. We present SLITE, an explainable hybrid model for Recognizing Textual Entailment that integrates two complementary layers of semantic analysis: a structural-relational layer, based on semantic compatibility and incompatibility between compositional entities, and a distributional-informational layer, based on structured patterns of information change between embedding-based representations of the premise and the hypothesis. We propose 17 features that combine entity-level semantic relations, polarity-sensitive lexical matching, and alignment measures over semantic sub-representations of the similarity matrix, including measures based on entropy and transfer entropy. A logistic regression trained on these features achieves an accuracy of 83% on three-class SICK and 96% on SICK-CE, outperforming IsoLex by 4 percentage points and falling within 2 percentage points of RoBERTa with a fraction of its computational complexity. Ablation studies and SHAP analysis confirm that structural-relational features are the primary drivers of classification, while distributional-informational features provide essential complementary contributions, particularly for detecting neutrality and contradiction. Our results demonstrate that further exploration of hybrid approaches is a viable and scientifically productive alternative to massive neural architectures, and we hope they will strengthen the dialogue between linguistic theory and computational modeling of inference

### 🤖 AI 总结

**一句话总结**：Despite the success of neural models in natural language processing, their black-box nature limits interpretability and conceals the linguistic phenomena underlying their predictions. We present SLITE...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Linguistic, Features, Interpretable, Textual, Entailment, Despite, success

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24932v1) | [下载PDF](https://arxiv.org/pdf/2609.24932v1.pdf)

---

## [11. SocioVerse2: A Longitudinal Dynamic Social Simulation Framework under a Human-AI Co-evolutionary Paradigm](https://arxiv.org/abs/2609.24911v1)

**作者**：Xinnong Zhang, Jiayu Lin, Jia Wang 等 22 位作者  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-09-21

### 📄 论文摘要

Social simulation offers the social sciences an experimental instrument that the real world cannot supply, and generative agents have transformed it by acting as silicon samples that unite agent-based modeling with real behavioral data. Existing platforms verify collective behavior, align simulated populations with real societies in cross-sections, and employ autonomous agents for the research process. However, two social science requirements remain without systematic support: intervention in the content of a simulation and the researcher's control over the process that produces it. We present SocioVerse2, which extends SocioVerse 1.0 into a human-AI co-evolutionary paradigm built from two loops and one infrastructure. The longitudinal simulation loop simulates the target population with evolving environments and forks counterfactual branches via interventions. The controllable research loop takes the study itself as an editable state and updates state versions via controllable editing. The social science agentic infrastructure carries both loops through composable skills with researcher checkpoints, a population service over five persona pools, and an environment service over 21 real-world signal sources with point-in-time guarantees. We validate SocioVerse2 across three case families and seven case studies, from reproducing canonical agent-based models to modeling policy processes on real records and nowcasting macro-economic indices beyond the response model's knowledge cutoff. With the human-AI co-evolutionary paradigm, these cases go beyond system demonstrations to become substantive studies that investigate frontier questions in their respective disciplines. Code, data services, and a workbench are released as open-source resources.

### 🤖 AI 总结

**一句话总结**：Social simulation offers the social sciences an experimental instrument that the real world cannot supply, and generative agents have transformed it by acting as silicon samples that unite agent-based...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SocioVerse2, Longitudinal, Dynamic, Social, Simulation, Framework, under, Human-AI

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24911v1) | [下载PDF](https://arxiv.org/pdf/2609.24911v1.pdf)

---

## [12. ToneCL: Contrastive Learning for Few-Shot Syllable-Level Tone Classification](https://arxiv.org/abs/2609.24903v1)

**作者**：Qisheng Liao, Youngah Do  
**分类**：cs.CL  
**发布时间**：2026-09-21

### 📄 论文摘要

Tone languages constitute over 50-70% of the world's languages, but the vast majority are low-resource, lacking the large transcribed corpora needed for automatic tone classification. Existing datasets are typically collected at the sentence level, whereas field linguists require fine-grained syllable-level annotations. We propose ToneCL, a lightweight contrastive learning framework for few-shot syllable-level tone classification. We simulate low-resource conditions on Mandarin and Vietnamese, limiting labeled data to tens of examples per tone class. ToneCL is pretrained on unlabeled speech with augmentations that preserve tonal identity, then fine-tuned on few-shot examples. Experiments show our method consistently outperforms baselines, achieving 91.6% on six-speaker Mandarin at 10 shots. Cross-lingual transfer is also effective: pretraining on Vietnamese and fine-tuning on Mandarin reaches 91.0\% accuracy at 10 shots. Ablation confirms that frequency band rejection is the most critical augmentation.

### 🤖 AI 总结

**一句话总结**：Tone languages constitute over 50-70% of the world's languages, but the vast majority are low-resource, lacking the large transcribed corpora needed for automatic tone classification. Existing dataset...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ToneCL, Contrastive, Learning, Few-Shot, Syllable-Level, Tone, Classification, languages

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24903v1) | [下载PDF](https://arxiv.org/pdf/2609.24903v1.pdf)

---

## [13. Human-LLM Deliberation as Interactive Proof: Conditions for Verifiability Without Transparency](https://arxiv.org/abs/2609.24895v1)

**作者**：Baotong Zhang, Dean Foster, João Sedoc  
**分类**：cs.CL  
**发布时间**：2026-09-21

### 📄 论文摘要

When an LLM supplies an argument that a user could not readily construct, how can the user decide whether to accept its claim? Inspired by interactive proofs, we model human-LLM deliberation as an interaction between a prover with unrestricted internal search and a resource-bounded human verifier. The verifier requests and checks supporting details without access to the LLM's internal state. Passed checks accumulate evidence toward an acceptance threshold. We prove anytime-valid soundness against adaptive provers: the probability of ever accepting a false claim is at most a chosen error level, provided the task supplies bounds on false passes and human checking errors that remain valid after every relevant history. A finite-horizon completeness bound additionally requires bounds on the adequacy of honest responses and sufficient diagnostic progress. Further checks can strengthen the evidence for acceptance, but each requires another adequate response and reliable human effort. Whether this tradeoff permits certification depends on the verifier's effort budget, cognitive load, expertise, and fatigue. We identify conditions under which the supplied bounds certify a specified sequence of local checks but not a specified global check under the same resource budgets.

### 🤖 AI 总结

**一句话总结**：When an LLM supplies an argument that a user could not readily construct, how can the user decide whether to accept its claim? Inspired by interactive proofs, we model human-LLM deliberation as an int...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Human-LLM, Deliberation, Interactive, Proof, Conditions, Verifiability, Without

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24895v1) | [下载PDF](https://arxiv.org/pdf/2609.24895v1.pdf)

---

## [14. OSWorld-Pro: Process-based Evaluation for Computer Use Agents](https://arxiv.org/abs/2609.24890v1)

**作者**：Zhilin Wang, Shaokun Zhang, Yifan Zhang 等 12 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-09-21

### 📄 论文摘要

Evaluation of Computer-Use Agents (CUAs) is often limited to the final deliverables they create (at the end of hundreds of steps) and assessed with functional verifiers, as seen in OSWorld. However, such evaluation of end-state performance lacks transparency into how and why agents fail in various tasks, obfuscating critical insight for subsequent improvement. For instance, agents that err during keyboard inputs would require a different mitigation strategy from those that fail to precisely provide click-based inputs on the graphical UI. We introduce OSWorld-Pro: a set of over 300 tasks containing over 2800 subgoals to enable the procedural evaluation of CUAs grounded in over 67,000 human annotations. We use robust human-aligned LLM-Judges to evaluate the fulfillment of OSWorld-Pro subgoals and thereby reveal the progress that models make throughout a series of sequentially dependent subgoals. Our findings reveal that OSWorld-Pro is challenging even for state-of-the-art LLMs, with top performers like Claude Opus 5 achieving only 75.7% vs. 83.4% on OSWorld. Furthermore, we identify critical process-focused failure modes of various models (e.g. subgoal-irrelevant actions and click-based mistakes) to provide insights to improve performance and efficiency of CUAs.

### 🤖 AI 总结

**一句话总结**：Evaluation of Computer-Use Agents (CUAs) is often limited to the final deliverables they create (at the end of hundreds of steps) and assessed with functional verifiers, as seen in OSWorld. However, s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, of, OSWorld-Pro, Process-based, Evaluation, Computer, Use, Computer-Use

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24890v1) | [下载PDF](https://arxiv.org/pdf/2609.24890v1.pdf)

---

## [15. The Copy Ceiling: An Input-Exposure Control for Ontology-Grounded Generation over Curated Corpora](https://arxiv.org/abs/2609.24885v1)

**作者**：John J. O'Hare  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-09-21

### 📄 论文摘要

When a language model answers from a curated corpus via graph-based retrieval, a large grounding uplift does not establish reasoning over the retrieved structure: the context may already expose the gold answers. We propose exposure accounting, which classifies each gold item by whether the shown context exposes it and whether the answer recovers it. Its scalar reference is the copy ceiling, the recall a verbatim copy of the context achieves; signed gain over copy measures the model's recall relative to this deterministic, judge-free baseline. Across ten models, unaided recall averages 0.26 and grounded recall 0.92, yet gain over copy is uniformly negative (-0.067 to -0.022). Of 11,360 gold-item observations, representing 1,136 target instances evaluated under ten models, only three unexposed items receive lexical credit. A stratified model-judged audit of 423 observations, with a symmetric quotation-verification policy, estimates that 97.1% of credited items assert the requested relation; all three unexposed credits fail relational adjudication. On targets the scaffold does not expose, lexical recovery falls from 0.121 unaided to 0.004 grounded; adjudication validates 71 of the 92 unaided credits and none of the three grounded credits, without establishing full-frame relational recovery rates. Rephrasing questions outside the graph's title vocabulary reduces exposure from 0.964 to 0.328, while an absence-triggered fallback activates on only 2 of 506 questions. A paired production study improves judged quality by +0.27 pooled, but negative controls do not establish content specificity beyond a well-formed on-corpus block. These results support exposure accounting as a standing control for corpus-derived evaluations. The accounting distinguishes exposed-item omissions from beyond-exposure recoveries; it does not determine whether reasoning occurred.

### 🤖 AI 总结

**一句话总结**：When a language model answers from a curated corpus via graph-based retrieval, a large grounding uplift does not establish reasoning over the retrieved structure: the context may already expose the go...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Copy, Ceiling, Input-Exposure, Control, Ontology-Grounded, Generation, over

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24885v1) | [下载PDF](https://arxiv.org/pdf/2609.24885v1.pdf)

---

## [16. Decomposing Error and Style in Automated Clinical Coding](https://arxiv.org/abs/2609.24877v1)

**作者**：Han-Chin Shing, Jack Moriarty, Ryan Ware 等 9 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-21

### 📄 论文摘要

In automated clinical coding, where the label space spans tens of thousands of diagnosis and procedure codes, models are currently evaluated against a single gold annotation, treating any deviation as error. But we find when two teams code the same 110 ACI-Bench encounters, they agree on only 73% of codes (Jaccard similarity) for the same note; even after an independent clinical audit removes erroneous codes, agreement rises only to 77%. Is that gap error or something systematic? We model the systematic component as coding style $ψ$, a coder- or site-specific policy over what to code and how much to document, and recast coding as $p(\mathrm{code}\mid\mathrm{note},ψ)$, estimating $ψ$ with a 10-dimension rubric. If style were noise, conditioning on it would do nothing. Instead, across five datasets a model conditioned with a data-matching style raises ICD F1 by up to 26 points and an extreme mismatched one lowers it by up to 21. Four prompt based coding methods spanning 39-49 F1 converge to 52-56 once style is supplied (All p<0.05). Much of what single-gold evaluation charges to model error is recoverable, unmodeled style.

### 🤖 AI 总结

**一句话总结**：In automated clinical coding, where the label space spans tens of thousands of diagnosis and procedure codes, models are currently evaluated against a single gold annotation, treating any deviation as...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Decomposing, Error, Style, Automated, Clinical, Coding, where, label

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24877v1) | [下载PDF](https://arxiv.org/pdf/2609.24877v1.pdf)

---

## cs.CV

## [17. VideoGen-Agent: Reinforcing Video Generation Agents](https://arxiv.org/abs/2609.24997v1)

**作者**：Binxu Li, Haoyi Duan, Yuhui Zhang 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-21

### 📄 论文摘要

Recent advances in video generative models have enabled high-fidelity, temporally coherent video generation. However, these models often struggle to satisfy prompts requiring specialized knowledge, specific identities, physical consistency, or ordered events. In this paper, we present VideoGen-Agent, a multimodal agent trained through multitask agentic reinforcement learning to use external tools for video generation. The agent coordinates augmentation, generation, and verification tools through multi-turn interactions, using the prompt and intermediate observations to guide its decisions. We train a shared policy on a category-balanced dataset spanning six tasks. Supervised fine-tuning on teacher-generated trajectories establishes tool-use behavior, which is then refined through reinforcement learning. A category-aware hybrid reward evaluates tool-call validity, task-appropriate tool use, and generated video quality. We further introduce VABench, a held-out benchmark of 600 prompts covering procedural knowledge, single- and multi-entity identity preservation, physical consistency, scene composition, and multi-shot temporal structure. On VABench, VideoGen-Agent improves over its base text-to-video generator by 19.1 points, from 56.5 to 75.6. Upgrading the generation tools further raises the score to 86.1 without additional agent training. Human raters prefer the upgraded configuration over the strongest standalone baseline in 84.3% of comparisons. These results support learning tool use across video-generation tasks and show that the trained agent can benefit from subsequent advances in generation tools.

### 🤖 AI 总结

**一句话总结**：Recent advances in video generative models have enabled high-fidelity, temporally coherent video generation. However, these models often struggle to satisfy prompts requiring specialized knowledge, sp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, VideoGen-Agent, Reinforcing, Video, Generation, Recent, advances, generative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24997v1) | [下载PDF](https://arxiv.org/pdf/2609.24997v1.pdf)

---

## [18. GAE: Learning a Geometry-Native Latent Space for 3D-Consistent World Generation](https://arxiv.org/abs/2609.24981v1)

**作者**：Jiahao Lu, Minghao Yin, Wenbo Hu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-21

### 📄 论文摘要

We present a compact geometry-native latent space as a shared foundation for perception and generation. Visual generators can produce photorealistic frames without preserving a consistent 3D scene. We argue that this is not only a modeling problem but also a representation problem: generators typically evolve appearance-centric latents, while perception models recover geometry in a semantically rich space that encodes cross-view structure. Rather than adding geometry as another output, we reparameterize a geometry foundation model's features into a compact latent space for generation. We realize this shift with the geometry-native autoencoder (GAE), whose latent is jointly decodable to appearance, depth, cameras, and point maps. With this state, a standard conditional flow supports diverse generation tasks. In controlled comparisons that hold the generator and training protocol fixed, replacing the latent with GAE improves both visual quality and independently measured 3D coherence: FVD falls by $12.7\%$ and $23.1\%$ on RealEstate10K and DL3DV, and camera-trajectory error is halved on RealEstate10K. Together, these results show that the latent space is central to geometry-consistent generation and can serve as a shared interface between perception and generation.

### 🤖 AI 总结

**一句话总结**：We present a compact geometry-native latent space as a shared foundation for perception and generation. Visual generators can produce photorealistic frames without preserving a consistent 3D scene. We...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GAE, Learning, Geometry-Native, Latent, Space, 3D-Consistent, World, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24981v1) | [下载PDF](https://arxiv.org/pdf/2609.24981v1.pdf)

---

## [19. Anatomy-Decomposed Chest Computed Tomography (CT) Projections as Scalable Supervision for Bone Suppression in Chest Radiographs](https://arxiv.org/abs/2609.24937v1)

**作者**：Mrunmay Angaitkar, Piyush Kumar, Aarjav Satia 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-21

### 📄 论文摘要

Bone overlap can obscure abnormalities in chest radiographs, while scarce paired training data limit supervised bone suppression. We address this challenge with a digitally reconstructed radiograph (DRR) framework that converts chest computed tomography (CT) into paired supervision for component suppression. A novel bone segmentation algorithm enables CT decomposition into bone, non-lung soft-tissue, and lung components, which are projected separately. Their weighted combination yields synthetic radiographs with pixel-registered component images that sum exactly to the full DRR. Models trained on these data suppress bone or lung components by predicting the target component and recovering the remainder by subtraction, transferring to real radiographs without real paired training data. As an extension, their outputs on real radiographs provide target domains for unpaired, component-wise DRR translation, reducing the appearance gap while retaining anatomical details. Across multiple public datasets, downstream detection experiments demonstrate the utility of bone suppression, with gains concentrated on abnormalities with substantial bone overlap. Compared with open-source DRR engines applied to the same CTs, our unmodified DRRs achieve comparable realism and preservation of label-relevant anatomy, while translated DRRs achieve the best Fréchet inception distance (FID), lung-field sharpness, and agreement with source-CT anatomy among the evaluated methods. Models and inference code: https://huggingface.co/qureaiorg/bone-suppression; Translated projections: https://huggingface.co/datasets/qureaiorg/ct2xr-projections.

### 🤖 AI 总结

**一句话总结**：Bone overlap can obscure abnormalities in chest radiographs, while scarce paired training data limit supervised bone suppression. We address this challenge with a digitally reconstructed radiograph (D...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CT, as, Anatomy-Decomposed, Chest, Computed, Tomography, Projections, Scalable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24937v1) | [下载PDF](https://arxiv.org/pdf/2609.24937v1.pdf)

---

## [20. PixelDiT2: Representation-Grounded Pixel Diffusion Transformers](https://arxiv.org/abs/2609.24919v1)

**作者**：Yongsheng Yu, Wei Xiong, Yichen Sheng 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-21

### 📄 论文摘要

Recent advances in pixel-space diffusion models have narrowed the image quality gap with latent-space diffusion, but still converge more slowly and lag behind in final image quality. We argue that a key reason is the lack of an explicit representation prior: unlike latent diffusion, which usually denoises in a compact and structured latent space, pixel diffusion needs to learn denoising-friendly representations and pixel generation simultaneously from raw RGB space. To address this problem, we propose PixelDiT2, an end-to-end pixel-space diffusion model designed to decouple representation learning from pixel generation without introducing an autoencoder or latent reconstruction bottleneck. We propose representation grounding that uses a frozen pretrained vision foundation model to provide explicit per-patch representation guidance throughout denoising, allowing the pixel diffusion transformer to focus more on pixel generation. On ImageNet-256x256, PixelDiT2 achieves an FID of 1.46 after 600 epochs; at 512x512 resolution, PixelDiT2 achieves an FID of 1.48 after 680 epochs.

### 🤖 AI 总结

**一句话总结**：Recent advances in pixel-space diffusion models have narrowed the image quality gap with latent-space diffusion, but still converge more slowly and lag behind in final image quality. We argue that a k...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, PixelDiT2, Representation-Grounded, Pixel, Transformers, Recent, advances, pixel-space

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24919v1) | [下载PDF](https://arxiv.org/pdf/2609.24919v1.pdf)

---

## [21. Generating Chest X-Ray Counterfactuals by Specialising Foundation Image Models](https://arxiv.org/abs/2609.24879v1)

**作者**：Xiaodan Xing, Rajat R. Rasal, Julia A. Meister 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-21

### 📄 论文摘要

Counterfactual image generation answers questions about how a subject would have looked under retrospective, hypothetical scenarios. Recent methods have improved perceptual quality, identity preservation and faithfulness to an underlying causal model, but their adoption in healthcare is limited by scarce annotated data, distribution shift between datasets, and mismatches between pretrained generative models and those required for counterfactual inference. We propose specialisation, a data and parameter-efficient framework for adapting pretrained, non-causal generative models into causal mechanisms under distribution shift. Based on this framework, we train a radiology counterfactual image generation model, called RadCF, using latent flow matching. We validate our approach on three chest X-ray datasets spanning different dataset shifts, data volumes, and counterfactual questions, associated with challenging, highly-localised interventions. Our results show that RadCF and specialisation improve counterfactual soundness over existing methods while being data and parameter efficient, and that the resulting counterfactuals can detect and mitigate shortcut learning in a downstream medical classifier. Code is available at https://github.com/GSK-AI/RadCF/.

### 🤖 AI 总结

**一句话总结**：Counterfactual image generation answers questions about how a subject would have looked under retrospective, hypothetical scenarios. Recent methods have improved perceptual quality, identity preservat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Generating, Chest, X-Ray, Counterfactuals, Specialising, Foundation, Image, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24879v1) | [下载PDF](https://arxiv.org/pdf/2609.24879v1.pdf)

---

## [22. SPHQuant: Efficient extreme low bit weight quantization for Vision-Language Models](https://arxiv.org/abs/2609.24875v1)

**作者**：Kewei Zhang, Zheng Chen, Haotong Qin 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-21

### 📄 论文摘要

Recent foundation models are moving toward native multimodal Vision-Language Models (VLMs), making VLMs a central form of next-generation foundation models. However, their large language backbones make edge deployment difficult due to high memory footprint and memory-bound autoregressive decoding. Weight-only post-training quantization is a practical solution, but pushing VLMs to extreme low bit-widths remains challenging: existing rotation-free methods suffer from outliers at 2-3 bits, while rotation-based methods improve accuracy at the cost of additional runtime overhead. We propose SPHQuant, a rotation-free spherical weight-only quantization framework for VLMs. Instead of quantizing weights directly in Cartesian coordinates, SPHQuant decomposes each 8D weight vector into coordinate signs, radius, and a positive unit direction. This representation isolates outlier magnitude into the radius while keeping directions bounded and statistically regular. Based on this insight, SPHQuant allocates extra precision to the radius to mitigate accuracy degradation induced by outliers. It further uses a compact positive-direction codebook and fine-tunes codebook entries through angular parameterization to preserve the unit-sphere constraint. We also design a hardware-friendly GEMV kernel that keeps the direction codebook small enough for shared-memory lookup and packs radial bits efficiently. Experiments show that SPHQuant matches the performance of state-of-the-art extreme low-bit quantization methods while improving decode throughput over QTIP by 30.3% on RTX A6000. Code will be released in https://github.com/Pushazf/SPHQuant.

### 🤖 AI 总结

**一句话总结**：Recent foundation models are moving toward native multimodal Vision-Language Models (VLMs), making VLMs a central form of next-generation foundation models. However, their large language backbones mak...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SPHQuant, Efficient, extreme, low, bit, weight, quantization, Vision-Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24875v1) | [下载PDF](https://arxiv.org/pdf/2609.24875v1.pdf)

---

## [23. DTKDP: A Dual Teacher Knowledge Distillation and Pruning Framework for Lightweight Oriented SAR Ship Detection](https://arxiv.org/abs/2609.24872v1)

**作者**：Yuming Li, Fan Zhang, Alin M. Achim  
**分类**：cs.CV  
**发布时间**：2026-09-21

### 📄 论文摘要

Two-stage oriented detectors achieve high localization accuracy in synthetic aperture radar (SAR) ship detection, but their large backbones, feature pyramids, proposal modules, and heavy region of interest (RoI) heads hinder deployment. Existing lightweight SAR ship detectors typically use one-stage frameworks that lack proposal-level refinement for precise rotated localization. This paper presents a dual-teacher knowledge distillation and pruning (DTKDP) framework for lightweight oriented SAR ship detection. DTKDP introduces learnable gates into convolutional, normalization, and linear layers to prune convolutional channels and RoI-head neurons. Rotated proposal alignment (RPA) distills teacher and student predictions in a shared teacher-generated rotated proposal space, while a dual-teacher scheme combines classification and regression guidance from a homogeneous main teacher with complementary classification cues from a heterogeneous auxiliary teacher. Experiments on the SAR Ship Detection Dataset (SSDD) and Rotated Ship Detection Dataset in SAR Images (RSDD-SAR) show that DTKDP reduces the parameters of Oriented Region-based Convolutional Neural Network (Oriented R-CNN) and RoI Transformer equipped with ResNet-50 backbones by 87.5-91.8% and their floating-point operations (FLOPs) by 75.6-79.9%. In terms of average precision (AP) and mean average precision (mAP), the resulting Oriented R-CNN-slim and RoI Transformer-slim retain accuracy close to their full-scale counterparts. Relative changes across $\mathrm{AP}_{50}$, $\mathrm{AP}_{75}$, $\mathrm{mAP}_{50:75}$, and $\mathrm{mAP}_{50:95}$ range from a 2.38% decrease to a 0.65% improvement. Compared with RTMDet-tiny, they improve all four metrics on both datasets by 0.52-27.55% and consistently surpass representative distillation methods, demonstrating a favorable accuracy-efficiency trade-off.

### 🤖 AI 总结

**一句话总结**：Two-stage oriented detectors achieve high localization accuracy in synthetic aperture radar (SAR) ship detection, but their large backbones, feature pyramids, proposal modules, and heavy region of int...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DTKDP, Dual, Teacher, Knowledge, Distillation, Pruning, Framework, Lightweight

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24872v1) | [下载PDF](https://arxiv.org/pdf/2609.24872v1.pdf)

---

## [24. When Wider Views Fail: Stress-Testing Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2609.24839v1)

**作者**：Daisy Li, Kyle Gao, Quanyun Wu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-21

### 📄 论文摘要

Feed-forward 3D reconstruction models enable efficient geometry estimation from sparse images, but their pretrained nature can make them vulnerable to distribution shifts beyond their training data. Identifying these failure modes is important for understanding when such models can be reliably deployed in unconstrained imaging settings. We investigate viewpoint variation as a controlled distribution shift by varying the angular span of sparse image inputs while keeping the input budget fixed. Across multiple feed-forward reconstruction models, we observe substantial degradation as viewpoint span increases, with wide spans producing both incomplete surface coverage and geometry unsupported by the observed imagery. These results reveal that viewpoint variation can induce failure modes beyond conventional reconstruction incompleteness, highlighting the need to evaluate pretrained feed-forward models under distribution shifts that challenge their learned geometric priors.

### 🤖 AI 总结

**一句话总结**：Feed-forward 3D reconstruction models enable efficient geometry estimation from sparse images, but their pretrained nature can make them vulnerable to distribution shifts beyond their training data. I...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, When, Wider, Views, Fail, Stress-Testing, Feed-Forward, Reconstruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24839v1) | [下载PDF](https://arxiv.org/pdf/2609.24839v1.pdf)

---

## cs.LG

## [25. Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use](https://arxiv.org/abs/2609.24985v1)

**作者**：Zixiang Chen, Wenting Zhao, Zhepeng Cen 等 12 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-09-21

### 📄 论文摘要

Multi-turn tool-use failures can hinge on a single model call, yet reward variation alone does not reveal which call would benefit from training. When rewards depend on later interactions, their variation can reflect downstream randomness rather than differences between the current actions. We introduce Critical-State RL to identify trainable states in multi-turn interactions. Given task-defined candidate calls and local rewards, the method assesses whether each reward captures the action's effect on task success and whether improvement over a reference policy is possible. It then uses nested sampling to separate action-dependent reward variation from continuation noise and optimizes the policy at the selected states using contextual-bandit training. Experiments on the Berkeley Function Calling Leaderboard (BFCL) v4 compare training at diagnostic-selected states with training at alternative states. For missing-function tasks, the diagnostic selects the response after the tool becomes available; for missing-argument tasks, it selects the response before the missing argument is supplied. Training the selected responses improves performance, including about 14 percentage points on the missing-function task, while training the alternatives leaves performance flat or worse. We further apply the recipe across models and tasks, including logged repeat-call avoidance and memory management.

### 🤖 AI 总结

**一句话总结**：Multi-turn tool-use failures can hinge on a single model call, yet reward variation alone does not reveal which call would benefit from training. When rewards depend on later interactions, their varia...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Critical-State, Diagnosing, Trainable, States, Multi-Turn, Tool, Use

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24985v1) | [下载PDF](https://arxiv.org/pdf/2609.24985v1.pdf)

---

## [26. Rare Event Estimation via Iterative Unalignment](https://arxiv.org/abs/2609.24969v1)

**作者**：Hanming Yang, Daksh Mittal, Jing Dong 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-21

### 📄 论文摘要

As agents are deployed with increased autonomy, even extremely rare events along their stochastic output trajectories can occur and prove catastrophic. Safe deployment therefore does not depend on whether these events can occur, but on how often they might. We study the problem of estimating the probability of rare events that arise from stochastic variation in the agent's own actions. Estimating this type of risk requires searching over the combinatorially vast space of trajectories. Naive Monte Carlo is computationally prohibitive in this regime, and constructing effective importance sampling (IS) proposals requires coordinated changes to a context-dependent chain of conditional distributions. We develop a new IS method that perturbs the original model's weights to construct the proposal. The proposal is itself a differentiably parameterized language model, enabling gradient-based search over weight space. We formulate an objective that combines a differentiable surrogate for event amplification and an adaptive regularization scheme that dynamically balances amplification against estimator stability. We evaluate our approach on $\sim$120M and $\sim$2.6B models across three event families spanning 300+ rare events as rare as $10^{-9}$, with reference probabilities computed with $<10\%$ relative standard error. In our most verifiable settings, we observe that our IS estimator achieves over $800\times$ compute-weighted efficiency gains over naive Monte Carlo for events with probabilities lower than $10^{-7}$. Our implementation is available at https://github.com/namkoong-lab/iterative-unalignment.

### 🤖 AI 总结

**一句话总结**：As agents are deployed with increased autonomy, even extremely rare events along their stochastic output trajectories can occur and prove catastrophic. Safe deployment therefore does not depend on whe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, Agent, Rare, Event, Estimation, via, Iterative, Unalignment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24969v1) | [下载PDF](https://arxiv.org/pdf/2609.24969v1.pdf)

---

## [27. Learning Physics from an Imperfect Ancestor](https://arxiv.org/abs/2609.24947v1)

**作者**：S. Mohammad Mousavi, Teeratorn Kadeethum, Nikolaos Bouklas 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-21

### 📄 论文摘要

Neural operators evaluate parametric partial differential equations cheaply but degrade sharply outside their training distribution. Physics-informed neural networks avoid dependence on labeled data, yet their optimization can be basin-fragile: when the governing residual admits multiple solutions, a PINN trained from scratch may converge to a physically incorrect state despite achieving a small residual. We show that these failure modes can be addressed jointly: an imperfect NO provides the structural prior needed to place a PINN in the correct solution basin, while the PDE residual refines the solution beyond the operator's accuracy. We introduce a three-stage framework that freezes the spatial basis of a physics-informed NO, extrapolates its solution branch to an out-of-distribution parameter using a polynomial continuation prior, and distills the resulting field into a fresh PINN. The NO need not be accurate at the target; it transfers solution-branch information, while PDE residual minimization in the PINN governs convergence. We evaluate the framework on three nonlinear PDEs: 1D viscous Burgers, 2D steady Allen-Cahn near a pitchfork bifurcation, and 2D steady lid-driven cavity flow. For Allen-Cahn, where the trivial solution satisfies the PDE residual exactly, a standard PINN collapses to the trivial zero branch, whereas distillation from the crude extrapolated operator recovers the non-trivial branch that matches the finite-difference reference. For the lid-driven cavity, extrapolating to a Reynolds number of Re = 3200 accelerates convergence to the correct physical state, achieving competitive accuracy using fewer parameters and optimization steps than recent literature baselines. These results establish a simple principle: an NO need not accurately predict the solution to be useful; it only needs to identify the correct basin from which PINN optimization can recover it.

### 🤖 AI 总结

**一句话总结**：Neural operators evaluate parametric partial differential equations cheaply but degrade sharply outside their training distribution. Physics-informed neural networks avoid dependence on labeled data, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Learning, Physics, Imperfect, Ancestor, Neural, operators, evaluate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24947v1) | [下载PDF](https://arxiv.org/pdf/2609.24947v1.pdf)

---

## [28. Exactness at Inference: A Representational Criterion for Out-of-Distribution Generalization](https://arxiv.org/abs/2609.24942v1)

**作者**：Filipe Marinho Rocha, Inês Dutra, Vítor Santos Costa 等 4 位作者  
**分类**：cs.LG, cs.AI, cs.LO  
**发布时间**：2026-09-21

### 📄 论文摘要

A model generalizes outside its training distribution only when it computes a representation structurally equivalent to the generating mechanism, not an approximation fitted to it. Such equivalence is necessary for exactness in and out of distribution, and extrapolation is governed by this exactness at inference, whatever its realization. Tensor Logic shows this: a zero-temperature contraction is equivalent to discrete logic, deducing in place with no artefact extracted, its tensors Boolean, its embeddings orthonormal, only its arithmetic continuous. Lacking infinite recursion it reaches Datalog, not Prolog, and though exact over closed domains it needs external memory to bind a novel entity. The criterion needs neither a discrete representation nor an extracted expression, and constrains inference, not training: an exact marginal in $[0,1]$ passes, a Neural Network thresholded to a hard label does not. Logic Tensor Networks fail it, while differentiable ILP and Tensor Logic at $T=0$ pass. Piecewise-affine extrapolation divergence and an inability to bind novel entities are two faces of a shortfall in exact representability. For hybrid architectures, a propagation rule follows: the output inherits the bounds of every fitted estimator on its path, explaining which axes fail in equivariant models and the ARC-AGI induction/transduction split. Only an exact hypothesis class certifies what the training data leave underdetermined: on a law-derived partition it finds the $56.3\%$ of distant queries that are answerable, which ensembles meet with false confidence and distance metrics rank backwards. Common inductive biases, from symmetries to memory, reach exactness only because humans inject them, an argument for inducing exact representations rather than fitting surrogates whose residuals, even at the arithmetic floor in training, diverge outside the data and compound under composition.

### 🤖 AI 总结

**一句话总结**：A model generalizes outside its training distribution only when it computes a representation structurally equivalent to the generating mechanism, not an approximation fitted to it. Such equivalence is...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Exactness, Inference, Representational, Criterion, Out-of-Distribution, Generalization, model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24942v1) | [下载PDF](https://arxiv.org/pdf/2609.24942v1.pdf)

---

## [29. Learning Prognostic Variables for AI Convective Parameterizations via Symbolic Distillation](https://arxiv.org/abs/2609.24882v1)

**作者**：Jurij Schönfeld, Tom Beucler, Julien Savre 等 5 位作者  
**分类**：cs.LG, physics.ao-ph  
**发布时间**：2026-09-21

### 📄 论文摘要

Hybrid AI-physics climate modeling aims to improve coarse (~100km-resolution) Earth system models by learning to parameterize subgrid processes from high-fidelity data. However, this so far mostly involves local-in-time, diagnostic parameterizations, in which the subgrid state depends only on the current coarse state with no memory of previous states, which is unrealistic for processes such as convection that have intrinsic persistence. To address this, we enhance local-in-time parameterizations by learning prognostic variables that compactly carry important, additional past information where no explicit sub-grid information is available. First we compress past information into a low-dimensional latent space using an autoencoder, which then informs a neural network trained to parameterize targeted subgrid-scale processes. We then replace the autoencoder with symbolic equations that govern the time evolution of the latent variables, yielding additional prognostic memory variables that can be integrated alongside the resolved atmospheric state. We evaluate this approach on two systems: the Lorenz-96 model (online) and surface precipitation from high-resolution atmospheric simulations (offline). A forced multivariate linear ordinary differential equation recovers most of the added value achieved by the autoencoder-based approach in both experiments. Benchmarked against diagnostic parameterizations without memory, our memory-informed approach improves climate statistics and temporal structure, including a realistic diurnal cycle of tropical land precipitation.

### 🤖 AI 总结

**一句话总结**：Hybrid AI-physics climate modeling aims to improve coarse (~100km-resolution) Earth system models by learning to parameterize subgrid processes from high-fidelity data. However, this so far mostly inv...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Prognostic, Variables, Convective, Parameterizations, via, Symbolic, Distillation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24882v1) | [下载PDF](https://arxiv.org/pdf/2609.24882v1.pdf)

---

## [30. When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series Forecasting](https://arxiv.org/abs/2609.24862v1)

**作者**：Yifan Hu, Xilin Dai, Zhiyuan Qu 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-21

### 📄 论文摘要

Agentic time series forecasting concerns systems whose underlying mechanisms evolve, making the relative effectiveness of numerical models, reasoning strategies, and intervention rules inherently time-varying. Consequently, a time series agent must adapt the forecasts it produces and the orchestration policy that determines which components to trust and how to coordinate them. The deployment process naturally provides supervision for this adaptation as forecast horizons elapse and realized targets reveal the effectiveness of earlier decisions. Committing all numerical expert forecasts and candidate agent paths before target observation allows each realized outcome to evaluate the entire alternative set, providing delayed feedback without additional annotation. However, existing time series agents primarily incorporate prior experience through forecast refinement, reflection, or retrieval, without systematically converting realized outcomes into persistent updates to the joint orchestration policy governing later origins. To exploit this delayed feedback systematically, we introduce TimEvolve, a frozen-backbone time series agent that converts each realized outcome into persistent joint updates of expert trust, agent path selection, and intervention strength. A temporally ordered predict, reveal, and update protocol applies this feedback to subsequent forecasts. Experiments across eight Time-MMD domains show that TimEvolve achieves the best average MSE and MAE ranks among fifteen methods and the lowest errors on both metrics in seven domains. These results demonstrate the value of learning forecasting policies from the futures encountered during deployment.

### 🤖 AI 总结

**一句话总结**：Agentic time series forecasting concerns systems whose underlying mechanisms evolve, making the relative effectiveness of numerical models, reasoning strategies, and intervention rules inherently time...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Tomorrow, Becomes, Today, Self-Evolving, Policies, Agentic, Time-Series

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.24862v1) | [下载PDF](https://arxiv.org/pdf/2609.24862v1.pdf)

---

