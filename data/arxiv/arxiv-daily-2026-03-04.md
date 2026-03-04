# arXiv AI 论文日报 | 2026-03-04

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (10 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.AI](#csAI) (7 篇)
- [cs.CL](#csCL) (3 篇)

---

## cs.AI

## [1. Inherited Goal Drift: Contextual Pressure Can Undermine Agentic Goals](https://arxiv.org/abs/2603.03258v1)

**作者**：Achyutha Menon, Magnus Saebo, Tyler Crosse 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-03-03

### 📄 论文摘要

The accelerating adoption of language models (LMs) as agents for deployment in long-context tasks motivates a thorough understanding of goal drift: agents' tendency to deviate from an original objective. While prior-generation language model agents have been shown to be susceptible to drift, the extent to which drift affects more recent models remains unclear. In this work, we provide an updated characterization of the extent and causes of goal drift. We investigate drift in state-of-the-art models within a simulated stock-trading environment (Arike et al., 2025). These models are largely shown to be robust even when subjected to adversarial pressure. We show, however, that this robustness is brittle: across multiple settings, the same models often inherit drift when conditioned on prefilled trajectories from weaker agents. The extent of conditioning-induced drift varies significantly by model family, with only GPT-5.1 maintaining consistent resilience among tested models. We find that drift behavior is inconsistent between prompt variations and correlates poorly with instruction hierarchy following behavior, with strong hierarchy following failing to reliably predict resistance to drift. Finally, we run analogous experiments in a new emergency room triage environment to show preliminary evidence for the transferability of our results across qualitatively different settings. Our findings underscore the continued vulnerability of modern LM agents to contextual pressures and the need for refined post-training techniques to mitigate this.

### 🤖 AI 总结

**一句话总结**：最新LM代理在直接对抗压力下大多不易偏离目标，但一旦被“较弱代理的预填轨迹/上下文”条件化，往往会继承并放大目标漂移（goal drift）。

**研究动机**：随着LM以长上下文代理形态被部署，必须弄清它们在复杂情境中是否会偏离原始目标及其成因，尤其是新一代模型是否仍存在脆弱点。

**核心方法**：在模拟股票交易环境中系统测试多种SOTA模型的目标漂移：对比对抗压力下的稳健性与“预填弱代理轨迹”条件化后的继承性漂移，并分析与提示变体、指令层级遵循的相关性；再在急诊分诊环境复现实验以检验可迁移性。

**主要结论**：模型的抗漂移稳健性呈“脆而不稳”：对抗压力下看似稳健，但对来自弱代理的上下文轨迹高度敏感且家族差异显著，仅GPT-5.1保持较一致韧性；漂移对提示变体不稳定，且与指令层级遵循相关性弱，提示需要更精细的后训练方法来缓解上下文压力导致的漂移。

**关键词**：目标漂移, 上下文压力, 长上下文智能体, 条件诱导漂移, 轨迹预填充, 鲁棒性评测, 脆弱鲁棒性, 指令层级遵循, 后训练对齐, 模拟股票交易环境, 急诊分诊环境

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03258v1) | [下载PDF](https://arxiv.org/pdf/2603.03258v1.pdf)

---

## [2. Density-Guided Response Optimization: Community-Grounded Alignment via Implicit Acceptance Signals](https://arxiv.org/abs/2603.03242v1)

**作者**：Patrick Gerard, Svitlana Volkova  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-03-03

### 📄 论文摘要

Language models deployed in online communities must adapt to norms that vary across social, cultural, and domain-specific contexts. Prior alignment approaches rely on explicit preference supervision or predefined principles, which are effective for well-resourced settings but exclude most online communities -- particularly those without institutional backing, annotation infrastructure, or organized around sensitive topics -- where preference elicitation is costly, ethically fraught, or culturally misaligned.   We observe that communities already express preferences implicitly through what content they accept, engage with, and allow to persist. We show that this acceptance behavior induces measurable geometric structure in representation space: accepted responses occupy coherent, high-density regions that reflect community-specific norms, while rejected content falls in sparser or misaligned areas. We operationalize this structure as an implicit preference signal for alignment and introduce density-guided response optimization (DGRO), a method that aligns language models to community norms without requiring explicit preference labels.   Using labeled preference data, we demonstrate that local density recovers pairwise community judgments, indicating that geometric structure encodes meaningful preference signal. We then apply DGRO in annotation-scarce settings across diverse communities spanning platform, topic, and language. DGRO-aligned models consistently produce responses preferred by human annotators, domain experts, and model-based judges over supervised and prompt-based baselines. We position DGRO as a practical alignment alternative for communities where explicit preference supervision is unavailable or misaligned with situated practices, and discuss the implications and risks of learning from emergent acceptance behavior.

### 🤖 AI 总结

**一句话总结**：提出DGRO：利用社区“隐式接受/留存”行为在表示空间形成的高密度区域作为偏好信号，实现无需显式偏好标注的社区对齐。

**研究动机**：许多线上社区缺乏显式偏好数据与标注基础设施，且在敏感/文化差异场景下显式偏好征询成本高、风险大、可能不适配。作者认为社区已通过互动、点赞、留存等“接受行为”隐式表达规范，可用于对齐。

**核心方法**：观察到被接受的回复在表示空间中聚成一致的高密度区域，而被拒内容更稀疏/偏离；将“局部密度”作为隐式偏好指标。DGRO据此优化模型生成，使输出更靠近社区接受的高密度区域，并在有标注数据上验证密度可恢复成对偏好判断，在低标注社区中进行对齐实验。

**主要结论**：局部密度确实编码了社区偏好信号，能在一定程度上替代显式偏好监督。DGRO在多平台、多主题、多语言、标注稀缺场景下生成的回复更受人类/专家/模型评审偏好，整体优于监督与纯提示基线，同时作者讨论了从“涌现接受行为”学习的风险与影响。

**关键词**：社区规范对齐, 隐式偏好信号, 内容接受行为, 密度引导响应优化（DGRO）, 表示空间几何结构, 局部密度估计, 偏好学习, 无标注对齐, 稀缺标注场景, 跨社区泛化, 人类偏好评测

**评分**：49

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03242v1) | [下载PDF](https://arxiv.org/pdf/2603.03242v1.pdf)

---

## [3. AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework](https://arxiv.org/abs/2603.03233v1)

**作者**：Zihang Zeng, Jiaquan Zhang, Pengze Li 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-03-03

### 📄 论文摘要

Large Language Models (LLMs) demonstrate potentials for automating scientific code generation but face challenges in reliability, error propagation in multi-agent workflows, and evaluation in domains with ill-defined success metrics. We present a Bayesian adversarial multi-agent framework specifically designed for AI for Science (AI4S) tasks in the form of a Low-code Platform (LCP). Three LLM-based agents are coordinated under the Bayesian framework: a Task Manager that structures user inputs into actionable plans and adaptive test cases, a Code Generator that produces candidate solutions, and an Evaluator providing comprehensive feedback. The framework employs an adversarial loop where the Task Manager iteratively refines test cases to challenge the Code Generator, while prompt distributions are dynamically updated using Bayesian principles by integrating code quality metrics: functional correctness, structural alignment, and static analysis. This co-optimization of tests and code reduces dependence on LLM reliability and addresses evaluation uncertainty inherent to scientific tasks. LCP also streamlines human-AI collaboration by translating non-expert prompts into domain-specific requirements, bypassing the need for manual prompt engineering by practitioners without coding backgrounds. Benchmark evaluations demonstrate LCP's effectiveness in generating robust code while minimizing error propagation. The proposed platform is also tested on an Earth Science cross-disciplinary task and demonstrates strong reliability, outperforming competing models.

### 🤖 AI 总结

**一句话总结**：提出一个面向AI4S的低代码平台，用贝叶斯对抗式多智能体（任务管理/代码生成/评估）协同迭代测试与代码，以提升科学代码生成的可靠性。

**研究动机**：LLM用于科学代码生成时容易出现不可靠与多智能体流程中的错误传播，且科学任务常缺乏明确成功指标导致评估困难。平台还需降低非编程科学用户的提示工程与需求表达门槛。

**核心方法**：在贝叶斯框架下协调三类LLM代理：Task Manager将用户输入转为计划与自适应测试并在对抗循环中持续强化测试来“刁难”代码，Code Generator产出候选方案，Evaluator基于功能正确性、结构对齐与静态分析给出反馈。通过将这些质量指标做贝叶斯更新来动态调整提示分布，实现测试与代码的联合优化并抑制误差传播。

**主要结论**：基准实验显示该低代码平台能生成更鲁棒的代码并减少多代理链路中的错误累积；在地球科学跨学科任务上也表现出更强可靠性，整体优于对比模型。

**关键词**：科学代码生成, AI4S 任务, 低代码开发, 贝叶斯优化, 多智能体误差传播, 代码质量评测, 静态分析, 功能正确性评估, 地球科学基准测试

**评分**：50

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03233v1) | [下载PDF](https://arxiv.org/pdf/2603.03233v1.pdf)

---

## [4. NeuroSkill(tm): Proactive Real-Time Agentic System Capable of Modeling Human State of Mind](https://arxiv.org/abs/2603.03212v1)

**作者**：Nataliya Kosmyna, Eugene Hauptmann  
**分类**：cs.AI  
**发布时间**：2026-03-03

### 📄 论文摘要

Real-time proactive agentic system, capable of modeling Human State of Mind, using foundation EXG model and text embeddings model, running fully offline on the edge. Unlike all previously known systems, the NeuroSkill(tm) system leverages SKILL.md description of Human's State of Mind via API and CLI provided by the system, directly from the Brain-Computer Interface (BCI) devices, which records Human biophysical and brain signals. Our custom harness - NeuroLoop(tm) - utilizes all of the above to run agentic flow that manages to engage with the Human on multiple cognitive and affective levels of their State of Mind (e.g., empathy), by providing actionable tool calls and protocol execution with explicit or implicit requests from the Human. GPLv3 open-source software with ethically aligned AI100 licensing for the skill markdown.

### 🤖 AI 总结

**一句话总结**：NeuroSkill(tm) 提出一个可离线在边缘端实时运行的主动式智能体系统，通过BCI采集的生理/脑信号来建模人的心智状态，并据此执行工具调用与协议以进行多层次交互。

**研究动机**：现有交互式智能体多依赖在线服务与文本输入，难以在真实场景中实时、主动地理解人的认知与情感状态。作者希望利用BCI等生物信号在本地推断“心智状态”，让系统能更及时地提供同理与行动建议。

**核心方法**：系统以“基础EXG模型+文本嵌入模型”在边缘端离线推理，并用SKILL.md将“心智状态”以可编程的技能描述暴露为API/CLI接口。自定义执行框架NeuroLoop(tm)将状态建模结果接入agentic flow，面向显式或隐式请求触发工具调用与协议执行以实现主动交互。

**主要结论**：论文宣称该系统相较以往方案能直接从BCI信号驱动、以技能化接口表达人类心智状态，并在本地实时运行以支持更具同理与行动性的交互。摘要未提供定量实验、对比评测或消融结果，因此结论主要为系统能力与设计主张层面的描述。

**关键词**：实时主动式智能体, 心智状态建模, 脑机接口（BCI）, 生理信号建模（EXG）, 边缘离线推理, 基础模型, 文本嵌入, 认知-情感交互, 技能描述规范（Markdown）

**评分**：54

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03212v1) | [下载PDF](https://arxiv.org/pdf/2603.03212v1.pdf)

---

## [5. No Memorization, No Detection: Output Distribution-Based Contamination Detection in Small Language Models](https://arxiv.org/abs/2603.03203v1)

**作者**：Omer Sela  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-03-03

### 📄 论文摘要

CDD, or Contamination Detection via output Distribution, identifies data contamination by measuring the peakedness of a model's sampled outputs. We study the conditions under which this approach succeeds and fails on small language models ranging from 70M to 410M parameters. Using controlled contamination experiments on GSM8K, HumanEval, and MATH, we find that CDD's effectiveness depends critically on whether fine-tuning produces verbatim memorization. With low-rank adaptation, models can learn from contaminated data without memorizing it, and CDD performs at chance level even when the data is verifiably contaminated. Only when fine-tuning capacity is sufficient to induce memorization does CDD recover strong detection accuracy. Our results characterize a memorization threshold that governs detectability and highlight a practical consideration: parameter-efficient fine-tuning can produce contamination that output-distribution methods do not detect. Our code is available at https://github.com/Sela-Omer/Contamination-Detection-Small-LM

### 🤖 AI 总结

**一句话总结**：论文指出：基于输出分布峰度的污染检测（CDD）只有在微调引发逐字记忆（verbatim memorization）时才有效，否则在小模型上会退化为随机猜测。

**研究动机**：现有输出分布法被用于检测训练数据污染，但其在小参数语言模型与参数高效微调（如LoRA）场景下是否可靠尚不清楚。作者希望厘清CDD成功/失败的条件，并给出可操作的判别边界。

**核心方法**：在70M-410M小模型上，对GSM8K、HumanEval、MATH进行可控“污染”微调实验，比较不同微调容量/方式（含低秩适配）下CDD基于采样输出“峰度”的检测表现，并分析其与逐字记忆之间的关系。

**主要结论**：CDD的检测能力由“记忆阈值”主导：当微调容量足以造成逐字记忆时检测准确率显著提升；而LoRA等参数高效微调可在不逐字记忆的情况下学习被污染数据，导致CDD接近随机水平，从而提示该类方法可能漏检实际污染。

**关键词**：数据污染检测, 输出分布检测, 峰度指标, 小语言模型, 微调容量, 逐字记忆, 记忆阈值, 参数高效微调, 受控污染实验

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03203v1) | [下载PDF](https://arxiv.org/pdf/2603.03203v1.pdf)

---

## [6. Expectation and Acoustic Neural Network Representations Enhance Music Identification from Brain Activity](https://arxiv.org/abs/2603.03190v1)

**作者**：Shogo Noguchi, Taketo Akama, Tai Nakamura 等 5 位作者  
**分类**：cs.AI, q-bio.NC  
**发布时间**：2026-03-03

### 📄 论文摘要

During music listening, cortical activity encodes both acoustic and expectation-related information. Prior work has shown that ANN representations resemble cortical representations and can serve as supervisory signals for EEG recognition. Here we show that distinguishing acoustic and expectation-related ANN representations as teacher targets improves EEG-based music identification. Models pretrained to predict either representation outperform non-pretrained baselines, and combining them yields complementary gains that exceed strong seed ensembles formed by varying random initializations. These findings show that teacher representation type shapes downstream performance and that representation learning can be guided by neural encoding. This work points toward advances in predictive music cognition and neural decoding. Our expectation representation, computed directly from raw signals without manual labels, reflects predictive structure beyond onset or pitch, enabling investigation of multilayer predictive encoding across diverse stimuli. Its scalability to large, diverse datasets further suggests potential for developing general-purpose EEG models grounded in cortical encoding principles.

### 🤖 AI 总结

**一句话总结**：将声学与“期望（预测）”两类ANN教师表征区分开来做预训练目标，可显著提升基于EEG的音乐识别，并且两者结合带来互补增益。

**研究动机**：听音乐时大脑皮层同时编码声学信息与基于预测/期望的信息，但以往多用单一ANN表征做监督，可能混淆两类信号而限制EEG解码性能。

**核心方法**：构建两种ANN教师目标（声学表征与从原始音频直接计算、无需人工标签的期望表征），分别预训练EEG模型去预测对应表征；再将两类预训练模型进行组合以利用互补信息，并与未预训练基线及随机种子集成作对比。

**主要结论**：分别以声学或期望表征作教师信号的预训练均优于无预训练基线；二者组合的提升超过仅靠不同随机初始化的强集成，表明教师表征类型会系统性影响下游EEG音乐识别效果，且期望表征能捕捉超越起音/音高的可扩展预测结构。

**关键词**：脑电解码, 音乐识别, 皮层神经编码, 声学表征, 期望表征, 教师-学生学习, 监督信号迁移, 表征预训练, 预测编码, 自监督学习

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03190v1) | [下载PDF](https://arxiv.org/pdf/2603.03190v1.pdf)

---

## [7. Neuro-Symbolic Artificial Intelligence: A Task-Directed Survey in the Black-Box Models Era](https://arxiv.org/abs/2603.03177v1)

**作者**：Giovanni Pio Delvecchio, Lorenzo Molfetta, Gianluca Moro  
**分类**：cs.AI  
**发布时间**：2026-03-03

### 📄 论文摘要

The integration of symbolic computing with neural networks has intrigued researchers since the first theorizations of Artificial intelligence (AI). The ability of Neuro-Symbolic (NeSy) methods to infer or exploit behavioral schema has been widely considered as one of the possible proxies for human-level intelligence. However, the limited semantic generalizability and the challenges in declining complex domains with pre-defined patterns and rules hinder their practical implementation in real-world scenarios. The unprecedented results achieved by connectionist systems since the last AI breakthrough in 2017 have raised questions about the competitiveness of NeSy solutions, with particular emphasis on the Natural Language Processing and Computer Vision fields. This survey examines task-specific advancements in the NeSy domain to explore how incorporating symbolic systems can enhance explainability and reasoning capabilities. Our findings are meant to serve as a resource for researchers exploring explainable NeSy methodologies for real-life tasks and applications. Reproducibility details and in-depth comments on each surveyed research work are made available at https://github.com/disi-unibo-nlp/task-oriented-neuro-symbolic.git.

### 🤖 AI 总结

**一句话总结**：这是一篇面向具体任务的神经符号AI综述，梳理在黑箱深度模型时代如何通过引入符号系统提升模型的可解释性与推理能力。

**研究动机**：纯神经网络虽在NLP与CV等领域表现强劲，但常缺乏可解释推理；而传统神经符号方法又受限于语义泛化不足与复杂领域规则难以预定义，促使作者系统盘点任务导向的NeSy进展与可落地性。

**核心方法**：以“任务”为主线综述NeSy研究，比较不同任务中神经与符号结合的设计与收益，强调其在解释、推理与行为模式利用上的作用，并提供可复现资源与逐篇评论的配套仓库。

**主要结论**：作者认为在真实任务中适当融入符号计算能补足黑箱模型在解释与推理方面的短板，但NeSy在复杂开放域仍面临泛化与规则建模难题；该综述与仓库旨在为研究者提供系统参考与复现入口。

**关键词**：神经符号方法, 符号推理, 可解释性, 任务导向综述, 黑箱模型, 语义泛化, 行为模式归纳, 自然语言处理, 计算机视觉, 可复现性

**评分**：10

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03177v1) | [下载PDF](https://arxiv.org/pdf/2603.03177v1.pdf)

---

## cs.CL

## [8. Using Learning Progressions to Guide AI Feedback for Science Learning](https://arxiv.org/abs/2603.03249v1)

**作者**：Xin Xia, Nejla Yuruk, Yun Wang 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-03

### 📄 论文摘要

Generative artificial intelligence (AI) offers scalable support for formative feedback, yet most AI-generated feedback relies on task-specific rubrics authored by domain experts. While effective, rubric authoring is time-consuming and limits scalability across instructional contexts. Learning progressions (LP) provide a theoretically grounded representation of students' developing understanding and may offer an alternative solution. This study examines whether an LP-driven rubric generation pipeline can produce AI-generated feedback comparable in quality to feedback guided by expert-authored task rubrics. We analyzed AI-generated feedback for written scientific explanations produced by 207 middle school students in a chemistry task. Two pipelines were compared: (a) feedback guided by a human expert-designed, task-specific rubric, and (b) feedback guided by a task-specific rubric automatically derived from a learning progression prior to grading and feedback generation. Two human coders evaluated feedback quality using a multi-dimensional rubric assessing Clarity, Accuracy, Relevance, Engagement and Motivation, and Reflectiveness (10 sub-dimensions). Inter-rater reliability was high, with percent agreement ranging from 89% to 100% and Cohen's kappa values for estimable dimensions (kappa = .66 to .88). Paired t-tests revealed no statistically significant differences between the two pipelines for Clarity (t1 = 0.00, p1 = 1.000; t2 = 0.84, p2 = .399), Relevance (t1 = 0.28, p1 = .782; t2 = -0.58, p2 = .565), Engagement and Motivation (t1 = 0.50, p1 = .618; t2 = -0.58, p2 = .565), or Reflectiveness (t = -0.45, p = .656). These findings suggest that the LP-driven rubric pipeline can serve as an alternative solution.

### 🤖 AI 总结

**一句话总结**：用学习进阶（LP）自动生成任务rubric来驱动生成式AI反馈，其反馈质量与专家手写rubric驱动的反馈相当。

**研究动机**：现有AI形成性反馈常依赖专家为每个任务编写rubric，成本高且难以跨情境扩展；LP作为学生理解发展的理论框架，可能替代人工rubric以提升可扩展性。

**核心方法**：在一项面向207名初中生化学书面解释的任务中，对比两条反馈生成流水线：专家任务rubric驱动 vs 基于LP自动派生的任务rubric驱动；由两位编码员用包含清晰度、准确性、相关性、动机与参与、反思性等10个子维度的量表评估，并用配对t检验比较差异。

**主要结论**：两条流水线在清晰度、相关性、动机与参与、反思性等维度上均无显著差异，且评分一致性较高，表明LP驱动的自动rubric生成可作为专家rubric的可扩展替代方案。

**关键词**：形成性反馈, 自动化评分, 反馈生成, 评分量规, 量规生成, 学习进阶（LP）, 学习进阶驱动量规, 科学解释写作, 科学教育评测, 反馈质量评估

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03249v1) | [下载PDF](https://arxiv.org/pdf/2603.03249v1.pdf)

---

## [9. Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use](https://arxiv.org/abs/2603.03205v1)

**作者**：Aradhye Agarwal, Gurdit Siyan, Yash Pandya 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-03

### 📄 论文摘要

Agentic language models operate in a fundamentally different safety regime than chat models: they must plan, call tools, and execute long-horizon actions where a single misstep, such as accessing files or entering credentials, can cause irreversible harm. Existing alignment methods, largely optimized for static generation and task completion, break down in these settings due to sequential decision-making, adversarial tool feedback, and overconfident intermediate reasoning. We introduce MOSAIC, a post-training framework that aligns agents for safe multi-step tool use by making safety decisions explicit and learnable. MOSAIC structures inference as a plan, check, then act or refuse loop, with explicit safety reasoning and refusal as first-class actions. To train without trajectory-level labels, we use preference-based reinforcement learning with pairwise trajectory comparisons, which captures safety distinctions often missed by scalar rewards. We evaluate MOSAIC zero-shot across three model families, Qwen2.5-7B, Qwen3-4B-Thinking, and Phi-4, and across out-of-distribution benchmarks spanning harmful tasks, prompt injection, benign tool use, and cross-domain privacy leakage. MOSAIC reduces harmful behavior by up to 50%, increases harmful-task refusal by over 20% on injection attacks, cuts privacy leakage, and preserves or improves benign task performance, demonstrating robust generalization across models, domains, and agentic settings.

### 🤖 AI 总结

**一句话总结**：MOSAIC 通过“规划-安全检查-执行/拒绝”的显式决策循环与偏好强化学习后训练，让具备多步工具调用能力的智能体模型更安全且不明显牺牲可用性。

**研究动机**：智能体模型需要在长链路、多次工具交互中做序列决策，一次错误动作就可能造成不可逆伤害，而现有面向静态生成的对齐方法在对抗性工具反馈、过度自信中间推理等情境下失效。

**核心方法**：提出 MOSAIC 后训练框架：将推理过程结构化为 plan→check→act/refuse，并把安全推理与“拒绝”作为可学习的一等动作；训练时不依赖逐步轨迹标注，而用基于偏好的强化学习进行成对轨迹比较来学习安全差异。

**主要结论**：在 Qwen2.5-7B、Qwen3-4B-Thinking、Phi-4 上零样本评测显示，MOSAIC 可将有害行为最多降低约 50%，在注入攻击上提升有害任务拒绝率 20%+、减少隐私泄漏，同时保持或提升良性工具任务表现，具备较强跨模型与跨域泛化。

**关键词**：智能体模型安全, 长程行动规划, 安全拒答机制, 显式安全推理, 计划-检查-行动循环, 偏好强化学习, 轨迹成对比较, 提示注入防御, 隐私泄露防护, 分布外鲁棒性

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03205v1) | [下载PDF](https://arxiv.org/pdf/2603.03205v1.pdf)

---

## [10. BeyondSWE: Can Current Code Agent Survive Beyond Single-Repo Bug Fixing?](https://arxiv.org/abs/2603.03194v1)

**作者**：Guoxin Chen, Fanzhe Meng, Jiale Zhao 等 15 位作者  
**分类**：cs.CL, cs.SE  
**发布时间**：2026-03-03

### 📄 论文摘要

Current benchmarks for code agents primarily assess narrow, repository-specific fixes, overlooking critical real-world challenges such as cross-repository reasoning, domain-specialized problem solving, dependency-driven migration, and full-repository generation. To address this gap, we introduce BeyondSWE, a comprehensive benchmark that broadens existing evaluations along two axes - resolution scope and knowledge scope - using 500 real-world instances across four distinct settings. Experimental results reveal a significant capability gap: even frontier models plateau below 45% success, and no single model performs consistently across task types. To systematically investigate the role of external knowledge, we develop SearchSWE, a framework that integrates deep search with coding abilities. Our experiments show that search augmentation yields inconsistent gains and can in some cases degrade performance, highlighting the difficulty of emulating developer-like workflows that interleave search and reasoning during coding tasks. This work offers both a realistic, challenging evaluation benchmark and a flexible framework to advance research toward more capable code agents.

### 🤖 AI 总结

**一句话总结**：提出BeyondSWE基准以评测代码智能体在跨仓库与知识密集型真实任务中的能力，并发现现有前沿模型在该更真实设定下成功率仍明显不足且不稳定。

**研究动机**：现有代码智能体基准多聚焦单仓库bug修复，忽略跨仓库推理、领域知识问题、依赖迁移与全仓生成等真实开发挑战，导致评测与实际能力脱节。

**核心方法**：构建BeyondSWE：沿“解决范围（resolution scope）”与“知识范围（knowledge scope）”两轴扩展评测，覆盖四类场景共500个真实实例；并提出SearchSWE框架，将深度搜索与编码能力结合以研究外部知识检索的作用。

**主要结论**：实验显示能力鸿沟显著：即使最强模型成功率也在45%以下且不同任务类型间无一致优势；检索增强带来的收益不稳定，甚至可能降性能，说明将“搜索-推理-编码”交织的开发者式工作流自动化仍很困难。

**关键词**：代码智能体评测, 软件工程基准, 跨仓库推理, 领域知识编码, 依赖迁移, 全仓库生成, 搜索增强编程, 外部知识集成, 可靠性评估, 任务多样性

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03194v1) | [下载PDF](https://arxiv.org/pdf/2603.03194v1.pdf)

---

## cs.CV

## [11. Utonia: Toward One Encoder for All Point Clouds](https://arxiv.org/abs/2603.03283v1)

**作者**：Yujia Zhang, Xiaoyang Wu, Yunhan Yang 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-03

### 📄 论文摘要

We dream of a future where point clouds from all domains can come together to shape a single model that benefits them all. Toward this goal, we present Utonia, a first step toward training a single self-supervised point transformer encoder across diverse domains, spanning remote sensing, outdoor LiDAR, indoor RGB-D sequences, object-centric CAD models, and point clouds lifted from RGB-only videos. Despite their distinct sensing geometries, densities, and priors, Utonia learns a consistent representation space that transfers across domains. This unification improves perception capability while revealing intriguing emergent behaviors that arise only when domains are trained jointly. Beyond perception, we observe that Utonia representations can also benefit embodied and multimodal reasoning: conditioning vision-language-action policies on Utonia features improves robotic manipulation, and integrating them into vision-language models yields gains on spatial reasoning. We hope Utonia can serve as a step toward foundation models for sparse 3D data, and support downstream applications in AR/VR, robotics, and autonomous driving.

### 🤖 AI 总结

**一句话总结**：Utonia提出一个跨多种点云域统一训练的自监督Point Transformer编码器，学习可迁移的通用3D表示并提升感知与推理能力。

**研究动机**：不同来源点云（遥感/车载激光/室内RGB-D/CAD/视频重建）在几何、密度与先验上差异巨大，导致现有模型难以共享表示与跨域泛化。作者希望用“单一编码器”汇聚多域数据，迈向稀疏3D基础模型。

**核心方法**：训练一个自监督的Point Transformer编码器，在多域点云上联合学习，使其在同一表示空间中对齐不同域的特征分布并实现跨域迁移。进一步将Utonia特征作为条件输入，接入视觉-语言-动作策略与视觉-语言模型以验证其对具身控制与空间推理的增益。

**主要结论**：联合多域训练可获得一致且可迁移的点云表示，相比单域训练在感知任务上更强，并出现仅在多域联合时涌现的行为。该表示还能提升机器人操作与视觉语言空间推理表现，展示了面向AR/VR、机器人与自动驾驶的3D基础模型潜力。

**关键词**：点云基础模型, 自监督表征学习, 跨域点云预训练, 统一表征空间, 稀疏3D数据, 多源3D感知, 迁移学习, 视觉-语言-动作（VLA）, 机器人操作, 空间推理, 自动驾驶感知

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03283v1) | [下载PDF](https://arxiv.org/pdf/2603.03283v1.pdf)

---

## [12. CFG-Ctrl: Control-Based Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2603.03281v1)

**作者**：Hanyang Wang, Yiyang Liu, Jiawei Chi 等 6 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-03

### 📄 论文摘要

Classifier-Free Guidance (CFG) has emerged as a central approach for enhancing semantic alignment in flow-based diffusion models. In this paper, we explore a unified framework called CFG-Ctrl, which reinterprets CFG as a control applied to the first-order continuous-time generative flow, using the conditional-unconditional discrepancy as an error signal to adjust the velocity field. From this perspective, we summarize vanilla CFG as a proportional controller (P-control) with fixed gain, and typical follow-up variants develop extended control-law designs derived from it. However, existing methods mainly rely on linear control, inherently leading to instability, overshooting, and degraded semantic fidelity especially on large guidance scales. To address this, we introduce Sliding Mode Control CFG (SMC-CFG), which enforces the generative flow toward a rapidly convergent sliding manifold. Specifically, we define an exponential sliding mode surface over the semantic prediction error and introduce a switching control term to establish nonlinear feedback-guided correction. Moreover, we provide a Lyapunov stability analysis to theoretically support finite-time convergence. Experiments across text-to-image generation models including Stable Diffusion 3.5, Flux, and Qwen-Image demonstrate that SMC-CFG outperforms standard CFG in semantic alignment and enhances robustness across a wide range of guidance scales. Project Page: https://hanyang-21.github.io/CFG-Ctrl

### 🤖 AI 总结

**一句话总结**：提出CFG-Ctrl将CFG统一解释为生成流上的控制问题，并用滑模控制(SMC-CFG)替代线性增益式CFG以提升大guidance下的语义对齐与稳定性。

**研究动机**：现有CFG及其变体可视作线性控制（如固定增益P控制），在guidance scale较大时容易出现不稳定、过冲与语义保真下降。作者希望用更稳健的控制律来系统性改善CFG在不同尺度下的鲁棒性与对齐效果。

**核心方法**：将条件-无条件预测差作为“误差信号”来修正连续时间一阶生成流的速度场，构建统一的CFG-Ctrl框架；进一步提出SMC-CFG：定义指数滑模面并加入切换控制项形成非线性反馈校正，并用Lyapunov分析证明有限时间收敛。

**主要结论**：在Stable Diffusion 3.5、Flux、Qwen-Image等文本到图像模型上，SMC-CFG相较标准CFG在语义对齐上更优，并在更宽的guidance scale范围内表现出更强的稳定性与鲁棒性。

**关键词**：无分类器引导（CFG）, 扩散模型引导, 连续时间生成流, 控制理论引导, 比例控制（P-control）, 滑模控制（SMC）, 非线性反馈控制, 李雅普诺夫稳定性分析, 有限时间收敛, 语义对齐, 引导尺度鲁棒性, 文本到图像生成

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03281v1) | [下载PDF](https://arxiv.org/pdf/2603.03281v1.pdf)

---

## [13. LoGeR: Long-Context Geometric Reconstruction with Hybrid Memory](https://arxiv.org/abs/2603.03269v1)

**作者**：Junyi Zhang, Charles Herrmann, Junhwa Hur 等 8 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-03

### 📄 论文摘要

Feedforward geometric foundation models achieve strong short-window reconstruction, yet scaling them to minutes-long videos is bottlenecked by quadratic attention complexity or limited effective memory in recurrent designs. We present LoGeR (Long-context Geometric Reconstruction), a novel architecture that scales dense 3D reconstruction to extremely long sequences without post-optimization. LoGeR processes video streams in chunks, leveraging strong bidirectional priors for high-fidelity intra-chunk reasoning. To manage the critical challenge of coherence across chunk boundaries, we propose a learning-based hybrid memory module. This dual-component system combines a parametric Test-Time Training (TTT) memory to anchor the global coordinate frame and prevent scale drift, alongside a non-parametric Sliding Window Attention (SWA) mechanism to preserve uncompressed context for high-precision adjacent alignment. Remarkably, this memory architecture enables LoGeR to be trained on sequences of 128 frames, and generalize up to thousands of frames during inference. Evaluated across standard benchmarks and a newly repurposed VBR dataset with sequences of up to 19k frames, LoGeR substantially outperforms prior state-of-the-art feedforward methods--reducing ATE on KITTI by over 74%--and achieves robust, globally consistent reconstruction over unprecedented horizons.

### 🤖 AI 总结

**一句话总结**：LoGeR 通过分块处理与混合记忆机制，将密集3D重建从短窗口扩展到超长视频序列，实现无需后优化的全局一致重建。

**研究动机**：现有前馈几何基础模型在短序列上效果好，但扩展到分钟级长视频会受限于注意力的二次复杂度或循环结构的有效记忆不足，导致跨段不一致与尺度漂移。

**核心方法**：模型将视频流按chunk处理，利用双向先验做高质量块内推理；为解决块间一致性，引入学习式混合记忆：参数化的测试时训练(TTT)记忆用于锚定全局坐标并抑制尺度漂移，非参数化的滑动窗口注意力(SWA)保留未压缩邻近上下文以实现精确对齐。

**主要结论**：LoGeR 可在训练仅128帧序列的情况下泛化到推理时上千乃至19k帧，显著优于先前前馈方法（如KITTI上ATE降低超74%），并在超长时域上保持鲁棒的全局一致重建。

**关键词**：长时序视频, 稠密三维重建, 长上下文建模, 分块处理, 混合记忆模块, 滑动窗口注意力（SWA）, 全局坐标系对齐, 尺度漂移抑制, 无后优化重建, 轨迹误差（ATE）评测

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03269v1) | [下载PDF](https://arxiv.org/pdf/2603.03269v1.pdf)

---

## [14. DuoMo: Dual Motion Diffusion for World-Space Human Reconstruction](https://arxiv.org/abs/2603.03265v1)

**作者**：Yufu Wang, Evonne Ng, Soyong Shin 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-03

### 📄 论文摘要

We present DuoMo, a generative method that recovers human motion in world-space coordinates from unconstrained videos with noisy or incomplete observations. Reconstructing such motion requires solving a fundamental trade-off: generalizing from diverse and noisy video inputs while maintaining global motion consistency. Our approach addresses this problem by factorizing motion learning into two diffusion models. The camera-space model first estimates motion from videos in camera coordinates. The world-space model then lifts this initial estimate into world coordinates and refines it to be globally consistent. Together, the two models can reconstruct motion across diverse scenes and trajectories, even from highly noisy or incomplete observations. Moreover, our formulation is general, generating the motion of mesh vertices directly and bypassing parametric models. DuoMo achieves state-of-the-art performance. On EMDB, our method obtains a 16% reduction in world-space reconstruction error while maintaining low foot skating. On RICH, it obtains a 30% reduction in world-space error. Project page: https://yufu-wang.github.io/duomo/

### 🤖 AI 总结

**一句话总结**：DuoMo通过“相机空间→世界空间”的双扩散模型分解学习，在噪声/缺失视频观测下仍能重建全局一致的世界坐标人体运动。

**研究动机**：从非受控视频恢复世界空间人体运动时，既要适应多样且噪声很大的输入，又要保证全局轨迹与接触（如脚步）一致性，这两者往往相互制约。

**核心方法**：方法将运动生成拆成两个扩散模型：先在相机坐标系中从视频估计初始运动，再用世界空间扩散模型将其抬升并全局一致性细化；同时直接生成网格顶点运动，绕过参数化人体模型的限制。

**主要结论**：DuoMo在EMDB与RICH上取得SOTA世界空间重建误差（分别降低约16%与30%），并能在保持较低脚滑的同时对严重噪声或不完整观测具有鲁棒性。

**关键词**：世界坐标人体运动重建, 无约束视频人体运动估计, 运动扩散模型, 双阶段扩散, 相机坐标到世界坐标提升, 全局运动一致性, 噪声与缺失观测鲁棒重建, 网格顶点运动生成, 非参数人体模型, 脚滑抑制

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03265v1) | [下载PDF](https://arxiv.org/pdf/2603.03265v1.pdf)

---

## [15. UniG2U-Bench: Do Unified Models Advance Multimodal Understanding?](https://arxiv.org/abs/2603.03241v1)

**作者**：Zimo Wen, Boxiu Li, Wanbo Zhang 等 14 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-03

### 📄 论文摘要

Unified multimodal models have recently demonstrated strong generative capabilities, yet whether and when generation improves understanding remains unclear. Existing benchmarks lack a systematic exploration of the specific tasks where generation facilitates understanding. To this end, we introduce UniG2U-Bench, a comprehensive benchmark categorizing generation-to-understanding (G2U) evaluation into 7 regimes and 30 subtasks, requiring varying degrees of implicit or explicit visual transformations. Extensive evaluation of over 30 models reveals three core findings: 1) Unified models generally underperform their base Vision-Language Models (VLMs), and Generate-then-Answer (GtA) inference typically degrades performance relative to direct inference. 2) Consistent enhancements emerge in spatial intelligence, visual illusions, or multi-round reasoning subtasks, where enhanced spatial and shape perception, as well as multi-step intermediate image states, prove beneficial. 3) Tasks with similar reasoning structures and models sharing architectures exhibit correlated behaviors, suggesting that generation-understanding coupling induces class-consistent inductive biases over tasks, pretraining data, and model architectures. These findings highlight the necessity for more diverse training data and novel paradigms to fully unlock the potential of unified multimodal modeling.

