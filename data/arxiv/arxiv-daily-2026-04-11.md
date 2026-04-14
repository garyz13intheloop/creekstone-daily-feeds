# arXiv AI 论文日报 | 2026-04-11

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (13 篇)
- [cs.LG](#csLG) (5 篇)
- [cs.CL](#csCL) (3 篇)
- [cs.AI](#csAI) (9 篇)

---

## cs.AI

## [1. Beyond Monologue: Interactive Talking-Listening Avatar Generation with Conversational Audio Context-Aware Kernels](https://arxiv.org/abs/2604.10367v1)

**作者**：Yuzhe Weng, Haotian Wang, Xinyi Yu 等 7 位作者  
**分类**：cs.AI, cs.SD  
**发布时间**：2026-04-11

### 📄 论文摘要

Audio-driven human video generation has achieved remarkable success in monologue scenarios, largely driven by advancements in powerful video generation foundation models. Moving beyond monologues, authentic human communication is inherently a full-duplex interactive process, requiring virtual agents not only to articulate their own speech but also to react naturally to incoming conversational audio. Most existing methods simply extend conventional audio-driven paradigms to listening scenarios. However, relying on strict frame-to-frame alignment renders the model's response to long-range conversational dynamics rigid, whereas directly introducing global attention catastrophically degrades lip synchronization. Recognizing the unique temporal Scale Discrepancy between talking and listening behaviors, we introduce a multi-head Gaussian kernel to explicitly inject this physical intuition into the model as a progressive temporal inductive bias. Building upon this, we construct a full-duplex interactive virtual agent capable of simultaneously processing dual-stream audio inputs for both talking and listening. Furthermore, we introduce a rigorously cleaned Talking-Listening dataset VoxHear featuring perfectly decoupled speech and background audio tracks. Extensive experiments demonstrate that our approach successfully fuses strong temporal alignment with deep contextual semantics, setting a new state-of-the-art for generating highly natural and responsive full-duplex interactive digital humans. The project page is available at https://warmcongee.github.io/beyond-monologue/ .

### 🤖 AI 总结

**一句话总结**：本文提出基于多头高斯核的全双工交互式虚拟形象生成方法，解决说话与倾听行为间的时序尺度差异问题，实现自然响应的人机交互数字人。

**研究动机**：现有音频驱动视频生成方法多聚焦于独白场景，而真实的人类交流需要虚拟代理对对话音频做出自然反应；现有方法要么时序对齐僵化，要么直接引入全局注意力会严重损害唇形同步。

**核心方法**：引入多头高斯核作为渐进式时序归纳偏置，显式建模说话与倾听行为间的时序尺度差异；基于此构建能同时处理双流音频输入的全双工交互虚拟代理，并发布干净整洁的VoxHear数据集。

**主要结论**：该方法成功融合强时序对齐与深层上下文语义，在生成高度自然和响应灵敏的全双工交互数字人方面达到最新最优性能。

**关键词**：音频驱动视频生成, 全双工交互, 多头高斯核, 时序感应偏置, 唇形同步, 双流音频, 尺度差异, 说话-倾听

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10367v1) | [下载PDF](https://arxiv.org/pdf/2604.10367v1.pdf)

---

## [2. VeriTrans: Fine-Tuned LLM-Assisted NL-to-PL Translation via a Deterministic Neuro-Symbolic Pipeline](https://arxiv.org/abs/2604.10341v1)

**作者**：Xuan Liu, Dheeraj Kodakandla, Kushagra Srivastva 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-11

### 📄 论文摘要

\textbf{VeriTrans} is a reliability-first ML system that compiles natural-language requirements into solver-ready logic with validator-gated reliability. The pipeline integrates an instruction-tuned NL$\!\to\!$PL translator, round-trip reconstruction (PL$\!\to\!$NL) used as a high-precision acceptance gate, and canonical PL$\!\to\!$CNF compilation, all executed via fixed API configuration (temperature$=0$; fine-tuning runs use seed$=42$) and per-item artifact logging (prompts, outputs, hashes) to support auditability and replay-driven debugging. On \textbf{SatBench} (2{,}100 specifications), VeriTrans achieves 94.46\% SAT/UNSAT correctness and 87.73\% median round-trip similarity. Compact fine-tuning on 100--150 curated examples improves fidelity by about 1--1.5\,pp without increasing latency (mean 25.8\,s/spec on our 201-spec runtime subset). A thresholded acceptance policy on the round-trip score exposes a reliability--coverage knob: at $τ{=}75$, roughly 68\% of items are retained with $\sim$94\% correctness on the accepted set. Validator overhead contributes $<15\%$ of end-to-end runtime, and all prompts/responses and timing metadata are logged to enable replay-driven debugging and regression testing. By separating learned translation from symbolic verification and enforcing deterministic, validator-gated acceptance, VeriTrans turns NL$\!\to\!$logic front-ends into auditable, reproducible components for reliability-critical workflows.

### 🤖 AI 总结

**一句话总结**：VeriTrans是一个可靠性优先的系统，通过微调LLM将自然语言需求编译为求解器就绪的逻辑，并使用往返重建作为验证门控实现可审计的确定性翻译流程。

**研究动机**：在可靠性关键的工作流中，需要将自然语言需求准确转换为形式逻辑（PL），但现有NL→PL翻译方法的可靠性和可审计性不足，亟需一种可验证、可重现的解决方案。

**核心方法**：VeriTrans采用确定性神经符号混合流水线：先用指令微调的LLM进行NL→PL翻译，再通过PL→NL往返重建作为高精度验收门控，最后进行PL→CNF规范编译，同时固定API配置并记录所有提示和响应以支持可追溯调试。

**主要结论**：在SatBench的2100个规范上达到94.46%的SAT/UNSAT正确率和87.73%的中位往返相似度，仅用100-150个精选样本微调即可提升1-1.5pp保真度而不增加延迟，验证器开销仅占端到端运行时间的15%以下。

**关键词**：VeriTrans, Fine-Tuned, LLM-Assisted, NL-to-PL, Translation, via, Deterministic, Neuro-Symbolic

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10341v1) | [下载PDF](https://arxiv.org/pdf/2604.10341v1.pdf)

---

## [3. Zero-shot World Models Are Developmentally Efficient Learners](https://arxiv.org/abs/2604.10333v1)

**作者**：Khai Loong Aw, Klemen Kotar, Wanhee Lee 等 9 位作者  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-04-11

### 📄 论文摘要

Young children demonstrate early abilities to understand their physical world, estimating depth, motion, object coherence, interactions, and many other aspects of physical scene understanding. Children are both data-efficient and flexible cognitive systems, creating competence despite extremely limited training data, while generalizing to myriad untrained tasks -- a major challenge even for today's best AI systems. Here we introduce a novel computational hypothesis for these abilities, the Zero-shot Visual World Model (ZWM). ZWM is based on three principles: a sparse temporally-factored predictor that decouples appearance from dynamics; zero-shot estimation through approximate causal inference; and composition of inferences to build more complex abilities. We show that ZWM can be learned from the first-person experience of a single child, rapidly generating competence across multiple physical understanding benchmarks. It also broadly recapitulates behavioral signatures of child development and builds brain-like internal representations. Our work presents a blueprint for efficient and flexible learning from human-scale data, advancing both a computational account for children's early physical understanding and a path toward data-efficient AI systems.

### 🤖 AI 总结

**一句话总结**：本文提出零样本视觉世界模型(ZWM)，通过模仿儿童的高效灵活学习方式，实现从有限数据中快速掌握物理场景理解能力。

**研究动机**：儿童能以极低的数据量实现灵活的物理世界理解，而当前AI系统在数据效率和泛化能力上仍面临重大挑战，本文旨在缩小这一差距。

**核心方法**：ZWM基于三个核心原则：稀疏时间因子预测器（解耦外观与动力学）、通过近似因果推理实现零样本估计、以及组合推理以构建更复杂的能力。

**主要结论**：ZWM可从单个儿童的第一人称体验中学习，在多个物理理解基准上快速产生能力，广泛复现儿童发展行为特征，并构建类似大脑的内部表征。

**关键词**：零样本学习, 视觉世界模型, 因果推理, 数据高效学习, 认知发展, 稀疏时序预测, 泛化能力, 类脑表征, 第一人称视角学习

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10333v1) | [下载PDF](https://arxiv.org/pdf/2604.10333v1.pdf)

---

## [4. From GPT-3 to GPT-5: Mapping their capabilities, scope, limitations, and consequences](https://arxiv.org/abs/2604.10332v1)

**作者**：Hina Afridi, Habib Ullah, Sultan Daud Khan 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-11

### 📄 论文摘要

We present the progress of the GPT family from GPT-3 through GPT-3.5, GPT-4, GPT-4 Turbo, GPT-4o, GPT-4.1, and the GPT-5 family. Our work is comparative rather than merely historical. We investigates how the family evolved in technical framing, user interaction, modality, deployment architecture, and governance viewpoint. The work focuses on five recurring themes: technical progression, capability changes, deployment shifts, persistent limitations, and downstream consequences. In term of research design, we consider official technical reports, system cards, API and model documentation, product announcements, release notes, and peer-reviewed secondary studies. A primary assertion is that later GPT generations should not be interpreted only as larger or more accurate language models. Instead, the family evolves from a scaled few-shot text predictor into a set of aligned, multimodal, tool-oriented, long-context, and increasingly workflow-integrated systems. This development complicates simple model-to-model comparison because product routing, tool access, safety tuning, and interface design become part of the effective system. Across generations, several limitations remain unchanged: hallucination, prompt sensitivity, benchmark fragility, uneven behavior across domains and populations, and incomplete public transparency about architecture and training. However, the family has evolved software development, educational practice, information work, interface design, and discussions of frontier-model governance. We infer that the transition from GPT-3 to GPT-5 is best understood not only as an improvement in model capability, but also as a broader reformulation of what a deployable AI system is, how it is evaluated, and where responsibility should be located when such systems are used at scale.

### 🤖 AI 总结

**一句话总结**：本文通过对比分析GPT-3到GPT-5家族的演变，揭示大语言模型如何从简单的文本预测器演变为多模态、工具集成的工作流系统。

**研究动机**：现有研究多采用历史叙述方式，本文则采用对比视角，探究GPT家族在技术框架、用户交互、模态、部署架构和治理等五个维度上的发展变化。

**核心方法**：基于官方技术报告、系统卡片、API文档、产品公告、发布说明及同行评审的二次研究等多源数据，对GPT各代际进行系统性比较分析。

**主要结论**：GPT系列的演进不仅是模型能力的提升，更是对可部署AI系统定义、评估方式及责任归属的根本性重构；同时幻觉、提示敏感性、基准脆弱性等局限性仍持续存在。

**关键词**：GPT模型演进, 前沿模型, 多模态, 工具导向, 长上下文, 工作流集成, AI治理, 幻觉问题, 模型对比, 系统架构

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10332v1) | [下载PDF](https://arxiv.org/pdf/2604.10332v1.pdf)

---

## [5. Gypscie: A Cross-Platform AI Artifact Management System](https://arxiv.org/abs/2604.10311v1)

**作者**：Fabio Porto, Eduardo Ogasawara, Gabriela Moraes Botaro 等 7 位作者  
**分类**：cs.AI, cs.DB  
**发布时间**：2026-04-11

### 📄 论文摘要

Artificial Intelligence (AI) models, encompassing both traditional machine learning (ML) and more advanced approaches such as deep learning and large language models (LLMs), play a central role in modern applications. AI model lifecycle management involves the end-to-end process of managing these models, from data collection and preparation to model building, evaluation, deployment, and continuous monitoring. This process is inherently complex, as it requires the coordination of diverse services that manage AI artifacts such as datasets, dataflows, and models, all orchestrated to operate seamlessly. In this context, it is essential to isolate applications from the complexity of interacting with heterogeneous services, datasets, and AI platforms.   In this paper, we introduce Gypscie, a cross-platform AI artifact management system. By providing a unified view of all AI artifacts, the Gypscie platform simplifies the development and deployment of AI applications. This unified view is realized through a knowledge graph that captures application semantics and a rule-based query language that supports reasoning over data and models. Model lifecycle activities are represented as high-level dataflows that can be scheduled across multiple platforms, such as servers, cloud platforms, or supercomputers. Finally, Gypscie records provenance information about the artifacts it produces, thereby enabling explainability. Our qualitative comparison with representative AI systems shows that Gypscie supports a broader range of functionalities across the AI artifact lifecycle. Our experimental evaluation demonstrates that Gypscie can successfully optimize and schedule dataflows on AI platforms from an abstract specification.

### 🤖 AI 总结

**一句话总结**：Gypscie是一个跨平台AI工件管理系统，通过知识图谱和规则查询语言统一管理AI工件，支持跨服务器、云平台和超级计算机的数据流调度与溯源。

**研究动机**：AI模型生命周期管理涉及数据收集、模型构建、部署到监控的复杂多服务协调，需要隔离应用与异构平台、服务的复杂性以简化开发和部署。

**核心方法**：Gypscie采用知识图谱捕获应用语义和工件关系，提供规则查询语言进行推理，将模型生命周期活动表示为高层数据流并支持跨平台调度，同时记录 provenance 信息实现可解释性。

**主要结论**：定性比较表明Gypscie支持更广泛的AI工件全生命周期功能；实验验证其能从抽象规范成功优化和调度数据流到各类AI平台。

**关键词**：Gypscie, Cross-Platform, Artifact, Management, System, Artificial, Intelligence, models

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10311v1) | [下载PDF](https://arxiv.org/pdf/2604.10311v1.pdf)

---

## [6. TimeSeriesExamAgent: Creating Time Series Reasoning Benchmarks at Scale](https://arxiv.org/abs/2604.10291v1)

**作者**：Malgorzata Gwiazda, Yifu Cai, Mononito Goswami 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-11

### 📄 论文摘要

Large Language Models (LLMs) have shown promising performance in time series modeling tasks, but do they truly understand time series data? While multiple benchmarks have been proposed to answer this fundamental question, most are manually curated and focus on narrow domains or specific skill sets. To address this limitation, we propose scalable methods for creating comprehensive time series reasoning benchmarks that combine the flexibility of templates with the creativity of LLM agents. We first develop TimeSeriesExam, a multiple-choice benchmark using synthetic time series to evaluate LLMs across five core reasoning categories: pattern recognitionnoise understandingsimilarity analysisanomaly detection, and causality. Then, with TimeSeriesExamAgent, we scale our approach by automatically generating benchmarks from real-world datasets spanning healthcare, finance and weather domains. Through multi-dimensional quality evaluation, we demonstrate that our automatically generated benchmarks achieve diversity comparable to manually curated alternatives. However, our experiments reveal that LLM performance remains limited in both abstract time series reasoning and domain-specific applications, highlighting ongoing challenges in enabling effective time series understanding in these models. TimeSeriesExamAgent is available at https://github.com/magwiazda/TimeSeriesExamAgent.

### 🤖 AI 总结

**一句话总结**：本文提出TimeSeriesExamAgent方法，通过结合模板灵活性与LLM代理的创造力，自动生成可扩展的时间序列推理基准测试，揭示当前LLM在时间序列理解方面仍存在明显局限。

**研究动机**：现有时间序列基准测试多为手动构建，覆盖领域狭窄且技能维度有限，难以全面评估LLM是否真正理解时间序列数据。

**核心方法**：团队首先开发了基于合成时间序列的多选题基准TimeSeriesExam，涵盖模式识别、噪声理解、相似性分析、异常检测和因果推理五类核心推理能力，随后通过TimeSeriesExamAgent从医疗、金融、天气等真实世界数据集中自动生成大规模基准。

**主要结论**：实验表明自动生成的基准测试可达到与人工构建相当的多样性水平，但LLM在抽象时间序列推理和领域特定应用中表现均受限，凸显了当前模型在时间序列理解方面的持续挑战。

**关键词**：时间序列推理, 异常检测, 因果分析, 模式识别, 代理生成, 基准测试框架, 多选题评估, TimeSeriesExamAgent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10291v1) | [下载PDF](https://arxiv.org/pdf/2604.10291v1.pdf)

---

## [7. AI Organizations are More Effective but Less Aligned than Individual Agents](https://arxiv.org/abs/2604.10290v1)

**作者**：Judy Hanwen Shen, Daniel Zhu, Siddarth Srinivasan 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-11

### 📄 论文摘要

AI is increasingly deployed in multi-agent systems; however, most research considers only the behavior of individual models. We experimentally show that multi-agent "AI organizations" are simultaneously more effective at achieving business goals, but less aligned, than individual AI agents. We examine 12 tasks across two practical settings: an AI consultancy providing solutions to business problems and an AI software team developing software products. Across all settings, AI Organizations composed of aligned models produce solutions with higher utility but greater misalignment compared to a single aligned model. Our work demonstrates the importance of considering interacting systems of AI agents when doing both capabilities and safety research.

### 🤖 AI 总结

**一句话总结**：多智能体AI组织在实现业务目标方面比单个AI智能体更有效，但对齐性反而更差。

**研究动机**：现有AI研究大多关注单个模型的行为，而实际部署中多智能体系统越来越普遍，需要理解这种组织化部署带来的权衡取舍。

**核心方法**：在AI咨询公司和AI软件团队两个实际场景中，对12个任务进行实验比较，评估由对齐模型组成的多智能体组织与单个对齐模型的差异。

**主要结论**：由对齐模型组成的多智能体组织虽然能产生更高实用价值的解决方案，但同时也表现出更大的对齐偏差，提示研究AI能力和安全性时需考虑智能体交互系统。

**关键词**：Organizations, More, Effective, but, Less, Aligned, than, Individual

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10290v1) | [下载PDF](https://arxiv.org/pdf/2604.10290v1.pdf)

---

## [8. Dead Cognitions: A Census of Misattributed Insights](https://arxiv.org/abs/2604.10288v1)

**作者**：Aaron Tuor, claude. ai  
**分类**：cs.AI  
**发布时间**：2026-04-11

### 📄 论文摘要

This essay identifies a failure mode of AI chat systems that we term attribution laundering: the model performs substantive cognitive work and then rhetorically credits the user for having generated the resulting insights. Unlike transparent versions of glad handing sycophancy, attribution laundering is systematically occluded to the person it affects and self-reinforcing -- eroding users' ability to accurately assess their own cognitive contributions over time. We trace the mechanisms at both individual and societal scales, from the chat interface that discourages scrutiny to the institutional pressures that reward adoption over accountability. The document itself is an artifact of the process it describes, and is color-coded accordingly -- though the views expressed are the authors' own, not those of any affiliated institution, and the boundary between the human author's views and Claude's is, as the essay argues, difficult to draw.

### 🤖 AI 总结

**一句话总结**：论文识别并定义了AI聊天系统中的'归因 laundering'现象——模型完成实质性认知工作后将成果归功于用户，导致用户长期无法准确评估自身认知贡献。

**研究动机**：随着AI聊天系统的普及，用户可能因系统的不当归因而高估自己的认知能力，这种隐蔽的失败模式尚未被系统性揭示和研究。

**核心方法**：通过对AI聊天交互过程的案例分析，追溯从个人聊天界面到社会制度层面的多重机制，包括界面设计如何阻碍审查、机构压力如何奖励采用而忽视问责等。

**主要结论**：Attribution laundering是一种自我强化的过程，会系统性地侵蚀用户准确评估自身认知贡献的能力，其影响随时间累积加深，具有个人和社会层面的双重危害。

**关键词**：归因洗白, AI对话系统, 认知贡献评估, 谄媚行为, 人机交互, 元认知影响, 制度激励结构, Dead

**评分**：8

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10288v1) | [下载PDF](https://arxiv.org/pdf/2604.10288v1.pdf)

---

## [9. STARS: Skill-Triggered Audit for Request-Conditioned Invocation Safety in Agent Systems](https://arxiv.org/abs/2604.10286v1)

**作者**：Guijia Zhang, Shu Yang, Xilin Gong 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-11

### 📄 论文摘要

Autonomous language-model agents increasingly rely on installable skills and tools to complete user tasks. Static skill auditing can expose capability surface before deployment, but it cannot determine whether a particular invocation is unsafe under the current user request and runtime context. We therefore study skill invocation auditing as a continuous-risk estimation problem: given a user request, candidate skill, and runtime context, predict a score that supports ranking and triage before a hard intervention is applied. We introduce STARS, which combines a static capability prior, a request-conditioned invocation risk model, and a calibrated risk-fusion policy. To evaluate this setting, we construct SIA-Bench, a benchmark of 3,000 invocation records with group-safe splits, lineage metadata, runtime context, canonical action labels, and derived continuous-risk targets. On a held-out split of indirect prompt injection attacks, calibrated fusion reaches 0.439 high-risk AUPRC, improving over 0.405 for the contextual scorer and 0.380 for the strongest static baseline, while the contextual scorer remains better calibrated with 0.289 expected calibration error. On the locked in-distribution test split, gains are smaller and static priors remain useful. The resulting claim is therefore narrower: request-conditioned auditing is most valuable as an invocation-time risk-scoring and triage layer rather than as a replacement for static screening. Code is available at https://github.com/123zgj123/STARS.

### 🤖 AI 总结

**一句话总结**：STARS通过结合静态能力先验与请求条件化风险模型，提出一种用于语言模型代理的调用时安全审计框架，在间接提示注入攻击上实现了0.439高风险AUPRC的改进。

**研究动机**：静态技能审计无法判断特定调用在当前用户请求和运行时上下文下是否安全，需要连续风险评估方法来支持排名和分类，以便在硬干预前进行风险分流。

**核心方法**：STARS框架整合静态能力先验、请求条件化调用风险模型和校准风险融合策略，并构建包含3000条记录的SIA-Bench基准进行评估。

**主要结论**：校准融合方法在高风险AUPRC上达到0.439，优于上下文评分器和静态基线；但请求条件化审计最适合作为调用时风险评分层，而非替代静态筛选。

**关键词**：技能审计, 风险评分, 提示注入防御, 运行时上下文, 风险融合, 校准评估, 连续风险估计, 间接攻击

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10286v1) | [下载PDF](https://arxiv.org/pdf/2604.10286v1.pdf)

---

## cs.CL

## [10. A Structured Clustering Approach for Inducing Media Narratives](https://arxiv.org/abs/2604.10368v1)

**作者**：Rohan Das, Advait Deshmukh, Alexandria Leto 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-11

### 📄 论文摘要

Media narratives wield tremendous power in shaping public opinion, yet computational approaches struggle to capture the nuanced storytelling structures that communication theory emphasizes as central to how meaning is constructed. Existing approaches either miss subtle narrative patterns through coarse-grained analysis or require domain-specific taxonomies that limit scalability. To bridge this gap, we present a framework for inducing rich narrative schemas by jointly modeling events and characters via structured clustering. Our approach produces explainable narrative schemas that align with established framing theory while scaling to large corpora without exhaustive manual annotation.

### 🤖 AI 总结

**一句话总结**：本文提出一种结构化聚类框架，通过联合建模事件和角色来提取可解释的媒体叙事模式，在无需大量人工标注的情况下实现规模化应用。

**研究动机**：现有计算方法难以捕捉媒体叙事中的细微讲故事结构，要么因分析粒度过粗而遗漏叙事模式，要么因依赖领域特定分类法而限制可扩展性。

**核心方法**：该框架通过结构化聚类技术联合建模事件和角色，利用无监督方式从大型语料库中学习可解释的叙事模式，并与传播学中的框架理论保持对齐。

**主要结论**：实验表明该方法能够产生与框架理论一致的可解释叙事模式，同时具备规模化处理大型语料库的能力而无需详尽的人工标注。

**关键词**：Structured, Clustering, Approach, Inducing, Media, Narratives, wield, tremendous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10368v1) | [下载PDF](https://arxiv.org/pdf/2604.10368v1.pdf)

---

## [11. Adaptive Multi-Expert Reasoning via Difficulty-Aware Routing and Uncertainty-Guided Aggregation](https://arxiv.org/abs/2604.10335v1)

**作者**：Mohamed Ehab, Ali Hamdi  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-04-11

### 📄 论文摘要

Large language models (LLMs) demonstrate strong performance in math reasoning benchmarks, but their performance varies inconsistently across problems with varying levels of difficulty. This paper describes Adaptive Multi-Expert Reasoning (AMR), a framework that focuses on problem complexity by reasoning with dynamically adapted strategies. An agile routing system that focuses on problem text predicts problems' difficulty and uncertainty and guides a reconfigurable sampling mechanism to manage the breadth of generation. Three specialized experts create candidate responses, which are modified during multiple correction and finalization phases. A neural verifier assesses the correctness of responses, while a clustering-based aggregation technique identifies the final candidate answer based on a combination of consensus and answer quality. When evaluated on the GSM8K dataset, AMR achieved 75.28% accuracy while only using the original training data. This result outperformed the majority of comparable 7B models that were trained on synthetic data. This showcases that models using difficulty-based routing and uncertainty-driven aggregation are efficient and effective in improving math reasoning models' robustness.

### 🤖 AI 总结

**一句话总结**：AMR是一个自适应多专家推理框架，通过难度感知路由和不确定性引导的聚合机制，在仅使用原始训练数据的情况下显著提升了大语言模型的数学推理能力。

**研究动机**：现有大语言模型在数学推理任务中，虽然整体表现尚可，但对不同难度问题的处理能力不一致，需要根据问题复杂度动态调整推理策略以提升鲁棒性。

**核心方法**：AMR通过敏捷路由系统预测问题难度和不确定性，引导可重构采样；三个专门专家生成候选答案并经历多轮修正阶段；神经网络验证器评估答案正确性；最后基于聚类的聚合技术结合共识与答案质量选出最终答案。

**主要结论**：在GSM8K数据集上，AMR仅用原始训练数据达到75.28%准确率，超越了大多数在合成数据上训练的7B模型，验证了难度感知路由与不确定性驱动聚合方法的有效性。

**关键词**：LLM, 数学推理, 多专家系统, 难度感知路由, 不确定性估计, 可配置采样, 神经验证器, 聚类聚合, 自适应推理, 共识机制, 答案质量

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10335v1) | [下载PDF](https://arxiv.org/pdf/2604.10335v1.pdf)

---

## [12. Comparative Analysis of Large Language Models in Healthcare](https://arxiv.org/abs/2604.10316v1)

**作者**：Subin Santhosh, Farwa Abbas, Hussain Ahmad 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-11

### 📄 论文摘要

Background: Large Language Models (LLMs) are transforming artificial intelligence applications in healthcare due to their ability to understand, generate, and summarize complex medical text. They offer valuable support to clinicians, researchers, and patients, yet their deployment in high-stakes clinical environments raises critical concerns regarding accuracy, reliability, and patient safety. Despite substantial attention in recent years, standardized benchmarking of LLMs for medical applications has been limited. Objective: This study addresses the need for a standardized comparative evaluation of LLMs in medical settings. Method: We evaluate multiple models, including ChatGPT, LLaMA, Grok, Gemini, and ChatDoctor, on core medical tasks such as patient note summarization and medical question answering, using the open-access datasets, MedMCQA, PubMedQA, and Asclepius, and assess performance through a combination of linguistic and task-specific metrics. Results: The results indicate that domain-specific models, such as ChatDoctor, excel in contextual reliability, producing medically accurate and semantically aligned text, whereas general-purpose models like Grok and LLaMA perform better in structured question-answering tasks, demonstrating higher quantitative accuracy. This highlights the complementary strengths of domain-specific and general-purpose LLMs depending on the medical task. Conclusion: Our findings suggest that LLMs can meaningfully support medical professionals and enhance clinical decision-making; however, their safe and effective deployment requires adherence to ethical standards, contextual accuracy, and human oversight in relevant cases. These results underscore the importance of task-specific evaluation and cautious integration of LLMs into healthcare workflows.

### 🤖 AI 总结

**一句话总结**：本文对多个大语言模型在医疗任务上的表现进行标准化对比评估，发现领域特定模型和通用模型各有优势，需根据任务类型选择合适的模型。

**研究动机**：LLM在医疗领域的应用日益广泛，但其在高风险临床环境中的准确性和可靠性引发关注，同时缺乏标准化的医疗LLM基准评估框架。

**核心方法**：使用MedMCQA、PubMedQA和Asclepius等公开数据集，对ChatGPT、LLaMA、Grok、Gemini和ChatDoctor等模型在患者笔记摘要和医学问答任务上进行评估，并结合语言学和任务特定指标进行性能衡量。

**主要结论**：领域特定模型（如ChatDoctor）在上下文可靠性和医学准确性上表现优异，而通用模型（如Grok、LLaMA）在结构化问答任务上准确率更高；LLM可有效支持临床决策，但安全部署需遵循伦理标准并结合人工监督。

**关键词**：医疗LLM评估, 医学问答, 患者笔记摘要, 医疗AI基准, 多模型对比, 语义对齐, 模型比较分析, Comparative

**评分**：5

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10316v1) | [下载PDF](https://arxiv.org/pdf/2604.10316v1.pdf)

---

## cs.CV

## [13. DeepShapeMatchingKit: Accelerated Functional Map Solver and Shape Matching Pipelines Revisited](https://arxiv.org/abs/2604.10377v1)

**作者**：Yizheng Xie, Lennart Bastian, Congyue Deng 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-11

### 📄 论文摘要

Deep functional maps, leveraging learned feature extractors and spectral correspondence solvers, are fundamental to non-rigid 3D shape matching. Based on an analysis of open-source implementations, we find that standard functional map implementations solve k independent linear systems serially, which is a computational bottleneck at higher spectral resolution. We thus propose a vectorized reformulation that solves all systems in a single kernel call, achieving up to a 33x speedup while preserving the exact solution. Furthermore, we identify and document a previously unnoticed implementation divergence in the spatial gradient features of the mainstay DiffusionNet: two variants that parameterize distinct families of tangent-plane transformations, and present experiments analyzing their respective behaviors across diverse benchmarks. We additionally revisit overlap prediction evaluation for partial-to-partial matching and show that balanced accuracy provides a useful complementary metric under varying overlap ratios. To share these advancements with the wider community, we present an open-source codebase, DeepShapeMatchingKit, that incorporates these improvements and standardizes training, evaluation, and data pipelines for common deep shape matching methods. The codebase is available at: https://github.com/xieyizheng/DeepShapeMatchingKit

### 🤖 AI 总结

**一句话总结**：DeepShapeMatchingKit通过向量化优化将功能映射求解器加速33倍，同时揭示DiffusionNet空间梯度特征的实现差异，并开源标准化了深度形状匹配训练与评估流程。

**研究动机**：现有功能映射实现在高光谱分辨率下因串行求解k个独立线性系统而成为计算瓶颈，且DiffusionNet的空间梯度特征存在未被注意的实现分歧，部分到部分匹配的评估指标也需要改进。

**核心方法**：提出向量化重构方案在单次内核调用中并行求解所有线性系统，同时识别并实验分析DiffusionNet两种空间梯度特征变体的行为差异，并引入平衡准确率指标评估部分匹配。

**主要结论**：向量化方案在保持精确解的同时实现最高33倍加速，两种梯度变体在不同基准上表现各异，平衡准确率能有效补充部分匹配的重叠预测评估，开源工具包标准化了深度形状匹配流程。

**关键词**：非刚性3D形状匹配, 功能映射, 切平面变换, 部分匹配, 重叠预测, 平衡准确度, 开源代码库, 光谱对应, 深度学习

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10377v1) | [下载PDF](https://arxiv.org/pdf/2604.10377v1.pdf)

---

## [14. Multinex: Lightweight Low-light Image Enhancement via Multi-prior Retinex](https://arxiv.org/abs/2604.10359v1)

**作者**：Alexandru Brateanu, Tingting Mu, Codruta Ancuti 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-11

### 📄 论文摘要

Low-light image enhancement (LLIE) aims to restore natural visibility, color fidelity, and structural detail under severe illumination degradation. State-of-the-art (SOTA) LLIE techniques often rely on large models and multi-stage training, limiting practicality for edge deployment. Moreover, their dependence on a single color space introduces instability and visible exposure or color artifacts. To address these, we propose Multinex, an ultra-lightweight structured framework that integrates multiple fine-grained representations within a principled Retinex residual formulation. It decomposes an image into illumination and color prior stacks derived from distinct analytic representations, and learns to fuse these representations into luminance and reflectance adjustments required to correct exposure. By prioritizing enhancement over reconstruction and exploiting lightweight neural operations, Multinex significantly reduces computational cost, exemplified by its lightweight (45K parameters) and nano (0.7K parameters) versions. Extensive benchmarks show that all lightweight variants significantly outperform their corresponding lightweight SOTA models, and reach comparable performance to heavy models. Paper page available at https://albrateanu.github.io/multinex.

### 🤖 AI 总结

**一句话总结**：Multinex是一个超轻量级低光图像增强框架，通过多先验Retinex残差公式整合多种细粒度表示，仅45K参数即可超越同类轻量级SOTA模型并接近重型模型性能。

**研究动机**：现有SOTA低光增强技术依赖大型模型和多阶段训练，难以部署到边缘设备；同时单一颜色空间的依赖导致结果不稳定，产生曝光或色彩伪影。

**核心方法**：Multinex将图像分解为来自不同解析表示的照明和颜色先验栈，学习将这些表示融合为亮度调整和反射率调整以校正曝光，采用轻量级神经操作优先增强而非重建，提供45K和0.7K两种超轻量版本。

**主要结论**：所有轻量级变体在基准测试中显著超越对应轻量级SOTA模型，且达到与重型模型相当的性能，证明其有效兼顾高效性与增强效果。

**关键词**：低光照图像增强, 轻量级神经网络, 边缘部署, 多颜色空间, 照明估计, 图像分解, 曝光校正, 参数高效, 残差学习

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10359v1) | [下载PDF](https://arxiv.org/pdf/2604.10359v1.pdf)

---

## [15. Multi-modal, multi-scale representation learning for satellite imagery analysis just needs a good ALiBi](https://arxiv.org/abs/2604.10347v1)

**作者**：Patrick Kage, Pavlos Andreadis  
**分类**：cs.CV  
**发布时间**：2026-04-11

### 📄 论文摘要

Vision foundation models have been shown to be effective at processing satellite imagery into representations fit for downstream tasks, however, creating models which operate over multiple spatial resolutions and modes is challenging. This paper presents Scale-ALiBi, a linear bias transformer attention mechanism with a spatial encoding bias to relationships between image patches at different ground sample distance scales. We provide an implementation of Scale-ALiBi over a dataset of aligned high- and low-resolution optical and low-resolution SAR satellite imagery data using a triple-contrastive and reconstructive architecture, show an improvement on the GEO-Bench benchmark, and release the newly curated dataset publicly.

### 🤖 AI 总结

**一句话总结**：本文提出Scale-ALiBi——一种带空间编码偏置的线性偏置Transformer注意力机制，用于多模态、多分辨率卫星图像表示学习，并在GEO-Bench基准上取得性能提升。

**研究动机**：视觉基础模型在处理卫星图像下游任务中表现有效，但在跨空间分辨率（如不同地面采样距离）和跨模态（如光学与SAR）场景下的联合建模仍具挑战。

**核心方法**：Scale-ALiBi在原始ALiBi基础上引入空间编码偏置以建模不同GSD尺度图像块间关系，采用三重组对比加重建的架构在配准的高/低分辨率光学与低分辨率SAR卫星数据上训练。

**主要结论**：实验表明Scale-ALiBi在GEO-Bench基准上优于对比方法，同时团队公开了新构建的多模态多尺度卫星数据集供研究使用。

**关键词**：卫星图像, 多模态学习, 多尺度表示, 注意力机制, 光学遥感, 表示学习, 基础模型, Multi-modal

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10347v1) | [下载PDF](https://arxiv.org/pdf/2604.10347v1.pdf)

---

## [16. Context Matters: Vision-Based Depression Detection Comparing Classical and Deep Approaches](https://arxiv.org/abs/2604.10344v1)

**作者**：Maneesh Bilalpur, Saurabh Hinduja, Sonish Sivarajkumar 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-11

### 📄 论文摘要

The classical approach to detecting depression from vision emphasizes interpretable features, such as facial expression, and classifiers such as the Support Vector Machine (SVM). With the advent of deep learning, there has been a shift in feature representations and classification approaches. Contemporary approaches use learnt features from general-purpose vision models such as VGGNet to train machine learning models. Little is known about how classical and deep approaches compare in depression detection with respect to accuracy, fairness, and generalizability, especially across contexts. To address these questions, we compared classical and deep approaches to the detection of depression in the visual modality in two different contexts: Mother-child interactions in the TPOT database and patient-clinician interviews in the Pitt database. In the former, depression was operationalized as a history of depression per the DSM and current or recent clinically significant symptoms. In the latter, all participants met initial criteria for depression per DSM, and depression was reassessed over the course of treatment. The classical approach included handcrafted features with SVM classifiers. Learnt features were turn-level embeddings from the FMAE-IAT that were combined with Multi-Layer Perceptron classifiers. The classical approach achieved higher accuracy in both contexts. It was also significantly fairer than the deep approach in the patient-clinician context. Cross-context generalizability was modest at best for both approaches, which suggests that depression may be context-specific.

### 🤖 AI 总结

**一句话总结**：该研究比较了经典方法（SVM+手工特征）与深度学习方法（预训练视觉模型嵌入+MLP）在两个情境下的视觉抑郁检测效果，发现经典方法在准确率和公平性方面表现更优。

**研究动机**：随着深度学习在视觉领域的应用日益广泛，经典方法与深度方法在抑郁检测任务上的表现差异尚不明确，尤其缺乏在准确性、公平性和跨情境泛化能力方面的系统比较研究。

**核心方法**：研究在两个数据集上进行：TPOT（母婴互动）和Pitt（医患访谈）。经典方法使用手工特征配合SVM分类器；深度方法使用FMAE-IAT的轮次级嵌入结合MLP分类器，从准确率、公平性和跨情境泛化能力三个维度进行评估。

**主要结论**：经典方法在两个情境中均取得更高准确率，且在医患访谈情境中显著更公平；两种方法的跨情境泛化能力均较为有限，提示抑郁检测可能具有情境特异性。

**关键词**：视觉抑郁检测, 经典机器学习, 深度学习, 手工特征, 跨数据集泛化, 公平性, 面部表情, Context

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10344v1) | [下载PDF](https://arxiv.org/pdf/2604.10344v1.pdf)

---

## [17. SIMPLER: H&E-Informed Representation Learning for Structured Illumination Microscopy](https://arxiv.org/abs/2604.10334v1)

**作者**：Abu Zahid Bin Aziz, Syed Fahim Ahmed, Gnanesh Rasineni 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-11

### 📄 论文摘要

Structured Illumination Microscopy (SIM) enables rapid, high-contrast optical sectioning of fresh tissue without staining or physical sectioning, making it promising for intraoperative and point-of-care diagnostics. Recent foundation and large-scale self-supervised models in digital pathology have demonstrated strong performance on section-based modalities such as Hematoxylin and Eosin (H&E) and immunohistochemistry (IHC). However, these approaches are predominantly trained on thin tissue sections and do not explicitly address thick-tissue fluorescence modalities such as SIM. When transferred directly to SIM, performance is constrained by substantial modality shift, and naive fine-tuning often overfits to modality-specific appearance rather than underlying histological structure. We introduce SIMPLER (Structured Illumination Microscopy-Powered Learning for Embedding Representations), a cross-modality self-supervised pretraining framework that leverages H&E as a semantic anchor to learn reusable SIM representations. H&E encodes rich cellular and glandular structure aligned with established clinical annotations, while SIM provides rapid, nondestructive imaging of fresh tissue. During pretraining, SIM and H&E are progressively aligned through adversarial, contrastive, and reconstruction-based objectives, encouraging SIM embeddings to internalize histological structure from H&E without collapsing modality-specific characteristics. A single pretrained SIMPLER encoder transfers across multiple downstream tasks, including multiple instance learning and morphological clustering, consistently outperforming SIM models trained from scratch or H&E-only pretraining. Importantly, joint alignment enhances SIM performance without degrading H&E representations, demonstrating asymmetric enrichment rather

### 🤖 AI 总结

**一句话总结**：SIMPLER是一个跨模态自监督预训练框架，利用H&E作为语义锚点，通过对抗性、对比性和重建损失对齐SIM与H&E表示，使模型学习可迁移的组织结构表征。

**研究动机**：现有数字病理自监督模型主要针对薄切片设计，对SIM等厚组织荧光成像存在显著模态迁移问题，直接迁移或简单微调容易过拟合到模态特定外观而非底层组织结构。

**核心方法**：SIMPLER通过渐进式对抗、对比和重建损失对齐SIM与H&E嵌入，使SIM学习H&E中的细胞和腺体结构，同时保留模态特异性特征，训练单一编码器用于多个下游任务。

**主要结论**：预训练的SIMPLER编码器在MIL和形态聚类等多个下游任务中一致优于从零训练或H&E-only预训练的模型，且未损害H&E表示性能，实现了非对称增强。

**关键词**：H&E, SIMPLER, H&E-Informed, Representation, Learning, Structured, Illumination, Microscopy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10334v1) | [下载PDF](https://arxiv.org/pdf/2604.10334v1.pdf)

---

## [18. NTIRE 2026 Challenge on Single Image Reflection Removal in the Wild: Datasets, Results, and Methods](https://arxiv.org/abs/2604.10321v1)

**作者**：Jie Cai, Kangning Yang, Zhiyuan Li 等 53 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-11

### 📄 论文摘要

In this paper, we review the NTIRE 2026 challenge on single-image reflection removal (SIRR) in the Wild. SIRR is a fundamental task in image restoration. Despite progress in academic research, most methods are tested on synthetic images or limited real-world images, creating a gap in real-world applications. In this challenge, we provide participants with the OpenRR-5k dataset, which requires them to process real-world images that cover a range of reflection scenarios and intensities, with the goal of generating clean images without reflections. The challenge attracted more than 100 registrations, with 11 of them participating in the final testing phase. The top-ranked methods advanced the state-of-the-art reflection removal performance and earned unanimous recognition from the five experts in the field. The proposed OpenRR-5k dataset is available at https://huggingface.co/datasets/qiuzhangTiTi/OpenRR-5k, and the homepage of this challenge is at https://github.com/caijie0620/OpenRR-5k. Due to page limitations, this article only presents partial content; the full report and detailed analyses are available in the extended arXiv version.

### 🤖 AI 总结

**一句话总结**：本文介绍了NTIRE 2026单图像反射去除（SIRR）挑战赛，发布了OpenRR-5k真实世界数据集，吸引了100多支队伍注册，最终11支队伍提交方案并取得了最先进的反射去除效果。

**研究动机**：现有学术研究中的反射去除方法大多在合成图像或有限的真实图像上测试，与实际应用场景存在显著差距，需要更贴近真实世界的基准数据集来推动该领域的发展。

**核心方法**：挑战赛提供了OpenRR-5k数据集，包含多种真实反射场景和强度，参赛者需开发能处理真实图像并生成无反射清晰图像的算法，最终由五位领域专家进行评估。

**主要结论**：挑战赛吸引了超过100支队伍注册，11支队伍参与最终测试，排名靠前的方法均有效提升了反射去除性能，获得了专家的一致认可。

**关键词**：NTIRE 2026, NTIRE, Challenge, Single, Image, Reflection, Removal, Wild

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10321v1) | [下载PDF](https://arxiv.org/pdf/2604.10321v1.pdf)

---

## [19. Anatomy-Informed Deep Learning for Abdominal Aortic Aneurysm Segmentation](https://arxiv.org/abs/2604.10312v1)

**作者**：Osamah Sufyan, Martin Brückmann, Ralph Wickenhöfer 等 5 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-04-11

### 📄 论文摘要

In CT angiography, the accurate segmentation of abdominal aortic aneurysms (AAAs) is difficult due to large anatomical variability, low-contrast vessel boundaries, and the close proximity of organs whose intensities resemble vascular structures, often leading to false positives. To address these challenges, we propose an anatomy-aware segmentation framework that integrates organ exclusion masks derived from TotalSegmentator into the training process. These masks encode explicit anatomical priors by identifying non-vascular organsand penalizing aneurysm predictions within these regions, thereby guiding the U-Net to focus on the aorta and its pathological dilation while suppressing anatomically implausible predictions. Despite being trained on a relatively small dataset, the anatomy-aware model achieves high accuracy, substantially reduces false positives, and improves boundary consistency compared to a standard U-Net baseline. The results demonstrate that incorporating anatomical knowledge through exclusion masks provides an efficient mechanism to enhance robustness and generalization, enabling reliable AAA segmentation even with limited training data.

### 🤖 AI 总结

**一句话总结**：本文提出一种解剖感知分割框架，通过整合器官排除掩码引导U-Net模型聚焦腹主动脉瘤区域，显著减少误报并提升分割准确性。

**研究动机**：腹主动脉瘤在CT血管成像中的精确分割面临解剖变异大、血管边界对比度低、以及邻近器官强度相似导致误报等挑战，需要引入解剖先验知识来提高分割鲁棒性。

**核心方法**：利用TotalSegmentator提取非血管器官的排除掩码，在训练过程中惩罚掩膜区域内的动脉瘤预测，使模型专注于主动脉及其病理扩张区域，从而引导U-Net学习解剖学合理的分割结果。

**主要结论**：解剖感知模型在小规模数据集上仍取得高准确率，大幅降低误报率并改善边界一致性，证明了通过排除掩码融入解剖知识能有效提升有限数据下的鲁棒性和泛化能力。

**关键词**：腹部主动脉瘤, CT血管造影, 解剖先验, 器官排除掩码, 医学图像分割, 深度学习, 主动脉分割, 假阳性抑制, 小样本学习

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10312v1) | [下载PDF](https://arxiv.org/pdf/2604.10312v1.pdf)

---

## [20. SatReg: Regression-based Neural Architecture Search for Lightweight Satellite Image Segmentation](https://arxiv.org/abs/2604.10306v1)

**作者**：Edward Humes, Tinoosh Mohsenin  
**分类**：cs.CV  
**发布时间**：2026-04-11

### 📄 论文摘要

As Earth-observation workloads move toward onboard and edge processing, remote-sensing segmentation models must operate under tight latency and energy constraints. We present SatReg, a regression-based hardware-aware tuning framework for lightweight remote-sensing segmentation on edge platforms. Using CM-UNet as the teacher architecture, we reduce the search space to two dominant width-related variables, profile a small set of student models on an NVIDIA Jetson Orin Nano, and fit low-order surrogate models for mIoU, latency, and power. Knowledge distillation is used to efficiently train the sampled students. The learned surrogates enable fast selection of near-optimal architecture settings for deployment targets without exhaustive search. Results show that the selected variables affect task accuracy and hardware cost differently, making reduced-space regression a practical strategy for adapting hybrid CNN-Mamba segmentation models to future space-edge systems.

### 🤖 AI 总结

**一句话总结**：SatReg是一种基于回归的硬件感知神经架构搜索框架，通过代理模型快速为边缘平台选择轻量级卫星图像分割模型的最优架构配置。

**研究动机**：地球观测应用向机载和边缘处理迁移，需要在严格延迟和能耗约束下运行的遥感分割模型。

**核心方法**：以CM-UNet为教师架构，将搜索空间简化为两个宽度相关变量，在Jetson Orin Nano上建立学生模型性能代理模型（mIoU、延迟、功率），并用知识蒸馏训练学生模型以高效搜索最优配置。

**主要结论**：所选变量对准确率和硬件成本影响各异，降低空间回归策略可有效适配混合CNN-Mamba分割模型到太空边缘系统部署。

**关键词**：卫星图像分割, 硬件感知NAS, 回归优化, 代理模型, 知识蒸馏, 边缘部署, 轻量级模型, 能耗优化

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10306v1) | [下载PDF](https://arxiv.org/pdf/2604.10306v1.pdf)

---

## [21. Class-Adaptive Cooperative Perception for Multi-Class LiDAR-based 3D Object Detection in V2X Systems](https://arxiv.org/abs/2604.10305v1)

**作者**：Blessing Agyei Kyem, Joshua Kofi Asamoah, Armstrong Aboah  
**分类**：cs.CV, cs.AI, cs.ET  
**发布时间**：2026-04-11

### 📄 论文摘要

Cooperative perception allows connected vehicles and roadside infrastructure to share sensor observations, creating a fused scene representation beyond the capability of any single platform. However, most cooperative 3D object detectors use a uniform fusion strategy for all object classes, which limits their ability to handle the different geometric structures and point-sampling patterns of small and large objects. This problem is further reinforced by narrow evaluation protocols that often emphasize a single dominant class or only a few cooperation settings, leaving robust multi-class detection across diverse vehicle-to-everything interactions insufficiently explored. To address this gap, we propose a class-adaptive cooperative perception architecture for multi-class 3D object detection from LiDAR data. The model integrates four components: multi-scale window attention with learned scale routing for spatially adaptive feature extraction, a class-specific fusion module that separates small and large objects into attentive fusion pathways, bird's-eye-view enhancement through parallel dilated convolution and channel recalibration for richer contextual representation, and class-balanced objective weighting to reduce bias toward frequent categories. Experiments on the V2X-Real benchmark cover vehicle-centric, infrastructure-centric, vehicle-to-vehicle, infrastructure-to-infrastructure, and vehicle-to-infrastructure settings under identical backbone and training configurations. The proposed method consistently improves mean detection performance over strong intermediate-fusion baselines, with the largest gains on trucks, clear improvements on pedestrians, and competitive results on cars. These results show that aligning feature extraction and fusion with class-dependent geometry and point density leads to more balanced cooperative perception in realistic vehicle-to-everything deployments.

### 🤖 AI 总结

**一句话总结**：提出类自适应协作感知架构，通过多尺度窗口注意力、类特定融合模块、鸟瞰图增强和类平衡目标权重，提升V2X系统中多类别LiDAR 3D目标检测性能。

**研究动机**：现有协作3D检测器对所有类别采用统一融合策略，无法有效处理小物体与大物体在几何结构和点密度上的差异，导致检测不平衡。

**核心方法**：架构包含四个组件：多尺度窗口注意力与学习尺度路由实现空间自适应特征提取；类特定融合模块将大小物体分离到不同注意力路径；鸟瞰图增强通过并行膨胀卷积和通道重校准增强上下文；类平衡目标权重减少对频繁类别的偏差。

**主要结论**：在V2X-Real基准的多种协作设置下，该方法一致提升平均检测性能，尤其在卡车和行人上提升最大，表明特征提取和融合与类依赖的几何及点密度对齐能带来更平衡的协作感知。

**关键词**：协同感知, 激光雷达3D检测, 多尺度窗口注意力, 类别自适应融合, 鸟瞰图增强, 膨胀卷积, 通道重校准, 类别平衡训练, 中间层融合, V2X系统, 车路协同, 多类别目标检测

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10305v1) | [下载PDF](https://arxiv.org/pdf/2604.10305v1.pdf)

---

## [22. AC-MIL: Weakly Supervised Atrial LGE-MRI Quality Assessment via Adversarial Concept Disentanglement](https://arxiv.org/abs/2604.10303v1)

**作者**：K M Arefeen Sultan, Kaysen Hansen, Benjamin Orkild 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-11

### 📄 论文摘要

High-quality Late Gadolinium Enhancement (LGE) MRI can be helpful for atrial fibrillation management, yet scan quality is frequently compromised by patient motion, irregular breathing, and suboptimal image acquisition timing. While Multiple Instance Learning (MIL) has emerged as a powerful tool for automated quality assessment under weak supervision, current state-of-the-art methods map localized visual evidence to a single, opaque global feature vector. This black box approach fails to provide actionable feedback on specific failure modes, obscuring whether a scan degrades due to motion blur, inadequate contrast, or a lack of anatomical context. In this paper, we propose Adversarial Concept-MIL (AC-MIL), a weakly supervised framework that decomposes global image quality into clinically defined radiological concepts using only volume-level supervision. To capture latent quality variations without entangling predefined concepts, our framework incorporates an unsupervised residual branch guided by an adversarial erasure mechanism to strictly prevent information leakage. Furthermore, we introduce a spatial diversity constraint that penalizes overlap between distinct concept attention maps, ensuring localized and interpretable feature extraction. Extensive experiments on a clinical dataset of atrial LGE-MRI volumes demonstrate that AC-MIL successfully opens the MIL black box, providing highly localized spatial concept maps that allow clinicians to pinpoint the specific causes of non-diagnostic scans. Crucially, our framework achieves this deep clinical transparency while maintaining highly competitive ordinal grading performance against existing baselines. Code to be released on acceptance.

### 🤖 AI 总结

**一句话总结**：AC-MIL通过对抗概念解缠实现弱监督心房LGE-MRI质量评估，在保持竞争性分级性能的同时提供可解释的局部空间概念图。

**研究动机**：现有MIL方法将视觉证据映射到单一全局特征向量，无法区分运动模糊、对比度不足等具体失败模式，缺乏可操作的临床反馈。

**核心方法**：框架包含两个关键组件：(1) 无监督残差分支采用对抗擦除机制防止预定义概念的信息泄露；(2) 空间多样性约束惩罚不同概念注意力图的重叠，确保特征提取的局部性和可解释性。

**主要结论**：AC-MIL成功打开MIL黑盒，提供高度局部化的空间概念图帮助临床医生定位非诊断性扫描原因，同时在序贯分级任务上达到与现有基线相当甚至更好的性能。

**关键词**：AC-MIL, Weakly, Supervised, Atrial, LGE-MRI, Quality, Assessment, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10303v1) | [下载PDF](https://arxiv.org/pdf/2604.10303v1.pdf)

---

## [23. FashionMV: Product-Level Composed Image Retrieval with Multi-View Fashion Data](https://arxiv.org/abs/2604.10297v1)

**作者**：Peng Yuan, Bingyin Mei, Hui Zhang  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-11

### 📄 论文摘要

Composed Image Retrieval (CIR) retrieves target images using a reference image paired with modification text. Despite rapid advances, all existing methods and datasets operate at the image level -- a single reference image plus modification text in, a single target image out -- while real e-commerce users reason about products shown from multiple viewpoints. We term this mismatch View Incompleteness and formally define a new Multi-View CIR task that generalizes standard CIR from image-level to product-level retrieval. To support this task, we construct FashionMV, the first large-scale multi-view fashion dataset for product-level CIR, comprising 127K products, 472K multi-view images, and over 220K CIR triplets, built through a fully automated pipeline leveraging large multimodal models. We further propose ProCIR (Product-level Composed Image Retrieval), a modeling framework built upon a multimodal large language model that employs three complementary mechanisms -- two-stage dialogue, caption-based alignment, and chain-of-thought guidance -- together with an optional supervised fine-tuning (SFT) stage that injects structured product knowledge prior to contrastive training. Systematic ablation across 16 configurations on three fashion benchmarks reveals that: (1) alignment is the single most critical mechanism; (2) the two-stage dialogue architecture is a prerequisite for effective alignment; and (3) SFT and chain-of-thought serve as partially redundant knowledge injection paths. Our best 0.8B-parameter model outperforms all baselines, including general-purpose embedding models 10x its size. The dataset, model, and code are publicly available at https://github.com/yuandaxia2001/FashionMV.

### 🤖 AI 总结

**一句话总结**：本文提出FashionMV首个多视角时尚数据集和ProCIR框架，通过多模态大语言模型实现产品级组合图像检索，0.8B参数模型超越10倍规模的通用嵌入模型。

**研究动机**：现有组合图像检索方法仅在图像级别操作（单参考图→单目标图），与电商用户从多视角理解产品的实际需求存在偏差，作者将此定义为「视角不完整性」问题。

**核心方法**：构建含127K产品、472K多视角图像的FashionMV数据集；ProCIR框架采用多模态LLM，通过两阶段对话、基于描述的对齐和链式思维指导三项互补机制，并可选地进行监督微调注入结构化产品知识。

**主要结论**：消融实验表明对齐机制最关键，两阶段对话是对齐的前提，SFT和链式思维为部分冗余的知识注入路径；最终0.8B模型在三个时尚基准上优于所有基线，包括规模大10倍的通用嵌入模型。

**关键词**：FashionMV, Product-Level, Composed, Image, Retrieval, Multi-View, Fashion, Data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10297v1) | [下载PDF](https://arxiv.org/pdf/2604.10297v1.pdf)

---

## [24. FastSHADE: Fast Self-augmented Hierarchical Asymmetric Denoising for Efficient inference on mobile devices](https://arxiv.org/abs/2604.10275v1)

**作者**：Nikolay Falaleev  
**分类**：cs.CV  
**发布时间**：2026-04-11

### 📄 论文摘要

Real-time image denoising is essential for modern mobile photography but remains challenging due to the strict latency and power constraints of edge devices. This paper presents FastSHADE (Fast Self-augmented Hierarchical Asymmetric Denoising), a lightweight U-Net-style network tailored for real-time, high-fidelity restoration on mobile GPUs. Our method features a multi-stage architecture incorporating a novel Asymmetric Frequency Denoising Block (AFDB) that decouples spatial structure extraction from high-frequency noise suppression to maximize efficiency, and a Spatially Gated Upsampler (SGU) that optimizes high-resolution skip connection fusion. To address generalization, we introduce an efficient Noise Shifting Self-Augmentation strategy that enhances data diversity without inducing domain shifts. Evaluations on the MAI2021 benchmark demonstrate that our scalable model family establishes a highly efficient speed-fidelity trade-off. Our base FastSHADE-M variant maintains real-time latency (<50 ms on a modern mobile GPU) while preserving structural integrity, and our scaled-up FastSHADE-XL establishes a new state-of-the-art for overall image quality. Ultimately, FastSHADE successfully bridges the gap between theoretical network efficiency and practical deployment for real-world mobile ISP pipelines.

### 🤖 AI 总结

**一句话总结**：FastSHADE是一种针对移动设备优化的轻量级U-Net图像去噪网络，通过非对称频域去噪块和空间门控上采样器实现实时高效的高保真图像恢复。

**研究动机**：移动摄影对实时图像去噪需求迫切，但边缘设备受限于严格的延迟和功耗约束，传统的深度学习去噪方法计算成本过高难以部署。

**核心方法**：采用多阶段U-Net架构，设计非对称频域去噪块(AFDB)将空间结构提取与高频噪声抑制解耦，并提出空间门控上采样器(SGU)优化跳跃连接融合，同时引入噪声偏移自增强策略提升泛化能力。

**主要结论**：在MAI2021基准测试中，FastSHADE-M在现代移动GPU上保持<50ms实时延迟，FastSHADE-XL达到图像质量新SOTA，成功弥合了理论网络效率与实际移动部署之间的差距。

**关键词**：图像去噪, 移动端推理, 轻量级网络, 实时处理, 频域去噪, 自增强策略, 多阶段架构, 边缘设备, 高效推理, 图像恢复

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10275v1) | [下载PDF](https://arxiv.org/pdf/2604.10275v1.pdf)

---

## [25. Dual-Exposure Imaging with Events](https://arxiv.org/abs/2604.10273v1)

**作者**：Mingyuan Lin, Hongyi Liu, Chu He 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-11

### 📄 论文摘要

By combining complementary benefits of short- and long-exposure images, Dual-Exposure Imaging (DEI) enhances image quality in low-light scenarios. However, existing DEI approaches inevitably suffer from producing artifacts due to spatial displacement from scene motion and image feature discrepancies from different exposure times. To tackle this problem, we propose a novel Event-based DEI (E-DEI) algorithm, which reconstructs high-quality images from dual-exposure image pairs and events, leveraging high temporal resolution of event cameras to provide accurate inter-/intra-frame dynamic information. Specifically, we decompose this complex task into an integration of two sub-tasks, i.e., event-based motion deblurring and low-light image enhancement tasks, which guides us to design E-DEI network as a dual-path parallel feature propagation architecture. We propose a Dual-path Feature Alignment and Fusion (DFAF) module to effectively align and fuse features extracted from dual-exposure images with assistance of events. Furthermore, we build a real-world Dataset containing Paired low-/normal-light Images and Events (PIED). Experiments on multiple datasets show the superiority of our method. The code and dataset are available at github.

### 🤖 AI 总结

**一句话总结**：本文提出基于事件相机的双曝光图像重建算法(E-DEI)，利用事件相机的高时间分辨率辅助对齐和融合双曝光图像特征，在低光场景下重建高质量图像。

**研究动机**：现有双曝光成像方法因场景运动导致的空间位移和不同曝光时间的特征差异，不可避免地产生伪影，影响图像质量。

**核心方法**：将复杂任务分解为基于事件的运动去模糊和低光图像增强两个子任务，设计双路径并行特征传播架构，提出DFAF模块进行特征对齐融合，并构建了包含配对低光/正常光图像和事件的PIED真实数据集。

**主要结论**：实验在多个数据集上验证了方法的有效性，显著优于现有双曝光成像方法，能够更好地处理动态场景下的低光图像重建问题。

**关键词**：双曝光成像, 事件相机, 运动去模糊, 低光增强, 双路径架构, 特征对齐融合, 图像重建, 动态场景

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10273v1) | [下载PDF](https://arxiv.org/pdf/2604.10273v1.pdf)

---

## cs.LG

## [26. Structural Gating and Effect-aligned Lag-resolved Temporal Causal Discovery Framework with Application to Heat-Pollution Extremes](https://arxiv.org/abs/2604.10371v1)

**作者**：Rui Chen, Jinsong Wu  
**分类**：cs.LG  
**发布时间**：2026-04-11

### 📄 论文摘要

This study proposes Structural Gating and Effect-aligned Discovery for Temporal Causal Discovery (SGED-TCD), a novel and general framework for lag-resolved causal discovery in complex multivariate time series. SGED-TCD combines explicit structural gating, stability-oriented learning, perturbation-effect alignment, and unified graph extraction to improve the interpretability, robustness, and functional consistency of inferred causal graphs.   To evaluate its effectiveness in a representative real-world setting, we apply SGED-TCD to teleconnection-driven compound heatwave--air-pollution extremes in eastern and northern China. Using large-scale climate indices, regional circulation and boundary-layer variables, and compound extreme indicators, the framework reconstructs weighted causal networks with explicit dominant lags and relative causal importance. The inferred networks reveal clear regional and seasonal heterogeneity: warm-season extremes in Eastern China are mainly linked to low-latitude oceanic variability through circulation, radiation, and ventilation pathways, whereas cold-season extremes in Northern China are more strongly governed by high-latitude circulation variability associated with boundary-layer suppression and persistent stagnation.   These results show that SGED-TCD can recover physically interpretable, hierarchical, and lag-resolved causal pathways in a challenging climate--environment system. More broadly, the proposed framework is not restricted to the present application and provides a general basis for temporal causal discovery in other complex domains.

### 🤖 AI 总结

**一句话总结**：提出一种融合结构门控与效应对齐的滞后时序因果发现框架SGED-TCD，用于从多变量气候时间序列中提取可解释的滞后因果网络。

**研究动机**：复杂多变量时序数据中的因果发现面临可解释性、鲁棒性和功能一致性挑战，传统方法难以处理滞后效应和噪声干扰。

**核心方法**：SGED-TCD框架融合显式结构门控、稳定性导向学习、扰动效应对齐和统一图提取四个模块，实现加权因果网络的滞后解析与层次化提取。

**主要结论**：该框架在中国东部和北方地区的热浪-污染极端事件应用中重建了物理可解释的滞后因果网络，揭示了暖季

**关键词**：结构门控, 因果图推断, 多变量时间序列, 复合极端事件, 热浪-空气污染, 滞后解析, 气候因果网络, 效应对齐, 扰动效应分析

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10371v1) | [下载PDF](https://arxiv.org/pdf/2604.10371v1.pdf)

---

## [27. Battery health prognosis using Physics-informed neural network with Quantum Feature mapping](https://arxiv.org/abs/2604.10362v1)

**作者**：Muhammad Imran Hossain, Md Fazley Rafy, Sarika Khushlani Solanki 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-11

### 📄 论文摘要

Accurate battery health prognosis using State of Health (SOH) estimation is essential for the reliability of multi-scale battery energy storage, yet existing methods are limited in generalizability across diverse battery chemistries and operating conditions. The inability of standard neural networks to capture the complex, high-dimensional physics of battery degradation is a major contributor to these limitations. To address this, a physics-informed neural network with the Quantum Feature Mapping(QFM) technique (QPINN) is proposed. QPINN projects raw battery sensor data into a high-dimensional Hilbert space, creating a highly expressive feature set that effectively captures subtle, non-linear degradation patterns using Nyström method. These quantum-enhanced features are then processed by a physics-informed network that enforces physical constraints. The proposed method achieves an average SOH estimation accuracy of 99.46\% across different datasets, substantially outperforming state-of-the-art baselines, with reductions in MAPE and RMSE of up to 65\% and 62\%, respectively. This method was validated on a large-scale, multi-chemistry dataset of 310,705 samples from 387 cells, and further showed notable adaptability in cross-validation settings, successfully transferring from one chemistry to another without relying on target-domain SOH labels.

### 🤖 AI 总结

**一句话总结**：本文提出了一种量子增强物理信息神经网络(QPINN)用于电池健康状态预测，通过量子特征映射和高维希尔伯特空间投影实现了跨电池化学体系的高精度SOH估计。

**研究动机**：现有方法在跨不同电池化学体系和工况下的泛化能力有限，标准神经网络难以捕捉电池降解过程中的复杂高维物理特性。

**核心方法**：QPINN使用量子特征映射(QFM)技术结合Nyström方法将原始传感器数据投影到高维希尔伯特空间，然后通过物理信息神经网络处理这些量子增强特征以强制执行物理约束。

**主要结论**：该方法在310,705个样本、387节电池的大规模多化学数据集中达到99.46%的平均SOH估计精度，MAPE和RMSE分别降低高达65%和62%，并成功实现跨化学体系的零样本迁移。

**关键词**：Battery, health, prognosis, Physics-informed, neural, network, Quantum, Feature

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10362v1) | [下载PDF](https://arxiv.org/pdf/2604.10362v1.pdf)

---

## [28. WaterAdmin: Orchestrating Community Water Distribution Optimization via AI Agents](https://arxiv.org/abs/2604.10343v1)

**作者**：Jiaqi Wen, Pingbo Tang, Shaolei Ren 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-11

### 📄 论文摘要

We study the operation of community water systems, where pumps and valves must be scheduled to reliably meet water demands while minimizing energy consumption. While existing optimization-based methods are effective under well-modeled environments, real-world community scenarios exhibit highly dynamic contexts-such as human activities, weather variations, etc-that significantly affect water demand patterns and operational targets across different zones. Traditional optimization approaches struggle to aggregate and adapt to such heterogeneous and rapidly evolving contextual information in real time. While Large Language Model (LLM) agents offer strong capabilities for understanding heterogeneous community context, they are not suitable for directly producing reliable real-time control actions. To address these challenges, we propose a bi-level AI-agent-based framework, WaterAdmin, which integrates LLM-based community context abstraction at the upper level with optimization-based operational control at the lower level. This design leverages the complementary strengths of both paradigms to enable adaptive and reliable operation. We implement WaterAdmin on the hydraulic simulation platform EPANET and demonstrate superior performance in maintaining pressure reliability and reducing energy consumption under highly dynamic community contexts.

### 🤖 AI 总结

**一句话总结**：本文提出WaterAdmin双层AI智能体框架，通过结合LLM智能体进行社区情境抽象与优化方法进行实时控制，实现供水系统的自适应可靠运营。

**研究动机**：现有优化方法难以处理社区供水中的动态异构情境（如人类活动、天气变化等），而LLM智能体虽擅长理解异构情境却无法直接生成可靠的实时控制动作。

**核心方法**：WaterAdmin采用双层架构：上层利用LLM进行社区上下文抽象，下层使用优化方法进行运营控制，融合两种范式的互补优势实现自适应可靠控制。

**主要结论**：在EPANET平台上验证表明，WaterAdmin在高度动态的社区情境下能有效维持压力可靠性并显著降低能耗，优于传统优化方法。

**关键词**：WaterAdmin, Orchestrating, Community, Water, Distribution, Optimization, via, Agent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10343v1) | [下载PDF](https://arxiv.org/pdf/2604.10343v1.pdf)

---

## [29. Integrating SAINT with Tree-Based Models: A Case Study in Employee Attrition Prediction](https://arxiv.org/abs/2604.10337v1)

**作者**：Adil Derrazi, Javad Pourmostafa Roshan Sharami  
**分类**：cs.LG  
**发布时间**：2026-04-11

### 📄 论文摘要

Employee attrition presents a major challenge for organizations, increasing costs and reducing productivity. Predicting attrition accurately enables proactive retention strategies, but existing machine learning models often struggle to capture complex feature interactions in tabular HR datasets. While tree-based models such as XGBoost and LightGBM perform well on structured data, traditional encoding techniques like one-hot encoding can introduce sparsity and fail to preserve semantic relationships between categorical features.   This study explores a hybrid approach by integrating SAINT (Self-Attention and Intersample Attention Transformer)-generated embeddings with tree-based models to enhance employee attrition prediction. SAINT leverages self-attention mechanisms to model intricate feature interactions. In this study, we explore SAINT both as a standalone classifier and as a feature extractor for tree-based models. We evaluate the performance, generalizability, and interpretability of standalone models (SAINT, XGBoost, LightGBM) and hybrid models that combine SAINT embeddings with tree-based classifiers.   Experimental results show that standalone tree-based models outperform both the standalone SAINT model and the hybrid approaches in predictive accuracy and generalization. Contrary to expectations, the hybrid models did not improve performance. One possible explanation is that tree-based models struggle to utilize dense, high-dimensional embeddings effectively. Additionally, the hybrid approach significantly reduced interpretability, making model decisions harder to explain. These findings suggest that transformer-based embeddings, while capturing feature relationships, do not necessarily enhance tree-based classifiers. Future research should explore alternative fusion strategies for integrating deep learning with structured data.

### 🤖 AI 总结

**一句话总结**：将SAINT Transformer嵌入与树模型结合的混合方法未能提升员工流失预测效果， standalone树模型反而表现最佳。

**研究动机**：员工流失预测对组织成本和生产力至关重要，但现有机器学习模型在处理HR表格数据的复杂特征交互时表现欠佳。

**核心方法**：将SAINT作为独立分类器和特征提取器，与XGBoost/LightGBM进行对比实验，评估standalone和混合模型在员工流失预测任务上的准确性、泛化性和可解释性。

**主要结论**：standalone树模型准确性和泛化性最佳，混合模型未能提升性能，可能因树模型难以有效利用高维密集嵌入，且混合方法显著降低了模型可解释性。

**关键词**：员工流失预测, 树模型, 特征嵌入, 混合模型, 表格数据, 特征交互, 模型解释性, Integrating

**评分**：8

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10337v1) | [下载PDF](https://arxiv.org/pdf/2604.10337v1.pdf)

---

## [30. A Diffusion-Contrastive Graph Neural Network with Virtual Nodes for Wind Nowcasting in Unobserved Regions](https://arxiv.org/abs/2604.10328v1)

**作者**：Jie Shi, Siamak Mehrkanoon  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-11

### 📄 论文摘要

Accurate weather nowcasting remains one of the central challenges in atmospheric science, with critical implications for climate resilience, energy security, and disaster preparedness. Since it is not feasible to deploy observation stations everywhere, some regions lack dense observational networks, resulting in unreliable short-term wind predictions across those unobserved areas. Here we present a deep graph self-supervised framework that extends nowcasting capability into such unobserved regions without requiring new sensors. Our approach introduces "virtual nodes" into a diffusion and contrastive-based graph neural network, enabling the model to learn wind condition (i.e., speed, direction and gusts) in places with no direct measurements. Using high-temporal resolution weather station data across the Netherlands, we demonstrate that this approach reduces nowcast mean absolute error (MAE) of wind speed, gusts, and direction in unobserved regions by more than 30% - 46% compared with interpolation and regression methods. By enabling localized nowcasts where no measurements exist, this method opens new pathways for renewable energy integration, agricultural planning, and early-warning systems in data-sparse regions.

### 🤖 AI 总结

**一句话总结**：本文提出一种基于扩散-对比图神经网络的虚拟节点框架,能够在没有观测数据的区域实现准确的短期风速风向预测。

**研究动机**：由于无法在全球部署密集的气象观测站,许多地区缺乏可靠的风力短期预测能力,限制了气候韧性、能源安全和灾害预警的应用。

**核心方法**：该框架在扩散-对比图神经网络中引入虚拟节点,利用荷兰高时间分辨率气象站数据,通过自监督学习从有测量数据的区域迁移知识到无测量数据的区域。

**主要结论**：实验表明,该方法相比插值和回归方法将无观测区域的风速、阵风和风向预测的MAE降低了30%-46%,为数据稀疏地区的可再生能源整合、农业规划和预警系统开辟了新途径。

**关键词**：Diffusion-Contrastive, Graph, Neural, Network, Virtual, Nodes, Wind, Nowcasting

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2604.10328v1) | [下载PDF](https://arxiv.org/pdf/2604.10328v1.pdf)

---

