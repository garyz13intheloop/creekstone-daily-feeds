# arXiv AI 论文日报 | 2026-07-01

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (6 篇)
- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (9 篇)
- [cs.AI](#csAI) (4 篇)

---

## cs.AI

## [1. AxDafny: Agentic Verified Code Generation in Dafny](https://arxiv.org/abs/2606.32007v1)

**作者**：Benjamin Breen, Austin Letson, Borja Requena Pozo 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-06-30

### 📄 论文摘要

We study agentic code generation in Dafny, where a model must generate both executable code and the proof artifacts for verification. We present AxDafny, a verifier-guided repair framework that iteratively generates implementations, invariants, assertions, and termination arguments. We also introduce LiveCodeBench-Pro-Dafny (LCB-Pro-Dafny), a benchmark of 250 competition-style programming problems translated into Dafny with formal specifications and a verifier-based evaluation harness. On LCB-Pro-Dafny, AxDafny substantially improves verification success over baseline GPT-5.5 performance. On DafnyBench, AxDafny achieves 92.7\% verification success, outperforming the strongest previously reported proof-hint baseline by 6.5 percentage points. Lastly, we show that verification success and runtime test performance measure different aspects of generated code.

### 🤖 AI 总结

**一句话总结**：We study agentic code generation in Dafny, where a model must generate both executable code and the proof artifacts for verification. We present AxDafny, a verifier-guided repair framework that iterat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, AxDafny, Agentic, Verified, Code, Generation, Dafny, study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32007v1) | [下载PDF](https://arxiv.org/pdf/2606.32007v1.pdf)

---

## [2. PolicyGuard: From Organizational Policies to Neuro-SymbolicCompliance Review Engines](https://arxiv.org/abs/2606.32004v1)

**作者**：Sameer Malik, Ayush Singh, Amar Prakash Azad  
**分类**：cs.AI, cs.LG, cs.LO, cs.SC  
**发布时间**：2026-06-30

### 📄 论文摘要

Policy-grounded document review requires determining whether a target document complies with organization-specific policies, guidelines, or playbooks. While large language models can assist with policy interpretation and document analysis, end-to-end prompting leaves the applied policy logic implicit, making compliance decisions difficult to inspect, update, and test. We present PolicyGuard, a neuro-symbolic framework for policy-grounded document compliance review. PolicyGuard converts organizational policy guidance into an executable review engine consisting of typed relational logic rules and atom-level extraction questions. During review, LLMs answer these local questions using retrieved document evidence, and a symbolic evaluator applies the formal rules to detect non-compliance. We instantiate and evaluate PolicyGuard on company-specific NDA compliance review, where contract clauses must be checked against organization-specific negotiation policies. By separating policy formalization, local document interpretation, and symbolic compliance evaluation, PolicyGuard makes document review more explicit, maintainable, and systematically testable.

### 🤖 AI 总结

**一句话总结**：Policy-grounded document review requires determining whether a target document complies with organization-specific policies, guidelines, or playbooks. While large language models can assist with polic...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PolicyGuard, Organizational, Policies, Neuro-SymbolicCompliance, Review, Engines, Policy-grounded, document

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32004v1) | [下载PDF](https://arxiv.org/pdf/2606.32004v1.pdf)

---

## [3. Self-Study Reconsidered: The Hidden Fragility of Learning from Self-Generated QA](https://arxiv.org/abs/2606.32002v1)

**作者**：Ekaterina Alimaskina, Denis Shveykin, Gleb Molodtsov 等 6 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-06-30

### 📄 论文摘要

Language models are increasingly taught from synthetic question--answer (QA) supervision: a model generates questions about a document, answers them from the same text, and the resulting pairs are used to fine-tune, distill, or compress knowledge into another model. We show that this generation step is not neutral preprocessing. It is an implicit policy that both selects which evidence becomes training signal and decides how that evidence is answered, and it is fragile at both stages. When choosing what to ask, generators do not scan a document uniformly. Coverage saturates early and concentrates on salient spans, diverse prompts converge on the same regions, and what looks question-worthy is driven by local presentation. As a result, salient artifacts such as poorly cleaned markup can hijack question generation across model families and scales. When answering, the model that produces the supervision tends to obey instruction-like passages embedded in the text. This compliance depends on the intent and surface form of the passage rather than its strictness, and is worst under task conflict, where larger models comply more often. These failure modes arise from choices made during QA generation, so they can be reduced without changing the training loop. Tying each question to a fixed target reduces biased selection, and filtering instruction-like spans before answering lowers mean injection compliance from $88\%$ to $13\%$ in our evaluation while retaining nearly all clean text.

### 🤖 AI 总结

**一句话总结**：Language models are increasingly taught from synthetic question--answer (QA) supervision: a model generates questions about a document, answers them from the same text, and the resulting pairs are use...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, QA, Self-Study, Reconsidered, Hidden, Fragility, Learning, Self-Generated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32002v1) | [下载PDF](https://arxiv.org/pdf/2606.32002v1.pdf)

---

## [4. TreeAgent: A Generalizable Multi-Agent Framework for Automated Bias Labeling in Forestry via Compiled Expert Rules and Vision-Language Models](https://arxiv.org/abs/2606.31976v1)

**作者**：Shiyi Chen, Nicholas Saban, Collin Hargreaves 等 4 位作者  
**分类**：cs.AI, cs.MA  
**发布时间**：2026-06-30

### 📄 论文摘要

Human-labeled data are widely used as reference annotations in ML, despite known variability across annotators in many expert-driven domains. In addition, expert annotation is slow, inconsistent, and remains a major bottleneck for scaling tasks like tree height bias classification in forestry remote sensing. We propose a multi-agent system (MAS) that orchestrates expert decision trees with Vision-Language Models (VLMs), treating the decision tree as a structural prior while VLMs perform localized semantic perception at individual nodes, with multi-agent voting to mitigate VLM stochasticity. We formalize a Decoupled Declarative Decision (D3) Framework that enables zero-modification generalization across diverse expert-defined decision structures. On a tree bias classification testbed, our framework outperforms supervised ML baselines and reduces the amount of expert labeling effort required. These results suggest that agentic orchestration of VLMs with expert priors can reproduce expert-defined labeling procedures at substantially lower annotation cost while maintaining interpretability.

### 🤖 AI 总结

**一句话总结**：Human-labeled data are widely used as reference annotations in ML, despite known variability across annotators in many expert-driven domains. In addition, expert annotation is slow, inconsistent, and ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, TreeAgent, Generalizable, Framework, Automated, Bias, Labeling, Forestry

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.31976v1) | [下载PDF](https://arxiv.org/pdf/2606.31976v1.pdf)

---

## cs.CL

## [5. Introspective Coupling: Self-Explanation Training Tracks Behavioral Change Despite Fixed Supervision](https://arxiv.org/abs/2606.32038v1)

**作者**：Zifan Carl Guo, Laura Ruis, Jacob Andreas 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-06-30

### 📄 论文摘要

When does training language models (LMs) to generate explanations of their predictions yield faithful introspection, rather than superficial imitation? We study LMs trained to explain which features of their inputs influenced their behavior, using models' counterfactual behavior on modified inputs as supervision. Surprisingly, we find that LMs trained on fixed counterfactual explanations derived from earlier checkpoints of themselves, or even from behaviorally similar models in different families, frequently produce explanations more faithful to their own current behaviors than to those of their training targets. This "introspective" coupling between LM explanations and behaviors occurs when training explanations remain sufficiently correlated with current behaviors over the course of training, even as behaviors themselves shift. We also show that introspective coupling tracks behavior shifts: when explanation training is provided concurrently with other post-training objectives, explanations track those shifts without requiring updated supervision. This phenomenon appears in multiple tasks, including sycophancy and refusal, and is robust to label noise. Overall, our results show that even fixed datasets of counterfactual explanations can provide scalable and generalizable post-training signal for introspection.

### 🤖 AI 总结

**一句话总结**：When does training language models (LMs) to generate explanations of their predictions yield faithful introspection, rather than superficial imitation? We study LMs trained to explain which features o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Introspective, Coupling, Self-Explanation, Training, Tracks, Behavioral, Change, Despite

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32038v1) | [下载PDF](https://arxiv.org/pdf/2606.32038v1.pdf)

---

## [6. Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs](https://arxiv.org/abs/2606.32032v1)

**作者**：Gabrielle Kaili-May Liu, Avi Caciularu, Gal Yona 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-30

### 📄 论文摘要

Metacognition is a critical component of intelligence that describes the ability to monitor and regulate one's own cognitive processes. Yet LLMs exhibit systemic deficiencies in key metacognitive faculties: they hallucinate with high confidence, fail to recognize knowledge boundaries, and misrepresent their internal uncertainty--undermining trustworthiness and reliability. Since monitoring task performance and adapting behavior accordingly are central to metacognition, we posit that models capable of accurately judging their own performance are better positioned to improve it. We operationalize this idea via two novel mechanisms: reinforcement learning with metacognitive feedback (RLMF), a paradigm to refine completion rankings during preference optimization based on the quality of a model's self-judgments of performance, and metacognitive data selection, which uses similar self-judgments to identify high-value training examples, outperforming naive active learning. We apply these innovations to the problem of faithful calibration (FC), a task that is itself fundamentally metacognitive: the goal is to align expressed with intrinsic uncertainty, difficult even for frontier LLMs. We adopt a two-stage, decoupled approach, first using these methods to calibrate the faithfulness of models' self-reported confidence scores, then mapping to natural, context-adaptable linguistic uncertainty via targeted output editing. Extensive experiments show RLMF achieves generalizable, state-of-the-art FC on diverse tasks while preserving accuracy. Further, RLMF surpasses standard RL by up to 63% while enhancing models' ability to assess and express their own capability limits. This positions RLMF as a promising paradigm to enhance LLM metacognition toward improved abilities and alignment, and suggests metacognitive performance as an effective RL signal to overcome limits of prior intrinsic feedback methods.

### 🤖 AI 总结

**一句话总结**：Metacognition is a critical component of intelligence that describes the ability to monitor and regulate one's own cognitive processes. Yet LLMs exhibit systemic deficiencies in key metacognitive facu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Reinforcement, Learning, Metacognitive, Feedback, Elicits, Faithful, Uncertainty, Expression

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32032v1) | [下载PDF](https://arxiv.org/pdf/2606.32032v1.pdf)

---

## [7. When LLMs Read Tables Carelessly: Measuring and Reducing Data Referencing Errors](https://arxiv.org/abs/2606.32029v1)

**作者**：Yuqing Yang, Qi Zhu, Zhen Han 等 8 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-30

### 📄 论文摘要

While large language models (LLMs) perform well on table tasks, they still make data referencing errors (DREs), i.e., incorrectly citing or omitting table values, despite understanding the table structure. Beyond final-answer accuracy, DREs directly compromise the correctness and reliability of intermediate reasoning steps. Yet prior studies have only offered limited, small-scale analyses. In this work, we present the first systematic evaluation of tabular data referencing errors across different models and tasks. Our results show that DREs occur across all tested models (1.7B to 20B parameters). Furthermore, we demonstrate that incorporating data referencing as a critic significantly improves answer accuracy up to 12.0%, through critic-based filtering and rejection sampling. Finally, we trained a lightweight 4B-parameter critic model that achieves an average F1 score of 78.2% in detecting both in-distribution and out-of-distribution DREs, and effectively assists inference for larger models.

### 🤖 AI 总结

**一句话总结**：While large language models (LLMs) perform well on table tasks, they still make data referencing errors (DREs), i.e., incorrectly citing or omitting table values, despite understanding the table struc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, When, Read, Tables, Carelessly, Measuring, Reducing, Data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32029v1) | [下载PDF](https://arxiv.org/pdf/2606.32029v1.pdf)

---

## [8. Scalable Behaviour Cloning on Browser Using via Skill Distillation](https://arxiv.org/abs/2606.32014v1)

**作者**：Kaisen Yang, Zheng Jiang, Yuzhao Peng 等 14 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-30

### 📄 论文摘要

Internet users collectively perform an enormous range of skilled work through web browsers, from software development and document editing to search, forms, and enterprise workflows, making human browsing a highly scalable but under-exploited source of reusable browser skills. We argue that the bottleneck for browser agents is decision-making under incomplete information rather than low-level operation, and that the priors agents lack are already implicit in human interaction traces. We therefore study scalable behavior cloning for browser agents via skill distillation, converting user interaction trajectories into compact natural-language skills that agents can read, retrieve, reuse, and compose directly. We further organize the distilled skills into a skill graph so that growth proceeds through consolidation rather than unbounded accumulation. This suggests that the scalability of browser agents may come less from manually designed tasks and more from the collective skills already expressed by internet users. Our project is available at: https://lab.einsia.ai/browserbc/.

### 🤖 AI 总结

**一句话总结**：Internet users collectively perform an enormous range of skilled work through web browsers, from software development and document editing to search, forms, and enterprise workflows, making human brow...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Scalable, Behaviour, Cloning, Browser, via, Skill, Distillation, Internet

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32014v1) | [下载PDF](https://arxiv.org/pdf/2606.32014v1.pdf)

---

## [9. DigitalCoach: Communication and Grounding Gaps in Human and Agentic Computer Use Coaching](https://arxiv.org/abs/2606.31980v1)

**作者**：Meng Chen, Anya Ji, Tsung-Han Wu 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-30

### 📄 论文摘要

Agents are increasingly capable of automating software tasks, but can they teach humans how to use software themselves? We introduce DigitalCoach, a multimodal dataset of 72 human expert-novice computer use coaching sessions consisting of 22,752 dialogue turns grounded in 28.1 hours of screen and input event recordings across five software applications. We use DigitalCoach to evaluate whether state-of-the-art models can teach humans how to use computers. Automated evaluation shows that models differ from humans in how they coach: models provide more direct instructions, but fewer explanations, error diagnoses, and knowledge-check questions. When we fix the coaching method, models produce utterances similar to human references yet poorly grounded in visual context. Interactive evaluation confirms that model coaches cause learners to passively follow instructions without deeper engagement and fall short in visual grounding. DigitalCoach lays a foundation for collaborative and proactive computer use coaching agents.

### 🤖 AI 总结

**一句话总结**：Agents are increasingly capable of automating software tasks, but can they teach humans how to use software themselves? We introduce DigitalCoach, a multimodal dataset of 72 human expert-novice comput...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DigitalCoach, Communication, Grounding, Gaps, Human, Agentic, Computer, Use

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.31980v1) | [下载PDF](https://arxiv.org/pdf/2606.31980v1.pdf)

---

## [10. LuxEmo: Expressive Text-to-Speech Corpus for Luxembourgish](https://arxiv.org/abs/2606.31947v1)

**作者**：Nina Hosseini-Kivanani, Sandipana Dowerah  
**分类**：cs.CL  
**发布时间**：2026-06-30

### 📄 论文摘要

State-of-the-art speech datasets predominantly focus on widely spoken languages, often overlooking low-resource languages such as Luxembourgish, which remain underrepresented in speech technology research. In this work, we introduce LuxEmo, a 21-hour conversational expressive speech corpus for Luxembourgish with 4 emotion categories. LuxEmo is derived from Radio Télévision Luxembourg (RTL) youth broadcasts, using automated detection followed by human validation. We propose a semi-automatic curation workflow combining voice activity detection, denoising, language identification, LuxASR-based segmentation, automatic emotion prediction, lexical cues, and targeted human review. Additionally, we benchmark five expressive TTS systems covering German-based cross-lingual transfer, multilingual Luxembourgish support, Luxembourgish adaptation, and non-parametric prosody transfer. Performance is evaluated using both objective metrics and human evaluation.

### 🤖 AI 总结

**一句话总结**：State-of-the-art speech datasets predominantly focus on widely spoken languages, often overlooking low-resource languages such as Luxembourgish, which remain underrepresented in speech technology rese...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LuxEmo, Expressive, Text-to-Speech, Corpus, Luxembourgish, State-of-the-art, speech, datasets

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.31947v1) | [下载PDF](https://arxiv.org/pdf/2606.31947v1.pdf)

---

## cs.CV

## [11. PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)

**作者**：Yujie Guo, Yudong Jin, Lingteng Qiu 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-30

### 📄 论文摘要

Producing 3D human representations from input views on the fly is essential for immersive live streaming systems, where representation compactness is as critical as high fidelity given limited computational power and transmission bandwidth. Although recent feed-forward reconstruction methods achieve impressive quality through the view-centric prediction of 3D representations, they repeatedly encode the same subject content across multiple views, leading to significant inter-view redundancy. Our key insight is to perform predictions directly in 3D space, enabling the network to learn and produce a highly compact representation. To this end, we propose PointSplat, a novel human-centric approach that directly infers Gaussian primitives from an input point set. The proposed method first estimates a coarse geometric proxy and performs ray casting to prune redundant points and establish explicit 2D--3D correspondences. Subsequently, it employs a Point-Image Transformer to fuse appearance and geometry features, predicting Gaussian attributes in a single forward pass. This design restricts predictions to foreground regions of interest, substantially reducing the total number of Gaussians while improving novel-view rendering quality. Extensive experiments demonstrate that PointSplat achieves higher efficiency and quality while exhibiting strong robustness to variations in view count and image resolution across multiple datasets.

### 🤖 AI 总结

**一句话总结**：Producing 3D human representations from input views on the fly is essential for immersive live streaming systems, where representation compactness is as critical as high fidelity given limited computa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PointSplat, Compact, Gaussian, Splatting, via, Human-Centric, Prediction, Producing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32036v1) | [下载PDF](https://arxiv.org/pdf/2606.32036v1.pdf)

---

## [12. SpheRoPE: Zero-Shot Optimization-Free 360 Panorama Generation with Spherical RoPE](https://arxiv.org/abs/2606.32033v1)

**作者**：Or Hirschorn, Aaron Olender, Eli Alshan 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-30

### 📄 论文摘要

We present a zero-shot, training-free and optimization-free framework for generating 360 panoramic images and videos by directly injecting spherical priors into pre-trained diffusion transformers. Existing methods either rely on costly fine-tuning on scarce panoramic data that limits generalization, or leverage multi-step optimization that incurs prohibitive inference latency. We observe that contemporary generative models natively exhibit some panoramic priors from large-scale training. However, these emergent capabilities are insufficient, as the models fundamentally fail to satisfy the rigorous topological constraints imposed by equirectangular projection (ERP). We introduce a zero-shot and optimization-free approach that resolves these constraints at inference time. Spherical RoPE replaces standard rotary position embeddings: low-frequency channels are re-parameterized as 3D Cartesian coordinates to natively encode the spherical manifold, while high-frequency channels are harmonically quantized to enforce exact periodicity. Coupled with complementary Semantic Distortion classifier-free guidance (CFG) that explicitly steers geometry, we avoid retraining and inherit the full creative breadth of state-of-the-art models. Our approach generalizes across diverse backbones and 360 generation modalities. We demonstrate this across text-to-panorama using Flux.1, Flux.2, and LTX-Video backbones, achieving competitive performance against baselines, all while remaining training-free. Project page: https://orhir.github.io/SpheRoPE

### 🤖 AI 总结

**一句话总结**：We present a zero-shot, training-free and optimization-free framework for generating 360 panoramic images and videos by directly injecting spherical priors into pre-trained diffusion transformers. Exi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, SpheRoPE, Zero-Shot, Optimization-Free, Panorama, Generation, Spherical, RoPE

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32033v1) | [下载PDF](https://arxiv.org/pdf/2606.32033v1.pdf)

---

## [13. FLORA: A deep learning approach to predict forest attributes from heterogeneous LiDAR data](https://arxiv.org/abs/2606.32023v1)

**作者**：Emilie Vautier, Clément Mallet, Cédric Vega  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-30

### 📄 论文摘要

Forest attributes are essential for national-scale resource monitoring. Airborne LiDAR metrics are among the auxiliary variables most strongly correlated with forest attributes used in National Forest Inventory (NFI) estimates. However, producing wall-to-wall predictions remains challenging when LiDAR data are acquired under heterogeneous conditions. As national LiDAR programs expand across Europe, variability in sensors, flight parameters, seasons, and scan angles limits the robustness of existing models, which are often calibrated for local conditions. We present FLORA (Forest LiDAR Octree Regression with Auxiliary Data), a deep learning framework that predicts six forest attributes: dominant height, total volume, deciduous volume, coniferous volume, basal area, and stem density from heterogeneous LiDAR point clouds. FLORA combines an octree-based backbone with ecological and spatiotemporal auxiliary variables through a late-fusion gating mechanism. Models are trained and evaluated on 32,052 National Forest Inventory plots across mainland France using data from the French LiDAR HD program. A single model trained on both leaf-on and leaf-off acquisitions outperforms season-specific models and improves cross-season robustness. Auxiliary variables provide modest overall gains but contribute more strongly to species-specific volume prediction. FLORA achieves an rRMSE of about 12.3% (R2 = 0.88) for dominant height and 39% (R2 = 0.74) for total volume, providing a robust baseline for large-scale forest attribute estimation from heterogeneous national LiDAR programs.

### 🤖 AI 总结

**一句话总结**：Forest attributes are essential for national-scale resource monitoring. Airborne LiDAR metrics are among the auxiliary variables most strongly correlated with forest attributes used in National Forest...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FLORA, deep, learning, approach, predict, forest, attributes, heterogeneous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32023v1) | [下载PDF](https://arxiv.org/pdf/2606.32023v1.pdf)

---

## [14. Cross-Space Distillation: Teaching One-Step Students with Modern Diffusion Teachers](https://arxiv.org/abs/2606.32020v1)

**作者**：Anh Nguyen, Ngan Nguyen, Duc Vu 等 14 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-30

### 📄 论文摘要

Modern one-step diffusion models achieve impressive quality through distribution-based timestep distillation. Yet, they rely on a critical assumption: Teacher and Student must inhabit the same latent space. This Shared-Space constraint prevents knowledge transfer from modern high-capacity Teachers (e.g., SD 3.5 and Flux) into compact, deployment-friendly Students such as SD 1.5, whose latent resolution and VAE parameterization differ from the Teacher. We formalize this overlooked regime as Cross-Space Distillation, where Teacher and Student differ in both latent resolution and VAE space. To enable distillation under this mismatch, we introduce the Bridge, a lightweight latent interface that maps Student latents into the Teacher space without modifying the Student backbone. Bridge combines a frozen Student VAE decoder as a spatial prior with a compact learnable projector, and is trained with latent reconstruction and attention fidelity objectives for stable Teacher-space alignment. Across diverse modern Teachers, Bridge enables substantial gains for compact one-step Students; for example, it improves SD 1.5 from 5.4 to 9.4 HPSv3 while preserving one-step inference, low latency, and broad ecosystem compatibility. These results show that heterogeneous large Teachers can be distilled into efficient, deployable backbones through a lightweight latent-space interface.

### 🤖 AI 总结

**一句话总结**：Modern one-step diffusion models achieve impressive quality through distribution-based timestep distillation. Yet, they rely on a critical assumption: Teacher and Student must inhabit the same latent ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Cross-Space, Distillation, Teaching, One-Step, Students, Modern, Teachers

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32020v1) | [下载PDF](https://arxiv.org/pdf/2606.32020v1.pdf)

---

## [15. Automated Background Swapping for Robustness against Spurious Backgrounds](https://arxiv.org/abs/2606.32018v1)

**作者**：Cesar Roder, Kajetan Schweighofer  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-06-30

### 📄 论文摘要

Classifiers based on Deep Neural Networks exhibit strong performance across domains, yet can fail catastrophically if they rely on spurious correlations, i.e., features that are predictive of the target label in the training data but are not causally linked and thus fail to generalize. For the vision domain, many such spurious correlations manifest themselves within the background of the image, where only the foreground is predictive of the class label. In this paper, we introduce Automated Background Swapping (AutoBackSwap) to reduce the reliance of classifiers on such spurious backgrounds. AutoBackSwap uses a secondary network to disentangle the foreground and background, followed by infilling to synthesize complete backgrounds, and finally combines different foregrounds and inpainted backgrounds to augment the training data. We find that patch-wise labeling of just a few hundred samples suffices to train the secondary network and automatically augment the full training dataset on challenging image classification tasks. In contrast to many previous methods, AutoBackSwap proves very effective even if there is not a single sample in the training data breaking the spurious correlation. Across a range of image classification tasks with spurious backgrounds, AutoBackSwap consistently outperforms prior methods.

### 🤖 AI 总结

**一句话总结**：Classifiers based on Deep Neural Networks exhibit strong performance across domains, yet can fail catastrophically if they rely on spurious correlations, i.e., features that are predictive of the targ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Automated, Background, Swapping, Robustness, against, Spurious, Backgrounds, Classifiers

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32018v1) | [下载PDF](https://arxiv.org/pdf/2606.32018v1.pdf)

---

## [16. LUNA: Learning Universal 3D Human Animation Beyond Skinning](https://arxiv.org/abs/2606.31981v1)

**作者**：Peng Li, Rawal Khirodkar, Junxuan Li 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-30

### 📄 论文摘要

Creating photorealistic, animatable 3D human avatars from monocular images still largely depends on Linear Blend Skinning (LBS) and parametric body models, which constrain expressivity and often introduce artifacts due to imperfect fitting. We propose LUNA, an LBS-free universal neural animation model that directly maps multiple 2D controls like images, keypoints, sketches, and unseen characters into 3D Gaussian deformations, bypassing explicit body fitting. At its core, a transformer-based motion regressor disentangles global rigid motion from fine-grained local dynamics to capture both coherent movement and subtle non-rigid effects. To resolve the inherent ambiguity of 2D-to-3D lifting while scaling beyond fitted datasets, we introduce hybrid supervision that distills soft structural priors from an LBS teacher and a loss that supports training on both limited fitted data and large in-the-wild unlabeled videos. Extensive experiments show LUNA achieves competitive visual fidelity compared to LBS-based approaches, while delivering realistic human motion and zero-shot cross-identity generalization across diverse driving modalities. To the best of our knowledge, LUNA is the first end-to-end 3D animatable model that supports implicit 2D driving.

### 🤖 AI 总结

**一句话总结**：Creating photorealistic, animatable 3D human avatars from monocular images still largely depends on Linear Blend Skinning (LBS) and parametric body models, which constrain expressivity and often intro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, LUNA, Learning, Universal, Human, Animation, Beyond, Skinning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.31981v1) | [下载PDF](https://arxiv.org/pdf/2606.31981v1.pdf)

---

## [17. Planar-SfM: Camera Pose Estimation via Homography Graph Embeddings](https://arxiv.org/abs/2606.31979v1)

**作者**：Gabi Pragier, Matan Karklinsky, David Ungarish 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-30

### 📄 论文摘要

Structure from Motion (SfM) systems traditionally struggle with planar scenes, where standard epipolar geometry-based methods become degenerate. Rather than viewing planar surfaces as a limitation, we propose a unified framework that leverages them as a source of geometric constraints. Our key insight is that each planar surface visible across multiple views provides an independent estimate of relative camera poses through homography decomposition. By aggregating estimates from multiple planes or even from a single dominant plane we achieve robust pose recovery in scenarios where traditional methods fail. We introduce a novel graph-based approach that constructs a pose-graph from homography estimates and employs spectral embedding to identify and filter unreliable edges. Our method maps homography-based pose estimates onto the real line based on their geometric and visual consistency, enabling efficient extraction of a maximally consistent spanning tree for pose recovery. This approach naturally handles both highly planar scenes, such as indoor sports arenas, and general $3$D environments. We demonstrate superior performance on basketball court imagery where existing methods struggle, while matching or exceeding state-of-the-art results on unconstrained outdoor scenes from the IMC Phototourism benchmark.

### 🤖 AI 总结

**一句话总结**：Structure from Motion (SfM) systems traditionally struggle with planar scenes, where standard epipolar geometry-based methods become degenerate. Rather than viewing planar surfaces as a limitation, we...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Planar-SfM, Camera, Pose, Estimation, via, Homography, Graph, Embeddings

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.31979v1) | [下载PDF](https://arxiv.org/pdf/2606.31979v1.pdf)

---

## [18. AnyBokeh: Physics-Guided Any-to-Any Bokeh Editing with Optical Fingerprint Transfer](https://arxiv.org/abs/2606.31959v1)

**作者**：Xinyu Hou, Xiaoming Li, Zongsheng Yue 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-30

### 📄 论文摘要

Depth-of-field control is a fundamental tool in photography, yet post-capture bokeh editing from a single image remains challenging. A practical editor should handle images captured under arbitrary focus and aperture settings. Existing methods typically assume an all-in-focus input, or first recover an all-in-focus image before rendering new bokeh. Such pipelines can discard useful blur cues from the source image and propagate reconstruction artifacts into the final edit. We introduce AnyBokeh, a physics-guided framework for any-to-any bokeh editing. Instead of treating source blur merely as a degradation to be removed, AnyBokeh estimates the source blur state with a signed circle-of-confusion map and a disparity map. By modeling the linear relation between signed circle of confusion and disparity difference, AnyBokeh estimates a source-specific optical fingerprint and transfers the source optical characteristics to the desired focus and aperture setting. A generative editor conditioned on both source and target circle-of-confusion maps then performs relative blur synthesis, enabling spatially adaptive deblurring, preservation, and defocus rendering. To support physically supervised learning, we further construct a high-fidelity synthetic dataset with accurate depth, focus distance, and full EXIF metadata. Experiments on real-world benchmarks show that AnyBokeh achieves faithful and controllable editing across any-to-any bokeh editing, all-in-focus-to-bokeh rendering, and defocus deblurring, while avoiding all-in-focus reconstruction and test-time bokeh-level calibration commonly required by existing approaches. The code and dataset will be available at https://github.com/itsmag11/AnyBokeh.

### 🤖 AI 总结

**一句话总结**：Depth-of-field control is a fundamental tool in photography, yet post-capture bokeh editing from a single image remains challenging. A practical editor should handle images captured under arbitrary fo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AnyBokeh, Physics-Guided, Any-to-Any, Bokeh, Editing, Optical, Fingerprint, Transfer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.31959v1) | [下载PDF](https://arxiv.org/pdf/2606.31959v1.pdf)

---

## [19. World Narrative Model for Highly Controllable Video Generation: A Paradigm Shift from Pixel Sampling to Physical World Orchestration](https://arxiv.org/abs/2606.31946v1)

**作者**：Ye Chen, Xuanhong Chen, Yupeng Zhu 等 26 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-30

### 📄 论文摘要

The fundamental obstacle to industrial grade video generation is the lack of controllability: existing models treat video as a pixel distribution sampling problem, bypassing the explicit, instance level $4D$ $(3D + T)$ physical world. Consequently, content creators cannot specify geometry, motion, camera parameters, or lighting in a deterministic, quantitative way, leading to the infamous ''gacha'' loop that makes professional content creation prohibitively inefficient and expensive. To address this, we introduce the World Narrative Model (WNM), a paradigm that decouples what to render -- the structured physical narrative -- from how to render -- the pixel generation process. WNM replaces end-to-end black-box sampling with orchestrated $4D$ pre-visualization for media generation. Collaborative agents translate sparse multimodal inputs, including text, reference videos, and sketches, into a fully editable world representation with scene geometry, object layouts, character/animal skeleton motion, trajectories, camera motion, and lighting at quantitative, physically meaningful granularity. This representation acts as a deterministic structural blueprint that drives existing video foundation models, either frozen or lightly adapted, to render final footage, turning the base model into a faithful neural shader. Built on this engine, our human-AI platform supports automatic world generation and pre-visualization aligned with professional filmmaking pipelines, while director consoles enable seamless human refinement. Experiments show that WNM greatly reduces probabilistic ``gacha'' calls and produces videos whose layout, motion, and cinematography closely follow creator intent. The framework is open and modular, allowing each component, such as world representation, control agents, and adapters, to be independently improved. Project website: https://glassroom.sjtu.edu.cn/WNM/.

### 🤖 AI 总结

**一句话总结**：The fundamental obstacle to industrial grade video generation is the lack of controllability: existing models treat video as a pixel distribution sampling problem, bypassing the explicit, instance lev...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：World, Narrative, Model, Highly, Controllable, Video, Generation, Paradigm

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.31946v1) | [下载PDF](https://arxiv.org/pdf/2606.31946v1.pdf)

---

## [20. No Place to Hide: Benchmarking Video Hallucination with Background-Controlled Pairs](https://arxiv.org/abs/2606.31933v1)

**作者**：Haojian Huang, Harold Haodong Chen, Meng Luo 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-30

### 📄 论文摘要

We introduce VidPair-Halluc, a new benchmark for evaluating video hallucination in large video models (LVMs) under rigorous and controlled conditions. Unlike previous benchmarks that primarily rely on text-based perturbations or adversarial questions while neglecting the consistency of visual backgrounds, VidPair-Halluc features video pairs with highly similar backgrounds but distinctly different foreground semantics, enabling precise attribution of model errors to genuine hallucination rather than background variation. The benchmark is constructed through PairFlow, a pipeline that leverages recent advances in text-to-image and video generation to systematically compose stories, generate coherent video clips, and assemble them into adversarial pairs. Covering both spatial and temporal reasoning across ten semantic aspects, VidPair-Halluc comprises 1K high-quality adversarial video pairs and 11K spatio-temporal QA pairs with control over background and foreground variations. Evaluations on mainstream LVMs show persistent difficulty with robust fine-grained video understanding in adversarial settings, and code and data are available at the https://jethrojames.github.io/VidPair-Halluc/.

### 🤖 AI 总结

**一句话总结**：We introduce VidPair-Halluc, a new benchmark for evaluating video hallucination in large video models (LVMs) under rigorous and controlled conditions. Unlike previous benchmarks that primarily rely on...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：No, Place, Hide, Benchmarking, Video, Hallucination, Background-Controlled, Pairs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.31933v1) | [下载PDF](https://arxiv.org/pdf/2606.31933v1.pdf)

---

## [21. InstanceControl: Controllable Complex Image Generation without Instance Labeling](https://arxiv.org/abs/2606.31924v1)

**作者**：Xiaoyu Liu, Huan Wang, Fan Li 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-30

### 📄 论文摘要

Controllable image generation methods, such as ControlNet, have demonstrated a remarkable capacity to introduce visual conditions(e.g., depth maps) to guide image generation. However, these methods often struggle with complex multi-instance scenes, frequently leading to attribute confusion among instances. While recent approaches attempt to mitigate this via manual instance labeling, such requirements are labor-intensive. In this paper, we propose InstanceControl, a novel multi-instance controllable generation method that eliminates the need for instance labeling. We identify the primary bottleneck in existing methods as the inability to accurately associate instance descriptions with their corresponding regions within visual conditions. To address this, we leverage the Vision-Language Model (VLM) to establish instance-level correspondences between text prompts and visual conditions. Specifically, the VLM automatically parses instance descriptions from the text prompts and simultaneously predicts instance masks based on the visual conditions. Furthermore, since the predicted masks may contain noise, we introduce an adaptive mask refinement strategy that dynamically refines these instance masks during the generation process. Extensive experiments demonstrate that our approach outperforms state-of-the-art methods, achieving superior fidelity and precise instance-level control.

### 🤖 AI 总结

**一句话总结**：Controllable image generation methods, such as ControlNet, have demonstrated a remarkable capacity to introduce visual conditions(e.g., depth maps) to guide image generation. However, these methods of...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：InstanceControl, Controllable, Complex, Image, Generation, without, Instance, Labeling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.31924v1) | [下载PDF](https://arxiv.org/pdf/2606.31924v1.pdf)

---

## cs.LG

## [22. QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents](https://arxiv.org/abs/2606.32034v1)

**作者**：Sergio Hernández-Gutiérrez, Matteo Merler, Ilze Amanda Auzina 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-06-30

### 📄 论文摘要

LLM agents increasingly act over long horizons, where a single trajectory can contain hundreds or thousands of actions. In these settings, outcome-only rewards provide too sparse guidance, failing to inform the model about the goodness of intermediate actions. Dense supervision methods aim to solve this problem by scoring intermediate steps, from intrinsic confidence to self-distillation and embedding similarities. However, it is common practice to evaluate them by measuring the downstream performance of a training pipeline that integrates them. This is expensive, conflates supervision quality with training engineering confounders, and renders different methodological families requiring distinct training setups incomparable. As a result, dense supervision methods are rarely benchmarked on common ground. We introduce QVal, a training-free testbed for directly evaluating dense supervision signals. Given a state-action pair, QVal measures how well a method's score is Q-aligned: whether it orders actions according to the Q-values of a strong reference-policy. This lets us compare signals before any training run and separate signal quality from other engineering choices. We instantiate QVal as QVal-v1.0, benchmarking 21 dense supervision methods across four diverse environments and seven methodological families, with over 1.2K evaluation experiments across six open-weight model backbones. We find that simple prompting baselines consistently outperform recent dense supervision methods from the literature, and that performance clusters strongly by family. These findings hold across model sizes, environments, and observation modalities. QVal is designed to be easily extensible to new environments and methods, enabling researchers to iterate on dense supervision methods before any training run.

### 🤖 AI 总结

**一句话总结**：LLM agents increasingly act over long horizons, where a single trajectory can contain hundreds or thousands of actions. In these settings, outcome-only rewards provide too sparse guidance, failing to ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, QVal, Cheaply, Evaluating, Dense, Supervision, Signals, Long-Horizon

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32034v1) | [下载PDF](https://arxiv.org/pdf/2606.32034v1.pdf)

---

## [23. AdaJEPA: An Adaptive Latent World Model](https://arxiv.org/abs/2606.32026v1)

**作者**：Ying Wang, Oumayma Bounou, Yann LeCun 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-30

### 📄 论文摘要

Latent world models enable planning from high-dimensional observations by predicting future states in a compact latent space. However, these models are typically kept frozen at test time: when their predictions become inaccurate, planning can fail, especially under test-time distribution shift. To address this, we propose AdaJEPA, an adaptive latent world model that performs test-time adaptation within the closed loop of model predictive control (MPC). After training, AdaJEPA plans and executes the first action chunk, uses the observed next-state transition as a self-supervised adaptation signal, and replans with the updated model. This closed-loop update continuously recalibrates the world model without additional expert demonstrations. Across a range of goal-reaching tasks, AdaJEPA substantially improves planning success with as few as one gradient step per MPC replanning step.

### 🤖 AI 总结

**一句话总结**：Latent world models enable planning from high-dimensional observations by predicting future states in a compact latent space. However, these models are typically kept frozen at test time: when their p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, AdaJEPA, Adaptive, Latent, World, Model, models, enable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32026v1) | [下载PDF](https://arxiv.org/pdf/2606.32026v1.pdf)

---

## [24. SemRF: A Semantic Reference Frame for Residual-Stream Dynamics in Language Models](https://arxiv.org/abs/2606.32022v1)

**作者**：Jian Gu, Aldeida Aleti, Chunyang Chen 等 4 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-06-30

### 📄 论文摘要

Residual-stream analysis asks how language-model computation evolves across depth, but intermediate decoding requires comparable readout coordinates across layers. If embedding anchors and unembedding readout disagree on the chosen span, apparent motion may reflect measurement drift rather than computation. We introduce \emph{Semantic Reference Frames} (SemRF), an anchor-based formalism separating semantic measurement from residual dynamics. A SemRF fixes anchors and measures states against them. Pseudo-inverse tying gives exact synchronization; under restricted bi-invertibility, SemRF yields stable semantic-basis coordinates, distortion bounds, and near-identity changes. With the frame fixed, residual computation becomes a depthwise semantic trajectory. The anchors induce a semantic Voronoi diagram: distance, or evidence such as logits, assigns each layer to a coarse cell, while coordinates retain within-cell motion and margins. We define layerwise steps, contribution profiles, and imbalance diagnostics, then use the Voronoi trace to define a margin-relaxed tube. The canonical trace is the minimum-action path inside this tube; when nonempty with positive quadratic weight, it is unique and obeys a discrete spline equation away from active constraints. Excess action controls step, curvature, and profile mismatch. Low curvature implies piecewise-linear compressibility and local knowledge density: lower trace complexity means fewer semantic knots. Through the parameter-to-trajectory map, this gives a conditional link to parameter efficiency: among admissible settings fitting data, lower-action and lower-complexity traces use fewer semantic degrees of freedom. The guarantees require controlled interface error and small projection residual under explicit tube constraints.

### 🤖 AI 总结

**一句话总结**：Residual-stream analysis asks how language-model computation evolves across depth, but intermediate decoding requires comparable readout coordinates across layers. If embedding anchors and unembedding...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SemRF, Semantic, Reference, Frame, Residual-Stream, Dynamics, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32022v1) | [下载PDF](https://arxiv.org/pdf/2606.32022v1.pdf)

---

## [25. FedLAB: Traceable Semantic Codebooks for Federated Multimodal Graph Foundation Learning](https://arxiv.org/abs/2606.32016v1)

**作者**：Zekai Chen, Kairui Yang, Xuaner Chen 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-30

### 📄 论文摘要

Multimodal graph foundation models aim to learn reusable knowledge from graphs enriched with text, images, attributes, and relational topology, thereby supporting diverse graph-centric and modality-centric tasks. In practice, however, such multimodal graphs are often distributed across decentralized clients, where raw contents and local structures cannot be centrally shared due to privacy constraints. This motivates federated multimodal graph foundation learning, which requires not only transferable representation learning but also intrinsic semantic traceability under strict data isolation. Existing methods usually exchange or store knowledge through parameters, prototypes, embeddings, or compact codebooks, which support optimization and transfer but do not explicitly expose how modality evidence, node semantics, and topology context jointly support predictions. To bridge this gap, we propose FedLAB, a traceable semantic codebook framework that organizes multimodal graph knowledge into typed hierarchical codebooks for modality evidence, node semantics, and topology context. FedLAB further refines these trace units through federated semantic barycenter pre-training while keeping raw multimodal contents and graph structures local. Extensive experiments on 10 benchmarks and 6 downstream tasks show that FedLAB improves over state-of-the-art baselines by up to 7.53\%, while preserving a native semantic trace interface.

### 🤖 AI 总结

**一句话总结**：Multimodal graph foundation models aim to learn reusable knowledge from graphs enriched with text, images, attributes, and relational topology, thereby supporting diverse graph-centric and modality-ce...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FedLAB, Traceable, Semantic, Codebooks, Federated, Multimodal, Graph, Foundation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32016v1) | [下载PDF](https://arxiv.org/pdf/2606.32016v1.pdf)

---

## [26. CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation](https://arxiv.org/abs/2606.32012v1)

**作者**：Sanghyuk Chun, William Yang, Amaya Dharmasiri 等 4 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-06-30

### 📄 论文摘要

Uncertainty estimation has been a long-standing challenge in AI models; it amounts to "knowing what you don't know," and metacognition is notoriously difficult even for humans (cf. the Dunning-Kruger effect). Although it is still far from solved even in simpler classification systems, tackling it in multimodal large language models (MLLMs) is becoming increasingly important. Within MLLMs, uncertainty can stem from any of the diverse sources as well as from their relationships, and further can stem from the unbounded answers in the open-ended setting. To tackle the issues, we propose CoMet, an MLLM uncertainty estimation method by decomposing uncertainty into a context-specific term and a multiplicity-specific term. The former captures ambiguity induced by the given context (e.g., task or prompt), while the latter captures how many plausible answers determined by the context remain compatible with the given input. We train a lightweight post-hoc uncertainty module to estimate these quantities, which enables efficient uncertainty estimation without autoregressive answer generation or repeated sampling. Experiments on various open-ended multimodal benchmarks, hallucination detection, and multiple-choice visual question answering benchmarks show that CoMet consistently improves uncertainty estimation over existing baselines while remaining efficient in practice. Code is available at https://github.com/princetonvisualai/comet_uncertainty

### 🤖 AI 总结

**一句话总结**：Uncertainty estimation has been a long-standing challenge in AI models; it amounts to "knowing what you don't know," and metacognition is notoriously difficult even for humans (cf. the Dunning-Kruger ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CoMet, Context, Multiplicity, Decomposition, Multimodal, Uncertainty, Estimation, has

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32012v1) | [下载PDF](https://arxiv.org/pdf/2606.32012v1.pdf)

---

## [27. Radial Suppression Accelerates Algorithmic Generalization: A Geometric Analysis of Delayed Generalization](https://arxiv.org/abs/2606.32000v1)

**作者**：Srijan Tiwari, Aditya Chauhan, Manjot Singh  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-30

### 📄 论文摘要

Why do neural networks memorize algorithmic training data long before they generalize? We present a geometric case study demonstrating that, on tasks where generalization requires discovering structured low-dimensional circuits, the memorization-generalization delay is driven by radial inflation of hidden representations under cross-entropy optimization. We formalize a radial-angular decomposition of activation-space dynamics and derive three testable propositions: (i) that penalizing radial inflation induces anisotropic, data-dependent weight regularization; (ii) that it suppresses radial gradient energy below the isotropic random baseline, forcing predominantly angular updates; and (iii) that it biases convergence toward flatter minima. To empirically validate these propositions, we study a single-hyperparameter norm penalty that softly constrains activations to a sqrt(d)-radius hypersphere. On modular arithmetic, this penalty accelerates grokking up to 6x across MLPs and Transformers, and halves training steps for a 10M-parameter nanoGPT on 3-digit addition.

### 🤖 AI 总结

**一句话总结**：Why do neural networks memorize algorithmic training data long before they generalize? We present a geometric case study demonstrating that, on tasks where generalization requires discovering structur...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Radial, Suppression, Accelerates, Algorithmic, Generalization, Geometric, Analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.32000v1) | [下载PDF](https://arxiv.org/pdf/2606.32000v1.pdf)

---

## [28. Amplifying Membership Signal Through Chained Regeneration](https://arxiv.org/abs/2606.31991v1)

**作者**：Wojciech Łapacz, Stanisław Pawlak  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-30

### 📄 论文摘要

The tendency of large generative models to memorize training data makes sample verification critical for privacy auditing and copyright enforcement. Current membership (MIA) and dataset inference (DI) attacks often rely on one-shot generations, which yield weak signals and limited sensitivity across modalities. Inspired by Model Autophagy Disorder (MAD), we introduce MADreMIA, a model-agnostic framework that enhances white-, gray-, and black-box MIA and DI. Rather than relying on shadow model training -- often infeasible for large generative models -- our framework facilitates scalable inference by leveraging inherent signals through iterative trajectories. This process utilizes chained generations across diverse modalities, where each output serves as the subsequent input, to improve membership evidence at low FPR. We demonstrate that memorized training samples exhibit significantly higher coherence and slower degradation during iterative regeneration than non-member generations. Our results show that MADreMIA provides richer signals across diverse model families and modalities; we present comprehensive evaluations for IARs, diffusion, and language models, alongside preliminary results demonstrating its potential for audio models.

### 🤖 AI 总结

**一句话总结**：The tendency of large generative models to memorize training data makes sample verification critical for privacy auditing and copyright enforcement. Current membership (MIA) and dataset inference (DI)...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Amplifying, Membership, Signal, Through, Chained, Regeneration, tendency

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.31991v1) | [下载PDF](https://arxiv.org/pdf/2606.31991v1.pdf)

---

## [29. Signed-Permutation Coordinate Transport for RMSNorm Transformers](https://arxiv.org/abs/2606.31963v1)

**作者**：John Sweeney  
**分类**：cs.LG, cs.CL, stat.ML  
**发布时间**：2026-06-30

### 📄 论文摘要

Modern LLM workflows move coordinate-indexed objects across checkpoints: steering vectors, sparse autoencoders, top-$k$ neuron sets, attribution lists, and merge alignments. This is only well posed after fixing the model's residual-stream gauge, which we show is architecture-dependent: LayerNorm residual charts have permutation gauge $S_d$ (up to a global sign flip), while RMSNorm charts with generic per-channel gain have signed-permutation gauge $B_d = S_d \ltimes \{\pm 1\}^d$. Permutation-only alignment is therefore symmetry-incomplete for RMSNorm models. We introduce sign-marginalized Hungarian matching and prove a sharp failure mode: with decorrelated coordinates, raw signed-correlation matching has a structural permutation-accuracy ceiling at the positive-sign fraction of the true gauge, which sign-marginalization removes. We then make coordinate-preserving transport, not function-level merging, the primary object: composing saved-checkpoint local $B_d$ gauges along same-base fine-tuning trajectories recovers 91.1% of cross-run coordinates at 1500 steps versus 60.3% for endpoint matching, and the gain is not explained by merely routing through the base. The recovered gauge transfers tools that permutation-only alignment breaks: TinyLlama SAE reconstruction has NMSE 0.004 under $B_d$ versus 1.08 under $S_d$; Qwen sentiment steering preserves 95.8% of its effect versus 17.2%; refusal steering reverses sign under $S_d$; coordinate-preserving merges behave the same way. The same covariance governs stateful training: signed transport of AdamW state preserves the resumed trajectory, while permutation-only state follows a different one from a functionally identical checkpoint. Finally, gauge-sweep audits show index-level interpretability claims are reproducible only relative to an explicit gauge.

### 🤖 AI 总结

**一句话总结**：Modern LLM workflows move coordinate-indexed objects across checkpoints: steering vectors, sparse autoencoders, top-$k$ neuron sets, attribution lists, and merge alignments. This is only well posed af...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Signed-Permutation, Coordinate, Transport, RMSNorm, Transformers, Modern, workflows

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.31963v1) | [下载PDF](https://arxiv.org/pdf/2606.31963v1.pdf)

---

## [30. Making Sense of Touch from the Child's View for Contrastive Learning](https://arxiv.org/abs/2606.31943v1)

**作者**：Max Whitton, Zecheng Wang, Puchen Liu 等 15 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-30

### 📄 论文摘要

Is the sense of touch a mechanism for human babies' learning of visual concepts? If so, can we quantify its importance, and to what extent do babies rely on their sense of touch for visual learning? To approach these questions in a principled way, we propose a structured coding system for baby-centric touch events, yielding a dataset of 264k two-second clips of touch events coded according to this system. Using this dataset, we pretrain developmentally grounded models that reveal promising insights into the nature of baby learning from touch.

### 🤖 AI 总结

**一句话总结**：Is the sense of touch a mechanism for human babies' learning of visual concepts? If so, can we quantify its importance, and to what extent do babies rely on their sense of touch for visual learning? T...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Making, Sense, Touch, Child's, View, Contrastive, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.31943v1) | [下载PDF](https://arxiv.org/pdf/2606.31943v1.pdf)

---

