# arXiv AI 论文日报 | 2026-10-15

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.AI](#csAI) (4 篇)
- [cs.LG](#csLG) (9 篇)
- [cs.CL](#csCL) (6 篇)

---

## cs.AI

## [1. Co-Evolving Acting and Forecasting for Language Agents](https://arxiv.org/abs/2610.20597v1)

**作者**：Haofei Yu, Yixing Chen, Yining Zhao 等 9 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-10-14

### 📄 论文摘要

Training language agents is bottlenecked by the high cost of long-horizon rollouts, yet standard agentic reinforcement learning (RL) learns only from a terminal scalar reward, leaving the supervision in intermediate steps largely unused. Prior work exploits this supervision through value targets that estimate per-step success probabilities or observation targets that fit environment response. Both are hard to construct well: (1) value targets come from the same single scalar signal for each step in the trajectory, and (2) observation targets, such as web pages and terminal logs, are long and noisy and reach only one step ahead. We propose \name, which adds a third kind of multi-step action targets. On successful on-policy trajectories, \name trains the policy backbone to generate the action sequences that follows each history. Each action is also supervised when forecast from the preceding histories, forming a temporal ensemble that the shared backbone absorbs during training, and this enables acting and forecasting to co-evolve. The policy still acts one step at a time at inference, with no overhead. Across five benchmarks (ALFWorld, ScienceWorld, WebShop, $τ^2$-bench, and AppWorld), \name (1) achieves stronger aggregate performance than GRPO and RL baselines with predictive auxiliary targets across simulated environments, while improving overall performance on both realistic applications; (2) delivers up to $1.9\times$ and $2.0\times$ higher sample efficiency than ECHO and GRPO, respectively, on ScienceWorld; and (3) achieves these gains with a single policy backbone, without additional models, separate pretraining, or inference overhead. The codebase is available at https://github.com/ulab-uiuc/CoPE.

### 🤖 AI 总结

**一句话总结**：Training language agents is bottlenecked by the high cost of long-horizon rollouts, yet standard agentic reinforcement learning (RL) learns only from a terminal scalar reward, leaving the supervision ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Co-Evolving, Acting, Forecasting, Language, Training, bottlenecked, high

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20597v1) | [下载PDF](https://arxiv.org/pdf/2610.20597v1.pdf)

---

## [2. Scaling Discovery Requires Forgetting](https://arxiv.org/abs/2610.20563v1)

**作者**：Shangyin Tan, Ben Zhou, Lakshya A Agrawal 等 11 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-10-14

### 📄 论文摘要

Automated research with LLM agents has shown promising results in various domains. Through iterative refinement and scored verifiers, LLM agents are capable of discovering new ideas. There are different ways to scale automated research: let one agent iterate for longer, run several agents in parallel, or further let the parallel agents communicate and build on one another's candidates. However, we find that all three strategies eventually plateau as the agents accumulate history. Each agent becomes anchored to its own past attempts, making fewer and smaller edits. Beyond this point, additional budget brings little further improvement. In this paper, we show that the key to scaling discovery further is to forget. Periodically discarding the search state, including every agent's session and the candidate history, and restarting from the best candidate found so far, unblocks the search and pushes the same budget further.   We implement forgetting in a team of agents with communication and evaluate it on four tasks spanning heuristic programming, kernel optimization and model training. The results show up to 15% improvement compared to parallel agents, and up to 39% compared to a single agent. Our results suggest that, for open-ended discovery, what an agent is allowed to remember matters as much as how much compute it is given.

### 🤖 AI 总结

**一句话总结**：Automated research with LLM agents has shown promising results in various domains. Through iterative refinement and scored verifiers, LLM agents are capable of discovering new ideas. There are differe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, Scaling, Discovery, Requires, Forgetting, Automated, research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20563v1) | [下载PDF](https://arxiv.org/pdf/2610.20563v1.pdf)

---

## [3. PhySGA: A Physics-Space Grounded Agentic Framework for Generalizable and Interactive 3D Composition](https://arxiv.org/abs/2610.20560v1)

**作者**：Weichen Lyu, Chong Xia, Mingyu Dong 等 6 位作者  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-10-14

### 📄 论文摘要

3D object composition is pivotal to digital content creation and robot simulation, while also serving as a critical testbed for physical intelligence in foundation models. Previous methods either leverage large language models to directly predict object coordinates, or utilize generative diffusion priors to synthesize composite images for visual alignment, both of which rely on static priors in digital spaces. However, these methods consistently struggle with complex compositions such as precise hanging, gravity-driven settling and hidden containment, as these tasks require interactive construction processes involving global planning, fine-grained alignment, and physical simulation. To address these challenges, we propose PhySGA, a Physics-Space Grounded Agentic Framework for 3D composition via agent exploration and physical simulation, enabling the universal interactive assembly of rigid, articulated, and deformable objects. Directly applying vanilla LLMs or VLMs to this task proves insufficient, as current models inherently lack grounded physical understanding and interactive construction experience. To overcome this limitation, we design a collaborative feedforward-feedback architecture: an Assembly Agent focuses on geometric and kinematic reasoning for global step planning and coarse adjustment, while a Critic Agent reasons over contact dynamics for simulator state diagnosis and fine-grained closed-loop correction. Furthermore, Action Routers map semantic planning and analysis onto executable physical primitives within the simulator, while a task-specific Self-Evolving Skill Library distills historical trial-and-error feedback into reusable experiences, boosting success rates and minimizing exploration attempts. Extensive experiments within Isaac Sim demonstrate that PhySGA significantly surpasses existing methods in relation fidelity, physical plausibility, and visual quality.

### 🤖 AI 总结

**一句话总结**：3D object composition is pivotal to digital content creation and robot simulation, while also serving as a critical testbed for physical intelligence in foundation models. Previous methods either leve...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, PhySGA, Physics-Space, Grounded, Agentic, Framework, Generalizable, Interactive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20560v1) | [下载PDF](https://arxiv.org/pdf/2610.20560v1.pdf)

---

## [4. The Wealth of Agents: Scaling Agentic AI Across Developers](https://arxiv.org/abs/2610.20518v1)

**作者**：Austin W. Hanjie, Carlos E. Jimenez, Zirui Wang 等 4 位作者  
**分类**：cs.AI, cs.MA  
**发布时间**：2026-10-14

### 📄 论文摘要

Today's agentic systems are typically designed, built, and deployed by single developers with full control over all participating agents. While this simplifies development, it limits the potential scale of agentic systems. We study multi-developer agentic systems (MDAs) which enable developers to collaboratively build agentic systems to push frontier capability beyond what any individual developer could achieve alone. We construct empirical and theoretical models of developers to compare MDAs with single-developer agentic systems (SDAs). On GAIA, a general assistant benchmark, a population of specialized developers whose individual agents do not exceed 35% accuracy reaches 70% when their agents are combined in an MDA. This MDA performs 12 percentage points above the median general-purpose SDA built with several times each specialist's development budget. Our theoretical models show how MDAs can incentivize specialization and encourage more efficient use of aggregated developer resources. Put together, our results make a preliminary case for MDAs as a new scaling axis by enabling developers with diverse capabilities and resources to advance agentic AI collaboratively.

### 🤖 AI 总结

**一句话总结**：Today's agentic systems are typically designed, built, and deployed by single developers with full control over all participating agents. While this simplifies development, it limits the potential sca...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, Wealth, Scaling, Agentic, Across, Developers, Today's

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20518v1) | [下载PDF](https://arxiv.org/pdf/2610.20518v1.pdf)

---

## cs.CL

## [5. Latent Compaction with Test-Time Training](https://arxiv.org/abs/2610.20582v1)

**作者**：Yingfa Chen, Xingyu Shen, Chaojun Xiao 等 4 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-10-14

### 📄 论文摘要

Long contexts enlarge key--value (KV) caches, increasing memory use and attention costs during generation. Compressing these caches must preserve information for unseen questions. We introduce **Latent Compaction**, which learns a compact document-specific cache through test-time training. We initialize cache entries using reconstruction importance, teacher attention, and key-space diversity. Training first fits attention outputs and log-normalizers to those of the full cache, with reconstruction-selected entries held fixed. It then jointly optimizes the entire cache through end-to-end distillation from the full-cache model. Model weights remain frozen throughout, and training uses only generic prompts about the document, without access to downstream questions or answers. Experiments on RULER, LongBench, and Phonebook Lookup demonstrate substantial gains over budget-matched compression baselines. On a RULER, for example, our method achieves 96.7% accuracy at 32$\times$ compression, compared with 40.0% for KVZip+. The method also transfers across model scales and families, with retrieval gains on both Qwen3 and MiniCPM5. These results show that treating the KV cache as a neural network and optimizing it with test-time training can preserve retrieval accuracy under aggressive compression. The code is released at https://www.github.com/THUNLP/latent-compaction

### 🤖 AI 总结

**一句话总结**：Long contexts enlarge key--value (KV) caches, increasing memory use and attention costs during generation. Compressing these caches must preserve information for unseen questions. We introduce **Laten...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Latent, Compaction, Test-Time, Training, Long, contexts, enlarge, key--value

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20582v1) | [下载PDF](https://arxiv.org/pdf/2610.20582v1.pdf)

---

## [6. Manacá-1B-Instruct-2: Reproducible Safety Alignment for a Native Brazilian-Portuguese LLM. Negative DPO Results, a Controlled Composition Scan, and a Silent Failure Mode of the LLM Judge](https://arxiv.org/abs/2610.20570v1)

**作者**：Bruno Leonardo Santos Menezes, Carlos Leonardo Souza Cardoso, Fabio André Machado Porto  
**分类**：cs.CL  
**发布时间**：2026-10-14

### 📄 论文摘要

Brazilian Portuguese remains underserved by open-source language models, and the few that are safety-aligned rarely document what did not work or validate comparisons with statistical significance. We present Manacá-1B-Instruct-2, the second-generation post-training alignment of Manacá-1B (1.72B parameters, trained from scratch for PT-BR), with an SFT corpus of 291,223 examples. We document three DPO attempts, all negative, including a case where the training reward margin reaches 1.0 while free generation does not change at all, and show that safety came from a dedicated safety-SFT (LLM-jp AnswerCarefully style), refined over three iterations until closing the safety-helpfulness frontier. A controlled scan of the fraction of general data in the safety-SFT mix (10% to 60%) reveals a non-monotonic over-refusal curve with a knee point at 40-50%. The final model is compared against four external PT-BR models on the same items, with Wilson confidence intervals and paired McNemar tests with Holm-Bonferroni correction: the lower bound of its safety interval (94.1%) lies above the upper bound of all four baselines. We also report a methodological finding for LLM-judge evaluation: on two of six safety items in MT-Bench-PT, the judge categorically refuses to assign a score regardless of the evaluated response, silently reducing the effective N of that category in every prior report of the project. We complement this with an n-gram decontamination check and a Chinchilla-anchored compute-budget table that attributes the gap in general capability to pre-training scale rather than alignment methodology. All code, raw data, logs, and scripts that produce every reported number are publicly released.

### 🤖 AI 总结

**一句话总结**：Brazilian Portuguese remains underserved by open-source language models, and the few that are safety-aligned rarely document what did not work or validate comparisons with statistical significance. We...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Manacá-1B-Instruct-2, Reproducible, Safety, Alignment, Native, Brazilian-Portuguese, Negative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20570v1) | [下载PDF](https://arxiv.org/pdf/2610.20570v1.pdf)

---

## [7. PerSo: Investigating Facets of LLMs' Social Intelligence in Real-World Persuasion Scenarios](https://arxiv.org/abs/2610.20548v1)

**作者**：Ali Zamani, Soroush Esfahanian, Erfan Shahabi 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.SI  
**发布时间**：2026-10-14

### 📄 论文摘要

Understanding the social intelligence of large language models (LLMs) is increasingly important for applications involving human-AI interaction and multi-agent environments. Social intelligence comprises two aspects: cognitive intelligence, the ability to infer others' mental states, and behavioral intelligence, the ability to select appropriate social actions based on these inferences to achieve social goals. Persuasion provides a natural testbed in which both aspects are simultaneously at play, yet prior benchmarks typically evaluate them in isolation using synthetic scenarios. We introduce PerSo, a benchmark that evaluates both aspects on real-world persuasion dialogues from Reddit's ChangeMyView community, using an LLM-in-the-loop pipeline to construct the evaluation tasks, validated through human annotation. Our evaluation of diverse LLMs shows that performance generally scales with model size but varies across dimensions. The strongest LLM slightly surpasses the best observed human performance on the behavioral task, while the best human participant remains ahead on the cognitive task.

### 🤖 AI 总结

**一句话总结**：Understanding the social intelligence of large language models (LLMs) is increasingly important for applications involving human-AI interaction and multi-agent environments. Social intelligence compri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, PerSo, Investigating, Facets, LLMs', Social, Intelligence, Real-World

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20548v1) | [下载PDF](https://arxiv.org/pdf/2610.20548v1.pdf)

---

## [8. PrismaCoder: Pushing the Boundaries of Open Multimodal Code Intelligence through Decomposed Rubric Synthesis](https://arxiv.org/abs/2610.20538v1)

**作者**：Qiushi Sun, Jingyang Gong, Yang Liu 等 17 位作者  
**分类**：cs.CL, cs.AI, cs.CV, cs.LG, cs.SE  
**发布时间**：2026-10-14

### 📄 论文摘要

Multimodal code intelligence connects the symbolic world of programs with the visual world their execution creates. Interest in this capability is burgeoning, as models are increasingly asked to produce charts, webpages, animations, and semi-structured documents. Recently, proprietary models have pushed far ahead, producing interactive artifacts even from a text description or a screenshot alone. Yet their data and training remain closed, and open progress is held back by the quantity and quality of available data and by the pipelines and methods for producing it. Quality is the harder of the two, since a sample must be correct as a program, well built, and above all visually right once rendered. No existing signal covers all three. Execution often returns just a pass or fail, code similarity does not map to the visual output, and task-specific verifiers do not generalize. To push open progress further, we start from the data side with PrismaForge, a hierarchical data pipeline centered on a synthesized rubric that decomposes these factors into checkable criteria. The same rubric serves as both filter and reward: it curates the supervised corpus, then drives reinforcement learning on visual-coding tasks. Leveraging PrismaForge for data synthesis and filtering, we build PrismaCoder-2M, the most diverse open dataset for multimodal code intelligence and the largest to date. On the model side, we train PrismaCoder-9B and PrismaCoder-35B on this data and release both. They lead the open state of the art by a wide margin and rival leading proprietary systems. Our analyses further show that the proposed rubric-based pipeline improves multimodal coding performance across model backbones. We release our code and data at https://qiushisun.github.io/PrismaCoder-Home/.

### 🤖 AI 总结

**一句话总结**：Multimodal code intelligence connects the symbolic world of programs with the visual world their execution creates. Interest in this capability is burgeoning, as models are increasingly asked to produ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, PrismaCoder, Pushing, Boundaries, Open, Multimodal, Code, Intelligence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20538v1) | [下载PDF](https://arxiv.org/pdf/2610.20538v1.pdf)

---

## [9. Lost in Translation: Why Lower Bias Scores Don't Mean Fairer Models](https://arxiv.org/abs/2610.20479v1)

**作者**：Harsh Kumar  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-10-14

### 📄 论文摘要

Bias audits of multilingual language models usually compare a model's average stereotype score in English with its average in another language and read the difference as a difference in fairness. We ask how much of that difference is noise. Auditing ten open models in eight languages, we measure how far scores move when English test items are merely reworded, test every language shift item by item, and check that the test catches shifts we inject on purpose. In all 70 model-language pairs the stereotype score falls below its English level, and for Hindi, Korean and Swahili the drop clearly exceeds what rewording English produces; most of it comes from StereoSet items. Judging every translation, we find that imperfect ones drop more, but faithful translations alone drop nearly as much. Still, a lower average does not show that a model is fairer. An item's English score predicts its translated score far less well than its reworded score (correlation 0.23, 0.27 on faithful translations, vs. 0.48), while scores stay as far from neutral, models agree on translated items, and within Hindi or Spanish a translated item's score correlates with its own rewording at 0.84 and 0.82. The average cannot distinguish lower bias from a different pattern of item-level scores. We also document three common pipeline errors that silently erase bias signal, and release our code.

### 🤖 AI 总结

**一句话总结**：Bias audits of multilingual language models usually compare a model's average stereotype score in English with its average in another language and read the difference as a difference in fairness. We a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Lost, Translation, Why, Lower, Bias, Scores, Don't, Mean

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20479v1) | [下载PDF](https://arxiv.org/pdf/2610.20479v1.pdf)

---

## [10. AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.20474v1)

**作者**：Peidong Wang, Ying Chang, Zhiming Ma 等 11 位作者  
**分类**：cs.CL, cs.RO  
**发布时间**：2026-10-14

### 📄 论文摘要

Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the executor on persistent failures without asking whether a failure lies in how the executor is called or in what it can do. We ask when a self-improving embodied system should change the weights of its executor, and propose AdaRSI, an on-demand RSI framework for embodied agents. A coding agent first improves its skills and harness, then attributes persistent failures by retrying failing sub-steps from saved states, and fine-tunes only the sub-steps that remain unreliable, with demonstrations it collects itself and experience carried over from earlier tasks. On all 50 target tasks of RoboCasa365, with GR00T N1.5 as the executor and no human demonstrations, AdaRSI improves the VLA on all three suites and raises its success on unseen composite tasks from 4.6% to 13.8%. Compared with fine-tuning every sub-step, it reaches slightly higher success while using only 28% of the GPU time and 22% of the self-collected demonstrations, and fine-tuning without a harness trains more yet gains far less.

### 🤖 AI 总结

**一句话总结**：Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harnes...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, AdaRSI, On-Demand, Recursive, Self-Improvement, Embodied, Pretrained, vision-language-action

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20474v1) | [下载PDF](https://arxiv.org/pdf/2610.20474v1.pdf)

---

## cs.CV

## [11. Can Learning to Answer Spatial Questions Improve Novel-View Generation?](https://arxiv.org/abs/2610.20610v1)

**作者**：Jahyeok Koo, Hyeonseo Yu, Seungho Jang 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-14

### 📄 论文摘要

Generating novel views from limited observations requires preserving both the appearance and spatial structure of a scene. Although recent approaches exploit fine-grained geometric cues, they do not explicitly model high-level semantic and spatial properties such as object identity, attributes, and inter-object relationships. In this work, we investigate whether 3D language understanding can provide complementary supervision for novel-view generation. We introduce Ask4NV, built on a pretrained unified multimodal model with a Mixture-of-Transformers (MoT) architecture. Our model incorporates camera geometry into both VAE and ViT representations and leverages understanding features during generation through joint self-attention with a modality-aware attention masking strategy. Experiments demonstrate strong image quality and geometric consistency in novel-view generation, alongside competitive 3D language understanding. Further analysis shows that joint training improves cross-view correspondence in VAE representations and similarity in a 3D-aware feature space.

### 🤖 AI 总结

**一句话总结**：Generating novel views from limited observations requires preserving both the appearance and spatial structure of a scene. Although recent approaches exploit fine-grained geometric cues, they do not e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Can, Learning, Answer, Spatial, Questions, Improve, Novel-View, Generation?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20610v1) | [下载PDF](https://arxiv.org/pdf/2610.20610v1.pdf)

---

## [12. CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image Generation](https://arxiv.org/abs/2610.20603v1)

**作者**：Xiaoli Xu, Zhengtao Wu, Zhengze Xu 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-14

### 📄 论文摘要

We present CommerceGen-Studio, an end-to-end framework for generating commercial-grade main images for e-commerce Stock Keeping Units (SKUs). Our framework is organized along a three-stage pipeline of information extraction, semantic rewriting, and multi-condition generation: Prompt-Eval-Refine-Loop Agent (PERL-Agent) distills heterogeneous SKU metadata into concise selling-point text lists through an iterative closed loop of VLM and LLM roles scored by a reference-free rubric. Layout Thinker Optimization (LTO) aligns the rewriter with both caption and rendered-image quality via alternating domain-specific policy optimization. SKU-DiT, trained under Reinforce-Distill-Reinforce (RDR) progressive training, conditions jointly on the white-background product image, the trademark crop, and the structured layout to hold subject fidelity, trademark integrity, and character-level text accuracy together. The framework runs in production at a scale of millions of main images per day with a latency of a few seconds per image, which we believe makes it among the first systems of this kind to operate at commercial scale. We also release CommerceGen-Bench, a benchmark of hard cases collected from live traffic across all product categories. On it, our framework achieves the highest overall scores among the evaluated open-source baselines on both editing tracks, with and without prompt enhancement. It also matches much larger closed-source models, and beats several of them at Instruction Following and Product Integration - the two properties that determine whether an image can be published.

### 🤖 AI 总结

**一句话总结**：We present CommerceGen-Studio, an end-to-end framework for generating commercial-grade main images for e-commerce Stock Keeping Units (SKUs). Our framework is organized along a three-stage pipeline of...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, We, CommerceGen-Studio, End-to-End, Framework, Commercial-Grade, Main-Image, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20603v1) | [下载PDF](https://arxiv.org/pdf/2610.20603v1.pdf)

---

## [13. DynThinker: Unifying Static 3D and Dynamic 4D Spatial Reasoning](https://arxiv.org/abs/2610.20598v1)

**作者**：Qihang Cao, Haoyuan Li, Zihan Guo 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-14

### 📄 论文摘要

Achieving general spatial intelligence requires a unified understanding of both static 3D and dynamic 4D. However, we find that existing models struggle to excel at both: 3D post-training can weaken dynamic understanding, while 4D-specialized models often lack strong static 3D reasoning. Our analysis reveals that this spatial--dynamic interference is highly non-uniform across parameter groups, with the balance between static and dynamic capabilities particularly sensitive to changes in late-layer MLPs. To address this interference, we propose DynThinker, a unified framework for jointly strengthening static and dynamic spatial reasoning. Decoupled Exponential Moving Average (D-EMA) applies configurable group-wise averaging to constrain drift in interference-sensitive pretrained parameters while preserving flexibility for capability enhancement. Spatial-Dynamic Fusion (SDF) complements D-EMA by selectively integrating spatial and temporal priors from a dynamic geometry encoder into intermediate VLM representations under semantic guidance. Across ten metrics spanning nine static 3D and dynamic 4D benchmarks, DynThinker achieves the highest average score among all evaluated models. Notably, DynThinker achieves 56.0 on ReVSI, 67.2 on DSR-Bench, and 51.2 and 40.1 under the sample-wise and group-wise evaluation protocols of DSI-Bench, respectively, setting new state-of-the-art results among the compared open-source models across all four evaluations within a unified model.

### 🤖 AI 总结

**一句话总结**：Achieving general spatial intelligence requires a unified understanding of both static 3D and dynamic 4D. However, we find that existing models struggle to excel at both: 3D post-training can weaken d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, 4D, DynThinker, Unifying, Static, Dynamic, Spatial, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20598v1) | [下载PDF](https://arxiv.org/pdf/2610.20598v1.pdf)

---

## [14. GeoThinker-$F$: Endogenous Predictive World Representations for Fast Spatial Intelligence](https://arxiv.org/abs/2610.20592v1)

**作者**：Haoyuan Li, Qihang Cao, Huanyuan Zhou 等 13 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-14

### 📄 论文摘要

Existing geometry-aware Multimodal Large Language Models (MLLMs) increasingly rely on external 3D encoders to provide structural priors, but executing these additional encoder paths at inference introduces substantial latency and computational overhead. We propose GeoThinker-$F$, an efficient framework that internalizes spatiotemporal perception by transforming causal MLLM hidden states into predictive latent world representations. Our key insight is that intermediate semantic representations contain sufficient information to predict useful representations of current geometry and future semantics, without requiring an exact reproduction of features from a dedicated 3D encoder. To realize this idea, GeoThinker-$F$ adopts a decoupled two-stage training strategy. In the first stage, the MLLM backbone is frozen while lightweight Latent Frame Prediction (LFP) heads learn from an offline 3D geometry expert and next-frame semantic targets. In the second stage, the external expert is removed, and the model is jointly optimized to generate and selectively integrate its self-predicted priors through a specialized Spatial-Grounded Temporal (SGT) Fusion module. Extensive evaluations show that GeoThinker-$F$ eliminates runtime dependence on external 3D geometry encoders while maintaining competitive performance across diverse spatial intelligence benchmarks. It achieves up to a $3.6\times$ inference speedup, reducing latency from $1.45\,\mathrm{s}$ to $0.40\,\mathrm{s}$ while retaining strong spatial reasoning performance.

### 🤖 AI 总结

**一句话总结**：Existing geometry-aware Multimodal Large Language Models (MLLMs) increasingly rely on external 3D encoders to provide structural priors, but executing these additional encoder paths at inference intro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GeoThinker-$F$, Endogenous, Predictive, World, Representations, Fast, Spatial, Intelligence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20592v1) | [下载PDF](https://arxiv.org/pdf/2610.20592v1.pdf)

---

## [15. Feed-Forward Multi-View Feature Coding for 3D Gaussian Splatting](https://arxiv.org/abs/2610.20590v1)

**作者**：Seungmi Choi, Ji-Hyoun Choi, Suhyun Jo 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-14

### 📄 论文摘要

Feed-forward 3D Gaussian Splatting (3DGS) methods enable efficient reconstruction of 3D scenes from sparse multi-view images in a single forward pass, without scene-specific optimization. However, existing feed-forward scene-coding pipelines first generate a complete Gaussian representation and then encode its geometry and appearance attributes separately, often involving non-differentiable operations. The resulting 'generate-then-compress' pipeline requires complex attribute-specific codec designs and limits rate-distortion performance by restricting the exploitation of cross-attribute redundancy. We propose multi-view feature coding for Gaussian splatting (MFGS), an end-to-end feed-forward framework for scene coding. Instead of compressing an explicit Gaussian representation, MFGS extracts multi-view features from the input images and encodes them into a compact bitstream. Through end-to-end rate-distortion training, MFGS learns compact multi-view features that jointly represent geometry and appearance, enabling the receiver to predict Gaussian attributes from the decoded features. We further introduce importance-guided Gaussian selection to accommodate different rendering budgets, allowing the receiver to adjust the number of Gaussians used for rendering from the same bitstream. Across RE10K, ACID, and DL3DV, MFGS achieves 99.76-99.86% bitrate savings over the generate-then-compress pipeline, as measured by BD-rate, while reducing total GMACs by 52-55% and providing an approximately 12 times end-to-end speedup.

### 🤖 AI 总结

**一句话总结**：Feed-forward 3D Gaussian Splatting (3DGS) methods enable efficient reconstruction of 3D scenes from sparse multi-view images in a single forward pass, without scene-specific optimization. However, exi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Feed-Forward, Multi-View, Feature, Coding, Gaussian, Splatting, 3DGS

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20590v1) | [下载PDF](https://arxiv.org/pdf/2610.20590v1.pdf)

---

## [16. Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation](https://arxiv.org/abs/2610.20571v1)

**作者**：Weijie Wang, Haomin Zhang, Ye Li 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-14

### 📄 论文摘要

Long-form agentic video generation must turn a screenplay into shots that remain spatially and temporally consistent across nonconsecutive requests. Passing prompts or recent frames between shots does not provide a shared spatial frame for revisiting a scene or a time-indexed record for replaying an earlier event. We present Any Time, Any Space (ATAS), which compiles a screenplay into shot requests with explicit location, camera, and event-time references. Before generation, it retrieves relevant evidence from a scene memory of registered static geometry and an event memory of dynamic observations indexed by scene, event, and time. After generation, ATAS reconstructs and registers the clip. It updates memory only when review and state checks accept the observation, while film delivery remains independent of memory admission. Across four video generators, ATAS improves all reported cross-shot consistency measures and achieves the highest aggregate benchmark score for each backbone. It also outperforms the compared agents and 3D-guided methods on target-image spatial revisit, leads three event-recapture criteria, and receives the highest human ratings on all six criteria. The video results and code are available on our project page: https://lhmd.top/atas/.

### 🤖 AI 总结

**一句话总结**：Long-form agentic video generation must turn a screenplay into shots that remain spatially and temporally consistent across nonconsecutive requests. Passing prompts or recent frames between shots does...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Any, Time, Space, World-State-Centric, Framework, Agentic, Video, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20571v1) | [下载PDF](https://arxiv.org/pdf/2610.20571v1.pdf)

---

## [17. A$^3$PreCore: Robust Rigid Registration for Native FLAIR-Space Brain-Mask Transfer](https://arxiv.org/abs/2610.20561v1)

**作者**：Elmira Mirzabeigi, Zahra Khalilzad, Taylor Snowden-Richardson 等 7 位作者  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-10-14

### 📄 论文摘要

Reliable brain-mask transfer into native fluid-attenuated inversion recovery (FLAIR) space can fail when T1-to-FLAIR rigid registration is unstable. We developed A$^3$PreCore, a six-degree-of-freedom rigid-registration strategy that aligns the full bias-corrected T1-weighted image to native FLAIR using normalized mutual information while preserving the established T1-space anatomical mask. We also introduced extended quantitative quality control (E-QC), which characterizes mask extent, field-of-view-relative position, FLAIR intensity support, boundary support, inferior morphology, and pairwise geometric disagreement. In 78 participants with paired T1-weighted and FLAIR imaging, A$^3$PreCore was compared with fsl_anat and the Brain Extraction Tool (BET). Gross rigid-body misregistration occurred in 21/78 fsl_anat outputs (26.9%) and 0/78 A$^3$PreCore outputs (exact two-sided McNemar p=9.54 x 10^-7). Among 57 participants without gross fsl_anat misregistration, A$^3$PreCore preserved close agreement (median Dice=0.993; median paired Delta NMI=-0.00007, p=0.429). A$^3$PreCore remained broadly concordant with BET (median Dice=0.955), with less inferior and extracranial extension in representative comparisons. Method-blinded neuroscientists ranked A$^3$PreCore first in 35/40 participants (87.5%). E-QC additionally exposed severe orientation-related disagreement not evident from global descriptors or centroid displacement alone. These findings support A$^3$PreCore as a robust native-FLAIR brain-mask transfer strategy and E-QC as a complementary framework for multidimensional mask characterization and participant-specific geometric quality control.

### 🤖 AI 总结

**一句话总结**：Reliable brain-mask transfer into native fluid-attenuated inversion recovery (FLAIR) space can fail when T1-to-FLAIR rigid registration is unstable. We developed A$^3$PreCore, a six-degree-of-freedom ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：A$^3$PreCore, Robust, Rigid, Registration, Native, FLAIR-Space, Brain-Mask, Transfer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20561v1) | [下载PDF](https://arxiv.org/pdf/2610.20561v1.pdf)

---

## [18. Speculative Sampling in Interactive Video Generation](https://arxiv.org/abs/2610.20556v1)

**作者**：Yubo Huang, Yuxuan Zhang, Jiaming Liu 等 5 位作者  
**分类**：cs.CV, cs.HC  
**发布时间**：2026-10-14

### 📄 论文摘要

Interactive video generation commonly relies on small bidirectional chunks to reduce response latency. Yet our preliminary experiments show that larger chunks improve video quality and better utilize GPU parallelism, allowing more latents to be sampled with only a modest increase in sampling time. Motivated by these observations, we propose Speculative Sampling, a strategy that combines the modeling power of large bidirectional windows with the low-latency interaction of small ones. It expands the modeling window by appending noise latents as padding and caches the resulting predictions for reuse when the condition remains unchanged. Predictions are delivered incrementally, while the uncommitted future remains replaceable. Our latency analysis shows that this removes the waiting-time lower bound imposed by chunk boundaries, shifting the optimization focus from reducing chunk size to accelerating per-chunk sampling. Bidirectional window size thus becomes a decision variable for jointly optimizing visual quality and sampling time, rather than a necessary constraint on low-latency interaction. This opens a path to serving large bidirectional models in interactive streaming systems without complex streaming post-training.

### 🤖 AI 总结

**一句话总结**：Interactive video generation commonly relies on small bidirectional chunks to reduce response latency. Yet our preliminary experiments show that larger chunks improve video quality and better utilize ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Speculative, Sampling, Interactive, Video, Generation, commonly, relies, small

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20556v1) | [下载PDF](https://arxiv.org/pdf/2610.20556v1.pdf)

---

## [19. VascuSR: Iterative Anatomy-Aware Diffusion for CT Super-Resolution](https://arxiv.org/abs/2610.20509v1)

**作者**：Hairong Ni, Jiahe Huang, Minghao Guo 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-10-14

### 📄 论文摘要

Generative super-resolution (SR) can recover sharp detail in computed tomography (CT) images from severely downsampled observations, but the missing high-frequency content is not uniquely determined by the low-resolution input. Consequently, visually plausible reconstructions may contain anatomically unsupported vascular detail, such as missing, spurious, or incorrectly connected vessels. To overcome this challenge, we introduce VascuSR, an iterative anatomy-aware diffusion framework that combines image reconstruction with explicit 3D vascular guidance. First, to provide richer anatomical guidance, we use an explicit 3D vascular representation that captures structural information beyond individual slices. This representation also simplifies vascular refinement by allowing a lightweight 3D generative refiner to focus on vascular structure rather than complex CT appearance. Second, to guide slice-wise SR, a lightweight anatomy controller injects the refined structure into the diffusion decoder, while iterative feedback updates this guidance from each new SR volume. On re-annotated MSD Task08 and HVM datasets, VascuSR outperforms interpolation and learning-based SR baselines in segmentation accuracy (Dice and clDice) and 3D vascular structure (connectivity and mean centerline distance), while maintaining image quality comparable to its SR backbone. Compared with learning-based baselines, VascuSR reduces class-averaged connected-component counts by over 20% on both datasets and mean centerline distance by over 10% on MSD.

### 🤖 AI 总结

**一句话总结**：Generative super-resolution (SR) can recover sharp detail in computed tomography (CT) images from severely downsampled observations, but the missing high-frequency content is not uniquely determined b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, CT, SR, VascuSR, Iterative, Anatomy-Aware, Super-Resolution, Generative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20509v1) | [下载PDF](https://arxiv.org/pdf/2610.20509v1.pdf)

---

## [20. OLiVES: An Outdoor Low-Light Video Benchmark for Enhancement and Segmentation](https://arxiv.org/abs/2610.20501v1)

**作者**：Yini Li, Joanne Lin, David Blackham 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-14

### 📄 论文摘要

Low-light video processing remains an underexplored problem in computer vision, primarily due to the scarcity of high-quality ground-truth data. Existing public datasets exhibit several limitations, including restricted motion diversity, limited scene coverage, weak degradations, reliance on auxiliary modalities such as event data, and misalignment between low-light inputs and ground truth. Furthermore, current datasets typically address either low-light enhancement or scene understanding, whereas these tasks should be considered jointly. We introduce \textbf{OLiVES}, a benchmark dataset for outdoor low-light videos with dynamic scenes, designed to support both low-light video enhancement (LLVE) and video object segmentation (VOS). The dataset addresses key content gaps by incorporating a diverse range of natural textures, animals, occlusions, dynamic activities, and close-up scenes. To the best of our knowledge, OLiVES is the first outdoor low-light video dataset captured using professional cinema-grade cameras. It provides over 25,000 aligned normal- and low-light frame pairs, along with over 46,000 VOS annotations. We benchmark state-of-the-art LLVE and VOS methods on OLiVES and show that training on it improves performance on both tasks. The OLiVES project page is available at: https://anonymous-OLiVES.github.io/.

### 🤖 AI 总结

**一句话总结**：Low-light video processing remains an underexplored problem in computer vision, primarily due to the scarcity of high-quality ground-truth data. Existing public datasets exhibit several limitations, i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, OLiVES, Outdoor, Low-Light, Video, Benchmark, Enhancement, Segmentation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20501v1) | [下载PDF](https://arxiv.org/pdf/2610.20501v1.pdf)

---

## [21. Quantifying privacy risks in foundation model representations of brain MRI](https://arxiv.org/abs/2610.20494v1)

**作者**：Imen Bajar, Héber Hwang Arcolezi, Antoine Boutet 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-10-14

### 📄 论文摘要

Pretrained representations are increasingly used to share and reuse information from medical images without exposing the original scans, but it is unclear how much patient-specific information these representations retain. We investigate this question for brain magnetic resonance imaging (MRI) by evaluating five frozen pretrained encoders spanning different architectures, pretraining objectives, and training domains on two longitudinal T1-weighted datasets, OASIS-2 and MIRIAD. Under an attacker model with access to released embeddings, the corresponding public encoder, and auxiliary MRI scans, we evaluate patient linkage and sensitive-attribute inference. Across the evaluated representations, we observe substantial subject-specific information: rank-1 patient linkage reaches up to 99\% on MIRIAD and exceeds 90\% on OASIS-2 for the highest-risk representation, despite the absence of an identification objective during encoder training. We further show that the released embeddings retain information about a demographic attribute, with recorded-sex prediction reaching balanced accuracy of 90.9\% on OASIS-2 and 95.5\% on MIRIAD. Overall, our results demonstrate that replacing raw brain MRI with learned embeddings does not, by itself, eliminate patient-linkage or attribute-inference risk, and is therefore insufficient on its own to establish anonymity.

### 🤖 AI 总结

**一句话总结**：Pretrained representations are increasingly used to share and reuse information from medical images without exposing the original scans, but it is unclear how much patient-specific information these r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Quantifying, privacy, risks, foundation, model, representations, brain

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20494v1) | [下载PDF](https://arxiv.org/pdf/2610.20494v1.pdf)

---

## cs.LG

## [22. Your Transformer Is Secretly Elastic](https://arxiv.org/abs/2610.20588v1)

**作者**：Walter Simoncini, Dheeraj Varghese, Gertjan J. Burghouts 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-14

### 📄 论文摘要

Scaling up transformers has produced models with broad capabilities, deployed across heterogeneous hardware and fluctuating workloads. Yet, model families offer only a few fixed sizes (e.g., S, B, L), forcing users to commit to a model based on hardware and latency constraints. This rigidity is often suboptimal under varying query loads. We introduce a retraining-free method that elastifies pre-trained transformers into a single model that adapts on-the-fly across a continuum of computational budgets. Our key contribution is a differentiable relaxation of the functional unit-ranking problem: unlike prior work, which optimizes a single importance weight per MLP block or attention head, we rank every individual MLP neuron and attention head jointly, on a common scale, by minimizing the model's loss under soft pruning across many sparsity targets, all at once. Across 27 vision and text transformer encoders ranging from 22M to 8B parameters, our method yields smooth degradation up to 60% sparsity and outperforms one-shot baselines under deep pruning. For example, pruning DINOv3 ViT-H+/16 to 50% sparsity removes 427M parameters while reducing ImageNet-1k linear-probing accuracy by only 0.8%, without the need for weight correction or retraining. At 60% sparsity, a pruned AugReg ViT-B/16 model achieves up to $1.80\times$ higher throughput and $1.26\times$ lower single-query latency on an A100 GPU. Elastic models are produced in minutes, with construction time scaling sub-linearly with parameter count.

### 🤖 AI 总结

**一句话总结**：Scaling up transformers has produced models with broad capabilities, deployed across heterogeneous hardware and fluctuating workloads. Yet, model families offer only a few fixed sizes (e.g., S, B, L),...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：up, Transformer, Secretly, Elastic, Scaling, transformers, has, produced

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20588v1) | [下载PDF](https://arxiv.org/pdf/2610.20588v1.pdf)

---

## [23. Learnable Hodge-Laplacian Driven Mixture of Experts for Steady-PDE Surrogates on Coarse Unstructured Meshes](https://arxiv.org/abs/2610.20585v1)

**作者**：Stavros Nousias, Akis Nousias, Konstantinos Gkrispanis  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-10-14

### 📄 论文摘要

Current approaches for steady partial differential equations surrogate models on unstructured meshes apply a single mixing mechanism to the whole solution. This paper proposes an architecture that partitions the solution among vanilla transformer experts, each focused on a different spectral scale. The partition is built from a discrete Hodge Laplacian $L_0=\star_0^{-1} d_0^{\top}\star_1 d_0$, that serves as a fitting layer measuring high-frequency content. A gating mechanism takes the mesh as input and produces the per-vertex weights that recombine the expert outputs. AirFRANS is a steady Reynolds-averaged Navier--Stokes (RANS) airfoil benchmark. We evaluate our approach in a reduced remeshed version of the benchmark with each unstructured mesh counting 9.6K faces and 4.9K vertices. We compare our approach with the Transolver on the same dataset and dataset slit. Our approach reduces relative $L_2$ error by 31\% and interior mean squared error by 47\%.

### 🤖 AI 总结

**一句话总结**：Current approaches for steady partial differential equations surrogate models on unstructured meshes apply a single mixing mechanism to the whole solution. This paper proposes an architecture that par...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Learnable, Hodge-Laplacian, Driven, Mixture, Experts, Steady-PDE, Surrogates

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20585v1) | [下载PDF](https://arxiv.org/pdf/2610.20585v1.pdf)

---

## [24. One Task, Many Interfaces: Simple Cross-Interface Consistency Training Improves LLM Agent Robustness](https://arxiv.org/abs/2610.20576v1)

**作者**：Artin Tajdini, Manpreet Kaur, Peng Qi  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-10-14

### 📄 论文摘要

Post-training binds the competence of an LLM agent to the interface it was trained on. Semantics-preserving perturbations of that interface, such as renaming an action or changing the notation, leave the underlying task unchanged yet make the agent worse at it. Scoring each sample independently means interface randomization only broadens this dependence from a single interface to the training interface distribution, so out-of-distribution perturbations still degrade the agent. We propose Cross-Interface Policy Regularization (CIPR), a self-supervised objective that replaces action names with uninformative identifiers and presents each training sample under two interfaces in which equivalent actions are identified by construction. CIPR penalizes the KL divergence between the action distributions induced under the two interfaces, so the policy behaves consistently across them. We evaluate CIPR in both supervised and reinforcement-learning post-training, where it improves robustness. On agentic function calling, held-out interface perturbations reduce the accuracy of a post-trained agent by nearly 25%, and CIPR recovers 10.5% while leaving accuracy on the unchanged interface intact.

### 🤖 AI 总结

**一句话总结**：Post-training binds the competence of an LLM agent to the interface it was trained on. Semantics-preserving perturbations of that interface, such as renaming an action or changing the notation, leave ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：One, Task, Many, Interfaces, Simple, Cross-Interface, Consistency, Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20576v1) | [下载PDF](https://arxiv.org/pdf/2610.20576v1.pdf)

---

## [25. Detection of Potato Plant Leaf Diseases using Convolutional Neural Networks](https://arxiv.org/abs/2610.20544v1)

**作者**：Haimanot Bitew Alemayehu, Simachew Melaku Ayalew, Chilotie Desalew Mengesha 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-14

### 📄 论文摘要

Potato is an important food-security crop in Ethiopia, but its production is affected by foliar diseases, particularly early blight and late blight. This study develops a lightweight convolutional neural network (CNN) to classify potato leaves into three categories: healthy, early blight, and late blight. The proposed model was trained using 2,215 images from the PlantVillage dataset and evaluated on an independent field dataset containing 247 images collected from potato farms in Banja, Awi Zone, Ethiopia. On PlantVillage, the model achieved 99.04% training accuracy, 98.21% validation accuracy, and 98.66% test accuracy. On the field dataset, it achieved 90.28% accuracy. The study also compares the proposed CNN with VGG16 and MobileNetV2 in terms of classification performance and computational efficiency. The proposed model contains 446,787 trainable parameters, occupies approximately 1.70 MB, and requires an average of 5.58 seconds per training epoch in the reported experimental setup, compared with 9.96 seconds for VGG16 and 7.68 seconds for MobileNetV2. The results demonstrate the potential of a compact CNN for potato leaf disease classification and highlight the importance of independent field evaluation, where image conditions are more variable than in controlled benchmark datasets. The proposed approach may support preliminary disease identification for smallholder farmers in Ethiopia and similar agricultural settings.

### 🤖 AI 总结

**一句话总结**：Potato is an important food-security crop in Ethiopia, but its production is affected by foliar diseases, particularly early blight and late blight. This study develops a lightweight convolutional neu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Detection, Potato, Plant, Leaf, Diseases, Convolutional, Neural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20544v1) | [下载PDF](https://arxiv.org/pdf/2610.20544v1.pdf)

---

## [26. Revisiting Simple Baselines for Relational Deep Learning](https://arxiv.org/abs/2610.20534v1)

**作者**：Viet The Nguyen, Vijay Prakash Dwivedi, Gunther Gust  
**分类**：cs.LG  
**发布时间**：2026-10-14

### 📄 论文摘要

Relational deep learning has emerged as a powerful paradigm for learning end-to-end predictive models over relational databases by representing them as temporal heterogeneous graphs. Recent advances based on graph neural networks and Transformers have achieved strong performance across diverse domains. However, the effectiveness of simpler relational baselines remains underexplored, making it difficult to assess how much architectural complexity is needed to achieve strong predictive performance. Motivated by the observation that predictive signals arise from target attributes, relational attributes, and historical labels, we revisit how effectively these signals can be exploited using simple propagation methods. We adapt fixed low-pass feature propagation to relational entity graphs and train an MLP for prediction. The resulting predictions are further refined using Correct-and-Smooth, a graph-based label propagation algorithm that incorporates historical labels over task-specific meta-graphs connecting target entities. Across classification and regression tasks on RelBench, an MLP trained on neighborhood-filtered features outperforms one using only target-entity features on most tasks and recovers a substantial portion of the performance of heterogeneous GNNs. Correct-and-Smooth provides further gains from historical labels, although applying it requires a separately constructed meta-graph because connections among target entities are not directly specified by the relational entity graph. Together, our studies revisit the effectiveness of established propagation methods as simple RDL baselines while identifying canonical meta-graph construction as a key challenge for effective label propagation.

### 🤖 AI 总结

**一句话总结**：Relational deep learning has emerged as a powerful paradigm for learning end-to-end predictive models over relational databases by representing them as temporal heterogeneous graphs. Recent advances b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Revisiting, Simple, Baselines, Relational, Deep, Learning, has, emerged

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20534v1) | [下载PDF](https://arxiv.org/pdf/2610.20534v1.pdf)

---

## [27. The Physics Is the Network: Fast, Training-Free Neural Emulation](https://arxiv.org/abs/2610.20525v1)

**作者**：Luka Todorovic, Kaushal Gianchandani, Sai Ravela  
**分类**：cs.LG, eess.SY, nlin.CD, stat.AP  
**发布时间**：2026-10-14

### 📄 论文摘要

Neural emulation need not require learning a substitute for known physics. We investigate PolyNets that couple a continuous-time neural representation of polynomial dynamics with a simple recurrent network for discrete-time integration. When the governing coefficients are known, the resulting tensor graph requires no training and preserves the prescribed numerical scheme while enabling efficient hardware execution and parallel simulation. Using the one-dimensional Korteweg-de Vries equation, we compare PolyNet with CPU and GPU finite-difference Runge-Kutta solvers and three trained neural models: a state-map emulator, a physics-informed predictor, and a learned-tendency integrator. Analytical soliton solutions provide a reference for amplitude and phase errors across grid resolutions, 10^6 dispersively scaled time steps, ensembles of up to 10^4 trajectories, and varying initial amplitudes. PolyNet achieves accuracy comparable to the numerical solvers, including at amplitudes outside the learned models' training conditions. It combines this fidelity with high GPU throughput, approximately constant over the tested resolution range, and favorable ensemble scaling.

### 🤖 AI 总结

**一句话总结**：Neural emulation need not require learning a substitute for known physics. We investigate PolyNets that couple a continuous-time neural representation of polynomial dynamics with a simple recurrent ne...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Physics, Network, Fast, Training-Free, Neural, Emulation, need, not

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20525v1) | [下载PDF](https://arxiv.org/pdf/2610.20525v1.pdf)

---

## [28. Bayesian Learning to Select Fair Classifiers](https://arxiv.org/abs/2610.20514v1)

**作者**：Saatvik Kher, Hyungrok Do, Judy Zhong 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-14

### 📄 论文摘要

Evaluations of classifiers (AI or human or agents) often assume a batch setting in which every agent produces labels on every example in a test set, which can be expensive or impractical in many contexts. This motivates online policies that adaptively select agents to query as examples arrive and update policies as outcomes are observed. We study the problem of selecting, in an online stream, the agent that best balances (i) predictive performance and (ii) subgroup fairness of a sensitive attribute, and that allows for delayed observations of true class labels. We formulate this as a Bayesian multi-armed bandit problem using Thompson Sampling, explicitly balancing accuracy and fairness. We conduct empirical evaluations on real-world datasets spanning problems involving tabular classifiers, large language models, and human labelers, demonstrating substantial reductions in regret relative to baselines. Our theoretical contributions include guarantees on the performance of the selected agent that incorporate both the accuracy and fairness aspects of the problem.

### 🤖 AI 总结

**一句话总结**：Evaluations of classifiers (AI or human or agents) often assume a batch setting in which every agent produces labels on every example in a test set, which can be expensive or impractical in many conte...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, or, Bayesian, Learning, Select, Fair, Classifiers, Evaluations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20514v1) | [下载PDF](https://arxiv.org/pdf/2610.20514v1.pdf)

---

## [29. Graph-Enhanced Disease Trajectory Discovery and Temporal Endpoint Forecasting from Longitudinal Electronic Health Records](https://arxiv.org/abs/2610.20502v1)

**作者**：Jin-Jia Zheng, Vincent S. Tseng  
**分类**：cs.LG  
**发布时间**：2026-10-14

### 📄 论文摘要

Longitudinal electronic health records (EHRs) can reveal disease-progression structure, while useful forecasting requires leakage-controlled discovery, censor-aware outcomes, and inspectable trajectory evidence. We developed a graph-enhanced framework in MIMIC-IV v3.1 that splits patients before graph construction, learns train-only consecutive-admission transitions, and freezes endpoint-specific branching-motif policies selected on validation data. The final catalog contained 99,527 motifs, and a time-aware Transformer retrieved at most 24 patient-compatible motifs per endpoint through endpoint-specific cross-attention. Across five training seeds, micro-AUPRC increased from 0.9330 to 0.9357, while event-time MAE decreased from 676.9 to 657.7 days (reduction 19.2 days; 95% paired patient-cluster bootstrap CI, 13.8-24.8). Timing effects were heterogeneous: MAE worsened for events within 730 days but improved by 58.9 days for events occurring after 730 days. In an exploratory internal temporal split, branch conditioning reduced conditional event-time MAE by 26.9 days (95% CI, 23.0-30.8) without evidence of better micro-AUPRC. Corrected survival evaluation over the supported 0-2,555-day interval did not establish macro C-index or integrated Brier score superiority over a matched history-only discrete-hazard model. A directed, degree-matched GNN repair substantially improved unseen-edge discovery, yet replacing GNN-derived scores within fixed motif identities did not improve downstream forecasting. These results position branching motifs as structured trajectory context whose main value is long-range timing support rather than uniformly stronger endpoint discrimination, survival prediction, or causal explanation.

### 🤖 AI 总结

**一句话总结**：Longitudinal electronic health records (EHRs) can reveal disease-progression structure, while useful forecasting requires leakage-controlled discovery, censor-aware outcomes, and inspectable trajector...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Graph-Enhanced, Disease, Trajectory, Discovery, Temporal, Endpoint, Forecasting, Longitudinal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20502v1) | [下载PDF](https://arxiv.org/pdf/2610.20502v1.pdf)

---

## [30. Average-Reward Policy Identification from a Single Continuing Trajectory](https://arxiv.org/abs/2610.20486v1)

**作者**：Tongxi Wang  
**分类**：cs.LG  
**发布时间**：2026-10-14

### 📄 论文摘要

In reinforcement learning, an agent must explore an unknown environment to learn how to make good decisions. Unlike methods that can freely sample any state--action pair, an agent learning from a single trajectory must spend additional time navigating between states. It is therefore natural to expect that learning from a single trajectory requires more experience. In this paper, we show that this additional cost is not always necessary. For average-reward reinforcement learning, we develop an algorithm that learns where to collect information while ensuring that the required samples can be obtained efficiently. We establish an upper bound on the number of interactions needed to identify a near-optimal policy. Furthermore, we prove a matching information theoretic lower bound, showing that, for a broad class of environments and at sufficiently high accuracy, learning from a single trajectory is no harder in the worst case than learning with unrestricted access to state action samples. Our results reveal that the additional complexity cost of navigation can be avoided by adapting information gathering requirements to how the environment provides information.

### 🤖 AI 总结

**一句话总结**：In reinforcement learning, an agent must explore an unknown environment to learn how to make good decisions. Unlike methods that can freely sample any state--action pair, an agent learning from a sing...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Average-Reward, Policy, Identification, Single, Continuing, Trajectory, reinforcement, learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.20486v1) | [下载PDF](https://arxiv.org/pdf/2610.20486v1.pdf)

---

