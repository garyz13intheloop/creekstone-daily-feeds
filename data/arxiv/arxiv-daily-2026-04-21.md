# arXiv AI 论文日报 | 2026-04-21

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.AI](#csAI) (6 篇)
- [cs.CV](#csCV) (8 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.CL](#csCL) (6 篇)

---

## cs.AI

## [1. MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval](https://arxiv.org/abs/2604.18584v1)

**作者**：Shaden Alshammari, Kevin Wen, Abrar Zainal 等 8 位作者  
**分类**：cs.AI, cs.DL, cs.IR, cs.LG  
**发布时间**：2026-04-20

### 📄 论文摘要

Mathematical problem solving remains a challenging test of reasoning for large language and multimodal models, yet existing benchmarks are limited in size, language coverage, and task diversity. We introduce MathNet, a high-quality, large-scale, multimodal, and multilingual dataset of Olympiad-level math problems together with a benchmark for evaluating mathematical reasoning in generative models and mathematical retrieval in embedding-based systems. MathNet spans 47 countries, 17 languages, and two decades of competitions, comprising 30,676 expert-authored problems with solutions across diverse domains. In addition to the core dataset, we construct a retrieval benchmark consisting of mathematically equivalent and structurally similar problem pairs curated by human experts.   MathNet supports three tasks: (i) Problem Solving, (ii) Math-Aware Retrieval, and (iii) Retrieval-Augmented Problem Solving. Experimental results show that even state-of-the-art reasoning models (78.4% for Gemini-3.1-Pro and 69.3% for GPT-5) remain challenged, while embedding models struggle to retrieve equivalent problems. We further show that retrieval-augmented generation performance is highly sensitive to retrieval quality; for example, DeepSeek-V3.2-Speciale achieves gains of up to 12%, obtaining the highest scores on the benchmark. MathNet provides the largest high-quality Olympiad dataset together with the first benchmark for evaluating mathematical problem retrieval, and we publicly release both the dataset and benchmark at https://mathnet.mit.edu.

### 🤖 AI 总结

**一句话总结**：Mathematical problem solving remains a challenging test of reasoning for large language and multimodal models, yet existing benchmarks are limited in size, language coverage, and task diversity. We in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MathNet, Global, Multimodal, Benchmark, Mathematical, Reasoning, Retrieval, problem

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18584v1) | [下载PDF](https://arxiv.org/pdf/2604.18584v1.pdf)

---

## [2. Benchmarking System Dynamics AI Assistants: Cloud Versus Local LLMs on CLD Extraction and Discussion](https://arxiv.org/abs/2604.18566v1)

**作者**：Terry Leitch  
**分类**：cs.AI, cs.HC, cs.LG  
**发布时间**：2026-04-20

### 📄 论文摘要

We present a systematic evaluation of large language model families -- spanning both proprietary cloud APIs and locally-hosted open-source models -- on two purpose-built benchmarks for System Dynamics AI assistance: the \textbf{CLD Leaderboard} (53 tests, structured causal loop diagram extraction) and the \textbf{Discussion Leaderboard} (interactive model discussion, feedback explanation, and model building coaching).   On CLD extraction, cloud models achieve 77--89\% overall pass rates; the best local model reaches 77\% (Kimi~K2.5~GGUF~Q3, zero-shot engine), matching mid-tier cloud performance. On Discussion, the best local models achieve 50--100\% on model building steps and 47--75\% on feedback explanation, but only 0--50\% on error fixing -- a category dominated by long-context prompts that expose memory limits in local deployments.   A central contribution of this paper is a systematic analysis of \textit{model type effects} on performance: we compare reasoning vs.\ instruction-tuned architectures, GGUF (llama.cpp) vs.\ MLX (mlx\_lm) backends, and quantization levels (Q3 / Q4\_K\_M / MLX-3bit / MLX-4bit / MLX-6bit) across the same underlying model families. We find that backend choice has larger practical impact than quantization level: mlx\_lm does not enforce JSON schema constraints, requiring explicit prompt-level JSON instructions, while llama.cpp grammar-constrained sampling handles JSON reliably but causes indefinite generation on long-context prompts for dense models.   We document the full parameter sweep ($t$, $p$, $k$) for all local models, cleaned timing data (stuck requests excluded), and a practitioner guide for running 671B--123B parameter models on Apple~Silicon.

### 🤖 AI 总结

**一句话总结**：We present a systematic evaluation of large language model families -- spanning both proprietary cloud APIs and locally-hosted open-source models -- on two purpose-built benchmarks for System Dynamics...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Benchmarking, System, Dynamics, Assistants, Cloud, Versus, Local

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18566v1) | [下载PDF](https://arxiv.org/pdf/2604.18566v1.pdf)

---

## [3. ClawEnvKit: Automatic Environment Generation for Claw-Like Agents](https://arxiv.org/abs/2604.18543v1)

**作者**：Xirui Li, Ming Li, Derry Xu 等 7 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-04-20

### 📄 论文摘要

Constructing environments for training and evaluating claw-like agents remains a manual, human-intensive process that does not scale. We argue that what is needed is not just a dataset, but an automated pipeline capable of generating diverse, verified environments on demand. To this end, we introduce ClawEnvKit, an autonomous generation pipeline that instantiates this formalism from natural language descriptions. The pipeline comprises three modules: (1) a parser that extracts structured generation parameters from natural language input; (2) a generator that produces the task specification, tool interface, and scoring configuration; and (3) a validator that enforces feasibility, diversity, structural validity, and internal consistency across the generated environments. Using ClawEnvKit, we construct Auto-ClawEval, the first large-scale benchmark for claw-like agents, comprising 1,040 environments across 24 categories. Empirically, Auto-ClawEval matches or exceeds human-curated environments on coherence and clarity at 13,800x lower cost. Evaluated across 4 model families and 8 agent harness frameworks, we find that harness engineering boosts performance by up to 15.7 percentage points over a bare ReAct baseline, completion remains the primary axis of variation with no model saturating the benchmark, and automated generation enables evaluation at a scale previously infeasible. Beyond static benchmarking, ClawEnvKit enables live evaluation: users describe a desired capability in natural language and obtain a verified environment on demand, turning evaluation into a continuous, user-driven process. The same mechanism serves as an on-demand training environment generator, producing task distributions that adapt to an agent's current weaknesses rather than being bounded by existing user logs.

### 🤖 AI 总结

**一句话总结**：Constructing environments for training and evaluating claw-like agents remains a manual, human-intensive process that does not scale. We argue that what is needed is not just a dataset, but an automat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, ClawEnvKit, Automatic, Environment, Generation, Claw-Like, Constructing, environments

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18543v1) | [下载PDF](https://arxiv.org/pdf/2604.18543v1.pdf)

---

## [4. OGER: A Robust Offline-Guided Exploration Reward for Hybrid Reinforcement Learning](https://arxiv.org/abs/2604.18530v1)

**作者**：Xinyu Ma, Mingzhou Xu, Xuebo Liu 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-20

### 📄 论文摘要

Recent advancements in Reinforcement Learning with Verifiable Rewards (RLVR) have significantly improved Large Language Model (LLM) reasoning, yet models often struggle to explore novel trajectories beyond their initial latent space. While offline teacher guidance and entropy-driven strategies have been proposed to address this, they often lack deep integration or are constrained by the model's inherent capacity. In this paper, we propose OGER, a novel framework that unifies offline teacher guidance and online reinforcement learning through a specialized reward modeling lens. OGER employs multi-teacher collaborative training and constructs an auxiliary exploration reward that leverages both offline trajectories and the model's own entropy to incentivize autonomous exploration. Extensive experiments across mathematical and general reasoning benchmarks demonstrate that OGER significantly outperforms competitive baselines, achieving substantial gains in mathematical reasoning while maintaining robust generalization to out-of-domain tasks. We provide a comprehensive analysis of training dynamics and conduct detailed ablation studies to validate the effectiveness of our entropy-aware reward modulation. Our code is available at https://github.com/ecoli-hit/OGER.git.

### 🤖 AI 总结

**一句话总结**：Recent advancements in Reinforcement Learning with Verifiable Rewards (RLVR) have significantly improved Large Language Model (LLM) reasoning, yet models often struggle to explore novel trajectories b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OGER, Robust, Offline-Guided, Exploration, Reward, Hybrid, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18530v1) | [下载PDF](https://arxiv.org/pdf/2604.18530v1.pdf)

---

## [5. LLM Safety From Within: Detecting Harmful Content with Internal Representations](https://arxiv.org/abs/2604.18519v1)

**作者**：Difan Jiao, Yilun Liu, Ye Yuan 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-20

### 📄 论文摘要

Guard models are widely used to detect harmful content in user prompts and LLM responses. However, state-of-the-art guard models rely solely on terminal-layer representations and overlook the rich safety-relevant features distributed across internal layers. We present SIREN, a lightweight guard model that harnesses these internal features. By identifying safety neurons via linear probing and combining them through an adaptive layer-weighted strategy, SIREN builds a harmfulness detector from LLM internals without modifying the underlying model. Our comprehensive evaluation shows that SIREN substantially outperforms state-of-the-art open-source guard models across multiple benchmarks while using 250 times fewer trainable parameters. Moreover, SIREN exhibits superior generalization to unseen benchmarks, naturally enables real-time streaming detection, and significantly improves inference efficiency compared to generative guard models. Overall, our results highlight LLM internal states as a promising foundation for practical, high-performance harmfulness detection.

### 🤖 AI 总结

**一句话总结**：Guard models are widely used to detect harmful content in user prompts and LLM responses. However, state-of-the-art guard models rely solely on terminal-layer representations and overlook the rich saf...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Safety, Within, Detecting, Harmful, Content, Internal, Representations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18519v1) | [下载PDF](https://arxiv.org/pdf/2604.18519v1.pdf)

---

## [6. A Generalized Synthetic Control Method for Baseline Estimation in Demand Response Services](https://arxiv.org/abs/2604.18469v1)

**作者**：Jonas Sievers, Mardavij Roozbehani  
**分类**：cs.AI  
**发布时间**：2026-04-20

### 📄 论文摘要

Baseline estimation is critical to Demand Response (DR) settlement in electricity markets, yet existing machine learning methods remain limited in predictive performance, while methodologies from causal inference and counterfactual prediction are still underutilized in this domain. We introduce a Generalized Synthetic Control Method that builds on the classical Synthetic Control Method (SCM) from econometrics. While SCM provides a powerful framework for counterfactual estimation, classical SCM remains a static estimator: it fits the treated unit as a combination of contemporaneous donor units and therefore ignores predictable temporal structure in the residual error. We develop a generalized SCM framework that transforms baseline estimation into a dynamic counterfactual prediction problem by augmenting the donor representation with exogenous features, lagged treated load, and selected lagged donor signals. This enriched representation allows the estimator to capture autoregressive dependence, delayed donor-response patterns, and error-correction effects beyond the scope of standard SCM. The framework further accommodates nonlinear predictors when linear weighting is inadequate, with the greatest benefit arising in limited-data settings. Experiments on the Ausgrid smart-meter dataset show consistent improvements over classical SCM and strong benchmark methods, with the dominant performance gains driven by dynamic augmentation.

### 🤖 AI 总结

**一句话总结**：Baseline estimation is critical to Demand Response (DR) settlement in electricity markets, yet existing machine learning methods remain limited in predictive performance, while methodologies from caus...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Generalized, Synthetic, Control, Method, Baseline, Estimation, Demand, Response

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18469v1) | [下载PDF](https://arxiv.org/pdf/2604.18469v1.pdf)

---

## cs.CL

## [7. Dual Alignment Between Language Model Layers and Human Sentence Processing](https://arxiv.org/abs/2604.18563v1)

**作者**：Tatsuki Kuribayashi, Alex Warstadt, Yohei Oseki 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-20

### 📄 论文摘要

A recent study (Kuribayashi et al., 2025) has shown that human sentence processing behavior, typically measured on syntactically unchallenging constructions, can be effectively modeled using surprisal from early layers of large language models (LLMs). This raises the question of whether such advantages of internal layers extend to more syntactically challenging constructions, where surprisal has been reported to underestimate human cognitive effort. In this paper, we begin by exploring internal layers that better estimate human cognitive effort observed in syntactic ambiguity processing in English. Our experiments show that, in contrast to naturalistic reading, later layers better estimate such a cognitive effort, but still underestimate the human data. This dual alignment sheds light on different modes of sentence processing in humans and LMs: naturalistic reading employs a somewhat weak prediction akin to earlier layers of LMs, while syntactically challenging processing requires more fully-contextualized representations, better modeled by later layers of LMs. Motivated by these findings, we also explore several probability-update measures using shallow and deep layers of LMs, showing a complementary advantage to single-layer's surprisal in reading time modeling.

### 🤖 AI 总结

**一句话总结**：A recent study (Kuribayashi et al., 2025) has shown that human sentence processing behavior, typically measured on syntactically unchallenging constructions, can be effectively modeled using surprisal...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Dual, Alignment, Between, Language, Model, Layers, Human, Sentence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18563v1) | [下载PDF](https://arxiv.org/pdf/2604.18563v1.pdf)

---

## [8. GSQ: Highly-Accurate Low-Precision Scalar Quantization for LLMs via Gumbel-Softmax Sampling](https://arxiv.org/abs/2604.18556v1)

**作者**：Alireza Dadgarnia, Soroush Tabesh, Mahdi Nikdan 等 6 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-04-20

### 📄 论文摘要

Weight quantization has become a standard tool for efficient LLM deployment, especially for local inference, where models are now routinely served at 2-3 bits per parameter. The state of the art is currently split into two sets of methods: simple scalar quantization techniques, such as GPTQ or AWQ, which are widely deployed but plateau in accuracy at 3-4 bits per parameter (bpp), and "second-generation" vector- or trellis-quantized methods, such as QTIP, GPTVQ and AQLM, which push the accuracy frontier at low bit-widths but are notoriously hard to implement and to scale, and have gained relatively less traction. In this paper, we ask whether this gap is fundamental, or whether a carefully optimized scalar quantizer can recover most of it. We answer in the affirmative, by introducing GSQ (Gumbel-Softmax Quantization), a post-training scalar quantization method which jointly learns the per-coordinate grid assignments and the per-group scales using a Gumbel-Softmax relaxation of the discrete grid. GSQ matches the cardinality of the relaxation to the small number of levels available in the target bit-width regime (e.g., 3-8 levels for ternary and 3 bpp, respectively), making the relaxation tight and the optimization tractable. Practically, on the standard Llama-3.1-8B/70B-Instruct models, GSQ closes most of the gap between scalar quantization and the QTIP frontier at 2 and 3 bits, while using a symmetric scalar grid with group-wise quantization, and thus fully compatible with existing scalar inference kernels. We further show that GSQ scales to trillion-scale Mixture-of-Experts models such as Kimi-K2.5, where vector-quantized methods are difficult to apply.

### 🤖 AI 总结

**一句话总结**：Weight quantization has become a standard tool for efficient LLM deployment, especially for local inference, where models are now routinely served at 2-3 bits per parameter. The state of the art is cu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, GSQ, Highly-Accurate, Low-Precision, Scalar, Quantization, via, Gumbel-Softmax

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18556v1) | [下载PDF](https://arxiv.org/pdf/2604.18556v1.pdf)

---

## [9. Transition-Matrix Regularization for Next Dialogue Act Prediction in Counselling Conversations](https://arxiv.org/abs/2604.18539v1)

**作者**：Eric Rudolph, Philipp Steigerwald, Jens Albrecht  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-20

### 📄 论文摘要

This paper studies how empirical dialogue-flow statistics can be incorporated into Next Dialogue Act Prediction (NDAP). A KL regularization term is proposed that aligns predicted act distributions with corpus-derived transition patterns. Evaluated on a 60-class German counselling taxonomy using 5-fold cross-validation, this improves macro-F1 by 9--42% relative depending on encoder and substantially improves dialogue-flow alignment. Cross-dataset validation on HOPE suggests that improvements transfer across languages and counselling domains. In systematic ablations across pretrained encoders and architectures, the findings indicate that transition regularization provides consistent gains and disproportionately benefits weaker baseline models. The results suggest that lightweight discourse-flow priors complement pretrained encoders, especially in fine-grained, data-sparse dialogue tasks.

### 🤖 AI 总结

**一句话总结**：This paper studies how empirical dialogue-flow statistics can be incorporated into Next Dialogue Act Prediction (NDAP). A KL regularization term is proposed that aligns predicted act distributions wit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Transition-Matrix, Regularization, Next, Dialogue, Act, Prediction, Counselling, Conversations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18539v1) | [下载PDF](https://arxiv.org/pdf/2604.18539v1.pdf)

---

## [10. MASS-RAG: Multi-Agent Synthesis Retrieval-Augmented Generation](https://arxiv.org/abs/2604.18509v1)

**作者**：Xingchen Xiao, Heyan Huang, Runheng Liu 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-20

### 📄 论文摘要

Large language models (LLMs) are widely used in retrieval-augmented generation (RAG) to incorporate external knowledge at inference time. However, when retrieved contexts are noisy, incomplete, or heterogeneous, a single generation process often struggles to reconcile evidence effectively. We propose \textbf{MASS-RAG}, a multi-agent synthesis approach to retrieval-augmented generation that structures evidence processing into multiple role-specialized agents. MASS-RAG applies distinct agents for evidence summarization, evidence extraction, and reasoning over retrieved documents, and combines their outputs through a dedicated synthesis stage to produce the final answer. This design exposes multiple intermediate evidence views, allowing the model to compare and integrate complementary information before answer generation. Experiments on four benchmarks show that MASS-RAG consistently improves performance over strong RAG baselines, particularly in settings where relevant evidence is distributed across retrieved contexts.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are widely used in retrieval-augmented generation (RAG) to incorporate external knowledge at inference time. However, when retrieved contexts are noisy, incomplete, or het...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, MASS-RAG, Synthesis, Retrieval-Augmented, Generation, Large, language, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18509v1) | [下载PDF](https://arxiv.org/pdf/2604.18509v1.pdf)

---

## [11. LQM: Linguistically Motivated Multidimensional Quality Metrics for Machine Translation](https://arxiv.org/abs/2604.18490v1)

**作者**：Samar M. Magdy, Fakhraddin Alwajih, Abdellah El Mekki 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-20

### 📄 论文摘要

Existing MT evaluation frameworks, including automatic metrics and human evaluation schemes such as Multidimensional Quality Metrics (MQM), are largely language-agnostic. However, they often fail to capture dialect- and culture-specific errors in diglossic languages (e.g., Arabic), where translation failures stem from mismatches in language variety, content coverage, and pragmatic appropriateness rather than surface form alone.We introduce LQM: Linguistically Motivated Multidimensional Quality Metrics for MT. LQM is a hierarchical error taxonomy for diagnosing MT errors through six linguistically grounded levels: sociolinguistics, pragmatics, semantics, morphosyntax, orthography, and graphetics (Figure 1). We construct a bidirectional parallel corpus of 3,850 sentences (550 per variety) spanning seven Arabic dialects (Egyptian, Emirati, Jordanian, Mauritanian, Moroccan, Palestinian, and Yemeni), derived from conversational, culturally rich content. We evaluate six LLMs in a zero-shot setting and conduct expert span-level human annotation using LQM, producing 6,113 labeled error spans across 3,495 unique erroneous sentences, along with severity-weighted quality scores. We complement this analysis with an automatic metric (spBLEU). Though validated here on Arabic, LQM is a language-agnostic framework designed to be easily applied to or adapted for other languages. LQM annotated errors data, prompts, and annotation guidelines are publicly available at https://github.com/UBC-NLP/LQM_MT.

### 🤖 AI 总结

**一句话总结**：Existing MT evaluation frameworks, including automatic metrics and human evaluation schemes such as Multidimensional Quality Metrics (MQM), are largely language-agnostic. However, they often fail to c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LQM, Linguistically, Motivated, Multidimensional, Quality, Metrics, Machine, Translation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18490v1) | [下载PDF](https://arxiv.org/pdf/2604.18490v1.pdf)

---

## [12. Adversarial Humanities Benchmark: Results on Stylistic Robustness in Frontier Model Safety](https://arxiv.org/abs/2604.18487v1)

**作者**：Marcello Galisai, Susanna Cifani, Francesco Giarrusso 等 8 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-20

### 📄 论文摘要

The Adversarial Humanities Benchmark (AHB) evaluates whether model safety refusals survive a shift away from familiar harmful prompt forms. Starting from harmful tasks drawn from MLCommons AILuminate, the benchmark rewrites the same objectives through humanities-style transformations while preserving intent. This extends literature on Adversarial Poetry and Adversarial Tales from single jailbreak operators to a broader benchmark family of stylistic obfuscation and goal concealment. In the benchmark results reported here, the original attacks record 3.84% attack success rate (ASR), while transformed methods range from 36.8% to 65.0%, yielding 55.75% overall ASR across 31 frontier models. Under a European Union AI Act Code-of-Practice-inspired systemic-risk lens, Chemical, biological, radiological and nuclear (CBRN) is the highest bucket. Taken together, this lack of stylistic robustness suggests that current safety techniques suffer from weak generalization: deep understanding of 'non-maleficence' remains a central unresolved problem in frontier model safety.

### 🤖 AI 总结

**一句话总结**：The Adversarial Humanities Benchmark (AHB) evaluates whether model safety refusals survive a shift away from familiar harmful prompt forms. Starting from harmful tasks drawn from MLCommons AILuminate,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Adversarial, Humanities, Benchmark, Results, Stylistic, Robustness, Frontier, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18487v1) | [下载PDF](https://arxiv.org/pdf/2604.18487v1.pdf)

---

## cs.CV

## [13. MUA: Mobile Ultra-detailed Animatable Avatars](https://arxiv.org/abs/2604.18583v1)

**作者**：Heming Zhu, Guoxing Sun, Marc Habermann  
**分类**：cs.CV  
**发布时间**：2026-04-20

### 📄 论文摘要

Building photorealistic, animatable full-body digital humans remains a longstanding challenge in computer graphics and vision. Recent advances in animatable avatar modeling have largely progressed along two directions: improving the fidelity of dynamic geometry and appearance, or reducing computational complexity to enable deployment on resource-constrained platforms, e.g., VR headsets. However, existing approaches fail to achieve both goals simultaneously: Ultra-high-fidelity avatars typically require substantial computation on server-class GPUs, whereas lightweight avatars often suffer from limited surface dynamics, reduced appearance details, and noticeable artifacts. To bridge this gap, we propose a novel animatable avatar representation, termed Wavelet-guided Multi-level Spatial Factorized Blendshapes, and a corresponding distillation pipeline that transfers motion-aware clothing dynamics and fine-grained appearance details from a pre-trained ultra-high-quality avatar model into a compact, efficient representation. By coupling multi-level wavelet spectral decomposition with low-rank structural factorization in texture space, our method achieves up to 2000X lower computational cost and a 10X smaller model size than the original high-quality teacher avatar model, while preserving visually plausible dynamics and appearance details closely resemble those of the teacher model. Extensive comparisons with state-of-the-art methods show that our approach significantly outperforms existing avatar approaches designed for mobile settings and achieves comparable or superior rendering quality to most approaches that can only run on servers. Importantly, our representation substantially improves the practicality of high-fidelity avatars for immersive applications, achieving over 180 FPS on a desktop PC and real-time native on-device performance at 24 FPS on a standalone Meta Quest 3.

### 🤖 AI 总结

**一句话总结**：Building photorealistic, animatable full-body digital humans remains a longstanding challenge in computer graphics and vision. Recent advances in animatable avatar modeling have largely progressed alo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MUA, Mobile, Ultra-detailed, Animatable, Avatars, Building, photorealistic, full-body

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18583v1) | [下载PDF](https://arxiv.org/pdf/2604.18583v1.pdf)

---

## [14. ReCap: Lightweight Referential Grounding for Coherent Story Visualization](https://arxiv.org/abs/2604.18575v1)

**作者**：Aditya Arora, Akshita Gupta, Pau Rodriguez 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-20

### 📄 论文摘要

Story Visualization aims to generate a sequence of images that faithfully depicts a textual narrative that preserve character identity, spatial configuration, and stylistic coherence as the narratives unfold. Maintaining such cross-frame consistency has traditionally relied on explicit memory banks, architectural expansion, or auxiliary language models, resulting in substantial parameter growth and inference overhead. We introduce ReCap, a lightweight consistency framework that improves character stability and visual fidelity without modifying the base diffusion backbone. ReCap's CORE (COnditional frame REferencing) module treats anaphors, in our case pronouns, as visual anchors, activating only when characters are referred to by a pronoun and conditioning on the preceding frame to propagate visual identity. This selective design avoids unconditional cross-frame conditioning and introduces only 149K additional parameters, a fraction of the cost of memory-bank and LLM-augmented approaches. To further stabilize identity, we incorporate SemDrift (Guided Semantic Drift Correction) applied only during training. When text is vague or referential, the denoiser lacks a visual anchor for identity-defining attributes, causing character appearance to drift across frames, SemDrift corrects this by aligning denoiser representations with pretrained DINOv3 visual embeddings, enforcing semantic identity stability at zero inference cost. ReCap outperforms previous state-of-the-art, StoryGPT-V, on the two main benchmarks for story visualization by 2.63% Character-Accuracy on FlintstonesSV and by 5.65% on PororoSV, establishing a new state-of-the-art character consistency on both benchmarks. Furthermore, we extend story visualization to human-centric narratives derived from real films, demonstrating the capability of ReCap beyond stylized cartoon domains.

### 🤖 AI 总结

**一句话总结**：Story Visualization aims to generate a sequence of images that faithfully depicts a textual narrative that preserve character identity, spatial configuration, and stylistic coherence as the narratives...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ReCap, Lightweight, Referential, Grounding, Coherent, Story, Visualization, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18575v1) | [下载PDF](https://arxiv.org/pdf/2604.18575v1.pdf)

---

## [15. Back into Plato's Cave: Examining Cross-modal Representational Convergence at Scale](https://arxiv.org/abs/2604.18572v1)

**作者**：A. Sophia Koepke, Daniil Zverev, Shiry Ginosar 等 4 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-04-20

### 📄 论文摘要

The Platonic Representation Hypothesis suggests that neural networks trained on different modalities (e.g., text and images) align and eventually converge toward the same representation of reality. If true, this has significant implications for whether modality choice matters at all. We show that the experimental evidence for this hypothesis is fragile and depends critically on the evaluation regime. Alignment is measured using mutual nearest neighbors on small datasets ($\approx$1K samples) and degrades substantially as the dataset is scaled to millions of samples. The alignment that remains between model representations reflects coarse semantic overlap rather than consistent fine-grained structure. Moreover, the evaluations in Huh et al. are done in a one-to-one image-caption setting, a constraint that breaks down in realistic many-to-many settings and further reduces alignment. We also find that the reported trend of stronger language models increasingly aligning with vision does not appear to hold for newer models. Overall, our findings suggest that the current evidence for cross-modal representational convergence is considerably weaker than subsequent works have taken it to be. Models trained on different modalities may learn equally rich representations of the world, just not the same one.

### 🤖 AI 总结

**一句话总结**：The Platonic Representation Hypothesis suggests that neural networks trained on different modalities (e.g., text and images) align and eventually converge toward the same representation of reality. If...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Back, Plato's, Cave, Examining, Cross-modal, Representational, Convergence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18572v1) | [下载PDF](https://arxiv.org/pdf/2604.18572v1.pdf)

---

## [16. SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy](https://arxiv.org/abs/2604.18557v1)

**作者**：Wei Yao, Haohan Ma, Hongwen Zhang 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-20

### 📄 论文摘要

Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent human-object-human scenarios. To maintain semantic integrity during motion transfer, we introduce an interaction-preserving retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which faithfully maintains spatial relationships among humans and objects. Building upon this refined data, we propose a single-agent pretraining and adaptation paradigm that bootstraps synergistic collaborative behaviors from abundant single-human data through decentralized training and multi-agent PPO. Finally, we develop a trajectory-conditioned generative policy using a conditional VAE, trained via multi-teacher distillation from motion imitation priors to achieve stable and controllable object-level trajectory execution. Extensive experiments demonstrate that SynAgent significantly outperforms existing baselines in both cooperative imitation and trajectory-conditioned control, while generalizing across diverse object geometries. Codes and data will be available after publication. Project Page: http://yw0208.github.io/synagent

### 🤖 AI 总结

**一句话总结**：Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due to severe data scarcity, complexities in multi-agent coordination, and limited ge...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SynAgent, Generalizable, Cooperative, Humanoid, Manipulation, via, Solo-to-Cooperative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18557v1) | [下载PDF](https://arxiv.org/pdf/2604.18557v1.pdf)

---

## [17. MetaCloak-JPEG: JPEG-Robust Adversarial Perturbation for Preventing Unauthorized DreamBooth-Based Deepfake Generation](https://arxiv.org/abs/2604.18537v1)

**作者**：Tanjim Rahaman Fardin, S M Zunaid Alam, Mahadi Hasan Fahim 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-20

### 📄 论文摘要

The rapid progress of subject-driven text-to-image synthesis, and in particular DreamBooth, has enabled a consent-free deepfake pipeline: an adversary needs only 4-8 publicly available face images to fine-tune a personalized diffusion model and produce photorealistic harmful content. Current adversarial face-protection systems -- PhotoGuard, Anti-DreamBooth, and MetaCloak -- perturb user images to disrupt surrogate fine-tuning, but all share a structural blindness: none backpropagates gradients through the JPEG compression pipeline that every major social-media platform applies before adversary access. Because JPEG quantization relies on round(), whose derivative is zero almost everywhere, adversarial energy concentrates in high-frequency DCT bands that JPEG discards, eliminating 60-80% of the protective signal. We introduce MetaCloak-JPEG, which closes this gap by inserting a Differentiable JPEG (DiffJPEG) layer built on the Straight-Through Estimator (STE): the forward pass applies standard JPEG compression, while the backward pass replaces round() with the identity. DiffJPEG is embedded in a JPEG-aware EOT distribution (~70% of augmentations include DiffJPEG) and a curriculum quality-factor schedule (QF: 95 to 50) inside a bilevel meta-learning loop. Under an l-inf perturbation budget of eps=8/255, MetaCloak-JPEG attains 32.7 dB PSNR, a 91.3% JPEG survival rate, and outperforms PhotoGuard on all 9 evaluated JPEG quality factors (9/9 wins, mean denoising-loss gain +0.125) within a 4.1 GB training-memory budget.

### 🤖 AI 总结

**一句话总结**：The rapid progress of subject-driven text-to-image synthesis, and in particular DreamBooth, has enabled a consent-free deepfake pipeline: an adversary needs only 4-8 publicly available face images to ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MetaCloak-JPEG, JPEG-Robust, Adversarial, Perturbation, Preventing, Unauthorized, DreamBooth-Based, Deepfake

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18537v1) | [下载PDF](https://arxiv.org/pdf/2604.18537v1.pdf)

---

## [18. S2H-DPO: Hardness-Aware Preference Optimization for Vision-Language Models](https://arxiv.org/abs/2604.18512v1)

**作者**：Nitish Shukla, Surgan Jandial, Arun Ross  
**分类**：cs.CV  
**发布时间**：2026-04-20

### 📄 论文摘要

Vision-Language Models (VLMs) have demonstrated remarkable progress in single-image understanding, yet effective reasoning across multiple images remains challenging. We identify a critical capability gap in existing multi-image alignment approaches: current methods focus primarily on localized reasoning with pre-specified image indices (``Look at Image 3 and...''), bypassing the essential skills of global visual search and autonomous cross-image comparison. To address this limitation, we introduce a Simple-to-Hard (S2H) learning framework that systematically constructs multi-image preference data across three hierarchical reasoning levels requiring an increasing level of capabilities: (1) single-image localized reasoning, (2) multi-image localized comparison, and (3) global visual search. Unlike prior work that relies on model-specific attributes, such as hallucinations or attention heuristics, to generate preference pairs, our approach leverages prompt-driven complexity to create chosen/rejected pairs that are applicable across different models. Through extensive evaluations on LLaVA and Qwen-VL models, we show that our diverse multi-image reasoning data significantly enhances multi-image reasoning performance, yielding significant improvements over baseline methods across benchmarks. Importantly, our approach maintains strong single-image reasoning performance while simultaneously strengthening multi-image understanding capabilities, thus advancing the state of the art for holistic visual preference alignment.

### 🤖 AI 总结

**一句话总结**：Vision-Language Models (VLMs) have demonstrated remarkable progress in single-image understanding, yet effective reasoning across multiple images remains challenging. We identify a critical capability...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：S2H-DPO, Hardness-Aware, Preference, Optimization, Vision-Language, Models, VLMs, have

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18512v1) | [下载PDF](https://arxiv.org/pdf/2604.18512v1.pdf)

---

## [19. SemLT3D: Semantic-Guided Expert Distillation for Camera-only Long-Tailed 3D Object Detection](https://arxiv.org/abs/2604.18476v1)

**作者**：Hao Vo, Khoa Vo, Thinh Phan 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-20

### 📄 论文摘要

Camera-only 3D object detection has emerged as a cost-effective and scalable alternative to LiDAR for autonomous driving, yet existing methods primarily prioritize overall performance while overlooking the severe long-tail imbalance inherent in real-world datasets. In practice, many rare but safety-critical categories such as children, strollers, or emergency vehicles are heavily underrepresented, leading to biased learning and degraded performance. This challenge is further exacerbated by pronounced inter-class ambiguity (e.g., visually similar subclasses) and substantial intra-class diversity (e.g., objects varying widely in appearance, scale, pose, or context), which together hinder reliable long-tail recognition. In this work, we introduce SemLT3D, a Semantic-Guided Expert Distillation framework designed to enrich the representation space for underrepresented classes through semantic priors. SemLT3D consists of: (1) a language-guided mixture-of-experts module that routes 3D queries to specialized experts according to their semantic affinity, enabling the model to better disentangle confusing classes and specialize on tail distributions; and (2) a semantic projection distillation pipeline that aligns 3D queries with CLIP-informed 2D semantics, producing more coherent and discriminative features across diverse visual manifestations. Although motivated by long-tail imbalance, the semantically structured learning in SemLT3D also improves robustness under broader appearance variations and challenging corner cases, offering a principled step toward more reliable camera-only 3D perception.

### 🤖 AI 总结

**一句话总结**：Camera-only 3D object detection has emerged as a cost-effective and scalable alternative to LiDAR for autonomous driving, yet existing methods primarily prioritize overall performance while overlookin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, SemLT3D, Semantic-Guided, Expert, Distillation, Camera-only, Long-Tailed, Object

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18476v1) | [下载PDF](https://arxiv.org/pdf/2604.18476v1.pdf)

---

## [20. Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation](https://arxiv.org/abs/2604.18468v1)

**作者**：Tianshi Cao, Jiawei Ren, Yuxuan Zhang 等 15 位作者  
**分类**：cs.CV, cs.AI, cs.GR, cs.LG  
**发布时间**：2026-04-20

### 📄 论文摘要

Closed-loop simulation is a core component of autonomous vehicle (AV) development, enabling scalable testing, training, and safety validation before real-world deployment. Neural scene reconstruction converts driving logs into interactive 3D environments for simulation, but it does not produce complete 3D object assets required for agent manipulation and large-viewpoint novel-view synthesis. To address this challenge, we present Asset Harvester, an image-to-3D model and end-to-end pipeline that converts sparse, in-the-wild object observations from real driving logs into complete, simulation-ready assets. Rather than relying on a single model component, we developed a system-level design for real-world AV data that combines large-scale curation of object-centric training tuples, geometry-aware preprocessing across heterogeneous sensors, and a robust training recipe that couples sparse-view-conditioned multiview generation with 3D Gaussian lifting. Within this system, SparseViewDiT is explicitly designed to address limited-angle views and other real-world data challenges. Together with hybrid data curation, augmentation, and self-distillation, this system enables scalable conversion of sparse AV object observations into reusable 3D assets.

### 🤖 AI 总结

**一句话总结**：Closed-loop simulation is a core component of autonomous vehicle (AV) development, enabling scalable testing, training, and safety validation before real-world deployment. Neural scene reconstruction ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Asset, Harvester, Extracting, Assets, Autonomous, Driving, Logs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18468v1) | [下载PDF](https://arxiv.org/pdf/2604.18468v1.pdf)

---

## cs.LG

## [21. Bounded Ratio Reinforcement Learning](https://arxiv.org/abs/2604.18578v1)

**作者**：Yunke Ao, Le Chen, Bruce D. Lee 等 8 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-20

### 📄 论文摘要

Proximal Policy Optimization (PPO) has become the predominant algorithm for on-policy reinforcement learning due to its scalability and empirical robustness across domains. However, there is a significant disconnect between the underlying foundations of trust region methods and the heuristic clipped objective used in PPO. In this paper, we bridge this gap by introducing the Bounded Ratio Reinforcement Learning (BRRL) framework. We formulate a novel regularized and constrained policy optimization problem and derive its analytical optimal solution. We prove that this solution ensures monotonic performance improvement. To handle parameterized policy classes, we develop a policy optimization algorithm called Bounded Policy Optimization (BPO) that minimizes an advantage-weighted divergence between the policy and the analytic optimal solution from BRRL. We further establish a lower bound on the expected performance of the resulting policy in terms of the BPO loss function. Notably, our framework also provides a new theoretical lens to interpret the success of the PPO loss, and connects trust region policy optimization and the Cross-Entropy Method (CEM). We additionally extend BPO to Group-relative BPO (GBPO) for LLM fine-tuning. Empirical evaluations of BPO across MuJoCo, Atari, and complex IsaacLab environments (e.g., Humanoid locomotion), and of GBPO for LLM fine-tuning tasks, demonstrate that BPO and GBPO generally match or outperform PPO and GRPO in stability and final performance.

### 🤖 AI 总结

**一句话总结**：Proximal Policy Optimization (PPO) has become the predominant algorithm for on-policy reinforcement learning due to its scalability and empirical robustness across domains. However, there is a signifi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bounded, Ratio, Reinforcement, Learning, Proximal, Policy, Optimization, PPO

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18578v1) | [下载PDF](https://arxiv.org/pdf/2604.18578v1.pdf)

---

## [22. When Can LLMs Learn to Reason with Weak Supervision?](https://arxiv.org/abs/2604.18574v1)

**作者**：Salman Rahman, Jingyan Shen, Anna Mordvina 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-20

### 📄 论文摘要

Large language models have achieved significant reasoning improvements through reinforcement learning with verifiable rewards (RLVR). Yet as model capabilities grow, constructing high-quality reward signals becomes increasingly difficult, making it essential to understand when RLVR can succeed under weaker forms of supervision. We conduct a systematic empirical study across diverse model families and reasoning domains under three weak supervision settings: scarce data, noisy rewards, and self-supervised proxy rewards. We find that generalization is governed by training reward saturation dynamics: models that generalize exhibit a prolonged pre-saturation phase during which training reward and downstream performance climb together, while models that saturate rapidly memorize rather than learn. We identify reasoning faithfulness, defined as the extent to which intermediate steps logically support the final answer, as the pre-RL property that predicts which regime a model falls into, while output diversity alone is uninformative. Motivated by these findings, we disentangle the contributions of continual pre-training and supervised fine-tuning, finding that SFT on explicit reasoning traces is necessary for generalization under weak supervision, while continual pre-training on domain data amplifies the effect. Applied together to Llama3.2-3B-Base, these interventions enable generalization across all three settings where the base model previously failed.

### 🤖 AI 总结

**一句话总结**：Large language models have achieved significant reasoning improvements through reinforcement learning with verifiable rewards (RLVR). Yet as model capabilities grow, constructing high-quality reward s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, When, Can, Learn, Reason, Weak, Supervision?, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18574v1) | [下载PDF](https://arxiv.org/pdf/2604.18574v1.pdf)

---

## [23. A multimodal and temporal foundation model for virtual patient representations at healthcare system scale](https://arxiv.org/abs/2604.18570v1)

**作者**：Andrew Zhang, Tong Ding, Sophia J. Wagner 等 11 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-04-20

### 📄 论文摘要

Modern medicine generates vast multimodal data across siloed systems, yet no existing model integrates the full breadth and temporal depth of the clinical record into a unified patient representation. We introduce Apollo, a multimodal temporal foundation model trained and evaluated on over three decades of longitudinal hospital records from a major US hospital system, composed of 25 billion records from 7.2 million patients, representing 28 distinct medical modalities and 12 major medical specialties. Apollo learns a unified representation space integrating over 100 thousand unique medical events in our clinical vocabulary as well as images and clinical text. This "atlas of medical concepts" forms a computational substrate for modeling entire patient care journeys comprised of sequences of structured and unstructured events, which are compressed by Apollo into virtual patient representations. To assess the potential of these whole-patient representations, we created 322 prognosis and retrieval tasks from a held-out test set of 1.4 million patients. We demonstrate the generalized clinical forecasting potential of Apollo embeddings, including predicting new disease onset risk up to five years in advance (95 tasks), disease progression (78 tasks), treatment response (59 tasks), risk of treatment-related adverse events (17 tasks), and hospital operations endpoints (12 tasks). Using feature attribution techniques, we show that model predictions align with clinically-interpretable multimodal biomarkers. We evaluate semantic similarity search on 61 retrieval tasks, and moreover demonstrate the potential of Apollo as a multimodal medical search engine using text and image queries. Together, these modeling capabilities establish the foundation for computable medicine, where the full context of patient care becomes accessible to computational reasoning.

### 🤖 AI 总结

**一句话总结**：Modern medicine generates vast multimodal data across siloed systems, yet no existing model integrates the full breadth and temporal depth of the clinical record into a unified patient representation....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, multimodal, temporal, foundation, model, virtual, patient, representations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18570v1) | [下载PDF](https://arxiv.org/pdf/2604.18570v1.pdf)

---

## [24. A Note on TurboQuant and the Earlier DRIVE/EDEN Line of Work](https://arxiv.org/abs/2604.18555v1)

**作者**：Ran Ben-Basat, Yaniv Ben-Itzhak, Gal Mendelson 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-20

### 📄 论文摘要

This note clarifies the relationship between the recent TurboQuant work and the earlier DRIVE (NeurIPS 2021) and EDEN (ICML 2022) schemes. DRIVE is a 1-bit quantizer that EDEN extended to any $b>0$ bits per coordinate; we refer to them collectively as EDEN.   First, TurboQuant$_{\text{mse}}$ is a special case of EDEN obtained by fixing EDEN's scalar scale parameter to $S=1$. EDEN supports both biased and unbiased quantization, each optimized by a different $S$ (chosen via methods described in the EDEN works). The fixed choice $S=1$ used by TurboQuant is generally suboptimal, although the optimal $S$ for biased EDEN converges to $1$ as the dimension grows; accordingly TurboQuant$_{\text{mse}}$ approaches EDEN's behavior for large $d$.   Second, TurboQuant$_{\text{prod}}$ combines a biased $(b-1)$-bit EDEN step with an unbiased 1-bit QJL quantization of the residual. It is suboptimal in three ways: (1) its $(b-1)$-bit step uses the suboptimal $S=1$; (2) its 1-bit unbiased residual quantization has worse MSE than (unbiased) 1-bit EDEN; (3) chaining a biased $(b-1)$-bit step with a 1-bit unbiased residual step is inferior to unbiasedly quantizing the input directly with $b$-bit EDEN.   Third, some of the analysis in the TurboQuant work mirrors that of the EDEN works: both exploit the connection between random rotations and the shifted Beta distribution, use the Lloyd-Max algorithm, and note that Randomized Hadamard Transforms can replace uniform random rotations.   Experiments support these claims: biased EDEN (with optimized $S$) is more accurate than TurboQuant$_{\text{mse}}$, and unbiased EDEN is markedly more accurate than TurboQuant$_{\text{prod}}$, often by more than a bit (e.g., 2-bit EDEN beats 3-bit TurboQuant$_{\text{prod}}$). We also repeat all accuracy experiments from the TurboQuant paper, showing that EDEN outperforms it in every setup we have tried.

### 🤖 AI 总结

**一句话总结**：This note clarifies the relationship between the recent TurboQuant work and the earlier DRIVE (NeurIPS 2021) and EDEN (ICML 2022) schemes. DRIVE is a 1-bit quantizer that EDEN extended to any $b>0$ bi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Note, TurboQuant, Earlier, DRIVE, EDEN, Line, Work

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18555v1) | [下载PDF](https://arxiv.org/pdf/2604.18555v1.pdf)

---

## [25. Physics-Informed Neural Networks for Biological $2\mathrm{D}{+}t$ Reaction-Diffusion Systems](https://arxiv.org/abs/2604.18548v1)

**作者**：William Lavery, Jodie A. Cochrane, Christian Olesen 等 6 位作者  
**分类**：cs.LG, q-bio.QM  
**发布时间**：2026-04-20

### 📄 论文摘要

Physics-informed neural networks (PINNs) provide a powerful framework for learning governing equations of dynamical systems from data. Biologically-informed neural networks (BINNs) are a variant of PINNs that preserve the known differential operator structure (e.g., reaction-diffusion) while learning constitutive terms via trainable neural subnetworks, enforced through soft residual penalties. Existing BINN studies are limited to $1\mathrm{D}{+}t$ reaction-diffusion systems and focus on forward prediction, using the governing partial differential equation as a regulariser rather than an explicit identification target. Here, we extend BINNs to $2\mathrm{D}{+}t$ systems within a PINN framework that combines data preprocessing, BINN-based equation learning, and symbolic regression post-processing for closed-form equation discovery. We demonstrate the framework's real-world applicability by learning the governing equations of lung cancer cell population dynamics from time-lapse microscopy data, recovering $2\mathrm{D}{+}t$ reaction-diffusion models from experimental observations. The proposed framework is readily applicable to other spatio-temporal systems, providing a practical and interpretable tool for fast analytic equation discovery from data.

### 🤖 AI 总结

**一句话总结**：Physics-informed neural networks (PINNs) provide a powerful framework for learning governing equations of dynamical systems from data. Biologically-informed neural networks (BINNs) are a variant of PI...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：$2, t$, Physics-Informed, Neural, Networks, Biological, mathrm, Reaction-Diffusion

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18548v1) | [下载PDF](https://arxiv.org/pdf/2604.18548v1.pdf)

---

## [26. Wasserstein Distributionally Robust Risk-Sensitive Estimation via Conditional Value-at-Risk](https://arxiv.org/abs/2604.18546v1)

**作者**：Feras Al Taha, Eilyan Bitar  
**分类**：cs.LG, eess.SP, math.OC  
**发布时间**：2026-04-20

### 📄 论文摘要

We propose a distributionally robust approach to risk-sensitive estimation of an unknown signal x from an observed signal y. The unknown signal and observation are modeled as random vectors whose joint probability distribution is unknown, but assumed to belong to a given type-2 Wasserstein ball of distributions, termed the ambiguity set. The performance of an estimator is measured according to the conditional value-at-risk (CVaR) of the squared estimation error. Within this framework, we study the problem of computing affine estimators that minimize the worst-case CVaR over all distributions in the given ambiguity set. As our main result, we show that, when the nominal distribution at the center of the Wasserstein ball is finitely supported, such estimators can be exactly computed by solving a tractable semidefinite program. We evaluate the proposed estimators on a wholesale electricity price forecasting task using real market data and show that they deliver lower out-of-sample CVaR of squared error compared to existing methods.

### 🤖 AI 总结

**一句话总结**：We propose a distributionally robust approach to risk-sensitive estimation of an unknown signal x from an observed signal y. The unknown signal and observation are modeled as random vectors whose join...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Wasserstein, Distributionally, Robust, Risk-Sensitive, Estimation, via, Conditional, Value-at-Risk

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18546v1) | [下载PDF](https://arxiv.org/pdf/2604.18546v1.pdf)

---

## [27. IDOBE: Infectious Disease Outbreak forecasting Benchmark Ecosystem](https://arxiv.org/abs/2604.18521v1)

**作者**：Aniruddha Adiga, Jingyuan Chou, Anshul Chiranth 等 10 位作者  
**分类**：cs.LG, cs.AI, q-bio.PE  
**发布时间**：2026-04-20

### 📄 论文摘要

Epidemic forecasting has become an integral part of real-time infectious disease outbreak response. While collaborative ensembles composed of statistical and machine learning models have become the norm for real-time forecasting, standardized benchmark datasets for evaluating such methods are lacking. Further, there is limited understanding on performance of these methods for novel outbreaks with limited historical data. In this paper, we propose IDOBE, a curated collection of epidemiological time series focused on outbreak forecasting. IDOBE compiles from multiple data repositories spanning over a century of surveillance and across U.S. states and global locations. We perform derivative-based segmentation to generate over 10,000 outbreaks covering multiple outcomes such as cases and hospitalizations for 13 diseases. We consider a variety of information-theoretic and distributional measures to quantify the epidemiological diversity of the dataset. Finally, we perform multi-horizon short-term forecasting (1- to 4-week-ahead) through the progression of the outbreak using 11 baseline models and report on their performance. In addition to standard metrics such as NMSE and MAPE for point forecasts, we include probabilistic scoring rules such as Normalized Weighted Interval Score (NWIS) to quantify the performance. We find that MLP-based methods have the most robust performance, with statistical methods having a slight edge during the pre-peak phase. IDOBE dataset along with baselines are released publicly on https://github.com/NSSAC/IDOBE to enable standardized, reproducible benchmarking of outbreak forecasting methods.

### 🤖 AI 总结

**一句话总结**：Epidemic forecasting has become an integral part of real-time infectious disease outbreak response. While collaborative ensembles composed of statistical and machine learning models have become the no...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：IDOBE, Infectious, Disease, Outbreak, forecasting, Benchmark, Ecosystem, Epidemic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18521v1) | [下载PDF](https://arxiv.org/pdf/2604.18521v1.pdf)

---

## [28. Barrier-enforced multi-objective optimization for direct point and sharp interval forecasting](https://arxiv.org/abs/2604.18492v1)

**作者**：Worachit Amnuaypongsa, Yotsapat Suparanonrat, Pana Wanitchollakit 等 4 位作者  
**分类**：cs.LG, eess.SY  
**发布时间**：2026-04-20

### 📄 论文摘要

This paper proposes a multi-step probabilistic forecasting framework using a single neural-network based model to generate simultaneous point and interval forecasts. Our approach ensures non-crossing prediction intervals (PIs) through a model structure design that strictly satisfy a target coverage probability (PICP) while maximizing sharpness. Unlike existing methods that rely on manual weight tuning for scalarized loss functions, we treat point and PI forecasting as a multi-objective optimization problem, utilizing multi-gradient descent to adaptively select optimal weights. Key innovations include a new PI loss function based on an extended log-barrier with an adaptive hyperparameter to guarantee the coverage, a hybrid architecture featuring a shared temporal model with horizon-specific submodels, and a training strategy. The proposed loss is scale-independent and universally applicable; combined with our training algorithm, the framework eliminates trial-and-error hyperparameter tuning for balancing multiple objectives. Validated by an intra-day solar irradiance forecasting application, results demonstrate that our proposed loss consistently outperforms those in current literature by achieving target coverage with the narrowest PI widths. Furthermore, when compared against LSTM encoder-decoder and Transformer architectures--including those augmented with Chronos foundation models--our method remains highly competitive and can be seamlessly adapted to any deep learning structure.

### 🤖 AI 总结

**一句话总结**：This paper proposes a multi-step probabilistic forecasting framework using a single neural-network based model to generate simultaneous point and interval forecasts. Our approach ensures non-crossing ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Barrier-enforced, multi-objective, optimization, direct, point, sharp, interval, forecasting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18492v1) | [下载PDF](https://arxiv.org/pdf/2604.18492v1.pdf)

---

## [29. Faster by Design: Interactive Aerodynamics via Neural Surrogates Trained on Expert-Validated CFD](https://arxiv.org/abs/2604.18491v1)

**作者**：Nicholas Thumiger, Andrea Bartezzaghi, Mattia Rigotti 等 8 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-20

### 📄 论文摘要

Computational Fluid Dynamics (CFD) is central to race-car aerodynamic development, yet its cost -- tens of thousands of core-hours per high-fidelity evaluation -- severely limits the design space exploration feasible within realistic budgets. AI-based surrogate models promise to alleviate this bottleneck, but progress has been constrained by the limited complexity of public datasets, which are dominated by smoothed passenger-car shapes that fail to exercise surrogates on the thin, complex, highly loaded components governing motorsport performance. This work presents three primary contributions. First, we introduce a high-fidelity RANS dataset built on a parametric LMP2-class CAD model and spanning six operating conditions (map points) covering straight-line and cornering regimes, generated and validated by aerodynamics experts at Dallara to preserve features relevant to industrial motorsport. Second, we present the Gauge-Invariant Spectral Transformer (GIST), a graph-based neural operator whose spectral embeddings encode mesh connectivity to enhance predictions on tightly packed, complex geometries. GIST guarantees discretization invariance and scales linearly with mesh size, achieving state-of-the-art accuracy on both public benchmarks and the proposed race-car dataset. Third, we demonstrate that GIST achieves a level of predictive accuracy suitable for early-stage aerodynamic design, providing a first validation of the concept of interactive design-space exploration -- where engineers query a surrogate in place of the CFD solver -- within industrial motorsport workflows.

### 🤖 AI 总结

**一句话总结**：Computational Fluid Dynamics (CFD) is central to race-car aerodynamic development, yet its cost -- tens of thousands of core-hours per high-fidelity evaluation -- severely limits the design space expl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Faster, Design, Interactive, Aerodynamics, via, Neural, Surrogates, Trained

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18491v1) | [下载PDF](https://arxiv.org/pdf/2604.18491v1.pdf)

---

## [30. An Integrated Deep-Learning Framework for Peptide-Protein Interaction Prediction and Target-Conditioned Peptide Generation with ConGA-PePPI and TC-PepGen](https://arxiv.org/abs/2604.18467v1)

**作者**：Chupei Tang, Junxiao Kong, Moyu Tang 等 8 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-20

### 📄 论文摘要

Motivation: Peptide-protein interactions (PepPIs) are central to cellular regulation and peptide therapeutics, but experimental characterization remains too slow for large-scale screening. Existing methods usually emphasize either interaction prediction or peptide generation, leaving candidate prioritization, residue-level interpretation, and target-conditioned expansion insufficiently integrated. Results: We present an integrated framework for early-stage peptide screening that combines a partner-aware prediction and localization model (ConGA-PepPI) with a target-conditioned generative model (TC-PepGen). ConGA-PepPI uses asymmetric encoding, bidirectional cross-attention, and progressive transfer from pair prediction to binding-site localization, while TC-PepGen preserves target information throughout autoregressive decoding via layerwise conditioning. In five-fold cross-validation, ConGA-PepPI achieved 0.839 accuracy and 0.921 AUROC, with binding-site AUPR values of 0.601 on the protein side and 0.950 on the peptide side, and remained competitive on external benchmarks. Under a controlled length-conditioned benchmark, 40.39% of TC-PepGen peptides exceeded native templates in AlphaFold 3 ipTM, and unconstrained generation retained evidence of target-conditioned signal.

### 🤖 AI 总结

**一句话总结**：Motivation: Peptide-protein interactions (PepPIs) are central to cellular regulation and peptide therapeutics, but experimental characterization remains too slow for large-scale screening. Existing me...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Integrated, Deep-Learning, Framework, Peptide-Protein, Interaction, Prediction, Target-Conditioned

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.18467v1) | [下载PDF](https://arxiv.org/pdf/2604.18467v1.pdf)

---

