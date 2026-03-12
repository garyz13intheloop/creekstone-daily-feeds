# arXiv AI 论文日报 | 2026-03-11

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (8 篇)
- [cs.CV](#csCV) (5 篇)
- [cs.CL](#csCL) (2 篇)

---

## cs.CL

## [1. GR-SAP: Generative Replay for Safety Alignment Preservation during Fine-Tuning](https://arxiv.org/abs/2603.10243v1)

**作者**：Zhouxiang Fang, Jiawei Zhou, Hanjie Chen  
**分类**：cs.CL  
**发布时间**：2026-03-10

### 📄 论文摘要

Recent studies show that the safety alignment of large language models (LLMs) can be easily compromised even by seemingly non-adversarial fine-tuning. To preserve safety alignment during fine-tuning, a widely used strategy is to jointly optimize safety and task objectives by mixing in the original alignment data, which is typically inaccessible even for open-weight LLMs. Inspired by generative replay in continual learning, we propose Generative Replay for Safety Alignment Preservation (GR-SAP), a unified framework that synthesizes domain-specific alignment data from LLMs and integrate them during downstream adaption to preserve safety alignment. Theoretical and empirical analyses demonstrate this synthetic data serves as a reliable proxy for the original alignment data. Experiments across various models and downstream tasks show that GR-SAP substantially mitigates fine-tuning-induced safety degradation while maintaining comparable downstream performance. Our code is available at https://github.com/chili-lab/gr-sap.

### 🤖 AI 总结

**一句话总结**：GR-SAP通过“生成式回放”在微调时合成并混入安全对齐数据，在不访问原始对齐数据的情况下显著缓解安全性退化且保持任务性能。

**研究动机**：LLM在看似无害的下游微调中也可能快速丢失安全对齐，而常用的“混入原始安全对齐数据”策略往往因数据不可得（即便开源权重）而难以实施。

**核心方法**：借鉴持续学习的generative replay，GR-SAP让模型生成领域相关的合成对齐/安全数据作为原始对齐数据的代理，并在下游适配训练时与任务数据联合优化以维持安全约束。

**主要结论**：理论与实证结果表明合成对齐数据能可靠替代原始对齐数据；在多模型、多任务实验中，GR-SAP显著降低微调引发的安全降级，同时下游性能与常规微调相比基本可比。

**关键词**：安全对齐保持, 微调安全退化, 生成式回放, 持续学习, 合成对齐数据, 领域对齐数据生成, 下游任务适配, 安全-任务联合优化, 开源权重LLM

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10243v1) | [下载PDF](https://arxiv.org/pdf/2603.10243v1.pdf)

---

## [2. S-GRADES -- Studying Generalization of Student Response Assessments in Diverse Evaluative Settings](https://arxiv.org/abs/2603.10233v1)

**作者**：Tasfia Seuti, Sagnik Ray Choudhury  
**分类**：cs.CL  
**发布时间**：2026-03-10

### 📄 论文摘要

Evaluating student responses, from long essays to short factual answers, is a key challenge in educational NLP. Automated Essay Scoring (AES) focuses on holistic writing qualities such as coherence and argumentation, while Automatic Short Answer Grading (ASAG) emphasizes factual correctness and conceptual understanding. Despite their shared goal, these paradigms have progressed in isolation with fragmented datasets, inconsistent metrics, and separate communities. We introduce S-GRADES (Studying Generalization of Student Response Assessments in Diverse Evaluative Settings), a web-based benchmark that consolidates 14 diverse grading datasets under a unified interface with standardized access and reproducible evaluation protocols. The benchmark is fully open-source and designed for extensibility, enabling continuous integration of new datasets and evaluation settings. To demonstrate the utility of S-GRADES, we evaluate three state-of-the-art large language models across the benchmark using multiple reasoning strategies in prompting. We further examine the effects of exemplar selection and cross-dataset exemplar transfer. Our analyses illustrate how benchmark-driven evaluation reveals reliability and generalization gaps across essay and short-answer grading tasks, highlighting the importance of standardized, cross-paradigm assessment.

### 🤖 AI 总结

**一句话总结**：S-GRADES 将作文评分（AES）与短答评分（ASAG）等14个学生作答评测数据集统一到一个可复现的开放基准中，用于系统检验大模型在不同评分场景下的泛化与可靠性。

**研究动机**：现有AES与ASAG研究长期割裂，数据集分散、指标不一致、评测协议不统一，导致模型能力难以横向比较与验证泛化。需要一个跨范式、标准化、可扩展的基准来揭示不同评估设置下的性能差距与可靠性问题。

**核心方法**：构建Web端开放源代码基准S-GRADES，整合14个多样化评分数据集，提供统一接口、标准化访问与可复现评测协议，并支持持续扩展新数据与新设置。用多种提示推理策略评测三种SOTA大语言模型，同时分析示例（exemplar）选择以及跨数据集示例迁移对结果的影响。

**主要结论**：基准驱动评测显示：大模型在作文与短答等不同评分任务间存在明显的可靠性与泛化缺口，且对提示策略与示例选择较敏感。标准化、跨范式的统一评测对于真实刻画模型能力与推进学生作答自动评估研究至关重要。

**关键词**：教育NLP评测, 学生作答自动评分, 作文自动评分（AES）, 短答案自动评分（ASAG）, 评分泛化能力, 跨数据集评测, 评测基准构建, 数据集整合, 标准化评测协议, 可复现评测, 提示推理策略, 示例选择与迁移

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10233v1) | [下载PDF](https://arxiv.org/pdf/2603.10233v1.pdf)

---

## cs.CV

## [3. A Robust Deep Learning Framework for Bangla License Plate Recognition Using YOLO and Vision-Language OCR](https://arxiv.org/abs/2603.10267v1)

**作者**：Nayeb Hasin, Md. Arafath Rahman Nishat, Mainul Islam 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-10

### 📄 论文摘要

An Automatic License Plate Recognition (ALPR) system constitutes a crucial element in an intelligent traffic management system. However, the detection of Bangla license plates remains challenging because of the complicated character scheme and uneven layouts. This paper presents a robust Bangla License Plate Recognition system that integrates a deep learning-based object detection model for license plate localization with Optical Character Recognition for text extraction. Multiple object detection architectures, including U-Net and several YOLO (You Only Look Once) variants, are compared for license plate localization. This study proposes a novel two-stage adaptive training strategy built upon the YOLOv8 architecture to improve localization performance. The proposed approach outperforms the established models, achieving an accuracy of 97.83% and an Intersection over Union (IoU) of 91.3%. The text recognition problem is phrased as a sequence generation problem with a VisionEncoderDecoder architecture, with a combination of encoder-decoders evaluated. It was demonstrated that the ViT + BanglaBERT model gives better results at the character level, with a Character Error Rate of 0.1323 and Word Error Rate of 0.1068. The proposed system also shows a consistent performance when tested on an external dataset that has been curated for this study purpose. The dataset offers completely different environment and lighting conditions compared to the training sample, indicating the robustness of the proposed framework. Overall, our proposed system provides a robust and reliable solution for Bangla license plate recognition and performs effectively across diverse real-world scenarios, including variations in lighting, noise, and plate styles. These strengths make it well suited for deployment in intelligent transportation applications such as automated law enforcement and access control.

### 🤖 AI 总结

**一句话总结**：本文提出一个面向孟加拉语车牌的两阶段深度学习ALPR框架：用改进的YOLOv8进行车牌定位，并用视觉-语言OCR进行序列生成式文本识别，在多场景下表现稳健。

**研究动机**：孟加拉语车牌字符体系复杂且排版不规则，导致传统或通用ALPR在定位与识别上鲁棒性不足，亟需在不同光照、噪声与车牌样式下仍可靠的端到端方案。

**核心方法**：在定位阶段对比U-Net与多种YOLO变体，并基于YOLOv8提出两阶段自适应训练策略以提升检测精度与IoU；在识别阶段将OCR建模为序列生成任务，采用VisionEncoderDecoder并评估不同编码器-解码器组合（如ViT + BanglaBERT）。

**主要结论**：所提框架在车牌定位上达到97.83%准确率与91.3% IoU，文本识别中ViT+BanglaBERT取得CER 0.1323与WER 0.1068；在与训练集环境/光照显著不同的外部数据集上仍保持稳定性能，显示出较强的跨场景鲁棒性与落地潜力。

**关键词**：孟加拉语车牌识别, 自动车牌识别, 车牌定位, 目标检测, 两阶段自适应训练, 光学字符识别（OCR）, 视觉-语言OCR, 视觉编码器-解码器, 序列生成, 跨域鲁棒性评测

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10267v1) | [下载PDF](https://arxiv.org/pdf/2603.10267v1.pdf)

---

## [4. Joint Imaging-ROI Representation Learning via Cross-View Contrastive Alignment for Brain Disorder Classification](https://arxiv.org/abs/2603.10253v1)

**作者**：Wei Liang, Lifang He  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-10

### 📄 论文摘要

Brain imaging classification is commonly approached from two perspectives: modeling the full image volume to capture global anatomical context, or constructing ROI-based graphs to encode localized and topological interactions. Although both representations have demonstrated independent efficacy, their relative contributions and potential complementarity remain insufficiently understood. Existing fusion approaches are typically task-specific and do not enable controlled evaluation of each representation under consistent training settings. To address this gap, we propose a unified cross-view contrastive framework for joint imaging-ROI representation learning. Our method learns subject-level global (imaging) and local (ROI-graph) embeddings and aligns them in a shared latent space using a bidirectional contrastive objective, encouraging representations from the same subject to converge while separating those from different subjects. This alignment produces comparable embeddings suitable for downstream fusion and enables systematic evaluation of imaging-only, ROI-only, and joint configurations within a unified training protocol. Extensive experiments on the ADHD-200 and ABIDE datasets demonstrate that joint learning consistently improves classification performance over either branch alone across multiple backbone choices. Moreover, interpretability analyses reveal that imaging-based and ROI-based branches emphasize distinct yet complementary discriminative patterns, explaining the observed performance gains. These findings provide principled evidence that explicitly integrating global volumetric and ROI-level representations is a promising direction for neuroimaging-based brain disorder classification. The source code is available at https://anonymous.4open.science/r/imaging-roi-contrastive-152C/.

### 🤖 AI 总结

**一句话总结**：提出一种跨视角对比学习框架，将全脑影像与ROI图两种表示对齐到共享潜空间，从而在统一训练协议下实现更强的脑疾病分类。

**研究动机**：现有脑影像分类常分别依赖全局体素影像或局部ROI图，两者贡献与互补性缺乏在一致训练设置下的可控比较与系统评估。已有融合方法多为任务特定，难以公平评估“单分支 vs 联合”的真实收益。

**核心方法**：构建影像分支（学习subject-level全局embedding）与ROI-图分支（学习局部/拓扑embedding），并用双向对比学习目标进行跨视角对齐：同一受试者跨视图表示拉近、不同受试者拉远。对齐后的可比embedding支持影像-only、ROI-only与联合/融合配置在同一框架内训练与对照。

**主要结论**：在ADHD-200与ABIDE上，联合学习在多种backbone下均稳定优于任一单分支，说明全局体积信息与ROI拓扑信息具有互补性。可解释性分析进一步表明两分支关注的判别模式不同且互补，从机制上解释了性能提升。

**关键词**：神经影像分类, 脑疾病分类, 跨视角对比学习, 联合表征学习, 全脑体积表征, ROI 图表示, 共享潜空间嵌入, 多分支融合评测框架, 模型可解释性分析, ADHD-200 数据集

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10253v1) | [下载PDF](https://arxiv.org/pdf/2603.10253v1.pdf)

---

## [5. One Adapter for All: Towards Unified Representation in Step-Imbalanced Class-Incremental Learning](https://arxiv.org/abs/2603.10237v1)

**作者**：Xiaoyan Zhang, Jiangpeng He  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-10

### 📄 论文摘要

Class-incremental learning (CIL) aims to acquire new classes over time while retaining prior knowledge, yet most setups and methods assume balanced task streams. In practice, the number of classes per task often varies significantly. We refer to this as step imbalance, where large tasks that contain more classes dominate learning and small tasks inject unstable updates. Existing CIL methods assume balanced tasks and therefore treat all tasks uniformly, producing imbalanced updates that degrade overall learning performance. To address this challenge, we propose One-A, a unified and imbalance-aware framework that incrementally merges task updates into a single adapter, maintaining constant inference cost. One-A performs asymmetric subspace alignment to preserve dominant subspaces learned from large tasks while constraining low-information updates within them. An information-adaptive weighting balances the contribution between base and new adapters, and a directional gating mechanism selectively fuses updates along each singular direction, maintaining stability in head directions and plasticity in tail ones. Across multiple benchmarks and step-imbalanced streams, One-A achieves competitive accuracy with significantly low inference overhead, showing that a single, asymmetrically fused adapter can remain both adaptive to dynamic task sizes and efficient at deployment.

### 🤖 AI 总结

**一句话总结**：提出One-A框架，用单个适配器在“每步类别数不均衡”的类增量学习中统一融合各任务更新，在保持常量推理开销的同时提升稳定性与准确率。

**研究动机**：现有CIL方法大多默认任务流类别数均衡，但现实中常出现“大任务主导、小任务更新不稳定”的step imbalance，导致对所有任务一视同仁的更新策略产生失衡梯度并损害总体性能。

**核心方法**：One-A将每个任务的更新增量式合并进同一个adapter，通过非对称子空间对齐保留大任务学到的主导子空间并约束小任务低信息更新；再用信息自适应加权与按奇异方向的门控融合机制，在“头部方向”保持稳定、在“尾部方向”保持可塑性。

**主要结论**：在多个基准与step-imbalanced任务流上，One-A以显著更低的推理开销获得具有竞争力的准确率，证明单一且非对称融合的adapter能同时适应动态任务规模并便于高效部署。

**关键词**：类增量学习, 持续学习, 步长不均衡, 任务流不平衡, 适配器融合, 单适配器, 非对称子空间对齐, 信息自适应加权, 方向门控, 奇异值分解, 恒定推理开销

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10237v1) | [下载PDF](https://arxiv.org/pdf/2603.10237v1.pdf)

---

## [6. Why Does It Look There? Structured Explanations for Image Classification](https://arxiv.org/abs/2603.10234v1)

**作者**：Jiarui Li, Zixiang Yin, Samuel J Landry 等 5 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-10

### 📄 论文摘要

Deep learning models achieve remarkable predictive performance, yet their black-box nature limits transparency and trustworthiness. Although numerous explainable artificial intelligence (XAI) methods have been proposed, they primarily provide saliency maps or concepts (i.e., unstructured interpretability). Existing approaches often rely on auxiliary models (\eg, GPT, CLIP) to describe model behavior, thereby compromising faithfulness to the original models. We propose Interpretability to Explainability (I2X), a framework that builds structured explanations directly from unstructured interpretability by quantifying progress at selected checkpoints during training using prototypes extracted from post-hoc XAI methods (e.g., GradCAM). I2X answers the question of "why does it look there" by providing a structured view of both intra- and inter-class decision making during training. Experiments on MNIST and CIFAR10 demonstrate effectiveness of I2X to reveal prototype-based inference process of various image classification models. Moreover, we demonstrate that I2X can be used to improve predictions across different model architectures and datasets: we can identify uncertain prototypes recognized by I2X and then use targeted perturbation of samples that allows fine-tuning to ultimately improve accuracy. Thus, I2X not only faithfully explains model behavior but also provides a practical approach to guide optimization toward desired targets.

### 🤖 AI 总结

**一句话总结**：I2X将GradCAM等后验可解释性产生的“非结构化关注区域”转化为训练过程中可追踪的“原型”与结构化解释，从而回答模型为何看向某处并可据此提升分类性能。

**研究动机**：现有XAI多停留在显著性图/概念等非结构化解释，且常借助GPT/CLIP等辅助模型生成描述，可能削弱对原模型的忠实性与可验证性。作者希望直接从原模型的解释信号中构建结构化、随训练演化的解释框架，以提升透明度与可用性。

**核心方法**：提出Interpretability to Explainability (I2X)：在训练的多个检查点提取GradCAM等方法得到的关注模式并聚类为“原型”，量化原型随训练的形成与变化，构建类内/类间决策依据的结构化视图。进一步识别不确定/混淆原型，对对应样本做定向扰动并微调模型，以引导优化并提升准确率。

**主要结论**：在MNIST与CIFAR10上，I2X能揭示不同分类模型的原型式推理过程，提供更结构化且更忠实于模型本身的解释。利用I2X定位不确定原型并进行针对性微调，还可在不同架构与数据集上带来预测性能提升。

**关键词**：可解释人工智能, 结构化解释, 图像分类, 后验解释, 显著性图, 原型学习, 训练过程分析, 类内决策, 类间决策, 不确定性原型, 定向扰动微调

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10234v1) | [下载PDF](https://arxiv.org/pdf/2603.10234v1.pdf)

---

## [7. OilSAM2: Memory-Augmented SAM2 for Scalable SAR Oil Spill Detection](https://arxiv.org/abs/2603.10231v1)

**作者**：Shuaiyu Chen, Ming Yin, Peng Ren 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-10

### 📄 论文摘要

Segmenting oil spills from Synthetic Aperture Radar (SAR) imagery remains challenging due to severe appearance variability, scale heterogeneity, and the absence of temporal continuity in real world monitoring scenarios. While foundation models such as Segment Anything (SAM) enable prompt driven segmentation, existing SAM based approaches operate on single images and cannot effectively reuse information across scenes. Memory augmented variants (e.g., SAM2) further assume temporal coherence, making them prone to semantic drift when applied to unordered SAR image collections. We propose OilSAM2, a memory augmented segmentation framework tailored for unordered SAR oil spill monitoring. OilSAM2 introduces a hierarchical feature aware multi scale memory bank that explicitly models texture, structure, and semantic level representations, enabling robust cross image information reuse. To mitigate memory drift, we further propose a structure semantic consistent memory update strategy that selectively refreshes memory based on semantic discrepancy and structural variation.Experiments on two public SAR oil spill datasets demonstrate that OilSAM2 achieves state of the art segmentation performance, delivering stable and accurate results under noisy SAR monitoring scenarios. The source code is available at https://github.com/Chenshuaiyu1120/OILSAM2.

### 🤖 AI 总结

**一句话总结**：OilSAM2 面向无序SAR油污监测，引入分层多尺度记忆库与一致性更新策略，在跨图像复用信息的同时抑制记忆漂移，从而提升油污分割精度与稳定性。

**研究动机**：SAR油污外观差异大、尺度多样且真实监测缺乏时间连续性，导致单图SAM难以跨场景泛化；而依赖时序一致性的SAM2在无序图像集合上易发生语义漂移。

**核心方法**：提出层次化、特征感知的多尺度记忆库，分别建模纹理/结构/语义表征以实现跨图像信息复用；并设计结构-语义一致的记忆更新机制，根据语义差异与结构变化选择性刷新记忆以减少漂移。

**主要结论**：在两个公开SAR油污数据集上，OilSAM2 达到SOTA分割表现，并在噪声较强、场景无序的监测条件下输出更稳定、更准确的检测结果。

**关键词**：SAR油膜分割, 油膜泄漏检测, 提示驱动分割, 基础模型分割, 记忆增强分割, 多尺度记忆库, 层级特征表示, 语义漂移抑制, 一致性记忆更新, 无序图像集合

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10231v1) | [下载PDF](https://arxiv.org/pdf/2603.10231v1.pdf)

---

## cs.LG

## [8. GSVD for Geometry-Grounded Dataset Comparison: An Alignment Angle Is All You Need](https://arxiv.org/abs/2603.10283v1)

**作者**：Eduarda de Souza Marques, Arthur Sobrinho Ferreira da Rocha, Joao Paixao 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-10

### 📄 论文摘要

Geometry-grounded learning asks models to respect structure in the problem domain rather than treating observations as arbitrary vectors. Motivated by this view, we revisit a classical but underused primitive for comparing datasets: linear relations between two data matrices, expressed via the co-span constraint $Ax = By = z$ in a shared ambient space. To operationalize this comparison, we use the generalized singular value decomposition (GSVD) as a joint coordinate system for two subspaces. In particular, we exploit the GSVD form $A = HCU$, $B = HSV$ with $C^{\top}C + S^{\top}S = I$, which separates shared versus dataset-specific directions through the diagonal structure of $(C, S)$. From these factors we derive an interpretable *angle score* $θ(z) \in [0, π/2]$ for a sample $z$, quantifying whether z is explained relatively more by $A$, more by $B$, or comparably by both. The primary role of $θ(z)$ is as a *per-sample geometric diagnostic*. We illustrate the behavior of the score on MNIST through angle distributions and representative GSVD directions. A binary classifier derived from $θ(z)$ is presented as an illustrative application of the score as an interpretable diagnostic tool.

### 🤖 AI 总结

**一句话总结**：提出用GSVD将两个数据集的子空间对齐，并通过一个可解释的“对齐角度”评分θ(z)逐样本诊断样本更偏向由哪个数据集解释。

**研究动机**：几何约束学习强调数据具有结构而非任意向量，因此需要一种能刻画两个数据矩阵线性关系与共享/特有方向的、可解释的数据集比较工具。

**核心方法**：利用GSVD将A、B分解为A=HCU、B=HSV且满足CᵀC+SᵀS=I，通过(C,S)的对角结构分离共享与数据集特定方向，并为每个样本z定义角度分数θ(z)∈[0,π/2]衡量其相对更被A或B解释；并展示基于θ(z)的简单二分类作为示例应用。

**主要结论**：角度分数θ(z)可作为逐样本的几何诊断指标，能在MNIST上通过角度分布与代表性GSVD方向直观揭示两数据集的共享/差异结构，并支持构建可解释的判别器。

**关键词**：广义奇异值分解（GSVD）, 数据集比较, 子空间对齐, 几何约束学习, 共张成约束（co-span）, 共享-特定方向分解, 样本级几何诊断, 可解释性诊断指标, 线性关系建模

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10283v1) | [下载PDF](https://arxiv.org/pdf/2603.10283v1.pdf)

---

## [9. Taming Score-Based Denoisers in ADMM: A Convergent Plug-and-Play Framework](https://arxiv.org/abs/2603.10281v1)

**作者**：Rajesh Shrestha, Xiao Fu  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-03-10

### 📄 论文摘要

While score-based generative models have emerged as powerful priors for solving inverse problems, directly integrating them into optimization algorithms such as ADMM remains nontrivial. Two central challenges arise: i) the mismatch between the noisy data manifolds used to train the score functions and the geometry of ADMM iterates, especially due to the influence of dual variables, and ii) the lack of convergence understanding when ADMM is equipped with score-based denoisers. To address the manifold mismatch issue, we propose ADMM plug-and-play (ADMM-PnP) with the AC-DC denoiser, a new framework that embeds a three-stage denoiser into ADMM: (1) auto-correction (AC) via additive Gaussian noise, (2) directional correction (DC) using conditional Langevin dynamics, and (3) score-based denoising. In terms of convergence, we establish two results: first, under proper denoiser parameters, each ADMM iteration is a weakly nonexpansive operator, ensuring high-probability fixed-point $\textit{ball convergence}$ using a constant step size; second, under more relaxed conditions, the AC-DC denoiser is a bounded denoiser, which leads to convergence under an adaptive step size schedule. Experiments on a range of inverse problems demonstrate that our method consistently improves solution quality over a variety of baselines.

