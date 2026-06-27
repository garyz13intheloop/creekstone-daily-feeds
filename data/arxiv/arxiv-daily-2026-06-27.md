# arXiv AI 论文日报 | 2026-06-27

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.AI](#csAI) (5 篇)
- [cs.CL](#csCL) (4 篇)

---

## cs.AI

## [1. Language-Based Digital Twins for Elderly Cognitive Assistance](https://arxiv.org/abs/2606.27334v1)

**作者**：Mohammad Mehdi Hosseini, Mohammad H. Mahoor, Hiroko H. Dodge  
**分类**：cs.AI  
**发布时间**：2026-06-25

### 📄 论文摘要

Digital twins have emerged as a promising paradigm for personalized healthcare, enabling modeling of individual behavior and health trajectories. In cognitive health, early detection of Mild Cognitive Impairment (MCI) remains challenging, where language and conversational patterns serve as non-invasive biomarkers. In this work, we propose a language-based digital twin framework that leverages large language models (LLMs) to mimic the conversational behavior of elderly individuals by incorporating stylometric cues and contextual metadata. To evaluate fidelity and cognitive consistency, we introduce a multi-head conditional variational autoencoder (cVAE) that jointly measures reconstruction quality and predicts cognitive scores. Experiments on the I-CONECT dataset show that the digital twin preserves identity-specific characteristics and achieves reconstruction and MoCA prediction errors comparable to real data, while outperforming baseline GPT-generated responses. These results highlight the potential of language-based digital twins as a scalable and non-invasive approach for personalized and continuous cognitive health monitoring.

### 🤖 AI 总结

**一句话总结**：Digital twins have emerged as a promising paradigm for personalized healthcare, enabling modeling of individual behavior and health trajectories. In cognitive health, early detection of Mild Cognitive...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Language-Based, Digital, Twins, Elderly, Cognitive, Assistance, have, emerged

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27334v1) | [下载PDF](https://arxiv.org/pdf/2606.27334v1.pdf)

---

## [2. When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models](https://arxiv.org/abs/2606.27288v1)

**作者**：Josef Chen  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-06-25

### 📄 论文摘要

Multi-model LLM systems such as routing, voting, cascades, fusion, and mixture-of-agents are used to beat single-model accuracy. We show that their gain is capped by a quantity the field rarely reports. For any policy whose output is one member model answer, accuracy cannot exceed one minus beta, where beta is the rate at which every model is wrong on the same query. In contrast, the usual diagnostic, average pairwise error correlation rho, cannot identify beta: error laws with identical marginals and pairwise correlations can have different all-wrong rates. A Clopper-Pearson bound on beta gives a finite-sample certificate on the largest gain any router, vote, or cascade could deliver before training a router.   Across 67 models from 21 providers, a tetrachoric-calibrated single-factor model still underprices the all-wrong tail: on open-ended mathematics, observed beta is 0.052 versus 0.023 under the full 67-model Gaussian copula, about 2.5 times underpricing, with 90 percent CI 1.7 to 3.4 and k equals 17. The effect recurs on execution-graded code, where beta is 0.079. Re-asking the same GPQA-Diamond questions in free-response rather than multiple-choice form reopens the tail, with beta 0.127 and a five-judge panel with kappa 0.73 to 0.92, locating co-failure in answer format rather than subject. At matched quality, low-rho heterogeneous ensembles beat high-rho Self-MoA, but on checkable tasks in our pool, combining models rarely beats the single best model without a strong query-level routing signal. Gains come from models failing on different questions, not from adding more models.

### 🤖 AI 总结

**一句话总结**：Multi-model LLM systems such as routing, voting, cascades, fusion, and mixture-of-agents are used to beat single-model accuracy. We show that their gain is capped by a quantity the field rarely report...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Does, Combining, Language, Models, Help?, Co-Failure, Ceiling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27288v1) | [下载PDF](https://arxiv.org/pdf/2606.27288v1.pdf)

---

## [3. Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings](https://arxiv.org/abs/2606.27287v1)

**作者**：Preet Baxi, Jiannan Xu, Jane Yi Jiang 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-25

### 📄 论文摘要

Large language models (LLMs) are increasingly used to screen and rank job applicants, creating incentives for candidates to strategically manipulate algorithmic hiring systems. We study prompt injection in automated résumé screening, defined as subtle self-promotional text that introduces no new qualifications but is designed to influence LLM evaluations. Using controlled experiments, we show that prompt injection reliably improves applicant rankings when résumé quality is homogeneous and few candidates inject. However, its effectiveness rapidly diminishes as more candidates inject, collapsing when manipulation becomes widespread. When candidate quality is heterogeneous, prompt injection is less effective on average, but can occasionally allow lower-quality candidates to outrank higher-quality ones, raising fairness concerns. Overall, LLM-based screening is most vulnerable when manipulation is rare and candidate quality differences are small. Code and resources are publicly available at: https://github.com/preetb1199/Prompt_Injection_ACL26

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly used to screen and rank job applicants, creating incentives for candidates to strategically manipulate algorithmic hiring systems. We study prompt injecti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Prompt, Injection, Automated, Résumé, Screening, Large, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27287v1) | [下载PDF](https://arxiv.org/pdf/2606.27287v1.pdf)

---

## [4. Simulation-based inference for rapid Bayesian parameter estimation in epidemiological models: a comparison with MCMC](https://arxiv.org/abs/2606.27286v1)

**作者**：Alina Bazarova, Johann Fredrik Jadebeck, Henrik Zunker 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-25

### 📄 论文摘要

Mechanistic epidemiological models are widely used to support infectious disease forecasting and public-health decision making. Bayesian calibration of such models is commonly performed using Markov chain Monte Carlo (MCMC), which can become computationally expensive for high-dimensional nonlinear systems and repeated near-real-time analyses. Here, we investigate simulation-based inference (SBI) using neural posterior estimation as a scalable alternative for Bayesian calibration of a mechanistic SECIR epidemiological model using COVID-19 intensive care unit (ICU) occupancy data from Germany during 2020. We compared SBI and MCMC across multiple epidemic phases using both 31-day inference windows and a substantially more challenging 201-day reconstruction problem involving multiple transmission change points. Posterior agreement was evaluated quantitatively using Wasserstein distances and Kullback-Leibler divergences together with posterior predictive checks. Across the 31-day windows, SBI recovered posterior distributions in strong agreement with MCMC while accurately reproducing observed ICU trajectories. In the 201-day setting, SBI preserved the dominant posterior structure despite increased uncertainty. SBI, by combining CPU and GPU resources, substantially reduced computational runtime compared with MCMC, which was restricted to running on CPUs. Whereas MCMC required approximately 1000 seconds for the 31-day inference problems, SBI achieved comparable posterior and predictive performance in approximately 60-70 seconds on a single GPU. For the 201-day inference problem, SBI required an average of 157 seconds, while the MCMC runs took over 19,000 seconds. Our results demonstrate that SBI provides a rapid and computationally efficient framework for Bayesian calibration of mechanistic epidemiological models, supporting repeated near-real-time inference and rapid outbreak analysis.

### 🤖 AI 总结

**一句话总结**：Mechanistic epidemiological models are widely used to support infectious disease forecasting and public-health decision making. Bayesian calibration of such models is commonly performed using Markov c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Simulation-based, inference, rapid, Bayesian, parameter, estimation, epidemiological, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27286v1) | [下载PDF](https://arxiv.org/pdf/2606.27286v1.pdf)

---

## [5. EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting](https://arxiv.org/abs/2606.27277v1)

**作者**：Junwei Luo, Shuai Yuan, Zhenya Yang 等 6 位作者  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-06-25

### 📄 论文摘要

Earth Observation (EO) forecasting aims to predict future Earth surface dynamics from satellite observations under changing meteorological conditions. In this paper, we view this task as a partially observed, weather-driven world modeling problem, in which weather acts as a conditioning signal, while forecasting remains uncertain due to sparse observations and unobserved land-surface states. However, existing methods do not fully capture this setting: deterministic models collapse uncertainty into a single future prediction, while diffusion-based methods typically treat weather variables as undifferentiated conditioning signals, and existing benchmarks focus mainly on reconstruction accuracy rather than whether forecasts respond correctly to changed weather forcing.We introduce EO-WM, a video diffusion transformer for multispectral EO forecasting. EO-WM incorporates a physically informed conditioning framework that represents meteorological forcing through a climatological baseline, weather anomalies, and cumulative physical stress signals. Specifically, it separates baseline and anomaly through distinct conditioning pathways, and accumulates anomalous forcing over time to capture sustained heat and drought stress. To evaluate weather-response behavior beyond standard metrics, we introduce two diagnostic benchmarks: an Extreme Summer Benchmark for severity-aware prediction of vegetation degradation under extreme weather, and a Seasonal Matched-Pair Benchmark for testing response fidelity under changed weather forcing. Experiments show that EO-WM reduces the error in predicted Normalized Difference Vegetation Index (NDVI) decline amplitude by a relative 5.63% and improves directional hit rate by a relative 7.80%, while remaining competitive on standard pixel-level metrics. The benchmarks and model will be made open-source at https://github.com/Luo-Z13/EO-WM.

### 🤖 AI 总结

**一句话总结**：Earth Observation (EO) forecasting aims to predict future Earth surface dynamics from satellite observations under changing meteorological conditions. In this paper, we view this task as a partially o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EO-WM, Physically, Informed, World, Model, Probabilistic, Earth, Observation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27277v1) | [下载PDF](https://arxiv.org/pdf/2606.27277v1.pdf)

---

## cs.CL

## [6. Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning](https://arxiv.org/abs/2606.27330v1)

**作者**：Tianyi Men, Zhuoran Jin, Pengfei Cao 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.CV, cs.LG  
**发布时间**：2026-06-25

### 📄 论文摘要

Multimodal web agents can assist humans in operating repetitive GUI tasks, where effective task planning is essential for decomposing complex tasks into executable actions. While small open source MLLMs are cost efficient and privacy preserving compared with commercial large models, they suffer from weak planning and limited cross website generalization. To address these limitations, we introduce the planning experience exploration and utilization (PEEU) method, which autonomously explores environments to discover experiences and utilizes hindsight experience to synthesize strictly aligned, high level training data. To quantitatively analyze the generalization behaviors driving this performance, we propose the task decomposition hierarchical analysis framework (TDHAF) to systematically study compositional generalization across three task granularities: low, middle and high levels. Our analysis reveals that mastering low level atomic skills does not guarantee high level planning competence, while high level task training yields stronger OOD generalization. Experiments on real world benchmarks demonstrate PEEU's superior effectiveness: our 7B model achieves 30.6% accuracy, outperforming the much larger Qwen2.5-VL-32B model. These demonstrate constructing hindsight high level tasks and leveraging experiences is crucial for OOD planning abilities of small MLLMs.

### 🤖 AI 总结

**一句话总结**：Multimodal web agents can assist humans in operating repetitive GUI tasks, where effective task planning is essential for decomposing complex tasks into executable actions. While small open source MLL...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Empowering, GUI, via, Autonomous, Experience, Exploration, Hindsight

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27330v1) | [下载PDF](https://arxiv.org/pdf/2606.27330v1.pdf)

---

## [7. LLM-Based Examination of Eligibility Criteria from Securities Prospectuses at the German Central Bank](https://arxiv.org/abs/2606.27316v1)

**作者**：Serhii Hamotskyi, Akash Kumar Gautam, Christian Hänig  
**分类**：cs.CL  
**发布时间**：2026-06-25

### 📄 论文摘要

Verifying the eligibility of securities as collateral is a key responsibility of the German Central Bank. However, manually verifying these assets against legal and financial criteria within lengthy, semi-structured, and often bilingual prospectuses is a resource-intensive task. While previous efforts utilized traditional Named Entity Recognition (NER) for information extraction, these methods can struggle with OCR noise, linguistic variance, and rigid span-based constraints, and the need for manually annotated training data for each relevant annotation type. In this paper, we present the first case study applying Large Language Models (LLMs) to the eligibility examination process, shifting the paradigm toward a generative Information Extraction pipeline. Our approach decomposes the task into extraction, normalization, and interpretation, allowing for greater flexibility in handling noisy text and interleaved German-English content. We further introduce a value-based evaluation methodology using LLM-as-a-judge, which offers a more semantic assessment than location-based metrics. Our results demonstrate that LLM-based systems achieve high precision (up to 91%) in document-level eligibility, exhibiting a conservative operating profile that minimizes false acceptance.

### 🤖 AI 总结

**一句话总结**：Verifying the eligibility of securities as collateral is a key responsibility of the German Central Bank. However, manually verifying these assets against legal and financial criteria within lengthy, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, at, LLM-Based, Examination, Eligibility, Criteria, Securities, Prospectuses

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27316v1) | [下载PDF](https://arxiv.org/pdf/2606.27316v1.pdf)

---

## [8. Beyond Surface Forms: A Comprehensive, Mechanism-Oriented Taxonomy of Indirect Linguistic Encoding for LLM-Based Coded Language Detection](https://arxiv.org/abs/2606.27314v1)

**作者**：Hamid Reza Firoozfar, Mohammadsadegh Abolhasani, Reza Mousavi 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-25

### 📄 论文摘要

To avoid moderation and surveillance on social media, some users routinely invent indirect linguistic expressions (ILE) that camouflage sensitive meanings. Such expressions surface as algospeak, euphemisms, and adversarial obfuscation, depending on intent and context, and they involve recurring encoding mechanisms. We propose a comprehensive, mechanism-oriented taxonomy of ILE that abstracts away from communicative goals and instead categorizes the underlying operations through which meaning is encoded and recovered. We evaluate the taxonomy by incorporating it into LLM prompts and comparing it with four existing taxonomies and a no-taxonomy baseline, using 2,000 manually annotated TikTok and Bluesky posts. The proposed taxonomy attains the strongest document- and span-level performance across the three LLMs, achieving an improvement of 4.7% in accuracy and 5.4% in F1 over the best-performing benchmark. The empirical results reveal the importance of a comprehensive, mechanism-oriented taxonomy as a stable scaffold for detecting emerging coded language and a useful input to content moderation. Disclaimer: This paper contains content that may be profane, vulgar, or offensive.

### 🤖 AI 总结

**一句话总结**：To avoid moderation and surveillance on social media, some users routinely invent indirect linguistic expressions (ILE) that camouflage sensitive meanings. Such expressions surface as algospeak, euphe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Beyond, Surface, Forms, Comprehensive, Mechanism-Oriented, Taxonomy, Indirect

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27314v1) | [下载PDF](https://arxiv.org/pdf/2606.27314v1.pdf)

---

## [9. Multilingual Reasoning Cascades Need More Context](https://arxiv.org/abs/2606.27306v1)

**作者**：Arnav Mazumder, Dengjia Zhang, Shuyue Stella Li 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-25

### 📄 论文摘要

Translation cascades for reasoning translate the query from another language to English, reason in English, and translate the answer back to the original language. This is a competitive approach to multilingual reasoning, but structurally lossy, since each stage discards information later stages may need, including cues for cultural grounding, register, and disambiguation. We examine the benefits of a simple and training-free intervention: a context-aware translation cascade, which additionally provides the original question, the English translated question, and the reasoning trace to the context of the final translation module. We evaluate gains across nine multilingual benchmarks including various task types, three backbone models, and 285 high-, mid-, and low-resource languages, and demonstrate strong gains for open-ended generation across models and resource regimes. We show that the original language question carries most of the beneficial context. Our study emphasizes the need to better design information flow in machine translation cascades for mitigating error propagation, and provides a simple and actionable default strategy: preserve the original user question until the end of the pipeline.

### 🤖 AI 总结

**一句话总结**：Translation cascades for reasoning translate the query from another language to English, reason in English, and translate the answer back to the original language. This is a competitive approach to mu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multilingual, Reasoning, Cascades, Need, More, Context, Translation, translate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27306v1) | [下载PDF](https://arxiv.org/pdf/2606.27306v1.pdf)

---

## cs.CV

## [10. DanceOPD: On-Policy Generative Field Distillation](https://arxiv.org/abs/2606.27377v1)

**作者**：Wei Zhou, Xiongwei Zhu, Zelin Xu 等 11 位作者  
**分类**：cs.CV, cs.CL, cs.LG  
**发布时间**：2026-06-25

### 📄 论文摘要

Modern image generation demands a single model that unifies diverse capabilities, including text-to-image (T2I), local editing, and global editing. However, these capabilities are rarely naturally aligned and often conflict. For instance, editing tends to degrade T2I performance, while global and local editing interfere with each other. Consequently, effectively composing these capabilities has become a central challenge for image generation model training. To tackle this, we introduce DanceOPD, an on-policy generative field distillation framework for flow-matching models that routes each sample to one capability field, queries one low-noise student-induced state, and trains with a simple velocity MSE objective. With each capability source defined as a velocity field over the shared flow state space, the student learns from fields queried on its own rollout states to compose expert capabilities. This formulation also absorbs operator-defined fields such as classifier-free guidance. Comprehensive experiments on T2I, editing, realism-field absorption, and CFG absorption show that our approach improves multi-capability composition, strengthening target capabilities while preserving anchor generation quality. We believe this work establishes a practical route for generative field distillation in flow-matching models.

### 🤖 AI 总结

**一句话总结**：Modern image generation demands a single model that unifies diverse capabilities, including text-to-image (T2I), local editing, and global editing. However, these capabilities are rarely naturally ali...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DanceOPD, On-Policy, Generative, Field, Distillation, Modern, image, generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27377v1) | [下载PDF](https://arxiv.org/pdf/2606.27377v1.pdf)

---

## [11. DnA: Denoising Attention for Visual Tasks](https://arxiv.org/abs/2606.27372v1)

**作者**：Ron Campos, Subhajit Maity, Xin Li 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-25

### 📄 论文摘要

The softmax activation in multihead attention (MHA) is the de facto standard for attention-based models in visual perception tasks. However, standard softmax can produce noisy attention patterns that dilute relevant features and degrade its performance. In this paper, we propose Denoising Attention or DnA, in which, first, a positive query identifies which image features belong to the correct class, and a negative query identifies closely associated but irrelevant image features. DnA then projects these interactions into two distinct subspaces with larger principal angles, promoting subspace separation and improved discriminability. Using a ViT-B backbone, our proposed DnA achieves an absolute gain of 0.8% on ImageNet-1K compared to the baseline. We further show improvements across multiple visual understanding tasks, including video understanding with video transformers (1.8%) and video LLMs (0.5%). Our extensive empirical analyses justify the design choices involving two interacting subspaces and the denoising effect of DnA.

### 🤖 AI 总结

**一句话总结**：The softmax activation in multihead attention (MHA) is the de facto standard for attention-based models in visual perception tasks. However, standard softmax can produce noisy attention patterns that ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DnA, Denoising, Attention, Visual, Tasks, softmax, activation, multihead

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27372v1) | [下载PDF](https://arxiv.org/pdf/2606.27372v1.pdf)

---

## [12. Don't Settle at the Mode! Mitigating Diversity Collapse in Pretrained Flow Models via Feature Self-Guidance](https://arxiv.org/abs/2606.27371v1)

**作者**：Pradhaan S Bhat, Rishubh Parihar, Abhijnya Bhat 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-25

### 📄 论文摘要

State-of-the-art flow models generate stunning images from text or image prompts. However, they suffer from diversity collapse when generating multiple samples under the same conditioning. Existing methods address this issue via either latent guidance, which has limited effectiveness, or sample selection, which relies on external reward models that incur significant inference-time overhead. In this work, we introduce an efficient, training-free self-guidance mechanism to mitigate diversity collapse without requiring additional reward models. Specifically, we disperse the internal features of the flow model during batch generation with feature self-guidance. Further, to keep the features close to the manifold, we introduce a manifold regularization step that projects these dispersed features back onto the data manifold, ensuring diverse generation without sacrificing alignment with the input conditions. Our method integrates seamlessly as a plug-and-play module into pretrained flow models, adding only a marginal inference cost. Experiments demonstrate significant improvements in diversity while preserving fidelity across several conditional flow models, including multi-step and few-step text-to-image, depth-to-image, and reference image generation.

### 🤖 AI 总结

**一句话总结**：State-of-the-art flow models generate stunning images from text or image prompts. However, they suffer from diversity collapse when generating multiple samples under the same conditioning. Existing me...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Don't, Settle, Mode!, Mitigating, Diversity, Collapse, Pretrained

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27371v1) | [下载PDF](https://arxiv.org/pdf/2606.27371v1.pdf)

---

## [13. PhysiFormer: Learning to Simulate Mechanics in World Space](https://arxiv.org/abs/2606.27364v1)

**作者**：Yiming Chen, Yushi Lan, Andrea Vedaldi  
**分类**：cs.CV  
**发布时间**：2026-06-25

### 📄 论文摘要

We present PhysiFormer, a diffusion transformer for physically-plausible 3D object motion. Unlike video world models that operate in view-dependent pixel space, PhysiFormer represents objects as 3D meshes expressed in world coordinates. Given the initial vertex positions and velocities, as well as object material type, rigid or elastic, the model samples future vertex trajectories. While related neural physics approaches build on ad-hoc latent spaces or explicitly enforce rigidity and causality, PhysiFormer shows that excellent results can be obtained without any such inductive biases, by casting vertex trajectory prediction as a single denoising diffusion process directly in world coordinates. The probabilistic formulation captures uncertainty in the learned dynamics, enabling diverse plausible futures from initial conditions, making this framework potentially useful for applications with unobserved uncertainty. The model features attention factorised over time, space, and objects for efficiency, enabling permutation-invariant multi-object reasoning without needing explicit object encoding. Trained on over 100k simulated trajectories, PhysiFormer generates rigid and elastic mechanics, and generalises to mixed-material settings, unseen real-world geometries, and larger object counts. It substantially outperforms autoregressive baselines in trajectory accuracy, rigidity preservation, and momentum-based physical consistency. Our results position coordinate-space diffusion as a promising step toward view-invariant, geometry-aware world modelling for robotics, graphics, and physical design. Visualisations, code, and models are available at https://yimingc9.github.io/physiformer.

### 🤖 AI 总结

**一句话总结**：We present PhysiFormer, a diffusion transformer for physically-plausible 3D object motion. Unlike video world models that operate in view-dependent pixel space, PhysiFormer represents objects as 3D me...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, PhysiFormer, Learning, Simulate, Mechanics, World, Space, present

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27364v1) | [下载PDF](https://arxiv.org/pdf/2606.27364v1.pdf)

---

## [14. SAM2Matting: Generalized Image and Video Matting](https://arxiv.org/abs/2606.27339v1)

**作者**：Ruiqi Shen, Guangquan Jie, Chang Liu 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-25

### 📄 论文摘要

Despite impressive advances in image matting, video matting remains challenging due to the inherent gap between high-level tracking, which requires frame-wise understanding, and low-level matting, which focuses on extremely fine-grained details. Existing methods attempt this with expensive and narrowly-scoped video matting datasets, which may limit out-of-domain generalization and compromise tracking robustness. We rethink the paradigm with SAM2Matting, a tracker-to-matting framework that advances VOS trackers to high-fidelity video matting. Specifically, it decouples the task by enhancing a foundational tracker (e.g., SAM2, SAM3) with a region-proposal bridge and dedicated matting heads, enabling the uncompromised tracker to handle temporal consistency while the matting components resolve fine-grained details. Notably, despite being trained only on images, SAM2Matting establishes new state-of-the-art performance on video matting, supports diverse prompt types, maintains strong temporal consistency, and demonstrates robust generalization across both human-centric and in-the-wild scenarios.

### 🤖 AI 总结

**一句话总结**：Despite impressive advances in image matting, video matting remains challenging due to the inherent gap between high-level tracking, which requires frame-wise understanding, and low-level matting, whi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SAM2Matting, Generalized, Image, Video, Matting, Despite, impressive, advances

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27339v1) | [下载PDF](https://arxiv.org/pdf/2606.27339v1.pdf)

---

## [15. RoPEMover: Depth-Aware Object Relocation via Positional Embeddings](https://arxiv.org/abs/2606.27332v1)

**作者**：Ipek Oztas, Duygu Ceylan, Aybars Bugra Aksoy 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-25

### 📄 论文摘要

Moving an object in a single image requires geometry-consistent spatial rearrangement, including handling occlusions, revealing previously unseen regions, and maintaining coherent shadows and reflections. Existing approaches are not well suited to this setting and often fail to preserve such scene-level consistency. We address this problem by introducing a geometry-aware object motion method that operates directly on the positional representations of diffusion transformers. Our key insight is that rotary positional embeddings (RoPE) define a structured spatial field that can be explicitly manipulated to induce controlled motion. We extend 2D RoPE into a depth-aware formulation that encodes 3D spatial structure, enabling consistent object displacement and scene-aware updates. Our model is trained using synthetic data combined with a small set of real images via parameter-efficient fine-tuning. Despite minimal real supervision, it preserves object identity under large spatial displacements, generates plausible content in newly revealed regions, and consistently updates scene-dependent effects such as shadows and illumination. Experimental results on standard object motion benchmarks demonstrate state-of-the-art performance across all evaluation metrics.

### 🤖 AI 总结

**一句话总结**：Moving an object in a single image requires geometry-consistent spatial rearrangement, including handling occlusions, revealing previously unseen regions, and maintaining coherent shadows and reflecti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RoPEMover, Depth-Aware, Object, Relocation, via, Positional, Embeddings, Moving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27332v1) | [下载PDF](https://arxiv.org/pdf/2606.27332v1.pdf)

---

## [16. ViQ: Text-Aligned Visual Quantized Representations at Any Resolution](https://arxiv.org/abs/2606.27313v1)

**作者**：Xumin Yu, Zuyan Liu, Zhenyu Yang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-25

### 📄 论文摘要

A unified representation for text and vision is a natural pursuit, as it enables simpler multimodal modeling and more efficient training. However, representing images as discrete signals in the same way as text inevitably introduces severe information loss. Existing work struggles to balance low-level details and high-level semantics in discrete representations: reconstruction-oriented representations often lack semantic information, whereas semantically stronger features typically suffer from severe loss of detail. We present ViQ, a Visual Quantized Representations framework, which is designed to balance semantics and details in discrete representations while supporting inputs at native resolutions, thereby enabling it to serve as a unified and general discrete representation for arbitrary visual inputs. Our approach structures quantization learning into two stages: text-aligned pre-training and feature discretization. With text-aligned pre-training, we enhance the visual encoder semantic-rich supervision from the pretrained language model and enable it to process native-resolution visual inputs. During discretization, we propose a proximal representation learning strategy to progressively compact the feature space, along with a position-aware head-wise quantization mechanism that enables flexible processing of arbitrary resolutions. Extensive experiments on multimodal tasks demonstrate that ViQ achieves competitive performance compared to state-of-the-art multimodal vision encoders with continuous and high-dimensional visual features, while maintaining high precision in low-level reconstruction. We also show that multimodal training with visual quantized representations largely improves efficiency, yielding up to 20\%-70\% acceleration with different base LLMs and training recipes.

### 🤖 AI 总结

**一句话总结**：A unified representation for text and vision is a natural pursuit, as it enables simpler multimodal modeling and more efficient training. However, representing images as discrete signals in the same w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, ViQ, Text-Aligned, Visual, Quantized, Representations, Any, Resolution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27313v1) | [下载PDF](https://arxiv.org/pdf/2606.27313v1.pdf)

---

## [17. See & Sniff: Learning Visuo-Olfactory Representations](https://arxiv.org/abs/2606.27307v1)

**作者**：Seongyu Kim, Seungwoo Lee, Hyeonggon Ryu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-25

### 📄 论文摘要

While modern multimodal models integrate vision with language, audio, or touch, olfaction remains largely unexplored due to the lack of paired visuo-olfactory data. We introduce SmellNet-V, a scalable visuo-olfactory dataset built on the insight that odor identity is largely invariant to visual transformations within a semantic category. This allows us to synthetically pair smell-only samples with semantically aligned in-the-wild web images, converting a unimodal olfactory dataset into a cross-modal benchmark without costly co-collection. Building on this dataset, we propose See & Sniff, a self-supervised framework that learns joint visuo-olfactory representations via dense local alignment and naturally produces smell saliency maps for spatial grounding of odor sources. We further introduce pixel-level smell localization task and a benchmark for evaluation. Our method surpasses smell-only baselines by 7% in smell classification from smell alone and generalizes to cross-modal retrieval and smell localization, establishing visuo-olfactory learning as a new direction in multimodal perception.

### 🤖 AI 总结

**一句话总结**：While modern multimodal models integrate vision with language, audio, or touch, olfaction remains largely unexplored due to the lack of paired visuo-olfactory data. We introduce SmellNet-V, a scalable...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：See, Sniff, Learning, Visuo-Olfactory, Representations, While, modern, multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27307v1) | [下载PDF](https://arxiv.org/pdf/2606.27307v1.pdf)

---

## [18. Sculpting NeRF Geometry: Human-Preference Fine-Tuning of a 3D-Aware Face GAN](https://arxiv.org/abs/2606.27305v1)

**作者**：Archer Moore, Mingming Gong, Liam Hodgkinson  
**分类**：cs.CV  
**发布时间**：2026-06-25

### 📄 论文摘要

Reinforcement learning from human feedback (RLHF) for 3D generation is now established across a number of works, but most existing pipelines optimise explicit surface representations, often by converting radiance fields into meshes and training heavily on surface-supervised data. We instead fine-tune a pretrained 3D-aware generative model directly from a learned reward over radiance-field density ($σ$) values, with no externally supplied mesh or shape prior. The reward model requires no pretraining, trains easily on a small set of preference samples, and yields robust improvement in 3D geometry. Working on an unconditional 3D-aware face GAN (EG3D), our reward reads the continuous 3D density field of the neural radiance field (NeRF) directly and supplies a geometry-only learning signal, requiring neither text conditioning, mesh extraction, nor multi-view rendering. A density-consistency constraint keeps the 2D appearance qualitatively similar while the geometry is reshaped, at a measurable but bounded distributional cost (FID-50k rises from 4.09 to 6.66): the fine-tuned generator, trained from the preferences of a single annotator as a proof of concept, produces face geometries preferred by users in 74.4% of pairwise comparisons.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning from human feedback (RLHF) for 3D generation is now established across a number of works, but most existing pipelines optimise explicit surface representations, often by convert...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Sculpting, NeRF, Geometry, Human-Preference, Fine-Tuning, 3D-Aware, Face

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27305v1) | [下载PDF](https://arxiv.org/pdf/2606.27305v1.pdf)

---

## [19. Exact and Deterministic Patch Descriptor Retrieval via Hierarchical Normalization](https://arxiv.org/abs/2606.27280v1)

**作者**：Koichi Sato  
**分类**：cs.CV  
**发布时间**：2026-06-25

### 📄 论文摘要

We present a patch descriptor retrieval method that returns the exact nearest neighbour -- provably identical to exhaustive full-vector search -- while evaluating only a small fraction of the database, and does so deterministically: the same (database, query) pair always produces the same result, independent of run order, thread count, or hardware. This contrasts with approximate nearest-neighbour (ANN) approaches such as HNSW and IVF-PQ, which trade exactness for speed and may return different results across runs. The enabling mechanism is Hierarchical Normalization (HN): a normalisation scheme that splits the pre-normalisation feature vector into a K-dim major component (norm sqrt(1-alpha)) and a (128-K)-dim minor component (norm sqrt(alpha)). Since the minor inner product is bounded by alpha (Cauchy-Schwarz on the prescribed norms), the major similarity plus alpha is an admissible upper bound on the full similarity: the search scans the K-dim major component for all entries, then applies full 128-dim evaluation only to entries that cannot be pruned -- a provably exact branch-and-bound scan. We train HN-modified HardNet on the notredame split of the UBC patch dataset and evaluate on trevi and halfdome. With a cache-optimised Structure-of-Arrays layout and K=8, alpha=1/32, the search achieves 13.7x (trevi) / 12.7x (halfdome) speed-up over brute-force 128-dim search, with only 0.4% of entries requiring full evaluation. At K=16, alpha=1/8, FPR@95 rises from 0.0062 to 0.0064 on trevi at 7.2x speed-up, with 98.8% of entries bypassing full evaluation.

### 🤖 AI 总结

**一句话总结**：We present a patch descriptor retrieval method that returns the exact nearest neighbour -- provably identical to exhaustive full-vector search -- while evaluating only a small fraction of the database...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Exact, Deterministic, Patch, Descriptor, Retrieval, via, Hierarchical, Normalization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27280v1) | [下载PDF](https://arxiv.org/pdf/2606.27280v1.pdf)

---

## [20. CORTEX: A Structured Reasoning Benchmark for Trustworthy 3D Chest CT MLLMs](https://arxiv.org/abs/2606.27264v1)

**作者**：Hashmat Shadab Malik, Anees Ur Rehman Hashmi, Numan Saeed 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-25

### 📄 论文摘要

Reasoning in multimodal large language models (MLLMs) has shown strong promise in medical imaging. However, this reasoning is usually free-form text judged only by its final answer, making it hard to interpret and verify, especially in 3D radiology, where a diagnosis should be traceable to evidence in the scan. Existing chest CT question-answering datasets compound this by reducing expert radiology reports to answer-only pairs, dropping the reasoning that links findings to conclusions and omitting the patient history clinicians rely on. As a result, reasoning-capable 3D chest CT MLLMs remain out of reach, as neither the structured supervision needed to train them nor the protocol needed to verify their reasoning yet exists. We introduce CORTEX (Clinically Organized Reasoning and sTructured EXplanation), a structured reasoning benchmark for 3D chest CT. For each question, CORTEX restores the missing reasoning as a four-stage diagnostic trace mirroring a radiologist's workflow: task understanding, visual observation, diagnostic reasoning, and answer synthesis. We generate these traces using frontier large language models with broad medical and general-domain knowledge, then filter and verify them with a stage-level evaluation protocol combining automated rubric scoring with expert radiologist review. Crucially, both the reasoning structure and evaluation rubrics are designed in close collaboration with clinicians. Built on CT-RATE, a large, publicly available chest CT dataset without reasoning annotations, CORTEX comprises 76,177 validated reasoning traces across open-ended VQA, closed-ended VQA, and report generation, providing both the structured supervision and the stage-level evaluation protocol needed to build and evaluate trustworthy reasoning models for 3D chest CT. Our dataset and evaluation code will be made publicly available upon acceptance.

### 🤖 AI 总结

**一句话总结**：Reasoning in multimodal large language models (MLLMs) has shown strong promise in medical imaging. However, this reasoning is usually free-form text judged only by its final answer, making it hard to ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, CT, CORTEX, Structured, Reasoning, Benchmark, Trustworthy, Chest

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27264v1) | [下载PDF](https://arxiv.org/pdf/2606.27264v1.pdf)

---

## cs.LG

## [21. Reinforcement Learning without Ground-Truth Solutions can Improve LLMs](https://arxiv.org/abs/2606.27369v1)

**作者**：Yingyu Lin, Qiyue Gao, Nikki Lijing Kuang 等 9 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-25

### 📄 论文摘要

Reinforcement learning with verifiable rewards (RLVR) for training LLMs typically rely on ground-truth answers to assign rewards, limiting their applicability to tasks where the ground-truth solution is unknown. We introduce a \textbf{R}anking-\textbf{i}nduced \textbf{VER}ifiable framework (RiVER) that trains LLMs on score-based optimization tasks without ground-truth solutions, using deterministic execution feedback as continuous-valued supervision. When applying group-relative RL to such continuous rewards, we identify two key challenges: \emph{scale dominance}, where uncalibrated score magnitudes across test instances distort policy updates, and \emph{frequency dominance}, where repeatedly sampled suboptimal solutions can outweigh rare but stronger candidates. RiVER addresses these challenges with calibrated reward shaping that uses instance-wise comparisons and emphasizes top-ranked solvers while retaining bounded feedback for other valid solutions. We train on 12 AtCoder Heuristic Contest tasks and evaluate on Algorithm Engineering Benchmark (ALE-Bench), LiveCodeBench, and USACO. RiVER advances Qwen3-8B and GLM-Z1-9B-0414 by 8.9\% and 9.4\% in ALE rating rank. More importantly, despite training exclusively on score-based tasks without any ground-truth solutions, RiVER also improves the backbones across exact-solution benchmarks such as LiveCodeBench and USACO by an absolute average improvement of 2.4\% and 3.5\%. By contrast, baselines trained with raw execution scores improve ALE rating but fail to transfer to exact-solution benchmarks. These results suggest that score-based optimization tasks, combined with proper reward calibration, can serve as effective training environments for general coding ability without ground-truth solutions.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning with verifiable rewards (RLVR) for training LLMs typically rely on ground-truth answers to assign rewards, limiting their applicability to tasks where the ground-truth solution ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Reinforcement, Learning, without, Ground-Truth, Solutions, can, Improve

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27369v1) | [下载PDF](https://arxiv.org/pdf/2606.27369v1.pdf)

---

## [22. Autoregressive Boltzmann Generators](https://arxiv.org/abs/2606.27361v1)

**作者**：Danyal Rehman, Charlie B. Tan, Yoshua Bengio 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-25

### 📄 论文摘要

Efficient sampling of molecular systems at thermodynamic equilibrium is a hallmark challenge in statistical physics. This challenge has driven the development of Boltzmann Generators (BGs), which allow rapid generation of uncorrelated equilibrium samples by combining a generative model with exact likelihoods and an importance sampling correction. However, modern BGs predominantly rely on normalizing flows (NFs), which either suffer from limited expressivity due to strict invertibility constraints (discrete time) or computationally expensive likelihoods (continuous time). In this paper, we propose Autoregressive Boltzmann Generators (ArBG) -- a novel autoregressive modelling framework -- that overcomes these limitations by departing from the flow-based BG paradigm. ArBG circumvents the topological constraints of flows and enables sequential inference-time interventions, while offering enhanced scalability by leveraging architectures effective in Large Language Models. We empirically demonstrate that ArBG leads to significant improvements over flow-based models across all benchmarks, but particularly in larger peptide systems such as the 10-residue Chignolin. Furthermore, we introduce Robin, a 132 million parameter transferable model trained with the ArBG framework which improves over the previous state-of-the-art, reducing the zero-shot energy error, E-W$_2$, on 8-residue systems by over 60$\%$. The code can be found at the following link: https://github.com/danyalrehman/autobg.

### 🤖 AI 总结

**一句话总结**：Efficient sampling of molecular systems at thermodynamic equilibrium is a hallmark challenge in statistical physics. This challenge has driven the development of Boltzmann Generators (BGs), which allo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Autoregressive, Boltzmann, Generators, Efficient, sampling, molecular, systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27361v1) | [下载PDF](https://arxiv.org/pdf/2606.27361v1.pdf)

---

## [23. Error-Conditioned Neural Solvers](https://arxiv.org/abs/2606.27354v1)

**作者**：Haina Jiang, Liam Wang, Peng-Chen Chen 等 7 位作者  
**分类**：cs.LG, cs.AI, cs.CV, math.NA  
**发布时间**：2026-06-25

### 📄 论文摘要

Neural surrogate models offer fast approximate mappings from PDE parameters to solutions, but they typically treat solving as a purely statistical task: once trained, they struggle to correct their own constraint violations and extrapolate beyond the training distribution. Recent hybrid methods promote physical correctness by targeting the PDE residual via gradient descent or Gauss--Newton steps, but inherit the compute cost and instability of the underlying classical optimizers. We show, theoretically and empirically, that numerically minimizing the PDE residual can be an unreliable proxy for reconstruction accuracy in ill-conditioned systems, explaining why these methods often do not make accurate predictions despite achieving low residuals. We propose error-conditioned Neural Solvers (ENS), built on a different principle: rather than an optimization target, the PDE residual field is passed as a direct input to the network at each iteration, enabling it to read the spatial structure of its own errors and learn an update policy to iteratively correct its predictions. Across four PDE families, ENS attains the highest prediction accuracy in the large majority of settings, with gains reaching $10\times$ on turbulent Kolmogorov flow, while avoiding the expensive compute cost of hybrid methods. ENS's learned correction policy generalizes under distribution shift, including zero-shot parameter changes and cross-equation transfer, where its relative advantage is largest in the ill-conditioned regimes where residual minimization is least reliable. Project website: https://neuralsolver.github.io/.

### 🤖 AI 总结

**一句话总结**：Neural surrogate models offer fast approximate mappings from PDE parameters to solutions, but they typically treat solving as a purely statistical task: once trained, they struggle to correct their ow...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Error-Conditioned, Neural, Solvers, surrogate, models, offer, fast, approximate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27354v1) | [下载PDF](https://arxiv.org/pdf/2606.27354v1.pdf)

---

## [24. Hallucination in World Models is Predictable and Preventable](https://arxiv.org/abs/2606.27326v1)

**作者**：Nicklas Hansen, Xiaolong Wang  
**分类**：cs.LG, cs.CV, cs.RO  
**发布时间**：2026-06-25

### 📄 论文摘要

Modern generative world models render increasingly realistic action-controllable futures, yet they frequently hallucinate: rollouts remain visually fluent while drifting from the ground-truth dynamics. We hypothesize that hallucination concentrates in low-coverage regions of the state-action space, where lightweight data-centric signals can both detect it and guide mitigation. To test this, we introduce MMBench2, a 427-hour, 210-task dataset for visual world modeling with ground-truth actions, rewards, and live simulators, and train a 350M-parameter world model on it. We identify three distinct hallucination modes: perceptual, action-marginalized, and scene-diverging -- each anchored to a different stage of the pipeline, and develop three signals that accurately predict where the model will fail. To close coverage gaps at training time, we develop a coverage-aware sampling technique; to close them online, our hallucination predictors serve as curiosity rewards for targeted data collection, yielding a data-efficient finetuning recipe that adapts the pretrained world model to entirely unseen environments with as few as 50 real environment trajectories. Overall, our findings reveal that hallucination in world models is inherently a data coverage issue, and that the same signals used to detect it can also be used for mitigation.   An interactive web version of our paper is available at https://www.nicklashansen.com/mmbench2

### 🤖 AI 总结

**一句话总结**：Modern generative world models render increasingly realistic action-controllable futures, yet they frequently hallucinate: rollouts remain visually fluent while drifting from the ground-truth dynamics...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hallucination, World, Models, Predictable, Preventable, Modern, generative, render

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27326v1) | [下载PDF](https://arxiv.org/pdf/2606.27326v1.pdf)

---

## [25. Beyond the Hard Budget: Sparsity Regularizers for More Interpretable Top-k Sparse Autoencoders](https://arxiv.org/abs/2606.27321v1)

**作者**：Nathanaël Jacquier, Maria Vakalopoulou, Mahdi S. Hosseini  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-25

### 📄 论文摘要

Sparse autoencoders (SAEs) have become a leading tool for interpreting the representations of vision foundation models, decomposing their polysemantic activations into a larger set of sparse, more monosemantic features. The Top-$k$ SAE, a now-standard variant, enforces sparsity architecturally through its activation function, retaining only the $k$ most active latents per input. Because it was designed precisely to avoid the $\ell_1$ penalty used by earlier SAEs and its known drawbacks, it has not been combined with an explicit sparsity regularizer, despite retaining limitations of its own, such as a budget $k$ that is fixed regardless of input complexity and a tendency to overfit to the training value of $k$. We introduce two sparsity regularizers compatible with the Top-$k$ architecture, both acting on the activations before the Top-$k$ selection: an $\ell_1$ penalty on the unselected (off-support) units, and a scale-invariant $\ell_1/\ell_2$-ratio penalty that concentrates the code onto fewer effective units. Both penalties are applied only to the batch-active units, those selected by the Top-$k$ operator at least once within the batch. Across two datasets, three vision foundation models, and a range of $k$, both regularizers consistently improve monosemanticity at no cost to reconstruction quality. The $\ell_1/\ell_2$ penalty further concentrates information into fewer latents, making reconstruction more robust to the inference-time choice of $k$ and improving small-budget linear probing. Our central finding is that hard architectural sparsity and soft sparsity regularization are complementary rather than mutually exclusive.

### 🤖 AI 总结

**一句话总结**：Sparse autoencoders (SAEs) have become a leading tool for interpreting the representations of vision foundation models, decomposing their polysemantic activations into a larger set of sparse, more mon...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Hard, Budget, Sparsity, Regularizers, More, Interpretable, Top-k

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27321v1) | [下载PDF](https://arxiv.org/pdf/2606.27321v1.pdf)

---

## [26. Blackwell Approachability and Gradient Equilibrium are Equivalent](https://arxiv.org/abs/2606.27315v1)

**作者**：Brian W. Lee, Nika Haghtalab, Michael I. Jordan 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-25

### 📄 论文摘要

Gradient equilibrium (GEQ) is a recently introduced online optimization framework that generalizes first-order stationarity from offline optimization and abstracts problems like online conformal prediction. While GEQ has curious similarities with known online learning frameworks, namely regret minimization, prior work has shown that GEQ error and regret are incomparable objectives, leaving open a precise understanding of how GEQ fits into the broader online learning landscape. In this work, we show that GEQ is equivalent to Blackwell approachability in the algorithmic sense. That is, a Blackwell approachability problem can always be solved using queries to a black-box GEQ oracle, with no asymptotic loss in the oracle's error rate, and vice versa. Taken together with known equivalences between approachability, regret minimization, and calibration, these results imply that GEQ is equivalent to these frameworks, as well. Our reductions are efficient and can be used to transfer refined guarantees, such as optimism and strong adaptivity, from regret minimization to GEQ. Along the way, we also identify necessary and sufficient conditions for GEQ, and establish reductions between different notions of GEQ with unconstrained and constrained decision sets.

### 🤖 AI 总结

**一句话总结**：Gradient equilibrium (GEQ) is a recently introduced online optimization framework that generalizes first-order stationarity from offline optimization and abstracts problems like online conformal predi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Blackwell, Approachability, Gradient, Equilibrium, Equivalent, GEQ, recently, introduced

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27315v1) | [下载PDF](https://arxiv.org/pdf/2606.27315v1.pdf)

---

## [27. A Multi-Fidelity Convolutional Autoencoder-Transfer Learning Framework for Guided-Wave-Based Damage Diagnosis Using Large Simulated and Limited Experimental Datasets](https://arxiv.org/abs/2606.27304v1)

**作者**：Santosh Kapuria, Abhishek  
**分类**：cs.LG  
**发布时间**：2026-06-25

### 📄 论文摘要

Guided wave-based structural health monitoring (GWSHM) with onboard transducers offers significant potential for the early diagnosis of damage in engineering structures. However, the practical deployment of deep learning models is often hindered by the limited availability of labelled experimental data and the high computational cost of generating large-scale high-fidelity simulation datasets. This study presents a multifidelity transfer learning framework that integrates lightweight physics-based simulations, convolutional autoencoder (CAE)-based deep feature learning, a feed-forward neural network, and limited experimental measurements for accurate damage localisation and sizing in plate-like structures instrumented with piezoelectric transducers. A computationally efficient one-dimensional time-domain spectral element model is employed to generate a large synthetic dataset for pretraining, while transfer learning adapts the model to experimental domains using only a small amount of labelled data. The CAE-based transfer learning framework significantly outperforms its CNN-based counterpart in damage localisation accuracy. The model achieves excellent predictive performance with $R^2$ scores exceeding 0.93 for damage localisation and 0.99 for damage sizing. Its generalisation capability is demonstrated on previously unseen data, showing high prediction accuracy for damage scenarios not represented during pretraining or fine-tuning. The results establish the proposed framework as an accurate, computationally efficient, and practically viable solution for real-world GWSHM applications.

### 🤖 AI 总结

**一句话总结**：Guided wave-based structural health monitoring (GWSHM) with onboard transducers offers significant potential for the early diagnosis of damage in engineering structures. However, the practical deploym...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Fidelity, Convolutional, Autoencoder-Transfer, Learning, Framework, Guided-Wave-Based, Damage, Diagnosis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27304v1) | [下载PDF](https://arxiv.org/pdf/2606.27304v1.pdf)

---

## [28. Designing Reward Signals for Portable Query Generation: A Case Study in Industrial Semantic Job Search](https://arxiv.org/abs/2606.27291v1)

**作者**：Ping Liu, Qianqi Shen, Jianqiang Shen 等 14 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-25

### 📄 论文摘要

Job-search platforms rely on low-bandwidth query interfaces that often fail to capture the high-dimensional complexity of candidate profiles. We present an end-to-end RLAIF (Reinforcement Learning from AI Feedback) framework to generate \emph{portable} job search queries, terms that abstract away seeker-specific identifiers while preserving generalizable qualifications. This task introduces a highly adversarial reward surface where policy optimization frequently exploits flaws in LLM-as-judge rubrics, resulting in degenerate verbatim-copying behaviors.   We conducted comprehensive empirical experiments to isolate the impact of optimization mechanics against structured reward engineering. Our results demonstrate that for critic-free optimizers, performance is overwhelmingly dictated by robust reward shaping, rendering the specific choice of algorithm largely immaterial. While critic-free per-rollout baseline methods (RLOO and REINFORCE++) natively resist reward-hacking, the group-relative advantage normalization in GRPO appears uniquely sensitive to spurious reward signals, making it disproportionately susceptible to exploitation. We show that introducing a deterministic, rule-based reward floor to correct for rewards assigned to verbatim copying mitigates this failure mode, resulting in a substantial $+0.147$ quality improvement on a cross-family evaluation judge. Ultimately, we show that the training-time reward model inflates performance gains by $2.4\times$, confirming that the training success is fundamentally dependent on enforcing reward-shaping disciplines rather than selecting alternative optimizers.

### 🤖 AI 总结

**一句话总结**：Job-search platforms rely on low-bandwidth query interfaces that often fail to capture the high-dimensional complexity of candidate profiles. We present an end-to-end RLAIF (Reinforcement Learning fro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Designing, Reward, Signals, Portable, Query, Generation, Case, Study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27291v1) | [下载PDF](https://arxiv.org/pdf/2606.27291v1.pdf)

---

## [29. Recovering Governing Equations from Solution Data: Identifiability Bounds for Linear and Nonlinear ODEs](https://arxiv.org/abs/2606.27285v1)

**作者**：Yang Pan, Helmut Bölcskei  
**分类**：cs.LG, cs.IT, math.CA, math.DS  
**发布时间**：2026-06-25

### 📄 论文摘要

Learning governing equations from observed solution data is a fundamental challenge in scientific machine learning \cite{bruntonDiscoveringGoverningEquations2016,kovachkiNeuralOperatorLearning2023,longPDENetLearningPDEs2018,rudyDatadrivenDiscoveryPartial2017,raonicConvolutionalNeuralOperators2023}, yet the theoretical conditions under which a ground-truth ODE can be uniquely and stably identified from multiple solution observations remain largely undeveloped, and no quantitative analysis of the sample complexity of such learning tasks exists in the literature. To address this gap, we introduce the Hausdorff distance on solution sets as the natural metric for comparing differential equations, since it captures the worst-case separation between two equations over all admissible initial conditions and thus encodes the minimax structure of the identification problem. We establish identifiability bounds for governing ODEs across a wide class of structure equations--ranging from linear ODEs to nonlinear classes with Lipschitz (Hölder)-continuous vector fields--characterizing precisely when two distinct equations can be distinguished from solution data. Using this metric, we derive metric entropy estimates for the relevant ODE classes and analyze sample complexity bounds, quantifying how many solution observations are needed to reliably recover the governing equation.

### 🤖 AI 总结

**一句话总结**：Learning governing equations from observed solution data is a fundamental challenge in scientific machine learning \cite{bruntonDiscoveringGoverningEquations2016,kovachkiNeuralOperatorLearning2023,lon...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Recovering, Governing, Equations, Solution, Data, Identifiability, Bounds, Linear

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27285v1) | [下载PDF](https://arxiv.org/pdf/2606.27285v1.pdf)

---

## [30. How Good Can Linear Models Be for Time-Series Forecasting?](https://arxiv.org/abs/2606.27282v1)

**作者**：Lang Huang, Jinglue Xu, Luke Darlow  
**分类**：cs.LG  
**发布时间**：2026-06-25

### 📄 论文摘要

Time-series forecasting research has been moving steadily toward larger architectures, from specialized transformers to general-purpose foundation models, on the assumption that capacity is what unlocks accuracy. We take the opposite position: most of the gap can be closed at far lower cost by tuning preprocessing rather than scaling models. We use Ridge regression as the testbed, since it has a closed-form solution and interpretable weights, which let the optimal hyperparameters be read off the search directly. We search over context length, local normalization, regularization, and augmentation on eight standard benchmarks and find three patterns. (1) Optimal lookback is strongly series-specific and often non-monotonic in forecast horizon, with fitted power-law exponents ranging from $+0.46$ on ETTm2 to $-0.19$ on Exchange and Traffic, challenging the convention that longer horizons need longer history. (2) Normalizing over a learned trailing fraction of the context, rather than its entirety, is almost universally preferred. (3) Series within the same dataset often disagree on hyperparameters; the optimal degree of cross-series sharing varies from fully shared to fully per-series. The resulting models beat prior linear forecasters on most dataset-horizon entries and exceed Transformer, MLP, and CNN baselines on six of eight benchmarks. The optimized hyperparameters also serve as a diagnostic on the data itself, revealing structures that larger models absorb silently into their learned parameters.

### 🤖 AI 总结

**一句话总结**：Time-series forecasting research has been moving steadily toward larger architectures, from specialized transformers to general-purpose foundation models, on the assumption that capacity is what unloc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Be, How, Good, Can, Linear, Models, Time-Series, Forecasting?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.27282v1) | [下载PDF](https://arxiv.org/pdf/2606.27282v1.pdf)

---

