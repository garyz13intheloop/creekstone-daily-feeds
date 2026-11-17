# arXiv AI 论文日报 | 2026-11-17

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (10 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. Right Reason, Wrong Advice: Evaluating Recourse in LLM Explanations of Denied Requests](https://arxiv.org/abs/2611.21545v1)

**作者**：Arunkumar V  
**分类**：cs.AI, cs.CL, cs.CY  
**发布时间**：2026-11-16

### 📄 论文摘要

Language models increasingly write the explanations people receive when a rule system denies their request. If several rules deny the request independently, an explanation can name a true reason and still leave the person denied after they fix it. We call the missing property recourse validity: changing what the explanation cites, without changing what was asked for, can flip the decision. We compute it exactly, and a hitting-set argument predicts from the policy alone when a correct reason fails. In six of seven rule systems ported from access control and US benefit eligibility, a single correct reason almost never gives recourse when several reasons apply. Across 20 LLMs, checks of whether the cited reasons are correct, computed or asked of an LLM judge, are close to chance at spotting this failure, as the argument predicts. A strong judge asked whether acting on the explanation would work does spot it. Stronger and reasoning models do better but still fail on many denials with four or more independent reasons. Asking for every rule helps every open model with room to improve. Explanations of eligibility decisions should be built from the decision function and judged by whether acting on them works.

### 🤖 AI 总结

**一句话总结**：Language models increasingly write the explanations people receive when a rule system denies their request. If several rules deny the request independently, an explanation can name a true reason and s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Right, Reason, Wrong, Advice, Evaluating, Recourse, Explanations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21545v1) | [下载PDF](https://arxiv.org/pdf/2611.21545v1.pdf)

---

## [2. Procedure without Judgment: What Small Language Models Learn under an Exact Verifier](https://arxiv.org/abs/2611.21529v1)

**作者**：Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R. 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-11-16

### 📄 论文摘要

When an authorization policy blocks an agent's tool call, the audit log should name the facts that forced the decision and nothing more. For an executable policy over an enumerable context space this minimal sufficient reason can be computed exactly, so an explanation is scored against ground truth rather than a proxy for it. We use that exactness to ask what a model can learn from a verifier that has no error in it. The explainer sees one request and one decision, never the policy, and has thirty turns in which it may call the policy on altered requests and ask whether a candidate set of facts is sufficient. Frontier models find the exact reason about half the time with the tools alone, and one sentence telling them to shrink the answer lifts Haiku 4.5 from 58% to 75%. A 4B model fine-tuned on 2000 traces of the deletion algorithm reaches 92% on the policy it was trained on. Teacher kind is what moves this: at matched data size the algorithm-taught student leads the frontier-taught one in all three training seeds, and the two arms never overlap. What the student learns is a fixed schedule of sufficiency checks, and the schedule does not travel. On three public policies it never saw, its answers stay sufficient (94%) and stop being minimal (48%), while Haiku under the same sentence is exact on all 47 episodes. Reinforcement learning from the exact reward leaves held-out accuracy where it was and inverts the strategy, from probing the policy to spending the entire budget on sufficiency checks. The oracle made the effect of training legible, but it did not make training better.

### 🤖 AI 总结

**一句话总结**：When an authorization policy blocks an agent's tool call, the audit log should name the facts that forced the decision and nothing more. For an executable policy over an enumerable context space this ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Procedure, without, Judgment, What, Small, Language, Models, Learn

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21529v1) | [下载PDF](https://arxiv.org/pdf/2611.21529v1.pdf)

---

## [3. Safe Resemblance, Silent Propagation: Limits of Text-Similarity Guardrails for AI Agent Safety](https://arxiv.org/abs/2611.21520v1)

**作者**：Charles Xiao  
**分类**：cs.AI  
**发布时间**：2026-11-16

### 📄 论文摘要

When AI agents relay information to one another, an output can preserve an injected instruction's effect on downstream agents even after its wording changes, yet legitimate quotation and template reuse can produce high textual overlap with the source, so text-similarity guardrails that attempt to flag the former risk conflating these two cases. We test this distinction using DonkeyRail, a public classifier combining BLEU, ROUGE-L, and METEOR features, deployed in a controlled three-agent email relay, defining a behavioral measure in which an output counts as functional (the injected procedure induces fresh computations in two subsequent agents) independent of the detector's score, alongside legitimate controls that explicitly authorize quotation and reuse. At its default threshold the classifier misses 8 of 19 functional outputs while flagging 70 of 192 legitimate replies, with every completed quotation and template-reuse reply triggering a false alert; calibrating for low false positives on one template set does not transfer, as the recalibrated threshold detects only one functional output and still produces 15 false alerts on new templates. We also identify an operating-point error in all 21 published classifier configurations, where ROC interpolation replaces direct threshold application, and show formally that high AUC against a surface-level text criterion provides no distribution-free guarantee of high AUC against the behavioral target, while the existing evaluation labels lack the joint observations needed to estimate the gap. An authorization analysis further shows that identical visible transcripts can require different safety decisions depending on the governing policy, a distinction no observation-only classifier can resolve. These results argue for behavioral and policy-grounded evaluation over text-similarity guardrails.

### 🤖 AI 总结

**一句话总结**：When AI agents relay information to one another, an output can preserve an injected instruction's effect on downstream agents even after its wording changes, yet legitimate quotation and template reus...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Safe, Resemblance, Silent, Propagation, Limits, Text-Similarity, Guardrails

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21520v1) | [下载PDF](https://arxiv.org/pdf/2611.21520v1.pdf)

---

## [4. Generative AI and the Crisis of Higher Education Assessments: Examining 'AI-Proofing' Strategies for College-Level Assessments](https://arxiv.org/abs/2611.21476v1)

**作者**：Bonam Mingole, Davis Yadav, Hui Min Lee 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-16

### 📄 论文摘要

Higher education is confronting an academic-integrity challenge unlike any in its history. Students can now outsource homework, take-home assignments, and online examinations to large language models (LLMs) that complete them in seconds. Existing research on evaluating LLM performance on academic assessments has focused largely on standardized examinations, or on questions from college-level courses drawn from a single discipline. Far less is known about how LLMs perform on college-level assessment questions spanning multiple disciplines, that instructors have purposely designed to be AI-resistant, and about which features of such questions, if any, meaningfully constrain LLM performance. We address this gap by collecting 75 questions from authentic college coursework assessments, spanning 17 disciplines, which were contributed by 37 faculty members from ten U.S. universities and one U.K. university. Of these, 61 questions were intentionally designed by faculty members to be 'LLM-proof', while the remaining 14 questions were sourced from online courses. We then (i) evaluate three state-of-the-art LLMs' ability to correctly answer these questions with and without supplementary course materials; (ii) identify five strategies, through thematic analysis, that faculty used to make their questions harder for LLMs to solve; and (iii) test whether these strategies impact LLMs' ability to answer the questions accurately. Our experimental results show that the best-performing model scored approximately 83% without supplementary course materials and 85% with them, and we observed noteworthy differences across models, answer formats, and instructor tweaking strategies. We discuss implications for assessment design, academic-integrity policy, and the broader ethics of deploying LLMs in educational settings.

### 🤖 AI 总结

**一句话总结**：Higher education is confronting an academic-integrity challenge unlike any in its history. Students can now outsource homework, take-home assignments, and online examinations to large language models ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Generative, Crisis, Higher, Education, Assessments, Examining, 'AI-Proofing'

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21476v1) | [下载PDF](https://arxiv.org/pdf/2611.21476v1.pdf)

---

## [5. Subprocess-Constrained Markov Decision Processes](https://arxiv.org/abs/2611.21471v1)

**作者**：Jiarui Gan, Debmalya Mandal  
**分类**：cs.AI  
**发布时间**：2026-11-16

### 📄 论文摘要

Constrained Markov decision processes (CMDPs) typically bound expected cumulative cost from an initial state. Such a guarantee can be insufficient when a policy must remain feasible after every history it may encounter. We introduce \emph{subprocess-constrained MDPs} (S-CMDPs), which require the expected discounted cost of each continuation, conditional on any reachable history, to satisfy a bound determined by the current state. This stronger requirement changes the structure and complexity of the problem: we show that stationary policies can be strictly suboptimal, and finding even an approximately optimal stationary policy is NP-hard. We adapt a recently introduced value-set iteration framework to show that history-dependent policies surprisingly overcome both obstacles. Our polynomial-time algorithm represents such a policy implicitly: its expected reward is within $ε$ of the optimal feasible value, it violates each subprocess cost bound by at most $δ$, and its action distribution can be computed in polynomial time for any given history.

### 🤖 AI 总结

**一句话总结**：Constrained Markov decision processes (CMDPs) typically bound expected cumulative cost from an initial state. Such a guarantee can be insufficient when a policy must remain feasible after every histor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Subprocess-Constrained, Markov, Decision, Processes, Constrained, CMDPs, typically, bound

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21471v1) | [下载PDF](https://arxiv.org/pdf/2611.21471v1.pdf)

---

## cs.CL

## [6. Beyond Job Titles: Interpreting Early-Career Job Advertisements with Sparse Autoencoders and Semantic Clustering](https://arxiv.org/abs/2611.21586v1)

**作者**：Yisong Cao, Leah Kim, Brian Wright 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-11-16

### 📄 论文摘要

Job titles and job descriptions alone provide limited insight into how technical roles differ in a changing job market. To assess how such roles differ in their work and industry applications, we design and compare two methods based on deep learning and transformer representations using 36,081 early-career job postings collected from LinkedIn in the United States between December 2025 and October 2026.   We first apply PERC, short for Preprocessing (P), Embedding (E), Dimensionality Reduction (R) and Clustering (C). We employ GPT-6 Luna to classify job description passages into Team context, Role task and Qualifications. We then create combinations of these sections and examine whether embedding and clustering the segmented passages produce meaningful semantic clusters about different job roles. We use Maximum Mean Discrepancy (MMD) to rank observed differences between embedding distributions and employ a pretrained sparse autoencoder (SAE) to extract features from layer-19 representations of Llama-3.1-8B-Instruct. Lastly, we employ GPT-6 Luna to come up with hypotheses about job roles' feature patterns, and GPT-6.1 Terra to investigate whether those patterns exist in held-out job descriptions from unseen companies.   Some example findings include Data Scientist advertisements placing more emphasis on machine learning model development, Data Analyst advertisements on reporting business performance, and Machine Learning Engineer advertisements on applying developed models in real-world settings. We also observe differences in the applications described by Data Analyst and Business Analyst advertisements across selected months, although our dataset's scale and uneven coverage limit their interpretation. Overall, we present a realistic application of SAEs and PERC to unstructured textual data and examine how automated insight extraction could support manual analysis of job descriptions.

### 🤖 AI 总结

**一句话总结**：Job titles and job descriptions alone provide limited insight into how technical roles differ in a changing job market. To assess how such roles differ in their work and industry applications, we desi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Job, Titles, Interpreting, Early-Career, Advertisements, Sparse, Autoencoders

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21586v1) | [下载PDF](https://arxiv.org/pdf/2611.21586v1.pdf)

---

## [7. Evaluating Cultural Reasoning and Robustness in LLMs for Spanish Political Discourse](https://arxiv.org/abs/2611.21535v1)

**作者**：Jorge Valverde-Rebaza, Nathan Garcia-Larios, Karime Ruvalcaba-Perez 等 6 位作者  
**分类**：cs.CL, cs.CY, cs.SI  
**发布时间**：2026-11-16

### 📄 论文摘要

Large language models (LLMs) are increasingly used to interpret, generate, and mediate public-facing language, which makes their reliability especially consequential in politically sensitive settings. Although sentiment analysis is a common task in this area, affective meaning in social media discourse is often conveyed through culturally situated and pragmatically indirect cues that are not well captured by label-centric evaluation alone. In this paper, we evaluate the robustness of LLMs for sentiment analysis of Spanish political discourse from social media, with emphasis on culturally situated affective interpretation. We introduce a diagnostic protocol that combines three independent human annotation views into Gold and Ambiguous subsets, and extends the corpus with a Synthetic subset built from sentiment-flipped counterfactuals selected through model-conditioned perplexity and LLM-as-a-judge criteria. Using this framework, we compare proprietary and open-weight models under zero-shot and few-shot prompting, focusing on predictive robustness across human agreement conditions and counterfactual shift. Our results show that annotation ambiguity and counterfactual perturbation reveal failure modes that conventional evaluation on the original corpus tends to obscure. GPT-4.1-mini remains the most stable among the evaluated models, whereas the two smaller open-weight models degrade more markedly under synthetic perturbations, and few-shot prompting provides only limited gains. Overall, the paper contributes a reproducible protocol for robustness-oriented evaluation in political sentiment analysis, an empirical characterization of model behavior under ambiguity and sentiment-flipped counterfactuals, and a publicly available Spanish social media dataset with three-way human sentiment annotations.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly used to interpret, generate, and mediate public-facing language, which makes their reliability especially consequential in politically sensitive settings....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Evaluating, Cultural, Reasoning, Robustness, Spanish, Political, Discourse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21535v1) | [下载PDF](https://arxiv.org/pdf/2611.21535v1.pdf)

---

## [8. Embedding Cosine Measures Text Length Before It Measures Homogenization](https://arxiv.org/abs/2611.21519v1)

**作者**：Fengming Liu  
**分类**：cs.CL, cs.CY, cs.SI  
**发布时间**：2026-11-16

### 📄 论文摘要

Mean pairwise cosine similarity between transformer embeddings is a standard measure of whether online discourse is converging under generative AI. When the embeddings are mean-pooled outputs of an encoder never trained for sentence similarity, this measure mostly tracks text length. In 6.06 million Reddit comments, an uncentered DeBERTa-v3 measure had suggested that only conservative discourse broke toward homogeneity after late 2022. Truncating the same comments from 10 to 150 words raises their mean cosine by eight times the reported break. A placebo that swaps every comment for a random one of equal length reproduces 81% of the asymmetry, and a fixed-content simulation reproduces 78%. The leading principal direction carries 99.9% of raw DeBERTa homogeneity, and once length is handled the asymmetry disappears under every encoder. On 575,000 Stack Exchange answers the measure reports a post-ChatGPT homogenization of technical sites that the placebo fully reproduces, although answers grew longer. A census of 31 studies locates the risk where anisotropic encoders meet time-series or length-unequal designs. A reverse control on a well-known experiment shows that centering with renormalization can reverse a genuine effect. I propose a low-cost diagnostic protocol. Corrected measures show that the two political camps converged between 2019 and 2022 and stopped converging before ChatGPT. Cross-camp replies engage their targets more closely than same-camp replies.

### 🤖 AI 总结

**一句话总结**：Mean pairwise cosine similarity between transformer embeddings is a standard measure of whether online discourse is converging under generative AI. When the embeddings are mean-pooled outputs of an en...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：It, Embedding, Cosine, Measures, Text, Length, Before, Homogenization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21519v1) | [下载PDF](https://arxiv.org/pdf/2611.21519v1.pdf)

---

## [9. Jetriever: Shifting Agent Memory Retrieval from Similarity to Utility](https://arxiv.org/abs/2611.21478v1)

**作者**：Ruizhe Li, Licheng Zhang, Mingxuan Du 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-11-16

### 📄 论文摘要

A useful memory need not resemble the question it helps answer. Jetriever ranks each stored memory by Jev's decision score for its usefulness to the current question, replacing similarity search with full-pool utility scoring. On InMind's 125 indirect-query tasks, it places the gold exchange first in 84.8% of cases; matched BM25 and MiniLM controls reach 1.6% and 0.0% when indexing user turns. A 20-question comparison separates finding evidence from ranking it: Jev and Qwen3.5 9B each find 90% of gold exchanges by rank 50, while Laya finds 30%; at rank one, Jev reaches 85% and Qwen3.5 9B 40%. On a dimension-proportional random sample of 60 MemoryAgentBench questions, Jetriever's four-dimension score is 55.4%, against 44.3% for ReFind on the same questions. Jev retrieval costs USD 0.00834 per InMind question and USD 0.03103 per MAB question on average. These results show the value of world knowledge, scores that rank decisive memories first, and affordable full-pool scoring.

### 🤖 AI 总结

**一句话总结**：A useful memory need not resemble the question it helps answer. Jetriever ranks each stored memory by Jev's decision score for its usefulness to the current question, replacing similarity search with ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Jetriever, Shifting, Memory, Retrieval, Similarity, Utility, useful

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21478v1) | [下载PDF](https://arxiv.org/pdf/2611.21478v1.pdf)

---

## [10. A Scalable Multi Task Learning Framework for Modeling Demographic Disagreements in Annotation Tasks](https://arxiv.org/abs/2611.21458v1)

**作者**：Soumyajit Gupta, Maria De-Arteaga, Matthew Lease  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-11-16

### 📄 论文摘要

Annotators from different demographic backgrounds often disagree in systematic ways due to varying lived experiences, cultural contexts, and their relationship to the content. When such disagreement occurs, one group's perspective may sometimes warrant prioritization because they hold an epistemically advantaged standpoint or bear greater stake in the outcome. For example, when assessing toxicity of posts on social media, it may be important to prioritize a targeted group's viewpoint. We propose a Stakeholder-Aware Joint Multi-Task Learning (SAJ-MTL) framework to jointly model demographic disagreement both across- and within- annotator groups. The model uses conditional gradient routing to handle sparsity induced by group-conditional labeling, and parameterization supports customized weighting of groups in different task settings. SAJ-MTL improves group-level performance in toxicity detection through better context-aware understanding of demographic-sensitive content. Only annotator group-membership information is required, which is more practical than existing methods requiring more privacy-invasive individual-level annotator details. Our scalable architecture is also computationally efficient to support large-scale deployment.

### 🤖 AI 总结

**一句话总结**：Annotators from different demographic backgrounds often disagree in systematic ways due to varying lived experiences, cultural contexts, and their relationship to the content. When such disagreement o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Scalable, Multi, Task, Learning, Framework, Modeling, Demographic, Disagreements

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21458v1) | [下载PDF](https://arxiv.org/pdf/2611.21458v1.pdf)

---

## cs.CV

## [11. ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization](https://arxiv.org/abs/2611.21605v1)

**作者**：Huawei Lin, Jinting Liu, Tongyan Wang 等 12 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-16

### 📄 论文摘要

Visual agents answer questions about ultra-high-resolution photos by zooming into the relevant regions. However, existing agents often answer from common sense instead of reading the evidence. Reinforcement learning (RL) on the final answer cannot correct this, because a guess earns the same reward as reading. We propose Cross-Input Relative Policy Optimization (CrossRPO), which trains agents on contrast sets. A contrast set asks one question about several versions of an image that differ only in a small region with the evidence and have different answers, so only reading the evidence solves the whole set. CrossRPO rewards solving the whole set, and we prove that it does not reinforce a set answered from common sense. We build contrast sets for training (ViRA-Train) and evaluation (ViRA-Bench) by editing one small object in images of 21 to 120 megapixels, and we photograph further sets with real changes (ViRA-Bench-Real) to exclude editing traces. We train two Visual Reasoning Agents, ViRA-9B and ViRA-27B, with CrossRPO on only about 3,500 items of ViRA-Train each. CrossRPO achieves 63.3% set accuracy on ViRA-Bench at the maximum resolution, against 59.3% for GRPO. ViRA-9B is the most accurate open model of its size on all benchmarks, and ViRA-27B outperforms Claude Haiku 5.5 and GPT-6-Luna, both at their highest thinking level, on most benchmarks.

### 🤖 AI 总结

**一句话总结**：Visual agents answer questions about ultra-high-resolution photos by zooming into the relevant regions. However, existing agents often answer from common sense instead of reading the evidence. Reinfor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, ViRA, Toward, Ultra-High-Resolution, Visual, via, Cross-Input, Relative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21605v1) | [下载PDF](https://arxiv.org/pdf/2611.21605v1.pdf)

---

## [12. FaceJev: Direct Visual Decisions for Face Forgery Detection](https://arxiv.org/abs/2611.21604v1)

**作者**：Siran Peng, Tianshuo Zhang, Yibo Xue 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-16

### 📄 论文摘要

Face forgery detection methods often perform well on seen manipulations but generalize poorly to unseen ones. Multimodal Large Language Models (MLLMs) can recognize facial parts and assess their visual plausibility. Existing MLLM-based methods typically express these judgments through textual explanations, but seldom treat individual part decisions as explicit learning targets. We present FaceJev, an MLLM-based method for face forgery detection through direct visual decisions. Following the Jev formulation, FaceJev answers eight independent questions about facial parts using a shared image encoding and reads anomaly probabilities from the native answer logits. A face is classified as forged if any part is predicted to be abnormal, directly linking the detection result to the part decisions. We construct PartForensics, a dataset of approximately 160k images with binary anomaly targets for the eight facial parts, to supervise these decisions. We further propose FS-GRPO, which optimizes each part decision through an exact reward comparison with its alternative, using both detection and part rewards. FaceJev outperforms the strongest baseline by 7.25 percentage points on unseen manipulations. Extensive ablation studies validate our design choices and the effectiveness of the main components.

### 🤖 AI 总结

**一句话总结**：Face forgery detection methods often perform well on seen manipulations but generalize poorly to unseen ones. Multimodal Large Language Models (MLLMs) can recognize facial parts and assess their visua...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FaceJev, Direct, Visual, Decisions, Face, Forgery, Detection, methods

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21604v1) | [下载PDF](https://arxiv.org/pdf/2611.21604v1.pdf)

---

## [13. When Do Histology Foundation Models Need Geometric Test-Time Augmentation?](https://arxiv.org/abs/2611.21565v1)

**作者**：Lars Chen, Valentino F. Foit, Dorry Segev 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-16

### 📄 论文摘要

Test-time augmentation (TTA) aggregates model predictions across multiple transformed views of an input during inference. Because histology images lack a canonical orientation, $D_4$ TTA---pooling across the 8 rotations and reflections of a square---is a standard default in computational pathology. However, the rise of self-supervised histology foundation models (FMs) with inherent rotational invariance calls its continued utility into question. We benchmark 9 histology FMs and 6 general-purpose models across four patch-level and two whole-slide image (WSI) datasets. We find that $D_4$ TTA remains a reliable post hoc improvement, but benefits diminish from $+1.98$ percentage points (pp) for general-purpose backbones to $+0.50$ pp for histology FMs on TCGA-UT, and shrink further for the largest models. To eliminate computational overhead, our experiments demonstrate that entropy routing---applying TTA selectively to uncertain predictions---recovers most of the gain while augmenting only ${\sim}13\%$ of samples. Finally, we show that patch-level TTA improvements do not transfer to slide-level multiple instance learning (MIL). Code: https://github.com/lars-chen/histology-tta

### 🤖 AI 总结

**一句话总结**：Test-time augmentation (TTA) aggregates model predictions across multiple transformed views of an input during inference. Because histology images lack a canonical orientation, $D_4$ TTA---pooling acr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, When, Histology, Foundation, Models, Need, Geometric, Test-Time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21565v1) | [下载PDF](https://arxiv.org/pdf/2611.21565v1.pdf)

---

## [14. Wildfire-SSR: Geolocation-Aware Multimodal Fusion for Structure-Level Wildfire Risk Assessment](https://arxiv.org/abs/2611.21563v1)

**作者**：Yu-Hsuan Ho, Yiming Xiao, Hao-En Lai 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-16

### 📄 论文摘要

Structure-level wildfire vulnerability assessment is critical for reducing losses in wildland-urban interface communities, yet existing methods often fail to combine parcel-scale ignition pathways with community-scale geographic coverage. This study introduces Wildfire-SSR (Satellite and Street-view for wildfire Risk), a geolocation-aware multimodal framework that integrates macro-scale satellite context with micro-scale street-view evidence. A Vision-Language Model extracts wildfire-relevant building and site attributes from pre-event street-view panoramas and converts them into structured semantic text. These features are spatially aligned with satellite imagery through a decoupled cross-attention fusion decoder, while a frozen satellite-pretrained DINOv3 encoder captures overhead visual context. Alternative geolocation embedding strategies are evaluated to anchor text-derived features within each satellite patch. The framework is tested on approximately 37,000 structures affected by the 2025 Eaton and Palisades fires in Los Angeles, using wildfire risk labels derived from relative post-event damage patterns to better represent inherent structural vulnerability. Rotary Positional Embedding provides the strongest spatial grounding, achieving a building localization F1 score of 0.6735 and a harmonic mean F1 score of 0.2476 for five-class pixel-level risk classification, outperforming unimodal baselines and an unanchored multimodal configuration. The model also shows a conservative bias in higher-risk classes, reducing severe-risk underestimation, and completes end-to-end assessment of the study area in 37 minutes on a single GPU. Wildfire-SSR reframes cross-view fusion as localized semantic alignment and provides a scalable tool for mitigation prioritization, resilience planning, and insurance-oriented wildfire risk assessment.

### 🤖 AI 总结

**一句话总结**：Structure-level wildfire vulnerability assessment is critical for reducing losses in wildland-urban interface communities, yet existing methods often fail to combine parcel-scale ignition pathways wit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Wildfire-SSR, Geolocation-Aware, Multimodal, Fusion, Structure-Level, Wildfire, Risk, Assessment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21563v1) | [下载PDF](https://arxiv.org/pdf/2611.21563v1.pdf)

---

## [15. Reference Forcing: Long Video Generation with Region-Guided Drift Correction](https://arxiv.org/abs/2611.21559v1)

**作者**：Sheng Zhao, Haitian Zheng, Weikai Lin 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-16

### 📄 论文摘要

Long video generation should keep the subject and background consistent while supporting rich, natural motion. However, autoregressive models are often distilled with distribution matching distillation (DMD) over short windows, which does not train them to keep this consistency over long ranges. As a result, the subject and background can drift over time. Methods that manage the key-value (KV) cache retain or retrieve history to reduce drift. Yet this history may itself have drifted. We propose Reference Forcing, which uses the initial frames as an appearance reference. We first build a teacher that uses attention masks to force each region of a new frame to attend to the same region in the initial frames. The teacher finds these regions with off-the-shelf segmentation models. We then distill this behavior into a separate attention path of the student, which needs no external models at inference. We further introduce value correction, which corrects drifted values in the KV cache toward the matching values of drift-free initial frames. Experiments show that Reference Forcing achieves state-of-the-art subject and background consistency among long-video methods on different base models, and its advantage grows with video length. Ablations show both components are needed to gain consistency without losing motion. More visualizations and code are available at https://zhaosheng-thu.github.io/reference-force/

### 🤖 AI 总结

**一句话总结**：Long video generation should keep the subject and background consistent while supporting rich, natural motion. However, autoregressive models are often distilled with distribution matching distillatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Reference, Forcing, Long, Video, Generation, Region-Guided, Drift, Correction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21559v1) | [下载PDF](https://arxiv.org/pdf/2611.21559v1.pdf)

---

## [16. BLIP-Live: Balancing Timeliness & Firing Precision in Proactive Streaming Video Agents](https://arxiv.org/abs/2611.21553v1)

**作者**：Kanchana Ranasinghe, Honglu Zhou, Dominick Reilly 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-16

### 📄 论文摘要

Streaming video understanding is becoming increasingly important for real-world interactive systems. Such systems must be proactive for natural and useful human interaction: they should respond as soon as sufficient evidence becomes available while avoiding premature, redundant, or incorrect responses. We present BLIP-Live, a framework unifying data, metrics, harness, and training around a shared formulation of proactivity as effective causal response decisions balancing the two competing objectives of responding vs silence. First, we construct BLIP-Live-780K dataset containing human annotations of proactive response content and timing, which defines this desired behavior. We then propose PAUC-F, a metric to effectively measure our desired proactive behavior. PAUC-F combines existing response timeliness metrics with firing precision to reward early useful responses without rewarding excessive firing. With our desired behavior defined and measurable, we finally investigate model-agnostic inference harnesses that draw out proactive streaming capabilities of offline vision language models (VLMs), together with training pipelines that learn to further improve their proactive responsiveness. Across both settings, we find that combinations of sliding visual windows, online interaction memory, and structured response outputs consistently yield strongest proactive performance. Our experiments result in two models, with our BLIP-Live-Qwen model achieving state-of-the-art performance across four proactive streaming benchmarks, with gains up to 44% over baselines and outperforming multiple closed API models. Our code and data will be released publicly.

### 🤖 AI 总结

**一句话总结**：Streaming video understanding is becoming increasingly important for real-world interactive systems. Such systems must be proactive for natural and useful human interaction: they should respond as soo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BLIP-Live, Balancing, Timeliness, Firing, Precision, Proactive, Streaming, Video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21553v1) | [下载PDF](https://arxiv.org/pdf/2611.21553v1.pdf)

---

## [17. DuoFlow: Towards Synchronized Speech and Motion Generation with Fine-Grained Control](https://arxiv.org/abs/2611.21530v1)

**作者**：Jun Dong, Ronghui Li, Zhongyuan Hu 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-16

### 📄 论文摘要

An embodied speaker's expressiveness depends not only on what is said, but also on how the voice sounds and how the body moves. However, existing joint speech-motion generation models are largely driven implicitly by transcript semantics or intermediate speech representations, offering little explicit control over motion hierarchy, body parts, or vocal style. To bridge this gap, we construct MotionSpeech, a structured benchmark for controllable joint speech-motion generation that includes transcripts, voice-style descriptions, and motion conditions at two hierarchical levels. Building on this benchmark, we propose DuoFlow, a dual-stream latent flow transformer that jointly denoises speech and motion under a shared noise level and a unified second-based temporal coordinate. Modality-specific residual connectors inject structured conditions into the corresponding streams, layer-wise bidirectional cross-modal attention coordinates their generation, and a monotonic phoneme pathway combines normalized progress anchors with CTC supervision to strengthen speech temporal modeling. DuoFlow provides a unified interface for fine-grained motion and vocal-style control and demonstrates the ability to synthesize high-quality, synchronized, and instruction-consistent speech-motion sequences.

### 🤖 AI 总结

**一句话总结**：An embodied speaker's expressiveness depends not only on what is said, but also on how the voice sounds and how the body moves. However, existing joint speech-motion generation models are largely driv...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DuoFlow, Towards, Synchronized, Speech, Motion, Generation, Fine-Grained, Control

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21530v1) | [下载PDF](https://arxiv.org/pdf/2611.21530v1.pdf)

---

## [18. LynnReal-Hand: Unlocking World Interaction with Hand Control](https://arxiv.org/abs/2611.21479v1)

**作者**：Shaohao Rui, Chaoyang Zhang, Xiaofeng Mao 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-16

### 📄 论文摘要

Interactive video world models enable exploration through text and camera controls, yet direct object interaction requires finer control. Hands provide a natural interface, but translating continuous hand movements into coherent visual responses remains challenging because of complex hand-object dynamics and demanding real-time computation. To address these challenges, we introduce LynnReal-Hand, a hand-controlled video world model that unifies precise interaction modeling with efficient streaming generation. We curate 100K interaction clips spanning diverse real and synthetic environments and develop hand-aware supervision to improve fine-grained hand motions and object interactions. Building on this foundation, we learn a causal flow map for few-step generation and introduce region-aware score distillation that combines complementary video and image priors to refine interaction dynamics and visual appearance. To further reduce inference latency, we propose Ultra-Fast-VAE, a compact video decoder that preserves high reconstruction fidelity with substantially lower computational cost. Extensive evaluations on HandBench demonstrate superior hand-following accuracy and visual quality compared with existing approaches. Our full-sequence model achieves an FVD of 181.67 and a MANO Dice score of 93.02, while the three-step causal model maintains a MANO Dice score of 92.49. For real-time interaction, 540p streaming on a single H200 reaches 18.03 FPS with 741ms latency and an optimized peak GPU memory footprint of only 34.89GB. We will release the datasets, model weights, and the full training and inference code to support research on hand-controlled video world models.

### 🤖 AI 总结

**一句话总结**：Interactive video world models enable exploration through text and camera controls, yet direct object interaction requires finer control. Hands provide a natural interface, but translating continuous ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LynnReal-Hand, Unlocking, World, Interaction, Hand, Control, Interactive, video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21479v1) | [下载PDF](https://arxiv.org/pdf/2611.21479v1.pdf)

---

## [19. Event-Triggered Visual Perception for Real-Time Harvest Outcome Estimation in Mechanical Blueberry Harvesting](https://arxiv.org/abs/2611.21472v1)

**作者**：Nicolas Miroslav Husár, Jelle Driessen, Petra Bosilj 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-16

### 📄 论文摘要

Mechanical blueberry harvesting requires a balance between removing ripe fruit and avoiding premature removal of unripe berries that could remain on the bush for a later harvest. However, operators generally lack real-time information about the maturity composition of the fruit being collected. This study develops an event-triggered machine-vision system that measures the maturity of harvested blueberries directly on the harvester. When a filled crate is moved by the machine, an RGB image is automatically captured and analysed using a three-class detector that identifies ripe, semi-ripe, and unripe berries. The system operates locally on the existing CPU-only industrial computer and therefore requires neither continuous image processing nor dedicated GPU hardware. During field testing, 79 crate images containing 48,634 visible blueberries in manually verified reference annotations were evaluated. The vision system estimated an overall ripe-fruit fraction of 90.22%, compared with 90.97% determined manually. Per-image ripe-fruit estimates showed a mean absolute error of 0.935 percentage points and a Pearson correlation of r=0.967. Maturity estimates remained similar between the two sides of the harvester for which the light conditions varied despite poorer absolute counting performance under direct sunlight. All field events were processed within the available 14 s per-side crate interval. The proposed approach provides a practical means of quantifying one component of harvest selectivity while the machine is operating. Such information could support operator decision-making and, when combined with measurements of fruit recovery and losses, contribute to future feedback-based control of mechanical harvesting.

### 🤖 AI 总结

**一句话总结**：Mechanical blueberry harvesting requires a balance between removing ripe fruit and avoiding premature removal of unripe berries that could remain on the bush for a later harvest. However, operators ge...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Event-Triggered, Visual, Perception, Real-Time, Harvest, Outcome, Estimation, Mechanical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21472v1) | [下载PDF](https://arxiv.org/pdf/2611.21472v1.pdf)

---

## [20. Balanced Twin Weight Factorization for Efficient MLLMs](https://arxiv.org/abs/2611.21459v1)

**作者**：Bryan A. Plummer, Shan Lu, Keval Doshi 等 7 位作者  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-11-16

### 📄 论文摘要

Weight Factorization (WF) methods aim to reduce a model's latency, memory, or both. These typically decompose a pretrained model into two or more factors that approximate the original model weights with fewer parameters and floating point operations (FLOPs). However, translating fewer FLOPs into reduced latency is challenging for WF methods in practice due to overhead introduced by replacing a single large weight matrix with multiple smaller ones. To address this, we propose Balanced Twin Weight Factorization (BTWF), which uses the unique structure of factorized models to simultaneously lower latency and increase learning capacity. Specifically, BTWF operates in the shared basis WF setting, where two or more layers are decomposed into a shared basis matrix and a layer-specific mixing matrix. If these shared layers have the same input (i.e., are twins), then we need only perform this shared forward pass once, reducing inference time. However, twin layers are often of varying sizes, and methods from prior work tend to favor the larger layer. In contrast, our approach boosts performance by combining Factor Component Balancing (FCB), which ensures every shared member is well represented in the selected factors, with Block Contribution Balancing (BCB), which considers downstream model effects. Further, we also show that an overparameterized BTWF, where some layer's factors result in higher FLOPs than the original during training, can boost task performance without additional resources at test time. Experiments on six models over nine benchmarks show BTWF obtains a 2-6% gain over the state-of-the-art without expensive finetuning (1-3.5% gain with it) at comparable computational costs.

### 🤖 AI 总结

**一句话总结**：Weight Factorization (WF) methods aim to reduce a model's latency, memory, or both. These typically decompose a pretrained model into two or more factors that approximate the original model weights wi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：WF, Balanced, Twin, Weight, Factorization, Efficient, MLLMs, methods

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21459v1) | [下载PDF](https://arxiv.org/pdf/2611.21459v1.pdf)

---

## cs.LG

## [21. Quantifying the added value of human forecaster discussions for tropical cyclone intensity prediction](https://arxiv.org/abs/2611.21602v1)

**作者**：Ilia Azizi, Frederick Iat-Hin Tam, Marc-Olivier Boldi 等 5 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-11-16

### 📄 论文摘要

The National Hurricane Center routinely releases Tropical Cyclone Discussions that offer insights into its tropical cyclone forecasts. This study examines the added value of these discussions for intensity forecasting beyond a set of numerical predictors. For 637 Atlantic and eastern North Pacific tropical cyclones from the 2002-2023 hurricane seasons, we analyze the discussion text and its combination with 13 hurricane environmental predictors from SHIPS and ERA5 10-meter wind fields, for forecasting intensity changes at lead times of 24 to 120 hours using three modeling methods. In one approach, an end-to-end deep learning framework for the text shows that the discussions alone offer comparable value for 24-hour intensity forecasts to the SHIPS predictors. Adding discussion information to the SHIPS predictors in an ensemble of five such models reduces the mean absolute error of 24-hour maximum sustained wind forecasts for 2022-2023 cyclones from 9.89 to 8.90 kt, with a confidence interval that excludes zero when whole storms are resampled. The ERA5 wind fields have a minor effect on mean absolute error in wind predictions, and model rankings differ across predicted variables, lead times and model types. We provide prediction intervals for these forecasts, whose coverage falls below the 90% target during rapid intensification. Analysis of the text shows that words related to intensity and intensity change (such as intensify, weaken, eyewall and category) are important for the model predictions. This retrospective study shows the added value of the forecasters' discussions and suggests that multi-modal learning can help understand the predictive contribution of expert human judgment. The reanalysis data differ from real-time analyses, and the discussions are issued at least three hours after the valid time of the other inputs, so these results should not be interpreted operationally.

### 🤖 AI 总结

**一句话总结**：The National Hurricane Center routinely releases Tropical Cyclone Discussions that offer insights into its tropical cyclone forecasts. This study examines the added value of these discussions for inte...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Quantifying, added, value, human, forecaster, discussions, tropical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21602v1) | [下载PDF](https://arxiv.org/pdf/2611.21602v1.pdf)

---

## [22. Mitigating Catastrophic Forgetting with Physics-Indexed Specialist Memory: the Evolutionary Neuroplastic Agent](https://arxiv.org/abs/2611.21598v1)

**作者**：Blas Eugenio Vicco Zarate, Miguel Hernán Vicco  
**分类**：cs.LG, cs.AI, cs.NE  
**发布时间**：2026-11-16

### 📄 论文摘要

Continual reinforcement learning requires adaptation to changing conditions while preserving performance under previously encountered dynamics. It was investigated whether specialists generated by evolutionary search can provide a reusable memory when combined with environment detection and failure-driven search. The Evolutionary Neuroplastic Agent (ENA) evolves small neural networks without gradients, archives selected policies by detected dynamic regime, and retrieves them through Bayesian policy reuse. The architecture was evaluated in non-stationary CartPole and HalfCheetah environments. In the 30-replicate CartPole ablation, the complete architecture achieved a mean success rate of 83.2% across the five test environments. Among variants that learned the harder CartPole environments, the complete architecture showed the most consistent retention. A selection ablation also showed that the retrieval rule affected performance. In the evaluated sequences, ENA adapted more slowly than PPO on CartPole and achieved lower returns than SAC on HalfCheetah. The evidence concerns the complete architecture and does not isolate gradient-free optimization as the cause of retention or establish superiority over other continual-learning methods.

### 🤖 AI 总结

**一句话总结**：Continual reinforcement learning requires adaptation to changing conditions while preserving performance under previously encountered dynamics. It was investigated whether specialists generated by evo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mitigating, Catastrophic, Forgetting, Physics-Indexed, Specialist, Memory, Evolutionary, Neuroplastic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21598v1) | [下载PDF](https://arxiv.org/pdf/2611.21598v1.pdf)

---

## [23. CertiSum: Bitwise-Identical MXFP4 Training Across Platforms and Parallelism Layouts](https://arxiv.org/abs/2611.21584v1)

**作者**：Steve Rhyner, Yubo Gao, Stefan de Lasa 等 5 位作者  
**分类**：cs.LG, cs.DC  
**发布时间**：2026-11-16

### 📄 论文摘要

Training with MXFP4, a 4-bit microscaling format, is non-deterministic: identical inputs can produce different results across parallelism layouts and GPU vendors. These differences complicate debugging and training audits and can cause training and inference engines to disagree. We present CertiSum to make MXFP4 training bitwise invariant across runs, parallelism layouts, and GPU vendors. Its key insight is that native FP32 accumulation of MXFP4 products is often already exact for every summation order. CertiSum collects statistics during quantization to certify native matrix multiplication results, recomputes uncertified outputs exactly, and uses exact kernels directly where certification rarely succeeds. CertiSum keeps quantization blocks unchanged across layouts and merges partial sums without rounding, including in attention and weight-gradient computation. In 200-step Qwen3-8B-Base experiments, CertiSum preserves training states bit for bit across AMD MI350X and NVIDIA GB200 and across changes in data, tensor, and context parallelism on MI350X. Across three 8B--14B models on FineWeb-Edu using MI350X, it adds 11.8--60.5% to training-step latency relative to its non-exact MXFP4 counterpart at the larger evaluated input shapes, with speedups of up to $1.24\times$ over BF16 and $1.70\times$ over deterministic BF16.

### 🤖 AI 总结

**一句话总结**：Training with MXFP4, a 4-bit microscaling format, is non-deterministic: identical inputs can produce different results across parallelism layouts and GPU vendors. These differences complicate debuggin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CertiSum, Bitwise-Identical, MXFP4, Training, Across, Platforms, Parallelism, Layouts

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21584v1) | [下载PDF](https://arxiv.org/pdf/2611.21584v1.pdf)

---

## [24. DynSurvX: Time-Resolved Explanations for Dynamic Survival Predictions](https://arxiv.org/abs/2611.21571v1)

**作者**：Van Tuan Nguyen, Agathe Guilloux  
**分类**：cs.LG  
**发布时间**：2026-11-16

### 📄 论文摘要

Recent survival models integrating longitudinal data achieve strong predictive performance, but their predictions are often difficult to interpret, limiting their clinical use. We propose DynSurvX, a model-agnostic explainability framework for dynamic survival prediction with mixed static and longitudinal covariates. Based on Shapley values, DynSurvX introduces a hierarchical two-phase strategy that first identifies influential longitudinal features and then adaptively refines their temporal importance, enabling fine-grained explanations while reducing computational cost. The framework provides time-resolved explanations that evolve as new patient data become available. Experiments on simulated and two clinical datasets show varying agreement with theoretical importance across prediction models, with closer agreement for better-performing models, alongside clinically interpretable insights in real-world settings. It remains robust across prediction settings and reduces computation time by 41--80\% relative to the temporal explanation baseline, making dynamic explanations practical.

### 🤖 AI 总结

**一句话总结**：Recent survival models integrating longitudinal data achieve strong predictive performance, but their predictions are often difficult to interpret, limiting their clinical use. We propose DynSurvX, a ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DynSurvX, Time-Resolved, Explanations, Dynamic, Survival, Predictions, Recent, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21571v1) | [下载PDF](https://arxiv.org/pdf/2611.21571v1.pdf)

---

## [25. Severe but Harmless: Stress-Testing Shift Severity for Frozen Time-Series Forecasters](https://arxiv.org/abs/2611.21562v1)

**作者**：Korede R. Bishi, Dominic Okonkwo, Adetayo Okunoye  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-16

### 📄 论文摘要

Zero-shot time-series foundation models (TSFMs) have become attractive alternatives to task-specific models because they handle diverse downstream tasks, including anomaly detection and forecasting, without per-series training. However, time-series data undergo distribution shifts, and the dissimilarity between two regimes is commonly scored with statistical measures such as Wasserstein-1, where a higher score is read as a more severe shift. In systematic experiments using three established severity measures on nine regime shifts from three standard traffic datasets, we show that these measures do not reliably predict degradation for instance-normalized TSFMs. The regimes rated most severe are not the regimes that degrade the models most, and degradation reaches 29% in the lowest-scoring regime. In most cases, the audit shows no positive relationship between measured severity and model degradation. We provide an equivariance-based stress-testing analysis that explains why severity readings can become decoupled from model degradation.

### 🤖 AI 总结

**一句话总结**：Zero-shot time-series foundation models (TSFMs) have become attractive alternatives to task-specific models because they handle diverse downstream tasks, including anomaly detection and forecasting, w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Severe, but, Harmless, Stress-Testing, Shift, Severity, Frozen, Time-Series

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21562v1) | [下载PDF](https://arxiv.org/pdf/2611.21562v1.pdf)

---

## [26. Reading or Remembering? Measuring Temporal Contamination in Language Models](https://arxiv.org/abs/2611.21554v1)

**作者**：Arunkumar V, Gangadharan G. R., S. Senthilkumar  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-11-16

### 📄 论文摘要

Language models are now used to read central-bank text for economic forecasting, but most were trained on text written after the documents they read. A model reading a 2021 FOMC statement may already know that inflation rose in 2022, so part of its apparent skill can be memory of the outcome, a temporal form of test-set contamination. We measure this memory on FOMC statements and minutes from 2000 to 2026 by comparing modern open models with chronologically consistent models, which are trained only on text from before a fixed date. Asked about past GDP outcomes given only a date, models that cannot know the answer still reach an AUC of up to 0.64 from priors on dates and eras, so chance is the wrong baseline. Against these memory-free models on the same questions, most modern models recall which years had strong growth. Membership-inference scores sort documents by era and document type rather than by whether a model saw them, as exact counts in an open pretraining corpus show. In real-time nowcasts, every lookahead premium we estimate on US GDP is smaller than the forecast comparison can detect at macroeconomic sample sizes, and none on GDP or inflation survives correction for multiple testing. Lookahead audits should therefore measure memory directly against memory-free models on the same items.

### 🤖 AI 总结

**一句话总结**：Language models are now used to read central-bank text for economic forecasting, but most were trained on text written after the documents they read. A model reading a 2021 FOMC statement may already ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：or, Reading, Remembering?, Measuring, Temporal, Contamination, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21554v1) | [下载PDF](https://arxiv.org/pdf/2611.21554v1.pdf)

---

## [27. Optimistic Verifiers Get Hacked: Reward Hacking Under an Exact Process Oracle](https://arxiv.org/abs/2611.21538v1)

**作者**：Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R. 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-11-16

### 📄 论文摘要

Reinforcement learning from verifiable rewards inherits whatever its verifier gets wrong. Outside mathematics and code the verifier is a proxy, a rubric, a learned judge or a hand-written checker, and its distance from the true objective is never measured, so a rising reward cannot be told apart from a hack. We build a setting where the true reward is exactly computable at the process level: executable authorization policies over 124,416 contexts admit an oracle that lists every minimal sufficient reason for every decision. We compile these policies into exact process rewards, degrade the verifier along seven realistic axes (outcome-only, sufficiency, recall-only, extraction noise, coarse taxonomy, stale policy, LLM judge), and train against each while the exact verifier scores every rollout. Four phenotypes appear. Optimistic verifiers are hacked by padding: the sufficiency proxy ends at 0.940 while true faithfulness falls from 0.731 to 0.667 on 96 held-out episodes. Outcome-only verifiers saturate and stop teaching, noise dilutes, and ranking-preserving gaps do no harm. A model-free audit of the verifier, its selection error and gap sign, together with a short saturation pilot, anticipates which phenotype a run will produce. Across nine configurations spanning two frameworks, two model vendors, two adapter sizes, three precisions, two initialisations and two seeds, the phenotypes recur, sufficiency damage is positive in all 10 replication cells and beyond two standard errors in 7, and optimistic gaps remain the steeper branch. The damage magnitude does not replicate, and five pre-registered attempts to explain it are reported as they fell. We release the testbed, the training instrumentation, and 14 real public policies (Cedar, OPA, Gatekeeper) ported to executable oracles.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning from verifiable rewards inherits whatever its verifier gets wrong. Outside mathematics and code the verifier is a proxy, a rubric, a learned judge or a hand-written checker, and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Optimistic, Verifiers, Get, Hacked, Reward, Hacking, Under

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21538v1) | [下载PDF](https://arxiv.org/pdf/2611.21538v1.pdf)

---

## [28. Algorithm Distillation for Safe In-Context Reinforcement Learning](https://arxiv.org/abs/2611.21524v1)

**作者**：Minjae Kwon, Amir Moeini, Shangtong Zhang 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-16

### 📄 论文摘要

Safe in-context reinforcement learning (Safe ICRL) asks a policy with fixed parameters to improve on an unseen constrained task from its interaction history while aiming to keep its cost within a budget. Prior work studied Safe ICRL on five benchmarks in three families: a grid world with a hidden goal and obstacles (DarkRoom), continuous navigation where goals and hazards stay invisible until reached (PointGoal, CarGoal), and locomotion with a hidden velocity limit (HalfCheetah, Ant). Safe Algorithm Distillation (Safe AD), trained on the learning histories of a safe RL algorithm, has shown adaptation failures in prior evaluations. For example, in the locomotion tasks its return stays below zero, and it rarely reaches the goal in CarGoal. We revisit two parts of Safe AD. First, we distill a budget-aware teacher with two phases. It searches for the hidden task, exploring more when more budget remains. After its first reward or cost, an expert policy exploits the task within the remaining budget. We collect the teacher's histories under fixed or dynamic budgets. Dynamic budgets increase the occupancy entropy of the return and budget inputs in every environment, and at test time they improve return and lower cost in DarkRoom and HalfCheetah. Second, we propose A-Lag, a test-time adjustment that reweights the distilled policy's actions by their predicted cost, with an adaptive Lagrange multiplier that is updated from the costs observed. In our experiments, A-Lag had lower mean episode cost than Safe AD in all five environments, with lower mean final return in four.

### 🤖 AI 总结

**一句话总结**：Safe in-context reinforcement learning (Safe ICRL) asks a policy with fixed parameters to improve on an unseen constrained task from its interaction history while aiming to keep its cost within a budg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Algorithm, Distillation, Safe, In-Context, Reinforcement, Learning, ICRL, asks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21524v1) | [下载PDF](https://arxiv.org/pdf/2611.21524v1.pdf)

---

## [29. Differentiable Exact Learning](https://arxiv.org/abs/2611.21486v1)

**作者**：Hristo Papazov, Francesco D'Angelo, Nicolas Flammarion  
**分类**：cs.LG, cs.AI, cs.FL, stat.ML  
**发布时间**：2026-11-16

### 📄 论文摘要

We introduce a framework for differentiable exact learning that couples an unbounded external environment to a state-tracking neural controller, which we train on policy-trajectory observations (PTOs): expert behavior traces that expose observations and actions while hiding internal states. In addition to the learning framework, we introduce Differentiable Finite-State Transducers (DFSTs) which use multilinear updates, support log-parallel training, and emulate arbitrary finite-state controllers, yielding computational universality through environmental interaction. From tiny training datasets, compact DFSTs achieve extreme length generalization on arithmetic and universal-simulation tasks. We replicate the success of DFSTs on RNNs and GRUs, thereby supporting a broader learning recipe: State-Tracking Controller + Unbounded External Environment + PTOs = Extreme Length Generalization. Beyond length generalization, our metric-extraction protocol recovers interpretable discrete controllers from trained DFSTs, which we prove equivalent to the target arithmetic and universal-simulation algorithms. Furthermore, for our Softmax DFST models, simply taking $\mathrm{argmax}$ over the transition probabilities yields discrete controllers which provably exactly perform universal Turing-machine simulation and binary arithmetic. Proving exact learning for the neural controllers requires assumptions, which we empirically support. We make our code, training recipes, model weights, and proof checkers publicly available at https://github.com/fanagor/DEL.

### 🤖 AI 总结

**一句话总结**：We introduce a framework for differentiable exact learning that couples an unbounded external environment to a state-tracking neural controller, which we train on policy-trajectory observations (PTOs)...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, an, Differentiable, Exact, Learning, introduce, framework, couples

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21486v1) | [下载PDF](https://arxiv.org/pdf/2611.21486v1.pdf)

---

## [30. Warm Starting Neural Dynamics Models From Few Jacobian Samples](https://arxiv.org/abs/2611.21465v1)

**作者**：Maxime Rochkoulets, Joppe De Jonghe, Mariya Ishteva  
**分类**：cs.LG, cs.AI, eess.SY  
**发布时间**：2026-11-16

### 📄 论文摘要

Model-based reinforcement learning (MBRL) leverages a model of the environment, used for planning and generating samples without interacting with the real world. Motivated by evidence that informed initialization significantly improves the efficiency of MBRL, we propose TDec-Init, an algorithm to warm-start neural dynamics models using transition Jacobians. Using a decoupling algorithm based on the decomposition of a tensor of stacked Jacobian samples, we recover weights and flexible nonlinearities, and use them to initialize a feedforward neural network. In the low-data regime, we show on several benchmark environments that our approach outperforms random initialization and value training, and either matches or outperforms Sobolev training, while requiring fewer training steps between episodes.

### 🤖 AI 总结

**一句话总结**：Model-based reinforcement learning (MBRL) leverages a model of the environment, used for planning and generating samples without interacting with the real world. Motivated by evidence that informed in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Warm, Starting, Neural, Dynamics, Models, Few, Jacobian, Samples

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.21465v1) | [下载PDF](https://arxiv.org/pdf/2611.21465v1.pdf)

---