### 🤖 AI 总结

**一句话总结**：提出一种将score-based去噪器稳定地嵌入ADMM的PnP框架（AC-DC denoiser），同时给出可收敛的迭代条件并在多种逆问题上提升重建质量。

**研究动机**：直接把score模型作为ADMM中的去噪先验会遇到“训练噪声流形”与“ADMM迭代几何（含对偶变量影响）”不匹配的问题，且缺乏带score去噪器的ADMM收敛理论保证。

**核心方法**：在ADMM-PnP中引入三阶段AC-DC去噪：先通过加性高斯噪声做auto-correction以对齐流形，再用条件Langevin动力学做directional correction修正迭代方向，最后执行score-based去噪；并证明在合适参数下迭代算子弱非扩张以获得高概率的定点球收敛，或在更宽松条件下把去噪器视为有界并配合自适应步长实现收敛。

**主要结论**：理论上给出了两类收敛保证（常数步长下的高概率球收敛与自适应步长下的收敛），实验上在多种逆问题设置中相较多种基线方法取得更稳定且更高质量的重建结果。

**关键词**：逆问题, 交替方向乘子法（ADMM）, 得分去噪器, AC-DC 去噪器, 流形不匹配, 条件朗之万动力学, 收敛性分析, 弱非扩张算子, 不动点球收敛, 自适应步长

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10281v1) | [下载PDF](https://arxiv.org/pdf/2603.10281v1.pdf)

---

## [10. Robust Post-Training for Generative Recommenders: Why Exponential Reward-Weighted SFT Outperforms RLHF](https://arxiv.org/abs/2603.10279v1)

**作者**：Keertana Chidambaram, Sanath Kumar Krishnamurthy, Qiuling Xu 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-10

### 📄 论文摘要

Aligning generative recommender systems to user preferences via post-training is critical for closing the gap between next-item prediction and actual recommendation quality. Existing post-training methods are ill-suited for production-scale systems: RLHF methods reward hack due to noisy user feedback and unreliable reward models, offline RL alternatives require propensity scores that are unavailable, and online interaction is infeasible. We identify exponential reward-weighted SFT with weights $w = \exp(r/λ)$ as uniquely suited to this setting, and provide the theoretical and empirical foundations that explain why. By optimizing directly on observed rewards without querying a learned reward model, the method is immune to reward hacking, requires no propensity scores, and is fully offline. We prove the first policy improvement guarantees for this setting under noisy rewards, showing that the gap scales only logarithmically with catalog size and remains informative even for large item catalogs. Crucially, we show that temperature $λ$ explicitly and quantifiably controls the robustness-improvement tradeoff, providing practitioners with a single interpretable regularization hyperparameter with theoretical grounding. Experiments on three open-source and one proprietary dataset against four baselines confirm that exponential reward weighting is simple, scalable, and consistently outperforms RLHF-based alternatives.

### 🤖 AI 总结

**一句话总结**：论文提出用指数奖励加权的监督微调（w=exp(r/λ)）做生成式推荐的离线后训练，比RLHF更稳健且效果更好。

**研究动机**：生产级推荐的用户反馈噪声大、奖励模型不可靠导致RLHF易“奖励黑客”，而离线RL常需不可得的倾向分（propensity）且在线交互成本高不可行。

**核心方法**：直接基于观测到的奖励对SFT样本做指数加权训练，避免查询/学习奖励模型并不依赖propensity；同时给出在噪声奖励下的策略改进理论保证，并用温度λ刻画可控的“稳健性-提升幅度”权衡。

**主要结论**：理论上证明该方法在噪声场景仍能带来策略改进，且性能差距对商品目录规模仅对数增长、适用于大规模catalog；实验在多个公开与私有数据集上也一致优于RLHF等基线，兼具简单、可扩展与稳健。

**关键词**：生成式推荐系统, 推荐对齐, 后训练, 指数奖励加权 SFT, 奖励黑客, 离线学习, 噪声奖励鲁棒性, 策略改进保证, 温度参数 λ, 大规模物品目录扩展性, 倾向评分

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10279v1) | [下载PDF](https://arxiv.org/pdf/2603.10279v1.pdf)

---

## [11. Estimating condition number with Graph Neural Networks](https://arxiv.org/abs/2603.10277v1)

**作者**：Erin Carson, Xinye Chen  
**分类**：cs.LG, math.NA  
**发布时间**：2026-03-10

### 📄 论文摘要

In this paper, we propose a fast method for estimating the condition number of sparse matrices using graph neural networks (GNNs). To enable efficient training and inference of GNNs, our proposed feature engineering for GNNs achieves $\mathrm{O}(\mathrm{nnz} + n)$, where $\mathrm{nnz}$ is the number of non-zero elements in the matrix and $n$ denotes the matrix dimension. We propose two prediction schemes for estimating the matrix condition number using GNNs. The extensive experiments for the two schemes are conducted for 1-norm and 2-norm condition number estimation, which show that our method achieves a significant speedup over the Hager-Higham and Lanczos methods.

### 🤖 AI 总结

**一句话总结**：提出用图神经网络快速估计稀疏矩阵的1范数/2范数条件数，在保持较低特征构造开销的同时显著加速相较传统算法的估计流程。

**研究动机**：传统条件数估计方法（如Hager-Higham、Lanczos）在大规模稀疏矩阵上计算成本较高，实际应用中需要更快的近似估计以服务数值线性代数与求解器选择/预处理等任务。

**核心方法**：将稀疏矩阵视为图结构输入GNN，并设计可在O(nnz+n)时间内完成的特征工程以支持高效训练与推理；同时提出两种基于GNN的预测方案来分别估计1范数与2范数条件数。

**主要结论**：在大量实验中，两种GNN估计方案在1范数与2范数条件数预测上均取得相对Hager-Higham与Lanczos方法的显著速度提升，表明GNN可作为高效的条件数近似估计器。

**关键词**：稀疏矩阵, 条件数估计, 图神经网络（GNN）, 矩阵图表示, 特征工程, 线性代数数值计算, 1-范数条件数, 2-范数条件数, 线性时间复杂度 O(nnz+n

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10277v1) | [下载PDF](https://arxiv.org/pdf/2603.10277v1.pdf)

---

## [12. Discovery of a Hematopoietic Manifold in scGPT Yields a Method for Extracting Performant Algorithms from Biological Foundation Model Internals](https://arxiv.org/abs/2603.10261v1)

**作者**：Ihor Kendiukhov  
**分类**：cs.LG, q-bio.CB, q-bio.GN  
**发布时间**：2026-03-10

### 📄 论文摘要

We report the discovery and extraction of a compact hematopoietic algorithm from the single-cell foundation model scGPT, to our knowledge the first biologically useful, competitive algorithm extracted from a foundation model via mechanistic interpretability. We show that scGPT internally encodes a compact hematopoietic manifold with significant developmental branch structure, validated on a strict non-overlap Tabula Sapiens external panel and confirmed via frozen-head zero-shot transfer to an independent multi-donor immune panel. To isolate this geometry, we introduce a general three-stage extraction method consisting of direct operator export from frozen attention weights, a lightweight learned adaptor, and a task-specific readout, producing a standalone algorithm without target-dataset retraining. In 88-split donor-holdout benchmarks against scVI, Palantir, DPT, CellTypist, PCA, and raw-expression baselines, the extracted algorithm achieves the strongest pseudotime-depth ordering and leads on key subtype endpoints (CD4/CD8 AUROC 0.867, mono/macro AUROC 0.951). Compared to standard probing of frozen scGPT embeddings with a 3-layer MLP, the extracted head is BH-significantly better on 6/8 classification endpoints while completing a full 12-split evaluation campaign 34.5x faster with approximately 1000x fewer trainable parameters. The exported operator compresses from three pooled attention heads to a single head without statistically significant loss, and further to a rank-64 surrogate. Mechanistic interpretability of the compact operator reveals a concentrated four-factor core explaining 66.2% of ablation impact, with factors resolving into explicit T/lymphoid, B/plasma, granulocytic, and monocyte/macrophage gene programs. A supplementary second-manifold validation (intercellular communication geometry) confirms that the extraction method generalizes beyond hematopoiesis.

### 🤖 AI 总结

**一句话总结**：论文从单细胞基础模型 scGPT 的内部机制中提取出一个紧凑的“造血流形/算法”，在多数据集零样本迁移下仍能高效完成拟时序与免疫细胞亚型判别，并显著加速评测与降低参数量。

**研究动机**：基础模型在生物任务上表现强但难以解释与复用；作者希望用机制可解释性从 scGPT 内部“导出”可独立运行、无需在目标数据集上再训练且仍具竞争力的生物算法。

**核心方法**：提出三阶段提取流程：从冻结的注意力权重直接导出算子（operator export）以捕捉造血几何结构，再训练一个轻量适配器（adaptor），最后加上任务特定读出头（readout）形成独立算法。并通过压缩（多头到单头、再到低秩 rank-64）与消融/因素分解，定位核心基因程序因子来解释算子机理。

**主要结论**：提取算法在严格外部非重叠面板与独立免疫面板上实现零样本验证，在供体留出基准中拟时序排序与关键亚型分类（如 CD4/CD8、单核/巨噬）优于或媲美 scVI/Palantir/DPT/CellTypist 等，并相对冻结嵌入+MLP 探针以更少参数获得更好结果且评测快 34.5 倍；机制分析揭示由四类细胞谱系相关基因程序构成的核心因子解释了大部分性能贡献，且方法可推广到第二类流形（细胞间通讯几何）。

**关键词**：机制可解释性, 基础模型算法抽取, 注意力权重导出算子, 冻结模型探针, 轻量适配器, 低秩近似, 单细胞基础模型, 造血分化流形, 伪时间排序, 零样本迁移, 供体留出评测

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10261v1) | [下载PDF](https://arxiv.org/pdf/2603.10261v1.pdf)

---

## [13. Improving TabPFN's Synthetic Data Generation by Integrating Causal Structure](https://arxiv.org/abs/2603.10254v1)

**作者**：Davide Tugnoli, Andrea De Lorenzo, Marco Virgolin 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-10

### 📄 论文摘要

Synthetic tabular data generation addresses data scarcity and privacy constraints in a variety of domains. Tabular Prior-Data Fitted Network (TabPFN), a recent foundation model for tabular data, has been shown capable of generating high-quality synthetic tabular data. However, TabPFN is autoregressive: features are generated sequentially by conditioning on the previous ones, depending on the order in which they appear in the input data. We demonstrate that when the feature order conflicts with causal structure, the model produces spurious correlations that impair its ability to generate synthetic data and preserve causal effects. We address this limitation by integrating causal structure into TabPFN's generation process through two complementary approaches: Directed Acyclic Graph (DAG)-aware conditioning, which samples each variable given its causal parents, and a Completed Partially Directed Acyclic Graph (CPDAG)-based strategy for scenarios with partial causal knowledge. We evaluate these approaches on controlled benchmarks and six CSuite datasets, assessing structural fidelity, distributional alignment, privacy preservation, and Average Treatment Effect (ATE) preservation. Across most settings, DAG-aware conditioning improves the quality and stability of synthetic data relative to vanilla TabPFN. The CPDAG-based strategy shows moderate improvements, with effectiveness depending on the number of oriented edges. These results indicate that injecting causal structure into autoregressive generation enhances the reliability of synthetic tabular data.

### 🤖 AI 总结

**一句话总结**：通过将因果结构（DAG/CPDAG）注入TabPFN的自回归生成过程，可减少因特征顺序与因果方向冲突导致的伪相关，从而提升合成表格数据质量与因果效应保持能力。

**研究动机**：原版TabPFN按输入特征顺序自回归生成，若该顺序违背真实因果结构，会引入伪相关并削弱分布拟合、结构保真与因果效应（如ATE）保留。

**核心方法**：提出两种结合因果知识的生成策略：DAG-aware conditioning按每个变量的因果父节点进行条件采样；在只有部分因果信息时使用CPDAG-based策略，利用部分定向边约束生成顺序/条件关系。

**主要结论**：在受控基准与6个CSuite数据集上，DAG-aware conditioning在结构保真、分布对齐、隐私与ATE保持等指标上总体更优且更稳定；CPDAG策略带来中等改进，其收益随可定向边数量增加而更明显。

**关键词**：合成表格数据生成, 自回归生成, 特征顺序偏置, 因果结构注入, DAG 条件生成, CPDAG 部分因果知识, 虚假相关, 结构保真度评估, 隐私保护评估, 平均处理效应（ATE）保真

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10254v1) | [下载PDF](https://arxiv.org/pdf/2603.10254v1.pdf)

---

## [14. SiMPO: Measure Matching for Online Diffusion Reinforcement Learning](https://arxiv.org/abs/2603.10250v1)

**作者**：Haitong Ma, Chenxiao Gao, Tianyi Chen 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-10

### 📄 论文摘要

A commonly used family of RL algorithms for diffusion policies conducts softmax reweighting over the behavior policy, which usually induces an over-greedy policy and fails to leverage feedback from negative samples. In this work, we introduce Signed Measure Policy Optimization (SiMPO), a simple and unified framework that generalizes reweighting scheme in diffusion RL with general monotonic functions. SiMPO revisits diffusion RL via a two-stage measure matching lens. First, we construct a virtual target policy by $f$-divergence regularized policy optimization, where we can relax the non-negativity constraint to allow for a signed target measure. Second, we use this signed measure to guide diffusion or flow models through reweighted matching. This formulation offers two key advantages: a) it generalizes to arbitrary monotonically increasing weighting functions; and b) it provides a principled justification and practical guidance for negative reweighting. Furthermore, we provide geometric interpretations to illustrate how negative reweighting actively repels the policy from suboptimal actions. Extensive empirical evaluations demonstrate that SiMPO achieves superior performance by leveraging these flexible weighting schemes, and we provide practical guidelines for selecting reweighting methods tailored to the reward landscape.

