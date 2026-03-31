# arXiv AI 论文日报 | 2026-03-31

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (14 篇)
- [cs.CL](#csCL) (2 篇)
- [cs.LG](#csLG) (12 篇)
- [cs.AI](#csAI) (2 篇)

---

## cs.AI

## [1. The Ultimate Tutorial for AI-driven Scale Development in Generative Psychometrics: Releasing AIGENIE from its Bottle](https://arxiv.org/abs/2603.28643v1)

**作者**：Lara Russell-Lasalandra, Hudson Golino, Luis Eduardo Garrido 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.HC  
**发布时间**：2026-03-30

### 📄 论文摘要

Psychological scale development has traditionally required extensive expert involvement, iterative revision, and large-scale pilot testing before psychometric evaluation can begin. The `AIGENIE` R package implements the AI-GENIE framework (Automatic Item Generation with Network-Integrated Evaluation), which integrates large language model (LLM) text generation with network psychometric methods to automate the early stages of this process. The package generates candidate item pools using LLMs, transforms them into high-dimensional embeddings, and applies a multi-step reduction pipeline -- Exploratory Graph Analysis (EGA), Unique Variable Analysis (UVA), and bootstrap EGA -- to produce structurally validated item pools entirely *in silico*. This tutorial introduces the package across six parts: installation and setup, understanding Application Programming Interfaces (APIs), text generation, item generation, the `AIGENIE` function, and the `GENIE` function. Two running examples illustrate the package's use: the Big Five personality model (a well-established construct) and AI Anxiety (an emerging construct). The package supports multiple LLM providers (OpenAI, Anthropic, Groq, HuggingFace, and local models), offers a fully offline mode with no external API calls, and provides the `GENIE()` function for researchers who wish to apply the psychometric reduction pipeline to existing item pools regardless of their origin. The `AIGENIE` package is freely available on R-universe at https://laralee.r-universe.dev/AIGENIE.

### 🤖 AI 总结

**一句话总结**：Psychological scale development has traditionally required extensive expert involvement, iterative revision, and large-scale pilot testing before psychometric evaluation can begin. The `AIGENIE` R pac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：心理量表开发, 自动化条目生成, LLM 文本生成, 项目池生成, 文本嵌入, 网络心理测量, 探索性图分析（EGA）, 独特变量分析（UVA）, 离线生成模式

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28643v1) | [下载PDF](https://arxiv.org/pdf/2603.28643v1.pdf)

---

## [2. Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning](https://arxiv.org/abs/2603.28618v1)

**作者**：Ziqi Miao, Haonan Jia, Lijun Li 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-03-30

### 📄 论文摘要

Reinforcement learning with verifiable rewards (RLVR) has substantially enhanced the reasoning capabilities of multimodal large language models (MLLMs). However, existing RLVR approaches typically rely on outcome-driven optimization that updates both perception and reasoning using a shared reward based solely on the final answer. This shared reward blurs credit assignment, frequently improving reasoning patterns while failing to reliably enhance the accuracy of upstream visual evidence extraction. To address this perception bottleneck, we introduce PRCO (Perception-Reasoning Coevolution), a dual-role RLVR framework with a shared policy. PRCO consists of two cooperative roles: an Observer that generates an evidence caption tailored to the question and a Solver that predicts the final answer based on this caption. Crucially, PRCO employs role-specific reward signals: the Solver is optimized using verifiable outcome rewards on the final answer, while the Observer receives a utility reward derived from the Solver's downstream success. Extensive experiments across eight challenging multimodal reasoning benchmarks demonstrate that PRCO yields consistent improvements across model scales by over 7 points on average accuracy compared to the base model, outperforming prior open-source RL-tuned baselines.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning with verifiable rewards (RLVR) has substantially enhanced the reasoning capabilities of multimodal large language models (MLLMs). However, existing RLVR approaches typically rel...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：多模态推理, 多模态大模型, 可验证奖励强化学习, 感知-推理协同进化, 双角色策略共享, 证据描述生成, 观察者-求解者框架, 角色特定奖励, 视觉证据抽取, 多模态推理基准评测

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28618v1) | [下载PDF](https://arxiv.org/pdf/2603.28618v1.pdf)

---

## cs.CL

## [3. Adaptive Block-Scaled Data Types](https://arxiv.org/abs/2603.28765v1)

**作者**：Jack Cook, Hyemin S. Lee, Kathryn Le 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-30

### 📄 论文摘要

NVFP4 has grown increasingly popular as a 4-bit format for quantizing large language models due to its hardware support and its ability to retain useful information with relatively few bits per parameter. However, the format is not without limitations: recent work has shown that NVFP4 suffers from its error distribution, resulting in large amounts of quantization error on near-maximal values in each group of 16 values. In this work, we leverage this insight to design new Adaptive Block-Scaled Data Types that can adapt to the distribution of their input values. For four-bit quantization, our proposed IF4 (Int/Float 4) data type selects between FP4 and INT4 representations for each group of 16 values, which are then scaled by an E4M3 scale factor as is done with NVFP4. The selected data type is denoted using the scale factor's sign bit, which is currently unused in NVFP4, and we apply the same insight to design formats for other bit-widths, including IF3 and IF6. When used to quantize language models, we find that IF4 outperforms existing 4-bit block-scaled formats, achieving lower loss during quantized training and achieving higher accuracy on many tasks in post-training quantization. We additionally design and evaluate an IF4 Multiply-Accumulate (MAC) unit to demonstrate that IF4 can be implemented efficiently in next-generation hardware accelerators. Our code is available at https://github.com/mit-han-lab/fouroversix.

### 🤖 AI 总结

**一句话总结**：论文提出自适应块缩放数据类型IF4，在每16个值的块内动态选择FP4或INT4表示以降低量化误差，并在LLM量化训练与后训练量化中优于现有4-bit块缩放格式且易于硬件实现。

**研究动机**：NVFP4虽有硬件支持但其误差分布存在缺陷，导致每16值分组中接近最大值的元素量化误差偏大；因此需要一种能随输入分布自适应的4-bit块量化格式来提升精度与稳定性。

**核心方法**：提出IF4（以及IF3/IF6）：对每个16值分组在FP4与INT4两种表示间选择，并像NVFP4一样使用E4M3尺度因子进行块缩放；利用NVFP4当前未使用的尺度因子符号位编码“选择了哪种数据类型”，并设计验证了对应的IF4 MAC硬件单元以证明实现效率。

**主要结论**：在量化训练中IF4带来更低训练损失，在后训练量化中在多项任务上取得更高准确率，整体优于现有4-bit块缩放方案；同时IF4可通过复用尺度因子符号位等设计实现高效硬件落地。

**关键词**：四比特量化, 块缩放数据类型, 自适应数据类型, IF4, FP4/INT4切换, E4M3缩放因子, 量化训练, 后训练量化, MAC硬件单元

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28765v1) | [下载PDF](https://arxiv.org/pdf/2603.28765v1.pdf)

---

## [4. EpiScreen: Early Epilepsy Detection from Electronic Health Records with Large Language Models](https://arxiv.org/abs/2603.28698v1)

**作者**：Shuang Zhou, Kai Yu, Zaifu Zhan 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-30

### 📄 论文摘要

Epilepsy and psychogenic non-epileptic seizures often present with similar seizure-like manifestations but require fundamentally different management strategies. Misdiagnosis is common and can lead to prolonged diagnostic delays, unnecessary treatments, and substantial patient morbidity. Although prolonged video-electroencephalography is the diagnostic gold standard, its high cost and limited accessibility hinder timely diagnosis. Here, we developed a low-cost, effective approach, EpiScreen, for early epilepsy detection by utilizing routinely collected clinical notes from electronic health records. Through fine-tuning large language models on labeled notes, EpiScreen achieved an AUC of up to 0.875 on the MIMIC-IV dataset and 0.980 on a private cohort of the University of Minnesota. In a clinician-AI collaboration setting, EpiScreen-assisted neurologists outperformed unaided experts by up to 10.9%. Overall, this study demonstrates that EpiScreen supports early epilepsy detection, facilitating timely and cost-effective screening that may reduce diagnostic delays and avoid unnecessary interventions, particularly in resource-limited regions.

### 🤖 AI 总结

**一句话总结**：EpiScreen 通过微调大语言模型分析电子病历临床文本，实现对癫痫的低成本早期筛查，并在公开与私有数据集上取得较高AUC且能提升神经科医生诊断表现。

**研究动机**：癫痫与心因性非癫痫性发作症状相似，误诊与延迟诊断常见且代价高；而金标准视频脑电图昂贵且可及性有限，亟需可扩展、低成本的早筛方案。

**核心方法**：利用电子健康记录中的常规临床笔记构建标注数据，对大语言模型进行微调以区分癫痫相关病例；并在MIMIC-IV与明尼苏达大学私有队列上评估AUC，同时测试“医生+模型”协作诊断效果。

**主要结论**：EpiScreen 在MIMIC-IV上最高AUC达0.875、在私有队列上达0.980，并在协作场景中使神经科医生相对无辅助表现提升最高约10.9%，表明其可用于更及时、经济的癫痫筛查以减少不必要干预与诊断延误。

**关键词**：早期癫痫检测, 心因性非癫痫发作鉴别, 电子病历, 临床笔记, 医学文本分类, 弱资源筛查, 临床医生-AI协作, EpiScreen

**评分**：59

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28698v1) | [下载PDF](https://arxiv.org/pdf/2603.28698v1.pdf)

---

## cs.CV

## [5. Gen-Searcher: Reinforcing Agentic Search for Image Generation](https://arxiv.org/abs/2603.28767v1)

**作者**：Kaituo Feng, Manyuan Zhang, Shuang Chen 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-30

### 📄 论文摘要

Recent image generation models have shown strong capabilities in generating high-fidelity and photorealistic images. However, they are fundamentally constrained by frozen internal knowledge, thus often failing on real-world scenarios that are knowledge-intensive or require up-to-date information. In this paper, we present Gen-Searcher, as the first attempt to train a search-augmented image generation agent, which performs multi-hop reasoning and search to collect the textual knowledge and reference images needed for grounded generation. To achieve this, we construct a tailored data pipeline and curate two high-quality datasets, Gen-Searcher-SFT-10k and Gen-Searcher-RL-6k, containing diverse search-intensive prompts and corresponding ground-truth synthesis images. We further introduce KnowGen, a comprehensive benchmark that explicitly requires search-grounded external knowledge for image generation and evaluates models from multiple dimensions. Based on these resources, we train Gen-Searcher with SFT followed by agentic reinforcement learning with dual reward feedback, which combines text-based and image-based rewards to provide more stable and informative learning signals for GRPO training. Experiments show that Gen-Searcher brings substantial gains, improving Qwen-Image by around 16 points on KnowGen and 15 points on WISE. We hope this work can serve as an open foundation for search agents in image generation, and we fully open-source our data, models, and code.

### 🤖 AI 总结

**一句话总结**：Gen-Searcher 通过引入“搜索+多跳推理+强化学习”的代理式流程，让图像生成模型能检索外部知识与参考图并进行更可靠的知识落地生成。

**研究动机**：现有图像生成模型受限于冻结的内部知识，遇到需要最新信息或强知识依赖的真实场景时容易生成不准确或不 grounded 的结果，因此需要可检索外部信息的生成机制。

**核心方法**：作者构建面向搜索增强生成的数据管线与两套数据集（SFT-10k 与 RL-6k），并提出需要外部知识支撑的基准 KnowGen；训练上先做监督微调，再进行带双重奖励（文本奖励+图像奖励）的代理式强化学习以稳定 GRPO 训练并提升搜索与合成能力。

**主要结论**：实验表明 Gen-Searcher 显著提升了知识驱动的图像生成表现，相比基础模型（如 Qwen-Image）在 KnowGen 与 WISE 上分别提升约 16 分和 15 分，证明搜索增强与双奖励 RL 能有效改善 grounded 生成。

**关键词**：搜索增强图像生成, 多跳推理, 知识驱动生成, 参考图像检索, 外部知识对齐, 监督微调, 强化学习, 双重奖励机制, 评测基准

**评分**：83

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28767v1) | [下载PDF](https://arxiv.org/pdf/2603.28767v1.pdf)

---

## [6. HandX: Scaling Bimanual Motion and Interaction Generation](https://arxiv.org/abs/2603.28766v1)

**作者**：Zimu Zhang, Yucheng Zhang, Xiyan Xu 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-30

### 📄 论文摘要

Synthesizing human motion has advanced rapidly, yet realistic hand motion and bimanual interaction remain underexplored. Whole-body models often miss the fine-grained cues that drive dexterous behavior, finger articulation, contact timing, and inter-hand coordination, and existing resources lack high-fidelity bimanual sequences that capture nuanced finger dynamics and collaboration. To fill this gap, we present HandX, a unified foundation spanning data, annotation, and evaluation. We consolidate and filter existing datasets for quality, and collect a new motion-capture dataset targeting underrepresented bimanual interactions with detailed finger dynamics. For scalable annotation, we introduce a decoupled strategy that extracts representative motion features, e.g., contact events and finger flexion, and then leverages reasoning from large language models to produce fine-grained, semantically rich descriptions aligned with these features. Building on the resulting data and annotations, we benchmark diffusion and autoregressive models with versatile conditioning modes. Experiments demonstrate high-quality dexterous motion generation, supported by our newly proposed hand-focused metrics. We further observe clear scaling trends: larger models trained on larger, higher-quality datasets produce more semantically coherent bimanual motion. Our dataset is released to support future research.

### 🤖 AI 总结

**一句话总结**：HandX 提供从数据、标注到评测的一体化基础设施，用于扩展高保真双手（含手指细节）运动与交互生成，并验证数据与模型规模提升能显著增强语义一致性与生成质量。

**研究动机**：现有全身动作生成往往忽略精细手部线索，难以刻画手指关节、接触时序与双手协同等关键细节；同时缺乏覆盖丰富双手交互、且高保真手指动态的数据与评测标准。

**核心方法**：作者整合并过滤既有数据集，并新增采集面向欠覆盖双手交互的动捕数据以强化手指动态；提出“特征提取（如接触事件、手指屈伸）+ LLM 推理生成语义描述”的解耦标注策略，并在此基础上用扩散/自回归模型在多种条件输入下进行基准测试，配套提出手部聚焦指标进行评估。

**主要结论**：实验表明基于 HandX 可生成更高质量、更灵巧的双手交互动作，且手部专用指标能更敏感地衡量改进；同时观察到明确的 scaling 趋势：更大模型与更大、更高质量数据带来更强的语义连贯性与动作真实性。

**关键词**：双手运动生成, 手部细粒度运动, 双手交互建模, 动作捕捉数据集, 高保真手指动力学, 接触事件检测, 手指屈伸特征, LLM辅助标注, Diffusion, 自回归模型, 条件生成

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28766v1) | [下载PDF](https://arxiv.org/pdf/2603.28766v1.pdf)

---

## [7. PoseDreamer: Scalable and Photorealistic Human Data Generation Pipeline with Diffusion Models](https://arxiv.org/abs/2603.28763v1)

**作者**：Lorenza Prospero, Orest Kupyn, Ostap Viniavskyi 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-30

### 📄 论文摘要

Acquiring labeled datasets for 3D human mesh estimation is challenging due to depth ambiguities and the inherent difficulty of annotating 3D geometry from monocular images. Existing datasets are either real, with manually annotated 3D geometry and limited scale, or synthetic, rendered from 3D engines that provide precise labels but suffer from limited photorealism, low diversity, and high production costs. In this work, we explore a third path: generated data. We introduce PoseDreamer, a novel pipeline that leverages diffusion models to generate large-scale synthetic datasets with 3D mesh annotations. Our approach combines controllable image generation with Direct Preference Optimization for control alignment, curriculum-based hard sample mining, and multi-stage quality filtering. Together, these components naturally maintain correspondence between 3D labels and generated images, while prioritizing challenging samples to maximize dataset utility. Using PoseDreamer, we generate more than 500,000 high-quality synthetic samples, achieving a 76% improvement in image-quality metrics compared to rendering-based datasets. Models trained on PoseDreamer achieve performance comparable to or superior to those trained on real-world and traditional synthetic datasets. In addition, combining PoseDreamer with synthetic datasets results in better performance than combining real-world and synthetic datasets, demonstrating the complementary nature of our dataset. We will release the full dataset and generation code.

### 🤖 AI 总结

**一句话总结**：PoseDreamer 提出一套基于扩散模型的人体图像生成与3D网格标注数据管线，可大规模产出高拟真且“图像-3D标签”对应一致的数据，用于提升3D人体网格估计训练效果。

**研究动机**：真实数据集3D标注昂贵且规模受限，而传统引擎渲染合成数据虽有精确标签但拟真度与多样性不足、制作成本高；因此作者探索用生成式模型在保证可控与标签一致性的前提下，生成高质量大规模训练数据。

**核心方法**：管线结合可控扩散生成与DPO（Direct Preference Optimization）进行控制对齐，配合基于课程学习的困难样本挖掘与多阶段质量过滤，从而在生成过程中维持3D标注与图像的一致对应，并优先产出更具训练价值的“难样本”。

**主要结论**：PoseDreamer 生成超50万高质量样本，相比渲染式数据集在图像质量指标上提升约76%，用其训练的模型性能可达或超过真实/传统合成数据；且与传统合成数据联合训练优于“真实+合成”的组合，表明其数据具有互补性与实用价值。

**关键词**：3D人体网格估计, 数据集生成, Diffusion, 可控图像生成, 3D网格标注, 课程式难例挖掘, 多阶段质量过滤, 合成数据增强, 真实感评估, 单目3D重建

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28763v1) | [下载PDF](https://arxiv.org/pdf/2603.28763v1.pdf)

---

## [8. On-the-fly Repulsion in the Contextual Space for Rich Diversity in Diffusion Transformers](https://arxiv.org/abs/2603.28762v1)

**作者**：Omer Dahary, Benaya Koren, Daniel Garibi 等 4 位作者  
**分类**：cs.CV, cs.AI, cs.GR, cs.LG  
**发布时间**：2026-03-30

### 📄 论文摘要

Modern Text-to-Image (T2I) diffusion models have achieved remarkable semantic alignment, yet they often suffer from a significant lack of variety, converging on a narrow set of visual solutions for any given prompt. This typicality bias presents a challenge for creative applications that require a wide range of generative outcomes. We identify a fundamental trade-off in current approaches to diversity: modifying model inputs requires costly optimization to incorporate feedback from the generative path. In contrast, acting on spatially-committed intermediate latents tends to disrupt the forming visual structure, leading to artifacts. In this work, we propose to apply repulsion in the Contextual Space as a novel framework for achieving rich diversity in Diffusion Transformers. By intervening in the multimodal attention channels, we apply on-the-fly repulsion during the transformer's forward pass, injecting the intervention between blocks where text conditioning is enriched with emergent image structure. This allows for redirecting the guidance trajectory after it is structurally informed but before the composition is fixed. Our results demonstrate that repulsion in the Contextual Space produces significantly richer diversity without sacrificing visual fidelity or semantic adherence. Furthermore, our method is uniquely efficient, imposing a small computational overhead while remaining effective even in modern "Turbo" and distilled models where traditional trajectory-based interventions typically fail.

### 🤖 AI 总结

**一句话总结**：提出在扩散Transformer的“上下文空间”（多模态注意力通道）中进行前向过程的即时repulsion干预，在不损害语义对齐与画质的前提下显著提升同一提示词的生成多样性。

**研究动机**：现有T2I扩散模型存在“典型性偏差”，容易收敛到少数视觉解而缺乏多样性；同时，基于输入的改动往往需要代价高的轨迹反馈优化，而对中间潜变量的空间级干预又容易破坏结构并引入伪影。

**核心方法**：在Transformer前向传播中、跨block地对多模态注意力形成的上下文表征施加repulsion：选择在文本条件已被初步图像结构“丰富”但构图尚未固定的阶段插入干预，以重定向guidance轨迹并促成不同解的分化；该方式计算开销小，且对Turbo/蒸馏等短步模型仍有效。

**主要结论**：上下文空间repulsion能在保持视觉保真度与语义一致性的同时带来更“丰富”的多样性，并且相比传统轨迹类或潜空间干预更高效、更稳健，尤其在加速/蒸馏扩散模型中优势明显。

**关键词**：文生图扩散模型, 生成多样性, 典型性偏差, 上下文空间排斥, 多模态注意力干预, 前向过程注入, 引导轨迹重定向, 中间潜变量编辑, 蒸馏模型

**评分**：82

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28762v1) | [下载PDF](https://arxiv.org/pdf/2603.28762v1.pdf)

---

## [9. SHOW3D: Capturing Scenes of 3D Hands and Objects in the Wild](https://arxiv.org/abs/2603.28760v1)

**作者**：Patrick Rim, Kevin Harris, Braden Copple 等 11 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-03-30

### 📄 论文摘要

Accurate 3D understanding of human hands and objects during manipulation remains a significant challenge for egocentric computer vision. Existing hand-object interaction datasets are predominantly captured in controlled studio settings, which limits both environmental diversity and the ability of models trained on such data to generalize to real-world scenarios. To address this challenge, we introduce a novel marker-less multi-camera system that allows for nearly unconstrained mobility in genuinely in-the-wild conditions, while still having the ability to generate precise 3D annotations of hands and objects. The capture system consists of a lightweight, back-mounted, multi-camera rig that is synchronized and calibrated with a user-worn VR headset. For 3D ground-truth annotation of hands and objects, we develop an ego-exo tracking pipeline and rigorously evaluate its quality. Finally, we present SHOW3D, the first large-scale dataset with 3D annotations that show hands interacting with objects in diverse real-world environments, including outdoor settings. Our approach significantly reduces the fundamental trade-off between environmental realism and accuracy of 3D annotations, which we validate with experiments on several downstream tasks. show3d-dataset.github.io

### 🤖 AI 总结

**一句话总结**：SHOW3D提出一种可在真实野外环境中自由移动的无标记多相机采集系统与追踪流程，构建了首个大规模“手-物体交互”3D标注野外数据集。

**研究动机**：现有手-物体交互数据集多在棚内受控环境采集，环境多样性不足，导致模型难以泛化到真实世界（含户外）场景。研究希望在“环境真实感”与“高精度3D标注”之间打破长期存在的权衡。

**核心方法**：作者设计轻量化背负式多相机Rig，并与佩戴式VR头显进行同步与标定，实现近乎不受限的野外采集。随后提出ego-exo手/物体追踪与3D标注管线，生成并评估高质量3D真值，最终发布SHOW3D数据集并在多个下游任务上验证其价值。

**主要结论**：该系统与数据集在保持野外多样性与可移动性的同时，仍能提供精确的手与物体3D注释，从而显著缓解真实环境与标注精度的矛盾。实验表明使用SHOW3D能提升多项下游任务表现与对真实场景的泛化能力。

**关键词**：第一人称视觉, 手-物体交互, 三维手部姿态估计, 三维物体位姿估计, 三维标注数据集, 野外场景采集, 无标记多相机系统, 可穿戴多相机背负式支架, VR头显同步标定, 多视角三维重建, 跨场景泛化评测

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28760v1) | [下载PDF](https://arxiv.org/pdf/2603.28760v1.pdf)

---

## [10. FlowIt: Global Matching for Optical Flow with Confidence-Guided Refinement](https://arxiv.org/abs/2603.28759v1)

**作者**：Sadra Safadoust, Fabio Tosi, Matteo Poggi 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-30

### 📄 论文摘要

We present FlowIt, a novel architecture for optical flow estimation designed to robustly handle large pixel displacements. At its core, FlowIt leverages a hierarchical transformer architecture that captures extensive global context, enabling the model to effectively model long-range correspondences. To overcome the limitations of localized matching, we formulate the flow initialization as an optimal transport problem. This formulation yields a highly robust initial flow field, alongside explicitly derived occlusion and confidence maps. These cues are then seamlessly integrated into a guided refinement stage, where the network actively propagates reliable motion estimates from high-confidence regions into ambiguous, low-confidence areas. Extensive experiments across the Sintel, KITTI, Spring, and LayeredFlow datasets validate the efficacy of our approach. FlowIt achieves state-of-the-art results on the competitive Sintel and KITTI benchmarks, while simultaneously establishing new state-of-the-art cross-dataset zero-shot generalization performance on Sintel, Spring, and LayeredFlow.

### 🤖 AI 总结

**一句话总结**：FlowIt通过全局匹配与置信度引导的细化机制，实现对大位移光流的鲁棒估计并在多项基准上达到SOTA与强零样本泛化。

**研究动机**：现有光流方法常受限于局部匹配与有限感受野，在大位移、遮挡与纹理模糊区域易产生错误对应与不稳定估计。作者希望在获得可靠全局对应的同时，显式建模遮挡/置信度来指导后续修正。

**核心方法**：采用分层Transformer获取全局上下文以建模长程对应，并将初始光流估计表述为最优传输（Optimal Transport）问题以得到鲁棒初始流场，同时显式推导遮挡与置信度图。随后在置信度引导的细化阶段，将高置信区域的可靠运动估计传播到低置信、歧义区域以提升整体质量。

**主要结论**：在Sintel、KITTI、Spring与LayeredFlow等数据集上实验表明，FlowIt在Sintel与KITTI上取得（或达到）最先进性能，并在跨数据集零样本泛化方面在Sintel、Spring与LayeredFlow上建立新的SOTA。其优势主要来自全局匹配的稳健初始化与利用置信度/遮挡进行针对性细化。

**关键词**：光流估计, 大位移匹配, 全局匹配, 长程对应, 最优传输, 置信度图, 遮挡估计, 置信引导细化, 零样本泛化, 跨数据集评测

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28759v1) | [下载PDF](https://arxiv.org/pdf/2603.28759v1.pdf)

---

## [11. SonoWorld: From One Image to a 3D Audio-Visual Scene](https://arxiv.org/abs/2603.28757v1)

**作者**：Derong Jin, Xiyi Chen, Ming C. Lin 等 4 位作者  
**分类**：cs.CV, cs.MM, cs.SD  
**发布时间**：2026-03-30

### 📄 论文摘要

Tremendous progress in visual scene generation now turns a single image into an explorable 3D world, yet immersion remains incomplete without sound. We introduce Image2AVScene, the task of generating a 3D audio-visual scene from a single image, and present SonoWorld, the first framework to tackle this challenge. From one image, our pipeline outpaints a 360° panorama, lifts it into a navigable 3D scene, places language-guided sound anchors, and renders ambisonics for point, areal, and ambient sources, yielding spatial audio aligned with scene geometry and semantics. Quantitative evaluations on a newly curated real-world dataset and a controlled user study confirm the effectiveness of our approach. Beyond free-viewpoint audio-visual rendering, we also demonstrate applications to one-shot acoustic learning and audio-visual spatial source separation. Project website: https://humathe.github.io/sonoworld/

### 🤖 AI 总结

**一句话总结**：SonoWorld提出从单张图片生成可自由视角探索的3D视听场景，并为场景渲染与几何/语义一致的空间音频。

**研究动机**：现有从单图生成3D世界的视觉效果已很强，但缺少与场景匹配的空间声音使沉浸感不完整；因此需要把“图像→可导航3D场景→空间音频”打通为统一任务。

**核心方法**：提出Image2AVScene任务与SonoWorld流水线：先将单图外延生成360°全景，再提升为可导航3D场景；随后用语言引导放置声音锚点，并对点声源/面声源/环境声源渲染全向声（ambisonics），使音频与场景几何和语义对齐。

**主要结论**：在新构建的真实数据集与受控用户研究中，该方法在视听一致性与空间音频效果上表现有效；并展示了其在一次性声学学习与视听空间源分离等下游应用中的潜力。

**关键词**：单图生成3D场景, 音视频场景生成, 360°全景补全, 自由视点渲染, 空间音频渲染, 声源锚点定位, 语言引导声源放置, 点源面源环境声建模, 音视频空间源分离, 一次声学学习, 真实世界数据集评测

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28757v1) | [下载PDF](https://arxiv.org/pdf/2603.28757v1.pdf)

---

## [12. DreamLite: A Lightweight On-Device Unified Model for Image Generation and Editing](https://arxiv.org/abs/2603.28713v1)

**作者**：Kailai Feng, Yuxiang Wei, Bo Chen 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-30

### 📄 论文摘要

Diffusion models have made significant progress in both text-to-image (T2I) generation and text-guided image editing. However, these models are typically built with billions of parameters, leading to high latency and increased deployment challenges. While on-device diffusion models improve efficiency, they largely focus on T2I generation and lack support for image editing. In this paper, we propose DreamLite, a compact unified on-device diffusion model (0.39B) that supports both T2I generation and text-guided image editing within a single network. DreamLite is built on a pruned mobile U-Net backbone and unifies conditioning through in-context spatial concatenation in the latent space. It concatenates images horizontally as input, using a (target | blank) configuration for generation tasks and (target | source) for editing tasks. To stabilize the training of this compact model, we introduce a task-progressive joint pretraining strategy that sequentially targets T2I, editing, and joint tasks. After high-quality SFT and reinforcement learning, DreamLite achieves GenEval (0.72) for image generation and ImgEdit (4.11) for image editing, outperforming existing on-device models and remaining competitive with several server-side models. By employing step distillation, we further reduce denoising processing to just 4 steps, enabling our DreamLite could generate or edit a 1024 x 1024 image in less than 1s on a Xiaomi 14 smartphone. To the best of our knowledge, DreamLite is the first unified on-device diffusion model that supports both image generation and image editing.

### 🤖 AI 总结

**一句话总结**：DreamLite 提出一个仅 0.39B 参数的端侧统一扩散模型，在单一网络内同时支持文生图与文本引导图像编辑，并通过蒸馏将推理步数降到 4 步实现手机端 1 秒内生成/编辑 1024×1024 图像。

**研究动机**：现有扩散模型多为十亿级参数，端侧部署延迟高且成本大；而已有端侧扩散模型大多只覆盖文生图，缺少统一且高质量的图像编辑能力。

**核心方法**：基于剪枝后的移动端 U-Net 作为骨干，在潜空间通过“上下文式空间拼接”统一条件输入：将图像水平拼接，生成用 (target|blank)，编辑用 (target|source)。训练上采用任务渐进的联合预训练（先 T2I、再编辑、再联合），并结合高质量 SFT 与强化学习提升对齐，最后用 step distillation 将去噪步数压缩到 4 步以加速端侧推理。

**主要结论**：DreamLite 在生成与编辑上分别达到 GenEval 0.72 与 ImgEdit 4.11，优于现有端侧模型并可与部分服务端模型竞争；在小米 14 上可在 1 秒内完成 1024×1024 的生成或编辑，证明统一端侧扩散模型在效率与能力上的可行性。

**关键词**：端侧扩散模型, 统一生成编辑, 文本到图像生成, 文本引导图像编辑, 模型剪枝, 潜空间空间拼接, 任务渐进联合预训练, 步数蒸馏, 强化学习微调, 少步去噪推理

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28713v1) | [下载PDF](https://arxiv.org/pdf/2603.28713v1.pdf)

---

## [13. Why Aggregate Accuracy is Inadequate for Evaluating Fairness in Law Enforcement Facial Recognition Systems](https://arxiv.org/abs/2603.28675v1)

**作者**：Khalid Adnan Alsayed  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-03-30

### 📄 论文摘要

Facial recognition systems are increasingly deployed in law enforcement and security contexts, where algorithmic decisions can carry significant societal consequences. Despite high reported accuracy, growing evidence demonstrates that such systems often exhibit uneven performance across demographic groups, leading to disproportionate error rates and potential harm. This paper argues that aggregate accuracy is an insufficient metric for evaluating the fairness and reliability of facial recognition systems in high-stakes environments. Through analysis of subgroup-level error distribution, including false positive rate (FPR) and false negative rate (FNR), the paper demonstrates how aggregate performance metrics can obscure critical disparities across demographic groups. Empirical observations show that systems with similar overall accuracy can exhibit substantially different fairness profiles, with subgroup error rates varying significantly despite a single aggregate metric. The paper further examines the operational risks associated with accuracy-centric evaluation practices in law enforcement applications, where misclassification may result in wrongful suspicion or missed identification. It highlights the importance of fairness-aware evaluation approaches and model-agnostic auditing strategies that enable post-deployment assessment of real-world systems. The findings emphasise the need to move beyond accuracy as a primary metric and adopt more comprehensive evaluation frameworks for responsible AI deployment.

### 🤖 AI 总结

**一句话总结**：论文指出在执法场景中仅用总体准确率评估人脸识别系统会掩盖不同人群间的错误率差异，从而无法反映真实的公平性与风险。

**研究动机**：人脸识别在高风险执法应用中即使“整体很准”，也可能对某些人口统计子群体产生更高误报/漏报并造成不成比例的伤害，因此需要更可靠的公平性评估指标。

**核心方法**：通过分析分组（subgroup）层面的错误分布，重点比较不同群体的假阳性率（FPR）与假阴性率（FNR），展示相同或相近总体准确率下仍可能存在显著不同的公平性画像；并讨论与模型无关的审计与部署后评估策略。

**主要结论**：总体准确率不足以作为执法用人脸识别系统的主要评价标准，因为它会遮蔽关键的群体差异并带来运营风险（如冤错指认或漏识别）；应采用面向公平的综合评估框架与可审计方法来支持负责任部署。

**关键词**：执法场景人脸识别, 公平性评估, 总体准确率局限, 群体差异性能, 子群错误率分析, 假阳性率 FPR, 假阴性率 FNR, 人口统计偏差, 模型无关审计, 部署后评测

**评分**：67

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28675v1) | [下载PDF](https://arxiv.org/pdf/2603.28675v1.pdf)

---

## [14. Sim-to-Real Fruit Detection Using Synthetic Data: Quantitative Evaluation and Embedded Deployment with Isaac Sim](https://arxiv.org/abs/2603.28670v1)

**作者**：Martina Hutter-Mironovova  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-03-30

### 📄 论文摘要

This study investigates the effectiveness of synthetic data for sim-to-real transfer in object detection under constrained data conditions and embedded deployment requirements. Synthetic datasets were generated in NVIDIA Isaac Sim and combined with limited real-world fruit images to train YOLO-based detection models under real-only, synthetic-only, and hybrid regimes. Performance was evaluated on two test datasets: an in-domain dataset with conditions matching the training data and a domain shift dataset containing real fruit and different background conditions. Results show that models trained exclusively on real data achieve the highest accuracy, while synthetic-only models exhibit reduced performance due to a domain gap. Hybrid training strategies significantly improve performance compared to synthetic-only approaches and achieve results close to real-only training while reducing the need for manual annotation. Under domain shift conditions, all models show performance degradation, with hybrid models providing improved robustness. The trained models were successfully deployed on a Jetson Orin NX using TensorRT optimization, achieving real-time inference performance. The findings highlight that synthetic data is most effective when used in combination with real data and that deployment constraints must be considered alongside detection accuracy.

### 🤖 AI 总结

**一句话总结**：用Isaac Sim生成的合成水果数据单独训练会受域差影响，但与少量真实数据混合训练可在减少标注成本的同时获得接近纯真实数据训练的检测效果，并可在Jetson Orin NX上实现实时部署。

**研究动机**：在真实数据稀缺且人工标注成本高的情况下，探索合成数据是否能有效提升目标检测的sim-to-real迁移效果；同时考虑模型需在嵌入式设备上以实时性能运行的工程约束。

**核心方法**：在NVIDIA Isaac Sim中生成合成水果数据，并与少量真实图片组合，分别按“仅真实/仅合成/混合”训练YOLO系目标检测模型；在同域测试集与存在背景变化的域偏移测试集上定量评估，并将模型通过TensorRT优化部署到Jetson Orin NX验证实时推理。

**主要结论**：纯真实数据训练精度最高，纯合成训练因域差性能明显下降；混合训练显著优于纯合成并接近纯真实，同时在域偏移下更鲁棒但所有模型都会退化；经TensorRT优化后模型可在Jetson Orin NX上实现实时推理，表明需同时权衡数据策略与部署约束。

**关键词**：仿真到现实迁移, 水果目标检测, 合成数据生成, 混合训练, 领域差距, 领域迁移评测, 嵌入式部署, 实时推理

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28670v1) | [下载PDF](https://arxiv.org/pdf/2603.28670v1.pdf)

---

## [15. Industrial3D: A Terrestrial LiDAR Point Cloud Dataset and CrossParadigm Benchmark for Industrial Infrastructure](https://arxiv.org/abs/2603.28660v1)

**作者**：Chao Yin, Hongzhe Yue, Qing Han 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-30

### 📄 论文摘要

Automated semantic understanding of dense point clouds is a prerequisite for Scan-to-BIM pipelines, digital twin construction, and as-built verification--core tasks in the digital transformation of the construction industry. Yet for industrial mechanical, electrical, and plumbing (MEP) facilities, this challenge remains largely unsolved: TLS acquisitions of water treatment plants, chiller halls, and pumping stations exhibit extreme geometric ambiguity, severe occlusion, and extreme class imbalance that architectural benchmarks (e.g., S3DIS or ScanNet) cannot adequately represent. We present Industrial3D, a terrestrial LiDAR dataset comprising 612 million expertly labelled points at 6 mm resolution from 13 water treatment facilities. At 6.6x the scale of the closest comparable MEP dataset, Industrial3D provides the largest and most demanding testbed for industrial 3D scene understanding to date. We further establish the first industrial cross-paradigm benchmark, evaluating nine representative methods across fully supervised, weakly supervised, unsupervised, and foundation model settings under a unified benchmark protocol. The best supervised method achieves 55.74% mIoU, whereas zero-shot Point-SAM reaches only 15.79%--a 39.95 percentage-point gap that quantifies the unresolved domain-transfer challenge for industrial TLS data. Systematic analysis reveals that this gap originates from a dual crisis: statistical rarity (215:1 imbalance, 3.5x more severe than S3DIS) and geometric ambiguity (tail-class points share cylindrical primitives with head-class pipes) that frequency-based re-weighting alone cannot resolve. Industrial3D, along with benchmark code and pre-trained models, will be publicly available at https://github.com/pointcloudyc/Industrial3D.

### 🤖 AI 总结

**一句话总结**：提出并公开Industrial3D工业设施TLS点云大规模数据集与跨范式基准，系统揭示工业场景在类别极度不均衡与几何歧义下仍显著落后于现有方法与零样本基础模型。

**研究动机**：工业MEP设施的TLS点云存在严重遮挡、几何相似与类别长尾不均衡，导致建筑类数据集（如S3DIS/ScanNet）上的方法难以迁移，Scan-to-BIM与数字孪生等关键流程缺乏可靠语义理解能力。

**核心方法**：构建包含13个水处理设施、6mm分辨率、6.12亿人工精标点的Industrial3D数据集，并在统一协议下对9类代表方法进行跨范式评测（全监督/弱监督/无监督/基础模型零样本），同时分析性能差距来源。

**主要结论**：最优全监督方法仅达55.74% mIoU，而零样本Point-SAM仅15.79%，表明工业TLS的域迁移仍未解决；差距主要由“统计稀有性”（约215:1长尾不均衡）与“几何歧义”（尾类与管道共享圆柱几何原语）共同造成，单靠频率重加权难以弥补。

**关键词**：工业TLS点云, 语义分割, 工业MEP设施, 数字孪生, 极端类别不平衡, 几何歧义, 遮挡鲁棒性, 跨范式评测基准, 零样本迁移, 弱监督学习

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28660v1) | [下载PDF](https://arxiv.org/pdf/2603.28660v1.pdf)

---

## [16. TGIF2: Extended Text-Guided Inpainting Forgery Dataset & Benchmark](https://arxiv.org/abs/2603.28613v1)

**作者**：Hannes Mareen, Dimitrios Karageorgiou, Paschalis Giakoumoglou 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.CR, cs.MM  
**发布时间**：2026-03-30

### 📄 论文摘要

Generative AI has made text-guided inpainting a powerful image editing tool, but at the same time a growing challenge for media forensics. Existing benchmarks, including our text-guided inpainting forgery (TGIF) dataset, show that image forgery localization (IFL) methods can localize manipulations in spliced images but struggle not in fully regenerated (FR) images, while synthetic image detection (SID) methods can detect fully regenerated images but cannot perform localization. With new generative inpainting models emerging and the open problem of localization in FR images remaining, updated datasets and benchmarks are needed. We introduce TGIF2, an extended version of TGIF, that captures recent advances in text-guided inpainting and enables a deeper analysis of forensic robustness. TGIF2 augments the original dataset with edits generated by FLUX.1 models, as well as with random non-semantic masks. Using the TGIF2 dataset, we conduct a forensic evaluation spanning IFL and SID, including fine-tuning IFL methods on FR images and generative super-resolution attacks. Our experiments show that both IFL and SID methods degrade on FLUX.1 manipulations, highlighting limited generalization. Additionally, while fine-tuning improves localization on FR images, evaluation with random non-semantic masks reveals object bias. Furthermore, generative super-resolution significantly weakens forensic traces, demonstrating that common image enhancement operations can undermine current forensic pipelines. In summary, TGIF2 provides an updated dataset and benchmark, which enables new insights into the challenges posed by modern inpainting and AI-based image enhancements. TGIF2 is available at https://github.com/IDLabMedia/tgif-dataset.

### 🤖 AI 总结

**一句话总结**：TGIF2 扩展了文本引导修复伪造数据集与基准，引入 FLUX.1 生成编辑与随机掩码，并系统评估发现现有检测/定位方法对新型修复与超分增强的鲁棒性和泛化性不足。

**研究动机**：随着文本引导 inpainting 生成模型快速演进，既有数据集难覆盖最新伪造痕迹，且“完全再生成（FR）图像的定位”仍是开放难题，需要更新基准来检验方法的泛化与真实场景稳健性。

**核心方法**：构建 TGIF2：在原 TGIF 基础上加入 FLUX.1 生成的编辑样本及随机非语义掩码，并在该数据集上同时评测 IFL（伪造定位）与 SID（合成检测），包含对 FR 图像的 IFL 微调以及生成式超分辨率攻击测试。

**主要结论**：IFL 与 SID 在 FLUX.1 操作上性能明显下降，显示对新模型的泛化有限；微调虽提升 FR 定位，但随机掩码评测暴露出对象偏置；生成式超分辨率会显著削弱取证痕迹，说明常见增强操作即可破坏当前取证流水线。

**关键词**：文本引导图像修复, 图像篡改定位, 合成图像检测, 全再生成图像, 伪造数据集, 评测基准, 随机非语义掩码, 生成式超分辨率攻击, 鲁棒性泛化评估

**评分**：61

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28613v1) | [下载PDF](https://arxiv.org/pdf/2603.28613v1.pdf)

---

## [17. Unsafe2Safe: Controllable Image Anonymization for Downstream Utility](https://arxiv.org/abs/2603.28605v1)

**作者**：Mih Dinh, SouYoung Jin  
**分类**：cs.CV, cs.CY, cs.LG  
**发布时间**：2026-03-30

### 📄 论文摘要

Large-scale image datasets frequently contain identifiable or sensitive content, raising privacy risks when training models that may memorize and leak such information. We present Unsafe2Safe, a fully automated pipeline that detects privacy-prone images and rewrites only their sensitive regions using multimodally guided diffusion editing. Unsafe2Safe operates in two stages. Stage 1 uses a vision-language model to (i) inspect images for privacy risks, (ii) generate paired private and public captions that respectively include and omit sensitive attributes, and (iii) prompt a large language model to produce structured, identity-neutral edit instructions conditioned on the public caption. Stage 2 employs instruction-driven diffusion editors to apply these dual textual prompts, producing privacy-safe images that preserve global structure and task-relevant semantics while neutralizing private content. To measure anonymization quality, we introduce a unified evaluation suite covering Quality, Cheating, Privacy, and Utility dimensions. Across MS-COCO, Caltech101, and MIT Indoor67, Unsafe2Safe reduces face similarity, text similarity, and demographic predictability by large margins, while maintaining downstream model accuracy comparable to training on raw data. Fine-tuning diffusion editors on our automatically generated triplets (private caption, public caption, edit instruction) further improves both privacy protection and semantic fidelity. Unsafe2Safe provides a scalable, principled solution for constructing large, privacy-safe datasets without sacrificing visual consistency or downstream utility.

### 🤖 AI 总结

**一句话总结**：Unsafe2Safe 通过“检测隐私风险 + 扩散模型局部重写”自动将含敏感信息的图像匿名化，同时尽量保持下游任务所需语义与数据效用。

**研究动机**：大规模图像数据常包含可识别身份或敏感属性，训练模型可能记忆并泄露隐私；现有匿名化方法往往牺牲图像一致性或破坏下游可用性，因此需要可控、可规模化且兼顾效用的方案。

**核心方法**：两阶段流水线：阶段1用视觉-语言模型识别隐私风险并生成“私有/公开”成对描述，再由LLM基于公开描述产出结构化、身份中立的编辑指令；阶段2用指令驱动的扩散编辑器在双文本提示引导下仅重写敏感区域，生成隐私安全且保持全局结构与任务语义的图像，并提供覆盖质量/作弊/隐私/效用的统一评测套件。

**主要结论**：在多个数据集上，该方法显著降低人脸相似度、文本相似度与人口属性可预测性，同时下游模型精度接近使用原始数据训练；基于自动生成的三元组数据微调扩散编辑器还能进一步提升隐私保护与语义保真度。

**关键词**：图像匿名化, 隐私安全数据集, 敏感区域重写, 扩散模型编辑, 指令驱动图像编辑, 多模态引导, 视觉语言模型, 私有-公开双字幕, 身份中性编辑指令, 匿名化评测体系

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28605v1) | [下载PDF](https://arxiv.org/pdf/2603.28605v1.pdf)

---

## [18. ELViS: Efficient Visual Similarity from Local Descriptors that Generalizes Across Domains](https://arxiv.org/abs/2603.28603v1)

**作者**：Pavel Suma, Giorgos Kordopatis-Zilos, Yannis Kalantidis 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-30

### 📄 论文摘要

Large-scale instance-level training data is scarce, so models are typically trained on domain-specific datasets. Yet in real-world retrieval, they must handle diverse domains, making generalization to unseen data critical. We introduce ELViS, an image-to-image similarity model that generalizes effectively to unseen domains. Unlike conventional approaches, our model operates in similarity space rather than representation space, promoting cross-domain transfer. It leverages local descriptor correspondences, refines their similarities through an optimal transport step with data-dependent gains that suppress uninformative descriptors, and aggregates strong correspondences via a voting process into an image-level similarity. This design injects strong inductive biases, yielding a simple, efficient, and interpretable model. To assess generalization, we compile a benchmark of eight datasets spanning landmarks, artworks, products, and multi-domain collections, and evaluate ELViS as a re-ranking method. Our experiments show that ELViS outperforms competing methods by a large margin in out-of-domain scenarios and on average, while requiring only a fraction of their computational cost. Code available at: https://github.com/pavelsuma/ELViS/

### 🤖 AI 总结

**一句话总结**：ELViS提出一种基于局部描述子匹配与相似度空间建模的高效图像相似度方法，在跨域（未见域）检索重排序中显著优于现有方法且计算更省。

**研究动机**：大规模实例级训练数据稀缺导致模型常在单一域训练，但真实检索任务覆盖多种域，因此需要能强泛化到未见数据的相似度模型。

**核心方法**：ELViS不直接学习全局表征，而在“相似度空间”中利用局部描述子对应关系；通过带数据依赖增益的最优传输步骤抑制无信息描述子、精炼匹配相似度，并用投票式聚合强对应得到图像级相似度用于重排序。

**主要结论**：在作者构建的覆盖地标、艺术品、商品与多域集合的8数据集基准上，ELViS在域外场景与平均表现上大幅领先竞争方法，同时计算开销仅为其一小部分，体现出简单、可解释且高效的跨域泛化能力。

**关键词**：跨域图像检索, 图像相似度学习, 重排序, 局部特征描述子, 局部对应匹配, 最优传输, 数据依赖增益, 相似度空间, 投票聚合, 实例级检索评测基准

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28603v1) | [下载PDF](https://arxiv.org/pdf/2603.28603v1.pdf)

---

## cs.LG

## [19. Geometry-aware similarity metrics for neural representations on Riemannian and statistical manifolds](https://arxiv.org/abs/2603.28764v1)

**作者**：N Alex Cayco Gajic, Arthur Pellegrino  
**分类**：cs.LG, cs.AI, math.DG, q-bio.NC  
**发布时间**：2026-03-30

### 📄 论文摘要

Similarity measures are widely used to interpret the representational geometries used by neural networks to solve tasks. Yet, because existing methods compare the extrinsic geometry of representations in state space, rather than their intrinsic geometry, they may fail to capture subtle yet crucial distinctions between fundamentally different neural network solutions. Here, we introduce metric similarity analysis (MSA), a novel method which leverages tools from Riemannian geometry to compare the intrinsic geometry of neural representations under the manifold hypothesis. We show that MSA can be used to i) disentangle features of neural computations in deep networks with different learning regimes, ii) compare nonlinear dynamics, and iii) investigate diffusion models. Hence, we introduce a mathematically grounded and broadly applicable framework to understand the mechanisms behind neural computations by comparing their intrinsic geometries.

