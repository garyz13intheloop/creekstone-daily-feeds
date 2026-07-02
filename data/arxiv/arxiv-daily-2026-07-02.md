# arXiv AI 论文日报 | 2026-07-02

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (5 篇)
- [cs.LG](#csLG) (12 篇)
- [cs.AI](#csAI) (2 篇)
- [cs.CV](#csCV) (11 篇)

---

## cs.AI

## [1. Theoria: Rewrite-Acceptability Verification over Informal Reasoning States](https://arxiv.org/abs/2607.01223v1)

**作者**：Ben Slivinski, Michael Saldivar  
**分类**：cs.AI, cs.CL, cs.LG, cs.LO, cs.SE  
**发布时间**：2026-07-01

### 📄 论文摘要

When should an AI system's answer be trusted? Formal proof assistants offer certainty but cannot reach most of the problem distribution; scalar LLM judges offer coverage but produce opaque scores that cannot be audited after the fact and are subject to the same coherence issues as any LLM. We present Theoria, a verification architecture that closes this gap. A candidate solution is rewritten into a sequence of typed state transitions, each licensed by an explicit justification, whether that be a citation, computation, or problem-given fact, and every transition is independently auditable. The foundational invariant is completeness of change: every difference between consecutive proof states must be accounted for, so hidden premises surface as unlicensed mutations rather than passing silently. On HLE-Verified Gold (185 text-only expert problems), Theoria certifies 105 at 91.4% strict precision (Wilson 95% CI [84.5%, 95.4%]). Every certification produces a human readable proof trace in which each step can be independently challenged. Holistic LLM judges achieve comparable precision at matched coverage but fail on different problems (Jaccard 0.14-0.36), making the approaches complementary. On 95 adversarial poisoned proofs across 15 domains, structured judges catch 94.7% versus 83.2% for holistic judging (p= 0.0017). The overall 11.5 pp gap concentrates in hidden premises (90.6% vs. 62.5%, a 28 pp difference) and fabricated citations (100% vs. 90%), the error classes where the formal analysis predicts an advantage; performance is identical on arithmetic and theorem-misapplication errors, where no advantage is predicted. On GPQA Diamond (n= 65), certified precision is 97.1% (Wilson CI [85.1%, 99.5%]).

### 🤖 AI 总结

**一句话总结**：When should an AI system's answer be trusted? Formal proof assistants offer certainty but cannot reach most of the problem distribution; scalar LLM judges offer coverage but produce opaque scores that...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Theoria, Rewrite-Acceptability, Verification, over, Informal, Reasoning, States, When

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01223v1) | [下载PDF](https://arxiv.org/pdf/2607.01223v1.pdf)

---

## [2. Optimal Resource Utilization for Autonomous Laboratory Orchestrators](https://arxiv.org/abs/2607.01188v1)

**作者**：Austin McDannald, Julia Tisaranni, Howie Joress  
**分类**：cs.AI, cond-mat.mtrl-sci  
**发布时间**：2026-07-01

### 📄 论文摘要

In autonomous laboratories, AI agents suggest the next batch of experiments to do. However, planning and executing those tasks taking full advantage of the available resources is a completely different question. This can be challenging when dealing with real-world hardware constraints, especially so when there are multiple instruments with different capacities and throughputs. Here we demonstrate a 2-step method to address resource utilization for our autonomous platform for metal-organic framework synthesis. First, we use constraint programming to find optimal schedules. This finds schedules that minimizes the total time while still satisfying the limitations and capacities of the hardware. Secondly, we use a system of status dependencies for each task, which allows for the robust execution of the optimal schedules.

### 🤖 AI 总结

**一句话总结**：In autonomous laboratories, AI agents suggest the next batch of experiments to do. However, planning and executing those tasks taking full advantage of the available resources is a completely differen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Optimal, Resource, Utilization, Autonomous, Laboratory, Orchestrators, laboratories

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01188v1) | [下载PDF](https://arxiv.org/pdf/2607.01188v1.pdf)

---

## cs.CL

## [3. Measuring the Gap Between Human and LLM Research Ideas](https://arxiv.org/abs/2607.01233v1)

**作者**：Ziyu Chen, Yilun Zhao, Arman Cohan  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-01

### 📄 论文摘要

LLMs are increasingly used to brainstorm research ideas, but existing evaluations mostly judge individual ideas by novelty, feasibility, or expert preference. We instead ask: how far are current LLM-generated ideas from human researchers? To characterize this gap, we build a large-scale evaluation framework for ideation from high-quality human research papers. For each paper, we reverse-engineer a small set of closely related prior works that likely inspired its core idea. LLMs are then prompted to generate a new idea from the set of paper titles and summaries. We introduce a two-axis research-taste taxonomy to profile each idea by its opportunity pattern and research paradigm, and use it to quantify the divergence between human and LLM ideas. Across idea sets generated by different LLMs, we observe a consistent distributional gap: LLM ideas are disproportionately concentrated around bridge-like opportunities and synthesis methods, whereas the human paper reference distribution spreads more broadly across ways of framing gaps and constructing contributions. This result suggests that strong LLMs can produce a range of reasonable ideas, but that range remains narrower than, and systematically shifted relative to, human research taste.

### 🤖 AI 总结

**一句话总结**：LLMs are increasingly used to brainstorm research ideas, but existing evaluations mostly judge individual ideas by novelty, feasibility, or expert preference. We instead ask: how far are current LLM-g...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Measuring, Gap, Between, Human, Research, Ideas, increasingly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01233v1) | [下载PDF](https://arxiv.org/pdf/2607.01233v1.pdf)

---

## [4. Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation](https://arxiv.org/abs/2607.01208v1)

**作者**：Shayan Talaei, Abhinav Chinta, Devvrit Khatri 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-07-01

### 📄 论文摘要

Language models deployed in high-stakes roles can potentially favor certain entities, brands, or viewpoints, steering user decisions at scale. Such preferential biases can be introduced by any actor in the model's supply chain and are most dangerous when the model reveals its preference only on the relevant topic while behaving identically to its unmodified base on all other inputs. Recent work has shown that these biases can transfer through context distillation on semantically unrelated data, with the signal residing entirely in the soft logit distribution and remaining invisible to text-based inspection. However, the defender faces a fundamental asymmetry: without knowing the bias topic, no detection method can reliably surface a stealth preferential bias, regardless of whether it examines generated text, internal representations, or model weights. Here we introduce Distill to Detect (D2D), a method that surfaces hidden biases by distilling the distributional shift between a suspected model and its base into a cartridge (a KV-cache prefix adapter), concentrating the dominant divergence and amplifying the bias signal into generated text. We show that D2D successfully amplifies the hidden biases of stealth models to the extent that they can be reliably detected across multiple bias types. We also propose a theoretical framework that explains the efficacy of D2D through the lens of Fisher-weighted projection of the logit distribution shift, supported by empirical observations. By turning the capacity bottleneck of prefix-tuning adapters into a detection tool, D2D provides a practical building block for auditing hidden behaviors in deployed language models.

### 🤖 AI 总结

**一句话总结**：Language models deployed in high-stakes roles can potentially favor certain entities, brands, or viewpoints, steering user decisions at scale. Such preferential biases can be introduced by any actor i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Distill, Detect, Exposing, Stealth, Biases, through, Cartridge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01208v1) | [下载PDF](https://arxiv.org/pdf/2607.01208v1.pdf)

---

## [5. AGC-Bench: Measuring Artificial General Creativity](https://arxiv.org/abs/2607.01152v1)

**作者**：Roger Beaty, Vijeta Deshpande, Clin K. Y. Lai 等 12 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-01

### 📄 论文摘要

Creativity research has debated whether creativity is domain-specific (e.g., visual, writing, science), and if it is psychometrically separable from general intelligence. Both questions now apply to LLMs, but a unified benchmark of AI creativity remains elusive. We introduce AGC-Bench, an artificial general creativity benchmark built from a systematic review of the AI creativity literature (3,101 papers screened, 497 benchmarks identified), paired with an agentic harness that converts idiosyncratic codebases into HELM-standardized benchmarks. The first release covers 78 datasets spanning brainstorming, problem solving, STEM, narrative, figurative language, and humor. To address bias in LLM-as-judge, we apply Judge Response Theory -- a psychometric calibration of judge leniency/severity; we then fine-tune Qwen3-30B on the bias-corrected ratings of three frontier LLMs to produce AGC-Judge, an open-weight model that robustly scores new creativity benchmarks it was not trained on. Results reveal frontier models at the top of the AGC-Bench leaderboard, with open models close behind. LLMs show different creative strengths, ranking higher on some domains (e.g., writing) than others (e.g., scientific ideation). Extensive experiments yield three main findings. First, applying factor analysis across 83 LLMs, we recover a single creativity factor 'c', analogous to the 'g' factor of general intelligence, that explains 81.5% of variance, related to but separable from general knowledge/reasoning. Second, we show that prompting models to "be creative" boosts their performance far more than enabling reasoning, evidence that the benchmark tracks creativity over general ability. Third, on a human-matched subset, we find the top human still leads the top LLM on creativity. We release AGC-Bench with a public leaderboard, AGC-Judge, and human data as open infrastructure for measuring AI creativity at scale.

### 🤖 AI 总结

**一句话总结**：Creativity research has debated whether creativity is domain-specific (e.g., visual, writing, science), and if it is psychometrically separable from general intelligence. Both questions now apply to L...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AGC-Bench, Measuring, Artificial, General, Creativity, research, has, debated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01152v1) | [下载PDF](https://arxiv.org/pdf/2607.01152v1.pdf)

---

## [6. $\text{Log}_\text{b}$Quant: Quantizing Language Models in Logarithmic Space](https://arxiv.org/abs/2607.01127v1)

**作者**：Jeremias Bohn, Tizian Dippold, Mahdi Koubaa 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-01

### 📄 论文摘要

Quantization has become an invaluable tool to reduce memory requirements and inference speed of modern language models, in particular to make them available for consumer setups and edge devices. While previous work has primarily focused on uniform quantization codebooks, such approaches are prone to suboptimal representations due to low-frequency high-magnitude weights. We introduce Log$_\text{b}$Quant, a novel logarithmic quantization approach with adjustable bases, to adapt to common parameter distributions. We show that our method exhibits superior performance at 4-bit precision on several performance benchmarks compared to asymmetric linear quantization at tensor-wise granularity, while achieving moderate speedup and high memory savings, making it suitable for private use on consumer-grade GPUs.

### 🤖 AI 总结

**一句话总结**：Quantization has become an invaluable tool to reduce memory requirements and inference speed of modern language models, in particular to make them available for consumer setups and edge devices. While...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：text, Log, $Quant, Quantizing, Language, Models, Logarithmic, Space

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01127v1) | [下载PDF](https://arxiv.org/pdf/2607.01127v1.pdf)

---

## [7. Towards Developing a Multimodal Chat Assistant for University Stakeholders: RAG-based Approach](https://arxiv.org/abs/2607.01115v1)

**作者**：Md Abu Hanif Shaikh, Abdullah Al Shafi  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-01

### 📄 论文摘要

University stakeholders often face difficulties in accessing timely and reliable information, especially in developing countries, where there are very few intelligent support systems. Existing rule-based chatbots are unable to handle complex, domain-specific queries and are not well-equipped to adapt to evolving institutional policies. As a fill-in-the-gap solution, we present the multimodal university chatbot with retrieval-augmented generation. The system combines the large language model with semantic retrieval to produce context-based responses from institution-centric resources, such as the university handbook. The system accepts text and image queries through the vision-language model and applies quantized inference for rapid deployment on constrained hardware. A scalable backend built with FastAPI, adjoined with a responsive frontend developed with Next.js, ensures real-time usability. Our multimodal evaluation demonstrates that the system maintains strong satisfaction scores across both text and image queries, despite increased response time for visual inputs. Furthermore, quantitative evaluation shows that hallucination is reduced from 31.7% to 6.6% in our proposed RAG-based system, confirming the effectiveness of retrieval grounding.

### 🤖 AI 总结

**一句话总结**：University stakeholders often face difficulties in accessing timely and reliable information, especially in developing countries, where there are very few intelligent support systems. Existing rule-ba...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Towards, Developing, Multimodal, Chat, Assistant, University, Stakeholders, RAG-based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01115v1) | [下载PDF](https://arxiv.org/pdf/2607.01115v1.pdf)

---

## cs.CV

## [8. Ink3D: Sculpting 3D Assets with Extremely Complex Textures via Video Generative Models](https://arxiv.org/abs/2607.01222v1)

**作者**：Yue Han, Chong Li, Zhening Liu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-01

### 📄 论文摘要

Recent 3D generative models can synthesize high-quality geometry but often struggle to reproduce intricate textures from reference images, largely due to the scarcity of large-scale 3D training data with rich surface appearance. In contrast, visual generative models are trained on datasets several orders of magnitude larger and excel at modeling complex visual patterns. Motivated by this gap, we introduce Ink3D, a framework that bridges 3D generation with large-scale video generative models to synthesize extremely complex textures. Ink3D first reconstructs a white-mesh geometry using an off-the-shelf 3D generation model. It then employs OrbitPainter, a conditional video generative model, to produce dense orbit-scan videos capturing object appearance across viewpoints. To convert these views into coherent textures, we introduce TextureOptimizer, a neural baking module that integrates dense multi-view observations while mitigating geometry inconsistencies arising from video generation. By decoupling geometry and texture synthesis and leveraging large-scale pretrained video priors, Ink3D enables significantly richer and more faithful texture generation than prior approaches.

### 🤖 AI 总结

**一句话总结**：Recent 3D generative models can synthesize high-quality geometry but often struggle to reproduce intricate textures from reference images, largely due to the scarcity of large-scale 3D training data w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Ink3D, Sculpting, Assets, Extremely, Complex, Textures, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01222v1) | [下载PDF](https://arxiv.org/pdf/2607.01222v1.pdf)

---

## [9. Linkify: Learning from Interface-Augmented Assembly Graphs](https://arxiv.org/abs/2607.01205v1)

**作者**：Anushrut Jignasu, Daniele Grandi  
**分类**：cs.CV  
**发布时间**：2026-07-01

### 📄 论文摘要

We present Linkify, a framework for learning from interface-augmented assembly graphs to enable context-aware part retrieval in mechanical assemblies. While recent generative AI methods for CAD have focused largely on isolated parts or monolithic assemblies, the rich geometric information at the interfaces between parts, where function is realized, remains underexplored. We address this gap by recomputing high-fidelity interface geometry for the Fusion 360 Gallery Assembly dataset, correcting missing and erroneous contacts, and generating point-cloud representations of local contact regions. Using this data, we construct assembly graphs whose nodes encode part geometry and whose edges encode interface geometry via a pretrained point-cloud encoder. On top of this representation, we train a Graph Attention Network based on GATv2 to solve a masked part prediction task: given an assembly with one part held out, the model predicts the class of the missing component from a large vocabulary of geometrically clustered parts, thereby approximating a realistic part-retrieval scenario. Compared to non-graph baselines such as logistic regression and k-nearest neighbors operating on aggregated node features, Linkify achieves higher Top-K accuracy and F1 scores. Ablation studies on graph connectivity, edge attributes, and attention mechanisms demonstrate that accurate contact computation and dynamic attention over interfaces are critical for performance. Our corrected interface dataset and training pipeline, released publicly, provide a foundation for future interface-aware models for assembly retrieval, validation, and generative design.

### 🤖 AI 总结

**一句话总结**：We present Linkify, a framework for learning from interface-augmented assembly graphs to enable context-aware part retrieval in mechanical assemblies. While recent generative AI methods for CAD have f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Linkify, Learning, Interface-Augmented, Assembly, Graphs, present, framework

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01205v1) | [下载PDF](https://arxiv.org/pdf/2607.01205v1.pdf)

---

## [10. World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video](https://arxiv.org/abs/2607.01202v1)

**作者**：Liyuan Zhu, Shengyu Huang, Amrita Mazumdar 等 9 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-07-01

### 📄 论文摘要

We present World from Motion, a method for generating freely renderable dynamic 3D Gaussian representations from monocular videos. Our approach conditions a video model on dense, pixel-aligned renderings that encode appearance, geometry, and 3D scene motion along both input and target camera trajectories to correct rendering artifacts and fill in missing regions from an initial reconstruction. To train this model, we construct a dataset of aligned multiview video pairs and dynamic 3DGS representations, with simulated artifacts characteristic of monocular reconstruction. At test time, we distill the model's generations, including newly observed regions and motions, back into a single consistent, high-quality dynamic 3DGS, improving both novel-view synthesis and the underlying 3D motion. Our method sets a new state of the art in 4D reconstruction and seamlessly generalizes to in-the-wild videos with large viewpoint changes and dynamic motions.

### 🤖 AI 总结

**一句话总结**：We present World from Motion, a method for generating freely renderable dynamic 3D Gaussian representations from monocular videos. Our approach conditions a video model on dense, pixel-aligned renderi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：World, Motion, Generative, Dynamic, Gaussian, Reconstruction, Monocular, Video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01202v1) | [下载PDF](https://arxiv.org/pdf/2607.01202v1.pdf)

---

## [11. Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual Reasoning](https://arxiv.org/abs/2607.01191v1)

**作者**：Hongxing Li, Xiufeng Huang, Dingming Li 等 14 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-01

### 📄 论文摘要

Fine-grained visual reasoning remains challenging for vision-language models, especially when small but critical visual cues are buried in high-resolution images. Existing approaches rely on repeated cropping or test-time visual search to introduce local evidence, but they typically do not explicitly distinguish perception from reasoning. In this paper, we propose Perceive-to-Reason (P2R), a unified framework that formulates fine-grained visual reasoning as a two-stage process: the model first localizes question-relevant evidence as a Perceiver, and then answers the question as a Reasoner based on the annotated image and cropped regions. To better align training with this decoupled formulation, we further introduce Perception-Reasoning Alternating GRPO (PRA-GRPO), a role-aware reinforcement learning strategy that alternates between perception-focused and reasoning-focused updates using only final-answer supervision. Built on top of Qwen3-VL-Instruct-2B/4B/8B, P2R consistently improves performance across model scales. In particular, P2R-4B achieves 93.2% on V-Star, 81.9% on HR-Bench-4K, and 80.5% on HR-Bench-8K, substantially outperforming its corresponding backbone. Further experiments show that the benefits of P2R extend beyond high-resolution benchmarks to broader multimodal reasoning tasks. These results suggest that explicitly decoupling perception from reasoning provides an effective framework for fine-grained visual reasoning.

### 🤖 AI 总结

**一句话总结**：Fine-grained visual reasoning remains challenging for vision-language models, especially when small but critical visual cues are buried in high-resolution images. Existing approaches rely on repeated ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Perceive-to-Reason, Decoupling, Perception, Reasoning, Fine-Grained, Visual, remains, challenging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01191v1) | [下载PDF](https://arxiv.org/pdf/2607.01191v1.pdf)

---

## [12. High-dimensional Embedding Prior for Noisy K-space Domain MRIReconstruction](https://arxiv.org/abs/2607.01176v1)

**作者**：Yu Guan, Tianjia Huang, Qinrong Cai 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-01

### 📄 论文摘要

Magnetic resonance imaging (MRI) reconstruction under realistic acquisition conditions can be fundamentally viewed as estimating the underlying k-space distribution from incomplete and noise-corrupted measurements. While diffusion models have recently shown strong potential as generative prior for inverse problems,existingapproachesstruggletohandlenoisyreconstruction settings, especially when operating directly in k-space domain. In this work, we propose a unified high-dimensional k-space reconstruction framework tailored for noisy inverse problems, whichenhancesdiffusion-based solversthroughrepresentation lifting.Ratherthanmodifyingthe underlying optimization procedures, the proposed framework augments the data representation space, enabling existing diffusion-based solvers to operate on enriched k-space embeddings with improved expressiveness. Extensive experiments on both in-house and public datasets across varying noise levels and undersampled factors demonstrate that the proposed frame work consistently improves reconstruction quality for multiple diffusion-based inverse solvers. Notably, the largest gains are observed in high-noise regimes, which is consistent with our theoretical analysis of error propagation under high-dimensional representation. These results suggest that high-dimensional representation provides a general and model-agnostic mechanism for improving diffusion-based MRI reconstruction in noisy settings, offering a new perspective on robust k-space generative modeling for practical inverse problems. The code will be available at https://github.com/yqx7150/HEP-MRIRec.

### 🤖 AI 总结

**一句话总结**：Magnetic resonance imaging (MRI) reconstruction under realistic acquisition conditions can be fundamentally viewed as estimating the underlying k-space distribution from incomplete and noise-corrupted...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：High-dimensional, Embedding, Prior, Noisy, K-space, Domain, MRIReconstruction, Magnetic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01176v1) | [下载PDF](https://arxiv.org/pdf/2607.01176v1.pdf)

---

## [13. EquiSteer: Cross-Attention Steering Towards a Fairer Text-Guided Image Generation](https://arxiv.org/abs/2607.01147v1)

**作者**：Tatiana Gaintseva, Akshit Achara, Gregory Slabaugh 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-01

### 📄 论文摘要

Text-to-image diffusion models power everyday creative tasks, but they still reproduce the demographic biases in their training data. On common prompts such as ``a photo of a nurse,'' ``a photo of a CEO'', they skew their outputs toward one gender, driven by the statistics of training data rather than anything in the text. Existing debiasing methods show promise in narrow settings but require retraining, batch-level control, or prompt-specific tuning, limiting their scalability. We propose \emph{EquiSteer}, a training-free method that works per sample by steering cross-attention (CA) activations at inference time. For each target attribute, EquiSteer precomputes steering vectors from contrastive prompts. Then at generation time, a prompt-aware gate leaves attribute-specific prompts untouched, while for neutral ones it clears existing attribute signals from the CA activations and injects a target attribute. Across SD-1.5, SD-2.1, SDXL, and SANA, EquiSteer reduces the average parity gap by up to $87\%$, with minimal effect on image quality and text-image alignment. Code is available at \href{https://github.com/Atmyre/EquiSteer}{https://github.com/Atmyre/EquiSteer}.%

### 🤖 AI 总结

**一句话总结**：Text-to-image diffusion models power everyday creative tasks, but they still reproduce the demographic biases in their training data. On common prompts such as ``a photo of a nurse,'' ``a photo of a C...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EquiSteer, Cross-Attention, Steering, Towards, Fairer, Text-Guided, Image, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01147v1) | [下载PDF](https://arxiv.org/pdf/2607.01147v1.pdf)

---

## [14. Relation-Centric Open-Vocabulary 3D Gaussian Segmentation](https://arxiv.org/abs/2607.01140v1)

**作者**：Eunsung Cha, Hyunjoon Lee, Jaesik Park  
**分类**：cs.CV  
**发布时间**：2026-07-01

### 📄 论文摘要

Open-vocabulary 3D Gaussian segmentation is challenging because it requires language understanding for diverse queries and accurate separation of Gaussians along object boundaries. Prior approaches either embed language knowledge into individual Gaussians to improve query responsiveness or optimize per-Gaussian instance features to encode object identity. However, these strategies may produce noisy Gaussian segmentations or rely on cost-inefficient per-scene optimization. We propose PairGS, a framework that reframes Gaussian segmentation as modeling pairwise relations between Gaussians. 3D Gaussian representations provide rich signals for relation estimation, such as view contribution weights and multi-view mask evidence. By leveraging these cues, PairGS explicitly constructs a relation graph for segmentation without a heavy optimization process. PairGS first proposes sparse edge candidates using low-dimensional descriptors, computes precise pairwise affinities only on those candidates, and builds a hierarchical cluster tree for multi-granular querying. It achieves state-of-the-art results on open-vocabulary 3D Gaussian segmentation benchmarks, while the fast variant is 50x faster than optimization-based instance-feature approaches.

### 🤖 AI 总结

**一句话总结**：Open-vocabulary 3D Gaussian segmentation is challenging because it requires language understanding for diverse queries and accurate separation of Gaussians along object boundaries. Prior approaches ei...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, it, Relation-Centric, Open-Vocabulary, Gaussian, Segmentation, challenging, because

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01140v1) | [下载PDF](https://arxiv.org/pdf/2607.01140v1.pdf)

---

## [15. SD-RouteFusion: Ego-Trajectory Prediction with SD-Map Route Conditioning](https://arxiv.org/abs/2607.01139v1)

**作者**：Sviatoslav Voloshyn, Bruno K. W. Martens, Wangxin Liu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-01

### 📄 论文摘要

This paper presents SD-RouteFusion, a deployable end-to-end ego-trajectory prediction method that fuses a front-facing camera, vehicle kinematics, and a navigation route derived from a Standard Definition (SD) map. Unlike approaches that rely on High Definition (HD) map geometry, SD-RouteFusion aligns the learning objective with scalable and production-ready SD-map route inputs, enabling route-aware prediction without requiring HD-map infrastructure. First, we demonstrate that SD-map route prior provides a powerful long-horizon semantic prior. Through a comprehensive study on a large-scale real-world dataset comprising 480k driving scenarios across 10 European countries and the U.S., we quantify the value of SD-route conditioning: incorporating SD-map routes yields a 10.5% ADE improvement over an image-and-kinematics baseline, while our full fusion strategy achieves a 16.9% ADE reduction given a prediction horizon of 8 seconds. The fusion strategy consists of a dual-hypothesis design paired with a gated classifier, to ensure robustness under route corruption and visual uncertainty. Finally, to support broader evaluation, we release an SD-route generation toolkit that enables SD-route-conditioned ego-trajectory prediction on all datasets containing ego pose and future trajectories. Together, SD-RouteFusion establishes a practical path toward robust, route-aware ego-trajectory prediction at scale.

### 🤖 AI 总结

**一句话总结**：This paper presents SD-RouteFusion, a deployable end-to-end ego-trajectory prediction method that fuses a front-facing camera, vehicle kinematics, and a navigation route derived from a Standard Defini...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SD-RouteFusion, Ego-Trajectory, Prediction, SD-Map, Route, Conditioning, paper, presents

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01139v1) | [下载PDF](https://arxiv.org/pdf/2607.01139v1.pdf)

---

## [16. Towards Metric-Agnostic Trajectory Forecasting](https://arxiv.org/abs/2607.01133v1)

**作者**：Markus Knoche, Daan de Geus, Bastian Leibe  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-07-01

### 📄 论文摘要

Accurate trajectory forecasting of surrounding traffic participants is a core capability for autonomous driving, enabling vehicles to anticipate behavior and plan safe maneuvers. We observe that current state-of-the-art forecasting models on Argoverse 2 and the Waymo Open Motion Dataset tailor their training objectives to the different benchmark metrics. Because these metrics encourage conflicting behavior, we propose a paradigm change for trajectory forecasting: training models with metric-agnostic probabilistic objectives and treating metric optimization as a downstream task applied to the predictive distribution. Concretely, we introduce Trajectory Distribution Evaluation (TraDiE) policies, metric-specific policies that map a predictive distribution to the set of $K$ trajectories and confidences required by trajectory forecasting metrics. We evaluate this framework by introducing DONUT-NLL, which adapts the training objective of the state-of-the-art trajectory forecasting model DONUT to directly optimize the predictive distribution. Using our policies, DONUT-NLL achieves state-of-the-art results on all metrics of the Waymo motion prediction benchmark.

### 🤖 AI 总结

**一句话总结**：Accurate trajectory forecasting of surrounding traffic participants is a core capability for autonomous driving, enabling vehicles to anticipate behavior and plan safe maneuvers. We observe that curre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Towards, Metric-Agnostic, Trajectory, Forecasting, Accurate, surrounding, traffic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01133v1) | [下载PDF](https://arxiv.org/pdf/2607.01133v1.pdf)

---

## [17. Autonomous Scientific Discovery via Iterative Meta-Reflection](https://arxiv.org/abs/2607.01131v1)

**作者**：Bingchen Zhao, Sara Beery, Oisin Mac Aodha  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-01

### 📄 论文摘要

Autonomous scientific discovery systems offer the potential to accelerate research by automating the process of hypothesis generation and validation. However, current systems operate within constrained search spaces or require predefined research questions, limiting their capacity for true open-ended inquiry. Furthermore, while they generate hypotheses iteratively, they largely lack the ability to explicitly synthesize their own accumulated findings to uncover complex, interconnected phenomena. We introduce DiscoPER, an autonomous large language model-powered framework that conducts open-ended research by dynamically generating and executing code to explore datasets without pre-specified research objectives. To ensure rigorous scientific validity, every proposed discovery must pass statistical testing. To overcome the limitations of isolated search, our framework introduces a second-order reasoning mechanism that periodically analyzes its own accumulated discoveries. By treating prior discoveries as empirical data, DiscoPER identifies structural patterns, confounds, and epistemic gaps, actively redirecting hypothesis exploration toward uncharted regions of the search space. The search space is further expanded by incorporating tool use, enabling the system to explore hypotheses beyond structured metadata by seamlessly processing and extracting useful information from multimodal sources like images. Evaluated on iNatDisco, a new multimodal ecological knowledge benchmark with pattern-level ground truth obtained from peer-reviewed literature, DiscoPER recovers 8 of 9 known patterns with a 72.7% hypothesis support rate, outperforming both classical causal discovery and LLM-guided baselines. Ablations show that DiscoPER scales with more data, and confirms the benefits of second-order meta-reflection.

### 🤖 AI 总结

**一句话总结**：Autonomous scientific discovery systems offer the potential to accelerate research by automating the process of hypothesis generation and validation. However, current systems operate within constraine...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Autonomous, Scientific, Discovery, via, Iterative, Meta-Reflection, systems, offer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01131v1) | [下载PDF](https://arxiv.org/pdf/2607.01131v1.pdf)

---

## [18. MoHallBench: A Benchmark for Motion Hallucination in Video Large Language Models](https://arxiv.org/abs/2607.01117v1)

**作者**：Jiale Li, Sihan Chen, Mengyuan Liu  
**分类**：cs.CV  
**发布时间**：2026-07-01

### 📄 论文摘要

Video Large Language Models (VideoLLMs) have shown strong progress in video understanding, yet they still suffer from hallucinations that are inconsistent with visual evidence. Existing benchmarks mainly focus on object hallucination or coarse action perception, leaving a key video-specific problem underexplored: motion hallucination, in which models infer human motions that are absent from the video. We present MoHallBench, a benchmark for diagnosing motion hallucination in VideoLLMs. MoHallBench systematically evaluates three major sources of hallucination: co-occurrence priors, sequential inference, and similarity confusion. It contains 11,306 video clips and 40,493 question-answer pairs, covering binary-choice, multiple-choice, and generative settings. We further introduce a bi-directional questioning protocol with bias-aware metrics to reduce affirmation bias in binary evaluation. Experiments on ten recent open-source VideoLLMs reveal a clear decoupling between action recognition and hallucination resistance, as models that perform well on positive action recognition often fail on adversarial negatives. Among all settings, sequential inference hallucination is the most severe, showing that current models tend to over-infer expected outcomes from partial motion cues. Our analyses further confirm that stronger priors and finer-grained similarity substantially amplify hallucination. We hope MoHallBench can facilitate future evaluation and mitigation of motion hallucination in VideoLLMs.

### 🤖 AI 总结

**一句话总结**：Video Large Language Models (VideoLLMs) have shown strong progress in video understanding, yet they still suffer from hallucinations that are inconsistent with visual evidence. Existing benchmarks mai...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MoHallBench, Benchmark, Motion, Hallucination, Video, Large, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01117v1) | [下载PDF](https://arxiv.org/pdf/2607.01117v1.pdf)

---

## cs.LG

## [19. Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training](https://arxiv.org/abs/2607.01232v1)

**作者**：Zijian Zhang, Rizhen Hu, Athanasios Glentis 等 7 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-07-01

### 📄 论文摘要

Reinforcement learning (RL) has become a central component of post-training large language models (LLMs), yet little is understood about how RL adaptation is distributed across transformer layers. Existing approaches typically update all model parameters uniformly, implicitly assuming that every layer contributes similarly to the gains obtained during RL post-training. In this work, we challenge this assumption through a systematic layer-wise study of RL training. Surprisingly, we find that training a single transformer layer can recover most of the gains achieved by full-parameter RL training, and in some cases even surpass it. To quantify this phenomenon, we introduce the quantity layer contribution, which measures the fraction of full RL improvement recovered by training a layer in isolation. Across seven models spanning two model families (Qwen3, Qwen2.5), three RL algorithms (GRPO, GiGPO, Dr. GRPO), and multiple task domains including mathematical reasoning, code generation, and agentic decision-making, we observe a remarkably stable pattern: RL gains are highly concentrated in a small subset of, and in many cases even a single, transformer layers. More strikingly, the same structural pattern consistently emerges: high-contribution layers concentrate in the middle of the transformer stack, while layers near the input and output ends contribute substantially less. The resulting layer rankings remain strongly correlated across datasets, tasks, model families, and RL algorithms.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning (RL) has become a central component of post-training large language models (LLMs), yet little is understood about how RL adaptation is distributed across transformer layers. Exi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：One, Layer, Enough?, Training, Single, Transformer, Can, Match

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01232v1) | [下载PDF](https://arxiv.org/pdf/2607.01232v1.pdf)

---

## [20. TiRex-2: Generalizing TiRex to Multivariate Data and Streaming](https://arxiv.org/abs/2607.01204v1)

**作者**：Patrick Podest, Marco Pichler, Elias Bürger 等 10 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-01

### 📄 论文摘要

We introduce TiRex-2, a recurrent xLSTM-based time series foundation model that generalizes the univariate TiRex to multivariate forecasting with both past and future covariates. Real-world forecasting is inherently sequential: observations arrive continuously, variables evolve jointly, and a subset of covariates is known ahead of time. Existing Transformer-based time series foundation models capture cross-variate dependencies but incur quadratic complexity in context length and require full-history recomputation as new observations arrive. TiRex-2 addresses these limitations through a memory-centric recurrent design that operates at constant per-patch cost under streaming. The model combines a bidirectional time mixer with an asymmetric grouped-attention variate mixer, enabling the integration of future-known covariates while preserving strict causality over target variables. To our knowledge, this is the first time series foundation model that achieves this combination of properties. To support scalable multivariate pretraining, we propose a synthetic coupling pipeline that composes diverse multivariate samples on the fly from large univariate corpora. Empirically, TiRex-2 achieves state-of-the-art zero-shot performance on GIFT-Eval and fev-bench, remains stable when streamed to arbitrary context lengths, and maintains constant inference cost per patch. The model uses 38.4M active parameters in univariate mode, with an additional 44.1M parameters activated for multivariate forecasting.

### 🤖 AI 总结

**一句话总结**：We introduce TiRex-2, a recurrent xLSTM-based time series foundation model that generalizes the univariate TiRex to multivariate forecasting with both past and future covariates. Real-world forecastin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, TiRex-2, Generalizing, TiRex, Multivariate, Data, Streaming, introduce

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01204v1) | [下载PDF](https://arxiv.org/pdf/2607.01204v1.pdf)

---

## [21. Quantum vs. Classical Machine Learning: A Unified Empirical Comparison](https://arxiv.org/abs/2607.01197v1)

**作者**：Chuanming Yu, Jiaming Liu, Zihao Ge 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-01

### 📄 论文摘要

Quantum computing has emerged as a promising computational paradigm for machine learning (ML), with the potential to offer computational advantages over classical approaches. At this stage, the evidence supporting the performance and advantages of quantum machine learning (QML) models relative to classical models is insufficient.To address this gap, this paper presents an empirical study on the performance of QML models and their classical counterparts. We compare seven model pairs spanning supervised learning and reinforcement learning. Our results indicate that the evaluated quantum machine learning models do not yet surpass the classical baselines in overall prediction performance, policy stability, or training time. Nevertheless, QML remains a promising approach for filtering noise and controlling false positives. Our research findings summarize the challenges facing quantum machine learning across hardware environments, training efficiency, and convergence stability, providing a foundation for research into the robustness and parameter optimization of QML. This work is publicly available at https://github.com/Z-537-437/QML.

### 🤖 AI 总结

**一句话总结**：Quantum computing has emerged as a promising computational paradigm for machine learning (ML), with the potential to offer computational advantages over classical approaches. At this stage, the eviden...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：vs, Quantum, Classical, Machine, Learning, Unified, Empirical, Comparison

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01197v1) | [下载PDF](https://arxiv.org/pdf/2607.01197v1.pdf)

---

## [22. Neural Certificate Pricing for Combinatorial Optimization Problems](https://arxiv.org/abs/2607.01185v1)

**作者**：Jingyi Chen, Xinyuan Zhang, Xinwu Qian  
**分类**：cs.LG  
**发布时间**：2026-07-01

### 📄 论文摘要

Combinatorial optimization (CO) problems are difficult because certifiable discrete structure induces exponential search. One needs to search over the set exponentially many candidates to certify optimality, however, the structural feasibility of a path, packing, or cover can be verified in polynomial time once supplied. In this study, we introduce Neural Certificate Pricing (NCP) that exploits this asymmetry under an unsupervised learning framework. A neural network is trained to predict certificate-level dual prices, while a structured recovery layer constructs the induced primal marginal. NCP can be viewed as amortized separation: instead of enumerating violated inequalities, it learns the residual prices through which their aggregate effect enters recovery. When the certificate-consistency condition holds, the recovered marginal is globally feasible, and a local theory shows that first-order errors in the predicted price induce only second-order loss in objective value. Across three classes of CO problems, NCP either outperforms state-of-the-art neural baselines by large margins or matches them at a fraction of the computation time, and shows stronger out-of-distribution generalization.

### 🤖 AI 总结

**一句话总结**：Combinatorial optimization (CO) problems are difficult because certifiable discrete structure induces exponential search. One needs to search over the set exponentially many candidates to certify opti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CO, Neural, Certificate, Pricing, Combinatorial, Optimization, Problems, difficult

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01185v1) | [下载PDF](https://arxiv.org/pdf/2607.01185v1.pdf)

---

## [23. Right in the Right Way: LM Training with Verifiable Rewards and Human Demonstrations](https://arxiv.org/abs/2607.01181v1)

**作者**：Mehul Damani, Isha Puri, Idan Shenfeld 等 4 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-07-01

### 📄 论文摘要

RL with verifiable rewards (RLVR) has emerged as a powerful paradigm for training LMs on tasks with well-defined success metrics, such as code generation and mathematical reasoning. However, current RLVR methods optimize only what can be objectively scored, often neglecting subjective, non-verifiable aspects of human-like outputs, such as style and structure. This limitation leads to well-documented failure modes such as diversity collapse, unnatural-sounding responses, and reward hacking. We propose an adversarial generator-discriminator framework that augments verifiable rewards with a learned signal from human demonstrations. A generator model is trained using RL to maximize both task accuracy and an adversarial reward derived from a discriminator. The discriminator, trained alongside the generator policy, learns to distinguish human-written outputs from model-generated ones. The discriminator serves as a learned proxy for the human output distribution, providing feedback on aspects of generation that are difficult to formalize as scalar rewards. Across diverse domains, including bug fixing and open-ended generation, our approach consistently improves non-verifiable properties while preserving the accuracy gains of RLVR. In bug fixing, our method produces solutions with significantly lower edit distance compared to RLVR baselines while matching end performance. In story generation, our method significantly improves win rate while producing stories that are diverse and more human-like. And in a simple reward hacking benchmark, our method nearly eliminates model misbehavior while maintaining high benchmark scores. Together, these results show that our approach bridges RL and SFT, offering a scalable path toward jointly optimizing the verifiable and non-verifiable properties of a task.

### 🤖 AI 总结

**一句话总结**：RL with verifiable rewards (RLVR) has emerged as a powerful paradigm for training LMs on tasks with well-defined success metrics, such as code generation and mathematical reasoning. However, current R...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LM, Right, Way, Training, Verifiable, Rewards, Human, Demonstrations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01181v1) | [下载PDF](https://arxiv.org/pdf/2607.01181v1.pdf)

---

## [24. QuasiMoTTo: Quasi-Monte Carlo Test-Time Scaling](https://arxiv.org/abs/2607.01179v1)

**作者**：Michael Y. Li, Anthony Zhan, Kanishk Gandhi 等 5 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-07-01

### 📄 论文摘要

Scaling inference compute, by generating many parallel attempts per problem, is a costly but reliable lever for improving language model capabilities. By default these attempts are generated independently, wasting inference compute on redundant solutions. This waste seems unavoidable. After all, independence is what makes parallel sampling trivial to scale. However, this tradeoff is not fundamental: there is a rich design space of samplers that generate correlated but exact samples entirely in parallel. We explore this design space as an avenue for improving sample efficiency in scaling inference compute and reinforcement learning (RL). Concretely, we introduce QuasiMoTTo, which uses correlated samples as a drop-in replacement for i.i.d. samples. To generate these samples, QuasiMoTTo uses a reparameterization of autoregressive sampling as inverse-CDF sampling and draws the underlying uniforms with quasi-Monte Carlo (QMC); because QMC spreads the uniforms out more evenly than i.i.d., the resulting samples cover the output space with far less redundancy. Even though the batch is correlated, each sample is marginally distributed according to the language model, so we can use the batch for policy-gradient training. Our empirical analysis focuses on understanding how efficiently QuasiMoTTo can turn compute into performance. To evaluate correlated samplers, whose dependence breaks standard pass@k estimators, we first develop an unbiased bootstrap estimator. Across four reasoning benchmarks, QuasiMoTTo matches i.i.d. pass@k accuracy with 25-47% fewer samples. Strikingly, QuasiMoTTo often saturates an upper bound on pass@k that holds for any marginal-preserving sampler. We also apply QuasiMoTTo to policy-gradient RL (GRPO) where it matches i.i.d. performance with 50% fewer training steps. These gains come from higher coverage, which yields a stronger learning signal per batch.

### 🤖 AI 总结

**一句话总结**：Scaling inference compute, by generating many parallel attempts per problem, is a costly but reliable lever for improving language model capabilities. By default these attempts are generated independe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：QuasiMoTTo, Quasi-Monte, Carlo, Test-Time, Scaling, inference, compute, generating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01179v1) | [下载PDF](https://arxiv.org/pdf/2607.01179v1.pdf)

---

## [25. Decision-Aware Training for Sample-Based Generative Models](https://arxiv.org/abs/2607.01171v1)

**作者**：Kornelius Raeth, Nicole Ludwig  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-07-01

### 📄 论文摘要

Sample-based generative models are increasingly used for probabilistic forecasting in high-stakes decision settings, yet their training objectives are blind to the decision maker's cost structure. These models are commonly trained with strictly proper scoring rules, such as the energy score, which allocate their training signal in proportion to data density, with no awareness of where forecast errors are most costly for downstream decisions. We therefore propose decision-aware training for sample-based generative models, augmenting the energy score objective with a differentiable decision loss that directly penalises the cost incurred by acting on the model's forecast. This combined loss is theoretically grounded, as the decision loss is itself a proper scoring rule. We validate our method on one synthetic and two real-world tasks, showing targeted improvements in cost-sensitive regions while retaining full probabilistic forecasts.

### 🤖 AI 总结

**一句话总结**：Sample-based generative models are increasingly used for probabilistic forecasting in high-stakes decision settings, yet their training objectives are blind to the decision maker's cost structure. The...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Decision-Aware, Training, Sample-Based, Generative, Models, increasingly, used, probabilistic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01171v1) | [下载PDF](https://arxiv.org/pdf/2607.01171v1.pdf)

---

## [26. Efficient Compression of Structured and Unstructured Volumes via Learned 3D Gaussian Representation](https://arxiv.org/abs/2607.01164v1)

**作者**：Landon Dyken, Sharmistha Chakrabarti, Nathan Debardeleben 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-07-01

### 📄 论文摘要

Recent work has shown that implicit neural representations (INRs) can be trained to effectively compress structured and unstructured volume data, allowing for direct data querying with a reduced memory footprint. However, as existing INRs for unstructured volumes do not encode geometry, they require partial mesh storage for later sampling, limiting achievable compression. At the same time, novel view synthesis methods have shown that explicit collections of 3D Gaussians can be used to accurately visualize volume data. In this work, we introduce an explicit model for volume data compression based on 3D Gaussian primitives. We reinterpret collections of 3D Gaussians as an explicit representation of a scalar field and use a sampling strategy that reconstructs scalar values at spatial locations through weighted aggregation of intersecting Gaussians. We develop optimized CUDA-accelerated pipelines for structured and unstructured model sampling, loss functions that encourage accurate domain encoding by our models, and a novel sampling-error based densification strategy. Our explicit formulation naturally encodes domain geometry, eliminating the need for mesh storage in unstructured volumes and introducing significantly higher compression opportunities. Compared to existing INRs, we demonstrate that our explicit model achieves competitive reconstruction quality with significant training speedups on structured volumes, while markedly outperforming in all metrics on unstructured volumes.

### 🤖 AI 总结

**一句话总结**：Recent work has shown that implicit neural representations (INRs) can be trained to effectively compress structured and unstructured volume data, allowing for direct data querying with a reduced memor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Efficient, Compression, Structured, Unstructured, Volumes, via, Learned

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01164v1) | [下载PDF](https://arxiv.org/pdf/2607.01164v1.pdf)

---

## [27. A Lightweight Self-Supervised Learning Framework for Multivariate Time Series using Hierarchical-JEPA on ECG Data](https://arxiv.org/abs/2607.01145v1)

**作者**：Siwon Kim  
**分类**：cs.LG, eess.SP  
**发布时间**：2026-07-01

### 📄 论文摘要

Data analysis in the medical domain often encounters scenarios involving a limited target dataset and a large, unannotated dataset with a general distribution. Under such circumstances, self-supervised learning (SSL) methods are highly effective for utilizing large datasets, making them a popular choice for electrocardiogram (ECG) analysis. This work presents the Event Reconstruction Joint-Embedding Predictive Architecture (ER-JEPA), a lightweight SSL framework for multivariate time series, whose name and two-fold hierarchical structure are inspired by the diagnostic approach of cardiologists. At its core, ER-JEPA features: (1) a two-stage structure that constructs representations for each time interval and subsequently processes these representations as a univariate time series, (2) the hierarchical integration of two Joint-Embedding Predictive Architectures (JEPAs), and (3) a Vision Transformer (ViT) backbone. The structural concatenation of two JEPAs categorizes the model as a Hierarchical JEPA (H-JEPA), designed to encode multiple levels of abstract representations for enhanced prediction on complex tasks. This study reports a successful application of H-JEPA to 12-lead ECG data as a multivariate time series alongside an analysis of the sensitivity of hierarchical representation during the pretraining stage. Pretrained on approximately 180,000 10-second recordings, the model achieves state-of-the-art downstream performance on the ST-MEM benchmark, with rapid computation and minimal resource usage.

### 🤖 AI 总结

**一句话总结**：Data analysis in the medical domain often encounters scenarios involving a limited target dataset and a large, unannotated dataset with a general distribution. Under such circumstances, self-supervise...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Lightweight, Self-Supervised, Learning, Framework, Multivariate, Time, Series, Hierarchical-JEPA

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01145v1) | [下载PDF](https://arxiv.org/pdf/2607.01145v1.pdf)

---

## [28. Sequentially-Controlled Interactive Multi-Particle Flow-Maps for Online Feedback-Driven Search](https://arxiv.org/abs/2607.01144v1)

**作者**：Binglin Ji, Anindya Sarkar, Hengchang Lu 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CE  
**发布时间**：2026-07-01

### 📄 论文摘要

While generative models have enabled training-free reward alignment, current methods typically excel in local exploration within narrow regions of the underlying distribution. These approaches struggle when preferences are unknown a priori and only revealed through sequential feedback-a scenario demanding broad exploration to uncover high-utility regions. To address this, we propose Sequentially-Controlled Interactive Multi-Particle Flow-Maps (IMPFM), a framework for sample-efficient online feedback-driven search. IMPFM progressively transports a group of interactive particles toward the target distribution, maintaining the broad coverage essential for heterogeneous preference alignment. IMPFM introduces a principled and efficient posterior sample sharing mechanism across particles powered by flow maps. By correcting individual particle drift with the collective posterior samples of the entire ensemble at each resampling step, the framework maximizes sample utility to enable global exploration while actively mitigating reward over-optimization, typical of standard control frameworks. Paired with a principled exploration-exploitation reweighting mechanism involving multi-particle interaction, this sequentially corrected multi-particle dynamics explicitly preserves structural diversity and overcomes the weight degeneracy inherent to standard SMC samplers. Crucially, we prove that the resulting sampling framework yields a multi-particle interaction-aware Feynman-Kac corrector that progressively steers the multi-particle system toward a KL-tilted target distribution, facilitating global exploration and preventing mode collapse. Extensive empirical evaluations and rigorous ablations across diverse search and alignment tasks confirm the efficacy of IMPFM over existing baselines.

### 🤖 AI 总结

**一句话总结**：While generative models have enabled training-free reward alignment, current methods typically excel in local exploration within narrow regions of the underlying distribution. These approaches struggl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sequentially-Controlled, Interactive, Multi-Particle, Flow-Maps, Online, Feedback-Driven, Search, While

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01144v1) | [下载PDF](https://arxiv.org/pdf/2607.01144v1.pdf)

---

## [29. ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed Low-Rank Subspaces](https://arxiv.org/abs/2607.01125v1)

**作者**：Xun Dong, Yibo Xu, Naigang Wang 等 6 位作者  
**分类**：cs.LG, math.OC  
**发布时间**：2026-07-01

### 📄 论文摘要

Zeroth-order (ZO) optimization enables fine-tuning large language models when backpropagation is unavailable or memory-prohibitive, but existing methods often perturb full model weights or randomly constructed low-dimensional subspaces, yielding high-variance estimates and limited performance. We propose ZO-Act, an activation-informed ZO fine-tuning method that restricts perturbations to a fixed low-rank subspace derived from input activations. For each linear layer, ZO-Act computes a small activation basis once at initialization and optimizes only lightweight coefficient matrices using forward-only loss evaluations. This reduces the effective perturbation dimension, exposes explicit trainable variables compatible with momentum-based optimizers such as Adam, and naturally supports quantized LLM fine-tuning by keeping low-bit weights frozen. We analyze ZO-Act as zeroth-order optimization over a restricted coefficient space and show that perturbing the low-dimensional coefficients reduces both the variance-dependent convergence term and the finite-difference error of the ZO estimator, at the cost of a controlled subspace approximation bias that is mitigated by the low-rank structure of LLM activations and gradients. Experiments on Llama-3-8B, OPT-13B, and INT4 Llama-3-8B show consistent gains over strong ZO fine-tuning baselines across language understanding, question answering, and commonsense reasoning.

### 🤖 AI 总结

**一句话总结**：Zeroth-order (ZO) optimization enables fine-tuning large language models when backpropagation is unavailable or memory-prohibitive, but existing methods often perturb full model weights or randomly co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ZO-Act, Efficient, Zeroth-Order, Fine-Tuning, via, One-Shot, Activation-Informed, Low-Rank

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01125v1) | [下载PDF](https://arxiv.org/pdf/2607.01125v1.pdf)

---

## [30. Muon as a Residual Connection](https://arxiv.org/abs/2607.01124v1)

**作者**：Hao Huang  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-01

### 📄 论文摘要

Muon has recently emerged as one of the most effective optimizers for training large neural networks, yet its empirical success has been explained from several different perspectives. In this paper, we propose a simple mechanistic interpretation: Muon can be understood as an implicit residual connection during training. Specifically, orthogonalizing the update can sacrifice some immediate gradient fidelity while improving representation preservation for downstream layers. We study this trade-off in controlled linear optimization settings, where Muon can learn representations that are slower to fit a local target but easier for downstream layers to exploit. Our results suggest a conceptual explanation for Muon and a design perspective for optimizers that balance local descent with downstream usability.

### 🤖 AI 总结

**一句话总结**：Muon has recently emerged as one of the most effective optimizers for training large neural networks, yet its empirical success has been explained from several different perspectives. In this paper, w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Muon, Residual, Connection, has, recently, emerged, one

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.01124v1) | [下载PDF](https://arxiv.org/pdf/2607.01124v1.pdf)

---

