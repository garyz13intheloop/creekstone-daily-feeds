# arXiv AI 论文日报 | 2026-03-10

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (13 篇)
- [cs.LG](#csLG) (12 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. Agentic Critical Training](https://arxiv.org/abs/2603.08706v1)

**作者**：Weize Liu, Minghui Liu, Sy-Tuyen Ho 等 6 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-03-09

### 📄 论文摘要

Training large language models (LLMs) as autonomous agents often begins with imitation learning, but it only teaches agents what to do without understanding why: agents never contrast successful actions against suboptimal alternatives and thus lack awareness of action quality. Recent approaches attempt to address this by introducing self-reflection supervision derived from contrasts between expert and alternative actions. However, the training paradigm fundamentally remains imitation learning: the model imitates pre-constructed reflection text rather than learning to reason autonomously. We propose Agentic Critical Training (ACT), a reinforcement learning paradigm that trains agents to identify the better action among alternatives. By rewarding whether the model's judgment is correct, ACT drives the model to autonomously develop reasoning about action quality, producing genuine self-reflection rather than imitating it. Across three challenging agent benchmarks, ACT consistently improves agent performance when combined with different post-training methods. It achieves an average improvement of 5.07 points over imitation learning and 4.62 points over reinforcement learning. Compared to approaches that inject reflection capability through knowledge distillation, ACT also demonstrates clear advantages, yielding an average improvement of 2.42 points. Moreover, ACT enables strong out-of-distribution generalization on agentic benchmarks and improves performance on general reasoning benchmarks without any reasoning-specific training data, highlighting the value of our method. These results suggest that ACT is a promising path toward developing more reflective and capable LLM agents.

### 🤖 AI 总结

**一句话总结**：ACT用强化学习训练LLM代理在备选行动中做出更优判断，从而学会真正的自我反思并提升多项代理与推理基准表现。

**研究动机**：模仿学习只教“做什么”而不教“为何更好”，代理缺乏对行动质量的对比与评估能力；现有自反思监督多为模仿预先构造的反思文本，难以形成自主推理。

**核心方法**：提出Agentic Critical Training：给定专家与替代行动等候选，模型输出对“哪个更好”的判断，并以判断正确与否作为奖励进行强化学习训练，以促使模型自发学习行动质量推理而非模仿反思措辞。

**主要结论**：ACT在三个高难代理基准上与不同后训练方法结合均稳定提升，平均较模仿学习+5.07、较常规RL+4.62，并优于反思蒸馏类方法+2.42；同时具备更强OOD泛化，并在无推理专用数据下提升通用推理基准表现。

**关键词**：LLM智能体训练, 强化学习后训练, 动作质量评估, 行动偏好排序, 自反思生成, 模仿学习局限, 智能体基准评测, 分布外泛化

**评分**：46

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08706v1) | [下载PDF](https://arxiv.org/pdf/2603.08706v1.pdf)

---

## [2. Evaluating Financial Intelligence in Large Language Models: Benchmarking SuperInvesting AI with LLM Engines](https://arxiv.org/abs/2603.08704v1)

**作者**：Akshay Gulati, Kanha Singhania, Tushar Banga 等 11 位作者  
**分类**：cs.AI  
**发布时间**：2026-03-09

### 📄 论文摘要

Large language models are increasingly used for financial analysis and investment research, yet systematic evaluation of their financial reasoning capabilities remains limited. In this work, we introduce the AI Financial Intelligence Benchmark (AFIB), a multi-dimensional evaluation framework designed to assess financial analysis capabilities across five dimensions: factual accuracy, analytical completeness, data recency, model consistency, and failure patterns. We evaluate five AI systems: GPT, Gemini, Perplexity, Claude, and SuperInvesting, using a dataset of 95+ structured financial analysis questions derived from real-world equity research tasks. The results reveal substantial differences in performance across models. Within this benchmark setting, SuperInvesting achieves the highest aggregate performance, with an average factual accuracy score of 8.96/10 and the highest completeness score of 56.65/70, while also demonstrating the lowest hallucination rate among evaluated systems. Retrieval-oriented systems such as Perplexity perform strongly on data recency tasks due to live information access but exhibit weaker analytical synthesis and consistency. Overall, the results highlight that financial intelligence in large language models is inherently multi-dimensional, and systems that combine structured financial data access with analytical reasoning capabilities provide the most reliable performance for complex investment research workflows.

### 🤖 AI 总结

**一句话总结**：论文提出并使用AFIB基准从多维度评测LLM的金融分析能力，发现结合结构化金融数据与推理能力的系统（如SuperInvesting）整体表现最佳。

**研究动机**：尽管LLM被广泛用于金融研究，但其金融推理能力缺乏系统、可重复的评测框架，导致难以比较不同系统的可靠性与失效方式。

**核心方法**：构建AI Financial Intelligence Benchmark（AFIB），从事实准确性、分析完整性、数据新鲜度、一致性与失败模式五个维度评估，并用95+源自真实股票研究任务的结构化问题对GPT、Gemini、Perplexity、Claude与SuperInvesting进行对比测试。

**主要结论**：在该基准下SuperInvesting取得最高总体表现（准确性8.96/10、完整性56.65/70且幻觉率最低）；检索导向系统如Perplexity在数据新鲜度上占优但综合分析与一致性较弱，说明金融智能是多维能力，需数据访问与推理能力结合才能更可靠。

**关键词**：金融推理评测, LLM 评测基准, 多维度评测框架, 事实准确性, 分析完整性, 数据时效性, 模型一致性, 幻觉率, 失败模式分析, 检索增强生成（RAG）, 股权研究问答数据集

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08704v1) | [下载PDF](https://arxiv.org/pdf/2603.08704v1.pdf)

---

## [3. A Multi-Objective Optimization Approach for Sustainable AI-Driven Entrepreneurship in Resilient Economies](https://arxiv.org/abs/2603.08692v1)

**作者**：Anas ALsobeh, Raneem Alkurdi  
**分类**：cs.AI  
**发布时间**：2026-03-09

### 📄 论文摘要

The rapid advancement of artificial intelligence (AI) technologies presents both unprecedented opportunities and significant challenges for sustainable economic development. While AI offers transformative potential for addressing environmental challenges and enhancing economic resilience, its deployment often involves substantial energy consumption and environmental costs. This research introduces the EcoAI-Resilience framework, a multi-objective optimization approach designed to maximize the sustainability benefits of AI deployment while minimizing environmental costs and enhancing economic resilience. The framework addresses three critical objectives through mathematical optimization: sustainability impact maximization, economic resilience enhancement, and environmental cost minimization. The methodology integrates diverse data sources, including energy consumption metrics, sustainability indicators, economic performance data, and entrepreneurship outcomes across 53 countries and 14 sectors from 2015-2024. Our experimental validation demonstrates exceptional performance with R scores exceeding 0.99 across all model components, significantly outperforming baseline methods, including Linear Regression (R = 0.943), Random Forest (R = 0.957), and Gradient Boosting (R = 0.989). The framework successfully identifies optimal AI deployment strategies featuring 100\% renewable energy integration, 80% efficiency improvement targets, and optimal investment levels of $202.48 per capita. Key findings reveal strong correlations between economic complexity and resilience (r = 0.82), renewable energy adoption and sustainability outcomes (r = 0.71), and demonstrate significant temporal improvements in AI readiness (+1.12 points/year) and renewable energy adoption (+0.67 year) globally.

### 🤖 AI 总结

**一句话总结**：提出EcoAI-Resilience多目标优化框架，在53国14行业数据上同时优化AI部署的可持续性、经济韧性与环境成本，并给出可实现的最优策略组合。

**研究动机**：AI应用能提升绿色转型与经济韧性，但其能耗与环境代价可能抵消收益；因此需要一个能在多重目标间权衡、指导AI可持续部署与创业投资的系统方法。

**核心方法**：构建包含“可持续影响最大化、经济韧性增强、环境成本最小化”的数学多目标优化框架，融合2015-2024年跨国家/行业的能耗指标、可持续性指标、经济表现与创业产出等多源数据进行建模与验证，并与线性回归、随机森林、梯度提升等基线比较。

**主要结论**：实验显示各组件R>0.99，整体优于基线模型，并识别出包含100%可再生能源接入、80%效率提升目标与人均约202.48美元投资的最优部署策略；同时发现经济复杂度与韧性强相关(r=0.82)、可再生能源采用与可持续结果相关(r=0.71)，且全球AI就绪度与可再生能源采用率呈显著逐年提升。

**关键词**：多目标优化, 可持续计算, 绿色AI, 能源消耗建模, 环境成本最小化, 可再生能源集成, 经济韧性评估, 创业绩效, 经济复杂度, AI就绪度, 跨国面板数据

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08692v1) | [下载PDF](https://arxiv.org/pdf/2603.08692v1.pdf)

---

## [4. OfficeQA Pro: An Enterprise Benchmark for End-to-End Grounded Reasoning](https://arxiv.org/abs/2603.08655v1)

**作者**：Krista Opsahl-Ong, Arnav Singhvi, Jasmine Collins 等 13 位作者  
**分类**：cs.AI, cs.CL, cs.IR  
**发布时间**：2026-03-09

### 📄 论文摘要

We introduce OfficeQA Pro, a benchmark for evaluating AI agents on grounded, multi-document reasoning over a large and heterogeneous document corpus. The corpus consists of U.S. Treasury Bulletins spanning nearly 100 years, comprising 89,000 pages and over 26 million numerical values. OfficeQA Pro consists of 133 questions that require precise document parsing, retrieval, and analytical reasoning across both unstructured text and tabular data. Frontier LLMs including Claude Opus 4.6, GPT-5.4, and Gemini 3.1 Pro Preview achieve less than 5% accuracy on OfficeQA Pro when relying on parametric knowledge, and less than 12% with additional access to the web. When provided directly with the document corpus, frontier agents still struggle on over half of questions, scoring 34.1% on average. We find that providing agents with a structured document representation produced by Databricks' ai_parse_document yields a 16.1% average relative performance gain across agents. We conduct additional ablations to study the effects of model selection, table representation, retrieval strategy, and test-time scaling on performance. Despite these improvements, significant headroom remains before agents can be considered reliable at enterprise-grade grounded reasoning.

### 🤖 AI 总结

**一句话总结**：OfficeQA Pro 是一个面向企业场景的端到端“有据可依”多文档推理基准，显示当前前沿LLM/智能体在真实文档检索与表格数值推理上仍明显不可靠。

**研究动机**：现实企业知识常分散在大量异构文档（含文本与表格）中，单靠模型参数知识或联网检索难以保证可追溯与精确计算，因此需要更贴近真实工作的评测来量化短板。

**核心方法**：构建基于近百年美国财政部公告的超大文档语料（89,000页、2,600万数值）与133道问题，评测从解析→检索→跨文档分析推理的端到端能力，并通过消融比较模型选择、表格表示、检索策略、测试时扩展，以及引入结构化文档表示（ai_parse_document）的效果。

**主要结论**：前沿模型在仅依赖参数知识时准确率<5%，加上网页也<12%；即便直接提供完整语料平均也仅34.1%，且过半问题仍失败，而结构化文档表示可带来约16.1%的相对提升但仍有大量提升空间。

**关键词**：企业级基准, 多文档推理, 信息检索, 表格问答, 数值推理, RAG, 结构化文档表示, 测试时扩展

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08655v1) | [下载PDF](https://arxiv.org/pdf/2603.08655v1.pdf)

---

## [5. CoCo: Code as CoT for Text-to-Image Preview and Rare Concept Generation](https://arxiv.org/abs/2603.08652v1)

**作者**：Haodong Li, Chunmei Qing, Huanyu Zhang 等 13 位作者  
**分类**：cs.AI  
**发布时间**：2026-03-09

### 📄 论文摘要

Recent advancements in Unified Multimodal Models (UMMs) have significantly advanced text-to-image (T2I) generation, particularly through the integration of Chain-of-Thought (CoT) reasoning. However, existing CoT-based T2I methods largely rely on abstract natural-language planning, which lacks the precision required for complex spatial layouts, structured visual elements, and dense textual content. In this work, we propose CoCo (Code-as-CoT), a code-driven reasoning framework that represents the reasoning process as executable code, enabling explicit and verifiable intermediate planning for image generation. Given a text prompt, CoCo first generates executable code that specifies the structural layout of the scene, which is then executed in a sandboxed environment to render a deterministic draft image. The model subsequently refines this draft through fine-grained image editing to produce the final high-fidelity result. To support this training paradigm, we construct CoCo-10K, a curated dataset containing structured draft-final image pairs designed to teach both structured draft construction and corrective visual refinement. Empirical evaluations on StructT2IBench, OneIG-Bench, and LongText-Bench show that CoCo achieves improvements of +68.83%, +54.8%, and +41.23% over direct generation, while also outperforming other generation methods empowered by CoT. These results demonstrate that executable code is an effective and reliable reasoning paradigm for precise, controllable, and structured text-to-image generation. The code is available at: https://github.com/micky-li-hd/CoCo

### 🤖 AI 总结

**一句话总结**：CoCo 用“可执行代码”替代自然语言式 CoT 规划，先生成可验证的结构草图再精修，从而显著提升复杂布局与长文本的文本到图像生成质量与可控性。

**研究动机**：现有 CoT 驱动的 T2I 多用抽象自然语言规划，难以精确表达空间布局、结构化元素与密集文字，且中间步骤不可执行、不可验证，导致复杂场景生成不稳定。

**核心方法**：给定文本提示，模型先生成描述场景结构与布局的可执行代码，在沙箱环境执行渲染出确定性的草稿图，再通过细粒度图像编辑对草稿进行纠错与细化得到最终高保真图像；并构建 CoCo-10K 草稿-成图配对数据集用于联合训练“结构草图构建+视觉精修”。

**主要结论**：在 StructT2IBench、OneIG-Bench、LongText-Bench 上，相比直接生成分别提升 +68.83%、+54.8%、+41.23%，且优于其他 CoT 增强方法，表明“代码即推理”能提供更可靠的中间规划与更强的可控结构化生成能力。

**关键词**：文本到图像生成, 可控生成, 结构化场景布局, 长文本渲染, 稀有概念生成, 代码驱动推理, 可执行代码规划, 沙箱执行, 确定性草图渲染, 图像编辑精修, 结构化评测基准

**评分**：41

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08652v1) | [下载PDF](https://arxiv.org/pdf/2603.08652v1.pdf)

---

## cs.CV

## [6. Scale Space Diffusion](https://arxiv.org/abs/2603.08709v1)

**作者**：Soumik Mukhopadhyay, Prateksha Udhayanan, Abhinav Shrivastava  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-09

### 📄 论文摘要

Diffusion models degrade images through noise, and reversing this process reveals an information hierarchy across timesteps. Scale-space theory exhibits a similar hierarchy via low-pass filtering. We formalize this connection and show that highly noisy diffusion states contain no more information than small, downsampled images - raising the question of why they must be processed at full resolution. To address this, we fuse scale spaces into the diffusion process by formulating a family of diffusion models with generalized linear degradations and practical implementations. Using downsampling as the degradation yields our proposed Scale Space Diffusion. To support Scale Space Diffusion, we introduce Flexi-UNet, a UNet variant that performs resolution-preserving and resolution-increasing denoising using only the necessary parts of the network. We evaluate our framework on CelebA and ImageNet and analyze its scaling behavior across resolutions and network depths. Our project website ( https://prateksha.github.io/projects/scale-space-diffusion/ ) is available publicly.

### 🤖 AI 总结

**一句话总结**：提出将“尺度空间”的降采样退化融入扩散过程（Scale Space Diffusion），并配合可变分辨率的Flexi-UNet，在高噪声阶段用更低分辨率计算以提升效率且保持生成质量。

**研究动机**：扩散模型在高噪声时间步包含的信息量与低分辨率小图相当，却仍需全分辨率处理，造成不必要的计算开销。作者希望利用尺度空间的层级信息结构，让不同时间步在“足够的”分辨率上进行去噪。

**核心方法**：将标准加噪扩散推广为“广义线性退化”的扩散族，并用下采样作为退化算子实现Scale Space Diffusion，使扩散状态随时间步自然对应不同尺度/分辨率。为适配该流程，提出Flexi-UNet：在分辨率保持与提升的去噪中，仅启用UNet中必要的子网络模块以支持跨尺度推理与训练。

**主要结论**：在CelebA与ImageNet上验证该框架可在多分辨率与不同网络深度下良好扩展，表明高噪声阶段用低分辨率处理是可行的，并能在不显著损失效果的前提下降低计算成本/提高效率。

**关键词**：Diffusion, 尺度空间理论, 多分辨率生成, 下采样退化, 广义线性退化, 信息层级, 分辨率自适应去噪, 计算效率, 图像生成, 分辨率缩放规律

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08709v1) | [下载PDF](https://arxiv.org/pdf/2603.08709v1.pdf)

---

## [7. FVG-PT: Adaptive Foreground View-Guided Prompt Tuning for Vision-Language Models](https://arxiv.org/abs/2603.08708v1)

**作者**：Haoyang Li, Liang Wang, Siyu Zhou 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-09

### 📄 论文摘要

CLIP-based prompt tuning enables pretrained Vision-Language Models (VLMs) to efficiently adapt to downstream tasks. Although existing studies have made significant progress, they pay limited attention to changes in the internal attention representations of VLMs during the tuning process. In this paper, we attribute the failure modes of prompt tuning predictions to shifts in foreground attention of the visual encoder, and propose Foreground View-Guided Prompt Tuning (FVG-PT), an adaptive plug-and-play foreground attention guidance module, to alleviate the shifts. Concretely, FVG-PT introduces a learnable Foreground Reliability Gate to automatically enhance the foreground view quality, applies a Foreground Distillation Compensation module to guide visual attention toward the foreground, and further introduces a Prior Calibration module to mitigate generalization degradation caused by excessive focus on the foreground. Experiments on multiple backbone models and datasets show the effectiveness and compatibility of FVG-PT. Codes are available at: https://github.com/JREion/FVG-PT

### 🤖 AI 总结

**一句话总结**：FVG-PT通过自适应前景注意力引导与校准，减少CLIP类提示微调中的前景注意力漂移，从而提升下游任务性能与泛化。

**研究动机**：现有prompt tuning多关注文本提示设计/优化，较少分析调优过程中VLM内部注意力表征的变化；作者观察到预测失败常源于视觉编码器前景注意力发生漂移。

**核心方法**：提出可插拔的FVG-PT模块：用Foreground Reliability Gate自适应增强前景视图质量；用Foreground Distillation Compensation蒸馏式补偿来引导注意力聚焦前景；再用Prior Calibration抑制过度前景聚焦带来的泛化退化。

**主要结论**：在多种骨干与数据集上，FVG-PT能稳定缓解前景注意力漂移并带来更好精度/泛化，且与现有CLIP类prompt tuning方案兼容、易于集成。

**关键词**：视觉-语言模型, 提示调优, 参数高效微调, 视觉注意力漂移, 前景注意力引导, 前景可靠性门控, 蒸馏补偿, 先验校准, 跨数据集泛化

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08708v1) | [下载PDF](https://arxiv.org/pdf/2603.08708v1.pdf)

---

## [8. HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising](https://arxiv.org/abs/2603.08703v1)

**作者**：Kai Zou, Dian Zheng, Hongbo Liu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-09

### 📄 论文摘要

Autoregressive (AR) diffusion offers a promising framework for generating videos of theoretically infinite length. However, a major challenge is maintaining temporal continuity while preventing the progressive quality degradation caused by error accumulation. To ensure continuity, existing methods typically condition on highly denoised contexts; yet, this practice propagates prediction errors with high certainty, thereby exacerbating degradation. In this paper, we argue that a highly clean context is unnecessary. Drawing inspiration from bidirectional diffusion models, which denoise frames at a shared noise level while maintaining coherence, we propose that conditioning on context at the same noise level as the current block provides sufficient signal for temporal consistency while effectively mitigating error propagation. Building on this insight, we propose HiAR, a hierarchical denoising framework that reverses the conventional generation order: instead of completing each block sequentially, it performs causal generation across all blocks at every denoising step, so that each block is always conditioned on context at the same noise level. This hierarchy naturally admits pipelined parallel inference, yielding a 1.8 wall-clock speedup in our 4-step setting. We further observe that self-rollout distillation under this paradigm amplifies a low-motion shortcut inherent to the mode-seeking reverse-KL objective. To counteract this, we introduce a forward-KL regulariser in bidirectional-attention mode, which preserves motion diversity for causal inference without interfering with the distillation loss. On VBench (20s generation), HiAR achieves the best overall score and the lowest temporal drift among all compared methods.

### 🤖 AI 总结

**一句话总结**：HiAR通过“同噪声级条件”的层级去噪式自回归扩散，在生成超长视频时显著降低误差累积导致的画质与时序漂移，并支持流水线并行加速。

**研究动机**：现有AR扩散为保证连续性常依赖高度去噪的历史上下文，但这会以高置信度传播预测误差，导致随时间推移质量持续退化；作者认为并不需要“很干净”的上下文也能保持一致性。

**核心方法**：提出HiAR：在每个去噪步上对所有块进行因果生成（反转“逐块完成”的顺序），使每个块始终条件于与其相同噪声级的上下文，从而兼顾连续性与抑制误差传播，并天然支持流水线并行推理（4步设置下约1.8×提速）。此外针对自回滚蒸馏放大“低运动捷径”的问题，引入双向注意力模式下的forward-KL正则以保持运动多样性且不干扰蒸馏损失。

**主要结论**：在VBench的20秒视频生成上，HiAR取得最佳总体分数并实现最低时间漂移，验证了同噪声级上下文条件与层级去噪生成顺序能有效提升长视频稳定性与效率。

**关键词**：长视频生成, 自回归扩散, 层级去噪, 同噪声级条件, 时序一致性, 误差累积, 因果生成, 自滚动蒸馏, 反向KL, 前向KL正则

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08703v1) | [下载PDF](https://arxiv.org/pdf/2603.08703v1.pdf)

---

## [9. ER-Pose: Rethinking Keypoint-Driven Representation Learning for Real-Time Human Pose Estimation](https://arxiv.org/abs/2603.08681v1)

**作者**：Nanjun Li, Pinqi Cheng, Zean Liu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-09

### 📄 论文摘要

Single-stage multi-person pose estimation aims to jointly perform human localization and keypoint prediction within a unified framework, offering advantages in inference efficiency and architectural simplicity. Consequently, multi-scale real-time detection architectures, such as YOLO-like models, are widely adopted for real-time pose estimation. However, these approaches typically inherit a box-driven modeling paradigm from object detection, in which pose estimation is implicitly constrained by bounding-box supervision during training. This formulation introduces biases in sample assignment and feature representation, resulting in task misalignment and ultimately limiting pose estimation accuracy. In this work, we revisit box-driven single-stage pose estimation from a keypoint-driven perspective and identify semantic conflicts among parallel objectives as a key source of performance degradation. To address this issue, we propose a keypoint-driven learning paradigm that elevates pose estimation to a primary prediction objective. Specifically, we remove bounding-box prediction and redesign the prediction head to better accommodate the high-dimensional structured representations for pose estimation. We further introduce a keypoint-driven dynamic sample assignment strategy to align training objectives with pose evaluation metrics, enabling dense supervision during training and efficient NMS-free inference. In addition, we propose a smooth OKS-based loss function to stabilize optimization in regression-based pose estimation. Based on these designs, we develop a single-stage multi-person pose estimation framework, termed ER-Pose. On MS COCO and CrowdPose, ER-Pose-n achieves AP improvements of 3.2/6.7 without pre-training and 7.4/4.9 with pre-training respectively compared with the baseline YOLO-Pose. These improvements are achieved with fewer parameters and higher inference efficiency.

### 🤖 AI 总结

**一句话总结**：ER-Pose从“关键点优先”重构单阶段实时多人姿态估计，去除框预测并改进样本分配与损失设计，在更高效率/更少参数下显著提升COCO与CrowdPose精度。

**研究动机**：现有YOLO式实时姿态方法沿用检测的“框驱动”范式，训练时受框监督约束导致样本分配与特征表征偏置、目标间语义冲突，从而造成任务不对齐并限制姿态精度。

**核心方法**：提出关键点驱动学习：移除bbox预测并重设计预测头以适配高维结构化关键点表示；采用关键点驱动的动态样本分配以对齐OKS等评测并实现密集监督与免NMS推理；引入平滑的OKS-based损失稳定回归优化。

**主要结论**：在MS COCO与CrowdPose上，ER-Pose相较YOLO-Pose在无预训练/有预训练条件下分别获得3.2/6.7与7.4/4.9的AP提升，同时参数更少、推理更高效，验证关键点驱动范式能有效缓解任务冲突并提升实时姿态性能。

**关键词**：单阶段多人人体姿态估计, 实时姿态估计, 关键点驱动学习, 去边界框预测, 动态样本分配, 关键点回归, 检测-姿态任务对齐, 密集监督

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08681v1) | [下载PDF](https://arxiv.org/pdf/2603.08681v1.pdf)

---

## [10. Talking Together: Synthesizing Co-Located 3D Conversations from Audio](https://arxiv.org/abs/2603.08674v1)

**作者**：Mengyi Shan, Shouchieh Chang, Ziqian Bai 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-09

### 📄 论文摘要

We tackle the challenging task of generating complete 3D facial animations for two interacting, co-located participants from a mixed audio stream. While existing methods often produce disembodied "talking heads" akin to a video conference call, our work is the first to explicitly model the dynamic 3D spatial relationship -- including relative position, orientation, and mutual gaze -- that is crucial for realistic in-person dialogues. Our system synthesizes the full performance of both individuals, including precise lip-sync, and uniquely allows their relative head poses to be controlled via textual descriptions. To achieve this, we propose a dual-stream architecture where each stream is responsible for one participant's output. We employ speaker's role embeddings and inter-speaker cross-attention mechanisms designed to disentangle the mixed audio and model the interaction. Furthermore, we introduce a novel eye gaze loss to promote natural, mutual eye contact. To power our data-hungry approach, we introduce a novel pipeline to curate a large-scale conversational dataset consisting of over 2 million dyadic pairs from in-the-wild videos. Our method generates fluid, controllable, and spatially aware dyadic animations suitable for immersive applications in VR and telepresence, significantly outperforming existing baselines in perceived realism and interaction coherence.

### 🤖 AI 总结

**一句话总结**：提出从混合对话音频直接合成两位同地交互者的完整3D面部与头部表演，并显式建模相对位置/朝向与互相注视以生成更真实的面对面对话动画。

**研究动机**：现有“talking head”方法多忽略线下对话关键的空间关系与互动线索（相对姿态、互视），且在混合音频下难以为两人分别生成一致、自然的同步表演。

**核心方法**：采用双流架构分别生成两位参与者的3D动画，通过角色嵌入与跨说话人交叉注意力从混合音频中解耦并建模互动；引入眼神（互视）损失提升自然目光交流，并支持用文本描述控制两人相对头部姿态；同时构建从野外视频自动整理的超大规模数据集（200万+双人对话对）支撑训练。

**主要结论**：方法可生成流畅、可控且具空间感的双人3D对话表演（含精确唇形同步与更自然的互视/互动一致性），在主观真实感与交互连贯性上显著优于现有基线，适用于VR与远程临场等沉浸应用。

**关键词**：音频驱动3D人脸动画, 双人对话动画合成, 混合语音解耦, 双流架构, 跨说话人交叉注意力, 说话人角色嵌入, 3D空间关系建模, 互视凝视建模, 凝视损失函数, 文本控制头部姿态, 大规模对话数据集, VR远程临场

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08674v1) | [下载PDF](https://arxiv.org/pdf/2603.08674v1.pdf)

---

## [11. ImprovedGS+: A High-Performance C++/CUDA Re-Implementation Strategy for 3D Gaussian Splatting](https://arxiv.org/abs/2603.08661v1)

**作者**：Jordi Muñoz Vicente  
**分类**：cs.CV  
**发布时间**：2026-03-09

### 📄 论文摘要

Recent advancements in 3D Gaussian Splatting (3DGS) have shifted the focus toward balancing reconstruction fidelity with computational efficiency. In this work, we propose ImprovedGS+, a high-performance, low-level reinvention of the ImprovedGS strategy, implemented natively within the LichtFeld-Studio framework. By transitioning from high-level Python logic to hardware-optimized C++/CUDA kernels, we achieve a significant reduction in host-device synchronization and training latency. Our implementation introduces a Long-Axis-Split (LAS) CUDA kernel, custom Laplacian-based importance kernels with Non-Maximum Suppression (NMS) for edge scores, and an adaptive Exponential Scale Scheduler. Experimental results on the Mip-NeRF360 dataset demonstrate that ImprovedGS+ establishes a new Pareto-optimal front for scene reconstruction. Our 1M-budget variant outperforms the state-of-the-art MCMC baseline by achieving a 26.8% reduction in training time (saving 17 minutes per session) and utilizing 13.3% fewer Gaussians while maintaining superior visual quality. Furthermore, our full variant demonstrates a 1.28 dB PSNR increase over the ADC baseline with a 38.4% reduction in parametric complexity. These results validate ImprovedGS+ as a scalable, high-speed solution that upholds the core pillars of Speed, Quality, and Usability within the LichtFeld-Studio ecosystem.

### 🤖 AI 总结

**一句话总结**：ImprovedGS+ 通过将 ImprovedGS 从 Python 迁移到 C++/CUDA 并加入新核函数与调度策略，在 Mip-NeRF360 上实现更快训练、更少高斯数量且保持/提升重建质量。

**研究动机**：现有 3D Gaussian Splatting 方法在追求高保真重建时常伴随训练开销与同步瓶颈，难以同时兼顾速度与可用性。作者希望用底层高性能实现降低 host-device 同步与延迟，在固定预算下取得更优的质量-效率折中。

**核心方法**：在 LichtFeld-Studio 框架内进行原生 C++/CUDA 重实现，替换高层 Python 逻辑以减少同步与开销；提出 Long-Axis-Split (LAS) CUDA kernel、自定义基于拉普拉斯的重要性评估核并对边缘分数做 NMS，以及自适应指数尺度调度器（Exponential Scale Scheduler）。

**主要结论**：在 Mip-NeRF360 上，1M 预算版本较 SOTA MCMC 基线训练时间减少 26.8% 且高斯数减少 13.3% 并保持更佳观感；完整版本较 ADC 基线 PSNR 提升 1.28 dB 且参数复杂度降低 38.4%，表明其在速度、质量与可用性上达到新的 Pareto 最优。

**关键词**：3D 场景重建, C++/CUDA 实现, 训练加速, 主机-设备同步优化, 长轴分裂（LAS）, 非极大值抑制（NMS）, 指数尺度调度, ImprovedGS+

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08661v1) | [下载PDF](https://arxiv.org/pdf/2603.08661v1.pdf)

---

## [12. CAST: Modeling Visual State Transitions for Consistent Video Retrieval](https://arxiv.org/abs/2603.08648v1)

**作者**：Yanqing Liu, Yingcheng Liu, Fanghong Dong 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-09

### 📄 论文摘要

As video content creation shifts toward long-form narratives, composing short clips into coherent storylines becomes increasingly important. However, prevailing retrieval formulations remain context-agnostic at inference time, prioritizing local semantic alignment while neglecting state and identity consistency. To address this structural limitation, we formalize the task of Consistent Video Retrieval (CVR) and introduce a diagnostic benchmark spanning YouCook2, COIN, and CrossTask. We propose CAST (Context-Aware State Transition), a lightweight, plug-and-play adapter compatible with diverse frozen vision-language embedding spaces. By predicting a state-conditioned residual update ($Δ$) from visual history, CAST introduces an explicit inductive bias for latent state evolution. Extensive experiments show that CAST improves performance on YouCook2 and CrossTask, remains competitive on COIN, and consistently outperforms zero-shot baselines across diverse foundation backbones. Furthermore, CAST provides a useful reranking signal for black-box video generation candidates (e.g., from Veo), promoting more temporally coherent continuations.

### 🤖 AI 总结

**一句话总结**：CAST通过建模视觉状态随时间的转移，在视频检索中显式强化身份与状态一致性，从而提升长叙事/多步骤视频的检索连贯性。

**研究动机**：现有视频检索多在推理时忽略上下文，只做局部语义对齐，导致跨片段的状态变化与角色/物体身份不一致。为此作者提出“Consistent Video Retrieval”任务与基准，用于诊断并推动检索结果的时序一致性。

**核心方法**：提出轻量可插拔的CAST适配器，可接在冻结的视觉-语言嵌入空间上；它利用视觉历史预测“状态条件化”的残差更新Δ，为隐式表征注入状态演化的归纳偏置，从而在检索/重排序时偏好时序连贯的候选。

**主要结论**：在YouCook2与CrossTask上CAST带来显著提升、在COIN上保持竞争力，并在多种基础模型骨干下稳定优于零样本基线；此外它还能作为黑盒视频生成候选（如Veo）的重排序信号，促进更一致的时间延续。

**关键词**：一致性视频检索, 上下文感知检索, 视觉状态转移建模, 状态条件残差更新, 时序一致性, 身份一致性, 视频-语言嵌入空间, 轻量级适配器, 冻结视觉-语言骨干, 诊断评测基准, 视频生成候选重排序

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08648v1) | [下载PDF](https://arxiv.org/pdf/2603.08648v1.pdf)

---

## [13. Retrieval-Augmented Gaussian Avatars: Improving Expression Generalization](https://arxiv.org/abs/2603.08645v1)

**作者**：Matan Levy, Gavriel Habib, Issar Tzachor 等 8 位作者  
**分类**：cs.CV, cs.GR, cs.LG  
**发布时间**：2026-03-09

### 📄 论文摘要

Template-free animatable head avatars can achieve high visual fidelity by learning expression-dependent facial deformation directly from a subject's capture, avoiding parametric face templates and hand-designed blendshape spaces. However, since learned deformation is supervised only by the expressions observed for a single identity, these models suffer from limited expression coverage and often struggle when driven by motions that deviate from the training distribution. We introduce RAF (Retrieval-Augmented Faces), a simple training-time augmentation designed for template-free head avatars that learn deformation from data. RAF constructs a large unlabeled expression bank and, during training, replaces a subset of the subject's expression features with nearest-neighbor expressions retrieved from this bank while still reconstructing the subject's original frames. This exposes the deformation field to a broader range of expression conditions, encouraging stronger identity-expression decoupling and improving robustness to expression distribution shift without requiring paired cross-identity data, additional annotations, or architectural changes. We further analyze how retrieval augmentation increases expression diversity and validate retrieval quality with a user study showing that retrieved neighbors are perceptually closer in expression and pose. Experiments on the NeRSemble benchmark demonstrate that RAF consistently improves expression fidelity over the baseline, in both self-driving and cross-driving scenarios.

### 🤖 AI 总结

**一句话总结**：提出RAF检索增强训练：用无标注表情库的近邻表情替换部分训练特征，从而让模板无关的高斯头部头像在分布外表情驱动下更稳、更逼真。

**研究动机**：模板无关头像仅由单个身份的有限表情监督学习形变，导致表情覆盖不足、身份与表情耦合强，遇到训练分布外驱动（尤其跨人驱动）时容易失真。

**核心方法**：构建大规模无标注“表情银行”，训练时对部分帧将该主体的表情特征替换为从表情银行检索到的最近邻表情特征，但仍以主体原始帧为重建目标，以此扩大形变场见到的表情条件而无需配对跨身份数据、额外标注或改网络结构。

**主要结论**：检索增强显著提升训练中的表情多样性并促进身份-表情解耦；在NeRSemble上自驱与跨驱均稳定提升表情保真度，且用户研究表明检索到的邻居在感知表情/姿态上更接近。

**关键词**：可动画头部虚拟人, 模板自由人脸建模, 高斯虚拟人, 表情泛化, 检索增强训练, 最近邻检索, 无标注表情库, 身份-表情解耦, 表情分布偏移鲁棒性, 人脸形变场学习, 跨身份驱动

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08645v1) | [下载PDF](https://arxiv.org/pdf/2603.08645v1.pdf)

---

## [14. UNBOX: Unveiling Black-box visual models with Natural-language](https://arxiv.org/abs/2603.08639v1)

**作者**：Simone Carnemolla, Chiara Russo, Simone Palazzo 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-09

### 📄 论文摘要

Ensuring trustworthiness in open-world visual recognition requires models that are interpretable, fair, and robust to distribution shifts. Yet modern vision systems are increasingly deployed as proprietary black-box APIs, exposing only output probabilities and hiding architecture, parameters, gradients, and training data. This opacity prevents meaningful auditing, bias detection, and failure analysis. Existing explanation methods assume white- or gray-box access or knowledge of the training distribution, making them unusable in these real-world settings. We introduce UNBOX, a framework for class-wise model dissection under fully data-free, gradient-free, and backpropagation-free constraints. UNBOX leverages Large Language Models and text-to-image diffusion models to recast activation maximization as a purely semantic search driven by output probabilities. The method produces human-interpretable text descriptors that maximally activate each class, revealing the concepts a model has implicitly learned, the training distribution it reflects, and potential sources of bias. We evaluate UNBOX on ImageNet-1K, Waterbirds, and CelebA through semantic fidelity tests, visual-feature correlation analyses and slice-discovery auditing. Despite operating under the strictest black-box constraints, UNBOX performs competitively with state-of-the-art white-box interpretability methods. This demonstrates that meaningful insight into a model's internal reasoning can be recovered without any internal access, enabling more trustworthy and accountable visual recognition systems.

### 🤖 AI 总结

**一句话总结**：UNBOX在完全黑盒、无数据无梯度条件下，用自然语言与扩散生成把“激活最大化”转为语义搜索，从而为每个类别生成可解释的概念描述以审计视觉模型。

**研究动机**：现实中大量视觉模型以封闭API形式部署，外界只能拿到输出概率，导致难以做可解释性分析、偏差检测与失效归因。现有解释方法多依赖白盒/灰盒访问或已知训练分布，在真实黑盒场景不可用。

**核心方法**：UNBOX结合大语言模型与文生图扩散模型：LLM提出/迭代文本描述，扩散模型把描述生成图像，通过黑盒API返回的类别概率作为唯一反馈信号进行语义层面的搜索与优化。最终为每个类别产出“最能激活该类”的人类可读文本概念，并用语义保真度、视觉特征相关与切片发现审计等指标评估。

**主要结论**：在ImageNet-1K、Waterbirds与CelebA上，即使在最严格黑盒约束下，UNBOX仍能生成与类别相关且可用于发现训练分布痕迹与潜在偏差的概念描述，表现与部分白盒可解释方法具有竞争力。结果表明无需内部访问也能恢复对模型表征与决策偏好的有意义洞察，从而支持更可信的模型审计。

**关键词**：黑盒视觉模型解释, 仅概率查询, 数据无关解释, 无梯度分析, 类别级模型剖析, 激活最大化, 语义搜索, LLM, 文生图扩散模型, 偏见审计, 分布偏移鲁棒性

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08639v1) | [下载PDF](https://arxiv.org/pdf/2603.08639v1.pdf)

---

## [15. StreamReady: Learning What to Answer and When in Long Streaming Videos](https://arxiv.org/abs/2603.08620v1)

**作者**：Shehreen Azad, Vibhav Vineet, Yogesh Singh Rawat  
**分类**：cs.CV  
**发布时间**：2026-03-09

### 📄 论文摘要

Streaming video understanding often involves time-sensitive scenarios where models need to answer exactly when the supporting visual evidence appears: answering before the evidence reflects speculation, answering after it has passed reduces real-time utility. To capture this behavior, we introduce a readiness-aware formulation of streaming video understanding with the Answer Readiness Score (ARS), a timing-aware objective with asymmetric early and late penalties. When combined with correctness, ARS defines an effective accuracy that measures not just whether a model is right, but whether it answers at the appropriate moment. Building on this formulation, we introduce StreamReady, a framework to unify temporal reasoning with on-time answering through a lightweight readiness mechanism that decides if sufficient evidence has been observed before responding. To evaluate this capability, we further introduce ProReady-QA, a benchmark with annotated answer evidence windows and proactive multi-turn questions across local and global contexts. StreamReady achieves superior performance on ProReady-QA, and consistently outperforms prior methods across eight additional streaming and offline long-video benchmarks, demonstrating robust and broadly generalizable video understanding capability.

### 🤖 AI 总结

**一句话总结**：Streaming video understanding often involves time-sensitive scenarios where models need to answer exactly when the supporting visual evidence appears: answering before the evidence reflects speculatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：长视频问答, 及时作答, 时间敏感推理, 证据窗口标注, 答案就绪度评分（ARS）, 非对称时序惩罚, 有效准确率, 就绪机制, 主动多轮问答

**评分**：41

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08620v1) | [下载PDF](https://arxiv.org/pdf/2603.08620v1.pdf)

---

## [16. FOMO-3D: Using Vision Foundation Models for Long-Tailed 3D Object Detection](https://arxiv.org/abs/2603.08611v1)

**作者**：Anqi Joyce Yang, James Tu, Nikita Dvornik 等 5 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-03-09

### 📄 论文摘要

In order to navigate complex traffic environments, self-driving vehicles must recognize many semantic classes pertaining to vulnerable road users or traffic control devices. However, many safety-critical objects (e.g., construction worker) appear infrequently in nominal traffic conditions, leading to a severe shortage of training examples from driving data alone. Recent vision foundation models, which are trained on a large corpus of data, can serve as a good source of external prior knowledge to improve generalization. We propose FOMO-3D, the first multi-modal 3D detector to leverage vision foundation models for long-tailed 3D detection. Specifically, FOMO-3D exploits rich semantic and depth priors from OWLv2 and Metric3Dv2 within a two-stage detection paradigm that first generates proposals with a LiDAR-based branch and a novel camera-based branch, and refines them with attention especially to image features from OWL. Evaluations on real-world driving data show that using rich priors from vision foundation models with careful multi-modal fusion designs leads to large gains for long-tailed 3D detection. Project website is at https://waabi.ai/fomo3d/.

### 🤖 AI 总结

**一句话总结**：FOMO-3D通过引入视觉基础模型的语义与深度先验，在多模态两阶段框架中显著提升自动驾驶场景的长尾3D目标检测能力。

**研究动机**：自动驾驶中许多安全关键类别（如施工人员、交通设施）在真实数据里极少出现，导致训练样本不足、模型泛化差。视觉基础模型具备大规模预训练带来的通用知识，可作为外部先验缓解长尾问题。

**核心方法**：提出首个利用视觉基础模型的多模态3D检测器：在两阶段检测中，第一阶段用LiDAR分支+新相机分支生成候选框，并引入OWLv2的丰富语义特征与Metric3Dv2的深度/尺度先验。第二阶段通过注意力等融合机制重点利用来自OWL的图像特征对候选框进行精炼，实现更强的跨模态对齐与长尾识别。

**主要结论**：在真实驾驶数据评测中，结合视觉基础模型先验并进行精心的多模态融合设计，可为长尾3D检测带来显著性能提升，尤其改善稀有类别的检测效果。

**关键词**：长尾3D目标检测, 多模态3D检测, 自动驾驶感知, LiDAR-相机融合, 两阶段目标检测, 视觉基础模型, 开放词汇目标检测, 单目深度估计, 语义先验, 深度先验, 注意力特征融合

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08611v1) | [下载PDF](https://arxiv.org/pdf/2603.08611v1.pdf)

---

## [17. Weakly Supervised Teacher-Student Framework with Progressive Pseudo-mask Refinement for Gland Segmentation](https://arxiv.org/abs/2603.08605v1)

**作者**：Hikmat Khan, Wei Chen, Muhammad Khalid Khan Niazi  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-09

### 📄 论文摘要

Background and objectives: Colorectal cancer histopathological grading depends on accurate segmentation of glandular structures. Current deep learning approaches rely on large scale pixel level annotations that are labor intensive and difficult to obtain in routine clinical practice. Weakly supervised semantic segmentation offers a promising alternative. However, class activation map based methods often produce incomplete pseudo masks that emphasize highly discriminative regions and fail to supervise unannotated glandular structures. We propose a weakly supervised teacher student framework that leverages sparse pathologist annotations and an Exponential Moving Average stabilized teacher network to generate refined pseudo masks.   Methods: The framework integrates confidence based filtering, adaptive fusion of teacher predictions with limited ground truth, and curriculum guided refinement to progressively segment unannotated glandular regions. The method was evaluated on an institutional colorectal cancer cohort from The Ohio State University Wexner Medical Center consisting of 60 hematoxylin and eosin stained whole slide images and on public datasets including the Gland Segmentation dataset, TCGA COAD, TCGA READ, and SPIDER.   Results: On the Gland Segmentation dataset the framework achieved a mean Intersection over Union of 80.10 and a mean Dice coefficient of 89.10. Cross cohort evaluation demonstrated robust generalization on TCGA COAD and TCGA READ without additional annotations, while reduced performance on SPIDER reflected domain shift.   Conclusions: The proposed framework provides an annotation efficient and generalizable approach for gland segmentation in colorectal histopathology.

### 🤖 AI 总结

**一句话总结**：提出一种基于EMA教师-学生的弱监督框架，通过逐步精炼伪掩码，在仅有稀疏病理标注的情况下实现高质量结肠腺体分割并具备较好跨队列泛化。

**研究动机**：腺体分割对结直肠癌病理分级关键，但像素级全标注成本高且临床难以规模化获取；现有CAM类弱监督方法伪掩码往往不完整，难以覆盖未标注的腺体区域。

**核心方法**：采用EMA稳定的教师网络生成预测，并通过置信度过滤与“教师预测+少量真值”的自适应融合来构造更可靠的伪掩码；再用课程式（由易到难）策略进行渐进式伪掩码精炼，逐步扩展到未标注腺体区域以监督学生网络训练。

**主要结论**：在Gland Segmentation数据集上达到mIoU 80.10、mDice 89.10，并在TCGA COAD/READ上无需额外标注仍表现稳健；在SPIDER上性能下降主要反映域偏移影响，整体证明该方法具备标注高效性与较强泛化能力。

**关键词**：弱监督语义分割, 腺体分割, 结直肠癌病理, 全视野切片, 教师-学生框架, EMA教师网络, 伪掩膜细化, 稀疏病理标注, 置信度过滤, 课程学习, 跨队列泛化, 领域偏移

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08605v1) | [下载PDF](https://arxiv.org/pdf/2603.08605v1.pdf)

---

## [18. Boosting MLLM Spatial Reasoning with Geometrically Referenced 3D Scene Representations](https://arxiv.org/abs/2603.08592v1)

**作者**：Jiangye Yuan, Gowri Kumar, Baoyuan Wang  
**分类**：cs.CV  
**发布时间**：2026-03-09

### 📄 论文摘要

While Multimodal Large Language Models (MLLMs) have achieved remarkable success in 2D visual understanding, their ability to reason about 3D space remains limited. To address this gap, we introduce geometrically referenced 3D scene representations (GR3D). Given a set of input images, GR3D annotates objects in the images with unique IDs and encodes their 3D geometric attributes as textual references indexed by these IDs. This representation enables MLLMs to interpret 3D cues using their advanced language-based skills in mathematical reasoning, while concurrently analyzing 2D visual features in a tightly coupled way. We present a simple yet effective approach based on GR3D, which requires no additional training and is readily applicable to different MLLMs. Implemented in a zero-shot setting, our approach boosts GPT-5's performance on VSI-Bench by 8% overall and more than 11% on tasks that rely heavily on spatial layout understanding. Qualitative studies further demonstrate that GR3D empowers MLLMs to perform complex spatial reasoning with highly sparse input views.

### 🤖 AI 总结

**一句话总结**：提出GR3D：将多视图图像中的对象用ID索引并把其3D几何属性转成文本引用，从而在零训练条件下显著提升MLLM的3D空间推理能力。

**研究动机**：现有MLLM在2D理解上表现强，但缺乏对3D空间关系/布局的可靠推理能力，尤其在视角稀疏或需要精确几何约束的任务中表现受限。

**核心方法**：从输入图像中为物体分配唯一ID，并将其3D几何属性（如位置、尺度、相对关系等）编码为与ID绑定的文本化几何引用，让MLLM同时利用语言端的数学推理与视觉端的2D特征进行耦合推理；方法无需额外训练、可直接用于不同MLLM。

**主要结论**：在零样本设置下，该方案使GPT-5在VSI-Bench总体提升约8%，在强依赖空间布局理解的任务上提升超过11%；定性结果显示即使输入视角很稀疏也能完成更复杂的空间推理。

**关键词**：3D, Boosting, MLLM, Spatial, Reasoning, Geometrically, Referenced, Scene

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08592v1) | [下载PDF](https://arxiv.org/pdf/2603.08592v1.pdf)

---

## cs.LG

## [19. Impermanent: A Live Benchmark for Temporal Generalization in Time Series Forecasting](https://arxiv.org/abs/2603.08707v1)

**作者**：Azul Garza, Renée Rosillo, Rodrigo Mendoza-Smith 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-09

### 📄 论文摘要

Recent advances in time-series forecasting increasingly rely on pre-trained foundation-style models. While these models often claim broad generalization, existing evaluation protocols provide limited evidence. Indeed, most current benchmarks use static train-test splits that can easily lead to contamination as foundation models can inadvertently train on test data or perform model selection using test scores, which can inflate performance. We introduce Impermanent, a live benchmark that evaluates forecasting models under open-world temporal change by scoring forecasts sequentially over time on continuously updated data streams, enabling the study of temporal robustness, distributional shift, and performance stability rather than one-off accuracy on a frozen test set. Impermanent is instantiated on GitHub open-source activity, providing a naturally live and highly non-stationary dataset shaped by releases, shifting contributor behavior, platform/tooling changes, and external events. We focus on the top 400 repositories by star count and construct time series from issues opened, pull requests opened, push events, and new stargazers, evaluated over a rolling window with daily updates, alongside standardized protocols and leaderboards for reproducible, ongoing comparison. By shifting evaluation from static accuracy to sustained performance, Impermanent takes a concrete step toward assessing when and whether foundation-level generalization in time-series forecasting can be meaningfully claimed. Code and a live dashboard are available at https://github.com/TimeCopilot/impermanent and https://impermanent.timecopilot.dev.

### 🤖 AI 总结

**一句话总结**：Impermanent 提出一个“在线/持续更新”的时间序列预测基准，用逐日滚动评分来检验模型在真实时间变化与分布漂移下的长期泛化与稳定性。

**研究动机**：现有时间序列基准多采用静态划分，基础模型可能因数据泄漏或用测试集做模型选择而导致成绩被高估，难以证明真正的广泛泛化。需要一种能反映开放世界时间演化、分布变化与性能稳定性的评测方式。

**核心方法**：构建 Impermanent 在线基准：在持续更新的数据流上按时间顺序滚动评测与记分，而非一次性冻结测试集。其实现基于 GitHub 前400高星仓库的多变量事件序列（issues/PR/push/star），采用每日更新与滚动窗口评估，并提供标准化协议与排行榜/仪表盘以支持可复现的持续对比。

**主要结论**：将评估从“静态一次性准确率”转为“持续表现”，能更可靠地衡量时间序列模型对时间变化与分布漂移的鲁棒性，并使“基础模型级泛化”的主张更可检验。Impermanent 作为开放的实时基准为长期、可追踪的模型比较提供了基础设施。

**关键词**：时间序列预测, 时间泛化, 实时基准测试, 开放世界评测, 时间分布漂移, 非平稳时间序列, 滚动窗口评估, 持续性能评估, 数据泄漏检测, 预训练基础模型

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08707v1) | [下载PDF](https://arxiv.org/pdf/2603.08707v1.pdf)

---

## [20. Split Federated Learning Architectures for High-Accuracy and Low-Delay Model Training](https://arxiv.org/abs/2603.08687v1)

**作者**：Yiannis Papageorgiou, Yannis Thomas, Ramin Khalili 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-09

### 📄 论文摘要

Can we find a network architecture for ML model training so as to optimize training loss (and thus, accuracy) in Split Federated Learning (SFL)? And can this architecture also reduce training delay and communication overhead? While accuracy is not influenced by how we split the model in ordinary, state-of-the-art SFL, in this work we answer the questions above in the affirmative. Recent Hierarchical SFL (HSFL) architectures adopt a three-tier training structure consisting of clients, (local) aggregators, and a central server. In this architecture, the model is partitioned at two partitioning layers into three sub-models, which are executed across the three tiers. Despite their merits, HSFL architectures overlook the impact of the partitioning layers and client-to-aggregator assignments on accuracy, delay, and overhead. This work explicitly captures the impact of the partitioning layers and client-to-aggregator assignments on accuracy, delay and overhead by formulating a joint optimization problem. We prove that the problem is NP-hard and propose the first accuracy-aware heuristic algorithm that explicitly accounts for model accuracy, while remaining delay-efficient. Simulation results on public datasets show that our approach can improve accuracy by 3%, while reducing delay by 20% and overhead by 50%, compared to state-of-the-art SFL and HSFL schemes.

### 🤖 AI 总结

**一句话总结**：论文提出一种面向准确率的分层Split Federated Learning（HSFL）架构联合优化方法，通过优化切分层与客户端-聚合器分配，在提升精度的同时降低训练时延与通信开销。

**研究动机**：现有SFL/HSFL通常认为模型切分位置不影响精度，因而忽略切分层选择与客户端到聚合器分配对准确率、时延和开销的耦合影响，导致整体性能未被充分优化。

**核心方法**：将“两处模型切分层选择 + 客户端-聚合器指派”建模为联合优化问题，显式刻画其对准确率、时延与通信开销的影响；证明该问题NP-hard，并提出首个准确率感知的启发式算法，在兼顾低时延的同时优化精度。

**主要结论**：在公开数据集仿真中，相比现有SFL与HSFL方案，该方法将准确率提升约3%，训练时延降低约20%，通信开销降低约50%，实现了精度与效率的同步改进。

**关键词**：分割联邦学习（SFL）, 分层分割联邦学习（HSFL）, 三层训练架构, 模型分区层选择, 客户端-聚合器分配, 准确率-时延-开销联合优化, 准确率感知启发式算法, 训练时延优化, 通信开销优化, 训练损失最小化

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08687v1) | [下载PDF](https://arxiv.org/pdf/2603.08687v1.pdf)

---

## [21. A New Lower Bound for the Random Offerer Mechanism in Bilateral Trade using AI-Guided Evolutionary Search](https://arxiv.org/abs/2603.08679v1)

**作者**：Yang Cai, Vineet Gupta, Zun Li 等 4 位作者  
**分类**：cs.LG, cs.AI, cs.GT, econ.TH  
**发布时间**：2026-03-09

### 📄 论文摘要

The celebrated Myerson--Satterthwaite theorem shows that in bilateral trade, no mechanism can be simultaneously fully efficient, Bayesian incentive compatible (BIC), and budget balanced (BB). This naturally raises the question of how closely the gains from trade (GFT) achievable by a BIC and BB mechanism can approximate the first-best (fully efficient) benchmark. The optimal BIC and BB mechanism is typically complex and highly distribution-dependent, making it difficult to characterize directly. Consequently, much of the literature analyzes simpler mechanisms such as the Random-Offerer (RO) mechanism and establishes constant-factor guarantees relative to the first-best GFT. An important open question concerns the worst-case performance of the RO mechanism relative to first-best (FB) efficiency. While it was originally hypothesized that the approximation ratio $\frac{\text{GFT}_{\text{FB}}}{\text{GFT}_{\text{RO}}}$ is bounded by $2$, recent work provided counterexamples to this conjecture: Cai et al. proved that the ratio can be strictly larger than $2$, and Babaioff et al. exhibited an explicit example with ratio approximately $2.02$.   In this work, we employ AlphaEvolve, an AI-guided evolutionary search framework, to explore the space of value distributions. We identify a new worst-case instance that yields an improved lower bound of $\frac{\text{GFT}_{\text{FB}}}{\text{GFT}_{\text{RO}}} \ge \textbf{2.0749}$. This establishes a new lower bound on the worst-case performance of the Random-Offerer mechanism, demonstrating a wider efficiency gap than previously known.

### 🤖 AI 总结

**一句话总结**：用AI引导的进化搜索在双边交易问题中找到了Random-Offerer机制更差的分布实例，将其相对一阶最优的最坏情况效率缺口下界提高到2.0749。

**研究动机**：由于Myerson–Satterthwaite定理表明无法同时满足完全效率、BIC与预算平衡，研究者关注简单机制（如RO）能在多大程度上逼近一阶最优GFT；而RO的最坏情况近似比一直是开放问题。近期已知其可超过2，但现有反例仍较弱，因此需要更强的下界与更系统的反例搜索。

**核心方法**：使用AlphaEvolve这一AI引导的进化搜索框架，在价值分布空间中自动探索并优化“使FB/RO比值尽可能大”的实例。通过搜索得到新的分布构造，使RO机制在该实例上的GFT显著低于一阶最优基准。

**主要结论**：作者发现一个新的最坏情况实例，证明FB相对RO的比值下界达到2.0749，刷新了此前约2.02的已知下界。结果表明RO机制的最坏情况效率缺口比先前认识更大，进一步削弱了“比值不超过2”的猜想。

**关键词**：双边交易机制设计, 贝叶斯激励相容（BIC）, 预算平衡（BB）, 交易增益（GFT）, 第一最佳效率（FB）, 随机报价者机制（RO）, 最坏情况近似比, 价值分布构造, 进化搜索（AI引导）, 效率缺口下界

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08679v1) | [下载PDF](https://arxiv.org/pdf/2603.08679v1.pdf)

---

## [22. How Far Can Unsupervised RLVR Scale LLM Training?](https://arxiv.org/abs/2603.08660v1)

**作者**：Bingxiang He, Yuxin Zuo, Zeyuan Liu 等 21 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-03-09

### 📄 论文摘要

Unsupervised reinforcement learning with verifiable rewards (URLVR) offers a pathway to scale LLM training beyond the supervision bottleneck by deriving rewards without ground truth labels. Recent works leverage model intrinsic signals, showing promising early gains, yet their potential and limitations remain unclear. In this work, we revisit URLVR and provide a comprehensive analysis spanning taxonomy, theory and extensive experiments. We first classify URLVR methods into intrinsic versus external based on reward sources, then establish a unified theoretical framework revealing that all intrinsic methods converge toward sharpening the model's initial distribution This sharpening mechanism succeeds when initial confidence aligns with correctness but fails catastrophically when misaligned. Through systematic experiments, we show intrinsic rewards consistently follow a rise-then-fall pattern across methods, with collapse timing determined by model prior rather than engineering choices. Despite these scaling limits, we find intrinsic rewards remain valuable in test-time training on small datasets, and propose Model Collapse Step to measure model prior, serving as a practical indicator for RL trainability. Finally, we explore external reward methods that ground verification in computational asymmetries, showing preliminary evidence they may escape the confidence-correctness ceiling. Our findings chart boundaries for intrinsic URLVR while motivating paths toward scalable alternatives.

### 🤖 AI 总结

**一句话总结**：论文系统分析了无监督“可验证奖励”强化学习（URLVR）的可扩展性，指出内在奖励方法本质上会“锐化”初始分布而存在先升后崩的规模上限，外在奖励可能是更可扩展的出路。

**研究动机**：URLVR希望在缺少人工标注/真值监督时仍能训练并扩展LLM，但现有依赖模型内在信号的做法虽有效却缺乏对其上限、失败模式与可训练性判断的清晰认识。

**核心方法**：作者提出按奖励来源将URLVR划分为“内在(intrinsic)”与“外在(external)”两类，并给出统一理论框架证明内在方法等价于推动模型分布向初始高置信区域“锐化”；随后通过系统实验验证不同内在奖励普遍呈现“提升-坍塌”曲线，并引入Model Collapse Step作为衡量模型先验/可RL训练性的指标，同时探索基于计算不对称性验证的外在奖励路线。

**主要结论**：内在URLVR的成功依赖“初始置信度与正确性对齐”，一旦错配会灾难性崩塌且崩塌时机主要由模型先验决定而非工程细节；尽管不适合无限规模训练，内在奖励在小数据测试时训练仍有价值，而外在可验证奖励初步显示可能突破该置信-正确性天花板。

**关键词**：可验证奖励, LLM训练扩展, 内在奖励, 外部奖励, 分布锐化, 置信度-正确性对齐, 奖励崩塌, 模型先验, 测试时训练, 模型崩塌步（MCS）, 计算不对称验证

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08660v1) | [下载PDF](https://arxiv.org/pdf/2603.08660v1.pdf)

---

## [23. Context-free Self-Conditioned GAN for Trajectory Forecasting](https://arxiv.org/abs/2603.08658v1)

**作者**：Tiago Rodrigues de Almeida, Eduardo Gutierrez Maestro, Oscar Martinez Mozos  
**分类**：cs.LG  
**发布时间**：2026-03-09

### 📄 论文摘要

In this paper, we present a context-free unsupervised approach based on a self-conditioned GAN to learn different modes from 2D trajectories. Our intuition is that each mode indicates a different behavioral moving pattern in the discriminator's feature space. We apply this approach to the problem of trajectory forecasting. We present three different training settings based on self-conditioned GAN, which produce better forecasters. We test our method in two data sets: human motion and road agents. Experimental results show that our approach outperforms previous context-free methods in the least representative supervised labels while performing well in the remaining labels. In addition, our approach outperforms globally in human motion, while performing well in road agents.

### 🤖 AI 总结

**一句话总结**：提出一种无上下文、无监督的自条件GAN，从2D轨迹中学习多模态运动模式以提升轨迹预测表现。

**研究动机**：现有轨迹预测常依赖场景上下文或监督标签，代价高且在标签稀缺/不均衡时效果受限；作者希望在不使用上下文与监督的前提下仍能捕捉多种行为模式。

**核心方法**：构建自条件GAN：将判别器特征空间中的“模式”作为不同运动行为的表征，并通过自条件机制引导生成器学习多模态轨迹；同时设计三种基于自条件GAN的训练设置来训练更好的预测器。

**主要结论**：在人体运动与道路参与者两类数据集上，该方法在最不具代表性的监督标签上优于以往无上下文方法，并在人体运动任务上整体领先；在道路参与者数据上也保持良好表现。

**关键词**：轨迹预测, 生成对抗网络, 无监督学习, 上下文无关建模, 多模态轨迹生成, 2D轨迹建模, 判别器特征空间, 人体运动数据集, 道路交通参与者轨迹

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08658v1) | [下载PDF](https://arxiv.org/pdf/2603.08658v1.pdf)

---

## [24. Group Entropies and Mirror Duality: A Class of Flexible Mirror Descent Updates for Machine Learning](https://arxiv.org/abs/2603.08651v1)

**作者**：Andrzej Cichocki, Piergiulio Tempesta  
**分类**：cs.LG, hep-th, math-ph  
**发布时间**：2026-03-09

### 📄 论文摘要

We introduce a comprehensive theoretical and algorithmic framework that bridges formal group theory and group entropies with modern machine learning, paving the way for an infinite, flexible family of Mirror Descent (MD) optimization algorithms. Our approach exploits the rich structure of group entropies, which are generalized entropic functionals governed by group composition laws, encompassing and significantly extending all trace-form entropies such as the Shannon, Tsallis, and Kaniadakis families. By leveraging group-theoretical mirror maps (or link functions) in MD, expressed via multi-parametric generalized logarithms and their inverses (group exponentials), we achieve highly flexible and adaptable MD updates that can be tailored to diverse data geometries and statistical distributions. To this end, we introduce the notion of \textit{mirror duality}, which allows us to seamlessly switch or interchange group-theoretical link functions with their inverses, subject to specific learning rate constraints. By tuning or learning the hyperparameters of the group logarithms enables us to adapt the model to the statistical properties of the training distribution, while simultaneously ensuring desirable convergence characteristics via fine-tuning. This generality not only provides greater flexibility and improved convergence properties, but also opens new perspectives for applications in machine learning and deep learning by expanding the design of regularizers and natural gradient algorithms. We extensively evaluate the validity, robustness, and performance of the proposed updates on large-scale, simplex-constrained quadratic programming problems.

### 🤖 AI 总结

**一句话总结**：提出将群熵（group entropies）与群论镜像映射引入镜像下降（Mirror Descent），构造一个可通过多参数广义对数/指数灵活定制、并带有“镜像对偶性”切换机制的新型优化更新族。

**研究动机**：传统MD的镜像映射/正则（如Shannon/Tsallis等）选择有限，难以匹配不同数据几何与分布形态，进而影响收敛与鲁棒性。作者希望用更一般的群熵框架统一并扩展这些选择，使优化算法可按任务统计性质自适应调参。

**核心方法**：用由群组合律支配的群熵定义一类群论镜像映射（link function），通过多参数广义对数及其逆（群指数）给出MD更新，并提出“镜像对偶性”在学习率约束下实现link与其逆的互换。通过调优/学习广义对数的超参数以适配训练分布，同时分析并保持良好收敛性质，并在大规模单纯形约束二次规划上进行验证。

**主要结论**：该框架在理论上统一并显著扩展了trace-form熵诱导的MD更新，提供无限且可调的优化算法家族，并能通过对偶切换与超参数调节获得更灵活的几何匹配与潜在更好的收敛/鲁棒性。实验在大规模单纯形约束QP上显示所提更新具有有效性、稳定性与竞争性性能。

**关键词**：镜像下降, 群论优化, 广义对数, 群指数函数, 镜像映射, 镜像对偶, 自适应学习率约束, 收敛性分析, 自然梯度, 正则化设计, 单纯形约束二次规划

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08651v1) | [下载PDF](https://arxiv.org/pdf/2603.08651v1.pdf)

---

## [25. Divide and Predict: An Architecture for Input Space Partitioning and Enhanced Accuracy](https://arxiv.org/abs/2603.08649v1)

**作者**：Fenix W. Huang, Henning S. Mortveit, Christian M. Reidys  
**分类**：cs.LG  
**发布时间**：2026-03-09

### 📄 论文摘要

In this article the authors develop an intrinsic measure for quantifying heterogeneity in training data for supervised learning. This measure is the variance of a random variable which factors through the influences of pairs of training points. The variance is shown to capture data heterogeneity and can thus be used to assess if a sample is a mixture of distributions. The authors prove that the data itself contains key information that supports a partitioning into blocks. Several proof of concept studies are provided that quantify the connection between variance and heterogeneity for EMNIST image data and synthetic data. The authors establish that variance is maximal for equal mixes of distributions, and detail how variance-based data purification followed by conventional training over blocks can lead to significant increases in test accuracy.

### 🤖 AI 总结

**一句话总结**：提出一种用“成对样本影响”定义的方差来度量训练数据异质性，并据此将输入空间分块净化后分别训练，从而提升测试精度。

**研究动机**：监督学习数据往往混合多个分布导致异质性高、模型学习受干扰，但缺少一种可从数据本身直接计算、可解释的异质性量化指标来指导数据划分与训练。

**核心方法**：定义一个随机变量，其取值通过训练集中样本对的相互影响进行因子分解，并以其方差作为异质性度量；证明该方差能揭示混合分布并支持将数据划分为若干块，再进行基于方差的“数据净化”与分块常规训练。

**主要结论**：理论与实验表明该方差能有效刻画数据异质性，且在等比例混合分布时达到最大；采用方差驱动的分块/净化策略后，在EMNIST与合成数据上可显著提高测试准确率。

**关键词**：数据异质性度量, 方差指标, 混合分布检测, 训练数据分块, 输入空间划分, 基于方差的数据净化, 分块训练, 监督学习, 点对影响建模

**评分**：15

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08649v1) | [下载PDF](https://arxiv.org/pdf/2603.08649v1.pdf)

---

## [26. Grow, Don't Overwrite: Fine-tuning Without Forgetting](https://arxiv.org/abs/2603.08647v1)

**作者**：Dyah Adila, Hanna Mazzawi, Benoit Dherin 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-09

### 📄 论文摘要

Adapting pre-trained models to specialized tasks often leads to catastrophic forgetting, where new knowledge overwrites foundational capabilities. Existing methods either compromise performance on the new task or struggle to balance training stability with efficient reuse of pre-trained knowledge. We introduce a novel function-preserving expansion method that resolves this dilemma. Our technique expands model capacity by replicating pre-trained parameters within transformer submodules and applying a scaling correction that guarantees the expanded model is mathematically identical to the original at initialization, enabling stable training while exploiting existing knowledge. Empirically, our method eliminates the trade-off between plasticity and stability, matching the performance of full fine-tuning on downstream tasks without any degradation of the model's original capabilities. Furthermore, we demonstrate the modularity of our approach, showing that by selectively expanding a small subset of layers we can achieve the same performance as full fine-tuning at a fraction of the computational cost.

### 🤖 AI 总结

**一句话总结**：提出一种“函数保持的模型扩容”微调方法，在初始化时与原模型数学等价，从而在不遗忘原能力的前提下获得接近全量微调的下游性能。

**研究动机**：预训练模型在适配专门任务时常发生灾难性遗忘，现有方法往往在新任务性能（可塑性）与保留旧能力（稳定性）之间难以兼得。作者希望找到一种既稳定又能充分复用预训练知识、且训练高效的微调方案。

**核心方法**：在Transformer子模块中复制（replicate）预训练参数以扩展容量，并施加缩放校正，使扩容后的网络在初始化时与原模型函数完全一致（function-preserving）。同时支持只对少量层进行选择性扩容，以模块化方式降低计算开销。

**主要结论**：该方法实证上消除了可塑性-稳定性的权衡：下游任务性能可匹配全量微调，同时不损害原模型能力；此外，仅扩展少数层也能达到接近全量微调的效果，并显著节省计算成本。

**关键词**：灾难性遗忘, 无遗忘微调, 持续学习, 函数保持扩展, 参数复制, 缩放校正, 可塑性-稳定性权衡, 容量扩展, 选择性层扩展, 计算高效微调

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08647v1) | [下载PDF](https://arxiv.org/pdf/2603.08647v1.pdf)

---

## [27. Integral Formulas for Vector Spherical Tensor Products](https://arxiv.org/abs/2603.08630v1)

**作者**：Valentin Heyraud, Zachary Weller-Davies, Jules Tilly  
**分类**：cs.LG, physics.comp-ph  
**发布时间**：2026-03-09

### 📄 论文摘要

We derive integral formulas that simplify the Vector Spherical Tensor Product recently introduced by Xie et al., which generalizes the Gaunt tensor product to antisymmetric couplings. In particular, we obtain explicit closed-form expressions for the antisymmetric analogues of the Gaunt coefficients. This enables us to simulate the Clebsch-Gordan tensor product using a single Vector Spherical Tensor Product, yielding a $9\times$ reduction in the required tensor product evaluations. Our results enable efficient and practical implementations of the Vector Spherical Tensor Product, paving the way for applications of this generalization of Gaunt tensor products in $\mathrm{SO}(3)$-equivariant neural networks. Moreover, we discuss how the Gaunt and the Vector Spherical Tensor Products allow to control the expressivity-runtime tradeoff associated with the usual Clebsch-Gordan Tensor Products. Finally, we investigate low rank decompositions of the normalizations of the considered tensor products in view of their use in equivariant neural networks.

### 🤖 AI 总结

**一句话总结**：论文推导了向量球谐张量积（Vector Spherical Tensor Product, VSTP）的积分闭式公式与反对称“Gaunt系数”类比物，从而用一次VSTP高效模拟Clebsch–Gordan张量积并显著降低计算开销。

**研究动机**：SO(3)等变神经网络中常用的Clebsch–Gordan张量积计算代价高，而VSTP作为对Gaunt张量积的反对称推广尚缺少可高效实现的显式公式与系数表达。

**核心方法**：通过推导将VSTP简化的积分表示，给出反对称耦合对应系数的显式闭式解；进一步展示如何用单次VSTP复现Clebsch–Gordan张量积，并分析Gaunt/VSTP在表达力-运行时之间的可控折中，同时研究相关归一化项的低秩分解以利于实现。

**主要结论**：作者得到可直接实现的VSTP闭式与积分公式，使得模拟Clebsch–Gordan张量积时所需张量积评估次数减少约9倍，并为在SO(3)等变神经网络中更高效地使用Gaunt/VSTP及其低秩近似提供了实践路径。

**关键词**：矢量球面张量积, 高恩特张量积, 反对称耦合, 高恩特系数, 反对称高恩特系数, 积分公式, 闭式解, SO(3) 等变神经网络, 表达性-运行时权衡, 低秩分解, 张量归一化

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08630v1) | [下载PDF](https://arxiv.org/pdf/2603.08630v1.pdf)

---

## [28. Don't Look Back in Anger: MAGIC Net for Streaming Continual Learning with Temporal Dependence](https://arxiv.org/abs/2603.08600v1)

**作者**：Federico Giannini, Sandro D'Andrea, Emanuele Della Valle  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-09

### 📄 论文摘要

Concept drift, temporal dependence, and catastrophic forgetting represent major challenges when learning from data streams. While Streaming Machine Learning and Continual Learning (CL) address these issues separately, recent efforts in Streaming Continual Learning (SCL) aim to unify them. In this work, we introduce MAGIC Net, a novel SCL approach that integrates CL-inspired architectural strategies with recurrent neural networks to tame temporal dependence. MAGIC Net continuously learns, looks back at past knowledge by applying learnable masks over frozen weights, and expands its architecture when necessary. It performs all operations online, ensuring inference availability at all times. Experiments on synthetic and real-world streams show that it improves adaptation to new concepts, limits memory usage, and mitigates forgetting.

### 🤖 AI 总结

**一句话总结**：MAGIC Net 面向具有时间依赖的数据流提出在线可扩展的持续学习框架，通过“冻结权重+可学习掩码回看历史”与必要时的结构扩展来适应概念漂移并减轻遗忘。

**研究动机**：数据流学习同时面临概念漂移、序列时间依赖与灾难性遗忘，但传统流式学习与持续学习往往各自处理其中一部分，缺少统一且能持续在线推理的方案。

**核心方法**：将CL启发的结构策略与RNN结合：主干权重冻结以保留旧知识，在其上学习可训练掩码实现对历史能力的“选择性调用”，并在检测到容量不足时按需扩展网络；全流程在线更新，保证任意时刻可用推理。

**主要结论**：在合成与真实数据流实验中，MAGIC Net 相比基线更能快速适应新概念，同时控制内存/模型增长并显著缓解灾难性遗忘，适用于带时间依赖的流式持续学习场景。

**关键词**：流式持续学习, 数据流在线学习, 概念漂移, 时间依赖建模, 灾难性遗忘缓解, 循环神经网络, 可学习掩码, 冻结权重, 动态架构扩展, 内存受限学习

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08600v1) | [下载PDF](https://arxiv.org/pdf/2603.08600v1.pdf)

---

## [29. Towards Batch-to-Streaming Deep Reinforcement Learning for Continuous Control](https://arxiv.org/abs/2603.08588v1)

**作者**：Riccardo De Monte, Matteo Cederle, Gian Antonio Susto  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-09

### 📄 论文摘要

State-of-the-art deep reinforcement learning (RL) methods have achieved remarkable performance in continuous control tasks, yet their computational complexity is often incompatible with the constraints of resource-limited hardware, due to their reliance on replay buffers, batch updates, and target networks. The emerging paradigm of streaming deep RL addresses this limitation through purely online updates, achieving strong empirical performance on standard benchmarks. In this work, we propose two novel streaming deep RL algorithms, Streaming Soft Actor-Critic (S2AC) and Streaming Deterministic Actor-Critic (SDAC), explicitly designed to be compatible with state-of-the-art batch RL methods, making them particularly suitable for on-device finetuning applications such as Sim2Real transfer. Both algorithms achieve performance comparable to state-of-the-art streaming baselines on standard benchmarks without requiring tedious hyperparameter tuning. Finally, we further investigate the practical challenges of transitioning from batch to streaming learning during finetuning and propose concrete strategies to tackle them.

### 🤖 AI 总结

**一句话总结**：提出S2AC与SDAC两种“批量到流式”深度强化学习算法，在无需回放缓存/目标网络的纯在线更新下，实现与主流流式基线相当的连续控制性能，并更适合端侧微调与Sim2Real。

**研究动机**：现有连续控制SOTA深度RL依赖回放缓冲、批量更新和目标网络，计算/存储开销大，不适合资源受限硬件与端侧微调；流式RL虽更轻量，但与批量RL方法的兼容性与从批量到流式切换的实践问题仍未充分解决。

**核心方法**：设计Streaming Soft Actor-Critic (S2AC) 与Streaming Deterministic Actor-Critic (SDAC)，采用纯在线（逐步）更新并显式对齐SAC/DDPG等批量方法的结构与训练习惯，以提升用于在设备上finetuning的可迁移性；同时分析从batch预训练到streaming微调的过渡难点并给出可操作的应对策略。

**主要结论**：S2AC/SDAC在标准连续控制基准上达到与当前流式SOTA基线可比的表现，且无需繁琐的超参调试；论文还总结并缓解了批量→流式微调中的关键工程挑战，为Sim2Real等端侧在线适配提供了更实用的方案。

**关键词**：流式深度强化学习, 批量到流式迁移, 连续控制, 资源受限硬件, 无回放缓冲训练, 确定性策略梯度, 端侧微调, 超参数鲁棒性

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08588v1) | [下载PDF](https://arxiv.org/pdf/2603.08588v1.pdf)

---

## [30. DualFlexKAN: Dual-stage Kolmogorov-Arnold Networks with Independent Function Control](https://arxiv.org/abs/2603.08583v1)

**作者**：Andrés Ortiz, Nicolás J. Gallego-Molina, Carmen Jiménez-Mesa 等 5 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-03-09

### 📄 论文摘要

Multi-Layer Perceptrons (MLPs) rely on pre-defined, fixed activation functions, imposing a static inductive bias that forces the network to approximate complex topologies solely through increased depth and width. Kolmogorov-Arnold Networks (KANs) address this limitation through edge-centric learnable functions, yet their formulation suffers from quadratic parameter scaling and architectural rigidity that hinders the effective integration of standard regularization techniques. This paper introduces the DualFlexKAN (DFKAN), a flexible architecture featuring a dual-stage mechanism that independently controls pre-linear input transformations and post-linear output activations. This decoupling enables hybrid networks that optimize the trade-off between expressiveness and computational cost. Unlike standard formulations, DFKAN supports diverse basis function families, including orthogonal polynomials, B-splines, and radial basis functions, integrated with configurable regularization strategies that stabilize training dynamics. Comprehensive evaluations across regression benchmarks, physics-informed tasks, and function approximation demonstrate that DFKAN outperforms both MLPs and conventional KANs in accuracy, convergence speed, and gradient fidelity. The proposed hybrid configurations achieve superior performance with one to two orders of magnitude fewer parameters than standard KANs, effectively mitigating the parameter explosion problem while preserving KAN-style expressiveness. DFKAN provides a principled, scalable framework for incorporating adaptive non-linearities, proving particularly advantageous for data-efficient learning and interpretable function discovery in scientific applications.

### 🤖 AI 总结

**一句话总结**：DualFlexKAN 通过“双阶段”可学习函数将 KAN 的边函数分解为输入预变换与输出后激活两部分，在显著降低参数量的同时提升精度与训练稳定性。

**研究动机**：MLP 使用固定激活导致归纳偏置静态、需靠更深更宽拟合复杂函数；传统 KAN 虽可学习边函数但参数呈二次增长且结构刚性，难以有效结合常规正则化并稳定训练。

**核心方法**：提出 DFKAN 的双阶段机制：独立控制线性层前的输入函数变换与线性层后的输出激活，从而可灵活构建混合架构以权衡表达力与计算开销；同时支持多种基函数族（正交多项式、B-spline、RBF 等）并引入可配置正则化策略以稳定训练动态。

**主要结论**：在回归基准、物理信息任务与函数逼近实验中，DFKAN 相比 MLP 与常规 KAN 在准确率、收敛速度和梯度保真度上更优；其混合配置可用比标准 KAN 少 1–2 个数量级的参数达到更好性能，缓解参数爆炸并保留 KAN 式表达性，适合数据高效与可解释科学建模。

**关键词**：双阶段非线性控制, 可学习激活函数, 边中心函数建模, 参数规模控制, 混合神经网络架构, 正则化策略, 物理信息神经网络（PINN）, DualFlexKAN

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.08583v1) | [下载PDF](https://arxiv.org/pdf/2603.08583v1.pdf)

---

