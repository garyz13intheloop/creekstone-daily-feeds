# arXiv AI 论文日报 | 2026-10-20

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (7 篇)
- [cs.CV](#csCV) (10 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.CL](#csCL) (7 篇)

---

## cs.AI

## [1. Train An Imaginative Agent](https://arxiv.org/abs/2610.26845v1)

**作者**：Jiaxin Ge, Junyi Zhang, Tianning Chai 等 12 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-19

### 📄 论文摘要

A seemingly reasonable push in Sokoban can make the puzzle unsolvable. To avoid such mistakes, an agent has to anticipate the consequences of its actions before execution, especially when feedback from the real environment is sparse or actions are irreversible. We introduce Agentic Imagination (Agima), a training framework that trains an agent to imagine before acting, i.e. to be imaginative. Agima trains a single omni model to propose actions, generate images of their outcomes, and then reason over these imagined futures to decide what to execute in the real environment. Rather than committing to a single plan, the agent can simulate a sequence of actions, explore alternatives, and compare possible futures. We first use supervised fine-tuning (SFT) to unify policy and world modeling within a single omni model. This enables the agent to predict future outcomes and perform basic forms of imagination, such as forward thinking and counterfactual branching. We then use agentic reinforcement learning (RL) to teach the agent to reason with its imagined futures and use them effectively for planning. Across four environments spanning Maze2D, Sokoban, Pacman, and PushT, Agima generalizes to harder settings unseen during training. Trained with SFT alone on two-box Sokoban, Agima solves 40% of four-box puzzles while seeing the real board only once every five moves, compared with an action-only planner that only solves 2%. After RL, new behaviors emerge in how Agima uses its imagination: it learns a new unified format that was unseen during the SFT stage, learns to conduct forward thinking only when necessary, and branches more frequently at critical decision points. An agent that can picture where its actions lead can learn when and where to look ahead, that is, to plan. Project page: https://agima.net/.

### 🤖 AI 总结

**一句话总结**：A seemingly reasonable push in Sokoban can make the puzzle unsolvable. To avoid such mistakes, an agent has to anticipate the consequences of its actions before execution, especially when feedback fro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Agent, Train, Imaginative, seemingly, reasonable, push, Sokoban

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26845v1) | [下载PDF](https://arxiv.org/pdf/2610.26845v1.pdf)

---

## [2. AnyGoal: On World Model Generalization Beyond Expert Rollouts](https://arxiv.org/abs/2610.26844v1)

**作者**：Heejeong Nam, Divyat Mahajan, Quentin Le Lidec 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-19

### 📄 论文摘要

The goal of a world model is to capture the dynamics of an environment. This has the great appeal that it allows agents to plan and simulate a course of actions with the help of a world model. For these uses to be reliable, however, the learned dynamics must behave well beyond the specific state-action combinations observed in expert rollouts. Despite this, the relationship between data coverage, dynamics generalization, and downstream planning performance remains underexplored. We study this relationship through the lens of compositional generalization: can a world model recombine familiar state and action factors into valid dynamics? To answer this, we introduce AnyGoal, a benchmark of goal-shifted task variants built from widely used world-model environments, together with an open-source library. Each task is designed to be within reach of a world model that has learned the underlying dynamics: individual state factors and actions remain within their training support, but their combinations are underrepresented in expert trajectories. Across multiple environments and world model families, we find that current models consistently exhibit failures under these recombinations. By examining dynamics and representation failures across model families, interaction regimes, and evaluation metrics, we study where current world models generalize and where challenges remain for goal-shifted prediction and planning. Together, this framework, benchmark, and analysis provide a basis for evaluating progress toward world models that generalize to new planning tasks.

### 🤖 AI 总结

**一句话总结**：The goal of a world model is to capture the dynamics of an environment. This has the great appeal that it allows agents to plan and simulate a course of actions with the help of a world model. For the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AnyGoal, World, Model, Generalization, Beyond, Expert, Rollouts, goal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26844v1) | [下载PDF](https://arxiv.org/pdf/2610.26844v1.pdf)

---

## [3. Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy](https://arxiv.org/abs/2610.26836v1)

**作者**：Ke Zhang, Sahchit Chundur, Jerry Peprah Owusu 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-19

### 📄 论文摘要

LLM agents that compute the right answer can still answer wrongly. Agent harnesses increasingly keep long tool outputs out of the context window, saving them to files that the agent searches or reads on demand. We ask where this costs accuracy with a real scientific tool: PHREEQC, a widely used geochemistry simulator from the USGS, whose reports reach 846.8k characters and whose determinism lets every printed value be traced. Agents use it to answer 158 execution-verified multiple-choice items. When agents read the simulator's report through a section index rather than in context, GPT-5.1 and GPT-5.2 lose 11.3 and 7.9 points of accuracy, while Claude Opus 4.6 and Claude Sonnet 4.6 show no detectable cost. Re-running all 11,007 logged simulator calls shows that both GPT models compute the keyed value about as often as before; what changes is the evidence they answer from. Under retrieval they often skip the report, answer from their own higher-precision output files, and misround to a neighboring option, a failure we call evidence substitution. With the simulation held fixed, retrieval still costs GPT-5.2 9.4 points. For GPT-5.4, more frequent correct simulations mask an evidence-use loss of about ten points, leaving a net change indistinguishable from zero. Naming the authoritative output raises accuracy by 6.3-7.9 points over plain retrieval for the three GPT models; for GPT-5.1 and GPT-5.2, inlining outputs that fit works as well, while asking for correct rounding does not. Context-management choices in agent harnesses should be judged by where accuracy is lost, not only by final accuracy.

### 🤖 AI 总结

**一句话总结**：LLM agents that compute the right answer can still answer wrongly. Agent harnesses increasingly keep long tool outputs out of the context window, saving them to files that the agent searches or reads ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Same, Simulation, Different, Evidence, Where, Retrieved, Tool, Output

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26836v1) | [下载PDF](https://arxiv.org/pdf/2610.26836v1.pdf)

---

## [4. ProteinGeoBench: Frontier Structural-Biology Agents Are Fluent at Lookup but Lost in Geometry](https://arxiv.org/abs/2610.26829v1)

**作者**：Matt Turk, Brandon L. Neel, Diana M. Lopez 等 6 位作者  
**分类**：cs.AI, cs.LG, q-bio.BM  
**发布时间**：2026-10-19

### 📄 论文摘要

Frontier agents retrieve structural metadata well and compute geometry from coordinates less reliably. We ask how much of a benchmark score reflects that gap and how much reflects the evaluation configuration around the model. We study ProteinGeoBench, a suite of 131 protein-structure tasks, using 4,249 rollouts from four frontier models and 4,486 further trials across 26 models. Three of the four frontier models fall within 0.031 of one another (0.785 to 0.816) with no difference between them resolved, while the fourth scores 0.707 and all three gaps to it exclude zero. Three of the four do better on metadata lookup than on numeric calculation. The fourth is slightly better on numeric. Numeric tasks are 28 of the 131 but half of the twelve tasks that all four models fail. The ranking also depends on the evaluation budget: with one run per task, 23.9% of bootstrap replicates put a different model first. On a selected 15-task slice, removing network access lowers scores more than blocking eight structural-database domains, but the two contrasts were graded in different passes and cannot be cleanly decomposed. Swapping in each model's own command-line agent changes scores by -0.071 to +0.086, a comparison too small to rule out moderate harness effects. Across 26 models, numeric performance rises with non-numeric performance rather than staying flat. The experiments use different task subsets, so they cannot rank model, harness, access and task composition against one another. Evaluations should report results by task family, along with the number of runs, the harness and the access conditions.

### 🤖 AI 总结

**一句话总结**：Frontier agents retrieve structural metadata well and compute geometry from coordinates less reliably. We ask how much of a benchmark score reflects that gap and how much reflects the evaluation confi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, at, ProteinGeoBench, Frontier, Structural-Biology, Fluent, Lookup, but

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26829v1) | [下载PDF](https://arxiv.org/pdf/2610.26829v1.pdf)

---

## [5. Agent World Model in the Wild: Computer-Use Agent Environment Synthesis](https://arxiv.org/abs/2610.26828v1)

**作者**：Zhaoyang Wang, Qianhui Wu, Haorui Wang 等 12 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-10-19

### 📄 论文摘要

Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems is challenging and can introduce substantial security risks. We therefore propose Agent World Model in the Wild (WildAWM), a scalable pipeline for synthesizing controllable environments and tasks for training general computer-use agents (CUAs). Whereas existing approaches typically specialize in a single agent interaction interface, we construct executable environments that jointly support graphical user interfaces, model context protocol services, and command-line interfaces, allowing agents to flexibly combine visual interaction, tool use, and code execution. WildAWM is entirely powered by open-source models, demonstrating that high-quality computer-use environments can be generated without proprietary frontier models. Beyond environments, we address three recurring challenges in task synthesis: ensuring solvability, maintaining sufficient difficulty, and producing reliable verifiers, by introducing execution-based quality gates that combine heterogeneous agent rollouts, cross-judge consistency checks, and counterfactual probes of judgment robustness. The resulting pipeline synthesizes 341 long-horizon environment-task pairs that can require over 100 agent steps to solve and remain challenging even for frontier models, with GPT-6-Astra solving only 60% of them. We train two Qwen models of different sizes exclusively in these synthetic worlds. Both models achieve substantial gains across 8 out-of-distribution benchmarks spanning web, claw, and computer-use agents, demonstrating that learning in WildAWM's synthesized worlds generalizes broadly to unseen computer-use tasks. The code is publicly available at https://github.com/MSR-Orchard/WildAWM.

### 🤖 AI 总结

**一句话总结**：Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems is challenging and c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, World, Model, Wild, Computer-Use, Environment, Synthesis, learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26828v1) | [下载PDF](https://arxiv.org/pdf/2610.26828v1.pdf)

---

## [6. LG-Bench: A Graph-Structured Evaluation Benchmark for Life Sciences](https://arxiv.org/abs/2610.26787v1)

**作者**：Lu Sun, Xiangyi Zhang, Xiangyang Zhu 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-19

### 📄 论文摘要

Traditional evaluation benchmarks reduce inherently interconnected scientific knowledge in life sciences into flat lists of questions, disregarding the underlying topological structure of the knowledge. We introduce, the first graph-structured benchmark for life sciences, featuring over 10,000 high-quality multiple-choice questions across medicine, biology, and chemistry. Our approach constructs a weighted evaluation graph using bidirectional matching and semantic similarity algorithms, where nodes represent questions and edge weights capture their semantic relationships. Leveraging this graph topology, we design two novel evaluation metrics. The Global Coherence Score (GCS) measures a model's consistency within semantically related neighborhoods, while Knowledge Balance Score (KBS) analyzes how model errors are distributed across the graph to reveal conceptual blind spots. LG-Bench facilitates fine-grained comparison of LLMs by surfacing differences in conceptual coherence and patterns of knowledge organization across models. Our framework shifts the evaluation paradigm from flat accuracy metrics to structure-aware analysis, offering a new lens for diagnosing and improving LLM performance in the life sciences domain.

### 🤖 AI 总结

**一句话总结**：Traditional evaluation benchmarks reduce inherently interconnected scientific knowledge in life sciences into flat lists of questions, disregarding the underlying topological structure of the knowledg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LG-Bench, Graph-Structured, Evaluation, Benchmark, Life, Sciences, Traditional, benchmarks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26787v1) | [下载PDF](https://arxiv.org/pdf/2610.26787v1.pdf)

---

## cs.CL

## [7. Competing Learning in Hybrid Architectures](https://arxiv.org/abs/2610.26830v1)

**作者**：Xingyu Shen, Yingfa Chen, Ziqing Qiao 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-19

### 📄 论文摘要

Many modern language models have adopted hybrid architectures that incorporate both linear-time recurrence and softmax attention. Modern recurrence layers provide a highly expressive mixing mechanism while ensuring high throughput by compressing contextual information into a fixed-size state, but underperform softmax attention in contextual information retrieval. In this paper, we reveal a Competing Learning phenomenon where different kinds of mixers compete to learn the same function, and when any layer learns a function, it suppresses the corresponding learning signal for other layers. Layer attribution analysis reveals that under typical data distributions, modern recurrence learns retrieval functions faster than softmax attention, causing attention to fail to learn retrieval in most cases. Stopping weight updates in recurrence in the middle of training helps attention learn retrieval. Based on these results, we propose a staged training procedure for pre-training hybrid architectures on natural language. Empirical results on models up to 1B parameters show that our method results in substantial improvement in language modeling loss, common-sense reasoning, as well as a wide range of retrieval-related tasks across different context lengths.

### 🤖 AI 总结

**一句话总结**：Many modern language models have adopted hybrid architectures that incorporate both linear-time recurrence and softmax attention. Modern recurrence layers provide a highly expressive mixing mechanism ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Competing, Learning, Hybrid, Architectures, Many, modern, language, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26830v1) | [下载PDF](https://arxiv.org/pdf/2610.26830v1.pdf)

---

## [8. RefCraft: Benchmarking Visual-Reference-Conditioned Agentic Generation through Web Development](https://arxiv.org/abs/2610.26826v1)

**作者**：Yuchi Wang, Rongyao Fang, Weihao Yu 等 10 位作者  
**分类**：cs.CL, cs.AI, cs.CV  
**发布时间**：2026-10-19

### 📄 论文摘要

Beyond basic tool use and coding skills, effectively incorporating visual references into agentic generation is equally essential for applying AI agents to real-world productivity tasks. We study this crucial capability through webpage development, a practical and readily evaluable setting in which existing benchmarks remain largely idealized: they typically focus on reconstructing visual targets or generating webpages from textual instructions alone, overlooking the more common workflow of developing from visual examples. Specifically, we introduce RefCraft, a benchmark comprising 300 realistic multimodal webpage-development tasks that combine natural-language instructions with screenshots from one to five reference webpages. Agents must selectively interpret and utilize these references while rendering, visually inspecting, and iteratively refining their outputs. We evaluate the resulting open-ended artifacts using independently verifiable keypoints and complementary programmatic and VLM judges. Across nine frontier (M)LLMs, the strongest system achieves an overall score of only 52.12 out of 100, revealing that visual-reference-conditioned agentic generation remains a substantial challenge for current models in practical webpage-development settings.

### 🤖 AI 总结

**一句话总结**：Beyond basic tool use and coding skills, effectively incorporating visual references into agentic generation is equally essential for applying AI agents to real-world productivity tasks. We study this...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RefCraft, Benchmarking, Agentic, Generation, through, Web, Development, Beyond

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26826v1) | [下载PDF](https://arxiv.org/pdf/2610.26826v1.pdf)

---

## [9. SpecMRL: Redesign Matryoshka Representation Learning within Parametric Spectrum](https://arxiv.org/abs/2610.26824v1)

**作者**：Zhongxin Chen, Songhao Wu, Heng Cui 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-19

### 📄 论文摘要

Matryoshka Representation Learning (MRL) is designed to support flexible representation sizes by jointly optimizing nested prefixes. While effective, this design lacks an explicit constraint to ensure that the leading portion provides a suitable compact encoding. To address this, we propose SpecMRL, which reorganizes the feature space to enable more effective prefix readout. Specifically, we extend MRL with a parameter-derived spectral basis organized with feature importance. SpecMRL otherwise follows standard MRL, with prefix readout performed in the learned spectral space. Experiments on MTEB show that SpecMRL outperforms MRL at all evaluated reduced dimensions, with larger gains under more aggressive compression. These results suggest that the learned spectral basis better prioritizes informative directions, enabling more effective representation compression. Notably, SpecMRL extends the performance frontier of MRL, surpassing full-dimensional MRL with only half the embedding dimensions.

### 🤖 AI 总结

**一句话总结**：Matryoshka Representation Learning (MRL) is designed to support flexible representation sizes by jointly optimizing nested prefixes. While effective, this design lacks an explicit constraint to ensure...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SpecMRL, Redesign, Matryoshka, Representation, Learning, within, Parametric, Spectrum

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26824v1) | [下载PDF](https://arxiv.org/pdf/2610.26824v1.pdf)

---

## [10. AfriBED: a Speech Recognition Bias Evaluation Dataset for Low Resource African Languages](https://arxiv.org/abs/2610.26821v1)

**作者**：Claytone Sikasote, Hussein Suleman, Jan Buys  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-10-19

### 📄 论文摘要

Despite advancements in automatic speech recognition systems (ASR), current systems exhibit speaker-attribute bias, i.e., their speech recognition performance is biased against certain speakers based on their demographic attributes such as gender, accents, and speaker type. However, accurately assessing speaker attribute bias in a given ASR system requires the availability of a bias evaluation dataset with comparable speech across subgroups of a speaker attribute. In this paper, we introduce African speech Bias Evaluation Dataset (AfriBED), a novel speech recognition bias evaluation dataset for two low resource African languages, Bemba and Nyanja, to detect and estimate gender and speaker-type bias for ASR systems. The dataset comprises 9 hours of speech with 3928 utterances recorded by 80 speakers for Bemba, while the Nyanja set includes 6260 utterances with approximately 18 hours of speech recorded by 127 speakers. The results of our baseline experiments demonstrate that the datasets are useful for examining gender and speaker-type attribute bias in the target languages.

### 🤖 AI 总结

**一句话总结**：Despite advancements in automatic speech recognition systems (ASR), current systems exhibit speaker-attribute bias, i.e., their speech recognition performance is biased against certain speakers based ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AfriBED, Speech, Recognition, Bias, Evaluation, Dataset, Low, Resource

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26821v1) | [下载PDF](https://arxiv.org/pdf/2610.26821v1.pdf)

---

## [11. ASTOR: Benchmarking and Improving Autoformulation for Soft-Constraint Optimization with a Formal Grammar](https://arxiv.org/abs/2610.26819v1)

**作者**：Amer Goel, Yeganeh Alimohammadi, Andrew Daw  
**分类**：cs.CL  
**发布时间**：2026-10-19

### 📄 论文摘要

Real-world decision problems combine two qualitatively different kinds of constraints: requirements that must be satisfied, called hard constraints, and preferences that can be violated, called soft constraints. Because these problems are often posed to decision-makers in natural language, large language models offer a natural tool for assisting with their solution. This has given rise to autoformulation, which focuses on using LLMs to translate natural-language descriptions of decision problems into executable mathematical optimization models. However, this research often neglects soft constraints like those proposed by consumers, managers, and planners, despite the fact that many practical problems require modeling them explicitly. We introduce ASTOR, an inference-time framework that maps a natural-language decision problem to a grammar-guided abstract syntax tree (AST) before deterministically compiling the resulting representation into executable optimization code. We also introduce SoftOR, a unified benchmark of natural language problems which focuses on soft constraint formulations. On SoftOR, ASTOR achieves the best aggregate accuracy among comparable single-request and multi-agent LLM methods while remaining competitive on standard autoformulation benchmarks that include only hard constraints. Code and data are available at https://anonymous.4open.science/r/astor-softor-iclr-E34C/README.md.

### 🤖 AI 总结

**一句话总结**：Real-world decision problems combine two qualitatively different kinds of constraints: requirements that must be satisfied, called hard constraints, and preferences that can be violated, called soft c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ASTOR, Benchmarking, Improving, Autoformulation, Soft-Constraint, Optimization, Formal, Grammar

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26819v1) | [下载PDF](https://arxiv.org/pdf/2610.26819v1.pdf)

---

## [12. Safety Mid-Training: Internalizing LLM Safety as a Foundational Capability](https://arxiv.org/abs/2610.26809v1)

**作者**：Zhengyue Zhao, Liwei Jiang, Yejin Choi 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-19

### 📄 论文摘要

Safety alignment for large language models (LLMs) is primarily performed during post-training, while recent work has also begun incorporating safety data into pre-training. Yet safety can degrade when later training no longer includes safety data, and gains in safety often come at the cost of general capability. This tension suggests that safety and general reasoning should not be treated as separate training goals. We instead view safety as an LLM capability that can be learned through a reasoning structure shared with general tasks. Both require the model to understand intent or task goals, apply relevant knowledge, and reason about potential consequences. We introduce safety mid-training, a stage between pre-training and post-training that jointly develops safety and general reasoning through this shared structure. Given safety and utility prompts, the base model generates structured documents and reasoning traces that are then used for mid-training. Safety mid-training reduces average attack success rate (ASR) by 72% to 81% relative to Qwen3-1.7B, 4B, and 8B base models, while also improving general capability. The benefits persist through subsequent post-training. After general-only SFT, mid-trained models largely retain their safety, achieving lower ASR than the baselines without sacrificing general capability. They also retain safety under general-only GRPO without safety rewards, while subsequent RL reaches a better safety-utility frontier when initialized from the mid-trained models. Together, these results suggest that learning safety and general reasoning within a shared mid-training stage can reduce the safety-utility trade-off and make safety more robust to subsequent training.

### 🤖 AI 总结

**一句话总结**：Safety alignment for large language models (LLMs) is primarily performed during post-training, while recent work has also begun incorporating safety data into pre-training. Yet safety can degrade when...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, as, Safety, Mid-Training, Internalizing, Foundational, Capability, alignment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26809v1) | [下载PDF](https://arxiv.org/pdf/2610.26809v1.pdf)

---

## [13. RESIN: Multi-Chain Reasoning with Entity-Structured Indexing](https://arxiv.org/abs/2610.26782v1)

**作者**：Xuanyu Meng, Jash Rajesh Parekh, Jiawei Han  
**分类**：cs.CL  
**发布时间**：2026-10-19

### 📄 论文摘要

Multi-chain reasoning is a challenging task not only because the multi-chain evidence is dispersed, but also because different parts of reasoning may require distinct, interacting chains of support. Flat retrieval can flood a model with loosely related text, whereas early selection of a single reasoning path can discard evidence that becomes useful only after other facts are considered. We introduce RESIN (Reasoning with Entity Structured Indexing), which uses structure to locate evidence while keeping the original source as the basis for reasoning. RESIN decomposes a question into focused one-hop needs, retrieves a small set of source-grounded units for each hop, and places only this relevant evidence in a compact reasoning buffer. The buffer preserves alternative supports until final composition, making intermediate decisions explicit without forcing a brittle path. On the full HolisQA benchmark, RESIN achieves 82.92 context recall and 76.70 answer relevancy over all questions, with higher reported CR and AR across five domains and higher F1 in four domains than the published baselines. Ablations show that both typed evidence diversity and hop-wise decomposition are essential, supporting a clear conclusion: Precise evidence organization and delayed commitment make multi-chain reasoning effective and auditable. Our code is available at https://github.com/RamonMeng/RESIN.

### 🤖 AI 总结

**一句话总结**：Multi-chain reasoning is a challenging task not only because the multi-chain evidence is dispersed, but also because different parts of reasoning may require distinct, interacting chains of support. F...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RESIN, Multi-Chain, Reasoning, Entity-Structured, Indexing, challenging, task, not

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26782v1) | [下载PDF](https://arxiv.org/pdf/2610.26782v1.pdf)

---

## cs.CV

## [14. Can It Actually Work? Synthesizing Functional CAD Mechanisms](https://arxiv.org/abs/2610.26861v1)

**作者**：Wenqian Zhang, Yangyi Huang, Zigeng Xu 等 5 位作者  
**分类**：cs.CV, cs.CL, cs.GR  
**发布时间**：2026-10-19

### 📄 论文摘要

While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret underspecified requests to construct and iteratively revise mechanisms that satisfy functional requirements in physical simulation. Verifying these requirements is nontrivial: different candidate mechanisms may realize the same function through entirely different components, controls, and operating sequences. To bridge this gap, we propose FunCAD-Harness, a framework that translates abstract requirements into candidate-specific physical tests and uses simulation feedback to guide design revisions. To systematically evaluate this capability, we introduce FunCADBench, a benchmark spanning 46 mechanism families with interdependent and multi-step operations. Experiments across frontier LLM agents show that FunCAD-Harness exposes subtle mechanical failures invisible to visual inspection, substantially improving functional success rates over standard simulation-augmented baselines. Ultimately, our work marks a step toward CAD agents capable of translating human intent into working mechanisms.

### 🤖 AI 总结

**一句话总结**：While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：It, Can, Actually, Work?, Synthesizing, Functional, CAD, Mechanisms

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26861v1) | [下载PDF](https://arxiv.org/pdf/2610.26861v1.pdf)

---

## [15. Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855v1)

**作者**：Tianqi Liu, Hanfei Zhao, Qifeng Liang 等 15 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-10-19

### 📄 论文摘要

World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse embodiments. We curate Xp-Data, comprising 10k hours of egocentric human data and 3k hours of robot data with unified multimodal annotations and systematic quality control. A unified kinematic representation encodes locomotion through camera poses and manipulation through projected skeletons, with robot skeletons combining embodiment-specific forward kinematics with extensive manual keypoint annotation and correction. We also introduce Xp-Teleop, a long-horizon loco-manipulation benchmark based on high-quality dexterous humanoid teleoperation data. Evaluations demonstrate state-of-the-art performance across five cross-embodiment benchmarks (DreamDojo, $Ψ_0$, $ω$-HOME, Xp-Teleop, and AgiBot) and on held-out human egocentric video, from zero-shot inference to few-shot and full-data post-training. Scaling human pre-training data improves performance on both human and robot evaluations. After distillation, our model supports real-time, minute-long rollouts, enabling live VR interaction. Applications in policy evaluation, model-based planning, and world-action modeling further demonstrate the model's utility for embodied decision-making.

### 🤖 AI 总结

**一句话总结**：World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action space...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：W0, Ropedia, Scaling, Loco-Manipulation, World, Models, across, Embodiments

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26855v1) | [下载PDF](https://arxiv.org/pdf/2610.26855v1.pdf)

---

## [16. Manga2Animate: An Agentic Framework for Faithful Manga Animation with Script and Storyboard Planning](https://arxiv.org/abs/2610.26851v1)

**作者**：Sheng-Wei Zhang, Hsi-An Chen, Yan-Ting Liou 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-19

### 📄 论文摘要

Adapting existing manga into coherent animation that stays faithful to the source is a valuable yet challenging task. Existing methods either access the manga mainly through text, losing its characters and art style, or feed manga pages directly into video generation models, which misinterpret the manga's structure and produce incorrect storylines. In this paper, we propose Manga2Animate, a multi-agent framework that grounds every stage of generation in the source manga. We decompose the task into two intermediate representations, an animation script and a visual storyboard. Each representation is produced by a creator agent and reviewed against the source panels by a paired reviewer agent. We tailor representation-specific selection and dual-level feedback to progressively refine both before synthesizing the final animation. Extensive experiments and a user study demonstrate that Manga2Animate produces animations more faithful to the source manga and more consistent across shots than state-of-the-art approaches. Project page: https://annchenn.github.io/Manga2Animate/

### 🤖 AI 总结

**一句话总结**：Adapting existing manga into coherent animation that stays faithful to the source is a valuable yet challenging task. Existing methods either access the manga mainly through text, losing its character...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Manga2Animate, Agentic, Framework, Faithful, Manga, Animation, Script

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26851v1) | [下载PDF](https://arxiv.org/pdf/2610.26851v1.pdf)

---

## [17. GenOlympiad: Benchmarking Frontier Image Models at Their Capability Boundaries](https://arxiv.org/abs/2610.26850v1)

**作者**：Xi Hu, Martin Bell, Liang Zheng  
**分类**：cs.CV  
**发布时间**：2026-10-19

### 📄 论文摘要

Text-to-image models have made tremendous progress and can produce high-quality images. However, a question which would be asked in any other discipline is where the frontier models fall short. We introduce GenOlympiad, a benchmark which provides the most challenging text prompts from nine capability axes for stress-testing frontier text-to-image models. The assessed capabilities include generating large quantities, performing deep reasoning, ensuring hard physical consistency, following complex rules and so on. The prompts are designed such that prompt alignment is visually verifiable (e.g., counting) instead of relying on subjectiveness (e.g., style). Based on this, we develop an automated evaluation framework which decomposes the prompt into easy and hard questions, and for most hard questions, draws help lines to ground evidence for accurate grading. We evaluate 20+ strong text-to-image models, including Nano Banana Pro, GPT-Image-2.5, Seedream-5.0 and so on. We report that even the best-performing T2I model (Nano Banana Pro) only achieves a strict score of 23.9 out of 100 and that coding models such as GPT-6 Astra have higher prompt alignment scores (but not as visually pleasing). We also derive insights in model evolution, alignment with Elo scores, and effectiveness of our grounding-based evaluation protocol. Code is available at https://github.com/GenOlympiad/GenOlympiad and the project page is at https://genolympiad.github.io/

### 🤖 AI 总结

**一句话总结**：Text-to-image models have made tremendous progress and can produce high-quality images. However, a question which would be asked in any other discipline is where the frontier models fall short. We int...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, GenOlympiad, Benchmarking, Frontier, Image, Models, Their, Capability

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26850v1) | [下载PDF](https://arxiv.org/pdf/2610.26850v1.pdf)

---

## [18. SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration](https://arxiv.org/abs/2610.26837v1)

**作者**：Javad Rajabi, Hakki Can Karaimer, David B. Lindell 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-19

### 📄 论文摘要

Diffusion Transformers (DiTs) achieve high-fidelity image and video generation, but they suffer from substantial inference costs due to repeated transformer evaluations across many denoising steps. Feature caching reduces this cost by reusing features across denoising steps. Recent forecasting methods extend this idea by extrapolating features to skipped steps instead of reusing them. However, existing forecasting methods extrapolate the features they predict uniformly, even though the spatial-frequency components of these features change most at different stages of denoising. They also overlook that denoising progresses nonuniformly, so equal step intervals can correspond to very different amounts of change. These mismatches amplify forecast errors as more steps are skipped, limiting the achievable acceleration. We propose SpecKCast, a training-free method that forecasts the model output in the frequency domain. SpecKCast applies a 2D discrete cosine transform (DCT) to the output and tracks each coefficient with a lightweight Kalman filter along a band-specific time coordinate derived from the noise schedule. The filter tracks each coefficient's value and rate of change, and the transformer is evaluated only when the filter's forecast uncertainty exceeds a threshold. Experiments on FLUX.1-dev, Qwen-Image, Wan2.1-14B, and HunyuanVideo show that SpecKCast achieves a better trade-off between acceleration and fidelity than existing caching and forecasting methods, reaching up to 6x speedup with less than 0.05 GiB of additional memory.

### 🤖 AI 总结

**一句话总结**：Diffusion Transformers (DiTs) achieve high-fidelity image and video generation, but they suffer from substantial inference costs due to repeated transformer evaluations across many denoising steps. Fe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, SpecKCast, Spectral, Kalman, Forecasting, Acceleration, Transformers, DiTs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26837v1) | [下载PDF](https://arxiv.org/pdf/2610.26837v1.pdf)

---

## [19. Real-Time Radar Semantic and Panoptic Scene Understanding](https://arxiv.org/abs/2610.26816v1)

**作者**：Santosh Parit, Julia Hindel, Rohit Mohan 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-19

### 📄 论文摘要

Robust scene understanding under varying environmental conditions is essential for safe autonomous driving. While cameras and LiDAR degrade in adverse weather and poor lighting, Frequency-Modulated Continuous-Wave (FMCW) spinning radar provides dependable 360° perception at extended ranges with minimal compute cost. However, real-time FMCW radar scene understanding is challenging due to complex signal returns, limited temporal resolution, and scarce annotated datasets. We introduce StreamRPS, a novel framework for streaming FMCW radar panoptic segmentation, comprising an automated label-generation pipeline via LiDAR scene completion and a real-time streaming network for semantic and panoptic segmentation. Our encoder-decoder streaming architecture comprises a radar-specific hierarchical Transformer encoder and task-specific decoders for semantic or panoptic prediction. Our encoder introduces a stem to capture range-dependent signatures, anisotropic patch embeddings to preserve angular resolution, and axial polar attention to separately model the periodic azimuth and bounded range axes. We further introduce azimuth roll rotation augmentation to simulate ego-vehicle rotation during training. Comprehensive experiments on the SAX and BOREAS datasets validate both our auto-labeling methodology and streaming segmentation network against established baselines. We outperform the strongest baseline by at least 1.4pp while processing sectors at over 400 FPS in a 4-sector streaming setting. We additionally provide manual annotations for 100 SAX radar scans, enabling independent evaluation of the entire framework.

### 🤖 AI 总结

**一句话总结**：Robust scene understanding under varying environmental conditions is essential for safe autonomous driving. While cameras and LiDAR degrade in adverse weather and poor lighting, Frequency-Modulated Co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Real-Time, Radar, Semantic, Panoptic, Scene, Understanding, Robust, under

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26816v1) | [下载PDF](https://arxiv.org/pdf/2610.26816v1.pdf)

---

## [20. PICA-WAM: Visual Perturbation Invariance via Cross-Appearance Self-Alignment in World Action Models](https://arxiv.org/abs/2610.26813v1)

**作者**：Yude Zou, Yifei Yao, Guanbo Jiao 等 6 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-10-19

### 📄 论文摘要

World Action Models (WAMs) jointly predict future video and generate actions, yet remain sensitive to task-irrelevant visual perturbations, i.e., changes in visual appearance that should not affect robot behavior. We identify a gap in conventional WAM training: video prediction encourages representations to preserve appearance information, while action generation does not explicitly enforce invariance to task-irrelevant appearance. Data augmentation exposes WAMs to such perturbations but does not require perturbed and nominal observations to produce consistent action representations, and alignment with external pretrained features does not guarantee the desired invariance. To address this gap, we propose PICA-WAM, a self-supervised training framework that casts perturbation invariance as an auxiliary cross-appearance self-alignment task for WAMs. An exponential-moving-average (EMA) teacher processes the nominal observation to provide a deeper-layer target, while the online WAM processes a perturbed observation and aligns its shallower-layer action representation to this target through a lightweight projection head. Across four strong WAMs evaluated on RoboTwin 2.0, LIBERO-Plus, EBench, and a real robot, PICA-WAM consistently improves robustness under visual perturbations, preserves nominal performance in simulation, and raises the real robot success rate. PICA-WAM further reduces the sensitivity of video features to task-irrelevant appearance and its propagation into actions, as shown by paired layer-wise diagnostics. Code: https://github.com/YudeZou/PICA-WAM-release

### 🤖 AI 总结

**一句话总结**：World Action Models (WAMs) jointly predict future video and generate actions, yet remain sensitive to task-irrelevant visual perturbations, i.e., changes in visual appearance that should not affect ro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PICA-WAM, Visual, Perturbation, Invariance, via, Cross-Appearance, Self-Alignment, World

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26813v1) | [下载PDF](https://arxiv.org/pdf/2610.26813v1.pdf)

---

## [21. State World Models: Execute the Rules, Generate the Pixels](https://arxiv.org/abs/2610.26811v1)

**作者**：Chan Yan Ki, Yanran Zhang, Wenzhao Zheng 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-19

### 📄 论文摘要

Existing world models can generate action-conditioned video from a single image. Many focus on camera movement, allowing users to explore the generated scene. However, navigation alone does not ensure that an action follows persistent rules when its outcome depends on state that is invisible in the current frame. We present Stateful Harness, a framework that separates world evolution from video rendering to support stateful and rule-governed interaction. It maintains an evolving world state under specified rules, renders each resulting event with a frozen video model, and uses the generated clip to update the world state for the next turn. At each turn, the harness resolves the action selected by the user and compiles the resulting event into an instruction, while a preview clip from an editable 3D scene provides spatial and camera guidance. To evaluate rule compliance, we build WorldState-Bench, a benchmark of 50 counterfactual twin pairs that share an initial frame and action but differ in hidden state and required outcome. Under rule-only prompting, the best of the 11 evaluated video backends produces the required endings for both cases in 32% of pairs. For MiniMax-H3, specifying the required endings raises this rate from 32% to 64%, while the full harness reaches 92% with the same frozen model. These results support separating rule execution from video rendering for world interactions with hidden state.

### 🤖 AI 总结

**一句话总结**：Existing world models can generate action-conditioned video from a single image. Many focus on camera movement, allowing users to explore the generated scene. However, navigation alone does not ensure...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：State, World, Models, Execute, Rules, Generate, Pixels, Existing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26811v1) | [下载PDF](https://arxiv.org/pdf/2610.26811v1.pdf)

---

## [22. What Language Adds, and at What Cost: Four Controlled Probes of Pathology Vision-Language Models](https://arxiv.org/abs/2610.26805v1)

**作者**：Wenhao Zhang, Zhongliang Zhou, Yi Ping 等 5 位作者  
**分类**：cs.CV, q-bio.QM  
**发布时间**：2026-10-19

### 📄 论文摘要

Vision--language models (VLMs) promise to make computational pathology queryable and able to draft reports, but how much language adds beyond the vision backbone is unclear, because almost every system is evaluated by its developers on test sets of their own choosing. We grade published evidence by how it was produced and test four claims with controlled probes that reuse released checkpoints and public data, varying one input at a time. Report text adds prognostic signal: adding a frozen embedding of the stage-redacted report to a slide embedding raises the pooled C-index by 0.019 for progression-free interval and by 0.016 for overall survival across 1{,}633 TCGA patients, and restoring the stage statement adds nothing. Prompts add no measurable accuracy at inference: with features and pooling fixed, zero-shot classification is statistically indistinguishable from a supervised linear probe for lung and renal cancer subtyping. Slide-level question answering is barely grounded: SlideChat answers 74.82\% of SlideBench-VQA(TCGA) items correctly with the slide and 74.41\% without it, whereas its language backbone alone reaches 43.52\%. Paraphrasing leaves accuracy unchanged but flips 8--23\% of answers. Self-reported gains from agentic navigation and few-shot language priors cannot yet be attributed to language. Language thus adds real but narrow value, and we propose minimum controls that would expose these failure modes in future evaluations.

### 🤖 AI 总结

**一句话总结**：Vision--language models (VLMs) promise to make computational pathology queryable and able to draft reports, but how much language adds beyond the vision backbone is unclear, because almost every syste...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, What, Language, Adds, Cost, Four, Controlled, Probes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26805v1) | [下载PDF](https://arxiv.org/pdf/2610.26805v1.pdf)

---

## [23. Mise-en-Video: Fine-Grained 3D Control for Multi-Shot Video Generation](https://arxiv.org/abs/2610.26801v1)

**作者**：Yingshuang Zou, Xiaoyu Shi, Yawen Luo 等 11 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-10-19

### 📄 论文摘要

Recent advances in text-to-video generation have enabled high-fidelity single-shot synthesis, yet practical storytelling creation requires multi-shot videos with both strong inter-shot consistency and fine-grained controllability. Existing multi-shot video generation approaches achieve strong consistency but still fall short in controllability. In this paper, we propose Mise-en-Video (MeV), a highly controllable multi-shot video generation framework that allows video creators to conduct staging the multi-shot in the 3D space and then generate the corresponding multi-shot video. To achieve this, our framework combines a hierarchical attention mechanism for multi-level narrative consistency with 3D-aware layout guidance for precise, per-shot spatial control. To support training and evaluation, we develop standardized annotation pipelines and construct a 160K-video dataset with hierarchical multi-shot texts and oriented 3D bounding boxes. Extensive experiments demonstrate that MeV consistently outperforms strong baselines in video quality, inter-shot consistency, and subject-level controllability.

### 🤖 AI 总结

**一句话总结**：Recent advances in text-to-video generation have enabled high-fidelity single-shot synthesis, yet practical storytelling creation requires multi-shot videos with both strong inter-shot consistency and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Mise-en-Video, Fine-Grained, Control, Multi-Shot, Video, Generation, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26801v1) | [下载PDF](https://arxiv.org/pdf/2610.26801v1.pdf)

---

## cs.LG

## [24. Text-to-Image Generative Modeling Without Language Pretraining](https://arxiv.org/abs/2610.26863v1)

**作者**：Keshigeyan Chandrasegaran, Yue Zhao, Armin W. Thomas 等 8 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-10-19

### 📄 论文摘要

Modern text-to-image (T2I) systems use internet-scale language pretraining for text-conditioned image generation. We ask whether language pretraining is necessary for strong T2I generation. We introduce Halcyon, a family of early-fusion multimodal autoregressive models pretrained entirely from scratch on GPIC, a dataset of 100M image-text pairs. Halcyon-0.52B outperforms LlamaGen-XL/8 (48.0 vs. 63.3 gFD) with 18.2$\times$ less pretraining compute. Further, Halcyon-1.6B outperforms JiT-T2I-XXL/8++ (35.3 vs. 41.0 gFD) with 275$\times$ less pretraining compute. Controlled experiments show that text-only pretraining does not improve T2I generation. Halcyon also learns image captioning by replacing caption dropout with I2T supervision, maintaining competitive T2I generation quality under the same pretraining budget. We show that strong T2I systems can be trained from scratch without internet-scale language pretraining. Code and models are available at https://cs.stanford.edu/~keshik/halcyon

### 🤖 AI 总结

**一句话总结**：Modern text-to-image (T2I) systems use internet-scale language pretraining for text-conditioned image generation. We ask whether language pretraining is necessary for strong T2I generation. We introdu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：T2I, Text-to-Image, Generative, Modeling, Without, Language, Pretraining, Modern

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26863v1) | [下载PDF](https://arxiv.org/pdf/2610.26863v1.pdf)

---

## [25. Kronecker Delta Rule for Long Context Linear Attention](https://arxiv.org/abs/2610.26834v1)

**作者**：Anamaria-Roberta Hartl, Levente Zólyomi, Michael List 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-19

### 📄 论文摘要

We propose KronLSTM, a linear attention architecture based on the Kronecker Delta Rule, a novel update rule for associative matrix memories. KronLSTM extends the xLSTM family with a memory-revision mechanism that corrects targeted associations while modifying the memory only along a single direction in matrix space. This minimally invasive memory revision reduces interference with previously stored information compared with delta-rule updates, making it particularly well suited for long-context language modeling. The resulting memory dynamics can be mathematically described as a Markov chain that converges to a steady-state distribution, while the expected norm of the memory matrix remains uniformly bounded throughout the entire input sequence. Hence, KronLSTM ensures stable memory dynamics without requiring additional normalization and stabilization mechanisms for the memory state. Experiments show that KronLSTM is competitive with, and often outperforms, existing linear attention architectures, including models of the (Gated) DeltaNet family, with particularly strong performance on long context benchmarks. These results establish the Kronecker Delta Rule as an effective and analytically tractable foundation for stable associative memory in recurrent linear attention architectures. Our code (https://github.com/NX-AI/KronLSTM) and models (https://huggingface.co/collections/NX-AI/kronlstm) are open-source.

### 🤖 AI 总结

**一句话总结**：We propose KronLSTM, a linear attention architecture based on the Kronecker Delta Rule, a novel update rule for associative matrix memories. KronLSTM extends the xLSTM family with a memory-revision me...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Kronecker, Delta, Rule, Long, Context, Linear, Attention

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26834v1) | [下载PDF](https://arxiv.org/pdf/2610.26834v1.pdf)

---

## [26. Next Best Action: Causal Constrained Offline RL for Business Action Targeting](https://arxiv.org/abs/2610.26817v1)

**作者**：Surya Ramachandiran, Yiming Li, Juan Mancilla-Caceres 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.IR, math.OC  
**发布时间**：2026-10-19

### 📄 论文摘要

Next Best Action (NBA) systems must select among customer interventions (e.g., discounts, promotions, and lifecycle actions), maximize long-term economic value, satisfy complex operational constraints, and remain causally grounded. Existing approaches lack a rigorous framework for meeting these requirements jointly. We address this gap by formulating NBA as a Constrained Markov Decision Process (CMDP). We then integrate off-policy causal correction of the estimated customer dynamics directly into the Linear Programming (LP) formulation of the CMDP. The resulting policy selects actions based on customer states to maximize long-term value while explicitly enforcing business guardrails. Furthermore, the LP formulation yields shadow prices that quantify the economic trade-offs of operational constraints (e.g., fairness and user welfare), enhancing policy interpretability. We validate our proposed offline Reinforcement Learning (RL) framework on an industry case study involving rideshare coupon targeting, where customer states are defined by Recency, Frequency, and Monetary (RFM) stages. We evaluate performance using model-based off-policy evaluation, with causal dynamics estimated from a temporal holdout. Under the observed coupon budget and RFM state representation, our optimized policy improves customer lifetime value (LTV) by 19% over the estimated behavior policy and 8% over a myopic baseline. Although the demonstrated action space is binary, the proposed framework is action-agnostic, yielding a general-purpose decision module for targeting systems that manage multiple interventions.

### 🤖 AI 总结

**一句话总结**：Next Best Action (NBA) systems must select among customer interventions (e.g., discounts, promotions, and lifecycle actions), maximize long-term economic value, satisfy complex operational constraints...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Next, Best, Action, Causal, Constrained, Offline, Business

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26817v1) | [下载PDF](https://arxiv.org/pdf/2610.26817v1.pdf)

---

## [27. Scaling Parameter-Efficient Fine-Tuning for Brain Encoding](https://arxiv.org/abs/2610.26802v1)

**作者**：Zhuofan Josh Ying, Guanglong Sun, Nolan Ho 等 9 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-19

### 📄 论文摘要

Brain encoding models aim to predict neural responses to stimuli. The most widely used approach fits readouts from frozen pretrained backbones. Using neural data to train large models from scratch or fully fine-tune them after task-pretraining has proven difficult because neural data is costly and limited. We show that parameter-efficient fine-tuning (PEFT) enables us to effectively adapt very large pretrained backbones for brain encoding with a small number of trainable parameters. To make it computationally practical, we exploit the backbone's causal structure to predict multiple timepoints in a single pass instead of using sliding windows, significantly reducing feature-extraction cost. This enables efficient fine-tuning of multimodal backbones with up to 104B parameters, the largest model adapted for brain encoding to our knowledge. Trained with a low-rank adapter (LoRA) and a lightweight readout, our approach consistently improves brain encoding performance across nine diverse multimodal backbones. On the same Qwen3-Omni backbone as the prior state-of-the-art (SoTA), our method BrainLoRA achieves the best published performance on the Algonauts 2025 Challenge. We also show the adapted multimodal backbones remain interpretable: modality attribution recovers the canonical sensory topography that prior work often obtains by construction from separate unimodal encoders, and neural adaptation increases the contribution of audio inputs and cross-modal mixing within the backbone. To scale out the number of adapted models, we develop a multi-LoRA kernel that accelerates joint training of multiple LoRAs on a shared backbone. This enables an ensemble of 200+ adapted models that ranks first on the public Algonauts post-challenge leaderboard at the time of writing. Together, our results highlight PEFT as an efficient and powerful paradigm for brain encoding.

### 🤖 AI 总结

**一句话总结**：Brain encoding models aim to predict neural responses to stimuli. The most widely used approach fits readouts from frozen pretrained backbones. Using neural data to train large models from scratch or ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Scaling, Parameter-Efficient, Fine-Tuning, Brain, Encoding, models, aim, predict

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26802v1) | [下载PDF](https://arxiv.org/pdf/2610.26802v1.pdf)

---

## [28. Learning to Refer: Inference-Time Collaboration in Decentralized Federated Learning](https://arxiv.org/abs/2610.26800v1)

**作者**：Yuheng Ma, Chendi Wang, Qiong Zhang  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-10-19

### 📄 论文摘要

In decentralized federated learning, heterogeneous clients may develop complementary expertise, yet each query is typically evaluated only by the client where it arrives. To exploit this distributed expertise without global coordination, we formulate inference-time collaboration as budgeted local expert referral, a graph-constrained routing process in which a query can move only between neighboring clients and only visited clients contribute to its final prediction. EdgeDRM implements this framework by learning a density-based routing potential for each client: differences between neighboring potentials provide the comparisons used to select successive referrals, while local task models generate predictions that are aggregated along the resulting route. Both training and inference are decentralized, using only neighbor-local information without a central router or graph-wide client scoring. We establish estimation guarantees for the learned comparisons and characterize how local improvement and graph structure govern prior-weighted density gains from referral. Experiments on benchmark and real-world medical data show that EdgeDRM outperforms graph-matched decentralized baselines in most settings, with the clearest benefits under sparse connectivity.

### 🤖 AI 总结

**一句话总结**：In decentralized federated learning, heterogeneous clients may develop complementary expertise, yet each query is typically evaluated only by the client where it arrives. To exploit this distributed e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Refer, Inference-Time, Collaboration, Decentralized, Federated, heterogeneous, clients

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26800v1) | [下载PDF](https://arxiv.org/pdf/2610.26800v1.pdf)

---

## [29. On Data Scaling in Tabular ML: More Data, Better Generalization?](https://arxiv.org/abs/2610.26794v1)

**作者**：Ivan Rubachev, Nikita Lazarev, Artem Babenko  
**分类**：cs.LG  
**发布时间**：2026-10-19

### 📄 论文摘要

Recent work in tabular machine learning has emphasized the importance of diverse and realistic evaluation settings. The niche of large-scale (1M+) data, however, remains under-explored. To study training-data scaling, we assemble eight real-world tabular datasets with up to around ten million training examples, retaining the natural distribution shifts of the tasks and using random-split evaluation as a control. We find that GBDTs and MLP-based models show broadly similar scaling trends, with gains from both additional training data and algorithmic improvements. Tabular foundation models show more varied scaling behavior, with recent versions benefiting more consistently from larger contexts even under distribution shift. However, scaling training data under distribution shift introduces new challenges: in-distribution and out-of-distribution performance mostly improve together at smaller scales but can diverge at larger scales. We examine this through MLP capacity sweeps and comparisons of the validation distributions used for tuning and early stopping in MLPs and GBDTs. We also compare common practices of using validation data, contrasting its use for model selection in MLP pipelines with using it for in-context fitting in tabular foundation model pipelines. Under stronger shifts, MLPs selected using validation representative of the evaluation conditions generally maintain or improve performance as training data grows. In contrast, including such examples in context improves foundation-model performance, but does not prevent deterioration with increasing training size in our experiments.

### 🤖 AI 总结

**一句话总结**：Recent work in tabular machine learning has emphasized the importance of diverse and realistic evaluation settings. The niche of large-scale (1M+) data, however, remains under-explored. To study train...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ML, Data, Scaling, Tabular, More, Better, Generalization?, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26794v1) | [下载PDF](https://arxiv.org/pdf/2610.26794v1.pdf)

---

## [30. Training with ML-labeled Data via Stochastic First- and Zeroth-Order Optimization](https://arxiv.org/abs/2610.26790v1)

**作者**：Maria-Eleni Sfyraki, Jun-Kun Wang  
**分类**：cs.LG, math.OC  
**发布时间**：2026-10-19

### 📄 论文摘要

Training a machine learning (ML) model is an optimization process that typically requires a set of examples with ground-truth labels beforehand. Obtaining these ground truths usually requires laborious human effort and can be costly. The scalability of human labeling becomes a concern when there are a large number of data points that need to be labeled. To address this practical issue, we consider an optimization setting where a subset of samples has ground-truth labels, while the remaining data points were labeled by an ML predictor, which could potentially assign incorrect labels to those points. We propose both first-order and zeroth-order stochastic optimization methods for training on datasets consisting of a mix of true-labeled and ML-labeled samples. We further conduct comprehensive empirical studies from training a linear regression model to fine-tuning a large language model (LLM) to showcase the effectiveness of the proposed algorithms for training with ML-labeled data.

### 🤖 AI 总结

**一句话总结**：Training a machine learning (ML) model is an optimization process that typically requires a set of examples with ground-truth labels beforehand. Obtaining these ground truths usually requires laboriou...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Training, ML-labeled, Data, via, Stochastic, First, Zeroth-Order, Optimization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.26790v1) | [下载PDF](https://arxiv.org/pdf/2610.26790v1.pdf)

---

