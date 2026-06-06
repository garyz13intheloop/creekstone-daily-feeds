# arXiv AI 论文日报 | 2026-06-06

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (11 篇)
- [cs.CV](#csCV) (8 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.CL](#csCL) (5 篇)

---

## cs.AI

## [1. MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery](https://arxiv.org/abs/2606.06473v1)

**作者**：Shangheng Du, Xiangchao Yan, Jinxin Shi 等 14 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-06-04

### 📄 论文摘要

Large language model (LLM) agents are increasingly applied to long-horizon tasks such as scientific discovery and machine learning engineering (MLE), where sustained self-evolution becomes a key capability. However, existing MLE agents suffer from inter-branch information isolation, memoryless search, and lack of hierarchical control, which together hinder long-horizon optimization. We present MLEvolve, an LLM-based self-evolving multi-agent framework for end-to-end machine learning algorithm discovery. By extending tree search to Progressive MCGS, MLEvolve enables cross-branch information flow through graph-based reference edges and gradually shifts the search from broad exploration to focused exploitation with an entropy-inspired progressive schedule. To allow the agent to evolve with accumulated experience, we introduce Retrospective Memory, which combines a cold-start domain knowledge base with a dynamic global memory for task-specific experience retrieval and reuse. For stable long-horizon iteration, we further decouple strategic planning from code generation with adaptive coding modes. Evaluation on MLE-Bench shows that MLEvolve achieves state-of-the-art performance across multiple dimensions including average medal rate and valid submission rate under a 12-hour budget (half the standard runtime). Moreover, MLEvolve also outperforms specialized algorithm discovery methods including AlphaEvolve on mathematical algorithm optimization tasks, demonstrating strong cross-domain generalization. Our code is available at https://github.com/InternScience/MLEvolve.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM) agents are increasingly applied to long-horizon tasks such as scientific discovery and machine learning engineering (MLE), where sustained self-evolution becomes a key capab...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MLEvolve, Self-Evolving, Framework, Automated, Machine, Learning, Algorithm, Discovery

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06473v1) | [下载PDF](https://arxiv.org/pdf/2606.06473v1.pdf)

---

## [2. Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement](https://arxiv.org/abs/2606.06468v1)

**作者**：Jui-Hui Chung, Ziyang Cai, Zihao Li 等 17 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-04

### 📄 论文摘要

We introduce Goedel-Architect, an agentic framework for formal theorem proving in Lean 4 centered on blueprint generation and refinement. A blueprint is a dependency graph of definitions and lemmas that builds up to the main theorem. First, Goedel-Architect generates a blueprint of formally stated definitions and lemmas, along with declared dependencies. This blueprint is optionally guided by a natural language proof. Then, a tool-equipped Lean prover component closes each open lemma node in parallel using relevant dependencies. Failed lemmas in turn drive refinement of the global blueprint. This strategy contrasts with other mainstream approaches which use recursive lemma decomposition, and can inefficiently loop on dead-end strategies. Using the open-weight DeepSeek-V4-Flash (284B-A13B) as the backbone, Goedel-Architect attains 99.2% pass@1 on MiniF2F-test and 75.6% pass@1 on PutnamBench. With an optional natural-language proof seeding the initial blueprint on the harder problems, we additionally close the remaining two MiniF2F-test problems (reaching 100%), lift PutnamBench to 88.8% (597/672), and solve 4/6 on IMO 2025, 11/12 on Putnam 2025, and 3/6 on USAMO 2026. This represents state-of-the-art performance for an open-source pipeline at a price point up to 500x less than comparable open-source pipelines.

### 🤖 AI 总结

**一句话总结**：We introduce Goedel-Architect, an agentic framework for formal theorem proving in Lean 4 centered on blueprint generation and refinement. A blueprint is a dependency graph of definitions and lemmas th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Goedel-Architect, Streamlining, Formal, Theorem, Proving, Blueprint, Generation, Refinement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06468v1) | [下载PDF](https://arxiv.org/pdf/2606.06468v1.pdf)

---

## [3. Benchmark Everything Everywhere All at Once](https://arxiv.org/abs/2606.06462v1)

**作者**：Shiyun Xiong, Dongming Wu, Peiwen Sun 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-04

### 📄 论文摘要

Benchmarks are fundamental for evaluating and advancing LLMs and MLLMs by providing standardized and explicit measures of performance. However, their construction is labor-intensive and hard to reuse, raising concerns about sustainability and scalability. Moreover, existing benchmarks often quickly reach performance saturation after their release, resulting in insufficient discrimination among state-of-the-art models. To address these challenges, we introduce Benchmark Agent, a fully autonomous agentic system designed for benchmark building. Our framework orchestrates the complete benchmark construction pipeline, from user query analysis and subtask design to data annotation and quality control. To assess Benchmark Agent, we implement it to produce 15 representative benchmarks, spanning diverse evaluation scenarios, including text understanding, multimodal understanding, and domain-specific reasoning. Extensive experiments, including human evaluation, LLM-as-a-judge assessment, and consistency checks, demonstrate Benchmark Agent can generate high-quality benchmark samples with minimal human involvement. More importantly, through continual evaluation, we observe several insightful findings, including that current models struggle with certain domain-specific reasoning tasks. We believe that rapidly evolving benchmarks can contribute significantly to the research community. The preview and code will be publicly available at the demo page and code repository.

### 🤖 AI 总结

**一句话总结**：Benchmarks are fundamental for evaluating and advancing LLMs and MLLMs by providing standardized and explicit measures of performance. However, their construction is labor-intensive and hard to reuse,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Benchmark, Everything, Everywhere, All, Once, Benchmarks, fundamental

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06462v1) | [下载PDF](https://arxiv.org/pdf/2606.06462v1.pdf)

---

## [4. Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents](https://arxiv.org/abs/2606.06453v1)

**作者**：Zhuoming Chen, Xinrui Zhong, Qilong Feng 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-04

### 📄 论文摘要

Sparse attention is becoming increasingly important for serving large language models (LLMs) as generation lengths continue to grow. However, deploying and evaluating new sparse attention algorithms at scale remains highly engineering-intensive, slowing both human researchers and AI agents in exploring the sparse attention design. To address this challenge, we present Vortex, a system that combines a Python-embedded frontend language atop a page-centric tensor abstraction for expressing a broad range of sparse attention algorithms, with an efficient backend tightly integrated into modern LLM serving stacks. Vortex enables rapid prototyping, deployment, and evaluation of sparse attention algorithms, effectively translating their theoretical efficiency gains into real-world throughput improvements. As a result, Vortex substantially accelerates the design and iteration of sparse attention algorithms. First, AI agents use Vortex to automatically generate and refine diverse algorithms, the best reaching up to $3.46\times$ higher throughput than full attention while preserving accuracy. Second, Vortex extends sparse attention to emerging architectures and very large models that are otherwise hard to experiment with, reaching up to $4.7\times$ higher throughput on the MLA-based GLM-4.7-Flash and $1.37\times$ on the 229B-parameter MiniMax-M2.7 on NVIDIA B200 GPUs.

### 🤖 AI 总结

**一句话总结**：Sparse attention is becoming increasingly important for serving large language models (LLMs) as generation lengths continue to grow. However, deploying and evaluating new sparse attention algorithms a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Vortex, Efficient, Programmable, Sparse, Attention, Serving, becoming

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06453v1) | [下载PDF](https://arxiv.org/pdf/2606.06453v1.pdf)

---

## [5. Risk Assessment of Autonomous Driving: Integrating Technical Failures, Ethical Dilemmas, and Policy Frameworks](https://arxiv.org/abs/2606.06396v1)

**作者**：Boyi Chen, Shengqin Chu, Zicheng Wang 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-04

### 📄 论文摘要

Autonomous driving technology has the potential to reduce the large number of road traffic accidents caused by human error each year, but it also brings new types of risks that need to be evaluated from the aspects of technology, ethics and regulations. Based on public crash data from the National Highway Traffic Safety Administration (NHTSA), disengagement reports from the California Department of Motor Vehicles (DMV), the MIT Moral Machines dataset, and a comparative regulatory analysis of five jurisdictions, we have found that the main types of technical failure modes are perception and classification errors. These account for a relatively large proportion of the reported accidents, and it can be concluded that there are different ethical frameworks for autonomous vehicle decision-making, and inconsistent regulations in different areas increase the uncertainty of widespread application. Generally speaking, the problems of technology, ethics and regulation are closely related and need to be solved together. Therefore, this paper recommends a more adaptive and cooperative governance approach that combines engineering standards, ethical discussion, and institutional supervision.

### 🤖 AI 总结

**一句话总结**：Autonomous driving technology has the potential to reduce the large number of road traffic accidents caused by human error each year, but it also brings new types of risks that need to be evaluated fr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Risk, Assessment, Autonomous, Driving, Integrating, Technical, Failures

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06396v1) | [下载PDF](https://arxiv.org/pdf/2606.06396v1.pdf)

---

## [6. Humans' ALMANAC: A Human Collaboration Dataset of Action-Level Mental Model Annotations for Agent Collaboration](https://arxiv.org/abs/2606.06388v1)

**作者**：Jiaju Chen, Yuxuan Lu, Jiayi Su 等 13 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-06-04

### 📄 论文摘要

Recent advances in LLM agents have enabled complex cognitive capabilities, such as multi-step reasoning, planning, and tool use, that increasingly position these agents as human collaborators. Effective collaboration, however, requires collaborators to continuously maintain and align mental models of their own reasoning,partners' intentions, and shared goals during the collaborative process. Today's agents rarely develop such capabilities since they are primarily optimized for task completion, and the community lacks authentic human collaboration data with action-level mental model annotations that could guide agents toward process-level collaborative competence. To bridge this gap, we present ALMANAC, a dataset of Action-Level Mental model ANnotations for Agent Collaboration built from the Map Task, a classic dyadic routing task from social science. ALMANAC contains 2,987 collaboration actions, each paired with theory-informed mental model annotations that record the participants' self-reasoning, perceived partner intent, and perceived team goal. We benchmark six LLMs on predicting humans' next-turn behavior and mental models. Our results demonstrate ALMANAC's utility in evaluating models' ability to simulate human collaborative behaviors and infer their underlying mental models.

### 🤖 AI 总结

**一句话总结**：Recent advances in LLM agents have enabled complex cognitive capabilities, such as multi-step reasoning, planning, and tool use, that increasingly position these agents as human collaborators. Effecti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Humans', ALMANAC, Human, Collaboration, Dataset, Action-Level, Mental

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06388v1) | [下载PDF](https://arxiv.org/pdf/2606.06388v1.pdf)

---

## cs.CL

## [7. Revising Context, Shifting Simulated Stance: Auditing LLM-Based Stance Simulation in Online Discussions](https://arxiv.org/abs/2606.06443v1)

**作者**：Xinnong Zhang, Wanting Shan, Hanjia Lyu 等 5 位作者  
**分类**：cs.CL, cs.MM, cs.SI  
**发布时间**：2026-06-04

### 📄 论文摘要

Large language models are increasingly used to simulate social media users and infer how individuals may respond to online discussions. However, it remains unclear whether these simulations reflect precise user-specific beliefs or whether they are highly sensitive to semantically independent changes in conversational contexts. In this work, we study counterfactual context revision as a framework for auditing LLM-based stance simulation. Given an original online conversation, we first infer a target user's stance toward a specific topic. We then apply controlled revision strategies to the conversational context and simulate the user's stance again under the revised context. We compare text-only revision strategies with a multimodal one that incorporates meme-based context and evaluate two main effectiveness metrics, i.e., average directional stance shift and stance transition rate. The results reveal effective and robust stance transitions in both text-only and multimodal strategies across different polarization-preference mechanisms. Our study contributes an evaluation framework for understanding the context sensitivity of LLM-based stance simulation. More broadly, it highlights both the promise and risk of using LLMs to simulate online opinion dynamics.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly used to simulate social media users and infer how individuals may respond to online discussions. However, it remains unclear whether these simulations reflect pr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Revising, Context, Shifting, Simulated, Stance, Auditing, LLM-Based, Simulation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06443v1) | [下载PDF](https://arxiv.org/pdf/2606.06443v1.pdf)

---

## [8. Reinforcement Learning Elicits Contextual Learning of Unseen Language Translation](https://arxiv.org/abs/2606.06428v1)

**作者**：Hanxu Hu, Zdeněk Šnajdr, Pinzhen Chen 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-04

### 📄 论文摘要

Prior work has shown that large language models (LLMs) can translate unseen or low-resource languages by undergoing continued training or even by encoding a grammar book in their context. However, both methods typically overfit specific languages, with limited zero-shot transfer at test time. To translate extremely low-resource languages at scale, we argue that LLMs must acquire the meta-skill of utilizing in-context linguistic knowledge rather than memorizing specific languages. In this paper, we propose a reinforcement learning (RL) approach to unseen language translation given rich linguistic context, using a surface-level translation metric (chrF) as the reward. Empirically, despite the lightweight reward, our RL-trained models effectively extract and apply relevant linguistic information from the provided context, leading to better translations on completely unseen languages than in-context learning or supervised fine-tuning. Our analyses suggest that outcome-based RL can extend beyond conventional reasoning tasks like math and coding to serve as a recipe for language learning from context.

### 🤖 AI 总结

**一句话总结**：Prior work has shown that large language models (LLMs) can translate unseen or low-resource languages by undergoing continued training or even by encoding a grammar book in their context. However, bot...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Reinforcement, Learning, Elicits, Contextual, Unseen, Language, Translation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06428v1) | [下载PDF](https://arxiv.org/pdf/2606.06428v1.pdf)

---

## [9. A Komi-Yazva--Russian Parallel Corpus and Evaluation Protocol for Zero- and Few-Shot LLM Translation](https://arxiv.org/abs/2606.06420v1)

**作者**：Petr Parshakov  
**分类**：cs.CL  
**发布时间**：2026-06-04

### 📄 论文摘要

We present the first Komi-Yazva--Russian parallel corpus together with an explicit evaluation protocol for studying LLM translation in an endangered, extremely low-resource setting. The dataset contains 457 aligned sentence pairs from 74 narrative texts and is accompanied by documented provenance, sentence-level alignment, and story identifiers that enable leakage-aware evaluation. We use this setup to compare modern large language models on Komi-Yazva-to-Russian translation under severe parallel-data scarcity in zero-shot and retrieval-based few-shot regimes. The protocol includes story-level cross-validation, deterministic retrieval for few-shot prompting, strict validation of generated outputs, complementary reference-based and judge-based metrics, and story-level uncertainty estimates. Across models, LLMs produce non-trivial translations, but performance varies strongly by model family and prompting regime. Retrieval-based few-shot prompting consistently improves over zero-shot prompting, while gains beyond a small retrieved context remain limited. The results show that evaluative conclusions in this setting depend materially on metric choice and failure handling, so the paper frames the corpus as both a dataset contribution and a reproducible evaluation testbed for endangered-language machine translation.

### 🤖 AI 总结

**一句话总结**：We present the first Komi-Yazva--Russian parallel corpus together with an explicit evaluation protocol for studying LLM translation in an endangered, extremely low-resource setting. The dataset contai...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Komi-Yazva--Russian, Parallel, Corpus, Evaluation, Protocol, Zero, Few-Shot

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06420v1) | [下载PDF](https://arxiv.org/pdf/2606.06420v1.pdf)

---

## [10. CollabSim: A CSCW-Grounded Methodology for Investigating Collaborative Competence of LLM Agents through Controlled Multi-Agent Experiments](https://arxiv.org/abs/2606.06399v1)

**作者**：Jiaju Chen, Bo Sun, Yuxuan Lu 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-04

### 📄 论文摘要

Multi-agent systems (MAS) built on large language models have shown growing promise, with their effectiveness resting on agents' ability to coordinate through text-based channels much as human teams do. Yet recent study suggests that MAS often falter not because agents lack individual task-solving ability, but because they lack collaborative competence: the capacity to establish common ground, maintain shared task understanding, balance individual and collective incentives, and repair misalignment as interaction unfolds. Decades of research in Computer-Supported Cooperative Work have characterized these requirements for human teams coordinating under constrained communication, yet existing MAS evaluations focus mainly on task outcomes or single-agent proficiency in reasoning, planning, and tool use. To enable a systematic analysis of agents' collaborative competence in MAS, we introduce CollabSim, a configurable simulation framework that combines a theory-grounded definition of collaborative capabilities, controlled manipulation of interaction conditions, and action-level probing of agents' internal states. Experiments across four LLMs show that CollabSim can capture condition effects, separate model performance patterns, and reveal task-dependent effects of agent design.

### 🤖 AI 总结

**一句话总结**：Multi-agent systems (MAS) built on large language models have shown growing promise, with their effectiveness resting on agents' ability to coordinate through text-based channels much as human teams d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, CollabSim, CSCW-Grounded, Methodology, Investigating, Collaborative, Competence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06399v1) | [下载PDF](https://arxiv.org/pdf/2606.06399v1.pdf)

---

## [11. Emergent Language as an Approach to Conscious AI](https://arxiv.org/abs/2606.06380v1)

**作者**：Zengqing Wu, Chuan Xiao  
**分类**：cs.CL, cs.AI, cs.MA, cs.NE  
**发布时间**：2026-06-04

### 📄 论文摘要

The question of whether artificial systems can be conscious remains open, in part because existing approaches either evaluate systems against theory-derived checklists (discriminative) or engineer consciousness-inspired modules directly (architectural); both leave open whether observed structures are artifacts of human language priors. We propose a generative methodology: emergent language (EL) in multi-agent reinforcement learning, where agents start from minimal (no language, no concept of self, minimal exposure to human text) and develop communication under task pressure alone, ensuring causal attributability to task demands rather than inherited human language priors. We position our methodology by discussing how EL serves as a generative tool for studying consciousness-relevant structure, including the role of environment complexity and the interpretation of emergent communication. As a proof of concept, we instantiate this methodology in a minimal environment and show that agents develop self-referential communication, including an echo-mismatch detection circuit that is not predicted by task structure or architecture alone but emerges from a specific environmental affordance.

### 🤖 AI 总结

**一句话总结**：The question of whether artificial systems can be conscious remains open, in part because existing approaches either evaluate systems against theory-derived checklists (discriminative) or engineer con...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, an, of, Emergent, Language, Approach, Conscious, question

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06380v1) | [下载PDF](https://arxiv.org/pdf/2606.06380v1.pdf)

---

## cs.CV

## [12. PAR3D: A Unified 3D-MLLM with Part-Aware Representation for Scene Understanding](https://arxiv.org/abs/2606.06485v1)

**作者**：Shaohui Dai, Yansong Qu, You Shen 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-04

### 📄 论文摘要

Recent advances in 3D multimodal large language models (3D-MLLMs) have enabled unified solutions for 3D scene understanding tasks, including visual question answering, captioning, and referring segmentation. However, existing 3D-MLLMs remain largely object-centric, limiting their ability to model fine-grained part structures that are essential for embodied interaction with 3D environments. In this work, we present PAR3D, a unified part-aware 3D-MLLM framework that enables models to understand, reason about, and ground both objects and their parts in 3D scenes. To enable training and evaluation of part-aware 3D scene understanding, we introduce ScenePart, a synthetic 3D scene dataset with part-level annotations and language instructions. We further develop Part-Aware 3D Representation Learning to enrich 3D visual representations with fine-grained part-level semantics, and propose Hierarchical Segmentation Query Generation to ground part targets via hierarchical object-part queries. Extensive experiments show that our method substantially improves part-level question answering and referring segmentation, while also achieving strong performance across object-level vision-language tasks.

### 🤖 AI 总结

**一句话总结**：Recent advances in 3D multimodal large language models (3D-MLLMs) have enabled unified solutions for 3D scene understanding tasks, including visual question answering, captioning, and referring segmen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PAR3D, Unified, 3D-MLLM, Part-Aware, Representation, Scene, Understanding, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06485v1) | [下载PDF](https://arxiv.org/pdf/2606.06485v1.pdf)

---

## [13. Complexity-Balanced Diffusion Splitting](https://arxiv.org/abs/2606.06477v1)

**作者**：Noam Issachar, Dani Lischinski, Raanan Fattal  
**分类**：cs.CV  
**发布时间**：2026-06-04

### 📄 论文摘要

Standard continuous-time generative models rely on monolithic architectures that must navigate vastly different signal regimes, from isotropic noise to intricate data distributions. While scaling model capacity improves performance, deploying a massive network uniformly across the entire generative timeline is inherently inefficient. In this work, we propose Complexity-Balanced Splitting (CBS), a principled framework for temporal capacity allocation that distributes the generative workload across multiple specialized sub-networks. Grounded in function approximation theory and de Boor's equidistribution principle, CBS partitions the diffusion timeline into segments of equal approximation burden, allocating more representational capacity to regions where the generative dynamics are more difficult to model. To estimate this local complexity, we introduce two complementary and tractable monitor functions: a spatial measure based on the flow's Dirichlet energy, and a geometric measure based on the acceleration of the sampling trajectories. Using a lightweight auxiliary model to estimate these complexity profiles, our approach eliminates the need for heuristic temporal splits or computationally expensive search procedures. Extensive evaluation across multiple architectures (SiT, JiT, and UNet) and datasets demonstrates that CBS consistently improves synthesis quality without increasing per-step inference cost. In particular, CBS improves FID by ~35% on SiT-XL with CFG relative to naive temporal partitioning. Project page is available at https://noamissachar.github.io/CBS/.

### 🤖 AI 总结

**一句话总结**：Standard continuous-time generative models rely on monolithic architectures that must navigate vastly different signal regimes, from isotropic noise to intricate data distributions. While scaling mode...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Complexity-Balanced, Splitting, Standard, continuous-time, generative, models, rely

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06477v1) | [下载PDF](https://arxiv.org/pdf/2606.06477v1.pdf)

---

## [14. Thinking with Imagination: Agentic Visual Spatial Reasoning with World Simulators](https://arxiv.org/abs/2606.06476v1)

**作者**：Chenming Zhu, Jingli Lin, Yilin Long 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-04

### 📄 论文摘要

While Vision-Language Models (VLMs) have shown strong visual reasoning capabilities, their spatial reasoning abilities remain largely constrained to the observed images and text-oriented chain-of-thought. They often struggle to infer unobserved layouts, maintain cross-view consistency, and reason from alternative viewpoints when only limited egocentric observations are available. In this work, we study this problem as thinking with imagination, where a VLM actively acquires imagined visual evidence by interacting with a world simulator during reasoning. We propose Astra, an agentic spatial reasoning framework that empowers VLMs with action-conditioned visual imagination. Specifically, Astra couples Astra-VL, an RL-trained VLM policy, with Astra-WM, a Bagel-based world simulator that generates novel-view observations from context images and natural-language camera motions. To provide reliable imagined evidence, Astra-WM is trained with view consistency tuning to improve pose and content consistency across views. In the RL stage, we propose a world-simulator-in-the-loop two-phase RL curriculum to stabilize tool-use exploration and advance the model's ability to invoke the simulator only when imagined observations improve over direct answering. Experiments demonstrate that both the world simulator and the agentic policy are necessary: Astra-WM improves simulator-augmented Gemini-3-Flash on MMSI-Bench from 45.1 to 49.5, while Astra-VL improves the Qwen3-VL backbone from 29.8 to 38.8 on MMSI-Bench and from 36.8 to 42.7 on MindCube. These results show that imagined observations can provide useful spatial evidence, but effective world-model-augmented reasoning requires learning when, where, and how to imagine.

### 🤖 AI 总结

**一句话总结**：While Vision-Language Models (VLMs) have shown strong visual reasoning capabilities, their spatial reasoning abilities remain largely constrained to the observed images and text-oriented chain-of-thou...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Thinking, Imagination, Agentic, Visual, Spatial, Reasoning, World, Simulators

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06476v1) | [下载PDF](https://arxiv.org/pdf/2606.06476v1.pdf)

---

## [15. A Vision-language Framework for Comparative Reasoning in Radiology](https://arxiv.org/abs/2606.06407v1)

**作者**：Tengfei Zhang, Ziheng Zhao, Lisong Dai 等 8 位作者  
**分类**：cs.CV, cs.IR, cs.LG, eess.IV  
**发布时间**：2026-06-04

### 📄 论文摘要

Medical imaging artificial intelligence has achieved strong performance in isolated image interpretation, but remains poorly aligned with radiological practice, where diagnosis and follow-up rely on comparison across prior studies and analogous reference cases. Here we formulate radiological comparison as an entity-aware cross-image reasoning problem and introduce a framework that supports both reference-case retrieval and temporal comparative interpretation. We construct MedReCo-DB, a large-scale comparative imaging resource derived from routine image-report pairs, comprising more than 690,000 images from over 160,000 patients across eight institutions, four countries and seven imaging modalities. Reports are decomposed into anatomical structures, abnormal findings and pathological conditions to provide supervision for entity-conditioned retrieval and comparative visual question answering. Using this resource, we develop MedReCo, an entity-aware visual encoder for controllable retrieval of clinically analogous cases, and MedReCo-VLM, a vision--language extension for generative interpretation of interval change. Across internal, external and cross-center evaluations, MedReCo achieved the highest Recall@1 in all 12 internal retrieval settings and improved external retrieval by a mean of 6.0 percentage points. In clinically confusable differential groups, it consistently outperformed the strongest baselines. MedReCo-VLM achieved the best performance across all comparative generation evaluations and improved longitudinal follow-up accuracy by 14.5-46.5 percentage points on chest radiographs and 13.0-27.9 percentage points on CT. These findings suggest that entity-aware comparative reasoning can be learned from routine clinical data at scale and may provide a more clinically aligned foundation for medical imaging AI.

### 🤖 AI 总结

**一句话总结**：Medical imaging artificial intelligence has achieved strong performance in isolated image interpretation, but remains poorly aligned with radiological practice, where diagnosis and follow-up rely on c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Vision-language, Framework, Comparative, Reasoning, Radiology, Medical, imaging, artificial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06407v1) | [下载PDF](https://arxiv.org/pdf/2606.06407v1.pdf)

---

## [16. HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes](https://arxiv.org/abs/2606.06390v1)

**作者**：Wenbo Li, Xiaoliang Ju, Zipeng Qin 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-04

### 📄 论文摘要

Indoor scene generation is crucial for robot simulation and modern interior design. However, complex layouts together with scarce 3D scene data make learning-based generation challenging. Existing methods often rely on hand-crafted rules or focus on isolated sub-tasks (e.g., floorplan synthesis or single-room furnishing), producing whole-home scenes that lack global coherence, realism, and simulation readiness. To mitigate these limitations, we propose a unified hierarchical framework that decomposes indoor scene synthesis into controllable stages. First, we curate a large-scale dataset of 300K real residential floorplans to train a large language model for whole-home floorplan generation. With detailed descriptions and a K-D tree-based representation, our method enables fine-grained, controllable whole-home floorplan generation. Building upon the generated whole-home floorplan, we leverage image generation models to draft furniture layouts from multi-level roaming viewpoints, and then generate the layouts of small manipulable objects on different supporting surfaces (e.g., cabinets, desks, and dining tables) for embodied AI simulation. During furniture and object layout generation, a VLM-based refiner iteratively corrects furniture and object placement, and a 3D generative model enables flexible replacement of individual assets. We further attach basic physical attributes and simple surface texture and lighting setups to complete the pipeline for embodied AI use. Experiments and user studies demonstrate that our pipeline produces indoor spaces with greater layout diversity and stronger 3D design appeal, outperforming prior methods on both quantitative and qualitative metrics. Finally, alongside our generation pipeline, we will release the floorplan dataset and 5K fully furnished scenes to the community. Project Page: https://kairos-homeworld.github.io/

### 🤖 AI 总结

**一句话总结**：Indoor scene generation is crucial for robot simulation and modern interior design. However, complex layouts together with scarce 3D scene data make learning-based generation challenging. Existing met...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HomeWorld, Unified, Floorplan-to-Furnished, Framework, Generating, Controllable, Densely, Interactive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06390v1) | [下载PDF](https://arxiv.org/pdf/2606.06390v1.pdf)

---

## [17. Visual Commonsense Driven Knowledge Refinements for Scene Graph Generation](https://arxiv.org/abs/2606.06369v1)

**作者**：Maëlic Neau, Salim Baloch, Jakob Suchan 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-04

### 📄 论文摘要

Learning-driven Scene Graph Generation (SGG) models excel on frequent relation types but degrade sharply under annotation sparsity, failing to capture reliable visual commonsense knowledge. We propose a model-agnostic, semantically-guided knowledge refinement framework that systematically mines commonsense-grounded constraints from training data - capturing spatial, functional, and qualitative relational regularities - and uses general declarative commonsense reasoning to correct and refine ranked SGG predictions at inference time. The framework requires no manual rule authoring, no model retraining, and transfers across datasets and architectures. On three standard benchmarks, we obtain consistent improvements over strong baselines, demonstrating that structured visual commonsense reasoning over deep scene semantics is a practical and effective complement to purely learning-based scene graph generation.

### 🤖 AI 总结

**一句话总结**：Learning-driven Scene Graph Generation (SGG) models excel on frequent relation types but degrade sharply under annotation sparsity, failing to capture reliable visual commonsense knowledge. We propose...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Visual, Commonsense, Driven, Knowledge, Refinements, Scene, Graph, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06369v1) | [下载PDF](https://arxiv.org/pdf/2606.06369v1.pdf)

---

## [18. GMBFormer: An NDVI-Guided Global Memory Bank Transformer for Urban Green-Space Extraction from Ultra-High-Resolution Imagery](https://arxiv.org/abs/2606.06363v1)

**作者**：Hao Lei, Xi Cheng, Chenlu Shu 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-04

### 📄 论文摘要

Urban green-space extraction from ultra-high-resolution (UHR) imagery is commonly performed patch by patch, which limits semantic reuse among spatially separated but visually similar vegetation patterns. Directly injecting the Normalized Difference Vegetation Index (NDVI) into red-green-blue (RGB) backbones can also blur the roles of visual appearance learning and physical vegetation confidence. We propose GMBFormer, a SegFormer-based framework that replaces adjacency-driven feature propagation with selective, similarity-driven prototype retrieval. Only RGB channels enter the backbone and decoder, while NDVI is decoupled as a physics-informed gate that admits high-confidence vegetation descriptors into a compact global memory bank through momentum updates. During training and inference, the current patch queries stored prototypes through memory-mediated cross-attention, and the retrieved response is integrated with bounded overhead. Experiments use a self-constructed Chengdu UHR dataset with 7,700 labeled 512 x 512 patches and two reduced-label settings derived from the public International Society for Photogrammetry and Remote Sensing (ISPRS) Potsdam dataset. Under the same training and evaluation protocol, GMBFormer obtains mean intersection over union (mIoU)/mean Dice (mDice) scores of 89.25%/94.31%, 92.17%/95.92%, and 83.72%/90.86%, respectively, improving the controlled SegFormer-B4 baseline in each setting. Ablation studies indicate that decoupled NDVI admission, memory retrieval, capacity, and momentum jointly shape the final performance.

### 🤖 AI 总结

**一句话总结**：Urban green-space extraction from ultra-high-resolution (UHR) imagery is commonly performed patch by patch, which limits semantic reuse among spatially separated but visually similar vegetation patter...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, GMBFormer, NDVI-Guided, Global, Memory, Bank, Transformer, Urban

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06363v1) | [下载PDF](https://arxiv.org/pdf/2606.06363v1.pdf)

---

## [19. Physics in 2-Steps: Locking Motion Priors Before Visual Refinement Erases Them](https://arxiv.org/abs/2606.06361v1)

**作者**：Woojung Han, Seil Kang, Youngjun Jun 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-04

### 📄 论文摘要

Image-to-Video diffusion models leverage input images to generate visually stunning content, yet frequently produce motion that violates physical laws. We reveal a surprising finding: a 2-step generation often exhibits better physical consistency than a 50-step output from the same model. Through spectral analysis, we trace this to phase erosion during denoising; the phase degrades significantly (dropping by $\approx 18\%$ from step 2 to step 50), whereas the magnitude remains relatively stable. Building on this insight, we propose PhaseLock, a training-free framework that preserves the valid motion priors from few-step inference throughout the denoising trajectory. Rather than relying on full-step inference for physical consistency, PhaseLock extracts a motion prior from just 2 steps and enforces it onto high-fidelity generation via Latent Delta Guidance. Our approach effectively mitigates phase degradation, improving physical consistency by an average of 6.2 points across diverse models while largely maintaining visual fidelity, with negligible overhead ($1.06\times$ time, $1.02\times$ memory) and reduced reliance on expensive external guidance methods ($\sim5\times$ time).

### 🤖 AI 总结

**一句话总结**：Image-to-Video diffusion models leverage input images to generate visually stunning content, yet frequently produce motion that violates physical laws. We reveal a surprising finding: a 2-step generat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Physics, 2-Steps, Locking, Motion, Priors, Before, Visual, Refinement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06361v1) | [下载PDF](https://arxiv.org/pdf/2606.06361v1.pdf)

---

## cs.LG

## [20. TailLoR: Protecting Principal Components in Parameter-Efficient Continual Learning](https://arxiv.org/abs/2606.06494v1)

**作者**：Marius Dragoi, Ioana Pintilie, Alexandra Dragomir 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-04

### 📄 论文摘要

Parameter-efficient finetuning methods based on spectral decomposition have enabled progress in Continual Learning. In this paper we introduce TailLoR, which utilizes the singular bases U and V of the pre-trained weights as a fixed reference frame to learn a low-rank update applied to the singular value matrix. A soft spectral penalty discourages updates aligned with dominant singular directions, reducing interference while routing fine-grained adaptation into the highly flexible, long-tail spectral coordinates.

### 🤖 AI 总结

**一句话总结**：Parameter-efficient finetuning methods based on spectral decomposition have enabled progress in Continual Learning. In this paper we introduce TailLoR, which utilizes the singular bases U and V of the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TailLoR, Protecting, Principal, Components, Parameter-Efficient, Continual, Learning, finetuning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06494v1) | [下载PDF](https://arxiv.org/pdf/2606.06494v1.pdf)

---

## [21. RREDCoT: Segment-Level Reward Redistribution for Reasoning Models](https://arxiv.org/abs/2606.06475v1)

**作者**：Mykyta Ielanskyi, Kajetan Schweighofer, Lukas Aichberger 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-04

### 📄 论文摘要

Recent advancements in reasoning language models have been driven by Reinforcement Learning (RL) fine-tuning. Most often, these rely on the Group Relative Policy Optimization (GRPO) algorithm or modifications thereof to steer the models to produce Chain-of-Thought (CoT) traces. The final answer can only be verified, and the reward assigned, after the CoT trace is complete, making it a delayed reward problem. GRPO and its modifications correspond to Monte Carlo methods in standard RL, which are known to suffer from high variance. A possible solution to this problem is the redistribution of rewards through credit assignment, where segments of the CoT trace that are important for arriving at the desirable solution are emphasized by assigning a higher reward. While Monte Carlo sampling can be used to provide an unbiased estimate of intermediate state values, its computational overhead makes it unsuitable for train-time credit assignment in long contexts at high granularity. We introduce RREDCoT (Reward REDistribution for Chain of Thoughts), which utilizes the model itself to approximate the optimal reward redistribution without additional generation. We investigate the advantages of our method compared to MC sampling and several attribution methods. We further analyze several aspects relevant to the construction of the redistribution such as segmentation of CoT traces and state value estimation.

### 🤖 AI 总结

**一句话总结**：Recent advancements in reasoning language models have been driven by Reinforcement Learning (RL) fine-tuning. Most often, these rely on the Group Relative Policy Optimization (GRPO) algorithm or modif...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RREDCoT, Segment-Level, Reward, Redistribution, Reasoning, Models, Recent, advancements

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06475v1) | [下载PDF](https://arxiv.org/pdf/2606.06475v1.pdf)

---

## [22. PC Layer: Polynomial Weight Preconditioning for Improving LLM Pre-Training](https://arxiv.org/abs/2606.06470v1)

**作者**：Senmiao Wang, Tiantian Fang, Haoran Zhang 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-04

### 📄 论文摘要

We propose a preconditioning (PC) layer, a weight parameterization via polynomial preconditioner that ensures stable weight conditioning throughout LLM training. The PC module reshapes the singular-value spectrum of weight matrices via low-degree polynomial preconditioning. After training, the preconditioned weights can be merged back into the original architecture, incurring no inference overhead. We demonstrate the advantage of the proposed PC layer over standard transformers in Llama-1B pre-training, for both the AdamW and Muon optimizers. Theoretically, we justify this spectrum-control principle by proving that uniformly bounding each layer's singular values ensures geometric convergence of gradient descent to global minima, for certain deep linear networks. Our code is available at https://github.com/Empath-aln/PC-layer.

### 🤖 AI 总结

**一句话总结**：We propose a preconditioning (PC) layer, a weight parameterization via polynomial preconditioner that ensures stable weight conditioning throughout LLM training. The PC module reshapes the singular-va...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PC, LLM, Layer, Polynomial, Weight, Preconditioning, Improving, Pre-Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06470v1) | [下载PDF](https://arxiv.org/pdf/2606.06470v1.pdf)

---

## [23. Event Detection for Parameter-to-KPI Dependency Learning for AI-RAN](https://arxiv.org/abs/2606.06459v1)

**作者**：Christie Djidjev, Nicholas Kaminski  
**分类**：cs.LG  
**发布时间**：2026-06-04

### 📄 论文摘要

Next-generation wireless networks are expected to rely on multiple concurrent AI-driven control functions that optimize different network objectives simultaneously, particularly in AI-integrated and open radio access network architectures such as AI Radio Access Network (AI-RAN) and Open Radio Access Network (O-RAN). When these functions interact, they can interfere with one another in ways that are difficult to detect from raw network data alone. A key missing piece for managing such interactions is a reliable, interpretable dependency structure that captures which control parameters are actively influencing which network performance outcomes at any given time. This paper focuses on the event-detection step needed to support such dependency learning by converting noisy continuous telemetry into binary indicators of parameter activity and KPI response. The central difficulty is that not every fluctuation in the data reflects a genuine control interaction, so the method must distinguish real parameter-outcome relationships from background variation. Because real AI-RAN traffic traces with known parameter-KPI ground truth are difficult to obtain, we introduce a synthetic closed-loop traffic generator with planted latent dependencies. We use this controlled telemetry to evaluate a machine-learning-based dependency recovery pipeline that formulates the conversion of continuous traces into binary event indicators as a significance-detection problem. Experimental evaluation shows that the proposed pipeline reliably recovers the latent dependency structure from noisy continuous traces when the signal is sufficiently separated from background variation, while highlighting threshold calibration as the key factor controlling event-detection quality. These results constitute a foundational step toward interpretable dependency learning for adaptive AI-RAN control systems.

### 🤖 AI 总结

**一句话总结**：Next-generation wireless networks are expected to rely on multiple concurrent AI-driven control functions that optimize different network objectives simultaneously, particularly in AI-integrated and o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Event, Detection, Parameter-to-KPI, Dependency, Learning, AI-RAN, Next-generation, wireless

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06459v1) | [下载PDF](https://arxiv.org/pdf/2606.06459v1.pdf)

---

## [24. In-Context Multiple Instance Learning](https://arxiv.org/abs/2606.06458v1)

**作者**：Alexander Möllers, Marvin Sextro, Julius Hense 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-06-04

### 📄 论文摘要

Multiple Instance Learning (MIL) addresses problems where supervision is available at the level of bags of instances and has been successfully applied in fields ranging from computational pathology to satellite imagery. Nevertheless, existing algorithms struggle in the low-label regime that characterizes many real-world applications. Flexible models overfit and rigid ones fail to adapt to the task at hand. We show that pretraining an in-context learner with a Perceiver-style architecture on synthetic data yields a model that can solve new tasks from a handful of labeled bags. At inference time, classification happens in a single forward pass and requires no gradient updates. We propose and investigate different synthetic data generators for bag-structured data and find that they capture complementary inductive biases. A model pretrained on a mixture of these generators inherits their per-task strengths and achieves the best average performance across twelve MIL benchmarks, outperforming supervised baselines that require task-specific training.

### 🤖 AI 总结

**一句话总结**：Multiple Instance Learning (MIL) addresses problems where supervision is available at the level of bags of instances and has been successfully applied in fields ranging from computational pathology to...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：In-Context, Multiple, Instance, Learning, MIL, addresses, problems, where

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06458v1) | [下载PDF](https://arxiv.org/pdf/2606.06458v1.pdf)

---

## [25. Causal Atlases from Entropic Inference: Bayesian Networks beyond Optimal DAGs](https://arxiv.org/abs/2606.06440v1)

**作者**：Hazhir Aliahmadi, Irina Babayan, Greg van Anders  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-06-04

### 📄 论文摘要

Data-driven causal relationship identification is pertinent to advancing understanding of complex systems both within and beyond science. Bayesian networks offer a probabilistic method for modelling generic causal relationships via directed acyclic graphs (DAGs). However, typical techniques for constructing Bayesian networks rely on optimization, which can be ill-suited for learning causal relationships because the underlying data may admit multiple chains of causation. More data-faithful representations of causal relationships would provide frameworks for constructing multiple causal maps that are consistent with the variability that is inherent in underlying data. Here, we show that entropy-based inference generates atlases of plausible causal relationships that are consistent with underlying data. On simulated noisy data of 2- and 20-node linear structural equation models, we sample a maximum-entropy ensemble of graphs that allow us to quantify the inherent structural ambiguity in underlying causal relationships. Our method shows that "optimized" DAGs can contain causal artifacts are not consistent across equivalently accurate topologies.

### 🤖 AI 总结

**一句话总结**：Data-driven causal relationship identification is pertinent to advancing understanding of complex systems both within and beyond science. Bayesian networks offer a probabilistic method for modelling g...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Causal, Atlases, Entropic, Inference, Bayesian, Networks, beyond, Optimal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06440v1) | [下载PDF](https://arxiv.org/pdf/2606.06440v1.pdf)

---

## [26. Double Preconditioning (DoPr): Optimization for Test-Time Performance, not Validation Loss](https://arxiv.org/abs/2606.06418v1)

**作者**：Thomas T. Zhang, Alok Shah, Yifei Zhang 等 6 位作者  
**分类**：cs.LG, cs.AI, eess.SY  
**发布时间**：2026-06-04

### 📄 论文摘要

Many modern applications of deep learning involve training a neural network via a one-step prediction loss (e.g., $L^2$ regression, cross-entropy), but deploy the network by rolling out along its own predictions. Key examples include autoregressive language modeling, flow-based generative modeling, and robot policy learning. It is well-documented that these settings induce a phenomenon we call test-time feedback (TTF): the mismatch between the training/validation loss and downstream metrics of interest, such as task success rate and generation quality, which grows with task length. While data curation, architecture, and objective design have been proposed to combat train-test shift in TTF settings, this paper proposes optimization as a new design axis to mitigate error accumulation. Specifically, we introduce a new optimization paradigm called double-preconditioning (DoPr) uniquely tailored to the challenges of TTF. DoPr combines gradient-wise preconditioning, as in Adam and Muon, with activation-wise preconditioning (AP), such as in KFAC. We show that the addition of AP yields a drop-in intervention for increasing downstream model performance across a range of TTF settings. Interestingly, these gains in test-time performance do not consistently accompany improvements in validation loss, opening new questions about how to properly evaluate models trained with one-step supervised objectives.

### 🤖 AI 总结

**一句话总结**：Many modern applications of deep learning involve training a neural network via a one-step prediction loss (e.g., $L^2$ regression, cross-entropy), but deploy the network by rolling out along its own ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Double, Preconditioning, DoPr, Optimization, Test-Time, Performance, not, Validation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06418v1) | [下载PDF](https://arxiv.org/pdf/2606.06418v1.pdf)

---

## [27. The Post-GCN Decade Revisited: Curvature-Stratified Evaluation of Relational Learning](https://arxiv.org/abs/2606.06397v1)

**作者**：Shuo Wang, Xiangyu Wang, Quanxin Wang 等 12 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-04

### 📄 论文摘要

Current evaluation practices in relational learning rely heavily on flat leaderboards that average performance across heterogeneous datasets, implicitly assuming a uniform underlying structure. We show that this assumption introduces systematic bias: it obscures geometry-dependent performance variations and can lead to misleading conclusions about model generalization. In this work, we identify intrinsic geometry as a key latent factor governing model effectiveness. We demonstrate that conventional aggregated metrics mask critical performance trade-offs that only become visible when datasets are stratified by their geometric properties. To address this issue, we introduce a curvature-stratified evaluation framework that partitions datasets into positive, negative, and near-zero curvature regimes. Our benchmark evaluates 18 representative models including Graph Convolutional Networks (GCNs), Graph Foundation Models (GFMs), and tabular learning methods across 14 datasets. We find that model rankings are highly stable within each curvature regime but shift significantly across regimes, indicating that performance is fundamentally geometry-dependent rather than universally transferable. Notably, we identify regimes where GFMs offer diminishing returns compared to geometry-aligned GNNs. Based on these findings, we propose a geometry-aware evaluation protocol that yields more reliable and interpretable comparisons than standard aggregated benchmarks. We release all code, curvature-stratified dataset splits, and evaluation tools to support reproducible and rigorous assessment of future relational learning methods. Code and datasets are provided in our project homepage: https://sirbabbage.github.io/CurvBench_HOME/.

### 🤖 AI 总结

**一句话总结**：Current evaluation practices in relational learning rely heavily on flat leaderboards that average performance across heterogeneous datasets, implicitly assuming a uniform underlying structure. We sho...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Post-GCN, Decade, Revisited, Curvature-Stratified, Evaluation, Relational, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06397v1) | [下载PDF](https://arxiv.org/pdf/2606.06397v1.pdf)

---

## [28. Proper Scoring Rules for Right-Censored Survival Data](https://arxiv.org/abs/2606.06393v1)

**作者**：Jef Jonkers, Glenn Van Wallendael, Luc Duchateau 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-04

### 📄 论文摘要

Proper scoring rules provide a rigorous theoretical basis for the training and evaluation of probabilistic forecasts. However, in the presence of right censoring, the event time is only partially observed, rendering conventional scoring rules inapplicable in their standard form. We propose a framework for proper scoring of right-censored survival outcomes based on a simple idea: first, map the predictive distribution through the censoring mechanism, then apply the underlying proper score on the induced observed-data law. This yields localized scores for fixed censoring times and marginalized scores when the censoring time is random or only partially observed. The resulting construction recovers familiar right-censored likelihood and IPCW-type criteria within a coherent framework, while also yielding right-censored versions of the CRPS, pinball loss, Brier score, and energy score. We show that the marginalized score is proper under conditional independent censoring and strictly proper on the identifiable region. The same principle also leads to censored engression, a sample-based learning objective for multivariate right-censored survival modeling. In experiments, our scores correctly rank the oracle forecast across several censoring regimes, whereas forecast-dependent plug-in weighted scores can exhibit ranking reversals. Censored engression likewise substantially improves over naive training on censored outcomes.

### 🤖 AI 总结

**一句话总结**：Proper scoring rules provide a rigorous theoretical basis for the training and evaluation of probabilistic forecasts. However, in the presence of right censoring, the event time is only partially obse...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Proper, Scoring, Rules, Right-Censored, Survival, Data, provide, rigorous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06393v1) | [下载PDF](https://arxiv.org/pdf/2606.06393v1.pdf)

---

## [29. Learned Response-Field Inertia Operator for HEC-RAS 2D Water-Surface Elevation Prediction](https://arxiv.org/abs/2606.06385v1)

**作者**：Edward Holmberg, Elias Ioup, Md Meftahul Ferdaus 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-04

### 📄 论文摘要

This article presents a cross-dataset evaluation of learned native-cell surrogate models for solver-consistent water-surface elevation (WSE) prediction in HEC-RAS 2D. To avoid raster remapping error and information-access confounding, surrogates are evaluated directly on the original nonuniform computational cells under an explicit policy that separates static project inputs, current hydraulic state, project-input forcing, calibration-derived quantities, and future solver-output targets. We introduce the Learned Response-Field Inertia Operator (LRFIO), a no-forcing, increment-based learned surrogate that calibrates an inertial response operator from solved HEC-RAS trajectories and deploys the retained operator through closed-form native-cell rollout. LRFIO evaluates a base-case-first response hierarchy consisting of persistence, global calibrated inertia, and segmented response-field inertia. Segmentation, residual correction, and neuralized inertia are treated as learnable modeling choices, with added complexity retained only when validation evidence justifies its cost. Evaluated across four diverse HEC-RAS 2D benchmarks, LRFIO retains different response structures for different domains, demonstrating adaptive learned complexity. The selector audit shows controlled complexity with a maximum validation regret of 4.30%. During deployment, retained rollout times range from 0.003 s to 0.242 s, and the Beaver Bayou measured-solve comparison gives an estimated 2.75 x 10^4 horizon-normalized speedup over HEC-RAS. These results indicate that the current native-cell increment is a strong solver-conditioned predictive scaffold and that added response-field, neural, or spatial complexity should be retained only when empirically justified.

### 🤖 AI 总结

**一句话总结**：This article presents a cross-dataset evaluation of learned native-cell surrogate models for solver-consistent water-surface elevation (WSE) prediction in HEC-RAS 2D. To avoid raster remapping error a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：2D, Learned, Response-Field, Inertia, Operator, HEC-RAS, Water-Surface, Elevation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06385v1) | [下载PDF](https://arxiv.org/pdf/2606.06385v1.pdf)

---

## [30. End-to-End Subgraph Detection with GraphDETR](https://arxiv.org/abs/2606.06364v1)

**作者**：Dexiong Chen, Till Hendrik Schulz, Karsten Borgwardt  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-06-04

### 📄 论文摘要

Subgraph detection seeks to identify whether and where instances of query patterns occur within a larger graph. This problem is fundamental across scientific domains and is closely related to subgraph isomorphism, which is NP-complete, limiting combinatorial approaches to small patterns or moderately sized graphs. We introduce GraphDETR, a deep learning framework that formulates subgraph detection as a set prediction problem, analogous to DETR in object detection. GraphDETR encodes the target graph with a graph neural network, and employs a fixed set of learnable query vectors, decoded via a transformer decoder, to predict all pattern occurrences jointly in a single forward pass. This is enabled by training the model end-to-end with bipartite matching. Unlike traditional combinatorial methods that only solve exact structural matching, GraphDETR naturally extends to approximate matching, enabling detection beyond exact pattern correspondence. Empirically, we show that GraphDETR can detect diverse patterns, such as molecular structures, cycles, cliques, and fuzzy patterns of up to 50 nodes, in target graphs with up to 1000 nodes. We further evaluate on molecular functional group detection over the ChEMBL dataset, where GraphDETR predicts the complete set of functional groups per molecule, achieving a strong performance of $\text{AP}_{100} = 91.2$.

### 🤖 AI 总结

**一句话总结**：Subgraph detection seeks to identify whether and where instances of query patterns occur within a larger graph. This problem is fundamental across scientific domains and is closely related to subgraph...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：End-to-End, Subgraph, Detection, GraphDETR, seeks, identify, whether, where

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.06364v1) | [下载PDF](https://arxiv.org/pdf/2606.06364v1.pdf)

---

