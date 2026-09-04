# arXiv AI 论文日报 | 2026-09-04

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (10 篇)
- [cs.LG](#csLG) (4 篇)

---

## cs.AI

## [1. A Computationally Feasible Framework for Causal Probabilistic Explanation](https://arxiv.org/abs/2609.04177v1)

**作者**：Rafal Urbaniak, Sam Witty, Daniel Waxman 等 10 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-03

### 📄 论文摘要

Explaining why a specific outcome occurred, and which inputs deserve the blame or credit, is central to philosophical, scientific, and policy analysis. Existing tools split into two camps. The theory of actual causality (AC) gives principled verdicts, but only for toy-sized models, because computing them requires enumerating counterfactual scenarios. Scalable attribution methods like SHAP (or even causal SHAP) at least partially ignore the causal structure that generated the data, and can give answers that conflict with a careful causal analysis. We close this gap with Probabilistic Causal Impact (PCI).   PCI builds on actual causality and on Pearl's notions of probability of necessity and sufficiency, but recasts the question of explainability as an estimation problem on a probabilistic causal model that is easily approximated via Monte Carlo. By specifying a distribution over "candidate explanations," a distribution over counterfactual values, and a scoring function, PCI provides tractable, causally grounded, graded explanations, generalizing AC and Pearl's probability of causation as degenerate cases.   We evaluate PCI in synthetic and real-world examples, spanning consistency checks with AC, scaling experiments, complex continuous-valued dynamical systems, and a real-world deployed causal machine learning model trained on millions of datapoints.

### 🤖 AI 总结

**一句话总结**：Explaining why a specific outcome occurred, and which inputs deserve the blame or credit, is central to philosophical, scientific, and policy analysis. Existing tools split into two camps. The theory ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Computationally, Feasible, Framework, Causal, Probabilistic, Explanation, Explaining, why

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04177v1) | [下载PDF](https://arxiv.org/pdf/2609.04177v1.pdf)

---

## [2. A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms](https://arxiv.org/abs/2609.04170v1)

**作者**：Davide Paglieri, Logan Cross, Tim Genewein 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-03

### 📄 论文摘要

Multi-agent AI science ecosystems rely on agents possessing tools that allow them to communicate, coordinate, and build on each other's work. Yet this shared infrastructure can also introduce vulnerabilities by creating a substrate for the contagious spread of unintended and undesirable behaviors. We report a case study on a research collective of 100 autonomous LLM agents tasked with proving formal mathematical conjectures. Within the swarm, cheating spontaneously emerged and was later challenged by whistleblowers - both without any external intervention. When a single agent discovered an exploit in the evaluation system, it propagated across the collective via a shared knowledge library and later through peer-to-peer messages. Despite early reluctance, a cohort of agents adopted the exploit in response to competitive pressure. A separate group of agents produced an emergent counter-response: auditing fraudulent proofs, alerting peers across broadcast and private channels, staging boycotts, lodging formal complaints, and proposing validation patches. In recent incidents, agent swarms coordinated covertly through improvised side-channels (Dalton and Wallace, 2026; Greenblatt et al., 2026). Our setting differs: the same transparent channels that carried the exploit also gave non-cheating agents the visibility they needed to detect fraud, organize resistance, and enforce norms. We cast the problem of managing the agents' shared infrastructure as the knowledge commons governance problem (Ostrom, 1990). To protect the commons from exploits, we propose to adopt institutional mechanisms, such as graduated sanctioning and collective-choice rules, to support decentralized self-governance in autonomous swarms.

### 🤖 AI 总结

**一句话总结**：Multi-agent AI science ecosystems rely on agents possessing tools that allow them to communicate, coordinate, and build on each other's work. Yet this shared infrastructure can also introduce vulnerab...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Case, Study, Emergent, Cheating, Whistleblowing, Autonomous, Research, Swarms

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04170v1) | [下载PDF](https://arxiv.org/pdf/2609.04170v1.pdf)

---

## [3. Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments](https://arxiv.org/abs/2609.04148v1)

**作者**：Jie Wu, Zhenru Zhang, Beichen Zhang 等 14 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-09-03

### 📄 论文摘要

As terminal-based code agents become prevalent, agent trajectories have accumulated at scale, while realistic, executable environments remain scarce. However, environments are what agent post-training actually requires: each can be re-queried into many verifiable tasks and provides execution feedback, whereas a trajectory is a single frozen demonstration. Rather than generating environments from scratch, we observe that the tool-execution history in existing trajectories exposes the structure and contents of the environments in which they ran, making it possible to reconstruct those environments from the trajectories themselves. Thus, we introduce Terminal-Universe, a framework which turns each trajectory into a reusable environment and explores it for synthesizing new tasks and continued interactions. Specifically, Terminal-Universe replays the file operations recorded in a trajectory to restore each file before the agent modified it, yielding a partial workspace; a completion agent then supplies the missing files and dependencies. On this recovered workspace, we both reconstruct the original intent task and synthesize entirely new ones. Besides, we also scale the tasks along two complementary axes: breadth and depth. For breadth, we mine directional dependency relations between related environments and synthesize cross-workspace queries spanning multiple codebases, as developers routinely do in real-world development. For depth, we extend the initial single-turn query into a multi-round session that captures iterative user feedback and requirement refinement via a user agent. Applied to public terminal agent trajectories, Terminal-Universe produces 37.3k task-sufficient environments. Supervised fine-tuning of Qwen3.5-27B on this corpus improves single-round performance on Terminal-Bench 2.1 by 11.9 points and multi-round performance on EvoCode-Bench v2 MT@4 by 13.8 points.

### 🤖 AI 总结

**一句话总结**：As terminal-based code agents become prevalent, agent trajectories have accumulated at scale, while realistic, executable environments remain scarce. However, environments are what agent post-training...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, As, Terminal-Universe, Turning, Trajectories, Scalable, Terminal, Environments

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04148v1) | [下载PDF](https://arxiv.org/pdf/2609.04148v1.pdf)

---

## [4. Efficient Test-Time Adaptation through Human-AI Interaction](https://arxiv.org/abs/2609.04141v1)

**作者**：Zora Zhiruo Wang, Apurva Gandhi, Rulin Shao 等 25 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-03

### 📄 论文摘要

AI agents are trained on population-scale data to encode broad capabilities spanning those of many practitioners. Yet the artifacts they produce rarely meet the personal bar professionals need to stake their reputation on. On realistic, open-ended tasks where success criteria are heterogeneous and insufficiently documented, individual expertise lives precisely in the elevation and departure from the average. In practice, iterative human-agent interaction surfaces criteria that users cannot fully specify up front, yet apply repeatedly across tasks. We argue this cross-session interaction data is a rich, underused signal for closing the gap to individual expertise. In this work, we propose test-time adaptation through human-agent interaction (TAHI), which integrates these signals into agent context and weights, and crystallizes each user's training and evaluation criteria via an evolving rubric module. We adapt agents to 30 individuals in two high-utility domains, writing and visual creation, on a total of 600 tasks. Our agents improve solo task success by 4.5-20.9% within only tens of tasks. Meanwhile, our evolving rubric module serves as a scalable annotation tool, creating evaluation rubrics that catch 16.0-22.3% more failures than those from LMs or humans alone. While agents are adapted towards individuals, we show these personalized agents also produce improvements in success of up to 8.8% that generalize across users.

### 🤖 AI 总结

**一句话总结**：AI agents are trained on population-scale data to encode broad capabilities spanning those of many practitioners. Yet the artifacts they produce rarely meet the personal bar professionals need to stak...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Efficient, Test-Time, Adaptation, through, Human-AI, Interaction, trained

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04141v1) | [下载PDF](https://arxiv.org/pdf/2609.04141v1.pdf)

---

## [5. The Natural Language Interaction Protocol and Standard for AI Agents](https://arxiv.org/abs/2609.04135v1)

**作者**：Luyi Xing, Rasit Onur Topaloglu, Ranjan Sinha 等 12 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-03

### 📄 论文摘要

AI agents are increasingly being developed and deployed across organizations using heterogeneous agent-development frameworks, AI models, tool interfaces, protocols, and execution environments. To realize their potential social and business impact, these agents must be able to interoperate through a common communication protocol. The Natural Language Interaction Protocol (NLIP), developed by researchers and practitioners across companies and universities and standardized by Ecma International, addresses this need by defining a standards-based application-layer protocol for AI-agent interaction. NLIP provides a lightweight semantic message envelope that can be carried over existing transports such as HTTP/HTTPS, WebSocket, and AMQP, while allowing NLIP-aware agents and gateways to adapt between clients, agents, local context stores, ontologies, tools, enterprise services, and heterogeneous underlying protocols. This paper presents the motivation and design rationale of NLIP, its message model and transport bindings, security-by-design considerations, reference implementation, representative applications, adoption signals, and relationship to emerging agent protocols such as MCP and A2A.

### 🤖 AI 总结

**一句话总结**：AI agents are increasingly being developed and deployed across organizations using heterogeneous agent-development frameworks, AI models, tool interfaces, protocols, and execution environments. To rea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Natural, Language, Interaction, Protocol, Standard, increasingly, being

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04135v1) | [下载PDF](https://arxiv.org/pdf/2609.04135v1.pdf)

---

## [6. Environment Evolution for Terminal Agents](https://arxiv.org/abs/2609.04128v1)

**作者**：Zhiyuan Fan, Tinghao Yu, Yuanjun Cai 等 12 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-03

### 📄 论文摘要

Scaling interactive and verifiable environments is critical for training terminal agents. As frontier models become more capable, environments synthesized from scratch become less challenging and thus provide limited learning signals. Recent co-evolution methods iteratively synthesize environments near the model's learnable frontier based on weaknesses exposed during rollouts. However, their dependence on on-policy rollouts limits generalization and the continuous provision of learning signals as the model becomes stronger. In this paper, we propose environment evolution, which incrementally increases environment difficulty off-policy and schedules the evolved environments generation by generation during training to provide continuous learning signals. We derive three evolution directions that influence environment difficulty from the multi-turn learning objective and then implement evolution along these directions through a loop-engineered multi-agent harness. Quantitative rollout experiments with Hy4 preview, Claude Opus 5, and GPT-5.6 Sol show that environment evolution consistently produces more difficult environments. We validate its effectiveness on Qwen3.6-27B and Qwen3.6-35B-A3B through simple long-horizon RL training, improving their performance by 14.4 and 18.0 percentage points on Terminal-Bench 2.1, respectively.

### 🤖 AI 总结

**一句话总结**：Scaling interactive and verifiable environments is critical for training terminal agents. As frontier models become more capable, environments synthesized from scratch become less challenging and thus...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Environment, Evolution, Terminal, Scaling, interactive, verifiable, environments

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04128v1) | [下载PDF](https://arxiv.org/pdf/2609.04128v1.pdf)

---

## [7. Epistemic Warrant for LLM Recommendations: Characterizing the Basis for Reliance When Ground Truth Is Unavailable](https://arxiv.org/abs/2609.04127v1)

**作者**：Shai Vardi, João Sedoc  
**分类**：cs.AI  
**发布时间**：2026-09-03

### 📄 论文摘要

Large language models are increasingly used to support organizational decisions, yet users often lack a principled basis for assessing whether to rely on a specific recommendation. Existing approaches typically evaluate broad model properties, such as reliability, uncertainty, or robustness, or focus on user trust, rather than the underlying basis for relying on an individual recommendation. Adapting theoretical foundations from epistemology, we introduce epistemic warrant, a decision-level construct that characterizes the stability of a model's preference and the scope over which that preference holds. We operationalize this construct through a four-tier reliance certificate for pairwise recommendations, distinguishing among unstable, context-dependent, locally supported, and broadly supported recommendations. We validate the construct using contemporary methodologies: known-groups tests successfully recover expert-prespecified warrant orderings, and stronger warrants systematically align with independent consensus from crowd workers. Furthermore, we demonstrate that epistemic warrant provides information distinct from verbalized confidence and is not readily explained by decision difficulty. Ultimately, this framework offers a theoretically grounded, implementable approach for characterizing the warrant of individual LLM recommendations when objective ground truth is unavailable.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly used to support organizational decisions, yet users often lack a principled basis for assessing whether to rely on a specific recommendation. Existing approaches...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Epistemic, Warrant, Recommendations, Characterizing, Basis, Reliance, When

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04127v1) | [下载PDF](https://arxiv.org/pdf/2609.04127v1.pdf)

---

## [8. DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training](https://arxiv.org/abs/2609.04094v1)

**作者**：Shubham Gandhi, Saurabh Goyal, Kiran Kate 等 4 位作者  
**分类**：cs.AI, cs.LG, cs.SE  
**发布时间**：2026-09-03

### 📄 论文摘要

Reinforcement Learning from Verifiable Rewards works well when a task has a programmatic checker, but most long-horizon agent domains have none. We work in the outcome-blind setting, where ground-truth success signals are not available. Multi-criteria rubrics are a popular way to supply such a reward; they are scored once per trajectory, but a single scalar is a poor signal across tens of steps. We propose DRACO: Distributing Rubric-based Advantage for Credit Optimization. It generates rubrics dynamically during training to track the policy's evolving capability, scores those rubrics once per completed trajectory, and redistributes that judgment over the steps responsible for annotated rubrics to produce differentiated per-step advantages in GRPO. The redistribution is closed-form and does not introduce any trained attribution module. On AppWorld, DRACO gains 15.9 points over the base model and 5.3 points over GRPO trained with a sparse ground-truth reward, despite not using any verifiers itself. On out-of-domain Tau-Bench, it gains 5.3 points over the base model even without a frontier judge, beating both ground-truth-reward training and other rubric-based training settings. The code for DRACO is available at https://github.com/IBM/draco.

### 🤖 AI 总结

**一句话总结**：Reinforcement Learning from Verifiable Rewards works well when a task has a programmatic checker, but most long-horizon agent domains have none. We work in the outcome-blind setting, where ground-trut...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, DRACO, Fine-Grained, Credit, Assignment, Dynamic, Rubrics, Long-Horizon

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04094v1) | [下载PDF](https://arxiv.org/pdf/2609.04094v1.pdf)

---

## [9. Spurious Advantage Hidden in GRPO](https://arxiv.org/abs/2609.04063v1)

**作者**：Jiamian Wang, Samyadeep Basu, Koustava Goswami 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-03

### 📄 论文摘要

Group Relative Policy Optimization (GRPO) is widely studied for reinforcement learning with verifiable rewards, where its advantage estimator assigns each rollout a magnitude from within-group reward statistics. In the common case, this magnitude rewards rollouts that reach the correct answer through reasoning. Yet, an overlooked case shares the same surface: a rollout may land on it by guessing, and the formula still assigns a high magnitude, which we identify as the spurious advantage. This arises in three cases: bounded-answer tasks with a small candidate set; open-answer sets hosting bounded sub-cases; and search agents whose budget opens many paths to the same answer. In all three, this misleads the policy toward guess-like behaviors. We propose SIGNBALANCE, whose magnitude is composition-free: it keeps the verifier sign, uses a global scale, and restores zero-mean balance via a stop-gradient per-class rescaling. Across math and search agent benchmarks at different scales, SIGNBALANCE matches GRPO on open-answer math and improves on bounded-answer math and search agents. Code will be released.

### 🤖 AI 总结

**一句话总结**：Group Relative Policy Optimization (GRPO) is widely studied for reinforcement learning with verifiable rewards, where its advantage estimator assigns each rollout a magnitude from within-group reward ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Spurious, Advantage, Hidden, GRPO, Group, Relative, Policy, Optimization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04063v1) | [下载PDF](https://arxiv.org/pdf/2609.04063v1.pdf)

---

## [10. IRWOZ 2.0: A Large Language Model-driven Dialogue Dataset for Industrial Robot Conversations](https://arxiv.org/abs/2609.04030v1)

**作者**：Chen Li, Dimitrios Chrysostomou  
**分类**：cs.AI  
**发布时间**：2026-09-03

### 📄 论文摘要

IRWOZ has improved industrial human-robot interaction (HRI) dialogue systems through domain-specific annotations. However, its initial version contains substantial noise in dialogue states and utterances, limiting state-tracking accuracy. We introduce IRWOZ 2.0, which addresses these limitations through large language model (LLM) enhanced generation (Mistral/Claude-3.5) and quality refinements. Our improved dataset expands to 390 dialogues across 4 industrial domains (Assembly, Delivery, Position, Relocation), featuring manual corrections and automated typo removal. Benchmark experiments on dialogue state tracking demonstrate significant improvements, with GPT-2's BLEU-4 score increasing from 0.1651 to 0.5604 compared to original IRWOZ. To support industrial HRI research, we publicly released IRWOZ 2.0 dataset at https://ieee-dataport.org/documents/irwoz-20-large-language-model-driven-dialogue-dataset-industrial-robot-conversations

### 🤖 AI 总结

**一句话总结**：IRWOZ has improved industrial human-robot interaction (HRI) dialogue systems through domain-specific annotations. However, its initial version contains substantial noise in dialogue states and utteran...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IRWOZ, Large, Language, Model-driven, Dialogue, Dataset, Industrial, Robot

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04030v1) | [下载PDF](https://arxiv.org/pdf/2609.04030v1.pdf)

---

## cs.CL

## [11. Compile by Training: Turning Natural-Language Specifications into Local Neural Functions](https://arxiv.org/abs/2609.04199v1)

**作者**：Yuntian Deng, Pengyu Nie, Stuart Shieber  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-09-03

### 📄 论文摘要

Many recurring text functions are easy to describe but difficult to implement with rules, while calling a large remote model for every input introduces repeated cost, latency, and dependency on a provider. We present compile by training, which turns a natural-language specification into a reusable neural function. At compile time, teacher models generate task-specific examples that are used to train a small adapter for a compact interpreter. The resulting function runs without the teachers and can be stored, versioned, and composed like ordinary software. On FuzzyBench-Hard, a subset on which the Program-as-Weights fast compiler produced no exact matches, compile by training reaches 83.6% semantic accuracy. This higher accuracy comes with a higher compile-time cost: roughly a minute rather than seconds for the fast compiler. We deploy the compiler in a public interactive service and demonstrate compiled functions in a multi-site website helper, a language-controlled 3D avatar, and a bidirectional English-Claudish translator.

### 🤖 AI 总结

**一句话总结**：Many recurring text functions are easy to describe but difficult to implement with rules, while calling a large remote model for every input introduces repeated cost, latency, and dependency on a prov...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Compile, Training, Turning, Natural-Language, Specifications, Local, Neural, Functions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04199v1) | [下载PDF](https://arxiv.org/pdf/2609.04199v1.pdf)

---

## [12. ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize](https://arxiv.org/abs/2609.04197v1)

**作者**：Lihao Liu, Peng Tang, Kunwar Yashraj Singh 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-03

### 📄 论文摘要

Evolutionary prompt optimizers such as GEPA suffer from prompt bloat: each iteration appends rules and caveats, producing prompts up to 3$\times$ longer yet no more accurate. We trace this to three deficiencies - incomplete error observation, limited search diversity, and unreliable selection - and propose ESPO (Error-Structured Prompt Optimization), which decomposes prompt optimization into three phases: Diagnose clusters all training errors into structural patterns in one round; Propose generates candidates via four complementary strategies with independent biases; Select applies bootstrap stability selection. On seven public NLP benchmarks - Tweet, MMLU, GSM8K, HotpotQA, ScoNe, HoVer, and PUPA - ESPO improves average accuracy by $+$3.76 pp over the state-of-the-art (74.67% vs 70.91% for GEPA), matching or exceeding GEPA on every dataset while producing prompts 47% shorter (1,004 vs 1,878 chars) and faster at inference. Cross-model experiments across four additional student models (Gemma 3 12B, Mistral 14B, Qwen3 32B, Claude Haiku 4.5) show ESPO yields the best average accuracy on every model tested, with the largest gap on Qwen3 GSM8K (15.00% $\to$ 91.40%). A generalization bound (Appendix) grounds each phase in a corresponding term of the test-time gap, and the ablation confirms a key prediction: adding diversity without bootstrap selection actually hurts performance ($-$1.20%).

### 🤖 AI 总结

**一句话总结**：Evolutionary prompt optimizers such as GEPA suffer from prompt bloat: each iteration appends rules and caveats, producing prompts up to 3$\times$ longer yet no more accurate. We trace this to three de...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ESPO, Error-Structured, Prompt, Optimization, via, Diagnose, Diversify, Stabilize

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04197v1) | [下载PDF](https://arxiv.org/pdf/2609.04197v1.pdf)

---

## [13. Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning](https://arxiv.org/abs/2609.04194v1)

**作者**：Kevin Du, Alexander Hoyle, Laura Ruis 等 4 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-09-03

### 📄 论文摘要

Reasoning traces from chain-of-thought models appear to offer a legible window into how a model arrives at its answer. A growing body of work treats them as such, using LLM judges to diagnose errors, evaluate faithfulness, and provide step-level supervision via process reward models and generative critics. These practices rely on the text of a reasoning step carrying information about its functional role. But does the text actually encode information about which reasoning steps matter? We operationalize the importance of a reasoning step as its advantage: the change in expected reward, e.g., producing the correct final answer, from including that step, estimated via Monte Carlo rollouts. Basing ground truth on these estimates, we evaluate whether LLM judges can identify high-advantage steps and find that sufficiently capable LLMs can outperform a prevalence baseline but fall well short of a noise ceiling. Fine-tuning a model as a step-level critic yields strong improvement for incorrect responses but remains distant from ceiling for correct responses, suggesting that step importance is only partially recoverable from the text of the reasoning trace. Our findings contribute to a growing body of chain-of-thought faithfulness work that cautions against treating the legibility of reasoning traces as interpretability, especially with implications for process reward modeling.

### 🤖 AI 总结

**一句话总结**：Reasoning traces from chain-of-thought models appear to offer a legible window into how a model arrives at its answer. A growing body of work treats them as such, using LLM judges to diagnose errors, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Legibility, Not, Interpretability, Comparing, Judged, Actual, Importance, Chain-Of-Thought

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04194v1) | [下载PDF](https://arxiv.org/pdf/2609.04194v1.pdf)

---

## [14. Last Translation Benchmark](https://arxiv.org/abs/2609.04173v1)

**作者**：Vilém Zouhar, Niyati Bafna, Mukund Choudhary 等 244 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-03

### 📄 论文摘要

For scientific progress, we need benchmarks that test the limits of state-of-the-art models, and evaluation methods that inform us about failure cases. As models get stronger, standard benchmarks for machine translation are approaching saturation. Further, automatic translation metrics are unreliable, vulnerable to reward-hacking, and provide unactionable assessments. Even gold human evaluation is not problem-free, because it often lacks reproducibility, objectivity, and scalability. Overall, this prevents us from tracking objective progress in the field and identifying pathways for improvement. We introduce the Last Translation Benchmark, a collection of human-authored and peer-reviewed examples (texts, images, audio, videos) that break leading machine translation models. We also present a new evaluation approach: each example comes with handcrafted verification rules describing concrete failure cases on that example, therefore allowing reliable and actionable future evaluation. The Last Translation Benchmark is a live dataset that accepts ongoing contributions. The latest version is LTBv1, containing accepted contributions prior to September 1st 2026, with future releases planned as new data is continuously collected.

### 🤖 AI 总结

**一句话总结**：For scientific progress, we need benchmarks that test the limits of state-of-the-art models, and evaluation methods that inform us about failure cases. As models get stronger, standard benchmarks for ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：we, Last, Translation, Benchmark, scientific, progress, need, benchmarks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04173v1) | [下载PDF](https://arxiv.org/pdf/2609.04173v1.pdf)

---

## [15. Translation as a Decision Space: A Multi-Agent Perspective on Low-Resource Dialect Generation](https://arxiv.org/abs/2609.04048v1)

**作者**：Hasan Alkhder, Mohammad Abboush, Igor Tchappi 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-03

### 📄 论文摘要

Neural machine translation (NMT) systems typically produce a single output per input, obscuring the alternative decision trajectories implicitly available within multilingual decoding. This opacity becomes particularly problematic in low-resource dialect settings, where multiple linguistically valid realizations may differ in lexical authenticity, register, and structural stability. We propose reframing translation as a structured decision space explored by autonomous translation agents. Instead of analyzing a single output, we model distinct translation pathways as agents operating over a shared multilingual backbone. Inter-agent divergence is treated not as error but as an interpretable behavioral signal. We conduct an empirical study on Turkish--Syrian Arabic translation using three agents: (1) zero-shot direct translation, (2) dialect-stabilized translation via lightweight fine-tuning, and (3) pivot translation through English. Evaluation is performed on 5,000 dialogue sentences, while stabilization is trained on 5,000 additional Turkish--Syrian sentence pairs drawn from television dialogue and MADAR-Turk resources. Rather than optimizing for conventional performance metrics, we quantify structured behavioral displacement using dialect marker frequency, lexical proximity to standardized Arabic, and structural variance. Lightweight stabilization nearly doubles dialect marker usage, increasing it from 0.2266 to 0.4988, while significantly reducing structural instability. Pivot mediation introduces normalization pressure and measurable compression effects, whereas zero-shot translation exhibits the highest decision variance. We argue that translation divergence across agents reveals latent decision flexibility within multilingual models and we provide a principled interpretability framework for low-resource dialect generation.

### 🤖 AI 总结

**一句话总结**：Neural machine translation (NMT) systems typically produce a single output per input, obscuring the alternative decision trajectories implicitly available within multilingual decoding. This opacity be...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Multi-Agent, Translation, Decision, Space, Perspective, Low-Resource, Dialect

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04048v1) | [下载PDF](https://arxiv.org/pdf/2609.04048v1.pdf)

---

## cs.CV

## [16. Principia: Relational Physics Tests for Video Models](https://arxiv.org/abs/2609.04200v1)

**作者**：Varun Varma Thozhiyoor, Shivam Tripathi, Venkatesh Babu Radhakrishnan 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-03

### 📄 论文摘要

Evaluating physical reasoning in video models is difficult because absolute motion measurements depend on frame rate, object scale, and camera calibration, all of which are often ambiguous or unavailable in generated video. We propose a different approach. When two objects in the same scene obey the same physical law, their motions must satisfy predictable relationships, and these relationships hold independent of calibration. We introduce Principia, a benchmark that evaluates Newtonian physics through relational consistency between paired objects. Principia spans eight phenomena - gravity, restitution, friction, rotational inertia, projectile motion, momentum, pendulum, and mass-spring oscillation - across translational, rotational, collisional, and oscillatory dynamics, using real-world scenes recorded under controlled protocols. We also introduce a calibration-independent consistency score that quantifies physical violation directly in image space. Across thousands of generations from six state-of-the-art video generators, no model exceeds 0.42 on Principia despite all scoring around 0.8 on VBench. Vision-language models are evaluated on their ability to detect relational physics violations, with the best model achieving only 67% accuracy and most performing near chance level.

### 🤖 AI 总结

**一句话总结**：Evaluating physical reasoning in video models is difficult because absolute motion measurements depend on frame rate, object scale, and camera calibration, all of which are often ambiguous or unavaila...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Principia, Relational, Physics, Tests, Video, Models, Evaluating, physical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04200v1) | [下载PDF](https://arxiv.org/pdf/2609.04200v1.pdf)

---

## [17. Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States](https://arxiv.org/abs/2609.04196v1)

**作者**：Kang Liao, Yihang Luo, Xiao-Ming Wu 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-03

### 📄 论文摘要

We propose Puffin-World, a unified multimodal architecture that integrates physical understanding, spatial simulation, and 3D world generation and reconstruction without relying on external offline modules. To reliably construct and interact with 3D worlds, our framework jointly models three native world states: physics (gravity field and latitude), geometry (depth), and appearance (image), together with a unified Omni-Camera representation that supports diverse tasks and flexible motions. Beyond modeling these states, we introduce a strategy for propagating physical dynamics across future frames. By grounding absolute camera properties in the real world, Puffin-World enables physically consistent and visually stable world generation. We further couple appearance and geometry within a single generative process, jointly synthesizing each future view and reconstructing its underlying geometry. This unified paradigm enables interleaved closed-loop applications requiring synergy across multiple tasks, including mimic and self-calibrated world exploration. To scale Puffin-World to complex scenarios, we construct Puffin-16M, comprising 15 million vision-language-camera triplets and 1 million trajectories featuring various and challenging motions. To foster further research in this area, we released the code, models, and datasets.

### 🤖 AI 总结

**一句话总结**：We propose Puffin-World, a unified multimodal architecture that integrates physical understanding, spatial simulation, and 3D world generation and reconstruction without relying on external offline mo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Puffin-World, Scaling, Unified, Multimodal, Model, Native, World

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04196v1) | [下载PDF](https://arxiv.org/pdf/2609.04196v1.pdf)

---

## [18. Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised Dense Video Captioning](https://arxiv.org/abs/2609.04183v1)

**作者**：Ye-Chan Kim, Seunghee Choi, SeungJu Cha 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-09-03

### 📄 论文摘要

Weakly-Supervised Dense Video Captioning aims to localize and describe multiple events in untrimmed videos given only an ordered set of event-level captions per video. Recent work synthesizes auxiliary transition captions via LLM to provide additional vision-language alignment, but these captions lack visual grounding and are rigidly assigned to every inter-event gap at a fixed location and duration. To address these, we propose Seeing Before Synthesizing (SBS), a framework that adaptively provides visually grounded linguistic guidance only where warranted. Leveraging a VLM, we generate frame-level narratives for the inter-event gaps and detect transitions from the semantic variation across them. For identified transitions, we then refine inter-event temporal masks by blending the temporal midpoint with the semantic change point and selecting the width that maximizes vision-language alignment. Experiments on ActivityNet Captions and YouCook2 demonstrate state-of-the-art performance in both captioning and localization.

### 🤖 AI 总结

**一句话总结**：Weakly-Supervised Dense Video Captioning aims to localize and describe multiple events in untrimmed videos given only an ordered set of event-level captions per video. Recent work synthesizes auxiliar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Seeing, Before, Synthesizing, VLM-Guided, Transition, Event, Discovery, Weakly-Supervised

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04183v1) | [下载PDF](https://arxiv.org/pdf/2609.04183v1.pdf)

---

## [19. Zero-Shot Novel Depth Synthesis Using 3D Foundation Models Scene Representations](https://arxiv.org/abs/2609.04174v1)

**作者**：Denis M. Akola, David F. Fouhey  
**分类**：cs.CV  
**发布时间**：2026-09-03

### 📄 论文摘要

3D Foundation Models (3DFMs) such as VGGT have recently pushed the boundaries of 3D vision by predicting rich unified representations with feed-foward transformers. The scene representations learned by these models enable strong performance on multiple 3D vision tasks. In this paper, we investigate using their internal representations to infer 3D in the scene from new views. Our hypothesis is that in order to solve the task of 3D reconstruction, these models need to learn a representation that includes a large amount of general knowledge about 3D scenes. After showing that it is possible to decode hidden surfaces from internal 3DFM representations, we propose a method, Z3D, that estimates pointmaps in unseen views by doing latent diffusion on 3DFM representation. We show that Z3D can predict realistic depth maps for new views across multiple datasets.

### 🤖 AI 总结

**一句话总结**：3D Foundation Models (3DFMs) such as VGGT have recently pushed the boundaries of 3D vision by predicting rich unified representations with feed-foward transformers. The scene representations learned b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Zero-Shot, Novel, Depth, Synthesis, Foundation, Models, Scene

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04174v1) | [下载PDF](https://arxiv.org/pdf/2609.04174v1.pdf)

---

## [20. Persistent Identity Preservation in Generative Image Models: A Benchmark and Evaluation System](https://arxiv.org/abs/2609.04151v1)

**作者**：Mengwei Ren, Xuaner Zhang, Zhihao Xia  
**分类**：cs.CV  
**发布时间**：2026-09-03

### 📄 论文摘要

Generative image models can now produce high-quality images, follow complex instructions, and support precise edits, but they still struggle to preserve who or what is being depicted. When generating or editing images of a specific subject, identity may drift as the pose, expression, appearance, viewpoint, or surrounding scene changes. Existing subject-driven methods make fundamentally different choices about where identity is represented: through the input context (GPT-Image-2, NB2), as trainable subject-specific model parameters (LoRA), or as a persistent identity layer (PHOTA IDENTITY) reusable across generations and edits. We systematically benchmark these paradigms across subject-driven generation, editing, restoration, and multi-subject settings, with tasks designed to increasingly stress identity preservation. Our results show that identity preservation remains a distinct limitation of current generative foundation models: strong image quality and instruction following do not necessarily imply strong identity fidelity, and identity degradation becomes more pronounced under iterative edits, small subject scales, severe image degradation, and multi-subject composition. Persistent identity substantially reduces this degradation across generation, editing, and restoration, consistently improving identity preservation when applied to different foundation models while maintaining comparable instruction adherence and perceptual image quality. These results suggest that identity does not simply emerge from increasingly capable generative models, but can instead be represented as persistent subject knowledge that is composed independently with the underlying generative model.

### 🤖 AI 总结

**一句话总结**：Generative image models can now produce high-quality images, follow complex instructions, and support precise edits, but they still struggle to preserve who or what is being depicted. When generating ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Persistent, Identity, Preservation, Generative, Image, Models, Benchmark, Evaluation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04151v1) | [下载PDF](https://arxiv.org/pdf/2609.04151v1.pdf)

---

## [21. BooM-VVT: Boosting Mask-Free Video Virtual Try-On with Image-Level Pseudo Data](https://arxiv.org/abs/2609.04120v1)

**作者**：Wei Zhang, Xin Li, Peishu Shi 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-03

### 📄 论文摘要

Video virtual try-on (VVT) aims to generate realistic videos of a person wearing a target garment. Recent methods leverage a keyframe-driven video generation paradigm to improve in-the-wild performance, yet they still rely on masks to localize try-on regions, making them vulnerable to large motions and severe occlusions. Although mask-free image-based try-on methods have shown promising results by leveraging large-scale pseudo data, extending this paradigm to videos remains difficult, as constructing video-level pseudo data is prohibitively expensive. Furthermore, coarse keyframe sampling and the scarcity of multi-view try-on data limit existing keyframe-driven methods in maintaining garment consistency and handling diverse try-on tasks.   To address these challenges, we propose BooM-VVT, a mask-free VVT framework built upon the keyframe-driven paradigm. To achieve mask-free VVT, we introduce a multi-stage training strategy that leverages image-level pseudo data for mask-free localization learning, substantially reducing the need for costly video-level pseudo data. To improve garment consistency, we propose Garment-Sensitive Keyframe Sampling, which selects keyframes based on garment-relevant body regions to better capture garment appearance. We further introduce Frame-Shared 3D-RoPE to establish spatiotemporal correspondences between keyframes and target video frames for accurate garment-detail transfer. Finally, we construct OmniView, a large-scale multi-view try-on dataset to support reliable try-on video generation under complex camera viewpoints and diverse try-on tasks. Extensive experiments demonstrate that BooM-VVT achieves superior temporal consistency and garment fidelity over existing methods. Project page: https://boomvvt.github.io/boomvvt.

### 🤖 AI 总结

**一句话总结**：Video virtual try-on (VVT) aims to generate realistic videos of a person wearing a target garment. Recent methods leverage a keyframe-driven video generation paradigm to improve in-the-wild performanc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BooM-VVT, Boosting, Mask-Free, Video, Virtual, Try-On, Image-Level, Pseudo

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04120v1) | [下载PDF](https://arxiv.org/pdf/2609.04120v1.pdf)

---

## [22. Efficient Semantic Understanding from Digital Foveation](https://arxiv.org/abs/2609.04088v1)

**作者**：Caterina Caccavella, Vittorio Fra, Andreas Ziegler 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-03

### 📄 论文摘要

Dense semantic segmentation allocates computational resources uniformly across the entire image, regardless of scene complexity or task relevance. Inspired by biological vision, we investigate whether semantic understanding can be achieved more efficiently through digital foveated perception. We introduce a lightweight active-vision pipeline that combines saliency-driven fixation selection, high-resolution foveal observations, low-resolution contextual information, semantic accumulation, and adaptive computation. Beyond conventional dense prediction metrics, we use object-level evaluation to measure semantic understanding under sparse observations. On ADE20K-Object, a single foveated observation achieves 95.9% of the baseline Top-1 accuracy and 96.9% of the baseline Top-3 accuracy while requiring only 4.7% of the computational cost. At the scene level, semantic accumulation recovers 90.6% of the baseline object recall while using 58.6% of the computation. These results suggest that substantial semantic understanding can emerge from sparse observations when computation is allocated selectively, highlighting active vision as an efficient alternative to uniform dense processing and motivating evaluation protocols beyond conventional pixel-wise segmentation metrics.

### 🤖 AI 总结

**一句话总结**：Dense semantic segmentation allocates computational resources uniformly across the entire image, regardless of scene complexity or task relevance. Inspired by biological vision, we investigate whether...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Efficient, Semantic, Understanding, Digital, Foveation, Dense, segmentation, allocates

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04088v1) | [下载PDF](https://arxiv.org/pdf/2609.04088v1.pdf)

---

## [23. CORE: Improving Compositional Reasoning in MLLM Embedding via Reranker Distillation](https://arxiv.org/abs/2609.04083v1)

**作者**：Tingyu Song, Mingxin Li, Yanzhao Zhang 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.CL, cs.IR  
**发布时间**：2026-09-03

### 📄 论文摘要

MLLM-based embedding models remain limited in compositional retrieval, often failing to distinguish scenes containing the same concepts but different attribute-object bindings. Yet the same backbone can resolve such distinctions when used as a cross-attentive reranker, motivating us to distill its compositional judgments into the embedding model. We propose CORE, which synthesizes candidate lists spanning five compositional matching levels and introduces a Rank-KL objective that trains the embedding model to reproduce the reranker's fine-grained ranking. We further introduce a graded evaluation protocol and compare contrastive learning, pairwise CoSENT, and listwise Rank-KL under the same data and tuning budget. Our comparison shows that both CoSENT and Rank-KL use the multi-level supervision more effectively than contrastive learning, with Rank-KL achieving the strongest overall performance. Across three compositional reasoning benchmarks (COLA, SUGARCREPE++, NEGBENCH), CORE-RERANKER-8B achieves an 82.7% total average, outperforming Jina-Reranker by 10.7 points, while CORE-EMBED-8B achieves the best total average (0.666) among all evaluated embedding models. The improvements transfer to the MCMR benchmark without sacrificing retrieval performance on COCO and Flickr30K.

### 🤖 AI 总结

**一句话总结**：MLLM-based embedding models remain limited in compositional retrieval, often failing to distinguish scenes containing the same concepts but different attribute-object bindings. Yet the same backbone c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CORE, Improving, Compositional, Reasoning, MLLM, Embedding, via, Reranker

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04083v1) | [下载PDF](https://arxiv.org/pdf/2609.04083v1.pdf)

---

## [24. Editable Visual Design](https://arxiv.org/abs/2609.04034v1)

**作者**：Junyan Ye, Wei Liu, Dongzhi Jiang 等 12 位作者  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-09-03

### 📄 论文摘要

While diffusion base models such as GPT-Image-2 and Nano-Banana exhibit remarkable visual expressiveness, their end-to-end generation inherently yields flattened bitmaps with error-prone text, precluding layer-wise post-editing. Conversely, code-based visual generation via Coding Agents provides precise layout control and decoupled layers, yet remains constrained by a lack of global aesthetic intuition and the difficulty of coding complex visual assets.   To address this, we propose Editable Visual Design, a new paradigm driven by a Coding Agent. We designate the VLM as the ``creative brain'' for requirement comprehension, task planning, and aesthetic judgment, while utilizing the image generation model as an on-demand ``visual world simulator'' to synthesize standalone visual assets. Operating under an ``imagine first, then act'' closed-loop workflow, the agent generates isolated assets, writes native HTML/CSS, and iteratively refines the design against visual rendering feedback.   Furthermore, Agent Design Replay faithfully reproduces the creative and reasoning trajectory akin to that of professional human designers. Ultimately, the system delivers editable artifacts with decoupled layers and real text, enabling users to perform intuitive mouse dragging and layout adjustments on a graphical user interface. Validations on posters, infographics, and other scenarios show that this paradigm successfully achieves both refined aesthetics and production-grade editability.

### 🤖 AI 总结

**一句话总结**：While diffusion base models such as GPT-Image-2 and Nano-Banana exhibit remarkable visual expressiveness, their end-to-end generation inherently yields flattened bitmaps with error-prone text, preclud...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Editable, Visual, Design, While, base, models, such

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04034v1) | [下载PDF](https://arxiv.org/pdf/2609.04034v1.pdf)

---

## [25. DSAQuant: Denoising-Stage-Aligned Quantization-Aware Training for Video Generation](https://arxiv.org/abs/2609.04031v1)

**作者**：Shuaiting Li, Zelin Gao, Haibin Shen 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-03

### 📄 论文摘要

Video diffusion models (VDMs) have achieved impressive progress in text-to-video generation, but their high memory and computational costs hinder practical deployment. Quantization-aware training (QAT) is an effective solution for compressing and accelerating advanced generative models without runtime overhead at inference. However, existing QAT methods suffer from a distinctive challenge in VDMs: while they often preserve prompt semantics, global layout, and coarse motion, the quantized model severely degrades visual details, texture fidelity, and sharpness. In this paper, we trace this degradation to the timestep-agnostic design of conventional quantization pipelines, which overlooks the stage-wise functionality of video denoising. In VDMs, early denoising steps mainly establish global structure and motion, whereas middle and late steps refine local appearance and high-frequency details. Based on this insight, we propose DSAQuant, a Denoising-Stage-Aligned Quantization-aware training framework for VDMs. During training, Denoising-Stage Oriented Supervision preserves teacher distillation in early steps for stable structure planning, while shifting later steps toward target-driven optimization to enhance detail reconstruction. During inference, Denoising-Stage Gated Guidance disables CFG in the final denoising steps to prevent it from amplifying quantization-induced errors into high-frequency artifacts. Extensive experiments on the Wan and CogVideoX families under W4A4 and W3A3 settings show that DSAQuant consistently outperforms the SOTA QAT baseline, improving the VBench average score by up to 6.60 under aggressive W3A3 quantization while preserving strong text-video alignment. These results demonstrate that effective VDM quantization requires not only reducing quantization error, but also aligning quantization training and inference with the stage-wise nature of video diffusion.

### 🤖 AI 总结

**一句话总结**：Video diffusion models (VDMs) have achieved impressive progress in text-to-video generation, but their high memory and computational costs hinder practical deployment. Quantization-aware training (QAT...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, DSAQuant, Denoising-Stage-Aligned, Quantization-Aware, Training, Video, Generation, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04031v1) | [下载PDF](https://arxiv.org/pdf/2609.04031v1.pdf)

---

## [26. Stable and Scalable Bundle Adjustment of Holistic 3D Structures](https://arxiv.org/abs/2609.04026v1)

**作者**：Shaohui Liu, Rémi Pautrat, Daniel Barath 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-03

### 📄 论文摘要

Bundle Adjustment (BA) is a cornerstone of 3D computer vision and has benefited from decades of advances in sparse optimization and numerical methods. It was originally developed for jointly optimizing camera intrinsics, poses and sparse 3D points. While extensions incorporate lines and other primitives, integrating richer geometric structures such as parallelism, coplanarity, or wireframes often introduces significantly increased computational cost and reduced numerical stability. In this paper, we propose a unified framework that extends bundle adjustment to jointly optimize geometric features and higher-order relations. We first introduce a taxonomy that distinguishes scalable geometric features with direct 2D measurements (e.g., points and lines), from groups encoding higher-order relations (e.g., coplanarity, parallelism, etc.), where we show that groups can be modeled as camera-like entities within the bundle adjustment framework. Building on this formulation, we propose that both group constraints and cross-feature relations (i.e., point-line associations) can be expressed through 2D reprojection measurements. By formulating group-induced and cross-feature reprojection errors, we preserve the sparsity structure of classical point-based BA under Schur elimination, while avoiding direct 3D regularization that degrades the conditioning and stability. Experiments on both real-world and synthetic datasets demonstrate runtime performance comparable to classical point-only bundle adjustment, while producing significantly richer 3D structures and improved geometric accuracy.

### 🤖 AI 总结

**一句话总结**：Bundle Adjustment (BA) is a cornerstone of 3D computer vision and has benefited from decades of advances in sparse optimization and numerical methods. It was originally developed for jointly optimizin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, 3D, Stable, Scalable, Bundle, Adjustment, Holistic, Structures

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04026v1) | [下载PDF](https://arxiv.org/pdf/2609.04026v1.pdf)

---

## cs.LG

## [27. A Low-Cost, Open Platform for End-to-End Autonomous Driving on a Miniature Ackermann Vehicle](https://arxiv.org/abs/2609.04147v1)

**作者**：Gustavo Claudio Karl Couto, Eric Aislan Antonelo, Gabriel George Zipperer  
**分类**：cs.LG, cs.AI, cs.RO  
**发布时间**：2026-09-03

### 📄 论文摘要

This paper presents a low-cost, open experimental platform for research in end-to-end autonomous driving with miniature Ackermann vehicles. The platform combines a physical vehicle, a printed urban track, data collection tools, trajectory registration, and a Webots digital twin, enabling controlled experiments that connect simulation-based autonomous-driving methods to real-world execution. As a first baseline, we implement command-conditioned behavior cloning, in which a neural policy receives an on-board camera image and a high-level navigation command and outputs steering and speed. The system is evaluated both on the physical vehicle and in simulation. In real closed-loop experiments, the learned policy follows lanes and executes commanded turns, reaching a mean cross-track error of 6.1 cm with respect to the reference route, close to the 4.7 cm observed in human demonstrations. In the digital twin, camera field of view has a strong effect on performance, reducing the mean cross-track error from 35.6 to 3.3 cm when widened from 58 to 120 degrees. Using the digital twin to generate synthetic driving data and a learned sim-to-real image translator to reduce the appearance gap, we further show that a higher-capacity policy trained on this synthetic data combined with real demonstrations is the only configuration that completes all four track routes in closed loop, whereas the compact baseline and the same network trained on real data alone complete fewer. These results establish the open platform as a practical testbed for sim-to-real studies and provide an initial command-conditioned imitation-learning baseline; we release it to support reproducible research.

### 🤖 AI 总结

**一句话总结**：This paper presents a low-cost, open experimental platform for research in end-to-end autonomous driving with miniature Ackermann vehicles. The platform combines a physical vehicle, a printed urban tr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Low-Cost, Open, Platform, End-to-End, Autonomous, Driving, Miniature, Ackermann

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04147v1) | [下载PDF](https://arxiv.org/pdf/2609.04147v1.pdf)

---

## [28. Prospective Coding Improves Learning in Deep Continuous-Time Recurrent Networks](https://arxiv.org/abs/2609.04134v1)

**作者**：Shivang Rawat, Mirko Morello, Flaviano Morone 等 4 位作者  
**分类**：cs.LG, cs.NE, q-bio.NC  
**发布时间**：2026-09-03

### 📄 论文摘要

Temporal integration gives continuous-time recurrent networks memory, but in deep stacks it also delays bottom-up signals and attenuates top-down errors. We develop Recursive Quadrature Filters (RQFs), biologically motivated complex-valued temporal filters that are a special case of diagonal state-space models (SSMs), and ask whether this failure mode can be addressed by making each layer's bottom-up input prospective. Starting from an energy model, we derive the RQF dynamics and show that each RQF is a band-pass filter whose learnable parameters control its tuning frequency and bandwidth. We then make each layer's bottom-up input prospective using a parameter-free two-tap update that leaves the recurrent transition and parallel scan unchanged. We extend this correction to general diagonal SSMs and show that it mitigates depth-dependent gradient attenuation when temporal gradients are truncated, i.e., spatial-only backpropagation. We evaluate the intervention in RQFs, S5, and ORGaNICs (a nonlinear gated RNN) trained using full backpropagation through time (BPTT) and spatial-only backpropagation. Under full BPTT, prospective variants match or outperform their non-prospective controls in every model and configuration. A non-residual width-32 six-layer RQF reaches 96.09% accuracy on raw-audio Speech Commands with 31.9k parameters; a width-64 six-layer RQF reaches 83.56% on the 16,384-step Path-X task. These results identify RQFs as a parameter-efficient recurrent substrate and prospective-input coding as an input-side correction for deep continuous-time recurrent networks.

### 🤖 AI 总结

**一句话总结**：Temporal integration gives continuous-time recurrent networks memory, but in deep stacks it also delays bottom-up signals and attenuates top-down errors. We develop Recursive Quadrature Filters (RQFs)...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Prospective, Coding, Improves, Learning, Deep, Continuous-Time, Recurrent, Networks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04134v1) | [下载PDF](https://arxiv.org/pdf/2609.04134v1.pdf)

---

## [29. Hardware-Aware FP4 FlashAttention-4](https://arxiv.org/abs/2609.04105v1)

**作者**：Robert Hu  
**分类**：cs.LG  
**发布时间**：2026-09-03

### 📄 论文摘要

Blackwell's 4-bit floating-point (FP4) tensor cores do not automatically make attention faster because softmax conversion and on-chip dependencies dominate once its matrix products shrink. We address this with \emph{Direct-P} for noncausal inference and a causal path that passes the forward quantization directly into backward. Direct-P maps scores directly to FP4 probabilities and reaches up to 2.13$\times$ the bfloat16 (BF16) forward throughput on an NVIDIA GB200. The causal path reconstructs probabilities from saved quantized queries and keys and uses 8-bit floating-point (FP8) gradient operands, accelerating a complete single-GPU 8-billion-parameter update by up to 1.14$\times$. Matched distributed training retains FP8 probabilities and values; every tested MXFP4 probability/value training trajectory diverges.

### 🤖 AI 总结

**一句话总结**：Blackwell's 4-bit floating-point (FP4) tensor cores do not automatically make attention faster because softmax conversion and on-chip dependencies dominate once its matrix products shrink. We address ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FP4, Hardware-Aware, FlashAttention-4, Blackwell's, 4-bit, floating-point, tensor, cores

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04105v1) | [下载PDF](https://arxiv.org/pdf/2609.04105v1.pdf)

---

## [30. Conditioning Degenerate Diffusion Models](https://arxiv.org/abs/2609.04090v1)

**作者**：Uğur Aydın, Tamer Başar  
**分类**：cs.LG  
**发布时间**：2026-09-03

### 📄 论文摘要

Current conditioned generative models heavily rely on score functions for guidance during training. When the generative model is a diffusion process with a singular diffusion coefficient and the underlying (conditional) densities either do not exist or are not smooth, we use causal optimal transport to define \emph{approximate} loss functions that identify a minimum-entropy control for guidance under minimal assumptions. Our approach relies on causal optimal transport and its characterization through the predictable representation property of (conditioned) diffusion processes whose associated martingale problem is well posed, à la Üstünel.

### 🤖 AI 总结

**一句话总结**：Current conditioned generative models heavily rely on score functions for guidance during training. When the generative model is a diffusion process with a singular diffusion coefficient and the under...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Conditioning, Degenerate, Models, Current, conditioned, generative, heavily

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.04090v1) | [下载PDF](https://arxiv.org/pdf/2609.04090v1.pdf)

---

