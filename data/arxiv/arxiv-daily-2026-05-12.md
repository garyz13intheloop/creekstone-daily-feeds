# arXiv AI 论文日报 | 2026-05-12

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (10 篇)
- [cs.LG](#csLG) (9 篇)
- [cs.AI](#csAI) (3 篇)
- [cs.CL](#csCL) (8 篇)

---

## cs.AI

## [1. Shepherd: A Runtime Substrate Empowering Meta-Agents with a Formalized Execution Trace](https://arxiv.org/abs/2605.10913v1)

**作者**：Simon Yu, Derek Chong, Ananjan Nandi 等 7 位作者  
**分类**：cs.AI, cs.PL, cs.SE  
**发布时间**：2026-05-11

### 📄 论文摘要

We introduce Shepherd, a functional programming model that formalizes meta-agent operations on target agents as functions, with core operations mechanized in Lean. Shepherd records every agent-environment interaction as a typed event in a Git-like execution trace, enabling any past state to be forked and replayed. The system forks the agent process and its filesystem $5\times$ faster than Docker, achieving $>95\%$ prompt-cache reuse on replay. We demonstrate the model through three applications. First, in runtime intervention, a live supervisor increases pair coding pass rates from 28.8% to 54.7% on CooperBench. Second, in counterfactual meta-optimization, branching exploration outperforms baselines across four benchmarks by up to 11 points while reducing wall-clock time by up to 58%. Third, in Tree-RL training, forking rollouts at selected turns improves TerminalBench-2 performance from 34.2% to 39.4%. These results establish Shepherd as an efficient infrastructure for programming meta-agents. We open-source the system to support future research.

### 🤖 AI 总结

**一句话总结**：We introduce Shepherd, a functional programming model that formalizes meta-agent operations on target agents as functions, with core operations mechanized in Lean. Shepherd records every agent-environ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Shepherd, Runtime, Substrate, Empowering, Meta-Agents, Formalized, Execution, Trace

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10913v1) | [下载PDF](https://arxiv.org/pdf/2605.10913v1.pdf)

---

## [2. Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory](https://arxiv.org/abs/2605.10870v1)

**作者**：Mingxi Zou, Zhihan Guo, Langzhang Liang 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-11

### 📄 论文摘要

Long-horizon language agents must operate under limited runtime memory, yet existing memory mechanisms often organize experience around descriptive criteria such as relevance, salience, or summary quality. For an agent, however, memory is valuable not because it faithfully describes the past, but because it preserves the distinctions between histories that must remain separated under a fixed budget to support good decisions. We cast this as a decision-centric rate-distortion problem, measuring memory quality by the loss in achievable decision quality induced by compression. This yields an exact forgetting boundary for what can be safely forgotten, and a memory-distortion frontier characterizing the optimal tradeoff between memory budget and decision quality. Motivated by this decision-centric view of memory, we propose DeMem, an online memory learner that refines its partition only when data certify that a shared state would induce decision conflict, and prove near-minimax regret guarantees. On both controlled synthetic diagnostics and long-horizon conversational benchmarks, DeMem yields consistent gains under the same runtime budget, supporting the principle that memory should preserve the distinctions that matter for decisions, not descriptions.

### 🤖 AI 总结

**一句话总结**：Long-horizon language agents must operate under limited runtime memory, yet existing memory mechanisms often organize experience around descriptive criteria such as relevance, salience, or summary qua...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Remember, Decision, Not, Rate-Distortion, Framework, Memory, Long-horizon

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10870v1) | [下载PDF](https://arxiv.org/pdf/2605.10870v1.pdf)

---

## [3. BenchCAD: A Comprehensive, Industry-Standard Benchmark for Programmatic CAD](https://arxiv.org/abs/2605.10865v1)

**作者**：Haozhe Zhang, Kaichen Liu, Miaomiao Chen 等 7 位作者  
**分类**：cs.AI, cs.CV, cs.SE  
**发布时间**：2026-05-11

### 📄 论文摘要

Industrial Computer-Aided Design (CAD) code generation requires models to produce executable parametric programs from visual or textual inputs. Beyond recognizing the outer shape of a part, this task involves understanding its 3D structure, inferring engineering parameters, and choosing CAD operations that reflect how the part would be designed and manufactured. Despite the promise of Multimodal large language models (MLLMs) for this task, they are rarely evaluated on whether these capabilities jointly hold in realistic industrial CAD settings. We present BenchCAD, a unified benchmark for industrial CAD reasoning. BenchCAD contains 17,900 execution-verified CadQuery programs across 106 industrial part families, including bevel gears, compression springs, twist drills, and other reusable engineering designs. It evaluates models through visual question answering, code question answering, image-to-code generation, and instruction-guided code editing, enabling fine-grained analysis across perception, parametric abstraction, and executable program synthesis. Across 10+ frontier models, BenchCAD shows that current systems often recover coarse outer geometry but fail to produce faithful parametric CAD programs. Common failures include missing fine 3D structure, misinterpreting industrial design parameters, and replacing essential operations such as sweeps, lofts, and twist-extrudes with simpler sketch-and-extrude patterns. Fine-tuning and reinforcement learning improve in-distribution performance, but generalization to unseen part families remains limited. These results position BenchCAD as a benchmark for measuring and improving the industrial readiness of multimodal CAD automation.

### 🤖 AI 总结

**一句话总结**：Industrial Computer-Aided Design (CAD) code generation requires models to produce executable parametric programs from visual or textual inputs. Beyond recognizing the outer shape of a part, this task ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BenchCAD, Comprehensive, Industry-Standard, Benchmark, Programmatic, CAD, Industrial, Computer-Aided

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10865v1) | [下载PDF](https://arxiv.org/pdf/2605.10865v1.pdf)

---

## cs.CL

## [4. WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation](https://arxiv.org/abs/2605.10912v1)

**作者**：Shuangrui Ding, Xuanlang Dai, Long Xing 等 17 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-11

### 📄 论文摘要

Large language and vision-language models increasingly power agents that act on a user's behalf through command-line interface (CLI) harnesses. However, most agent benchmarks still rely on synthetic sandboxes, short-horizon tasks, mock-service APIs, and final-answer checks, leaving open whether agents can complete realistic long-horizon work in the runtimes where they are deployed. This work presents WildClawBench, a native-runtime benchmark of 60 human-authored, bilingual, multimodal tasks spanning six thematic categories. Each task averages roughly 8 minutes of wall-clock time and over 20 tool calls, and runs inside a reproducible Docker container hosting an actual CLI agent harness (OpenClaw, Claude Code, Codex, or Hermes Agent) with access to real tools rather than mock services. Grading is hybrid, combining deterministic rule-based checks, environment-state auditing of side effects, and an LLM/VLM judge for semantic verification. Across 19 frontier models, the best, Claude Opus 4.7, reaches only 62.2% overall under OpenClaw, while every other model stays below 60%, and switching harness alone shifts a single model by up to 18 points. These results show that long-horizon, native-runtime agent evaluation remains a far-from-resolved task for current frontier models. We release the tasks, code, and containerized tooling to support reproducible evaluation.

### 🤖 AI 总结

**一句话总结**：Large language and vision-language models increasingly power agents that act on a user's behalf through command-line interface (CLI) harnesses. However, most agent benchmarks still rely on synthetic s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, WildClawBench, Benchmark, Real-World, Long-Horizon, Evaluation, Large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10912v1) | [下载PDF](https://arxiv.org/pdf/2605.10912v1.pdf)

---

## [5. RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards](https://arxiv.org/abs/2605.10899v1)

**作者**：Gaotang Li, Bhavana Dalvi Mishra, Zifeng Wang 等 12 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-05-11

### 📄 论文摘要

Training deep research agents, namely systems that plan, search, evaluate evidence, and synthesize long-form reports, pushes reinforcement learning beyond the regime of verifiable rewards. Their outputs lack ground-truth answers, their trajectories span many tool-augmented decisions, and standard post-training offers little mechanism for turning past attempts into reusable experience. In this work, we argue that rubrics should serve not merely as final-answer evaluators, but as the shared interface that structures policy execution, judge feedback, and agent memory. Based on this view, we introduce RubricEM, a rubric-guided reinforcement learning framework that combines stagewise policy decomposition with reflection-based meta-policy evolution. RubricEM first makes research trajectories stage-aware by conditioning planning, evidence gathering, review, and synthesis on self-generated rubrics. It then assigns credit with Stage-Structured GRPO, which uses stagewise rubric judgments to provide denser semantic feedback for long-horizon optimization. In parallel, RubricEM trains a shared-backbone reflection meta-policy that distills judged trajectories into reusable rubric-grounded guidance for future attempts. The resulting RubricEM-8B achieves strong performance across four long-form research benchmarks, outperforming comparable open models and approaching proprietary deep-research systems. Beyond final performance, we perform thorough analyses to understand the key ingredients of RubricEM.

### 🤖 AI 总结

**一句话总结**：Training deep research agents, namely systems that plan, search, evaluate evidence, and synthesize long-form reports, pushes reinforcement learning beyond the regime of verifiable rewards. Their outpu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RubricEM, Meta-RL, Rubric-guided, Policy, Decomposition, beyond, Verifiable, Rewards

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10899v1) | [下载PDF](https://arxiv.org/pdf/2605.10899v1.pdf)

---

## [6. Grounded or Guessing? LVLM Confidence Estimation via Blind-Image Contrastive Ranking](https://arxiv.org/abs/2605.10893v1)

**作者**：Reza Khanmohammadi, Erfan Miahi, Simerjot Kaur 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-11

### 📄 论文摘要

Large vision-language models suffer from visual ungroundedness: they can produce a fluent, confident, and even correct response driven entirely by language priors, with the image contributing nothing to the prediction. Existing confidence estimation methods cannot detect this, as they observe model behavior under normal inference with no mechanism to determine whether a prediction was shaped by the image or by text alone. We introduce BICR (Blind-Image Contrastive Ranking), a model-agnostic confidence estimation framework that makes this contrast explicit during training by extracting hidden states from a frozen LVLM twice: once with the real image-question pair, and once with the image blacked out while the question is held fixed. A lightweight probe is trained on the real-image hidden state and regularized by a ranking loss that penalizes higher confidence on the blacked-out view, teaching it to treat visual grounding as a signal of reliability at zero additional inference cost. Evaluated across five modern LVLMs and seven baselines on a benchmark covering visual question answering, object hallucination detection, medical imaging, and financial document understanding, BICR achieves the best cross-LVLM average on both calibration and discrimination simultaneously, with statistically significant discrimination gains robust to cluster-aware analysis at 4-18x fewer parameters than the strongest probing baseline.

### 🤖 AI 总结

**一句话总结**：Large vision-language models suffer from visual ungroundedness: they can produce a fluent, confident, and even correct response driven entirely by language priors, with the image contributing nothing ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：or, Grounded, Guessing?, LVLM, Confidence, Estimation, via, Blind-Image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10893v1) | [下载PDF](https://arxiv.org/pdf/2605.10893v1.pdf)

---

## [7. Neural at ArchEHR-QA 2026: One Method Fits All: Unified Prompt Optimization for Clinical QA over EHRs](https://arxiv.org/abs/2605.10877v1)

**作者**：Abrar Majeedi, Viswanatha Reddy Gajjala, Sai Prasanna Teja Reddy Bogireddy 等 4 位作者  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-05-11

### 📄 论文摘要

Automated question answering (QA) over electronic health records (EHRs) demands precise evidence retrieval, faithful answer generation, and explicit grounding of answers in clinical notes. In this work, we present Neural1.5, our method for the ArchEHR-QA 2026 shared task at CL4Health@LREC 2026, which comprises four subtasks: question interpretation, evidence identification, answer generation, and evidence alignment. Our approach decouples the task into independent, modular stages and employs DSPy"s MIPROv2 optimizer to automatically discover high-performing prompts, jointly tuning instructions and few-shot demonstrations for each stage. Within every stage, self-consistency voting over multiple stochastic inference runs suppresses spurious errors and improves reliability, while stage-specific verification mechanisms (e.g., self-reflection and chain-of-verification for alignment) further refine output quality. Among all teams that participated in all four subtasks, our method ranks second overall (mean rank 4.00), placing 4th, 1st, 4th, and 7th on Subtasks 1-4, respectively. These results demonstrate that systematic, per-stage prompt optimization combined with self-consistency mechanisms is a cost-effective alternative to model fine-tuning for multifaceted clinical QA.

### 🤖 AI 总结

**一句话总结**：Automated question answering (QA) over electronic health records (EHRs) demands precise evidence retrieval, faithful answer generation, and explicit grounding of answers in clinical notes. In this wor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Neural, ArchEHR-QA, One, Method, Fits, All, Unified

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10877v1) | [下载PDF](https://arxiv.org/pdf/2605.10877v1.pdf)

---

## [8. DGPO: Beyond Pairwise Preferences with Directional Consistent Groupwise Optimization](https://arxiv.org/abs/2605.10863v1)

**作者**：Mengyi Deng, Zhiwei Li, Xin Li 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-11

### 📄 论文摘要

Although Large Language Models (LLMs) have made remarkable progress, current preference optimization methods still struggle to align directional consistency while preserving reasoning diversity. To address this limitation, we propose Directional-Groupwise Preference Optimization (DGPO), a lightweight framework that aggregates supervision signals at the group level and explicitly models direction-aware alignment through multi-candidate comparisons. DGPO organizes forward and reverse question-answer instances into structured sets and optimizes a margin-based likelihood objective that separates coherent reasoning paths from inconsistent alternatives. This group-wise formulation captures richer relative information than pairwise objectives and reinforces consistency across diverse reasoning pathways. Empirical results show that our constructed reverse data yields a 3.2% average improvement across five benchmarks, while DGPO further delivers consistent gains across multiple datasets and model families, achieving average accuracy improvements of up to 3.6%.

### 🤖 AI 总结

**一句话总结**：Although Large Language Models (LLMs) have made remarkable progress, current preference optimization methods still struggle to align directional consistency while preserving reasoning diversity. To ad...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DGPO, Beyond, Pairwise, Preferences, Directional, Consistent, Groupwise, Optimization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10863v1) | [下载PDF](https://arxiv.org/pdf/2605.10863v1.pdf)

---

## [9. RUBEN: Rule-Based Explanations for Retrieval-Augmented LLM Systems](https://arxiv.org/abs/2605.10862v1)

**作者**：Joel Rorseth, Parke Godfrey, Lukasz Golab 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-11

### 📄 论文摘要

This paper demonstrates RUBEN, an interactive tool for discovering minimal rules to explain the outputs of retrieval-augmented large language models (LLMs) in data-driven applications. We leverage novel pruning strategies to efficiently identify a minimal set of rules that subsume all others. We further demonstrate novel applications of these rules for LLM safety, specifically to test the resiliency of safety training and effectiveness of adversarial prompt injections.

### 🤖 AI 总结

**一句话总结**：This paper demonstrates RUBEN, an interactive tool for discovering minimal rules to explain the outputs of retrieval-augmented large language models (LLMs) in data-driven applications. We leverage nov...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, RUBEN, Rule-Based, Explanations, Retrieval-Augmented, Systems, paper, demonstrates

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10862v1) | [下载PDF](https://arxiv.org/pdf/2605.10862v1.pdf)

---

## [10. Learning More from Less: Exploiting Counterfactuals for Data-Efficient Chart Understanding](https://arxiv.org/abs/2605.10855v1)

**作者**：Jianzhu Bao, Haozhen Zhang, Kuicai Dong 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-11

### 📄 论文摘要

Vision-Language Models (VLMs) have demonstrated remarkable progress in chart understanding, largely driven by supervised fine-tuning (SFT) on increasingly large synthetic datasets. However, scaling SFT data alone is inefficient and overlooks a key property of charts: charts are programmatically generated visual artifacts, where small, code-controlled visual changes can induce drastic shifts in semantics and correct answers. Learning this counterfactual sensitivity requires VLMs to discriminate fine-grained visual differences, yet standard SFT treats training instances independently and provides limited supervision to enforce this behavior. To address this, we introduce ChartCF, a data-efficient training framework designed to enhance counterfactual sensitivity. ChartCF consists of: (1) a counterfactual data synthesis pipeline via code modification, (2) a chart similarity-based data selection strategy that filters overly difficult samples for improved training efficiency, and (3) multimodal preference optimization across both textual and visual modalities. Experiments on five benchmarks show that ChartCF achieves superior or comparable performance to strong chart-specific VLMs while using significantly less training data.

### 🤖 AI 总结

**一句话总结**：Vision-Language Models (VLMs) have demonstrated remarkable progress in chart understanding, largely driven by supervised fine-tuning (SFT) on increasingly large synthetic datasets. However, scaling SF...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, More, Less, Exploiting, Counterfactuals, Data-Efficient, Chart, Understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10855v1) | [下载PDF](https://arxiv.org/pdf/2605.10855v1.pdf)

---

## [11. Grounded Satirical Generation with RAG](https://arxiv.org/abs/2605.10853v1)

**作者**：Oona Itkonen, Yuxin Su, Linyao Du 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-11

### 📄 论文摘要

Humor generation remains challenging task for Large Language Models (LLMs), due to their subjective nature. We focus on satire, a form of humor strongly shaped by context. In this work, we present a novel pipeline for grounded satire generation that uses Retrieval-Augmented Generation (RAG) over current news to produce satirical dictionary definitions in the Finnish context. We also introduce a new task-specific evaluation framework and annotate 100 generated definitions with six human annotators, enabling analysis across multiple experimental conditions, including cultural background, source-word type, and the presence or absence of RAG. Our results show that the generated definitions are perceived as more political than humorous. Both topic-based word selection and RAG improve the political relevance of the outputs, but neither yields clear gains in humor generation. In addition, our LLM-as-a-judge evaluation of five state-of-the-art models indicates that LLMs correlate well with human judgments on political relevance, but perform poorly on humor. We release our code and annotated dataset to support further research on grounded satire generation and evaluation.

### 🤖 AI 总结

**一句话总结**：Humor generation remains challenging task for Large Language Models (LLMs), due to their subjective nature. We focus on satire, a form of humor strongly shaped by context. In this work, we present a n...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RAG, Grounded, Satirical, Generation, Humor, remains, challenging, task

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10853v1) | [下载PDF](https://arxiv.org/pdf/2605.10853v1.pdf)

---

## cs.CV

## [12. Power Reinforcement Post-Training of Text-to-Image Models with Super-Linear Advantage Shaping](https://arxiv.org/abs/2605.10937v1)

**作者**：Haoyuan Sun, Jing Wang, Yuxin Song 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-11

### 📄 论文摘要

Recently, post-training methods based on reinforcement learning, with a particular focus on Group Relative Policy Optimization (GRPO), have emerged as the robust paradigm for further advancement of text-to-image (T2I) models. However, these methods are often prone to reward hacking, wherein models exploit biases in imperfect reward functions rather than yielding genuine performance gains. In this work, we identify that normalization could lead to miscalibration and directly removing the prompt-level standard deviation term yields an optimal policy ascent direction that is linear in the advantage but still limits the separation of genuine signals from noise. To mitigate the above issues, we propose Super-Linear Advantage Shaping (SLAS) by revisiting the functional update from an information geometry perspective. By extending the Fisher-Rao information metric with advantage-dependent weighting, SLAS introduces a non-linear geometric structure that reshapes the local policy space. This design relaxes constraints along high-advantage directions to amplify informative updates, while tightening those in low-advantage regions to suppress illusory gradients. In addition, batch-level normalization is applied to stabilize training under varying reward scales. Extensive evaluations demonstrate that SLAS consistently surpasses the DanceGRPO baseline across multiple backbones and benchmarks. In particular, it yields faster training dynamics, improved out-of-domain performance on GenEval and UniGenBench++, and enhanced robustness to model scaling, while mitigating reward hacking and preserving semantic and compositional fidelity in generations.

### 🤖 AI 总结

**一句话总结**：Recently, post-training methods based on reinforcement learning, with a particular focus on Group Relative Policy Optimization (GRPO), have emerged as the robust paradigm for further advancement of te...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Power, Reinforcement, Post-Training, Text-to-Image, Models, Super-Linear, Advantage

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10937v1) | [下载PDF](https://arxiv.org/pdf/2605.10937v1.pdf)

---

## [13. Personal Visual Context Learning in Large Multimodal Models](https://arxiv.org/abs/2605.10936v1)

**作者**：Zihui Xue, Ami Baid, Sangho Kim 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-11

### 📄 论文摘要

As wearable devices like smart glasses integrate Large Multimodal Models (LMMs) into the continuous first-person visual streams of individual users, the evolution of these models into true personal assistants hinges on visual personalization: the ability to reason over visual information unique to the wearer. We formalize this capability as Personal Visual Context Learning (Personal VCL), the prompt-time capability of using user-specific visual context to resolve personalized queries. To systematically evaluate this, we present Personal-VCL-Bench, a comprehensive benchmark capturing the personal visual world across persons, objects, and behaviors. Our analysis of frontier LMMs identifies a profound context utilization gap, revealing that the mechanisms for leveraging visual evidence, as well as aggregating multiple visual observations, remain critically understudied. Motivated by these findings, we propose the Agentic Context Bank, a strong inference-time baseline that structures a user's visual context into a self-refining memory bank and employs query-adaptive evidence selection. Our baseline approach consistently improves over standard context prompting regimes across tasks and evaluated backbones, demonstrating a practical path towards future personalized LMMs.

### 🤖 AI 总结

**一句话总结**：As wearable devices like smart glasses integrate Large Multimodal Models (LMMs) into the continuous first-person visual streams of individual users, the evolution of these models into true personal as...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, Personal, Visual, Context, Learning, Large, Multimodal, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10936v1) | [下载PDF](https://arxiv.org/pdf/2605.10936v1.pdf)

---

## [14. Pixal3D: Pixel-Aligned 3D Generation from Images](https://arxiv.org/abs/2605.10922v1)

**作者**：Dong-Yang Li, Wang Zhao, Yuxin Chen 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-11

### 📄 论文摘要

Recent advances in 3D generative models have rapidly improved image-to-3D synthesis quality, enabling higher-resolution geometry and more realistic appearance. Yet fidelity, which measures pixel-level faithfulness of the generated 3D asset to the input image, still remains a central bottleneck. We argue this stems from an implicit 2D-3D correspondence issue: most 3D-native generators synthesize shape in canonical space and inject image cues via attention, leaving pixel-to-3D associations ambiguous. To tackle this issue, we draw inspiration from 3D reconstruction and propose Pixal3D, a pixel-aligned 3D generation paradigm for high-fidelity 3D asset creation from images. Instead of generating in a canonical pose, Pixal3D directly generates 3D in a pixel-aligned way, consistent with the input view. To enable this, we introduce a pixel back-projection conditioning scheme that explicitly lifts multi-scale image features into a 3D feature volume, establishing direct pixel-to-3D correspondence without ambiguity. We show that Pixal3D is not only scalable and capable of producing high-quality 3D assets, but also substantially improves fidelity, approaching the fidelity level of reconstruction. Furthermore, Pixal3D naturally extends to multi-view generation by aggregating back-projected feature volumes across views. Finally, we show pixel-aligned generation benefits scene synthesis, and present a modular pipeline that produces high-fidelity, object-separated 3D scenes from images. Pixal3D for the first time demonstrates 3D-native pixel-aligned generation at scale, and provides a new inspiring way towards high-fidelity 3D generation of object or scene from single or multi-view images. Project page: https://ldyang694.github.io/projects/pixal3d/

### 🤖 AI 总结

**一句话总结**：Recent advances in 3D generative models have rapidly improved image-to-3D synthesis quality, enabling higher-resolution geometry and more realistic appearance. Yet fidelity, which measures pixel-level...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Pixal3D, Pixel-Aligned, Generation, Images, Recent, advances, generative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10922v1) | [下载PDF](https://arxiv.org/pdf/2605.10922v1.pdf)

---

## [15. Confidence-Guided Diffusion Augmentation for Enhanced Bangla Compound Character Recognition](https://arxiv.org/abs/2605.10916v1)

**作者**：Md. Sultan Al Rayhan, Maheen Islam  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-11

### 📄 论文摘要

Recognition of handwritten Bangla compound characters remains a challenging problem due to complex character structures, large intra-class variation, and limited availability of high-quality annotated data. Existing Bangla handwritten character recognition systems often struggle to generalize across diverse writing styles, particularly for compound characters containing intricate ligatures and diacritical variations. In this work, we propose a confidence-guided diffusion augmentation framework for low-resolution Bangla compound character recognition. Our framework combines class-conditional diffusion modeling with classifier guidance to synthesize high-quality handwritten compound character samples. To further improve generation quality, we introduce Squeeze-and-Excitation enhanced residual blocks within the diffusion model's U-Net backbone. We additionally propose a confidence-based filtering mechanism where pre-trained classifiers act as quality gates to retain only highly class-consistent synthetic samples. The filtered synthetic images are fused with the original training data and used to retrain multiple classification architectures. Experiments conducted on the AIBangla compound character dataset demonstrate consistent performance improvements across ResNet50, DenseNet121, VGG16, and Vision Transformer architectures. Our best-performing model achieves 89.2\% classification accuracy, surpassing the previously published AIBangla benchmark by a substantial margin. The results demonstrate that quality-aware diffusion augmentation can effectively enhance handwritten character recognition performance in low-resource script domains.

### 🤖 AI 总结

**一句话总结**：Recognition of handwritten Bangla compound characters remains a challenging problem due to complex character structures, large intra-class variation, and limited availability of high-quality annotated...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Confidence-Guided, Augmentation, Enhanced, Bangla, Compound, Character, Recognition

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10916v1) | [下载PDF](https://arxiv.org/pdf/2605.10916v1.pdf)

---

## [16. CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models](https://arxiv.org/abs/2605.10903v1)

**作者**：Wenxuan Song, Han Zhao, Fuhao Li 等 10 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-05-11

### 📄 论文摘要

This paper proposes a novel approach to address the challenge that pretrained VLA models often fail to effectively improve performance and reduce adaptation costs during standard supervised finetuning (SFT). Some advanced finetuning methods with auxiliary training objectives can improve performance and reduce the number of convergence steps. However, they typically incur significant computational overhead due to the additional losses from auxiliary objectives. To simultaneously achieve the enhanced capabilities of auxiliary training with the simplicity of standard SFT, we decouple the two objectives of auxiliary-objective SFT within the parameter space, namely, enhancing general capabilities and fitting task-specific action distributions. To deliver the goal, we only need to train the model to converge on a small-scale task set using two distinct training strategies, resulting in two finetuned models. The parameters' difference between the two models can then be interpreted as capability vectors provided by auxiliary objectives. These vectors are then merged with pretrained parameters to form a capability-enhanced meta model. Moreover, when standard SFT is augmented with a lightweight orthogonal regularization loss, the merged model attains performance comparable to auxiliary finetuned baselines with reduced computational overhead. Internal and external experiments demonstrate that our capability vectors (1) are effective and versatile across diverse models, (2) can generalize to novel environments and embodiments out of the box.

### 🤖 AI 总结

**一句话总结**：This paper proposes a novel approach to address the challenge that pretrained VLA models often fail to effectively improve performance and reduce adaptation costs during standard supervised finetuning...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CapVector, Learning, Transferable, Capability, Vectors, Parametric, Space, Vision-Language-Action

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10903v1) | [下载PDF](https://arxiv.org/pdf/2605.10903v1.pdf)

---

## [17. Counterfactual Stress Testing for Image Classification Models](https://arxiv.org/abs/2605.10894v1)

**作者**：Moritz Stammel, Fabio De Sousa Ribeiro, Raghav Mehta 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-11

### 📄 论文摘要

Deep learning models in medical imaging often fail when deployed in new clinical environments due to distribution shifts in demographics, scanner hardware, or acquisition protocols. A central challenge is underspecification, where models with similar validation performance exhibit divergent real-world failure modes. Although stress testing has emerged as a tool to assess this, current methods typically rely on simple, uninformed perturbations (e.g., brightness or contrast changes), which fail to capture clinically realistic variation and can overestimate robustness. In this work, we introduce a counterfactual stress testing framework based on causal generative models that create realistic "what if" images by intervening on attributes such as scanner type and patient sex while preserving anatomical identity, enabling controlled and semantically meaningful evaluation under targeted distribution shifts. Across two imaging modalities (chest X-ray and mammography), three model architectures, and multiple shift scenarios, we show that counterfactual stress tests provide a substantially more accurate proxy for real out-of-distribution performance than classical perturbations, capturing the direction and relative magnitude of performance changes as well as model ranking. These results suggest that causal generative models can serve as practical simulators for robustness assessment, offering a more reliable basis for evaluating medical AI systems prior to deployment.

### 🤖 AI 总结

**一句话总结**：Deep learning models in medical imaging often fail when deployed in new clinical environments due to distribution shifts in demographics, scanner hardware, or acquisition protocols. A central challeng...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Counterfactual, Stress, Testing, Image, Classification, Models, Deep, learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10894v1) | [下载PDF](https://arxiv.org/pdf/2605.10894v1.pdf)

---

## [18. Count Anything at Any Granularity](https://arxiv.org/abs/2605.10887v1)

**作者**：Chang Liu, Haoning Wu, Weidi Xie  
**分类**：cs.CV  
**发布时间**：2026-05-11

### 📄 论文摘要

Open-world object counting remains brittle: despite rapid advances in vision-language models (VLMs), reliably counting the objects a user intends is far from solved. We argue that a central reason is that counting granularity is left implicit; users may refer to a specific identity, an attribute, an instance type, a category, or an abstract concept, yet most methods treat "what to count" as a single, category-level matching problem. In this work, we redefine open-world counting as multi-grained counting, where visual exemplars specify target appearance and fine-grained text, with optional negative prompts, specifies the intended semantic granularity across five explicit levels. Making granularity explicit, however, exposes a critical data bottleneck: existing counting datasets lack the multi-category scenes, controlled distractors, and instance-level annotations needed to verify fine-grained prompt semantics. To address this, we propose the first fully automatic data-scaling pipeline that integrates controllable 3D synthesis with consistent image editing and VLM-based filtering, and use it to construct KubriCount, the largest and most comprehensively annotated counting dataset to date, supporting both training and multi-grained evaluation. Systematic benchmarking reveals that both multimodal large language models and specialist counting models exhibit severe prompt-following failures under fine-grained distinctions. Motivated by these findings, we train HieraCount, a multi-grained counting model that jointly leverages text and visual exemplars as complementary target specifications. HieraCount substantially improves multi-grained counting accuracy and generalizes robustly to challenging real-world scenarios. The project page is available here: https://verg-avesta.github.io/KubriCount/.

### 🤖 AI 总结

**一句话总结**：Open-world object counting remains brittle: despite rapid advances in vision-language models (VLMs), reliably counting the objects a user intends is far from solved. We argue that a central reason is ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Count, Anything, Any, Granularity, Open-world, object, counting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10887v1) | [下载PDF](https://arxiv.org/pdf/2605.10887v1.pdf)

---

## [19. Geometry-aware Prototype Learning for Cross-domain Few-shot Medical Image Segmentation](https://arxiv.org/abs/2605.10885v1)

**作者**：Feifan Song, Yuntian Bo, Haofeng Zhang  
**分类**：cs.CV  
**发布时间**：2026-05-11

### 📄 论文摘要

Cross-domain few-shot medical image segmentation (CD-FSMIS) requires a model to generalise simultaneously to novel anatomical categories and unseen imaging domains from only a handful of annotated examples. Existing prototypical approaches inevitably entangle anatomical structure with domain-specific appearance variations, and thus lack a stable reference for reliable matching under domain shift. We observe that the geometric structure of human anatomy constitutes a reliable, domain-transferable prior that has been overlooked. Building on this insight, we propose GeoProto, a geometry-aware CD-FSMIS framework that enriches prototypical matching with explicit structural priors. The core component, Geometry-Aware Prototype Enrichment (GAPE), augments each local appearance prototype with a learned geometric offset encoding its ordinal position within the organ's interior topology. This offset is derived from an auxiliary Ordinal Shape Branch (OSB) trained under an ordinally consistent objective that enforces monotonic variation of geometric embeddings across interior strata, requiring no annotation beyond standard segmentation masks. Extensive experiments across seven datasets spanning three evaluation settings (cross-modality, cross-sequence, and cross-context) demonstrate that GeoProto achieves state-of-the-art performance.

### 🤖 AI 总结

**一句话总结**：Cross-domain few-shot medical image segmentation (CD-FSMIS) requires a model to generalise simultaneously to novel anatomical categories and unseen imaging domains from only a handful of annotated exa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Geometry-aware, Prototype, Learning, Cross-domain, Few-shot, Medical, Image, Segmentation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10885v1) | [下载PDF](https://arxiv.org/pdf/2605.10885v1.pdf)

---

## [20. CADBench: A Multimodal Benchmark for AI-Assisted CAD Program Generation](https://arxiv.org/abs/2605.10873v1)

**作者**：Anna C. Doris, Jacob Thomas Sony, Ghadi Nehme 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-11

### 📄 论文摘要

Recovering editable CAD programs from images or 3D observations is central to AI-assisted design, but progress is difficult to measure because existing evaluations are fragmented across datasets, modalities, and metrics. We introduce CADBench, a unified benchmark for multimodal CAD program generation. CADBench contains 18,000 evaluation samples spanning six benchmark families derived from DeepCAD, Fusion 360, ABC, MCB, and Objaverse; five input modalities including clean meshes, noisy meshes, single-view renders, photorealistic renders, and multi-view renders; and six metrics covering geometric fidelity, executability, and program compactness. STEP-based families are stratified by B-rep face count and all families are diversity-sampled to support controlled analysis across complexity and object variation. We benchmark eleven CAD-specialized and general-purpose vision-language systems, generating more than 1.4 million CAD programs. Under idealized inputs, specialized mesh-to-CAD models substantially outperform code-generating VLMs, which remain far from reliable CAD program reconstruction. CADBench further reveals three recurring failure modes: reconstruction quality degrades with geometric complexity, CAD-specialized models can be brittle under modality shift, and model rankings change across metrics. Together, these results position CADBench as a diagnostic testbed for measuring progress in editable 3D reconstruction and multimodal CAD understanding. The benchmark is publicly available at https://huggingface.co/datasets/DeCoDELab/CADBench.

### 🤖 AI 总结

**一句话总结**：Recovering editable CAD programs from images or 3D observations is central to AI-assisted design, but progress is difficult to measure because existing evaluations are fragmented across datasets, moda...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CADBench, Multimodal, Benchmark, AI-Assisted, CAD, Program, Generation, Recovering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10873v1) | [下载PDF](https://arxiv.org/pdf/2605.10873v1.pdf)

---

## [21. Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858v1)

**作者**：Lingdong Kong, Ao Liang, Tianyi Yan 等 23 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-05-11

### 📄 论文摘要

Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally. Some generate photorealistic textures but violate basic physics; others maintain geometric consistency but fail when subjected to closed-loop planning. This disconnect exposes a critical gap: the field evaluates how real generated worlds appear, but rarely whether they behave realistically. We introduce WorldLens, a unified benchmark that measures world-model fidelity across the full spectrum, from pixel quality and 4D geometry to closed-loop driving and human perceptual alignment, through five complementary aspects and 24 standardized dimensions. Our evaluation of six representative models reveals that no existing approach dominates across all axes: texture-rich models violate geometry, geometry-aware models lack behavioral fidelity, and even the strongest performers achieve only 2-3 out of 10 on human realism ratings. To bridge algorithmic metrics with human perception, we further contribute WorldLens-26K, a 26,808-entry human-annotated preference dataset pairing numerical scores with textual rationales, and WorldLens-Agent, a vision-language evaluator distilled from these judgments that enables scalable, explainable auto-assessment. Together, the benchmark, dataset, and agent form a unified ecosystem for assessing generated worlds not merely by visual appeal, but by physical and behavioral fidelity.

### 🤖 AI 总结

**一句话总结**：Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally. Some generate photorealistic textures but violate basic physics; others maintain...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Driving, World, Model, All-Around, Player?, Today's, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10858v1) | [下载PDF](https://arxiv.org/pdf/2605.10858v1.pdf)

---

## cs.LG

## [22. Variational Inference for Lévy Process-Driven SDEs via Neural Tilting](https://arxiv.org/abs/2605.10934v1)

**作者**：Yaman Kindap, Manfred Opper, Benjamin Dupuis 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CV, cs.RO, stat.ML  
**发布时间**：2026-05-11

### 📄 论文摘要

Modelling extreme events and heavy-tailed phenomena is central to building reliable predictive systems in domains such as finance, climate science, and safety-critical AI. While Lévy processes provide a natural mathematical framework for capturing jumps and heavy tails, Bayesian inference for Lévy-driven stochastic differential equations (SDEs) remains intractable with existing methods: Monte Carlo approaches are rigorous but lack scalability, whereas neural variational inference methods are efficient but rely on Gaussian assumptions that fail to capture discontinuities. We address this tension by introducing a neural exponential tilting framework for variational inference in Lévy-driven SDEs. Our approach constructs a flexible variational family by exponentially reweighting the Lévy measure using neural networks. This parametrization preserves the jump structure of the underlying process while remaining computationally tractable. To enable efficient inference, we develop a quadratic neural parametrization that yields closed-form normalization of the tilted measure, a conditional Gaussian representation for stable processes that facilitates simulation, and symmetry-aware Monte Carlo estimators for scalable optimization. Empirically, we demonstrate that the method accurately captures jump dynamics and yields reliable posterior inference in regimes where Gaussian-based variational approaches fail, on both synthetic and real-world datasets.

### 🤖 AI 总结

**一句话总结**：Modelling extreme events and heavy-tailed phenomena is central to building reliable predictive systems in domains such as finance, climate science, and safety-critical AI. While Lévy processes provide...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Variational, Inference, Lévy, Process-Driven, SDEs, via, Neural, Tilting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10934v1) | [下载PDF](https://arxiv.org/pdf/2605.10934v1.pdf)

---

## [23. Dynamic Skill Lifecycle Management for Agentic Reinforcement Learning](https://arxiv.org/abs/2605.10923v1)

**作者**：Junhao Shen, Teng Zhang, Xiaoyan Zhao 等 4 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-05-11

### 📄 论文摘要

Large language model agents increasingly rely on external skills to solve complex tasks, where skills act as modular units that extend their capabilities beyond what parametric memory alone supports. Existing methods assume external skills either accumulate as persistent guidance or internalized into the policy, eventually leading to zero-skill inference. We argue this assumption is overly restrictive, since with limited parametric capacity and uneven marginal contribution across skills, the optimal active skill set is non-monotonic, task- and stage-dependent. In this work, we propose SLIM, a framework of dynamic Skill LIfecycle Management for agentic reinforcement learning (RL), which treats the active external skill set as a dynamic optimization variable jointly updated with policy learning. Specifically, SLIM estimates each active skill's marginal external contribution through leave-one-skill-out validation, then applies three lifecycle operations: retaining high-value skills, retiring skills whose contribution becomes negligible after sufficient exposure, and expanding the skill bank when persistent failures reveal missing capability coverage. Experiments show that SLIM outperforms the best baselines by an average of 7.1% points across ALFWorld and SearchQA. Results further indicate that policy learning and external skill retention are not mutually exclusive: some skills are absorbed into the policy, while others continue to provide external value, supporting SLIM as a more general paradigm for skill-based agentic RL.

### 🤖 AI 总结

**一句话总结**：Large language model agents increasingly rely on external skills to solve complex tasks, where skills act as modular units that extend their capabilities beyond what parametric memory alone supports. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Dynamic, Skill, Lifecycle, Management, Agentic, Reinforcement, Learning, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10923v1) | [下载PDF](https://arxiv.org/pdf/2605.10923v1.pdf)

---

## [24. Optimal and Scalable MAPF via Multi-Marginal Optimal Transport and Schrödinger Bridges](https://arxiv.org/abs/2605.10917v1)

**作者**：Usman A. Khan, Joseph W. Durham  
**分类**：cs.LG, cs.MA, cs.RO  
**发布时间**：2026-05-11

### 📄 论文摘要

We consider anonymous multi-agent path finding (MAPF) where a set of robots is tasked to travel to a set of targets on a finite, connected graph. We show that MAPF can be cast as a special class of multi-marginal optimal transport (MMOT) problems with an underlying Markovian structure, under which the exponentially large MMOT collapses to a linear program (LP) polynomial in size. Focusing on the anonymous setting, we establish conditions under which the corresponding LP is feasible, totally unimodular, and consequently, yields min-cost, integral $(\{0,1\})$ transports that do not overlap in both space and time. To adapt the approach to large-scale problems, we cast the MAPF-MMOT in a probabilistic framework via Schrödinger bridges. Under standard assumptions, we show that the Schrödinger bridge formulation reduces to an entropic regularization of the corresponding MMOT that admits an iterative Sinkhorn-type solution. The Schrödinger bridge, being a probabilistic framework, provides a shadow (fractional) transport that we use as a template to solve a reduced LP and demonstrate that it results in near-optimal, integral transports at a significant reduction in complexity. Extensive experiments highlight the optimality and scalability of the proposed approaches.

### 🤖 AI 总结

**一句话总结**：We consider anonymous multi-agent path finding (MAPF) where a set of robots is tasked to travel to a set of targets on a finite, connected graph. We show that MAPF can be cast as a special class of mu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Optimal, Scalable, MAPF, via, Multi-Marginal, Transport, Schrödinger, Bridges

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10917v1) | [下载PDF](https://arxiv.org/pdf/2605.10917v1.pdf)

---

## [25. DataMaster: Towards Autonomous Data Engineering for Machine Learning](https://arxiv.org/abs/2605.10906v1)

**作者**：Yaxin Du, Xiyuan Yang, Zhifan Zhou 等 15 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-11

### 📄 论文摘要

As model families, training recipes, and compute budgets become increasingly standardized, further gains in machine learning systems depend increasingly on data. Yet data engineering remains largely manual and ad hoc: practitioners repeatedly search for external datasets, adapt them to existing pipelines, validate candidate data through downstream training, and carry forward lessons from prior attempts. We study task-conditioned autonomous data engineering, where an autonomous agent improves a fixed learning algorithm by optimizing only the data side, including external data discovery, data selection and composition, cleaning and transformation. The goal is to obtain a stronger downstream solution while leaving the learning algorithm unchanged. To address the open-ended search space, branch-dependent refinement, and delayed validation inherent in autonomous data engineering, we propose DataMaster, a data-agent framework that integrates tree-structured search, shared candidate data, and cumulative memory. DataMaster consists of three key components: a DataTree that organizes alternative data-engineering branches, a shared Data Pool that stores discovered external data sources for reuse, and a Global Memory that records node outcomes, artifacts, and reusable findings. Together, these components allow the agent to discover candidate data, construct executable training inputs, evaluate them through downstream feedback, and carry useful evidence across branches. We evaluate DataMaster on two types of benchmarks, MLE-Bench Lite and PostTrainBench. On MLE-Bench Lite, it improves medal rate by 32.27% over the initial score; on PostTrainBench, it surpasses the instruct model on GPQA (31.02% vs 30.35%).

### 🤖 AI 总结

**一句话总结**：As model families, training recipes, and compute budgets become increasingly standardized, further gains in machine learning systems depend increasingly on data. Yet data engineering remains largely m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, DataMaster, Towards, Autonomous, Data, Engineering, Machine, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10906v1) | [下载PDF](https://arxiv.org/pdf/2605.10906v1.pdf)

---

## [26. Beyond Red-Teaming: Formal Guarantees of LLM Guardrail Classifiers](https://arxiv.org/abs/2605.10901v1)

**作者**：Nikita Kezins, Urbas Ekka, Pascal Berrang 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-11

### 📄 论文摘要

Guardrail Classifiers defend production language models against harmful behavior, but although results seem promising in testing, they provide no formal guarantees. Providing formal guarantees for such models is hard because "harmful behavior" has no natural specification in a discrete input space: and the standard epsilon-ball properties used in other domains do not carry semantic meaning. We close this gap by shifting verification from the discrete input space to the classifier's pre-activation space, where we define a harmful region as a convex shape enclosing the representations of known harmful prompts. Because the sigmoid classification head is monotonic, certifying the worst-case point is sufficient to certify the entire region, yielding a closed-form soundness proof without approximation in O(d) time. To formally evaluate these classifiers, we propose two constructions of such regions: SVD-aligned hyper-rectangles, which yield exact SAT/UNSAT certificates, and Gaussian Mixture Models, which yield probabilistic certificates over semantically coherent clusters. Applying this framework to three author-trained Guardrail Classifiers on the toxicity domain, every hyper-rectangle configuration returns SAT, exposing verifiable safety holes across all classifiers, despite seemingly high empirical metrics. Probabilistic GMM certificates also expose a divergent structural stability in how these models represent harm. While GPT-2 and Llama-3.1-8B maintain robust coverage of 90% and 80% across varying boundaries, BERT's safety guarantees prove uniquely volatile. This 'coverage collapse' to 55% at the optimal threshold reveals a sparsely populated safety margin in BERT, which only achieves full coverage by adopting an extremely conservative pessimistic threshold. These approaches combined, provide new insights on how effective Guardrail Classifiers really are, beyond traditional red-teaming.

### 🤖 AI 总结

**一句话总结**：Guardrail Classifiers defend production language models against harmful behavior, but although results seem promising in testing, they provide no formal guarantees. Providing formal guarantees for suc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Beyond, Red-Teaming, Formal, Guarantees, Guardrail, Classifiers

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10901v1) | [下载PDF](https://arxiv.org/pdf/2605.10901v1.pdf)

---

## [27. V4FinBench: Benchmarking Tabular Foundation Models, LLMs, and Standard Methods on Corporate Bankruptcy Prediction](https://arxiv.org/abs/2605.10896v1)

**作者**：Marcin Kostrzewa, Sebastian Tomczak, Roman Furman 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-05-11

### 📄 论文摘要

Corporate bankruptcy prediction is a high-stakes financial task characterized by severe class imbalance and multi-horizon forecasting demands. Public datasets supporting it remain scarce and small: widely used free benchmarks contain between 6,000 and 80,000 company-year observations, while larger resources are behind subscription paywalls. To address this gap, we introduce V4FinBench, a benchmark of over one million company-year records from the Visegràd Group (V4) economies (2006-2021), with 131 financial and non-financial features, six prediction horizons, and a composite distress criterion jointly capturing solvency, profitability, and liquidity deterioration. V4FinBench is designed to support the evaluation of tabular and foundation-model methods under realistic class imbalance, with positive rates between 0.19% and 0.36%. We provide reference evaluations of standard tabular baselines, finetuned TabPFN, and QLoRA-finetuned Llama-3-8B. With imbalance-aware finetuning, TabPFN matches or exceeds gradient boosting at longer time horizons on both $F_1$-score and ROC-AUC. In contrast, Llama-3-8B trails gradient boosting on ROC-AUC at every horizon and is generally weaker on $F_1$-score, with the gap widening sharply beyond the immediate horizon. In an external evaluation on the American Bankruptcy Dataset, the V4FinBench-finetuned TabPFN checkpoint improves over vanilla TabPFN, suggesting that adaptation captures transferable financial-distress structure rather than only V4-specific patterns. V4FinBench is publicly released to support further evaluation and development of prediction methods on realistic financial data.

### 🤖 AI 总结

**一句话总结**：Corporate bankruptcy prediction is a high-stakes financial task characterized by severe class imbalance and multi-horizon forecasting demands. Public datasets supporting it remain scarce and small: wi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, V4FinBench, Benchmarking, Tabular, Foundation, Models, Standard, Methods

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10896v1) | [下载PDF](https://arxiv.org/pdf/2605.10896v1.pdf)

---

## [28. LoKA: Low-precision Kernel Applications for Recommendation Models At Scale](https://arxiv.org/abs/2605.10886v1)

**作者**：Liang Luo, Yinbin Ma, Quanyu Zhu 等 23 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-11

### 📄 论文摘要

Recent GPU generations deliver significantly higher FLOPs using lower-precision arithmetic, such as FP8. While successfully applied to large language models (LLMs), its adoption in large recommendation models (LRMs) has been limited. This is because LRMs are numerically sensitive, dominated by small matrix multiplications (GEMMs) followed by normalization, and trained in communication-intensive environments. Applying FP8 directly to LRMs often degrades model quality and prolongs training time. These challenges are inherent to LRM workloads and cannot be resolved merely by introducing better FP8 kernels. Instead, a system-model co-design approach is needed to successfully integrate FP8. We present LoKA (Low-precision Kernel Applications), a framework that makes FP8 practical for LRMs through three principles: profile under realistic distributions to know where low precision is safe, co-design model components with hardware to expand where it is safe, and orchestrate across kernel libraries to maximize the gains. Concretely, LoKA Probe is a statistically grounded, online benchmarking method that learns activation and weight statistics, and quantifies per-layer errors. This process pinpoints safe and unsafe, fast and slow sites for FP8 adoption. LoKA Mods is a set of reusable model adaptations that improve both numerical stability and execution efficiency with FP8. LoKA Dispatch is a runtime that leverages the statistical insights from LoKA Probe to select the fastest FP8 kernel that satisfies the accuracy requirements.

### 🤖 AI 总结

**一句话总结**：Recent GPU generations deliver significantly higher FLOPs using lower-precision arithmetic, such as FP8. While successfully applied to large language models (LLMs), its adoption in large recommendatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：At, LoKA, Low-precision, Kernel, Applications, Recommendation, Models, Scale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10886v1) | [下载PDF](https://arxiv.org/pdf/2605.10886v1.pdf)

---

## [29. Neural Weight Norm = Kolmogorov Complexity](https://arxiv.org/abs/2605.10878v1)

**作者**：Tiberiu Musat  
**分类**：cs.LG, cs.IT  
**发布时间**：2026-05-11

### 📄 论文摘要

Why does weight decay work? We prove that, in any fixed-precision regime, the smallest weight norm of a looped neural network outputting a binary string equals the Kolmogorov complexity of that string, up to a logarithmic factor. This implies that weight decay induces a prior matching Solomonoff's universal prior, the optimal prior over computable functions, up to a polynomial factor. The result is norm-agnostic: in fixed precision, every weight norm collapses to the non-zero parameter count up to constants, so the same sandwich bound holds for any norm used as a regulariser. The proof has two short reductions: any program for a universal Turing machine can be encoded into neural weights at unit cost per program bit, and any fixed-precision network can be described by enumerating its non-zero parameters with logarithmic addressing overhead. Both bounds are tight up to constants, with the logarithmic factor realised by permutation encodings: a network whose parameters encode a permutation produces a string whose Kolmogorov complexity is the non-zero parameter count times its logarithm. The fixed-precision assumption is essential: with infinite precision, neural networks can encode non-computable functions and the weight norm loses its relevance.

### 🤖 AI 总结

**一句话总结**：Why does weight decay work? We prove that, in any fixed-precision regime, the smallest weight norm of a looped neural network outputting a binary string equals the Kolmogorov complexity of that string...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Neural, Weight, Norm, Kolmogorov, Complexity, Why, does, decay

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10878v1) | [下载PDF](https://arxiv.org/pdf/2605.10878v1.pdf)

---

## [30. AssayBench: An Assay-Level Virtual Cell Benchmark for LLMs and Agents](https://arxiv.org/abs/2605.10876v1)

**作者**：Edward De Brouwer, Carl Edwards, Alexander Wu 等 12 位作者  
**分类**：cs.LG, cs.AI, q-bio.QM  
**发布时间**：2026-05-11

### 📄 论文摘要

Recent advances in machine learning and large-scale biological data collections have revived the prospect of building a virtual cell, a computational model of cellular behavior that could accelerate biological discovery. One of the most compelling promises of this vision is the ability to perform in silico phenotypic screens, in which a model predicts the effects of cellular perturbations in unseen biological contexts. This task combines heterogeneous textual inputs with diverse phenotypic outputs, making it particularly well-suited to LLMs and agentic systems. Yet, no standard benchmark currently exists for this task, as existing efforts focus on narrower molecular readouts that are only indirectly aligned with the phenotypic endpoints driving many real-world drug discovery workflows. In this work, we present AssayBench, a benchmark for phenotypic screen prediction, built from 1,920 publicly available CRISPR screens spanning five broad classes of cellular phenotypes. We formulate the screen prediction task as a gene rank prediction for each screen and introduce the adjusted nDCG, a continuous metric for comparing performance across heterogeneous assays. Our extensive evaluation shows that existing methods remain far from empirically estimated performance ceilings and zero-shot generalist LLMs outperform biology-specific LLMs and trainable baselines. Optimization techniques such as fine-tuning, ensembling, and prompt optimization can further improve LLM performance on this task. Overall, AssayBench offers a practical testbed for measuring progress toward in silico phenotypic screening and, more broadly, virtual cell models.

### 🤖 AI 总结

**一句话总结**：Recent advances in machine learning and large-scale biological data collections have revived the prospect of building a virtual cell, a computational model of cellular behavior that could accelerate b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, LLM, Agent, AssayBench, Assay-Level, Virtual, Cell, Benchmark

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.10876v1) | [下载PDF](https://arxiv.org/pdf/2605.10876v1.pdf)

---