### 🤖 AI 总结

**一句话总结**：SiMPO 将扩散策略的强化学习重加权统一为“带符号测度匹配”，允许对负样本进行负权重，从而避免过度贪婪并提升性能。

**研究动机**：现有扩散RL常用的softmax重加权容易把策略推向过度贪婪，且几乎无法有效利用负反馈/负样本信息。作者希望用更一般的单调权重函数与理论视角，解释并指导“负重加权”带来的改进。

**核心方法**：提出两阶段的“测度匹配”框架：先在带$f$-divergence正则的策略优化中放松非负约束，构造可为负的“带符号目标测度/虚拟目标策略”；再用该测度对扩散/流模型做重加权匹配训练，从而兼容任意单调递增权重并给出负重加权的几何解释（对次优动作产生“排斥”）。

**主要结论**：实验表明 SiMPO 利用更灵活的重加权（含负权）能稳定优于传统softmax式方法，既提升性能也更能利用负反馈；同时给出了根据奖励景观选择重加权函数的实践指导。

**关键词**：扩散强化学习, 扩散策略, 行为策略重加权, 负重加权, 符号测度, 测度匹配, f-散度正则化, 单调加权函数, 策略优化, 流模型

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10250v1) | [下载PDF](https://arxiv.org/pdf/2603.10250v1.pdf)

---

## [15. Rethinking the Harmonic Loss via Non-Euclidean Distance Layers](https://arxiv.org/abs/2603.10225v1)

**作者**：Maxwell Miller-Golub, Kamil Faber, Marcin Pietron 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-10

### 📄 论文摘要

Cross-entropy loss has long been the standard choice for training deep neural networks, yet it suffers from interpretability limitations, unbounded weight growth, and inefficiencies that can contribute to costly training dynamics. The harmonic loss is a distance-based alternative grounded in Euclidean geometry that improves interpretability and mitigates phenomena such as grokking, or delayed generalization on the test set. However, the study of harmonic loss remains narrow: only Euclidean distance is explored, and no systematic evaluation of computational efficiency or sustainability was conducted. We extend harmonic loss by systematically investigating a broad spectrum of distance metrics as replacements for the Euclidean distance. We comprehensively evaluate distance-tailored harmonic losses on both vision backbones and large language models. Our analysis is framed around a three-way evaluation of model performance, interpretability, and sustainability. On vision tasks, cosine distances provide the most favorable trade-off, consistently improving accuracy while lowering carbon emissions, whereas Bray-Curtis and Mahalanobis further enhance interpretability at varying efficiency costs. On language models, cosine-based harmonic losses improve gradient and learning stability, strengthen representation structure, and reduce emissions relative to cross-entropy and Euclidean heads. Our code is available at: https://anonymous.4open.science/r/rethinking-harmonic-loss-5BAB/.

### 🤖 AI 总结

**一句话总结**：本文将harmonic loss从欧氏距离推广到多种非欧距离层，并在视觉与大语言模型上发现以余弦距离为代表的方案能在精度、可解释性与碳排/效率之间取得更优折中。

**研究动机**：交叉熵存在可解释性弱、权重无界增长与训练效率不佳等问题；现有harmonic loss虽能改善部分现象（如grokking/泛化延迟），但几乎只研究欧氏距离且缺少对计算效率与可持续性的系统评估。

**核心方法**：将harmonic loss中的欧氏距离替换为一系列距离度量（如余弦、Bray-Curtis、Mahalanobis等），在视觉backbone与LLM上进行对照实验，并从性能、可解释性、可持续性（三维指标含碳排/效率）进行统一评测与分析。

**主要结论**：在视觉任务中，余弦距离harmonic loss通常同时提升准确率并降低碳排，Bray-Curtis与Mahalanobis可进一步增强可解释性但代价因效率而异；在语言模型中，余弦型harmonic loss相对交叉熵与欧氏head带来更稳定的梯度/学习过程、更强的表示结构并减少排放。

**关键词**：调和损失, 非欧几里得距离层, 距离度量学习, 余弦距离, 马氏距离, 可解释性评估, 训练可持续性, 碳排放评估, 梯度稳定性, 视觉骨干网络

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.10225v1) | [下载PDF](https://arxiv.org/pdf/2603.10225v1.pdf)

---

