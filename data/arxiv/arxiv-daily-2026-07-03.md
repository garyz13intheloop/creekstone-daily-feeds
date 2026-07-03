# arXiv AI 论文日报 | 2026-07-03

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.AI](#csAI) (7 篇)
- [cs.CL](#csCL) (7 篇)
- [cs.LG](#csLG) (5 篇)

---

## cs.AI

## [1. Distributed Attacks in Persistent-State AI Control](https://arxiv.org/abs/2607.02514v1)

**作者**：Josh Hills, Ida Caspary, Asa Cooper Stickland  
**分类**：cs.AI  
**发布时间**：2026-07-02

### 📄 论文摘要

As AI coding agents become more autonomous, they increasingly ship code iteratively, with the codebase persisting across sessions. This persistence creates a new attack surface: a misaligned or prompt-injected agent can distribute attacks across pull requests (PRs) and time its payload for the PR with the best natural cover. To study the resulting dynamics, we introduce Iterative VibeCoding, a setting for AI control, the study of safely deploying capable but potentially untrusted AI. In Iterative VibeCoding, a coding agent builds software over a sequence of PRs in a persistent codebase while pursuing a covert side task. Our benchmark includes two task families: CLI tools and Flask web services, across 20 total task variations. We use Claude Sonnet 4.5 as the attack agent and GPT-4o as the monitor. We compare gradual attacks, which distribute the side task across PRs, against non-gradual attacks concentrated in a single PR. No single monitor is robust to both: which strategy evades best (success while evading the monitor) depends on the monitor type, so a defender cannot close off both gradual and non-gradual attacks with any one monitor. High evasion (>= 65%) generalizes across model attack agent backends (Sonnet 4.5, Gemini 3.1 Pro, Kimi K2.5), confirming this is a property of the persistent-state attack surface rather than a single model's capability. Evasion also remains high across state-of-the-art monitor models and the gap between gradual and non-gradual evasion widens for more capable models. We introduce a stateful link-tracker monitor that tracks suspicious buildup across PRs. On both task families, it detects gradual attacks substantially better than diff monitors that merely see more accumulated history. Combining this stronger monitor with trajectory monitors in a four-monitor ensemble reduces gradual-attack evasion from 93% under the weakest standard diff monitor to 47%.

### 🤖 AI 总结

**一句话总结**：As AI coding agents become more autonomous, they increasingly ship code iteratively, with the codebase persisting across sessions. This persistence creates a new attack surface: a misaligned or prompt...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, Agent, Distributed, Attacks, Persistent-State, Control, coding, become

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02514v1) | [下载PDF](https://arxiv.org/pdf/2607.02514v1.pdf)

---

## [2. Online Safety Monitoring for LLMs](https://arxiv.org/abs/2607.02510v1)

**作者**：Mona Schirmer, Metod Jazbec, Alexander Timans 等 6 位作者  
**分类**：cs.AI, cs.CL, cs.LG, stat.AP, stat.ML  
**发布时间**：2026-07-02

### 📄 论文摘要

Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising an alarm when safety can no longer be assumed is therefore critical. We study a simple real-time monitor that turns a verifier signal from an external model into an alarm decision by thresholding, with the threshold calibrated via risk control. In experiments on mathematical reasoning and red teaming datasets, we show that this simple design is competitive with more advanced monitors based on sequential hypothesis testing.

### 🤖 AI 总结

**一句话总结**：Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising an alarm when safety can no longer be assumed is therefore critical...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Online, Safety, Monitoring, Despite, alignment, training, remain

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02510v1) | [下载PDF](https://arxiv.org/pdf/2607.02510v1.pdf)

---

## [3. ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning](https://arxiv.org/abs/2607.02509v1)

**作者**：Yanjun Zhao, Ruizhong Qiu, Tianxin Wei 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-02

### 📄 论文摘要

Understanding and reasoning over long contexts has become a key requirement for deploying large language models (LLMs) in realistic applications. Although recent LLMs support increasingly long context windows, they often fail to use relevant evidence that is already present in the input, revealing a gap between context access and effective context utilization. In this work, we propose Recursive Evidence Replay as LLM Harness for Long-Context Reasoning (RECONTEXT), a training-free inference method for improving long-context reasoning. RECONTEXT uses model-internal relevance signals to construct a query-conditioned evidence pool and replays it before final generation while preserving the full original context. This recursive selection process separates evidence organization from answer generation without training, external memory, or context pruning. We also provide a theoretical analysis based on associative memory, which characterizes the context as a memory store, the question as a retrieval cue, attention as cue-trace association, and replay as trace reactivation. Experiments on eight long-context datasets with 128K context length show that RECONTEXT consistently improves evidence utilization across Qwen3-4B, Qwen3-8B, and Llama3-8B, achieving the best average rank on all three backbones. Code is available at https://github.com/Yanjun-Zhao/ReContext.

### 🤖 AI 总结

**一句话总结**：Understanding and reasoning over long contexts has become a key requirement for deploying large language models (LLMs) in realistic applications. Although recent LLMs support increasingly long context...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, LLM, ReContext, Recursive, Evidence, Replay, Harness, Long-Context

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02509v1) | [下载PDF](https://arxiv.org/pdf/2607.02509v1.pdf)

---

## [4. What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates](https://arxiv.org/abs/2607.02507v1)

**作者**：Arman Ghaffarizadeh, Danyal Mohaddes, Aliakbar Izadkhah 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.LG, cs.MA  
**发布时间**：2026-07-02

### 📄 论文摘要

LLM agents will increasingly act in socially structured settings where role, audience, and relational context can shape what is advantageous or costly to say. We study whether such social structure, without any explicit objective in the prompt, changes what an agent expresses publicly relative to an off-the-record (OTR) channel elicited under the same condition. We introduce a dual-channel debate framework in which agents produce public utterances that enter the shared history alongside OTR responses that are recorded but never shown to the other participant. Across 10 models, 3 scenarios, and 5 variations within each scenario, alignment-inducing settings produce systematic public-OTR divergence in the targeted agent, with its decision divergence rising from a $\sim$3% baseline to roughly 40%. The effect is consistent across four aggregate analyses: stance, semantic similarity, natural language inference, and survey responses. In some cases, the OTR response explicitly attributes public accommodation to relational pressures, such as career risk or sponsorship obligation. The findings suggest that agent evaluation should extend beyond explicit goals and detect emergent objectives. We present a dual-channel evaluation framework and complementary behavioral measures that operationalize this assessment.

### 🤖 AI 总结

**一句话总结**：LLM agents will increasingly act in socially structured settings where role, audience, and relational context can shape what is advantageous or costly to say. We study whether such social structure, w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, No, What, Say, When, One, Watching

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02507v1) | [下载PDF](https://arxiv.org/pdf/2607.02507v1.pdf)

---

## [5. G-RRM: Guiding Symbolic Solvers with Recurrent Reasoning Models](https://arxiv.org/abs/2607.02491v1)

**作者**：Timo Bertram, Sidhant Bhavnani, Richard Freinschlag 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-02

### 📄 论文摘要

In this work, we focus on SE-RRMs, a symbol-equivariant instantiation of RRMs that exhibits improved extrapolation to larger problem sizes. We propose a neuro-symbolic approach, ``Guiding with Recurrent Reasoning Models'' (G-RRM), which integrates SE-RRMs with symbolic solvers for constraint satisfaction problems. SE-RRMs act as neural solvers that generate full solution proposals and guide classical symbolic solvers, such as backtracking or SAT-based methods like Glucose 4.1 and CaDiCaL 3.0.0, that produce globally correct solutions. Centrally, we investigate when neural guidance with G-RRM improves the search efficiency of symbolic solvers. % Our experiments show that the efficacy of G-RRM depends on two conditions: first, the problem instances must have an expansive combinatorial search space to expose potential gains, and second, the solver architecture must be capable of dynamically overwriting its branching choices to recover when neural hints are imperfect. When these conditions hold, guidance drives median conflict counts to zero and yields significant wall-clock speedups: on $9\times9$ Sudoku, where the SE-RRM correctly solves $91.1\%$ of instances, backtracking accelerates by $33.3\times$ and Glucose 4.1 by $1.70\times$ (median, $p<0.001$), with Glucose 4.1 retaining a $1.17\times$ speedup on perfect-hint $25\times25$ grids. In contrast, CaDiCaL 3.0.0, whose runtime is overhead-dominated and which always respects the injected branching hints rather than overwriting them, shows no significant speedup (median $1.02\times$, n.s.) and even a small significant mean slowdown ($0.90\times$) on $9\times9$. These results delineate the regimes in which neural guidance translates into practical speedups.

### 🤖 AI 总结

**一句话总结**：In this work, we focus on SE-RRMs, a symbol-equivariant instantiation of RRMs that exhibits improved extrapolation to larger problem sizes. We propose a neuro-symbolic approach, ``Guiding with Recurre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：G-RRM, Guiding, Symbolic, Solvers, Recurrent, Reasoning, Models, work

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02491v1) | [下载PDF](https://arxiv.org/pdf/2607.02491v1.pdf)

---

## [6. EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments](https://arxiv.org/abs/2607.02440v1)

**作者**：Zhilin Wang, Han Song, Runzhe Zhan 等 16 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-07-02

### 📄 论文摘要

Autonomous agents are increasingly expected to improve executable policies through feedback, yet existing evaluations often collapse this process into a final score or confound it with open-ended software-engineering progress. We introduce Autonomous Policy Evolution, a controlled evaluation setting in which a harness-model agent repeatedly edits an executable policy system under a fixed interaction budget. We instantiate this setting in EvoPolicyGym, a benchmark built from compact interactive RL environments that evaluates how agents iteratively improve explored policies. On the EvoPolicyGym suite, GPT-5.5 achieves the strongest aggregate rank score and top-two performance on all 16 environments. Beyond leaderboard results, EvoPolicyGym also provides trajectory-level diagnostics that distinguish how agents allocate budget, convert feedback into parametric tuning. These analyses show that strong autonomous policy evolution depends not only on isolated task wins, but on discovering task-appropriate mechanisms and refining policies under bounded feedback.

### 🤖 AI 总结

**一句话总结**：Autonomous agents are increasingly expected to improve executable policies through feedback, yet existing evaluations often collapse this process into a final score or confound it with open-ended soft...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, EvoPolicyGym, Evaluating, Autonomous, Policy, Evolution, Interactive, Environments

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02440v1) | [下载PDF](https://arxiv.org/pdf/2607.02440v1.pdf)

---

## [7. Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach](https://arxiv.org/abs/2607.02432v1)

**作者**：Manuel Alonso-Carracedo, Ruben Fernandez-Boullon, Pedro Celard 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.CY  
**发布时间**：2026-07-02

### 📄 论文摘要

Scalable and reliable grading of command-line examinations remains a challenge in computing education, where rising enrolments make manual marking difficult and rule-based autograders cannot handle partial credit, equivalent solutions, or syntactic variation. This paper evaluates whether four frontier Large Language Models (GPT, Claude Opus, Gemini, and GLM) can approximate expert judgment when grading short Linux/bash command responses. The study adopts a four-level cognitive taxonomy that combines cognitive complexity and operational impact, ranging from information retrieval (L1) and basic file manipulation (L2) to structural operations (L3) and advanced system management (L4). The models were tested with two prompt variants, a minimal baseline and a rubric-enhanced version, on 1200 real responses from second-year Computer Engineering students independently graded by three expert instructors. Gemini~3.0 Pro with rubric-guided prompting achieved the highest human-AI agreement (ICC(3,1) = 0.888, MAE = 0.10, Bland-Altman bias = -0.014). Agreement declined consistently as taxonomy level increased, with the largest discrepancies at higher levels. Across all models, rubric quality had a larger effect than provider choice, with structured prompts consistently improving agreement. These results show that question complexity is a reliable predictor of the difficulty LLMs face in grading accurately, and they establish a principled, taxonomy-based framework for determining which questions are suitable for AI-assisted grading and which require human review, while also providing a transferable evaluation protocol and prompt templates.

### 🤖 AI 总结

**一句话总结**：Scalable and reliable grading of command-line examinations remains a challenge in computing education, where rising enrolments make manual marking difficult and rule-based autograders cannot handle pa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Automated, grading, Linux, bash, examinations, large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02432v1) | [下载PDF](https://arxiv.org/pdf/2607.02432v1.pdf)

---

## cs.CL

## [8. LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning](https://arxiv.org/abs/2607.02513v1)

**作者**：Matteo Boglioni, Thibault Rousset, Siva Reddy 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-07-02

### 📄 论文摘要

LLMs memorize sensitive training data, including personally identifiable information (PII), creating a pressing need for reliable post hoc removal methods. Unlearning has emerged as a promising solution, with state-of-the-art(SOTA) methods often following a localize-first, unlearn-second paradigm that targets specific model parameters. However, existing benchmarks evaluate unlearning solely at the output level, leaving open the question of whether unlearning truly erases knowledge from a model's parameters or merely obfuscates it, a concern reinforced by the success of resurfacing attacks. To bridge this gap, we introduce LACUNA: the first unlearning testbed with ground-truth parameter-level localization. LACUNA injects PII of synthetic individuals into predefined parameters of 1B and 7B OLMo-based models via masked continual pretraining, enabling direct evaluation of whether unlearning targets the weights responsible for knowledge storage. We use LACUNA to benchmark current SOTA unlearning methods and find that, despite strong output-level performance, existing methods are highly imprecise and susceptible to resurfacing attacks. We further show that when localization is successful, even a simple gradient-based unlearning method achieves strong erasure and robustness to resurfacing attacks, highlighting the importance of precise unlearning. We release LACUNA to complement behavioral evaluations and drive further advances in robust, localization-based unlearning.

### 🤖 AI 总结

**一句话总结**：LLMs memorize sensitive training data, including personally identifiable information (PII), creating a pressing need for reliable post hoc removal methods. Unlearning has emerged as a promising soluti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, LACUNA, Testbed, Evaluating, Localization, Precision, Unlearning, memorize

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02513v1) | [下载PDF](https://arxiv.org/pdf/2607.02513v1.pdf)

---

## [9. Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas](https://arxiv.org/abs/2607.02504v1)

**作者**：Yuxuan Li, Lingxi Xie, Xinyue Huo 等 9 位作者  
**分类**：cs.CL, cs.AI, cs.CV  
**发布时间**：2026-07-02

### 📄 论文摘要

Long-form TV dramas present a formidable challenge for comprehensive video understanding, where deciphering complex storyline often relies on \textbf{speaker recognition}, the task of accurately attributing each spoken utterance to its respective character. In this paper, we advance this field through two primary contributions. (1) We introduce \textbf{DramaSR-532K}, a large-scale benchmark comprising 532K annotated dialogue lines across more than 900 unique characters, necessitating the integration of auditory, linguistic, and visual cues for speaker recognition. (2) We propose \textbf{DramaSR-LRM}, a robust approach built upon a large reasoning model (LRM). DramaSR-LRM is designed to autonomously aggregate contextual evidence via multimodal tool-use, synthesizing diverse inputs to achieve high-fidelity attribution. Experimental results demonstrate that DramaSR-LRM significantly outperforms existing baselines, particularly on short utterances where acoustic biometrics are inherently unreliable. \textit{All the data and code will be made publicly available at the project page: https://www.github.com/198808xc/DramaSR-LRM.}

### 🤖 AI 总结

**一句话总结**：Long-form TV dramas present a formidable challenge for comprehensive video understanding, where deciphering complex storyline often relies on \textbf{speaker recognition}, the task of accurately attri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, TV, Reasoning, Improves, Speaker, Recognition, Long-form, Dramas

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02504v1) | [下载PDF](https://arxiv.org/pdf/2607.02504v1.pdf)

---

## [10. Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning](https://arxiv.org/abs/2607.02490v1)

**作者**：Liyan Tang, Fangcong Yin, Greg Durrett  
**分类**：cs.CL, cs.CV  
**发布时间**：2026-07-02

### 📄 论文摘要

Large vision-language models can reason over multimodal inputs by generating textual chains of thought (CoT). A key capability exhibited in CoT reasoning is self-reflection: revisiting earlier decisions and correcting previous errors. However, existing LVLMs often fail to properly attend to visual inputs during reflection, limiting their ability to translate feedback into grounded corrections, especially for out-of-distribution images. To address this issue, we propose a novel reinforcement learning training framework VRRL, with two components explicitly designed to elicit visually grounded self-reflection. First, we randomly mask trajectory prefixes during training to emphasize recovery from incorrect intermediate predictions rather than making early mistakes. Second, we introduce buffered roll-ins from an experience replay buffer to expose the model to diverse failure states that it must learn to correct. We evaluate our approach on visual grounding tasks involving tables and charts, as well as spatial navigation benchmarks. While off-the-shelf and conventionally fine-tuned models degrade substantially under distribution shift, our method substantially improves average out-of-distribution accuracy over standard RL and reflection-oriented fine-tuning baselines by using self-reflection effectively.

### 🤖 AI 总结

**一句话总结**：Large vision-language models can reason over multimodal inputs by generating textual chains of thought (CoT). A key capability exhibited in CoT reasoning is self-reflection: revisiting earlier decisio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Visually, Grounded, Self-Reflection, Vision-Language, Models, via, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02490v1) | [下载PDF](https://arxiv.org/pdf/2607.02490v1.pdf)

---

## [11. Audio-Based Understanding of Audiobook Narration Appeal](https://arxiv.org/abs/2607.02473v1)

**作者**：Shahar Elisha, Mariano Beguerisse-Díaz, Emmanouil Benetos  
**分类**：cs.CL, cs.SD, eess.AS  
**发布时间**：2026-07-02

### 📄 论文摘要

Narration is central to the audiobook listening experience, shaping how listeners engage with and understand the content. This work explores how narration qualities shape an audiobook's appeal, noting that their effects can vary by genre, title, and audience. We extract vocal and acoustic features (e.g., tone, pace, loudness) from LibriVox using pre-trained audio models and analyse their relationship with consumption data (specifically, view-rate) and their interplay with genre and title. Despite limited consumption data, we find that acoustic information alone has a robust association with appeal, even after accounting for title effects. We further validate these findings using more nuanced proprietary engagement metrics. To our knowledge, this is the first systematic computational study linking narration qualities, genre, title, and audiobook consumption, highlighting the potential of data-driven insights to improve audiobook personalisation and narrator casting.

### 🤖 AI 总结

**一句话总结**：Narration is central to the audiobook listening experience, shaping how listeners engage with and understand the content. This work explores how narration qualities shape an audiobook's appeal, noting...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Audio-Based, Understanding, Audiobook, Narration, Appeal, central, listening

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02473v1) | [下载PDF](https://arxiv.org/pdf/2607.02473v1.pdf)

---

## [12. Will Scaling Improve Social Simulation with LLMs?](https://arxiv.org/abs/2607.02464v1)

**作者**：Caleb Ziems, William Held, Su Doga Karaca 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-02

### 📄 论文摘要

Large Language Model (LLM) social simulations are a promising research method, but they are not yet faithful enough to be adopted widely. In this work, we investigate whether the current scaling paradigm in language modeling is likely to close these gaps, or whether simulation fidelity is orthogonal to general capabilities and therefore deserving of more research attention. We use scaling laws to study the relationship between LLMs' compute scale, general capability benchmarks, and the fidelity of social simulation in three representative sub-domains: opinion modeling, behavioral simulation, and longitudinal forecasting. Surprisingly, we discover strong compute scaling in all three settings, using a suite of 85 transformer LLMs with the Qwen3 architecture pre-trained on the DCLM web text corpus under fixed-compute budgets from $10^{18}$ to $10^{20}$ FLOPs. Then we evaluate 35 larger and more capable open-weight models up to 70B parameters, allowing us to predict downstream accuracy from loss. This reveals that the majority of behavioral and opinion simulation tasks will rapidly improve with scale, particularly when they involve populations that are well-represented in English web corpora. Longitudinal forecasting and underrepresented opinions scale more slowly, especially when they are less correlated with general knowledge and reasoning benchmarks like MMLU. In behavior simulation, scaling fails to improve model calibration with human cognitive biases like risk aversion, as well as human heuristics like learning correlated rewards from related tasks. On these tasks, even fine-tuned models fail to noticeably scale up performance from 0.5B to 8B parameters. Taken together, we conclude that scale will improve social simulations in most settings, but outliers exist, and improvements will be less reliable in low-resource domains.

### 🤖 AI 总结

**一句话总结**：Large Language Model (LLM) social simulations are a promising research method, but they are not yet faithful enough to be adopted widely. In this work, we investigate whether the current scaling parad...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Will, Scaling, Improve, Social, Simulation, LLMs?, Large, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02464v1) | [下载PDF](https://arxiv.org/pdf/2607.02464v1.pdf)

---

## [13. Language Models as Measurement Apparatus for Culture](https://arxiv.org/abs/2607.02459v1)

**作者**：Kent K. Chang  
**分类**：cs.CL  
**发布时间**：2026-07-02

### 📄 论文摘要

Language models are increasingly used to quantify cultural phenomena, but what makes such measurement distinctively cultural? This paper argues that NLP work on culture is a material-discursive practice: the apparatus -- model, data, annotation, evaluation -- participates in constituting the cultural reality it measures, rather than passively recording it. Drawing on Karen Barad's concept of the agential cut -- the contingent boundary between phenomenon and instrument -- I show that the apparatus's substantive design choices draw such boundaries, and that the boundary is entangled from the start because language models have already internalized much of the cultural material they measure. I illustrate this through three case studies on television and film dialogue (measuring structure, interaction, and deviation) and three examinations of the apparatus itself (erasure of cultural markers, attunement to historical material, and agency in an agentic workflow). This big picture analysis proposes a research program that is theory-driven, empirically rigorous, and culturally contingent, treating each agential cut as a conscious commitment, at once methodological and ethical.

### 🤖 AI 总结

**一句话总结**：Language models are increasingly used to quantify cultural phenomena, but what makes such measurement distinctively cultural? This paper argues that NLP work on culture is a material-discursive practi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Language, Models, Measurement, Apparatus, Culture, increasingly, used

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02459v1) | [下载PDF](https://arxiv.org/pdf/2607.02459v1.pdf)

---

## [14. The Future of NLP may not be at NLP Conferences: Scholarly Migration Patterns in Natural Language Processing](https://arxiv.org/abs/2607.02416v1)

**作者**：David Jurgens  
**分类**：cs.CL  
**发布时间**：2026-07-02

### 📄 论文摘要

Natural Language Processing (NLP) has traditionally been published in its core disciplinary venues like ACL. However, advances in Large Language Models (LLMs) has led to a blurring of the disciplinary lines between NLP and general Machine Learning (ML), with authors regularly publishing in venues from both fields. Here, we ask whether the disciplinary center of gravity is shifting. Using NLP research published from 2010 to 2026 and studies of both established and new authors, we find that a migration is taking place. First, comparing the pre- and post-LLM eras, established authors lost 19.2pp of share at flagship *ACL main-conference tracks while gaining 14.8pp in the newer Findings tracks, and general ML venues rose 8.6pp, even when adjusting for parallel growth in the fields. Second, among newer authors who debut with at least three first-author NLP-topic papers, the share whose work appears mostly at *ACL venues fell from 84% (2019) to 74% (2024), while the share appearing mostly at general ML venues rose from 5% to 21%. Using causal inference techniques, we estimate that these general ML venues confer a significant citation premium, which influences venue selection. Together, these results point to a significant shift in where NLP research is published.

### 🤖 AI 总结

**一句话总结**：Natural Language Processing (NLP) has traditionally been published in its core disciplinary venues like ACL. However, advances in Large Language Models (LLMs) has led to a blurring of the disciplinary...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, be, at, Future, NLP, may, not, Conferences

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02416v1) | [下载PDF](https://arxiv.org/pdf/2607.02416v1.pdf)

---

## cs.CV

## [15. WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory](https://arxiv.org/abs/2607.02517v1)

**作者**：Hanlin Wang, Hao Ouyang, Qiuyu Wang 等 13 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-02

### 📄 论文摘要

We present WorldDirector, a highly controllable video world model framework designed for persistent dynamic object memory and unrestricted viewpoint exploration. Unlike existing world models that entangle physical dynamics with pixel rendering and rely on continuous visual observation to sustain motion, our framework explicitly decouples semantic motion orchestration from visual generation. By leveraging an LLM to coordinate 3D trajectories with camera movements and subsequently employing these orchestrated trajectories as control signals for video generation, our approach ensures strict physical logic and appearance stability, successfully preserving the exact visual identities of dynamic entities even when they re-enter the scene after prolonged periods out of view. Experimental results demonstrate that our method supports the synthesis of complex and extended events with unprecedented controllability and persistent dynamic object memory. Project Page: https://worlddirector.github.io/

### 🤖 AI 总结

**一句话总结**：We present WorldDirector, a highly controllable video world model framework designed for persistent dynamic object memory and unrestricted viewpoint exploration. Unlike existing world models that enta...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：WorldDirector, Building, Controllable, World, Simulators, Persistent, Dynamic, Memory

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02517v1) | [下载PDF](https://arxiv.org/pdf/2607.02517v1.pdf)

---

## [16. Alignment Is All You Need For X-to-4D Generation](https://arxiv.org/abs/2607.02516v1)

**作者**：Qiaowei Miao, Kehan Li, Yawei Luo 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-02

### 📄 论文摘要

Generative diffusion models excel at synthesizing high-quality images, videos, and 3D content under multimodal control. However, arbitrary user-defined modality-to-4D (X-to-4D) generation remains challenging due to the high cost of constructing diverse datasets and the limited scalability of existing methods. This paper presents Align4D, a flexible framework that translates any-modal input into coherent video-3D pairs, using video to guide 4D motion and 3D data to shape 4D geometry. Align4D introduces three key techniques: (1) Object Distance Alignment, which searches Video-Aligned and Multiview-Aligned Object Distances (VAOD/MAOD), respectively, to reconcile 4D renderings with video and the priors of multiview diffusion models; (2) Motion-Geometry Joint Alignment, which constrains known and unknown views through synchronized video and 3D inputs, ensuring consistent 4D generation; and (3) Asynchronous Optimization, which decouples Gaussian attribute and deformation network training to enhance motion and geometry fidelity. We further propose the X4D dataset, which integrates prompt, image, video, and 3D data for benchmarking. Experiments on X4D and Consistent4D demonstrate that Align4D achieves state-of-the-art quality and consistency in X-to-4D generation. Project page: https://miaoqiaowei.github.io/Align4D/.

### 🤖 AI 总结

**一句话总结**：Generative diffusion models excel at synthesizing high-quality images, videos, and 3D content under multimodal control. However, arbitrary user-defined modality-to-4D (X-to-4D) generation remains chal...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Alignment, All, Need, X-to-4D, Generation, Generative, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02516v1) | [下载PDF](https://arxiv.org/pdf/2607.02516v1.pdf)

---

## [17. Seek to Segment: Active Perception for Panoramic Referring Segmentation](https://arxiv.org/abs/2607.02497v1)

**作者**：Song Tang, Shuming Hu, Xincheng Shuai 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-02

### 📄 论文摘要

Existing referring segmentation models passively process static images captured from fixed perspectives, limiting their applicability in Embodied AI, where agents must perform active perception in the continuous 360$^\circ$ environments. To bridge this gap, we introduce a novel task: Active Panoramic Referring Segmentation (APRS). In this setting, an agent is required to adjust its viewing direction ($Δθ, Δφ$) to explore the 360$^\circ$ environment, seeking the object specified by a user instruction for segmentation. To tackle this challenging task, we propose PanoSeeker, a memory-augmented agent for efficient APRS. Rather than relying on heuristic scanning, PanoSeeker integrates a Vision-Language Model (VLM) with EgoSphere, an explicit spatial visual memory. By progressively integrating sequential local observations into a unified 360$^\circ$ representation, EgoSphere enables the agent to plan efficient and non-redundant search trajectories. Once the target is found, the agent performs active viewpoint alignment and outputs the segmentation mask. Furthermore, we curate an expert-annotated search trajectory dataset with memory timelines for Supervised Fine-Tuning, followed by Reinforcement Learning post-training to explicitly optimize PanoSeeker's exploration efficiency. Extensive experiments on our newly established APRS benchmark demonstrate that PanoSeeker achieves superior search efficiency and segmentation accuracy, significantly outperforming adapted state-of-the-art baselines.

### 🤖 AI 总结

**一句话总结**：Existing referring segmentation models passively process static images captured from fixed perspectives, limiting their applicability in Embodied AI, where agents must perform active perception in the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Seek, Segment, Active, Perception, Panoramic, Referring, Segmentation, Existing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02497v1) | [下载PDF](https://arxiv.org/pdf/2607.02497v1.pdf)

---

## [18. Towards Robustness against Typographic Attack with Training-free Concept Localization](https://arxiv.org/abs/2607.02494v1)

**作者**：Bohan Liu, Wenqian Ye, Guangzhi Xiong 等 6 位作者  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-07-02

### 📄 论文摘要

Models trained via Contrastive Language-Image Pretraining (CLIP) serve as the foundational vision encoders for most modern Large Vision Language Models (LVLMs). Despite their widespread adoption, CLIP models exhibit a critical yet underexplored failure mode: irrelevant text appearing within images confounds visual representations, biasing them toward lexical meaning rather than true visual semantics. This robustness issue, commonly described as a Typographic Attack (TA), exposes a vulnerability that poses a significant risk to safety-critical applications such as autonomous driving. To achieve interpretable and effective robustness against TA, we propose a novel, training-free mechanistic interpretability method. Our method provides sampling-based interpretations of hidden state representations and quantitatively attributes semantic versus lexical focus to individual attention heads. Through probabilistic analysis and circuit mining, we isolate specific Vision Transformer (ViT) components that disproportionately encode lexical information, thereby identifying the mechanistic source of TA. We further show that simple interventions applied directly to the identified circuits, without any additional training, can substantially improve robustness against Typographic Attacks in object classification. These interventions, such as selective adjustment of attention weights, also outperform both supervised and training-free defense methods. Our experiments demonstrate that applying the proposed intervention to the vision encoders of several state-of-the-art LVLMs yields substantial gains in Visual Question Answering accuracy under Typographic Attack interference on RIO-Bench. These results confirm both the efficacy and the generalizability of our mechanistic approach. Code is released at https://github.com/Liu-524/SamplingTAR.

### 🤖 AI 总结

**一句话总结**：Models trained via Contrastive Language-Image Pretraining (CLIP) serve as the foundational vision encoders for most modern Large Vision Language Models (LVLMs). Despite their widespread adoption, CLIP...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Towards, Robustness, against, Typographic, Attack, Training-free, Concept, Localization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02494v1) | [下载PDF](https://arxiv.org/pdf/2607.02494v1.pdf)

---

## [19. GeoMix: Descriptor-Free Visual Localization via Global Context and Multi-Detector Training](https://arxiv.org/abs/2607.02486v1)

**作者**：Yejun Zhang, Xinjue Wang, Zihan Wang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-02

### 📄 论文摘要

Descriptor-free visual localization eliminates high-dimensional descriptor storage, preserves scene privacy, and simplifies map maintenance, yet its accuracy still lags far behind descriptor-based pipelines. We identify this gap to insufficient geometric discriminability in geometry-only matching. Without visual appearance, current methods underutilize local geometry cues, lack the global context among keypoints, and overfit to a single keypoint detector. We further observe that descriptor-free matching naturally enables multi-detector training, as heterogeneous keypoints can be optimized in a shared geometry-only space without aligning descriptor spaces. Building on these insights, we propose GeoMix, a descriptor-free 2D-3D matching framework that strengthens geometric discriminability at three levels. Locally, directional and distance-aware embeddings enrich neighborhood aggregation with fine-grained spatial structure. Globally, learnable context nodes aggregate and redistribute scene-wide information via cross-attention to resolve ambiguities beyond local receptive fields. At the training level, Mix-Training exploits this detector-agnostic geometry space to learn representations across multiple keypoint detectors. Extensive experiments on MegaDepth, Cambridge Landmarks, 7Scenes, and Aachen Day-Night show that GeoMix sets a new state of the art among descriptor-free methods, reducing 75th-percentile rotation error by 89\% and translation error by up to 90\% over the previous best, while generalizing zero-shot to unseen detectors and narrowing the gap to descriptor-based pipelines. Code is available at $\href{https://github.com/YejunZhang/Geomix}{\text{this links}}$.

### 🤖 AI 总结

**一句话总结**：Descriptor-free visual localization eliminates high-dimensional descriptor storage, preserves scene privacy, and simplifies map maintenance, yet its accuracy still lags far behind descriptor-based pip...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GeoMix, Descriptor-Free, Visual, Localization, via, Global, Context, Multi-Detector

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02486v1) | [下载PDF](https://arxiv.org/pdf/2607.02486v1.pdf)

---

## [20. EAGLE-360: Embodied Active Global-to-Local Exploration in 360$^\circ$](https://arxiv.org/abs/2607.02479v1)

**作者**：Jingtao Xu, Zizhuo Lin, Jianwen Sun 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-02

### 📄 论文摘要

While Multimodal Large Language Models (MLLMs) have demonstrated exceptional capabilities in standard visual understanding, adapting them for active visual search in 360$^\circ$ panoramic environments exposes fundamental limitations. Specifically, standard MLLMs struggle to effectively model inherent panoramic properties, such as severe polar distortion and continuous cylindrical topologies, which significantly degrades target detection accuracy. Consequently, existing panoramic search methods attempt to compensate by relying heavily on fragmented local viewpoints. Burdened by rigid initialization and a lack of global panoramic priors, these approaches suffer from myopic, inefficient exploration and struggle with robust error recovery when targets are out of view. To overcome these challenges, we propose EAGLE-360, a novel Embodied Active Global-to-Local Exploration framework. Rather than performing exhaustive local searches, EAGLE-360 leverages global priors to establish an initial holistic perspective, iteratively reasoning and progressively narrowing the search space. Architecturally, we adapt RoPE Rolling, a coordinate-shifting positional encoding mechanism, to seamlessly model the continuous topologies of panoramas. To facilitate this paradigm, we construct the large-scale EAGLE-360 dataset, comprising 14,000+ 4K panoramas and 70,000+ rounds of high-quality VQA dialogues. By employing a training pipeline that integrates Supervised Fine-Tuning (SFT) with Group Relative Policy Optimization (GRPO), we effectively elicit complex spatial reasoning and tool-calling capabilities. Extensive experiments demonstrate that EAGLE-360 establishes a new state-of-the-art for 360$^\circ$ visual search, achieving nearly an 8-fold increase in accuracy over the base model while significantly enhancing exploration efficiency.

### 🤖 AI 总结

**一句话总结**：While Multimodal Large Language Models (MLLMs) have demonstrated exceptional capabilities in standard visual understanding, adapting them for active visual search in 360$^\circ$ panoramic environments...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：360$^, EAGLE-360, Embodied, Active, Global-to-Local, Exploration, circ$, While

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02479v1) | [下载PDF](https://arxiv.org/pdf/2607.02479v1.pdf)

---

## [21. Interpretation-Oriented Cloud Removal via Observation-Anchored Residual Flow with Geo-Contextual Alignment](https://arxiv.org/abs/2607.02471v1)

**作者**：Ziyao Wang, Maonan Wang, Yucheng He 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-02

### 📄 论文摘要

Cloud removal (CR) is essential for optical remote sensing, serving as a prerequisite for reliable downstream interpretation, such as semantic segmentation and change detection. However, existing CR approaches often prioritize visual realism while overlooking their impact on subsequent analytical tasks, leading to semantic drift and degraded downstream performance. To address this issue, we propose Geo-Anchored Cloud Removal (GACR), a unified framework that jointly ensures faithful reconstruction and robust interpretability. At its core, GACR incorporates Observation-Anchored Residual Flow (OAR-Flow), which reformulates CR as a physically grounded residual inversion process. By anchoring the generative trajectory to the cloudy observation rather than pure noise, OAR-Flow enables fast, stable, and faithful reconstruction. To further preserve semantic structures critical for downstream interpretation, GACR integrates Geo-Contextual Prior Alignment (GCPA) to constrain the reconstruction within a semantic manifold induced by a Vision Foundation Model (VFM). Consequently, GACR strictly maintains the spatial-semantic integrity of complex landscapes. Extensive experiments across six CR datasets and twelve downstream tasks demonstrate that GACR produces superior reconstruction quality while consistently improving downstream task accuracy. The code is available at https://github.com/wzy6055/GACR.

### 🤖 AI 总结

**一句话总结**：Cloud removal (CR) is essential for optical remote sensing, serving as a prerequisite for reliable downstream interpretation, such as semantic segmentation and change detection. However, existing CR a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Interpretation-Oriented, Cloud, Removal, via, Observation-Anchored, Residual, Flow, Geo-Contextual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02471v1) | [下载PDF](https://arxiv.org/pdf/2607.02471v1.pdf)

---

## [22. OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers](https://arxiv.org/abs/2607.02461v1)

**作者**：Donghyun Lee, Jitesh Chavan, Duy Nguyen 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-07-02

### 📄 论文摘要

Diffusion transformers (DiTs) achieve state-of-the-art image and video generation, but their multi-step sampling and growing parameter count make inference expensive. Post-training quantization (PTQ) is the natural remedy, yet DiT activations shift across timesteps, prompts, and guidance branches, forcing prior methods to re-fit calibration data for every new checkpoint or modality. We present OrbitQuant, a data-agnostic weight-activation quantizer that bypasses range estimation by quantizing in a normalized, rotated basis. In this basis, a randomized permuted block-Hadamard (RPBH) rotation concentrates each coordinate around one fixed, known marginal regardless of the input, so a single Lloyd-Max codebook serves all timesteps, prompts, and layers of a given input dimension. We extend the same quantizer to weight rows offline, absorbing the rotation into the weights so that it cancels inside each linear layer and only a forward rotation on the activations remains at runtime. The same recipe transfers from image to video with no per-modality tuning. Across FLUX.1, Z-Image-Turbo, Wan 2.1, and CogVideoX, it sets the state of the art for PTQ at several low-bit settings. It also pushes PTQ of image diffusion transformers to W2A4 with usable generation quality.

### 🤖 AI 总结

**一句话总结**：Diffusion transformers (DiTs) achieve state-of-the-art image and video generation, but their multi-step sampling and growing parameter count make inference expensive. Post-training quantization (PTQ) ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, OrbitQuant, Data-Agnostic, Quantization, Image, Video, Transformers, DiTs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02461v1) | [下载PDF](https://arxiv.org/pdf/2607.02461v1.pdf)

---

## [23. MARVEL: Margin-Aware Robust von Mises-Fischer Expert Learning for Long-Tailed Out-of-Distribution Detection](https://arxiv.org/abs/2607.02435v1)

**作者**：A. S. Anudeep, Vaanathi Sundaresan  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-07-02

### 📄 论文摘要

For clinical deployment, it is essential that automated diagnostic systems remain reliable when confronted with previously unseen cases, yet deep models routinely misclassify out-of-distribution (OOD) inputs with high confidence, underscoring the need for more robust OOD detection methods. Although substantial effort has been devoted to improving model robustness, most of the existing literature assumes balanced datasets, evaluates OOD detection on coarse or non-clinical OOD sources, or lacks comprehensive assessment across diverse OOD scenarios. To address the gaps, we propose a novel methodology trained on diverse and imbalanced medical datasets and evaluated across a clinically reflective OOD spectrum. Our framework comprises three key components: (1) a Nonlinear von Mises-Fisher (NvMF) classifier capable of learning non-linear decision boundaries, with theoretical proof of its asymptotic connection to cosine classifiers; (2) a multi-expert framework in which margin-aware NvMF classifiers specialise in different regions of label distribution to better handle imbalance; and (3) an outlier expert trained explicitly to distinguish inlier from outlier data, thereby strengthening OOD detection. Evaluation on RFMiD, ISIC2019, and NCTCRC datasets demonstrates consistent improvements over state-of-the-art methods, achieving mean FPR95 reductions of 8.45%, 13.02%, and 36.90% respectively. These gains are further supported by comprehensive ablations that validated the contributions of each component. This enables reliable identification of unfamiliar cases for deferral to clinicians, supporting safer AI-assisted diagnosis in real-world workflows. Our code is available at https://github.com/redboxup/MARVEL.

### 🤖 AI 总结

**一句话总结**：For clinical deployment, it is essential that automated diagnostic systems remain reliable when confronted with previously unseen cases, yet deep models routinely misclassify out-of-distribution (OOD)...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MARVEL, Margin-Aware, Robust, von, Mises-Fischer, Expert, Learning, Long-Tailed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02435v1) | [下载PDF](https://arxiv.org/pdf/2607.02435v1.pdf)

---

## [24. Learning to Evolve Scenes: Reasoning about Human Activities with Scene Graphs](https://arxiv.org/abs/2607.02425v1)

**作者**：Francesca Pistilli, Simone Alberto Peirone, Giuseppe Averta  
**分类**：cs.CV  
**发布时间**：2026-07-02

### 📄 论文摘要

Understanding human behavior while interacting with the surrounding world is crucial for many applications of embodied AI. First-person videos are particularly informative for this problem, as they well capture how activities reshape the scene over time. However, existing approaches often rely on implicit visual or language-aligned representations, disregarding structured reasoning over the scene dynamic. We argue that explicit, compositional and editable representations of human-environment interactions can play a crucial role for rich grounded activity understanding. To this end, we introduce SG-Ego, a large scale annotation set extending Ego4D with spatio-temporal scene graphs, where relations triplets are consolidated over time into explicit time-evolving descriptions of the scene state. To reason over this representation, we propose GLEN, a graph-based model that operates over scene graph sequences to both align them with textual actions and model their temporal evolution. In addition, we formulate the activity-driven graph-edit forecasting (A-GEF) problem, a novel task that casts scene dynamics as a sequence of structured transformations conditioned on ongoing actions, enabling explicit reasoning about how scenes change over time. We validate our approach across multiple downstream tasks, spanning retrieval benchmarks as EgoMCQ and EgoCVR, as well as long-horizon reasoning benchmarks as EXPLORE-Bench and the newly introduced A-GEF. GLEN achieves strong results compared to raw video baselines and it excels in reasoning settings, typically addressed only with MLLMs, while enabling controllable and structured predictions of scene dynamics driven by human activities. We believe our results establish spatio-temporal scene graphs, together with models that reason over them, as strong compositional and interpretable representations for video understanding and potentially beyond.

### 🤖 AI 总结

**一句话总结**：Understanding human behavior while interacting with the surrounding world is crucial for many applications of embodied AI. First-person videos are particularly informative for this problem, as they we...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Evolve, Scenes, Reasoning, about, Human, Activities, Scene

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02425v1) | [下载PDF](https://arxiv.org/pdf/2607.02425v1.pdf)

---

## [25. Wavelet-Guided Semantic Signal Compensation for Inversion-Free Image Editing](https://arxiv.org/abs/2607.02421v1)

**作者**：Anqi Tang, Wenhao Sun, Zhaoqiang Liu  
**分类**：cs.CV  
**发布时间**：2026-07-02

### 📄 论文摘要

Text-guided image editing aims to modify visual content according to a target prompt while preserving the background. Recent inversion-free image editing frameworks such as FlowEdit have demonstrated strong editing capability without requiring inversion. Empirically, FlowEdit can achieve substantial semantic changes under appropriate hyperparameter settings. However, we observe that under certain global attribute shifts, the editing trajectory may not effectively move away from the source distribution in the early timesteps. Our analysis suggests that in the high-noise regime, the dominant manifold-seeking flow toward the data manifold can reduce the influence of the text-conditioned direction, leading to limited global modification while background structures remain only moderately preserved. Inspired by this observation, we propose an inversion-free, frequency-aware semantic compensation strategy that strengthens the effective signal in the early stage of generation, while maintaining structural consistency in the background. The proposed method improves global editing capacity without sacrificing background fidelity.

### 🤖 AI 总结

**一句话总结**：Text-guided image editing aims to modify visual content according to a target prompt while preserving the background. Recent inversion-free image editing frameworks such as FlowEdit have demonstrated ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Wavelet-Guided, Semantic, Signal, Compensation, Inversion-Free, Image, Editing, Text-guided

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02421v1) | [下载PDF](https://arxiv.org/pdf/2607.02421v1.pdf)

---

## cs.LG

## [26. Beyond Adam: SOAP and Muon for Faster, Label-Efficient Training of Machine Learning Interatomic Potentials](https://arxiv.org/abs/2607.02499v1)

**作者**：Gil Harari, Yoel Zimmermann, Ola Tangen Kulseng 等 7 位作者  
**分类**：cs.LG, cs.AI, physics.chem-ph, physics.comp-ph  
**发布时间**：2026-07-02

### 📄 论文摘要

Machine learning interatomic potentials (MLIPs) have become a hallmark of AI for scientific simulation. While efforts on new architectures and datasets have led to increasingly accurate and general models, the choice of optimizer for training has largely remained unexplored, defaulting to Adam and its variants in the community. Here, we implement and systematically compare a class of recently proposed matrix-structured optimizers, including Muon, SOAP, and the hybrid SOAP-Muon, for training NequIP and Allegro MLIP models. We find that these optimizers can substantially outperform Adam in both convergence speed and final accuracy. SOAP and SOAP-Muon emerge as robust and consistently strong methods, while Muon only provides partial gains relative to Adam. The improvements are particularly pronounced under partial force supervision. Our results indicate that optimizer choice is an overlooked yet impactful design axis for MLIPs.

### 🤖 AI 总结

**一句话总结**：Machine learning interatomic potentials (MLIPs) have become a hallmark of AI for scientific simulation. While efforts on new architectures and datasets have led to increasingly accurate and general mo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Beyond, Adam, SOAP, Muon, Faster, Label-Efficient, Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02499v1) | [下载PDF](https://arxiv.org/pdf/2607.02499v1.pdf)

---

## [27. Neuron-Aware Data Selection for Annotation-Free LLM Self-Distillation](https://arxiv.org/abs/2607.02460v1)

**作者**：Zhuowei Chen, Xiang Lorraine Li  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-02

### 📄 论文摘要

Post-training large language models (LLMs) without real-world interaction feedback or human-labeled supervision remains challenging, particularly in specialized domains where expert annotations are costly to obtain. Recent annotation-free self-evolution methods address this by using the model's own outputs as supervision signals, constructing a teacher via additional context and aggregating predictions across multiple rollouts through majority voting to produce pseudo-labels. However, these approaches are not without drawbacks: SFT- and GRPO-based variants suffer out-of-domain performance degradation, while reward-based on-policy RL inflates calibration error. In this paper, we propose Neuron On-Policy Self-Distillation (Neuron-OPSD), a data-centric framework for annotation-free self-distillation that leverages internal neuron activations to guide both training-data selection and teacher context construction. The model is then trained via on-policy distillation from the teacher distribution, requiring no ground-truth labels at any stage. Across specialized-domain benchmarks, Neuron-OPSD improves in-domain task performance while preserving cross-domain generalization and mitigating calibration collapse over prior annotation-free baselines. This framework is particularly relevant to settings where online interaction or external supervision is costly or infeasible, and is conceptually distinct from offline RL approaches that rely on logged, reward-labeled trajectories.

### 🤖 AI 总结

**一句话总结**：Post-training large language models (LLMs) without real-world interaction feedback or human-labeled supervision remains challenging, particularly in specialized domains where expert annotations are co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Neuron-Aware, Data, Selection, Annotation-Free, Self-Distillation, Post-training, large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02460v1) | [下载PDF](https://arxiv.org/pdf/2607.02460v1.pdf)

---

## [28. Understanding the Robustness of Distributed Self-Supervised Learning Frameworks Against Non-IID Data](https://arxiv.org/abs/2607.02447v1)

**作者**：Xuanyu Chen, Nan Yang, Shuai Wang 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-02

### 📄 论文摘要

Recent research has introduced distributed self-supervised learning (D-SSL) approaches to leverage vast amounts of unlabeled decentralized data. However, D-SSL faces the critical challenge of data heterogeneity, and there is limited theoretical understanding of how different D-SSL frameworks respond to this challenge. To fill this gap, we present a rigorous theoretical analysis of the robustness of D-SSL frameworks under non-IID (non-independent and identically distributed) settings. Our results show that pre-training with Masked Image Modeling (MIM) is inherently more robust to heterogeneous data than Contrastive Learning (CL), and that the robustness of decentralized SSL increases with average network connectivity, implying that federated learning (FL) is no less robust than decentralized learning (DecL). These findings provide a solid theoretical foundation for guiding the design of future D-SSL algorithms. To further illustrate the practical implications of our theory, we introduce MAR loss, a refinement of the MIM objective with local-to-global alignment regularization. Extensive experiments across model architectures and distributed settings validate our theoretical insights, and additionally confirm the effectiveness of MAR loss as an application of our analysis.

### 🤖 AI 总结

**一句话总结**：Recent research has introduced distributed self-supervised learning (D-SSL) approaches to leverage vast amounts of unlabeled decentralized data. However, D-SSL faces the critical challenge of data het...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Understanding, Robustness, Distributed, Self-Supervised, Learning, Frameworks, Against

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02447v1) | [下载PDF](https://arxiv.org/pdf/2607.02447v1.pdf)

---

## [29. Extreme Adaptive Transformer for Time Series Forecasting](https://arxiv.org/abs/2607.02437v1)

**作者**：Sanjeev Shrestha, Hui Liu, Yifan Zhang  
**分类**：cs.LG  
**发布时间**：2026-07-02

### 📄 论文摘要

Time series forecasting remains challenging when the underlying data contain rare but critical extreme events. This issue is particularly important in hydrologic forecasting, where streamflow distributions are often highly skewed and extreme peaks can have substantial impacts on flood monitoring, water resource management, and early warning systems. Although Transformer-based forecasting models have achieved strong performance by modeling long-range temporal dependencies, they typically treat all time points uniformly and may therefore underrepresent rare extreme patterns. In this paper, we propose the Extreme-Adaptive Transformer (Exformer), a forecasting framework designed to explicitly model temporal dependencies involving both normal and extreme events. Exformer introduces an extreme-adaptive attention mechanism composed of three sparse components: Local, Stride, and Extreme. The Local and Stride components capture short-term and periodic temporal dependencies, respectively, while the Extreme component selectively models event-aware dependencies between normal and extreme streamflow patterns. Experiments on four real-world hydrologic streamflow datasets show that Exformer achieves superior 3-day forecasting performance compared with state-of-the-art baselines. Our findings demonstrate that explicitly incorporating extreme-aware attention improves the forecasting capacity of Transformer models on imbalanced time series with rare but consequential events.

### 🤖 AI 总结

**一句话总结**：Time series forecasting remains challenging when the underlying data contain rare but critical extreme events. This issue is particularly important in hydrologic forecasting, where streamflow distribu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Extreme, Adaptive, Transformer, Time, Series, Forecasting, remains, challenging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02437v1) | [下载PDF](https://arxiv.org/pdf/2607.02437v1.pdf)

---

## [30. QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition](https://arxiv.org/abs/2607.02426v1)

**作者**：Quoc Bao Phan, Tuy Tan Nguyen  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-02

### 📄 论文摘要

Federated learning (FL) enables collaborative model training across distributed devices without sharing raw data, making it suitable for privacy-sensitive robotic sensing applications. However, multi-agent systems generate heterogeneous and non-independent and identically distributed (non-IID) multimodal sensor streams that degrade conventional FL algorithms, while classical fusion modules introduce substantial parameter overhead and communication cost. This paper proposes QFedAgent, a hybrid quantum-classical personalized FL framework for multi-agent activity recognition. The approach integrates a variational quantum circuit fusion module that models accelerometer--gyroscope interactions through quantum state encoding and entanglement, requiring only 72 quantum rotation parameters versus 33K in classical multi-layer perceptron-based fusion, achieving approximately 10x total parameter reduction. Experiments on the OPPORTUNITY dataset under subject-based non-IID partitions demonstrate 97.7% mean test accuracy, confirming that parameter-efficient quantum fusion remains competitive with conventional federated baselines.

### 🤖 AI 总结

**一句话总结**：Federated learning (FL) enables collaborative model training across distributed devices without sharing raw data, making it suitable for privacy-sensitive robotic sensing applications. However, multi-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, QFedAgent, Quantum-Enhanced, Personalized, Federated, Learning, Activity, Recognition

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.02426v1) | [下载PDF](https://arxiv.org/pdf/2607.02426v1.pdf)

---

