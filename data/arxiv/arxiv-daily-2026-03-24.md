# arXiv AI 论文日报 | 2026-03-24

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (18 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.CL](#csCL) (4 篇)
- [cs.AI](#csAI) (1 篇)

---

## cs.AI

## [1. MARCUS: An agentic, multimodal vision-language model for cardiac diagnosis and management](https://arxiv.org/abs/2603.22179v1)

**作者**：Jack W O'Sullivan, Mohammad Asadi, Lennart Elbe 等 11 位作者  
**分类**：cs.AI  
**发布时间**：2026-03-23

### 📄 论文摘要

Cardiovascular disease remains the leading cause of global mortality, with progress hindered by human interpretation of complex cardiac tests. Current AI vision-language models are limited to single-modality inputs and are non-interactive. We present MARCUS (Multimodal Autonomous Reasoning and Chat for Ultrasound and Signals), an agentic vision-language system for end-to-end interpretation of electrocardiograms (ECGs), echocardiograms, and cardiac magnetic resonance imaging (CMR) independently and as multimodal input. MARCUS employs a hierarchical agentic architecture comprising modality-specific vision-language expert models, each integrating domain-trained visual encoders with multi-stage language model optimization, coordinated by a multimodal orchestrator. Trained on 13.5 million images (0.25M ECGs, 1.3M echocardiogram images, 12M CMR images) and our novel expert-curated dataset spanning 1.6 million questions, MARCUS achieves state-of-the-art performance surpassing frontier models (GPT-5 Thinking, Gemini 2.5 Pro Deep Think). Across internal (Stanford) and external (UCSF) test cohorts, MARCUS achieves accuracies of 87-91% for ECG, 67-86% for echocardiography, and 85-88% for CMR, outperforming frontier models by 34-45% (P<0.001). On multimodal cases, MARCUS achieved 70% accuracy, nearly triple that of frontier models (22-28%), with 1.7-3.0x higher free-text quality scores. Our agentic architecture also confers resistance to mirage reasoning, whereby vision-language models derive reasoning from unintended textual signals or hallucinated visual content. MARCUS demonstrates that domain-specific visual encoders with an agentic orchestrator enable multimodal cardiac interpretation. We release our models, code, and benchmark open-source.

### 🤖 AI 总结

**一句话总结**：MARCUS 是一个可交互的多模态心脏诊断代理式视觉-语言系统，能联合解读 ECG/超声/CMR 并在多项基准上显著超越通用前沿大模型。

**研究动机**：心血管检查（ECG、超声、CMR）解读复杂且高度依赖专家经验，现有视觉-语言模型多为单模态、非交互式，难以支持端到端的临床诊断与管理决策。

**核心方法**：提出分层代理架构：为 ECG/超声/CMR 各自训练“模态专家”视觉-语言模型（领域视觉编码器+多阶段语言模型优化），再由多模态编排器进行协调融合与对话式推理；并基于 1350 万图像与 160 万专家标注问答数据进行训练与评测。

**主要结论**：MARCUS 在内部/外部队列上分别取得 ECG 87–91%、超声 67–86%、CMR 85–88% 的准确率，并在多模态病例上达 70%（显著高于通用模型的 22–28%），同时提升自由文本质量并更抗“mirage reasoning”，证明领域编码器+代理编排能有效实现多模态心脏影像/信号解读，且将模型与代码开源。

**关键词**：多模态心脏诊断, 心血管影像-语言模型, 心电图解读, 超声心动图解读, 心脏磁共振解读, 分层智能体架构, 多模态编排器, 模态专家模型, 领域视觉编码器, 医疗多模态问答数据集, 幻觉抑制

**评分**：49

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22179v1) | [下载PDF](https://arxiv.org/pdf/2603.22179v1.pdf)

---

## cs.CL

## [2. TiCo: Time-Controllable Training for Spoken Dialogue Models](https://arxiv.org/abs/2603.22267v1)

**作者**：Kai-Wei Chang, Wei-Chih Chen, En-Pei Hu 等 5 位作者  
**分类**：cs.CL, cs.AI, eess.AS  
**发布时间**：2026-03-23

### 📄 论文摘要

We propose TiCo, a simple post-training method for enabling spoken dialogue models (SDMs) to follow time-constrained instructions and generate responses with controllable duration. This capability is valuable for real-world spoken language systems such as voice assistants and interactive agents, where controlling response duration can improve interaction quality. However, despite their strong ability to generate natural spoken responses, existing models lack time awareness and struggle to follow duration-related instructions (e.g., "Please generate a response lasting about 15 seconds"). Through an empirical evaluation of both open-source and commercial SDMs, we show that they frequently fail to satisfy such time-control requirements. TiCo addresses this limitation by enabling models to estimate elapsed speaking time during generation through Spoken Time Markers (STM) (e.g., <10.6 seconds>). These markers help the model maintain awareness of time and adjust the remaining content to meet the target duration. TiCo is simple and efficient: it requires only a small amount of data and no additional question-answer pairs, relying instead on self-generation and reinforcement learning. Experimental results show that TiCo significantly improves adherence to duration constraints while preserving response quality.

### 🤖 AI 总结

**一句话总结**：TiCo 通过在生成中引入“口语时间标记（STM）”让口语对话模型具备时间感知，从而能按指令生成时长可控的语音回复。

**研究动机**：真实语音助手等场景需要控制回复时长以优化交互体验，但现有口语对话模型缺乏时间意识，常无法满足“约15秒”等时长约束指令。

**核心方法**：TiCo 在后训练阶段让模型学习在生成过程中估计已用口语时间，并插入如“<10.6 seconds>”的STM来持续校准剩余内容；训练上主要依赖自生成数据与强化学习，不需要额外人工问答对且数据量较小。

**主要结论**：实验表明，TiCo 显著提升模型对时长约束的遵循能力，同时基本保持原有的回复质量与自然度。

**关键词**：口语对话模型, 响应时长可控, 时长指令遵循, 时间感知生成, 语音时间标记（STM）, 后训练方法, 自生成数据, 强化学习, 时长控制评测, 语音助手, 交互式智能体

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22267v1) | [下载PDF](https://arxiv.org/pdf/2603.22267v1.pdf)

---

## [3. Greater accessibility can amplify discrimination in generative AI](https://arxiv.org/abs/2603.22260v1)

**作者**：Carolin Holtermann, Minh Duc Bui, Kaitlyn Zhou 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-23

### 📄 论文摘要

Hundreds of millions of people rely on large language models (LLMs) for education, work, and even healthcare. Yet these models are known to reproduce and amplify social biases present in their training data. Moreover, text-based interfaces remain a barrier for many, for example, users with limited literacy, motor impairments, or mobile-only devices. Voice interaction promises to expand accessibility, but unlike text, speech carries identity cues that users cannot easily mask, raising concerns about whether accessibility gains may come at the cost of equitable treatment. Here we show that audio-enabled LLMs exhibit systematic gender discrimination, shifting responses toward gender-stereotyped adjectives and occupations solely on the basis of speaker voice, and amplifying bias beyond that observed in text-based interaction. Thus, voice interfaces do not merely extend text models to a new modality but introduce distinct bias mechanisms tied to paralinguistic cues. Complementary survey evidence ($n=1,000$) shows that infrequent chatbot users are most hesitant to undisclosed attribute inference and most likely to disengage when such practices are revealed. To demonstrate a potential mitigation strategy, we show that pitch manipulation can systematically regulate gender-discriminatory outputs. Overall, our findings reveal a critical tension in AI development: efforts to expand accessibility through voice interfaces simultaneously create new pathways for discrimination, demanding that fairness and accessibility be addressed in tandem.

### 🤖 AI 总结

**一句话总结**：语音交互虽提升大模型可达性，但会因语音中的身份线索引入并放大性别歧视，使模型输出更偏向性别刻板印象。

**研究动机**：文本界面对低识字、肢体障碍或仅移动端用户仍有门槛，而语音可能扩大覆盖人群；但语音难以隐藏性别等线索，可能让“更可达”以“更不公平”为代价。

**核心方法**：对音频输入的LLM进行对照实验，仅改变说话者声音特征（性别线索）并比较输出在形容词与职业等方面的性别刻板偏移及其相对文本交互的放大程度；并结合n=1000问卷评估用户对未披露属性推断的接受度，最后用音高（pitch）操控验证一种可调节偏见的缓解策略。

**主要结论**：音频版LLM会仅因说话者声音就系统性地产生并放大性别歧视，形成不同于文本模式的新偏见机制；用户（尤其不常用者）对隐性属性推断更反感且可能因此退出，而音高操控可在一定程度上调控/缓解歧视输出，提示公平与可达性需联合设计。

**关键词**：语音交互LLM, 生成式AI偏见, 性别歧视, 语音身份线索, 副语言特征, 属性推断, 刻板印象强化, 公平性-可访问性权衡, 语音接口偏差机制, 音高操控去偏

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22260v1) | [下载PDF](https://arxiv.org/pdf/2603.22260v1.pdf)

---

## [4. Adapting Self-Supervised Speech Representations for Cross-lingual Dysarthria Detection in Parkinson's Disease](https://arxiv.org/abs/2603.22225v1)

**作者**：Abner Hernandez, Eunjung Yeo, Kwanghee Choi 等 15 位作者  
**分类**：cs.CL, cs.SD  
**发布时间**：2026-03-23

### 📄 论文摘要

The limited availability of dysarthric speech data makes cross-lingual detection an important but challenging problem. A key difficulty is that speech representations often encode language-dependent structure that can confound dysarthria detection. We propose a representation-level language shift (LS) that aligns source-language self-supervised speech representations with the target-language distribution using centroid-based vector adaptation estimated from healthy-control speech. We evaluate the approach on oral DDK recordings from Parkinson's disease speech datasets in Czech, German, and Spanish under both cross-lingual and multilingual settings. LS substantially improves sensitivity and F1 in cross-lingual settings, while yielding smaller but consistent gains in multilingual settings. Representation analysis further shows that LS reduces language identity in the embedding space, supporting the interpretation that LS removes language-dependent structure.

### 🤖 AI 总结

**一句话总结**：提出一种表示级语言偏移（LS）方法，用少量目标语言健康语音对自监督语音表征做分布对齐，从而显著提升帕金森病构音障碍的跨语种检测性能。

**研究动机**：构音障碍语音数据稀缺使跨语种检测很重要，但自监督表征往往包含强语言相关结构，导致模型把“语言差异”误当作“病理差异”而性能下降。

**核心方法**：在表征空间中基于健康对照语音估计源语言与目标语言的类中心（centroid）差异，用该向量对源语言自监督嵌入进行平移/适配，实现语言分布对齐后再进行检测；在捷克语、德语、西班牙语的DDK任务上评估跨语种与多语种两种设置。

**主要结论**：LS在跨语种设置下显著提高敏感性与F1，多语种设置下也带来小幅但稳定增益；嵌入分析显示LS降低了语言身份可分性，支持其确实削弱语言依赖结构、突出病理相关信息。

**关键词**：跨语言构音障碍检测, 帕金森病语音评估, 自监督语音表征, 表征级语言偏移（LS）, 嵌入空间对齐, 健康对照校准, 口腔DDK任务, 多语言语音建模, 语言身份去除, 跨语言迁移学习

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22225v1) | [下载PDF](https://arxiv.org/pdf/2603.22225v1.pdf)

---

## [5. Enhancing Document-Level Machine Translation via Filtered Synthetic Corpora and Two-Stage LLM Adaptation](https://arxiv.org/abs/2603.22186v1)

**作者**：Ireh Kim, Tesia Sker, Chanwoo Kim  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-03-23

### 📄 论文摘要

In Machine Translation, Large Language Models (LLMs) have generally underperformed compared to conventional encoder-decoder systems and thus see limited adoption. However, LLMs excel at modeling contextual information, making them a natural fit for document-level translation tasks where coherence across sentences is crucial. Despite this potential, document-level MT with LLMs faces two key challenges: (1) the scarcity of large-scale, high-quality document-level parallel data; and (2) the propensity of LLMs to introduce hallucinations and omissions during generation. To address these challenges, we propose a two-stage fine-tuning strategy leveraging LLM-augmented document-level data. First, we augment data by converting summarization data into document-level parallel data using a LLM, and then filter it using multiple metrics, leveraging sacreBLEU, COMET, and LaBSE-based cosine similarity-to improve data quality. Finally, we employ a two-stage fine-tuning strategy: first fine-tuning on the abundant sentence-level MT resources, and then on the filtered document-level corpus.

### 🤖 AI 总结

**一句话总结**：通过LLM生成并多指标过滤的合成文档级平行语料，再结合“句子级→文档级”的两阶段微调，可提升LLM的文档级机器翻译质量与一致性。

**研究动机**：LLM在句子级MT上常不如传统编码器-解码器，但其上下文建模能力更适合文档级一致性需求；然而高质量文档级平行数据稀缺且LLM生成易出现幻觉与遗漏。

**核心方法**：先用LLM将摘要类数据转换为文档级平行数据进行数据增强，并用sacreBLEU、COMET与LaBSE余弦相似度等多指标联合过滤以提高语料质量；再采用两阶段微调：先在大量句子级MT资源上适配翻译能力，再在过滤后的文档级语料上强化跨句一致性。

**主要结论**：过滤后的合成文档级语料能有效缓解噪声带来的幻觉/遗漏问题，两阶段微调使LLM在文档级翻译中更好利用上下文信息，从而整体提升文档级MT表现。

**关键词**：文档级机器翻译, 两阶段微调, 合成平行语料, 平行数据增强, 语料质量过滤, 机器翻译质量评估, 余弦相似度, 幻觉与遗漏控制

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22186v1) | [下载PDF](https://arxiv.org/pdf/2603.22186v1.pdf)

---

## cs.CV

## [6. WorldCache: Content-Aware Caching for Accelerated Video World Models](https://arxiv.org/abs/2603.22286v1)

**作者**：Umair Nawaz, Ahmed Heakl, Ufaq Khan 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.CL, cs.LG  
**发布时间**：2026-03-23

### 📄 论文摘要

Diffusion Transformers (DiTs) power high-fidelity video world models but remain computationally expensive due to sequential denoising and costly spatio-temporal attention. Training-free feature caching accelerates inference by reusing intermediate activations across denoising steps; however, existing methods largely rely on a Zero-Order Hold assumption i.e., reusing cached features as static snapshots when global drift is small. This often leads to ghosting artifacts, blur, and motion inconsistencies in dynamic scenes. We propose \textbf{WorldCache}, a Perception-Constrained Dynamical Caching framework that improves both when and how to reuse features. WorldCache introduces motion-adaptive thresholds, saliency-weighted drift estimation, optimal approximation via blending and warping, and phase-aware threshold scheduling across diffusion steps. Our cohesive approach enables adaptive, motion-consistent feature reuse without retraining. On Cosmos-Predict2.5-2B evaluated on PAI-Bench, WorldCache achieves \textbf{2.3$\times$} inference speedup while preserving \textbf{99.4\%} of baseline quality, substantially outperforming prior training-free caching approaches. Our code can be accessed on \href{https://umair1221.github.io/World-Cache/}{World-Cache}.

### 🤖 AI 总结

**一句话总结**：WorldCache 提出一种感知约束的动态特征缓存机制，在不训练的前提下自适应复用扩散视频世界模型的中间特征，实现约2.3×推理加速且基本不损画质。

**研究动机**：现有训练外缓存多基于“零阶保持”(ZOH)把缓存特征当静态快照复用，只在全局漂移很小时有效；在动态场景会引入重影、模糊与运动不一致等伪影。

**核心方法**：WorldCache 同时改进“何时复用”和“如何复用”：用运动自适应阈值与显著性加权的漂移估计来决定是否命中缓存，并通过特征混合与运动/对齐式warping做最优近似以保持运动一致；另外引入扩散步的phase-aware阈值调度，随去噪阶段调整缓存策略。

**主要结论**：在 Cosmos-Predict2.5-2B（PAI-Bench）上，WorldCache 相比先前训练外缓存方法显著减少动态伪影，在保留99.4%基线质量的同时获得2.3×推理速度提升，证明内容感知的动态缓存可有效加速视频DiT世界模型推理。

**关键词**：视频世界模型, 扩散推理加速, 免训练加速, 特征缓存, 动态缓存策略, 时空注意力优化, 运动自适应阈值, 显著性加权漂移估计, 特征变形（warping）与融合, 分阶段阈值调度, 感知约束优化

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22286v1) | [下载PDF](https://arxiv.org/pdf/2603.22286v1.pdf)

---

## [7. VideoDetective: Clue Hunting via both Extrinsic Query and Intrinsic Relevance for Long Video Understanding](https://arxiv.org/abs/2603.22285v1)

**作者**：Ruoliu Yang, Chu Wu, Caifeng Shan 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

Long video understanding remains challenging for multimodal large language models (MLLMs) due to limited context windows, which necessitate identifying sparse query-relevant video segments. However, existing methods predominantly localize clues based solely on the query, overlooking the video's intrinsic structure and varying relevance across segments. To address this, we propose VideoDetective, a framework that integrates query-to-segment relevance and inter-segment affinity for effective clue hunting in long-video question answering. Specifically, we divide a video into various segments and represent them as a visual-temporal affinity graph built from visual similarity and temporal proximity. We then perform a Hypothesis-Verification-Refinement loop to estimate relevance scores of observed segments to the query and propagate them to unseen segments, yielding a global relevance distribution that guides the localization of the most critical segments for final answering with sparse observation. Experiments show our method consistently achieves substantial gains across a wide range of mainstream MLLMs on representative benchmarks, with accuracy improvements of up to 7.5% on VideoMME-long. Our code is available at https://videodetective.github.io/

### 🤖 AI 总结

**一句话总结**：VideoDetective 通过同时建模“问题-片段相关性”和“片段间内在关联”，在只稀疏观察长视频的情况下更准确地定位关键线索并提升长视频问答效果。

**研究动机**：长视频超出多模态大模型的上下文窗口，必须先找出少量与问题相关的片段；但现有方法多仅依赖问题检索，忽视视频自身结构与不同片段之间的内在相关性，导致线索定位不稳。

**核心方法**：将视频切分为多个片段，并基于视觉相似度与时间邻近性构建视觉-时序亲和图；在此图上进行“假设-验证-细化”(Hypothesis-Verification-Refinement)循环，估计已观测片段对问题的相关分数并向未观测片段传播，得到全局相关性分布以指导关键片段的稀疏采样与最终回答。

**主要结论**：在多个主流多模态大模型与代表性基准上，VideoDetective 均带来稳定且显著的长视频问答准确率提升，最高在 VideoMME-long 上提升约 7.5%，验证了结合外部查询信号与内部片段关联的线索猎取策略有效。

**关键词**：长视频问答, 视频片段定位, 稀疏观测, 查询-片段相关性, 片段间亲和力, 视觉-时间亲和图, 视觉相似性, 时间邻近性, 假设-验证-精炼循环, 相关性传播, 多模态大语言模型

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22285v1) | [下载PDF](https://arxiv.org/pdf/2603.22285v1.pdf)

---

## [8. ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model](https://arxiv.org/abs/2603.22281v1)

**作者**：Haichao Zhang, Yijiang Li, Shwai He 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.CL, cs.LG, cs.RO  
**发布时间**：2026-03-23

### 📄 论文摘要

Recent progress in latent world models (e.g., V-JEPA2) has shown promising capability in forecasting future world states from video observations. Nevertheless, dense prediction from a short observation window limits temporal context and can bias predictors toward local, low-level extrapolation, making it difficult to capture long-horizon semantics and reducing downstream utility. Vision--language models (VLMs), in contrast, provide strong semantic grounding and general knowledge by reasoning over uniformly sampled frames, but they are not ideal as standalone dense predictors due to compute-driven sparse sampling, a language-output bottleneck that compresses fine-grained interaction states into text-oriented representations, and a data-regime mismatch when adapting to small action-conditioned datasets. We propose a VLM-guided JEPA-style latent world modeling framework that combines dense-frame dynamics modeling with long-horizon semantic guidance via a dual-temporal pathway: a dense JEPA branch for fine-grained motion and interaction cues, and a uniformly sampled VLM \emph{thinker} branch with a larger temporal stride for knowledge-rich guidance. To transfer the VLM's progressive reasoning signals effectively, we introduce a hierarchical pyramid representation extraction module that aggregates multi-layer VLM representations into guidance features compatible with latent prediction. Experiments on hand-manipulation trajectory prediction show that our method outperforms both a strong VLM-only baseline and a JEPA-predictor baseline, and yields more robust long-horizon rollout behavior.

### 🤖 AI 总结

**一句话总结**：ThinkJEPA通过“双时间尺度”融合JEPA式稠密潜变量预测与VLM长时程语义推理指导，提升视频未来状态的长期预测与滚动稳定性。

**研究动机**：仅靠短窗口的稠密预测容易偏向局部低层外推、缺乏长时程语义；而VLM虽具知识与语义推理能力，但受稀疏采样与语言瓶颈限制，难以单独承担细粒度密集预测且不易适配小规模动作条件数据。

**核心方法**：提出VLM引导的JEPA潜在世界模型：一条JEPA稠密分支建模细粒度运动/交互，另一条VLM“thinker”分支对均匀采样帧进行大步长推理提供长程语义指导；并用层次金字塔表征提取模块聚合VLM多层表示，转换为与潜变量预测对齐的指导特征以进行有效知识迁移。

**主要结论**：在手部操作轨迹预测上，该方法优于强VLM-only基线与JEPA预测器基线，并在长时程rollout中表现出更稳健的行为与更好的长期语义一致性。

**关键词**：潜在世界模型, 视频未来预测, 长时序预测, 密集帧动态建模, 视觉-语言模型引导, 双时间尺度建模, 分层金字塔表征, 多层特征聚合, 动作条件轨迹预测, 手部操作轨迹预测

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22281v1) | [下载PDF](https://arxiv.org/pdf/2603.22281v1.pdf)

---

## [9. 3D-Layout-R1: Structured Reasoning for Language-Instructed Spatial Editing](https://arxiv.org/abs/2603.22279v1)

**作者**：Haoyu Zhen, Xiaolong Li, Yilin Zhao 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-23

### 📄 论文摘要

Large Language Models (LLMs) and Vision Language Models (VLMs) have shown impressive reasoning abilities, yet they struggle with spatial understanding and layout consistency when performing fine-grained visual editing. We introduce a Structured Reasoning framework that performs text-conditioned spatial layout editing via scene-graph reasoning. Given an input scene graph and a natural-language instruction, the model reasons over the graph to generate an updated scene graph that satisfies the text condition while maintaining spatial coherence. By explicitly guiding the reasoning process through structured relational representations, our approach improves both interpretability and control over spatial relationships. We evaluate our method on a new text-guided layout editing benchmark encompassing sorting, spatial alignment, and room-editing tasks. Our training paradigm yields an average 15% improvement in IoU and 25% reduction in center-distance error compared to Chain of Thought Fine-tuning (CoT-SFT) and vanilla GRPO baselines. Compared to SOTA zero-shot LLMs, our best models achieve up to 20% higher mIoU, demonstrating markedly improved spatial precision.

### 🤖 AI 总结

**一句话总结**：提出3D-Layout-R1，通过对场景图进行结构化关系推理来执行语言指令的空间布局编辑，显著提升空间一致性与编辑精度。

**研究动机**：现有LLM/VLM在细粒度视觉编辑中常出现空间理解不足与布局不一致问题，导致物体相对位置、对齐与整体场景连贯性难以可靠控制。

**核心方法**：输入为场景图与自然语言指令，模型在图上进行显式的关系推理与更新，生成满足指令且保持空间连贯的新场景图；并在包含排序、空间对齐、房间编辑的新基准上训练与评测，以结构化关系表示引导推理提升可解释性与可控性。

**主要结论**：在新基准上相较CoT-SFT与vanilla GRPO平均提升约15% IoU并降低约25%中心距离误差；相较SOTA零样本LLM最高可达约20% mIoU提升，证明结构化推理能显著增强空间编辑的精度与一致性。

**关键词**：语言指令视觉编辑, 空间布局编辑, 空间推理, 场景图推理, 结构化推理框架, 文本引导布局编辑, 关系表示, 空间一致性, 可解释性控制, 布局编辑基准, 中心距离误差

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22279v1) | [下载PDF](https://arxiv.org/pdf/2603.22279v1.pdf)

---

## [10. Repurposing Geometric Foundation Models for Multi-view Diffusion](https://arxiv.org/abs/2603.22275v1)

**作者**：Wooseok Jang, Seonghu Jeon, Jisang Han 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

While recent advances in generative latent spaces have driven substantial progress in single-image generation, the optimal latent space for novel view synthesis (NVS) remains largely unexplored. In particular, NVS requires geometrically consistent generation across viewpoints, but existing approaches typically operate in a view-independent VAE latent space. In this paper, we propose Geometric Latent Diffusion (GLD), a framework that repurposes the geometrically consistent feature space of geometric foundation models as the latent space for multi-view diffusion. We show that these features not only support high-fidelity RGB reconstruction but also encode strong cross-view geometric correspondences, providing a well-suited latent space for NVS. Our experiments demonstrate that GLD outperforms both VAE and RAE on 2D image quality and 3D consistency metrics, while accelerating training by more than 4.4x compared to the VAE latent space. Notably, GLD remains competitive with state-of-the-art methods that leverage large-scale text-to-image pretraining, despite training its diffusion model from scratch without such generative pretraining.

### 🤖 AI 总结

**一句话总结**：提出GLD，将几何基础模型的几何一致特征空间作为多视角扩散的潜空间，用于更一致的Novel View Synthesis并提升训练效率。

**研究动机**：传统NVS多在与视角无关的VAE潜空间中生成，难以保证跨视角的几何一致性；因此需要一种天然包含几何对应关系的更优潜表示。

**核心方法**：用几何基础模型提取的几何一致特征替代VAE/RAE潜变量作为扩散模型的latent，并验证该特征既能高保真重建RGB，又能编码强跨视角几何对应，从而支撑多视角一致生成。

**主要结论**：GLD在2D图像质量与3D一致性指标上优于VAE与RAE，同时训练相较VAE潜空间加速超过4.4×；在不依赖大规模文生图预训练、从零训练扩散的条件下仍能与SOTA方法竞争。

**关键词**：新视角合成, 多视图扩散模型, 几何潜空间扩散（GLD）, 几何基础模型, 几何一致性生成, 跨视角几何对应, 视角无关VAE潜空间, 2D图像质量评测, 3D一致性指标

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22275v1) | [下载PDF](https://arxiv.org/pdf/2603.22275v1.pdf)

---

## [11. DUO-VSR: Dual-Stream Distillation for One-Step Video Super-Resolution](https://arxiv.org/abs/2603.22271v1)

**作者**：Zhengyao Lv, Menghan Xia, Xintao Wang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

Diffusion-based video super-resolution (VSR) has recently achieved remarkable fidelity but still suffers from prohibitive sampling costs. While distribution matching distillation (DMD) can accelerate diffusion models toward one-step generation, directly applying it to VSR often results in training instability alongside degraded and insufficient supervision. To address these issues, we propose DUO-VSR, a three-stage framework built upon a Dual-Stream Distillation strategy that unifies distribution matching and adversarial supervision for one-step VSR. Firstly, a Progressive Guided Distillation Initialization is employed to stabilize subsequent training through trajectory-preserving distillation. Next, the Dual-Stream Distillation jointly optimizes the DMD and Real-Fake Score Feature GAN (RFS-GAN) streams, with the latter providing complementary adversarial supervision leveraging discriminative features from both real and fake score models. Finally, a Preference-Guided Refinement stage further aligns the student with perceptual quality preferences. Extensive experiments demonstrate that DUO-VSR achieves superior visual quality and efficiency over previous one-step VSR approaches.

### 🤖 AI 总结

**一句话总结**：DUO-VSR 通过双流蒸馏将分布匹配蒸馏与对抗监督结合，实现高画质且高效率的一步式视频超分辨率。

**研究动机**：扩散式VSR虽保真度高但采样成本极高；直接用DMD做一步生成在VSR上易训练不稳定且监督不足，导致画质下降。

**核心方法**：提出三阶段框架：先用渐进式引导蒸馏初始化以保持轨迹并稳定训练；再进行双流蒸馏联合优化DMD与RFS-GAN（利用真实/伪造score模型的判别特征提供互补对抗监督）；最后用偏好引导精炼进一步对齐感知质量偏好。

**主要结论**：实验表明，DUO-VSR 相比以往一步式VSR方法在视觉质量与生成效率上均取得更优表现，并缓解了DMD在VSR蒸馏中的稳定性与监督不足问题。

**关键词**：视频超分辨率, Diffusion, 单步生成, 分布匹配蒸馏, 双流蒸馏, 轨迹保持蒸馏, 渐进式引导蒸馏, 偏好引导优化, 采样加速, 训练稳定性

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22271v1) | [下载PDF](https://arxiv.org/pdf/2603.22271v1.pdf)

---

## [12. GenOpticalFlow: A Generative Approach to Unsupervised Optical Flow Learning](https://arxiv.org/abs/2603.22270v1)

**作者**：Yixuan Luo, Feng Qiao, Zhexiao Xiong 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

Optical flow estimation is a fundamental problem in computer vision, yet the reliance on expensive ground-truth annotations limits the scalability of supervised approaches. Although unsupervised and semi-supervised methods alleviate this issue, they often suffer from unreliable supervision signals based on brightness constancy and smoothness assumptions, leading to inaccurate motion estimation in complex real-world scenarios. To overcome these limitations, we introduce \textbf{\modelname}, a novel framework that synthesizes large-scale, perfectly aligned frame--flow data pairs for supervised optical flow training without human annotations. Specifically, our method leverages a pre-trained depth estimation network to generate pseudo optical flows, which serve as conditioning inputs for a next-frame generation model trained to produce high-fidelity, pixel-aligned subsequent frames. This process enables the creation of abundant, high-quality synthetic data with precise motion correspondence. Furthermore, we propose an \textit{inconsistent pixel filtering} strategy that identifies and removes unreliable pixels in generated frames, effectively enhancing fine-tuning performance on real-world datasets. Extensive experiments on KITTI2012, KITTI2015, and Sintel demonstrate that \textbf{\modelname} achieves competitive or superior results compared to existing unsupervised and semi-supervised approaches, highlighting its potential as a scalable and annotation-free solution for optical flow learning. We will release our code upon acceptance.

### 🤖 AI 总结

**一句话总结**：GenOpticalFlow 通过生成式模型合成大规模、像素级对齐的“帧-光流”数据对，在无需人工标注的情况下实现高质量光流监督训练。

**研究动机**：现有无监督/半监督光流方法依赖亮度一致性与平滑等假设，监督信号在真实复杂场景中常不可靠，导致运动估计不准；而全监督又受限于昂贵标注，难以规模化。

**核心方法**：先用预训练深度估计网络产生伪光流作为条件输入，训练下一帧生成模型生成与光流严格对齐的高保真后续帧，从而自动构造大量精准对应的合成训练数据；并提出不一致像素过滤，剔除生成帧中不可靠像素以提升在真实数据上的微调效果。

**主要结论**：在 KITTI2012/2015 与 Sintel 上，该框架相比现有无监督与半监督方法达到有竞争力或更优的光流精度，表明“生成式合成对齐数据”可作为可扩展、免标注的光流学习方案。

**关键词**：光流估计, 无监督学习, 半监督学习, 生成式建模, 合成训练数据, 帧预测生成, 深度估计, 伪光流, 像素级对齐, 不一致像素过滤

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22270v1) | [下载PDF](https://arxiv.org/pdf/2603.22270v1.pdf)

---

## [13. EgoGroups: A Benchmark For Detecting Social Groups of People in the Wild](https://arxiv.org/abs/2603.22249v1)

**作者**：Jeffri Murrugarra-Llerena, Pranav Chitale, Zicheng Liu 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

Social group detection, or the identification of humans involved in reciprocal interpersonal interactions (e.g., family members, friends, and customers and merchants), is a crucial component of social intelligence needed for agents transacting in the world. The few existing benchmarks for social group detection are limited by low scene diversity and reliance on third-person camera sources (e.g., surveillance footage). Consequently, these benchmarks generally lack real-world evaluation on how groups form and evolve in diverse cultural contexts and unconstrained settings. To address this gap, we introduce EgoGroups, a first-person view dataset that captures social dynamics in cities around the world. EgoGroups spans 65 countries covering low, medium, and high-crowd settings under four weather/time-of-day conditions. We include dense human annotations for person and social groups, along with rich geographic and scene metadata. Using this dataset, we performed an extensive evaluation of state-of-the-art VLM/LLMs and supervised models on their group detection capabilities. We found several interesting findings, including VLMs and LLMs can outperform supervised baselines in a zero-shot setting, while crowd density and cultural regions clearly influence model performance.

### 🤖 AI 总结

**一句话总结**：提出EgoGroups这一覆盖全球多城市的第一人称视角社交群体检测基准，并系统评测VLM/LLM与监督模型在真实多文化拥挤场景中的群体识别能力。

**研究动机**：现有社交群体检测数据集多来自第三人称/监控视角且场景与文化多样性不足，难以评估真实世界中群体在不同地区与拥挤度下的形成与演化。

**核心方法**：构建EgoGroups第一人称数据集，覆盖65个国家、不同拥挤度与天气/时段条件，提供密集的行人及社交群体标注与地理/场景元数据；在该基准上对SOTA VLM/LLM零样本与监督方法进行全面对比评测。

**主要结论**：实验发现VLM/LLM在零样本设置下可优于部分监督基线，同时模型表现显著受人群密度与文化区域影响，表明跨场景/跨文化的鲁棒群体检测仍具挑战。

**关键词**：社交群体检测, 人际互动识别, 第一人称数据集, 开放场景基准评测, 跨文化场景, 人群密度, 时空环境条件, 视觉语言模型（VLM）, 大语言模型（LLM）, 零样本评测, 密集人工标注

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22249v1) | [下载PDF](https://arxiv.org/pdf/2603.22249v1.pdf)

---

## [14. Riverine Land Cover Mapping through Semantic Segmentation of Multispectral Point Clouds](https://arxiv.org/abs/2603.22230v1)

**作者**：Sopitta Thurachen, Josef Taher, Matti Lehtomäki 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

Accurate land cover mapping in riverine environments is essential for effective river management, ecological understanding, and geomorphic change monitoring. This study explores the use of Point Transformer v2 (PTv2), an advanced deep neural network architecture designed for point cloud data, for land cover mapping through semantic segmentation of multispectral LiDAR data in real-world riverine environments. We utilize the geometric and spectral information from the 3-channel LiDAR point cloud to map land cover classes, including sand, gravel, low vegetation, high vegetation, forest floor, and water. The PTv2 model was trained and evaluated on point cloud data from the Oulanka river in northern Finland using both geometry and spectral features. To improve the model's generalization in new riverine environments, we additionally investigate multi-dataset training that adds sparsely annotated data from an additional river dataset. Results demonstrated that using the full-feature configuration resulted in performance with a mean Intersection over Union (mIoU) of 0.950, significantly outperforming the geometry baseline. Other ablation studies revealed that intensity and reflectance features were the key for accurate land cover mapping. The multi-dataset training experiment showed improved generalization performance, suggesting potential for developing more robust models despite limited high-quality annotated data. Our work demonstrates the potential of applying transformer-based architectures to multispectral point clouds in riverine environments. The approach offers new capabilities for monitoring sediment transport and other river management applications.

### 🤖 AI 总结

**一句话总结**：本文使用Point Transformer v2对三通道多光谱LiDAR点云做语义分割，实现河流环境地表覆盖（砂/砾石/植被/林下/水体等）高精度制图，并通过多数据集训练提升跨区域泛化。

**研究动机**：河流地表覆盖信息对河道管理、生态评估与地貌变化监测至关重要，但传统方法在复杂河岸场景与跨流域迁移时精度和泛化受限。作者希望利用同时包含几何与光谱信息的点云与更强的点云网络架构，提高分类精度并缓解标注数据不足带来的泛化问题。

**核心方法**：采用Point Transformer v2对Oulanka河的3通道LiDAR点云进行端到端语义分割，输入包含几何与光谱特征，并通过消融实验对比仅几何基线与不同特征组合。进一步引入另一条河流的稀疏标注数据进行多数据集联合训练，以评估并提升模型在新河流环境中的泛化能力。

**主要结论**：使用全特征配置可达mIoU=0.950，显著优于仅几何输入，其中强度（intensity）与反射率（reflectance）是提升准确性的关键特征。多数据集训练能改善跨数据集泛化，表明在高质量标注有限的情况下，基于Transformer的多光谱点云分割有望构建更稳健的河流地表覆盖制图模型。

**关键词**：河流地表覆盖制图, 语义分割, 点云分割, 光谱特征融合, 强度与反射率特征, 多数据集训练, 小样本标注, 跨场景泛化, 泥沙输运监测, 地貌变化监测

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22230v1) | [下载PDF](https://arxiv.org/pdf/2603.22230v1.pdf)

---

## [15. Benchmarking Deep Learning Models for Aerial LiDAR Point Cloud Semantic Segmentation under Real Acquisition Conditions: A Case Study in Navarre](https://arxiv.org/abs/2603.22229v1)

**作者**：Alex Salvatierra, José Antonio Sanz, Christian Gutiérrez 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

Recent advances in deep learning have significantly improved 3D semantic segmentation, but most models focus on indoor or terrestrial datasets. Their behavior under real aerial acquisition conditions remains insufficiently explored, and although a few studies have addressed similar scenarios, they differ in dataset design, acquisition conditions, and model selection. To address this gap, we conduct an experimental benchmark evaluating several state-of-the-art architectures on a large-scale aerial LiDAR dataset acquired under operational flight conditions in Navarre, Spain, covering heterogeneous urban, rural, and industrial landscapes. This study compares four representative deep learning models, including KPConv, RandLA-Net, Superpoint Transformer, and Point Transformer V3, across five semantic classes commonly found in airborne surveys, such as ground, vegetation, buildings, and vehicles, highlighting the inherent challenges of class imbalance and geometric variability in aerial data. Results show that all tested models achieve high overall accuracy exceeding 93%, with KPConv attaining the highest mean IoU (78.51%) through consistent performance across classes, particularly on challenging and underrepresented categories. Point Transformer V3 demonstrates superior performance on the underrepresented vehicle class (75.11% IoU), while Superpoint Transformer and RandLA-Net trade off segmentation robustness for computational efficiency.

### 🤖 AI 总结

**一句话总结**：在西班牙纳瓦拉真实机载航测条件下对多种点云语义分割模型做基准评测，KPConv整体最稳且mIoU最高，Point Transformer V3在车辆等小样本类上更占优。

**研究动机**：现有3D语义分割方法多在室内/地面数据集验证，缺少对真实机载LiDAR采集条件（地物复杂、几何变化大、类别极不均衡）下模型行为的系统比较。

**核心方法**：构建/使用覆盖城市-乡村-工业多场景的大规模机载LiDAR数据集（5类语义，如地面、植被、建筑、车辆等），对KPConv、RandLA-Net、Superpoint Transformer、Point Transformer V3进行统一实验设置下的对比评测，并分析精度与效率权衡及小类表现。

**主要结论**：所有模型总体精度均超过93%，其中KPConv取得最高mIoU 78.51%且跨类表现更稳定；Point Transformer V3在车辆类IoU达75.11%表现最佳，而Superpoint Transformer与RandLA-Net以更高计算效率换取一定的分割鲁棒性下降。

**关键词**：点云语义分割, 三维语义分割, 真实空中采集条件, 模型基准评测, 类别不平衡, 几何可变性, 精度-效率权衡, Benchmarking

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22229v1) | [下载PDF](https://arxiv.org/pdf/2603.22229v1.pdf)

---

## [16. SpatialReward: Verifiable Spatial Reward Modeling for Fine-Grained Spatial Consistency in Text-to-Image Generation](https://arxiv.org/abs/2603.22228v1)

**作者**：Sashuai Zhou, Qiang Zhou, Junpeng Ma 等 12 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-23

### 📄 论文摘要

Recent advances in text-to-image (T2I) generation via reinforcement learning (RL) have benefited from reward models that assess semantic alignment and visual quality. However, most existing reward models pay limited attention to fine-grained spatial relationships, often producing images that appear plausible overall yet contain inaccuracies in object positioning. In this work, we present \textbf{SpatialReward}, a verifiable reward model explicitly designed to evaluate spatial layouts in generated images. SpatialReward adopts a multi-stage pipeline: a \emph{Prompt Decomposer} extracts entities, attributes, and spatial metadata from free-form prompts; expert detectors provide accurate visual grounding of object positions and attributes; and a vision-language model applies chain-of-thought reasoning over grounded observations to assess complex spatial relations that are challenging for rule-based methods. To more comprehensively evaluate spatial relationships in generated images, we introduce \textbf{SpatRelBench}, a benchmark covering object attributes, orientation, inter-object relations, and rendered text placement. Experiments on Stable Diffusion and FLUX show that incorporating SpatialReward into RL training consistently improves spatial consistency and overall generation quality, with results aligned more closely to human judgments. These findings indicate that verifiable reward models hold considerable potential for enabling more accurate and controllable optimization in text-to-image generation models.

### 🤖 AI 总结

**一句话总结**：SpatialReward 提出一种可验证的空间奖励模型，用于强化学习优化文生图模型的细粒度空间一致性，并配套提出空间关系评测基准 SpatRelBench。

**研究动机**：现有文生图奖励模型多关注语义对齐与画质，往往忽略复杂且细粒度的空间关系，导致图像整体合理但物体位置/朝向/相对关系出错。

**核心方法**：采用多阶段可验证管线：Prompt Decomposer 从提示词解析实体、属性与空间元数据；专家检测器对图像中对象位置与属性做可靠视觉落地；再由视觉语言模型基于落地证据进行链式推理评估复杂空间关系，并用 SpatRelBench 覆盖属性、朝向、对象间关系与渲染文字位置等维度进行系统评测。

**主要结论**：在 Stable Diffusion 与 FLUX 上，将 SpatialReward 纳入 RL 训练能稳定提升空间一致性及整体生成质量，且更贴近人类评判，表明“可验证奖励模型”对提升文生图可控性与优化可靠性具有潜力。

**关键词**：文生图生成, 强化学习微调, 奖励模型, 可验证奖励模型, 空间一致性, 空间关系推理, 视觉定位, 专家检测器, 视觉语言模型, 链式思维推理, 提示词分解, 空间关系评测基准

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22228v1) | [下载PDF](https://arxiv.org/pdf/2603.22228v1.pdf)

---

## [17. Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models](https://arxiv.org/abs/2603.22212v1)

**作者**：Meiqi Wu, Zhixin Cai, Fufangchen Zhao 等 16 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

Video--based world models have emerged along two dominant paradigms: video generation and 3D reconstruction. However, existing evaluation benchmarks either focus narrowly on visual fidelity and text--video alignment for generative models, or rely on static 3D reconstruction metrics that fundamentally neglect temporal dynamics. We argue that the future of world modeling lies in 4D generation, which jointly models spatial structure and temporal evolution. In this paradigm, the core capability is interactive response: the ability to faithfully reflect how interaction actions drive state transitions across space and time. Yet no existing benchmark systematically evaluates this critical dimension. To address this gap, we propose Omni--WorldBench, a comprehensive benchmark specifically designed to evaluate the interactive response capabilities of world models in 4D settings. Omni--WorldBench comprises two key components: Omni--WorldSuite, a systematic prompt suite spanning diverse interaction levels and scene types; and Omni--Metrics, an agent-based evaluation framework that quantifies world modeling capabilities by measuring the causal impact of interaction actions on both final outcomes and intermediate state evolution trajectories. We conduct extensive evaluations of 18 representative world models across multiple paradigms. Our analysis reveals critical limitations of current world models in interactive response, providing actionable insights for future research. Omni-WorldBench will be publicly released to foster progress in interactive 4D world modeling.

### 🤖 AI 总结

**一句话总结**：Omni-WorldBench 提出一个面向4D世界模型的交互响应评测基准，用系统化提示与基于智能体的度量来衡量“动作→状态变化”的因果一致性。

**研究动机**：现有评测要么偏重视频生成的画质与文图对齐，要么依赖静态3D重建指标，普遍忽视时序动态与交互导致的状态转移。作者认为未来世界模型关键在4D生成中的“可交互响应”，但缺乏专门基准进行系统评估。

**核心方法**：构建 Omni-WorldBench：包含覆盖不同交互级别与场景类型的提示集 Omni-WorldSuite，以及通过智能体评估动作对最终结果与中间轨迹因果影响的 Omni-Metrics。并在18个代表性世界模型、跨多种范式上进行对比评测与诊断分析。

**主要结论**：实验显示当前世界模型在交互响应方面存在显著短板，难以稳定、因果一致地反映交互动作引发的时空状态演化。该基准的发布为后续提升交互式4D世界建模提供了可量化的评测工具与改进方向。

**关键词**：4D世界模型, 交互响应评测, 世界模型基准, 代理评测框架, 因果影响度量, 交互动作, 状态转移, 时空建模, 时间动态评估, 中间状态轨迹, 视频生成评测, 3D重建评测

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22212v1) | [下载PDF](https://arxiv.org/pdf/2603.22212v1.pdf)

---

## [18. Mixture of Mini Experts: Overcoming the Linear Layer Bottleneck in Multiple Instance Learning](https://arxiv.org/abs/2603.22198v1)

**作者**：Daniel Shao, Joel Runevic, Richard J. Chen 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

Multiple Instance Learning (MIL) is the predominant framework for classifying gigapixel whole-slide images in computational pathology. MIL follows a sequence of 1) extracting patch features, 2) applying a linear layer to obtain task-specific patch features, and 3) aggregating the patches into a slide feature for classification. While substantial efforts have been devoted to optimizing patch feature extraction and aggregation, none have yet addressed the second point, the critical layer which transforms general-purpose features into task-specific features. We hypothesize that this layer constitutes an overlooked performance bottleneck and that stronger representations can be achieved with a low-rank transformation tailored to each patch's phenotype, yielding synergistic effects with any of the existing MIL approaches. To this end, we introduce MAMMOTH, a parameter-efficient, multi-head mixture of experts module designed to improve the performance of any MIL model with minimal alterations to the total number of parameters. Across eight MIL methods and 19 different classification tasks, we find that such task-specific transformation has a larger effect on performance than the choice of aggregation method. For instance, when equipped with MAMMOTH, even simple methods such as max or mean pooling attain higher average performance than any method with the standard linear layer. Overall, MAMMOTH improves performance in 130 of the 152 examined configurations, with an average $+3.8\%$ change in performance. Code is available at https://github.com/mahmoodlab/mammoth.