### 🤖 AI 总结

**一句话总结**：提出一种几何感知的表示相似度度量MSA，用黎曼几何比较神经表示的“内禀几何”，从而更准确地区分不同网络解法与动力学机制。

**研究动机**：现有表示相似性方法多比较状态空间中的外在几何，可能忽略表示流形的内在结构差异，导致无法捕捉本质不同但表面相近的神经网络解。

**核心方法**：在“流形假设”下引入Metric Similarity Analysis（MSA），利用黎曼几何工具在黎曼/统计流形上比较神经表示的内禀度量结构，从而在不依赖外在嵌入的情况下评估表示几何相似性。

**主要结论**：MSA能够区分不同学习机制下深度网络的计算特征、比较非线性动力学，并用于分析扩散模型，提供了一个数学上更扎实且通用的表示机制比较框架。

**关键词**：度量相似性分析（MSA）, 神经表征相似度, 内禀几何, 外禀几何, 黎曼几何, 统计流形, 流形假设, 表示几何分析, 非线性动力学比较, 扩散模型表征

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28764v1) | [下载PDF](https://arxiv.org/pdf/2603.28764v1.pdf)

---

## [20. Temporal Credit Is Free](https://arxiv.org/abs/2603.28750v1)

**作者**：Aur Shalev Merin  
**分类**：cs.LG  
**发布时间**：2026-03-30

### 📄 论文摘要

Recurrent networks do not need Jacobian propagation to adapt online. The hidden state already carries temporal credit through the forward pass; immediate derivatives suffice if you stop corrupting them with stale trace memory and normalize gradient scales across parameter groups. An architectural rule predicts when normalization is needed: \b{eta}2 is required when gradients must pass through a nonlinear state update with no output bypass, and unnecessary otherwise. Across ten architectures, real primate neural data, and streaming ML benchmarks, immediate derivatives with RMSprop match or exceed full RTRL, scaling to n = 1024 at 1000x less memory.

### 🤖 AI 总结

**一句话总结**：论文提出在线训练循环网络时无需传播雅可比或维护长时间迹（如RTRL），仅用“即时导数”并配合合适的梯度归一化即可获得与全RTRL相当甚至更好的效果，同时大幅降低内存开销。

**研究动机**：传统在线时序信用分配方法（如RTRL）内存/计算代价极高且难扩展，而常见近似又容易因“陈旧的迹记忆”导致梯度被污染、尺度失衡，从而影响在线适应能力。

**核心方法**：作者主张只使用前向传播中已隐含的时序信息来做信用分配，训练时仅依赖即时梯度，并通过RMSprop及按结构决定的归一化规则（当梯度需穿过无输出旁路的非线性状态更新时需要η²归一化，否则不需要）来稳定不同参数组的梯度尺度。

**主要结论**：在10种架构、真实灵长类神经数据与流式ML基准上，即时导数+RMSprop表现匹配或超过全RTRL，并在n=1024时以约1000倍更低内存实现可扩展的在线学习，说明“时序信用”在很大程度上已由隐藏状态的前向计算免费携带。

**关键词**：循环神经网络, 即时梯度, 雅可比传播, 梯度归一化, 状态更新非线性, 输出旁路, 流式基准, 内存优化

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28750v1) | [下载PDF](https://arxiv.org/pdf/2603.28750v1.pdf)

---

## [21. Stop Probing, Start Coding: Why Linear Probes and Sparse Autoencoders Fail at Compositional Generalisation](https://arxiv.org/abs/2603.28744v1)

**作者**：Vitória Barin Pacela, Shruti Joshi, Isabela Camacho 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-30

### 📄 论文摘要

The linear representation hypothesis states that neural network activations encode high-level concepts as linear mixtures. However, under superposition, this encoding is a projection from a higher-dimensional concept space into a lower-dimensional activation space, and a linear decision boundary in the concept space need not remain linear after projection. In this setting, classical sparse coding methods with per-sample iterative inference leverage compressed sensing guarantees to recover latent factors. Sparse autoencoders (SAEs), on the other hand, amortise sparse inference into a fixed encoder, introducing a systematic gap. We show this amortisation gap persists across training set sizes, latent dimensions, and sparsity levels, causing SAEs to fail under out-of-distribution (OOD) compositional shifts. Through controlled experiments that decompose the failure, we identify dictionary learning -- not the inference procedure -- as the binding constraint: SAE-learned dictionaries point in substantially wrong directions, and replacing the encoder with per-sample FISTA on the same dictionary does not close the gap. An oracle baseline proves the problem is solvable with a good dictionary at all scales tested. Our results reframe the SAE failure as a dictionary learning challenge, not an amortisation problem, and point to scalable dictionary learning as the key open problem for sparse inference under superposition.

### 🤖 AI 总结

**一句话总结**：在概念叠加（superposition）下，线性探针与稀疏自编码器在组合式OOD泛化中失败的关键不在“推断是否摊销”，而在于SAE学到的字典方向错误，导致无法可靠恢复潜在概念。

**研究动机**：线性表征假设常被用线性探针/SAE验证，但在叠加导致的“高维概念→低维激活”投影中，概念空间的线性可分性未必在激活空间保持线性，从而可能造成对“是否学到概念”的误判。作者希望解释为何SAE在组合式分布外迁移中系统失效，并定位瓶颈是在推断还是在字典学习。

**核心方法**：通过受控实验系统改变训练集规模、潜变量维度与稀疏度，比较经典逐样本迭代稀疏推断（如FISTA/压缩感知式推断）与SAE的摊销编码器，并将失败分解为“推断程序 vs 字典质量”的贡献。进一步在同一SAE字典上用逐样本FISTA替换编码器，以及引入“oracle好字典”基线来验证问题在各规模下可解。

**主要结论**：摊销差距在多种设置下持续存在并导致SAE在组合式OOD偏移下失败，但用FISTA替换SAE编码器也无法弥补，说明主要瓶颈是SAE学到的字典本身方向偏离严重。只要字典足够好（oracle），稀疏恢复与泛化是可行的，因此关键开放问题转向“可扩展的高质量字典学习”，而非单纯改进摊销推断。

**关键词**：线性表征假设, 组合泛化, 线性探针, 稀疏自编码器（SAE）, 稀疏编码, 压缩感知, 摊销推断差距, 字典学习, FISTA 迭代推断, 分布外（OOD）组合移位, 潜在因子恢复

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28744v1) | [下载PDF](https://arxiv.org/pdf/2603.28744v1.pdf)

---

## [22. Expectation Error Bounds for Transfer Learning in Linear Regression and Linear Neural Networks](https://arxiv.org/abs/2603.28739v1)

**作者**：Meitong Liu, Christopher Jung, Rui Li 等 5 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-03-30

### 📄 论文摘要

In transfer learning, the learner leverages auxiliary data to improve generalization on a main task. However, the precise theoretical understanding of when and how auxiliary data help remains incomplete. We provide new insights on this issue in two canonical linear settings: ordinary least squares regression and under-parameterized linear neural networks. For linear regression, we derive exact closed-form expressions for the expected generalization error with bias-variance decomposition, yielding necessary and sufficient conditions for auxiliary tasks to improve generalization on the main task. We also derive globally optimal task weights as outputs of solvable optimization programs, with consistency guarantees for empirical estimates. For linear neural networks with shared representations of width $q \leq K$, where $K$ is the number of auxiliary tasks, we derive a non-asymptotic expectation bound on the generalization error, yielding the first non-vacuous sufficient condition for beneficial auxiliary learning in this setting, as well as principled directions for task weight curation. We achieve this by proving a new column-wise low-rank perturbation bound for random matrices, which improves upon existing bounds by preserving fine-grained column structures. Our results are verified on synthetic data simulated with controlled parameters.

### 🤖 AI 总结

**一句话总结**：在两类线性模型（线性回归与欠参数线性神经网络）中，论文给出了迁移学习泛化误差的期望/上界表达，从而刻画辅助任务何时能提升主任务并如何最优加权。

**研究动机**：迁移学习常用辅助数据提升主任务泛化，但“辅助任务什么时候有用、为什么有用”缺少精确且可操作的理论条件与加权准则。

**核心方法**：在线性回归中推导泛化误差的精确闭式期望并做偏差-方差分解，进而给出辅助任务有益的充要条件与可解的全局最优任务权重优化（并证明经验估计一致性）；在线性神经网络中基于新的按列低秩扰动随机矩阵界，推导非渐近期望误差上界并据此提出任务加权/筛选方向。

**主要结论**：线性回归情形下可精确判定辅助任务是否改善主任务并计算最优权重；线性神经网络共享表征情形下得到首个非空洞的充分条件与加权指导，且理论在可控合成数据实验中得到验证。

**关键词**：迁移学习, 辅助任务, 线性回归, 最小二乘回归, 期望泛化误差, 偏差-方差分解, 任务权重优化, 线性神经网络, 共享表征, 非渐近误差界, 随机矩阵低秩扰动界, 列结构保持扰动界

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28739v1) | [下载PDF](https://arxiv.org/pdf/2603.28739v1.pdf)

---

## [23. See it to Place it: Evolving Macro Placements with Vision-Language Models](https://arxiv.org/abs/2603.28733v1)

**作者**：Ikechukwu Uchendu, Swati Goel, Karly Hou 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-30

### 📄 论文摘要

We propose using Vision-Language Models (VLMs) for macro placement in chip floorplanning, a complex optimization task that has recently shown promising advancements through machine learning methods. Because human designers rely heavily on spatial reasoning to arrange components on the chip canvas, we hypothesize that VLMs with strong visual reasoning abilities can effectively complement existing learning-based approaches. We introduce VeoPlace (Visual Evolutionary Optimization Placement), a novel framework that uses a VLM, without any fine-tuning, to guide the actions of a base placer by constraining them to subregions of the chip canvas. The VLM proposals are iteratively optimized through an evolutionary search strategy with respect to resulting placement quality. On open-source benchmarks, VeoPlace outperforms the best prior learning-based approach on 9 of 10 benchmarks with peak wirelength reductions exceeding 32%. We further demonstrate that VeoPlace generalizes to analytical placers, improving DREAMPlace performance on all 8 evaluated benchmarks with gains up to 4.3%. Our approach opens new possibilities for electronic design automation tools that leverage foundation models to solve complex physical design problems.

### 🤖 AI 总结

**一句话总结**：提出VeoPlace框架，利用无需微调的视觉-语言模型（VLM）通过进化搜索指导芯片宏单元布局，在多项基准上显著降低线长并可泛化到传统解析布局器。

**研究动机**：宏布局是高度依赖空间推理的复杂优化问题，而人类设计者常通过视觉理解来做布局决策；作者因此希望借助具备强视觉推理能力的VLM来补强现有学习式布局方法并提升泛化性。

**核心方法**：VeoPlace在每一步让VLM基于布局画布提出“将动作限制在某个子区域”的约束建议，不对VLM做微调；随后用进化搜索迭代筛选与优化这些VLM提案，以最终布局质量（如线长）为适应度来驱动改进，并与底层布局器协同生成结果。

**主要结论**：在开源基准上，VeoPlace相较此前最佳学习方法在10个中有9个更优，峰值线长降低超过32%；同时它还能迁移到解析布局器（如DREAMPlace），在全部8个基准上带来最高4.3%的性能提升，显示基础模型可有效赋能EDA物理设计优化。

**关键词**：宏单元布局, 芯片楼层规划, 视觉语言模型, 无微调推理, 进化搜索优化, 子区域约束, 基准布局器引导, 线长优化, 开源基准评测, 解析布局器集成

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28733v1) | [下载PDF](https://arxiv.org/pdf/2603.28733v1.pdf)

---

## [24. Stepwise Credit Assignment for GRPO on Flow-Matching Models](https://arxiv.org/abs/2603.28718v1)

**作者**：Yash Savani, Branislav Kveton, Yuchen Liu 等 8 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-03-30

### 📄 论文摘要

Flow-GRPO successfully applies reinforcement learning to flow models, but uses uniform credit assignment across all steps. This ignores the temporal structure of diffusion generation: early steps determine composition and content (low-frequency structure), while late steps resolve details and textures (high-frequency details). Moreover, assigning uniform credit based solely on the final image can inadvertently reward suboptimal intermediate steps, especially when errors are corrected later in the diffusion trajectory. We propose Stepwise-Flow-GRPO, which assigns credit based on each step's reward improvement. By leveraging Tweedie's formula to obtain intermediate reward estimates and introducing gain-based advantages, our method achieves superior sample efficiency and faster convergence. We also introduce a DDIM-inspired SDE that improves reward quality while preserving stochasticity for policy gradients.

### 🤖 AI 总结

**一句话总结**：提出Stepwise-Flow-GRPO，在扩散/flow生成过程中按“每一步对奖励的增益”分配信用，从而提升样本效率并加速收敛。

**研究动机**：现有Flow-GRPO对所有扩散步统一分配信用，忽略了早期步决定全局结构、后期步决定细节的时序差异；仅用最终图像回传奖励还可能错误奖励被后续纠正的中间失误。

**核心方法**：利用Tweedie公式为中间状态构造奖励估计，并用“增益(gain)-based advantage”将信用分配到各步的奖励改进上；同时引入受DDIM启发的SDE，在保持策略梯度所需随机性的前提下提高中间奖励信号质量。

**主要结论**：Stepwise-Flow-GRPO相较均匀信用分配的Flow-GRPO具备更好的样本效率与更快的训练收敛，并能更合理地区分不同扩散步对最终质量的贡献。

**关键词**：流匹配模型, 扩散生成, 强化学习微调, 中间奖励估计, 增益优势函数, 策略梯度, 采样效率, 收敛加速

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28718v1) | [下载PDF](https://arxiv.org/pdf/2603.28718v1.pdf)

---

## [25. GPU-Accelerated Optimization of Transformer-Based Neural Networks for Real-Time Inference](https://arxiv.org/abs/2603.28708v1)

**作者**：Soutrik Mukherjee, Sangwhan Cha  
**分类**：cs.LG, cs.DC  
**发布时间**：2026-03-30

### 📄 论文摘要

This paper presents the design and evaluation of a GPU-accelerated inference pipeline for transformer models using NVIDIA TensorRT with mixed-precision optimization. We evaluate BERT-base (110M parameters) and GPT-2 (124M parameters) across batch sizes from 1 to 32 and sequence lengths from 32 to 512. The system achieves up to 64.4x speedup over CPU baselines, sub-10 ms latency for single-sample inference, and a 63 percent reduction in memory usage. We introduce a hybrid precision strategy that preserves FP32 for numerically sensitive operations such as softmax and layer normalization, while applying FP16 to linear layers. This approach maintains high numerical fidelity (cosine similarity >= 0.9998 relative to baseline outputs) and eliminates NaN instability. The pipeline is implemented as a modular, containerized system that enables reproducible benchmarking across more than 360 configurations. Cross-GPU validation on an NVIDIA A100 shows consistent FP16 speedup ratios between 1.84x and 2.00x, along with stable numerical behavior. Downstream evaluation on SST-2 demonstrates no accuracy degradation under hybrid precision. Validation on WikiText-2 shows that random inputs underestimate NaN instability by up to 6x for full FP16, while confirming the robustness of the hybrid approach (0.0 percent NaN, cosine similarity >= 0.9998). These results provide a detailed characterization of performance and accuracy trade-offs across GPU architectures and offer practical guidance for deploying transformer models in latency-critical environments.

### 🤖 AI 总结

**一句话总结**：论文提出并评估了一套基于TensorRT的Transformer GPU混合精度推理方案，在保持几乎无精度损失与无NaN的前提下实现显著加速与内存节省，满足实时低延迟部署需求。

**研究动机**：Transformer在实时场景中常受CPU推理慢、GPU全FP16易数值不稳定（NaN）以及显存占用高的限制，需要系统化刻画性能/精度权衡并给出可落地的优化策略。

**核心方法**：使用NVIDIA TensorRT构建模块化、容器化推理流水线，对BERT-base与GPT-2在不同batch/序列长度下进行混合精度优化与基准测试；提出“混合精度保真策略”：对softmax、LayerNorm等敏感算子保留FP32，线性层等使用FP16，并用余弦相似度与NaN率做数值验证，同时跨GPU(A100)与下游任务(SST-2、WikiText-2)验证稳健性。

**主要结论**：该方案相对CPU最高提速64.4×、单样本延迟可低于10ms且显存减少约63%，在A100上FP16加速比稳定在1.84×~2.00×；混合精度在余弦相似度≥0.9998且NaN为0的情况下不降低SST-2准确率，并指出随机输入会显著低估全FP16的NaN风险（最高约6×）。

**关键词**：GPU 推理加速, 混合精度推理, FP16 线性层, 层归一化稳定性, NaN 稳定性评测, 推理延迟基准, 容器化基准框架, 跨 GPU 性能验证

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28708v1) | [下载PDF](https://arxiv.org/pdf/2603.28708v1.pdf)

---

## [26. Subspace Optimization for Backpropagation-Free Continual Test-Time Adaptation](https://arxiv.org/abs/2603.28678v1)

**作者**：Damian Sójka, Sebastian Cygert, Marc Masana  
**分类**：cs.LG  
**发布时间**：2026-03-30

### 📄 论文摘要

We introduce PACE, a backpropagation-free continual test-time adaptation system that directly optimizes the affine parameters of normalization layers. Existing derivative-free approaches struggle to balance runtime efficiency with learning capacity, as they either restrict updates to input prompts or require continuous, resource-intensive adaptation regardless of domain stability. To address these limitations, PACE leverages the Covariance Matrix Adaptation Evolution Strategy with the Fastfood projection to optimize high-dimensional affine parameters within a low-dimensional subspace, leading to superior adaptive performance. Furthermore, we enhance the runtime efficiency by incorporating an adaptation stopping criterion and a domain-specialized vector bank to eliminate redundant computation. Our framework achieves state-of-the-art accuracy across multiple benchmarks under continual distribution shifts, reducing runtime by over 50% compared to existing backpropagation-free methods.

### 🤖 AI 总结

**一句话总结**：PACE提出一种无需反向传播的持续测试时自适应方法，在归一化层仿射参数的低维子空间中进行高效优化，实现更高精度与更低运行开销。

**研究动机**：现有无梯度测试时自适应方法要么更新能力受限（如只调输入prompt），要么在域稳定时仍持续适应导致计算浪费，难以兼顾效果与效率。

**核心方法**：使用CMA-ES在Fastfood投影构建的低维子空间中直接优化归一化层的高维仿射参数；同时引入自适应停止准则与“域专用向量库”复用已学到的域信息，减少冗余更新与计算。

**主要结论**：在持续分布漂移的多个基准上达到SOTA准确率，并相对现有无反向传播方法将运行时间降低超过50%，且在域稳定阶段能显著避免不必要的适应开销。

**关键词**：无反向传播, 持续测试时自适应, 归一化层仿射参数, 子空间优化, 导数自由优化, 自适应停止准则, 领域特化向量库, 持续分布漂移评测

**评分**：67

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28678v1) | [下载PDF](https://arxiv.org/pdf/2603.28678v1.pdf)

---

## [27. FL-PBM: Pre-Training Backdoor Mitigation for Federated Learning](https://arxiv.org/abs/2603.28673v1)

**作者**：Osama Wehbi, Sarhad Arisdakessian, Omar Abdel Wahab 等 6 位作者  
**分类**：cs.LG, cs.CR, cs.DC  
**发布时间**：2026-03-30

### 📄 论文摘要

Backdoor attacks pose a significant threat to the integrity and reliability of Artificial Intelligence (AI) models, enabling adversaries to manipulate model behavior by injecting poisoned data with hidden triggers. These attacks can lead to severe consequences, especially in critical applications such as autonomous driving, healthcare, and finance. Detecting and mitigating backdoor attacks is crucial across the lifespan of model's phases, including pre-training, in-training, and post-training. In this paper, we propose Pre-Training Backdoor Mitigation for Federated Learning (FL-PBM), a novel defense mechanism that proactively filters poisoned data on the client side before model training in a federated learning (FL) environment. The approach consists of three stages: (1) inserting a benign trigger into the data to establish a controlled baseline, (2) applying Principal Component Analysis (PCA) to extract discriminative features and assess the separability of the data, (3) performing Gaussian Mixture Model (GMM) clustering to identify potentially malicious data samples based on their distribution in the PCA-transformed space, and (4) applying a targeted blurring technique to disrupt potential backdoor triggers. Together, these steps ensure that suspicious data is detected early and sanitized effectively, thereby minimizing the influence of backdoor triggers on the global model. Experimental evaluations on image-based datasets demonstrate that FL-PBM reduces attack success rates by up to 95% compared to baseline federated learning (FedAvg) and by 30 to 80% relative to state-of-the-art defenses (RDFL and LPSF). At the same time, it maintains over 90% clean model accuracy in most experiments, achieving better mitigation without degrading model performance.

### 🤖 AI 总结

**一句话总结**：FL-PBM是一种面向联邦学习的“预训练阶段”后门防御方法，通过在客户端训练前检测并净化可疑样本来显著降低后门攻击成功率且保持较高干净准确率。

**研究动机**：联邦学习中客户端数据不可见使后门更难发现，而现有防御多集中在训练中/训练后；因此需要在训练前就能在本地识别并削弱投毒触发器影响的主动防御。

**核心方法**：方法在客户端侧进行预过滤与净化：先插入良性触发器建立对照基线，再用PCA提取判别特征并评估可分性，随后在PCA空间用GMM聚类定位分布异常的潜在恶意样本，最后对可疑样本施加定向模糊以破坏触发器。

**主要结论**：在图像数据集实验中，FL-PBM相较FedAvg最高将攻击成功率降低约95%，相较RDFL/LPSF再降约30%–80%，同时多数设置下保持90%以上的干净精度，体现了更强的后门缓解与较小性能损失。

**关键词**：联邦学习, 后门攻击, 预训练防御, 客户端数据过滤, 良性触发器注入, 主成分分析（PCA）, 高斯混合模型（GMM）, 聚类异常检测, 触发器模糊净化, 攻击成功率, 干净准确率

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28673v1) | [下载PDF](https://arxiv.org/pdf/2603.28673v1.pdf)

---

## [28. AMIGO: Agentic Multi-Image Grounding Oracle Benchmark](https://arxiv.org/abs/2603.28662v1)

**作者**：Min Wang, Ata Mahjoubfar  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-30

### 📄 论文摘要

Agentic vision-language models increasingly act through extended interactions, but most evaluations still focus on single-image, single-turn correctness. We introduce AMIGO (Agentic Multi-Image Grounding Oracle Benchmark), a long-horizon benchmark for hidden-target identification over galleries of visually similar images. In AMIGO, the oracle privately selects a target image, and the model must recover it by asking a sequence of attribute-focused Yes/No/Unsure questions under a strict protocol that penalizes invalid actions with Skip. This setting stresses (i) question selection under uncertainty, (ii) consistent constraint tracking across turns, and (iii) fine-grained discrimination as evidence accumulates. AMIGO also supports controlled oracle imperfections to probe robustness and verification behavior under inconsistent feedback. We instantiate AMIGO with Guess My Preferred Dress task and report metrics covering both outcomes and interaction quality, including identification success, evidence verification, efficiency, protocol compliance, noise tolerance, and trajectory-level diagnostics.

### 🤖 AI 总结

**一句话总结**：AMIGO 提出一个长时序、多图像的“隐藏目标识别”基准，用严格交互协议评测视觉语言模型在连续提问、约束跟踪与细粒度判别上的代理式能力。

**研究动机**：现有评测多停留在单图单轮问答，难以衡量模型在多轮交互中如何在不确定性下选择问题、累积证据并保持一致推理。作者希望用更接近“代理式检索/定位”的设置，系统测量模型的策略质量与稳健性。

**核心方法**：基准中由“oracle”私下选定目标图像，模型必须在一组相似图片中通过连续的属性型 Yes/No/Unsure 问题逐步缩小范围，并遵守会对无效动作判为 Skip 的严格协议。AMIGO 还可注入受控的 oracle 噪声/不一致反馈，并用包含成功率、效率、合规性、证据验证与轨迹诊断等指标进行评估（实例任务为 Guess My Preferred Dress）。

**主要结论**：AMIGO 能同时评估结果与交互过程质量，突出模型在长程对话中的提问策略、约束一致性维护以及随证据累积的细粒度区分能力。引入不完美 oracle 后还能检验模型对矛盾反馈的容错与验证行为，从而更全面刻画代理式 VLM 的可靠性。

**关键词**：多图像指代定位, 长时序交互评测, 隐目标识别, 属性问答策略, 是非不确定反馈, 约束一致性跟踪, 细粒度视觉区分, 噪声鲁棒性, 证据验证, 交互效率指标, 轨迹级诊断

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28662v1) | [下载PDF](https://arxiv.org/pdf/2603.28662v1.pdf)

---

## [29. Information-Theoretic Limits of Safety Verification for Self-Improving Systems](https://arxiv.org/abs/2603.28650v1)

**作者**：Arsenios Scrivens  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-03-30

### 📄 论文摘要

Can a safety gate permit unbounded beneficial self-modification while maintaining bounded cumulative risk? We formalize this question through dual conditions -- requiring sum delta_n < infinity (bounded risk) and sum TPR_n = infinity (unbounded utility) -- and establish a theory of their (in)compatibility.   Classification impossibility (Theorem 1): For power-law risk schedules delta_n = O(n^{-p}) with p > 1, any classifier-based gate under overlapping safe/unsafe distributions satisfies TPR_n <= C_alpha * delta_n^beta via Holder's inequality, forcing sum TPR_n < infinity. This impossibility is exponent-optimal (Theorem 3). A second independent proof via the NP counting method (Theorem 4) yields a 13% tighter bound without Holder's inequality.   Universal finite-horizon ceiling (Theorem 5): For any summable risk schedule, the exact maximum achievable classifier utility is U*(N, B) = N * TPR_NP(B/N), growing as exp(O(sqrt(log N))) -- subpolynomial. At N = 10^6 with budget B = 1.0, a classifier extracts at most U* ~ 87 versus a verifier's ~500,000.   Verification escape (Theorem 2): A Lipschitz ball verifier achieves delta = 0 with TPR > 0, escaping the impossibility. Formal Lipschitz bounds for pre-LayerNorm transformers under LoRA enable LLM-scale verification. The separation is strict. We validate on GPT-2 (d_LoRA = 147,456): conditional delta = 0 with TPR = 0.352. Comprehensive empirical validation is in the companion paper [D2].

### 🤖 AI 总结

**一句话总结**：Can a safety gate permit unbounded beneficial self-modification while maintaining bounded cumulative risk? We formalize this question through dual conditions -- requiring sum delta_n < infinity (bound...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：信息论极限, 安全门控分类器, 累计风险预算, 真阳性率上界, 幂律风险调度, 分布重叠不可判别, LoRA 参数扰动验证, Information-Theoretic

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28650v1) | [下载PDF](https://arxiv.org/pdf/2603.28650v1.pdf)

---

## [30. LACE: Loss-Adaptive Capacity Expansion for Continual Learning](https://arxiv.org/abs/2603.28611v1)

**作者**：Shivnath Tathe  
**分类**：cs.LG  
**发布时间**：2026-03-30

### 📄 论文摘要

Fixed representational capacity is a fundamental constraint in continual learning: practitioners must guess an appropriate model width before training, without knowing how many distinct concepts the data contains. We propose LACE (Loss-Adaptive Capacity Expansion), a simple online mechanism that expands a model's representational capacity during training by monitoring its own loss signal. When sustained loss deviation exceeds a threshold - indicating that the current capacity is insufficient for newly encountered data - LACE adds new dimensions to the projection layer and trains them jointly with existing parameters. Across synthetic and real-data experiments, LACE triggers expansions exclusively at domain boundaries (100% boundary precision, zero false positives), matches the accuracy of a large fixed-capacity model while starting from a fraction of its dimensions, and produces adapter dimensions that are collectively critical to performance (3% accuracy drop when all adapters removed). We further demonstrate unsupervised domain separation in GPT-2 activations via layer-wise clustering, showing a U-shaped separability curve across layers that motivates adaptive capacity allocation in deep networks. LACE requires no labels, no replay buffers, and no external controllers, making it suitable for on-device continual learning under resource constraints.

### 🤖 AI 总结

**一句话总结**：LACE通过监控训练损失在持续学习过程中按需扩展模型投影层维度，使小模型在遇到新域/新概念时自适应增容并达到接近大模型的性能。

**研究动机**：持续学习中固定容量要求预先猜测模型宽度，但任务/概念数未知，容易出现容量不足导致遗忘或性能下降。作者希望在无标签、无回放、无外部控制器的条件下，让模型在检测到“新域带来持续性损失偏移”时自动扩容。

**核心方法**：LACE在线监控损失信号，当损失在一段时间内持续偏离并超过阈值（指示当前表示容量不足）时，向投影层追加新的维度/适配器参数，并与原参数联合训练。扩容触发仅依赖损失统计，不需要域标签或额外模块；并通过对GPT-2各层激活做无监督聚类分析域可分性，为深层网络中“按层自适应分配容量”提供依据。

**主要结论**：实验表明LACE能在域边界处精准触发扩容（报告为100%边界精度、零误报），从较小初始维度出发达到与大固定容量模型相当的准确率。新增维度对性能确有贡献（移除全部适配器维度约导致3%准确率下降），且GPT-2激活的域可分性随层呈U形变化，支持在不同层进行自适应容量配置的动机。

**关键词**：持续学习, 自适应容量扩展, 损失信号监测, 投影层扩展, 适配器维度, 域边界检测, 无回放学习, 无监督域分离, GPT-2 激活聚类, 资源受限设备端学习

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.28611v1) | [下载PDF](https://arxiv.org/pdf/2603.28611v1.pdf)

---

