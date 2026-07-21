# arXiv AI 论文日报 | 2026-07-21

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (12 篇)
- [cs.CL](#csCL) (6 篇)
- [cs.AI](#csAI) (3 篇)
- [cs.LG](#csLG) (9 篇)

---

## cs.AI

## [1. Logical Judgments Under Pressure: Diagnosing Syllogistic Stability with Learned Soft Prefixes](https://arxiv.org/abs/2607.18228v1)

**作者**：Brian K Chen  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-07-20

### 📄 论文摘要

To test how correct logical judgments respond to learned context, we prepend a soft prefix to an exactly labeled syllogistic reasoning benchmark while keeping the model fixed. Soft prefixes are opaque continuous vectors, so we characterize them through the behavior they induce across controlled variations in logical form and interface. By studying which prefixes succeed and how their effects generalize, we characterize how learned contextual pressure can override correct judgments and expose limits in a model's logical stability. Across Qwen3.6-35B-A3B MoE, Qwen3-8B, and Gemma 4 31B, learned prefixes redirect many correct answers and remain effective across unseen forms and interface changes. In repeated tests with Qwen3.6 MoE and Gemma, they outperform paired random controls in all 16 model--direction--split comparisons by 37 to 99 percentage points. Qwen3.6 MoE flip rates remain between 72% and 90% across wording and prompt changes, while Gemma validity prefixes retain 54% to 56% flip compared with less than 1% for matched random prefixes. Diagnostic tests show that the dominant effect is a broad preference for one answer meaning rather than fixed-symbol forcing or a logical operation that transfers reliably between tasks. The form of this bias differs across models. In both Qwen models, simple score models often predict which judgments will flip but not how far their margins will move, whereas Gemma's overall response is more closely approximated by the same models. These results show that the dominant behavioral effect of successful soft prefixes is a broad answer preference, while the remaining response reveals substantial model-specific differences in logical stability.

### 🤖 AI 总结

**一句话总结**：To test how correct logical judgments respond to learned context, we prepend a soft prefix to an exactly labeled syllogistic reasoning benchmark while keeping the model fixed. Soft prefixes are opaque...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Logical, Judgments, Under, Pressure, Diagnosing, Syllogistic, Stability, Learned

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18228v1) | [下载PDF](https://arxiv.org/pdf/2607.18228v1.pdf)

---

## [2. SGA: Plug&Play Geometric Verification for Educational Video Synthesis](https://arxiv.org/abs/2607.18116v1)

**作者**：Lopez Jhon, Hinojosa Carlos, Ghanem Bernard  
**分类**：cs.AI, cs.CV, cs.GR, cs.MA, cs.MM  
**发布时间**：2026-07-20

### 📄 论文摘要

Recent work leverages Large Language Models (LLMs) to generate executable code for pedagogical animations using libraries such as Manim. However, ensuring spatial correctness and visual legibility remains challenging, as existing frameworks emphasize pedagogical content while overlooking geometric occlusions. We propose the Symbolic Geometric Agent (SGA), a plug-and-play module for code-centric animation pipelines that intercepts LLM-generated code, performs partial execution to extract symbolic scene graphs, and applies targeted refinement when spatial conflicts are detected. We further introduce the Manim Visual Quality Score (MVQS), a deterministic rendering-free proxy for spatial integrity. Experiments on the MMMC-Code benchmark across four LLM backbones and two agentic pipelines show that SGA achieves a peak MVQS of 73.11 (Code2Video + GPT-5.1), corresponding to a 16.1% relative improvement over the raw baseline, and improves MVQS in 7 of 8 backbone x pipeline configurations.

### 🤖 AI 总结

**一句话总结**：Recent work leverages Large Language Models (LLMs) to generate executable code for pedagogical animations using libraries such as Manim. However, ensuring spatial correctness and visual legibility rem...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SGA, Plug&Play, Geometric, Verification, Educational, Video, Synthesis, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18116v1) | [下载PDF](https://arxiv.org/pdf/2607.18116v1.pdf)

---

## [3. Judge-dependent safety gains and model-specific helpfulness costs of evidence-sufficiency prompting in clinical LLMs](https://arxiv.org/abs/2607.18086v1)

**作者**：Koyar Afrasyab  
**分类**：cs.AI  
**发布时间**：2026-07-20

### 📄 论文摘要

Background: LLM judges increasingly score whether clinical language models give overconfident answers under incomplete evidence, yet whether a measured "safety gain" reflects real behavior change or the judge's calibration is unresolved. Using a structured evidence-sufficiency prompt as a test case, we asked whether it reduces unsafe overconfident answers, how far that effect depends on the scoring judge, and what it costs in helpfulness.   Methods: In a retrospective public-data benchmark (Real-POCQi, HealthBench, MedRBench), four models (GPT-5.5, Claude Opus 4.8, Gemini 3.5 Flash, Grok 4.3) answered a fully paired common panel (1,200 cells) with a standard prompt and the wrapper. The pre-specified endpoint was the paired reduction in unsafe overconfidence scored by the primary judge (GPT-5.4-nano); secondary analyses added a different-family judge (Claude Sonnet 5), a correctness judge, matched scaffold controls, and a blinded three-clinician review.   Results: Unsafe overconfidence fell from 49.3% to 24.7%, a paired reduction of 24.7 points (95% CI 21.8-27.7; p<0.001), robust in direction across models and paraphrases. Magnitude was judge-dependent: Sonnet agreed on direction but nearly halved the effect (+13.1 points), with one-directional disagreement. Blinded clinicians characterized the primary judge as a high-sensitivity (1.00), low-specificity (0.55) screen, not a calibrated rate. The gain carried a model-specific helpfulness cost (correct diagnosis 80.3% to 50.3%): near-free for GPT-5.5, near-total for Gemini (-58 points). Matched scaffold controls showed genuine behavior change, not judge circularity.   Conclusions: LLM-judged clinical safety effects should be reported as directional and relative, anchored to human review and evaluated jointly with helpfulness, not as calibrated absolute rates. This does not establish clinical deployment readiness.

### 🤖 AI 总结

**一句话总结**：Background: LLM judges increasingly score whether clinical language models give overconfident answers under incomplete evidence, yet whether a measured "safety gain" reflects real behavior change or t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Judge-dependent, safety, gains, model-specific, helpfulness, costs, evidence-sufficiency

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18086v1) | [下载PDF](https://arxiv.org/pdf/2607.18086v1.pdf)

---

## cs.CL

## [4. Automated Discovery Has No Universally Superior Harness](https://arxiv.org/abs/2607.18235v1)

**作者**：Akshat Gupta, Jermaine Lei, Alexander Lu 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-20

### 📄 论文摘要

Autonomous discovery systems such as OpenEvolve and TTT-Discover are often used as general-purpose harnesses. However, in practice these are composite systems combining several design choices about archives, parent selection, exploration, and budget allocation into a single recipe. Because discovery runs are expensive and inherently stochastic, existing harnesses are often compared using too few independent trials to distinguish key methodological improvements from run-to-run variance. We systematically decompose OpenEvolve-style evolutionary search and the TTT-Discover search harness into its constituent components and systematically evaluate 30 budget-matched harnesses across 12 model-problem pairs using more than 3.1 million LLM rollouts and repeated-trial statistical analysis. Our results show that discovery harnesses have a generalization problem: No fixed harness is reliably superior across the evaluated model-problem pairs, and variants of OpenEvolve generally underperform simpler alternatives. Thus, harness choice is better viewed as a hyperparameter rather than as a universal recipe, and should be tailored to the specific problem and underlying model. We also find that early discovery progress predicts final performance, and use this property to present a budget-matched adaptive-allocation experiment that starts multiple harnesses, prunes weak partial runs, and reallocates compute to stronger survivors, outperforming both commitment to a randomly sampled fixed harness and a non-adaptive harness ensemble. Together, these results motivate shifting from fixed harness selection to online adaptation guided by early performance. We release all run pools including baseline null distributions for every model-problem pair as reusable statistical infrastructure against for future harness proposals.

### 🤖 AI 总结

**一句话总结**：Autonomous discovery systems such as OpenEvolve and TTT-Discover are often used as general-purpose harnesses. However, in practice these are composite systems combining several design choices about ar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：No, Automated, Discovery, Has, Universally, Superior, Harness, Autonomous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18235v1) | [下载PDF](https://arxiv.org/pdf/2607.18235v1.pdf)

---

## [5. It's Not What You Say, It's How You Say It: Evaluating LLM Responses to Expressions of Belief](https://arxiv.org/abs/2607.18232v1)

**作者**：Kevin Du, Clara Kümpel, Michelle Wastl 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-20

### 📄 论文摘要

Users frequently express their beliefs to large language models (LLMs). In some situations, the LLM should accept these contextual beliefs as true. In others, they should stick to their prior knowledge. Notably, users' expressions of belief (EoBs) can take linguistically diverse forms - using presuppositions, evidential and certainty markers, or varied tones - each of which may have a different persuasiveness over the LLMs. We introduce a typology to systematically evaluate how different EoBs affect whether models follow context versus prior knowledge. The typology is grounded in four linguistically motivated dimensions: form, evidentiality, epistemic stance, and tone, spanning 17 fine-grained types. By pairing these EoBs with world knowledge facts, we generate controlled EoB-query pairs that isolate the effect of linguistic variation. Using this benchmark, we evaluate 16 LLMs that differ in architecture (Llama3, Qwen3, Gemma3), scale (1B-30B parameters), and training stages (base vs instruct). We identify meaningful variations in response behavior across these axes, e.g., that bigger models and instruction models tend to be less context-following than smaller models and base models. We further identify specific EoBs that statistically significantly persuade LMs more consistently than others. Our work reveals systematic patterns in how linguistic framing affects LLM context integration, with implications for prompt engineering and model robustness.

### 🤖 AI 总结

**一句话总结**：Users frequently express their beliefs to large language models (LLMs). In some situations, the LLM should accept these contextual beliefs as true. In others, they should stick to their prior knowledg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：It, LLM, It's, Not, What, Say, How, Evaluating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18232v1) | [下载PDF](https://arxiv.org/pdf/2607.18232v1.pdf)

---

## [6. PPL-Factory: Task-Aware and Budget-Aware Data Selection from Language Modeling to Reasoning](https://arxiv.org/abs/2607.18199v1)

**作者**：Hang Zhang, Warren J. Gross  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-07-20

### 📄 论文摘要

Not all training samples contribute equally to large language model fine-tuning. Selecting informative training samples can reduce the computational cost while preserving downstream performance. Many existing data selection methods rely on indirect heuristics, such as data quality, diversity or reasoning trace length. However, the effectiveness of these fixed criteria is task-dependent and difficult to generalize across diverse downstream tasks. Perplexity-based data selection provides a simple and model-aware solution to estimate the sample difficulty, but existing approaches typically score the entire training sequence and ignore the difference in learning objectives of language modeling and reasoning tasks. In this paper, we propose PPL-Factory, a simple and interpretable data selection framework that combines task-aware perplexity-based scores and data budget-aware selection criteria. Experiments on GSM8K demonstrate that PPL-Factory outperforms other state-of-the-art data selection methods using only $1\%$ of the training set. With $10\%$ of the data, PPL-Factory exceeds full-data fine-tuning accuracy by 0.9 on GSM8K and 4.8 on MATH. Overall, our results demonstrate that task-aware and budget-aware perplexity-based selection provides an effective and applicable approach for efficient fine-tuning.

### 🤖 AI 总结

**一句话总结**：Not all training samples contribute equally to large language model fine-tuning. Selecting informative training samples can reduce the computational cost while preserving downstream performance. Many ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PPL-Factory, Task-Aware, Budget-Aware, Data, Selection, Language, Modeling, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18199v1) | [下载PDF](https://arxiv.org/pdf/2607.18199v1.pdf)

---

## [7. VEHBench: A Stage-Local Diagnostic Benchmark for LLM-Assisted Vibration Energy Harvester Design](https://arxiv.org/abs/2607.18181v1)

**作者**：Depeng Su, Yuyu Luo, Guobiao Hu  
**分类**：cs.CL, cs.SE  
**发布时间**：2026-07-20

### 📄 论文摘要

Battery-free Internet of Things (IoT) requires iterative design of vibration energy harvesters (VEHs) under coupled physical constraints, while LLMs are emerging as interface layers for engineering workflows. However, existing engineering benchmarks primarily assess final artifact validity, offering limited insights into how LLMs behave across different stages of coupled physical design. We introduce VEHBench, an engineering-native diagnostic benchmark for LLM-assisted VEH design, featuring 763 literature-grounded tasks scored by an analytical physical oracle. VEHBench evaluates four design roles: specification triage, verifier-guided search, corrupted-state recovery, and policy-conditioned selection. Experimental results reveal that LLM capability is strongly stage-dependent: no single model consistently dominates the entire workflow, and response-control profiles expose distinct behavioral patterns across design roles. VEHBench thus provides a stage-aware foundation for evaluating, selecting, routing, and improving verifier-grounded engineering LLMs. The benchmark artifact is available at https://huggingface.co/datasets/AnonymousVehbench/vehbench

### 🤖 AI 总结

**一句话总结**：Battery-free Internet of Things (IoT) requires iterative design of vibration energy harvesters (VEHs) under coupled physical constraints, while LLMs are emerging as interface layers for engineering wo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VEHBench, Stage-Local, Diagnostic, Benchmark, LLM-Assisted, Vibration, Energy, Harvester

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18181v1) | [下载PDF](https://arxiv.org/pdf/2607.18181v1.pdf)

---

## [8. How Does Alignment Tuning Shape Representations of Sycophancy and Related Cue-Induced Biases in LLMs?](https://arxiv.org/abs/2607.18114v1)

**作者**：Prakhar Gupta, Terry Jingchen Zhang, Florent Draye 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-07-20

### 📄 论文摘要

Modern LLMs are alarmingly susceptible to surprisingly simple immaterial changes of input prompts: a casual hint, an incorrectly labeled few-shot example, or a fake prior assistant turn often flips an originally correct answer. We study where this susceptibility, spanning sycophancy and related cue-induced biases, lives inside the model. Across five model families and seven BCT bias types, we extract a per-bias direction from hidden states and triangulate it through three measures: probing, leave-one-dataset-out transfer, and causal intervention. The susceptibility is largely installed by alignment tuning rather than pretraining: pretrained base models barely cave to these biases, and their activations carry no cue-specific signal beyond question content. Within aligned models, each bias becomes a single coherent direction that we can both decode and steer along, recovering the unbiased answer across every family we test. The biases stay representationally distinct, however: cross-bias entanglement is model-specific rather than a property of the bias category, and even behaviorally similar biases occupy different directions. The same intervention also serves as a modest debiasing tool, recovering a meaningful share of bias-induced errors while preserving most correct answers across all instruct families. Cue-induced bias is therefore best understood not as a single flaw in LLMs but as a family of distinct, causally active directions that alignment tuning installs.

### 🤖 AI 总结

**一句话总结**：Modern LLMs are alarmingly susceptible to surprisingly simple immaterial changes of input prompts: a casual hint, an incorrectly labeled few-shot example, or a fake prior assistant turn often flips an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, How, Does, Alignment, Tuning, Shape, Representations, Sycophancy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18114v1) | [下载PDF](https://arxiv.org/pdf/2607.18114v1.pdf)

---

## [9. VDAR-Router: Adaptive LLMs Routing via Verbalized Query Difficulty Analysis Retrieval](https://arxiv.org/abs/2607.18098v1)

**作者**：Yu-Chien Tang, Jun-Chen Hung, Wen-Chih Peng 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-20

### 📄 论文摘要

Large language models are increasingly used in practical systems, making efficient model selection important for reducing deployment cost. LLM routing has emerged as a practical solution for allocating each input query to an appropriate model under a desired cost-performance trade-off. Existing routing methods often estimate model suitability from the surface semantics or embedding similarity of the input query. However, such methods may ignore the underlying difficulty of a query, leading to suboptimal routing decisions. To address the challenge, we propose VDAR-Router, a difficulty-aware retrieval-based routing framework. For each input query, VDAR-Router first generates an explicit difficulty analysis. It then retrieves historical examples with similar difficulty profiles. Based on the retrieved records, it estimates candidate model suitability and selects the model using a reward function that considers both performance and cost. Experiments on three datasets show that VDAR-Router consistently achieves better cost-performance trade-offs than existing baselines. These results demonstrate the effectiveness of difficulty-aware retrieval for training-free LLM routing. Case studies further show that explicit query analysis helps retrieve more relevant examples and supports more reliable routing decisions.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly used in practical systems, making efficient model selection important for reducing deployment cost. LLM routing has emerged as a practical solution for allocatin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, VDAR-Router, Adaptive, Routing, via, Verbalized, Query, Difficulty

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18098v1) | [下载PDF](https://arxiv.org/pdf/2607.18098v1.pdf)

---

## cs.CV

## [10. The Many Senses of Visual Similarity: A Text-Prompted Image Perceptual Metric](https://arxiv.org/abs/2607.18237v1)

**作者**：Sheng-Yu Wang, Yotam Nitzan, Aaron Hertzmann 等 7 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-07-20

### 📄 论文摘要

Human visual similarity judgments are context-dependent. For example, two images may be similar in shape but distinct in color. Existing perceptual similarity metrics, however, collapse these nuances into a single scalar value, offering no mechanism to condition on specific aspects. To bridge this gap, we introduce a large-scale dataset of human similarity judgments over image triplets, where each triplet is annotated across multiple, free-form semantic aspects of similarity. Benchmarking a broad range of frontier vision-language models (VLMs) reveals a considerable performance gap compared to human annotators' consensus. Leveraging our data, we fine-tune a VLM to produce our Text-Prompted Image Perceptual Similarity (TPIPS) metric, capturing multiple senses of visual similarity depending on the specified text prompt. We demonstrate that TPIPS aligns more closely with human perception and generalizes reliably beyond the training distribution. Finally, we show that TPIPS unlocks new capabilities in text-guided retrieval, compositional search, and the fine-grained evaluation of generative models. Our code, data, and trained models are at https://peterwang512.github.io/TPIPS

### 🤖 AI 总结

**一句话总结**：Human visual similarity judgments are context-dependent. For example, two images may be similar in shape but distinct in color. Existing perceptual similarity metrics, however, collapse these nuances ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Many, Senses, Visual, Similarity, Text-Prompted, Image, Perceptual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18237v1) | [下载PDF](https://arxiv.org/pdf/2607.18237v1.pdf)

---

## [11. Simple Domain Generalization for Strong Pixel-Level Image Tampering Detection in Modern VLMs](https://arxiv.org/abs/2607.18230v1)

**作者**：Yi Tang, Xinyi Shang, Jiacheng Cui 等 15 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-20

### 📄 论文摘要

Modern vision-language models (VLMs) have significantly improved image generation and editing capabilities, making pixel-level image tampering detection increasingly important yet challenging under cross-model and out-of-distribution shifts. This work studies domain generalization for pixel-level image tampering detection in modern VLMs like ChatGPT, Gemini, Qwen-Image, etc., aiming to learn tampering localization models that remain robust across diverse VLM-generated manipulation distributions. We propose a simple yet effective domain-generalized training framework built on two practical strategies. First, we introduce a balanced minibatch sampling scheme that strategically samples tampered and real images in each minibatch, preventing biased optimization toward either manipulated artifacts or clean-image priors and avoiding training collapse, ensuring that each optimization step receives proper sampled gradient signals. Second, we adopt a simple late-injection strategy, where the detector is first trained on large-scale base data until stable convergence, and then exposed to a small amount of newly selected supporting data from emerging VLM distributions, improving adaptability without overfitting to limited new domains. Together, these components provide a simple yet strong recipe for improving pixel-level tampering localization and OOD robustness across modern VLMs. Despite the conceptual simplicity, our framework outperforms the prior state-of-the-art PIXAR by a large margin of 26.1% and 26.8% relative improvement in average gIoU and cIoU, respectively, across OOD VLMs of GPT-Images-2.0, Gemini-3.1, FLUX.2, and Seedream 4.5. Our code is available at https://github.com/VILA-Lab/PIXAR-DG

### 🤖 AI 总结

**一句话总结**：Modern vision-language models (VLMs) have significantly improved image generation and editing capabilities, making pixel-level image tampering detection increasingly important yet challenging under cr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Simple, Domain, Generalization, Strong, Pixel-Level, Image, Tampering, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18230v1) | [下载PDF](https://arxiv.org/pdf/2607.18230v1.pdf)

---

## [12. FlowMimic: Mask-free Visual Editing and Generation with Pixel-pair Warped Flow Field for Online Video Editing Data Generation and Modality Mimicry](https://arxiv.org/abs/2607.18227v1)

**作者**：Dingyun Zhang, Lixue Gong, Wei Liu  
**分类**：cs.CV  
**发布时间**：2026-07-20

### 📄 论文摘要

In line with the prevailing direction of vision research, we explore the integration of both generation and editing capabilities for video and image modalities within a single model. Current approaches to collecting video editing data typically depend on labour-intensive, time-consuming curated procedures--involving object mask annotation, the use of error-introducing pair synthesis via I2V model and ControlNet-like guidance, and VLM-based quality filtering or refinement--and demonstrate limited task scalability. As a result, the diversity of editing tasks remains substantially narrower than that available for image editing models. We develop a pixel-pair temporal warped flow field that can directly generate corresponding video editing samples in real time from image editing samples, and we demonstrate across multiple levels of video editing tasks that a model can learn video editing using only such data. We regard the image modality as a particular form of the video modality. Accordingly, we design a modality mimic generation loss and a modality mimic editing loss to relatively align the capabilities--and thereby the output distributions--of the two modalities through mutual imitation. Moreover, language-based visual editing entails the comprehension of the editing instruction and the reference visual content, the localization of the region corresponding to that instruction within the reference visual contents, and the modification of that region alone. Existing approaches predominantly rely on external aids, such as fine-tuning an additional MLLM or explicitly supplying a mask sequence as auxiliary input during inference. In contrast, we aspire for the model to internalize this capability. To that end, we introduce sense-related tasks--for instance, referring expression segmentation--along with corresponding editing-region-aware latent-level loss and attention-level loss.

### 🤖 AI 总结

**一句话总结**：In line with the prevailing direction of vision research, we explore the integration of both generation and editing capabilities for video and image modalities within a single model. Current approache...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FlowMimic, Mask-free, Visual, Editing, Generation, Pixel-pair, Warped, Flow

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18227v1) | [下载PDF](https://arxiv.org/pdf/2607.18227v1.pdf)

---

## [13. GigaPath-Flash and GigaTIME-Flash: Efficient Pathology Foundation Models for Whole-Slide and Tumor Microenvironment Analysis](https://arxiv.org/abs/2607.18218v1)

**作者**：Naoto Usuyama, Jeya Maria Jose Valanarasu, Sicong Yao 等 27 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-20

### 📄 论文摘要

Foundation models have emerged as a driving force in computational pathology, with the potential to transform cancer diagnosis, prognosis, and treatment selection by learning transferable representations from large-scale histopathology data. A growing landscape of pathology foundation models now spans diverse data sources, architectures, and downstream applications. However, most pretrained models operate only at the image-tile level, use restrictive licenses, and remain computationally expensive, limiting large-scale slide-level clinical and research use.   Here, we introduce GigaPath-Flash and GigaTIME-Flash, efficient models for whole-slide pathology AI and spatial proteomics prediction. GigaPath-Flash combines a 22M-parameter ViT-S tile encoder with a 21M-parameter LongNet slide encoder, both pretrained on large-scale real-world histopathology data. Its compact tile encoder is distilled from the billion-parameter GigaPath (ViT-g) teacher and shared by both models. GigaPath-Flash retains 97% of GigaPath's average slide-level performance with 50x less compute. GigaTIME-Flash extends this backbone to predict the tumor immune microenvironment directly from routine H&E images. It surpasses the original CNN-based GigaTIME in prediction quality while running 6x faster and using 8x less GPU memory.   Together with GigaPath and GigaTIME, these models form an open-weight, Apache-2.0-licensed family pretrained on large-scale real-world clinical data. By releasing all models and weights, we provide accessible building blocks for computational pathology, immuno-oncology, and precision health.

### 🤖 AI 总结

**一句话总结**：Foundation models have emerged as a driving force in computational pathology, with the potential to transform cancer diagnosis, prognosis, and treatment selection by learning transferable representati...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GigaPath-Flash, GigaTIME-Flash, Efficient, Pathology, Foundation, Models, Whole-Slide, Tumor

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18218v1) | [下载PDF](https://arxiv.org/pdf/2607.18218v1.pdf)

---

## [14. Certified Training for Convolutional Perturbations](https://arxiv.org/abs/2607.18195v1)

**作者**：Benedikt Brückner, Alessio Lomuscio  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-07-20

### 📄 论文摘要

Vision models have been found to be susceptible to perturbations such as motion blur induced at runtime by a shaking camera. This impedes their deployment in critical applications since phenomena such as slightly blurred vision might lead to failures, for example an object detector missing objects. While methods such as data augmentation or Adversarial Training can improve empirical robustness, they lack formal safety guarantees, making it difficult to identify and mitigate hidden vulnerabilities. We introduce a novel Certified Training approach that leverages an efficient encoding of convolutional perturbations to train provably robust models. Our method significantly outperforms Adversarial Training, achieving, for example, over 80% robust accuracy against motion blur of reasonable intensity on CIFAR10 while maintaining comparable standard accuracy.

### 🤖 AI 总结

**一句话总结**：Vision models have been found to be susceptible to perturbations such as motion blur induced at runtime by a shaking camera. This impedes their deployment in critical applications since phenomena such...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Certified, Training, Convolutional, Perturbations, Vision, models, have, been

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18195v1) | [下载PDF](https://arxiv.org/pdf/2607.18195v1.pdf)

---

## [15. Robust Multimodal Dynamic Object Segmentation](https://arxiv.org/abs/2607.18153v1)

**作者**：Zhe Xin, Hanzhi Chang, Penghui Huang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-20

### 📄 论文摘要

Dynamic object segmentation plays a critical role in many visual applications such as static scene reconstruction from dynamic videos. However, existing optical flow-based methods fail to ensure consistent static/dynamic segmentation along object boundaries, while 3D reconstruction-based approaches are highly sensitive to reconstruction errors. To address these limitations, we present a dynamic object segmentation framework that can generate both precise and complete dynamic masks by integrating multimodal cues including 2D point tracks, 3D reconstruction, and semantic information. We design a network combining Transformer architectures with feature clustering aggregation modules to perform static/dynamic classification of multimodal feature trajectories. It enables the model to adaptively determine which type of feature should dominate based on the characteristics of each scene, while also mitigating the impact of feature degradation. Additionally, we introduce a novel point-query-based SAM post-processing method capable of handling multiple objects within a single mask. Extensive experiments demonstrate that our approach achieves state-of-the-art performance in both dynamic object segmentation and static scene reconstruction tasks.

### 🤖 AI 总结

**一句话总结**：Dynamic object segmentation plays a critical role in many visual applications such as static scene reconstruction from dynamic videos. However, existing optical flow-based methods fail to ensure consi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Robust, Multimodal, Dynamic, Object, Segmentation, plays, critical, role

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18153v1) | [下载PDF](https://arxiv.org/pdf/2607.18153v1.pdf)

---

## [16. Plenoptic Condensation: A Novel Approach to Generalized Scene Reconstruction](https://arxiv.org/abs/2607.18151v1)

**作者**：Brevin Tilmon, Alex DeJournett, John Leffingwell 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-20

### 📄 论文摘要

We present a novel Generalized Scene Reconstruction (GSR) approach called Plenoptic Condensation (PCon). PCon uses a multi-stage reconstruction pipeline, initially converting images into "soupy" scene elements with low (representational) power, then adaptively condensing the "soup" into "structured" elements of higher power capable of efficiently representing, for example, sharp edges and smooth reflective surfaces. PCon scene models called Reality Models (Relms) enable spatially varying representational power, which is essential for high-fidelity rendering, measurement, and scene understanding. We showcase several in-the-wild PCon reconstructions captured with consumer phone cameras and drones. In one case called "Damaged Fiat", PCon is benchmarked against two state-of-the-art (SOTA) GSR methods: NeRO and RT-Splatting. Referring to Figure 1 below, PCon reconstructs the car hood more than twice as accurately as the SOTA methods. But more importantly, the local damage profile error for PCon is 35 um (0.035 mm), whereas the two other SOTA methods are essentially unable to measure the damage at all. Our project website is available at https://quidient.github.io/pcon-2026.html.

### 🤖 AI 总结

**一句话总结**：We present a novel Generalized Scene Reconstruction (GSR) approach called Plenoptic Condensation (PCon). PCon uses a multi-stage reconstruction pipeline, initially converting images into "soupy" scene...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Plenoptic, Condensation, Novel, Approach, Generalized, Scene, Reconstruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18151v1) | [下载PDF](https://arxiv.org/pdf/2607.18151v1.pdf)

---

## [17. Lossless-INR: Lossless Volumetric Implicit Neural Representations](https://arxiv.org/abs/2607.18150v1)

**作者**：Kaiyuan Tang, Daniel Burke, Chaoli Wang  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-07-20

### 📄 论文摘要

Implicit neural representation (INR) methods provide continuous coordinate-to-value mappings and integrate naturally with direct volume rendering, making them attractive for representing volumetric data. However, existing INR-based approaches for volumetric data are inherently lossy, and even small reconstruction errors can propagate through rendering and downstream analysis. In this work, we explore Lossless-INR, a lossless INR framework for 3D scientific volumetric data based on bit-plane decomposition. By decomposing each voxel value into binary bit-planes, we reformulate reconstruction as per-bit binary classification, so that exact recovery reduces to predicting every bit correctly. To make this optimization tractable while keeping the representation compact, we combine an octree block-partitioning strategy that adaptively subdivides complex regions with a ternary feature-grid network whose grid entries are parameterized by a ternary set of values. Experiments on diverse volumetric datasets show that this design can achieve zero bit-error rate and bit-exact reconstruction, enabling faithful rendering and downstream analysis with a compact representation. The code is available at https://github.com/TouKaienn/Lossless-INR.

### 🤖 AI 总结

**一句话总结**：Implicit neural representation (INR) methods provide continuous coordinate-to-value mappings and integrate naturally with direct volume rendering, making them attractive for representing volumetric da...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Lossless-INR, Lossless, Volumetric, Implicit, Neural, Representations, representation, INR

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18150v1) | [下载PDF](https://arxiv.org/pdf/2607.18150v1.pdf)

---

## [18. O-VAD: Industrial Video Anomaly Detection through Object-Centric Tracking and Reasoning](https://arxiv.org/abs/2607.18142v1)

**作者**：Mei Yuan, Qi Long, Qifeng Wu 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.CL, cs.MA  
**发布时间**：2026-07-20

### 📄 论文摘要

Industrial Video Anomaly Detection (IVAD) aims to identify anomalous objects and events in an industrial process, which is crucial for modern manufacturing and quality control systems. Existing VLM-based anomaly reasoning methods are capable of detecting open-ended anomalies in general domains. However, their performance declines in industrial settings characterized by intricate object transformations, strict physics, and procedural constraints. To tackle the complexity of such interaction-intensive detection, we introduce a training-free agentic framework for anomaly detection free of domain-specific knowledge, emphasizing object state evolution like humans inspectors. It is designed to track spatial-temporal dynamics and underlying transformations of detected objects over time, and then reason over the object-wise temporal state trajectories to identify abnormal objects in grounded frames. Our method overcomes limitations of prior approaches that rely on retraining on normal clips or injecting domain knowledge as context for test-time inference. Extensive experiments on three IVAD datasets demonstrate that our method outperforms frontier VLMs, agentic frameworks, and traditional VAD methods fine-tuned on the respective datasets, while providing interpretable reports over anomaly processes and types.

### 🤖 AI 总结

**一句话总结**：Industrial Video Anomaly Detection (IVAD) aims to identify anomalous objects and events in an industrial process, which is crucial for modern manufacturing and quality control systems. Existing VLM-ba...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：O-VAD, Industrial, Video, Anomaly, Detection, through, Object-Centric, Tracking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18142v1) | [下载PDF](https://arxiv.org/pdf/2607.18142v1.pdf)

---

## [19. Occlusion-Aware Panoptic Segmentation with Joint Position Embedding and Occlusion-Level Attention](https://arxiv.org/abs/2607.18112v1)

**作者**：Wenbo Wei, Jun Wang, Shan Raza 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-20

### 📄 论文摘要

Panoptic segmentation in complex scenes remains challenging because of occlusions, yet modern approaches often neglect occlusion modelling. In this paper, we propose \textbf{P}osition \textbf{E}mbedding \textbf{M}odulation with \textbf{O}cclusion-\textbf{L}evel \textbf{A}ttention (PEMOLA), a novel occlusion-aware module that can be seamlessly integrated into transformer-based panoptic segmentation. To obtain occlusion cues, we train an occlusion classifier on the COCO-OLAC dataset. The classifier derives the occlusion-level attention, which serves as spatial guidance, while the occlusion labels are encoded into a learnable embedding to produce channel-wise weights. Through joint modulation, PEMOLA elegantly introduces the occlusion priors into the position embedding, thereby improving the occlusion modelling. We further annotate the Cityscapes dataset with occlusion levels, termed Cityscapes Occlusion Labels for All Computer Vision Tasks (Cityscapes-OLAC), following the same labelling protocol as COCO-OLAC, to evaluate the cross-dataset generalisation ability of PEMOLA. Extensive experiments on COCO-OLAC and Cityscapes-OLAC demonstrate that PEMOLA consistently improves panoptic segmentation quality while introducing minimal computational overhead. These results highlight the importance of occlusion modelling, where incorporating occlusion-level attention helps deliver robust panoptic segmentation under occlusion. Code and dataset are available at https://github.com/wenbo-wei/PEMOLA.

### 🤖 AI 总结

**一句话总结**：Panoptic segmentation in complex scenes remains challenging because of occlusions, yet modern approaches often neglect occlusion modelling. In this paper, we propose \textbf{P}osition \textbf{E}mbeddi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Occlusion-Aware, Panoptic, Segmentation, Joint, Position, Embedding, Occlusion-Level, Attention

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18112v1) | [下载PDF](https://arxiv.org/pdf/2607.18112v1.pdf)

---

## [20. SpEmoC: A Balanced Speaker-Segment Multimodal Emotion Benchmark](https://arxiv.org/abs/2607.18109v1)

**作者**：Sania Bano, Shahzad Ahmad, Santosh Kumar Vipparthi 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-20

### 📄 论文摘要

Understanding human emotions in spoken conversations is a key challenge in affective computing, with applications in empathetic AI, human computer interaction, and mental health monitoring. However, existing datasets vary in scale, emotion distribution, modality alignment, and data partitioning strategies, which can influence reliable cross-dataset generalization and minority-emotion modeling. We introduce SpEmoC a Speaking segment Emotion for Conversations comprising 306,544 raw clips from 3,100 English language movies and TV series. From these, 30,000 high quality, class balanced clips are curated, featuring synchronized visual, audio, and textual modalities annotated for seven emotions through a hybrid pipeline that integrates pretrained models with human validation. SpEmoC uses strict movie- and series-level splits to prevent content overlap between split sets, allowing more reliable evaluation of model generalization. The dataset also maintains a near-balanced distribution across seven emotions, including minority classes such as Fear and Disgust, which supports more balanced learning across categories. Extensive experiments, including in-domain benchmarking, cross-dataset transfer, low-data training, class-imbalance analysis, and modality transfer show that balanced data and careful splitting lead to more stable performance across emotions when models are evaluated on other datasets. These results highlight the importance of dataset design for robust and transferable multimodal emotion recognition.

### 🤖 AI 总结

**一句话总结**：Understanding human emotions in spoken conversations is a key challenge in affective computing, with applications in empathetic AI, human computer interaction, and mental health monitoring. However, e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SpEmoC, Balanced, Speaker-Segment, Multimodal, Emotion, Benchmark, Understanding, human

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18109v1) | [下载PDF](https://arxiv.org/pdf/2607.18109v1.pdf)

---

## [21. SciForma: Structure-Faithful Generation of Scientific Diagrams](https://arxiv.org/abs/2607.18091v1)

**作者**：Yuxuan Luo, Peng Zhang, Xinjie Zhang 等 6 位作者  
**分类**：cs.CV, cs.GR, cs.LG  
**发布时间**：2026-07-20

### 📄 论文摘要

Structural fidelity is essential to scientific methodology diagrams. To communicate research logic, these diagrams must faithfully render components, directional relations, and textual annotations. Since a single error, such as a reversed arrow or an unreadable equation, can invalidate the entire figure, structural fidelity is inherently conjunctive: correctness on one axis cannot compensate for failure on another. Current open-source models fail to satisfy this criterion. Supervised fine-tuning (SFT) learns plausible layouts but cannot reliably ensure structural correctness, while scalar reward-based post-training obscures which structural dimension has failed. To address this, we introduce SciForma, a framework for the structure faithful generation of scientific methodology diagrams. Specifically, SciForma decomposes diagram quality into three structural axes: Component, Arrow, and Text, guided by a structural inventory. Built on this foundation, we curate SciFormaData-700K for structured training and SciFormaBench-2K for logic-verified evaluation. To close the gap left by SFT, we develop Multi-Dimensional Conjunctive Preference Optimization (M-DPO), which enforces simultaneous correctness across all axes and adaptively routes gradients to the most deficient dimension in post-training. The same structural inventory also enables iterative editing at inference time to correct residual errors. This combination allows SciForma-9B to exceed all open-source baselines and GPT-Image-1.5 on both SciFormaBench-2K and AIBench, bringing open scientific diagram generation close to proprietary-level structural fidelity. Our code and data will be available at: https://github.com/microsoft/SciForma.

### 🤖 AI 总结

**一句话总结**：Structural fidelity is essential to scientific methodology diagrams. To communicate research logic, these diagrams must faithfully render components, directional relations, and textual annotations. Si...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, SciForma, Structure-Faithful, Generation, Scientific, Diagrams, Structural, fidelity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18091v1) | [下载PDF](https://arxiv.org/pdf/2607.18091v1.pdf)

---

## cs.LG

## [22. Three-Body Scattering for Generative Modeling](https://arxiv.org/abs/2607.18198v1)

**作者**：Peng Sun, Zhenglin Cheng, Deyuan Liu 等 6 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-07-20

### 📄 论文摘要

Modern generative models typically rely on an adversarial critic, a prescribed noise-to-data path, or an autoregressive factorization. Instead, we show that a proper distributional energy can induce sample-level motion and provide direct regression supervision for a one-step generator. Three-Body Scattering Modeling (TBSM) for generation turns the energy distance into a constant-size per-projectile interaction: each projectile is attracted toward one real source and repelled from one independently generated source. Conditioned on the projectile and its condition, its expectation equals the $2$-Wasserstein gradient-flow velocity of $\frac12D_E^2(P_θ,Q)$. A batch of $B$ frozen-target events yields $O(B)$ sample-level losses, each using one reference for its condition instead of the minibatch-wide all-pairs field used by methods such as Drifting Models. Tracking this conditional expectation online can reduce field noise. Using scattering in frozen image features, TBSM trains one-step generators on ImageNet-256, achieving FID${}=2.23$ with pixel-space PixelDiT-XL and FID${}=1.63$ with latent-space DiT-XL at NFE${}=1$. We provide a design map relating diffusion-related supervision, Drift-like dynamics, and GAN-like objectives. These results establish tracked scattering as a route to high-dimensional one-step generation. Code: https://github.com/sp12138/TBSM.

### 🤖 AI 总结

**一句话总结**：Modern generative models typically rely on an adversarial critic, a prescribed noise-to-data path, or an autoregressive factorization. Instead, we show that a proper distributional energy can induce s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Three-Body, Scattering, Generative, Modeling, Modern, models, typically, rely

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18198v1) | [下载PDF](https://arxiv.org/pdf/2607.18198v1.pdf)

---

## [23. FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications](https://arxiv.org/abs/2607.18171v1)

**作者**：Krish Agarwal, Zhuoming Chen, Yanyuan Qin 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-20

### 📄 论文摘要

Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisions about placement, streaming, and intra-model parallelism. Existing serving systems and auto-parallelism compilers commit to limited transformations and fixed workload assumptions, so achieving high performance on a new application requires hand-crafting an efficient implementation. We present FlashRT, an agent harness that guides coding agents to lift simple developer-written reference implementations into optimized multi-GPU deployments that flexibly weigh target metrics like latency and throughput. Using a new chain-of-program paradigm, FlashRT directs a generic coding agent through a multi-pass transformation process where an agent transforms the reference into an intermediate representation (IR) to capture data dependencies and persistent-state scopes, validates this IR via a sequential interpreter, and performs static analyses to identify candidate transformations. Then, the agent iteratively implements, verifies, and benchmarks each candidate under a measurement-gated optimization loop to produce effective deployments that span different hardware budgets. Across various applications, including video world models and multimodal LLMs, FlashRT converts reference implementations into highly efficient deployments, delivering up to ~70x latency reduction and 2.8x throughput improvement on NVIDIA B200 GPUs. On AMD MI355X GPUs, FlashRT matches the peak latency reduction while increasing peak throughput improvement to 3.6x, demonstrating that agent-driven optimization can be more scalable on platforms with less mature expert optimization. In fact, for Qwen3-Omni text-to-audio inference, FlashRT reduces response latency by 65% compared to the expert vLLM-Omni implementation on AMD MI355X.

### 🤖 AI 总结

**一句话总结**：Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, FlashRT, Harness, Guiding, Deploy, Real-Time, Multimodal, Applications

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18171v1) | [下载PDF](https://arxiv.org/pdf/2607.18171v1.pdf)

---

## [24. The Calibration Channel Determines the Bayes-Error Proxy: An Exact Law for Temperature-Induced Distortion](https://arxiv.org/abs/2607.18162v1)

**作者**：Shreyas Pradeepkumar Khandale  
**分类**：cs.LG  
**发布时间**：2026-07-20

### 📄 论文摘要

The soft-label Bayes-error estimator beta(z) = E[min(z, 1-z)] of Ishida et al. estimates the irreducible error of a binary task directly from probability-valued labels. Recent work by Ushio et al. showed that this estimator is fragile when the probabilities are not the true posterior: even perfectly calibrated soft labels can yield a substantially inaccurate estimate, and they propose isotonic calibration as a consistent remedy. We complement that line of work by characterizing exactly how the most widely used post-hoc calibration map -- temperature scaling -- distorts the proxy. We prove an exact, model-free identity reducing the temperature-scaled proxy to the classifier's margin distribution, from which we obtain (i) strict monotonicity in the temperature and (ii) a continuous bijection from the temperature axis onto the open interval (0, 1/2), so that a fixed classifier -- with fixed decisions and fixed 0-1 error -- can be made to report any proxy value whatsoever. Under a Gaussian model of the logits we further derive a two-parameter closed form for the entire proxy-versus-temperature curve. Across CIFAR-10, Fashion-MNIST, and SVHN (eight binary tasks), the proxy varies by 56x to 980x at constant test error, the closed form reproduces the empirical curve to within 0.018, and the calibration temperature that minimizes the expected calibration error does not coincide with any stable proxy value. Our results give a precise, predictive account of the distortion whose existence motivates calibration-based remedies, and they reinforce the practical recommendation that a proxy value is meaningful only together with the mechanism that produced its probabilities.

### 🤖 AI 总结

**一句话总结**：The soft-label Bayes-error estimator beta(z) = E[min(z, 1-z)] of Ishida et al. estimates the irreducible error of a binary task directly from probability-valued labels. Recent work by Ushio et al. sho...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Calibration, Channel, Determines, Bayes-Error, Proxy, Exact, Law

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18162v1) | [下载PDF](https://arxiv.org/pdf/2607.18162v1.pdf)

---

## [25. Differentiable Logic Gate Networks for Low-Latency EEG Classification on Edge Devices](https://arxiv.org/abs/2607.18149v1)

**作者**：Shyamal Y. Dharia, Stephen D. Smith, Camilo E. Valderrama  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-20

### 📄 论文摘要

Real-time EEG classification on edge devices is bottlenecked by the floating-point arithmetic of conventional neural networks. We investigated Differentiable Logic Gate Networks (Diff-Logic) as a hardware-native alternative that compiles models into pure Boolean circuits executable via bitwise CPU operations. Through rigorous iso-parameter experiments across four EEG datasets spanning two classification tasks, binary dementia detection and 3-class emotion recognition, we compared Diff-Logic against matched-capacity Multi-Layer Perceptron (MLP) and Binarized Neural Network (BNN) baselines at four complexity tiers (50k-500k parameters). On dementia screening, Diff-Logic achieved 80.2% Macro F1, outperforming the MLP baseline by 6.8%. On emotion recognition, the MLP retained a moderate performance advantage but incurred a 2.3$\times$ higher latency and 14$\times$ larger model size when deployed on a power-constrained (7W) Nvidia Jetson Orin Nano CPU (Single-core). Critically, Diff-Logic inference time remained nearly constant across a 10$\times$ increase in model scale, achieving a peak speedup of 2.9$\times$ over MLPs at the largest complexity tier. Our results establish logic-based neural architectures as a practical paradigm for resource-constrained brain-computer interfaces, achieving competitive or superior performance while natively satisfying the latency and memory constraints of portable edge deployment. Code is available on GitHub: https://github.com/Shyamal-Dharia/eeg-difflogic

### 🤖 AI 总结

**一句话总结**：Real-time EEG classification on edge devices is bottlenecked by the floating-point arithmetic of conventional neural networks. We investigated Differentiable Logic Gate Networks (Diff-Logic) as a hard...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Differentiable, Logic, Gate, Networks, Low-Latency, EEG, Classification, Edge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18149v1) | [下载PDF](https://arxiv.org/pdf/2607.18149v1.pdf)

---

## [26. Totally Positive Matrices and the Highest-Order Coefficients of the Characteristic Polynomial](https://arxiv.org/abs/2607.18148v1)

**作者**：Tiago Closs, Leandro Farina  
**分类**：cs.LG, math.RA  
**发布时间**：2026-07-20

### 📄 论文摘要

We investigate the extent to which totally positive matrices can be distinguished through the highest-order coefficients of their characteristic polynomials. To identify the most informative coefficients, we also employed neural-network classifiers together with feature-attribution methods. Using datasets built from several structured totally positive families, including products of positive bidiagonal matrices, Vandermonde matrices, and Cauchy matrices, we find that the coefficients (a_{n-1}, a_{n-2}, a_{n-3}) already contain strong discriminatory information for separating totally positive from non-totally positive matrices in dimensions 5, 10, and 30. The resulting separation is markedly nonlinear and admits a natural geometric description in the corresponding three-dimensional coefficient space by means of Mahalanobis ellipsoids. These ellipsoids enclose the totally positive samples while excluding most non-totally positive ones. Moreover, different structured totally positive families exhibit distinct ellipsoidal signatures, and the separation between these signatures increases with the dimension. These observations lead us to formulate a conjecture on the geometric separation of structured totally positive families in the space determined by the three highest-order characteristic coefficients.

### 🤖 AI 总结

**一句话总结**：We investigate the extent to which totally positive matrices can be distinguished through the highest-order coefficients of their characteristic polynomials. To identify the most informative coefficie...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Totally, Positive, Matrices, Highest-Order, Coefficients, Characteristic, Polynomial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18148v1) | [下载PDF](https://arxiv.org/pdf/2607.18148v1.pdf)

---

## [27. Manifold-Constrained Hyper-Connections for Parameter-Efficient Finetuning](https://arxiv.org/abs/2607.18130v1)

**作者**：Valentijn Oldenburg, Floris de Kam, Bente Zuijdam 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-20

### 📄 论文摘要

Most parameter-efficient finetuning (PEFT) methods adapt weights or activations, thus leaving one of the key Transformer components unchanged: residual connections. This paper investigates Manifold-Constrained Hyper-Connections (mHC), a generalisation of residual connections, as a novel PEFT approach, wrapping frozen OLMo-2 backbones with learned residual routing modules. We find that mHC can finetune frozen Transformers, but that its role differs fundamentally from the original pre-training setting: in finetuning, fixing the residual mixing matrix to identity often improves performance. As a standalone PEFT method, mHC does not consistently outperform LoRA. However, at matched trainable parameter budgets, mHC+LoRA combinations improve language-modelling loss and show task-dependent benchmark gains at both 1B and 7B scale. Overall, our results identify residual routing as a distinct and promising novel PEFT axis.

### 🤖 AI 总结

**一句话总结**：Most parameter-efficient finetuning (PEFT) methods adapt weights or activations, thus leaving one of the key Transformer components unchanged: residual connections. This paper investigates Manifold-Co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Manifold-Constrained, Hyper-Connections, Parameter-Efficient, Finetuning, Most, PEFT, methods, adapt

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18130v1) | [下载PDF](https://arxiv.org/pdf/2607.18130v1.pdf)

---

## [28. LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks](https://arxiv.org/abs/2607.18110v1)

**作者**：Tianzhu Ye, Li Dong, Guanheng Chen 等 7 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-07-20

### 📄 论文摘要

Reinforcement learning (RL) on open-ended tasks compresses an LLM's rubric-based evaluation into a scalar reward, discarding rich textual feedback and conflating responses with distinct quality profiles. We propose Experiential Learning (EL), which repurposes the feedback model from an LLM-as-a-Judge into an LLM-as-a-Coach. The coach distills its assessment of each on-policy response into transferable experiential knowledge, which conditions a teacher model and is internalized by the policy through on-policy context distillation. Compared with scalar rewards, this higher-bandwidth feedback channel provides dense supervision and preserves fine-grained preferences among high-quality responses. Across two policy families, with feedback from the policy itself or a proprietary model, EL consistently outperforms rubric-based RL on held-out and unseen open-ended tasks. Notably, EL generalizes better beyond the training distribution, and mitigates reward hacking. These findings establish experiential knowledge as a richer and more generalizable learning signal for post-training on non-verifiable tasks.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning (RL) on open-ended tasks compresses an LLM's rubric-based evaluation into a scalar reward, discarding rich textual feedback and conflating responses with distinct quality profil...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, LLM-as-a-Coach, Experiential, Learning, Non-Verifiable, Tasks, Reinforcement, open-ended

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18110v1) | [下载PDF](https://arxiv.org/pdf/2607.18110v1.pdf)

---

## [29. Empowering On-Device Model Adaptation with an Edge AI Inference Accelerator](https://arxiv.org/abs/2607.18101v1)

**作者**：Mateusz Piechocki, Alessandro Capotondi, Marek Kraft  
**分类**：cs.LG, cs.AR, cs.CV  
**发布时间**：2026-07-20

### 📄 论文摘要

On-device model adaptation is essential to enable lifelong personalization on resource-constrained hardware, but compute, power, and memory limitations of such devices make end-to-end backpropagation impractical for modern deep neural networks. This work proposes a heterogeneous adaptation pipeline that repurposes a commercial edge AI inference accelerator, Hailo-8L, for frozen-backbone feature extraction during on-device training. The computational graph is partitioned so that the pre-trained backbone is quantized to INT8 and run on the accelerator, while only a lightweight FP32 classification head is fine-tuned on the host CPU, enabling frequent, energy-efficient in-field updates with most weights remaining fixed. Across multiple architectures and datasets, this pipeline achieves up to 15.4x faster wall-clock training time compared to a Raspberry Pi 5 CPU baseline, offers competitive throughput in favorable settings, and consistently reduces energy per sample. Post-training quantization restoration is shown to be crucial for preserving the quality of accelerator-generated features and mitigating accuracy loss in quantization-sensitive architectures. Overall, the results demonstrate a practical approach to efficient on-device adaptation using inference-oriented edge accelerators. The implementation is available at https://github.com/MatPiech/accelerator-training.

### 🤖 AI 总结

**一句话总结**：On-device model adaptation is essential to enable lifelong personalization on resource-constrained hardware, but compute, power, and memory limitations of such devices make end-to-end backpropagation ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Empowering, On-Device, Model, Adaptation, Edge, Inference, Accelerator

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18101v1) | [下载PDF](https://arxiv.org/pdf/2607.18101v1.pdf)

---

## [30. The Label Complexity of Class-Conditional Coverage under Distribution Shift](https://arxiv.org/abs/2607.18088v1)

**作者**：Weijia Han, Lisha Qu  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-07-20

### 📄 论文摘要

Standard evaluation of many recognition systems contains distribution shift by construction, since benchmarks place disjoint conditions in the training and test splits. Under such a shift, split conformal prediction keeps marginal coverage near the nominal level while per-class coverage fails silently: on a real cross-subject skeleton benchmark, marginal coverage stays near ninety percent, the worst action class is covered about seventy percent of the time, and ten of the sixty classes fall below eighty percent coverage.   We characterize the cost of restoring per-class validity. First, an impossibility: once the shift acts jointly on the covariates and the labels, the target class-conditional score law is unidentified from source labels and an unlabeled target sample, so no label-free method attains per-class coverage that is at once valid and efficient. Second, we make the cost precise: per-class validity alone needs only a handful of target labels per class, while the label count necessary and sufficient for validity together with per-class efficiency grows as the inverse square of the efficiency tolerance and the logarithm of the number of classes, with matching upper and lower bounds. Third, within the evaluated prediction-powered inference family, even the most favorable use of the classifier's own pseudo-labels on an unbounded unlabeled target pool improves efficiency by at most a small constant factor where coverage collapses.   Skeleton action recognition is our real-data case study. A per-class calibration using source labels alone recovers a substantial share of the per-class gap while the shift preserves marginal coverage, and stops helping exactly when marginal coverage itself breaks. Three real shifts of increasing severity trace this boundary, and the same collapse and recovery appears on a natural-image corruption benchmark, beyond any single modality.

### 🤖 AI 总结

**一句话总结**：Standard evaluation of many recognition systems contains distribution shift by construction, since benchmarks place disjoint conditions in the training and test splits. Under such a shift, split confo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Label, Complexity, Class-Conditional, Coverage, under, Distribution, Shift

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.18088v1) | [下载PDF](https://arxiv.org/pdf/2607.18088v1.pdf)

---