### 🤖 AI 总结

**一句话总结**：提出MAMMOTH（Mixture of Mini Experts）替换MIL中常被忽视的“线性层”，以更强的任务特定特征变换显著提升病理全切片分类性能。

**研究动机**：现有MIL主要优化特征提取与聚合，却默认用一个线性层将通用特征转为任务特征；作者认为该线性层是性能瓶颈，限制了对不同patch表型的适配。

**核心方法**：在patch到任务特定表示的阶段，引入参数高效的多头“小专家混合”(低秩/分解式变换并按patch表型路由/加权)，作为可插拔模块与各种MIL聚合器协同，且几乎不增加总参数量。

**主要结论**：在8种MIL方法、19个任务的152种配置中，MAMMOTH在130种配置上带来提升，平均提升约+3.8%；任务特定变换的影响甚至超过聚合方法选择，使简单的mean/max pooling也能优于使用标准线性层的更复杂方法。

**关键词**：多实例学习, 计算病理, 全切片图像, 千兆像素图像分类, 线性层瓶颈, 任务特定特征变换, 低秩变换, 混合专家模型, 参数高效微调, 多头专家模块, 补丁表型自适应, 池化聚合（最大/均值）

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22198v1) | [下载PDF](https://arxiv.org/pdf/2603.22198v1.pdf)

---

## [19. PAM: A Pose-Appearance-Motion Engine for Sim-to-Real HOI Video Generation](https://arxiv.org/abs/2603.22193v1)

**作者**：Mingju Gao, Kaisen Yang, Huan-ang Gao 等 15 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

Hand-object interaction (HOI) reconstruction and synthesis are becoming central to embodied AI and AR/VR. Yet, despite rapid progress, existing HOI generation research remains fragmented across three disjoint tracks: (1) pose-only synthesis that predicts MANO trajectories without producing pixels; (2) single-image HOI generation that hallucinates appearance from masks or 2D cues but lacks dynamics; and (3) video generation methods that require both the entire pose sequence and the ground-truth first frame as inputs, preventing true sim-to-real deployment. Inspired by the philosophy of Joo et al. (2018), we think that HOI generation requires a unified engine that brings together pose, appearance, and motion within one coherent framework. Thus we introduce PAM: a Pose-Appearance-Motion Engine for controllable HOI video generation. The performance of our engine is validated by: (1) On DexYCB, we obtain an FVD of 29.13 (vs. 38.83 for InterDyn), and MPJPE of 19.37 mm (vs. 30.05 mm for CosHand), while generating higher-resolution 480x720 videos compared to 256x256 and 256x384 baselines. (2) On OAKINK2, our full multi-condition model improves FVD from 68.76 to 46.31. (3) An ablation over input conditions on DexYCB shows that combining depth, segmentation, and keypoints consistently yields the best results. (4) For a downstream hand pose estimation task using SimpleHand, augmenting training with 3,400 synthetic videos (207k frames) allows a model trained on only 50% of the real data plus our synthetic data to match the 100% real baseline.

### 🤖 AI 总结

**一句话总结**：PAM提出一个统一的Pose-Appearance-Motion生成引擎，在不依赖真实首帧/完整GT姿态序列的前提下实现可控的仿真到真实（sim-to-real）手-物交互视频生成，并在多数据集上显著提升视频质量与姿态精度。

**研究动机**：现有HOI生成研究割裂为“只生成姿态”“只生成单帧外观”“视频生成但强依赖真实首帧与完整姿态序列”三条路线，难以形成真正可部署的sim-to-real方案。作者希望把姿态、外观与运动统一到一个框架中，既能生成像素级视频，又能保持时序动力学一致性与可控性。

**核心方法**：PAM构建一个将姿态（如关键点/手模型线索）、外观（如分割/深度等条件）与运动建模耦合的多条件视频生成框架，通过组合深度+分割+关键点等输入条件来增强可控生成与时序一致性。并在DexYCB与OAKINK2上进行完整模型与条件消融，同时用生成数据增强下游手姿态估计验证其有效性。

**主要结论**：在DexYCB上PAM以更高分辨率生成视频的同时取得更低FVD与更优MPJPE（相对多种基线明显提升），在OAKINK2上也将FVD大幅降低；消融表明深度+分割+关键点的条件组合最佳。生成的3,400段合成视频可显著增强手姿态估计，使仅用50%真实数据+合成数据达到100%真实数据训练的性能。

**关键词**：手-物体交互（HOI）生成, 可控视频生成, 姿态-外观-运动联合建模, 条件视频生成, 深度-分割-关键点条件, HOI重建与合成, 三维手部姿态估计（MPJPE）, 合成数据增强

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22193v1) | [下载PDF](https://arxiv.org/pdf/2603.22193v1.pdf)

---

## [20. A Backbone Benchmarking Study on Self-supervised Learning as a Auxiliary Task with Texture-based Local Descriptors for Face Analysis](https://arxiv.org/abs/2603.22190v1)

**作者**：Shukesh Reddy, Abhijit Das  
**分类**：cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

In this work, we benchmark with different backbones and study their impact for self-supervised learning (SSL) as an auxiliary task to blend texture-based local descriptors into feature modelling for efficient face analysis. It is established in previous work that combining a primary task and a self-supervised auxiliary task enables more robust and discriminative representation learning.   We employed different shallow to deep backbones for the SSL task of Masked Auto-Encoder (MAE) as an auxiliary objective to reconstruct texture features such as local patterns alongside the primary task in local pattern SSAT (L-SSAT), ensuring robust and unbiased face analysis.   To expand the benchmark, we conducted a comprehensive comparative analysis across multiple model configurations within the proposed framework. To this end, we address the three research questions: "What is the role of the backbone in performance L-SSAT?", "What type of backbone is effective for different face analysis tasks?", and "Is there any generalized backbone for effective face analysis with L-SSAT?".   Towards answering these questions, we provide a detailed study and experiments. The performance evaluation demonstrates that the backbone for the proposed method is highly dependent on the downstream task, achieving average accuracies of 0.94 on FaceForensics++, 0.87 on CelebA, and 0.88 on AffectNet.   For consistency of feature representation quality and generalisation capability across various face analysis paradigms, including face attribute prediction, emotion classification, and deepfake detection, there is no unified backbone.

### 🤖 AI 总结

**一句话总结**：本文系统评测不同网络骨干在L-SSAT框架中作为MAE自监督辅助任务的作用，发现骨干选择强依赖下游人脸任务且不存在通用最优骨干。

**研究动机**：以往研究表明“主任务+自监督辅助任务”可提升表征鲁棒性，但在将纹理型局部描述子融入人脸分析时，不同backbone对效果的影响尚缺乏系统基准。

**核心方法**：在L-SSAT中引入MAE作为辅助目标，让不同深浅backbone在重建局部纹理特征（如local patterns）的同时优化主任务，并在深伪检测、属性预测、表情识别等多任务上进行多配置对比实验以回答骨干选择问题。

**主要结论**：实验显示性能随任务而变：在FaceForensics++、CelebA、AffectNet上平均准确率分别达0.94/0.87/0.88，但跨不同人脸分析范式并不存在一致泛化、表现最优的统一骨干网络。

**关键词**：人脸分析, 自监督学习, 辅助任务, 局部纹理描述子, 局部模式建模, 骨干网络基准评测, 多任务表示学习, 深度伪造检测, 人脸属性预测, 情绪识别, 跨数据集泛化

**评分**：14

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22190v1) | [下载PDF](https://arxiv.org/pdf/2603.22190v1.pdf)

---

## [21. Seeing is Improving: Visual Feedback for Iterative Text Layout Refinement](https://arxiv.org/abs/2603.22187v1)

**作者**：Junrong Guo, Shancheng Fang, Yadong Qu 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-23

### 📄 论文摘要

Recent advances in Multimodal Large Language Models (MLLMs) have enabled automated generation of structured layouts from natural language descriptions. Existing methods typically follow a code-only paradigm that generates code to represent layouts, which are then rendered by graphic engines to produce final images. However, they are blind to the rendered visual outcome, making it difficult to guarantee readability and aesthetics. In this paper, we identify visual feedback as a critical factor in layout generation and propose Visual Feedback Layout Model (VFLM), a self-improving framework that leverages visual feedback iterative refinement. VFLM is capable of performing adaptive reflective generation, which leverages visual information to reflect on previous issues and iteratively generates outputs until satisfactory quality is achieved. It is achieved through reinforcement learning with a visually grounded reward model that incorporates OCR accuracy. By rewarding only the final generated outcome, we can effectively stimulate the model's iterative and reflective generative capabilities. Experiments across multiple benchmarks show that VFLM consistently outperforms advanced MLLMs, existing layout models, and code-only baselines, establishing visual feedback as critical for design-oriented MLLMs. Our code and data are available at https://github.com/FolSpark/VFLM.

### 🤖 AI 总结

**一句话总结**：论文提出VFLM，通过“渲染后的视觉反馈+迭代反思生成”来持续修正文本版式，从而显著提升可读性与美观性。

**研究动机**：现有“只生成代码”的版式方法看不到最终渲染效果，难以及时发现遮挡、对齐、字体可读性等视觉问题，导致输出质量不可控。作者认为视觉反馈是版式生成的关键缺口，需要让模型基于图像结果进行自我改进。

**核心方法**：VFLM在每轮生成后将代码渲染成图像，并利用视觉信息进行反思与迭代修订，直到达到满意质量；训练上采用强化学习，并引入视觉落地的奖励模型（结合OCR准确率）来评价最终渲染结果。通过只奖励最终产物，鼓励模型学会多轮自我纠错与改进。

**主要结论**：在多个基准上，VFLM稳定优于先进MLLM、已有布局模型和代码-only基线，证明“基于视觉结果的反馈迭代”对设计导向的多模态布局生成至关重要。

**关键词**：文本到版面生成, 视觉反馈, 迭代式版面优化, 反思式生成, 强化学习, 视觉对齐奖励模型, OCR准确率奖励, 代码式版面生成, 可读性与美观评估

**评分**：52

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22187v1) | [下载PDF](https://arxiv.org/pdf/2603.22187v1.pdf)

---

## [22. Beyond Matching to Tiles: Bridging Unaligned Aerial and Satellite Views for Vision-Only UAV Navigation](https://arxiv.org/abs/2603.22153v1)

**作者**：Kejia Liu, Haoyang Zhou, Ruoyu Xu 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-23

### 📄 论文摘要

Recent advances in cross-view geo-localization (CVGL) methods have shown strong potential for supporting unmanned aerial vehicle (UAV) navigation in GNSS-denied environments. However, existing work predominantly focuses on matching UAV views to onboard map tiles, which introduces an inherent trade-off between accuracy and storage overhead, and overlooks the importance of the UAV's heading during navigation. Moreover, the substantial discrepancies and varying overlaps in cross-view scenarios have been insufficiently considered, limiting their generalization to real-world scenarios. In this paper, we present Bearing-UAV, a purely vision-driven cross-view navigation method that jointly predicts UAV absolute location and heading from neighboring features, enabling accurate, lightweight, and robust navigation in the wild. Our method leverages global and local structural features and explicitly encodes relative spatial relationships, making it robust to cross-view variations, misalignment, and feature-sparse conditions. We also present Bearing-UAV-90k, a multi-city benchmark for evaluating cross-view localization and navigation. Extensive experiments show encouraging results that Bearing-UAV yields lower localization error than previous matching/retrieval paradigm across diverse terrains. Our code and dataset will be made publicly available.

### 🤖 AI 总结

**一句话总结**：提出Bearing-UAV，一种纯视觉的跨视角方法，可同时预测无人机绝对位置与航向，在GNSS缺失场景下实现更准确且轻量的导航。

**研究动机**：现有跨视角地理定位多依赖“匹配到地图切片”的检索范式，存在精度与存储开销的权衡，并且常忽视航向信息；同时跨视角差异大、重叠不定与视角未对齐等问题削弱了真实场景泛化。

**核心方法**：Bearing-UAV通过融合全局与局部结构特征，并显式编码邻域特征间的相对空间关系，联合回归无人机的绝对位置与heading，从而提升对跨视角变化、未对齐、以及特征稀疏区域的鲁棒性；并构建多城市基准Bearing-UAV-90k用于评测定位与导航。

**主要结论**：在多地形与多城市实验中，Bearing-UAV相较以往匹配/检索到切片的方法取得更低的定位误差，验证了联合预测位置与航向及关系建模对“野外”跨视角导航的有效性与泛化能力。

**关键词**：跨视角地理定位, 视觉导航, 无人机导航, 航向估计, 航拍-卫星跨视角匹配, 视角差异鲁棒性, 视角重叠变化, 相对空间关系编码, 全局-局部结构特征, 多城市评测基准

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22153v1) | [下载PDF](https://arxiv.org/pdf/2603.22153v1.pdf)

---

## [23. OpenEarth-Agent: From Tool Calling to Tool Creation for Open-Environment Earth Observation](https://arxiv.org/abs/2603.22148v1)

**作者**：Sijie Zhao, Feng Liu, Xueliang Zhang 等 14 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

Earth Observation (EO) is essential for perceiving dynamic land surface changes, yet deploying autonomous EO in open environments is hindered by the immense diversity of multi-source data and heterogeneous tasks. While remote sensing agents have emerged to streamline EO workflows, existing tool-calling agents are confined to closed environments. They rely on pre-defined tools and are restricted to narrow scope, limiting their generalization to the diverse data and tasks. To overcome these limitations, we introduce OpenEarth-Agent, the first tool-creation agent framework tailored for open-environment EO. Rather than calling predefined tools, OpenEarth-Agent employs adaptive workflow planning and tool creation to generalize to unseen data and tasks. This adaptability is bolstered by an open-ended integration of multi-stage tools and cross-domain knowledge bases, enabling robust execution in the entire EO pipeline across multiple application domains. To comprehensively evaluate EO agents in open environments, we propose OpenEarth-Bench, a novel benchmark comprising 596 real-world, full-pipeline cases across seven application domains, explicitly designed to assess agents' adaptive planning and tool creation capabilities. Only essential pre-trained model tools are provided in this benchmark, devoid of any other predefined task-specific tools. Extensive experiments demonstrate that OpenEarth-Agent successfully masters full-pipeline EO across multiple domains in the open environment. Notably, on the cross-benchmark Earth-Bench, our tool-creating agent equipped with 6 essential pre-trained models achieves performance comparable to tool-calling agents relying on 104 specialized tools, and significantly outperforms them when provided with the complete toolset. In several cases, the created tools exhibit superior robustness to data anomalies compared to human-engineered counterparts.

### 🤖 AI 总结

**一句话总结**：OpenEarth-Agent 面向开放环境地球观测提出“工具创建”型智能体，通过自适应规划与动态生成工具来完成多域全流程 EO 任务，并在新基准 OpenEarth-Bench 上验证其泛化与鲁棒性。

**研究动机**：现有 EO 智能体多为“工具调用”，依赖预定义且封闭的工具集，难以适应开放环境中多源数据多样性与异构任务需求，导致泛化能力受限。

**核心方法**：提出 OpenEarth-Agent：以自适应工作流规划为核心，在执行过程中按需创建并组合多阶段工具，并开放式接入跨领域知识库与少量必要的预训练模型工具以覆盖完整 EO 管线；同时构建 OpenEarth-Bench（596 个真实全流程案例、7 个应用域），仅提供必要模型工具以专门评测规划与工具创建能力。

**主要结论**：实验显示 OpenEarth-Agent 能在开放环境跨多领域掌握全流程 EO；在 Earth-Bench 上仅用 6 个必要预训练模型工具即可达到依赖 104 个专用工具的工具调用型方法相当的表现，并在提供完整工具集时显著超越，且部分自动创建的工具对数据异常更鲁棒。

**关键词**：地球观测自动化, 开放环境遥感, 遥感智能体, 工具创建, 自适应工作流规划, 多源遥感数据融合, 端到端遥感管线, 跨领域知识库集成, 开放环境基准评测, 未知任务泛化, 数据异常鲁棒性

**评分**：57

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22148v1) | [下载PDF](https://arxiv.org/pdf/2603.22148v1.pdf)

---

## cs.LG

## [24. Scaling DoRA: High-Rank Adaptation via Factored Norms and Fused Kernels](https://arxiv.org/abs/2603.22276v1)

**作者**：Alexandra Zelenin, Alexandra Zhuravlyova  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-03-23

### 📄 论文摘要

Weight-Decomposed Low-Rank Adaptation (DoRA) extends LoRA by decoupling weight magnitude from direction, but its forward pass requires the row-wise norm of W + sBA, a computation that every major framework we surveyed implements by materializing the dense [d_out, d_in] product BA. At d_in = 8192 and rank r = 384, a single module's norm requires about 512 MB of transient working memory in bf16, making high-rank DoRA costly and often infeasible on common single-GPU setups once hundreds of adapted modules and checkpointing are involved.   We present two systems contributions. A factored norm decomposes the squared norm into base, cross, and Gram terms computable through O(d_out r + r^2) intermediates, eliminating the dense product. Fused Triton kernels collapse the four-kernel DoRA composition into a single pass, reducing memory traffic by about 4x and using a numerically stable form that avoids catastrophic cancellation in the near-unity rescaling regime where magnitude scales concentrate in practice.   Across six 8-32B vision-language models (VLMs) on three NVIDIA GPUs (RTX 6000 PRO, H200, B200) at r = 384 in bf16, the fused implementation is 1.5-2.0x faster than Hugging Face PEFT's DoRA implementation for inference and 1.5-1.9x faster for gradient computation (optimizer step excluded), with up to 7 GB lower peak VRAM. Microbenchmarks on six GPUs spanning four architecture generations (L40S, A100, RTX 6000 PRO, H200, B200, B300) confirm 1.5-2.7x compose-kernel speedup. Final-logit cosine similarity exceeds 0.9999 across all model/GPU pairs, and multi-seed training curves match within 7.1 x 10^-4 mean per-step loss delta over 2000 steps.

### 🤖 AI 总结

**一句话总结**：本文通过“因子化范数计算+Triton融合算子”消除DoRA高秩适配中的密集临时张量开销，使高rank（如r=384）DoRA在常见单卡上更省显存且显著加速。

**研究动机**：现有DoRA在计算||W+sBA||的行范数时通常会显式物化[d_out,d_in]的BA密集乘积，导致巨大的瞬时显存（如8192×384时单模块约512MB bf16），使高秩与多模块训练/推理成本过高甚至不可行。

**核心方法**：提出“因子化范数”(factored norm)，将平方范数分解为base/cross/Gram项，仅用O(d_out·r + r^2)中间量完成计算，避免生成BA密集矩阵；并用融合的Triton kernel把DoRA原本多算子组合合并为单次pass，减少约4×内存读写，同时用数值稳定形式避免接近1的重缩放下的灾难性消减。

**主要结论**：在6个8–32B VLM、三类GPU上，r=384 bf16时相对HF PEFT DoRA推理与反传分别提升约1.5–2.0×和1.5–1.9×，峰值显存最多降低7GB；多GPU微基准验证1.5–2.7×加速，且数值一致性高（logit余弦>0.9999、训练loss曲线几乎重合）。

**关键词**：参数高效微调, 高秩适配, 权重分解, 分解范数, 融合算子, 显存优化, 推理加速, 视觉语言模型

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22276v1) | [下载PDF](https://arxiv.org/pdf/2603.22276v1.pdf)

---

## [25. Decoupling Exploration and Policy Optimization: Uncertainty Guided Tree Search for Hard Exploration](https://arxiv.org/abs/2603.22273v1)

**作者**：Zakaria Mhammedi, James Cohan  
**分类**：cs.LG  
**发布时间**：2026-03-23

### 📄 论文摘要

The process of discovery requires active exploration -- the act of collecting new and informative data. However, efficient autonomous exploration remains a major unsolved problem. The dominant paradigm addresses this challenge by using Reinforcement Learning (RL) to train agents with intrinsic motivation, maximizing a composite objective of extrinsic and intrinsic rewards. We suggest that this approach incurs unnecessary overhead: while policy optimization is necessary for precise task execution, employing such machinery solely to expand state coverage may be inefficient. In this paper, we propose a new paradigm that explicitly separates exploration from exploitation and bypasses RL during the exploration phase. Our method uses a tree-search strategy inspired by the Go-With-The-Winner algorithm, paired with a measure of epistemic uncertainty to systematically drive exploration. By removing the overhead of policy optimization, our approach explores an order of magnitude more efficiently than standard intrinsic motivation baselines on hard Atari benchmarks. Further, we demonstrate that the discovered trajectories can be distilled into deployable policies using existing supervised backward learning algorithms, achieving state-of-the-art scores by a wide margin on Montezuma's Revenge, Pitfall!, and Venture without relying on domain-specific knowledge. Finally, we demonstrate the generality of our framework in high-dimensional continuous action spaces by solving the MuJoCo Adroit dexterous manipulation and AntMaze tasks in a sparse-reward setting, directly from image observations and without expert demonstrations or offline datasets. To the best of our knowledge, this has not been achieved before.

### 🤖 AI 总结

**一句话总结**：提出一种将“探索”与“策略优化”解耦的框架：用不确定性引导的树搜索高效收集轨迹，再用监督学习蒸馏成可执行策略，在硬探索与稀疏奖励任务上显著优于内在奖励RL基线。

**研究动机**：传统“内在动机+RL”把扩大状态覆盖与精确执行绑在同一套策略优化流程里，导致仅为探索付出昂贵的RL训练开销、效率低且在硬探索环境中表现受限。作者认为探索可先独立完成数据发现，再在需要时进行策略学习。

**核心方法**：探索阶段完全绕过RL，采用受Go-With-The-Winner启发的树搜索，在分支选择中结合表征模型的认知（epistemic）不确定性来系统性地驱动新状态/新轨迹发现。随后将搜索得到的高价值轨迹用现有的监督式“反向学习/回溯模仿”方法蒸馏为可部署策略，实现从探索到执行的解耦流水线。

**主要结论**：该方法在Atari硬探索基准上探索效率较内在动机基线提升一个数量级，并在Montezuma’s Revenge、Pitfall!、Venture上无需领域知识即可大幅刷新SOTA分数。它还可推广到高维连续动作与稀疏奖励（如MuJoCo Adroit与AntMaze），从图像观测直接学习且不依赖专家示范或离线数据。

**关键词**：硬探索, 不确定性引导树搜索, 认知不确定性, 内在动机, 稀疏奖励, 轨迹蒸馏, 监督式逆向学习, 连续控制（图像观测）, 灵巧操作（Adroit）

**评分**：41

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22273v1) | [下载PDF](https://arxiv.org/pdf/2603.22273v1.pdf)

---

## [26. Revisiting Quantum Code Generation: Where Should Domain Knowledge Live?](https://arxiv.org/abs/2603.22184v1)

**作者**：Oscar Novo, Oscar Bastidas-Jossa, Alberto Calvo 等 5 位作者  
**分类**：cs.LG, quant-ph  
**发布时间**：2026-03-23

### 📄 论文摘要

Recent advances in large language models (LLMs) have enabled the automation of an increasing number of programming tasks, including code generation for scientific and engineering domains. In rapidly evolving software ecosystems such as quantum software development, where frameworks expose complex abstractions, a central question is how best to incorporate domain knowledge into LLM-based assistants while preserving maintainability as libraries evolve.   In this work, we study specialization strategies for Qiskit code generation using the Qiskit-HumanEval benchmark. We compare a parameter-specialized fine-tuned baseline introduced in prior work against a range of recent general-purpose LLMs enhanced with retrieval-augmented generation (RAG) and agent-based inference with execution feedback.   Our results show that modern general-purpose LLMs consistently outperform the parameter-specialized baseline. While the fine-tuned model achieves approximately 47% pass@1 on Qiskit-HumanEval, recent general-purpose models reach 60-65% under zero-shot and retrieval-augmented settings, and up to 85% for the strongest evaluated model when combined with iterative execution-feedback agents -representing an improvement of more than 20% over zero-shot general-purpose performance and more than 35% over the parameter-specialized baseline.   Agentic execution feedback yields the most consistent improvements, albeit at increased runtime cost, while RAG provides modest and model-dependent gains. These findings indicate that performance gains can be achieved without domain-specific fine-tuning, instead relying on inference-time augmentation, thereby enabling a more flexible and maintainable approach to LLM-assisted quantum software development.

### 🤖 AI 总结

**一句话总结**：论文发现：在Qiskit量子代码生成任务上，通用大模型通过推理时增强（尤其是带执行反馈的agent）可显著超越领域微调模型，最高达约85% pass@1。

**研究动机**：量子软件生态演进快、API抽象复杂，领域微调模型维护成本高且易随库版本变化失效，因此需要探索“领域知识应放在参数里还是推理时”的更可维护方案。

**核心方法**：基于Qiskit-HumanEval基准，对比参数微调的专用模型与多种通用LLM在零样本、RAG检索增强、以及结合可执行反馈的迭代式agent推理三种设置下的代码生成表现。

**主要结论**：通用LLM在零样本与RAG下已达到约60–65% pass@1，明显超过微调基线约47%；引入执行反馈agent后最强模型可达约85%，增益最稳定但运行成本更高，而RAG提升较温和且依赖模型，表明无需领域微调也能通过推理时增强获得更高性能与可维护性。

**关键词**：量子代码生成, 量子软件开发, 领域知识注入, LLM代码生成, 参数微调, 推理时增强, 检索增强生成（RAG）, 执行反馈代理（Agent）, 零样本评测

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22184v1) | [下载PDF](https://arxiv.org/pdf/2603.22184v1.pdf)

---

## [27. Calibeating Made Simple](https://arxiv.org/abs/2603.22167v1)

**作者**：Yurong Chen, Zhiyi Huang, Michael I. Jordan 等 4 位作者  
**分类**：cs.LG, cs.AI, cs.GT, econ.TH  
**发布时间**：2026-03-23

### 📄 论文摘要

We study calibeating, the problem of post-processing external forecasts online to minimize cumulative losses and match an informativeness-based benchmark. Unlike prior work, which analyzed calibeating for specific losses with specific arguments, we reduce calibeating to existing online learning techniques and obtain results for general proper losses. More concretely, we first show that calibeating is minimax-equivalent to regret minimization. This recovers the $O(\log T)$ calibeating rate of Foster and Hart [FH23] for the Brier and log losses and its optimality, and yields new optimal calibeating rates for mixable losses and general bounded losses. Second, we prove that multi-calibeating is minimax-equivalent to the combination of calibeating and the classical expert problem. This yields new optimal multi-calibeating rates for mixable losses, including Brier and log losses, and general bounded losses. Finally, we obtain new bounds for achieving calibeating and calibration simultaneously for the Brier loss. For binary predictions, our result gives the first calibrated algorithm that at the same time also achieves the optimal $O(\log T)$ calibeating rate.

### 🤖 AI 总结

**一句话总结**：本文将“calibeating”（在线后处理外部预测以同时逼近信息量基准并最小化累计损失）系统化地归约到在线学习中的遗憾最小化框架，从而得到适用于一般 proper loss 的最优速率结果。

**研究动机**：以往工作往往针对特定损失函数（如Brier、log）用特定技巧分析calibeating，缺乏统一理论与对一般损失的最优界。作者希望用现成的在线学习工具给出更通用、可复用且可证明最优的calibeating与multi-calibeating性能界。

**核心方法**：首先证明calibeating与遗憾最小化在minimax意义下等价，从而可直接调用在线学习中对mixable损失与一般有界损失的最优遗憾界来推出calibeating速率；随后证明multi-calibeating在minimax上等价于“calibeating + 经典专家问题”的组合，并进一步分析在Brier损失下同时实现calibeating与校准（calibration）的算法与界。

**主要结论**：该归约统一恢复并解释了FH23在Brier与log损失上的$O(\log T)$ calibeating速率及其最优性，并给出mixable损失与一般有界损失下新的最优calibeating与multi-calibeating速率；此外在二元预测的Brier损失下，首次给出同时满足校准且仍达到最优$O(\log T)$ calibeating的算法界。

**关键词**：预测后处理, 校准与信息性基准, 最小最大等价, 遗憾最小化, 有界损失, 二元概率预测, Calibeating, Made

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22167v1) | [下载PDF](https://arxiv.org/pdf/2603.22167v1.pdf)

---

## [28. Causal Evidence that Language Models use Confidence to Drive Behavior](https://arxiv.org/abs/2603.22161v1)

**作者**：Dharshan Kumaran, Nathaniel Daw, Simon Osindero 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-23

### 📄 论文摘要

Metacognition -- the ability to assess one's own cognitive performance -- is documented across species, with internal confidence estimates serving as a key signal for adaptive behavior. While confidence can be extracted from Large Language Model (LLM) outputs, whether models actively use these signals to regulate behavior remains a fundamental question. We investigate this through a four-phase abstention paradigm.Phase 1 established internal confidence estimates in the absence of an abstention option. Phase 2 revealed that LLMs apply implicit thresholds to these estimates when deciding to answer or abstain. Confidence emerged as the dominant predictor of behavior, with effect sizes an order of magnitude larger than knowledge retrieval accessibility (RAG scores) or surface-level semantic features. Phase 3 provided causal evidence through activation steering: manipulating internal confidence signals correspondingly shifted abstention rates. Finally, Phase 4 demonstrated that models can systematically vary abstention policies based on instructed thresholds.Our findings indicate that abstention arises from the joint operation of internal confidence representations and threshold-based policies, mirroring the two-stage metacognitive control found in biological systems. This capacity is essential as LLMs transition into autonomous agents that must recognize their own uncertainty to decide when to act or seek help.

### 🤖 AI 总结

**一句话总结**：论文通过四阶段“可弃答(Abstention)”范式与激活操控实验证明：语言模型会利用内部置信度信号并结合阈值策略来决定回答或弃答。

**研究动机**：虽然可以从LLM输出中提取“置信度”，但模型是否会像生物元认知那样主动使用内部置信度来调节行为（例如不确定时选择弃答）仍不清楚；这对自主智能体的安全决策与求助机制尤为关键。

**核心方法**：作者设计四阶段实验：先在无弃答选项下建立内部置信度估计，再观察模型在可弃答条件下是否对置信度施加隐式阈值；随后用activation steering直接操控内部置信度表征以测试因果性，并最后通过指令化阈值让模型系统性改变弃答策略。

**主要结论**：置信度是预测“回答/弃答”行为的最强因素，其影响远大于RAG可达性分数或表层语义特征；更重要的是，操控置信度表征会因果性改变弃答率，表明LLM存在“置信度表征+阈值策略”的两阶段元认知控制机制。

**关键词**：元认知, 置信度估计, 不确定性感知, 拒答机制, 拒答阈值策略, 激活引导, 因果验证, 内部表征操控, LLM行为调控, RAG可达性对比

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22161v1) | [下载PDF](https://arxiv.org/pdf/2603.22161v1.pdf)

---

## [29. Multimodal Survival Analysis with Locally Deployable Large Language Models](https://arxiv.org/abs/2603.22158v1)

**作者**：Moritz Gögl, Christopher Yau  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-23

### 📄 论文摘要

We study multimodal survival analysis integrating clinical text, tabular covariates, and genomic profiles using locally deployable large language models (LLMs). As many institutions face tight computational and privacy constraints, this setting motivates the use of lightweight, on-premises models. Our approach jointly estimates calibrated survival probabilities and generates concise, evidence-grounded prognosis text via teacher-student distillation and principled multimodal fusion. On a TCGA cohort, it outperforms standard baselines, avoids reliance on cloud services and associated privacy concerns, and reduces the risk of hallucinated or miscalibrated estimates that can be observed in base LLMs.

### 🤖 AI 总结

**一句话总结**：提出一种可本地部署的轻量级LLM多模态生存分析框架，融合临床文本、表格变量与基因组信息，同时输出校准的生存概率与有依据的预后解释，并在TCGA上优于基线。

**研究动机**：许多医疗机构受算力与隐私约束，难以依赖云端大模型进行生存分析与临床文本推理；同时基础LLM可能产生幻觉或不校准的风险预测，影响临床可用性与安全性。

**核心方法**：采用教师-学生蒸馏将能力迁移到可本地部署的小模型，并通过原则化的多模态融合联合建模文本、表格与基因组特征；模型同时学习生存概率的校准估计与生成简洁、证据支撑的预后文本说明。

**主要结论**：在TCGA队列上该方法相较标准基线表现更好，并能在不依赖云服务的情况下缓解隐私风险；同时降低了大模型常见的幻觉与风险估计失准问题，提升预测与解释的可靠性。

**关键词**：多模态生存分析, 本地部署 LLM, 临床预后生成, 生存概率校准, 证据对齐生成, 教师-学生蒸馏, 多模态融合, 临床文本建模, 基因组特征融合, 隐私保护推理, 幻觉抑制

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22158v1) | [下载PDF](https://arxiv.org/pdf/2603.22158v1.pdf)

---

## [30. dynActivation: A Trainable Activation Family for Adaptive Nonlinearity](https://arxiv.org/abs/2603.22154v1)

**作者**：Alois Bachmann  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-03-23

### 📄 论文摘要

This paper proposes $\mathrm{dynActivation}$, a per-layer trainable activation defined as $f_i(x) = \mathrm{BaseAct}(x)(α_i - β_i) + β_i x$, where $α_i$ and $β_i$ are lightweight learned scalars that interpolate between the base nonlinearity and a linear path and $\mathrm{BaseAct}(x)$ resembles any ReLU-like function. The static and dynamic ReLU-like variants are then compared across multiple vision tasks, language modeling tasks, and ablation studies. The results suggest that dynActivation variants tend to linearize deep layers while maintaining high performance, which can improve training efficiency by up to $+54\%$ over ReLU.   On CIFAR-10, dynActivation(Mish) improves over static Mish by up to $+14.02\%$ on AttentionCNN with an average improvment by $+6.00\%$, with a $24\%$ convergence-AUC reduction relative to Mish (2120 vs. 2785). In a 1-to-75-layer MNIST depth-scaling study, dynActivation never drops below $95\%$ test accuracy ($95.3$--$99.3\%$), while ReLU collapses below $80\%$ at 25 layers. Under FGSM at $\varepsilon{=}0.08$, dynActivation(Mish) incurs a $55.39\%$ accuracy drop versus $62.79\%$ for ReLU ($7.40\%$ advantage). Transferred to language modeling, a new proposed dynActGLU-variant achieves a $10.3\%$ relative perplexity reduction over SwiGLU at 5620 steps (4.047 vs. 4.514), though the gap vanishes at 34300 steps.

### 🤖 AI 总结

**一句话总结**：提出一种按层可训练的激活函数族dynActivation，用少量可学习标量在“基激活非线性”和“线性通路”之间自适应插值，从而在多任务上提升收敛效率并保持/提升性能。

**研究动机**：固定形状的ReLU类激活在不同网络深度与任务中可能并非最优，深层网络尤其容易因非线性过强或梯度问题导致训练不稳或性能塌陷。作者希望让每一层的非线性强度可学习，以在表达能力与可优化性之间自适应折中并加速训练。

**核心方法**：定义按层激活$f_i(x)=\mathrm{BaseAct}(x)(\alpha_i-\beta_i)+\beta_i x$，其中$\alpha_i,\beta_i$为轻量标量参数，使输出在“任意ReLU-like基激活”与“线性映射”之间连续插值。并给出静态/动态ReLU-like变体及在视觉、语言建模（含dynActGLU变体）上的对比与消融实验。

**主要结论**：实验显示dynActivation往往使深层更趋线性但不损性能，整体可带来显著训练效率提升（最高约+54%）且在多基激活（如Mish）与多任务上取得更好或相当结果。其在深度扩展与对抗扰动下表现更稳健；在语言建模中可早期降低困惑度但长期差距可能缩小。

**关键词**：可训练激活函数, 自适应非线性, 逐层参数化, 线性插值激活, 深层网络线性化, 训练效率提升, 视觉任务评测, 语言模型困惑度, 深度可扩展性

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.22154v1) | [下载PDF](https://arxiv.org/pdf/2603.22154v1.pdf)

---