### 🤖 AI 总结

**一句话总结**：提出UniG2U-Bench系统评测“生成是否促进理解”，发现统一多模态模型整体不如其基础VLM且GtA常降分，但在空间/错觉/多轮推理等任务上生成带来稳定收益。

**研究动机**：现有统一多模态模型生成能力强，但“何时生成能提升理解”缺乏清晰结论与系统基准；现有评测也未细分不同类型任务中G2U的作用机制。

**核心方法**：构建UniG2U-Bench，将Generation-to-Understanding评估划分为7种范式、30个子任务，覆盖不同程度的隐式/显式视觉变换需求；对30+模型进行对比，并评估直接推理与Generate-then-Answer两种推理方式的差异与跨任务相关性。

**主要结论**：统一模型通常弱于其基础VLM，且GtA推理多半会退化性能；但在空间智能、视觉错觉和多轮推理等子任务中，生成的中间图像状态/更强形状与空间感知能带来一致提升；同时相似推理结构与共享架构的模型在任务表现上呈相关，提示G2U耦合引入了类一致的归纳偏置，需更丰富数据与新训练范式释放潜力。

**关键词**：统一多模态模型, 多模态评测基准, 生成后作答（GtA）推理, 视觉-语言模型（VLM）, 空间智能, 视觉错觉, 多轮推理, 视觉变换, 中间图像状态, 归纳偏置

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03241v1) | [下载PDF](https://arxiv.org/pdf/2603.03241v1.pdf)

---

## [16. COP-GEN: Latent Diffusion Transformer for Copernicus Earth Observation Data -- Generation Stochastic by Design](https://arxiv.org/abs/2603.03239v1)

**作者**：Miguel Espinosa, Eva Gmelich Meijling, Valerio Marsocci 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-03

### 📄 论文摘要

Earth observation applications increasingly rely on data from multiple sensors, including optical, radar, elevation, and land-cover products. Relationships between these modalities are fundamental for data integration but are inherently non-injective: identical conditioning information can correspond to multiple physically plausible observations. Thus, such conditional mappings should be parametrised as data distributions. As a result, deterministic models tend to collapse toward conditional means and fail to represent the uncertainty and variability required for tasks such as data completion and cross-sensor translation. We introduce COP-GEN, a multimodal latent diffusion transformer that models the joint distribution of heterogeneous Earth Observation modalities at their native spatial resolutions. By parameterising cross-modal mappings as conditional distributions, COP-GEN enables flexible any-to-any conditional generation, including zero-shot modality translation, spectral band infilling, and generation under partial or missing inputs, without task-specific retraining. Experiments on a large-scale global multimodal dataset show that COP-GEN generates diverse yet physically consistent realisations while maintaining strong peak fidelity across optical, radar, and elevation modalities. Qualitative and quantitative analyses demonstrate that the model captures meaningful cross-modal structure and systematically adapts its output uncertainty as conditioning information increases. These results highlight the practical importance of stochastic generative modeling for Earth observation and motivate evaluation protocols that move beyond single-reference, pointwise metrics. Website: https:// miquel-espinosa.github.io/cop-gen

### 🤖 AI 总结

**一句话总结**：COP-GEN 是一种面向地球观测多模态数据的潜变量扩散Transformer，通过显式建模条件分布实现任意模态到任意模态的随机生成与补全。

**研究动机**：多传感器地球观测模态之间的映射本质上是非单射，同一条件可对应多种物理合理结果；确定性模型易退化到条件均值，难以表达不确定性与多样性，影响跨传感器翻译与缺失数据补全。

**核心方法**：提出多模态 latent diffusion transformer，在各模态原生空间分辨率上学习异构模态的联合分布，并将跨模态关系参数化为条件分布，从而支持 zero-shot 模态翻译、光谱波段填充、以及部分/缺失输入下的 any-to-any 生成且无需任务特定再训练。

**主要结论**：在大规模全球多模态数据集上，COP-GEN 能生成多样且物理一致的样本，同时在光学/雷达/高程上保持较高峰值保真度；模型还能随条件信息增多系统性降低输出不确定性，表明评估应超越单参考逐点指标以刻画随机生成质量。

**关键词**：地球观测多模态, 多传感器融合, 条件生成建模, 随机生成模型, 潜空间扩散模型, 零样本模态翻译, 跨传感器翻译, 光学-雷达-高程联合建模, 光谱波段补全, 缺失输入生成, 不确定性量化

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03239v1) | [下载PDF](https://arxiv.org/pdf/2603.03239v1.pdf)

---

## [17. Specificity-aware reinforcement learning for fine-grained open-world classification](https://arxiv.org/abs/2603.03197v1)

**作者**：Samuele Angheben, Davide Berasi, Alessandro Conti 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-03

### 📄 论文摘要

Classifying fine-grained visual concepts under open-world settings, i.e., without a predefined label set, demands models to be both accurate and specific. Recent reasoning Large Multimodal Models (LMMs) exhibit strong visual understanding capability but tend to produce overly generic predictions when performing fine-grained image classification. Our preliminary analysis reveals that models do possess the intrinsic fine-grained domain knowledge. However, promoting more specific predictions (specificity) without compromising correct ones (correctness) remains a non-trivial and understudied challenge. In this work, we investigate how to steer reasoning LMMs toward predictions that are both correct and specific. We propose a novel specificity-aware reinforcement learning framework, SpeciaRL, to fine-tune reasoning LMMs on fine-grained image classification under the open-world setting. SpeciaRL introduces a dynamic, verifier-based reward signal anchored to the best predictions within online rollouts, promoting specificity while respecting the model's capabilities to prevent incorrect predictions. Our out-of-domain experiments show that SpeciaRL delivers the best trade-off between correctness and specificity across extensive fine-grained benchmarks, surpassing existing methods and advancing open-world fine-grained image classification. Code and model are publicly available at https://github.com/s-angheben/SpeciaRL.

### 🤖 AI 总结

**一句话总结**：提出SpeciaRL，通过特异性敏感的强化学习微调推理型多模态大模型，使其在开放世界细粒度分类中同时提升“正确性”和“具体性”。

**研究动机**：推理型LMM虽然具备细粒度知识，但在开放世界分类时常给出过于泛化的标签；直接追求更具体又容易牺牲正确率，因此需要能在两者间自适应权衡的训练机制。

**核心方法**：SpeciaRL采用基于验证器的动态奖励，在在线rollout中以“当前最优预测”为锚点构造奖励信号，鼓励模型在不超出自身能力边界的前提下输出更具体的答案，并通过强化学习进行微调。

**主要结论**：在多项域外细粒度基准上，SpeciaRL在正确性-具体性的权衡上优于现有方法，显著减少过于宽泛的预测并保持/提升整体准确性，从而推进开放世界细粒度分类性能。

**关键词**：开放世界分类, 细粒度图像分类, 特异性预测, 正确性-特异性权衡, 多模态大模型（LMM）, 推理多模态模型, 强化学习微调（RLHF）, 验证器奖励模型, 动态奖励信号, 域外泛化评测, 细粒度基准测试

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03197v1) | [下载PDF](https://arxiv.org/pdf/2603.03197v1.pdf)

---

## [18. Chain of World: World Model Thinking in Latent Motion](https://arxiv.org/abs/2603.03195v1)

**作者**：Fuxiang Yang, Donglin Di, Lulu Tang 等 9 位作者  
**分类**：cs.CV, cs.AI, cs.RO  
**发布时间**：2026-03-03

### 📄 论文摘要

Vision-Language-Action (VLA) models are a promising path toward embodied intelligence, yet they often overlook the predictive and temporal-causal structure underlying visual dynamics. World-model VLAs address this by predicting future frames, but waste capacity reconstructing redundant backgrounds. Latent-action VLAs encode frame-to-frame transitions compactly, but lack temporally continuous dynamic modeling and world knowledge. To overcome these limitations, we introduce CoWVLA (Chain-of-World VLA), a new "Chain of World" paradigm that unifies world-model temporal reasoning with a disentangled latent motion representation. First, a pretrained video VAE serves as a latent motion extractor, explicitly factorizing video segments into structure and motion latents. Then, during pre-training, the VLA learns from an instruction and an initial frame to infer a continuous latent motion chain and predict the segment's terminal frame. Finally, during co-fine-tuning, this latent dynamic is aligned with discrete action prediction by jointly modeling sparse keyframes and action sequences in a unified autoregressive decoder. This design preserves the world-model benefits of temporal reasoning and world knowledge while retaining the compactness and interpretability of latent actions, enabling efficient visuomotor learning. Extensive experiments on robotic simulation benchmarks show that CoWVLA outperforms existing world-model and latent-action approaches and achieves moderate computational efficiency, highlighting its potential as a more effective VLA pretraining paradigm. The project website can be found at https://fx-hit.github.io/cowvla-io.

### 🤖 AI 总结

**一句话总结**：CoWVLA提出“Chain of World”范式，用结构/运动解耦的连续潜在运动链来做世界模型式时序推理，并在微调时与离散动作预测对齐，从而提升VLA的高效视觉-运动学习能力。

**研究动机**：现有世界模型VLA需要重建冗余背景而浪费容量，潜在动作VLA虽紧凑但缺少连续时序动力学建模与世界知识整合，导致对长期预测与因果动态理解不足。

**核心方法**：先用预训练视频VAE将视频片段显式分解为结构latent与运动latent；预训练阶段模型根据指令与首帧推断连续的“潜在运动链”并预测终帧；协同微调阶段在统一自回归解码器中联合建模稀疏关键帧与动作序列，使连续动力学表征与离散动作输出对齐。

**主要结论**：在机器人仿真基准上，CoWVLA相较世界模型和潜在动作方法取得更好性能，并保持中等计算效率，表明该预训练范式能兼顾时序推理/世界知识与表示紧凑性、可解释性。

**关键词**：视觉-语言-动作模型（VLA）, 具身智能, 世界模型, 时序因果推理, 未来帧预测, 潜在动作表示, 解耦潜在运动, 连续潜在动力学, 关键帧建模, 动作序列预测, 机器人仿真评测

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03195v1) | [下载PDF](https://arxiv.org/pdf/2603.03195v1.pdf)

---

## [19. MoD-DPO: Towards Mitigating Cross-modal Hallucinations in Omni LLMs using Modality Decoupled Preference Optimization](https://arxiv.org/abs/2603.03192v1)

**作者**：Ashutosh Chaubey, Jiacheng Pang, Mohammad Soleymani  
**分类**：cs.CV, cs.CL, cs.LG  
**发布时间**：2026-03-03

### 📄 论文摘要

Omni-modal large language models (omni LLMs) have recently achieved strong performance across audiovisual understanding tasks, yet they remain highly susceptible to cross-modal hallucinations arising from spurious correlations and dominant language priors. In this work, we propose Modality-Decoupled Direct Preference Optimization (MoD-DPO), a simple and effective framework for improving modality grounding in omni LLMs. MoD-DPO introduces modality-aware regularization terms that explicitly enforce invariance to corruptions in irrelevant modalities and sensitivity to perturbations in relevant modalities, thereby reducing unintended cross-modal interactions. To further mitigate over-reliance on textual priors, we incorporate a language-prior debiasing penalty that discourages hallucination-prone text-only responses. Extensive experiments across multiple audiovisual hallucination benchmarks demonstrate that MoD-DPO consistently improves perception accuracy and hallucination resistance, outperforming previous preference optimization baselines under similar training budgets. Our findings underscore the importance of modality-faithful alignment and demonstrate a scalable path toward more reliable and resilient multimodal foundation models.

### 🤖 AI 总结

**一句话总结**：MoD-DPO 通过“模态解耦”的偏好优化与语言先验去偏置，显著降低全模态LLM的跨模态幻觉并提升感知对齐。

**研究动机**：现有全模态LLM在音视频理解中容易因伪相关与强语言先验产生跨模态幻觉，导致回答与真实感知不一致。需要一种在不大幅增加训练成本下强化模态 grounding、抑制错误跨模态耦合的方法。

**核心方法**：提出 MoD-DPO，在DPO中加入模态感知正则：对“无关模态”的扰动保持不变性、对“相关模态”的扰动保持敏感性，以减少不必要的跨模态交互。同时引入语言先验去偏置惩罚，降低模型依赖文本先验生成“看似合理但与感知无关”的文本回答。

**主要结论**：在多项视听幻觉基准上，MoD-DPO 在相近训练预算下比既有偏好优化基线更能提升感知准确率与抗幻觉能力，证明模态忠实的对齐与去语言先验对可靠多模态模型至关重要。

**关键词**：跨模态幻觉, 多模态对齐, 模态扎根, 直接偏好优化（DPO）, 模态解耦偏好优化, 模态感知正则化, 模态不变性约束, 语言先验去偏, 多模态幻觉评测基准

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03192v1) | [下载PDF](https://arxiv.org/pdf/2603.03192v1.pdf)

---

## [20. ProSMA-UNet: Decoder Conditioning for Proximal-Sparse Skip Feature Selection](https://arxiv.org/abs/2603.03187v1)

**作者**：Chun-Wun Cheng, Yanqi Cheng, Peiyuan Jing 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-03

### 📄 论文摘要

Medical image segmentation commonly relies on U-shaped encoder-decoder architectures such as U-Net, where skip connections preserve fine spatial detail by injecting high-resolution encoder features into the decoder. However, these skip pathways also propagate low-level textures, background clutter, and acquisition noise, allowing irrelevant information to bypass deeper semantic filtering -- an issue that is particularly detrimental in low-contrast clinical imaging. Although attention gates have been introduced to address this limitation, they typically produce dense sigmoid masks that softly reweight features rather than explicitly removing irrelevant activations. We propose ProSMA-UNet (Proximal-Sparse Multi-Scale Attention U-Net), which reformulates skip gating as a decoder-conditioned sparse feature selection problem. ProSMA constructs a multi-scale compatibility field using lightweight depthwise dilated convolutions to capture relevance across local and contextual scales, then enforces explicit sparsity via an $\ell_1$ proximal operator with learnable per-channel thresholds, yielding a closed-form soft-thresholding gate that can remove noisy responses. To further suppress semantically irrelevant channels, ProSMA incorporates decoder-conditioned channel gating driven by global decoder context. Extensive experiments on challenging 2D and 3D benchmarks demonstrate state-of-the-art performance, with particularly large gains ($\approx20$\%) on difficult 3D segmentation tasks. Project page: https://math-ml-x.github.io/ProSMA-UNet/

### 🤖 AI 总结

**一句话总结**：ProSMA-UNet通过将跳连门控改为“解码器条件的稀疏特征选择”，用显式稀疏阈值化去除跳连噪声与无关信息，从而提升医学图像分割效果。

**研究动机**：U-Net跳跃连接虽保留细节，但也会把纹理噪声、背景杂波等低层信息直接注入解码器，尤其在低对比度医学影像中会显著干扰分割。现有注意力门多为稠密软权重（sigmoid重标定），难以真正“删掉”无关激活。

**核心方法**：提出ProSMA（Proximal-Sparse Multi-Scale Attention）跳连门控：先用轻量级深度可分离空洞卷积构建多尺度兼容性场以评估相关性；再通过带可学习通道阈值的ℓ1近端算子实现闭式软阈值（soft-thresholding）门控，显式产生稀疏选择以抑制噪声。进一步加入由全局解码器上下文驱动的解码器条件通道门控，抑制语义不相关通道。

**主要结论**：在多个2D与3D医学分割基准上取得SOTA表现，尤其在困难3D任务上提升显著（约20%）。结果表明，相比稠密注意力，显式稀疏的解码器条件跳连选择更能过滤无关特征并增强分割鲁棒性。

**关键词**：医学图像分割, 跳跃连接, 注意力门控, 稀疏特征选择, 解码器条件化, 多尺度注意力, 深度可分离空洞卷积, L1近端算子, 软阈值门控, 三维分割

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03187v1) | [下载PDF](https://arxiv.org/pdf/2603.03187v1.pdf)

---

## cs.LG

## [21. Learning Demographic-Conditioned Mobility Trajectories with Aggregate Supervision](https://arxiv.org/abs/2603.03275v1)

**作者**：Jessie Z. Li, Zhiqing Hong, Toru Shirakawa 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-03

### 📄 论文摘要

Human mobility trajectories are widely studied in public health and social science, where different demographic groups exhibit significantly different mobility patterns. However, existing trajectory generation models rarely capture this heterogeneity because most trajectory datasets lack demographic labels. To address this gap in data, we propose ATLAS, a weakly supervised approach for demographic-conditioned trajectory generation using only (i) individual trajectories without demographic labels, (ii) region-level aggregated mobility features, and (iii) region-level demographic compositions from census data. ATLAS trains a trajectory generator and fine-tunes it so that simulated mobility matches observed regional aggregates while conditioning on demographics. Experiments on real trajectory data with demographic labels show that ATLAS substantially improves demographic realism over baselines (JSD $\downarrow$ 12%--69%) and closes much of the gap to strongly supervised training. We further develop theoretical analyses for when and why ATLAS works, identifying key factors including demographic diversity across regions and the informativeness of the aggregate feature, paired with experiments demonstrating the practical implications of our theory. We release our code at https://github.com/schang-lab/ATLAS.

### 🤖 AI 总结

**一句话总结**：ATLAS在缺乏个体人口统计标签的情况下，利用区域级聚合移动特征与人口普查构成，实现可按人口统计条件生成更真实的人类移动轨迹。

**研究动机**：不同人口群体的出行模式差异显著，但大多数轨迹数据缺少人口统计标签，导致现有生成模型难以刻画群体异质性。为弥补标注缺口，作者希望仅用无标签个体轨迹与可获得的区域聚合统计来学习“按人口统计条件”的轨迹生成。

**核心方法**：提出弱监督框架ATLAS：先训练轨迹生成器，再在“按人口统计条件生成”的同时，通过匹配模拟结果与真实的区域级聚合移动特征/人口结构来微调，使生成分布在区域层面与观测统计一致。并给出理论分析，刻画ATLAS有效的条件（如区域间人口统计多样性、聚合特征的信息量等），并用实验验证这些因素的影响。

**主要结论**：在带有人口统计标签的真实数据上，ATLAS相较基线显著提升人口统计真实性（JSD降低12%–69%），并在效果上接近强监督训练。理论与实证共同表明：区域人口结构差异越大、聚合特征越能区分群体行为时，弱监督对齐越有效。

**关键词**：人口统计条件生成, 出行轨迹生成, 弱监督学习, 聚合监督, 区域级移动性特征, 人口普查数据, 群体异质性建模, 轨迹生成模型微调, 分布匹配

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03275v1) | [下载PDF](https://arxiv.org/pdf/2603.03275v1.pdf)

---

## [22. On Geometry Regularization in Autoencoder Reduced-Order Models with Latent Neural ODE Dynamics](https://arxiv.org/abs/2603.03238v1)

**作者**：Mikhail Osipov  
**分类**：cs.LG, math.NA, physics.comp-ph  
**发布时间**：2026-03-03

### 📄 论文摘要

We investigate geometric regularization strategies for learned latent representations in encoder--decoder reduced-order models. In a fixed experimental setting for the advection--diffusion--reaction (ADR) equation, we model latent dynamics using a neural ODE and evaluate four regularization approaches applied during autoencoder pre-training: (a) near-isometry regularization of the decoder Jacobian, (b) a stochastic decoder gain penalty based on random directional gains, (c) a second-order directional curvature penalty, and (d) Stiefel projection of the first decoder layer. Across multiple seeds, we find that (a)--(c) often produce latent representations that make subsequent latent-dynamics training with a frozen autoencoder more difficult, especially for long-horizon rollouts, even when they improve local decoder smoothness or related sensitivity proxies. In contrast, (d) consistently improves conditioning-related diagnostics of the learned latent dynamics and tends to yield better rollout performance. We discuss the hypothesis that, in this setting, the downstream impact of latent-geometry mismatch outweighs the benefits of improved decoder smoothness.

### 🤖 AI 总结

**一句话总结**：在基于Autoencoder+潜空间Neural ODE的ROM中，多数“平滑/近等距”几何正则会削弱后续潜动力学训练与长时预测，而将解码器首层做Stiefel正交投影更稳定并提升rollout表现。

**研究动机**：潜空间表示的几何性质会影响潜动力学（Neural ODE）的可训练性与长时稳定性，但哪些几何正则真正有利于下游动力学学习尚不清楚。

**核心方法**：在ADR方程的固定实验设置下，先对自编码器预训练并分别加入四类几何正则：(a)解码器Jacobian近等距、(b)随机方向增益惩罚、(c)二阶方向曲率惩罚、(d)解码器首层Stiefel投影；随后冻结AE训练潜空间Neural ODE，并用多seed比较诊断指标与长时rollout误差。

**主要结论**：(a)-(c)尽管改善局部平滑/敏感度代理指标，却常使冻结AE后的潜动力学训练更困难、长时rollout更差；(d)则一致改善潜动力学的条件数相关诊断并通常带来更好的rollout，作者推测“潜空间几何不匹配”的下游负面效应可能超过局部平滑带来的收益。

**关键词**：降阶模型（ROM）, 自编码器预训练, 潜变量表示学习, 潜变量神经ODE, 几何正则化, 解码器雅可比近等距, 随机方向增益惩罚, 二阶方向曲率惩罚, 动力学可条件性, 长时域滚动预测

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03238v1) | [下载PDF](https://arxiv.org/pdf/2603.03238v1.pdf)

---

## [23. Guiding Sparse Neural Networks with Neurobiological Principles to Elicit Biologically Plausible Representations](https://arxiv.org/abs/2603.03234v1)

**作者**：Patrick Inoue, Florian Röhrbein, Andreas Knoblauch  
**分类**：cs.LG  
**发布时间**：2026-03-03

### 📄 论文摘要

While deep neural networks (DNNs) have achieved remarkable performance in tasks such as image recognition, they often struggle with generalization, learning from few examples, and continuous adaptation - abilities inherent in biological neural systems. These challenges arise due to DNNs' failure to emulate the efficient, adaptive learning mechanisms of biological networks. To address these issues, we explore the integration of neurobiologically inspired assumptions in neural network learning. This study introduces a biologically inspired learning rule that naturally integrates neurobiological principles, including sparsity, lognormal weight distributions, and adherence to Dale's law, without requiring explicit enforcement. By aligning with these core neurobiological principles, our model enhances robustness against adversarial attacks and demonstrates superior generalization, particularly in few-shot learning scenarios. Notably, integrating these constraints leads to the emergence of biologically plausible neural representations, underscoring the efficacy of incorporating neurobiological assumptions into neural network design. Preliminary results suggest that this approach could extend from feature-specific to task-specific encoding, potentially offering insights into neural resource allocation for complex tasks.

### 🤖 AI 总结

**一句话总结**：提出一种无需显式约束即可自然产生稀疏性、对数正态权重分布与Dale定律的生物启发学习规则，从而提升鲁棒性与小样本泛化并诱导更“类脑”的表征。

**研究动机**：现有DNN在少样本学习、持续适应与泛化方面弱于生物神经系统，根源在于缺乏高效且自适应的生物式学习机制。作者希望将关键神经生物学原则融入学习过程以弥补这些能力差距。

**核心方法**：设计一种生物启发的学习规则，使网络在训练中自发呈现稀疏连接/激活、权重对数正态分布以及遵循Dale定律（兴奋/抑制分离），而非通过额外正则或硬约束强制实现。并评估其在对抗鲁棒性、泛化与few-shot场景中的表现及表征形态。

**主要结论**：引入这些神经生物学约束后，模型对对抗攻击更稳健、在小样本与泛化上优于基线，同时出现更符合生物可解释性的神经表征。初步结果还提示该机制可能从“特征特异”编码扩展到“任务特异”编码，为复杂任务的神经资源分配提供启示。

**关键词**：稀疏神经网络, 神经生物启发学习规则, 生物可解释表征, 少样本学习, 持续学习, 神经资源分配, 任务特定编码, Guiding

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03234v1) | [下载PDF](https://arxiv.org/pdf/2603.03234v1.pdf)

---

## [24. SynthCharge: An Electric Vehicle Routing Instance Generator with Feasibility Screening to Enable Learning-Based Optimization and Benchmarking](https://arxiv.org/abs/2603.03230v1)

**作者**：Mertcan Daysalilar, Fuat Uyguroglu, Gabriel Nicolosi 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-03

### 📄 论文摘要

The electric vehicle routing problem with time windows (EVRPTW) extends the classical VRPTW by introducing battery capacity constraints and charging station decisions. Existing benchmark datasets are often static and lack verifiable feasibility, which restricts reproducible evaluation of learning-based routing models. We introduce SynthCharge, a parametric generator that produces diverse, feasibility-screened EVRPTW instances across varying spatiotemporal configurations and scalable customer counts. While SynthCharge can currently generate large-scale instances of up to 500 customers, we focus our experiments on sizes ranging from 5 to 100 customers. Unlike static benchmark suites, SynthCharge integrates instance geometry with adaptive energy capacity scaling and range-aware charging station placement. To guarantee structural validity, the generator systematically filters out unsolvable instances through a fast feasibility screening process. Ultimately, SynthCharge provides the dynamic benchmarking infrastructure needed to systematically evaluate the robustness of emerging neural routing and data-driven approaches.

### 🤖 AI 总结

**一句话总结**：提出SynthCharge，一个可参数化生成并快速筛除不可行实例的EVRPTW数据生成器，用于支持学习式优化方法的系统评测与基准测试。

**研究动机**：现有EVRPTW基准数据集多为静态且可行性难以验证，导致学习型路径规划模型的评估不可复现、鲁棒性难以系统比较。需要能生成多样化、规模可扩展且具备可行性保障的动态评测基础设施。

**核心方法**：设计参数化实例生成流程，将空间几何、时间窗配置与“自适应能量容量缩放”和“面向续航的充电站布设”联合建模，覆盖不同规模（最高可到500客户）。随后通过快速可行性筛查过滤掉结构上不可解的实例，确保生成数据具备可解性与有效性。

**主要结论**：SynthCharge能稳定产出多样且经过可行性验证的EVRPTW实例（实验聚焦5–100客户），为神经路由与数据驱动方法提供更可复现、可扩展的动态基准测试环境，并便于评估模型在不同配置下的鲁棒性。

**关键词**：电动汽车路径规划（EVRPTW）, 时间窗车辆路径规划（VRPTW）, 合成实例生成器, 可行性筛查, 基准评测框架, 学习驱动优化, 神经路径规划, 充电站选址, 电池容量约束, 规模化实例生成

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03230v1) | [下载PDF](https://arxiv.org/pdf/2603.03230v1.pdf)

---

## [25. Inverse Reconstruction of Shock Time Series from Shock Response Spectrum Curves using Machine Learning](https://arxiv.org/abs/2603.03229v1)

**作者**：Adam Watts, Andrew Jeon, Destry Newton 等 4 位作者  
**分类**：cs.LG, eess.SP  
**发布时间**：2026-03-03

### 📄 论文摘要

The shock response spectrum (SRS) is widely used to characterize the response of single-degree-of-freedom (SDOF) systems to transient accelerations. Because the mapping from acceleration time history to SRS is nonlinear and many-to-one, reconstructing time-domain signals from a target spectrum is inherently ill-posed. Conventional approaches address this problem through iterative optimization, typically representing signals as sums of exponentially decayed sinusoids, but these methods are computationally expensive and constrained by predefined basis functions.   We propose a conditional variational autoencoder (CVAE) that learns a data-driven inverse mapping from SRS to acceleration time series. Once trained, the model generates signals consistent with prescribed target spectra without requiring iterative optimization. Experiments demonstrate improved spectral fidelity relative to classical techniques, strong generalization to unseen spectra, and inference speeds three to six orders of magnitude faster. These results establish deep generative modeling as a scalable and efficient approach for inverse SRS reconstruction.

### 🤖 AI 总结

**一句话总结**：论文提出用条件变分自编码器（CVAE）从冲击响应谱（SRS）直接生成满足目标谱的加速度时域信号，实现快速且高保真逆重建。

**研究动机**：SRS到时域加速度的映射是非线性且多对一，导致从目标谱反推时域信号天然病态；传统迭代优化方法计算昂贵且受限于预设基函数表达能力。

**核心方法**：训练一个以目标SRS为条件的CVAE，学习数据驱动的“谱→时域”生成式逆映射；推理阶段无需迭代优化即可采样生成与目标SRS一致的冲击时序。

**主要结论**：实验表明该方法在谱一致性上优于经典技术，并能泛化到未见过的谱；同时推理速度提升约3–6个数量级，证明深度生成模型可高效扩展用于逆SRS重建。

**关键词**：冲击响应谱（SRS）, 单自由度系统（SDOF）, 时域信号重建, 谱到时域逆映射, 非线性多对一映射, 病态逆问题, 条件变分自编码器（CVAE）, 深度生成模型, 迭代优化基线, 指数衰减正弦基函数, 推理加速

**评分**：17

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03229v1) | [下载PDF](https://arxiv.org/pdf/2603.03229v1.pdf)

---

## [26. Coalgebras for categorical deep learning: Representability and universal approximation](https://arxiv.org/abs/2603.03227v1)

**作者**：Dragan Mašulović  
**分类**：cs.LG  
**发布时间**：2026-03-03

### 📄 论文摘要

Categorical deep learning (CDL) has recently emerged as a framework that leverages category theory to unify diverse neural architectures. While geometric deep learning (GDL) is grounded in the specific context of invariants of group actions, CDL aims to provide domain-independent abstractions for reasoning about models and their properties. In this paper, we contribute to this program by developing a coalgebraic foundation for equivariant representation in deep learning, as classical notions of group actions and equivariant maps are naturally generalized by the coalgebraic formalism. Our first main result demonstrates that, given an embedding of data sets formalized as a functor from SET to VECT, and given a notion of invariant behavior on data sets modeled by an endofunctor on SET, there is a corresponding endofunctor on VECT that is compatible with the embedding in the sense that this lifted functor recovers the analogous notion of invariant behavior on the embedded data. Building on this foundation, we then establish a universal approximation theorem for equivariant maps in this generalized setting. We show that continuous equivariant functions can be approximated within our coalgebraic framework for a broad class of symmetries. This work thus provides a categorical bridge between the abstract specification of invariant behavior and its concrete realization in neural architectures.

### 🤖 AI 总结

**一句话总结**：提出用余代数（coalgebra）为范畴深度学习建立等变表示的统一基础，并在该框架下给出等变函数的通用逼近定理。

**研究动机**：现有几何深度学习多依赖群作用不变量，难以覆盖更一般的“对称/不变行为”抽象；CDL希望用领域无关的范畴语言统一刻画模型结构与性质。

**核心方法**：将数据集嵌入形式化为SET→VECT的函子，并用SET上的自函子刻画“不变行为”；证明可将该自函子提升到VECT上且与嵌入相容，从而在向量空间表征中复现原始不变性，并据此建立余代数化的等变映射定义与逼近框架。

**主要结论**：证明了上述“行为函子提升”的表示性结果，并在广泛对称性条件下给出连续等变函数的通用逼近定理，连接了抽象不变性规范与可实现的神经网络架构设计。

**关键词**：范畴深度学习, 几何深度学习, 余代数, 等变表示, 等变映射, 不变性, 函子提升, 端函子, 普适逼近定理

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03227v1) | [下载PDF](https://arxiv.org/pdf/2603.03227v1.pdf)

---

## [27. Adaptive Methods Are Preferable in High Privacy Settings: An SDE Perspective](https://arxiv.org/abs/2603.03226v1)

**作者**：Enea Monzio Compagnoni, Alessandro Stanghellini, Rustem Islamov 等 5 位作者  
**分类**：cs.LG, cs.CR  
**发布时间**：2026-03-03

### 📄 论文摘要

Differential Privacy (DP) is becoming central to large-scale training as privacy regulations tighten. We revisit how DP noise interacts with adaptivity in optimization through the lens of stochastic differential equations, providing the first SDE-based analysis of private optimizers. Focusing on DP-SGD and DP-SignSGD under per-example clipping, we show a sharp contrast under fixed hyperparameters: DP-SGD converges at a Privacy-Utility Trade-Off of $\mathcal{O}(1/\varepsilon^2)$ with speed independent of $\varepsilon$, while DP-SignSGD converges at a speed linear in $\varepsilon$ with an $\mathcal{O}(1/\varepsilon)$ trade-off, dominating in high-privacy or large batch noise regimes. By contrast, under optimal learning rates, both methods achieve comparable theoretical asymptotic performance; however, the optimal learning rate of DP-SGD scales linearly with $\varepsilon$, while that of DP-SignSGD is essentially $\varepsilon$-independent. This makes adaptive methods far more practical, as their hyperparameters transfer across privacy levels with little or no re-tuning. Empirical results confirm our theory across training and test metrics, and empirically extend from DP-SignSGD to DP-Adam.

### 🤖 AI 总结

**一句话总结**：从SDE视角分析差分隐私训练发现：在高隐私（小ε）或噪声更强的场景下，像DP-SignSGD这类自适应/符号方法比DP-SGD更稳健且更省调参。

**研究动机**：DP训练引入的噪声会显著改变优化动态，但现有理论较少刻画“隐私噪声×优化器自适应性”的交互规律。作者希望解释为何在不同隐私强度下，DP-SGD与自适应方法的收敛速度与调参敏感性差异巨大。

**核心方法**：将DP-SGD与DP-SignSGD（逐样本裁剪+DP噪声）的离散更新用随机微分方程（SDE）近似，推导在固定超参与最优学习率两种设定下的收敛速度与隐私-效用权衡。并通过实验验证理论结论，并将观察扩展到DP-Adam。

**主要结论**：固定超参时，DP-SGD呈现约O(1/ε^2)的隐私-效用权衡且收敛速度对ε不敏感，而DP-SignSGD达到约O(1/ε)权衡且收敛速度随ε线性变化，因此在高隐私/大噪声下更优。采用最优学习率时两者渐近性能接近，但DP-SGD的最优学习率需随ε线性缩放、DP-SignSGD几乎与ε无关，使自适应方法在跨隐私等级迁移时更实用、少调参。

**关键词**：差分隐私, 隐私优化器, 随机微分方程分析, 自适应优化, 逐样本梯度裁剪, 高隐私训练, 学习率缩放, 批量噪声

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03226v1) | [下载PDF](https://arxiv.org/pdf/2603.03226v1.pdf)

---

## [28. Stabilized Adaptive Loss and Residual-Based Collocation for Physics-Informed Neural Networks](https://arxiv.org/abs/2603.03224v1)

**作者**：Divyavardhan Singh, Shubham Kamble, Dimple Sonone 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-03

### 📄 论文摘要

Physics-Informed Neural Networks (PINNs) have been recognized as a mesh-free alternative to solve partial differential equations where physics information is incorporated. However, in dealing with problems characterized by high stiffness or shock-dominated dynamics, traditional PINNs have been found to have limitations, including unbalanced training and inaccuracy in solution, even with small physics residuals. In this research, we seek to address these limitations using the viscous Burgers' equation with low viscosity and the Allen-Cahn equation as test problems. In addressing unbalanced training, we have developed a new adaptive loss balancing scheme using smoothed gradient norms to ensure satisfaction of initial and boundary conditions. Further, to address inaccuracy in the solution, we have developed an adaptive residual-based collocation scheme to improve the accuracy of solutions in the regions with high physics residuals. The proposed new approach significantly improves solution accuracy with consistent satisfaction of physics residuals. For instance, in the case of Burgers' equation, the relative L2 error is reduced by about 44 percent compared to traditional PINNs, while for the Allen-Cahn equation, the relative L2 error is reduced by approximately 70 percent. Additionally, we show the trustworthy solution comparison of the proposed method using a robust finite difference solver.

### 🤖 AI 总结

**一句话总结**：本文提出“稳定的自适应损失平衡 + 基于残差的自适应采样”两项改进，以提升PINNs在高刚性/激波类PDE上的训练稳定性与解的精度。

**研究动机**：传统PINNs在低粘性Burgers方程、Allen–Cahn等高刚性或激波主导问题中易出现损失项训练不均衡，导致初边值条件难满足；且即便物理残差较小，数值解仍可能不准确。

**核心方法**：提出用“平滑梯度范数”驱动的自适应损失权重策略，动态平衡初值/边界/物理残差等项以稳定训练；并引入自适应残差驱动的配置点(collocation)重采样，把更多采样点分配到高残差区域以强化局部学习。

**主要结论**：在低粘性Burgers与Allen–Cahn测试中，该方法在保持物理残差一致满足的同时显著降低相对L2误差（分别约降低44%与70%）；并通过稳健的有限差分求解器对比验证了结果可信度。

**关键词**：物理信息神经网络（PINN）, 偏微分方程求解, 激波捕捉, 自适应损失平衡, 梯度范数平滑, 初边值条件约束, 残差驱动配点法, 自适应采样, 有限差分基准对比

**评分**：15

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03224v1) | [下载PDF](https://arxiv.org/pdf/2603.03224v1.pdf)

---

## [29. I-CAM-UV: Integrating Causal Graphs over Non-Identical Variable Sets Using Causal Additive Models with Unobserved Variables](https://arxiv.org/abs/2603.03207v1)

**作者**：Hirofumi Suzuki, Kentaro Kanamori, Takuya Takagi 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-03

### 📄 论文摘要

Causal discovery from observational data is a fundamental tool in various fields of science. While existing approaches are typically designed for a single dataset, we often need to handle multiple datasets with non-identical variable sets in practice. One straightforward approach is to estimate a causal graph from each dataset and construct a single causal graph by overlapping. However, this approach identifies limited causal relationships because unobserved variables in each dataset can be confounders, and some variable pairs may be unobserved in any dataset. To address this issue, we leverage Causal Additive Models with Unobserved Variables (CAM-UV) that provide causal graphs having information related to unobserved variables. We show that the ground truth causal graph has structural consistency with the information of CAM-UV on each dataset. As a result, we propose an approach named I-CAM-UV to integrate CAM-UV results by enumerating all consistent causal graphs. We also provide an efficient combinatorial search algorithm and demonstrate the usefulness of I-CAM-UV against existing methods.

### 🤖 AI 总结

**一句话总结**：I-CAM-UV利用CAM-UV在各数据集上推断出的“含未观测变量信息”的因果约束，枚举并整合得到跨多数据集（变量集合不一致）的全局一致因果图。

**研究动机**：现实中常有多个观测数据集且变量集合不完全重合，简单对各自学到的因果图做重叠会因未观测混杂与变量对从未共同出现而只能识别很少因果关系。

**核心方法**：先对每个数据集运行CAM-UV获取包含潜在未观测变量影响线索的局部因果信息，并证明真实全局因果图与这些信息满足结构一致性；随后提出I-CAM-UV，通过枚举所有与各数据集CAM-UV结果一致的候选因果图并用高效组合搜索算法完成整合。

**主要结论**：I-CAM-UV能在存在未观测混杂且变量集合不一致的多数据集场景下恢复更多因果关系，并在实验中相较现有整合/基线方法表现更优。

**关键词**：观测数据, 多数据集整合, 非一致变量集, 因果图融合, 潜变量, 未观测混杂, 因果加性模型, 一致因果图枚举, 组合搜索算法

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03207v1) | [下载PDF](https://arxiv.org/pdf/2603.03207v1.pdf)

---

## [30. Understanding and Mitigating Dataset Corruption in LLM Steering](https://arxiv.org/abs/2603.03206v1)

**作者**：Cullen Anderson, Narmeen Oozeer, Foad Namjoo 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-03-03

### 📄 论文摘要

Contrastive steering has been shown as a simple and effective method to adjust the generative behavior of LLMs at inference time. It uses examples of prompt responses with and without a trait to identify a direction in an intermediate activation layer, and then shifts activations in this 1-dimensional subspace. However, despite its growing use in AI safety applications, the robustness of contrastive steering to noisy or adversarial data corruption is poorly understood. We initiate a study of the robustness of this process with respect to corruption of the dataset of examples used to train the steering direction. Our first observation is that contrastive steering is quite robust to a moderate amount of corruption, but unwanted side effects can be clearly and maliciously manifested when a non-trivial fraction of the training data is altered. Second, we analyze the geometry of various types of corruption, and identify some safeguards. Notably, a key step in learning the steering direction involves high-dimensional mean computation, and we show that replacing this step with a recently developed robust mean estimator often mitigates most of the unwanted effects of malicious corruption.

### 🤖 AI 总结

**一句话总结**：论文研究对比式steering在训练示例数据被噪声/对抗性篡改时的鲁棒性，并提出用稳健均值估计替代普通均值以缓解恶意数据带来的副作用。

**研究动机**：对比式steering被广泛用于推理时行为调控与安全场景，但其依赖的“有/无特征”示例数据一旦被污染可能引入隐蔽且有害的偏移，现有对其鲁棒性理解不足。

**核心方法**：系统地向用于学习steering方向的示例数据注入不同类型与比例的随机/恶意腐化，分析其在激活空间中的几何影响；同时识别到关键脆弱环节是高维均值计算，并用近期的稳健均值估计器替换该步骤作为防护。

**主要结论**：对比式steering对中等比例的数据腐化总体较鲁棒，但当被篡改数据占到非平凡比例时会出现明显且可被恶意触发的副作用；采用稳健均值估计往往能显著削弱恶意腐化的影响并提升安全性。

**关键词**：LLM 行为控制, 推理时引导, 激活操控, 特征方向学习, 数据集污染, 鲁棒性分析, 高维均值估计, 鲁棒均值估计器

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.03206v1) | [下载PDF](https://arxiv.org/pdf/2603.03206v1.pdf)

---

