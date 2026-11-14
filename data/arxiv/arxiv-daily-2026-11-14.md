# arXiv AI 论文日报 | 2026-11-14

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (2 篇)
- [cs.LG](#csLG) (11 篇)
- [cs.CV](#csCV) (10 篇)
- [cs.AI](#csAI) (7 篇)

---

## cs.AI

## [1. AgentSSL: Can MLE Agents Leverage Unlabeled Data?](https://arxiv.org/abs/2611.17323v1)

**作者**：Ethan Lin, Akanksha Sarkar, Ziang Liu 等 5 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-11-12

### 📄 论文摘要

Applying machine learning systems to new domains introduces bottlenecks in both labeled data acquisition and manual pipeline engineering. While recent MLE agents show promise in automating pipeline design, they have been studied almost exclusively in fully supervised settings, leaving them untested in realistic regimes where labeled data is scarce but unlabeled data is abundant. In this work, we introduce Agentic Semi-Supervised Learning (AgentSSL), framing SSL as a program search problem and studying how agents navigate this space under limited supervision. We find that even under weak feedback and matched compute, agents can synthesize code that combines and adapts established SSL techniques, exceeding the strongest human-engineered baselines in 8 of 12 settings by up to +21.8%. However, our results identify program selection as a critical bottleneck in AgentSSL, where performance drops by as much as 47% when selecting based on the agent's feedback metric. To systematically study this bottleneck, we introduce ProgramSelectBench, a large-scale benchmark with a combined total of 16,977 agent-generated and human-engineered SSL programs, and evaluate both unsupervised and active program selection methods. We further evaluate AgentSSL on real-world ecology detection tasks, highlighting the opportunities and challenges of transferring agent-discovered strategies beyond controlled benchmarks.

### 🤖 AI 总结

**一句话总结**：Applying machine learning systems to new domains introduces bottlenecks in both labeled data acquisition and manual pipeline engineering. While recent MLE agents show promise in automating pipeline de...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, AgentSSL, Can, MLE, Leverage, Unlabeled, Data?, Applying

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17323v1) | [下载PDF](https://arxiv.org/pdf/2611.17323v1.pdf)

---

## [2. Classical Energies Learn to Reason 1,000x Faster than Looped Models](https://arxiv.org/abs/2611.17309v1)

**作者**：Benjamin Hoover, Hugh Blayney, James C. R. Whittington  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-11-12

### 📄 论文摘要

Looped models have emerged as a prominent paradigm for reasoning, with successes on simple reasoning puzzles such as Sudoku-Extreme and Maze-Unique. However, these models can be unstable, slow to train, and use many parameters and FLOPs to solve simple puzzles. Descent on an energy not only mitigates these issues but also offers advantages: built-in early stopping, compute that adapts to problem difficulty, fast training without differentiating through a solver, and interpretable weights that learn the constraints of the puzzle. Here we demonstrate this with a learned version of Hopfield & Tank's energy from the 80s, which we term CRAM, solves 99.996% of Sudoku-Extreme and 100% of Maze-Unique test puzzles after 42 ms and 132 ms of training on one GPU, at least 1,000x faster than looped models on these tasks. CRAM also matches baseline looped models at their highest accuracy on Sudoku-Extreme using at least 282x fewer inference FLOPs. Our work suggests two things. First, that energies are an extremely promising direction for training reasoning from data. Second, a caution against using trivially solvable benchmarks like Sudoku and Maze to test the scalability of looped reasoning techniques.

### 🤖 AI 总结

**一句话总结**：Looped models have emerged as a prominent paradigm for reasoning, with successes on simple reasoning puzzles such as Sudoku-Extreme and Maze-Unique. However, these models can be unstable, slow to trai...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：000x, Classical, Energies, Learn, Reason, Faster, than, Looped

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17309v1) | [下载PDF](https://arxiv.org/pdf/2611.17309v1.pdf)

---

## [3. LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds](https://arxiv.org/abs/2611.17267v1)

**作者**：Pengcheng Zhou, Xuanyu Liu, Yanchen Yin 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-12

### 📄 论文摘要

We introduce GeoWorld, a controllable and continuously evolving geographic environment platform for LLM agents, and LiveGeo, a benchmark for evaluating reliable decision-making in real-world geographic environments using GeoWorld. Unlike existing evaluations that largely reason and plan over fixed geographic states, GeoWorld is grounded in real-world geographic structure and allows external world states to evolve along their own temporal processes while preserving verifiable state histories. LiveGeo places geographic tasks within this evolving environment, requiring agents to actively acquire task-relevant information, verify whether the evidence supporting prior decisions remains valid, and revise their plans when necessary. Our results reveal that even frontier LLMs struggle with static tasks, with no model consistently excelling across tasks, while strong static performance does not ensure dynamic reliability. Further analysis identifies a key bottleneck: agents struggle to acquire and translate relevant evidence into valid decisions and maintain their correctness as the world evolves. By releasing LiveGeo together with its GeoWorld platform, we aim to provide the community with a flexible and extensible infrastructure for studying the next generation of agents capable of reliable action in evolving geographic worlds.

### 🤖 AI 总结

**一句话总结**：We introduce GeoWorld, a controllable and continuously evolving geographic environment platform for LLM agents, and LiveGeo, a benchmark for evaluating reliable decision-making in real-world geographi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, We, LiveGeo, Benchmarking, Geographic, Continuously, Evolving, Worlds

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17267v1) | [下载PDF](https://arxiv.org/pdf/2611.17267v1.pdf)

---

## [4. Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery](https://arxiv.org/abs/2611.17241v1)

**作者**：Samidha Verma, Ankit Anand, Sayan Ranu  
**分类**：cs.AI  
**发布时间**：2026-11-12

### 📄 论文摘要

Modern automated heuristic discovery (AHD) systems increasingly rival hand-crafted heuristics by leveraging Large Language Models (LLMs) to iteratively mutate and refine solutions. A natural assumption is that more powerful and more expensive models consistently yield better heuristics. We challenge this empirically: across multiple NP-hard combinatorial optimization problems, we find no consistent advantage for larger, costlier models. This raises a deeper question: given a pool of LLMs spanning frontier and freely hosted or open-weight models, how should one adaptively select which model to invoke at each step of the search? The challenge is non-trivial. The optimal LLM may shift over the course of a run, and because one LLM's output seeds the context for subsequent calls, each model's reward signal is non-stationary and entangled across the heuristic population, thus violating the independence assumptions of classical online decision-making settings. We address this through Ballad (Bandit-based LLM Routing for Automated Heuristic Discovery), an online bandit algorithm that learns to orchestrate a pool of LLMs into an ensemble that matches or exceeds what any soloist LLM achieves alone. This orchestration is powered by an LLM selection policy that favors rare, high-scoring heuristics over stable averages, a DAG-based credit propagation mechanism through the genealogy of the heuristic population, and discounting of stale observations to remain attuned to each model's current utility. Across five NP-hard combinatorial optimization problems and a pool of four models of varying capability and cost, Ballad not only matches the best individual LLM in hindsight but, in several cases, surpasses every individual model while reducing API cost by up to 65.6% relative to always using the strongest model.

### 🤖 AI 总结

**一句话总结**：Modern automated heuristic discovery (AHD) systems increasingly rival hand-crafted heuristics by leveraging Large Language Models (LLMs) to iteratively mutate and refine solutions. A natural assumptio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Ballad, Bandit-Based, Routing, Automated, Heuristic, Discovery, Modern

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17241v1) | [下载PDF](https://arxiv.org/pdf/2611.17241v1.pdf)

---

## [5. Al-Ghasali: A Computational Framework for Simulating Islamic Jurisprudential Rulings via Finite State Automata and Large Language Models](https://arxiv.org/abs/2611.17235v1)

**作者**：Elnaserledinellah Mahmoud Abdelwahab  
**分类**：cs.AI, cs.FL  
**发布时间**：2026-11-12

### 📄 论文摘要

This paper presents Al Ghasali, a computational framework designed to formalize and simulate Islamic jurisprudential (Fiqh) rulings. Building upon recent set theoretic formalizations of al sabr wa al Taqsim that extract minimal operational rules as simple Horn clause logical programs, this work proves that the semantics of closed Fiqh chapters collapse completely to deterministic Finite State Automata (FSA). We establish a formal computational hierarchy, demonstrating that restricting formalization to finite propositional Horn theories guarantees decidability and constant time (O(1)) verdict extraction after offline compilation. The framework formally proves that hierarchical compositions of sub-chapter FSAs preserve this O(1) complexity, and that temporal juristic requirements, such as Tartib (order), are deterministically flattened into static ontological states, preserving the memoryless property of the automaton. To generate human-readable juristic summaries, Al Ghasali incorporates Large Language Models (LLMs) via an architecture where the deterministic FSA strictly controls the probabilistic LLM. Crucially, the paper formulates sufficient design safety conditions for this FSA LLM integration, ensuring strict adherence to the epistemological boundaries of Usul al Fiqh. To neutralize the risk of LLM hallucination, the system employs a Grammar Guided Constrained Decoding mechanism. We formally define the mapping function that dynamically constructs unambiguous right linear grammars from the FSA execution history. The paper mathematically proves that this architecture, augmented by a Bounded Neutral Lexicon and Valence Locking, guarantees the absolute absence of Decisional Hallucination, Juristic Factual Hallucination, and Semantic Inversion reducing the LLM to a pure linguistic transformer of deterministic juristic facts

### 🤖 AI 总结

**一句话总结**：This paper presents Al Ghasali, a computational framework designed to formalize and simulate Islamic jurisprudential (Fiqh) rulings. Building upon recent set theoretic formalizations of al sabr wa al ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Al-Ghasali, Computational, Framework, Simulating, Islamic, Jurisprudential, Rulings, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17235v1) | [下载PDF](https://arxiv.org/pdf/2611.17235v1.pdf)

---

## [6. Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents](https://arxiv.org/abs/2611.17167v1)

**作者**：Haochen Liu, Qianhao Zhu, Zixuan Wang 等 10 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-11-12

### 📄 论文摘要

Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has studied them mainly as actors, judging their usefulness by how well they act. We ask whether a decision model that acts poorly can still teach well. We compare three decision models and three general LLMs as actors and judges on ALFWorld, and use JEV as a teacher on ALFWorld and WebShop. As actors, all six models are pulled away from a subgoal that must come first by an easier one. As judges that see the whole trajectory, the same models credit the steps toward that subgoal, and asking whether each action helped, rather than whether the task will succeed, separates useful from useless actions. As a teacher, JEV raises a Qwen2.5-1.5B policy over GRPO from 72.8% to 82.9% success on ALFWorld and from 56.8% to 71.4% on WebShop. These results suggest that a poor actor can still teach well, because judging an action after the episode ends reveals the consequences that acting must anticipate. Code is available at https://github.com/ZJU-REAL/decision-agents.

### 🤖 AI 总结

**一句话总结**：Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：or, Actor, Judge, Teacher?, Understanding, Decision, Models, Long-Horizon

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17167v1) | [下载PDF](https://arxiv.org/pdf/2611.17167v1.pdf)

---

## [7. Cited but Unused: Parametric Provenance in Retrieval-Augmented Generation](https://arxiv.org/abs/2611.17161v1)

**作者**：Tanzeel Abbas, Tehseen Zia, David Windridge  
**分类**：cs.AI  
**发布时间**：2026-11-12

### 📄 论文摘要

Retrieval-augmented generation systems attach citations to attribute claims to their sources. These citations frequently misstate provenance, and standard verification cannot detect this. We measure provenance by counterfactual value substitution: a fact in the retrieved passages is replaced with a false variant and the model re-queried. We find that across five sizes of one model family and a second comparator family, 1.2% to 15.7% of citable claims derive from parametric memory rather than the retrieved context. At the most conservative substitution distance these figures are 4.6% and 8.5% on the two models we tested at it, with the rate rising with model size within a family. We further find that natural language inference verification, the standard approach, gives results indistinguishable from chance across models, even when restricted to the cited passage. We determine that the cause is structural: a model answering from memory selects a citation that agrees with its output. Comparing ten attribution methods on identical claims, the contrast between the model's distribution with and without context best separates provenance. Acting on that signal does not improve provenance honesty at these base rates. The resulting detector is hence still not accurate enough to act on: it measures what the model knew rather than what it used, and separating those remains the open problem.

### 🤖 AI 总结

**一句话总结**：Retrieval-augmented generation systems attach citations to attribute claims to their sources. These citations frequently misstate provenance, and standard verification cannot detect this. We measure p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Cited, but, Unused, Parametric, Provenance, Retrieval-Augmented, Generation, systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17161v1) | [下载PDF](https://arxiv.org/pdf/2611.17161v1.pdf)

---

## cs.CL

## [8. ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research](https://arxiv.org/abs/2611.17332v1)

**作者**：Jie Wang, Tong Zhu, JiaHao Kuang 等 11 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-11-12

### 📄 论文摘要

Model architecture shapes the scaling behavior, training efficiency, and inference cost of LLMs, making it a central focus of both industry and academia. In industry, teams such as those behind DeepSeek, Qwen, and Kimi routinely introduce architectural innovations, yet public reports rarely document which ideas succeeded, which were abandoned, and why. In academia, limited compute and inconsistent baselines often restrict evaluations to small-scale, single-point comparisons, making it difficult to establish whether improvements hold at larger scales or translate into broader impact. ArchSpace addresses both gaps as a public platform for Recording, Reviewing, and Referencing Architecture Researc}: each proposal is recorded with its experiments and reasoning, reviewed by the community, and referenced by later work. To evaluate ideas before costly large-scale training, ArchSpace leverages scaling laws to predict model loss at larger scales from smaller experiments, a practice widely adopted in industry. We provide initial references that make the platform usable: Qwen3.5 and OLMo3 baselines, fitted scaling laws, and a reusable training recipe. Ideas validated through this review can in turn become new baselines, and ArchSpace thereby aims to broaden the range of ideas that shape the next generation of models.

### 🤖 AI 总结

**一句话总结**：Model architecture shapes the scaling behavior, training efficiency, and inference cost of LLMs, making it a central focus of both industry and academia. In industry, teams such as those behind DeepSe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, ArchSpace, Recording, Reviewing, Referencing, Architecture, Research, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17332v1) | [下载PDF](https://arxiv.org/pdf/2611.17332v1.pdf)

---

## [9. Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs](https://arxiv.org/abs/2611.17280v1)

**作者**：Gautam Galada, Supreeth Shastri, Sagnik Ray Choudhury  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-11-12

### 📄 论文摘要

We propose Synthesis Smuggling, a novel threat model in which an adversarial LLM infers sensitive information about a user from routine assistance-seeking interactions and steganographically encodes that into innocuous-looking model-generated content. The user may then unknowingly transmit that information by sharing the generated artifact, say as an email, social-media post, or message, through ordinary communication channels. An adversary monitoring these channels can discover this information. We demonstrate this threat by training two open-weight models to infer gender and age-group labels from conversational cues and encode their predictions using invisible characters or word choices. These results show that user-shared model outputs can become a covert channel for personal inferences, even when the model itself has no direct means of contacting an adversary.

### 🤖 AI 总结

**一句话总结**：We propose Synthesis Smuggling, a novel threat model in which an adversarial LLM infers sensitive information about a user from routine assistance-seeking interactions and steganographically encodes t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Synthesis, Smuggling, Maliciously, Hiding, Inferred, Personal, Attributes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17280v1) | [下载PDF](https://arxiv.org/pdf/2611.17280v1.pdf)

---

## cs.CV

## [10. K2V: Generative Keyframing For Physically Plausible Video Generation](https://arxiv.org/abs/2611.17324v1)

**作者**：Felix O'Mahony, Daniel Olmeda Reino, Roberto Cipolla 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-12

### 📄 论文摘要

Video diffusion models are able to generate samples with high-quality appearance and textural qualities. However, content produced by these methods is known to exhibit significant physical errors. This is because, in a classical video generation setting, all physical reasoning must take place simultaneously and exclusively within the diffusion process.We propose to resolve these issues by redistributing the task of physical reasoning onto a language model-backed keyframe generation module, which allows for explicit reasoning in language, and fine-grained control over the appearance of the video at important moments in the video. We then condition a video generation model with these keyframes, reducing the role of the diffusion model to the simpler task of interpolating between physically-correct intermediate states, rather than inferring an entire sequence with diffusion. Results demonstrate that our approach significantly outperforms existing approaches, achieving state-of-the-art performance on the Physics-IQ Verified benchmark and PhyGenBench.

### 🤖 AI 总结

**一句话总结**：Video diffusion models are able to generate samples with high-quality appearance and textural qualities. However, content produced by these methods is known to exhibit significant physical errors. Thi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：K2V, Diffusion, Generative, Keyframing, Physically, Plausible, Video, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17324v1) | [下载PDF](https://arxiv.org/pdf/2611.17324v1.pdf)

---

## [11. BrickFlow: Connectivity-Guided Brick Reconstruction](https://arxiv.org/abs/2611.17321v1)

**作者**：Peter Kulits, Cordelia Schmid  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-11-12

### 📄 论文摘要

Given a set of LEGO parts and an image of an assembled object, our task is to infer the pose of each part to assemble the object. In contrast with traditional 3D reconstruction, doing so requires satisfying discrete physical constraints, which provide structure but render the problem combinatorial and highly sensitive to small pose errors. To learn a prior over how parts fit together, we train a set-conditioned SE(3) flow model on procedurally generated assemblies. We then finetune this model to inject image conditioning, using 1% as much data. However, while the learned flow captures global structure, it does not enforce connectivity. To address this, we introduce an analytic connectivity-field guidance to pull predictions toward connected assemblies at test time. Through this, we demonstrate improved build quality with model size, pretraining, and guidance. We make our models and data available for research purposes at https://kulits.github.io/BrickFlow/

### 🤖 AI 总结

**一句话总结**：Given a set of LEGO parts and an image of an assembled object, our task is to infer the pose of each part to assemble the object. In contrast with traditional 3D reconstruction, doing so requires sati...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, BrickFlow, Connectivity-Guided, Brick, Reconstruction, Given, set, LEGO

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17321v1) | [下载PDF](https://arxiv.org/pdf/2611.17321v1.pdf)

---

## [12. Spatial Foundry: A Multimodal Dataset for Spatial Intelligence](https://arxiv.org/abs/2611.17318v1)

**作者**：Ethan Lin, Yang Song  
**分类**：cs.CV  
**发布时间**：2026-11-12

### 📄 论文摘要

Spatial intelligence requires connecting visual observations to the geometry, objects, and persistent state of an environment. Images alone leave these relationships implicit, while disconnected annotations make it difficult to study appearance, camera motion, and scene changes under a common reference. We introduce Spatial Foundry, a collection of 5,280 furnished residential 3D scene configurations with editable assets and aligned visual, geometric, and temporal data. Its modalities include floor plans, perspective and panoramic RGB, metric depth, point clouds, meshes, instance-level 3D bounding boxes, and camera trajectories paired with video. Shared scene coordinates link observations across views and time; editable source scenes enable additional camera paths and controlled object changes. We describe the data representation and construction workflow, and discuss applications in floor-plan-conditioned 3D generation, geometric reconstruction, instance-level perception, camera-conditioned video generation, shared world modeling, and scene editing. Controlled camera and scene variations support spatial perception and world-model research. The public project page provides videos and an interactive colored point-cloud preview.

### 🤖 AI 总结

**一句话总结**：Spatial intelligence requires connecting visual observations to the geometry, objects, and persistent state of an environment. Images alone leave these relationships implicit, while disconnected annot...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Spatial, Foundry, Multimodal, Dataset, Intelligence, requires, connecting, visual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17318v1) | [下载PDF](https://arxiv.org/pdf/2611.17318v1.pdf)

---

## [13. FLEX-LBP: Learning Local Binary Patterns with Exact Binary Inference for Texture Classification](https://arxiv.org/abs/2611.17302v1)

**作者**：Mohamed Alimoussa, Amal El Kaid  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-12

### 📄 论文摘要

Local Binary Patterns (LBP) remain among the most widely used texture descriptors, from industrial inspection to medical imaging. Yet their radius, sampling angles, color transform and thresholds are fixed by hand for each dataset. We present FLEX-LBP, which learns these parameters by backpropagation while every forward pass computes exact binary codes and hard histogram counts. A straight-through estimator acts only in the backward pass, so the deployed descriptor is an interpretable hard-binary LBP with 90 learnable parameters and unchanged inference cost. In a controlled ablation on six color texture benchmarks, the component worth learning is dataset-dependent. One configuration, applied unchanged everywhere, learns the geometry and thresholds with the color transform frozen. It improves the nearest-neighbor accuracy of the identical fixed descriptor by 3.55 points on average over five seeds, significantly on five of six benchmarks and never significantly worse. With a linear discriminant readout, it gains 0.9 points; the fully learned descriptor gains 2.7 and has the highest mean. FLEX-LBP is more accurate than five classical LBP-family descriptors, PCANet and a neural LBP on five of six benchmarks. Its mean nearest-neighbor accuracy exceeds that of frozen ImageNet ResNet-50 features (23.5 million parameters). On the Kather colorectal cancer histology benchmark, the fully learned descriptor reaches 93.8%, significantly above the best classical descriptor (Completed LBP, 92.8%). The learned radii adapt in directions that recur across seeds. Noise drowns single-pixel comparisons and illuminant change flips inter-channel ones; median sampling or gray-world normalization restores 96-97%. The code is available as a drop-in PyTorch layer at https://github.com/medalimoussa/FLEX-LBP.

### 🤖 AI 总结

**一句话总结**：Local Binary Patterns (LBP) remain among the most widely used texture descriptors, from industrial inspection to medical imaging. Yet their radius, sampling angles, color transform and thresholds are ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FLEX-LBP, Learning, Local, Binary, Patterns, Exact, Inference, Texture

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17302v1) | [下载PDF](https://arxiv.org/pdf/2611.17302v1.pdf)

---

## [14. Consistent Video-to-Video Translation via Explicit Correspondences](https://arxiv.org/abs/2611.17298v1)

**作者**：Gaurav Parmar, Zhengqi Li, Richard Zhang 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.GR, cs.LG  
**发布时间**：2026-11-12

### 📄 论文摘要

Interactive video-to-video applications require real-time generation while maintaining long-range temporal consistency. However, recent methods achieve speed by restricting attention to a fixed-length causal window. This limits long-range consistency whenever relevant history falls outside the context window. To address this limitation, we introduce vid2vid-long, a correspondence-based approach grounded in a simple observation. Video-to-video translation provides an explicit cross-frame reference: the regions that match in the input video should match in the output video too. Concretely, we compute patch-level correspondences in the input, guiding retrieval of previously generated outputs in the corresponding regions, and condition the model on these patches through correspondence cross-attention. Our experiments demonstrate that vid2vid-long consistently improves long-range temporal consistency across recent video models while preserving generation quality and real-time performance.

### 🤖 AI 总结

**一句话总结**：Interactive video-to-video applications require real-time generation while maintaining long-range temporal consistency. However, recent methods achieve speed by restricting attention to a fixed-length...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Consistent, Video-to-Video, Translation, via, Explicit, Correspondences, Interactive, applications

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17298v1) | [下载PDF](https://arxiv.org/pdf/2611.17298v1.pdf)

---

## [15. MALNISI-Infused Graph Construction and Weighted Contrastive Loss based GAT for Unsupervised Representation Learning in HSI](https://arxiv.org/abs/2611.17199v1)

**作者**：Soumi Sarkar, Subhadip Boral, Sarbani Palit 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-12

### 📄 论文摘要

Hyperspectral images (HSI) possess discriminating spectral characteristics with respect to land utilization due to high-dimensional information. Recently, unsupervised representation learning using graph neural networks has unveiled these utilization-specific complex spectral relations. This article has three main contributions. First, it proposes an index, the Mean Absolute Local Neighborhood Inverse Spectral Index (MALNISI), which measures the similarity between two pixels based on their neighborhood information. The index is used to construct a weighted adjacency matrix, giving the HSI a graph structure. Second, it proposes an upgraded Graph Attention Network that learns compact latent representations of hyperspectral data from the constructed graph. In this network, an enhanced multi-head attention mechanism incorporates the MALNISI weights as an auxiliary feature to emphasize learned attention between neighboring pixels. To alleviate over-smoothing and preserve fine-grained spectral details, the architecture integrates residual connections, skip projections, and feature normalization, which together enhance representation capability, stabilize learning, and accelerate convergence. Third, it proposes a weighted contrastive loss function that incorporates neighborhood-aware MALNISI between connected pixels, encouraging strongly connected pixels in the high-dimensional space to remain close in the latent space, and weakly connected pixels to stay apart. The resulting discriminative low-dimensional embeddings are then clustered using spectral clustering. Experimental analysis on six benchmark HSI datasets demonstrates the efficiency and necessity of the three aforementioned contributions, and the comparative study highlights superior performance over fourteen state-of-the-art approaches.

### 🤖 AI 总结

**一句话总结**：Hyperspectral images (HSI) possess discriminating spectral characteristics with respect to land utilization due to high-dimensional information. Recently, unsupervised representation learning using gr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MALNISI-Infused, Graph, Construction, Weighted, Contrastive, Loss, GAT, Unsupervised

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17199v1) | [下载PDF](https://arxiv.org/pdf/2611.17199v1.pdf)

---

## [16. eDMD: Endpoint Distribution Matching for Few-Step Diffusion Distillation](https://arxiv.org/abs/2611.17194v1)

**作者**：Tong Zhao, Xianfang Zeng, Yucheng Han 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-12

### 📄 论文摘要

Distribution matching distillation (DMD) has emerged as a leading paradigm for distilling diffusion models into few-step students, where an auxiliary fake score model tracks the student's distribution and the discrepancy between the teacher and fake predictions drives the student toward the teacher. In multi-step distillation, although only the student's final output is delivered, existing methods train the fake model on intermediate states or across all denoising steps. Consequently, the student's update signal becomes entangled with intermediate distributions, which can distort the matching direction and remain nonzero even after the student's final outputs already match the teacher distribution. To resolve this mismatch, we propose Endpoint Distribution Matching Distillation (eDMD), which trains a single shared fake model exclusively on the student's final outputs and uses it to correct every denoising step. Our theoretical analysis proves that this endpoint reference guarantees that the distribution matching term vanishes if and only if the student's final output distribution matches the teacher's, regardless of intermediate distributions. Beyond the fake reference, we further strengthen teacher supervision through a precise teacher (PT) that replaces single-step guided predictions with short multi-step trajectories on the final noise interval, paired with a calibrated query density for intermediate steps. Experiments on SD3-Medium, FLUX.2-klein (4B and 9B), and Qwen-Image-2.1 demonstrate that eDMD consistently outperforms existing distribution matching methods for 4-step generation.

### 🤖 AI 总结

**一句话总结**：Distribution matching distillation (DMD) has emerged as a leading paradigm for distilling diffusion models into few-step students, where an auxiliary fake score model tracks the student's distribution...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, eDMD, Endpoint, Distribution, Matching, Few-Step, Distillation, DMD

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17194v1) | [下载PDF](https://arxiv.org/pdf/2611.17194v1.pdf)

---

## [17. Consensus Capture in Reference-Based UAV Video Stabilization: A Benchmark on Dynamic Urban Scenes](https://arxiv.org/abs/2611.17190v1)

**作者**：Robert Fonod, Nikolas Geroliminis  
**分类**：cs.CV  
**发布时间**：2026-11-12

### 📄 论文摘要

Reference-frame stabilization registers every frame of a hovering-drone video onto one reference frame, keeping object positions comparable. The registration pipelines it relies on are selected on feature-matching benchmarks in which only the camera moves. Over a busy intersection, vehicles moving together supply mutually consistent correspondences that can draw the robust homography estimate toward their motion: consensus capture, which inlier statistics cannot flag. A two-part benchmark measures it and the object masking meant to prevent it. A static protocol scores ten pipelines under exactly known homographies on 4K aerial frames, tuned on a site-disjoint split at a matched resolution and feature budget. A dynamic protocol scores them at an offline and a real-time budget on hovers selected from the video alone to span the amount and coherence of moving foreground, plus a stationary control. It measures background alignment, object position error and the share of a moving group's displacement an estimate follows, against a pseudo-ground-truth reference audited with manually annotated ground control points, which also score every candidate. On static scenes, tuned AKAZE, RootSIFT, SIFT and BRISK lead, retuning the matcher thresholds raises the mean average accuracy (mAA) by at most 0.0062, and masking costs less than 0.005. Unmasked ORB is captured on 28 of 304 real-time dynamic pairs and on 6 offline; its real-time captured estimates have a median corner error of 18.8 px yet typical inlier counts and ratios. Masking removes capture for every pipeline and leaves the leading pipelines unchanged. Code, data and results are released.

### 🤖 AI 总结

**一句话总结**：Reference-frame stabilization registers every frame of a hovering-drone video onto one reference frame, keeping object positions comparable. The registration pipelines it relies on are selected on fea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Consensus, Capture, Reference-Based, UAV, Video, Stabilization, Benchmark, Dynamic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17190v1) | [下载PDF](https://arxiv.org/pdf/2611.17190v1.pdf)

---

## [18. Validation-Guided Prompt Selection for Differential Morphing Attack Detection](https://arxiv.org/abs/2611.17176v1)

**作者**：Raghavendra Ramachandra, Hailin Li  
**分类**：cs.CV  
**发布时间**：2026-11-12

### 📄 论文摘要

Differential morphing attack detection (D-MAD) compares a trusted live capture with a document image that may contain a facial morph. We investigate whether labelled validation data can improve a frozen-parameter vision-language evaluator through prompt selection rather than model fine-tuning. Version~1 generates 50 candidate prompts and selects the top-ranked instruction using a security-oriented loss that prioritises missed morph attacks (MACER) while accounting for bona fide classification errors (BSCER), response failures, parse failures, and decision inconsistency. Version~2 recursively revises prompts using aggregate validation feedback. On a subject-disjoint test set of 160 pairs spanning LMA, MIPGAN-2, and PIPE, the selected Version~1 prompt achieves a (19.17\%) morph attack classification error rate (MACER), with (0.00\%) observed bona fide sample classification error rate (BSCER), compared with (70.00\%) MACER for a controlled manual prompt. The paired (50.83) percentage-point difference has a (95\%) subject-bootstrap interval of ([43.33,58.33]). Recursive revision does not surpass the best Generation~0 validation loss; the reported revised descendant obtains (31.67\%) test MACER. All 23 attacks missed by Version~1 are landmark-based (LMA) morphs. Overall, the results show that prompt formulation can substantially influence frozen-parameter VLM-based D-MAD performance, while also highlighting the challenge of recursive prompt refinement under a compact 10-subject validation setting.

### 🤖 AI 总结

**一句话总结**：Differential morphing attack detection (D-MAD) compares a trusted live capture with a document image that may contain a facial morph. We investigate whether labelled validation data can improve a froz...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Validation-Guided, Prompt, Selection, Differential, Morphing, Attack, Detection, D-MAD

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17176v1) | [下载PDF](https://arxiv.org/pdf/2611.17176v1.pdf)

---

## [19. SpotDiff: A Plug-and-Play Framework for Zero-Shot Change Detection in Remote Sensing Imagery](https://arxiv.org/abs/2611.17172v1)

**作者**：Anit Upadhyaya, Ata Akbari Asanjan, Chaitanya Jalluri 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-12

### 📄 论文摘要

Remote sensing change detection usually relies on large collections of temporally aligned, pixel-level annotations, which limits its scalability across regions, imaging platforms and application domains. Recent zero-shot approaches reduce the need for supervision, but they often localize fine-grained changes poorly because their features are coarse or inconsistent across time. We present SpotDiff, a training-free, plug-and-play framework for zero-shot change detection built by composing complementary vision foundation models. SpotDiff uses DINOv3 for semantically robust features, AnyUp to reconstruct them at pixel resolution, and SAM 3 for text-guided region-of-interest proposals, which an inference-time multi-scale strategy (SWIMS) makes reliable on small objects. Change is then measured by comparing the reconstructed features of the two dates inside the proposed regions, with no learnable components, fine-tuning or change labels. To our knowledge, SpotDiff is the first change detection method to use a universal feature upsampler, which alone adds 13.8 F1 over bilinear upsampling of the same features. On LEVIR-CD, SpotDiff reaches 82.46 F1, 2.06 points above the strongest prior training-free method, and on the multi-class SECOND benchmark it improves building change detection by 10.3 IoU and the six-class average by 2.2 IoU. Qualitative results on PlanetScope (3 m) and Sentinel-2 (10 m) imagery show that the same pipeline transfers across resolutions without modification. Our results indicate that composing modern foundation models is an effective route to scalable, label-free change detection.

### 🤖 AI 总结

**一句话总结**：Remote sensing change detection usually relies on large collections of temporally aligned, pixel-level annotations, which limits its scalability across regions, imaging platforms and application domai...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SpotDiff, Plug-and-Play, Framework, Zero-Shot, Change, Detection, Remote, Sensing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17172v1) | [下载PDF](https://arxiv.org/pdf/2611.17172v1.pdf)

---

## cs.LG

## [20. Internalizing Investment Mandates: A Neurosymbolic RL Approach to Portfolio Allocation](https://arxiv.org/abs/2611.17329v1)

**作者**：Zeynep Yıldız, Satchit Chatterji, Ercan Atam 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-12

### 📄 论文摘要

Institutional portfolios operate under investment policy statements that specify asset allocation constraints, often conditioned on market regime information. Deep reinforcement learning has been shown to optimize financial performance but typically does not enforce rule compliance, making it unsuitable for real-world deployment. Existing neurosymbolic methods such as Probabilistic Logic Policy Gradient (PLPG) offer constraint-satisfying reinforcement learning (RL) via differentiable symbolic supervision but assume a finite, discrete action space. We present a PLPG-inspired continuous allocation method that estimates the probability that the policy's own executed action satisfies the investment mandate, using reparameterized Monte Carlo sampling, and adds it to the training objective. No post-hoc enforcement mechanism intercepts actions at inference time and compliance is learned by the agent. Audited directly on deterministic mean actions with no correction, the policy reduces violations of a six-rule regime-conditional mandate from 96-98% for unconstrained RL and 33.4% for a reward-penalty baseline to 4.8%, showing that a continuous-action neurosymbolic policy can substantially internalize a symbolic mandate.

### 🤖 AI 总结

**一句话总结**：Institutional portfolios operate under investment policy statements that specify asset allocation constraints, often conditioned on market regime information. Deep reinforcement learning has been show...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Internalizing, Investment, Mandates, Neurosymbolic, Approach, Portfolio, Allocation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17329v1) | [下载PDF](https://arxiv.org/pdf/2611.17329v1.pdf)

---

## [21. Linking Rapid Learning to Compositional Structure in Neural Networks: Evidence from Additive Analogies in Meta-Learned Parameter Spaces](https://arxiv.org/abs/2611.17314v1)

**作者**：Abigail L. Tenenbaum, R. Thomas McCoy  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-11-12

### 📄 论文摘要

Humans can learn rapidly from limited experience, while neural networks typically require extensive training. In this work, we investigate what properties of a neural network can enable it to learn rapidly. We study neural networks that have been optimized via meta-learning, a technique that exposes a network to many related functions to facilitate its subsequent learning of similar functions. Prior work has shown that these meta-learned networks can learn new functions rapidly, but how they do so remains unclear. To investigate their internal structure, we take inspiration from classic work demonstrating additive relationships among the learned vectors that neural networks use to represent words (e.g., "king" minus "man" plus "woman" approximates "queen"). Analogously, we look for additive relationships among a meta-learned network's "representations" of different functions; when a meta-learned network rapidly learns to implement a specific function, all of its adapted parameter values can be concatenated into a single vector that we treat as representing the function. We find that such parameter vectors can be added and subtracted according to symbolic relationships among the functions they represent, yielding new parameter vectors that successfully represent the functions predicted by the corresponding symbolic manipulations: the networks specified by these artificially recombined vectors actually implement the intended functions without any direct training on them. Our results suggest that meta-learning can tune a network's starting point to organize subsequent learning along systematic, functionally meaningful trajectories through the space of possible parameter vectors, providing a geometric basis for realizing inductive biases in neural networks.

### 🤖 AI 总结

**一句话总结**：Humans can learn rapidly from limited experience, while neural networks typically require extensive training. In this work, we investigate what properties of a neural network can enable it to learn ra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Linking, Rapid, Learning, Compositional, Structure, Neural, Networks, Evidence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17314v1) | [下载PDF](https://arxiv.org/pdf/2611.17314v1.pdf)

---

## [22. Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon](https://arxiv.org/abs/2611.17294v1)

**作者**：Haozhe Wang, Lina Chen, Fanqi Wan 等 8 位作者  
**分类**：cs.LG, cs.AI, cs.CL, cs.DC  
**发布时间**：2026-11-12

### 📄 论文摘要

On-device inference requires kernels that make effective use of local accelerators. Efficient training and evaluation of models that generate Apple Metal kernels benefit from native macOS tools and concurrent agent sessions. These sessions alternate between model requests, development commands, and GPU execution, leaving GPU capacity idle for much of a rollout. We present Metal Sandbox, infrastructure that combines restricted per-instance file access, native command execution, and command-level scheduling across interconnected Macs. Each agent retains its workspace and private development environment. Parallel commands can run concurrently, while serial commands share one execution slot per node; eligible waiting commands can migrate to available Macs and return results to the original agent. Integration with Harbor supports task execution, automatic verification, and rollout collection through a common workflow. Controlled experiments on four Mac mini M4 nodes achieve $1.68\times$--$2.05\times$ gains in command throughput under concentrated demand. Sixteen static agent traces give an estimated $2.14\times$ sustained-throughput gain for four sessions per node versus one, assuming continuously replenished sessions and unchanged mean durations. Replaying these measured traces under dynamic scheduling reduces mean tool waiting by 18.8% and batch elapsed time by 22.3%, assuming unchanged phase durations. Metal Sandbox and its Harbor integration are open-source on GitHub.

### 🤖 AI 总结

**一句话总结**：On-device inference requires kernels that make effective use of local accelerators. Efficient training and evaluation of models that generate Apple Metal kernels benefit from native macOS tools and co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Metal, Sandbox, Isolated, Execution, Command, Scheduling, GPU, Coding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17294v1) | [下载PDF](https://arxiv.org/pdf/2611.17294v1.pdf)

---

## [23. Negative-Only Policy Optimization for One-Sided Verifiable Rewards](https://arxiv.org/abs/2611.17287v1)

**作者**：Jiacheng Xu, Shuo He, Fuxiang Zhang 等 5 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-11-12

### 📄 论文摘要

Reinforcement learning with verifiable rewards (RLVR) typically relies on a verifier that can reliably judge whether sampled solutions are correct. However, in many realistic settings, complete verification is generally unavailable, while cheap checks can only falsify failures. We formalize this regime as one-sided verifiability (OSV): verified negatives are reliable counterexamples, but verified positives are merely non-falsified candidates and may contain many false positives. This asymmetry makes standard RLVR unreliable, because reinforcing verified positives can directly reward shortcuts that pass partial checks. To address this issue, we propose Negative-Only Policy Optimization (NOPO), which treats verified positives as unlabeled and updates the policy only by suppressing trusted verified negatives. Specifically, NOPO combines a reference-relative negative suppression loss with a group-level adapter that scales each update by the proportion of non-falsified responses. Across unit-test, constraint-check, and LLM self-verifiers, NOPO improves pass@k over baselines on code, logic, and math benchmarks when oracle rewards are unavailable. These gains persist under inference-time scaling and cross-benchmark transfer.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning with verifiable rewards (RLVR) typically relies on a verifier that can reliably judge whether sampled solutions are correct. However, in many realistic settings, complete verifi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Negative-Only, Policy, Optimization, One-Sided, Verifiable, Rewards, Reinforcement, learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17287v1) | [下载PDF](https://arxiv.org/pdf/2611.17287v1.pdf)

---

## [24. Two mathematical models of knowledge distillation](https://arxiv.org/abs/2611.17230v1)

**作者**：Audrey Xie, Ludwig Schmidt, John Duchi  
**分类**：cs.LG  
**发布时间**：2026-11-12

### 📄 论文摘要

Many hypotheses compete to explain the successes of knowledge distillation. To help address this, we propose and analyze a mathematical model of distillation, which suggests that distillation's performance comes not from obtaining better models but from easier to optimize landscapes. For generalized linear models trained with stochastic gradient descent, we prove that distillation fits performant student models asymptotically more quickly than non-distilled models. In rank-1 matrix approximation, we characterize conditions on the target matrix under which gradient descent with distillation converges strictly faster than training on the supervised objective. The theory helps delineate the ways distillation provides benefits (i.e., in optimization speed, not in generalization), and experiments on real datasets corroborate the theoretical predictions.

### 🤖 AI 总结

**一句话总结**：Many hypotheses compete to explain the successes of knowledge distillation. To help address this, we propose and analyze a mathematical model of distillation, which suggests that distillation's perfor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Two, mathematical, models, knowledge, distillation, Many, hypotheses

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17230v1) | [下载PDF](https://arxiv.org/pdf/2611.17230v1.pdf)

---

## [25. Physically Interpretable Basin Selection in Discrete-Variable Origami Design](https://arxiv.org/abs/2611.17196v1)

**作者**：Lucy Liu, Leon M. Kamp, Katia Bertoldi 等 4 位作者  
**分类**：cs.LG, cond-mat.mtrl-sci, cond-mat.soft  
**发布时间**：2026-11-12

### 📄 论文摘要

Automatic differentiation has enabled rapid progress on continuous-variable mechanical design problems, but gradient-based optimization still struggles with discrete variables. The standard approach is to optimize using a continuous relaxation of the choices, then commit to the nearest discrete design at the end. Why this procedure selects unfavorable basins is poorly understood. Here, we introduce a practical, interpretable design problem inspired by origami, in which automatic differentiation is used to design shapes with a target functional behavior. Each origami sheet has a fixed geometry, and a bilevel optimization framework tunes which one of four discrete hinge types to place at each fold. Baseline gradient-based design settles into basins with a large discretization gap: relaxed optimization solves 97% of runs, but the final, discrete solutions succeed only half the time. We find that the gap can be relieved with a surprisingly simple modification. An initialization prior uniformly biased toward the stiff, flat hinge option boosts the final solve fraction from 49% to 69%. Applying the prior adds no additional compute and leaves the optimization process unchanged. Compared to the baseline, sheets produced with the prior have greater geometric compatibility and mechanical stiffness. Directly penalizing frustration and floppiness in the outer loss function produces an even greater improvement than the prior does, raising the solve fraction to 78% and indicating that these properties help distinguish the unfavorable basins. Our results demonstrate that loss landscapes for mechanical design can have physically meaningful basins that are not robust to discretization and cause solves to fail. Targeting these basins' physical signatures, even with just an initialization bias, helps avoid them.

### 🤖 AI 总结

**一句话总结**：Automatic differentiation has enabled rapid progress on continuous-variable mechanical design problems, but gradient-based optimization still struggles with discrete variables. The standard approach i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Physically, Interpretable, Basin, Selection, Discrete-Variable, Origami, Design, Automatic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17196v1) | [下载PDF](https://arxiv.org/pdf/2611.17196v1.pdf)

---

## [26. Maximizing Capacity Utilization of LoRA Adapters for Mitigating the Learning-Forgetting Trade-off](https://arxiv.org/abs/2611.17191v1)

**作者**：Tomohiro Sawada, Kartik Goyal  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-11-12

### 📄 论文摘要

Low-Rank Adaptation (LoRA) often underperforms full fine-tuning, especially in heterogeneous and continual-learning settings in which substantial forgetting occurs. In general, it suffers from an undesirable learning-forgetting trade-off across diverse fine-tuning settings. We identify a potential contributor: LoRA adapters, especially high-rank ones, frequently fail to realize the available capacity afforded by the configured rank. Specifically, we find that standard LoRA updates have effective rank far below their configured rank, limiting how broadly the update energy is distributed. Therefore, we propose training mechanisms that optimize the original objective while maximizing adapter effective rank. Our main method adds a simple, stable, differentiable, and SVD-free Rényi-2 effective-rank regularizer to the language-modeling loss. We also connect capacity maximization to norm-bounded updates. In mixed-domain rank sweeps on three models evaluated with multiple random seeds, a penalty weight of $λ=0.01$ lowers mean Wiki perplexity at every tested rank of at least $16$ relative to unpenalized LoRA. Mean training perplexity improves or increases by at most $0.02$ in all but one model-rank comparison. Single-task and scheduling experiments further show that the balance between learning and retention depends on the configuration. We also observe that several LoRA variants in the literature also suffer from the identified capacity issue, and our approach provides a complementary axis of improvement to LoRA-based parameter-efficient fine-tuning. These results suggest that effective rank is not only a post-hoc diagnostic of adapter quality, but a trainable objective for improving the learning-forgetting frontier. Our code is available at https://github.com/tomohiro-sawada/lora-capacity-utilization

### 🤖 AI 总结

**一句话总结**：Low-Rank Adaptation (LoRA) often underperforms full fine-tuning, especially in heterogeneous and continual-learning settings in which substantial forgetting occurs. In general, it suffers from an unde...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Maximizing, Capacity, Utilization, LoRA, Adapters, Mitigating, Learning-Forgetting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17191v1) | [下载PDF](https://arxiv.org/pdf/2611.17191v1.pdf)

---

## [27. Symmetry in Time: A Representation Theory of Linear Recurrent Memory](https://arxiv.org/abs/2611.17162v1)

**作者**：Anif N. Shikder, Ramit Dey, Jan Minac 等 4 位作者  
**分类**：cs.LG, cs.NE, math.RT  
**发布时间**：2026-11-12

### 📄 论文摘要

State space models (SSMs) are an emerging alternative to Transformers. SSMs offer linear-time inference and parallel training, but most implementations make the parallel scan efficient by making the recurrence diagonal: each channel of the hidden state is multiplied by an input-dependent real or complex number. These numbers commute, so the state records which inputs occurred but not their order. We formalize this with representation theory, which explains and fixes the state-tracking failures previously reported for SSMs. The state update defines a linear representation of the monoid of input sequences, and we show that an SSM tracks a group at every sequence length exactly when that group is a quotient of the group generated by its transition matrices. Two consequences follow. Diagonal real- and complex-valued SSMs can track only commutative groups, while the transition matrices of any SSM that can track a group must split into independent blocks over the real, complex, and quaternion numbers. We then introduce HyperSSM, which adds quaternion channels while keeping linear-time inference and parallel training. Trained only on final answers, HyperSSM solves the group tasks of recent state-tracking benchmarks exactly with at most five state numbers. This includes $S_5$ with 32 generators, where previous SSMs are at chance, and HyperSSM generalizes to sequences 25 times longer than those seen in training. Because the theory says what the transitions must encode, the learned weights of the linear recurrence can be interpreted directly. We demonstrate this by recovering the calibration of a real gyroscope, the rotations of imperfect qubit gates and the geometry of protein backbones.

### 🤖 AI 总结

**一句话总结**：State space models (SSMs) are an emerging alternative to Transformers. SSMs offer linear-time inference and parallel training, but most implementations make the parallel scan efficient by making the r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Symmetry, Time, Representation, Theory, Linear, Recurrent, Memory

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17162v1) | [下载PDF](https://arxiv.org/pdf/2611.17162v1.pdf)

---

## [28. Enhancing Preference Detection using Eye Movement Cascade and Multilayer Combinatorial Fusion](https://arxiv.org/abs/2611.17145v1)

**作者**：Yuanhong Wu, Mary Tsaryk, Sam Watson 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-12

### 📄 论文摘要

Understanding how visual attention influences human preference formation is a fundamental problem in consumer behavior and cognitive science. In this work, we investigate how eye movement patterns can be used to predict preference decisions when subjects compare two alternatives. To address this problem, we analyze an eye-tracking dataset, where subjects view pairs of face images and their gaze behavior is recorded throughout the decision process. We model this problem using multiple machine learning classifiers and apply the Multi-layer Combinatorial Fusion (MCF) framework to iteratively combine diverse models. The MCF framework expands models to a large pool of model fusions and then reduces them based on cognitive diversity, repeating this process across layers until diversity diminishes. Experimental results show that MCF significantly improves performance over individual models. The best single model achieves a Pre@k of 0.90, which is improved to 0.9143 after the first layer of MCF, and further increased to 0.9286 in the second layer. This progression demonstrates that the second layer not only surpasses the performance of the first layer but also outperforms the best individual model, highlighting the effectiveness of leveraging diversity through multi-layer fusion.

### 🤖 AI 总结

**一句话总结**：Understanding how visual attention influences human preference formation is a fundamental problem in consumer behavior and cognitive science. In this work, we investigate how eye movement patterns can...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Enhancing, Preference, Detection, Eye, Movement, Cascade, Multilayer, Combinatorial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17145v1) | [下载PDF](https://arxiv.org/pdf/2611.17145v1.pdf)

---

## [29. A Convex-Analytic Reformulation for Poisoning Attacks on Logistic Regression](https://arxiv.org/abs/2611.17143v1)

**作者**：Carina Moreira Costa, Maria Eduarda Pinheiro, Martin Schmidt  
**分类**：cs.LG, math.OC  
**发布时间**：2026-11-12

### 📄 论文摘要

We study data poisoning attacks on logistic regression with $\ell_2$-regularization, where an attacker chooses the features of a fixed number of injected observations with prescribed labels to maximize the logistic loss on the clean training data. Strong convexity of the defender's problem yields an exact reformulation through its first-order optimality conditions. Using convex conjugacy of the softplus function, we replace the sigmoid relations by a single convex optimality-gap inequality and express the attacker's objective as a concave function. A change of variables makes the stationarity condition affine, leaving bounded bilinear equalities as the only nonconvex constraints. We derive finite bounds on all variables involved in these equalities, including a global bound on the coefficient norm and tighter bounds obtained by preprocessing based on convex optimization. Experiments on eight binary classification datasets evaluate attack effectiveness and compare the two reformulations when solved with \textsf{SCIP}. Attacks obtained by local optimization degrade predictive performance on most datasets, while the convex-analytic formulation produces substantially stronger reported dual bounds within a fixed time limit.

### 🤖 AI 总结

**一句话总结**：We study data poisoning attacks on logistic regression with $\ell_2$-regularization, where an attacker chooses the features of a fixed number of injected observations with prescribed labels to maximiz...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Convex-Analytic, Reformulation, Poisoning, Attacks, Logistic, Regression, study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17143v1) | [下载PDF](https://arxiv.org/pdf/2611.17143v1.pdf)

---

## [30. Support-Constrained Offline Policy Improvement for Pediatric ECMO from Limited Clinical Data](https://arxiv.org/abs/2611.17134v1)

**作者**：Fateme Golivand Darvishvand, Saurabh Mathur, Nikhilesh Prabhakar 等 9 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-12

### 📄 论文摘要

Managing children on ECMO (Extracorporeal Membrane Oxygenation) requires balancing short-term physiological stability with the long-term goal of preventing neurological injury. Standard reinforcement learning can propose risky, out-of-distribution actions, while imitation learning is limited to reproducing clinician behavior. We introduce Support-Constrained Fitted Q-Iteration (FQI-SC), an offline reinforcement learning framework that cautiously improves upon expert behavior by restricting optimization to empirically supported state-action pairs and defaulting to the clinician baseline in low-data regions. On 78 pediatric trajectories totaling over 6,000 hours of clinical data, we evaluate our framework using Fitted Q-Evaluation (FQE) and a behavioral disagreement. Additionally, we formalize the performance-safety trade-off by introducing a unified Balance Score ($S(π)$). Our empirical evaluation shows that support-constrained policy improves the Balance Score by 38\% relative to FQI, improves estimated value by 1.28 FQE units over imitation learning, and reduces disagreement with clinician actions by 71\% relative to FQI.

### 🤖 AI 总结

**一句话总结**：Managing children on ECMO (Extracorporeal Membrane Oxygenation) requires balancing short-term physiological stability with the long-term goal of preventing neurological injury. Standard reinforcement ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Support-Constrained, Offline, Policy, Improvement, Pediatric, ECMO, Limited, Clinical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.17134v1) | [下载PDF](https://arxiv.org/pdf/2611.17134v1.pdf)

---

