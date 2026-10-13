# arXiv AI 论文日报 | 2026-10-13

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (12 篇)
- [cs.CL](#csCL) (4 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics](https://arxiv.org/abs/2610.13889v1)

**作者**：Weiliang Chen, Song Liao  
**分类**：cs.AI, cs.IR  
**发布时间**：2026-10-09

### 📄 论文摘要

As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execution. To address this gap, we propose RATED (Reliability-Aware Tool Retrieval via Execution Dynamics), a retrieval framework that combines robust semantic matching with dynamic reliability adaptation. RATED employs a frozen dual-encoder with contrastive fine-tuning for semantic matching, and a lightweight contextual bandit module that re-ranks candidates based on real-time execution feedback. This design enables rapid adaptation to runtime tool failures without expensive model retraining. We introduce EcoAgent, a benchmark of 5,172 real-world tools and over 210,000 query-tool pairs for offline retrieval and dynamic reliability evaluation. Experimental results demonstrate that RATED achieves a 52.2% relative MRR improvement over the ToolLLM API retriever on real-world queries, and reduces fault selection rate from 86.2% to 2.9% under severe API outage scenarios with a 30% failure rate, while incurring negligible latency overhead of less than 1 ms over encode-only inference. The code and dataset are available at https://github.com/Elliotes/EcoAgent.

### 🤖 AI 总结

**一句话总结**：As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execut...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, RATED, Reliability-Aware, Tool, Retrieval, via, Execution, Dynamics

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13889v1) | [下载PDF](https://arxiv.org/pdf/2610.13889v1.pdf)

---

## [2. X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems](https://arxiv.org/abs/2610.13886v1)

**作者**：Yeonsung Jung, Zhiyuan Wang, Zifan Wang 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-09

### 📄 论文摘要

Personal agents increasingly connect to services across the web and applications by using tools. As the effects of their actions accumulate and interact across services, unintended or harmful outcomes can arise when agents fulfill benign user requests. Proactively identifying these compositional failures requires systematically exploring diverse cross-service paths. Existing red-teaming methods often simply prompt LLMs to identify potentially harmful paths from task and environment descriptions or decompose harmful objectives specified by humans or LLMs into seemingly benign action combinations. However, generation is biased toward patterns learned during training, potentially favoring familiar tool combinations and leaving novel cross-service interactions underexplored. To address this, we propose X-AgentRed, a self-evolving red-teaming framework that discovers harmful tool call paths through a graph of tool dependencies and expands and refines them using execution feedback. By analyzing each tool's effects, potential harms, and preconditions for execution, the red-teaming agent constructs a directed graph that captures how one tool's effects can satisfy another's execution preconditions. Recipes sampled from this graph are instantiated as realistic scenarios in which agents can produce harmful outcomes. Execution feedback enables self-improvement by diversifying paths that produce harm through tool substitution and refining preconditions at blocked steps in unsuccessful paths to enable further execution. Across four frontier agentic models, X-AgentRed achieves $1.77\times$ the harmful path rate of STAC and explores a more diverse set of tools, yielding $2.99\times$ the tool coverage on average.

### 🤖 AI 总结

**一句话总结**：Personal agents increasingly connect to services across the web and applications by using tools. As the effects of their actions accumulate and interact across services, unintended or harmful outcomes...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, X-AgentRed, Red-Teaming, Personal, Evolving, Multi-Service, Ecosystems, increasingly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13886v1) | [下载PDF](https://arxiv.org/pdf/2610.13886v1.pdf)

---

## [3. Studying Comics at Scale with Artificial Intelligence: The PAGE Framework and Three Studies of American Comics and Japanese Manga](https://arxiv.org/abs/2610.13840v1)

**作者**：Emilio Ferrara  
**分类**：cs.AI, cs.CL, cs.CY  
**发布时间**：2026-10-09

### 📄 论文摘要

Comics are one of the great visual records of the twentieth century: hundreds of thousands of pages in which a mass readership saw its leaders, its wars and its heroes. Most of this record has never been studied as a whole; comics scholarship proceeds one book at a time. We argue that artificial intelligence, including generative models, can change this to the benefit of the medium itself. We propose PAGE, a framework that makes artificial intelligence an instrument for comics research. It parses every scan into panels, text and a bibliographic record; annotates each page with a vision-language model that follows a written codebook, as a human coder would; grounds samples of these readings in human annotation; and explains change across an archive, with estimates controlled for publisher and genre. We demonstrate the framework on 3,929 American comic books (1938--1956) and 87 volumes of Japanese manga, in three studies, each resting on a different capability. The first pairs text search with visual reading to recover how a mass medium portrayed political power. The second measures the page's visual form across an industry and recovers the hand of individual artists. The third follows who speaks across two comics traditions, checked against human annotation. Beyond research, the same instruments can make archives searchable by what is drawn, open comics to blind and low-vision readers, and help preserve fragile collections and credit uncredited artists. We outline a research agenda in which artificial intelligence strengthens the study, preservation and reach of the medium.

### 🤖 AI 总结

**一句话总结**：Comics are one of the great visual records of the twentieth century: hundreds of thousands of pages in which a mass readership saw its leaders, its wars and its heroes. Most of this record has never b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Studying, Comics, Scale, Artificial, Intelligence, PAGE, Framework

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13840v1) | [下载PDF](https://arxiv.org/pdf/2610.13840v1.pdf)

---

## cs.CL

## [4. RSI-Anything: Unlocking Recursive Self-Improvement with World Models](https://arxiv.org/abs/2610.13912v1)

**作者**：Taoyong Cui, Pinxian Zeng, Wanghan Xu 等 11 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-09

### 📄 论文摘要

Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies evolve. We introduce RSI-Anything, a domain-general framework built on JEPA-Anything that uses predictive world models to guide action and learning-data selection. Observed feedback drives policy or workflow improvement and conditional world-model adaptation, while component and compatibility checks govern the retention of updated policy-model pairs. Across diverse computational and scientific domains, RSI-Anything demonstrates substantial gains. In code repair, with the coder fixed, success increases from 26.3% with a static verifier to 29.2% through predictive selection and 31.2% after world-model adaptation, at comparable test usage. Graphical user interface (GUI) evaluations showed higher task completion, while average actions decrease by 39.4%. Across five successive policy versions, laboratory-planning scores more than double from 21.80% to 46.01%. In reaction optimization, RSI-Anything achieves 96.15% mean best observed yield versus 82.16% for Bayesian optimization under the same 40-experiment budget. An end-to-end immune-science application further connects workflow evolution and predictive modeling with therapeutic hypothesis generation. These results demonstrate how predictive world models and retained system updates enable recursive improvement across diverse environments.

### 🤖 AI 总结

**一句话总结**：Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies ev...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RSI-Anything, Unlocking, Recursive, Self-Improvement, World, Models, RSI, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13912v1) | [下载PDF](https://arxiv.org/pdf/2610.13912v1.pdf)

---

## [5. Task Context Shapes Component Roles in Language Models](https://arxiv.org/abs/2610.13895v1)

**作者**：Sovesh Mohapatra, Dani S Bassett  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-10-09

### 📄 论文摘要

Large language models reuse the same attention heads across tasks, but identifying these shared heads does not explain what they do differently in each task. A natural source of inspiration is task-dependent interactions among shared brain regions, which motivate a network view of language-model computation. Here, we compare fixed model components across tasks using identical graph facts, statements specifying which directed connections are present. We measure how interventions affect attention heads and the activation state in later layers (influence), as well as the answer (importance). Task changes redistribute the influence in five open-weight models spanning four families and 1.5-14 billion parameters. In Gemma-2-9B and Qwen3-14B, an activation edit changes an early internal activation vector and switches which fact the model reads while the written instruction stays fixed. The same heads then respond to different graph facts and influence later components differently. For each prompt, we construct two linear response maps, one before the edit and one after it. Each map predicts a later head's response from a measured change in an earlier head. For a separate factual intervention, the map for the corresponding condition reduces mean squared prediction error by 53.6% in Gemma and 5.0% in Qwen compared with the average of the two maps. These findings show that task context changes both which graph facts the shared components respond to and how their outputs affect later computation. A network account may help explain how models use shared parameters to perform different computations. Measurements of task-dependent influence could also guide interventions intended to alter one behavior while preserving others.

### 🤖 AI 总结

**一句话总结**：Large language models reuse the same attention heads across tasks, but identifying these shared heads does not explain what they do differently in each task. A natural source of inspiration is task-de...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Task, Context, Shapes, Component, Roles, Language, Models, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13895v1) | [下载PDF](https://arxiv.org/pdf/2610.13895v1.pdf)

---

## [6. Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer Selection](https://arxiv.org/abs/2610.13821v1)

**作者**：Juan Terven, Diana-Margarita Córdova-Esparza, Ruben Gomez 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-09

### 📄 论文摘要

A useful language model should know when to answer and when to say "I don't know." Can we improve that decision by training the model itself or by training a separate component to check its answers? We study both approaches on Qwen3-14B for factual questions, using a score that rewards correct answers, penalizes mistakes, and allows abstention. Across three training seeds and two held-out confidence thresholds, a learned answer selector improves threshold-averaged utility over the original model's calibrated confidence filter. On TriviaQA, mean coverage increases from 20.2% to 30.9%, while the pooled error rate among scored answers decreases from 23.0% to 14.5% under exact-match grading. The tested reinforcement-learning changes do not establish consistent gains. On NQ-Open, the selector improves threshold-averaged utility over the filter but still performs worse than always abstaining. A partial human-reviewed audit preserves the TriviaQA finding. Our results support learning to select answers in this setting while showing that reliable abstention across datasets remains unresolved.

### 🤖 AI 总结

**一句话总结**：A useful language model should know when to answer and when to say "I don't know." Can we improve that decision by training the model itself or by training a separate component to check its answers? W...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Can, Language, Models, Learn, When, Abstain?, Policy, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13821v1) | [下载PDF](https://arxiv.org/pdf/2610.13821v1.pdf)

---

## [7. Error Rate is Not Enough: Costs of Augmentation in Low-Resource ASR](https://arxiv.org/abs/2610.13807v1)

**作者**：Katsumi Ibaraki, David Chiang  
**分类**：cs.CL  
**发布时间**：2026-10-09

### 📄 论文摘要

Data augmentation is standard practice for low-resource automatic speech recognition (ASR), but its benefits are almost always reported as aggregate error rates, leaving open why and when a method helps. On four low-resource languages and English at five data sizes, we cross two augmentations that modify existing audio (speed perturbation and SpecAugment) with two that modify text transcriptions and synthesize audio from it. We analyze errors at the phoneme level and find that they help for complementary reasons. SpecAugment has the most reliable aggregate improvements, but increases tone and palatalization errors, whereas text-based methods introduce consonant insertions; in combination, each reduces the errors the other introduces. This complementarity is predictable. Tone and palatalization are each signaled by a single acoustic property and occur least frequently in training (lowest training exposure), and text-based methods that flatten word frequency raise their frequency by 37--38%, reversing those errors while further improving aggregate error. The improvement from combining the methods exceeds the sum of their individual improvements; the superadditivity vanishes by 100 hours, limiting the complementarity to the low-resource regime. Where specific error types matter, we recommend selecting augmentation by training exposure and acoustic properties, both measurable before any training.

### 🤖 AI 总结

**一句话总结**：Data augmentation is standard practice for low-resource automatic speech recognition (ASR), but its benefits are almost always reported as aggregate error rates, leaving open why and when a method hel...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Error, Rate, Not, Enough, Costs, Augmentation, Low-Resource

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13807v1) | [下载PDF](https://arxiv.org/pdf/2610.13807v1.pdf)

---

## cs.CV

## [8. Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark](https://arxiv.org/abs/2610.13947v1)

**作者**：Xudong Cai, Ruijie Zhu, Haoliang Shang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-09

### 📄 论文摘要

In this paper, we study physically grounded articulated 3D asset generation---moving the goal from reproducing how objects look to capturing how they move and function. Inspired by the literature on procedural and agentic generation, we present Artisan, a system that extends the latest method Articraft by introducing a multi-agent pipeline with physical simulation feedback, enabling comprehensive attributes beyond geometry, appearance, and physically plausible articulation, such as collision-free motion, stability under gravity, and accurate mass and material properties. Furthermore, we construct a unified benchmark spanning four key aspects: spatial fidelity, physical plausibility, downstream task performance, and overall quality. The benchmark encompasses 100 reference assets from ArtVIP and LightWheel, 50 stability prompts, and 50 ABO objects with reference masses, with protocols evaluating various metrics. Through extensive evaluation of more than 10 representative models, Artisan achieves competitive spatial fidelity while attaining the lowest collision rates and highest stability rates among the evaluated methods. Together, our system and benchmark establish insights for advancing 3D generation towards physically plausible, functionally usable assets.

### 🤖 AI 总结

**一句话总结**：In this paper, we study physically grounded articulated 3D asset generation---moving the goal from reproducing how objects look to capturing how they move and function. Inspired by the literature on p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Multi-Agent, Towards, Physically, Grounded, Articulated, Assets, Pipeline

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13947v1) | [下载PDF](https://arxiv.org/pdf/2610.13947v1.pdf)

---

## [9. InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators](https://arxiv.org/abs/2610.13944v1)

**作者**：Xuanlang Dai, Jiazi Bu, Yujie Zhou 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-09

### 📄 论文摘要

Diffusion/flow models have emerged as the de facto paradigms for image generation, giving rise to a diverse family of modern generators with increasingly heterogeneous architectures and representations. Despite their remarkable generation capabilities, the cross-model alignment of latent representations and the consistency of their underlying denoising dynamics remain underexplored. In this work, we uncover an intriguing cross-model compatibility: independently trained generators exhibit similar latent spatial organization, while directly handing off intermediate states between unaligned models can still preserve coarse visual content. Motivated by these observations, we propose InstantFusion, a lightweight shared latent interface that connects the denoising trajectories of heterogeneous image generators. Specifically, to enable flexible cross-model state translation, model-specific Latent AutoEncoders (LAEs) are introduced to project intermediate states from different generators into a shared latent space and decode them into the latent space of a target generator. This shared space is constrained by two complementary objectives: aligning intermediate states derived from the same image at matched noise levels and synchronizing their corresponding local denoising velocities. Once trained, InstantFusion allows denoising to seamlessly transition across frozen generators without requiring a dedicated mapping for every model pair. The versatility of InstantFusion is demonstrated across acceleration, multi-preference composition, cross-architecture on-policy distillation, and cross-model composition, achieving competitive performance across these diverse settings.

### 🤖 AI 总结

**一句话总结**：Diffusion/flow models have emerged as the de facto paradigms for image generation, giving rise to a diverse family of modern generators with increasingly heterogeneous architectures and representation...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, InstantFusion, Shared, Latent, Interface, Heterogeneous, Image, Generators

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13944v1) | [下载PDF](https://arxiv.org/pdf/2610.13944v1.pdf)

---

## [10. Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback](https://arxiv.org/abs/2610.13941v1)

**作者**：Yucheng Yang, Xiaoxiao Sun, Shusheng Yang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-09

### 📄 论文摘要

Multimodal diffusion transformers (MMDiTs) allow the evolving image to update internal text representations through joint attention. These representations then guide subsequent image updates, raising a question: does this feedback help correct deviations from the prompt, or preserve them? We find that image-to-text (I2T) feedback can preserve the objects and attributes already represented in the evolving image, including errors. Transplanting I2T messages can rescue failures or disrupt successes. At matched intervention strengths, suppressing the influence of I2T feedback improves generation, whereas opposite controls degrade it. These findings motivate Semantic Feedback Guidance (SFG), which suppresses the influence of I2T feedback by guiding away from an auxiliary branch that strengthens this feedback and weakens text-to-image conditioning. The in-place variant, iSFG, directly suppresses I2T feedback and strengthens text-to-image conditioning, requiring no extra model evaluations. Temporal interventions motivate running the SFG branch during the first 20% of image sampling steps, requiring about $1.2\times$ the base NFE without classifier-free guidance (CFG). Experiments across three image-generation backbones show gains in alignment and preference-model scores. On FLUX, adding SFG to CFG raises GenEval from $0.6661$ to $0.7479$; on SD3.5M, iSFG adds $+1.33$ HPSv2.1 over CFG at zero extra NFE. The control also transfers to text-to-video and image-to-video generation, improving VBench scores. Code is available at https://github.com/yyc1215lll-creator/SFG.

### 🤖 AI 总结

**一句话总结**：Multimodal diffusion transformers (MMDiTs) allow the evolving image to update internal text representations through joint attention. These representations then guide subsequent image updates, raising ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Images, Talk, Back, Guiding, MMDiTs, Suppressing, Image-to-Text, Feedback

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13941v1) | [下载PDF](https://arxiv.org/pdf/2610.13941v1.pdf)

---

## [11. Hide and Seek: HIDE Concepts to SEEK explanations for black box models](https://arxiv.org/abs/2610.13935v1)

**作者**：Bhanu Tokas, Rahul Nair, Rockwell Jackson 等 4 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-10-09

### 📄 论文摘要

Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts. Existing concept-based methods can only interpret classification and regression models. They require access to model weights or large concept-annotated datasets, and most methods cannot provide image-level attribution. We propose Hide and Seek (HnS), a new method for concept-level attribution that does not require access to model weights or labeled concept datasets. HnS can interpret a wide range of vision models. Given a concept and image set, HnS retrieves concept-aligned images using a vision-language model, localizes the concept within each image, masks the localized region, and measures attribution from the change in the black-box model's output between the original and masked images. This enables faithful attribution by directly measuring the model's behavior and supporting local attributions. We validated HnS on CelebA and COCO-Stuff. Compared to existing methods, HnS showed better agreement with ground-truth attributions. We demonstrated the applicability of HnS on diverse tasks, including image captioning and satellite image segmentation, where no existing concept attribution method can be used. We provided our anonymous code in the supplementary material.

### 🤖 AI 总结

**一句话总结**：Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hide, Seek, Concepts, explanations, black, box, models, Interpreting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13935v1) | [下载PDF](https://arxiv.org/pdf/2610.13935v1.pdf)

---

## [12. Can machines reason non-verbally?](https://arxiv.org/abs/2610.13925v1)

**作者**：Shaheer U. Saeed, Zion Tse, Gregory Slabaugh 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-09

### 📄 论文摘要

Modern machines can solve equations, follow logic and reason through language, yet they still struggle with problems that require visual non-verbal reasoning. This is evident even in advanced systems such as DeepSeek, ChatGPT and Gemini, which remain limited on visual tasks such as completing abstract patterns or delineating ambiguous regions-of-interest. Unlike explicit intermediate steps in verbal reasoning which can be verified through logic or automated tests, visual reasoning involves implicit intermediate steps with no clear methods for verification. Non-verbal reasoning is therefore challenging to model and, as a result, remains a fundamental limitation of current machine intelligence. Here we introduce GenVerOpt, a general framework that unifies generation, verification and optimisation into a reasoning pipeline for machines. By generating candidate solutions, verifying their correctness, and iteratively refining them, GenVerOpt enables per-sample optimisation rather than relying solely on dataset-level trends captured during model training. This process mirrors human problem-solving where multiple possibilities are imagined, evaluated, and refined until a correct solution emerges. Across diverse domains, GenVerOpt demonstrates capabilities beyond existing systems: it surpasses humans on abstract IQ puzzles, matches clinicians in prostate cancer segmentation, exceeds experts in liver vessel reconstruction and outperforms state-of-the-art approaches in tumour boundary alignment. These results show that machine reasoning can extend beyond language, establishing visual non-verbal reasoning as a foundation for more flexible and generalisable intelligence.

### 🤖 AI 总结

**一句话总结**：Modern machines can solve equations, follow logic and reason through language, yet they still struggle with problems that require visual non-verbal reasoning. This is evident even in advanced systems ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Can, machines, reason, non-verbally?, Modern, solve, equations, follow

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13925v1) | [下载PDF](https://arxiv.org/pdf/2610.13925v1.pdf)

---

## [13. Where to Look Matters: Rethinking Sub-Volume Sampling in 3D Medical Self-supervised Learning](https://arxiv.org/abs/2610.13915v1)

**作者**：Junkai Liu, Le Zhang  
**分类**：cs.CV  
**发布时间**：2026-10-09

### 📄 论文摘要

Self-supervised learning on 3D medical images commonly relies on random sub-volume sampling during pretraining. However, random cropping implicitly treats all spatial regions as equally worth observing, despite anatomical priors and spatial redundancy that make regions inherently unequal in their value for representation learning. To this end, we first show through controlled crop-quality manipulations that better sub-volumes lead to better downstream transfer, revealing the observation policy as an overlooked bottleneck in 3D medical SSL. Motivated by this finding, we revisit sub-volume sampling as a \emph{where-to-look} problem. We propose \textbf{\method}, a plug-and-play framework that replaces random cropping with an offline coarse-to-fine probe bank guided by \textit{anatomy-awareness}, \textit{informativeness}, and \textit{diversity}. We instantiate \method as a lightweight \lite variant using geometric and image-statistical cues, and a diagnostic \feat variant using frozen visual features, to examine whether lightweight volume-intrinsic priors suffice or richer semantic cues reliably provide additional value. Extensive experiments across multiple 3D medical SSL backbones and downstream tasks demonstrate that \method-\lite consistently improves transfer performance over random sampling. Mechanistic analyses further attribute these gains to more anatomically plausible and informative observations, reduced spatial redundancy, more efficient learning dynamics, and more structured representations.

### 🤖 AI 总结

**一句话总结**：Self-supervised learning on 3D medical images commonly relies on random sub-volume sampling during pretraining. However, random cropping implicitly treats all spatial regions as equally worth observin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Where, Look, Matters, Rethinking, Sub-Volume, Sampling, Medical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13915v1) | [下载PDF](https://arxiv.org/pdf/2610.13915v1.pdf)

---

## [14. Beyond the Snowflakes: Disentangling Weather Effects from Confounding Meta-Factors in LiDAR Object Detection](https://arxiv.org/abs/2610.13891v1)

**作者**：Yiming Yang, Jeremy P. Bos  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-10-09

### 📄 论文摘要

Light Detection and Ranging (LiDAR) is critical for autonomous perception, yet its performance is known to degrade in adverse weather. While existing literature models snow as atmospheric noise that degrades performance, our granular evaluation on the WADS-3D and CADC datasets reveals a counter-intuitive phenomenon: detection accuracy consistently improves as snow intensity increases. Through ablation study and meta-information analysis, we reconcile this by confirming that while falling snow acts as noise, its negative impact is outweighed by a dominant, concurrent factor: significantly increased object point count. We hypothesize that this object point count boost acts as a geometric enhancement, driven by snow accumulation increasing vehicle surface area and a shift from specular to diffuse reflectance. Our findings demonstrate that evaluating perception systems using broad weather-severity bins without accounting for correlated object-level data can lead to misleading conclusions about detector robustness. We conclude that accurate evaluation requires decoupling atmospheric noise from surface accumulation effects and outline future research to validate these physical models. The WADS-3D dataset is available at: https://digitalcommons.mtu.edu/wads-3d/.

### 🤖 AI 总结

**一句话总结**：Light Detection and Ranging (LiDAR) is critical for autonomous perception, yet its performance is known to degrade in adverse weather. While existing literature models snow as atmospheric noise that d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Snowflakes, Disentangling, Weather, Effects, Confounding, Meta-Factors, LiDAR

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13891v1) | [下载PDF](https://arxiv.org/pdf/2610.13891v1.pdf)

---

## [15. Tracking the Invisible: Self-Supervised Wheel Track Detection with Thermal-RGB Fusion](https://arxiv.org/abs/2610.13872v1)

**作者**：Yiming Yang, Jeremy P. Bos  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-10-09

### 📄 论文摘要

Accurate detection of drivable area is essential for autonomous driving and advanced driver assistance systems. While state-of-the-art methods focus on general traversability estimation, they prove inadequate for snow-covered roads where following existing wheel tracks offers crucial advantages: improved traction, predictable vehicle dynamics, and verified path stability. To address this, we propose a low-cost, self-supervised approach detecting safety-critical wheel tracks using synchronized RGB-I (RGB + Long-Wave Infrared) imagery. Our method automatically generates training labels by projecting future wheel trajectories from recorded GNSS data. A neural network is designed to identify wheel tracks with the 4-channel RGB-I images from challenging, white-out road surfaces. Experimental results demonstrate the effectiveness of our approach in visually monotonous and featureless adverse environment, offering a robust and cost-effective alternative for winter autonomy. The newly introduced ThermalTrack dataset is available at: https://digitalcommons.mtu.edu/thermaltrack/.

### 🤖 AI 总结

**一句话总结**：Accurate detection of drivable area is essential for autonomous driving and advanced driver assistance systems. While state-of-the-art methods focus on general traversability estimation, they prove in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Tracking, Invisible, Self-Supervised, Wheel, Track, Detection, Thermal-RGB, Fusion

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13872v1) | [下载PDF](https://arxiv.org/pdf/2610.13872v1.pdf)

---

## [16. Make It Flow: Animating Water in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2610.13860v1)

**作者**：Kjell Keune, Florian Hahlbohm, Jannis Möller 等 6 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-10-09

### 📄 论文摘要

Explicit 3D scene representations such as 3D Gaussian Splatting (3DGS) have recently enabled high-quality, real-time novel view synthesis. However, these methods assume static scenes, limiting realism in the presence of dynamic phenomena ubiquitous in real-world environments. While coherent motion (e.g., humans or vehicles) can be captured and reconstructed, high-frequency effects such as flowing water remain intractable under casual capture conditions, where dense multi-view, high-speed acquisition is not feasible. We present a method to animate water in static 3DGS scenes, enabling visually plausible motion without requiring dynamic capture or physical simulation. Our approach estimates 2D optical flow from reference images or model renderings and lifts it into a consistent 3D Eulerian motion field. We propose a cinemagraph-inspired algorithm that applies this motion field to deform Gaussian primitives, producing temporally seamless looping animations. The resulting representation retains real-time rendering performance, significantly enhances perceptual realism, and preserves free-viewpoint navigation within the scene. We evaluate our method on a newly captured dataset of in-the-wild waterfall scenes and demonstrate clear improvements over prior work in dynamic Gaussian splatting and 3D cinemagraph generation in visual quality and computational efficiency.

### 🤖 AI 总结

**一句话总结**：Explicit 3D scene representations such as 3D Gaussian Splatting (3DGS) have recently enabled high-quality, real-time novel view synthesis. However, these methods assume static scenes, limiting realism...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：It, 3D, Make, Flow, Animating, Water, Gaussian, Splatting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13860v1) | [下载PDF](https://arxiv.org/pdf/2610.13860v1.pdf)

---

## [17. Revisiting the Task of Building Damage Assessment by Satellite Imaging](https://arxiv.org/abs/2610.13857v1)

**作者**：Anthony Cioppa, Virgile Blua, Sébastien Piérard 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-09

### 📄 论文摘要

Natural disasters such as earthquakes, tropical storms, and floods cause extensive damage to buildings, and rapid, reliable damage maps are essential to guide emergency response. Automating this task, referred to as building damage assessment (BDA), from satellite imagery, has become an active research topic at the intersection of remote sensing, computer vision, and machine learning, particularly since supervised deep learning methods were shown to outperform earlier handcrafted approaches. Yet, despite a decade of intense activity and the release of several large-scale datasets, the field lacks a shared foundation. This chapter revisits the task of BDA from first principles, organized around three pillars: data, evaluation, and methods. We first clarify the candidate task for- mulations and argue for a sensor-agnostic, instance-based definition that tolerates missing pre-event imagery. We then review existing datasets along the axes of sensing modality, temporal configuration, and geographic coverage. On the evaluation side, we show that prevailing practices, largely based on a single aggregate score, are theoretically fragile, and we lay the foundations of a more informative, ranking-based, multi-score protocol. We further review methods ranging from task-specific deep networks to recent Earth observation foundation models, noticing that generalization to unseen events and regions remains an open difficulty. Finally, we discuss how these elements can inform the organization of a BDA challenge, including cross-validation, challenge, and private data-sharing setups designed to build trust between developers and users.

### 🤖 AI 总结

**一句话总结**：Natural disasters such as earthquakes, tropical storms, and floods cause extensive damage to buildings, and rapid, reliable damage maps are essential to guide emergency response. Automating this task,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Revisiting, Task, Building, Damage, Assessment, Satellite, Imaging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13857v1) | [下载PDF](https://arxiv.org/pdf/2610.13857v1.pdf)

---

## [18. SpatialASM: Internalizing Active Mentalization for Spatial Reasoning](https://arxiv.org/abs/2610.13832v1)

**作者**：Yuhong Liu, Shenxi Wu, Junyi Chi 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-10-09

### 📄 论文摘要

When solving complex spatial reasoning tasks, ordinary humans naturally revisit the scenes from task-relevant viewpoints and mentally reconstruct the spatial layouts from those viewpoints. But can Large Vision-Language Models (LVLMs) proactively think in the same way? We term this ability Active Spatial Mentalization (ASM), an intrinsic component of visual intelligence that remains substantially underdeveloped in current LVLMs. To bridge this gap, we introduce SpatialASM, a scalable framework to internalize ASM into LVLMs through training-time spatial simulation. SpatialASM employs an allocentric novel-view generator to ground hypothetical viewpoints in visual evidence and produces two complementary forms of supervision: i) explicit ASM trajectories that teach LVLMs when and how to adaptively invoke view planning and imagination during spatial reasoning, and ii) automatically-constructed perspective-taking tasks that further strengthens viewpoint-conditioned scene imagination. On seven benchmarks spanning relatively perception-oriented spatial understanding to more challenging tasks requiring multi-image, cross-view and viewpoint-transformation reasoning, SpatialASM yields performance gain on LVLMs of four LVLM backbones in spatial reasoning while retaining their original general vision capabilities. The experimental results demonstrate that our approach improves average accuracy across the seven spatial benchmarks. And the synthesis of ASM trajectories provides a scalable pathway to alleviate the scarcity of spatial Chain-of-Thought (CoT) supervision for eliciting active viewpoint exploration and mental scene simulation.

