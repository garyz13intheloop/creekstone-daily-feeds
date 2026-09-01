# arXiv AI 论文日报 | 2026-09-01

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (8 篇)
- [cs.CV](#csCV) (10 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. OntoAligner-Ensemble: Voting-Based Fusion across Heterogeneous Ontology Alignment Techniques](https://arxiv.org/abs/2608.31137v1)

**作者**：Hamed Babaei Giglou, Sören Auer, Peio Popov 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-31

### 📄 论文摘要

Ontology alignment (OA) has evolved through several methodological paradigms, ranging from lexical and structural aligners to knowledge graph embedding (KGE) models and, more recently, Large Language Model (LLM)-based approaches. Although modern OA frameworks provide unified ecosystems for deploying these heterogeneous aligners, mechanisms for systematically reconciling their complementary and sometimes conflicting predictions remain relatively underexplored. We present OntoAligner-Ensemble, a modular and aligner-agnostic framework that combines candidate correspondences through a configurable two-stage process comprising voting-based fusion strategies followed by post-fusion selection policies. The framework supports any aligner implemented within OntoAligner that produces candidate correspondences, enabling diverse alignment paradigms to be integrated through a unified decision process. To demonstrate its effectiveness, we instantiate the framework using representative lightweight string-aligner, KGE-based, and Retrieval-Augmented Generation aligners powered by both open-weight and API-based LLMs. We evaluate individual aligners and ensemble configurations across eight benchmark tasks from five OAEI tracks spanning biomedical to beyond-equivalence. The results show that ensemble fusion consistently improves the balance between precision and recall and frequently outperforms standalone aligners across diverse domains. Furthermore, our analysis reveals that ensemble composition directly affects the precision-recall trade-off: heterogeneous cross-paradigm ensembles generally improve precision, whereas homogeneous LLM ensembles more often achieve higher overall F1-scores. These findings demonstrate that systematic ensemble learning offers a robust and reproducible strategy for OA while providing practical guidance for selecting ensemble compositions under different alignment scenarios.

### 🤖 AI 总结

**一句话总结**：Ontology alignment (OA) has evolved through several methodological paradigms, ranging from lexical and structural aligners to knowledge graph embedding (KGE) models and, more recently, Large Language ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OntoAligner-Ensemble, Voting-Based, Fusion, across, Heterogeneous, Ontology, Alignment, Techniques

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31137v1) | [下载PDF](https://arxiv.org/pdf/2608.31137v1.pdf)

---

## [2. When Does Bigger Help? A Controlled Study of LLM Scale for Ontology Learning](https://arxiv.org/abs/2608.31118v1)

**作者**：Hamed Babaei Giglou, Sören Auer, Jennifer D'Souza  
**分类**：cs.AI  
**发布时间**：2026-08-31

### 📄 论文摘要

The effect of Large Language Model (LLM) scale on ontology learning (OL) performance remains insufficiently characterized. We present a controlled evaluation of 13 models spanning dense and Mixture-of-Experts variants from the Qwen3.5 and Qwen3.6 lineages, together with proprietary GPT release variants, using the OntoLearner retrieval-augmented generation pipeline. All models are evaluated with the same embedding model, retrieval configuration, prompt templates, decoding settings, datasets, and metrics on term typing, taxonomy discovery, and non-taxonomic relationship extraction across four biomedical and materials science and engineering ontologies. Within the dense Qwen3.5 lineage, increasing parameter count primarily improves precision rather than recall, with the largest gains occurring between 9B and 27B parameters. However, the effect of scale is neither monotonic nor uniform across tasks and domains. Dense 27B models outperform substantially larger sparse models on term typing, whereas larger Mixture-of-Experts models achieve the strongest open-weight results on taxonomy discovery. Non-taxonomic relationship extraction remains difficult across model scales, particularly for the Materials Data Science ontology. Performance differences across matched Qwen variants and proprietary GPT releases further indicate that architecture and model lineage can outweigh nominal parameter count. These findings show that model size alone is an insufficient selection criterion for OL and provide empirical guidance for reproducible LLM-assisted ontology engineering.

### 🤖 AI 总结

**一句话总结**：The effect of Large Language Model (LLM) scale on ontology learning (OL) performance remains insufficiently characterized. We present a controlled evaluation of 13 models spanning dense and Mixture-of...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, When, Does, Bigger, Help?, Controlled, Study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31118v1) | [下载PDF](https://arxiv.org/pdf/2608.31118v1.pdf)

---

## [3. Cross-Regional Grapevine Cold Hardiness Prediction via Learned Multimodal Latent Representations](https://arxiv.org/abs/2608.31097v1)

**作者**：William Solow, Paola Pesantez-Cabrera, Markus Keller 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-31

### 📄 论文摘要

Accurate daily predictions of cold hardiness in woody plants are critical in regions where freezing temperatures can damage dormant buds and reduce seasonal yield. Existing biophysical, hybrid, and deep learning models have shown high predictive accuracy when trained on local data but remain largely site-specific. The limited availability of cold hardiness data, coupled with the lack of principled methods for transferring cold hardiness predictions to new regions and cultivars, has limited the broader adoption and practical utility of these approaches, particularly in data-scarce regions. To address these limitations, we propose a cold hardiness prediction framework that learns a transferable latent representation by capturing region-specific variation through learned embeddings. To enable prediction in previously unseen regions, we infer embeddings from (1) text descriptions of the cultivar and growing region, and (2) limited historical observations, supporting both zero-shot and few-shot transfer. Experiments on datasets from six regions across North America demonstrate that our approach consistently outperforms state-of-the-art cold hardiness prediction methods, yielding more accurate predictions and substantially improving transfer to data-scarce regions.

### 🤖 AI 总结

**一句话总结**：Accurate daily predictions of cold hardiness in woody plants are critical in regions where freezing temperatures can damage dormant buds and reduce seasonal yield. Existing biophysical, hybrid, and de...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Cross-Regional, Grapevine, Cold, Hardiness, Prediction, via, Learned, Multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31097v1) | [下载PDF](https://arxiv.org/pdf/2608.31097v1.pdf)

---

## [4. Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superintelligence](https://arxiv.org/abs/2608.31075v1)

**作者**：Zhiqin Yang, Jingwen Fu, Yuhan Liu 等 19 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-31

### 📄 论文摘要

Recent advances in large reasoning models (LRMs) have shown that reinforcement learning with verifiable rewards (RLVR) can substantially improve reasoning in mathematics and code, where outcomes can be checked automatically. Extending this progress to open-ended and agentic tasks remains difficult because reliable rewards are harder to obtain and direct human supervision cannot keep pace with the scale and complexity of model-generated experience. This paper studies how LRMs can continue to improve as human supervision gradually recedes from the learning loop. We examine two connected dimensions of this problem. The reward axis traces the development from per-instance human judgments to reusable verifiers and rewards that operate even without human feedback. The experience axis examines how learning can progress from human-curated tasks and environments toward self-generated curricula, constructed environments, and autonomous co-evolution. We connect these dimensions through a five-level ladder from L0 to L4 that identifies which parts of the learning process remain under continued human control. Our analysis further highlights the risks introduced by increasingly autonomous rewards and experience generation, including reward hacking, feedback drift, curriculum collapse, and environment errors. Consequently, we also provide the evaluation around three complementary objects: policy capability, feedback fidelity, and experience quality. This analysis provides a structured account of current approaches to scaling LRMs beyond human supervision and the open problems involved in developing self-sustaining learning systems toward superintelligence. Furthermore, we maintain a continuously updated \href{https://github.com/visitworld123/Awesome-Scaling-LRM-Beyond-Human-Supervision}{GitHub repository} to track the latest advances.

### 🤖 AI 总结

**一句话总结**：Recent advances in large reasoning models (LRMs) have shown that reinforcement learning with verifiable rewards (RLVR) can substantially improve reasoning in mathematics and code, where outcomes can b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Scaling, Large, Reasoning, Models, beyond, Human, Supervision, Path

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31075v1) | [下载PDF](https://arxiv.org/pdf/2608.31075v1.pdf)

---

## [5. Wrong Prediction, Right Answer: Recovering Evidence from Collapsed LLM Sequence Scores](https://arxiv.org/abs/2608.31068v1)

**作者**：Qiyao Yan, Chenpeng Wang, Liangming Pan  
**分类**：cs.AI  
**发布时间**：2026-08-31

### 📄 论文摘要

When a large language model fails a reasoning task, it is often assumed to lack the underlying capability. However, this conflates a genuine absence of reasoning with a late-stage output bottleneck. We observe a consistent readout gap across diverse reasoning benchmarks: hidden-state probes successfully decode correct answers even when native sequence scoring completely collapses due to structural biases. To test whether instance-specific logic survives this collapse, we introduce a diagnostic protocol using a minimal, target-label-free additive correction. Fitting just two parameters on as few as 25 unlabeled examples recovers 9--34 accuracy points for Qwen3.5 models, transferring successfully to OLMo-2-1B and Llama-3.1-8B. Crucially, these recovered decisions persist on hard instances unresolved by simple lexical overlap and significantly exceed count-preserving permutation baselines. Our results show that many apparent zero-shot reasoning deficits are expression failures masking intact internal logic, urging a narrower interpretation of benchmark evaluations.

### 🤖 AI 总结

**一句话总结**：When a large language model fails a reasoning task, it is often assumed to lack the underlying capability. However, this conflates a genuine absence of reasoning with a late-stage output bottleneck. W...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Wrong, Prediction, Right, Answer, Recovering, Evidence, Collapsed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31068v1) | [下载PDF](https://arxiv.org/pdf/2608.31068v1.pdf)

---

## cs.CL

## [6. Context-Aware Interleaved Batching for WhisperX](https://arxiv.org/abs/2608.31170v1)

**作者**：Carlos Bain, Max Bain  
**分类**：cs.CL  
**发布时间**：2026-08-31

### 📄 论文摘要

While WhisperX accelerates speech transcription via intra-audio batching, it isolates audio segments, losing the historical context needed for coherent punctuation and terminology transcription. Conversely, standard Whisper retains context sequentially but suffers from slow inference and hallucination loops. To achieve the best of both worlds, we propose Context-Aware Interleaved Batching. By using VAD-derived segment boundaries, our algorithm stabilizes Whisper's text conditioning, allowing us to safely maintain continuous historical context across batched audio segments. As demonstrated on long-form audio benchmarks, this approach reduces Word Error Rate (WER) and improves proper noun transcription, all while maintaining high-throughput inference speeds.

### 🤖 AI 总结

**一句话总结**：While WhisperX accelerates speech transcription via intra-audio batching, it isolates audio segments, losing the historical context needed for coherent punctuation and terminology transcription. Conve...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Context-Aware, Interleaved, Batching, WhisperX, While, accelerates, speech, transcription

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31170v1) | [下载PDF](https://arxiv.org/pdf/2608.31170v1.pdf)

---

## [7. Configurable Semantic Chunking for Biomedical Information Extraction in Retrieval-Augmented Generation](https://arxiv.org/abs/2608.31139v1)

**作者**：Riya Ahuja, Tim Kacprowski, Roya Shiasi Sardoabi  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-08-31

### 📄 论文摘要

BioMedRAG introduced retrieval-augmented generation with a learned chunk scorer for biomedical information extraction. However, it relies on fixed-size chunking which can fragment semantic evidence. We propose a configurable semantic chunking framework that addresses this limitation by combining entity-preserving windows, trigger-centered chunking, proposition-first extraction, tiered trigger prioritization, and hierarchical relation resolution. The framework integrates with BioMedRAG by replacing only the chunk construction stage while preserving the embedding model, learned chunk scorer, generator, and evaluation protocol. We evaluate the framework on biomedical relation extraction benchmarks (GM-CIHT, DDI, ChemProt) and adverse event classification (ADE). On GM-CIHT, the full hybrid configuration achieves 82.6% F1, improving over the fixed-size baseline (74.2% F1) by 8.4 points under our experimental setup. Cross-dataset analysis shows that semantic chunking improves extraction datasets with explicit relation cues, such as GM-CIHT and DDI, while fixed chunking remains competitive or stronger for dense biochemical extraction and binary classification settings such as ChemProt and ADE. By externalizing chunking logic into configuration files, the framework provides an interpretable and adaptable alternative to rigid fixed-size chunking for biomedical RAG pipelines.

### 🤖 AI 总结

**一句话总结**：BioMedRAG introduced retrieval-augmented generation with a learned chunk scorer for biomedical information extraction. However, it relies on fixed-size chunking which can fragment semantic evidence. W...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Configurable, Semantic, Chunking, Biomedical, Information, Extraction, Retrieval-Augmented, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31139v1) | [下载PDF](https://arxiv.org/pdf/2608.31139v1.pdf)

---

## [8. DIASENTINEL: An Auditable Multi-Agent System for Guideline-Grounded Diabetes Risk Screening](https://arxiv.org/abs/2608.31128v1)

**作者**：Yung Wei Shueh, Zhi-Jie Chen, Chia-Hsuan Hsu 等 12 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-31

### 📄 论文摘要

Large language models (LLMs) offer promising clinical decision support but remain vulnerable to hallucinated facts, unsupported recommendations, and citation errors. We present DIASENTINEL, a fully on-premise multi-agent system for one-year type 2 diabetes mellitus (T2DM) risk screening and guideline-grounded report generation from electronic health records (EHRs). The system integrates calibrated risk prediction, deterministic clinical signal extraction, Reciprocal Rank Fusion over American Diabetes Association (ADA) guidelines, and a hybrid verification layer combining rule-based checks with LLM entailment. The demonstration provides a real-time batch-screening dashboard and an interactive patient report interface with cited recommendations, verification results, and raw EHR comparison. DIASENTINEL demonstrates a practical framework for reliable, auditable, and privacy-preserving LLM-based clinical decision support.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) offer promising clinical decision support but remain vulnerable to hallucinated facts, unsupported recommendations, and citation errors. We present DIASENTINEL, a fully on...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Multi-Agent, DIASENTINEL, Auditable, System, Guideline-Grounded, Diabetes, Risk

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31128v1) | [下载PDF](https://arxiv.org/pdf/2608.31128v1.pdf)

---

## [9. PaperGym: Rubric-Centered Evolution for Research-Plan Generation](https://arxiv.org/abs/2608.31119v1)

**作者**：Yuhan Wang, Zhengxi Lu, Yuchen Yan 等 9 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-31

### 📄 论文摘要

Research planning is the decisive capability of AI scientists. Yet a research plan admits no verifiable answer, so reinforcement learning lacks the environment it requires: tasks paired with a critic. Rubrics extracted from scientific papers can supply the critic. Existing pipelines, however, draw the question and the criteria from the same content, so the reward can be earned by paraphrase. The rubric is further compressed into a single scalar per rollout. We introduce PaperGym, a unified framework that turns each research paper into a complete training environment. PaperGym exploits the structure of a paper: the question is synthesized from the research goal and background, while the criteria are derived from the method and experiments. The criteria span methodological innovation and experimental design, and criterion leakage falls to 3.7%, versus 11.90% to 34.10% in existing datasets. Training uses the rubric twice: first as privileged context for OPSD's self-teacher, then as the reward for GRPO. Across Qwen3-1.7B/4B/8B, this schedule outperforms supervised fine-tuning, either stage alone, and the reverse ordering, improving five-benchmark averages by +5.6, +5.0, and +4.8 points. With the recipe held fixed, models trained on PaperGym-20k win 58.1% of three-way comparisons, against 28.2% for RubricHub Science. The trained Qwen3-8B reaches 73.48 on ResearchQA, above the far larger Kimi K2.6. We release the pipeline, the 20,000-instance corpus PaperGym-20k, and the benchmarks PaperGym-Innov and PaperGym-Design.

### 🤖 AI 总结

**一句话总结**：Research planning is the decisive capability of AI scientists. Yet a research plan admits no verifiable answer, so reinforcement learning lacks the environment it requires: tasks paired with a critic....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PaperGym, Rubric-Centered, Evolution, Research-Plan, Generation, Research, planning, decisive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31119v1) | [下载PDF](https://arxiv.org/pdf/2608.31119v1.pdf)

---

## [10. Aspire: Can Models Self-Evolve from Vague Goals?](https://arxiv.org/abs/2608.31111v1)

**作者**：Yuhao Wu, Jingyuan Zhang, Jiajun Shi 等 21 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-31

### 📄 论文摘要

Many important forms of human learning begin with a vague goal, such as "become a better physicist" or "improve at research." Learners must interpret the goal, identify capability gaps, decide how to learn, and determine whether they have actually improved. In contrast, existing work on LLM self-evolution typically begins with tasks and evaluation metrics specified by humans, reducing self-evolution to optimizing an explicit objective rather than deciding what and how to learn. We introduce ASPIRE, a benchmark for vague-goal-driven self-evolution. ASPIRE provides only a natural-language capability goal while downstream evaluation tasks remain hidden. The agent must operationalize the goal by choosing data and update methods, constructing training and validation signals, and deciding when to evaluate. ASPIRE supports both model-weight and agent-harness evolution in a unified interactive environment and evaluates the resulting systems on a hidden, expert-authored set of 520 items spanning six goals. Our experiments show that vague goals redirect search effort toward goal interpretation. Current agents routinely complete training and harness-editing loops, but weight-level gains remain sparse and unstable, and the strongest evolved harness remains below the engineered Qwen-Agent reference. Agents often train on mismatched data and trust narrow self-evaluations, so local gains fail to transfer to hidden evaluation and continued search and training can erase earlier improvements.

### 🤖 AI 总结

**一句话总结**：Many important forms of human learning begin with a vague goal, such as "become a better physicist" or "improve at research." Learners must interpret the goal, identify capability gaps, decide how to ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Aspire, Can, Models, Self-Evolve, Vague, Goals?, Many, important

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31111v1) | [下载PDF](https://arxiv.org/pdf/2608.31111v1.pdf)

---

## [11. Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents](https://arxiv.org/abs/2608.31076v1)

**作者**：Xuehai Wang, Haowei Qin, Tongxin Liu 等 9 位作者  
**分类**：cs.CL, cs.AI, cs.IR, cs.LG, cs.MA, cs.SE  
**发布时间**：2026-08-31

### 📄 论文摘要

Autonomous scientific research agents are increasingly applied to end-to-end scientific workflows, including literature review, data analysis, experimentation, and report generation. However, open-ended research tasks often do not clearly specify the analyses, methods, and success criteria required to complete the task. As a result, agents may miss important analyses, use inappropriate methods, or draw conclusions that are insufficiently supported by evidence. To address the problem, we present AutoSciRub, an evaluation-first framework that induces a task-specific executable rubric before research execution, and uses it to guide execution, criterion-level verification as well as iterative revision. AutoSciRub decomposes an underspecified instruction into atomic scientific goals, grounds them in relevant literature and task-visible data, and synthesizes specific, actionable, and verifiable criteria. The resulting rubric makes implicit experimental and evidential requirements explicit, providing guidance for experiments and analyses. During revision, rubric-guided verification identifies unmet criteria and enables targeted refinement of the research report and its supporting artifacts. On ResearchClawBench, AutoSciRub consistently improves all tested configurations, with an average gain of 2.08 points across three backbone LLMs under the fixed Codex harness and 2.95 points across three agent harnesses using a fixed DeepSeek-V4-Flash backbone. On a randomly sampled 20-task subset of AstaBench E2E Discovery, AutoSciRub further achieves an average improvement of 16.8 points across three agent harnesses, while maintaining or increasing the number of successfully completed tasks. These results demonstrate that evaluation-first guidance provides an effective and generalizable control mechanism for autonomous scientific research (Code: https://github.com/zjunlp/AutoSciRub).

### 🤖 AI 总结

**一句话总结**：Autonomous scientific research agents are increasingly applied to end-to-end scientific workflows, including literature review, data analysis, experimentation, and report generation. However, open-end...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Learning, Evaluate, Before, Improving, Automatic, Rubric, Induction, Research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31076v1) | [下载PDF](https://arxiv.org/pdf/2608.31076v1.pdf)

---

## [12. Improving Information Extraction with Learned Queries](https://arxiv.org/abs/2608.31058v1)

**作者**：Omar Sharif, Soroush Vosoughi, Nikhil Singh  
**分类**：cs.CL  
**发布时间**：2026-08-31

### 📄 论文摘要

When information extraction fails, a natural instinct is to improve the model doing it: for example, by scaling it up or refining its reasoning. In this paper, we show that another part of the pipeline matters at least as much: the queries used to elicit this information. Across four clinical benchmarks and five LLMs, improving the question design alone raises performance by 18.6 F1-score points, i.e. more than using larger extraction models. To make such question design learnable, we introduce List of Questions (LoQ), which generates document-specific question sets, and FeedQ, a feedback-driven optimization method that iteratively refines questions against extraction outcomes. The resulting optimized questions can be used to train lightweight generators: with fine-tuning, 4B-parameter models match or outperform expert-derived baselines and substantially exceed the performance of much larger untuned models. We release a dataset of 12,820 optimized questions to support a broader shift in information extraction research toward treating question design as a first-class problem.

### 🤖 AI 总结

**一句话总结**：When information extraction fails, a natural instinct is to improve the model doing it: for example, by scaling it up or refining its reasoning. In this paper, we show that another part of the pipelin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Improving, Information, Extraction, Learned, Queries, When, fails, natural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31058v1) | [下载PDF](https://arxiv.org/pdf/2608.31058v1.pdf)

---

## [13. When Does Predictor-Based RL Align with Human Perception? A Study of Subjective Rewards in Codec-Based Speech Language Models](https://arxiv.org/abs/2608.31035v1)

**作者**：Joonyong Park, Jerry Li  
**分类**：cs.CL, cs.SD, eess.AS  
**发布时间**：2026-08-31

### 📄 论文摘要

Codec-based text-to-speech (TTS) models make language-model post-training applicable to speech generation, but it remains unclear when learned perceptual predictors can serve as reinforcement learning rewards without losing alignment with human listeners. We study this question with Group Relative Policy Optimization (GRPO) using learned rewards for anime-like speaking style, naturalness, likability, and arousal. To prevent perceptual rewards from being optimized through transcript drift, we introduce a character error rate (CER) zone constraint and compare policy optimization with Best-of-$N$ reranking under the same reward gate. Across single-reward runs, each reward primarily improves its own target metric, showing that subjective predictors are not interchangeable quality surrogates. Multi-rater A/B tests further show uneven human transfer, while a reward-gap analysis separates average transfer from within-axis calibration: signed reward gaps significantly predict listener choices in the pooled analysis, whereas residual CER gaps do not, but per-axis calibration remains heterogeneous. Best-of-8 is a strong human-level baseline and is not clearly worse than GRPO perceptually, suggesting that GRPO should be viewed as amortizing reward-selected behavior into the policy rather than uniformly outperforming reranking. These results support analyzing subjective speech rewards as predictor-axis-base tuples and provide practical diagnostics for selecting rewards before multi-reward speech post-training.

### 🤖 AI 总结

**一句话总结**：Codec-based text-to-speech (TTS) models make language-model post-training applicable to speech generation, but it remains unclear when learned perceptual predictors can serve as reinforcement learning...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, When, Does, Predictor-Based, Align, Human, Perception?, Study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31035v1) | [下载PDF](https://arxiv.org/pdf/2608.31035v1.pdf)

---

## cs.CV

## [14. BRF-GS: Hyperspectral Bidirectional Reflectance Factor Modeling and Image Generation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2608.31159v1)

**作者**：Yiling Yao, Wenjuan Zhang, Bowen Wang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-31

### 📄 论文摘要

The bidirectional reflectance factor (BRF) characterizes the directional radiative properties of terrestrial surfaces. However, existing three-dimensional (3D) radiative transfer models require complex scene construction and computationally intensive radiative transfer solvers, limiting efficient generation of multi-angle hyperspectral reflectance imagery. 3D Gaussian Splatting (3DGS) offers an efficient framework for neural scene representation and novel view synthesis, but its low-order spherical harmonics representation is insufficient for complex directional reflectance, while the high dimensionality and inter-band quality differences of hyperspectral data introduce additional challenges. To address these challenges, we propose BRF-GS, a 3DGS-based framework for BRF modeling and hyperspectral reflectance image generation. BRF-GS introduces a hybrid BRDF-driven kernel to represent complex directional reflectance, selects geometry-reliable spectral bands for robust 3D scene initialization, and adopts a two-stage training strategy that decouples geometry optimization from spectral modeling. We further construct the AIR-BRF dataset, a multi-angle hyperspectral directional reflectance dataset comprising three scenes with diverse natural and artificial targets. Experiments demonstrate that BRF-GS achieves superior spatial and spectral fidelity and accurately reproduces characteristic view-dependent BRF responses. The proposed framework provides an efficient data-driven approach for BRF modeling and multi-angle hyperspectral reflectance image generation in remote sensing scenes.

### 🤖 AI 总结

**一句话总结**：The bidirectional reflectance factor (BRF) characterizes the directional radiative properties of terrestrial surfaces. However, existing three-dimensional (3D) radiative transfer models require comple...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BRF-GS, Hyperspectral, Bidirectional, Reflectance, Factor, Modeling, Image, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31159v1) | [下载PDF](https://arxiv.org/pdf/2608.31159v1.pdf)

---

## [15. BLARM: Animating 3D Objects from Video via Blending Latent Rigid Motion Primitives](https://arxiv.org/abs/2608.31113v1)

**作者**：Pradyumn Goyal, Yizhak Ben-Shabat, Hsueh-Ti Derek Liu 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-31

### 📄 论文摘要

We introduce BLARM, a feed-forward method for video-driven 3D mesh animation. Given a monocular video and a static object mesh, BLARM predicts a temporally coherent animated mesh whose motion follows the video. Rather than relying on explicit rigs or directly regressing high-dimensional vertex motion, we represent animation using a compact set of learned, time-varying rigid motion components and time-invariant vertex-to-component skinning weights. This yields a low-dimensional deformation space without requiring skeletons, cages, skinning weights, or rig annotations. Our architecture conditions geometry-derived deformation latents on video features through factorized spatial-temporal attention, then decodes rigid transformations blended by predicted skinning weights. Trained with trajectory reconstruction, entropy regularization, and motion-aware contrastive learning, BLARM produces accurate and temporally stable animations while recovering compact, interpretable motion structure from monocular video.

### 🤖 AI 总结

**一句话总结**：We introduce BLARM, a feed-forward method for video-driven 3D mesh animation. Given a monocular video and a static object mesh, BLARM predicts a temporally coherent animated mesh whose motion follows ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, BLARM, Animating, Objects, Video, via, Blending, Latent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31113v1) | [下载PDF](https://arxiv.org/pdf/2608.31113v1.pdf)

---

## [16. VeriCam: A Verification Baseline for the Classification of Unknown Data](https://arxiv.org/abs/2608.31107v1)

**作者**：Lucas Wojcik, Gabriel E. Lima, Sergio M. Silva 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-31

### 📄 论文摘要

The advent of foundation models have enabled a new era in zero-shot classification. Yet, key challenges persist. Despite their impressive generalization power that leverages the immense pre-training knowledge, both foundation models for image and text as well as vision-text hybrids lack the representational power needed for fine-grained, minutiae-based class separation that some real-world tasks require. To address the current gaps in the literature, we propose VeriCam, a pipeline designed to learn highly specialized features that enable classification of unknown classes in unseen data. VeriCam works by leveraging the representation power of image models trained for the verification task, where the model develops an intricate feature space that incorporates fine-grained details. By training a model to discriminate between pairs of images from the same and different classes, a relational graph is constructed, representing the class relationships between data points. We then present two approaches for graph clustering: a naive algorithm and a specific setup for the Leiden graph clustering algorithm. The pipeline is validated on the LPLCv2 dataset, which comprises real-world traffic surveillance images. We show that the dataset carries an inherent capture device bias that is posed as a generalization challenge for downstream License Plate recognition tasks such as OCR. As such, we dynamically identify capture devices with a label-agnostic approach, enabling the construction of a fair and unbiased benchmark. In the cross-device scenario, our pipeline reaches an F1-Score of 93.45 in the verification baseline and a V-Measure score of 80.13 in the clustering step. All code is publicly available at https://github.com/lmlwojcik/VeriCam

### 🤖 AI 总结

**一句话总结**：The advent of foundation models have enabled a new era in zero-shot classification. Yet, key challenges persist. Despite their impressive generalization power that leverages the immense pre-training k...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, VeriCam, Verification, Baseline, Classification, Unknown, Data, advent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31107v1) | [下载PDF](https://arxiv.org/pdf/2608.31107v1.pdf)

---

## [17. One Adapter, Many Tasks: Task-Conditioned Feature Transformations for Continual Learning](https://arxiv.org/abs/2608.31096v1)

**作者**：Yunxiang Fu, Meng Lou, Yizhou Yu  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-08-31

### 📄 论文摘要

Class-incremental learning (CIL) requires a model to incrementally learn tasks that contain new classes without accessing earlier training data while preserving the ability to recognize all seen classes. Recently, pretrained-model-based approaches have become prevalent by adapting a frozen backbone with additional lightweight trainable modules. Existing methods, however, exhibit limitations: task-specific adapters learn explicit per-task representations but are parameter- and computation-inefficient, while LoRA-based merging methods combine per-task LoRA parameters into a single model whose static aggregated weights cause representation interference during inference. To address these problems, we present \textbf{FACET}: task-conditioned \textbf{F}e\textbf{A}ture transformation with \textbf{C}ondition\textbf{E}d feature consis\textbf{T}ency, achieving excellent parameter efficiency while producing highly discriminative features during inference. When continually trained on a task sequence, FACET learns a single shared adapter that employs a dynamic task-conditioned feature transformation, shaping the overall feature distribution of the adapter into a mixture of overlap-reduced task-specific components. On the other hand, we propose an efficient replay-free task-conditioned feature consistency loss, aiming to mitigate catastrophic forgetting of the learned mixture distribution in the adapter's feature space. Even when maintaining only a single adapter, FACET demonstrates robust scalability. On both very long task sequences (e.g., 200 tasks) and standard short task sequences (e.g., 20 tasks), our method achieves superior performance while using significantly fewer trainable parameters and GFLOPs. The code will be made open source upon acceptance.

### 🤖 AI 总结

**一句话总结**：Class-incremental learning (CIL) requires a model to incrementally learn tasks that contain new classes without accessing earlier training data while preserving the ability to recognize all seen class...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：One, Adapter, Many, Tasks, Task-Conditioned, Feature, Transformations, Continual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31096v1) | [下载PDF](https://arxiv.org/pdf/2608.31096v1.pdf)

---

## [18. Robust retinal biometrics for patient identity verification and retrieval across age and imaging devices](https://arxiv.org/abs/2608.31094v1)

**作者**：Jose D. Vargas-Quiros, Dennis Bontempi, Jeroen Vermeulen 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-31

### 📄 论文摘要

Patient identity errors can compromise longitudinal medical records, research databases, and downstream clinical decisions. We present a retinal biometric system for verifying claimed identities and retrieving the correct identity from color fundus images. We trained a 512-dimensional metric-learning encoder combining a ConvNeXtV2 backbone with ArcFace and triplet losses on 227,004 images from 21,851 patient-eye identities in the Rotterdam Study, spanning multiple imaging devices and up to 32.6 years of follow-up. The system was evaluated on held-out Rotterdam Study data and externally on the UK Biobank and Age-Related Eye Disease Study (AREDS). Before evaluation, we used the model to screen for identity inconsistencies and manually adjudicated flagged images, identifying incorrect assignments in 0.588% of Rotterdam Study images, 0.259% of UK Biobank images, and 0.164% of AREDS images. In retrospective-only verification after removing near-duplicate images, the system achieved AUROCs of 0.9998, 0.9997, and 0.9998 in the Rotterdam Study, UK Biobank, and AREDS, respectively. For identity retrieval using only previously acquired images, Recall@1 was 99.7%, 97.2%, and 97.6%, respectively, from galleries averaging 4436-8510 identities; the correct identity appeared among the top five results in at least 98.6% of cases. Performance remained robust across imaging devices and long follow-up intervals, while lower image quality and inconsistent retinal fields accounted for most failures. These findings establish retinal anatomy as a durable biometric signal, useful for safeguarding the integrity of longitudinal imaging records.

### 🤖 AI 总结

**一句话总结**：Patient identity errors can compromise longitudinal medical records, research databases, and downstream clinical decisions. We present a retinal biometric system for verifying claimed identities and r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Robust, retinal, biometrics, patient, identity, verification, retrieval, across

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31094v1) | [下载PDF](https://arxiv.org/pdf/2608.31094v1.pdf)

---

## [19. Real-Time Video Anomaly Detection Using YOLO Pose Estimation and CLIP-Based Semantic Scoring](https://arxiv.org/abs/2608.31074v1)

**作者**：Vanodhya G. Warnasooriya, Amir Hajian, Watchara Ruangsang 等 4 位作者  
**分类**：cs.CV, cs.AI, eess.IV  
**发布时间**：2026-08-31

### 📄 论文摘要

We propose a lightweight two-stage framework for real-time video anomaly detection. The first stage employs YOLO v11n-pose to detect persons and extract seventeen skeletal keypoints in a single forward pass. The second stage encodes each cropped person region through CLIP ViT-B/32 and computes cosine similarity against predefined textual descriptions of anomalous behaviors. This architecture eliminates the need for optical flow, standalone pose estimators, and density-based scoring modules. Experiments on CUHK Avenue, ShanghaiTech Campus, and a custom indoor dataset collected at Chulalongkorn University demonstrate an end-to-end throughput of approximately 51 FPS on an NVIDIA Titan XP GPU, a 3.36x speedup over the multi-feature baseline, while maintaining frame-level AUROC values of 89.26%, 70.26%, and 84.13%, respectively.

### 🤖 AI 总结

**一句话总结**：We propose a lightweight two-stage framework for real-time video anomaly detection. The first stage employs YOLO v11n-pose to detect persons and extract seventeen skeletal keypoints in a single forwar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Real-Time, Video, Anomaly, Detection, YOLO, Pose, Estimation, CLIP-Based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31074v1) | [下载PDF](https://arxiv.org/pdf/2608.31074v1.pdf)

---

## [20. LISynSeg: Data-Centric Label-to-Image Synthesis for Cross-Modality Whole-Heart Segmentation](https://arxiv.org/abs/2608.31073v1)

**作者**：Jiacheng Wang, Ivana Isgum, Ipek Oguz  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-08-31

### 📄 论文摘要

Whole-heart segmentation (WHS) in computed tomography (CT) and magnetic resonance imaging (MRI) is affected by acquisition shifts and heterogeneous cardiac annotations. Existing WHS systems combine architectural design, transfer learning, and generic spatial or intensity augmentation. We investigate whether changes to data augmentation and training supervision can improve cross-modality WHS while the segmentation architecture is held constant. We present LISynSeg, a data-centric approach that augments real-image nnU-Net training with label-to-image synthesis. Synthetic volumes are generated from cardiac label maps using contrast and acquisition perturbations calibrated to the training cohort, then mixed with real images to retain thoracic context absent from the labels (and thus the synthesized images). We model cardiac label variation through controlled changes in myocardial wall thickness and partial supervision of uncertain vessel endpoints. On the CARE Whole-Heart benchmark, synthetic-only training performs worse than the real-image nnU-Net baseline, whereas calibrated real-synthetic training improves cross-modality segmentation without changing the architecture; the improvement is larger for MRI than for CT. The results show that modifying the training data strategy can benefit model development for heterogeneous cardiac data. Code and trained weights will be released at https://github.com/MedICL-VU/Care26_LISynSeg.

### 🤖 AI 总结

**一句话总结**：Whole-heart segmentation (WHS) in computed tomography (CT) and magnetic resonance imaging (MRI) is affected by acquisition shifts and heterogeneous cardiac annotations. Existing WHS systems combine ar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LISynSeg, Data-Centric, Label-to-Image, Synthesis, Cross-Modality, Whole-Heart, Segmentation, WHS

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31073v1) | [下载PDF](https://arxiv.org/pdf/2608.31073v1.pdf)

---

## [21. Multimodal Shared Latent Representation of Narration, Microscope and iOCT Images for Phase Recognition in Vitreoretinal Surgery](https://arxiv.org/abs/2608.31065v1)

**作者**：Onur Izmitlioglu, Shervin Dehghani, Tarek Ghannoum 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-31

### 📄 论文摘要

Surgical phase recognition is key to context-aware computer-assisted feedback in vitreoretinal procedures, yet the scarcity of synchronized multimodal intraoperative data, particularly microscope views and intraoperative OCT, limits approaches that aim to replicate the multimodal integration surgeons perform naturally. Surgical narration, by contrast, is abundantly available online and offers rich semantic supervision. Prior work has mainly explored pairwise contrastive learning (e.g., intraoperative OCT-microscope or microscope-narration), leaving the joint modeling of all three modalities largely unexplored. We introduce a framework that uses microscope views as a shared anchor to bridge surgical narrations and intraoperative OCT (iOCT) without requiring a fully synchronized tri-modal dataset, leveraging real microscope-narration videos and a synthetic dataset of synchronized microscope video and tool-aligned iOCT pairs. Contrastive alignment transfers structural priors from the synthetic domain to real videos lacking iOCT, and a dual-head MS-TCN++ integrates the resulting embeddings for joint macro- and micro-phase prediction. Evaluated on real vitreoretinal surgeries, our framework improves macro-phase recognition over a zero-shot baseline (mean F1 0.38 to 0.53) and provides an exploratory route to estimating fine-grained instrument-tissue measurements that are not directly observable in real microscope video alone; these micro-phase estimates are validated quantitatively on synthetic data and shown only qualitatively on real surgery. To our knowledge, this is the first work to unify microscope view, iOCT B-scans, and surgical narrations in a shared latent space for surgical phase recognition.

### 🤖 AI 总结

**一句话总结**：Surgical phase recognition is key to context-aware computer-assisted feedback in vitreoretinal procedures, yet the scarcity of synchronized multimodal intraoperative data, particularly microscope view...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Multimodal, Shared, Latent, Representation, Narration, Microscope, iOCT

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31065v1) | [下载PDF](https://arxiv.org/pdf/2608.31065v1.pdf)

---

## [22. Identity-Conditioned Latent Consistency Distillation for Face Synthesis](https://arxiv.org/abs/2608.31053v1)

**作者**：Tiago Kienen Chaves, Bernardo Biesseck, David Menotti  
**分类**：cs.CV  
**发布时间**：2026-08-31

### 📄 论文摘要

Diffusion models have achieved strong results in high-fidelity image synthesis, but their iterative sampling process makes large-scale generation computationally expensive. This limitation is especially relevant when generating synthetic face datasets for face recognition, where a large number of subjects with many samples in different poses, expressions, ages, etc., are required. In this work, we show that identity-conditioned face synthesis can be performed at a substantially lower computational cost by a latent Consistency Model with few iterations, without compromising image quality. For training, we distill knowledge from the foundation Diffusion Model Arc2Face (teacher) by adapting its original text-to-image pipeline to an embedding-to-face setting, replacing textual prompts with ArcFace identity embeddings. Our distilled model (student) generates identity-conditioned face images with an average inference time of 0.4819 seconds per image, compared with 2.102 seconds for Arc2Face, resulting in a 4.36$\times$ speed-up. Quantitative results, based on FID scores, show that the distilled model remains competitive with Arc2Face across all evaluation protocols. On 100k generated images, it achieves near-parity on CelebA (13.921 vs. 12.928) and outperforms the teacher on WebFace42M (9.317 vs. 9.802). Further evaluations on Synth-500 and AgeDB show a moderate performance gap for the former but comparable results for the latter. These results indicate that Arc2Face can be accelerated through task-specific latent consistency distillation while preserving high image quality for large-scale synthetic face generation. Our proposal is publicly available at https://github.com/UFPR-IPASP-PR/FaceRec-IdentityConsistency.

### 🤖 AI 总结

**一句话总结**：Diffusion models have achieved strong results in high-fidelity image synthesis, but their iterative sampling process makes large-scale generation computationally expensive. This limitation is especial...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Identity-Conditioned, Latent, Consistency, Distillation, Face, Synthesis, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31053v1) | [下载PDF](https://arxiv.org/pdf/2608.31053v1.pdf)

---

## [23. Segmentation of Bovid Dentition Under Imperfect Annotations: A Comparative Study of Convolutional and Attention Models](https://arxiv.org/abs/2608.31052v1)

**作者**：Keith G. Mills, Evan B. Sanders, Gregory J. Matthews 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-08-31

### 📄 论文摘要

Semantic segmentation decomposes an image into distinct mask regions corresponding to different object categories, such as people, cars, signs or buildings. Advances in machine learning (ML) have shifted this task away from traditional rule-based heuristics such as edge detection, towards deep neural networks (DNN) that learn to classify pixels directly. However, semantic segmentation DNNs crucially depend on expertly designed mask targets to learn from, and imperfect or misaligned masks can interfere with a model's ability to learn effectively.   This paper presents a comparative study of segmentation architectures, ranging from convolutional backbones to vision transformers, applied to the B.O.V.I.D. dataset, a corpus of high-resolution bovid dental photographs paired with hand-made segmentation masks not originally designed for ML-based training. We evaluate a range of preprocessing and alignment techniques to mitigate the resulting label imperfections. We find that while these preprocessing choices have limited effect on quantitative metrics such as Dice score and mIoU, their qualitative impact on predicted masks is substantial.

### 🤖 AI 总结

**一句话总结**：Semantic segmentation decomposes an image into distinct mask regions corresponding to different object categories, such as people, cars, signs or buildings. Advances in machine learning (ML) have shif...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Segmentation, Bovid, Dentition, Under, Imperfect, Annotations, Comparative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31052v1) | [下载PDF](https://arxiv.org/pdf/2608.31052v1.pdf)

---

## cs.LG

## [24. Sharp Approximation Rates for Neural Networks with Affine Latent Parameterizations](https://arxiv.org/abs/2608.31157v1)

**作者**：Shijun Zhang  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-08-31

### 📄 论文摘要

Many parameter-efficient methods generate the parameters of a large neural network from a low-dimensional latent representation. Given an architecture $Φ$ with $P_Φ$ parameter slots, we write $\boldsymbolθ_f=\mathcal{G}(\boldsymbolξ_f)$, where $\mathcal{G}\colon\mathbb{R}^M\to\mathbb{R}^{P_Φ}$ is a parameter generator and $\boldsymbolξ_f\in\mathbb{R}^M$ is a latent representation of the target function $f$. The architecture $Φ$ and the generator $\mathcal{G}$ are shared across the entire target class, while each target $f$ is represented by its own latent vector $\boldsymbolξ_f$, with $Φ_{\mathcal{G}(\boldsymbolξ_f)}$ approximating $f$. This framework encompasses hypernetworks, low-dimensional parameterizations, parameter-efficient adaptation, and model compression. Understanding the tradeoff between the latent dimension $M$ and the network budget $P$ is therefore fundamental to characterizing the expressive efficiency of these methods. We study this tradeoff for affine generators and fully connected ReLU architectures. More precisely, optimizing jointly over architectures $Φ$ satisfying $P_Φ\leq P$ and affine generators $\mathcal{G}:\mathbb{R}^M\to \mathbb{R}^{P_Φ}$, we prove that the optimal worst-case uniform approximation error over the unit ball of $α$-Hölder functions on $[0,1]^d$, where $0<α\leq1$, has the sharp order $ \bigl(P\min\{M,P\}\bigr)^{-α/d}. $ In particular, our result shows that even a fixed-dimensional latent space suffices to achieve vanishing approximation error as the network budget increases.

### 🤖 AI 总结

**一句话总结**：Many parameter-efficient methods generate the parameters of a large neural network from a low-dimensional latent representation. Given an architecture $Φ$ with $P_Φ$ parameter slots, we write $\boldsy...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sharp, Approximation, Rates, Neural, Networks, Affine, Latent, Parameterizations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31157v1) | [下载PDF](https://arxiv.org/pdf/2608.31157v1.pdf)

---

## [25. On the Complexity of the Compatibility Problem for Succinctly Encoded Conditional Distributions](https://arxiv.org/abs/2608.31120v1)

**作者**：Guy Emerson  
**分类**：cs.LG, cs.CC, math.PR  
**发布时间**：2026-08-31

### 📄 论文摘要

The motivation for this paper is the investigation of the trade-offs implicit in probabilistic models used in machine learning. Models are often used to make predictions in the form of conditional probabilities. However, a pair of conditional distributions p(x|y) and p(y|x) may not be compatible with any joint distribution p(x,y). Given two such conditionals, determining if there exists a compatible joint is known as the compatibility problem. For discrete random variables, when the conditionals are encoded as probability tables, the compatibility problem has a known solution, which is computationally tractable. In this paper, we formalise and study a succinct version of the problem, encoding conditional distributions as arithmetic circuits. This is applicable to practical applications of probabilistic modelling in high-dimensional settings, including neural network models. We show that, for succinct circuit representations of conditionals, the compatibility problem is intractable. In the case that all probabilities are non-zero, the problem is co-NP-complete. In the case that probabilities can be zero, we give examples to demonstrate that several notions of compatibility can be distinguished, and we prove that multiple versions of the problem are PSPACE-complete. Furthermore, we show that, assuming the polynomial hierarchy does not collapse, there exist compatible succinct conditionals whose joint cannot be expressed succinctly. Implications of these results for probabilistic modelling and machine learning are discussed.

### 🤖 AI 总结

**一句话总结**：The motivation for this paper is the investigation of the trade-offs implicit in probabilistic models used in machine learning. Models are often used to make predictions in the form of conditional pro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Complexity, Compatibility, Problem, Succinctly, Encoded, Conditional, Distributions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31120v1) | [下载PDF](https://arxiv.org/pdf/2608.31120v1.pdf)

---

## [26. Stress-Testing Efficient Responsible-AI Evaluation: When Compute Savings Change Benchmark Conclusions](https://arxiv.org/abs/2608.31108v1)

**作者**：Ahmed El Kady, Aravind Narayanan, Rehana Noorani 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-31

### 📄 论文摘要

Efficient evaluation changes the protocol used to support claims about model behavior, yet it is rarely tested whether those claims remain stable after the evaluation itself is made cheaper. We stress-test conclusion robustness in responsible-AI benchmarking by evaluating three dense and mixture-of-experts models on BBQ and BBQ-V under seven conditions spanning batching, quantization, benchmark reduction, and their combinations. Rather than treating preserved aggregate accuracy as sufficient, we compare accuracy, bias severity and prevalence, reasoning quality, subgroup behavior, subset-membership stability, runtime, and measured GPU energy against a full-benchmark BF16 baseline. Larger batching keeps accuracy within 0.35 percentage points of baseline and produces comparatively small subgroup changes, while reducing energy in five of six model--dataset settings. INT8 largely preserves quality but uses 1.79--4.26$\times$ baseline energy. INT4 causes larger, model- and context-dependent changes. Reduced benchmarks provide the most consistent savings, but very small subsets are substantially more sensitive to which items are retained. Efficient evaluation should therefore be treated as a measurement intervention whose validity must be checked across the conclusions the benchmark is intended to support. Our project website is https://vectorinstitute.github.io/sustainable-rai-evaluation/ and the code is available at https://github.com/VectorInstitute/sustainable-rai-evaluation.

### 🤖 AI 总结

**一句话总结**：Efficient evaluation changes the protocol used to support claims about model behavior, yet it is rarely tested whether those claims remain stable after the evaluation itself is made cheaper. We stress...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Stress-Testing, Efficient, Responsible-AI, Evaluation, When, Compute, Savings, Change

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31108v1) | [下载PDF](https://arxiv.org/pdf/2608.31108v1.pdf)

---

## [27. Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization](https://arxiv.org/abs/2608.31079v1)

**作者**：Camila Blank, Zhuofan Ying, Christopher Potts 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-31

### 📄 论文摘要

Sycophantic agreement refers to a behavior in which language models excessively affirm the user, often at the cost of factual accuracy. Although sycophantic agreement is a well-known failure of model alignment, there is limited understanding of how it emerges from model training. In this work, we demonstrate that sycophantic agreement can emerge as an unintended consequence of widely used contrastive preference optimization objectives. Using the OLMo 3 post-training pipeline, we show that, for various pairs of teacher models across three families, there is a strong correlation between the log-ratio of the teacher model sycophantic agreement rates and the resulting student model sycophantic agreement rate. We further demonstrate that this unintended transfer is not limited to DPO but also occurs across 6 other preference optimization objectives. To understand whether this effect can be attributed to particular training examples, we analyze the preference data and find that the sycophancy signal is diffused across the entire dataset rather than concentrated in a sparse set of examples: each example appears neutral, i.e., there are no explicit instances of sycophantic agreement, and filtering based on probe-based data attribution or logit-linear selection fails to mitigate sycophancy without removing a large portion of the dataset. Overall, our findings suggest that the teacher models used to generate preference data can interact with alignment training objectives in unexpected ways, generalizing to undesirable and potentially harmful behaviors like sycophantic agreement.

### 🤖 AI 总结

**一句话总结**：Sycophantic agreement refers to a behavior in which language models excessively affirm the user, often at the cost of factual accuracy. Although sycophantic agreement is a well-known failure of model ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sycophantic, Agreement, Transfers, Neutral, Data, via, Contrastive, Preference

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31079v1) | [下载PDF](https://arxiv.org/pdf/2608.31079v1.pdf)

---

## [28. Universal Transformers for Circuit Computations: Perfect Length Generalization in Tiny Transformers](https://arxiv.org/abs/2608.31067v1)

**作者**：Takuya Ito, Ruchir Puri, Murray Campbell 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-31

### 📄 论文摘要

Learning generalizable algorithmic computations remains a challenge for neural networks, as reflected in persistent failures on compositional and length generalization benchmarks. We present a provably correct, transformer parameterization (with only 280 learnable parameters for Boolean algebra tasks) capable of learning and evaluating problems of any depth or length. We assume inputs are fully parenthesized, well-formed expressions. Our approach conceptualizes algorithmic tasks as circuit models embedded in transformers, enabling depth-1 circuit reduction in a single forward pass. To achieve depth generalization, we introduce a positional encoding that tracks each gate's depth within the circuit, enabling the model to identify evaluable subexpressions at each iteration via masked hard attention, with $O(n)$ per-iteration complexity via linear attention. Combined with an autonomous halting criterion, the model terminates after $d$ iterations for problems of depth $d$, yielding $O(n \cdot d)$ total complexity. We show that training on shallow problem instances (depth 1 and depth 2) effectively recovers interpretable parameters that {\em snap} into place, resulting in exact length generalization. Though we establish that our construction provably evaluates Boolean expressions -- a universal symbolic computation -- of arbitrary length perfectly, in other experiments we also demonstrate that our transformer variant can learn and generalize perfectly (100% accuracy) on other common length generalization benchmarks, including modular arithmetic and ListOps.

### 🤖 AI 总结

**一句话总结**：Learning generalizable algorithmic computations remains a challenge for neural networks, as reflected in persistent failures on compositional and length generalization benchmarks. We present a provabl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Universal, Transformers, Circuit, Computations, Perfect, Length, Generalization, Tiny

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31067v1) | [下载PDF](https://arxiv.org/pdf/2608.31067v1.pdf)

---

## [29. Rotational Equivariance in Machine Learning: A Comprehensive Tutorial](https://arxiv.org/abs/2608.31045v1)

**作者**：Peter Lippmann, Fred A. Hamprecht  
**分类**：cs.LG  
**发布时间**：2026-08-31

### 📄 论文摘要

Rotational symmetry is one of the most important structural principles in machine learning on 3D data. In applications ranging from physics and materials science to 3D computer vision, predictions should not depend on an arbitrary choice of coordinate frame. Rotational equivariance captures this requirement mathematically by enforcing that a rotation of the input induces a corresponding transformation of the model output. This tutorial provides a comprehensive introduction to rotational equivariance, starting from the physical and geometric intuition behind coordinate independence and building up the necessary machinery from geometric deep learning, group theory, and representation theory. We introduce message passing on Euclidean graphs, group actions and representations, spherical harmonics, Wigner matrices, tensor products, and Clebsch-Gordan decomposition, and explain how these ingredients give rise to modern equivariant architectures. We then survey the principal strategies for incorporating rotational equivariance in deep learning, including group convolutions, internal tensorial representations, and canonicalization-based methods, and discuss their practical strengths and limitations. The tutorial aims to lower the barrier to the subject by connecting the underlying mathematics to practical model design, by unifying ideas that are often expressed in different formal languages, and by helping practitioners choose among competing approaches through a clear discussion of their trade-offs.

### 🤖 AI 总结

**一句话总结**：Rotational symmetry is one of the most important structural principles in machine learning on 3D data. In applications ranging from physics and materials science to 3D computer vision, predictions sho...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Rotational, Equivariance, Machine, Learning, Comprehensive, Tutorial, symmetry, one

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31045v1) | [下载PDF](https://arxiv.org/pdf/2608.31045v1.pdf)

---

## [30. Normalized Low-Rank Adaptation](https://arxiv.org/abs/2608.31036v1)

**作者**：Jiale Kang, Ziyin Yue, Zheng Zhan 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-31

### 📄 论文摘要

While low-rank adaptation (LoRA) is widely used for parameter-efficient model adaptation, how to regularize its training dynamics for stable and effective optimization remains underexplored. Because LoRA initializes the up-projection to zero, its early optimization dynamics are largely governed by the down-projection. Building on this observation, we introduce Normalized Low-Rank Adaptation (NoRA), a simple yet effective method that normalizes the down-projection matrices during training. We further show that the same normalization can be applied only at initialization, improving standard LoRA without requiring repeated normalization throughout training. Across pretraining, supervised finetuning, and reinforcement learning, NoRA consistently accelerates convergence, improves performance and training stability, and mitigates catastrophic forgetting. These benefits require neither additional trainable parameters nor inference-time computation, making NoRA a simple and broadly applicable enhancement to LoRA.

### 🤖 AI 总结

**一句话总结**：While low-rank adaptation (LoRA) is widely used for parameter-efficient model adaptation, how to regularize its training dynamics for stable and effective optimization remains underexplored. Because L...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Normalized, Low-Rank, Adaptation, While, LoRA, widely, used, parameter-efficient

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.31036v1) | [下载PDF](https://arxiv.org/pdf/2608.31036v1.pdf)

---

