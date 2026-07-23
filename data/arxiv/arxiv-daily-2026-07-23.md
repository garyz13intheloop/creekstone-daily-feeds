# arXiv AI 论文日报 | 2026-07-23

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (8 篇)
- [cs.AI](#csAI) (1 篇)
- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (10 篇)

---

## cs.AI

## [1. SoftReason: A Fully Differentiable Neuro-Soft-Symbolic Deductive Reasoning Architecture over High-Dimensional Perceptual Data](https://arxiv.org/abs/2607.20402v1)

**作者**：Wael AbdAlmageed  
**分类**：cs.AI  
**发布时间**：2026-07-22

### 📄 论文摘要

In many reasoning problems, the premises are not observed as discrete symbols, but must be inferred from high-dimensional inputs. Further, the predicate vocabulary, argument structure, and trusted evidence are supplied by a Knowledge Graph (KG), or rule definitions. Classical neuro-symbolic pipelines have a discrete interface between perception and deduction. We present a neuro-soft-symbolic architecture for differentiable deductive reasoning over latent perceptual facts and knowledge-provided predicates. SoftReason removes the gradient gap by representing the deductive state as a local soft interpretation tensor over candidate constants and predicates. Perception proposes probabilistic base facts, KG triples enter as high-confidence soft evidence, and every query anchor, predicate choice, and closure update remains differentiable. Our core innovation is a learned differentiable lift of the immediate-consequence operator. It uses predicate-definition embeddings and latent composition channels to form soft body-predicate mixtures, aggregate over all possible witnesses, propose query-conditioned head facts, and update the interpretation through a monotone probabilistic OR. We instantiate the framework on Knowledge-aware Visual Question Answering (KVQA), and demonstrates how SoftReason supports end-to-end perceptual grounding, KG evidence injection, and differentiable deductive closure in one trainable architecture.

### 🤖 AI 总结

**一句话总结**：In many reasoning problems, the premises are not observed as discrete symbols, but must be inferred from high-dimensional inputs. Further, the predicate vocabulary, argument structure, and trusted evi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SoftReason, Fully, Differentiable, Neuro-Soft-Symbolic, Deductive, Reasoning, Architecture, over

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20402v1) | [下载PDF](https://arxiv.org/pdf/2607.20402v1.pdf)

---

## cs.CL

## [2. LKValues: Aligning Large Language Models with Sri Lankan Societal Values](https://arxiv.org/abs/2607.20410v1)

**作者**：Nethmi Muthugala, Supryadi, Surangika Ranathunga 等 10 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-22

### 📄 论文摘要

Value alignment of Large Language Models (LLMs) has been shown to be culturally biased toward Western norms. This results in the mishandling of local values in multilingual societies such as Sri Lanka that have their unique cultural dynamics. Existing benchmarks overlook Sri Lankan-contextualized values in its official language Sinhala, hindering culturally sensitive evaluation and fine-tuning. To bridge this gap, we propose LKValues, the first survey-grounded resource suite for Sri Lankan value alignment. From a trilingual survey of 205 respondents, blending adapted global frameworks and LLM-elicited local constructs, we derive 40 majority-endorsed societal values. Using these values, we construct LKvaluesIT, a Sinhala-English news-derived instruction corpus containing 150k scenario-based instances, and LKvaluesBench, a value-sensitive evaluation benchmark of 1,000 instances. We evaluate a set of proprietary and open-weight LLMs with LKvaluesBench. We fine-tune three open-weight base models (Qwen3.5-4B-Base, Qwen3.5-9B-Base, and Aya-Expanse-8B-Base). Our experiments show that newer and larger LLMs still exhibit low-resource and cultural value-alignment gaps. LKValues fine-tuning improves Qwen-family models in English and Sinhala, reducing invalid outputs and cross-lingual disparities, though gains remain model-family dependent. These highlight LKValues efficacy in embedding Sri Lankan values, offering a replicable pipeline for low-resource, country-specific pluralist value alignment. The dataset is publicly available at https://github.com/NextME14/LKValues.

### 🤖 AI 总结

**一句话总结**：Value alignment of Large Language Models (LLMs) has been shown to be culturally biased toward Western norms. This results in the mishandling of local values in multilingual societies such as Sri Lanka...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LKValues, Aligning, Large, Language, Models, Sri, Lankan, Societal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20410v1) | [下载PDF](https://arxiv.org/pdf/2607.20410v1.pdf)

---

## [3. Notes to Self: Can LLMs Benefit from Experiential Abstractions?](https://arxiv.org/abs/2607.20372v1)

**作者**：Chang Liu, Xinyu Li, Artur Dubrawski  
**分类**：cs.CL  
**发布时间**：2026-07-22

### 📄 论文摘要

Humans distill experience into reusable abstractions, e.g., strategies and cautionary reminders, and apply them to gradually solve problems more effectively. We study whether Large Language Models (LLMs) can similarly benefit from such experiential abstractions. From LLMs' solution traces on the MATH training set, a stronger teacher or the LLMs themselves extract natural-language abstractions into a retrievable library. We explore two usage modes: (1) inference-time retrieval and (2) reinforcement learning (RL) with abstraction-augmented training prompts. Experiential abstractions improve LLM performance on mathematical and logical reasoning benchmarks. Self-extracted abstractions match teacher-extracted ones, and our abstraction usage framework can transfer to other datasets and models. These findings suggest LLMs can extract and apply experiential abstractions much as humans leverage distilled experience.

### 🤖 AI 总结

**一句话总结**：Humans distill experience into reusable abstractions, e.g., strategies and cautionary reminders, and apply them to gradually solve problems more effectively. We study whether Large Language Models (LL...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Notes, Self, Can, Benefit, Experiential, Abstractions?, Humans

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20372v1) | [下载PDF](https://arxiv.org/pdf/2607.20372v1.pdf)

---

## [4. Generative AI floods and dilutes the market for books](https://arxiv.org/abs/2607.20349v1)

**作者**：Tuhin Chakrabarty, Xinyue Liu, Jane C. Ginsburg 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.CY  
**发布时间**：2026-07-22

### 📄 论文摘要

Generative AI can produce book-length works of fiction at near-zero cost. These books are often dismissed as low-quality ``slop'' that buyers will ignore, and are assumed to carry little commercial weight. We test that assumption with full-text AI detection across 14,419 self-published genre-fiction books sold on Amazon from 2023 to 2026, matched to daily sales records through June 2026. None of these books disclose whether or not they contain AI-produced content. We find that books for which we detected substantial AI text ($>$ 25\%) make up a large share of the catalog but a smaller share of sales. Even so, they reach commercial scale, winning a growing share of sales over time and taking more of the scarce top-rank positions once held by books with no detected AI text. Over this period, the number of books with observed sales in a quarter grew 19.2-fold, while quarterly revenue grew only 8.9-fold. The market therefore added selling books faster than it added revenue, and revenue per selling book fell across most genres. Books with no AI text lose the most ground in genres with high AI diffusion, and most of all where Kindle Unlimited availability is high. Among top-selling books, those with substantial AI text draw on more distinctive language from existing books than do books with no AI text; for these books overlap rises with revenue, a gradient we do not detect for books with no AI text. Generative AI can thus reshape a creative market through scale rather than quality. Our results bear directly on the market-effect question at the center of the fair use defense to copyright infringement.

### 🤖 AI 总结

**一句话总结**：Generative AI can produce book-length works of fiction at near-zero cost. These books are often dismissed as low-quality ``slop'' that buyers will ignore, and are assumed to carry little commercial we...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Generative, floods, dilutes, market, books, can, produce, book-length

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20349v1) | [下载PDF](https://arxiv.org/pdf/2607.20349v1.pdf)

---

## [5. Sound Probabilistic Safety Bounds for Large Language Models](https://arxiv.org/abs/2607.20286v1)

**作者**：Mahdi Nazeri, Anne-Kathrin Schmuck, Sadegh Soudjani 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-22

### 📄 论文摘要

We propose a novel framework for computing rigorous bounds on the probability that a large language model (LLM) generates harmful output to a given prompt. We study a new application of the Clopper-Pearson confidence intervals to obtain probably approximately correct (PAC) bounds for this problem. As our main technical contribution, we propose an algorithm that leverages features in the latent space to prioritize exploring branches in the auto-regressive generation tree that are more likely to produce harmful outputs. Our approach in particular enables the efficient computation of useful lower bounds, even in scenarios where the true harm probability is extremely small, and crucially, the obtained lower bounds are sound, i.e., formally proven to be less than the actual harmfulness probability: our experimental results demonstrate the effectiveness of our method by computing non-trivial lower bounds on state-of-the-art LLMs. This study newly enables the evaluation and statistical certification of LLMs.

### 🤖 AI 总结

**一句话总结**：We propose a novel framework for computing rigorous bounds on the probability that a large language model (LLM) generates harmful output to a given prompt. We study a new application of the Clopper-Pe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Sound, Probabilistic, Safety, Bounds, Large, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20286v1) | [下载PDF](https://arxiv.org/pdf/2607.20286v1.pdf)

---

## [6. Which Values Do LLMs Confuse? A Schwartz-Based Recognition Study](https://arxiv.org/abs/2607.20270v1)

**作者**：Andrei Chetvergov, Stepan Ukolov, Timofei Sivoraksha 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-22

### 📄 论文摘要

Large language models are increasingly evaluated through the values they endorse, but such evaluations presuppose that models can identify the value expressed in a concrete situation. We study this prerequisite as controlled top-1 recognition over Schwartz's ten basic values. Our evaluation set contains 1,000 Russian situational texts, balanced across the ten values and independently labeled by two human annotators per item. We evaluate 21 instruction-tuned LLM runs under a fixed ranked-response protocol; 20 runs with reliable outputs form the semantic panel. Pooled Acc@1 is 0.683 and Acc@3 is 0.892, showing that models often locate the correct motivational region while ranking close alternatives unstably. Adjacent values account for 50.9% of semantic errors, compared with 24.4% under a checkpoint-specific null. Eight directed confusions recur across checkpoints and human-confirmed subsets. Several are strongly asymmetric, including Universalism to Benevolence, Tradition to Conformity, and Security to Power, whereas Stimulation-Hedonism forms a bidirectional boundary. Their severity is checkpoint-specific and can bias higher-order value profiles. The results motivate value-recognition evaluation that combines exact accuracy, ranked recovery, and directed error analysis.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly evaluated through the values they endorse, but such evaluations presuppose that models can identify the value expressed in a concrete situation. We study this pr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, LLM, Which, Values, Confuse?, Schwartz-Based, Recognition, Study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20270v1) | [下载PDF](https://arxiv.org/pdf/2607.20270v1.pdf)

---

## [7. The Maskability Index: Predicting Task-Objective Alignment in Pretrained Language Models](https://arxiv.org/abs/2607.20265v1)

**作者**：Ahmad Pouramini, Mahsa Afsharzadeh  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-22

### 📄 论文摘要

Large-scale pretrained language models such as T5 and BERT have demonstrated strong capabilities for generating structured knowledge. However, their performance depends on how closely the prompting strategy matches the objectives used during pretraining. We introduce the Maskability Index (MI), a quantitative metric that estimates whether a knowledge relation is better suited to masked-style prompting or prefix-style prompting in few-shot generation. MI is computed from differences in DepthRank scores between masked and unmasked templates, providing a principled measure of objective-template alignment. We evaluate MI on a diverse set of relations from the ATOMIC2020 knowledge base completion benchmark and show that it is positively correlated with downstream generation performance. These results indicate that MI can help select appropriate prompting templates and adaptation strategies for extracting relational knowledge from pretrained language models, especially in low-resource settings.

### 🤖 AI 总结

**一句话总结**：Large-scale pretrained language models such as T5 and BERT have demonstrated strong capabilities for generating structured knowledge. However, their performance depends on how closely the prompting st...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Maskability, Index, Predicting, Task-Objective, Alignment, Pretrained, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20265v1) | [下载PDF](https://arxiv.org/pdf/2607.20265v1.pdf)

---

## [8. Exposure is Optional: Learning Unlike Coordination in Language Models](https://arxiv.org/abs/2607.20251v1)

**作者**：Jiamu Luo, Shane Steinert-Threlkeld  
**分类**：cs.CL  
**发布时间**：2026-07-22

### 📄 论文摘要

Coordination, a fundamental linguistic structure, remains a subject of intense debate, and its exact nature continues to elude theoretical linguistics. A common view holds that only same-category constituents can be conjoined, which has been challenged by the many grammatical unlike coordinations found in natural language. Treating language models as a computational testbed, we investigate whether the acquisition of unlike coordination requires direct exposure in the training data, or whether it can emerge organically from general compositional abilities. Using Filtered-Corpus Training (FiCT), we train GPT-2 models on corpora from which all instances of unlike coordination have been removed. We find that direct exposure is not necessary: models trained on filtered data successfully generalize to unlike coordination, achieving perplexity and grammaticality judgments comparable to models trained on unfiltered text. Furthermore, our analyses of internal representations indicate that language models process unlike coordination by treating the conjoined elements as belonging to similar structural categories or through a mechanism akin to deletion, both of which appear learnable from exposure to alike coordination alone. This work contributes to the growing understanding of how language models internally represent linguistic structures, while also adding to the broader debate on coordination by showing how models generalize and process unlike coordination without direct exposure.

### 🤖 AI 总结

**一句话总结**：Coordination, a fundamental linguistic structure, remains a subject of intense debate, and its exact nature continues to elude theoretical linguistics. A common view holds that only same-category cons...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Exposure, Optional, Learning, Unlike, Coordination, Language, Models, fundamental

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20251v1) | [下载PDF](https://arxiv.org/pdf/2607.20251v1.pdf)

---

## [9. On the Systematic Challenges of Culturally Loaded Machine Translation: Dream of the Red Chamber as the Cultural Lens](https://arxiv.org/abs/2607.20241v1)

**作者**：Yiming Wang, Jiayuan Di  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-22

### 📄 论文摘要

Culturally loaded translation poses unique challenges for machine translation (MT), as meanings are deeply embedded in socio-cultural contexts beyond surface linguistic forms. Although large language models (LLMs) have enabled MT systems to achieve human-like quality in many scenarios, their ability to handle culturally loaded expressions remains underexplored. In this study, we systematically investigate the challenges posed by culturally loaded translation in LLM-based MT systems. We construct a Chinese-Japanese bilingual dataset from the culturally representative corpus Dream of the Red Chamber, containing 500 segments across diverse cultural categories. Using a comprehensive evaluation protocol, we reveal three main challenges: (1) task challenges, where frontier LLMs exhibit notable performance gaps and struggle with culturally loaded content; (2) human evaluation challenges, where evaluator backgrounds lead to substantial disagreement in translation judgments; and (3) automatic evaluation challenges, where widely used metrics fail to reliably assess translation quality for this task. These findings may offer valuable insights for culture-oriented translation research in both computational science and linguistics.

### 🤖 AI 总结

**一句话总结**：Culturally loaded translation poses unique challenges for machine translation (MT), as meanings are deeply embedded in socio-cultural contexts beyond surface linguistic forms. Although large language ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Systematic, Challenges, Culturally, Loaded, Machine, Translation, Dream

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20241v1) | [下载PDF](https://arxiv.org/pdf/2607.20241v1.pdf)

---

## cs.CV

## [10. PercepCap: Video Captioner with Structured Spatio-Temporal Perception](https://arxiv.org/abs/2607.20389v1)

**作者**：Yifan Xu, Zihao Wang, Zhixiao Wang 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-22

### 📄 论文摘要

Video captioning requires fine-grained spatio-temporal understanding of videos, including spatial perception of where objects are located and temporal perception of when events occur. Existing MLLMs usually generate captions directly from video inputs without exposing the perceptual evidence behind descriptions. As a result, mistakes in spatiotemporal perception are only observed in the final caption, making it difficult to identify the underlying perceptual errors directly. To address these issues, we present PercepCap, a perception-aware video captioning framework that makes perceptual evidence explicit before producing the final caption. Specifically, PercepCap follows a perceive-describe generation chain, where the model first produces a spatiotemporal perception trace comprising object trajectories and temporal events, and then generates the final caption conditioned on the perceived evidence. To support this, we design a two-stage training strategy. Perceive-then-Describe Supervised Fine-tuning adapts the model from caption-only generation to the proposed perceive-describe chain, while Perception-Grounded Reinforcement Learning optimizes perception trace and caption quality with joint rewards over perception chain and the final caption. To support our two-stage training, we introduce Caption-Anchored Perception Data Construction. This pipeline builds the SFT and RL training data by first generating a caption-only description, extracting the objects and events it mentions, and grounding them back in the video with boxes and timestamps. This yields caption-aligned perception data that provides solid training ground truth, ensuring that the explicit perception trace and final caption refer to the same objects and events. Across direct caption and caption-to-QA evaluation, PercepCap consistently improves upon the Qwen3-VL baseline and demonstrates leading caption quality.

### 🤖 AI 总结

**一句话总结**：Video captioning requires fine-grained spatio-temporal understanding of videos, including spatial perception of where objects are located and temporal perception of when events occur. Existing MLLMs u...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PercepCap, Video, Captioner, Structured, Spatio-Temporal, Perception, captioning, requires

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20389v1) | [下载PDF](https://arxiv.org/pdf/2607.20389v1.pdf)

---

## [11. Persian Pixel: A large-scale synthetic OCR dataset for Persian language](https://arxiv.org/abs/2607.20385v1)

**作者**：Pouria Mahdi, Haq Nawaz Malik  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-22

### 📄 论文摘要

Optical Character Recognition (OCR) for Persian remains substantially less mature than for Latin-script languages despite Persian being spoken by more than 110 million people across multiple countries. This gap arises from two fundamental challenges: the intrinsic complexity of the Perso-Arabic writing system and the limited availability of large-scale, high-quality annotated datasets. Persian script exhibits obligatory cursive connectivity, context-dependent glyph shaping, extensive ligatures, diacritic placement, and stylistic variation across writing forms such as Naskh and Nastaliq, all of which significantly complicate text recognition. At the same time, the high cost and labor-intensive nature of manual annotation have created a persistent data bottleneck, limiting the development of robust OCR systems and slowing progress in Persian document digitization.In this paper, we introduce Persian Pixel, a comprehensive synthetic OCR dataset specifically designed to address these challenges. Comprising over 343,000 high-fidelity image text pairs, the dataset spans sentence, paragraph, and full-page document layouts generated from a carefully curated seven-million-word Persian corpus using the SynthOCR-Gen rendering framework. The generation pipeline faithfully models the typographic characteristics of Persian script, including contextual character joining, positional glyph variants, diacritic placement, and multiple representative Persian typefaces. To bridge the synthetic-to-real domain gap, the rendered images are further enriched with more than twenty-five stochastic degradation models that emulate realistic document acquisition artifacts, including ink bleed, paper aging, blur, illumination variation, scanner imperfections, compression artifacts, and multiple noise processes.By overcoming the long-standing scarcity of annotated Persian OCR data, Persian Pixel provides a scalable and openly available resource for training and fine-tuning modern OCR architectures, including transformer-based models such as TrOCR and Donut. The dataset establishes a strong foundation for research in Persian document analysis, historical manuscript digitization, and end-to-end document understanding, while demonstrating that programmatic synthetic data generation offers a practical, cost-effective, and scalable alternative to manual annotation for advancing OCR in low-resource and typographically complex scripts.

### 🤖 AI 总结

**一句话总结**：Optical Character Recognition (OCR) for Persian remains substantially less mature than for Latin-script languages despite Persian being spoken by more than 110 million people across multiple countries...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OCR, Persian, Pixel, large-scale, synthetic, dataset, language, Optical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20385v1) | [下载PDF](https://arxiv.org/pdf/2607.20385v1.pdf)

---

## [12. Self Gradient Forcing: Native Long Video Extrapolation](https://arxiv.org/abs/2607.20368v1)

**作者**：Junhao Zhuang, Shiyi Zhang, Yuxuan Bian 等 14 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-22

### 📄 论文摘要

Recent autoregressive video diffusion methods are increasingly built upon Self Forcing, where the student is trained on histories produced by its own rollout rather than ground-truth video contexts. This reduces exposure bias, but the historical key-value cache is still used by future frames only as frozen rollout state. As a result, future losses cannot supervise how earlier generated latents should be written into more useful keys and values for later video-latent generation. We call this the historical context-gradient gap. We propose Self Gradient Forcing (SGF), a two-pass training strategy that restores this missing supervision signal without backpropagating through the full serial rollout. Pass 1 performs a no-gradient autoregressive rollout matching inference and, at a sampled denoising exit step, records both the self-generated context and the noisy latents fed to the model. Pass 2 performs parallel context-gradient reconstruction for the recorded exit step. The generated context is used as stop-gradient clean-latent input, while the model recomputes the context KV representations and future-to-context causal attention. Thus, SGF provides the missing memory-writing supervision within the native autoregressive training objective, using losses on future video latents to train the model to encode context into more effective causal memory. Across extensive long-horizon frame-wise and chunk-wise experiments under different initializations, SGF achieves stronger native long-video extrapolation than Self Forcing, especially in subject identity, background/layout consistency, and temporal stability. Remarkably, using only a 5-second training window, SGF can extrapolate to videos lasting several minutes. Code and models will be released to advance research on autoregressive video generation.

### 🤖 AI 总结

**一句话总结**：Recent autoregressive video diffusion methods are increasingly built upon Self Forcing, where the student is trained on histories produced by its own rollout rather than ground-truth video contexts. T...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Self, Gradient, Forcing, Native, Long, Video, Extrapolation, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20368v1) | [下载PDF](https://arxiv.org/pdf/2607.20368v1.pdf)

---

## [13. Test-Time Training for Modality Order Consistency in Vision-Language Models](https://arxiv.org/abs/2607.20351v1)

**作者**：Aditi Gupta, Yossi Gandelsman  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-07-22

### 📄 论文摘要

We find that vision-language models are sensitive to a specific semantically irrelevant change: the order in which the image and question are presented. Across three models and three benchmarks, image first prompting consistently outperforms question-first prompting, revealing a repeatable modality order failure. We use this gap to design an order-consistent test-time training method. Our method substantially closes the modality-order gap across all evaluated settings. Surprisingly, it also yields consistent improvements in the stronger image-first branch over the baseline, hence bootstrapping both orderings toward mutual consistency. Activation patching localizes the ordering failure to a narrow mid-network region where representations diverge sharply between prompt orders. We find that the test-time training method repairs this misalignment across layers. Together, our results identify modality-order sensitivity as a circuit-level failure in VLMs and demonstrate that simple, asymmetric test-time adaptation can effectively mitigate it and even improve performance over the baseline.

### 🤖 AI 总结

**一句话总结**：We find that vision-language models are sensitive to a specific semantically irrelevant change: the order in which the image and question are presented. Across three models and three benchmarks, image...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Test-Time, Training, Modality, Order, Consistency, Vision-Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20351v1) | [下载PDF](https://arxiv.org/pdf/2607.20351v1.pdf)

---

## [14. Toward Reliable RGB-D Semantic Segmentation: Handling Missing Modalities via Condition Dropout](https://arxiv.org/abs/2607.20326v1)

**作者**：Xuchen Zhu, Yajuan Wei, Shuang Hao 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-22

### 📄 论文摘要

RGB-D semantic segmentation has achieved remarkable progress, yet most models assume that RGB and depth are always available. In practice, failures or occlusions of surveillance sensors often remove one modality. Although RGB or depth alone can contain sufficient cues, models trained only on full-modality inputs fail to exploit the remaining modality once one is missing, causing severe degradation. We tackle this issue with a simple continued-training paradigm, \emph{Condition Dropout (ConD)}, which mitigates degradation while preserving full-modality accuracy. Starting from a pretrained RGB-D model, ConD adds a second stage that randomly simulates complete, RGB-missing, and depth-missing inputs, freezes the original encoders, and trains copied encoders with zero-initialized feature injection. Experiments on NYU-Depth V2 and SUN RGB-D show that ConD improves robustness under missing modalities and even yields slight gains when modalities are complete. Our code will be made publicly available upon acceptance.

### 🤖 AI 总结

**一句话总结**：RGB-D semantic segmentation has achieved remarkable progress, yet most models assume that RGB and depth are always available. In practice, failures or occlusions of surveillance sensors often remove o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Toward, Reliable, RGB-D, Semantic, Segmentation, Handling, Missing, Modalities

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20326v1) | [下载PDF](https://arxiv.org/pdf/2607.20326v1.pdf)

---

## [15. Evolving Cache Schedules for Fast Diffusion Policy Inference](https://arxiv.org/abs/2607.20293v1)

**作者**：Siying Wang, Kangye Ji, Di Wang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-22

### 📄 论文摘要

Diffusion policies achieve strong visuomotor control by iteratively denoising action chunks, but repeated denoising makes real-time deployment computationally demanding. Cache-based methods reduce inference cost by reusing intermediate activations, but existing training-free schedules typically allocate computation uniformly across blocks, ignoring heterogeneous redundancy across blocks and leading to a suboptimal performance-efficiency trade-off. To bridge this gap, we introduce Evolving Cache Schedules (EVO), a training-free acceleration framework that globally schedules cache refreshes via evolutionary search. EVO represents each candidate as a complete schedule over the block-timestep lattice. Thus, redundant transformer computations during iterative denoising can be skipped through cache reuse while preserving closed-loop rollout performance. To make the search practical, EVO introduces redundancy-aware initialization, which seeds the population with promising schedules, and target-conditioned early stopping, which verifies and terminates once a desired performance target is reached. The offline-optimized schedule can be directly plugged into pretrained diffusion policies without retraining. Extensive manipulation benchmarks show that EVO preserves near-full performance while substantially reducing computation, achieving up to 8.05x action-generation speedup and reducing FLOPs from 15.77G to as low as 1.96G. Source code is available at https://github.com/pillom/EVO.

### 🤖 AI 总结

**一句话总结**：Diffusion policies achieve strong visuomotor control by iteratively denoising action chunks, but repeated denoising makes real-time deployment computationally demanding. Cache-based methods reduce inf...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Evolving, Cache, Schedules, Fast, Policy, Inference, policies

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20293v1) | [下载PDF](https://arxiv.org/pdf/2607.20293v1.pdf)

---

## [16. Diverse-Intent Multi-Turn Fashion Image Retrieval](https://arxiv.org/abs/2607.20291v1)

**作者**：Mingqiang Tang, Haokun Wen, Meng Liu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-22

### 📄 论文摘要

Real-world fashion search involves interactive retrieval across multiple turns. However, existing multi-turn retrieval methods are built on a restrictive assumption that every interaction follows the same attribute-editing paradigm, leaving heterogeneous intent transitions unexplored. Moreover, existing approaches often rely on textification to bridge multimodal queries and visual retrieval, which may lose fine-grained visual cues. To address these gaps, we introduce DIM-Fashion, a benchmark of 26K multi-turn sessions constructed from 13 fashion retrieval datasets across 7 tasks, featuring diverse intent transitions and rollback behaviors. We further propose FashionAM, an MLLM-VLP framework that directly aligns multimodal conversational queries with a fashion-oriented gallery embedding space, avoiding intermediate textification. Extensive experiments demonstrate the effectiveness of FashionAM over existing approaches. The dataset and code will be made publicly available upon acceptance.

### 🤖 AI 总结

**一句话总结**：Real-world fashion search involves interactive retrieval across multiple turns. However, existing multi-turn retrieval methods are built on a restrictive assumption that every interaction follows the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diverse-Intent, Multi-Turn, Fashion, Image, Retrieval, Real-world, search, involves

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20291v1) | [下载PDF](https://arxiv.org/pdf/2607.20291v1.pdf)

---

## [17. Multimodal Large Language Models for Remote Sensing Image Understanding: Domain-Specific or General-Purpose?](https://arxiv.org/abs/2607.20284v1)

**作者**：Qiwei Ma, Chunping Qiu, Xinjun Cheng 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-22

### 📄 论文摘要

The rapid development of multimodal large language models (MLLMs) has introduced a flexible paradigm for remote sensing image scene understanding (RSISU), enabling natural-language interaction with remote sensing imagery. However, a systematic understanding of the capability boundaries, cross-task generalization, and task-specific limitations of existing remote sensing MLLMs (RS-MLLMs) is still lacking. This paper presents a systematic survey and diagnostic evaluation of MLLMs for RSISU. We review the technical evolution of RS-MLLMs, focusing on model design, multimodal learning, training data, and downstream capabilities. We further compare RS-MLLMs with general-purpose computer vision MLLMs (CV-MLLMs) across diverse RSISU tasks and benchmarks. RS-MLLMs remain competitive in domain-specific settings, particularly remote sensing visual grounding and high-resolution visual question answering. More notably, general-purpose CV-MLLMs can match or even outperform these specialized models on several RSISU tasks without remote sensing-specific fine-tuning. These findings demonstrate the strong transferability of general-purpose CV-MLLMs and show that current RS-MLLMs do not consistently outperform them across diverse RSISU tasks. Current MLLMs also face limitations in spatial and relational reasoning, fine-grained visual understanding, instruction diversity, and generalization across heterogeneous task formats. Based on these findings, we outline future directions toward reliable evaluation, multimodal and high-resolution reasoning, efficient deployment, and tool-augmented remote sensing agents. This survey provides a systematic reference for developing robust, generalizable, and practical MLLMs for RSISU.

### 🤖 AI 总结

**一句话总结**：The rapid development of multimodal large language models (MLLMs) has introduced a flexible paradigm for remote sensing image scene understanding (RSISU), enabling natural-language interaction with re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multimodal, Large, Language, Models, Remote, Sensing, Image, Understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20284v1) | [下载PDF](https://arxiv.org/pdf/2607.20284v1.pdf)

---

## [18. Self-supervision drives representational convergence in medical foundation models more than clinical supervision](https://arxiv.org/abs/2607.20274v1)

**作者**：Soroosh Tayebi Arasteh, Sebastian Ziegelmayer, Mahshad Lotfinia 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.CL, cs.LG  
**发布时间**：2026-07-22

### 📄 论文摘要

Medical image encoders from different groups are increasingly treated as interchangeable, on the assumption that scale and clinical supervision concentrate their representations onto a shared structure. Whether this convergence is real, what produces it, and whether it is clinically usable are untested, and the similarity measures behind such claims are fragile. We present a controlled dissection across 18 image and 7 text encoders, all open-weight and run locally, spanning 7M to 27B parameters and five imaging modalities, including 650,982 chest radiographs from six datasets. To isolate cause, we train encoders that vary only the objective under fixed data, architecture, and scale, and reproduce the effect in a synthetic model. Convergence is modest but above a random floor, driven by the self-supervised objective, not clinical supervision: matched self-supervised encoders aligned most (40.4% on chest radiography), with label-supervised (21.1%) and image-text (3.3%) far lower, and did not grow with size (Spearman 0.302, p=0.223) or capability. It is within-modality, does not reach clinical language, and does not reproduce how radiologists judge case similarity. Yet a linear classifier transfers across encoders and to five held-out hospitals, retaining about 85% of within-encoder performance. Convergence in medical imaging is therefore set by the pretraining objective, not inherited from scale or clinical supervision. Interoperability is accordingly something to design for through that objective, and to validate where the shared geometry is weakest, across patient subgroups and against clinical judgment.

### 🤖 AI 总结

**一句话总结**：Medical image encoders from different groups are increasingly treated as interchangeable, on the assumption that scale and clinical supervision concentrate their representations onto a shared structur...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Self-supervision, drives, representational, convergence, medical, foundation, models, more

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20274v1) | [下载PDF](https://arxiv.org/pdf/2607.20274v1.pdf)

---

## [19. How Does Urban Context Relate to Residential Building Health? A Vision-POI Fusion Framework for Building-Level Housing Inspection](https://arxiv.org/abs/2607.20263v1)

**作者**：Kun Zhao, Helei Ren, Guilin Tang 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-22

### 📄 论文摘要

Housing-level urban physical examination is essential for identifying residential building problems and supporting targeted urban renewal. Existing automated inspection studies primarily rely on individual images and rarely examine whether surrounding urban functional context can provide supplementary information for building-level assessment. This study proposes a vision-POI fusion framework that combines multi-view visual inspection with POI-derived neighborhood context for residential building health assessment. The empirical dataset covers 92 old residential communities, 3,237 residential buildings, and 25,608 field-acquired inspection images in Qingdao, China, encompassing seven categories of housing-related issues. First, multiple object detection models are evaluated to extract issue locations, categories, and confidence scores from individual images. The image-level outputs are subsequently aggregated across multiple views to construct interpretable building-level representations. Second, POI features are extracted within 500m, 1,000m, and 1,500m neighborhood buffers to characterize surrounding functional environments. Pearson and Spearman correlation analyses, combined with false discovery rate correction, are used to identify candidate contextual features. Finally, visual and POI features are integrated using a cost-sensitive Random Forest classifier under community-isolated spatial cross-validation. The results show that multi-view aggregation provides the main performance improvement, increasing the building-level Macro-F1 from 60.84% under Direct Detection to 74.95%. Incorporating POI context further increases Macro-F1 to 76.79%, although the additional gain is modest and category-dependent. POI information therefore functions as a supplementary contextual prior rather than a substitute for direct visual evidence or a causal determinant of building condition.

### 🤖 AI 总结

**一句话总结**：Housing-level urban physical examination is essential for identifying residential building problems and supporting targeted urban renewal. Existing automated inspection studies primarily rely on indiv...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：How, Does, Urban, Context, Relate, Residential, Building, Health?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20263v1) | [下载PDF](https://arxiv.org/pdf/2607.20263v1.pdf)

---

## [20. Not All Patches are Equal: Sampling Matters for Visible-Infrared Pre-Training](https://arxiv.org/abs/2607.20238v1)

**作者**：Qiwei Ma, Bin Deng, Junjie Zhu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-22

### 📄 论文摘要

Visible-infrared (VIS-IR) alignment is a key pre-training task for robust multi-sensor perception. Most existing methods use uniform patch-wise contrastive learning, but this can be unreliable in VIS-IR data because imaging-physics differences make some spatially paired regions inherently less comparable, and aligning them with equal strength hinders representation learning and downstream transfer. In this paper, we revisit VIS-IR pre-training from a sampling perspective and propose Importance-Aware Sampling (IAS), which adjusts training emphasis based on patch reliability. Specifically, IAS (i) derives patch weights from infrared structural cues and uses them to reweight the contrastive objective; (ii) learns a soft importance mask with a lightweight sampler, optionally warm-started from the hand-crafted prior; and (iii) employs a patch curriculum learning strategy that gradually expands from high-reliability regions to harder patches. It is worth noting that IAS is plug-and-play and works with both patch-/correlation-level alignment (e.g., UNIV-style) and image-level contrastive baselines (e.g., ImageBind-style). Extensive experiments on multiple VIS-IR benchmarks demonstrate consistent improvements over strong baselines, including for IR semantic segmentation, IR object detection and VIS semantic segmentation and cross-modal retrieval task. Code will be released on https://github.com/KlayMa527/IAS.

### 🤖 AI 总结

**一句话总结**：Visible-infrared (VIS-IR) alignment is a key pre-training task for robust multi-sensor perception. Most existing methods use uniform patch-wise contrastive learning, but this can be unreliable in VIS-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Not, All, Patches, Equal, Sampling, Matters, Visible-Infrared, Pre-Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20238v1) | [下载PDF](https://arxiv.org/pdf/2607.20238v1.pdf)

---

## cs.LG

## [21. PG-KINN: A Physics-Informed Petrov-Galerkin Kolmogorov-Arnold Network for Solving Forward and Inverse PDEs](https://arxiv.org/abs/2607.20378v1)

**作者**：Amirhossein Sadr, Nima Soltani, Vahideh Moghtadaiee 等 6 位作者  
**分类**：cs.LG, math.NA  
**发布时间**：2026-07-22

### 📄 论文摘要

Physics-informed learning of partial differential equations (PDEs) has been dominated by multilayer perceptrons (MLPs), whose spectral bias and dense parameterization limit both accuracy and interpretability. Kolmogorov Arnold Networks (KANs) mitigate these limitations because their learnable spline activations are structurally aligned with the piecewise-polynomial bases of classical discretizations. However, the way a PDE is cast into a loss functional is as decisive as the choice of approximator: strong-form residual minimization requires high-order derivatives and heavily weighted losses, the energy (Bubnov-Galerkin) form is restricted to self-adjoint operators and, as we show, collapses to a trivial solution for parameter-identification problems, and boundary integral forms require a known fundamental solution. We propose PG-KINN, a physics-informed KAN built on a Petrov-Galerkin formulation in which the trial space is a KAN and the test space is an independent, compactly supported, piecewise-polynomial space evaluated with Gauss-Legendre quadrature. Integration by parts lowers the differentiation order while retaining applicability to general non-self-adjoint, nonlinear, and inverse problems; the localized test functions turn the global residual into a set of element-wise weak residuals with favorable conditioning. On a suite of benchmarks spanning crack singularities, stress concentration, Neo-Hookean hyperelasticity, inverse parameter identification in heterogeneous media, and complex geometries, PG-KINN consistently outperforms legacy MLP baselines and state-of-the-art KAN-based strong/energy/inverse formulations (PIKAN). These results position the Petrov-Galerkin coupling of KAN trial spaces and polynomial test spaces as a robust and accurate route for AI-based computational mechanics.

### 🤖 AI 总结

**一句话总结**：Physics-informed learning of partial differential equations (PDEs) has been dominated by multilayer perceptrons (MLPs), whose spectral bias and dense parameterization limit both accuracy and interpret...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PG-KINN, Physics-Informed, Petrov-Galerkin, Kolmogorov-Arnold, Network, Solving, Forward, Inverse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20378v1) | [下载PDF](https://arxiv.org/pdf/2607.20378v1.pdf)

---

## [22. Online Variance Reduction for Domain Adaptation on Streaming Data](https://arxiv.org/abs/2607.20374v1)

**作者**：Andrea Napoli  
**分类**：cs.LG  
**发布时间**：2026-07-22

### 📄 论文摘要

This paper studies the problem of stochastic variance reduction (SVR) for the maximum mean discrepancy (MMD) and correlation alignment (CORAL) loss functions. Although various offline SVR algorithms for these losses have been proposed, these are incompatible with online, distributed, or incremental learning settings. This paper presents Adaptive vaRiance Reduction via Online reWeighting (ARROW), the first online SVR algorithm for the MMD and CORAL for streamed data. The method maintains moving average references of the alignment statistics, and adaptively reweights incoming minibatches so that the minibatch and reference statistics are aligned. Further, we propose a relaxed reweighting scheme so that the ensuing weight-optimisation problem is tractable. In experiments and simulations, we show that ARROW performs competitively with offline algorithms in terms of runtime, degree of variance reduction achieved, and target domain accuracy.

### 🤖 AI 总结

**一句话总结**：This paper studies the problem of stochastic variance reduction (SVR) for the maximum mean discrepancy (MMD) and correlation alignment (CORAL) loss functions. Although various offline SVR algorithms f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Online, Variance, Reduction, Domain, Adaptation, Streaming, Data, paper

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20374v1) | [下载PDF](https://arxiv.org/pdf/2607.20374v1.pdf)

---

## [23. Variance-reduced Domain Adaptation using Paired Sampling](https://arxiv.org/abs/2607.20367v1)

**作者**：Andrea Napoli  
**分类**：cs.LG  
**发布时间**：2026-07-22

### 📄 论文摘要

Correlation alignment and the maximum mean discrepancy are two widely used distribution-matching frameworks for unsupervised domain adaptation (UDA). However, high variance in these losses has been shown to undermine their effectiveness in minibatch optimisation settings. Furthermore, the losses lack finite-sum structure, which renders them incompatible with classical stochastic variance reduction (SVR) methods. This paper proposes Paired Sampling for Domain Adaptation (PSDA), a novel SVR technique tailored to such objectives. PSDA pairs observations both within and across domains, to form quadruplets that are always sampled together during training. The pairings are designed to minimise expected gradient variance, and reduce to solving a set of linear assignment problems. Our simulations demonstrate reduced variance compared to related methods, and experiments on three domain shift datasets show improved target domain accuracy.

### 🤖 AI 总结

**一句话总结**：Correlation alignment and the maximum mean discrepancy are two widely used distribution-matching frameworks for unsupervised domain adaptation (UDA). However, high variance in these losses has been sh...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Variance-reduced, Domain, Adaptation, Paired, Sampling, Correlation, alignment, maximum

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20367v1) | [下载PDF](https://arxiv.org/pdf/2607.20367v1.pdf)

---

## [24. Interval and fuzzy physics-augmented neural networks (iPANN and fPANN) for uncertainty quantification and propagation in constitutive modeling](https://arxiv.org/abs/2607.20339v1)

**作者**：Somesh Pratap Singh, Govinda Anantha Padmanabha, Jingye Tan 等 7 位作者  
**分类**：cs.LG, physics.comp-ph  
**发布时间**：2026-07-22

### 📄 论文摘要

Constitutive modeling under uncertainty remains a central challenge for reliable mechanics simulations, particularly when the available stress-deformation data are sparse, noisy, or heterogeneous. We propose interval and fuzzy physics-augmented neural networks (iPANNs and fPANNs) for uncertainty-aware hyperelastic constitutive modeling. iPANNs learn sparse lower, mean, and upper free energy density branches whose stresses, obtained by automatic differentiation, ultimately enclose noisy stress observations. In contrast to this deterministic interval description, fPANNs embed the learned iPANN branches into a fuzzy-set representation through alpha-cut interpolation, yielding a nested family of admissible responses. iPANNs and fPANNs encode mechanistic constraints - preserving objectivity, consistency and promoting polyconvexity - and smoothed L0 regularization promotes interpretable energy representations. The bound models are trained through a two-stage transfer-learning procedure in which a sparse mean constitutive response is learned first and then fine-tuned into lower and upper energy branches. We evaluate the framework on synthetic isotropic hyperelastic data with heteroscedastic noise, varying random realizations, shifted noise means, and varying noise magnitudes. The results show that the learned bounds enclose noisy stress observations while generalizing to the test set. Further, we examine the propagation of uncertainty through the mean, upper and lower bound predictions of the learned iPANN models in a finite element setting. The proposed framework provides a compact, physics-consistent route for distribution-free aleatoric uncertainty quantification in hyperelastic constitutive modeling, and propagation in downstream finite element simulations.

### 🤖 AI 总结

**一句话总结**：Constitutive modeling under uncertainty remains a central challenge for reliable mechanics simulations, particularly when the available stress-deformation data are sparse, noisy, or heterogeneous. We ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Interval, fuzzy, physics-augmented, neural, networks, iPANN, fPANN, uncertainty

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20339v1) | [下载PDF](https://arxiv.org/pdf/2607.20339v1.pdf)

---

## [25. Multi-modal transformer for signal classification in nanopore blockade experiments](https://arxiv.org/abs/2607.20323v1)

**作者**：Sandro Kuppel, Julian Hoßbach, Samuel Tovey 等 4 位作者  
**分类**：cs.LG, physics.comp-ph, q-bio.BM  
**发布时间**：2026-07-22

### 📄 论文摘要

Nanopore devices have emerged as powerful tools for single-molecule sensing, with potential for rapid, portable diagnostics. They detect changes in ionic current as analytes enter nanometer-scale pores, providing a means of identifying diverse biomarkers from their characteristic signal patterns. However, these signals are highly complex, and reliably assigning them to specific molecules remains a major challenge. Here, we address this by introducing a multi-modal deep learning architecture that jointly processes multiple signal representations, including raw time-series data, wavelet-based images, and static feature vectors. Our approach surpasses existing methods by more than 10 percentage points on a 42-peptide benchmark and transfers to a 20-amino-acid dataset with near-perfect accuracy. The model integrates complementary information from these representations, with attention analysis showing that the time-series and wavelet-image inputs emphasize different features of the same event. Together, these results demonstrate the potential of machine learning to enable robust, high-accuracy molecular identification with nanopore sensors.

### 🤖 AI 总结

**一句话总结**：Nanopore devices have emerged as powerful tools for single-molecule sensing, with potential for rapid, portable diagnostics. They detect changes in ionic current as analytes enter nanometer-scale pore...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-modal, transformer, signal, classification, nanopore, blockade, experiments, devices

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20323v1) | [下载PDF](https://arxiv.org/pdf/2607.20323v1.pdf)

---

## [26. Classical Hardware Acceleration of Quantum Autoencoders for Real-Time Anomaly Detection in Collider Experiments](https://arxiv.org/abs/2607.20302v1)

**作者**：Ivan Ge, Sagar Addepalli, Abhilasha Dave 等 4 位作者  
**分类**：cs.LG, hep-ph, physics.ins-det  
**发布时间**：2026-07-22

### 📄 论文摘要

Quantum machine learning (QML) algorithms in high energy physics (HEP) can efficiently represent and leverage long-range, high-order correlations in high-dimensional collider data, potentially with fewer parameters and favorable scaling relative to classical models. Deployment of QML in real-time collider applications such as trigger systems requires the ability to emulate and compile quantum circuits classically, then synthesize the resulting quantum gates onto low-latency hardware accelerators, namely field-programmable gate arrays (FPGAs). We present a study of variational quantum autoencoder models for real-time anomaly detection triggers in modern collider experiments. The models achieve performance comparable to state-of-the-art classical approaches and, after FPGA synthesis, satisfy resource usage and timing constraints consistent with trigger applications in future colliders. This work provides one of the first FPGA implementations of QML models for HEP triggers, enabling higher-capability models in today's classical data acquisition pipelines while advancing quantum readiness of collider experiment infrastructure.

### 🤖 AI 总结

**一句话总结**：Quantum machine learning (QML) algorithms in high energy physics (HEP) can efficiently represent and leverage long-range, high-order correlations in high-dimensional collider data, potentially with fe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Classical, Hardware, Acceleration, Quantum, Autoencoders, Real-Time, Anomaly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20302v1) | [下载PDF](https://arxiv.org/pdf/2607.20302v1.pdf)

---

## [27. The Blessing of Dimensionality: How Near-Orthogonality in High-Dimensional Spaces Explains Temporal Portability](https://arxiv.org/abs/2607.20301v1)

**作者**：Abigail Woodring, Adrian Chan, Rana Muhammad Shahroz Khan 等 6 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-07-22

### 📄 论文摘要

Fine-tuning has been widely used to adapt large language models (LLMs) for domain-specific tasks. Parameter efficient fine-tuning (PEFT) methods such as low-rank adaptation (LoRA) are frequently used to reduce computational costs. PortLLM is a training-free and data-free scheme used to adapt LLMs after continual pretraining. Although the initial PortLLM results show that LoRA patches exhibit short-term temporal portability, the long-term performance of PortLLM across several updates of continual pretraining remains underexplored. Furthermore, the intriguing effectiveness of PortLLM is not well understood from a theoretical standpoint. We address these two open questions by (1) performing an extensive empirical study of the long-term temporal portability of PortLLM patches across 10 continual pretraining steps using base models Mistral, Gemma, and Qwen; and (2) offering two theoretical analyses to explain our observation that the simple PortLLM method achieves competitive performance. We find empirically that the portability persists across longer time duration, indicating that repeated fine-tuning is not required when the base model is periodically updated. We find theoretically that near-orthogonality of high-dimensional vectors is a key justification for temporal portability. Our analyses also demonstrate a geometric perspective of the loss landscape in facilitating the theoretical comparison of different adaptation options.

### 🤖 AI 总结

**一句话总结**：Fine-tuning has been widely used to adapt large language models (LLMs) for domain-specific tasks. Parameter efficient fine-tuning (PEFT) methods such as low-rank adaptation (LoRA) are frequently used ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Blessing, Dimensionality, How, Near-Orthogonality, High-Dimensional, Spaces, Explains

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20301v1) | [下载PDF](https://arxiv.org/pdf/2607.20301v1.pdf)

---

## [28. Interpretable Fuzzy Rule-Based Regression Extension for Ex-Fuzzy Library](https://arxiv.org/abs/2607.20277v1)

**作者**：Cayan Deniz Kucuktopana, Javier Fumanal-Idocin, Richard Pitts 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-22

### 📄 论文摘要

Machine learning models achieve high predictive accuracy in regression tasks, but their deployment in safety-critical and regulated domains requires interpretability. While fuzzy rule-based systems offer transparent, linguistically explicit interpretable models, Mamdani-style fuzzy regression remains underrepresented in modern machine learning software libraries. This paper presents an interpretable regression extension for the Ex-Fuzzy library, enabling Mamdani fuzzy inference with scalar consequents learned directly from data. For this, a target-aware partition initialisation strategy based on Fuzzy C-Means clustering is introduced, in which linguistic variables are derived from an augmented input-output space to emphasise output-relevant regions of the feature space. The proposed extension is evaluated on ten regression datasets from the KEEL repository, comparing Gaussian and trapezoidal partition strategies against standard baselines including linear regression, multilayer perceptron, and random forests. Experimental results show that Gaussian partitions consistently outperform uniform trapezoidal partitions, achieving a mean coefficient of determination of approximately 0.86 while producing compact rule bases of 10-15 human-readable rules. The proposed implementation provides a transparent and competitive alternative to black-box regression models, supporting practical interpretability with competitive predictive performance.

### 🤖 AI 总结

**一句话总结**：Machine learning models achieve high predictive accuracy in regression tasks, but their deployment in safety-critical and regulated domains requires interpretability. While fuzzy rule-based systems of...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Interpretable, Fuzzy, Rule-Based, Regression, Extension, Ex-Fuzzy, Library, Machine

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20277v1) | [下载PDF](https://arxiv.org/pdf/2607.20277v1.pdf)

---

## [29. Breaking the $T^{3/4}$ Barrier for Regret Minimization With Bi-Dimensional CDFs](https://arxiv.org/abs/2607.20258v1)

**作者**：Matteo Castiglioni, Anna Lunghi, Alberto Marchesi  
**分类**：cs.LG  
**发布时间**：2026-07-22

### 📄 论文摘要

We study regret minimization for learning CDF-related objectives of the form \[ g(x)\cdot\mathbb{P}_{X\sim\mathcal{D}}(X\le x), \] over $[0,1]^2$, where $g$ is a known Lipschitz function and $\mathcal{D}$ is an unknown distribution. At each round $t$, the learner selects a point $x_t$ and observes the binary feedback $\mathbb{I}(X_t\le x_t)$, where $X_t\sim\mathcal{D}$. We design an algorithm achieving regret $\widetilde{\mathcal{O}}(T^{7/10})$, improving over the previous best-known bound of $\widetilde{\mathcal{O}}(T^{3/4})$ and showing that the curse of dimensionality can be at least partially lifted for this class of objectives, though a gap remains with the $Ω(T^{2/3})$ lower bound. As an application, our techniques yield the same $\widetilde{\mathcal{O}}(T^{7/10})$ regret bound for profit maximization in repeated bilateral trade with fixed prices.

### 🤖 AI 总结

**一句话总结**：We study regret minimization for learning CDF-related objectives of the form \[ g(x)\cdot\mathbb{P}_{X\sim\mathcal{D}}(X\le x), \] over $[0,1]^2$, where $g$ is a known Lipschitz function and $\mathcal...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：$T^, We, Breaking, Barrier, Regret, Minimization, Bi-Dimensional, CDFs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20258v1) | [下载PDF](https://arxiv.org/pdf/2607.20258v1.pdf)

---

## [30. PhaseAware: Interpretable Human-in-the-Loop Rehabilitation Scoring with Boundary Monitoring](https://arxiv.org/abs/2607.20237v1)

**作者**：Yankai Zheng, Yuhe Liu, Yuxin Ma 等 11 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-22

### 📄 论文摘要

Rehabilitation scoring systems are most useful when their outputs can be reviewed and interpreted within clinical workflows. This study presents PhaseAware, a compact framework for continuous rehabilitation quality assessment that combines a temporal backbone with phase- and body-group descriptors through a backbone-conditioned gated residual pathway. The model was evaluated on the UI-PRMD deep-squat protocol and further tested on the KIMORE squatting subset. On UI-PRMD, PhaseAware achieved an RMSE of 0.0230, corresponding to an 88.9% reduction relative to the accepted baseline. It also maintained favorable performance on KIMORE, suggesting that the phase-aware design transfers across related squatting protocols. In addition to score prediction, PhaseAware generates structured review cues based on phase- and body-level sensitivity, highlighting the movement stages and body regions most relevant to each prediction. The architecture employs a backbone-conditioned gated residual mechanism to stabilize feature representation, supporting use in resource-constrained settings. These cues are intended to support clinician review, boundary-case monitoring, and human-in-the-loop triage rather than autonomous decision-making. Overall, PhaseAware offers a practical and interpretable approach to rehabilitation scoring that may help integrate automated assessment into information systems while preserving clinician oversight.

### 🤖 AI 总结

**一句话总结**：Rehabilitation scoring systems are most useful when their outputs can be reviewed and interpreted within clinical workflows. This study presents PhaseAware, a compact framework for continuous rehabili...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PhaseAware, Interpretable, Human-in-the-Loop, Rehabilitation, Scoring, Boundary, Monitoring, systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.20237v1) | [下载PDF](https://arxiv.org/pdf/2607.20237v1.pdf)

---