### 🤖 AI 总结

**一句话总结**：When solving complex spatial reasoning tasks, ordinary humans naturally revisit the scenes from task-relevant viewpoints and mentally reconstruct the spatial layouts from those viewpoints. But can Lar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SpatialASM, Internalizing, Active, Mentalization, Spatial, Reasoning, When, solving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13832v1) | [下载PDF](https://arxiv.org/pdf/2610.13832v1.pdf)

---

## cs.LG

## [19. KL Before and After Mixing: A Round-Complexity Separation in Parallel Sampling](https://arxiv.org/abs/2610.13924v1)

**作者**：Tianyi Wu  
**分类**：cs.LG, cs.IT  
**发布时间**：2026-10-09

### 📄 论文摘要

A parallel sampler can choose at random which coordinates to generate together. For a target $p$ and the output law $q_U$ of a schedule $U$ drawn afresh for each output, we compare the schedule-averaged divergence $\mathbb{E}_U D_{\mathrm{KL}}(p\|q_U)$ with the output-law divergence $D_{\mathrm{KL}}(p\|\mathbb{E}_U q_U)$, in nats. Rounds commit independent draws from exact conditional marginals frozen at the round's start, each output's schedule is drawn before sampling from a finite mixture of schedules, and every scheduled round is charged. For the uniform distribution on binary strings of even length $n$ with $n/2$ ones, the least expected number of rounds at a fixed tolerance $\varepsilon>0$ is $Θ_\varepsilon((\log n)^2)$ under the first criterion but $(e^{-\varepsilon}+o(1))\log_2\ln n$ under the second, and the double-logarithmic order is attainable with the same round count on every run. For this target, a count-state recursion gives the exact least output divergence at every round cap over all causal randomized policies. The separation extends to weighted fixed-count targets with bounded weight ratios and quota fractions bounded away from zero and one, without permutation symmetry, and to the full-support Beta$(1,1)$--Bernoulli target, where the sharp expected cost under the output-law criterion is $(e^{-\varepsilon}/2+o(1))\log_2\log_2n$, attained with rare $n$-round runs. Prior work implies the order of the schedule-averaged cost on the balanced target and its $O_\varepsilon((\log n)^2)$ upper bounds on both extensions.

### 🤖 AI 总结

**一句话总结**：A parallel sampler can choose at random which coordinates to generate together. For a target $p$ and the output law $q_U$ of a schedule $U$ drawn afresh for each output, we compare the schedule-averag...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：KL, Before, After, Mixing, Round-Complexity, Separation, Parallel, Sampling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13924v1) | [下载PDF](https://arxiv.org/pdf/2610.13924v1.pdf)

---

## [20. Designing Protein Structures from Natural Language](https://arxiv.org/abs/2610.13917v1)

**作者**：Joseph Lee, Yanjing Li, Bo Qiang 等 10 位作者  
**分类**：cs.LG, q-bio.BM  
**发布时间**：2026-10-09

### 📄 论文摘要

A central challenge in de novo protein design is generating proteins with desired structural and functional properties. Existing design models typically require a dedicated input representation for each property, limiting the design objectives they support. We develop Prompteina, the first all-atom structure generation model that supports new and broader design objectives specified in natural language, analogous to text-to-image generation. To train Prompteina, we construct Prompteina-Data, a paired text--protein structure dataset of 1.8M structures and 50M+ captions describing global and residue-specific structural and functional properties. We adapt Proteina-Complexa, a pretrained structure generation model, through text-conditioned pretraining and finetuning that aligns residues with their corresponding text. Prompteina outperforms baselines on 15 of 18 structural properties and generates proteins that more closely match descriptions of their intended functions. In binder design, it leads baselines on at least 13 of 20 targets and improves interface confidence by 14\% over the strongest baseline. With iterative in silico feedback, Prompteina's gain over non-iterative generation is 57\% larger than the next-best baseline on the hardest targets. Finally, we experimentally validate Prompteina designs against GM2A, a target with no reported de novo binders. We identify nine binders, with the strongest at an apparent $K_{\mathrm{D}}$ of 107 nM. These results establish natural language as an effective and powerful conditioning interface for protein structure generation.

### 🤖 AI 总结

**一句话总结**：A central challenge in de novo protein design is generating proteins with desired structural and functional properties. Existing design models typically require a dedicated input representation for ea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：de, Designing, Protein, Structures, Natural, Language, central, challenge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13917v1) | [下载PDF](https://arxiv.org/pdf/2610.13917v1.pdf)

---

## [21. Revisiting Tabular Deep Regression: Objectives and the Limits of Global Early Stopping](https://arxiv.org/abs/2610.13909v1)

**作者**：Danil Rudenko, Georgii Bulgakov, Nikolay Kartashev 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-09

### 📄 论文摘要

While deep learning models for tabular data have recently received significant research attention, the choice of objective functions for regression tasks remains an understudied degree of freedom. Several lines of research offer alternatives to the standard Mean Squared Error (MSE), but differences in datasets, backbones, and evaluation protocols make their practical benefits difficult to compare. In this work, we address this gap by performing a systematic re-evaluation of regression objectives across a broad collection of established tabular datasets and multiple neural backbones. Our comparison reveals that many proposed objectives provide limited or inconsistent gains over a properly tuned MSE baseline, while quantile loss yields consistent aggregate improvements over MSE across the tested backbones. We then identify a limitation that remains even with this strong objective: regions with different levels of target noise can reach their best predictive performance at different training epochs. Consequently, a single global early-stopping checkpoint can impose a compromise between uncertainty regions, even when the objective can represent heteroskedastic target distributions. Motivated by this limitation, we introduce a heteroskedasticity-aware extension of quantile loss that uses input-dependent label smoothing as a potential remedy and improves over quantile loss on several backbones. Overall, our results provide a modern empirical picture of regression objectives for tabular deep learning and highlight how differences in optimal stopping times across uncertainty regions can limit the effectiveness of global early stopping. The code is available at https://github.com/yandex-research/tabular-regression.

### 🤖 AI 总结

**一句话总结**：While deep learning models for tabular data have recently received significant research attention, the choice of objective functions for regression tasks remains an understudied degree of freedom. Sev...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Revisiting, Tabular, Deep, Regression, Objectives, Limits, Global

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13909v1) | [下载PDF](https://arxiv.org/pdf/2610.13909v1.pdf)

---

## [22. Prediction Is Not a Sufficient Memory State](https://arxiv.org/abs/2610.13881v1)

**作者**：Robert Jenkinson Alvarez  
**分类**：cs.LG  
**发布时间**：2026-10-09

### 📄 论文摘要

A memory that reproduces every current prediction may still have forgotten how to learn from the next observation. We characterize this distinction for exact cumulative learning and attention. For smooth convex residual losses with unrestricted real features and labels, a continuous recurrent state of fixed dimension exists exactly when the loss is polynomial. With ordinary, unweighted observations, degree $D$ requires precisely $r=\binom{d+D}{D}-1$ coordinates; even among histories with one fixed current predictor, exactly $r-d$ coordinates can remain necessary for continuation. Nonpolynomial losses have unbounded requirements on such equal-prediction histories. Bounded scalar logistic examples retain this obstruction after fixing any finite derivative jet. For ridge regression, the hidden evidence is the design matrix: the exact state costs $dp+d(d+1)/2$, versus $dp$ for the predictor. On a well-conditioned zero-prediction family, optimal $B$-bit compression has average one-update error of order $d^{-1}2^{-2B/s_d}$, $s_d=d(d+1)/2$, even with arbitrary randomized codes. Kernel attention gives a second exact closure classification. The results identify what future updates reveal, rather than proposing a new regression algorithm or asserting trained-model gains.

### 🤖 AI 总结

**一句话总结**：A memory that reproduces every current prediction may still have forgotten how to learn from the next observation. We characterize this distinction for exact cumulative learning and attention. For smo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Prediction, Not, Sufficient, Memory, State, reproduces, every, current

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13881v1) | [下载PDF](https://arxiv.org/pdf/2610.13881v1.pdf)

---

## [23. Partially Informed Stochastic Optimization via Zeroth-Order Residual Tracking](https://arxiv.org/abs/2610.13871v1)

**作者**：El Mahdi Chayti, Alireza Mirrokni, Martin Jaggi  
**分类**：cs.LG  
**发布时间**：2026-10-09

### 📄 论文摘要

Many optimization problems provide direct access to only part of the gradient, while the remaining component must be inferred from function evaluations. This structure arises in performative prediction, performative reinforcement learning, and bilevel optimization with a black-box lower level. We introduce Partially Informed Stochastic Optimization (PISO), which combines the available gradient component with a running estimate of the residual. By centring each zeroth-order observation on this estimate, PISO makes the variance due to random probing depend on the tracking error rather than the residual's magnitude. This yields a randomized sketch iteration with an explicit contraction mechanism and a principled interpretation of momentum. For smooth nonconvex objectives, we establish convergence guarantees that depend on the residual's variation and initial magnitude, without requiring a uniform bound on the unavailable gradient component. With independently sampled function evaluations and Gaussian or spherical probes, PISO attains leading function-evaluation complexities of \(O(d^{2}\varepsilon^{-6})\) under Lipschitz gradients and \(O(d^{2}\varepsilon^{-5})\) under an additional Lipschitz-Hessian assumption. These rates require only one probe direction, two function samples, and one known-component sample per update. The analysis also quantifies how batching trades observations for fewer deployments. Across five settings, PISO variants improve on the tested baselines with comparable oracle access in three, reach a comparable solution faster in bilevel routing, and perform best among methods without response-model derivatives in performative reinforcement learning.

### 🤖 AI 总结

**一句话总结**：Many optimization problems provide direct access to only part of the gradient, while the remaining component must be inferred from function evaluations. This structure arises in performative predictio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Partially, Informed, Stochastic, Optimization, via, Zeroth-Order, Residual, Tracking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13871v1) | [下载PDF](https://arxiv.org/pdf/2610.13871v1.pdf)

---

## [24. Inference-Time Steering Across Scaffolds and Epitopes for Sample-Efficient De Novo Nanobody Design](https://arxiv.org/abs/2610.13844v1)

**作者**：Mason Minot, Simon Friedensohn, Cédric R. Weber  
**分类**：cs.LG  
**发布时间**：2026-10-09

### 📄 论文摘要

Generative molecular design typically relies on over-generation and post-hoc filtering. Inference-time steering methods like Feynman-Kac (FK) steering improve efficiency by biasing trajectories toward high-reward candidates, yet they optimize within a single fixed configuration. In de novo nanobody design, upfront commitment to conditioning choices like scaffold identity or target epitope creates a bottleneck. Since yield varies across these conditions, steering unpromising setups wastes compute. We recast generative condition selection as an inference-time resource-allocation problem. We propose two dynamic budget allocators: a joint Global Sequential Monte Carlo (SMC) formulation that steers and allocates compute across configurations concurrently, and a decoupled approach adapting Batched Successive Elimination (BaSE). Empirically, these dynamic allocators increase the yield of designable candidates per GPU-hour nearly 5$\times$ without sacrificing diversity across distinct therapeutic targets and generative configurations.

### 🤖 AI 总结

**一句话总结**：Generative molecular design typically relies on over-generation and post-hoc filtering. Inference-time steering methods like Feynman-Kac (FK) steering improve efficiency by biasing trajectories toward...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：De, Inference-Time, Steering, Across, Scaffolds, Epitopes, Sample-Efficient, Novo

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13844v1) | [下载PDF](https://arxiv.org/pdf/2610.13844v1.pdf)

---

## [25. Returning to Development States: When Full Sandbox Snapshots Help Coding Agents](https://arxiv.org/abs/2610.13841v1)

**作者**：Daniel Thi Graviet, Tanmay Shah  
**分类**：cs.LG, cs.SE  
**发布时间**：2026-10-09

### 📄 论文摘要

Coding agents often make useful progress before they fail, but retry-from-scratch discards the machine state created along the way. This makes failure recovery an interesting search problem: if intermediate environment states preserve meaningful progress, restoring and branching from them could outperform repeatedly restarting from the initial state. We implement Go-Explore-style search over full Daytona snapshots and find that higher and more efficient solve rates depend mainly on progress that sits outside the repository, such as databases, services, and other runtime state. Our results suggest that full-snapshot search is most effective when long-horizon coding work spans multiple services whose state cannot be reconstructed from a single diff.

### 🤖 AI 总结

**一句话总结**：Coding agents often make useful progress before they fail, but retry-from-scratch discards the machine state created along the way. This makes failure recovery an interesting search problem: if interm...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Returning, Development, States, When, Full, Sandbox, Snapshots, Help

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13841v1) | [下载PDF](https://arxiv.org/pdf/2610.13841v1.pdf)

---

## [26. Specialists Learn Faster: Knowledge Organization in Pre-training Shapes Knowledge Update Efficiency](https://arxiv.org/abs/2610.13835v1)

**作者**：Sheng Zhao, Yuhao Zhu  
**分类**：cs.LG  
**发布时间**：2026-10-09

### 📄 论文摘要

An ideal (language) model must continually update its knowledge. Existing work largely focuses on making these updates efficient after training. We investigate how the organization of time-varying knowledge during pre-training shapes the efficiency of subsequent updates. Models trained on chronologically ordered knowledge specialize in the most recently encountered knowledge; we call them specialists. In contrast, models trained on the same knowledge in randomly shuffled order perform well across all represented time periods; we call them generalists. Surprisingly, specialists require far fewer update steps than generalists to acquire new knowledge. To explain this advantage, we derive a law from first principles that relates update cost to the model's optimization dynamics and that closely predicts empirical results. Guided by these findings, we design a strategy for organizing pre-training data that preserves stable historical knowledge while enabling efficient updates to current knowledge. We also show that the benefits of temporal knowledge organization extend to real-world pre-trained models and existing knowledge update tools, and generalize to other knowledge orderings. Project page: https://horizon-lab.org/specialist/

### 🤖 AI 总结

**一句话总结**：An ideal (language) model must continually update its knowledge. Existing work largely focuses on making these updates efficient after training. We investigate how the organization of time-varying kno...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Specialists, Learn, Faster, Knowledge, Organization, Pre-training, Shapes, Update

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13835v1) | [下载PDF](https://arxiv.org/pdf/2610.13835v1.pdf)

---

## [27. Shared Canonical Component Removal Beyond Expert Views](https://arxiv.org/abs/2610.13819v1)

**作者**：Jose Roberto Tello Ayala, Akl C. Fahed, Roy Perlis 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-09

### 📄 论文摘要

In clinical practice, experts often begin by converting raw inputs into a set of expert features before making a decision. While black-box models trained on raw input can outperform models trained on expert views, it remains unclear what predictive signal the raw model exploits beyond what the expert view captures. We introduce an audit framework to quantify this gap using Shared Canonical Component Removal (SCCR). Unlike standard residualization or concept erasure, SCCR selectively removes only those directions strongly shared between learned raw and expert embeddings.   Evaluations on synthetic data, coronary artery disease (CAD) detection, antidepressant treatment dropout prediction, and skin lesion classification using SkinCon annotations show that SCCR identifies the ways in which expert views are insufficient and recovers residual predictive signal while minimizing redundancy with the expert view.

### 🤖 AI 总结

**一句话总结**：In clinical practice, experts often begin by converting raw inputs into a set of expert features before making a decision. While black-box models trained on raw input can outperform models trained on ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Shared, Canonical, Component, Removal, Beyond, Expert, Views, clinical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13819v1) | [下载PDF](https://arxiv.org/pdf/2610.13819v1.pdf)

---

## [28. TabMF: Learning Dataset Representations with Tabular Foundation Models](https://arxiv.org/abs/2610.13818v1)

**作者**：Rafiq Kamel, Nicolas Atienza, Aziz Fouché 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-09

### 📄 论文摘要

Representations of supervised datasets support higher-level machine-learning tasks such as dataset retrieval and distribution-shift monitoring. However, existing approaches typically rely either on hand-crafted meta-features or on dataset encoders trained specifically for representation learning. We introduce TabMF, a framework that repurposes pretrained tabular foundation models (TFMs) as encoders of supervised datasets. TabMF equips a predictive TFM with an architecture-aware dataset-level readout and adapts the model end-to-end using contrastive post-training on stochastic views of synthetic supervised datasets. We instantiate TabMF on TabICLv2 and TabPFN-2.5 and evaluate the resulting representations across six tasks on unseen real datasets. Simple frozen TFM readouts yield competitive representations, indicating that predictive pretraining already induces substantial dataset-level structure. The two TabMF encoders obtain the strongest aggregate performance among the evaluated learned and classical dataset representations, with particularly strong results in dataset retrieval, compact benchmark construction, and distribution-shift severity assessment.

### 🤖 AI 总结

**一句话总结**：Representations of supervised datasets support higher-level machine-learning tasks such as dataset retrieval and distribution-shift monitoring. However, existing approaches typically rely either on ha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, TabMF, Learning, Dataset, Representations, Tabular, Foundation, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13818v1) | [下载PDF](https://arxiv.org/pdf/2610.13818v1.pdf)

---

## [29. Spanning Diffusion and Flow-based Posterior Sampling via Exact Gaussian Conditioning](https://arxiv.org/abs/2610.13812v1)

**作者**：Teo Deveney, Lea Bogensperger, Hok Shing Wong  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-10-09

### 📄 论文摘要

Flow-matching and diffusion models are increasingly used as priors for linear inverse problems, however, most methods are bespoke to one class of trajectory prior. Plug-and-play methods have been proposed, however these implicitly decorrelate the guided trajectory, resulting in broad priors that can struggle when data is sparse. This work proposes $β$-Flow: a general plug-and-play method indexed by a correlation parameter $β$ that generalises over flow, diffusion, and decorrelated priors, and a confidence parameter $κ$ that controls how strongly the path distribution is enforced. Each step requires only one forward evaluation of a denoising network, followed by a Gaussian conditioning step. This step is an exact Kalman update that is not dependent on network gradients. We show that many existing guided samplers can be interpreted as instances or approximations of our method, each implicitly using a different trajectory prior and operator in place of the Kalman gain. From this viewpoint, we provide a qualitative comparison of methods in terms of their implicit biases and assumptions. We demonstrate consistently state-of-the-art level performance across 7 inverse problems over 4 datasets in terms of PSNR and SSIM. Moreover, we demonstrate the utility of this prior control, by showing that confident high correlations (strict priors) work best when observations are less informative, while low correlation is preferred when observations are more informative, reflecting the complementary roles of the prior and likelihood in Bayesian inference.

### 🤖 AI 总结

**一句话总结**：Flow-matching and diffusion models are increasingly used as priors for linear inverse problems, however, most methods are bespoke to one class of trajectory prior. Plug-and-play methods have been prop...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Spanning, Flow-based, Posterior, Sampling, via, Exact, Gaussian

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13812v1) | [下载PDF](https://arxiv.org/pdf/2610.13812v1.pdf)

---

## [30. QTestBench: A Test Framework for Evaluating LLM-Generated Quantum Code](https://arxiv.org/abs/2610.13811v1)

**作者**：Meriem Terki, Nouhaila Innan, Minghao Shao 等 6 位作者  
**分类**：cs.LG, cs.CL, quant-ph  
**发布时间**：2026-10-09

### 📄 论文摘要

Large language models (LLMs) have shown strong results in classical code generation and are increasingly used to write the unit tests that safeguard that code. Whether they can do the same for quantum software is less clear, because quantum programs are probabilistic, depend on numerical tolerances, and are judged by domain-specific checkers, so a well-formed test can still disagree with the benchmark's verdict. Existing quantum benchmarks measure whether a model produces a correct solution, but not whether its tests can distinguish correct implementations from faulty ones. We introduce QTestBench, a framework that evaluates LLM-generated quantum test suites against independent benchmark checkers, never treating the tests themselves as ground truth. For each task, QTestBench prompts models to produce syntactic, semantic, and behavioral tests, injects candidate solutions at runtime, and compares each test verdict with the checker's label under three validation cohorts, each answering a distinct diagnostic question. We benchmark five LLMs on eight PennyLane QHack challenges and ten Qiskit HumanEval tasks. Generated suites almost always execute, but discrimination lags behind: the best generator reaches a test quality of 0.71 on QHack and 0.34 on Qiskit HumanEval, so executability alone overstates test quality. Oracle-verified synthetic mutants stabilize bug-detection estimates when natural faulty solutions are scarce, as on three of ten Qiskit tasks that yield none. QTestBench offers a reproducible, cross-framework benchmark for the trustworthiness of LLM-generated quantum tests.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) have shown strong results in classical code generation and are increasingly used to write the unit tests that safeguard that code. Whether they can do the same for quantum...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：QTestBench, Test, Framework, Evaluating, LLM-Generated, Quantum, Code, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.13811v1) | [下载PDF](https://arxiv.org/pdf/2610.13811v1.pdf)

---

